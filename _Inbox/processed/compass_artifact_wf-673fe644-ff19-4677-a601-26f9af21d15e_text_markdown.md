# 800VDC AI Datacenter Power: Grid-to-Rack Equity Research (FY26–FY30)

## TL;DR
- **The 800VDC transition is a 2027-launch (NVIDIA Kyber/Rubin Ultra) industrial supercycle whose biggest, most defensible profit pools sit in the *grid-side* AC/DC infrastructure layer and a few *physically bottlenecked* component oligopolies — not in the wide-bandgap semis where most of the retail attention has been.** Top-conviction names: **Eaton (ETN), Vertiv (VRT), Schneider Electric (SU.PA), Hitachi (6501.T) via Hitachi Energy, Delta Electronics (2308.TW), HD Hyundai Electric (267260.KS), Hyosung Heavy Industries (298040.KS), Disco (6146.T), Monolithic Power (MPWR), Murata (6981.T)**.
- **Within wide-bandgap, the asymmetric set-ups are Infineon (IFX) and onsemi (ON) for SiC/GaN scale, Innoscience (2577.HK) as the only Chinese name on NVIDIA's silicon list with a Google design-in, and Navitas (NVTS) as the highest-beta/most-narrative-driven small-cap option; Wolfspeed (WOLF) is a post-Chapter-11 turnaround with optionality but execution risk.**
- **The chain has at least four structural oligopolies the market under-prices: (i) Disco's >70% share in SiC dicing/grinding, (ii) the Murata/Samsung-EM/TDK/Taiyo Yuden Japan-Korea oligopoly in high-cap MLCCs (Murata confirmed 15–35% price hikes effective April 1, 2026 per TrendForce/Liberty Times notice; Taiyo Yuden +6–13% in May 2026; Samsung Electro-Mechanics signaling 5–10%), (iii) the HD Hyundai/Hyosung/LS three-firm Korean lock on US 765kV transformer slots (orders booked through 2031), and (iv) Vacuumschmelze (VAC) in nanocrystalline cores for MFTs/SSTs.**

## Key Findings

### 1. The architecture in one paragraph
NVIDIA at Computex 2025 and the OCP Global Summit (Oct 13–16, 2025, San Jose) formalized an 800 VDC rack-power architecture targeted at the 2027 Rubin Ultra / Kyber generation, with first-rack densities at 600 kW–1 MW+ and a path to multi-MW per rack. The new chain converts MV AC (typ. 13.8 kV) at the data hall perimeter using **solid-state transformers and/or industrial rectifiers** directly to 800 VDC, distributes via 800 VDC busways, and steps down inside the rack via 800V→48V→core converters using **SiC for the front end and GaN for higher-frequency intermediate and point-of-load conversion**. NVIDIA's published ecosystem comprises three categories: (a) silicon — ADI, AOS, EPC, Infineon, Innoscience, MPS, Navitas, onsemi, Power Integrations, Renesas, Richtek, ROHM, STMicro, TI; (b) power-system components — BizLink, Delta, Flex, Lead Wealth, LITEON, Megmeet; (c) data-center power systems — ABB, Eaton, GE Vernova, Heron Power, Hitachi Energy, Mitsubishi Electric, Schneider Electric, Siemens, Vertiv. Vertiv has stated its 800VDC portfolio will ship 2H 2026 "ahead of Kyber/Rubin Ultra."

### 2. Best-positioned names (high-conviction)

**Eaton (ETN)** — Q1 FY26 (reported May 5, 2026): record revenue $7.5B (+17% YoY), data-center orders **+240% YoY**, US data-center capacity under construction now estimated at **32 GW (70% AI)**, total data-center backlog **228 GW (~12 years at 2025 build rates)**. Launched the "Eaton Beam Rubin DSX" platform with NVIDIA at OCP 2025; running **~24 solid-state transformer pilots with hyperscalers** with first orders expected late-2026 for 2027 ship. Boyd Thermal (closed March 2026) is the liquid-cooling complement; Electrical Americas backlog +44% YoY to $14.5B. Eaton has guided 2026 organic growth midpoint to 10%, FY26 EPS $13.05–$13.50 (Mobility spin Q1 2027). This is the cleanest, fastest-compounding, most-defensible name in our universe.

