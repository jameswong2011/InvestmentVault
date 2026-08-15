---
publish: false
date: 2026-08-13
updated: 2026-08-14
tags: [research, daily-intel-triage, news, AMD, TSM, AVGO, 000660]
sector: Compute & AI Compute Accelerators
ticker: AMD
propagated_to: [AMD, TSM, AVGO, 000660]
source: 'https://www.servethehome.com/amd-instinct-mi455x-deep-dive-cdna-5-marks-the-next-era-of-instinct/'
source_type: news
---

# AMD Instinct MI455X: CDNA 5 on TSMC N2, 12-Stack HBM4, Helios Rack

## Thesis Delta
Consensus prices [[Theses/AMD - Advanced Micro Devices]] Instinct as a CUDA-gap second source whose silicon stays one node and one HBM generation behind [[Theses/NVDA - Nvidia]] Rubin, so the OpenAI/Meta 6GW warrants are procurement insurance rather than a hardware-parity event → ServeTheHome’s Advancing AI 2026 teardown implies a different operating variable: MI455X is AMD’s first TSMC N2 GAAFET GPU, the first CDNA 5 part, and a 12-stack HBM4 package whose memory-bandwidth-per-FLOP *rises* versus MI355X — a hardware parity-*attempt* versus Rubin, not a software-moat collapse. Hypotheses to test, not verdicts: Industry #8 (rack-scale remaps the binding constraint to UAL interconnect + tray power — 3.6 TB/s scale-up and >2 kW/GPU, four accelerators per Helios tray); #1 (the scarce complementary assets are N2 logic + 12×HBM4, not peak FP4); [G-13] (the AMD multiple already embeds the GW hardware this chip must deliver into the §Conviction Triggers HIGH MLPerf); [G-10] (first-attempt next-gen training parity is rare); VLM §3 (infrastructure-layer toll at [[Theses/TSM - Taiwan Semiconductor]] N2 and [[Theses/000660 - SK Hynix]] HBM4; AMD is a layer-renter on those two).

## Summary
ServeTheHome’s 2026 Advancing AI deep-dive (vault-dated 2026-08-13; source URL dated to the event window) treats Instinct MI455X as the cornerstone of AMD’s next-year server-GPU lineup and of the Helios rack-scale systems wrapped around it. The piece opens from industry structure, not a model: ultra-large GPUs sit at the center of AI servers because they combine memory bandwidth with dense math, and that role has become a major product category and a major revenue line across tech. For AMD the AI boom has been company-transforming — Instinct, launched almost a decade ago, has gone from a handful of sales to helping drive data-center sales to over 50% of total revenue. If EPYC CPUs are not the single most important product line at AMD in 2026, Instinct is. That success is the pressure: the company must keep growing the server-GPU franchise, which is why the Advancing AI event put GPU silicon and Helios racks on center stage.

MI455X is framed as AMD’s fastest server GPU to date *and* as the introduction of CDNA 5, called the biggest server-GPU architecture overhaul in over a decade. The advertised combination is architectural rewrite + TSMC’s first GAAFET node (N2 / 2nm) + a heavy networking emphasis. At the surface CDNA 5 “does not bring much in the way of new high-level features”; the claim is that this hides the changes underneath, that the chip is unlike anything AMD has shipped, and that it is the blueprint for every Instinct GPU that follows. MI455X is the prime, full-featured, fully-enabled CDNA 5 implementation: revised core, HBM4, N2 compute dies. Versus the immediate predecessor MI355X, AMD is touting a 4× peak improvement in matrix (tensor) performance at FP4 and FP8, with peak compute for most other formats set to double — raw throughput only, before the rest of the architecture’s efficiency work.

A single MI455X is specified at a bit over 40 PFLOPS of dense FP4 tensor, half that for FP6 and FP8. Vector has not been dropped: 315 TFLOPS of FP32 (or FP16) vector, roughly twice MI355X. The simplest driver of the transistor count is N2 density — 320 billion transistors, +72% versus the prior generation — plus N2’s leakage-control perk beyond logic density. CDNA 5 is described as borrowing and enhancing the RDNA SIMD32 ALU organization, the largest change to AMD’s server-GPU architectures since Instinct launched. STH’s efficiency thesis is that this organization is a better fit to the instruction flows AI compilers actually emit.

