---
publish: false
date: 2026-08-16
tags: [research, Power-Grid, Macro, NBIS, NVDA, SPCX]
sector: 'Power & Energy Infrastructure'
ticker: 
source: 'https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted'
source_type: deep-dive
propagated_to: [NBIS, NVDA, SPCX, NET, TSM]
---

# $12B PJM Modeling Mistake — SemiAnalysis

## Thesis Delta

Consensus prices the 17–24% June 2025 PJM bill jump and the 6.8 GW Reliability Backstop as the physical cost of AI load growth in America's largest electricity market — a reading the vault already carries as "PJM 8+yr queue / BRA short ~6.6 GW" in [[Sectors/Data Center Power & Cooling]] and as corroboration of negative accredited headroom in [[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]]. This source implies the 2025–27 $12B overcharge is a Reserve Requirement Study error (summer-only thermal ratings plus Storm Elliott-era winter-failure clustering still in the Monte Carlo) that left ~4 GW of already-built winter capability uncredited, and that PJM is about to lock the same error into 11–15 year contracts to 2043 with no committed large-load counterparties — so [[Theses/NBIS - Nebius Group]]'s Philadelphia gigawatt sites, and any [[Theses/NVDA - Nvidia]] or [[Theses/SPCX - SpaceX]] campus that still needs a PJM interconnection, face a market that over-pays existing plants, does not accelerate the queue, and is being written off for behind-the-meter or other ISOs (touches [[Theses/NBIS - Nebius Group]] §Conviction Triggers → LOW if Q3 2026 active-power build misses by >20%; evidence-touched, dir=watch — Philadelphia sits in PJM; source does not print an NBIS MW figure).

## Summary

PJM's 66 million residents paid a ~20% bill increase that SemiAnalysis traces to auction design plus a black-box planning model, not to a physical shortage of already-built plants. The Energy Model team spent six months reverse-engineering the Reserve Requirement Study (RRS) — the hourly Monte Carlo that sets how many accredited megawatts the Base Residual Auction (BRA) must buy to hold loss-of-load expectation at 0.1 days per year. The reconstructed model matches PJM's published outputs across the last four auctions. Two input errors survive that match: (1) thermal plants are capped at summer ICAP even though cold, dense air raises combustion-turbine output by up to 25% (class-table winter average 8.4% for turbines) and PJM itself measured 8,561 MW of winter nameplate uplift; (2) class forced-outage series still embed the Polar Vortex (2013) and Storm Elliott (December 2022, 46 GW coincident outages, 24% of the fleet, two-thirds gas) as if the fleet had not winterized, even though >400 of ~450 gas units / ~750 thermal units had filed winterization improvements by January 2024 and post-Elliott storms (Gerri, MLK, Fern) printed 9–10% forced-outage rates against Elliott's 24%. Crediting both levers, net of overlap, is worth ~3.1–3.8 GW of reliable capacity on the auction's scale — eight large gas plants, ~$10B of avoided new-build, 56% of the 6.8 GW emergency-auction target.

The $12B is an auction-curve result, not a per-MW accounting identity. PJM runs the only capacity market that prices ~93% of the fleet — new and existing — at one one-year clearing price. Existing plants bid $8–14/MW-day (Great Britain paid existing generation $18/MW-day); the median existing combined cycle already recovered 407% of going-forward costs in energy and ancillary services in 2025 before a dollar of capacity revenue. New plants bid at the vertical spike of a right-angled supply curve. Four auctions since the July 2024 restart procured 134–138 GW/year at $270–333/MW-day versus $28.92 pre-delay, raising a single auction from $2.2B to $16.4B and the four-auction total to $63.6B, of which only 4.8 GW was new capacity. SemiAnalysis shifts the Variable Resource Requirement (VRR) demand curve left by the remodelled requirement (2,879 / 3,396 / 4,513 / 3,824 MW for 2025/26–2028/29) and re-clears against published supply-curve shapes, holding bids fixed. 2025/26: a 2.7 GW left-shift drops the clearing price from $270 to $135/MW-day while volume falls 14 MW (0.014 GW); $135 × 135.7 GW × 365 days = $6.7B. 2026/27 (first political cap, $329): a 3.1 GW left-shift clears 133.6 GW at $230 versus 134.2 GW at the cap, $4.9B. Combined $11.57B with an $8.0–14.5B sensitivity. 2027/28 and 2028/29 stay pinned at $333.44 and $325.00 because even 4.5 GW and 3.8 GW of requirement relief do not pull the demand curve under the cap against a 6.5 GW / 6.8 GW shortfall. The Independent Market Monitor's September 2024 cold-air-only run ($2.7B with reserve margin held fixed, up to $8.0B without) is the external sense-check; SemiAnalysis adds winterization.

