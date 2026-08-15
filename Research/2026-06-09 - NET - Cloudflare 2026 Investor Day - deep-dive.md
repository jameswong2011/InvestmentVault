---
publish: false
date: 2026-06-09
tags: [research, cybersecurity, NET, edge-computing, agentic-ai, investor-day]
sector: Cybersecurity
ticker: NET
source: 'Cloudflare 2026 Investor Day presentation (193 slides), June 9, 2026, New York Stock Exchange. Primary deck ingested from _Inbox/Cloudflare 2026 Investor Day.pdf (archived to _Inbox/processed/). Webcast/replay: Cloudflare IR (https://cloudflare.net). Slideshow mirror (paywalled): https://seekingalpha.com/article/4913553-cloudflare-inc-net-analyst-investor-day-slideshow'
source_type: deep-dive
---

# Cloudflare 2026 Investor Day — NET

Primary-source summary of the 193-slide deck presented at Cloudflare's first Investor Day since IPO, held at the NYSE on June 9, 2026. Speakers: Phil Winslow (VP Strategic Finance/IR, opening), Matthew Prince (CEO, Vision), Rita Kozlov (VP Product, Developer Platform — "AI"), Sam Rhea (CIO, "Cloudflare OS"), Stephanie Cohen (Chief Strategy Officer, "Act IV"), Mark Anderson (President of Revenue, GTM), Thomas Seifert (CFO, Finance). Relates to [[Theses/NET - Cloudflare]], [[Sectors/Cybersecurity]], [[Agentic Internet]].

## Thesis Delta

Cloudflare materially **raised its long-term operating model** — operating margin target 20%+ → **30%+**, FCF margin ~25% → **30–35%+**, with G&A cut to **3–5%** of revenue and S&M to 23–25% — and reframed the entire equity story around **"Act IV"**: monetizing agentic traffic at the network layer (pay-per-crawl, content marketplace, x402 payments). This strengthens the bull case on two of the thesis's open fronts (the FCF-margin path and the agentic-monetization TAM) while validating the bear case on gross margin — management **lowered the gross-margin floor to 70%** (from 75%) and argued GM is the wrong lens, pivoting investors to a **44% "unit economic margin."** Reaffirmed **$5B annualized revenue before YE2028** (from $2.4B at YE2025, ~28% CAGR) and a new commitment to **GAAP profitability by 2028 at the latest**; "Rule of 40" North Star raised to **Rule of 50 in 2027–2028**. Partial answer to the thesis's #1 Outstanding Question (segment mix): Developer ARR **+137% y/y** and Cloudflare One ARR **+43% y/y** in 2025, though no clean dollar split was given. Conviction unchanged (high) pending confirmation — the 30%+ operating-margin / 3–5% G&A model is predicated on the unproven agentic-AI-first restructuring delivering durable opex leverage.

## Summary

The deck's spine is a four-act narrative: **Act I (Connect & Protect)** + **Act III (Build)** = **Act IV (the Agentic Internet)** — the explicit equation on slide 115. Management's argument is that AI has triggered a platform shift on the scale of cloud (2000s) and mobile (2007), but faster — Gen AI reached 1B users in 2.5 years vs 6 for smartphones and 14 for the internet — and that this shift simultaneously (a) explodes the volume of code and applications being built, (b) breaks the ad/traffic business model of the open web, and (c) demands a fundamentally new cloud architecture that hyperscalers cannot provide. Cloudflare positions its 2017 bet on V8 **isolates** as the prescient foundation: because isolates re-share one runtime across many runs (0ms cold starts, scale-to-zero), they run agent workloads "up to 100x more efficiently" and lower agent TCO ~50% vs AWS/Vercel. The thesis: agents generate "infinite ephemeral applications, many per user" — the opposite of the microservices model hyperscalers optimized for ("many copies of one application") — so the next bottleneck to AI is not GPU intelligence but **CPU for execution**, where serving 1B knowledge workers × 10 agents would need ~20x current global server-CPU production.

