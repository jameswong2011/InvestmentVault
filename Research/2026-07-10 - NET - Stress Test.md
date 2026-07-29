---
date: 2026-07-10
tags: [research, stress-test, NET]
sector: Cybersecurity
ticker: NET
source: vault synthesis
source_type: stress-test
propagated_to: [NET]
---

# NET — Stress Test (Cloudflare short case)

Adversarial stress test of [[Theses/NET - Cloudflare]] (conviction: high). Prosecutorial by design — the job is to find why this investment fails, focused on the three fronts the user flagged: (a) zero-trust competitiveness vs incumbents, (b) agentic-internet / commerce monetization, (c) Workers / compute vs cloud + hosting peers. Built from the thesis, sector/macro notes, the two 2026-07-09 mental-model lens syntheses, and exhaustive July-2026 web evidence.

## Thesis Delta

The thesis raised conviction to HIGH on 2026-05-22 — a "portfolio alignment" manual entry, not fresh evidence — and leans on the June-9 Investor Day's *raised* operating model plus "Act IV" agentic monetization. The stress test finds the single leg that separates NET's HIGH conviction from a good-but-priced infrastructure story — **Act IV monetization** — has **zero disclosed revenue, a failed-and-pivoted first product, an unshipped stablecoin, and a two-week competitive clone from AWS**. Simultaneously the two legs the thesis treats as "growth vectors" are each structurally capped: SASE is *still* a Gartner niche-player business losing the AI-security ARR race to incumbents, and the Workers "moat" is the *lower-margin* product actively compressing gross margin toward the freshly-cut 70% floor. At ~$242 (≈204x forward P/E, ~33–37x P/S, sitting **at** the ~$224–243 consensus price target) the market already pays for flawless execution of all three. 3 of 7 core bull assumptions rate 🔴. This does not automatically flip conviction, but a HIGH built on an unproven fourth act, at a price with zero margin of safety, is not defensible without formal conviction triggers the thesis still lacks.

## Summary — Thesis Vulnerability Summary

**The one reason it fails: the market is paying a ~30x-sales, 204x-earnings premium for "Act IV" agentic monetization that, one full year after launch, has produced no disclosed revenue, no marquee AI-lab customer, an unshipped stablecoin, and a free AWS clone — while the two businesses that actually generate cash (SASE and Workers) are respectively a capped Gartner niche-player and a margin-dilutive commodity.** The bull case is a bet that traffic interception *converts to durable economic capture*. In July 2026 the conversion evidence points the wrong way: Cloudflare had to **retire pay-per-crawl and relaunch it as "pay-per-use"** on July 1 2026 with exactly two non-marquee partners (You.com, Ceramic.ai), publicly conceded that "licensing today remains largely bespoke and unlikely to fully replace lost referral, advertising, and affiliate revenue," and watched AWS embed the identical x402 tollbooth into CloudFront + WAF (GA, no extra charge) within two weeks. When the differentiating leg is unproven and commoditizing at once, a HIGH-conviction, priced-for-perfection multiple is the position's biggest risk — not its reward.

## Evidence — Evidence Against (five points)

