---
publish: true
date: 2026-05-15
tags: [thesis, neoclouds, GPU-as-a-Service, AI-infrastructure, CRWV]
status: monitoring
conviction: medium
sector: Neoclouds & GPU-as-a-Service
ticker: CRWV
source: CoreWeave Q1 2026 earnings (May 7 2026, $2.08B revenue, $99.4B backlog), DDTL 4.0 facility disclosure (March 2026, $8.5B IG-rated GPU-collateralized debt), NVIDIA $2B follow-on equity investment (January 2026), [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]]
key_metrics_last_refreshed: 2026-07-12
---

# CRWV - CoreWeave

## Summary

CoreWeave is the cleanest equity proxy for the bet that hyperscaler AI capex cannot keep pace with foundation-lab training demand through 2027, and that NVIDIA will systematically redistribute allocation to non-hyperscaler operators to keep the cloud layer fragmented. The operating story is best-in-class (56% adj EBITDA margin Q1 2026, $99.4B backlog, first IG-rated GPU-collateralized debt). The non-consensus question is whether the business is a structurally independent compounder or a high-quality levered derivative on NVIDIA chip economics and a 3-counterparty hyperscaler capex cycle. Consensus prices it as the former; the analytical evidence (67% Microsoft revenue, $40B+ in new commitments in a single quarter from Meta + Anthropic, NVIDIA's 13% equity stake, $46B liabilities against $3.3B equity) favours the latter. The position is sized around credit risk and counterparty disclosure cadence, not the AI demand story.

## Key Non-consensus Insights

**1. Counterparty concentration is mis-disclosed, not under-disclosed.** Sell-side flags 67% Microsoft as the concentration risk and accepts management's guidance that the share will "decline below 50% as OpenAI and Meta ramp." The actual risk is the opposite of decline: the OpenAI contract is $22.4B and Meta is $14B+, and the combined OpenAI + Meta + Anthropic addition to Q1 backlog was over $40B in a single quarter, so the mix shift away from Microsoft mechanically increases concentration to OpenAI (which has no operating cash flow and is itself financed by Microsoft) and to a small set of frontier labs whose training programs all face the same architectural-efficiency obsolescence risk. The market is treating the diversification narrative as risk-reducing; the mix shift is risk-redistributing within a tighter counterparty cluster. Lucent's 1999-2001 telco-capex concentration is the closest historical analog: Nortel and Lucent both believed customer diversification mattered while the underlying capex cycle was single-factor. *2026-08-15 Temple 8 Q2 cluster* (Meta +$21B, multi-year Anthropic, Jane Street $6B, backlog $104B excl. >$25B Q3 commitments) [1×: Temple 8] challenges the "no diversification" phrasing only at the surface: Jane Street is a new vertical, Meta is the existing cluster, Anthropic is unsized versus the $5B+ HIGH conjunct, so the insight's "risk-redistributing within a tighter counterparty cluster" read is not broken.

**2. The DDTL collateral mechanic is bull-cycle pattern recognition, not durable credit analysis.** The DDTL 4.0 facility's A3/A-low investment-grade ratings (Moody's, DBRS) are anchored on covenant DSCRs computed against contracted GPU rental rates, not market-clearing rates. GPU spot prices have already fallen 50-70% from peaks per debt-market commentary while underlying DDTL collateral is referenced at acquisition cost or original contracted rates. The 5-7 year initial-contract period creates an "amortization-cliff" structure: covenants hold while contracts are in primary term, then re-rent economics determine the back-end. If second-cycle re-rent rates compress at the rate Dylan Patel flagged (see [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]'s cluster-resign mechanic only works up to a bound), the IG rating is a backward-looking artifact, not forward credit protection. Jim Chanos has flagged this publicly; the market has not re-priced the credit.

> [!question] 2026-05-16
> Explain this dynamic further including pulling Jim Chanos' arguments

**3. NVIDIA's $40B+ AI equity portfolio is vendor financing dressed as strategic validation.** NVIDIA's stake in CRWV (~13%, $4.7B value), Nebius ($2B, ~10%), Nscale ($2B), Lambda, Crusoe, and ~$30B in OpenAI constitute a self-referential investment loop: NVIDIA invests equity → operator/lab uses proceeds to buy NVIDIA GPUs → NVIDIA reports revenue → operator reports backlog → NVIDIA stake appreciates with mark-to-market. The structural identity with 1999-2001 telco vendor financing (Lucent customer loans to CLECs) is precise; the historical outcome was 70-90% drawdowns at the financier. NVIDIA's 28% portfolio concentration in CRWV alone is the early-warning marker. GPU demand is not fake. The non-consensus claim is that the equity-stake validation is being used as a substitute for independent credit and demand analysis by both sell-side and the rating agencies.

**4. Hyperscaler in-housing risk is asymmetric: Microsoft is structurally the most-incentivized to internalize, and CoreWeave is the most-exposed neocloud to that decision.** Microsoft has launched MAIA 200 (30% performance-per-dollar improvement over MAIA 100, TSMC 3nm, 216GB HBM3e) and is publicly cutting commitments to CoreWeave per reports during Q1 2026. The decision tree is mechanical: if MAIA scales and matches H100 economics on inference workloads, Azure does not need to renew the CoreWeave overflow contracts in 2028-2030. This is not a NVIDIA-wide risk (NVIDIA has 4-5 hyperscaler counterparties plus the entire training-frontier-lab demand cluster), but for CoreWeave it is a single-customer-loss event for 67% of disclosed revenue. The mainstream framing groups CoreWeave with NVDA as "AI infrastructure" exposure; this conflates a diversified upstream supplier with a single-counterparty-concentrated downstream lessee.

**5. The Weights & Biases acquisition is a defensive bet against MLOps-layer disintermediation, not a vertical-integration upside.** The $1.7B W&B price assumed CoreWeave could move the MLOps layer onto its compute and capture more developer surplus. The empirical evidence after 12+ months is that frontier labs (OpenAI, Anthropic, Meta AI) use proprietary internal MLOps stacks regardless of where they rent compute, and W&B's 1,400-organization customer base skews to mid-market AI teams that are not the marginal buyers of CoreWeave's largest GPU clusters. The acquisition's strategic logic was correct (capture more of the workflow above the metal) but the execution-friction is high and the revenue contribution is undisclosed and likely sub-$200M. Reading the W&B deal as "MLOps platform play" overstates the upside; reading it as "we needed a defensive moat against AWS SageMaker / Azure ML / GCP Vertex eventually charging GPU-cloud-margins-equivalent on the layer above us" frames it correctly as a cost of staying in the game.

**6. Rubin's marginal fleet is not automatically value-destructive; the contract wrapper is the economic moat, shifting the bear case from launch capex to coverage and the 2028–2029 roll.** The live model prices Rubin on $183K all-in and a $6 numeraire that is not CRWV's realized wholesale. At N=7, 100% five-year take-or-pay, lifetime EBIT is **$9 → $175K · $12 → $282K · $15 → $389K · $18 → $496K**. $9 fails the **$192K gross-book screen** (average EBIT / original cost = 15%) and **clears 15% IRR (18.4%, NPV +$17K)**. Value destruction vs a 15% WACC starts at **~$8.22**, not $9.50. The 1.8×–3.0× "deployment corridor" is retired: $10.60 is revenue-per-watt parity, not a slot test; replacing live $6 Blackwell is indifferent near **$13.75**. The decisive asset remains the five-year take-or-pay: at $12 a contracted GPU earns $282K versus $122K merchant (**+$160K lifetime EBIT, ~$118K NPV @ 8%**). Coverage below ~44% at $12 fails the screen. This weakens "Rubin capex doubles, therefore CRWV destroys value." It strengthens the existing failure mode: pre-surge vintages locked near $3–6, incomplete coverage that puts capacity on the merchant curve from day one, or a 2029 Hopper roll at 35–40% rather than 55%. CRWV's base 120K-Rubin build stays pretax-positive across $9–18, but the build adds ~$22B of debt; better fleet economics do not remove common equity's claim-stack risk. [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]

## Outstanding Questions

**1. What is the actual second-cycle re-rent rate on Hopper/H100 clusters coming off four-year initial contracts in 2026-2028?** Management discloses contracted backlog but not the rate at which expiring contracts are re-priced. This is the single most important data point for the DDTL covenant analysis. Disclosure trigger: Q3/Q4 2026 earnings if any 2022-vintage clusters reach re-rent; tracker: [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] flagged cluster-resign gross margin >35% but rate compression vs. original is unknown.

**2. How does OpenAI service the $22.4B CoreWeave commitment if its own revenue trajectory disappoints?** OpenAI's CoreWeave obligation runs to May 2031. OpenAI revenue is real but its cash flow profile remains opaque, and Microsoft's prepayments are the dominant funding source. If OpenAI's own commercial trajectory misses the consensus path (subscription revenue plateaus, enterprise API adoption slower than expected, agentic monetization delayed), the contract becomes a credit event for CoreWeave even if OpenAI continues operating as a going concern. Disclosure trigger: OpenAI 10-K equivalents (none expected pre-IPO), Microsoft 10-Q segment commentary on AI Azure ARR.

**3. Why has Microsoft cut commitments to CoreWeave during Q1 2026, and what does this signal about the 2028+ renewal cycle?** Multiple sources report Microsoft reducing CoreWeave commitments citing delivery issues and missed deadlines. Management has framed Microsoft mix declining as a positive (diversification). The contrary read: Microsoft has surveyed its options (MAIA, Azure-owned capacity, Nscale alternative at $23B GB300, Nebius at $19.4B) and is renegotiating CoreWeave's contracts harder than the 2027-2030 renewal cycle implies. Disclosure trigger: any Microsoft 10-K mention of CoreWeave by name; Azure capacity utilization commentary.

**4. What is the gross margin on the new Anthropic and Meta contracts vs. the historical Microsoft contracts?** The 71.7% FY25 gross margin and 56% Q1 2026 adj EBITDA margin are blended; if the marginal Anthropic / Meta / Perplexity contracts are priced at lower per-GPU-hour rates (because they had less negotiating leverage when signed mid-2025 GPU shortage vs. now), the corporate gross margin may compress as the contract mix shifts. Disclosure trigger: Q2/Q3 2026 earnings if management discloses any segmentation; alternative: RPO-to-revenue conversion rate analysis as new contracts hit recognition.

**5. Does the W&B acquisition close the MLOps disintermediation risk or merely buy time?** Foundation labs build proprietary MLOps; mid-market enterprises use W&B + cloud vendor stacks. If hyperscalers (AWS SageMaker, Azure ML, GCP Vertex) start charging GPU-cloud-equivalent margins on MLOps-layer services, CoreWeave's pricing power on the metal layer compresses even before any GPU rental rate normalization. Disclosure trigger: hyperscaler pricing changes on managed ML services; W&B-attached customer cohort growth disclosure.

**6. What is the depreciation policy on the Hopper / Blackwell / Vera Rubin fleet, and is it aggressive enough?** CoreWeave depreciates GPUs over a useful life that the 2025 10-K disclosed as 5-6 years. Dylan Patel's claim that GPUs can be re-signed at >35% gross margin in years 5-8 supports the policy, but only if H100 inference demand absorbs the older fleet. If Vera Rubin economics are sufficiently better that frontier labs stop wanting Hopper for any workload, the older fleet hits residual-value impairment before depreciation catches up. Disclosure trigger: any impairment charge in 2026-2027 10-Q filings; secondary-market GPU pricing (DGX-Hopper used market).

**7. How much of CRWV's gross margin is sustainable post-debt-service ramp?** Adj EBITDA margin of 56% looks attractive, but interest expense was $311M in Q3 2025 (tripled YoY) and Q2 2026 guide is $650-730M. Annualized interest expense at the new run-rate is $2.6-2.9B against guided $12-13B revenue → roughly 22% of revenue. Net margin remains negative through 2026 even on management's bullish path. *Q2 2026 print ([[Research/2026-08-14 - LITE CRWV NBIS NVDA - Temple 8 Earnings Week 500B MOU - deep-dive]])*: revenue $2.575B (+112%), adj EBITDA $1.51B at 59% margin (above the 40% CLOSE line), FY guide $12.4–$13.2B / capex $35–$39B, **net loss widened to $626M vs $290M**, opex more than doubled and "marginally exceeded revenue." Temple 8: financing cost is moving the wrong way while credit conditions are "as good as the terms are going to get." Disclosure trigger: Q2 10-Q interest-expense run-rate vs the $650–730M guide; 2027 maturity wall.

**8. What cash Rubin rate and contract coverage does CRWV secure, and how much capacity is exposed to merchant pricing from day one?** The 15% IRR line is **~$8.22/GPU-hour**; the $9.50 figure is a gross-book accounting screen, not NPV. $10.60 is revenue-per-watt parity with a $6 Blackwell, not a deploy rule. The key disclosure is the absolute cash-equivalent rate, covered GPU/MW share, contract vintage vs the memory surge, cancellation/refund rights, and the age-six re-rent step, not headline backlog. *Answered by*: a dedicated Rubin contract or cohort disclosure; cash below ~$8.22 or coverage that puts the blend under the screen the IC is using validates the operating bear; near-full coverage at ~$12+ with a later re-rent near 55% would materially weaken it.

## Business Model & Product Description

CoreWeave operates a vertically-integrated GPU-as-a-Service platform: own the data centers, own the GPUs, sell GPU-hours on long-term contracts to hyperscalers and AI labs. Think of it as a hybrid of Equinix (real estate + power + interconnect), Coatue Black/AWS EC2 (instance rental), and Iron Mountain's specialty REIT model (collateralized lending against a depreciating physical asset class), with the analyst framing that's most useful being **"a specialty REIT for AI compute that finances the underlying asset class itself, with the tenants being a 4-5 hyperscaler/lab cluster instead of a diversified tenant base."**

**Compute platform.** 32+ data centers across North America and Europe house ~250,000+ NVIDIA GPUs (Hopper H100/H200, Blackwell B200/B300, Vera Rubin deployments H2 2026), networked with InfiniBand and direct-liquid-cooled at the highest rack densities in the industry (130 kW/rack public ceiling). 850 MW active power EOY 2025, projected 1.7+ GW EOY 2026, 3.5 GW contracted total. The cluster topology supports rack-scale NVL72 builds for frontier-lab training workloads. The bread-and-butter contract is multi-thousand-GPU dedicated clusters with 5-7 year terms, take-or-pay structure (96% of revenue is locked-in contracts; customer pays whether they use or not).

**MLOps platform (Weights & Biases).** Acquired May 2025 for $1.7B. Experiment tracking, model registry, evaluation, and observability tooling used by 1,400+ organizations and 1M+ developers. Strategic integration with the compute layer: customers using CoreWeave clusters get integrated W&B experiment-tracking and monitoring as a managed service. Revenue contribution is undisclosed and likely sub-$200M but the strategic logic is to capture more of the developer workflow above the metal and to defend against AWS SageMaker / Azure ML / GCP Vertex disintermediation.

**Revenue segmentation (heuristic, not formally reported).**

| Segment | Estimated % FY25 revenue | Notes |
|---|---|---|
| Microsoft (Azure overflow capacity) | 67% | Multi-year contracts, take-or-pay; reported declining as Anthropic/Meta ramp |
| OpenAI (Stargate-adjacent capacity) | ~12% | $22.4B total contract through May 2031; ramping |
| Meta (CoreWeave dedicated capacity) | ~5% (ramping) | $14B+ commitment signed Sept 2025 |
| Anthropic + other AI labs (Cohere, Mistral, Perplexity, World Labs, etc.) | ~10% | Multi-customer ramp through 2026; Anthropic deal April 2026 |
| Enterprise + financial services (Jane Street, Hudson River, etc.) | ~5% | Smaller dedicated clusters; higher margin per GPU-hour |
| W&B legacy software revenue | ~1% | MLOps platform; pre-existing W&B customer base |

The segmentation matters because the dominant pricing-power constraint flows through the Microsoft mix: as MSFT declines (management guidance: <50% by 2027), the marginal revenue is being added at rates negotiated when the AI labs were less price-sensitive but now in markets where Nscale/Nebius/IREN compete. Whether marginal gross margin compresses or expands is the central operating question.

**Unit economics (per disclosed Q1 2026 + 2025 10-K).**
- Gross margin: 71.7% FY25 (blended; pre-D&A and pre-interest)
- Adj EBITDA margin: 56.0% Q1 2026 (excludes D&A, SBC, interest)
- Operating margin: -0.9% FY25 (post-D&A; depreciation of ~$2.5B annualized on $30B+ asset base)
- Net margin: -23% FY25 (post-interest; interest expense alone consumed ~10% of revenue and ramping)
- FCF: -$7.3B FY25 (post-capex of $10.3B); FY26 capex guide $31-35B vs. revenue $12-13B → FCF accelerating negative through 2027

The model is "free cash flow positive on adj EBITDA, but cash-flow negative on operating after capex and ramping debt service": the same shape as a fast-growing telecom in the 1999-2001 cycle. The exit condition is either (a) capex tapers below D&A allowing FCF positivity around 2028-2029, or (b) debt service ramps faster than revenue and a credit event truncates the runway. The investment thesis stands or falls on which path materializes.

## Industry Context

CoreWeave sits in the **non-hyperscaler GPU infrastructure layer**, between NVIDIA (chip supply) and the customer cluster (hyperscalers buying overflow capacity + frontier labs buying training capacity + enterprises buying inference capacity). The category is structurally young (sub-3 years for the public-market version) and the competitive landscape is described in [[Sectors/Neoclouds & GPU-as-a-Service]]. The high-level competitive map:

| Layer | Player | CRWV relationship |
|---|---|---|
| **Upstream: chip supply** | NVIDIA (95%+ training-relevant GPU share) | Sole supplier; 13% equity holder; "MFN allocation priority" relationship |
| **Upstream: chip supply (competitive)** | AVGO (custom silicon design partner for Google TPU, Meta MTIA, OpenAI Stargate co-design) | Long-term pricing power compression vector; see [[Theses/AVGO - Broadcom]] |
| **Sidestream: pure-play neocloud peers** | Nebius (NBIS), Lambda (private), Crusoe (private), Nscale (private) | Direct competitors for hyperscaler overflow contracts; pricing race-to-bottom in spot ($8/hr H100 → <$2/hr) |
| **Sidestream: miner-pivot landlord model** | Applied Digital (APLD), Cipher Mining (CIFR) | $11B turnkey landlord relationship with APLD (CRWV is the tenant, not competitor); structurally durable model |
| **Sidestream: miner-pivot full-stack** | IREN | Direct competitor on Microsoft contracts ($9.7B IREN-Microsoft deal); same risk profile as CRWV |
| **Downstream: hyperscalers as customers** | Microsoft Azure (67% revenue), AWS, GCP | Customers in the near-term, competitors in the long-term as in-house ASIC scales |
| **Downstream: hyperscalers in-housing risk** | Microsoft (MAIA 200), AWS (Trainium 2/3), Google (TPU v6/v7) | The 2027-2030 demand-compression risk; see [[Sectors/Custom Silicon & Networking Semiconductors]] |
| **Downstream: frontier labs** | OpenAI, Anthropic, Meta AI, Mistral, Cohere, etc. | Growing share of backlog; concentration of model-architecture risk |
| **Adjacent: power + cooling** | Vertiv (VRT), Caterpillar generators, Bloom fuel cells | Neocloud customer base = 8-12% of VRT FY26E revenue at 38-42% gross margin per [[Theses/VRT - Vertiv Holdings]] |
| **Adjacent: edge alternative** | Cloudflare ([[Theses/NET - Cloudflare]] Workers AI), AWS Wavelength | Architectural competition for low-latency inference workloads (not training) |

**Pricing power is upstream-pinned at NVIDIA.** CoreWeave does not set GPU rental rates independently: its take-rate is constrained by the cost of NVIDIA chips on the supply side and by the rate at which Microsoft / Meta / OpenAI / Anthropic will pay on the demand side. The 56% adj EBITDA margin is real but it is a derived margin: if NVIDIA's gross margin compresses (currently ~75% but trending down as custom silicon ramps), CoreWeave's cost of goods rises; if hyperscaler in-housing accelerates, CoreWeave's pricing power compresses. The historical analog is the early 2000s competitive LEC layer: fiber infrastructure businesses sandwiched between upstream equipment (Cisco, Juniper, Lucent) and downstream incumbent telcos. The CLEC layer eventually proved economically untenable as bandwidth deflation outpaced operating leverage.

**Value chain position.** CoreWeave captures the spread between (a) NVIDIA chip + Vertiv-supplied infrastructure costs + Applied Digital landlord costs, and (b) Microsoft/Meta/OpenAI/Anthropic willingness-to-pay. The spread is currently wide because hyperscaler capex cannot scale fast enough to absorb training demand, but the spread is structurally one-way-compressible: every party adjacent to CoreWeave is incentivized to capture more of it (NVIDIA via equity stakes that ratchet allocation priorities, hyperscalers via MAIA/TPU/Trainium internalization, Applied Digital via long-term lease pricing power).

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | ~$48B (~$120/share, ~490M shares) | Mid-Q2 2026; range $43-200 12-month analyst targets |
| EV/Revenue (FY26E) | ~6.5x ($59B equity + $21.6B debt - $1.6B cash = $79B EV / $12-13B FY26 revenue) | Premium to AWS/Azure-comp (3-5x) but discount to early Snowflake-comparable hypergrowth (12-15x) |
| Revenue Growth (FY25→FY26E) | $5.13B → $12-13B = +134-153% | Q1 2026 +112% YoY; backlog 17x current revenue suggests multi-year continuation |
| Gross Margin (FY25) | 71.7% | Pre-D&A and pre-interest; the 56% adj EBITDA margin is post-SG&A but pre-D&A/interest |
| Operating Margin (FY25) | -0.9% | Post-D&A; $2.5B+ annualized depreciation |
| Net Margin (FY25) | -23% | Post-interest; interest expense ramping from $311M Q3'25 to $650-730M Q2'26 guide |
| FCF Yield (FY25) | -$7.3B / $59B market cap = -12% | Heavily negative through 2027 on management's own capex guide |
| Debt / EBITDA (FY25 trailing) | $21.6B / $2.4B = 9.0x | Levered for a hypergrowth name; DSCR covenants reference contracted rates |
| Total Liabilities / Equity | $46B / $3.3B = 14.0x | Aggressive even by REIT standards; vs. Equinix at ~2.5x |
| Backlog Coverage | $99.4B / $12-13B FY26E revenue = ~8x | RPO-to-current-year multiplier; longest of any public AI infrastructure name |
| NVIDIA Equity Stake | 13% ($4.7B at current price) | Up from 7% at IPO, 1.2% three years ago |
| Microsoft Concentration | 67% FY25 revenue | Management guides <50% by 2027 (mix-shift, not absolute decline) |

## Management and culture

Hypothesis: Inert on [[Lens - Management and Culture]]: Gate 1 passes (neocloud offtake/SKU/power/siting is a high-frequency feed); Gate 2 fails after the 11 Aug 2026 Q2 print ($104B backlog, Meta +$21B, Jane Street $6B): the MW pipeline is the sell-side compounder narrative this thesis already disputes, not priced at ≤0. Grade conversion on [G-7]/[G-8]/credit. [MC-2] 15 Apr 2026 DEF 14A: Class B 10-vote, Intrator 38.70% / three founders ~73.6% of votes; FY25 cash bonus 100% of target on discretionary corporate performance; LTI four-year time-based RSUs, no ROIC/EPS/product-volume metric; 10b5-1 sales, not clustered open-market buys (0 Form 4 purchases in the prior six months). [MC-7] 2,189 employees 31 Dec 2025 (881 YE2024). Q2 converted ~+500 MW to 1.5 GW / 51 sites; COO Jain (Aug 2024, Oracle/Google/Amazon) is the ops professionalisation. Debt-funded pace is founder-duration fighting mechanism for conversion speed; leverage vs [[Theses/NBIS - Nebius Group]] is [G-8], not MC. [MC-6]/[G-10]: Core Scientific termination 30 Oct 2025 and Q1 2026 Microsoft delivery misses are the entropy the dual-class claim has not retired.

## Bull Case

CoreWeave is structurally the best-positioned non-hyperscaler GPU operator in a market that is supply-constrained through at least 2027 and where the dominant customer cohort (hyperscalers + frontier labs) is signing 5-7 year take-or-pay contracts that lock in revenue visibility. The base case for 2030 is annualized revenue of $40-60B at adj EBITDA margins of 50-55%, implying $20-30B adj EBITDA, and a re-rating to specialty-REIT multiples (8-12x EV/EBITDA on stabilized operations) yields equity value of $160-360B vs. current $59B market cap.

The drivers that have to play out:
1. **GPU rental rates hold through second-cycle re-rents.** Dylan Patel's framing on Hopper economics (useful life extends to 7-8 years; cluster-resign gross margin >35%) has to materialize in CoreWeave's actual P&L disclosure through 2027-2028.
2. **Microsoft renews at 2028-2030 contract maturities, even at lower share of revenue.** The mechanical math is that Microsoft going from 67% to 40-45% is fine if absolute revenue grows 3-4x, but Microsoft has to renew most contracts, not walk away entirely.
3. **NVIDIA continues redistributing allocation toward CRWV vs. hyperscaler in-house ASICs.** The 13% equity stake is the strongest signal here; NVIDIA has every incentive to keep CoreWeave alive and scaling because the alternative is hyperscaler MAIA / TPU / Trainium captures CoreWeave's customer cluster.
4. **DDTL 4.0 IG rating holds through one credit cycle.** $8.5B IG-rated GPU-collateralized debt is a precedent; if it survives 2026-2027 spot-rate compression without covenant breach, the asset class is real and CoreWeave's cost of capital structurally compresses by 100-200bps.
5. **Vera Rubin contracts clear cash-rate and coverage tests, not a 1.8×–3.0× corridor.** CRWV is among the first cloud providers deploying Rubin in H2 2026. At **~$12/GPU-hour** the model generates ~$282K lifetime EBIT per $183K over seven years and clears both 15% IRR and the gross-book screen; the five-year take-or-pay adds ~$160K lifetime EBIT vs merchant (~$118K NPV @ 8%). The bull case requires near-full coverage at a cash rate that clears ~$8.22 IRR and a re-rent tail near the 55% blend, not just Rubin's headline performance gain.

**Valuation framework.** At $30B+ ARR by EOY 2027 (management guide), 50% adj EBITDA margin = $15B+ EBITDA. At 10x EV/EBITDA (specialty REIT, sustained 30%+ growth, IG-rated debt) = $150B EV → $130B equity (post-debt). At 25% per-year compounding from $59B current, that's a 5-year path. The bull case is "specialty AI REIT compounding at 25% with operational discipline."

## Bear Case

CoreWeave is a textbook late-cycle infrastructure-bubble vehicle whose business model assumes (a) NVIDIA chip economics hold up against custom silicon competition, (b) hyperscaler AI capex continues compounding at 30%+ annually for 4+ more years, (c) GPU rental rates do not compress faster than the DDTL amortization schedule, and (d) Microsoft / OpenAI / Anthropic / Meta all renew contracts in 2028-2031 without forcing rate compression. Each of these is contested, and the probability of all four holding simultaneously is structurally lower than the sum-of-parts narrative suggests.

The drivers that break the thesis:
1. **2026-2027 spot rate compression accelerates and infects contracted rates.** H100 spot has already fallen 50-70% per debt-market commentary. The corrected Rubin model weakens an automatic "new generation destroys value" claim: a fully contracted initial fleet at ~$12 cash clears 15% IRR and the gross-book screen. The bear instead requires one of three observable failures: pre-surge vintages locked near $3–6, incomplete coverage that puts Rubin onto the merchant curve from year one (screen fails below ~44% coverage at $12), or the 2028–2029 age-six re-rent step landing near open-market 35–40% rather than the modeled 55% blend. If the cluster-resign mechanic does not bridge to Vera Rubin economics (i.e., labs prefer brand-new Vera Rubin over re-signed Hopper at any price), the older fleet hits residual impairment and the DDTL collateral base deteriorates. Margin compression cascades through the P&L just as debt service ramps to $2.6-2.9B annualized, an interest burden that at ~25.8% of revenue already sits past the ~20-25% level at which the marginal leveraged builder historically broke in the telecom, railway and shale booms ([[Macro & Technology/Sustainability of AI Capex]]). That framework places CoreWeave in the most cyclically fragile tranche of the AI build (lab-serving, leveraged merchant capacity funded by debt/SPVs/prepays, the ~30-35% "where the correction will concentrate") and dates it: a 2028-29 capex digestion, or a deferred-but-sharper air-pocket if the complex first races its financing ceiling to exhaustion (the sector at ~90-100% of drawable leverage capacity, interest already at the break line). Either path, CoreWeave's profile (single-counterparty exposure, short-duration funding against fast-obsolescing hardware) is exactly what the correction selects first.
2. **Microsoft cuts CoreWeave commitments more aggressively than management has signaled.** Reports of Microsoft already reducing capacity during Q1 2026 may be the leading edge; MAIA 200 economics improving year-over-year, Azure-owned capacity scaling, and CoreWeave's "delivery issues and missed deadlines" framing all point toward Microsoft using the 2027-2028 renewal cycle to renegotiate rates 20-30% lower or shift volumes to in-house. A 25% cut to the Microsoft contract translates to ~$2B annual revenue impairment and is likely uncovered by Meta/Anthropic ramp.
3. **OpenAI revenue trajectory disappoints, $22.4B contract becomes a credit event.** OpenAI's commercial revenue is real but undisclosed in detail; if the consensus trajectory ($10B+ annualized exit to 2026 → $30-50B by 2027) misses by 30-50%, the OpenAI contract becomes the cleanest "neocloud counterparty default risk" disclosure event in the cycle. CoreWeave has no fallback customer to absorb $22B of dedicated capacity at short notice.
4. **DDTL covenants breach in 2027-2028 second-cycle re-rent shock.** The IG rating is forward-looking on contracted rates; if 2026-2027 spot rates remain 50-70% below contract rates and the first cohort of 2022-vintage Hopper clusters re-rents at heavy discount, DSCR covenants compress against the second-cycle period. Refinancing the $4.2B 2026 maturity is one event; refinancing a $20B+ DDTL stack in a credit-down scenario is a different problem.
5. **Custom silicon competitiveness scales faster than expected.** MAIA 200, Trainium 3, TPU v7 all show 30%+ performance-per-dollar improvements per cycle. The break-even for hyperscaler in-housing falls below outsourced GPU-cloud cost by ~2028. CoreWeave's structural ROI on Vera Rubin and beyond compresses just as the capex is deployed.

**Downside scenario.** Revenue plateaus at $10-15B (vs. $30B target), gross margins compress to 50%, operating margins remain negative through 2028, debt refinancing happens at 200bps higher coupon, and equity dilutes 30-40% to service the next refinancing tranche. Outcome: -60-80% drawdown from $59B market cap to $15-25B over 18-24 months. Comparable to Nortel 2001-2002 trajectory: not a zero, but a permanent capital impairment for late-cycle entrants.

## Catalysts

| Catalyst | Approximate timing | Direction |
|---|---|---|
| Q2 2026 earnings (revenue, interest expense run-rate, gross margin) | Aug 2026 | Both — bullish if margin holds with mix-shift; bearish if margin compresses |
| Microsoft contract renewal commentary | Q3-Q4 2026 | Both — bullish if any renewal disclosed at unchanged rates; bearish on rate cuts |
| Vera Rubin first deployments and customer wins | H2 2026 | Bullish if anchor customer wins; bearish if launch slips or pricing disappoints |
| First Hopper cluster re-rent disclosure | Q4 2026 - Q1 2027 | Both — the most informative single data point for DDTL durability |
| Microsoft MAIA 200 commercial deployment scale | 2026-2027 | Bearish — incremental evidence of in-housing acceleration |
| Next major AI lab contract announcement (likely xAI, Mistral expansion, sovereign-AI cloud win) | H2 2026 | Bullish — counterparty diversification beyond MSFT/OpenAI/Meta/Anthropic |
| 2027 maturity wall refinancing | Q1-Q2 2027 | Both — coupon disclosure reveals credit market pricing of CRWV-specific risk |
| OpenAI commercial revenue disclosure (any path) | Speculative 2026-2027 | Both — frames OpenAI's CRWV credit risk |
| Custom silicon ramp scale disclosure (NVDA / AVGO earnings color on Google TPU, Amazon Trainium 3, Meta MTIA volumes) | Ongoing through 2026-2027 | Bearish — incremental signal on in-housing trajectory |
| Lock-up expiry effects (insider selling) | Already past primary lock-up; secondary supply ongoing | Bearish — secondary supply pressure persists |

## Risks

**Thesis risks (investment case is wrong):**
1. **Counterparty consolidation risk.** Microsoft + OpenAI + Meta + Anthropic = >85% of contracted backlog. Any one of these cutting capex 25-30% (which has happened in every prior infrastructure cycle) impairs backlog directly and triggers DDTL covenant pressure. CoreWeave has no diversified customer base to fall back on.
2. **Hyperscaler in-housing risk.** MAIA, Trainium, TPU economics improving 30%/year × 2-3 more cycles = breakeven vs. outsourced GPU cloud by 2028. CoreWeave's 2028-2030 renewal cycle hits exactly as this breakeven is crossed.
3. **DDTL collateral compression risk.** $21.6B debt secured by GPUs depreciating at accelerated cycles. If second-cycle re-rent rates compress 30-50% from contracted rates, DSCR covenants pressure ratings and refinancing.
4. **NVIDIA strategic divergence risk.** NVIDIA's 13% equity stake aligns interests, but NVIDIA could equally pivot allocation toward AWS/Azure/GCP if hyperscaler ASICs threaten its chip business, leaving CoreWeave structurally short-allocated.
5. **Capex execution risk.** $31-35B FY26 capex against $12-13B revenue requires near-flawless construction, power interconnect, and supply chain execution. Microsoft already cited "delivery issues and missed deadlines"; repeated execution misses compound credit risk.

**Position risks (thesis right, stock wrong):**
6. **Secondary supply pressure.** IPO lockup expired; insiders, NVIDIA, and Magnetar / Blackstone all have unrealized gains; ongoing equity issuance to fund capex creates dilution overhang.
7. **Sentiment regime change.** Any broad "AI bubble" risk-off (DeepSeek-style efficiency-gain surprise, foundation lab capex revision down) hits CRWV harder than NVDA because of leverage and concentration.
8. **Index inclusion timing.** S&P 500 inclusion (likely 2026-2027 given size/seasoning) creates a forced-buying event but is well-telegraphed; if missed or delayed, the stock loses an expected catalyst.

## Conviction Triggers

→ HIGH if:
- Q3 2026 earnings discloses Microsoft contract renewal at flat-to-positive rate (not a cut), AND
- First Hopper cluster re-rent disclosed at >70% of original contracted rate, AND
- Anthropic or xAI signs an additional $5B+ contract (genuine counterparty diversification beyond MSFT/OpenAI/Meta)

→ LOW if:
- Microsoft cuts the Q3-Q4 2026 contract renewal by >15%, OR
- Q3 2026 gross margin compresses below 65% (signals marginal contract rate erosion), OR
- DDTL 4.0 or any prior facility receives a negative outlook revision from Moody's or DBRS, OR
- OpenAI commercial revenue disclosure (or absence) raises questions about $22.4B contract serviceability

→ CLOSE if:
- DDTL covenant breach disclosed in any quarterly filing, OR
- Microsoft contract reduction >30% on aggregate basis disclosed in 10-K or proxy, OR
- Equity dilution exceeds 15% in any 6-month window to fund capex (signals debt market closed and equity is funding-of-last-resort), OR
- Adjusted EBITDA margin compresses below 40% on a trailing 4-quarter basis (signals the operating leverage story has reversed)

## Mental Models
<!-- Outputs from applying the /Mental Models context files to this opportunity. Per the READING PROTOCOL in [[Generalist - Overview]], these are lenses and questions, never conclusions — every entry is a hypothesis to test against the evidence in this thesis, not a verdict. Populated incrementally: each research pass appends the models it applied and the specific triggers that fired. -->
- **Models applied** (2026-07-10 batch-4 pass, evidence-tested against July-2026 web research): [[Generalist - Overview]] (Perez frenzy, reflexivity) · [[Industry - Semiconductors]] (#3, #10) · [[Lens - Value Layer Monopoly]] (layer-renter test). **2026-08-06 /sync Rubin-economics repair:** [[Generalist - Overview]] ([G-7] ROIIC × runway, [G-13] price-implied operating variable) · [[Industry - Semiconductors]] (#4 generational cost curve, #8 architecture remaps bottlenecks) · [[Lens - Value Layer Monopoly]] (layer-renter / contract-wrapper test). **2026-08-20 MC backfill:** [[Lens - Management and Culture]] (gates + conversion; inert)
- **Triggers + evidence status**: hypotheses tested, not verdicts:
	- *The Summary's core premise is now CONTESTED by a new competitor class the trigger set never anticipated*: "hyperscaler capex cannot keep pace with demand" met **Meta Compute** (Jul 1: first hyperscaler selling excess capacity, GPU-hours "the same way neoclouds do") and **xAI/SpaceX renting all of Colossus 1 to Anthropic** ($1.25B/mo, 90-day termination either side). A secondary-supply class exists that didn't at thesis creation; CRWV -13.9% on the Meta news. Meta's dual role (marquee $35.2B customer AND named competitor) is a backlog-quality question, not just concentration. **The trigger set has no condition covering this; add one.**
	- *Contract-vs-spot bifurcation is the correct frame and currently protects the P&L*: 98% of Q1 revenue take-or-pay; SemiAnalysis reports H100s renewing at ~100% of original rates (HIGH-trigger re-rent leg trending MET at 100% vs the >70% bar), while B200 spot fell -31% in 3 weeks and the 90-day-out xAI-Anthropic template undermines the assumption that FUTURE deals carry 5–7yr take-or-pay terms. The DDTL amortization-cliff mechanic (Insight #2) now has named supply sources setting the 2027–28 re-contracting price.
	- *Generalist [G-7] · ROIIC × runway / [G-11] inverted / [G-13] · price-implied operating variable: Rubin cash rate, coverage, and vintage, not a 1.8×–3.0× corridor*: $9 fails the $192K gross-book screen and clears 15% IRR (18.4%). $12 contracted earns $282K vs $122K merchant. Coverage below ~44% at $12 fails the screen. Falsifier is a disclosed cash rate + coverage share, not the $6 multiple. (per [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]], rewrite 2026-08-13)
	- *Trigger scoreboard*: LOW/CLOSE: 0 fired (Moody's A3 stable, dilution ~8% <15%, adj EBITDA 56% >40%, GM 68% vs 65% line with 3pts runway). HIGH: 2 of 3 trending (Anthropic + Google + Jane Street = real diversification; re-rent at par); MSFT renewal leg resolves Q3–Q4 with Maia 200 deployed at scale as the bear counter-weight. Yet the stock is -40% YTD to ~$86/$47B: the market repriced the premise while the triggers stayed silent.
	- *Credit market leads equity (Insight #2 extended)*: A3 secured DDTL at 5.9% vs **9.75% unsecured notes**; the structural-subordination wedge priced the residual risk in April that equity only priced in July; converts now ~40% out-of-the-money; ~$120B of sector AI debt moved off-books via SPVs (systemic leverage larger than reported). Interest expense annualizing $2.1B+ on the thesis's modeled path; FCF -$4.7B in Q1.
	- *#10 anchor + execution*: Core Scientific deal TERMINATED (shareholder vote): single-builder dependence persists on the same counterparty whose delays drove the securities class action; >1GW active, $99.4B backlog (+284%), Vera Rubin first bring-up (a weeks-long lead, not quarters); CEO sold $37.7M the day before the Meta news.
	- *VLM layer-renter verdict unchanged and sharpening*: CRWV rents the layer below (NVIDIA allocation + silicon) and sells into a consolidating layer above (labs multi-sourcing with short-notice exits); the durable layers in this stack are NVIDIA's and the grid's. Perez frenzy-phase read: CRWV is the infrastructure over-builder whose capacity becomes the next cycle's cheap substrate; the thesis's Lucent analog is the right reference class.
	- Management & Culture [MC-1] · gates: Gate 1 pass (neocloud offtake/SKU/power feed); Gate 2 fail post-Q2 $104B backlog (pipeline is consensus compounder narrative). Lens inert; grade conversion on [G-7]/[G-8]/credit.
	- Management & Culture [MC-2] · incentive duration / founder control: Dual-class 10-vote, Intrator 38.70% / founders ~73.6% of votes (15 Apr 2026 DEF 14A); time-based RSUs + discretionary cash; 10b5-1 sales not buys. Founder duration is the MW-conversion fighting mechanism; leverage vs NBIS is [G-8], not MC.
	- Management & Culture [MC-6] · bureaucratic entropy: Core Scientific termination (30 Oct 2025) + Microsoft delivery misses (Q1 2026) vs Q2 ~+500 MW conversion; debt-driven pace as entropy vs fighting, unresolved.
	- Management & Culture [MC-7] · product vs matrix: 2,189 employees YE2025 (881 YE2024) still below the ~5,000 heuristic; COO Jain (Aug 2024) professionalising ops. No matrix-ceiling transition yet.
- **Disconfirming check** (evidence-updated): the thesis said to size the position around credit risk and counterparty cadence, and that discipline is validated: the July damage came through the demand-premise channel, not a credit event, and no LOW/CLOSE trigger fired. The steelman for the bull: $18B exit-ARR floor raised, four largest labs all customers, re-rents at par. The corrected Rubin model adds a harder adversarial test: a dedicated contract at ~$12 cash with near-full coverage would clear 15% IRR and the gross-book screen and confine the thesis to capital-structure risk; cash below ~$8.22, a coverage/vintage blend under the screen, or a later 35–40% re-rent would validate the operating bear. Other dated falsifiers: Q2 print (~Aug: GM vs 65% line, Meta Compute commentary); MSFT renewal disclosure Q3–Q4; any DDTL outlook change. Base rate: levered infrastructure builders at 2.2x interest coverage into a supply-normalizing market rarely re-rate up before a full credit cycle passes; the convexity here is in the debt pricing, not the equity multiple. Fresh callout (2026-05-16, Chanos arguments) remains unaddressed; flag. MC lens inert on Gate 2; the [MC-6]/[G-10] entropy and new-venture-destruction base rate is already the thesis's credit-cycle outside view; founder dual-class does not beat it until a Hopper re-rent or Microsoft renewal print.

## Related Research
- [[Macro & Technology/AI Datacenter Financing Mechanism Design]]: T3 GPU-DDTL template = CRWV's capital structure; 5.9% contract-backed vs 9.625% unsecured = live GPU-residual quote; total principal debt $25.15B (Mar) → ~$35.6B (Jun) via DDTL 5.0 + Aug-10 SOFR+550 facility [web, single-source]

**Research notes:**
- [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]]: June 2025 snapshot of CoreWeave business model, scale, and unit economics; refresh required for post-Q1 2026 data
- [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]]: Jensen's three-part flywheel explicitly frames CRWV as demand-side reinforcement
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]: GPU useful life extension 7-8 years, cluster-resign >35% gross margin, OpenAI's CRWV financing role
- [[Research/2025-12-05 - Macro - Gemini AI Bubble Risk Canvas]]: base rates for AI infrastructure bubble framings
- [[Research/2026-04-23 - Insight Surface Scan]]: vault-wide surface of AI infrastructure tensions
- [[Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison]]
- [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]: 2026-08-13 rewrite: cash $/hour + coverage + vintage; $9 = 18.4% IRR; 1.8×–3.0× corridor retired
- [[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]]: degentrading unit model; $11.6/hr is a retail outlier
- [[Research/2026-08-13 - Datacenter Capacity Cancellation Myth - deep-dive]]: 2026 US DC "cancellation wave" is announcement-layer noise
- [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]: nodal/LMP power-market framework: sharpens the location-level power-cost-pass-through disclosure ask (Outstanding Q#8, delivered power cost is nodal not a single number) and reinforces the willingness-to-pay-vs-bankability / contract-wrapper frame (Insight #6)


**Sector + macro context:**
- [[Sectors/Neoclouds & GPU-as-a-Service]]: parent sector MOC with full competitive landscape, miner-pivot bifurcation, pricing power trajectory
- [[Sectors/Compute & AI Compute Accelerators]]: upstream chip supply; Vera Rubin launch partner lineup
- [[Sectors/Data Center Power & Cooling]]: grid interconnect bottleneck; Vertiv unit economics
- [[Sectors/Custom Silicon & Networking Semiconductors]]: hyperscaler in-housing as dominant long-term demand risk
- [[AI Bubble Risk and Semiconductor Valuations]]: macro framing for credit cycle / capex normalization scenarios
- [[Macro & Technology/Sustainability of AI Capex]]: the AI-capex sustainability model that places CRWV in the fragile leveraged-merchant tranche; 25.8% interest/revenue past the historical builder break line; 2028-29 digestion vs. race-to-financing-ceiling timing and the dark-fiber-substrate second-order read

**Cross-thesis (strong factor exposure):**
- [[Theses/NVDA - Nvidia]]: sole GPU supplier, 13% equity owner, structural pricing-power upstream
- [[Theses/VRT - Vertiv Holdings]]: neoclouds 8-12% of FY26E revenue at 38-42% gross margin; same supply chain leverage
- [[Theses/META - Meta]]: $14B+ CRWV commitment plus $27B Nebius (counterparty concentration on the customer side)
- [[Theses/AVGO - Broadcom]]: custom silicon competition → long-term NVIDIA pricing compression → neocloud rental compression
- [[Theses/NET - Cloudflare]]: architectural alternative (edge AI vs. centralized GPU clusters)
- [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]]: miner-pivot category origin (IREN/APLD/CIFR pathway as comparable neocloud sub-segment)

**Cross-thesis (shared macro):**
- [[Theses/TSM - Taiwan Semiconductor]]: chip-fabrication supply chain underlying NVIDIA GPU shipments
- [[Theses/PSTG - Pure Storage]]: AI Compute Stack cluster adjacency (storage layer for GPU compute workloads)
- [[Research/2026-08-06 - Hyperscaler GPU Repricing Cycle Capex to L3 L4 - deep-dive]]
- [[Research/2026-07-22 - META Infrastructure Culture Reset - deep-dive]]
- [[Research/2026-07-23 - Vera Rubin NVL72 vs GB200 Inference TCO - deep-dive]]
- [[Research/2026-07-29 - LEGO Modular Datacenter Construction - deep-dive]]
- [[Research/2026-08-07 - GOOGL Gemini Decline GCP Financialization - deep-dive]]
- [[Research/2026-08-07 - SpaceX 10GW 2027 Microsoft Offtake - deep-dive]]
- [[Research/2026-08-08 - META Shanaka Clocks on One Building DC Finance - deep-dive]]
- [[Research/2026-08-10 - NVDA TileRT Ultra-High Interactivity InferenceX - deep-dive]]
- [[Research/2026-08-11 - NVDA Superposition AI Factory Underwriting - deep-dive]]
- [[Research/2026-08-11 - NVDA Superposition Open Weights Execution Share - deep-dive]]
- [[Research/2026-08-13 - NBIS NVDA - Nebius Q2 5GW Power Target - news]]
- [[Research/2026-08-13 - NVDA NBIS - CoreWeave Q2 104B Backlog - news]]

- [[Research/2026-08-14 - LITE CRWV NBIS NVDA - Temple 8 Earnings Week 500B MOU - deep-dive]]: Q2 print + credit-fragility / $500B MOU inversion; trigger-touch flags only
- [[Research/2026-08-14 - TSM NVDA - TSPA AI Servers Bottleneck Money - deep-dive]]: ODM working-capital / Taiwan bank concentration as a delivery choke below the factory SPV
- [[Research/2026-08-15 - NBIS CRWV - Neocloud Q2 CoreWeave Nebius Cerebras - news]]: Q2 $2.575B / adj EBITDA $1.51B (58.6%) / $9.4B capex / 1.5 GW·51 sites; A100 contract into 2029 at "attractive price" (2020-vintage residual)
- [[Research/2026-08-17 - SNDK MU SPCX - PhotonCap Aschenbrenner Baker 13F - deep-dive]]: named in the Baker book parse; no active-MW or residual-value print in this 13F
- [[Research/2026-08-15 - CRWV - Stress Test]]: late-cycle GPU-rental + leverage; Q2 backlog does not retire model
- [[Research/2026-08-26 - NBIS CRWV IREN vs Neocloud Complex - Competitive Comparison]]: twelve-name comparison; coordination proof (1.5 GW active, +25% list vs +17% input) against credit (covenant-lite over on the $2.6B facility); CRWV is the tenant at APLD 400 MW and CORZ 590 MW

## Log
### 2026-05-15
- Initial thesis created. Conviction: medium — best-in-class operating execution (56% adj EBITDA margin, $99.4B backlog, IG-rated GPU-collateralized debt) is genuinely impressive, but the structural setup (67% Microsoft concentration, $46B liabilities vs $3.3B equity, NVIDIA's 13% equity stake as vendor-financing flywheel, OpenAI's $22.4B contract serviceability, second-cycle DDTL re-rent risk) keeps this from being a high-conviction long. Sized as a credit-risk position, not a pure AI demand position; the trade is "long the cleanest neocloud equity while short its counterparty-concentration credit risk via NVDA pair or sector hedges." Primary sources: CoreWeave Q1 2026 earnings ($2.08B revenue +112% YoY, $99.4B backlog, $40B+ Q1 new commitments), DDTL 4.0 disclosure ($8.5B at A3/A-low IG ratings), NVIDIA $2B follow-on equity Jan 2026 (13% stake, $4.7B value), [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]], [[Sectors/Neoclouds & GPU-as-a-Service]].

