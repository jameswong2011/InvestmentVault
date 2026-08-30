---
publish: false
date: 2026-08-28
tags: [research, daily-intel-triage, news, NVDA, MRVL, 000660]
sector: DRAM & HBM Memory
ticker: NVDA
source: 'https://convergedigest.com/nvidia-nvhbm-nvlink-fusion-custom-hbm-aws-trainium4'
propagated_to: [NVDA, MRVL, 000660]
source_type: news
---

# NVIDIA NVHBM: Memory Controller Moves Into HBM Base Die — Annapurna First Collaborator

## Thesis Delta
Consensus heard NVIDIA’s NVHBM blog as a bandwidth/power slide — Converge Digest supplies the **mechanism + first customer** the blog under-specified: controller off the XPU die into the HBM base die (**≤30% BW / ≤15% HBM power / ≤25% compute-die area vs HBM4E**), multi-vendor standard using the same tech as future NVIDIA GPUs, and **Annapurna as first named collaborator** with Trainium4 Fusion support so Trainium and NVIDIA GPUs share MGX racks. Consensus prices custom XPUs as NVDA share loss; this is a **share-retention path around XPUs**. **Supports** [[Theses/NVDA - Nvidia]] Fusion lock-in; **Supports** [[Theses/MRVL - Marvell Technology]] Trainium/networking adjacency; **Supports** [[Theses/000660 - SK Hynix]] if SKH/Samsung/Micron disclose NVHBM base-die quals. Distinct from 2026-08-27 NVIDIA blog ingest. No trigger fire.

## Summary
NVHBM moves NVIDIA’s memory controller from the XPU compute die into the 3D HBM base die, claiming up to 30% more bandwidth, 15% lower HBM power, and up to 25% more XPU compute-die area vs standard HBM4E (NVIDIA blog had said “up to 30%” area — sources disagree). NVIDIA will standardize NVHBM across multiple memory suppliers. AWS Annapurna is the first announced collaborator; NVLink Fusion support starts on Trainium4. Nafea Bshara (Annapurna VP) is quoted endorsing the collaboration. Analysis: Fusion started as scale-up fabric access while hyperscalers keep XPUs; NVHBM pushes NVIDIA IP onto the compute–memory boundary — vertically integrated but heterogeneous AI infra.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Date | ~26 Aug 2026 | [web: convergedigest.com] |
| BW vs HBM4E | up to +30% | [1×: NVIDIA via Converge Digest] |
| HBM power | up to −15% | [1×: Converge Digest] |
| XPU die area freed | up to +25% (vs “up to 30%” in NVIDIA blog) | [1×: Converge Digest] |
| First collaborator | Amazon Annapurna Labs | [1×: Converge Digest] |
| Fusion start | Trainium4 | [1×: Converge Digest] |
| Multi-sourcing | Standard NVHBM across memory vendors | [1×: Converge Digest] |

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] NVLink Fusion / custom-silicon coexistence thesis — AWS taking NVIDIA controller IP + fabric while keeping Annapurna silicon. **Does not refute** [[Theses/MRVL - Marvell Technology]] custom-silicon shepherding (Trainium still exists); may raise the bar for non-Fusion XPUs. **Supports** [[Theses/000660 - SK Hynix]] HBM content intensity if NVHBM base dies require leading packaging — confirm/refute on supplier quals. Conviction/status unchanged.

## Source Excerpts
> "NVHBM moves NVIDIA’s memory controller from the XPU compute die into the HBM base die… up to 30% greater memory bandwidth, 15% lower HBM power consumption and up to 25% more available XPU compute-die area." [web: convergedigest.com]

> "Amazon’s Annapurna Labs will be the first announced customer to collaborate with NVIDIA on NVHBM." [web: convergedigest.com]