The Reliability Backstop Auction (30 September–21 October 2026, results 2 December, one week before the next BRA opens 9 December) converts that residual 6.8 GW shortfall into 11–15 year make-whole contracts ending 2043, payable in theory by new large loads that have not signed and that each state has not yet allocated. Only resources in service by June 2032 may bid. Zone shares are frozen for fifteen years off 2026/27–2028/29 forecast growth with no true-up. Load-serving entities must post $1.5M per MW of obligation; at the $555/MW-day average cap the 6.8 GW book is a ~$21B maximum liability. The Board overrode a two-thirds-supported voluntary subscription design on 27 July 2026 because it "would not provide sufficient assurance that capacity equal to the identified near-term shortfall would actually be procured," then filed the Board design at FERC on 31 July with pay-as-bid supply (PJM's own witness: sellers "are more likely to offer the expected clearing price"; mitigation "difficult and ineffective") and a revived Interim Resource Adequacy Service that curtails uncovered >50 MW loads first, ahead of paid demand response. Recalculating the shortfall at ~3.0 GW would have left a gap a subscription model could have covered. Participation buys no interconnection acceleration. Self-supply strictly dominates. Datacenter developers are already writing PJM off for other ISOs or behind-the-meter configurations. If states do nothing, the filing default drops costs on every load-serving entity by peak-load share — residential ratepayers again.

The deeper failure is a no-growth market hitting its first load-growth decade under a five-sector two-thirds vetocracy. Interconnection had no general study path from October 2021 to April 2026 (220 GW then applied). The Reliability Resource Initiative picked 51 shovel-ready projects in May 2025, now 41 with 31.5% of megawatts withdrawn and first output scheduled 2030; the 10-units-a-year Expedited Track opened 31 July 2026; neither has energized a megawatt. Lead time for new generation was cut from the Independent Market Monitor's intended 36 months to 10 months at restart, 23 months in the latest auction. Winter-ratings text (Package C) passed the ELCC task force 178–54 (77%) in July 2025 and died at the senior committee on 20 August 2025 with 30.7% of the weighted vote — generators argued a higher winter rating raises the summer performance-penalty benchmark; consumer sectors voted PJM's package down while backing blunter alternatives the generators then killed. E3's December 2025 review listed seasonal or daily capability ratings as consideration 4 of 14. FERC has given PJM until the end of September 2026 to reform governance or FERC will intervene; comments on the backstop close 21 August 17:00 Eastern. SemiAnalysis's ask: implement the two modeling credits for the emergency auction and future BRAs, open an inquiry into 2025/26 and 2026/27 overspend, split new versus existing auctions, recalculate the 6.8 GW target before contracts run to 2043, and prefer direct capacity contracting inside accelerated interconnection agreements over an unbacked 15-year backstop. The model is a public-data approximation (RTO-wide, no locational deliverability areas, confidential offer stack, four proxies, +3.0% EUE residual). If it is even half right, the next ninety days lock a modelling error into a multi-decade ratepayer liability and push the largest US datacenter market further off-grid.

## Framework / Mental Model

### 1. Reverse-engineered Reserve Requirement Study (SemiAnalysis PJM Model)

SemiAnalysis rebuilt PJM Manual 20A Revision 3 (effective 24 June 2026) in code, drove it with PJM's posted 2028/29 ELCC workbooks (25 February 2026) plus EIA/ERA5/FERC Form 1 proxies where PJM withholds resource-level detail, and validated against four auctions of published outputs. No confidential PJM data. The study is an hourly matching of supply against load across 416 scenarios (32 historical weather years × 13 calendar rotations) scaled to the 165,953.5 MW 50/50 forecast peak, averaged over 41,600 equally weighted annual cases. Manual 20A permits a daily random load adjustment; SemiAnalysis adds none because PJM's loss-of-load workbook shows zero load variation across replications.

| Block | Rule | Proxy / note |
|---|---|---|
| Thermal availability | `available = ICAP × (1 − forced outage rate) × (1 − ambient derate)` | Nine classes drawn together from one historical performance day, conditioned on temperature-humidity bins — nuclear, gas CC, gas turbine, dual-fuel GT, coal, steam, oil turbine, waste-to-energy, diesel |
| Dual-fuel | PJM withholds class composition | +3,250 MW dual-fuel availability uplift on gas CC, EIA-860/923, checked to posted supply stack |
| Planned outages | Posted weekly maintenance, allocated by class, after forced + ambient | Removing them entirely moves IRM 0.14 pp |
| Wind / solar / hydro | Posted hourly class series; hydro most-similar-delivery-year | Offshore wind = ERA5 reanalysis validated to posted LOLH; non-pumped hydro = flat 1,842 MW inferred from workbook floors |
| Storage | Manual 20A chronological heuristic: DR first, then batteries longest-duration-first (10h → 4h); surplus charging proportional | 4/6/8-hour split, 0.78 round-trip efficiency (EIA-923/930 + FERC Form 1); reproduces all four posted storage class ratings within 1.5 pp |
| Demand response | Summer: nominated MW × hourly load / 50/50 peak inside seasonal windows; winter: 2025 ELCC/RRS hourly shape | Winter shape matches 2028/29 LOLH workbook within 0.0005 pu; dispatch cap 24 h/day |
| Reliability metrics | Per hour: supply (thermal + variable + storage + DR) vs load | EUE = shortfall MWh; LOLE = days with ≥1 shortfall hour; LOLH = shortfall hours. Standard: LOLE = 0.1 days/year |
| Installed reserve margin | `IRM = (ICAP / solved peak − 1 − CBOT) × 100` | CBOT (capacity benefit of ties) = 1.5%. Solver brackets one rotation per weather year, then refines on the full 416 |

2028/29 validation against PJM: solved peak 162,107 MW vs 162,063 (+44 MW, +0.027%); IRM 19.95% vs 20.0%; LOLE at PJM's solved load 0.09921 vs 0.09988 (−0.7%); all 20 posted ELCC class ratings within 1.8 pp; winter and January EUE shares within 0.5 pp; EUE 1,808.8 vs 1,755.6 MWh/yr (+3.0% — the open residual, attributed to storage-dispatch detail).

Limitations the authors flag: RTO-wide only (no MAAC / EMAAC / SWMAAC / DOM locational deliverability, so no constrained-zone price); cannot re-run the auction (offer stack confidential) — results are positioned on the published VRR; four proxies (offshore wind, hydro-NPS, storage composition, dual-fuel block); 3,546 MW of PJM's official 154,234 MW accredited-UCAP total cannot be attributed to named resources and is carried as an unallocated reconciliation outside hourly physics.

Committed-fleet reconstruction for the July 2026 2028/29 auction: PJM published 138,317.8 MW UCAP cleared at the $325/MW-day cap, 6,831.3 MW below the 156,012.9 MW requirement, and did not publish winning units. SemiAnalysis graded all 1,308 rostered generators on public documents (FRR plans, must-offer notices, deactivation letters) into five evidence tiers (91 direct-commitment-floor, 36 high, 1,165 medium-high, 13 medium, 3 low). Four independent reconstruction methods (evidence-weighted refit, subtraction from the planning fleet, a 2,048-mapping constraint ensemble, cross-year continuity) all land between LOLE 0.43 and 0.59 at forecast load. The published case uses the best-evidenced reconstruction: 0.487 LOLE for the Committed Fleet, 0.24 LOLE for the full Assumed Fleet.

### 2. Two-control paired-run methodology (cold-air uplift × asset winterization)

Each control edits inputs before they reach the Monte Carlo. Winter capability and weatherization modify the raw forced-outage and ambient-derate arrays at a bridge layer. Impact is measured with paired runs: baseline, apply one control, re-run. The simulation is deterministic for a given data bundle, seed, and settings, so the two runs differ only in the control. Metrics: LOLE, solved peak load, and firm megawatts needed to restore the 0.1 standard. Both runs use identical weather years and identical outage draws.

**Cold-air uplift.** A turbine is a mass-flow machine: cold air is denser, so mass flow and peak electrical output rise. Combustion turbines up to 25%; PJM's class table averages 8.4% for turbines over November–April. Steam plants gain from colder cooling water (lower condenser pressure). PJM already applies ambient *derates* when temperatures rise and does not apply ambient *uprates* when they fall — E3's December 2025 line: "PJM asymmetrically applies ambient derates to the ICAP of unlimited resource classes when temperatures rise but does not apply ambient uprates when temperatures fall." SemiAnalysis credits 0–100% of the published 2026/27 class winter-uplift table, November–April only: nuclear 4.5%, coal 1.9%, gas CC 5.4%, gas turbine 8.4%, dual-fuel GT 14.8%, steam 1.8%, diesel 0.9%, other thermal 9.7%. PJM's winter *failure rates are left untouched*. Netted over 41,600 simulated years, cold air alone cuts the capacity requirement 1.3–2.2 GW depending on year. At 100% the model recreates PJM's historical bookend, not unit-level 2028/29 accreditation; Package C would cap actual winter output from 2028/29 at awarded winter interconnection rights (CIRs). PJM measured 8.5 GW / 8,561 MW winter nameplate uplift (May 2025 sensitivity: 33% fewer winter loss-of-load hours, 1.1 pp lower reserve margin on the 2026/27 model) and did not implement it, citing undelivered deliverability studies. SemiAnalysis's physical counter: in the stressed hours a large share of the otherwise-deliverable fleet is offline, and cold also raises the thermal rating of conductors, substations, and breakers.

**Asset winterization.** The lever does *not* assume plants fail less often. It preserves each class's annual average failure rate exactly and removes only weather clustering: each selected class's hourly profile is blended from the posted correlated series (0%) toward its flat annual mean (100%). At 100%, plants fail just as often on average but no longer all together on the coldest days — a mathematical upper bound on decorrelation. A genuinely winterized fleet would also fail less on average; that credit is excluded. Conservative schedule: 50% winterization for 2025/26, then +10% per year. Justification: FERC/NERC joint inquiry (October 2023) found at least 75% of Elliott freezing-caused failures occurred *above* the units' documented operating limits, so a properly winterized unit would not have failed. Mandatory cold-weather preparedness plans, annual training, and reporting of cold-weather operating limits were in force by April 2023. By January 2024 more than 400 generators had reported winterization improvements (PJM's own Storm Gerri review). Extreme-cold-weather-temperature calculations were due October 2024; the event-CAP rule was enforceable from October 2024; any unit that froze in winter 2024/25 owed a completed corrective plan before December 2025. Binding NERC winterization standards ramp through 2027 (too late for the auctions already run). Post-Elliott performance: Gerri (January 2024) 16 GW / 9% forced outages vs Elliott 46 GW; MLK (January 2025) 9% vs Elliott 24% on similar weather over a holiday weekend at an all-time winter peak, with no excess clustering; Fern (January 2026) 18–19 GW / 10%.

