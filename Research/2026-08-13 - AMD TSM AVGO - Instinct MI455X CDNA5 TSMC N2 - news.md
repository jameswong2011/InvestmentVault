---
date: 2026-08-13
tags: [research, daily-intel-triage, news, AMD, TSM, AVGO, 000660]
sector: Compute & AI Compute Accelerators
ticker: AMD
propagated_to: [AMD, TSM, AVGO, 000660]
source: 'https://www.servethehome.com/amd-instinct-mi455x-deep-dive-cdna-5-marks-the-next-era-of-instinct/'
source_type: news
---

# AMD Instinct MI455X: CDNA 5 on TSMC N2, 12-Stack HBM4, Helios Rack

## Thesis Delta
Consensus still treats AMD as a CUDA-gap / “second-source warrant” GPU vendor whose hardware lags NVDA by a generation. STH’s Advancing-AI teardown puts MI455X on TSMC N2 GAAFET (AMD’s first N2 GPU), CDNA 5 (largest server-GPU overhaul in a decade), 12 HBM4 stacks and 23.3 TB/s bandwidth, plus Helios rack-scale with Broadcom fabric — a *parity-attempt* datapoint versus Rubin, not a software-moat collapse. Direct transmission: [[Theses/AMD - Advanced Micro Devices]] product, [[Theses/TSM - Taiwan Semiconductor]] N2+CoWoS allocation, [[Theses/AVGO - Broadcom]] Ethernet/UALink rack fabric, [[Theses/000660 - SK Hynix]] HBM4 stacks. Mental-model triggers: Industry-Semiconductors #8 (architecture remaps bottleneck — rack-scale + HBM4 + N2); [G-13] expectations (price already embeds OpenAI/Meta GW deals — this is the hardware that must deliver); Value Layer Monopoly §3 infrastructure-layer.

## Summary
ServeTheHome deep-dive, published around AMD’s 2026 Advancing AI event and circulating August 13, 2026: Instinct MI455X is the cornerstone of next-year server GPUs and Helios racks. Architecture: CDNA 5 (radically revised vs CDNA 4), TSMC N2 (2nm GAAFET) vs prior N3/N4 family, transistor count +72% vs prior gen. Memory: 12 HBM4 stacks (4 more than MI355X) → 23.3 TB/s, 2.9× MI355X bandwidth. Instinct already helps drive data-center to >50% of AMD revenue. Helios is the rack-scale system wrapping the GPU; networking emphasis is explicit. This is a *product-roadmap* article, not an earnings print — no volume, ASP, or N2-wafer allocation figures.

## Evidence
| Metric | Figure | Tag |
|---|---|---|
| Process | TSMC N2 (GAAFET) | [web: servethehome.com] |
| Architecture | CDNA 5 | [web: servethehome.com] |
| HBM4 stacks | 12 (vs 8 on MI355X) | [web: servethehome.com] |
| Memory bandwidth | 23.3 TB/s (~2.9× prior) | [web: servethehome.com] |
| Transistor count | +72% vs prior gen | [web: servethehome.com] |
| DC mix (context) | >50% of AMD revenue | [web: servethehome.com] |

## Contradiction Check
**Supports** AMD §Summary “sole merchant full-stack alternative” *if* N2+HBM4 hardware actually ships into the OpenAI/Meta 6GW deals; **does not** close the CUDA/software gap the thesis already flags as the real moat at [[Theses/NVDA - Nvidia]] §Summary. **Supports** TSM §Key Non-consensus Insights CoWoS/N2 sold-out rents (another large N2 GPU customer) and 000660 HBM4 stack count. **Challenges** any AMD bear that “Instinct never gets leading-edge process or HBM allocation.” Named sections: AMD §Summary / §Bull Case; TSM §Summary N2 premium + CoWoS; AVGO §Summary Ethernet/Tomahawk AI-fabric; 000660 §Summary HBM4 Rubin-cycle.

## Source Excerpts
> "the Instinct MI455X is not only AMD’s fastest server GPU to date, but it marks the introduction of the radically revised CDNA 5 architecture"
> "equipped the chip with 12 stacks of HBM4 memory, 4 more stacks than the MI355X"
