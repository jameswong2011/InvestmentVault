---
publish: false
date: 2026-05-31
tags: [research, semiconductors, memory, DRAM, HBM, 000660, supercycle]
sector: DRAM & HBM Memory
ticker: "000660"
source: 'https://substack.com/home/post/p-186096534'
source_type: deep-dive
propagated_to: [000660, NVDA, AMD, AVGO, LRCX, AMAT, KLA, ASMI, BESI, TSM, 285A, SNDK]
---

# DRAM & HBM Memory Supercycle — SemiAnalysis "Memory Mania"

## Thesis Delta
Reinforces [[Theses/000660 - SK Hynix]] high conviction with fresh quantified supply-demand: a ~7% structural DRAM deficit persisting through 2027 (vs mid-single-digit at the 2017-18 peak), HBM shortfall widening 5%→6%→9% (2025→2027), and SK Hynix taking ~60% of first-12-month Rubin (R200) HBM share. The new, non-consensus wrinkle: commodity DRAM margins have caught or passed HBM margins (sharpest at Samsung), creating an incentive to slow HBM expansion and milk commodity — which sustains the "dual shortage" but puts Samsung's ~30% Rubin HBM share exactly on SK Hynix's `→ MEDIUM` conviction trigger.

## Summary
SemiAnalysis (Dylan Patel), published 2026-02-06 and ingested 2026-05-31 — the ~16-week lag matters because the near-term 1Q26 pricing calls below are now partially observable against actuals. The argument: the AI-driven memory supercycle is **bigger and longer** than any of the prior four (1993 Windows PC, 2010 mobile+cloud, 2017-18 server, 2020-21 COVID), and unlike them it will not self-correct in one-to-two years because the demand driver — HBM — is itself supply-destroying. The DRAM market is in a "dual-shortage dilemma": both HBM and commodity DRAM run structurally short (HBM 5-9%, commodity ~7%) and compete for the same wafers and cleanrooms, so neither slackens.

The core mechanism is what SemiAnalysis calls **"reverse scaling."** A commodity-DRAM wafer delivers roughly **3× the bit output** of an HBM3E 12-Hi wafer (widening to ~4× at HBM4) because HBM uses larger die (TSV keep-out zones reduce usable array area), demands higher cell performance (lower front-end sort yields), and compounds yield across 8-/12-high stacks (one bad die kills the stack). So every wafer reallocated to HBM both (a) removes commodity DRAM wafers and (b) produces fewer total bits — tightening the entire market even as total wafer capacity grows. HBM's share of the three makers' DRAM wafer capacity climbs from <5% (2022) → ~20% (2025) → ~35% (2027), meaning HBM alone consumes more than a third of combined DRAM wafers. Prior platform inflections (PC, smartphone, cloud) expanded demand *without* materially constraining supply; this one does both at once.

