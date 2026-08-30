---
publish: false
date: 2026-08-28
tags: [research, daily-intel-triage, news, SNDK, 285A]
sector: NAND & Storage
ticker: SNDK
source: 'https://global.techapple.com/2026/08/hot-chips-2026-analysis-suggests-high-bandwidth-flash-is-a-high-capacity-memory-not-an-hbm-replacement'
propagated_to: [SNDK, 285A]
source_type: news
---

# Hot Chips: HBF Is High-Capacity Memory Tier — Not an HBM Replacement

## Thesis Delta
Consensus swing trade on SanDisk HBF often prices it as “cheap HBM” — OXMIQ at Hot Chips 2026 says **HBF cannot replace HBM on most workloads**: at cost/power parity a 72-GPU rack goes from **20.7TB / 1,584 TB/s (HBM-only)** to **294.9TB but only 922 TB/s (~60% BW) HBF-only**; hybrid 89.3TB. Punchline: **“HBM for the rack, HBF for the box.”** Best fits: MoE expert weights (write-once / cold), fitting huge models, long-context KV. Software (vLLM + vendor DMA paths) is the hard gate. **Supports** [[Theses/SNDK - SanDisk]] HBF as capacity tier / ASP mix, not HBM-kill narrative; second-order [[Theses/285A - Kioxia]] Flash Ventures bit-add framing. No trigger fire.

## Summary
OXMIQ reported at Hot Chips 2026 (published 27 August 2026). SanDisk HBF grades: G1 256GB/384 GB/s; G2 512GB/1.536 TB/s; G3 3.072 TB/s @ 32 GT/s UCIe 2.0. Main feature is 8–16× capacity vs HBM at similar cost, not raw BW. OXMIQ Kimi-K2 FP4 rack model shows capacity×14 with BW cut to ~60% in HBF-only; HBF enables 72 instances/rack vs 9 HBM-only when capacity binds, but loses on cost/token as concurrency rises. MoE example (Kimi-K3): 93% of 1.56TB weights are expert weights suitable for HBF while hot weights stay in HBM. Software not ready: large DMA transfers, endurance management, need accelerator vendor + framework support.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Date | Hot Chips 2026 / 27 Aug write-up | [web: global.techapple.com] |
| Source | OXMIQ Labs analysis | [1×: TechApple] |
| HBM-only rack | 20.7TB / 1,584 TB/s | [1×: OXMIQ via TechApple] |
| HBF-only rack | 294.9TB / 922 TB/s (~60% BW) | [1×: OXMIQ via TechApple] |
| Hybrid | 89.3TB; 279–1,418 TB/s | [1×: OXMIQ via TechApple] |
| Capacity vs HBM | 8–16× at ~same cost | [1×: TechApple] |
| G1/G2/G3 | 384 / 1.536 / 3.072 TB/s | [1×: TechApple] |
| MoE expert share ex. | 93% of 1.56TB weights | [1×: TechApple] |

## Contradiction Check
**Supports** [[Theses/SNDK - SanDisk]] HBF as complementary capacity tier (MoE/cold/long-context) — **challenges** any bull framing that HBF displaces HBM attach in 2027 racks. Software readiness is the honest bear. Second-order [[Theses/285A - Kioxia]] unchanged on Flash Ventures bit-add. Conviction/status unchanged.

## Source Excerpts
> "OXMIQ Labs said High Bandwidth Flash cannot replace HBM across the vast majority of workloads." [web: global.techapple.com]

> "HBM for the rack, HBF for the box." [web: global.techapple.com]
