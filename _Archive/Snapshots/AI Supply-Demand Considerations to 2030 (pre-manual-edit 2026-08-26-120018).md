---
snapshot_of: "[[Macro & Technology/AI Supply-Demand Considerations to 2030]]"
snapshot_date: 2026-08-26
snapshot_trigger: manual-edit
snapshot_batch: manual-edit-2026-08-26-120018
publish: true
date: 2026-08-25
tags: [macro, technology, ai-compute, token-economics, HBM, power-grid, neoclouds, semiconductors]
status: active
sector: Cross-sector (AI Compute)
source: internal synthesis — session 2026-08-25, web-verified (TrendForce, SemiAnalysis, Goldman, Epoch AI, IEA, vendor disclosures)
---

# AI Supply-Demand Considerations to 2030

## Summary

Token supply capacity grows at roughly 3x per year through 2028; the identity is physical build (energised watts +40-50%/yr, HBM bit stock +55-60%/yr) multiplied by fleet-average efficiency (×1.7-2.0/yr on a measured basis, not vendor marketing). Token demand, compounding at 5-9x through mid-2026 and forecast here at ~3.5-4.5x (2027) fading to ~2.5-3.5x (2028), runs above that supply line through 2027 and converges to it during 2028. The consequence for pricing is a market that stays in managed famine through 2027, normalises rather than gluts in 2028, and carries rate discipline into 2029-30 on the power gate alone, with the genuine glut window opening 2029-30 only if a financing discontinuity converts backlog into idle capacity. Scarcity does not clear primarily through the posted token price: it clears through a cascade (training reallocation, internal squeeze, queues, price discrimination, posted price last), which is why the blended price signal is damped while the marginal price signal, the fast-tier/batch spread and the merchant GPU-hour, carries most of the information. GPU-hour rates and token prices decouple through the efficiency engine: a flat contracted GPU-hour delivers a $/token that falls 2-2.5x per year, and this decoupling is the stable equilibrium the neocloud model requires; the famine premium on top of it is cyclical and decays as demand converges with supply. We hold the balance of evidence at: demand at or above the balance line to late-2028 (~50%), extended famine (~25%), demand-side or financing-led glut (~20-25%).

## 1. Supply: two physical gates and one efficiency engine

Token capacity = physical input × tokens per unit of input. Both physical gates bind simultaneously at different stages: HBM gates what NVIDIA can package, watts gate what operators can energise, and token supply is set by the last stage in the chain. The wedge between them (silicon shipped but not powered) is a paid queue of weeks to months, not a stranded surplus, absorbed by inventory, old-fleet displacement, NVIDIA's configuration valve (memory per package rises when watts are scarce: ~80-110 GB/kW on Blackwell to ~200-240 GB/kW on Rubin Ultra's 1TB packages), and geographic reallocation to whoever has watts and export approval.

| Gate | 2026 | 2027 | 2028 | Mechanism |
|---|---|---|---|---|
| HBM bit flow | +30-35% | +50-60% | +40-60%E | 2026 masked by HBM4 wafer-to-bit penalty (wafer share 18%→22%, bit share 8%→9%); 2027 yields mature |
| HBM installed stock | ~×1.6 | +~60% | +~55% | ~×2.5 end-2026→end-2028; young fleet, flow-dominated |
| Energised AI watts (global) | +55-65% | +45-50% | +35-42% | US achievable +14-18 / +20-25 / +28-35 GW/yr; ex-US (Gulf, Asia) adds ~5pts |
| Fleet-average efficiency | ×1.7-2.0/yr | ×1.7-2.0/yr | ×1.7-2.0/yr | new silicon ~2.5x fleet average on the year's additions; software harvest ~1.3-1.4x on the standing fleet |
| **Token capacity** | **~×3** | **~×2.9-3.2** | **~×2.7-3.2** | ×8-12 cumulative end-2026→end-2028 |

