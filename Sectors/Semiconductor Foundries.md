---
date: 2026-04-22
tags: [sector, moc]
status: active
---

# Semiconductor Foundries

## Active Theses
- [[Theses/TSM - Taiwan Semiconductor]] — Taiwan Semiconductor (leading-edge foundry monopoly / 92% ≤7nm share / N2 +20% premium / Taiwan-tail risk materially higher than thesis-modeled)

## Key industry questions
1. Does leading-edge become a durable monopoly or a 2-of-3 oligopoly by 2028? TSMC is 70.2% of total foundry revenue (Q2 2025) and ~92% of ≤7nm wafers; Samsung (7.3%) and Intel (~2%) each need ONE external anchor at N2-class to matter. Tesla AI6 ($16.5B on Samsung Taylor 2nm, through 2033) and AWS AI Fabric + Microsoft on Intel 18A are the binary validation tests already in play.
2. Is the 2nm-era ~+50% wafer-cost step (N3 ~$20K → N2 ~$30K) absorbed by end-customer ASPs or compressed into design-cycle delays? Apple holds ≥50% of 2026-2027 N2 allocation; NVDA pre-booked A16 exclusively; the marginal ASIC customer is re-qualifying on Samsung or skipping a node.
3. Does advanced packaging (CoWoS, Foveros, I-Cube) become the new pinch-point replacing logic wafers as the leading-edge constraint? TSMC CoWoS scaling 35K → 75K → 130K wpm (2024 → 2026 → 2027), 100% in Taiwan (Kaohsiung + Chunan), is the single largest foundry capex bucket shift of this cycle.
4. Can Intel Foundry survive operationally separate from Intel Products at 14A? Anchor wins (AWS + Microsoft on 18A, Google likely to follow) prove technical viability; break-even needs 2+ 14A customers with committed volume; two early 14A prospects exist with zero commitments.
5. Does Rapidus' IBM-tech 2nm Chitose pilot convert to credible small-batch foundry in 2027-2028 and split US/JP customers from TSMC? ¥267.6B first-round funding plus $4B METI commitment; IIM-1 cleanroom activated mid-2025; PDK release 2H 2026; mass-production target end-2027.
6. How permanent is the China-domestic foundry split? SMIC targeting 5x total 7nm/5nm output by 2027; Ascend 950PR shipped Q1 2026 on SMIC N+2 at 15-46% yield; Huawei Atlas 950DT SuperCluster (524 EFLOPS FP8) is the first non-NVDA + non-TSMC hyperscale AI architecture. Separate-supply-chain permanence removes a ~$40-50B AI-compute bucket from TSMC.
7. Is the mature-node (≥22nm) segment entering a 2026-2027 "volume up, prices down" reset as TSMC recycles mature capacity toward advanced while UMC/VIS/PSMC/Nexchip price-compete on excess? UMC is hiking 2H26 list prices +5-10% while cutting supplier contracts 15% — divergent signals point to supply/demand mismatch.
8. Does High-NA EUV ($380-400M per scanner) adoption by Intel (14A) and Samsung (SF1.4) leapfrog TSMC's multi-patterning posture at A14? TSMC has explicitly stated it will not use High-NA at 1.4nm. The TSMC ROI-first bet is consensus; a Samsung/Intel process-lead swap would be the largest foundry realignment in 20 years.
9. How is the Taiwan concentration tail priced — as a ~15% discount (consensus) or as an 85-95% permanent-impairment binary (per [[Research/2026-04-19 - TSM - Stress Test]])? Arizona is 5-8% of total capacity through 2030; EUV replication elsewhere consumes 100% of ASML global output for 12-18mo.

## Industry history

**1987: Morris Chang founds TSMC as the world's first pure-play foundry.** Production technology and IP transfer from Philips for 27.6% equity; 48.3% from Taiwan's National Development Fund. The category insight was misaligned incentives — fabless firms would not trust IDMs (Intel, TI, Motorola) with their designs because IDMs competed for the same end markets. Until 1987, "fabless" did not exist as a viable model; by 2024 global fabless revenue exceeded $700B.

