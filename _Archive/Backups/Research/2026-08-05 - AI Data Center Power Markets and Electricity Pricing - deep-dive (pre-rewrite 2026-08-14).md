---
publish: false
date: 2026-08-05
tags: [research, data-center-power, AI-infrastructure, power-markets]
sector: Data Center Power & Cooling
source: '/Users/alexcohen/InvestmentVault/_Inbox/Power 2026 by Neel Somani - Electricity Pricing in the Age of AI.md'
original_source: 'https://power2026.ai/'
source_type: deep-dive
propagated_to: [IREN, NBIS, VRT, CRWV, BE]
---

# AI Data Center Power Markets and Electricity Pricing

## Thesis Delta

Consensus treats AI power as a national shortage that mechanically raises electricity prices and validates every “power bottleneck” equity; this source implies the investable variable is **locational and temporal scarcity**—the node, binding transmission constraint, marginal generator, firmness of interconnection, and contract duration. That strengthens the owned-power cases in [[Theses/IREN - IREN Limited]] and the deployment-speed case in [[Theses/BE - Bloom Energy]], but narrows both: headline megawatts are not a toll layer unless nodal economics, fuel exposure, deliverability, and multi-year customer commitments survive a demand air pocket.

## Summary

The source builds a first-principles chain from commodity balance to AI-data-center economics. Electricity cannot be transported or stored as freely as oil, so generation and consumption must balance continuously at thousands of grid locations subject to transmission ratings, generator limits, storage state, losses, outages, and reliability rules. In the author’s simplified competitive-market model, the last generator needed to serve an additional megawatt-hour sets the clearing price. A data center therefore does not have one generic “power cost”: its cost depends on which grid node it occupies, which unit is marginal at each hour, whether a line becomes congested, how renewable and battery output reshape the merit order, and how its actual load differs between day-ahead and real-time settlement.

That mechanism breaks the linear claim that more data centers always raise household electricity prices. A new load can increase the local marginal price or capacity requirement when it binds transmission or forces inefficient generation to run. It can also lower average system costs by sharing fixed network expenses, absorbing otherwise-curtailed renewable output, keeping an efficient combined-cycle plant online through low-demand hours, or offering interruptible load as an ancillary service. The sign depends on location, hour, market design, and flexibility. The source’s strongest analytical contribution is thus not a bullish forecast for power assets; it is a framework for identifying where scarcity rents actually accrue and where political responses, transmission limits, or demand flexibility redistribute them.

For data-center developers, the bottleneck is a coupled site-finance problem rather than a simple land or electricity purchase. Grid interconnection can take years; behind-the-meter generation can reduce that dependence but adds fuel, permitting, space, cooling, redundancy, and balancing requirements. A nine-figure plant normally needs years of contracted cash flow through a power purchase agreement, dedicated-supply contract, or hedge, while the author argues that some AI labs’ highest willingness to pay is concentrated in the next 6–12 months. This duration mismatch is the key thesis signal: near-term compute scarcity can produce extraordinary prices without creating a financeable long-duration power project. It supports the vault’s skepticism toward unaudited backlog and headline contracted capacity across [[Theses/BE - Bloom Energy]], [[Theses/CRWV - CoreWeave]], and [[Theses/NBIS - Nebius Group]], and sharpens the funding-duration question in [[Sectors/Neoclouds & GPU-as-a-Service]].

The second half turns the physical system into a pricing and trading model: minimize total production cost subject to nodal balance, transmission, capacity, and reliability constraints; read each balance constraint’s shadow price as the locational marginal price; then hedge the relevant exposures through forwards, spark spreads, basis trades, or financial transmission rights. The primer is educational rather than a forecast and its numerical claims remain source assertions, not independent verification. Its durable value is the decomposition: power ownership, interconnection, and turbine scarcity matter only after specifying the node, market rules, marginal fuel, hedge, counterparty, and duration.

## Framework / Mental Model

### 1. System-balance-to-price chain