The memory side of the constraint is severe but dated: all three vendors sold out 2026 and 2027 before those years began, Micron can serve 50-67% of key-customer 2027 demand, HBM4 contract prices are negotiated to roughly double into 2027 ($2/Gb toward $4-5/Gb), and NVIDIA has evaluated de-specced Rubin Ultra memory configurations to fit supply, which is the accelerator roadmap bending to memory. The relief wave is clustered: M15X full ramp mid-2027, Samsung capacity ~+50% through 2026, Micron Hiroshima equipment 2H28, Amkor Arizona and ASE K18B in 2028, CoPoS 2H28-29. The DRAM complex as a whole grows only ~16% (2026) because HBM cannibalises DDR5 wafers at ~3:1 per bit, and conventional DRAM pricing (+93-98% QoQ in 1Q26) is the pressure valve.

The power side outlasts it. The additions engine is bounded by delivered heavy equipment rather than permitting for anyone willing to build behind the meter: global gas-turbine manufacturing runs ~60-70GW/yr against 110GW of 2025 orders with slots sold through 2029-30, GSU transformers quote 128-144 weeks, and the grid-connected route is effectively closed in PJM (8-year timelines, 220GW queue, zero fast-track megawatts energised) while ERCOT/BTM compresses land-to-energised to 18-30 months. Realisation runs 50-60% of schedule. The two largest builders guide to doubling their fleets in two years (~41%/yr), which is the cleanest self-declared ceiling. China sits outside the constraint in both directions: domestically watts-rich and silicon-poor (>400GW of annual generation additions against export-controlled accelerators), so its Ascend-class token supply leaks into the global commodity tier, while its electrical-equipment complex (transformers, switchgear, solar-plus-storage) is the elastic margin that loosens the Western BTM gate.

The efficiency term deserves the most scrutiny because it is two-thirds of supply growth and carries the widest vendor-to-measured spread: Blackwell was marketed at 30x Hopper and benchmarked at ~4x throughput at ~1.7x power; Rubin's '10x lower cost per token' rests on one MoE configuration, and we expect ~2.5-3.5x per GPU on independent prints. The fleet-average construction (additions at ~2.5x fleet average, standing fleet harvesting ~1.3-1.4x from software maturation) is what produces ×1.7-2.0/yr; chaining the per-generation and software headline numbers would produce ~7x/yr and is the standard double-count.

## 2. Demand: the balance line and the composition shift