The strategic centerpiece is **Act IV** (Stephanie Cohen, the recently-hired Chief Strategy Officer): "every agentic interaction on the Internet is a chance for commerce." Because Cloudflare sits in front of ~20% of the web and is a **neutral** party (no frontier LLM, no publisher competition, trusted by both sides), it can become the "market maker" / "control plane" between content supply and agent demand. The functioning-market thesis enumerates six required capabilities Cloudflare claims to uniquely hold — reliable scarcity (bot management), analytics, value discovery, streamlined workflows, neutrality, and a payment system — and the strategic shift is "from protecting websites from bots to **monetizing trusted automated demand**." Daily AI-agent requests rose **1,700% y/y** (Jun 2025→May 2026); Cloudflare already serves **2 billion HTTP 402 ("payment required") responses per day** via the x402 standard it co-founded with Coinbase and Stripe. The CFO's section (Seifert) ties this to unit economics: each successive Act carries lower cost-to-book, lower cost-to-serve, and lower attrition, so **Act IV could have unit economics "off the chart,"** and the company uses Microsoft's Intelligent Cloud (gross margin fell 76%→62% as Azure scaled, yet operating margin held ~42% and Rule of 40 rose to 64%) to argue that falling gross margin is compatible with rising platform-level economics.

The second pillar is **Cloudflare as "its own most demanding AI customer"** (Sam Rhea, CIO) — the operational embodiment of the May 7 agentic-AI-first restructuring (1,100 roles / ~20% of headcount cut). "Cloudflare OS" is an internal agent harness (running in Cloudflare Containers) given to every employee, with a centrally-managed skill-file context layer, model optionality, and scoped system-of-record access. Proof points: AI-built `vinext` (a Next.js reimplementation, 4x faster builds, 57% smaller bundles, ~$1,100 in tokens, <1 week) and `EmDash` (a serverless CMS rebuilding WordPress in 2 months); an AI code-review system that ran 131,246 reviews across 48,095 merge requests in 5,169 repos in 30 days at $0.98 median cost and 100% coverage. This internal leverage is the mechanism management credits for the raised operating model — AI changes GTM staffing ratios (more quota-carrying AEs per support head) and rebuilds G&A around agentic workflows, justifying G&A at 3–5% of revenue. The GTM section (Anderson) frames a transition from "market education" to "market pull" — brand awareness up 2.3x, the buyer question shifting from "Who is Cloudflare?" to "Why now?" — supported by a new GTM leadership bench, sharper segmentation (Developer vs Cloudflare One "speedboats"), partner-first motion, and AE productivity at all-time highs.

## Framework / Mental Model

Three named frameworks anchor the deck and are reusable for tracking the thesis:

**1. The "Acts" framework (revenue eras → unit-economics ladder).** Cloudflare maps its business to four sequential "Acts," each with a distinct unit-economics signature. The CFO's innovation this Investor Day was overlaying the Acts onto a growth/margin frontier where each act sits further "up and to the right."

| Act | Business | Cost to Book (S&M/$ ARR) | Cost to Serve (Delivery+R&D+Support+G&A) | Attrition | Net |
|---|---|---|---|---|---|
| **Act I** | Connect & Protect (security/CDN) | Average | Average | Higher | Baseline |
| **Act II** | Network/performance (Zero Trust era) | Higher | Low | Lower | Improving |
| **Act III** | Build (Workers/developer platform) | Lower | Initially high, lower at scale | Low | Strong |
| **Act IV** | Agentic Internet (monetize agent demand) | **Lowest** | **Lowest** | **Lowest** | **"Off the chart"** |

Equation (slide 115): **Act I + Act III = Act IV** (Connect & Protect + Build = Agentic Internet). The point: Act IV is not a new product line requiring new cost structure — it monetizes traffic already flowing through the existing network, so incremental cost-to-serve approaches zero.

**2. Unit Economic Margin (the metric management wants to replace gross-margin focus).** Defined as `Unit Economic Margin = [LTR − CTB − (CTS × LTR)] / LTR`, where Lifetime Revenue `LTR = $1 ARR / attrition rate`, `CTB` = sales & marketing cost per dollar of incremental ARR, `CTS` = delivery + R&D + support + G&A as % of ARR. Current blended unit economic margin = **44%**. The framework's purpose: argue that a falling reported gross margin (Workers/paid-traffic mix) can coexist with a *rising* economic margin because platform businesses compress CTB and CTS faster than gross margin erodes (the Microsoft Intelligent Cloud case study is the evidence — see Evidence).

