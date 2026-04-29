---
date: 2026-04-15
tags: [thesis, semiconductors, NAND, SNDK, SanDisk, memory, AI-storage, HBF]
status: active
conviction: medium
sector: NAND Memory & Storage
ticker: SNDK
---

# SanDisk Corporation (SNDK) — The AI Storage Pure-Play Building the Missing Memory Tier

## Summary

$944/share (up ~3,271% from $28 spin-off debut), Q2 FY2026 revenue $3.025B (+61% YoY), gross margins 51.1% guided to 65-67%, and HBF (High-Bandwidth Flash) emerging as a potentially transformative new memory tier for AI inference. SanDisk re-listed on NASDAQ in February 2025 after spinning off from Western Digital and accesses NAND wafers at cost-plus through the Flash Ventures JV with Kioxia, giving it integrated-like economics without full fab ownership. Three questions define the investment case: whether HBF creates a multi-billion-dollar market that doesn't yet exist, whether NAND structural tailwinds sustain through 2027, and whether the margin trajectory is structural (business model transformation) or cyclical (pricing euphoria).

## Key Non-consensus Insights

- **HBF fills Jensen Huang's "completely unserved market" — this is a TAM creation event, not a TAM capture event, and the market is pricing it as an option rather than a probability.** HBF bridges HBM ($8-10/GB, 24-144GB) and enterprise SSDs ($0.10-0.20/GB) with ~$1/GB, 1.6 TB/s bandwidth (within 2.2% of HBM on Llama 3.1 405B inference), and 512GB-1TB per stack. SK Hynix OCP standardization partnership (February 2026) eliminates "Betamax risk" — the two largest NAND and HBM suppliers jointly defining the standard. Samples targeted H2 2026, commercial products early 2027, aligned with NVIDIA Rubin. $12B TAM by 2030 conservative if inference becomes dominant AI workload.

- **The margin trajectory is structural, not cyclical — SanDisk is undergoing a permanent business model transformation.** Gross margins: 22.7% to 29.9% to 51.1%, guided 65-67%. Driven by WD HDD separation, CBA architecture (BiCS8) per-bit economics, accelerating enterprise/AI mix shift, and Optimus premium repositioning. Pre-acquisition SanDisk peaked at 42-43%; 65%+ would be unprecedented in NAND history.

- **The March 2026 TurboQuant selloff was a category error that created a re-entry point — NAND is architecturally immune to KV cache compression.** TurboQuant compresses DRAM-resident KV cache 6x; SanDisk fell 5.7-10% alongside DRAM/HBM names. Zero effect on training data storage (Llama 3 = 2.4 exabytes), checkpoint storage (105GB-18TB per save, every 1-4 hours), enterprise SSD throughput, or model weight storage. Jevons Paradox applies: TurboQuant enables concurrency scaling from 16 to 100 users per H100, context window inflation to 1M-10M tokens, and local AI inference democratization — all increasing aggregate storage demand.

- **SanDisk's consumer brand heritage is an underappreciated pipeline into enterprise qualification — the Stargate program's progress validates this.** 35+ years of procurement relationships with every major OEM convert into enterprise qualification pipelines. Stargate program: 2 hyperscaler qualifications active, 5 more in pipeline. DC SN670 128TB described as "gold standard" for AI inference. Enterprise SSD share at just 4.1% — poised for step-change if 2-3 of the 5 pending quals convert in 2H 2026.

- **Edge AI and local inference create a net-new NAND demand vector that no analyst model has properly sized.** Local inference on Apple M3 Ultra/M4 Max via Q4.2/Q3.6 quantization creates demand for fast storage (model loading, checkpointing, caching) that didn't exist 18 months ago. Microsoft AI PC spec mandates shift average SSD capacity from 512GB to 1-2TB. SanDisk's Edge segment: 61% of revenue, $1.7B in Q2 FY2026, +63% YoY. Entirely outside traditional NAND forecasting models built on unit shipments and rack counts.

## Outstanding Questions

