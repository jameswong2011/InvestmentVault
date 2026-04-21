---
type: skill-rationale
skill: /graph
purpose: Design rationale and historical fix context for /graph. NOT loaded at invocation — SKILL.md references by §N.M.
last_reviewed: 2026-04-20
---

# /graph Design Rationale

> SKILL.md contains operational rules. This file explains the watermark semantics, reverse-index drift prevention, tool-call budgets, the T7.3 cache-field addition, and the cross-platform Bash portability requirements. Maintainers read this; the LLM executing /graph does not.

---

## §1 Drift-safety design — forward incremental + reverse always-full

### §1.1 Why reverse indexes always rebuild

Forward adjacency (per-thesis links) updates incrementally — re-extracted only for changed theses. Reverse indexes (Macro → Theses, Sector → Theses) **ALWAYS rebuild fully** from `Sectors/*.md` + `Macro/*.md` files on every run.

This combination eliminates the reverse-index drift that motivated the metadata-cull architecture: incremental updates cannot accumulate drift in reverse indexes because reverse indexes are never incrementally updated. Cross-thesis clusters and orphan list also always recompute from the in-memory adjacency state.

### §1.2 Why forward adjacency is safe to update incrementally

Forward adjacency is deterministic per-file: a thesis's `sectors:`, `macro:`, `cross-thesis:`, `research:` are extracted from THAT thesis's own wikilinks. If the thesis is unchanged, re-extracting produces identical output. Skipping unchanged theses saves time without risking drift — the baseline adjacency entry reflects the thesis's actual current state.

### §1.3 Existence validation completes the invalidation cycle

Step I.4 validates each extracted wikilink's target exists on disk. Dangling references (target missing — typically archived thesis) are dropped with an `ℹ️` log. This is the step that actually removes stale post-closure references from the graph — `.graph_invalidations` (written by `/status`/`/prune`) triggers re-extraction in Step I.2.5; Step I.4's existence check then cleans the stale cross-thesis pointers.

The same validation runs in Step I.5 (reverse indexes) — both forward and reverse drop dangling targets independently, preventing asymmetric state (`/lint #23` catches residual asymmetry).

---

## §2 Watermark semantics (T6.10)

### §2.1 Why ISO second-precision

Daily-granularity watermark (`date: YYYY-MM-DD`) had edge cases around midnight:
- Thesis edited at 23:59:30 on day D
- `/graph last` at 23:59:45 on day D writes `date: D`
- Next `/graph last` on day D+1 uses `date: D` watermark → treats anything after 00:00:00 of day D as "changed" → re-processes files already handled.

Correct but wasteful. With ISO precision (`last_graph_write: YYYY-MM-DDThh:mm:ssZ`), the watermark advances to the actual completion time; the next run correctly excludes already-processed files.

**Idempotency preserved**: running `/graph last` twice in the same second is still safe — the second run sees zero changes since the first run's timestamp is now the watermark.

### §2.2 Legacy fallback — why conservative

Graph files pre-dating T6.10 lack `last_graph_write:`. Fallback uses `date: YYYY-MM-DD` with implicit 00:00:00 UTC of that date. This may reprocess files modified earlier on the same day — safely idempotent, slightly wasteful. Next `/graph` write upgrades the frontmatter; subsequent runs benefit from second-precision.

### §2.3 Why NOT poisoning `_graph.md date: 1970-01-01` for /sync all

Earlier documentation referenced a `date: 1970-01-01` poisoning convention for `/sync all`. That convention was never implemented because `/sync` is architecturally forbidden from writing `_graph.md` (metadata ownership boundary). The `.sync_all_fresh` marker file is the replacement mechanism — same outcome (forced full rebuild), clean ownership boundary.

---

## §3 Cross-platform Bash portability (T6.12)

### §3.1 Why reference-file pattern, not `-newermt`

macOS BSD `find -newermt` silently returns an empty set on some ISO 8601 Z-suffixed inputs. Empirically observed Apr 19 2026: `2026-04-19T14:19:33Z` produced zero matches even though files were demonstrably newer. Same invocation worked with local-time string `"2026-04-20 00:19:33"`. GNU `find` on Linux handles Z-suffix correctly.

The `touch -d <ISO>` + `find -newer` pattern is cross-platform portable (BSD `touch` since macOS 10.11; GNU coreutils), produces identical output on both platforms, and eliminates 2-3 diagnostic Bash calls per run when `-newermt` fails silently.

### §3.2 Why NOT `touch -t <stamp>`

The `-t` flag interprets its argument in LOCAL time by default. Converting a UTC ISO to `-t` format requires a timezone-aware intermediate step (via `date -u -j -f` on BSD or `date -u -d` on GNU). `touch -d <ISO>` accepts the Z suffix directly and does the UTC→local conversion internally.