**1980s-1990s: the fabless revolution TSMC enabled.** Qualcomm (1985), Xilinx (1984), Altera (1983), Broadcom (1991), NVIDIA (1993), MediaTek (1997) built design-only businesses around contract foundry capacity. Unit economics: $10-50M design capital reached product-market fit vs $10B+ for a greenfield fab. The foundry industry became the infrastructure that made every subsequent chip-design startup possible.

**1994-2005: UMC and IBM as first challengers, both losing to scale.** UMC (founded 1980, pivoted to pure-play 1995) was TSMC's principal rival at 200mm wafers. IBM Microelectronics ran Fishkill as a contract foundry for AMD, Sony, Nintendo. Both lost the transition to 300mm + immersion lithography because TSMC's yield-learning curve at scale was structurally superior and its CapEx discipline (partnered with ASML and AMAT) outran IBM's internal roadmap.

**2005-2014: Samsung enters, AMD spins off GlobalFoundries, IBM exits.** Samsung Electronics began foundry operations in 2005, leveraging memory-manufacturing scale (DRAM/NAND). GlobalFoundries formed March 2009 as AMD manufacturing carve-out (Mubadala + AMD equity), acquired Singapore's Chartered Semiconductor (Sept 2009, $1.8B), then took over IBM Microelectronics in Oct 2014 — deal structured with IBM PAYING GF $1.5B to take the East Fishkill + Essex Junction fabs. AMD divested its final 14% GF stake March 2012.