- **Can HBF achieve commercial viability, or will it follow Intel Optane into technology graveyard?** HBF's 2.2%-of-HBM performance on Llama 3.1 405B is compelling in simulation, but Optane also showed promising lab results before failing commercially due to niche TAM, high manufacturing costs, and ecosystem resistance. The critical differences — SK Hynix partnership for standardization, OCP workstream, alignment with NVIDIA Rubin — reduce but don't eliminate this risk. The IC should assess: (1) whether NVIDIA commits to HBF integration on Rubin PCBs, (2) CBA-based manufacturing yields at scale, (3) whether hyperscalers are willing to re-architect their memory hierarchy for a new tier. If the H2 2026 sampling window is missed or yields are poor, the "AI premium" embedded in SanDisk's valuation could evaporate rapidly. *(Sources: [[Research/2026-01-18 - SNDK - Gemini AI Investment Canvas]], [[Research/2026-01-17 - SanDisk HBM and NAND in AI]])*

- **Is the 65–67% gross margin guide sustainable, or is it a cyclical peak that will revert?** NAND gross margins at 65%+ would be unprecedented in industry history. The structural arguments (CBA cost efficiency, mix shift to enterprise, separation from HDD drag) are compelling, but NAND has a 100% historical track record of creating oversupply that crushes margins. If Samsung breaks capex discipline (it has done so in every prior cycle) or YMTC Phase III ramps aggressively, pricing could reverse. The IC should model: (1) SanDisk's margin floor under a severe pricing scenario (the 2022–2023 trough saw single-digit to negative margins), (2) whether the enterprise/AI mix shift genuinely provides structural margin protection, (3) the degree to which LTA contracts vs. spot pricing affect margin durability.

- **At $944/share and ~30x+ trailing earnings, what is the market pricing in — and what breaks?** SanDisk has appreciated ~3,271% from its $28 spin-off debut. Consensus price target is ~$770 (range $600–1,000), meaning the stock already trades above the high end of some analyst targets. The key question is whether the market is pricing SanDisk as an "AI infrastructure" stock (30–40x P/E justified) or a "memory cyclical" (10–15x P/E appropriate). If the cycle turns or HBF disappoints, re-rating to memory cyclical multiples implies 50–70% downside. On forward FY2027 estimates (~$90 EPS consensus), the stock trades at ~10.5x — not expensive if those estimates are achievable.

- **Can SanDisk's enterprise SSD market share inflect from 4.1% to meaningful levels?** SanDisk ranks behind Samsung (35%), Solidigm/SK Hynix (30%), and Micron in enterprise SSD revenue. The Stargate program's 2 hyperscaler quals + 5 in pipeline is promising, but hyperscaler qualification cycles are 12–18 months. Samsung and Micron have deeper data center relationships, dedicated enterprise sales forces, and the bundling advantage of offering DRAM + NAND as a package. SanDisk's 89% customer concentration in top 7 cloud providers creates both opportunity (massive individual contracts) and risk (asymmetric negotiating leverage if they consolidate suppliers).

- **What is the tail risk from Kioxia JV competitive tension?** Kioxia and SanDisk share fabs but compete on controllers, firmware, and enterprise SSD sales. SanDisk's Stargate DC SN670 128TB competes directly with Kioxia's LC9 245TB. If one partner gains significant enterprise share at the other's expense, the incentive to cooperate on shared capacity could erode. Additionally, Kioxia's die-supply model to hyperscalers could undercut SanDisk's finished SSD sales if hyperscalers prefer bare die. The JV extension to 2034 provides structural stability, but competitive friction within the partnership is an underappreciated risk.

- **How does SanDisk compete in a world where Samsung enters HBF?** Samsung has announced aggressive CXL Memory and Z-NAND initiatives. If Samsung, with its 30–35% NAND share and $73.2B capex budget, launches a competitive HBF product, SanDisk's first-mover advantage narrows. Samsung's scale advantage means it can outspend SanDisk 10-to-1 on R&D and manufacturing capacity. The SK Hynix partnership provides some protection through joint standardization, but Samsung has historically bulldozed through standards with volume and pricing.

