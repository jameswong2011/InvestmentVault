---
publish: false
date: 2026-08-13
tags: [research, datacenter, ai-capex, macro]
sector: Data Center Power & Cooling
source: 'https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter'
source_type: deep-dive
propagated_to: [VRT, NBIS, CRWV, BE, IREN]
---

# Datacenter Capacity Cancellation Myth — SemiAnalysis vs the "50% Canceled" Headline

## Thesis Delta

Media consensus — Bloomberg's April 1 2026 "China electrical parts" feature, amplified into "half of 2026 US datacenter capacity is delayed or canceled" by TechRadar, Tom's Hardware, and The Register — collides with SemiAnalysis's bottom-up, filing-by-filing datacenter model, which moved its YE2026 North American hyperscaler self-build forecast by only ~1% (NA colocation <5%) over six months. The "cancellation wave" is a vibe-coded artifact of announcement-at-face-value models over-counting a structurally oversupplied early-stage announcement layer; the AI-capex-bust bear case is weaker than the headlines imply, because the veritable, equipment-ordered 2026 pipeline is progressing on schedule and delivered megawatts are accelerating, not stalling.

## Summary

The viral claim that half of 2026 US datacenter capacity will be delayed or canceled traces to a single Bloomberg feature framing the 2026 slowdown as a consequence of a fragile, China-dependent equipment supply chain, then sharpened into clickbait by downstream outlets. Against that headline, SemiAnalysis — whose datacenter model is updated by reviewing every site dozens of times a year, and which was first to flag Core Scientific's delays ahead of CoreWeave's Q3'25 earnings — moved its YE2026 NA hyperscaler self-build forecast by only ~1% over six months, and NA colocation by less than 5%. The distance between a "50% canceled" headline and a ~1% forecast revision is the entire insight: the two numbers cannot both describe the same pipeline.

Two structural errors manufacture the headline. First, a broken denominator: Bloomberg's underlying Sightline Climate data assumes roughly 12 GW comes online in the US in 2026 with only ~5 GW under construction, but SemiAnalysis's satellite-trained Vision Model finds the top-two hyperscalers alone exceed 5 GW of self-build under construction — before any third-party developer capacity. Sightline tracks large, publicly announced projects, which skews its basis toward exactly the speculative megaprojects most likely to slip; the "50% delayed" figure is therefore a statement about the slice of the pipeline most prone to slipping, not about the pipeline. Second, almost everything getting flagged sits in the pre-construction "announced" bucket — speculative megawatts that no rigorous analyst placed on a 2026 timeline in the first place. In SemiAnalysis's model these show up in 2028+, not as 2026 cancellations. Over a Terawatt now sits in the US large-load queue (up from half a Terawatt in December 2025); the vast majority is speculative, and low-probability datacenters never enter the delivery timeline.

Delays and cancellations are real, and the source is granular about them — which is what separates it from the narrative it attacks. The STACK Infrastructure/Oracle Stargate campus in New Mexico slipped to 2029 on a gas-pipeline permitting cascade (a FERC Section 7 review, a state-land right-of-way denial, and dual behind-the-meter microgrids squeezed just under the 250-tpy NOx major-source threshold). Nebius's New Jersey flagship stretched from a targeted 4-month first-phase delivery to roughly 10-11 months. Core Scientific's Denton campus missed its 250 MW YE2025 target on permitting, a GB200 infrastructure redesign, weather, and a transformer explosion. But these are localized construction and permitting stories, not demand destruction — and SemiAnalysis then correctly predicted CoreWeave's 1.7 GW of active power by YE2026, exactly the company guide, precisely because it determined most other sites were on time. The veritable 2026 projects — those with site control, equipment on order, signed interconnection, or vertical construction underway — continue to progress on schedule; 24 GW is expected online in 2026, already under construction and tracking.