**2015-2020: three-way race collapses to one.** Intel missed 10nm HVM repeatedly (originally 2016, shipping 2019); Samsung 3nm GAA (2022) yielded poorly and lost NVIDIA HBM qualification; GlobalFoundries publicly exited leading edge August 2018 (canceled 7nm). TSMC reached 80%+ leading-edge share by 2020. The pure-play model plus EUV bet (TSMC took ~70% of ASML's EUV shipments 2018-2022) compounded into structural advantage.

**2020-2023: pandemic + AI inflection.** COVID exposed auto-industry mature-node shortages; the 2022-2023 ChatGPT/GPU capex cycle created structural leading-edge and packaging shortages. TSMC ASP rose ~20% post-pandemic (one-time) plus 3-6% annually thereafter. CoWoS-L became the bottleneck for NVDA Hopper then Blackwell. Foundry moved from cost-optimized global supply chain to strategic national-security asset.

**2024-2026: geopolitical restructuring.** CHIPS Act (Aug 2022, $52B direct funding + $25B ITC) finalized: Intel $7.86B, TSMC $6.6B (later expanded to $165B Arizona commitment + $100B Trump 2025 additional pledge), Samsung $4.75B. Rapidus founded 2022 (Japan METI + IBM 2nm tech license, $4B+ committed). EU Chips Act (Feb 2023) allocated €43B. The industry transitioned from a cost-optimized global supply chain to a subsidized multi-regional oligopoly with margin dilution baked in for a decade.

## Competitive dynamics

**Leading-edge is a de facto monopoly.** Q2 2025 foundry rankings by revenue: TSMC 70.2%, Samsung 7.3%, SMIC 5.1%, UMC 4.4%, GlobalFoundries 3.9%, Hua Hong 2.5%, Vanguard 0.9%, Tower 0.9%, Nexchip 0.8%, Powerchip 0.8%. Leading-edge (≤7nm) concentration tighter still: TSMC ~92%, Samsung ~5%, Intel ~2%, SMIC ~1% (Chinese-domestic only).

**Yield divergence is the binary gating variable.** TSMC N2 reported 90%+ at mature and 65-80% at ramp phases; Samsung SF2 climbed 30% → 50% → 55-60% through 2025, remains below the 65-70% survival threshold; SMIC N+2 runs 15-46% across Huawei Kirin 9030 and Ascend 910C; Intel 18A improving ~7%/month, entering 2026 at reported 65-75%. Yield directly drives the gross-margin gap — TSMC 58.8% Q1 2026 vs Samsung Foundry reported losses.

**Customer-lock-in is asymmetric and anchor-customer-driven.** Apple takes ≥50% of N2 allocation 2026-2027 and treats TSMC as sole foundry. NVDA took A16 exclusivity for Feynman (2027). Samsung won Tesla AI6 ($16.5B, through 2033) plus AMD EPYC Venice dual-foundry talks. Intel 18A locked AWS AI Fabric (multi-billion) plus Microsoft. Each non-TSMC leading-edge foundry survives on 1-2 anchor customers, not a diversified book — which means any single anchor loss is existential.

**Pricing power is now nakedly divergent.** TSMC N2 prices at ~$30K/wafer (+~50% vs N3 ~$20K); full 2026 price hikes 5-10% across advanced nodes announced. Samsung undercut TSMC 2nm pricing to ~$20K (33% discount) to buy customer re-qualification trials. UMC + VIS + PSMC + Nexchip raising 2H26 mature-node quotes +5-10% while selectively cutting supplier contracts −15% — mature pricing discipline is collapsing because TSMC is redirecting mature capacity to advanced, leaving mature foundries with incremental supply chasing normalizing auto/IoT demand.

**Advanced packaging has become a second foundry franchise.** TSMC CoWoS scaling 35K → 75K → 130K wpm (2024 → 2026 → 2027), >50% of 2026 CoWoS pre-booked by NVDA at +20% pricing. Intel Foveros / EMIB capacity scaling +150% / +30% in New Mexico; Intel has confirmed some customer designs have ported from CoWoS to Foveros without modification. Samsung I-Cube in volume ramp targeting NVDA as secondary partner. OSATs (ASE VIPack, Amkor, SPIL) absorb lower-end InFO and overflow. Packaging capacity is now the 2021-equivalent of leading-edge wafer capacity as the binding AI-supply constraint.

**Geographic diversification is aspirational at leading edge through 2028.** TSMC Arizona Fab 21 (N4) reached yield parity with Taiwan in ~2 quarters (2025); Fab 22 (N2) first-wafer 2027-2028; A16 in Arizona 2029+. Arizona is 5-8% of total capacity at 2030 full-ramp. Samsung Taylor 2nm delayed to late 2026 (skipping originally planned N4 lines). Intel Ohio Fab 52 delayed from 2025 to 2030. Leading-edge through 2028 is >95% Taiwan-physical regardless of accounting-share redistribution.

## Product level analysis

### TSMC — the reference foundry node stack

| Node | Status 2026 | Use case | Revenue share Q1 2026 |
|---|---|---|---|
| N5/N4/N4P family | Mature HVM, workhorse | AAPL A-series 2020-2024, NVDA Hopper/Ada, AMD Zen 4/5 | 36% |
| N3/N3E/N3P | HVM | AAPL M5/A18 Pro, NVDA Blackwell, AMD Zen 5/Turin | 25% |
| N2 | HVM Q4 2025, ramping | AAPL M-series 2026, AMD EPYC 2026, AI accelerators | 1-3% (→35%+ by 2028) |
| N2P | 2026 refresh | Backside-power preview | — |
| A16 | Late 2026 HVM | Super Power Rail backside; NVDA Feynman exclusive | — |
| A14 / A14P | 2028-2029 | CFET-rumored next-gen transistor | — |
| N7/N7P/N6 | Mature HVM | Prior-gen AI, networking | 13% |
| 16/28/mature | Declining share | Auto, IoT, industrial | ~17% |

**Advanced packaging**: CoWoS-S (silicon interposer, HBM-adjacent GPU logic — NVDA H100/H200/B200), CoWoS-L (large interposer, 8-stack HBM — NVDA B300/Rubin, AMD MI325X), SoIC-X (hybrid bonding, 3D stacking — AAPL M5, NVDA Rubin Ultra, AMD 3D V-Cache), InFO (lower-cost fan-out for phones/edge), COUPE (Compact Universal Photonic Engine — AMD risk production Feb 2026).

### Samsung — SF2 and SF1.4 gate-all-around

SF2 (2nm GAA) entered mass production Q4 2025. Anchor products: Exynos 2600 (consumer phone), Tesla AI6 (2028 first-in-vehicle, $16.5B through 2033, Taylor TX), AMD EPYC Venice (negotiation). SF1.4 (1.4nm "SF2X") in development with High-NA EUV. Yield trajectory 55-60% (Nov 2025) → 65-70% target end-2026 = survival threshold. Wafer pricing ~$20K (−33% vs TSMC N2) to buy re-qualification trials. Samsung unique advantage: introduced GAA at 3nm (2022), so institutional learning curve on GAA exceeds TSMC's; disadvantage: 3nm yield failures cost the company NVIDIA HBM qualification from 2023-2025.

### Intel Foundry — 18A to 14A

Intel 18A (1.8nm-class, RibbonFET + PowerVia backside power) in HVM at Fab 52 Arizona. Lead products: Panther Lake (client), Clearwater Forest (server). External anchors: Microsoft (committed), AWS AI Fabric (multi-billion, ramping 2026), Google ("likely to follow" per Semicone reporting). 18A-P variant in development for external-foundry customers. Intel 14A targeted 2028-2029 HVM with 2 early customer prospects (PDK distributed, zero committed volume). 14A is Intel's High-NA EUV bet vs TSMC's multi-patterning A14. Capex 2026 flat to down from $17.7B 2025 under Lip-Bu Tan's CapEx discipline.

### SMIC — DUV multi-patterning at sub-7nm

N+2 (7nm-class, LELELE multipatterning on DUV) in volume at Shanghai + Beijing fabs; fabricates Huawei Kirin 9030 + Ascend 910C. 5nm pilot running, HVM target 2026 for Huawei and Alibaba AI accelerators. Yields 46% (Kirin) to 15-36% (5nm prototypes). Capacity target: 5x 7nm+5nm output over 2 years per China-domestic self-sufficiency mandate. DUV multi-patterning extends toward 5nm/3nm at yield and cost penalty that only works with state-subsidized CapEx and guaranteed domestic-customer offtake.

### GlobalFoundries — Foundry 2.0 specialty

Strategy: 12nm and above, differentiated platforms (FDX, RF-SOI, SiGe, BCD, integrated transceivers). Q4 2025 revenue $1.83B at 29.0% gross margin (vs TSMC 58.8%). Anchor customers: Infineon, NXP, Bosch, Aumovio under long-term automotive-supply agreements. 7nm canceled 2018; GF is the largest pure-mature Western foundry. Revenue CAGR modeled high-single-digit to low-double-digit through 2026-2027 as auto / industrial / connectivity demand normalizes.

### UMC — 22/28nm + Singapore expansion

Most advanced process 22/28nm. Q2 2025: 22/28nm = 40% of wafer revenue (up from 37% Q1), 40nm = 15%. New Singapore Fab 12i expansion (22/28nm, production 2026) the strategic response to mature-node geographic redistribution. Q2 2025 foundry share 4.4%, #4 globally. 2H26 price hikes announced against "volume up, prices down" sector backdrop — profitability defense through price.

### Rapidus — IBM-licensed 2nm, pilot 2026 → HVM end-2027

IIM-1 Chitose (Hokkaido): cleanroom activated mid-2025; EUV installed; 2nm GAA test wafers running; PDK release 2H 2026. Business model: small-volume, fast-cycle foundry for customers iterating chip designs — value proposition is cycle time, not capacity. Funding: ¥267.6B (~$1.7B) first round + $4B METI 2026 additional commitment. More than 150 Rapidus engineers trained at IBM Albany 2023-2024. The only credible new leading-edge entrant globally since 2010.

### VIS, PSMC, Hua Hong, Nexchip, Tower — specialty tier

- **Vanguard (VIS)**: 8-inch mature, TSMC+Philips JV legacy; Q2 2025 share 0.9%.
- **Powerchip (PSMC)**: legacy DRAM foundry pivoting to image sensors + auto; Q2 2025 share 0.8%.
- **Hua Hong**: Shanghai mature foundry for China-domestic auto/IoT; Q2 2025 share 2.5%; beneficiary of China's 5x 7nm+5nm expansion mandate.
- **Nexchip**: fastest-growing China mature foundry; Q2 2025 share 0.8%.
- **Tower Semiconductor**: Israeli specialty foundry (SiGe, BiCMOS, SOI, RF-CMOS, CMOS image sensors, BCD, MEMS); 2025 revenue $1.57B (+9% YoY); $18.4B market cap (~3.4x the $5.4B Intel offered pre-2023 acquisition collapse). Post-failed-merger, Intel/Tower 300mm New Mexico deal also terminated in 2026, with arbitration ongoing.

## Acquisitions and new entrants

**GlobalFoundries formation (2009-2015) — the defining foundry-industry roll-up.** AMD manufacturing → GF (Mar 2009, Mubadala-funded); GF + Chartered Semiconductor (Sept 2009, $1.8B); GF + IBM Microelectronics (Oct 2014 → Jul 2015 close, IBM paid GF $1.5B to take on East Fishkill 300mm + Essex Junction 200mm); GF → ON Semiconductor sale of Fishkill (Apr 2019, $430M). Net effect: consolidated four substandard leading-edge efforts (AMD + Chartered + IBM + later IBM-Sony-Toshiba co-dev) into one mature-specialty platform, clearing the leading-edge field for TSMC and Samsung.

**Intel-Tower acquisition failure (Feb 2022 announced → Aug 2023 terminated).** Intel agreed $5.4B to acquire Tower to accelerate specialty-foundry buildout; China's SAMR refused to approve; Intel paid $353M termination fee. Subsequent Intel/Tower $300M 2023 New Mexico manufacturing-services agreement also cancelled in 2026 — both parties now in arbitration. Tower compounded to $18.4B standalone market cap. The failure is the foundry industry's clearest proof of specialty-foundry scarcity value + export-regulatory-regime control points over M&A.

**Foundry-adjacent equipment consolidation.** Applied Materials took 9% equity in BESI (April 2025) to co-develop the Kinex hybrid-bonding platform — the first equipment-maker integration since AMAT/Varian (2011). Lam Research signaled parallel interest. Marvell's $10B InPhi acquisition (2020) pulled optical-interconnect IP into the hyperscaler ASIC stack. Coherent absorbed II-VI + Finisar ($7B) to consolidate EMLs. The pattern: consolidation concentrated at the equipment and IP layer, not at the foundry layer — structural capital concentration favoring TSMC's customer-facing position.

**New entrants to watch.**
- **Rapidus** — only credible Western leading-edge entrant since 2010; IBM-tech-licensed, Japan state-backed, 2nm pilot running.
- **Huawei (vertically integrated new entrant)** — Ascend chip designs fabbed at SMIC with in-house HBM planning; 1.6M dies target 2026; 750K units of Ascend 950PR shipping Q1 2026; ByteDance $5.6B committed order; Atlas 950DT SuperCluster (520,000+ chips, 524 EFLOPS FP8) Q4 2026. IDM-like model, structurally separate from fabless-foundry market.
- **China-domestic parallel ecosystem** — SMIC 5x capacity expansion + Hua Hong + Nexchip + CXMT (memory). Represents a parallel-universe supply chain, not a new entrant into the Western customer market. Addressable TAM lost to TSMC: ~$40-50B annual by 2027.

**Failed or stalled new entries.** Apple's rumored in-house 2nm fab (2020-2022 reports): never materialized once TSMC relationship quality + scaling CapEx eliminated incentive. Amazon's foundry rumor (2023): never credible; AWS instead selected Intel 18A. MediaTek rumored Samsung-Foundry-ownership talks (2024): abandoned. Pattern: at >$40B CapEx per leading-edge fab cluster, only states and incumbent foundries can fund greenfield competition.

## Macro shifts

**Export controls are now structural, not cyclical.** Oct 2022 BIS rules + Oct 2023 expansion + Trump 2025 tightening created a hard bifurcation: EUV embargo to China (no ASML NXE/EXE deliveries); US-origin EDA tools blocked; 14nm+ wafer production for blacklisted entities prohibited; hyperscaler AI chip exports constrained. TSMC Chinese revenue capped ~6% and declining; Samsung's constrained; Huawei Ascend 100% SMIC-fabbed. The Chinese foundry ecosystem (SMIC + Hua Hong + Nexchip) operates DUV multi-patterning on domestic SMEE/Naura tools in a parallel supply chain. This split is policy-locked for a decade-plus horizon.

**AI capex is the foundry demand cycle.** Hyperscaler 2026 aggregate capex ~$400-450B (Microsoft, Google, Meta, Amazon, Oracle, xAI), majority directed at AI silicon. TSMC 2026 revenue guide $116-120B (+30% YoY) with ~40% AI. Q1 2026 HPC platform was 59% of TSMC revenue vs 41% Q1 2023. The foundry industry has been absorbed into the AI infrastructure cycle: (i) 2027-2028 AI capex deceleration hits foundries first via utilization, then pricing; (ii) the customer base has narrowed from ~30 meaningful clients to ~8 hyperscalers + AAPL. See [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]] for Jensen's own CEO testimony that supply-chain depth + annual cadence, not CUDA, is the primary moat.

