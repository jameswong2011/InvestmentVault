---
date: 2026-08-16
tags: [research, fuel-cells, natural-gas, SOFC, BE, data-center-power]
sector: Natural Gas Fuel Cells
ticker: BE
source: 'https://www.bloomenergy.com/resources/#whitepapers'
source_type: deep-dive
propagated_to: [BE]
---

# Bloom Energy Whitepapers — vendor corpus vs the investable claim

## Thesis Delta

Consensus prices [[Theses/BE - Bloom Energy]] as a durable AI-power platform whose own literature proves SOFC superiority on efficiency, cost, emissions, and reliability. This corpus — seven listed whitepapers plus the Feb-2026 Energy Server 6.5 datasheet, the emissions technical note, the AlwaysON microgrid overview, and the electrolyzer product page — implies the opposite structure: Bloom sells a **time-to-power and criteria-pollutant product**, and every economic exhibit that looks like a TCO win is conditioned on (a) comparing 54% SOFC to **open-cycle** turbines / simple-cycle microturbines rather than combined-cycle, (b) **$5.00–$9.50/MMBtu** delivered gas rather than the $2.00–2.50 contracted BTM gas the thesis already flags, and (c) assigning a large **opportunity-cost** line to grid delay. Strip those three modelling choices and the whitepapers become a permitting-and-schedule brochure, not a layer-monopoly proof. They also silently concede the load-following product is **not a pure SOFC**: 40→100% step response is carried by **supercapacitor banks**, then the stack recharges them — the same pairing already in [[Research/2026-06-06 - 800VDC Revolution Part 1 - Datacenter Layout and Equipment Impact - deep-dive]] as the ~3 MW fuel-cell + ~2 MW supercap "Energy Stamp."

## Summary

Bloom's resources library lists seven whitepapers. Four of those (the September 2025 AI-power paper, *Resilient Microgrids*, *The Growing Demand for Resiliency Solutions*, *Evaluating the Cost of a Net-Zero Future*) sit behind lead-gen gates; their arguments are reconstructed below from Bloom landing-page copy plus independent close-reads that quote the September 2025 paper directly. The remaining papers and the technical notes were extracted from the live PDFs.

Taken as a single vendor argument, the corpus has one spine: **the grid cannot deliver firm, dispatchable, low-NOx megawatts on a 2026–2028 clock, so a factory-built, non-combustion, natural-gas SOFC module is the only commercial object that can**. Every paper is a different customer-mask on that spine — AI datacenters (September 2025), utilities and variable loads (February 2024 *Be Flexible*), RNG project developers (April 2024 *Power Crunch*), C&I microgrids (AlwaysON overview), California ratepayers (net-zero cost note), and hydrogen optionality (electrolyzer page). The product underneath does not change: a ceramic-electrolyte stack that internally steam-reforms methane to hydrogen, oxidises it electrochemically at >800 °C, and rejects a nitrogen-free, high-purity CO₂ stream plus high-grade heat.

What the corpus does *not* do is the thing a buyer of [[Theses/BE - Bloom Energy]] at ~12× forward sales needs it to do. It never compares SOFC to a **GE 7HA-class combined-cycle** plant at contracted BTM gas. It never publishes stack replacement cost, degradation slope, or the kW-definition that would reconcile the Feb-2026 **325 kW** Energy Server 6.5 nameplate with the thesis's **~850 kW module / 118 modules per 100 MW**. It never shows a Tier-IV (99.995%) primary-power array at 100 MW–1 GW. It treats hydrogen, biogas, and CCUS as a "pathway" while every worked example is pipeline natural gas. Read as primary evidence, the papers corroborate [[Theses/BE - Bloom Energy]] §Insight 1 (time-to-power arbitrage) and §Insight 3 (this is a natural-gas company) and leave §Insight 2 (unaudited backlog) and the Value-Layer-Monopoly WEAK FIT untouched.

## Framework / Mental Model

**Vendor frame — "time-to-power + non-combustion + fuel flexibility."** Bloom's papers repeatedly score generation options on four axes it controls the weights of:

