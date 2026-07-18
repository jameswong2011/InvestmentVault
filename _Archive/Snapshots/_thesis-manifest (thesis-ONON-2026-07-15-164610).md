---
type: thesis-manifest
batch: thesis-ONON-2026-07-15-164610
status: completed
completed_date: 2026-07-15
ticker: ONON
proposed_name: On Holding
proposed_path: Theses/ONON - On Holding.md
sector: Athletic Footwear & Apparel
date: 2026-07-15
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/ONON - On Holding.md`
- Status: created (conviction: medium, status: draft)

## Sector note update
- Sector resolution: none → new sector note created (exact match after creation); user chose option (a)
- Sector note path: Sectors/Athletic Footwear & Apparel.md
- Edit applied: new_sector_note_created — ONON seeded as first Active Thesis (anchor entry; thesis is draft)

## `_hot.md` updates
- Active Research Thread entry: added ONON MEDIUM-draft entry; compressed 3 prior 2026-07-14 entries (LYV/TSEM/Intel) to *Previous:* lines
- Recent Conviction Changes entry: added ONON initial MEDIUM
- Open Questions entries: 3 added (items 138-140: cohort/LTV, floor-vs-fade, premium-discipline)
- Word count post-edit: 4,406 (over 4,000 soft cap, under 5,000 hard cap; net reduction from prior ~4.9-5.0k). Warning raised; /sync all recommended for backlog roster-compression.

## Orphan research integration
- Orphan research notes touched: Research/2026-07-14 - ONON - On Holding Business Breakdown - deep-dive.md
- Wikilinks added to Related Research: 1

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (all 5 signals clear)
- User decision: n/a

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis ONON`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
