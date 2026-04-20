---
type: skill-rationale
skill: /rollback
purpose: Design rationale and edge-case documentation for /rollback. NOT loaded at invocation — SKILL.md references sections by §N.M anchor.
last_reviewed: 2026-04-20
---

# /rollback Design Rationale

> SKILL.md contains operational rules. This file explains why those rules are shaped the way they are. Maintainers read this; the LLM executing /rollback does not.

---

## §1 Batch ID & snapshot collision design

### §1.1 Why 6-digit HHMMSS for `snapshot_batch:`

6-digit second-precision (`rollback-YYYY-MM-DD-HHMMSS`) prevents same-minute batch collisions across concurrent skill invocations. A 4-digit HHMM scheme would produce identical batch IDs for two rollbacks started in the same minute — cascade detection would then incorrectly pair snapshots from unrelated operations.

### §1.2 Reuse across safety snapshots

Step 4 generates the HHMMSS once; Steps 4 (thesis safety snapshot), 6.1c (sector safety snapshot), 6.2 (archived-copy preservation) all reuse the same `snapshot_batch:` value. This enables a future "rollback of this rollback" to cascade-restore every file modified in one atomic operation rather than requiring user intervention per file.

### §1.3 Cascade batch mode interaction with per-file HHMMSS

When a cascade restores multiple theses whose sectors differ, each sector snapshot reuses the same rollback HHMMSS. When multiple theses share a sector, one sector snapshot suffices (don't double-snapshot). The batch ID binds the set; distinct HHMMSS within a batch would defeat cascade detection.

---

## §2 Cascade detection semantics

### §2.1 Why `snapshot_batch:` with legacy fallback

Primary match: `snapshot_batch:` frontmatter exact string. Legacy snapshots (pre-field) fall back to `snapshot_trigger:` + `snapshot_date:` date portion (`YYYY-MM-DD`, ignoring time suffix). The legacy fallback accepts `-HHMM` and `-HHMMSS` formats — matching on the date prefix only when formats differ.

Batch matching is operation-precise: same-day repeat operations (e.g., two `/sync` runs on the same day) get distinct batch IDs and never cross-match. The `YYYY-MM-DD`-only fallback is coarser but still safe because two legacy same-day operations writing multiple snapshots each is extraordinarily rare and the user confirms cascade scope explicitly.

### §2.2 Per-manifest cascade types (2.5b/c/d/e/f) — design

Each manifest type corresponds to a distinct multi-file transaction pattern:

| Cascade | Transaction pattern | Why it exists |
|---|---|---|
| 2.5a | Trigger+date match (no manifest) | Baseline for pre-manifest snapshots |
| 2.5b sync-manifest | Tier A snapshots + Tier B Log-only appends | Tier B cross-thesis propagation has no snapshot; manifest records the Log entry text for strikethrough review |
| 2.5c prune-manifest | Closures + upgrades + Stage 4.2 neighbor notifications | Prune writes Log entries on neighbors without per-neighbor snapshots (same rationale as sync Tier B) |
| 2.5d stress-test-manifest | Log-only (no snapshot) on tested thesis | Stress-test's only direct effect is an append-only Log entry; no snapshot possible |
| 2.5e status-manifest | Thesis frontmatter + sector + optional archive mv + invalidations + _hot.md | Multi-file transaction with all-or-nothing atomicity |
| 2.5f thesis-manifest | Deletion-based, not restore-based | /thesis creates new files; undo means deleting + reverting sector/hot.md — no "before state" to restore |

### §2.3 Why sync 2.5b surfaces Tier B entries for manual review

Tier B Log entries cannot be auto-reverted — they are append-only per CLAUDE.md Tier 2. Three user options exist:
- **Surface only**: leave as historical audit trail (preferred per CLAUDE.md convention)
- **Strikethrough with `~~entry~~ → Reverted YYYY-MM-DD:`**: preserves audit trail with explicit reversal signal; violates Tier 2 in letter but not in spirit (the original text is preserved)
- **Manual delete**: clear Tier 2 violation; only acceptable if entry was clearly erroneous

The skill does NOT auto-delete. Strikethrough is the middle path and must be user-confirmed.

### §2.4 Sync cascade fallback when manifest missing

`⚠️ No sync manifest found for batch [batch ID]. Cascade will only restore Tier A snapshots; any Tier B Log appends from this sync are invisible and will persist after rollback.`

This handles two cases: (1) sync ran before manifest support landed (pre-T2.1), (2) manifest write itself failed. The fallback grep instruction lets the user manually find intervening entries — not ideal but degrades gracefully rather than silently losing them.

---

## §3 Rename-snapshot handling (Step 4a)

### §3.1 Why three options instead of direct restore

A snapshot created by `/rename` points `snapshot_of:` to the OLD path but the file now lives at NEW path (via successful mv). Naïve restore would:
1. Write snapshot content to OLD path → creates a duplicate file (both old and new names exist)
2. Leave all inbound wikilinks pointing to NEW name (they were updated by /rename)
3. Produce permanent dual-file state until user manually deletes one

Options presented:
- **(a) Symmetric reverse-rename** — RECOMMENDED. Run `/rename [TICKER] "[old_name]"`. /rename is symmetric: its own inverse. Atomically restores filename + inbound wikilinks + graph header + sector Active Theses + snapshot_of fields. /rollback cannot inline this logic without duplicating the entire /rename implementation.
- **(b) Content-only restore** — write snapshot content to OLD path anyway. Accepts the duplicate-file outcome knowingly. Only useful for side-by-side comparison.
- **(c) Cancel** — user decides later.

### §3.2 Why /rollback doesn't inline /rename logic

The rename atomicity contract (7 wikilink patterns, `_graph.md` header, sector note entry, snapshot_of updates, `_hot.md` mentions) is non-trivial. Duplicating it in /rollback would create two implementations to keep in sync. The symmetric-reverse recommendation delegates to /rename's canonical logic.

---

## §4 Step 6.2.5 intervening-neighbor scan (recreated-file rollbacks only)

### §4.1 Problem this solves

Thesis X closed on day C. Between C and today (rollback day R), other skills (`/stress-test`, `/sync`, `/scenario`, `/compare`, `/prune`) may have written Log entries to OTHER theses citing X's closure as premise (e.g., "AMAT no longer faces NVDA competition after NVDA closure"). After restoring X on day R, those intervening Log entries are premised on a now-false state.

The entries are Tier 2 append-only — they cannot be silently edited. The user needs to know they exist, and needs tooling to annotate them.

### §4.2 Why only on recreated-file rollbacks

Standard rollbacks restore a file that was never closed. There's no closure date to anchor the post-closure scan, and intervening edits to the restored file's body (rather than to neighbors' Logs) are the relevant recovery concern — handled by cascade detection (Step 2.5), not 6.2.5.

### §4.3 H3 extension — why scan Macro + Sector beyond Theses

Pre-H3: scan only looked at `Theses/*.md` Log sections. This missed premise-dependent references in:
- **Macro body prose**: "Iranian retaliation risk most directly affects [[_Archive/LITE - Lumentum]]..." — macros often lack `## Log` sections; citations live in narrative prose.
- **Sector narrative sections**: post-closure text added to `## Acquisitions and new entrants`, `## Competitive dynamics`, `## Industry history` assuming the closure.

H3 extends the scan to all three directories. Mtime-based date attribution handles macros/sectors without dated Log entries: `file_mtime >= closure_date` → post-closure candidate; otherwise advisory flag.

### §4.4 Classification: premise-dependent vs contextual

LLM-judgment required for narrative prose (prefix heuristic doesn't apply):
- **Premise-dependent**: sentence asserts something about the closed state ("NVDA's exit removes..."). Strikethrough recommended.
- **Contextual**: sentence cites the thesis as historical example without premise dependency ("NVDA was closed in April 2026 after..."). Leave in place.

The three user options (surface / strikethrough premise-dependent only / strikethrough all matched / skip) trade aggressiveness vs risk. Default recommendation: (b) premise-dependent only.

### §4.5 Interaction with Step 2.5b/c cascades

If closure was via `/prune` (vs `/status`), the prune-manifest (30-day retained per 5.2) cascades Stage 4.2 "Cross-thesis closure" neighbor Logs at Step 2.5c. 6.2.5 then runs redundantly but safely — its `Cross-thesis closure:` prefix filter finds the same entries, user chooses once. Skill detects overlap and combines the list to avoid double-prompting.

If closure was via `/status`, no prune manifest exists and 6.2.5 is the primary tool.

---

## §5 Step 6.1 sector update — why mirror /status Step 5

### §5.1 Why full mirror not just partial

The sector note edit must be sector-resolved (contract-driven), dry-run gated (no orphan snapshots for no-op edits), snapshotted (for safety), and verified (post-edit syntax check). Each of these protections exists in `/status` Step 5 for the same reason: sector analytical text gets corrupted by partial edits.

Skipping any protection in `/rollback` Step 6.1 would re-introduce the drift class `/status` was designed to prevent. The full mirror is the safe default.

### §5.2 Decision matrix per revert direction

Different revert directions warrant different sector edits:
- `closed → active`: add back to Active Theses; remove from Closed/Archived if dual-listed
- `active → closed`: remove from Active Theses
- `monitoring → active`: remove monitoring annotation
- `active → monitoring`: add monitoring annotation (only if sector distinguishes monitoring)
- `conviction:` reverted: update displayed conviction (only if sector displays it)

The `edit_planned:` dry-run flag prevents orphan snapshots for no-op reverts (e.g., conviction revert on a sector that doesn't display conviction).

---

## §6 Step 6.3 — why graph update is deferred

### §6.1 Metadata boundary

`_graph.md` is owned exclusively by `/graph`. /rollback is a content-restore operation, not a graph maintenance operation. The "run `/graph last`" reminder is emitted in Step 7 report.

### §6.2 Why it matters especially for recreated-file rollbacks

Subsequent skills relying on `_graph.md` (e.g., `/sync` default mode) need the restored thesis's adjacency entry. Without `/graph last`, the thesis exists on disk but is invisible to graph-assisted propagation paths — `/sync` would see it only via the file-direct fallback, which is slower and incomplete.

For standard (non-recreated) rollbacks, the thesis's adjacency entry already exists in the graph; it may be slightly stale but still functional. Recreated files have no adjacency entry at all until `/graph last` runs.

---

## §7 Cascade batch-mode safety snapshots

### §7.1 Why Step 4 creates ALL safety snapshots before any Step 5 restoration

In cascade mode, Step 4 iterates the entire restore set creating pre-rollback snapshots FIRST, then Step 5 iterates again performing restorations. This ordering ensures:
- If any safety snapshot fails to create → abort before any restoration begins. User still has all original files.
- If any restoration fails mid-batch → all files have safety snapshots (both already-restored and not-yet-attempted). User can reverse the partial cascade with another `/rollback`.

Interleaved per-file (snapshot → restore → snapshot → restore) would leave not-yet-attempted files without safety snapshots if the run aborted.

### §7.2 Step 5 cascade failure reporting

Partial cascade completion reports:
- Which files successfully restored
- Which file failed + error
- Which remaining files not attempted
- The batch ID for reversing the partial cascade

Explicit fields prevent user confusion about which files are in what state.

---

## §8 Content-only restore warnings (Step 4a option b)

Duplicate-file outcome requires explicit acknowledgment because the vault ends up in a state the user may not expect:
- Two files exist: `[old_name]` (newly restored content) and `[new_name]` (unchanged current state)
- All inbound wikilinks across the vault still point to `[new_name]` (updated by the original /rename)
- `/sync` will see both files as distinct theses; `_graph.md` adjacency will list one or the other depending on `/graph` run timing

The Step 7 report's "Duplicate-file note" ensures the user is reminded of the side-by-side state and the consolidation steps required (decide which to keep, delete the other, re-run `/sync`).
