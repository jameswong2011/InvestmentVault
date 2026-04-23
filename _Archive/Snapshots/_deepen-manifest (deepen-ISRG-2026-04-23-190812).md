---
type: deepen-manifest
batch: deepen-ISRG-2026-04-23-190812
status: completed
ticker: ISRG
section: Risks
date: 2026-04-23
completed_date: 2026-04-23
---

# Deepen Manifest

> **If `status: in-progress`**, `/deepen` crashed between Phase 4.5 (skeleton)
> and Phase 7.5 (flip). Check thesis `## Log` for today's date + `Deepening` prefix
> to see whether the provisional entry has been superseded by the final `Deepened` entry.
> Recovery: `/rollback deepen-ISRG-2026-04-23-190812` → Step 2.5g offers:
>   (a) Restore thesis from pre-deepen snapshot (undo section rewrite + Log entry).
>   (b) Full cascade — (a) + delete supporting research note (if Phase 6 created one).
>   (c) Cancel.
>
> **If `status: completed`**, Phase 4-7 all succeeded. `/rollback` Step 2.5g is
> still available within the cascade's per-snapshot age window.

## Thesis snapshot
- [[_Archive/Snapshots/ISRG - Intuitive Surgical (pre-deepen 2026-04-23-190812)]]

## Thesis target
- `Theses/ISRG - Intuitive Surgical.md`
- Section deepened: Risks

## Research note created (if any)
- [[Research/2026-04-23 - ISRG - Industrial Robotics Convergence Risk - deep-dive]]

## Phase 5 Log-append outcome
- succeeded: provisional `Deepening Risks — in progress` replaced by final `Deepened Risks: ...` entry. `grep -qF` verification passed on first attempt (EDIT_OK).
