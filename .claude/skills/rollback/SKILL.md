---
name: rollback
description: Restore a thesis, sector, or macro note from a snapshot in _Archive/Snapshots/. Use when user says "rollback", "restore", "revert", "undo sync", or "go back to the previous version".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * cp * mkdir * mv * find * ls * wc * diff *)
---

Restore a vault note from a previous snapshot. Undo mechanism for `/sync`, `/deepen`, `/status`, `/compare`, and any other skill that creates pre-edit snapshots.

Design rationale lives in `.claude/skills/rollback/RATIONALE.md`. SKILL.md references sections via `§N.M`.

## Arguments

`$ARGUMENTS` should be one of:
- **Ticker** (e.g., `NVDA`): find all snapshots for that ticker and present options
- **Snapshot filename** (e.g., `NVDA - Nvidia (pre-sync 2026-04-16)`): restore a specific snapshot
- **Empty**: list all available snapshots grouped by source note

If ambiguous or no match → report what's available and ask user to clarify.

## Step 0: Pre-flight

### 0.1: Acquire vault lock (mode-dependent)
- **List mode** (no args OR ticker without snapshot name): `read-only` scope. Timeout 2 min.
- **Restore mode** (specific snapshot filename → will cp + possibly cascade): `vault-wide` scope. Timeout 10 min.

Per `.claude/skills/_shared/preflight.md` Procedure 1. Capture token, verify ownership (Procedure 1.5) at every subsequent Bash block, release via `rm -f "$LOCK_FILE"` in final reporting block.

### 0.2: Rename-marker check
- **List mode**: skip.
- **Restore mode**: glob `.rename_incomplete.*`. If any exists, emit advisory (non-blocking — rollback may be the recovery path FROM a bad rename):
  `⚠️ In-flight rename repair(s) detected: [markers]. Rollback may restore a snapshot of a file that has since been renamed. Snapshot frontmatter's snapshot_of: points to the ORIGINAL path; restoration writes to that path. Review after rollback and re-run /rename if needed.`

## Step 1: Inventory Snapshots

```bash
find _Archive/Snapshots/ -name '*.md' -type f | sort
```

If none exist: "No snapshots available — nothing to rollback." Stop.

### Match by argument
- **Ticker**: filename prefix match, plus grep `snapshot_of:` frontmatter for sector/macro snapshots.
- **Filename**: direct.
- **No argument**: list all, ask user to choose.

Multiple matches → present in a table and wait for selection:

| # | Snapshot | Date | Trigger | Source Note |
|---|----------|------|---------|-------------|
| 1 | `NVDA - Nvidia (pre-sync 2026-04-16-2115).md` | 2026-04-16 | sync | [[Theses/NVDA - Nvidia]] |
| 2 | `NVDA - Nvidia (pre-deepen 2026-04-14-0930).md` | 2026-04-14 | deepen | [[Theses/NVDA - Nvidia]] |

**Wait for user selection before proceeding.**

## Step 2: Read and Compare

1. Read selected snapshot in full.
2. Extract `snapshot_of:` → identify original file path.
3. Read current version of original file in full.
4. If original file no longer exists, branch on `snapshot_trigger:`:

### 4a. Rename-undo branch

If `snapshot_trigger: rename` AND snapshot has `rename_target:` AND file at `rename_target:` exists: three options (§3.1 for design):

```
⚠️ Rename detected. This snapshot was created by /rename.
  Original path:    [[snapshot_of value]]
  Current location: [[rename_target value]]

Restoring to the original path would create a duplicate file.
Inbound wikilinks across the vault still point to the current name.

Options:
  (a) Symmetric reverse-rename — RECOMMENDED.
      Run `/rename [TICKER] "[old_name]"` after this rollback exits.
  (b) Content-only restore — write snapshot content to the OLD path.
      Creates a duplicate (both names exist). Wikilinks retain current target.
      Use ONLY for side-by-side comparison.
  (c) Cancel.
```