The source starts from a commodity identity applied at every location:

**Supply = demand + net exports + change in storage.**

For electricity, the working form becomes:

**Generation = consumption + net power exports + change in storage + losses.**

Each term is both physical and price-sensitive. Generation rises only if another unit can start, ramp, or produce more. Net exports are capped by transmission-line ratings and by the network physics that determine how injections flow across multiple lines. Storage cannot discharge below zero or charge beyond its energy and power limits. Losses rise as current moves through the network. Demand is often modeled as inelastic in the short run, but flexible data-center workloads, batteries, and demand-response contracts relax that assumption.

Methodology:

1. Choose the relevant location and time interval; a national annual average is too coarse.
2. Forecast consumption, renewable output, generator availability, fuel costs, storage behavior, and imports/exports.
3. Enforce the balance identity plus the physical constraints.
4. Identify the next feasible unit or action that can supply one incremental MWh.
5. Treat its incremental system cost as the local price in the source’s simplified competitive framework.
6. Re-run the system under weather, outage, fuel-price, load, and transmission scenarios rather than relying on one forecast.

The investment implication is a move from “power is scarce” to “which constraint binds first?” A nominally power-rich region can still be expensive if the cheap generation sits behind a saturated line. A region with limited generation can remain cheap if imports are unconstrained. A gigawatt of data-center demand has different economics when it absorbs surplus midday wind, requires a new peaker on a hot evening, or can curtail within minutes. The model treats power as a networked dynamical system, not a fungible national commodity.

### 2. Merit order and plant economics

Generators are ranked by the marginal cost of producing the next MWh—the **merit order**. Solar and wind usually sit near the bottom because their fuel cost is close to zero; nuclear and hydro are low-variable-cost but operationally constrained; coal and gas depend on fuel and efficiency; oil or diesel peakers tend to be expensive. The last unit required to meet load is the **marginal unit**, and its offer anchors the uniform clearing price in the source’s stylized model.

For a gas or coal unit, the reusable approximation is:

**Fuel cost per MWh = heat rate × fuel price.**

Heat rate measures MMBtu of fuel required per MWh. Lower is better. The dispatch calculation then adds variable operations and maintenance, emissions costs where applicable, and other incremental costs. Startup cost, no-load cost, minimum run time, ramp rate, and minimum generation complicate the simple curve: a unit may be cheap once running but costly to start, so serving more daytime demand can sometimes lower the total daily system cost by avoiding a shutdown-and-restart cycle.

![[Power 2026 - Power Plant Offer Curve.png]]

The plant-development lens adds fixed capital and lead time. A project must select fuel, capacity, site, pipeline access, water, air permit, land rights, construction contractor, equipment, and grid posture before it can monetize the merit-order position. Simple-cycle gas turbines offer speed and flexibility; combined-cycle plants reuse exhaust heat to improve efficiency and output; peakers provide scarce capacity at worse heat rates. A low-variable-cost plant can still be a poor investment if construction overruns, utilization is low, interconnection is delayed, or contracted revenue does not cover fixed costs.

Methodology for an asset:

1. Build the unit’s hourly variable-cost curve from heat rate, fuel, emissions, and variable O&M.
2. Add startup/no-load/minimum-run constraints and expected forced outages.
3. Place the unit in the regional merit order under multiple fuel and load cases.
4. Estimate dispatched hours and gross spark spread, not just nameplate capacity.
5. Add capacity, ancillary-service, hedge, and contracted revenues.
6. Compare the complete cash-flow stack with construction cost, financing terms, and schedule risk.

### 3. Locational marginal pricing and the production-cost model

The source’s named analytical framework is the **production cost model**. Its objective is to minimize total system production cost subject to:

- **Balance constraints:** supply equals demand at every modeled node or zone.
- **Transmission constraints:** line flows stay within ratings.
- **Generator constraints:** output remains between technical minimum and maximum; richer models add unit commitment, ramp rates, minimum run times, and startup costs.
- **Storage constraints:** charging, discharging, energy inventory, and efficiency remain feasible.
- **Reliability constraints:** reserves and local-generation requirements remain available.

