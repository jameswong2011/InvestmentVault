---
date: 2026-04-15
tags: [sector, moc]
---

# Semiconductors

## Sub-Sector Maps
- [[Sectors/Semiconductor Capital Equipment]] — WFE equipment market breakdown by type, end market, and key players (ASML, AMAT, LRCX, KLAC, ASMI, TEL, BESI)
- [[Sectors/NAND Flash & Storage]] — NAND flash memory competitive dynamics, product-level technology comparison, Chinese (YMTC) disruption analysis, HBF category outlook, supply-demand pricing forecast

## Active Theses
- [[Theses/SEMICAP - Semiconductor Capital Equipment]] — Sector-level thesis: KLA + AMAT as highest risk-adjusted plays; non-consensus picks across WFE (conviction: high)
- [[Theses/TSM - Taiwan Semiconductor]] — Taiwan Semiconductor (leading-edge foundry monopoly — 92% ≤7nm share, N2 +20% premium; Taiwan-tail risk materially higher than thesis-modeled after stress test; conviction: low)
- [[Theses/AVGO - Broadcom]] — Broadcom
- [[Theses/BESI - BE Semiconductor Industries]] — BESI (Hybrid bonding / advanced packaging monopoly)
- [[Theses/EINK - E Ink Holdings]] — E Ink Holdings
- [[Theses/IQE - IQE]] — IQE (III-V epitaxy / M&A special situation / SiPh demand catalyst)
- [[Theses/285A - Kioxia]] — Kioxia Holdings (NAND inventor, BiCS/CBA tech leader, Flash Ventures JV)
- [[Theses/SNDK - SanDisk]] — SanDisk Corporation (Pure-play NAND, HBF technology, AI storage supercycle)
- [[Theses/LITE - Lumentum]] — Lumentum (Photonics/EML)
- [[Theses/NVDA - Nvidia]] — Nvidia
- [[Theses/AMD - Advanced Micro Devices]] — AMD (sole merchant full-stack Nvidia alternative — CPU+GPU+DPU+FPGA; OpenAI 6GW + Meta 6GW hyperscaler-imposed diversification; MI355X within single-digit % of B200 on MLPerf 6.0; ROCm framework-native step-function adoption; 38–41x fwd P/E embeds flawless execution; conviction: medium)
- [[Theses/VRT - Vertiv Holdings]] — Vertiv (AI data center critical infrastructure pure-play — $15B backlog at 2.9x book-to-bill, 27-29% organic guide 2026; non-consensus moat quality vs consensus capacity framing — physics-limited liquid cooling IP + NVIDIA/Intel co-design + OCP standards authorship with Meta; 43x fwd EPS and 336% TTM prices against near-cycle-peak sentiment; conviction: medium)

## Key Dynamics
- **NVDA is the operating system for Physical AI, not merely a GPU vendor — FY2026 $215.9B revenue (+65%), ~$4.6T market cap, ~30x forward P/E.** The durable moat is the vertically integrated software simulation stack (PhysX 5/Warp/Omniverse/Cosmos) that locks customers into Nvidia hardware from training through simulation to edge deployment. Warp achieves 8x–669x performance advantage over JAX/CPU alternatives in differentiable physics — this gap *widens* with each hardware generation. Every potential competitor (Siemens, Dassault, Ansys, Google DeepMind) has chosen to build on Nvidia's infrastructure rather than compete against it. Vera Rubin platform in production H1 2026 (10x lower inference cost vs Blackwell). Sovereign AI tripled to ~$30B. AI accelerator market share ~75% (declining from 87% peak as custom ASICs scale — Google TPU v7 ~70% cost reduction, Trainium 30–40% better price-perf). Key risk: ASIC maturation for inference workloads. Open-source strategy (Newton, Alpamayo, GR00T, Cosmos) is an "Android strategy" deepening hardware lock-in through 5.9M CUDA developers. Conviction medium — promote if Physical AI demonstrates commercial ROI at scale or sovereign AI accelerates. *(Sources: [[Theses/NVDA - Nvidia]], [[Research/2026-03-28 - NVDA - Gemini Omniverse Canvas]], [[Research/2026-03-28 - Nvidia PhyX and Physical AI]], updated Apr 15, 2026)*
- **BESI's CoWoS exposure is directly gated by NVDA chip demand.** Die attach market share at 42%; copper pillar plating at 40-45% share. Revenue trajectory tied to TSMC advanced packaging capacity expansion. Trailing P/E 48.9x vs European semi avg 22.1x, but PEG ~2x and 3yr revenue CAGR 22% support premium. *(Source: [[Research/2025-07-06 - BESI - Analyst Estimates and Valuation Trends]])*
- **Data center infrastructure is a chokepoint supply chain** — Vertiv holds structural moat (23 manufacturing facilities, decades of thermal IP) and collaborates with NVDA on GPU cooling. CoreWeave (250K+ GPUs, 32 DCs) is a new GPU cloud entrant structurally dependent on NVDA supply allocation. *(Sources: [[Research/2025-04-28 - VRT - Vertiv Role in Data Center Infrastructure]], [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]])*
- **III-V epitaxy is the hidden chokepoint beneath silicon photonics.** SiPh PICs cannot generate their own light — every transceiver and CPO module requires external III-V laser sources (InP or GaAs). Global InP supply gap is ~70% (2M pieces demand vs 600K capacity). IQE is the only major independent Western epitaxy supplier spanning all III-V material systems. NVIDIA's $4B dual investment in Lumentum/Coherent validates the laser supply chain as strategically critical. IQE under active Takeover Code offer period; stock at ~52p has rallied >1,000% from Nov 2025 lows and now trades at peer EV/Revenue multiples (~6x). *(Source: [[Theses/IQE - IQE]], [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]])*

