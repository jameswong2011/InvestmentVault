---
publish: true
date: 2026-05-16
tags: [sector, moc, semiconductors, test-equipment, ATE, backend, ADVT, TER, COHU, HBM]
status: draft
sector: Semiconductor Test Equipment
---
> [!question] 2026-05-17 → Addressed 2026-05-17
> **Prompt:** *Describe what a v93000 machine actually is, what are the tests that it conducts, how hard is it to manufacture by a Chinese cloner if it were able to skip IP protection.*
>
> **Response:** V93000 is Advantest's modular pin-scale tester (Verigy-origin, acquired 2011) running digital, parametric, high-speed-I/O, and HBM-specific tests via PinScale instrument cards on the IG-XL software stack — current generation is EXA Scale (HBM-optimised) with Smart Scale for mid-range SoC. Even with full IP access, a Chinese cloner faces 8-10 years minimum to credible HBM/AI parity — hardware reproduction is the easiest gate (~3-4 years, capex problem), software/applications-engineering replication is harder (5-7 years, tacit-knowledge problem), and 24-36 month memory-vendor re-qualification is the binding constraint. See §Product level analysis → V93000 — architecture, test suite, and clone-feasibility.

> [!question] 2026-05-17 → Addressed 2026-05-17
> **Prompt:** *Explain how does the time needed to test HBM increase superlinearly with the layer count. Shouldn't it just be one to one correlated with die surface area or layer count.*
>
> **Response:** Test time is a sum of sub-tests with different scaling exponents — TSV connectivity verification grows ~N² with fault-isolation patterns, bandwidth pattern test scales with channel-count × pattern-depth (which tightens with target BER per generation), thermal margin sweeps grow faster than linearly with bottom-die thermal coupling, and repair allocation is combinatorially complex in die-count × redundancy resources. The composition compounds: HBM3e → HBM4 is 33% more layers × 67% more bandwidth × tighter BER target × deeper hierarchical-redundancy search space — yielding the observed 1.4-1.8x test-time step-up vs the naïve 1.33x linear-in-layers extrapolation that sell-side models implicitly use. See §Product level analysis → HBM test specifics — why test time is scaling (new scaling-driver table).

# Semiconductor Test Equipment

> **Map of Content.** The production-test layer of the semiconductor value chain: wafer probe, wafer-level burn-in, final test (ATE), and handlers. Distinct from front-end WFE (covered in [[Sectors/Semiconductor Capital Equipment]]) and from photonic-domain test (covered in [[Sectors/Photonic Metrology]]). AI compute capacity is constrained as much by test-cell throughput as by fab wafers. HBM stack test time is scaling **6h → 10h → 14-18h** across HBM3 → HBM3e → HBM4, a test-capacity demand step-function that compounds on top of unit-volume growth. Backend test has historically been treated as commoditised back-of-house. The HBM-driven re-rating that re-rated SEMICAP from "cyclical" to "structural complexity compounder" is the same story playing out one node downstream, and consensus is 12-18 months behind on quantifying it.
>
> The sector is a functional duopoly at the high end (Advantest + Teradyne ≈ 90% of SoC/memory ATE) with a price-disciplined #3 (Cohu) in handlers/contactors and two adjacent pure-plays (FORM, AEHR) already covered as sub-cluster theses in Photonic Metrology and SEMICAP. No US-listed Advantest analog exists, making Advantest itself the cleanest expression of the AI test-capacity thesis, and the gap most directly accretive to the existing SK Hynix HBM thesis.

## Active Theses

- [[Theses/6857 - Advantest]]: HBM final-test monopoly (~95% share); central expression of the HBM4 test-time step-function thesis. Status: draft, conviction medium. Created 2026-05-16.
- [[Theses/TER - Teradyne]]: Custom AI ASIC test (Compute SoC mix 10%→50% in 24 months, UltraFLEXplus shipments doubled in 9 months); first merchant GPU win Q1 2026 breaks Advantest monopoly; HBM wafer test >50% share (Magnum EPIC, structurally distinct from Advantest HBM final test 95%); CPO test capture via Quantifi + UltraFLEXplus Zero-Overhead. Status: draft, conviction medium. Created 2026-05-16. Paired with ADVT as ATE duopoly long: TER as higher-beta catch-up leg at ~9x EV/Rev vs ADVT ~15x.

**Tier 2 candidates (active monitoring, not yet thesis-built):**
- **Cohu (COHU):** Pyramid handlers + recurring contactor business (~50% of revenue, software-like margins). The under-followed Tier-2 name where AI rack thermal-test handler density is the second-derivative growth lever.

**Adjacent active theses (already exist in sister sectors):**
- [[Theses/FORM - FormFactor]]: Probe cards. Covered in [[Sectors/Semiconductor Capital Equipment]] and [[Sectors/Photonic Metrology]]. HBM4 16-Hi probe-touchdown intensity is its central AI-test growth vector.
- [[Theses/AEHR - Aehr Test Systems]]: Wafer-level burn-in. Covered in [[Sectors/Semiconductor Capital Equipment]] and [[Sectors/Photonic Metrology]]. Pivoting from SiC to AI accelerator + silicon-photonics burn-in.

**Adjacent demand drivers:**
- [[Theses/000660 - SK Hynix]]: HBM volume ramp = direct test-capacity demand on Advantest (and to a lesser extent Teradyne Magnum).
- [[Theses/285A - Kioxia]], [[Theses/SNDK - SanDisk]]: NAND wafer test demand (Teradyne Magnum, Advantest T5000-series).
- [[Theses/NVDA - Nvidia]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell Technology]]: custom AI accelerator test programs driving ATE shipments at both Advantest and Teradyne.
- [[Theses/BESI - BE Semiconductor Industries]]: hybrid-bonding adjacent; post-bond test sequences increasingly drive the test-equipment specification cycle.

---

## Key industry questions

1. **HBM4 test time: does it scale 1.4x or 2x vs HBM3e?** Industry framing today is ~10 hours per HBM3e 8/12-Hi stack final test. HBM4 16-Hi stacks roughly double die count, add 2x bandwidth interface complexity, and require tighter thermal margin verification. Best estimates 14-18 hours per stack. If true, 2027 V93000 capacity demand step-functions roughly 60-80% above what sell-side currently models from pure HBM unit-growth assumptions, and that is the single most consequential modelling variable in the sector.

2. **Advantest HBM share: does it stay ~95% through HBM5?** Advantest V93000 EXA Scale captured HBM3/3e final-test as the de facto platform. Teradyne and FORM joint-venture on wafer-level HBM test (formed 2023) was the first credible competitive response; production traction has been limited. HBM5 hybrid-bonding transition (2028-2029) opens a re-qualification window: if Teradyne wins one of three memory vendors, market share normalises 75/20/5. If Advantest retains all three, the monopoly cements through 2032.

3. **Custom AI ASIC test platform: does Teradyne win share in compute?** Hyperscaler custom silicon (AWS Trainium, Microsoft Maia, Meta MTIA, Google TPU) test programs are split between V93000 and UltraFLEX based on which incumbent the OSAT or design-house uses. UltraFLEX retains structural advantage in mobile-derivative SoC architectures (Apple A/M-series legacy), while V93000 dominates merchant logic and HBM. The custom ASIC market is roughly 50/50 today; directional shifts of ±10pp per year matter materially to forward growth differential.

