---
date: 2026-08-04
tags: [research, Semiconductors, MPWR, Power]
sector: MLCC & Power Semiconductors
ticker: MPWR
propagated_to: [6981, VICR]
source: 'https://damnang2.substack.com/p/the-power-delivery-bottleneck-in'
source_type: deep-dive
---

## Thesis Delta
Consensus lumps "power" as grid/turbines → Damnang separates campus megawatts from board-level delivery: GPUs at >1kW/<1V force kiloamp currents where I²R loss and transient sag dominate. Near-term stack: MPWR (volume LPD/hybrid), Vicor (VPD density + patents), Murata/SEMCO (MLCC oligopoly). LPD-centered hybrid likely holds 2–3 years. Links [[Theses/6981 - Murata Manufacturing]] and Data Center Power sector notes.

## Summary
Two failure modes: resistive loss ∝ I² and load-step voltage sag. Fixes: shorten path (48V→PoL, LPD vs VPD) and local capacitance (hundreds of thousands of MLCCs per NVL72-class rack). MPWR enterprise data ~2.6× YoY; growth guide floor 85%→130%. Vicor ~17× sales on 1.5mm VPD modules; fab2 groundbreaking resets math. MLCC: Murata backlog ¥617.8B; SEMCO +30% Aug prices. Cycle risk: capacity + consumer recovery mean-reverts prices (2022 template).

## Evidence
| Item | Figure | Tag |
|---|---|---|
| GPU power / voltage | >1kW / <1V | [1×: Damnang] |
| MPWR enterprise data | ~2.6× YoY | [1×: Damnang / MPWR] |
| MPWR growth guide floor | 130% | [1×: Damnang] |
| Vicor 2nd-gen thickness | ~1.5mm vs ask ≤3mm | [1×: Vicor call / Damnang] |
| Murata capacitor backlog | ¥617.8B | [1×: Damnang] |
| SEMCO price hike | +30% Aug shipments | [1×: Damnang] |

## Contradiction Check
Challenges "own utilities or miss the power trade." Supports component-level scarcity. Falsifiers: VPD arrives faster than expected; MLCC capacity clears; GPU current density stalls.

## Framework / Mental Model
Three-scale power map: campus GW vs rack MW vs chip kW@<1V. Delivery bottleneck is current-density physics; converters and MLCCs are the equity expressions.