**CHIPS Act geographic redistribution is capex-positive but margin-dilutive.** Commitments: TSMC Arizona $165B (6 fabs + 2 advanced-packaging + 1 R&D), Intel $100B US, Samsung $40B Texas (Taylor), Rapidus $4B+ Japan. Industry capex 2026 ~$200B (+20% YoY); WFE 2026 ~$122B (+10%). US and Japan fab cost disadvantage is structurally 10-15% above Taiwan (labor, energy, supply-chain integration). TSMC Arizona margin dilution modeled at 2-3pts by 2030 is the canonical metric. Samsung's Taylor subsidy cuts (Dec 2025) + Intel Ohio delay to 2030 signal CHIPS-Act reality is bumpier than subsidy announcements suggested.

**Taiwan concentration tail is the industry's single unpriced macro variable.** TSMC: 92% of leading-edge wafers, 100% of CoWoS, ~95% of advanced-packaging output — all in a ~100-mile Taiwan Strait window. Per [[Research/2026-04-19 - TSM - Stress Test]]: Arizona is 5-8% of total capacity through 2030; full EUV fleet replication elsewhere consumes 100% of ASML global output for 12-18 months; "destroy the fabs" is documented US Commerce contingency (Bloomberg Mar 2023, former NSA O'Brien on-record). Realistic downside under invasion/destruction: 85-95% permanent impairment vs the ~15% Taiwan-risk discount embedded in TSM's 22x multiple. Joint Sword 2024 rehearsed encirclement; Taiwan's 14-day crude reserves + 97% energy-import dependence mean a 60-90-day blockade produces $100B+ TSMC revenue loss plus permanent customer transfer to Samsung/Intel. This is a thesis risk for every foundry-exposed long position, not a position risk.