4. **Cohu contactor recurring revenue: how much higher can mix go?** Contactors (consumable test sockets, ~50% of Cohu revenue) carry gross margins meaningfully above the handler business. AI accelerator thermal-test contactor wear cycles are 3-5x more aggressive than mobile SoC test. If recurring mix moves from ~50% to ~60%+ by 2028 on AI rack test density, Cohu structurally re-rates from cyclical handler vendor to industrial consumables compounder.

5. **China domestic ATE entry: what timeline to credible threat?** Hwatsing Technology (688120 SH, IPO 2020) is the visible Chinese ATE name; Beijing Huafeng and Shanghai Precise Test cover parametric/wafer test at low-end. None compete at production scale for advanced SoC or HBM final test today. Export controls block US/Japan-origin V93000/UltraFLEX shipments for advanced nodes, accelerating domestic effort but starting from a 10+ year capability gap. Parametric and wafer test likely lost to domestic by 2030; final test for AI compute stays Western through 2033+.

6. **Will TSMC internalise final test for CoWoS?** TSMC has incrementally internalised the highest-value packaging operations (CoWoS); the same pattern could extend to final test for chip-on-wafer assemblies. Today TSMC outsources final test to OSATs (ASE, Amkor) who own the ATE relationship. If TSMC builds in-house final test capacity 2027-2029, OSAT ATE purchase decisions consolidate into TSMC, concentrating Advantest/Teradyne customer power but probably not reducing absolute demand.

7. **Universal Robots (Teradyne robotics segment): strategic or distraction?** Acquired 2015 for $285M; revenue ~$300-400M annual run-rate; structurally lower margin than ATE. Teradyne's industrial automation diversification has muted the cyclical earnings recovery during memory test downcycles. 2025 strategic review chatter (unconfirmed) hints at potential divestiture, which would re-pure-play the test business and re-rate the equity.

8. **Test-time-per-die scaling vs Moore's Law inversion.** Front-end Moore's Law cadence has decelerated to ~3 years per node; back-end test-time-per-die has accelerated to ~2 years per doubling (driven by HBM stacks, chiplets, on-die interconnect verification, in-line burn-in). Test capex is becoming the trailing-edge capacity bottleneck, the inverse of the 1990s-2010s pattern where front-end was the constraint and test was over-supplied. This re-rating is structurally similar to what SEMICAP has experienced 2023-2026.

9. **Does the AVGO/MRVL custom silicon design-services model expand the ATE TAM?** Each new merchant AI accelerator program (Sohu, Cerebras WSE, Groq LPU, MTIA, Trainium 3, Maia 200) requires its own bespoke test program development. Test program development cycles run ~6-12 months and consume $5-15M of Advantest/Teradyne services revenue per program. Custom silicon proliferation directly scales the services annuity even before tool shipments.

10. **Photonic test integration into electrical test platforms.** AEHR's wafer-level burn-in is electrical-domain today; FORM's optical probe cards combine electrical and optical contact. Do Advantest or Teradyne acquire photonic-test capability organically or via M&A? Teradyne's 2023 Quantifi Photonics acquisition was a small step; Advantest's FORM partnership on HBM was a precedent for similar photonic partnerships. Sector consolidation 2026-2028 likely involves at least one ATE-photonic-test combination; see also [[Sectors/Photonic Metrology]] §Key industry questions #5.

---

## Industry history

**1960s-1980s: Origins in defence and IDM-captive supply.** Teradyne founded 1960 (Boston) by Alex d'Arbeloff and Nick DeWolf, initially testing transistors for IBM and Western Electric. Advantest's roots in Takeda Riken Industry (1954, Tokyo), renamed Advantest 1985. Both companies emerged from electronic measurement instrumentation: Teradyne from the US bench-instrument tradition (HP, Tektronix); Advantest from Japan's process-control instrumentation cluster (Sanwa Roki, Hitachi precision instruments). Through the 1980s, ATE was IDM-captive supply: Intel, IBM, Motorola, NEC, Toshiba bought test gear in lockstep with logic and memory capacity. Teradyne dominated US-side; Advantest dominated Japan-side; little overlap.

**1990s: DRAM cycle violence, memory-test scale-up.** DRAM consolidation from 20+ producers to 9 by 2000 concentrated memory-test demand. Teradyne acquired Megatest 1995 (memory test platform consolidation); Advantest's T5500 became the global memory-test workhorse. Logic-test platform competition intensified: Teradyne J750 (1992) became the dominant low-pin/microcontroller test platform, still in production volume today, 30+ years later. Test was framed as commodity: equipment lifecycles 10-15 years, no premium for advanced capability.

**2000s: SoC complexity inflection, Verigy spin-out.** Mobile baseband and applications-processor scale (Qualcomm, MediaTek, TI OMAP, Marvell) created a new high-end SoC test segment. Agilent spun out Verigy as a pure-play test company in 2006 (IPO). Verigy's V93000 platform, modular, software-defined, multi-site, became the standard high-end SoC platform; the V93000 outcompeted Teradyne UltraFLEX in Asian merchant logic markets. Advantest acquired Verigy in 2011 for $1.1B all-cash, integrating V93000 as the Advantest high-end logic platform. This acquisition is the single most consequential event in modern ATE history: it gave Advantest the platform that 15 years later dominates HBM final test.

**2010s: Mobile cycle dominance, robotics diversification, OSAT integration.** Apple iPhone and broader smartphone scale (5B+ cumulative units by 2020) made Teradyne UltraFLEX the dominant Apple A-series test platform, a customer concentration that benefitted Teradyne enormously through the 2012-2020 iPhone supercycle and remains material today. Teradyne acquired LitePoint (2011, $580M) for wireless test, and Universal Robots (2015, $285M) + MiR (2018) + Energid (2018) for industrial robotics diversification, a controversial strategic move that capped ATE earnings cyclicality but diluted ROIC and multiple. Cohu acquired Xcerra (2018, $796M) to consolidate the handler/contactor mid-tier; the combined entity captures ~30-40% of handler share globally.

**2020-2022: COVID supply shock, mobile cycle peak, memory test glut.** Smartphone volume peaked 2017-2019; 2020-2022 inventory build then violent destock collapsed memory test demand in 2023 (Teradyne memory revenue down ~50% peak-to-trough). Advantest revenue troughed in calendar 2023 at ~¥486B as mobile and memory cycles bottomed simultaneously. Cohu revenue fell ~30% peak-to-trough as handler demand follows test cell utilisation.

**2023-2024: HBM inflection, Advantest re-rating begins.** SK Hynix HBM2e/HBM3 volume ramp (sole-supplied to NVIDIA Hopper) drove the first HBM-specific final-test capacity demand. Advantest V93000 EXA Scale platform (launched 2018, scaled-up 2022-2024) became the de facto HBM final test standard. FY2024 (ending March 2025) Advantest revenue rebounded to ¥703B (~$5.4B); calendar 2024 stock price tripled from 2023 trough. Teradyne lagged the re-rating: calendar 2024 revenue ~$2.8B, stock roughly flat-to-up modestly. The market began pricing Advantest as an HBM picks-and-shovels play rather than a cyclical ATE vendor; forward multiples expanded from ~15x to ~28x.

