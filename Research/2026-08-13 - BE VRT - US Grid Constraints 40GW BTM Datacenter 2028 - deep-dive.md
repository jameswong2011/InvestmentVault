---
publish: false
date: 2026-08-13
tags: [research, datacenter, power, BE, VRT]
sector: Data Center Power & Cooling
ticker: BE
source: 'https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw'
source_type: deep-dive
propagated_to: [BE, VRT, LNG, CCJ]
---

# US Grid Constraints — Towards 40GW+ of Behind-The-Meter Datacenter by 2028

## Thesis Delta

Consensus prices US datacenter power as a grid-served load with behind-the-meter (BTM) generation as a niche bridge; SemiAnalysis's Energy Model instead shows accredited grid headroom turning negative by 2027 and never catching the +84GW-by-2030 buildout, forcing BTM to power **well over half of new US datacenters from 2028** and pushing **DC-BTM equipment TAM across 50GW/year by 2029**. If the binding constraint is power *generation* — not chips, not capital — the marginal AI datacenter is won by whoever supplies onsite generation, a structural tailwind for the [[Theses/BE - Bloom Energy]] demand leg and a grid-chokepoint confirmation for [[Theses/VRT - Vertiv Holdings]]; the disconfirming datapoint the same source hands over is that the BTM-equipment winner list is crowded (Bloom, INNIO, Wärtsilä, Bergen) and secondary-market turbine availability is "surging," so the supply response is elastic and the pricing-power / layer-monopoly leg the bull case needs does not follow from the TAM.

## Summary

The grid cannot add firm capacity fast enough to serve AI load, and the gap is structural, not transitional. SemiAnalysis models only **~15GW of net-new ELCC (accredited, firm) capacity added annually**, rising toward 20GW+ by decade-end, against a datacenter buildout that runs **+21GW in 2026 to +84GW by 2030** — and that thin firm-capacity stream must also serve non-datacenter firm load (industrial plants, semiconductor fabs). Available headroom, defined as accredited supply minus peak demand minus required reserves, is already near zero and turns negative across a growing set of subregions by 2027. The confirming datapoints are physical, not sentiment: US gas additions run **below 10GW/year in 2026 and 2027**; NERC's 2025 Long-Term Reliability Assessment flags **13 of 23 North American assessment areas** with resource-adequacy shortfalls; PJM's 2027/2028 Base Residual Auction cleared roughly **6.6GW short** of its reliability requirement (14.4% reserve margin against a 20% target). Renewables do not close the gap — solar and BESS each add 20GW+ nameplate per year but are accredited at steep, widening ELCC discounts (the duck curve for solar; duration-saturation for storage), so nameplate massively overstates firm contribution.

BTM is the only path to power for the largest buyers because the grid-connected route is gated by time, not money. The interconnection queue is no longer the binding constraint in PJM — conversion is: ~57GW has cleared studies and been offered agreements, yet since 2020 about **24GW of fully-executed projects (including 13.5GW of gas) terminated before commercial operation** on permitting, supply-chain, and financing failures. CCGTs — the efficient way to burn gas — are the slowest build of any generation type at 4–6 years to COD; gas-turbine and generator step-up transformer lead times have each stretched to **3–4 years versus an ~18-month historical norm**, pushing total gas-plant development past four years even optimistically. BTM in-service dates cluster around **2027–28** while grid timelines routinely slip toward **2030**, and the schedule sits in the buyer's hands rather than a utility's (utilities revise down promised load with little to no penalty). For AI labs — OpenAI, Anthropic, and the hyperscaler capacity built to serve them — power is an insignificant share of total TCO but the gating input to billions in inference and training revenue per GW, so any multi-year delay is disqualifying. Faster onsite technologies (fuel cells, RICE reciprocating engines) are being secured directly by operators, and relaxed redundancy tolerance removes the historical BTM cost barrier: Meta's Prometheus and Ohio campuses target **two nines of uptime and forgo backup gensets entirely**, and the Ohio site is designed never to connect to the PJM grid at all.

