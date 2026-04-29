---
type: thesis-manifest
batch: thesis-AIXA-2026-04-29-001208
status: in-progress
ticker: AIXA
proposed_name: Aixtron
proposed_path: Theses/AIXA - Aixtron.md
sector: Semiconductor Capital Equipment
date: 2026-04-29
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/AIXA - Aixtron.md`
- Status: created

## Sector note update
- Sector resolution: exact (Sectors/Semiconductor Capital Equipment.md)
- Sector note path: `Sectors/Semiconductor Capital Equipment.md`
- Edit applied: skipped (draft status — added to Active Theses when promoted via /status AIXA status draft→active)

## `_hot.md` updates
- Active Research Thread entry: (populated — text appended or `failed`)
- Recent Conviction Changes entry: (populated)
- Open Questions entries: (populated — count added)

## Orphan research integration
- Orphan research notes touched: (populated — list of paths whose mtime was advanced)
- Wikilinks added to Related Research: (populated — count)

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (Signals A/B/C/D all empty)
- User decision: n/a

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis AIXA`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: 2026-04-29`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
