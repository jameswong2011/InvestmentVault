---
publish: false
date: 2026-07-29
tags: [macro, technology, ai-capex, hyperscalers, datacenter, semiconductors, automation]
status: active
sector: Cross-sector — AI Infrastructure
source: Internal synthesis — FMP financials + multi-agent web research compiled 2026-07-28/29
---

# Sustainability of AI Capex

## Summary

The AI buildout is running at ~$850–900B of ecosystem capex in 2026 against ~$150–180B of annualized *end-demand* revenue — a 5–6x coverage gap that must compress toward 2–2.5x by 2029 for current equity multiples to survive. The conclusion of this note: **the capex is not one cycle but four tranches with different funding durability**, and only the credit-funded ~30–35% of it is cyclically fragile. Base case (55%): capex grows to ~$1.0–1.1T in 2027, then enters a **2028–29 growth digestion** (+5–15% decelerating to flat/down) as the depreciation wall hits P&Ls and the lab-funding chain tightens — a growth recession concentrated in merchant/lab-committed capacity, not a telecom-2001 collapse, because 65–70% of spend is internally cash-funded by firms defending core franchises. Demand-side, the two engines are asymmetric: **corporate automation demand is deep but rate-limited by organizational readiness** (binding to ~2032; 5-yr apps/agents TAM ~$250–400B), while **consumer/prosumer demand is fast but shallow** (price ceilings + churn; 5-yr TAM ~$85–135B) — together supporting ~$850B end-demand by 2030, enough to underwrite a plateau near $1.2–1.5T capex by 2031, not enough to underwrite the uninterrupted consensus glide path ($1.4T by 2028). The 2028 hyperscaler guidance cycle (Jan–Feb 2027 prints) is the single most important dated catalyst.

## 1. The Ledger — Capex vs. End-Demand, De-Circularized

### 1.1 Capex actuals and guidance

Cash capex from cash-flow statements (FMP, fiscal years; MSFT June-FY, ORCL May-FY), guidance from company disclosures:

| $B | FY2022 | FY2023 | FY2024 | FY2025 | 2026 guide/run-rate |
|---|---|---|---|---|---|
| Microsoft | 24 | 28 | 44 | 65 | ~190 planned CY26 (CNBC Feb-26) |
| Alphabet | 31 | 32 | 53 | 91 | 180–190 → ~200 (Jul-26); H1'26 actual **$80.6B** |
| Amazon | 64 | 53 | 83 | 132 | ~200; Q1'26 actual $44.2B |
| Meta | 31 | 27 | 37 | 70 | 125–145 incl. leases (raised Q1'26, "component pricing") |
| Oracle | 5 | 9 | 7 | 21 → **56 (FY26)** | FY27: ~$70B net / $90–95B gross incl. $20–25B customer prepays |
| **Big-4 subtotal** | **150** | **140** | **217** | **358** | **~700–735** |

Add Oracle (~$70–90B), CoreWeave ($31–35B guided), Nebius, xAI, sovereign builds (Stargate UAE 1GW, Saudi) and lab self-builds → **2026 ecosystem total ~$850–900B**, roughly 2x 2025. Forward consensus: Big-Tech >$1T in 2027 (CNBC Apr-26); Morgan Stanley five majors $1.2T 2027 / $1.4T 2028; Citi GOOGL+META+AMZN $801B 2027; JPMorgan $5.5T global through 2030; McKinsey $6.7T DC capex by 2030 ($5.2T AI-specific, 125GW); Goldman ~$7.6T 2026–2031.

Two structural markers fire this year:
- **Funding crossover**: Epoch AI projects hyperscaler capex exceeds operating cash flow from **Q3 2026**. FMP confirms the approach: GOOGL Q2'26 capex $44.9B vs OCF $39.1B — *already crossed at the quarterly level*; Oracle FY26 FCF **−$24B**; Meta ran zero buybacks in Q1'26 with FCF down to $12.4B. Marginal capex is now debt/SPV/prepay-funded. The date matters because of the reference class ([[Mental Models/Generalist - Overview|G-10]]): every >30%-CAGR capex boom sustained ≥3 years — railways 1840s, electrification 1920s, telecom 1996–2001, shale 2010–14 — drew down ≥25% within ~2 years of the marginal dollar shifting from cash flow to credit. That shift now has a date: this quarter.
- **Vendor-financing loop**: OpenAI's announced commitment stack totals ~**$1.4T** — Broadcom $350B, Oracle $300B, Microsoft $250B, Nvidia $100B (LOI, progressive), AMD $90B + warrants, AWS $38B, CoreWeave $22.4B — against ~$25B annualized revenue (Q1'26 $5.7B) and projected 2027 burn of ~$63B. Suppliers are financing their customer's purchases (Nvidia equity → OpenAI → Oracle/CoreWeave orders → Nvidia revenue). Lucent-1999 structure at 30x the scale, concentrated in one counterparty.

