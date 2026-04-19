---
name: clean
description: Delete old snapshots from _Archive/Snapshots/. Accepts a day threshold (default 180). Use when user says "clean", "clean snapshots", "delete old snapshots", or when /lint flags stale snapshots.
model: sonnet
effort: max
allowed-tools: Read Grep Glob Bash(find * rm * date * wc * ls *)
---

Delete snapshots older than a given threshold from `_Archive/Snapshots/`.

## Arguments (6.9 — orphan handling)

`$ARGUMENTS` patterns:
- **Number of days** (e.g., `90`, `30`): age-based cleanup. Default: **180** if no argument provided. Orphan snapshots (source file missing) are **PROTECTED by default** — reported but not deleted. See Step 2c.
- **`orphans`** (literal word): delete only orphan snapshots, regardless of age. Skips age-based cleanup entirely.
- **Number of days + `--include-orphans`** (e.g., `180 --include-orphans`): standard age-based cleanup PLUS delete orphans. Explicit opt-in.

Parse patterns in this order:
```
if $ARGUMENTS == "orphans" → orphans-only mode
elif $ARGUMENTS ends with "--include-orphans" → age + orphans mode; strip flag to get days
elif $ARGUMENTS is integer → age-only mode (default orphans PROTECTED)
else → default age-only mode (180 days; orphans PROTECTED)
```

## Step 0: Pre-flight

Acquire a `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 5 minutes. Release via `trap` on exit.

## Step 1: Inventory Snapshots

List all files in `_Archive/Snapshots/`:
```bash
find _Archive/Snapshots/ -name '*.md' -type f | sort
```

If no files found, report "No snapshots exist — nothing to clean." and stop.

## Step 2: Parse Ages and Safety Net Check

For each file in `_Archive/Snapshots/`, read only its frontmatter and extract `type:`, `snapshot_date:`, and `snapshot_of:`. Classify:

### 2a: Non-snapshot artifact guard (must run first)

Some files in `_Archive/Snapshots/` are NOT snapshots — they are operational artifacts that other skills store there to survive across sessions:

- **`_prune-manifest`** files — written by `/prune` Stage 1.5 as a crash-recovery breadcrumb. Frontmatter has `type: prune-manifest` and carries no `snapshot_date:`. While a prune is in progress (or the prune crashed mid-run), this file is the user's only pointer to the batch that needs cascade-rollback.
- **`_sync-manifest`** files — written by `/sync` Step 7.5 as a sidecar listing every thesis touched by a sync run (Tier A snapshots + Tier B Log appends). Frontmatter has `type: sync-manifest` and carries no `snapshot_date:` (it carries `date:` instead). Consumed by `/rollback` Step 2.5b cascade detection. Aged by `/lint #41`.
- **Future artifact types** — any file whose `type:` frontmatter is set to anything other than a snapshot flavor.

Detection rule: if the file's frontmatter has a `type:` field AND that value is not empty AND is not a snapshot-producer identifier (`snapshot`, or absent), treat the file as a non-snapshot artifact. Also treat any file missing `snapshot_date:` as non-snapshot (defensive — `/clean` cannot date-age what isn't dated).

Handling:
- **Skip the file entirely.** Do not classify as retained/expired. Do not offer for deletion under any threshold.
- **For `type: prune-manifest` with `status: in-progress`**: add a line to the Step 3 report under a new category `🛑 Prune manifest (in-progress)` — the user should resolve the in-flight prune (via `/rollback` cascade) before letting `/clean` proceed, though `/clean` itself takes no action on this file.
- **For `type: prune-manifest` with `status: completed`**: add a line to the Step 3 report under `🧹 Completed prune manifest — safe to delete manually` — the prune finished but the manifest wasn't cleaned up at Stage 5. `/clean` still doesn't auto-delete (scope is snapshots), but the user can `rm` it.
- **For any other non-snapshot type**: log `ℹ️ Skipped non-snapshot artifact: [path] (type: [value], no snapshot_date)`.

### 2b: Classify actual snapshots

For each file that passed the 2a guard (has `snapshot_date:`, no conflicting `type:`), calculate age in days from today's date.

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
4. If source file no longer exists (archived/deleted) → reclassify as **👻 Orphan** (6.9 fix). Handling depends on mode:
   - **Default age mode** (no `orphans` keyword, no `--include-orphans`): PROTECT — do NOT delete. List in Step 3 report under "Orphan snapshots (source file missing)" so the user can review. The snapshot may be the only recovery path if the source file was mistakenly deleted. **This is a deliberate fail-safe reversal from the legacy behavior where orphans were treated as "Expired" alongside stale-but-redundant snapshots.**
   - **`orphans` mode**: mark for deletion. This is the explicit opt-in.
   - **`--include-orphans` mode**: mark for deletion as part of age-based batch.

### 2c: Orphan enumeration (6.9 — explicit pass)

Orphans are identified by `snapshot_of:` pointing to a path that does NOT exist. Resolve the path:
- Wikilink form `"[[Theses/TICKER - Name]]"` → check `Theses/TICKER - Name.md`
- Wikilink form `"[[_Archive/TICKER - Name]]"` → check `_Archive/TICKER - Name.md`
- Plain path form `"Theses/TICKER - Name.md"` → check as-is

If the resolved path does not exist, the snapshot is an orphan.

**Why default-protect orphans**: the legacy "delete orphans as part of expired batch" behavior created an unrecoverable loss path for scenarios where a thesis was deleted manually (violating CLAUDE.md "archive don't delete") — the snapshots were the user's only lingering audit trail, and `/clean` silently erased them along with genuinely-stale redundant snapshots. Default-protect surfaces orphans for review; the user can explicitly opt in via `orphans` or `--include-orphans` once they've inspected the reported list.

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

### 🛑 Prune manifest (in-progress) — do NOT clean
| File | Batch ID | Status |
|------|---------|--------|

These represent in-flight `/prune` operations. Resolve the batch first (`/rollback` cascade via any ticker in the batch, then delete the manifest) before running `/clean` again.

### 🧹 Completed prune manifests — safe to delete manually
| File | Batch ID | Completed Date |
|------|---------|---------------|

These are stale breadcrumbs from successful prune runs whose Stage 5 cleanup failed. `/clean` does not auto-delete them (they are not snapshots); user can `rm` manually after confirming the batch succeeded.

### 👻 Orphan snapshots (source file missing)
| File | Snapshot Date | Age (days) | `snapshot_of` (missing) |
|------|--------------|------------|--------------------------|

These snapshots reference source files that no longer exist in the vault. Possible causes: (a) source was manually deleted (violates CLAUDE.md archive-don't-delete rule — investigate), (b) source was archived and the archive was later renamed (snapshots track original path), (c) legacy snapshot from a pre-6.9 vault where the convention drifted.

- **Default age mode**: orphans are PROTECTED and listed here only. Not deleted.
- **To delete orphans**: run `/clean orphans` (orphans only, any age) or `/clean [days] --include-orphans` (age + orphans).

### Non-snapshot artifacts (skipped)
| File | Type |
|------|------|

**Total**: X to delete, Y active safety nets (protected), Z retained, V orphans (protected by default | slated for deletion), W non-snapshot artifacts (skipped).

## Step 4: Confirm and Execute

**Wait for user confirmation before deleting.**

If confirmed, delete each expired snapshot:
```bash
rm "_Archive/Snapshots/[filename]"
```

Report: "Deleted X snapshots. Y remain."
