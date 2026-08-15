---
publish: false
date: 2026-06-03
tags: [research, AI-infrastructure, compute, neoclouds, memory, NVDA, TSM]
sector: Compute & AI Compute Accelerators
ticker: NVDA
source: 'https://substack.com/home/post/p-195347754'
source_type: deep-dive
propagated_to: [NVDA, CRWV, NBIS, TSM, 000660]
---

# AI Value Capture and GPU Rental Economics — The Shift to Model Labs

## Thesis Delta

Reframes where AI value now accrues: **the AI labs captured almost all the marginal value in 2025-26** (Anthropic ARR $9B→$44B+, inference gross margin 38%→70%), while **Nvidia and TSMC are deliberately under-pricing** scarce compute — a strategic "central bank" restraint, not an inability to charge. Two actionable vault implications: (1) an explicit, unpriced **NVDA pricing-lever bull vector** (SOCAMM memory disaggregation at ~60% margin; ~40% theoretical server-price headroom on Rubin before crossing the neocloud return hurdle) — input for [[Theses/NVDA - Nvidia]]; (2) a named **GPU-rental-economics framework** ("One Chart to Rule Them All") that bounds neocloud ([[Theses/NBIS - Nebius Group]] / [[Theses/CRWV - CoreWeave]]) pricing power between a cost-based floor (~$4.92/hr/GPU for Vera Rubin) and a value-based ceiling (~$9.63-12.25/hr).

## Summary

