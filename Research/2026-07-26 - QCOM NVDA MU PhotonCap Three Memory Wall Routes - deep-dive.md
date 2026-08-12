---
date: 2026-07-26
tags: [research, Semiconductors, QCOM, NVDA, MU, CBRS]
sector: Memory Semiconductors
ticker: MU
propagated_to: [NVDA]
source: 'https://photoncap.net/p/three-routes-around-the-memory-wall'
source_type: deep-dive
---

## Thesis Delta
Consensus treats HBM scarcity as pure DRAM-maker windfall with no architectural response → PhotonCap audits three bypass routes that HBM's own price summons: (1) distance—Qualcomm HBC stacking LPDDR via TSV claiming 133TB/s/card without HBM (MSFT Azure partner optics vs Meta deal which is C1000 CPU, not HBC); (2) compression—NVIDIA Rubin PTX ISA 9.4 LUT tensor cores at 3.125 bits/weight; (3) pooling—left mostly alone here. AMD–Cerebras disaggregated prefill(HBM)/decode(SRAM) and mega Samsung–Broadcom / SK–NVIDIA LOIs arrive in the same window. Higher HBM $/byte improves economics of using less HBM—but does not kill HBM as the proven path.

## Summary
Memory wall redefined as access-speed (decode bytes/s), not capacity (except large-KV branch). Kitchen analogy: speed trips, cut trips, or move fridge. Piece stress-tests Samsung SiPh vertical thesis under bypass pressure, maps DRAM makers' margin-mix game, and asks when optics still arrives even if some HBM content is engineered down. Key distinction: Meta multi-gen deal ≠ HBC deployment; Microsoft HBC partnership lacks disclosed scale/timing. Preview doc ≠ GA for Rubin 3-bit mode.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| QCOM HBC claim | 133TB/s per AI250 card; 18× vs AI200 LPDDR5X | [1×: QCOM / PhotonCap] |
| QCOM DC rev target | >$15B by FY2029 | [1×: QCOM ID] |
| Rubin weight format | 3.125 bits (3-bit LUT index) PTX 9.4 preview | [1×: NVIDIA / PhotonCap] |
| AMD–Cerebras avail | 2H26 Cerebras Cloud | [1×: PhotonCap] |
| Mega LOIs (pub day) | Samsung–AVGO $200B+ MOU; SK–NVDA $500B+ LOI | [1×: PhotonCap] |

## Contradiction Check
Supports holding MU/SKH through scarcity while tracking architectural erosion risk from QCOM HBC and aggressive quantization. Falsifiers: HBC sustained BW ≪ claim; Rubin 3-bit never ships; HBM price breaks and removes bypass urgency.
