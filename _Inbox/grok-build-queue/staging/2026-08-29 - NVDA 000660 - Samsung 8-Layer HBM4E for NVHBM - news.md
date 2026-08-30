---
publish: false
date: 2026-08-29
tags: [research, daily-intel-triage, news, NVDA, 000660]
sector: DRAM & HBM
ticker: NVDA
source: 'https://sammyfans.com/2026/08/28/samsung-develops-8-layer-hbm4e-for-nvidia-nvhbm'
propagated_to: [NVDA, 000660]
source_type: news
---

# Samsung Building 8-Layer HBM4E for Nvidia NVHBM (SEDaily via SammyFans)

## Thesis Delta
Consensus still models NVHBM as “taller stacks + custom base die.” SEDaily (via SammyFans) says Nvidia asked Samsung for **8-Hi HBM4E** at **17–18 Gbps/pin** (vs Samsung’s 16 Gbps samples), **instead of 12-/16-Hi** it had been preparing — prioritizing shippable bits, thermals, and speed over height. Controller-in-base-die NVHBM claims **~30% BW / ~15% power** vs commodity HBM4E. For held [[Theses/000660 - SK Hynix]] this is a **mix-shift / competitive** signal (Samsung as NVHBM supplier path); for [[Theses/NVDA - Nvidia]] it reinforces NVLink Fusion custom-memory control. Single-source trade press — treat as unverified until SK Hynix/Samsung primaries.

## Summary
SammyFans relays SEDaily: Nvidia asked Samsung to tailor HBM4E around an 8-layer stack for NVHBM rather than taller 12-/16-layer stacks. Target pin speed 17–18 Gbps vs Samsung’s initial 16 Gbps HBM4E samples. NVHBM (with NVLink Fusion) moves the memory controller into the HBM base die, freeing XPU area; claimed up to ~30% higher bandwidth and ~15% lower HBM power vs standard HBM4E. Piece says 8-layer NVHBM is being considered for future platforms including Vera Rubin Ultra. Notes Samsung’s integrated DRAM/logic/packaging/foundry stack as a fit for controller-in-base-die work.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Stack height ask | 8-Hi HBM4E for NVHBM (not 12/16-Hi) | [1×: SEDaily via sammyfans.com] |
| Pin speed | 17–18 Gbps vs 16 Gbps samples | [1×: SEDaily via sammyfans.com] |
| NVHBM claims | ~+30% BW / ~−15% power vs HBM4E | [1×: sammyfans.com] |
| Platforms named | Vera Rubin Ultra (reportedly) | [1×: sammyfans.com] |
| Source quality | Secondary (SEDaily → SammyFans) | [est.] |

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] NVHBM / NVLink Fusion custom-memory thesis (see prior Converge Digest / Nvidia blog notes). **Competitive pressure** on [[Theses/000660 - SK Hynix]] if Samsung locks 8-Hi NVHBM sockets — or validation that 8-Hi mix is industry-wide (Digitimes also flagged Nvidia 8-Hi HBM4 mix). Low confidence until primary confirmation. No conviction/status change.

## Source Excerpts
> "NVIDIA has asked Samsung to tailor its seventh-generation HBM4E around an 8-layer configuration for NVHBM, rather than the taller 12-layer and 16-layer stacks" [1×: SEDaily via sammyfans.com]

> "target speeds of 17 to 18Gbps per pin… above Samsung’s initial HBM4E sample specification of 16Gbps." [1×: sammyfans.com]