Supply cannot respond near-term. Post-COVID capex caution left a cleanroom shortfall: virtually all 2026 incremental wafer capacity is concentrated in three fabs — Samsung P4, SK Hynix M15X, Micron A3 — and M15X and A3 are HBM-skewed. Meaningful greenfield cleanroom does not arrive until roughly end-2027 (Yongin Phase 1 cleanroom Feb 2027 / output 3Q27; Micron Idaho Fab 1 mid-2027 / output 3Q27; Micron's ex-PSMC P5 Tongluo, ~45k wpm, 2H27). The only near-term bit lever is node migration to 1b/1c (combined 1b+1c capacity +~80% from 4Q25 to 4Q27), giving ~21% industry bit growth in 2026 and ~19% in 2027 — short of demand. Node transitions also impose temporary yield/output dips during ramp.

Competitively, HBM4 is consolidating into a two-player Korean race for NVIDIA. Engineering samples sit below target pin speed (~10 Gbps for both Samsung and SK Hynix; Micron materially lower). SK Hynix retains a signal-integrity / jitter (package-execution) edge and proven reliability; Samsung's 1c front-end is competitive on power and in some cases lower-power than SK Hynix. SemiAnalysis projects R200-class HBM share of ~60% SK Hynix / ~30% Samsung / ~0% Micron in Rubin's first 12 months, with HBM4 crossover in 2H26, HBM3E mix staying higher than consensus, and HBM3E 12-Hi 2026 pricing **flat** (vs consensus ~-15-20%); Samsung, having underpriced HBM3E in 2025, can take +10-15%. The non-consensus twist sits on the commodity side: commodity DRAM margins are now on par with or above HBM margins (most so at Samsung, whose HBM economics are weaker), so suppliers who doubt their HBM4 share — Samsung above all — have a rational incentive to balance HBM expansion against high-margin commodity, which self-reinforces the dual shortage. Downstream, "memoryflation" pressures OEM margins (Apple ~15% vs ~20% industry memory cost rise, worse for Tier-1.5/2 Chinese mobile and PCs facing a CPU+DRAM double-hit), and WFE is the cleanest derivative — memory WFE capex +26% / +34% / +20% (Samsung / SK Hynix / Micron) in 2026 with rising EUV layer counts, node migration to 1b/1c confirmed by [[Theses/LRCX - Lam Research]] and ASML management.

## Framework / Mental Model
The piece advances a reusable model of memory cyclicality plus a specific "why this time is different" framework.

**(0) Why memory pricing turned cyclical, not deflationary.** DRAM rode Moore's Law + Dennard scaling for decades on the 1T1C cell (one access transistor, one storage capacitor), with density historically doubling ~every 18 months — faster than logic. That has collapsed: density rose only ~2× over the past decade versus ~100×/decade at peak. Capacitors are now ~100:1-aspect-ratio 3D structures storing only tens of thousands of electrons (a doorknob static shock transfers billions; a dust speck holds ~10,000× a DRAM cell's charge), so bitlines and sense amplifiers — once secondary — are now the binding constraint, and each shrink cuts signal margin and raises cost. With cost-per-bit deflation stalled, DRAM pricing is set by capacity additions and cyclical supply-demand rather than technology-driven cost reduction. The cost curve no longer governs returns — the cycle does. This is the precondition that makes every section below matter.

**(1) The memory-cycle model — recurring components:**
- **Inelastic, lagged supply vs elastic, lumpy demand.** Fabs take years to build; demand fluctuates daily. Utilization swings ~95% (supercycle) to ~50% (deep downcycle).
- **Sunk-cost wafer logic.** Once a fab is built, run wafers as long as price exceeds cash operating cost. Node transitions do not stop when demand weakens, so bit supply keeps growing into gluts — exacerbating downturns.
- **Node migration as the supply lever.** Moving up nodes lifts bits/wafer without new cleanroom (Samsung 1c ≈ +70% bits/wafer vs 1a). This is the lever that historically breaks upcycles.
- **Commoditization → consolidation.** ~20+ DRAM makers (mid-1990s) → mid-teens (2000s) → <10 (2010s) → 3-4 today. Each bust eliminated the under-capitalized (low sales → no cash for next node → worse cost/bit → bankruptcy).
- **Forward-looking investors.** Memory equities peak *before* supplier earnings and margins peak — observed in every cycle for 30 years.
- **Demand inflections.** New computing platforms step-change both unit volume and memory content per system: PC/GUI 1993 (DRAM/PC 1-2MB → 4-8MB, ~4×), smartphone+cloud 2010 (server DRAM single-digit → tens of GB; LPDDR rises and dampens pricing uplift), server 2017-18 (high-ASP server mix), COVID 2020-21 (WFH demand shock + panic double/triple-ordering), and AI now.

**(2) Why this cycle is bigger/longer — three interrelated drivers:**
1. **Accelerating HBM demand + HBM capacity build** — HBM wafer capacity ~5× in four years; HBM content per AI server rising across GPU and ASIC.
2. **HBM-vs-commodity wafer tradeoff** under fixed cleanrooms — the "dual shortage."
3. **Cleanroom scarcity** from post-COVID underinvestment — supply cannot meaningfully respond until ~end-2027.

**(3) "Reverse scaling"** — the distinguishing feature: the demand-driving product (HBM) is more manufacturing-intensive and yields fewer bits/wafer, so demand growth and supply destruction are the *same* event.

**(4) "Dual-shortage dilemma"** — HBM and commodity DRAM compete for identical wafers/cleanrooms; both stay short, so the upcycle lacks the usual self-correcting glut. Re-applicable to any capacity-shared, two-product commodity market with divergent unit economics.

