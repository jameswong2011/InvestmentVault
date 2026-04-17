---
date: 2026-04-15
tags: [sector, moc, semiconductors, WFE, capital-equipment]
status: active
---

# Semiconductor Capital Equipment

> **Map of Content** — The picks-and-shovels layer of the AI infrastructure stack. This sector note covers the companies that build the machines that build the chips.

## Sector Overview

Semiconductor capital equipment (semicap) comprises the tools, systems, and services required to manufacture integrated circuits. These companies sit at the apex of the semiconductor value chain — every dollar of chip revenue requires upstream equipment investment. The sector is experiencing a structural supercycle driven by the convergence of AI infrastructure buildout, the most significant transistor architecture change in a decade (FinFET → Gate-All-Around), a memory revolution (HBM/3D NAND vertical scaling), and the emergence of advanced packaging as the new performance bottleneck.

**Wafer Fab Equipment (WFE) Market Sizing:**

| Year | WFE Market ($B) | YoY Growth | Total Semicap ($B) | Primary Driver |
|:-----|:----------------|:-----------|:-------------------|:---------------|
| 2019 | 48.8 | -19% | — | Memory glut |
| 2021 | 90+ | +38% | — | 5nm ramp |
| 2024 | 104 | +37% | ~$113 | AI recovery |
| 2025E | ~115 | +10% | ~$133 | Leading-edge logic |
| 2026E | 135 | +17% | ~$145 | GAA/HBM ramp |
| 2027E | 145–156 | +7–15% | ~$156 | Advanced packaging |

*Sources: SEMI, Bank of America, company filings. WFE is a subset of total semicap (which includes test, assembly, packaging).*

**Structural demand floor:** Hyperscaler capex (Amazon, Google, Microsoft, Meta) is projected to exceed $600B in 2026 (+36% YoY), with ~75% directed to AI infrastructure. This creates a multi-year equipment spending floor unprecedented in semiconductor history.

---

## Industry Context: Why This Cycle Is Different

### The Complexity Multiplier
Previous WFE cycles were driven by **capacity** (more wafers at the same node). This cycle is driven by **complexity** (more process steps per wafer):
- FinFET → GAA nanosheet: process steps increase from ~350 to 400–600 per wafer
- 2D NAND → 300+ layer 3D NAND: etch intensity increases ~5x
- HBM stacking: 8-Hi → 12-Hi → 16-Hi increases TSV count linearly
- Backside Power Delivery (BSPDN): creates entirely new process modules (wafer bonding, thinning, CMP)

This means **equipment revenue per wafer start is structurally increasing** — even flat wafer starts produce growing equipment demand.

### The Three Simultaneous Inflections
1. **Logic: GAA at 2nm** — TSMC N2 (2025), Intel 18A (2025), Samsung 2nm (2026). Each node migration expands ALD and selective etch intensity.
2. **Memory: HBM4 + 3D NAND recovery** — HBM market ~$35B (2025) → ~$100B (2030). DRAM equipment +15.1% in 2026. 3D NAND rebound with 300+ layer stacks requiring cryogenic etch.
3. **Advanced Packaging: CoWoS/Hybrid Bonding** — TSMC scaling CoWoS from 35K to 130K wafers/month (2024→2026). Advanced packaging equipment market projected $17.5B by 2028.

### Geopolitical Bifurcation
The market is splitting into two distinct demand pools:
- **China:** Demand for *capacity* at trailing nodes (28nm, 45nm). Domestic competitors (NAURA, AMEC) gaining share. ASML guided significant China revenue decline in 2026. Long-term structural threat to Western equipment share in this segment.
- **Rest of World:** Demand for *capability* at leading edge (2nm, HBM4). Export controls effectively ban Chinese competitors — Western equipment makers face no low-cost competition, preserving pricing power.

---

## Market Breakdown by Equipment Type

### 1. Lithography (~25% of WFE)

The patterning step — transferring circuit designs onto silicon wafers using light.

| Company | Ticker | Market Share | Key Products | Notes |
|:--------|:-------|:-------------|:-------------|:------|
| **ASML** | ASML | ~94% (EUV: 100%) | TWINSCAN EXE:5000 (High-NA EUV), NXE:3800 (EUV), NXT (DUV) | Monopoly in EUV. €32.7B 2025 revenue. €38.8B backlog. 2026 guide: €34–39B. SK Hynix placed $7.97B EUV order through 2027 — largest single customer order ever disclosed. High-NA EUV enters production 2027. |
| **Canon** | 7739.T | ~5% (DUV/NIL) | FPA-5520iV, Nanoimprint | Niche in mature node DUV and nanoimprint lithography. |
| **Nikon** | 7731.T | <1% (DUV) | NSR-S636E | Largely exited advanced litho. Focused on FPD and mature DUV. |

### 2. Etch (~15% of WFE)

