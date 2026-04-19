# Infrastructure Reference

> Deep technical details for the vault's consistency machinery. The user-facing summary lives in [[User Guide#11. Infrastructure (User-Facing)]]. Read this when you need to debug an edge case, understand why a skill behaves a certain way, or extend a skill's contract.

---

## 1. Content caches & metadata files

### 1.1 `_hot.md` — Session Context Cache

Persists context between sessions. Canonical six-section schema:
- **Active Research Thread**: what you're currently working on (auto-compressed history)
- **Latest Sync**: last sync summary
- **Sync Archive**: compressed older syncs (max 3)
- **Recent Conviction Changes**: conviction/status changes and drift flags
- **Open Questions**: unresolved questions across theses
- **Portfolio Snapshot**: high-level portfolio state

Updated by **11 skills**: `/sync`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/thesis`, `/deepen`, `/prune`, `/status`, `/rollback`, `/catalyst`. All writers follow the compression contract in `.claude/skills/_shared/hot-md-contract.md`:

- **Per-section budgets** (% of soft cap):
  - Active Research Thread 30%
  - Latest Sync 15%
  - Sync Archive 20%
  - Recent Conviction Changes 15% (**never compressed**)
  - Open Questions 15%
  - Portfolio Snapshot 5%

- **Caps**: soft 2,000 words / hard 2,500 words.
- **Compression trigger order** over soft cap: drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → warn in skill report.
- **Hard cap** aborts the `_hot.md` write (primary skill operation still succeeds).
- **Truncation markers forbidden**: `...` trailing bullets, `[compressed]`, `[truncated]`, unclosed formatting. Compression drops whole entries rather than truncating.
- **Same-ticker continuation**: same-ticker Active Research Thread stays live (append dated line); different-ticker compresses outgoing thread to a single `*Previous:*` line.

Lint checks:
- `/lint #35` verifies the six-section schema (missing sections cause silent skill no-ops)
- `/lint #42` catches truncation-marker drift

### 1.2 `_graph.md` — Vault Dependency Map

Owned exclusively by `/graph`. Three modes:

| Mode | When | Cost |
|---|---|---|
| `/graph last` | After every `/sync` | Skip if nothing changed; else re-extract only changed thesis adjacencies + rebuild reverse indexes in-memory |
| `/graph [N]` | Catch-up after N days without refresh | Same incremental logic; watermark = today − N days |
| `/graph` (no args) | After `/sync all` or disaster recovery | Full rebuild from scratch |

**Precise ISO watermark**: frontmatter carries `last_graph_write: YYYY-MM-DDThh:mm:ssZ` in addition to `date: YYYY-MM-DD`. Change detection uses ISO timestamp for second-precision — no edge cases at midnight rollovers. Legacy graph files without `last_graph_write:` fall back to `date:` at 00:00:00 UTC (conservative; next write upgrades).

**Reverse indexes always rebuild from scratch in-memory**: Sector → Theses, Macro → Theses, cross-thesis clusters, orphan list. This prevents drift even when incremental adjacency extraction skips unchanged theses.

**Research skills never write to `_graph.md`**: `/sync`, `/thesis`, `/compare`, `/scenario`, `/deepen`, `/surface`, `/stress-test`, `/brief`, `/status`, `/prune`, `/catalyst`, `/ingest`, `/lint`, `/clean`, `/rollback` all create content and remind you to run `/graph last`. `/rename` is the sole exception (updates adjacency entry header atomically with filename mv).

### 1.3 `_catalyst.md` — Catalyst Calendar

Regenerated each `/catalyst` run. Timeline: next 2 weeks (daily), weeks 3-4 (weekly), months 2-3 (grouped by week). Flags catalyst gaps and stale events.

**Pre-regenerate snapshot** (H2 fix): if web search fails mid-run, recover via `/rollback` batch `catalyst-YYYY-MM-DD-HHMMSS`. Snapshot failure **hard-aborts** `/catalyst` — the prior `_catalyst.md` is always preserved; no partial overwrite path exists.

---

## 2. Watermarks & state markers

### 2.1 `.last_sync` — Sync Watermark

Touched at the end of every default `/sync` and `/sync all`. Used by the next `/sync` to detect changed files via `find -newer .last_sync`.

- **Never touched by `/sync TICKER`** — ticker-scoped mode preserves the baseline for the next default sync. First-run exception: if `.last_sync` is absent when `/sync TICKER` runs, an epoch placeholder is created so default sync has a baseline.
- **Never touched by `/graph`** — graph has its own watermark (`_graph.md` frontmatter).

**Idempotency keying** (H4 fix): `/sync`'s per-thesis idempotency check keys on:
1. **Primary**: research-note wikilink presence in thesis Log
2. **Secondary** (new): source URL, date+ticker, tags — preserves idempotency across renames/moves

Once a research note has propagated to a thesis, that is terminal: subsequent `/sync` runs skip the propagation regardless of calendar day OR whether the research note has been renamed/moved. Eliminates:
- Midnight-rollover duplicates (11:59pm and 12:01am runs)
- Rename-induced re-propagation (research note filename change breaks wikilink match; secondary keys carry)