**Vertiv (VRT)** — explicitly the named NVIDIA 800VDC reference-architecture partner with portfolio launch in 2H 2026 to align with the 2027 Rubin Ultra rollout. Building **centralized rectifiers, high-efficiency DC busways, rack-level DC-DC converters, and DC-compatible BBUs**, leveraging its DC heritage from telecom (decades of ±400 VDC deployment). 4,000+ field-service engineers create high switching costs for AI factory operators. Already engaged in early-design phases of "several large-scale AI factory projects" using 800 VDC as basis-of-design.

**Schneider Electric (SU.PA / SBGSY)** — global, deeper EU exposure than Eaton/Vertiv. Co-developed reference designs with NVIDIA (announced GTC Paris June 2025; updated at OCP October 2025), launched first integrated power + liquid-cooling control framework (Motivair-based, acquired March 2025). Pitching as anchor partner for the EU's AI Continent Action Plan (13 AI factories, up to five gigafactories) and is the most logical primary winner of Europe-located gigawatt AI factories.

**ABB (ABBN.SW / ABB)** — joined NVIDIA collaboration October 13, 2025, explicitly aimed at **DC-rated breakers, protection, busways, and power shelves engineered for 800V DC and 1MW racks**. Giampiero Frisio, President ABB Electrification: "*ABB is leading the development of the key new power distribution technologies that will create the next generation of data centers… We have been an early investor in the cutting-edge UPS, DC and solid-state electronics that will enable data centres to stay ahead of AI's growing power demands.*" MegaFlex UPS line already in MW-class hyperscale deployment; AI-ready refresh of MNS low-voltage switchgear with SACE Emax 3. ABB's December 2024 deal to acquire Siemens Energy's power-electronics business strengthens its SST stack.

**Hitachi (6501.T) via Hitachi Energy** — listed in NVIDIA's data center power systems partner group. Hitachi Energy FY24 (to Mar-25) Power Grids revenue $19.8B (+26%), orders $32.8B, **backlog $57.9B**. CEO Andreas Schierenbeck (S&P Global, Jan 5, 2026): "*In the case of large transformers, the company still has waiting times of up to 40 months, despite investing in new production facilities… the gap between demand and supply is not really closing.*" Capex commitments: $1B+ US (including $457M South Boston VA new large-power-transformer plant, operational 2028 — the **largest such facility in the US**); $195M Quebec, $106M Alamo TN. Hitachi Energy India Q3FY26 backlog at a record ₹29,872 cr (~$3.5B), with MD N. Venu noting: "*AI's power intensive growth demands strategic infrastructure investments.*"