**2025: HBM3e ramp, custom AI ASIC proliferation.** SK Hynix HBM3e 8-Hi and 12-Hi shipments scaled into NVIDIA Blackwell. Samsung and Micron added Advantest V93000 capacity to support their HBM3e qualification. AWS Trainium 2, Microsoft Maia 100, Meta MTIA v2, Google TPU v6 all entered production test, and custom AI ASIC test program count doubled vs 2023 baseline. Advantest CY2025 revenue trajectory implied 30%+ YoY growth; Teradyne began signalling its own AI ASIC traction.

**2026: HBM4 program prep, test-time-per-die step-function.** SK Hynix HBM4 12-Hi sample shipments began Q1 2026 (TSMC base-die partnership announced March 2025); 16-Hi mass production targeted 2027. HBM4 test-time-per-stack estimates converging to 14-18 hours vs HBM3e ~10 hours, a 40-80% step-up in test cell-hours per equivalent unit output. Advantest CY2026 revenue guidance from Q4 FY2025 earnings (April 2026, scheduled) the key near-term catalyst. Teradyne Q1 2026 earnings (April 2026) signalled custom AI ASIC test ramp but HBM gap remained material. Cohu CY2025 revenue ~$370M with contactor mix ~50%; AI-driven thermal handler density story not yet visible in headline numbers.

**Pricing-power trajectory.** Advantest V93000 base unit ASP rose from ~$1.5M (2018) to ~$2.5-3.0M (2025), a ~70% increase driven by HBM-specific instrument cards and AI accelerator high-power test capability. Teradyne UltraFLEX ASP scaled ~50% across the same window. Test program development services revenue at Advantest has grown faster than tool shipments: services + spare parts is approaching 35-40% of revenue with structurally higher margins, mirroring the LRCX CSBG / AMAT AGS annuity dynamic in WFE.

---

## Competitive dynamics

### Oligopoly structure

ATE is a functional duopoly between Advantest and Teradyne, with Cohu the price-disciplined #3 in adjacent handler/contactor categories. Sub-segment concentration:

| Sub-segment | #1 Vendor (Share) | #2 Vendor (Share) | #3 / Other |
|---|---|---|---|
| **High-end SoC ATE** | Advantest V93000 (~55%) | Teradyne UltraFLEX (~35%) | Chroma, NI/Cohu (<10%) |
| **HBM final test** | Advantest V93000 (~95%) | Teradyne (FORM JV, <5%) | None at production scale |
| **DRAM/NAND wafer test** | Teradyne Magnum (~50%) | Advantest T5000-series (~40%) | Cohu, Chinese entrants (<10%) |
| **Microcontroller / low-pin ATE** | Teradyne J750 (~60%) | Advantest T2000 (~25%) | Chroma, Cohu (~15%) |
| **Test handlers (thermal)** | Cohu Pyramid (~30%) | Advantest M48xx (~25%) | Aehr FOX-XP (niche), Korean Exatron (~15%) |
| **Test contactors / sockets** | Cohu (~30%) | ISC (Korea, ~20%) | Smiths Interconnect, Yamaichi, Yokowo |
| **Wafer probe cards** | FormFactor (~31%) | MJC / Micronics Japan (~20%) | TSE, Technoprobe (~15%), MPI (~10%) |
| **Wafer-level burn-in** | Aehr FOX-XP (~80% commercial WLBI) | None at scale | Limited captive/IDM tooling |
| **Photonic wafer test** | FormFactor + Aehr (combined leadership) | Quantifi (Teradyne), Keysight | EXFO, niche |

### Structural moats (why ATE pricing power is closer to ASML than to OSAT)

1. **Test program lock-in.** Each chip design has a custom test program written for a specific ATE platform (V93000 vs UltraFLEX vs Magnum). Test programs encode signal-timing, power-supply ramps, voltage-margin sweeps, and pass/fail criteria for thousands of test patterns. Re-porting a test program to a competing platform takes 6-12 months and costs $5-15M per program, and incurs months of re-qualification at the foundry/OSAT. Once a chip is in production on V93000, it stays on V93000 for its full life cycle (typically 5-10 years).

2. **Customer concentration symmetry.** Three memory vendors (SK Hynix, Samsung, Micron) and ~5 leading-edge logic customers (TSMC, Intel, Samsung Foundry, GlobalFoundries, plus hyperscaler custom-silicon design teams) account for 75%+ of ATE purchases. New entrants face the same 5-customer qualification hurdle as WFE vendors, without the 20-year EUV-style co-development runway.

3. **Multi-site test = software-as-moat.** Modern V93000 / UltraFLEX systems test 256-512+ devices in parallel. Multi-site test efficiency is bottlenecked by software (test pattern compression, parallel resource allocation, real-time pass/fail decisioning). Advantest's IG-XL and Teradyne's TestStudio frameworks have accumulated 15-20 years of customer-specific optimisation libraries, replicable in theory, prohibitively expensive in practice for new entrants.

4. **Spare parts + service annuity.** Installed base of ATE tools globally is 30,000+ Advantest + ~20,000 Teradyne systems. Service revenue (calibration, instrument cards, software updates, applications engineering) is a structurally stable double-digit annual revenue stream; Advantest service mix has risen from ~25% (2018) to ~35% (2025) as installed base ages and AI test program complexity rises.

5. **HBM final test is single-vendor-locked.** SK Hynix, Samsung, and Micron all qualified Advantest V93000 EXA Scale as the HBM final test platform 2022-2024. Migrating to a competing platform would require re-qualification with all three memory customers in parallel, a 24-36 month exercise with no clear ROI given Advantest pricing remains tolerable. Effective lock-in is permanent through HBM5.

### Within-segment share dynamics — where shifts actually happen

Following the SEMICAP heuristic that ~80-90% of share shifts occur at node/architecture transitions, ATE share moves at:

- **New chip program tape-outs** (every 12-18 months for hyperscalers): test platform decision made at design phase, locks in 5-10 years of test capacity demand
- **Memory generation transitions** (HBM3 → HBM3e → HBM4 → HBM5): re-qualification window opens for ~12 months per generation
- **OSAT capacity additions**: new OSAT fab build (Amkor AZ, ASE TW expansion) re-opens platform-decision window for new wafer flows
- **Customer-of-record changes**: e.g., NVIDIA shifting custom test partnership from one OSAT to another

The HBM5 hybrid-bonding transition (2028-2029, deferred from earlier per JEDEC 2026 timeline) is the next major re-qualification window for memory test. Teradyne winning even one of the three HBM5 memory vendors would shift the market structure from 95/5 to 65/30/5, a material re-rating event for both Advantest (slight headwind) and Teradyne (material tailwind).

### Chinese ATE — capability gap quantification

