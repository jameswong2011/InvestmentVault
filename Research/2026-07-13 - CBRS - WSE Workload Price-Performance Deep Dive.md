---
date: 2026-07-13
tags: [research, deep-dive, CBRS, semiconductors, ai-inference, wafer-scale]
sector: Compute & AI Compute Accelerators
ticker: CBRS
source: vault synthesis + current web research (Cerebras public API/IR, Artificial Analysis, OpenAI, AWS/Cerebras, Golden et al. ISPASS 2026)
source_type: deep-dive
propagated_to: [CBRS]
---

# CBRS WSE Workload Price-Performance Deep Dive

> Supporting research for the 2026-07-13 /deepen of [[Theses/CBRS - Cerebras Systems]] §Business Model & Product Description. “WFE” in the research request is treated as Cerebras’ WSE-3 wafer-scale configuration. Reading protocol per [[Generalist - Overview]]: architecture fit is a hypothesis tested against same-model benchmarks, utilization and the semiconductor-challenger base rate—not a moat verdict.

## Thesis Delta

1. **WSE-3 is best framed as a low-batch decode appliance, not an all-purpose AI accelerator.** Its 44GB of 21 PB/s SRAM and wafer mesh attack sequential autoregressive decode; AWS’s decision to put Trainium3 on prefill and CS-3 on decode is the clearest commercial confirmation of the boundary.
2. **Cerebras wins cost per latency-sensitive result while losing cost per token.** On gpt-oss-120b (high), Cerebras is 7.8× CoreWeave’s blended price but 27.8× faster in output and 20.0× faster for a 10k-input/500-output response. The ~$0.003405 incremental request cost buys 36.95 seconds—only ~$0.33 per hour of user waiting time saved.
3. **Interactive coding is the strongest proven use case; model-bound research/agents, multimodal computer use and the LLM stage of voice are the next tier.** Bulk generation, embeddings, classification, long-input/short-output RAG and tool-latency-heavy autonomous agents are poor fits.
4. **Utilization, model availability and workflow Amdahl effects—not peak tokens/second—set the economic ceiling.** CS-3 idles at ~80% of TDP and reaches energy/token parity with 32 H100s only at ~34% duty cycle; Cerebras’ public API exposed three 131k-context models on 2026-07-13.
5. **Conviction remains low.** The evidence strengthens a real product-market fit for premium decode but narrows it to a specialized layer controlled upstream by model labs/cloud orchestrators and downstream by the customer workflow.

## Summary

Cerebras’ wafer-scale configuration maximizes price-performance when five conditions coincide: low per-request batch, long sequential output, model decode represents most of end-to-end latency, the customer can monetize seconds saved, and demand keeps the configured wafer above its utilization floor. Interactive coding satisfies all five. Serial reasoning and research agents qualify when model calls—not tools or data retrieval—are the bottleneck. Real-time multimodal and voice experiences qualify at the LLM stage. A premium latency tier for 100B–1T-parameter models also fits because scale-out communication and HBM bandwidth otherwise inflate per-user delay.

The opposing workload is high-batch, unattended or prefill-heavy. GPUs, TPUs and throughput accelerators can batch weight reads across users, expose broader software/model ecosystems and idle cheaply. The independent xPU-athalon study finds Cerebras on the energy-latency Pareto frontier at low batch but displaced by H100, MI300, TPU and SambaNova as batch grows. The best system-level design is therefore heterogeneous: cheap parallel compute for prompt prefill and bulk work; WSE for the serial decode stage. This supports Cerebras’ product-market fit but leaves the interface and routing layer with AWS, OpenAI or the application owner—consistent with the existing weak [[Lens - Value Layer Monopoly]] read.

## Framework / Mental Model

### Ideal workload fingerprint

| Test | WSE-positive condition | Economic reason | Disqualifier |
|---|---|---|---|
| Batch | 1–low batch per latency SLO | Preserves SRAM latency advantage | Requests can be pooled/batched without user penalty |
| Output shape | Long autoregressive generation | Decode is serial and memory-bandwidth-bound | Short labels, embeddings or classification |
| Latency mix | Decode ≥50% of end-to-end | WSE acceleration survives workflow Amdahl effects | Tools/network/CPU/retrieval dominate |
| Value of time | Human or high-value system waits | Milliseconds/seconds have monetizable value | Offline completion time has no value |
| Utilization | Sustained >~34% duty cycle | Amortizes ~80%-of-TDP idle draw | Sporadic on-prem demand |
| Model portfolio | Stable, repeated models | Compilation/configuration amortizes | Rapid model churn/custom CUDA kernels |
| Architecture | Prefill/batch offloaded; WSE handles decode | Each processor handles its native bottleneck | Full-stack WSE pays for speed where it is not needed |

