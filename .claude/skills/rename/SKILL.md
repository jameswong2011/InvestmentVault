---
name: rename
description: Rename a thesis file when company name changes. Atomically updates filename, all inbound wikilinks across the vault, graph adjacency entry header, sector note Active Theses entry, snapshot snapshot_of references, and _hot.md mentions. Use when company changes name (FB → META, Square → Block, etc.), or when correcting a typo in a thesis filename.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * mv * cp * mkdir * find * grep *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Rename a thesis file when the company name portion of the filename changes. The TICKER does NOT change — only the company-name segment after the ` - `. Example: `Theses/META - Meta.md` → `Theses/META - Meta Platforms.md`.

Without `/rename`, manual file renames break: (a) every inbound wikilink across the vault, (b) `_graph.md`'s adjacency entry header, (c) sector note Active Theses entries, (d) `snapshot_of:` fields in `_Archive/Snapshots/` (breaking `/rollback`), (e) `_hot.md` free-text mentions. `/lint #3` would catch broken wikilinks but only after the fact and without auto-fix.

## Arguments

`$ARGUMENTS` should be: `TICKER "New Company Name"`

Examples:
- `/rename META "Meta Platforms"`
- `/rename SHOP "Shopify Inc"`
- `/rename SQ "Block"` (after Square → Block rebrand)

If `$ARGUMENTS` lacks a quoted company name, has no ticker, or has extra arguments, ask the user to clarify before proceeding.

## Step 0: Pre-flight (MANDATORY — runs before any vault inspection)

### 0.1: Acquire vault lock

Acquire a `ticker:TICKER` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 5 minutes. If another skill holds a conflicting lock, abort with the standard collision message (Procedure 1.4). Capture the token emitted at Step 0.1, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block.

### 0.2: Name sanitization (6.1)

Run `.claude/skills/_shared/preflight.md` Procedure 3 (name sanitization) against the proposed `new_name` parsed from `$ARGUMENTS`. The rules:

1. NFC-normalize the input.
2. Trim leading/trailing whitespace. If empty → reject.
3. Length ≤ 100 bytes → reject if exceeded.
4. Character whitelist: `[a-zA-Z0-9 \-_.,'&()]`. Any other character → reject (with specific flag for `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`).
5. No leading dot → reject.
6. First whitespace-token must not be a reserved filesystem name (`CON`, `PRN`, `AUX`, `NUL`, `COM1`–`COM9`, `LPT1`–`LPT9`, case-insensitive) → reject.

On rejection, present the contract's standard rejection message with specific rule violated and a suggested clean variant where possible. Do NOT proceed to Step 1.

Only after Step 0.1 acquires the lock AND Step 0.2 accepts the new_name does the skill proceed to Step 1.

## Step 1: Validate

1. **Find the current thesis file** via ticker-prefix glob: `Theses/TICKER - *.md`.
   - Zero matches: stop with `⚠️ No thesis found for [TICKER] in Theses/. Run /thesis [TICKER] to create.`
   - Multiple matches: stop with `⚠️ Multiple Theses/ files match prefix "[TICKER]" — [list]. Resolve filename collision before re-running.`
   - One match: extract `[old_name]` from the filename pattern `Theses/TICKER - [old_name].md`.

2. **Compute the new filename**: `Theses/TICKER - [new_name].md`.

3. **Validate new name**:
   - Must not contain path-illegal characters: `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`.
   - Must not match an existing file at the new path in `Theses/`. If collision exists, stop: `⚠️ Target file already exists: Theses/TICKER - [new_name].md. Choose a different name or remove the existing file first.`
     - **Exception — incomplete-rename repair**: If `.rename_incomplete.TICKER` exists at vault root AND its frontmatter `new_name:` equals the proposed new name, this is a repair re-run for the same in-flight rename. The filename move from a prior failed run already produced `Theses/TICKER - [new_name].md`; the collision is expected. Skip the abort, log `ℹ️ Repair re-run detected — .rename_incomplete.TICKER exists for [TICKER] → [new_name]. Skipping mv (already done), proceeding to retry failed wikilink rewrites from Step 5.`, then jump from Step 1 directly to Step 5 (skipping Steps 2 confirmation, 3 snapshot, 3.5 pre-flight, 4 mv, since those already ran in the prior attempt).
   - **Archive collision check**: Glob `_Archive/TICKER - [new_name].md` (non-recursive — ignore `_Archive/Snapshots/`). If a file matches, warn and require explicit confirmation before proceeding: `⚠️ Archive collision: _Archive/TICKER - [new_name].md already exists from a prior closure of this ticker. If you later close the renamed thesis, /status Step 7.5 would mv the new thesis to the same archive path and silently overwrite the old archive copy. Options:` followed by three explicit user choices — (a) Proceed anyway (accept future overwrite risk), (b) Rename the old archive first (e.g., `mv "_Archive/TICKER - [new_name].md" "_Archive/TICKER - [new_name] (closed YYYY-MM-DD).md"` before re-running `/rename`), (c) Cancel. Wait for user selection. Do NOT proceed silently.