| Test Category | Best Chinese Capability (2026) | Western Best-in-Class Gap | Credible Competitor Horizon |
|---|---|---|---|
| Parametric / E-test | Hwatsing (688120 SH) at production scale | Near parity at 14nm+ | Already credible 2026 |
| DRAM/NAND wafer test | Hwatsing + Huafeng pilot lines | 1-2 nodes behind on test pattern density | 2028-2029 |
| Microcontroller ATE | Hwatsing T2000 alternatives at low-pin | At parity for sub-28nm MCU | Already credible 2026 |
| Mid-range SoC ATE | Limited; design wins at sub-tier 1 fabless | 4-6 years behind UltraFLEX/V93000 | 2030+ |
| High-end SoC ATE (AI/HBM) | None at production scale | 6-8 years behind V93000 EXA Scale | 2032+ if achievable at all |
| Test handlers | Multiple domestic vendors | Cohu-equivalent thermal handler 3-4 years out | 2028-2030 |

**Asymmetry vs WFE.** ATE has fewer Chinese entrants than WFE (which has NAURA, AMEC, ACMR, Piotech, SiCarrier as serious players). The capability gap is wider at the high end. Export controls bind harder on ATE because test program development requires Western applications-engineering teams; even if hardware is reverse-engineered, the software/services moat is harder to replicate.

---

## Product level analysis

### Advantest platforms

| Platform | Use Case | ASP (2025) | Customer Concentration | AI Test Relevance |
|---|---|---|---|---|
| **V93000 EXA Scale** | High-end SoC, HBM final test, AI accelerator | $2.5-3.0M base + $0.5-1.5M instrument cards | TSMC, Samsung, SK Hynix, Micron, major hyperscalers | **Critical** — HBM monopoly platform |
| **V93000 Smart Scale** | Mid-range SoC, automotive | $1.5-2.0M | Mobile fabless, automotive | Moderate — overflow capacity |
| **T2000** | Legacy SoC, microcontroller, low-pin | $0.8-1.2M | Chinese mobile, low-cost SoC | Low |
| **T5000 / T5500 series** | DRAM/NAND wafer test, memory characterisation | $1.5-2.5M | All memory vendors | High — non-HBM memory |
| **HA1000** | Memory device-level test | $1.0-1.5M | Memory vendors | Moderate |
| **M48xx handlers** | Final-test thermal handlers | $0.3-0.5M | All ATE customers | High — AI thermal density |
| **Service / spares / applications eng.** | Installed base support | Recurring | All customers | High — sticky annuity |

### Teradyne platforms

| Platform | Use Case | ASP (2025) | Customer Concentration | AI Test Relevance |
|---|---|---|---|---|
| **UltraFLEX Plus / UltraFLEX 5G** | High-end SoC, mobile baseband, custom AI ASIC | $2.0-2.8M | Apple, Qualcomm, MediaTek, hyperscaler custom silicon | **High** — custom AI ASIC ramp |
| **Magnum V** | DRAM/NAND wafer test (high parallel count) | $1.8-2.5M | Micron, Kioxia, SanDisk, Samsung | High — non-HBM memory |
| **J750 / J750Ex-HD** | Microcontroller, automotive, low-pin SoC | $0.5-1.0M | NXP, STM, Infineon, Renesas | Low |
| **ETS-800** | Mixed-signal, analog | $0.8-1.5M | ADI, TXN, ON Semi, Microchip | Low |
| **LitePoint IQxstream** | Wireless test (Wi-Fi, BLE, cellular) | $0.2-0.5M | Mobile OEM, IoT | Low |
| **Universal Robots cobots** | Industrial automation (non-ATE) | Bundle-priced | Manufacturing diversification | None — strategic question |
| **Quantifi Photonics** | Photonic test (post-2023 acquisition) | Early-stage | Sub-scale | Optionality on CPO |

### Cohu platforms

| Platform | Use Case | ASP (2025) | Customer Concentration | AI Test Relevance |
|---|---|---|---|---|
| **Pyramid handlers** | Final-test pick-and-place thermal handlers | $0.3-0.5M | Multi-vendor (handler-agnostic to ATE) | High — AI thermal handling |
| **DIAMONDx** | Test cells (system integration) | $0.4-0.7M | Mid-tier ATE buyers | Moderate |
| **Contactors / sockets (recurring)** | Consumable test contact interface | $50-500 per unit, high volume | Every ATE installation | **Critical recurring revenue** — AI thermal wear cycles |
| **MEMS / RF probe cards (legacy Xcerra)** | Specialised probe | $0.05-0.15M per card | Niche | Moderate |
| **Inspection systems** | Wafer/device inspection | $0.3-0.8M | OSAT, IDM | Moderate |

### V93000 — architecture, test suite, and clone-feasibility

The V93000 originated as Verigy's flagship SoC tester (Agilent spin-out 2006); Advantest acquired Verigy in 2011 for $1.1B and integrated V93000 as its high-end logic and HBM platform. Current generation is **V93000 EXA Scale** (launched 2018, scaled-up 2022-2024 for HBM); **V93000 Smart Scale** is the lower-tier mid-range SoC / automotive configuration.

**Architecture.** Modular rack chassis with a common backplane carrying high-speed digital, analog, and DC signals. Functionality is added through **PinScale instrument cards**: each card provides specific test capabilities and slots into the chassis:

- **Digital pin electronics cards:** drive/sense pin patterns at multi-Gbps rates; pin counts per card range 64-1024+ depending on configuration
- **DC parametric measurement units (PMU):** voltage/current force-and-measure on every pin
- **Power supply instruments:** multiple programmable rails with µA-resolution measurement
- **High-speed I/O cards:** SerDes / HBM / PCIe protocol-aware test up to 32+ Gbps per lane
- **RF instruments:** millimetre-wave and mid-frequency RF test (mobile baseband, Wi-Fi)
- **Thermal control:** ChillX / actively-heated test heads for hot/cold soak

A fully-configured EXA Scale system carries thousands of test pins and consumes 20-40 kW; HBM-optimised configurations add additional high-density digital pin cards to handle the wide TSV interface (1024+ I/O per stack). Test programs are written in the **IG-XL** framework (test patterns, sequencing, pass/fail logic, multi-site coordination).

**Test suite.** The V93000 is platform-agnostic in raw capability but configured per device under test via IG-XL. Test types it conducts:

| Test type | What it verifies | Why it matters |
|---|---|---|
| Digital functional test | Logic correctness — pattern in, pattern out | Catches design bugs, manufacturing defects |
| DC parametric | Voltage thresholds, leakage, current draw per pin | Power integrity, process variation |
| AC parametric | Signal timing, setup/hold, jitter | Speed binning, high-frequency operation |
| High-speed I/O (SerDes) | Multi-Gbps eye diagram, BER | PCIe / HBM / NVLink interface health |
| Memory BIST | Built-in self-test pattern coverage | Embedded SRAM, on-die memory |
| Power integrity | Rail ramp behaviour, droop under load | Voltage regulation, in-rush current |
| Thermal stress | Hot soak (110-125°C) and cold soak (-40°C) operation | Field-temperature reliability |
| TSV continuity (HBM) | Every through-silicon-via interconnect | Stack-level connectivity |
| Bandwidth + refresh (HBM) | Full read/write at rated speed; retention | Performance binning, reliability |
| Repair allocation (HBM) | Identify failing rows/columns, program redundancy | Yield rescue, capacity binning |

For HBM final test specifically, the V93000 executes the 8-step sequence detailed in §HBM test specifics below.