| Axis | Bloom's preferred scoring | What the axis actually measures |
|---|---|---|
| Time-to-power | 50–90 days / "months not years" vs multi-year interconnect and turbine backlog | Schedule option value, not LCOE |
| Electrical efficiency | 53–54% LHV net AC, flat to 30% load | Fuel burn at a stated gas price; collapses vs CCGT |
| Criteria pollutants | NOx ~0.003 lb/MWh, SOx/PM near zero, CARB DG-certified | Air-permit option value in non-attainment basins |
| Fuel flexibility | NG today, biogas / H₂ / CCUS "pathway" | Real option that is currently out of the money |

The investable inversion is to **re-weight the same axes**. Time-to-power is a wasting asset as [[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]] already shows a crowded BTM kit list (Bloom, INNIO, Wärtsilä, Bergen, secondary-market turbines). Efficiency only produces a fuel-cost wedge if gas is expensive *and* the alternative is simple-cycle. Criteria-pollutant advantage is real and is the one axis turbines cannot easily copy without SCR + permitting time. Fuel flexibility is a slide, not a 2026 cash-flow line — matching §Insight 3.

**Chemistry frame — which fuel-cell is even in the natural-gas race.** DOE's technology comparison is the outside-view table the whitepapers never print in full:

| Type | Electrolyte / temp | Electrical eff. (LHV) | Fuel it actually wants | Stationary role | Binding constraint |
|---|---|---|---|---|---|
| PEM | PFSA, <120 °C | ~60% on pure H₂; ~40% reformed | High-purity hydrogen | Backup, mobility, short-duration | H₂ purity + PGM catalyst |
| PAFC | H₃PO₄, 150–200 °C | ~40% | Reformed NG | Doosan-style multi-MW CHP (Korea) | Cost, start-up, sulphur |
| MCFC | Molten carbonate, 600–700 °C | ~50% | NG / biogas | FuelCell Energy SureSource | Corrosion, low power density |
| SOFC | YSZ ceramic, 500–1,000 °C | ~60% DOE / 53–54% Bloom claimed | NG, biogas, H₂ | Bloom Energy Server; Ceres/Doosan/Elcogen stacks | Thermal cycling, start-up, limited shutdowns |

Natural-gas stationary power is a **high-temperature** game (SOFC/MCFC/PAFC). PEM is a hydrogen product wearing a fuel-cell label. Any "fuel cell TAM" that mixes Plug/Ballard automotive PEM with Bloom's NG-SOFC is a category error — the two do not compete for the same electron.

## Evidence

**Product as specified (Energy Server 6.5, Feb 2026 datasheet)**

| Spec | Value | Tag |
|---|---|---|
| Nameplate | 325 kW net AC; 3-ph 480/415/400 V; 50/60 Hz | [IR] |
| Fuel | Natural gas, 12–18 psig (15 nominal) | [IR] |
| Water | None in normal operation | [IR] |
| Electrical efficiency | 65–53% LHV net AC (range, not a single point) | [IR] |
| Heat rate | 5,811–7,127 Btu/kWh HHV | [IR] |
| Thermal / total | >36% exhaust heat @ >350 °C; >90% combined | [IR] |
| CO₂ | 679–833 lb/MWh (308–378 kg/MWh) | [IR] |
| NOx / CO / VOC | 0.003 / 0.013 / 0.01 lb/MWh | [IR] |
| Physical | 28,745 lb; 29'5" × 4'4" × 8'2"; <65 dBA @ 10 ft; −20 to 45 °C | [IR] |
| Installed base claimed | >1.5 GW, 1,200+ sites | [IR] |
| CARB | DG Certification EO DG-058 | [IR] |

**Load-following vs simple-cycle microturbine (Feb 2024 whitepaper, Table 1)**

| Metric | On-site microturbine (aeroderivative) | Bloom SOFC | Tag |
|---|---|---|---|
| Efficiency @ full load | 37.1% | 54% | [1×: Bloom WP Feb-2024] |
| Efficiency @ 30% load | 25% | 53% | [1×: Bloom WP Feb-2024] |
| CO₂ @ full / 30% load | 1,095 / 1,620 lb/MWh | 800 / 815 lb/MWh | [1×: Bloom WP Feb-2024] |
| NOx / CO / VOC | 0.85 / 0.52 / 0.175 lb/MWh | 0.0017 / 0.012 / 0.01 | [1×: Bloom WP Feb-2024] |
| Step response shown | n/a (mechanical inertia) | 40→100% with supercaps; extreme-case 2,000%/min | [1×: Bloom WP Feb-2024] |