### 1.2 End-demand, counted once

Most published tallies double-count: a dollar of Anthropic API revenue reappears as Google/AWS cloud revenue (labs' compute costs), then again as Nvidia revenue (cloud's capex). Counting **only end-buyer dollars** (what consumers, enterprises, and governments pay for AI functionality), mid-2026 annualized:

| End-demand bucket | Run-rate ($B) | Anchors |
|---|---|---|
| Consumer/prosumer subscriptions + app spend | 25–35 | ChatGPT 50M paid subs (10M Plus = $2.4B ARR; mix shifting to $8 Go tier); Anthropic consumer 10–15% of mix; Sensor Tower mobile AI IAP >$4B H1'26; Google One AI, Grok, Perplexity ($450M ARR) |
| Coding/agent tools (net of model-lab double-count) | 8–12 | Cursor ~$4B [AGG], Copilot 4.7M paid subs, Cognition ~$0.5B, Lovable $0.5B, Replit ~$0.5B, v0/Bolt/Base44 |
| Enterprise API + AI software attach | 85–110 | Anthropic $10.9B Q2'26 (≈$44B annualized, 70–80% API; first operating profit $559M); OpenAI business/API share of ~$25–30B; Microsoft AI ($13B run-rate Jan-25, +175%); Agentforce $1.2B; Now Assist; PLTR ~$6B; Harvey $300M; Menlo enterprise genAI $11.5B→$37B in 2025 |
| Government/sovereign services (ex-infrastructure purchases) | 3–6 | DoD $200M-class awards ×3–4; GSA OneGov; UAE nationwide ChatGPT |
| **Total priced end-demand** | **~150–180** | growing >100% y/y (2025 exit ~$60–80B) |

**Coverage ratio: ~0.18–0.2x** (end-demand / same-year capex). Steady-state cloud economics run capex at 35–45% of revenue → sustaining $850B/yr requires a **$2.0–2.5T revenue pool** — independently consistent with Sequoia/Cahn's arithmetic ($1.5T of 2026 AI spend needs ~$3T revenue). Allianz: capex-vs-revenue divergence ~46%, already above the 32% of telecom-2001.

Why does usage explode while revenue lags? The Jevons mechanism ([[Mental Models/Generalist - Overview|G-14]]) is operating on volumes exactly as it should — token prices fall −9x to −900x/yr for fixed capability (median −50x, Epoch AI) and volumes compound +5–7x/yr as previously-uneconomic workloads cross the threshold — but Jevons creates *demand*, not *capture*. Only consumption-priced surfaces (API, usage-billed agents, ads) convert the volume into revenue; flat-rate subscriptions and free tiers leak it to users as surplus. The sustainability question is therefore not "is demand real" (it is) but "how much of it gets a price" — a capture question, which is what the rest of this note decomposes.

## 2. ROIC of the Datacenter Buildout, 2023–2026

### 2.1 Measured aggregate ROIC is below WACC — but the aggregate is the wrong unit

AI-incremental invested capital: actual big-4 capex above the pre-AI trend (2022 base $150B, +12%/yr counterfactual) sums to ~$630B for 2024–2026E; adding Oracle's above-trend $70B, neoclouds ~$60B, and lab/sovereign self-builds → **~$1.0–1.2T cumulative AI-incremental capital by end-2026**. Attributable operating profit today: labs in aggregate ≈ breakeven (Anthropic +$559M/qtr against OpenAI −$14–27B/yr), hyperscaler AI gross profit on ~$100–120B of AI cloud/software at 50–60% GM less allocated opex ≈ $50–70B EBIT-equivalent. **Aggregate pre-tax ROIC ≈ 5–7% against an 8–10% WACC — value-destructive on a spot basis, before the depreciation wave has even fully landed.**

But return on *incremental* capital is a forward question, not a measurement ([[Mental Models/Generalist - Overview|G-7]]): the historical number tells you what happened; where the *next* dollar sits in the stack tells you what it will earn. Segmenting the invested dollar by capture position — does it buy a layer everything above must pay to traverse, or contestable capacity ([[Mental Models/Lens - Value Layer Monopoly]]) — the dispersion is the finding, not the average:

| Layer | Spot economics | Evidence |
|---|---|---|
| Silicon toll (NVDA, TSM, HBM) | 35–60%+ ROIC | NVDA FY26 revenue $216B; TSM GM 67.7% (Q2'26); deliberate under-pricing leaves ~40% headroom unexercised ([[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]]) |
| Frontier model capture | Inflecting positive | Anthropic inference GM 38%→>70%, first op profit Q2'26 — first proof the token layer can price above cost at scale |
| Merchant GPU rental | Mid-teens IRR gross; negative equity FCF levered | SemiAnalysis floor $4.92/hr VR NVL72 at 15.6% IRR; CRWV interest = 25.8% of revenue, FCF −$4.7B/qtr |
| Integrated hyperscaler AI cloud | Accretive but undisclosed | "AI margin accretive" CFO commentary; utilization sold out; H100 rentals +40% off Oct-25 bottom |
| Internal-use (ads, feeds, search defense) | Unmeasurable, strategically mandatory | The capex is priced as franchise defense, not project ROI — its return is the avoided decay of a monopoly cash flow |

**The honest ROIC statement**: the buildout destroys value in aggregate *today* while chokepoint layers earn monopoly returns and the loss concentrates in the leveraged middle (merchant capacity) and the lab layer's burn. The mine worth owning is the toll booth, not the pit. This is the telecom-2000 distribution (equipment and users won; capacity owners lost) — with one structural difference: the four largest capacity owners also own the application and advertising layers that consume the capacity, which telecom carriers never did.

### 2.2 The depreciation wall, quantified

Big-4 D&A is running ~$42B/quarter (~$170B/yr) and compounding 30–40% y/y (GOOGL quarterly D&A +42% y/y; AMZN +32%). The 2025–26 capex cohort (~$1.09T big-4) at a blended ~13%/yr depreciation rate (≈60% IT at 5–6yr + 40% shells/power at 15–25yr) adds ~**$140B/yr of incremental D&A** as it enters service → big-4 D&A ≈ **$260–300B by 2028**. Neutralizing that step-up at 50% incremental margins requires ~**$300–360B of incremental AI revenue by 2028** — the EPS-compression test that makes 2028 the reckoning year regardless of narrative.

On Burry (Nov-25: $176B cumulative 2026–28 understatement via life extensions; Oracle earnings overstated 26.9%, Meta 20.8% by 2028): the *direction* is right but the *magnitude* is second-order. Useful-life extensions (MSFT 4→6yr FY23, GOOGL →6yr 2023, META →5.5yr 2025, ORCL →6yr FY25) shift perhaps $40–60B/yr of D&A rightward — real earnings flattery, but one-third the size of the cohort wave itself. The stronger rebuttal is empirical: 4-year-old H100s rent at $2.29–3.12/hr median, **up ~40% since Oct-25**, with $12–22K resale values — old silicon is monetizing, and Amazon *shortened* AI-server lives to 5yr (Jan-25, −$700M FY25 op income), the opposite of flattery. Verdict: depreciation schedules are defensible **while demand exceeds supply**; they become fraud-shaped retroactively only if utilization breaks. Watch rental prices, not accounting policies.

### 2.3 The J-curve defense and its boundary

Cloud 2015–2019 is the bull precedent: capex looked reckless, ROIC arrived late and enormous. Two disanalogies bound it: (1) cloud assets were long-lived and obsolescence-free; AI accelerators face generational cannibalization (GB300→VR NVL72 = 3.5x FP8 TCO improvement — each generation reprices the installed base); (2) cloud demand was *migration* of existing, budgeted enterprise workloads; AI end-demand must be *created* against organizational frictions (§5). And against the single flattering precedent stands the wider base rate from §1.1: capex booms that outrun cash funding correct. The cloud analogy earns its keep only for the tranches that stay cash-funded and franchise-linked; applied to lab-committed and levered-merchant capex, it is doing unlicensed work.

## 3. Demand Segmentation — Two Engines, Opposite Shapes

| | Corporate/government process automation | Consumer/prosumer DIY & vibecoding |
|---|---|---|
| Depth (ceiling) | Very deep — $15T+ knowledge-work wage pool adjacent | Shallow — competes in household $10–30/mo utility/entertainment budget |
| Speed (rate limiter) | Slow — organizational redesign, ~2032 horizon | Fast — viral adoption, weeks |
| Pricing power | Emerging at capture layers (consumption-priced platforms, frontier API) | None at chat layer; real only in income-generating prosumer tail |
| Revenue durability | High once embedded (switching costs, audit trails) | Low — AI-app churn 36% faster than non-AI subs (RevenueCat 2026) |
| 2026 run-rate | ~$90–120B | ~$40–50B |
| 2031 TAM (this note) | **$250–400B** apps/agents (+ infra serving it) | **$85–135B** all-in |

The capex cycle's sustainability question is a *race*: corporate depth must arrive before consumer shallowness, lab burn, and credit markets exhaust the bridge financing. That race — not any single TAM — is what the 2027–29 scenarios in §6 price.

## 4. Consumer / Prosumer — Pricing Power, Segmentation, and a 5-Year TAM

### 4.1 The pricing evidence runs downward, not upward

- **The $20 anchor is deflating in real terms and being undercut nominally.** Three years of nominal $20 stability = real price decline; 2026 brought ChatGPT **Go at $8** (global Jan-26, "fastest-growing plan") plus **ads testing on Free/Go**, and Gemini Ultra **cut $250→$100** at I/O-26. Price discrimination is being exercised *down-market* — the tell that the marginal subscriber's willingness-to-pay sits below $20, not above.
- **Conversion is a hard ceiling, not a funnel stage.** Free→paid 5–6% at OpenAI (50M paid / 900M WAU); ~3% of US households pay anything (BofA Feb-26, median $20); only 9% of payers hold >1 AI subscription (a16z). Stanford's WTP distribution is the structural datapoint: mean $124.50 but **median $11.40** — the value is real and the *median consumer knows the free tier delivers most of it*.
- **Churn is the second ceiling.** AI apps retain 21.1% at 12 months vs 30.7% non-AI; +41% revenue-per-user but 36% faster churn (RevenueCat, 115K apps). 53% of payers cancel-and-restart as needed. Consumer AI revenue behaves like mobile gaming, not like SaaS.
- **The $200 tier is a professional-income segment, not a consumer segment.** ChatGPT Pro ~500K subs ≈ 1% of payers [AGG]; Cursor Ultra / Claude Max 20x / SuperGrok Heavy price against income generated, and hold only there. The tier proves segmentation works — and simultaneously proves how thin the inelastic layer is.

### 4.2 Vibecoding: the tool monetizes; the output mostly doesn't

The tools are a real, violent growth market: Cursor $100M→~$4B ARR in 18 months [AGG; SpaceX all-stock acquisition at $60B announced Jun-26], Lovable $0→$500M in ~20 months, Replit ~$525M annualized, Base44 profitable solo-built and exited $80M+$90M earnouts, Copilot 4.7M paid. But the **monetization of the *output*** — the variable that determines whether tool pricing can scale like Shopify take-rates rather than cap at hobby budgets — fails almost every test available:

- No platform (Lovable/Replit/Bolt) discloses deploy/custom-domain/payments-attach rates — a uniform silence that is itself evidence.
- Abandonment: high-"vibe-score" GitHub projects 3.2x more likely abandoned within 18 months; Lovable creates 100K projects/day against ~zero disclosed commercial survivors at scale.
- Quality debt caps commercial life: 45% of AI-generated code carries OWASP flaws (Veracode); 5,600 scanned vibe-coded apps → 2,000+ vulnerabilities (Escape, Oct-25); Tea/Base44/Lovable-RLS incidents; a paid "rescue engineering" industry now exists (~$50–500K per rescue).
- The freelance market shows where output value goes: Upwork generic-genAI execution contracts +90% volume, **−13% per-contract earnings**; Fiverr lost ~14% of buyers and guides 2026 revenue −12% to +1%. AI is *deflating* the price of exactly the deliverables (logos, sites, simple apps) that DIY creators would sell. Stripe confirms the power law: solo founders at record share (63% of Atlas C-corps) but **median first-6-month revenue −23%** while the top decile grows +19% and the top-decile/median gap widened 34x→61x.

**Implication**: mass-market vibecoding is a *consumption* activity (creation-as-entertainment/aspiration) whose WTP anchors to hobby budgets ($8–25/mo, high churn), while a thin professional tail (income-generating devs, agencies, funded founders) sustains $200–500/mo + usage. Tool vendors are squeezed between the two: Cursor ran ~−30% gross margins pre-repricing and remains loss-making on individual subs; the Jun-25 usage-repricing backlash showed the mass tier will not absorb model costs. Resolution: consolidation into model owners (Windsurf carve-up; coding category consolidated to Claude within 18 months per Menlo). This is the [[Mental Models/Lens - Value Layer Monopoly]] AI-overlay playing out in real time: cheap intelligence makes the application layer *more* contestable while concentrating the layer below it — the wrappers' economics leak downward to whoever owns the model and the compute.

### 4.3 Consumer/prosumer TAM, 2031

Build: ~2.5–3B AI WAU by 2031 × 6–8% blended conversion (OpenAI's own 2030 plan: 8.5% → 220M payers) × blended ARPU $12–15/mo (Go-tier-heavy mix, 2–3% at $100–200 tiers) ≈ **$35–55B chat/assistant subscriptions**; + prosumer creation tools (coding/design/video: Cursor-class, Canva $4B ARR base, Adobe/Figma AI attach) **$40–60B**; + app-store/companion/misc **$15–25B** → **total $85–135B/yr by 2031** (~2.2–2.7x the mid-2026 run-rate, 17–22% CAGR — the *slowest*-growing major AI segment, bounded by conversion ceilings, churn, and nominal price deflation).

**The reconciliation that matters for capex**: capped consumer *revenue* ≠ capped consumer *compute demand*. Free tiers, ads (ChatGPT ad tests), and $8 tiers monetize by volume; agentic features multiply tokens per user 10–100x. Consumer inference capex is therefore underwritten by **advertising economics, not subscription economics** — which only Google, Meta, and OpenAI-with-ads can do. This concentrates sustainable consumer-serving capex in the ad-platform owners and structurally starves merchant capacity of the consumer segment — one more force pushing the fragility into Tranches C/D.

## 5. Corporate / Government — Organizational Readiness as the Rate Limiter

### 5.1 The constraint stack (what actually gates the TAM)

The core claim of [[Mental Models/Lens - Automation & AI Readiness]] — AI-readiness is an organizational-design and cultural problem, not a technical one; firms automate successfully only when they already produce governed, machine-readable decision context as a byproduct of how work gets done — is the single best-fitting frame for the mid-2026 evidence (verified base: [[Research/2026-07-12 - Enterprise AI Adoption - Gating Factors Critique, 2030 Trajectory, Winners-Losers - synthesis]]):

| Constraint | State mid-2026 | Resolves by | Gate class |
|---|---|---|---|
| Workforce/process redesign | Celonis: 60% cannot adapt operations fast enough; agents scaling ≤10% per function; 57% of adopters use AI in ≤3 functions | **~2032+** (electrification/dynamo lag — the reference class is ~30yr factory redesign) | **Binding** |
| Data/context readiness | Decision context not machine-readable — the lens's §1 mechanism: agents without grounded context confabulate, so ungoverned firms *can't* deploy safely | Firm-by-firm; culture-dependent | Binding for depth |
| Runtime governance/security | 78% AI incident/vulnerability rate (DigiCert); MAS SAFR spec shipped within 12mo | 2027–29 regulated verticals | Resolving |
| Identity/audit plumbing | Okta for AI Agents + Entra Agent ID both GA Apr-26 | 2027–28 procurement cycles | Resolving |
| Model capability | tau2-bench telecom top scores now 98–99%; SWE-bench Pro ~69% — the 2024 "30% agent success" era is over | Continuously | **Dissolving** |
| Legal liability | EU PLD strict liability Dec-26; precedent 5–10yrs | 2030+ external acts; never binding for internal workflows | Slow, non-blocking for current deployment mix |
| Government procurement | 18-month median federal cycles vs FedRAMP 20x two-month AI fast lane (IBM: 11 authorizations in a year) | Structurally slow, now accelerating | Caps pace not direction |

Failure-rate statistics support the *depth* gate, not a demand ceiling: S&P Global's 42% abandonment (up from 17%) and the average 46% POC→production attrition describe the median pilot dying while usage compounds — token volume +5–7x/yr, enterprise genAI spend +220% in 2025, agent-product ARR at incumbents +130–205%. Power-law outcome distribution, not stall: value concentrates in the successful tail, and the circulating doom stats (MIT 95%, "88% agent pilots fail") are caveat-heavy or source-laundered on adversarial verification. The same lens cuts the other way too: its anti-signal test — narrative without disclosed unit economics scores zero — applies to the *sellers* of the buildout. Hyperscaler "accretive returns" commentary without unit disclosure remains narrative until the 2028 D&A test (§2.2) is passed.

### 5.2 Corporate/government TAM, 2031

The addressable-now pool is the *externalizable, measurable, digitized* slice of knowledge work — BPO (~$300B), IT services (~$1.5T), customer experience, back-office F&A, software development — not the $15T wage pool consensus TAMs gesture at. Applying the verified adoption trajectory (enterprise AI dollars ~3x 2026→2030 at ~32% CAGR, decaying 45%→25%, consistent with the cloud reference class one S-curve stage earlier) to a 2026 apps+API base of ~$90–120B, extended one year: **corporate AI software/agents/API revenue ~$250–400B by 2031**, plus government ~$20–40B (procurement-capped despite the FedRAMP acceleration; sovereign *infrastructure* deals are capex demand, not end-demand — they add supply, a subtlety most sovereign-AI bullishness ignores). Wage-pool cross-check: 5% automation of the pool at 30% software capture = $225B — consistent.

The binding variable is organizational redesign speed — a variable **no supplier controls and no capex accelerates**. This is the central asymmetry of the whole cycle: supply is being installed on financing clocks (quarters) against demand that matures on organizational clocks (decade). Regulatory hardening (EU PLD, SAFR, agent-identity GA) is converting provenance-rich context into a compliance moat — the readiness lens's explicit up-weight trigger — which favors execution-path incumbents ([[Theses/NOW - ServiceNow]], [[Theses/PLTR - Palantir]]) and consumption-converted platforms over seat-priced laggards. But it shifts *where* corporate dollars land more than it changes *when*.

## 6. The Capex Projection, 2027–2031

### 6.1 Triangulating three independent constraints

1. **Funding**: big-4 OCF ~$600B (2026) growing ~12–15%/yr → ~$780B by 2028. With buybacks minimized (Meta already at zero), self-fundable capex ≈ $600–650B/yr by 2028. Everything above rides debt/SPV/private credit (realistic appetite $200–300B/yr for IG-adjacent DC paper) and lab equity raises. **Funding ceiling 2028 ≈ $900B–1.0T** without stressing credit markets; consensus $1.4T assumes the credit channel doubles — that is, it assumes the post-crossover regime that historically precedes drawdowns (§1.1) instead *expands* for three consecutive years.
2. **Revenue coverage**: base-case end-demand path $150–180B (2026) → ~$285B (2027) → ~$450B (2028) → ~$640B (2029) → ~$850B (2030) (growth 80%→60%→45%→35%, faster than the enterprise index alone because Anthropic-class API compounding front-loads it). Market tolerance requires capex/end-demand to fall from 5.7x toward 2–2.5x by 2029–30 → tolerated capex ≈ $1.0–1.1T (2027), $1.1–1.2T (2028), $1.3–1.5T (2029–31). **Consensus 2028 ($1.4T) sits above the tolerance band — it prices zero demand disappointment.**
3. **Physical (power)**: US DC power 75.8GW (2026) → 134.4GW (2030) ≈ +15GW/yr; GEV turbine slots effectively sold out through 2030 (116GW backlog+reservations; ramp 20→30GW/yr); interconnect queues 5–13yrs. At all-in $45–55B/GW, deployable global capex ceiling ≈ **$1.5–2.0T/yr by 2028–29**. Power binds the *bull* case, not the base; and shells/power are already running ahead of silicon and monetization (CRWV has energized only ~29% of 3.5GW contracted power; NBIS ~5–6%) — capital is queuing at the wall, not producing revenue.

### 6.2 The tranche model — what corrects and what doesn't

| Tranche | ~Share of 2026 spend | Funding | Elasticity to disappointment |
|---|---|---|---|
| A. Core-franchise defense + internal use (ads, search, feeds, M365) | ~30–35% | OCF | Near-zero — priced as existential, cuts last |
| B. Merchant enterprise AI cloud (non-lab customers) | ~25% | OCF | Low-moderate — tracks enterprise adoption trajectory |
| C. Lab-serving capacity (Azure/OCI/GCP/AWS for OpenAI/Anthropic; neoclouds) | ~25–30% | Debt, SPVs, prepays, vendor financing | **High** — take-or-pay contracts against a counterparty (OpenAI) burning $27B→$63B/yr on $25–30B revenue |
| D. Lab/sovereign self-build (Stargate sites, xAI, Gulf) | ~10–15% | Narrative-priced equity + state capital | **Highest** — first to freeze when funding reprices |

The tranche split is the value-layer filter applied to a capital-allocation question: A and B sit behind moats (franchise cash flows, enterprise switching costs); C and D are capacity without a chokepoint — melting assets the moment scarcity clears. It is also where the surge-cycle diagnosis lands most precisely: the 2026 markers — vendor-financed demand loops, capex crossing above cash flow, narrative-priced equity funding the margin — are textbook late-installation/frenzy signatures ([[Mental Models/Generalist - Overview|G-4]]), *but they coexist with genuine deployment-phase signals* (Anthropic's operating profit; consumption-priced agent ARR compounding at incumbents). The working hypothesis: the frenzy and the deployment phase are running concurrently in different tranches — C/D are the frenzy, A/B are early deployment — so the "turning point" resolves as a tranche-selective pause rather than a systemic crash. Both directions carry named falsifiers in §8.

### 6.3 Scenarios

| | 2027 | 2028 | 2029 | 2030 | 2031 | Path logic |
|---|---|---|---|---|---|---|
| **Base (55%)** — *digestion, not crash* | $1.00–1.10T (+30–40%) | $1.10–1.25T (+5–15%) | $1.05–1.20T (flat to −8%) | $1.20–1.35T | $1.30–1.50T | Depreciation wall + 2028 EPS math force discipline; Tranche C/D growth stops, A/B grinds on; re-acceleration 2030 as corporate depth (§5) matures into the installed base |
| **Bear (25%)** — *credit event* | $0.95–1.05T | **$700–800B (−25–30%)** | $750–850B | $900B–1.0T | $1.0–1.1T | Trigger: OpenAI raise fails/down-round, or a CRWV-class refinancing breaks, or enterprise depth stalls; C cut 50–70%, D frozen; A/B held → even the bear's 2030 ≥ 2026 level. WFE/HBM downcycle 2028 with structurally higher trough floors (service annuities, qualification gates) |
| **Bull (20%)** — *power-bound boom* | $1.15–1.25T | $1.40–1.55T | $1.6–1.8T | ~$2T | $2T+ | Anthropic-style doubling persists 12+ months; agents cross the reliability threshold from suggestion to delegated execution at consumer and enterprise scale; coverage ratio compresses through growth alone; the binding constraint becomes GEV slots and interconnect queues, not money |

Probability-weighted 2031 ≈ **$1.3–1.4T/yr**, cumulative 2027–31 ≈ **$5.5–6.5T** — landing between JPM ($5.5T-through-2030) and McKinsey/Goldman ($6.7–7.6T), but with a *shape* consensus does not carry: a 2028–29 growth pause concentrated in merchant/lab-committed capacity. AI hardware read-through (base): NVDA+AVGO+AMD+memory+networking TAM ~$450–500B (2026) → ~$650–750B (2028) with a flat 2028–29; silicon share of capex mix falls as power/shells absorb spend; custom ASIC share rises (Broadcom-OpenAI 10GW). The fragility is *not* in the semis chokepoints — it is in the leveraged capacity layer between them and the demand. And the bear case carries its own second-order bull: post-correction, stranded C/D capacity becomes cheap substrate for the deployment layer — the post-2000 dark-fiber pattern, where the frenzy's overbuild funds the next decade's application winners at marginal cost.

### 6.4 What would change the projection

The single highest-information window: **hyperscaler CY2027 guidance, Jan–Feb 2027 prints**. First sub-20% capex growth guide from MSFT/GOOGL/META = digestion confirmed on schedule; uniform +30%+ guides = bull path, rotate toward power/WFE bottlenecks harder. One standing caveat sits under every scenario: the projection assumes no macro credit tightening. The AI capex cycle overlays the economic cycle, and a rate shock or credit-spread regime change pulls every scenario left by roughly a year — the base case's 2028 digestion becomes 2027, and the bear's financing triggers fire early.

## 7. Positioning Read-Through

Per the three-clocks framework in [[Website/2026-07-22 - How to Read the Semiconductor Cycle]] — economic, capital/inventory, and technology clocks running at different speeds:

- **Capital clock: late-frenzy.** Vendor financing loops, the capex/OCF crossover, and credit-funded marginal capacity date it. The 2028 digestion is the base case; position via chokepoints, not merchant capacity. The discipline that matters most here is *decomposition*: do not read the coming digestion as "AI demand was fake" (the structural component — token volume, agent depth — is early-S-curve and compounding), and do not read 2026's sell-outs as "the cycle is abolished" (the cyclical component — credit-funded capacity, GPU hoarding at labs — behaves like every inventory cycle). Cycle and structure coexist; the expensive error is collapsing them into one story in either direction.
- **What the prices already embed** ([[Mental Models/Generalist - Overview|G-13]]): ORCL requires OpenAI solvency through 2030 — the market's largest unexamined credit assumption and the cleanest single mispricing candidate on the short side of this note's base case (FCF −$24B FY26 against a $300B receivable-in-waiting). NVDA ~30x fwd requires ~$350B+ DC revenue by 2028 — achievable in base. Semicap troughs are priced structurally higher — consistent with qualification-gate economics, and the bear case tests exactly that assumption. The operating variable the market is *not* pricing: the 2028 D&A-vs-AI-revenue race (§2.2).
- **Durable through digestion**: qualification-gated toll layers — [[Theses/TSM - Taiwan Semiconductor]], [[Theses/NVDA - Nvidia]] (with ASIC-share erosion), [[Theses/000660 - SK Hynix]] HBM, WFE service annuities ([[Theses/AMAT - Applied Materials]], [[Theses/LRCX - Lam Research]], [[Theses/KLA - KLA Corporation]], [[Theses/ASMI - ASM International]]), power/thermal backlogs ([[Theses/VRT - Vertiv Holdings]], [[Theses/VICR - Vicor Corporation]], [[Theses/CCJ - Cameco]]), materials/components insulation ([[Theses/6981 - Murata Manufacturing]], [[Theses/2383 - Elite Material]], [[Theses/BESI - BE Semiconductor Industries]]).
- **Fragile**: leveraged merchant capacity — [[Theses/CRWV - CoreWeave]] (interest 25.8% of revenue; the cycle's forward indicator — neocloud credit stress fires before hyperscaler earnings derate), [[Theses/NBIS - Nebius Group]] (cleaner balance sheet, same exposure), [[Theses/CBRS - Cerebras Systems]] (OpenAI-concentrated), Oracle's leveraged OpenAI bet.
- **Demand-capture beneficiaries of the digestion**: deployment layer converts cheap post-frenzy compute into margin — [[Theses/PLTR - Palantir]], [[Theses/NOW - ServiceNow]], [[Theses/SHOP - Shopify]]/[[Theses/NET - Cloudflare]] (agent-commerce and edge rails); the 2028 losers' capacity becomes the 2029+ winners' input cost.

## 8. Catalysts & Falsifiers (dated observables)

| When | Observable | Reads on |
|---|---|---|
| Jul 30–31, 2026 | AMZN Q2 (does it out-raise GOOGL's ~$200B?), META Q2 (guide top of $125–145B?) | 2026 exit velocity |
| Q3 2026 | Capex/OCF crossover confirmed in prints (Epoch projection); big-4 net debt issuance | Funding-structure shift — starts the base-rate clock (§1.1) |
| H2 2026 | Anthropic holds profitability through the compute-cost step-up; OpenAI next raise vs $852B post | Value-capture thesis; Tranche C/D counterparty health |
| H2 2026–2027 | H100/B200 rental prices — renewed slide below the Oct-25 floor ($1.70/hr) = oversupply; current +40% rebound = scarcity intact. Merchant rental IRRs sustainably >25% would falsify the toll-booth-only ROIC claim (§2.1) | Utilization / depreciation-schedule validity / where value accrues |
| Jan–Feb 2027 | **Hyperscaler CY2027 capex guides** — the single highest-information event for this note | Base/bull/bear branch point |
| 2027 | CRWV refinancing costs (interest already 25.8% of revenue); any neocloud restructuring | Credit-event trigger for bear path |
| 2027–28 | Enterprise depth metrics (functions/firm, agents-scaled-per-function) inflecting up *before* any capex deceleration | Falsifies the pause thesis in the bull direction — deployment phase without a correction |
| Through 2028 | Big-4 D&A ($170B→$260–300B) vs disclosed AI revenue (needs ~$300–360B incremental); big-4 cutting franchise-defense capex >15% would falsify the "cash-funded tranche is acyclical" claim | The EPS-compression reckoning (§2.2); tranche-model validity |
| Quarterly | Token-volume growth (Google/OpenRouter series): a quarter below ~2x/yr while efficiency gains continue flips the demand floor entirely | Demand-floor falsifier — shared with the semis book |

## 9. Related Research

- [[Research/2026-07-12 - Enterprise AI Adoption - Gating Factors Critique, 2030 Trajectory, Winners-Losers - synthesis]] — verified adoption trajectory and gate re-sort underlying §5
- [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]] — rental floor/ceiling framework and lab-capture regime shift underlying §2
- [[Research/2026-06-04 - AI Dark Output GDP Measurement Gap - deep-dive]] — why part of the coverage gap is measurement, and why capture (not output) still binds
- [[Research/2026-06-05 - AI Silicon Shortage - N3 and Memory Constraint - deep-dive]] — supply-constrained framing; power-ahead-of-silicon overbuild tell
- [[Website/2026-07-22 - How to Read the Semiconductor Cycle]] — three-clocks framework applied in §7
- [[Sectors/Neoclouds & GPU-as-a-Service]] · [[Sectors/Compute & AI Compute Accelerators]] · [[Sectors/Data Center Power & Cooling]] · [[Sectors/Semiconductor Capital Equipment]] · [[Sectors/Enterprise Workflow AI & Automation]]

## Log

- 2026-07-29: Note created. Independent build: de-circularized end-demand ledger (~$150–180B vs ~$850–900B 2026 capex, 5–6x coverage gap); four-tranche capex segmentation by funding durability; depreciation-wall math (big-4 D&A → $260–300B by 2028, requiring ~$300–360B incremental AI revenue); consumer/prosumer 5-yr TAM $85–135B (price ceilings, churn, output-monetization failure); corporate 5-yr TAM $250–400B (organizationally rate-limited to ~2032); capex projection base case $1.0–1.1T 2027 → 2028–29 digestion → ~$1.3–1.4T 2031. Sources: FMP statements, ~90 web sources via 5 research agents (2 killed by rate limit mid-run, data recovered from transcripts), vault research base. Key unfiled/[AGG] figures flagged inline (Cursor ARR, Anthropic annualization, ChatGPT Pro subs).
- 2026-07-29: Manual edit per user direction — detached from pre-June-2026 vault documents (removed AI Bubble Risk companion framing and $650B-threshold lineage, removed Agentic Internet citation; coverage requirement, digestion base case, and crossover marker re-derived on 2026-only data — conclusions unchanged); dissolved the standalone Mental Models section, weaving [G-4]/[G-7]/[G-10]/[G-13]/[G-14], the semis cycle-vs-structure discipline, and both lenses into §1, §2, §4–§7 inline; sections renumbered 8→8/9.