**Multi-site test = software-as-moat.** A single V93000 system tests 256-512+ devices in parallel by interleaving patterns across test sites. Multi-site efficiency is bottlenecked by software: pattern compression, parallel resource allocation, real-time pass/fail decisioning, fault isolation. IG-XL has accumulated 15-20 years of customer-specific optimisation libraries; a hyperscaler custom-silicon test program often runs to >100,000 lines of IG-XL pattern + control logic.

**Clone-feasibility under full IP access.** A Chinese entrant with stolen V93000 schematics, board files, ASIC RTL, and IG-XL source code would still face four sequential gates before reaching production volume:

1. **Hardware reproduction (~3-4 years, $500M-$1B capex).** Pin electronics ASICs (driver/comparator chips) require sub-picosecond timing precision and µA-resolution force/measure circuits, needing deep mixed-signal IC design talent and access to a leading-edge foundry (which itself is export-controlled for advanced ATE applications). PCB and chassis-level interconnect tolerances are achievable in the Chinese ecosystem at low volume with yield/uniformity gap. Thermal and power densities of a fully-loaded chassis sit at HPC-class; Chinese capability exists but rarely at single-vendor scale.

2. **Software re-creation (~2-3 years parallel, but fundamentally limited).** Stealing IG-XL source code doesn't replicate the applications-engineering knowledge base: customer-specific test methodology libraries, pattern compression heuristics, debug workflows, and silicon-correlation calibration data accumulated across thousands of programs over 15-20 years. This is tacit knowledge held by hundreds of Advantest applications engineers globally. Copying source yields a runtime environment without the methodology, analogous to cloning Photoshop's code without the colour-management calibration libraries that make professional output usable.

3. **Customer qualification (24-36 months minimum once hardware ships).** Each memory vendor (SK Hynix, Samsung, Micron) and leading-edge logic customer (TSMC, Intel) runs a multi-quarter qualification: correlate test results against known-good devices, characterise yield impact, validate edge-case patterns, baseline failure-analysis flow. No Western or Korean/Japanese memory vendor has incentive to qualify a Chinese platform unless their primary supply is blocked. China's domestic memory effort (CXMT, YMTC) provides a captive pathway, but those vendors are years from HBM production volume.

4. **Test program portability (6-12 months and $5-15M per design).** Every existing chip in production has a test program written for V93000 IG-XL. Re-porting to a Chinese platform requires re-writing the program, re-validating against silicon, re-correlating with the original platform's pass/fail bins. No fab has incentive to absorb this cost unless mandated. The portability tax effectively excludes the entire installed device base from Chinese ATE addressable market.

Hardware cloning is the easiest gate (3-4 years, money problem). Software gap is harder (5-7 years, talent + customer-base problem). Customer qualification is the binding constraint (8-10 years from credible prototype, requires either coerced customer adoption or a homegrown leading-edge memory/logic ecosystem to scale alongside). The visible Chinese ATE names (Hwatsing, Huafeng, Shanghai Precise Test) sit 6-8 years behind on the hardware gate alone; total time to credible HBM/AI parity exceeds 10 years even with optimistic IP-access assumptions. Cross-reference §Competitive dynamics → Chinese ATE: capability gap quantification for the broader sub-segment view.

### HBM test specifics — why test time is scaling

HBM stack final test sequence:

1. **Power delivery verification:** ramp all rails, verify each die in stack
2. **Through-silicon-via (TSV) connectivity:** test all TSV interconnects across stack
3. **Bandwidth pattern test:** full read/write across all channels at rated speed
4. **Thermal margin sweep:** hot/cold soak with bandwidth testing
5. **Refresh / retention test:** verify each die meets refresh spec
6. **Repair allocation:** identify failing rows/columns, program redundancy mapping
7. **Pseudo-random pattern (PRBS) verification:** long-duration error rate test
8. **Stack-level burn-in** (optional, increasing): accelerated stress test

**Time scaling rationale across HBM generations:**

| Generation | Stacks | Die per Stack | Bandwidth | Est. Final Test Time | Test Cell Demand vs HBM3 |
|---|---|---|---|---|---|
| HBM2e | 8-Hi | 8 | 460 GB/s | ~4 hours | 0.7x baseline |
| HBM3 | 8/12-Hi | 8-12 | 819 GB/s | ~6 hours | 1.0x (baseline) |
| HBM3e | 8/12-Hi | 8-12 | 1.2 TB/s | ~10 hours | ~1.7x |
| HBM4 | 12/16-Hi | 12-16 | 2.0 TB/s | **~14-18 hours** | **~2.5-3.0x** |
| HBM5 (2028+) | 16/20-Hi | 16-20 | 4.0+ TB/s | ~20-24 hours est. | ~3.5-4.0x |

**Why test time scales superlinearly with layer count, not 1:1 with die surface area.** The naïve expectation, that HBM test time should grow proportional to die area or layer count, assumes the test sequence is a single pass over each die. Actual HBM final test is a sum of sub-tests, each with a different scaling exponent in layer count N, bandwidth B, and per-die area A:

| Sub-test | Scaling | Why |
|---|---|---|
| TSV connectivity verification | **≈ N² with fault-isolation patterns** | Each layer-pair has thousands of TSVs; fault diagnosis requires patterns that isolate which TSV in which pair failed. Combinatorial, not linear in N. |
| Bandwidth pattern test | **≈ N × B × pattern depth** | Pattern depth grows with target BER tightening per generation (10⁻¹⁵ → 10⁻¹⁶ → 10⁻¹⁷ ...). HBM4 doubles B vs HBM3e independent of N. |
| Thermal margin sweep | **Grows faster than N** | Bottom dies in deeper stacks operate hotter; thermal coupling complexity rises; sweeps must cover wider envelope with longer dwell times to reach steady-state. |
| Repair allocation | **Combinatorial in N × redundancy resources per die** | Optimal redundancy mapping is an NP-hard search; algorithm runtime scales worse than linearly. HBM4 introduces hierarchical / nested redundancy that further deepens the search space. |
| Refresh / retention | **N × temperature points** | Each die characterised across multiple temperatures; per-die overhead roughly constant, total scales with N. |
| PRBS / long-duration error rate | **∝ 1 / target BER** | Statistical confidence requires bit-volume inversely proportional to target BER. BER targets tighten ~10× every two generations, independent of N. |
| Power delivery verification | **≈ N (rails × dies)** | Roughly linear in N — the only sub-test that matches the naïve linear-in-layers intuition. |

The composition compounds: HBM3e → HBM4 is **33% more layers** (12-Hi → 16-Hi worst case) × **67% more bandwidth** (1.2 → 2.0 TB/s) × tighter BER target × deeper hierarchical-redundancy search. Multiplying these factors yields the observed **1.4-1.8x test-time step-up** vs the naïve 1.33x linear-in-layers extrapolation that consensus sell-side models implicitly use. The same multiplicative dynamic recurs HBM4 → HBM5 (20-Hi, 4 TB/s, hybrid bonding adds TSV-equivalent contact density).

Per-unit test time approximately doubles every two generations. Combined with HBM unit volume CAGR of ~50%+ through 2027, **HBM test cell-hour demand compounds at ~3x per generation**. Sell-side models for Advantest predominantly capture the unit-volume axis but materially under-model the test-time axis.

---

## Acquisitions and new entrants

### Historical M&A (the structural events shaping today's industry)

