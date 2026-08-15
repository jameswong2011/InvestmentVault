---
publish: false
date: 2026-08-10
updated: 2026-08-14
tags: [research, Semiconductors, NVDA]
sector: Semiconductors
ticker: NVDA
propagated_to: [NVDA]
source: 'https://newsletter.semianalysis.com/p/ultra-high-interactivity-on-nvidia'
source_type: deep-dive
---

# Ultra-High Interactivity on NVIDIA GPUs? - TileRT InferenceX

## Thesis Delta
Consensus prices paid “fast mode” as a specialty-silicon TAM (Cerebras WSE, Groq LPU, SambaNova) that GPUs forfeit at batch-1 because kernel-launch plus HBM *latency* leave most of the 3,047 tok/s/user B200 roofline on the table, and reads [[Theses/NVDA - Nvidia]] §Bear Case / Risk #7 (Groq LPX, Rubin CPX cancelled) as proof that GPU architecture cannot serve dedicated inference → SemiAnalysis InferenceX shows a software-only persistent Engine Kernel on an 8-GPU B200 decode node at 494.2 tok/s/user (1k/1k FP8) and 340 tok/s/user (8k/1k), 1.9–3.6× conventional GB300/B300 engines, at $13.56 vs $13.4 per million output tokens for 1.9× interactivity, so most buyer need is a *speed tier* carved from the fungible GPU fleet already purchased, not a forklift to SRAM ASICs ([G-13] price-implied inference-architecture variable; #2 CUDA/software lock-in; #8 bottleneck remaps from kernel-launch/HBM-latency to compiler catalog + PD mix).

## Summary
Premium-priced fast modes (Claude Code cited as 2.5× interactivity at 2× $/token) demonstrate users will pay for lower latency; labs therefore evaluate purpose-built inference (Cerebras, NVIDIA Groq LPU) for interactive assistants and full-duplex voice (OpenAI GPT-Live). GPUs already win high-throughput / low-to-medium interactivity. They lose ultra-low latency: an 8-GPU HGX B200 offers 64 TB/s aggregate HBM, GLM-5 at NVFP4 moves ~21 GB of active-parameter traffic per token, and the bandwidth roofline is 3,047 tok/s/user without speculative decode — measured engines never approach it. The gap is latency, not bandwidth. Traditional serving launches and synchronizes thousands of kernels; setup/teardown and HBM spill of half-finished work dominate once Time Per Output Token enters the sub-millisecond band. CUDA graphs replay a DAG of launches but leave kernel boundaries and wipe on-chip state at each one. Memory *bandwidth* rises ~2–3× per generation; memory *latency* does not.

TileRT (same maintainer org as the TileLang DSL) statically compiles the decode graph into one persistent Engine Kernel. The host launches once; execution stays resident for the decode lifecycle; most orchestration moves to compile time. Work decomposes into tile-level tasks with warp- and block-specialization: warp groups split asynchronous data movement, tensor compute, and communication, overlapping what used to be serial load → barrier → compute → barrier, and keeping intermediates in registers, shared memory, and L2 instead of repeatedly spilling to HBM. Each CTA becomes a small heterogeneous factory rather than a uniform SIMT worker. Specialization then extends to whole GPUs: homogeneous all-rank SPMD wastes work on sparse routing, Top-K, dynamic indexing, long-context attention, and MTP. In GLM-5.1 attention, GPU 0 is a Sparse Indexer (Top-K, index construction, routing) while GPUs 1–7 run MLA (RMSNorm, GEMM, flash sparse attention, AllReduce). Collectives execute inside the tile flow, so an entire attention layer is one host launch and a continuous compute ↔ communication pipeline. SemiAnalysis’s claim scope is decode interactivity on GLM-5 / 5.1 FP8 744B under InferenceX, not training, not a general throughput engine, and not a raised HBM roofline.