The balance condition is thus: demand must compound ~3x per year (~×10 cumulative to end-2028, i.e. today's ~6-10 quadrillion tokens/month reaching ~60-100 quadrillion) for the current pricing structure to hold. The labs' own internal growth budgets (OpenAI 2.2x, Anthropic ≤4x for 2026) bracket this line, which we read as the industry procuring supply for a ~3x demand world.

Measured demand runs above it: Google 9.7T→480T→3.2 quadrillion tokens/month (April 2024→May 2025→May 2026), OpenAI 6B→15B tokens/min in five months, OpenRouter 25T/week with agentic volumes up 14x in six months, aggregate ~5-9x YoY. Two distortions roughly offset: rationing (rate limits, quota tiers, $496B of AWS backlog) means the prints understate demand at current prices, while tokens-per-task compression (Opus 4.5 delivering with 76% fewer output tokens) means token demand grows structurally slower than task demand.

The composition is the forecast. Token intensity per seat spans two orders of magnitude, so aggregate growth is increasingly set by the agentic S-curve alone:

| Segment | Penetration (mid-2026) | Intensity per seat/mo | Share of tokens | 2027E | 2028E |
|---|---|---|---|---|---|
| Consumer / prosumer chat | ~25-30% of internet users; ~5-7% paid | 1-5M | ~45-55% | 2-3x | ~2x |
| Agentic coding | ~15-25% of ~35M devs seated; ~10% intense | 50-400M (50-100x a prosumer sub) | ~15-25% | 3-4x | 2.5-3x |
| Enterprise workflow agents | ~2-5% (agents scaling in ≤10% of functions; adopters ≤3 functions) | comparable to coding, always-on | ~5-10% | 5-8x | 4-6x |
| Autonomous / background fleets | <2% | unbounded (no attention governor) | ~3-5% | 5-10x | 4-8x |
| Lab-internal (RL, synthetic, evals) | n/a — residual claimant | n/a | ~10-15% | 3-5x | 3-5x |

Blended: ~3.5-4.5x in 2027, ~2.5-3.5x in 2028 with the top half favoured, because by 2028 agentic workloads are ~60-75% of all tokens and the aggregate converges to their growth rate. The gate on enterprise depth is organisational rather than technical (the dynamo pattern: firms took decades to reorganise around electric motors because the gain required redesigning the factory), and as such it gates depth, not direction: adoption compounds for a decade rather than saturating in three years, which is precisely the profile that holds demand near the supply line for years rather than swinging through it. Into 2029-30 we expect the aggregate to fade toward ~2-2.5x as coding saturates and enterprise depth grinds on organisational clocks, with the volume/dollar wedge (tokens 3-7x against enterprise AI dollars 1.5-4x) persisting throughout.

## 3. Price formation: the cascade, the convexity, and the decoupling

Scarcity clears in sequence, and the posted price is the last absorber: training↔inference reallocation (the swing capacity, worth ~15-30% of frontier fleets, visible only as model-release slippage), lab-internal squeeze, queues and rationing, price discrimination (fast-tier surcharges, batch discounts), and only then the posted sheet. This ordering explains 2025-26: an enormous overhang produced +40% on the one-year H100 contract index, 2x fast-tier surcharges, and selective posted increases (GPT-5 at $1.25/$10 to GPT-5.5 at $5/$30; Gemini Flash repriced ~3x with a scheduled January 2027 step) while constant-capability prices kept deflating ~10x/yr underneath (GPT-4-class at $0.40/M; Opus 4.5 cut 67%). Both moves are real; they are different tiers of one market.

Convexity comes from three mechanisms. First, 80-90% of capacity is price-fixed under take-or-pay, so aggregate imbalance concentrates on the 10-20% merchant sliver, the same structure that turns a 5% electricity reserve shortfall into a 10-50x balancing-market spike, damped here because a delayed token has a cheap substitute in the same token later. Second, clearing is sequential across elasticity tiers (internal exits first, commodity substitutes down, the ~-0.2 elasticity frontier residual pays whatever it must), so each additional point of overhang meets a steeper remaining demand curve. Third, visible shortage induces reflexive over-ordering (backlogs compounding at +$25-130B per quarter across CoreWeave and AWS), which inflates measured commitments beyond demand-in-use and guarantees the eventual unwind overshoots. Our estimated response curve for a sustained overhang: 10% moves blended prices +3-5% and spot +15-30%; 33% (a 4x demand year against 3x supply) moves blended +20-40% and merchant spot +150-300%; the same structure runs in reverse with a harder crash, because supply cannot exit above cash electricity cost (the 2024 H100 template: ~-65% on perhaps 15% slack).

The agentic composition shift raises this convexity through 2027-28. Latency-sensitive agents cannot queue (an agent blocked mid-task is a human waiting, and the labour arbitrage breaks), so they exit the rationing absorber and enter the priority-priced tier; intelligence sensitivity compounds per step (95% per-step reliability across a 20-step chain completes 36% of tasks, 99% completes 82%), so agentic demand concentrates on the frontier model and cross-elasticity to cheap substitutes collapses. The posted price hikes of 2026 arrived as agentic share crossed ~25-30% of tokens; as that share passes half, the same overhang buys more price response. The fast-tier/batch spread (~4x today, ~8-10x in famine) is the single cleanest live gauge of scarcity.

For GPU-hours the load-bearing fact is the decoupling: at a flat contracted rate, $/token falls 2-2.5x/yr through efficiency pass-through, so falling token prices and firm GPU-hour rates coexist indefinitely provided demand absorbs capacity, and the famine premium (rates above the cost-plus ladder) is the only cyclical component. The Rubin ladder runs ~$8.20 deployment floor (drifting toward ~$9 as doubled HBM4 feeds fleet capex), $9.60-12 balance, $12-15 famine. In a watt-bound regime the rate decomposes into 'watt-rent' plus 'silicon-rent': the +40% repricing of three-year-old H100s is watt-rent, it does not decay with silicon age, and it accrues to whoever owns the energised slot, which is why re-rent steps for power-owning operators should land above the ~55% modelling convention while silicon economic life compresses (a Rubin-capable watt filled with Hopper forgoes 4-6x tokens/MW). The durable asset is the powered megawatt; the depreciating one is the silicon inside it.

## 4. Trajectory to 2030

| Window | Supply | Demand | Regime | Token prices | GPU-hr | Neocloud marginal ROIC |
|---|---|---|---|---|---|---|
| 2026-27 | ~3x/yr | 3.5-4.5x | managed famine | frontier premiums hold/extend; commodity deflates | at/above contract ladder; renewals above launch | famine rows, 22-30%+ |
| 2028 | ~3x/yr; HBM wave lands | 2.5-3.5x, converging | normalisation, not glut | famine premium decays; frontier resumes glide | new contracts cost-plus $9.60-12 | 18-22% |
| 2029-30 | power gate eases (turbine slots open, BTM engine ~50GW/yr); efficiency compounds | fading toward 2-2.5x | balance, tipping glut-ward if financing breaks | commodity deflation dominates; frontier premium episodic | merchant softens first; contracted vintages insulated to 2030-31 | new signings at hurdle ~15%; watt-rent supports re-rents |

Scenario weights: soft normalisation ~50%; extended famine ~25% (enterprise depth, computer-use and video compounding >4x into 2028, in which case frontier posted prices keep rising and the famine rows persist into 2029); glut ~20-25%, and the realistic trigger is financing rather than adoption: hyperscaler capex crossed above operating cash flow around Q3 2026, every prior infrastructure cycle broke on a 25-30% capex cut by an anchor buyer, and the reflexive-backlog unwind then converts precautionary commitments into idle capacity just as the 2028-29 supply waves land. Perez [G-4] frames the shape: the over-build is functional, installs the substrate, and the financiers of the frenzy are rarely the deployment-era winners.

## 5. Observables (ranked by information value)

| Signal | Current reading | Threshold that changes the view |
|---|---|---|
| Independent Rubin fleet benchmarks (InferenceMAX-class, 2H26) | pending | ≥3x measured per-watt vs Blackwell → supply cap leaks, famine ends earlier; ≤2x → shortage extends |
| Google/OpenAI token prints vs the 3x line | ~5-9x YoY | a print annualising <2.5x is the first genuine demand warning |
| Fast-tier/batch price spread | ~4x | sustained widening toward 8-10x = famine deepening; narrowing <3x = convergence arriving |
| 1-yr GPU contract index + first Rubin renewals | H100 $1.70→$2.35 (+40%) | renewals above launch ladder = famine; re-rents landing 35-40% = glut leg |
| Energised-vs-shipped wedge | Stargate 0.3/9GW; idle-chip commentary | NVDA inventory days stretching quarters → watts strangling silicon; then HBM orders wobble with a 2-3q lag |
| 2027-28 HBM bit revisions; Samsung Rubin HBM4 share | +50-60% 2027; Samsung 25-30% | share >40% erodes the Hynix rent; bit growth >70% pulls glut forward |
| Hyperscaler capex guidance vs operating cash flow | crossover ~Q3 2026 | first anchor-buyer cut of 25-30% = the glut trigger, worth more than any demand datapoint |
| Tokens-per-task in frontier releases | Opus 4.5 −76% output tokens | systematic 2x+ annual compression caps token demand below the balance line even in a strong adoption world |
| DDR5/HBM4 contract pricing | +93-98% QoQ 1Q26; HBM4 ~2x into 2027 | conventional DRAM rolling over = memory cycle peaking (equities lead the physical peak ~12 months) |

## 6. Affected theses

- [[Theses/000660 - SK Hynix]] — the memory-gate rent through 2027-28: HBM4 pricing ~2x, 2027 sold out, roadmap de-specs confirming excess demand; the erosion vector is Samsung's Rubin share, not the cycle.
- [[Theses/NBIS - Nebius Group]] / [[Sectors/Neoclouds & GPU-as-a-Service]] — the watt-rent thesis and vintage insulation; energisation prints are the sector's highest-information disclosures; companion frame in the Website essay on neocloud economics.
- [[Theses/NVDA - Nvidia]] — owner of the configuration valve between the two gates; watch HBM cost pass-through and the inventory-days tell.
- [[Theses/TSM - Taiwan Semiconductor]] — CoWoS has left the binding set (gap 20%→10%); packaging scarcity premium fading even as volumes compound.
- [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell]] — ASIC share of the energised-watt pool is the quiet share shift inside the supply number.
- [[Theses/SNDK - SanDisk]], [[Theses/285A - Kioxia]] — conventional-memory squeeze beneficiaries of the 3:1 wafer cannibalisation.
- [[Theses/LRCX - Lam Research]], [[Theses/AMAT - Applied Materials]], [[Theses/KLA - KLA Corporation]], [[Theses/ASMI - ASM International]] — the 2027-28 memory-capex wave is the order book; L2 (structurally higher troughs) is the frame.
- [[Theses/VICR - Vicor Corporation]], [[Theses/VRT - Vertiv Holdings]], [[Theses/BE - Bloom Energy]], [[Theses/LNG - Cheniere Energy]] — the BTM complex is the elastic margin of the power gate; scarcity rent without a monopoly toll.
- [[Theses/SPCX - SpaceX]] — the existence proof for the BTM fast path (~1GW in six months); its energisation cadence rewrites the buildout base rate.