### 2.2 `.sync_all_fresh` — Brute-force-sync marker

Touched at the end of `/sync all` only. Read by `/graph` at Watermark Resolution; if present, forces full rebuild regardless of mode and deletes marker after successful write.

Closes the gap where `/sync all`'s two-pass triage leaves "No delta" thesis mtimes untouched — incremental `/graph last` would otherwise miss them.

No user action required. `/graph` manages lifecycle. `/lint #38` ages it.

### 2.3 `.graph_invalidations` — Post-closure neighbor list

Written or appended by:
- `/status` Step 7.6 (on `active→closed`)
- `/prune` Stage 4.5 (on closure runs)

Contains relative paths of neighbor thesis files that `[[wikilink]]`-referenced the just-archived thesis; their `cross-thesis:` adjacency entries need re-extraction to clear dangling references.

Read by `/graph last`, folded into the changed-thesis bucket, and deleted only after successful graph write. Dedup via `sort -u`; repeated closures safely accumulate.

### 2.4 `.rename_incomplete.TICKER` — Failed-rename repair markers

Written by `/rename` Step 5.5 when one or more wikilink Edits fail after the file move completed.

**Per-ticker filename** so multiple concurrent rename repairs coexist without corrupting each other.

Marker YAML:
```yaml
ticker: META
old_name: Meta
new_name: Meta Platforms
batch_id: rename-2026-04-19-143022
failed_files:
  - Sectors/megacap.md
  - Research/2026-04-15 - Meta - earnings.md
```

Re-run `/rename TICKER "new_name"` to retry: repair-detection exception skips the already-completed mv and only re-attempts failed Edits. Marker shrinks monotonically across re-runs until empty, then auto-deletes.

**Cross-new_name guard** (Step 1.4.5): if the marker exists with a different `new_name:` than the proposed re-run, `/rename` aborts with explicit options — prevents corruption where two different target names would overwrite each other's repair state.

**Pre-flight marker check** in all ticker-scoped skills: `/status`, `/sync TICKER`, `/stress-test`, `/compare` (per-ticker), `/deepen`, `/brief`, `/surface TICKER`, `/thesis` hard-block on an active marker for their ticker. Vault-wide skills (`/sync`, `/sync all`, `/prune`, `/scenario`) hard-block on ANY active marker. Exceptions: `/lint`, `/rollback`, `/graph` (read-only), `/rename` (owns the marker), `/ingest` (advisory only).

`/lint #37` globs `.rename_incomplete.*` and surfaces each marker as Important until cleared.

### 2.5 `.archive_ticker_registry.md` — Archive lookup table

Flat append-only log of thesis archival events, auto-maintained by `/status` Step 7.5b (on closure) and `/prune` Stage 2 (on closure runs). One line per archive event:
```
TICKER|archived_filename.md|YYYY-MM-DD|conviction_at_closure|closure_rationale
```

Consumed by `/thesis` Step 1.2 multi-signal archive-collision check (Signal C) to detect prior archived theses even when the archived filename no longer matches the `_Archive/TICKER - *.md` pattern (renamed-then-archived cases).

`/lint #46` validates registry entries against current `_Archive/` state; stale entries (file no longer exists at listed path) tolerated — `/thesis` verifies existence before treating a registry entry as a match.

### 2.6 `.vault-lock*` — Concurrency locks

Acquired at Step 0 of every skill that modifies vault state, per `.claude/skills/_shared/preflight.md`. Prevents concurrent skill invocations from racing on `_hot.md`, thesis Logs, sector notes, `_graph.md`, and marker files.

**Token-based ownership** (not PID-based): because Claude Code's Bash tool is stateless (each Bash block runs in a fresh subshell with different `$$`), the lock's `token:` field identifies the skill-run. The LLM captures the token at Step 0.1 acquisition and carries it in its conversation context through all subsequent tool calls. Every subsequent Bash block verifies ownership by matching the captured token against the current `.vault-lock*` content; mismatch aborts the skill.

**Lock scopes**:

| Scope | File | Skills |
|---|---|---|
| Vault-wide | `.vault-lock` | `/sync all`, `/graph`, `/prune`, `/lint` full, `/clean`, `/catalyst`, `/ingest` (all modes), `/scenario`, `/surface` (unscoped/sector), `/rollback` restore mode |
| Ticker | `.vault-lock.TICKER` | `/sync TICKER`, `/deepen`, `/stress-test`, `/status TICKER`, `/brief`, `/rename`, `/thesis`, `/surface TICKER` |
| Multi-ticker | N separate per-ticker locks | `/compare A vs B vs C` acquires `.vault-lock.A` + `.vault-lock.B` + `.vault-lock.C` |
| Read-only | `.vault-lock.readonly` | `/lint TICKER`, `/rollback` list mode |

