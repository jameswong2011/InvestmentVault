---
type: compare-manifest
batch: compare-2026-08-04-202309
status: completed
completed_date: 2026-08-04
date: 2026-08-04
---

# Compare Batch Manifest

> **If `status: in-progress`**, `$compare` crashed between Phase 5.0 (skeleton)
> and Phase 5.5c (flip). Check the vault for partial state:
>   - Research note at `Research/2026-08-04 - [tickers] - Competitive Comparison.md` may or may not exist.
>   - Thesis Logs may have partial appends (filter by today's date + comparison wikilink).
>   - Sector notes may have been edited (Phase 5.5b rolls back on failure, but crash mid-5.5b leaves partial edits).
> Recovery: `$rollback compare-2026-08-04-202309` → cascade through each affected sector snapshot in Phase 5.5a.
>
> **If `status: completed`**, Phase 5 finished with all sector writes succeeding atomically.
> **If `status: rolled-back`**, Phase 5.5b atomicity fired — sectors restored from 5.5a snapshots; research note and thesis Logs preserved.

## Tickers compared
- NBIS, CRWV

## Sector writes attempted
- Sectors/Neoclouds & GPU-as-a-Service.md — succeeded (snapshot: [[_Archive/Snapshots/Neoclouds & GPU-as-a-Service (pre-compare 2026-08-04-202309)]])

## Sector writes rolled back (if any)
- (none)

## Thesis Log appends
- NBIS: succeeded
- CRWV: succeeded

## Research note
- [[Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison]]
- propagated_to: set ([NBIS, CRWV])
