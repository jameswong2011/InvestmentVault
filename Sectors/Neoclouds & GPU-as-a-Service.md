---
date: 2026-05-15
tags: [sector, moc, neoclouds, GPU-as-a-Service, AI-infrastructure]
status: active
sector: AI Infrastructure
---

# Neoclouds & GPU-as-a-Service

## Active Theses
- [[Theses/CRWV - CoreWeave]] — MEDIUM conviction, draft (init 2026-05-15). Cleanest equity proxy for "hyperscaler AI capex cannot keep pace with foundation-lab training demand through 2027." Best-in-class operating execution (Q1 2026 $2.08B revenue +112% YoY, 56% adj EBITDA margin, $99.4B backlog, first IG-rated GPU-collateralized debt) layered on structural credit risk (67% Microsoft concentration, $46B liabilities vs $3.3B equity, NVIDIA 13% vendor-financing-flywheel stake, OpenAI $22.4B contract serviceability, second-cycle DDTL re-rent compression). Sized as credit-risk position, not pure AI demand exposure.
- [[Theses/NBIS - Nebius Group]] — MEDIUM conviction, draft (init 2026-06-02). Cleaner-balance-sheet / execution-bet counterpart to CRWV's credit bet: ~$9.3B cash + ~$7-8B non-core stakes (ClickHouse ~$4.2B, Avride ~$2.2B) + customer-prepayment funding (Microsoft ~$7B upfront) vs CRWV's DDTL leverage. The binary is the >4x power build (~170MW→800MW-1GW by YE2026) converting a fully-contracted ~$50B Microsoft+Meta backlog; Q1 2026 $399M rev +684% YoY, $1.92B AI-cloud ARR, 45% core-AI-cloud margin. Sized as a quality-and-optionality position with a hard Q3-2026 execution catalyst.
- *Coverage candidates without theses yet (ranked by liquidity and disclosure quality): IREN (IREN Limited, ex-Iris Energy), APLD (Applied Digital), CIFR (Cipher Mining).*
- Adjacency theses informed by this sector: [[Theses/NVDA - Nvidia]] (sole GPU supplier, equity investor in CRWV/NBIS/Nscale), [[Theses/VRT - Vertiv Holdings]] (neoclouds = 8-12% of FY26E revenue at 38-42% gross margin), [[Theses/META - Meta]] ($27B Nebius + $14B+ CoreWeave commitments), [[Theses/NET - Cloudflare]] (centralized GPU cluster architecture is the implicit competition to edge AI), [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]] (miner-pivot pathway: IREN/APLD/CIFR origin story), [[Theses/6981 - Murata Manufacturing]] (component-layer beneficiary; neocloud GPU rack count is the primary demand driver behind GB200 NVL72 / Rubin / Rubin Ultra MLCC volume scaling).