**Overlap.** Both controls fix the same deep-cold hours that set the requirement. 2026/27 on the auction's scale: cold air alone 1,535 MW; weatherization at 100% 3,143 MW; together 3,320 MW, not 4,678. At 100% winterization covers 76–96% of cold air's effect depending on year; at the authors' annual settings the overlap is 53–69%. Combined 2026/27 setting used in the $12B arithmetic: cold air 1.5 GW + weatherization 2.5 GW at 60% → 3.1 GW net.

### 3. Capacity-market design: missing money, VRR, single-stack clearing

Two costs exist in any power market: short-run marginal cost (fuel, labor, variable maintenance) and long-run marginal cost (capital, fixed maintenance). The energy market clears at the SRMC of the last needed producer. The gap to LRMC is the "missing money" problem. ERCOT recovers it with energy-only scarcity pricing. PJM recovers it with an annual capacity auction. The RRS sets the reliability quantity (0.1 LOLE). The Variable Resource Requirement is a published sliding price schedule of what PJM will pay at each supply level. The BRA is the yearly auction in which generation bids and PJM buys against that curve. The BRA does not stop at the required quantity: if more capacity is offered at a price PJM has deemed acceptable, it clears.

PJM is unique on two axes. First, ~92–93% of fleet capacity — new and existing — settles at one one-year marginal price (the rest is Fixed Resource Requirement self-supply, ~8% / ~12 GW in 2026/27). Comparables: MISO residual auction ~15% of the requirement (86% of 2025/26 summer requirement met outside the auction); New York monthly rolling; California bilateral; Texas none; New England abandoned the design; Great Britain, Ireland, Italy, and Japan give qualifying new plants 10- or 20-year contracts and existing plants one year. Japan was the last other whole-fleet one-year market and has bolted on a separate 20-year new-entry auction after concluding the design builds nothing. Second, a right-angled supply curve: 2025/26 had the first 79% of bids at $2–5/MW-day, the next 20% rising to $105, and only the last 1% up to $352, clearing at $270. At the vertical spike, a small change in quantity demanded moves price and total cost by billions while moving volume by tens of megawatts. That is the mechanism that turns a 2.7 GW modelling error into a $6.7B bill with 14 MW of volume change.

