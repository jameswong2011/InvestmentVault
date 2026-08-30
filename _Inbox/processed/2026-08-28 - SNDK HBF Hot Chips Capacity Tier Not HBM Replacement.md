---
date: 2026-08-28
tags: [daily-intel-triage, news, SNDK, 285A]
source: 'https://global.techapple.com/2026/08/hot-chips-2026-analysis-suggests-high-bandwidth-flash-is-a-high-capacity-memory-not-an-hbm-replacement'
source_type: news
holdings: [SNDK, 285A]
score: 9
---

# Hot Chips: HBF Is High-Capacity Tier, Not an HBM Replacement

**Source:** https://global.techapple.com/2026/08/hot-chips-2026-analysis-suggests-high-bandwidth-flash-is-a-high-capacity-memory-not-an-hbm-replacement
**Date:** 2026-08-27 · **Brief score:** 9 · **Tags:** daily-intel-triage

## Why it matters (portfolio)
Frames SanDisk **SNDK** (and Flash Ventures peer **285A**) HBF thesis honestly: capacity/MoE/cold-tier, not HBM kill-shot; software readiness is the gating risk.

## Article body

Hot Chips 2026: Analysis Suggests High Bandwidth Flash Is a High-Capacity Memory, Not an HBM Replacement (TechApple Global, Aug 27, 2026).

OXMIQ Labs at Hot Chips 2026: HBF cannot replace HBM across the vast majority of workloads. HBF could be a specialized tier for huge but relatively cold datasets; for others it can do more harm than good.

SanDisk HBF grades: G1 8-Hi 256GB / 8 GT/s UCIe / 384 GB/s; G2 512GB / 16 GT/s / 1.536 TB/s; G3 512GB / 32 GT/s UCIe 2.0 / 3.072 TB/s. Main feature is 8–16× more capacity than HBM at roughly the same cost — not raw bandwidth.

OXMIQ 72-GPU rack model (Kimi-K2 1T FP4, cost/power parity): HBM-only 20.7TB / 1,584 TB/s aggregate BW; HBF-only 294.9TB (14× capacity) but only 922 TB/s (~60% BW); hybrid 89.3TB with 279–1,418 TB/s depending on workload. HBF-only enables 72 model instances/rack vs 9 for HBM-only — attractive when capacity sets GPU count; as users/token rates climb, HBF BW becomes bottleneck and HBM rack wins on cost/token. Conclusion: "HBM for the rack, HBF for the box."

MoE fit: Kimi-K3 example 1.56TB weights of which 1.45TB (93%) are MoE experts — mostly write-once / infrequent read → keep experts in HBF, hot weights in HBM; also long-context KV cache. Software is the hardest part: large DMA transfers (64KB reads / 1MB writes), write endurance; vLLM would need dedicated HBF support; AMD/NVIDIA need HW/driver paths between HBF and HBM.