## Key industry questions
- Are neoclouds structurally independent businesses or NVIDIA-allocated demand-side reinforcements whose pricing power, capital access, and customer relationships are all upstream-controlled?
- Does Microsoft's status as 67% of CRWV's FY25 revenue and $19.4B Nebius counterparty represent counterparty diversification or a single-point-of-failure for the entire publicly-traded neocloud complex?
- Will the "Bitcoin-miner-pivot" sub-category (IREN, APLD, CIFR) durably re-rate to AI-infrastructure multiples, or revert to commodity power-arbitrage multiples once GPU rental rates normalize?
- Is the DDTL-financed model (CRWV's $8.5B investment-grade GPU-collateralized debt) a bona-fide new asset class or vendor-financing-bubble in disguise — and what breaks when collateral rental rates compress faster than amortization schedules?
- How much of "AI infrastructure TAM" survives a hyperscaler in-housing scenario (Trainium2, TPUv6, MAIA at scale) where neocloud overflow demand compresses to specialty workloads?

## Industry history

The neocloud category did not exist before 2022. Three pre-existing infrastructure stacks converged into it: crypto-mining operators with surplus power and rack space, VFX/scientific-computing GPU renderers, and a small set of ML-researcher tooling startups.

| Year | Event | Significance |
|---|---|---|
| 2017 | CoreWeave founded as Atlantic Crypto by three commodities traders; Lambda Labs founded as a ML workstation vendor | Both companies start outside cloud infrastructure |
| 2019 | CoreWeave pivots from Ethereum mining to general GPU cloud (VFX, scientific compute) | First "neocloud" pivot; founders carry trader-style debt-financing instincts into infrastructure |
| 2020 | Yandex begins building AI training cluster (later spun out as Nebius) | Pre-AI-bubble buildout; Russian sanctions divestiture in 2024 separates Nebius as independent Western-listed entity |
| Nov 2022 | ChatGPT launch creates immediate GPU shortage | Hyperscalers cannot absorb demand fast enough; NVIDIA begins allocating direct to non-hyperscaler operators to fragment supply chain and prevent any single hyperscaler from cornering the model layer |
| 2023 | NVIDIA invests $100M in CoreWeave with "most favored nation" GPU access; CoreWeave revenue grows from $30M (2022) to $500M (2023) | NVIDIA's strategic bet on neoclouds as demand-side reinforcement validated; full thesis articulated in [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]] |
| 2024 | Bitcoin halving compresses miner profitability; CRWV hits $1.9B revenue (+737% YoY) | Miner pivot category emerges as Bitcoin economics force IREN/APLD/CIFR to monetize stranded power |
| Mar 2025 | CRWV IPO at $23B valuation, raises $1.5B; CRWV acquires Weights & Biases for $1.7B | First public-market test of neocloud business model; W&B acquisition signals vertical integration into MLOps |
| 2025 | Yandex divestiture completes; Nebius re-lists on Nasdaq | First non-CRWV publicly-traded pure-play neocloud |
| Jan 2026 | NVIDIA invests $2B in CoreWeave (stake now valued ~$4.4B, 28% of NVIDIA's public equity portfolio) | "Circular financing" critique becomes mainstream |
| Mar 2026 | NVIDIA invests $2B in Nebius; CRWV closes $8.5B DDTL 4.0 facility — first investment-grade rating (Moody's A3, DBRS A) on GPU-collateralized debt | NVIDIA equity flywheel scales from CRWV to a multi-operator portfolio; DDTL 4.0 IG rating institutionalizes neocloud debt as a recognized asset class |
| Apr-May 2026 | Meta announces $27B Nebius + ~$14B CoreWeave commitments; Microsoft commits $60B+ to neocloud capacity ($19.4B Nebius, $23B Nscale GB300, plus residual CRWV); CRWV Q1 reports $2.1B revenue with $99.4B backlog | Neoclouds become hyperscaler-counterparty capacity proxies rather than independent challengers |

The historical pricing-power trajectory: NVIDIA captured the GPU rents from chip sales; hyperscalers initially captured the GPU-hour rents at the cloud layer; neoclouds emerged when ChatGPT-era demand outstripped hyperscaler buildout pace and NVIDIA actively redistributed allocation to keep the cloud layer fragmented. Pricing power is upstream-pinned at NVIDIA — the entire neocloud complex is a derivative position.

## Competitive dynamics

The category bifurcates into two structurally distinct sub-segments with different durability profiles:

| Sub-segment | Members | Origin | Durable asset | Primary risk |
|---|---|---|---|---|
| **Pure-play AI cloud** | CRWV, NBIS, Lambda (private), Crusoe (private), Nscale (private) | Built post-2017 around GPU rental from inception | NVIDIA allocation priority + customer contracts | Hyperscaler in-housing; customer concentration; GPU rental-rate compression vs. DDTL amortization |
| **Bitcoin-miner pivot** | IREN, APLD, CIFR | Pivoted from crypto mining 2024-2026 | Land + grid interconnect + power contracts (NOT the GPU layer) | GPU rental rates revert to depreciation-only economics; stranded-asset risk for the second time |

**Pure-play AI cloud — competitive dynamics.** Five operators (CRWV public, NBIS public, Lambda private, Crusoe private, Nscale private) control the bulk of non-hyperscaler GPU capacity. None has differentiated technology — all run NVIDIA reference architectures with comparable InfiniBand networking, liquid cooling, and rack densities (CoreWeave's 130 kW/rack is the public-disclosure ceiling). Differentiation lives in: (a) speed-to-power (Vertiv estimates neoclouds pay 38-42% gross margin vs. 35% hyperscaler blended because urgency premium), (b) NVIDIA allocation priority (CoreWeave's MFN status, Nebius's $2B NVIDIA equity commitment), and (c) financing access (only operators with DDTL-grade collateral structures can scale).

The customer base is heavily concentrated. CoreWeave's FY25 mix: ~67% Microsoft, with OpenAI + Meta together representing ~55% of the $99.4B backlog. Nebius's stack: $27B Meta, up to $19.4B Microsoft. Three customers (Microsoft, Meta, OpenAI) underwrite the majority of publicly-disclosed neocloud revenue — this is not customer concentration in the conventional sense but rather counterparty consolidation of the entire sub-segment around a handful of hyperscaler/lab capex programs.

**Bitcoin-miner pivot — competitive dynamics.** Different problem, different solution. IREN (4.5 GW total power, 1.6 GW Oklahoma campus, 150,000 GPUs committed including 50,000+ B300s; $9.7B 5-year Microsoft GPU services contract), APLD (4 GW pipeline; $11B/15-year CoreWeave turnkey infrastructure contract for ~400 MW), CIFR ($5.5B/15-year AWS lease; multiple Fluidstack agreements totaling 224 MW). These operators sell two distinct products: (1) turnkey "AI superfactory" infrastructure (APLD-CRWV model — landlord economics, the operator never touches the GPU), and (2) end-to-end GPU cloud services (IREN-Microsoft model — same as pure-play neoclouds). The landlord variant has higher durability because the asset being sold (power, cooling, fiber, real estate) does not depreciate at GPU-cycle speed. The full-stack variant inherits the same GPU rental-rate risk as CRWV/NBIS.

**Pricing power.** Strengthening short-term (rental rates +/+, Nebius reports all capacity sold out with pricing "continues to strengthen"), structurally weak long-term. Three pressure vectors:
1. **NVIDIA upstream**: NVIDIA's $2B equity stake in CRWV and NBIS each is partly informational rent-extraction — the chip supplier knows operator economics and can price-discriminate on GPU shipments.
2. **Hyperscaler downstream**: Microsoft's $60B+ neocloud commitment is option value, not exclusivity — MSFT continues building Azure capacity in parallel and can shift allocation as in-house ASIC (MAIA) ramps.
3. **GPU rental rate compression**: H100/H200 rental rates have already fallen 50-70% in private spot markets per debt-market commentary on DDTL collateral; the cluster-resign mechanic that supports older Hopper economics (per [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]) is the offset, but it is bounded.

## Product level analysis

| Operator | Differentiation | Scale (Q1 2026) | Power | Key contracts | Margin/unit econ |
|---|---|---|---|---|---|
| **CRWV** | Highest rack density (130 kW), self-designed liquid cooling, Weights & Biases MLOps layer, NVL72/GB200/GB300 cluster builds, MFN GPU allocation | $2.1B Q1 revenue (+112% YoY), 250K+ GPUs, 32 data centers, 3.5 GW contracted power, $99.4B backlog | 360 MW active / 3.5 GW contracted | Microsoft (67% FY25); OpenAI/Meta ~55% of backlog; ~$11B APLD turnkey infrastructure deal | ~85% gross margin pre-D&A; -45% net margin (D&A + ~$1.2B annualized interest); $30B+ ARR target by end-2027 |
| **NBIS** | Full-stack from Yandex inheritance — built-in managed services, agentic-AI platform tooling, native MLOps; first to demonstrate GPU cloud at large scale outside CRWV | $399M Q1 revenue (+684% YoY), AI cloud ARR $1.9B (+50% QoQ), ~$50B backlog | 800 MW-1 GW connected EOY 2026; >4 GW contracted EOY 2026 | $27B Meta multi-year; up to $19.4B Microsoft; $2B NVIDIA equity | AI cloud adj. EBITDA margin 45% (up from 24% Q4 2025), turned adj. EBITDA profitable Q1 2026; FY26 capex guide raised to $20-25B |
| **IREN** | Renewable-powered (hydro Australia/Canada, gas Texas), B300-heavy roadmap, full-stack GPU cloud (not just colocation) | 150,000 GPUs committed, $3.4-3.7B AI cloud ARR target by EOY 2026 | 4.5 GW total power including 1.6 GW Oklahoma | $9.7B 5-year Microsoft GPU services | Margin disclosure thin pre-conversion; renewable power contracts at low fixed cost vs grid spot |
| **APLD** | Turnkey infrastructure landlord model — designs, builds, operates AI buildings for hyperscaler/neocloud tenants but does not own GPU layer; 12-14 month groundbreaking-to-RFS construction | 4 GW pipeline (larger than IREN) | 4 GW pipeline | ~$11B/15-year CoreWeave (~400 MW) | Landlord economics — recurring lease revenue, no GPU residual risk |
| **CIFR** | Full pivot from Bitcoin mining; landlord model serving hyperscalers + neoclouds | 224 MW signed (Fluidstack 168 MW + 56 MW); larger AWS pipeline | Multi-site Texas + new builds | $5.5B/15-year AWS lease; Fluidstack agreements | Landlord economics; 10-15 year contract durations stabilize cash flow but limit upside if GPU rates spike |

Reference architecture across the sub-segment is convergent: NVIDIA H100/H200/B100/B200/B300 GPUs, NVL72 rack-scale builds, InfiniBand or RoCEv2 networking, direct-liquid-cooled chassis at 100+ kW/rack, multi-megawatt cluster topology. No operator has demonstrated proprietary IP that materially differentiates compute performance. Differentiation reduces to commercial relationships (NVIDIA + customer contracts) and capital structure.

## Acquisitions and new entrants

**Material M&A (since 2024).** Two transactions have reshaped the operator-side stack:
- **CRWV acquires Weights & Biases ($1.7B, March 2025)** — vertically integrates the MLOps layer (experiment tracking, model registry, evaluation tooling) into the GPU compute stack. Strategic logic: capture more of the model-development workflow vs. allowing AWS SageMaker / Azure ML / GCP Vertex to capture the layer above the metal. Outcome unproven — most foundation labs (OpenAI, Anthropic, Meta) use proprietary internal MLOps stacks regardless of where they rent compute.
- **Yandex divestiture / Nebius listing (2024-2025)** — not a conventional acquisition, but functionally created a new publicly-traded operator out of a pre-existing Russian AI cluster. Sanctions-driven discount on entry price proved a meaningful tailwind to the relisted entity's compounding.

**New entrants and rate of formation.** Capital intensity creates a moat against pure new entry. The binding constraint is not capital ($5-10B project-finance facilities are available to operators with creditworthy customer contracts) but: (a) NVIDIA allocation priority — without an MFN-style relationship, new operators cannot acquire enough GPUs to bid for hyperscaler-scale contracts; and (b) grid interconnect timelines — power capacity reservations now run 24-48 months in tier-1 US/EU markets, making the Bitcoin-miner-pivot category structurally advantaged on the supply side because their grid connections predate the AI demand spike.

**NVIDIA equity strategy as a category-shaping force.** NVIDIA's $40B+ AI equity portfolio in 2026 (~$30B OpenAI, $2B CRWV, $2B NBIS, $2B Nscale, plus Lambda) is the dominant new-entrant filter. Operators NVIDIA backs are credentialed for hyperscaler-scale contracts; operators it does not back struggle to scale beyond regional niches. This makes NVIDIA's allocation decisions, not customer wins, the binding category-formation event. Detailed framing in [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]].

**Disruption potential from new entrants is constrained but real on the edges.** Sovereign-AI clouds (Nscale Norway/UK, GCC-funded clouds, potential Indian SOEs) may capture market share in regions where data residency or political sensitivity prevents hyperscaler use. Edge-inference platforms ([[Theses/NET - Cloudflare]] Workers AI, AWS Wavelength) compete for a different workload class (low-latency inference) but do not threaten training and large-batch inference, which is the neocloud bread-and-butter.

## Macro shifts

| Variable | Direction | Timing | Mechanism | Linked context |
|---|---|---|---|---|
| GPU useful life extension (5yr → 7-8yr) | Bullish for neocloud unit economics | Already in progress | Hopper/H100 clusters re-signing at >35% gross margin after initial 4-year contracts; old GPUs do not become obsolete because inference demand absorbs them | [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] |
| Grid interconnect bottleneck | Tailwind for incumbent operators with grid contracts; barrier to new entrants | 2026-2030 binding | 24-48 month interconnect queues in PJM, ERCOT, EU; behind-the-meter generation (gas turbines, fuel cells) becoming required to scale | [[Sectors/Data Center Power & Cooling]] |
| Hyperscaler in-housing of ASICs | Bearish for neocloud demand beyond 2027 | 2027-2030 inflection | Microsoft MAIA, AWS Trainium2/3, Google TPU v6/v7 scaling — if hyperscalers internalize 30%+ of training workloads, neocloud overflow demand compresses to inference + specialty | [[Theses/NVDA - Nvidia]] Bear Case; [[Sectors/Custom Silicon & Networking Semiconductors]] |
| NVIDIA roadmap acceleration (B300 → Vera Rubin → Feynman) | Mixed — operators must keep upgrading or face stranded older fleet, but newest fleet commands rental premium | 18-month product cycle | Each new generation depreciates the previous one's economics faster; CRWV/NBIS/IREN/Nscale all participating in Vera Rubin launch H2 2026 | [[Sectors/Compute & AI Compute Accelerators]] |
| Sovereign-AI / regulatory localization | TAM-positive for non-hyperscaler operators | 2026-2028 | EU AI Act + GDPR data residency, GCC/India/Korea sovereign-cloud programs route demand to regional neocloud operators (Nscale, Nebius, IREN, regional partners) | [[Theses/SKM - SK Telecom]] |
| Interest rates | Negative tail risk | 2026-2027 sensitivity | DDTL coupons at SOFR+225-400bps; CRWV's ~$1.2B annualized interest at average 11% borrowing cost. 200bps SOFR increase ≈ $400M+ incremental annual interest on CRWV alone | [[Macro & Technology/AI Bubble Risk and Semiconductor Valuations]] |
| AI demand normalization (post-bubble scenario) | Existential | Unknown timing | If foundation-lab training capex compresses (model architecture efficiency wins, e.g., DeepSeek-style efficiency gains compound) — neoclouds become first-to-default vehicle because they have no other revenue line | [[Research/2025-12-05 - Macro - Gemini AI Bubble Risk Canvas]] |

## Investor heuristics

**What's priced in (consensus view).** Neoclouds are levered AI infrastructure plays with multi-year contracted revenue visibility, validated by hyperscaler counterparties (Microsoft, Meta, AWS) and NVIDIA equity backing. CRWV at $30B+ ARR by end-2027 and NBIS at $7-9B ARR target by end-2026 imply 50-100x revenue CAGRs that the market assigns 80-90% probability. The DDTL 4.0 investment-grade rating is accepted as evidence that GPU-collateralized debt is a legitimate asset class. The miner-pivot operators (IREN, APLD, CIFR) trade at AI-infrastructure multiples, not commodity-mining multiples — the market has priced in successful conversion.

**Where consensus could be wrong — five non-consensus angles:**

1. **Counterparty concentration is underpriced.** Microsoft + Meta + OpenAI underwrite the majority of publicly-disclosed neocloud backlog. This is structurally analogous to Lucent/Nortel's 1999-2001 telco-capex dependence — the operators are not selling to many small customers but acting as capex-cycle proxies for three hyperscaler capex programs. If any one of Microsoft / Meta / OpenAI cuts capex 25-30% (which has happened in every prior infrastructure cycle), the affected neocloud's backlog impairs immediately. Disclosure that 67% of CRWV revenue is Microsoft frames this as a CRWV risk; the under-discussed framing is that all five public neoclouds collectively concentrate to the same 3-4 counterparties.

2. **NVIDIA's $40B equity flywheel is vendor financing, not validation.** The pattern — NVIDIA invests, the neocloud uses proceeds to buy NVIDIA GPUs, NVIDIA reports revenue, the neocloud reports backlog, NVIDIA stake appreciates with neocloud market cap — is structurally identical to 1999-2001 telco vendor financing (Lucent's customer loans to CLECs). The historical analog ended in 70-90% drawdowns at the financier. NVIDIA's 28% portfolio concentration in CRWV alone is the early-warning marker.

3. **The DDTL collateral mechanic is broken.** GPU rental rates in private spot markets have fallen 50-70% from peaks while DDTL 3.0 / 4.0 covenants reference acquisition cost or contracted rates. The 1.15-1.20x DSCR covenants assume contracted-rate revenue, which holds while the 5-7 year contracts are in their initial period — but the second-cycle re-rent (after 4-year initial contracts roll) economics determine the back-end of the DDTL amortization. If GPU oversupply emerges by 2027-2028, DDTLs face covenant breach risk before maturity. The "first investment-grade GPU-backed debt" framing is bull-cycle pattern recognition, not durable credit analysis.

4. **Miner-pivot durability bifurcates by business model.** APLD and CIFR's landlord model (sell power + space, do not own GPUs) is genuinely more durable than CRWV/NBIS because the asset being sold does not depreciate at GPU-cycle speed. IREN's full-stack model (own and rent GPUs end-to-end via $9.7B Microsoft contract) carries the same depreciation/rental-rate risk as the pure-plays. The market currently rates them as a homogenous "Bitcoin-miner-pivot" category — disaggregation creates pair-trade opportunity.

5. **Neoclouds are levered NVIDIA derivatives, not independent businesses.** The conventional valuation reflex (compare to AWS/Azure/GCP on EV/Revenue or to legacy data center REITs on cap rate) misses that pricing power is upstream-pinned at NVIDIA. If NVIDIA's chip margins compress (custom silicon competition from Broadcom-led hyperscaler ASICs — see [[Sectors/Custom Silicon & Networking Semiconductors]] and [[Theses/AVGO - Broadcom]]), the neocloud rental rates that justify current valuations compress on the same timeline. The cleanest expression of bullish-AI-infrastructure is NVIDIA itself; neoclouds are levered beta on the same factor with idiosyncratic credit risk overlaid.

**Trade construction implications.** Long-bias trades in this sector — if any — should favor the landlord-model miner-pivots (APLD, CIFR) over full-stack neoclouds (CRWV, NBIS, IREN) on durability grounds. Short-bias trades should target the full-stack operators with the highest customer concentration and most aggressive DDTL leverage (CRWV is the cleanest expression). Pair: short CRWV / long NVDA captures the NVIDIA-derivative spread and isolates idiosyncratic credit risk.

## Related Research
- [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]] — primary CRWV business model + scale data (note: contains off-topic Grok output; treat as June 2025 snapshot, refresh with post-Q1 2026 data)
- [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]] — Jensen's three-part flywheel explicitly frames CRWV/NBIS/Nscale as demand-side reinforcements
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] — GPU useful life extension to 7-8 years; cluster-resign gross margin >35%; OpenAI's CoreWeave financing role
- [[Research/2026-03-31 - Cloudflare Path to Competing with Hyperscalers]] — neocloud vs. edge-AI architectural competition framing
- [[Research/2025-12-05 - Macro - Gemini AI Bubble Risk Canvas]] — base-rate framing for AI infrastructure bubble risk
- [[Sectors/Compute & AI Compute Accelerators]] — upstream chip-supply context, Vera Rubin launch partner lineup
- [[Sectors/Data Center Power & Cooling]] — grid interconnect bottleneck, Vertiv neocloud margin disclosure (38-42% gross on 8-12% of revenue)
- [[Sectors/Custom Silicon & Networking Semiconductors]] — hyperscaler in-housing as the dominant long-term demand risk