The memory subsystem is written as larger than the compute step-up. Twelve HBM4 stacks (four more than MI355X) deliver 23.3 TB/s, 2.9× MI355X bandwidth. STH flags this as one of the rare generations where memory bandwidth per compute FLOP *increases* rather than falls — the mechanism they assign to MI455X being more architecturally efficient than MI355X. Capacity does not keep up with that multiple: 36 GB per stack × 12 = 432 GB local, 1.5× MI355X, one of the few specs that does not double. The bottleneck named is not AMD’s stack count; it is the slowed pace of DRAM density, with all parties stuck on it. I/O is the other bandwidth upgrade and, in STH’s ranking, the unlock for Helios: 3.6 TB/s via Ultra Accelerator Link (UAL) scale-up lanes, plus more via UAL, PCIe, and xGMI, for over 4× the aggregate link bandwidth of MI355X. For this generation “moving data was as important (if not more so) than computing it.”

The trade-off is power. MI355X already ran up to 1,400 W per accelerator. AMD has not disclosed MI455X TDP (STH’s parenthetical: customers are meant to buy by the rack). A Helios rack is written at upwards of 245 kW, majority to GPUs; STH estimates MI455X “somewhere north of 2 kW” per GPU. That power envelope, together with networking-topology constraints, is why Helios puts only four MI455X devices in a compute tray. Claim scope is a product-roadmap teardown around the Advancing AI event — no wafer starts, N2 allocation, CoWoS share, ASP, or shipment volume. The Inbox extract is truncated: the clip ends at the four-GPU tray and does not retain the rest of the published STH article (die breakdown, floorplan, further Helios topology). Vault header annotation on the Inbox file tags Helios as a Broadcom fabric and as an N2/HBM4 demand print for TSM/000660; the extracted STH body itself names UAL / PCIe / xGMI and does not name Broadcom.

## Evidence

| Chip / system | Spec | vs MI355X | Tag |
|---|---|---|---|
| Process (compute dies) | TSMC N2 (2nm GAAFET) | First Instinct on N2; prior gen N3/N4-class | [web: servethehome.com] |
| Architecture | CDNA 5 (prime, fully enabled) | Largest server-GPU rewrite since Instinct launch (~decade) | [web: servethehome.com] |
| Transistors | 320 billion | +72% | [web: servethehome.com] |
| Dense FP4 tensor | >40 PFLOPS | 4× peak matrix at FP4/FP8 (AMD-touted) | [web: servethehome.com] |
| Dense FP6 / FP8 tensor | ~20 PFLOPS (half of FP4) | 4× peak matrix at FP8 (AMD-touted) | [web: servethehome.com] |
| FP32 / FP16 vector | 315 TFLOPS | ~2× | [web: servethehome.com] |
| Other-format peak compute | — | ~2× for most non-FP4/FP8 formats | [web: servethehome.com] |
| HBM stacks | 12 × HBM4 | +4 stacks vs 8 | [web: servethehome.com] |
| HBM capacity | 432 GB (36 GB/stack) | 1.5× | [web: servethehome.com] |
| HBM bandwidth | 23.3 TB/s | 2.9× | [web: servethehome.com] |
| Bandwidth per FLOP | Rises gen-on-gen | STH: rare inversion vs usual decline | [web: servethehome.com] |
| Scale-up I/O | 3.6 TB/s UAL | Part of >4× aggregate link | [web: servethehome.com] |
| Other I/O | UAL + PCIe + xGMI | Aggregate link >4× | [web: servethehome.com] |
| MI355X TDP | Up to 1,400 W | Disclosed prior-gen ceiling | [web: servethehome.com] |
| MI455X TDP | Undisclosed; STH “north of 2 kW” | [est.] from 245 kW rack, GPU-majority | [web: servethehome.com] [est.] |
| Helios rack power | Upwards of 245 kW | Majority to GPUs | [web: servethehome.com] |
| Helios compute tray | 4 × MI455X | Power + topology constraint | [web: servethehome.com] |
| AMD DC mix (context) | Data center >50% of company revenue | Instinct a primary driver | [web: servethehome.com] |

