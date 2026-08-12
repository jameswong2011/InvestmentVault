---
publish: true
date: 2026-05-15
tags: [thesis, mlcc, semiconductors, passives, 6981]
status: active
conviction: medium
sector: MLCC & Power Semiconductors
ticker: 6981
fmp_symbol: 6981.T
source: Murata IR FY2026 results + multi-source web research 2026-05-15
key_metrics_last_refreshed: 2026-07-12
snapshot_of: "[[Theses/6981 - Murata Manufacturing]]"
snapshot_date: 2026-08-12
snapshot_trigger: sync
snapshot_batch: sync-2026-08-12-213539

---

# 6981 - Murata Manufacturing

## Summary
Consensus models Murata as a saturated passive-components supplier with growth pegged to smartphone units and a slow erosion in commodity MLCC share to Chinese suppliers. The non-consensus read: small-form-factor MLCC mix shift (008004, 0201) into AI server boards and EVs is decoupling Murata's volume and ASP trajectory from smartphone units entirely. A GB200 NVL72 rack consumes ~440,000 MLCCs versus ~1,300 per iPhone — one AI rack equals ~340 smartphones of MLCC content, and Murata holds the dominant share precisely in the small-case parts AI boards require. Add 50% Murata share of EV MLCCs at 3-5x ICE content and the structural unit ramp is more durable than the trailing-multiple price implies. At ¥17.95T market cap (~$116B) and ~77x trailing FY2026 earnings, the market has already re-rated Murata well past the smartphone-cycle name it was priced as at thesis inception (¥4.66T, ~20x); the AI-server/EV durability case is no longer a catalyst to wait for but a premium already capitalised, shifting the question to whether ~77x is too much to pay for a durability that must compound for years to justify the multiple.

## Key Non-consensus Insights
- **AI server MLCC volume swamps smartphone weakness — the math is structural, not cyclical.** Conventional servers used 1,000-3,000 MLCCs per board. GB200 NVL72 uses ~440,000 per rack across 72 GPUs (≈6,100 MLCCs per accelerator socket including power delivery, decoupling, and CoWoS-S substrate filtering). At NVIDIA's projected ~30k-40k Rubin/Blackwell rack shipments through 2027, AI servers alone add ~15-18 billion MLCC units of annual demand — equivalent to ~12-15% of Murata's current annual MLCC volume on top of the smartphone base. Consensus is modeling MLCC growth at 4-6% off smartphone units; AI design-ins suggest 10%+ unit CAGR through 2028 driven by board-content scaling that does not appear in handset shipment forecasts.

- **EV exposure is misclassified as auto-cyclical when it is share-expansion masquerading as cyclicality.** Murata holds ~50% global share of EV-grade MLCCs (high-temperature, automotive-qualified 1206/0805) versus ~33% across the broader MLCC market. EV BOM content is 3-5x ICE vehicles (~10,000 MLCCs per EV versus ~3,000 ICE). At BYD/Tesla/legacy-OEM EV unit run-rates, this segment is growing 20%+ even as global vehicle units stagnate. Sell-side models bucket this inside "Automotive" which carries a cyclical discount; the right framing is "secular content growth at majority share with pricing power tied to AEC-Q200 qualification barriers."

> [!question] 2026-06-11 → Addressed 2026-06-11
> **Prompt:** *Firm up the demand side breakdown on MLCCs by component level.*
>
> **Response:** Built per-platform component-level demand tables (AI rack 440k / EV 10k / iPhone 1,300 MLCCs) decomposing count by function × case size × voltage-temp class, each mapped to Murata share. Count-weighted share (~40% AI / ~34% EV / ~52% iPhone) runs below value-weighted (~48% / ~50% EV-grade / ~57%) because Murata over-indexes the high-ASP small-case + high-V slices — the bottom-up behind the 48% AI-MLCC share in the §Key Metrics forecast. Full analysis: §Business Model & Product Description → "MLCC demand breakdown by component level".

> [!question] 2026-05-15 → Addressed 2026-05-15
> **Prompt:** *Does Murata supply Chinese EV makers, or is there domestic alternatives for MLCCs that are more price competitive for the budget end of Chinese EVs.*
>
> **Response:** Murata supplies Chinese EVs across all tiers but with sharply different share — 60-70% of MLCC BOM in premium (>¥250k RMB) models, 40-50% mid-tier, 15-25% budget — with Sunlord/Walsin/BYD Electronic taking commodity sockets at lower price tiers and Murata locked in only at safety-critical AEC-Q200 sockets (battery management, motor inverter) where domestic suppliers lack qualification. The asymmetric setup: Chinese EV premiumization is an unpriced tailwind, downshift to budget is the asymmetric risk. Full analysis: §Industry Context → "Chinese EV exposure — Murata supplies premium tiers; domestic suppliers serve budget".

- **Chinese commoditization threat is backwards — Murata's lead widens in the parts the market actually wants.** Yageo, Walsin, and Sunlord have closed the gap on 1206/0805 commodity MLCCs (Murata's share in those parts has drifted from 35% to ~25% over five years). But the mix shift in every growth end-market — AI server boards, smartphones, EVs, wearables — is toward 008004/0201 small case sizes where sub-100nm dielectric layer chemistry is the binding constraint. Murata + Samsung Electro-Mechanics control ~85% of 008004 share; Chinese suppliers have not demonstrated comparable yield at that case size despite ¥1T+ of cumulative state-backed capex over the last decade. The "Chinese will commoditize Murata" thesis is true for the parts that are becoming a smaller share of total demand.

> [!question] 2026-05-15 → Addressed 2026-05-15
> **Prompt:** *How do you quantify Murata's edge vs. competitors including Chinese competitors. Is this product quality, reliability delta or simply manufacturing yield and in-field defect advantage.*
>
> **Response:** All four — they are separable and individually measurable: 008004 yield (>95% vs 70-85% Chinese, drives 35% cost gap), in-field DPM (<0.1 vs 1-10, compounds catastrophically at AI-rack part counts), AEC-Q200 platform installed base (hundreds vs dozens, non-transferable across designs), and dielectric chemistry IP (40-year iteration, 10+ years to close). The edges reinforce — a competitor must neutralize all four simultaneously to dislodge Murata at premium tiers. Full analysis: §Industry Context → "Quantifying the moat — four distinct edges that compound".

> [!question] 2026-05-15 → Addressed 2026-05-15
> **Prompt:** *What does Murata's product / segment level market share look like. Are they a specialist in high end products and have disproportionately higher market share there?*
>
> **Response:** Yes — Murata is a premium-tier specialist whose share rises monotonically with technical difficulty across all three axes: case size (50% at 008004 vs 15% at 1206/0805), application (50-60% in EV-grade / AI server / premium iPhone vs ~15% in commodity consumer), and reliability tier (~50% automotive-150°C vs ~15-20% consumer commodity). Chinese share gains have come exclusively from the commodity end; in premium buckets Murata has held or expanded share over five years. Full analysis: §Industry Context → "Murata's specialist share profile — share concentrates at the segments with growing demand".

- **Lead time persistence at 12-20 weeks signals durable supply-side discipline, not transient backlog.** Post-2022 inventory drawdown, Murata + TDK + Samsung Electro-Mechanics did not add MLCC capacity at the rate needed to satisfy AI server design-ins. Lead times stretched from 8 weeks (2024) to 12 weeks (2025) to 18-20 weeks on small-case parts (Q1 FY2026). Capacity utilization is 90-95% across the top three. This is not a cyclical inventory squeeze — it reflects a structural under-build relative to AI/EV pull. Pricing on 008004 has firmed for three consecutive quarters; commodity-case pricing remains soft but is a shrinking revenue contribution.

- **Capital intensity is the moat, not the burden.** Murata's barium titanate dielectric slurry chemistry took ~40 years of process iteration to perfect; the production line for 008004 uses sub-micron layer stacking with thousands of layers per part at sub-100nm thickness. This is closer to leading-edge logic process control than to traditional passive components. Chinese suppliers' state-backed capex has gone primarily into adding 1206/0805 capacity (where they were already competitive), not into 008004 chemistry development. The gap is widening, not closing.

