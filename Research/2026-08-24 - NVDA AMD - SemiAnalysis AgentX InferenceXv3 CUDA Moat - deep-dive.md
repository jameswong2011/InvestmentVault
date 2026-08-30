---
date: 2026-08-24
tags: [research, Semiconductors, NVDA, AMD]
sector: Semiconductors
ticker: NVDA
source: 'https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat'
source_type: deep-dive
propagated_to: [NVDA, AMD]
---

# AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?

## Thesis Delta
Consensus still prices the CUDA "moat" as a *developer rewrite cost* and prices AMD/ASIC displacement off fixed-sequence MLPerf or day-zero tok/s/GPU snapshots — as if agentic production traffic were still 8k/1k single-turn kernel races → SemiAnalysis AgentX / InferenceXv3 shows production inferencing is now a *systems* workload (multi-turn, ~142k median ISL, ~99% theoretical prefix reuse, sub-agent bursts, KV offload, routing affinity), where NVIDIA's lead is the *rate and breadth of upstream stack maturation* (vLLM/SGLang/TRT-LLM/Dynamo + DCP/PCP) more than raw FLOPs, and AMD can win individual ATOM/e2e slices yet still lose the customer-relevant upstream comparison and the lifecycle integral of tokens. Consensus-vs-source contrast for [[Theses/NVDA - Nvidia]] Insight #1 (CUDA general-purpose moat) and [[Theses/AMD - Advanced Micro Devices]] Insight #3 (ROCm inference step-function): the market variable to watch is *time-to-first-inference + weeks of stack improvement under AgentX*, not a single Pareto point ([G-13]; Industry #8 bottleneck remap to KV/routing/offload).

## Summary
SemiAnalysis announces **AgentX 1.0** — claimed as the first fully open-source, multi-turn agentic *coding* inference benchmark at **1M context** (Apache 2.0) — as the new primary scenario inside **InferenceXv3**, alongside the legacy fixed-sequence scenarios (8k1k, 1k1k, 1k8k) that the authors now treat as incomplete for production traffic. The demand backdrop: since the Claude Code inflection (Nov 2025), long-context multi-turn agentic workloads dominate production inferencing; by April 2026 OpenAI Enterprise *agentic* spending overtook ChatGPT spending. Fixed ISL/OSL benches miss high prefix reuse, sub-agent KV bursts, CPU/DRAM/SSD KV offload, and tool-call timing. AgentX replays anonymized real coding-agent traces (Claude Code, Codex, etc.) collected at **>$3M** token spend; the open subset is on HuggingFace. The live matrix runs on **~2MW** continuous compute across **>1,000 chips** (MI355X, GB300 NVL72, GB200 NVL72, B300, B200, MI325, MI300X, H200, RTX Pro); Rubin is due later the same month as publication, with TPUs and MI455X UALoE72 later in 2026.

The article's investment-relevant claim is not a single "NVIDIA wins" scoreboard. On several frontier open-weight agentic models NVIDIA leads hard on customer-relevant stacks (especially SGLang/vLLM); on others AMD ATOM is competitive or locally ahead on perf/$; and the *most valuable early output* of AgentX is industrial: **50–70+ upstream PRs** across vLLM, SGLang, TensorRT-LLM, ATOM, AITER, Dynamo, LMCache, and Mooncake that transfer to production traffic. Agentic serving is framed as a distributed-systems problem (routers, schedulers, pluggable KV managers, transfer engines) rather than a chip/kernel contest. Explicit CUDA-moat language appears around **decode/prefill context parallelism (DCP/PCP)**: SemiAnalysis calls DCP/PCP "part of CUDA moat" because the AMD implementation is not optimized and every AMD backend in the vLLM support matrix is unsupported. A second structural claim is the **lifecycle integral of throughput at fixed interactivity**: day-zero snapshots mis-rank platforms; B200's early readiness and months of flat high throughput can beat a later higher MI355X peak on cumulative tokens. GB300 rack-scale is repeatedly the revenue/MW and lifecycle winner when wide-EP and disaggregation are available — but on AgentX MiniMax M3, single-node B200/B300 can beat rack-scale on TCO-normalized throughput when Dynamo routing and untuned wide-EP/DCP/TP dominate.

Scope limits the authors stress: configs track recipes.vllm.ai / SGLang cookbook on *upstream* images (not benchmaxed vendor images); both TPS/user and TTFT must be read together; an experimental **E2E Normalized Interactivity** (= OSL/E2EL) is introduced but flagged imperfect; ATOM often leads AMD's curve but most China/West labs refuse ATOM in production (one small Alibaba advertising BU cited; main Qwen org does not use it); a follow-up AgentX update is promised in 3–4 weeks with more AMD/NVIDIA points. Claim scope for investors: agentic traffic *raises* the value of a general-purpose, fast-iterating CUDA/upstream software ecology and remaps the competitive surface from FLOPs to KV lifecycle + routing + offload + TTFI — without proving ASICs irrelevant for stable, short-context, or specialist decode.
 Mechanically, the authors collected 393 anonymized SemiAnalysis Claude Code traces (method akin to Qwen-Bailian), partnered with Anthropic on two Claude Code fixes to make replay possible, and use AIPerf to reconstruct request schedules at varying concurrency. Dataset medians — 142k ISL, 444 OSL, 3.84 s inter-turn, 44% of sessions with subagents — set the KV working-set and routing problem that fixed 8k1k never sees. The CUDA-moat question in the title is answered operationally: moat surfaces that AgentX stresses are context-parallelism support, upstream recipe velocity, TTFI, and hybrid KV correctness — not a permanent monopoly on every Pareto point.
 Numerically, the open AgentX corpus is small in session count (393) but large in context (median ISL 142k; tails to 1M; 1,697 subagent rollouts), which is exactly the regime where HBM working sets (22M tokens on B200 vs 43M on B300 in the DeepSeek offload vignette), write-through DRAM pools, and prefix-aware routing dominate chip-level kernel deltas. That is why SemiAnalysis can simultaneously report 'amazing performance from both NVIDIA and AMD' and still title the piece around whether the CUDA moat holds: the moat under test is the ability to keep the entire agentic serving graph correct and improving under open upstream recipes, not whether MI355X can print a local ATOM win.

