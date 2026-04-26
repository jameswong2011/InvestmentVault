---
date: 2026-04-26
tags: [macro, technology, agentic-ai, AI-agents, internet-infrastructure, payments, commerce, identity, search-disruption, x402, MCP, UCP, ACP]
status: active
source: Vault synthesis (NET, CRCL, SHOP theses; Blockchain & Stablecoins / E-commerce Infrastructure / Cybersecurity sector notes; Stablecoin Regulation macro; April 2026 Cloudflare / Shopify / Circle product launches)
---

# The Agentic Internet

## Thesis

The internet is being rebuilt around a non-human user. AI agents — autonomous programs acting on behalf of humans — already account for the majority of new traffic at the edge (416B AI bot requests blocked by Cloudflare in 5 months; weekly agent requests doubled in January 2026 alone; 75M+ x402 transactions in 3 months at 99% USDC settlement; AI-driven Shopify orders +15x in 2025). The architecture invented for humans clicking pages — cookies, session tokens, ad-supported content, form-based checkout, card networks with chargebacks, captchas — does not survive contact with agents that visit 1,000x more sites, traverse APIs not pages, can't pass KYC, and need atomic-settled programmable money. This is not a 2027 forecast — it is a 2026 empirical category with measurable commercial volume across edge networks, payment rails, merchant platforms, and server silicon.

The transformation reorganizes the internet around three new principles: (1) **machine identity** replaces human identity as the unit of trust, (2) **API-first protocols** replace page-rendered HTML as the unit of interaction, and (3) **programmable money** replaces card-based payment as the unit of value transfer. Each principle changes who builds, who pays, who monetizes, and how. Mainstream consumer agent autonomy for purchases is likely 2027-2029; B2B agent autonomy for procurement and workflow is likely 2027-2028; the deep transformation (search ad-model collapse, aggregator disintermediation, end of seat-based SaaS, inter-agent commerce) compounds across 2028-2035.

## What the agentic internet is

The "agentic internet" describes the structural shift from internet-as-document-network to internet-as-action-network. Eight concrete differences from the human web:

| Dimension | Human web | Agentic web |
|---|---|---|
| **Primary user** | Human via browser | Software agent acting under delegation |
| **Interaction surface** | HTML page rendered for human eye | API or structured data return for agent ingestion |
| **Discovery** | Search → blue links → page visit → eyeball impression | Direct API traversal; 50-200 sources per task vs. 3-5 |
| **Identity** | Cookie + session + occasional KYC | Cryptographic attestation + delegated authority + revocable scope |
| **Payment** | Card with chargeback infrastructure | Atomic stablecoin settlement; programmable conditionality |
| **Monetization** | Display advertising on rendered pages | Pay-per-call / pay-per-crawl / data licensing / consumption pricing |
| **Trust model** | Brand reputation + visual cues + reviews | Cryptographic provenance + agent reputation + on-chain history |
| **Latency tolerance** | Seconds (human reads) | Sub-second (agent waits cost real compute) |

The substitution is not "humans use AI to browse faster." It is humans delegating outcomes to agents that construct their own multi-step traversal of an internet built for them. Four scope tiers describe the trajectory:

1. **Tier 1 — Augmented browsing (today, 2024-2026).** Human asks a chat interface a question; the model returns synthesized text. The agent does not transact. Examples: ChatGPT, Perplexity, Claude. Volume meaningful, transactional impact limited.
2. **Tier 2 — Delegated research and micro-purchase (now, 2026-2028).** Human delegates a constrained task with explicit budget and approval. Agent executes within scope. Examples: ChatGPT Instant Checkout (1M Shopify merchants live), Sidekick on Shopify, agent-driven travel research that hands off to human for booking.
3. **Tier 3 — Persistent autonomous agents (emerging, 2027-2030).** Agents run continuously on behalf of a principal — managing subscriptions, monitoring deals, reordering household goods, executing standing rules. Trust threshold materially higher; requires both reliability gains and an identity/attestation/dispute infrastructure that does not yet exist at consumer scale.
4. **Tier 4 — Inter-agent economy (2030+).** Agents transact with other agents without human-in-loop for negotiation, contracting, or payment. The architecture invented for humans (chargebacks, dispute resolution, brand trust) breaks completely; the new architecture (cryptographic agent identity, on-chain reputation, programmable contracts) becomes load-bearing. Entirely new commerce categories become viable: per-second leasing, micro-licensing, agent-aggregated demand.

## Why now: the empirical case (April 2026 data)

The "agentic internet" stopped being a forecast in 2025 and became a measurable category in 2026. Six leading indicators:

| Signal | Data point | Source |
|---|---|---|
| Edge bot traffic inflection | 416B AI bot requests blocked at Cloudflare in 5 months; weekly AI-agent requests **doubled in January 2026 alone** | [[Theses/NET - Cloudflare]] §Insight #2 |
| Agent-to-site fanout ratio | AI agents visit **~1,000x more sites than humans** per task; competitive price research touches 50-200 URLs vs. a human's 3-5 | [[Theses/NET - Cloudflare]] §Insight #2 |
| Agent payment volume | 75M+ x402 transactions on Base + Solana since early 2026; 99% USDC settlement; Linux Foundation governance with Coinbase, Google, AWS, Microsoft, Stripe, Visa, Mastercard, Cloudflare as founding members | [[Theses/CRCL - Circle Internet Group]] §Insight #3 |
| AI commerce orders | AI-driven order volume on Shopify **+15x in 2025**; 1M+ merchants live on ChatGPT Instant Checkout (ACP); Agentic Storefronts (UCP) rolled out universally March 2026 | [[Theses/SHOP - Shopify]] §Insight #3 |
| Server-CPU re-pricing | CPU:GPU ratios in agentic racks **rising above 1:1**; Georgia Tech/Intel paper estimates tool-processing on CPUs accounts for **50–90% of total agentic workload latency** | [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]] |
| Per-seat SaaS pricing dislocation | ServiceNow consolidates Foundation/Advanced/Prime tiers (April 9 2026) embedding AI free in baseline; UiPath -87% from highs as RPA fails the LLM-orchestration transition | [[Sectors/Enterprise Workflow AI & Automation]] |