**High-NA EUV adoption split is a technology-macro event.** ASML High-NA scanners at $380-400M each. Intel deployed Twinscan EXE:5200B (Dec 2024) for 14A development. Samsung received first High-NA unit late 2025, second H1 2026, deploying on 2nm / SF1.4. TSMC has stated it will not use High-NA at 2nm, A16, or 1.4nm — extending current-gen EUV with multi-patterning. If Intel/Samsung achieve cost-competitive 14A/SF1.4 ahead of TSMC A14, the 8-year TSMC node-leadership window compresses for the first time since 2018. Consensus bet is TSMC ROI-first posture is correct; the alternative is unpriced.

**Mature-node pricing reset (2026-2027).** TSMC has recycled mature capacity toward advanced (shrinking mature supply), while UMC/VIS/PSMC/Nexchip/Hua Hong expanded 2022-2024 on expected auto/IoT demand. Auto semiconductor inventory now normalizing → mature supply glut. Trendforce forecast: mature pricing enters "volume up, prices down" through 2026-2027. UMC 2H26 hikes + 15% supplier price cuts + PSMC / VIS pricing plans are inconsistent signals from a sector reaching pricing-discipline breakdown. GF Foundry 2.0 specialty-pivot is the pre-positioned defensive strategy.

## Investor heuristics

