---
snapshot_of: "[[Macro & Technology/AI Supply-Demand Considerations to 2030]]"
snapshot_date: 2026-08-26
snapshot_trigger: manual-edit
snapshot_batch: manual-edit-2026-08-26-123020
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

The cost side closes the identity: cost per energised watt-year is flat (~$6.5 accounting on a 7-year accelerator and 25-year shell; ~$10.6 with the cost of capital charged), so the industry's cost of producing tokens grows with energised watts rather than with tokens: token-serving COGS ~$75B (2026) → ~$420B (2030), the full AI fleet ~$150B → ~$600B, against tokens ×40 and cost per token ÷7. Compute expenditure runs 2-2.5x measured AI revenue (~$300-400B in 2026 against $165B) because training, hyperscaler internal workloads and open-weight serving all pay for watts without appearing as AI revenue; every energised watt has a payer, and the compute layer earns ~1.4-1.7x its economic cost today, a famine multiple that normalises toward 1.0x as watts quadruple, without any deepening of the shortage. Neocloud margins hold only if compute expenditure grows with total watts, ×4 by 2030; the base case delivers ~×3-3.5, which lands new fleets at the 15% hurdle (§7).

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
| Rent per MW-yr on new Rubin paper vs energised-watt growth (compute-dollar demand ÷ watts) | contracted $21-26M ($9.60-12/GPU-hr); merchant H100 +40% YoY | new signings below $17.6M ($8.20) = 15% floor breached; above $26M with renewals above launch = famine extends (§7) |
| Blended realised $/M tokens at the labs vs the serving cost curve | Opus 4.7 agentic ~$0.99/M realised on a $5/$25 sticker; serving cost ~$0.75/M accounting | price falling faster than ~1.5x/yr on the mix = Jevons pass-through, revenue per capex dollar falls; slower = labs keep the efficiency gain and the bridge holds (§7) |
| Payer mix of compute expenditure (revenue-funded / franchise-funded / training / open-weight and sovereign) | 2026 ~35% / 20% / 30% / 10%; compute expenditure ~2-2.5x measured AI revenue | revenue- and profit-funded share rising = durable demand, famine multiple normalises to the hurdle; equity-funded training share rising = the financing trigger moves forward (§7) |

## 6. Affected theses

- [[Theses/000660 - SK Hynix]] — the memory-gate rent through 2027-28: HBM4 pricing ~2x, 2027 sold out, roadmap de-specs confirming excess demand; the erosion vector is Samsung's Rubin share, not the cycle.
- [[Theses/NBIS - Nebius Group]] / [[Sectors/Neoclouds & GPU-as-a-Service]] — the watt-rent thesis and vintage insulation; energisation prints are the sector's highest-information disclosures; companion frame in the Website essay on neocloud economics. §7 sets the margin condition: rent per watt holds iff total compute dollars grow with total watts (×4 by 2030); the base-case bridge lands new fleets at the 15% hurdle, and the share-of-supply point (neoclouds ~10% of energised watts, pipelines implying 15-20% by 2028) is thesis-level, not industry-level.
- [[Theses/NVDA - Nvidia]] — owner of the configuration valve between the two gates; watch HBM cost pass-through and the inventory-days tell.
- [[Theses/TSM - Taiwan Semiconductor]] — CoWoS has left the binding set (gap 20%→10%); packaging scarcity premium fading even as volumes compound.
- [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell]] — ASIC share of the energised-watt pool is the quiet share shift inside the supply number.
- [[Theses/SNDK - SanDisk]], [[Theses/285A - Kioxia]] — conventional-memory squeeze beneficiaries of the 3:1 wafer cannibalisation.
- [[Theses/LRCX - Lam Research]], [[Theses/AMAT - Applied Materials]], [[Theses/KLA - KLA Corporation]], [[Theses/ASMI - ASM International]] — the 2027-28 memory-capex wave is the order book; L2 (structurally higher troughs) is the frame.
- [[Theses/VICR - Vicor Corporation]], [[Theses/VRT - Vertiv Holdings]], [[Theses/BE - Bloom Energy]], [[Theses/LNG - Cheniere Energy]] — the BTM complex is the elastic margin of the power gate; scarcity rent without a monopoly toll.
- [[Theses/SPCX - SpaceX]] — the existence proof for the BTM fast path (~1GW in six months); its energisation cadence rewrites the buildout base rate.