### 2026-05-22 (manual)
- Status change: portfolio-wide realignment — not in current Live Portfolio holdings; status active→monitoring.

### 2026-06-03 (/sync)
- [[Research/2026-06-03 - Neoclouds NBIS vs CRWV - deep-dive]] + [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]]: New public peer [[Theses/NBIS - Nebius Group]] created (cleaner balance sheet; execution-vs-credit framing). 40% H100 1-yr contract-rate rebound (Oct'25 $1.70→Mar'26 $2.35) partially rebuts the rental-compression bear thread; rental-economics framework bounds neocloud pricing ($4.92 floor / $9.63-12.25 ceiling at Vera Rubin). Conviction unchanged (medium) — rebound is demand-cyclical not structural; DDTL re-rent risk intact.

### 2026-07-10
- Mental models pass: batch-4 evidence sweep populated ## Mental Models — core premise contested by a competitor class the triggers never anticipated (Meta Compute + xAI→Anthropic 90-day-out template); 0 LOW/CLOSE triggers fired yet stock -40% YTD — the market repriced the premise; contract book (98% take-or-pay, H100 re-rents at par) protects near-term P&L while credit market already priced the wedge (9.75% unsecured vs 5.9% secured); add a hyperscaler-excess-capacity trigger; 05-16 Chanos callout still unaddressed — conviction unchanged (medium); Q2 ~Aug, MSFT renewal Q3-Q4.