Verified InferenceX points put TileRT “in a class of its own” on per-user speed and simultaneously worse on aggregate work. At 8k/1k, 340 tok/s/user on an eight-GPU B200 node is 1.9× the prior dataset best (181.4 tok/s/user on GB300 NVL72 NVFP4+MTP) and 3.0× the fastest conventional FP8 (113.6 on B300+MTP). At 1k/1k, TileRT FP8 hits 494.2 tok/s/user — 1.9× the best conventional result (256.3 FP4) and 3.6× the best conventional FP8 (136.3) — without TileRT FP4 support, and without using the 72-GPU NVLink copper domain that does nothing for batch-1 interactivity. The same 8k/1k slice shows the cost: GB300 FP4+MTP at concurrency 12 delivers ~240 total tok/s/GPU at 154 tok/s/user; TileRT delivers 160.4 tok/s/GPU at 340 tok/s/user. End-to-end, TileRT FP8 is 4.5× faster at 1k/1k and 3.0× at 8k/1k versus the prior GLM-5.1 best; TTFT is merely “good”; the decode tail is 3.01s versus 6.54s (best NVFP4+MTP) and 18.18s ([[Theses/AMD - Advanced Micro Devices|AMD]] MI355X). TileRT v0.1.5 serves one in-flight request per decode node — “not just a race car… a private rocket ship with room for just one passenger.” Engineering more passengers is described as ambitious, not scheduled.

The serving composition is PD-disaggregated, not a vLLM replacement. Prefill stays compute-bound and throughput-priced on vLLM/SGLang (scheduler, chunked prefill, prefix cache, OpenAI-compatible API). Decode that is latency-critical is marked and routed to a TileRT pool; general traffic stays on a conventional vLLM decode pool. Both classes share one prefill server via vLLM’s MultiConnector: TileRTConnector claims only tagged requests and is a no-op otherwise. KV moves over Mooncake and NIXL; the router applies back-pressure when the single-passenger node is occupied. Xiaomi (MiMo V2.5 Pro UltraSpeed) and Z.ai (GLM-5.1 HighSpeed) already run this pattern in production — neither bought a dataflow chip; both carved a speed tier from the GPU cluster they already ran. That is the TAM argument against Cerebras / Groq / SambaNova: those vendors encoded AoT scheduling, persistent execution, specialized workers, and fused comms in SRAM/wafer/dataflow silicon (CS-3: ~900k cores, 44 GB on-chip SRAM, 21 PB/s). TileRT imports software analogues onto a SIMT + HBM machine that still has dynamic warp schedulers and must be “convinced” to impersonate a spatial pipeline via statically expanded kernels, hand-carved warp specialization, and per-model compilation against pinned drivers. Software can approach the HBM roofline; it cannot raise it — Cerebras still serves a dense 70B at speeds no eight-GPU node can reach. What most buyers need, SemiAnalysis argues, is not a speed *machine* whose PD ratio is frozen on the purchase-order date, but a speed *tier* whose capacity is a scheduler decision on a liquid GPU pool. Guess the conversational-versus-agent mix wrong on GPUs and you rebalance in software; guess wrong on dedicated silicon and you wait months to re-rack or you strand the premium SKU. Specialists now compete against their own execution model running on fungible hardware. The inbox clip’s TCO slice puts that in dollars: at 8k/1k TileRT does 340 tok/s/user and 35.4 output tok/s per B200 = $13.56 / million output tokens, versus GB200 FP4+MTP at concurrency 5 (~176 tok/s/user, ~286 tok/s/GPU, $1.86 / GB200-hour) at $13.4 / million — 1% more cost for 1.9× interactivity, versus Claude Code fast mode’s 2.5× speed at 2× price. Same-precision, GB300 FP8+MTP at 108 tok/s/user prices at $35 / million; TileRT is 61% cheaper at 3.1× interactivity. The clip ends there.