## Framework / Mental Model
**AgentX workload definition (four elements).** (1) Multi-turn sessions (tens–hundreds of user/assistant turns vs chatbot handfuls); (2) long context (system prompts, tool defs, accumulating history); (3) high prefix reuse (turn *n* concatenates turn *n−1* output; cached/uncached ratio → 1 as *n* grows, conditional on KV storage); (4) sub-agent bursts (short-lived fresh-context agents → bursty KV patterns that can evict the main agent if poorly scheduled). Implication: agentic inference is a *systems* problem (NIXL/MORI-IO/Mooncake transfers; LLM-d/Dynamo/vLLM/SGLang routers; DRAM/SSD offload via Mooncake Store, LMCache, vLLM Simple Offloading, SGLang HiCache).

**InferenceX Pareto + TCO normalization.** Axes remain interactivity (tok/s/user = 1/TPOT) vs throughput (tok/s/GPU or perf/$ / perf/MW). AgentX adds concurrent-session sweeps against a single deployment with realistic inter-turn delays; frontend now merges allowed optimizations onto one best curve per (model, SKU, engine) while exposing per-point provenance. KV-offload points marked with dotted circles.

**E2E Normalized Interactivity (experimental).** Defined as OSL/E2EL ≈ interactivity (1/TPOT) plus a TTFT penalty. Captures joint responsiveness; heavily penalizes high TTFT; imperfect for PD-disagg nuances. AgentX v1.0 still optimizes TPS and TTFT separately.

**Lifecycle integral of tokens (Q(t,s)).** At fixed interactivity target *s*, integrate highest validated throughput from first production-ready date *t₀* to cutoff *t₁*. Approximated as a step sum between InferenceX measurements (no retroactive credit). Variants: $/M tokens, tokens/MW, revenue/MW. Separates three conflated claims: (i) higher point-in-time result, (ii) earlier production readiness (TTFI), (iii) larger lifecycle integral.

**Distributed inference stack model.** Routers (vLLM router, llm-d, SGLang gateway, ATOM Mesh) → engine schedulers (vLLM, SGLang, TRT-LLM, ATOM) → pluggable KV connectors (MooncakeStoreConnector, etc.) → transfer engines (Mooncake TE, NIXL/UCX/GPUDirect). Platforms (NVIDIA Dynamo, llm-d, AMD Infera) package combinations as k8s distributions. Context parallelism splits as PCP (prefill, compute-bound query chunks) and DCP (decode, BW-bound KV shards, flash-decode merge).

**Fair speculative decoding on synthetic traces.** Anonymized 64-token hash blocks are filled from a synthetic coding/tool pool (preserves KV-reuse timing, not semantics). Acceptance lengths forced from SPEED-Bench averages per (model, speculator, draft length, thinking mode) so vendors cannot game AgentX with unnatural accept rates on synthetic tokens.

## Evidence

| Program / demand backdrop | Figure | Tag |
|---|---|---|
| Claude Code inflection | Nov 2025 | [1×: SemiAnalysis] |
| OpenAI Enterprise agentic spend vs ChatGPT | Agentic overtook ChatGPT, Apr 2026 | [1×: SemiAnalysis] |
| AgentX context target | 1,000,000 tokens | [1×: SemiAnalysis] |
| Dataset build cost | >$3M USD token spend | [1×: SemiAnalysis] |
| Continuous bench power | ~2 MW | [1×: SemiAnalysis] |
| Chips in matrix | >1,000 | [1×: SemiAnalysis] |
| SKUs named (AgentX matrix) | MI355X, GB300 NVL72, GB200 NVL72, B300, B200, MI325, MI300X, H200, RTX Pro | [1×: SemiAnalysis] |
| Upcoming silicon on InferenceX | Rubin (later same month); TPUs; MI455X UALoE72 (later 2026) | [1×: SemiAnalysis] |
| Upstream PRs attributed to AgentX | 50+ / "70+" (article uses both) | [1×: SemiAnalysis] |
| License | Apache 2.0 | [1×: SemiAnalysis] |
| Internal Claude Code traces (initial corpus) | 393 sessions | [1×: SemiAnalysis] |
| Sessions with ≥1 subagent | 175 (~44%) | [1×: SemiAnalysis] |
| Total subagent rollouts | 1,697; median 4 / session | [1×: SemiAnalysis] |
| Median subagent wall-clock | 2.27 min | [1×: SemiAnalysis] |
| Median ISL / OSL (AgentX dataset) | 142k / 444 tokens | [1×: SemiAnalysis] |
| Median inter-turn (tool-use) latency | 3.84 s; ~10% >1 min | [1×: SemiAnalysis] |
| Truncated dataset for ≤256k models | 256k context | [1×: SemiAnalysis] |
| Profiling duration / idle cap | 1 hour / 5 min (Anthropic default KV TTL) | [1×: SemiAnalysis] |
| Warmup | primer at 25–75% of conversation + 10 extra 1-token requests / lane | [1×: SemiAnalysis] |

