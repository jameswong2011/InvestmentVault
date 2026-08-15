---
publish: false
date: 2026-08-05
updated: 2026-08-14
tags: [research, data-center-power, AI-infrastructure, power-markets]
sector: Data Center Power & Cooling
source: '/Users/alexcohen/InvestmentVault/_Inbox/Power 2026 by Neel Somani - Electricity Pricing in the Age of AI.md'
original_source: 'https://power2026.ai/'
source_type: deep-dive
propagated_to: [IREN, NBIS, VRT, CRWV, BE]
---

# AI Data Center Power Markets and Electricity Pricing

## Thesis Delta

Consensus treats AI power as a national shortage that mechanically raises household electricity prices and validates every “power bottleneck” equity — [[Theses/IREN - IREN Limited]] headline gigawatts, [[Theses/BE - Bloom Energy]] time-to-power, [[Theses/VRT - Vertiv Holdings]] “benefits regardless of direction,” [[Theses/CCJ - Cameco]] AI-baseload uranium floor, [[Theses/LNG - Cheniere Energy]] Henry Hub bid from data centers. This source implies the investable variable is **locational and temporal scarcity** (bus, binding line, merit-order unit, market-design rule, interconnection firmness, bankable duration), so owned-deliverability and deployment-speed cases strengthen only after nodal economics, fuel exposure, and multi-year commitments survive a demand air pocket ([G-3], [G-13], VLM political-ceiling hypothesis).

## Summary

Neel Somani’s *Power 2026* primer is a first-principles chain from commodity identity to AI-data-center site finance to ISO production-cost pricing. Electricity cannot be stored or shipped as freely as crude: generation and consumption must balance continuously at thousands of buses subject to line ratings, generator limits, storage state, I²R losses, outages, and reliability rules. In the author’s competitive-market model a uniform clearing price equals the marginal cost of the last feasible megawatt-hour, so a data center does not have one generic “power cost.” Cost depends on which node it occupies, which unit is on the margin each hour, whether a line binds, how renewables and batteries reshape the merit order, and how actual load differs from the day-ahead schedule. Buying 1 MWh on a wholesale market does not confer the right to plug in 1,000 GPUs; the independent system operator (or a balancing authority) dispatches generation to hold frequency at 60 Hz, and extreme imbalance produces brownouts or blackouts rather than a private shortfall [1×: Power 2026].

That mechanism breaks the linear claim that more data centers always raise household bills. A new load can raise the locational marginal price or the capacity/resource-adequacy requirement when it binds transmission or forces inefficient units to run. It can also lower average system cost by sharing fixed transmission and distribution expenses, absorbing otherwise-curtailed wind or solar (including ERCOT hours that print negative because Production Tax Credit plus startup/shutdown costs keep turbines spinning to about −$20/MWh), keeping an efficient combined-cycle plant online through a low-demand afternoon so evening startup is avoided, or selling interruptible load as an ancillary service the way Bitcoin mines were discussed as Texas-grid stabilizers [1×: Power 2026]. The sign is a function of location, hour, market design, and flexibility. The source’s contribution is not a bullish forecast for power equities; it is a decomposition of where scarcity rents actually accrue and where political responses (White House Ratepayer Protection Pledge, Power for the People Act, municipal bans, off-grid mandates) redistribute or cap them.

Part 1 is a founder/investor operating manual. Plant type is chosen before the site: fuel constrains geography (a gas unit needs pipeline access, often a new lateral), interconnection queues govern grid sales, and behind-the-meter generation can shorten the generator-interconnection path without removing permits, fuel logistics, GPU-hall space, cooling, batteries, redundancy, or load-balancing. Site work is conflict elimination — oil and gas, trona, mines, existing queue positions, wildlife avoidance (Greater Sage Grouse Plan of 2025), water and air rights — using GIS files and, in Washington, EFSEC-style pre-clearance, then a third-party legal report. Land is often bought with equity cash so construction debt can be drawn slowly against contracted cash flow. A nine-figure plant (author’s $300M example, GPUs able to dominate the bill) needs years of locked revenue via a PPA, energy-services or dedicated-supply agreement, or a heat-rate call option sold to a hedge fund that approximates plant economics in exchange for a fixed periodic payment. Banks price the counterparty: an established developer with a prime hyperscaler tenant is ballpark SOFR + 2.25% [1×: Power 2026]. Construction is procurement-constrained: GE Vernova, Siemens Energy, and Mitsubishi Power are described as sold out months to years, with jet engines being converted and parts imported from China. After COD the construction loan is refinanced or the asset is sold to an independent power producer.

The duration mismatch is the vault-relevant claim. The author, from conversations rather than a disclosed survey, reads some major labs as comfortable on power/compute by 2028; the urgent willingness to pay is now, and 6–12 months of demand does not underwrite a multi-year plant loan. SpaceX–Reflection is the short-duration extreme: either party can exit in 90 days, implied ~$5,000/MWh for power bundled with ready GPUs. Anthropic–TeraWulf is the long-duration extreme: $19B, 400 MW, 20 years from H2 2027, implied ~$271/MWh without GPUs but with building and cooling [1×: Power 2026 / napkin]. That pair supports backlog skepticism across [[Theses/BE - Bloom Energy]], [[Theses/CRWV - CoreWeave]], and [[Theses/NBIS - Nebius Group]] and sharpens the funding-duration question in [[Sectors/Neoclouds & GPU-as-a-Service]] and [[Macro & Technology/Sustainability of AI Capex]]. Homer City is the worked physical case: a ~2 GW, three-unit, ~10-heat-rate coal plant in PJM that lost dispatch to 6–7-heat-rate gas and closed in 2023 after ~50 years, now a 4.4 GW / ~$10B gas-plus-campus redevelopment with EQT as fuel partner, Pennsylvania DEP air permit November 2025, a waterway permit, ~1,000 construction workers, and unannounced tenants [1×: Power 2026]. Training still requires co-located, gigawatt-scale GPU halls ([[Theses/NVDA - Nvidia]] rack-scale topology); inference can be routed to whichever cluster sits on cheap power that hour, which is why “inference-first grids” and smaller wellhead generators reappear even though they are not a physically separate US interconnection.

Part 2 is a trader’s pricing model. Each ISO runs a production-cost optimization that minimizes total system cost subject to nodal balance, transmission ratings, generator limits, storage feasibility, and reliability reserves. The Lagrange multiplier on a node’s balance constraint is the locational marginal price. When a line binds, cheap remote generation cannot serve the constrained bus and a local expensive unit sets the incremental price — the two-node textbook: 50 MW line, $10/MWh at B versus $100/MWh at A, 10 MWh of demand at A clears at $10, 60 MWh saturates the line and the last 10 MWh prices at $100 [1×: Power 2026]. Most traders do not trade individual buses; they trade zonal averages. Retail bills add transmission, distribution, and utility overhead that can be the majority of the check, so household rates are not wholesale LMPs. Market design then decides whether inframarginal energy rents, a capacity/resource-adequacy payment, or an energy-only scarcity adder (ERCOT value-of-lost-load construction toward a $5,000/MWh offer-cap example; Alberta scarcity rent under a C$1,000/MWh cap slated to rise) covers the “missing money” that pure marginal-cost pricing does not pay the least-efficient reliability unit. Day-ahead clears the day before physical delivery; real-time re-optimizes every five minutes and settles deviations; weather drives both load and gas. Hedges map to those exposures: zonal forwards, spark and dark spreads, basis/FTRs, peak/off-peak and hour-versus-hour spreads, heat-rate call options. A zonal forward does not fully hedge a specific bus; expected load is not actual load; a plant can be on outage when the hedge assumes output. “Fixed power cost” is a portfolio of partially matched instruments.

