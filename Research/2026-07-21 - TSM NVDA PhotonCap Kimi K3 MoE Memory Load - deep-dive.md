---
publish: false
date: 2026-07-21
tags: [research, Semiconductors, TSM, NVDA, MU]
sector: Foundry & Logic Semiconductors
ticker: TSM
propagated_to: [NVDA, TSM]
source: 'https://photoncap.net/p/kimi-k3s-active-set-is-50b-class'
source_type: deep-dive
updated: 2026-08-14
---

# Kimi K3's Active Set Is 50B-Class

## Thesis Delta
Consensus priced Kimi K3 as a DeepSeek-rerun "cheap open model kills AI capex" shock — [[Theses/TSM - Taiwan Semiconductor]] printed NI +77.4% then TW −7.3% / ADR −2.8% the next session — → PhotonCap's public-spec arithmetic shows K3 cuts per-token compute while raising memory and communication load: ~50–60B active of 2.8T, MXFP4 weight floor ~1.4TB (FP8-class ~2.8TB), a 1M-context KV term, and a widening total-vs-active gap (totals ~4.2× / actives ~1.4× in 19 months) that maps onto die / package / rack / campus / test rather than fewer GPUs. [G-13] the mispriced variable is resident bits and scale-up domain size, not token list price; [G-10] / [G-14] the January 2025 DeepSeek tape already ran this experiment and hyperscaler capex did not follow the selloff down.

## Summary
PhotonCap maps K3's *memory load*, not its kernels. Cutoff is 20 July 2026 — weights and the technical report still unpublished (promised 27 July) — so this note is the resident-set / supply-chain half; [[Research/2026-08-03 - Kimi K3 Architecture Inference Performance - deep-dive]] is the post-weight architecture/TCO half. The 17 July tape treated a cheap API or downloadable frontier model as a reason to spend less on silicon: TSMC's 16 July print (EPS NT$27.25, NI +77.4% YoY) was sold TW −7.3% / ADR −2.8%, SoftBank −9%, NDX −1% intraday, [[Theses/NVDA - Nvidia]] briefly ceded largest-cap to Apple. PhotonCap calls K3 the amplifier of an already-built capex caution, then takes Damnang as given: open models compress the lab software premium and move value to hyperscalers plus the semiconductor stack. January 2025 DeepSeek already ran the experiment; cheaper model did not show up as cheaper infrastructure in subsequent capex guides.

The title is Calculation 1. Official spec: 2.8T total, 16 of 896 experts, 1M context, MXFP4 weights / MXFP8 activations from SFT. Active count is unofficial (~50–60B, Ken Huang). 2.8T × 16/896 ≈ 50B only if every parameter lives in a routed expert; the 2.8T also holds always-on attention, embeddings, routing, and shared paths, so the right expression is common + 16/896 of routed — uncomputable from the public split. 2.8T × 0.5 bytes ≈ 1.4TB is a theoretical MXFP4 *floor* (scales, alignment, comm buffers stripped); FP8-class is 2.8TB. Versus B300 288GB HBM3E that is 5 / 10 GPUs of *nominal* HBM, not a minimum deploy — KV, activations, and parallelism stack on top, and Moonshot recommends 64+ accelerator supernodes. One FP8-class copy is >13% of a GB300 NVL72's ~20.7TB rack HBM as a resident. K2 was 1.04T (2.7× totals in twelve months). 1.8% expert-activation is not 1.8% of FLOPs. Offload is possible; the price is latency and throughput.

Calculation 2 splits cost type: weights are fixed per replica; KV/state is variable in sessions × context. The 123GB number is a GQA *counterfactual* (author-assumed 60 / 8 / 128 / FP8 / 1M), >40% of one B300 for a single conversation — not K3's hybrid KDA + Gated MLA figure, which the cutoff cannot size. Labs spent two years saving bits (MLA, KDA, MoE sparsity, MXFP4), and each prior compression step was filled by longer context and more concurrency. Calculation 3 is the largest-open-MoE snapshot series only: DeepSeek-V3 671B/37B/5.5% → K2 1.04T/32B/3.1% → K3 2.8T/50–60B/1.8–2.1%, Qwen3.8-Max-Preview 2.4T the same weekend. Nineteen months: totals 4.2×, actives 1.35–1.62×, activation 5.5% → ~2%. Forces: export-control FLOP scarcity (squeeze compute, architecture grows toward memory); a total-scale race with no stop incentive; self-hosting that, if 27 July weights land, recreates lab serving demand in enterprises and sovereign clouds. Direct opposite of the selloff logic arrived 19 July: Moonshot paused new subscriptions inside 48 hours on cluster limits.