These are commercial-volume metrics across edge networks, payment rails, merchant platforms, server silicon, and enterprise software pricing books. The agentic internet is closer to where stablecoins were in mid-2024 (TAM measurable, infrastructure live, regulatory architecture forming) than where AR/VR has been since 2014 (always two years away).

## User adoption: where we are and where it goes

Adoption is bifurcated by user type and task. The pattern: infrastructure adoption is ahead of consumer adoption; B2B / developer adoption is ahead of consumer adoption; high-frequency / low-stakes tasks are ahead of low-frequency / high-stakes ones.

### Where adoption sits today (April 2026)

| User segment | Adoption level | Representative tasks |
|---|---|---|
| **Developers** | High and accelerating | Coding agents (Cursor, Claude Code, GitHub Copilot Workspaces); tool-orchestration via MCP (97M monthly SDK downloads by March 2026); CI/CD agents |
| **Knowledge workers (consumer surface)** | Medium and growing | ChatGPT for research, drafting, comparative analysis; Perplexity for fact-finding; Claude for long-form analysis |
| **Knowledge workers (enterprise)** | Medium-low; gated by IT | M365 Copilot, Glean enterprise search, ServiceNow agents; deployment-led not user-led |
| **Consumers — research / discovery** | Medium | Pre-purchase research via ChatGPT/Perplexity; recipe and travel ideation; restaurant discovery |
| **Consumers — transactional** | Low but inflecting | ChatGPT Instant Checkout (1M Shopify merchants), Shopify Sidekick assisted purchases; agent-driven order growth +15x on small base |
| **Small business operators** | Medium | Shopify Sidekick for store management; agent-drafted emails / customer service responses |
| **Enterprise procurement** | Low | Pilots only; multi-stakeholder approval and audit requirements unmet |
| **Regulated industries (finance, healthcare, legal)** | Very low | Reliability gap (>30% multi-step failure rate per Carnegie Mellon) blocks production deployment for high-stakes decisions |

### The four-phase adoption cascade

**Phase 1 — Tool-use plateau (2024-2026, in progress).** Agents reliably execute single-purpose tasks (one search, one summary, one code completion). Consumer interaction is chat-mediated. Commercial volume ahead of consumer mindshare; most consumers do not realize how much of their software interaction is already agent-mediated (M365 Copilot, Gmail Smart Compose, code completion).

**Phase 2 — Delegated multi-step (2026-2028, beginning).** Agents complete multi-step tasks within bounded scope. ChatGPT Instant Checkout is the canonical case — user describes intent, agent constructs cart across merchants, presents for one-click confirmation. Consumer trust threshold today is "I will let it spend $50 on a known item from a known merchant"; the gap to "$500 on novel item from unknown merchant" is large.

**Phase 3 — Persistent autonomous (2028-2030, projected).** Agents run continuously without per-action approval. Examples: monitor flight prices and rebook automatically; reorder household goods on inferred schedule; manage subscriptions; execute standing rules ("if my electricity rate exceeds X, switch providers"). Requires (a) persistent memory of preferences, (b) revocable cryptographic delegation, (c) dispute infrastructure analogous to credit-card chargebacks. None solved at consumer scale today.

**Phase 4 — Agent-to-agent (2030+, projected).** B2B agents negotiate with B2B agents (procurement bot ↔ vendor bot) without human approval per transaction. Consumer-side, agents in different households coordinate (rideshare pooling, group purchasing). The unit economics of human transaction overhead disappear; entirely new commerce categories become viable (per-second leasing, micro-licensing, agent-aggregated demand).

### What unlocks each phase

| Phase | Key unlock | Status (April 2026) |
|---|---|---|
| Phase 1 → 2 | Frontier-model tool-use reliability >80% on multi-step + consumer payment delegation infrastructure | Reliability ~65-70% on best models; payment infra (Instant Checkout, Sidekick) live |
| Phase 2 → 3 | Sub-30% error rate on persistent tasks + revocable cryptographic identity at scale + chargeback-equivalent dispute system | Reliability gap material; identity layer green-field (no Visa-equivalent); dispute system unbuilt |
| Phase 3 → 4 | Inter-agent reputation / attestation standards + sub-cent micropayment rails at scale + regulatory clarity for autonomous transactions | Web Bot Auth + x402 are early prototypes; regulatory clarity 2026-2028 horizon |

The honest read: Phase 1 is fully here, Phase 2 is in early commercial rollout, Phase 3 requires multiple infrastructure layers that do not yet exist, Phase 4 is conceptual. The investable thesis spans Phases 1-3; the speculative upside spans Phase 4.

## Hurdles remaining

Six structural barriers between today's commercial volume and mainstream Phase 3 adoption.

### 1. Reliability ceiling

Frontier agents fail at multi-step tasks at 30-65% rate (Carnegie Mellon benchmarks; SWE-bench Pro <20% on private codebases). For consumer trust, the failure rate has to drop into single digits for transactions involving real money. Token deflation (~86% annual inference cost reduction) helps the cost side but not the reliability side directly — that requires architectural improvement (better grounding, better tool-use, better memory). The bear case: reliability plateaus and Phase 3 stalls. The bull case: capability gains compound model-by-model and reliability hits the threshold by 2027-2028.

### 2. Identity and attestation infrastructure

There is no "OKTA for agents" yet, no "Visa for agents," no consumer-facing dispute system. An agent that spends $200 on the wrong item has no equivalent of a chargeback. The architectural problem is hard: agents act under delegated authority that must be cryptographically verifiable, revocable, and rate-limited; the principal must have audit rights; merchants must have liability frameworks. Web Bot Auth, V/MA agent commerce protocols, and Cloudflare's NET Dollar are early prototypes; consumer-grade infrastructure is 2-3 years out.