## Outstanding Questions
- **What is the verified MLCC content per AI accelerator module across Blackwell → Rubin → Rubin Ultra?** Industry estimates range from 4,000-7,500 per GPU socket including substrate, power delivery, and decoupling. A bottom-up reconciliation from board teardowns (or Murata's design-win commentary) would shift the AI MLCC TAM by ±30%. Answered by: Q3-Q4 FY2026 earnings commentary, board-level teardowns from Asianometry/SemiAnalysis, NVIDIA reference design disclosures.

- **What is Murata's Apple MLCC share post-2023 Samsung Electro-Mechanics share-war?** Apple historically allocated ~60% of iPhone MLCC content to Murata, ~25% to Samsung Electro-Mechanics, ~15% to Taiyo Yuden. Samsung is reported to have aggressively priced into iPhone 17/18 sockets. Answered by: FY2026 Q2/Q3 customer concentration disclosures, supply-chain checks from Nikkei/DigiTimes, Samsung Electro-Mechanics earnings color.

- **How sensitive is Murata gross margin to JPY/USD?** Murata reports in JPY but ~70% of revenue is non-Japan-billed. A 10-yen JPY appreciation against USD shaves ~150-200bps of reported gross margin without any unit-economics change. If JPY strengthens from 145 to 130 in 2026-2027 (BOJ rate normalization), reported margins could compress meaningfully. Answered by: FY26 hedging disclosures, sensitivity tables in IR deck.

- **Is current capex sufficient for AI MLCC ramp?** Murata's annual capex of ¥250-280B funds ~5-7% capacity growth per year. AI server MLCC pull alone implies 10%+ growth need. Either capex accelerates (margin headwind near-term but volume capture) or Murata gives share to Samsung/TDK. Answered by: FY27 capex guidance in May 2026 earnings, fab announcement cadence through 2026-2027.

> [!question] 2026-05-28 → Addressed 2026-05-28
> **Prompt:** *Model AI-related MLCC demand as a proportion of total Murata revenues up to 2035 on both the % sales, and % OP side. Present a forecasted EV/S and EV/EBIT view on the basis of this forecast. What are the assumptions that need to hold for this forecast to be true (AI server growth, MLCC content per server growth).*
>
> **Response:** Demand-led (capex assumed to fund the capacity): AI-MLCC scales from ~9% of sales / ~19% of OP (FY26) to ~43% of sales / ~62% of OP (FY35). Two pricing refinements raise it vs the first cut: (1) ASP-mix ~1.45× (not 1.25×) because the incremental 800VDC content — high-V/008004/auto-grade — prices ~3-5× the baseline rack part; (2) a 2027-29 shortage overshoot (capex lags demand 18-24mo) lifts FY28-30 corporate OPM to ~18-19.5% (+200-300bps over trend, LTA-tempered) and front-loads OP ~15-25% vs a smooth ramp, with partial give-back FY30-31. Static-EV EV/EBIT hits ~10.6x by FY28 / ~4.3x FY35; 17x on FY30 OP implies ~+126% EV upside. Swing risk: capex shortfall → supply-capped ~24%. Full model: §Key Metrics → AI MLCC revenue-mix forecast — demand-led.

> [!question] 2026-05-28 → Addressed 2026-05-28
> **Prompt:** *What is the impact of 800VDC architecture adoption on MLCC demand profile.*
>
> **Response:** 800VDC shifts the MLCC demand profile up every difficulty axis at once — higher voltage rating (sub-100V → 250-1000V bus/DC-link parts), smaller case size (volumetric-efficiency pressure at 300-600 kW racks), higher temperature/reliability (vertical power delivery places parts beside hot GPU/SiC dies, pulling auto-grade 150°C parts into servers), and +2-3× small-case count per rack. Each axis concentrates demand where Murata's share is 50%+ vs 33% blended, so 800VDC mechanically up-mixes both Murata's AI-MLCC share and ASP. Full analysis: §Industry Context → "800VDC architecture — MLCC demand-profile shift"; see also structural force #5 and [[Macro & Technology/800VDC Adoption]].

- **What share of Murata revenue is exposed to Chinese OEM smartphones (Xiaomi, Oppo, Vivo, Honor)?** Estimated 15-25% via direct + indirect channels. Chinese smartphone strength in 2025-2026 has cushioned Apple weakness; reversal would expose Murata to a double smartphone shock. Answered by: end-market disclosures in FY26 results, China shipment data from IDC/Canalys.

- **Has the 2024 inventory cycle on lithium-ion polymer (TLP) batteries and SAW filters fully cleared?** These two product lines reported ~20% volume declines in FY24-FY25 on Chinese smartphone weakness. Recovery cadence affects Functional Devices segment margins. Answered by: Q2 FY26 segment disclosure, channel inventory commentary.

- **Realistic timeline for Yageo/Walsin/Sunlord to demonstrate 008004 at scale?** A 5-year horizon would mean the moat compresses by decade-end; a 10+ year horizon validates structural durability. Industry consensus is 7-10 years for chemistry parity, but Chinese state capacity buildouts in passives are accelerating. Answered by: trade publication monitoring (EE Times, JEITA), patent filings on dielectric chemistry, sample qualifications from major OEMs.

- **Geopolitical risk: would Japanese MLCC exports to China face restrictions analogous to ASML/Tokyo Electron EUV controls?** MLCCs are dual-use components in military and AI systems. Japan has not enacted export controls on passives, but precedent in semicap equipment is concerning. A restriction would simultaneously hurt Murata's China revenue (~30%) and structurally weaken Chinese competitor advancement. Net impact ambiguous. Answered by: METI policy monitoring, trade-restriction precedent watch.

- **Does in-package silicon-capacitor substitution erode Murata's highest-ASP near-die MLCC tier, and has Murata ceded the AI silicon-cap socket to Samsung Electro-Mechanics?** Silicon capacitors (deep-trench/MIM on silicon, ESL ~1-2 orders of magnitude below MLCC) absorb the innermost near-die decoupling role as vertical/backside power delivery pulls decoupling into the package — the 008004/01005 tier (~5,000-10,000 of the 440k rack MLCCs but the 3-5× ASP slice). Murata pioneered the category (IPDiA, 2016; 250nF/mm² in production, roadmap to 4µF/mm²) yet anchored it in medical/aerospace/RF; Samsung Electro-Mechanics signed a ~1.5T KRW (~$1.1B) AI silicon-cap contract (2027-28, undisclosed US AI-chip developer), has supplied Marvell since June 2025, and uniquely bundles MLCC + FC-BGA substrate + silicon cap — the substrate leg Murata lacks. Bounding facts: silicon caps are complementary (cannot replace bulk decoupling; ~$2-3B market vs MLCC ~$15-16B) and Murata retains IPDiA optionality, so the exposure is a slow AI-MLCC ASP-mix haircut + bundling spillover into Murata's AI MLCC sockets, not a core-thesis break. Answered by: Murata silicon-cap / power-module commentary in FY26-27 earnings; Samsung Electro-Mechanics silicon-cap contract cadence; accelerator teardowns quantifying silicon-cap vs near-die MLCC counts per package.

## Business Model & Product Description
Murata Manufacturing makes ceramic-based passive electronic components — predominantly multilayer ceramic capacitors (MLCCs), but also inductors, EMI filters, RF SAW/BAW filters, antennas, connectivity modules (Wi-Fi/BT SoCs sourced + packaged), polymer lithium-ion batteries, MEMS sensors, and piezoelectric devices. Total revenue FY2026: ¥1.83T (+5% YoY), with operating margin 17.5% and net margin ~13%. The simplest analogy: Murata is to passive components what TSMC is to logic fabrication — the volume leader whose process-control IP in a narrow ceramic chemistry niche compounds over decades, leaving newer entrants two generations behind on yield and reliability at the smallest case sizes.

**Product taxonomy by reported segment** (FY2026):

| Segment | Revenue | YoY | Margin | Key products |
|---|---|---|---|---|
| Components | ¥1.01T (55%) | +13% | ~22% OPM | MLCCs (¥936B, +12.6%), inductors, EMI filters |
| Communication Modules | ¥457B (25%) | +5% | ~14% OPM | SAW/BAW filters, antennas, Wi-Fi/BT modules |
| Functional Devices | ¥275B (15%) | -2% | ~6% OPM | Polymer Li-ion batteries (TLP), MEMS, piezoelectric |
| Power & Sensors | ¥91B (5%) | +8% | ~12% OPM | DC-DC converters, current sensors |

**A more useful heuristic — end-market segmentation** (estimated, since Murata does not formally disclose):

| End market | % FY26 revenue | Growth profile | Key dynamic |
|---|---|---|---|
| Smartphones | ~32% | Flat to -3% | Apple ~25%, Samsung ~10%, Chinese OEMs combined ~20% indirect; MLCC content per phone slowly rising (~1,300 in iPhone 17) |
| Automotive/EV | ~28% | +15-20% | 50% share of EV MLCC; ICE→EV content shift drives 3-5x MLCC per vehicle; ADAS adds further passives |
| Datacenter/AI servers | ~14% | +30-40% | Fastest-growing segment; 440k MLCCs per GB200 NVL72; 008004 case-size dominance |
| Industrial/Energy | ~12% | +5-8% | Power semis, solar inverters, robotics |
| Consumer/Other | ~14% | -2% | TVs, wearables, audio; lower-margin commodity-case parts |

**MLCC demand breakdown by component level** (per-platform, estimated from board teardowns + power-delivery-network norms — firms the headline counts of 440k/rack, ~10k/EV, ~1,300/iPhone): the demand-side question that moves the thesis is not how many MLCCs a platform consumes but *which kind*, because Murata's share runs ~50% in small-case low-voltage decoupling and auto-grade high-voltage parts versus ~15-20% in commodity infotainment/body sockets. Decomposing each platform by function × case size × voltage/temperature class:

*AI rack (GB200 NVL72, ~440,000 MLCCs):*

| Function | ~Count/rack | Typical case | Voltage class | Murata share |
|---|---|---|---|---|
| GPU/ASIC core decoupling (PDN) | ~190,000 (43%) | 0201/0402, 008004 near-die | ≤6.3V high-cap | ~40% |
| HBM + CoWoS-S substrate decoupling | ~80,000 (18%) | 008004/0201 | ≤6.3V high-cap | ~47% |
| VRM / power-stage filtering | ~60,000 (14%) | 0402/0603 | 6.3-25V | ~32% |
| High-speed SerDes AC-coupling (NVLink/PCIe) | ~50,000 (11%) | 0201/008004 | ≤16V | ~42% |
| DC-link / bus (48V → 250-1000V at 800VDC) | ~15,000 (3%) | 0805/1206 | 100-1000V | ~47% |
| Clock / PLL / sensor / misc | ~45,000 (10%) | mixed | mixed | ~30% |

The bleeding-edge 008004/01005 subset is ~5,000-10,000 of the 440k today — concentrated in the most space-constrained near-die and CoWoS-S substrate positions — and triples to 15,000-25,000 under 800VDC (structural force #5) as volumetric pressure forces case-size down and a growing fraction of the 0201/0402 bulk migrates to 008004.

*Premium EV (~10,000 MLCCs):*

| Function | ~Count/EV | Typical case | Voltage / temp | Murata share |
|---|---|---|---|---|
| Infotainment / cockpit / displays | ~3,500 (35%) | 0402/0603 | 85-105°C consumer | ~15-20% (contested) |
| ADAS / radar / camera / sensor-fusion SoC | ~2,200 (22%) | 008004/0201 | 125-150°C auto | ~50% |
| Powertrain inverter (SiC/IGBT gate-drive + DC-link) | ~1,300 (13%) | 0805/1206 hi-cap, 0402 gate | 630-1000V, 150°C | ~55% |
| BMS / cell monitoring | ~1,000 (10%) | 0402/0603 | 125°C, safety-critical | ~50% |
| OBC / DC-DC converter | ~800 (8%) | 0603/0805 | 250-650V | ~45% |
| Body / lighting / 12V / misc | ~1,200 (12%) | 0603/0805 | 105°C commodity | ~15% (contested) |

~47% of vehicle count (infotainment + body) is commodity where Sunlord/Walsin compete; the ~53% auto-grade balance (ADAS, inverter, BMS, OBC) is where Murata holds ~50% — matching the note's "50% of EV-grade MLCC" headline once the commodity slice is netted out. EV premiumization grows the auto-grade slices faster (§Industry Context → "Chinese EV exposure").

*Smartphone (iPhone 17, ~1,300 MLCCs):*

| Function | ~Count/phone | Typical case | Murata share |
|---|---|---|---|
| AP/SoC core decoupling | ~450 (35%) | 008004/01005 | ~57% |
| RF front-end (filters/matching, sub-6 + mmWave) | ~300 (23%) | 008004/0201 | ~55% |
| PMIC / power management | ~220 (17%) | 0201/0402 | ~50% |
| Camera modules (multi-cam) | ~170 (13%) | 008004/0201 | ~50% |
| Display / touch / misc | ~160 (12%) | 0402 | ~40% |

~70% of count is 008004/0201 — the iPhone is structurally Murata's highest-share-per-unit platform.

**Count share vs. value share — the reconciliation that matters:** count-weighted Murata share sits below the value-weighted figures the thesis relies on, because Murata over-indexes the high-ASP slices (008004, high-voltage DC-link, auto-grade 150°C):

| Platform | MLCC count/unit | Count-weighted share | Value-weighted share | Source of the gap |
|---|---|---|---|---|
| AI rack | ~440,000 | ~40% | **~48%** | 008004 + high-V DC-link at 3-5× ASP, ~50% share |
| Premium EV | ~10,000 | ~34% | ~45-50% | ~47% of count is commodity (~15-20% share); auto-grade subset ~50% |
| iPhone 17 | ~1,300 | ~52% | ~57% | ~70% of count is 008004/0201 at ~55-60% share |

The AI-rack value-weighted ~48% is exactly the AI-MLCC share assumption carried in the §Key Metrics FY35 forecast — this component-level breakdown is the bottom-up that supports it. The general mechanism: every growth platform's demand concentrates in small-case low-voltage decoupling (AI, phone) or auto-grade high-voltage parts (EV inverter/BMS) — Murata's 50%+ buckets — while the contested commodity slices are a minority of premium-hardware demand and the majority only in budget devices. The blended 33% headline understates per-platform value capture, and the demand mix is shifting toward the parts Murata dominates, not away from them (the component-level mechanism beneath §Industry Context → "specialist share profile").

The flagship product is the 008004 MLCC (0.25mm × 0.125mm, ~3,000 dielectric layers, each <100nm thick). Murata achieves this at yields north of 95% through proprietary barium titanate slurry chemistry and roll-to-roll lamination control. Competitors' 008004 yields are reportedly in the 70-85% range, which makes the part economically unviable at AEC-Q200 quality bars. The 008004 ASP runs ~3-5x a comparable 0402 part on a volume basis, and Murata commands a tier-one premium.

## Industry Context
Global MLCC market: ~$15-16B annually, growing 6-8% in unit terms with mid-single-digit ASP appreciation as mix shifts to smaller case sizes and high-spec parts. Top five suppliers and 2025 share estimates: Murata 33%, Samsung Electro-Mechanics 16%, TDK 12%, Taiyo Yuden 10%, Yageo 10%, Walsin/Sunlord/Chinese long-tail ~19%.

**Competitive dynamics by case size**:
- **008004 (smallest, premium):** Murata 50%, Samsung Electro-Mechanics 35%, TDK 12%, others <3%. Yields and chemistry IP are the binding moat. AI server boards, flagship smartphones, premium EVs.
- **0201 (next-smallest, high-spec):** Murata 40%, Samsung Electro-Mechanics 25%, Taiyo Yuden 15%, others 20%.
- **0402/0603 (mainstream high-spec):** Murata 30%, Samsung Electro-Mechanics 18%, Taiyo Yuden 14%, Yageo 12%, others 26%.
- **1206/0805 (commodity, automotive bulk):** Yageo 20%, Walsin 16%, Murata 15%, Sunlord 12%, others 37%.

**Murata's specialist share profile — share concentrates at the segments with growing demand:** The "33% global MLCC share" headline understates the company's strategic positioning. Decomposed across three axes — case size, application, and reliability tier — Murata's share rises monotonically with technical difficulty:

| Axis | Highest-difficulty bucket | Murata share | Lowest-difficulty bucket | Murata share |
|---|---|---|---|---|
| **Case size** | 008004 | 50% | 1206/0805 | 15% |
| **Application** | EV-grade AEC-Q200 / AI server 008004 / premium iPhone sockets | 50% / 50% / ~60% | Commodity consumer electronics, white-goods | ~15-18% |
| **Reliability tier** | Automotive 150°C+, industrial high-temp | ~50% / ~45% | Consumer commodity, low-spec industrial | ~15-20% |
| **Non-MLCC specialist parts** | BAW filters for sub-6GHz cellular, automotive-grade Li-polymer cells, RF antenna-on-glass for premium phones | 40-55% | Generic SAW filters, commodity inductors | ~10-20% |

Chinese share gains over the last five years have come entirely from the right column — commodity case sizes, consumer-grade reliability, low-spec end markets. Murata has not lost share in any premium bucket; in 008004 share has expanded modestly as 0201 customers migrate up the case-size curve. The structural mismatch the "Chinese commoditization" narrative misses: the parts being commoditized are a shrinking share of forward demand, and the parts growing fastest (small-case, AEC-Q200, high-reliability) are where Murata's lead is widening.

**Quantifying the moat — four distinct edges that compound:** Murata's advantage decomposes into four measurable edges that operate on different timescales and reinforce each other. The question of "is the edge quality, reliability, yield, or chemistry" resolves to all four — but they are separable and individually measurable:

| Edge | Measurable signal | Murata vs. best Chinese competitor | Time to close (industry estimate) |
|---|---|---|---|
| **Yield at smallest case sizes** | 008004 production yield | >95% vs 70-85% | 5-10 years |
| **In-field defect rate (DPM)** | OEM warranty / failure analysis data | <0.1 DPM vs 1-10 DPM | 7-15 years |
| **AEC-Q200 qualification track record** | Platform-design count + duration | Hundreds across 20+ years vs dozens across 5-7 years | 3-5 years per platform, non-transferable |
| **Dielectric chemistry IP** | Patent thicket + 40 years of process iteration | Decades-deep vs reverse-engineering Chinese R&D | 10+ years |

Yield is the binding constraint at premium tiers: at 70% vs 95% yield, the Chinese cost per qualified 008004 part runs ~35% higher before any overhead allocation, eliminating the price advantage on premium sockets even after state subsidies. In-field DPM compounds dramatically with part count — for a 440,000-MLCC AI rack, expected board fail rate at 0.1 DPM is ~4.4%; at 5 DPM it is >80%, which AI server OEMs cannot tolerate at any unit-economics gap. AEC-Q200 qualification platform installed base is non-transferable across designs, locking in stickiness platform-by-platform across thousands of automotive sockets. Chemistry IP is the longest-duration edge — patent thickets around barium titanate dielectrics, sub-100nm layer thickness control, and roll-to-roll lamination would require Chinese suppliers to develop equivalent IP from first principles rather than reverse-engineering finished parts, which state-backed capex has shown no signs of pursuing (CapEx has gone into 1206/0805 capacity expansion, not chemistry R&D).

The four edges reinforce each other: chemistry enables yield, yield enables cost-competitive premium parts, qualification track record creates platform stickiness, low DPM compounds with platform stickiness into OEM trust at design-in. To dislodge Murata at premium tiers, a competitor must neutralize all four simultaneously — a multi-decade challenge even with continued state support.

**Chinese EV exposure — Murata supplies premium tiers; domestic suppliers serve budget:** Murata supplies Chinese EV OEMs across all price tiers but with sharply different content per vehicle:

| Chinese EV tier | Examples | Murata MLCCs per vehicle | Murata share of vehicle MLCC BOM |
|---|---|---|---|
| Premium (>¥250k RMB) | Nio ET7/EC7, Zeekr 001/009, Avatar 12, BYD Yangwang | ~10,000-12,000 | 60-70% |
| Mid-tier (¥150-250k RMB) | BYD Han/Tang, Xpeng P7/G9, Tesla Model 3/Y (China-built) | ~7,000-9,000 | 40-50% |
| Budget (<¥100k RMB) | BYD Seal/Yuan Plus, Geely Geometry, MG4, GAC Aion | ~3,000-5,000 | 15-25% |

Premium Chinese EVs use Murata for safety-critical sockets (battery management, ADAS sensor fusion, motor-control inverter decoupling) where AEC-Q200 150°C-rated spec is non-negotiable, with Sunlord and Walsin filling commodity sockets (12V power supply, infotainment, lighting). Budget Chinese EVs reverse the share split — Sunlord/Walsin take majority at lower-spec ratings (105°C industrial-grade rather than 150°C automotive-grade), and Murata is limited to highest-criticality sockets where qualification has cleared (typically motor inverters and battery management even at the budget tier, because safety regulators require AEC-Q200-equivalent on these systems regardless of vehicle price).

BYD specifically operates an in-house passive components capability via BYD Electronic, but supplies <30% of its own MLCC requirement (primarily commodity case sizes for non-safety-critical sockets). BYD's premium tier (Yangwang U8/U9, Denza N7/N9, Han EV high-spec) sources 008004 and AEC-Q200-qualified parts primarily from Murata and Samsung Electro-Mechanics; commodity content splits across Sunlord, Walsin, and BYD Electronic.

The thesis implication runs against surface intuition: as Chinese EV mix premiumizes (Yangwang, Zeekr, Nio, Denza gaining share at the expense of sub-¥100k budget cars), Murata's effective content per Chinese EV rises even if total China-domiciled MLCC volume sees modest pressure. The asymmetric risk: Chinese consumer downshift to budget vehicles compresses Murata's auto exposure faster than headline EV-unit data implies. The asymmetric tailwind: continued Chinese EV premiumization is an underappreciated structural support that sell-side auto-MLCC models price as flat-share.

**Pricing power trajectory:** Strengthening in 008004/0201 (Murata gaining share in growth case sizes); weakening in 1206/0805 (Chinese commoditization advancing). Net effect on Murata: gross margin mix-up because growth-case parts carry 1.5-2x the GM of commodity-case parts. Murata FY2026 GM at 42.3% vs ~28% three years prior — the mix shift has compounded well past the pace the thesis modeled, the cleanest confirmation of the small-case ASP-mix argument in the P&L.

**Value chain position:** Murata sits between dielectric raw material suppliers (barium titanate from Sakai Chemical, Toda Kogyo) and module/OEM customers. Murata has integrated upstream into its own dielectric slurry production, which is the principal cost and quality differentiator. The merchant BaTiO₃ market it sits above is a three-firm Japanese oligopoly — Sakai Chemical (~25% merchant share), Nippon Chemical Industrial, and Fuji Titanium — that serves the gap between captive supply and total demand; high-spec sub-100 nm AI-grade powder is increasingly merchant-sourced across the industry, underscored by TDK's April 2026 TDK-NCI Advanced Materials JV (TDK 51% / NCI 49%) locking in merchant powder chemistry rather than fully internalising it. Murata's own move runs the other way — it is *deepening* captive integration through the MF Material JV (Murata 35% / Fuji Titanium 55% / Ishihara 10%, BaTiO₃ capacity expansion at Nobeoka for 2027 commissioning), reinforcing rather than diluting the in-house-powder moat that anchors the cost/chemistry differentiator. Downstream, Murata sells direct to OEMs (Apple, NVIDIA, Tesla, BYD), to EMS (Foxconn, Pegatron), and through distributors (Arrow, Avnet) for long-tail customers. Direct-to-OEM channels are 50%+ of revenue and carry pricing-power advantages.

**Structural forces reshaping the industry:**
1. *Small-form-factor mix shift* — every major end-market (AI servers, smartphones, EVs) demands smaller case sizes; this concentrates demand at the top of the supply curve where Murata and Samsung Electro-Mechanics dominate.
2. *Capacity discipline among top suppliers* — post-2022, the top three have held capex flat; lead times stretched; pricing has firmed selectively. Contrasts with prior cycles where suppliers raced to add capacity into downturns.
3. *Chinese supplier advancement at commodity case sizes* — Yageo and Walsin now compete credibly at 1206/0805, but face a multi-year gap at 008004.
4. *AEC-Q200 qualification barriers in auto* — automotive MLCCs face thermal-shock testing, humidity testing, and 15-year reliability requirements; new entrants face 3-5 year qualification cycles per platform. Murata's existing platform installed base compounds.
5. *800VDC AI-rack architecture transition (2H 2026 - 2028 inflection)* — NVIDIA's March 2026 Kyber row-rectified ±400V/800V reference and OCP Mt. Diablo sidecar adoption materially scale per-rack passives content as AI racks migrate from 40-120 kW (Hopper/Blackwell) toward 300-600 kW (Rubin/Rubin Ultra). Component scaling per rack: 008004/01005 MLCC count rises from 5,000-10,000 to 15,000-25,000 (+2-3×); film capacitor content from $500-800 to $2,500-4,000 (+4-5×); SiC MOSFET 1200V die count from 20-40 to 150-250 (+5-8×). The MLCC scaling is the most defensible content-growth vector for Murata because 008004 yield economics (>95% vs 70-85% Chinese competitor) are already cleared — the architecture transition asymmetrically rewards suppliers with proven small-case-size production at automotive/server reliability bars. Combined with the +30-40% datacenter/AI segment growth already in the base case, 800VDC architecture mainstreaming through 2027-2032 ([[Macro & Technology/800VDC Adoption|adoption forecast: 10-15% of new AI racks 2027 → 65-75% by 2032]]) adds a generational compounding mechanism on top of the per-rack 440k-MLCC GB200 NVL72 baseline. See [[Macro & Technology/800VDC Adoption]] for full component-scaling table, value-chain map, and adoption forecast.

**800VDC architecture — MLCC demand-profile shift:** Beyond the raw count scaling (structural force #5 above), the 800VDC transition reshapes *what kind* of MLCCs AI racks demand — pushing the profile up every difficulty axis at once, each of which concentrates demand toward Murata's strongest share buckets:

| Demand-profile axis | Pre-800VDC (48V/12V racks) | Post-800VDC (300-600 kW racks) | Why it favors Murata |
|---|---|---|---|
| **Count (small-case subset)** | 5,000-10,000 per rack | 15,000-25,000 (+2-3×) | 008004 yield economics already cleared (>95% vs 70-85% Chinese) |
| **Voltage rating** | sub-100V decoupling | 250-1000V DC-link / bus parts | High-V small-case is the thinnest Chinese capability |
| **Case size** | mixed 0402/0201 | 008004/01005 (volumetric-efficiency pressure) | Murata 50% share at 008004 vs 33% blended |
| **Temperature / reliability** | consumer / commercial | auto-grade 150°C (VPD places parts beside hot GPU/SiC dies) | Murata's AEC-Q200 installed base transfers directly |

Net effect: 800VDC does not merely add MLCC units — it migrates demand from "many commodity parts" toward "fewer, higher-voltage, smaller-case, higher-reliability, higher-ASP parts," exactly the quadrant where Murata's share is 50%+ rather than the 33% blended figure. The transition therefore up-mixes Murata's AI-MLCC share *and* blended ASP simultaneously — the mechanism behind the margin premium assumed in the FY2035 forecast (§Key Metrics). It also reframes the Chinese-commoditization risk: 800VDC pulls the AI socket further from the commodity case sizes where Yageo/Walsin compete, widening rather than narrowing the relevant moat.

**Pricing of the incremental content:** the added 800VDC parts are not priced at the rack average. High-voltage (250-1000V) DC-link/bus parts, 008004 high-cap, and auto-grade 150°C MLCCs run ~3-5× a baseline 0402/0603 (the note already cites 008004 at 3-5× a 0402), so per-rack MLCC *revenue* content grows faster than the ~2-3× unit count — the structural ASP-mix lift (~1.45×) carried in the §Key Metrics forecast.

A per-rack revenue bridge shows why this is ~3.2×, not the 6-15× a naive read implies — multiplying 2-3× content by the 3-5× premium double-counts (the premium hits only the *added* units, and the 3-5× is vs commodity parts an AI rack already exceeds):

| Step | Calc | Murata MLCC revenue / rack vs traditional |
|---|---|---|
| Naive — total units × commodity premium | (2-3×) × (3-5×) | 6-15× |
| Fix 1 — premium applies to incremental units only | 1 + (1-2) × (3-5) | 4-11× |
| Fix 2 — premium vs rack's already-premium 008004 content (~1.5-2.5×) | 1 + (1-2) × (1.5-2.5) | 2.5-6× |
| **Forecast point estimate (conservative)** | **2.2× content × 1.45× ASP** | **~3.2×** |

The forecast deliberately sits at the low end of the corrected 2.5-6× range: ~3.2×/rack already puts AI-MLCC at 43% of FY35 sales (MLCC TAM tripling); the ~4× midpoint would push AI toward ~50% of sales and a ~4× TAM, straining share/TAM consistency more than it adds signal.

Because the capex super-cycle brings capacity online ~18-24 months after the FY28-30 demand inflection, 2027-29 is also a supply-gap window: small-case ASP runs above trend and Murata's OPM overshoots (a tempered repeat of the 2018 MLCC shortage), front-loading FY28-30 profit before partial give-back as capacity lands.

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | ¥17.95T (~$116B USD) | TSE: 6981; ~1.9B shares × ~¥9,860 |
| EV/Revenue | 9.5x | EV ~¥17.35T; FY2026 revenue ¥1.83T |
| Revenue Growth | +5% YoY (FY2026) | MLCC segment +12.6%; modules +5%; functional devices -2% |
| Gross Margin | 42.3% | Up from ~28% three years prior on mix shift |
| Operating Margin | 17.5% | FY2026; mid-cycle |
| FCF Yield | 1% | Capex ~¥250-280B/yr; FCF ~¥150-180B |
| P/E | ~77x trailing | On ¥234B FY26 net income; a steep premium to TDK (~18x), Taiyo Yuden (~16x) — the AI-MLCC re-rating is now fully in the price |
| ROE | ~10% | Capital-intensive but improving on mix shift |
| Net Cash | ¥800B | Strong balance sheet enables capex flexibility |
| Capex / Revenue | ~14% | Persistently high; the cost of the moat |

### AI MLCC revenue-mix forecast (FY2026 → FY2035) — demand-led
Built bottoms-up from the demand vectors (rack units × MLCC content per rack × ASP), with **capex assumed to catch up** to fund the capacity. Two pricing refinements vs the first cut: (1) the structural ASP-mix factor is raised to **~1.45× (from 1.25×)** because the incremental 800VDC content is the highest-ASP tier — high-voltage (250-1000V), 008004, and auto-grade 150°C parts price at ~3-5× the rack's baseline MLCC (see §Industry Context → "800VDC architecture — MLCC demand-profile shift"); (2) a **2027-29 shortage overshoot** (Murata FY28-30) is layered on, because the capex super-cycle brings capacity online ~18-24 months after the FY28-30 demand inflection — the supply gap is worst exactly then. "AI-MLCC" ≈ ¥170B in FY26 (~9% of revenue, ~18% of MLCC revenue). Driver assumptions: rack units ~17%/yr blended (30% FY26-28 → 8% FY32-35, 4.1× over 9yr); content/rack ~2.2×; ASP-mix ~1.45×; Murata share ~48%.

| Metric (¥B) | FY26 | FY28E | FY30E | FY32E | FY35E |
|---|---|---|---|---|---|
| Total revenue | 1,830 | 2,310 | 3,000 | 3,790 | 4,820 |
| AI-MLCC revenue | 170 | 410 | 840 | 1,390 | 2,080 |
| **AI-MLCC % of sales** | **9.3%** | **17.7%** | **28.0%** | **36.7%** | **43.2%** |
| Corporate OP | 258 | 416 | 585 | 758 | 1,012 |
| Corporate OPM | 14.1% | 18.0% | 19.5% | 20.0% | 21.0% |
| AI-MLCC OP | 48 | 139 | 269 | 417 | 624 |
| **AI-MLCC % of OP** | **18.6%** | **33.4%** | **46.0%** | **55.0%** | **61.7%** |

Reading the OPM path: corporate OPM humps to ~18-19.5% in FY28-30 then keeps rising in absolute terms, but the *shortage premium over trend* is giving back — FY28 carries ~+260bps over the secular mix-up trend (~15.4%), FY30 ~+210bps, and by FY32 the premium is gone (the ~20-21% level is pure secular mix). The ~21% FY35 steady-state ≈ the 2018-19 shortage peak, but structural here rather than cyclical: AI 43% of sales × ~30% OPM + non-AI 57% × ~14% ≈ 21% blended.

Structural punchline: by FY35 AI-MLCC is **~43% of revenue but ~62% of operating profit** — OP share runs 1.4-2× sales share (2.0× FY26 → 1.4× FY35, compressing as AI scales large enough to pull the corporate average toward its own ~30% margin). The 2027-29 shortage front-loads the profit: **corporate OP is ~15-25% higher in FY28-30 than a smooth-ramp model**, and EV/EBIT (below) de-rates fastest in exactly those years. **TAM consistency check:** implies the AI slice of the MLCC market expands ~12× (¥350B → ¥4.3T at 48% share) and total MLCC TAM more than triples by FY35 — driven by rack content and shortage-era pricing, not unit price alone.

**Forward valuation on a static current EV (¥4,400B) — what the forecast implies if the share price does not move:**

| Multiple | FY26 | FY28E | FY30E | FY32E | FY35E |
|---|---|---|---|---|---|
| EV/Sales | 2.40x | 1.90x | 1.47x | 1.16x | 0.91x |
| EV/EBIT | 17.1x | 10.6x | 7.5x | 5.8x | 4.3x |

The shortage hump pulls forward EV/EBIT down to ~10.6x as early as FY28 (vs ~12.8x in the smooth cut) — FY27-29 is the window where the multiple visibly breaks from a smartphone-cycle rating. Mirror view: holding Murata's current ~17x EV/EBIT on FY30 OP implies EV ~¥9.9T (+126% vs ¥4.4T); on FY35 OP at a conservative 15x, ~¥15.2T (+245%). The §Bull Case re-rating (28-30x P/E, ¥10,500-11,500 target) is the near-term expression; the shortage is the catalyst that triggers it.

**Assumptions that must hold for the demand-led base case:**
1. **AI rack-unit shipments compound ~17%/yr blended** (30% FY26-28 → 8% FY32-35) — buildout sustains without a multi-year digestion (the AI-capex-cycle item in §Risks is the primary external threat).
2. **Content per rack ~2.2-2.4×** over the 800VDC transition, back-loaded FY28-32 (adoption 10-15% of racks 2027 → 65-75% by 2032; see §Industry Context → "800VDC architecture — MLCC demand-profile shift" and [[Macro & Technology/800VDC Adoption]]).
3. **ASP-mix ~1.45× (raised from 1.25×)** — incremental 800VDC content (high-V 250-1000V / 008004 / auto-grade 150°C) prices ~3-5× the baseline rack part; partly offset by tier-1 OEM annual price-downs on legacy SKUs.
4. **2027-29 shortage overshoot, LTA-tempered (new).** Capex lands ~18-24mo after the FY28-30 demand inflection, so small-case ASP runs +10-20% above trend and corporate OPM +200-300bps in FY28-30, with partial give-back FY30-31 and a permanent design-in ratchet (800VDC content priced in a tight market sets the platform baseline). Murata captures less than a pure spot supplier did in 2018 (~50%+ revenue is direct-OEM on annual contracts). Reverses to a *downside* if demand digests mid-shortage — stranded capacity + price give-back (see §Risks).
5. **Murata holds ~48% AI-MLCC share** — 008004 moat intact; Chinese closure 7-10yr out (breach = the CLOSE trigger).
6. **Capex catches up (the swing assumption)** — ~¥550-700B/yr FY28-32 (capex/revenue ~18-20% vs ~14% today), FCF yield ~1-2% in build years. **If not, reverts to supply-capped (~¥880B AI-MLCC, ~24% of sales by FY35) and demand flows to Samsung Electro-Mechanics / TDK** (see §Outstanding Questions, capex sufficiency; §Risks, capex super-cycle).
7. **AI-MLCC margin premium persists (~28-30% base OPM)** and **JPY stable** — model is in JPY; sharp appreciation (§Outstanding Questions, JPY sensitivity) compresses reported figures without changing unit economics.

## Bull Case
AI server design-ins compound through 2028 as Rubin/Rubin Ultra ramp; MLCC content per accelerator scales further with higher-bandwidth memory subsystems (HBM4/5) requiring more decoupling. EV ramp executes globally with BYD, Tesla, and legacy OEMs at projected unit run-rates; Murata holds 50% share with 3-5x ICE content. Small-form-factor mix shift drives consolidated GM to 33-34% by FY2029. Smartphone units stabilize or accelerate modestly on a 2027 AI-iPhone supercycle. Revenue CAGR through FY2029 at 11-13%; EPS CAGR at 15-17% on margin expansion. Multiple re-rates to 28-30x as growth durability becomes consensus. Implied price target: ¥10,500-11,500 vs current ~¥7,640 (~40-50% upside). ¥6.5-7T market cap.

## Bear Case
Chinese suppliers close 008004 chemistry gap faster than expected (3-5 year horizon); pricing on small-case parts compresses 10-15% by FY2028. Smartphone weakness persists through 2027 (no AI-iPhone supercycle; Chinese smartphone unit growth reverses); Murata's smartphone exposure drags on consolidated growth. EV unit volumes disappoint on tariff escalation, demand fatigue, or pricing wars; auto MLCC growth slows from +18% to +8%. AI capex cycle peaks in 2026 and contracts in 2027 (hyperscaler capex digestion); MLCC unit pull moderates. JPY appreciates from 145 to 125 against USD on BOJ normalization, compressing reported margins by 250-300bps without any unit-economics deterioration. Revenue growth slows to 3-5%; GM compresses back to ~28%. Multiple de-rates to 16-18x. Implied price target: ¥4,500-5,000 (~35-40% downside). ¥3T market cap.

## Catalysts
- **Q1 FY2027 earnings (Jul/Aug 2026):** Book-to-bill ratio, lead time updates, segment-level MLCC growth, AI/datacenter mention frequency. First clean read on whether the AI MLCC ramp is sustaining.
- **NVIDIA Rubin platform launch (2H 2026):** Volume ramp begins late CY2026; first-quarter MLCC pull commentary expected in Murata Q3 FY27 (Oct-Dec 2026 results).
- **FY2027 capex guidance (May 2026 results):** Acceleration would signal AI demand pull confirmation; flat capex would imply share donation to Samsung Electro-Mechanics.
- **Apple iPhone 18 launch (Sep 2026):** TLP/SAW filter share commentary; MLCC content per phone trajectory; Apple capex run-rate signaling.
- **BYD / Tesla / legacy-OEM EV unit volumes (monthly):** Direct correlation to Murata's auto/EV MLCC pull-through.
- **Samsung Electro-Mechanics earnings (quarterly):** Direct competitor commentary on AI server design-ins and Apple share would inform Murata's relative positioning.
- **METI export-control announcements:** Any policy signal on passives or ceramic-electronics could materially shift China revenue exposure and competitor advancement timeline.

## Risks
- **Thesis risk — Chinese 008004 capability acceleration.** If Yageo, Sunlord, or Walsin demonstrates production-scale 008004 with comparable yields and AEC-Q200 qualification within 3-5 years rather than 7-10, the chemistry moat compresses rapidly and Murata's mix-shift tailwind reverses. Most likely scenario for thesis invalidation.
- **Position risk — JPY appreciation.** Murata reports in JPY; ~70% of revenue is non-Japan-billed. A 10-yen JPY appreciation against USD shaves ~150-200bps of reported gross margin. BOJ normalization timing is the primary FX risk.
- **Thesis risk — AI capex cycle digestion.** If hyperscaler AI capex contracts in 2027-2028 after a 2024-2026 buildout cycle, MLCC unit pull from AI servers decelerates from +30% to single digits. The structural-volume thesis was built off projected NVIDIA/AMD accelerator shipment ramps; a digestion year compresses Murata's growth premium.
- **Execution risk — Murata's own capex super-cycle, plus shortage cyclicality.** The demand-led FY35 forecast (§Key Metrics) requires Murata to roughly double capex to ~¥550-700B/yr through FY28-32 (capex/revenue ~18-20% vs ~14%) to fund 12-15%/yr capacity growth — a three-way capacity fight against simultaneous EV and smartphone demand. This compresses FCF yield to ~1-2% in the build years and front-loads execution risk (fab-ramp timing, yield at new 008004 lines). The same capex lag creates a 2027-29 shortage that lifts FY28-30 pricing/OP but gives back in FY30-31 as capacity lands — a 2018→2019-style margin round-trip; if AI demand digests mid-shortage, Murata is left holding stranded capacity into a price-give-back. Under-build instead cedes incremental AI demand to Samsung Electro-Mechanics/TDK and reverts the trajectory to ~24% of sales. The capex decision is the central swing between the demand-led (~43% of sales) and supply-capped (~24%) outcomes.
- **Position risk — Japanese equity drawdowns in risk-off scenarios.** Nikkei tends to underperform global indices in USD risk-off; Murata's ~$116B market cap and large foreign-investor base still amplify drawdowns even when fundamentals are intact — though at ~$116B (re-rated from ~$30B) the deeper index and passive-flow support cushions somewhat versus the smaller-cap name the thesis first modeled.
- **Thesis risk — smartphone unit weakness extends.** If Apple iPhone units stagnate through 2028 and Chinese smartphone share gains stall, ~32% of Murata revenue (smartphones) sees prolonged unit pressure that the AI/EV growth cannot fully offset.
- **Geopolitical risk — Taiwan/China conflict.** Murata operates production facilities in Taiwan (Murata Electronics Taiwan); a Taiwan Strait conflict disrupts both supply and Asian distribution. Long-tail tail risk but consequential.
- **Customer concentration risk — Apple at ~25%.** Apple is Murata's largest customer; a strategic shift toward Samsung Electro-Mechanics or in-house passive sourcing (unlikely but non-zero) would meaningfully impact Murata's smartphone segment economics.
- **Thesis risk — silicon-capacitor substitution + Samsung's integrated bundle.** As AI power delivery goes vertical/backside, in-package silicon capacitors (deep-trench MIM, ESL ~1-2 orders of magnitude below MLCC) take over the highest-frequency near-die decoupling — the 008004/01005 tier carrying 3-5× ASP that anchors the AI-MLCC mix-up. Murata pioneered silicon caps (IPDiA, 2016) but focused them on medical/aerospace and ceded the AI socket: Samsung Electro-Mechanics signed a ~1.5T KRW (~$1.1B) AI silicon-cap contract (2027-28), supplies Marvell, and is the only vendor bundling MLCC + FC-BGA substrate + silicon cap — a package-level power-integrity offer Murata cannot match without a leading-edge substrate business (TSMC holds the in-CoWoS deep-trench version). Bounded (silicon caps complementary, ~$2-3B market, IPDiA optionality intact), but it reframes Samsung from commodity MLCC share-taker into a structurally sharper AI competitor and drags on the premium tip of the AI-MLCC content story. See [[Sectors/MLCC & Power Semiconductors]].

## Conviction Triggers
<!-- Pre-defined, falsifiable if/then statements. Review each time you update the thesis. -->
- **→ HIGH if**: AI server MLCC content per accelerator verified at 5,000+ units across Rubin/Rubin Ultra (vs. ~4,500 estimated for Blackwell) in Q3-Q4 FY2026 commentary, AND Murata 008004 capacity utilization stays 95%+ through FY2027, AND Yageo/Sunlord 008004 qualification samples remain absent from major OEMs through FY2027. Confirms three pillars of the structural-volume thesis.
- **→ LOW if**: MLCC ASPs on small-case parts (008004/0201) decline >5% YoY for 2 consecutive quarters, AND Murata lead times collapse below 10 weeks across small-case SKUs, AND consolidated gross margin compresses below 28%. Signals capacity discipline broken or competitor encroachment landing.
- **→ CLOSE if**: Yageo, Sunlord, or Walsin publicly demonstrates 008004 case-size MLCC at scale with comparable yields (>90%) AND wins design-in at a major smartphone or AI server OEM. The chemistry moat is the central thesis pillar; verifiable breach forces exit.

## Mental Models
- **Models applied**: [[Generalist - Overview]] (always) · [[Industry - Semiconductors]] (sector) · [[Lens - Value Layer Monopoly]] (008004 small-case layer position) · [[Lens - Automation & AI Readiness]] (physical / tacit-yield sector overlay). *(First populated 2026-06-27 via stress test.)*
- **Triggers that fired** (each a hypothesis to test, not a verdict):
    - *Generalist · mean-reversion vs trend-continuation* — Murata may be a late-mainstream cyclical (1Y +247%; April-2026 +15-35% hike = units↑+prices↑ shortage) narrated as a structural compounder; the thesis's own FY30-31 give-back concedes embedded cyclicality. Test: does small-case ASP hold past the 2027-29 shortage, or round-trip like 2018→2019?
    - *Generalist · ROIIC × runway* — incremental capital earns only ~9-10% ROIC while the demand-led path needs ¥550-700B/yr capex; deploying near cost-of-capital is value-neutral unless the shortage premium is durable. Test: does ROIC inflect above mid-teens as AI-mix scales, or stay pinned ~10%?
    - *Generalist · expectations investing / reverse-DCF* — the "priced at 22.6x, prices ≈zero mix-shift" premise is contradicted by the vault's FMP refresh (~59x NTM P/E, ~37x EV/EBIT NTM); if the higher anchor holds, the re-rate upside is already priced. Test: reconcile clean FY26 OP/EPS to FMP NTM EBIT (run /numbers).
    - *Generalist · base rates / outside view* — a ¥1.8T-rev mature passive maker sustaining ~11% rev CAGR + AI-MLCC 12× to FY35 is a positive outlier to the Mauboussin growth-persistence base rate, starker given current negative rev/EPS growth.
    - *Industry · #1 bottleneck / #7 cycle-phase* — the 2027-29 small-case shortage is a genuine bottleneck call but reads as LATE up-cycle (units↑ prices↑): a cycle trade, not structural compounding.
    - *Industry · #13 classification* — vault rebalancing classifies Murata "semi-cyclical compounder (mature)"; paying a premium multiple at late-mainstream is the #13 error if the structural-compounder read is wrong.
    - *Industry · #2 qualification-gate monopoly* (partly supportive) — 008004 + AEC-Q200 are real structural gates, but protect only the premium slice while blended pricing still declines (net −¥105B); cyclical-scarcity pricing power is being conflated with durable-monopoly pricing power.
    - *Value Layer Monopoly · layer-renter disqualifier + pricing-power evidence* — Murata owns the 008004 layer but pays rent *upward* to single-source materials (release film / BaTiO₃ / Ni powder) that may capture more shortage rent; "100% in-house powder" nuanced by merchant-sourced AI-grade powder → WEAK-to-MODERATE layer monopoly, cleanest rent possibly upstream.
    - *Value Layer Monopoly · layer pioneer out-commercialized in the AI application (silicon caps)* — the near-die in-package decoupling layer is concentrating as power delivery goes vertical (AI-era overlay: infrastructure layer, moat-widening for whoever owns it), yet Murata is the category *pioneer* (IPDiA, 2016) that let the AI socket go to Samsung Electro-Mechanics (~$1.1B 2027-28 contract, Marvell since 6/25) and TSMC (in-CoWoS deep-trench) — owning the technology ≠ owning the layer. Samsung's MLCC + FC-BGA substrate + silicon-cap bundle is the envelopment play Murata can't mirror (no leading-edge substrate). Test: does Murata convert IPDiA into disclosed AI silicon-cap design-ins by FY27, or does the near-die decoupling value migrate to Samsung/TSMC? *(Silicon-cap research 2026-07-09.)*
    - *Automation & AI Readiness · semiconductor split overlay* — Murata's edge is tacit yield/chemistry (durable moat, Anti-fit on operator-automation); the margin-expansion case cannot lean on AI operating leverage — it rests on mix + shortage only.
- **Disconfirming check**: The models broadly agree Murata is a durable small-case-MLCC monopoly riding AI/EV content growth — per the READING PROTOCOL, treat that agreement as the trigger to disconfirm. Bear case / single falsifying datapoint / outside view the thesis must beat: (1) **base rate** — a mature ¥1.8T passive maker at ~10% ROIC with *negative current* growth rarely sustains the modeled S-curve; (2) **falsifying datapoint** — FY28 capex guidance staying ≤¥400B (vs ¥550-700B required) locks the supply-capped ~24%-of-sales path and collapses the demand-led 43% case the ¥10,500-11,500 target depends on; (3) **valuation outside-view** — on the vault's own FMP NTM multiples (~37x EV/EBIT, ~59x P/E) the "cheap, prices zero mix-shift" premise fails and there is no re-rating headroom. *(Stress test [[Research/2026-06-27 - 6981 - Stress Test]], 2026-06-27.)*
- **Evidence update (2026-07-09 batch-2 pass, web-tested)**: the demand/pricing pillars swept their tests while the stress-test's structural vulnerabilities held. *HIGH trigger — all three legs met/tracking*: AI-MLCC content verified ahead of schedule (Rubin ~12,000/board, MI450 count +632% per TrendForce Jun 17); utilization ~95% with orders ~2x capacity and 16–24wk lead times; no Chinese 008004-at-scale qualification (though the yield-gap estimate compressed to 3–4 yrs vs the thesis's 7–10 — watch the CLOSE trigger fire via *domestic-China* server quals first). *LOW trigger decisively refuted — pricing regime FLIPPED*: two hike rounds in one quarter (Apr 1 +15–35%, Jul 1 +10–40%), spot 3–5x on scarce SKUs; the stress-test's "net −¥105B pricing headwind" is stale as of ~May (Goldman: blended 2026 pricing 0–5%+; "MLCC is the next memory"); FY27 guide OP +34.8% / ROIC target 12.3% (the ROIC-pinned-at-10% claim is now in live test). *Vulnerabilities that HELD*: capex still underfunded (¥250B + ¥80B emergency vs ¥550–700B required; Tome plant only ¥9.7B) — currently profit-accretive via scarcity pricing but locking the supply-capped path, kill-trigger tests May 2027; silicon-cap/SEMCO envelopment ESCALATING (SEMCO ~$1.1B silicon-cap contract + first-ever KRW 450B AI-MLCC LTA + substrate bundle; Murata counter = VPD power modules, ¥50B by FY27, CSP talks); valuation re-rated 6x faster than modeled from a premium base — ¥10,310, ~81x TTM, MS PT ¥12,500 — the re-rate hypothesis played out, so forward return now rides the earnings path exactly as the stress test framed. Smartphone-decoupling claim CONFIRMED in the harshest test (China 618 −13%, Xiaomi/Oppo/Vivo target cuts — yet FY27 OP guided +35%). Next test: Q1 FY27 print late July (hike flow-through); `/numbers 6981` still owed (Key Metrics stale on every line).

## Related Research
- [[Sectors/MLCC & Power Semiconductors]] — primary sector note; Murata is the #1 incumbent and majority share holder
- [[Sectors/Compute & AI Compute Accelerators]] — AI server MLCC pull originates from NVIDIA accelerator design-ins
- [[Sectors/Neoclouds & GPU-as-a-Service]] — neocloud capex demand pattern feeds MLCC unit pull through NVIDIA supply chain
- [[AI Bubble Risk and Semiconductor Valuations]] — AI demand durability is the central macro variable for the AI server MLCC pillar
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]] — Tier 4 cyclical challenger (mature); TRIM Low→1-2% (800VDC MLCC scaling + 50% EV share real, but ROIC 9% rich vs multiple)
- [[Research/2026-06-05 - AI-Grade MLCC Upstream Pricing Power - deep-dive]] — Upstream-materials bottleneck map (release film / BaTiO₃ / Ni powder); positions Murata as the demand anchor while arguing single-source materials suppliers may capture more shortage rent. MF Material JV (Murata 35%) + TDK-NCI JV detail in §Industry Context → Value chain position
- [[Research/2026-06-27 - 6981 - Stress Test]] — Adversarial short case: upside is a re-rate off a 22.6x anchor contradicted by the vault's own FMP refresh (~59x NTM P/E); demand-led 43%-of-sales path unfunded (mgmt capex ~¥330B vs ¥550-700B); 2/7 bull assumptions 🔴. Conviction flagged weakened (not changed). Mental-models lenses applied (Generalist / Industry-Semis / Value-Layer-Monopoly / AI-Readiness)
- [[Research/2026-07-11 - Murata vs MLCC Peers - Process and Yield Moat Comparison]] — Head-to-head process/cost/yield moat vs SEMCO / TDK / Taiyo Yuden / Yageo / Chinese cohort: edge is a gradient (huge vs China at 008004, only 5-10pp vs SEMCO, narrowest ~45/40 in AI-server MLCC), ascribed to sole 100%-in-house sub-100nm BaTiO₃ powder + tacit sinter chemistry; moat is a lead not a monopoly in the growth segment. Conviction unchanged (high)