The offsetting constraint is ASIC-like compiler tax. The catalog is GLM-5/5.1 and DeepSeek-V3.2; GLM-5.1 is already a generation behind and deprecated on mainline InferenceX; MiMo UltraSpeed is a closed co-design. A persistent kernel forces compile-time choices on tile shapes, pipeline depth, register/SMEM/L2 residency, warp-group split, fused collectives, and specialized ranks; change attention or routing and the schedule dies. TileOPs (per-operator machine-readable manifests with signatures, workloads, and roofline models driving codegen/test/bench against hardware bounds) plus AI coding agents are the stated path to shorten that loop; novel transforms still need experts, and a monolithic kernel weakens conventional per-kernel profiler feedback. Next InferenceX work is AgentX (replayed Claude Code / Codex traces, median 140k input tokens, 99.2% theoretical median cache-hit roofline) to test incremental KV transfer, prefix reuse, offload, routing, and whether interactivity survives multi-turn — plus batch-size 2/4/8 sweeps to find where the Engine Kernel’s latency edge flattens. Claim scope is therefore: software-defined batch-1 decode on NVIDIA GPUs is already a production speed tier at iso-cost interactivity the conventional stack cannot reach; it is not a generic serving engine, not FP4, not multi-user, and not a substitute for the SRAM roofline on the models that still need it.

## Framework / Mental Model
**InferenceX latency–throughput Pareto.** SemiAnalysis’s open, vendor-neutral, continuously updated benchmark (reproduced/supported by GCP, Azure, Oracle, Meta; vLLM, LMCache, SGLang, PyTorch, Hugging Face; labs including OpenAI, MiniMax, ZAI, Qwen, Moonshot Kimi). Two axes, no single operating point: *interactivity* = tok/s/user = 1/TPOT (whether a response feels snappy); *throughput* = tok/s/GPU (cost per token). Batching raises aggregate work and lowers per-user speed. NVIDIA has committed Vera Rubin numbers; Google TPUv7 and AMD MI455X UALoE72 are queued.

**Bus / race car / private rocket ship.** A bus amortizes cost across passengers and forces shared stops (high concurrency, low $/token, low interactivity). A race car carries one or two people faster at high $/passenger (small-batch conventional engines). TileRT at batch-1 is a private rocket ship: one in-flight request per decode node, maximum tok/s/user, deliberately specialized. The source’s numerical illustration of the conventional curve: moving interactivity from ~25 to ~260 tok/s/user cuts per-GPU throughput from ~5,900 to ~200 tok/s/GPU — ~30× less aggregate work for ~10× per-user speed.

**PD-disagg two-pool routing.** One shared vLLM prefill pool feeds Pool A (TileRT ultra-high-interactivity decode, tagged via `kv_transfer_params` after vLLM emits the first token) and Pool B (native vLLM/SGLang decode for general traffic). The TileRT connector is class-selective; providers pay the rocket-ship utilization tax only on latency-critical requests.

**AI TCO Model (iso-cost interactivity).** SemiAnalysis prices cost per million *output* tokens only after a latency SLO is feasible. Compare (a) the cheapest system that *reaches* a tok/s/user target versus (b) same-precision conventional endpoints. Accelerator Model (separate) tracks NVIDIA LPU30/LPU40 and Cerebras WSE-3/WSE-4 shipments; this article uses it as context, not as a published shipment table.

## Evidence

| Roofline / traffic | Figure | Tag |
|---|---|---|
| 8-GPU HGX B200 aggregate HBM BW | 64 TB/s | [1×: SemiAnalysis] |
| GLM-5 NVFP4 active-parameter traffic / token | ~21 GB | [1×: SemiAnalysis] |
| Theoretical B200 BS1 tok/s/user (no speculation) | 3,047 | [est. from BW/traffic; SemiAnalysis] |
| Single HGX H200 aggregate HBM BW | 38.4 TB/s | [1×: SemiAnalysis] |
| H200-class MXFP8 active traffic / token | 42 GB | [1×: SemiAnalysis] |
| Theoretical H200 BS1 tok/s/user (no speculation) | ~1,000 | [est. from BW/traffic; SemiAnalysis] |
| Memory BW per generation | ~2–3× | [1×: SemiAnalysis] |
| Memory latency per generation | unchanged | [1×: SemiAnalysis] |

