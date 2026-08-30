---
type: status-manifest
batch: status-NBIS-2026-08-27-184559
status: completed
completed_date: 2026-08-27
ticker: NBIS
transition_type: status
field: status
old_value: draft
new_value: active
trigger_alignment: outside triggers (Conviction Triggers section gates HIGH/LOW/CLOSE conviction moves only; no trigger covers a status draft→active transition)
date: 2026-08-27
---

# Status Transaction Manifest (in-progress)

Manifest written at Step 3.0.5 before any file modifications. Intended edits:

## Thesis frontmatter edit
- Target: `Theses/NBIS - Nebius Group.md`
- Field: status
- Change: draft → active
- Snapshot taken: skipped (draft→active exception per §2.2 — no analytical content change, only frontmatter status flip)

## Sector note edit (if applicable per Step 5.1 dry-run)
- Resolution: exact — `Sectors/Neoclouds & GPU-as-a-Service.md` (thesis `sector:` frontmatter matches filename verbatim)
- Edit planned: yes — NBIS's Active Theses bullet is already present but its descriptive text still reads "draft (init 2026-06-02)"; by analogy to the monitoring→active "present but annotated monitoring" case, a present-but-stale-annotation counts as edit-needed. Mirrors the SPCX precedent in the same sector note (draft→active promoted 2026-08-13, bullet text updated to "active (promoted ...)").
- Snapshot taken: [[_Archive/Snapshots/Neoclouds & GPU-as-a-Service (pre-status 2026-08-27-184559)]]
- Applied: §Active Theses NBIS bullet annotation "draft (init 2026-06-02)" → "active (promoted 2026-08-27; Live Portfolio Full 25%+ weight was ahead of draft status)"; §Log entry appended documenting the promotion.

## Archive move (closure only)
- N/A — not a closure transition.

## Graph invalidations (closure only)
- N/A — not a closure transition.

## Archive registry append (closure only)
- N/A — not a closure transition.

## _hot.md edits
- Active Research Thread: different-ticker continuation (no single-ticker wikilink in prior thread) — compressed outgoing thread to a new `*Previous 2026-08-27:*` line (prepended), replaced thread body with this status change; dropped oldest `*Previous 2026-08-24:* /thesis VSH + CRDO` line per the max-5 rule.
- Recent Conviction Changes: new verbatim entry prepended (never compressed per contract).
- Portfolio Snapshot: Conviction line + regenerated-comment updated to reflect the status touch; Coverage/Open-followups lines untouched.
- Open Questions: no edit — OQ-197 (NBIS weight vs disclosure) is not resolved by this transition, stays open.
- Word count post-edit: 6,807 / 8,000 soft cap — no compression triggered. No truncation markers found.
- _followups.md: grepped `## Open` for NBIS — no matching entries, nothing to resolve.

## Recovery guidance

If this file persists with `status: in-progress`, /status crashed mid-run:
- (a) Skeleton only → thesis unchanged; rm manifest.
- (b) Thesis edited but later steps failed → /rollback [snapshot_batch].
- (c) Partial closure (archived but sector not updated) → /rollback handles both via snapshots. (N/A this run — non-closure transition.)

Flipped to `status: completed` at Step 7.9 after all stages succeed.
/lint #48 surfaces in-progress as Important.
