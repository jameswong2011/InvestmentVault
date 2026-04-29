---
date: 2026-04-24
tags: [research, AI-infrastructure, tokens, anthropic, memory, CPU, TSMC, semiconductors]
sector: GPU & AI Compute Accelerators
ticker: [NVDA, AMD, TSM, 000660, 285A]
source: https://www.youtube.com/watch?v=LF3aUIM57uw
source_type: video-transcript
propagated_to: [NVDA, AMD, TSM, 000660, 285A, SEMICAP]
---

# Dylan Patel (SemiAnalysis) on Token Supply and Demand — Invest Like the Best, Apr 2026

## Thesis Delta

Three specific supply-side data points in this interview re-price multiple vault theses simultaneously: **(1) GPU useful life has extended from <5 years to 7-8 years** (incumbent ASP stickiness; Hopper/A100 resigning at higher prices) — positive for [[Theses/NVDA - Nvidia]] installed-base durability. **(2) DRAM pricing will double/triple from current levels** because true incremental memory supply doesn't arrive until 2028 despite 2025 demand signal — directly validates [[Theses/000660 - SK Hynix]] 2026-2027 HBM supercycle and threatens Goldman's 25% oversupply scenario. **(3) TSMC capex trajectory implies $100B by 2028** (vs $57.4B 2026 January-baseline) — directly validates [[Theses/TSM - Taiwan Semiconductor]] Bull Case and [[Sectors/Semiconductor Capital Equipment]] complexity-driven supercycle framing. **(4) CPUs "completely sold out and demand skyrocketing"** — driven by RL environments and AI-generated-code deployment — strengthens [[Theses/AMD - Advanced Micro Devices]] Venice Dense positioning. Also introduces a novel framing — "phantom GDP" — for measuring AI-generated economic value orthogonal to GDP statistics.

## Summary

Patel's core thesis across the interview is that **AI infrastructure spending is rational because the gap between "what tokens can economically produce" and "what tokens cost to serve" is widening faster than supply can catch up** — and the bubble-risk framing that prices $650B of infrastructure capex against current revenue misses the compounding productivity delta. Anthropic is the canonical demand proxy: its revenue compressed from ~$9B to $35–40B to $40–45B ARR within the interview window, with gross margins inflecting from "30-something percent" (start of 2025, per leaked funding-round docs) to a ~72% floor by Q1 2026 assuming all incremental compute went to inference (actual likely higher because some compute went to R&D). SemiAnalysis's own internal spend on Claude Code compounded from $5M to $7M run-rate in one week — ~25% of their $25M annual salary expense — illustrating the "if you don't use more tokens you'll never escape the permanent underclass" dynamic. Release cadence compressed from 6 months (Claude 3 → 3.5) to 2 months (Opus 4.7 → Mythos), with Mythos representing "the biggest step up in model capabilities in like 2 years" (an internal L4 → L6 engineer benchmark), selectively released only to large-capital customers at 5–10x Opus 4.7 token pricing.

On the supply side, Patel walks through four constraints that collectively rationalize doubling/tripling of memory pricing and 75%+ growth in TSMC capex through 2028. **(1) GPU useful life is extending from a prior assumption of <5 years to 7–8 years** — Hopper and A100 clusters are resigning for another 3–4 years at higher rents, with cluster-resign gross margin "beyond 35%." **(2) DRAM/HBM supply growth is structurally capped** at low double-digit % annually with NAND growth lower; true incremental memory capacity "doesn't come till '28 at best," so 2026 DRAM pricing "will double or triple from here" because the only way to steal capacity from commodity DRAM in a capitalist economy is demand destruction via higher pricing. **(3) TSMC capex is trajectoried to ~$100B by 2028** (vs $57.4B January 2026 baseline) — Patel characterizes TSMC's "good people" pricing discipline (single-digit price increases vs memory's triple-digit) as a moat durability signal and a hidden option on gross margin expansion beyond the 60–65% baseline. **(4) CPUs are "completely sold out and demand skyrocketing"** — attributed to RL environments running on CPUs and AI-generated code deploying on CPU infrastructure; copper foil, glass fiber PCB, lasers, and MKSI equipment all seeing the "tail whip" of prepayments.