- **(a) Symmetric reverse-rename**: stop rollback. Output exact command:
  ```
  Run this command:
    /rename [TICKER] "[old_name from snapshot]"

  /rename will atomically reverse and produce its own pre-rename snapshot.
  Do NOT re-run /rollback for the rename — use /rename inverse.
  ```
  Skip Steps 3-7. Report exit reason in Step 7.
- **(b) Content-only restore**: proceed to Step 3 with explicit duplicate-file warning. Step 5 writes snapshot content to OLD path; file at `rename_target:` untouched.
- **(c) Cancel**: stop entirely. Report in Step 7.

### 4b. Other-trigger branch (default)

If `snapshot_trigger:` is anything other than `rename`: proceed with recreate flow. Warn: `⚠️ Original file [path] no longer exists. Rollback will recreate it. Confirm?` Wait for confirmation.

### Diff summary

- **Original file does not exist** (4b recreate flow): skip diff. Report: "No current version to compare — file was archived/deleted. Snapshot contents will be restored in full. The archived copy in `_Archive/` (if found) will be moved to Snapshots during Step 6 cleanup."
- **4a content-only restore chosen**: skip diff. Report: "No diff possible — original path is empty (file was renamed to [[rename_target]]). Snapshot content will be written to the original path, creating a duplicate. Wikilinks across the vault retain their current targets. Acknowledge the side-by-side outcome in confirmation."
- **Original file exists**: compare snapshot vs current. Report:
  - **Sections changed**: each `##` section that differs + one-line description
  - **Frontmatter changes**: fields that differ (conviction, status, etc.)
  - **Log entries added since snapshot**: will be LOST — highlight these (Tier 2 append-only audit trail loss is primary rollback cost)
  - **Net change**: word count delta

## Step 2.5: Cascade Detection

### 2.5a: Batch matching

1. Extract `snapshot_batch:` from selected snapshot. If absent (legacy), fall back to `snapshot_trigger:` + `YYYY-MM-DD` portion of `snapshot_date:`. Both `-HHMM` (legacy) and `-HHMMSS` (current) recognized.
2. Search `_Archive/Snapshots/` for other snapshots with matching `snapshot_batch:` (or trigger+date in fallback).
3. If matches found:

```
Found [N] other snapshot(s) from the same batch [batch ID]:
  - [[_Archive/Snapshots/other-snapshot-1]] → [[source-file-1]]
  - [[_Archive/Snapshots/other-snapshot-2]] → [[source-file-2]]

These files were modified together. Restoring only [[selected file]] may
leave the vault inconsistent (e.g., thesis reverted but sector note retains
post-sync content).

Options:
  (a) Cascade — restore ALL [N+1] files from this [trigger]
  (b) Single — restore only [[selected file]]
  (c) Cancel
```

4. **Wait for user selection.**
   - **(a) Cascade**: add all matched snapshots to restore set. For each, read snapshot + current + perform diff. Combined confirmation in Step 3 covers all files. Execute Step 4 + Step 5 in **batched phases**: ALL safety snapshots first, then ALL restorations (§7.1). Step 6 runs once at end.
   - **(b) Single**: emit warning then wait for re-confirmation:
     ```
     ⚠️ Proceeding with single-file rollback. [N] other file(s) retain content
     from the reverted [trigger]. Run /sync TICKER to re-propagate, but pre-sync
     content in sector/macro/cross-thesis notes cannot be automatically reverted.
     Consider cascade (option a) instead.
     ```
   - **(c) Cancel**: stop.

If no matches, proceed silently to Step 3.

### 2.5b: Sync manifest sidecar lookup (sync-trigger snapshots only)

If `snapshot_trigger: sync` (or any cascade match is sync-triggered), check for companion manifest:
```
_Archive/Snapshots/_sync-manifest (sync-YYYY-MM-DD-HHMMSS).md
```