## 7. Unit economics: the token cost identity and the industry COGS line

Cost per token is a ratio of one flat quantity and one compounding one. The numerator, cost per energised watt-year, is flat because shell, substation, switchgear and cooling plant scale with watts, and because NVIDIA prices each generation to hold system dollars per watt while performance per watt rises (GB300 $37.4/W against Vera Rubin $38.1/W marketed IT capex despite TDP 1,400W→2,300W; [Epoch](https://epoch.ai/data-insights/ai-datacenter-cost-breakdown) $38B/GW all-in on a GB200 build; Foxconn ~$47B/GW all-in on Rubin; Goldman's VR200 at $80.5K per GPU and 3 kW is ~$27/W compute-only). The denominator, tokens per watt-year, compounds ×1.7-2.0 a year on a measured fleet basis (§1). Electricity is 4-12% of the numerator, so a doubling of delivered power price adds 5-10% to the cost of a token, roughly six weeks of efficiency; its availability is the supply line, and the price signal of the watt gate is the GPU-hour, not $/MWh. As such the industry's cost of producing tokens grows at the rate watts energise, not at the rate tokens are served, and efficiency absorbs the difference. Memory is the one component breaking the flat numerator into 2027 (a VR NVL72 rack at $7.8-9.1M carries $2-3.2M of HBM4 and LPDDR5X; HBM4 contracts ~2x into 2027); the 2028 relief wave and Rubin Ultra's 8-Hi despec take it back while Kyber 600 kW racks and NVL576 optics add, so we hold capex per all-in watt within ±15% of $45/W to 2030.

**Cost per all-in utility watt, Rubin-class new build (~$47/W).** Accounting recovers the principal over the asset's life; the economic basis recovers principal and the required return, an annuity at 15% over seven years on IT and 10% over 25 years on the shell. Per Rubin GPU ($183K) that is $20.3K against $36.5K a year, and the $16K gap is the profit the asset must earn every year to have been worth buying. Reported gross margins use the first basis; the neocloud deployment floor ($8.20/GPU-hr) uses the second. Life moves the accounting figure (a 5.5-year accelerator life gives $8.0/W-yr) and the economic one barely, because a longer life spreads the principal while the return on it keeps accruing.

| Component | Capex $/W | Life | Accounting $/W-yr | Economic $/W-yr |
|---|---:|---:|---:|---:|
| Accelerators + HBM/LPDDR (dies ~$15, memory ~$10) | ~25 | 7 yr | 3.6 | 6.0 |
| Other IT: CPUs, NVSwitch, scale-out network, storage | ~7 | 7 yr | 1.0 | 1.7 |
| Shell, substation, switchgear, UPS, cooling plant | ~15 | 25 yr | 0.6 | 1.65 |
| Electricity (8.76 kWh per W-yr at ~$90/MWh; PUE inside the watt) | | | 0.8 | 0.8 |
| Maintenance, staff, water, property tax, insurance | | | 0.5 | 0.5 |
| **Total** | **~47** | | **~6.5** | **~10.6** |

**Tokens per watt: the generational gain and the interactivity tax.** On SemiAnalysis's renormalised CoreWeave data ([DeepSeek R1, output tokens, all-in MW](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference)) Rubin NVL72 serves 1.33M tokens/s per MW at 50 tok/s/user, 886K at 135, 96K at 300 and 71K at 350: 42T tokens per MW-year at the batch end and 2-3T at the fast end, a 14-19x spread, which on the economic stack is $0.31 per million output tokens against $4-6, and on realised terms (60% utilisation, a 0.4 penalty for frontier model size and agentic context) roughly $1.3 against $18. The generational multiple therefore depends on where the comparison sits: ~2x GB300 at ≤100 tok/s/user, ~4x at 200, 5.4x at 300 where GB300's frontier ends; NVIDIA's own [24 August claims](https://developer.nvidia.com/blog/nvidia-vera-rubin-and-blackwell-set-a-new-standard-for-agentic-ai-performance-per-watt/) of 2x/10x/30x at 110/130/160 tok/s/user on DeepSeek V4-Pro are pending independent review, and the 10x headline is against a 2025 GB200 stack. Two consequences carry into the supply arithmetic of §1. Agentic composition (§2) pushes the fleet's operating point up the interactivity curve, where tokens per watt is 10-20x worse, so realised fleet efficiency lags the benchmark generational gain and the fast-tier/batch price spread is also a tokens-per-watt spread. And the source of the ~2x-per-generation 'free' multiplier is the precision ladder, FP16→FP8→FP4→Rubin's 3.125-bit LUT; below ~3-4 bits accuracy fails, so after Feynman (2028, A16, kernel rewrite) the gain must come from node (backside power ~1.3x), HBM bandwidth, SRAM-first decode (the Groq LPX licence, marketed at 35x per MW) and co-packaged optics, and the base rate for process-only gains is ~1.3-1.5x a year. We thus expect fleet efficiency to fade from ×1.7-2.0 (2026-28) toward ×1.4-1.7 (2029-30). Held as a hypothesis against §4: supply growth fades alongside demand in 2029-30, which narrows the glut window rather than widening it; the falsifier is a Feynman print at ≥2.5x per watt with no further precision drop.

**The COGS line, 2026-2030.** Token-serving COGS is defined at the physical layer: depreciation of the inference fleet, shell and power amortisation, electricity and operating cost. It excludes training compute (R&D), model development, the cloud or neocloud rental markup (a transfer inside the industry: a lab renting Rubin capacity reports COGS at 1.5-2.5x the physical figure in a famine) and SG&A. Watts follow §1 (19 GW installed at end-2025, derived from ~$1.0-1.2T of AI capital invested through 2026 at $35-47B/GW; additions +55-65% / +45-50% / +35-42%, then an easing gate); the inference share of the fleet rises from 50% to 70%; tokens served follow the supply line in §2 (×10 to end-2028) and fade to ×2-2.5 a year after. Cross-checks: Big Four D&A of $170B rising to $260-300B by 2028 with ~60% of AI depreciation on inference gives $200-250B of 2028 serving cost; ~1e17 tokens in 2026 at ~$0.75/M realised gives ~$75B; Epoch's GB200 build annualises at $8.5M per MW-year with energy at 7%.

| | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Installed AI capacity, year-average (GW, all-in utility) | 24 | 37 | 52 | 71 | 96 |
| Inference GW (share 50% → 70%) | 12 | 20 | 31 | 46 | 67 |
| Fleet accounting cost per W-yr (7-yr IT, 25-yr shell) | $6.1 | $6.5 | $6.5 | $6.3 | $6.2 |
| **Token-serving COGS, accounting ($B)** | **75** | **133** | **203** | **291** | **417** |
| YoY | | +77% | +53% | +43% | +43% |
| Token-serving COGS, economic basis ($B) | 120 | 215 | 325 | 465 | 670 |
| Tokens served, year-end run-rate (quadrillion/month; mid-2026 = 8) | 14 | 40 | 100 | 220 | 450 |
| Tokens served, calendar total (quadrillion) | 100 | 300 | 800 | 1,900 | 4,000 |
| Serving COGS per million tokens, accounting | $0.75 | $0.44 | $0.25 | $0.15 | $0.10 |
| **Total industry COGS, all AI watts, accounting ($B)** | **149** | **241** | **338** | **447** | **595** |
| YoY | | +62% | +40% | +32% | +33% |
| Total industry COGS, economic basis ($B) | 240 | 385 | 540 | 715 | 950 |
| End-buyer AI revenue bridge ([[Macro & Technology/Sustainability of AI Capex]]) ($B) | 165 | 290 | 450 | 630 | 850 |
| Revenue coverage of total COGS, accounting / economic | 1.1x / 0.7x | 1.2x / 0.75x | 1.3x / 0.8x | 1.4x / 0.9x | 1.4x / 0.9x |

Serving cost compounds at +53% a year and the full fleet at +41%, against tokens ×40 and cost per token ÷7; the slope is the watts line and the level is the life assumption (accelerator-plus-memory depreciation alone is ~$230B of the 2030 serving figure and ~$330B of the total; a 5.5-year life lifts the accounting rows ~20%; the economic rows are ~1.6x accounting and insensitive to life). The outside view [G-10] is the IEA path, AI-focused electricity tripling by 2030, which gives ~40 GW of 2030 inference capacity, ~$250B of serving cost and ~$370B for the fleet; we hold ×3.3-5.5 as the range with the vault path at the top end because the BTM engine and China's watts-rich build sit outside a grid-based count. If tokens stall at ×10 after 2028 the COGS rows do not change, since they are committed two to three years ahead; 2030 cost per token is ~$0.40 rather than $0.10, utilisation falls toward a third, and the watts line breaks by financing in 2029, stranding $120-200B of the 2030 cost base. That is the §4 glut case in cost terms.

Two readings of the coverage row. On these lives the industry is gross-profitable all-in throughout (1.1x rising to 1.4x), which is the version the hyperscalers will report; on the economic basis measured AI revenue does not pay the fleet's cost of capital before 2031 (0.7x rising to 0.9x), which is the 5-7% spot ROIC of [[Macro & Technology/Sustainability of AI Capex]] restated from the cost side: a stack-level test of end-customer revenue against the whole fleet's capital, not the compute layer's demand line, which runs 2-2.5x higher because training, internal workloads and open-weight serving pay for watts without appearing as AI revenue (next subsection). One inversion follows: the bull case for serving margins is the slow power path, since scarcity holds COGS growth near +35% a year and revenue per watt high, and the fast BTM build the power complex is paid to deliver is what drives the cost base to $600B and margins down.

### Who pays for the watts, and what the compute layer earns

Measured AI revenue understates compute demand by 2-2.5x, because most of what pays for energised watts never appears as an 'AI revenue' line. Building 2026 compute expenditure by payer, i.e. what the compute layer receives at rent or transfer price for every energised watt:

| Payer, 2026 | Compute expenditure ($B) | Rent tier per MW-yr | Funded by | Durability |
|---|---:|---|---|---|
| End-customer revenue: cloud AI services plus the labs' inference compute cost (~30-40% of token revenue) | 110-140 | $12M to ~$100M (frontier API at the top) | Enterprises and consumers | Grows with the revenue bridge |
| Hyperscaler internal: ad ranking, search, recommendations, bundled copilots | 50-100 | $12-15M transfer price | Ad and search franchise cash flow | Most durable of the four; scales with usage, not with an AI price |
| Training, labs and hyperscalers | 100-120 | Contracted $20-26M | Raised equity, vendor finance, and increasingly the labs' own gross profit | Fragile while equity-funded; self-funding as token gross profit compounds |
| Open-weight serving, enterprise self-hosting, sovereign clusters | 25-40 | Mostly $10-15M, the residual bidder (sub-$30M) | Enterprise IT budgets, states | Low rent, high watt share; fills what the frontier labs do not take |
| **Compute-layer receipts** | **~300-400** | **Fleet average $14-17M** | | |
| vs total economic COGS $240B / accounting COGS $149B | **1.4-1.7x / 2.0-2.7x** | | | |

Every energised watt has a payer, so there is no air gap at the compute layer: it earns ~1.4-1.7x its economic cost in 2026, about +$100-160B of economic profit and +$150-250B above accounting COGS, with the neocloud's contracted 2x and the frontier lab's 4x at the top of a wide dispersion and internal transfer and open-weight serving at the bottom. The 0.7x measured-revenue coverage in the table above answers a different question, the whole stack's return on end-customer revenue, which is what [[Macro & Technology/Sustainability of AI Capex]] asks of the labs' and hyperscalers' shareholders; it is not the compute layer's demand line. Open-source usage is the clearest case of the gap between the two: a fifth to a third of tokens run on open weights at sub-$1/M, small in revenue and large in watts, paid at the residual rent.

What differs between payers is duration, not whether they pay. Training paid from equity is the tranche that stops when financing reprices (tranches C and D in the capex note), but as the labs' gross profit compounds it becomes self-funded: Anthropic at $44B ARR and a 70%+ inference margin can fund $20-30B of training from gross profit, and on the bridge lab gross profit reaches ~$300B by 2030, enough for $150-250B of training without external capital. That is the installation-to-deployment handover in [G-4], and it makes the four payers correlated rather than independent: all scale with token revenue, and the financing tranche fails only in the world where the bridge is missed.

The industry balances on this basis in the ordinary way. Rent per watt, compute expenditure divided by watts, drifts from 1.4-1.7x economic cost toward ~1.0-1.2x as watts quadruple and expenditure grows ~×3-3.5; the famine multiple normalises without any deepening of the shortage, and the watt-owner's spread compresses in the same move. A deeper shortage would raise the multiple on every payer at the payers' expense; it is not required for balance, and it leaks back into the cost line through the next generation's $/W.

### The neocloud margin condition

The proposition to test: as long as dollar demand for tokens meets the COGS line, the neocloud industry maintains its current margin and grows at the supply rate, and if demand exceeds the line, economics improve. It holds in structure and must be stated on all watts and all payers, because about half of neocloud capacity serves training and its customers pay from revenue, franchise cash and raised equity alike. Rent per watt-year is total compute expenditure divided by energised watts; the cost per watt-year is flat; so the spread holds if and only if compute expenditure grows with total watts (×4 on year-average watts, 24 → 96 GW, i.e. ~$300-400B → ~$1.2-1.6T by 2030), widens above that and narrows below. Reference points per Rubin-class MW-year: famine $26-32M ($12-15/GPU-hr), the balance ladder $21-26M ($9.60-12), the 15% IRR floor $17.6M ($8.20), reported breakeven ~$7M (~$3.0-3.5 at a 7-year life); today's contracted rent sits at ~2x economic cost and ~3.5x accounting cost, and the cushion to the floor is ~25%.

| 2030 case | Revenue-funded compute (~75% of end revenue) | Franchise-funded internal | Training (gross profit + financing) | Open-weight, enterprise, sovereign | Total compute $ | Rent per watt vs 2026 | New-fleet economics |
|---|---:|---:|---:|---:|---:|---:|---|
| Bridge hit (end revenue ×5 to $850B) | $550-700B | $100-200B | $150-250B | $75-100B | ~$0.9-1.25T | −15 to −25% | Contracted rents fall from $21-26M toward $17-21M: at or just above the 15% floor. §4 balance row |
| Bridge missed by a third (end revenue ×3.3 to ~$550B) | $375-450B | $100-150B | $100-150B | $50-75B | ~$0.65-0.8T | −40 to −50% | Below the $17.6M floor on new Rubin fleets; equity-funded training stops first. §4 glut row |
| Above the bridge (end revenue ×6-7) | $750-900B | $150-250B | $250-350B | $100B+ | ~$1.3-1.6T | ~flat | Famine rows persist. §4 extended-famine row |

The base-case bridge thus consumes the whole cushion by 2030: neoclouds earn the hurdle on new fleets, not today's spread. Because the four payers are correlated (all scale with token revenue), the useful split is not revenue versus financing but bridge-hit versus bridge-missed, and the number to watch is end-customer AI revenue against the ×5 path. Three refinements to the proposition follow. 'Current margin' is a famine multiple, so holding it is the above-bridge case, and no industry has compounded revenue 50% a year for four years from a $150B base (cloud managed 35-40% at $50-100B). 'Grows at the supply rate' is a share statement that belongs in the NBIS thesis (neoclouds hold ~10% of energised watts, with contracted pipelines implying 15-20% by 2028 if energisation and NVIDIA's allocation hold); at the industry level it reduces to the payer mix staying weighted to revenue- and profit-funded compute as the fleet quadruples. 'Economics improve' at the industry level is true on all watts, and the contract structure only decides who takes the surplus first (labs through posted prices and gross margin, as in 2025-26; watt-owners at renewal; then the silicon layer through the next generation's $/W, which is how a famine leaks back into the cost line, as the 2026-27 memory surge shows); the ceiling is the end customer's value per token rather than GPU-generation parity, the measured response is damped by take-or-pay (§3: +3-5% blended per 10% overhang), and the crash side is harder. Underneath sits the financing point: three capex programmes underwrite most disclosed backlog, so the aggregate can meet the line while one anchor's 25-30% cut converts a slice of contracted paper into disputed paper.

Restated: compute expenditure must grow ×4 by 2030 to keep today's margins; the base case delivers ~×3-3.5, so margins compress to the hurdle; a third shortfall on the bridge takes new fleets below the floor; better than the bridge is needed for the famine spread to persist. The observables in §5 that read this directly are the rent per MW-year on new Rubin paper against energised-watt growth, the blended realised price per million tokens at the labs against the serving cost curve, and the payer mix of compute expenditure.

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
- Generalist [G-7] · ROIIC × runway, cost-side — tokens per capex dollar (~×15 by 2030) is the physical yield; revenue per capex dollar is the return, and the two diverge by the price-deflation rate. Hypothesis: the return variable for every layer is rent per watt, not tokens per watt (§7).
- Generalist [G-11] · accounting vs economic basis — a 7-year accelerator and 25-year shell make the fleet gross-profitable on reported numbers (coverage 1.1-1.4x) while sub-hurdle on an economic basis (0.7-0.9x). Hypothesis: reported neocloud margins stay positive well past the point where new fleets stop clearing 15%, so the accounting print is a lagging signal.
- Generalist [G-10] · base rate on the revenue bridge — holding famine margins needs compute dollars at +45-60%/yr for four years from a $150-180B token base; cloud managed 35-40% at $50-100B. Hypothesis to test against the January-February 2027 capex guides and the first post-surge Rubin paper.
- Semis #4 / #8 · tech-curve race and architecture remap — the precision ladder (FP16→FP8→FP4→3.125-bit) is the exhausting lever behind ×2/gen tokens/W; after Feynman the gain relocates to memory bandwidth, SRAM-first decode and CPO. Hypothesis: fleet efficiency fades to ×1.4-1.7 in 2029-30, narrowing the §4 glut window; falsifier: a Feynman print ≥2.5x/W at fixed precision.
- Lens - Value Layer Monopoly · claw-back — excess compute-dollar demand improves neocloud economics only on the uncontracted sliver and is partly recaptured by the layer owner (NVIDIA system pricing, allocation) and by the labs' cascade. Hypothesis: the durable neocloud variable is the renewal rate on the next contract, not the spot print.
- Generalist [G-4] · installation-to-deployment transfer — compute expenditure (~$300-400B) is 2-2.5x measured AI revenue and the compute layer earns ~1.4-1.7x economic cost, paid by four correlated payers (revenue-funded, franchise-funded, training from equity then gross profit, open-weight residual). Hypothesis: the industry balances as the famine multiple normalises with watts ×4, not as monetisation 'catches up'; the financing tranche fails only where the bridge is missed. Falsifier: rent per watt holding while watts quadruple (a value-layer regime, not a famine).

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
- [[Research/2026-07-23 - Vera Rubin NVL72 vs GB200 Inference TCO - deep-dive]]
- [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]
- [[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]]

## Log

- 2026-08-25: Note created — synthesis of session on HBM/power supply gates, token demand balance line (~3x/yr), price-formation cascade/convexity, and GPU-hr/token price decoupling to 2030. Verified via three web sweeps (HBM/CoWoS supply, token demand/pricing, power capacity) + vault power complex.
- 2026-08-26: Manual edit (session, user-directed) — added §7 unit economics: token cost identity, cost per watt-year on a 7-yr accelerator / 25-yr shell (accounting vs economic basis), tokens/W interactivity tax and precision-ladder fade, the 2026-30 token-serving and total-industry COGS lines vs the revenue bridge, and the neocloud margin condition (assessment of 'demand meets COGS ⇒ margins hold'); Summary, two §5 observables, §6 NBIS pointer, five Mental Models hypotheses and three Related Research links added — framework unchanged; §4 glut window flagged as narrower (held as hypothesis).
- 2026-08-26: Manual edit (session, user-directed) — §7 extended: per-layer economic-return split (who earns above the 15% rate, who pays), the monetised-share × multiple decomposition (fleet covers 0.7x → 0.9x of economic cost via monetisation, not deeper shortage), margin condition restated on all watts (total compute dollars ×4 by 2030; base case ×3-3.5 lands new fleets at the hurdle), share point relegated to thesis level; Summary, §5 monetised-share observable, §6 pointer and one [G-4] hypothesis updated — framework unchanged.
- 2026-08-26: Manual edit (session, user-directed) — §7 reframed on payers: compute expenditure by payer (~$300-400B, 2-2.5x measured AI revenue; every watt paid, compute layer at 1.4-1.7x economic cost), training and internal workloads treated as paid-for demand of differing duration rather than an unmonetised gap, margin-condition scenarios recut as bridge-hit / bridge-missed / above-bridge; Summary, §5 payer-mix observable and the [G-4] hypothesis updated — framework unchanged.