The equipment-market implication reshuffles winners away from the obvious names. With BTM powering >50% of new datacenters from 2028 and TAM crossing 50GW/year by 2029, the beneficiaries are onsite generation OEMs — **Bloom Energy** (flagged by SemiAnalysis as the biggest beneficiary since December 2024), **INNIO, Wärtsilä, Bergen Engines** — while the big-3 gas-turbine OEMs (**GE Vernova, Siemens Energy, Mitsubishi**) are disproportionately exposed to the grid-connected buildout and face **2026 as a potential peak for turbine orders** as buyers pivot to 2028 BTM. The bridge structures are codifying fastest in ERCOT, where the Batch Zero process (NPRR1325 + PGRR145, effective July 11, 2026) formalizes co-location: Net-Metering Arrangements (NMA) tap existing generation, Bring-Your-Own-Generation (BYOG) adds new units, and Withdrawal-Limited PUN (WLPUN) plus Provisional Controllable Load Resource (PCLR) let a site connect far more load than transmission alone supports in exchange for an enforced grid-withdrawal cap. The fuel and firm-power adjacencies matter for the vault: BTM at GW scale is a natural-gas demand story ([[Theses/LNG - Cheniere Energy]]), and the largest co-location deals reach for nuclear baseload — AWS's 1,200MW campus adjacent to Vistra's Comanche Peak reactor is a 20-year PPA — which keeps the SMR / uranium leg ([[Theses/CCJ - Cameco]]) in the same firm-power contest. This source is the demand-side confirmation for the vault's power-bottleneck complex — the binding physical constraint of the cycle, per Perez [G-4] — but the crowded winner list is the reason the bottleneck confers scarcity rent, not a monopoly toll.

## Framework / Mental Model

The source presents a repeatable GW-accounting methodology — the **SemiAnalysis Energy Model** — that reconciles three forecast blocks into a single headroom number per subregion:

| Building block | Method | Key metric |
|---|---|---|
| Datacenter gross power demand | Bottom-up, building-by-building, cross-checked to a chip-by-chip Accelerator Model and a Tokenomics model | +21GW (2026) → +84GW (2030) |
| Available grid capacity (headroom) | ISO/RTO methodology; models UCAP/ICAP reserves, ELCC accreditation, reliability risk | Headroom → negative by 2027 |
| New grid supply | Bottom-up COD forecast across ~40,000 generation assets, all fuel types, quarter-by-quarter | ~15GW/yr net-new ELCC |

The load-bearing concept is **ELCC (Effective Load Carrying Capability)** — the "true" firm-capacity value of a plant to the system, distinct from nameplate. The headroom identity is deterministic:

`Headroom = accredited supply − peak demand − required reserves`

Headroom goes "red" when a market's reserve margin falls below its required target (commonly a 15–20% ICAP reserve, or PJM's 1-in-10 loss-of-load-expectation ~20% installed reserve margin). UCAP (accredited) headroom turns red before ICAP (nameplate) headroom because it nets out both thermal forced-outage risk and the steep ELCC discounts on renewables. The model's second repeatable insight is **declining marginal ELCC**: each incremental GW of a given resource is accredited lower as it saturates the specific grid-risk window it addresses (4hr BESS nullifies sub-4hr risk, then adds little; solar's value collapses as correlated midday output floods the duck curve). The argument then runs in three deterministic steps — (1) grid supply is structurally constrained → (2) the constraint pushes the marginal buyer behind the meter → (3) the shift reshuffles OEM and IPP winners across islanded and hybrid BTM. This is a genuine framework (named methodology, GW-accounting identity, transferable ELCC/headroom logic), so it is retained rather than folded into Evidence.

## Evidence

**Datacenter buildout vs firm grid supply (GW/year)** `[web: semianalysis]` `[1×: SemiAnalysis Energy Model]`