| InferenceX interactivity (tok/s/user) | Config | Figure | Tag |
|---|---|---|---|
| TileRT peak (intro, FP8, 1k-class) | 8-GPU B200 decode | ~500 | [1×: InferenceX/SemiAnalysis] |
| TileRT 1k/1k FP8 | 8-GPU B200 | 494.2 | [1×: InferenceX/SemiAnalysis] |
| Best conventional 1k/1k | FP4 | 256.3 | [1×: InferenceX/SemiAnalysis] |
| Best conventional 1k/1k FP8 | — | 136.3 | [1×: InferenceX/SemiAnalysis] |
| TileRT vs best conventional 1k/1k | mixed precision | 1.9× | [1×: SemiAnalysis] |
| TileRT vs best conventional FP8 1k/1k | same precision | 3.6× | [1×: SemiAnalysis] |
| TileRT 8k/1k | 8-GPU B200 | 340 | [1×: InferenceX/SemiAnalysis] |
| Prior best 8k/1k | GB300 NVL72 NVFP4+MTP | 181.4 | [1×: InferenceX/SemiAnalysis] |
| TileRT vs prior best 8k/1k | mixed precision | 1.9× | [1×: SemiAnalysis] |
| Fastest conventional FP8 8k-class | B300+MTP | 113.6 | [1×: InferenceX/SemiAnalysis] |
| TileRT vs conventional FP8 (8k-class) | same precision | 3.0× | [1×: SemiAnalysis] |
| Conventional Pareto illustration | 25 → 260 tok/s/user | 5,900 → 200 tok/s/GPU (~30× / ~10×) | [1×: SemiAnalysis] |

| Throughput / concurrency trade-off (8k/1k) | tok/s/user | tok/s/GPU | Concurrency | Tag |
|---|---|---|---|---|
| GB300 FP4+MTP (traditional) | 154 | ~240 | 12 | [1×: InferenceX/SemiAnalysis] |
| TileRT FP8 | 340 | 160.4 | 1 / decode node | [1×: InferenceX/SemiAnalysis] |
| TileRT in-flight model | — | — | 1 request (v0.1.5) | [1×: SemiAnalysis] |

| End-to-end latency | Figure | Tag |
|---|---|---|
| TileRT vs prior best GLM-5.1 E2E 1k/1k | 4.5× | [1×: InferenceX/SemiAnalysis] |
| TileRT vs prior best GLM-5.1 E2E 8k/1k | 3.0× | [1×: InferenceX/SemiAnalysis] |
| TileRT decode tail | 3.01 s | [1×: InferenceX/SemiAnalysis] |
| Best NVFP4+MTP decode tail | 6.54 s | [1×: InferenceX/SemiAnalysis] |
| MI355X decode tail | 18.18 s | [1×: InferenceX/SemiAnalysis] |
| TileRT TTFT | “good but not exceptional” | [1×: SemiAnalysis] |