Verified Apr 2026: `touch -d "2026-04-19T14:19:33Z" /tmp/wm` on macOS UTC+10 correctly produces `stat` mtime `Apr 20 00:19:33` local (= 2026-04-19T14:19:33Z).

### §3.3 POSIX bracket-expression regex gotcha

Use `[^]]+` NOT `[^\]]+` when excluding `]` in grep character classes. Inside a POSIX bracket expression the backslash has no special meaning — `[^\]]+` is parsed as `[^\]` (reject backslash) followed by `]+` (literal `]` one or more times), which silently matches nothing on BSD `grep` builds.

`[^]]+` (reject the `]` char directly) is the correct POSIX form and works on macOS + Linux. This was the failure mode that forced N separate Bash calls during the Apr 19 2026 run — the shell appeared to succeed but found zero wikilinks, leading the LLM to conclude "no changes" when there were many.

---

## §4 Tool-call budget rationale (T6.12 + T6.13)

### §4.1 Incremental Path budget

The Incremental Path has strict read → extract → rebuild → write → validate order, but within that order most work bundles into ~8 Bash blocks total instead of 25+. The budget table in SKILL.md Step I.11 header captures the savings per step.

### §4.2 Full Rebuild Path budget

Steps 1-3 are independent filesystem reads — inventory, thesis wikilink extraction, sector/macro reverse indexes. Bundling them into ONE Bash block with section delimiters saves 2 full round trips (~1.5 min on a 40-thesis vault) with bit-identical output.

Step 5's orphan computation requires NO additional Bash — it's a pure set difference against data already extracted in Steps 1+2.

### §4.3 Why re-reading `_graph.md` a second time is wasteful

Step I.1's Single-Read directive: issue ONE `Read` on `_graph.md` in full. Do NOT preview-read with `limit:` then re-read the whole file — the file is <1000 lines, the cache cost is identical, and the extra tool call adds a full round-trip.

Legitimate split only when the file exceeds Read's 2000-line default limit (pre-6.10 full-rebuild output for large vaults could trip this) — in that case pass `limit:` AND `offset:` to cover the whole file in ≤2 reads.

### §4.4 Discrete Edits at Step I.9 — why not fuse

Step I.9's one-Edit-per-thesis pattern is deliberately kept discrete despite the tool-call count. Atomicity preservation takes priority: if the LLM fuses N thesis updates into a single Edit, a partial failure leaves `_graph.md` in an inconsistent intermediate state. Per-thesis Edits each succeed or fail atomically.

This directive was extended in §10: the dominant cost of `/graph last` is output-token generation for the full `Write`, not tool-call round-trips. §10 formalizes the Path A / Path B split — surgical Edits for small diffs (preferred), full Write fallback for wide or legacy diffs.

---

## §5 Step 7.0 no-op short circuit (T6.13)

### §5.1 Why Edit frontmatter-only when body unchanged

Full `Write` emits ~40 KB of model output; `Edit` emits ~30 bytes per field. On a no-op full rebuild (the common case when `/graph` runs on a quiet vault), body is byte-identical — only `date:`, `last_graph_write:`, `graph_mode:` need updating. 2-3 `Edit` calls replace one 40 KB `Write`.

Streams faster end-to-end AND keeps Write-count-dependent audit logs cleaner (each full Write would otherwise show as a content change in git diff).

### §5.2 Why this is safe

The written bytes after the last `Edit` are identical to what a full `Write` would have produced. No other skill reads `_graph.md` differently based on write mechanism — mtime and content both advance. The fix leaves output format, frontmatter schema, and section layout unchanged.

### §5.3 Legacy-frontmatter exception

If prior `_graph.md` lacks `last_graph_write:` (pre-6.10 format), skip the short circuit and do a full `Write`. This upgrades the frontmatter schema in one pass rather than patching a missing field via `Edit`.

---

## §6 Timestamp reuse (T6.13)

### §6.1 Why `last_graph_write:` reuses Step 0.1 timestamp

Step 0.1 lock-acquisition Bash block already captured `NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)` as the lock's `started_at:`. Carry that same value in LLM memory alongside the lock token and reuse it at Step 7.1 as `last_graph_write:`.

Using the lock-acquisition timestamp (a few minutes earlier than actual write completion) is **conservative and correct**:
- A crashed write would leave `last_graph_write:` from a prior run — strictly older, same conservative-watermark semantics.
- Next `/graph last` re-detects any files edited during this run as "changed" and re-extracts them — wasted cycles, never missed changes.
- Clock skew within a single `/graph` run is at most a few minutes; the watermark model is designed to tolerate this.