Five exposures run in parallel, not in sequence. Die: more resident bits → DRAM wafers + HBM base/logic dies + SiPh. Package: total bits shipped, not $/bit; BW/latency/pJ can bind before GB does. Rack: 896-expert all-to-all plus the 64+ supernode rec makes scale-up domain bandwidth the serving lever (InP where copper dies). Campus/DCI turns on only if hosting splits sites. Test is cross-cutting. The 17 July multiple applied model-premium compression and HBM/optics/foundry demand as if they pointed the same way. Author weakeners: expert cache better than expected, another quant step, self-hosting stuck in cloud APIs, KDA cutting far deeper versus the GQA baseline than assumed.

## Framework / Mental Model

PhotonCap names four reusable frames (Damnang's is imported; the other three are this piece's method).

| Frame | Components | How it is applied |
|---|---|---|
| **Damnang open-model / hardware-demand** | Open weights compress the frontier-lab software premium; value migrates to hyperscalers + the semiconductor stack | Taken as given. K3 is the worked example, not a re-derivation. January 2025 DeepSeek is the prior experiment: cheaper model ≠ cheaper infrastructure. |
| **Three-calculation spec audit** | (1) weight-memory floor from total params × bits; (2) KV as a GQA counterfactual, not as K3's hybrid number; (3) largest-open-MoE time series of total vs active | Separates official spec from estimate. Calc 1 is a floor (buffers stripped). Calc 2 is labelled counterfactual. Calc 3 excludes dense models and small MoE. |
| **Active-set vs resident-set (library)** | Books on the desk = params touched this token. Shelves / waiting-room librarians = the full expert pool that must stay reachable because the next token can call any of 896 | Compute tracks the 16 at work. Memory tracks room size. 1.8% expert-activation ≠ 1.8% of FLOPs (attention, router, shared paths stay on). |
| **Five-layer exposure map (die → test)** | Die (foundry wafers: DRAM + HBM base/logic + SiPh). Package (HBM bits + BW/latency/energy). Rack (scale-up domain + InP). Campus (coherent DCI, multi-site switch). Test (cross-cutting) | Parallel exposures, not a sequence. Land-grab first where lead times are longest (foundry). Volume first where demand tracks usage (HBM, scale-up optics). DCI is off until hosting splits sites. |

## Evidence

### Official spec vs estimates (data cutoff 2026-07-20)

| Item | Figure | Tag |
|---|---|---|
| K3 release | 2026-07-16 | [1×: Moonshot via PhotonCap] |
| Total parameters | 2.8T | [1×: Moonshot / PhotonCap] |
| Routed experts | 16 of 896 (1.8% of expert pool) | [1×: Moonshot / PhotonCap] |
| Context | 1M tokens | [1×: Moonshot / PhotonCap] |
| Training quant | MXFP4 weights, MXFP8 activations, QAT from SFT | [1×: Moonshot / PhotonCap] |
| Active params | ~50–60B (unofficial; report unpublished) | [1×: Ken Huang via PhotonCap] |
| Naive routed arithmetic | 2.8T × 16/896 ≈ 50B (assumes uniform routed split; ignores common params) | [est.: PhotonCap] |
| Correct active expression | common + 16/896 of routed; split undisclosed | [1×: PhotonCap] |
| Weight floor, MXFP4 | 2.8T × 0.5 B ≈ 1.4TB (raw payload; no scales/align/buffers) | [est.: PhotonCap] |
| FP8-class weight copy | ~2.8TB | [est.: PhotonCap] |
| Serving recommendation | supernodes of 64+ accelerators; larger high-BW domains raise inference efficiency | [1×: Moonshot via PhotonCap] |
| Weight drop promised | 2026-07-27; license unannounced at cutoff | [1×: Moonshot via PhotonCap] |

### Accelerator geometry

| Item | Figure | Tag |
|---|---|---|
| B300 / GB300 HBM3E | 288GB / GPU | [1×: NVIDIA via PhotonCap] |
| MXFP4 floor / B300 | 1.4TB ÷ 288GB ≈ 5 GPUs of nominal HBM (not min deploy) | [est.: PhotonCap] |
| FP8-class / B300 | 2.8TB ÷ 288GB ≈ 10 GPUs of nominal HBM (not min deploy) | [est.: PhotonCap] |
| GB300 NVL72 rack HBM | 72 × 288GB ≈ 20.7TB | [est.: PhotonCap from NVIDIA 288GB] |
| One FP8-class K3 copy / NVL72 | >13% of nominal rack HBM as a resident | [est.: PhotonCap] |
| K2 → K3 totals | 1.04T → 2.8T = 2.7× in 12 months | [1×: Moonshot K2 arXiv + K3 spec via PhotonCap] |