Removing material from wafer surfaces to create circuit patterns. The most critical step for vertical scaling (3D NAND, HBM TSVs, GAA selective etch).

| Company | Ticker | Market Share | Key Products | Notes |
|:--------|:-------|:-------------|:-------------|:------|
| **Lam Research** | LRCX | ~45–50% | Vantex (HBM4 TSV), Akara (GAA conductor etch), Sense.i (cryo etch for 3D NAND) | Dominant in high-aspect-ratio etch. $5.34B Q2 FY26 revenue (+22% YoY). Advanced packaging biz growing >40% in FY26. 59% of systems revenue now from Foundry/Logic (was 60%+ Memory historically). |
| **Tokyo Electron** | 8035.T | ~25–28% | EVAROS, CLEAN TRACK series | Strong in oxide etch and thermal etch. 92% share in coater/developers (litho-adjacent). FY26 guide: ¥2.38T. |
| **Applied Materials** | AMAT | ~15–18% | Centura (selective etch), CMP systems | Primarily competes in selective removal and CMP rather than high-aspect-ratio. |
| **NAURA (China)** | 002371.SZ | Growing domestic | NAURA Etch | Gaining share at trailing nodes in China. First area where Chinese competitors are "good enough." |
| **AMEC (China)** | 688012.SS | Growing domestic | Primo nevo | Competing in etch at mature nodes (28nm+). Long-term threat to Western China revenue. |

### 3. Deposition (~20% of WFE)

Adding thin films of material onto wafers. Includes CVD, PVD, ALD, and electrochemical deposition.

| Company | Ticker | Market Share | Key Products | Notes |
|:--------|:-------|:-------------|:-------------|:------|
| **Applied Materials** | AMAT | ~30% (CVD/PVD leader) | Endura (PVD/Mo), Centura (CVD), Producer (ALD) | Broadest portfolio — "department store" model. Pioneered molybdenum interconnects for GAA. FY25 revenue $28.4B. FY26 guide: >20% equipment growth. EPIC Center ($4–5B R&D facility) is a customer lock-in strategy. |
| **ASM International** | ASM.AS | ~55% (single-wafer ALD) | Intrepid (ALD), Epsilon (Epi) | Pure GAA play. ALD SAM increases $400M per 100K wafer starts at GAA. Record €3.2B 2025 revenue. Targeting 12%+ CAGR through 2030. |
| **Lam Research** | LRCX | ~25–30% (PECVD) | SABRE 3D (electroplating), ALTUS (ALD) | SABRE 3D electroplating for TSV fill doubled revenue in 2024. Critical for HBM copper fill. |
| **Tokyo Electron** | 8035.T | ~15–20% (batch ALD) | TELINDY PLUS (batch ALD) | Leader in batch furnace ALD for high-volume manufacturing. |

### 4. Process Control — Inspection & Metrology (~12% of WFE)

The "yield gatekeepers" — detecting defects and measuring critical dimensions.

| Company | Ticker | Market Share | Key Products | Notes |
|:--------|:-------|:-------------|:-------------|:------|
| **KLA Corporation** | KLAC | ~63% | 8 Series (e-beam), Surfscan SP7, SpectraFilm | Near-monopoly. $3.3B Q2 FY26 revenue. $950M advanced packaging revenue in CY25 (+70% YoY). 62% gross margin, 43% operating margin — best-in-class profitability. HBM requires 3x inspection intensity of standard DRAM. |
| **Applied Materials** | AMAT | ~10% | SEMVision, Aera | Smaller player in inspection; primarily competes via integrated metrology. |
| **Lasertec** | 6920.T | Niche leader | ACTIS (EUV mask inspection) | Only company capable of inspecting EUV photomasks. Essential ASML ecosystem partner. |
| **Onto Innovation** | ONTO | ~5% | Dragonfly (3D metrology) | Specialist in advanced packaging metrology. Growing with CoWoS/HBM. |

### 5. Ion Implantation & Thermal Processing (~5% of WFE)

Modifying electrical properties of silicon through doping and heat treatment.

| Company | Ticker | Market Share | Key Products | Notes |
|:--------|:-------|:-------------|:-------------|:------|
| **Applied Materials** | AMAT | ~70% (implant) | VIISta | Dominant in ion implantation with ~70% share. |
| **Axcelis Technologies** | ACLS | ~25% (implant) | Purion (power devices) | Strong position in SiC implant for EV power semiconductors. |
| **Tokyo Electron** | 8035.T | ~60% (thermal) | TELINDY (batch furnace) | Leader in thermal processing (diffusion, oxidation). |
| **Kokusai Electric** | 6525.T | ~30% (thermal) | Vertus (batch ALD/CVD) | Spun out of Applied Materials. Specialist in batch thermal. |

### 6. Advanced Packaging & Assembly Equipment