| DeepSeek V4 Pro 0813 (AgentX themes) | Figure | Tag |
|---|---|---|
| Model size | ~1.6T total / 49B active | [1×: SemiAnalysis] |
| Acceptable p90 TTFT (production agentic) | 200–5,000 ms; >5–10 s pushes "online" boundary | [1×: SemiAnalysis] |
| Pre-2026-08-21 | MI355X SGLang matched B200 vLLM on e2e perf/$ | [1×: SemiAnalysis] |
| Still ahead of MI355X pre-cut | B300 vLLM; B200 SGLang | [1×: SemiAnalysis] |
| Post-2026-08-21 | B200 vLLM perf/$ surpassed MI355X (Inferact + NVIDIA vLLM opts) | [1×: SemiAnalysis] |
| ATOM MI355X vs B200 vLLM e2e | ATOM wins e2e vs B200 vLLM; loses to B300 and B200 SGLang | [1×: SemiAnalysis] |
| ATOM production adoption | ~1 small Alibaba advertising BU; main Qwen org does not use ATOM | [1×: SemiAnalysis] |
| NVIDIA competitive configs | GB300 Dynamo TRT-LLM; GB200 Dynamo vLLM; PD disagg; GB300 wide-EP DEP32 decode | [1×: SemiAnalysis] |
| B300 vs B200 HBM | B300 +50% HBM vs B200 | [1×: SemiAnalysis] |
| B300 @ 384 concurrent traces (DEP8 + 3TB DRAM simple offload) | 91% HBM hit + 1.36% DRAM hit; ~43M-token HBM working set | [1×: SemiAnalysis] |
| B200 @ concurrency 196 (same other params) | 73% HBM hit; ~20% DRAM offload hit; ~22M-token HBM working set | [1×: SemiAnalysis] |
| DRAM offload sizing heuristic | DRAM pool ~1.5–3× HBM KV capacity (write-through) | [1×: SemiAnalysis] |
| MI355X HBM vs B200 | ~1.5× HBM over B200; needs DEP kernel work for high-throughput region | [1×: SemiAnalysis] |
| Disagg 1xDEP8+1xDEP8 (AMD) | Slight high-throughput gain; worse low-latency; p90 TTFT spike; prefill-delayer above conc. 64; chunked prefill 8,192→65,536 | [1×: SemiAnalysis] |

| Kimi K3 / MiniMax M3 / Qwen3.5 / GLM 5.3 (AgentX) | Figure | Tag |
|---|---|---|
| Kimi K3 size | 2.8T params (open-weight proxy for Claude Mythos/Fable5-class) | [1×: SemiAnalysis] |
| K3 fit | Does not fit single B200; needs wide EP/TP or PP | [1×: SemiAnalysis] |
| Early B200 K3 issue | Spec decode / DSpark would not compose with PP → MI355X mogged B200 until fixed | [1×: SemiAnalysis] |
| MI355X day-0 vs week-1 on long-context multi-turn | Short-context OK day-0; AITER/Triton "panic"; upstream vLLM unusable week-1 on realistic K3 | [1×: SemiAnalysis] |
| MI355X ATOM vs GB300 NVL72 vLLM | ATOM beats GB300 vLLM on perf/$ on part of 40–60s e2e latency band | [1×: SemiAnalysis] |
| MiniMax M3 size | 432B | [1×: SemiAnalysis] |
| M3 crown | B300 TRT-LLM TP2; "NVIDIA absolutely destroys" competitors; AMD "horrible" at high context (incentive = short-context tuning) | [1×: SemiAnalysis] |
| GB200 conc. 40 TP4/EP4/DPA vs plain TP4 | 0.60× throughput; >3× p90 TTFT | [1×: SemiAnalysis] |
| GB200 conc. 32 cache | 28.8% actual vs 96.0% theoretical; 300k-token session on wrong DP rank recomputes all | [1×: SemiAnalysis] |
| M3 P90 ISL | 317k; no submission runs context parallelism | [1×: SemiAnalysis] |
| KV offload on Pareto | NVIDIA: all optimal points use offload above conc. 20; AMD: none (hipMemcpyBatchAsync missing until ROCm 7.14 → serialized memcpy) | [1×: SemiAnalysis] |
| Qwen3.5 397B | GatedDeltaNet hybrid; native max ctx 262k (truncated dataset); NVIDIA SGLang >20× better at 90 tok/s/user vs AMD; zero AMD SGLang competition | [1×: SemiAnalysis] |
| B300 FP4 vs H100 (Qwen3.5) | 12× better perf/$ | [1×: SemiAnalysis] |
| GLM 5.3 base | GLM5.2 744B + post-training | [1×: SemiAnalysis] |
| GLM 5.3 @ 150 tok/s/user p90 | NVIDIA up to 5× better cost efficiency on OSS SGLang; even "free AMD chip" still loses on $/token after hosting/power | [1×: SemiAnalysis] |
| GLM 5.3 ATOM | Better perf/$ than GB300 NVL72 SGLang and some TRT-LLM points on E2E Normalized Interactivity band | [1×: SemiAnalysis] |