- **What is the real exposure to algorithmic efficiency compounding?** TurboQuant alone doesn't threaten NAND. But if TurboQuant + Muon optimizer (35% training acceleration, halves GPU requirement) + Block AttnRes + quantization compound, total GPU count per data center drops dramatically → fewer enterprise SSDs per rack. Current evidence favours Jevons Paradox (proliferation > efficiency), but a scenario where algorithmic efficiency gains outpace demand growth is the genuine non-obvious bear case. The IC should monitor aggregate hyperscaler GPU procurement trends as a leading indicator.

## Business Model & Product Description

SanDisk Corporation was founded in Silicon Valley in 1988 (as SunDisk Corp.) by three immigrant technologists: Dr. Eli Harari (Israel), Sanjay Mehrotra (India), and Jack Yuan (Taiwan). Harari had developed critical floating-gate EEPROM technology at Intel that proved the viability of flash memory storage. The team pioneered what Harari called "System Flash" — combining flash memory with a controller to emulate a disk drive. In 1991, SanDisk produced the world's first flash-based SSD (2.5-inch, 20MB, for IBM). The company IPO'd on NASDAQ in November 1995, co-developed the CompactFlash standard, and formed a transformative joint venture with Toshiba (now Kioxia) in 2000 that gave SanDisk guaranteed supply of cutting-edge flash at cost. SanDisk was acquired by Western Digital in May 2016 for ~$16B. After nearly a decade inside the conglomerate, SanDisk was spun back out as an independent public company on February 24, 2025, re-listing on NASDAQ under its original SNDK ticker.

**The Business Model in Analogy:** SanDisk can be understood as "AMD post-spinoff of GlobalFoundries" — a fabless-like designer that accesses manufacturing through a dedicated JV partner at cost-plus economics, competing on product design, firmware, and go-to-market rather than bearing full fab ownership. The Flash Ventures JV with Kioxia (SanDisk holds 49.9%) provides wafers from eight fabs in Japan at cost-plus pricing, giving SanDisk functionally equivalent economics to a fully integrated manufacturer without the capital burden. This is SanDisk's most underappreciated structural advantage.

**Revenue Segments (Q2 FY2026):**

1. **Edge (formerly Client) — 56% of revenue ($1.7B, +63% YoY):** Storage for PCs, smartphones, automotive, and IoT. The largest segment by revenue. Benefiting from the "AI PC" upgrade cycle (Microsoft mandating high-speed storage, average SSD capacity shifting from 512GB to 1–2TB) and edge AI inference requirements. Products include PCIe Gen 4/Gen 5 NVMe client SSDs and UFS 4.0 mobile storage. The "SanDisk Optimus" rebrand at CES 2026 positions these products at premium price points for AI developers and gamers.

2. **Consumer — 30% of revenue ($907M, +52% YoY):** Retail products including SD cards, microSD, USB flash drives, and portable SSDs. SanDisk is the dominant global brand in removable consumer storage. Steady cash flow generator with brand moat. Recent success with co-branded storage for Nintendo Switch 2.

3. **Datacenter — 14% of revenue ($440M, +76% YoY):** Enterprise SSDs for hyperscale data centers and enterprise OEMs. The smallest but fastest-growing and highest-margin segment. The Stargate program's DC SN670 128TB enterprise SSD is the flagship product, described as the "gold standard" for AI inference workloads. BiCS8 QLC Stargate product advancing through hyperscaler qualification. This segment represents the future of SanDisk's margin expansion story.

**Key Product Lines:**