If manifest exists, parse:
- `## Theses with snapshots taken (Tier A)` — confirms Step 2.5a cascade set
- `## Theses with Log-only appends (Tier B — NO snapshot, NOT recoverable)` — **invisible-to-cascade** entries; surface during prompt
- `## Sector notes touched` / `## Macro notes touched` (Tier B link-only) — also invisible to cascade

Extend cascade prompt:

```
⚠️ Tier B appends from this batch (cannot be auto-restored — manual review needed):

[N] thesis Log entries written without snapshots (cross-thesis propagation,
augmented targets, etc.):

  - Theses/TICKER1 - Name.md:
    ### YYYY-MM-DD
    - [[Research/source]]: [what changed] — conviction [impact]
    Reason: cross-thesis propagation from [[Research/...]]

  - Theses/TICKER2 - Name.md:
    [Log entry text]
    Reason: ...

[M] sector/macro notes received link-only additions (harmless to leave in place):
  - Sectors/Foo.md (link added to Related Research)
  - Macro/Bar.md (link added to body)

Options:
  (a) Cascade — restore ALL Tier A files. Tier B entries SURFACED in Step 7 for manual review.
  (b) Cascade + strikethrough — restore Tier A AND auto-strikethrough every Tier B Log entry:
      "~~[entry]~~ → Reverted YYYY-MM-DD: rolled back via /rollback batch [batch ID]"
  (c) Single — restore only [[selected file]] (NOT recommended).
  (d) Cancel.
```

**Wait for selection.** If (b), perform strikethrough Edits after Step 5 cascade completes (one Edit per Tier B entry). If (a), include Tier B list in Step 7 report.

**Manifest missing** (sync pre-T2.1, or manifest write failed): fall back to 2.5a with warning: `⚠️ No sync manifest found for batch [batch ID]. Cascade will only restore Tier A snapshots; any Tier B Log appends from this sync are invisible and will persist after rollback. To find them manually, grep Theses/*.md for entries dated [snapshot date] referencing [source research notes from the snapshot's referenced sources].`

### 2.5c: Non-sync trigger snapshots (no-manifest case)

Triggers without manifests (`deepen`, `catalyst`, `rename`, `rollback` pre-rollback safety net) snapshot every modified file (Tier A only). Proceed with 2.5a behavior unchanged.

### 2.5d: Stress-test manifest cascade (T3.1)

If snapshot associated with `/stress-test` batch (user-supplied `stress-test-YYYY-MM-DD-HHMMSS` OR companion `_stress-test-manifest (...)` matches): read manifest, surface Log entry for strikethrough review. `/stress-test` writes NO thesis snapshot — only a Log append (§2.2).

```
Stress-test batch cascade detected:
  Batch:       stress-test-YYYY-MM-DD-HHMMSS
  Ticker:      TICKER
  Research note: [[Research/YYYY-MM-DD - TICKER - Stress Test]]  (NOT deleted by rollback)

Log entry appended to Theses/TICKER - Name.md (Tier 2 append-only — no snapshot):
  [full entry text from manifest]

Options:
  (a) Surface only — leave Log entry as historical audit; manually annotate later.
  (b) Cascade + strikethrough — rewrite as:
      `~~[original entry]~~ → Reverted YYYY-MM-DD: stress-test run judged
      invalid (rolled back via /rollback batch stress-test-YYYY-MM-DD-HHMMSS).`
  (c) Cancel.
```

If (b), perform strikethrough Edit. Edit failure → report and continue (degrades to (a)).

Research note at `Research/` preserved as historical record (same policy as scenario and compare research notes).

### 2.5e: Status manifest cascade (T2.2)

If snapshot associated with `/status` batch: read manifest for full transaction context. `/status` = single-ticker multi-file transaction (thesis frontmatter + sector + optional archive mv + optional `.graph_invalidations` + `_hot.md`).

