---
publish: false
date: 2026-08-06
tags: [research, AI Infrastructure, MU, LITE, MRVL]
sector: Compute & AI Compute Accelerators
ticker: MU
propagated_to: [CRWV, LITE, MU]
source: 'https://photoncap.net/p/the-gpu-repricing-cycle-and-q2-hyperscaler'
source_type: deep-dive
---

## Thesis Delta
Consensus frets hyperscaler FCF burn from AI capex → PhotonCap (Baker underearning frame) argues hyperscalers are landlords on below-market GPU leases; early repricing + usage-above-commit accelerates OCF. Hardware benefit sticks longest in non-insourcable L3 memory and L4 optics/DCI (MU, SK hynix, MRVL, CIEN, COHR, LITE). Supports [[Theses/MU]], [[Theses/LITE - Lumentum]], [[Theses/MRVL - Marvell Technology]], [[Theses/CRWV - CoreWeave]].

## Summary
July stack: GOOGL Cloud +82% / $514B backlog; MSFT Azure +43% / FY27 capex ~$255–260B; AMZN AWS +37% / 2026 capex ~$220B; META floor raised to $130–145B. Repricing evidence: GCP customers ~50% above commitments; Oracle $75B customer-prepaid/supplied GPUs in RPO. Memory ~30% of DC investment (36% next year). Gates: Nebius 8/12, MU late-Sep, hyperscaler Q3 late-Oct.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| GCP rev / YoY | $24.77B / +82% | [1×: Alphabet / PhotonCap] |
| GCP backlog | $514B | [1×: PhotonCap] |
| MSFT FY27 capex | $255–260B | [1×: PhotonCap] |
| AMZN 2026 capex | ~$220B | [1×: PhotonCap] |
| META FY capex | $130–145B | [1×: PhotonCap] |
| GCP usage vs commit | ~+50% | [1×: secondary via PhotonCap] |
| Oracle prepaid GPUs | $75B of RPO | [1×: Oracle / PhotonCap] |
| Spot vs contract GPU | ≥2× | [1×: Gavin Baker] |

## Contradiction Check
Challenges "capex unsustainable" narrative. Aligns with memory+optics bottleneck theses. Falsifiers: usage-above-commit rolls over; backlog stalls; cloud GM fails to rise on renewals.

## Framework / Mental Model
Baker underearning / rent-stabilized compute: spot ≫ contract ⇒ installed base earns below market until renewals; residual scarcity rents accrue to L3/L4.
