---
name: status
description: Change conviction level or status on a single thesis. Use when user says "change conviction", "downgrade", "upgrade", "move to monitoring", "close [TICKER]", or "set [TICKER] to [level]".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * cp * mkdir * mv * find * grep * cat * sort * printf * ls *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Execute a conviction or status change on a single thesis. This is the atomic operation that closes the loop after `/stress-test`, `/scenario`, `/deepen`, `/compare`, or any manual reassessment.

## Arguments

$ARGUMENTS should follow one of these patterns:

**Conviction or status change**: `TICKER field old→new [rationale]`
- `NVDA conviction medium→low China risk unhedgeable`
- `BESI status active→monitoring awaiting Q3 earnings`
- `LITE conviction low→medium photonics design wins accelerating`
- `SHOP status active→closed thesis invalidated by margin compression`

**Drift acknowledgment**: `TICKER reaffirm [rationale]`
- `NVDA reaffirm earnings miss was one-time; competitive position unchanged`
- `BESI reaffirm hybrid bonding thesis intact despite cycle weakness`

If $ARGUMENTS is ambiguous or incomplete, ask the user to clarify the ticker, field, direction, and rationale before proceeding.

If $ARGUMENTS matches the `reaffirm` pattern, skip to **Step 2R (Reaffirm Flow)** below.

## Step 1: Validate

1. **Find the thesis**: Search `Theses/` for a file matching the ticker. If not found, stop: `⚠️ No thesis found for [TICKER] in Theses/. Nothing to update.`
2. **Read the full thesis note** to understand current state.
3. **Verify current value**: Confirm the `old` value in $ARGUMENTS matches the actual frontmatter. If it doesn't, stop and report the mismatch: `⚠️ Expected [field]: [old] but found [field]: [actual]. Confirm the intended change.`
4. **Parse the change type**:
   - `conviction` change → proceed to Step 2
   - `status` change to `closed` → proceed to Step 2 (will trigger archive flow)
   - `status` change to anything else (`active→monitoring`, `draft→active`, `monitoring→active`) → proceed to Step 2

## Step 2R: Reaffirm Flow (drift acknowledgment)

**Only entered when $ARGUMENTS matches `TICKER reaffirm [rationale]`.** This is a lightweight operation — no frontmatter change, no snapshot, no sector/graph update.

1. **Find and read the thesis** (same as Step 1.1–1.2).
2. **Extract drift context**: Scan the last 5 Log entries. Identify entries with "weakened" or "strengthened" sentiment. Count the drift pattern.
3. **Present the evidence summary and wait for confirmation**:
   ```
   Drift review for [[Theses/TICKER - Company Name]]:
     Current conviction: [level]
     Recent log sentiment:
       - YYYY-MM-DD: [summary] — [weakened/strengthened/unchanged]
       - YYYY-MM-DD: [summary] — [weakened/strengthened/unchanged]
       - ...
     Drift signal: [N]/[window] entries flagged headwinds (or tailwinds)

     Reaffirming conviction at [level] with rationale: [from $ARGUMENTS]
     This resets the drift detection window for future /sync runs.

   Confirm? (y/n)
   ```
   **Do NOT proceed without explicit user confirmation.**
4. **Append Log entry** (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Conviction reaffirmed at [level] after drift review — [rationale from $ARGUMENTS]
   ```
   > **Drift coupling**: `/sync` Step 3e uses `"Conviction reaffirmed"` as a drift window anchor. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §5. Do not change this prefix without updating the registry and `/sync`; `/lint` check #29 flags drift.

5. **Update _hot.md** (read first, then edit — do NOT touch Latest Sync or Sync Archive):
   - **Recent Conviction Changes**: Add entry: `- **[TICKER]**: conviction [level] reaffirmed — [rationale]`

6. **Report**:
   - **Reaffirmed**: [TICKER] conviction [level] maintained
   - **Drift window reset**: next /sync will anchor drift detection after this entry
   - **No snapshot, sector, or graph changes**

**Stop here — do not continue to Step 2 or beyond.**

---

## Step 2: Confirm (Tier 3 — Mandatory)

Present the proposed change and **wait for user confirmation** before proceeding:

```
Proposed change:
  Thesis: [[Theses/TICKER - Company Name]]
  Field: [conviction | status]
  Change: [old] → [new]
  Rationale: [from $ARGUMENTS]
  Side effects: [list what will be updated — sector note, archive move, graph cleanup]

Confirm? (y/n)
```

**Do NOT proceed without explicit user confirmation.** These are investment decisions per CLAUDE.md Tier 3.

## Step 3: Snapshot

### 3.0: Generate batch ID (always)

Generate `HHMMSS` once at the start of this step (6-digit second-precision prevents same-minute batch collisions across skills):
```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
```
Use `status-YYYY-MM-DD-$HHMMSSSS` as the `snapshot_batch` value across **all** snapshots created in this run (thesis snapshot in Step 3.1, sector note snapshot in Step 5a). Reusing a single batch ID lets `/rollback` cascade detection restore both files atomically as a single operation.

> **Draft→active note**: The batch ID is still generated even when Step 3.1 is skipped — Step 5a needs it for the sector note snapshot.

### 3.1: Thesis snapshot

Create a pre-change snapshot (conviction and most status changes are Tier A edits on the thesis body):

```bash
cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-$HHMMSS).md"
```

Read the newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - Company Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMMSS
```