**3. Four revenue models (and why "Cap Model" shapes reporting).** Cloudflare monetizes via: (1) **Flat Rate** (Free/Pro/Business — fixed price, feature-gated), (2) **Pure Usage** (pay-as-you-go, billed in arrears), (3) **Pool of Funds** (enterprise commits an upfront value drawn down flexibly — "effectively ramped deals," revenue recognized lower near-term then accelerating), (4) **Cap Model** (committed capacity: fixed recurring fee + monthly entitlement + tiered overages). **The majority of contracts are Cap Model, with "requests" as the primary unit of measure.** Investor-relevant mechanic: accelerating traffic causes *earlier-than-forecast* cap upsizing — revenue inflects up but with a lag to the underlying usage inflection, so the agentic surge feeds revenue on a delay.

## Evidence

### Headline financial targets

| Target | Detail |
|---|---|
| Revenue | **$5B annualized before year-end 2028** (from **$2.4B** annualized at YE2025) — ~28% CAGR, roughly 2x in 3 years |
| "Rule of" North Star | Rule of **40** since IPO → **50% in 2027** → **50%+ in 2028** |
| GAAP profitability | **By 2028 at the latest** (first explicit GAAP-breakeven commitment) |
| Operating margin (LT) | Prior 20%+ → **Updated 30%+** |
| FCF margin (LT) | Prior ~25% → **Updated 30–35%+** |

### Long-term operating model — prior vs updated (slide 186)

| Line | 2022 | 2023 | 2024 | 2025 | Prior LT model | **Updated LT model** |
|---|---|---|---|---|---|---|
| Gross margin | 78% | 78% | 79% | 76% | 75–77% | **70–77%** |
| Sales & Marketing (% rev) | 42% | 40% | 38% | 36% | 27–29% | **23–25%** |
| Research & Development (% rev) | 19% | 17% | 16% | 16% | 18–20% | **15–17%** |
| General & Administrative (% rev) | 14% | 12% | 11% | 10% | 8–10% | **3–5%** |
| Operating margin | 4% | 9% | 14% | 14% | 20%+ | **30%+** |
| Free cash flow margin | (4)% | 9% | 10% | 12% | ~25% | **30–35%+** |

The raise is driven entirely by **opex leverage from the agentic-AI-first model**, not gross margin (which was *lowered* on the low end). G&A compression (10% → 3–5%) is the single largest delta and the most AI-dependent assumption.

### Total Addressable Market (slide 162, Cloudflare estimates on Gartner forecasts)

| Year | TAM |
|---|---|
| 2018 | $32B |
| 2026 | **$238B** |
| 2027 | $282B |
| 2028 | $329B |
| 2029 | **$384B** |

TAM stack: Cloudflare One (Zero Trust Services), Application Services, Network Services, Developer Services. **Beyond the $384B**, flagged as "Areas for Potential Incremental Growth": **Act IV**, Database, Internet of Things, 5G Cellular, Network Services — i.e., agentic monetization is explicitly *not yet* in the headline TAM.

### Scale, footprint & adoption