The primer is educational, not a forecast. Numerical claims are source assertions (DOE/Goldman citations for the 5% / doubling setup; author’s napkin math on contract implied prices; EIA May 2026 on MISO coal-versus-gas profitability). Its durable use is the checklist: power ownership, interconnection, and turbine scarcity matter only after specifying the node, the market rule, the marginal fuel, the hedge, the counterparty, and the duration.

## Framework / Mental Model

### 1. Commodity identity, residual gas, and the power balance

Three commodity families — energy, agriculture, metals — share a settlement forcing function equities lack. A stock has no date on which a physical buyer refuses an unmoored price; a commodity contract does. Commodities also chain more linearly than corporate cash flows: a well produces crude and methane; crude is globally shippable (Strait of Hormuz concern is a crude-market fact); dedicated gas wells, not associated oil wells, supply most US dry gas; gas is regional unless liquefied. Foreign gas prices have lately exceeded US prices, so the US exports what it can and the domestic residual is what could not physically leave as LNG [1×: Power 2026]. That residual is consumed by industrials (chemicals), residential-commercial heat, and power — the primer’s object.

The identity that must hold at every location:

**Supply = demand + net exports + change in storage.**

Electricity rewrite at a bus, city, or state:

**Generation = consumption + net power exports + change in storage + losses.**

Constraints: transfer capacity (line ratings; thermal expansion can sag a conductor into a tree), storage energy and power limits, and losses that rise with current. Every term is price-sensitive. Higher local price calls less-efficient generation, cuts demand, reduces net exports, and pulls storage. In a competitive market every unit sold in an interval clears at one price equal to the marginal cost of the cheapest producer not yet at capacity. The author’s oil toy: Producer A offers 99 barrels at $5, Producer B the next  at $6; the market price is $6 and B earns zero on the last barrel. Undercutting continues until that equality holds [1×: Power 2026].

Methodology:

1. Choose location and interval. A national annual average erases the binding constraint.
2. Forecast load, renewable output, outages, fuel, storage, and interchange.
3. Enforce the identity plus physical limits.
4. Identify the next feasible action that supplies one incremental MWh.
5. Treat that incremental system cost as the local competitive price.
6. Re-run weather, outage, fuel, load, and transmission scenarios.

Investment translation: a nominally generation-rich region can still be expensive if cheap units sit behind a saturated line (NYISO upstate nuclear versus Manhattan). A generation-poor region can stay cheap if imports are unconstrained. One gigawatt of data-center load has different economics when it absorbs surplus midday wind, requires a new peaker on a hot evening, or can curtail in minutes. Power is a networked dynamical system, not a fungible national commodity ([G-3]).

### 2. Merit order, heat rate, and plant physics

A plant is one or more units. Nearly every US generator above 1 MW appears in EIA-860 (imperfect, sufficient to start). Rank units by marginal cost of the next MWh — the **merit order**. Typical ascending order: solar and wind (near-zero fuel), hydro, nuclear, then gas or coal depending on efficiency and fuel, then oil/diesel peakers. The last unit required is the **marginal unit**; in many hours that is gas, and its offer anchors the uniform clearing price. Uniform-price auctions pay every dispatched unit the clearing price, which is the incentive to produce cheaply.

Heat rate converts fuel heat content to electricity: MMBtu per MWh. Lower is better. 1,400 MMBtu through a 7-heat-rate unit yields 200 MWh — 200 MW for one hour or 100 MW for two [1×: Power 2026]. Variable cost ≈ heat rate × fuel price, plus variable O&M and, where applicable, carbon (California cap-and-trade; RGGI in the Northeast).

Gas-plant physics: compress air, combust methane, expand through a turbine (Brayton cycle), spin a rotor inside a stator. That rotation is how most thermal and hydro generation works; photovoltaics are the exception. A **simple-cycle gas turbine (SCGT)** is that core machine, ~300–400 MW in the author’s sketch. Exhaust is still hot enough to boil water in a heat-recovery steam generator and run a second turbine (Rankine cycle). Combined, that is a **combined-cycle gas turbine (CCGT)** at ~600 MW and a better (lower) heat rate. Separate inefficient peakers, sometimes oil-capable, can push a site toward ~800 MW when prices justify the worse heat rate. Operators run CCGT first and peakers only when the spark spread covers them.

Startup cost (fuel and wear to reach synchronous speed), no-load cost (on but not generating), minimum run time, and ramp rates bend the simple curve. Serving more daytime load can *lower* the 24-hour system cost if it avoids a shutdown-restart of an efficient CCGT — the author’s assigned exercise behind the duck-curve discussion. The plant offer curve slopes up as the operator stacks units from most to least efficient.

![[Power 2026 - Power Plant Offer Curve.png]]

Plant-development overlay: fuel, nameplate, site, pipeline lateral, water, air permit, land rights, EPC, equipment, and grid posture are chosen before any merit-order rent is earned. A low-variable-cost unit is still a bad investment if construction overruns, utilization is low, interconnection slips, or contracted revenue does not cover fixed cost.

Asset underwriting steps:

1. Build the hourly variable-cost curve (heat rate, fuel, emissions, VOM).
2. Add startup / no-load / min-run / forced-outage.
3. Place the unit in the regional merit order under multiple fuel and load cases.
4. Estimate dispatched hours and spark (or dark) spread, not nameplate.
5. Stack capacity, ancillary, hedge, and contract revenues.
6. Compare the cash-flow stack with construction cost, financing, and schedule.

Illustrative plant math the source uses as scale, not a forecast: regional wholesale often $10–150/MWh; 100 MW × 16 hours × $60/MWh ≈ $96,000/day, rounded to ~$100,000 gross [1×: Power 2026].

### 3. Production-cost model and locational marginal price

Named framework: the **production cost model**. Objective — minimize total system production cost (startup + marginal + losses) subject to:

- **Balance:** supply equals demand at each modeled node or zone.
- **Transmission:** flows stay inside ratings.
- **Generator:** output between technical min and max; richer models add unit commitment, ramps, min run, startup.
- **Storage:** charge, discharge, inventory, efficiency.
- **Reliability:** reserves and, in some regions, local-generation requirements (importing is not always allowed to cover the whole obligation).

Solvers: Gurobi, CPLEX. Binary on/off turns the problem mixed-integer; unit commitment (who is on) is combinatorially harder than economic dispatch (how much each committed unit produces). The Lagrange multiplier on a node’s balance constraint is the **locational marginal price (LMP)** — the incremental system cost of one more MWh there. LMP can be decomposed (energy, congestion, loss); the primer treats the shadow price as the traded object.

Power-flow approximation: **shift factors / Power Transfer Distribution Factors**. Inject 1 MWh at one bus and withdraw 1 MWh at another; the linear change in each line’s flow is the shift factor, purchasable from vendors. Exact AC flows are harder.