- **DC SN670 "Stargate" Enterprise SSD:** 128TB capacity, BiCS8 QLC NAND, PCIe NVMe interface. Designed for AI inference workloads. Two hyperscaler qualifications active, three more plus a top storage OEM planned for calendar 2026.
- **DC SN861 Enterprise SSD:** PCIe Gen5, 1 DWPD, up to 7.68TB. Competitive but not class-leading (Micron 9550 MAX dominates benchmarks).
- **SanDisk Optimus GX Pro:** Consumer/prosumer NVMe SSD, marketed for AI developers and high-end gaming.
- **High-Bandwidth Flash (HBF):** Pre-revenue, in development with SK Hynix. Combines 3D NAND flash with advanced packaging (TSVs, CBA) to create NAND-based memory with HBM-like bandwidth. 512GB–1TB per stack. Samples targeted H2 2026, commercial products early 2027.

**HBF Technology Deep Dive:**

HBF borrows architectural principles from HBM to create what is effectively "NAND-based HBM." The key innovations:
- **CBA (CMOS directly Bonded to Array):** Memory array and control logic on separate wafers, bonded together. Enables faster, more complex logic to drive memory cells, unlocking parallelism impossible in traditional NAND.
- **Through-Silicon Vias (TSVs):** 16 layers of 3D NAND stacked vertically with thousands of simultaneous data pathways, delivering 1.6 TB/s read bandwidth in Gen 1.
- **Non-volatility advantage:** Unlike HBM (DRAM-based, requires constant refresh power), HBF retains data without power — critical as AI clusters scale to megawatt power envelopes.
- **Performance benchmark:** Within 2.2% of hypothetical unlimited-capacity HBM on Llama 3.1 405B inference. "98% of the performance for 10% of the cost per gigabyte."

**Financial Trajectory:**

| Period | Revenue | Gross Margin | EPS | Key Events |
|--------|---------|-------------|-----|------------|
| Q1 FY2026 (Oct 2025) | $2.31B | 29.9% | $1.22 | Beat consensus; Datacenter +26% QoQ |
| Q2 FY2026 (Jan 2026) | $3.025B | 51.1% | $6.20 | Beat by $350M; 61% YoY growth |
| Q3 FY2026 (guide) | $4.4–4.8B | 65–67% | $12–14 | Acceleration continues |
| FY2027E (consensus) | — | — | ~$90 | At $944 stock, ~10.5x forward |

**Balance Sheet:** Net cash position of $936M (flipped from $500M net debt at separation, 6 months ahead of schedule). WD stake liquidation (February 2026) generated $3.17B for debt reduction. S&P 500 member since November 2025.

## Industry Context

**The AI Memory Hierarchy and the "Missing Middle":**

The AI data center architecture in 2026 has a clearly defined memory hierarchy with a conspicuous gap:

| Tier | Technology | Speed | Capacity | Cost/GB | Purpose |
|------|-----------|-------|----------|---------|---------|
| L1 | GPU Registers/SRAM | Fastest | KB–MB | Extremely high | Active computation |
| L2 | HBM (HBM3E/HBM4) | ~2 TB/s | 24–144GB | $8–10 | GPU-adjacent; model weights, hot KV cache |
| **GAP** | **Nothing exists** | — | — | — | **"Working memory" for inference** |
| L3 | Enterprise SSD (NVMe) | ~14 GB/s | 4–245TB | $0.10–0.20 | Cold storage, training data, checkpoints |
| L4 | HDD | ~0.5 GB/s | 20–30TB | $0.02 | Archive, backup, data lake |

NVIDIA CEO Jensen Huang described this gap as a "completely unserved market" at CES 2026, predicting it could become "the largest storage market in the world." SanDisk's HBF technology is designed to fill this gap with 1.6 TB/s bandwidth and 512GB–1TB capacity at ~$1/GB. If HBF achieves adoption, it creates a market that literally didn't exist before — estimated at $12B by 2030 by industry analysts.

**The NAND Supercycle (2025–2027):**

The current NAND cycle is structurally different from historical boom-bust patterns for three reasons:

1. **Zero-sum capacity allocation between HBM and NAND:** Samsung and SK Hynix are diverting up to 40% of advanced wafer capacity to HBM production. This creates a structural NAND supply constraint enforced by competitors' capital allocation decisions — not voluntary discipline (which always breaks). NAND capex in 2026 is $22.2B (+5% YoY) versus DRAM capex of $61.3B (+14%).