| Mechanism STH assigns | Content | Tag |
|---|---|---|
| N2 perks beyond density | Leakage control on compute dies | [web: servethehome.com] |
| CDNA 5 ALU organization | RDNA-like SIMD32, better fit to AI instruction flows | [web: servethehome.com] |
| Efficiency claim | Bandwidth/FLOP up + CDNA 5 rewrite → more efficient than MI355X | [web: servethehome.com] |
| Capacity ceiling | DRAM density, not AMD stack-count effort (12 stacks already) | [web: servethehome.com] |
| Helios unlock | I/O (UAL) ranked as important as, or more than, compute | [web: servethehome.com] |
| Four-GPU tray | >2 kW/GPU [est.] + networking topology | [web: servethehome.com] [est.] |
| Feature-surface caveat | Few new high-level features; changes are underneath | [web: servethehome.com] |
| What the source does not give | Volume, ASP, N2 wafer allocation, CoWoS share, MLPerf, TDP | [web: servethehome.com] |

## Contradiction Check
**[[Theses/AMD - Advanced Micro Devices]] §Summary** (“sole merchant full-stack alternative”) and **§Key Non-consensus Insights #2** (Helios as the only non-Nvidia rack stack: 72 MI455X, 31 TB HBM4, 3 AI exaflops) get a hardware-spec update, not a close: STH’s 12 × 36 GB = 432 GB/GPU × 72 is 31.1 TB, matching the thesis rack memory line, and four GPUs/tray × 18 trays is the 72-GPU Helios geometry the thesis already uses. **§Outstanding Questions #2** (is Helios rack-for-rack competitive with Rubin GR200 or one generation behind at H2 2026 launch?) and **§Conviction Triggers → HIGH** (MLPerf Training v5.0 MI455X within 10% of Rubin GR200 on Llama 5-class *and* Meta Llama 5 on ROCm *and* a third ≥2 GW hyperscaler) remain unfired — this source has no benchmark, no ROCm result, and no third-customer print. **§Conviction Triggers → LOW** (Helios gap >25% to Rubin on published MLPerf, *or* OpenAI/Meta take-or-pay cut >30%, *or* 2027 CoWoS <12%) is also unmoved. The surface-feature caveat (CDNA 5 adds little at the programming-model layer) is consistent with the thesis **§Risks** line that software/composability still gates Helios displacement; STH does not speak to ROCm, UALink bring-up, or CUDA. [G-10] / [G-13]: a 4× FP4 slide and a 2.9× HBM-bandwidth print are the *inside-view* inputs the HIGH trigger was written to falsify; they do not themselves fire it.

**[[Theses/TSM - Taiwan Semiconductor]] §Summary** (sold-out N2 at a 10–20% premium; monopoly rents being harvested) and **§Key Non-consensus Insights #5** (N2 pricing power) are directionally supported: another large, 320-billion-transistor N2 GPU customer exists and is being productized as the 2026–27 Instinct flagship. **§Insight #1** (CoWoS as a separable sold-out annuity; AVGO/AMD/custom fight for residual after NVDA) is implied, not measured — STH never names CoWoS, CoWoS-L, or allocation. **§Conviction Triggers → HIGH-reaffirm** (FY26 >40% USD growth *and* Q3 GM ≥66% *and* 2027 capex ≥$70B) and **→ LOW** (HPC growth <10% or GM <63% for two quarters) are earnings gates this product article cannot touch. Hypothesis: #1/#8 — if Helios ships at 12-stack HBM4 on N2, the binding constraint stays packaging + HBM + N2 wafers, not AMD demand.

**[[Theses/AVGO - Broadcom]] §Summary** (Ethernet/Tomahawk as the open-standards backbone “regardless of compute vendor”) and **§Key Non-consensus Insights #1** (Tomahawk sits in the data path of Nvidia GPUs, custom ASICs, *or AMD accelerators*) are compatible with Helios’s UAL/xGMI/PCIe scale-up story and with the Inbox header’s “Broadcom fabric” annotation, but the extracted STH body does not name Broadcom, Tomahawk, or UALink-Ethernet retimers. AVGO has **no §Conviction Triggers** section; the closest live claim is **§Bull Case** “Ethernet is winning / every AI cluster needs switching silicon.” Treat merchant-switch attach as a hypothesis, not a STH datapoint.

