---
type: thesis-manifest
batch: thesis-ORCL-2026-07-29-234656
status: completed
completed_date: 2026-07-29
ticker: ORCL
proposed_name: Oracle Corporation
proposed_path: Theses/ORCL - Oracle Corporation.md
sector: Cloud Infrastructure
date: 2026-07-29
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/ORCL - Oracle Corporation.md`
- Status: created

## Sector note update
- Sector resolution: none (`Cloud Infrastructure` — no exact/normalized/substring match in Sectors/*.md)
- Sector note path: n/a
- Edit applied: skipped (no sector note; user-confirmed Step 5 option b — proceed without sector update; also draft status)

## `_hot.md` updates
- Active Research Thread entry: ORCL top bullet added; BE demoted to *Previous:* line; oldest *Previous:* (2026-07-17 /deepen 000660) dropped per max-5 rule
- Recent Conviction Changes entry: ORCL initial MEDIUM entry prepended
- Open Questions entries: 3 added (146-148)

## Orphan research integration
- Orphan research notes touched: none (no Research note carries `ticker: ORCL` or ORCL as a tags token; body-text Oracle mentions are not orphan matches per resolution order a/b)
- Wikilinks added to Related Research: 0 orphan-driven (11 Related Research links added at authoring time)

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (Signals A–E all empty)
- User decision: n/a (no collision)

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis ORCL`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