**Why per-ticker for `/compare`** (not `+`-delimited): prior `+`-delimiter scheme failed on hyphen-containing tickers (`BRK-B`, `BF-A`). Per-ticker locks handle these cleanly and roll back on partial acquisition failure (release all previously-acquired locks before aborting).

Each lock carries `token:`, `skill:`, `scope:`, `started_at:`, `timeout_at:`, `session_id:` in YAML frontmatter. Multi-ticker locks additionally carry `multi_scope:` listing peer tickers.

**Release** is explicit in the skill's final Bash block (`rm -f "$LOCK_FILE"`), not trap-based. `trap "... INT TERM"` handles Ctrl-C / kill signals within the acquisition block; subsequent blocks don't inherit the trap by design.

**Stale detection**: a lock is stale when `timeout_at` < now. Staleness does NOT trigger auto-steal — timeout-based stealing would race legitimately long-running skills (web research, large batches). Recovery is user-initiated: manually `rm` the lockfile after confirming the prior skill is truly abandoned. `/lint #43` surfaces stale locks for review.

### 2.7 `.drift-config.md` (optional) — `/sync` drift tuning

Optional vault-root file for tuning `/sync` Step 3e conviction-drift heuristics. Format:
```yaml
---
window_size: 5                 # default 5; min 3, max 10
base_threshold: 3              # default 3 weakening entries in window fires drift
post_stress_threshold: 4       # default 4 (suppresses drift within 30 days of stress test)
post_stress_window_days: 30    # default 30
deepened_exclusion_days: 14    # default 14 (was 7 pre-tuning update)
---
```

Missing file → use defaults. Malformed → log warning and proceed with defaults.

**Default drift rules**: base 3/5 weakening triggers drift flag; if a `"Stress test"` Log entry exists within 30 days for the ticker, threshold raises to 4/5 (post-stress-test suppression). Deepened entries within 14 days of a Stress test are excluded from the window. The drift flag text reports threshold state: `⚠️ Conviction drift — 3/5 recent updates flagged headwinds (post-stress-test suppression: no)`.

---

## 3. Snapshots & transaction manifests

Every multi-file skill uses the **skeleton → populate → flip** pattern to enable crash-recovery and cascade rollback. Manifests are written BEFORE any destructive mutation lands, populated incrementally, then flipped to `status: completed` at the end. An `in-progress` manifest is `/lint`'s signal that the skill crashed or the final flip silently missed.

### 3.1 `_Archive/Snapshots/` — Version Control

Created automatically before destructive edits by:
- `/sync` — Tier A section edits
- `/deepen` — every edit
- `/status` — except draft→active
- `/compare` — sector note changes, per-sector batch IDs on cross-sector runs
- `/prune` — sector note changes
- `/catalyst` — pre-regenerate
- `/rollback` — pre-rollback safety net
- `/rename` — pre-rename snapshot

Cleaned by `/clean`; non-snapshot artifacts (manifests) are skipped by age-based cleanup and handled per artifact type.

**Batch ID format**: `<trigger>-YYYY-MM-DD-HHMMSS` with 6-digit second-precision. `/rollback` cascade detection matches snapshots by batch ID prefix.

**Orphan protection**: snapshots whose `snapshot_of:` source file is missing default to PROTECTED by `/clean`. Explicit opt-in via `/clean orphans` (orphans only, any age) or `/clean [days] --include-orphans` (age-based + orphans). Fail-safe default because a deleted source may have been removed in error, and the snapshot is the only recovery path.

### 3.2 `_prune-manifest (prune-*).md`

Written by `/prune` Stage 1.5 before any closure/upgrade lands. Records:
- Intended closures (ticker, target `_Archive/` path)
- Upgrades (ticker, old/new conviction)
- Affected sector notes
- Stage 4.2 neighbor targets (for cross-thesis closure Log entries)

Flipped to `status: completed` + `completed_date:` at Stage 5.

**30-day regret-recovery window**: the manifest is retained for 30 days after `completed_date:`. Within this window, `/rollback` cascade-detection can surface Tier B "Cross-thesis closure" Log entries on neighbor theses (which have no per-neighbor snapshots) for strikethrough review.

Lifecycle:
- `/lint #36` — Pass within 30 days, Nice to Have after
- `/clean` — removes manifests only after BOTH the age threshold AND the 30-day floor are satisfied. A user running `/clean 10` does NOT delete a 15-day-old completed manifest. A user running `/clean 180` DOES delete a 40-day-old completed manifest.

### 3.3 `_sync-manifest (sync-*).md`

Two-phase write.

**Skeleton** (Step 2.9, new): writes with `status: in-progress` BEFORE any Tier A snapshot or Tier B Log append lands. Skeleton write failure hard-aborts the sync pre-mutation — no silent audit gap possible.

**Populate** (Steps 3–6): append accumulator entries incrementally:
- Tier A snapshots (per-thesis section edits)
- Tier B Log appends on neighbor theses without snapshots
- Sector/macro edits
- Source research notes