**Emissions vs combustion (emissions technical note)**

| Pollutant | Bloom | Gas turbine + SCR | Gas engine | Bloom vs turbine | Tag |
|---|---|---|---|---|---|
| Efficiency | 54% | 36% | 46% | — | [1×: Bloom TN] |
| CO₂ lb/MWh | 818 | 1,238 | 957 | −34% / −14% | [1×: Bloom TN] |
| NOx lb/MWh | 0.003 | 0.078 | 0.085 | −96% | [1×: Bloom TN] |
| SO₂ lb/MWh | <0.001 | 0.036 | 0.007 | >99.9% | [1×: Bloom TN] |
| PM lb/MWh | None | 0.063 | 1.93 | 100% | [1×: Bloom TN] |
| Diesel genset CO₂e | — | — | 1,243 lb/MWh (Tier 2) | Bloom 818 | [1×: Bloom TN] |
| US DC diesel capacity | — | — | ~55 GW by 2024, ~3× 2018 | — | [1×: Bloom TN / betterdatacenterproject] |

**Worked economics inside the papers (all Bloom-assumed)**

| Case | Setup | Result Bloom prints | Hidden drivers | Tag |
|---|---|---|---|---|
| Flagship AI WP (Sep 2025) | 175 MW facility, 5 years, vs gas turbines | $70–100M fuel savings | **$5.00/MMBtu** gas; 54% vs **35–40% OCGT**, not 54–57% CCGT; 99.9% uptime (Tier III) | [web: sheephillgroup.com] [web: utilitydive.com] |
| Retail *Be Flexible* | CA store, PG&E B-19S, 15-yr amortisation | "up to 50%" vs grid; demand-charge wipe | **$9.00/MMBtu** delivered gas; CA tariff structure | [1×: Bloom WP Feb-2024] |
| 10 MW AI hall | 15-yr delivered cost | $163M Bloom vs $227M utility (28%) | **3 years of grid unavailability** priced at $200/kW-mo Silicon Valley rent + 30% opex; 12.5¢/kWh grid @ 3.5% escalate; **$9.50/MMBtu** gas | [1×: Bloom WP Feb-2024] |
| RNG *Power Crunch* | Process power + CHP heat vs CA grid | CI ~25% below grid; ~40% with heat; 85% with CO₂ capture | GREET CA-grid baseline; 45Z / 45Q / LCFS stacking | [1×: Bloom WP Apr-2024] |

**Electrolyzer page (SOEC, not the NG-SOFC cash business)**

| Claim | Value | Tag |
|---|---|---|
| NASA Ames demo | 4 MW, ~2.4 t/day H₂, installed in 2 months | [IR] |
| System energy | 37.5 kWh/kg H₂ (INL pilot); range 37–44 | [IR] |
| PEM / alkaline | 52 / 54 kWh/kg | [IR] |
| Learning rate claimed | 28% per doubling vs 13% PEM / 9% alkaline | [IR] |
| Materials | No PGMs; "2 GW SOEC-equivalent" of SOFC fleet experience | [IR] |

**Module-size reconciliation (partially resolved by the 2022 microgrid paper)**

| Source | Unit | Implied 100 MW count |
|---|---|---|
| *Resilient Microgrids* (2022) | 25 W cell → **50 kW independent power module** → **200 / 250 / 300 kW Energy Server** | ~333–500 servers @ 200–300 kW |
| Energy Server 6.5 datasheet (Feb 2026) | 325 kW nameplate | ~308 servers |
| [[Theses/BE - Bloom Energy]] §Business Model | ~850 kW "module"; 118 modules / 100 MW | 118 |
| 800VDC research "Energy Stamp" | ~3 MW fuel cell + ~2 MW supercap | ~33 stamps |

The 2022 paper and the 2026 datasheet agree the *server* is a ~200–325 kW cabinet. The thesis's 850 kW "module" and the ~3 MW Energy Stamp are multi-server blocks, not the shipping SKU. A 100 MW site is ~300+ cabinets, not 118 — which is the scale objection (unit count vs two gas turbines) in sharper form.