Self-supply (FRR) lets a utility eject from the auction for five years against an obligation equal to its load share. The RRS models an Assumed Fleet and prints a whole-system number (e.g. 146 GW reliable capacity for 2026/27). The auction target is that number minus the FRR obligation (e.g. 134 GW). The Committed Fleet is auction winners plus FRR plans. In 2026/27 the auction cleared 134.3 GW (0.2 GW short of target) while FRR committed 12 GW (~0.3 GW over obligation); the system finished 0.1 GW above the whole-system requirement only because self-supply over-delivered by more than the auction missed.

Retail-choice deregulation, a Supreme Court case striking down state long-term-contract support, and a long FERC fight over resource preferences are why PJM households take the full auction swing. Next door, MISO also printed a sharp residual-auction spike; most households were unaffected because utilities had already contracted.

### 4. Reliability metrics and failure archetypes

PJM uses LOLE as the *system* reliability metric and EUE as the *plant-level* (ELCC) metric. A one-hour rolling brownout and a nine-hour blackout count as the same LOLE event; EUE weights depth and duration. Because the two are mixed, the Reliability Backstop can overshoot or undershoot the 0.1 LOLE target and leave residual shortfalls for later BRAs. Most other markets are moving to EUE and splitting winter/summer; PJM proposed a two-season construct in 2023, withdrew it after IMM objections, and filed an annual-only package that FERC approved in January 2024 without requiring seasonality.

