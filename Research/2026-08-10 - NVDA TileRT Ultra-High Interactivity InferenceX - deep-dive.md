---
date: 2026-08-10
tags: [research, Semiconductors, NVDA]
sector: Semiconductors
ticker: NVDA
propagated_to: [NVDA]
source: 'https://newsletter.semianalysis.com/p/ultra-high-interactivity-on-nvidia'
source_type: deep-dive
---

## Thesis Delta
Consensus prices NVIDIA’s inference stack as a throughput/TCO machine whose specialty-chip threat (Cerebras/Groq/SambaNova) owns the ultra-low-latency “fast mode” tier → SemiAnalysis’s TileRT InferenceX results imply that software-only persistent decode on commodity B200 nodes can already deliver ~2–3× higher tok/s/user than conventional GB300 engines at batch-1, reframing specialty SRAM accelerators as competing against a *speed tier provisioned from fungible GPU fleets* rather than against a clumsy kernel launcher. That weakens the pure-hardware scarcity narrative for LPU/WSE share if TileRT (and peers) productize, while reinforcing [[Theses/NVDA - Nvidia]]’s software+CUDA moat as the interactivity layer can be leased from the same GPUs hyperscalers already buy.

## Summary
Premium “fast modes” show users will pay for lower latency; labs therefore evaluate purpose-built inference (Cerebras, Groq LPU) against GPU serving. GPUs win high-throughput/medium-interactivity but miss HBM rooflines at batch-1 because kernel launch/teardown and HBM round-trips dominate sub-ms TPOT—even as bandwidth scales 2–3×/gen, memory *latency* does not. TileRT statically compiles the decode graph into one persistent kernel, overlapping compute/memory/comms; on InferenceX GLM-5 FP8, an 8-GPU B200 decode node reached up to ~500 tok/s/user (~3× vs GB300 NVL72 traditional engines at same precision class) and ~340 tok/s/user at 8k/1k vs a prior best ~181 on GB300 FP4+MTP. Prefill stays on vLLM/SGLang via PD-disaggregation; TileRT decode is already in production at Xiaomi (MiMo V2.5 Pro UltraSpeed) and ZAI (GLM 5.1 HighSpeed). Tradeoff: TileRT is currently ~one in-flight request per decode node (private rocket ship), so aggregate tok/s/GPU trails batched conventional points; specialty chips still own absolute SRAM rooflines for some model sizes, but TileRT reframes most buyer need as a speed *tier* on fungible GPUs.

## Evidence
| Metric | Figure | Tag |
|---|---|---|
| B200 aggregate HBM BW (8-GPU) | 64 TB/s | [1×: SemiAnalysis] |
| GLM-5 NVFP4 active traffic / token | ~21 GB | [1×: SemiAnalysis] |
| Theoretical B200 BS1 tok/s/user (no speculation) | ~3,047 | [est.] |
| TileRT FP8 peak tok/s/user (1k/1k) | 494.2 | [1×: InferenceX/SemiAnalysis] |
| Best conventional FP4 tok/s/user (1k/1k) | 256.3 | [1×: InferenceX/SemiAnalysis] |
| TileRT vs best conventional FP8 (1k/1k) | 3.6× | [1×: SemiAnalysis] |
| TileRT 8k/1k tok/s/user | 340 | [1×: SemiAnalysis] |
| Prior best GB300 FP4+MTP 8k/1k | 181.4 | [1×: SemiAnalysis] |
| TileRT vs GB300 conventional (same precision class) | ~3× | [1×: SemiAnalysis] |
| Iso-cost interactivity vs traditional engines | up to 2× | [1×: SemiAnalysis] |
| TileRT decode E2E latency advantage 1k/1k | 4.5× | [1×: SemiAnalysis] |
| TileRT decode tail | 3.01s vs 6.54s (best NVFP4+MTP) / 18.18s (MI355X) | [1×: SemiAnalysis] |
| Production deployers | Xiaomi, ZAI | [1×: SemiAnalysis] |
| Concurrency model | ~1 in-flight req / decode node | [1×: SemiAnalysis] |

## Contradiction Check
Supports [[Theses/NVDA - Nvidia]] CUDA/software-stack conviction: interactivity gains arrive as *compiler/runtime* on Blackwell rather than requiring a forklift to SRAM ASICs. Challenges any thesis that specialty inference chips have a durable monopoly on paid fast tiers—SemiAnalysis explicitly argues those vendors now compete with their own execution model reimplemented on fungible GPUs. Does **not** invalidate Cerebras/Groq for absolute max tok/s or SRAM-favored model shapes; it compresses the *addressable* specialty TAM to workloads that truly need the SRAM roofline.

## Source Excerpts
> "TileRT on B200 is in a class of its own... TileRT reached 340 tokens/s/user on an eight-GPU B200 node... previously 181.4 tokens/s/user on GB300 NVL72"
> "with support only for a batch size of 1 user, TileRT is not just a race car, but it is more like a private rocket ship with room for just one passenger."
