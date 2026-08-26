---
publish: true
date: 2026-07-28
tags: [macro, technology, artificial-intelligence, datacenters, capex, semiconductors]
status: active
source: "Independent synthesis of company filings, official statistics, primary research, and vault evidence"
---

# Sustainability of AI Capex

## Executive judgment

**The 2026 AI build is running at roughly $850–900B of ecosystem capex against only $150–180B of annualized end-buyer revenue: a 5–6x coverage gap. Aggregate spot pre-tax ROIC on the estimated $1.0–1.2T of AI-incremental capital invested through 2026 is only 5–7%, below an 8–10% cost of capital, before the full depreciation wave reaches earnings.** None of that makes AI demand false. Workload growth, revenue capture, and asset-owner returns are different variables.

**The 5–7% headline is a spot estimate of near-term returns built on a backward-looking method: today's attributable operating profit divided by capital invested to date, not a forecast of what the build will ultimately earn.** It mechanically penalizes cohorts still ramping toward monetization. True long-run ROIC is impossible to estimate today and will not cluster near its mean: the distribution is power-law: exceptionally high for the few AI winners that convert compute into durable revenue capture, exceptionally negative for losers holding stranded or refinanced capacity, with the capital-weighted average meaningfully above the cost of capital. That asymmetry is what participants are underwriting: a seat at the table is an option on AI-winner economics, and every company holding one is racing to capture them rather than pricing capex off the spot return. The spot measure's role in this note is a clock, not a verdict: it dates how much monetization must arrive before the depreciation wave lands, and it prices the cost of owning the wrong cohort.

The build is four cycles sharing one label:

| Tranche | Approx. 2026 share | Funding durability | Return character |
|---|---:|---|---|
| Core-franchise defense and internal use | 30–35% | Operating cash flow; cut last | Strategically mandatory, financially hard to attribute |
| Merchant enterprise cloud | ~25% | Mostly operating cash flow | Proven demand pool, but adoption-depth and price/volume risk remain |
| Frontier-lab-serving capacity | 25–30% | Debt, SPVs, prepays, vendor finance | High counterparty, utilization, and residual-value risk |
| Lab/sovereign self-build | 10–15% | Equity or state capital | Highest elasticity to funding conditions; financial hurdle may be secondary |

Roughly **55–60% of spend sits in cash-funded franchise defense and enterprise cloud**, while state or equity capital funds part of the remainder. The most cyclically fragile 30–35% is lab-committed and leveraged merchant capacity: tranche C plus the equity-funded share of D; state-funded self-build answers to politics, not financing. SemiAnalysis (Aug 2026) adds an *inside-tranche* allocator: selling frontier tokens at API prices reaches as high as $100M per MW per year vs sub $30M per MW for open TaaS / colo / RecSys / legacy cloud, so Anthropic+OpenAI (27% of 2026 net new GW today, including Bedrock/Foundry/Gemini Enterprise Agent) should outbid overflow and open serving for incremental megawatts [1×: SemiAnalysis]. That reallocates mix inside tranche C; it does not close the $850–900B vs $150–180B coverage gap. This funding mix makes a telecom-style systemic collapse unlikely. The base case is therefore **digestion, not crash**: capex reaches roughly **$1.0–1.1T in 2027**, slows to **$1.1–1.25T in 2028**, then runs flat to down in 2029 as depreciation and financing discipline expose weak cohorts. The correction is concentrated in contestable capacity rather than the qualification-gated silicon, networking, memory, and power bottlenecks.

Demand has two opposite shapes. Corporate automation is deep but rate-limited by organizational redesign: documented processes, governed context, decision rights, liability, and change capacity mature on a decade clock that suppliers cannot accelerate with more compute. Consumer and prosumer adoption is fast but shallow: free substitutes, an $8–20 mass-market price band, 5–6% current paid conversion, high churn, and power-law output monetization cap revenue. The conservative 2031 ranges are **$250–400B of corporate AI software/agents/API revenue**, **$20–40B of government applications**, and **$85–135B of consumer/prosumer revenue**.

Those direct pools sum to **$355–575B by 2031**. A broader de-circularized monetization path can reach roughly **$850B by 2030** only by also counting end-customer cloud/model consumption, advertising and commerce uplift, and internal cost savings once, never lab revenue, cloud revenue, and chip revenue for the same dollar. Even that broader path does not support an uninterrupted consensus glide to $1.4T of capex in 2028 without unusually high usage elasticity and financing appetite.

The return dispersion matters more than the average. Chokepoint suppliers can retain monopoly-like returns while integrated hyperscalers earn acceptable blended returns through cloud, advertising, applications, and internal savings. Leveraged merchant capacity and frontier-lab commitments can destroy equity value even if every accelerator remains useful. The industry can be **functionally underbuilt and financially overbuilt at the same time**.

### Forecast snapshot

| Question | Conservative view |
|---|---:|
| 2026 ecosystem capex | **$850–900B** |
| 2026 annualized priced end demand | **$150–180B** |
| Current capex / end-demand coverage gap | **5–6x** |
| AI-incremental capital invested through 2026 | **$1.0–1.2T** |
| Current aggregate pre-tax ROIC | **5–7% vs. 8–10% WACC** |
| 2031 corporate AI software/agents/API | **$250–400B** |
| 2031 government applications | **$20–40B** |
| 2031 consumer/prosumer | **$85–135B** |
| 2027–2031 base cumulative capex | **$5.5–6.5T** |
| Base capex shape | **2028–29 digestion; re-acceleration from 2030** |
| Binding base-case gate | **Organizational readiness, then financing discipline** |

## Scope and method

### What is being measured

| Term | Definition used here | Exclusions |
|---|---|---|
| **Ecosystem capex** | Reported or estimated physical capital expenditure by hyperscalers, Oracle, neoclouds, labs, Chinese platforms, and sovereign asset owners | Frontier-lab commitments already financed on another asset owner’s balance sheet; adding commitments to the owner’s capex would double-count |
| **AI hardware capex** | Accelerators, host CPUs, memory, networking/optics, storage, racks, and power electronics bought for AI clusters | Land, buildings, grid interconnects, long-lived power generation, and non-datacenter Amazon logistics/satellite assets |
| **Priced end demand** | Dollars paid by consumers, enterprises, and governments for AI functionality, counted once at the ultimate end buyer | A lab’s API revenue counted again as hyperscaler cloud revenue and again as hardware revenue |
| **Direct application/agent revenue** | Copilots, agents, creative/building tools, vertical AI, governance, and application-level usage/outcome fees | Infrastructure revenue and indirect advertising, commerce, or internal-cost value |
| **Datacenter ROIC** | After-tax operating profit attributable to a datacenter cohort divided by the full capital invested in that cohort | Reported by none of the five companies; the note therefore uses bounded proxies |
| **Projection window** | 2026 current-year anchor plus calendar 2027E through 2031E | Longer-run deployment upside after organizational redesign |

Company filings, official adoption surveys, current vendor pricing, productivity experiments, and a de-circularized demand ledger provide the anchors. Third-party capex forecasts are used as outside-view checks, not as the answer.

### Why exact datacenter ROIC is unknowable from public accounts

Each company mixes several economic engines inside the same facilities:

1. **External rental:** Azure, AWS, Google Cloud, and OCI sell compute, storage, database, and model access.
2. **First-party applications:** Microsoft 365 Copilot, GitHub Copilot, Gemini, advertising systems, recommendation models, and internal agents consume the same hardware.
3. **Indirect revenue uplift:** better ad targeting, search retention, conversion, content ranking, and marketplace efficiency raise revenue without an “AI revenue” line.
4. **Cost avoidance:** coding, customer service, moderation, security, and infrastructure optimization can generate a return without external revenue.
5. **Strategic capacity:** sovereign, research, and competitive-option capacity may be rational even below a normal financial hurdle.

Reported PP&E is also the wrong denominator. Net PP&E subtracts accounting depreciation; true invested capital should include construction in progress, finance leases, datacenter operating leases, networking, working capital, and retired or impaired assets. Segment operating income is the wrong numerator because cloud segments bundle software and support, while advertising segments contain decades of accumulated data and distribution.

The analysis therefore uses three layers:

- **direct-monetization signal:** segment operating income / total company net PP&E;
- **whole-company return ceiling:** total operating income / total company net PP&E;
- **cohort profit-conversion ceiling:** change in after-tax company operating income / cumulative capex over the same period.
- **aggregate spot-return estimate:** attributable current AI operating profit / estimated AI-incremental capital invested.

None is labelled datacenter ROIC. Agreement across all four raises confidence; divergence reveals where attribution is doing the work.

## I. What the last six years of capex produced

### The capital step-up

Reported capex rose at a **32% compound rate from 2020 to 2025**, then approximately doubled again in the 2026 plans. The forward column mixes cash capex, lease-inclusive guidance, and fiscal years, so it defines the capital envelope rather than a clean accounting subtotal.

| $B | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Current 2026 plan / run-rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Microsoft | 15.4 | 20.6 | 23.9 | 28.1 | 44.5 | 64.6 | **190** |
| Alphabet | 22.3 | 24.6 | 31.5 | 32.3 | 52.5 | 91.4 | **~200** |
| Amazon | 40.1 | 61.1 | 63.6 | 52.7 | 83.0 | 131.8 | **~200** |
| Meta | 15.1 | 18.6 | 31.4 | 27.3 | 37.3 | 69.7 | **125–145** |
| Oracle | 1.6 | 2.1 | 4.5 | 8.7 | 6.9 | 21.2 | **~70 net / $90–95 gross FY27 plan** |
| **Core five envelope** | **94.5** | **127.0** | **155.0** | **149.1** | **224.1** | **378.7** | **~$785–830** |

**Comparability limits:** Microsoft and Oracle use June/May fiscal years; the other rows are calendar-year reporters. Amazon’s reported asset purchases include fulfillment and other non-datacenter assets. Meta’s guide includes leases. Oracle’s plan distinguishes roughly $70B of net capex from $90–95B gross before $20–25B of customer prepays. It is an asset-owner envelope, not pure AI spend.

Alphabet’s H1 2026 capex reached **$80.6B** and its current plan moved toward **$200B**, above the $175–185B disclosed in the [FY2025 release](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx). [Microsoft’s FY2026 Q3 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3) implied approximately **$190B** of calendar-2026 capex, including $25B of component inflation; two-thirds of Q3 capex was short-lived GPUs and CPUs. [Amazon’s FY2025 release](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/) guided to roughly **$200B** across Amazon. [Meta’s Q1 2026 release](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/) raised its range to **$125–145B**. [Oracle’s FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm) reported **$55.7B** of capex against $32.0B of operating cash flow before the larger FY2027 plan.

Adding CoreWeave’s **$31–35B** guide, Nebius, xAI, Chinese platforms, and sovereign builds, while excluding contracts already financed on a hyperscaler balance sheet, produces the conservative **$850–900B 2026 ecosystem anchor**. The lower figure versus a simple sum of announced commitments reflects netting, timing, lease treatment, and double-count removal.

### Cash-flow coverage has already separated

| Company | Latest capex | Operating cash flow | Capex / OCF | Interpretation |
|---|---:|---:|---:|---|
| Microsoft FY25 | $64.6B | $136.2B | **47%** | Legacy software and cloud fund the build with room to spare |
| Alphabet FY25 | $91.4B | $164.7B | **56%** | Search advertising remains the financing engine |
| Amazon FY25 | $131.8B | $139.5B | **95%** | Build consumed almost all operating cash flow before leases and other uses |
| Meta FY25 | $69.7B | $115.8B | **60%** | Advertising funds AI despite Reality Labs losses |
| Oracle FY26 | $55.7B | $32.0B | **174%** | External financing and contracted customer economics are load-bearing |

The funding hierarchy matters. Microsoft, Alphabet, and Meta can tolerate a weak AI cohort because high-margin incumbency cash flows absorb it. Amazon can fund the build but has little free-cash-flow cushion at the current cadence. Oracle raised debt and equity while scaling OCI; its return depends more directly on contract duration, customer credit, financing cost, and residual hardware value.

### The funding crossover changes the base rate

The marginal dollar is moving from internally funded strategic investment toward credit, prepays, SPVs, and supplier finance:

- Alphabet’s Q2 2026 capex was **$44.9B against $39.1B of operating cash flow**, an early quarterly crossover;
- Oracle’s FY2026 free cash flow was approximately **negative $24B**;
- Meta paused buybacks in Q1 2026 (no repurchases; authorization retained) while free cash flow fell to $12.4B;
- hyperscaler capex is projected to exceed operating cash flow from Q3 2026.