2. **AI demand is secular, not cyclical:** Hyperscaler capex exceeds $660B in 2026. Enterprise SSDs are surpassing smartphones as the single largest NAND end market for the first time. AI training data requirements (Llama 3 = 2.4 exabytes), checkpoint storage (105GB–18TB per save, every 1–4 hours), and inference data serving create sustained, growing demand.

3. **Institutional reluctance to build greenfield NAND capacity:** Post-2022 industry losses ($252B+ cumulative operating losses across the industry) created deep institutional reluctance to fund $10–24B greenfield fabs with 7–10 year payback periods. The only greenfield NAND fab under construction is Micron's Singapore Fab 10B (H2 2028 earliest).

**Pricing evidence:** NAND contract prices rose 55–60% QoQ in Q1 2026. Wafer prices up 246% YoY. A 30TB enterprise TLC SSD surged from $3,062 to $10,950 in 9 months. QLC NAND is backordered by two years. All 2026 production is sold out; customers negotiating 2027 allocations.

**NAND Market Share and Competitive Position:**

SanDisk's ~12% NAND market share makes it the fifth-largest supplier globally (behind Samsung 30–35%, SK Hynix/Solidigm 20–25%, Micron 15–20%, and Kioxia 14%). However, market share understates SanDisk's competitive position because:

1. **Consumer brand dominance:** #1 global brand in removable flash storage. This translates to pricing power and retail channel control that pure-play enterprise suppliers lack.
2. **Flash Ventures access:** Cost-plus wafer economics from Kioxia JV give SanDisk integrated-like margins without integrated-like capex. Combined Kioxia/SanDisk output is ~30% of global NAND bits.
3. **HBF first-mover position:** Only NAND supplier with a commercially-oriented product designed for the HBM-SSD gap, with SK Hynix partnership for standardization.
4. **Pure NAND focus:** Unlike Samsung, Micron, and SK Hynix (whose management attention and capex are split across HBM, DRAM, and NAND), SanDisk directs 100% of R&D and capital toward NAND and flash innovation.

**Enterprise SSD Competitive Landscape:**

| Supplier | Enterprise SSD Share | Key Advantage | Key Weakness |
|----------|---------------------|---------------|--------------|
| Samsung | ~35% | Scale, V9/V10 NAND, bundling with DRAM | Attention split across HBM/DRAM/Foundry |
| Solidigm (SK Hynix) | ~30% | Intel NAND heritage, SK Hynix backing | Integration complexity; HBM-focused parent |
| Micron | ~15-20% | US-based, NVIDIA qualified, 9550 MAX performance | HBM ramp consuming management focus |
| **SanDisk** | **~4.1%** | **CBA/BiCS8 tech, HBF optionality, JV cost structure** | **Scale disadvantage, building enterprise relationships** |
| Kioxia | ~10% | Die-supply model, LC9 245TB, inventor heritage | PE overhang, limited enterprise brand |

The critical observation: SanDisk's enterprise SSD share is disproportionately low relative to its technology position and NAND scale. The Stargate program represents the catalytic effort to close this gap. If 2–3 of the 5 pending hyperscaler qualifications convert in 2H 2026, enterprise SSD revenue could step-change.

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Stock Price | $944.51 | Up ~3,271% from $28 spin-off debut (Feb 2025) |
| Market Cap | ~$200B+ (est.) | Based on $944 × ~212M diluted shares |
| Q2 FY2026 Revenue | $3.025B | +61% YoY, +31% QoQ; beat by $350M |
| Q3 FY2026 Revenue (guide) | $4.4–4.8B | Acceleration continuing |
| Q2 FY2026 Gross Margin | 51.1% | Guided 65–67% for Q3 |
| Q2 FY2026 EPS | $6.20 | vs. $1.22 prior quarter; 71% surprise |
| FY2027E EPS (consensus) | ~$90 | Forward P/E ~10.5x at current price |
| NAND Market Share | ~12% | 5th globally; combined JV ~30% |
| Enterprise SSD Share | ~4.1% | Major growth opportunity via Stargate |
| Net Cash | $936M | Flipped from $500M net debt at spin-off |
| 2026 Capacity | 100% sold out | Firm POs from top 7 customers; 2027 negotiations underway |
| HBF Timeline | Samples H2 2026 | Commercial products early 2027 |