## Key Segments

### 1. *Fuel Cells: A Technology Whose Time Has Come* (Sep 2025) — gated flagship

Landing-page title on the resources page is "Fuel Cells: The Power Advantage for AI Data Centers"; the paper itself is *Fuel Cells: A Technology Whose Time Has Come*, authored by KR Sridhar and Peter Gross. Access is a form gate. Reconstructable claims, quoted by Utility Dive (sponsored) and dissected by SheepHill's March 2026 initiating coverage:

- Power, not chips, is "the #1 constraint on digital infrastructure growth."
- SOFC is 15–20% more efficient than "most" open-cycle gas turbines or reciprocating engines; 54% vs 35–40% is the comparison pair.
- That efficiency "reduces fuel consumption"; "capital cost advantages over gas turbines and engines grow even stronger if customers require higher availability."
- 1.5 GW deployed, 1,200+ sites, "hundreds of megawatts" already in datacenters — the commercialisation-complete claim.
- Reliability marketed at 99.9% (three nines).
- Fuel-savings exhibit: $70–100M over five years on a 175 MW site at **$5.00/MMBtu**.

SheepHill's technical appendix is the only independent line-by-line we have on this paper, and it lands on the same three objections already in [[Theses/BE - Bloom Energy]]: the $5 gas case is "overly punitive" versus $2.00–2.50 BTM contract gas; the turbine comparator is the wrong machine (OCGT / RICE, not 7HA.02 CCGT at 54–57%); 99.9% is Tier III, not the 99.995% / N+3–N+4 hyperscale spec. The paper is therefore best read as a **sales leave-behind for time-to-power buyers**, not as engineering evidence that SOFC wins a cost-of-energy bake-off at GW scale.

### 2. *Load Following Solid Oxide Fuel Cell* (Feb 2024) — the *Be Flexible* paper

This is the most technically specific document in the public set. Historical Energy Servers were baseload boxes. Two internal changes — longer stack life plus balance-of-plant work driven by a digital twin of field data — are said to have unlocked controlled ramp. The demonstration architecture is explicit: **fuel cell + inverter + supercapacitor banks**, with an AI-load simulator (controllable resistor, computer-generated amplitude/frequency/duty cycle) stepping 40→100%. The caps take the instant edge; the stack then carries the load and recharges the caps; on the way down the stack drops to 40% "instantaneously." Extreme-case slope shown: 2,000%/min. Inverter output claimed to meet ITIC, IEC 62040, and SEMI; frequency held inside a droop band.

The part-load table is the paper's sharpest claim and its most revealing comparator. Bloom holds 54% → 53% from full load to 30% load; the aeroderivative microturbine they chose falls 37.1% → 25%, so CO₂ blows out from 1,095 to 1,620 lb/MWh while Bloom stays ~800–815. That is a real physical difference between a solid-state electrochemical converter and a rotating machine. It is also the **wrong rotating machine** for a 100 MW+ AI campus, which specifies combined-cycle or large aero derivatives with HRSG, not a Capstone-class microturbine.

Economics are CA- and delay-driven. Retail: wipe PG&E B-19S energy *and* demand charges, optionally export ~150 kW × 5 h × 5 months at $50/MWh, at **$9/MMBtu** delivered — "up to 50%" vs the grid. 10 MW AI hall over 15 years: $163M vs $227M. Decompose the $227M: $177M is 15-year grid energy at 12.5¢ escalating 3.5%, **$50M is three years of unpaid Silicon Valley rent at $200/kW-month**. The 28% "saving" is mostly **avoided delay**, not cheaper electrons. Change the delay from 36 months to 12, or the rent from $200 to colo-market $80, and the exhibit flips. Gas at $9.50/MMBtu is more than 3× current Henry Hub and ~4× the $2–2.50 BTM number in the thesis.

FOTM use-case (duck curve / CAISO net-load ramp) is asserted, not sized. No utility has been shown running *Be Flexible* as a system-level duck-curve asset at scale in this paper.

