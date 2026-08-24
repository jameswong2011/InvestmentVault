---
type: sync-manifest
batch: sync-2026-08-22-100928
mode: default
status: completed
date: 2026-08-22
completed_date: 2026-08-22
---

# Sync Batch Manifest (completed)

Manifest written at Step 2.9 before any file modifications. Populated at
phase boundaries (end of Step 3, 4, 5) then flipped to status: completed
at Step 7.5.

If this file persists with status: in-progress, the sync crashed or was
interrupted. Recovery: inspect the sections below, then /rollback to
restore any Tier A snapshots listed.

## Theses with snapshots taken (Tier A)
- [[Theses/NVDA - Nvidia]] → [[_Archive/Snapshots/NVDA - Nvidia (pre-sync 2026-08-22-100928)]]
- [[Theses/NBIS - Nebius Group]] → [[_Archive/Snapshots/NBIS - Nebius Group (pre-sync 2026-08-22-100928)]]
- [[Theses/NET - Cloudflare]] → [[_Archive/Snapshots/NET - Cloudflare (pre-sync 2026-08-22-100928)]]
- [[Theses/AVGO - Broadcom]] → [[_Archive/Snapshots/AVGO - Broadcom (pre-sync 2026-08-22-100928)]]
- [[Theses/MRVL - Marvell Technology]] → [[_Archive/Snapshots/MRVL - Marvell Technology (pre-sync 2026-08-22-100928)]]

## Theses with Log-only appends (Tier B)
- [[Theses/000660 - SK Hynix]] — CMM-Ax is CXL-PNM not HBM; HIGH/LOW/CLOSE no-touch

## Sector notes touched
- [[Sectors/Compute & AI Compute Accelerators]] — Tier A (heuristics #9 + MM [G-14]/[G-3]; snapshot)
- [[Sectors/Custom Silicon & Networking Semiconductors]] — Tier A (heuristics Google 8-K + MM first-pop CHG-14; snapshot)
- [[Sectors/Neoclouds & GPU-as-a-Service]] — Tier A (incremental-MW auction mix; snapshot)

## Macro notes touched
- [[Macro & Technology/Sustainability of AI Capex]] — Tier A (tranche-C mix allocator)
- [[Macro & Technology/Agentic Internet]] — Tier A (Era 3 harness + compute economics)
- [[Macro & Technology/CXL Memory Disaggregation Framework]] — Tier A (Aug delta: CMM-Ax ≠ PF)

## Source research notes processed
- [[Research/2026-08-21 - NVDA - SemiAnalysis Open Models Catching Up - deep-dive]] → NVDA, NBIS, NET, AVGO
- [[Research/2026-08-21 - MRVL NVDA 000660 - Damnang Marvell Part 3 - deep-dive]] → MRVL, NVDA, 000660, AVGO
- [[Research/2026-08-21 - Macro Quantum - Superposition Qubit Count Is Not Compute - deep-dive]] — unresolved (no quantum thesis / sector / macro file; not invented)
