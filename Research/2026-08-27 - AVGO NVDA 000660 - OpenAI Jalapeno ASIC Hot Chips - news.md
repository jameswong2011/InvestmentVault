---
publish: false
date: 2026-08-27
tags: [research, daily-intel-triage, news, AVGO, NVDA, 000660]
sector: Custom Silicon & Networking Semiconductors
ticker: AVGO
source: 'https://www.servethehome.com/openai-jalapeno-asic-at-hot-chips-2026/'
propagated_to: [AVGO, NVDA, 000660]
source_type: news
---

# OpenAI Jalapeno ASIC at Hot Chips 2026: Broadcom-Built 700W Inference Chip; HBM4 216 GiB

## Thesis Delta
Consensus treats OpenAI as an NVIDIA-training customer that *might* one day tape a Broadcom XPU — this ServeTheHome Hot Chips live blog is the first full public architecture: **Jalapeño is a Broadcom-built inference ASIC**, ~nine months RTL-to-tapeout (concept late 2024 → RTL freeze 2025 → tapeout late 2025 → Codex early 2026 → ChatGPT shortly after), **700 W vs GB200 1.2 kW / GB300 1.4 kW**, **13.4 PFLOP/s mxfp4, 216 GiB HBM4 at 15.4 TB/s**, 128-ASIC local domain and **Broadcom Tomahawk6 Clos to 2,048 chips**. Vendor-claimed InferenceX: ~1.5–1.9× tok/s/kW and 1.7–3.6× lower e2e latency vs GB200/GB300 on GPT-OSS 120B, DeepSeek R1, Kimi K2.5 — **but NVIDIA baselines used multi-token prediction while Jalapeño used single-token**, so the Pareto is not an apples-to-apples CUDA-kill. **Supports** [[Theses/AVGO - Broadcom]] six-XPU flywheel (OpenAI is a named customer; this is silicon-in-lab, not a backlog print). **Challenges** a naive reading of [[Theses/NVDA - Nvidia]] CUDA-as-permanent-tok/s-lead (Outstanding Q1) without falsifying the general-purpose / AgentX systems-velocity half — OpenAI still buys NVIDIA for training and this chip is inference-only Gen 1. **Second-order HBM4 content** for [[Theses/000660 - SK Hynix]] (216 GiB/package) with **no supplier named** — HIGH/LOW/CLOSE no-touch.

## Summary
OpenAI disclosed Jalapeño at Hot Chips 2026 on August 26, 2026 (ServeTheHome live blog, reported the same day). Richard Ho, Ravi Narayanaswami and Chris Leary presented Jalapeño as an inference *platform* (chip + host + accelerator rack) co-designed with Broadcom, not a raw accelerator. Design loop used OpenAI's own models plus XLS HDL; PPA vs human baseline includes 56% on a BF16 multiply and 10% smaller matrix-unit area; attention/MoE kernels 1.5–1.8× faster than expert-written, validated on A0 silicon. Metrics are time-to-last-token and tokens/joule on the latency-vs-energy Pareto, not chip TOPS.

InferenceX (power-normalized, July 2026 frontier) is the comparison surface. Jalapeño 700 W vs GB200 1.2 kW vs GB300/MI355X 1.4 kW. OpenAI ran GPT-OSS 120B, DeepSeek R1 670B MXFP4, and 1T Kimi K2.5 — none co-designed for the chip, all brought up between A0 return and the talk. Headline matched-point claims: GPT-OSS 1.9× peak mixed tok/s/kW and 1.7× lower e2e latency vs GB200; R1 1.7× / 3.6× vs GB300; Kimi 1.5× / 3.4× vs GB300. A cleaner cut: single-token Jalapeño vs multi-token GB300 on R1 still leads ~1.5× tok/s/kW and 2.2× lower latency. OpenAI says MTP on Jalapeño would add another 3–5× latency at iso-efficiency; sub-ms token-to-token is claimed at economical throughputs.