### 3. *The Power Crunch: Meeting Critical Path RNG Power Demands While Decarbonizing* (Apr 2024)

A 7-page Canva-built sales piece aimed at renewable-natural-gas developers, not datacenters, but it is the cleanest statement of Bloom's **grid-as-critical-path** doctrine. NERC 2023 LTRA: every US state is in some resource-adequacy risk bucket 2024–2028. Supporting colour: 19 GW of 2022 additions delayed; <6% of solar/wind clears the interconnection queue; median interconnect time doubled from <2 years (2000–07) to ~4 years (2018–22); coal 280 GW (2014) → 195 (2023) → ~90 (2035); US datacenter capacity 5,319 MW (2022) → >24,000 MW (2029); 670 miles of transmission completed in 2022 against a DOE GDO need of 47,300 miles by 2035; $3.9 Tn of grid capex to 2050; peak demand +38 GW through 2028.

The RNG-specific hook: a dairy / landfill / wastewater project cannot wait four years for a feeder, and its LCFS / 45Z cash flow is a function of carbon intensity. Bloom claims process electricity CI ~25% below the CA GREET grid average, ~40% with digester/upgrader heat, and ~85% if the nitrogen-free anode exhaust is captured alongside the already-pure CO₂ from biogas upgrading. That last step is the paper's only novel mechanism: SOFC exhaust is high-purity CO₂ because air-side nitrogen never mixes with the fuel-side carbon — so 45Q / LCFS stacking is *chemically* easier than post-combustion capture on a turbine. The paper does not size how many RNG projects can absorb a multi-MW SOFC, nor what happens to that CI math outside California's LCFS.

For the BE thesis this paper is confirmatory colour on grid delay and a reminder that **the decarbonisation option Bloom can actually ship is RNG + CHP + capture on a niche offtaker**, not green hydrogen at GW. US biogas is ~2.5% of gas consumption per the thesis; this paper does not contradict that.

### 4. *How Bloom Reduces Emissions* (technical note)

The most useful non-gated document after *Be Flexible*. It restates the 54% / 818 lb-CO₂/MWh stack, then puts Solar Titan 130 + SCR and a Bergen B3645V gas engine next to it. Versus the engine — the machine SemiAnalysis keeps grouping with Bloom in the BTM winner list (INNIO / Wärtsilä / Bergen) — the CO₂ edge shrinks to **14%** (818 vs 957). Versus a turbine+SCR it is 34%. The NOx/SOx/PM wipeout is the durable differentiator in both comparisons (96–100%).

Local-air-quality is the note's real product. CARB DG certification (and the BAAQMD / SCAQMD fuel-cell exemptions that ride on it) is why a New Mexico air board can treat a SOFC swap as a NOx solution when turbines fail — the Project Jupiter pattern already in [[Research/2026-08-13 - Datacenter Capacity Cancellation Myth - deep-dive]] (Bloom swap ~37 tpy NOx vs 250–388 tpy turbine request). Diesel displacement is the other local-AQ claim: US datacenter diesel genset capacity nearly tripled 2018–2024 to ~55 GW; a Tier-2 diesel is 1,243 lb CO₂e/MWh and >1,000× Bloom's NOx/SOx. If SOFC is *primary* power, those diesels become less necessary for ride-through; if SOFC is *bridge / supplemental*, the diesel farm stays and the AQ win is smaller than the brochure.

The "low-carbon pathway" close is hydrogen-blend + biogas + CHP + CCUS. Full-H₂ is "modest changes to system design"; internal SMR already makes hydrogen as the working fuel, so blending is a plumbing problem. SOEC is mentioned as the same platform in reverse. None of this is in the FY26 revenue mix.

### 5. Electrolyzer whitepaper — *Unlocking the Power of Heat* (Jul 2021, 11 pp, full PDF)

Opened from Bloom's HubSpot host. Argument: ~80% of clean-hydrogen opex is electricity, so cutting kWh/kg is the only lever that matters. Thermodynamics: liquid-water electrolysis takes ~15.9 MJ/kg; at 850 °C total demand falls to 13.8 MJ/kg, of which 3.5 MJ can be heat and 10.3 MJ electricity. Hardware-test exhibit (Figure 2): SOEC all-electric uses **15% less electricity** than low-temperature PEM/alkaline; SOEC + external steam **29% less**; SOEC + high-temperature external heat **35–45% less**. Operating window 700–850 °C; steam can be made internally or taken from nuclear, industrial furnaces, or solar concentrators.