| TCO (AI TCO Model; 8k/1k unless noted) | Interactivity | Work / GPU | Cost | Tag |
|---|---|---|---|---|
| TileRT B200 | 340 tok/s/user | 35.4 output tok/s per B200 | $13.56 / M output tok | [1×: SemiAnalysis AI TCO] |
| GB200 FP4+MTP disagg (highest conventional interactivity) | ~176 tok/s/user | ~286 total tok/s/GPU @ conc. 5 | $13.4 / M output tok @ $1.86 / GB200-hour | [1×: SemiAnalysis AI TCO] |
| TileRT vs that GB200 point | 1.9× interactivity | — | +1% $/token | [1×: SemiAnalysis] |
| Fastest conventional disagg FP8 | GB300 SGLang+MTP 108.0 tok/s/user | — | $35 / M output tok (endpoint) | [1×: SemiAnalysis AI TCO] |
| TileRT vs that FP8 point | 3.1× interactivity | — | 61% cheaper $/token | [1×: SemiAnalysis] |
| Feasible set at 339 tok/s/user (GLM-5.1 GPU) | TileRT only | — | conventional max 176 tok/s/user | [1×: SemiAnalysis] |
| Iso-cost interactivity vs traditional engines (article claim) | up to 2× / 1.9× | — | same $/token band | [1×: SemiAnalysis] |
| Claude Code fast mode (comparison, not InferenceX) | up to 2.5× interactivity | — | 2× price/token | [1×: SemiAnalysis] |

| Specialists / production / catalog | Figure | Tag |
|---|---|---|
| Cerebras CS-3 | ~900,000 cores; 44 GB on-chip SRAM; 21 PB/s mem BW | [1×: SemiAnalysis] |
| Groq | Deterministic compiler + large on-chip SRAM | [1×: SemiAnalysis] |
| SambaNova | Reconfigurable dataflow; SRAM + HBM + DDR tiers | [1×: SemiAnalysis] |
| Production decode | Xiaomi MiMo V2.5 Pro UltraSpeed; Z.ai GLM 5.1 HighSpeed | [1×: SemiAnalysis] |
| TileRT model catalog | GLM-5/5.1, DeepSeek-V3.2 | [1×: SemiAnalysis] |
| GLM-5.1 on mainline InferenceX | Deprecated; “a generation behind” | [1×: SemiAnalysis] |
| MiMo UltraSpeed weights | Co-design; not open-sourced | [1×: SemiAnalysis] |
| KV path | Mooncake Transfer Engine + NIXL Transfer Engine | [1×: SemiAnalysis] |
| AgentX median input | 140k tokens | [1×: SemiAnalysis] |
| AgentX theoretical median cache-hit roofline | 99.2% | [1×: SemiAnalysis] |
| Next TileRT batch sweep | BS 2, 4, 8 | [1×: SemiAnalysis] |
| Accelerator Model SKUs named | NVIDIA LPU30, LPU40; Cerebras WSE-3, WSE-4 | [1×: SemiAnalysis] |
| InferenceX upcoming silicon | Vera Rubin (NVIDIA committed); TPUv7; MI455X UALoE72 | [1×: SemiAnalysis] |

## Contradiction Check
Supports [[Theses/NVDA - Nvidia]] §Bull Case bullet “Software keeps closing the inference gap” and the CUDA-generality Non-consensus Insight (general-purpose silicon inherits new execution models without a respin): interactivity gains arrive as a *compiler/runtime* on Blackwell the buyer already owns. Challenges the same thesis’s §Bear Case Groq-LPX paragraph, Risk #7 (inference-architecture disruption), and Outstanding Question on whether LPX “validates the bear thesis that GPUs are training chips” — SemiAnalysis’s explicit claim is that specialists now compete against *their own execution model* reimplemented on fungible GPUs, with Xiaomi/Z.ai as the deployment tell. Does **not** falsify the SRAM roofline or Cerebras-class dense-70B points; it compresses addressable specialty TAM to workloads that truly need that roofline or a catalog TileRT cannot compile ([G-10] outside view: software approaches the HBM ceiling, never raises it; #18 do not read one software engine as structural death of dataflow silicon). [G-6]/VLM hypothesis to test: CUDA remains the toll layer others traverse, but TileRT is *community* software (TileLang org), not first-party NVIDIA IP — lock-in is “runs on the GPU fleet you already bought,” not a NVIDIA license line. [G-14] / Automation Lens B: cheaper iso-cost interactivity expands voice/agent SLOs that were uneconomic on conventional GPU decode; NVDA captures the incremental GPU-hours, not the application layer. [G-4]/[G-11]: frenzy-phase GPU overbuild plus expensed compiler effort is the substrate; production capital harvests it as a scheduler flag.