**Consensus framing: TSMC is a capex-cyclical with monopoly-adjacent margins.** Sell-side models TSMC at ~22x NTM earnings vs 25-35x for monopoly-analogue comparables (ASML 35x, LVMH 25x, Visa 28x). The embedded discount attributes ~10-15% to customer concentration (AAPL + NVDA = 40% revenue) and ~10-15% to Taiwan risk. The framing is internally inconsistent: a de facto monopoly on ~$250B of AI accelerator BOM through 2028 does not cycle with WFE.

**Where consensus is likely wrong (non-consensus insights):**

1. **Advanced packaging is a separable, re-rateable franchise.** CoWoS + SoIC + COUPE approaching ~15% of TSMC revenue by 2027 at 55-60% gross margin, NVDA paying +20% pricing. Reported separately, the packaging franchise would deserve 35-40x forward earnings as a monopoly, tools-adjacent business. Consensus models it as wafer revenue — compressed to the TSMC blended multiple.

2. **Taiwan risk is mispriced as position risk, not thesis risk.** [[Research/2026-04-19 - TSM - Stress Test]] quantifies realistic downside at -85-95% permanent impairment under invasion or destruction scenarios — not the ~-30% embedded in bear cases. Arizona is 5-8% of capacity through 2030; "silicon shield" theory fails the Ukraine-precedent stress test; US defense of Taiwan is not an Article-5-equivalent treaty; Xi's 2027 PLA readiness deadline coincides with current bull-case horizons. The embedded Taiwan discount is too narrow for a 2027-2028 horizon.

