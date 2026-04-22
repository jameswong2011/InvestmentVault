---
type: vault-graph
date: 2026-04-21
last_graph_write: 2026-04-21T13:04:50Z
graph_mode: last
theses: 42
sectors: 13
macro: 6
research: 134
edges: 397
orphans: 15
---

# Vault Dependency Graph

> Pre-computed link map for /sync. Read this first to resolve "X changed → what needs updating?" without brute-force file traversal. Maintained exclusively by /graph (three modes: full rebuild, /graph last incremental, /graph [N] catch-up).

## Thesis Adjacency Index

Each thesis lists its sector notes, macro notes, research notes, and cross-thesis references. This is the primary lookup for propagation.

### 285A - Kioxia
- **sectors:** [[Sectors/NAND Flash & Storage]], [[Sectors/Semiconductors]]
- **macro:** —
- **cross-thesis:** [[Theses/SNDK - SanDisk]]
- **research:** [[Research/2025-11-01 - DRAM HBM Competitive Dynamics]], [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]], [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]], [[Research/2026-01-18 - SNDK - Gemini AI Investment Canvas]], [[Research/2026-03-27 - Semis - Gemini TurboQuant Memory Canvas]], [[Research/2026-03-28 - AI - Gemini AI Ecosystem Canvas]], [[Research/2026-03-31 - SanDisk Valuation Assessment]], [[Research/2026-04-15 - SNDK - Investment Evaluation]], [[Research/2026-04-16 - NAND Sector Key Questions Deep Dive - deep-dive]]
- **status:** active
- **log_tail:**
  - `2026-04-16 (NAND sector research sync) | [NAND sector creation + web research]: Three conviction-relevant findings: (1) Kioxia posted 33.1% Q…`
  - `2026-04-16 (sector key questions deep dive) | [[Research/2026-04-16 - NAND Sector Key Questions Deep Dive - deep-dive]]: CBA density advantage now…`
  - `2026-04-15 | [Thesis created]: Split from KIOXIA-SNDK archive. Consolidated ChatGPT/Gemini/Claude/web research. S…`

### AMD - Advanced Micro Devices
- **sectors:** [[Sectors/Semiconductors]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** [[Theses/285A - Kioxia]], [[Theses/AVGO - Broadcom]], [[Theses/IQE - IQE]], [[Theses/LITE - Lumentum]], [[Theses/NVDA - Nvidia]], [[Theses/SNDK - SanDisk]], [[Theses/TSM - Taiwan Semiconductor]]
- **research:** [[Research/2025-11-27 - Broadcom Data Center Opportunity]], [[Research/2026-01-15 - AI Compute and Memory Demands - HBM Shortage]], [[Research/2026-03-14 - CXL Technology Adoption]], [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]], [[Research/2026-04-19 - TSM - Stress Test]]
- **status:** active
- **log_tail:**
  - `2026-04-21 | Initial thesis created. Conviction: medium — AMD is the sole merchant full-stack Nvidia alternativ…`

### APP - AppLovin
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2026-02-26 - APP - AppLovin AI Ad Platform Deep Dive]], [[Research/2026-03-09 - APP - Gemini Business Analysis Canvas]], [[Research/2026-03-19 - AppLovin AXON Engine Differentiation]]
- **status:** active
- **log_tail:**
  - `2026-03-19 | [Claude research]: AXON differentiation, "Golden 9" competitive field, e-commerce incrementality evi…`
  - `2026-03-09 | [Gemini Canvas ingestion]: AXON dominance, CloudX challenge, financial deep-dive — conviction unch…`
  - `2026-02-26 | [Thesis created]: From Grok + ChatGPT research. Core framing: AI ad infrastructure with SEC/incremen…`