Four failure archetypes sit in the model: (1) summer peaks — heat-driven efficiency loss plus correlated air-conditioning; the 2 July 2026 heat dome printed a preliminary 168,158 MW all-time high, beating the 165,563 MW August 2006 record; (2) winter storms — longer, more deadly, more likely to cascade; Elliott 46 GW / 70% of gas / 24% of fleet, worse than the 2014 Polar Vortex's 22% fleet failure; two modes, icing of rarely-run units and fuel-accessibility (gas diverted to home heating, wellhead freeze-off); (3) shoulder-season planned-maintenance coinciding with unseasonal weather; (4) random forced trips. SPP and others set a tighter winter reliability standard for this reason. ELCC compresses each resource's marginal reliability contribution to a single score (100% = a perfect resource that shows up at full output in every event). A winter-risk system degrades summer-strong resources (solar, storage) and enhances winter-strong resources (nuclear, coal); a small change in winter gas risk reprices every class.

## Evidence

**Headline cost and volume** `[1×: SemiAnalysis]` `[web: semianalysis.com]`

| Claim | Figure | Window / note |
|---|---|---|
| Ratepayer overcharge, remodelled vs actual BRA | **$12B** headline; **$11.57B** calculated; **$8.0–14.5B** sensitivity | 2025/26 + 2026/27 only; 2027/28 and 2028/29 price-cap bound |
| 2025/26 saving | **$6.7B** | Price $270 → $135/MW-day; volume −**0.014 GW (14 MW)** |
| 2026/27 saving | **$4.9B** | Price cap-bound → $230/MW-day; volume −**0.6–0.8 GW** |
| Uncredited existing reliable capacity | **~4 GW** (~3.1–3.8 GW net of overlap) | Cold-air + winterization vs PJM RRS |
| Emergency-auction offset | **3.8 GW = 56% of 6.8 GW** | Equivalent of **8 large gas plants / ~$10B** to build today |
| Residents / bill shock | **66 million**; bills **+17–24%** June 2025 | State regulators named the capacity auction as the driver |

**Four-auction history (post-restart)** `[1×: SemiAnalysis]`

| Delivery year | Auction timing | Cleared UCAP | Clearing price | vs requirement | Auction cost |
|---|---|---|---|---|---|
| Pre-delay reference | — | — | **$28.92/MW-day** | — | **$2.2B** |
| 2025/26 | (first spike year) | **135.7 GW** | **$270** (ceiling $452; required 133.6 GW) | +2.1 GW over required | (inside $16.4B peak-year print) |
| 2026/27 | first political cap **$329** | **134.2 GW** | cap-bound | **−0.3 GW** vs 134.5 GW required | — |
| 2027/28 | December 2025 | — | **$333.44** (cap) | **−6.5 GW** | — |
| 2028/29 | July 2026 | **138,317.8 MW** | **$325.00** (cap) | **−6,831.3 MW** vs **156,012.9 MW** | — |
| Four-auction total | Jul 2024 restart onward | 134–138 GW/yr | $270–333 | — | **$63.6B** |
| New capacity procured across four auctions | | **4.8 GW** | | | Transfer to existing plants |

**2025/26 supply-curve shape (why 14 MW moves $6.7B)** `[1×: SemiAnalysis]`

| Bid tranche | Share of stack | Price band |
|---|---|---|
| Existing / infra-marginal | first **79%** | **$2–5/MW-day** |
| Intermediate | next **20%** | rising to **$105** |
| New / vertical spike | last **1%** | up to **$352**; market cleared **$270** |

Worked re-clear, bids held fixed: VRR shifted left **2.7 GW** → required 130.9 GW; auction still clears 135.7 GW at **$135/MW-day** (50% discount). Saving = $135/MW-day × 135.7 GW × 365 days (+ $270 × 0.014 GW). IMM September 2024 cold-air-only: **$2.7B** reserve-margin-fixed, up to **$8.0B** without. `[1×: SemiAnalysis]` `[1×: PJM IMM]`

**2026/27 re-clear** `[1×: SemiAnalysis]`

| | As run | Remodelled |
|---|---|---|
| VRR shift | — | **3.1 GW** left |
| Required | 134.5 GW | 131.4 GW |
| Cleared | 134.2 GW at $329 cap | 133.6 GW at **$230** |
| Reliability margin | 0.3 GW short | improved vs remodelled target |
| Saving | — | **$99/MW-day × stack = $4.9B** |

**Whole-system requirement relief at 0.1 LOLE (RRS remodel)** `[1×: SemiAnalysis]`

| Delivery year | Requirement reduction | Auction price impact |
|---|---|---|
| 2025/26 | **2,879 MW** | $6.7B (free-moving price) |
| 2026/27 | **3,396 MW** | $4.9B (under $329 cap) |
| 2027/28 | **4,513 MW** | none — still under cap against 6.5 GW short |
| 2028/29 | **3,824 MW** | none — still under cap; emergency target **6.8 → ~3.0 GW** |

**Cold-air and winterization levers** `[1×: SemiAnalysis]` `[web: semianalysis.com]`