| Selected upstream optimization deltas (AgentX-driven) | Figure | Tag |
|---|---|---|
| vLLM hybrid prefix retention | >95% prefix-cache hit @ 14 concurrent, contexts to 1M | [1×: SemiAnalysis] |
| SimpleCPU offload + DeepSeek-V4 hybrid | +81.7% output throughput; −46.6% mean e2e vs recompute once HBM full | [1×: SemiAnalysis] |
| ROCm AITER sparse-MLA decode (Kimi-K3 path) | +5.22% AgentX output throughput | [1×: SemiAnalysis] |
| DeepSeek V4 C4A selector hybrid AITER/native (gfx950) | E2E selector 1.21–1.76×; decode-kernel geomean 1.2–2.9× over 84-shape matrix | [1×: SemiAnalysis] |
| SGLang FlashInfer GDN checkpoints | 47,771 → 53,004 tok/s/GPU @ 92.4% cache-hit | [1×: SemiAnalysis] |
| SGLang runtime-scalar context length (vs per-length compile) | AgentX conc. 384: +26.75% output throughput; −36.25% mean TTFT | [1×: SemiAnalysis] |
| SGLang decode-interval after prefill (DSv4 Pro) | +141% output throughput; −97.3% p99 inter-token latency; median TTFT 36.5→59 s | [1×: SemiAnalysis] |
| SGLang staging-buffer radix fix (127.5k shared prefix) | Needles 2/128 → 128/128 correct; +9.6% median per-user throughput | [1×: SemiAnalysis] |
| Drop unused PREBUILT prompt transfer (AgentX GB300) | +18.0% per-user output; +12.7% decode tok/s/GPU | [1×: SemiAnalysis] |
| TRT-LLM boundary-aware incremental tokenization (Qwen3.5) | 1,087/1,087 transitions match full tokenize; mean 185.1→11.3 ms | [1×: SemiAnalysis] |
| TRT-LLM MiniMax-M3 KV p99 (NIXL bounce path) | Conc.5: 26.74s→125ms; conc.40: 10.15s→288ms | [1×: SemiAnalysis] |
| TRT-LLM MiniMax context-graph producers | +12.58% per-user output throughput | [1×: SemiAnalysis] |
| TRT-LLM MXFP8 CuTeDSL autotune (M3) | ~+7–10% output tok/s/GPU at low-concurrency aggregates | [1×: SemiAnalysis] |
| DeepSeek-V4 sparse SWA checkpoint retention | Prefix hit 5.6%→96.45% @ conc.48; sliding-window gate losses 91.35%→0.16% | [1×: SemiAnalysis] |
| Standalone LMCache 32k prefix reload vs recompute | ~0.32 s vs ~2.5 s (~8×) | [1×: SemiAnalysis] |
| ATOM PCP | −35–43% mean TTFT; up to ~+49% total throughput @ 64k input | [1×: SemiAnalysis] |
| ATOM GLM-5.2 high load (complete result cited) | Throughput ~2×; median TTFT 28.6→8.7 s; 3.68× KV blocks / prefill GPU | [1×: SemiAnalysis] |

| Lifecycle integral / fixed-sequence archive (selected) | Figure | Tag |
|---|---|---|
| Kimi K2.5 integral setup | Single-node 8k1k @ 35 tok/s/user median; cutoff Aug 18, 2026 | [1×: SemiAnalysis] |
| B200 first / Mar 11 jump | Feb 24: 1,104 tok/s/GPU → Mar 11 vLLM v0.17.0: 3,776 (3.4× in ~2 weeks); Aug 7: 3,813 | [1×: SemiAnalysis] |
| MI355X vLLM path | Mar 26 debut 1,431; Jul 30 nightlies 2,873 | [1×: SemiAnalysis] |
| MI355X ATOM FP4 Jul 12 | 4,081 tok/s/GPU (> every B200 result in scenario); @ 75 tok/s/user: 2,261 vs B200 2,083 | [1×: SemiAnalysis] |
| Lifecycle tokens/GPU (K2.5) | B200 53.8B; MI355X 35.2B; B300 45.6B (single strong Apr 20 launch 4,381) | [1×: SemiAnalysis] |
| MI355X head-start gap vs B200 | +30 days TTFI | [1×: SemiAnalysis] |
| MiniMax M3 day-0 → +3 weeks | Jun 13: MI355X 1,072 / B200 1,890 → Jul 3/6: 8,662 (8.1×) / 8,945 (4.7×); integrals ~42.7B vs 42.4B | [1×: SemiAnalysis] |
| DeepSeek v4 8k1k revenue/MW vignette | 10 MW; 1-week ramp; OpenRouter DSv4 Pro 0813 prices; GB300 maximizes revenue; ΔTTFI GB300 +1 week vs B200/B300; MI355X +2 weeks vs B200/B300; GB300 >2× Δ$/W vs MI355X | [1×: SemiAnalysis / est. from SA charts] |
| Qwen3.5 fixed-seq archive | 1,028 datapoints; 49 dates; 97 CI runs; 42 images; Feb 17–Aug 19, 2026 | [1×: SemiAnalysis] |
| MiniMax M3 fixed-seq archive | 1,977 datapoints; 30 dates; 89 CI; 25 images; Jun 12–Aug 4, 2026 | [1×: SemiAnalysis] |
| GLM 5 FP8 SGLang (deprecated model) | @25 tok/s/user MI355X ~94% of B200 (1.7k vs 1.8k); @35 ~77%; @75 ~68%; AMD improved ~4.8×; NVIDIA ~4.68× | [1×: SemiAnalysis] |
| Kimi K2.X 8k1k submissions | 60 submissions Feb 18–Aug 7, 2026 | [1×: SemiAnalysis] |
| B200 DEP8 (Aug nightly; conc. 512 / 1024) | 6.14k tok/s/GPU @ 1.15s TTFT vs ~3.9k @ ~50s TTFT for TP8/TEP8; 7.66k @ conc. 1024 | [1×: SemiAnalysis] |
| MI325X v0.18→v0.21 (8k/1k) | Throughput/GPU +1.9–2.6×; median TTFT −43–53% | [1×: SemiAnalysis] |
| NVIDIA v0.15.1→v0.20.2 (8k/1k) | Throughput/GPU +8–28%; median TTFT −20–37% (conc. 4–64) | [1×: SemiAnalysis] |

