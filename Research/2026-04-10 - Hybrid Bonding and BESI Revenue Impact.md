---
date: 2026-04-10
tags: [research, semiconductors]
status: active
sector: Semiconductors
source: Claude conversation export
source_type: deep-dive
---

# Hybrid Bonding and BESI Revenue Impact

## Original Query
> Give me an update on hybrid bonding space. What is the share of expected demand from DRAM / compute packaging. Within DRAM, breakdown Samsung's approach vs. SK Hynix and Micron in using traditional solder bonding vs. hybrid bonding. When is hybrid bonding expected to reach mass adoption, what are th

---

# Hybrid bonding's pivotal moment in semiconductor packaging

**Hybrid bonding for HBM memory remains at roughly 10% yield and zero volume production as of April 2026, but all three major DRAM vendors are racing toward adoption by 2027–2029.** This gap between ambition and execution defines the current state of the technology. Samsung has moved most aggressively—building dedicated hybrid copper bonding (HCB) lines and shipping HBM4 first—but faces severe yield hurdles. SK Hynix is deliberately maximizing its proven MR-MUF process while treating hybrid bonding as a next-generation backup. BESI, the dominant equipment supplier with ~67% die-to-wafer market share, stands to see its hybrid bonding revenue grow from €36M in 2023 to potentially €400M+ by 2027–2028, but the trajectory hinges on a critical variable: when JEDEC finalizes HBM4E/HBM5 thickness standards, which could accelerate or delay the entire transition by one to two years.

## Conclusion

Hybrid bonding for HBM stands at an inflection point defined by a tension between technological necessity and economic reality. The physics is clear: 20+ layer memory stacks will require bumpless interconnects, and every major vendor acknowledges this. But the economics remain challenging—**~10% yields, $3M+ equipment costs, and front-end-grade cleanroom requirements** make hybrid bonding 2–3x more expensive than proven alternatives that JEDEC's relaxed standards continue to enable.

For BESI, the bull case remains intact but time-shifted: hybrid bonding equipment demand is a question of "when," not "if." The company's 67% D2W market share, Applied Materials partnership, and expanding customer base (18 customers, including all three memory majors) position it as the primary beneficiary of any acceleration. The critical watch items are SK Hynix's Kinex system qualification results, Samsung's Cheonan HCB line yield progression, and whether BESI's Gen-2 50nm platform can deliver the throughput improvements memory customers demand. The $2.8 billion equipment TAM by 2030 that BESI projects is achievable but depends on hybrid bonding crossing from pilot to production in HBM within the next 18–24 months.

The most important near-term signal is JEDEC's HBM4E/HBM5 thickness standard, expected to be finalized in late 2026. A relaxation to 825–900µm would push mass hybrid bonding adoption toward 2028–2029 (the HBM5 generation), favoring SK Hynix's conservative MR-MUF strategy and dampening BESI's near-term revenue trajectory. Maintaining the current 775µm standard would validate Samsung's aggressive bet and accelerate equipment demand into 2027. Samsung's and SK Hynix's submission of hybrid-bonded HBM3E samples to NVIDIA for testing, reported in April 2026, suggests the technology qualification cycle has begun regardless of JEDEC decisions.

## BESI versus the competition in hybrid bonding equipment

Emerging competitors include SUSS MicroTec (XBC300 Gen2 D2W platform launched May 2025), Hanmi Semiconductor (investing 100 billion won in a hybrid bonding factory, targeting HBM bonder delivery by end-2027), and Samsung's subsidiary Semes. The competitive landscape is intensifying, but BESI's 150+ installed base, proven production track record at TSMC, and Applied Materials integration create significant switching costs.

**EVG (EV Group)** dominates W2W hybrid bonding with over 70% market share and the largest installed base of wafer bonding solutions worldwide. Its GEMINI FB platform is the industry standard for image sensors and 3D NAND. EVG is entering D2W through collective die-to-wafer (Co-D2W) approaches using carrier wafers, but BESI's direct D2W approach remains better suited for heterogeneous integration and HBM stacking, where dies of different sizes must be bonded. **Tokyo Electron (TEL)** leverages its front-end equipment dominance (cleaning, etching, CMP) to enter the bonding market with its Synapse platform, primarily targeting W2W applications. TEL estimates the bonder TAM at roughly $670 million in 2025, growing to $2 billion by 2030. **ASMPT**, the market leader in thermocompression bonding with 500+ installed TCB tools, shipped its first LITHOBOLT D2W hybrid bonding system to a logic customer in Q3 2024 and is planning second-generation tools for HBM customers—a direct competitive threat to BESI.

