---
date: 2026-04-22
tags: [sector, moc]
status: active
---

# Mobile Advertising Technology

## Active Theses
- [[Theses/APP - AppLovin]] — AppLovin (Axon AI ad engine / gaming mediation monopoly / CTV + e-commerce TAM expansion / sentiment-driven drawdown vs record operations)

## Key industry questions
- Can post-ATT "contextual/AI-signal" platforms (AppLovin, Moloco) hold their 2022–2025 structural lead as walled gardens (Meta Advantage+, Google Gemini ads) close the iOS signal gap via generative-AI creative automation — and does regulatory pressure on cross-platform identifier bridging (SEC, DMA) compress that lead further or entrench the incumbents against sub-scale challengers like CloudX and Liftoff?

## Industry history

The mobile ad-tech industry has cycled through five distinct power regimes since the iPhone launch, each driven by a platform-level event that reshuffled who captured the economic rent.

**Origin era (2007–2013) — networks hold power through fragmentation.** Global mobile ad spend was ~$400M in 2007 (IAB). Apple's App Store (July 2008) created the inventory substrate. The first wave of ad networks — AdMob (founded April 2006 by Omar Hamoui; acquired by Google November 2009, closing May 2010 for $750M in stock after outbidding Apple), Quattro Wireless (acquired by Apple January 2010 for $275M and relaunched as the ill-fated iAd, which Apple shuttered June 2016), Millennial Media (IPO March 2012 at $13, peaked at $27, acquired by AOL September 2015 for $238M — ~18% of peak market cap), InMobi, Jumptap, and Mobclix — served fragmented display inventory at CPM pricing. When Zynga/Supercell/King proved install-driven unit economics, cost-per-install (CPI) bidding replaced CPM, and publishers stacked networks in **waterfalls** — call Network A at $8 eCPM, cascade unfulfilled impressions to Network B at $6, then C at $4. Waterfalls created arbitrage for networks that overpromised fill and starved publishers of price discovery.

**In-app bidding era (2013–2020) — publishers gain leverage through unified auctions.** MoPub (founded 2010 by Jim Payne; acquired by Twitter September 2013 for $350M) became the neutral iOS mediation leader. AppLovin was founded 2012 in Palo Alto by Adam Foroughi, Andrew Karam, and John Krystynak; KKR took majority at $2B EV in 2018; IPO April 14, 2021 at $80 raising $1.8B at a $28.6B day-one valuation. ironSource (founded 2010 in Tel Aviv by seven co-founders led by Tomer Bar-Zeev) went public via Thoma Bravo Advantage SPAC in June 2021 at $11.1B. Facebook Audience Network and MoPub pioneered real-time in-app bidding (2016–2018), replacing waterfalls with unified auctions; by end-2020 ~60% of top-100 iOS games used bidding mediation and publishers captured 20–40% eCPM uplift.

**Privacy earthquake (2021–2023) — mediation platforms capture the vacuum.** Apple launched App Tracking Transparency on April 26, 2021 (iOS 14.5). Opt-in rates stabilized at ~25% globally by 2022 (ranging to ~35% in more recent AppsFlyer data); Meta quantified a **$10B 2022 revenue headwind** on February 2 2022 earnings, triggering a 26% one-day drop ($232B market-cap loss). Facebook Audience Network's in-app share collapsed from ~30% pre-ATT to <10% by 2023. AppLovin acquired MoPub from Twitter October 2021 for **$1.05B** (closing January 2022) and sunset the platform March 31 2022, forcing ~90 days of migration onto MAX; **apps monetizing via MAX rose 60%+** within a year and MAX absorbed MoPub's 60% iOS mediation share. SKAdNetwork (2021) → SKAN 4 (iOS 16.1, October 2022) → SKAN 5 (iOS 17.4, March 2024) progressively restored partial attribution on Apple's privacy-first terms, but none of these replaced the IDFA-era signal density — creating the structural opening for machine-learning-based predictive bidding.

