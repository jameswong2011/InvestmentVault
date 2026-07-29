---
date: 2026-07-12
tags: [research, synthesis, agentic-AI, enterprise-software, macro, semiconductors, sector/enterprise-workflow-ai]
status: active
sector: Enterprise Workflow AI & Automation
source: Synthesis of [[2026-07-11 Gating Thresholds for AI Adoption]] (Gemini Deep Research) + 100-agent adversarial web verification (Gartner, Census BTOS, Stanford HAI, Epoch AI, Menlo Ventures, Ramp, MAS/IMDA/EU primary documents, company filings)
---

# Enterprise AI Adoption — Gating Factors Critique, 2030 Trajectory, Winners/Losers

## Thesis Delta

- **[[Theses/NOW - ServiceNow|NOW]] — strengthens the non-consensus bull.** ~50% of new ACV now from non-seat models (tokens/connectors/usage, CFO Apr 2026); Now Assist ACV $600M FY25 → ~$750M entering Q1 2026, FY26 AI ACV target raised $1B→$1.5B. The "SaaS Reset" bear assumes seat-monetization is trapped; NOW is the fastest converter to consumption pricing among incumbents. Gartner's $234B "agentic arbitrage" release (2026-07-01) explicitly frames the shift as "metamorphosis, not apocalypse" — spend redirects to orchestration layers, which is the CMDB-as-governance-substrate thesis.
- **[[Theses/NET - Cloudflare|NET]] — supports the pending high→medium downgrade.** Every measured adoption series says agentic traffic monetization is early: agents scaling ≤10% per business function (McKinsey), agent deployment "single digits across nearly all business functions" (Stanford HAI 2026). Act IV zero-disclosed-revenue is consistent with the adoption reality, not an execution anomaly — but the thesis's HIGH conviction was priced for nearer-term inflection.
- **[[Theses/PLTR - Palantir|PLTR]] — open question #120 falsification watch: no trigger.** Q1 2026 revenue +85%, US commercial +133%, NDR 150% (>120% threshold). The workforce-redesign gate (slowest to resolve) is PLTR's demand driver — forward-deployed process redesign is exactly what 60% of enterprises say they cannot do alone (Celonis).
- **Semis book ([[Theses/TSM - Taiwan Semiconductor|TSM]], [[Theses/NVDA - Nvidia|NVDA]], [[Theses/AVGO - Broadcom|AVGO]], [[Theses/000660 - SK Hynix|000660]], WFE) — demand signal intact, cycle-marker flagged.** Token volume compounding 5–7x/yr (Google 3.2 quadrillion/mo May 2026, +7x YoY; OpenRouter 5x in 6 months), HBM sold out through 2027, Anthropic rationing peak-hour usage on GPU scarcity. The single most important new cycle datapoint: hyperscaler capex is projected to exceed operating cash flow by Q3 2026 (Epoch AI) — the funding-constraint marker for [[AI Bubble Risk and Semiconductor Valuations]].
- **[[Theses/INTU - Intuit|INTU]] / [[Theses/CSU - Constellation Software|CSU]] — AI-extinction bear weakened at the margin.** The binding gate is organizational redesign (decade-scale), not model capability; vertical switching costs survive longer than the 2026 sell-offs priced.

## Summary