## Bull Case
- **HBF creates a new $12B+ market:** Fills the "missing middle" in AI memory hierarchy; SK Hynix partnership + OCP standardization de-risks adoption
- **Structural margin transformation:** 51.1% → 65–67% gross margins are structural (mix shift, CBA, separation from HDD), not cyclical
- **NAND supercycle extension:** HBM capacity diversion, AI demand, sold-out 2026 capacity sustain pricing through 2027
- **Enterprise SSD share inflection:** Stargate program converting hyperscaler quals could step-change Datacenter revenue in 2H 2026
- **Edge AI demand vector:** AI PCs, local inference, context window inflation create net-new NAND demand not in traditional models
- **Jevons Paradox on efficiency gains:** TurboQuant/algorithmic improvements increase total AI adoption → more storage demand
- **Flash Ventures JV:** Cost-plus wafer economics without full fab capex; extended to 2034
- **Forward P/E ~10.5x on FY2027E:** Not expensive if $90 EPS estimates hold

## Bear Case
- **Stock up 3,271% from spin-off:** Limited margin for error at current levels
- **HBF execution risk:** Pre-revenue technology; if sampling is delayed or yields are poor, AI premium evaporates
- **Cycle timing:** Memory supercycles have never sustained beyond 2–3 years; 65% gross margins are historically unprecedented in NAND
- **Enterprise SSD share is only 4.1%:** Samsung/Solidigm/Micron have entrenched enterprise relationships; qualification takes 12–18 months
- **No HBM diversification:** 100% NAND exposure; cannot participate in the highest-margin memory segment ($98B HBM TAM by 2030)
- **Samsung competitive response:** If Samsung enters HBF with 10x the R&D budget, SanDisk's first-mover advantage narrows rapidly
- **Customer concentration:** 89% of enterprise revenue from top 7 cloud providers; asymmetric negotiating leverage
- **Algorithmic efficiency compounding:** If TurboQuant + Muon + quantization compound → fewer GPUs per DC → fewer SSDs per rack

## Catalysts
- **Q3 FY2026 earnings (April 30, 2026):** Revenue guided $4.4–4.8B with 65–67% gross margins; execution on this guide is the near-term make-or-break
- **HBF sampling milestone (H2 2026):** First silicon samples to hyperscaler/GPU partners; timeline adherence is critical
- **Stargate hyperscaler qualification conversions:** 3 additional qualifications + top storage OEM expected in calendar 2026
- **NVIDIA Rubin architecture reveal:** If HBF integration is confirmed, validates SanDisk's strategic roadmap
- **Flash Memory Summit 2026:** HBF yield data, competitive landscape updates, BiCS roadmap
- **2027 LTA contract announcements:** Shift from spot to long-term agreements would signal pricing durability

## Risks
1. **HBF commercialization failure:** If sampling is delayed, yields are poor, or NVIDIA doesn't adopt, the AI premium in the stock evaporates
2. **Cycle peak and margin reversion:** If NAND pricing reverts to 2023 levels, margins collapse from 65% to single digits; pure NAND exposure amplifies cyclicality
3. **Valuation compression:** If market re-rates from "AI infrastructure" (30x+) to "memory cyclical" (10–15x P/E), 50–70% downside
4. **Samsung competitive entry into HBF:** CXL Memory, Z-NAND, or direct HBF competitor from the industry's largest player
5. **Kioxia JV tension:** Competitive overlap in enterprise SSDs (Stargate vs. LC9) could create friction in shared fab operations
6. **Customer concentration:** 89% enterprise revenue from 7 customers; loss of a major account is disproportionate
7. **Algorithmic efficiency compounding:** Genuine bear scenario if GPU count per data center drops faster than AI adoption grows
8. **Japanese photo-materials supply chain disruption (new, 2026-04-22):** Iran War Hormuz blockade disrupts Japanese PGME/PGMEA solvent supply → threatens PR/BARC/SOH production at Shin-Etsu/TOK/JSR/Fujifilm consumed by the Flash Ventures JV fabs (Yokkaichi + Kitakami). SNDK is 49.9% JV partner with Kioxia; any JV fab-output slippage directly hits SNDK's cost-plus wafer access. PCN requalification cycle ~1 year for standard nodes, longer for BiCS10 332L. Korean alternatives (Chemtronics, Jaewon Industrial) require qualification. See [[Research/2026-04-24 - Iran War Japan Semiconductor Photo Materials Shortage - news]].