**Consolidation wave (2021–2024) — mediation oligopoly forms.** Unity announced a $4.4B all-stock merger with ironSource July 13 2022; AppLovin countered August 9 2022 with a $17.54B ($20B+ headline) hostile bid for Unity contingent on terminating the ironSource deal; Unity's board rejected and closed November 2022. Unity's subsequent runtime-fee debacle (September 2023, $0.20/install, rescinded January 2024), 25% workforce cut to 4,987 employees costing $214M, and mass 2023–2024 developer defections gave AppLovin an 18–24 month head start. Digital Turbine executed $1B+ in acquisitions (Fyber $600M, AdColony $400M, Appreciate — all 2021) and saw its stock fall from ~$96 (Nov 2021) to sub-$4 today. Blackstone merged Liftoff + Vungle + JetFuel + GameRefinery (2021). Chartboost was acquired by Zynga (August 2021, $250M) then absorbed into Take-Two's Zynga deal (January 2022, $12.7B).

**AI-engine era (2023–2026) — data-flywheel winners re-rate, middle tier consolidates out.** AppLovin's AXON 2.0 (Q2 2023) replaced heuristic LTV lookalikes with deep-learning predictive models trained across billions of devices; Software Platform revenue inflected from ~$200M/quarter (Q4 2022) to ~$1.66B (Q4 2025); APP stock moved from $11 (Dec 2022) to $745 ATH (Sep 2025) — a ~68x move, the most extreme fundamental re-rating in ad-tech history. Global mobile ad spend reached **~$470B in 2025** (eMarketer/IAB blended) from $170B in 2018 and $9B in 2012 — 15% CAGR 2018–2025 decelerating to ~9% 2022–2025 as the market matures. Mobile now represents ~70% of the ~$670B global digital ad market.

## Competitive dynamics

The stack has polarized into a mediation oligopoly (MAX, AdMob, LevelPlay control ~90% of mobile gaming mediation per GameBiz/Gamesforum) paired with a fragmenting demand-side where ML-native DSPs (Moloco, Liftoff Cortex, Apple Ads) are taking share from legacy walled gardens.

**AppLovin** — Dual-side control is the moat competitors cannot replicate: MAX sees competitor bid prices and clearing rates in real time, feeding AXON's predictive models at 2M+ auctions/second. Wedbush (April 2026) notes "training data learned exponentially more" vs peers, raising PT to $725. MAX's ~5% fee is charged to advertisers, not publishers, and sits **below Unity LevelPlay's 10–12% rev-share** — AppLovin is the *cheapest* major mediation option, inverting the standard "incumbent rent extraction" narrative. The vulnerabilities are regulatory (SEC identifier-bridging probe since October 2025) and tying-style (MAX refuses to run ROAS optimization for non-MAX users, a defensive mechanic that creates antitrust exposure).

**Google AdMob** — Ecosystem leverage and AdWords demand aggregation. Outperforms LevelPlay on top-downloaded iOS by ~2x (GameBiz 2025). Weaknesses: ATT dependency on a rival platform (Apple), DMA enforcement accelerating, not first in performance ROI rankings.