- **Lumentum's EML monopoly is physics-gated and widens at each speed generation — the market prices it as a cyclical supplier rather than a structural chokepoint.** 50-60% share of high-speed EMLs with sole volume production at 200G per lane. Failure rates scale with the 4th power of bandwidth, meaning 200G is ~16x harder than 100G in yield terms. Coherent buys EMLs FROM Lumentum despite 6-inch InP wafer advantage — epitaxial mastery trumps wafer diameter. Demand exceeds supply by 25-30%; management targeting $2B/quarter revenue run-rate by late 2027 at 40% operating margins. NVIDIA $2B investment includes capacity lock-out rights. OCS market revised from $500M to $1.5B (2026), projected $2.5B by 2029. SiPh foundry buildout is paradoxically bullish — every SiPh chip shipped needs an InP laser Lumentum supplies. *(Source: [[Theses/LITE - Lumentum]], updated Apr 15, 2026)*

- **The CPO transition is accelerating faster than consensus: TSMC COUPE entered risk production with AMD (Feb 2026), Broadcom shipping TH6-Davisson CPO at 102.4 Tbps, and the optical interconnect market is projected $18B to $90B by 2030.** Broadcom shipped 50K+ CPO switches in 2025. NVIDIA's Spectrum-X/Quantum-X CPO platforms ship in H2 2026. Marvell acquired Celestial AI ($3.25B) for Photonic Fabric technology. Every CPO module requires external InP laser sources from the Lumentum/Coherent/Broadcom oligopoly. CPO laser TAM estimated at $22B by 2030. Emerging entrants: Ciena/Nubis ($270M acquisition, 6.4 Tbps CPO modules), OpenLight (InP-on-silicon via Tower Semi). *(Sources: [[Theses/LITE - Lumentum]], [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]])*

- **NAND structural shortage is driven by HBM capacity diversion, not voluntary supply discipline — making it more durable than historical cycles.** Samsung and SK Hynix are reallocating up to 40% of advanced wafer capacity to HBM production. NAND capex in 2026 is $22.2B (+5% YoY) vs DRAM capex of $61.3B (+14%). Demand growing 20–22% vs supply growth 15–17%. All 2026 production sold out; 2027 allocations being negotiated. NAND wafer prices up 246% YoY. The only greenfield NAND fab under construction (Micron Singapore Fab 10B) won't produce until H2 2028. *(Sources: [[Theses/285A - Kioxia]], [[Theses/SNDK - SanDisk]], [[Research/2026-03-31 - SanDisk Valuation Assessment]])*
- **SanDisk's HBF technology could create an entirely new memory tier worth $12B+ by 2030.** High-Bandwidth Flash fills the gap between HBM ($8–10/GB, 24–144GB) and SSDs ($0.10–0.20/GB, high latency) with 1.6 TB/s bandwidth, 512GB–1TB capacity at ~$1/GB. SK Hynix partnership for OCP standardization (Feb 2026) de-risks adoption. Samples targeted H2 2026, aligned with NVIDIA Rubin. Jensen Huang's CES 2026 "completely unserved market" comment validates the category. *(Source: [[Theses/SNDK - SanDisk]])*
- **Kioxia's BiCS/CBA architecture achieves 15–20% higher density per layer than competitors — the market fixates on layer counts and draws the wrong conclusion.** BiCS10 (332-layer) expedited to 2026. LC9 245.76TB enterprise SSD (32-die stack) won FMS 2025 Best of Show. Flash Ventures JV with SanDisk provides unique capital-efficient structure. *(Source: [[Theses/285A - Kioxia]])*

