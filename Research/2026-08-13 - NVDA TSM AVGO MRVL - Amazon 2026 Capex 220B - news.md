---
publish: false
date: 2026-08-13
updated: 2026-08-14
tags: [research, daily-intel-triage, news, macro, datacenter, NVDA, TSM, AVGO, MRVL, 000660]
sector: macro
ticker: NVDA
propagated_to: [NVDA, TSM, AVGO, MRVL, 000660]
source: 'https://www.datacenterknowledge.com/infrastructure/amazon-lifts-ai-infrastructure-spending-to-220b-as-demand-outpaces-capacity'
source_type: news
---

# Amazon Lifts 2026 Capex to ~$220B; AWS Still Capacity-Constrained into 2028

## Thesis Delta
Consensus prices (and has been selling) another hyperscaler capex raise as late-cycle overbuild after Alphabet’s $195–205B lift ([[Research/2026-08-12 - NVDA AVGO TSM 000660 - Alphabet Raises 2026 Capex to 205B - news]]) → this source implies Amazon’s +$20B to ~$220B is HBM/memory inflation on already-contracted 2027–2028 demand, not a new construction wave, while Anthropic/OpenAI multi-gigawatt Trainium bookings plus a live merchant-chip sale exploration is the ASIC-mix variable [[Theses/NVDA - Nvidia]] §Outstanding Questions already flags. Transmission to [[Theses/TSM - Taiwan Semiconductor]] CoWoS, [[Theses/AVGO - Broadcom]] Ethernet/XPU, [[Theses/MRVL - Marvell Technology]] custom/optics, [[Theses/000660 - SK Hynix]] HBM — hypotheses [G-4] Perez frenzy, [G-13] sell-the-guide, [G-7] two-bucket ROIIC, [G-14] AI pulling traditional compute, Industry #1 (memory the named bottleneck) + #8 (Trainium) + #18 (deployment vs optimization).

## Summary
Shane Snider’s Data Center Knowledge recap of Amazon’s Thursday Q2 call (31 Jul 2026, still circulating 13 Aug) frames the print as a capacity-delivery story, not a demand-finding story. 2026 capex moves to approximately $220 billion from about $200 billion; CEO Andy Jassy attributes the $20B delta to higher memory costs rather than a broader construction push, and lists “resource and supply volatility, including for memory chips” among business risks. The same call says AWS will still lack capacity to meet all demand in 2026 *and* 2027, with contracted 2028 demand already “striking.” Sid Nag (Tekonyx) reads that pairing as proof the industry is in the infrastructure-deployment phase, not the optimization phase: compute, power, networking, and data-center construction are the binding constraints, not customer interest. He adds that the raise was driven by the cost of *equipping* halls — particularly high-bandwidth memory — so the next investment phase is shaped as much by silicon and memory economics as by concrete, steel, and power. That is the named-bottleneck handoff from last cycle’s CoWoS/wafer scarcity to HBM as the cost inflator inside a hyperscaler guide.

AWS printed its fastest growth in 18 quarters: revenue $42.2B (+36.7% YoY), operating income $16.6B, $169B annualized run-rate. AI and custom-silicon businesses each now exceed $25B ARR. Backlog hit $496B at a triple-digit year-over-year rate, and Jassy said Amazon remains on pace to double power capacity by end-2027 versus 2025, with much of the planned 2027 capacity already reserved. Steven Dickens (HyperFrame) ties the print to Amazon stepping back from model development toward model hosting — “back to what it does best, namely infrastructure.” Holger Mueller (Constellation) calls it the “gold rush era”: vendors must build to sell, and Amazon is assembling the same investment stack as peers — except it must keep funding retail while running record AI capex, a constraint Google/Microsoft do not share at the same scale.

Jassy split the $220B into two capital-return buckets. Data centers take capital roughly two years before revenue and stay productive more than 30 years. Servers and networking typically break even in less than three years and then throw free cash flow until replacement. His ROI claim is duration, not just dollars: “as we get a few years out and the revenue growth outpaces the incremental CapEx growth … the resulting revenue, free cash flow, and return on invested capital are very compelling.” He also said AWS could “very possibly” become a trillion-dollar annual-revenue business. Complementarity, not substitution, is the demand architecture he sold: reinforcement learning, post-training, agent orchestration, storage, and vector databases all pull conventional compute and storage; Graviton benefits as customers deploy more AI; “growth in one is driving growth in the other.” CFO Brian Olsavsky said enterprises migrating traditional workloads are expanding core cloud consumption *alongside* AI. Mueller’s enterprise read matches: AI handles intent and orchestration while conventional infrastructure and databases execute the underlying work.