| Lever | Isolated effect | Combined (net of overlap) | Source corroboration |
|---|---|---|---|
| Cold-air uplift, failure rates untouched | **1.3–2.2 GW** requirement cut; **1,535 MW** on 2026/27 auction scale | — | E3 Dec 2025 asymmetry quote; PJM May 2025 sensitivity **−33% winter LOLH, −1.1 pp** reserve margin; PJM-measured winter nameplate **8.5 GW / 8,561 MW** (~$13B of new gas at $1,500/kW) |
| Winterization (preserves mean FOR, removes clustering) | up to **3 GW** (2026/27); **3,143 MW** at 100% | — | >**400** of ~450 gas / ~750 thermal units filed improvements by Jan 2024; FERC/NERC ≥**75%** of Elliott freeze failures above documented limits |
| Combined, authors' settings | 1.5 GW + 2.5 GW @ 60% | **3.1 GW** (2026/27); **3,320 MW** at 100% winterization vs 4,678 arithmetic sum | Overlap **53–69%** at chosen settings; **76–96%** at 100% winterization |
| Conservative winterization path | **50%** in 2025/26, **+10 pp/year** | used in $12B case | Explicitly excludes any cut in *average* failure rates |

**Post-Elliott winter performance vs model memory** `[1×: SemiAnalysis]`

