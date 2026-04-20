---
name: rollback
description: Restore a thesis, sector, or macro note from a snapshot in _Archive/Snapshots/. Use when user says "rollback", "restore", "revert", "undo sync", or "go back to the previous version".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * cp * mkdir * mv * find * ls * wc * diff *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Restore a vault note from a previous snapshot. This is the undo mechanism for `/sync`, `/deepen`, `/status`, `/compare`, and any other skill that creates pre-edit snapshots.

## Arguments

$ARGUMENTS should be one of:
- **Ticker** (e.g., `NVDA`): find all snapshots for that ticker and present options
- **Snapshot filename** (e.g., `NVDA - Nvidia (pre-sync 2026-04-16)`): restore a specific snapshot
- **No arguments / empty**: list all available snapshots grouped by source note

If $ARGUMENTS is ambiguous or matches no snapshots, report what's available and ask the user to clarify.

## Step 0: Pre-flight

### 0.1: Acquire vault lock (mode-dependent)
- **List mode** (no args OR arg is ticker without snapshot name → listing snapshots): acquire `read-only` scope lock. Timeout: 2 minutes.
- **Restore mode** (specific snapshot filename → will cp + possibly cascade): acquire `vault-wide` scope lock. Timeout: 10 minutes (cascade may touch many files).

Per `.claude/skills/_shared/preflight.md` Procedure 1. Capture the token emitted by the acquisition Bash block and verify ownership (Procedure 1.5) at the start of each subsequent Bash block. Release in the final reporting Bash block via `rm -f "$LOCK_FILE"`.

### 0.2: Rename-marker check
- **List mode**: skip (read-only).
- **Restore mode**: glob `.rename_incomplete.*`. If ANY marker exists, emit advisory: `⚠️ In-flight rename repair(s) detected: [markers]. Rollback may restore a snapshot of a file that has since been renamed. Snapshot frontmatter's snapshot_of: points to the ORIGINAL path; restoration writes to that path. Review after rollback and re-run /rename if needed.` Do NOT block — rollback may be the user's recovery path FROM a bad rename, so blocking would be counterproductive.

## Step 1: Inventory Snapshots

List all snapshots in `_Archive/Snapshots/`:
```bash
find _Archive/Snapshots/ -name '*.md' -type f | sort
```

If no snapshots exist, report "No snapshots available — nothing to rollback." and stop.

### Match by argument
- **Ticker**: Match snapshots whose filename starts with the ticker (e.g., `NVDA` matches `NVDA - Nvidia (pre-sync 2026-04-16).md`). Also match sector/macro snapshots by grepping `snapshot_of:` frontmatter.
- **Filename**: Direct match.
- **No argument**: List all and ask which to restore.

If multiple snapshots match, present them in a table and ask the user to choose:

| # | Snapshot | Date | Trigger | Source Note |
|---|----------|------|---------|-------------|
| 1 | `NVDA - Nvidia (pre-sync 2026-04-16-2115).md` | 2026-04-16 | sync | [[Theses/NVDA - Nvidia]] |
| 2 | `NVDA - Nvidia (pre-deepen 2026-04-14-0930).md` | 2026-04-14 | deepen | [[Theses/NVDA - Nvidia]] |

**Wait for user selection before proceeding.**

## Step 2: Read and Compare

1. Read the selected snapshot in full.
2. Extract `snapshot_of:` from frontmatter to identify the original file path.
3. Read the current version of the original file in full.
4. If the original file no longer exists (e.g., archived, deleted, or renamed), branch on the snapshot's `snapshot_trigger:` to determine the correct flow:

   ### 4a. Rename-undo branch
   **If `snapshot_trigger: rename`** AND the snapshot has a `rename_target:` field, AND the file at `rename_target:` exists on disk:
   This snapshot was created by `/rename`. The file lives at the new path; "recreating" at the old path would produce a duplicate (both `[old_name]` and `[new_name]` would exist, with all inbound wikilinks pointing to `[new_name]`). Present three options:

   ```
   ⚠️ Rename detected. This snapshot was created by /rename.
     Original path:    [[snapshot_of value]]
     Current location: [[rename_target value]]

   Restoring to the original path would create a duplicate file
   (both names will exist; inbound wikilinks across the vault still point to the current name).

   Options:
     (a) Symmetric reverse-rename — RECOMMENDED.
         Run `/rename [TICKER] "[old_name]"` after this rollback exits.
         /rename atomically restores filename, inbound wikilinks, graph header,
         sector note entry, and snapshot_of fields. /rollback cannot do this
         inline (it is not a renaming skill).
     (b) Content-only restore — write snapshot content to the OLD path.
         Creates a duplicate file at [[snapshot_of]]; current file at [[rename_target]] is untouched.
         Inbound wikilinks across vault still point to the current name.
         Use ONLY if you want both versions side-by-side for comparison.
     (c) Cancel.
   ```

   - **(a) Symmetric reverse-rename**: Stop the rollback. Output the exact command to run:
     ```
     Run this command:
       /rename [TICKER] "[old_name from snapshot]"

     /rename will atomically reverse the original operation and produce its own
     pre-rename snapshot. After /rename succeeds, this snapshot becomes older
     history (clean up later via /clean if desired). Do NOT re-run /rollback
     for the rename — use /rename inverse.
     ```
     Skip Steps 3–7 entirely. Report exit reason in Step 7.
   - **(b) Content-only restore**: proceed to Step 3 confirmation with explicit warning text noting the duplicate-file outcome. Step 5 writes snapshot content to the OLD path; the file at `rename_target:` remains untouched. The user accepts the inconsistency knowingly.
   - **(c) Cancel**: stop entirely. Report cancellation in Step 7.

   ### 4b. Other-trigger branch (default)
   **If `snapshot_trigger:` is anything other than `rename`** (sync, status, deepen, compare, prune, catalyst, rollback, surface, stress-test, scenario, brief, thesis): proceed with existing recreate flow. Warn: `⚠️ Original file [path] no longer exists. Rollback will recreate it. Confirm?` Wait for confirmation.

### Diff summary
**If the original file does not exist** (archived/deleted via 4b — recreate flow): skip the diff. Instead report: "No current version to compare — file was archived/deleted. Snapshot contents will be restored in full. The archived copy in `_Archive/` (if found) will be moved to Snapshots during Step 6 cleanup."

**If 4a content-only restore was chosen**: skip the standard diff. Instead report: "No diff possible — original path is empty (file was renamed to [[rename_target]]). Snapshot content will be written to the original path, creating a duplicate. Wikilinks across the vault retain their current targets and will point to [[rename_target]] after restoration. Acknowledge the side-by-side outcome in confirmation."

**If the original file exists**, compare the snapshot against the current version. Report a concise summary:

