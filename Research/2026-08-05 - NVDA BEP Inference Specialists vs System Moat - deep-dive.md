---
date: 2026-08-05
tags: [research, Semiconductors, NVDA, AMD]
sector: Custom Silicon & Networking Semiconductors
ticker: NVDA
propagated_to: [AMD]
source: 'https://bepresearch.substack.com/p/all-roads-and-rockets-lead-to-nvidia'
source_type: deep-dive
---

## Thesis Delta
Consensus frames inference startups (photonic/analog/in-memory) as credible NVIDIA share takers on tok/s → BEP (free half) argues training is already conceded, and the real fight is whether inference stays a **system/fleet problem** NVIDIA expands into (Dynamo/LPU/software 2.7× on same silicon) vs a separable commodity layer specialists need. SpaceX/Musk Q2 endorsement of Vera Rubin as "best AI computer" + exclusive NVIDIA plan (with Starmind NVL72-in-orbit and vendor-agnostic fine print) is customer-layer confirmation. Updates [[Theses/NVDA - Nvidia]]; paid AMD-print/bear section not ingested.

## Summary
Rosewood Sand Hill panel (Lightmatter, d-Matrix, EnCharge, Mythic) under Chatham House: training conceded to NVIDIA; inference is the battleground. Specialist attack pattern: narrow workload, strip unused silicon, win a number, get designed in — same pattern that lost to NVIDIA when product definition moved (T&L, then CUDA). Tokens/s and tok/W are non-comparable across vendor-chosen configs; CFOs want cost-per-task (Octane tool: 20 models × 32 tasks, 73× price spread at similar top quality). Dynamo + MLPerf v6.0: same GB300 NVL72 DeepSeek-R1 tok/s/GPU 2,907→8,064 in six months via software. Same day: Musk on SpaceX Q2 — exclusive NVIDIA going forward; end-2026 >2GW, next year closer to 10GW than 5, up to 20GW power/cooling ahead of GPUs; Starmind = optimized Vera Rubin NVL72 in SSO; also "AI chip vendor agnostic" + planned in-house/Tesla fab — exclusive can be unmade. Free half ends before paid AMD earnings reprice / bear case.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| Panel specialists | Lightmatter, d-Matrix, EnCharge, Mythic | [1×: BEP] |
| MLPerf GB300 DeepSeek-R1 | 2,907 → 8,064 tok/s/GPU (~2.7×) | [1×: MLPerf via BEP] |
| SpaceX year-end compute | >2 GW (2026); ~10 GW framing 2027 | [1×: Musk / BEP] |
| Power/cooling target | up to 20 GW ahead of GPUs | [1×: Musk / BEP] |
| Architecture choice | "exclusively on Nvidia" / Vera Rubin | [1×: Musk quote] |
| Starmind | orbital NVL72-class; sun power / vacuum cool | [1×: Musk / BEP] |
| Octane spread | 73× $/finished-task at similar quality | [1×: BEP tool] |

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] ecosystem/system-product framing vs pure-ASIC displacement. Challenges "challenger tok/s wins sockets." Partial (paywalled AMD/bear half). Falsifiers: SpaceX unwinds exclusivity into agnostic modules; specialist cost-per-task wins hyperscaler sockets at scale; Dynamo gains stall.

## Framework / Mental Model
Price = tokens; cost = mistakes. Unit of product is the fleet, not the chip. Specialist wins a layer; NVIDIA expands the stack until that layer is an internal optimization.