The Gemini report's architecture survives adversarial verification but its precision does not. Of ~25 load-bearing claims fact-checked against primary sources, the macro anchors are real (Gartner $2.59T/+47% 2026 AI spend, >40% agentic project cancellations by 2027, $234B SaaS "agentic arbitrage", MAST taxonomy, MAS SAFR, IMDA paper, EU PLD, CA AB 316, the labor statistics), but the enterprise-adoption statistics that carry its "structural stall" narrative are distorted or fabricated: "31% in production" misreads a Gartner wait-and-see poll bucket, "88% of agent pilots fail" mutates an IDC all-AI-POC stat, "80% of apps ship with agents" doubles Gartner's 40%, the industry pilot-to-production table traces only to an SEO aggregator, and its benchmark scores contradict published figures (claimed ~76.8% SWE-bench Verified vs Anthropic's published 93.9% for the same model family). The distortions share a direction: every one understates current adoption and capability. The report is directionally right that gates exist, and systematically too bearish about where the frontier actually is.

The deeper analytical error is the report's central claim that the gates are "structural, not cultural." Re-sorted by rate of resolution, its six gates split into two classes. Four are engineering/market problems that vendors are visibly industrializing — identity (Okta for AI Agents and Entra Agent ID both GA April 2026), token economics (fixed-capability inference prices falling 9–900x/yr, median 50x — the report's cost-escalation is a workload-mix choice, not a gate), runtime governance (MAS SAFR published as a deployable pattern within 12 months of the problem emerging), and multi-agent coordination (a design choice that stronger single agents keep deferring). These resolve on procurement cycles, 2027–2029. Two are diffusion problems only time resolves — legal precedent and workforce/process redesign — and both are organizational/institutional, i.e., precisely cultural. The report's own best evidence (Celonis: 60% cannot adapt operations fast enough; MIT NANDA's "learning gap"; McKinsey: two-thirds not yet scaling) describes the cultural gate. This is the electrification pattern: Paul David's dynamo lag — factories took ~30 years to reorganize around electric motors because the gain required redesigning the factory, not swapping the power source. The gate is real; it gates *depth*, not *direction* — and it is the reason adoption compounds for a decade rather than saturating in three years.

On that re-based foundation, the enterprise-adoption index (2026=100, value-weighted enterprise AI usage proxied by enterprise AI software+API+services spend) compounds to ~300–340 by 2030 in the probability-weighted case — annual growth decaying from ~45% (2027) to ~20–25% (2030), consistent with the cloud reference class one stage earlier on the S-curve, IDC's 31.9% CAGR, and the labs' own internal deceleration budgets. The measured-volume index (tokens/work-units) runs 3–7x/yr against this, with a 60–90%/yr price-deflation wedge between them. That wedge is the single most important variable for winners/losers: it transfers surplus from whoever monetizes dollars-per-human (seats, billable hours, placements) to whoever monetizes volume (compute, power, consumption-priced platforms) and to adopters themselves.

## Evidence

### 1. Verification scorecard — Gemini report claims vs primary sources

| Claim | Verdict | Primary-source reality |
|---|---|---|
| Gartner $2.59T AI spend 2026, +47% | **CONFIRMED** (3-0) | Gartner 2026-05-19 release; arithmetic checks; "2026 will be the inflection year" for enterprise spend is a forecast, not data |
| Gartner >40% agentic projects canceled by end-2027 | **CONFIRMED** (3-0) | 2025-06-25 release, still cited unrevised Jul 2026 |
| Agent software $206.5B, +139% YoY | **DISTORTED** | Not in the cited release (AI Software $453.2B +60%; AI Models $32.6B +110%); figure enters via secondary blogs |
| "31% of enterprises have agents in production" | **DISTORTED** | 31% is Gartner's *wait-and-see/unsure* poll bucket (Jan 2025, n=3,412). Real production readings run higher: LangChain 57% (Dec 2025), KPMG 42–54% (2025–Q1 2026) — self-selected samples, read as upper bounds |
| "88% of agent pilots fail to scale" | **DISTORTED** | IDC/Lenovo: 88% of *all AI* POCs fail to reach production — not agent-specific |
| "80% of enterprise apps ship with an agent (2026)" | **DISTORTED** | Gartner: 40% by end-2026, from <5% in 2025 — doubled |
| Industry pilot→production table (Banking 81/47 … Government 49/14) | **FABRICATED (source-laundered)** | Appears verbatim only on an SEO stats aggregator citing "Gartner/McKinsey/IDC/Forrester" with no direct sources |
| MIT 95% of GenAI pilots produce no P&L impact | **CONFIRMED, caveat-heavy** | MIT NANDA Aug 2025; non-peer-reviewed, derivation untraceable (Wharton demanded data release), 6-month P&L window, conflict of interest |
| UC Berkeley MAST taxonomy | **CONFIRMED structure / UNVERIFIED split** | Real NeurIPS 2025 paper (arXiv:2503.13657), 14 modes, 3 categories, 1,642 traces; the 44.2/39.1/16.7% split absent from abstract and project page |
| DigiCert "50% had agent-linked incident in 6 months" | **DISTORTED** | Real: 78% experienced AI-related incidents OR vulnerabilities (May 2026, n=1,001) — broader scope, no agent scoping, no time window. Directionally *worse* than claimed |
| MAS SAFR framework Jul 2026 | **CONFIRMED** | Real white paper v1.0, 2026-07-03 (BuildFin.ai); disposition engine, governance envelope, native/gateway patterns all real. Industry framework, not binding regulation |
| IMDA May 2026 liability paper | **CONFIRMED** | Real 36-page paper; product-liability/component-parts emphasis overstated |
| EU PLD software strict liability Dec 2026 | **CONFIRMED** | Directive 2024/2853; transposition deadline 2026-12-09 |
| CA AB 316 | **CONFIRMED** | Effective 2026-01-01; removes autonomy defense only, no strict liability |
| Anthropic 75% programming task coverage | **CONFIRMED** (occupation swap: 67% = data-entry keyers, not CSRs) | Anthropic labor-market research, 2026-03-05 |
| Net −16,000 US jobs/month | **CONFIRMED** | Goldman Sachs Apr 2026 (−25k substitution, +9k augmentation) |
| PwC 42% wage differential; 7x senior-skill demand in entry roles | **CONFIRMED** (context-specific) | PwC 2026 Jobs Barometer; "40% higher productivity" is PwC, misattributed to BCG |
| WEF 170M created / 92M displaced by 2030 | **CONFIRMED** | Future of Jobs 2025 |
| Gartner autonomy levels (3 listed) | **TRUNCATED** | Gartner 2026-05-26 defines four (drops "Act Autonomously") |
| Benchmark scores (SWE-bench Verified ~76.8% frontier) | **CONTRADICTED** | Anthropic's published SWE-bench Verified for the same model family: 93.9%. Report's WebArena/OSWorld figures match no published number |
| Token economics ($0.04→$1.20, 7.2x bills, FinOps 31→98%, $18.40/$2.31 routing study) | **UNVERIFIABLE** | None traced to a primary source in two verification passes |