```
Status transaction cascade detected:
  Batch:          status-YYYY-MM-DD-HHMMSS
  Ticker:         TICKER
  Transition:    [conviction|status] [old] → [new]
  Manifest:      [[_Archive/Snapshots/_status-manifest (status-...)]]

Stages that landed:
  ✅ Thesis frontmatter edited — snapshot: [[_Archive/Snapshots/...]]
  ✅ Sector note edited — snapshot: [[_Archive/Snapshots/...]]
  ✅ Archive move (closure only)
  ✅ Graph invalidations written
  ✅ _hot.md updated

Cascade options:
  (a) Restore thesis frontmatter only (from thesis snapshot).
  (b) Restore full transaction (thesis + sector + un-archive + clear invalidations).
  (c) Cancel.
```

Option (b) execution: restore thesis → restore sector → if closure: `mv _Archive/TICKER - Name.md Theses/TICKER - Name.md` → clear matching entries from `.graph_invalidations` → revert `_hot.md` Recent Conviction Changes. On any sub-step failure → abort remaining, report. Pre-rollback safety snapshot (Step 4) covers worst case.

### 2.5f: Thesis manifest cascade (H1)

If snapshot or user-supplied batch matches `/thesis` batch (`thesis-TICKER-YYYY-MM-DD-HHMMSS` OR companion `_thesis-manifest (thesis-...)`): read manifest. **Cascade is deletion-based, not snapshot-based** — `/thesis` creates new files; undo = delete (§2.2).

```
Thesis creation cascade detected:
  Batch:           thesis-TICKER-YYYY-MM-DD-HHMMSS
  Ticker:          TICKER
  Proposed name:   [proposed_name from manifest]
  Proposed path:   Theses/TICKER - [proposed_name].md
  Manifest:        [[_Archive/Snapshots/_thesis-manifest (...)]]

Landed operations:
  ✅ Thesis file created (or ⚠️ not created)
  ✅ Sector note updated — [sector] (or ℹ️ skipped/new_sector_created)
  ✅ _hot.md updated
  ✅ [N] orphan research notes touched

Cascade options:
  (a) Delete thesis file only — leaves sector note and _hot.md modifications.
  (b) Full cascade — (a) + remove thesis wikilink from sector note Active Theses
      + revert _hot.md entries (targeted Edits) + revert orphan research mtimes
      (if captured in manifest; otherwise skip).
  (c) Cancel — manual cleanup.

Confirm (a/b/c):
```

**Option (b) execution**:
1. `rm "Theses/TICKER - [proposed_name].md"` (if exists)
2. Remove `- [[Theses/TICKER - [proposed_name]]]` line from sector note Active Theses (exact-match Edit)
3. Revert `_hot.md`:
   - Active Research Thread: strike/remove thesis-creation entry
   - Recent Conviction Changes: remove `- **[TICKER]**: ... initial [level]` line
   - Open Questions: remove entries added by this `/thesis` run (manifest lists verbatim)
4. If `new_sector_note_created` in manifest (user chose option (a) of `/thesis` §5 new-sector): offer to delete newly-created sector note file — ONLY if manifest confirms sector was new.

**Edit failures during cascade**: continue remaining steps; report per-step outcome. Users complete partial cascade manually via manifest body.

**Preservation**: thesis file content NOT preserved in `_Archive/Snapshots/` unless user chose (a) and archived manually. Before accepting (b), consider saving thesis content elsewhere.

## Step 3: Confirm (Mandatory)

Present the rollback plan and **wait for explicit user confirmation**:

**If original file exists:**
```
Proposed rollback:
  Restore: [[path/to/original]]
  From snapshot: [[_Archive/Snapshots/snapshot-name]]
  Snapshot date: YYYY-MM-DD
  Trigger: [sync/deepen/status/compare]

  Sections that will revert: [list]
  Frontmatter changes reverted: [list, e.g., conviction: medium → high]
  Log entries that will be LOST: [count] entries from [dates]

  A pre-rollback snapshot will be created as safety net.

Confirm? (y/n)
```