### KV counterfactual (not K3's hybrid number)

| Item | Figure | Tag |
|---|---|---|
| Formula | 2 (K,V) × layers × KV heads × head dim × context × precision | [1×: PhotonCap] |
| Assumed GQA config | 60 layers, 8 GQA KV heads, d=128, FP8, 1M tokens | [est.: PhotonCap] |
| One 1M-token session | ~123GB | [est.: PhotonCap] |
| Share of one B300 | >40% of 288GB HBM | [est.: PhotonCap] |
| K3 actual KV | Hybrid KDA + Gated MLA; reduction vs 123GB unquantified at cutoff | [1×: PhotonCap] |
| Weight vs KV cost type | Weights = fixed per replica; KV/state = variable in sessions × context | [1×: PhotonCap] |

### Largest open-weight MoE snapshots (not all open models)

| Date | Model | Total | Active | Activation | Tag |
|---|---|---:|---:|---:|---|
| Dec 2024 | DeepSeek-V3 | 671B | 37B | 5.5% | [1×: DeepSeek-V3 report via PhotonCap] |
| Jul 2025 | Kimi K2 | 1.04T | 32B | 3.1% | [1×: K2 arXiv via PhotonCap] |
| Jul 2026 | Kimi K3 | 2.8T | 50–60B | 1.8–2.1% | [1×: Moonshot + Ken Huang via PhotonCap] |
| Jul 2026 (same weekend) | Qwen3.8-Max-Preview | 2.4T | — | — (open-weight planned) | [1×: Reuters via PhotonCap] |
| 19-month slope | V3 → K3 | totals **4.2×** | actives **1.35–1.62×** | 5.5% → ~2% | [est.: PhotonCap] |

### Tape, DeepSeek analog, demand signal

| Item | Figure | Tag |
|---|---|---|
| TSMC Q2 print | 2026-07-16; EPS NT$27.25; quarterly NI +77.4% YoY | [1×: TSMC PR via PhotonCap] |
| Next session | TW −7.3%; $TSM ADR −2.8% (NYSE 2026-07-17); SoftBank −9%; NDX −1% intraday; NVDA briefly lost #1 mcap to AAPL | [1×: Bloomberg / Fortune via PhotonCap] |
| Prior experiment | Jan 2025 DeepSeek: "cheaper model → less infra" did not appear in subsequent hyperscaler capex guides | [1×: PhotonCap] |
| Subscription pause | 2026-07-19: new Kimi subs paused; demand hit cluster limits inside 48h; compute reserved for paid users | [1×: Reuters via PhotonCap] |
| Export-control force | US compute controls named as a reason Chinese labs choose sparse MoE | [1×: Reuters via PhotonCap] |

### Five-layer map (parallel, not sequential)

| Layer | What K3 loads | First tell | PhotonCap prior |
|---|---|---|---|
| Die (foundry) | DRAM wafers + HBM base/logic dies + SiPh wafers | Capacity reservations (year lead times) | *Everyone Saw a Laser Shortage. The Money Went to the Foundries First.* |
| Package (HBM) | Total bits shipped; BW / latency / pJ/bit can bind before GB does | HBM production / attach | *The More Anthropic Buys Micron HBM, the Faster Optical Memory Pooling Arrives* |
| Rack (scale-up + InP) | 896-expert all-to-all; 64+ supernode domains | Rack networking / InP | *The More Silicon Wins, the More InP Sells* |
| Campus (coherent DCI) | Multi-site self-host / inference split | Site-to-site traffic; off if single-DC | *One Layer Below SemiAnalysis's Meta Map* |
| Test (cross-cut) | Every new HBM stack and optical link | Test-equipment orders | *Compute Is the New Oil. So Who Builds the Drilling Rigs?* |

