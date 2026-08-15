---
publish: false
date: 2026-07-21
tags: [research, Semiconductors, TSM, NVDA, MU]
sector: Foundry & Logic Semiconductors
ticker: TSM
propagated_to: [NVDA, TSM]
source: 'https://photoncap.net/p/kimi-k3s-active-set-is-50b-class'
source_type: deep-dive
---

## Thesis Delta
Consensus priced Kimi K3 as another DeepSeek-style "cheap model kills capex" shock (TSM -7.3% TW / ADR -2.8% day after +77.4% NI) → PhotonCap shows K3 cuts per-token compute while raising memory and communication load: ~50–60B active of 2.8T MoE, ~1.4TB MXFP4 weight floor (~2.8TB FP8-class), 1M context KV, and maps load to die/package/rack/campus/test. Open models compress frontier software premium, not the semiconductor stack.

## Summary
K3 activates 16/896 experts; official active count undisclosed—~50B arithmetic estimate. Weight floor 2.8T×0.5B ≈ 1.4TB ignores scales/buffers; vs B300 288GB HBM that is ≥5 GPUs raw, ≥10 at FP8-class; >13% of a GB300 NVL72's ~20.7TB nominal HBM for one FP8-class copy. Widening MoE pattern: total params ~4× in 19 months vs active ~1.4×. Piece is free full-text. Follows Damnang frame that open models move value to hyperscalers + infra.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| K3 total / experts | 2.8T; 16 of 896 | [1×: Moonshot / PhotonCap] |
| Active params (est.) | ~50–60B | [est.: Ken Huang / PhotonCap] |
| Weight floor MXFP4 | ~1.4TB | [est.: PhotonCap] |
| B300 HBM | 288GB/GPU; NVL72 ~20.7TB | [1×: NVIDIA via PhotonCap] |
| TSM Q print / next day | NI +77.4%; TW -7.3% / ADR -2.8% | [1×: PhotonCap] |

## Contradiction Check
Challenges "open MoE shrinks foundry/HBM demand." Falsifiers: serving footprints collapse via better quantization/offload; hyperscalers cut capex guides after open-weight waves.