4. **Check no-op**: if `[old_name]` == `[new_name]` (case-sensitive after trim), stop: `⚠️ Old and new names match. Nothing to rename.`
   - **Exception — incomplete-rename repair**: same logic as Step 1.3 — if `.rename_incomplete.TICKER` exists with `new_name:` matching the proposed new name and the prior run's repair targets are still unresolved, the no-op check is bypassed. The skill enters Step 5 to retry the wikilink rewrites for the still-stale files listed in the marker.

### Step 1.4.5: Incomplete-rename cross-name guard (NEW — runs after the no-op check)

If `.rename_incomplete.TICKER` exists at vault root, read its frontmatter and compare `new_name:` to the proposed new name from `$ARGUMENTS`:

- **`marker.new_name == proposed_new_name`** → repair re-run (already handled by exceptions in Steps 1.3 and 1.4 above). Proceed to Step 5 directly.
- **`marker.new_name != proposed_new_name`** → STOP with explicit guard. The marker tracks an in-flight rename to a DIFFERENT name; proceeding would corrupt the marker's repair-target context (failed_files were collected against `marker.new_name`, but proceeding would rename to `proposed_new_name`, leaving those failed wikilinks pointing to a name that no longer matches anything).

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
         (1) READ the marker's "Failed files" list — print it to the user with
             explicit warning text:
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
         (2) Wait for explicit user confirmation that they have manually
             remediated the listed files OR explicitly accept the broken-wikilink
             outcome.
         (3) Only then rm ".rename_incomplete.TICKER" and re-run /rename with
             the new name.
   ```

   Do NOT proceed silently. Wait for user to take action externally and re-invoke `/rename`.

5. **Survey inbound references** (read-only — for the confirmation prompt):
   - Grep vault (excluding `.git/` and `_Inbox/processed/` only) for the patterns in Step 5 below. `_Archive/Snapshots/` IS included in the survey because Step 5 rewrites snapshot bodies. Count live-file matches and snapshot-body matches separately so the user can see both counts in the confirmation.
   - Grep `_Archive/Snapshots/` frontmatter for `snapshot_of:` referencing the old path. Count. (This is a separate count from snapshot body matches — `snapshot_of:` is frontmatter metadata, handled by Step 8.)
   - Read `_graph.md`, locate the adjacency entry header `### TICKER - [old_name]`. Note presence.
   - Resolve sector note via canonical procedure **`.claude/skills/_shared/sector-resolution.md`**. If matched, scan its Active Theses section for the old wikilink. Note presence.
   - Read `_hot.md`, count free-text mentions of `TICKER - [old_name]` (outside wikilink syntax — wikilinks are handled in Step 5).

## Step 2: Confirm (Tier 3 — Mandatory)

Present the proposed rename and the survey from Step 1.5. **Wait for explicit user confirmation.**

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

Create a snapshot of the current thesis (in case rename needs reversal):

```bash
mkdir -p _Archive/Snapshots
HHMMSS=$(date +%H%M%S)
cp "Theses/TICKER - [old_name].md" "_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS).md"
```

Read the newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - [old_name]]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: rename
snapshot_batch: rename-YYYY-MM-DD-HHMMSS
rename_target: "[[Theses/TICKER - [new_name]]]"
```

> **Batch ID note**: Uses HHMMSS (6 digits) to prevent same-minute collisions. If a future `/rollback` cascade matches this batch, the `rename_target:` field tells it the cascade is reversing a rename — `/rollback` should additionally restore the old filename via `mv` (out of scope for current `/rollback`; user must manually move).

## Step 3.5: Pre-flight Read/Write Check (NEW — abort BEFORE mv if any file is unreachable)

The Step 5 wikilink rewrite touches every file in the inbound-reference set surveyed by Step 1.5. If any of those files is unreadable or unwritable, the rewrite will fail mid-stream — but by that point `mv` has already happened, so the rename is committed and partial wikilinks are unavoidable. Catch this BEFORE the mv.

For each file in the inbound-reference set (live files in `Theses/`, `Sectors/`, `Macro/`, `Research/`, `_hot.md`, plus `_Archive/Snapshots/*.md` with body matches and `snapshot_of:` matches):

1. **Read check**: attempt to read the file's first 10 bytes (or use the existing `Read` tool). If the read fails (file deleted between Step 1.5 survey and now, permission error, file lock), record the file path in `unreachable_files: [list]`.
2. **Write probe**: confirm the file is writable. On macOS/Linux, the simplest probe is `[ -w "path" ]`:
   ```bash
   [ -w "Theses/TICKER - Name.md" ] || echo "NOT_WRITABLE: Theses/TICKER - Name.md"
   ```
   Capture any `NOT_WRITABLE` output into `unreachable_files`.

**If `unreachable_files` is non-empty**: stop. The vault is in its original state — `mv` has not run, no wikilinks modified, no graph edits. Report:
```
❌ Pre-flight check failed: [N] file(s) cannot be edited. Rename aborted — vault unchanged.

Unreachable files:
  - [path 1] (reason: [permission denied | file locked | not found])
  - [path 2] (reason: ...)

Resolve the access issue (close the file in another editor, fix permissions, restore deleted file)
and re-run /rename. Pre-rename snapshot retained: [[_Archive/Snapshots/...]].
```

**Why pre-flight matters**: Without this check, the original Step 4 mv could succeed and Step 5 could leave 47 of 50 files updated and 3 with stale wikilinks pointing to a non-existent file. Backups can restore "all-old" or "all-new" state but cannot synthesize "47 fixed + 3 fixed." Pre-flight reduces post-mv failure surface to genuinely transient issues (concurrent edit, race conditions) — those rare cases are handled by Step 5's incomplete-rename marker.

## Step 4: Move the File

```bash
mv "Theses/TICKER - [old_name].md" "Theses/TICKER - [new_name].md"
```

**Verification**: confirm new path exists and old doesn't:
```bash
ls "Theses/TICKER - [new_name].md"
ls "Theses/TICKER - [old_name].md" 2>/dev/null  # should produce no output
```

**If `mv` fails**: stop. Snapshot exists; vault is in original state (no destructive changes yet — wikilinks not modified). Report: `❌ Rename failed at mv step — vault unchanged. Snapshot retained: [[_Archive/Snapshots/...]]. Investigate filesystem permissions.`

## Step 5: Update Inbound Wikilinks Across Vault (including snapshot bodies)

Process each wikilink pattern. For each, grep the vault (excluding `.git/` and `_Inbox/processed/`), then `Edit` each file to replace. **Crucially, `_Archive/Snapshots/` is NOT excluded** — snapshot bodies frequently contain wikilinks to other theses (e.g., `[[Theses/META - Meta]]` embedded in a pre-sync snapshot of a different thesis). Leaving these stale causes rollback-induced wikilink breakage: rolling back that snapshot re-introduces the old thesis name into a live file, producing broken wikilinks that `/lint` #3 then flags.

| Pattern | Replacement |
|---|---|
| `[[Theses/TICKER - old_name]]` | `[[Theses/TICKER - new_name]]` |
| `[[Theses/TICKER - old_name\|alias]]` | `[[Theses/TICKER - new_name\|alias]]` (preserve alias text) |
| `[[Theses/TICKER - old_name#section]]` | `[[Theses/TICKER - new_name#section]]` (preserve section anchor) |
| `[[Theses/TICKER - old_name.md]]` | `[[Theses/TICKER - new_name.md]]` |
| `[[TICKER - old_name]]` | `[[TICKER - new_name]]` (folder-less form, less common) |
| `[[TICKER - old_name\|alias]]` | `[[TICKER - new_name\|alias]]` |
| `[[TICKER - old_name#section]]` | `[[TICKER - new_name#section]]` |

**Edit-per-file approach**: For each file with matches, use a single `Edit` with `replace_all: true` per pattern. Keeps each edit atomic and the failure blast-radius bounded.

**Self-references in the renamed thesis itself**: the renamed thesis may contain wikilinks back to itself (e.g., template scaffolding). These also get rewritten in this step.

**Snapshot body rewrite — one exception**: Skip the just-created pre-rename snapshot from Step 3 (identify it by matching both the `snapshot_trigger: rename` frontmatter AND a `snapshot_batch` or filename that contains the current rename's HHMMSS stamp). That snapshot's body IS the pre-rename thesis state and must stay untouched so `/rollback` can recover the original content. All OTHER snapshots in `_Archive/Snapshots/` — whether or not they reference the renamed thesis — are eligible for body wikilink rewrites and should be processed normally. In practice, unrelated snapshots won't contain the renamed thesis's wikilinks so the grep will skip them; snapshots that DO reference the renamed thesis are exactly the ones that need updating.

**Trade-off acknowledged**: rewriting snapshot bodies means the snapshot no longer faithfully reproduces the vault state at snapshot time (wikilink text has drifted forward). The alternative — not rewriting — re-injects broken wikilinks on rollback. The forward-drift is the lesser evil because `/rollback` is the scenario that matters; a snapshot that can't cleanly restore is a dead snapshot.

**Track**: list of files modified (split by live files vs. snapshot files for the Step 11 report), total wikilink count rewritten, **and a separate `failed_edits: [list]` accumulator for any Edit that errors during this step**.

**Failure handling**: If an `Edit` fails for any file (live or snapshot), do NOT abort the loop — continue with remaining files so the rename completes as much work as possible. Append the failed file path + reason to `failed_edits`. At the end of Step 5, if `failed_edits` is non-empty, write the **incomplete-rename marker** below.

### Step 5.5: Write `.rename_incomplete.TICKER` Marker (only if any Edit failed)

If `failed_edits` is empty, skip this sub-step.

If `failed_edits` is non-empty, write `.rename_incomplete.TICKER` at vault root with the rename context, so `/lint` check #37 can surface this state and the user can repair without re-deriving what failed.

> **Per-ticker filename**: the marker filename includes the TICKER suffix so multiple in-flight repairs (across different tickers) coexist as separate marker files. Each `/rename` operation only reads/writes the marker for its own ticker. This eliminates cross-ticker corruption that a single shared marker would cause.

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

For each failed file, manually replace the wikilink patterns from Step 5
of `/rename` (7 patterns total) — old name → new name. Or close any process
holding the file open and re-run:

  /rename TICKER "[new_name]"

`/rename`'s no-op detection (Step 1.4) will skip the filename move (already
done) and re-attempt the wikilink rewrites for the still-stale files.
Successful re-attempts remove their entries here; when the failed list is
empty, this marker is auto-deleted.

DO NOT delete this marker manually unless you have verified all failed
files have been repaired — `/lint` #37 uses it to track repair state.
```

**Append-only on re-runs (same-ticker, same-new_name only)**: If `.rename_incomplete.TICKER` already exists AND its `new_name:` matches the current run's new_name, READ it first. Merge the new failed_edits into the existing list (dedupe by file path), update the `batch:` field to the latest run's batch, and rewrite the file. Don't overwrite — accumulating across multiple repair attempts surfaces persistent problem files.

**Cross-new_name conflict prevention**: if `.rename_incomplete.TICKER` exists with a different `new_name:`, Step 1.4.5 has already aborted the run with the in-flight conflict guard. This sub-step never runs in that scenario.

**Lifecycle**: deleted automatically when a subsequent `/rename` run completes with all wikilink rewrites succeeding (i.e., new `failed_edits` is empty AND prior `.rename_incomplete.TICKER`'s file list now resolves cleanly via re-attempted Edits). Until deletion, `/lint` #37 surfaces the marker as an Important issue. Do NOT include the failed list in the regular Step 11 report's success counts — they are tracked separately.

## Step 6: Update Graph Adjacency Entry Header

Edit `_graph.md`:
- Find heading: `### TICKER - [old_name]` in the `## Thesis Adjacency Index` section.
- Replace with: `### TICKER - [new_name]`.

If the heading is missing (graph stale), warn but do not fail: `⚠️ Graph adjacency entry for [TICKER] not found — graph is stale. Run /graph after rename to rebuild.`

Also scan `## Cross-Thesis Clusters` table for cells containing the old name format. Replace with new name. (Note: most cluster references use `[[Theses/...]]` wikilinks, which Step 5 already handled. This catches any free-text occurrences.)

**Do NOT update `_graph.md` frontmatter `date:`.** The `date:` field is the watermark `/graph last` uses to detect changed files via `find -newermt "[date]"`. Advancing it here would silently mask any thesis modified before today but not yet captured by `/graph last` — those files would be excluded from the next `/graph last` change-detection set, leaving stale adjacency entries undetected. Watermark ownership belongs exclusively to `/graph`; `/rename` updates content of `_graph.md` (the adjacency entry header) but must not advance the watermark. The next `/graph last` will correctly re-extract this thesis (mtime advanced by the rename) plus any other pending changes.

**Graph validation**: After edits, re-read `_graph.md` and verify:
1. YAML frontmatter parses without error.
2. The new heading `### TICKER - [new_name]` exists in the adjacency index.
3. The old heading `### TICKER - [old_name]` does not exist anywhere.
4. Adjacency entry count matches `theses:` frontmatter (±2).

If any check fails: `⚠️ Graph may be corrupted by rename — [specific failure]. Run /graph to rebuild.`

## Step 7: Update Sector Note

If the thesis is `status: active` or `status: monitoring`, the sector note (resolved in Step 1.5) likely contains the thesis in its Active Theses section.

Read the sector note. If it contains `[[Theses/TICKER - old_name]]` or `[[TICKER - old_name]]`:
- These were already rewritten in Step 5 if grep covered the sector note. Verify via re-read.
- If for any reason the wikilink wasn't caught (e.g., unusual format), apply targeted Edit here.

Skip if `status: draft` (draft theses aren't in sector notes per `/thesis` Step 5).

## Step 8: Update Snapshot `snapshot_of:` Fields

For each `_Archive/Snapshots/*.md` whose frontmatter contains `snapshot_of: "[[Theses/TICKER - [old_name]]]"`:
1. Read the snapshot's frontmatter.
2. Apply targeted `Edit`: replace `snapshot_of: "[[Theses/TICKER - [old_name]]]"` with `snapshot_of: "[[Theses/TICKER - [new_name]]]"`.

This preserves `/rollback` functionality. Without it, `/rollback` would read the snapshot's `snapshot_of:` field, look for the old path, and fail to find the original (or worse, recreate at the old path causing filename split).

**Exception**: Skip snapshots whose `snapshot_trigger:` is `rename` and `rename_target:` matches the new path — these are this skill's own snapshots (Step 3) and should retain the old `snapshot_of:` reference for accurate rollback semantics (the snapshot captures the file BEFORE the rename, so `snapshot_of:` correctly references the pre-rename path).

## Step 9: Update _hot.md Free-Text Mentions

Most `_hot.md` references use `[[Theses/...]]` wikilinks — already handled in Step 5. This step catches free-text mentions like:

- `Recent Conviction Changes`: bullets may say `**TICKER - old_name**: ...` → replace.
- `Active Research Thread`: prose may mention the old name in narrative form.
- `Latest Sync` / `Sync Archive`: descriptions may include the old name.

Use `Edit` with `replace_all: true` for any literal occurrence of `TICKER - [old_name]` (not in wikilink syntax). Apply word-boundary care — don't accidentally match `TICKER - old_name` substring inside a longer word.

**Word cap**: After edits, follow the compression trigger order in `.claude/skills/_shared/hot-md-contract.md` §"Compression trigger order". Soft cap 4,000 words, hard cap 5,000 words (hard-cap breach unlikely from rename alone). `/rename` primary operation always succeeds regardless of `_hot.md` state.

## Step 10: Append Log Entry to Renamed Thesis

Append to the renamed thesis's `## Log` section:

```
### YYYY-MM-DD
- Renamed file: "TICKER - [old_name]" → "TICKER - [new_name]". [N] inbound wikilinks rewritten across [M] files. Snapshot: [[_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS)]]
```

## Step 11: Report

- **Renamed**: `Theses/TICKER - [old_name].md` → `Theses/TICKER - [new_name].md` (or `Repair re-run — mv skipped (already done)` if entered via incomplete-rename marker)
- **Pre-flight check**: `passed ([N] files reachable)` or `aborted ([M] unreachable — no changes made)`
- **Wikilinks rewritten (live files)**: [count] across [list of live file paths in Theses/, Sectors/, Macro/, Research/, _hot.md]
- **Wikilinks rewritten (snapshot bodies)**: [count] across [list of `_Archive/Snapshots/*.md` paths whose bodies were updated]. Excludes the pre-rename snapshot created in Step 3.
- **Wikilink update failures** (if any): [list files that failed Edit operations]. **`.rename_incomplete.TICKER` marker**: `created` | `updated (appended new failures to existing marker for same new_name)` | `n/a (no failures)`
- **Repair status** (if `.rename_incomplete.TICKER` was processed in this run):
  - **Resolved this run**: [list paths that were retried successfully and removed from the marker]
  - **Still failing**: [list paths still in the marker — manual fix or next re-run]
  - **Marker state**: `cleared (all repairs succeeded — file deleted)` | `retained ([N] files still need repair)`
- **Graph adjacency entry**: header updated OR `⚠️ stale graph — entry not found, run /graph`
- **Sector note**: updated as `[sector_name]` (resolution `[exact|normalized|substring]`) OR `skipped (draft status)` OR `skipped (no matching sector note)`
- **Snapshots updated**: [count] `snapshot_of:` fields adjusted
- **_hot.md**: [count] free-text mentions replaced
- **Pre-rename snapshot**: `[[_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS)]]`
- **Batch ID**: `rename-YYYY-MM-DD-HHMMSS`

**To undo this rename**: run `/rename TICKER "[old_name]"` (symmetric inverse). The pre-rename snapshot is also available via `/rollback TICKER` → select `(pre-rename)` snapshot, but rollback alone restores file content only; the filename revert and inbound wikilink revert require running this skill in reverse.

### Marker auto-cleanup contract

If this run started with `.rename_incomplete.TICKER` present (repair re-run), at the end of Step 5 check whether all originally-listed failed files were successfully retried this run. If `failed_edits` after this run's retries is empty (every prior failure resolved AND no new failures), delete the marker:
```bash
rm -f ".rename_incomplete.TICKER"
```
Otherwise, rewrite the marker with the still-failing subset (drop resolved entries, keep unresolved, plus any new failures from this run). The marker thus shrinks monotonically across repair re-runs until empty, then disappears.

> **Per-ticker scope**: this skill only touches `.rename_incomplete.TICKER` for the current run's TICKER. Markers for other tickers (e.g., `.rename_incomplete.META` while running `/rename SHOP`) are untouched. `/lint` #37 globs `.rename_incomplete.*` to surface every in-flight repair independently.

## Edge cases

- **Rename across ticker change** (e.g., `FB - Facebook` → `META - Meta`): out of scope — TICKER must be stable. For ticker changes, manually create a new thesis with `/thesis META`, copy content, archive the old via `/status FB active→closed`. Future enhancement could add a `/reticker` skill.
- **Renamed thesis already in `_Archive/`** (closed): out of scope — `/rename` operates on active/monitoring/draft theses in `Theses/`. To rename an archived thesis, manually move + adjust.
- **Old name contains regex special characters**: glob and grep must escape correctly. The rename procedure assumes literal string matching; alphanumeric and common punctuation (spaces, hyphens, ampersands) are fine, but unusual symbols (parentheses, braces, dollar signs) should prompt explicit escaping confirmation.

## Step 12: Release lock

After Step 11's report is complete, release the ticker lock per `.claude/skills/_shared/preflight.md` §1.7 as the skill's FINAL Bash block. Runs unconditionally — whether the rename completed cleanly, left a `.rename_incomplete.TICKER` marker (partial-failure path), or aborted at Step 0.2/0.3 (marker collision, name sanitization rejection).

```bash
# Lock release — verify ownership before rm (preflight §1.5)
LOCK_FILE=".vault-lock.TICKER"                   # TICKER from $ARGUMENTS, e.g., .vault-lock.META
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ($LOCK_FILE) ==="
else
  echo "⚠️ Lock ownership check failed at release ($LOCK_FILE) — skipping rm to avoid stealing another skill's lock."
fi
```
