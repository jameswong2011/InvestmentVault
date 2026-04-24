---
date: 2026-04-24
tags: [research, semiconductors, AMD, NVDA, AI-infrastructure, server-CPU, deep-dive]
sector: GPU & AI Compute Accelerators
ticker: [AMD, NVDA]
source: https://www.viksnewsletter.com/p/the-cpu-bottleneck-in-agentic-ai?r=222kot&utm_campaign=post&utm_medium=web&triedRedirect=true
source_type: deep-dive
propagated_to: [AMD, NVDA]
---

# The CPU Bottleneck in Agentic AI — Server CPU Scoring Framework (Vikram Sekar, Apr 23, 2026 update)

## Thesis Delta

Agentic AI orchestration is shifting CPU:GPU ratios above 1:1 at the rack level, expanding server-CPU TAM and re-pricing the server-CPU competitive surface. On a 9-metric reasoning/action scoring framework, **AMD Venice Dense scores 5 for action workloads** (256 Zen6c cores, 512 SMT threads, 1GB L3, x86 ISA) and **NVIDIA Vera scores 5 for reasoning** (88 custom Olympus ARM cores with SMT, NVLink-C2C 1.8 TB/s coherent to Rubin, 1.5TB LPDDR5). **Intel Diamond Rapids scores 3/3 — mediocre at both ends** after Intel removed SMT (192 cores = 192 threads vs Granite Rapids' 128 cores = 256 threads), structurally regressing its own roadmap. This directly strengthens [[Theses/AMD - Advanced Micro Devices]] Bull Case pillar #3 (EPYC 50%+ share by end-2026) and [[Theses/NVDA - Nvidia]] three-computer architecture (Vera standalone now a merchant CPU, not just a GPU companion).

## Evidence

| CPU | ISA | Cores / Threads | Memory BW | Reasoning Score | Action Score | Strategic Fit |
|---|---|---|---|---|---|---|
| **NVIDIA Vera** | ARM (custom Olympus) | 88 / ~SMT-ish | NVLink-C2C 1.8 TB/s; 1.5TB LPDDR5 @ 1.2 TB/s | **5** | 2 | Reasoning flagship; coherent with Rubin GPU memory |
| **AMD Venice Dense** | x86 (Zen 6c) | 256 / 512 | High IPC; 1GB L3 (8 CCDs × 32c × 4MB) | 3 | **5** | Action flagship; broadest tool-call compatibility |
| **AMD Venice-F** | x86 | — | — | Mid | Mid | Middle ground with AMD GPU attach |
| **AWS Graviton5** | ARM | — | — | Mid | Mid | Middle; Trainium3 head-node role |
| **ARM Phoenix** | ARM | — | PCIe6 XPU attach | Mid | Mid | Middle; hyperscaler flexibility |
| **Intel Diamond Rapids** | x86 | 192 / **192 (SMT removed)** | — | 3 | 3 | Regressed vs Granite Rapids (128c/256t) |

**Workload-latency split** (Georgia Tech/Intel paper, Nov 2025, v2):
- Tool processing on CPU = **50–90% of total agentic workflow latency**
- Pure inference on GPU = 10–50% of latency depending on reasoning vs action weighting

**Agentic CPU demand drivers**:
1. Orchestration per-token monitoring at low tail latency (per-core performance)
2. Parallel sub-agent execution (core count, SMT)
3. Low-latency context/state access (memory bandwidth, cache hierarchy)
4. Tool call throughput (PCIe lanes, ISA compatibility)

**Structural shifts identified**:
- NVIDIA Vera announced as **standalone platform** for agentic processing (CoreWeave deployment). Jensen: "there are going to be many more."
- Intel Q4 2025 earnings: management "caught off guard" on CPU demand inflection.
- ARM SMT gap: standard ARM Neoverse lacks SMT; only Vera's custom Olympus has SMT-ish support — structural x86 advantage in thread density for action workloads.
- NUMA is universal weakness at 192+ cores; every multi-chiplet CPU at scale scores 2–3.
- AMD's x86 license is cross-licensed with Intel under 1980s agreement — disruption to the cross-license is an existential threat to AMD's Venice Dense moat.

## Contradiction Check

**Strengthens [[Theses/AMD - Advanced Micro Devices]] Bull Case #3** ("EPYC passes 50% server CPU share by end 2026"): Venice Dense's 2.7x thread-density advantage over Diamond Rapids (512 vs 192 threads) on a workload that did not exist when Intel scoped Diamond Rapids (pre-2025 agentic inflection) is a direct validation of the Venice 2nm launch thesis. The article's framing — Intel stranded on Granite Rapids until 2028 after cancelling 8-channel Diamond Rapids-SP — directly supports the AMD thesis claim that Intel has no credible counter-punch until Coral Rapids (SMT restored).

**Addresses [[Theses/AMD - Advanced Micro Devices]] Outstanding Question #7** ("Is EPYC share gain durable against Intel 18A Clearwater Forest?"): answer leans positive — Clearwater Forest does not rescue Intel's agentic-AI server positioning if Diamond Rapids already loses the thread-density race. Intel needs an SMT-restored successor (Coral Rapids) before it can compete, pushing recovery to 2027+.

**Strengthens [[Theses/NVDA - Nvidia]] three-computer architecture**: Vera as merchant standalone CPU is an un-modeled TAM expansion for NVDA beyond GPU. The market prices NVDA as a GPU + networking + AI software stack; agentic CPU TAM participation (Vera) is orthogonal revenue currently buried inside Data Center segment reporting. Directly supports the NVDA Bull Case on Physical AI vertical integration — the reasoning-optimized CPU extends CUDA + ecosystem lock-in into the CPU layer itself.

**Quantifies a gap in [[Sectors/GPU & AI Compute Accelerators]]**: no current sector coverage of the server-CPU dimension of agentic AI. The sector frame has been AI accelerator (GPU/ASIC) dominated; this article argues CPUs are a co-equal bottleneck at the rack level. Worth considering whether the sector should expand scope or whether a separate "Server CPUs" sector is warranted given the divergent reasoning vs action optimization paths.

**Caveat on scoring methodology**: author discloses judgment-based adjustments (non-mathematical), used Claude Opus 4.6 Thinking to generate scoring tables, and flagged that "this is the last iteration of the table that will overweight x86 over ARM ISA" — meaning future updates will compress the x86 advantage. Venice Dense's 5/5 action score is partially an x86 weighting artifact that may narrow in 2027+ iterations.

**Partial contradiction to AMD bear case risk #8** ("NVIDIA+MediaTek consumer PC CPU threatens Ryzen"): the article's focus on server CPUs does not address the PC gaming CPU entry risk. Different market, different optimization. Leaves AMD client segment bear case unchanged.

## Source Excerpts

> "tool processing on CPUs accounts for anywhere between 50-90% of total latency in agentic workloads."

> "Vera scores 5 for reasoning and 2 for action. Venice Dense scores 3 for reasoning and 5 for action. The gap between them on each other's turf is large — confirming that CPU designs are diverging along this spectrum."

> "Intel Diamond Rapids' removal of SMT (192 cores = 192 threads) makes it worse than the older Intel Granite Rapids (128 cores = 256 threads) on thread density. AMD Venice Dense's SMT doubles its effective thread count to 512, creating a 2.7x advantage over Diamond Rapids."

> "The cancellation of 8-channel Diamond Rapids-SP leaves Intel's mainstream market stranded on Granite Rapids until at least 2028. As a result, they have neither a clear reasoning-oriented CPU, nor an action-oriented one. Intel may have a path back via Coral Rapids with SMT restored."

> "AMD's x86 license only exists because of an agreement dating back to the 1980s when IBM required a second source for PC processors... Anything that disrupts this licensing agreement will be a big threat to AMD's CPU dominance."

## Related

- [[Theses/AMD - Advanced Micro Devices]] — directly strengthens EPYC Bull Case pillar #3 and Outstanding Question #7 (Intel counter-punch timing)
- [[Theses/NVDA - Nvidia]] — Vera standalone platform validates three-computer architecture CPU extension
- [[Sectors/GPU & AI Compute Accelerators]] — agentic CPU bottleneck extends sector scope beyond accelerators
- [[Sectors/Custom Silicon & Networking Semiconductors]] — tangential (AWS Graviton5, Google x86+TPU, ARM Phoenix PCIe6 XPU)
- [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]] — complementary context on Jensen's "many more" Vera deployments framing
- [[Macro/AI Bubble Risk and Semiconductor Valuations]] — CPU demand inflection validates continued AI capex cycle (expanding silicon TAM vs concentration in GPU alone)