**If original file does not exist:**
```
Proposed rollback:
  Recreate: [[path/to/original]] (file currently absent)
  From snapshot: [[_Archive/Snapshots/snapshot-name]]
  Snapshot date: YYYY-MM-DD
  Trigger: [sync/deepen/status/compare]

  Full restoration from snapshot. Archived copy (if found) will be moved to Snapshots.
  Safety snapshot: skipped (no current file to snapshot).

Confirm? (y/n)
```

**Do NOT proceed without explicit user confirmation.**

## Step 4: Create Pre-Rollback Safety Snapshot

**If original file exists**:
```bash
mkdir -p _Archive/Snapshots
cp "[original file path]" "_Archive/Snapshots/[Name] (pre-rollback YYYY-MM-DD-HHMMSS).md"
```

Read the new safety snapshot, add frontmatter:
```yaml
snapshot_of: "[[original file path]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: rollback
snapshot_batch: rollback-YYYY-MM-DD-HHMMSS
```

Generate `HHMMSS` once via `date +%H%M%S`. Reuse this `snapshot_batch:` for Step 6 cleanup snapshots (§1.1).

**If original file does not exist** (archived/closed): skip safety snapshot. Log: `Safety snapshot skipped — original file does not exist at [path].`

**Cascade batch mode**: complete Step 4 for ALL files in restore set BEFORE Step 5 begins (§7.1). If any safety snapshot fails, abort — do NOT proceed to Step 5. Same `snapshot_batch:` across all safety snapshots in batch.

## Step 5: Restore

1. Read snapshot content.
2. Remove snapshot-specific frontmatter (`snapshot_of`, `snapshot_date`, `snapshot_trigger`, `snapshot_batch`) — they belong to snapshot, not live note.
3. Write cleaned content to original file path, fully replacing current.
4. Append Log entry to restored note:
   ```
   ### YYYY-MM-DD
   - ROLLBACK to snapshot (YYYY-MM-DD, pre-[trigger]). [N] log entries from [date range] lost. Safety snapshot: [[_Archive/Snapshots/Name (pre-rollback YYYY-MM-DD-HHMMSS)]]
   ```

### Cascade failure handling

Mid-batch failure → all files have safety snapshots (from Step 4). Report:
```
⚠️ Cascade rollback partially completed.
Restored: [list]
Failed: [file + error]
Not attempted: [remaining]
All pre-rollback safety snapshots exist (batch: rollback-YYYY-MM-DD-HHMMSS).
To undo restored files: /rollback [any restored ticker] → select (pre-rollback) → cascade (a).
To retry failed files: /rollback [failed ticker] → select original (pre-[trigger]) snapshot.
```

**Do NOT proceed to Step 6** for partial cascade — cleanup requires consistent state.

## Step 6: Post-Rollback Cleanup

### 6.1: Conviction/status revert — sector note update

Runs only if rollback changed `conviction:` or `status:` frontmatter (snapshot vs current pre-rollback differ). Mirrors `/status` Step 5 end-to-end (§5.1).

If `status:` reverted to `active` from closure (file recreated): surface once: `ℹ️ Restored status is already active — do NOT run /status closed→active (it will fail validation). Proceed directly to /sync TICKER → /graph.`

#### 6.1a: Resolve sector note (via contract)

Use `.claude/skills/_shared/sector-resolution.md`. Inputs: restored thesis's `sector:`. Outputs: `sector_note_path`, `match_confidence`, `log_message`.
- `none` → emit warning, skip 6.1b-6.1f, proceed to 6.2.
- `normalized` → emit log, silent to 6.1b.
- `substring` → emit log AND **stop for explicit user confirmation**. Declined → skip to 6.2.
- `exact` → silent to 6.1b.

#### 6.1b: Dry-run — determine if edit needed