### AVGO - Broadcom
- **sectors:** [[Sectors/Semiconductors]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** [[Theses/LITE - Lumentum]], [[Theses/NVDA - Nvidia]], [[Theses/PSTG - Pure Storage]]
- **research:** [[Research/2025-11-27 - Broadcom Data Center Opportunity]], [[Research/2025-11-27 - Broadcom Equity Research Framework]], [[Research/2025-11-27 - Broadcom Ethernet Networking Position]], [[Research/2025-11-29 - AVGO - Gemini Investment Analysis Canvas]], [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]], [[Research/2026-04-19 - Huawei Ascend Roadmap - news]], [[Research/2026-04-19 - TSM - Stress Test]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | Template restructure: Renamed/repositioned Business Model section. Added framing paragraph — convi…`
  - `2026-04-14 | Major thesis restructure: Consolidated all LLM sources (Gemini, Claude, ChatGPT). Added Industry Con…`
  - `2026-04-14 (earlier) | [Gemini/ChatGPT]: Initial thesis created from Broadcom investment analysis. Hock Tan aggregation str…`

### BESI - BE Semiconductor Industries
- **sectors:** [[Sectors/Semiconductors]]
- **macro:** —
- **cross-thesis:** [[Theses/285A - Kioxia]], [[Theses/SEMICAP - Semiconductor Capital Equipment]], [[Theses/SNDK - SanDisk]]
- **research:** [[Research/2025-07-06 - BESI - Analyst Estimates and Valuation Trends]], [[Research/2025-11-01 - BESI - BESI Role in HBM Manufacturing]], [[Research/2025-11-01 - DRAM HBM Competitive Dynamics]], [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]], [[Research/2025-11-27 - Semis - Gemini HBM4 Market Canvas]], [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]], [[Research/2026-02-26 - Semis - Gemini Lam vs AMAT Canvas]], [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]], [[Research/2026-03-20 - Lam Research and Applied Materials Evaluation]], [[Research/2026-04-10 - Hybrid Bonding and BESI Revenue Impact]], [[Research/2026-04-15 - BESI - Hybrid Bonding Market Projections]], [[Research/2026-04-19 - TSM - Stress Test]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Template restructure + research sync]: Repositioned Business Model section. Linked HB market projec…`
  - `2026-04-14 | [Major restructure]: Consolidated ChatGPT/Claude/Grok/Gemini sources. Added Hanmi share erosion, Gen…`
  - `2026-04-14 (initial) | [Thesis created]: Built from 3 research notes + web search. Core thesis: 3D integration monopoly mis…`

### BTC-CRYPTO - Bitcoin & Digital Assets
- **sectors:** [[Sectors/Consumer & Digital]], [[Sectors/Energy & Commodities]], [[Sectors/Precious Metals]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-07-10 - CRCL - Circle USDC vs BRICS mBridge Geopolitical Analysis]], [[Research/2025-07-15 - Visa Mastercard Stablecoin Competition]], [[Research/2025-07-21 - Ethereum Solana Tokenization]], [[Research/2025-08-06 - Crypto - AI Regulation Impact on Crypto Development]], [[Research/2025-11-18 - Ethereum vs Layer 1 Chains]], [[Research/2025-11-24 - BTC - Quantum Computing Threat to Bitcoin Security]], [[Research/2025-12-01 - CRCL - Circle Internet Group and USDC Dynamics]], [[Research/2025-12-26 - ETH - Ethereum Investment Dynamics Deep Dive]], [[Research/2025-12-26 - ETH - Gemini Stablecoins Ecosystem Canvas]], [[Research/2025-12-26 - Ethereum Stablecoin Adoption]], [[Research/2026-03-20 - Crypto - Gemini Trading Infrastructure Canvas]], [[Research/2026-04-01 - MSTR - Strategy Preferred Stock Capital Stack]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Initial thesis creation]: Synthesised 8 vault research notes + deep web research into commodity/cur…`

### CCJ - Cameco
- **sectors:** [[Sectors/Energy & Commodities]]
- **macro:** [[Macro/Commodity Impacts from Iran Tensions]], [[Macro/Investment Strategy for US-Iran Conflict]], [[Macro/Iran War Macroeconomic Scenario]]
- **cross-thesis:** —
- **research:** [[Research/2026-01-12 - Macro - Gemini Iran Investment Strategy Canvas]], [[Research/2026-01-26 - Silver Demand and Data Centers]], [[Research/2026-03-30 - Commodity Market Analysis 2026]], [[Research/2026-03-30 - Macro - Gemini Commodity Impact Canvas]], [[Research/2026-03-30 - Macro - Gemini Iran War Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-14 (initial enrichment) | [ChatGPT/Gemini integration]: Uranium as second-wave trade, A→C macro uniquely bullish for nuclear…`
  - `2026-04-13 | Major overhaul from stub: 6 non-consensus insights, full thesis structure from Gemini research. Uran…`
  - `2026-03-30 | Initial thesis created from Claude conversation — conviction high.`

### CRCL - Circle Internet Group
- **sectors:** [[Sectors/Crypto & Digital Assets]], [[Sectors/Financial Services]]
- **macro:** —
- **cross-thesis:** [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]]
- **research:** [[Research/2025-07-10 - CRCL - Circle USDC vs BRICS mBridge Geopolitical Analysis]], [[Research/2025-07-15 - Visa Mastercard Stablecoin Competition]], [[Research/2025-12-01 - CRCL - Circle Internet Group and USDC Dynamics]], [[Research/2025-12-26 - ETH - Ethereum Investment Dynamics Deep Dive]], [[Research/2025-12-26 - Ethereum Stablecoin Adoption]], [[Research/2026-04-15 - BTC-CRYPTO - Comprehensive Digital Assets Update April 2026 - deep-dive]]
- **status:** active
- **log_tail:** —

### CSGP - CoStar Group
- **sectors:** [[Sectors/Enterprise Software]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2026-03-26 - CSGP - CoStar Group Investment Evaluation]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [Major thesis overhaul]: Restructured to Thesis Template; consolidated 6 source segments across Clau…`
  - `2026-03-25 | [Initial thesis]: Distilled from 6 Claude source segments — conviction set at medium.`

### DE - John Deere
- **sectors:** [[Sectors/Agriculture & Industrial Equipment]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-11-28 - DE - Gemini Equity Research Canvas]], [[Research/2025-12-11 - DE - Gemini Tech Advantage Canvas]], [[Research/2025-12-11 - John Deere Technology Assessment]], [[Research/2026-02-17 - DE - Gemini Stock Price Canvas]], [[Research/2026-03-31 - John Deere Farm Automation Platform]], [[Research/2026-04-15 - DE - Investment Evaluation]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [Major restructure]: Consolidated from 5 research notes + 4 LLM exports; added Summary, Outstanding …`
  - `2026-04-14 (earlier) | [ChatGPT research integration]: Added farm ERP framing, tech lead narrowing (ag) / absent (construct…`
  - `2026-02-12 | Distilled from 2 source segments across 1 conversations. Filtered for non-consensus views and differ…`