### 3. Trust gap at the consumer layer

Even if reliability and identity are solved technically, consumers may not delegate spending authority. The 2026 consumer reality: most users will let an agent suggest, but want to approve every purchase. Crossing into autonomous spending requires (a) a track record of low error rates, (b) a known recourse system, (c) cultural normalization. Online banking took ~10 years (1995-2005) to cross from early adopters to majority adoption; agent-mediated spending may track a similar curve.

### 4. Regulatory architecture

Agent transactions stress-test KYC, fiduciary duty, chargeback law, advertising regulation (FTC), securities law (SEC), payment regulation (CFPB), and consumer protection. The current GENIUS Act (US stablecoin) and MiCA (EU) provide payment-rail clarity but don't address autonomous agent decision-making. Two scenarios: (a) regulators establish workable frameworks by 2027-2028 accepting some autonomous agent action with human accountability; (b) regulators impose human-in-loop requirements on every transaction above a threshold, which caps Phase 3 adoption indefinitely.

### 5. Publisher / website crawler revolt

If publishers mass-deploy paywalls, captchas, and pay-per-crawl on every site, the cost of agent traversal rises and the agent's ability to discover information narrows. The 2nd-order effect could *accelerate* the agent-payment economy (every crawl becomes a micro-transaction), but the 1st-order effect is friction that constrains Phase 1-2 utility. Cloudflare's pay-per-crawl is the cleanest current implementation; whether it becomes a healthy two-sided market or a wall depends on price discovery in 2026-2027.

### 6. Compute economics for high-frequency agent action

A persistent agent doing 100 inference calls per task at $0.001-$0.01 per call costs $0.10-$1.00 per task. For high-frequency low-value actions (every-page price check, every-listing comparison), this exceeds the value extracted. Token deflation is solving this on a steep curve, but the infrastructure for sub-cent action economics requires both inference cost reduction AND payment-rail efficiency at micro-scale (which x402 / USDC delivers but card networks do not).

## What 10-20 years out looks like

Forward projection assumes Phase 3 reaches majority consumer adoption by ~2032 and Phase 4 begins reaching scale by ~2035. The end-state internet differs structurally from today's.

### The structural shifts

**Discovery is API-first, not page-first.** Most commercial discovery happens through agent traversal of structured product/service feeds. The "website" survives as an authoritative source for brand identity and human inspection but is no longer the primary commerce surface. Search engines (Google, Bing) are partially replaced by frontier-model query interfaces; the residual search use case is provenance ("show me the source") not discovery ("what should I buy"). Display advertising shrinks 50-70% from 2025 levels in real terms; the surplus advertising spend redirects to (a) sponsored content inside agent responses, (b) data licensing fees, (c) paid placement in agent-curated catalogs.

**Money is programmable by default.** Stablecoin settlement is the underlying rail for the majority of internet transactions <$500. Card networks survive but reposition as identity / dispute / loyalty layers atop stablecoin settlement (the Visa B2B Connect / Mastercard Move pattern generalizes). Sub-cent transactions become economic for the first time, enabling new content models (per-article, per-API-call, per-second-of-attention pricing). Cross-border B2B settles in minutes for transparent fees vs. today's 3-5 days at 2.5-5% all-in cost.

**Agents have identity, reputation, and accountability.** Every agent operates under cryptographic attestation tied to a human or corporate principal. Reputation systems (the "Visa for agents" that does not exist today) enable agent-to-agent trust at scale. Disputes are arbitrated through on-chain mechanisms with human appeal — the equivalent of small-claims court for autonomous agent actions. New regulatory bodies emerge to oversee the agent economy.

**The labor / SaaS economy reorganizes.** Per-seat SaaS pricing dies for any category where agent-based execution is feasible — the 1:5 seat-compression ratio cited in [[Sectors/Enterprise Workflow AI & Automation]] becomes the norm, not the bear case. Software pricing migrates to consumption (per-action, per-token, per-decision) or outcomes (per-resolved-ticket, per-closed-deal). Knowledge work that decomposes into agent-doable subtasks shifts to agent execution with human review; jobs that survive require physical presence, executive judgment, or relationship management.