## Legacy Callouts
<!-- Auto-managed by /archive-callouts. Addressed callouts older than the sweep threshold (default 180 days) are moved here from their original sections as plain bulleted entries: `- **<addressed-date>** · <type> · <section> · raised <fresh-date> → <body>` with a `**Response:**` sub-bullet. Sorted descending (newest first). Do NOT hand-edit. To exempt a callout from sweeping, add `[[pinned]]` to its header in-place. -->

## Log
### 2026-05-15
- Initial sector note created. Coverage scope: public neoclouds (CRWV, NBIS) + Bitcoin-miner pivots (IREN, APLD, CIFR). Industry framing inherits established vault POV: neoclouds are NVIDIA demand-side reinforcements with upstream-pinned pricing power; counterparty concentration to 3-4 hyperscaler capex programs is the dominant under-priced risk; landlord-model miner-pivots (APLD, CIFR) bifurcate on durability vs. full-stack operators (CRWV, NBIS, IREN). Sources: CoreWeave Q1 2026 ($2.1B revenue, $99.4B backlog), Nebius Q1 2026 ($399M revenue +684% YoY, $50B backlog), IREN $9.7B Microsoft contract, APLD $11B CRWV turnkey, CIFR $5.5B AWS lease; CRWV DDTL 4.0 ($8.5B, first IG GPU-collateralized debt rating); NVIDIA $40B+ AI equity portfolio Q1 2026.
- /sync all (sync-2026-05-15-145500): promoted [[Theses/CRWV - CoreWeave]] from coverage-candidate placeholder to Active Theses entry (MEDIUM conviction, draft; init 2026-05-15 — counterparty-concentration + DDTL credit thesis sized as credit-risk position not pure AI demand exposure). Added [[Theses/6981 - Murata Manufacturing]] to adjacency theses (component-layer beneficiary of neocloud GPU rack volume scaling — GB200 NVL72 = 440k MLCCs per rack, Murata ~50% share at 008004 case size). — conviction impact: unchanged (sector framing intact; CRWV promotion confirms primary coverage axis is now staffed; adjacency expansion sharpens the demand-side / component-side feedback loop documented in §Competitive dynamics and §Macro shifts).

### 2026-06-03 (/sync)
- [[Research/2026-06-03 - Neoclouds NBIS vs CRWV - deep-dive]] + [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]]: Second public pure-play [[Theses/NBIS - Nebius Group]] thesis created (draft, MEDIUM) + added to §Active Theses — both NBIS and CRWV now staffed; NBIS = balance-sheet-quality/execution bet vs CRWV credit bet. Rental-economics "One Chart" framework quantifies pricing-power-pinned-at-Nvidia (cost floor ~$4.92/hr vs value ceiling ~$9.63-12.25/hr at Vera Rubin; Nvidia price hikes shift the curve up-left, compressing neocloud IRR). 40% H100 1-yr contract rebound (Oct'25→Mar'26) nuances the rental-compression thread. Sector framing unchanged.