**Flip** (Step 7.5): flips status to `completed` + verifies the flip landed.

Consumed by `/rollback` Step 2.5b cascade detection: when the user selects a pre-sync snapshot, the manifest's Tier B Log entries are surfaced for review with options — (a) surface-only, (b) auto-strikethrough, (c) manual. Without the manifest, Tier B appends would persist as orphan audit entries after rollback.

`/lint #41` classifies by `status:`:
- `in-progress` → Important (crash or flip failure)
- `completed` → age-based tiers (90+ days Nice to Have, 180+ days Important)

### 3.4 `_compare-manifest (compare-*).md`

Written by `/compare` Phase 5.5c after the cross-sector atomic transaction. Records:
- Sectors successfully edited
- Sectors rolled back (if atomicity fired)
- Thesis Log append outcomes per target
- Research note path

`status: completed | rolled-back`. `/lint #45` handles aging.

### 3.5 `_stress-test-manifest (stress-test-*).md` (T3.1)

Written by `/stress-test` Phase 4.6 recording the Log entry text appended to the tested thesis. Enables `/rollback` Step 2.5d cascade for strikethrough annotation of the append-only Log entry. Research note at `Research/` is preserved (same policy as scenario and compare research notes).

`/lint #47` handles aging + status.

### 3.6 `_status-manifest (status-*).md` (T2.2)

Two-phase write matching `/sync`.

**Skeleton** (Step 3.0.5): writes before any file modification; records:
- Intended thesis frontmatter change
- Sector note edit
- Archive move (closure only)
- Graph invalidations
- `_hot.md` update

**Flip** (Step 7.9): flips status after all landings verified.

`/rollback` Step 2.5e cascade offers:
- (a) thesis-only restore
- (b) full transaction restore (thesis + sector + un-archive + clear invalidations)

Reaffirm flow does NOT write a manifest (no multi-file transaction).

`/lint #48` handles aging + in-progress detection.

### 3.7 `_thesis-manifest (thesis-TICKER-*).md` (H1)

Two-phase write matching the other manifests.

**Skeleton** (`/thesis` Step 3.5): writes before any file modification; records:
- Intended thesis file path
- Sector note edit plan
- `_hot.md` edits
- Orphan research integration targets
- (If encountered) archive-collision decision from Step 1.2

**Flip** (Step 7.5): flips status.

`/rollback` Step 2.5f cascade offers:
- (a) delete thesis file only
- (b) full cascade (delete + revert sector + revert `_hot.md` + orphan mtime revert if captured)
- (c) cancel

**Unlike status/sync which restore FROM snapshots, thesis cascade is deletion-based** since `/thesis` creates new files with no "before" state to snapshot.

`/lint #49` handles aging + in-progress detection. No regret-recovery window — `/thesis` is constructive, not destructive; post-hoc edits are `/deepen`'s job.

---

## 4. Content-quality gate (`/ingest`)

URL and PDF ingests block on failure; manual local files receive advisory logs.

### 4.1 Structural checks
- ≥150 word body
- Absence of paywall/CAPTCHA/anti-bot sentinels
- At least 2 of 4 expected body sections populated

### 4.2 Domain-specific checks by `source_type:`

| `source_type` | Requirements |
|---|---|
| `earnings` | Period tokens (Q1/Q2/Q3/Q4/FY20XX) + 2+ currency figures + ticker/company reference |
| `analyst-report` | Rating token (Buy/Sell/Hold/Overweight/Underweight/etc.) + price-target reference + ticker |
| `news` | Ticker + dated event reference (absolute date or temporal token like "announced"/"reported") |
| `deep-dive` | ≥500 words + ≥3 substantive sections (higher floor than generic) |
| `web-clip`, `data` | Skip domain checks (no vocabulary expected) |

### 4.3 Integrity checks
- **Numerical integrity**: detects OCR corruption patterns (capital-O-as-zero, decimal-dropped currency like `$1 5B`, `II` as `11`)
- **Title-URL consistency** (URL mode): first heading tokens must overlap ≥50% (Jaccard) with URL path slug — catches redirects to login/subscribe pages

### 4.4 Failure handling
Failed gate → research note deleted, source retained for re-ingest after resolving access or correcting `source_type:`. Blocks the most damaging silent-corruption path: paywalled or wrong-content URLs propagating into thesis Log entries via `/sync`.

### 4.5 Source-URL dedup
- **Mode A URL, Mode B single-file**: exact-match grep against existing `Research/*.md` `source:` frontmatter
- Same-day match → hard-block
- Cross-day match → prompts skip/re-ingest/cancel
- **Batch Mode C** uses `_Inbox/processed/` filename-based guard instead

---

## 5. Atomicity & producer contracts

### 5.1 `propagated_to:` — the atomicity signal

Research notes from `/scenario`, `/stress-test`, `/compare` carry a `propagated_to:` frontmatter field listing tickers whose thesis Logs received the propagation.

