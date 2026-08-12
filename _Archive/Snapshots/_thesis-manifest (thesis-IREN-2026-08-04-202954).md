---
type: thesis-manifest
batch: thesis-IREN-2026-08-04-202954
status: completed
completed_date: 2026-08-04
ticker: IREN
proposed_name: IREN Limited
proposed_path: Theses/IREN - IREN Limited.md
sector: Neoclouds & GPU-as-a-Service
date: 2026-08-04
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/IREN - IREN Limited.md`
- Status: created

## Sector note update
- Sector resolution: exact (filename match)
- Sector note path: Sectors/Neoclouds & GPU-as-a-Service.md
- Edit applied: skipped (draft status) for Active Theses list; coverage-candidate pointer updated with wikilink + /thesis Log entry appended (additive)

## `_hot.md` updates
- Active Research Thread entry: IREN thread prepended; outgoing /compare NBIS-vs-CRWV compressed to *Previous* line
- Recent Conviction Changes entry: added (IREN initial MEDIUM, draft)
- Open Questions entries: 3 added (159 funding gap/dilution, 160 GPU re-rent, 161 power-floor valuation)
- Compression applied: dropped oldest *Previous* (07-29 ORCL) [step 2] + roster-compressed 2 oldest <30d RCC entries (CBRS, CAMT) [step 6]. Final word count 4,902 (under 5,000 hard cap; remains over 4,000 soft cap — chronic pre-existing state, flagged for /sync cleanup)

## Orphan research integration
- Orphan research notes touched: none (no Research note carries IREN in ticker:/tags: frontmatter; sole reference is a body-mention in 2026-06-03 Neoclouds NBIS vs CRWV deep-dive, already wikilinked)
- Wikilinks added to Related Research: 13 (sector, macro, 4 peer theses, 2 adjacency theses, power sector, 3 research notes, hedge doc)

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (Signal E hit `_Archive/Docs/Semiconductor bear market hedges 2.md` verified as a status:active macro hedging synthesis that merely tags IREN — NOT an archived IREN thesis; no dual-file collision)
- User decision: n/a (no collision)

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis IREN`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
