---
type: skill-rationale
skill: /status
purpose: Design rationale and transaction-ordering context for /status. NOT loaded at invocation — SKILL.md references by §N.M.
last_reviewed: 2026-04-20
---

# /status Design Rationale

> SKILL.md contains operational rules. This file explains the T2.2 manifest contract, C4 batch-ID qualification, reaffirm audit-trail requirement, sector-note dry-run design, reopen anti-collision semantics, and the closure ordering contract. Maintainers read this; the LLM executing /status does not.

---

## §1 Reaffirm flow design (Step 2R)

### §1.1 Why always write the Log entry

Prior spec suggested reaffirm was "lightweight", which some implementations interpreted as "skip Log entry when no drift flag exists." That created an audit gap — a user's proactive conviction reaffirmation left no trace in the Log. The resulting audit story was "user never reviewed this thesis" even when they explicitly did.

Always writing the Log entry closes that gap; the tiny overhead is worth the auditability. Reaffirm is idempotent-safe: it can be run even if no drift flag is currently active, because the operation always appends a Log entry and always resets the drift detection window (resetting an already-clean window is harmless).

### §1.2 Drift flag cleanup coupling

Step 2R.5's Recent Conviction Changes entry + `## Open Questions` drift-flag resolve work together. `/sync` Step 6 checks `_hot.md` for active drift flags; clearing the flag here prevents it from re-appearing as an Open Question on the next sync.

### §1.3 Why `"Conviction reaffirmed"` prefix must not change

`/sync` Step 3e drift detection uses `"Conviction reaffirmed"` as the window anchor. Registry entry: `.claude/skills/_shared/log-prefixes.md §5`. Changing the prefix silently breaks drift detection's anchor logic — drift windows would count entries from before the reaffirm, producing false positives.

`/lint #29` enforces registry alignment across producer + consumer + vault presence.

---

## §2 Batch ID qualification (C4 fix)

### §2.1 Why ticker qualifier in batch ID

Pre-C4 format `status-YYYY-MM-DD-HHMMSS` could collide when two concurrent `/status` runs on different tickers hit the same HHMMSS. Simultaneous `/status NVDA conviction...` and `/status AMAT status...` would write two snapshots with identical `snapshot_batch:` values — `/rollback` cascade detection would then pair them incorrectly.

New format `status-TICKER-YYYY-MM-DD-HHMMSS` makes every batch unique even under concurrent invocations.

### §2.2 Why batch ID always generated — even when thesis snapshot is skipped

`draft→active` skips the thesis snapshot (no analytical content changes; only frontmatter `status:` field flips). But Step 5a still needs the batch ID for the sector note snapshot — a batch ID ties the sector snapshot to this `/status` run for cascade restore.

Generate HHMMSS unconditionally at Step 3.0; reuse in Step 5a regardless of whether Step 3.1 ran.

---

## §3 Manifest skeleton contract (T2.2 fix)

### §3.1 Why skeleton before any file modification

Prior behavior: manifest written at end of run as "best-effort audit trail". End-write failure silently violated the cascade-recovery contract — `/rollback` saw pre-status snapshots but no manifest to distinguish partial from complete runs.

T2.2 pattern matches `/sync` Step 2.9 and `/prune` Stage 1.5: skeleton written BEFORE any mutation. Skeleton write failure hard-aborts pre-mutation — no thesis snapshot, no frontmatter edit, no sector edit, no archive move. User re-runs after fixing filesystem issue; no silent corruption possible.

### §3.2 Why Reaffirm flow (Step 2R) skips the manifest

Reaffirm is a single Log append. No multi-file transaction, no snapshot, no sector/graph/archive work — nothing to manifest. Skipping the skeleton keeps the fast-path operation fast.

### §3.3 Incremental population across Steps 3.1 → 7.5 → 7.6 → 7.9

Each step appends completion state to the manifest via Edit. Crash between Step 5a and Step 7.5 → manifest reflects thesis + sector edits but NOT archive move → `/rollback` sees this partial state and offers appropriate cascade options (either thesis-only restore or full transaction restore).

### §3.4 Flip-failure handling at Step 7.9