## Legacy Callouts
<!-- Auto-managed by /archive-callouts. Addressed callouts older than the sweep threshold (default 180 days) are moved here from their original sections as plain bulleted entries: `- **<addressed-date>** · <type> · <section> · raised <fresh-date> → <body>` with a `**Response:**` sub-bullet. Sorted descending (newest first). Do NOT hand-edit. To exempt a callout from sweeping, add `[[pinned]]` to its header in-place. -->

## Log
<!-- Format: [source/trigger]: [what changed] — [conviction impact: unchanged/strengthened/weakened + 1 reason] -->
### 2026-05-15
- Initial thesis created. Conviction: medium — AI server MLCC content scaling (440k per GB200 NVL72) and 50% EV MLCC share at 3-5x ICE content underwrite a structural volume case decoupled from smartphone units; chemistry moat at 008004 case size is intact but timeline for Chinese closure is the central uncertainty.
- Addressed user callouts: §Key Non-consensus Insights (×3 fresh `[!question]` callouts on Chinese EV exposure, moat quantification, segment-level share specialism). Added three new subsections to §Industry Context — specialist share profile by axis (case-size/application/reliability), four-edge moat decomposition (yield/DPM/AEC-Q200 platform base/chemistry IP) with closure-time estimates, and Chinese EV tier-by-tier content table (premium 60-70% share / mid-tier 40-50% / budget 15-25%). Conviction: unchanged — analysis reinforces structural thesis (Murata's share concentrates monotonically in fastest-growing segments; moat is multi-dimensional rather than single-axis; Chinese EV premiumization is an unpriced tailwind, downshift is the asymmetric risk).

### 2026-05-19 (/sync)
- Cross-thesis propagation from [[Macro & Technology/800VDC Adoption]]: Macro note created 2026-05-18 + enhanced 2026-05-19 with two new financial columns (AI-DC Rev/OP exposure %, ROIC/EV-EBIT LTM) across all six Layer tables in §Value chain map and named beneficiaries. Murata appears in TWO layers: Layer 5 (Last 1.5 mm / VPD module, ~28% / ~33% AI-DC Rev/OP) AND Layer 6 (Passives — high-cap MLCC ~33% share); ROIC ~10% / EV-EBIT ~14x sits at a discount to Tier 1 AI-DC pure-plays (VRT ~28x, VICR ~50x) reflecting the diversified passives portfolio mix. Quantitative anchor for the existing §Industry Context §5 "800VDC AI-rack architecture transition" subsection where MLCC count per rack scales from 5,000-10,000 (Hopper/Blackwell) to 15,000-25,000 (Rubin/Rubin Ultra) — the macro's adoption forecast (10-15% of new AI racks 2027 → 65-75% by 2032) anchors the FY30 AI-server MLCC demand 3.3× FY25 trajectory. Conviction unchanged at medium — strengthens existing structural-volume thesis without resolving Chinese 008004 closure-timing or JPY-strengthening overhangs.

### 2026-05-22 (manual)
- Status change: portfolio-wide alignment — confirmed as current Live Portfolio holding; conviction medium→high.

### 2026-05-26
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]]: Rebalancing flags TRIM to 1-2% (structural-volume thesis real but ROIC 9% + negative growth makes the rich multiple uncomfortable) — sizing call; conviction unchanged (high).