**Meta-finding**: the confabulation pattern is not random. Genuine anchors are macro (Gartner, regulators, labor economists — institutions with indexed press releases); fabrications concentrate in enterprise-adoption micro-statistics, laundered through SEO stats aggregators that Gemini's retrieval treats as sources. And the distortions all point the same way — adoption understated, capability understated. Any conclusion inherited from this report starts with a bearish bias baked into its data layer.

### 2. Gating factors re-sorted by resolution speed

| Gate | Binding today? | Resolution mechanism | Evidence of rate | Non-binding by |
|---|---|---|---|---|
| Token economics | **No** (budgeting problem) | Price deflation + routing/caching markets | Fixed-capability inference price −9x to −900x/yr, median −50x, ~−200x post-2024 (Epoch AI); Gartner: >90% inference cost decline for 1T-param models by 2030 | Already, for fixed-capability workloads |
| Identity / execution architecture | Yes, in regulated deploys | Vendor products on procurement cycles | Okta for AI Agents GA 2026-04-30; Entra Agent ID GA Apr 2026; ~90% of orgs have begun agent-identity practices, ~half assigned identities to all agents (DigiCert May 2026) | 2027–28 |
| Runtime governance/security | **Yes** (78% AI incident/vulnerability rate) | Regulator-led templates + gateway products | Problem emerged 2025 → MAS SAFR deployable spec Jul 2026, 12-month lag; Gartner 4-level differentiated-governance framework May 2026 | 2027–29 in regulated verticals |
| Multi-agent coordination | Partially (a design choice) | Model capability + orchestration frameworks; single-agent scope expands with context/capability | MAST is real but measures 2024–25-era frameworks; failure modes are system-design, addressable in code | 2027–29, partially obviated by capability |
| Legal liability | Yes for external/high-stakes acts; **no for internal workflows** | Court precedent, statute — institutional clock | EU PLD Dec 2026 → litigation 2027+; AB 316 effective Jan 2026; precedent takes 5–10 yrs | 2030+ (externally-facing); never binding for coding/research/back-office where adoption is actually concentrated |
| Workforce / process redesign | **Yes — the binding gate** | Organizational learning; generational | Celonis: 60% can't adapt operations fast enough; McKinsey: 62% experimenting with agents but ≤10% scaling per function; Census: 57% of adopters use AI in ≤3 functions | ~2032+; the electrification/dynamo pattern (~30 yrs for factory redesign) is the reference class |

