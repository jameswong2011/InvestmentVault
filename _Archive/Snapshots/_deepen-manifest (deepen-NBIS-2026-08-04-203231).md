---
type: deepen-manifest
batch: deepen-NBIS-2026-08-04-203231
status: completed
ticker: NBIS
section: Key Non-consensus Insights
date: 2026-08-04
completed_date: 2026-08-04
---

# Deepen Manifest

> **If `status: in-progress`**, `/deepen` crashed between Phase 4.5 (skeleton)
> and Phase 7.5 (flip). Check thesis `## Log` for today's date + `Deepening` prefix
> to see whether the provisional entry has been superseded by the final `Deepened` entry.
> Recovery: `/rollback deepen-NBIS-2026-08-04-203231` → Step 2.5g offers:
>   (a) Restore thesis from pre-deepen snapshot (undo section rewrite + Log entry).
>   (b) Full cascade — (a) + delete supporting research note (if Phase 6 created one).
>   (c) Cancel.
>
> **If `status: completed`**, Phase 4-7 all succeeded. `/rollback` Step 2.5g is
> still available within the cascade's per-snapshot age window.

## Thesis snapshot
- [[_Archive/Snapshots/NBIS - Nebius Group (pre-deepen 2026-08-04-203231)]]

## Thesis target
- `Theses/NBIS - Nebius Group.md`
- Section deepened: Key Non-consensus Insights

## Research note created (if any)
- [[Research/2026-08-04 - NBIS - Rubin Generation ROIC - deep-dive]]

## Phase 5 Log-append outcome
- succeeded: provisional `Deepening Key Non-consensus Insights — in progress` replaced by final `Deepened Key Non-consensus Insights (new Insight #6, Rubin-generation ROIC)`.

## _hot.md update
- ABORTED per hot-md-contract hard-cap rule: file was already at 5,012 words (>5,000 hard cap) pre-run from today's /thesis IREN + /compare adds. Deepen recorded in thesis Log + research note + this manifest instead. Recommend a /sync compression pass to bring _hot.md under cap, then add the NBIS Rubin-ROIC Active Research Thread entry.