| Privacy / replay / fairness mechanics | Figure | Tag |
|---|---|---|
| Anonymization | 64-token blocks → session-scoped chained hashes; no prompts/code/tool args/results | [1×: SemiAnalysis] |
| Trace format | WEKA (Callan Fox / kv-cache-tester); mappable to Mooncake | [1×: SemiAnalysis] |
| Replayer | AIPerf (NVIDIA-origin); AgentX maintains vendor-neutral fork | [1×: SemiAnalysis] |
| Session graph | DAG with spawn/join subagents; auxiliary one-offs never join | [1×: SemiAnalysis] |
| Spec-decode fairness | Forced acceptance lengths from SPEED-Bench averages | [1×: SemiAnalysis] |
| Post-processing filters | Drop Claude Code security-monitor / title-gen; drop reconstructed ISL >990k; drop duplicates | [1×: SemiAnalysis] |
| OSS supporters named | Meta, Microsoft, Oracle, OpenAI, MiniMax, Moonshot Kimi, Alibaba Qwen, Zhipu GLM | [1×: SemiAnalysis] |
| Partner engines named | Inferact/vLLM, RedHat/llm-d, RadixArk/SGLang, LMCache/TensorMesh, Weka, Mooncake, AMD, NVIDIA TensorRT-LLM | [1×: SemiAnalysis] |
| Follow-up cadence | AgentX update article in 3–4 weeks (more AMD/NVIDIA opts + results) | [1×: SemiAnalysis] |
| GDN / LatentMoE credit | NVIDIA Research fundamental work used on frontier models (vs Nemotron3 Ultra end-to-end training critique) | [1×: SemiAnalysis] |
| Qwen3.8 contrast (Nemotron critique) | Nemotron3 Ultra "massively beaten" by Qwen3.8 27B (author aside) | [1×: SemiAnalysis] |


| GB300 / rack-scale AgentX nuances | Figure | Tag |
|---|---|---|
| NVIDIA competitive AgentX configs (DeepSeek-class) | GB300 Dynamo TRT-LLM; GB200 Dynamo vLLM; PD disagg; wide-EP DEP32 decode on GB300 | [1×: SemiAnalysis] |
| GB200 vs GB300 concurrency/TTFT trade | Higher GB300 concurrency → more subagent cold prefills → worse TTFT vs closer TPS | [1×: SemiAnalysis] |
| MiniMax M3 rack vs node | B200/B300 beat GB200/300 on TCO-normalized throughput when wide-EP/DCP/TP untuned | [1×: SemiAnalysis] |
| Dynamo router bottleneck | Work scales with number and length of live prefixes | [1×: SemiAnalysis] |
| Context parallelism on M3 | No submission despite P90 ISL 317k; DCP caps at 2 with 4 KV heads even at TP8; MSA indexer needs own CP handling | [1×: SemiAnalysis] |
| vLLM vs TRT-LLM (M3 themes) | Comparable throughput vs p90 interactivity; vLLM better throughput vs p90 TTFT | [1×: SemiAnalysis] |
| Chunked-prefill metadata / FA4 note (NVIDIA nightlies) | Conc. 32/64 v0.25 points failed FA4 MLA output-stride — not a valid frontier | [1×: SemiAnalysis] |
| DEP8 recipe GMU | Lowered 0.90→0.80 for replicated attention/KV headroom | [1×: SemiAnalysis] |
| Unconditional checkpoint publish cost | −17.5% throughput on zero-hit traffic if always publishing | [1×: SemiAnalysis] |
| TRT-LLM corrupt split-K MoE tactics | Crashed 5/7 AgentX runs before disable; 0/7 after | [1×: SemiAnalysis] |
| Device-scalar sync removal (DSv4 sparse metadata) | Eliminated 18× 4-byte device reads / step forcing cudaStreamSynchronize on GB300 context worker | [1×: SemiAnalysis] |
| AITER 64-bit addressing | Runtime 64-bit dispatch for batch prefill >4 GB; MLA offsets >2 GB; pools ~150M rows | [1×: SemiAnalysis] |

## Key Segments

### AgentX demand shift and benchmark charter
Production inferencing has flipped from chatbot-like fixed sequences to agentic coding traffic: multi-turn, long context, high prefix reuse, sub-agent bursts, and tool calls. SemiAnalysis positions AgentX 1.0 / InferenceXv3 as the industry measurement standard for that reality — open frontend, public REST DB already consumed by tier-1 lab capacity-planning teams, GitHub Actions CI provenance, accuracy validation per point, and recipes pinned to upstream vLLM/SGLang images so measured performance matches what customers actually run. Fixed-sequence scenarios remain as a kernel/baseline strip-down and for historical software-maturation curves, but are explicitly less representative of current production. The charter's economic backdrop — agentic spend overtaking ChatGPT at OpenAI Enterprise, power (not "unlimited" lab capital) as the binding constraint — reframes SKU choice as tokens per MW and revenue per MW under realistic KV pressure, not peak bench FLOPs.

