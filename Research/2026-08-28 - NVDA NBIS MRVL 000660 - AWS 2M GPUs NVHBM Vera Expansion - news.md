---
publish: false
date: 2026-08-28
tags: [research, daily-intel-triage, news, NVDA, NBIS, MRVL, 000660, AVGO]
sector: AI Accelerators & GPUs
ticker: NVDA
source: 'https://convergedigest.com/aws-nvidia-2-million-gpus-ai-infrastructure'
propagated_to: [NVDA, NBIS, MRVL, 000660]
source_type: news
---

# AWS Plans 2 Million Additional NVIDIA GPUs (2027–28) Plus NVHBM / Vera / Spectrum Stack

## Thesis Delta
Consensus after the NVDA Q2 print still debated whether hyperscaler GPU offtake was peaking into custom XPUs — this Converge Digest recap of the AWS–NVIDIA expansion is the **named 2027–28 volume lock**: **2 million additional Blackwell Ultra / Rubin / Rubin Ultra GPUs** on top of the prior >1M from 2026, plus Vera CPUs, Spectrum clustering, **NVHBM on Trainium4 via Annapurna**, and a **100k-GPU IL6+ U.S. government AI-factory** tranche. Consensus assumed substitution; this source implies **both stacks expand**. **Supports** [[Theses/NVDA - Nvidia]] Rubin-ramp / hyperscaler-demand. Second-order [[Theses/NBIS - Nebius Group]] (Rubin rack comps / GW demand). **Supports** [[Theses/MRVL - Marvell Technology]] Fusion/Spectrum adjacency and [[Theses/000660 - SK Hynix]] custom-HBM attach. No HIGH/LOW/CLOSE fire; conviction untouched.

## Summary
AWS and NVIDIA plan to deploy 2 million additional NVIDIA GPUs across AWS global infrastructure in 2027–2028 (Blackwell Ultra, Rubin, Rubin Ultra), after demand exceeded the GTC 2026 plan for >1 million GPUs starting 2026. The deal extends beyond GPUs: Vera CPU infrastructure for agentic AI; Annapurna Labs extending NVLink Fusion onto NVIDIA’s custom NVHBM so Trainium can tap NVIDIA memory and scale-up fabric while Nitro/EFA remain the scale-out/security stack; Spectrum networking for large clusters; 100,000 GPUs on secure AWS infrastructure for federal/national-security workloads at IL6+; Nemotron on Bedrock/SageMaker; cuDF/cuVS acceleration on EMR/OpenSearch; Amazon Robotics adopting Jetson/Omniverse/Isaac. Garman and Huang quotes frame demand “running ahead of every forecast.” Analysis note: AWS is simultaneously committing to merchant NVIDIA silicon and accelerating Trainium — heterogeneous, not substitution.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Date | Announced ~26 Aug 2026 | [web: convergedigest.com] |
| Incremental GPUs | 2M additional in 2027–28 | [1×: AWS/NVIDIA via Converge Digest] |
| Prior plan | >1M NVIDIA GPUs from 2026 | [1×: Converge Digest] |
| SKUs | Blackwell Ultra, Rubin, Rubin Ultra | [1×: Converge Digest] |
| CPU | Vera CPU instances on AWS | [1×: Converge Digest] |
| Memory | NVHBM + NVLink Fusion on Trainium4 (Annapurna) | [1×: Converge Digest] |
| Gov | 100k GPUs, IL6+ AI factories | [1×: Converge Digest] |
| Software | Nemotron on Bedrock/SageMaker; cuDF ≤3.7× EMR; cuVS ≤9× OpenSearch index | [1×: Converge Digest] |

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] §Catalysts Rubin ramp and the “compute is revenue” framing — a named 2M 2027–28 add is harder than qualitative “demand strong.” Does **not** refute custom-silicon share (Trainium4 still ships); it reframes XPU as **alongside** merchant GPUs in a common Fusion rack. **Second-order support** [[Theses/NBIS - Nebius Group]] contracted-GW vs energised-MW test (hyperscaler Rubin intensity). **Supports** [[Theses/000660 - SK Hynix]] HBM4/NVHBM intensity if multi-vendor base-die quals land. Conviction/status unchanged.

## Source Excerpts
> "AWS plans to deploy an additional 2 million NVIDIA Blackwell Ultra, Rubin and Rubin Ultra GPUs in 2027-2028 across AWS Global Infrastructure." [web: convergedigest.com]

> "Amazon’s Annapurna Labs will extend its use of NVIDIA NVLink Fusion to NVIDIA’s new custom high-bandwidth memory technology, NVHBM." [web: convergedigest.com]