**Aggregators are disintermediated, marketplaces persist conditionally.** Pure-aggregator businesses (Booking, Expedia, comparison-shopping engines) compress materially because agents do their function natively for free. Marketplaces with strong supply-side moats (Amazon's logistics, Uber's network density, Shopify's merchant tools) survive by becoming agent-friendly fulfillment layers under a new discovery layer. The economic value of "discovery + curation" migrates from incumbent aggregators to whichever agent platforms users entrust with their delegation.

**A new browser-equivalent emerges.** The "browser" of the agentic internet is the agent runtime — the environment where agents execute on behalf of a principal. Today this lives inside chat interfaces (ChatGPT, Claude, Perplexity); by 2030-2035 it is more likely a dedicated OS-level surface (Apple Intelligence, Microsoft Copilot OS layer, ChromeOS-equivalent for agents). Whoever owns that runtime captures distribution analogous to what browsers captured in the 1995-2005 web.

### The investable categories at maturity

| Category | Function | Today's prototypes | Mature-state economics |
|---|---|---|---|
| Edge interception | Toll on agent-to-internet traffic | Cloudflare | High-margin infrastructure rent; oligopoly of 2-3 players globally |
| Programmable money issuance | Stablecoin float + transaction fees | Circle (USDC), Tether, PYUSD | Bank-like spread economics + transaction-fee layer; regulated handful |
| Commerce protocol stewardship | Merchant-side protocol adoption | Shopify (UCP+ACP), Stripe (ACP) | Network-effect platform economics; merchant-share captures value |
| Agent runtime / OS | Where agents execute on behalf of principals | OpenAI, Anthropic, Microsoft, Apple, Google | Distribution oligopoly analogous to mobile OS (2-3 players) |
| Agent identity & reputation | Verifiable provenance + recourse | Web Bot Auth, V/MA agent protocols | New category; current incumbents (Okta, Visa) have first claim but uncaptured |
| Compute fanout | Inference, memory, networking, storage | NVDA, AMD, AVGO, hyperscalers | Continued dominant compute spend; CPU/GPU/storage/photonic blend reflects agent workload mix |
| Content & data licensing | Provenance-attributed access for agent training and retrieval | Reddit, Cloudflare Human Native, Tollbit | New revenue category; partial replacement of display ad model |

### Failure modes for the 10-20 year vision

1. Reliability never crosses the trust threshold for autonomous spending — Phase 3 stalls; commercial impact remains in research and assistance only.
2. Regulators impose human-in-loop requirements on every agent transaction — agent commerce reverts to assisted browsing.
3. A platform monopolist (most likely Microsoft or Google) absorbs the agent runtime layer end-to-end and prices the rest of the stack out — pure-play infrastructure plays become commodities.
4. Hard recession in 2026-2028 compresses enterprise software budgets and consumer discretionary, stretching the inflection from 2027-2029 to 2032-2034 — interim valuations destroy even if long-term thesis holds.

## The eight-layer stack (compressed reference)

The agentic internet decomposes into eight layers. Detailed treatment of layers 1, 4, and 5 (where NET, SHOP, CRCL play) is in §Impact on NET / CRCL / SHOP below. Other layers in summary:

| Layer | Function | Key dynamic | Vault wikilink anchor |
|---|---|---|---|
| **1. Traffic interception** | Toll on agent-to-internet traffic at the edge | NET dominant; AKAM disrupted; VRSN beneficiary via DNS query growth | [[Theses/NET - Cloudflare]] |
| **2. Identity & attestation** | Cryptographic agent identity, delegated authority, revocable scope | Green-field; OKTA candidate; hyperscaler bundle risk (Microsoft Entra) | OKTA, [[Theses/NET - Cloudflare]] (Web Bot Auth) |
| **3. Discovery & search** | How agents find products / data / services | Search ad-model breaks; Google bear, Microsoft bull, BKNG/EXPE textbook disintermediation | [[Theses/META - Meta]], [[Theses/APP - AppLovin]] |
| **4. Commerce protocol** | Standards for agent-to-merchant transaction (UCP, ACP, MCP) | Dual-protocol merchants capture +40% agentic traffic; SHOP pure-play | [[Theses/SHOP - Shopify]] |
| **5. Payments & settlement** | Programmable money, atomic settlement, micropayments | Stablecoin <$25 displaces card; CRCL 99% x402; V/MA reposition as identity layer | [[Theses/CRCL - Circle Internet Group]] |
| **6. Compute fanout** | Silicon TAM expansion from agent action multiplication | NVDA Vera CPU + Rubin GPU; AMD Venice Dense; AVGO custom; photonic interconnect | [[Theses/NVDA - Nvidia]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], [[Theses/PSTG - Pure Storage]], [[Theses/SNDK - SanDisk]], [[Theses/LITE - Lumentum]], [[Theses/IQE - IQE]], [[Theses/MRVL - Marvell Technology]] |
| **7. Data & context** | Operational data, vector DBs, ontology, write-back, content licensing | PLTR Ontology = agent-safe write-back; Snowflake/MDB picks-and-shovels; Reddit data licensing | [[Theses/PLTR - Palantir]], [[Theses/NOW - ServiceNow]] |
| **8. Cybersecurity** | Prompt injection, agent identity spoofing, agent-to-agent fraud | New attack categories; PANW platform consolidation; CRWD endpoint; NET network-layer | [[Theses/PANW - Palo Alto Networks]], [[Theses/CRWD - CrowdStrike Holdings]] |

The compute layer (6) is the highest-confidence beneficiary — every other layer is a competitive battle, but more agents = more compute regardless of which agent platform / payment rail / commerce protocol wins.

## Impact on NET, CRCL, SHOP

These three vault names have the most direct agentic-internet exposure. Each plays a different layer; together they form a diversified expression of the thesis.

### NET — Cloudflare (layers 1, 2, 5, 8)

Cloudflare is the only single vendor active across four layers. The structural position:

- **Layer 1 (interception).** ~20% of all web traffic proxied through Cloudflare's 330+ city anycast network. Every agent request to a Cloudflare-protected origin is observable, identifiable, and rate-limitable at the edge. AI bot identification (Web Bot Auth) is live as of April 2026; pay-per-crawl monetization is an entirely new revenue line with no incumbent. Per [[Theses/NET - Cloudflare]] §Insight #2, weekly AI-agent requests doubled in January 2026 — a step-function not yet priced into consensus traffic projections.
- **Layer 2 (identity).** Web Bot Auth + Workers + NET Dollar gives Cloudflare the unique ability to do agent attestation + payment + execution in a single Cloudflare-hosted flow. Green-field expansion no competitor can replicate without similar traffic position. The risk is hyperscaler absorption — Microsoft Entra Agent ID could foreclose enterprise identity even if Cloudflare wins consumer / web.
- **Layer 5 (NET Dollar).** Cloudflare's own stablecoin creates payment-at-the-edge with no settlement intermediary. Per [[Theses/NET - Cloudflare]] §Insight #5, this is genuinely novel revenue with no competitor able to build it from a standing start. Adoption depends on developer + agent-platform integration; if NET Dollar becomes a default settlement option for x402-compatible agents, it captures non-trivial share of the agent payment volume that today defaults to USDC.
- **Layer 8 (security).** Firewall for AI, Web Bot Auth bot management, agent-aware DDoS protection. Every agent deployment expands Cloudflare's addressable security spend at the network layer.

**What to watch (NET):** Q2/Q3 2026 Agent Cloud adoption metrics; pay-per-crawl revenue disclosure; NET Dollar transaction volume; whether Microsoft / Google deploy aggressive edge compute (the chokepoint compression risk). Bull case requires Cloudflare retaining >15% web traffic share AND capturing meaningful agent-attestation share AND NET Dollar reaching $1B+ annual transaction volume by 2027. Base case requires only the first two; pay-per-crawl alone justifies the multiple expansion.

**What it means for the agent thesis:** NET is the cleanest single-equity expression of the toll-collector position. If the agent economy generates the volume implied by current adoption curves, NET captures rent at the chokepoint regardless of which agent platform / payment rail / commerce protocol wins. The pay-per-crawl + Web Bot Auth + NET Dollar stack is also the most plausible vault answer to "what replaces display advertising as the discovery-layer monetization model?"

### CRCL — Circle Internet Group (layers 5, 2)

Circle is the programmable-money issuer for the agent economy. The structural position:

- **Layer 5 (settlement).** 99% of x402 agent payment volume settles in USDC. CPN (Circle Payments Network) launched April 8, 2026 with Santander / Deutsche Bank / SocGen / StanChart — the cross-border B2B agent-payment rail. Per [[Theses/CRCL - Circle Internet Group]] §Insight #3, x402 revenue bypasses Coinbase distribution entirely (50-60% higher gross margin per dollar of agent volume). Sector context: [[Sectors/Blockchain & Stablecoins]] §6 estimates ~$70B agent-payment TAM at 5% of e-commerce by 2030.
- **Layer 2 (wallet as identity).** Programmable Wallets become the de-facto agent wallet for x402 settlement. Identity rides on the wallet — every agent has a wallet, every wallet has cryptographic provenance, every transaction has an audit trail. The closest current implementation of "agent identity tied to payment authority."

**What to watch (CRCL):** Q1 2026 earnings (May 11) — CPN volume disclosure, x402 adoption metrics, whether fee-based revenue scales fast enough to offset reserve income exposure to falling rates. The August 2026 Coinbase revenue-sharing renegotiation is the single largest binary catalyst; the agent-payment volume is the structural offset that justifies a higher base case if interest income compresses.

**What it means for the agent thesis:** CRCL is the cleanest pure-play on programmable money as the agent-payment substrate. The economics are levered to two variables: (a) what share of agent commerce settles in stablecoin vs. card (today 99% on x402, materially lower on retail-size agent purchases that still use cards), and (b) what share of stablecoin agent payments settle in USDC vs. PYUSD / RLUSD / NET Dollar. Bull case requires both variables to stay favorable through a multi-year ramp; bear case is share erosion to a hyperscaler-issued or merchant-issued stablecoin.

### SHOP — Shopify (layer 4)

Shopify is the merchant-side protocol consolidator. The structural position:

- **Layer 4 (commerce protocol).** SHOP merchants stacked on both UCP (Universal Commerce Protocol — Google + Walmart + Target consortium) and ACP (Agentic Commerce Protocol — Stripe + OpenAI) capture **40% more agentic traffic** than single-protocol stores per [[Theses/SHOP - Shopify]] §Insight #3. 1M+ merchants live on ChatGPT Instant Checkout; Agentic Storefronts (UCP) rolled out universally March 2026. Sidekick is the merchant-side agent for store management; Shop is the consumer-side agent for shopping.
- **Adjacent layers.** Shopify Pay + the Stripe integration give SHOP optionality on the payment layer; Shop App as a consumer surface gives SHOP optionality on the discovery layer. Neither is the primary thesis but both reduce the risk of being squeezed out at the merchant interface.

**What to watch (SHOP):** Q1 2026 earnings — AI-driven order GMV disclosure (the +15x 2025 growth needs to compound, not plateau); UCP + ACP adoption breadth (single-protocol merchants should continue migrating to dual-stack); Sidekick attach rate (proxy for merchant-side agent adoption). Structural risk: one protocol wins decisively (most likely UCP given Google + Walmart + Target distribution), reducing the value of SHOP's dual-protocol hedge.

**What it means for the agent thesis:** SHOP is the cleanest pure-play on the merchant-side capture of agent-driven commerce. Bull case: agent-mediated commerce reaches 5-10% of e-commerce GMV by 2030, with SHOP's merchant share roughly proportional to its current ~10% U.S. e-commerce share — yields a multi-billion-dollar incremental revenue stream from agent-traffic-share above current trend. Bear case: protocol-wars favor a single platform (GOOG via UCP) that captures the merchant-relationship economics directly, leaving SHOP as a fulfillment back-end with compressed margins.

### How NET / CRCL / SHOP interact

The three are layered, not redundant. An agent placing an order on Shopify-via-ACP (SHOP layer 4) authenticates through Web Bot Auth at Cloudflare's edge (NET layer 1+2), pays in USDC (CRCL layer 5), with the entire flow secured by Cloudflare's Firewall for AI (NET layer 8). The same agent doing competitive price research traverses 50-200 sites (NET layer 1 traffic; CRCL pay-per-crawl micro-payments to publishers; SHOP merchant catalogs as a primary destination). Each name compounds the others' adoption — agent volume growth at any layer increases volume at every layer.

For a portfolio with all three, the diversification is by failure mode:
- **NET fails** if hyperscalers replicate the edge chokepoint (low probability near-term, real long-term risk).
- **CRCL fails** if a competing stablecoin (PYUSD, NET Dollar, hyperscaler-issued) takes share, or if interest income compresses faster than fee income scales.
- **SHOP fails** if the protocol wars resolve in favor of a single platform that captures merchant economics directly.

The probabilities are uncorrelated; the basket is structurally diversified within the agent thesis.

## Other names: compressed map

The full eight-layer winners-losers map preserved below for reference. Detail intentionally lighter than in prior versions of the note — see linked theses for full coverage.

| Ticker | Coverage | Layer(s) | Net | One-line case |
|---|---|---|---|---|
| **NVDA** | ✓ | 6 | Bull | Vera CPU + Rubin GPU agentic-flagship |
| **AMD** | ✓ | 6 | Bull | Venice Dense action-workload merchant CPU |
| **AVGO** | ✓ | 6 | Bull | Custom XPU + Tomahawk for agent racks |
| **PSTG / SNDK** | ✓ | 6, 7 | Bull | Storage I/O for agent state and context windows |
| **LITE / IQE / MRVL** | ✓ | 6 | Bull | East-west photonic interconnect for sub-agent fanout |
| **META** | ✓ | 3, 6 | Mixed-Bull | Llama as agent substrate; ad delivery to humans inside Meta surfaces |
| **PLTR** | ✓ | 7 | Bull | Ontology = agent-safe write-back substrate |
| **NOW** | ✓ | 7 | Mixed | Per-seat pricing risk vs. AI Control Tower orchestration |
| **PANW / CRWD** | ✓ | 8 | Bull | Agent attack surface = security spend uplift |
| **APP** | ✓ | 3 | Mixed-Bull | In-app ad model partially insulated from agent discovery |
| **UBER** | ✓ | 3, 4 | Mixed | "Get me a car" through agent bypasses Uber app |
| **GOOGL** | (no coverage) | 3, 6, 7 | Mixed-Bear | Search ad model breaks; Gemini + TPU partial hedge |
| **MSFT** | (no coverage) | 2, 3, 4, 6, 7, 8 | Bull | Full-stack agent platform across most layers |
| **V / MA** | (no coverage) | 5 | Mixed | Tokenization frenemies; lose interchange below $25 |
| **PYPL** | (no coverage) | 5, 4 | Mixed-Bull | PYUSD + Honey + Braintree defensive reposition |
| **BKNG / EXPE** | (no coverage) | 3 | Bear | Canonical aggregator disintermediation |
| **OKTA** | (no coverage) | 2 | Bull-optionality | Agent identity green-field; hyperscaler bundle risk |
| **AKAM** | (no coverage) | 1 | Bear | NET-disrupted CDN incumbent |
| **VRSN** | (no coverage) | 1 | Bull | DNS query growth from agent fanout |
| **RDDT** | (no coverage) | 3, 7 | Mixed-Bull | Data licensing as new revenue category |
| **SNOW / MDB** | (no coverage) | 7 | Bull | Vector DB + lakehouse picks-and-shovels |

Suggested new coverage priorities (preserved from prior version): Tier 1 — GOOGL (Search disruption bear), MSFT (full-stack agent bull), V/MA pair (tokenization frenemies). Tier 2 — BKNG (aggregator bear), PYPL (PYUSD reposition), AMZN (mixed). Tier 3 — OKTA, AKAM, VRSN, RDDT, SNOW/MDB.

## Mental models and historical analogies

Three historical parallels frame the agentic transition. None is a perfect map; each illuminates a specific dynamic.

**Mobile (2007-2014) — the platform transition.** iPhone + Android created a new computing surface in ~5 years; incumbents that defended legacy architecture (Microsoft Windows Mobile, BlackBerry, Nokia) were structurally re-rated downward. Agentic-internet parallel: ~3-5 year transition window (2025-2029) where re-platformers (NET, SHOP, MSFT) entrench and defenders of the legacy stack (BKNG, GOOGL Search, single-protocol commerce platforms) get re-rated. The asymmetry: agent re-platforming requires *exposing* APIs, not *building* new surfaces — capex is lower and speed should be faster than mobile.

**TCP/IP / commercial internet (1995-2002) — the protocol layer.** USDC is to internet-native money what TCP/IP was to internet-native communication. Same framing applies to x402, MCP, UCP/ACP. Investor implication: protocol-layer value capture is structurally harder than application-layer — TCP/IP made Cisco rich, not Vint Cerf. The "buy Cisco" of this analogy is the toll-collector (NET) and the merchant interface (SHOP), not the protocol developer (Anthropic on MCP, Coinbase on x402).

**2010s instant payment rails — the layering lesson.** SEPA Inst, FedNow, TCH RTP, PIX, UPI built domestic instant rails; cross-border remained 1970s SWIFT. CPN bridges the gap in 2026. Agent-economy parallel: cross-domain interoperability is the scarcest and most valuable layer. NET's traffic-interception position is the agent equivalent of CPN's cross-border position — connecting domains that would otherwise stay siloed. Single-domain agent platforms are SEPA / FedNow / PIX equivalents; cross-domain owners win.

## Catalysts and re-rating triggers (next 12 months)

| Catalyst | Date | Names re-rated |
|---|---|---|
| Cloudflare Q1 2026 earnings; Agent Cloud adoption metrics; pay-per-crawl revenue disclosure | May 2026 | NET |
| Circle Q1 2026 earnings (May 11); CPN volume; x402 adoption | May 2026 | CRCL |
| Shopify Q1 2026 earnings; AI-driven order GMV disclosure | May 2026 | SHOP |
| Coinbase August 2026 revenue-sharing renegotiation | August 2026 | CRCL |
| First major hyperscaler agent SDK GA → mainstream enterprise deployment | 2H 2026 | MSFT, AMZN, GOOGL |
| First publicized agent-driven cybersecurity breach (prompt injection in production) | Likely 2026 | PANW, CRWD, NET; tail risk to all agent platforms |
| Booking / Expedia disclosure of agent-mediated booking share | 2026-2027 | BKNG, EXPE |
| First $1B+ agent-platform IPO (Sierra, Adept, etc.) | 2026-2027 | Validates category; benefits NET/CRCL/SHOP indirectly |
| GENIUS Act final implementation rules (Treasury/OCC/FDIC) | July 2026 | CRCL, V, MA, PYPL |
| EU agent-governance / AI Act enforcement specifics | 2H 2026 | All EU-exposed names; potential headwind |

## Bear case: structural objections

Three coherent objections to taking this thesis at face value:

**1. The "every transformation timeline gets stretched" objection.** AR/VR has been "two years away" since 2014; metaverse since 2021; FSD since 2016. Each had infrastructure metrics that *looked* convincing in year 1 and stalled at consumer adoption for 5+ years. Agentic internet may follow the same pattern: infrastructure (NET, CRCL, SHOP) re-platforms successfully, but mainstream consumer + B2B autonomous adoption stalls at trust, regulation, reliability. **Counter:** Agent adoption is already commercial (75M x402 transactions, 1M Shopify ACP merchants, 15x AI-driven Shopify orders) — past the "real volume on real transactions" threshold AR/VR never reached.

**2. The "platform absorbs everything" objection.** Microsoft, Apple, Google, Meta absorb the agent layer into existing surfaces (Copilot, Apple Intelligence, Gemini, Meta AI). Pure-play infrastructure plays (NET, CRCL) become commodities. **Counter:** Strongest objection. Hedge is to weight toward (a) layers hyperscalers can't replicate (NET's 14-year network buildout, CRCL's regulatory moat) and (b) hyperscalers themselves (MSFT). Pure-play "agent identity green-field" thesis (OKTA) is most exposed.

**3. The "regulation kills it" objection.** Regulators impose KYC, dispute, fiduciary requirements that destroy the cost/speed advantage. Agent commerce reverts to human-mediated above any threshold that triggers scrutiny. **Counter:** GENIUS Act explicitly enables payment stablecoins; V/MA + Cloudflare + Linux Foundation x402 governance includes regulated-payment incumbents; CFPB principles compatible with agent commerce. Friction more likely to slow than block, and slowing primarily hurts disrupted incumbents (BKNG, GOOGL Search).

## Trading and portfolio implications

For a portfolio with existing NET / CRCL / SHOP positions:

- **High-conviction add:** MSFT (full-stack agent platform), VRSN (under-discussed 1st-layer beneficiary).
- **Asymmetric / smaller sizing:** OKTA (agent-identity optionality), PYPL (defensive reposition with PYUSD upside), RDDT / SNOW / MDB (picks-and-shovels at data layer).
- **Pair trades:** Long NET / short AKAM; Long MA / short V.
- **Shorts / underweights:** BKNG / EXPE (aggregator disintermediation), GOOGL (until Gemini-Chrome bundle proves agent retention), per-seat SaaS exposed to seat compression.

Existing NET / CRCL / SHOP are 3 high-conviction expressions; adding MSFT and a Tier 2 short (BKNG) creates a 5-name agentic-internet basket with diversified layer exposure.

## Connections

### Direct theses (existing coverage)
- [[Theses/NET - Cloudflare]] — primary equity expression: layer-1/2/5/8 (interception + agent ID + NET Dollar + AI security)
- [[Theses/CRCL - Circle Internet Group]] — primary equity expression: layer-5 (USDC settlement, x402, CPN, Programmable Wallets)
- [[Theses/SHOP - Shopify]] — primary equity expression: layer-4 (UCP+ACP dual hedge, Sidekick, Agentic Storefronts)
- [[Theses/NVDA - Nvidia]] — layer-6 compute; Vera CPU agentic-flagship
- [[Theses/AMD - Advanced Micro Devices]] — layer-6 compute; Venice Dense action-flagship
- [[Theses/AVGO - Broadcom]] — layer-6 custom silicon for agent racks
- [[Theses/PSTG - Pure Storage]] — layer-6/7 storage for agent state
- [[Theses/SNDK - SanDisk]] — layer-6 NAND demand from agent context windows
- [[Theses/META - Meta]] — layer-3/6 Llama agent substrate + 1B Meta AI MAU
- [[Theses/PLTR - Palantir]] — layer-7 Ontology as agent-safe write-back substrate
- [[Theses/NOW - ServiceNow]] — layer-7 Knowledge Graph + AI Control Tower; per-seat risk
- [[Theses/PANW - Palo Alto Networks]] — layer-8 platform consolidation
- [[Theses/CRWD - CrowdStrike Holdings]] — layer-8 endpoint agent security
- [[Theses/APP - AppLovin]] — layer-3 in-app ad insulation from agent discovery
- [[Theses/UBER - Uber]] — layer-3/4 Khosrowshahi-flagged agent disintermediation risk
- [[Theses/LITE - Lumentum]], [[Theses/IQE - IQE]], [[Theses/MRVL - Marvell Technology]] — layer-6 photonic interconnect for agent rack east-west traffic

### Sector context
- [[Sectors/Blockchain & Stablecoins]] — §6 AI-agent payments (x402); ~$70B agent-payment TAM at 5% e-commerce by 2030; Cloudflare bot-paywall as policy/identity middleware
- [[Sectors/E-commerce Infrastructure]] — UCP/ACP/MCP protocol-wars context; SHOP dual-stack positioning
- [[Sectors/Cybersecurity]] — agent attack-surface expansion; AI-powered threats
- [[Sectors/Enterprise Workflow AI & Automation]] — per-seat SaaS pricing risk; orchestration-layer contest
- [[Sectors/GPU & AI Compute Accelerators]] — agent compute fanout
- [[Sectors/NAND Memory & Storage]] — agent context window memory demand
- [[Sectors/Mobile Advertising Technology]] — in-app vs open-web agent exposure differential
- [[Sectors/Optical Networking & Photonics]] — east-west sub-agent fanout

### Macro adjacencies
- [[Stablecoin Regulation as Geopolitical Infrastructure]] — GENIUS Act / MiCA enable USDC as agent-payment substrate; yield prohibition forces fee-based infrastructure (CPN, x402, Arc)
- [[AI Bubble Risk and Semiconductor Valuations]] — agent fanout is a credible mechanism to bridge the J.P. Morgan $650B/yr threshold; CPU TAM expansion validates capex durability per [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]]