If the status flip fails silently (Edit landed but frontmatter didn't update), manifest persists as `in-progress`. `/lint #48` surfaces it as Important. Do NOT rollback the `/status` on flip failure — all stages already succeeded; only the completion marker failed. User manually edits manifest to `status: completed`.

---

## §4 Closure ordering contract (Steps 4/5/6/7.5/7.6/7.9)

### §4.1 Why archive move is at Step 7.5, not Step 4

Change order matters for closure transactions:
1. Step 4: frontmatter edit (`status: closed`)
2. Step 5: sector note edit (remove from Active Theses)
3. Step 6: graph update deferred (no-op — `/graph` owns `_graph.md`)
4. Step 7: `_hot.md` update (Recent Conviction Changes, Portfolio Snapshot)
5. **Step 7.5: archive `mv` (final)**
6. Step 7.6: `.graph_invalidations` write
7. Step 7.9: manifest flip

If Step 4 archived the file immediately, subsequent steps (5, 7, 7.6) would need to reference the archived path in `_Archive/`, creating ordering complexity. Keeping the file in `Theses/` with `status: closed` until all metadata updates succeed means every reader sees the thesis in its original location with a consistent "closed" signal.

The intermediate state (`status: closed` in `Theses/`) is **safe and recoverable**:
- `/sync` skips `status: closed` theses in propagation analysis (§2.5 skill-origin gate)
- `/lint #33` flags the pending move for user awareness
- Re-running the closure OR manual `mv "Theses/[file]" "_Archive/[file]"` completes it

### §4.2 Archive-path collision check (Step 7.5a)

`mv` on POSIX silently overwrites. Prior closures of the same ticker-and-name combination would produce silent data loss. Pre-move check + three user options (suffix old, suffix new, cancel) prevents this.

### §4.3 Archive move failure — metadata updates already landed

If the `mv` fails, all metadata (sector note, graph invalidations, `_hot.md`) already succeeded. Do NOT attempt to undo — the intermediate state is self-consistent. Report the completion command for manual resolution. The closure is logically complete.

### §4.4 Graph invalidation (Step 7.6) — why before `/graph last`, not inline

`/graph last`'s incremental path only re-extracts adjacency for thesis files whose mtime advanced since the last graph write. Untouched neighbors keep stale `cross-thesis:` references until their next edit, accumulating dangling graph edges (`/lint #21` flags).

`.graph_invalidations` — written here, consumed by next `/graph last` — forces re-extraction of neighbors that referenced the closed thesis even if they haven't been edited. Without this list, the graph would need a full rebuild every closure.

### §4.5 Why skip Step 7.6 if Step 7.5 move failed

If archive move failed, the closure is incomplete — thesis still in `Theses/`. Writing `.graph_invalidations` for neighbors would force them to re-extract adjacency against a still-living thesis, which correctly preserves their `cross-thesis:` references. Better to skip and let the next run (after manual completion) write the invalidation list correctly.

---

## §5 Sector note dry-run (Step 5.1)

### §5.1 Why dry-run before snapshot

Unconditional snapshotting creates orphan snapshot files for no-op transitions (e.g., `active→monitoring` on a sector note that doesn't track monitoring status). These accumulate disk usage, clutter `/rollback` snapshot lists, and dilute cascade-detection signal.

The dry-run keeps snapshots aligned with actual edits without sacrificing safety. When `edit_planned: false`, no snapshot, no edit — the transition already reflects current sector state.

### §5.2 Decision matrix per transition

Different transitions require different sector-note reactions:
- `draft→active`, `monitoring→active`, `closed→active`: add to Active Theses (with cleanup variations)
- `active→monitoring`: annotate per sector convention (only if sector distinguishes monitoring)
- `active→closed`: remove from Active Theses
- conviction change: update displayed conviction level (only if sector displays conviction)

The matrix column "Set `edit_planned: true` when..." captures the specific precondition for each row.

### §5.3 Detection indicators — how to tell if sector distinguishes monitoring/conviction

Sector notes have variable structure. The heuristics:
- **Monitoring distinction**: section heading `## Monitoring`, suffix `(monitoring)` on wikilinks, `monitoring:` annotation, or any thesis wikilink with monitoring marker
- **Conviction display**: `(high|medium|low)` suffix adjacent to wikilinks, `| Conviction |` column header, or sections grouped by conviction level

Absence of these indicators → sector doesn't distinguish that dimension → `edit_planned: false` for transitions touching only that dimension.

---

## §6 Reopen anti-collision check (closed→active)

### §6.1 Why the two-check composition exists

`closed→active` has a specific double-listing hazard absent in other transitions. The typical path:

1. User closes thesis via `/status active→closed` → Step 5b removes wikilink from sector Active Theses → `/status` archives.
2. User later runs `/rollback TICKER` to reopen. Rollback cascade (Step 2.5) typically restores BOTH thesis AND sector-note snapshot taken before closure — sector note reverts to PRE-closure state, which already has the wikilink in Active Theses.
3. User (per User Guide §3.F "Undo a closure") checks restored `status:` frontmatter. If pre-closure snapshot: status is already `active`, no `/status` run. If post-closure snapshot: user runs `/status TICKER status closed→active`.

At step 3, if sector was already restored by rollback cascade, wikilink is present — unconditional Step 5b would add a duplicate. The check-before-add prevents this.

### §6.2 Four case outcomes

The composed "present in Active OR present in Closed/Archived" check handles every scenario:
- **In Active only** (clean rollback-restored state): no edit needed
- **In Closed/Archived only** (manual mv reopen without sector restore): edit — add to Active, remove from Closed/Archived
- **In both** (double-listed from messy prior state): edit — leave Active alone (or dedupe), remove from Closed/Archived
- **In neither** (partial rollback or fresh manual reopen): edit — add to Active

Single presence check → all four cases handled without separate "did the user just run /rollback?" detection.

### §6.3 Closed/Archived cleanup as second composition

If a prior closure added the thesis to a sector's `## Closed/Archived` section, that stale entry persists until explicitly removed. Sector note snapshot rollback (scenario 1 above) gets it for free. Manual reopen (`mv` + `/status closed→active` without sector restore) would leave it stale — second check catches this.

---

## §7 Trigger conflict warning (Step 4 conviction)

When new conviction contradicts an active Conviction Trigger condition (e.g., moving to `high` but a `→ LOW if X` trigger is currently active), warn the user. This isn't a block — the user may knowingly override the trigger (e.g., trigger condition was transient, thesis revised). Warning surfaces the contradiction so the override is explicit.

`⚠️ Active trigger conflicts with new conviction: [quote trigger]. Confirm this is intentional.`

---

## §8 `/clean` interaction — status manifest 90-day threshold

Unlike `/prune`'s 30-day regret-recovery retention (T5 5.2), `/status` does not have a defined regret-recovery window. Conviction and status changes are typically intentional single-thesis operations, not mass-triggered events. 90-day `/clean` threshold is sufficient.

`/lint #48` surfaces in-progress status manifests as Important regardless of age (crash recovery signal). Completed manifests age per the 90-day threshold with Nice to Have severity beyond.