**Gates the report missed:**
1. **Supply-side compute/power — the binding 2026 gate the report never mentions.** HBM sold out through 2027 (SK Hynix, Micron); Anthropic rationing weekday peak usage on GPU scarcity (Mar 2026); transformer lead times 3–5 years; hyperscaler capex projected to cross above operating cash flow Q3 2026. A demand-side gating analysis in a supply-constrained market misidentifies the rate-limiter — the observable "deployment gap" partly reflects rationed inference, not just unready enterprises.
2. **Data/context readiness** — the [[Mental Models/Lens - Automation & AI Readiness|Automation & AI Readiness]] Lens A claim: firms that produce governed, machine-readable decision context as a byproduct of how they work automate successfully; the rest automate bad precedent. The report gestures at "shared business context" (45% stat) but treats it as a checklist item, not the organizational-design variable it is.
3. **Model capability trajectory as gate-dissolver.** The report holds capability constant and projects gates forward. If fixed-capability cost falls ~50x/yr and capability at fixed cost compounds similarly, the multi-agent, evaluation, and cost gates get partially bulldozed rather than resolved — the same error class as extrapolating early-adopter growth as saturation behavior, inverted.

**Gates the report overweights:** token economics (deflation-blind — its entire chapter extrapolates a snapshot); public benchmarks (enterprises gate on their own evals, and its scores are wrong anyway); legal liability for the internal-workflow majority of current deployment.

### 3. Adoption trajectory 2026→2030 (index, 2026 = 100)

**Index definition**: value-weighted enterprise AI adoption, proxied by enterprise AI software + API + services spend (excluding hyperscaler capex). Volume (tokens/work-units) reported separately — the divergence is the analytical payload, not noise.