The Lagrange multiplier, or shadow price, on a node’s balance constraint is the marginal cost of serving one more MWh there: the **locational marginal price (LMP)**. When transmission is unconstrained, cheap generation can serve both locations and prices converge, aside from losses. When a line binds, the constrained location must call a more expensive local unit and the price separates. The resulting basis is not an accounting artifact; it is the economic value of the network bottleneck.

Power-flow detail can be approximated with shift factors or Power Transfer Distribution Factors: the estimated change in each line’s flow after injecting power at one point and withdrawing it at another. A full mixed-integer production-cost model is computationally expensive because generators are on or off. Common approximations include fixing unit commitment, relaxing the binary decision, assuming predictable imports and battery behavior, dispatching by merit order, and ignoring or linearizing losses. Each shortcut must be matched to the market: a simplified merit-order model can be useful where flows are stable and dangerously wrong where congestion drives most price variance.

![[Power 2026 - ISO Map.png]]

### 4. Market-design taxonomy

The same physical grid produces different investment outcomes under different market rules.

| Design element | Mechanism | Economic question |
|---|---|---|
| Uniform energy clearing | All dispatched units receive the clearing price | Does the marginal unit provide enough inframarginal rent to cover fixed cost? |
| Capacity market / resource adequacy | Generators receive payment for being available | Which assets earn an existence payment even when rarely dispatched? |
| Energy-only market | Fixed costs must be recovered through energy and scarcity prices | Are scarcity rents high and frequent enough to finance reliable capacity? |
| Scarcity adder / offer cap | Price rises as reserve margin falls or load is unserved | Does political tolerance permit prices needed to sustain peakers? |
| Day-ahead market | Financial schedule clears before delivery | How much volume and price can the asset lock before weather and outages resolve? |
| Real-time market | Deviations settle close to physical delivery | How costly are forecast errors, forced outages, or load deviations? |
| Ancillary services | Fast generation, storage, or curtailable load is paid for flexibility | Can a data center monetize interruptibility rather than remain a fixed load? |

This taxonomy prevents importing one region’s economics into another. PJM combines organized energy and capacity markets; ERCOT relies more heavily on energy scarcity; CAISO’s renewables and batteries reshape intraday pricing; vertically integrated utility regions recover costs through regulated retail rates. A power thesis must name the market rule that converts a physical advantage into cash flow.

### 5. Data-center site-and-finance decision tree

The source’s development methodology can be reapplied as a gating sequence:

1. **Define the load:** training requires co-located, high-density, relatively continuous power; inference can be geographically distributed and may offer more scheduling flexibility.
2. **Choose the grid posture:** grid-connected, co-located/behind-the-meter, or physically separate. Behind-the-meter can reduce interconnection dependence but does not remove permits, fuel logistics, redundancy, storage, maintenance, or load-balancing needs.
3. **Screen the site:** transmission node, queue position, gas pipeline, water, fiber, land conflicts, wildlife/mineral rights, tax treatment, local politics, and construction labor.
4. **Secure equipment and EPC capacity:** turbine, transformer, switchgear, cooling, battery, and contractor lead times can each become the critical path.
5. **Match contract duration to asset life:** a PPA, dedicated-supply agreement, anchor tenancy, or heat-rate call option converts volatile merchant revenue into financeable cash flow.
6. **Underwrite the counterparty:** a headline price is not bankable if the buyer can exit before debt amortizes or lacks the balance sheet to honor the contract.
7. **Hedge residual risk:** manage power price, gas price, congestion basis, hourly shape, and day-ahead/real-time volume mismatch.

