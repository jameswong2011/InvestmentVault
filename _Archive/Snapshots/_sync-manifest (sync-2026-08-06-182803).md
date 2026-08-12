---
type: sync-manifest
batch: sync-2026-08-06-182803
mode: default
status: completed
date: 2026-08-06
completed_date: 2026-08-06
---

# Sync Batch Manifest (completed)

Manifest written at Step 2.9 before any file modifications. Populated at
phase boundaries (end of Step 3, 4, 5) then flipped to status: completed
at Step 7.5.

If this file persists with status: in-progress, the sync crashed or was
interrupted. Recovery: inspect the sections below, then $rollback to
restore any Tier A snapshots listed.

## Theses with snapshots taken (Tier A)
- `Theses/CRWV - CoreWeave.md` → `_Archive/Snapshots/CRWV - CoreWeave (pre-sync 2026-08-06-182803).md` — substantive Rubin fleet-economics integration; repaired producer-state inconsistency (source frontmatter claimed propagation, live thesis contained no reference or Log entry)

## Theses with Log-only appends (Tier B)
- None

## Sector notes touched
- Tier A: `Sectors/Neoclouds & GPU-as-a-Service.md` → `_Archive/Snapshots/Neoclouds & GPU-as-a-Service (pre-sync 2026-08-06-182803).md` — corrected Rubin rate corridor integrated into competitive dynamics, investor heuristics, Mental Models, Related Research, and Log
- Tier B: `Sectors/Data Center Power & Cooling.md` — comparison link + Log only
- Tier B: `Sectors/Compute & AI Compute Accelerators.md` — comparison link + Log only
- Tier B: `Sectors/Custom Silicon & Networking Semiconductors.md` — comparison link + Log only

## Macro notes touched
- None — user scope was limited to related theses and sector notes

## Source research notes processed
- `Research/2026-08-04 - NBIS - Rubin Generation ROIC - deep-dive.md` — already propagated to NBIS; superseded derivation history retained for sector context
- `Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison.md` — thesis propagation already present in NBIS and CRWV
- `Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive.md` — NBIS already propagated; CRWV live-state repair completed