**(5) The HBM / commodity asymmetry** — why makers chase HBM, and why commodity can still out-re-rate it. Suppliers race to HBM for two reasons: it is a structural, sustainable growth engine beyond legacy PC/mobile/auto end-markets (indispensable to both training and inference, with rising content per AI server), and its complex front-end + back-end enables genuine product differentiation (pin speed, power efficiency, thermal, packaging integration) and therefore pricing power — unlike commodity DRAM, where competition is cost/scale. The catch, and the source's key investment insight: HBM's long-term volume commitments give visibility but cap intra-year price increases, whereas commodity DRAM can "re-rate" far faster in a supercycle of this magnitude. That asymmetry is why SemiAnalysis turned bullish on the most commodity-exposed major (Samsung) alongside the HBM leader (SK Hynix) — in a violent up-move, the ability to reprice commodity quarterly can out-earn locked HBM contracts, even though HBM is the superior long-term franchise.

## Evidence

**Supply-demand imbalance (SemiAnalysis Memory Model):**
| Metric | 2025 | 2026E | 2027E |
|---|---|---|---|
| Total DRAM supply vs demand | — | ~7% below demand | ~7% below (commodity) |
| HBM shortfall | ~5% | ~6% | ~9% |
| Commodity DRAM deficit | — | ~7% | ~7% |

Context: the 2017-18 supercycle gap was only ~mid-single-digit — current imbalance is wider and longer.

**HBM wafer capacity, 3 makers (kwspm):**
| End-2023 | End-2025 | End-2026E | End-2027E |
|---|---|---|---|
| ~123 | ~331 (2.7×) | ~473 | ~668 |

→ ~5× in four years; >2× again 2025→2027.

**HBM as % of total DRAM wafer capacity (Samsung + SK Hynix + Micron):**
| 2022 | 2025 | 2027E |
|---|---|---|
| <5% | ~20% | ~35% |

**Bit-output penalty:** commodity wafer ≈ 3× the bits of an HBM3E 12-Hi wafer; ≈ 4× at HBM4 (more at HBM4E). Industry bit growth ~21% (2026), ~19% (2027). Combined 1b+1c capacity +~80% (4Q25→4Q27); Samsung & SK Hynix targeting ~30% of DRAM wafers on 1c by end-2026, Micron ~30% on 1c/1γ. Node migration carries execution friction — new tool installs, process-window re-optimization, and yield deterioration during ramp — so effective wafer capacity and bit output at transitioning fabs typically *dip for several quarters* before recovering, a near-term tightener layered on top of the structural one.

**DRAM pricing (SemiAnalysis model):**
| Product | 1Q26 QoQ contract | 1Q26 YoY | ~Price exit-1Q26 |
|---|---|---|---|
| DDR5 | +70% | +638% | ~$14/GB |
| LPDDR5 | +35% | +369% | ~$11.5/GB |

Further ~2× potential on a 4Q25 vs 4Q26 basis. Historical down-leg reference (2010 analogue): DDR3 2Gb fell ~46% from ~$46.5 (1H10 peak) to ~$25 by Nov 2010.

**HBM4 competitive landscape:**
| Supplier | HBM4 sample pin speed | R200 HBM share (first 12mo) | Notes |
|---|---|---|---|
| [[Theses/000660 - SK Hynix]] | ~10 Gbps | ~60% | SI/jitter lead, proven reliability |
| Samsung | ~10 Gbps | ~30% | 1c front-end competitive on power; underpriced HBM3E in '25 → +10-15% achievable '26 |
| Micron | much lower | ~0% | execution skepticism on NVIDIA pin speed |

HBM3E 12-Hi 2026 pricing: consensus ~-15-20% → SemiAnalysis **flat**. HBM4 crossover 2H26; HBM3E mix higher than initially forecast.

**Memory WFE capex, 2026 YoY:**
| Samsung | SK Hynix | Micron |
|---|---|---|
| +26% | +34% | +20% |