The decision tree separates **willingness to pay** from **bankability**. A customer paying an extreme near-term rate with a 90-day cancellation right can be less useful for construction finance than a lower-priced 20-year contract. This is the bridge between power-market mechanics and the vault’s neocloud/backlog analysis: the value of a contracted megawatt depends on duration, firmness, credit, node, and hedge—not the headline dollar value alone.

### 6. Hedge decomposition

The framework maps each physical risk to a financial exposure:

- **Power-price level:** buy or sell zonal forwards.
- **Fuel-price level:** buy gas forwards for a gas plant.
- **Plant gross margin:** hedge the **spark spread**: power price minus heat rate multiplied by gas price.
- **Coal economics:** use the analogous dark spread.
- **Nodal congestion:** trade basis between locations or use Financial Transmission Rights.
- **Hourly shape:** trade peak/off-peak or one-hour-versus-another spreads.
- **Forecast error:** manage day-ahead versus real-time exposure.

The hedge is only as good as its basis match. A zonal forward does not fully hedge a specific bus; expected consumption can differ from actual consumption; plant availability can fail when the hedge assumes output; and gas basis can diverge from the benchmark. The framework therefore treats “fixed power cost” as a portfolio of partially matched instruments rather than a single contract.

## Evidence

### AI load and development economics

| Source claim / example | Value | Analytical use |
|---|---:|---|
| US electricity consumed by data centers | ~5% | Starting load share cited by the author |
| Data-center power-demand cadence | Doubling every 2 years | Source’s high-growth premise; not independently verified here |
| Theoretical crossover with total US generation | Mid-2030s | Extrapolation illustrating why physical supply becomes binding, not a forecast |
| Illustrative new gas plant construction cost | $300M | Nine-figure financing requirement used in the development example |
| Established developer construction debt | ~SOFR + 2.25% | Ballpark with a prime hyperscaler anchor tenant |
| Major turbine availability | Months to years of backlog | GE Vernova, Siemens Energy, and Mitsubishi Power cited as sold out |
| Training-load topology | Many GPUs co-located; gigawatt-scale | Limits geographic load shifting |
| Inference-load topology | Smaller, distributable clusters | Supports geographic/time-of-day routing thesis |
| Author’s AI-lab demand read | Strongest demand is now; some labs comfortable by 2028 | Creates a duration mismatch versus multi-year plant underwriting |

### Generation and plant-unit examples

| Item | Source value | Relationship |
|---|---:|---|
| Typical gas-unit heat rate | ~7 MMBtu/MWh | 1,400 MMBtu produces ~200 MWh in the example |
| SCGT output | ~300–400 MW | Simple-cycle turbine before heat recovery |
| CCGT output | ~600 MW | Combined Brayton + Rankine cycle example |
| Plant with peakers | ~800 MW | Higher output at worse marginal efficiency |
| Typical regional wholesale-price range | ~$10–150/MWh | Wide dispersion before scarcity tails |
| Illustrative plant revenue | 100 MW × 16 hours × $60/MWh ≈ $96,000/day | Rounded by source to ~$100,000 gross daily revenue |
| Grid frequency | 60 Hz | Continuous balance protects rotating generators |
| Data-center physical example | 1 MWh does not automatically support 1,000 GPUs at 1 MW for one hour | Delivery rights differ from financial power purchases |

### Homer City redevelopment case

| Attribute | Historical / new plan |
|---|---|
| Legacy plant | ~2 GW, three coal units, Pennsylvania / PJM |
| Legacy efficiency | ~10 heat-rate coal versus ~6–7 heat-rate gas competitors |
| Closure | 2023 after ~50 years |
| Redevelopment | 4.4 GW natural-gas plant and data-center campus |
| Estimated construction cost | ~$10B |
| Gas partner | EQT Corporation |
| Target unit efficiency | ~6 heat rate |
| Air-quality permit | Pennsylvania DEP approval in November 2025 |
| Construction workforce cited | 1,000 people |
| Investment variables | Schedule, permit completion, anchor tenancy, financing, turbine delivery, refinancing |

### Contract-duration and willingness-to-pay examples