Welfare justification for cost-minimization: if demand is treated as inelastic (vertical), maximizing the area between supply and demand collapses to pushing the supply curve down. That is why ISOs minimize production cost rather than maximize a more general surplus. The author flags the assumption: demand response exists and pays customers to curtail; data-center interruptibility is the live relaxation.

![[Power 2026 - Supply and Demand.png]]

![[Power 2026 - Inelastic Demand.png]]

![[Power 2026 - Optimized Supply Curve.png]]

Two-node binding-constraint pedagogy:

| Demand at A | Line limit | Dispatch | LMP at A |
|---|---:|---|---:|
| 10 MWh | 50 MW | All imported from $10 B | ~$10/MWh |
| 60 MWh | 50 MW | 50 MW from B + 10 MWh from $100 A | ~$100/MWh |

The price jump is the line binding, not “the nation ran out of megawatts.” Binding constraints are, in the author’s phrase, theoretically the core of what causes prices to increase.

A single-day PCM output averaged across a quarter is a three-month forward-strip estimate; power trades in strips. Full mixed-integer PCM cannot be run across thousands of weather/outage scenarios, so practitioners approximate.

### 4. Market-design taxonomy

The same physics produces different cash flows under different rules.

| Design element | Mechanism | Economic question |
|---|---|---|
| Uniform energy clearing | All dispatched units receive the clearing price | Does the marginal unit leave enough inframarginal rent to cover fixed cost? |
| Capacity market / resource adequacy | Payment for existing | Which assets earn an existence payment even when rarely dispatched? PJM: ISO-run capacity market. CAISO: utilities (PG&E and peers) procure RA bilaterally. |
| Energy-only market | Fixed costs recovered in energy and scarcity prices | Are scarcity rents high and frequent enough to finance reliability? ERCOT, Alberta. |
| Scarcity adder / offer cap | Price rises as reserve margin falls or load is unserved | Does political tolerance permit the prices peakers need? ERCOT VOLL construction toward ~$5,000/MWh; Alberta C$1,000/MWh cap rising. Fabled ERCOT prints to $9,000/MWh are the public memory, not the model’s working cap. |
| Missing-money diagnosis | Pure MC pricing pays the last unit zero quasi-rent | How does this ISO keep the least-efficient reliability unit from retiring and starting a cascade? |
| Day-ahead market | Financial schedule the day before delivery | How much volume and price can be locked before weather and outages resolve? DA for July 2 clears July 1. |
| Real-time market | Re-optimized every 5 minutes | How costly are forecast errors, forced outages, or load deviations? Extra MWh settle at RT. |
| Ancillary services | Fast generation, storage, or curtailable load | Can a data center monetize interruptibility rather than remain a fixed block? |
| Wholesale vs retail | Retail = wholesale + T&D + utility overhead | Are household-bill politics tracking LMP, or socialized fixed costs? |
| Zone vs bus | Traders usually trade zonal averages of thousands of nodal LMPs | How large is the basis between the hedge zone and the physical bus? |

ISO map the source uses:

![[Power 2026 - ISO Map.png]]

| Market | Source characterization | AI/power relevance |
|---|---|---|
| PJM | Most liquid US organized market; capacity market; footprint beyond PA/NJ/MD into parts of IL, KY, MI | Virginia is the US data-center capital; queue, capacity, and transmission set incremental-load cost |
| MISO | Coal retirements, large wind, interchange with PJM; EIA May 2026: MISO coal recently more profitable than gas | Indiana, Illinois, Michigan cited as popular new data-center states; marginal fuel is changing |
| CAISO | NP-15 / SP-15 via Path 15; ZP-26 (Diablo Canyon) no longer heavily traded; no coal; renewables + nuclear + gas; BTM rooftop solar hides load | Duck curve; NP-15 imports hydro from the regulated Pacific Northwest |
| ERCOT | Isolated energy-only market; ~1 GW HVDC to the rest of the US; FERC-light because Texas is a third interconnection beside Eastern and Western | Negative West/North Texas wind; Bitcoin-mine then data-center siting; scarcity spikes |
| SPP | Wind-heavy | Load can raise the value of otherwise-curtailed generation |
| NYISO | Cheap upstate nuclear constrained from Manhattan | Transmission, not aggregate generation, creates nodal scarcity |
| ISO-NE | Winter gas scarcity forces oil | Fuel deliverability changes the marginal unit and the spark spread |
| Southeast / south of PJM | Vertically integrated regulated utilities; fixed allowed margin | Retail-rate and allowed-return logic; weak incentive to cut cost |
| Alberta | Gas-heavy energy-only; AECO vs Henry Hub; $0 daytime floor; SCGT evenings; batteries flattening the spread; market being restructured | Combined Texas energy-only logic + California renewables problem in one ISO |

US topology: Eastern Interconnection and Western Interconnection are separate AC machines linked by limited HVDC (HVDC can join different frequencies; it is expensive). Texas is the third machine. Isolation is why ERCOT can write its own reliability-through-price rules.

### 5. Data-center site-and-finance decision tree

Reuse as a gating sequence:

1. **Define the load.** Training: co-located, high-density, relatively continuous, gigawatt-class ([[Theses/NVDA - Nvidia]] NVL72/NVL576). Inference: smaller clusters, geographically and temporally routable.
2. **Choose grid posture.** Grid-connected, behind-the-meter / co-located, or physically islanded (New Hampshire-style off-grid proposal). Islanding avoids splitting T&D fixed costs and avoids direct electrical demand on the ISO; a gas-fired island still bids for pipeline gas and raises the regional fuel price for grid generators.
3. **Screen the site.** Node, queue position, gas pipeline, water, fiber, land conflicts (minerals, existing projects, sage grouse and other avoidance layers), tax (Virginia Data Center Retail Sales and Use Tax Exemption as the named example), local politics, construction labor. Type of plant first, site second; most offered land fails.
4. **Permits as rights confirmation, not theater.** Air, water, land. Homer City’s binding air-quality permit is the Pennsylvania DEP approval of November 2025.
5. **Secure equipment and EPC.** Turbine, transformer, switchgear, cooling, battery, contractor. Lead times are the critical path. Author policy aside: EPC as part-owner; temporary tolerance of dirtier bridge fuel; private-equity vehicles matched to a 2–3 year demand pulse rather than a startup’s longer life.
6. **Match contract duration to asset life.** PPA / ESA / dedicated supply / hyperscaler or lab tenancy / HRCO. Land in cash; construction debt drawn late.
7. **Underwrite the counterparty.** Headline $/MWh is not bankable if the buyer can exit before amortization or lacks the balance sheet. 90-day mutual out versus 20-year lease is the spread.
8. **Hedge residual risk.** Power level, gas, congestion basis, hourly shape, DA/RT volume mismatch.

The tree separates **willingness to pay** from **bankability**. A customer paying an extreme near-term rate with a 90-day cancellation right is worse construction collateral than a lower-priced 20-year contract. That is the bridge from power mechanics to neocloud/backlog analysis: a contracted megawatt is duration × firmness × credit × node × hedge, not the press-release dollar figure.

### 6. Hedge decomposition and PCM shortcuts

Physical risk → instrument:

- **Power-price level:** buy or sell zonal forwards. Worked consumer hedge: 300 MW continuous for a year, long a 1-year strip at $50/MWh. DA clears $25 → lose $25/MWh on the forward, buy physical at $25, net $50. DA clears $100 → gain $50 on the forward, buy physical at $100, net $50. The forward never delivers electrons [1×: Power 2026].
- **Fuel-price level:** buy gas forwards for a gas plant (sell-power-only leaves the owner short gas).
- **Plant gross margin:** **spark spread** = power price − heat rate × gas price. A 7-heat-rate plant sells a 7-heat-rate spark. **Dark spread** is the coal analog.
- **Effective heat rate:** implied heat rate of a gas unit that earns exactly zero at current power and gas — a dispatch predictor, not a plant spec.
- **Nodal congestion:** basis (long one location, short another) or Financial Transmission Rights whose payoff tracks congestion between two nodes. Flows are emergent; the ISO does not set them directly. Disagreement about which line binds is why basis is a distinct trade from directional zonal.
- **Hourly shape:** on-peak versus off-peak (peak definitions vary by ISO; peaks are the liquid contract); hour-versus-hour; month-versus-month.
- **Forecast error:** DA versus RT. Virtual trading exists to arbitrage DA/RT gaps; the primer names it and does not teach it.
- **HRCO:** sell a theoretical plant’s spark to a fund, receive a fixed periodic premium, use that premium as construction DSCR.

Hedge failure modes: zonal ≠ bus; expected MWh ≠ actual MWh; RT optimization ≠ DA optimization (RT already knows commitment); plant outage when the sold spark assumes generation; gas basis versus Henry Hub (or AECO).

PCM shortcuts when full unit-commitment Monte Carlo is too slow:

| Shortcut | What is frozen | Where it breaks |
|---|---|---|
| Continuous relaxation | Units may be “half on” | Startup economics and min-gen |
| Exogenous interchange | Imports/exports assumed (e.g. NP-15 takes a few GW from the PNW, maybe SP-15) | Flow-driven congestion is the whole trade |
| Predictable batteries | Charge cheap daytime (~$0), discharge evening | Intraday cycling, opportunity sales |
| Merit-order dispatch | Sort remaining units after fixing interchange and storage; last unit sets price | Unit commitment, local RA, startup |
| Ignore or linearize losses | Drop I²R or apply a fixed percent | High-flow hours |

A daily PCM averaged into a strip is how a hyperscaler or a trader turns a structural view into a hedge. Managing that hedge can itself be P&L.

## Evidence

### AI load and development economics

| Source claim / example | Value | Provenance | Analytical use |
|---|---:|---|---|
| US electricity consumed by data centers | ~5% | [1×: Power 2026] citing DOE | Starting load share, not a 2030 forecast |
| Data-center power-demand cadence | Doubling every 2 years | [1×: Power 2026] citing Goldman | High-growth premise; not independently verified here |
| Theoretical crossover with total US generation | Mid-2030s | [1×: Power 2026] extrapolation | Illustrates why physical supply becomes binding if the cadence holds |
| Illustrative new gas plant construction cost | $300M | [1×: Power 2026] | Nine-figure financing requirement; GPUs can dominate the total |
| Established-developer construction debt | ~SOFR + 2.25% | [1×: Power 2026] | Ballpark with a prime hyperscaler anchor |
| Major turbine availability | Months to years of backlog | [1×: Power 2026] | GE Vernova, Siemens Energy, Mitsubishi Power cited as sold out; jet engines and Chinese parts as substitutes |
| Training-load topology | Many GPUs co-located; gigawatt-scale | [1×: Power 2026] | Limits geographic load shifting; binds [[Theses/NVDA - Nvidia]] cluster design |
| Inference-load topology | Smaller, distributable clusters | [1×: Power 2026] | Supports follow-the-cheap-electron routing |
| Author’s AI-lab demand read | Strongest demand is now; some labs comfortable by 2028 | [1×: Power 2026] conversations | Duration mismatch versus multi-year plant underwriting |
| Generator capital scale | $100M+ rotating machines | [1×: Power 2026] | Frequency deviations damage equipment; ISO exists to protect them |

### Generation and plant-unit examples

| Item | Source value | Provenance | Relationship |
|---|---:|---|---|
| Typical gas-unit heat rate | ~7 MMBtu/MWh | [1×: Power 2026] | 1,400 MMBtu → ~200 MWh |
| SCGT output (sketch) | ~300–400 MW | [1×: Power 2026] | Brayton only |
| CCGT output (sketch) | ~600 MW | [1×: Power 2026] | Brayton + Rankine via HRSG |
| Plant with peakers | ~800 MW | [1×: Power 2026] | Higher output, worse marginal heat rate |
| Typical regional wholesale-price range | ~$10–150/MWh | [1×: Power 2026] | Dispersion before scarcity tails |
| Illustrative plant revenue | 100 MW × 16 h × $60/MWh ≈ $96,000/day | [1×: Power 2026] | Rounded by source to ~$100,000 gross |
| Grid frequency | 60 Hz | [1×: Power 2026] | Continuous balance protects rotors |
| EIA-860 coverage | US plants ≳1 MW | [1×: Power 2026] / [web: eia.gov] | Starting inventory of units and heat rates |
| Financial vs physical power | 1 MWh purchased ≠ 1,000 GPUs at 1 MW for one hour | [1×: Power 2026] | Delivery rights ≠ wholesale tickets |
| Nuclear “already big” benchmark | ~1 GW | [1×: Power 2026] | Sets scale for Homer City 4.4 GW |

### Homer City redevelopment case

| Attribute | Historical / new plan | Provenance |
|---|---|---|
| Legacy plant | ~2 GW, three coal units, Pennsylvania / PJM | [1×: Power 2026] |
| Legacy efficiency | ~10 heat-rate coal versus ~6–7 heat-rate gas | [1×: Power 2026] |
| Closure | 2023 after ~50 years; declining dispatch | [1×: Power 2026] |
| Redevelopment | 4.4 GW natural-gas plant and data-center campus | [1×: Power 2026] / [web: homercityredevelopment.com] |
| Estimated construction cost | ~$10B | [1×: Power 2026] |
| Gas partner | EQT Corporation (announced) | [1×: Power 2026] |
| Anchor tenants | Not announced (financing leverage, permit optics, or customer-owned PR) | [1×: Power 2026] |
| Target unit efficiency | ~6 heat rate | [1×: Power 2026] |
| Air-quality permit | Pennsylvania DEP, November 2025 | [1×: Power 2026] |
| Other permit cited | Waterway | [1×: Power 2026] |
| Construction workforce | 1,000 people | [1×: Power 2026] |
| Live risk the author flags | Schedule; things must go “perfectly” at this dollar scale | [1×: Power 2026] |

### Contract-duration and willingness-to-pay examples

