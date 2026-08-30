---
publish: false
date: 2026-08-28
tags: [research, daily-intel-triage, news, AVGO, NVDA]
sector: Custom Silicon & ASICs
ticker: AVGO
source: 'https://openai.com/index/jalapeno-first-results/'
propagated_to: [AVGO, NVDA]
source_type: news
---

# OpenAI Jalapeño First InferenceX Results: 1.5–1.9× Work/W vs Blackwell

## Thesis Delta
Consensus after Hot Chips had architecture slides but no public InferenceX numbers — OpenAI’s **25 Aug primary** is the first quantitative print: Jalapeño (Broadcom-built, 700 W package / ≤550 W measured) delivered **1.5–1.9× peak mixed TPS/kW** and **1.7–3.6× lower E2E latency** vs selected GB200/GB300 systems on GPT-OSS 120B, DeepSeek R1, and Kimi K2.5 (8K/1K STP). Consensus either prices “CUDA moat forever” or “ASIC kills GPU in 2026” — this source prices **multi-sourcing at GW scale**: YE26 initial deploy, Gen 2 deep, while OpenAI **keeps buying NVIDIA for training and inference**. **Supports** [[Theses/AVGO - Broadcom]] openai-xpu / custom platform. **Inference-economics warning** for [[Theses/NVDA - Nvidia]] without proving near-term unit collapse. Distinct from 2026-08-27 STH Hot Chips ingest. No trigger fire.

## Summary
OpenAI measured Jalapeño on SemiAnalysis InferenceX across three public models, normalizing by published package TDP. GPT-OSS vs GB200: ~1.9× TPS/kW, ~1.7× lower E2E; DeepSeek vs GB300: ~1.7× / ~3.6×; Kimi vs GB300: ~1.5× / ~3.4×. Iso-interactivity “throughput at previous-best TBT” prints (53.7× / 104.3× / 56.1×) are operating-point comparisons, not 100× hardware multiples. Architecture co-designs chip/memory/network/software around prefill vs decode and local KV cache. AI-assisted design: ~9 months design→tapeout; three unplanned open-weight models ported in ~2 months; selected attention/MoE blocks 1.5–1.8× faster than prior human kernels. Path: deploy inside OpenAI by YE26; continue NVIDIA purchases; separate 10 GW arrangements with both Broadcom and NVIDIA. Caveats: not AgentX/long multi-turn; not Rubin like-for-like; not fleet TCO.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Date | 25 Aug 2026 | [web: openai.com] |
| Peak work/W | 1.5–1.9× vs GB200/GB300 pairs | [1×: OpenAI] |
| E2E latency | 1.7–3.6× lower | [1×: OpenAI] |
| Interactive | 2.1–4.1× higher performance | [1×: OpenAI] |
| Package TDP | Jalapeño 700 W (≤550 W measured); GB200 1,200 W; GB300 1,400 W | [1×: OpenAI] |
| GPT-OSS TPS/kW | 85,448 vs 44,960 | [1×: OpenAI] |
| DeepSeek TPS/kW | 19,641 vs 11,781 | [1×: OpenAI] |
| Kimi TPS/kW | 18,195 vs 11,862 | [1×: OpenAI] |
| Design cycle | ~9 months to tapeout | [1×: OpenAI] |
| Deploy | YE26 initial; Gen 2 in development | [1×: OpenAI] |
| Partner | Broadcom silicon; Celestica board/rack | [web: openai.com / prior] |

## Contradiction Check
**Supports** [[Theses/AVGO - Broadcom]] custom-ASIC platform narrative and 10 GW Broadcom accelerator pact framing. **Challenges** any [[Theses/NVDA - Nvidia]] assumption that OpenAI inference watts are captive to merchant GPUs through 2027 — but OpenAI explicitly continues NVIDIA buys; fair compare is Rubin/HBM4, not only Blackwell. Does not fire HIGH/LOW/CLOSE. Conviction/status unchanged.

## Source Excerpts
> "Across all three, Jalapeño delivered 1.5 to 1.9 times more AI work per watt at peak throughput and 1.7 to 3.6 times lower end-to-end latency than the comparison systems." [web: openai.com]

> "We will continue to widely deploy accelerators from NVIDIA and other partners for both training and inference workloads." [web: openai.com]
