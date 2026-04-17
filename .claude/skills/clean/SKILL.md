---
name: clean
description: Delete old snapshots from _Archive/Snapshots/. Accepts a day threshold (default 180). Use when user says "clean", "clean snapshots", "delete old snapshots", or when /lint flags stale snapshots.
model: sonnet
effort: max
allowed-tools: Read Grep Glob Bash(find * rm * date * wc * ls *)
---

Delete snapshots older than a given threshold from `_Archive/Snapshots/`.

## Arguments

`$ARGUMENTS` should be a number of days (e.g., `90`). Default: **180** if no argument provided.

## Step 1: Inventory Snapshots

List all files in `_Archive/Snapshots/`:
```bash
find _Archive/Snapshots/ -name '*.md' -type f | sort
```

If no files found, report "No snapshots exist — nothing to clean." and stop.

## Step 2: Parse Ages and Safety Net Check

For each snapshot, read only its frontmatter and extract `snapshot_date:` and `snapshot_of:`. Calculate age in days from today's date.

Classify each snapshot:
- **Retained**: age <= threshold (kept)
- **Expired**: age > threshold — but check safety net status before marking for deletion (see below)

### Safety Net Check (expired snapshots only)

For each snapshot classified as Expired:
1. Extract `snapshot_of:` to identify the source file path
2. Check if the source file still exists at its original path
3. If source exists: check whether it was modified after `snapshot_date:` (compare file mtime against snapshot_date)
   - Modified after snapshot → reclassify as **🛡️ Active safety net** — this snapshot captures a pre-modification state that cannot be recovered otherwise. Exclude from deletion.
   - Not modified after snapshot → keep as **Expired** — snapshot is redundant (source unchanged since snapshot was taken)
4. If source file no longer exists (archived/deleted) → keep as **Expired** (orphan record with no live file to protect)

## Step 3: Report Before Deletion

Present a summary table. **Do NOT delete anything yet.**

### Snapshots to delete (older than N days)
| File | Snapshot Date | Age (days) | Source Note |
|------|--------------|------------|------------|
| `filename.md` | YYYY-MM-DD | X | `snapshot_of` value |

### 🛡️ Active safety nets (excluded from deletion)
| File | Snapshot Date | Age (days) | Source Note | Source Modified |
|------|--------------|------------|------------|----------------|
| `filename.md` | YYYY-MM-DD | X | `snapshot_of` value | YYYY-MM-DD |

These snapshots exceed the age threshold but their source files were modified after the snapshot was taken. Deleting them removes the only recovery path to the pre-modification state. To override, re-run `/clean` targeting specific filenames.

### Snapshots retained (within threshold)
| File | Snapshot Date | Age (days) |
|------|--------------|------------|

**Total**: X to delete, Y active safety nets (protected), Z retained.

## Step 4: Confirm and Execute

**Wait for user confirmation before deleting.**

If confirmed, delete each expired snapshot:
```bash
rm "_Archive/Snapshots/[filename]"
```

Report: "Deleted X snapshots. Y remain."