Drivers: HBM capacity, 1b/1c migration (higher EUV layer intensity), 2027 fab build-outs. All three lift EUV layer counts; SK Hynix 1γ EUV spend to decelerate later via MOR adoption (throughput per tool up without ASML upgrade) — still a net increase. Beneficiaries span EUV (ASML), front-end ([[Theses/AMAT - Applied Materials]], [[Theses/LRCX - Lam Research]], [[Theses/ASMI - ASM International]], [[Theses/KLA - KLA Corporation]]) and HBM back-end packaging / TC bonders ([[Theses/BESI - BE Semiconductor Industries]]). 2026 incremental capacity concentrated in Samsung P4, SK Hynix M15X, Micron A3 (M15X & A3 HBM-skewed); [[Theses/TSM - Taiwan Semiconductor]]'s higher-than-expected 2026 capex already priced some of the logic side.

**EUV adoption path (DRAM):** EUV first replaces DUV multipatterning in the congested region where access transistors meet storage capacitors — storage-node (buried) contact, bitline cut (the tight tip-to-tip gap between bitline ends), and bitline contact — mirroring 7nm logic, where the tightest-pitch via layers adopted EUV first. DRAM EUV intensity rises sharply near-term as makers rush to convert capacity to EUV-heavy 1b/1c processes; longer term SK Hynix's 1γ keeps adding EUV layers but spend decelerates via MOR (multiple-exposure-on-resist / metal-oxide-resist throughput gains that raise output per tool without paying ASML for an upgrade) and the 6F² architecture nears its scaling limits. A slower increase is still an increase — net positive for ASML and for EUV-layer-count exposure across the WFE complex.

**Capacity timing / fab pull-ins:** SK Hynix pulled in both M15X and Yongin Phase 1; Micron pulled Idaho Fab 1 from 2H27 to mid-2027; the ex-PSMC P5 Tongluo fab adds up to ~45k wpm (output 2H27, lower if HBM-configured given TC-bonder cleanroom needs). Samsung P4 Phase 4 arrives late-2026 (after fully-equipped Phase 1/Phase 3), with P4 Phase 2 possibly pulled into 1H27. Net: material new wafer/bit output is back-half-2027-weighted — the supply response lags the shortage by ~18+ months, the structural reason the deficit persists.

**AI memory content step-ups (demand side):**
| Platform | Memory step |
|---|---|
| NVIDIA Blackwell → Blackwell Ultra → Rubin | HBM capacity +~50%; Rubin Ultra system memory 288 GB → ~1 TB (~4×) |
| AMD MI350 → MI400 | ~288 GB → ~432 GB |
| Google TPU v8AX, Amazon Trainium3 | HBM3E 8-Hi → 12-Hi |

HBM alone >10% of total DRAM demand by end-2027; servers ~40% of the DRAM end market and rising; rising LPDDR5-based server products (SOCAMM / SOCAMM2) add further server DRAM content. Demand-side consumers: [[Theses/NVDA - Nvidia]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]] (Google TPU / custom-ASIC HBM).

**"Memoryflation" / OEM exposure:**
| Segment | Memory cost impact | Note |
|---|---|---|
| Apple | ~15% | best procurement leverage; larger hit 2H26 |
| Industry (broad) | ~20% | limited ASP offset to date |
| Tier-1.5/2 Chinese mobile | worst | weak pass-through → spec downgrades |
| PCs | double-hit | + processor price rises; spec cuts since 4Q25 |

PCs + mobile ≈ 30% of DRAM demand (watch elasticity / shipment cuts into 2026); server strength (~40%, rising) is expected to more than offset consumer softness.

**Historical supercycle analogues (every prior peak rolled within 1-2 years):**
| Cycle | Demand trigger | Content / supply setup | Peak → rollover |
|---|---|---|---|
| 1993 Windows PC | GUI shift; PC units +double-digit | DRAM/PC 1-2MB → 4-8MB (~4×); supply lean post-1980s shakeout | GMs >50% on 4Mb/16Mb; capex >30% of semi production, ~50 fab plans '95-96 → oversupply '95-96, prices -60%+, consolidation |
| 2010 mobile + cloud | iPhone/Android + early hyperscaler buildout | server DRAM single-digit → tens of GB; supply muted post-GFC cuts | LPDDR rise dampened uplift; LPDDR2 JEDEC-standardized '09 → faster commoditization; DDR3 2Gb -46% ($46.5 → $25, 1H10 → Nov '10) |
| 2017-18 server | virtualization, scale-out, memory-heavy workloads | higher server DRAM content + ASP/margin | record FCF, GMs at new highs, peak 2H18 → supply re-accel + demand normalize late-'18/'19 |
| 2020-21 COVID | WFH / education / cloud demand shock | double/triple-ordering masked true demand; supply constrained (labor, logistics, equipment) | peaked 2021; reset behavior → capex discipline, node-migration over greenfield, margin-over-bits |