| Year | Acquirer | Target | Value | Strategic Outcome |
|---|---|---|---|---|
| 2006 (spin-out) | Agilent → Verigy | (Verigy IPO) | n/a | Created pure-play high-end SoC ATE; V93000 platform reached escape velocity |
| 2011 | Advantest | Verigy | $1.1B | **Most consequential ATE deal in modern history** — gave Advantest the platform that 15 years later dominates HBM final test |
| 2011 | Teradyne | LitePoint | $580M | Wireless test diversification; modest revenue contributor today |
| 2015 | Teradyne | Universal Robots | $285M | Industrial robotics diversification; controversial — multiple compression vs pure-play comp |
| 2016 | FormFactor | Cascade Microtech | $355M | Probe-card consolidation; gave FORM analytical/photonic probe optionality |
| 2018 | Teradyne | MiR (Mobile Industrial Robots) | $272M | Robotics expansion; further multiple drag |
| 2018 | Teradyne | Energid Technologies | ~$25M | Robotics software / motion planning |
| 2018 | Cohu | Xcerra | $796M | Created the Cohu of today — consolidated handler + contactor mid-tier |
| 2020 | Advantest | Crocus Technology test business | undisclosed (~$30M) | Niche magnetic memory test capability |
| 2023 | Teradyne | Quantifi Photonics | undisclosed (~$50M) | Toehold in photonic test — sub-scale today |
| 2024 | Advantest | various smaller bolt-ons (HBM-specific instrument card vendors) | undisclosed | Vertical integration of HBM test capability |

### New entrants worth watching

- **Hwatsing Technology (688120 SH):** Chinese ATE; IPO 2020; revenue scaling from low base. Pure parametric/E-test today; targeting wafer test and low-end SoC by 2028. Capability gap to V93000/UltraFLEX is wide but closing under domestic substitution pressure.
- **Beijing Huafeng:** wafer test; sub-tier 1 Chinese fabless customers.
- **Shanghai Precise Test:** parametric, mature node.
- **Chroma ATE (2360 TW):** Taiwan-listed; mid-range SoC, power semiconductor test, EV battery test. Real but niche.
- **MPI Corporation (8147 TW):** probe stations, RF/MMW test; closer to FormFactor's adjacent space.
- **Korean ISC, Yokowo, Smiths Interconnect:** contactor specialists; cohabit Cohu's contactor TAM.

**Potential consolidation paths 2026-2028:**

1. **Cohu acquired by Teradyne or Advantest:** handler + contactor adjacency makes strategic sense for either; Cohu market cap ~$1.5B is digestible. Antitrust likely manageable (handlers/contactors are not at the same monopoly concentration as ATE).
2. **Teradyne divests Universal Robots:** re-pure-plays the test business; would drive re-rating to Advantest-style multiples; market cap could rise $5-10B on re-rating alone.
3. **Advantest acquires photonic test capability:** likely a smaller bolt-on rather than a FORM-scale acquisition; could be a Quantifi-equivalent target or a FORM partnership extension.
4. **FORM acquired by Advantest or Teradyne:** discussed periodically; FORM's $4-5B market cap is digestible for either; antitrust uncertain given probe card concentration.

---

## Macro shifts