| Arrangement | Scale / term | Implied price | Bankability signal | Provenance |
|---|---|---:|---|---|
| SpaceX–Reflection | 90-day termination right either party; power bundled with ready GPUs | ~$5,000/MWh | Extreme near-term scarcity; weak duration for plant debt | [1×: Power 2026] napkin / [web: x.com] |
| Anthropic–TeraWulf | $19B lease; 400 MW; 20 years; starts H2 2027; building + cooling, no GPUs | ~$271/MWh | Lower price, long infrastructure-backed cash flow | [1×: Power 2026] napkin / [web: x.com] |
| Generic hyperscaler / lab PPA | Multi-month to multi-year dedicated $/MWh | Not specified | Longer term improves construction-loan underwriting | [1×: Power 2026] |
| Heat-rate call option | Theoretical plant spark sold for a fixed periodic premium | Plant-specific | Converts merchant gross margin into DSCR | [1×: Power 2026] |
| Author policy vehicle | PE fund with shorter lifespan; EPC as part-owner | n/a | Matches 2–3 year demand pulse, not a 10-year startup | [1×: Power 2026] |

### Market-design and price examples

| Example | Input | Output / implication | Provenance |
|---|---|---|---|
| Two-node congestion | Node B $10/MWh; node A $100/MWh; line 50 MW | 10 MWh at A → ~$10; 60 MWh → line binds, incremental ~$100 | [1×: Power 2026] |
| ERCOT VOLL / offer-cap construction | $5,000/MWh × probability of lost load added to served MWh | Scarcity adder intended to keep peaker economics alive without a capacity market | [1×: Power 2026] |
| Fabled ERCOT prints | $9,000/MWh | Public memory of energy-only tails | [1×: Power 2026] |
| ERCOT negative wind | PTC + startup/shutdown; offers to about −$20/MWh | Paid-to-consume hours; siting magnet for mines then data centers | [1×: Power 2026] |
| Alberta cap | C$1,000/MWh, scheduled to rise | Caps recoverable scarcity rent; units above the cap need other revenue | [1×: Power 2026] / [web: aeso.ca] |
| Alberta / CAISO daytime floor | $0 (Alberta); duck curve (CAISO) | CCGTs uneconomic midday; SCGTs run evenings because they start cheap | [1×: Power 2026] |
| Texas interchange | ~1 GW limited HVDC | Isolation raises local market-design importance | [1×: Power 2026] |
| Forward worked example | 300 MW × 1 year at $50/MWh | Financial gain/loss offsets DA purchase; physical still bought spot | [1×: Power 2026] |
| Spark-spread formula | Power − heat rate × gas | Gross-margin proxy for a gas generator | [1×: Power 2026] / [web: eia.gov] |
| Seven-heat-rate spark | Sell power forward; buy gas at 7:1 energy ratio | Hedge of a 7-heat-rate plant | [1×: Power 2026] |
| MISO coal vs gas | EIA May 2026: coal more profitable than gas recently | Merit-order fuel is not a permanent ranking | [1×: Power 2026] / [web: eia.gov] |
| Monterey Park | First municipal data-center ban by ballot | Political ceiling on siting | [1×: Power 2026] / [web: theguardian.com] |
| Maine statewide ban | Attempted; vetoed | Moratoria are live and uneven | [1×: Power 2026] |
| Retail vs wholesale | T&D + utility overhead can be the majority of a household bill | Ratepayer politics ≠ LMP | [1×: Power 2026] |

### Data-center ratepayer and political transmission channels

| Channel | Direction in source | Condition | Provenance |
|---|---|---|---|
| Incremental marginal generation | Higher LMP | Load calls a more expensive unit | [1×: Power 2026] |
| Transmission congestion | Higher local LMP / wider basis | A line hits its rating | [1×: Power 2026] |
| Capacity / resource adequacy | Higher system cost | New peak load requires paid standby capacity; NERC warning | [1×: Power 2026] / [web: nerc.com] |
| Fixed network-cost sharing | Lower average rate for incumbents | New customer pays into existing T&D base | [1×: Power 2026] |
| Renewable-surplus absorption | Higher producer revenue; possibly lower total-system cost | Load runs when prices are near zero or negative | [1×: Power 2026] |
| CCGT commitment smoothing | Possibly lower evening cost | Daytime load keeps CCGT online, avoiding later startup or a peaker | [1×: Power 2026] |
| Curtailable compute / ancillary service | Reliability payment | Load can stop when the grid is short (Bitcoin-mine precedent) | [1×: Power 2026] |
| Behind-the-meter or islanded gas | Higher regional gas cost | Off-grid electricity still competes for pipeline fuel | [1×: Power 2026] |
| Ratepayer Protection Pledge | Political alignment, not binding | White House high-level intent to shield ordinary ratepayers | [1×: Power 2026] / [web: whitehouse.gov] |
| Power for the People Act | Proposed new rate classes, queues, FERC rules; little traction | Attempt to socialize or isolate data-center cost | [1×: Power 2026] / [web: congress.gov] |
| Moratorium / special rate class | Lower project option value | Some bans failed; at least one succeeded | [1×: Power 2026] |
| Off-grid mandate (NH proposal) | Avoids electrical peak; does not avoid gas-basis spillover | Islanded plant still consumes methane | [1×: Power 2026] |

### Commodity and gas-chain facts the power thesis inherits

| Claim | Value / mechanism | Provenance | Vault use |
|---|---|---|---|
| Crude vs gas tradability | Crude globally shippable; raw gas is not | [1×: Power 2026] | Hormuz is a crude shock first |
| US dry-gas origin | Majority from dedicated gas wells | [1×: Power 2026] | Associated-gas narratives are incomplete |
| US gas residual | Domestic supply ≈ what could not be exported as LNG | [1×: Power 2026] | Links [[Theses/LNG - Cheniere Energy]] export capacity to US power fuel |
| Foreign vs US gas prices | Foreign higher lately; limited short-term pass-through into US | [1×: Power 2026] | Henry Hub is not JKM |
| US gas demand split | Industrial, res-comm heat, power | [1×: Power 2026] | AI load competes inside the power slice and, if BTM, the same molecules |
| Benchmarks | Henry Hub (US); AECO (Canada) | [1×: Power 2026] | Spark-spread denominator is hub-specific |

## Key Segments

### Commodities versus equities and the system-balance identity

A commodity future has a settlement date that forces price back to a physical bid or offer; an equity does not. Energy, agriculture, and metals therefore “solve” at every location via supply = demand + net exports + Δstorage, with transfer caps and storage bounds, every term a function of price. Electricity rewrites the identity with losses and with buses instead of warehouses: generation = consumption + net exports + Δstorage + losses. Competitive markets then impose uniform marginal pricing — the last cheap-enough producer sets the price everyone receives — so infra-marginal nuclear or wind collect rent and the last peaker collects none on the marginal megawatt-hour. The primer’s opening move is to stop treating power as a stock-like narrative (“AI demand is up, therefore the sector re-rates”) and start treating it as a spatially solved commodity.

### Why a megawatt-hour is not a barrel

Power is injected and withdrawn at physical buses tied by thermally rated lines; push too much current and the conductor sags. Buying 1 MWh does not authorize 1,000 GPUs: an ISO (or a balancing authority where there is no ISO) takes load-serving-entity bids and generator offers, computes nodal prices and intended flows, and dispatches units so frequency stays at 60 Hz. Draw too much and frequency falls; inject too much and it rises; $100M+ rotors are damaged if the grid leaves 60 Hz, which is why operators shed load rather than let a private consumer “take their purchased megawatts.” Storage here means batteries, pumped hydro, compressed air — not a tank farm — and most data-center operators hedge because they cannot live on ISO whim.