| Arrangement | Scale / term | Implied price | Bankability signal |
|---|---|---:|---|
| SpaceX–Reflection | 90-day termination right for either party; power bundled with ready GPUs | Author estimates ~$5,000/MWh | Extreme near-term scarcity price; weak duration for plant debt |
| Anthropic–TeraWulf | $19B lease; 400 MW; 20 years; starts H2 2027 | Author estimates ~$271/MWh without GPUs | Lower price but long, infrastructure-backed cash flow |
| Generic hyperscaler anchor | Multi-month/year dedicated price per MWh | Not specified | Longer term improves construction-loan underwriting |
| Heat-rate call option | Plant economics exchanged for fixed periodic payment | Plant-specific | Converts volatile merchant gross margin into financeable cash flow |

### Regional market map

| Market | Source characterization | AI/power relevance |
|---|---|---|
| PJM | Most liquid organized US market; capacity market; Virginia data-center concentration | Queue, capacity, and transmission constraints determine incremental-load cost |
| MISO | Coal retirements, large wind fleet, flows with PJM | Data-center additions interact with changing marginal fuel |
| CAISO | High renewables, no coal, nuclear + gas residual stack, NP-15/SP-15 split | Solar duck curve, batteries, imports, and Path 15 shape prices |
| ERCOT | Isolated energy-only market; limited HVDC ties; negative wind prices and scarcity spikes | Flexible compute can absorb surplus or monetize curtailment |
| SPP | Wind-heavy | Load can raise value of otherwise-curtailed generation |
| NYISO | Cheap upstate nuclear constrained from Manhattan | Transmission, not aggregate generation, creates nodal scarcity |
| ISO-NE | Winter gas scarcity can force oil generation | Fuel deliverability changes marginal unit and spark spread |
| Southeast / parts south of PJM | Vertically integrated regulated utilities | Retail-rate and allowed-return logic differs from ISO trading |
| Alberta | Gas-heavy energy-only market with renewables growth | Scarcity-rent design plus batteries flattening the daytime/evening spread |

### Market-design and price examples

| Example | Input | Output / implication |
|---|---|---|
| Two-node congestion | Node B marginal cost $10/MWh; node A $100/MWh; line limit 50 MW | At 10 MWh demand in A, import from B sets ~$10; at 60 MWh, line binds and local ~$100 unit sets incremental price |
| ERCOT value of lost load / offer-cap example | $5,000/MWh | Scarcity pricing intended to recover reliability value without a conventional capacity market |
| Alberta cap | C$1,000/MWh, scheduled to rise | Caps recoverable scarcity rent for the marginal generator |
| Texas interconnection with other US grids | ~1 GW of limited HVDC transfer | Isolation increases local market-design importance |
| Day-ahead market | Clears one day before delivery | Schedules and prices expected generation/load |
| Real-time market | Re-optimized every 5 minutes | Settles deviations, outages, and forecast errors |
| Forward example | 300 MW for one year at $50/MWh | Financial gain/loss offsets day-ahead purchase cost; physical power still bought in spot market |
| Spark-spread formula | Power price − heat rate × gas price | Gross margin proxy for a gas generator |
| Seven-heat-rate spark spread | Sell power forward; buy gas forward at 7:1 energy ratio | Hedge approximates a 7-heat-rate plant’s fuel-linked margin |

### Data-center ratepayer transmission channels

| Channel | Direction in source | Condition |
|---|---|---|
| Incremental marginal generation | Higher prices | Load calls a more expensive unit |
| Transmission congestion | Higher local prices / wider basis | A line reaches its rating |
| Capacity/resource adequacy | Higher system cost | New peak load requires paid standby capacity |
| Fixed network-cost sharing | Lower average rate for existing users | New customer pays into existing transmission/distribution base |
| Renewable-surplus absorption | Higher producer revenue; potentially lower total-system cost | Load runs when prices are near zero or negative |
| CCGT commitment smoothing | Potentially lower evening cost | Daytime load keeps an efficient combined-cycle unit online, avoiding a later startup or inefficient peaker |
| Curtailable compute / ancillary service | Reliability value | Load can stop quickly when the grid is short |
| Behind-the-meter gas demand | Higher regional gas cost | Off-grid electricity still competes for pipeline fuel |
| Moratorium / special rate class | Lower project option value | Political response socializes or blocks perceived ratepayer harm |