1. **AI compute capex driving HBM test demand 30-50% CAGR through 2027.** Hyperscaler 2026 capex $600-750B (per [[Sectors/Semiconductor Capital Equipment]] #6), 75% AI-directed. HBM is the gating component for AI compute deployment. Memory vendor capex (Samsung $20B, SK Hynix $20.5B, Micron $13.5B 2026) flows into Advantest V93000 final test capacity. Each $1B of HBM capex maps to roughly $200-300M of Advantest revenue across tools + services.

2. **Custom AI ASIC proliferation broadening SoC test TAM.** AWS Trainium 3, Microsoft Maia 200, Meta MTIA v3, Google TPU v7, Apple AJAX, Tesla Dojo 2, plus merchant accelerators (NVIDIA Rubin, AMD MI400, Intel Gaudi 4, Cerebras WSE-4, Groq LPU v2, Sohu, Tenstorrent). Each program = 6-12 months of test program development = $5-15M services revenue per program before tool shipments. Custom ASIC volume = recurring tool demand thereafter.

3. **US export controls (October 2022 + tightening 2024-2026) blocking China high-end ATE access.** Advantest V93000 EXA Scale and Teradyne UltraFLEX shipments to China subject to entity-list restrictions for advanced nodes. The counter-intuitive net effect is that export controls have accelerated Chinese domestic ATE development (Hwatsing scaling) but more critically have prevented Chinese fabs from absorbing AI test demand, concentrating that demand at TSMC/Samsung/Intel and their OSAT/test partners, all of which remain locked-in V93000/UltraFLEX users.

4. **TSMC backend consolidation (CoWoS internalisation).** TSMC's progressive internalisation of CoWoS packaging is extending to final test. Currently TSMC outsources final test to OSAT partners (ASE, Amkor, SPIL). If TSMC internalises CoWoS final test 2027-2029, ATE purchase decisions consolidate from 5-7 OSATs to TSMC + 2-3 OSATs, concentrating customer power but not reducing volume. Likely net neutral to slightly negative for ATE margins.

5. **HBM5 hybrid bonding transition (2028-2029) reopening qualification window.** Per [[Sectors/Semiconductor Capital Equipment]] #5, JEDEC's April 2026 package thickness relaxation deferred mandatory HBM hybrid bonding to HBM5. The transition will require re-qualification of test platforms for hybrid-bonded stacks (electrical contact pattern, thermal characteristics, TSV count all change). First open re-qual window for memory test in 4+ years: Teradyne's best opportunity to win share back from Advantest.

6. **Geopolitical concentration risk (Taiwan tail).** Per [[Sectors/Semiconductor Capital Equipment]] #9, TSMC concentration drives sector customer-concentration risk. ATE customer concentration is similarly Taiwan-heavy: TSMC + Taiwan OSATs (ASE, SPIL) drive ~30-35% of Advantest revenue. Taiwan disruption scenarios would constrain test capacity rebuild more than fab capacity rebuild (fab tools are at ASML/AMAT/LRCX; test tools at Advantest/Teradyne both have Japan/US production geography but customer concentration sits in Taiwan).

7. **Universal Robots / industrial automation cyclical hangover.** Teradyne's robotics segment ~10-15% of revenue; structurally lower margin than ATE; cyclical with industrial capex. Continued underperformance pressures Teradyne strategic review (divestiture chatter persistent 2024-2026). Resolution either way, divestiture and re-pure-play or recommitment with growth re-acceleration, would be a multiple-rerating catalyst.

8. **Service annuity compounding faster than tool shipments.** Installed base of 50,000+ Advantest + Teradyne systems globally generates 10-15% annual service revenue growth independent of new tool sales. As AI test program complexity rises, applications-engineering service revenue per tool rises. Service/spares mix at Advantest ~35% today, projected ~40-42% by 2028, mirroring the LRCX CSBG / AMAT AGS / KLAC services trajectory in WFE.

---

## Investor heuristics

### Consensus framing

The sell-side and buy-side currently price the ATE complex as follows:

| Vendor | Consensus Multiple (Fwd P/E) | Consensus Growth (2026-2028 CAGR) | Implicit Framing |
|---|---|---|---|
| Advantest | ~28-32x | 25-30% | "HBM picks-and-shovels" — already largely priced |
| Teradyne | ~18-22x | 8-12% | "Mobile cycle + slow AI ramp" — discounted vs Advantest |
| Cohu | ~15-18x | 5-10% | "Cyclical handler vendor" — perennial value trap framing |

### Where consensus is likely wrong (non-consensus insights)

**HBM4 test-time scaling not in models.** Consensus Advantest models extrapolate ~25-30% revenue CAGR off HBM unit-volume growth and modest test-time creep. The actual test-time step-function from HBM3e (~10h) to HBM4 (~14-18h) is a 40-80% per-stack capacity demand uplift on top of unit growth. If realised, 2027 Advantest revenue runs 15-25% above current sell-side consensus. The forward multiple is full at ~30x, but earnings growth could surprise meaningfully, meaning the equity story works on E rather than P/E.

**Teradyne custom AI ASIC traction under-modelled.** Teradyne UltraFLEX is the platform of choice for several hyperscaler custom-silicon programs that originated in mobile-derivative architectures (Apple-heritage design teams). As custom AI ASIC volume scales 2026-2028, Teradyne SoC revenue could grow 15-20% CAGR, meaningfully above the ~10% consensus. The "Advantest has all the AI exposure" framing is partially wrong; Teradyne has compute exposure, just not HBM exposure.

**Cohu contactor recurring revenue is software-margins-like.** Cohu's contactor business (~50% of revenue) carries gross margins meaningfully above the handler business, with recurring consumption tied to test cell utilisation. AI accelerator thermal contactor wear cycles are 3-5x more aggressive than mobile SoC test contactors, structurally lifting contactor mix and gross margin over 2026-2028. Cohu re-rating from ~16x to ~22-25x is plausible if contactor mix moves from 50% → 60%+.

**China export controls help, don't hurt, Western ATE.** Conventional read: export controls limit Western ATE addressable market by excluding China demand. The actual dynamic is that export controls have prevented Chinese AI compute capacity from materialising, concentrating AI test demand at Western-fab-customer OSATs that use Western ATE. The TAM loss from China advanced-node ATE blocking is more than offset by AI capacity concentration at Western customers.

**Test cycle decoupling from front-end WFE cycle.** Historically WFE and ATE moved in tight correlation (tools shipped → wafers produced → test cells deployed in lockstep). HBM-specific test capacity now leads front-end capex by 6-12 months because HBM final test is the binding constraint on memory vendor revenue recognition. Advantest revenue is showing earlier cyclical recovery and shallower drawdowns than the broader WFE complex, a structural change not yet recognised in cross-correlation analysis.

**Services annuity convergence with WFE service business model.** Per the insight in [[Sectors/Semiconductor Capital Equipment]] re. LRCX CSBG / AMAT AGS / KLAC services trajectories, the same dynamic is playing out in ATE on a 2-3 year lag. Advantest service mix moving from ~35% to ~42% by 2028 with structurally higher margins would compress reported "tool shipment" growth but expand earnings quality. Cyclicality discount applied to Advantest should compress (similar to the SEMICAP cyclicality-discount-mispricing dynamic per [[Sectors/Semiconductor Capital Equipment]] addressed callout).

**Universal Robots divestiture as Teradyne catalyst.** Persistent 2024-2026 chatter on Teradyne strategic review for Universal Robots. Divestiture proceeds estimated $1-2B; re-pure-play would compress holding-company discount and re-rate Teradyne toward Advantest multiples (mid-20s P/E vs current ~20x). Could be a 30-50% equity re-rating without earnings change.

### What to own — positioning recommendation

For an investor expressing the "AI test capacity is the second-derivative chokepoint" thesis with the constraint of avoiding overlap with existing vault holdings:

- **Tier 1 (highest conviction)**: Initiate **Advantest (6857 JP)** thesis. Most direct expression. Pairs with [[Theses/000660 - SK Hynix]] HBM thesis. Watch CY2026 revenue guidance (April 2026 Q4 FY2025 print) and HBM4 customer disclosures.
- **Tier 2 (asymmetric)**: Initiate **Teradyne (TER)** thesis on the Universal Robots-divestiture re-rating catalyst + custom AI ASIC under-modelling. Lower probability than Advantest but higher payoff per dollar of conviction.
- **Tier 3 (recurring annuity)**: Monitor **Cohu (COHU)** for contactor mix inflection. Watch quarterly contactor revenue disclosures and AI accelerator customer attribution. Initiate if FY2026 contactor mix prints >55%.
- **Already owned (cross-sector)**: [[Theses/FORM - FormFactor]] and [[Theses/AEHR - Aehr Test Systems]] capture the photonic/wafer test sub-cluster; no incremental position needed.

**Avoid / underweight**: Chinese ATE entrants (Hwatsing) at current scale: capability gap too wide; valuation already prices domestic substitution narrative. Chroma ATE (Taiwan): niche, lacks scale; useful watchlist not portfolio name.

### Risk factors to monitor (sector-level)

1. **HBM demand pause from inference-efficiency breakthrough.** Same risk vector as SEMICAP: DeepSeek/TurboQuant-style efficiency wins reduce HBM unit demand growth, indirectly compressing test capacity demand. Advantest more exposed than Teradyne.
2. **Teradyne winning HBM5: Advantest share compression.** Re-qualification window 2028-2029. Probability of Teradyne winning one memory vendor non-trivial (~25-35% subjective). Impact: Advantest 2030+ revenue growth slows from ~25% to ~15% CAGR; Teradyne growth accelerates ~10% to ~18-22% CAGR.
3. **Major OSAT cyber/operational disruption.** ATE customer concentration at OSATs (ASE + Amkor + SPIL ~55% of merchant test) creates correlated operational risk.
4. **TSMC final test internalisation accelerating.** If TSMC builds in-house final test capacity meaningfully earlier than 2028, OSAT ATE purchase pattern destabilises; Advantest/Teradyne revenue visibility compresses.
5. **JEDEC HBM5 specification volatility.** HBM5 spec uncertainty could push hybrid bonding earlier (Advantest negative: re-qual window opens for Teradyne) or push it later (Advantest positive: V93000 monopoly extends).

---

## Mental Models
<!-- Outputs from applying the /Mental Models context files to this sector. Per the READING PROTOCOL in [[Generalist - Overview]], these are lenses and questions, never conclusions — every entry is a hypothesis to test against the sector evidence above, not a verdict. Populated incrementally: each research pass appends the models it applied and the specific triggers that fired. -->
- **Models applied**: <!-- [[Generalist - Overview]] (always) · the matching Industry note (e.g. [[Industry - Semiconductors]]) · any relevant Lens note (e.g. [[Lens - Automation & AI Readiness]], [[Lens - Value Layer Monopoly]]) -->
- **Triggers that fired**: <!-- For each pertinent trigger/test/lens: name it, the model it came from, and the one-line read it produced for this sector — held as a hypothesis to test -->
- **Disconfirming check**: <!-- Where multiple models agree, treat it as a trigger to disconfirm: the bear case, the single falsifying datapoint, and the base-rate / outside view sector consensus (or a thesis here) must beat -->

## Related Research

*First active research note added 2026-05-24:*

- [[Research/2026-05-24 - 2802 vs 6857 - Competitive Comparison]]: cross-sector competitive comparison between Advantest (ATE) and Ajinomoto (ABF dielectric materials) on ROIC × valuation × growth; surfaces ~75% shared AI-capex driver correlation, the AI-purity premium that Advantest commands at ~5.8× EV/Revenue vs Ajinomoto group ~3.2× (the SEMICAP comp anchor), and the rare segment-level ROIC parity (Ajinomoto Electronic Materials ~50% margin, +31% growth) that defines preference-flip triggers across the two Japanese-listed AI-cycle names
- [[Research/2026-05-29 - Earnings Transcripts vs Thesis - 6 Holdings - synthesis]]: earnings-transcript review; Advantest share corrected to mgmt-stated ~66% overall / "majority" in AI accelerators (not the 95%/80% sub-segment estimates), and capacity reframed to ~10,000 systems/yr by ~CY2029 (not "10K installed base by 2028"). HBM4 test-time pillar uncorroborated in FY25 calls; realized driver is SoC/AI accelerators

*Suggested research backlog:*

- `2026-05-XX - Semiconductor Test Equipment - Sector Initiation - synthesis.md`: formal initiation research note documenting HBM test-time scaling math, custom ASIC test program inventory, China capability gap quantification
- `2026-05-XX - Advantest - HBM4 Test Capacity Analysis - deep-dive.md`: quantify V93000 capacity demand under multiple HBM4 ramp scenarios; calibrate to memory vendor capex disclosures
- `2026-05-XX - Teradyne - Custom AI ASIC Test Program Inventory - data.md`: enumerate which hyperscaler custom silicon programs run on UltraFLEX vs V93000; estimate share split
- `2026-05-XX - Cohu - Contactor Recurring Revenue Analysis - deep-dive.md`: decompose contactor revenue by end-market; estimate AI accelerator contribution to gross margin

*Existing adjacent research (cross-referenced):*
- [[Sectors/Semiconductor Capital Equipment]]: parent context (WFE complex)
- [[Sectors/Photonic Metrology]]: sister sub-cluster (optical-domain test)
- [[Sectors/DRAM & HBM Memory]]: primary HBM test demand driver
- [[Sectors/NAND Memory & Storage]]: wafer test demand driver
- [[Sectors/Custom Silicon & Networking Semiconductors]]: custom ASIC test demand driver

---

## Legacy Callouts

*This section is owned exclusively by `/archive-callouts` and is currently empty. Addressed callouts older than 180 days will be swept here as plain bullets sorted descending.*

---

## Log

- **2026-05-16**: Sector note initialised. Scope: ATE (Advantest, Teradyne, Cohu) + cross-reference to FORM (probe cards) and AEHR (wafer burn-in) already in [[Sectors/Semiconductor Capital Equipment]] and [[Sectors/Photonic Metrology]]. Candidate theses: ADVT (Tier 1 — HBM monopoly), TER (Tier 2 — custom AI ASIC + UR divestiture catalyst), COHU (Tier 3 — contactor recurring revenue inflection). Central non-consensus insight: HBM test-time scaling (6h → 10h → 14-18h across HBM3/3e/4) is a capacity-demand step-function not modelled in sell-side Advantest forecasts.
- **2026-05-16**: [[Theses/6857 - Advantest]] thesis created by `/thesis ADVT` — first active thesis in this sector. Filename uses TSE code 6857 per vault Japanese-listing convention; alias ADVT retained in tags. Conviction medium (HBM test-time step-function thesis intact; 40-57x forward P/E multiple is the gating concern). Kill trigger: any Teradyne HBM5 hybrid-bonding qualification win at Samsung or SK Hynix by Q4 2027.
- **2026-05-16**: [[Theses/TER - Teradyne]] thesis created by `/thesis Teradyne` — second active thesis in this sector, promoted from Tier 2 candidate (now removed from candidates list). Conviction medium (operating thesis strong: Compute SoC mix 50% +90% YoY, first merchant GPU win Q1 2026, HBM wafer test >50% via Magnum EPIC, CPO test capture via Quantifi/UltraFLEXplus Zero-Overhead, UR robotics scaling via Flex partnership not divesting; 62x trailing P/E + 2027-2028 AI digestion risk + customer concentration cap conviction at medium not high). Kill trigger: Compute SoC mix falls below 35% for 2 consecutive quarters (signal: AI ASIC qualification wave is one-time not structural). Paired with ADVT thesis — TER as higher-beta catch-up leg at ~9x EV/Rev vs ADVT ~15x; together form the ATE duopoly long with explicit cross-thesis tension (TER bull case is partial ADVT bear case via merchant GPU monopoly break, but both win on HBM test-time step-function + custom AI ASIC proliferation). Sector note Tier-1 vs Tier-2 positioning updated: TER moves from Tier-2 candidate to Tier-1 conviction alongside ADVT; Cohu remains Tier-3 monitor.
- **2026-05-17**: Addressed user callouts (2× `[!question]`): added §Product level analysis → "V93000 — architecture, test suite, and clone-feasibility" subsection (PinScale modular instrument cards on IG-XL software stack, 10-row test-type table, four-gate clone analysis = 8-10y to credible HBM/AI parity even under full IP access — software/applications-engineering tacit knowledge and 24-36 month customer re-qualification are the binding constraints, not hardware reproduction); expanded §HBM test specifics with 7-row scaling-driver table (TSV ~N² fault-isolation, bandwidth × pattern-depth, combinatorial repair allocation, BER-tightening) reconciling 1.4-1.8x observed HBM3e→HBM4 test-time step-up vs naïve 1.33x linear-in-layers consensus extrapolation. No conviction/status changes.
- **2026-05-24**: Comparison [[Research/2026-05-24 - 2802 vs 6857 - Competitive Comparison]]: cross-sector comparison registered — Advantest vs Ajinomoto on ROIC × valuation × growth. Advantest wins decisively on consolidated ROIC (~25-28% vs Ajinomoto group ~10-12%) and headline growth purity (+26%, zero food/amino dilution) but trades at ~80% EV/Revenue premium to a same-AI-capex-correlation cross-sector peer; the spread is the AI-purity premium and the SEMICAP comp anchor. The Ajinomoto Electronic Materials segment (>50% margin, +31% growth) approaches Advantest's standalone ROIC, meaning the cross-sector benchmark validates the SEMICAP-multiple framework while flagging that owning both names creates hidden AI-cycle concentration (~75% driver overlap). No within-ATE-sector narrative change — comparison adds peer-asset-quality and valuation context only; Advantest's HBM monopoly framing intact.

### 2026-05-29 (/sync)
- [[Research/2026-05-29 - Earnings Transcripts vs Thesis - 6 Holdings - synthesis]]: transcript-vs-thesis review registered. Advantest share corrected (mgmt-stated ~66% overall / "majority" in AI accelerators, not the 95%/80% sub-segment estimates); capacity reframed 5K→10K systems/yr by ~CY2029 (not "10K installed base by 2028"); HBM4 test-time pillar uncorroborated, realized driver SoC. No sector-framework change — competitive positioning intact.

### 2026-08-20
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged
