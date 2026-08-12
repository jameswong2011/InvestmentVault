---
date: 2026-08-11
tags: [research, Semiconductors, MU, NVDA, HBM]
sector: DRAM & HBM Memory
ticker: MU
propagated_to: [LITE]
source: 'https://damnang2.substack.com/p/what-does-rubin-ultras-8-hi-hbm-mean'
source_type: deep-dive
---

## Thesis Delta
Consensus reads NVIDIA’s Rubin Ultra HBM4 **8-Hi despec** as a memory-cycle break / HBM revenue cliff → Damnang argues it is a **sold-out-market volume unlock**: NVIDIA cuts stack height to build more GPUs from scarce HBM, offset by NPO multi-rack scale-up (NVL576) and software (Wide EP, DWDP, Helix, Dynamo). Revenue math: total HBM revenue can hold **81.5–98%** of planned 4E if output gains (≤1.63×) offset price/mix down. Relative winners: Samsung (standard 8-Hi yield/capacity), optics/scale-up (ALAB, MRVL, COHR, LITE, MACOM); Hynix faces delayed 4E/custom premium. Touches [[Theses/NVDA - Nvidia]], [[Theses/000660 - SK Hynix]], [[Theses/MU]], [[Theses/LITE - Lumentum]].

## Summary
Drivers of 8-Hi vs 12-Hi HBM4E: (1) HBM4E ~16Gbps pin-speed quals struggling while HBM4 already at 10–11Gbps; (2) DRAM supply constraint through 2027. Capacity path: GTC’25 1,024GB → successive cuts to ~192GB/GPU. Performance compensation is **range not speed**—NPO extends NVLink domain 72→576 GPUs; peer HBM still far slower than local (~21–22TB/s vs 3.6TB/s NVLink6). Software keeps MoE weights/KV on local HBM while distributing the rest. Author rejects “cycle broken” framing; reads as supplier–customer coordination on price, volume, and design.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| Rubin Ultra HBM config (reported) | 8-Hi HBM4 ~192GB | [1×: Damnang / field] |
| Prior planned | 12-Hi HBM4E ~384GB class | [1×: Damnang] |
| Local HBM BW | ~21–22 TB/s | [1×: Damnang] |
| NVLink6 GPU-GPU | 3.6 TB/s | [1×: Damnang] |
| Scale-up domain | NVL72 → NVL576 via NPO | [1×: Damnang] |
| Stacking output sensitivity | up to ~1.63× (1.5× layers × ~1.084× yield) | [est.: Damnang] |
| HBM rev vs planned 4E | 81.5% (half $/GB) to 98% (die-ratio pricing) | [est.: Damnang] |
| Relative beneficiary | Samsung among memory three | [1×: Damnang] |

## Contradiction Check
Challenges bear narrative that despec = HBM ASP collapse / cycle end. Supports [[Theses/NVDA - Nvidia]] vertical-integration moat (optics+software enable the despec). Partial challenge to SK hynix premium-mix timeline. Falsifiers: packaging/rack bottleneck prevents volume uplift; HBM4E quals clear fast and 8-Hi is abandoned; NPO slip.

## Framework / Mental Model
**Despec as volume unlock under sold-out HBM**: when bits are binding, lowering stack height raises stack count and can raise total $ if price falls less than volume rises—especially when the buyer can compensate capacity with scale-up fabric + software.