### 1. Act IV monetization: a failed first product, an unshipped coin, and a two-week AWS clone (prong b) 🔴
The thesis's Non-consensus Insight #5 and #2 — pay-per-crawl / NET Dollar / content marketplace as the settlement layer for the agentic web — is the reason conviction is HIGH. The July-2026 evidence dismantles it:
- **Pay-per-crawl was quietly discontinued and re-launched as "pay-per-use" on July 1 2026** — a one-year-in pivot Cloudflare frames as a bandwidth-efficiency upgrade but which is the classic tell of a product that did not gain paid traction. Launch partners: **You.com and Ceramic.ai only**. Not OpenAI, not Anthropic, not Google — i.e., none of the crawl demand that would make the market real.
- **Cloudflare's own one-year retrospective discloses zero revenue, zero opt-in counts, zero transaction volume**, and concedes: *"licensing today remains largely bespoke and unlikely to fully replace lost referral, advertising, and affiliate revenue."* Its headline proof point — ">50 publisher-AI agreements" — is measured **since 2023**, predating the product, and is not attributed to Cloudflare's rails.
- **AWS shipped the same tollbooth for free.** On June 17 2026 AWS CloudFront + WAF added a "Monetize" Bot Control action letting any origin charge AI agents per request in USDC via x402 — GA, no charge beyond standard WAF pricing — plus Bedrock AgentCore Payments (May 2026). x402 is a **Linux Foundation open standard co-owned by AWS, Coinbase, Circle, Cloudflare and 20+ members**; it is not a proprietary Cloudflare layer. This is the [[Lens - Value Layer Monopoly]] §2 falsifier firing in real time (the thesis's own 2026-07-10 Mental Models entry logged it): the *rail* is a commodity; the only defensible residual is default-block enforcement over ~20% of web traffic — itself contestable (see #4).
- **NET Dollar remains vaporware.** Announced September 2025, still "coming soon / exploring partnerships (Coinbase, Zerohash)" in mid-2026. Novel revenue stream #1 has not shipped a year later.
The [[Macro & Technology/Agentic Internet]] note itself lists "publisher/crawler revolt fails to become a healthy two-sided market" and "hyperscaler absorption" as live failure modes — both are now happening.

### 2. Zero-trust: still a Gartner *niche player*, losing the AI-security ARR race to the incumbents (prong a) 🔴
The thesis's Outstanding Question #4 ("when does NET reach Gartner Leader?") is now answered — **it did not, in 2026.**
- **2026 Gartner Magic Quadrant for SSE: Cloudflare = "niche player."** Leaders are Zscaler, Netskope, and Palo Alto Networks (which *joined* the leaders). NET's positioning did not move into the enterprise-procurement-cleared quadrant that unlocks security-led F500 evaluations. Per the thesis's own SASE deep-dive, Leader status is a procurement filter for ~70% of F500 RFPs — NET is still excluded before pricing.
- **Incumbents are winning the AI-security narrative that was supposed to be NET's opening.** Zscaler (Q3 FY26): revenue $850.5M +25%, ARR +25%, **AI-Security ARR heading past $500M by FY-end**, non-GAAP operating margin at an all-time-high 23%. Netskope: ARR **$845M +29%** with best-in-class DLP/CASB. Zscaler's *AI-security ARR alone* (~$500M) roughly equals Cloudflare's **entire** estimated SASE ARR ($325–540M). The gap is not closing; the incumbents are compounding 25–29% off 6–10x larger bases while adding the exact AI-security ARR NET's thesis assumed it would capture.
- Cloudflare's flagship Q1-2026 SASE win was a **$5.1M / 5-year** deal (a Fortune 500 insurer replacing six vendors) — real, but an order of magnitude below Zscaler's 8-figure ZFlex deals, and still against ~400 enterprise SASE customers vs ZS ~4,000+ / PANW ~6,300+. DLP is text-only/no-OCR/network-only, CASB is in-line only, SD-WAN ~4/10 — none addressed at Investor Day.

### 3. Workers / edge compute is the margin *problem*, not a high-margin toll (prong c) 🔴
The bull frames Workers as a structural unit-economics weapon. The financials say it is the **lower-margin drag pulling gross margin down**:
- Q1 2026 GAAP gross margin **71.2%**, down from 75.9% a year earlier and **-210 bps q/q** — management attributed the decline explicitly to *"higher growth in lower-margin developer products"* plus network-cost allocation. Investor Day already **cut the long-term GM floor to 70%** and said Workers is "not yet optimized for gross margin."
- Workers' genuine technical edge (≈240x faster cold start than Lambda, 2–5x cheaper, 330+ cities) does **not** confer pricing power — the workloads are cheap *by design* ($0.30/M requests, free egress). Cheap + fast + commoditized is a share-gain engine that *dilutes* margin, the opposite of a value-layer toll. The [[Research/2026-07-09 - Automation AI Readiness Lens - Highest Fit Listed Beneficiaries - synthesis]] scores NET "A Strong, **B Weak** — Workers AI monetization still sub-scale vs valuation."
- The competitive floor is rising: Vercel, Fly.io, Deno and now **AWS at the edge** (x402 in CloudFront) are all present; R2's zero-egress wedge is narrowing (AWS cut egress to $0.085/GB) while R2 still lacks HIPAA/FedRAMP-High/PCI-DSS-L1 to win regulated storage. The "1B CPUs needed" scale math is an *industry* demand story; the CPU buyers are hyperscalers and neoclouds, not necessarily Cloudflare.

### 4. The enforcement moat underpinning the *entire* Act IV market is contestable — and invites retaliation 🟡
Act IV rests on "reliable scarcity" (bot management as market infrastructure). Two problems:
- **Enforcement is a cat-and-mouse that Cloudflare is visibly fighting.** Agentic browsers (OpenAI Atlas, Perplexity Comet) run on Chromium and are near-indistinguishable from human Chrome traffic; the public Cloudflare–Perplexity spoofing dispute (UA rotation, network cycling, ignored do-not-crawl) shows the "scarcity" is leaky. If agents route API-direct or via cloud browsers, the tollgate is bypassed.
- **Retaliation / antitrust tail absent from thesis Risks.** Google (the largest crawler, with ~2x more data access) refuses to separate crawlers; Cloudflare's Sept 15 2026 default-block of mixed-use crawlers on ad pages picks a fight with Googlebot. The mechanism to force payment is also the mechanism to trigger Google Search deprioritization of Cloudflare-fronted sites — a systemic risk to Cloudflare's publisher base. Cloudflare is lobbying UK/EU regulators against Google, converting a "product" into a regulatory campaign.

### 5. Valuation leaves zero margin of safety; conviction was raised on non-evidence; insider selling into strength 🔴/🟡
- **The stock is at its price target.** ~$242 (July 6 2026) vs consensus PT ~$224–243 → ~0% implied upside; forward P/E ~204x (industry ~19x), P/S ~33–37x, ~115x forward EBITDA. Motley Fool ("Is Cloudflare Overvalued?"), Seeking Alpha ("Too Expensive, Too Little Room For Error"), and short-seller screens all flag it. The thesis's own reverse DCF ($100–150 fair value) is anchored to the stale **$183 / $65B** Key Metrics table; at $242 (~$85B+ mcap) the required 25–30% CAGR × 5–7 years + FCF-margin-doubling bar is *higher*, not lower.
- **HIGH conviction rests on promises, not results.** The raised 30%+ operating-margin / 3–5% G&A model is 100% dependent on the **unproven 1,100-role (20%) "agentic-AI-first" restructuring** delivering *durable* leverage — announced *with* the Q1 record print, which the stock sold off **-18%** on. If AI productivity plateaus, the raised model is unmet and there is no Act IV revenue to fill the gap.
- **NGR/DBNR fell to 118%** (-2 pts y/y — wrong direction) and FCF margin is still 13% — both trending against the bull's Rule-of-50 story.
- **Prince sold ~243,000 shares for ~$55M between June 22 and July 6 2026** at $212–247 (near the ATH after a ~50% run), leaving him only 360,807 shares (~$99M). 10b5-1, but the magnitude and timing are a signal, not a comfort.

## Assumption Stress Table

| Bull Assumption | What Must Be True | Evidence For | Evidence Against | Fragility |
|---|---|---|---|---|
| Act IV converts traffic interception into durable economic capture | Publishers + AI labs pay Cloudflare a take-rate on agent traffic at scale | 20% of web fronted; +1,700% y/y agent requests; 2B HTTP 402/day (Investor Day) | Pay-per-crawl pivoted after 1yr to pay-per-use w/ 2 non-marquee partners; **zero disclosed revenue**; Cloudflare concedes licensing "unlikely to fully replace lost… revenue"; **AWS cloned x402 into CloudFront free**; NET Dollar unshipped | 🔴 |
| NET closes the SASE gap → Gartner Leader, wins security-led F500 | DLP/CASB/SD-WAN parity + Leader status by 2027–28 | Anycast perf edge; 50–65% price discount; $5.1M/5yr vendor-consolidation win | **Still Gartner niche-player 2026**; ZS AI-security ARR (~$500M) ≈ NET's whole SASE ARR; ~400 vs ZS 4,000+/PANW 6,300+ enterprise SASE customers; gaps unaddressed at Investor Day | 🔴 |
| Workers/edge is a high-margin profit engine | Edge compute monetizes at platform-level GM as it scales | 5.5M devs; Dev ARR +137%; 240x cold-start & 2–5x cost edge real | Dev products are the **explicit GM-compression driver** (GAAP GM 71.2%, floor cut to 70%); "not yet optimized for gross margin"; workloads cheap by design → dilutive | 🔴 |
| FCF margin doubles to 30–35% via AI-first restructuring | 20% headcount cut delivers durable opex leverage (G&A 10%→3–5%) | Investor-Day model; internal "Cloudflare OS" proof points | Unproven restructuring; FCF still 13%; $140–150M charge; stock -18% on the print; execution/culture risk of cutting 20% of staff at a record quarter | 🟡 |
| Revenue holds 25–30% CAGR to $5B+ by YE2028 | Sustained ~28–34% growth at $2.8B+ base for 5–7 yrs | Q1 +34% reaccel; RPO strength; cRPO +34% | [G-10] base rate: few firms hold >25% CAGR at this scale for 5–7 yrs; **NGR fell to 118%** (-2pts); reverse-DCF bar rises at $242 | 🟡 |
| R2 zero-egress stays a durable adoption wedge | Egress stays the deciding cost; NET keeps the price gap | R2 $0 egress vs S3; AI storage tier added | AWS cut egress to $0.085/GB (gap narrowing); R2 lacks HIPAA/FedRAMP-High/PCI-DSS-L1 → locked out of regulated storage | 🟡 |
| Physics/network moat stays uncontested at the edge | Hyperscalers keep ceding the edge layer | 14-yr network, 330+ cities, homogeneous stack — genuinely hard to replicate | AWS now monetizing agents at CloudFront edge; agentic browsers evade "reliable scarcity"; the moat is real but no longer uncontested | 🟡 |

**Score: 3 of 7 core assumptions 🔴 (critical), 4 🟡 (fragile). Zero 🟢.** The three 🔴s are precisely the legs that justify a HIGH conviction and a ~30x-sales multiple.

## Research Gaps

What the thesis does not know that it needs to:
- **Dollar revenue from Act IV.** Pay-per-crawl / pay-per-use / Content Signals / NET Dollar have *no* disclosed revenue line. Until there is one, the HIGH-conviction leg is unfalsifiable narrative. Outstanding Question #8 (pay-per-crawl TAM/timeline) remains open and now leans negative.
- **Clean segment split.** Outstanding Question #1 is still unresolved — single-segment reporting means investors cannot verify whether the developer platform is $200M or $500M, i.e., whether the growth story is real or mix-flattered.
- **What a serious short has that the vault doesn't:** (a) real pay-per-crawl opt-in/settlement data (Cloudflare withholds it — itself a tell); (b) SASE win/loss rates vs ZS/PANW at F500; (c) Workers *gross-margin-by-product* (hidden inside the single segment); (d) the durability of the 20% restructuring (churned senior ICs, roadmap slippage); (e) Google's actual response to the Sept 15 crawler block.
- **Framework gap (flagged in the thesis's own Mental Models section):** conviction was raised to HIGH on 2026-05-22 with **no Conviction Triggers section**. There is no pre-committed NGR floor, Act IV revenue-disclosure deadline, or outage-frequency threshold — so the thesis can degrade indefinitely without ever formally triggering a reassessment.

## Kill Trigger

Specific, falsifiable events that invalidate the thesis:
1. **Primary (monetization):** The FY2027 guide (given ~Feb 2027) or any FY2026 print through Q4 discloses **no** standalone Act IV revenue line, OR pay-per-use is still confined to sub-scale partners (no OpenAI/Anthropic/Google/major-publisher paying at scale) — while the stock trades >25x P/S. This is the "toll-layer before monetization" base-rate failure crystallizing.
2. **Secondary (growth quality):** DBNR/NGR prints **<115%** on any quarter (already 118% and falling) — signals the expansion engine, not just new logos, is decelerating and the Rule-of-50 target is unreachable.
3. **Competitive (SASE):** The 2027 Gartner SSE MQ keeps Cloudflare a niche-player while Zscaler AI-Security ARR clears ~$750M — confirming NET is permanently excluded from security-led F500 SASE and the "1 of 3 growth vectors" argument loses a vector.
4. **Structural (moat):** A fourth multi-hour global outage, OR Google publicly deprioritizes/deranks Cloudflare-fronted sites in response to the Sept 15 crawler block — either converts the "tollbooth" from an asset into a systemic liability.

## Section Weakness Map (handoff to /deepen)

| Section | Weakness | Severity | What /deepen should fix |
|---|---|---|---|
| Key Metrics | Table stale at ~$183/$65B "as of April 14 2026"; stock ~$242, ~$85B+ mcap — flatters the reverse-DCF | 🔴 | Refresh via `/numbers`; re-run reverse DCF at current price so the required-CAGR bar is honest |
| Conviction Triggers | **Section does not exist**; HIGH raised on portfolio-alignment, no falsifiable triggers | 🔴 | Add the section: NGR floor (≥115%), Act IV revenue-disclosure deadline, outage-frequency threshold, Gartner-Leader-by-date |
| Bull Case / Insight #5 (Act IV) | Treats pay-per-crawl/NET Dollar as validated optionality; ignores the July-2026 pivot, AWS clone, unshipped coin | 🔴 | Rewrite to reflect zero-revenue reality + x402 commoditization; downgrade from differentiator to speculative optionality |
| Risks | Missing: x402 commoditization by hyperscalers; Google retaliation/antitrust tail; agentic-browser bot-detection evasion; single-point-of-failure outage risk | 🔴 | Add these four; the current Risks under-weight the ones now firing |
| Industry Context → SASE | Gartner "Visionary" language stale; 2026 MQ = niche-player; incumbent AI-security ARR now dwarfs NET SASE ARR | 🟡 | Update MQ status; add ZS/Netskope AI-security ARR comparison |
| Business Model → Developer Platform | Presents Workers as unit-economics weapon without flagging it is the GM-compression driver | 🟡 | Reconcile the "moat" framing with the fact that its growth cuts gross margin toward the 70% floor |

## Contradiction Check (internal)

- **Bull vs Bear/Risks:** The Bull Case leans on "agentic internet creates a new TAM"; the Bear Case and Risk #8 already flag these streams as "unproven / no precedent." The new evidence moves them from *unproven* to *actively failing/commoditized* — the internal contradiction is now resolved *against* the bull.
- **Conviction vs evidence:** HIGH conviction with (a) OQ#1 unresolved, (b) OQ#4 answered negatively (still niche-player), (c) OQ#8 leaning negative, and (d) no Conviction Triggers section = the classic red flag the stress-test spec names ("High conviction with thin/unanswered questions").
- **Key Metrics internal consistency:** 34% revenue growth **with** a 44% "unit-economic-margin" reframe **and** a falling GAAP gross margin (71.2%) **and** FCF still 13% — the high-growth-AND-margin-expansion combination the thesis requires has few precedents at $2.8B scale, and current prints trend the wrong way on both margin and NGR.
- **Mental-models agreement is an echo, not confirmation:** both 2026-07-09 lens syntheses independently warn that NET is "already HIGH — the lens confirms rather than discovers, which the Contradiction Check treats as an echo warning, not validation." Per the READING PROTOCOL, cross-model agreement (VLM + Automation + Agentic macro all bullish) is the trigger to *disconfirm* — which this test does.

## Idiosyncratic vs cluster-wide (graph primer)

- **Idiosyncratic to NET** (peers unaffected — surfaced first per confirmation-bias mitigation): SASE niche-player status (CRWD/PANW are Leaders/platform-strong); Workers gross-margin drag; pay-per-crawl pivot/failure; unshipped NET Dollar; multi-outage single-point-of-failure risk; Prince selling.
- **Cluster-wide** (Agentic Internet + Cybersecurity clusters): "will agent-commerce volume convert to revenue?" also gates [[Theses/CRCL - Circle Internet Group]] (x402 take-rate) and [[Theses/SHOP - Shopify]] (agent GMV); AWS/hyperscaler x402 commoditization pressures CRCL's issuer economics too; high-multiple/rate-regime compression hits the whole [[AI Bubble Risk and Semiconductor Valuations]] cohort. NET's *distinctive* damage is idiosyncratic; its monetization-timing risk is shared.

## Source Excerpts

> "licensing today remains largely bespoke and unlikely to fully replace lost referral, advertising, and affiliate revenue." — Cloudflare, Content Independence Day one-year retrospective (blog.cloudflare.com/agentic-internet-bot-report, July 2026)

> "Cloudflare and AWS both implemented x402 stablecoin micropayments at their edge networks within two weeks." — InfoQ, July 2026

> "Cloudflare was labeled as a 'niche player'." — 2026 Gartner Magic Quadrant for SSE coverage (SDxCentral / BankInfoSecurity)

> "at this multiple, execution ambiguity gets repriced fast." — bear-case summary, 2026 (Seeking Alpha: "Too Expensive, Too Little Room For Error")

### Sources
- Cloudflare Q1 2026 results — [businesswire](https://www.businesswire.com/news/home/20260507927382/en/Cloudflare-Announces-First-Quarter-2026-Financial-Results), [Q1 transcript](https://www.theglobeandmail.com/investing/markets/stocks/NET/pressreleases/1789259/cloudflare-net-q1-2026-earnings-call-transcript/)
- Pay-per-crawl → pay-per-use pivot — [TechCrunch](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/), [Cloudflare blog](https://blog.cloudflare.com/agentic-internet-bot-report/)
- AWS x402 in CloudFront — [InfoQ](https://www.infoq.com/news/2026/07/cloudflare-aws-x402-micropayment/), [The Defiant](https://thedefiant.io/news/defi/aws-cloudfront-coinbase-x402-ai-agents-usdc-base)
- Gartner SSE 2026 (NET niche-player) — [SDxCentral](https://www.sdxcentral.com/analysis/palo-alto-networks-joins-netskope-zscaler-as-leaders-in-gartner-sse-magic-quadrant/), [BankInfoSecurity](https://www.bankinfosecurity.com/zscaler-netskope-palo-alto-top-sse-gartner-magic-quadrant-a-28565)
- Zscaler / Netskope AI-security ARR — [Investing.com](https://www.investing.com/news/earnings/zscaler-faces-earnings-test-as-ai-security-bets-face-scrutiny-93CH-4710151), [Yahoo/Netskope](https://finance.yahoo.com/technology/ai/articles/netskope-stock-outlook-hinges-ai-143600084.html)
- Workers vs Lambda/Vercel — [morphllm](https://www.morphllm.com/comparisons/cloudflare-workers-vs-vercel), [tech-insider](https://tech-insider.org/cloudflare-workers-vs-lambda-2026/)
- Valuation / bear case — [Motley Fool](https://www.fool.com/investing/2026/06/23/is-cloudflare-overvalued/), [Seeking Alpha](https://seekingalpha.com/article/4918709-cloudflare-stock-too-expensive-too-little-room-for-error), [24/7 Wall St](https://247wallst.com/investing/2026/05/04/is-cloudflare-overvalued-at-182x-earnings-analysts-still-see-12-upside/)
- Prince insider sales — [StockTitan Form 4](https://www.stocktitan.net/sec-filings/NET/form-4-cloudflare-inc-insider-trading-activity-c8f71fc3850f.html)
- Outages — [Nov 18 2025](https://blog.cloudflare.com/18-november-2025-outage/), [Feb 20 2026](https://blog.cloudflare.com/cloudflare-outage-february-20-2026/)
- Google crawler / antitrust — [Cloudflare blog](https://blog.cloudflare.com/uk-google-ai-crawler-policy/), [TechCrunch](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/)
- Agentic browsers / bot evasion — [HUMAN Security](https://www.humansecurity.com/learn/blog/chatgpt-atlas-vs-perplexity-comet-agentic-browsers/), [AI CERTs](https://www.aicerts.ai/news/crawler-bypass-showdown-cloudflare-vs-perplexity-ai-agents/)
- NET Dollar status — [The Defiant](https://thedefiant.io/news/defi/cloudflare-to-launch-net-dollar-stablecoin)

## Related
- [[Theses/NET - Cloudflare]] — parent thesis (conviction high; this test argues for a formal reassessment + Conviction Triggers section)
- [[Research/2026-07-09 - Value Layer Monopoly Lens - Highest Fit Listed Beneficiaries - synthesis]] — NET as layer-*creation* bet; x402 falsifier
- [[Research/2026-07-09 - Automation AI Readiness Lens - Highest Fit Listed Beneficiaries - synthesis]] — NET "A Strong, B Weak"; Workers AI sub-scale vs valuation
- [[Research/2026-06-09 - NET - Cloudflare 2026 Investor Day - deep-dive]] — the raised model + Act IV framing this test stresses
- [[Sectors/Cybersecurity]] — SASE competitive context; NET 2-5yrs behind ZS/PANW
- [[Macro & Technology/Agentic Internet]] — the failure modes (publisher revolt, hyperscaler absorption) now firing