### DUOL - Duolingo
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-09-22 - DUOL - Gemini Analysis Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [Full thesis rebuild]: Consolidated Claude/ChatGPT/Gemini/Grok exports + web research. Updated to FY…`
  - `2026-04-14 (prior session) | [ChatGPT/Gemini integration]: Added multi-subject expansion, LTV framework, DET institutional insigh…`
  - `2025-12-01 | [Initial creation]: Distilled from 1 source segment (Quartr article). Filtered for non-consensus vie…`

### EDEL - Edelweiss Financial Group
- **sectors:** [[Sectors/Financial Services]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-12-26 - EDEL - Edelweiss Financial Group Market Share]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [Full thesis rebuild]: Consolidated Claude/ChatGPT/Gemini exports + web research. Updated to Q3 FY26…`
  - `2026-04-14 (prior session) | [ChatGPT integration]: Added incubate-scale-monetize playbook, WestBridge 57x PAT price discovery, s…`
  - `2025-12-26 | [Initial creation]: Distilled from 2 source segments. Filtered for non-consensus views.`

### EINK - E Ink Holdings
- **sectors:** [[Sectors/Semiconductors]]
- **macro:** —
- **cross-thesis:** —
- **research:** —
- **status:** active
- **log_tail:**
  - `2026-04-10 | [Claude conversation export]: Initial thesis created — competitive dynamics, growth vectors, margi…`
  - `2026-04-14 | [SiPh/CPO review]: No EINK-applicable insights found in silicon photonics conversations — convicti…`
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template format, consolidated duplicates, integ…`

### GAW - Games Workshop
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2026-04-15 - GAW - 3D Printing Competitive Impact]], [[Research/2026-04-15 - GAW - Investment Analysis]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | Template restructure: Renamed/repositioned Business Model & Product Description section. Added busin…`

### HIMS - Hims & Hers Health
- **sectors:** [[Sectors/Healthcare & MedTech]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2026-02-12 - HIMS - Gemini Analysis Outline Canvas]], [[Research/2026-03-20 - HIMS Investment Case Deep Dive]], [[Research/2026-03-21 - HIMS - Gemini Investment Case Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [ChatGPT research integration]: Added 2 non-consensus insights (telehealth behavioral permanence, su…`
  - `2026-04-13 | [Major expansion]: Built from stub to full thesis using Gemini HIMS research (Mar 21); added Summary…`
  - `2026-01-22 | Initial thesis stub created. Distilled from 4 source segments across 1 conversation. Filtered for no…`

### IOT - Samsara
- **sectors:** [[Sectors/Enterprise Software]]
- **macro:** —
- **cross-thesis:** [[Theses/DE - John Deere]], [[Theses/NOW - ServiceNow]], [[Theses/PLTR - Palantir]]
- **research:** [[Research/2026-04-15 - IOT - Samsara Business Deep Dive]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Thesis created]: Built from vault research + web search. Framing: Samsara as physical operations sy…`
  - `2026-04-15 (cross-thesis sync) | [Deere cross-ref]: DE's Operations Center (500M+ acres) validates physical operations TAM; construct…`

### IQE - IQE
- **sectors:** [[Sectors/Semiconductors]]
- **macro:** —
- **cross-thesis:** [[Theses/AVGO - Broadcom]], [[Theses/BESI - BE Semiconductor Industries]], [[Theses/LITE - Lumentum]]
- **research:** [[Research/2025-11-25 - LITE - Silicon Photonics Supply Chain]], [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]], [[Research/2026-03-02 - Chinese Silicon Photonics Threat]], [[Research/2026-03-09 - Photonics and CPO Investment Outlook]], [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]], [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template. Critical: stock rallied from 19p to ~…`
  - `2026-04-14 | [Gemini/ChatGPT integration]: Linked SiPh supply chain and CPO outlook research — conviction uncha…`
  - `2026-03-02 | [Claude conversation export]: Initial thesis created — M&A special situation overlaid on structura…`

### ISRG - Intuitive Surgical
- **sectors:** [[Sectors/Healthcare & MedTech]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2026-01-18 - Healthcare and Biotech Stock Screen]], [[Research/2026-01-21 - ISRG - Gemini Investment Thesis Canvas]], [[Research/2026-03-28 - AI Threats to Intuitive Surgical]], [[Research/2026-03-29 - Cross-Procedure Capability in Surgical Robotics]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [Initial thesis creation]: Synthesized from 3 vault research sources + web research. Key angle: ISRG…`
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template. Key corrections: NVIDIA partnership c…`

### KAMBI - Kambi Group
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** —
- **research:** —
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full thesis restructure]: Rebuilt to template with FY2025 results (€162M rev, €15.5M adj. EBITA…`
  - `2026-04-14 | [ChatGPT research integration]: Reviewed Kambi Business Update conversation — no substantive new i…`
  - `2026-04-10 | [Initial creation]: Distilled from 4 source segments. Filtered for non-consensus views.`

### LITE - Lumentum
- **sectors:** [[Sectors/Semiconductors]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** [[Theses/SEMICAP - Semiconductor Capital Equipment]]
- **research:** [[Research/2025-11-25 - LITE - Silicon Photonics Supply Chain]], [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]], [[Research/2026-03-02 - Chinese Silicon Photonics Threat]], [[Research/2026-03-09 - Photonics and CPO Investment Outlook]], [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]], [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]], [[Research/2026-04-15 - LITE COHR - Lumentum vs Coherent Analysis]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full restructure + web research]: Complete rewrite to Thesis Template. Integrated Q2 FY2026 data, Q…`
  - `2026-04-14 | [Gemini/ChatGPT integration]: Linked CPO adoption dynamics and SiPh supply chain canvases — convic…`
  - `2026-04-03 | [Claude conversation export]: Initial thesis distilled — non-consensus views on EML monopoly and p…`

### LNG - Cheniere Energy
- **sectors:** [[Sectors/Energy & Commodities]]
- **macro:** [[Macro/Commodity Impacts from Iran Tensions]], [[Macro/Investment Strategy for US-Iran Conflict]], [[Macro/Iran War Macroeconomic Scenario]]
- **cross-thesis:** —
- **research:** [[Research/2025-07-03 - Macro - Iran-Israel Ceasefire Tensions and Geopolitical Risk]], [[Research/2026-01-12 - Macro - Gemini Iran Investment Strategy Canvas]], [[Research/2026-03-30 - Commodity Market Analysis 2026]], [[Research/2026-03-30 - Macro - Gemini Commodity Impact Canvas]], [[Research/2026-03-30 - Macro - Gemini Iran War Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [ChatGPT/Gemini integration]: JKM ranked #1 most impacted commodity, gas-to-coal substitution as dem…`
  - `2026-04-13 | 4 non-consensus insights from Gemini: Europe's broken LNG bridge, Japan/Korea 3-week reserve vulnera…`
  - `2026-03-30 | Initial thesis created from Claude conversation. Filtered for non-consensus views — conviction hig…`

