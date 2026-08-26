---
type: compare-manifest
batch: compare-2026-08-26-015403
status: completed
completed_date: 2026-08-26
date: 2026-08-26
---

# Compare Batch Manifest

> **If `status: in-progress`**, `/compare` crashed between Phase 5.0 (skeleton)
> and Phase 5.5c (flip). Check the vault for partial state:
>   - Research note at `Research/2026-08-26 - NBIS CRWV IREN vs Neocloud Complex - Competitive Comparison.md` may or may not exist.
>   - Thesis Logs may have partial appends (filter by today's date + comparison wikilink).
>   - Sector notes may have been edited (Phase 5.5b rolls back on failure, but crash mid-5.5b leaves partial edits).
> Recovery: `/rollback compare-2026-08-26-015403` → cascade through each affected sector snapshot in Phase 5.5a.
>
> **If `status: completed`**, Phase 5 finished with all sector writes succeeding atomically.
> **If `status: rolled-back`**, Phase 5.5b atomicity fired — sectors restored from 5.5a snapshots; research note and thesis Logs preserved.

## Tickers compared
- NBIS, CRWV, IREN (theses; vault writes)
- Web-supplemented, no vault writes: APLD, CIFR, WULF, CORZ, Lambda, Crusoe, Nscale, Together AI, Fluidstack

## Sector writes attempted
- Sectors/Neoclouds & GPU-as-a-Service.md — succeeded, 4 surfaces (Competitive dynamics prose ×3 insertions; Product level analysis table: APLD/CIFR refreshed + WULF/CORZ rows; Related Research; Log) (snapshot: [[_Archive/Snapshots/Neoclouds & GPU-as-a-Service (pre-compare 2026-08-26-015403)]]; match_confidence: exact)

## Sector writes rolled back (if any)
- (none)

## Thesis Log appends
- NBIS: succeeded (Log + Related Research)
- CRWV: succeeded (Log + Related Research)
- IREN: succeeded (Log + Related Research)

## Research note
- [[Research/2026-08-26 - NBIS CRWV IREN vs Neocloud Complex - Competitive Comparison]]
- propagated_to: set [NBIS, CRWV, IREN]
- _hot.md: Active Research Thread (same-ticker continuation), Recent Conviction Changes (flag-only), Open Questions #195–197; 6,993 words
