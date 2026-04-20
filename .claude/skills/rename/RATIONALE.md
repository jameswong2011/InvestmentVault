---
type: skill-rationale
skill: /rename
purpose: Design rationale for /rename — atomicity, pre-flight probe, snapshot body rewrite trade-off, per-ticker repair markers. NOT loaded at invocation.
last_reviewed: 2026-04-20
---

# /rename Design Rationale

> SKILL.md contains operational rules. This file explains the pre-flight probe, cross-name guard, snapshot-body-rewrite trade-off, per-ticker marker design, and watermark-preservation contract.

---

## §1 Pre-flight Read/Write probe (Step 3.5)

### §1.1 Why pre-flight matters

Step 5 wikilink rewrite touches every file in the inbound-reference set. If any file is unreadable/unwritable, rewrite fails mid-stream — but by then `mv` already ran, so the rename is committed and partial wikilinks are unavoidable. The pre-flight catches this BEFORE the mv.

Without pre-flight: Step 4 mv succeeds → Step 5 leaves 47 of 50 files updated and 3 with stale wikilinks pointing to non-existent file. Backups can restore "all-old" or "all-new" state but cannot synthesize "47 fixed + 3 fixed."

Pre-flight reduces post-mv failure surface to genuinely transient issues (concurrent edit, race conditions) — those rare cases handled by Step 5's incomplete-rename marker.

### §1.2 Why both Read + Write probes

`Read` check alone misses permission mismatches (file readable but not writable). `Write` probe alone misses file-not-found. Both together cover all pre-mv access failure modes.

Single-file Bash `[ -w "path" ]` is cheap — costs ~1ms per file. Running it for 50 files still completes in <100ms total.

---

## §2 Incomplete-rename repair semantics

### §2.1 Why per-ticker marker filenames

Single shared `.rename_incomplete` marker would cause cross-ticker corruption: running `/rename META` while `/rename SHOP`'s repair is in flight would overwrite SHOP's failed-file list. Each ticker's marker (`.rename_incomplete.TICKER`) is independent.

`/lint #37` globs `.rename_incomplete.*` to surface every in-flight repair.

### §2.2 Repair re-run detection (Steps 1.3, 1.4 exceptions)

If `.rename_incomplete.TICKER` exists AND its `new_name:` matches the proposed new_name, the current run is a repair re-run:
- Filename move already ran successfully in the prior attempt — `Theses/TICKER - [new_name].md` exists (would normally be a collision abort)
- No-op check would fire (`old_name` and `new_name` differ only because the file already has the new name)

Both checks bypass the abort in this exception. The skill jumps from Step 1 directly to Step 5, retrying only the failed wikilink rewrites.

### §2.3 Cross-name guard (Step 1.4.5) — why stop

If `.rename_incomplete.TICKER` exists with `new_name:` DIFFERENT from the proposed new_name, proceeding would corrupt the marker's repair-target context:
- Failed wikilinks were collected expecting `old_name → marker.new_name` rewrite
- Proceeding with `proposed_new_name` would orphan those repair targets (wikilinks still reference obsolete `old_name`, never `marker.new_name` or `proposed_new_name`)

Hard-stop with three user options:
- **(a) Finish prior rename first**: `/rename TICKER "[marker.new_name]"` — retries the pending work; marker auto-deletes on success.
- **(b) Manually resolve listed files + rm marker**: user takes over the repair manually.
- **(c) Accept loss of repair state**: explicit acknowledgment of orphan wikilinks. Includes safety step: READ the marker's failed-files list, warn user that re-running Step 5 against those files won't fix them (grep targets current filename, not truly-original name), require manual grep-replace BEFORE `rm`-ing marker.

### §2.4 Why monotonic-shrink marker