Patel closes with two predictions and a framing concept. The framing is **"phantom GDP"**: as AI replaces labor tasks, output can rise while measured GDP theoretically shrinks because cost compression outweighs volume growth (a bank economist built a BLS 2,000-task AI-feasibility rubric using Claude, finding ~3% of tasks doable by AI today — directly deflationary if replaced). The first prediction is that if "46 Opus tier" spreads linearly through the economy, aggregate 2026 AI spend reaches $400B; exponential requires better models. The second prediction is near-term political: **large-scale protests against Anthropic and OpenAI within ~3 months (by July 2026)**, attributed to AI's popularity lagging ICE and politicians per Pew polling, physical attacks on Sam Altman's house (Molotov cocktails twice), and uncharismatic CEO communication amplifying diffuse economic anxiety. Actual contracted capex is 2+ years forward, so the financial impact would run through multiple compression rather than earnings.

## Framework / Mental Model

**Name**: "Phantom GDP" — a measurement-of-economic-value framing orthogonal to traditional GDP accounting.

**Components**:

1. **The pricing-power vs volume asymmetry** — GDP measures nominal output (price × volume). When AI dramatically reduces the cost of producing a task, the volume of that task produced can increase while the nominal GDP contribution of that task decreases (because per-unit price fell more than per-unit volume grew).
2. **The task-replacement rubric** — Patel references a BLS 2,000-task rubric (built by a bank economist, Malcolm, using Claude) scoring what fraction of standard Bureau of Labor Statistics work tasks are AI-feasible today. Current estimate: ~3% of BLS tasks are AI-doable today, with the fraction rising as models improve.
3. **The deflationary transmission mechanism** — AI replaces a task → task output compresses by (say) 100–1000x in cost → user surplus rises → measured GDP for that task falls → but aggregate economic value created rises.