### Agentic performance themes across frontier open-weight models
Results are model-conditional, not a universal NVIDIA wipeout or AMD breakthrough. DeepSeek V4 Pro 0813 is a close B200/B300/MI355X race where mid-August Inferact/NVIDIA vLLM work flipped B200 ahead of MI355X on perf/$, while ATOM can win e2e slices customers will not ship. Kimi K3 (2.8T) exposes composition gaps (spec decode × pipeline parallel on B200; AITER panic on MI355X long-context) and a band where ATOM beats even GB300 NVL72 vLLM on perf/$. MiniMax M3 is a NVIDIA rout (B300 TRT-LLM TP2) where AMD's short-context tuning incentive shows up as "horrible" long-context software, DP-attention cache locality collapses (28.8% vs 96% theoretical), and single-node beats rack-scale on TCO when wide-EP/DCP are untuned and Dynamo routing scales with live prefixes. Qwen3.5 (GatedDeltaNet) is a CUDA/SGLang fortress (>20× at 90 tok/s/user; zero AMD SGLang competition). GLM 5.3 is the starkest $/token statement: at 150 tok/s/user, NVIDIA's SGLang lead is large enough that a free AMD chip still loses after opex — even as ATOM looks good on the experimental E2E Normalized Interactivity axis versus some GB300 points. Across models, read TPS and TTFT jointly; "acceptable" p90 TTFT for agentic is roughly 200 ms–5 s.

### Industry impact — agentic serving as a systems stack
The authors argue AgentX's first-order effect is 50–70+ upstream PRs that harden production paths: hybrid-attention prefix retention, CPU KV offload for hybrid layouts, Mooncake/NIXL transfer correctness, DP cache affinity, decode-vs-prefill fairness, boundary-aware incremental tokenization, and coalesced disagg KV descriptors. Sub-agents that evict the main agent's cache, write-through DRAM offload sizing (1.5–3× HBM), and router affinity under data-parallel attention are first-class failure modes invisible on 8k1k. SemiAnalysis's multi-year AMD software collaboration is credited with modernizing AMD OSS toward "first class" agentic support — while still calling out ATOM-vs-upstream divergence and missing ROCm primitives (hipMemcpyBatchAsync until 7.14). Platforms (Dynamo, llm-d, Infera) are packaging layers over engines + KV managers + transfer libraries, not monolithic runtimes.

### CUDA moat surfaces that AgentX actually stresses
Explicit moat language attaches to **DCP/PCP** (NVIDIA Research–origin context parallelism): long context makes TP/DP attention suboptimal; PCP parallelizes prefill FLOPs; DCP parallelizes decode KV reads; AMD backends are unsupported in the vLLM matrix — "DCP/PCP forms part of CUDA moat." Adjacent soft-moat surfaces in the article: (i) upstream image quality and recipe velocity on vLLM/SGLang/TRT-LLM; (ii) GB300 scale-up world size enabling wide-EP and tilting economics toward disaggregation when software is ready; (iii) TTFI and lifecycle integral advantages when NVIDIA stacks reach production weeks earlier; (iv) hybrid-model offload/disagg state movement (conv+ssm recurrent state, GDN checkpoints) where CUDA-ecosystem libraries land first. Counter-evidence the article itself supplies: ATOM can beat NVIDIA points on perf/$ bands; MI355X can lead fixed-sequence peaks; B200 historically lost to MI355X on K3 until software composed; rack-scale can lose AgentX TCO when routers/kernels are immature. Moat holds as *ecosystem iteration under agentic systems load*, not as permanent kernel monopoly.

### Methodology, replay harness, and fairness constraints
Traces are privacy-preserving: tokenize → 64-token blocks → session-scoped chained hashes (no prompts, code, tool args/results). WEKA trace format; AIPerf (NVIDIA-origin, AgentX fork for vendor neutrality) replays sessions as DAGs with inter-turn delays and subagent spawn/join structure; auxiliary one-offs (title generation, `/btw`) modeled separately. Warmup reconstructs mid-conversation state then advances 10 one-token steps; profiling is one hour with 5-minute idle caps; cache-bust markers allow concurrency >393. Speculative decoding uses forced acceptance lengths from SPEED-Bench to avoid synthetic-token accept-rate distortion. Visualization merges optimization families onto best-available curves with per-point provenance; future work includes NVMe offload, structured message boundaries for smarter PD routing, and better north-star metrics than raw e2e latency (which scales with OSL tails).

### Lifecycle integral case studies and fixed-sequence deprecation
Kimi K2.5 shows why integrals beat peaks: B200's February readiness and ~3.8k tok/s/GPU plateau accumulate 53.8B tokens/GPU vs MI355X 35.2B despite ATOM's July 4,081 peak. MiniMax M3 shows matched day-zero starts and near-tied integrals after AMD's 8.1× three-week climb. DeepSeek v4 revenue/MW vignette: GB300 maximizes accumulated revenue despite +1 week TTFI vs B200/B300, with MI355X another week behind — "rack scale architecture is a decisive advancement" when wide-EP/disagg software exists. Fixed-sequence archives (Kimi K2.X sixty 8k1k submissions; Qwen3.5 1,028 points; M3 1,977 points; GLM 5 FP8 parity study) document multi-fold post-launch software gains on both vendors and the pattern that MI355X is relatively strongest at throughput-oriented operating points while B200/B300 widen the gap at stricter interactivity. AgentX is now the main scenario; most single-turn 8k1k runs are deprecated.

### Router, KV-manager, and transfer-engine failure modes under AgentX
Agentic traffic makes the "pluggable" inference ecosystem load-bearing. A request that carries megabytes of cached prefix must stick to the rank that holds it; a cold redirect is an expensive recompute, not a free load-balance win. SemiAnalysis documents DP cache affinity in SGLang (prefill and decode halves deciding consistently; cache balance as a routing signal so affinity does not collapse onto one hot worker), hybrid cache events becoming radix- and sliding-window-aware, and Dynamo-router cost scaling with the number and length of live prefixes — a reason single-node B200/B300 can beat GB200/GB300 on MiniMax M3 TCO-normalized throughput when wide-EP/wide-DCP/wide-TP kernels are missing. Mooncake Store plus Mooncake Transfer Engine can share a node with vLLM (each worker contributes host DRAM to an external pool via MooncakeStoreConnector) while NIXL separately moves request-specific KV from prefill GPUs to decode GPUs over UCX/GPUDirect; multiple KV paths therefore coexist inside one engine. Correctness bugs dominate the AgentX changelog: sliding-window pages evicting durable prefixes; ring-cache slot reuse yielding wrong output; staging buffers scattering shared-prefix KV to the wrong decode offsets (127,500-token needle test 2/128 → 128/128); speculative/EAGLE/MTP draft state dropped across Mooncake groups or prefill→decode boundaries; Kimi-K3 conv+ssm recurrent state omitted from MoRI-IO 1P1D splits so decode starts uninitialized. Throughput benches would have scored several of these as "fast." AgentX's north-star role is forcing upstreams to treat them as production blockers.

### Software velocity asymmetry and the ATOM vs upstream customer gap
Two AMD software stories run in parallel and must not be conflated. Story A — velocity: MI355X/ATOM and ROCm nightlies deliver multi-fold gains inside weeks (GLM 5 ~4.8×; MiniMax M3 8.1× in three weeks; PCP cutting mean TTFT 35–43%; GLM-5.2 high-load ATOM doubling throughput and cutting median TTFT 28.6→8.7 s). Story B — customer stack: "most AI labs in China or the west do not want to use ATOM in production" except one small Alibaba advertising BU; the main Qwen org does not; vLLM remains the relevant comparison for upstream open-source buyers. AgentX repeatedly shows ATOM points that beat NVIDIA on a band (K3 40–60 s e2e perf/$; some GLM E2E Normalized Interactivity slices; K2.5 peak 4,081 tok/s/GPU) while the same article's customer-relevant ranking uses vLLM/SGLang where NVIDIA flipped ahead of MI355X on DeepSeek V4 perf/$ after 2026-08-21 Inferact/NVIDIA commits, owns Qwen3.5 SGLang by >20× at 90 tok/s/user, and owns GLM 5.3 SGLang by up to 5× at 150 tok/s/user. Missing ROCm primitives amplify the gap: without hipMemcpyBatchAsync (until ROCm 7.14), vLLM Simple CPUOffloading serializes GPU↔CPU memcpy, so none of AMD's MiniMax Pareto-optimal AgentX points use DRAM KV offload while every NVIDIA optimal point above concurrency 20 does. Investment read: AMD's hardware (including ~1.5× HBM vs B200) is not the binding constraint on agentic competitive position; upstream feature parity and lab willingness to run non-ATOM engines are.

### Power, TCO lenses, and what the article does not claim
SemiAnalysis layers three operator lenses on top of raw tok/s: performance per dollar, performance per megawatt, and lifecycle revenue per megawatt at a fixed interactivity SLO (own-as-hyperscaler, own-as-neocloud, three-year rental cost bases on the public TCO calculator). The DeepSeek v4 8k1k vignette — 10 MW, one-week ramp, OpenRouter DSv4 Pro 0813 prices — maximizes revenue on GB300 despite a one-week TTFI lag vs B200/B300 and a two-week lag for MI355X, with GB300 more than doubling MI355X on Δ$/W and pulling ahead on accumulated revenue via faster post-launch software. That is a rack-scale + software co-evolution proof point when wide-EP and disaggregation are live — not a claim that every AgentX model prefers NVL72 (MiniMax M3 counterexample). The article does **not** deliver Rubin, TPU, or MI455X UALoE72 numbers yet; does **not** crown a single SKU across all frontier models; does **not** measure Cerebras/Groq/SRAM specialists on AgentX; and does **not** assert that ASICs cannot win stable non-agentic inference. Its falsifiable near-term tell for the CUDA-moat question under agentic load is whether AMD closes DCP/PCP + upstream hybrid-offload + lab-adopted engine parity before the next AgentX update (promised in three to four weeks), and whether NVIDIA's GB300 AgentX software catches the article's own critique of under-tuned rack-scale recipes.

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] Key Non-consensus Insight #1 (CUDA as general-purpose architectural moat, not merely rewrite cost) and Bull Case software/Jevons lines: agentic production traffic expands the *systems* surface (KV lifecycle, routing, DCP/PCP, hybrid offload) where CUDA-adjacent upstream stacks iterate weekly, and GB300 lifecycle revenue/MW leadership reinforces scale-up + software co-evolution. Supports the TileRT-era read in [[Research/2026-08-10 - NVDA TileRT Ultra-High Interactivity InferenceX - deep-dive]] that InferenceX is shifting from fixed sequences to AgentX — this article *is* that shift shipping. **Challenges** a naive "CUDA moat = permanent tok/s lead on every model" reading of the same Insight: AMD ATOM and MI355X win identifiable bands (K3 e2e perf/$ slice; some GLM ATOM points; K2.5 peak tok/s); day-zero and fixed-sequence snapshots can flatter either vendor. **Challenges** [[Theses/NVDA - Nvidia]] Bear Case ASIC/inference-displacement when the displacement thesis assumes stable short-context transformers — AgentX says the growing traffic share is the opposite shape — but does **not** falsify ASIC economics for stable, high-volume, non-agentic decode (article scope is GPU/accelerator serving stacks, with TPUs still "later this year" on the bench).

