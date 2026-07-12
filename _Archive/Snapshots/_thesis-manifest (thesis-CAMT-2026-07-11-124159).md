---
type: thesis-manifest
batch: thesis-CAMT-2026-07-11-124159
status: completed
completed_date: 2026-07-11
ticker: CAMT
proposed_name: Camtek
proposed_path: Theses/CAMT - Camtek.md
sector: Advanced Semi Metrology
date: 2026-07-11
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/CAMT - Camtek.md`
- Status: created

## Sector note update
- Sector resolution: exact
- Sector note path: Sectors/Advanced Semi Metrology.md
- Edit applied: skipped (draft status) — CAMT added to Active Theses on /status draft→active promotion

## `_hot.md` updates
- Active Research Thread entry: appended (CAMT live thread; outgoing NET thread compressed to *Previous*). Note: a concurrent /compare 6981 run co-occupied the section and independently dropped the MRVL/AVGO *Previous* line.
- Recent Conviction Changes entry: added (CAMT initial MEDIUM)
- Open Questions entries: 3 added (items 123-125 — HBM4 tool-of-record durability, China race up/down, H2/2027 backlog vs forecast)
- Compression: compressed own CAMT ARThread+RCC entries; dropped sole Sync Archive entry (step 1) after concurrent /compare 6981 tipped file >5,000 hard cap. File chronically over 4,000 soft cap — flagged for next /sync.

## Orphan research integration
- Orphan research notes touched: none (only a body-text mention in an 000660.KS HBM note; no ticker:CAMT / tags:CAMT orphan research exists)
- Wikilinks added to Related Research: 14 (at creation — sector, ONTO, KLA, HBM research, SemiCap, BESI, AMAT, SK Hynix, TSM, NVDA, 2 macros, 2 mental-model notes)

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (all five signals clear)
- User decision: n/a

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis CAMT`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