This is [[Industry - Semiconductors]] #8 (architecture transitions remap the bottleneck) without proving #6/#7 lock-in. It also activates [[Generalist - Overview]] [G-14] Jevons only conditionally: cheaper *latency* can unlock more iterative reasoning, but the 7.8× token premium means demand must be latency-elastic rather than merely token-elastic. The adversarial [[Generalist - Overview]] [G-10] base rate remains: merchant accelerators lose if they do not own the software/routing interface.

### Same-model customer economics

Artificial Analysis reports P50 measurements over the prior 72 hours using a 10,000-token prompt and standardized 500-token response. Blended price uses a 7:2:1 cache-hit/input/output mix.

| gpt-oss-120b (high) provider | Blended $/1M | Output tok/s | First chunk | Total response |
|---|---:|---:|---:|---:|
| **Cerebras** | **$0.39** | **1,861** | **0.60s** | **1.94s** |
| CoreWeave | $0.05 | 67 | 1.48s | 38.89s |
| Google Vertex | $0.12 | 422 | 0.40s | 6.32s |
| Groq | $0.14 | 479 | 0.70s | 5.92s |
| SambaNova | $0.26 | 692 | 1.02s | 4.64s |

Current posted per-token prices:
- Cerebras gpt-oss-120b: $0.35/M input, $0.75/M output.
- CoreWeave: $0.04/M input, $0.14/M output.

For 10,000 input + 500 output:
- Cerebras = \(0.01×$0.35 + 0.0005×$0.75 = $0.003875\).
- CoreWeave = \(0.01×$0.04 + 0.0005×$0.14 = $0.000470\).
- Premium = **$0.003405**; measured time saved = **36.95 seconds**; premium per waiting-hour saved = **~$0.33**.

The inference is narrow: any human wage clears the direct API premium. It does not show WSE has lower hardware TCO, because Cerebras has not published a standardized on-prem system price/fully loaded utilization comparison.

### Workflow Amdahl test

Let \(s\) be the share of workflow latency spent in model decode and \(k\) the WSE decode-speed ratio. Total speedup is:

\[
\text{Workflow speedup} = \frac{1}{(1-s)+s/k}
\]

Using \(k=27.8×\), the current Cerebras/CoreWeave output-speed ratio:

| Decode share of end-to-end latency | Workflow speedup |
|---:|---:|
| 90% | **7.6×** |
| 50% | **1.9×** |
| 10% | **1.1×** |

A model-bound IDE completion maps to the first row; an agent waiting on browsers, databases and external tools can map to the last. This explains why “agentic” is not automatically a WSE use case.

### Use-case ranking

| Tier | Use case | Evidence level | Price-performance read |
|---|---|---|---|
| 1 | Interactive coding/edit/debug/search | High | Best proven fit: long decode, human waits, serial revisions. OpenAI Codex-Spark >1,000 tok/s; Cognition SWE-1.6 up to ~950 tok/s/~5× GPU. |
| 1 | Model-bound serial reasoning/research agents | Medium-high | Strong when model calls dominate; AlphaSense uses speed to run more searches/documents/tool work per analyst session. |
| 1 | Interactive multimodal document/GUI/computer-use | Medium-high | Gemma 4 31B: Cerebras 1,974 tok/s/1.73s vs CoreWeave 39 tok/s/57.78s; useful for observe→reason→act. Price is $1.04/M vs $0.12/M and context 131k vs 262k. |
| 1 | Real-time voice/dialogue—LLM stage | Medium | Dead-air avoidance monetizes low latency. Public endpoint is text/vision, so ASR/TTS/network remain outside WSE. |
| 2 | Premium latency tier for 100B–1T reasoning | Medium-high | Kimi K2.6 approached 1,000 tok/s at 1T parameters; on-wafer communication helps. Independent study still puts CS-3/H100/MI300 on the 405B batch-1 Pareto frontier depending configuration. |
| 2 | Best-of-N/test-time compute under deadline | Medium | More reasoning/samples per second can raise quality; high token price requires expensive errors or high result value. |
| 2 | Sparse foundation training/fine-tuning | Low-medium | Native unstructured sparsity and Weight Streaming fit; vendor reports up to 8× sparse-training acceleration. No current independent $/trained-quality benchmark. |
| 2 | Scientific AI with stencil/graph/sparse communication | Low-medium | WSE mesh/SRAM can remove memory movement; a 2026 stencil study reports up to 342× A100 on a tailored kernel. Porting/compiler burden makes this specialist, not general. |
| 3 | High-batch offline generation, embeddings, ranking, classification, ETL | High | Poor fit: throughput/$ and batching dominate; xPU-athalon moves GPU/TPU/SambaNova onto Pareto frontier as batch rises. |
| 3 | Long-input/short-output RAG or summarization | High | Poor/mixed: prefill is parallel and compute-bound; AWS assigns it to Trainium3. WSE earns its premium only if generated reasoning is long. |
| 3 | Sporadic on-prem, edge and broad changing model fleets | High | Poor: 15U/~23kW, ~80% TDP idle, compiler/model-catalog friction and only three public models. |