### Merit order, heat rates, and gas-plant physics

EIA-860 is the unit census. Merit order is the cost ranking; gas is often marginal; heat rate (MMBtu/MWh) times fuel price is the backbone of the offer. Brayton-cycle SCGTs (~300–400 MW in the sketch) become CCGTs (~600 MW, better heat rate) when an HRSG and Rankine steam turbine sit on the exhaust; peakers take a site toward ~800 MW at worse efficiency. Startup, no-load, and min-run costs make the daily commitment problem path-dependent: extra daytime load can save evening system cost by keeping a CCGT from cycling. Carbon adders in California and RGGI shift the same physical stack. A 100 MW unit at $60/MWh for 16 hours is ~$100k of gross revenue — enough to explain the asset class, not enough to finance it without a hedge.

### Site, finance, construction, Homer City

Plant type is chosen before the parcel. Grid sales wait in the interconnection queue because the ISO must restudy congestion; BTM compute can skip some of that queue and then inherits hall, cooling, and battery-balancing problems. Wyoming-style GIS conflict screens (minerals, existing queues, sage grouse) plus EFSEC-like stamps and local tax exemptions (Virginia’s named sales-and-use holiday) are the real site filter. Land is equity-cash; a $300M construction loan needs contracted cash flow or an HRCO; SOFR+2.25% is the prime-hyperscaler ballpark; turbines from GE Vernova, Siemens Energy, and Mitsubishi Power are months-to-years out. Homer City is the case: 2 GW of 10-heat-rate PJM coal retired in 2023, reborn as 4.4 GW / ~$10B / ~6-heat-rate gas plus campus, EQT fuel, DEP air permit November 2025, 1,000 workers, tenants undisclosed.

### Ratepayers, politics, training versus inference

Data-center legislation in the source is hesitant or hostile: a non-binding White House Ratepayer Protection Pledge, a low-traction Power for the People Act (new rate classes, queues, FERC rules), NERC warnings that new load lifts resource-adequacy prices, municipal bans (Monterey Park passed; Maine’s statewide attempt was vetoed), and at least one successful moratorium. The economics do not all point one way — T&D cost sharing, surplus-renewable absorption, and CCGT commitment smoothing can cut system cost — which is why the politics are confused rather than uniformly punitive. Physically islanded plants (New Hampshire proposal) dodge electrical peaks and still tighten gas. Training cannot follow the sun; inference can, so “independent” or “inference-first” grids are routing overlays, not a fourth US interconnection, and they revive smaller wellhead generators as [[Theses/NVDA - Nvidia]] spend mix tilts toward serving trained models.

### ISO map: PJM, MISO, CAISO, ERCOT, and the others

Traders live in zonal averages inside ISO-specific optimizations; retail customers pay wholesale plus T&D. PJM is the liquid default and hosts Virginia’s data-center stack plus a capacity market. MISO borders it, is retiring coal toward wind, and yet recently saw coal out-earn gas (EIA May 2026); Indiana, Illinois, and Michigan are the named data-center magnets. CAISO is NP-15/SP-15 across Path 15, no coal, BTM solar, PNW hydro imports on regulated ROE. ERCOT is a third interconnection with ~1 GW of HVDC, energy-only rules, negative west-Texas wind, and scarcity tails. SPP is wind; NYISO is stranded upstate nuclear versus Manhattan; ISO-NE burns oil when winter gas is short; the Southeast is vertically integrated cost-plus. Importing one region’s multiple onto another is a category error.

### Missing money: capacity markets versus energy-only

If the last unit is paid only its marginal cost, the least-efficient reliability resource earns zero quasi-rent, retires, and the next-least follows — the missing-money cascade. PJM and California pay for existence (ISO capacity market; utility RA contracts). Texas and Alberta refuse that “pay them to sit” design and try to put reliability into the energy price: ERCOT via a value-of-lost-load × probability-of-lost-load adder toward a $5,000/MWh-style cap; Alberta via uncapped-in-theory scarcity rent under a C$1,000/MWh cap that is scheduled to rise. Alberta then stacks a California problem on a Texas design: $0 daytime floors, evening SCGT, widening diurnal spreads, batteries flattening the curve, and an ISO mid-restructure. Political tolerance for those caps is part of the asset’s duration, not a footnote.

### Production-cost model, LMP, hedges, and spreads

Minimize total system cost subject to balance, transmission, generator, storage, and reliability constraints; read the balance-constraint shadow price as LMP; approximate flows with shift factors. Binary commitment makes the full problem mixed-integer, so traders relax binaries, freeze interchange and batteries, dispatch by merit order, and linearize losses — and they lose money when the frozen piece was the binding one. Spot is DA (clears the day before) plus 5-minute RT (weather-driven); deviations settle RT. A 300 MW year strip at $50/MWh converts volatile DA into a known all-in; spark and dark spreads hedge plants; effective heat rate predicts which gas units ignite; basis and FTRs express a view that a line will bind; on-peak products are the liquid hours. The last page of the primer refuses the question “do data centers raise or lower price?” and hands back the model.

## Contradiction Check

