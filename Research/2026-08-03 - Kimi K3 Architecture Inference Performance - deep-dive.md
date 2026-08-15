---
publish: false
date: 2026-08-03
tags: [research, Semiconductors, NVDA]
sector: Semiconductors
ticker: NVDA
source: 'https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the'
source_type: deep-dive
updated: 2026-08-14
---

# Kimi K3 Architecture and Inference Performance

## Thesis Delta
Consensus prices Chinese open-weight frontier models as ChatGPT clones whose KV compression and MoE sparsity shrink HBM-linear token demand, and prices K3 serving at the OpenRouter floor ($3/M in, $15/M out as of 30 Jul 2026) → SemiAnalysis’s architecture primer shows Kimi Delta Attention makes **decode compute and memory constant in sequence length**, LatentMoE **doubles active experts (8→16) at unchanged all-to-all volume** by halving expert input dim (7168→3584), and InferenceX cost on one B300 node with DSpark is **$0.1712/M input at 4844.1 tok/s/GPU** — an order of magnitude below list and 76.89% below Moonshot’s $0.74 blended — so the binding constraint relocates from raw HBM-bits to leftover HBM after weights plus DRAM-tier offload plus EP comm-hide, not to fewer GPUs ([G-14] Jevons, [G-13] expectations, Semis #8 architecture-remap).

## Summary
Kimi K3 is framed as an inference-economics architecture, not a leaderboard footnote. Moonshot’s hybrid attention stacks Kimi Delta Attention (KDA) — a gated, per-channel-decay descendant of linear attention → DeltaNet → Gated DeltaNet — with full Multi-head Latent Attention (MLA) at a **3:1 KDA:MLA ratio** inherited from the Kimi Linear proof-of-concept. Linear attention compresses the entire past into one recurrent state S (O(Ld²) vs softmax’s quadratic access of all past K/V). DeltaNet stops S from growing unboundedly by a targeted “remove irrelevant associations” update (the Delta Rule). Gated DeltaNet adds an LSTM-style forget gate α; KDA expands α into a **diagonal per-channel decay** with positional awareness. FlashKDA, Moonshot’s open-sourced kernel, is the serving primitive: decode is ~**7D² FLOPs and ~8D² bytes** (FP32 state R/W dominates traffic), so both compute and memory are **constant in sequence length**; prefill unrolls the recurrence in chunks of C tokens, costing **12C³ + 8C²D + 6CD² FLOPs** per chunk and **~8C² + 22CD bytes** of traffic, which at T ≫ C collapses to **O(TD²) compute and O(TC + TD + D²) memory** — linear in T, not quadratic. That is the mechanism behind “compressed memory”: long-context decode stops being an HBM-bandwidth tax that scales with tokens.

Moonshot kept MLA layers as **full attention**, against Zhipu’s DeepSeek Sparse Attention and DeepSeek’s further Compressed Sparse / Heavily Compressed Attention. Jianlin Su’s stated reasons: no better attention found yet, and they refuse to stack too many architectural changes at once. MLA’s two modes are the agentic-workload crack. Prefill uses Multi-Head Attention mode and caches a **latent KV entry** rather than materialised K/V — **42.67× less KV memory per token** on the DeepSeek V3 config. Decode uses Multi-Query Attention mode (query multi-headed, KV entry single-headed) to avoid rematerialising the full cache; SDPA then runs in latent dim 512 rather than head dim 128, so MQA SDPA is **~4× the FLOPs** and overall **up to 3.4× FLOPs per token** vs MHA. Reasoning workloads (short prompt, long decode) love MLA’s tiny KV. Agentic workloads do not: tool returns create **append-prefill** (long cached prefix + long incremental prefill). MHA mode is too memory-heavy to materialise; MQA mode is too FLOP-heavy. vLLM/SGLang pick MHA + chunked prefill as a compromise. DeepSeek and Zhipu’s answer is sparse attention on the MQA path. SemiAnalysis’s forward claim: **Kimi K4 will replace MLA**.

KV cache “efficiency” is not KV bytes. No open-weight model ships static KV compression; leftover HBM after weights and activations depends on **wide expert-parallel vs tensor-parallel** deployment, so the same model has different KV budgets under different sharding. SemiAnalysis’s proposed metric is **KV throughput = KV cache size / prefill time (TTFT) at a given sequence length** — the minimum bandwidth to serve under PD-disaggregation, and a proxy for offload-tier bandwidth. Hybrid linear attention’s advantage widens with sequence length (the source’s comparison table is missing from the email clip). Residency follows the memory hierarchy: leftover **HBM → server DRAM → SSD**, with Mooncake Store as a distributed KV pool supporting write-through/write-back, prefix sharing across nodes, and avoiding TP-MLA duplication. KDA’s fixed-size recurrent state would be constant-memory **if** you stored one S; prefix-cache matching without known prefix boundaries forces a snapshot at every token and **regresses to sequence-length growth**. Production compromise: vLLM caches KDA state every **32K tokens** plus at prompt boundaries (agentic turns start there). Linear attention does **not** consume a constant KV in real serving.

The rest of the stack is built to keep that serving economics intact at depth and at MoE width. **Attention Residuals** replace the identity residual with softmax attention **over prior layer representations** (query is a learned per-layer vector, not token-generated), giving every layer selective access to earlier depth rather than an irreversible residual stream. Full attention-over-depth costs **O(Ld) communication** on a multi-GPU train; **Block Attention Residuals** cut that to **O(Nd)** by attending over N completed blocks plus the current block’s running sum. Claimed training properties: **1.25× compute efficiency** vs standard residuals, lower validation loss that widens in the decay phase, bounded output magnitude, consistent gradient scale. Pipeline-parallelism would otherwise ship all prior block outputs across stages; cross-stage caching plus activation checkpointing cuts the PP overhead to **4%**. Inference mirrors prefill/decode: Phase 1 batches all inter-block queries against completed block states; Phase 2 does sequential intra-block online softmax. IO footprint stays near a standard residual plus the amortized Phase-1 batch.

**LatentMoE** compresses routed tokens before dispatch and decompresses after combine; K3’s Stable LatentMoE adds RMSNorm before the up-projection to desensitise scale. Communication volume ∝ t × K × d / E. Kimi K2 ran **8 active experts at input dim 7168**; K3’s latent dim **3584 (half)** is the lever that **doubles active experts to 16 at constant communication volume**. The ratio that actually sets the roofline is **T_comm / T_comp = (P·F)/(6·m·B) × (1 − 1/E)** — independent of token count, active-expert count, and input dim; the only model knob is expert **intermediate dim m**. That formula is SemiAnalysis’s reason **m rose to 3072** not just K2→K3 but across DeepSeek V4 Pro, MiniMax M3, MiMo V2.5 Pro, and Inkling: as GPU FLOP/s (F) rises and weight precision falls, you grow m to keep communication hideable. Quantile Balancing (Jianlin Su, Feb 2026) is the aux-loss-free load-balance: bias is solved from the **(1 − k/n) quantile** of per-expert score-minus-cutoff margins so each expert gets q = mk/n tokens, with no tuned step-size.

InferenceX is the investor-facing output of that stack. Day-0 bring-up on K3 was easier than DeepSeek V4 because images and a speculative-decoder model shipped with the weights; **both Nvidia and AMD had Day-0 vLLM recipes** with DRAM offload and DSpark speculative decoding. The benchmark is no longer 8k1k/1k1k: it replays an hour of internal Claude Code traces to steady state — **median 142k input tokens, 444 output tokens, 65 turns/session**. That ISL:OSL shape is the agentic harness (tool calls, including edits). On the related DeepSeek V4 1.6T bring-up (the time-series the piece uses as the serving-physics illustration): the model **does not fit a single B200 node** (pipeline parallel required; DSpark broken under PP); it **fits one B300 node**, after which leftover HBM holds **3.25M tokens** of KV. Throughput rises with batch until concurrency **>8**, then cache hit rate collapses to **<10%** against a **95%** theoretical hit rate — the 3.25M-tok budget thrashing. Adding **219.91 GB/rank CPU DRAM offload** buys **+15.76M tokens (4.85×)** and lets concurrency >8 run without thrash. Cache-read already dominates SemiAnalysis’s own Claude Code / Codex bill. At P90 **30 tok/s/user**, one B300 node + DSpark delivers **4844.1 tok/s/GPU → $0.1712/M input** at July 2026 3-year rental **$2.60/hr**. OpenRouter’s $3/$15 floor is **~18× that input cost**. AgentX (315:1 ISL:OSL) puts Moonshot’s own blended price at **$0.74/M at 22 tok/s/user**; InferenceX on B300+vLLM is **$0.171/M at more than double the interactivity — a 76.89% cost cut**. B200 is described as “much worse and nearly infeasible.” The software (FlashKDA, DSpark, DRAM-tier KV, PD-disaggregation, wide EP) is what converts K3’s architectural constants into a token-price that can pull new agentic workload onto GPUs ([G-14]).

## Framework / Mental Model

Four named frames in the source, plus one load-balance typology.

| Frame | Definition | What it is for |
|---|---|---|
| **FlashKDA complexity / arithmetic intensity** | Decode ≈ 7D² FLOPs / 8D² bytes. Prefill per chunk 12C³ + 8C²D + 6CD² FLOPs; traffic ~8C² + 22CD; global O(TD²) compute, O(TC+TD+D²) bytes | Proves KDA prefill is linear in T and decode is **constant** in T for both compute and memory |
| **MLA dual-mode (MHA prefill / MQA decode)** | Cache latent KV entry (42.67× smaller); MQA SDPA in d=512 vs MHA d=128 → up to 3.4× FLOPs/token | Explains why MLA wins reasoning decode and loses **append-prefill** agentic extend |
| **KV throughput** | KV cache size ÷ prefill time (TTFT) at a stated sequence length | Minimum interconnect/offload bandwidth for PD-disaggregated serve; architecture-aware KV-efficiency proxy (not bytes-alone) |
| **KV residency hierarchy** | Leftover HBM → server DRAM → SSD; Mooncake write-through/write-back across a cluster-visible pool | Turns “KV compression” into a **tier-bandwidth** question; DRAM offload is a first-class serving config |
| **MoE T_comm / T_comp** | (P·F)/(6·m·B) × (1 − 1/E) | Roofline for overlapping dispatch/combine with SwiGLU. Only **m** (intermediate dim) is a model lever; motivates m=3072 industry-wide as F rises |
| **Quantile Balancing (QB)** | Aux-loss-free, hyperparameter-free: next bias = (1 − k/n) quantile of (score − cutoff) margins so each expert gets q=mk/n tokens | Replaces tuned aux-free step-size; bias updates shrink to zero when already balanced |

KDA prefix-cache rule sits under KV throughput: constant-size S is the training/math object; serving snapshots every 32K tokens + prompt boundaries, so production KV is **piecewise-constant**, not constant.

## Evidence

### Attention and kernel math

| Quantity | Value | Tag |
|---|---|---|
| Softmax attention vs linear attention complexity | Quadratic vs O(Ld²); linear attention stores past K/V in one state S | [1×: SemiAnalysis] |
| FlashKDA decode FLOPs / traffic | ~7D² FLOPs; ~8D² bytes (FP32 state dominates) | [1×: SemiAnalysis] |
| FlashKDA prefill FLOPs (chunk C) | 12C³ + 8C²D + 6CD²; global O(TD²) for T ≫ C | [1×: SemiAnalysis] |
| FlashKDA prefill traffic | ~8C² + 22CD bytes/chunk + 8D² state; global O(TC + TD + D²) | [1×: SemiAnalysis] |
| KDA sequence scaling | Prefill: linear in T (compute + memory). Decode: **constant** in T (compute + memory) | [1×: SemiAnalysis] |
| Kimi Linear → K3 inheritance | Shared-expert count, hybrid linear-attention ratio, attention-module design | [1×: SemiAnalysis / Kimi Linear vs K3 tech blog] |
| Ideal KDA:MLA ratio | 3:1 (performance vs efficiency) | [1×: SemiAnalysis / Kimi Linear] |
| KDA vs RoPE | KDA used as the position-aware operator; replaces RoPE on MLA | [1×: SemiAnalysis] |
| MLA KV-entry compression | 42.67× less KV memory per token (DeepSeek V3 config; RoPE dims omitted) | [1×: SemiAnalysis / DeepSeek V3.2] |
| MHA vs MQA SDPA | MHA in head dim 128; MQA in latent dim 512 → ~4× SDPA FLOPs; up to 3.4× FLOPs/token overall | [1×: SemiAnalysis] |
| Workload fit | Reasoning = short prefill + long decode → MLA KV win. Agentic = append-prefill → neither MLA mode fits | [1×: SemiAnalysis] |
| Engine compromise | vLLM / SGLang: MHA + chunked prefill (avoid full-context materialisation) | [1×: SemiAnalysis] |
| Peer response / K4 claim | DeepSeek, Zhipu: sparse attention on MQA path. SA: K4 replaces MLA | [1×: SemiAnalysis] |
| KDA prefix-cache granularity | vLLM snapshot every 32K tokens + prompt boundaries | [1×: SemiAnalysis / vLLM] |

### Depth residuals and LatentMoE

| Quantity | Value | Tag |
|---|---|---|
| Full Attention-Residual comm | O(Ld) | [1×: SemiAnalysis] |
| Block Attention Residual comm | O(Nd) (N blocks of S layers) | [1×: SemiAnalysis] |
| Block-residual training claim | 1.25× compute efficiency vs standard residual; bounded output; consistent gradient magnitude | [1×: SemiAnalysis] |
| PP overhead after caching + checkpointing | 4% vs standard residual architecture | [1×: SemiAnalysis] |
| Cross-stage cache comm | First virtual stage quadratic in physical stages; later virtual stages O(P); overlapable over a full fwd+bwd | [1×: SemiAnalysis] |
| Extra activation memory | None after checkpointing (stage activation matches standard Hl) | [1×: SemiAnalysis] |
| LatentMoE comm volume | ∝ t · K · d / E (tokens × active experts × expert input dim / EP size) | [1×: SemiAnalysis / LatentMoE paper] |
| K2 → K3 expert config | K2: 8 active, d=7168. K3: latent d=3584 (½), active K=16 (×2). Comm volume held flat | [1×: SemiAnalysis] |
| T_comm / T_comp | (P·F)/(6·m·B) × (1 − 1/E). Independent of t, K, d | [1×: SemiAnalysis] |
| SwiGLU FLOPs/token | 6 · d · m | [1×: SemiAnalysis] |
| Expert intermediate dim | 3072 (K2→K3 and DeepSeek V4 Pro, MiniMax M3, MiMo V2.5 Pro, Inkling) | [1×: SemiAnalysis] |
| Quantile Balancing | Feb 2026, Jianlin Su; (1 − k/n) quantile of margins; q = mk/n tokens/expert; hyperparameter-free | [1×: SemiAnalysis / Su blog] |

### Serving, memory hierarchy, TCO

| Quantity | Value | Tag |
|---|---|---|
| OpenRouter K3 floor (30 Jul 2026) | $3/M input, $15/M output — all listed providers | [1×: SemiAnalysis / OpenRouter] |
| Day-0 recipes | Nvidia **and** AMD on vLLM; DRAM offload + DSpark speculative decoding | [1×: SemiAnalysis] |
| InferenceX trace mix | Median 142k in / 444 out / 65 turns per session; 1 hour to steady state | [1×: SemiAnalysis, internal Claude Code traces] |
| AgentX ISL:OSL | 315:1 | [1×: SemiAnalysis] |
| Prior InferenceX mix (superseded) | 8k1k / 1k1k | [1×: SemiAnalysis] |
| DSv4 1.6T fit | Does **not** fit 1× B200 node (PP required; DSpark incompatible with PP). Fits 1× B300 node | [1×: SemiAnalysis / InferenceX] |
| B300 leftover HBM KV | 3.25M tokens after weights | [1×: SemiAnalysis] |
| Cache-thrash threshold | Concurrency >8; hit rate <10% vs 95% theoretical | [1×: SemiAnalysis] |
| DRAM offload | 219.91 GB/rank → +15.76M tokens → **4.85×** KV capacity | [1×: SemiAnalysis] |
| TCO, B300 + DSpark, P90 30 tok/s/user | 4844.1 tok/s/GPU; **$0.1712/M input** at $2.60/hr 3Y rental (Jul 2026) | [1×: SemiAnalysis] |
| List vs cost | OpenRouter $3/M in ≈ **17.5×** $0.1712 cost | [1×: SemiAnalysis; ratio est.] |
| Moonshot platform vs InferenceX | $0.74/M blended at 22 tok/s/user vs $0.171/M at >2× interactivity = **76.89%** cheaper | [1×: SemiAnalysis] |
| B200 K3 TCO | “Much worse and nearly infeasible” vs B300 | [1×: SemiAnalysis] |
| Spend mix (SA own usage) | Cache-read dominates Claude Code / Codex cost | [1×: SemiAnalysis] |
| K3 vs DSv4 bring-up | K3 Day-0 easier: docs, images, speculative-decoder shipped with weights | [1×: SemiAnalysis] |

## Contradiction Check
Supports [[Theses/NVDA - Nvidia]] §Summary open-weight-as-workload-generator and §Industry Context “more model providers → more aggregate compute”: K3 is a serving-stack requirement (FlashKDA, 16-expert LatentMoE, PD-disagg, DRAM offload, DSpark) that still runs on merchant GPUs, and $0.1712/M vs $3/$15 is the [G-14] price cut that pulls agentic traces (142k/444, 65 turns) onto silicon rather than shrinking the installed base. Challenges the same thesis’s §Outstanding Questions “algorithmic efficiency overwhelm Jevons” and the TurboQuant-style “KV compression 6× kills HBM” reading: KDA decode is O(1) in T **and** production KV is still piecewise-growing (32K snapshots), leftover-HBM after a 1.6T-class weight load is only 3.25M tok on B300, and the 4.85× capacity add is **DRAM**, not deleted demand. Challenges §Outstanding Questions CUDA-durability / §Key Non-consensus Insight “CUDA is general-purpose”: **AMD shipped Day-0 vLLM recipes** alongside Nvidia — the serving surface for this model is vLLM/SGLang + custom KDA kernels, not a CUDA-only ABI. Supports the software-closes-the-inference-gap log line (DSpark, DRAM offload, FlashKDA) and the B200→B300 generation step: B200 is called nearly infeasible for this TCO. NVDA has **no Conviction Triggers section** to pin; the live falsifiers this source writes are (i) K4 replaces MLA with a sparse/linear design that also collapses EP width, (ii) OpenRouter/Moonshot prices converge to the $0.17 band without a matching volume explosion, (iii) AMD Day-0 parity holds on the 142k-class agentic trace rather than a demo kernel.

Challenges [[Theses/000660 - SK Hynix]] §Key Non-consensus Insight #3 HBF-as-inference-tier and the implicit “more tokens → more HBM bits linearly” demand function used in §Summary’s $30B HBM book: KV residency already spills HBM→DRAM→SSD; 219.91 GB/rank DRAM is a **4.85×** KV multiplier on a B300 node whose HBM leftover is 3.25M tok; KDA decode traffic is constant in T. That is a **near-term DDR/LPDDR attach** story and a structural haircut to HBM-intensity per agentic token, not a 2028 HBF option. Does not fire the §Conviction Triggers Samsung-Rubin >35% kill — this source never measures HBM vendor share. Hypothesis to test (Semis #8, #1): the bottleneck relocates from HBM-bits to leftover-HBM-after-MoE-weights + DRAM-tier bandwidth + EP all-to-all; HBM still sets the weight floor (see [[Research/2026-07-21 - TSM NVDA PhotonCap Kimi K3 MoE Memory Load - deep-dive]] ~1.4TB MXFP4 class) so instance **count** can stay high while KV-HBM **per token** falls.

Challenges [[Theses/MU - Micron Technology]] §Summary / Insight “mix-shift dollars exist without Rubin cubes; SOCAMM is a gate, not a layer” only on the gate-vs-layer wording: InferenceX treats 219.91 GB/rank CPU DRAM offload as **load-bearing serving capacity** (the difference between cache-thrash at concurrency >8 and a 4.85× KV budget). That is a DRAM-attach demand line independent of Rubin HBM4 board share. Does **not** promote MU: the source never names a DRAM vendor, never measures SOCAMM/LPDDR sole-source, and does not fire → HIGH (board meter + LTA-cap removal + TrendForce). Semis L1 (DRAM less cyclical) stays a hypothesis; this is one more contracted inference-adjacent use of server DRAM, not a destock falsifier.

Supports [[Theses/TSM - Taiwan Semiconductor]] §Insight #1 CoWoS-as-annuity via instance geometry rather than tok/s: LatentMoE at 16 active experts plus “wide EP changes leftover HBM vs TP” means more GPUs (and more CoWoS sites) **per replica** even as KDA cuts per-token attention FLOPs and KV growth. [G-14] then scales replica count as $0.17 tokens pull agentic ISL. Does not fire TSM → LOW (HPC growth <10%, GM <63%, CoWoS-alternative win). Watch the bear: if KDA + DRAM offload + m=3072 comm-hide lets labs serve K3-class models on fewer packages per tok, packaging intensity per token compresses while token volume must more than offset — the same Jevons test as NVDA.

[[Theses/AMD - Advanced Micro Devices]] is a weak-match adjacency: Day-0 vLLM + DSpark on AMD is the first concrete serving-stack claim that K3 does not wait on CUDA. Not a thesis-section hit without an AMD inference-software trigger to name.

Mental-model triggers held as hypotheses, not verdicts: [G-13] the mispriced operating variable is **tok/$ at a stated tok/s/user on an agentic ISL**, not GPU list price or OpenRouter list; [G-14] a 76.89% cost cut plus 18× provider markup is the labour-to-compute unlock for 142k-in tool loops; [G-3] do not apply mean-reversion (“efficiency → less silicon”) to a workload class still pre-chasm on agentic traces; [G-4] frenzy GPU/HBM capacity is the substrate this software is now harvesting; [G-10] base rate = prior “efficient open model kills capex” tapes (DeepSeek-class) that did not cut foundry/HBM units; Semis #8 architecture remap (softmax-KV → hybrid linear + latent EP + DRAM tier); Semis #1 re-identify the binding segment (leftover HBM + DRAM BW, not last cycle’s HBM-bit shortage); Semis #18 do not read KDA’s O(1) decode as “HBM is dead”; Automation Lens B adjacency only (NVDA/AMD sell the compute other firms automate on; operator-readiness of Moonshot itself is out of scope).

## Source Excerpts

> “This concretely shows that the computational complexity of KDA: Prefill: Linear to sequence length for both computation and memory. Decode: Constant to sequence length for both computation and memory.”

> “By saving KV entries, we reduce the memory usage by 42.67x per token.” … “MQA mode incurs roughly 4x FLOPs for SDPA, and overall can cost up to 3.4x FLOPs per token, compared to MHA mode.”

> “Neither mode of MLA suits append-prefill. … We suspect Moonshot’s future models such as Kimi K4 will feature attention mechanisms that replace MLA.”

> “Kimi K2 series feature 8 active experts with input dimension size 7168, so Kimi K3’s latent input dimension size being 3584 (half of 7168) would allow the active expert count to double to 16 without increasing the communication volume.”

> “The communication to computation time ratio is T_comm / T_comp = (P*F) / (6*m*B) * (1-1/E).” … “We believe this formula also motivates an increase in expert intermediate dimension to 3072 in not just Kimi K2 to K3, but all recent open weight models, including DeepSeek V4 Pro, MiniMax M3, MiMo V2.5 Pro, and Inkling.”

> “There is a median of 142k input tokens and a median of 444 output tokens per turn with a median of 65 turns per session.”

> “After accounting for the weights, GPU HBM can only hold 3.25M tok. … But for a system with 219.91 GB/rank CPU DRAM offload, this results in an additional 15.76M tokens worth of KV cache, or a 4.85× total tokens worth of KV cache.”

> “At a P90 of 30 tok/s/user, serving with 1 node of B300 utilizing DSpark speculative decoding, gives you an input throughput of 4844.1 tok/s/GPU, translating to a cost of $0.1712/M input tokens for 3Y rental prices of $2.60/hr as of July 2026. This means providers are offering at an order of magnitude more than cost on serving Kimi K3. On B200 this is much worse and nearly infeasible.”

> “Using our AgentX dataset, which has 315:1 ISL to OSL ratio, we estimate the blended price of using Kimi K3 on Moonshot’s platform is $0.74 per million tokens at 22 tok/s/user. … serving Kimi K3 on B300 with vLLM costs $0.171 per million tokens at more than double the interactivity, a 76.89% reduction in cost.”