The fastest-growing segment (~40%+ growth in 2026). Includes die bonding, hybrid bonding, wire bonding, and wafer-level packaging.

| Company | Ticker | Market Share | Key Products | Notes |
|:--------|:-------|:-------------|:-------------|:------|
| **BESI** | BESI.AS | ~67% (D2W hybrid bonding), 42% (die attach) | Kinex (inline hybrid bonder, co-developed with AMAT), Gen-2 50nm platform | Monopoly-like position. €476M hybrid bonding revenue estimated for 2026. 150+ installed systems across 18 customers. Dual M&A interest from LRCX and AMAT. See [[Theses/BESI - BE Semiconductor Industries]]. |
| **ASMPT** | 522.HK | Growing | LITHOBOLT (hybrid bonder) | Pre-production. Increasing R&D spend. Potential second source but 2–3 years behind BESI in qualification. |
| **Kulicke & Soffa** | KLIC | Legacy leader (wire bonding) | CuFirst (hybrid bonding), APTURA FTC | Strong legacy position in wire/thermo-compression bonding. CuFirst hybrid process is differentiated but not yet at scale. |
| **TOWA** | 6315.T | Niche (molding) | Ultra-high-density stacking | Japanese specialist in molding/singulation for packaging. New tech for 16-Hi HBM stacking. |
| **EV Group** | Private | Niche (wafer bonding) | GEMINI (W2W bonding) | Specialist in wafer-to-wafer bonding. Critical for SoIC and CPO. |
| **SUSS MicroTec** | SMHN.DE | Niche (wafer bonding) | XBC300 Gen2 | Competing in wafer bonding for advanced packaging. |

### 7. Test Equipment

Testing chips after fabrication (wafer-level) and after packaging (final test).

| Company | Ticker | Market Share | Key Products | Notes |
|:--------|:-------|:-------------|:-------------|:------|
| **Advantest** | 6857.T | ~55% (SoC test) | V93000 | Dominant in SoC/HPC test. AI chip test complexity growing 2–3x per generation. |
| **Teradyne** | TER | ~35% (SoC test) | UltraFLEX | Strong in automotive and mobile test. Also robotics (Universal Robots). |
| **Cohu** | COHU | Niche | DIAMONDX handler | Specialist in test handlers and interface. |
| **Aehr Test** | AEHR | Niche | FOX-XP (wafer-level burn-in) | Emerging photonics test play. 9× 300mm wafer parallel test. Order surge in Q1 2026 for SiPh burn-in. |
| **FormFactor** | FORM | Niche | Optical metrology probes | Picks-and-shovels of the photonics buildout. Optical test is the critical bottleneck for CPO yield. |

### 8. Photonics & Optical Equipment Enablers

Equipment and foundry services enabling the copper-to-optical transition. See also [[Sectors/Semiconductors]] for photonics investable names (LITE, COHR, AAOI, IQE).

| Company | Ticker | Role | Notes |
|:--------|:-------|:-----|:------|
| **GlobalFoundries** | GFS | SiPh foundry | Acquired AMF Singapore — now world's largest pure-play SiPh foundry. Targeting $1B+ photonics revenue by 2030. 45CLO process. |
| **Tower Semiconductor** | TSEM | SiPh foundry | Tripling photonics capacity by mid-2026. Unique SiGe-integrated process for ultrafast modulators. OpenLight InP-on-silicon partnership. |
| **TSMC** | TSM | SiPh/CPO foundry | COUPE CPO platform in risk production with AMD (Feb 2026). Yields below ideal — may outsource optical engine packaging. |
| **Fabrinet** | FN | Optical assembly | NVIDIA's primary optical assembly partner. Micron-level laser alignment capability. Gearing up for CPO module assembly. |

---

## End Market Demand Map

```
                    ┌────────────────────────────────────────────┐
                    │         AI INFRASTRUCTURE DEMAND            │
                    │  Hyperscaler Capex >$600B (2026E, +36%)    │
                    └────────────┬───────────────────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
    ┌─────────────────┐ ┌────────────────┐ ┌────────────────────┐
    │  LEADING-EDGE   │ │    MEMORY      │ │ ADVANCED PACKAGING │
    │   LOGIC (2nm)   │ │  (HBM + NAND)  │ │ (CoWoS/HB/CPO)    │
    │                 │ │                │ │                    │
    │ ASML (litho)    │ │ LRCX (TSV etch)│ │ BESI (hybrid bond) │
    │ ASMI (ALD)      │ │ AMAT (dep/CMP) │ │ LRCX (electrochem) │
    │ AMAT (Mo/BSPD)  │ │ KLAC (inspect) │ │ KLAC (3x inspect)  │
    │ LRCX (sel. etch)│ │ TEL (thermal)  │ │ AMAT (CMP/W2W)     │
    │ TEL (coater)    │ │ ASML (EUV)     │ │ Advantest (test)    │
    │ KLAC (metrology)│ │ Advantest(test) │ │ EV Group (W2W bond) │
    └─────────────────┘ └────────────────┘ └────────────────────┘
              │                  │                  │
              ▼                  ▼                  ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                    MATURE / ICAPS NODES                      │
    │  (Automotive, IoT, Power, Industrial — recovery in 2026)    │
    │  AMAT (broad portfolio), TEL (thermal), Axcelis (SiC imp)   │
    └─────────────────────────────────────────────────────────────┘
```