### 2026-07-12
- Numbers refresh: 1 metric updated, 0 material. Market Cap ~$59B→~$48B (-17.8%, non-material). Snapshot: [[_Archive/Snapshots/CRWV - CoreWeave (pre-numbers 20260712-174510)]]

### 2026-07-12 (/numbers)
- Numbers refresh (second same-day pass): 0 metrics changed — Market Cap rounds to already-current ~$48B. Snapshot: [[_Archive/Snapshots/CRWV - CoreWeave (pre-numbers 20260712-184111)]]

### 2026-07-29 (/sync)
- [[Macro & Technology/Sustainability of AI Capex]]: AI-capex model places CRWV in the fragile leveraged-merchant tranche; cross-sources the 25.8% interest/revenue as *past* the historical ~20-25% builder break line and dates the correction (2028-29 digestion or race-to-ceiling air-pocket) — conviction unchanged (medium): sharpens Bear Case driver #1 with an external outside-view frame, no new failure mode. Snapshot: [[_Archive/Snapshots/CRWV - CoreWeave (pre-sync 2026-07-29-155247)]]

### 2026-08-04
- Comparison [[Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison]]: CRWV wins on scale, valuation, and boom-duration torque, but its Q1 interest burden turns a demand miss into capital-stack impairment — conviction unchanged (medium; cheapness offsets no full credit-cycle proof).