### 2026-05-28
- Addressed user callouts: §Outstanding Questions (×2 fresh `[!question]` — AI-MLCC revenue-mix model to 2035; 800VDC impact on MLCC demand profile). Built base-case AI-MLCC forecast in §Key Metrics (AI-MLCC 9.3%→23.5% of sales, 18.6%→38.1% of OP by FY35; OP share ~1.6-2× sales share on 28-30% premium-part margin; static-EV forward EV/EBIT 17x→6x implies market prices ≈zero of mix shift) and added an 800VDC MLCC demand-profile-shift table to §Industry Context (count/voltage/case-size/temperature axes all concentrate demand toward Murata's 50%+ buckets). Conviction: unchanged (high) — quantifies the existing structural-volume thesis; does not resolve Chinese 008004 closure-timing or JPY overhangs.
- Reframed the §Key Metrics AI-MLCC forecast demand-led per user finding that the initial cut implicitly assumed only ~5.6%/yr AI rack-unit growth — inconsistent with the 800VDC 2-3× content commentary. New base case multiplies the three demand vectors explicitly (rack units ~17%/yr × content/rack ~2.2× × ASP ~1.25× → ~31% AI-MLCC revenue CAGR): AI-MLCC reaches ~41% of sales / ~60% of OP by FY35 (was 24%/38%); total-rev CAGR lifts to ~11%/yr; static-EV forward EV/EBIT collapses to ~4.6x (FY35). Capex catch-up is now the explicit swing assumption (~¥550-700B/yr FY28-32 peak, FCF yield ~1-2% in build years); added §Risks capex super-cycle / FCF-compression item. Conviction: unchanged (high) — larger upside, more execution-dependent; supply-capped reversion (~24% of sales) is the downside if capex lags.
- Refined the §Key Metrics forecast for MLCC pricing per user challenge on the 2-3× content: (1) raised the structural ASP-mix factor 1.25×→~1.45× (incremental 800VDC content — high-V/008004/auto-grade — prices ~3-5× the baseline rack part); (2) layered a 2027-29 shortage overshoot (capex lags demand 18-24mo → FY28-30 corporate OPM ~18-19.5%, +200-300bps over trend, LTA-tempered) with partial give-back FY30-31 + permanent design-in ratchet. Revised endpoints: AI-MLCC ~43% of sales / ~62% of OP by FY35 (was 41%/60%); corporate OP ~15-25% higher in FY28-30 vs the smooth ramp; static-EV EV/EBIT ~10.6x FY28 / ~4.3x FY35. Added pricing note to §Industry Context demand-profile subsection; widened §Risks capex item to cover the shortage→give-back round-trip. Conviction: unchanged (high).
- Added a per-rack MLCC revenue bridge to §Industry Context (per user query on 2-3× content × 3-5× price): reconciles the naive 6-15×/rack down to the forecast's ~3.2× — the 3-5× premium applies only to incremental units (not the whole rack) and is measured vs commodity parts an AI rack already exceeds (incremental premium ~1.5-2.5× vs the rack's own 008004 content). Point estimate unchanged (conservative low end of the corrected 2.5-6×/rack range); no change to headline forecast (43% sales / 62% OP by FY35). Conviction: unchanged (high).

