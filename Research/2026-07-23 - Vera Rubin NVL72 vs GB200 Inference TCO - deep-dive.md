---
publish: false
date: 2026-07-23
updated: 2026-08-14
tags: [research, Semiconductors, NVDA]
sector: Semiconductors
ticker: NVDA
propagated_to: [NVDA]
source: 'https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference'
source_type: deep-dive
---

# Vera Rubin NVL72 vs GB200 NVL72? Inference TCO & Architecture Analysis

## Thesis Delta

Consensus (and [[Theses/NVDA - Nvidia]] §Summary) prices Vera Rubin as a production H1-2026 refresh that already delivers **10x lower inference cost vs Blackwell** → this SemiAnalysis InferenceX / AI-TCO piece implies the 10x is a **2025-GB200, year-old-stack marketing baseline at ~150 tok/s/user**, while the buy-today comparison is **~1.5–3x cheaper $/M output tokens vs July-2026 GB200/GB300 through 250 tok/s/user**, and the 5.4x / 5x prints at 300 tok/s/user are GB300’s last barely-viable frontier point, not Rubin pulling away. [G-10] / [G-13]: treat the 10x as a priced expectation to test — and do not import this source’s **$3.57 / $1.84 / $2.36 operator-ownership TCO per GPU-hour** into the vault cash-rent model in [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]].

## Summary

Vera Rubin NVL72 is the second-generation Oberon rack. SemiAnalysis’s claim is that inference gains come from **extreme co-design** (SM107 microarchitecture + HBM4 + cableless tray + copper-backplane learnings + CUDA 13.4 kernel reuse), not a FLOPs-marketing step, and that early CoreWeave engineering-sample results already show a **performance-per-MW and performance-per-dollar curve that widens at high interactivity** — the “fast mode” band Blackwell cannot occupy. Headline ES numbers on DeepSeek R1: **5.4x tok/s per all-in utility MW and 5x performance per dollar vs GB200 NVL72 “today”**, wider still versus GB200’s 2025 bring-up. Rubin itself is still in early bring-up; the house prior is that the gap **widens** as kernels mature, repeating the Blackwell InferenceX path. Nvidia has published the first public Rubin (SM_107) stack (CUDA 13.4) and upstreamed PRs to PyTorch, vLLM, and OpenAI Triton. Blackwell could not reuse Hopper WGMMA kernels; **Rubin can reuse Blackwell SM100-family kernels** (DeepGEMM, FlashMLA, CUTLASS), which buys time-to-market even though speed-of-light still needs Rubin-specific rewrites. Feynman is disclosed on GitHub as **SM_140** — a new architecture family, not a kicker; Rubin→Feynman is the Hopper→Blackwell-class kernel rewrite. [G-6] / Industry #2 / VLM interface-control: kernel ABI inheritance is the lock-in mechanism this source actually measures. [Industry #4]: Rubin is framed as a **Blackwell kicker**; Feynman is the real tech-curve race.

Metrics on the chart are **CoreWeave’s**, on a **Dell Engineering Sample rack with no scale-out fabric**, and SemiAnalysis has **not independently verified** them. Nvidia has committed **verifiable InferenceX numbers by Q3 CY2026**; Google is expected to submit TPUv7 in the following months; AMD has committed **MI455X UALoE72**. The analytical move is to **renormalize InferenceX July-2026 GB200/GB300 results onto CoreWeave’s total-GPU, output-tokens-only, prefill+decode-watts convention** and then split the 2025-GB200 marketing baseline from the July-2026 installed-base baseline. Three chart artefacts inflate the Nvidia/CoreWeave 10x: (1) single-turn **8k in / 1k out**; (2) y-axis is **output** tok/s/MW, not total tokens; (3) the MW denominator **includes prefill GPUs** even though only output tokens are counted. Both sides of the CoreWeave chart claim the same recipe: NVFP4, MTP speculative decoding, Dynamo PD-disagg, wide expert parallelism, TensorRT-LLM. DeepSeek R1 671B is an **old** model; SemiAnalysis argues this choice is **theoretically kinder to Blackwell**, because Rubin’s HBM capacity/bandwidth and CPU DRAM advantages show up on multi-trillion-parameter models (Fable 5, Gemini Pro, Kimi K3, Qwen3.8 2.4T) and on multi-turn agentic context that a single-turn 8k/1k test cannot score. Upcoming **AgentX** (Weka, LMCache, vLLM/SGLang, Nvidia, AMD) is the intended agentic replacement.