The outside-view warning is that railway, electrification, telecom, and shale booms became less tolerant of demand disappointment within roughly two years of the marginal dollar shifting from cash generation to credit, not that every >30%-growth capital cycle must collapse. Integrated hyperscalers are better businesses than the median historical builder, but that exception applies mainly to cash-funded franchise capacity, not to every contract they sponsor.

The frontier-lab commitment stack intensifies the risk. OpenAI’s announced commitments total roughly **$1.4T** across Broadcom, Oracle, Microsoft, Nvidia, AMD, AWS, and CoreWeave, against approximately **$25–30B of annualized revenue** and a projected 2027 cash burn near **$63B**. Some figures are non-binding, multi-year, or overlapping, so $1.4T is not near-term capex. The economic issue is the circular chain: suppliers or infrastructure owners finance the customer whose commitment then supports their own revenue. Backlog protects volume only if the counterparty remains financeable.

### Direct monetization signals

| Company | 2025/FY26 monetization evidence | Operating-profit / PP&E signal | What the ratio says | What it does not say |
|---|---|---:|---|---|
| Microsoft | Intelligent Cloud revenue **$106.3B**, operating income **$44.6B**; Azure exceeded $75B | **21.8%** pre-tax on $205.0B total net PP&E | The installed cloud estate already produces strong direct profit | Intelligent Cloud includes software; total PP&E includes non-cloud assets; current capex is not fully productive |
| Alphabet | Google Cloud revenue **$58.7B**, operating income **$13.9B** | **5.6%** on $246.6B total net PP&E | Direct cloud profit has crossed scale but does not yet cover the full asset base at a high return | Search/YouTube AI uplift is outside Cloud; the denominator includes first-party infrastructure |
| Amazon | AWS revenue **$128.7B**, operating income **$45.6B** | **12.8%** on $357.0B total net PP&E | AWS is a proven profit pool | Fulfillment and logistics make the denominator much too large for AWS; capex includes non-AWS assets |
| Meta | Family of Apps revenue **$198.8B**, operating income **$102.5B** | **58.1%** on $176.4B total net PP&E | The ad platform has abundant profit capacity to fund compute | Almost none of the numerator can be causally assigned to marginal AI capex |
| Oracle | Total operating income **$20.6B**; OCI revenue **$18.1B** | **20.6% company OI / $100.0B PP&E** | Legacy software provides some earnings coverage | OCI profit is undisclosed; the 20.6% is an upper bound, not a cloud return |

The ratios support three conclusions:

1. **The legacy cloud cohort was good capital allocation.** AWS and Azure have direct profit at a scale that would be impossible without datacenters.
2. **Integrated platforms hide the best and worst returns.** Meta and Alphabet can earn exceptional returns from recommendation and advertising models while underpricing internal compute; external cloud segment margins miss that value.
3. **A profitable installed base does not validate the marginal cohort.** The 2026 spend is much larger, more accelerator-heavy, and enters a market with more suppliers, custom silicon, and price competition.

### Aggregate spot ROIC is below WACC; the layer distribution is the result

Capex above a pre-AI 2022 baseline growing at 12% annually implies roughly **$630B of AI-incremental Big Four capital in 2024–2026**. Adding Oracle’s above-trend spend, neoclouds, labs, and sovereign self-builds produces **$1.0–1.2T of cumulative AI-incremental capital by end-2026**. Current attributable operating profit is approximately **$50–70B**: frontier labs are near breakeven in aggregate, while hyperscaler AI cloud/software revenue of roughly $100–120B generates perhaps 50–60% gross margins before allocated operating expense.

That implies **5–7% aggregate pre-tax spot ROIC versus an 8–10% WACC**. The estimate is coarse (the numerator is a gross-margin proxy before allocated opex and tax, so the true operating figure is lower) but directionally more honest than assigning all platform profit growth to AI capex. Return on incremental capital is a forward cohort question, so the decisive decomposition is where the dollar sits:

| Layer | Current return evidence | Capital-cycle interpretation |
|---|---|---|
| Silicon, leading-edge fabrication, and qualified HBM/networking tolls | **35–60%+ ROIC** at leaders | Scarcity plus qualification gates preserve pricing until the bottleneck moves |
| Frontier model layer | Inflecting from loss toward positive unit economics | Anthropic’s reported inference gross-margin expansion and first operating profit are proof of possible capture, not a sector average |
| Integrated hyperscaler cloud | Accretive but undisclosed | Internal demand, distribution, and custom silicon improve utilization; transfer pricing prevents clean attribution |
| Merchant GPU rental | Mid-teens unlevered gross IRR; negative equity FCF when levered; CoreWeave interest reached **25.8% of revenue** | Contestable capacity absorbs rental-price, refinancing, and residual-value risk |
| Internal ads/search/feed defense | Unmeasurable but strategically mandatory | Return is partly avoided franchise decay, not incremental revenue |

The value-layer test cuts against treating all infrastructure as a moat. A qualified silicon or workflow chokepoint can tax the stack; a financed building full of interchangeable accelerators is capacity, not a monopoly. The aggregate can destroy value while the toll layers earn exceptional returns.

### Same-period corporate profit-conversion ceiling

The following proxy asks a narrow question: how much after-tax operating-profit growth appeared while the company spent each dollar of capex? It uses:

`(2025 operating income – 2023 operating income) × normalized after-tax factor ÷ 2023–2025 cumulative capex`

Oracle uses FY2024–FY2026. The result is an upper bound because it attributes all profit improvement to all capex without a lag.

| Company | Three-year cumulative capex | Approx. after-tax operating-profit increase | Profit-conversion ceiling |
|---|---:|---:|---:|
| Microsoft | $137.1B | $32.8B | **23.9%** |
| Alphabet | $176.2B | $36.7B | **20.8%** |
| Amazon | $267.5B | $34.5B | **12.9%** |
| Meta | $134.2B | $31.0B | **23.1%** |
| Oracle | $83.7B | $4.5B | **5.3%** |

The proxy overstates causal return for four reasons:

- 2023 was a depressed cost base for some platforms, so layoffs and expense discipline inflate the numerator;
- much of 2025 capex had not entered service and therefore depresses the denominator’s apparent return only later;
- advertising recovery and pricing contribute without requiring the measured capex;
- gross capex includes maintenance and replacement, while operating-profit growth should be compared with incremental capital.

It still identifies the direction of travel. Microsoft, Alphabet, and Meta entered the 2026 build with high-return incumbent engines. Amazon’s asset intensity already reduced the conversion rate. Oracle’s profit growth did not keep pace with its build before the next, larger cohort arrived. These are **financing-capacity and attribution ceilings**, not evidence that the marginal AI cohort earns double-digit returns.

### Company-by-company marginal return judgment

#### Microsoft — strongest direct bridge, but the 2026 denominator changes the answer

Microsoft combines three monetization routes: Azure consumption, paid application seats, and internal productivity. FY2025 Microsoft Cloud revenue reached **$168.9B**, Azure exceeded **$75B**, and Intelligent Cloud operating income reached **$44.6B**. By FY2026 Q3, Microsoft reported **more than 20M paid Microsoft 365 Copilot seats**, 250% year-over-year seat-add growth, nearly **140,000 organizations** using GitHub Copilot, and a shift toward usage-based GitHub pricing.

The return case is stronger than a seat count suggests because the same cluster can sell Azure tokens, power GitHub/M365, and improve Microsoft’s own engineering. The risk is the denominator: calendar-2026 capex of $190B is approximately three times FY2025 cash capex. The existing segment profit cannot be treated as the return on the new cohort. Microsoft needs either Azure revenue acceleration on a very large base or Copilot to move from low-single-digit installed-base attachment toward mass deployment while preserving user-plus-usage pricing.

**Judgment:** Microsoft has the strongest direct bridge, but there is not yet enough disclosure to underwrite a double-digit return on the 2026 cohort. Copilot and agent consumption must become a second material consumption engine rather than a feature bundled into existing licenses merely to offset the larger depreciation denominator.

#### Alphabet — direct cloud returns lag, indirect search returns dominate

Google Cloud moved from **$1.7B operating income in 2023 to $13.9B in 2025**, while FY2025 Cloud revenue reached **$58.7B**. The Q4 2025 call disclosed **$240B of Cloud backlog**, more than 8M paid Gemini Enterprise seats, and rapid model-product growth. Search and YouTube remain the much larger profit pools.

Alphabet’s capex supports external Cloud, Gemini, Search quality, ad conversion, YouTube recommendations, and internal model development. This makes the true return wider than Cloud operating income. It also permits weak transfer pricing: first-party products may receive compute below an arm’s-length price, making Cloud margins look lower and Services margins higher.

The bear case is that AI answers substitute higher-margin search clicks, model/API prices fall faster than workload volume rises, and the company spends to defend a legacy profit pool rather than create an incremental one, not that “Gemini has no revenue.”

**Judgment:** Alphabet has the widest measurement range. Search monetization can make the blended strategic return acceptable even if direct Cloud asset returns remain below WACC; a defense of legacy search economics should not be counted as wholly incremental AI profit.

#### Amazon — proven cloud economics, highest near-term cash absorption among the integrated three

AWS generated **$128.7B of FY2025 revenue and $45.6B of operating income**. Amazon’s PP&E denominator is dominated by a mix of AWS and fulfillment, so AWS-specific installed-base returns are higher than the 12.8% signal. Trainium, Graviton, Nitro, and large customer commitments improve asset utilization and reduce reliance on merchant GPU pricing.

Amazon’s FY2025 capital purchases approached operating cash flow, and trailing free cash flow fell sharply as AI capex accelerated. Contracted capacity reduces demand risk but can introduce:

- customer concentration;
- minimum-price commitments that become unattractive if hardware economics improve faster than expected;
- power and delivery penalties;
- a mismatch between five-year contracts and shorter economic hardware lives.

**Judgment:** AWS has proven installed-base economics, but current cash absorption and contract/hardware-life mismatch prevent assuming the new cohort repeats them. The marginal return is unproven until free cash flow and AWS profit grow through the depreciation step-up.

#### Meta — strongest indirect economics, weakest causal proof

Meta generated **$196.2B of advertising revenue and $102.5B of Family of Apps operating income in 2025**. AI can lift ad ranking, recommendation engagement, creative generation, advertiser conversion, moderation, and engineering productivity. These are high-margin benefits on an enormous revenue base: a 2% durable uplift to ad revenue would equal almost $4B before knock-on engagement effects.

The same scale creates a misleading inference. Family of Apps profitability proves Meta can fund AI, not that the next $135B capex cohort earns a high return. Diminishing returns in recommendation quality, cannibalization from AI-generated content, and large foundation-model research costs can absorb capital without a discrete revenue line.

Meta also extended the useful life of most servers and network equipment to 5.5 years, reducing 2025 depreciation by **$2.92B** and increasing net income by **$2.59B**, according to its [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm). The accounting change raises current earnings while the technology cadence is accelerating.

**Judgment:** Meta’s franchise can finance the build and may earn a high strategic return, but causal ROIC remains unknowable. Ad auction, conversion, and engagement disclosures, not platform margin alone, must validate the cohort.

#### Oracle — contracted demand does not eliminate financing and residual-value risk

OCI revenue rose from **$6.8B in FY2024 to $10.2B in FY2025 and $18.1B in FY2026**, while FY2026 capex reached **$55.7B** and operating cash flow reached **$32.0B**. Oracle does not disclose OCI operating profit. It raised substantial debt and equity and expects further external financing for customer capacity.

Oracle can earn acceptable returns if contracts are take-or-pay, pricing includes financing and power risk, customers remain creditworthy, and the hardware can be redeployed after the initial term. Backlog is not enough: a low-margin, debt-funded contract can be value destructive despite guaranteed revenue.

**Judgment:** Oracle carries the clearest below-WACC equity-return tail even if the contracted asset earns a positive unlevered return. Customer solvency, financing cost, contract repricing, and residual hardware value are all load-bearing.

### Economic depreciation is the hidden swing factor

Accounting useful life and economic useful life are different:

- Amazon shortened the useful life of a subset of servers and networking equipment from six to five years because of faster AI/ML technology development in its [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm).
- Meta extended most server/network lives to 5.5 years.
- Microsoft describes equipment lives of roughly 2–6 years and disclosed that two-thirds of FY2026 Q3 capex was short-lived GPUs and CPUs.

Big Four depreciation and amortization is already running near **$170B annually** and growing 30–40%. The roughly **$1.09T 2025–2026 capex cohort**, at a blended depreciation rate near 13% (about 60% IT equipment at five-to-six-year lives and 40% shells/power at 15–25 years), adds approximately **$140B of annual D&A** as it enters service. Big Four D&A can therefore reach **$260–300B by 2028**. At a 50% incremental margin before the new depreciation, neutralizing the step-up, measured against the ~$110–120B pre-wave 2025 D&A base, requires roughly **$300–360B of incremental AI revenue by 2028**.

