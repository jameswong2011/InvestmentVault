---
type: skill-rationale
skill: /compare
purpose: Design rationale for /compare — per-ticker locks (C4), cross-sector atomic transaction (6.5 fix), propagated_to atomicity, manifest contract.
last_reviewed: 2026-04-20
---

# /compare Design Rationale

> SKILL.md contains operational rules. This file explains per-ticker lock acquisition (not joint locks), the cross-sector atomic rollback pattern, the `propagated_to:` atomicity rule, and the per-sector batch ID scoping.

---

## §1 Per-ticker locks (C4 — not joint locks)

### §1.1 Why NOT a single joint `+`-delimited lock

Pre-C4 design used a joint lock like `.vault-lock.A+B+C`. Broke on hyphen-containing tickers:
- `BRK-B` — the hyphen is part of the ticker
- `BF-A`, `PBR-A` — same pattern

A joint lock `.vault-lock.BRK-B+AAPL+NVDA` would be parsed ambiguously — where does the first ticker end? The `+`-delimiter collides with `-` used in tickers.

### §1.2 Per-ticker acquisition design

Each ticker gets its own lock file (`.vault-lock.A`, `.vault-lock.B`, `.vault-lock.C`). Acquire sequentially. If any acquisition fails (another skill holds a ticker), rollback — release all previously-acquired locks in this run.

Rollback-on-partial-acquisition prevents:
- Holding a proper subset of the compare set while concurrent skills hold the rest
- Deadlock between two `/compare` runs that share some tickers (`/compare A vs B` + `/compare B vs C` — both would acquire B first, then one would wait forever for A or C)

### §1.3 Per-ticker vs vault-wide trade-off

Could use vault-wide lock for simplicity. But `/compare` is a natural multi-ticker operation — allowing concurrent `/compare NVDA vs AMAT` with `/compare BESI vs AMAT` (no overlap) requires per-ticker granularity.

Per-ticker locks match the per-ticker nature of the compare operation; vault-wide would unnecessarily serialize independent comparisons.

---

## §2 Phase 0 thesis existence check + web-supplemented mode

### §2.1 Why require at least one thesis

`/compare` without any thesis anchor is essentially a web-research operation with comparison framing. No vault-depth analysis possible, no thesis update to propagate. Rather than degrade silently, hard-stop and require at least one thesis — that thesis is the analytical anchor that vault insights hang off.

### §2.2 Web-supplemented mode (Phase 0 option a)

When some tickers have theses and others don't, two paths:
- **(a) Proceed with web research for missing**: lighter comparison. Missing tickers use web research in Phase 1. Phase 5 vault updates apply ONLY to tickers with existing theses. Report appends `💡 Consider /thesis [TICKER] to formalize coverage.`
- **(b) Stop and run /thesis first**: full-depth comparison after thesis creation.

(a) unblocks comparison when the user wants quick insight without the overhead of full thesis creation. (b) preserves the "thesis is the analytical anchor" design when depth matters.

### §2.3 Why no Phase 5 updates for web-supplemented tickers

Missing tickers have no `Theses/TICKER - *.md` to update — no Log to append, no `## Related Research` to extend. The comparison research note still wikilinks them (for future-thesis cross-reference), but no thesis-level propagation is possible until a thesis exists.

---

## §3 `propagated_to:` atomicity (Phase 5.4)

### §3.1 Why omitted at write time (Phase 5.1)

Mirrors `/scenario` Phase 6.1 + 6.3 atomicity. If any per-thesis Log append in Phase 5.2 fails (file lock, missing `## Log` section, malformed frontmatter), pre-writing `propagated_to: [...]` would falsely claim every listed ticker received its Log entry. Future `/sync` Case 2b would skip them all, never retrying the failed appends — permanent audit gap.

The all-or-nothing rule trades a single trivial frontmatter Edit at Phase 5.4 for guaranteed eventual consistency.

### §3.2 Why never partial