3. **Intel Foundry equity optionality is over-priced relative to capacity economics.** Intel 18A yields and AWS + Microsoft anchors suggest technical viability. Break-even requires 20K+ wpm external volume through 2028, and the Fab 52 Arizona + Ohio timeline does not support that scale. Most-probable outcome: Intel Foundry as niche second-source (AWS ASIC, Microsoft ASIC, US government / defense) rather than credible leading-edge scale alternative.

4. **Samsung Foundry is priced as memory + foundry optionality; both segments are margin-challenged.** Samsung Foundry reports losses; memory HBM market share fell 41% → 17% (Q2 2024 → Q2 2025) post-NVIDIA qualification failures. Tesla AI6 is a 2028 revenue event, not a 2026-2027 one. Samsung's foundry business alone is worth <$20B enterprise value on standalone yield trajectory; the parent trades as if 2nm GAA leadership is worth materially more.

5. **Mature-node foundries face asymmetric 2026-2027 earnings risk.** UMC, VIS, PSMC, GlobalFoundries priced as "non-AI beneficiaries" at 12-15x earnings. 2026 "volume up, prices down" reset + TSMC continued mature-capacity migration implies 2027 EPS revisions down 15-25%. GF's specialty-auto focus is defensive but not immune to the broader mature-node repricing.

6. **Rapidus is an out-of-the-money option not in consensus.** If 2nm pilot converts to small-volume HVM end-2027 with credible US/JP anchor customers (Intel-adjacent sovereign compute, Tenstorrent-class startups, small-volume defense), Rapidus creates the first leading-edge alternative TSMC has faced since Samsung's 2005 entry. Probability <30% but completely unpriced.

7. **Per Jensen's own testimony, the supply-chain depth is structurally not replicable.** [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]] — NVDA has ~$100B in explicit upstream commitments, CEO-to-CEO allocation with Morris Chang / C.C. Wei, co-developed silicon photonics ecosystem (Lumentum, Coherent, TSMC COUPE licensing). The TSMC-NVDA relationship is not a supplier-customer contract — it is infrastructural. Any ASIC challenger (Google TPU, Amazon Trainium, Microsoft Maia) has to recreate this across 20+ upstream suppliers without CEO-level pre-commitment.

8. **"No second" logic-leader thesis is structurally robust but financially fragile.** TSMC's dominance is real; the fragility is that the entire AI infrastructure buildout rests on one company's Taiwan operations. Portfolio implication: any long-foundry exposure needs a paired Taiwan-event hedge (long defense LMT/NOC, long INTC call spreads as US-based foundry optionality, or outright put premium on TSM).

## Related Research