### Key research
- [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]] — Vera/Venice Dense/Diamond Rapids 9-metric scoring; CPU:GPU >1:1 in agent racks; tool-processing 50-90% of agentic latency
- [[Research/2026-04-01 - Salesforce vs ServiceNow in Agentic AI]] — orchestration-layer contest detail
- [[Research/2026-04-14 - NOW - AI Disruption Risk - deep-dive]] — AI coding tool enterprise readiness gap (45% AI-generated code with vulnerabilities, 30-35% multi-step task completion)
- [[Research/2025-12-01 - CRCL - Circle Internet Group and USDC Dynamics]] — USDC architecture for x402 settlement
- [[Research/2026-04-15 - SHOP - Comprehensive Update April 2026 - deep-dive]] — UCP/ACP protocol-wars detail
- [[Research/2026-03-31 - Cloudflare Path to Competing with Hyperscalers]] — agent-stack architecture and hyperscaler-disruption framing
- [[Research/2026-04-03 - Cloudflare Role in Telecom Edge Computing]] — agentic traffic multiplication; telecom-edge convergence

## Open Questions

1. **What does mainstream agent-mediated retail commerce actually look like at 5%+ of e-commerce GMV?** SHOP's 15x AI-driven order growth in 2025 is on a small base; the inflection from <1% to 5% requires (a) consumer trust in delegated spending, (b) workable dispute infrastructure, (c) a recognizable agent UX that crosses from ChatGPT-tab to ambient surface. None in place at consumer scale today. Best estimate: 5% by 2029-2030, 15-20% by 2032-2035.