Useful-life extensions can shift perhaps $40–60B of annual depreciation to later periods, flattering near-term earnings, but that is smaller than the cohort wave itself. The bear claim becomes decisive only if older accelerators lose utilization and price faster than their accounting lives assume. Mid-2026 market evidence put four-year-old H100 rentals near **$2.29–3.12 per hour** with $12–22K resale values; Amazon shortened some AI-server lives to five years. Watch rental price, utilization, and revenue per watt rather than treating every life extension as either proof of fraud or proof of durability.

For an illustrative fully deployed **$500B annual AI-hardware cohort**:

| Economic life | Annual straight-line economic depreciation | Difference vs. five years |
|---|---:|---:|
| 5 years | $100B | — |
| 4 years | $125B | +$25B |
| 3 years | $167B | +$67B |

A new architecture does not make the old fleet worthless. Older accelerators can migrate from frontier training to fine-tuning, batch inference, smaller models, or lower service tiers. The relevant variable is **revenue per watt and per occupied rack after migration**, not benchmark leadership. Economic impairment occurs when the rental or internal transfer price falls faster than the decline in operating cost and the asset cannot stay utilized.

The best capex disclosure would therefore be vintage-level:

- installed MW and hardware cost;
- revenue-ready date;
- utilization by workload;
- realized revenue per accelerator-hour;
- power and networking cost;
- economic depreciation and resale value;
- customer concentration and contracted term.

No hyperscaler provides that full set.

### The cloud J-curve is a valid precedent only for the cash-funded tranches

The 2015–2019 cloud build looked overcapitalized before delayed utilization produced extraordinary returns. Two disanalogies limit the comparison:

1. cloud largely migrated existing, budgeted enterprise workloads onto assets with slow functional obsolescence;
2. AI must create or reprice demand while accelerators face rapid generational price-tier migration.

The cloud analogy is strongest for internally funded franchise defense and diversified enterprise cloud, where the same fleet serves multiple workloads. It is weakest for take-or-pay lab capacity and leveraged merchant fleets, where one counterparty and one hardware vintage carry the return. A flattering precedent applied across all four tranches conceals the exact cohort most likely to fail.

## II. Where AI-application revenue comes from

### The de-circularized 2026 demand ledger

Most industry revenue stacks count the same dollar three times: an enterprise pays a lab for API usage, the lab pays a hyperscaler for compute, and the hyperscaler buys accelerators. Only the enterprise dollar is end demand; the other two are transfers and capital formation inside the stack.

| Priced end-demand bucket | Mid-2026 annualized run-rate | Current anchors |
|---|---:|---|
| Consumer/prosumer subscriptions and app spend | **$25–35B** | 50M paid ChatGPT subscribers, mobile in-app purchases, Google One AI, Grok, and Perplexity |
| Coding and agent tools, net of model-lab pass-through | **$8–12B** | Cursor, Copilot, Cognition, Lovable, Replit, and adjacent builders |
| Enterprise API and AI-software attach | **$85–110B** | Frontier APIs, Microsoft AI, Agentforce, Now Assist, Palantir, and vertical tools |
| Government/sovereign services, excluding infrastructure purchases | **$3–6B** | Defense awards, procurement frameworks, and citizen-service deployments |
| Unitemized vertical services, governance/data tooling, and direct end-buyer cloud consumption | **$25–30B** | Top-down allowance for spend not cleanly assigned to the named vendors above |
| **Total priced end demand** | **$150–180B** | More than 100% year-over-year growth from a smaller base |

The component ranges are correlated and should not be summed at every independent high or low; the allowance reconciles the named-vendor build to the $150–180B top-down ledger. The resulting end-demand/capex ratio is only **0.18–0.20x**. Mature cloud economics typically carry capex at roughly 35–45% of revenue, so sustaining $850B of annual capex ultimately requires a **$2.0–2.5T revenue pool** or a structurally lower return hurdle. That is a coverage requirement, not a forecast.

### Five revenue mechanisms

| Mechanism | Buyer | Pricing unit | Pricing power | Revenue visibility |
|---|---|---|---|---|
| **Broad copilot** | Enterprise or consumer | Seat / month | Moderate; free alternatives cap price | High once seats are contracted; utilization may be low |
| **Agent / workflow execution** | Corporate and government process owner | Action, token, workflow, resolved case, or outcome | High when embedded in a governed system of record | Medium; usage is variable |
| **Creative and builder tools** | Consumer, prosumer, freelancer, agency | Subscription plus credits | Low for hobbyists; high for monetizing power users | Low-to-medium due bursty churn |
| **Vertical embedded AI** | Industry software buyer | Module, transaction, or premium bundle | High where data, liability, or distribution is proprietary | High after deployment; slow sales cycle |
| **Governance and control plane** | Enterprise, regulated buyer, government | Managed endpoint, agent, model, or usage | High because failure cost exceeds license cost | High; becomes mandatory as autonomous scope expands |

Three non-application return pools sit beside this table:

1. model/API and cloud infrastructure revenue;
2. advertising, commerce, and engagement uplift;
3. internal labor and infrastructure savings.

Model/API revenue already embedded in an application price would double-count the same buyer dollar. Advertising uplift and internal savings are distinct return pools, not application revenue. Each channel belongs once in a specific hyperscaler’s P&L bridge.

Falling inference prices reconcile exploding usage with slow revenue capture. Fixed-capability token prices have fallen by orders of magnitude while volume compounds several-fold annually. This is the Jevons mechanism: cheaper compute unlocks a much larger pool of previously uneconomic work. It guarantees neither provider revenue nor ROIC. Flat-rate subscriptions and free tiers pass the gain to users; consumption pricing, advertising, and outcome fees capture it. The sustainability question is therefore not whether demand is real, but whether volume elasticity exceeds price deflation on surfaces that can charge.

### Two demand engines, opposite shapes

| | Corporate/government automation | Consumer/prosumer creation |
|---|---|---|
| Ceiling | Deep: measurable digital work and service budgets | Shallow: household utility/entertainment budgets plus a thin professional tail |
| Speed | Slow: workflow and organization redesign | Fast: viral adoption in weeks |
| Pricing power | At execution, governance, and outcome layers | Weak at chat/generation; stronger only when output earns income |
| Durability | High after integration and audit trails | Low at the mass tier because switching and cancellation are easy |
| 2026 run-rate | **~$90–120B** | **~$40–50B** |
| 2031 direct revenue | **$270–440B including government** | **$85–135B** |

The capex bridge is a race: slow corporate depth must arrive before shallow consumer economics, frontier-lab burn, and credit markets exhaust the financing chain.

## III. Corporate and government process automation

### Current adoption is broad but shallow

Official surveys reject both extremes: enterprise AI is neither a demo-only category nor a fully scaled replacement cycle.

- The [US Census Bureau’s 2026 AI supplement](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) found **18% of firms** using AI in a business function and **32% on an employment-weighted basis**. Among adopters, **57% used AI in three or fewer functions**.
- Census data through May 2026 put overall firm use near **17–20%**, versus **37% for firms with at least 250 employees**. Information reached 39.7% and finance/insurance 33.9%.
- [Eurostat](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2) found **20.0% of EU enterprises with 10+ employees** using AI in 2025, versus 55% of large enterprises.
- The [UK Department for Science, Innovation and Technology](https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research) found 16% adoption, but only **7% of adopters used agentic AI**. Existing adopters reported 30% of staff using AI on average, while most firms reported productivity improvement without a revenue change.
- The same UK survey found **54% of existing adopters ready to scale**, versus **34% of firms planning adoption** ready to implement.

“Any use” measures access. Capex returns require paid, repeated, production use with enough autonomy to consume tokens and enough value to support price.

### The readiness funnel

The $15T-plus knowledge-work wage pool is not a five-year software TAM. The addressable-now pool is the **externalizable, measurable, digitized** slice of work: BPO at roughly $300B, IT services near $1.5T, customer operations, software development, finance and accounting, procurement, and repeatable back-office workflows. Physical work, relationship judgment, ambiguous management decisions, and processes without observable inputs or outputs do not become vendor revenue merely because a model can discuss them.

| Gate | Mid-2026 state | Likely resolution | Investment read |
|---|---|---|---|
| Workforce/process redesign | 60% report they cannot adapt operations fast enough; agents scale in ≤10% of functions | **~2032+** for the median firm | **Binding** |
| Data/context readiness | Decision rationale, permissions, and exceptions are not machine-readable | Firm-specific; culture-dependent | **Binding for depth** |
| Runtime governance/security | High incident rates; formal safety frameworks are emerging | 2027–2029 in regulated buyers | Resolving |
| Identity and audit plumbing | Agent identity products entered general availability in 2026 | 2027–2028 procurement cycles | Resolving |
| Model capability | Benchmarks have moved from fragile suggestion toward high reliability in bounded tasks | Continuous | No longer the median bottleneck |
| Legal liability | Strict-liability and precedent regimes remain incomplete | 2030+ for external acts | Slow; less binding for internal assistance |
| Government procurement | Long median cycles, partly offset by AI fast lanes | Structurally slow | Caps pace, not direction |

The central asymmetry is temporal: **supply is installed on financing clocks measured in quarters while demand matures on organizational clocks measured in years**. No supplier can capex its way through an enterprise’s unclear decision rights or fragmented data. This is why a task-level productivity result does not automatically become financial return.

Pilot failure statistics describe a power-law distribution, not zero demand. High abandonment can coexist with token growth and rapidly expanding agent revenue because successful deployments scale while the median pilot dies. The same evidence cuts against seller narratives: “accretive AI returns” without disclosed utilization, unit economics, or workflow depth is context theater until the 2028 depreciation test is passed.

### Organizational constraints that determine the 2031 range

| Constraint | Observable anti-signal | Economic effect | Likely 2026–2030 resolution |
|---|---|---|---|
| **Culture and incentives** | Managers rewarded for headcount; employees hide workarounds; errors punished more than experimentation | Pilots stay optional; savings never convert to fewer hours or more output | Slow. Requires role redesign, not a model upgrade |
| **Tribal process knowledge** | “Ask Sarah” is the workflow; exceptions live in email and memory | Context acquisition and verification consume the labor saved | Slow-to-medium. Process mining and documentation help |
| **Data silos** | Customer, product, permissions, and transaction history disagree across systems | Retrieval improves fluency but not truth; write-back becomes dangerous | Medium. Integration is technically solvable but politically owned |
| **Decision rights** | No rule for what an agent may approve, spend, change, or disclose | Human-in-the-loop remains at every step; token volume rises without labor removal | Medium. Policy and audit layers can codify authority |
| **Governance software** | No model inventory, evaluation set, prompt/version log, kill switch, or incident owner | Regulated workflows cannot move from assistive to autonomous | Medium-fast for large firms; slow for SMEs |
| **Liability and regulation** | Output can harm a patient, borrower, employee, citizen, or physical asset | Verification, documentation, and insurance become part of COGS | Slow in high-stakes sectors |
| **Legacy workflow architecture** | Screen scraping, brittle APIs, inconsistent identifiers, batch updates | Agent errors compound across tools; integration costs dominate model cost | Medium; incumbent workflow vendors capture the budget |
| **Measurement** | No baseline cycle time, quality, revenue, or error cost | CFO cannot distinguish real ROI from perceived convenience | Fast technically; hard culturally |
| **Change capacity** | Too many concurrent ERP, cloud, security, and restructuring programs | AI waits for scarce data, security, and operations staff | Persistent portfolio constraint |
| **Workforce redeployment** | Saved minutes do not change staffing, throughput, or service level | Productivity exists but financial ROIC does not | Slow; value appears first as quality/capacity, later as margin |