**[[Theses/000660 - SK Hynix]] §Summary** (HBM4 Rubin-cycle share path; kill if Samsung >35% of Rubin SKU allocation in the first two shipping quarters) and **§Conviction Triggers → HIGH** (Rubin HBM ≥60% SK Hynix) get an incremental *demand* print, not an allocation print: a 12-stack HBM4 GPU is a larger per-device pull than the 8-stack MI355X and competes for the same qualified HBM4 pool the thesis already assigns primarily to Rubin. STH does not name the memory vendor. L1 / #2: 12-Hi HBM4 at 36 GB/stack is a qualification-gated stack, not commodity DRAM.

**[[Theses/NVDA - Nvidia]] §Summary** (moat is the software/simulation stack, not peak FLOPS) and **§Outstanding Questions** (CUDA durability as ASICs and ROCm improve) are not closed by a CDNA 5 spec sheet. **§Bear Case** share-erosion toward 60% is the scenario this hardware would have to *enable*; STH supplies the silicon description, not the software or shipment evidence. NVDA also has **no §Conviction Triggers** section; the thesis Log already treats Fall 2026 MLPerf Training v5.0 as the kill/confirm event versus MI455X.

## Source Excerpts
> "If not EPYC CPUs, then Instinct GPUs are the single most important product line at AMD in 2026."

> "the Instinct MI455X is not only AMD’s fastest server GPU to date, but it marks the introduction of the radically revised CDNA 5 architecture, AMD’s biggest server GPU architecture overhaul in over a decade."

> "At the surface level, CDNA 5 does not bring much in the way of new high-level features, but this belies all of the major changes that AMD has made underneath. It is a GPU unlike anything AMD has done before, and it is the blueprint for all the server GPUs that will eventually follow."

> "AMD is touting a 4x peak improvement in matrix (tensor) performance with the all-critical FP4 and FP8 precisions. Meanwhile, peak compute performance for most other formats is set to double."

> "a single MI455X can process a bit over 40 PFLOPS of dense FP4 tensor operations or half that for FP6 and FP8."

> "The chip can chew through 315 TFLOPS of FP32 (or FP16) vector operations, roughly twice the rate of the MI355X."

> "AMD is now able to assemble a chip with 320 billion transistors, a 72% increase from the previous generation."

> "Essentially borrowing and enhancing the core compute architecture of AMD’s RDNA line of GPUs, which introduced a similar, SIMD32-based approach to ALU organization, CDNA 5 is the biggest change to AMD’s server GPU architectures since the Instinct line was launched almost a decade ago."

> "AMD has equipped the chip with 12 stacks of HBM4 memory, 4 more stacks than the MI355X. Which, thanks to all of the generational improvements in HBM4, gives the chip some 23.3 TB/second of memory bandwidth, 2.9x the bandwidth of the MI355X."

> "the release of the MI455X will be one of those rare times where we see the amount of memory bandwidth per compute FLOP actually increase from one generation to the next"

> "At 36GB per stack, AMD can outfit MI455X with 432GB of local memory, some 1.5 times the capacity of MI355X."

> "At this point, all parties are bottlenecked by the slowed pace of DRAM density increases these days."

> "With 3.6TB/second of bandwidth available via Ultra Accelerator Link (UAL) lanes for scale-up fabrics, and more still via UAL, PCIe, and xGMI, MI455X offers over 4x the aggregate link bandwidth of MI355X."

> "For this generation of AMD hardware, moving data was as important (if not more so) than computing it for the company."

> "MI355X was already a toasty chip at up to 1400 Watts for a single accelerator. AMD has not even disclosed the power consumption of MI455X"

> "with a Helios rack consuming upwards of 245 kW of power, and with the majority of that going to GPUs, MI455X is thought to be somewhere north of 2 kW per GPU. Which, next to networking topology considerations, is one of the reasons that AMD is only putting four of them in a Helios compute tray."