2. **What replaces "search ad" monetization at the discovery layer if agents don't render pages?** Pay-per-crawl (Cloudflare), per-query API fees (Perplexity), data licensing (Reddit, NYT) are candidates. None scales to ~$240B Google ad revenue replacement individually. The aggregate transition is value-destructive in the short term even if it benefits specific names; the question is whether the new categories grow to fill the gap by 2032.

3. **Does the agent identity / attestation layer become a standalone investable category, or is it absorbed by hyperscalers?** OKTA is the candidate; Cloudflare's Web Bot Auth is the green-field expansion that could foreclose this. If Microsoft Entra Agent ID becomes the de-facto enterprise standard within 18 months, agent identity is structurally a Microsoft moat.

4. **Does the per-seat SaaS pricing dislocation become severe enough to invert sector multiples?** ServiceNow Foundation/Advanced/Prime tier consolidation (April 9 2026) is the first explicit acknowledgment. If the 1:5 seat-compression ratio holds, NOW / CRM / TEAM / ZM / DOCN face structural seat erosion that consumption pricing only partly offsets. The implied multiple compression is not yet priced.

5. **Does an agent-reputation / agent-fraud "Visa for agents" emerge as an investable layer?** The dispute / reputation / chargeback infrastructure for agent-mediated transactions has no incumbent. The first vendor to credibly stand this up could capture a category analogous to early Visa or PayPal. Likely candidates: Cloudflare (extension of Web Bot Auth + NET Dollar), Stripe (extension of Radar fraud), Visa/Mastercard (extension of dispute infrastructure).