The silicon-mix paragraph is the non-consensus hook for the book. Jassy said Anthropic and OpenAI have made multi-year, multi-gigawatt commitments to Trainium, with a widening list of startups and enterprises on the accelerator, and that Amazon is exploring selling Trainium chips outside AWS after inbound interest in third-party data centers — “I expect there’s a real chance we’ll do that in the future.” Matt Kimball (Moor Insights & Strategy) calls two frontier labs putting multi-year, multi-GW behind Trainium “about the strongest validation a piece of silicon can get,” because training scale is where accelerators either hold up or don’t, and says the commitments challenge the perception that [[Theses/NVDA - Nvidia]] and [[Theses/AMD - Advanced Micro Devices]] have locked training. He immediately qualifies the merchant path: selling chips and racks means public roadmaps, field engineering, lifecycle support, system integration, and channel — go-to-market motions other vendors spent decades building. The source therefore simultaneously extends the AI-infra order book (memory + power + backlog into 2028) and puts a dated ASIC-share test on the table (Trainium as training-scale, not just inference-price, plus a possible merchant Trainium).

## Evidence

| Metric | Figure | Tag |
|---|---|---|
| 2026 capex guide | ~$220B, from ~$200B | [web: datacenterknowledge.com / Amazon Q2 call] |
| Capex delta (cited cause) | Higher memory costs, not a broader construction push | [web: datacenterknowledge.com / Jassy] |
| Named risk language | Resource and supply volatility, including memory chips | [web: datacenterknowledge.com / Amazon] |
| Capacity constraint | Not enough capacity in 2026 or 2027; 2028 contracted demand “striking” | [web: datacenterknowledge.com / Jassy] |
| AWS Q2 revenue | $42.2B (+36.7% YoY); fastest growth in 18 quarters | [web: datacenterknowledge.com] |
| AWS Q2 operating income | $16.6B | [web: datacenterknowledge.com] |
| AWS ARR | $169B annualized | [web: datacenterknowledge.com] |
| AI ARR | >$25B | [web: datacenterknowledge.com] |
| Custom-silicon ARR | >$25B (separate from AI ARR) | [web: datacenterknowledge.com] |
| AWS backlog | $496B; triple-digit YoY | [web: datacenterknowledge.com] |
| Power build | Double 2025 capacity by end-2027; much of 2027 capacity already reserved | [web: datacenterknowledge.com / Jassy] |
| DC payback (Jassy) | Capex ~2 years before revenue; productive >30 years | [web: datacenterknowledge.com] |
| Server/network payback (Jassy) | Break-even <3 years, then FCF until replacement | [web: datacenterknowledge.com] |
| Long-run AWS claim | “Very possibly” a $1T annual-revenue business | [web: datacenterknowledge.com / Jassy] |
| Trainium anchors | Anthropic + OpenAI: multi-year, multi-gigawatt | [web: datacenterknowledge.com / Jassy] |
| Merchant Trainium | Exploring sales outside AWS to third-party DCs; “real chance” | [web: datacenterknowledge.com / Jassy] |
| Call date | Thursday, 31 Jul 2026 (recap circulating 13 Aug) | [web: datacenterknowledge.com] |

| Speaker | Claim | Tag |
|---|---|---|
| Sid Nag (Tekonyx) | Deployment phase, not optimization; HBM the cost inflator; next phase = silicon/memory economics as much as concrete/steel/power | [web: datacenterknowledge.com] |
| Steven Dickens (HyperFrame) | Amazon off model-development, onto model-hosting / infrastructure | [web: datacenterknowledge.com] |
| Holger Mueller (Constellation) | “Gold rush” — build to sell; Amazon must fund retail + AI capex | [web: datacenterknowledge.com] |
| Matt Kimball (Moor Insights) | Multi-GW Trainium from two frontier labs is training-scale validation; challenges NVDA/AMD training lock; merchant path requires decades-deep GTM | [web: datacenterknowledge.com] |
| Brian Olsavsky (CFO) | Traditional-workload migrants expand core cloud alongside AI | [web: datacenterknowledge.com] |