**Measured 2026 baseline (the report's missing foundation):** Census BTOS firm-level AI use 17–20% (32% employment-weighted; 50–60% for large firms in information/professional services/finance); Ramp: 54.2% of businesses pay for AI (Jun 2026), penetration curve flattening; org-level "use AI somewhere" 88% (McKinsey/HAI) — saturated and no longer informative; agents scaling per function ≤10%. Breadth is largely spent; depth is nearly all ahead.

| Year | Bear (30%) | Base (50%) | Bull (20%) | Base YoY | Anchors for the base path |
|---|---|---|---|---|---|
| 2026 | 100 | 100 | 100 | — | Gartner +47% total AI spend; Menlo enterprise genAI $11.5B→$37B (+220%) in 2025; enterprise still "tactical" per Gartner |
| 2027 | 135 | 145 | 160 | +45% | Gartner "inflection year" carry-through; agent-product ACV tripling at NOW/CRM; IDC AI CAGR 31.9% is the floor |
| 2028 | 155 | 197 | 248 | +36% | Gartner: 15% of work decisions autonomous, 33% of apps agentic (from <1% in 2024); cloud analog year-3 |
| 2029 | 174 | 256 | 360 | +30% | IDC agentic spend $1.3T = 26% of IT spend; deceleration per labs' own budgets (OpenAI 2.2x, Anthropic ≤4x internal 2026 plans) |
| 2030 | 209 | 320 | 486 | +25% | Cloud reference class: ~10pp step-down every 2–3 yrs from ~50%; Gartner $234B/20% of SaaS spend arbitraged |

**Probability-weighted 2030: ~305 (≈ 3x, ~32% CAGR), annual growth decaying ~45% → ~36% → ~30% → ~25%.**

- **Base (50%)**: decay path matches AWS post-$5B-scale (48/72/54/43/47% held ~5 years, then −10pp per 2–3 yrs) and sits between IDC (31.9% CAGR) and the Gartner 2026 print (+47%). The workforce-redesign gate is what *prevents* the bull path — depth per firm (≤3 functions today) grinds up on organizational clocks, not procurement clocks.
- **Bear (30%)**: Perez-frenzy correction — capex/cash-flow crossover Q3 2026 forces hyperscaler discipline, a funding shock compresses the 2027–28 prints to +15–20%, recovery by 2030. Even the bear doubles: measured penetration is too low, and unit-cost deflation keeps usage compounding straight through a spending pause (post-2000 dark-fiber pattern — the [[Mental Models/Generalist - Overview|G-4]] mechanism where crash-era infrastructure becomes the cheap substrate).
- **Bull (20%)**: capability compounding dissolves the engineering gates faster than organizations are expected to absorb; consumption-priced agents (Agentforce +205%, Now Assist >2x) let spend scale with work volume rather than headcount. Requires the supply gate (HBM/power) to clear by 2028 — currently the binding physical constraint.
- **The volume/dollar wedge**: tokens grew 5–7x/yr through mid-2026 (Google 480T→3.2 quadrillion/mo in 12 months; Microsoft Foundry +7x; OpenRouter 5x in 6 months) against dollar growth of 1.5–4x. If the wedge persists, 2030 work-volume runs 30–100x on a 3x dollar index. Consensus tracks the dollar index; the economic transformation tracks the volume index.

### 4. Winners and losers (relative, ranked by exposure mechanism)

**Winners — monetize volume, own an unavoidable layer, or sell the gate's resolution:**

| Tier | Names | Mechanism | Disclosed evidence |
|---|---|---|---|
| 1. Compute toll-collectors | [[Theses/TSM - Taiwan Semiconductor|TSM]], [[Theses/NVDA - Nvidia|NVDA]], [[Theses/AVGO - Broadcom|AVGO]], [[Theses/000660 - SK Hynix|000660]], WFE ([[Theses/AMAT - Applied Materials|AMAT]]/[[Theses/LRCX - Lam Research|LRCX]]/[[Theses/KLA - KLA Corporation|KLA]]/[[Theses/ASMI - ASM International|ASMI]]) | Token volume 5–7x/yr is a direct unit driver; deflation is absorbed by Moore/packaging economics, not vendor margin | NVDA DC rev +92% (Q1 FY27); AVGO AI semis ~$56B FY26 guided (~3x), FY27 >$100B; TSM +40.6% Q1, HPC 61% of sales; HBM sold out through 2027 |
| 2. Power & thermal | [[Theses/VRT - Vertiv Holdings|VRT]], [[Theses/VICR - Vicor Corporation|VICR]], Eaton, GE Vernova | Hardest supply gate = longest-duration backlog | VRT backlog >$15B (2x YoY); Eaton DC orders +240%; GEV ≥110GW turbine backlog+reservations by YE26 |
| 3. Consumption-converted platforms / context layer | [[Theses/PLTR - Palantir|PLTR]], [[Theses/NOW - ServiceNow|NOW]], Databricks (private), SNOW | Own execution-path context + already re-priced to consumption; sell the workforce-redesign gate's resolution | PLTR +85%, US comm +133%, NDR 150%; NOW ~50% of new ACV non-seat; Databricks $6.9B run-rate +80% accelerating; SNOW +34% accelerating |
| 4. Agent infrastructure (identity, observability) | Okta, CyberArk→PANW, [[Theses/CRWD - CrowdStrike Holdings|CRWD]], [[Theses/PANW - Palo Alto Networks|PANW]], DDOG | Every gate the Gemini report lists correctly = a product category; 78% AI incident rate is their demand curve | DDOG +32%, LLM-obs spans 3x QoQ, MCP calls 4x QoQ; CYBR ARR +23% citing agentic identities; Okta agent products GA but zero disclosed revenue yet — thesis is forward |
| 5. Foundation models w/ enterprise distribution | Anthropic (private; public proxies: AVGO custom-silicon chain, AMZN/GOOGL stakes) | Enterprise API share 40% vs OpenAI 27% (Menlo); first B2B adoption lead (Ramp Jun 2026: 41.0% vs 39.5%) | Run-rate $9B→~$30B in 4 months (press-reported, unfiled) |
| 6. AI-data-services BPO | TaskUs | Non-consensus: BPO bifurcates rather than dies — the AI-training/eval segment grows on the same trend that kills voice-seat BPO | TASK +19% FY25, AI Services +59%, 6 straight quarters >30% |

**Losers — monetize dollars-per-human or aggregate content agents disintermediate:**

| Tier | Names | Mechanism | Disclosed evidence |
|---|---|---|---|
| 1. Answer/content aggregators (precedent class — already dead) | Chegg, Stack Overflow | Agent answers substitute the product wholesale | CHGG revenue −48% (Q1 26); SO questions −78% YoY, at 2008 levels |
| 2. People-hour-priced services | HCL/TCS/Infosys/Wipro, Teleperformance, TTEC, Concentrix core | Clients demand AI productivity be passed through as price | HCL discloses "AI deflation" 3–5% revenue headwind — the single clearest datapoint in this class; TCS −3.1% CC; TEP −2.2% LFL; TTEC −3.2% and guiding lower |
| 3. White-collar staffing | Robert Half et al. | Entry-level task automation shrinks placement volume | RHI −7% (Q2 25), −3.8% (Q1 26); 10-K names AI as demand dampener; Stanford: −13% relative employment for 22–25-year-olds in exposed occupations |
| 4. Seat-priced SaaS, slow converters | WDAY (most exposed), HUBS, generic seat-CRM/HCM | $234B/20% of SaaS spend exposed to agentic arbitrage by 2030 (Gartner); WDAY doubly exposed — priced per human worker while agents shrink worker counts | WDAY FY27 guide cut to 12–13% (sell-off on "agentic AI fears"); HUBS ASRPC guided low-single-digit; CRM contested: Agentforce $1.2B ARR +205% is genuine counter-evidence against total-revenue +10% |
| 5. Application-layer wrappers | Thin agents-on-rented-models | [[Mental Models/Lens - Value Layer Monopoly|Value-layer]] overlay: cheap intelligence makes the app layer more contestable while concentrating infrastructure | Menlo: coding category consolidated to Claude-dominated in 18 months — model vendors eat their wrappers |

**Contested — the interesting mispricings:** CRM (fastest agent-ARR ramp of any incumbent inside a decelerating core — the market prices the core, the bull case is the mix), ACN (record $22.1B bookings *while* cutting 22k heads — a deliberate revenue-per-employee inflection, Lens-A operator case, not a melting-ice-cube), OKTA (owns the identity gate with zero monetization proof yet — cheapest option on Tier-4 if agent identity becomes a compliance requirement, per the Automation-lens up-weight trigger on regulatory hardening).

## Contradiction Check

- **The report's central thesis contradicts its own evidence**: it claims gates are "overwhelmingly structural, not cultural" while its strongest verified statistics (Celonis 60/76%, MIT learning-gap, McKinsey scaling gap) describe organizational adaptation failure — cultural by any definition. This synthesis inverts the ranking: the durable gates are the organizational/institutional ones.
- **The adoption-stall narrative contradicts measured usage**: tokens +5–7x/yr, enterprise genAI spend +220% (2025), agent-product ARR at incumbents +130–205% YoY. What stalls is *pilots-per-P&L-dollar* accounting; what compounds is usage. Both MIT-NANDA-style failure stats and explosive usage can be true — failure of the median pilot, concentration of value in the successful tail, exactly the power-law outcome distribution [[Mental Models/Generalist - Overview|[G-9]]] predicts.
- **Deflation cuts both ways for the semis book**: the same 50x/yr fixed-capability price decline that kills the token-economics gate is a latent risk to compute demand if model-efficiency gains ever outpace workload growth (DeepSeek-shock class). Current evidence says demand wins (HBM sold out, usage rationing), but this is the single falsifying-datapoint class to monitor for Tier-1 winners: **a quarter where disclosed token volume growth decelerates below ~2x/yr while efficiency gains continue would flip the semis demand thesis**.
- **Survey-frame contradiction**: Census (representative, all firms) says 18% adoption; McKinsey/HAI say 88%. Both true — different denominators (any-AI-anywhere vs firm-level business use). The Gemini report mixes frames freely; any adoption model must not.
- **Anthropic revenue figures are unfiled** ($30B run-rate is press-reported; OpenAI disputes gross-vs-net comparability, ~$8B delta). Winners-Tier-5 rests partly on Menlo survey + Ramp card data, which are methodologically independent and agree — but no audited number exists until an IPO filing.
- **Perez cross-check adversarial to the whole bull structure** [[Mental Models/Generalist - Overview|[G-4]]]: capex/cash-flow crossover Q3 2026, neocloud credit structures ([[Theses/CRWV - CoreWeave|CRWV]] $46B liabilities), and vendor-financed demand loops are frenzy-phase markers. If 2026–27 is late-installation, the correction hits infrastructure builders hardest while *lowering* the cost floor for deployment-phase adopters — the bear case for the index (2.1x) is simultaneously the bull case for 2028+ application-layer winners.

## Framework / Mental Model

Applied per the READING PROTOCOL in [[Mental Models/Generalist - Overview]] — hypotheses to test, not verdicts:

- **[G-4] Perez surge phases**: token-price deflation + volume explosion + capex-exceeding-cash-flow = installation→deployment transition mechanics. *Hypothesis*: 2026–27 sits late-installation; infrastructure over-build risk concentrates in levered builders (neoclouds), deployment surplus accrues 2028+ to consumption-priced platforms and adopters. *Falsifier*: enterprise depth metrics (functions per firm, agents-scaling-per-function) inflecting up **before** any capex correction would indicate synergy-phase entry without a crash.
- **[G-10] Base rates**: a 3x/4-year spend index requires the category to be a justified outlier; the cloud reference class (AWS held ~50% for 5 years post-scale) says it is — but the same base rates cap the bull case: no enterprise-technology category has sustained >45% dollar growth for 5+ years at $100B+ scale.
- **[G-3] Mean reversion vs trend**: volume (tokens) = trend continuation; dollar growth = decaying trend; per-seat SaaS pricing = mean-reverting toward consumption. Misclassifying which series a company monetizes is the expensive error.
- **[G-13] Expectations**: the market prices the dollar index (visible in WDAY/HUBS de-ratings and the NOW/PLTR 2026 sell-offs) but not the volume/dollar wedge. The re-rating variable for Tier-3 winners is the quarter consumption revenue becomes disclosable line-items.
- **[[Mental Models/Lens - Automation & AI Readiness|Automation & AI Readiness]]**: the workforce-redesign gate *is* Lens A at economy scale — the Gemini report unknowingly re-derives the lens's core claim (AI-readiness is organizational, not technical). Regulatory hardening (SAFR, EU PLD, AB 316) fires the lens's up-weight trigger: provenance-rich context becomes a compliance moat (NOW CMDB, PLTR ontology, agent-identity vendors).
- **[[Mental Models/Lens - Value Layer Monopoly|Value Layer Monopoly]]**: AI-era overlay confirmed by the data — infrastructure layers concentrating (TSM share, HBM oligopoly, hyperscaler backlogs doubling), application layer contestability rising (coding-category consolidation in 18 months, seat-pricing breakdown). The toll-collector test sorts the whole winners/losers table.
- **[[Mental Models/Industry - Semiconductors|Industry - Semiconductors]] #18 (cycle vs structure)**: decompose the 2026 AI demand print into structural (token volume, agent depth — early S-curve) and cyclical (capex financing, inventory of compute) components; the Q3 2026 cash-flow crossover is the cycle-phase marker to watch.

## Source Excerpts

- Gartner, 2026-07-01: "up to $234 billion of enterprise application spending exposed to agentic arbitrage between now and 2030… roughly 20% of enterprise application SaaS spending… [agents] break the link between user growth and revenue growth."
- Epoch AI (llm-inference-price-trends): "prices declining between 9x to 900x per year, with a median of 50x per year," rising to ~200x/yr on post-Jan-2024 data.
- HCL CEO (Apr 2026): AI-driven pricing "deflation" of 3–5% revenue headwind — the clearest disclosed AI price-passthrough in services.
- Celonis 2026 Process Optimization Report: 76% "getting by" with sub-optimal processes; 60% cannot adapt operations fast enough for AI ROI; 85% aspire to agentic enterprise within 3 years.
- Census BTOS (May 2026): 17–20% of US firms use AI; 32% employment-weighted; 57% of adopters use it in ≤3 functions.
