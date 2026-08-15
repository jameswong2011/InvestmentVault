---
type: sync-manifest
batch: sync-2026-08-15-130825
mode: default
status: in-progress
date: 2026-08-15
---

# Sync Batch Manifest (in-progress)

Manifest written at Step 2.9 before any file modifications. Populated at
phase boundaries (end of Step 3, 4, 5) then flipped to status: completed
at Step 7.5.

If this file persists with status: in-progress, the sync crashed or was
interrupted. Recovery: inspect the sections below, then /rollback to
restore any Tier A snapshots listed.

## Theses with snapshots taken (Tier A)
(none — all thesis edits this run were Tier B Log + Related Research appends)

## Theses with Log-only appends (Tier B)
- Theses/000660 - SK Hynix.md — Log + Related Research; driver: Samsung 2nm HBM base-die note
- Theses/TSM - Taiwan Semiconductor.md — Log (2 bullets) + Related Research (2); drivers: Samsung 2nm base-die + Feynman/A16 notes
- Theses/NVDA - Nvidia.md — Log + Related Research; driver: Feynman/A16 note
- Theses/LITE - Lumentum.md — Log + Related Research; driver: CPO delay-crushed note
- Theses/AAOI - Applied Optoelectronics.md — Log + Related Research (cross-thesis: CPO calendar challenges Bull #5); driver: CPO delay-crushed note
- Theses/IQE - IQE.md — Log + Related Research; driver: CPO delay-crushed note
- Theses/NBIS - Nebius Group.md — Log + Related Research; driver: Neocloud Q2 note
- Theses/CRWV - CoreWeave.md — Log + Related Research; driver: Neocloud Q2 note
- Theses/CBRS - Cerebras Systems.md — Log + Related Research (adverse blended-GM trigger-touch); driver: Neocloud Q2 note

## Sector notes touched
_populated at end of Step 4_

## Macro notes touched
_populated at end of Step 5_

## Source research notes processed
- Research/2026-08-15 - 000660 TSM NVDA - Samsung 2nm HBM Base Die - news.md → propagated_to [000660, TSM]; NVDA/MU skipped (trivial delta)
- Research/2026-08-15 - LITE AAOI NVDA - CPO Delay Rumors Crushed - news.md → propagated_to [LITE, AAOI, IQE]; NVDA/AVGO skipped (adjacent-only)
- Research/2026-08-15 - NBIS CRWV - Neocloud Q2 CoreWeave Nebius Cerebras - news.md → propagated_to [NBIS, CRWV, CBRS]; NVDA skipped (A100 print folded into CRWV Log)
- Research/2026-08-15 - NVDA TSM - Feynman Ramp TSMC A16 - news.md → propagated_to [NVDA, TSM]; AMAT/LRCX/KLAC skipped (not named, no WFE trigger)