**Meta Audience Network** — Had the most to lose from ATT and the most to gain from recovery. The January 28 2026 "Chained Ads" event spiked iOS revenue 5–7x overnight at eCPMs +36% to +295% (mean +125%), then vanished by January 31 (Felix Braberg). Meta's broader **Advantage+ platform hit ~$60B annualized run-rate October 2025** from $20B March 2025 — tripled in seven months. eMarketer projects Meta's 2026 worldwide ad growth at 24.1% (vs Google's 22.1%), with Meta overtaking Google in digital ad revenue for the first time. The walled-garden recovery is further along than AppLovin bulls model.

**Unity (LevelPlay + Vector)** — Vector AI platform is the gap-closer: +53% YoY growth through Q3 2025, on pace for $1B+ run rate end-2026, +15–25% ARPDAU lift in early publisher tests (below AXON's reported +40–60%). ironSource network has shrunk to <6% of Unity revenue and is declining. LevelPlay mediation is losing ground to MAX (GameBiz: "falling behind"). Margin profile ~25% EBITDA vs AppLovin's 82% reflects technical catch-up without scale leverage.

**The Trade Desk** — CTV/brand programmatic leader (~26% DSP share, CTV >50% of revenue), but minimal mobile in-app exposure. Collision with AppLovin comes through Wurl's CTV expansion and Amazon DSP's 1% take-rate assault on TTD's 20% fee. TTD market cap has collapsed from $58B (Jan 2025) to ~$10B (April 2026) — **-85% from high** — on Publicis audit findings of Kokai fees/AI behavior issues, board-member resignations, and Amazon's $80M auto-brand share shift in Q1 2025. Ad-tech's prior category leader has become the cautionary tale on software-infrastructure-premium compression.

**Moloco** — AppsFlyer Performance Index rise from #15 (2023) to #5 (Q1 2026) — the most rapid independent rise in the industry. Last private valuation $2B (Bloomberg reported IPO talks January 2026). Participates *within* AppLovin's MAX as a bidder, which structurally caps its threat but validates competitive pressure on AXON's demand-side.

**Market share shifts 2023 → 2026**: MAX gained to ~60%+ mediation (from ~50%); AdMob stable at #2; LevelPlay lost ground; ironSource collapsed; Moloco surged; Meta Audience Network latent; legacy networks (Chartboost, Fyber, InMobi) consolidating. **Ad spend concentration is accelerating** — top-5 platforms grew 60% YoY in 2025 while ranks 11–20 grew only 30% (Singular ROI Index 2025); Apple Ads entered the top tier in 2026, pressuring mid-tier DSPs.

## Product level analysis

| Product | Owner | Technical Architecture | Market Purpose | Why It Wins (or Lost) |
|---|---|---|---|---|
| **AXON 2.0** | AppLovin | Deep-learning + reinforcement-learning predictive bidding; processes 2M+ auctions/second; trained on first-party SDK telemetry across billions of devices; uses ephemeral contextual signals not persistent IDs | Predict long-term user LTV for UA and retargeting campaigns | Efficiency Paradox: total mobile installs grew modestly in 2025 but AppLovin's Net Revenue Per Installation rose **72–75%** — the engine finds *better* users, not more. Continuous retraining on MAX auction outcomes creates compounding data advantage |
| **MAX mediation** | AppLovin | Unified real-time in-app bidding across publisher ad slots; 5% fee on third-party winning bids; ~60%+ mediation share | Publisher yield management with bidding transparency | Inherited MoPub's 60% iOS share post-2022 migration; fee charged to advertisers (not publishers) at half of LevelPlay's rev-share; see-through visibility into competitor bids feeds AXON |
| **Adjust** | AppLovin | Mobile attribution + analytics across SKAN 4/5, probabilistic, and modeled conversions; 85,000+ apps | Measurement ground truth for marketing spend | Acquired for ~$1B (April 2021) pre-ATT; central to closing the AXON → attribution → retraining loop |
| **Wurl** | AppLovin | CTV ad delivery and content distribution; 300M+ TVs / 30M users/month | Extend AXON optimization into CTV inventory | Acquired $430M February 2022; launched "CTV-Connect" linking mobile installs to smart-TV ads; April 2026 Stagwell partnership tests Axon on agency CTV spend |
| **Axon Ads Manager** | AppLovin | Self-serve e-commerce DSP with Shopify direct plugin, Dynamic Product Ads, piloted GenAI creative tools | Move from sales-led DTC onboarding to platform-led e-commerce | Referral-only launch October 1, 2025; GA targeted H1 2026; 57% go-live conversion rate; $10K → $1B run-rate in 12 months |
| **Vector** | Unity | ML-based predictive UA targeting; launched Q4 2024, built internally (not ironSource legacy) | Counter AXON on demand-side for gaming UA | +53% growth; on pace $1B+ run rate; +15–25% ARPDAU lift in early tests (below AXON's +40–60%) |
| **LevelPlay** | Unity / ironSource | Bidding-era mediation platform; ~10–12% rev-share on publisher earnings | Gaming-adjacent to Unity engine integration | Losing share to MAX post-2022 merger pain; stronger in small/mid-cap studios than professional publishers |
| **AdMob** | Google | Google Ads demand aggregation + real-time bidding mediation | Fill rate + Android-ecosystem dominance | Highest fill rates due to Google Ads demand; strong on top-download iOS; weak on performance ROI rankings |
| **Audience Network** | Meta | Off-Meta inventory fill from Meta's ad demand; reliant on Meta's social graph for targeting | Extend Meta advertiser reach outside walled garden | Structurally damaged by ATT; "Chained Ads" January 2026 spike showed latent capability but no durable recovery; Advantage+ AI creative automation ($60B run rate) is the more relevant Meta vehicle |
| **Cortex (Liftoff)** | Liftoff / Blackstone | Neural-net bidding + creative optimization across 140K+ apps, 1.4B DAU reach | Performance UA DSP | Blackstone-backed roll-up; General Atlantic minority at $4.3B (May 2025); IPO refiled April 17 2026 targeting up to $5.17B valuation, $762M raise, $686M FY25 revenue — the largest ad-tech IPO filing since 2021 |
| **Moloco Ads** | Moloco | ML-first DSP; APAC strength; "Commerce Media" product for retail DSP as-a-service | Performance UA outside walled gardens | #5 AppsFlyer Performance Index Q1 2026; 904 employees; Fidelity + Tiger Global backed; IPO talks reported January 2026 |
| **CloudX** | CloudX | SDK-less "monetization as code"; Anthropic Claude-orchestrated AI agents for SDK integration, ad formats, line items; Trusted Execution Environments for auction transparency | Federated-learning/mid-tier alternative to AXON-scale capex | Launched GA February 4 2026 with seven bidders (Meta, Unity, Liftoff, Magnite, InMobi, Mintegral, Moloco); $30M Series A led by Addition; no named major publisher migration from MAX as of April 2026 |
| **SingleTap / Ignite** | Digital Turbine | On-device pre-install via carrier partnerships; ~500M device footprint | Alternative app distribution bypassing App Stores | Three of top-10 global mobile game developers signed December 2025; defensible niche but sub-scale |
| **Chartboost** | Take-Two / Zynga | Gaming-native cross-promo + direct-deals platform | Captive adtech for Take-Two's mobile portfolio | Absorbed into Zynga (Aug 2021 $250M) → Take-Two (Jan 2022 $12.7B); no longer independent market force |

## Acquisitions and new entrants

**The defining acquisitions of the ATT era were AppLovin's three-deal stack: Adjust (April 2021, ~$1B; measurement), MoPub (January 2022 close, $1.05B; mediation), and Wurl (February 2022, $430M; CTV).** Together they cost ~$2.5B and created a vertically integrated software platform that today generates $4B+ annual FCF at 82% EBITDA margin. The MoPub deal is the most strategically consequential ad-tech acquisition of the decade — AppLovin paid ~$1.05B for what had been purchased for $350M in 2013, then sunset the platform and forced 90 days of migration to MAX, capturing the information asymmetry moat that now underpins AXON. The **Tripledot divestiture** (closed June 30 2025, $400M cash + ~20% equity of Tripledot, headline $800M including equity for 10 gaming studios) completed AppLovin's pure-play transformation.

**The Unity–ironSource merger (closed November 2022, $4.4B all-stock) is the cautionary tale** — Unity's board rejected AppLovin's $17.54B counter, then absorbed ironSource as AppLovin paid $1.05B for MoPub and captured the real strategic prize. Unity's subsequent runtime-fee rollback (January 2024), 25% workforce cut ($214M cost), and 15% US-advertiser defection cost Unity both its performance edge and developer trust. **Digital Turbine's $1B+ 2021 roll-up (Fyber $600M, AdColony $400M, Appreciate) is the second cautionary tale** — carrier-channel and DSP/SSP/on-device integration complexity collapsed the investment thesis; stock fell ~96% from 2021 peak. **Chartboost → Zynga → Take-Two** shows the path of an ad-tech asset absorbed into a gaming captive, no longer independent.

**Current new-entrant threats cluster around three architectures:**

1. **SDK-less / agentic AI (CloudX)** — Launched February 2026 by the original MoPub and MAX founder (Jim Payne). Uses Anthropic's Claude to orchestrate agents that manage line items, ad-format testing, and SDK integration in 15 minutes. Seven bidders at GA. No named MAX publisher migration through April 2026. Historical SDK-less bidding attempts have failed, but Payne's insider knowledge of mediation-stack friction makes this the most credible architectural challenge AppLovin has faced. SEC identifier-bridging probe implicitly validates the "transparency-native" pitch.

2. **ML-native DSPs (Moloco, Liftoff Cortex)** — Moloco's rise from #15 to #5 in the AppsFlyer Performance Index is the fastest independent DSP climb on record. Liftoff's April 2026 IPO refile at $5.17B target valuation on $686M revenue = **~7.5x P/S** — if it prices there, it sets the comparable benchmark for Moloco's likely 2026 IPO. Both participate inside MAX as bidders, constraining structural threat but raising demand-side competitive intensity.

3. **AI-chat monetization (OpenAI/ChatGPT)** — ChatGPT Ads launched February 9 2026 (US Free tier + Go plan); passed **$100M annualized revenue** within first two months. StackAdapt DSP courting advertisers at $15–60 CPMs, $50K minimums. This is the first genuinely new attention surface since TikTok, and it threatens mobile ad-tech indirectly by pulling time-spent away from social/gaming apps.

Retail media convergence (**Amazon Ads $56B 2024, +18% YoY, ~$69B run rate**) threatens mobile ad-tech asymmetrically — it pulls commerce advertiser budgets from performance-mobile to retail media but complements gaming publishers without Amazon inventory.

## Macro shifts

1. **Privacy-Sandbox reversal (October 2025) removes the Damocles sword**. Google officially retired the entire Privacy Sandbox project after six years; third-party cookies stay in Chrome indefinitely (April 22 2025 decision). Only CHIPS / FedCM / Private State Tokens survive as privacy primitives — no targeting replacements. Implication: the walled-garden identity graph is not being dismantled by the Android ecosystem. The ATT/IDFA asymmetry between iOS (broken) and Android (intact) widens, favoring whichever platform scales identity-graph + AI-creative fastest on Android. Meta and Google are both structurally better-positioned post-Sandbox-death than pre-.

2. **EU DMA enforcement accelerating (2026)** — Preliminary findings against Google on data access April 2026; final Google decision expected July 27 2026. Meta implemented January 2026 consent choice; non-compliance risk is 5% daily global revenue fines. Commission pegs collective gatekeeper exposure for Apple/Google/Meta/Amazon/Microsoft at **€100B+**. Fragmentation pressure on global ad stacks — regulatory arbitrage between EU/US becomes material.

3. **Generative AI ad creative automation** — Meta Advantage+ run-rate tripled in 7 months to $60B (October 2025); Google Gemini Marketing Platform integration unveiled at NewFront 2026; AppLovin GenAI creative pilot with 100+ advertisers targets the 57% go-live bottleneck. **The creative-agency layer is compressing**, and platforms with proprietary first-party data (MAX telemetry, Meta's social graph) have the highest retraining velocity.

4. **Mobile gaming saturation — attention, not supply, is the constraint**. Global mobile gaming ~$307B in 2025; IAP 77% of consumer spend; user-acquisition spend $25B in 2025. **Downloads fell 7% to 49B installs in 2024** while impressions rose 20% (AI creative glut). Paid installs grew 10% despite fewer total installs — the bifurcation favors platforms that can extract more revenue per declining install (the Efficiency Paradox that AXON's +72–75% RPI exemplifies).

5. **TikTok divestiture closed January 22, 2026** — US operations transferred to TikTok USDS Joint Venture LLC (Oracle/Silver Lake/MGX as primary managing partners; ByteDance retains 19.9% below legal threshold; algorithm licensed and retrained via Oracle cloud). Mintegral (Chinese-owned) operates with residual geopolitical overhang; Mobvista parent weighs Mintegral sale (Bain Capital reportedly interested).

6. **SEC Cyber and Emerging Technologies Unit precedent** — The October 2025 AppLovin probe into alleged "identifier bridging" (harvesting user IDs from Meta/Snap/TikTok/Reddit/Google to stitch cross-platform profiles violating platform TOS) sets the regulatory template. A structural limit on cross-platform identifier bridging would hit AppLovin, Moloco, and Liftoff symmetrically — a *relative* win for walled gardens (Meta, Google) that don't need to bridge because they own the identity graph outright.

7. **Interest-rate regime** — 2022–2024 tightening compressed ad-tech multiples broadly; only pure-play leaders (AppLovin, TTD pre-2026) recovered. 2026 softer rate environment favors growth re-rating in names that can demonstrate margin and FCF durability.

8. **CTV / mobile convergence** — ~$30B+ CTV ad market; Netflix/Disney+/Roku/Amazon Prime ads layer; Wurl gives AppLovin a CTV beachhead but TTD is incumbent. Magnite CTV >50% of revenue, PubMatic CTV >50% growth — mid-cap SSPs offer pure-play CTV exposure at fractions of APP/TTD multiples.

## Investor heuristics

**Consensus is priced for AppLovin-as-AI-software-infrastructure at mid-30s forward P/E, but the narrative has cracked.** APP fell from ATH $745 (Sep 2025) to ~$411 (April 2026), a ~45% drawdown. Sell-side is bruised but not broken: 24 Buy / 4 Hold / 0 Sell of 36 covering analysts; median PT $655, range $340 (Hedgeye short) to $860 (Jefferies); Benchmark "2026 Top Idea" at $775; Wells Fargo cut Feb 13 2026 from $735 → $543. **No Sell ratings despite the 45% drawdown is notable** — this is a classic divergence setup where sell-side anchors on the AI-infrastructure multiple while buyside trims. Institutional ownership fell 13% from December 2024; Whale Rock holds but retail is the marginal long.

**Three non-consensus insights:**

1. **"Post-ATT winner" is cyclical, not structural** — The consensus stratifies winners (AppLovin, Moloco) vs losers (Meta, Google) on ATT exposure. But Meta's Advantage+ AI creative automation tripled to $60B run rate in 7 months, and eMarketer projects Meta overtaking Google in 2026 worldwide ad revenue. **The walled-garden recovery is further along than AppLovin's multiple implies, and Privacy-Sandbox death (Oct 2025) entrenches Google/Meta identity-graph value** rather than dismantling it. AppLovin's widest AXON lead was 2023–2024; the gap is compressing in 2026, not expanding.

2. **Mediation ≠ demand-side moat** — Consensus conflates MAX dominance (~60% mediation) with AXON demand-side dominance. The MoPub-absorbed information asymmetry is a durable structural moat; AXON's algorithmic lead is not. Unity Vector's $1B run-rate trajectory, Moloco's #5 AppsFlyer rise, CloudX's SDK-less architecture, and Meta's Chained Ads all attack the demand-side where AXON's lead is narrowing. **If the SEC forces AppLovin off identifier bridging, the MAX moat holds but AXON's delta compresses** — and the stock de-rates toward the Unity multiple (which is structural, not temporary).

3. **Liftoff's IPO prints the sector's marginal comp** — Liftoff filed April 17 2026 for up to $5.17B valuation on $686M revenue (**~7.5x P/S**). If it prices there, it establishes the benchmark for Moloco's 2026 IPO and creates a gravitational anchor for AppLovin's multiple (currently ~18x P/S on $7.5B 2026E revenue). **Sell-side treats Liftoff/Moloco IPOs as noise; they are actually the marginal-buyer repricing events for the entire sector.** TTD's 85% drawdown is the precedent — ad-tech's software-infrastructure premium compresses fast when growth decelerates and AI-disruption narratives land.

**Re-rating metrics to watch (in order of signal strength):**
- E-commerce net revenue run-rate + QoQ retention (Q1 $34M → $90M ramp; 2026 consensus $1.5B, BofA bull case $2.1B)
- MAX take-rate stability under SEC probe resolution
- Advertiser count growth (proxy for TAM expansion)
- Liftoff/Moloco IPO multiples (sector-wide comp floor)

**Historical parallel is 2022-era cloud software** — Snowflake, Datadog, MongoDB sustained 80%+ premiums during ZIRP, then compressed 50–60% as growth decelerated AND AI-disruption narratives emerged simultaneously. AppLovin is in the early innings of that compression, not the end. TTD's -85% from high is the sector's worst-case demonstration; APP's -45% is mid-compression. The asymmetric upside requires both SEC resolution AND e-commerce execution; the asymmetric downside only requires one of CloudX adoption, Meta recovery, or SEC structural finding.

## Related Research
- [[Research/2026-02-26 - APP - AppLovin AI Ad Platform Deep Dive]] — Grok deep-dive on AppLovin business model, AXON 2.0 architecture, competitive dynamics, investor sentiment
- [[Research/2026-03-09 - APP - Gemini Business Analysis Canvas]] — Gemini Canvas: AXON dominance, Tripledot divestiture, CloudX challenge, financial performance deep-dive
- [[Research/2026-03-19 - AppLovin AXON Engine Differentiation]] — Claude research on AXON differentiation, "Golden 9" competitive field, e-commerce incrementality evidence, SEC probe context

## Log
### 2026-04-22
- Initial sector note created via subsector split from [[_Archive/Sectors/Consumer & Digital]] — pending prompt-fill of sector analysis sections.
- Reordered sections: Active Theses moved to first position per Sector Template / CLAUDE.md §Sector Notes (MOC navigation goes first).
- Filled all 8 analytical sections via web research (industry history 2007–2026; competitive dynamics 2026; product-level stack; M&A + new entrants; macro shifts incl. Privacy-Sandbox death, DMA, TikTok divestiture, ChatGPT Ads; investor heuristics with three non-consensus insights). Status flipped draft → active.