## Related Research
- [[Research/2026-01-18 - SNDK - Gemini AI Investment Canvas]] — Comprehensive SanDisk AI storage thesis, HBF technology deep dive, financial analysis
- [[Research/2026-04-15 - SNDK - Investment Evaluation]] — Post-separation assessment, competitive positioning, HBM exclusion analysis
- [[Research/2026-03-31 - SanDisk Valuation Assessment]] — NAND structural shortage thesis, wafer supply-demand model, margin analysis
- [[Research/2026-01-17 - SanDisk HBM and NAND in AI]] — HBF technology analysis, stock attribution, WDC comparison
- [[Research/2026-03-27 - Semis - Gemini TurboQuant Memory Canvas]] — TurboQuant impact on memory demand; Jevons Paradox framework
- [[Research/2026-03-27 - TurboQuant Impact on Memory Demand]] — Full deep-dive: NAND architecturally immune to KV cache compression; reinforces Insight #3 on March 24 selloff as category error; concurrency scaling 16→100 users/H100, context inflation 1M-10M tokens as net-new storage demand
- [[Research/2026-03-28 - AI - Gemini AI Ecosystem Canvas]] — Edge/local AI inference, Muon optimizer, open-source model parity
- [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]] — HBM4 vendor yields; capacity diversion quantification
- [[Research/2025-11-01 - DRAM HBM Competitive Dynamics]] — Samsung/Micron/SK Hynix HBM-vs-NAND capex allocation
- [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]] — HBM shortage dynamics; inference economics
- [[Theses/285A - Kioxia]] — Flash Ventures JV partner; shared thesis dynamics
- [[Sectors/Semiconductor Capital Equipment]] — Sector-level WFE thesis: TEL cryogenic etch for 400-layer NAND in 2026 volume deployment; etch intensity ~5x increase vs 2D NAND; 3D NAND recovery as equipment demand driver
- [[Sectors/NAND Memory & Storage]] — NAND sector note: competitive dynamics, YMTC disruption analysis, HBF category assessment, product-level differentiation
- [[Sectors/Semiconductor Capital Equipment]] — WFE sector hub: hybrid-bonded flash (HBF) as second hybrid-bonding TAM vector; pilot line accelerated H2 2026; TEL cryogenic etch HVM 2026 for 400L NAND; equipment-adjacent secondary sector reference
- [[Research/2026-04-24 - Iran War Japan Semiconductor Photo Materials Shortage - news]] — Iran War naphtha disruption threatens Japanese PR/BARC supply to Flash Ventures JV fabs (Yokkaichi/Kitakami); direct impact on SNDK's cost-plus wafer access

## Log
### 2026-04-16 (NAND sector research sync)
- [NAND sector creation + web research]: Three conviction-relevant findings: (1) SanDisk HBF pilot line accelerated 6 months to H2 2026 (TrendForce Apr 13) — Japan production site, materials/components/equipment ecosystem engagement underway — strengthened, timeline de-risks execution concern. (2) Samsung now developing own HBF — validates category as real market rather than science project, reduces "next Optane" probability; however introduces competitive threat from player with 10x R&D budget — net neutral for conviction, positive for category validation. (3) YMTC at 13% shipment share targeting 15% by end-2026, but Entity List + enterprise qual barriers keep western enterprise/AI market protected — YMTC impact is consumer ASP pressure, which is actually bullish for SanDisk's enterprise mix shift. Additional: NAND Q2 2026 contract prices +70-75% QoQ (TrendForce); "Father of HBM" (KAIST Prof. Joungho Kim) predicts HBF could surpass HBM by 2038; SK Hynix H3 architecture simulation shows 2.69x perf/watt improvement with HBF+HBM hybrid — conviction unchanged (medium), HBF optionality strengthening.