- **Sections changed since snapshot**: list each `##` section that differs, with a one-line description of what changed
- **Frontmatter changes**: list any frontmatter fields that differ (conviction, status, etc.)
- **Log entries added since snapshot**: list log entries present in current but absent in snapshot (these will be lost)
- **Net change**: word count delta (e.g., "current is +340 words vs snapshot")

**Highlight any log entries that will be lost** — these are the append-only audit trail. Losing them is the primary cost of a rollback.

## Step 2.5: Cascade Detection

Check whether other snapshots were created by the same operation (indicating a multi-file mutation like `/sync` that should be rolled back atomically):

### Step 2.5a — Determine matching mode

Resolve the selected snapshot's identity using a frontmatter-then-filename cascade. This handles three real-world snapshot classes observed in mature vaults:

| Class | Has `snapshot_batch:`? | Has `snapshot_trigger:` + `snapshot_date:`? | Source of truth |
|---|---|---|---|
| **A — Modern** | yes | yes | frontmatter only |
| **B — Partial-legacy** | no | yes | frontmatter (trigger+date), filename (time suffix) |
| **C — Bare-legacy** | no | NO snapshot frontmatter at all | **filename only** |

Resolution procedure:

1. Read the selected snapshot's frontmatter. Extract `snapshot_batch:`, `snapshot_trigger:`, `snapshot_date:` if present.

2. If `snapshot_trigger:` OR `snapshot_date:` are missing, derive them from the filename. Filename pattern: `[Name] (pre-[trigger] YYYY-MM-DD[-HHMM[SS]]).md`. Regex (informal):
   ```
   ^(?<name>.*) \(pre-(?<trigger>[a-z-]+) (?<date>\d{4}-\d{2}-\d{2})(-(?<time>\d{4}|\d{6}))?\)\.md$
   ```
   - `name` → for display only
   - `trigger` → fills `snapshot_trigger:` if missing
   - `date` → fills `snapshot_date:` if missing
   - `time` → captured as the "time suffix" used by Step 2.5a-legacy clustering (none / `HHMM` / `HHMMSS`)

   If the filename does not match the expected pattern, abort with: `❌ Snapshot filename does not match expected pattern (pre-TRIGGER YYYY-MM-DD[-HHMM[SS]]). Cannot determine trigger/date for cascade detection. Manual restore via cp + git commit recommended.`

3. Route based on `snapshot_batch:` presence:

- **Class A — Modern** (`snapshot_batch:` present): use **batch-ID match**. Search `_Archive/Snapshots/` for other snapshots with EXACTLY matching `snapshot_batch:` value. Batch matching is operation-precise — same-day repeat operations (two `/sync` runs on the same day) get distinct batch IDs and will not cross-match. Proceed to **Step 2.5a-modern** (cascade presentation).

- **Class B / C — Legacy** (`snapshot_batch:` absent): use **trigger + date fallback**, with trigger and date sourced per Step 2 above (frontmatter or filename). Search `_Archive/Snapshots/` for other snapshots whose effective trigger + date (also sourced via the same frontmatter-then-filename cascade) match the selected snapshot. Recognized legacy filename formats: `(pre-[trigger] YYYY-MM-DD)` (no time suffix), `(pre-[trigger] YYYY-MM-DD-HHMM)` (4-digit time, pre-HHMMSS standardization), and `(pre-[trigger] YYYY-MM-DD-HHMMSS)` (6-digit, may also lack the batch field if the snapshot predates field introduction). Proceed to **Step 2.5a-legacy** (CRITICAL-2 disambiguation).

> **Why filename fallback exists**: your vault may contain `(pre-sync 2026-04-19-1354)` snapshots from an early `/sync` version that wrote no `snapshot_*` frontmatter at all (Class C). Without filename-derivation, Step 2.5a-legacy would receive empty trigger/date and produce zero candidates — silently allowing single-file rollback when there may have been a same-day batch. Filename-derivation gives Class C the same safety net as Class B.

### Step 2.5a-legacy — Legacy fallback disambiguation (CRITICAL-2 fix)

> **Why this exists**: trigger + date matching is intrinsically imprecise. Two completely independent `/sync` runs on the same day (e.g., morning sync at 09:00 and evening sync at 18:00) produce snapshots that share `snapshot_trigger: sync` and the same `snapshot_date: YYYY-MM-DD`, but were never part of the same batch. Without explicit disambiguation, `/rollback` would offer ALL same-day same-trigger snapshots as a "cascade" — accepting it would silently restore files unrelated to the batch you intended to undo. Modern snapshots (with `snapshot_batch:`) are immune; legacy snapshots are not. Your `_Archive/Snapshots/` may contain both formats — see CRITICAL-2 in the integrity report.

When operating in legacy mode, the cascade prompt MUST surface the ambiguity. Do NOT auto-include any candidate without explicit user confirmation.

1. Build the candidate list. For each candidate, capture:
   - Snapshot filename (full)
   - Source file path (from `snapshot_of:` if present, else inferred from filename)
   - Time portion of the snapshot filename (none / `HHMM` / `HHMMSS`)
   - File mtime of the snapshot file (independent ground-truth signal)

2. Cluster candidates by their time portion when possible. Two snapshots sharing the exact same time suffix (e.g., both `(pre-sync 2026-04-19-1354)`) are MORE likely to be the same batch than two with different suffixes. Use this as advisory, not definitive.

3. Present the legacy disambiguation prompt:

   ```
   ⚠️ Legacy cascade detection (no `snapshot_batch:` field).
   
   Selected snapshot: [[_Archive/Snapshots/[selected]]]
     Trigger: [trigger]
     Date:    YYYY-MM-DD
     Time:    [HHMM | HHMMSS | none]
     Mtime:   [filesystem mtime of the snapshot file]
   
   Found [N] other same-trigger snapshot(s) on the same date:
   
     [1] [[_Archive/Snapshots/candidate-1]] → [[source-file-1]]
         Time: [HHMM] | Mtime: [mtime]
         Likely same batch? [yes if time suffix matches; no if differs; unknown if either has no suffix]
     
     [2] [[_Archive/Snapshots/candidate-2]] → [[source-file-2]]
         Time: [none] | Mtime: [mtime]
         Likely same batch? unknown (no time suffix to compare)
     
     [3] [[_Archive/Snapshots/candidate-3]] → [[source-file-3]]
         Time: [HHMMSS] | Mtime: [mtime]
         Likely same batch? no (different time format suggests independent run)
   
   These could be the same batch as your selected snapshot OR independent
   operations from different times on the same day. Without `snapshot_batch:`
   the difference cannot be determined automatically.
   
   Options:
     (a) Include ALL candidates in cascade — accept the legacy ambiguity, restore everything that matches trigger+date
     (b) Include SOME — specify which by number (e.g., "1,3" includes candidates 1 and 3 only)
     (c) Include NONE — single-file rollback of just the selected snapshot
     (d) Cancel
   ```