For [[Theses/AMD - Advanced Micro Devices]]: supports Insight #3's *direction* (ROCm/vLLM/SGLang path can close gaps fast — 4.8× GLM 5, 8.1× M3 in weeks) but **challenges** treating ATOM headline wins as customer-equivalent to upstream vLLM/SGLang (labs avoid ATOM; hipMemcpyBatchAsync gap; DCP/PCP unsupported; Qwen3.5/GLM 5.3/M3 agentic gaps). Touches AMD Conviction **→ CLOSE if** "ROCm is publicly de-prioritized… in favor of CUDA-only" as an *evidence-touched* observable in the direction of risk: the article's customer-relevant comparison repeatedly privileges upstream CUDA-centered stacks, while AMD's best points sit on ATOM. Does **not** fire AMD → LOW Helios/MLPerf gap triggers (different benchmark family; Rubin not yet in matrix). For [[Theses/CRWV - CoreWeave]] / [[Theses/NBIS - Nebius Group]]: lifecycle integral + AgentX TCO pages (hyperscaler own / neocloud own / 3-year rental) raise the option value of fleets that can absorb weekly stack gains and PD/KV software — constructive for residual value — while TTFI gaps and model-specific software holes are utilization/revenue-per-MW risks, not balance-sheet triggers. Adjacent: [[Research/2026-08-05 - NVDA BEP Inference Specialists vs System Moat - deep-dive]], [[Research/2026-07-25 - AMD Advancing AI CUDA Moat Helios - deep-dive]], [[Sectors/Compute & AI Compute Accelerators]], [[Sectors/Neoclouds & GPU-as-a-Service]].

Mental-model triggers to carry into `/sync` (hypotheses, not verdicts): [[Generalist - Overview]] [G-6] software-like monopoly characteristics · [G-11] expensed intangible stack investment · [G-13] mispriced variable = agentic systems-software velocity / TTFI · [G-14] Jevons from longer agentic traces; [[Industry - Semiconductors]] #2 qualification/software gate · #8 bottleneck remap (KV/routing/offload vs raw GEMM) · #18 price-vs-volume (tokens/MW vs capex optics); [[Lens - Value Layer Monopoly]] toll is workload-conditional — holds inside CUDA-upstream agentic serving, contested on ATOM-only peaks and still-unbenchmarked TPUs.

## Source Excerpts

> "Agentic inference is inherently a systems problem."

> "Before August 21, 2026, AMD's MI355X strong SGLang development team was matching B200 vLLM on performance per dollar on end to end (e2e) performance. … After August 21, 2026, due to optimizations in vLLM from Inferact and Nvidia, the performance per dollar of Nvidia's B200 has surpassed that of the MI355X."

> "Qwen3.5 397B is a strong hold for NVIDIA on SGLang versus SGLang, with over 20x better performance at 90 tok/s/user. There is currently zero competition from AMD for Qwen3.5 SGLang."

> "A platform with lower performance on day zero may still produce more tokens over the model lifecycle if its software stack improves more quickly."

> "The issue with this is that most AI labs in China or the west do not want to use ATOM in production besides 1 small advertising business unit at Alibaba Corp due to tons of missing features."

> "Today, we announce AgentX 1.0 - the world's first fully open source, multi-turn agentic coding inference benchmark at 1 million context, released under Apache 2.0."

> "In April 2026, OpenAI's Enterprise agentic spending overtook ChatGPT spending."

> "Reality is multi-turn, long context, high prefill reuse, with sub agent bursts, KVCache offload, and numerous tool calls."

> "DCP/PCP forms part of CUDA moat as the AMD implementation of DCP/PCP isn't optimized yet. In the vLLM support matrix, every single AMD backend is unsupported."

> "With the current state of AMD software, at 150 tok/s/user, Nvidia's performance advantage is so great that even if the competitor chip hardware was sold for free (but with providers still of course paying for datacenter hosting and power and other operating costs), cost per token would still be cheaper when using Nvidia."

> "Judging by the integral analysis, B200 wins not because it was faster at the end, but because it got there earlier in February and held the line for six months."

> "Even though GB300 had a TTFI longer than the other Nvidia chips, accumulated revenue quickly caught up for the GB300 due to fast software development and lifecycle profit is decisively higher for the GB300 NVL72."

> "The most valuable thing AgentX produced in its first months was not the initial results. It was the massive industry impact the benchmark is already having. Over 70+ upstream PRs…"

> "ATOM is currently AMD's best-performing engine, but vLLM remains the more relevant comparison for customers using an upstream open-source serving stack."