## Contradiction Check

| Vault target | Specific assumption affected | Source effect | Required follow-up / falsifier |
|---|---|---|---|
| [[Theses/IREN - IREN Limited]] §Summary and Key Non-consensus Insight 1 | “5.8 GW of owned, permitted, grid-interconnected power + land” is the durable toll layer | **Supports scarcity, challenges fungibility.** Queue position and energized infrastructure can be durable, but MW value is nodal: transmission basis, firmness, hourly shape, curtailment rights, local marginal fuel, and retail treatment determine the rent. “Connected” capacity without deliverability or a bankable load contract may not bound downside. | Map each campus to node/zone, queue status, firm vs interruptible service, historical basis, curtailment, and contracted term. Falsifier for the article-driven caution: IREN monetizes the same MW at premium economics through a demand air pocket without material basis or curtailment leakage. |
| [[Theses/BE - Bloom Energy]] §Summary and Insight 1 | Bloom monetizes a temporary time-to-power arbitrage while turbines and grids are delayed | **Near-term support with a financing caveat.** The source independently describes major turbine backlogs and BTM as a potential interconnection bypass. It also shows why bypass is not equivalent to bankability: fuel, permits, batteries, redundancy, EPC, and years of anchor cash flow remain, while the highest AI willingness to pay may last only 6–12 months. | Compare Bloom’s audited RPO and cancellation terms with construction/debt duration; test whether deployments are primary power or bridge capacity. A repeat Tier-IV-scale order with long take-or-pay duration would convert the source’s timing rent into a more durable annuity. |
| [[Theses/CRWV - CoreWeave]] §Summary, Outstanding Questions 1–4, and Bear Case | Backlog and contracted rates protect a leveraged GPU fleet through the initial term | **Strengthens the duration/counterparty risk.** Extraordinary short-term compute prices do not prove long-duration power-project economics. If customers’ urgent need fades by 2028, the first re-rent period collides with plants, data halls, and debt underwritten over much longer lives. Nodal power and basis costs add a risk obscured by aggregate backlog. | Obtain contract firmness, location-level power pass-through, curtailment provisions, and second-cycle re-rent rates. Challenge is falsified if expiring cohorts renew at attractive spreads while customer commitments remain long enough to amortize power and GPU infrastructure. |
| [[Theses/NBIS - Nebius Group]] §Outstanding Question 1 and Bear Case 1 | The load-bearing variable is physically energizing 800 MW–1 GW, not selling demand | **Strengthens the thesis’s own execution warning.** The source’s site sequence—land conflicts, interconnection, transmission, fuel, permits, EPC, turbines, transformers, balancing—shows why a sold-out book cannot accelerate physical commissioning. The production-cost framework also says every added MW has a different delivered cost. | Track active, firm, commissioned MW rather than announced or connected pipeline; disclose nodal power cost and commissioning slippage. Caution is falsified if NBIS delivers the ramp without basis blowouts, emergency generation, or materially higher capex per MW. |
| [[Theses/VRT - Vertiv Holdings]] §Industry Context and [[Sectors/Data Center Power & Cooling]] §Key industry questions / Macro shifts 1–2 | Grid queues and equipment shortages force density per site and make vendor backlog less cyclical | **Supports the physical bottleneck, does not validate vendor moat.** The source corroborates transmission and turbine scarcity directionally, but it contains no evidence on Vertiv share, OCP advantage, pricing, or backlog conversion. It also challenges “bullish regardless of AI-capex direction”: flexible load, fixed-cost sharing, and regional price effects mean the grid constraint can change architecture without guaranteeing every equipment vendor’s return. | Separate equipment scarcity from supplier-specific pricing power. The relevant falsifier is order/RPO conversion and realized margin after turbine/transformer lead times normalize, not aggregate data-center MW alone. |
| [[Macro & Technology/Sustainability of AI Capex]] §Power and physical capacity / funding-duration logic | Power is a physical ceiling, while fragile AI-capacity tranches are financed ahead of durable end demand | **Supports and sharpens.** The author’s “demand is now” versus multi-year plant underwriting creates the same maturity mismatch as the macro note’s financed-capacity concern. The offset is that game-theoretic near-term spending can continue at very high willingness to pay even if terminal utilization is uncertain. | Track the weighted-average term and cancellation rights of AI power/colo contracts, not just dollar backlog; compare them with debt and equipment lives. A sustained rise in 10–20-year take-or-pay commitments from creditworthy buyers would weaken the mismatch thesis. |
| [[Sectors/@LNG & Natural Gas Infrastructure]] §Investor heuristics | AI data-center demand raises the Henry Hub floor | **Directionally supportive, quantitatively insufficient.** Gas is often the marginal power fuel, and BTM gas generation still competes with grid and LNG demand for pipeline supply. The source does not estimate incremental Bcf/day, regional basis, pipeline capacity, or Cheniere margin sensitivity, so it cannot validate the magnitude of the sector claim. | Convert announced gas-backed data-center MW into heat-rate-adjusted Bcf/day by basin and pipeline; compare with LNG feed-gas growth and new takeaway. |

