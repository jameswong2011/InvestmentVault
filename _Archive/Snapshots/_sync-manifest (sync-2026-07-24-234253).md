---
publish: false
type: sync-manifest
batch: sync-2026-07-24-234253
mode: default
status: completed
date: 2026-07-24
completed_date: 2026-07-24
---

# Sync Batch Manifest (in-progress)

Manifest written at Step 2.9 before any file modifications. Populated at
phase boundaries (end of Step 3, 4, 5) then flipped to status: completed
at Step 7.5.

If this file persists with status: in-progress, the sync crashed or was
interrupted. Recovery: inspect the sections below, then /rollback to
restore any Tier A snapshots listed.

## Theses with snapshots taken (Tier A)
- None in this sync run. (TSM's Tier A body rebase happened same-session immediately pre-sync as a research-driven manual update; its snapshot: [[_Archive/Snapshots/TSM - Taiwan Semiconductor (pre-earnings-update 2026-07-24-233324)]] — recorded here for batch-audit continuity.)

## Theses with Log-only appends (Tier B)
- Theses/NVDA - Nvidia.md — cross-thesis propagation (packaging = binding growth limit)
- Theses/AMAT - Applied Materials.md — cross-thesis propagation (capex raise → WFE floor)
- Theses/LRCX - Lam Research.md — cross-thesis propagation (capex raise → WFE floor)
- Theses/KLA - KLA Corporation.md — cross-thesis propagation (capex raise + node cadence)
- Theses/ASMI - ASM International.md — cross-thesis propagation (capex raise + GAA cadence)
- Theses/BESI - BE Semiconductor Industries.md — cross-thesis propagation (AP 10-20% of capex)
- Theses/AVGO - Broadcom.md — cross-thesis propagation (CoWoS allocation + EMIB-T)
- Theses/AMD - Advanced Micro Devices.md — cross-thesis propagation (N2/A14 runway + packaging allocation)
- Theses/MRVL - Marvell Technology.md — cross-thesis propagation (allocation squeeze on marginal ASICs)
- Theses/INTC - Intel.md — cross-thesis propagation (EMIB overflow + 18A reports, unconfirmed)
- Theses/000660 - SK Hynix.md — cross-thesis propagation (HBM4 demand-side corroboration)
- Theses/TSEM - Tower Semiconductor.md — cross-thesis propagation (COUPE shadow)
- Theses/2383 - Elite Material.md — cross-thesis propagation (substrate volume + glass-free CoPoS)
- Theses/3110 - Nitto Boseki.md — cross-thesis propagation (glass-free CoPoS timing)

## Sector notes touched
- Sectors/Semiconductor Foundries.md — Tier A analytical edits (node table, GM anchor, guide/capex/US-commitment rebase, KQ#3, Investor heuristics). Snapshot: [[_Archive/Snapshots/Semiconductor Foundries (pre-sync 2026-07-24-234253)]]

## Macro notes touched
- Macro & Technology/AI Bubble Risk and Semiconductor Valuations.md — Tier B Log append (supply-commitment + sell-the-beat datapoint)
- Macro & Technology/Organic ABF to Glass-Core Substrate Transition.md — Tier B Log append (CoPoS gen-1 possibly glass-free signpost)

## Source research notes processed
- Research/2026-07-24 - TSM Q2 2026 Results - earnings.md — propagated_to backfilled: [TSM, NVDA, AMAT, LRCX, KLA, ASMI, BESI, AVGO, AMD, MRVL, INTC, 000660, TSEM, 2383, 3110]