The epistemic core is bottom-up primary-source reconciliation versus top-down vibe models. SemiAnalysis parses thousands of municipal, county, state, and utility portals — many resistant to scraping, some still in scanned PDFs — and reconciles every signal against tasked satellite imagery, while its Industrials Model maps 550+ equipment suppliers across 6,000+ facilities. That is contrasted with "Claude Coded" models that ingest press releases, treat GW-scale announcements as ground truth, misunderstand construction timelines and grid complexity, and compile inaccurate reports. This is the base-rate / outside-view discipline in action ([[Mental Models/Generalist - Overview|G-10]]): the ~1% revision is the reference-class correction to an extrapolated, sensational narrative, and the announced-MW pipeline is precisely the inside-view artifact that base rates deflate. Held as a hypothesis to test rather than a verdict: a model marketed as "trusted for billion-dollar decisions" is itself an inside-view authority claim, and "the physical build is intact" — Perez-style on-track deployment ([[Mental Models/Generalist - Overview|G-4]]) — is a narrower claim than "the build earns its cost of capital." The semiconductor anti-pattern against reading real capacity from announcements taken at face value ([[Mental Models/Industry - Semiconductors|#17]]) applies symmetrically here: you cannot infer real cancellation from an announcement's withdrawal any more than you can infer real capacity from its unveiling. Both directions require reconciliation against site control, permits, equipment orders, and imagery — which is exactly the reconciliation the headline skips.

## Evidence

**Forecast revision — the core datapoint (past 6 months):**

| Metric | Revision / figure | Tag |
|---|---|---|
| YE2026 NA hyperscaler self-build forecast | ~1% moved | [1×: SemiAnalysis datacenter model] |
| NA colocation forecast | <5% moved | [1×: SemiAnalysis datacenter model] |
| 2026 US capacity coming online (SemiAnalysis base) | 24 GW, already under construction and tracking | [web: semianalysis] |

**The broken denominator + speculative queue:**

| Item | Figure | Tag |
|---|---|---|
| Sightline Climate: 2026 US capacity online | ~12 GW | [web: semianalysis] |
| Sightline Climate: currently under construction | ~5 GW | [web: semianalysis] |
| SemiAnalysis Vision Model: top-2 hyperscalers alone, under construction (self-build only) | >5 GW | [1×: SemiAnalysis Vision Model] |
| US large-load queue (Dec 2025 → now) | >0.5 TW → >1 TW | [web: semianalysis] |
| ERCOT large-load interconnection requests (Apr 2026) | >410 GW, >87% from datacenters | [web: semianalysis] |
| Texas all-time peak demand (queue ≈ 5x grid) | ~85 GW | [web: semianalysis] |
| ERCOT "phantom" datacenter demand (SemiAnalysis) | 311 GW | [1×: SemiAnalysis datacenter model] |

**Anatomy of real delays (per-site, primary filings + satellite):**

| Site / operator | Original target | SemiAnalysis call | Binding cause | Tag |
|---|---|---|---|---|
| STACK/Oracle NM Stargate (Project Jupiter) | 1H2027 delivery (Oracle Jun 10 guide) | Delayed to 2029 | Gas pipeline (FERC CP26-80-000, Section 7), NM State Land Office ROW denial, dual-microgrid NOx | [web: semianalysis] |
| — East microgrid NOx | 248.90 tpy requested vs up to 521 tpy | Untenable vs 250 tpy major-source line | [web: semianalysis] |
| — West microgrid NOx | 249.97 tpy requested vs up to 388 tpy | Untenable; Bloom fuel-cell swap ~37 tpy | [web: semianalysis] |
| Nebius NJ flagship (DataOne) | 4-mo first 50 MW; 100 MW by YE2025 | ~25 MW energized at YE2025; full 50 MW ~Jan-Feb 2026 (~10-11 mo) | Late supplier deliveries, MEP + commissioning | [web: semianalysis] |
| Core Scientific Denton (→ CoreWeave) | 250 MW by YE2025 | Missed | Permitting, GB200 redesign, weather, transformer explosion | [web: semianalysis] |
| Cloudburst San Marcos TX (1.2 GW total) | 50 MW live Q3→Q4 2026 | Q4 2026 too aggressive; broke ground Nov 2025 | Shell construction not started | [web: semianalysis] |
| TeraWulf Lake Mariner + Abernathy (Fluidstack) | YE2026 (company reiterated Feb 26 2026) | Abernathy → 2027; Lake Mariner 2nd 80 MW tight | MEP + commissioning overlooked | [web: semianalysis] |

**Speculative announcements SemiAnalysis discounts (culled, not "canceled 2026 capacity"):**

| Announcement | Headline | Reality per satellite / filings | Tag |
|---|---|---|---|
| Data City / Energy Abundance (Laredo TX) | 5 GW campus, 300 MW in 2026 | No physical progress; site is a "Contact Us" page | [web: semianalysis] |
| APR Energy (Pampa TX) | 400 MW, first phase early 2026 | No customer, new developer, <1-yr timeline; no news since | [web: semianalysis] |
| Compass (Prince William County) + rezonings (GA, 20+ states) | "canceled/withdrawn" | Announcement-layer only — no equipment, no interconnect, no 2026 delivery to lose | [web: semianalysis] |
| Maine LD 307 (would-be first statewide ban) | Statewide ban (vetoed Apr) | Maine has <5 MW planned; ≥12 states filed moratorium bills, all in inconsequential areas | [web: semianalysis] |

**Equipment supplier / lead-time evidence (directly rebuts the Vertiv bear framing):**

| Item | Figure | Tag |
|---|---|---|
| Grid connection lead times (multiple metros) | 7-10 years | [web: semianalysis] |
| Reinhausen tap-changer bushings (gates entire HV stack) | 3-5 years quoted | [web: semianalysis] |
| GE Vernova / Hitachi Energy / Mitsubishi Electric main lines | Booked out 3-4 years | [web: semianalysis] |
| Hitachi Energy South Boston plant (announced Sep 2025) | Not operational until 2028 | [web: semianalysis] |
| Behind-the-meter prepayment to hold queue slot | 10-15% now standard | [web: semianalysis] |
| Vertiv / Schneider pure-play datacenter electricals margin | >20% on demand-supply imbalance | [web: semianalysis] |
| SemiAnalysis Industrials Model coverage | 550+ suppliers, 75 subcategories, 6,000+ facilities | [1×: SemiAnalysis Industrials Model] |

**Demand signals that did not move:**

| Item | Figure | Tag |
|---|---|---|
| CoreWeave active power YE2026 (SemiAnalysis predicted = company guide) | 1.7 GW | [web: semianalysis] |
| NA RPO signed by Q1 2026 (SemiAnalysis industry-first method) | ~$35B | [1×: SemiAnalysis datacenter model] |
| Nebius ARR guidance YE2026 | $7-9B | [web: semianalysis] |
| SemiAnalysis reported Claude Code spend (own usage) | $170K+ in one week | [web: semianalysis] |

## Contradiction Check

This source **challenges** the "AI datacenter cancellation / capex bubble bursting" bear narrative on its physical leg, and **supports** buildout-levered theses. It bears most directly on [[Theses/VRT - Vertiv Holdings]], with secondary two-sided read-through to [[Theses/NBIS - Nebius Group]] and [[Theses/CRWV - CoreWeave]], and a partial tension with the macro view.

**VRT — most directly supported.** The source's "The Equipment Supplier Narrative Is Wrong Too" section is a point-by-point rebuttal of the mechanism in [[Theses/VRT - Vertiv Holdings]] §Bear Case ("AI capex peaks 2H 2026... orders fall 40-60% in 2027, creating 2028 revenue decline"). SemiAnalysis's counter: the projects getting canceled sit in the early-stage layer that never placed equipment orders, so a speculative announcement dying in a county commission hearing removes zero orders from anyone's books; the projects actually in OEM backlogs have prepaid for queue position and locked long-lead SKUs in scoping; and a queue running 3-4 years deep means a rare real cancellation reallocates the slot to the next buyer rather than vanishing. Delivered MWs are accelerating and pure-play electricals hold >20% margins — the physical evidence under VRT §Key Non-consensus Insights ("Backlog duration is being underpriced as demand volume" and "The real chokepoint is grid interconnect, and Vertiv benefits regardless"). It cuts against VRT §Risks position-risk #1 ("if 'AI bubble' becomes consensus framing in 2026-2027, multiple compression can happen 6-12 months before earnings actually disappoint"): the source argues that framing is factually wrong on the physical build. Held as hypothesis, not verdict: this is a physical-pipeline datapoint, and carries no evidence on VRT share, OCP-authorship advantage, or order conversion — the same separation already logged in the VRT §Key Non-consensus Insights power-markets caution (equipment scarcity ≠ vendor pricing power). Same-class read-through extends to [[Sectors/Data Center Power & Cooling]] and to [[Theses/BE - Bloom Energy]], whose fuel cells are the permit-driven substitute at the STACK/Oracle site once the gas turbines failed to clear NOx.

**NBIS — two-sided execution evidence.** SemiAnalysis uses Nebius's NJ flagship (DataOne) as its worked example of construction difficulty, bearing directly on [[Theses/NBIS - Nebius Group]] §Outstanding Questions #1 ("Can NBIS physically energize 800MW-1GW by YE2026 off ~170MW at YE2025 — a >4x build") and §Bear Case #1 ("The power build slips"). The evidence must be held as genuinely two-sided: real slippage (a 4-month target became ~10-11 months; only ~25 MW energized against 100 MW promised for YE2025) confirms the execution risk is live and physical — but SemiAnalysis explicitly calls 10-11 months "very fast relative to industry standards," and the cause is MEP/commissioning and supplier lateness, not demand or financing. This sharpens NBIS Outstanding Q#1's own instruction to track active/commissioned MW, not announced pipeline. It does not resolve the load-bearing >4x build; it quantifies how long one flagship's first phase actually took, which is the base rate the Q3-weighted 2026 ramp must beat.

**CRWV — supports the demand/backlog leg, silent on the credit leg.** The Core Scientific/Denton delay is the source's third worked example, bearing on [[Theses/CRWV - CoreWeave]] §Risks thesis-risk #5 ("Capex execution risk... Microsoft already cited delivery issues and missed deadlines") and the single-builder dependence flagged in CRWV §Mental Models ("Core Scientific deal TERMINATED... single-builder dependence persists on the same counterparty whose delays drove the securities class action"). SemiAnalysis flagged the CoreWeave delay ahead of Q3'25 earnings — then predicted CoreWeave's 1.7 GW active power by YE2026 exactly on the company guide, evidence that aggregate 2026 delivery is on track even where one builder slipped. This supports the demand/backlog leg of the CRWV thesis while leaving the credit/re-rent leg (§Bear Case driver #1, the DDTL amortization-cliff) entirely untouched. The miner-pivot buildout class the source tracks (TeraWulf/Fluidstack, Core Scientific) is the same durable-landlord segment covered in [[Sectors/Neoclouds & GPU-as-a-Service]] and adjacent to [[Theses/IREN - IREN Limited]].

**Tension with the macro view.** This source is in partial tension with [[Macro & Technology/Sustainability of AI Capex]]. It reinforces the "delayed MW, not delayed demand" framing that [[Research/2026-08-12 - Macro - AWS Calvert County DC Withdrawal - news]] already feeds the macro note — SemiAnalysis's structurally-oversupplied early-stage bucket is the same "contestable capacity" the macro note says the correction will concentrate in. But it pushes hard against any reading that a 2026 physical cancellation wave is imminent. Critically, it does not rebut the macro note's central claim that the build can be "functionally underbuilt and financially overbuilt at the same time." SemiAnalysis argues the physical pipeline is intact (functionally on-track, 24 GW tracking); it is silent on whether that on-track build earns its 8-10% WACC against the macro note's 5-7% aggregate spot ROIC. The two are therefore reconcilable rather than contradictory: physical build on schedule (SemiAnalysis) coexisting with unresolved financial-return dispersion (macro note). The Perez frame ([[Mental Models/Generalist - Overview|G-4]]) holds both — a functional over-build in the frenzy phase lays down real, on-schedule capacity that can still crater equity for the leveraged-merchant tranche. Confirming test to watch: hyperscalers and neoclouds hold or raise capex while lengthening delivery language, and delivered-MW prints keep accelerating even as announcement-layer headlines multiply.

## Source Excerpts

> "over the last 6 months, our YE2026 NA Hyperscaler Self-build forecast only moved by ~1%, and NA colocation <5%."

> "the data sources behind these claims of '50% of 2026 datacenters are delayed' are essentially uninformed vibe-coded datacenter forecasts that take announcements at face value, without any bit of critical judgement."

> "The '50% cancelled or delayed' figure isn't really a statement about the US datacenter pipeline, but rather about the slice of the pipeline most prone to slipping."

> "The projects getting canceled sit in the early stage layer that never placed equipment orders in the first place; a speculative announcement dying in a county commission hearing removes zero orders from anyone's books."

> "When the noise is filtered out, our 2026 US datacenter outlook is largely intact. 24GW is expected to come online this year, which are already under construction and tracking."