### Mental-model triggers fired

- **Generalist [G-3] · complex dynamical system / mean reversion versus trend:** identical data-center load can raise prices, lower total system cost, or change only basis depending on the marginal unit, transmission state, storage, and flexibility. Hypothesis: the durable alpha lies in predicting the next binding constraint, not extrapolating national load growth. Disconfirm with node-level outcomes rather than sector narratives.
- **Generalist [G-4] · Perez infrastructure installation:** turbines, transmission, substations, and data-center shells resemble frenzy-funded enabling infrastructure whose capacity may outlive the builders’ returns. Hypothesis: the substrate will retain social value even if late-cycle equity holders lose; this does not identify which current builder captures it.
- **Generalist [G-14] · Jevons rebound:** lower compute cost and inference distribution can unlock workloads large enough to keep electricity demand rising despite efficiency gains. The article’s doubling claim is consistent with the lens but does not prove it. Falsifier: efficiency-adjusted US data-center load growth falls below the pace of compute-cost decline for several years while utilization and workload volume remain weak.
- **[[Lens - Automation & AI Readiness]] §6 · energy/industrials physical-core overlay:** plant siting, grid operations, construction, and permitting remain atom-heavy, regulated, and tacit. Hypothesis: power companies can be AI-demand beneficiaries without having AI-driven operating leverage; no margin premium should be assigned without workflow-level evidence.
- **[[Lens - Value Layer Monopoly]] §1A / §2 · interface control and political ceiling:** interconnection rights, transmission paths, and market rules can function as toll layers that every AI load must traverse, but they are regulated, geographically fragmented, capital-intensive, and politically visible. Hypothesis: rents accrue to scarce deliverability rather than generic generation; ratepayer-protection rules, special tariffs, or moratoria cap extraction before it becomes a software-like monopoly.

### Disconfirming check

The models and source agree too cleanly that power is the next AI bottleneck, so the bear case deserves priority: announced demand may be short-duration, double-counted, geographically mismatched, interruptible, or unable to finance the supply it supposedly requires. The single falsifying datapoint for that bear case is **creditworthy 10–20-year contracted AI load converting into active nodal MW at delivered prices that cover generation, transmission, fuel, and financing without special subsidies or repeated delay**. Until that series exists, “gigawatts secured” should remain a hypothesis rather than a valuation input.