SemiAnalysis (Daniel Nishball) argues that agentic AI crossed a real inflection in **December 2025**, driving a step-change in the economic value of a token while software + hardware improvements collapsed the cost of producing one. The result is a value-capture regime shift: from 2023-25 *all* AI value went to the infrastructure layer (Nvidia, power names Vistra/GE Vernova, then 2025's memory complex — SanDisk/WDC/Seagate/Micron all +200%), with model-creator margins "famously bad." Now the **labs capture a disproportionate share** — Anthropic's inference gross margin went 38%→>70% and ARR $9B→$44B+ — because the gap between a frontier token's price and the economic value of the work it produces is the widest it has ever been.

The mechanism is two-sided. **Token value rose** (agentic workloads do work that previously cost tens of person-hours). **Token production cost fell** even faster: Blackwell generates ~30x more tokens/sec on frontier workloads than Hopper a year ago; software alone (wideEP + disaggregation + MTP) yields up to 14x throughput on the same B300; GB300 NVL72 achieves ~17x H100 throughput in FP8 (32x in FP4) for only ~70% higher TCO/GPU. Crucially, the author argues lab margins **won't be competed away**: frontier models retain pricing power (open-source like Kimi K2.6 exerts little downward pressure on Opus), and compute is so constrained that no single lab can serve the whole market — so any lab with true frontier quality can price to the *value delivered* rather than to cost. Anthropic has further margin levers via SKU laddering (Opus 4.5 cut to $5/$25 but margins rose on cost reduction + volume mix-shift to Opus; Opus fast priced 6x, Mythos $25/$125).

The central tension: **Nvidia and TSMC, the two firms with the most pricing power, "haven't flinched."** N3 utilization is expected to exceed 100% in 2H26 and DRAM fabs already run >90%, yet wafer and system pricing remain anchored to cost-based frameworks. The author frames this as deliberate restraint ("Nvidia as the central bank of AI") — supporting ecosystem development and avoiding antitrust scrutiny and customer diversification, the same playbook TSMC has long run (protect downcycle profitability, blunt upcycle extraction, prefer long-term relationships + prepayments over scarcity pricing). The verdict is that this is leaving value on the table and is "unlikely to hold": as inference ROI becomes accepted, pricing shifts from cost-based to value-based, opening room for Nvidia to raise — "they should strike while the iron is hot."

The most specific lever identified is **memory, via SOCAMM**. Because Vera Rubin NVL72 uses a *socketed* LPDDR module (SOCAMM2) rather than GB300's soldered LPDDR5X, Nvidia can disaggregate memory as its own line item and reprice it independently of the board — and memory, unlike the GPU, is not an antitrust concern, so it is the cleaner vector for price discrimination. The counterweight is **compute competition**: Anthropic has diversified to Trainium/TPU (Mythos was *not* trained on Nvidia), and credible lower-cost alternatives (Amazon/Google paying lower margins to Marvell/Alchip/Broadcom/Mediatek than Nvidia charges) limit how aggressively Nvidia can price without accelerating diversification.

## Framework / Mental Model

**"One Chart to Rule Them All" — GPU rental economics (cost floor vs value ceiling).** A framework for understanding neocloud pricing power and where AI-cluster value accrues, built from two bounding constraints plus a returns curve:

1. **Cost-based pricing = the FLOOR.** GPU deployments only happen if a project clears the neocloud's minimum IRR hurdle. Today most projects earn mid-to-high-teens IRR; an illustrative GB300 deployment ≈ **15.6% IRR** over 5 years with a 15% prepay. For Vera Rubin NVL72 to earn that same 15.6% hurdle requires a rental price of **≥ ~$4.92/hr/GPU** (5-yr, 15% prepay). Below the floor, capacity is not greenlit until pricing adjusts up.

2. **Value-based pricing = the CEILING.** Anchored to $/FLOP parity — the maximum a renter would pay to remain indifferent between Rubin and current-gen GPUs. Using GB300 at ~$0.70/PFLOP (5-yr, FP8 dense), VR NVL72 ceiling ≈ **$12.25/hr/GPU** at parity; a conservative below-trend $0.55/PFLOP ⇒ **$9.63/hr/GPU** — nearly **2x the cost-based floor**. VR NVL72 is unusual in that the value-vs-cost gap is far larger than for GB300 or prior cards.

3. **The chart**: plot observed neocloud GPU rental prices against project IRRs. **Up-and-right along the curve = stronger neocloud bargaining power** (charging above hurdle). **A Nvidia price increase shifts the curve up-and-left** (a higher rental is needed to preserve the same IRR = stronger *supplier* bargaining power). The **top-left corner** (max rental/PFLOP ∩ min IRR hurdle) = maximum theoretical AI-cluster pricing; the gap between the current curve and that corner = headroom for Nvidia to raise system prices. At today's VR NVL72 pricing, neoclouds charge ~$4.90/hr for 15% IRR ⇒ $0.28/PFLOP for customers (a 60% cost drop vs GB300, *below trend*), implying **~40% server-price headroom** for Nvidia while still leaving neoclouds room to lift prices. Even neoclouds at $8/hr / 38% IRR = $0.46/PFLOP is still below the cost-improvement trend.

**Cost-based vs value-based as a general pricing lens**: when competition is intense, price → cost (low margin); monopolies price → value (high margin). The framework re-applies to any node where a scarce supplier sells into a higher-WTP downstream (Nvidia↔neocloud, Nvidia↔memory via SOCAMM markup, TSMC↔fabless).

## Evidence

**VR NVL72 vs GB300 (per-GPU, marketed):**

| Metric | GB300 NVL72 | VR NVL72 |
|---|---|---|
| Total cost / GPU / hr | $2.69 | $4.18 |
| Capex per watt | $37.4/W | $38.1/W (barely up despite TDP 1400W→2300W) |
| BF16 dense | 2,500 TFLOPS | 4,000 TFLOPS |
| FP8 dense | 5,000 TFLOPS | 17,500 TFLOPS |
| FP4 dense | 15,000 TFLOPS | 35,000 (50,000 w/ sparsity) |
| Memory bandwidth | 8 TB/s | 22 TB/s per logical GPU |
| TCO/PFLOP BF16 | $1.07 | $1.04 |
| TCO/PFLOP FP8 | $0.54 | $0.24 |
| TCO/PFLOP FP4 dense | $0.18 | $0.12 |

- Key spec nuance: BF16 flops/clock/SM **unchanged** from Blackwell; FP8/FP4 **doubled** → Rubin's gains concentrated in low precision (BF16 uplift comes only from higher SM count + clocks).

**SOCAMM memory pricing lever:**
- SOCAMM2 = socketed LPDDR module on VR NVL72 (vs GB300 soldered LPDDR5X) → disaggregated, independently repriceable.
- Nvidia SOCAMM contract cost ~$8/GB in 1Q26 (premium to mobile LPDDR5X ~$6-7/GB); exit-2026 could exceed $13/GB; ~$10/GB reasonable Nvidia cost assumption.
- Author argues Nvidia justified taking ~60% margin on SOCAMM (supply tightness + best-platform + own cost inflation); GB300 bundled DRAM at ~75% GM.
- Memory ≠ antitrust concern (GPU is) → preferred price-discrimination vector.

**Token economics:**
- Anthropic ARR $9B → $44B+ YTD (from $30B last update); inference GM 38% → >70%.
- Opus 4.5 priced $5/$25 (vs Opus 4/4.1 $15/$75); blended true price for Opus 4.7 agentic ~$0.99/MTok despite $5/$25 sticker (300:1 input:output, 90%+ cache hit, cached input $0.50/MTok). Mythos $25/$125; Opus fast 6x regular.
- Throughput: Blackwell ~30x tokens/sec vs Hopper (1yr); software (wideEP+disagg+MTP) up to 14x on same B300 (~1k → ~14k tok/s/gpu on DeepSeek R1, 8k-in/1k-out); GB300 NVL72 ~17x H100 FP8 throughput, 32x FP4.
- SemiAnalysis internal: token spend ~30% of comp; ~5B tokens/month/employee (>5x Meta); power-law, some staff >100B/month.

**Supply / pricing backdrop:**
- 1-yr H100 rental +40% from Oct 2025 bottom; memory prices +6x in past year; DRAM fabs >90% util; N3 util >100% expected 2H26.
- Networking price discrimination: SN5610 ~2x for neocloud vs hyperscaler, but 94% networking premium = only ~10% all-in rack-scale capital cost increase → limited remaining lever.
- N3 demand convergence: Nvidia, Broadcom, Annapurna, Mediatek, AMD all competing for N3 allocation; TSMC pricing stable.

**Competitive durability & pricing-restraint logic (per source):**
- *Why lab profits won't be competed away* — two reasons: (1) frontier models retain pricing power; open-source (Kimi K2.6 $0.95/$4) is "noticeably worse for real knowledge work" and exerts little downward pressure on Opus. (2) Compute constraints mean no single lab can serve the whole market — Anthropic already gates Claude Code behind $100+/month and blocks third-party harnesses (OpenClaw) — so demand outstrips supply and any frontier-quality lab prices to value, not to each other's margins.
- *Networking price discrimination*: Nvidia discriminates on networking (not GPU/memory) — the SN5610 can be ~2x for a neocloud vs hyperscaler (hyperscalers work directly with OEMs/ODMs and have the engineering bench; neoclouds prefer turnkey). But a 94% networking premium = only ~10% of all-in rack-scale capital cost, so the lever is largely exhausted.
- *TSMC as the template for Nvidia*: TSMC protects downcycle profitability and blunts upcycle extraction — preferring long-term relationships + capacity commitments + prepayments over scarcity pricing, leaving value on the table while fabless customers enjoy high GMs. Jensen said in 2024 that "TSMC should charge more for wafers" (to shut out lower-ability-to-pay competitors). The author concludes "Nvidia is starting to look a lot like TSMC," its greatest strength being procurement (disproportionate access to constrained TSMC wafers); the likely near-term path is LTAs/prepayments rather than headline price hikes.
- *MFU caveat*: VR NVL72 vs GB300 comparisons use *marketed* performance; effective throughput depends on model FLOPs utilization (MFU), which is lower on initial deployment before software/engineering matures — a gating factor for Rubin reaching value-based pricing at launch.

## Contradiction Check

**Supports** [[Theses/NVDA - Nvidia]] bull case with a concrete, *unpriced* mechanism — Nvidia holds material pricing optionality (SOCAMM 60% margin, ~40% Rubin server-price headroom) it has deliberately not exercised; "central bank" restraint is bullish for durability/ecosystem but means consensus may under-model a future margin step-up. Affected assumption: NVDA's forward gross-margin trajectory (consensus likely extrapolates the cost-based framework; the source argues a value-based regime shift is coming).

**Refines** the neocloud theses ([[Theses/NBIS - Nebius Group]], [[Theses/CRWV - CoreWeave]]): the One Chart framework formalizes that neocloud pricing power is **bounded above by Nvidia's pricing decision** — if Nvidia shifts the curve up-and-left (raises VR NVL72 prices), neocloud IRRs compress unless they pass it through. This is the quantitative backbone of the vault's "pricing power is upstream-pinned at Nvidia" sector thesis, and it sharpens the NBIS Vera Rubin deployment (H2 2026) risk/reward: the $4.92/hr floor vs $9.63-12.25 ceiling gap is the margin both NBIS and CRWV are fighting Nvidia for.

**Cross-validates** the memory complex ([[Theses/000660 - SK Hynix]], [[Theses/SNDK - SanDisk]], [[Theses/285A - Kioxia]]): SOCAMM/LPDDR5X tightness and "memory is the tightest constraint" reinforce the DRAM/HBM supercycle thread — but with a twist: Nvidia, not the memory makers, may capture the SOCAMM markup (60% margin to Nvidia), so memory-vendor upside is in volume/ASP, while the *system* markup accrues to Nvidia.

**Tension** with the NVDA bull: Anthropic's Trainium/TPU diversification (Mythos not on Nvidia) and lower-cost ASIC alternatives (via [[Theses/AVGO - Broadcom]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/MRVL - Marvell Technology]]) cap how far Nvidia can push value-based pricing — the same custom-silicon competition thread in [[Sectors/Custom Silicon & Networking Semiconductors]].

## Source Excerpts

- "any lab capable of providing true frontier quality will be able to charge based on the economic value delivered by the token rather than competing away each other's margins."
- "Even if Nvidia raises server pricing and infrastructure providers increase compute pricing, demand would remain intact. Buyers are optimizing for access to compute… marginal cost optimization is not their primary concern today."
- On capex/watt: "$/GW appears to remain largely stagnant from GB300 to VR NVL72… puzzling… given the step up in performance/W… is more than double."
- "Nvidia also has the opportunity to price discriminate on memory more than they do on the GPU because memory isn't an anti-trust concern whereas the GPU is."
- "Our verdict is they should strike while the iron is hot and take advantage of their long term advantages in memory pricing, capacity, and performance."

## Related Research
- [[Theses/NVDA - Nvidia]] · [[Theses/TSM - Taiwan Semiconductor]] · [[Theses/NBIS - Nebius Group]] · [[Theses/CRWV - CoreWeave]]
- [[Theses/AVGO - Broadcom]] · [[Theses/AMD - Advanced Micro Devices]] · [[Theses/MRVL - Marvell Technology]] (custom-silicon / ASIC competition that caps value-based pricing)
- [[Theses/000660 - SK Hynix]] · [[Theses/SNDK - SanDisk]] · [[Theses/285A - Kioxia]] (memory tightness / SOCAMM / LPDDR)
- [[Sectors/Neoclouds & GPU-as-a-Service]] · [[Sectors/Compute & AI Compute Accelerators]] · [[Sectors/Custom Silicon & Networking Semiconductors]]
- [[AI Bubble Risk and Semiconductor Valuations]]
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] (companion SemiAnalysis token-economics framing)
