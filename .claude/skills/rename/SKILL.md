---
name: rename
description: Rename a thesis file when company name changes. Atomically updates filename, all inbound wikilinks across the vault, graph adjacency entry header, sector note Active Theses entry, snapshot snapshot_of references, and _hot.md mentions. Use when company changes name (FB → META, Square → Block, etc.), or when correcting a typo in a thesis filename.
model: sonnet
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * mv * cp * mkdir * find * grep *)
---

Rename a thesis file when the company name portion changes. **TICKER does NOT change** — only the segment after ` - `. Example: `Theses/META - Meta.md` → `Theses/META - Meta Platforms.md`.

Without `/rename`, manual file renames break: (a) every inbound wikilink across the vault, (b) `_graph.md`'s adjacency header, (c) sector note Active Theses entries, (d) `snapshot_of:` fields in `_Archive/Snapshots/` (breaking `/rollback`), (e) `_hot.md` free-text mentions. `/lint #3` catches broken wikilinks only after the fact without auto-fix.

Design rationale in `.claude/skills/rename/RATIONALE.md` (§N.M anchors).

## Arguments

`$ARGUMENTS` = `TICKER "New Company Name"`. Examples:
- `/rename META "Meta Platforms"`
- `/rename SHOP "Shopify Inc"`
- `/rename SQ "Block"` (after Square → Block rebrand)

Missing quoted name, no ticker, or extra args → ask user to clarify.

## Step 0: Pre-flight

### 0.1: Acquire vault lock

`ticker:TICKER` scope per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout 5 min. Capture token, verify (Procedure 1.5) every subsequent block, release in final reporting block.

### 0.2: Name sanitization (C6.1 — §7)

Run `.claude/skills/_shared/preflight.md` Procedure 3 against proposed `new_name` from $ARGUMENTS:
1. NFC-normalize input.
2. Trim leading/trailing whitespace. Empty → reject.
3. Length ≤ 100 bytes → reject if exceeded.
4. Character whitelist: `[a-zA-Z0-9 \-_.,'&()]`. Any other character → reject (specific flag for `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`).
5. No leading dot → reject.
6. First whitespace-token not reserved (`CON`, `PRN`, `AUX`, `NUL`, `COM1-9`, `LPT1-9`, case-insensitive) → reject.

On rejection, emit contract's standard rejection message + suggested clean variant. Do NOT proceed.

## Step 1: Validate

1. **Find current thesis** via ticker-prefix glob: `Theses/TICKER - *.md`.
   - Zero matches: stop. `⚠️ No thesis found for [TICKER] in Theses/. Run /thesis [TICKER] to create.`
   - Multiple: stop. `⚠️ Multiple Theses/ files match prefix "[TICKER]" — [list]. Resolve filename collision before re-running.`
   - One match: extract `[old_name]` from `Theses/TICKER - [old_name].md`.

2. **Compute new filename**: `Theses/TICKER - [new_name].md`.

3. **Validate new name**:
   - No path-illegal characters (double-checked post-sanitization).
   - Must not match existing file at new path in `Theses/`. Collision → stop: `⚠️ Target file already exists: Theses/TICKER - [new_name].md. Choose a different name or remove the existing file first.`
     - **Exception — incomplete-rename repair** (§2.2): if `.rename_incomplete.TICKER` exists AND its `new_name:` equals proposed new name, this is a repair re-run. The collision is expected (filename move from prior failed run already produced `Theses/TICKER - [new_name].md`). Skip abort, log `ℹ️ Repair re-run detected — .rename_incomplete.TICKER exists for [TICKER] → [new_name]. Skipping mv (already done), proceeding to retry failed wikilink rewrites from Step 5.`, jump from Step 1 directly to Step 5 (skip Steps 2/3/3.5/4).
   - **Archive collision check** (§6): glob `_Archive/TICKER - [new_name].md` (non-recursive — ignore `_Archive/Snapshots/`). Match → warn, require explicit confirmation:
     ```
     ⚠️ Archive collision: _Archive/TICKER - [new_name].md already exists from a prior closure of this ticker. If you later close the renamed thesis, /status Step 7.5 would mv the new thesis to the same archive path and silently overwrite the old archive copy.
     
     Options:
       (a) Proceed anyway (accept future overwrite risk).
       (b) Rename the old archive first: mv "_Archive/TICKER - [new_name].md" "_Archive/TICKER - [new_name] (closed YYYY-MM-DD).md" — then re-run /rename.
       (c) Cancel.
     ```
     Wait for user selection. Do NOT proceed silently.