## Contradiction Check
**Supports** [[Theses/000660 - SK Hynix]] §Summary HBM-cycle and live-layer L1 (contracted memory, winner-take-most): a hyperscaler named *memory costs* as the primary $20B guide inflator and flagged memory-chip supply volatility as a risk, which is the opposite of Goldman-style 2026 HBM oversupply in 000660 §Outstanding Questions Q5. Does **not** resolve 000660 → LOW (Samsung >35% of Rubin HBM in Q3–Q4 2026) — Amazon did not split HBM vendors.

**Supports** [[Theses/TSM - Taiwan Semiconductor]] §Summary CoWoS/N2 durability and Conviction Trigger → LOW’s first leg (any 2027 HPC growth <10% = cycle topping): reserved 2027 power + 2028 contracted demand + $496B backlog is the opposite of a 2027 HPC air-pocket. Qualifier: if the +$20B is almost entirely HBM ASP, incremental CoWoS *units* are smaller than the headline capex implies — test TSM packaging commentary, not the Amazon dollar print.

**Supports** [[Theses/AVGO - Broadcom]] §Summary Ethernet-as-compute-agnostic substrate and §Outstanding Questions (“is $100B+ 2027 AI revenue achievable if hyperscaler capex decelerates”): Amazon is accelerating, not decelerating, and every Trainium or GPU MW still needs switching. Does not name Tomahawk/Jericho or an XPU socket, so it does not move the five-customer XPU flywheel on its own.

**Splits** [[Theses/NVDA - Nvidia]] §Summary (ASIC risk: Trainium 30–40% better price-performance) and §Outstanding Questions (CUDA durability as ASICs mature; share 87%→75% vs 60% by 2028). Order-book side supports the demand/Jevons leg ([G-14]: AI pulling Graviton, storage, vector DBs, traditional compute). Mix side is adverse: two frontier labs putting *training-scale* multi-GW on Trainium, plus a merchant-Trainium exploration, is exactly the “are ASICs incremental or substitutional?” question. Kimball’s GTM caution is the offsetting hypothesis (layer-renter vs layer-owner under [[Lens - Value Layer Monopoly]] — AWS owns the AWS seat; merchant silicon is a different go-to-market layer NVDA already occupies).

**Splits** [[Theses/MRVL - Marvell Technology]] §Summary three-engine and Insight #5 / Conviction → CLOSE leg 3 (Trainium 4 exclusive to Alchip). Custom-silicon ARR >$25B confirms the AWS custom pool is large enough to fund FY28–FY29 custom guides; seat identity is the problem — T3 already went to Alchip, and this recap does not name Marvell, Alchip, or T4. Amazon warrant/Photonic Fabric (thesis Insight #2) is unmentioned. Concentration/seat-churn risk *rises* if the $25B+ custom book stays Trainium-primary and T4 stays off-Marvell.

**Challenges** multiple expansion across the AI-infra complex ([G-13]): same sell-the-guide regime as the Alphabet $195–205B raise. [G-4] frenzy / Mueller “gold rush” and [G-10] base rate (trillion-dollar AWS; few firms sustain >20% CAGR at this scale) are the disconfirming pair — agreement across demand lenses is the cue to hunt the payback miss, not to raise conviction. Related: [[Theses/AMD - Advanced Micro Devices]] only via Kimball’s training-lock comment.

## Source Excerpts
> "We will still not have enough capacity to meet all the demand we have in 2026. I believe this dynamic will also be true in 2027, too. In fact, the demand we already have for 2028 is striking."
> "The jump from roughly $200 billion to $220 billion this year primarily reflects higher memory costs rather than a broader construction push."
> "The increase wasn’t driven by building more data centers, but by the rising cost of equipping them, particularly high-bandwidth memory, which has become one of the most constrained and expensive components in AI infrastructure."
> "As we get a few years out and the revenue growth outpaces the incremental CapEx growth … the resulting revenue, free cash flow, and return on invested capital are very compelling."
> "Two of the frontier labs putting multi-year, multi-gigawatt commitments behind Trainium is about the strongest validation a piece of silicon can get."
> "Selling chips and racks means public roadmaps, field engineering, lifecycle support, system integration, and channel. Those are go-to-market motions other vendors have spent decades building."