Use-cases are 2021-vintage pairing slides: (i) oversized solar + battery to keep stacks hot and raise electrolyzer capacity factor (a 10 MW solar plant shown swinging 7,583 kW June vs winter-storm near-zero); (ii) nuclear plants dumping midday surplus MWh *and* waste heat into SOEC (INL collaboration named); (iii) steel/chemical/cement/glass (22% of global CO₂) feeding furnace waste heat back into on-site electrolyzers, with a Baker Hughes compressor/thermal partnership; (iv) CSP heat cheaper than PV electrons on land. Same-platform claim closes the paper: the SOFC fleet is the SOEC manufacturing base.

The 2026 product page's 37.5 kWh/kg INL number and 4 MW Ames demo are later hardware; this 2021 PDF is the *mechanism* paper. It does not size a GW hydrogen book, does not give LCOH at a stated power price, and does not survive 45V-to-2027 / cancelled hubs. Electricity is still the LCOH. Those electrons are being bid into GPU halls.

### 6. *Resilient Microgrids* (2022, 12 pp, full PDF) + AlwaysON overview + 2018 DC paper

The 2022 resiliency whitepaper is now opened (HubSpot). It is a C&I mission-critical brochure, not an AI-campus engineering paper. Frame: grid outages + PSPS + wildfire hardening make "AlwaysON primary power" cheaper than diesel + UPS + cold-start risk. AlwaysON "takes all the functions of today's centralized power infrastructure — transmission, distribution, substations, batteries, back-up — and integrates them into a single distributed generation platform." When the grid is up, the box offsets retail kWh; when the grid dies, it carries critical load with "minimal to no interruption" because the servers are already running — **no cold start**.

**SKU architecture the 2026 datasheet never restates:** one cell = 25 W; cells stack into **50 kW power modules** that "function independently"; modules combine into a **200 / 250 / 300 kW Energy Server**; servers cluster from hundreds of kW to "many tens of megawatts." Field service claim: any failed component removed/replaced in **≤6 hours** once parts and people are on site. Fuel: NG, biogas, or hydrogen; "pathway to upgrade existing systems."

Worked case: unnamed Northern-California test-and-measurement OEM (high-risk wildfire zone) puts **2.8 MW** AlwaysON on the HQ campus after repeated outages were damaging sensitive manufacturing kit; rides through the 2019 PSPS that left millions dark for multiple days. Same pattern as the AlwaysON overview's Hartford 800 kW / Santa Rosa 5.5-day / Delmarva-Sandy / 6.0-earthquake list. Census on the companion overview (500+ MW, 700+ sites, ~$4B third-party financing) is stale versus the Feb-2026 1.5 GW / 1,200+ claim.

A separate 2018 two-pager, *Clean, Reliable Power for Data Centers* (not on the current seven-item list; Sunnyvale letterhead), is the ancestor AI/DC pitch: Equinix/eBay/Uptime quotes ("we don't trust the grid"); Bloom as **primary** power so "the grid becomes the backup"; **"up to 6 9s reliability"**; **"65% starting efficiency"**; diesel gensets removed; "Power Tower" in Korea = **8 MW in a basketball-court footprint**. That 6-nines claim is two orders of magnitude more aggressive than the September 2025 paper's 99.9% (three nines) — the marketing reliability number has *come down* as the product went to hyperscale, which is the opposite of a Tier-IV proof.

*The Growing Demand for Resiliency Solutions* remains a gated one-paragraph landing page. No additional PDF found.

Read-through: these papers prove **C&I ride-through on pipeline gas** and give the only first-party module tree (25 W → 50 kW → 200–300 kW). They do not prove Tier-IV primary power at 100 MW–1 GW. The 2018 "6 nines" line should not be cited as current. EaaS / tax-equity (Southern, Duke, Exelon, Wells, BofA) predates Brookfield — the financing wrapper is the go-to-market, not an AI invention.

### 7. *Evaluating the Cost of a Net-Zero Future* + CA utilities technical note