**Delta Electronics (2308.TW)** — author of the OCP 800 VDC technical white paper, dominant server-PSU vendor (CommonWealth Magazine citing Goldman Sachs analyst Bruce Lu, May 2024: "*Delta was already a top dog in AC/DC electric power supplies for AI servers, with over one-half of the market share*"; Yole's *Power Electronics for Data Centers 2025* report further notes Delta/Liteon/Huawei/Advanced Energy collectively hold over 60% PSU market share). Launched a 1 MW-scale in-row power system, 800 VDC solid-state transformer (98.5% efficiency), 108 kW HVDC/DC power shelf and a 660 kW 800 VDC in-row rack with 480 kW embedded BBU. Per-server revenue path: $43,800 (GB200) → $90,600 (GB300) → potentially $171,000 with Rubin Ultra 800V HVDC + POWER RACK. Co-developed "Panama Power" MV-DC solution with Alibaba. **Strategic differentiator**: TrendForce notes Delta and Flex are the only two players with integrated capability across both "grey space" (facility infrastructure) and "white space" (rack/compute).

**Korean Transformer Trio — HD Hyundai Electric (267260.KS), Hyosung Heavy Industries (298040.KS), LS Electric (010120.KS)**. Combined Q1 2026 orders **>₩7 trillion (~$5.1B)**, combined backlog **>₩32 trillion**. Hyosung Heavy 765 kV ultra-high-voltage transformer market share in US transmission grids ~50%; combined backlog hit ₩15.1 trillion (first ever). HD Hyundai Q1 2026 orders $1.797B (42.6% of full-year target in three months); backlog $7.888B. Hyosung is building a **₩330B HVDC transformer plant in Changwon**; HD Hyundai expanding Alabama plant by 2027 for 765 kV production; LS Electric expanding Busan and won a ₩170B AWS switchgear contract plus ₩319B Bloom Energy distribution contract. Some orders booked through 2031 — a structural, multi-year visibility setup with US-tariff-protected local production.

**Disco Corporation (6146.T)** — near-monopoly (>70% share) in wafer dicing saws and grinders, indispensable for SiC processing. ROIC 54% in FY25 ending Mar-25; debt-free balance sheet; FY24 revenue ¥393.3B (+27.9% YoY). Every new SiC fab built (Wolfspeed Mohawk Valley, Coherent Easton, ROHM, STM Catania, Bosch, San'an, Hua Hong) installs Disco tools — pure picks-and-shovels exposure to the SiC capex cycle. P/E ~38–40, premium to the group but justified by structural moat.

**Monolithic Power Systems (MPWR)** — replaced Vicor in NVIDIA's H100 socket and remains primary vertical-power-delivery supplier for Blackwell and on-track for Vera Rubin (late-2026 launch). Modules engineered for 98% efficiency, well-suited to direct-to-chip liquid cooling. ~$78B market cap, stock made all-time high April 24, 2026 at $1,661. Risks: Texas Instruments, ADI, Renesas, Infineon, Vicor all attacking the 48V/VPD socket — but MPWR is the incumbent.

**Murata (6981.T) + Samsung Electro-Mechanics (009150.KS) + TDK (6762.T) + Taiyo Yuden (6976.T)** — the high-cap MLCC oligopoly controls 70–80% of global share, higher in AI-server grades. A single NVIDIA GB300 server uses ~30,000 MLCCs; a rack ~450,000. Murata confirmed **15–35% price increases effective April 1, 2026** on AI-server high-cap, automotive and RF MLCCs (TrendForce, March 17, 2026, citing Liberty Times customer notice; corroborated by Investing.com and Banyan Lane Capital May 2026: "Murata raises AI/auto-grade MLCC prices 15–25%, Taiyo Yuden +6–13% in May 2026, Samsung Electro-Mechanics signaling 5–10%"); high-end utilization >80%; FY30 AI-server MLCC demand projected at **3.3× FY25**. Murata also begins **VPD power-module mass production in 2026** with cloud-provider engagement targeting ¥50B revenue cumulative through FY27.

### 3. Wide-bandgap layer

**Infineon (IFX.DE / IFNNY)** — broadest portfolio across Si/SiC/GaN, on both NVIDIA's silicon list and announced collaboration. CoolGaN G5 (650V) and G3 medium-voltage on 8-inch lines in Kulim (Malaysia) and Villach (Austria), with planned **12-inch GaN transition** for capacity. Power-GaN market expected to reach **~$3B by 2030 at a 42% CAGR from $355M in 2024**, per Yole Group's *Power GaN 2025* report (released October 29, 2025); Roy Dagher of Yole: "*Power GaN is transitioning from promise to production reality.*" Infineon expects "*the proportion of power semiconductors in a centralized HVDC architecture to be similar or higher than in today's AC distribution architecture*" (Dr. Gerald Deboy media briefing). The cleanest large-cap wide-bandgap play.

**onsemi (ON)** — EliteSiC platform; **December 2, 2025 MoU with Innoscience** to combine onsemi's packaging/system integration with Innoscience's 200mm GaN-on-Si capacity for 40–200V devices targeting AI data center, industrial, automotive, telecom, with onsemi sampling 1H 2026. Parallel collaboration with **GlobalFoundries** also announced Dec 2025 for 200mm eMode GaN-on-Si — implies dual sourcing. **September 23, 2025**: acquired Aura Semiconductor's Vcore IP, explicitly targeting "*solid state transformers, power supply units, 800 VDC distribution, and core power delivery.*" Significant heavy-auto SiC exposure remains a near-term offset.

**ROHM (6963.T)** — on NVIDIA silicon list; co-published a technical white paper at OCP 2025 (October 20, 2025) outlining 800 VDC / ±400 VDC topologies using Si/SiC/GaN; second-source SiC MOSFET package collaboration with Infineon. SiC trench MOSFET differentiation is strong; the issue is investor visibility — earnings are weighed down by SiC EV softness and capex.

**STMicroelectronics (STM)** — on NVIDIA list. China JV with Sanan and Catania mega-fab are EV-focused but provide SiC scale, and STM has SiC content in HVDC power conversion. Currently consensus-bearish due to SiC EV demand slump in 2025; the 800VDC datacenter ramp is the optionality.

**Mitsubishi Electric (6503.T)** — on NVIDIA's data-center power systems list. Mitsubishi Electric Power Products (MEPPI), Warrendale, PA, formally announced 800 VDC infrastructure support October 13, 2025: "*800 VDC is emerging as the new standard for these applications.*" New Kumamoto SiC fab completion ceremony October 1, 2025 (EV-focused). Also a 12.5% stakeholder in Coherent's SiC subsidiary — indirect SiC substrate exposure.

**Wolfspeed (WOLF)** — emerged from Chapter 11 on September 29, 2025. Q1 FY26 (reported Oct 29, 2025): revenue $197M (Mohawk Valley contributed $97M, +98% YoY); $926M cash; ~70% debt reduction to $4.6B; ~60% lower interest. CEO Robert Feurle has accelerated the **shutdown of the 150mm Durham fab** (completed one month early); production shifting to **200mm Mohawk Valley**. EV softness remains, but per Wolfspeed's 8-K filed February 4, 2026: "*AI datacenter revenue grew approximately 50% sequentially, reflecting a modest but expanding part of the Company's business with meaningful long-term potential.*" Optionality on 200mm SiC substrate scale plus 10kV+ thick-epi capability targeted at data-center UPS/SST is real, but the share price reflects bankruptcy-emergence dilution and operational risk dominates the next 12 months.

**Coherent (COHR)** — SiC substrate franchise held 75% by Coherent with Denso and Mitsubishi each owning 12.5% (December 2023). **December 3, 2025**: announced 300mm SiC platform aimed explicitly at "*new levels of thermal efficiency that translate directly into faster, more power-efficient AI datacenters*" (Gary Ruland, VP SiC). **April 9, 2026**: launched 10kV thick-epi capability for 150/200mm targeting AI data-center UPS and distribution. FY25 revenue $5.81B (+23%); CEO Jim Anderson: "*Coherent experienced strong growth in fiscal '25, with data center revenue increasing over 60%.*" Easton/Palmer PA expansion partly CHIPS-Act funded (>750,000 substrates/year capacity). After July 2025 segment reorganization, SiC revenue is no longer separately disclosed (analyst-estimated sub-$300M inside Industrial) — transparency loss is a near-term overhang.

**Innoscience (2577.HK)** — only Chinese supplier on NVIDIA's silicon list. World's largest 8-inch GaN-on-Si IDM; Suzhou fab at 15,000 wpm with 97% yield (TrendForce, Feb 2026), targeting 20,000 wpm by end-2025 and 70,000 wpm by 2029 (delayed from original 2025 target). Cumulative shipments >2B units. **Google design-in announced February 3, 2026**; onsemi MoU December 2, 2025; third-gen devices span 15V–1200V "from 800V input to GPU terminals." Geopolitical/export-control risk is real but partially de-risked by Google and onsemi commercial relationships.

**Navitas Semiconductor (NVTS)** — announced as NVIDIA 800V HVDC collaborator May 21, 2025. Q1 FY26 (reported May 5, 2026): revenue **$8.6M (+18% sequential, –38.6% YoY)**, gross margin 39.0% non-GAAP, cash $221M, no debt; AI infra revenue +50% sequential; **high-power business +35% YoY** and now a "large majority" of revenue. Demonstrated 800V→6V PDB and 250 kW solid-state transformer. Stock up ~**868% trailing twelve months** into the Q1 FY26 print with a 52-week peak of $19.93 and market cap of $4.49B (per Parameter.io, Blockonomi and MoneyCheck, May 2026); analyst consensus FY26 revenue $41.3M; no profitability expected until revenue reaches high-$30M quarterly. This is the highest-beta name in the universe — long thesis is real but the multiple already embeds aggressive design-win expectations.

**Vicor (VICR)** — Q1 FY26 revenue $113M (+20% YoY), book-to-bill >2. Second-gen Vertical Power Delivery: **3 A/mm² current density, 40× current multiplication, 1.5mm package thickness** — uniquely enabled for wafer-scale and CoWoS chiplets. Capacity is the bottleneck: existing Andover CHiP fab can be pushed to $1.5B/year run-rate; second fab being scoped. FY26 guidance ~$570M revenue assumes no new licensing pre-2027 ITC determination. Long-tail option with strong IP but currently a single-lead-customer concentration.

### 4. Critical bottlenecks and oligopolies (where the alpha really sits)

**Disco** — already discussed. Every SiC fab adds Disco tools; consumables (30–35% of revenue) are razor-blade economics.

**Vacuumschmelze (VAC)** — private (held by Apollo). Near-monopoly on **nanocrystalline VITROPERM cores** for medium-frequency transformers, which are the magnetic heart of any solid-state transformer. Hitachi Metals/Proterial (5232.T) FINEMET is the only meaningful alternative. Not directly investable as equity — but it is the *single biggest physical bottleneck* for ramping SSTs at scale, and is the reason public SST products are still 12–24 months out.

**Korean transformer oligopoly** — HD Hyundai Electric, Hyosung Heavy Industries, LS Electric. Most concentrated visibility in the report: Hyosung Q1 2026 orders ₩4.17 trillion (largest ever single project: ₩787.1B from a US transmission grid operator), HD Hyundai $1.797B orders Q1 alone, LS Electric ₩627.1B + AWS/Bloom contracts in Q2. Order books extending **through 2031**. US production (Memphis, Alabama) tariff-protects against the recent US tariff regime. Hyosung explicitly building HVDC transformer capacity in Changwon for next-gen.

**High-cap MLCC oligopoly** — Murata/Samsung-EM/TDK/Taiyo Yuden 70–80% global share. AI server is currently estimated at 20–30% of MLCC demand growth. Lead times have stretched from 8 weeks to **24–40 weeks** on AI-server-grade MLCCs (Banyan Lane Capital May 2026 research note; TradingKey separately cites "8 weeks to 24 weeks"; BXW-BOM April 2026 describes lead times "beyond 20 weeks" on large-case high-capacitance parts). Murata price increase 15–35% effective April 1, 2026 (TrendForce/Liberty Times); AI-server MLCC demand FY30 = 3.3× FY25 per Murata mid-term plan. Fenghua (000636.SZ) is the leveraged Chinese option.

**Server PSU oligopoly** — per Yole's *Power Electronics for Data Centers 2025*: "*major PSU suppliers include Delta, Liteon, Huawei and Advanced Energy collectively holding over 60% market share.*" Delta is the leader; Lite-On (2301.TW), Chicony (6411.TW), AcBel (6282.TW) round out the Taiwan exposure. Megmeet (Chinese) entered NVIDIA supply chain but share builds slowly.

**SiC substrate (200mm/300mm)** — Wolfspeed + Coherent + Resonac/Showa Denko (~25% global SiC epi share, per Nikkei/Electronics Weekly 2023). Plus SK Siltron and II-VI/Coherent already covered. 200mm transition is the swing factor for unit economics; Wolfspeed's Mohawk Valley and Coherent's December 2025 300mm announcement are the most strategic moves.

**Connectors/busbars** — BizLink (3665.TW) is the named NVIDIA partner with explicit 800V busway, liquid-cooled rack busbar, and OCP-compliant ORv3 connectors; supports BzLisa S series for power-shelf interconnection. Amphenol (APH), TE Connectivity (TEL), Hirose (6806.T), JAE (6807.T) all play.

### 5. BBU/supercap layer

Power transients of 30%+ on GPU loads in microseconds force in-rack BBU integration. Delta's 800 VDC architecture integrates 80 kW BBU per power shelf (480 kW per rack). EnerSys (ENS), Saft (TotalEnergies private), Mersen (DC fuses), Littelfuse (LFUS) and Eaton/Bussmann are exposed. China's Sungrow announced an "AIDC" division May 2025 with products expected 2026.

### 6. Time-phased framework

**Now → FY26**: focus is on AC infrastructure (Korean transformers, Eaton, Vertiv, Schneider, ABB, Hitachi Energy), MLCC capacity allocation (Murata price hike April 2026), Disco tool orders for the SiC fab build-out, and Vicor/MPS sockets in current Blackwell generation. Eaton Q1 FY26 already showed +240% YoY data-center orders.

**FY27 — Rubin / Rubin Ultra / Kyber launch**: First 800 VDC racks at hyperscale. Vertiv 800 VDC portfolio ships H2 2026; Eaton solid-state-transformer orders late-2026. Navitas, Innoscience, Infineon, MPS, ROHM, onsemi power-semi content per rack scales sharply. Coherent 300mm SiC ramp begins to matter for unit economics.

**FY28–FY30**: 800 VDC becomes mainstream; multi-MW racks at gigawatt-class AI campuses. The bottlenecks (VAC nanocrystalline cores, large-power transformers, MLCCs, 200mm SiC substrates) sustain pricing power for the oligopolies. Geographic diversification of hyperscaler builds into Europe (Schneider) and Japan/Korea (Mitsubishi Electric, Korean transformer trio) becomes prominent.

## Details — by sub-segment

The section-by-section content above covers each subsegment with named, company-level analysis. The structure to read it in for due-diligence prioritization is:

1. Grid → MV switchgear → SST: Hitachi Energy (6501.T), ABB, Siemens Energy, GE Vernova, Korean transformer trio. Bottleneck = nanocrystalline cores (VAC), large-power-transformer manufacturing slots (Hitachi 40-month lead times).
2. AC/DC rectifier → 800 VDC distribution → busway → BBU → power shelf: Eaton, Vertiv, Schneider, ABB; component layer Delta, LITEON, Flex, Megmeet; BBU/protection Mersen, Littelfuse, EnerSys, Saft.
3. In-rack 800V→48V→PoL DC-DC + VPD: Delta, Vicor, MPS, ADI, TI, Infineon (CoolGaN/CoolSiC), Navitas, Innoscience, Power Integrations, EPC, Renesas.
4. Power-semi substrates and tools: Wolfspeed, Coherent, Resonac, SK Siltron, Sumitomo Electric (GaN), Mitsubishi Chemical; Disco, Tokyo Seimitsu, Aixtron, Veeco, Lam, AMAT, TEL, Entegris.
5. Passive components and magnetics: Murata, Samsung Electro-Mechanics, TDK, Taiyo Yuden, Yageo, Vishay, Walsin, Nichicon, Nippon Chemi-Con, Panasonic Industry, VAC, Proterial/Hitachi Metals.
6. Connectors/cabling/enclosures: BizLink, Amphenol, TE Connectivity, Hirose, JAE, nVent, Prysmian, Nexans.

## Recommendations

**Core long book (sized largest):**
- **Eaton, Vertiv, Schneider Electric, Hitachi (6501.T)**: own as a basket. These are the cleanest grid-to-rack infrastructure compounders with multi-year backlog visibility and direct NVIDIA partnership status. Eaton is the largest weight given quantified backlog (228 GW), the explicit Eaton Beam Rubin DSX platform, and ~24 SST pilots with hyperscalers.

**Bottleneck specialists (concentrated positions):**
- **Disco (6146.T), Murata (6981.T), HD Hyundai Electric (267260.KS), Hyosung Heavy Industries (298040.KS), LS Electric (010120.KS)**: each represents an oligopoly with pricing power and multi-year demand visibility. Korean trio is best paired into a basket — the share-of-orders rotates among them.

**Pure datacenter-power leverage:**
- **Delta Electronics (2308.TW), Monolithic Power (MPWR), BizLink (3665.TW)**: these are the most-direct beneficiaries of the in-rack 800VDC stack. Delta is the most-asymmetric of the three given per-server revenue trajectory and TrendForce-validated dual-space integration.

**Wide-bandgap exposure (sized smaller, paired):**
- Pair **Infineon (IFX)** and **onsemi (ON)** for the broad SiC/GaN merchant exposure; add **Innoscience (2577.HK)** for higher-beta Chinese GaN.
- **Navitas (NVTS)** as a small high-beta sleeve only; **Wolfspeed (WOLF)** as a post-emergence turnaround sleeve.
- **Coherent (COHR)** for the 200/300mm SiC substrate story plus the broader datacomms ramp.

**MLCC basket:** Murata + Samsung-EM + TDK + Taiyo Yuden as a four-stock basket, given the April 2026 price hike, capacity tightness, and 3.3× FY30 demand outlook.

**Benchmarks that would change these calls:**
- **Slip in NVIDIA Rubin Ultra / Kyber from 2027 to 2028+**: would compress the immediate 800VDC ramp; reduce wide-bandgap and Vertiv exposure; the Korean transformer trio and Eaton thesis remain intact (AC grid demand is independent).
- **Hyperscalers move to in-house custom power modules at scale**: largest risk to MPS, Vicor and to a lesser extent Navitas.
- **SiC substrate price war driven by Chinese over-capacity (San'an, Hua Hong, TankeBlue, SICC)**: compresses Wolfspeed/Coherent unit economics; structurally bullish for Disco (tool sales independent of substrate ASP).
- **China export-control escalation**: most negative for Innoscience and any Chinese-content path; net positive for ex-China players (Infineon, Navitas, Wolfspeed, Coherent, onsemi).
- **Korean tariff escalation on transformers**: thesis is built around US-local production at Memphis/Alabama plants, so should remain insulated.

## Caveats

1. Several of the cited datapoints (Murata 15–35% April 1, 2026 price increase, Eaton 32 GW / 228 GW backlog, Hyosung ₩787.1B single contract, Hitachi 40-month lead times) are drawn from company press releases, transcripts and trade press; we treat as directionally correct but recommend cross-referencing against latest 10-Q/F-1 filings before sizing.
2. NVIDIA's 800VDC partner list is an *announced collaboration* list — being on it does NOT automatically equal volume design wins. Conversely, partners *not* on the list (Fuji Electric, Sumitomo Electric, several Chinese SiC vendors) may still capture content. We have been explicit about who has *named* products vs. who is partner-list-only.
3. The transition timeline carries real execution risk. Vertiv has stated H2 2026 readiness; Eaton expects SST orders "late 2026 for 2027 shipment." Any slip in NVIDIA Rubin Ultra (currently 2027) would propagate. NVIDIA itself uses forward-looking language ("rollout targeted for 2027") that should not be treated as certain.
4. We avoided several speculative narratives: hyperscaler in-house power-module efforts (Microsoft, Meta, Google) are real and well-evidenced; specific design-win granularity (e.g., "MPS is locked in Vera Rubin VRMs") is *plausible based on management commentary* but not confirmed by NVIDIA — treat as base case not certainty.
5. Wolfspeed remains in a fresh-start-accounting period; its forward financials will be restated through 2H FY26. Treat reported margins with caution.
6. Coherent stopped disclosing SiC revenue separately after July 2025 segment changes; SiC investment thesis there is partly faith-based until management provides incremental color.

## Follow-up research areas

- Hyperscaler-specific 800 VDC adoption commitments (Microsoft, Meta, Google, Amazon, Oracle) — material to the slope of the ramp.
- China domestic SiC and GaN price elasticity and the impact on global merchant ASPs through 2027.
- Detailed VAC (Vacuumschmelze) capacity expansion plans for nanocrystalline cores — the single biggest physical bottleneck for SST scaling.
- Quantification of BBU/supercap content per 800 VDC rack and the addressable market for EnerSys/Saft/Skeleton.
- TSMC's role in GaN foundry (recent press has TSMC exiting its in-house GaN line, which structurally tightens Innoscience/Infineon merchant capacity).
- Sumitomo Electric (5802.T) and Mitsubishi Chemical GaN-on-GaN substrate plans for future power devices beyond 800 VDC.