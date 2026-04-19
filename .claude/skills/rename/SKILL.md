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

## Step 1: Validate

1. **Find the current thesis file** via ticker-prefix glob: `Theses/TICKER - *.md`.
   - Zero matches: stop with `⚠️ No thesis found for [TICKER] in Theses/. Run /thesis [TICKER] to create.`
   - Multiple matches: stop with `⚠️ Multiple Theses/ files match prefix "[TICKER]" — [list]. Resolve filename collision before re-running.`
   - One match: extract `[old_name]` from the filename pattern `Theses/TICKER - [old_name].md`.

2. **Compute the new filename**: `Theses/TICKER - [new_name].md`.

3. **Validate new name**:
   - Must not contain path-illegal characters: `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`.
   - Must not match an existing file at the new path. If collision exists, stop: `⚠️ Target file already exists: Theses/TICKER - [new_name].md. Choose a different name or remove the existing file first.`

4. **Check no-op**: if `[old_name]` == `[new_name]` (case-sensitive after trim), stop: `⚠️ Old and new names match. Nothing to rename.`

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

**Track**: list of files modified (split by live files vs. snapshot files for the Step 11 report), total wikilink count rewritten.

**Failure handling**: If an `Edit` fails for any file (live or snapshot), do NOT abort. Continue with remaining files. At Step 11 report, list all files that failed for manual review. The pre-rename snapshot allows full recovery via `/rollback`.

## Step 6: Update Graph Adjacency Entry Header

Edit `_graph.md`:
- Find heading: `### TICKER - [old_name]` in the `## Thesis Adjacency Index` section.
- Replace with: `### TICKER - [new_name]`.

If the heading is missing (graph stale), warn but do not fail: `⚠️ Graph adjacency entry for [TICKER] not found — graph is stale. Run /graph after rename to rebuild.`

Also scan `## Cross-Thesis Clusters` table for cells containing the old name format. Replace with new name. (Note: most cluster references use `[[Theses/...]]` wikilinks, which Step 5 already handled. This catches any free-text occurrences.)

Update `_graph.md` frontmatter `date:` to today.

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

**Word cap**: After edits, check `_hot.md` total word count. If over 2,000 words (unlikely from rename alone), prune `## Sync Archive` entries (oldest first) until under cap.

## Step 10: Append Log Entry to Renamed Thesis

Append to the renamed thesis's `## Log` section:

```
### YYYY-MM-DD
- Renamed file: "TICKER - [old_name]" → "TICKER - [new_name]". [N] inbound wikilinks rewritten across [M] files. Snapshot: [[_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS)]]
```

## Step 11: Report

- **Renamed**: `Theses/TICKER - [old_name].md` → `Theses/TICKER - [new_name].md`
- **Wikilinks rewritten (live files)**: [count] across [list of live file paths in Theses/, Sectors/, Macro/, Research/, _hot.md]
- **Wikilinks rewritten (snapshot bodies)**: [count] across [list of `_Archive/Snapshots/*.md` paths whose bodies were updated]. Excludes the pre-rename snapshot created in Step 3.
- **Wikilink update failures** (if any): [list files that failed Edit operations — recommend manual review]
- **Graph adjacency entry**: header updated OR `⚠️ stale graph — entry not found, run /graph`
- **Sector note**: updated as `[sector_name]` (resolution `[exact|normalized|substring]`) OR `skipped (draft status)` OR `skipped (no matching sector note)`
- **Snapshots updated**: [count] `snapshot_of:` fields adjusted
- **_hot.md**: [count] free-text mentions replaced
- **Pre-rename snapshot**: `[[_Archive/Snapshots/TICKER - [old_name] (pre-rename YYYY-MM-DD-HHMMSS)]]`
- **Batch ID**: `rename-YYYY-MM-DD-HHMMSS`

**To undo this rename**: run `/rename TICKER "[old_name]"` (symmetric inverse). The pre-rename snapshot is also available via `/rollback TICKER` → select `(pre-rename)` snapshot, but rollback alone restores file content only; the filename revert and inbound wikilink revert require running this skill in reverse.

## Edge cases

- **Rename across ticker change** (e.g., `FB - Facebook` → `META - Meta`): out of scope — TICKER must be stable. For ticker changes, manually create a new thesis with `/thesis META`, copy content, archive the old via `/status FB active→closed`. Future enhancement could add a `/reticker` skill.
- **Renamed thesis already in `_Archive/`** (closed): out of scope — `/rename` operates on active/monitoring/draft theses in `Theses/`. To rename an archived thesis, manually move + adjust.
- **Old name contains regex special characters**: glob and grep must escape correctly. The rename procedure assumes literal string matching; alphanumeric and common punctuation (spaces, hyphens, ampersands) are fine, but unusual symbols (parentheses, braces, dollar signs) should prompt explicit escaping confirmation.