4. **Check no-op**: `[old_name] == [new_name]` (case-sensitive after trim) → stop. `⚠️ Old and new names match. Nothing to rename.`
   - **Exception — incomplete-rename repair**: same bypass as Step 1.3 when `.rename_incomplete.TICKER` matches proposed new name.

### Step 1.4.5: Incomplete-rename cross-name guard (§2.3)

If `.rename_incomplete.TICKER` exists, read its frontmatter and compare `new_name:` to proposed new name:

- **`marker.new_name == proposed_new_name`** → repair re-run (already handled by Steps 1.3/1.4 exceptions). Jump to Step 5.
- **`marker.new_name != proposed_new_name`** → STOP with explicit guard. Proceeding would orphan repair targets.

   ```
   ❌ In-flight rename conflict for TICKER:
     Existing marker: .rename_incomplete.TICKER
       prior new_name:     [marker.new_name]
       failed_files:       [N entries — these need OldName → marker.new_name rewrites]
       batch:              [marker.batch]
   
     Proposed rename:
       new new_name:       [proposed_new_name]
   
   These conflict. The marker's failed wikilink rewrites were collected for
   "[marker.new_name]" — proceeding with "[proposed_new_name]" would orphan those
   repair targets (their wikilinks would still reference an obsolete OldName,
   never NewName2, with no marker to track them).
   
   Resolve before re-running /rename. Options:
     (a) Finish the prior rename first:
         /rename TICKER "[marker.new_name]"
         (re-runs Step 5 wikilink rewrites for the still-failing files;
         when all succeed, marker auto-deletes)
     (b) Manually resolve the failed files listed in the marker, then
         delete the marker (rm ".rename_incomplete.TICKER"), then re-run
         this rename.
     (c) Accept loss of in-flight repair state. BEFORE running rm:
         (1) READ the marker's "Failed files" list. Print with explicit warning:
             "These N file(s) currently contain wikilinks to [[Theses/TICKER -
              [TRULY_ORIGINAL_NAME]]] (the name BEFORE the prior failed rename).
              After deleting the marker and re-running with the new name, those
              wikilinks will remain broken — Step 5's grep/replace targets the
              CURRENT filename ([marker.new_name]), not the truly-original name.
              The new rename's Step 5 will NOT fix these. /lint #3 will flag them
              eventually.
              Resolution before option (c): manually grep-replace
              [TRULY_ORIGINAL_NAME] → [proposed_new_name] in each listed file
              FIRST, then proceed."
         (2) Wait for explicit user confirmation of manual remediation OR explicit
             acceptance of broken-wikilink outcome.
         (3) Only then rm ".rename_incomplete.TICKER" and re-run /rename.
   ```

   Do NOT proceed silently. Wait for user action, then re-invoke.

5. **Survey inbound references** (read-only — for confirmation prompt):
   - Grep vault (excluding `.git/` and `_Inbox/processed/`) for Step 5 patterns. `_Archive/Snapshots/` IS included (Step 5 rewrites snapshot bodies). Count live-file matches vs snapshot-body matches separately.
   - Grep `_Archive/Snapshots/` frontmatter for `snapshot_of:` referencing old path. Count. (Separate from body matches — frontmatter handled by Step 8.)
   - Read `_graph.md`, locate `### TICKER - [old_name]` in Adjacency Index. Note presence.
   - Resolve sector note via `.claude/skills/_shared/sector-resolution.md`. Matched → scan Active Theses for old wikilink.
   - Read `_hot.md`, count free-text mentions of `TICKER - [old_name]` (outside wikilink syntax).

## Step 2: Confirm (Tier 3 — Mandatory)

Present proposed rename + survey. **Wait for explicit user confirmation.**

```
Proposed rename:
  Old: [[Theses/TICKER - old_name]]
  New: [[Theses/TICKER - new_name]]

Side effects (will be updated):
  - Inbound wikilinks in live files: [count] across [N] files — [list paths]
  - Inbound wikilinks in snapshot bodies: [count] across [M] snapshots (excludes the pre-rename snapshot from Step 3)
  - Graph adjacency entry header: ### TICKER - [old_name] → ### TICKER - [new_name]
  - Sector note Active Theses entry: [present/absent — sector resolved as [sector_name] via [confidence]]
  - Snapshot snapshot_of fields: [count] snapshots in _Archive/Snapshots/
  - _hot.md free-text mentions: [count] occurrences

Pre-rename safety snapshot will be created.

Confirm? (y/n)
```