### META - Meta
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** —
- **research:** [[Research/2025-04-29 - META VRT - Open Compute Project and Vertiv Collaboration]], [[Research/2025-12-05 - Macro - Gemini AI Bubble Risk Canvas]]
- **status:** active
- **log_tail:**
  - `2026-01-06 | Initial thesis created. Distilled from 3 source segments across 1 Claude conversation. Filtered for …`
  - `2026-04-14 | [ChatGPT research integration]: Added 3 non-consensus insights (Advantage+ monetization speed, capex…`
  - `2026-04-15 | [Complete thesis restructure]: Rewrote to Thesis Template format; consolidated all LLM imports; adde…`

### MTN - Vail Resorts
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-12-15 - MTN - Gemini Stock Decline Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Major thesis restructure]: Complete rewrite to Thesis Template format — consolidated ChatGPT, Gem…`
  - `2026-04-14 | [ChatGPT research integration]: Added 5 non-consensus insights (Epic Pass saturation, deferred maint…`
  - `2025-12-11 | Distilled from 3 source segments across 1 conversations. Filtered for non-consensus views and differ…`

### NET - Cloudflare
- **sectors:** [[Sectors/Cybersecurity]]
- **macro:** —
- **cross-thesis:** [[Theses/PANW - Palo Alto Networks]]
- **research:** [[Research/2025-07-08 - PANW - AWS vs Palo Alto Cybersecurity Competitive Dynamics]], [[Research/2025-07-15 - NET - Cloudflare Workers Edge Computing]], [[Research/2026-03-31 - Cloudflare Path to Competing with Hyperscalers]], [[Research/2026-03-31 - NET - Gemini Edge Compute Canvas]], [[Research/2026-04-03 - Cloudflare Role in Telecom Edge Computing]], [[Research/2026-04-14 - NOW - AI Disruption Risk - deep-dive]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [ChatGPT integration]: Agentic web payments/content monetization, "every feature for everyone" GTM, …`
  - `2026-04-13 | 7 non-consensus insights from Gemini: Hyperscaler margin hollowing, R2 compliance gap, physics moat …`
  - `2026-03-20 | Initial thesis created from Claude conversation — conviction medium.`

### NFLX - Netflix
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** [[Theses/SPOT - Spotify]]
- **research:** [[Research/2026-03-21 - NFLX - Gemini Investment Case Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template, consolidated Claude/Gemini sources. K…`
  - `2026-04-14 | [Gemini Canvas ingestion]: Linked NFLX investment case analysis — streaming hegemony thesis — co…`
  - `2026-03-20 | [Claude conversation export]: Initial thesis distilled from 3 source segments — non-consensus view…`

### NOW - ServiceNow
- **sectors:** [[Sectors/Enterprise Software]]
- **macro:** —
- **cross-thesis:** [[Theses/NET - Cloudflare]], [[Theses/PLTR - Palantir]]
- **research:** [[Research/2025-12-26 - ServiceNow Acquisition Strategy]], [[Research/2026-01-06 - NOW - Gemini Acquisition Strategy Canvas]], [[Research/2026-01-06 - ServiceNow Stock Decline and AI Traction]], [[Research/2026-03-30 - ServiceNow Distribution and Partner Economics]], [[Research/2026-04-01 - Salesforce vs ServiceNow in Agentic AI]], [[Research/2026-04-02 - ServiceNow Subreddit Investor Insights]], [[Research/2026-04-05 - ServiceNow CMDB vs Palantir Ontology]], [[Research/2026-04-09 - ServiceNow CMDB Dependency and Limitations]], [[Research/2026-04-14 - NOW - AI Disruption Risk - deep-dive]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full thesis restructure]: Consolidated 9 research notes into template format. Updated to April 2026…`
  - `2026-04-14 | [Thesis created]: Built from ChatGPT/Gemini/Claude research on acquisition strategy, CMDB vs Ontolog…`

### NVDA - Nvidia
- **sectors:** [[Sectors/NAND Flash & Storage]], [[Sectors/Semiconductors]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** [[Theses/285A - Kioxia]], [[Theses/AVGO - Broadcom]], [[Theses/IQE - IQE]], [[Theses/LITE - Lumentum]], [[Theses/PLTR - Palantir]], [[Theses/SEMICAP - Semiconductor Capital Equipment]], [[Theses/SNDK - SanDisk]]
- **research:** [[Research/2025-07-15 - Data Center Liquid Cooling]], [[Research/2025-08-09 - Performance vs Standardization]], [[Research/2025-11-01 - DRAM HBM Competitive Dynamics]], [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]], [[Research/2025-11-27 - Semis - Gemini HBM4 Market Canvas]], [[Research/2026-01-07 - NVDA - Nvidia CES 2026 Summary]], [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]], [[Research/2026-03-28 - AI - Gemini AI Ecosystem Canvas]], [[Research/2026-03-28 - NVDA - Gemini Omniverse Canvas]], [[Research/2026-03-28 - NVDA - Omniverse and PhysX in Physical AI]], [[Research/2026-03-28 - Nvidia PhyX and Physical AI]], [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]], [[Research/2026-04-19 - Huawei Ascend Roadmap - news]], [[Research/2026-04-19 - TSM - Stress Test]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template. FY2026 results ($215.9B, +65%), Vera …`
  - `2026-04-14 | [ChatGPT/Gemini integration]: CES 2026, HBM4 yields, AI bubble risk, SiPh supply chain added — con…`
  - `2026-04-13 | [Initial thesis creation]: Synthesized from 3 Gemini canvases + Grok PhysX deep-dive. Cross-thesis l…`

### OPEN - Opendoor
- **sectors:** —
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-11-29 - OPEN - Opendoor Progress Assessment]], [[Research/2025-12-04 - OPEN - Gemini Business Assessment Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | Template restructure: Complete rewrite to Thesis Template format. Consolidated all LLM sources (Chat…`
  - `2026-04-14 | [Gemini/ChatGPT integration]: Linked business assessment canvas. Added 3 non-consensus insights: com…`
  - `2025-11-28 | Initial thesis created. Distilled from 2 source segments across 1 conversations. Filtered for non-co…`

### PANW - Palo Alto Networks
- **sectors:** [[Sectors/Cybersecurity]]
- **macro:** —
- **cross-thesis:** [[Theses/NET - Cloudflare]]
- **research:** [[Research/2025-07-08 - PANW - AWS vs Palo Alto Cybersecurity Competitive Dynamics]], [[Research/2026-04-21 - CRWD vs PANW - Competitive Comparison]]
- **status:** draft
- **log_tail:**
  - `2026-04-15 | Initial thesis created from vault research + comprehensive web research. Q2 FY2026: $2.6B rev (+15%)…`
  - `2026-04-21 | Comparison [[Research/2026-04-21 - CRWD vs PANW - Competitive Comparison]]: product/tech — CRWD wi…`

### PLTR - Palantir
- **sectors:** [[Sectors/Defense & Geopolitics]], [[Sectors/Enterprise Software]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** [[Theses/NET - Cloudflare]], [[Theses/NOW - ServiceNow]]
- **research:** [[Research/2025-02-19 - PLTR - Palantir Valuation Analysis]], [[Research/2026-03-21 - PLTR - Gemini Strategy Canvas]], [[Research/2026-03-29 - PLTR - Gemini Automation Platforms Canvas]], [[Research/2026-03-29 - Palantir Comparison]], [[Research/2026-03-31 - Databricks Threat to Palantir]], [[Research/2026-04-05 - ServiceNow CMDB vs Palantir Ontology]], [[Research/2026-04-09 - ServiceNow CMDB Dependency and Limitations]], [[Research/2026-04-14 - NOW - AI Disruption Risk - deep-dive]], [[Research/2026-04-15 - PLTR - Competitive Win Scenarios]]
- **status:** active
- **log_tail:**
  - `2026-04-15 (earlier) | [Research sync]: Linked [[Research/2026-04-15 - PLTR - Competitive Win Scenarios]] — win scenarios…`
  - `2026-04-14 | [ChatGPT research integration]: Added insights from PLTR vs NOW AI comparison, AI regulation, AI bub…`
  - `2026-04-13 | [Initial thesis]: Created from two Gemini canvases (Strategy, Automation Platforms); Ontology as ope…`

### PSTG - Pure Storage
- **sectors:** [[Sectors/Enterprise Software]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** [[Theses/285A - Kioxia]], [[Theses/AVGO - Broadcom]], [[Theses/META - Meta]], [[Theses/NVDA - Nvidia]], [[Theses/SNDK - SanDisk]]
- **research:** [[Research/2026-01-15 - PSTG - Gemini Investment Thesis Canvas]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Complete thesis restructure]: Rewrote to Thesis Template; consolidated Gemini/ChatGPT/Claude source…`
  - `2026-04-14 | [Gemini Canvas ingestion]: Linked Pure Storage investment thesis canvas — AI infrastructure storag…`
  - `2026-01-14 | Distilled from 1 source segments across 1 conversations. Filtered for non-consensus views and differ…`

### RELIANCE - Reliance Industries
- **sectors:** [[Sectors/Consumer & Digital]], [[Sectors/Energy & Commodities]]
- **macro:** [[Macro/Commodity Impacts from Iran Tensions]]
- **cross-thesis:** —
- **research:** [[Research/2026-04-15 - RELIANCE - Comprehensive Update April 2026 - deep-dive]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template, consolidated duplicate content from L…`
  - `2026-04-10 | [Claude conversation export]: Initial thesis distilled — SOTP anomaly, Jio IPO catalyst, consumer …`

### SEMICAP - Semiconductor Capital Equipment
- **sectors:** [[Sectors/NAND Flash & Storage]], [[Sectors/Semiconductor Capital Equipment]], [[Sectors/Semiconductors]]
- **macro:** —
- **cross-thesis:** [[Theses/BESI - BE Semiconductor Industries]], [[Theses/LITE - Lumentum]], [[Theses/NVDA - Nvidia]]
- **research:** [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]], [[Research/2025-11-27 - Semis - Gemini HBM4 Market Canvas]], [[Research/2026-02-26 - Semis - Gemini Lam vs AMAT Canvas]], [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]], [[Research/2026-03-20 - Semis - Gemini WFE Equipment Canvas]], [[Research/2026-04-10 - Hybrid Bonding and BESI Revenue Impact]], [[Research/2026-04-19 - TSM - Stress Test]]
- **status:** active
- **log_tail:** —

### SHOP - Shopify
- **sectors:** [[Sectors/Enterprise Software]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-09-18 - US Insurance Broking Market]], [[Research/2025-12-01 - CRCL - Circle Internet Group and USDC Dynamics]], [[Research/2026-04-15 - SHOP - Comprehensive Update April 2026 - deep-dive]]
- **status:** active
- **log_tail:**
  - `2026-04-10 | Initial thesis distilled from 2 source segments across 1 Claude conversation. Filtered for non-conse…`
  - `2026-04-15 | [Complete thesis restructure]: Rewrote to Thesis Template; consolidated all LLM sources; added Summa…`
  - `2026-04-15 (cross-thesis sync) | [Crypto research sync]: Stablecoin market $318.6B ATH, Visa/Mastercard expanding USDC settlement —…`

### SNDK - SanDisk
- **sectors:** [[Sectors/NAND Flash & Storage]], [[Sectors/Semiconductors]]
- **macro:** —
- **cross-thesis:** [[Theses/285A - Kioxia]], [[Theses/SEMICAP - Semiconductor Capital Equipment]]
- **research:** [[Research/2025-11-01 - DRAM HBM Competitive Dynamics]], [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]], [[Research/2026-01-17 - SanDisk HBM and NAND in AI]], [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]], [[Research/2026-01-18 - SNDK - Gemini AI Investment Canvas]], [[Research/2026-03-27 - Semis - Gemini TurboQuant Memory Canvas]], [[Research/2026-03-28 - AI - Gemini AI Ecosystem Canvas]], [[Research/2026-03-31 - SanDisk Valuation Assessment]], [[Research/2026-04-15 - SNDK - Investment Evaluation]], [[Research/2026-04-16 - NAND Sector Key Questions Deep Dive - deep-dive]]
- **status:** active
- **log_tail:**
  - `2026-04-15 (SEMICAP cross-thesis sync) | [SEMICAP thesis]: TEL cryogenic etch enters volume for 400-layer NAND in 2026; etch intensity ~5x vs…`
  - `2026-04-15 | [Thesis created]: Split from KIOXIA-SNDK archive. Consolidated ChatGPT/Gemini/Claude/web research. S…`
  - `2026-04-15 (BESI cross-thesis sync) | [BESI hybrid bonding research]: Samsung licensing W2W from Changjiang for V10 NAND (420-430 layers) …`