Re-runs append new failures to existing marker, dedupe by file path, update `batch:` to latest run. Marker shrinks across attempts until empty, then auto-deletes. Persistent problem files (file always locked, permission issue that won't resolve) accumulate visibility through repeat appearance; transient failures clear on next attempt.

---

## §3 Snapshot body wikilink rewrite

### §3.1 Why rewrite snapshot bodies

Snapshot bodies frequently contain wikilinks to other theses (e.g., `[[Theses/META - Meta]]` embedded in a pre-sync snapshot of a different thesis). Leaving these stale causes rollback-induced wikilink breakage: rolling back that snapshot re-introduces the OLD thesis name into a live file, producing broken wikilinks that `/lint #3` then flags.

Step 5 rewrite touches `_Archive/Snapshots/` bodies to prevent this.

### §3.2 The forward-drift trade-off

Rewriting snapshot bodies means the snapshot no longer faithfully reproduces vault state at snapshot time — wikilink text has drifted forward to current names. Alternative (not rewriting) re-injects broken wikilinks on rollback.

Forward-drift is the lesser evil because `/rollback` is the scenario that matters; a snapshot that can't cleanly restore is a dead snapshot. Preserving "snapshot time fidelity" for wikilink TEXT while breaking LINK RESOLUTION on rollback defeats the point of having a snapshot.

### §3.3 Own-snapshot exception

Skip rewriting the just-created pre-rename snapshot from Step 3. Identify via `snapshot_trigger: rename` + matching HHMMSS. That snapshot's body IS the pre-rename thesis state — must stay untouched so `/rollback` can recover original content.

Also skip own-snapshot's `snapshot_of:` field update in Step 8 — same reason. The rename-snapshot correctly references the pre-rename path.

### §3.4 Snapshot body vs frontmatter split

Step 5 handles snapshot BODIES (wikilink text in content). Step 8 handles snapshot FRONTMATTER (`snapshot_of:` field). Different patterns, different scan/replace logic, so separate steps.

---

## §4 Watermark preservation contract (Step 6)

### §4.1 Why NOT update `_graph.md` frontmatter `date:`

`date:` (and `last_graph_write:` — the ISO precision field) is the watermark `/graph last` uses to detect changed files. Advancing it here would silently mask any thesis modified before today but not yet captured by `/graph last` — those files would be excluded from the next `/graph last` change-detection set, leaving stale adjacency entries undetected.

Watermark ownership belongs exclusively to `/graph`. `/rename` updates CONTENT of `_graph.md` (the adjacency entry header) but must NOT advance the watermark.

The next `/graph last` will correctly re-extract this thesis (mtime advanced by the rename) plus any other pending changes.

### §4.2 Why surgical adjacency-header Edit, not full re-extract

`/rename` doesn't do full `/graph` work — it just renames the entry header:
- `### TICKER - [old_name]` → `### TICKER - [new_name]`

Adjacency links (sectors, macros, cross-thesis, research, plus T7.3 `status:` and `log_tail:`) all remain valid — they weren't affected by the name change. Full re-extract would be wasteful.

Graph validation (Step 6 tail) catches any corruption from the targeted Edit.

---

## §5 Seven wikilink patterns

### §5.1 Why seven, not five

The `_shared/wikilink-forms.md` contract defines 5 canonical forms. `/rename` includes 2 additional archive-specific forms (`[[_Archive/TICKER - OldName]]` and `[[_Archive/TICKER - OldName.md]]`) because:

Pre-closure history may include wikilinks created by `/scenario reverse` `## Reversal Notes`, `/prune` closure-notification Log entries, or `/rollback` Step 6.2.5 intervening-neighbor scans — all of which use archive-path wikilinks for closed theses.

If the renamed thesis was previously closed-then-reopened (e.g., via rollback + /status closed→active), those archive-path wikilinks still exist in other files' histories. `/rename` must cover them.

---

## §6 Archive collision check (Step 1.3)

### §6.1 Why warn, not block

`_Archive/TICKER - [new_name].md` existing from a prior closure means: if the renamed thesis is later closed, `/status` Step 7.5 would silently overwrite the old archive copy (POSIX `mv` semantics).

This isn't a present-time breakage — the rename itself is safe. It's a future-time hazard. User gets three options:
- **(a) Proceed anyway** — accept future overwrite risk (user may intend to replace old archive)
- **(b) Rename old archive first** — timestamp-suffix the old archive (e.g., `(closed YYYY-MM-DD)`) before re-running /rename
- **(c) Cancel** — handle archive elsewhere before renaming

### §6.2 Why `_Archive/` non-recursive

`_Archive/Snapshots/` is excluded from the collision check. Snapshots aren't live theses — they're tier-2 immutable audit records. A snapshot at `_Archive/Snapshots/TICKER - [new_name] (pre-sync ...).md` doesn't collide with the thesis at `_Archive/TICKER - [new_name].md`; they coexist.

---

## §7 Name sanitization (Step 0.2) — why before Step 1

Sanitization runs at Step 0.2 (pre-flight) rather than Step 1 (validate) because:
- Rejected names should fail FAST before any file inspection
- Sanitization produces clean variant suggestions — user can re-invoke with a corrected name without having spent time on vault surveys
- Separating concerns keeps Step 1 focused on existence checks

The contract's rejection rules catch: illegal filesystem chars, leading dot, reserved Windows names, length >100, non-NFC Unicode, empty-after-trim.

---

## §8 Out-of-scope edge cases

### §8.1 Ticker change (`FB → META`)

TICKER must be stable — `/rename` operates on the company-name segment only. For ticker changes:
1. `/thesis META` (create new thesis)
2. Copy content from old thesis manually
3. `/status FB active→closed` (archive the old)

Future `/reticker` skill could automate this.

### §8.2 Renaming archived theses

`/rename` operates on `Theses/` only. Archived theses in `_Archive/` are Tier 3 immutable — renaming them would require different handling (update archive-ticker-registry entry, preserve snapshot refs). Manual mv + registry edit is the current path.

### §8.3 Old name with regex special chars

Glob and grep assume literal string matching. Alphanumeric and common punctuation (spaces, hyphens, ampersands) work. Unusual symbols (parentheses, braces, dollar signs) in the OLD name should prompt explicit escaping confirmation — not currently enforced; user responsibility until automation lands.