### 2026-05-29
- [[Research/2026-05-29 - Earnings Transcripts vs Thesis - 6 Holdings - synthesis]]: next-year guide (FYE-Mar-27) confirms margin ramp ahead of thesis schedule — rev ¥1,960B (+7%), OP ¥380B (+34.8%, ~19% OPM) on data-center demand + mix; AI-server MLCC "major expansion cycle," 800V→50V→GPU named, small-case share >50%, utilisation 90-95%. Capex ¥250B + ¥80B emergency AI capacity (still below the demand-led bull's ¥550-700B). Conviction unchanged (high).

### 2026-06-05
- [[Research/2026-06-05 - AI-Grade MLCC Upstream Pricing Power - deep-dive]]: upstream-materials map adds merchant-BaTiO₃ oligopoly detail (Sakai ~25%, NCI) + MF Material JV (Murata 35%, Nobeoka 2027) to §Industry Context Value chain — captive-integration moat reinforced, not challenged. Conviction unchanged (high).

### 2026-06-11
- Addressed user callouts: §Key Non-consensus Insights (×1 fresh `[!question]` — firm up demand-side MLCC breakdown by component level). Built per-platform component-level demand tables in §Business Model & Product Description (AI rack 440k / EV 10k / iPhone 1,300 MLCCs, each decomposed by function × case × voltage and mapped to Murata share). Reconciled count-weighted share (~40% AI / ~34% EV / ~52% iPhone) to value-weighted (~48% AI / ~50% EV-grade / ~57% iPhone) — Murata over-indexes high-ASP small-case + high-V slices, providing the bottom-up behind the 48% AI-MLCC share forecast assumption. Conviction: unchanged (high) — firms the demand-side mechanism beneath the existing specialist-share thesis; no new directional claim.

### 2026-06-27
- Stress test [[Research/2026-06-27 - 6981 - Stress Test]]: top vulnerability — the +40-50% upside is a re-rate off a 22.6x anchor the vault's own FMP refresh contradicts (~59x NTM P/E / ~37x EV/EBIT NTM = already premium), while the demand-led 43%-of-sales path is unfunded (mgmt capex ~¥330B vs ¥550-700B required). 2/7 bull assumptions 🔴, 5/7 🟡 — conviction weakened: reassess HIGH (ROIC ~9%, negative current growth, vault rebalancing flags TRIM to 1-2%).
- Filled §Mental Models (user request): applied [[Generalist - Overview]] / [[Industry - Semiconductors]] / [[Lens - Value Layer Monopoly]] / [[Lens - Automation & AI Readiness]] as hypotheses-to-test — mean-reversion-vs-trend, ROIIC×runway, expectations/reverse-DCF, base-rate, #13 classification, and layer-renter disqualifier fired.

### 2026-07-09 (manual)
- Manual edit: silicon-capacitor competitive risk (user research Q). Added §Outstanding Questions + §Risks entries on in-package silicon-cap substitution of the near-die decoupling tier and Samsung Electro-Mechanics' integrated MLCC+FC-BGA-substrate+silicon-cap bundle (Samsung ~1.5T KRW / ~$1.1B AI silicon-cap contract 2027-28, Marvell since 6/25; Murata a pioneer via IPDiA but AI socket ceded; TSMC holds the in-CoWoS deep-trench version). Added §Mental Models fired trigger (Value Layer Monopoly — layer pioneer out-commercialized in the AI application). Bounded risk — silicon caps complementary to MLCC (~$2-3B mkt vs ~$15-16B), IPDiA optionality retained; reframes Samsung as a sharper AI competitor + slow drag on premium AI-MLCC ASP tip. Conviction: unchanged (high) — bear-case addition, no trigger breach; user retains the conviction call. TODO: propagate to [[Sectors/MLCC & Power Semiconductors]] (run /sync + /graph last).

### 2026-07-09
- Mental models pass: batch-2 evidence sweep appended ## Mental Models update — all 3 HIGH legs met/tracking (Rubin ~12K MLCC/board, ~95% utilization, no Chinese 008004 qual), LOW refuted (2 hike rounds in one qtr; stress-test pricing-headwind claim stale), but capex underfund + SEMCO silicon-cap/LTA envelopment held and China gap estimate compressed to 3-4yrs — conviction unchanged (high); Q1 FY27 print late July; /numbers 6981 owed.

### 2026-07-11
- Comparison [[Research/2026-07-11 - Murata vs MLCC Peers - Process and Yield Moat Comparison]]: process/yield moat is a gradient that inverts by tier — huge/structurally capped-open vs China at 008004 (>95% vs 70-85% yield, 7-10yr), moderate/orthogonal vs TDK + Taiyo Yuden (sub-scale or auto-grade niche), but only 5-10pp vs SEMCO and NARROWEST in AI-server MLCC (SEMCO ~40% vs Murata ~45%); ascribed to the only 100%-in-house sub-100nm BaTiO₃ powder + tacit sinter/co-fire chemistry, monetised via yield/DPM/AEC-Q200 stack (MLCC OPM ~18-22% vs SEMCO ~8%). Conviction unchanged (high) — no trigger breach; moat is a lead not a monopoly in the growth segment. Watch: SEMCO silicon-cap+substrate bundle Murata can't mirror + Sinocera powder now in SEMCO/Yageo supply chains. TODO: /numbers 6981 (Key Metrics market cap stale ~3×), /graph last.
- Status change: conviction high → medium — vault-wide multi-agent valuation scoreboard: ~49x fwd P/E / ~44x EV/EBIT vs 15-25x history embeds durable shortage pricing and a decade-plus moat; ROIC ~9-10% and FY26 OP +0.8% read weaker than the multiple demands, and management's own capex (~¥330B) funds only about half the demand-led 43%-of-sales path. Snapshot: [[_Archive/Snapshots/6981 - Murata Manufacturing (pre-status 2026-07-11-063211)]]

### 2026-07-12
- Numbers refresh: 5 metrics updated, 4 material. Gross Margin 30.5%→42.3% (material); Operating Margin 14.1%→17.5% (material); FCF Yield 3-4%→1% (material); Market Cap ¥4.66T→¥17.95T (+285%, material). Summary's "¥4.66T market cap and ~22x FY2026 P/E" framing is now stale (live ~¥17.95T) — flagged for /deepen. Snapshot: [[_Archive/Snapshots/6981 - Murata Manufacturing (pre-numbers 20260712-173653)]]

### 2026-07-12 (/numbers)
- Numbers refresh (2nd same-day pass, fmp_symbol 6981.T verified): 0 rows edited — Market Cap, Revenue Growth, Gross Margin, Operating Margin, FCF Yield all re-render identical to current cell text; no material change since last-hour refresh. Prior Summary staleness flag ("¥4.66T market cap and ~22x FY2026 P/E") still stands, unresolved. Snapshot: [[_Archive/Snapshots/6981 - Murata Manufacturing (pre-numbers 20260712-184025)]]

### 2026-07-12 (/deepen --sync-metrics)
- Metrics synced + 6981 numbers fixed (FMP 6981.T + web-verified ¥17.95T is real, not bad data): corrected Key Metrics — Market Cap USD ~$30B→~$116B, share basis "152M×¥7,640"→"~1.9B×~¥9,860", EV/Rev 2.4x→9.5x (EV ¥4.4T→¥17.35T), P/E 22.6x→~77x trailing — and reconciled Summary/Business Model (rev +9%→+5%, op margin ~14%→17.5%)/Industry Context (GM ~30.5%→42.3%)/Risks to the real cap. The bull-case re-rating has already happened (stock ~77x trailing). FLAGGED, out of sync scope: §Key Metrics forward-valuation model tables still keyed to a stale "¥4.4T static current EV" — needs a full /deepen re-underwrite; and conviction (medium) likely warrants a /status review, as valuation now sits at/above the §Bull Case target (¥10,500-11,500 / ¥6.5-7T cap, already exceeded at ¥9,860 / ¥17.95T). Snapshot: [[_Archive/Snapshots/6981 - Murata Manufacturing (pre-deepen-metrics-sync 2026-07-12-203456)]]