Both gated. Reconstructable thesis from the landing page and a Trellis/Scribd abstract: utilities face compounding rate pressure from (i) climate-hardening and disaster recovery in the ratebase, (ii) transmission to remote renewables, (iii) load growth from electrification + datacenters, and (iv) the retirement of dispatchable plants. Bloom's insertion is that a behind-the-meter SOFC is a **rate-mitigation and non-wires alternative**, not a generation-fleet replacement — i.e. the customer leaves the utility's capex cycle. This is the FOTM/BTM political argument that sits underneath *Be Flexible*'s duck-curve chapter. No independent numbers were recoverable from the PDFs.

## Contradiction Check

**Supports [[Theses/BE - Bloom Energy]] §Insight 1 (time-to-power arbitrage, not layer monopoly) and the → HIGH/LOW triggers' first half.** Every paper's binding constraint is *schedule*: interconnect queues, 5–7 year turbine waits, 7-year transmission permits, Ireland/Dublin moratoria, 3-year unavailability in the 10 MW exhibit. None of them argue SOFC wins a same-year, same-gas, same-reliability bake-off against CCGT. That is exactly the wasting-asset frame.

**Supports §Insight 3 (this is a natural-gas company).** Every numerical exhibit is pipeline NG. Hydrogen, biogas, and CCUS are closing slides. The electrolyzer page is a 2021-vintage option. CARB / NOx math is a gas-permitting product.

**Challenges the bull-case reading of "54% efficiency" as a durable cost edge.** The papers themselves choose comparators (OCGT 35–40%, microturbine 37%, engine 46%) that maximise the wedge. Versus the engine class SemiAnalysis puts in the same BTM bucket, Bloom's own emissions note says the CO₂ edge is **14%**. Versus CCGT the wedge is zero-to-negative at $2–2.50 gas. The $5 / $9 / $9.50 MMBtu cases are not the AI-campus fuel deck.

**Challenges any reading of *Be Flexible* as "SOFC now load-follows like a battery."** The 40→100% step is a **hybrid**: supercapacitors for the instant, stack for the sustain. That is a real product (and a supercap-content adjacency for the 800VDC chain). It is not evidence the ceramic stack itself is a millisecond device, and it inherits the start-up / thermal-cycle limits DOE lists as SOFC's structural challenges ("limited number of shutdowns").

**Does not touch §Insight 2 (backlog / $20B vs $492.6M RPO) or related-party quality.** Marketing PDFs do not create take-or-pay.

**Does not fire → HIGH.** No audited RPO, no repeat Tier-IV primary-power hyperscale print, no 99.995% array data. The 99.9% claim in the September 2025 paper, if anything, **leans toward → LOW's reliability gap** (Outstanding Question 2).

**New tension with the thesis's own product description.** Energy Server 6.5 is specified at **325 kW**. The thesis's "850 kW module / 118 per 100 MW" and the "Energy Stamp ~3 MW" are not reconciled in any paper. Until IR defines the shipping SKU, MW-per-acre and 50–90-day claims are unanchored.

**Mental-model triggers this corpus activates (for `$sync`, not verdicts):**
- **VLM · layer test — WEAK FIT** — hardware, per-unit cost, stack degradation, contestable vs turbines/RICE; papers never claim non-rivalry.
- **Generalist [G-4] · Perez frenzy** — vendor literature from the installation-phase builder, written to justify the build.
- **Generalist [G-10] · base rates** — 20+ years of stationary-fuel-cell commercialisation, one scaled SOFC OEM, still selling on *schedule* not on LCOE.
- **Generalist [G-13] · expectations** — the price embeds winner-take-most primary power; the papers embed delay-arbitrage vs OCGT.
- **Generalist [G-14] · Jevons** — cheaper/faster on-site MW expands siteable AI load; surplus accrues to the campus, not automatically to the interchangeable kit vendor.
- **Automation lens · energy overlay — Anti-fit/bounded** — Bloom is a demand beneficiary of AI siting, not an operator-automation story.

## Source Excerpts