**Atomicity rule**: the field is written ONLY after all Log appends succeed. On partial failure, the field is omitted, which is the signal for `/sync` to retry via file-direct fallback (research note's `ticker:` or `tags:`).

**Terminal signals**:
- `synthesis` and `brief` notes have `propagated_to: []` — terminal; blocks `/sync` from spamming 10+ theses with circular self-propagation Log entries

### 5.2 `/lint #39` — producer contract verification

Vault-wide only. For each `Research/*.md`, verifies:

| `source_type` | Requirement | Severity if missing |
|---|---|---|
| `synthesis`, `brief` | Must be `[]` | Important regardless of date |
| `scenario`, `stress-test`, `comparison` | Must be present unless atomicity rule fired | Important if absent and date ≥ 2026-04-19; Nice to Have if pre-spec |
| `deep-dive` and others | No requirement | — |

Cross-checks with `/lint #1` — notes flagged by both are strongest cleanup candidates.

### 5.3 Multi-signal archive-collision check (`/thesis` Step 1.2)

Before creating a new thesis, `/thesis` checks for prior archived analysis via four signals (union):

| Signal | Source |
|---|---|
| A | Filename glob `_Archive/TICKER - *.md` |
| B | Frontmatter `ticker: TICKER` in any `_Archive/*.md` (catches renamed-then-archived theses) |
| C | Lookup in `.archive_ticker_registry.md` |
| D | Historical `snapshot_of:` references in `_Archive/Snapshots/` |

On any match → 4 explicit options:
- (a) `/rollback TICKER` to restore the prior thesis
- (b) proceed with different name suffix to make dual-file state intentional
- (c) proceed with proposed name accepting dual files (caveat in initial Log entry)
- (d) cancel

### 5.4 `/thesis` new-sector handling (Step 5)

If the thesis's `sector:` frontmatter doesn't resolve to any `Sectors/*.md` (via exact, normalized, or substring matching), Step 5 prompts:
- (a) create a minimal `Sectors/[sector].md` scaffold with this thesis as first Active Thesis
- (b) proceed without sector update
- (c) cancel to fix the sector value

No silent skip.

### 5.5 `/scenario` classification approval gate (Phase 6.1.5)

Before any Log entries or research note write, `/scenario` pauses and presents the Major/Minor/Neutral classification for explicit review. Options:
- (a) approve and proceed
- (b) promote specific Minor/Neutral theses to Major with user-provided rationale
- (c) demote Major to Minor
- (d) cancel (no files written)

Catches LLM misclassification on either side — a Minor-classified thesis that's actually exposed (false negative) or a Major-classified thesis that isn't (false positive, reversible but noisy).

After approval, appends Log entries to all Major-impact theses. `propagated_to:` on the research note is set only if ALL Major-impact Log appends succeed (atomicity rule).

### 5.6 `/scenario reverse` archive-aware iteration

Resolves each previously-affected ticker's current location:
- Live theses in `/Theses` receive the `Scenario REVERSED` Log entry
- Theses archived since the scenario propagated are NOT modified (Tier 3 archive protection) — the archive-skip is instead documented in a `## Reversal Notes` section appended to the scenario research note body

Full audit preserved across both reopened and archived sides.

### 5.7 `/sync` drift detection window (H4 integration)

Conviction drift Log-entry scanning uses exclusion rules (registry §14):
- `"Conviction reaffirmed"` — window anchor; Log entries older than this are excluded from drift scoring
- `"Scenario REVERSED"` — drift-exclusion (so reversal doesn't inflate drift signal on affected theses)
- `"Cross-thesis closure"` — drift-exclusion (premise entry from neighbor closure, not thesis-level signal)

### 5.8 `/rollback` neighbor-citation scan (H3)

Beyond Log-entry cascade detection, `/rollback` for a closed thesis now also scans:
- **Macro notes** — body prose outside Log sections for `[[TICKER]]` citations
- **Sector notes** — body prose outside Log sections (Acquisitions, Industry history) for `[[TICKER]]` citations

Each hit is classified:
- **Premise-dependent**: prose that assumes the thesis's operating state (e.g., "LITE's closure removes the CPO supply bottleneck")
- **Contextual**: prose that names the ticker historically without premise dependency

Surfaced in the rollback report for manual review. Not auto-edited (body prose is not Log-tier append-only; manual judgment required).

---

## 6. Idempotency keys (H4)

### 6.1 Primary key
Research-note **wikilink presence** in thesis Log.

### 6.2 Secondary keys (rename/move resilience)
- `source:` URL
- `date:` + `ticker:` pair
- `tags:` set

On `/sync`, if primary key misses (wikilink not present), secondary keys are consulted. If any secondary key resolves to a prior propagation, skip — the note has already been propagated, the wikilink just shifted (renamed or moved).

### 6.3 Why H4 matters
Pre-H4: renaming a research note caused the wikilink check to miss, leading to re-propagation and a duplicate Log entry on the thesis.

Post-H4: secondary keys carry across renames. The primary key is still authoritative when present; secondaries are the fallback.

### 6.4 Detection & cleanup of legacy duplicates
If you rename a research note pre-H4 and `/sync` subsequently re-propagated:
- Logs show two consecutive entries with different research-note names but same date/ticker/tags
- Manual cleanup: strikethrough the second entry with `~~entry~~ → Duplicate; superseded by [earlier wikilink]`

Going forward, new runs handle renames correctly.

---

## 7. Lock semantics deep-dive

### 7.1 Why token-based (not PID-based)

Claude Code's Bash tool is stateless — each Bash block runs in a fresh subshell with a different `$$`. PID-based ownership would require carrying the parent-process context across shell invocations, which isn't possible.

Token-based: the LLM captures the token emitted at Step 0.1 and includes it as a variable in every subsequent Bash block. The lock file's `token:` field is matched against the captured token at every ownership verification (Procedure 1.5).

### 7.2 Why explicit release (not trap-based)

`trap "... INT TERM"` would handle Ctrl-C / kill signals within the acquisition block, but subsequent blocks don't inherit the trap because each is a fresh subshell.

Explicit release in the skill's final Bash block (`rm -f "$LOCK_FILE"`) is more reliable. If the skill aborts mid-run, the lock persists and shows as stale on `/lint #43` — user decides whether to manually `rm` after confirming abandonment.

### 7.3 Why no auto-steal

Timeout-based stealing would race legitimately long-running skills:
- Web research may legitimately take >5 min (`/thesis`, `/stress-test`)
- Large batches (`/sync all` on a mature vault) may exceed timeouts

Auto-steal would corrupt any transaction where the "abandoned" skill is still writing. Manual recovery is the safer default.

### 7.4 Multi-ticker partial acquisition rollback (`/compare`)

`/compare A vs B vs C` acquires `.vault-lock.A` + `.vault-lock.B` + `.vault-lock.C` sequentially. If any acquisition fails (another skill holds that ticker's lock):

1. Release all previously-acquired locks in reverse order (C, B) — NOT orphan them
2. Abort `/compare` with message "Partial lock acquisition failed on TICKER; rolled back prior acquisitions"
3. User waits for the conflicting lock to clear, re-runs `/compare`

**Why reverse-order release**: ensures cleanup is deterministic even if individual `rm -f` fails. Partial rollback state is detectable: any surviving pre-acquired lock with matching token but skill ≠ current is a rollback orphan.

### 7.5 Lock token ownership verification (Procedure 1.5)

Every Bash block after Step 0.1 runs:
```bash
CURRENT_TOKEN=$(grep '^token:' "$LOCK_FILE" | awk '{print $2}')
if [ "$CURRENT_TOKEN" != "$MY_TOKEN" ]; then
  echo "❌ LOCK_LOST — token mismatch (expected $MY_TOKEN, found $CURRENT_TOKEN)"
  exit 1
fi
```

Mismatch means another skill (or user `rm` + re-acquire) seized the lock. Abort immediately; any in-progress transaction manifest remains `in-progress` for `/rollback` cascade recovery.

---

## 8. Rollback cascade catalogue

Each multi-file skill writes a manifest; `/rollback` reads the manifest to offer atomic restore.

| Cascade | Trigger | Options offered |
|---|---|---|
| 2.5a | `/sync` primary snapshot | (b) Auto-strikethrough Tier B Log entries on neighbor theses |
| 2.5b | `/sync` cascade via `_sync-manifest` | Tier B Log entry review: (a) surface, (b) auto-strikethrough, (c) manual |
| 2.5c | `/prune` batch | (a) Restore thesis from snapshot + unarchive, (b) also surface Tier B Stage 4.2 neighbor Logs for strikethrough |
| 2.5d | `/stress-test` batch | (a) Restore snapshot, (b) cascade + strikethrough Log entry on tested thesis |
| 2.5e | `/status` batch | (a) Thesis-only restore, (b) Full transaction restore (thesis + sector + un-archive + clear invalidations) |
| 2.5f | `/thesis` batch | (a) Delete thesis only, (b) Full cascade (delete + revert sector + revert `_hot.md` + orphan mtime revert), (c) cancel |
| Catalyst | `/catalyst` batch | Restore prior `_catalyst.md` from pre-regenerate snapshot |
| Rename | `/rename` pre-rename snapshot | Restore thesis file + inbound wikilinks to pre-rename state |

### 8.1 `/rollback` Step 6.2.5 — Intervening-entries scan (closed theses only)

When rolling back a closed thesis, scan all neighbor theses (and now H3-extended Macro + Sector notes) for Log entries or prose dated after the closure but referencing the closed thesis.

Options:
- (a) surface-only (user handles manually)
- (b) auto-strikethrough entries tagged `Cross-thesis closure:` (premise-dependent on the closure)
- (c) auto-strikethrough ALL intervening references
- (d) skip

Premise-dependent vs contextual classification guides default recommendation — premise-dependent entries are usually strikethrough candidates; contextual mentions can safely persist.

---

## 9. Skill pre-flight contract

Every skill that modifies vault state runs pre-flight checks at `.claude/skills/_shared/preflight.md` at Step 0:

### 9.1 Procedure 1 — Vault lock acquisition
Scope per skill type (see §2.6). Timeout budget varies: 5 minutes for most, longer for `/prune` / `/sync all` / `/scenario`.

### 9.2 Procedure 1.5 — Ownership verification
Run at every subsequent Bash block. Mismatch → abort with `LOCK_LOST` / `LOCK_STOLEN`.

### 9.3 Procedure 2 — Rename-marker check
Any ticker-scoped skill hard-blocks if `.rename_incomplete.TICKER` exists at vault root. Vault-wide skills glob `.rename_incomplete.*` — most hard-block, a few (`/ingest`, `/rollback` restore, read-only `/surface`) warn-only. Exceptions: `/lint`, `/rollback` list mode, `/graph` (read-only for theses), `/rename` itself.

### 9.4 Procedure 3 — Name sanitization
Any skill taking user-supplied string as filename (currently `/rename` new_name) runs whitelist + NFC validation:
- Allowed: `[a-zA-Z0-9 \-_.,'&()]`
- Rejected: `/\:*?"<>|`, leading dot, reserved names, length >100

### 9.5 Procedure 4 — Section existence probe
Skills editing a specific `## Heading` abort if section is absent (e.g., `/deepen` never creates sections that don't exist in the thesis).

### 9.6 Release
Final Bash block: `rm -f "$LOCK_FILE"` after all writes verified.

---

## 10. `/graph last` cost model

| Vault state | Work performed |
|---|---|
| No files changed since last graph | Skip — zero reads |
| 1–5 thesis files changed | Re-extract those theses + read 19 sector/macro files for reverse indexes |
| 30+ thesis files changed | Approaches the cost of a full rebuild |

**Watermark precision is second-level** (ISO timestamp in `last_graph_write:`). Running `/graph last` twice the same minute still re-processes files modified between runs — output is idempotent (correct, just wasted compute).

Legacy graph files without `last_graph_write:` fall back to `date:` at 00:00:00 UTC. Next `/graph` write upgrades the frontmatter; subsequent runs use second-precision.

---

## 11. `/rename` atomicity details

### 11.1 Wikilink patterns (7 variants)

`/rename` Edit scans for and updates 7 wikilink patterns:
1. `[[TICKER - OldName]]`
2. `[[TICKER - OldName.md]]`
3. `[[TICKER - OldName|alias]]`
4. `[[Theses/TICKER - OldName]]`
5. `[[Theses/TICKER - OldName.md]]`
6. `[[_Archive/TICKER - OldName]]` (for archived-then-renamed cases)
7. `[[_Archive/TICKER - OldName.md]]`

### 11.2 Pre-flight Read/Write probe (Step 3.5)

Before the `mv`, `/rename` reads every file that contains an inbound wikilink (glob across `Theses/`, `Research/`, `Sectors/`, `Macro/`, `_Archive/`, `_hot.md`, `_graph.md`). If any file is unreachable (permission, lock, disk), `/rename` aborts BEFORE the mv — no partial state.

### 11.3 Step 1.4.5 cross-new_name guard

If `.rename_incomplete.TICKER` marker exists from a prior failed rename:
- If `new_name` matches → repair mode (skip mv, retry Edits only)
- If `new_name` differs → abort with "In-flight rename conflict" — prevents two different target names from corrupting each other's repair state

User options when conflict:
- Finish prior rename with marker's `new_name:` first
- OR manually resolve listed files + `rm` marker
- OR accept loss of repair state (manually fix listed files first to avoid broken wikilinks)

### 11.4 Post-mv Edit failure

If any wikilink Edit fails after the mv completed, `/rename` writes `.rename_incomplete.TICKER` containing:
- Rename context (ticker, old_name, new_name, batch ID)
- Failed-file list

Re-run `/rename TICKER "[new_name]"` triggers repair mode: marker-detected, mv skipped, only failed Edits retried. Marker shrinks monotonically across re-runs until empty, then auto-deletes.

### 11.5 `/lint #37` multi-marker detection

`/lint #37` globs `.rename_incomplete.*` — multiple in-flight repairs surface independently. Scoped `/lint TICKER` runs only for the specific ticker's marker if present.

---

## 12. Lint registry (by ID)

Key checks:

| ID | Scope | What it catches | Severity |
|---|---|---|---|
| #1 | Full | Research note without propagated_to AND no thesis Log reference | Important |
| #16 | Full | Stale snapshots (>180 days) | Nice to Have |
| #18, #20, #23 | Full | Graph health (existence, staleness, missing/ghost entries) | Important |
| #32 | Full | Orphaned ticker references (research note `ticker:` matches no thesis) | Nice to Have |
| #33 | Full | Closed thesis file still in `Theses/` | Important |
| #35 | Full + scoped | `_hot.md` schema drift | Important (silent no-op source) |
| #36 | Full | `_prune-manifest` state | Important if in-progress; Nice to Have if completed >30 days |
| #37 | Full + scoped (if marker) | `.rename_incomplete.*` markers | Important |
| #38 | Full | State marker hygiene (`.sync_all_fresh`, `.graph_invalidations` aging) | Nice to Have |
| #39 | Full | `propagated_to:` producer contract | Important (post-spec) / Nice to Have (pre-spec) |
| #41 | Full | `_sync-manifest` aging | Important if in-progress; tiered if completed |
| #42 | Full + scoped | `_hot.md` truncation markers | Important |
| #43 | Full | Stale locks | Nice to Have (user-triggered recovery) |
| #45 | Full | `_compare-manifest` aging | Important if in-progress; tiered if completed |
| #46 | Full | `.archive_ticker_registry.md` validation | Nice to Have |
| #47 | Full | `_stress-test-manifest` aging | Important if in-progress |
| #48 | Full | `_status-manifest` aging | Important if in-progress |
| #49 | Full | `_thesis-manifest` aging | Important if in-progress |

Scoped mode always runs #35 and (if marker exists) #37, because these are vault-global concerns whose cost is low enough to gate weekly rather than monthly.

---

## 13. Commit archaeology (H1–H4 summary)

Recent hardening commits and their contracts:

| Commit | Layer | What it changed |
|---|---|---|
| `569b1e6` Pre Flight Safety | T6 | Pre-flight contract (Procedure 1.5 ownership, Procedure 2 marker, Procedure 3 sanitization, Procedure 4 section probe) |
| `eaef12d` Workflow Hardening | T5 | 5.1 scenario reverse mode; 5.2 scenario classification approval; 5.3 deepen missing-section handling; 5.4 thesis new-sector handling; 5.5 clean orphan protection; 5.7 User Guide §15 additions |
| `4d12f96` Transaction Integrity | T1–T4 | Manifest skeletons, atomicity rules, `propagated_to:` producer contract, retry logic |
| `d6247da` User Guide refactor | — | First restructure; redistributed tier-labeled content |
| `dda1cc9` Concurrency Integrity | C1–C4 | `/compare` per-ticker locks, multi-ticker partial rollback, LOCK_LOST detection |
| `597885e` Transaction Completeness | H1–H4 | H1: `_thesis-manifest` + `/lint #49` + `/rollback` cascade 2.5f; H2: `/catalyst` hard-abort on snapshot failure; H3: `/rollback` scan Macro + Sectors; H4: `/sync` idempotency secondary keys |

Later commits (User Guide restructure Apr 19, 2026) pushed deep technical content here; User Guide became user-facing surface.

---

## Appendix: File ownership matrix

| File / directory | Creators | Modifiers | Cleaners |
|---|---|---|---|
| `Theses/*.md` | `/thesis` | `/sync`, `/deepen`, `/status`, `/compare`, `/scenario`, `/stress-test`, `/prune`, `/rename`, `/rollback` | `/status` (archive), `/prune` (archive) |
| `Research/*.md` | `/ingest`, `/thesis`, `/deepen`, `/compare`, `/scenario`, `/stress-test`, `/surface`, `/brief`, manual | — (Tier 2 immutable bodies) | manual `mv` to `_Archive/Briefs/` |
| `Sectors/*.md` | manual (prompt §6.4.1), `/thesis` (scaffold) | `/sync`, `/status`, `/compare`, `/prune`, manual | — |
| `Macro/*.md` | manual | `/sync`, `/scenario` | — |
| `_hot.md` | `/sync` (auto-create) or any of 11 skills via CLAUDE.md rule #9 | 11 skills (Absorb/Synthesize/Decide + Reconcile subset) | manual when `/lint #35` or `#42` fires |
| `_graph.md` | `/graph` | `/graph`, `/rename` (adjacency header only) | `/graph` |
| `_catalyst.md` | `/catalyst` | `/catalyst` | `/catalyst` (overwrite) |
| `.last_sync` | `/sync`, `/sync all` | `/sync`, `/sync all` | — |
| `.sync_all_fresh` | `/sync all` | — | `/graph` (consume & delete) |
| `.graph_invalidations` | `/status` (closure), `/prune` | append only | `/graph last` (consume & delete) |
| `.rename_incomplete.TICKER` | `/rename` (on post-mv Edit failure) | `/rename` (repair retries) | `/rename` (auto-delete when empty) |
| `.archive_ticker_registry.md` | `/status`, `/prune` (closures) | append only | — (stale entries tolerated by `/thesis` verification) |
| `.vault-lock*` | all state-modifying skills | own skill only | own skill (explicit release); manual on abandonment |
| `.drift-config.md` | manual (optional) | manual | manual |
| `_Archive/Snapshots/*.md` | destructive skills (pre-edit snapshot) | — | `/clean` |
| `_Archive/Snapshots/_*-manifest-*.md` | multi-file skills (skeleton) | own skill (populate + flip) | `/clean` (after manifest-specific aging rules satisfied) |
