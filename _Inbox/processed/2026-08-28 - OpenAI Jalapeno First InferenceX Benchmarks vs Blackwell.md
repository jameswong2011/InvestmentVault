---
date: 2026-08-28
tags: [daily-intel-triage, news, AVGO, NVDA]
source: 'https://openai.com/index/jalapeno-first-results/'
source_type: news
holdings: [AVGO, NVDA]
score: 9
---

# OpenAI Jalapeño First InferenceX Results vs NVIDIA Blackwell

**Source:** https://openai.com/index/jalapeno-first-results/
**Date:** 2026-08-25 · **Brief score:** 9 · **Tags:** daily-intel-triage

## Why it matters (portfolio)
First quantitative InferenceX print for Broadcom-built Jalapeño — transmission to **AVGO** (custom XPU platform) and **NVDA** (inference economics / negotiating leverage, not near-term GPU collapse). Distinct from prior Hot Chips architecture clip already ingested.

## Article body

Jalapeño’s first results show industry-leading speed and efficiency in AI inference (OpenAI, Aug 25, 2026).

OpenAI tested Jalapeño on SemiAnalysis InferenceX across GPT-OSS 120B, DeepSeek R1 670B MXFP4, and Kimi K2.5 1T MXFP4 (nominal 8K input / 1K output, single-token prediction). Across all three, Jalapeño delivered 1.5–1.9× more AI work per watt at peak throughput and 1.7–3.6× lower end-to-end latency vs selected GB200/GB300 systems. For highly interactive workloads, 2.1–4.1× higher performance. Package TDP normalization: Jalapeño 700 W (measured sustained ≤550 W), GB200 1,200 W, GB300 1,400 W.

Model pairs (OpenAI-reported):
- GPT-OSS 120B vs GB200: 85,448 vs 44,960 mixed TPS/kW (~1.9×); E2E 1.03 vs 1.80 s (~1.7×); min TBT ~2.7×; throughput at prior TBT ~53.7×
- DeepSeek R1 vs GB300: 19,641 vs 11,781 mixed TPS/kW (~1.7×); E2E 1.65 vs 5.99 s (~3.6×); min TBT ~4.1×; iso-TBT throughput ~104.3×
- Kimi K2.5 vs GB300: 18,195 vs 11,862 mixed TPS/kW (~1.5×); E2E 1.56 vs 5.31 s (~3.4×); min TBT ~3.8×; iso-TBT ~56.1×

Architecture: inference-first co-design of chip/memory/network/software/rack around prefill vs decode bottlenecks and local KV-cache placement. Broadcom silicon implementation; Celestica board/rack. AI-assisted design: ~9 months initial design to tapeout; Codex+GPT-Astra ported three unplanned open-weight models to high performance in ~2 months; selected GPT-OSS attention/MoE blocks 1.5–1.8× faster than prior human kernels (block-level, not full-model).

Deployment: initial deploy inside OpenAI fleet by end-2026; Gen 2 deep in development; Gen 3 taking shape. OpenAI will continue deploying NVIDIA (and other) accelerators for training and inference. Separate forward-looking 10 GW arrangements with both Broadcom custom accelerators and NVIDIA systems.

Caveats in-source: production qualification and software maturation ongoing; figures are package-TDP-normalized InferenceX STP 8K/1K — not fleet TCO, AgentX multi-turn, or Rubin-like-for-like.