The COVID reset is load-bearing for the current cycle: it pushed suppliers toward capex discipline, tighter inventory, and prioritizing high-margin product over pure bit growth, and pushed customers to treat memory capacity as strategic — together manufacturing the structurally tighter supply base the AI cycle now exploits. The reusable lesson is that prior peaks arrived when supply re-accelerated (capacity + node migration) *and* demand normalized (inventory digestion) at the same time. **Peak-prediction checklist for the current cycle:** (1) greenfield cleanroom coming online (~end-2027); (2) 1b/1c node-migration bit growth outrunning demand; (3) HBM or commodity demand normalization / hyperscaler inventory digestion; (4) memory equities rolling over ahead of the earnings print — investors lead the peak in every cycle, so price action is the early tell, not the lagging fundamentals.

## Contradiction Check
- **Supports** [[Theses/000660 - SK Hynix]] high conviction. Bigger/longer cycle, ~60% Rubin share, and the HBM4 signal-integrity lead reinforce non-consensus insights #2 (supply discipline + HBM wafer-intensity) and #3 (HBM4 widens the moat). Affected assumption — durability of HBM tightness — strengthened.
- **Yellow flag on the SK Hynix `→ MEDIUM` trigger.** That trigger reads: "Samsung qualifies HBM4 at NVIDIA AND takes >30% Rubin HBM share." SemiAnalysis puts Samsung at **~30%** of first-12-month R200 HBM — exactly at the threshold, not yet through it, but narrowing. Monitor Samsung HBM4 qualification + Rubin allocation as the single most trigger-relevant datapoint; affected assumption is SK Hynix's >50% HBM-share durability.
- **Partial tension with non-consensus insight #1** ("HBM is not commodity DRAM" / HBM margin premium). The article says commodity DRAM margins now equal or exceed HBM margins (sharpest at Samsung). The premium narrows — not because HBM weakened but because commodity re-rated. Net positive for SK Hynix earnings (the "second margin lever" is bigger than modeled), but it weakens the specific *HBM-commands-structurally-higher-margin* framing and reduces some suppliers' urgency to grab HBM share — which paradoxically protects SK Hynix's HBM position (Samsung milking commodity).
- **Cost headwind for memory consumers.** Memoryflation is a BoM/TCO drag for [[Theses/NVDA - Nvidia]] / [[Theses/AMD - Advanced Micro Devices]] AI servers and a margin risk for consumer-exposed names; ties to [[AI Bubble Risk and Semiconductor Valuations]] (rising AI-server memory cost → TCO / ROI scrutiny).
- **No-thesis names discussed.** Micron (MU), Samsung, and ASML are central to the analysis but have no vault thesis — candidates for coverage given the WFE/EUV and #3-DRAM-maker exposure.
- **Staleness caveat.** Published 2026-02-06; the 1Q26 +70% DDR5 / +638% YoY figures are now (end-May) checkable against actuals — verify before treating the forward "~2× on 4Q26" call as live.

## Source Excerpts
- "A wafer dedicated to commodity DRAM typically delivers roughly 3× the bit output of a wafer dedicated to HBM in the case of HBM3E 12-Hi… likely to widen to nearly 4× as the industry transitions to HBM4."
- "HBM wafer capacity as a share of total DRAM wafer capacity at Samsung, SK hynix, and Micron was below 5% in 2022, but has already increased to approximately 20% by year-end 2025. By the end of 2027, we estimate this figure will reach ~35%."
- "We model 1Q26 QoQ contract price increases of 70% for DDR5 and 35% for LPDDR5… YoY price increases of 638% for DDR5 and 369% for LPDDR5."
- "Commodity DRAM margins are now on par with—or in many cases exceeding—HBM margins since late 4Q… This is particularly the case for Samsung."
- "For R200-class HBM supply, we envision SK hynix capturing approximately ~60% share, followed by Samsung at ~30%, with Micron accounting for none in the first 12 months of Rubin."
- "DRAM WFE capex will increase by roughly 26%, 34%, and 20% for Samsung, SK hynix, and Micron, respectively, in 2026."
