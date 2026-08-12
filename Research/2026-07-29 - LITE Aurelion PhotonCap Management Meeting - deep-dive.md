---
date: 2026-07-29
tags: [research, Semiconductors, LITE, Optics, CPO]
sector: Optical Networking & Photonics
ticker: LITE
propagated_to: [LITE]
source: 'https://photoncap.net/p/a-conversation-with-lumentum'
source_type: deep-dive
---

## Thesis Delta
Consensus debates whether LITE is a crowded optics supercycle that fades with capacity → Aurelion IR meeting + PhotonCap technical overlay argue the durable edge is **qualified high-power usable yield** (RIN/COD/SMSR/FIT at temperature), not headline EML scarcity, while CPO scale-up is a second S-curve (~late-2027) that can coexist with copper on a power-budget cost curve. Updates [[Theses/LITE - Lumentum]] with management framing: 8× EML capacity in ~2.5 years is real but overstates relief vs top-bin yield; copper "wall" ~late 2027 at ~3m practical reach; three defenses (power ratings, telecom survivorship, China yield gap) with PhotonCap sharpening which are durable.

## Summary
Aurelion met Kathryn Ta (VP IR). Lumentum optimizes power-per-bit via higher-power lasers; two Japan fabs dominate world EML supply with capacity ~8× in 2.5 years; five fabs total including a new ramp not yet producing wafers. CPO today is opportunistic (power freed for GPUs), not forced by copper exhaustion; copper impractical beyond ~3m at rising lane rates despite Credo/Broadcom 6m claims. Competitive defenses: 150–400 mW high-volume lasers thin competition; telecom reliability heritage vs Coherent systems-strong/components-catching-up; internal China laser comparisons show better yield/uniformity/reliability (unverified externally). Architecture-agnostic bet on InP laser chips first, MEMS/OCS second (Google spine/cluster). PhotonCap product map: EML = today's cash flow (modulated InP); high-power CW = CPO/SiPh external light (NVIDIA path); GaAs VCSEL hedge for chip-to-chip (OFC 2026 1060nm arrays). Bull stack: >30% supply gap, LTAs through FY27, scale-up CPO under-modeled, channel CW laser guides (Global Semi Research ~40M→100M units). Bear stack: Coherent 6" InP (~2.25× area), SemiAnalysis CPO delay (scale-up to FY29), Chinese EML progress (Zetta 100G/200G samples), 2028 capacity landing into softer demand, customer concentration (26%/12% top two in FQ3'26) + NVIDIA dual role. Note: interview answers paraphrased; free article ends before paid basket details if any.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| EML capacity add | ~8× in ~2.5 years (Japan fabs) | [1×: IR / Aurelion] |
| Fab count | 5 InP fabs (1 new ramp) | [1×: IR] |
| Copper practical wall | ~late 2027 / ~3m | [1×: IR paraphrase] |
| Power range cited | 150–400 mW class | [1×: IR] |
| EML market share (Aurelion) | ~60%; sole 200G volume | [est.: Aurelion] |
| NVIDIA convert | $2B + multi-year buy | [1×: known / article] |
| Supply gap (mgmt) | ~30% demand > supply | [1×: mgmt via article] |
| Top customers FQ3'26 | 26% + 12% | [1×: article] |
| CW laser channel (GSR) | ~40M → ~100M units | [est.: Global Semi Research] |

## Contradiction Check
**Supports** [[Theses/LITE - Lumentum]] arms-dealer / physics-gated framing and CPO-as-incremental-TAM. PhotonCap explicitly softens pure-scarcity: 8× capacity + Coherent/Sumitomo/AAOI CW second-sourcing outside FY27 LTA window. Falsifiers: Coherent 6" closes parametric tails; CPO ASIC delay without pluggable offset; China high-power yield catches hyperscale quals before 2028.

## Framework / Mental Model
Optical architecture ladder: pluggable DSP → LPO → NPO → CPO; delay on a higher rung keeps traffic (and EML content) on the rung below. Moat = qualified usable power × spectral quality × reliability × HVM yield — not peak-power datasheet.

## Source Excerpts
> "Wafer starts and qualified yield at the newest spec are different numbers... the binding constraint is yield at the highest power bins, not floor space."
> "Copper's limit is not a date. It is a cost curve of reach, speed, and power."