Issuing a separate `date -u` call adds a round trip with no behavior improvement.

---

## §7 T7.3 cache fields (`status:` + `log_tail:`)

### §7.1 Why cache these in the graph

`/sync` Pass 1 triage (for `/sync all`) and Step 2.5 skill-origin classification previously read every thesis file to extract `status:` and the last few Log entries. On a 40-thesis vault, that's ~40 Read calls per sync. Caching these fields in `_graph.md` — which `/sync` already reads for adjacency — eliminates that read burden.

The fields are a **read-through cache**: `/graph` re-derives them from the source thesis on every rebuild, so the cache is automatically invalidated by any subsequent `/graph last` after a thesis edit.

### §7.2 Consumer contract

- `/sync` Pass 1 classification reads the 3 `log_tail:` prefixes to detect conviction/status-change recency, Stress test / Deepened markers (for drift exclusion), and skill-origin prefixes.
- `/sync` Step 2.5 pattern-matches the **most recent** entry's prefix against the skill-origin list from `_shared/log-prefixes.md`.
- Future consumers (`/surface`, `/lint`) may adopt the same fields.

### §7.3 Schema-version signal — by field presence

When ANY adjacency entry in `_graph.md` carries a `log_tail:` field, consumers assume T7.3 coverage. When the field is absent from the first parsed entry, consumers fall back to per-thesis file reads. No explicit `schema_version:` frontmatter field is required — the field's presence IS the signal.

Pre-T7.3 graphs remain readable; they just cost consumers an extra round of file reads until `/graph` (full or incremental) runs and upgrades the cache. Step I.1's "missing T7.3 cache fields" flag triggers re-extraction for entries lacking the fields.

### §7.4 Why horizontal ellipsis `…` for truncation

`log_tail:` bullets longer than 100 chars get truncated with `…` (horizontal ellipsis, U+2026). This is distinct from `...` (three dots), which `/lint #42` forbids as a truncation-marker artifact in `_hot.md`. Different Unicode character → lint doesn't flag it.

### §7.5 AWK state-machine design

The extraction awk walks top-to-bottom through the `## Log` section, pairs each `### YYYY-MM-DD` header with the first `- ` bullet following it (skipping blank lines), and keeps the last 3 pairs via an `entries[]` array. This handles all the edge cases of the Log format (multi-bullet dates, blank lines between entries, multiple `### Date` headers in sequence).

---

## §8 Full rebuild vs incremental — no disk cross-check on full

The Incremental Path Step I.7 runs a disk-linked cross-check to surface baseline drift between the in-memory adjacency map and current thesis wikilinks. Full rebuild has no baseline — every thesis is freshly re-extracted from disk in Step 2, so the "in-memory map" IS the disk state by definition. Re-reading the same data via `comm` saves zero information and costs one full Bash round trip.

---

## §9 Post-write marker cleanup

### §9.1 Why delete `.graph_invalidations` after write, not before

Ordering matters: delete only AFTER the write succeeds. If the write fails, `.graph_invalidations` persists so the next `/graph last` still re-extracts the same neighbors. Step I.11 reports delete success/failure.

### §9.2 Why delete `.sync_all_fresh` on full rebuild

A full rebuild re-extracts every thesis from source, which is exactly what the marker was requesting. Clearing it prevents subsequent `/graph last` runs from redundantly forcing another full rebuild.

If the rebuild write fails, both markers are preserved so the next `/graph` run still honors them.

---

## §10 Diff-aware Incremental Path — Step I.9 (Path A / Path B)

### §10.1 Why the optimization exists

The dominant cost of `/graph last` is not tool-call round-trips (the fused Bash blocks already collapse these efficiently) — it is **model output-token generation during the final `Write`**. The full graph body is ~400 lines / ~15 KB regardless of how many theses changed. Prior spec (pre-§10) Wrote the full file for any non-empty diff, forcing the model to emit 40 theses' worth of adjacency blocks even to reflect a one-thesis addition.

Measured end-to-end: on a 40-thesis vault with a 1-thesis change, full `Write` dominates latency at 70-80% of total runtime. Surgical Edits emit ~300 bytes each; total output for a typical 1-3 thesis change drops from ~15 KB to ~2 KB — a 5-7× reduction in the critical section.

This mirrors the Step 7.0 no-op short circuit (§5) for the Full Rebuild Path: same principle, extended to the far more common non-no-op incremental case.

### §10.2 Path B escalation triggers

Surgical Edits are correct only when anchors are unique and the diff is small enough that per-delta Edits cost less than a single Write. Path A aborts to Path B in five cases:

1. **Baseline parse failure** (Step I.1 unparseable): no baseline to diff against — can only emit a full file.
2. **Pre-T6.10 legacy frontmatter** (no `last_graph_write:` field): Edit needs an `old_string`; missing field can't be Edited, only prepended via Write. Upgrades schema in one pass.
3. **Wide pre-T7.3 upgrade** (≥10 entries missing `status:` / `log_tail:`): each upgrade needs an Edit (insert 4-6 lines per entry). At 10+ entries × ~250 bytes per granular Edit = 2.5+ KB output PLUS per-call overhead > full Write breakeven.
4. **Half the theses modified** (|modified| > 0.5 × |baseline|): output-token math flips — per-thesis Edit replaces one full block of ~8 lines, so N full-block Edits ≈ N × block-size, which at N ≥ 20 approaches the full Write size anyway. The 50% threshold leaves headroom.
5. **Mid-cascade Edit failure**: partial Path A leaves `_graph.md` in inconsistent state. Path B re-renders the full in-memory state and Writes over the partial result, restoring consistency.

Triggers 3 and 4 are computed from counts available after Step I.4; no additional probing needed.

### §10.3 Anchor uniqueness — why it holds by construction

Path A Edits rely on `old_string` being unique in `_graph.md`. The graph's own structure guarantees this for every anchor type used:

- **Thesis headers** (`### TICKER - Company Name`): by definition one per thesis, and tickers are unique in the active vault (archive-collision protocol in `/thesis` and `/rename` enforces no duplicate tickers).
- **Reverse-index rows** (`| [[Sectors/X]] | ... |`): each sector/macro has one row in its respective table; the full row line begins with a unique wikilink.
- **Orphan lines** (`- [[Research/YYYY-MM-DD - ...]]`): research note filenames are time-stamped and globally unique.
- **Frontmatter fields** (`date: ...`, `edges: ...`): each field name appears exactly once in the YAML block.

The pre-emission uniqueness check is a safety net, not an expected hot path. Only degenerate cases (e.g., corrupted graph with duplicate headers) trigger it, and they correctly escalate to Path B where a full re-render fixes the corruption.

### §10.4 Tool-call and output-token budget

Typical `/graph last` with 1 changed thesis under Path A:

| Stage | Tool calls | Model output |
|---|---|---|
| Pre-flight (lock + watermark + change detection fused) | 1 Bash | ~80 B |
| I.1 Read baseline | 1 Read | 0 |
| I.4 + I.5 extraction (fused per-thesis + reverse indexes) | 1 Bash | ~60 B |
| I.9 Path A: frontmatter (3 fields) + 1 added thesis block + 1 reverse-index row + 2 orphan removes | 7 Edit | ~2.0 KB |
| I.10 + I.11 validation + cleanup + lock release | 1 Bash | ~100 B |
| **Total** | **11 calls** | **~2.3 KB** |

Same scenario under pre-§10 Write-everything spec:

| Stage | Tool calls | Model output |
|---|---|---|
| Pre-flight + I.1 Read + I.4/I.5 extraction | 3 | ~140 B |
| I.9 full `Write` | 1 Write | ~15 KB |
| I.10 + I.11 | 1 Bash | ~100 B |
| **Total** | **5 calls** | **~15 KB** |

Path A trades 6 extra tool calls (cheap, ~1s each) for a 6.5× reduction in model output (expensive, token-streaming-bound). Observed end-to-end savings: 3-5 minutes on a 40-thesis vault.

### §10.5 Why per-Edit atomicity is still honored

§4.4's atomicity priority remains: each Path A Edit targets exactly one anchor and succeeds or fails independently. A failed Edit doesn't corrupt neighboring state — the in-memory new state is unchanged, and the mid-cascade escalation to Path B re-renders the complete target from that memory, overwriting any partial bytes.

The difference from pre-§10 spec: §4.4 originally described per-thesis Edits as if that were the then-current behavior, but the actual Step I.9 text prescribed a full Write. §10 resolves this inconsistency — Path A is the described per-Edit behavior made concrete, Path B is the Write escape hatch.

### §10.6 Why not cache rendered blocks

An alternative optimization is caching rendered adjacency blocks in memory / a sidecar file, so unchanged blocks don't need to be re-emitted. Rejected for complexity: the graph is markdown-native for a reason — plain text is reviewable, diffable, Git-friendly. Adding a parallel cache layer creates schema-drift risk (cache vs. `_graph.md` out of sync) with no benefit Path A doesn't already deliver. If future vault growth (150+ theses) makes Path A insufficient, the next lever is a helper script that renders sections from structured data — but that is a larger architectural change and out of scope here.