### SPOT - Spotify
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2026-04-15 - SPOT - Product Strategy and Competitive Position]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Major thesis restructure]: Complete rewrite to Thesis Template; consolidated all LLM sources; added…`
  - `2026-04-14 | [ChatGPT research integration]: ChatGPT consumer spending at half of Spotify's despite 800M WAU vali…`
  - `2026-04-04 | Distilled from 3 source segments across 1 conversations. Filtered for non-consensus views and differ…`

### STNG - Scorpio Tankers
- **sectors:** [[Sectors/Defense & Geopolitics]], [[Sectors/Energy & Commodities]]
- **macro:** [[Macro/Commodity Impacts from Iran Tensions]], [[Macro/Investment Strategy for US-Iran Conflict]], [[Macro/Iran War Macroeconomic Scenario]]
- **cross-thesis:** —
- **research:** [[Research/2025-07-03 - Macro - Iran-Israel Ceasefire Tensions and Geopolitical Risk]], [[Research/2026-01-12 - Macro - Gemini Iran Investment Strategy Canvas]], [[Research/2026-03-30 - Commodity Market Analysis 2026]], [[Research/2026-03-30 - Macro - Gemini Commodity Impact Canvas]], [[Research/2026-03-30 - Macro - Gemini Iran War Canvas]], [[Research/2026-04-02 - GCC Market Shorting Options]]
- **status:** active
- **log_tail:**
  - `2026-04-14 | [ChatGPT/Gemini integration]: Product tankers capture the tighter barrel (diesel cracks $44-50/bbl),…`
  - `2026-04-13 | 5 non-consensus insights added from Gemini Iran/commodity research: market complacency vs physical d…`
  - `2026-04-12 | Initial thesis created: Iran-Hormuz disruption. Dual-closure analysis: ~15-25% ton-mile demand shock…`