| Event | Date | Forced outages | vs Elliott |
|---|---|---|---|
| Polar Vortex | 2014 (2013 vortex is the model's largest remaining driver) | **22%** of fleet | — |
| Storm Elliott | Dec 2022 | **46 GW / 24%** of fleet; **70%** of gas; two-thirds of the 24% loss from gas | reference |
| Storm Gerri | Jan 2024 | **16 GW / 9%** | ~1/3 of Elliott MW |
| MLK storm | Jan 2025 | **9%** on Elliott-like weather, holiday weekend, all-time winter peak; **no excess clustering** | — |
| Storm Fern | Jan 2026 | **18–19 GW / 10%** | — |

EFORd → RRS (2024) was the response to Elliott: hourly risk, correlated winter failures, variable and limited resources. Gas took a **10–20%** accreditation knock-down. Cleared capacity fell **8% / 12 GW** (147 → 135 GW) between 2024/25 and 2025/26. Historical performance is flushed on a decade-plus lag; investment, regulation, and subsequent good performance cannot lift the judgment until the event ages out. `[1×: SemiAnalysis]`

**Going-forward cost vs clearing price** `[1×: SemiAnalysis]` `[1×: PJM IMM]`

| Benchmark | Level |
|---|---|
| Existing-generator BRA offers (IMM) | **$8–14/MW-day** |
| Great Britain existing-generation auction | **$18/MW-day** (£5/kW-year) |
| PJM clearing, last four auctions | **$270–333/MW-day** (20–40× existing offers; ~10–12× pre-delay $28.92) |
| Median existing combined cycle, energy + AS only, 2025 | **407%** of going-forward costs *before* capacity revenue |

**Interconnection and "new supply" tracks** `[1×: SemiAnalysis]`

| Item | Figure |
|---|---|
| General interconnection study path closed | Oct 2021 – Apr 2026 |
| Applications when window reopened | **220 GW** (Apr 2026) |
| Reliability Resource Initiative | 51 shovel-ready picked May 2025 → **41** remaining; **31.5%** of MW withdrawn; first output **2030** |
| Expedited Track | 10 units/year, opened **31 July 2026** |
| MW energized by either fast-track | **0** |
| BRA lead time vs IMM 36-month design | **10 months** at Jul 2024 restart, **23 months** latest auction |

**Emergency / Reliability Backstop Auction** `[1×: SemiAnalysis]` `[web: semianalysis.com]`

| Parameter | Value |
|---|---|
| Offer window | **30 Sep – 21 Oct 2026**; results **2 Dec 2026** (BRA opens **9 Dec**) |
| FERC comments close | **21 Aug 2026, 17:00 ET** |
| Eligible supply | New resources in service by **June 2032** |
| Contract end | **2043** (≈11 years if COD 2032; up to 15 years if earlier) |
| Quantity | **6.8 GW** as filed; **~3.0 GW** under remodelled RRS |
| Average-price cap | **$555/MW-day** (portfolio average, not per-contract; PJM worked example clears a **$600** offer) |
| Max liability at cap × 6.8 GW | **~$21B** |
| Credit support | **$1.5M / MW** of LSE obligation, within 90 days of each delivery year |
| Cost allocation | Zone shares ∝ forecast load growth 2026/27→2028/29, **frozen 15 years, no true-up**; states must pass retail allocation; default = all LSEs by peak-load share |
| Who has signed | **No committed large-load counterparties.** PJM: "state action will be essential" |
| Interconnection sweetener | **None** (not even an unaccelerated-timeline assurance) |
| Supply-side under-delivery penalty once running | **Little** |
| Next BRA even with backstop | PJM projects it **"may clear short"** |
| Board override of subscription design | **27 Jul 2026** decisional letter; FERC file **31 Jul 2026** |
| IRAS | Loads **>50 MW** after 2027/28 not covered by central procurement / self-supply / bilateral → **non-firm, curtailed first**, ahead of paid pre-emergency DR |
| 2029/30 class ratings posted | **7 Aug 2026** — again summer-only ("endless summer") |
| Remaining BRA parameters | **31 Aug 2026** |

**Governance votes that already rejected the fix** `[1×: SemiAnalysis]`

| Date | Action | Result |
|---|---|---|
| 2023 | PJM proposes two-season capacity market | Withdrawn after IMM "needs more development"; annual-only package filed |
| Jan 2024 | FERC | Approves annual-only; declines to require seasonality |
| Sep 2024 | IMM winter-capability note | **$2.7B / up to $8.0B**; standing rec: assign excess winter CIRs immediately |
| May 2025 | PJM sensitivity | Winter capability **8,561 MW** above summer ratings |
| May 2025 | Members | **3.699 / 5** sector-weighted votes to defer adjacent transmission work until a seasonal construct is taken up |
| Jul 2025 | ELCC task force Package C (winter ratings) | **178–54, 77%** |
| 20 Aug 2025 | Senior committee | Kills Package C at **30.7%** weighted vote |
| Dec 2025 | E3 review | Seasonal or daily ratings = consideration **4 of 14**. No vote since |
| End-Sep 2026 | FERC | Governance-reform deadline or FERC intervenes (reactive powers; not strictly about auctions/modelling) |

**Fleet / auction identity (2026/27 worked example)** `[1×: SemiAnalysis]`

| Layer | MW |
|---|---|
| Whole-system RRS requirement (Assumed Fleet) | **146 GW** |
| FRR self-supply obligation (~8% of system) | **~12 GW** |
| BRA target | **134 GW** |
| BRA cleared | **134.3 GW** (−0.2 vs target) |
| FRR committed | **12 GW** (+0.3 vs obligation) |
| System vs whole-system requirement | **+0.1 GW** (FRR over-delivery > BRA miss) |

**Model-validation residuals (2028/29)** `[1×: SemiAnalysis]`

| Metric | SemiAnalysis | PJM | Delta |
|---|---|---|---|
| Solved peak | 162,107 MW | 162,063 MW | +44 MW / +0.027% |
| IRM | 19.95% | 20.0% | −0.05 pp |
| LOLE at PJM solved load | 0.09921 | 0.09988 | −0.7% |
| ELCC class ratings (20 classes) | — | — | all within 1.8 pp |
| EUE at solved load | 1,808.8 MWh/yr | 1,755.6 | +3.0% |
| Unallocated accredited UCAP | 3,546 MW of 154,234 MW | — | carried outside hourly physics |

**Cross-market design (why the same GW of growth costs more in PJM)** `[1×: SemiAnalysis]`

| Market | Share of fleet in the marginal-priced residual | New-plant contract tenor |
|---|---|---|
| PJM | **~93%** | 1 year (new = existing) |
| MISO | **~15%** residual (86% of 2025/26 summer requirement outside the auction) | utility self-supply / bilateral |
| NYISO | monthly rolling | — |
| CAISO | bilateral | — |
| ERCOT | none (energy-only) | — |
| GB / Ireland / Italy / Japan | centralized, but new plants **10–20 years**; existing 1 year | Japan added a 20-year new-entry auction after concluding whole-fleet one-year terms build nothing |

## Contradiction Check

No live thesis is directly falsified. The source revises the *size and incidence* of the PJM shortfall, not the existence of a queue/COD problem.

- **[[Theses/NBIS - Nebius Group]] §Outstanding Questions #1 / §Bear Case #1 / §Risks #1 / §Conviction Triggers → LOW if Q3 2026 active-power build misses by >20%.** Philadelphia 1.2 GW and the second Pennsylvania gigawatt site sit inside PJM. The source does not print an NBIS megawatt, COD, or basis figure, so no trigger fires. It does change the mechanism: the 6.8 GW "need" PJM is using to justify a 15-year backstop is ~3 GW after remodel, the backstop buys no interconnection acceleration, IRAS makes participation strictly dominated by self-supply/BTM, and "many datacenter developers have written off PJM." That is a watch on the power-build trigger (dir=watch, not crossed) and a confirmation that announced/contracted MW ≠ energized MW — the same distinction Q#1 already demands. The 24–48 month interconnect queue in the thesis remains; this source adds that PJM's own "we are short" signal is a noisy, winter-biased RRS output, not a physical census of existing plants.
- **[[Theses/NVDA - Nvidia]] §Risks #11 (third-party AI-infrastructure financing / siting friction).** No `## Conviction Triggers` to test. The source is a siting-friction datapoint for the largest US ISO: ratepayer backlash is already political (governor price caps, FERC comment window, IRAS litigation risk), and the Board design is "designed to dissuade new large loads from joining." Supports the financing-layer caveat that an order booked is not a delivered rack; does not touch CUDA, ASIC, or the $500B MOU numerics.
- **[[Theses/SPCX - SpaceX]] §Risks "Power architecture" / §Conviction Triggers (YE26 nameplate, CSA duration, Connectivity margin).** Memphis / Colossus is not PJM. No trigger handle is touched. The BTM/write-off paragraph is consistent with the thesis's "islanding + 24–48 mo interconnect" risk but is not a named-observable print on 2 GW or CSA duration.
- **[[Sectors/Data Center Power & Cooling]] §Macro shifts #1 and §Key industry questions (PJM 8+yr queue, 2027/28 BRA ~6.6 GW short, "grid constraint forces density up").** The queue, RRI withdrawal, and zero energized fast-track megawatts *support* the physical-constraint read. The 6.6–6.8 GW BRA shortfall as a *reliability* number is challenged: remodelled, the 2028/29 emergency target is ~3 GW, and 2025/26–2026/27 "shortfall" was an accreditation miss on the existing fleet. The sector question already posed by [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]] — is the investable variable nodal/temporal/market-design, and what is the ratepayer-cost *sign*? — is answered here with a specific sign: the $12B was market-design plus modelling, not inherent to load growth. Same growth in a split new/existing auction does not reprice the entire fleet.
- **[[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]] (same publisher, eight days earlier).** The Aug 13 note used PJM's 2027/28 BRA short (~6.6 GW, 14.4% vs 20% target) as corroboration of negative accredited headroom and a structural generation shortage forcing BTM. This Aug 16 note says a material fraction of that accredited shortfall is an RRS input error. That is a same-source revision of the *accreditation arithmetic*, not a withdrawal of the BTM conclusion: this piece independently predicts BTM/other-ISO defection because the backstop has no interconnection sweetener, unknown state-by-state cost, IRAS curtailment, and pay-as-bid price opacity. Hold both: physical COD/queue/turbine-lead-time constraints remain; do not treat PJM's 6.8 GW backstop target as a clean generation-gap observable.
- **[[Theses/NET - Cloudflare]] / [[Theses/TSM - Taiwan Semiconductor]].** No load-bearing overlap. NET's edge/PoP footprint is not a PJM large-load interconnection story. TSM conviction triggers (GM, HPC growth, Arizona, CoWoS) are untouched; any demand second-order (delayed PJM halls → delayed GPU installs) is too many steps to register as a contradiction.

## Source Excerpts

> "PJM asymmetrically applies ambient derates to the ICAP of unlimited resource classes when temperatures rise but does not apply ambient uprates when temperatures fall." — E3, December 2025 evaluation, quoted by SemiAnalysis. `[1×: SemiAnalysis / E3]`

> "Because PJM does not have jurisdiction to allocate retail costs directly to individual data centers, state action will be essential." — PJM backstop filing, quoted. `[1×: SemiAnalysis / PJM FERC filing]`

> The Board rejected the members' two-thirds-supported subscription framework because it "would not provide sufficient assurance that capacity equal to the identified near-term shortfall would actually be procured." — PJM Board decisional letter, 27 July 2026. `[1×: SemiAnalysis / PJM Board]`

> Pay-as-bid sellers "are more likely to offer the expected clearing price," and market-power mitigation in this setting is "difficult and ineffective." — PJM witness in the FERC filing. `[1×: SemiAnalysis / PJM FERC filing]`

> IMM standing recommendation, September 2024: "There is no reason that excess winter CIRs cannot be assigned to these resources immediately." Cold-air-only bill cut: $2.7B with reserve margin held fixed, up to $8.0B otherwise. `[1×: SemiAnalysis / PJM IMM]`

> "If we are even half right, we need to change this modelling urgently to avoid further waste and create a clearer signal of what new capacity is required to enable PJM to grow once again." — SemiAnalysis conclusion. The authors flag that key inputs are not public and the reconstruction is "at best a good approximation." `[1×: SemiAnalysis]`

SemiAnalysis will file this analysis in the FERC comment docket (closes 21 August 2026, 17:00 Eastern). Board path they name: file improved modelling criteria at FERC on the same fast-path used to install the current rules in 2023 and to launch the backstop in July 2026; FERC accepted seasonal accreditation at MISO in 2022; Package C winter-ratings text is already written; crediting mandated winterization has not been drafted (closest attempt was the IMM's proposal to delete the storm data outright, refused in the same session). Loosely held: cancel the emergency auction and use direct capacity contracting inside accelerated interconnection agreements; if kept, pay the residual from existing demand and lower the BRA price cap further, which would de facto split existing and new auctions. Datacenters, in their framing, are how electricity becomes cheaper — by paying down high system costs on economies of scale — if governors and customer advocates fix the bureaucratic failure first.