> "This white paper discusses the latest technological breakthrough in Bloom Energy's solid oxide fuel cell (SOFC) technology to enable load following for both Front-of-the-Meter applications for utilities and Behind-the-Meter applications for various end-use customers such as retail, EV chargers, and AI data centers. We call this solution the Be Flexible™ Energy Server." — *Load Following*, Feb 2024, Abstract

> "To meet that instant demand, the fuel cell system uses Bloom's supercapacitor banks that discharge the power instantly. Once the target power is reached, the fuel cell supports the load and recharges the capacitors." — *Load Following*, p.8

> "Time to power value assumes three years of grid unavailability, data center rental rates of $200/kW-month, and 30% operating costs. … Bloom cost is based on the Be Flexible Energy Server solution with capital and service costs over a 15-year term, and a $9.50/MMBTU average delivered gas price." — *Load Following*, pp.12–13

> "Power availability at sufficient quantity and quality is no longer a given when developing RNG projects – it is now a critical path item driving project viability." — *Power Crunch*, Apr 2024

> "Because carbon and nitrogen never mix in Bloom's fuel cells, it is both feasible and cost effective to capture CO2." — Emissions technical note

> "Nameplate power output (net AC) 325 kW … Cumulative electrical efficiency 65-53% (LHV net AC) … CO2 @ stated efficiency 679-833 lbs/MWh … Bloom Energy has deployed over 1.5 GW across 1,200+ sites." — Energy Server 6.5 datasheet, Feb 2026

> "The Bloom Electrolyzer is producing hydrogen at 37.5 kWh per kilogram of hydrogen at the system level. Alternative efficient electrolyzer technologies, such as PEM or Alkaline, consume as much as 52 – 54 kWh per kilogram." — Electrolyzer product page (INL)

Access notes — what was actually opened vs reconstructed:

| Document | Opened? | How |
|---|---|---|
| *Load Following Solid Oxide Fuel Cell* (Feb 2024, 13 pp) | **Yes — full PDF** | bloomenergy.com/wp-content/uploads/load-following-solid-oxide-fuel-cell.pdf |
| *The Power Crunch* / RNG (Apr 2024, 7 pp) | **Yes — full PDF** (image-heavy Canva; text extracted) | bloom-energy-whitepaper-time-to-power.pdf |
| *How Bloom Reduces Emissions* technical note | **Yes — full PDF** | bloom-energy-how-bloom-reduces-emissions-technical-note.pdf |
| Energy Server 6.5 datasheet (Feb 2026) | **Yes — full PDF** | bloom-energy-server-datasheet-feb-2026.pdf |
| Electrolyzer WP *Unlocking the Power of Heat* (Jul 2021, 11 pp) | **Yes — full PDF** (HubSpot host, not the gated `#download`) | f.hubspotusercontent30.net/…/Be-Electrolyzer-White-Paper_07142021.pdf |
| *Resilient Microgrids* (2022, 12 pp) | **Yes — full PDF** (HubSpot host; bloomenergy.com landing page is gated) | f.hubspotusercontent30.net/…/2022-Whitepaper_Resilient-Microgrids.pdf |
| *Clean, Reliable Power for Data Centers* (2018, 2 pp) | **Yes — full PDF** (older DC paper, not on the current 7-item list) | bloom-data-center-whitepaper.pdf |
| AlwaysON Microgrid Solution Overview (2022) | **Yes — full PDF** | bloom-energy-microgrid-overview.pdf |
| Electrolyzer / Energy Server landing pages | Yes — HTML | public product copy |
| *Fuel Cells: A Technology Whose Time Has Come* (Sep 2025) | **No — form gate** | reconstructed from Utility Dive sponsored write-up + SheepHill initiating coverage quoting the PDF |
| *The Growing Demand for Resiliency Solutions* | **No — form gate** | landing-page paragraph only |
| *Evaluating the Cost of a Net-Zero Future* | **No — form gate** | landing-page paragraph + Trellis/Scribd abstract |
| CA utilities technical note PDF | **No — form gate** | image-caption fragments (CPUC R.18-10-007 / SCE wildfire $582M — 2018–19 vintage) |

The September 2025 flagship is the one paper that still matters and is still unread first-party. Drop a downloaded copy in `_Inbox/` and it can replace the SheepHill/Utility Dive reconstruction.