| Metric | Value |
|---|---|
| Share of the Internet on Cloudflare | **20%** |
| Top 10,000 sites on Cloudflare | 36% |
| Fortune 500 on Cloudflare | **42%** (Mar 31 2026; up from 39%) |
| Top 50 generative-AI web products on Cloudflare | **78%** (a16z list, Mar 2026) |
| Active developers | **5.5M+** (Mar 2026) vs 4.5M+ (Dec 2025), 3M+ (Dec 2024), 1M+ (Nov 2022) |
| $1M+ customers | **269** (Q4'25) vs 173 (Q4'24); <1% of paying customers |
| Brand awareness | 49% (Q4'23) → 52% (Q4'24) → **61% (Q4'25)** — 2.3x "market pull" |
| Agents SDK downloads | **3.2M/month** (May 2026), 42x growth, 14M since Mar 2025 launch |
| Cloudflare Vite plugin | **>10% of all global Vite downloads** |

### Product-line growth & unit economics

| Metric | Value |
|---|---|
| Developer platform ARR | **+137% y/y** (2025) |
| Cloudflare One ARR | **+43% y/y** (2025) |
| Pipeline | **+40%** |
| Blended unit economic margin | **44%** |
| Media vertical: revenue/customer | 1.3x company average |
| Media vertical: revenue growth | 37%+ (Q1'26 vs Q1'25) |
| Media vertical: expansion rate (retained) | 60%+ (Q1'26) |
| Media vertical: dollar net retention | **117% DNR** (Q1'26) |

### The agentic surge & payments

| Metric | Value |
|---|---|
| Daily AI-agent requests growth | **+1,700% y/y** (Jun 1 2025 → May 31 2026) |
| HTTP 402 responses served | **2 billion/day** (x402 standard, co-founded with Coinbase + Stripe) |
| Cloudflare network transactions/day | **30+ trillion** vs 900M for the largest payment network |
| Cloudflare network throughput | 500M+ transactions/sec vs ~100,000/sec for largest payment network |
| Registered bots identified | 500+; "hundreds of billions" of bot requests processed daily |

### Agent economics — TCO & efficiency (slide 44, vs published AWS/Vercel pricing)

| Workload | Cloudflare savings |
|---|---|
| Isolates vs container runtimes | Up to **100x more efficient** |
| Blended agent TCO | ~**50% lower** |
| Single-region web app | 15.2% lower TCO |
| Deploy 10K agent-generated apps | **63.6% lower** TCO |
| Run 1M agent sessions | **74.7% lower** TCO |

Scale math (slide 39): 1B global knowledge workers × 10 agents/worker ÷ 10 agents/CPU = **1B CPUs needed**, vs current global server-CPU production of **35–45M/year** = ~20x current output. Stated conclusion: "the next bottleneck to AI adoption… is the CPU for execution." (Cross-reads to [[Sectors/Compute & AI Compute Accelerators]] / datacenter-CPU demand.)

### The open web is breaking (the "why now" for Act IV)

| Metric | Value |
|---|---|
| Gen AI to 1B users | **2.5 years** (vs Smartphone 6y, Social 8.5y, Internet 14y) — 2x+ faster |
| Share of online attention on open web | 100% (2000s/2010s) → 55% (2015–22) → **25% (2024 AI era)**; Social+AI = 75% |
| Top tech-publication search traffic | **−58%** since 2024 (individual publishers −30% to −97% peak vs Jan 2026) |
| Human (non-bot) traffic by industry | **−35% to −40%** Jun 2025→Apr 2026 (Retail, Computer Software, IT & Services, Financial Services) |
| Digital economy | $16T (15% of global GDP); 6B+ people online (doubled in 11 years) |

### Coding-productivity explosion (Kozlov)

| Indicator | Y/Y growth |
|---|---|
| Wrangler total downloads | **+942%** |
| GitHub PRs merged | +153% |
| New iOS apps | +68% |
| New websites | +34% |
| "OpenClaw" GitHub stars | Fastest-growing repo in history — React's 13-year star count surpassed in **3 months** |

### "Our own most demanding AI customer" — internal AI proof points (Rhea)

| Build | Result |
|---|---|
| **vinext** (Next.js reimplementation on Vite → deploys to Workers in one command) | 4x faster production builds, 57% smaller client bundles; ~$1,100 in tokens, <1 week (1 engineer) |
| **EmDash** (serverless AI-native CMS on Astro + Workers) | Rebuilt WordPress-class CMS in 2 months; plugins in sandboxed isolates (solves the flaw behind 96% of WordPress vulns); built-in x402 payments |
| **AI code review** (up to 7 specialized agents per merge request) | 131,246 reviews / 48,095 merge requests / 5,169 repos in first 30 days; median 3m39s; **$0.98 median cost/review; 100% coverage** |
| GTM ratio model (illustrative) | AI automates support functions → reallocate budget to quota-carrying AEs → **+35% ACV** at flat S&M cost |

### Microsoft Intelligent Cloud — the "Act III" case study (slide 175)

| | FY2015 | FY2020 | FY2025 |
|---|---|---|---|
| Revenue y/y growth | 9.1% | 24.1% | 21.5% |
| Azure % of IC revenue | 4.0% | 29.0% | 71.0% |
| Gross margin | 76.1% | 69.1% | **62.2%** |
| Opex % of IC revenue | 34.5% | 31.3% | 20.2% |
| Operating margin | 41.6% | 37.9% | **42.0%** |
| Rule of 40 | 50.7% | 61.9% | **63.5%** |

Argument: Azure scaling from 4%→71% of mix dropped gross margin 14 points, yet operating margin *held* and Rule of 40 *rose* — "lower gross margin doesn't mean lower unit economic margin… especially for platform businesses at scale." This is the analytical defense for Cloudflare's own GM decline.

### Gross-margin reframe (slide 170)

Two drivers cited for GM trending down since Q1'24: (1) **paid-vs-free traffic mix** shifting toward paid — explicitly stated as **neutral to operating margin**; (2) **Workers developer-platform products not yet optimized for gross margin** (but "improving") while delivering outsized growth. Management: "gross margin may continue to trend down in the near-term… the scalability, elasticity, and efficiency of our network remain unchanged."

### AI-security positioning & IT-spend backdrop (slides 24, 121–130)

"Cloudflare is the only vendor to help customers **connect, protect, and build AI**" (slide 130) — positioning across four CIO/CISO + developer needs:

| Customer need | Cloudflare product(s) | "Other major vendors" |
|---|---|---|
| Secure workforce use of AI | Cloudflare One | SASE / SSE |
| Govern AI agents | Remote MCP servers, Access with MCP Server Portals | Developer-focused point tools |
| Protect AI-powered apps | Application Security (incl. AI Security for Apps) | App Security / WAAP |
| Build AI securely | Workers AI, AI Search, AI Gateway, Agents SDK, Dynamic Workers, Containers, Artifacts | Hyperscalers |

Stated edge: comprehensive AI-lifecycle protection + future-proof global architecture + model-agnostic deployment, "all on one platform and one network."

- **Model optionality** (slide 24): AI Gateway / Workers AI offer **150+ models, no vendor lock-in** (incl. private + open-source such as Kimi K2.6).
- **Demand urgency shift** (slide 121): 9 months ago "AI needs guardrails" → today "experimentation to urgency" → next 12 months "autonomous agents will automate a **double-digit percentage of all work**."
- **Attack surface** (slide 123): time between vulnerability disclosure and confirmed exploitation is collapsing toward **24 hours by 2027** — frontier models change the attack landscape (reinforces the security-spend driver in [[Sectors/Cybersecurity]]).
- **IT-spend backdrop** (Gartner CIO Agenda 2026, slides 125–126): IT budgets **+2.8%**, tech-worker headcount **+1.3%** — yet CIOs are increasing investment in cloud platforms (88%), application modernization (84%), AI (72%), and cyber/information security (69%). The "do more with flat budgets" squeeze is the consolidation tailwind underpinning the platform sell.

## Key Segments

### Opening (Phil Winslow) & Vision (Matthew Prince) — slides 3–6
Sets the frame: AI is the biggest tailwind in Cloudflare's history and a re-platforming of the internet. Prince's Vision segment is light on slides (full-bleed delivery) but seeds the four-act thesis the rest of the deck builds out.

### "AI" / Developer Platform (Rita Kozlov, VP Product) — slides 7–52
The greenfield-developer thesis. Generative AI drove the cost of writing code "to near zero," flipping the economics so it is now cheaper to **rebuild than migrate** legacy apps. Four developer-vision pillars: remove friction/velocity, best modern primitives, enterprise-grade scale, enable new AI workloads. The 2017 **isolates** bet is recast as "built for this moment" — Generation Four compute (serverless V8 isolates: 0ms cold start, scale-to-zero, no DevOps) vs Gen 1–3 (metal → VMs → containers/K8s). Core argument for *why agents need a new cloud*: agents must write and execute code because (1) context windows can't hold all tools (Cloudflare's REST API alone = 2.5M tokens as one MCP server vs 1M-token models), (2) LLMs lack situational accuracy, (3) LLMs are bad at tool-calling (~50K tokens per call). Hyperscaler microservices ("many copies of one app") can't serve agents ("infinite ephemeral applications, many per user"). New agentic primitives map to AWS's 2006 set: S3→Durable Objects & Artifacts, EC2→Isolates/Workers, SQS→Workflows. Discord's VP of Core Tech quoted endorsing Cloudflare as "the next generation cloud." Close: "Agent-native businesses are powered by Cloudflare."

### "Cloudflare OS" (Sam Rhea, CIO) — slides 53–73
"We don't just build and sell AI tools… we are our own most demanding AI customer." **Cloudflare OS** = a one-click full agent harness (in a Cloudflare Container) for every employee, a centrally-managed **skill-file context layer**, scoped system-of-record access, and model optionality by role. The "magic inbox" pattern: experts document workflows → skill files → AI agent operators run an internal service → curated back into Cloudflare OS. Cost control via model optionality, dynamic routing, the Infire inference engine, and caching ("scaling productivity without scaling cost"). Use-case demos span Builders (AI code review, agents fixing problems) and Sellers (prospect research, prescriptive daily plans, custom decks, solution-architecture proposals). This segment is the operational justification for the raised operating model.

### "Act IV" (Stephanie Cohen, Chief Strategy Officer) — slides 74–115
The agentic-commerce thesis and the deck's strategic core. "The business model of the Internet is changing… Cloudflare is the only cloud built for the Agentic Internet… every agentic interaction is a chance for commerce." Cloudflare is positioned as the neutral **"control plane"** between content **Supply** (transparency, control, optimize, charge) and agent **Demand** (optimize, behave, access, discover). Six capabilities a "functioning market" requires, each mapped to a Cloudflare product: **reliable scarcity** (Bot Management / AI Crawl Control — see-it-first on 20%+ of web), **analytics** (bot data → market intelligence), **value discovery** (first-party quality signals), **streamlined workflows** (pay-per-crawl "Easy Button," Agents SDK, AI Search), **neutrality** (no frontier LLM, no publisher competition — quantified: the #1 crawler gets up to 100x more access than the smallest, a gap only a neutral party can level), and a **payment system** (x402 + Web Bot Auth, cryptographically binding agent identity to transaction flows). Proof it's "already happening": **People Inc.** used Cloudflare to block AI crawlers and reported deal progress "much further along" — driving AI labs to the negotiating table. Strategic shift stated plainly: "from protecting websites from bots to **monetizing trusted automated demand**." Roadmap from media-today (37%+ growth, 117% DNR) to tomorrow: **Content Marketplace, Signals, Payments (micropayment rails), "Easy Button" for Agents.**

### Go-To-Market (Mark Anderson, President of Revenue) — slides 116–148
"The market has come to Cloudflare" — the buyer question shifted from "Who/Why Cloudflare?" (market education) to "Why now?" (market pull), with brand awareness up 2.3x and $1M customers 173→269. Six GTM initiatives: (1) stage-appropriate leadership & talent — a substantially new senior bench (CMO Jeff Samuels, regional GEO VPs, Chief Partner Officer); (2) become systematic/targeted — Developer vs Cloudflare One "speedboats" across Startup→Digital Native→Midmarket→Enterprise→Majors→Public Sector; (3) march toward the enterprise (42% of Fortune 500; large-customer revenue up 23–56x since Q1'18 by cohort); (4) sell the platform (one platform, one network — full product timeline since 2010); (5) win with partners first; (6) accelerate AE momentum (rolling-4Q ACV/AE at all-time highs; new-hire mix tilting to enterprise reps). AI as "full-cycle co-seller": reps spend only ~40% of time selling, and AI agents absorb the non-selling 60%.

### Finance (Thomas Seifert, CFO) — slides 149–187
Traffic growth accelerating (requests/sec +600bps q/q; agent requests +1,700% y/y). Walks the **four revenue models** (Flat / Pure Usage / Pool of Funds / Cap) and how **Cap-Model** dominance + accelerating usage pulls cap-upsizing forward; **Pool-of-Funds** (rising % of new ACV) ramps revenue recognition over the contract (example: a leading AI company's PoF deals drove +215% ACV; $85M 2-yr + $13.5M 1-yr). Value-creation = Growth + Profitability. Six growth drivers: expanding TAM, growing pipeline (+40%), improving sales productivity/capacity, momentum with larger customers, increasing platform adoption (ARR by attach-rate cohort), accelerating key products (Developer +137%, Cloudflare One +43%). Profitability built on the **unit-economics** framework (44% margin), the **Acts ladder** (Act IV "off the chart"), the **Microsoft IC** GM-vs-economics case study, and AI-driven cost-to-book (S&M) and cost-to-serve (R&D/G&A) leverage. Lands the headline targets: $5B by YE2028, Rule of 50, raised operating model, GAAP profitability by 2028.

## Contradiction Check

**Supports existing conviction (high):**
- **FCF-margin path** — the thesis's reverse-DCF required FCF margin to roughly double from 12% to 20–25%. Management now guides **30–35%+** with operating margin 30%+. If credible, this widens the valuation-support gap the bear case relied on. Affects thesis Outstanding Question #2 (can NET expand FCF margin while sustaining growth) and the Bear Case valuation point.
- **Agentic-internet monetization** — the thesis's Non-consensus Insight #5 (NET Dollar / pay-per-crawl as a settlement layer) and Insight #2 (agentic positioning) are now Cloudflare's explicit #1 strategic act, with hard usage data (1,700% agent-request growth, 2B x402/day) and a live commercial proof point (People Inc.). Affects the "novel revenue streams unproven" risk — still unproven on revenue, but adoption evidence strengthened.
- **Segment disclosure gap (partial)** — thesis Outstanding Question #1 asked for revenue mix by line. Investor Day gave growth rates (Developer +137%, Cloudflare One +43% ARR in 2025) and ARR-by-attach-rate-cohort, but **still no clean dollar split** of security vs developer vs Zero Trust. Question is narrowed, not closed.

**Challenges / validates the bear case:**
- **Gross-margin compression is now official guidance, not just a trend** — the long-term GM floor was *cut* from 75% to **70%**. This confirms the thesis Bear Case ("gross margin compression is structural, not cyclical") and Risk #2. Management's counter (unit economic margin 44%; Microsoft IC analogy) is an analytical reframe, not a reversal — investors must accept a new, lower GM regime. Affects thesis Risk #2 and the Q4'25 73.6% GAAP GM data point.
- **The 30%+ operating-margin model depends on the unproven restructuring** — G&A at 3–5% (from 10%) and S&M at 23–25% assume the agentic-AI-first model (1,100 roles cut, ~20% of staff) delivers durable, not one-time, leverage. Execution risk is concentrated here; if AI productivity gains plateau, the raised model is unmet. New risk to track that the thesis should add.

**No change to:** the SASE competitive position (DLP/CASB gaps, Gartner "Visionary" not Leader) — Investor Day did not address the enterprise-SASE product-depth gap; the thesis's SASE deep-dive stands unmodified. The deck's competitive slide (130) positions Cloudflare on AI security + AI infrastructure breadth ("connect, protect, and build AI") rather than SASE-feature parity.

## Source Excerpts

> "Act I + Act III = Act IV" — Connect & Protect + Build = Agentic Internet. (slide 115)

> "Act IV could have unit economics 'off the chart'." (slide 178)

> "The strategic shift: from protecting websites from bots to monetizing trusted automated demand." (slide 108)

> "We don't just build and sell AI tools and platforms… we are our own most demanding AI customer." (slides 54–55, Sam Rhea)

> "We know what the hyperscalers will look like in 10 years… the same as they do now. We're looking to Cloudflare for what the next generation cloud will look like." — Mark Smith, VP of Core Tech, Discord (slide 47)

> "Mobile-native businesses were powered by the cloud → Agent-native businesses are powered by Cloudflare." (slide 49)

> "Achieve GAAP profitability by 2028 latest." (slide 187)

> "$5B annualized revenue before year-end 2028" (from "$2.4B annualized revenue" at year-end 2025). (slide 180)

> "1,700% increase in daily AI agent requests on Cloudflare's network from June 1, 2025 to May 31, 2026." (slides 105/122/150)

> "2 BILLION 402 responses served per day on Cloudflare's network." (slide 106)

## Related Research & Notes
- [[Theses/NET - Cloudflare]] — parent thesis (conviction high); this Investor Day strengthens the FCF/agentic pillars, validates the GM bear case, and partially addresses the segment-disclosure Outstanding Question
- [[Agentic Internet]] — macro framework; Act IV is Cloudflare's formal claim to the layer-1/2/5/8 positioning the macro note assigns it
- [[Theses/CRCL - Circle Internet Group]] — x402 / agentic-payment rails: Cloudflare co-founded the x402 Foundation with Coinbase & Stripe and serves 2B HTTP 402 responses/day; the agent-commerce settlement layer is the shared thesis (CRCL Business Model §8 covers the x402 adoption stack)
- [[Sectors/Cybersecurity]] — sector note; "reliable scarcity / bot management as market infrastructure" extends the security-as-flywheel argument
- [[Sectors/Compute & AI Compute Accelerators]] — the "CPU for execution is the next bottleneck" claim (1B CPUs vs 35–45M/yr production) is a cross-sector datapoint on server-CPU demand
- [[Research/2026-03-31 - Cloudflare Path to Competing with Hyperscalers]] — the isolates-vs-hyperscaler and "innovator's dilemma" arguments here update that analysis
- [[Research/2026-03-31 - NET - Gemini Edge Compute Canvas]] — edge-compute economics (isolates, R2 zero-egress) corroborated by the TCO slides
- [[Research/2025-07-15 - NET - Cloudflare Workers Edge Computing]] — Workers/isolate architecture baseline