**Exception**: Skip the thesis snapshot for `status: draft→active` (no analytical content is being changed on the thesis body — only the status frontmatter field is flipped). The sector note snapshot in Step 5a still runs, because Step 5b modifies the sector note even for this transition (adding the thesis to Active Theses).

## Step 4: Apply Change

### For conviction changes:
1. Update `conviction:` in frontmatter
2. Append Log entry (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Status change: conviction [old] → [new] — [rationale from $ARGUMENTS]. Snapshot: [[_Archive/Snapshots/...]]
   ```
   > **Drift coupling**: `/sync` Step 3e uses `"Status change: conviction"` as a drift window anchor. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §6. Do not change this prefix without updating the registry and `/sync`; `/lint` check #29 flags drift.

3. **Conviction trigger check**: Read the Conviction Triggers section. If the new level contradicts a trigger condition (e.g., moving to high but a → LOW trigger is active), warn: `⚠️ Active trigger conflicts with new conviction: [quote trigger]. Confirm this is intentional.`

### For status changes (non-closure):
1. Update `status:` in frontmatter
2. Append Log entry (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Status change: [old] → [new] — [rationale from $ARGUMENTS]. Snapshot: [[_Archive/Snapshots/...]]
   ```

### For status → closed (archive flow):
1. Add final Log entry:
   ```
   ### YYYY-MM-DD
   - CLOSED: [rationale from $ARGUMENTS]. Archived.
   ```
2. Change frontmatter: `status: closed`

> **The file is NOT moved yet.** The archive move runs in Step 7.5, after all metadata updates (sector note, graph, `_hot.md`) succeed. This ordering guarantees that if the skill fails mid-execution, the thesis file remains in `Theses/` with `status: closed` — no ghost graph entries, no broken wikilinks, no stale sector note references. The intermediate state (`status: closed` in `Theses/`) is recoverable by re-running the closure or manually executing the `mv` command from Step 7.5.

## Step 5: Update Sector Note

### 5.0: Locate the sector note

Resolve the sector note using the canonical procedure: **`.claude/skills/_shared/sector-resolution.md`**. Inputs: thesis's `sector:` frontmatter. Outputs: `sector_note_path`, `match_confidence`, `log_message`.

- If `match_confidence` is `none`: emit the contract's no-match warning, skip the rest of Step 5, and proceed to Step 6.
- If `match_confidence` is `normalized` or `substring`: emit the contract's `log_message` in the Step 8 report, then proceed with the resolved sector note.
- If `match_confidence` is `exact`: proceed silently with the resolved sector note.

### 5.1: Dry-run — determine whether an edit is actually needed

Read the sector note's content and analyze what Step 5b would do for this specific transition. The goal is to avoid a redundant snapshot (and redundant downstream noise) when the transition is a no-op against the current sector note state.

Decision matrix — set `edit_planned: true` only when at least one of the conditions below is met:

| Transition | Check against sector note | Set `edit_planned: true` when... |
|---|---|---|
| `draft→active` | Is the thesis wikilink already present in the Active Theses section? | Thesis wikilink ABSENT — Step 5b will add it. |
| `monitoring→active` | Is the thesis wikilink already in the Active Theses section (not annotated as monitoring)? | Thesis wikilink absent from Active Theses, OR present but annotated as monitoring (annotation will be removed). |
| `closed→active` (reopen) | (1) Is the thesis wikilink already present in the Active Theses section? (2) Is the thesis wikilink also present in a Closed/Archived section? | Thesis wikilink ABSENT from Active Theses **OR** PRESENT in a Closed/Archived section (stale entry from a prior closure that needs cleanup). The two checks compose independently — either condition alone triggers `edit_planned: true`. See "Reopen anti-collision check" below for why this row exists. |
| `active→monitoring` | Does the sector note distinguish monitoring (e.g., separate "Monitoring" section, `(monitoring)` suffix on wikilink, conviction column, or annotation convention)? | Sector note distinguishes monitoring AND the thesis is NOT already annotated as such. |
| `active→closed` | Is the thesis wikilink in the Active Theses section? | Thesis wikilink present — Step 5b will remove it (and optionally add to Closed/Archived). |
| Conviction change | Does the sector note display conviction levels alongside thesis links (e.g., `[[TICKER]] (medium)`, a conviction column, or a grouped-by-conviction structure)? | Sector note displays conviction AND the displayed value differs from the new conviction. |

Distinguish "sector note distinguishes monitoring" and "sector note displays conviction" by grepping the sector note body:
- Monitoring distinction indicators: `## Monitoring`, `(monitoring)`, `monitoring:`, or any thesis wikilink suffixed with a monitoring marker.
- Conviction display indicators: `(high)`, `(medium)`, `(low)` adjacent to thesis wikilinks, OR a `| Conviction |` column header, OR section headings grouped by conviction level.

### Reopen anti-collision check (closed→active only)

`closed→active` has a specific double-listing hazard that doesn't apply to other transitions. The typical path to this transition is:

1. User closes thesis via `/status active→closed` → Step 5b removes the wikilink from sector Active Theses, `/status` archives the thesis.
2. User later runs `/rollback TICKER` to reopen. The rollback cascade (Step 2.5) typically restores BOTH the thesis file AND the sector-note snapshot taken before closure — so the sector note is reverted to its PRE-closure state, which already has the wikilink in Active Theses.
3. User (per User Guide §3n) checks the restored `status:` frontmatter. If the snapshot was pre-closure: status is already `active`, no `/status` run needed. If the snapshot was post-closure: user runs `/status TICKER status closed→active`.

At step 3, if the sector was already restored by the rollback cascade, the wikilink is present — Step 5b would add a duplicate and the sector note would end up double-listing the thesis. The decision-matrix row above prevents this: check wikilink presence first, only set `edit_planned: true` when ABSENT.

Manual `mv` reopens (user moved the file from `_Archive/` back to `Theses/` without running `/rollback`) follow the same logic: sector note was never restored, wikilink IS absent from Active Theses, `edit_planned: true`, Step 5b adds it.

**Closed/Archived section cleanup** is the second composition check. If a prior closure added the thesis to a Closed/Archived section and the user then rolled back to a pre-closure sector snapshot (which has the thesis only in Active Theses), the Closed/Archived section is now clean. But if the user manually reopened (`mv` from `_Archive/` + `/status closed→active`) WITHOUT restoring the sector note, the Closed/Archived section still carries the stale entry even though Active Theses may or may not have it. The composed check catches every case:
- In Active only → no edit (from rollback, already clean)
- In Closed/Archived only → edit (add to Active, remove from Closed/Archived)
- In both (double-listed from a messy prior state) → edit (leave Active alone or dedupe, remove from Closed/Archived)
- In neither → edit (add to Active)

Either way, the presence check in Step 5.1 is the single source of truth — no separate "did the user just run /rollback?" detection is needed.

If `edit_planned: false` after evaluating: skip both Step 5a and Step 5b. Report in Step 8 as `Sector note: no edit needed — [TICKER] transition [old→new] already reflects current sector note state.` Proceed to Step 6.

### 5a: Pre-edit snapshot (conditional on Step 5.1 `edit_planned: true`)

Only runs if Step 5.1 set `edit_planned: true`. Before modifying the sector note, snapshot it:
```bash
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-$HHMMSS).md"
```
Read the newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMMSS
```
Reuse the batch ID generated in Step 3.0. The snapshot runs for every transition where Step 5.1 determined an edit is required — including `draft→active`, where the thesis snapshot is skipped but the sector note IS being modified. Without this snapshot, a corrupted Edit to the sector note would leave no recovery path.

> **Skip cases**:
> - Step 5.0 returned "no matching sector note" → Steps 5.1, 5a, 5b are all skipped.
> - Step 5.1 determined `edit_planned: false` → Steps 5a, 5b are skipped; no snapshot, no edit.

### 5b: Apply the sector note update (conditional on Step 5.1 `edit_planned: true`)

Only runs if Step 5.1 set `edit_planned: true`. Apply the specific edit identified in Step 5.1's decision matrix:

1. **For status → active** (e.g., draft→active, monitoring→active, closed→active): Add the thesis to the Active Theses section. If it was present with a monitoring annotation, remove the annotation. For `closed→active` specifically, if a "Closed/Archived" section exists in the sector note and contains this thesis, remove the entry from there as well (prevents dual listing: active AND closed).
2. **For conviction changes** (when sector note displays conviction): Update the displayed conviction level for this thesis to the new value.
3. **For status → monitoring** (when sector note distinguishes monitoring): Move or annotate the thesis to reflect monitoring status per the sector note's convention.
4. **For status → closed**: Remove the thesis from the Active Theses section. If a "Closed/Archived" section exists, add it there. If not, just remove.

> **Why the dry-run matters**: Unconditional snapshotting creates orphan snapshot files for no-op transitions (e.g., `active→monitoring` on a sector note that doesn't track monitoring status). These accumulate disk usage, clutter `/rollback` snapshot lists, and dilute cascade-detection signal. The dry-run keeps snapshots aligned with actual edits without sacrificing safety.

## Step 6: Graph update deferred

`_graph.md` is now owned exclusively by `/graph`.

- **Conviction and non-closure status changes**: no graph impact (graph tracks links, not conviction/status metadata).
- **Status → closed**: after this skill (and after Step 7.5 archive move and Step 7.6 invalidation write), run `/graph last` to remove the archived thesis from the Adjacency Index, reverse indexes, Cross-Thesis Clusters, and other theses' `cross-thesis:` fields. Step 7.6 writes an invalidation list that forces `/graph last` to re-extract adjacency for every neighbor thesis that referenced the closed thesis — without the list, neighbors keep stale `cross-thesis:` references until the neighbor is next edited. Research notes orphaned by the closure are moved to the Orphan list automatically by `/graph last` rebuild.

> **Why deferred**: The incremental path of `/graph last` — augmented by the Step 7.6 invalidation list — captures closure cleanup from current vault state without requiring a full rebuild. No skill-level graph cleanup logic; `/graph` remains the sole writer of `_graph.md`.

## Step 7: Update _hot.md

Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: [TICKER] [field] changed [old] → [new], and the logical next step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry: `- **[TICKER]**: [field] [old] → [new] — [rationale]`
3. **Open Questions**: If closing a thesis, remove any open questions specific to that ticker
4. **Portfolio Snapshot**: Update conviction-level counts if conviction changed; update active/monitoring/closed counts if status changed

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Step 7.5: Archive Move (closure only)

**Only runs for `status → closed` changes. Skip for conviction changes, non-closure status changes, and reaffirmations.**

### 7.5a: Pre-move archive-collision check

`mv` on POSIX silently overwrites the destination if it exists. If the target archive path already contains a file from a prior closure of the same ticker-and-name, silent overwrite would destroy the old archive copy. Check before moving:

```bash
ls "_Archive/TICKER - Company Name.md" 2>/dev/null
```

If a file exists at the destination: pause and present options to the user — do NOT proceed silently:

```
⚠️ Archive-path collision: _Archive/TICKER - Company Name.md already exists from a
   prior closure of this ticker-name combination. Running mv would silently
   overwrite the old archive copy.

Options:
  (a) Timestamp-suffix the old archive, then proceed:
      mv "_Archive/TICKER - Company Name.md" "_Archive/TICKER - Company Name (closed YYYY-MM-DD).md"
      then mv the new thesis to the clean path.
  (b) Timestamp-suffix the NEW archive path instead:
      mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name (closed YYYY-MM-DD).md"
  (c) Cancel — leave thesis in Theses/ with status: closed; user resolves manually.

Confirm (a/b/c):
```

Wait for user selection. If (c), report that metadata updates (sector note, `_hot.md`, invalidation list) already completed and the thesis remains in `Theses/` with `status: closed` pending manual archive resolution.

### 7.5b: Move to `_Archive/`

Move the closed thesis to `_Archive/` (using the path determined in 7.5a — either the clean target or a timestamp-suffixed path):
```bash
mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
```

**Verification**: After the `mv`, confirm the file exists at the new path and no longer exists at the old path:
```bash
ls "_Archive/TICKER - Company Name.md"
ls "Theses/TICKER - Company Name.md" 2>/dev/null
```

**If the move fails**: All metadata updates (sector note, graph, `_hot.md`) have already succeeded — the closure is logically complete. The thesis file remains in `Theses/` with `status: closed`. Report:
```
⚠️ Archive move failed — thesis remains in Theses/ with status: closed.
Metadata (sector note, graph, _hot.md) already updated.
To complete manually: mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
```
Do NOT attempt to undo the metadata updates. The intermediate state (`status: closed` in `Theses/`) is safe: `/sync` will skip a closed thesis in its propagation analysis, and `/lint` will flag the pending move. The next session can complete the move with the single `mv` command above.

## Step 7.6: Write Graph Invalidation List (closure only)

**Only runs for `status → closed` changes. Skip for conviction changes, non-closure status changes, and reaffirmations.** Skip silently if Step 7.5 reported the archive move failed — the closure is incomplete; invalidation must wait until the move completes.

Closure removes the thesis from `Theses/`, but neighbor theses (those that referenced the closed thesis via `[[wikilinks]]`) still have `cross-thesis:` entries in `_graph.md` pointing to the now-archived thesis. `/graph last`'s incremental path only re-extracts adjacency for thesis files whose mtime advanced since the last graph write — so untouched neighbors keep stale `cross-thesis:` references until their next edit. This accumulates dangling graph edges that `/lint` #21 flags.

Fix: write the neighbor list to `.graph_invalidations` at vault root. `/graph last` reads this file on its next run, folds the listed theses into the changed-file set for re-extraction, then deletes the file.

### 7.6a: Identify neighbor theses

Grep the `Theses/` directory (excluding the just-archived thesis) for wikilink patterns that reference the closed thesis:

```bash
# Patterns to search (each ticker/name occurrence matching any):
#   [[Theses/TICKER - Company Name]]
#   [[Theses/TICKER - Company Name|alias]]
#   [[Theses/TICKER - Company Name#section]]
#   [[Theses/TICKER - Company Name.md]]
#   [[TICKER - Company Name]]
#   [[TICKER - Company Name|alias]]
#   [[TICKER - Company Name#section]]
```

Use `Grep` with `output_mode: files_with_matches` and multiple pattern runs (one per form). Deduplicate the resulting file list. Exclude the just-archived thesis itself (if any match surfaced from _Archive/, ignore — only `Theses/*.md` neighbors matter for graph re-extraction).

### 7.6b: Append to `.graph_invalidations`

Create or append to `.graph_invalidations` at vault root (relative path `.graph_invalidations`). Format: one relative thesis path per line (e.g., `Theses/NVDA - Nvidia.md`). If the file already exists (prior closure produced unconsumed entries — `/graph last` hasn't run yet), append rather than overwrite, then deduplicate.

```bash
{
  # Existing entries (if any)
  [ -f .graph_invalidations ] && cat .graph_invalidations
  # New neighbors from 7.6a
  printf '%s\n' "Theses/NEIGHBOR1 - ...md" "Theses/NEIGHBOR2 - ...md"
} | sort -u > .graph_invalidations.tmp && mv .graph_invalidations.tmp .graph_invalidations
```

If no neighbors found (closed thesis was isolated): skip file creation. Report `Invalidation: no neighbors — isolated thesis.`

### 7.6c: Validate and report

After write, verify the file exists and contains the expected entries. Include in Step 8 report:
- **Graph invalidation**: `[N] neighbors added to .graph_invalidations: [list first 5, truncate with "...+M more" if longer]`
- **Graph reminder**: emphasize `/graph last` is now mandatory — without it, the invalidation list accumulates.

## Step 8: Report

- **Change applied**: [TICKER] [field] [old] → [new]
- **Rationale**: [from $ARGUMENTS]
- **Thesis snapshot**: `[[_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-HHMMSS)]]` or "skipped (draft→active)"
- **Sector note snapshot**: `[[_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-HHMMSS)]]` OR "skipped (no matching sector note)" OR "skipped (no edit needed — sector note state already reflects transition)"
- **Batch ID**: `status-YYYY-MM-DD-HHMMSS` (cascade-restore with /rollback if needed)
- **Sector Note updated**: [sector name] — [what changed] OR "no edit needed (dry-run determined current state already matches the transition)"
- **Graph reminder**: `→ Run /graph last` (closure only — conviction/non-closure changes have no graph impact). For closures the invalidation list from Step 7.6 is unconsumed until `/graph last` runs; a stale list accumulates across successive closures but does no harm beyond slightly wider re-extraction on the next `/graph last`.
- **Archived** (closure only): `[[_Archive/TICKER - Company Name]]` or `⚠️ Archive move failed — see Step 7.5 output`
- **Graph invalidation** (closure only): `[N] neighbor theses queued for re-extraction in .graph_invalidations: [first 5 relative paths, truncate with "...+M more" if longer]` OR `no neighbors — isolated thesis` OR `skipped — archive move failed at Step 7.5`
- **Wikilink breakages** (closure only): `⚠️ [N] notes contain wikilinks to this thesis. Run /lint to review.`
- **Trigger conflict** (if any): `⚠️ [quote conflicting trigger]`