BESI's competitive moat is strongest in D2W hybrid bonding, where it holds an estimated **67% market share**. Its partnership with Applied Materials—which took a 9% strategic stake in April 2025 and co-developed the integrated Kinex platform—creates a uniquely comprehensive offering spanning surface preparation, plasma activation, bonding, and metrology in a single inline system. This integration directly addresses the queue-time contamination problem that plagues standalone bonding tools.

## The 10-micrometer cliff and when hybrid bonding becomes unavoidable

The critical question is whether HBM4E will require hybrid bonding. **JEDEC's evolving thickness standards are the single most important variable.** The consortium relaxed HBM4's height limit from 720µm to 775µm in 2025, enabling 16-layer stacking with microbumps by thinning wafers to ~30µm. In April 2026, reports emerged that JEDEC is considering a further relaxation to approximately **825–900µm for HBM4E**, which would allow continued use of cheaper solder-based bonding for 16-layer and potentially even 20-layer stacks. BESI's stock fell 13% on this news. SK Hynix's Lee Kang-seok has stated definitively that "starting from 20-layer stacks, hybrid bonding will become the baseline," but relaxed height standards could push that milestone further out.

The four key bottlenecks limiting mass adoption are well-defined. **Alignment accuracy** for D2W stands at ~100nm today (BESI's production systems), with Gen-2 systems targeting 50nm; sub-1µm pad pitches will demand sub-25nm accuracy that no production tool yet achieves. **Throughput** sits at 1,600–2,000 die placements per hour—adequate for logic but potentially constraining for high-volume HBM production. **Cost** remains 2–3x higher than conventional bonding: hybrid bonders run **~$3 million** versus $1–2 million for thermocompression tools, and require front-end-grade ISO 3 cleanrooms plus additional CMP, plasma activation, and metrology steps. A promising transitional architecture—"hybrid of hybrid"—bonds die pairs face-to-face with hybrid bonding, then stacks them back-to-back with microbumps, potentially bridging the gap.

## Three vendors, three bonding philosophies for HBM

**Samsung: betting on hybrid bonding to leapfrog.** Samsung's aggressive pursuit of hybrid bonding is inseparable from its HBM market share collapse—from **41% in Q2 2024 to just 17% in Q2 2025**—driven by repeated NVIDIA HBM3E qualification failures related to thermal performance. Samsung finally passed NVIDIA's 12-layer HBM3E qualification in approximately September 2025, roughly 18 months after development completion. Its initial mass-production HBM4 (12-layer, shipped February 2026) still uses TC-NCF, but Samsung is constructing a dedicated HCB production line at its Cheonan campus, with equipment arriving in March 2026 and targeting HBM4 16-layer and HBM4E products. Samsung claims HCB reduces thermal resistance by **more than 20%** versus thermocompression bonding—directly addressing the thermal issues that cost it the NVIDIA contract. Samsung's unique vertical integration (in-house 4nm foundry for the logic base die, 1c DRAM, and packaging) gives it flexibility competitors lack, but also means it bears the full technology risk internally.

**Micron: pragmatic silence.** Micron uses TC-NCF for current HBM production and has been notably quiet about specific hybrid bonding timelines. The company licensed hybrid bonding IP from Adeia (formerly Xperi) in 2022 and holds **180+ hybrid bonding patents**, but has made no public commitment to a production timeline. Micron's HBM4 (sampling since June 2025, mass production expected Q2 2026) uses an in-house base die rather than outsourcing to TSMC, and its strategy emphasizes power efficiency—claiming 30% lower power than competitors—over bonding technology leadership. Multiple analysts suggest Micron may be the last major memory vendor to adopt hybrid bonding, likely at HBM5 or later. Micron broke ground on a **$7 billion HBM advanced packaging facility in Singapore** in 2025, with production expected in 2027.

**SK Hynix: "Maximize MR-MUF for as long as possible."** SK Hynix has never used thermocompression bonding for HBM. Its proprietary Mass Reflow with Molded Underfill (MR-MUF) process, co-developed with Japan's Namics Corporation, has been its approach since HBM2E. The batch mass reflow process delivers higher throughput, ~10% better thermal dissipation, and lower bump damage risk compared to Samsung and Micron's TC-NCF approach. VP Lee Kang-seok confirmed that HBM4 (up to 16-layer) will use Advanced MR-MUF, with hybrid bonding **partially introduced for HBM4E 20-layer stacks and fully adopted at HBM5**. SK Hynix placed its first mass-production hybrid bonding equipment order in March 2026—an Applied Materials/BESI Kinex inline system—signaling preparation for the 2027–2028 timeframe. The company holds **53–60% HBM market share** and has sold out its entire 2026 supply, giving it little incentive to rush a technology transition.

## Samsung's yield crisis extends beyond hybrid bonding

Samsung's problems are compounded by yield issues at multiple levels of the HBM stack. Its **1c DRAM yield for HBM4 was approximately 50%** as of November 2025, well below the 70%+ threshold needed for full-scale production (standard DDR5 on the same node achieved over 70%). Its 4nm foundry logic die yield progressed from mid-to-high teens percent to over 90% by late 2025, a remarkable improvement but one that consumed critical time. The interaction of these yields with hybrid bonding's stringent requirements creates a compounding problem: as Professor Yoon noted, "If one out of eight wafers being stacked using hybrid bonding fails, all eight must be scrapped."

The specific technical challenges for hybrid bonding are formidable. A particle of just **1 micrometer creates a bond void of 10 millimeters in diameter**. Copper pad surface roughness must be below 0.5 nanometers. Queue time between surface activation and bonding is critical—the Applied Materials/BESI Kinex integrated system reduces this from up to 13 hours to minutes, addressing a major contamination vector. Testing creates a paradox: probing bond pads to verify die quality before bonding can damage the pristine surfaces needed for bonding. Samsung's in-house equipment subsidiary Semes is developing hybrid bonding tools, but according to 36Kr's April 2026 analysis, "the overall quality of Semes' hybrid bonding equipment currently lags behind BESI."

## BESI's financial position and the hybrid bonding revenue inflection

BESI's die-attach equipment segment (which includes hybrid bonding, flip chip, thermocompression, and standard die bonding) constitutes approximately **80% of revenue**. The company does not separately disclose hybrid bonding revenue in financial statements, but the Financial Times reported hybrid bonding revenue of approximately **€36 million in 2023**, with projections reaching **€476 million by 2026**—a figure that implies hybrid bonding would constitute roughly one-third of total revenue. Over **150 hybrid bonding systems** have been installed across 18 customers as of late 2025, including TSMC, Intel, Samsung, and now SK Hynix (which placed its first mass-production order in March 2026).

BESI reported **€591.3 million in FY2025 revenue** (down 2.7% year-over-year) with 63.3% gross margins, but order momentum tells a different story: FY2025 orders reached **€685 million** (+16.8%), with Q4 orders surging 105% year-over-year to €250.4 million. Computing now represents ~50% of revenue, up from ~40% in 2024, with AI applications driving roughly half of all orders.

For revenue modeling, UBS projects BESI revenue reaching **€1.23 billion by 2027** with EBIT margins expanding to 42.3%. BESI's own long-term targets, disclosed at its 2025 Investor Day, call for **€1.5–1.9 billion in revenue** with 40–55% operating margins. The company projects demand for **1,400 hybrid bonding systems by 2030**, implying a total equipment market of approximately **€2.8 billion**.

System ASPs run approximately **$3 million** for current 100nm-accuracy platforms, with the Gen-2 50nm system (shipped to a leading Taiwanese foundry in Q4 2025) commanding a ~20% premium at an estimated **$3.6 million**. BESI's Gen-2 system represents a significant technology step: at 50nm placement accuracy, it enables the sub-5µm pitches that next-generation logic and HBM4E will require.

---

## Related
- [[Sectors/Semiconductors]]

## Related Sectors
- [[Sectors/Semiconductor Capital Equipment]] — Back-reference: cited in sector hub under Product-level vendor map (advanced packaging & assembly — BESI vs ASMPT/SUSS/Hanmi/Samsung Semes), M&A history (AMAT 9% BESI stake; LRCX/AMAT dual takeover interest), and Insight #3 (hybrid bonding market model, revenue inflection, JEDEC binary).
- [[Sectors/Semiconductor Foundries]] — Back-reference: cited in sector fill under Competitive dynamics (advanced packaging as second foundry franchise — CoWoS 35K → 130K wpm, 100% Taiwan), Product level analysis (TSMC SoIC-X hybrid bonding roadmap; AMAT/BESI Kinex co-platform), Acquisitions and new entrants (AMAT 9% BESI stake as foundry-adjacent equipment consolidation), and Related Research as packaging-economics primary source.