Decision matrix per revert direction (§5.2):

| Revert direction | Check against sector note | `edit_planned: true` when... |
|---|---|---|
| `status: closed → active` (recreated) | (1) in Active Theses? (2) in Closed/Archived? | ABSENT from Active Theses OR PRESENT in Closed/Archived |
| `status: active → closed` (reopen revert) | in Active Theses? | PRESENT (remove) |
| `status: monitoring → active` | absent from Active OR annotated as monitoring? | Either |
| `status: active → monitoring` | sector distinguishes monitoring AND thesis not annotated? | Both |
| `conviction:` reverted | sector displays conviction AND displayed differs from reverted? | Both |

Detection indicators (mirror `/status` Step 5.1):
- Monitoring: `## Monitoring`, `(monitoring)`, `monitoring:`, suffix
- Conviction: `(high|medium|low)` adjacent, `| Conviction |` column, grouped sections

`edit_planned: false` → log `ℹ️ Sector note update skipped — [sector_note_path] already reflects reverted state.` Proceed to 6.2.
`edit_planned: true` → 6.1c.

#### 6.1c: Pre-edit snapshot

```bash
cp "[sector_note_path]" "_Archive/Snapshots/[Sector Name] (pre-rollback YYYY-MM-DD-HHMMSS).md"
```