- **The semicap "cycle" has structurally changed — equipment revenue per wafer start is increasing even in flat volume environments, driven by complexity rather than capacity.** WFE spending projected $135B CY2026 (+17%), with three simultaneous inflections for the first time in industry history: GAA at 2nm (process steps increase ~350→400–600), HBM4 vertical scaling (16-Hi = 3x inspection intensity), and advanced packaging (CoWoS capacity 35K→130K wafers/month, doubling process control spend per unit). KLA is the most underappreciated compounder (63% process control share, advanced packaging inspection +70% CY2025, 62% GM / 43% OM). AMAT is the value trade (31x P/E vs LRCX 48x / ASMI 45x, >20% guided growth CY2026). TEL's 92% coater/developer monopoly trades at a "Japan discount." Optical test (FormFactor, Aehr Test) is the undiscovered photonics bottleneck. *(Source: [[Theses/SEMICAP - Semiconductor Capital Equipment]], created Apr 15, 2026)*

## Watchlist
- **CRWV (CoreWeave)** — GPU cloud IPO'd Mar 2025 at $23B. Revenue $30M (2022) → $500M (2023) → ~$2B contracts (2024). NVDA-invested. Capital-intensive, debt-funded model. Deep Grok research available.

## Related Research
- [[Research/2026-04-19 - Huawei Ascend Roadmap - news]] — Huawei Ascend three-year roadmap: 950PR Q1 2026 (128GB/1.6 TB/s in-house HBM), 1.6M-die plan, ByteDance $5.6B order, Atlas SuperCluster 524 EFLOPS FP8 — quantifies China-domestic-alternative threat to NVDA, validates non-Nvidia vertically integrated AI compute at scale
- [[Research/2026-04-16 - NVDA - Jensen Huang Moat Persistence Interview - deep-dive]] — Jensen Huang CEO interview: CUDA/install base moat, ASIC competition dismissal, $100B+ supply chain commitments, China compute sufficiency argument, Groq inference segmentation
- [[Research/2025-11-27 - Broadcom Data Center Opportunity]] — Broadcom Data Center Opportunity
- [[Research/2025-11-27 - Broadcom Equity Research Framework]] — Broadcom Equity Research Framework
- [[Research/2025-11-27 - Broadcom Ethernet Networking Position]] — Broadcom Ethernet Networking Position
- [[Research/2026-01-15 - AI Compute and Memory Demands - HBM Shortage]] — AI Compute and Memory Demands - HBM Shortage
- [[Research/2026-01-17 - SanDisk HBM and NAND in AI]] — SanDisk HBM and NAND in AI
- [[Research/2026-03-02 - Chinese Silicon Photonics Threat]] — Chinese Silicon Photonics Threat
- [[Research/2026-03-09 - Photonics and CPO Investment Outlook]] — Photonics and CPO Investment Outlook
- [[Research/2026-03-14 - CXL Technology Adoption]] — CXL Technology Adoption
- [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]] — CPO Market Entry for Pluggable Optics
- [[Research/2026-03-20 - Lam Research and Applied Materials Evaluation]] — Lam Research and Applied Materials Evaluation
- [[Research/2026-03-27 - TurboQuant Impact on Memory Demand]] — TurboQuant Impact on Memory Demand
- [[Research/2026-03-28 - Nvidia PhyX and Physical AI]] — Nvidia PhyX and Physical AI
- [[Research/2026-03-31 - SanDisk Valuation Assessment]] — SanDisk Valuation Assessment
- [[Research/2026-04-10 - Hybrid Bonding and BESI Revenue Impact]] — Hybrid Bonding and BESI Revenue Impact
- [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]] — HBM4 vendor yields and revenue projections
- [[Research/2025-11-25 - LITE - Silicon Photonics Supply Chain]] — Full silicon photonics supply chain mapping
- [[Research/2025-11-01 - DRAM HBM Competitive Dynamics]] — Samsung/Micron/Hynix HBM competitive dynamics
- [[Research/2025-11-01 - BESI - BESI Role in HBM Manufacturing]] — BESI's role in HBM hybrid bonding
- [[Research/2026-01-07 - NVDA - Nvidia CES 2026 Summary]] — Nvidia CES 2026 product announcements
- [[Research/2025-07-15 - Data Center Liquid Cooling]] — Liquid cooling feasibility for data centers