### Vault research (sector-relevant)
- [[Research/2026-04-19 - TSM - Stress Test]] — Taiwan invasion / blockade stress test; 8/9 bull-case assumptions rated 🔴; realistic downside -85-95% permanent impairment; drives the Taiwan-tail mispricing insight
- [[Research/2026-04-10 - Hybrid Bonding and BESI Revenue Impact]] — CoWoS / SoIC packaging ecosystem; BESI / EVG / ASMPT hybrid-bonding supply chain; relevant to TSMC advanced-packaging franchise economics
- [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]] — NVDA CEO testimony on foundry dependencies ($100B upstream commitments), supply-chain swarming, ASIC margin spread (65% vs 70%), China compute-sufficiency admission
- [[Research/2026-04-19 - Huawei Ascend Roadmap - news]] — Huawei Ascend 950PR/950DT/960/970 roadmap fabbed at SMIC with in-house HBM; quantifies the ~$40-50B China-domestic bucket structurally lost to TSMC

### Macro linkage
- [[AI Bubble Risk and Semiconductor Valuations]] — AI capex cycle is the demand driver for foundry advanced-node / advanced-packaging pricing power
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] — SemiAnalysis projects TSMC 2028 capex ~$100B; "good people" single-digit pricing discipline is both durability signal and hidden option value
- [[Research/2026-04-24 - Iran War Japan Semiconductor Photo Materials Shortage - news]] — Japanese PR/BARC supply chain risk to leading-edge foundry EUV lithography; TSM less exposed than Samsung/Hynix per Taiwan/Korean localization status

### Related sectors
- [[Sectors/Semiconductor Capital Equipment]] — WFE demand is a derivative of foundry CapEx; shared customer-concentration tail risk
- [[Sectors/GPU & AI Compute Accelerators]] — NVDA + AMD foundry dependency is the largest single leading-edge demand bucket
- [[Sectors/Custom Silicon & Networking Semiconductors]] — AVGO ASIC + hyperscaler XPU demand is the second-largest leading-edge bucket
- [[Sectors/NAND Memory & Storage]] — adjacent foundry-tech franchise; hybrid-bonding overlap with TSMC SoIC
- [[Sectors/Optical Networking & Photonics]] — COUPE / co-packaged-optics integration with TSMC advanced packaging

## Log
### 2026-04-22
- Initial sector note created via subsector split from [[_Archive/Sectors/Semiconductors]] — pending prompt-fill of sector analysis sections.
- Reordered sections: Active Theses moved to first position per Sector Template / CLAUDE.md §Sector Notes (MOC navigation goes first).
- Sector fill (web-primary + vault-secondary): populated Key industry questions, Industry history, Competitive dynamics, Product level analysis, Acquisitions and new entrants, Macro shifts, Investor heuristics, Related Research. Status flipped draft → active (8 sections filled ≥ 5 threshold). Web sources: TSMC Q1 2026 (70% share, 74% ≤7nm, 58.8% GM, N2 HVM); Samsung SF2 55-60% yield + Tesla AI6 $16.5B; Intel 18A HVM at Fab 52 + AWS/MSFT anchors; SMIC N+2 at 15-46%; Rapidus IIM-1 2nm pilot; GF Foundry 2.0; UMC/VIS/PSMC/Hua Hong/Nexchip/Tower mature tier; foundry history (Chang 1987 → UMC → Samsung 2005 → GF 2009 → IBM 2014); CHIPS Act finalized ($7.86B Intel / $6.6B TSMC / $4.75B Samsung); advanced packaging (CoWoS 35K→130K wpm, Foveros, I-Cube); High-NA EUV split. Vault-secondary: TSM Stress Test, Hybrid Bonding/BESI, Jensen moat interview, Huawei Ascend roadmap.

### 2026-04-24 (/sync)
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]: $100B 2028 capex + "good people" pricing discipline validates monopoly-rents thesis for TSM; ASML sold out adds upstream tail-risk. Sector-level implication reinforces the "leading-edge de-facto monopoly" core framing.
- [[Research/2026-04-24 - Iran War Japan Semiconductor Photo Materials Shortage - news]]: Leading-edge PR/BARC supply chain (Shin-Etsu, TOK feed TSMC too); Taiwan localization farther along than Japanese per source — TSM less exposed but not zero. Adds a fifth unmodeled foundry supply-chain vector.