### 2026-08-06
- [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]: ≥2.0× contracted Rubin pricing clears the fleet hurdle; CRWV's risk shifts to coverage, 2028–2029 re-rent and ~$22B pro-forma debt — conviction unchanged (medium; stronger initial economics offset by the same claim-stack risk).
- [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]: nodal/LMP framework sharpens the location-level power-cost-pass-through ask (Outstanding Q#8) — delivered power cost is nodal (basis/congestion), not one number — and reinforces the duration/counterparty risk (near-term willingness-to-pay ≠ bankable long-duration power). Conviction unchanged (medium).

### 2026-08-12
- [[Research/2026-08-06 - Hyperscaler GPU Repricing Cycle Capex to L3 L4 - deep-dive]]: GPU repricing cycle stresses leveraged neocloud unit economics — reinforces rate/power sensitivity; conviction unchanged.

### 2026-08-13
- [[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]: rewrite retires 1.8×–3.0× corridor; $9 clears 15% IRR and fails only the gross-book screen; coverage <~44% at $12 fails the screen — conviction unchanged (medium): operating bear is still coverage/vintage/re-rent, claim-stack untouched.
- [[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]]: $11.6/hr payback is a retail outlier; wholesale + Rubin-2× keep CRWV a layer-renter — conviction unchanged (medium).
- [[Research/2026-08-13 - Datacenter Capacity Cancellation Myth - deep-dive]]: 2026 US DC cancellation headlines are announcement-layer noise; does not lift the DDTL/re-rent bear — conviction unchanged (medium).
### 2026-08-14
- [[Research/2026-07-22 - META Infrastructure Culture Reset - deep-dive]]: Meta tokens/$ + SKU tribalism — demand color, not a DDTL print — conviction unchanged (medium).
- [[Research/2026-07-23 - Vera Rubin NVL72 vs GB200 Inference TCO - deep-dive]]: operator TCO is contract coverage, not $6 numeraire — re-rent still the 2028–29 ask — conviction unchanged (medium).
- [[Research/2026-07-29 - LEGO Modular Datacenter Construction - deep-dive]]: DSX Air twins — execution color, not residual-value — conviction unchanged (medium).
- [[Research/2026-08-07 - GOOGL Gemini Decline GCP Financialization - deep-dive]]: GCP as competing neocloud/TPU host — layer-renter frame intact — conviction unchanged (medium).
- [[Research/2026-08-07 - SpaceX 10GW 2027 Microsoft Offtake - deep-dive]]: 90-day CSA product vs CRWV multi-year take-or-pay — duration contrast, not a backlog print — conviction unchanged (medium).
- [[Research/2026-08-08 - META Shanaka Clocks on One Building DC Finance - deep-dive]]: 20–25y amort vs 4y occupancy — residual-value analog for GPU collateral — conviction unchanged (medium).
- [[Research/2026-08-10 - NVDA TileRT Ultra-High Interactivity InferenceX - deep-dive]]: interactivity TCO is software, not a re-rent rate — conviction unchanged (medium).
- [[Research/2026-08-11 - NVDA Superposition AI Factory Underwriting - deep-dive]]: DDTL residual/re-rent + vendor-finance analog; correlated PD×LGD — Outstanding Q#1 sharper — conviction unchanged (medium).
- [[Research/2026-08-11 - NVDA Superposition Open Weights Execution Share - deep-dive]]: remarketing/second-cycle clock is the open-weight implication — conviction unchanged (medium).
- [[Research/2026-08-13 - NBIS NVDA - Nebius Q2 5GW Power Target - news]]: peer 5 GW contracted / $3.0B ARR — orthogonal to CRWV credit binary — conviction unchanged (medium).
- [[Research/2026-08-13 - NVDA NBIS - CoreWeave Q2 104B Backlog - news]]: Q2 beat / $104B backlog / $35–39B capex vs $0.2–0.4B guide lift — execution/pass-through is the priced variable — conviction unchanged (medium).
### 2026-08-15
- [[Research/2026-08-14 - LITE CRWV NBIS NVDA - Temple 8 Earnings Week 500B MOU - deep-dive]]: Q2 $2.575B / $104B backlog / 59% adj EBITDA; net loss $626M and opex>revenue is the credit line, not the demand line — HIGH Anthropic/$5B+ evidence-touched not satisfied; LOW/CLOSE credit handles not crossed — conviction unchanged (medium).
- [[Research/2026-08-14 - TSM NVDA - TSPA AI Servers Bottleneck Money - deep-dive]]: ODM WC / bank-group concentration can slip neocloud energization even with contracted offtake — mechanism-adjacent to Superposition failure-mode #1, no DDTL trigger fire — conviction unchanged (medium).
- [[Research/2026-08-15 - NBIS CRWV - Neocloud Q2 CoreWeave Nebius Cerebras - news]]: DCD Q2 recap — $2.575B rev / $1.51B adj EBITDA / $626M net loss / $9.4B capex; A100-into-2029 residual print; no new credit-trigger fire vs the 08-14 Temple 8 note — conviction unchanged (medium).
- [[Macro & Technology/AI Datacenter Financing Mechanism Design]]: T3 template frames the DDTL amortization-cliff + 325bp contract-vs-marginal spread; total principal debt ~$35.6B (Jun-30) via DDTL 5.0 + Aug-10 SOFR+550 flagged for ingest — conviction unchanged (medium).

### 2026-08-18
- [[Research/2026-08-17 - SNDK MU SPCX - PhotonCap Aschenbrenner Baker 13F - deep-dive]]: Baker-book mention only — no CRWV MW / residual-value / backlog print — conviction unchanged (medium, monitoring).
- [[Research/2026-08-15 - CRWV - Stress Test]]: late-cycle GPU-rental + leverage; Q2 backlog does not retire the model — conviction unchanged (medium).

### 2026-08-20
- Lens backfill: ## Management and culture from [[Lens - Management and Culture]] — hypothesis inert (Gate 2 fail post-$104B backlog); founder-duration converts MW, leverage is [G-8] not MC. Conviction unchanged.
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged

### 2026-08-26 (/compare)
- Comparison [[Research/2026-08-26 - NBIS CRWV IREN vs Neocloud Complex - Competitive Comparison]]: best coordination proof in the complex (1.5 GW active, +~500 MW in Q2, list +25% vs Nvidia +17%, ~8 pts kept above the layer below) against the worst credit (the $2.6B facility repriced +100–125bp with a 1.35x DSCR maintenance covenant; Jefferies / Citi Buy→Hold; CDS round-trip 452→~855bp [T2]) — conviction unchanged (medium, monitoring): operating leg strengthened, credit leg weakened, net flat.