6. **How does the hyperscaler-vs-toll-collector dynamic resolve?** Microsoft, AWS, Google can theoretically replicate Cloudflare's traffic interception position by deploying anycast networks. They have not, partly because edge compute economics are misaligned with their existing P&L. If a hyperscaler deploys aggressive edge compute by 2027-2028, NET's chokepoint moat narrows.

7. **Does the agentic-internet thesis survive a hard recession?** Infrastructure-buildout-ahead-of-monetization is identical to AI capex broadly. A 2026-2027 recession compressing enterprise software budgets and consumer discretionary could stretch the agent-mediated commerce inflection from 2027-2029 to 2030-2032 — a multi-year delay that destroys interim valuations even if the long-term thesis holds.

8. **What does Phase 4 (inter-agent commerce) actually enable that does not exist today?** Per-second leasing, micro-licensing, agent-aggregated demand are the speculative upside categories. None has a current commercial prototype at scale; whether they materialize into investable businesses (vs. features inside existing platforms) is the largest unknown in the 2030+ projection.

## Log

### 2026-04-26 (creation)
- Initial macro note created from vault synthesis of [[Theses/NET - Cloudflare]], [[Theses/CRCL - Circle Internet Group]], [[Theses/SHOP - Shopify]], [[Sectors/Blockchain & Stablecoins]] §6, [[Sectors/E-commerce Infrastructure]], [[Stablecoin Regulation as Geopolitical Infrastructure]], [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]]. Eight-layer stack framework. Cross-portfolio winners-losers map covers 26 names. Tier 1 new coverage: GOOGL, MSFT, V/MA. Conviction: high on infrastructure-layer winners (NET/CRCL/SHOP/MSFT), medium on consumer-adoption timeline (2027-2029 inflection).

### 2026-04-26 (refocus)
- Manual edit: reworked structure to lead with what the agentic internet means in itself rather than stock implications. Added §What the agentic internet is (definition, eight-dimension human-vs-agent web table, four-tier scope from augmented browsing → inter-agent economy). Added §User adoption (segment-by-segment status table + four-phase trajectory + per-phase unlocks). Expanded §Hurdles remaining (six structural barriers from reliability ceiling to compute economics). Added §What 10-20 years out looks like (six structural shifts + investable categories at maturity + four failure modes). Compressed eight-layer stack from per-layer prose into reference table; expanded layers 1/4/5 into dedicated NET/CRCL/SHOP impact subsections with what-to-watch and what-it-means-for-the-thesis framing for each name. Added §How NET/CRCL/SHOP interact subsection covering layered composition and uncorrelated failure modes. Compressed cross-portfolio winners/losers map to one-line table; preserved all wikilinks and Tier 1/2/3 coverage suggestions. Added Open Question #8 on Phase 4 inter-agent commerce category emergence. No analysis deleted; secondary-name detail compressed to make room for agent-itself depth.