## Mental Models

- Generalist [G-10] · base-rate check — no computing input has sustained rising unit prices over a multi-year window; the frontier token tier is currently violating this. Hypothesis to test: regime break (agentic inelasticity) vs unsustainable famine artefact; the 2028 convergence call assumes the latter.
- Generalist [G-14] · Jevons elasticity — commodity-tier deflation keeps unlocking latent workloads, which is why demand fades toward the supply line rather than through it; a rising-price world would choke the very migration the demand thesis requires.
- Generalist [G-4] · Perez frenzy — capex>operating-cash-flow crossover (Q3 2026) plus vendor financing is the frenzy signature; the glut scenario is financing-led, not adoption-led.
- Generalist [G-3] · reflexivity — backlog-as-demand feeds the overshoot both directions; measured commitments ≠ demand-in-use.
- Semis #1 · bottleneck relocation — logic (2021) → CoWoS (2024) → HBM (2026) → watts (2027-28); the alpha is in re-identifying the binding segment before consensus.
- Semis #7 · units-and-price phase read — units up + prices up across HBM, DDR5, GPU rentals and frontier tokens = shortage confirmed at every layer.
- Semis #17 / #18 · supply lag and cycle-vs-structural decomposition — 18-30 month lags hold; the 2028 normalisation vs 2029-30 glut question is the live decomposition.
- Semis L1 · contracted memory — LTAs and the 1Q26 HBM-below-DDR5 margin inversion remove the incentive to over-add HBM specifically; discipline hypothesis intact.
- Lens - Value Layer Monopoly — rent lands at owned layers (HBM qualification gate, NVIDIA allocation, energised megawatts); the token layer is the contestable layer and reprices last; its repricing at all is the measure of the shortage.
- Lens - Automation & AI Readiness — enterprise depth is organisationally gated (dynamo pattern), which shapes demand as a decade-long grind rather than a spike; the same lens caps the bull case for a uniform enterprise inflection.

## Related Research

- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]
- [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]]
- [[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]]
- [[Research/2026-08-16 - Macro PJM - SemiAnalysis 12B Modeling Mistake - deep-dive]]
- [[Research/2026-08-18 - SPCX - 10GW Datacenter Pipeline Feasibility - deep-dive]]
- [[Research/2026-07-12 - Enterprise AI Adoption - Gating Factors Critique, 2030 Trajectory, Winners-Losers - synthesis]]
- [[Macro & Technology/Sustainability of AI Capex]]
- [[Macro & Technology/DRAM Memory Cycle - Duration, Peak Timing and Second-Order Effects]]
- [[Macro & Technology/Agentic Internet]]
- [[Sectors/DRAM & HBM Memory]]
- [[Sectors/Compute & AI Compute Accelerators]]
- [[Sectors/Data Center Power & Cooling]]
- [[Website/2026-08-22 - Neoclouds - The Property Developers of Compute]]

## Log

- 2026-08-25: Note created — synthesis of session on HBM/power supply gates, token demand balance line (~3x/yr), price-formation cascade/convexity, and GPU-hr/token price decoupling to 2030. Verified via three web sweeps (HBM/CoWoS supply, token demand/pricing, power capacity) + vault power complex.