Architecture is the mechanism, not decoration. Rubin SMEM rises to **328 KiB** in oversized mode (default still 228 KiB); TMEM to **256 KiB** (512→576 columns) so block-scale factors can sit disjoint from accumulators. TMA gains **inline descriptor updates** (ISA `.override`), removing the in-memory rewrite + sync that Blackwell paid on every MoE expert switch — decode at low batch is the beneficiary. BF16/FP16 exponential throughput **doubles per clock per SM** (softmax overlap); FP32 is unchanged from Blackwell Ultra. Tensor cores accept **UE5M3** 8-bit block scales in addition to UE4M3/UE8M0. **Counted writes** cut SM-driven NVLink chatter; Blackwell NVLink latency is described as **multiple times** TPU/Trainium. FP8/FP4 tensor-core throughput **doubles** via a doubled K dimension (plus a new K=128 alongside Blackwell Ultra’s awkward K=96/3×FP4). Programmatic Dependent Launch moves from **grid-level** to **threadblock-level** overlap. Global memory bandwidth is **2.8x Blackwell Ultra** via 3D-stacked HBM4; **memory-system latency is not expected to improve**. 2:4 **activation** sparsity (runtime, no retrain) is in silicon; Ampere 2:4 on weights was unused because it required prune-and-retrain; CoreWeave’s R1 numbers **do not appear to use it**, and Nvidia has published **no accuracy data**. LUT B is a new MMA mode: 3-bit indices into an 8-entry E4M3 codebook per 8×64 block = **3.125 bits/weight** stored, decode inside the MMA at FP8, weight-stationary, **no B transpose**. Versus MXFP4/NVFP4 this is a non-uniform codebook rather than a uniform block scale; it is **not automatically more accurate** (one codebook over 512 weights vs NVFP4’s scale over 16). Worked example: Kimi K3 2.8T raw weights ~**1,487.5 GB** at 4.25 bits vs ~**1,094 GB** at 3.125 bits (Δ ~**393.5 GB**), or ~**6 vs ~4** Rubin packages at **288 GB HBM4** per package — KV cache, activations, and replication excluded.

TCO, not FLOPs, is the investor object. Rubin’s **operator-ownership** TCO is **$3.57 per GPU-hour** vs **$1.84 GB200** and **$2.36 GB300**, so the $/token lead is **narrower** than the per-MW lead. Against July-2026 GB200/GB300, Rubin is cheaper at every interactivity: **~1.5x** through 100 tok/s/user, **~3x** at 200–250, **5x vs GB300 at 300** (GB200 cannot serve 300). Against the 2025 GB200 stack the curve peaks near **8x cheaper at 150 tok/s/user**. At 350 tok/s/user only Rubin has a point: **$4.18 per million output tokens**. Rack power is modeled at **~185 kW** server-level (ex-networking) for Max-Q **1,800 W** TDP plus the latest SOCAMM fit. Dense FP8 marketed FLOPs step from GB300’s **5,000 TFLOPs** to Rubin’s **~16,625 (1,800 W) / 17,500 (2,300 W)** — a **2.3–2.5x** FLOPs jump that **understates** the high-interactivity inference multiple. Cableless compute trays plus a second-generation copper backplane are expected to **shorten the production ramp** versus GB200 Oberon’s reliability tax. [Industry #8]: NVL72 scale-up, not the GPU die, is the binding reliability object this generation.

The AMD comparison in the subscriber-gated remainder is a **negative control**, not a horse-race. MI355X DeepSeek R1 MTP figures (434,235 tok/s/MW at 50 tok/s/user; 187,848 at 135) sit **3.06x / 4.72x** behind Rubin’s 1,330,000 / ~886,000, but SemiAnalysis marks the **non-MTP** MI355X path **invalid**: SGLang/AITER FlyDSL MoE reduce allocates an uninitialized intermediate, so EP decode at the M≈1024 bucket silently NaNs gsm8k to 0 while still emitting tokens. A partial fix restores concurrency 64; **≤32 still fails**. Current MI355X MTP nonetheless **beats last year’s GB200** — the same 2025 baseline CoreWeave markets against. [G-10] outside view: do not promote an AMD-vs-Rubin ranking off a corrupted decode path. Falsifier for the whole piece is the same date the source names: **InferenceX Rubin + TPUv7 + MI455X UALoE72 submissions, Q3 CY2026**.

## Framework / Mental Model

Three SemiAnalysis instruments, not one number.

| Instrument | What it measures | How this piece uses it |
|---|---|---|
| **InferenceX** (renormalized) | Output tok/s vs **decode-GPU watts** on a published recipe; SemiAnalysis re-bases onto CoreWeave’s **all-GPU (prefill+decode) MW** and **output-tokens-only** y-axis | Pareto of tok/s/MW vs interactivity (tok/s/user). A cell marked **impossible** means that recipe’s frontier ended — the SKU cannot serve that speed, not “zero tokens.” |
| **AI TCO model** (operator ownership) | All-in **$/GPU-hour** = IT capex + electricity + datacenter opex; **not** spot/rental | Cost per million output tokens = TCO ÷ renormalized output throughput. Rubin $3.57 vs GB200 $1.84 vs GB300 $2.36. Lower is better. Distinct from the vault’s $183K / cash-rent model in [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]. |
| **One Chart to Rule Them All** (from the AI Value Capture article; applied here) | Vertical dotted line = **cost-based rental floor** (min price for a standard neocloud project IRR). Horizontal dotted line = **value-based rental ceiling** (price at which the customer is indifferent vs the prior generation) | GB→VR FP8 FLOPs 2.3–2.5x set a high **theoretical** ceiling; this article’s inference TCO multiples (1.5x / 3x / 5x) are the evidence that the ceiling is **justified and still widening** as Rubin software matures. Same-PUE assumption: 45 °C coolant *could* cut Rubin PUE in a custom plant, but most halls are mixed-SKU so PUE is held constant. |

Supporting models named but not tabulated here: **All-in Utility Provisioned Power** (Datacenter Model), **VR NVL72 BoM Model** (component build-up, upcoming), **Accelerator Model** (quarterly Rubin package- and rack-level shipments), **Accelerator & HBM Model** (HBM volumes and vendor mix — vendor split is **not** printed in this article).

## Evidence

| Claim | Value | Tag |
|---|---|---|
| Platform | Vera Rubin NVL72 (SM107 / SM_107), 2nd-gen Oberon | [1×: SemiAnalysis] |
| Next arch | Feynman SM_140; new family, kernel rewrite vs Rubin kicker | [1×: SemiAnalysis] |
| Software drop | CUDA 13.4; PyTorch / vLLM / Triton / Dynamo PRs; Blackwell SM100 kernels reusable | [1×: SemiAnalysis] |
| Data origin | CoreWeave on Dell ES rack; **no scale-out fabric**; **not independently verified** | [1×: SemiAnalysis] |
| Verification date | Nvidia InferenceX commit **Q3 CY2026**; TPUv7 “next couple of months”; AMD MI455X UALoE72 | [1×: SemiAnalysis] |
| Workload on the chart | DeepSeek R1 671B; single-turn **8k / 1k**; output tok only; MW = prefill+decode | [1×: SemiAnalysis / CoreWeave] |
| Recipe (both sides) | NVFP4, MTP, Dynamo PD-disagg, wide EP, TensorRT-LLM | [1×: SemiAnalysis / CoreWeave] |
| Headline vs “today” GB200 | **5.4x** tok/s/MW; **5x** perf/$ | [1×: SemiAnalysis] |
| Nvidia/CoreWeave marketing point | **~10x** tok/s/MW vs **2025** GB200 at **~150 tok/s/user** (~50% faster than current frontier “fast mode”) | [1×: SemiAnalysis / CoreWeave] |
| SMEM / TMEM | 328 KiB oversized SMEM (default 228); TMEM 256 KiB, 576 cols (from 228 KiB / 512) | [1×: SemiAnalysis] |
| HBM | 3D-stacked HBM4; **2.8x** global BW vs Blackwell Ultra; **288 GB / package**; latency **not** improved | [1×: SemiAnalysis] |
| Tensor throughput | **2x** FP8 and FP4; doubled K; K=128 added; BF16/FP16 exp **2x**/SM/clock; FP32 flat | [1×: SemiAnalysis] |
| Block scale | UE5M3 8-bit added to UE4M3 / UE8M0 | [1×: SemiAnalysis] |
| LUT B | 3-bit index × 8-entry E4M3 LUT / 8×64 block = **3.125 bits/weight**; in-MMA; no B transpose | [1×: SemiAnalysis] |
| Kimi K3 2.8T raw weights | MXFP4 ~**1,487.5 GB** (2.8e12 × 4.25 / 8); LUT ~**1,094 GB**; Δ **~393.5 GB** | [1×: SemiAnalysis] [est. from their arithmetic] |
| Package count for those weights | ~**6** pkgs NVFP4 vs ~**4** pkgs LUT at 288 GB HBM4 (weights only) | [1×: SemiAnalysis] |
| 2:4 activation sparsity | Silicon present; **no** published accuracy; **not** in CoreWeave R1 results | [1×: SemiAnalysis] |
| NVLink | Counted writes; Blackwell NVLink latency **multiple times** TPU / Trainium | [1×: SemiAnalysis] |
| Rack power | **~185 kW** server-level ex-networking; Max-Q **1,800 W** TDP + latest SOCAMM | [1×: SemiAnalysis AI TCO / memory model] |
| Dense FP8 | GB300 **5,000 TFLOPs** → VR **~16,625** (1,800 W) / **17,500** (2,300 W) = **2.3–2.5x** | [1×: SemiAnalysis] |
| Operator TCO $/GPU-hr | Rubin **$3.57**; GB200 **$1.84**; GB300 **$2.36** (ownership, **not** rental) | [1×: SemiAnalysis AI TCO] |
| Coolant / PUE | Rubin can run **45 °C** coolant, chiller-less custom halls; **same PUE** used in the comparison | [1×: SemiAnalysis] |
| Ramp | Cableless compute tray; 2nd-gen copper backplane; faster production ramp vs GB200 Oberon | [1×: SemiAnalysis Accelerator Model] |
| Feynman extras | AMD-like 3D stacking (MI300X/CDNA3 analog); sparsity-aware data-movement ops | [1×: SemiAnalysis] |

### Perf / MW vs interactivity (renormalized InferenceX + CoreWeave)

| Interactivity | Rubin vs Jul-2026 GB300 | Rubin vs 2025 GB200 | Who can serve |
|---|---|---|---|
| Low / through **100** tok/s/user | **~2x** | **<3x** | All four recipes through 250 except as noted |
| **150** tok/s/user | (widening) | **~10x** (Nvidia lead chart) | All |
| **~200** tok/s/user | **~4x** (gap **peaks** vs GB300) | **~6x** | All |
| **250** | all four recipes have data | — | All four |
| **300** | **5.4x** — GB300 **last viable** point, ratio balloons | GB200 **impossible** | Rubin + GB300 only |
| **350** | GB300 **impossible** | GB200 **impossible** | **Rubin only** |
| Rubin absolute | **96,446** tok/s/MW @ 300; **70,703** @ 350 | — | [1×: SemiAnalysis] |

Blackwell per-GPU throughput **falls off as batch shrinks** at high interactivity; Rubin stays on a **flatter** frontier. That is the “more fast mode” claim.

### Cost / million output tokens (TCO ÷ throughput)

| Interactivity | vs Jul-2026 GB200 | vs Jul-2026 GB300 | vs 2025 GB200 |
|---|---|---|---|
| Through **100** tok/s/user | **~1.5x** cheaper | cheaper (unspecified split) | **~2x** cheaper |
| **150** | widening | widening | **~8x** (curve peak) |
| **200–250** | **~3x** | **~3x** class | **~5x** by 200 |
| **300** | GB200 **impossible** | **5x** (same balloon as per-MW) | — |
| **350** | impossible | impossible | — |
| Rubin @ 350 | **$4.18 / M output tokens** | only SKU on the curve | [1×: SemiAnalysis] |

### MI355X PD-disagg vs VR NVL72 (DeepSeek R1; accuracy caveat)

| Config @ interactivity | MI355X tok/s/MW | VR NVL72 | Ratio |
|---|---|---|---|
| MTP @ **50** tok/s/user | 434,235 | 1,330,000 | **3.06x** Rubin |
| non-MTP @ 50 | ~32,000 | 1,330,000 | **0.074x** (invalid path) |
| MTP @ **135** tok/s/user | 187,848 | ~886,000 | **4.72x** Rubin |
| non-MTP @ 135 | ~6,000 | ~886,000 | **0.032x** (invalid path) |

Bug: AITER FlyDSL MoE reduce intermediate **uninitialized**; EP `gemm2` fills only local expert slots; `torch.sum` folds garbage → NaN. Hits the **M≈1024** tuning bucket (low concurrency); mid/high concurrency stays clean. Fix restores **concurrency 64**; **≤32** still fails (sub-1024 M-buckets uncovered). [1×: SemiAnalysis]

## Contradiction Check

**[[Theses/NVDA - Nvidia]] §Summary (“10x lower inference cost vs Blackwell”; “Vera Rubin entered production H1 2026”).** Challenges the production-and-10x compression. This source’s object is a **pre-production Dell ES rack** without scale-out fabric, CoreWeave-supplied, unverified, on DeepSeek R1 671B. The **10x tok/MW** is vs **2025 GB200** at ~150 tok/s/user; vs **July 2026 GB300** the same chart is ~2x / ~4x / 5.4x (the last being GB300’s dying frontier). Operator TCO is **$3.57 vs $1.84 / $2.36**, so $/token is **1.5–3x** on the live Blackwell install, not 10x. Supports the **direction** of the inference-cost claim and the software-stack moat (CUDA 13.4 + SM100 kernel reuse). [G-13] hypothesis: the priced operating variable is “10x vs Blackwell”; the source’s mispricing, if any, is **which Blackwell vintage** the 10x is against.

**[[Theses/NVDA - Nvidia]] Insight #1 / CUDA generality (Pascal ABI → Rubin; ASICs re-spin).** Supports the **kicker** half: Rubin runs Blackwell kernels, so the annual cadence does **not** impose a Hopper→Blackwell rewrite on customers. Challenges the **unconditional** inheritance story at the next step: **Feynman SM_140 is a new family** requiring a rewrite “similar to Hopper WGMMA → Blackwell tcgen05.” LUT B, counted writes, threadblock PDL, and activation 2:4 are **silicon-present, kernel-absent** features — CoreWeave R1 does not use 2:4; no LUT accuracy paper. Hypothesis [Industry #2] / VLM interface-control: lock-in holds **this** generation via reuse; Feynman is the first CUDA-tax event since Blackwell. Falsifier: InferenceX Q3 CY2026 on modern models (Kimi K3 / Qwen3.8), not R1.

**[[Theses/NVDA - Nvidia]] Outstanding Q “ASIC inference cost gap” / Risk #2 / Risk #7 (Groq / TPU / Trainium).** Supports Nvidia on **tokens per MW and per TCO-dollar vs GB200/GB300 and vs a buggy MI355X path**. Does **not** measure TPU v7 or Trainium; those are **promised** submissions. Blackwell NVLink latency still “multiple times” TPU/Trainium — Rubin counted writes are a **partial** close, unquantified. Do not retire the ASIC Q on this clip.

**[[Theses/CRWV - CoreWeave]] Insight #6 / Conviction Trigger cash-rate / coverage; [[Theses/NBIS - Nebius Group]] Insight #6.** Supports “Rubin is not automatically value-destructive” **only on the SemiAnalysis operator-TCO and tok/MW axes**: Rubin is more expensive per GPU-hour ($3.57 vs $1.84/$2.36) and cheaper per **output token**, especially above 150 tok/s/user. That is **not** a cash-rent print and **not** a coverage %. Do not import $3.57 as CRWV/NBIS wholesale; do not import the vault’s **$183K / $8.22 IRR line / $12 contracted** into this source. CoreWeave is the **measurement host** (first public VR NVL72 inference chart; weeks-long bring-up lead). Hypothesis [VLM layer-renter] / [G-7]: Nvidia harvests the TCO-per-token surplus; the neocloud captures it only if the **contracted cash rate** prices “fast mode.” Falsifier remains a disclosed Rubin **cash** $/GPU-hour + coverage, not this TCO table.

**[[Theses/AMD - Advanced Micro Devices]] §Summary / Insight #3 (ROCm step-function) / Insight #5 (HBM-per-dollar) / → HIGH (MLPerf Training v5.0 within 10% of Rubin GR200) / → LOW (Helios gap >25% to Rubin).** Challenges the “MI355X within single-digit % of B200 ⇒ inference parity” interpolation. On DeepSeek R1 PD-disagg, even the **valid MTP** path is **3.06–4.72x** behind VR NVL72 on tok/MW; the non-MTP path is **accuracy-invalid**. Supports Insight #1’s “deals are diversification, not merit” if customers still buy Helios into a 3–5x tok/MW hole. Does **not** resolve the HIGH trigger (that is **training**, Llama-5-class, vs GR200). Hypothesis [G-10]: reference class is “challenger inference charts on last-gen models with known kernel bugs,” not MLPerf Training.

**[[Theses/MU - Micron Technology]] Insight #1 (qualified ≠ allocated) / Insight #4 (SOCAMM is a gate).** This article states **288 GB HBM4 per Rubin package** and **SOCAMM in the Max-Q 1,800 W / ~185 kW rack**, plus LUT B cutting weight footprint ~393.5 GB on a 2.8T model. It does **not** name a memory vendor and does **not** put MU cubes on first-wave boards. Hypothesis [Industry L1] / [Industry #1]: HBM4 capacity/bandwidth is the Rubin decode bottleneck this source is designing around; vendor rent is out of scope. Leave MU at **don’t-own** until the Q3 board meter.

**[[Theses/000660 - SK Hynix]] §Summary / → LOW (Samsung >35% of Rubin HBM4 in Q3–Q4 2026).** Neutral on allocation. Confirms Rubin’s memory step (HBM4, 2.8x BW, 288 GB/pkg) is load-bearing for the inference TCO story. Accelerator & HBM Model is cited for vendor volumes; **no split is printed here**. Do not move the 70/30/0 prior on this clip.

**Cross-model disconfirm.** [G-4] frenzy + [G-14] Jevons + [G-6]/VLM CUDA + [Industry #4/#8] kicker-plus-rack all point the same way (Rubin extends NVDA’s inference toll). That agreement is the cue to hunt the bear, not to raise conviction: **unverified ES rack, old model, unused LUT/sparsity, same-PUE conservative on power, $3.57 TCO already 1.9x GB200 per hour, Feynman rewrite ahead, TPU v7 and MI455X still outstanding.** Single falsifying datapoint: **Q3 CY2026 InferenceX on a modern MoE (Kimi K3 / Qwen3.8 / GLM5.2) where Rubin’s tok/MW lead vs July-2026 GB300 collapses toward 1x at 150–200 tok/s/user, or TPU v7 / MI455X UALoE72 prints inside that band.**

## Source Excerpts

> "Vera Rubin NVL72 running DeepSeek R1 delivers 5.4x performance per MW and 5x performance per dollar over GB200 NVL72 today, and the gap is even wider against GB200 NVL72 during its early bringup in 2025."

> "The first notable claim on the CoreWeave-Nvidia chart is that VR NVL72 achieves 10x better token throughput per megawatt than GB200 NVL72 at the iso-interactivity of ~150 tok/s/user."

> "Rubin carries a higher TCO per GPU than Blackwell, $3.57 per GPU-hour against $1.84 for GB200 and $2.36 for GB300 in the operator ownership scenario (not rental prices)."

> "The 5x edge over GB300 at 300 tok/s/user is the same as the per-MW view, where GB300 can barely serve tokens and GB200 can’t serve at this interactivity level at all."

> "At 3.125 bits per weight, the Rubin lookup-table format stores 2.8e12 x 3.125 / 8 = about 1,094 GB (about 1.09 TB). The difference is about 393.5 GB. … At 288 GB of HBM4 per Rubin package, the weights alone need about 6 packages in NVFP4 and about 4 packages in the new Rubin format."

> "We model the VR NVL72 as landing around ~185kW server-level power (excludes networking), for the Max-Q configuration with a TDP of 1,800W and with the latest SOCAMM configuration."

> "MI355X’s best figures for DeepSeek R1 are currently invalid due to an accuracy issue on SGLang: the MoRI EP decode path silently corrupts output at low concurrency, collapsing gsm8k to 0 while the server still generates tokens at full throughput."