Add frontmatter (reuse Step 4 HHMMSS — §1.2):
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: rollback
snapshot_batch: rollback-YYYY-MM-DD-HHMMSS
```

Cascade batch: distinct HHMMSS per sector only if sectors differ. Shared sector → one snapshot (§1.3).

#### 6.1d: Apply edit

Mirror `/status` Step 5b. Targeted `Edit` (atomic), NOT full `Write`.

1. **Reverted to `active`** (from closed/monitoring/draft): add to Active Theses (if absent). Remove monitoring annotation. If "Closed/Archived" section exists and contains this thesis, remove from there (prevents dual listing).
2. **Reverted to `monitoring`** (from active): apply monitoring annotation per sector convention (move to "Monitoring" section, add `(monitoring)` suffix, etc.).
3. **Reverted to `closed`** (reopen revert): remove from Active Theses. Add to "Closed/Archived" if exists.
4. **Conviction reverted**: update displayed level (e.g., `(medium)` → `(high)`, or move between conviction-grouped sections).

#### 6.1e: Post-edit verification

Re-read. For each edited section:
1. Ends with complete sentence (no mid-word, no unmatched `**` or `*`)
2. No incomplete table rows (line starts `|` but doesn't end `|`)
3. Thesis wikilink present/absent per 6.1d intention (re-grep to confirm)
4. Dual-listing absent: wikilink appears in AT MOST ONE of {Active Theses, Closed/Archived, Monitoring}

Any fail: `⚠️ Sector note may contain a partial edit in [section]. Snapshot available: [[_Archive/Snapshots/[Sector Name] (pre-rollback YYYY-MM-DD-HHMMSS)]]. Review manually or run /rollback on the sector snapshot.`

#### 6.1f: Report

- **Sector resolved**: `[sector_note_path]` (confidence `[exact|normalized|substring|none]`)
- **Sector edit**: `applied` | `skipped (edit_planned: false)` | `skipped (match_confidence: none)` | `skipped (declined substring confirmation)`
- **Sector snapshot**: `[[_Archive/Snapshots/...]]` (if 6.1c ran) | `n/a`
- **Post-edit verification**: `passed` | `⚠️ failed: [check]`

### 6.2: Archived file cleanup

If original file recreated (detected Step 2), check for archived copy:
```bash
find _Archive/ -maxdepth 1 -name "TICKER - *.md" -type f
```
(Glob includes ` - ` and `.md` to avoid false positives on short tickers like `A`, `T`, `U`.)

If found, move to Snapshots:
```bash
mv "_Archive/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (archived pre-rollback YYYY-MM-DD-HHMMSS).md"
```

Add `snapshot_of`, `snapshot_date`, `snapshot_trigger: rollback-cleanup`, `snapshot_batch: rollback-YYYY-MM-DD-HHMMSS` (reuse Step 4 batch ID).

### 6.2.5: Intervening-neighbor Log scan (recreated-file rollbacks only)

**Only runs on recreated-file rollbacks** (original did NOT exist before rollback). Skip for standard rollbacks. Rationale: §4.

Procedure:

1. **Identify closure date**. From restored thesis's Log, find final `CLOSED:` or `Cross-thesis closure:` pre-closure entry. Alternate: pre-rollback snapshot body. Capture `closure_date: YYYY-MM-DD` (date Log entry written, NOT date file mv'd).

2. **Identify citing files** — H3 extension: grep Theses/ + Macro/ + Sectors/ (excluding restored thesis) for wikilink patterns referencing restored thesis:
   - `[[Theses/TICKER - Name]]`, `[[Theses/TICKER - Name|...]]`, `[[Theses/TICKER - Name#...]]`, `[[Theses/TICKER - Name.md]]`
   - `[[_Archive/TICKER - Name]]` (from `Cross-thesis closure:` entries and post-closure narrative)
   - `[[TICKER - Name]]` folder-less form
   
   Tag each match with category (`thesis` | `macro` | `sector`).

3. **Scan for post-closure references** per category:
   - **Theses**: `## Log` section, entries where date `>= closure_date` AND body contains wikilink to restored thesis.
   - **Macros**: ENTIRE BODY (macros often lack Log). Capture file-path + line number. Date attribution: `file_mtime >= closure_date` → post-closure candidate; otherwise advisory flag.
   - **Sectors**: `## Log` per thesis pattern + narrative sections (`## Acquisitions and new entrants`, `## Competitive dynamics`, `## Industry history`) with mtime attribution. Skip `## Active Theses` (handled by `/status`/`/prune` at closure time).

4. **Classify each match**:
   - **Thesis Log — Premise-dependent**: prefix `Cross-thesis closure:` / `Cross-thesis closures:` (registry §13 — explicitly premised on closure)
   - **Thesis Log — Scenario/stress-test**: prefix `Stress test`/`Scenario`/`Scenario REVERSED` + body cites restored thesis
   - **Thesis Log — Sync-propagated**: prefix is research-note wikilink that cites closed thesis in rationale
   - **Macro/Sector body citation**: LLM-judgment premise-dependent vs contextual (§4.4)
   - **Sector Log — post-closure**: same as thesis Log pattern
   - **Other**

5. **Present findings**:

```
⚠️ Intervening Log entries detected — closure of [[restored thesis]] dated [closure_date]
   may have been cited as premise by other skills.

[N] entries found across [M] files:

[[Theses/AMAT - Applied Materials.md]]:
  - 2026-04-20: Cross-thesis closure: [[_Archive/NVDA - Nvidia]] archived — AI capex
    exposure reduced. [PREMISE-DEPENDENT]
  - 2026-04-25: [[Research/...]]: ASML guidance... given NVDA exit, AMAT positioning...
    [PARTIAL PREMISE]

[[Macro/...]]:
  - Line 42: "Iranian retaliation risk most directly affects [[_Archive/LITE - Lumentum]]..."
    [premise-dependent — macro body prose]

Options:
  (a) Surface only — leave as historical audit trail.
  (b) Auto-strikethrough premise-dependent entries (`Cross-thesis closure:` prefix only):
      `~~Cross-thesis closure: ...~~ → Superseded YYYY-MM-DD: [restored thesis] reopened via /rollback.`
  (c) Auto-strikethrough ALL matched entries (premise-dependent + partial):
      `~~entry~~ → Review YYYY-MM-DD: [restored thesis] was reopened — premise may no longer apply.`
  (d) Skip — acknowledge gap manually.

Confirm (a/b/c/d):
```

6. **Branch behavior**:
   - **(a)**: add summary to Step 7 report. No edits. User reviews manually.
   - **(b)**: iterate `Cross-thesis closure:` entries, strikethrough each. Include in Step 7.
   - **(c)**: iterate ALL matched entries, apply generic strikethrough template. Report in Step 7.
   - **(d)**: `ℹ️ Intervening-neighbor scan skipped per user. [N] entries flagged but not annotated.` Include full list in Step 7.

7. **Edit failures**: record + continue. Report failed Edits in Step 7 alongside successful.

**Overlap with Step 2.5c prune-manifest cascade**: `Cross-thesis closure:` prefix filter may duplicate 2.5b cascade surfacing (§4.5). Detect overlap → log `ℹ️ 6.2.5 scan overlaps with Step 2.5b prune-manifest cascade; showing combined list.`

### 6.3: Graph update deferred

`_graph.md` owned exclusively by `/graph` (§6). **After this rollback, run `/graph last` immediately** — re-extracts adjacency from restored thesis file, updates reverse indexes, removes restored research notes from orphan list.

Recreated-file rollback: `/graph last` rebuilds the absent adjacency entry; single-pass captures new adjacency + reverse-index re-entry + Cross-Thesis Cluster restoration.

### 6.4: Update _hot.md

Read `_hot.md` then edit (do NOT touch Latest Sync / Sync Archive — owned by `/sync`). Follow `_shared/hot-md-contract.md`:

1. **Active Research Thread**: same-ticker continuation (append dated line). New topic: compress outgoing to `*Previous:*` line. Write: `rolled back [TICKER/note] to [snapshot date] snapshot, and what was reverted`. Max 5 `*Previous:*` lines; drop oldest.
2. **Recent Conviction Changes**: if conviction/status reverted, add: `- **[TICKER]**: rollback [field] [current] → [reverted] — restored to [snapshot date] state`
3. **Open Questions**: if rollback restored previously-resolved Outstanding Questions, re-add them.

**Word cap**: after all edits, if over 4,000 words (soft cap per `_shared/hot-md-contract.md`), prune `## Sync Archive` (oldest first) then `*Previous:*` lines. Abort if over 5,000 hard cap.

## Step 7: Report

### Normal rollbacks (Steps 4-6 executed)

- **Restored**: [[original file path]] from snapshot dated YYYY-MM-DD
- **Safety snapshot**: [[_Archive/Snapshots/Name (pre-rollback YYYY-MM-DD-HHMMSS)]]
- **Sections reverted**: [list]
- **Log entries lost**: [count] — preserved in safety snapshot
- **Side effects**: [sector updated / graph updated / conviction reverted]
- **Graph reminder**: `→ Run /graph last to update the dependency map.` (Critical for recreated-file rollbacks — restored thesis is invisible to graph-assisted propagation until /graph last runs.)
- **Duplicate-file note** (Step 4a option (b) only): `⚠️ Content-only restore created duplicate file. Original path: [[snapshot_of]]. Current name: [[rename_target]]. Wikilinks retain current targets. To consolidate: decide which to keep, delete the other, run /sync.`
- **To undo this rollback**: `/rollback [ticker]` → select `(pre-rollback)` snapshot

### Rename-undo redirect (Step 4a option (a))

- **Rollback exited — no changes made.**
- **Reason**: snapshot was created by `/rename`. Symmetric reverse via `/rename` is the correct undo path.
- **Run this command**: `/rename [TICKER] "[old_name from snapshot]"`
- **Rationale**: `/rename` atomically restores filename, inbound wikilinks (7 patterns), `_graph.md` adjacency header, sector note Active Theses, `_Archive/Snapshots/` `snapshot_of:`. After `/rename` succeeds, this snapshot remains as historical record.

### Cancellation (Step 4a option (c))

- **Rollback canceled — no changes made.**
