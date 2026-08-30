---
publish: false
title: "OpenAI Jalapeno Custom AI ASIC at Hot Chips 2026"
url: "https://www.servethehome.com/openai-jalapeno-asic-at-hot-chips-2026/"
source: ServeTheHome
date: "2026-08-27"
why_selected: "Holdings AVGO/NVDA/000660: OpenAI publicly details Broadcom-built Jalapeño inference ASIC — 9 months RTL-to-silicon, 700W vs GB300 1400W, HBM4 216 GiB / 15.4 TB/s, Tomahawk6 Clos to 2048 chips."
tags:
  - daily-intel-triage
  - AVGO
  - NVDA
  - 000660
---

# OpenAI Jalapeno Custom AI ASIC at Hot Chips 2026

Source: [ServeTheHome](https://www.servethehome.com/openai-jalapeno-asic-at-hot-chips-2026/) — live from Hot Chips 2026 Day 2

OpenAI took the Hot Chips 2026 stage on Day 2 to detail Jalapeño, an in-house inference ASIC and system built with Broadcom and designed to be the best compute platform for OpenAI's own inference workloads. Richard Ho, Ravi Narayanaswami, and Chris Leary walked through the chip's roughly nine-month path from initial RTL to tapeout, its performance positioning against NVIDIA GB200 and GB300, and an architecture built around HBM4 and a spatial programming model.

OpenAI Jalapeño is framed as an inference platform rather than a raw accelerator. OpenAI is talking about this in terms of the silicon, together with its host and accelerator rack pair, targeting state-of-the-art performance per watt at low latency for multi-chip workloads, aided by AI-accelerated hardware and software co-design.

This project moved quickly once OpenAI concluded that inference and agentic workloads needed a purpose-built design. Timeline: architecture concept late 2024, RTL freeze 2025, late 2025 tapeout, Codex running in early 2026, with ChatGPT on the chip not long after.

OpenAI frames the design around two metrics, time to last token for user experience and tokens per joule for inference efficiency. Across those, it compares systems along the full Pareto frontier of request latency versus energy per token rather than chasing raw chip counts, throughput per chip, or time to first token.

For comparisons, OpenAI uses InferenceX, a public, power-normalized benchmark across a basket of open-source models that spans the full prefill-to-decode spectrum. Runs normalize to the package TDP, with Jalapeño at 700 watts against the GB200 at 1.2 kilowatts, and the GB300 and MI355X at 1.4 kilowatts, and OpenAI measured against the July 2026 Pareto frontier across other accelerators.

Jalapeño uses single-token prediction, whereas the NVIDIA baselines it is compared against use multi-token prediction. MTP uses seven tiny draft-model turns plus one batched large-trunk pass to produce up to eight output tokens, reducing the number of expensive large-model passes by up to 8x.

OpenAI ran GPT-OSS to stress latency limits, DeepSeek R1 is a good draft-model case, and the 1-trillion-parameter Kimi K2.5 shows scaling across many devices. OpenAI notes none of the three were co-designed for Jalapeño and that it got all of them running between when A0 silicon returned to the lab and now.

Throughput-per-kilowatt frontier for GPT-OSS 120B: Jalapeño sits on the Pareto frontier at 700 watts, compared to the GB200 at 1,200 watts. At matched operating points on GPT-OSS 120B, Jalapeño shows about 1.9x higher peak mixed tokens per second per kilowatt and roughly 1.7x lower end-to-end latency. At the previous best time between tokens, it delivers around 53.7x more throughput.

DeepSeek R1 670B MXFP4: Jalapeño holds the frontier at 700 watts against the GB300 at 1,400 watts. Matched-operating-point gains: about 1.7x higher peak mixed tokens per kilowatt per second and 3.6x lower end-to-end latency; at previous best TBT, roughly 104.3x more throughput.

OpenAI also runs Jalapeño in single-token mode directly against the GB300 in multi-token mode on DeepSeek R1. Even without the speculative-decode advantage, Jalapeño pushes the throughput-per-kilowatt frontier forward. At matched operating points, single-token Jalapeño still leads multi-token GB300, with about 1.5x higher peak mixed-token rate per kilowatt and 2.2x lower end-to-end latency.

Kimi K2.5 1T MXFP4: Jalapeño lands at about 1.5x higher peak mixed tokens per second per kilowatt and 3.4x lower end-to-end latency, with roughly 56.1x higher throughput than the previous best TBT.

OpenAI also claims sub-millisecond token-to-token latency on frontier models at economical throughputs and notes that multi-token prediction would add another 3x to 5x latency improvement at iso-efficiency.

A request spans three hardware stages: compute-bound prefill, a small draft model at ultra-low batch for latency-sensitive speculation, and a memory-bandwidth-bound spec-verify decode with bursty MoE communication. Jalapeño answers with a single balanced chip, where idle blocks are gated, rather than paying for a separate accelerator's baseline package, HBM, I/O, and network power. OpenAI keeps KV local on Jalapeño and varies the active ratio of compute, memory, and network per phase.

Raw HBM4 bandwidth: at a 128-chip aggregate of more than one petabyte per second, a bandwidth-only ceiling implies 1,000 to 2,000 tokens per second per user without speculative decoding and 5,000 to 10,000 with it, yet the real system lands well below either rate.

Architecture pairs each core slice with an HBM slice. A local Jalapeño domain reaches 128 ASICs with low core-to-core latency, and a half-flattened two-level Clos topology built around Broadcom Tomahawk6 switches spans a global domain of 2,048 chips, with higher bandwidth for tensor parallel and lower bandwidth for expert parallel.

OpenAI used its own internal AI model and the XLS hardware description language. Major changes landed up to the day of the RTL freeze, plus measured PPA wins over a human baseline, such as 56 percent on a BF16 multiply, back-to-back with a 10 percent smaller matrix unit area. Optimized attention and MoE kernels run 1.5x to 1.8x faster than existing expert-written implementations.

Jalapeño delivers 13.4 PFLOP/s of mxfp4 by mxfp4 matrix compute, 15.4 TB/s of HBM4 bandwidth across 216 GiB, and a 700-watt package, scaling to 27 EFLOP/s and 432 TiB across a 2,048-chip system, with the network split at 600 GB/s for the local 128-ASIC domain and 200 GB/s for the global 2,048-ASIC domain.

OpenAI frames Jalapeño as Gen 1 of a multi-generation roadmap. Gen 2 targets better performance per watt, and Gen 3 aims for economical, low-latency serving. Shout-out to Broadcom and Celestica.