| Year | New DC gross demand | Net-new ELCC (firm) grid capacity | Gas nameplate added |
|---|---|---|---|
| 2026 | +21GW | ~15GW | <10GW |
| 2027 | (ramping) | ~15GW | <10GW |
| 2028 | (ramping) | ~15GW+ | picks up |
| 2030 | +84GW | toward 20GW+ | higher |

**BTM share of new datacenters and equipment TAM** `[web: semianalysis]`

| Metric | Value | Note |
|---|---|---|
| BTM share of new US DCs | >50% from 2028+ | "well over half" |
| DC-BTM equipment TAM | crosses **50GW/year by 2029** | fully-islanded + hybrid |
| BTM in-service date cluster | 2027–28 | vs grid slipping to ~2030 |
| Top-tier developer BTM plans | 5GW+ behind-the-meter facilities (Texas) | permitting onsite gas easier in ERCOT |

**Grid-shortfall corroboration** `[web: semianalysis]` `[est.]`

| Datapoint | Value | Source detail |
|---|---|---|
| Grid headroom inflection | negative by 2027 | UCAP basis, growing set of subregions |
| PJM 2027/28 BRA shortfall | ~6.6GW (6,517MW UCAP) | 14.4% reserve margin vs 20% target |
| NERC 2025 LTRA shortfall areas | 13 of 23 | resource-adequacy over next decade |
| PJM terminated projects since 2020 | ~24GW executed (incl. 13.5GW gas) | permitting / supply-chain / financing |
| Gas turbine + GSU transformer lead time | 3–4 years | vs ~18-month historical norm |
| CCGT planning-to-COD | 4–6 years | slowest generation build type |

**Named BTM equipment winners / losers** `[web: semianalysis]`

| Category | Names | Positioning |
|---|---|---|
| BTM winners (fuel cells + RICE) | **Bloom Energy**, INNIO, Wärtsilä, Bergen Engines | flow of 2028 buyer demand; Bloom flagged biggest beneficiary since Dec-2024 |
| Grid-exposed / peak-order risk | GE Vernova, Siemens Energy, Mitsubishi | carry the grid nameplate forecast; **2026 = potential peak turbine orders** |
| Secondary-market signal | turbine availability "surging" | overcoming GEV/Siemens capacity constraints "far easier than feared" |
| ERCOT IPP BYOG play | NRG | ~5.4GW BYOG, ~$2.5bn incremental EBITDA, first power ~late 2029 |

**ERCOT co-location deals (~2,885MW reported, existing-generation bucket)** `[web: semianalysis]` `[est.]`

| Developer / site | Load | Structure |
|---|---|---|
| Crusoe — Goodnight | 525.5MW (265.5 + 260) for a ~1GW IT campus | NMA; +TCEQ filing up to 933MW gross gas (~665MW = 19× GE Vernova LM2500) |
| AWS — Comanche Peak | 1,200MW co-located at Vistra nuclear | 20-yr PPA, full ramp by 2032 |
| CyrusOne — Thad Hill | 400MW (190 + 210) at Calpine plant | NMA |
| CyrusOne / Constellation — Freestone | 760MW potential (380 contracted) | NMA via Calpine/Constellation |
| Microsoft–Chevron — Project Kilby | ~2.67GW, West Texas | 20-yr agreement (comp for NRG deal math) |

**Regulatory catalysts** `[web: semianalysis]`: FERC's December 2025 order directed PJM to create co-location rules and opened Docket RM26-4 on faster interconnection of loads >20MW; PJM's Expedited Interconnection Track (~10-month study) was accepted June 12, 2026; ERCOT's Batch Zero constructs (NMA / BYOG / PUN / WLPUN / PCLR) took effect July 11, 2026, with SB6's September 1, 2025 vintage trigger separating existing-generation NMAs from new BYOG builds.

## Contradiction Check

**Does the 50GW/yr BTM-equipment TAM strengthen the [[Theses/BE - Bloom Energy]] thesis? Partially — on the demand leg only, and the source hands over the datapoint that caps the rest.**