**Do NOT proceed without explicit user confirmation.**

## Step 3: Pre-Rename Snapshot

```bash
mkdir -p _Archive/Snapshots
HHMMSS=$(date +%H%M%S)
cp "Theses/TICKER - [old_name].md" "_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS).md"
```

Read snapshot, add frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - [old_name]]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: rename
snapshot_batch: rename-YYYY-MM-DD-HHMMSS
rename_target: "[[Theses/TICKER - [new_name]]]"
```

Batch ID uses HHMMSS (6 digits) to prevent same-minute collisions. `rename_target:` field tells `/rollback` that a cascade matching this batch is reversing a rename.

## Step 3.5: Pre-flight Read/Write Check (§1)

Step 5's rewrite will touch every file in the inbound-reference set. Catch unreachable files BEFORE the mv — §1.1 explains why.

For each file in the inbound-reference set (live files in `Theses/`, `Sectors/`, `Macro/`, `Research/`, `_hot.md`, plus `_Archive/Snapshots/*.md` with body matches and `snapshot_of:` matches):

1. **Read check**: attempt to read file's first 10 bytes. Fail → record in `unreachable_files: [list]`.
2. **Write probe**: `[ -w "path" ]`. Not writable → record in `unreachable_files`.

**`unreachable_files` non-empty → STOP.** Vault in original state (no mv, no edits).

```
❌ Pre-flight check failed: [N] file(s) cannot be edited. Rename aborted — vault unchanged.

Unreachable files:
  - [path 1] (reason: [permission denied | file locked | not found])
  - [path 2] (reason: ...)

Resolve access issue (close file in another editor, fix permissions, restore deleted file) and re-run /rename. Pre-rename snapshot retained: [[_Archive/Snapshots/...]].
```

## Step 4: Move the File

```bash
mv "Theses/TICKER - [old_name].md" "Theses/TICKER - [new_name].md"
```

Verification:
```bash
ls "Theses/TICKER - [new_name].md"
ls "Theses/TICKER - [old_name].md" 2>/dev/null  # should produce no output
```

`mv` fails → stop. `❌ Rename failed at mv step — vault unchanged. Snapshot retained: [[_Archive/Snapshots/...]]. Investigate filesystem permissions.` Wikilinks not modified; vault safe.

## Step 5: Update Inbound Wikilinks (§3, §5)

Grep vault (excluding `.git/` and `_Inbox/processed/`), Edit each file. **`_Archive/Snapshots/` is NOT excluded** — snapshot bodies contain wikilinks that, if stale, break on rollback (§3.1).

Seven wikilink patterns (§5 — includes 2 archive-specific forms beyond the 5-form canonical contract):

| Pattern | Replacement |
|---|---|
| `[[Theses/TICKER - old_name]]` | `[[Theses/TICKER - new_name]]` |
| `[[Theses/TICKER - old_name\|alias]]` | `[[Theses/TICKER - new_name\|alias]]` (preserve alias) |
| `[[Theses/TICKER - old_name#section]]` | `[[Theses/TICKER - new_name#section]]` (preserve anchor) |
| `[[Theses/TICKER - old_name.md]]` | `[[Theses/TICKER - new_name.md]]` |
| `[[TICKER - old_name]]` | `[[TICKER - new_name]]` (folder-less, less common) |
| `[[TICKER - old_name\|alias]]` | `[[TICKER - new_name\|alias]]` |
| `[[TICKER - old_name#section]]` | `[[TICKER - new_name#section]]` |

**Edit-per-file approach**: per file with matches, single `Edit` with `replace_all: true` per pattern. Atomic; bounded failure blast-radius.

**Self-references in renamed thesis**: covered by same rewrite (e.g., template scaffolding wikilinks back to the thesis itself).

**Snapshot body rewrite exception** (§3.3): skip the just-created pre-rename snapshot from Step 3. Identify via `snapshot_trigger: rename` frontmatter + matching HHMMSS. That snapshot IS the pre-rename state — must stay untouched so `/rollback` recovers original content. All OTHER snapshots are eligible for body wikilink rewrites.

**Forward-drift trade-off** (§3.2): rewriting snapshot bodies means snapshots no longer faithfully reproduce vault state at snapshot time. Alternative (not rewriting) re-injects broken wikilinks on rollback. Forward-drift is lesser evil — a snapshot that can't cleanly restore is a dead snapshot.

**Track**: list of files modified (split by live vs snapshot for Step 11 report), total wikilink count, `failed_edits: [list]` for any Edit that errors.

**Failure handling**: Edit fails for a file → do NOT abort loop. Continue with remaining. Append failed path + reason to `failed_edits`. End of Step 5, if `failed_edits` non-empty → write incomplete-rename marker (Step 5.5).

### Step 5.5: Write `.rename_incomplete.TICKER` Marker (if any Edit failed)

If `failed_edits` empty → skip.

If non-empty → write `.rename_incomplete.TICKER` at vault root. Per-ticker filename (§2.1 — multiple in-flight repairs coexist).

```markdown
---
type: rename-incomplete
ticker: TICKER
old_name: [old_name]
new_name: [new_name]
batch: rename-YYYY-MM-DD-HHMMSS
date: YYYY-MM-DD
---

# Incomplete Rename

`/rename TICKER "[new_name]"` completed the move and most wikilink rewrites,
but [N] file(s) failed Edit operations. These files retain stale wikilinks
pointing to the now-missing path `[[Theses/TICKER - [old_name]]]`.

## Failed files

- `Theses/SOMEOTHER - Foo.md` — reason: [Edit error: file lock | permission denied | concurrent modification]
- `_Archive/Snapshots/X.md` — reason: ...

## Recovery

For each failed file, manually replace wikilink patterns from Step 5 of /rename
(7 patterns total) — old name → new name. Or close any process holding the file
open and re-run:

  /rename TICKER "[new_name]"

/rename's repair detection (Step 1.3/1.4 exceptions) will skip the filename
move (already done) and re-attempt wikilink rewrites for still-stale files.
Successful re-attempts remove their entries here; when the failed list is
empty, this marker is auto-deleted.

DO NOT delete this marker manually unless you have verified all failed files
have been repaired — /lint #37 uses it to track repair state.
```

**Append-only on re-runs** (§2.4): if `.rename_incomplete.TICKER` already exists AND `new_name:` matches current run, READ first. Merge new failed_edits into existing list (dedupe by file path), update `batch:` to latest run's batch, rewrite. Don't overwrite — accumulating across repair attempts surfaces persistent problem files.

**Cross-new_name conflict**: handled by Step 1.4.5 guard. Never runs here.

## Step 6: Update Graph Adjacency Entry Header (§4)

Edit `_graph.md`:
- Find: `### TICKER - [old_name]` in `## Thesis Adjacency Index` section.
- Replace with: `### TICKER - [new_name]`.

Missing heading (graph stale) → warn, do not fail: `⚠️ Graph adjacency entry for [TICKER] not found — graph is stale. Run /graph after rename to rebuild.`

Scan `## Cross-Thesis Clusters` table for cells containing old name format. Replace. (Most cluster references use `[[Theses/...]]` wikilinks — Step 5 handled. This catches free-text.)

**Do NOT update `_graph.md` frontmatter `date:` or `last_graph_write:`** (§4.1). Watermark ownership is `/graph`'s. Advancing would silently mask pending changes from next `/graph last`. Next `/graph last` correctly re-extracts this thesis (mtime advanced by rename).

**Graph validation**: re-read `_graph.md`. Verify:
1. YAML frontmatter parses.
2. New heading `### TICKER - [new_name]` exists in adjacency index.
3. Old heading `### TICKER - [old_name]` does not exist anywhere.
4. Adjacency entry count matches `theses:` frontmatter (±2).

Any fail: `⚠️ Graph may be corrupted by rename — [specific failure]. Run /graph to rebuild.`

## Step 7: Update Sector Note

If thesis is `status: active` or `status: monitoring`, sector note (resolved Step 1.5) likely contains thesis in Active Theses.

Read sector note. If contains `[[Theses/TICKER - old_name]]` or `[[TICKER - old_name]]`:
- Already rewritten in Step 5 if grep covered sector note. Verify via re-read.
- If missed (unusual format), apply targeted Edit here.

Skip if `status: draft` (drafts aren't in sector notes per `/thesis` Step 5).

## Step 8: Update Snapshot `snapshot_of:` Fields (§3.4)

For each `_Archive/Snapshots/*.md` with `snapshot_of: "[[Theses/TICKER - [old_name]]]"`:
1. Read frontmatter.
2. Targeted `Edit`: `snapshot_of: "[[Theses/TICKER - [old_name]]]"` → `snapshot_of: "[[Theses/TICKER - [new_name]]]"`.

Preserves `/rollback` functionality. Without this, `/rollback` would read `snapshot_of:`, look for old path, fail to find original (or recreate at old path causing filename split).

**Exception** (§3.3): skip snapshots whose `snapshot_trigger: rename` AND `rename_target:` matches the new path — these are this skill's own snapshots (Step 3); must retain old `snapshot_of:` reference for accurate rollback semantics.

## Step 9: Update _hot.md Free-Text Mentions

Most `_hot.md` references use `[[Theses/...]]` — handled by Step 5. This step catches free-text:
- `Recent Conviction Changes`: bullets may say `**TICKER - old_name**: ...` → replace.
- `Active Research Thread`: narrative prose mentions.
- `Latest Sync` / `Sync Archive`: descriptions.

Use `Edit` with `replace_all: true` for literal `TICKER - [old_name]` (not in wikilink syntax). Word-boundary care — don't match substring inside longer words.

**Word cap**: after edits, check `_hot.md` total. Over 4,000 (soft cap per `_shared/hot-md-contract.md`; unlikely from rename) → prune `## Sync Archive` oldest first. Abort if over 5,000 hard cap.

## Step 10: Append Log Entry to Renamed Thesis

Append to renamed thesis's `## Log`:

```
### YYYY-MM-DD
- Renamed file: "TICKER - [old_name]" → "TICKER - [new_name]". [N] inbound wikilinks rewritten across [M] files. Snapshot: [[_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS)]]
```

Prefix `"Renamed file:"` — `/sync` Step 2.5 skill-origin classification + Step 3e drift exclusion (registry §15).

## Step 11: Report

- **Renamed**: `Theses/TICKER - [old_name].md` → `Theses/TICKER - [new_name].md` | `Repair re-run — mv skipped (already done)`
- **Pre-flight check**: `passed ([N] files reachable)` | `aborted ([M] unreachable — no changes made)`
- **Wikilinks rewritten (live files)**: [count] across [live file paths in Theses/, Sectors/, Macro/, Research/, _hot.md]
- **Wikilinks rewritten (snapshot bodies)**: [count] across [`_Archive/Snapshots/*.md` paths]. Excludes pre-rename snapshot from Step 3.
- **Wikilink update failures** (if any): [list files]. **`.rename_incomplete.TICKER` marker**: `created` | `updated (appended new failures for same new_name)` | `n/a`
- **Repair status** (if marker processed this run):
  - **Resolved this run**: [paths retried successfully and removed from marker]
  - **Still failing**: [paths still in marker]
  - **Marker state**: `cleared (all repairs succeeded — file deleted)` | `retained ([N] files still need repair)`
- **Graph adjacency entry**: header updated | `⚠️ stale graph — entry not found, run /graph`
- **Sector note**: updated as `[sector_name]` (resolution `[exact|normalized|substring]`) | `skipped (draft status)` | `skipped (no matching sector note)`
- **Snapshots updated**: [count] `snapshot_of:` fields adjusted
- **_hot.md**: [count] free-text mentions replaced
- **Pre-rename snapshot**: `[[_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS)]]`
- **Batch ID**: `rename-YYYY-MM-DD-HHMMSS`

**To undo this rename**: run `/rename TICKER "[old_name]"` (symmetric inverse). Pre-rename snapshot also available via `/rollback TICKER` → select `(pre-rename)` snapshot, but rollback alone restores content only; filename revert + inbound wikilink revert require running this skill in reverse.

### Marker auto-cleanup contract

If this run started with `.rename_incomplete.TICKER` (repair re-run), at end of Step 5 check whether all originally-listed failed files were successfully retried. If `failed_edits` empty after retries (every prior failure resolved AND no new failures) → delete marker:
```bash
rm -f ".rename_incomplete.TICKER"
```

Otherwise rewrite marker with still-failing subset (drop resolved, keep unresolved, plus new failures). Monotonic shrink across re-runs until empty, then disappears.

## Edge cases (§8 — all out-of-scope)

- **Rename across ticker change** (`FB - Facebook` → `META - Meta`): TICKER must be stable. Manual workaround: `/thesis META` + copy content + `/status FB active→closed`.
- **Renaming archived theses**: `/rename` operates on active/monitoring/draft in `Theses/`. Manual mv + registry edit for archived.
- **Old name with regex special chars**: glob/grep assume literal string matching. Unusual symbols (parens, braces, `$`) prompt explicit escaping confirmation.