4. **Wait for user selection.**
   - **(a) Include ALL**: add all candidates to the restore set. Surface in Step 7 report: `Cascade restored [N] files via legacy fallback (trigger+date match). User accepted ambiguity.`
   - **(b) Include SOME**: parse the comma-separated list of numbers. Validate each number maps to a candidate. Add only the selected candidates to the restore set. Surface in Step 7 report: `Cascade restored selected files [list] via legacy fallback. User excluded [excluded list] as not part of the batch.`
   - **(c) Include NONE**: emit the same single-file warning as Step 2.5b option (b), then proceed with single-file rollback.
   - **(d) Cancel**: Stop.

5. After cascade resolution, proceed to Step 2.5b (sync manifest sidecar lookup) — manifest lookup applies to both modern and legacy flows.

### Step 2.5a-modern — Modern (batch-ID match) cascade presentation

Used when `snapshot_batch:` was present on the selected snapshot. If matches were found in Step 2.5a (modern path), present them:

   ```
   Found [N] other snapshot(s) from the same batch [batch ID]:
     - [[_Archive/Snapshots/other-snapshot-1]] → [[source-file-1]]
     - [[_Archive/Snapshots/other-snapshot-2]] → [[source-file-2]]

   These files were modified together. Restoring only [[selected file]]
   without its counterparts may leave the vault in an inconsistent state
   (e.g., thesis reverted but sector note retains post-sync content).

   Options:
     (a) Cascade — restore ALL [N+1] files from this [trigger]
     (b) Single — restore only [[selected file]]
     (c) Cancel
   ```

**Wait for user selection.**
   - **(a) Cascade**: Add all matched snapshots to the restore set. For each additional file, read the snapshot and current file and perform the same diff summary as Step 2. Present a combined confirmation in Step 3 covering all files. Execute Steps 4 and 5 in **batched phases**: first, create ALL pre-rollback safety snapshots (Step 4) for every file in the restore set before restoring any of them. Then restore ALL files (Step 5). This ensures that if a restoration fails mid-batch, every file — including those not yet restored — has a safety snapshot from its pre-rollback state. Perform Step 6 once at the end for all restored files.
   - **(b) Single**: Emit the following warning before proceeding:
     ```
     ⚠️ Proceeding with single-file rollback. [N] other file(s) retain content
     from the reverted [trigger]. Run /sync TICKER to re-propagate, but pre-sync
     content in sector/macro/cross-thesis notes cannot be automatically reverted.
     Consider cascade (option a) instead.
     ```
     Then wait for the user to acknowledge or switch to cascade. If they confirm single-file, proceed with rollback as normal.
   - **(c) Cancel**: Stop.

If no matches are found (in either modern or legacy flow), proceed silently to Step 2.5b (sync manifest sidecar lookup, only relevant for sync-trigger snapshots) and then Step 3.

### Step 2.5b: Sync manifest sidecar lookup (sync-trigger snapshots only)

If the selected snapshot's `snapshot_trigger:` is `sync` (or any matched snapshot in the cascade is sync-triggered), additionally check for a corresponding sync manifest:
```
_Archive/Snapshots/_sync-manifest (sync-YYYY-MM-DD-HHMMSS).md
```
where `HHMMSS` is the same batch ID as the snapshot.

If the manifest exists, parse:
- `## Theses with snapshots taken (Tier A)` — these are already in the cascade restore set from Step 2.5a; manifest confirms.
- `## Theses with Log-only appends (Tier B — NO snapshot, NOT recoverable)` — these are the **invisible-to-cascade** entries. Surface them to the user during the cascade prompt.
- `## Sector notes touched` (Tier B link-only entries) and `## Macro notes touched` (Tier B link-only entries) — also invisible to cascade.

Extend the cascade prompt with a new section:
```
⚠️ Tier B appends from this batch (cannot be auto-restored — manual review needed):

[N] thesis Log entries written without snapshots (cross-thesis propagation, augmented targets, etc.):

  - Theses/TICKER1 - Name.md:
    ### YYYY-MM-DD
    - [[Research/source]]: [what changed] — conviction [impact]
    Reason: cross-thesis propagation from [[Research/...]] (TICKER1 wikilinked from another thesis touched in this run)

  - Theses/TICKER2 - Name.md:
    [Log entry text]
    Reason: ...

[M] sector/macro notes received link-only additions (no analytical text changed; harmless to leave in place):
  - Sectors/Foo.md (link added to Related Research)
  - Macro/Bar.md (link added to body)

After the cascade restore completes, you'll need to manually decide per Tier B Log entry:
  (1) Leave as historical audit trail (preferred — Tier 2 append-only convention).
  (2) Strikethrough with a reverted-on-rollback note.
  (3) Manually delete (violates Tier 2 — only if entry was clearly erroneous).

The link-only additions are Tier B but harmless — they just point to a research note whose content was reverted on cascade. Most users leave them in place.

Options:
  (a) Cascade — restore ALL Tier A files. Tier B entries listed above will be SURFACED in Step 7 report for manual review (you decide per entry).
  (b) Cascade + strikethrough — restore Tier A files AND auto-strikethrough every Tier B Log entry above with the format "~~[entry]~~ → Reverted YYYY-MM-DD: rolled back via /rollback batch [batch ID]". Preserves audit trail with explicit reversal signal.
  (c) Single — restore only [[selected file]] (NOT recommended — even more inconsistencies).
  (d) Cancel.
```

**Wait for user selection.** If (b) is chosen, perform the strikethrough Edits in batched phase after Step 5 cascade restore completes (one Edit per Tier B Log entry). If (a) is chosen, just include the Tier B list in the Step 7 report so the user can act post-rollback.