The UK survey supports the data and governance gates: 71% of non-adopters cited no identified need, 60% limited skills, 29% integration/scale complexity, and 21% data complexity. Large firms were more likely to rate data complexity as a material barrier. The [UK Business Data Survey 2026](https://www.gov.uk/government/statistics/uk-business-data-survey-2026/uk-business-data-survey-2026) found only 17% of AI-using businesses had formal or informal AI policy/guidance, although 56% of large users had a formal written policy.

### Which workflows monetize inside five years

| Workflow class | 2030 readiness | Why | Monetization model |
|---|---|---|---|
| Drafting, summarization, search, meeting and document assistance | High | Reversible output; human review already exists | Low-price seat bundle |
| Coding in greenfield/small repositories, testing, migration, documentation | High | Digital feedback loops; value measurable | Seat plus usage |
| Customer-service triage and resolution | Medium-high | Large volume and clear outcomes; permissions and exceptions remain | Per resolved case / usage |
| Sales research, lead preparation, campaign content | Medium-high | Data already digital; attribution is noisy | Seat, usage, or revenue-linked |
| Finance close, invoice, procurement, HR service workflows | Medium | Structured cores with many policy exceptions | Workflow/action pricing |
| Cybersecurity investigation and remediation | Medium | Machine-speed need supports price; false positives and authority constrain autonomy | Endpoint plus usage/outcome |
| Legal, healthcare, lending, insurance claims | Medium-low | High value but liability, evidence, and audit burdens | Premium vertical pricing with human review |
| Physical operations, field service, manufacturing control | Low-to-medium | Requires sensors, real-time state, safety cases, and hardware integration | Platform plus equipment/usage |
| Executive allocation, hiring/firing, high-value procurement | Low | Ambiguous objective and accountability cannot be delegated cleanly | Decision support, not autonomous outcome fee |

Productivity evidence is task- and context-dependent. The [NBER customer-support study](https://www.nber.org/papers/w31161) found roughly 14% productivity improvement across 5,179 agents, with larger gains for less-experienced workers. The [Harvard/BCG jagged-frontier experiment](https://www.hbs.edu/ris/download.aspx?name=24-013.pdf) found faster, higher-quality work inside the model frontier and worse accuracy outside it. [METR’s early-2025 randomized developer study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) found experienced open-source developers 19% slower on familiar repositories while believing they were faster; its [late-2025 update](https://metr.org/blog/2026-02-24-uplift-update/) pointed toward positive speedups but with selection effects and wide confidence intervals.

The combined read is not an average productivity percentage. AI raises the return to **novice transfer, bounded digital tasks, and measurable feedback**; it can lower productivity where tacit context, review burden, or expert baseline speed dominates.

### Government demand: large budgets, low financial-ROIC comparability

Government demand divides into four pools:

1. **Administrative copilots:** drafting, translation, records search, grants, procurement, tax, benefits, and case management.
2. **Citizen service:** contact centers, forms, eligibility navigation, fraud detection, and scheduling.
3. **Mission systems:** intelligence, defense, cyber, logistics, scientific analysis, and emergency response.
4. **Governance infrastructure:** model inventories, evaluation, audit, security, data lineage, and procurement controls.

The [US GAO](https://www.gao.gov/products/gao-25-107653) found reported AI use cases across 11 selected agencies nearly doubled from **571 in 2023 to 1,110 in 2024**, while generative-AI cases increased ninefold. Another GAO review identified **94 government-wide AI-related requirements** as of July 2025. Demand therefore grows together with compliance overhead.

Government will accept returns that a listed company would reject when the payoff is capability, resilience, intelligence advantage, or service quality. That makes sovereign demand a real capacity buyer but a poor proof of private-sector ROIC. Procurement cycles, accreditation, data classification, and budget appropriations also move revenue several years behind announced programs.

The conservative 2031 government application range is **$20–40B**. Sovereign infrastructure purchases are capex demand, not application end demand: they add supply and may accept sub-commercial returns, but they should not be used as proof of private-sector software ROIC.

### Corporate and government revenue range, 2031

Applying a decelerating adoption path to the current **$90–120B corporate run-rate** supports **$250–400B of corporate AI software, agents, and API revenue by 2031**, plus **$20–40B of government applications**. A wage-pool cross-check, 5% of relevant work automated with 30% vendor capture, lands near $225B, consistent with the low end once new tasks and governance spend are added.

The midpoint is **$355B of corporate/government revenue in 2031**. Organizational redesign is the binding variable. Hardening audit, provenance, and agent-identity rules can shift value toward execution-path incumbents with governed context, but it changes **where** the dollars land faster than **when** they arrive.

## IV. Consumer, prosumer, DIY, and vibe-coded demand

### Adoption is much larger than paid demand

[OpenAI reported](https://openai.com/index/scaling-ai-for-everyone/) more than **900M weekly ChatGPT users and 50M consumer subscribers** in February 2026: a paid conversion near 5–6% before adjusting for account overlap and plan mix. [Eurostat](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251216-3) found 32.7% of EU residents aged 16–74 used generative AI in 2025, mostly for personal use.

Free usage is economically valuable because it:

- creates habit and distribution;
- provides a conversion funnel for work and education;
- seeds prosumer projects;
- generates demand for advertising, commerce, or platform distribution;
- expands token volume and therefore infrastructure utilization.

It is not subscription TAM. Consumer revenue depends on paid conversion, retained usage, and the number of people willing to maintain multiple AI subscriptions.

### The current price ladder reveals willingness to pay

| User | Current market anchor | Buyer economics | Price sensitivity |
|---|---:|---|---|
| Curiosity / occasional consumer | Free or ad-supported | Substitutes are abundant; value is episodic | Very high |
| Regular individual | **$8–20/month** | Comparable to media/productivity subscription; median willingness to pay is below $20 | High |
| Serious creator or developer | ~$39–100/month | Saves several hours or replaces multiple tools | Medium |
| Heavy professional | ~$100–200/month | Tool directly supports income or billable output | Low if utilization is high |
| Small team / production builder | $100–4,000+ credits/month | Spend scales with projects, traffic, and revenue | Low on successful projects; high before product-market proof |
| Enterprise | Seat plus API/usage | Governance, security, support, and context justify premium | Low to price; high to unmeasured utilization and liability |

The ladder is visible in primary pricing:

- ChatGPT added an **$8 Go tier** and began testing ads on Free/Go; Gemini cut its top consumer tier from roughly $250 to $100.
- [Claude](https://claude.com/pricing) offers a $17 annualized/$20 monthly Pro plan, $100+ Max plans, $20 enterprise seats plus API usage, and higher-priced premium team seats.
- [GitHub Copilot](https://github.com/features/copilot/plans) spans free, $10 Pro, $39 Pro+, and $100 Max, then sells additional usage credits.
- [Replit](https://replit.com/blog/pro-plan) cut Core from $25 to $20 while launching a $100 Pro plan and $100–$4,000 pooled credit tiers.
- [Lovable](https://lovable.dev/pricing) offers free building credits, pooled usage rather than per-seat pricing, and credits for building, hosting, and AI features inside deployed apps.

Conversion and retention cap the mass tier:

- paid conversion is currently **5–6%** at OpenAI and only a small minority of payers hold more than one AI subscription;
- one cited distribution of what users would need to be paid to give up AI for a month (willingness-to-accept; willingness-to-pay runs lower) has a **$11.40 median** despite a $124.50 mean, exposing a thin high-value tail;
- AI apps retain roughly **21% at 12 months versus 31% for non-AI apps**, and many users cancel and restart around projects;
- the $100–200 tier is a professional-income segment, not evidence that the median consumer price can rise.

The $20 price is therefore an anchor under pressure, not durable model-layer pricing power. Pricing power reappears only when a tool owns deployment, collaboration, proprietary context, transactions, or a live production workflow.

### Vibe-coded output has a power-law revenue distribution

AI reduces the cost of producing software, websites, designs, video, analysis, and automations. It does not reduce the cost of attention, distribution, trust, customer acquisition, support, compliance, or selecting a useful problem by the same amount.

The tools can grow violently while their users’ output remains poorly monetized. Cursor, Lovable, Replit, and Copilot show real willingness to pay for creation; the missing disclosure is the share of generated projects that deploy, attach a custom domain or payments, retain users, and earn revenue. Uniform silence on those conversion metrics is negative evidence.

Available outcome signals point to a widening power law:

- high-vibe-score GitHub projects were reported as **3.2x more likely to be abandoned** within 18 months;
- security studies find high vulnerability rates in AI-generated code, creating a commercial-life and remediation burden;
- generic generative-AI freelance contract volume rose while per-contract earnings fell, indicating output-price deflation;
- solo-company formation increased while median early revenue fell and the top-decile/median gap widened.

The precise vendor estimates are noisy and several are aggregator-derived. The mechanism is sturdier than any single number: creation supply rises faster than attention, distribution, and trust, so a thin professional tail supports high usage while the median project remains a hobby.

Tool economics leak down the stack as well. Some individual coding subscriptions ran at negative gross margin before usage repricing, while repricing triggered customer backlash and model owners absorbed or displaced independent tools. Cheap intelligence makes the application layer easier to enter and harder to defend; the wrapper’s surplus accrues to the model, compute, deployment, or distribution owner unless the tool controls a production workflow.

My planning distribution for 1,000 consumer/prosumer projects is:

| Outcome by 24 months | Projects | Likely tool-spend behavior |
|---|---:|---|
| Prototype never published | 650 | Free tier or one paid month |
| Published, less than $100 lifetime revenue/value | 230 | $0–20/month; high churn |
| $100–10,000 cumulative revenue or measured savings | 90 | $20–100/month while active |
| $10,000–100,000 | 25 | $100–500/month plus hosting |
| More than $100,000 | 5 | $500–4,000+/month, team, governance, and infrastructure |

This is an explicit scenario, not observed industry data. Its purpose is to prevent a false inference: a tenfold increase in projects does not create a tenfold increase in subscription revenue. Most projects have zero monetization; a small tail pays for most usage.

The rational budget is tied to expected output:

| Project economics | Sustainable AI-tool budget | Buyer behavior |
|---|---:|---|
| Hobby / learning, no revenue | $0–20/month | Substitutes between free tools; cancels after build burst |
| Side project earning/saving $50–500/month | $20–50/month | Pays for convenience; sensitive to hosting and credit overages |
| Micro-SaaS / design practice earning $1,000–10,000/month | $50–300/month | Pays for iteration speed and deployment reliability |
| Agency / high-output operator above $10,000/month | $100–4,000+/month | Buys capacity, collaboration, governance, and support |

Tool vendors should therefore price the funnel in three steps:

1. **Free creation** to maximize projects and find the tail.
2. **Credit-based iteration** to monetize bursty work without forcing a high fixed subscription.
3. **Hosting, inference, payments, distribution, and governance** to participate in projects that become businesses.

Pure generation has weak pricing power. Production runtime has better retention because switching threatens a live application, customer data, and revenue. A builder platform that charges only for prompts subsidizes experimentation and misses the successful tail; a platform that owns deployment can let creation prices fall while revenue per successful project rises.

### 2031 consumer/prosumer range

| Revenue pool | Conservative driver | 2031 revenue |
|---|---|---:|
| General chat/assistant subscriptions | 2.5–3B weekly users × 6–8% blended conversion × $12–15 mass-tier ARPU, plus premium-tier and multi-subscription uplift (strict base multiplication alone gives $22–43B) | **$35–55B** |
| Coding, design, video, and other creation tools | Mass $8–25 tiers plus a thin $100–500 professional tail | **$40–60B** |
| App-store, companion, and miscellaneous monetization | Ads, distribution, and specialist products | **$15–25B** |
| **Consumer + prosumer total after overlap/rounding** | — | **$85–135B** |

This is roughly 2.2–2.7x the mid-2026 run-rate, or 17–22% annual growth, the slowest major AI demand pool because conversion, churn, and price deflation bind together.

Capped consumer revenue does not imply capped compute. Free tiers, ads, and persistent agents can multiply tokens per user by 10–100x. That demand is underwritten mainly by advertising economics, which concentrates sustainable consumer-serving capex in owners with distribution and ad monetization. Merchant capacity cannot infer a durable consumer revenue pool from token volume alone.

## V. Independent demand range

### Direct application and agent revenue, 2031

| Annual vendor revenue | Conservative range | Binding assumptions |
|---|---:|---|
| Corporate software, agents, and APIs | **$250–400B** | 25–35% decelerating growth; depth expands beyond copilots into measured workflows |
| Government applications | **$20–40B** | Procurement and authorization cap pace despite strategic willingness to pay |
| Consumer/prosumer | **$85–135B** | 6–8% paid conversion, $12–15 blended mass ARPU, thin professional tail |
| **Total direct application/agent revenue** | **$355–575B** | Revenue counted once; excludes internal stack transfers |

The **$465B midpoint** rests on observable adoption, price, churn, and deployment constraints rather than top-down wage-pool capture.

### Broader monetization bridge used for capex coverage

The direct table is not the whole hyperscaler return pool. A broader, still de-circularized path adds:

1. cloud/model runtime purchased directly by end enterprises or governments rather than embedded in an application price;
2. advertising and commerce revenue generated from free consumer usage;
3. internal engineering, support, moderation, search, and recommendation savings;
4. non-AI cloud workloads sharing the same power, networking, and shells.

The coverage path is **$150–180B in 2026 → ~$285B in 2027 → ~$450B in 2028 → ~$640B in 2029 → ~$850B in 2030**. The growth rates, roughly 80%, 60%, 45%, then 35%, are demanding but below the current small-base rate. Treat $850B as the **broader monetization bridge the capex case needs**, not as direct application TAM and not as a social-productivity estimate.

### What the ranges do and do not imply

- **Customers retain most value.** Labor savings and new output do not become vendor revenue one-for-one.
- **Cannibalization matters.** AI modules replace some software seats, services, search clicks, design work, and development spend.
- **Volume grows faster than dollars.** Falling unit cost expands tasks while compressing revenue per token.
- **Application winners may not be hyperscalers.** Workflow and vertical vendors can capture revenue while infrastructure owners bear the capital.
- **The $850B bridge is not enough by itself to validate $1.4T of 2028 capex.** Funding durability, margins, depreciation, utilization, and the share captured by asset owners still decide returns.

## VI. Pricing power by layer

### Where price survives model deflation

| Layer | Competitive structure | Price direction | Durable source of pricing power |
|---|---|---|---|
| Accelerator / scarce hardware | Concentrated, supply-constrained | High until capacity catches demand | Performance/watt, software ecosystem, networking, qualification |
| Cloud/model API | Several scaled suppliers plus open models | Down per unit; dollars depend on volume | Capacity, latency, reliability, distribution, data residency |
| General assistant | Low switching cost, free alternatives | Consumer anchor near $20; bundle pressure | Memory, default distribution, ecosystem, trusted identity |
| Specialist creation/build tool | Fragmented, fast feature copying | Entry price down; power tier stable | Workflow depth, deployment, collaboration, proprietary context |
| Enterprise system of record/action | Concentrated incumbent platforms | User-plus-usage and outcome pricing | Data, permissions, audit, write-back, change cost |
| Governance/control plane | Early but structurally required | Premium expands with autonomous scope | Cross-model visibility, policy, evidence, incident control |
| Transaction/distribution | Winner-take-most in successful niches | Share of outcome | Demand aggregation, payments, customer ownership |

The value-layer test points to a barbell:

- qualified infrastructure chokepoints can collect a toll while compute is scarce;
- application wrappers lose price as generation becomes abundant;
- context, governance, workflow execution, and distribution become the durable application-layer tolls.

This does not guarantee returns for every infrastructure owner. A scarce interface or qualified component is a toll; interchangeable financed capacity is a melting asset once scarcity clears. Too many toll roads built ahead of traffic can destroy builder returns while making every application cheaper.

### Price sensitivity differs by who captures the output

**Consumer:** pays from discretionary income. Free substitutes and low switching costs make demand elastic. Better model quality often increases usage without increasing willingness to pay.

**Prosumer:** pays from expected project income or avoided freelance labor. Demand is bimodal: a non-monetized builder behaves like a consumer; a successful operator behaves like a small enterprise. The same person can move from $20 to $500 per month when a project gains customers.

**Corporate:** the sticker price is small relative to wages, but total cost includes integration, security, evaluation, data work, review, change management, and duplicate software. Enterprises are less price-sensitive to a validated workflow and more sensitive to unused seats and unbounded consumption.

**Government:** contract price can be secondary to mission and sovereignty, but procurement, authorization, audit, and appropriations create extreme time sensitivity. High willingness to pay does not mean fast revenue recognition.

## VII. Capex projection, 2027–2031

### 2026 anchor

The conservative ecosystem anchor is **$850–900B** after netting customer prepays, overlapping lab commitments, lease treatment, and equipment already owned by a hyperscaler. [NVIDIA’s Q1 FY2027 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx) remain a hardware cross-check: quarterly Data Center revenue reached **$75.2B**, a $300B annualized rate before AMD, custom ASICs, CPUs, memory, networking, storage, racks, and system margins.

### Three constraints triangulate the path

1. **Funding:** Big Four operating cash flow is roughly $600B in 2026 and can reach about $780B by 2028 at 12–15% growth. With distributions reduced, internally fundable capex is approximately **$600–650B annually**. Adding a realistic $200–300B of annual debt, SPV, private-credit, and lab-equity capacity gives the core US financing chain a **$900B–1.0T 2028 ceiling without credit stress**; Chinese and sovereign balance sheets sit outside it. The §XI maximum-drawdown case relaxes exactly this no-stress assumption. A $1.4T global consensus outcome still assumes the credit channel expands for three more years after the crossover.
2. **Revenue coverage:** The broader monetization bridge rises from $150–180B in 2026 to roughly $450B in 2028 and $850B in 2030. Market tolerance requires capex/end demand to compress from 5–6x toward 2–2.5x. That supports about **$1.0–1.1T in 2027, $1.1–1.2T in 2028, and $1.3–1.5T by 2029–2031** only if demand compounds near the bridge.
3. **Physical delivery:** US datacenter power can expand from roughly 76GW in 2026 to 134GW in 2030, but turbine slots, transformers, and interconnections are constrained; global additions run roughly twice the US pace. At $45–55B per delivered GW, the global physical ceiling is around **$1.5–2.0T annually by 2028–2029**. Power binds the bull case, not the base. CoreWeave had energized only about 29% of 3.5GW contracted power and Nebius roughly 5–6% in the underlying evidence: capital is queuing rather than earning revenue. Power scarcity is also **locational and temporal, not a single national number** ([[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]): delivered cost turns on the node, the binding transmission constraint, the marginal generator by hour, and market design, so "gigawatts secured" masks wide dispersion in what a megawatt actually earns. The deeper point sharpens the maturity mismatch this note already carries: a nine-figure power project needs years of contracted cash flow, yet some labs' highest willingness-to-pay is concentrated in the next 6–12 months (a 90-day-cancellation deal at ~$5,000/MWh vs a 20-year take-or-pay at ~$271/MWh), so near-term compute scarcity can produce extraordinary prices without financing a durable long-duration asset. Contract duration and firmness, not headline dollar backlog, decide whether the queued capital becomes financeable.

The [US Department of Energy/LBNL](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers) estimated datacenters at 4.4% of US electricity in 2023 and 6.7–12% by 2028. The [IEA’s 2026 update](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions) projects global datacenter electricity use to double by 2030 and AI-focused use to triple.

### Tranche model: what corrects and what does not

| Tranche | Approx. share | Funding | Elasticity to disappointment |
|---|---:|---|---|
| A. Core-franchise defense and internal use | 30–35% | Operating cash flow | Near-zero; cuts last |
| B. Merchant enterprise cloud, excluding labs | ~25% | Mostly operating cash flow | Low-to-moderate; follows enterprise depth |
| C. Lab-serving hyperscaler/neocloud capacity | 25–30% | Debt, SPVs, prepays, vendor finance | **High; counterparty and refinancing dependent** |
| D. Lab/sovereign self-build | 10–15% | Narrative-priced equity or state capital | **Highest; first to freeze when funding reprices** |

The split avoids the most expensive classification error in the semiconductor cycle: treating structural workload growth and cyclical capacity as the same variable. A and B are early deployment backed by existing franchises; C and D carry late-installation financing behavior. A 2028 pause can coexist with rising tokens, inference units, and enterprise adoption.

### Scenarios

| Scenario | 2027 | 2028 | 2029 | 2030 | 2031 | Path logic |
|---|---:|---:|---:|---:|---:|---|
| **Base: digestion, not crash** | $1.00–1.10T | $1.10–1.25T | $1.05–1.20T | $1.20–1.35T | $1.30–1.50T | D&A and financing discipline stop C/D growth; A/B continue; deployment depth supports re-acceleration |
| **Bull: max-leverage race** | $1.20–1.30T | $1.50–1.70T | $1.80–2.00T | $2.00–2.20T | ~$2.0–2.2T | Every tranche races to the financing ceiling (§XI): distributions suspended, platforms lever to 2.0–2.5x, fragile tranches refinanced; power binds before financing; the $5.6–7.0T stack exhausts by 2030–31 |

The base path delivers **$1.30–1.50T in 2031 and $5.5–6.5T cumulative from 2027 through 2031**; the race path spends more in four years than the base does in five and exhausts the stack by 2030–31. The non-consensus feature is the shape: a 2028–2029 growth pause concentrated in merchant and lab-committed capacity, rather than a straight line or a systemic collapse, unless the §XI race defers the pause to the financing ceiling.

AI-hardware revenue can still rise from roughly **$450–500B in 2026 to $650–750B in 2028**, then flatten through 2029 as power and shells absorb a larger share of the envelope and custom ASICs lower cost per unit of compute. Qualification-gated suppliers can retain structurally higher troughs even while contestable capacity corrects.

### What would change the projection

The highest-information window is **hyperscaler calendar-2027 guidance in January–February 2027**. The first sub-20% guide from Microsoft, Alphabet, or Meta confirms digestion on schedule; uniform 30%+ guides move the path toward the max-leverage race case (§XI). A credit-spread shock pulls either scenario roughly one year earlier.

## VIII. The capex-to-profit bridge

### Three hurdles must be cleared

| Hurdle | Current/base-case arithmetic | Why it matters |
|---|---|---|
| **Spot return** | $50–70B attributable operating profit / $1.0–1.2T AI-incremental capital = **5–7% pre-tax** | The invested build is below an 8–10% WACC today |
| **Depreciation** | Big Four D&A **$170B → $260–300B by 2028** | Roughly $300–360B of incremental AI revenue at 50% margin is needed merely to neutralize the P&L step-up |
| **Steady-state coverage** | $850B annual capex / 35–45% capex-to-revenue = **$2.0–2.5T required revenue pool** | Current $150–180B end demand must compound by more than an order of magnitude or annual capex must settle lower |

Historical 13–24% corporate profit-conversion ceilings are not a credible forecast for the marginal cohort. They combine legacy cloud, advertising recovery, cost cuts, and capital not yet in service. The spot estimate is deliberately harsher because it asks what attributable profit exists against AI-incremental capital now.

### How integrated hyperscalers can still clear the hurdle

Direct applications alone, **$355–575B by 2031**, cannot support the whole build. An acceptable blended return requires several channels:

| Return channel | Economic role | Attribution risk |
|---|---|---|
| External cloud/model consumption | Direct utilization and revenue | Price per unit can fall faster than volume expands |
| First-party copilots, agents, and vertical products | Higher-margin application capture | Bundling can hide weak standalone willingness to pay |
| Non-AI cloud sharing the estate | Raises shell, network, and power utilization | Should not be labeled AI revenue |
| Advertising, commerce, search, and recommendation uplift | Monetizes free consumer usage and internal inference | Defense of a legacy pool is not wholly incremental |
| Internal engineering/support savings | Converts compute into avoided labor or faster output | Saved minutes do not become profit without role redesign |
| Sovereign/strategic capacity | Pays for resilience and option value | May rationally accept sub-commercial financial returns |

The most favorable case for Microsoft, Alphabet, Amazon, and Meta is that vertical integration lets one weak layer be subsidized by distribution, internal demand, advertising, and custom silicon, not that every AI project earns a high standalone return. Oracle and neoclouds have fewer offsets and more financing exposure.

The base case is **useful infrastructure with mediocre aggregate asset-owner returns and extreme layer dispersion**. It fails if low paid conversion, shallow enterprise autonomy, rapid API deflation, underutilization, power delay, and shorter economic lives occur together. It strengthens if broad enterprise write-back arrives before capex decelerates and old hardware retains utilization through price-tier migration.

## IX. Capital-cycle interpretation

### Structural demand and cyclical spend can coexist

The semiconductor-cycle discipline separates the economic, capital/inventory, and technology clocks:

| Clock | Current signal | 2026–2030 implication |
|---|---|---|
| **Economic demand** | AI users, tokens, enterprise seats, and cloud backlog rising | Workload volume remains structural |
| **Capital/inventory** | Capex doubles before the 2025 cohort is fully revenue-ready | 2028–2030 utilization and order correction risk rises |
| **Technology** | New accelerator, networking, memory, rack-power, and cooling generations arrive quickly | Old hardware migrates down the price curve; dollar capex can peak while compute units grow |

The likely cycle is a **unit/dollar divergence**, not a collapse in AI use:

- accelerator-hours, tokens, and agent actions continue rising;
- price per unit falls through better chips, quantization, distillation, caching, routing, and competition;
- suppliers and asset owners discover that demand growth does not guarantee revenue growth at the same rate;
- orders correct when installed capacity and contracted power finally catch demand.

The semiconductor bear case should therefore be timed to **utilization, rental pricing, order lead times, customer prepayments, and capex/OCF**, not to slower model improvement or a headline saying “AI adoption is high.”

### Functional overbuild versus financial overbuild

AI infrastructure can be:

- **functionally underbuilt** because demand, power, and strategic urgency remain large;
- **financially overbuilt** because several asset owners construct competing capacity and pass efficiency gains to customers.

Fiber, railroads, electricity, and cloud all created social value beyond the return earned by every builder. AI capex can follow the same pattern. The social and application surplus may accrue to enterprises, consumers, and new software businesses while a marginal datacenter cohort earns below its cost of capital.

The surge-cycle interpretation is tranche-specific rather than binary. Vendor-financed demand loops, the capex/OCF crossover, and narrative-priced equity are late-installation/frenzy signals. Cash-funded franchise defense and consumption-priced enterprise deployments are early deployment signals. Both phases can coexist because different owners and workloads sit on different clocks. The likely turning point is therefore a selective C/D pause, not proof that AI adoption failed.

The second-order bull case begins after that pause. Stranded merchant and lab capacity becomes cheap substrate for application and workflow businesses, as dark fiber did after 2000. The infrastructure builder can lose while the platform it installed increases economy-wide productivity.

### Positioning implications without collapsing the stack

- **Durable through digestion:** qualification-gated silicon, fabrication, HBM, networking, WFE service, and power/thermal bottlenecks where customers cannot rapidly qualify substitutes.
- **Fragile:** leveraged merchant capacity, single-lab exposure, short-duration funding against faster-obsolescing hardware, and sovereign projects whose capital is politically reversible.
- **Potential beneficiaries after digestion:** workflow, governance, distribution, and transaction layers that convert cheaper inference into measured outcomes.
- **Single expectations variable:** the market is under-testing the 2028 race between **$260–300B of Big Four D&A and the $300–360B of incremental AI revenue needed to offset it**.

The outside-view bear case is the repeated history of credit-funded capacity overshooting demand. The disconfirming bull evidence would be fleet utilization above 80%, enterprise workflow depth rising before capex slows, and provider gross profit compounding even as price per token falls.

## X. Leading indicators and falsifiers

### Dated observables

| When | Observable | Interpretation |
|---|---|---|
| Jul 30–31, 2026 | Amazon and Meta capex updates | 2026 exit velocity and whether the $850–900B anchor moves |
| Q3 2026 | Hyperscaler capex/OCF crossover and net debt issuance | Funding structure shifts from strategic cash to credit |
| H2 2026 | Frontier-lab profitability and financing versus commitment stack | Tranche C/D counterparty health |
| H2 2026–2027 | H100/B200 rental pricing and merchant gross IRR | Utilization, residual value, and depreciation validity; sustained merchant IRR above 25% weakens the toll-layer-only return thesis |
| Jan–Feb 2027 | **Hyperscaler calendar-2027 capex guides** | Highest-information base/bull branch point |
| 2027 | Neocloud refinancing costs or restructuring | Credit-event trigger before hyperscaler earnings weaken |
| 2027–2028 | Functions per enterprise adopter and agents scaled per function | Whether organizational depth arrives before capex digestion |
| Through 2028 | Big Four D&A versus disclosed AI revenue and savings | The $260–300B D&A / $300–360B revenue race |
| Quarterly | Token growth, provider gross profit, and effective price per task | Whether Jevons volume elasticity produces revenue capture |
| Quarterly | Weighted-average term and cancellation rights of AI power/colo contracts, not just dollar backlog ([[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]) | Whether "gigawatts secured" is financeable long-duration cash flow or short-duration willingness-to-pay; a sustained rise in 10–20-year take-or-pay from creditworthy buyers weakens the maturity-mismatch thesis, while 90-day-cancellation deals confirm it |

### Operating thresholds

| Indicator | Base-case requirement | Bull falsifier of the pause | Correction confirmation |
|---|---|---|---|
| Accelerator utilization | >70% on revenue-ready fleet | >80% despite rapid additions | <60–65% for two quarters |
| Enterprise depth | Median adopter moves beyond three functions | Audited write-back scales before capex slows | “Any use” rises but workflow depth does not |
| Consumer conversion | 6–8% with $12–15 blended ARPU | >10% without subsidy or churn deterioration | ≤5–6% as free/ads dominate |
| Provider price/volume | Gross profit rises despite unit deflation | >30% gross-profit growth through falling prices | Price decline exceeds volume and cost gains |
| Token volume | Remains above ~2x year-over-year while efficiency improves | Machine-to-machine demand sustains several-fold growth | A quarter below ~2x while unit cost keeps falling breaks the demand floor |
| Capex funding | A/B remain cash-funded; C/D growth stops | OCF catches capex without weaker distributions | Credit-funded share rises into weaker demand or A is cut >15% |
| Economic life | Four-to-five-year blended life | Old fleets retain high inference utilization | Three-year life, impairments, or rental-price break |

### Falsification

**The financial base case breaks downward if, by end-2028, Big Four D&A reaches $260–300B while incremental AI revenue and realized savings remain below $180B and fleet utilization falls below 65%.** Backlog, token volume, and user counts would not rescue cohort returns.

**The digestion thesis breaks upward if utilization stays above 80%, enterprise write-back scales across functions, and provider gross profit compounds while effective inference price keeps falling.** That combination would show usage elasticity and workflow capture strong enough to make this cycle structurally different from the credit-funded infrastructure base rate.

## XI. The game-theoretic offset: racing to the financing ceiling

The bearish lens of this note (sub-WACC spot returns, a 5–6x coverage gap, a 2028–29 digestion) carries one structural counterweight strong enough to equalise it. If terminal returns are power-law distributed (per the Executive judgment), the rational strategy for every participant with a seat at the table is to spend to its financing limit: the player that under-invests is close to guaranteed exclusion from the winner set, while the over-investor risks bad-but-survivable returns on a marginal cohort, for franchise owners at least; the deeply negative outcomes concentrate in the leveraged vehicles. No one's expected value is maximized by unilaterally slowing while rivals continue. The equilibrium is capitulation-by-exhaustion rather than capitulation-by-discipline: parties stop when they cannot finance the next cohort, not when spot returns disappoint.

The near-term implication is bullish for capex volume: there may be no meaningful digestion on the 2028 schedule. The financing chain is not yet exhausted: $600–650B of internally fundable capex after distribution cuts, plus $200–300B of annual debt/SPV/prepay/lab-equity capacity before credit stress (Section VII). If every tranche races to that ceiling, 2027–2028 capex prints at or above the base path on game theory alone, without requiring the enterprise-depth arrival the rest of this note treats as the binding gate. Under this reading the bull scenario's spending path needs no demand confirmation, only unwillingness to be the first to blink. The no-stress ceiling is not the limit: the leverage ledger below measures the full-drawdown capacity.

Observables that confirm the race is running: uniform 30%+ calendar-2027 guides despite the capex/OCF crossover; buybacks and dividends cut to fund capex (Meta's Q1 2026 suspension is the prototype); credit issuance accelerating into flat spot returns; lab commitments expanding faster than lab revenue. The same observables mark the offset's limit: a race run to financing exhaustion defers the correction and sharpens it, because exhaustion-capitulation is an air pocket where discipline-capitulation is a digestion. The bull case for near-term volume and the bear case for eventual cohort returns are the same mechanism observed at different dates.

### The leverage ledger: how much race remains

Converting the race into a capacity question means measuring every debt-like claim (reported debt, finance and operating leases, SPV structures, vendor financing, customer prepays) against the cash flow of the complex. The figures below are order-of-magnitude estimates assembled from the coverage data above, not a filing-by-filing build; the ceilings are calibrated to ratings behavior and the historical tripwires in the next subsection.

| Segment | Debt-like claims (est.) | Cash-flow anchor | Current multiple | Ceiling before credit stress | Capacity drawn |
|---|---|---|---|---|---:|
| Big Four platforms | $400–500B gross incl. leases; ~$100–200B net of cash | ~$700–750B EBITDA (on ~$600B OCF) | ~0.6x gross / 0–0.3x net | 2.0–2.5x net for A/AA franchise cash flows | **~5–15% net** |
| Oracle | ~$110–130B and rising | ~$30–35B EBITDA | ~3.5x | ~4.5x (IG cusp) | **~75–85%** |
| Neoclouds | ~$60–100B, largely asset-backed/prepay-secured | CoreWeave interest already 25.8% of revenue | n/m: negative levered FCF | Interest ~20–25% of revenue is the historical break line | **~90–100%** |
| Labs / sovereign | ~$1.4T of commitments vs $25–30B revenue (OpenAI) | Equity and state capital, not debt service | n/m | No historical builder survived commitments at ~50x revenue | **Undefinable; narrative-priced** |
| **Complex blended** | **~$0.8–1.1T** (listed segments plus ~$200–350B of complex-level SPV/vendor-finance/prepay structures) | **~$800–850B EBITDA** | **~1.0–1.3x** | **~3–4x historical terminal tolerance** | **~30–35%** |

The distribution is the finding, not the blended number: roughly two-thirds of the complex's unused leverage capacity sits on the four platform balance sheets, the owners of tranches A/B, the parties least likely to blink. The fragile tranches are already at or beyond their ceilings; the strong tranches have barely started drawing theirs. The blended row is a scale gauge against history, not a claim of fungibility: no entity here cross-guarantees another.

### Historical leverage ceilings

| Boom | Financing form | Peak intensity | Terminal tripwire | Resolution |
|---|---|---|---|---|
| UK canals, 1790s | Equity only | ~⅓ of projects never paid a dividend | Equity repricing; no credit chain | Slow fade; assets ran for a century |
| UK railway mania, 1840s | Partly-paid shares (contingent capital calls) | ~5–7% of GDP invested at the 1847 peak | Capital calls forced holder liquidation | 1847 crisis; the network kept operating |
| US railroads, 1880s–93 | Bonds | Fixed charges exceeded earnings for ~⅓ of mileage | Interest coverage <1x at the marginal road | ~30% of mileage in receivership; Morganization: assets migrated to strong balance sheets, fixed charges cut |
| Electric utilities, 1920s | Holding-company pyramids | ~8–10x effective leverage at apex layers | Refinancing of stacked, hidden debt | 1932 Insull collapse; PUHCA forced simplification |
| Telecom, 1996–2002 | ~$1.6T of debt and equity raised | Sector ~25–30% of the high-yield market; capex >100% of OCF for ~3 years | Marginal builders' interest >20–25% of revenue | ~35% cumulative HY default; capex −50–60%; traffic never stopped growing |
| Shale, 2010s | High-yield debt + serial equity | 2.5–4x debt/EBITDA with negative FCF for a decade | Equity window closed 2015–16 | ~$175B+ of debt through bankruptcy; discipline only at exhaustion |

Three tripwires generalize across the set: **(1)** the marginal builder's interest bill crossing ~20–25% of revenue; **(2)** the boom's paper saturating the credit market that funds it (telecom reached ~25–30% of high-yield in 2000); **(3)** the complex spending >100% of operating cash flow for two-to-three consecutive years. AI's mid-2026 position against them: tripwire 1 is already breached at the neoclouds (25.8%); tripwire 2 is approaching: $200–300B of annual AI-complex issuance would be 15–20%+ of investment-grade supply by 2028, before counting private credit; tripwire 3's clock starts at the projected Q3 2026 capex/OCF crossover, and two-to-three years lands on 2028–2029, the same date the depreciation wave and the digestion base case already occupy. Scale check: $850–900B is ~0.8% of gross world product and ~3% of US GDP; a $2T run-rate by 2030 approaches railway-mania intensity (5–7% of UK GDP in 1847) relative to the host economy.

### Max-leverage bull path to 2035

If the race runs to full drawdown (distributions suspended, platforms levered to 2.0–2.5x against ~$1.1T of 2030 EBITDA, fragile tranches refinanced to their ceilings, lab and sovereign equity staying open), the fundable stack for 2027–2030 is approximately:

| Funding source, cumulative 2027–2030 | Capacity |
|---|---:|
| Retained operating cash flow (full suspension, incl. Oracle; before non-AI maintenance capex) | ~$3.0–3.4T |
| Platform net issuance to 2.0–2.5x | ~$1.8–2.3T |
| Oracle + neocloud secured/ABS/prepay structures (net of prepays already in OCF) | ~$0.3–0.5T |
| Lab + sovereign equity | ~$0.5–0.8T |
| **Total fundable** | **~$5.6–7.0T** |

That stack finances an annual path of roughly **$1.2–1.3T (2027) → $1.5–1.7T (2028) → $1.8–2.0T (2029) → $2.0–2.2T (2030)**, carried as the §VII bull scenario, at which point the physical delivery ceiling ($1.5–2.0T annually by 2028–29, drifting higher as contracted power delivers) binds before the financial one and the stack is effectively exhausted. Three implications. First, the $1.4T consensus 2028 figure that the demand ledger cannot justify is comfortably financeable: financing cannot falsify the bull case before 2029; only demand, or a tranche-C/D tripwire, can. Second, the path ends power-bound (~$2.0–2.2T by 2030) with the platforms exiting at 2.0–2.5x net leverage and interest near 10–12% of EBITDA and ~5% of revenue: the platforms never hit the historical tripwires; the binding constraints are the fragile tranches and the credit market's absorption capacity. Third, the exit asymmetry: if organizational depth has arrived by the ceiling, the leverage amortizes into the deployment phase; if it has not, the correction lands on a complex at 85–100% of capacity, telecom-shaped rather than digestion-shaped, and, per every precedent from Morganization to MCI, the stranded assets migrate at cents on the dollar to the strongest owners. Historically the consolidation, not the construction, is where the returns were made.

Extending the clock to 2035 dates the maximum-leverage point and the shape beyond it. The stack draws down through 2030; the final borrowing completes in **2031**, with platforms at the 2.0–2.5x ceiling and interest near 10–12% of EBITDA. Beyond the ceiling the constraint inverts (no net new borrowing, capex capped at internal funding) and leverage deflates passively at ~0.2–0.3x per year on ~12% EBITDA growth, or through forced cuts if demand lagged:

| Race path | AI capex | Platform net leverage vs 2.0–2.5x ceiling | Financing state |
|---|---:|---:|---|
| 2027 | $1.20–1.30T | ~0.4–0.6x (≈20% drawn) | Distributions suspended; issuance begins |
| 2028 | $1.50–1.70T | ~0.9–1.0x (≈40%) | Above the $1.4T consensus; AI paper 15–20%+ of IG supply |
| 2029 | $1.80–2.00T | ~1.4–1.5x (≈60%) | Credit-market appetite becomes the swing variable |
| 2030 | $2.00–2.20T | ~1.9–2.0x (≈85%) | Power-bound; stack near exhaustion |
| **2031: maximum leverage** | ~$2.0–2.2T | **~2.0–2.5x (fully drawn)** | Final draw completes; capex capped at internal funding |
| 2032–33 | $1.4–1.9T | ~1.8–2.1x, deflating | Plateau-to-cut: EBITDA growth deleverages if demand arrived; forced cuts if it has not |
| 2034–35 | $1.9–2.6T | ~1.5–1.7x | Headroom reopens; a second borrowing leg becomes possible |

Base-path comparison: digestion's organic re-acceleration compounds from the §VII base 2031 exit ($1.30–1.50T) at ~8–12% to roughly **$1.8–2.2T by 2035**, so the two scenarios converge in the low-$2T range mid-decade. The race pulls ~$3T of spending forward into 2027–2031 (cumulative 2027–2035 ≈ $15–17T vs ≈ $12.5–14T base) and pays for it with a harder 2031–33; the base defers it and pays with the 2028–29 pause. Date and depth differ; the destination does not, by construction, since both paths share the same terminal demand.

## Addendum — 2026-08-12: Financing platforms, siting friction, and announced-MW conversion

Dated overlay on §§VII / X / XI. Log already cites the source notes; this section merges them into the framework (Tier A; snapshot `[[_Archive/Snapshots/Sustainability of AI Capex (pre-sync sync-2026-08-12-213539)]]`).

### What changed in the evidence set (Aug 10–12)

1. **Third-party compute financing institutionalized.** Nvidia’s MOUs with Apollo / BlackRock / Blackstone / Brookfield / Goldman / KKR target **>$500B** of third-party capital for AI infrastructure, with Nvidia optionally backstopping up to **25% (~$125B)** residual-value financing ([[Research/2026-08-12 - NVDA - Nvidia 500B AI Infrastructure Financing Platforms - news]]; Stratechery residual-value / 1873 framing in [[Research/2026-08-12 - NVDA - Risky Business Stratechery AI Financing - news]]). This is the §XI “fragile tranche / off-balance-sheet wave” mechanism named at platform scale: socializing refinancing/residual risk into pension/insurance AUM rather than hyperscaler IG alone.
    - *2026-08-15 Temple 8 inversion* ([[Research/2026-08-14 - LITE CRWV NBIS NVDA - Temple 8 Earnings Week 500B MOU - deep-dive]]): GPUs fail the toll-road / energy / CRE underwriting triad: useful life debated, residual value untested in a downcycle, cash-flow counterparties mostly unprofitable. The $500B is a design target, not a committed fund and not NVDA revenue; even full execution covers less than one year of ~$570B 2026 AI debt / ~$850B DC capex [1×: Temple 8]. Self-interest qualifier: the vendor promoting residual-value durability is the vendor whose ASP depends on lenders believing it.
    - *2026-08-15 TSPA fifth tranche* ([[Research/2026-08-14 - TSM NVDA - TSPA AI Servers Bottleneck Money - deep-dive]]): Foxconn–Quanta–Wistron–Wiwynn working capital + Taiwan bank group concentration sits below the factory SPV. Consignment vs ODM-owned GPU is the swing: an already-allocated GPU can miss a shipped-rack quarter if bank caps bind. Challenges treating announced-MW / reserved-CoWoS as delivered capacity.
2. **Sovereign / infra-GP ownership of purpose-built DCs.** Theseus Infrastructure (Anthropic × Macquarie Asset Management × GIC): Macquarie funds + GIC own the platform and fund majority equity; Anthropic anchors under long-term leases (US-first; Anthropic covers consumer electricity-price increases). No MW/capex disclosed ([[Research/2026-08-12 - Macro - Theseus Infrastructure Anthropic GIC Macquarie - news]]).
3. **Announced-MW conversion risk ≠ demand destruction.** AWS withdrew a ≤**500MW** / 2.5M sq ft Calvert County (MD) campus adjacent to Calvert Cliffs after a local political flip and an Aug 18 moratorium hearing; QTS’s ~$30B Digital Gateway was abandoned in July; Data Center Watch cites **75 projects / >$130B** delayed/canceled in 1Q26 partly from opposition ([1×: Data Center Watch via [[Research/2026-08-12 - Macro - AWS Calvert County DC Withdrawal - news]]]). Primary source attributes AWS’s move to development timelines / deliverability: **siting and politics, not CapEx cooling**. Dollars can still rise while announced-MW pipelines slip toward permissive / behind-the-meter / self-supply sites.
4. **Hyperscaler dollar demand still rising into a sell-the-guide regime.** Alphabet lifted 2026 capex to **$195–205B** (from $180–190B) with Q2 capex $44.9B (+100% YoY) and Cloud +82%; the stock sold ~7% on the print ([[Research/2026-08-12 - NVDA AVGO TSM 000660 - Alphabet Raises 2026 Capex to 205B - news]]). Order-book bullish for the silicon/memory/networking complex; multiple risk is now the default market response to the same headlines.
5. **1873 analogy sharpens financing-as-margin-defense.** Stratechery maps hyperscaler debt acceleration ($194B YTD by Jul 7 vs $108B all of 2025; interest cover <2x from ~5x) and Nvidia’s residual-value puts onto a Jay Cooke / Northern Pacific financing-overbuild template: financing innovation can be **margin defense and risk socialization**, not independent demand proof.

### Framework implications (no scenario rewrite)

| Framework hook | Read after this evidence | What would falsify the read |
|---|---|---|
| §VII physical-delivery / power | Siting/politics joins interconnect + turbine lead times as a **binding conversion filter** on announced MW. Track delivered MW and weighted-avg contract term/cancellation rights, not press-release MW. | Hyperscalers convert nuclear-adjacent / contested sites on schedule despite moratoria; announced→energized lag compresses. |
| §VII / §XI funding stack | Vendor platforms + sovereign/infra-GP SPVs are live **non-IG** capacity in the ~$5.6–7.0T fundable stack, and they pull residual-value / lease risk back onto the silicon vendor and into safety-seeking AUM. | First closed platform tickets remain tiny vs $500B headline, or residual-value puts are never drawn / marked. |
| §X observables | Add: (a) first disclosed closed ticket size under Nvidia’s platforms; (b) county/state moratorium count and MW stranded in hearing queues; (c) share of new MW behind-the-meter / self-supply vs grid-interconnect; (d) sell-the-guide persistence on further hyperscaler raises. | Capex guides cut and financing platforms stall and MW conversion accelerates: classic digestion, not delayed-MW. |
| Positioning without collapsing the stack | Separate **order-book** (still up: Alphabet, Theseus, Nvidia platforms) from **multiple / credit** (sell-the-guide + cover compression + residual-value socialization). Delayed MW is bearish for near-term GPU/networking units only if CapEx dollars also roll over; so far the evidence is rotation, not cancellation of intent. | CapEx guides roll over in dollars (not just MW slips) into 2H26/2027. |

### Executive-judgment touch (unchanged direction)

The note’s core split (structural demand vs cyclical spend; functional vs financial overbuild) is **reinforced, not rewritten**. New information thickens the §XI race-to-the-financing-ceiling path (named $500B platforms + Theseus) while adding a physical/political conversion haircut to announced MW (Calvert / QTS / DC Watch). Probability-weighted 2031 / cumulative paths in §VII are left intact pending a closed-platform ticket or a dollar CapEx guide cut.


## Related research
- [[Macro & Technology/AI Datacenter Financing Mechanism Design]]: deal-level mechanism-design companion: six financing templates (corporate / site-SPV+RVG / GPU-DDTL / prepay / vendor-support / infra-wrap) + shell-ABS (T7) + 8-axis permutation grid; the §XI leverage ledger here is its macro companion

- [[Research/2026-07-12 - Enterprise AI Adoption - Gating Factors Critique, 2030 Trajectory, Winners-Losers - synthesis]]
- [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]]
- [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]: nodal/LMP power-market framework; the "demand is now (6–12mo WTP) vs multi-year plant underwriting" maturity mismatch sharpens the funding-duration logic (§VII physical delivery, §I funding crossover); track contract term / cancellation rights, not just dollar backlog
- [[Research/2026-08-12 - NVDA AVGO TSM 000660 - Alphabet Raises 2026 Capex to 205B - news]]

## Primary-source register

### Company financials and capex

- [Alphabet FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm) and [Q4 2025 earnings call](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx)
- [Microsoft FY2025 annual report](https://www.microsoft.com/investor/reports/ar25/index.html) and [FY2026 Q3 earnings call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3)
- [Amazon FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm), [Q4 2025 release](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/), and [Q1 2026 release](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx)
- [Meta FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm), [Q4/FY2025 release](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/), and [Q1 2026 release](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/)
- [Oracle FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm) and [FY2026 results](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/)
- [NVIDIA Q1 FY2027 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx)

### Adoption, readiness, governance, and productivity

- [US Census — Microstructure of AI Diffusion](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html)
- [US Census — Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html)
- [Eurostat — 20% of EU enterprises use AI](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2)
- [UK DSIT — AI Adoption Research](https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research)
- [UK Business Data Survey 2026](https://www.gov.uk/government/statistics/uk-business-data-survey-2026/uk-business-data-survey-2026)
- [US GAO — Generative AI Use and Management at Federal Agencies](https://www.gao.gov/products/gao-25-107653)
- [NIST AI Risk Management Framework and Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework)
- [NBER — Generative AI at Work](https://www.nber.org/papers/w31161)
- [Harvard Business School — Navigating the Jagged Technological Frontier](https://www.hbs.edu/ris/download.aspx?name=24-013.pdf)
- [METR — Early-2025 developer productivity RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) and [late-2025 update](https://metr.org/blog/2026-02-24-uplift-update/)

### User scale and pricing

- [OpenAI — Next phase of enterprise AI](https://openai.com/index/next-phase-of-enterprise-ai/)
- [OpenAI — Scaling AI for everyone](https://openai.com/index/scaling-ai-for-everyone/)
- [Claude pricing](https://claude.com/pricing)
- [GitHub Copilot pricing](https://github.com/features/copilot/plans)
- [Replit Pro/Core pricing change](https://replit.com/blog/pro-plan)
- [Lovable credit and workspace pricing](https://lovable.dev/pricing)

### Power and physical capacity

- [US DOE/LBNL — 2024 US Data Center Energy Usage Report release](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers)
- [IEA — Energy and AI](https://www.iea.org/reports/energy-and-ai/)
- [IEA — 2026 datacenter electricity and bottleneck update](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)

- [[Research/2026-08-14 - LITE CRWV NBIS NVDA - Temple 8 Earnings Week 500B MOU - deep-dive]]: $500B MOU as GPU-as-financeable-asset inversion
- [[Research/2026-08-14 - TSM NVDA - TSPA AI Servers Bottleneck Money - deep-dive]]: ODM WC / Taiwan bank concentration as delivery choke

- [[Research/2026-08-15 - TSM AMAT LRCX - Chip Industry Week In Review - news]]: $500B third-party capital mixed reviews (cycle extension vs depreciating-GPU residual)

- [[Research/2026-08-15 - NBIS CRWV - Neocloud Q2 CoreWeave Nebius Cerebras - news]]: CRWV $9.4B Q2 / $35–39B FY capex vs $626M net loss; A100-into-2029 residual print

## Log

### 2026-07-28
- Created: independent AI-capex sustainability model — historical capex/return proxies, 2030 application TAM, organizational-readiness funnel, pricing segmentation, and 2026–2030 hyperscaler/hardware capex scenarios.

### 2026-07-29
- Manual merge: incorporated the conservative capex, ROIC, and demand case from Sustainability of AI Capex — $850–900B 2026 capex vs $150–180B end demand, 5–7% spot pre-tax ROIC, 2028–29 tranche-selective digestion, and lower 2031 direct-demand ranges; mental-model analysis moved into the body and vault references reduced.
- Manual edit: added spot-vs-terminal ROIC clarification to Executive judgment (5–7% is backward-looking; terminal returns power-law with capital-weighted mean above WACC) and new §XI game-theoretic offset (all players race to the financing ceiling before any blinks) — bull-case counterweight implying digestion may defer until financing exhaustion.
- Manual edit: extended §XI with leverage-capacity scenario analysis — complex at ~30–35% of historical terminal leverage (platforms ~10–20%, Oracle ~75–85%, neoclouds ~90–100%); three boom tripwires (interest/revenue, credit-market saturation, capex>OCF 2–3yrs) vs canal/railway/utilities/telecom/shale; max-drawdown stack ~$5.5–6.7T funding $2.0–2.2T by 2030 — financing cannot falsify the bull before 2029.
- Manual edit: replaced §VII bull scenario (power-bound boom) with the §XI max-leverage race path ($1.5–1.7T 2028 → $2.0–2.2T 2030); probability-weighted 2031 now $1.4–1.5T, cumulative 2027–31 $6.0–6.5T. Website essay scenario table now presents base + max-leverage bull only (bear row removed from essay; retained here).
- Manual edit: stripped the bear scenario from the note per user direction — §VII row deleted, probability labels dropped (base + max-leverage race presented as the two paths), branch-point and threshold-table labels updated (Bear confirmation → Correction confirmation). Downside falsifiers in §X retained; argument-level bear-case discussions (Alphabet, depreciation, outside view) untouched.
- Manual edit: consistency pass across note + website essay — race-path funding reconciled (retained OCF $3.0–3.4T full-suspension, stack $5.5–6.7T → $5.5–7.0T so the path no longer outruns its stack); complex-level SPV/vendor/prepay claims (~$200–350B) itemized in the leverage ledger; no-stress ceiling vs race-case bridge added in §VII; D&A neutralization arithmetic anchored to the ~$110–120B pre-wave 2025 base.
- Manual edit: extended §XI race scenario to 2035 in note + essay — maximum-leverage point dated to 2031 (2.0–2.5x fully drawn), 2032–33 plateau-to-cut at $1.4–1.9T as leverage deflates ~0.2–0.3x/yr, 2034–35 headroom reopens ($1.9–2.6T); base and race converge in the low-$2T range by 2035 (~$15–17T vs ~$12.5–14T cumulative 2027–35).
- Addressed audit findings: applied Tier-1 fixes from [[_Archive/Docs/2026-07-29 - Sustainability of AI Capex - Audit Report]] to essay + note — profit-proxy relabel, invested-through-2026 wording, Meta paused (not suspended), crossover as projection, WTP→WTA, platform leverage on net basis (~5–15% drawn), stack total $5.6–7.0T with prepay/maintenance qualifiers, global power scope, world+US GDP framing, METR update, tranche C+D reconciliation, composition/convergence caveats, essay Sources footer; note subs-row drivers annotated. Rejected: range-pairing and Alphabet-staleness findings (methodology inconsistent/misread); bear scenario stays removed per user direction.

### 2026-08-06 (/sync)
- [[Research/2026-08-05 - AI Data Center Power Markets and Electricity Pricing - deep-dive]]: power-markets deep-dive supports and sharpens the funding-duration logic — added nodal+temporal scarcity + the 6–12mo-WTP-vs-multi-year-underwriting maturity mismatch to §VII physical-delivery, and a §X observable (weighted-avg AI power/colo contract term + cancellation rights, not dollar backlog; a rise in creditworthy 10–20yr take-or-pay weakens the mismatch). Tier A (snapshot). Executive judgment unchanged. Snapshot: [[_Archive/Snapshots/Sustainability of AI Capex (pre-sync 2026-08-06-184125)]]

### 2026-08-12
- [[Research/2026-08-12 - Macro - AWS Calvert County DC Withdrawal - news]]: AWS Calvert 500MW withdrawal = siting/politics friction (moratorium risk), not demand destruction — raises announced-MW conversion risk while CapEx dollars rotate to permissive/self-supply sites.
- [[Research/2026-08-12 - Macro - Theseus Infrastructure Anthropic GIC Macquarie - news]]: Theseus (Anthropic×Macquarie×GIC) shows sovereign/infra-GP capital owning purpose-built DCs under long-term leases — extends off-balance-sheet financing wave alongside NVDA $500B platforms.
- [[Research/2026-08-12 - NVDA - Risky Business Stratechery AI Financing - news]]: Stratechery maps vendor/infra financing + residual-value backstops onto 1873-style overbuild risk — financing innovation is margin defense as much as demand proof.
- [[Research/2026-08-12 - NVDA - Nvidia 500B AI Infrastructure Financing Platforms - news]]: Nvidia >$500B third-party financing platforms institutionalize GPU/infra funding outside hyperscaler IG debt alone.
- [[Research/2026-08-12 - NVDA AVGO TSM 000660 - Alphabet Raises 2026 Capex to 205B - news]]: Alphabet 2026 capex $195–205B + sell-the-guide — order-book up, multiple risk default.

### 2026-08-13
- [[Research/2026-08-13 - NVDA TSM AVGO MRVL - Amazon 2026 Capex 220B - news]]: Amazon lifts 2026 capex to ~$220B (from ~$200B), citing memory costs; AWS backlog $496B, constrained through 2027 into 2028 — complements Alphabet $195–205B; sell-the-guide overlay.
- [[Research/2026-08-13 - Datacenter Capacity Cancellation Myth - deep-dive]]: SemiAnalysis YE26 NA hyperscaler self-build moved ~1% vs media "half canceled" — announcement-layer overcount, not demand destruction; supports the structural-demand vs cyclical-spend split.
- [[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]]: accredited grid headroom turns negative 2027; BTM forced for >half of new US DCs from 2028 — physical conversion constraint, not a capex-dollar cut.
- [[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]]: $11.6/hr neocloud payback is a shortage-vintage retail outlier; Rubin 2× capex keeps the renter below the layer owner.

### 2026-08-14
- [[Research/2026-08-11 - NVDA Superposition AI Factory Underwriting - deep-dive]]: $500B platforms are uncommitted MOUs; residual-value / first-loss is the credit variable — financing innovation ≠ funded WACC cut.
- [[Research/2026-08-06 - Hyperscaler GPU Repricing Cycle Capex to L3 L4 - deep-dive]]: tape prices FCF burn; source prices contracted-rate catch-up — race-to-ceiling intact, L3/L4 rent hypothesized.
- [[Research/2026-08-07 - SpaceX 10GW 2027 Microsoft Offtake - deep-dive]]: 90-day CSA underwrites less power-project debt than 20-yr take-or-pay — duration mismatch live.

- [[Research/2026-08-14 - SPCX NVDA - xAI 10GW 2027 Compute Target - news]]: Musk $30–50/W → $300–500B at 10GW by end-2027 — revenue claim, not a CSA/duration print; does not close the capex-to-profit bridge.
### 2026-08-22
- [[Research/2026-08-21 - NVDA - SemiAnalysis Open Models Catching Up - deep-dive]]: $100M/MW vs sub-$30M/MW auction is a reallocation inside lab-serving capacity, not a coverage-gap close and not a digestion print.
## Related Research
- [[Research/2026-08-12 - NVDA AVGO TSM 000660 - Alphabet Raises 2026 Capex to 205B - news]]
- [[Research/2026-08-12 - Macro - AWS Calvert County DC Withdrawal - news]]
- [[Research/2026-08-12 - Macro - Theseus Infrastructure Anthropic GIC Macquarie - news]]
- [[Research/2026-08-12 - NVDA - Risky Business Stratechery AI Financing - news]]
- [[Research/2026-08-12 - NVDA - Nvidia 500B AI Infrastructure Financing Platforms - news]]
- [[Research/2026-08-13 - NVDA TSM AVGO MRVL - Amazon 2026 Capex 220B - news]]
- [[Research/2026-08-13 - Datacenter Capacity Cancellation Myth - deep-dive]]
- [[Research/2026-08-13 - BE VRT - US Grid Constraints 40GW BTM Datacenter 2028 - deep-dive]]
- [[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]]
- [[Research/2026-08-11 - NVDA Superposition AI Factory Underwriting - deep-dive]]
- [[Research/2026-08-06 - Hyperscaler GPU Repricing Cycle Capex to L3 L4 - deep-dive]]
- [[Research/2026-08-07 - SpaceX 10GW 2027 Microsoft Offtake - deep-dive]]
- [[Research/2026-07-29 - LEGO Modular Datacenter Construction - deep-dive]]
- [[Research/2026-08-14 - SPCX NVDA - xAI 10GW 2027 Compute Target - news]]
- [[Research/2026-08-25 - NBIS - ClickHouse and Avride Private Stakes - synthesis]]: NBIS converts (Mar $4.34B + Aug $5.75B) as equity-linked claims in the neocloud tranche; stakes booked ~$1.6B, unsold
### 2026-08-15
- [[Research/2026-08-14 - LITE CRWV NBIS NVDA - Temple 8 Earnings Week 500B MOU - deep-dive]]: $500B MOU inverted as residual-value experiment that fails the toll-road triad; design target, not committed fund.
- [[Research/2026-08-14 - TSM NVDA - TSPA AI Servers Bottleneck Money - deep-dive]]: ODM WC / bank-group concentration is a fifth financing tranche below the factory SPV.
- [[Research/2026-08-15 - TSM AMAT LRCX - Chip Industry Week In Review - news]]: $500B residual-value debate restated — financing innovation ≠ funded WACC cut; race-to-ceiling intact.
- [[Research/2026-08-15 - NBIS CRWV - Neocloud Q2 CoreWeave Nebius Cerebras - news]]: CRWV capex/loss tape + A100-2029 residual is the credit/residual-value variable already in Superposition / Temple 8 — no new tranche.
- Companion note created: [[Macro & Technology/AI Datacenter Financing Mechanism Design]] — deal-mechanics layer (templates T1-T7, waterfall grammar, 8-axis permutation grid) to this note's §XI macro leverage ledger; web-verified deltas (El Paso Sopaipilla 7.534%, CRWV ~$35.6B, BofA $370B XPV RVG).
- [[Research/2026-08-17 - TSM - TSPA Taiwan AI Fiscal Dividend - news]] — Taiwan converting AI-boom tax receipts into a balanced-budget cash transfer + defence/tech spend; live test is whether the windfall finances the next growth cycle before capex slows
- [[Research/2026-08-16 - Macro PJM - SemiAnalysis 12B Modeling Mistake - deep-dive]] — US-ISO color: $12B ratepayer overcharge as RRS error does not accelerate the queue and does not add accredited MW

### 2026-08-18
- [[Research/2026-08-17 - TSM - TSPA Taiwan AI Fiscal Dividend - news]]: Taipei fiscalizes the AI boom (NT$10k cheque, defence >3% GDP, NT$40.6B AI infrastructure) — same durability question as this note's capex-to-profit bridge; not a WACC or residual-value print.
- [[Research/2026-08-16 - Macro PJM - SemiAnalysis 12B Modeling Mistake - deep-dive]]: PJM $12B overcharge is a modeling error locking 11–15y contracts — financing/siting friction, not new accredited supply.
- [[Research/2026-08-18 - SPCX - 10GW Datacenter Pipeline Feasibility - deep-dive]]: SPCX 10GW-compute needs ~5–6× the historical build rate (no org has energized >3GW IT/yr) + ~½ global Blackwell + $320–440B — a vivid §IX functional-underbuild / power-binds instance; orbital Starmind = the terrestrial-ceiling escape hatch, 2029+ — framework unchanged.
- [[Research/2026-08-21 - NVDA - SemiAnalysis Open Models Catching Up - deep-dive]]: $100M/MW frontier-token API vs sub-$30M/MW open TaaS reallocates incremental GW toward labs (today 27% of 2026 net new GW) — mix inside tranche C, not a capex-dollar cut

### 2026-08-20
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged

### 2026-08-26 (/sync all)
- [[Research/2026-08-25 - NBIS - ClickHouse and Avride Private Stakes - synthesis]]: NBIS's March $4.34B + August $5.75B converts add ~$10B of equity-linked claims to the neocloud tranche and the ClickHouse/Avride 'reserve' is ~$1.6B at book, unsold — the ~90–100% drawn read for the tranche stands; leverage ledger and scenarios unchanged (Tier B, no snapshot).