Partial `propagated_to:` would claim SOME failed-target tickers as propagated when their Log entries never landed → permanent audit gap → future `/sync` runs silently skip because the dedup hint says "already done."

All-or-nothing:
- **All succeeded**: write `propagated_to: [all tickers with existing theses]`. `/sync` Case 2b skips.
- **One or more failed**: do NOT write `propagated_to:` at all. Next `/sync` detects each via file-direct fallback (research note's `tags:` and body wikilinks list each compared ticker), checks per-thesis idempotency, re-attempts failed targets.

Succeeded targets re-encounter the per-thesis idempotency check on retry — wikilink-presence in `## Log` produces skip. No duplicate Log entries.

### §3.3 Why Related Research (Phase 5.3) runs regardless

Adding the comparison wikilink to `## Related Research` is wikilink registration (presence record), NOT propagation claim. Runs regardless of Phase 5.2 Log outcome because:
- Related Research is a discovery-aid list, not a Log-propagation record
- Even a failed-Log-append target benefits from having the comparison discoverable from its thesis
- `/lint #23` reverse-index consistency doesn't care about Log state; it cares about wikilink presence

Separation: `propagated_to:` = "Log propagation succeeded"; Related Research = "reference exists." Different semantics.

---

## §4 Cross-sector atomic transaction (Phase 5.5 — 6.5 fix)

### §4.1 Why cross-sector atomicity

Pre-6.5: `/compare` edited each sector note's analytical text independently. If sector A's write succeeded but sector B's write failed, the vault ended up in mixed state — sector A reflects new comparison insight, sector B doesn't. Partial cross-sector propagation is worse than no propagation because:
- `/sync` sees a changed sector note (A) without corresponding insight in the other affected sectors (B)
- `/lint` can't easily detect "sector A received this comparison's update but sector B didn't" — it checks individual notes, not cross-sector consistency
- User discovers inconsistency weeks later when re-reading sector B

All-or-nothing: either all sector notes receive the update, or none do.

### §4.2 Transaction pattern — pre-snapshot then apply

Phase 5.5a snapshots ALL target sectors FIRST (via `cp` to `_Archive/Snapshots/`). If any snapshot fails, abort pre-mutation — no destructive edits yet. Stores `snapshot_map: {sector_note_path → snapshot_path}` for potential rollback.

Phase 5.5b applies sector edits in sequence. Per edit:
- Success → append to `attempted_and_succeeded` list
- Failure → roll back ALL prior succeeded edits via `cp` from snapshots → abort transaction → report

Rollback uses the snapshots taken in 5.5a. Clean reverse of partial state.

### §4.3 Confidence handling in sector resolution

Per resolved sector (via `_shared/sector-resolution.md`):
- **`match_confidence: none`**: emit no-match warning. Remove sector from atomic transaction set. Compare still completes for sectors that DO resolve; unresolved sectors are reported but don't participate in atomicity.
- **`match_confidence: substring`**: emit `log_message` AND pause for explicit user confirmation before modifying analytical text. If declined, remove from transaction set.
- **`match_confidence: normalized` or `exact`**: proceed silently (normalized logs in final report).

### §4.4 Abort-transaction surfacing

On failure, report:
- Sectors successfully edited (now rolled back): list
- Sector that failed: path + reason
- Research note status: preserved (Phase 5.1 already wrote it)
- Thesis Logs status: preserved (Phase 5.2 already wrote them)
- `propagated_to:` status: depends on Phase 5.4 — if all Log appends succeeded, it was already written; if any failed, it was already omitted

Research note + thesis Logs are PRESERVED because they landed before the sector transaction — only sector-note state reverts.

---

## §5 Per-sector batch ID scoping (Phase 5.5 + Snapshot batch ID note)

### §5.1 Why distinct `snapshot_batch` per sector

`/rollback` Step 2.5 groups snapshots by `snapshot_batch` for cascade detection. Two sector notes sharing `compare-2026-04-19-1530` would couple unrelated sectors on rollback — user rolls back one sector and gets offered to cascade-restore the other even though they're independent.

Per-sector scoping: `compare-semiconductors-YYYY-MM-DD-HHMMSS` vs `compare-cybersecurity-YYYY-MM-DD-HHMMSS`. Cascade only couples snapshots truly belonging together.

### §5.2 Single-sector case

When all compared theses share one sector, only one sector note exists. Slug still included for format uniformity: `compare-semiconductors-YYYY-MM-DD-HHMMSS`. Keeps batch-ID format consistent regardless of sector count — no special-case logic.

### §5.3 Thesis Log entries don't use batch ID

Thesis Log entries are not snapshots. They don't carry `snapshot_batch:` — no cascade-coupling risk at the Log-entry level. The research note wikilink in the Log entry provides the cross-reference for audit purposes.

---

## §6 Manifest sidecar (Phase 5.5c)

### §6.1 Why manifest even for atomic success

Matches pattern from `/sync` Step 7.5, `/prune` Stage 1.5, `/status` Step 3.0.5, `/thesis` Step 3.5: manifest records every file touched + outcome. Enables `/rollback` cascade + crash-recovery.

For successful `/compare` run, manifest records:
- Tickers compared
- Sector writes: succeeded list + snapshot paths
- Rolled-back sectors (none if `status: completed`)
- Thesis Log appends: per-ticker succeeded/failed
- Research note + `propagated_to:` state

For aborted `/compare` run (transaction rollback), `status: rolled-back` — clean abort marker. `/lint #45` distinguishes `completed | rolled-back | in-progress`.

### §6.2 Why `status: in-progress` is Critical

`/compare` is a multi-phase transaction. In-progress manifest means the skill crashed between writing the research note + Log appends + starting sector edits. User needs to investigate:
- Did Phase 5.5b start? If yes, some sectors may be edited + some not.
- Did the per-sector snapshots all land? Those are the rollback anchors.
- Does `propagated_to:` reflect reality?

No auto-recovery — `/lint #45 Critical` surfaces for manual investigation. Manual `/rollback` can restore sectors using the manifest's snapshot references.

---

## §7 Phase ordering — research note first, sector edits last

### §7.1 Why 5.1 → 5.2 → 5.3 → 5.4 → 5.5

Sequence:
1. **5.1**: write research note (without `propagated_to:`) — Tier 2 append-only; no rollback needed
2. **5.2**: per-thesis Log appends — tracked failure list
3. **5.3**: Related Research wikilink additions — independent of 5.2 outcome
4. **5.4**: atomicity decision for `propagated_to:` (based on 5.2 results)
5. **5.5**: cross-sector atomic transaction (sector analytical edits)

Research note + Log appends land BEFORE sector edits because:
- Research note is Tier 2 append-only (preserved even on sector-transaction abort)
- Thesis Log appends are Tier 2 append-only (preserved on sector abort)
- Sector edits are rewrites of analytical text (reversible via snapshots)

Phase 5.5 abort rolls back sectors only; preserves research note + thesis Logs. The user sees the comparison + per-thesis insights even if sector-level synthesis fails.

---

## §8 Phase 3 "Dynamic Analysis" — why this is the value

Static comparison (Phase 2) is table-filling — business model columns, financial metrics. Useful but shallow. Phase 3 is where investment insight lives:
- Market share trajectory (structural vs cyclical shift)
- Pricing power divergence (what drives it)
- Technology trajectory (platform-shift positioning)
- Logical tension (what each company needs to be true that the other's success disproves)
- Scenario divergence (when the underdog wins)
- Customer/supplier overlap (pricing power + correlated risk)

Without Phase 3, `/compare` is a glorified side-by-side spreadsheet. The "logical tension" point in particular surfaces non-consensus insights — if both companies can't simultaneously be right, one is mispriced.