If the manifest does NOT exist (sync ran before manifest support was added, OR the manifest write itself failed in Step 7.5c), fall back to the original Step 2.5a behavior with an explicit warning: `⚠️ No sync manifest found for batch [batch ID]. Cascade will only restore Tier A snapshots; any Tier B Log appends from this sync are invisible and will persist after rollback. To find them manually, grep `Theses/*.md` for entries dated [snapshot date] referencing [source research notes from the snapshot's referenced sources].`

### Step 2.5c: Non-sync trigger snapshots (no-manifest case)

For triggers with no manifest (`deepen`, `catalyst`, `rename`, `rollback` pre-rollback safety net), no manifest exists — those skills snapshot every modified file (Tier A only) per their own atomicity rules. Proceed with the standard Step 2.5a dispatcher behavior unchanged: the dispatcher routes to Step 2.5a-modern (batch-ID match) if the snapshot has `snapshot_batch:`, or Step 2.5a-legacy (CRITICAL-2 disambiguation prompt) if it does not. Non-sync legacy snapshots (e.g., a `pre-deepen 2026-04-15` from before batch-ID introduction) also benefit from the legacy disambiguation — same-day repeat `/deepen` runs can otherwise be conflated.

### Step 2.5d: Stress-test manifest cascade (T3.1)

If the selected snapshot is associated with a `/stress-test` batch (user explicitly supplied a `stress-test-YYYY-MM-DD-HHMMSS` batch ID, OR a companion `_stress-test-manifest (stress-test-...)` file matches the snapshot's batch), read the manifest and surface the Log entry for strikethrough review.

`/stress-test` writes NO thesis snapshot (its only direct effect on theses is a Log append, which is Tier 2 append-only and cannot be restored via file-copy). The manifest records the Log entry text so the rollback can offer strikethrough annotation.

```
Stress-test batch cascade detected:
  Batch:       stress-test-YYYY-MM-DD-HHMMSS
  Ticker:      TICKER
  Research note: [[Research/YYYY-MM-DD - TICKER - Stress Test]]  (NOT deleted by rollback)
  
Log entry appended to Theses/TICKER - Name.md (Tier 2 append-only — no snapshot):
  [full entry text from manifest]

Options:
  (a) Surface only — leave Log entry as historical audit; manually annotate later.
  (b) Cascade + strikethrough — rewrite the Log entry as:
      `~~[original entry]~~ → Reverted YYYY-MM-DD: stress-test run judged
      invalid (rolled back via /rollback batch stress-test-YYYY-MM-DD-HHMMSS).`
  (c) Cancel.
```

If (b), perform the strikethrough Edit on the listed thesis. If the Edit fails, report and continue — the audit trail degrades gracefully to option (a).

Note: this cascade only surfaces the manifest's recorded Log entry. The research note under `Research/` is preserved as historical record (same policy as scenario and compare research notes).

### Step 2.5f: Thesis manifest cascade (H1)

If the selected snapshot or user-supplied batch ID matches a `/thesis` batch (`thesis-TICKER-YYYY-MM-DD-HHMMSS` prefix OR a companion `_thesis-manifest (thesis-...)` file exists), read the manifest for the full creation context.

`/thesis` is a constructive operation — it creates a new thesis file rather than modifying an existing one. There is no "before state" snapshot to restore; cascade recovery for thesis batches means **undoing the creation** (deleting the new thesis file, un-adding from sector note, reverting `_hot.md` entries, un-touching orphan research notes).

```
Thesis creation cascade detected:
  Batch:           thesis-TICKER-YYYY-MM-DD-HHMMSS
  Ticker:          TICKER
  Proposed name:   [proposed_name from manifest]
  Proposed path:   Theses/TICKER - [proposed_name].md
  Manifest:        [[_Archive/Snapshots/_thesis-manifest (...)]]

Landed operations (from manifest body):
  ✅ Thesis file created (or ⚠️ not created)
  ✅ Sector note updated — [sector] (or ℹ️ skipped/new_sector_created)
  ✅ _hot.md updated (Active Research Thread, Recent Conviction Changes, Open Questions)
  ✅ [N] orphan research notes touched (wikilinks added to Related Research)

Cascade options:
  (a) Delete thesis file only — remove `Theses/TICKER - [proposed_name].md`.
      Leaves sector note and _hot.md modifications in place (will dangle).
      Choose if you want to save the thesis content elsewhere first.
  (b) Full cascade — (a) + remove thesis wikilink from sector note Active Theses
      (use pre-thesis-snapshot if available, otherwise targeted Edit) + revert
      _hot.md entries (targeted Edit on manifest-listed entries) + revert orphan
      research mtimes (touch -d to pre-thesis timestamps from manifest if
      captured; otherwise skip mtime revert — unrelated Research/ mtime drift
      is low-blast-radius).
  (c) Cancel — take no action. Manually delete thesis + clean up if needed.

Confirm (a/b/c):
```

**Option (b) execution**:
1. `rm "Theses/TICKER - [proposed_name].md"` (if exists)
2. Remove `- [[Theses/TICKER - [proposed_name]]]` line from sector note Active Theses (Edit with exact-match)
3. Revert `_hot.md`:
   - Active Research Thread: strike through or remove the thesis-creation entry
   - Recent Conviction Changes: remove the `- **[TICKER]**: ... initial [level]` line
   - Open Questions: remove entries added by this `/thesis` run (manifest lists them verbatim)
4. If `new_sector_note_created` was in the manifest (user chose option (a) of §5 new-sector handling), offer to delete the newly-created sector note file too — but ONLY if the manifest confirms the sector was new (no prior content).

**Edit failures during cascade**: continue remaining steps; report per-step outcome. Users can complete partially-failed cascade manually via the manifest body as reference.

**Preservation note**: unlike sync/status rollbacks (which have pre-edit snapshots), thesis rollbacks are deletion-based. The thesis file's content is NOT preserved in `_Archive/Snapshots/` unless the user chose (a) and archived manually. Before accepting (b), consider whether the thesis content should be saved elsewhere.

### Step 2.5e: Status manifest cascade (T2.2)

If the selected snapshot is associated with a `/status` batch (user supplied `status-YYYY-MM-DD-HHMMSS` batch ID, OR the snapshot's `snapshot_batch:` field matches a `status-*` pattern), read the manifest for the full transaction context.

Unlike sync/compare/prune, `/status` is a single-ticker multi-file transaction (thesis frontmatter + sector note + optional archive mv + optional `.graph_invalidations` + `_hot.md`). The manifest lists every stage that landed:

```
Status transaction cascade detected:
  Batch:          status-YYYY-MM-DD-HHMMSS
  Ticker:         TICKER
  Transition:    [conviction|status] [old] → [new]
  Manifest:      [[_Archive/Snapshots/_status-manifest (status-...)]]
  
Stages that landed:
  ✅ Thesis frontmatter edited — snapshot: [[_Archive/Snapshots/...]]
  ✅ Sector note edited — snapshot: [[_Archive/Snapshots/...]]
  ✅ Archive move (closure only) — thesis moved to _Archive/
  ✅ Graph invalidations written
  ✅ _hot.md updated
  
Cascade options:
  (a) Restore thesis frontmatter only (from thesis snapshot).
  (b) Restore full transaction (thesis + sector note + un-archive + clear
      invalidation list). All-or-nothing atomicity restore.
  (c) Cancel.
```

Option (b) executes: restore thesis from its pre-status snapshot → restore sector note from its pre-status snapshot → if closure: `mv _Archive/TICKER - Name.md Theses/TICKER - Name.md` → clear matching entries from `.graph_invalidations` → revert `_hot.md` Recent Conviction Changes entry.

On any sub-step failure during cascade, abort remaining steps and report — the user can address each partial state manually. Pre-rollback safety snapshot (Step 4) covers the worst case.

## Step 3: Confirm (Mandatory)

Present the rollback plan and **wait for explicit user confirmation**:

**If the original file exists:**
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

**If the original file does not exist** (archived/deleted):
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

Before overwriting, snapshot the CURRENT version so the rollback itself is reversible.

**If the original file exists** (normal case):

### 4.1 — Generate timestamp and propose target path

```bash
mkdir -p _Archive/Snapshots
TS=$(date +%Y-%m-%d-%H%M%S)              # generate HHMMSS once
TARGET_BASE="_Archive/Snapshots/[Name] (pre-rollback ${TS})"
TARGET="${TARGET_BASE}.md"
```

### 4.2 — Filename collision check (CRITICAL-3 fix — handles recursive rollback)

> **Why this exists**: two consecutive `/rollback TICKER` invocations on the same file in the same minute (e.g., user rolls back, realizes wrong choice, immediately rolls back again to undo the undo) generate identical `(pre-rollback YYYY-MM-DD-HHMMSS).md` filenames. Without collision handling, the second `cp` silently overwrites the first safety snapshot — destroying the only path back to the intermediate state. Recursive rollbacks happen exactly when users are uncertain about which snapshot to restore, which is when the safety net matters most.

Before writing the safety snapshot, check if `${TARGET}` already exists. If yes, append an incrementing numeric suffix until a free filename is found:

```bash
SUFFIX=2
FINAL_TARGET="$TARGET"
while [ -e "$FINAL_TARGET" ]; do
  FINAL_TARGET="${TARGET_BASE}-${SUFFIX}.md"
  SUFFIX=$((SUFFIX + 1))
  # Sanity cap — abort if we somehow hit 100 collisions
  if [ "$SUFFIX" -gt 100 ]; then
    echo "❌ Pre-rollback safety snapshot: 100 same-second collisions on ${TARGET_BASE}. Aborting — investigate why so many rollbacks ran in the same second."
    exit 1
  fi
done
```

Example progression for three same-second recursive rollbacks of `TSM - Taiwan Semiconductor.md`:
- 1st rollback: `TSM - Taiwan Semiconductor (pre-rollback 2026-04-20-130045).md`
- 2nd rollback: `TSM - Taiwan Semiconductor (pre-rollback 2026-04-20-130045-2).md`
- 3rd rollback: `TSM - Taiwan Semiconductor (pre-rollback 2026-04-20-130045-3).md`

Each rollback gets its own safety net; none overwrites another.

### 4.3 — Write the safety snapshot

```bash
cp "[original file path]" "$FINAL_TARGET"
```

If `$FINAL_TARGET` differs from the original `$TARGET` (suffix was appended), surface in the skill report:
```
ℹ️ Safety snapshot used collision-suffix filename: [final basename] (incremented from [original basename] due to existing same-second snapshot — likely a prior rollback in this minute).
```

### 4.4 — Annotate frontmatter

Read the newly created safety snapshot and add to its frontmatter:
```yaml
snapshot_of: "[[original file path]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: rollback
snapshot_batch: rollback-YYYY-MM-DD-HHMMSS    # use the original TS, not the suffix — see note
```

> **Batch ID note**: the `snapshot_batch:` value uses the original `HHMMSS` timestamp WITHOUT the collision suffix. This is intentional — the batch ID groups snapshots created by the SAME `/rollback` invocation (cascade mode), not snapshots that happen to share a same-second timestamp across DIFFERENT invocations. Two recursive `/rollback TSM` runs each have their own batch ID generated at their own Step 4.1 — they will not share `snapshot_batch:` even if `HHMMSS` collides at the filename level. The collision-suffix lives only in the filename to keep snapshots distinguishable on disk.

**If the original file does not exist** (archived/closed — detected in Step 2):
Skip the safety snapshot — the current state is "file absent", preserved by the pre-archive snapshot (e.g., pre-prune or pre-status snapshot). Log: `Safety snapshot skipped — original file does not exist at [path].`

**Cascade batch mode**: When restoring multiple files (Step 2.5 option a), complete Step 4 (4.1 → 4.2 → 4.3 → 4.4) for ALL files in the restore set before proceeding to Step 5. This guarantees that every file has a safety snapshot before any restoration begins. If a safety snapshot fails to create for any file, report the failure and **do not proceed to Step 5** — no restorations should begin until all safety nets are in place. Use the same `snapshot_batch: rollback-YYYY-MM-DD-HHMMSS` value across all safety snapshots in the batch (per-file collision suffixes apply only to the filename portion, not the batch ID).

## Step 5: Restore

1. Read the snapshot content.
2. Remove the snapshot-specific frontmatter fields (`snapshot_of`, `snapshot_date`, `snapshot_trigger`, `snapshot_batch`) — these belong to the snapshot, not the live note.
3. Write the cleaned content to the original file path, fully replacing the current version.
4. Append a Log entry to the restored note (preserving the audit trail going forward):
   ```
   ### YYYY-MM-DD
   - ROLLBACK to snapshot (YYYY-MM-DD, pre-[trigger]). [N] log entries from [date range] lost. Safety snapshot: [[_Archive/Snapshots/Name (pre-rollback YYYY-MM-DD-HHMMSS)]]
   ```

### Cascade failure handling

**If a restoration fails mid-batch** (cascade mode — one or more files restored, others not): because Step 4 created safety snapshots for ALL files before any restoration began, the user has a complete safety net. Report:
```
⚠️ Cascade rollback partially completed.
Restored: [list of files successfully restored]
Failed: [file that failed + error]
Not attempted: [remaining files in the set]
All pre-rollback safety snapshots exist (batch: rollback-YYYY-MM-DD-HHMMSS).
To undo restored files: /rollback [any restored ticker] → select (pre-rollback) snapshot → cascade (a).
To retry failed files: /rollback [failed ticker] → select the original (pre-[trigger]) snapshot.
```
**Do NOT proceed to Step 6** for a partial cascade — post-rollback cleanup (sector note updates, graph reconciliation) should only run when all files in the set are at a consistent state.

## Step 6: Post-Rollback Cleanup

### 6.1: Conviction/status revert — sector note update

Runs only if the rollback changed `conviction:` or `status:` frontmatter (snapshot values differ from current pre-rollback values). Mirrors `/status` Step 5 protocol end-to-end to guarantee the sector note edit is sector-resolved, dry-run gated, snapshotted, and verified — no implementation-dependent ambiguity.

If `status:` was reverted to `active` from a closure (file recreated from archive), surface the informational warning once at the start of 6.1: `ℹ️ Restored status is already active — do NOT run /status closed→active (it will fail validation). Proceed directly to /sync TICKER → /graph.`

#### 6.1a: Resolve sector note (via contract)

Resolve the sector note using the canonical procedure at **`.claude/skills/_shared/sector-resolution.md`**. Inputs: restored thesis's `sector:` frontmatter. Outputs: `sector_note_path`, `match_confidence`, `log_message`.

- `match_confidence: none` → emit contract's no-match warning, skip 6.1b–6.1f entirely, proceed to 6.2.
- `match_confidence: normalized` → emit contract's `log_message`, proceed silently to 6.1b.
- `match_confidence: substring` → emit contract's `log_message` AND **stop for explicit user confirmation** before proceeding (per contract Caller Responsibility #4 — destructive edits on substring-matched sectors require confirmation). If declined, skip 6.1b–6.1f, proceed to 6.2.
- `match_confidence: exact` → proceed silently to 6.1b.

#### 6.1b: Dry-run — determine whether an edit is needed

Mirror `/status` Step 5.1 decision matrix based on the reverted field and direction:

| Revert direction | Check against sector note | Set `edit_planned: true` when... |
|---|---|---|
| `status: closed → active` (file recreated from archive) | (1) thesis wikilink in Active Theses? (2) thesis wikilink in Closed/Archived section? | ABSENT from Active Theses **OR** PRESENT in Closed/Archived (stale entry from prior closure). Composed check — either condition triggers. |
| `status: active → closed` (revert of reopen) | thesis wikilink in Active Theses? | PRESENT — Step 6.1d will remove it. |
| `status: monitoring → active` (revert) | thesis wikilink absent from Active Theses OR annotated as monitoring? | Either condition true. |
| `status: active → monitoring` (revert) | does sector distinguish monitoring AND thesis not already annotated? | Both true. |
| `conviction:` reverted (any direction) | does sector display conviction levels (e.g., `(medium)` suffix, Conviction column, grouped-by-conviction structure) AND displayed value differs from reverted value? | Both true. |

Detection indicators (reuse `/status` Step 5.1):
- Monitoring distinction: `## Monitoring`, `(monitoring)`, `monitoring:`, or thesis wikilink suffixed with monitoring marker.
- Conviction display: `(high)`, `(medium)`, `(low)` adjacent to thesis wikilinks, OR `| Conviction |` column header, OR section headings grouped by conviction level.

If `edit_planned: false`: log `ℹ️ Sector note update skipped — [sector_note_path] already reflects reverted state (rationale: [cascade already restored | post-closure state clean | conviction not displayed | state already matches]).` Proceed to 6.2.

If `edit_planned: true`: proceed to 6.1c.

#### 6.1c: Pre-edit snapshot

Before modifying the sector note, snapshot it:

```bash
cp "[sector_note_path]" "_Archive/Snapshots/[Sector Name] (pre-rollback YYYY-MM-DD-HHMMSS).md"
```

Read the newly created snapshot and add to frontmatter:
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: rollback
snapshot_batch: rollback-YYYY-MM-DD-HHMMSS
```

**Reuse the `HHMMSS` batch ID generated in Step 4** (same rollback run's safety snapshot). This enables `/rollback` cascade detection to couple this sector snapshot with the thesis's pre-rollback safety snapshot — a future rollback of this rollback (rare but supported) can cascade-restore both files atomically.

**Cascade batch mode interaction**: if the rollback is itself a cascade restoring multiple theses whose sectors all need updates, generate a distinct `HHMMSS` for each sector's snapshot only if the sectors differ. If one sector serves multiple cascaded theses, one sector snapshot with one batch ID suffices.

#### 6.1d: Apply the edit

Mirror `/status` Step 5b rules. Use targeted `Edit` operations (atomic string replacement), NOT full-file `Write`. Each `Edit` either succeeds atomically or leaves the section unchanged.

1. **For status reverted to `active`** (from closed, monitoring, or draft): add thesis wikilink to Active Theses section (if ABSENT). Remove monitoring annotation if present. If a "Closed/Archived" section exists and contains this thesis, remove the entry from there as well (prevents dual listing).
2. **For status reverted to `monitoring`** (from active): apply monitoring annotation per sector convention (move to "Monitoring" section, add `(monitoring)` suffix, etc. — match the sector's existing convention).
3. **For status reverted to `closed`** (rare — rollback of a reopen): remove thesis from Active Theses. Add to "Closed/Archived" section if one exists.
4. **For `conviction:` reverted**: update the displayed conviction level for this thesis to the reverted value (e.g., `(medium)` → `(high)`, or move thesis between conviction-grouped sections).

#### 6.1e: Post-edit verification

Re-read the modified sector note. For each edited section, verify:
1. Ends with a complete sentence (not mid-word, mid-sentence, or with unmatched `**` or `*`).
2. No incomplete table rows (lines starting with `|` but not ending with `|`).
3. Thesis wikilink is present/absent per 6.1d intention (re-grep the section to confirm).
4. Dual-listing absent: thesis wikilink appears in AT MOST ONE of {Active Theses, Closed/Archived, Monitoring} sections.

If any check fails: `⚠️ Sector note may contain a partial edit in [section]. Snapshot available: [[_Archive/Snapshots/[Sector Name] (pre-rollback YYYY-MM-DD-HHMMSS)]]. Review manually or run /rollback on the sector snapshot to revert this rollback's sector update independently.`

#### 6.1f: Report

- **Sector note resolved**: `[sector_note_path]` (confidence `[exact|normalized|substring|none]`)
- **Sector edit**: `applied (edit_planned: true)` | `skipped (edit_planned: false — state already matches)` | `skipped (match_confidence: none)` | `skipped (user declined substring confirmation)`
- **Sector snapshot**: `[[_Archive/Snapshots/[Sector Name] (pre-rollback YYYY-MM-DD-HHMMSS)]]` (if 6.1c ran) | `n/a (skip case)`
- **Post-edit verification**: `passed` | `⚠️ failed: [specific check]` (if 6.1e ran)

### 6.2: Archived file cleanup
If the original file was recreated (did not exist before rollback — detected in Step 2), check for a corresponding archived copy. **Glob must include the ` - ` separator and `.md` suffix** to avoid false positives on short tickers (e.g., `A`, `T`, `U`) where `TICKER*` would match every archived file whose name starts with that letter:
```bash
find _Archive/ -maxdepth 1 -name "TICKER - *.md" -type f
```
If found, move it to Snapshots to prevent duplication (preserves the closure audit trail):
```bash
mv "_Archive/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (archived pre-rollback YYYY-MM-DD-HHMMSS).md"
```
Add `snapshot_of`, `snapshot_date: YYYY-MM-DD`, `snapshot_trigger: rollback-cleanup`, `snapshot_batch: rollback-YYYY-MM-DD-HHMMSS` (reuse the batch ID from Step 4) to its frontmatter.

### 6.2.5: Intervening-neighbor Log scan (5.3 fix — recreated-file rollbacks only)

**Only runs for recreated-file rollbacks** (i.e., the original file did NOT exist before rollback — Step 2 detection). Skip entirely for standard rollbacks (existing file restored in place).

Problem this solves: Thesis X was closed on day C. Between day C and today (rollback day R), other skills (`/stress-test`, `/sync`, `/scenario`, `/compare`) may have written Log entries to OTHER theses citing X's closure as premise (e.g., "AMAT no longer faces NVDA competition after NVDA closure"). After restoring X on day R, those intervening Log entries are premised on a now-false state. The entries are Tier 2 append-only; they cannot be silently edited. But the user needs to know they exist, and needs tooling to annotate them.

Procedure:

1. **Identify closure date**. From the just-restored thesis's Log, find the final `CLOSED:` or `Cross-thesis closure:` pre-closure entry if present. Alternate source: the pre-rollback snapshot's body if the current restored state doesn't carry closure markers. Capture `closure_date: YYYY-MM-DD` (the date the `CLOSED` Log entry was written, NOT the date the file was mv'd — those are typically the same but may differ by a day for delayed archive moves).

2. **Identify citing files** (H3 — extended beyond `Theses/` to cover macros and sectors). Grep THREE directories (excluding the just-restored thesis itself) for wikilink patterns that reference the just-restored thesis:
   - **`Theses/*.md`** — neighbor thesis Logs with post-closure entries
   - **`Macro/*.md`** (H3 addition) — macro notes may cite the closed thesis in narrative (e.g., "Iranian retaliation risk most directly affects [[_Archive/LITE - Lumentum]]..."). Macros often lack `## Log` sections, so body-prose citations matter.
   - **`Sectors/*.md`** (H3 addition) — sector notes may reference the closed thesis in Acquisitions and new entrants, Industry history, Competitive dynamics, or Log sections. Post-closure narrative may have been written assuming the closure.

   Wikilink patterns (searched across all three directories):
   - `[[Theses/TICKER - Name]]`, `[[Theses/TICKER - Name|...]]`, `[[Theses/TICKER - Name#...]]`, `[[Theses/TICKER - Name.md]]`
   - `[[_Archive/TICKER - Name]]` (from `Cross-thesis closure:` entries and post-closure narrative references)
   - `[[TICKER - Name]]` folder-less form

   Collect unique citing-file paths, tagging each with its category (`thesis` | `macro` | `sector`).

3. **For each citing file**, scan for post-closure references:
   - **Theses** — scan the `## Log` section for entries matching BOTH:
     - Entry date `>= closure_date` (post-closure)
     - Entry body contains a wikilink to the restored thesis
   - **Macros** — scan the ENTIRE BODY (not just Log) for citations. Macros use narrative prose — a sentence like "LITE's closure removes the Lumentum lever from this transmission chain" is a premise-dependent reference but isn't in a Log entry. Capture citation location as file-path + line-number context for the user review prompt. If the macro DOES have a `## Log` section with dated entries, prioritize those per the thesis pattern.
     - **Date attribution**: macros without dated Log entries are harder to classify as "post-closure" vs "pre-closure legacy". Use the file's mtime as a weak signal: if `file_mtime >= closure_date`, treat body citations as post-closure candidates; otherwise include with an advisory flag ("citation predates closure — may be legitimate historical context").
   - **Sectors** — scan:
     - `## Log` section per the thesis pattern (post-closure dated entries)
     - Narrative sections that may carry post-closure premise: `## Acquisitions and new entrants`, `## Competitive dynamics`, `## Industry history` (if post-closure text was added). Use same mtime-based attribution as macros.
     - `## Active Theses` — already handled by `/status`/`/prune` at closure time; not scanned here (those sections should no longer reference the closed thesis if closure was clean).

4. **Classify each matched citation** by source and prefix heuristic:
   - **Thesis Log — Premise-dependent**: entry prefix is one of `Cross-thesis closure:`, `Cross-thesis closures:` (registry §13 — `/prune`-emitted notification, explicitly premised on closure)
   - **Thesis Log — Scenario/stress-test citation**: entry prefix starts with `Stress test`, `Scenario`, or `Scenario REVERSED` AND body text cites the restored thesis (premise depends on context)
   - **Thesis Log — Sync-propagated**: entry prefix is a research-note wikilink (`- [[Research/...]]:`) that happens to cite the closed thesis in its rationale
   - **Macro body citation** (H3): prose sentence in a macro note referencing the closed thesis. Categorize as "likely premise-dependent" (sentence asserts something about the closed state) or "contextual" (sentence cites the thesis as historical example). LLM judgment required — the prefix heuristic doesn't apply to narrative prose.
   - **Sector body citation** (H3): prose in a sector narrative section. Same sub-categories as macro.
   - **Sector Log — post-closure entry**: same pattern as thesis Log entries.
   - **Other**: any other citation

5. **Present findings for user review**:

   ```
   ⚠️ Intervening Log entries detected — closure of [[restored thesis]] dated [closure_date]
      may have been cited as premise by other skills between [closure_date] and today.

   [N] entries found across [M] theses (dated post-closure, citing this thesis):

   [[Theses/AMAT - Applied Materials.md]]:
     - 2026-04-20: Cross-thesis closure: [[_Archive/NVDA - Nvidia]] archived — AI capex
       exposure reduced. [prefix: Cross-thesis closure — PREMISE-DEPENDENT]
     - 2026-04-25: [[Research/...]]: ASML guidance... given NVDA exit, AMAT positioning... 
       [prefix: research-note wikilink — PARTIAL PREMISE DEPENDENCY]

   [[Theses/AVGO - Broadcom.md]]:
     - 2026-05-02: Stress test [[Research/...]]: without NVDA competition... [prefix: 
       Stress test — PARTIAL PREMISE DEPENDENCY]

   Options:
     (a) Surface only — leave entries as historical audit trail, no edits. Recommended if
         the user will manually review each thesis.
     (b) Auto-strikethrough premise-dependent entries (`Cross-thesis closure:` prefix only —
         the explicit premise category). Entries are rewritten as:
         `~~Cross-thesis closure: ...~~ → Superseded YYYY-MM-DD: [restored thesis] reopened via /rollback.`
         This violates Tier 2 append-only, but closure-notification entries are explicitly
         corrective-signal-preservable (mirrors the /scenario reverse and /sync cascade
         strikethrough pattern).
     (c) Auto-strikethrough ALL matched entries (premise-dependent + partial) with:
         `~~entry~~ → Review YYYY-MM-DD: [restored thesis] was reopened — premise may no
         longer apply.` Aggressive but unambiguous; user must manually re-add accurate
         context per affected entry.
     (d) Skip — do not scan further; acknowledge the gap manually.

   Confirm (a/b/c/d):
   ```

6. **Branch behavior**:
   - **(a)**: Add a summary note to the rollback report (Step 7) listing affected theses and entries. No file modifications beyond what Step 6 already did. User does manual review.
   - **(b)**: Iterate the "Cross-thesis closure" entries and strikethrough-rewrite each per the template. Include affected theses in the Step 7 report. The strikethrough preserves audit trail; the `→ Superseded` annotation creates a corrective signal for future Log readers.
   - **(c)**: Iterate ALL matched entries; apply the more generic strikethrough template. Report in Step 7.
   - **(d)**: Log `ℹ️ Intervening-neighbor scan skipped per user confirmation. [N] entries flagged but not annotated.` Include the full list in Step 7 report.

7. **Edit failure handling**: if a strikethrough Edit fails on an affected thesis (file lock, concurrent modification), record the failure and continue with remaining edits. Report failed edits in Step 7 alongside successful ones.

> **Why this scan only runs on recreated-file rollbacks**: standard rollbacks restore a file that was never closed — there's no closure date to anchor the post-closure scan, and intervening edits to the restored file's body (rather than to neighbors' Logs) are the relevant recovery concern. Cascade detection (Step 2.5) already handles neighbor edits for sync-batch rollbacks; this new step covers the specific gap of closure-reopen.

> **Interaction with Step 2.5b sync manifest cascade**: if the rollback target's closure was done via `/status active→closed` (not `/prune`), no sync manifest exists for the closure itself; 6.2.5's scan is the primary tool. If closure was via `/prune`, the prune manifest (now 30-day retained per 5.2 fix) may exist and cascade detection at Step 2.5 already surfaces neighbor Log entries from the Stage 4.2 "Cross-thesis closure" batch. In that case, 6.2.5 runs redundantly but safely — its `Cross-thesis closure:` prefix filter finds the same entries Step 2.5b already presented, and the user chooses once. The skill should detect this overlap and log `ℹ️ 6.2.5 scan overlaps with Step 2.5b prune-manifest cascade; showing combined list.` rather than prompting twice.

### 6.3: Graph update deferred

`_graph.md` is now owned exclusively by `/graph`. **After this rollback, run `/graph last` immediately** — it captures all graph effects from current vault state:

- **Standard rollback** (existing thesis restored): `/graph last` re-extracts adjacency from the restored thesis file, updates reverse indexes, and removes any restored research notes from the orphan list (no longer orphaned now that the restored thesis links them).
- **Recreated-file rollback** (closed thesis re-opened): `/graph last` rebuilds the absent adjacency entry from the restored thesis file. The full-rebuild path captures the new adjacency, reverse-index re-entry, and Cross-Thesis Cluster restoration in a single pass — no need for the prior architecture's recreated-file exception logic.

> **Why running `/graph last` immediately matters for recreated-file rollbacks**: subsequent skills relying on `_graph.md` (e.g., `/sync` default mode) need the restored thesis's adjacency entry. Without `/graph last`, the thesis exists on disk but is invisible to graph-assisted propagation paths.

### 6.4: Update _hot.md
Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: rolled back [TICKER/note] to [snapshot date] snapshot, and what was reverted. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: If conviction or status was reverted, add entry: `- **[TICKER]**: rollback [field] [current] → [reverted] — restored to [snapshot date] state`
3. **Open Questions**: If the rollback restored previously-resolved Outstanding Questions, re-add them

**Word cap**: After all `_hot.md` edits, follow the compression trigger order in `.claude/skills/_shared/hot-md-contract.md` §"Compression trigger order": drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → emit warning. Soft cap 4,000 words, hard cap 5,000 words (abort `_hot.md` write on hard-cap breach; `/rollback` primary operation still succeeds).

## Step 7: Report

### For normal rollbacks (Steps 4–6 executed)

- **Restored**: [[original file path]] from snapshot dated YYYY-MM-DD
- **Safety snapshot**: [[_Archive/Snapshots/Name (pre-rollback YYYY-MM-DD-HHMMSS)]]
- **Sections reverted**: [list]
- **Log entries lost**: [count] — preserved in safety snapshot
- **Side effects**: [sector note updated / graph updated / conviction reverted]
- **Graph reminder**: `→ Run /graph last to update the dependency map.` (Critical for recreated-file rollbacks — restored thesis is invisible to graph-assisted propagation until /graph last runs.)
- **Duplicate-file note** (Step 4a option (b) only): `⚠️ Content-only restore created duplicate file. Original path: [[snapshot_of]]. Current name: [[rename_target]]. Inbound wikilinks across vault still point to current name. To consolidate, decide which copy to keep, then delete the other and run /sync.`
- **To undo this rollback**: `/rollback [ticker]` and select the `(pre-rollback)` snapshot

### For rename-undo redirect (Step 4a option (a) — symmetric reverse-rename)

When the user chose option (a), the rollback exited without modifying any files. Report:

- **Rollback exited — no changes made.**
- **Reason**: snapshot was created by `/rename`. Symmetric reverse via `/rename` is the correct undo path.
- **Run this command**: `/rename [TICKER] "[old_name from snapshot]"`
- **Rationale**: `/rename` atomically restores filename, inbound wikilinks (7 patterns), `_graph.md` adjacency header, sector note Active Theses entry, and `_Archive/Snapshots/` `snapshot_of:` fields — operations `/rollback` cannot perform without duplicating `/rename` logic. After `/rename` succeeds, this snapshot remains in `_Archive/Snapshots/` as historical record (clean up later via `/clean` if desired).

### For cancellation (Step 4a option (c))

- **Rollback canceled — no changes made.**

## Step 8: Release lock

After Step 7's report is complete, release the vault lock per `.claude/skills/_shared/preflight.md` §1.7 as the skill's FINAL Bash block. Lock scope depends on mode acquired in Step 0.1:
- List mode → `.vault-lock.readonly`
- Restore mode (including cascade) → `.vault-lock`

Runs unconditionally — whether restore completed, was redirected to `/rename` (Step 4a option a), or was cancelled (Step 4a option c).

```bash
# Lock release — verify ownership before rm (preflight §1.5)
# LOCK_FILE path depends on mode:
#   list mode   → .vault-lock.readonly
#   restore     → .vault-lock
LOCK_FILE="<paste-from-Step-0.1>"                # e.g., .vault-lock or .vault-lock.readonly
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ($LOCK_FILE) ==="
else
  echo "⚠️ Lock ownership check failed at release ($LOCK_FILE) — skipping rm to avoid stealing another skill's lock."
fi
```