- **BE §Bull Case + §Key Non-consensus Insight 1 ("time-to-power arbitrage") + §Conviction Trigger → HIGH.** The BE bull case rests on the power bottleneck being "structural and durable (grid to ~2035, turbines to ~2030)." SemiAnalysis independently models exactly that: negative accredited headroom by 2027, grid-connected timelines slipping to 2030, and only ~15GW/yr of firm capacity against +84GW/yr demand. This directly supports the *first half* of the BE → HIGH trigger's precondition ("turbine backlogs remain >4 years" / grid stuck) and the Insight-1 falsifier ("grid interconnect + turbine backlogs stay >4 years through 2029 → the arbitrage becomes an annuity"). SemiAnalysis's claim that fuel cells and RICE are "aggressively secured directly by datacenter operators" because CCGTs are too slow reframes Bloom's 50–90-day deployment as *structurally demanded*, not merely a temporary arbitrage — a lean against the BE thesis's own "wasting asset" framing on the demand side.
- **The cap: BE §Industry Context (Value-Layer-Monopoly WEAK FIT) + §Bear Case.** The → HIGH trigger requires *both* a durable bottleneck *and* audited RPO >$3B plus a repeat Tier-IV primary-power hyperscale win — SemiAnalysis speaks only to the first. It says nothing about Bloom's backlog quality (the $20B-vs-$492.6M RPO gap), Tier-IV reliability at GW scale, or related-party revenue — the actual thesis cruxes. And its winner list (Bloom, INNIO, Wärtsilä, Bergen "and many others") plus "surging" secondary-market turbine availability is affirmative evidence for the BE thesis's **WEAK FIT** Value-Layer-Monopoly call: a 50GW/yr TAM split across fuel cells, reciprocating engines, and newly-available turbines is scarcity demand, not a Bloom-monopolized layer. **Net: strengthens BE demand / bottleneck-durability; does not lift conviction (stays low), because the binding variables — RPO, Tier-IV, and the 2028–29 digestion repricing — sit where this source is silent.**

**[[Theses/VRT - Vertiv Holdings]] §Key Non-consensus Insight 5 ("grid interconnect is the real chokepoint; Vertiv benefits regardless of direction").** SemiAnalysis is a direct corroboration of the *physical-scarcity* leg — negative headroom by 2027, PJM ~6.6GW short, transformer/turbine lead times 3–4 years — matching the existing insight and the Layer-1 grid shortage. It also **reinforces the caution already appended to that insight** (from [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]): the "regardless of direction" leap does not follow. The source's islanding and lower-redundancy trend cuts against the grid-interface / backup slice of Vertiv content — Meta's Ohio campus never connects to PJM and Prometheus omits gensets at two-nines — while PCLR / load-flexibility structures *redistribute* the constraint (demand response, curtailment) rather than uniformly forcing more content per site. Vertiv's core white/grey-space stack (UPS, busway, CDU, rack PDU, BBU/supercap, 800VDC) is largely power-source-agnostic and survives the BTM shift; the grid-interconnect switchgear and genset-backup content does not. **Net: supports VRT grid-chokepoint framing (physical leg); no conviction change; mild negative for the backup/grid-interface sliver, consistent with the standing caution.**

