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

1. Extract `snapshot_batch:` from the selected snapshot's frontmatter. If `snapshot_batch:` is absent (legacy snapshot created before this field was introduced), fall back to matching on `snapshot_trigger:` + date portion of `snapshot_date:` (`YYYY-MM-DD`, ignoring any time suffix). **Both `-HHMM` (pre-HHMMSS-standardization legacy snapshots) and `-HHMMSS` (current 6-digit format) are recognized** — match on the `YYYY-MM-DD` prefix only when comparing across formats.
2. Search `_Archive/Snapshots/` for other snapshots with matching `snapshot_batch:` value (or matching trigger + date in fallback mode). Batch matching is operation-precise — same-day repeat operations (e.g., two `/sync` runs on the same day) get distinct batch IDs and will not cross-match.
3. If matches found, present them:

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

4. **Wait for user selection.**
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

If no matches are found, proceed silently to Step 3.

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

### Step 2.5c: Non-sync trigger snapshots

For non-sync triggers (status, deepen, compare, prune, catalyst, rename, rollback), no manifest exists — those skills snapshot every modified file (Tier A only) per their own atomicity rules. Proceed with Step 2.5a behavior unchanged.

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
```bash
mkdir -p _Archive/Snapshots
cp "[original file path]" "_Archive/Snapshots/[Name] (pre-rollback YYYY-MM-DD-HHMMSS).md"
```
Read the newly created safety snapshot and add to its frontmatter:
```yaml
snapshot_of: "[[original file path]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: rollback
snapshot_batch: rollback-YYYY-MM-DD-HHMMSS
```
> **Batch ID**: Generate `HHMMSS` once (via `date +%H%M%S`). 6-digit second-precision prevents same-minute snapshot batch collisions across skills. Reuse this `snapshot_batch` value for the Step 6 cleanup snapshot if one is created.

**If the original file does not exist** (archived/closed — detected in Step 2):
Skip the safety snapshot — the current state is "file absent", preserved by the pre-archive snapshot (e.g., pre-prune or pre-status snapshot). Log: `Safety snapshot skipped — original file does not exist at [path].`

**Cascade batch mode**: When restoring multiple files (Step 2.5 option a), complete Step 4 for ALL files in the restore set before proceeding to Step 5. This guarantees that every file has a safety snapshot before any restoration begins. If a safety snapshot fails to create for any file, report the failure and **do not proceed to Step 5** — no restorations should begin until all safety nets are in place. Use the same `snapshot_batch: rollback-YYYY-MM-DD-HHMMSS` value across all safety snapshots in the batch.

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

### Conviction or status revert
If the rollback changed `conviction:` or `status:` frontmatter (i.e., the snapshot has a different value than what was current):
- Update the relevant Sector Note to reflect the reverted value
- Warn: `⚠️ Conviction/status reverted to [old value]. Sector note updated.`
- If `status:` was reverted to `active` from a closure (file recreated from archive), additionally warn: `ℹ️ Restored status is already active — do NOT run /status closed→active (it will fail validation). Proceed directly to /sync TICKER → /graph.`

### Archived file cleanup
If the original file was recreated (did not exist before rollback — detected in Step 2), check for a corresponding archived copy. **Glob must include the ` - ` separator and `.md` suffix** to avoid false positives on short tickers (e.g., `A`, `T`, `U`) where `TICKER*` would match every archived file whose name starts with that letter:
```bash
find _Archive/ -maxdepth 1 -name "TICKER - *.md" -type f
```
If found, move it to Snapshots to prevent duplication (preserves the closure audit trail):
```bash
mv "_Archive/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (archived pre-rollback YYYY-MM-DD-HHMMSS).md"
```
Add `snapshot_of`, `snapshot_date: YYYY-MM-DD`, `snapshot_trigger: rollback-cleanup`, `snapshot_batch: rollback-YYYY-MM-DD-HHMMSS` (reuse the batch ID from Step 4) to its frontmatter.

### Graph update deferred

`_graph.md` is now owned exclusively by `/graph`. **After this rollback, run `/graph last` immediately** — it captures all graph effects from current vault state:

- **Standard rollback** (existing thesis restored): `/graph last` re-extracts adjacency from the restored thesis file, updates reverse indexes, and removes any restored research notes from the orphan list (no longer orphaned now that the restored thesis links them).
- **Recreated-file rollback** (closed thesis re-opened): `/graph last` rebuilds the absent adjacency entry from the restored thesis file. The full-rebuild path captures the new adjacency, reverse-index re-entry, and Cross-Thesis Cluster restoration in a single pass — no need for the prior architecture's recreated-file exception logic.

> **Why running `/graph last` immediately matters for recreated-file rollbacks**: subsequent skills relying on `_graph.md` (e.g., `/sync` default mode) need the restored thesis's adjacency entry. Without `/graph last`, the thesis exists on disk but is invisible to graph-assisted propagation paths.

### Update _hot.md
Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: rolled back [TICKER/note] to [snapshot date] snapshot, and what was reverted. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: If conviction or status was reverted, add entry: `- **[TICKER]**: rollback [field] [current] → [reverted] — restored to [snapshot date] state`
3. **Open Questions**: If the rollback restored previously-resolved Outstanding Questions, re-add them

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

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