### TSM - Taiwan Semiconductor
- **sectors:** [[Sectors/Semiconductor Capital Equipment]], [[Sectors/Semiconductors]]
- **macro:** [[Macro/AI Bubble Risk and Semiconductor Valuations]]
- **cross-thesis:** [[Theses/AVGO - Broadcom]], [[Theses/BESI - BE Semiconductor Industries]], [[Theses/NVDA - Nvidia]], [[Theses/SEMICAP - Semiconductor Capital Equipment]]
- **research:** [[Research/2026-04-10 - Hybrid Bonding and BESI Revenue Impact]], [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]], [[Research/2026-04-19 - Huawei Ascend Roadmap - news]], [[Research/2026-04-19 - TSM - Stress Test]]
- **status:** active
- **log_tail:**
  - `2026-04-19 | Initial thesis created. Conviction: medium — monopoly on leading-edge logic with expanding pricing…`

### TTWO - Take-Two Interactive
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** [[Macro/Iran War Macroeconomic Scenario]]
- **cross-thesis:** —
- **research:** —
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template, updated Q3 FY2026 actuals, added EA $…`
  - `2026-04-14 | [ChatGPT review]: No new insights from TTWO Business and Culture conversation — conviction unchang…`
  - `2026-04-11 | [Claude conversation export]: Initial thesis distilled — GTA VI binary outcome, UGC platform trans…`

### UBER - Uber
- **sectors:** [[Sectors/Consumer & Digital]]
- **macro:** —
- **cross-thesis:** —
- **research:** [[Research/2025-11-29 - OPEN - Opendoor Progress Assessment]]
- **status:** active
- **log_tail:**
  - `2026-04-15 | [Full restructure + web research]: Aligned to Thesis Template. Key new data: Rivian $1.25B/50K robot…`
  - `2026-04-14 | [ChatGPT review]: No new insights from Uber Investment Update conversation — conviction unchanged.`
  - `2026-04-12 | [Claude conversation export]: Initial thesis distilled — platform monopoly, AV distribution strate…`

### VRT - Vertiv Holdings
- **sectors:** [[Sectors/Semiconductors]]
- **macro:** —
- **cross-thesis:** [[Theses/META - Meta]], [[Theses/NVDA - Nvidia]]
- **research:** [[Research/2025-04-28 - VRT - Vertiv Role in Data Center Infrastructure]], [[Research/2025-04-29 - META VRT - Open Compute Project and Vertiv Collaboration]], [[Research/2025-07-15 - Data Center Liquid Cooling]]
- **status:** active
- **log_tail:**
  - `2026-04-21 | Initial thesis created. Conviction: medium — strong AI infra structural position priced against ne…`

### WTC - WiseTech Global
- **sectors:** [[Sectors/Enterprise Software]]
- **macro:** —
- **cross-thesis:** [[Theses/IOT - Samsara]], [[Theses/NOW - ServiceNow]], [[Theses/PLTR - Palantir]]
- **research:** [[Research/2025-09-24 - WTC - CargoWise vs In-House vs ERP Analysis]], [[Research/2025-09-24 - WTC - WiseTech 24-Month Strategic Review]], [[Research/2025-11-23 - WTC - WiseTech Tech Debt and Acquisition Integration]], [[Research/2025-11-25 - WTC - Cargowise Impact on Freight Forwarding]]
- **status:** active
- **log_tail:** —

## Reverse Index: Macro → Theses

| Macro Note | Linked Theses |
|---|---|
| [[Macro/AI Bubble Risk and Semiconductor Valuations]] | [[Theses/285A - Kioxia]], [[Theses/AVGO - Broadcom]], [[Theses/LITE - Lumentum]], [[Theses/META - Meta]], [[Theses/NOW - ServiceNow]], [[Theses/NVDA - Nvidia]], [[Theses/PANW - Palo Alto Networks]], [[Theses/PLTR - Palantir]], [[Theses/PSTG - Pure Storage]], [[Theses/SEMICAP - Semiconductor Capital Equipment]], [[Theses/SNDK - SanDisk]] |
| [[Macro/Commodity Impacts from Iran Tensions]] | [[Theses/CCJ - Cameco]], [[Theses/LNG - Cheniere Energy]], [[Theses/RELIANCE - Reliance Industries]], [[Theses/STNG - Scorpio Tankers]] |
| [[Macro/Investment Strategy for US-Iran Conflict]] | [[Theses/CCJ - Cameco]], [[Theses/LNG - Cheniere Energy]], [[Theses/PANW - Palo Alto Networks]], [[Theses/STNG - Scorpio Tankers]] |
| [[Macro/Iran War Macroeconomic Scenario]] | [[Theses/CCJ - Cameco]], [[Theses/LNG - Cheniere Energy]], [[Theses/STNG - Scorpio Tankers]], [[Theses/TTWO - Take-Two Interactive]] |
| [[Macro/Stablecoin Regulation as Geopolitical Infrastructure]] | [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]], [[Theses/CRCL - Circle Internet Group]] |
| [[Macro/VIX Index and Implied Volatility]] | — |

## Reverse Index: Sector → Theses

| Sector Note | Linked Theses |
|---|---|
| [[Sectors/Agriculture & Industrial Equipment]] | [[Theses/DE - John Deere]], [[Theses/IOT - Samsara]] |
| [[Sectors/Consumer & Digital]] | [[Theses/APP - AppLovin]], [[Theses/DUOL - Duolingo]], [[Theses/EDEL - Edelweiss Financial Group]], [[Theses/GAW - Games Workshop]], [[Theses/KAMBI - Kambi Group]], [[Theses/META - Meta]], [[Theses/MTN - Vail Resorts]], [[Theses/NFLX - Netflix]], [[Theses/OPEN - Opendoor]], [[Theses/RELIANCE - Reliance Industries]], [[Theses/SPOT - Spotify]], [[Theses/TTWO - Take-Two Interactive]], [[Theses/UBER - Uber]] |
| [[Sectors/Crypto & Digital Assets]] | [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]], [[Theses/CRCL - Circle Internet Group]] |
| [[Sectors/Cybersecurity]] | [[Theses/NET - Cloudflare]], [[Theses/PANW - Palo Alto Networks]] |
| [[Sectors/Defense & Geopolitics]] | [[Theses/PLTR - Palantir]], [[Theses/STNG - Scorpio Tankers]] |
| [[Sectors/Energy & Commodities]] | [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]], [[Theses/CCJ - Cameco]], [[Theses/LNG - Cheniere Energy]], [[Theses/RELIANCE - Reliance Industries]], [[Theses/STNG - Scorpio Tankers]] |
| [[Sectors/Enterprise Software]] | [[Theses/CSGP - CoStar Group]], [[Theses/IOT - Samsara]], [[Theses/NET - Cloudflare]], [[Theses/NOW - ServiceNow]], [[Theses/PANW - Palo Alto Networks]], [[Theses/PLTR - Palantir]], [[Theses/PSTG - Pure Storage]], [[Theses/SHOP - Shopify]], [[Theses/WTC - WiseTech Global]] |
| [[Sectors/Financial Services]] | [[Theses/CRCL - Circle Internet Group]], [[Theses/EDEL - Edelweiss Financial Group]] |
| [[Sectors/Healthcare & MedTech]] | [[Theses/HIMS - Hims & Hers Health]], [[Theses/ISRG - Intuitive Surgical]] |
| [[Sectors/NAND Flash & Storage]] | [[Theses/285A - Kioxia]], [[Theses/PSTG - Pure Storage]], [[Theses/SEMICAP - Semiconductor Capital Equipment]], [[Theses/SNDK - SanDisk]] |
| [[Sectors/Precious Metals]] | [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]] |
| [[Sectors/Semiconductor Capital Equipment]] | [[Theses/285A - Kioxia]], [[Theses/BESI - BE Semiconductor Industries]], [[Theses/IQE - IQE]], [[Theses/LITE - Lumentum]], [[Theses/NVDA - Nvidia]], [[Theses/SEMICAP - Semiconductor Capital Equipment]], [[Theses/SNDK - SanDisk]] |
| [[Sectors/Semiconductors]] | [[Theses/285A - Kioxia]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], [[Theses/BESI - BE Semiconductor Industries]], [[Theses/EINK - E Ink Holdings]], [[Theses/IQE - IQE]], [[Theses/LITE - Lumentum]], [[Theses/NVDA - Nvidia]], [[Theses/SEMICAP - Semiconductor Capital Equipment]], [[Theses/SNDK - SanDisk]], [[Theses/TSM - Taiwan Semiconductor]], [[Theses/VRT - Vertiv Holdings]] |

## Cross-Thesis Clusters

Bidirectional reference clusters (mutual `cross-thesis:` links). These propagate together — research affecting one member typically affects all.

| Cluster | Members | Link Type |
|---|---|---|
| NAND Memory | [[Theses/285A - Kioxia]], [[Theses/SNDK - SanDisk]] | ↔ |
| Semiconductors & AI Infrastructure | [[Theses/AVGO - Broadcom]], [[Theses/BESI - BE Semiconductor Industries]], [[Theses/LITE - Lumentum]], [[Theses/NVDA - Nvidia]], [[Theses/PSTG - Pure Storage]], [[Theses/SEMICAP - Semiconductor Capital Equipment]] | ↔ |
| Cybersecurity | [[Theses/NET - Cloudflare]], [[Theses/PANW - Palo Alto Networks]] | ↔ |
| Enterprise AI Platforms | [[Theses/NOW - ServiceNow]], [[Theses/PLTR - Palantir]] | ↔ |

## Orphan Research Notes

Research notes not linked from any thesis. Candidates for /thesis creation, integration into existing theses, or archival via /clean.

- [[Research/2025-02-24 - Macro - Gold Market Stress LBMA Shortages and Delivery Dynamics]]
- [[Research/2025-05-10 - Macro - Indian vs Pakistani Defence Stocks]]
- [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]]
- [[Research/2025-07-15 - CETY - CETY Company Report]]
- [[Research/2025-09-01 - Bali Tourism and Rental Income Trends]]
- [[Research/2025-11-27 - Misc - Gemini Essay Analysis Canvas]]
- [[Research/2025-12-10 - Australian Healthcare Non-Traditional Models]]
- [[Research/2026-03-21 - Betting on Inflation Trades]]
- [[Research/2026-03-26 - Fundrise Growth Tech Fund Holdings and Strategy]]
- [[Research/2026-03-27 - TurboQuant Impact on Memory Demand]]
- [[Research/2026-03-28 - Iran Weapons Supply Routes to Lebanon - deep-dive]]
- [[Research/2026-03-30 - FROG - Universal Artifact Management]]
- [[Research/2026-04-02 - Israel India Relations Analysis]]
- [[Research/2026-04-09 - Macro - Gemini Sydney Property Canvas]]
- [[Research/2026-04-14 - Claude Code Mastery Guide for Investment Research]]