**How to apply**: When reasoning about AI's macroeconomic contribution, adjust traditional GDP-based framing by estimating (a) what % of measured economic activity is AI-substitutable, (b) what the cost-compression factor is for substituted tasks, and (c) what fraction of the saved cost is retained as consumer/enterprise surplus versus captured as producer margin. The framework explains why J.P. Morgan's $650B revenue-requirement threshold for AI infrastructure capex may understate the productivity gains — the productivity is real and compounding, but not visible in GDP statistics because the price compression outweighs volume expansion. The framework also explains why labor-market protests (Patel's 3-month prediction) can intensify during a period of rising aggregate output: measured worker income falls as tasks get automated, even as aggregate economic value created rises.

**Caveat**: Phantom GDP is a qualitative framing, not a quantitative measurement methodology. It sets up the conceptual space (where to look for AI value creation that doesn't show up in GDP) rather than providing a precise measurement tool.

## Evidence

### Demand-side (Anthropic as proxy)

| Metric | Value | Notes |
|---|---|---|
| Anthropic revenue trajectory | $9B → $35-40B → $40-45B ARR | Compressed growth from start-of-year to interview |
| Anthropic gross margins, start of 2025 | "30-something %" | Per leaked funding-round docs |
| Anthropic gross margins, Q1 2026 floor | **72%** | Assuming all incremental compute → inference |
| Anthropic gross margins (likely) | Higher than 72% | Some incremental compute went to R&D |
| SemiAnalysis Claude Code run-rate | $5M → $7M (one-week delta) | 25%+ of $25M salary expense |
| Opus 4.7 / Mythos release cadence | Opus 4.7 released day of interview; Mythos internally Feb 2026 | Release cadence compressed from 6mo to 2mo |
| Mythos capability jump | Internal L4 → L6 engineer benchmark in 2 months | "Biggest step up in model capabilities in like 2 years" |
| Mythos pricing (selective cyber release) | 5-10x Opus 4.7 token cost | Selectively released only to large-capital customers |
| GPT-4 cost compression | 1/600th via DeepSeek by 2025 | General pattern: capability tier cost falls 100-1000x |

### Supply-side

| Constraint | Data point | Implication |
|---|---|---|
| GPU useful life | Extending from <5 yr → 7-8 yr (estimated) | Hopper, A100 resigning 3-4yr clusters at higher prices; gross margin on cluster resign "beyond 35%" |
| DRAM capacity growth | Low double-digit % / year (20-30% DRAM, lower NAND) | True incremental supply "doesn't come till '28 at best" |
| DRAM pricing trajectory | "Will double or triple from here" | Capacity must be stolen from other DRAM via higher pricing (no rationing in capitalist economy) |
| HBM supply | Tight through 2026-2027 | SK Hynix/Samsung at wafer-share tradeoff with NAND |
| TSMC 2026 capex | $57.4B (Jan baseline); may up slightly | "They're good people... single-digit price increases" |
| TSMC 2028 capex (implied) | ~$100B | Directly from Dylan: "they may spend $100 billion on capex in 2028" |
| ASML status | "Completely sold out" | Needs Carl Zeiss to expand faster |
| CPU supply | "Completely sold out and demand is skyrocketing" | Driven by (1) RL environments running on CPUs, (2) AI-generated-code deployment on CPU infrastructure |
| Copper foil, glass fiber PCB, lasers, MKSI | "Tail whip" — prepayments increasing | Return on invested capital up even where gross margin isn't |

### Model release cadence implications

- Mythos "materially larger model than prior models" — proof scaling laws still work
- Compute-efficiency wins compound alongside raw scaling: every 6-month capability tier delivers cost reduction
- Anthropic compute-constrained (cannot serve all demand); OpenAI less constrained (raised money for Oracle, CoreWeave, SoftBank, Microsoft, Tranium from Amazon)
- If 46 Opus tier spreads linearly → $400B economy spend in 2026; exponential requires better models

### "Phantom GDP" framing

> Malcolm (bank economist) built BLS 2,000-task AI-feasibility rubric using Claude: ~3% of BLS tasks doable by AI today. The deflationary economic value from AI replacing these tasks "you know output can go up but because cost falls so much actually GDP theoretically shrinks" — Dylan coins "phantom GDP" for output that doesn't show up in GDP statistics because price compression outweighs volume growth.

### Three-month forward prediction

- Dylan predicts **"large scale protests against Anthropic and OpenAI"** in 3 months (by ~July 2026).
- Attributes to: AI less popular than ICE/politicians per Pew; Sam Altman Molotov cocktail thrown in his house twice; blaming AI for deep-seated economic issues; uncharismatic CEO communication.

## Contradiction Check

**Strongly supports [[Theses/NVDA - Nvidia]] Bull Case**: Hopper/A100 re-signs with extending useful life = higher realized lifetime ASP per GPU than NVDA's models assume; gross margin expansion "beyond 35%" at cloud layer feeds back to NVDA pricing power. Also: Jevons paradox plays out — capability-tier-cost falls 100-1000x *and* tokenspend explodes alongside because new use cases keep opening.

**Strongly supports [[Theses/TSM - Taiwan Semiconductor]] Bull Case**: "$100B capex in 2028" directly validates the pricing-rents-compound thesis. TSMC "good people" pricing discipline (single-digit increases vs memory's triple-digit) is a moat durability signal — they're not extracting all available rents, preserving customer relationships — but **also signals they could extract more**. This is a hidden option on gross margin expansion beyond 60-65% baseline.

**Strongly supports [[Sectors/Semiconductor Capital Equipment]]**: "The tail whip just gets whipped harder and harder" — every component upstream of TSMC ($100B capex) is getting prepayments and capacity reservations. Directly validates SEMICAP Bull Case across LRCX, AMAT, KLAC, ASML, ASMI, BESI, TEL. ASML "completely sold out and needs Carl Zeiss to expand faster" extends timeline of constraint.

**Mixed signal on [[Theses/000660 - SK Hynix]]**: Bull — DRAM doubling/tripling = revenue upside on $30B 2026 HBM estimate that Goldman's oversupply scenario (25% oversupply, 10-15% decline) would invalidate. Bear — Dylan's "stealing capacity from somewhere else via demand destruction via higher pricing" logic implies commodity DRAM customers get rationed; SK Hynix's 40% commodity-DRAM revenue segment sees price gains but volume risk if downstream demand destruction hits (e.g., mobile, consumer). Net conviction: slightly stronger on HBM, unchanged on commodity mix.

**Supports [[Theses/285A - Kioxia]]**: NAND supply growth < DRAM (already lower double-digit), reinforcing supply-deficit durability through 2027+. Kioxia's die-supply model positions well for this.

**Strongly supports [[Theses/AMD - Advanced Micro Devices]]**: "CPUs completely sold out, demand skyrocketing" with specific attribution to RL environments and AI code deployment = direct validation of EPYC Bull Case + Venice Dense action-workload demand. Cross-references [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]] Venice Dense 5/5 action score.

**Introduces new risk for all AI-exposed theses**: Dylan's 3-month protest prediction (July 2026) is a political/regulatory tail not currently in any vault thesis Risks section. If protests materialize, hyperscaler capex sentiment could re-price — though actual capex is contractually committed 2+ years forward, so protest impact is likely multiple-compression (valuation) not earnings.

**Challenges [[AI Bubble Risk and Semiconductor Valuations]]**: Dylan frames the gap between "what model labs can serve" vs "what economic value tokens can generate" as growing — implying margin expansion at model labs and infrastructure is structurally protected from the J.P. Morgan $650B revenue-requirement threshold, because token-value-to-cost ratio keeps expanding faster than token supply. Partially invalidates the bubble framing by arguing the productivity-gains half of the ledger is accelerating.

**Alignment with [[Research/2026-04-23 - NVDA - Stress Test]]**: This interview provides bull-case counter-ammunition to the stress test's 6/10 🔴 assumptions — specifically the Jevons vs compound efficiency debate (token demand keeps growing faster than efficiency gains per Dylan's framing). Does not resolve Taiwan tail or ASIC share erosion 🔴 assumptions.

## Source Excerpts

> "last year we thought we were heavy users of AI... this year the spend has just skyrocketed... we're spending $7 million a year now on cloud code at the current rate um versus our salary expense being in the neighborhood of $25 million so you know we're north of 25% of spend on cloud code as a percentage of salary"

> "their margins are at a floor of 72% in reality some of that incremental compute they've got probably went to research and development it may be higher than 72% gross margins... at the start of the year... some of their funding round docs someone leaked it 30 something% gross margins"

> "if you don't use more tokens you'll never escape the permanent underclass"

> "there are people who have argued GPU's full lives are less than 5 years complete nonsense Um there are clusters now resigning three or foury old hopper clusters resigning for 3 or four more years um there's A100 clusters that are resigning for another couple years"

> "DM will double or triple from here still because that's that's how much capacity is required... the only way to steal capacity from somewhere else in a in a capitalist economy is demand destruction via higher pricing"

> "3 years from now TSMC is going to spend hundred billion on capex u maybe two years from now right maybe 28 sincerely they may spend $100 billion on capex in 2028 and people like just can't fathom that"

> "CPUs are completely sold out and demand is skyrocketing there... one is when you're doing reinforcement learning um the CPU is very critical to that... then once you have these great models and you're deploying them those models are generating code they're generating useful output... runs on CPUs"

> "I think there will be a large scale protest against anthropic and open AI"

## Related

- [[Theses/NVDA - Nvidia]] — useful-life extension, Jevons paradox play-out, token-value gap growing
- [[Theses/TSM - Taiwan Semiconductor]] — $100B 2028 capex directly validates Bull Case; "good people" pricing discipline is hidden option value
- [[Sectors/Semiconductor Capital Equipment]] — ASML sold out, tail-whip prepayments, TSMC capex doubling
- [[Theses/AMD - Advanced Micro Devices]] — CPU sold-out thesis directly validates Venice Dense positioning
- [[Theses/000660 - SK Hynix]] — DRAM 2-3x pricing trajectory supports HBM thesis; partial bear on commodity mix
- [[Theses/285A - Kioxia]] — NAND supply deficit durability through 2027+
- [[Compute & AI Compute Accelerators]] — token supply/demand imbalance driving sector
- [[Sectors/DRAM & HBM Memory]] — memory pricing trajectory
- [[Sectors/NAND Memory & Storage]] — supply growth differential
- [[Sectors/Semiconductor Foundries]] — TSMC capex trajectory
- [[Sectors/Semiconductor Capital Equipment]] — equipment supply-chain tail-whip
- [[AI Bubble Risk and Semiconductor Valuations]] — partial challenge; token-value-to-cost gap growing faster than infrastructure supply
- [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]] — complementary on CPU demand architecture
- [[Research/2026-04-23 - NVDA - Stress Test]] — bull-case counter-ammunition on Jevons/efficiency debate (does not resolve Taiwan/ASIC 🔴 assumptions)