### 2026-04-16 (sector key questions deep dive)
- [[Research/2026-04-16 - NAND Sector Key Questions Deep Dive - deep-dive]]: HBF de-risking accelerates — 5 signals (OCP standard, Samsung patents, pilot acceleration, H3 32→2 GPU benchmark, Kioxia GP Series). NVIDIA Rubin does NOT natively support HBF; first GPU integration late 2027/early 2028. Write endurance ~100K cycles limits Gen1 to read-intensive workloads. YMTC enterprise gap now 16x (15.36TB PCIe 4.0 vs 245TB PCIe 5.0) — enterprise barrier widening, not narrowing. Conviction unchanged (medium); HBF optionality strengthening incrementally, but GPU integration timeline remains the binding constraint.

### 2026-04-15 (SEMICAP cross-thesis sync)
- [SEMICAP thesis]: TEL cryogenic etch enters volume for 400-layer NAND in 2026; etch intensity ~5x vs 2D NAND. WFE $135B CY2026 (+17%) — reinforces bull case: equipment layer investing in NAND production infrastructure.

### 2026-04-15
- [Thesis created]: Split from KIOXIA-SNDK archive. Consolidated ChatGPT/Gemini/Claude/web research. Stock $944 vs $65-70 at original thesis. Q2 FY2026 $3.025B rev, 51.1% GM, $6.20 EPS. HBF OCP standardization kicked off. Conviction medium — HBF + NAND tailwinds offset by extreme valuation and cycle risk.

### 2026-04-15 (BESI cross-thesis sync)
- [BESI hybrid bonding research]: Samsung licensing W2W from Changjiang for V10 NAND (420-430 layers) could pressure Kioxia JV manufacturing differentiation. NAND packaging at 26% CAGR — conviction unchanged, indirect impact.

### 2026-04-22
- Sector re-scoped: Semiconductors & Photonics → NAND Memory & Storage (vault-wide subsector taxonomy reorganization).

### 2026-04-22 (Semicap sector rebuild sync)
- Wikilink cleanup: Replaced stale `[[Sectors/Semiconductors]]` parent reference with `[[Sectors/Semiconductor Capital Equipment]]` in Related Research; SNDK remains listed in Semicap sector's Equipment-Adjacent scope (HBF as second hybrid-bonding TAM vector beyond HBM; pilot line accelerated H2 2026). Thesis body unchanged; conviction unchanged.

### 2026-04-23
- Wikilink cleanup: Related Research: `[[Sectors/NAND Flash & Storage]]` → `[[Sectors/NAND Memory & Storage]]` (sector file renamed; rename-only fix). Conviction unchanged.

### 2026-04-23 (/sync — orphan linking)
- [[Research/2026-03-27 - TurboQuant Impact on Memory Demand]]: Validates Insight #3 — SNDK -5.7 to -10% March 24 selloff was category error since TurboQuant compresses DRAM KV cache only; zero effect on training data, checkpoint storage, model-weight storage, or enterprise SSD throughput. Conviction unchanged (medium).

### 2026-04-24 (/sync)
- [[Research/2026-04-24 - Iran War Japan Semiconductor Photo Materials Shortage - news]]: Added Risk #8 — JV-partner-fab Japanese PR/BARC supply chain exposure via Flash Ventures (Yokkaichi + Kitakami). Directly hits cost-plus wafer access if disruption materializes. Conviction unchanged — 12-18mo manageable vulnerability per 2019 HF-dispute precedent, but previously-unmodeled risk on the bull case.