For [[Theses/CRWV - CoreWeave]] §Summary (levered NVIDIA derivative) and Insight #6 / Rubin cash-rate, coverage, vintage: a software speed tier raises the *option value* of an already-financed GPU fleet (reallocate PD mix hour-by-hour instead of buying Groq/Cerebras SKUs), which is constructive for residual value and for Hopper/Blackwell second-cycle usefulness if decode-tail SLOs can be met without next-gen silicon. The same datapoint is adversarial to utilization: 160.4 vs ~240 tok/s/GPU at the 8k/1k slice, plus one-request-per-node, means a customer-driven shift into paid fast modes *lowers* tokens per financed GPU unless the price-per-token markup exceeds ~1.5× or the router keeps most traffic on Pool B. That does not fire CRWV Conviction Triggers (Microsoft renewal, Hopper re-rent >70%, DDTL outlook) — it changes the *workload mix* those re-rent rates will be asked to support. [[Theses/NBIS - Nebius Group]] Insight #4 / AI Studio (full-stack inference as the sole software differentiator versus CRWV’s acquired W&B) is the operator that should productize a TileRT-class pool first; the CLOSE trigger (GPU-collateralized debt / Meta flexible tranche) is untouched. For [[Theses/AMD - Advanced Micro Devices]] Insight #3 (ROCm inference step-function via vLLM/SGLang/MLPerf) and Conviction → LOW (Helios >25% gap to Rubin on published MLPerf): MI355X’s 18.18s decode tail versus TileRT’s 3.01s is a *software-class* gap on NVIDIA silicon, not a chip-spec gap — ROCm parity on conventional engines does not automatically inherit persistent-kernel interactivity. Adjacent notes: [[Research/2026-08-05 - NVDA BEP Inference Specialists vs System Moat - deep-dive]], [[Research/2026-07-23 - Vera Rubin NVL72 vs GB200 Inference TCO - deep-dive]].

## Source Excerpts
> "An 8-GPU HGX B200 server provides a theoretical HBM memory bandwidth of 64 TB/s of in aggregate. At batch size 1, GLM-5 at NVFP4 requires only approximately 21 GB of active-parameter traffic per generated token. The B200 HBM bandwidth roofline would therefore suggest up to 3,047 tokens/s/user without speculative decoding. In practice, GPUs come nowhere close to this limit."

> "TileRT on B200 is in a class of its own. For the 8k/1k input/output token scenario, TileRT reached 340 tokens/s/user on an eight-GPU B200 node. The fastest result in the current dataset was previously 181.4 tokens/s/user on GB300 NVL72 with NVFP4 and MTP, making TileRT 1.9× faster on this metric."

> "At 1k/1k input/output, TileRT FP8 reached 494.2 tokens/s/user. That was 1.9× the best conventional result, at 256.3 tokens/s/user using FP4, and 3.6× the best conventional FP8 result, at 136.3 tokens/s/user."

> "A CUDA graph optimizes the launching of kernels, while TileRT abolishes the kernel as the unit of execution."

> "Thus, with support only for a batch size of 1 user, TileRT is not just a race car, but it is more like a private rocket ship with room for just one passenger."

> "Cerebras, Groq, and SambaNova are no longer competing against a clumsy kernel-launcher. They are competing against their own execution model, running on fungible hardware, reallocated by a config file."

> "At 8k/1k, TileRT reaches 340 tokens/s/user while delivering 35.4 output tokens/s per B200. This comes out to $13.56 per million output tokens. … TileRT therefore costs only 1% more per token while delivering 1.9× the interactivity. … TileRT reaches 340 tokens/s/user for $13.56 per million, 61% cheaper per output token while delivering 3.1× the interactivity."