---

## Key Dynamics

- **WFE market projected $135B in CY2026 (+17%), reaching $145–156B in 2027.** SEMI, Bank of America, and company guidance converge on this range. DRAM equipment +15.1%, NAND equipment +12.7% in 2026.
- **Advanced packaging is the highest-growth sub-sector at 40%+ growth in 2026**, driven by HBM4 TSV etch, CoWoS capacity 3.7x expansion, and hybrid bonding adoption. LRCX and BESI are primary beneficiaries.
- **The GAA transistor transition at 2nm increases ALD and selective etch intensity per wafer by 30–50%**, creating a structural multiplier for ASMI and LRCX even at flat wafer starts.
- **ASML's EUV monopoly is widening with High-NA** — entry commercial production in 2027 enables another upgrade cycle. €38.8B backlog provides 1.2x annual revenue visibility.
- **KLA's inspection monopoly (63% share) becomes more valuable as defect tolerance collapses** — at 2nm, a single nanometer-scale defect can bankrupt a wafer. HBM stacking requires 3x inspection intensity vs. standard DRAM.
- **TSMC CoWoS is the tightest bottleneck in the AI semiconductor stack** — oversubscribed through 2026, with NVIDIA securing 60%+ of capacity. Scaling from 35K to 130K wafers/month drives equipment demand across etch, CMP, inspection, and bonding.
- **China equipment revenue is a declining contributor** — ASML guided significant China decline in 2026. Domestic Chinese competitors (NAURA, AMEC) gaining share at trailing nodes. Long-term structural risk to Western equipment makers' China revenue.

---

## Active Theses (Equipment-Specific)
- [[Theses/BESI - BE Semiconductor Industries]] — Hybrid bonding monopoly / 3D integration
- [[Theses/SEMICAP - Semiconductor Capital Equipment]] — Sector-level thesis (non-consensus picks)

## Related Theses (Equipment-Adjacent)
- [[Theses/LITE - Lumentum]] — Photonics/EML supply chain
- [[Theses/NVDA - Nvidia]] — Demand driver for all semicap
- [[Theses/285A - Kioxia]] — NAND recovery → LRCX/AMAT demand
- [[Theses/SNDK - SanDisk]] — NAND + HBF → memory equipment demand
- [[Theses/IQE - IQE]] — III-V substrate supply for photonics equipment

## Research Notes
- [[Research/2026-02-26 - Semis - Gemini Lam vs AMAT Canvas]] — AMAT vs LRCX strategic analysis
- [[Research/2026-03-20 - Semis - Gemini WFE Equipment Canvas]] — 5-company WFE evaluation
- [[Research/2025-11-27 - Semis - Gemini HBM4 Market Canvas]] — HBM4 vendor analysis
- [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]] — SiPh supply chain
- [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]] — Photonics/CPO analysis
- [[Research/2026-04-10 - Hybrid Bonding and BESI Revenue Impact]] — BESI hybrid bonding revenue model
- [[Research/2026-01-15 - AI Compute and Memory Demands - HBM Shortage]] — HBM shortage dynamics
- [[Research/2026-03-02 - Chinese Silicon Photonics Threat]] — Chinese competitive dynamics
- [[Research/2026-03-09 - Photonics and CPO Investment Outlook]] — Photonics investment outlook
- [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]] — CPO vendor analysis
- [[Research/2026-03-20 - Lam Research and Applied Materials Evaluation]] — LRCX/AMAT deep dive

## Watchlist
- **Lasertec (6920.T)** — Only EUV mask inspection tool maker. Essential ASML partner. Japan-listed.
- **Kokusai Electric (6525.T)** — Batch thermal processing specialist. Spun from AMAT. Japan-listed.
- **Onto Innovation (ONTO)** — Advanced packaging metrology. Growing with CoWoS/HBM.
- **Axcelis (ACLS)** — SiC implant specialist. Leveraged to EV power semiconductor capex.
- **FormFactor (FORM)** — Optical metrology probes. Picks-and-shovels of SiPh testing.
- **Aehr Test (AEHR)** — Wafer-level burn-in for SiPh. Order surge in 2026.
- **EV Group (Private)** — Wafer-to-wafer bonding for SoIC/CPO. Would be a strong IPO candidate.
