---
date: 2026-07-19
tags: [research, Semiconductors, LITE, COHR, AEVA, Optics]
sector: Custom Silicon & Networking Semiconductors
ticker: LITE
propagated_to: [LITE]
source: 'https://irrationalanalysis.substack.com/p/practical-semiconductor-optical-amplifiers'
source_type: deep-dive
---

## Thesis Delta
Consensus treats SOA as obscure LiDAR physics → IA argues high-power SOA becomes a pragmatic (ugly) CPO/NPO laser supply valve when UHP DFB is scarce: discrete DFB + isolator + SOA can work where monolithic MOPA mode-hops from back-reflection. Broader frame: LITE/Broadcom win on shorter cavities (linewidth + mode-hop + chips/wafer); COHR makes ~60% of world isolators; AEVA SOA ~650 mW is "quite good" but active-alignment hell (56+ alignments on 8λ ELSFP) caps margins at ~5–20% vs incumbents' ~50–65%.

## Summary
Recap of Vik's DFB physics plus IA deltas: reliability vs charge density (short cavity at same power = higher density risk) and mode-hop risk scaling with cavity length—LITE/AVGO acceptable CPO linewidth at shorter cavities than peers (~60% longer cavities elsewhere). EDFA/PDFA are excellent but large/expensive; SOA ≈ DFB without gratings—noisy, cheap, tiny. FWM in SOAs is severe with multi-λ input (junk conjugate spikes). For CPO/NPO: traditional datacom needs 20–100 mW; LiDAR SOAs at 400–650 mW enable MOPA-like boost of weak DFBs. Monolithic MOPA (Furukawa; COHR pivot after botched UHP DFB) suffers unfixable mode-hop without on-chip isolator. Discrete SOA + DFB needs isolators (COHR) and many active alignments (FiconTec-class). Sell-side pinging AEVA; IA skeptical of LiDAR names generally but rates Aeva SOA performance.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| Traditional long-haul power | 20–100 mW | [1×: IA] |
| AEVA SOA rating | ~650 mW; good WPE/low ASE | [1×: IA] |
| Incumbent ELSFP GM | ~50–65% | [est.: IA] |
| LiDAR-SOA ELSFP GM | ~5–20% | [est.: IA] |
| 8λ ELSFP alignments (SOA path) | 56+; 32–40 lenses; 8–16 isolators | [est.: IA napkin] |
| COHR isolator share | ~60% world | [est.: IA] |
| Peer cavity vs LITE/AVGO | ~+60% length | [1×: IA] |

## Contradiction Check
Reinforces LITE/AVGO laser moat and COHR isolator adjacency; frames AEVA as optionality not core. Falsifiers: monolithic MOPA reliability solved; UHP DFB supply normalizes; discrete SOA economics never clear active-alignment cost.