## Contradiction Check
Supports [[Theses/TSM - Taiwan Semiconductor]] §Key Non-consensus Insight #1 CoWoS-as-annuity and §Summary durability-of-monopoly over the next print: a 2.8T resident set plus Moonshot's 64+ supernode recommendation is more CoWoS sites per replica, and more HBM stacks per replica, even as 16-of-896 sparsity cuts per-token FLOPs. The 16 July beat / 17 July −7.3% TW / −2.8% ADR tape is the same "market declined to pay" event already logged on the Q2 print. Does not fire §Conviction Triggers → LOW (any 2027 HPC <10% YoY; GM <63% for two quarters; named production-scale CoWoS-alternative). Watch the author weakeener that would compress packaging intensity per token: expert offload plus another quant step that collapses the 1.4TB floor.

Challenges [[Theses/NVDA - Nvidia]] §Outstanding Questions "algorithmic efficiency overwhelm Jevons" and §Risks #3 compound-efficiency overshoot: K3 is the worked case of [G-14] where per-token compute falls and memory + communication load rises, and the builder paused new subs inside 48 hours. Supports §Summary's open-weight-as-workload-generator reading and the software-stack requirement (64+ scale-up domain, all 2.8T reachable). NVDA has **no Conviction Triggers section** to pin; this source does not measure CUDA share, MLPerf, or ASIC substitution. Session color only: NVDA briefly lost largest-cap to Apple on 17 July. Complement, not substitute, for [[Research/2026-08-03 - Kimi K3 Architecture Inference Performance - deep-dive]]: that note prices KDA decode as constant in T and InferenceX at $0.1712/M on one B300 + DRAM offload; this note prices the **weight floor** that sets leftover HBM before any KV math starts. SemiAnalysis already cites this file's ~1.4TB MXFP4 class as that floor.

Supports [[Theses/000660 - SK Hynix]] §Summary $30B HBM book on the bits-shipped (not $/bit) variable, and does **not** fire §Conviction Triggers → LOW (Samsung Rubin >35% in Q3–Q4 2026) — vendor share is unmeasured. Challenges any "open MoE shrinks HBM units" reading of that book: the resident set grew 4.2× while actives grew ~1.4×, so instance **count** can stay high while KV-HBM **per token** is a separate (later) question. Does not promote Insight #3 HBF: PhotonCap never names a flash inference tier.

Supports [[Theses/MU - Micron Technology]] Insight "mix-shift dollars exist without Rubin cubes" only on the demand line: more resident bits is HBM/DRAM wafer pull independent of first-wave Rubin board share. Does **not** promote MU and does not fire → HIGH (Q3 board meter ≥10% **and** LTA-cap removal **and** two TrendForce prints). Source never names a memory vendor for K3 serving. Semis L1 (DRAM less cyclical) stays a hypothesis; a 1.4TB weight floor is one more contracted-looking use of HBM bits, not a destock falsifier.

Mental-model triggers held as hypotheses, not verdicts: [G-13] tape applied one multiple to model-premium compression and to HBM/optics/foundry demand; [G-10] reference class is DeepSeek Jan 2025, not a new regime; [G-14] 48-hour cluster saturation is the labour-to-compute unlock firing in the opposite direction of the selloff; [G-3] do not apply mean-reversion ("efficiency → less silicon") to a class still racing on total params; [G-4] frenzy-funded GPU/HBM/optics capacity is the substrate this software harvests. Semis #8 architecture remap (compute-bound → memory/interconnect-bound as activation falls 5.5%→~2%); Semis #1 re-identify the binding segment (resident HBM bits + 64+ scale-up domain + foundry wafers, not last cycle's GPU-FLOP shortage); Semis #18 do not read a 50B-class active set as "AI demand is dead."

## Source Excerpts

> "The conclusion the public spec supports: K3 cuts per-token compute while raising memory and communication load at the same time."

> "A naive conversion at 4 bits per parameter gives 2.8T x 0.5 bytes = about 1.4TB. That number is not a conservative estimate. It is a theoretical floor: raw payload with scale metadata, alignment, and communication buffers stripped out. The actual serving footprint is larger. At FP8-class precision, the figure is 2.8TB."

> "Only 16 of the 896 librarians are working, but since nobody knows which one the next visitor will ask for, all of them have to sit in the waiting room. Compute cost tracks the 16 at work. Memory cost tracks the size of the room."

> "On July 19, Moonshot paused new subscriptions, saying K3 demand had approached the limits of its existing clusters within 48 hours, and allocated available compute to existing paid users."

> "Even granting those conditions, this correction is discounting the model layer's premium compression and the demand for HBM, optical interconnect, and foundry capacity at the same multiple. I do not think those two point the same way."