| Vault target | Specific assumption affected | Source effect | Required follow-up / falsifier |
|---|---|---|---|
| [[Theses/IREN - IREN Limited]] §Summary, Key Non-consensus Insight 1, Outstanding Question “is the power floor a number or a narrative?”, Conviction Trigger → LOW / → CLOSE | “5.8 GW of owned, permitted, grid-interconnected power + land” is the durable toll layer that bounds downside through a digestion | **Supports scarcity, challenges fungibility.** Queue position and energized shell can be a 24–48 month moat, but MW value is nodal: transmission basis, firm vs interruptible service, hourly shape, curtailment rights, local marginal fuel, and retail/tariff treatment determine the rent. “Connected” capacity without deliverability or a bankable load contract may not bound the → CLOSE distressed-sale path. VLM interface-control / political-ceiling hypothesis: interconnection is a toll every AI load must traverse, regulated and visible, not a software-like monopoly. | Map each campus to node/zone, queue status, firmness, historical basis, curtailment, contracted term. Falsifier for the article-driven caution: IREN monetizes the same MW at premium economics through a demand air pocket without material basis or curtailment leakage. |
| [[Theses/BE - Bloom Energy]] §Summary, Insight 1 (time-to-power arbitrage), Insight 2 (unaudited backlog), Conviction Triggers → HIGH / → LOW | Bloom monetizes a temporary time-to-power gap while turbines and grids are delayed; $20B “backlog” is treated as near-revenue | **Near-term support with a financing caveat.** The source independently describes major turbine backlogs and BTM as a possible interconnection bypass. Bypass is not bankability: fuel, permits, batteries, redundancy, EPC, and years of anchor cash flow remain, while the highest AI willingness to pay may last 6–12 months. A 90-day $5,000/MWh counterpart is the opposite of the → HIGH “repeat Tier-IV take-or-pay” condition. | Compare audited RPO and cancellation terms with construction/debt duration; test primary power versus bridge. A repeat Tier-IV-scale order with long take-or-pay would convert timing rent into an annuity and challenge the source’s duration mismatch. |
| [[Theses/CRWV - CoreWeave]] §Summary, Outstanding Questions 1–4, Bear Case, Insight 2 (amortization-cliff / re-rent) | Backlog and contracted rates protect a leveraged GPU fleet through the initial term | **Strengthens duration and counterparty risk.** Extraordinary short-term compute-plus-power prices do not prove long-duration project economics. If urgent lab need fades by 2028, the first re-rent collides with halls, plants, and debt underwritten over much longer lives. Nodal power and basis are a risk aggregate backlog conceals. SpaceX–Reflection-like optionality inside a “contracted” book would be the toxic case. | Obtain contract firmness, location-level power pass-through, curtailment, and second-cycle re-rent. Challenge is falsified if expiring cohorts renew at attractive spreads while commitments remain long enough to amortize power and GPUs. |
| [[Theses/NBIS - Nebius Group]] §Outstanding Question 1 (energize 800 MW–1 GW), Bear Case 1 | The load-bearing variable is physically energizing sold-out megawatts, not finding demand | **Strengthens the thesis’s own execution warning.** The site sequence — land conflicts, interconnection, transmission, fuel, permits, EPC, turbines, transformers, balancing — is why a sold-out book cannot accelerate commissioning. The production-cost framework adds that every incremental MW has its own delivered cost (basis, marginal fuel, firmness). Philadelphia / Finland ramps inherit nodal, not average, power. | Track active, firm, commissioned MW and delivered $/MW, not announced or connected pipeline. Caution is falsified if NBIS delivers the ramp without basis blowouts, emergency generation, or materially higher capex per MW. |
| [[Theses/VRT - Vertiv Holdings]] §Industry Context, Non-consensus Insight 5 (“benefits regardless of direction”), Conviction Triggers | Grid queues and equipment shortages force density per site and make vendor backlog less cyclical even if AI capex disappoints | **Supports the physical bottleneck, does not validate vendor moat.** Transmission and turbine scarcity are corroborated directionally. The source has no evidence on Vertiv share, OCP authorship, liquid-cooling IP, pricing, or backlog conversion. Flexible load, T&D cost sharing, negative-price absorption, and special rate classes can *redistribute* the constraint (siting, demand response, curtailability) rather than uniformly force more content per hall. “Regardless of direction” holds for physics, not for guaranteed RPO conversion or realized margin. | Separate equipment scarcity from supplier-specific pricing power. Falsifier is order/RPO conversion and realized margin after turbine/transformer lead times normalize, not aggregate data-center MW. |
| [[Theses/NVDA - Nvidia]] §Summary (Data Center 89.7%), Outstanding Question on Jevons vs algorithmic efficiency, three-computer / rack-scale architecture | GPU supply and software lock-in are the binding constraints on AI capacity; power is a background input | **Qualifies the complementary-asset claim.** The primer’s first sentence is that power, not GPU or memory, is the real constraint on expanding AI capacity. Training’s need for co-located gigawatts makes rack-scale NVL72/NVL576 deployments a *siting and interconnection* problem as much as a CoWoS/HBM problem (Industry-Semis #1 / #8: bottleneck can sit at power). Inference distribution toward cheap or negative-price nodes is a second-order demand support for merchant GPUs that can live in smaller halls — and a leak if workloads leave scarce campuses. [G-14] Jevons is consistent with the doubling claim and unproven by it. | Watch energized-MW growth versus GPU shipments, and whether inference load actually migrates to surplus-renewable nodes. Falsifier for “power binds first”: US data-center energized MW tracks GPU shipments with spare interconnect and flat nodal basis at the large training campuses. |
| [[Theses/META - Meta]] §Summary (capex $115–135B), Outstanding Question on isolatable ROI of incremental capex, Insight on infrastructure ROIC | Incremental infrastructure spend is assumed deliverable at planned sites and then earns on a 4–5 year asset life | **Challenges deliverability, not ad ROAS.** A hyperscaler is the primer’s “anchor tenant” archetype: the counterparty banks want, and the load that can congest the wrong node or trigger ratepayer rules (Monterey Park is the municipal-ban existence proof). Site, queue, gas lateral, and contract tenor determine whether 2026–28 dollars become energized MW on the original schedule. The source is silent on Advantage+/GEM; it is loud on the difference between a press-release campus and a financeable, interconnectable one. | Track Meta campus-level interconnection status, special tariffs, and behind-the-meter gas permits versus the capex guide. Falsifier: guided MW energize on schedule at contracted $/MWh that still clears the stripped ad-machine ROIC hurdle. |
| [[Theses/LNG - Cheniere Energy]] §Summary; [[Sectors/@LNG & Natural Gas Infrastructure]] §Investor heuristics (AI data-center demand raises the Henry Hub floor) | AI power is incremental US gas demand that lifts HH and, by implication, the export complex | **Directionally supportive, two-sided, quantitatively insufficient.** Gas is often the marginal power fuel; BTM and islanded plants still compete for pipeline molecules and “raise the natural gas price a little bit for everyone.” US gas is also the residual after LNG exports, so export capacity and AI-BTM load draw from the same domestic balance [1×: Power 2026]. The source does not estimate incremental Bcf/d, regional basis, or Cheniere SPA/IPM sensitivity; Cheniere’s 115% HH variable fee is mostly pass-through, so the bull for LNG-the-ticker is fee re-contracting and utilization, not a textbook HH print. | Convert announced gas-backed data-center MW into heat-rate-adjusted Bcf/d by basin and pipeline; compare with LNG feed-gas growth and new takeaway. Falsifier for a simple “AI raises HH, own Cheniere” chain: incremental DC gas is either interruptible, behind a different basin, or smaller than export + associated-gas variance. |
| [[Theses/CCJ - Cameco]] §Summary and Key Non-consensus Insight 3 (AI data-center baseload as a secular uranium demand floor) | AI load is 24/7 and therefore nuclear/uranium demand | **Does not validate the uranium transmission.** Nuclear sits low in the merit order (low variable cost, operationally constrained) and is “already big” at ~1 GW, which is why Homer City’s 4.4 GW gas campus is the author’s scale shock. The worked AI-adjacent plant in the primer is gas, not nuclear; Diablo Canyon appears as a CAISO geography (ZP-26), not as a new uranium offtake; NYISO’s lesson is that cheap nuclear can be *stranded* from the load sink by transmission. Data-center load can also be the thing that absorbs surplus wind or sits behind a gas turbine. Nuclear-as-baseload-for-AI remains a separate contracting story (Microsoft TMI, etc.) that this source does not evidence. | Look for named nuclear PPAs / restarts tied to specific campuses, not national TWh extrapolations. Falsifier for the caution: incremental AI MW show up as contracted nuclear (or SMR) offtake large enough to move the post-2027 uncontracted uranium book. |
| [[Macro & Technology/Sustainability of AI Capex]] §Power and physical capacity / funding-duration logic | Power is a physical ceiling; fragile AI-capacity tranches are financed ahead of durable end demand | **Supports and sharpens.** “Demand is now” versus multi-year plant underwriting is the same maturity mismatch as financed-capacity-ahead-of-utilization. Game-theoretic near-term spend can continue at very high WTP even if terminal utilization is uncertain ([G-4] frenzy installs the substrate). | Track weighted-average term and cancellation rights of AI power/colo contracts, not dollar backlog. A sustained rise in 10–20-year take-or-pay from creditworthy buyers would weaken the mismatch. |
| [[Sectors/Data Center Power & Cooling]] §Key industry questions / Macro shifts | Grid queues and equipment shortages are the sector’s binding 2026–30 constraint | **Supports the constraint, splits the cash-flow map.** Queues, turbines, and transformers are binding in the primer. Who gets paid depends on ISO rule, node, and contract, not on sector-level MW. | Keep vendor theses (VRT, BE) on conversion and duration metrics, not on national load-growth slides. |

### Mental-model triggers fired

- **Generalist [G-3] · complex dynamical system / mean reversion versus trend:** identical data-center load can raise LMP, lower total system cost, or change only basis depending on the marginal unit, transmission state, storage, and flexibility. Hypothesis: durable alpha is predicting the next *binding constraint*, not extrapolating national load. Disconfirm with node-level outcomes, not sector narratives.
- **Generalist [G-4] · Perez infrastructure installation:** turbines, transmission, substations, and data-center shells resemble frenzy-funded enabling infrastructure whose social capacity may outlive the builders’ equity. Hypothesis: the substrate retains use-value even if late-cycle holders lose; this does not name which current builder captures it. Homer City’s coal-to-gas-to-campus arc is a physical illustration of infrastructure being rewritten faster than the original owners were paid.
- **Generalist [G-10] · base rates / outside view:** nine-figure plants with “things have to go perfectly,” sold-out turbines, and 6–12 month demand pulses sit in a reference class of delayed, over-budget infrastructure. Hypothesis: treat announced GW as option value until COD plus contracted offtake. The inside view is the lab WTP napkin; the outside view is interconnection and EPC calendars.
- **Generalist [G-13] · expectations investing:** isolate the single operating variable the price implies — for IREN, campus-level delivered $/MWh and firmness; for BE/CRWV/NBIS, weighted contract term and cancellation; for VRT, conversion of equipment scarcity into margin. National “power shortage” is too coarse a value driver.
- **Generalist [G-14] · Jevons rebound:** lower compute cost and geographically distributed inference can unlock workloads large enough to keep electricity demand rising despite efficiency. The doubling claim is consistent with the lens and does not prove it. Falsifier: efficiency-adjusted US data-center load growth stays below the pace of compute-cost decline for several years while utilization stays weak.
- **Industry - Semiconductors #1 · emerging bottleneck = pricing power:** hypothesis that the binding AI-capacity bottleneck has moved from CoWoS/HBM toward interconnection, turbines, and nodal deliverability. Re-identify rather than freeze last cycle’s chokepoint.
- **Industry - Semiconductors #8 · architecture remaps the bottleneck:** NVL72 → rack-scale makes power and interconnect first-class constraints alongside the GPU. Training’s co-location requirement is the mechanism.
- **Industry - Semiconductors #17 · do not assume new supply appears at tight prices:** multi-year turbine and queue lead times are the power-market version of inelastic semi supply.
- **Industry - Semiconductors #18 · do not conflate cycle and structural:** a 6–12 month WTP spike can be a cycle; a 20-year 400 MW lease is closer to structural. Separate them in every backlog.
- **[[Lens - Automation & AI Readiness]] §6 · energy/industrials physical-core overlay:** siting, grid operations, construction, and permitting remain atom-heavy, regulated, and tacit. Hypothesis: power companies can be AI-*demand* beneficiaries without AI-driven operating leverage; assign no automation-margin premium without workflow-level evidence.
- **[[Lens - Value Layer Monopoly]] §1A / §2 · interface control and political ceiling:** interconnection rights, transmission paths, and ISO rules can function as toll layers every AI load must traverse, but they are regulated, geographically fragmented, capital-intensive (fail non-rivalry), and politically visible (Ratepayer Protection Pledge, bans, special tariffs). Hypothesis: rents accrue to scarce *deliverability*, not generic generation; ratepayer rules cap extraction before it becomes a software-like monopoly.

### Disconfirming check

The models and the source agree too cleanly that power is the next AI bottleneck, so the bear case takes priority: announced demand may be short-duration, double-counted, geographically mismatched, interruptible, or unable to finance the supply it supposedly requires. Agreement across [G-3]/[G-4]/[G-10]/VLM/Automation is a cue to hunt the single bullish falsifier, not to raise conviction. That falsifier is **creditworthy 10–20-year contracted AI load converting into active nodal MW at delivered prices that cover generation, transmission, fuel, and financing without special subsidies or repeated delay**. Until that series exists, “gigawatts secured” stays a hypothesis rather than a valuation input.

## Source Excerpts

> "Data centers already account for ~5% of US power consumption. With data center power demand doubling every two years, demand would in theory outpace total US power generation by the mid-2030s." [1×: Power 2026]

> "If I buy 1 megawatt-hour (MWh) of power on the market, that doesn't necessarily mean I can just go and plug 1000 GPUs into the wall and start consuming 1 MW for an hour." [1×: Power 2026]

> "If you have 1400 MMBtu of natural gas and a 7 heat rate unit (pretty typical efficiency), then that's enough to produce 200 MWh." [1×: Power 2026]

> "For a 100 MW unit running at full capacity for 16 hours at $60/MWh, we're talking on the order of $100K of gross revenue per day." [1×: Power 2026]

> "Major turbine manufacturers like GE Vernova, Siemens Energy, and Mitsubishi Power are completely out of stock, with the backlog months to years out." [1×: Power 2026]

> "If an established data center developer has a prime tenant like a hyperscaler, a reasonable ballpark is ~2.25% above SOFR." [1×: Power 2026]

> "They're redoing the whole thing to build a 4.4 GW natural gas plant. ... This 4.4 GW plant is intended to cost ~$10 billion to construct, and the plan is to turn it into a big data center campus." [1×: Power 2026]

> "Based on various discussions, some major labs are comfortable with their level of power/compute a couple of years from now (2028). The real demand for power is now. The problem is that 6-12 months of demand isn't necessarily enough to underwrite the development of an entire plant." [1×: Power 2026]

> "SpaceX entered into this deal to sell power to Reflection which offers high optionality: a 90-day out for either party. My napkin math indicates that this implies around ~$5000/MWh, but that's power that comes with GPUs ready to go." [1×: Power 2026]

> "A longer term structure is Anthropic's $19 billion lease with TeraWulf, which is 400 MW over 20 years starting in H2 2027. The implied revenue is ~$271/MWh with no GPUs included, but it does come with surrounding infrastructure like the building itself and cooling capacity." [1×: Power 2026]

> "In a simplified sense, the natural gas we have here in the US is the supply that couldn't be physically exported." [1×: Power 2026]

> "That doesn't work for the training of machine learning models, which requires many GPUs to be co-located, commanding gigawatts of power in the same place. But inference ... does not have the same gigawatt-scale requirements." [1×: Power 2026]

> "The Lagrange multiplier of each location's balance constraint is exactly the marginal cost for providing an additional MWh of power at that location. ... That's called the Locational Marginal Price (LMP)." [1×: Power 2026]

> "The moment the power line hit its maximum capacity, the power price increased. That's called a 'binding constraint.' Those binding constraints are theoretically the core of what causes prices to increase." [1×: Power 2026]

> "But is the build of a new data center going to cause prices to increase or decrease? ... Unsatisfyingly, it depends." [1×: Power 2026]