## Evidence

### Independent hardware evidence

Golden et al., *The xPU-athalon* (accepted ISPASS 2026), compares CS-3, SambaNova, Groq, Gaudi, TPUv5e, A/H100 and MI300 across latency, energy, power and programmability.

- Cerebras is energy-latency Pareto-optimal at low batch for both prefill and decode, remains competitive to higher batch in decode, then falls off as batch rises; H100, MI300, TPU and SambaNova enter the throughput-oriented frontier.
- Low-batch Llama-3.1-8B latency/token is **22.89% of H100** (~4.37× faster).
- CS-3, H100 and MI300 can all sit on the batch-1 Pareto frontier for Llama-3.1-405B; model size and sequence length alter the answer.
- CS-3 uses **100% of TDP during both prefill and decode**, idles at **~80% of TDP**, and reaches energy/token parity with a 32-H100 cluster at **~34% duty cycle**.
- Novel accelerator compilation can be **up to 5,000× GPU compilation time** across tested stacks. Cerebras’ programmability is stronger than Groq’s but trails mature GPU/TPU/Gaudi workflows.
- On-wafer communication materially reduces energy, but the benefit depends on keeping the working set local; large-model scale-out still needs realistic communication accounting.

Paper: [Golden et al., The xPU-athalon](https://arxiv.org/abs/2604.10852).

### Current delivered inference economics

- gpt-oss-120b same-model results above come from [Artificial Analysis provider benchmarking](https://artificialanalysis.ai/models/gpt-oss-120b/providers), measured over the prior 72 hours.
- Gemma 4 31B provider results come from [Artificial Analysis](https://artificialanalysis.ai/models/gemma-4-31b/providers): Cerebras 1,974 tok/s, 1.73s standardized response, $1.04/M blended; CoreWeave 39 tok/s, 57.78s, $0.12/M.
- The [Cerebras public models endpoint](https://api.cerebras.ai/public/v1/models) returned three models on 2026-07-13: production gpt-oss-120b and Gemma 4 31B; preview GLM-4.7. Each exposes 131,072 context and 40,960 maximum completion tokens. Posted model pricing supports the task-cost calculation.
- Public catalog breadth is not dedicated-endpoint breadth; enterprises can bring custom weights. It still measures developer-accessible ecosystem breadth and model churn risk.

### Commercial workload validation

- [OpenAI Codex-Spark](https://openai.com/index/introducing-gpt-5-3-codex-spark/) is a smaller GPT-5.3-Codex variant designed for real-time coding at >1,000 tok/s on Cerebras. OpenAI contrasts it with frontier models built for autonomous tasks lasting hours/days, drawing the same interactive-vs-batch boundary as the hardware analysis.
- [Cognition SWE-1.6](https://www.cerebras.ai/blog/case-study-cognition-x-cerebras) runs up to ~950 tok/s and ~5× GPU speed in interactive coding; the product team treats speed as a design input for context retrieval, UI and model behavior.
- [AlphaSense Generative Search](https://www.cerebras.ai/customer-spotlights/alphasense) uses a multi-agent/multi-LLM orchestrator; Cerebras shortens the model loop so it can search more documents and run more tool work while the analyst waits. No independent cost/quality uplift is disclosed.
- [Gemma 4 31B](https://www.cerebras.ai/blog/gemma-4-on-cerebras-the-fastest-inference-is-now-multimodal) is Cerebras’ first public vision model, aimed at screenshots, documents, charts and computer-use loops.
- Cerebras’ [Q1 2026 release](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-announces-strong-first-quarter-2026-results) reports Kimi K2.6 near 1,000 tok/s at 1T parameters and explicitly labels Codex-Spark “interactive work where latency matters.”

### Heterogeneous system design

The [AWS/Cerebras disaggregated inference design](https://www.cerebras.ai/press-release/awscollaboration) sends parallel, compute-bound prompt prefill to Trainium3 and serial, bandwidth-bound decode to CS-3. This is the strongest real-world configuration evidence because a cloud operator chose not to pay the WSE premium for both phases.

The positive read: Cerebras owns a technically scarce decode engine. The adverse [[Lens - Value Layer Monopoly]] read: AWS owns Bedrock, routing, networking, customer access and the heterogeneous system interface, so it can substitute whichever decode accelerator clears the latency/cost SLO.

### Training and scientific AI

- WSE’s Weight Streaming separates model storage from compute and its cores can skip unstructured zeros. Cerebras reports [up to 8× sparse Llama training acceleration](https://www.cerebras.ai/blog/introducing-sparse-llama-70-smaller-3x-faster-full-accuracy) and 60% fewer FLOPs at 75% sparsity in earlier GPT work. These are vendor-led results, not current fleet-TCO comparisons.
- A 2026 [WSE-3 stencil study](https://arxiv.org/abs/2605.07954) reports up to 342× over an adapted A100 solver by keeping memory-bound local-neighbour computation in distributed SRAM. It supports a niche scientific-AI fit for PDE, fluid, climate and physics kernels; it does not establish general model-training economics.
- The compiler and kernel burden identified by xPU-athalon is the economic counterweight. A high raw speedup can still lose after migration, model-port and low-utilization costs.

## Contradiction Check

- **Fastest is not cheapest.** Cerebras leads output speed and end-to-end response time on the measured models but charges 7.8× CoreWeave’s blended gpt-oss price and 8.7× on Gemma 4. “20× faster” cannot be used as a blanket cost claim.
- **API price is not hardware TCO.** Provider margin, power contracts, utilization, networking and capital life are embedded but undisclosed. The hosted inference ranking is high confidence; on-prem purchase economics and training $/quality are low confidence.
- **Agentic does not mean model-bound.** The Amdahl test caps benefit at 1.1× when decode is only 10% of workflow latency. Tool-heavy autonomous agents can prefer cheap GPU tokens despite many model calls.
- **Large model does not guarantee WSE dominance.** The independent 405B result leaves CS-3, H100 and MI300 on the Pareto frontier. Batch, sequence length and model topology decide.
- **Context and model breadth can outweigh speed.** Current public models cap context at 131k, while several Gemma GPU endpoints expose 262k; only three public model IDs were live. Dedicated endpoints mitigate breadth but add commitment.
- **Utilization reverses energy economics.** CS-3’s 80%-of-TDP idle state makes aggregated hosted demand or one saturated model superior to sporadic enterprise ownership.
- **Training/scientific claims have weaker evidence.** Sparse-training figures are vendor results and the stencil benchmark is a tailored kernel, so neither supports a broad “WSE beats GPUs” conclusion.
- **Model optimization can shrink the addressable bottleneck.** KV-cache compression, speculative decoding, disaggregated memory and better GPU batching can reduce the value of extreme SRAM bandwidth; track alongside [[Theses/MRVL - Marvell Technology]] and [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]].

## Source Excerpts

- Cerebras public model catalog/pricing: https://api.cerebras.ai/public/v1/models
- Artificial Analysis gpt-oss-120b providers: https://artificialanalysis.ai/models/gpt-oss-120b/providers
- Artificial Analysis Gemma 4 31B providers: https://artificialanalysis.ai/models/gemma-4-31b/providers
- xPU-athalon: https://arxiv.org/abs/2604.10852
- OpenAI Codex-Spark: https://openai.com/index/introducing-gpt-5-3-codex-spark/
- AWS/Cerebras disaggregated inference: https://www.cerebras.ai/press-release/awscollaboration
- Cerebras Q1 2026 results: https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-announces-strong-first-quarter-2026-results
- Cognition case study: https://www.cerebras.ai/blog/case-study-cognition-x-cerebras
- AlphaSense case study: https://www.cerebras.ai/customer-spotlights/alphasense
- Gemma 4 multimodal: https://www.cerebras.ai/blog/gemma-4-on-cerebras-the-fastest-inference-is-now-multimodal
- Sparse Llama: https://www.cerebras.ai/blog/introducing-sparse-llama-70-smaller-3x-faster-full-accuracy
- WSE-3 stencil study: https://arxiv.org/abs/2605.07954

## Related

- [[Theses/CBRS - Cerebras Systems]] · [[Sectors/Compute & AI Compute Accelerators]] · [[Theses/NVDA - Nvidia]] · [[Theses/CRWV - CoreWeave]] · [[Theses/MRVL - Marvell Technology]] · [[Theses/AVGO - Broadcom]]
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] · [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]] · [[Research/2026-01-15 - AI Compute and Memory Demands - HBM Shortage]] · [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]]