Architecture: one balanced chip covering prefill / draft / spec-verify rather than a heterogeneous fleet; KV stays local; unused units gate. Each core slice pairs with an HBM slice; specialized collectives plus a general NoC. Local domain 128 ASICs at 600 GB/s; global 2,048 ASICs at 200 GB/s via half-flattened two-level Clos on **Broadcom Tomahawk6**. Spec sheet: 13.4 PFLOP/s mxfp4, 15.4 TB/s HBM4 across 216 GiB, 700 W, scaling to 27 EFLOP/s and 432 TiB at 2,048 chips. 128-chip raw HBM >1 PB/s implies 1–2k tok/s/user without spec-decode (5–10k with) — real system is well below, so bandwidth is not the only limiter. Gen 1 of a multi-gen roadmap (Gen 2 perf/W, Gen 3 economical low-latency). Credit: Broadcom and Celestica.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Venue | Hot Chips 2026 Day 2; STH live blog | [web: servethehome.com] |
| Builder | Broadcom; rack shout-out Celestica | [web: servethehome.com] |
| Timeline | concept late 2024; RTL freeze 2025; tapeout late 2025; Codex early 2026; ChatGPT shortly after (~9 months RTL→silicon) | [1×: OpenAI via STH] |
| TDP | Jalapeño 700 W vs GB200 1.2 kW vs GB300 / MI355X 1.4 kW | [1×: OpenAI via STH] |
| Compute / HBM | 13.4 PFLOP/s mxfp4; 216 GiB HBM4 @ 15.4 TB/s | [1×: OpenAI via STH] |
| Scale | 128-ASIC local @ 600 GB/s; 2,048-ASIC global @ 200 GB/s | [1×: OpenAI via STH] |
| Switch | Broadcom Tomahawk6 two-level Clos | [web: servethehome.com] |
| GPT-OSS 120B matched | ~1.9× tok/s/kW; ~1.7× lower e2e latency vs GB200 | [1×: OpenAI InferenceX via STH] |
| DeepSeek R1 matched | ~1.7× tok/s/kW; 3.6× lower e2e vs GB300 | [1×: OpenAI InferenceX via STH] |
| R1 STP vs GB300 MTP | ~1.5× tok/s/kW; 2.2× lower e2e | [1×: OpenAI InferenceX via STH] |
| Kimi K2.5 matched | ~1.5× tok/s/kW; 3.4× lower e2e vs GB300 | [1×: OpenAI InferenceX via STH] |
| Qualifier | NVIDIA baselines used MTP; Jalapeño used STP | [web: servethehome.com] |
| PPA vs human | +56% BF16 mul; −10% matrix-unit area | [1×: OpenAI via STH] |
| Kernel | attention/MoE 1.5–1.8× vs expert-written, on-chip | [1×: OpenAI via STH] |
| Roadmap | Gen 1; Gen 2 perf/W; Gen 3 economical serving | [1×: OpenAI via STH] |

## Contradiction Check
**Supports** [[Theses/AVGO - Broadcom]] §Summary / Insight on six XPU customers: OpenAI is no longer a named-backlog abstraction — A0 is in the lab, ChatGPT is claimed on-chip, and Tomahawk6 is the scale-out. Does **not** quantify Jalapeño revenue inside the $73B AI backlog or the >$100B FY27 AI target; no AVGO Conviction Triggers exist. **Challenges** [[Theses/NVDA - Nvidia]] Outstanding Q1 only on the *inference tok/s/kW snapshot* for OpenAI's own models; **does not** falsify CUDA-as-general-purpose (Insight #1) or AgentX systems-velocity (24 Aug SemiAnalysis) because (a) the bench is OpenAI-run InferenceX with an MTP/STP mismatch, (b) the three models were not co-designed for NVIDIA either, (c) training remain NVIDIA, (d) Gen 1 is inference-only. **Second-order** [[Theses/000660 - SK Hynix]]: 216 GiB HBM4/package is a content datapoint; supplier unnamed (TrendForce Samsung-HBM4 chatter is a *different* article, skipped). HIGH/LOW/CLOSE no-touch. Conviction/status untouched.

## Source Excerpts
> "Jalapeño delivers 13.4 PFLOP/s of mxfp4 by mxfp4 matrix compute, 15.4 TB/s of HBM4 bandwidth across 216 GiB, and a 700-watt package, scaling to 27 EFLOP/s and 432 TiB across a 2,048-chip system." [1×: OpenAI via STH]

> "A local Jalapeño domain reaches 128 ASICs … a half-flattened two-level Clos topology built around Broadcom Tomahawk6 switches spans a global domain of 2,048 chips." [web: servethehome.com]