- [[Research/2026-03-28 - AI - Gemini AI Ecosystem Canvas]] — AI ecosystem: Muon optimizer, open-source model parity, edge inference
- [[Research/2026-03-28 - NVDA - Gemini Omniverse Canvas]] — Nvidia Physical AI: Omniverse, PhysX, Warp benchmarks
- [[Research/2026-03-27 - Semis - Gemini TurboQuant Memory Canvas]] — TurboQuant impact on DRAM/HBM/NAND markets
- [[Research/2026-03-20 - Semis - Gemini WFE Equipment Canvas]] — Tier-1 WFE supplier five-year strategic outlook
- [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]] — Co-packaged optics adoption and photonics investment
- [[Research/2026-02-26 - Semis - Gemini Lam vs AMAT Canvas]] — Lam Research vs Applied Materials investment comparison
- [[Research/2026-01-18 - SNDK - Gemini AI Investment Canvas]] — SanDisk AI storage supercycle thesis
- [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]] — HBM shortage, inference economics, Jevons Paradox
- [[Research/2025-12-05 - Macro - Gemini AI Bubble Risk Canvas]] — AI solvency gap and bubble risk framework
- [[Research/2025-11-29 - AVGO - Gemini Investment Analysis Canvas]] — Broadcom 'Android of AI' vs Nvidia comparison
- [[Research/2025-11-27 - Semis - Gemini HBM4 Market Canvas]] — HBM4 technology and manufacturing trajectory (2025-2030)
- [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]] — Silicon photonics supply chain for post-copper era
- [[Research/2026-03-28 - NVDA - Omniverse and PhysX in Physical AI]] — NVDA PhysX competitive dynamics, no viable alternatives (Grok)
- [[Research/2025-08-09 - Performance vs Standardization]] — NVLink 7x PCIe, CXL limitations, silicon photonics role (Grok)
- [[Research/2025-07-06 - BESI - Analyst Estimates and Valuation Trends]] — BESI 42% die attach share, CoWoS equipment stack, copper pillar plating (Grok)
- [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]] — CoreWeave history, PaaS stack, 250K+ GPUs, NVDA dependency (Grok)
- [[Research/2025-04-29 - META VRT - Open Compute Project and Vertiv Collaboration]] — Vertiv OCP co-development, META data center standards influence (Grok)
- [[Research/2025-04-28 - VRT - Vertiv Role in Data Center Infrastructure]] — Vertiv moat, 23 mfg facilities, NVDA cooling collab, competitive landscape (Grok)
- [[Research/2026-04-15 - BESI - Hybrid Bonding Market Projections]] — HB market $1.47B→$5.6B (2030), BESI D2W positioning, Samsung/SK Hynix/Micron adoption timelines
- [[Research/2026-04-15 - LITE COHR - Lumentum vs Coherent Analysis]] — "Great Photonic Divergence": LITE +1,098% vs COHR +328%, pure-play vs integrated comparison
- [[Research/2026-04-15 - SNDK - Investment Evaluation]] — Post-separation pure-play NAND, HBM exclusion as structural limitation, 2026 capacity sold out

## Log

### 2026-04-19 (TSM stress test sync)
- [[Research/2026-04-19 - TSM - Stress Test]]: Taiwan strait chokepoint quantified — 92% of global leading-edge (N5/N3/N2), 100% of CoWoS, ~95% of advanced packaging sit inside 100-mile PLA strike window. Xi 2027 PLA readiness directive (CIA Burns testimony, renewed Jan 2026) coincides with current AI capex horizon. "Destroy the fabs" is US default contingency policy (Bloomberg Mar 2023; former NSA O'Brien on-record) → sector residual EV under invasion = Arizona+Japan+Germany rebuild only, 5-7yr EUV replication lag. Silicon shield theory fails Ukraine/Nord Stream 2 precedent. Customer concentration (AAPL+NVDA=40% of TSMC) amplifies rather than diversifies the geopolitical tail.

### 2026-04-21 (VRT promotion)
- `/status VRT draft→active`: [[Theses/VRT - Vertiv Holdings]] added to Active Theses; removed from Watchlist. AI data center critical infrastructure pure-play — $15B backlog at 2.9x book-to-bill, NVDA/Intel liquid cooling co-design, OCP standards authorship with Meta. Sector now covers the full AI silicon-to-power stack: compute (NVDA/AMD/AVGO/BESI/SEMICAP/TSM), memory (SNDK/285A), photonics (LITE/IQE), and data center infrastructure (VRT).