**Tension with [[Macro & Technology/Sustainability of AI Capex]].** The macro's base case is a 2028–29 capex *digestion* (5–6x coverage gap; capex "flat to down in 2029 as depreciation and financing discipline expose weak cohorts"). SemiAnalysis's +84GW-by-2030 buildout and 50GW/yr BTM TAM are a demand-*continues* trajectory — a direct tension on the 2028–2030 magnitude. Partial reconciliation: the macro explicitly exempts "power bottlenecks" from the correction ("concentrated in contestable capacity rather than the qualification-gated silicon, networking, memory, and power bottlenecks"), so if power is a genuine gated bottleneck (SemiAnalysis's whole argument), BTM-equipment demand is more resilient than merchant-GPU capacity. But the BE thesis warns Bloom — levered, GAAP-unprofitable, ~55x book — "reprices hardest" in the digestion regardless of whether its end-demand is real. **The two documents disagree on trajectory but agree power is the more durable leg; the swing variable is whether BTM equipment is priced as a bottleneck or as AI-capex beta.**

**Support for [[Macro & Technology/800VDC Adoption]].** SemiAnalysis's grid Layer-1 evidence — 3–4 year transformer/GSU lead times, permitting and supply-chain conversion failure — independently corroborates the 800VDC macro's "bottleneck cascade Layer 1" (grid → MV AC: 128-week transformer lead times, structural shortage, Korean transformer trio / Hitachi Energy beneficiaries). The grid-shortfall and BTM shift are orthogonal to the *inside-the-datacenter* 800VDC transition (driven by rack current density, not grid access), so 800VDC content is preserved under either power-sourcing outcome — a clean, non-contradictory overlay.

**Mental-model triggers (hypotheses to test, per the READING PROTOCOL):**
- **Generalist [G-4] · Perez — power/grid is the binding physical constraint.** *Hypothesis:* this cycle's frenzy-phase over-build needs a physical substrate (as railway gauges / electricity grids did prior surges); here the grid itself is the binding constraint and BTM is the installation-phase capacity laid down ahead of grid catch-up. The +84GW/50GW-TAM buildout is the substrate; whoever *uses* it cheaply later may not be the equipment builders funding it now.
- **Semis [#8] analog · bottleneck relocation.** *Hypothesis:* the AI scale transition remaps scarcity from silicon (CoWoS, HBM) to power generation + grid interconnect; reading the relocation before it prices is the alpha, and this source dates the relocation (headroom red 2027).
- **Semis [#1] · bottleneck = pricing power — tested and partially failing.** *Hypothesis to disconfirm:* whoever supplies the scarce BTM layer gets asymmetric pricing power. The disconfirming datapoint the source itself supplies — crowded winner list + "surging" secondary-market turbine availability + turbine constraints "easier than feared" — argues the BTM-equipment supply response is *elastic*, unlike a qualification-gated semi bottleneck. Per the protocol, cross-model agreement ("power is scarce → buy BTM equipment") is the trigger to hunt the falsifier; the elastic, multi-vendor supply is it.
- **Value-Layer-Monopoly · BTM generation as an emerging layer — WEAK FIT confirmed.** *Hypothesis:* is onsite generation a durable layer everything above must traverse? The source's data (many vendors, loosening turbine chokepoint) supports the BE thesis's WEAK FIT: real input scarcity, but non-rivalry fails (hardware, per-unit cost) and durability is contestable. Scarcity rent, not a monopoly toll.

Corroborates directionally with [[Research/2026-07-17 - Power 10x Musk Turbine Bet AI Bottleneck - deep-dive]] (power as the 10x AI bottleneck / turbine-supply framing) and [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]] (separates equipment scarcity from supplier pricing power). Sector home: [[Sectors/Data Center Power & Cooling]].

## Source Excerpts

> "BTM will power well over half of new US datacenters in 2028+, and the Total Addressable Market (TAM) for DC BTM equipment to cross 50GW/year by 2029. New Grid Capacity isn't growing fast enough, and also needs to serve non-datacenter load growth."

> "Our forecast points to barely 15GW of net-new ELCC capacity being added annually, with a rising trend towards 20GW+ by the end of the decade... available headroom is already approaching zero and turns negative by 2027."

> "Overcoming GEV and Siemens turbine capacity constraints proved far easier than many had feared... We see 2026 as a potential peak for turbine orders for the big 3 OEMs. Most buyers will be focused on 2028, and that's going to flow to Bloom, Innio, Wartsila, Bergen and the likes."

> "The key advantage of BTM vs Grid is speed and certainty on the timeline of power... requested BTM in-service dates cluster around 2027–28, against grid timelines that routinely slip toward 2030."
