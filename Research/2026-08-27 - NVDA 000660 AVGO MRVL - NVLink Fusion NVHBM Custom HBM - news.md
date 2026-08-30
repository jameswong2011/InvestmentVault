---
publish: false
date: 2026-08-27
tags: [research, daily-intel-triage, news, NVDA, 000660, AVGO, MRVL]
sector: DRAM & HBM Memory
ticker: NVDA
source: 'https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory'
propagated_to: [NVDA, 000660, AVGO, MRVL]
source_type: news
---

# NVIDIA NVLink Fusion Expands With NVHBM Custom High-Bandwidth Memory — Controller-in-Base-Die vs HBM4E

## Thesis Delta
Consensus still prices HBM as a JEDEC stack whose controller lives on the XPU, so SK Hynix/Samsung/Micron compete on cube yield and I/O speed while custom XPUs (AVGO/MRVL/Trainium) buy "standard HBM4E" — this 26 August NVIDIA blog **moves NVIDIA's custom memory controller into the HBM base die (NVHBM)**, claims **up to +30% memory bandwidth, −15% HBM power, and up to +25% freed XPU compute area vs standard HBM4E**, standardises the implementation across "leading memory partners," and names **Annapurna Labs as first collaborator with Trainium4 on NVLink Fusion**. That is an architectural remap of the HBM value layer, not a bit-growth print. It **supports** [[Theses/NVDA - Nvidia]] Fusion-as-containment of custom silicon; **raises the question** for [[Theses/000660 - SK Hynix]] whether SKH is inside the "multiple memory providers" set (unnamed here); **supports** [[Theses/MRVL - Marvell Technology]] Insight #3 (Fusion as UALink containment) via the same rack-scale perimeter; **second-order** for [[Theses/AVGO - Broadcom]] XPUs that want Fusion attach. No conviction-trigger fire: 000660 HIGH/LOW/CLOSE are Rubin-share / Namics / CXMT, not NVHBM; MRVL first-confirming observable is OCP UALink vs Fusion, not this blog.

## Summary
NVIDIA announced on August 26, 2026 that NVLink Fusion expands with NVHBM custom high-bandwidth memory. Jesse Clayton (NVIDIA blog) frames NVHBM as an expansion of NVLink Fusion for semi-custom XPUs. Traditional HBM puts the memory controller on the XPU die; NVHBM, "built on the same technology that NVIDIA will use for future GPUs," integrates NVIDIA's custom memory controller into the 3D HBM stack. Vendor-claimed deltas vs standard HBM4E: up to 30% more bandwidth, 15% lower HBM power, up to 25% more XPU compute area. NVIDIA will publish a standard NVHBM implementation "available from multiple memory providers" to cut multi-supplier qualify effort for Fusion customers.

Amazon Annapurna Labs is the first named collaborator. AWS already supported NVLink Fusion; Annapurna will support Fusion on next-generation Trainium starting with **Trainium4**, so Amazon chips and NVIDIA GPUs can share a rack-scale architecture. Nafea Bshara: "NVHBM represents a new architectural approach to advancing high-bandwidth memory performance and efficiency." Fusion itself remains the prior offer: NVLink chiplets, NVLink-C2C, NVLink Switches, MGX racks — hyperscalers keep XPU differentiation and rent NVIDIA's scale-up/scale-out stack. Memory vendors are not named beyond "leading memory partners."

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Date | 26 Aug 2026 | [web: blogs.nvidia.com] |
| Product | NVHBM on NVLink Fusion | [web: blogs.nvidia.com] |
| Mechanism | NVIDIA custom memory controller moved into HBM base die | [web: blogs.nvidia.com] |
| vs HBM4E bandwidth | up to +30% | [1×: NVIDIA blog] |
| vs HBM4E HBM power | −15% | [1×: NVIDIA blog] |
| vs HBM4E XPU area | up to +25% compute-die area freed | [1×: NVIDIA blog] |
| Supply | "standard NVHBM implementation" from "multiple memory providers" | [1×: NVIDIA blog] |
| First collaborator | Amazon Annapurna Labs | [web: blogs.nvidia.com] |
| Trainium | Fusion support from Trainium4; Amazon chips + NVIDIA GPUs in common rack | [web: blogs.nvidia.com] |
| Quote | Nafea Bshara, VP Annapurna | [web: blogs.nvidia.com] |
| Scope | same tech NVIDIA will use for future GPUs | [1×: NVIDIA blog] |

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] §Industry Context / Fusion: custom XPUs attach to an NVIDIA-defined memory+fabric stack rather than a merchant JEDEC cube — a containment move consistent with the CUDA/systems moat, not a new earnings line. **Open for** [[Theses/000660 - SK Hynix]] Insight #2 (architecture vs process): if NVHBM requires a NVIDIA-specified base die, the competitive axis shifts further from MR-MUF chemistry toward who can ship NVIDIA's controller-in-stack; SKH is **not named**. Does **not** fire HIGH (Rubin ≥60% / HBM4E sole-source / Kinex 16-Hi / Namics) or LOW (>35% Samsung Rubin). **Supports** [[Theses/MRVL - Marvell Technology]] Insight #3 (Fusion as UALink containment) and the Trainium4 Fusion path already in the Celestial/Amazon warrant story — first confirming observable remains OCP 2026, not this blog. **Second-order** [[Theses/AVGO - Broadcom]]: OpenAI/Google XPUs that want Fusion memory attach inherit NVIDIA's controller spec; Tomahawk still sits in scale-out regardless. No status/conviction change.

## Source Excerpts
> "By integrating the memory controller into the 3D HBM stack instead of the XPU, NVHBM delivers up to 30% greater memory bandwidth and 15% lower HBM power consumption, and frees up to 25% more area on XPU compute die compared with standard HBM4E." [1×: NVIDIA blog]

> "Annapurna Labs will support NVLink Fusion with its next-generation Trainium chips starting with Trainium4, which would allow Amazon chips and NVIDIA GPUs to work together with common rack-scale architecture." [web: blogs.nvidia.com]
