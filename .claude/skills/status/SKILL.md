---
name: status
description: Change conviction level or status on a single thesis. Use when user says "change conviction", "downgrade", "upgrade", "move to monitoring", "close [TICKER]", or "set [TICKER] to [level]".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * cp * mkdir * mv * find *)
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

   > **Chain-aware (lightweight)**: Reaffirm is NOT a full chain participant — it does not write to the graph, so it cannot defer a graph update and is not counted in `Graph deferred`. But if a chain is active with scope overlapping this ticker, reaffirm's audit trail should still reach the Active Research Thread so the thread reflects the session's actual flow.
   >
   > Read `## Session Chain` in `_hot.md`:
   > - **Active chain with overlapping scope (same ticker, ticker within chain's sector, or either is vault-wide)**: append `YYYY-MM-DD: /status — [TICKER] reaffirmed, drift window reset` to Active Research Thread only. Do NOT mark a new step in `Steps:` (reaffirm is not a graph-producing step). Do NOT change `Graph deferred:`. Do NOT apply the compress/Previous rotation — this is a short line, not a thread reset.
   > - **Active chain with non-overlapping scope**: leave the chain untouched. Skip thread update (reaffirm is unrelated to the active work). Proceed normally with Recent Conviction Changes update above.
   > - **No active chain, or stale chain (date ≠ today)**: skip thread update. Do NOT start a new chain for reaffirm (it is too lightweight to anchor one). If stale chain with `Graph deferred` > 0, leave the stale chain as-is — the next proper chain-participant skill will trigger conversion to Graph Debt per the CLAUDE.md protocol.

6. **Report**:
   - **Reaffirmed**: [TICKER] conviction [level] maintained
   - **Drift window reset**: next /sync will anchor drift detection after this entry
   - **Chain**: `thread-appended to active chain` | `no active chain (skipped)` | `non-overlapping scope (skipped)`
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

Generate `HHMM` once at the start of this step:
```bash
HHMM=$(date +%H%M)
mkdir -p _Archive/Snapshots
```
Use `status-YYYY-MM-DD-$HHMM` as the `snapshot_batch` value across **all** snapshots created in this run (thesis snapshot in Step 3.1, sector note snapshot in Step 5a). Reusing a single batch ID lets `/rollback` cascade detection restore both files atomically as a single operation.

> **Draft→active note**: The batch ID is still generated even when Step 3.1 is skipped — Step 5a needs it for the sector note snapshot.

### 3.1: Thesis snapshot

Create a pre-change snapshot (conviction and most status changes are Tier A edits on the thesis body):

```bash
cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-$HHMM).md"
```

Read the newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - Company Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMM
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
| `active→monitoring` | Does the sector note distinguish monitoring (e.g., separate "Monitoring" section, `(monitoring)` suffix on wikilink, conviction column, or annotation convention)? | Sector note distinguishes monitoring AND the thesis is NOT already annotated as such. |
| `active→closed` | Is the thesis wikilink in the Active Theses section? | Thesis wikilink present — Step 5b will remove it (and optionally add to Closed/Archived). |
| Conviction change | Does the sector note display conviction levels alongside thesis links (e.g., `[[TICKER]] (medium)`, a conviction column, or a grouped-by-conviction structure)? | Sector note displays conviction AND the displayed value differs from the new conviction. |

Distinguish "sector note distinguishes monitoring" and "sector note displays conviction" by grepping the sector note body:
- Monitoring distinction indicators: `## Monitoring`, `(monitoring)`, `monitoring:`, or any thesis wikilink suffixed with a monitoring marker.
- Conviction display indicators: `(high)`, `(medium)`, `(low)` adjacent to thesis wikilinks, OR a `| Conviction |` column header, OR section headings grouped by conviction level.

If `edit_planned: false` after evaluating: skip both Step 5a and Step 5b. Report in Step 8 as `Sector note: no edit needed — [TICKER] transition [old→new] already reflects current sector note state.` Proceed to Step 6.

### 5a: Pre-edit snapshot (conditional on Step 5.1 `edit_planned: true`)

Only runs if Step 5.1 set `edit_planned: true`. Before modifying the sector note, snapshot it:
```bash
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-$HHMM).md"
```
Read the newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMM
```
Reuse the batch ID generated in Step 3.0. The snapshot runs for every transition where Step 5.1 determined an edit is required — including `draft→active`, where the thesis snapshot is skipped but the sector note IS being modified. Without this snapshot, a corrupted Edit to the sector note would leave no recovery path.

> **Skip cases**:
> - Step 5.0 returned "no matching sector note" → Steps 5.1, 5a, 5b are all skipped.
> - Step 5.1 determined `edit_planned: false` → Steps 5a, 5b are skipped; no snapshot, no edit.

### 5b: Apply the sector note update (conditional on Step 5.1 `edit_planned: true`)

Only runs if Step 5.1 set `edit_planned: true`. Apply the specific edit identified in Step 5.1's decision matrix:

1. **For status → active** (e.g., draft→active, monitoring→active): Add the thesis to the Active Theses section. If it was present with a monitoring annotation, remove the annotation.
2. **For conviction changes** (when sector note displays conviction): Update the displayed conviction level for this thesis to the new value.
3. **For status → monitoring** (when sector note distinguishes monitoring): Move or annotate the thesis to reflect monitoring status per the sector note's convention.
4. **For status → closed**: Remove the thesis from the Active Theses section. If a "Closed/Archived" section exists, add it there. If not, just remove.

> **Why the dry-run matters**: Unconditional snapshotting creates orphan snapshot files for no-op transitions (e.g., `active→monitoring` on a sector note that doesn't track monitoring status). These accumulate disk usage, clutter `/rollback` snapshot lists, and dilute cascade-detection signal. The dry-run keeps snapshots aligned with actual edits without sacrificing safety.

## Step 6: Update _graph.md (skip if it does not exist)

> **Chain-aware**: Per CLAUDE.md Session Chain Protocol — if joining an active chain, SKIP graph update below and increment `Graph deferred`. If starting or no chain, proceed.

### For conviction and non-closure status changes:
- No graph changes needed (graph tracks links, not conviction/status metadata).

### For status → closed:

> **EXCEPTION — closure-immediate override**: Closure graph cleanup MUST run immediately, regardless of chain state. Mirrors `/rollback`'s recreated-file exception (one creates the entry, the other destroys it; both are structural). Rationale:
> - Subsequent skills reading `_graph.md` would otherwise reference a thesis whose file is in `_Archive/`. `/sync` would attempt reads via missing-file resilience (warning every time), reverse indexes would still list the closed ticker, and other theses' `cross-thesis:` fields would still reference it.
> - Chain-deferred Rule 9 cleanup (`/sync` Step 7) runs in default mode only and is skipped in ticker-scoped mode. A chain finalized via `/sync TICKER` (different ticker) leaves the closed thesis's adjacency entry persisting until an unscoped `/sync` runs. The exception prevents the inconsistency from accumulating in the first place.
>
> When the exception fires inside an active chain: do NOT increment `Graph deferred` (closure is its own structural operation, not a deferred update). Mark step ✅ in `Steps:` normally. Append a note to the Step 8 report: `ℹ️ Graph cleanup applied immediately (closure exception) — not counted toward Graph deferred.`

- Remove the archived thesis's entry from the Thesis Adjacency Index
- Remove it from all reverse indexes (Macro → Theses, Sector → Theses)
- Remove it from Cross-Thesis Clusters
- Scan ALL remaining thesis entries in the Adjacency Index and remove the archived ticker from their `cross-thesis:` fields
- Move any research notes that were ONLY linked from this thesis to the Orphan list
- Update `date:` and `edges:` in frontmatter

**Graph validation** (closure only): After all graph edits, re-read the modified section and verify: (1) no unclosed `[[` brackets introduced, (2) `theses:` frontmatter count still within ±2 of actual `Theses/` file count. If either check fails: `⚠️ Graph may be corrupted — [specific failure]. Run /graph to rebuild.`

## Step 7: Update _hot.md

Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

> **Chain-aware**: Per CLAUDE.md Session Chain Protocol — if joining an active chain: append `YYYY-MM-DD: /status — [TICKER] [field] [old] → [new]` to Active Research Thread only (skip compress/Previous), mark step ✅, then proceed to remaining sections. If starting or no chain, set Session Chain and apply full update below. **Stale-chain preservation** (before overwriting): if existing Session Chain has `Date:` ≠ today AND `Graph deferred: [N]` with N > 0, FIRST convert to Graph Debt per CLAUDE.md § Stale Chain — write `**⚠️ Graph debt**: [N] deferred from [stale-date] ([stale-skill-list]). Run /graph to capture.` below `*No active chain.*` (accumulate count and skill list with any pre-existing Graph Debt line rather than overwriting it). Only after preservation, overwrite the active-chain block with this skill as Step 1.

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: [TICKER] [field] changed [old] → [new], and the logical next step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry: `- **[TICKER]**: [field] [old] → [new] — [rationale]`
3. **Open Questions**: If closing a thesis, remove any open questions specific to that ticker
4. **Portfolio Snapshot**: Update conviction-level counts if conviction changed; update active/monitoring/closed counts if status changed

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Step 7.5: Archive Move (closure only)

**Only runs for `status → closed` changes. Skip for conviction changes, non-closure status changes, and reaffirmations.**

Move the closed thesis to `_Archive/`:
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

## Step 8: Report

- **Change applied**: [TICKER] [field] [old] → [new]
- **Rationale**: [from $ARGUMENTS]
- **Thesis snapshot**: `[[_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-HHMM)]]` or "skipped (draft→active)"
- **Sector note snapshot**: `[[_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-HHMM)]]` OR "skipped (no matching sector note)" OR "skipped (no edit needed — sector note state already reflects transition)"
- **Batch ID**: `status-YYYY-MM-DD-HHMM` (cascade-restore with /rollback if needed)
- **Sector Note updated**: [sector name] — [what changed] OR "no edit needed (dry-run determined current state already matches the transition)"
- **Graph updated**: [edges removed, orphans created] or "no graph changes needed"
- **Archived** (closure only): `[[_Archive/TICKER - Company Name]]` or `⚠️ Archive move failed — see Step 7.5 output`
- **Wikilink breakages** (closure only): `⚠️ [N] notes contain wikilinks to this thesis. Run /lint to review.`
- **Trigger conflict** (if any): `⚠️ [quote conflicting trigger]`
