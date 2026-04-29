---
date: 2026-04-22
tags: [sector, moc]
status: active
---

# Optical Networking & Photonics

## Active Theses
- [[Theses/LITE - Lumentum]] — Lumentum (physics-gated 200G EML laser monopoly / 50-60% EML share / $2B NVIDIA investment / 8x capacity expansion from FY23 / $400M+ OCS backlog / Cloud Light transceiver vertical integration)
- [[Theses/IQE - IQE]] — IQE (world's largest independent III-V epitaxy / UK Takeover Code offer period active / Taiwan sale in progress / InP supply gap 70% / 52p vs 4.7p Nov 2025 low / M&A special situation vs SiPh demand catalyst)

## Key industry questions
- Does the **1.6T/CPO inflection year** (2026) unfold as consensus expects — 22M 1.6T units, ~49M 800G+, $26B Ethernet AI optics — or does the Goldman upward revision (+58% to 33.5M 1.6T units) point to consensus being systematically late on ramps that are now physics-limited rather than demand-limited?
- Will **Chinese module dominance** (Innolight 50-60% 1.6T share, 7 of top 10 merchants, 60% of NVDA GB200 volume) extend up the stack into laser chips and DSPs — or does the 3% Chinese InP localization rate at 25G+ and 0% at 200G represent a permanent Western chokepoint that compounds with each speed generation because failure rates scale with the 4th power of bandwidth?
- Does **co-packaged optics (CPO)** redistribute value away from transceiver makers (Lumentum Cloud Light, Coherent, Innolight) toward silicon photonics foundries (TSMC COUPE, GlobalFoundries/AMF, Tower) and vertically integrated ASIC houses (Broadcom, NVIDIA, Marvell/Celestial) — or does the "SiPh paradox" (every SiPh chip needs an external InP laser) mean component-level chokepoint players are net winners regardless of where module value shifts?
- Is the **EML five-player oligopoly** (Lumentum + Coherent + Broadcom + Mitsubishi Electric + Sumitomo ≈ 75.9% of EML revenue) structurally durable given butt-joint regrowth barriers, or does Coherent's 6-inch InP platform lead (2+ years ahead of Lumentum's Greensboro 2028 target, 4x device density, 50% cost reduction) collapse Lumentum's pricing power by 2027-2028 even if it doesn't close yield parity?
- How does the **optical circuit switch (OCS)** market — revised from $500M to $1.5B for 2026 and projected at $2.5B by 2029 — reshape hyperscaler capex allocation? Is this a permanent category (Google Apollo, Marvell-Lumentum R300 demo at OFC 2026, Ironwood TPU) that compresses traditional electrical spine-switch TAM, or a niche for workloads where topology reconfiguration dominates vs. pure bandwidth?
- Are **transitional architectures** (Linear Pluggable Optics removing the DSP, DSP-lite coherent-lite, NPO near-packaged optics) a multi-year deployment category or a 12-18 month bridge — and does LPO adoption at ~33% of 800G intra-datacenter by 2026-2027 structurally damage the Marvell/Broadcom DSP duopoly before CPO matures?
- Can **AAOI** execute $1B FY26 revenue (+120% YoY) on $200M+ 1.6T orders and $124M+ 800G orders from hyperscalers, or does its customer concentration (Microsoft 44% in 2024, top-10 = 95%), prior hyperscaler churn allegations (Amazon/Microsoft "walked away" per Culper/BMF short reports), and dependence on merchant Western EML chips make it a structurally lower-moat path into the supercycle?
- Does **thin-film lithium niobate (TFLN)** — HyperLight/UMC/Wavetek foundry partnership March 2026, 400G-per-lane PICs, 145 GHz bandwidth — emerge as the dominant modulator technology at 3.2T/6.4T, displacing both EML and Mach-Zehnder SiPh and resetting the competitive clock?

## Industry history

**Phase 1 — Laser fundamentals (1960–1990):** Theodore Maiman's ruby laser (1960, Hughes Research Labs) and Kao/Hockham's optical fiber transmission theory (1966, STL Harlow — earned Kao the 2009 Nobel) established the two primitives. Corning demonstrated 20 dB/km silica fiber (1970). The first commercial optical telecom systems went live in the early 1980s at 45 Mbps using 850nm multimode GaAs lasers. **II-VI Incorporated** was founded in 1971 by Carl Johnson and James Hawkey as a materials specialist in ZnSe/ZnS infrared optics for CO2 lasers. **JDS Fitel** (Canada) and **Uniphase** (USA) emerged as independent optical component makers through the 1980s. **Corning, Lucent (Bell Labs), and Nortel** led long-haul WDM system development.

**Phase 2 — WDM buildout and telecom bubble (1990–2001):** Wavelength-division multiplexing arrived commercially in 1995 — a single fiber carrying 40+ wavelengths at 2.5 Gbps each. Internet traffic tripled annually 1995-2000. **JDSU** formed July 1999 from the $6B merger of JDS Fitel and Uniphase — peaked at $153B market cap March 2000, the largest component vendor in optical networking. **Nortel Networks** peaked at $398B market cap September 2000 (35% of TSX weighting) as the dominant optical transport equipment maker. **Applied Optoelectronics (AAOI)** was founded 1997 in Sugar Land, Texas by Thompson Lin. **Lumentum's roots** trace through JDS Fitel's InP laser programs acquired 1997-1999. Fiber infrastructure buildout added 39M miles of fiber 1996-2001 — most of it "dark" (unused) for years. The bubble burst March 2000: JDSU collapsed 99%, Nortel 99%, Global Crossing/WorldCom bankrupted. Optical component market revenue fell from ~$40B (2000) to ~$7B (2002).

**Phase 3 — Telecom consolidation and survival (2002–2013):** Surviving optical vendors consolidated. Cisco acquired **Cerent** ($7B, 1999), **Pirelli Optical Systems** ($2.2B, 2000), and later Acacia Communications ($4.5B announced 2019, closed 2021). **Ciena** acquired Nortel's MEN (optical networking) business March 2010 for $773M out of bankruptcy — its survival moat. **Finisar** consolidated transceivers. **Oclaro** formed 2009 from the Bookham/Avanex merger. **II-VI** pivoted from CO2 laser optics into RF/compound-semi diversification. **Nortel** bankrupted 2009. The industry entered a ~10-year revenue-flat period 2003-2013 as dark fiber was lit up organically without new capacity buildout. EML and DFB laser development continued quietly at JDSU, Oclaro, Finisar, Sumitomo, Mitsubishi.

**Phase 4 — Datacom takeover and company reformation (2015–2020):** JDSU split August 1, 2015 into **Lumentum** (optical components, chips, lasers) and **Viavi Solutions** (network test/measurement). Datacenter interconnect became the primary growth driver as hyperscale cloud (AWS, Azure, GCP) passed telecom as the largest optical buyer. **Finisar merged with II-VI** ($3.2B, closed September 2019). **Oclaro acquired by Lumentum** ($1.8B, closed December 2018) — consolidating InP and indium phosphide foundry assets. **Acacia Communications** went public (2016), acquired by Cisco ($4.5B, 2021) for coherent DSP + pluggable ZR technology. **Broadcom** entered EML lasers via its **Avago → Emulex → Infineon Fiber Optics** heritage (Breinigsville, PA InP fab from former Agere/Bell Labs). **Innolight Technology** (China, founded 2008) scaled from $50M (2015) to $1B+ (2021) on 100G/400G datacom demand.

**Phase 5 — Pre-AI optical stabilization (2020–2022):** 400G ramp dominated datacom 2020-2022. **II-VI acquired Coherent Inc.** ($7B, closed July 2022) — adopted Coherent name, creating a vertically integrated $5B+ photonics conglomerate spanning materials (SiC, InP) → lasers → transceivers → industrial/auto. Post-merger integration pain (high debt, margin compression, SiC overcapacity) weighed on COHR through 2023-2024. **Jim Anderson** (ex-Lattice Semiconductor) appointed CEO effective June 3, 2024 — began aggressive margin turnaround. **Lumentum acquired Cloud Light** ($750M, closed October 2023) for pluggable transceiver vertical integration. NVIDIA's DGX-H100 (2022) launched the current AI networking era but optical deployment density stayed limited to ~4-8 transceivers per GPU.

**Phase 6 — AI optical supercycle and CPO inflection (2023–2026):** NVIDIA's H100/H200/Blackwell/GB200 ramp drove optical interconnect demand exponentially — a single GB200 NVL72 rack uses 288 GPUs requiring thousands of optical interconnects per rack. **800G shipments grew from ~5M (2023) to 24.5M (2025) to forecast 63M (2026, 2.6x YoY).** **1.6T commercial launch began 2025, with 22M unit forecast for 2026 (and Goldman upward revision to 33.5M).** **Innolight** overtook Finisar/Cloud Light as #1 transceiver vendor 2024 at ~40% 800G share. **Chinese merchant suppliers** (Innolight, Eoptolink, Accelink, Hisense, Hilink, Source Photonics China) captured 7 of top 10 positions and 60% of NVIDIA GB200 volume. **Lumentum became sole 200G EML supplier at volume** with 8x capacity expansion from FY23 and still demand-constrained. **Broadcom Bailly CPO** shipped 50,000+ switches (first commercial CPO product). **NVIDIA announced Spectrum-X and Quantum-X CPO switches** with TSMC COUPE optical engines for 2026 deployment. **NVIDIA invested $2B each** in Lumentum and Coherent (March 2026) — explicit dual-supplier hedge on the InP EML bottleneck. **GlobalFoundries acquired AMF** (November 2025) for world's largest dedicated SiPh foundry. **Tower Semiconductor tripling SiPh capacity** by mid-2026 on $650M investment. **TSMC COUPE entered risk production with AMD** February 2026, targeting 6.4T per package H2 2026. **HyperLight/UMC/Wavetek announced TFLN Chiplet foundry partnership** March 12, 2026. **OCS market revised from $500M to $1.5B for 2026**, $2.5B by 2029. **IQE placed under UK Takeover Code offer period** September 2025, stock rallied >1,000% from 4.7p to ~52p.

**Phase 7 — 2026-2030 outlook (forward roadmap):** 1.6T volume mainstream 2027 (consensus 22M units 2026 → 65M+ 2028); 3.2T pilots emerge 2028 with EML at 200G/lane ×16 or TFLN at 400G/lane ×8 lanes; 6.4T appears 2029-2030 in CPO-only deployments. TSMC COUPE 12.8T per package targeted by 2028. Lumentum Greensboro 6-inch InP fab production mid-2028 ($5B revenue capacity); Coherent's four 6-inch InP fabs fully online ~2027; Eindhoven Smart Photonics 6-inch online 2028 (€150M EU Chips Act). CPO penetration projected 5-10% of new deployments 2026, 25-35% by 2028, 50%+ by 2030. OCS market $2.5B by 2029 per Cignal AI. TFLN volume via UMC 8-inch foundry 2027-2028 enables 3.2T modulator alternatives. Chinese 200G EML localization milestones expected 2028-2030 (Yuanjie / Everbright / Henlitz roadmaps; Source Photonics China demo timelines slip 12-24 months from Western leader). Optical AI compute (Lightmatter Passage, Lightelligence) crosses commercial threshold ~2027 for hyperscaler trials. By 2030, optical interconnect TAM ~$90-100B, SiPh foundry $10B+, EML chips $3-4B, OCS $2.5-3B.

## Technology primitives — modulators, modulation formats, wavelengths, reach

The optical interconnect stack stratifies along four orthogonal technology axes; understanding which axis competition operates on disambiguates most architectural debates.

**Modulator architectures (the active element converting electrical signals to optical):**

| Architecture                                 | Material                       | Bandwidth ceiling                                  | Power efficiency             | Cost per Gbps     | 2026 commercial state                            |
| -------------------------------------------- | ------------------------------ | -------------------------------------------------- | ---------------------------- | ----------------- | ------------------------------------------------ |
| **DML** (Directly Modulated Laser)           | InP DFB                        | ~50G NRZ / 100G PAM4                               | High (no external modulator) | Lowest            | Volume at 100G; declining at 200G+               |
| **EML** (Electro-absorption Modulated Laser) | InP DFB+EA butt-joint regrowth | ~200G PAM4 commercial; 400G demoed (LITE OFC 2026) | Moderate                     | Mid (single chip) | **Sole commercial 200G/lane volume modulator**   |
| **MZM-SiPh** (Mach-Zehnder, silicon)         | Silicon waveguide + ext. InP CW laser | 100-200G PAM4; 400G coherent                       | Lower (drivers required)     | Low at scale      | CPO dominant: TSMC COUPE, Broadcom Bailly, NVIDIA Quantum-X / Spectrum-X |
| **MZM-InP** (Mach-Zehnder, indium phosphide) | InP MZM (monolithic with laser) | 200G PAM4; 400G coherent                                  | Moderate                     | Mid-high          | Coherent telecom: NEL/NTT, Fujitsu Optical, Ciena WaveLogic 6 |
| **TFLN** (Thin-Film LiNbO3 — MZM topology)   | Thin-film LiNbO3 on Si + ext. laser | 145 GHz demoed; 400G/lane                            | Highest at high BW           | Higher initially  | 2026 foundry launch (HyperLight/UMC/Wavetek); pre-volume |
| **EOP** (Electro-Optic Polymer)              | Organic polymer + ext. laser   | 100GHz+                                                  | Moderate                     | Unknown at scale  | R&D (Lightwave Logic LWLG)                       |
| **MRM / Ring resonator**                     | Silicon resonant + ext. laser  | Wavelength-selective; ≤100G/lane                          | Highest (resonant)           | Low               | Niche CPO + DWDM intra-DC (Ayar Labs TeraPHY)    |

> [!error] 2026-04-28 → Addressed 2026-04-28
> **Prompt:** *What is the material used for **MZM** (Mach-Zehnder) lasers, silicon photonics is not the right answer. Is this the standard (and only) architecture for CPO?*
>
> **Response:** MZM is a topology (Mach-Zehnder interferometer), not a material — silicon photonics is the CPO-dominant implementation but MZMs are also built in InP (NEL/Fujitsu/Ciena coherent line cards), thin-film LiNbO3 (the TFLN row), and bulk LiNbO3 (legacy coherent). MZM-SiPh leads CPO today (TSMC COUPE, Broadcom Bailly, NVIDIA Quantum-X) but is not the only viable architecture — ring resonators (Ayar Labs TeraPHY) compete on density and TFLN-MZM (HyperLight 2028+) on bandwidth. Table updated to split MZM by material; full breakdown in §Technology primitives → Modulator topology vs material clarification immediately below.

> [!todo] 2026-04-28 → Addressed 2026-04-28
> **Prompt:** *Can you map this table to actual listed companies and the products that they're selling. I want to understand who are the players at each technology stack.*
>
> **Response:** Mapping table added immediately below — each modulator architecture mapped to listed-ticker exposure with specific products and stack position. Key clusters: LITE/COHR at DML+EML; MRVL/AVGO/CSCO/INTC/GFS/TSEM at MZM-SiPh; NTT/Fujitsu/CIEN at MZM-InP; QUBT/LWLG at TFLN/EOP frontier; Ayar Labs (private) holds the ring-resonator path. See §Technology primitives → Modulator architecture → listed-company exposure mapping.

**MZM topology vs material clarification.** MZM (Mach-Zehnder) is a *modulator topology*, not a material — light splits into two arms, one arm receives an electrically-induced phase shift via the host material's electro-optic effect, and the recombined output produces intensity/phase modulation by interference. The MZM is the modulator; in most implementations it requires a *separate* CW laser source (only InP-MZM is monolithic with its own laser). Implementations differ by material with distinct physics tradeoffs:

- **Silicon-photonic MZM (CPO-dominant):** silicon waveguide + thermal or p-n junction phase shifter; requires external InP CW laser (silicon's indirect bandgap cannot lase). Power-efficient at 300mm-wafer scale and CMOS-compatible. TSMC COUPE, Broadcom Bailly, NVIDIA Quantum-X / Spectrum-X all use SiPh-MZM.
- **InP-MZM (coherent telecom standard):** monolithic InP wafer integrating laser + MZM modulator on the same die. InP's electro-optic coefficient is ~3x silicon's, enabling shorter arms and lower insertion loss — but InP wafers are 3-4-inch (vs silicon's 300mm) and ~10x more expensive per area. NEL (NTT subsidiary), Fujitsu Optical Components, and Ciena WaveLogic 6 use this for 400G/600G/800G coherent line cards.
- **TFLN MZM (next-gen, 3.2T+):** thin-film lithium niobate bonded on silicon. LiNbO3's electro-optic coefficient is ~30x silicon's — the highest of any practical material — enabling 145 GHz demonstrated bandwidth at short arm lengths. HyperLight/UMC/Wavetek announced 6/8-inch foundry partnership March 2026; commercial volume targeted 2027-2028. The TFLN row above represents this path.
- **Bulk LiNbO3 MZM (legacy coherent):** discrete waveguide-on-LiNbO3 chip, the ≥1990s long-haul coherent standard. Bulky form factor (~50mm chip length) ages out as TFLN scales; Sumitomo Electric, Fujitsu, and Exail are residual incumbents.

**Is MZM-SiPh the only CPO architecture?** No — three viable CPO modulator paths in 2026:

1. **MZM-SiPh (dominant, ~95% of 2026 CPO volume):** TSMC COUPE 6.4T-class engines (AMD risk prod Feb 2026); Broadcom Bailly (50K+ switches shipped, first commercial CPO product); NVIDIA Quantum-X / Spectrum-X with TSMC COUPE engines; Marvell-Celestial AI Photonic Fabric. Industry default for 2026-2028.
2. **Ring resonator (MRM, niche but growing):** Ayar Labs TeraPHY chiplet (Intel co-package partnership, NVIDIA + GlobalFoundries co-investors); IBM Research demos. ~10x denser per Tb/s than MZM (resonator footprint << arm length) but temperature-sensitive — requires precise thermal stabilization to lock the resonant wavelength to the laser carrier. Better suited to dense WDM where density matters more than thermal margin.
3. **TFLN MZM (future, 3.2T+ deployments):** HyperLight foundry roadmap targets CPO integration where SiPh-MZM hits voltage-length-product limits at 6.4T+. The 30x-stronger EO coefficient becomes essential when the modulator (not the laser) becomes the bandwidth bottleneck. Pre-volume in 2026; expected hyperscaler trials 2028-2029.

**Modulator architecture → listed-company exposure mapping.** Each architecture maps to specific listed-ticker exposure for portfolio construction:

| Architecture | Listed Companies (tickers) | Specific Products / Programs | Stack Position |
|---|---|---|---|
| **DML (100G)** | Lumentum (LITE), Coherent (COHR), Broadcom (AVGO), Mitsubishi Electric (TYO:6503), Sumitomo Electric (TYO:5802), Innolight (300308.SZ) | LITE 100G CWDM4/LR4 DFB chips; COHR 100G DFB; AVGO Breinigsville-fab DFBs; merchant 100G DFBs (Mitsubishi/Sumitomo) | Component (laser chip) |
| **EML (200G PAM4)** | Lumentum (LITE — sole 200G volume, 50-60% share), Coherent (COHR — qualifying), Broadcom (AVGO — captive), Mitsubishi Electric (TYO:6503), Sumitomo Electric (TYO:5802) | LITE 200G EML; COHR Greensboro 6-inch InP 200G (qualifying); AVGO captive EML for Tomahawk linkages; Mitsubishi 200G mass prod April 2024; Sumitomo qualifying | Component (laser chip) |
| **MZM-SiPh (CPO + pluggable + coherent)** | Cisco/Acacia (CSCO), Marvell (MRVL), Broadcom (AVGO), Intel Foundry (INTC), GlobalFoundries (GFS via AMF), Tower Semi (TSEM), TSMC (TSM) | TSMC COUPE 6.4T optical engine (AMD risk prod); AVGO Bailly CPO (50K+ shipped); CSCO/Acacia coherent ZR/ZR+; MRVL COLORZ + Celestial Photonic Fabric; GFS-AMF SiPh foundry; TSEM ARM/PCIe SiPh PIC | Foundry / module / system |
| **MZM-InP (coherent telecom)** | NTT (TYO:9432, NEL subsidiary), Fujitsu (TYO:6702, Fujitsu Optical Components), Ciena (CIEN), Lumentum (LITE) legacy, Coherent (COHR) | NEL InP MZM modulators for 400G/600G/800G coherent; Fujitsu InP MZMs for telecom equipment; Ciena WaveLogic 6 with InP MZM; LITE/COHR legacy InP MZMs | Component / line card |
| **TFLN (thin-film LiNbO3)** | Quantum Computing Inc (QUBT), United Microelectronics (UMC) for foundry, HyperLight (private — Series A 2024), Wavetek (private) | QUBT TFLN process / NJ fab; HyperLight-UMC-Wavetek foundry March 2026 (6/8-inch wafers); HyperLight 400G-per-lane PIC | Foundry / IP / PIC |
| **EOP (electro-optic polymer)** | Lightwave Logic (LWLG) | LWLG polymer modulator IP; MPW samples; pre-revenue at <$300M mkt cap | IP / R&D |
| **MRM / Ring resonator** | Ayar Labs (private — VC-backed by Intel Capital, NVIDIA, GlobalFoundries; reported $2.5B valuation 2024), IBM (IBM, research only) | Ayar Labs TeraPHY optical I/O chiplet (Intel co-package partnership); IBM CPO research demos | Component / chiplet |
| **Bulk LiNbO3 (legacy coherent)** | Sumitomo Electric (TYO:5802), Fujitsu (TYO:6702), Exail (private — Eutelsat-spun-out post-2022 merger) | Legacy 100G/400G coherent modulators (declining); displaced by TFLN over 2027-2030 | Component (legacy) |

Reading this mapping for portfolio expression: **DML/EML capture the laser-chip layer that every external-laser MZM/MRM/TFLN module requires** (per the SiPh paradox — silicon cannot lase) — making LITE/COHR "arms-dealer" exposure to the entire MZM-SiPh CPO buildout regardless of which module/ASIC vendor wins downstream. **MZM-SiPh listed exposure is broad** (CSCO/MRVL/AVGO/INTC/GFS/TSEM) but each is diversified — no pure-play public ticker captures the SiPh-MZM stratum the way LITE captures EML. **TFLN and EOP are pre-revenue venture-stage bets** with limited public expression (QUBT, LWLG); the Ayar Labs ring-resonator path remains private. **MZM-InP is a legacy + coherent-telecom layer** captured most directly through CIEN (US-listed) and JP-listed NTT/Fujitsu — counter-cyclical exposure to the telecom optical re-investment thesis (heuristic #11).

Physics gates: DML hits chirp ceiling at >100G; EML faces butt-joint regrowth yield wall at >200G/lane (failure rate ∝ bandwidth^4); MZM-SiPh faces voltage-length product limits at 6.4T+ requiring complex drivers (silicon's small electro-optic coefficient forces long arms); TFLN's 30x-stronger EO coefficient unblocks this electrically but manufacturing maturity lags 3-5 years behind SiPh. The 200G EML chokepoint reflects this physics ladder — every commercial modulator architecture strains its respective limit at 200G/lane simultaneously, which is why the Lumentum monopoly is structurally durable through the 1.6T cycle.

**Modulation formats by speed generation:**

| Format | Bits/symbol | Used at | Driver complexity |
|---|---|---|---|
| NRZ (Non-Return-to-Zero) | 1 | ≤100G/lane | Simplest |
| PAM4 (4-level pulse amplitude) | 2 | 200G/400G/800G/1.6T per lane | Moderate (DSP heavy) |
| PAM6 / PAM8 | 2.58 / 3 | 3.2T+ (development) | Higher SNR demand |
| DP-QPSK / DP-16QAM / DP-64QAM | 4 / 8 / 12 | Coherent telecom + ZR/ZR+ pluggables | Highest (coherent DSP) |
| OOK (on-off keying) | 1 | LPO short reach | Simplest (no DSP) |

**Wavelength assignments (datacenter optics):**

| Band | Wavelength | Use | Trajectory |
|---|---|---|---|
| 850nm multi-mode | 850nm | AOC + SR <100m (VCSEL) | Phasing out at 1.6T |
| O-band | 1310nm region | DR/FR ≤2km (zero-dispersion in SMF) | Dominant for AI clusters |
| C-band | 1550nm region | LR/ER/ZR ≥10km (fiber loss minimum) | DCI + telecom |
| CWDM4 | 1271/1291/1311/1331 | Legacy QSFP+ multiplex | Sunsetting |
| LAN-WDM (LR8) | 1295-1310 dense grid | 800G/1.6T DR8/FR8 | 1.6T dominant scheme |

**Reach categories** (defines transceiver SKU proliferation and laser power requirements):

| Category | Reach | Typical use | Power draw 800G |
|---|---|---|---|
| AOC (active optical cable) | <3m | Chip-to-chip intra-rack (often LPO/DML) | ~12W |
| SR (short reach) | <100m | Rack-to-rack intra-row | ~15W |
| DR (data center reach) | ≤500m | Within data hall | ~17W |
| FR (far reach) | ≤2km | Cross-campus | ~20W |
| LR (long reach) | ≤10km | Metro DCI | ~22W |
| ER / ZR / ZR+ | ≤40/120/400km | Long-haul DCI; coherent | ~25-30W |

Form factor evolution: SFP+ (10G) → QSFP+ (40G) → QSFP28 (100G) → QSFP-DD/OSFP (400G/800G) → OSFP-XD (1.6T) → NPO/CPO integrated (3.2T+). Each form factor halves power per Gbps roughly every 2 generations; pluggable thermal headroom exhausts at OSFP-XD ~30W per 1.6T port, forcing CPO migration at 3.2T+ deployment density.

**Speed-generation timeline and ASP curve:**

| Speed | First commercial | Volume year | Peak ASP | Mature ASP | Notes |
|---|---|---|---|---|---|
| 100G | 2014 | 2018 | ~$800 | $80-150 | CWDM4 / LR4 stable platform |
| 400G | 2018 | 2022 | ~$2,000 | $400-600 | DR4/FR4; 4×100G PAM4 |
| 800G | 2022 | 2024 | ~$1,500-2,000 | $600-800 (2025) | 8×100G or 4×200G PAM4 |
| 1.6T | 2025 | 2026-2027 | ~$3,000-4,000 | est. $1,200-1,500 (2028) | 8×200G PAM4 (EML-gated) |
| 3.2T | 2028E | 2029-2030E | est. $5,000+ | TBD | EML 200G×16 or TFLN 400G×8 |
| 6.4T | 2029-2030E | 2031+E | TBD | TBD | CPO-only; pluggable infeasible |

ASP compression cycle ~30-40% per generation as Chinese module scale catches up; component-level (EML, DSP) ASP rises 1.5-2x per generation due to physics-gated supply.

## Competitive dynamics

The optical networking & photonics value chain splits into six strata with distinct competitive structures, each with its own pricing power trajectory:

| Stratum | Lead Players | Moat Structure | Pricing Power 2026 |
|---|---|---|---|
| **III-V epitaxy (upstream substrate)** | Coherent (6-inch InP, vertically integrated), IQE (pure-play Western, UK/US/Taiwan), Win Semiconductors (>50% GaAs foundry), IntelliEPI (CHIPS-funded, US), VPEC (Taiwan), LandMark Opto | 12-24mo customer qualification; MOCVD/MBE process know-how; 70% InP supply gap | Strengthening — 70% InP demand shortfall, LandMark trades at ~79x revenue on scarcity |
| **EML / DFB / CW laser chips** | **Lumentum 50-60% (sole 200G at volume)**, Coherent (6-inch InP, qualifying 200G), Broadcom (Breinigsville InP fab, 50M unit capacity 2026), Mitsubishi Electric (200G mass-prod since Apr 2024), Sumitomo Electric (200G qualifying), Source Photonics | Butt-joint regrowth; failure rate scales with 4th power of bandwidth; top-5 = 75.9% of EML revenue | Strengthening at 200G+ (sole supplier pricing; double-digit price increases expected 2026); weakening at 100G (Chinese catch-up Yuanjie/Everbright) |
| **Optical DSP + ASIC** | Marvell (80%+ 800G DSP share; 1.6T Ara 3nm; 2nm Coherent roadmap), Broadcom (Tomahawk 6 switch ASIC, EML, DSP, BOLT; Bailly CPO), Cisco/Acacia (coherent DSP, pluggable ZR), MaxLinear, MACOM | 3nm/2nm design cycle cost; ecosystem lock-in; Chinese zero localization | Flat (Marvell gaining on Broadcom at 1.6T, but LPO threatens DSP TAM at short-reach) |
| **Transceiver modules (pluggable)** | **Innolight ~40% 800G, 50-60% 1.6T (#1 merchant)**, Eoptolink (#3 globally), Accelink, Cloud Light (Lumentum-owned), Coherent, AAOI, Hisense, HG Genuine | Vertical integration advantage; ASP compression from ~$1,200 (2023) to $600-800 (2025) at 800G; Chinese cost advantage | Weakening at module level (ASPs down 30-40%), except at bleeding edge (Cloud Light 70.5% GM on 1.6T EML-based) |
| **Optical contract manufacturing (EMS)** | **Fabrinet (dominant, ~28% revenue from NVDA, Cisco, Lumentum, Ciena; $3.42B FY25 → $5.39B FY26E)**, Benchmark Electronics, Sanmina, Celestica (selective) | Thailand concentration; precision optical alignment expertise; 50% capacity expansion underway | Strong — sold out through 2027, 2M sq ft expansion for +$2.4B capacity |
| **Advanced packaging / CPO integration** | **TSMC COUPE (risk prod with AMD Feb 2026; 6.4T H2 2026)**, Broadcom (Bailly 50K+ shipped), NVIDIA (Spectrum-X/Quantum-X 2026), Marvell (Celestial AI $3.25B — Photonic Fabric), GlobalFoundries/AMF (SiPh foundry), Tower Semi, Intel Foundry, Ayar Labs, Lightmatter, Ciena/Nubis ($270M Sept 2025) | Heterogeneous integration yield <70%; CoWoS capacity; wafer-scale optical alignment | Emerging — 2026 inflection year; hyperscaler adoption gated by yield |
| **Silicon photonic foundries** | **GlobalFoundries (AMF acquisition Nov 2025 — largest pure-play SiPh foundry)**, Tower Semiconductor ($650M capacity tripling by mid-2026), TSMC (COUPE 65nm+ PIC/7nm+ EIC), AIM Photonics, STMicroelectronics (re-entering), Intel Foundry | 300mm wafer scale; PDK maturity; 3 foundries = 60% of photonic wafer contracts | Strengthening as CPO scales; SiPh TAM $2.86B (2025) → $10.36B (2030) |
| **Optical circuit switching** | **Lumentum R300 (300x300 ports) + R64 MEMS-based**, Coherent (liquid crystal approach — second-scale switching), Google (internal Apollo OCS, deployed for years), Ciena Nubis (CPO angle) | MEMS mirror mfg knowledge; patent moat (1T+ mirror operating hours); physics advantage (ms vs s switching) | Emerging monopoly — Lumentum $400M+ backlog, market revised $500M → $1.5B for 2026 |

**Pricing-power trajectory is bifurcated by stratum.** Module-level ASPs are compressing (800G transceivers from ~$1,200 to $600-800 in 24 months as Chinese scale drove commoditization), but component-level pricing is moving the opposite direction. Lumentum 200G EML pricing is increasing at double-digit rates in 2026 because it is the sole volume supplier and sold out through 2027 at 8x prior capacity. Mitsubishi Electric's April 2024 200G EML mass-production launch added a second source but at low volume. Coherent's qualifying 200G EML platform and Broadcom's Breinigsville fab (projected 50M 2026 units) are adding meaningful capacity only in 2027+. The structural asymmetry — Chinese merchant dominance at module level, Western chokepoint at EML + DSP level — creates a bifurcated pricing regime that favors the laser chip layer for at least 2-3 more speed generations. This is the structural foundation of the Lumentum monopoly thesis and the reason IQE commands acquisition interest disproportionate to standalone financials.

**Market-share shifts 2022-2026:**
- Transceiver modules: Innolight from ~25% 400G share (2022) to ~40% 800G (2025) to projected 50-60% 1.6T (2026). Chinese top-10 share rose from ~45% (2022) to 70%+ (2026). Finisar/Coherent lost share as capacity couldn't ramp fast enough for 800G demand.
- EML lasers: Lumentum's share rose from ~40% (2022) to 50-60% (2026) at 200G (sole volume supplier). Coherent ramping 6-inch but still buying EMLs from Lumentum (the tell). Mitsubishi and Sumitomo hold ~20-25% combined at 100G but trail 200G by 12-18 months.
- DSP: Marvell gained from ~50% to 80%+ at 800G, Broadcom holding ~15% merchant DSP (vertically integrated into Bailly CPO). Chinese DSP localization 0%.
- OCS: Lumentum ~100% merchant share (excluding Google's internal Apollo OCS) — first-mover monopoly.
- Optical EMS: Fabrinet ~30% of optical transceiver assembly globally, rising as Celestica exits and Sanmina loses NVDA share.

**Five-front competitive war in 2026:**

- *Module makers vs. CPO displacement.* Innolight, Eoptolink, Coherent, Cloud Light, AAOI face the CPO threat: if hyperscalers deploy Broadcom Bailly / NVIDIA Quantum-X at scale, the TAM for bleeding-edge pluggable transceivers erodes by 2027-2028. Counter-move: Innolight and Cloud Light are designing hybrid pluggable-CPO architectures; Coherent is positioning SiC + InP as TSMC-independent CPO alternative.
- *EML suppliers vs. TFLN / MZ modulator substitution.* HyperLight (UMC foundry, March 2026), Lightium, and AIM Photonics position TFLN as the bandwidth leader at 400G/lane and 800G/lane (145 GHz demonstrated). SiPh Mach-Zehnder modulators remain cost-efficient for integrated CPO. If TFLN scales to volume via UMC's 8-inch foundry platform, Lumentum's EML lead resets at the 3.2T/6.4T transition.
- *Marvell vs. Broadcom at DSP.* Marvell gained 800G DSP share via earlier 5nm ramp; Broadcom's Tomahawk 6 co-designed with Bailly CPO creates a vertically integrated alternative. LPO (linear pluggable optics) threatens both by eliminating DSP for short-reach — Broadcom already achieves 35% power saving with LPO. If >33% of 800G goes LPO by 2026-2027, DSP TAM compresses before CPO replaces it.
- *TSMC COUPE vs. GlobalFoundries/AMF vs. Tower.* SiPh foundry war is the CPO manufacturing battleground. TSMC COUPE has NVDA, AMD, Broadcom early design wins but capacity-constrained. GF/AMF acquisition (Nov 2025) gives full SiPh stack ownership. Tower's $650M capacity tripling pursues the "best-of-breed specialty foundry" niche. The winner captures the CPO advanced packaging revenue pool ($95M 2025 → $1.05B 2034).
- *US vs. China supply chain bifurcation.* 75% of module fabrication in China, 70% of indium from Chinese zinc smelters, 98% gallium from China. China InP export controls imposed Feb 2025. US side: 145% tariffs on Chinese-origin transceivers (circumvented via Thailand/Vietnam final assembly). NVIDIA's Greensboro, NC InP fab funding (Lumentum) + dual-supplier $2B investments are explicit supply-chain resilience bets. Reciprocal vulnerability: Chinese modules can't run without Western EMLs and DSPs; Western systems can't scale without Chinese indium and module capacity.

**Hyperscaler deployment matrix (April 2026):**

| Hyperscaler | 2026 capex | 800G state | 1.6T state | CPO posture | Optical strategy |
|---|---|---|---|---|---|
| **Microsoft Azure** | ~$95-100B | Volume — primary AAOI customer (44% of AAOI 2024); Innolight + Cloud Light dual-source | Ramping H2 2026 — $200M AAOI 1.6T order; Cloud Light qualified | Evaluating Bailly + Quantum-X | Ethernet-heavy; NVDA + AMD ASIC dual-track; Maia internal silicon |
| **AWS** | ~$110-120B | Trainium/Inferentia internal + NVDA H100/B200 mixed; Innolight + Eoptolink primary | Q3 2026 commercial deployment | Evaluating internal CPO via Annapurna | Ethernet (EFA); aggressive cost optimization → Chinese module preference |
| **Meta** | ~$65-70B | Volume — Innolight ~50%; LPO leadership (35% power saving) | Pilot H2 2026; volume 2027 | Evaluating Bailly | LPO emphasis; MTIA internal silicon; Llama training scale |
| **Google** | ~$75-85B | Apollo OCS internal (years deployed); 800G external pluggables ramping | TPU Ironwood + 1.6T external 2026 | Internal CPO via TPU integration; OCS+CPO hybrid | OCS-first architecture; Marvell-Lumentum R300 partner; Broadcom co-designed Ironwood |
| **Oracle Cloud** | ~$30-35B | RDMA-heavy; NVDA H100/B200; Innolight primary | H2 2026 alongside GB300 | Following NVIDIA reference design | Stargate JV ($500B partnership with OpenAI announced Jan 2025) |
| **CoreWeave / Crusoe / Nebius** | ~$15-20B combined | NVDA reference architecture; Cloud Light + Innolight dual-source | 2026-2027 GB300 platform | NVIDIA-led CPO adoption | Pure-NVDA stack; no internal silicon |
| **Tencent / Alibaba / Baidu / ByteDance** | ~$50B combined | Chinese domestic merchant modules (Innolight, Eoptolink, Accelink) | 2026 ramp domestic + Western EML | Domestic CPO efforts (HiSilicon, Suzhou Lasertec) | Chinese-localization mandate; Western EML dependency at top speed |

Hyperscaler optical procurement converges on three patterns: (a) **dual-source merchant modules** to avoid single-vendor concentration (Innolight + Cloud Light + Eoptolink mix); (b) **vertical integration trials** (Google Apollo OCS, Meta MTIA, AWS Annapurna CPO, Microsoft Maia ASIC); (c) **NVIDIA reference architecture adoption** by emerging AI clouds (CoreWeave / Crusoe / Nebius / Lambda) without internal silicon teams. Implications: Cloud Light's bleeding-edge volume capture depends on Microsoft + Meta adoption (both willing to dual-source); Innolight's flat 50%+ share depends on hyperscaler tolerance for Chinese vendors at top speed (constrained by tariff + InP export risk).

## Product level analysis

### Lumentum (LITE) — pure-play laser chip + Cloud Light + OCS

Vertically positioned at the deepest-moat layer of the stack (laser chips) with expanding coverage into modules and systems.

| Product | Function | 2026 Position |
|---|---|---|
| **200G EML lasers** | Electro-absorption modulated laser on InP; single die DFB+EA via butt-joint regrowth; 8 lanes = 1.6T module | Sole volume supplier; 50-60% share; sold out through 2027; 8x capacity from FY23; 400G differential EML demo'd at OFC 2026 |
| **CW / SHP (800mW) lasers** | Continuous-wave external laser source for SiPh PICs + CPO modules | Named in NVIDIA Spectrum-X/Quantum-X specs; scales 1:1 with every SiPh shipment |
| **Narrow-linewidth tunable lasers (nano-ITLAs)** | Coherent telecom; >12.4 THz tuning range | Telecom diversification; stable |
| **1060nm VCSELs** | Co-packaged UCIe/PCIe optical links; >150°C operation | Emerging chip-to-chip optical TAM |
| **Cloud Light 1.6T transceivers** | Pluggable modules vertically integrating Lumentum's own 200G EMLs | Launched summer 2026; 70.5% GM on select products; >$1.3B FY27E revenue |
| **R300 / R64 MEMS OCS** | 300x300 / 64x64 port all-optical circuit switches; ms switching | Merchant near-monopoly; $400M+ backlog; Marvell co-demo OFC 2026; >$100M/quarter target by end-2026 |
| **Greensboro 6-inch InP fab** | $18M Qorvo facility acquisition April 2026; $5B revenue capacity | Production targeted mid-2028; NVIDIA-funded |

### Coherent (COHR) — vertically integrated photonics conglomerate

$5.8B+ revenue (FY26 run-rate); Datacom & Communications 70%+ of revenue, +36% YoY; 6-inch InP production leader.

| Product | Function | 2026 Position |
|---|---|---|
| **6-inch InP platform** | 4x device density, ~50% cost reduction vs 3-inch; four fabs (Sherman TX, Järfälla Sweden, others) | ~80% of planned 2026 doubling complete; 2+ year lead over Lumentum |
| **EML lasers (100G/200G)** | Internal for Coherent modules + external sales | Qualifying 200G; still buying 200G from Lumentum (telling gap at yield tails) |
| **Differential EML / DFB-MZ** | Alternative modulator architecture at 200G+ | Development path; reduces butt-joint regrowth dependency |
| **Transceivers (800G/1.6T)** | ~25% merchant share; volume leadership | Vertically integrated; lower GM than Cloud Light but scale advantage |
| **VCSELs (Apple Face ID)** | 3D sensing for consumer electronics | Major Apple contract (share from Lumentum); IQE-supplied epiwafers |
| **SiC substrates** | Power electronics, auto EV | Lower-growth segment; valuation drag 2023-2024 |
| **Laser systems (industrial)** | High-power industrial lasers; Rofin-Baasel divested to Bystronic | Divested 2025 to focus on datacom |

### Applied Optoelectronics (AAOI) — pluggable transceiver vendor

Sugar Land, TX; Thompson Lin CEO (founder); vertically integrated laser-to-module maker targeting $1B FY2026E revenue.

| Product | Function | 2026 Position |
|---|---|---|
| **400G / 800G datacenter transceivers** | Pluggable modules for hyperscaler deployment | Q4 2025 datacenter revenue $74.9M (+69% YoY); 90K/month 800G capacity end-2025 |
| **1.6T datacenter transceivers** | Next-gen pluggable | $200M+ single-customer order announced March 2026; production ramp H2 2026 |
| **CATV / RF laser modules** | Cable infrastructure | Legacy segment; stable |
| **In-house DFB/EML laser chips** | Vertically integrated laser production | Not at 200G volume — relies on merchant Western EMLs for top speeds |
| **500K/month 800G+1.6T capacity target** | End-2026 production ramp | 5.5x expansion vs 90K/month end-2025 |
| **$4B Amazon 10-year agreement** | Multi-year volume commitment | Disputed — Culper/BMF short reports allege Amazon/Microsoft "walked away"; reaffirmed by Zacks/Yahoo analyst coverage |

Customer concentration: Microsoft ~44% (2024), top-10 = ~95%. FY2025 revenue $455.7M → FY2026E $1B+ (consensus). Stock +237% YTD 2026 to $100+ range. Short interest elevated.

### IQE (IQE.L) — compound semiconductor epitaxial wafer foundry

World's largest independent III-V epitaxy supplier; only scaled Western provider spanning GaAs + InP + GaN + GaSb across MBE + MOCVD + CBE.

| Product | Function | 2026 Position |
|---|---|---|
| **GaAs VCSEL epiwafers** | 3D sensing (Apple Face ID via Lumentum), automotive LiDAR, short-reach datacom | Extended Lumentum supply agreement Dec 2025 |
| **InP epiwafers (EML, CW, photodetector)** | Upstream substrate for every high-speed laser | 6-inch InP foundry platform launched; multiple Tier-1 AI/hyperscale design wins |
| **GaN RF/defense epiwafers** | Military radar, electronic warfare, satellite comms | H2 2025 beat driven by US defense program funding; UK CSconnected Defence & Security Cluster anchor |
| **GaN-on-Si (sovereign supply)** | Western defense supply chain for power amps | Under development with US/UK government funding |
| **GaN microLED epiwafers** | Porotech partnership for AR/VR displays + datacom microLEDs | 8-inch GaN-on-Si foundry with unnamed consumer multinational |
| **GaSb epiwafers** | IR detectors, thermal imaging | Defense-focused; small but strategic |

FY25 revenue ~£97M (upper end £90-100M guide); adj EBITDA ~£2M (2% margin); net debt ~£70M; under UK Takeover Code offer period; Taiwan ops in sale process.

### Chinese merchant transceiver leaders

| Company | 2025 Revenue / Share | Positioning |
|---|---|---|
| **Innolight Technology** | ~$5.3B revenue, +60% YoY; ~40% 800G share; 50-60% 1.6T projected | First to complete 1.6T testing with NVIDIA; 86% overseas revenue; structural Western-component dependency |
| **Eoptolink** | 33% net margin; 179% growth; #3 globally | Aggressive 1.6T ramp; Nvidia top-2 supplier |
| **Accelink (Wuhan Research Institute)** | 500K units/month 1.6T capacity | SOE-adjacent; strong government support; coherent and datacom breadth |
| **Hisense Broadband** | Top-10 globally | Domestic + export mix |
| **HG Genuine, Hilink, Source Photonics China** | Top-10 collectively | Combined Chinese share ~70% of global merchant module market |

All Chinese merchants depend on Western EMLs (Lumentum, Coherent, Broadcom, Mitsubishi) at 200G+ and Western DSPs (Marvell, Broadcom) at 800G+. Chinese 200G EML localization estimated at 0% (BOC International).

### Silicon photonics foundries

| Foundry | 2026 Position | Customer wins |
|---|---|---|
| **TSMC COUPE** | 300mm SiPh N65 PIC + N7 EIC; CoWoS integration H2 2026; 6.4T per package | AMD (Feb 2026 risk prod), NVIDIA (Quantum-X engines), Broadcom (next-gen roadmap) |
| **GlobalFoundries / AMF** | Largest pure-play SiPh foundry post Nov 2025 acquisition; Singapore + US + Europe | Marketing "China-free" photonics supply chain; $1B+ photonics rev target by 2030 |
| **Tower Semiconductor** | 2x SiPh capacity by end-2025, 3x by mid-2026; $650M investment; CPO foundry platform | OpenLight (InP-on-Si), diverse CPO startups |
| **AIM Photonics** | US consortium; government-backed; smaller scale | Defense-adjacent; TFLN process access |
| **STMicroelectronics** | Re-entering SiPh after ~5yr absence | Auto/industrial focus |
| **Intel Foundry** | Legacy 300mm SiPh; shifted focus to CPO integration | Internal Xeon networking; selective external |

### Optical DSP

| Vendor | 2026 Position |
|---|---|
| **Marvell** | 80%+ 800G merchant DSP share; 1.6T Ara/Aquila 3nm portfolio Q1 2026; 2nm coherent DSP roadmap; $3.25B Celestial AI acquisition for CPO |
| **Broadcom** | ~15% merchant DSP but vertically integrated into Bailly CPO + Tomahawk 6 switch ASIC; Davisson-TH6 102.4 Tbps |
| **Cisco/Acacia** | Coherent DSP + pluggable ZR specialist; $4.5B acquisition closed 2021 |
| **MaxLinear, MACOM, Inphi (Marvell)** | Niche DSP + driver roles; MACOM focuses on linear drivers for LPO |

### Fabrinet (FN) — optical EMS

$3.42B FY25 revenue → $5.39B FY26E (+33%); 2M sq ft facility expansion underway; Thailand concentration. NVDA 28% of FY25 revenue; also Cisco, Lumentum, Ciena, Coherent as customers. Dominant in 1.6T module assembly for NVIDIA Blackwell/Rubin. Capacity capacity +50% post-expansion = +$2.4B annual revenue potential. Sold out through 2027.

### Optical circuit switches

| Vendor | Technology | 2026 Position |
|---|---|---|
| **Lumentum R300 / R64** | MEMS (microelectromechanical mirrors); ms switching | Merchant near-monopoly; $400M+ backlog; Marvell OFC 2026 co-demo |
| **Coherent** | Liquid crystal approach; second-scale switching | Trailing; slower switching disadvantageous for AI bursty traffic |
| **Google Apollo** | Internal MEMS OCS | Deployed across Google DCs for years; not sold externally |
| **Ciena / Nubis** | CPO-adjacent intra-DC switching | $270M acquisition Sept 2025; 6.4 Tbps modules |

OCS market revised $500M → ~$1.5B for 2026; $2.5B by 2029 (Cignal AI).

### TFLN (thin-film lithium niobate) modulator startups

| Company | 2026 Position |
|---|---|
| **HyperLight** | TFLN Chiplet platform; UMC/Wavetek foundry partnership March 2026; 400G-per-lane PICs; 145 GHz bandwidth |
| **Lightium** | TFLN startup with VC funding; less visible 2026 commercial progress |
| **Quantum Computing Inc** | TFLN fab for quantum photonic applications |
| **Lightwave Logic** | Electro-optic polymer modulator alternative; 100GHz+ |

TFLN market projected at 44.4% CAGR through 2032 — early stage but threatens EML at 3.2T/6.4T.

### Optical test equipment — wafer-level capacity bottleneck

Photonic chips test fundamentally differently from electrical ICs: each device requires a wavelength sweep across 10-50 wavelengths, sub-micron grating-coupler alignment, simultaneous photonic + electrical measurement, and laser burn-in days per wafer for reliability qualification. Result: photonic test runs 5-10x slower per device than electrical probing. Hyperscaler-grade SiPh + CPO ramps explicitly bottleneck on test capacity, not wafer fab — TSMC, GlobalFoundries, and Tower have flagged photonic test as the throttle on COUPE and AMF expansion. Aehr Test management commentary (Q4 2025) corroborates: photonic burn-in customer adds 4x volume YoY but shipping is gated by FOX-XP delivery slots through 2027.

| Vendor | Listed (mkt cap) | Photonic product line | 2026 photonic position |
|---|---|---|---|
| **Aehr Test Systems (AEHR)** | Yes (~$0.7-0.9B; thin sell-side) | FOX-XP wafer-level burn-in for laser/PIC reliability qualification | Sole volume photonic burn-in solution; ~$50-80M FY26E photonic revenue (40-60% of total); customer concentration on TSMC + GF + Tower; FOX-XP order book extends through 2027 |
| **FormFactor (FORM)** | Yes (~$3-4B) | Cascade optical probe cards + photonic engineering probe systems | Photonic ~10-15% of probe-card revenue, growing 30-40% YoY; SiPh wafer-level alignment + photonic DC/RF concurrent probing |
| **Teradyne (TER)** | Yes (~$15-20B) | UltraFlex / J750 platforms with photonic instrument modules; Optical Test Cell (OTC) integrated handler | Photonic test ~$80-120M FY26E; gaining share at hyperscaler IDMs (NVDA, AMD captive lines); production-scale handler integration play |
| **MKS Instruments (MKSI)** | Yes (~$8-10B) | Newport-Spectra-Physics tunable lasers + Photon Control optical metrology + vacuum systems for InP MOCVD/MBE | Optical/photonic ~5-10% of revenue (high-margin, accelerating); upstream tool play for III-V epitaxy capacity adds (IQE, COHR, Win Semi, VPEC) |
| **Keysight Technologies (KEYS)** | Yes (~$25-30B) | N4391A optical modulation analyzer; M8000 BERT family; lightwave component analyzers; high-speed sampling oscilloscopes | Photonic ~10% of test sector revenue; design-side test for every coherent ZR/ZR+ + 800G/1.6T PHY validation; recurring service revenue |
| **Anritsu (TYO:6754)** | Yes | MP2110A BERT, MS9740B OSA, signal/spectrum analyzers | Asia-strong test footprint; 800G/1.6T BERT for component qualification; smaller than KEYS, cost-competitive |
| **Viavi Solutions (VIAV)** | Yes (~$1.5-2B) | OSA, OTDR, network test for transceiver manufacturing + field test | Spun from JDSU 2015; 30%+ datacom exposure; transceiver production-line test complement to design-side KEYS |
| **EXFO (private since 2022)** | No (taken private by Germain Lamonde) | Optical test for telecom + datacenter field deployment | Private — benchmark for telecom-side test market structure but not a public-market expression |
| **Captive (LITE, COHR in-house)** | LITE, COHR | Internal proprietary photonic production test cells | Vertically integrated; adds to merchant test demand only via expansion (not 3rd-party purchases) |

**Investment dynamics at the test stratum:**

1. **Aehr Test (AEHR) is the most concentrated pure-play photonic test bet.** Wafer-level burn-in is the most constrained step in the photonic test sequence (days per wafer vs minutes for electrical probing). Each FOX-XP system supports ~$200-500M of laser-chip qualification volume over its lifetime, and current order book extends through 2027. Revenue ramp scenario: 30%+ photonic burn-in penetration of CPO line by 2028 implies $200-300M revenue (vs ~$50-80M FY26E photonic) — 4-5x revenue scenario at sub-$1B current cap. Risk: AEHR's customer concentration mirrors TSMC COUPE concentration risk — if CPO yields disappoint or schedules slip, AEHR's photonic ramp slips proportionally. Limited sell-side coverage (<6 active analysts) keeps the thesis structurally non-consensus.

2. **FormFactor (FORM) and Teradyne (TER) are diversified photonic test exposure.** Both have advanced-node electrical test as the dominant business line, with photonic test as an attached growth vector (~10-15% of probe-card / handler revenue). FORM's optical probe-card business attaches to GF-AMF and TSMC COUPE wafer flow; TER's OTC handlers integrate at hyperscaler IDMs. Beta exposure to photonic supercycle without binary ramp risk — but lower upside per dollar invested vs AEHR.

3. **Keysight (KEYS) and Anritsu are design-side test equipment.** Every PHY design house and validation lab needs high-speed BERT, optical signal analyzer, and component analyzer for 800G/1.6T validation. Lower revenue concentration to photonics (KEYS ~10% of sector revenue) but high margin and recurring service revenue. KEYS particularly benefits from coherent ZR/ZR+ design proliferation across telecom equipment vendors (heuristic #11 — telecom optical re-investment cycle).

4. **MKS Instruments (MKSI) is the upstream tool play** — InP epitaxy and metrology demand scales with III-V wafer fab capex, indirectly tracking IQE / Coherent / Win Semi / VPEC capacity adds. Lower beta than AEHR but linked to total III-V fab investment cycle. Also exposed to lithography metrology for SiPh and standard semiconductor process control.

5. **The test-bottleneck thesis is structurally non-consensus.** Sell-side coverage for AEHR is thin; the photonic test category is not standardly broken out in industry forecasts (LightCounting and Yole estimate photonic device TAM at $90B+ by 2030 but do not separately size test infrastructure); and most institutional photonic exposure flows to LITE / COHR / FN without recognizing the upstream test capacity bottleneck. AEHR's <$1B market cap with $200-300M revenue trajectory through 2028 (assuming 30% photonic burn-in penetration) creates asymmetric exposure to the same physics-gated supercycle as LITE — a "second-derivative" photonics trade with much lower entry valuation.

## Acquisitions and new entrants

**NVIDIA's dual $2B photonics investment (March 2026)** is the defining capital event of the cycle — explicit supply-chain resilience bet on the InP laser chokepoint. $2B convertible preferred to Lumentum (tied to Greensboro 6-inch fab development) + $2B to Coherent. Structured as capacity lock-out + multi-year purchase commitments. Mirrors NVIDIA's earlier SK Hynix / Samsung / Micron HBM allocation playbook. For context: NVIDIA's own market cap ~$3.5T could comfortably fund outright acquisition of either, but dual-investment preserves merchant supply-chain optionality while de-risking.

**GlobalFoundries acquisition of Advanced Micro Foundry (AMF), November 2025** — positioned GF as the world's largest dedicated SiPh foundry. Strategic logic: create a "China-free" SiPh supply chain ahead of expected Commerce Department export restrictions on Chinese silicon photonics (Moolenaar/Krishnamoorthi Congressional push).

**Other major M&A 2022-2026:**

| Transaction | Value | Closed | Strategic Purpose |
|---|---|---|---|
| **II-VI - Coherent Inc** | $7B | Jul 2022 | Vertical integration across materials/lasers/modules; re-branded as Coherent Corp |
| **Lumentum - Cloud Light** | $750M | Oct 2023 | Pluggable transceiver vertical integration |
| **Cisco - Acacia Communications** | $4.5B | Mar 2021 | Coherent DSP + pluggable ZR technology |
| **Marvell - Celestial AI** | $3.25B | 2025 | CPO Photonic Fabric; OMIB 16 Tbps modules |
| **GlobalFoundries - AMF** | undisclosed | Nov 2025 | SiPh foundry scale; "China-free" supply chain |
| **Ciena - Nubis Communications** | $270M | Sep 2025 | Intra-DC CPO angle; 6.4 Tbps modules |
| **Lumentum - NeoPhotonics** | ~$900M | 2022 | Coherent + 100G+ laser capacity |
| **Panasonic - Blue Yonder** (adjacent) | $7.1B | 2021 | Supply-chain-adjacent optical enablement |
| **Lumentum - Qorvo Greensboro facility** | $18M | Apr 2026 | Future 6-inch InP site; $5B revenue capacity |
| **Coherent - Rofin-Baasel divestiture** | undisclosed | 2025 | Portfolio rationalization; focus on datacom |

**Emerging / new entrant disruption strategies (2023-2026):**

- **HyperLight + UMC + Wavetek (TFLN)**: March 12, 2026 foundry partnership for 6-inch and 8-inch TFLN chiplet volume production. Targets 400G-per-lane and beyond where EML physics becomes constrained.
- **Ayar Labs (optical I/O)**: Secured $155M Series D funding 2024; Intel and NVIDIA investors; TeraPHY optical I/O chiplets for XPU-to-XPU intra-package optics.
- **Lightmatter**: $850M Series D at $4.4B valuation; Passage photonic interconnect for 3D-stacked compute; targeting 2027 commercial CPO for hyperscaler AI clusters.
- **OpenLight** (Synopsys spin-out; HPE, Juniper backing): InP-on-silicon integration via Tower Semiconductor foundry — reduces external laser packaging dependence.
- **Lightwave Logic**: Electro-optic polymer modulators, 100GHz+; longer-term threat to EML and TFLN if standard fab integration succeeds.
- **Celestial AI** (acquired by Marvell $3.25B): Photonic Fabric with OMIB delivering 16 Tbps, 25x bandwidth vs conventional CPO. Example of successful startup exit to integrated player.
- **Digital twins for optical networks, AI-driven characterization test bottleneck startups**: Aehr Test (FOX-XP wafer-level burn-in for SiPh dies) — testing is the systemic bottleneck throttling the entire sector's ramp.
- **Chinese SiPh push**: Moolenaar-Krishnamoorthi Congressional letter (2025) specifically targeted Chinese SiPh as "next front" — regulatory headwind against Chinese photonic foundry scale.

**Key incumbent conclusion**: acquisition intensity reflects a recognition that single-point-of-value bets (only EML, only DSP, only module assembly) are structurally exposed to architecture shifts (CPO, TFLN, LPO). Vertical integration (Coherent II-VI + Coherent Inc; Lumentum Cloud Light + Qorvo Greensboro; Marvell Celestial AI) and dual-sourcing (NVIDIA both Lumentum and Coherent) are the twin hedging patterns. AAOI and IQE represent the "unconsolidated middle" where M&A outcomes dominate standalone narrative.

## Macro shifts

**1. The copper-to-optics transition is physically mandatory, not demand-elastic.** Electrical signaling over copper traces hits reach/bandwidth limits at ~100-200 Gbps per lane over distances >~1m. AI clusters beyond 8-GPU pods require optical interconnects by physics, not preference. NVIDIA estimates a million-GPU datacenter with pluggable optics would consume 180 MW just for networking — forcing CPO adoption. McKinsey / Cignal AI / LightCounting triangulate that all AI datacenter interconnects become optical within 5 years. Implication: optical demand is growth-inelastic to individual AI capex pullbacks; the only real bear case is a full AI capex crash that reduces raw cluster build-out, not a relative compute/optical rebalancing.

**2. $18B → $90B optical interconnect TAM expansion (2025-2030).** 5x market expansion driven by AI-specific workloads. LightCounting March 2026 forecast: $100B market for AI cluster optics by 2030. 2026-specific: $26B Ethernet AI optics (+60% YoY); 63M 800G+ units (2.6x YoY); 22M 1.6T units (first year of 1.6T commercialization with upward revision pressure per Goldman). SiPh foundry market $2.86B (2025) → $10.36B (2030) → $28.75B (2034) at ~29% CAGR.

**3. CPO inflection year 2026 — capacity-constrained, not demand-constrained.** NVIDIA Spectrum-X/Quantum-X deployments begin H2 2026. TSMC COUPE entered risk production with AMD February 2026, targeting 6.4T per package volume H2 2026. Broadcom Bailly 50,000+ switches already shipped (first commercial CPO). But heterogeneous integration yields remain <70% (vs 80-85% needed for commercial viability). Advanced optical chip production projected +80% YoY 2026 but still 5-15% short of demand. The 2026 bull case is capacity-gated ramp; the bear case is a high-profile CPO field failure chilling adoption for 12-18 months and reverting demand to pluggable + OCS architectures.

**4. Linear pluggable optics (LPO) as transitional architecture.** LPO eliminates the DSP, cutting power 30-50% and latency to <15 ns. Broadcom reports ~35% power savings with its LPO implementation. >33% of intra-datacenter 800G deployments forecast to adopt LPO or LPO/DSP hybrid by 2026-2027. Already shipping in NVIDIA Spectrum-X and Meta AI networks. Implication: DSP revenue (Marvell + Broadcom) faces compression before CPO matures; LPO benefits linear driver specialists (MACOM) and component-side players (Lumentum 200G EMLs work in both DSP and LPO modules).

**5. Geopolitical supply-chain bifurcation accelerates.** Mutual weaponization: (a) US 145%+ tariffs on Chinese-origin transceivers (circumvented via Thailand/Vietnam final assembly); (b) Chinese export controls on gallium (Aug 2023, 98% primary Ga), indium (Feb 2025, 59% primary In), and InP (Feb 2025). Reciprocal dependency: Chinese modules depend on Western EMLs (100% at 200G) and DSPs (100% at 800G+). NVIDIA Greensboro fab mandate for Lumentum, Coherent's US/EU fab footprint, GlobalFoundries "China-free" marketing, Moolenaar/Krishnamoorthi Congressional letter all point to deliberate supply-chain resilience bets. Western InP capacity expansion: Lumentum Greensboro $5B revenue capacity (mid-2028); Coherent 6-inch InP doubling (~80% complete); Eindhoven 6-inch InP (EU Chips Act, €150M, 2028); IntelliEPI CHIPS-funded MBE expansion.

**Materials concentration detail** (the deeper supply chain layer below epitaxy):

| Material | Use | China share of primary supply | Key non-China sources | Spot-price trajectory 2024-2026 |
|---|---|---|---|---|
| **Indium (In)** | InP substrate (1g/InP wafer); ITO displays | ~59% primary; Chinese zinc smelter byproduct | Korea (~13%), Japan (~12%), Canada (Teck), Peru | $400 → $700/kg (+75%); Feb 2025 export controls compounded scarcity |
| **Gallium (Ga)** | GaAs/GaN substrate; LEDs | 98% primary | Russia, Germany (Recovery), Hungary | $300 → $1,200/kg (+300%); Aug 2023 controls drove 4x spike |
| **Germanium (Ge)** | Optical fiber dopant; IR optics; III-V epitaxy | ~60% primary | Russia, US (Teck Trail), Belgium | $1,500 → $4,000/kg (+167%) |
| **Phosphorus (P, high-purity 6N+)** | InP precursor | ~70% China | Morocco, US, Russia (lower purity) | Stable but specialty grades constrained |
| **Lithium niobate (LiNbO3 wafers)** | TFLN modulators | ~50% China + Russia | Crystal Technology (US), Yamaju Ceramics (Japan) | Shortage emerging as TFLN scales |
| **Rare earths (Yb, Er, Nd doping)** | EDFA fiber amplifiers; doped fiber | ~70-90% China primary | Lynas (Australia), MP Materials (US), Vital Metals | Erbium $80 → $150/kg in 2024-25 |

**InP wafer pricing dynamics:** 4-inch InP wafer ~$1,500-2,000; 6-inch ~$3,000-4,000 (cost scales with crystal-pulling complexity, not area). 6-inch yields 4x devices per wafer at ~50% cost reduction per device — explains why Coherent's 6-inch lead is structurally meaningful. IQE, Win Semiconductors, and LandMark Optoelectronics are the only scaled non-Chinese pure-play epi houses. China's Suzhou Lasertec and Shenzhen Han's Photonics are 2-3 years behind 6-inch InP.

**Indium criticality math:** Each 1.6T module uses ~1 gram InP across 8 EMLs + ~0.5g for CW lasers + InP photodetectors. 22M 1.6T units (2026) ≈ 33 metric tons InP demand. Global primary indium production ~900 tons/year — datacom optics already consumes 3-4% and rising 30% YoY. Spot indium prices doubled 2024-2025 reflecting this sectoral shift.

**6. S&P 500 inclusion / passive flow structural tailwind.** Lumentum joined S&P 500 in 2026 — with $7T+ benchmarked to the index, passive buying creates a structural valuation floor through price-insensitive institutional buying. Coherent is S&P 500 constituent. Fabrinet moved from IWM to S&P 400; AAOI remains small-cap. The S&P 500 inclusion mechanic creates a 2-3 day demand shock equivalent to ~1-2% of outstanding shares at inclusion and persistent rebalancing demand.

**7. Test and characterization as systemic bottleneck.** SiPh and CPO manufacturing is throttled less by wafer fabrication capacity than by test throughput: photonic chip testing requires full wavelength sweeps and repeated alignment, ~10x slower than electrical probing. Aehr Test's FOX-XP wafer-level burn-in is the first volume solution. MKS Instruments and FormFactor also position for optical characterization. Implication: the "picks and shovels" trade within the photonics supercycle includes optical test equipment makers that solve the ramp bottleneck.

**8. Defense / sovereign supply chain premium on Western III-V.** GaN RF for military radar, electronic warfare, satellite communications requires domestic sourcing by regulation. UK CSconnected cluster (2,800+ jobs, £160M Investment Zone, Wales Defence & Security Cluster launched March 2026) anchors IQE in a government-backed ecosystem. US CHIPS Act $10.3M to IntelliEPI for III-V expansion. EU Chips Act €150M to Eindhoven 6-inch InP fab. This creates acquisition value for Western III-V assets disproportionate to their standalone commercial financials — the IQE offer period dynamic reflects this premium.

**9. Power / thermal as the new scaling axis.** Per-rack compute power exceeds 100 kW for GB200 NVL72 and beyond. Pluggable transceivers consume ~30W/port at 1.6T; CPO ~9W/port. Power per bit is the gating constraint at million-GPU scale. CPO + OCS + LPO together could reduce networking power per bit by 70-80% vs. traditional DSP-based pluggable architectures — unlocking 2-3x more compute for the same data center power envelope. This is the non-cyclical demand driver behind the optical supercycle.

## Investor heuristics

**Current consensus framing.** Investors broadly treat optical networking as "pick the NVIDIA beneficiary list" — Lumentum, Coherent, Fabrinet, Arista (networking adjacent), Marvell, Broadcom. The sell-side narrative centers on hyperscaler capex pass-through: every incremental $100B of AI infrastructure spending flows ~10-15% to optical interconnect revenue. Valuations have re-rated sharply: Lumentum +1,098% trailing 12 months, Coherent +328%, AAOI +237% YTD 2026. Forward P/E multiples compressed from peak to 20-50x range as earnings caught up to price. The consensus bull case: continued hyperscaler capex growth + CPO inflection = multi-year earnings compounding. The consensus bear case: AI capex pullback + Chinese component catch-up + CPO architectural disruption to pluggable TAM.

**Valuation dispersion within the sector is extreme, reflecting investor disagreement on which layer captures durable value:**

| Company | Est. Mkt Cap | Est. EV/Rev FY26E | Rev Growth FY26E | Pricing Narrative |
|---|---|---|---|---|
| **LITE** (Lumentum) | ~$55-62B | ~19-22x | +79-85% (reported) | Physics-gated EML monopoly; S&P 500 inclusion; Greensboro 6-inch InP optionality |
| **COHR** (Coherent) | ~$40-50B | ~8.2x | +17-25% | 6-inch InP lead; vertical integration; Anderson turnaround |
| **AAOI** (Applied Optoelectronics) | ~$4-5B | ~5-7x | +120% ($455M→$1B) | Hyperscaler concentration bet; short-interest elevated; 1.6T order catalysts |
| **FN** (Fabrinet) | ~$20-25B | ~4-5x | +33% ($3.4B→$5.4B) | Optical EMS monopoly; 2M sq ft expansion; sold out through 2027 |
| **IQE** (IQE.L) | ~£525M (~$660M) | ~6.1x | Revenue recovering | Takeover special situation; Taiwan sale pending; EV/Rev at peer parity |
| **MRVL** (Marvell) | ~$75-90B | ~6-8x | +12-20% | Optical DSP + Celestial AI + custom silicon |
| **AVGO** (Broadcom) | ~$1.3T+ | embedded | high teens | Bailly CPO + Tomahawk 6 + DSP; horizontal play |
| **Innolight** (China-listed) | ~$30-40B | ~5-7x | +50-60% | Merchant module #1; Western component dependence |

**What's priced in (April 2026):**
- Lumentum: physics-gated EML monopoly recognized; $2B quarterly run-rate by late 2027 embedded; modest Greensboro execution risk priced.
- Coherent: 6-inch InP lead recognized; Anderson margin expansion partially priced; vertical integration narrative complete.
- AAOI: $1B FY26 revenue fully in; hyperscaler concentration risk + short thesis partially discounted.
- Fabrinet: optical EMS monopoly recognized; expansion capacity priced; execution on 2M sq ft is the swing factor.
- IQE: ~45-60p takeover outcome priced; residual downside to 4.7p if offer period lapses.

**Where consensus is likely wrong (non-consensus framings):**

1. **The "arms dealer" asymmetry — Lumentum wins regardless of which module vendor captures downstream share.** Investor debate centers on "Innolight vs Cloud Light vs Coherent" for module share — but at 200G+ only Lumentum (sole volume) + Coherent (qualifying) + Broadcom (internal) + Mitsubishi (low vol) can supply the EML. Every merchant module shipped pays a toll to 2-3 Western laser makers. The component-level structural premium to module-level scale is inverted from typical SaaS/software framing where scale IS the moat. Research: [[Research/2026-04-15 - LITE COHR - Lumentum vs Coherent Analysis]] Module-level gross margin 70.5% on Cloud Light 1.6T vs industry 30-40% quantifies this asymmetry.

2. **Silicon photonics foundry buildout is paradoxically bullish for InP laser demand.** Consensus reads GF/AMF acquisition, Tower 3x expansion, TSMC COUPE, STMicro re-entry as threats to InP. Physics: silicon has indirect bandgap and cannot generate laser light. Every SiPh transceiver and CPO module requires external InP or GaAs laser sources. SiPh penetration rising from 24% (2022) to 44% (2028) of transceivers = 1.8x InP laser demand growth from this vector alone, on top of volume growth. LightCounting: laser + PIC revenue $2.4B (2023) → $5.9B (2029). EML market specifically $1.3B (2023) → $3.0B (2027) concurrent with SiPh $0.8B → $4.6B — complementary, not substitutive. This is explicitly not priced in Lumentum's current multiple.

3. **Chinese module dominance masks a critical Western chokepoint — the asymmetry compounds each speed generation because failure rate scales with the 4th power of bandwidth.** Innolight + Eoptolink 60% of NVDA GB200 volume looks existentially threatening to Western module makers, but at the component level Chinese InP laser localization is ~3% at 25G+ and 0% at 200G. Every 800G module paid ~$40-80 to Lumentum for its 8 EMLs; every 1.6T module pays $80-160. ASP doubles with speed while manufacturing cost rises only ~15%, creating 16x harder yield problem that physics-gates the competitive gap. The bear narrative ("China catches up to everything eventually") misunderstands that the gap widens at each speed generation, not narrows. Chinese 200G EML timeline: Yuanjie/Everbright 2027-2030, vs Western 200G at volume today.

4. **OCS is a structural category, not a niche — and Lumentum has a merchant monopoly.** Consensus models OCS as a $500M-$1B specialty market. Cignal AI upward revision to $1.5B (2026) and $2.5B (2029) reflects Google Apollo going external and Marvell-Lumentum R300 demo at OFC 2026 signaling broader hyperscaler adoption. OCS advantages (95% power reduction vs electrical switches, ms switching speed for AI training dynamic reconfiguration, data-rate agnosticism allowing "deploy once, upgrade edges" economics) are structural. Coherent's liquid crystal approach (second-scale switching) is inferior for AI training — it's a real competitive gap, not a technology race. Lumentum's $400M+ backlog and $100M/quarter target by end-2026 understates the durability of a near-merchant-monopoly in a compounding category.

5. **IQE's acquisition value decouples from standalone fundamentals — the M&A discount has partially closed but strategic value is still mispriced.** At ~52p / ~6.1x EV/Rev, IQE trades near peer multiple (Win Semi 6.7x, Coherent 6.9x) on pro-forma view. But Takeover Code offer period + Taiwan sale + UK Defence & Security Cluster anchor + sole Western pure-play multi-III-V epitaxy supplier = strategic premium reflection incomplete. LandMark Optoelectronics (~$4.77B mkt cap on ~$60M revenue, ~79x rev) demonstrates the acquisition multiple for pure InP capability. A strategic acquirer (defense, foundry, or integrated photonics player) with CPO ambitions could justify 80-120p+. Research: [[Research/2026-03-02 - Chinese Silicon Photonics Threat]] — Moolenaar-Krishnamoorthi Congressional push for Chinese SiPh export restrictions strengthens Western epitaxy scarcity value.

6. **AAOI's $1B guidance depends on specific hyperscaler contracts that Culper Research and BMF Reports have aggressively shorted.** Consensus treats the $200M 1.6T order + $124M 800G order + $4B 10-year Amazon agreement as reliable forward signals. Culper Research ("An Optical Illusion") and BMF Reports allege Amazon and Microsoft "walked away" after September 2024 delivery disappointments. Microsoft 44% of 2024 revenue + top-10 = 95% customer concentration is binary — if any major customer reduces orders, the $1B target fails spectacularly. AAOI lacks the vertical laser chip integration Lumentum has at 200G (buys merchant EMLs), meaning its gross margin at 1.6T depends on merchant component availability it doesn't control. The short thesis is not trivially dismissible; the long thesis requires belief in hyperscaler dual-sourcing discipline maintained through AAOI's ramp execution.

7. **Fabrinet is the under-appreciated pure-play on optical volume — independent of which module/component vendor wins.** $3.42B FY25 → $5.39B FY26E (+33%); ~28% NVDA revenue; 2M sq ft expansion = +$2.4B future capacity; sold out through 2027. Fabrinet captures revenue regardless of whether Innolight, Cloud Light, Coherent, AAOI, or Ciena wins the module contract — all assemble through Fabrinet. The optical EMS monopoly at 1.6T is as structural as Lumentum's EML monopoly at the laser chip layer. At ~4-5x EV/Rev vs Lumentum ~20x, Fabrinet captures similar upside exposure at a third the multiple. Consensus under-weights Fabrinet because it lacks IP/moat narrative — but ramp-constrained capacity + Thailand concentration + precision optical alignment expertise + customer diversification IS the moat in a supply-constrained cycle.

8. **TFLN is a 3-5 year threat to EML at 3.2T+ that resets the competitive clock.** HyperLight + UMC + Wavetek March 2026 announcement = TFLN Chiplet foundry on 6-inch and 8-inch wafers. HyperLight 400G-per-lane demo on TFLN + 145 GHz bandwidth vs EML 200G-per-lane commercial = bandwidth leadership. Lightwave Logic's 100GHz+ electro-optic polymer modulators are a second-horizon alternative. If TFLN scales to volume at 3.2T/6.4T transition (2028-2030), Lumentum's EML monopoly resets and Coherent's 6-inch InP lead becomes less relevant. This is the longest-duration structural risk to the current laser chip pricing power — not priced in LITE's forward multiple.

9. **Coherent's Anderson turnaround uses a Lattice-Semi playbook that the market discounts.** Jim Anderson grew Lattice from $5B to ~$20B market cap (~4x) over six years (2018-2024) by exiting non-core lines, refocusing R&D, and lifting gross margin from ~57% to ~70%. At Coherent he has parallel levers: (a) Rofin/Bystronic divestiture 2025; (b) SiC overcapacity wind-down (consensus headwind already in numbers); (c) 6-inch InP scale economics (~50% device cost reduction); (d) Datacom mix shift from 50% → 70%+ of revenue. Coherent's ~30% GM has 600-800 bps expansion runway by FY28 on the same Lattice trajectory. Consensus models 50-100 bps/year — Anderson's track record points to 200-300 bps/year. The valuation gap to LITE (~8x vs ~20x EV/Rev) embeds none of this. Research: [[Research/2026-04-15 - LITE COHR - Lumentum vs Coherent Analysis]]

10. **The optical-test-equipment "picks and shovels" trade is the underappreciated scarcity bottleneck.** Every photonic chip requires full wavelength sweep + alignment testing — 5-10x slower than electrical probing. Current test capacity is the binding constraint on SiPh + CPO ramp — TSMC, GF, and Tower all flag test as the throttle, not wafer fab. Aehr Test FOX-XP wafer-level burn-in is sole volume solution; FormFactor optical probes; Teradyne IST optical handlers; MKS Instruments optical metrology. AEHR alone could see 5-10x revenue if SiPh test penetrates 30%+ of CPO line. Yet AEHR trades at <$1B market cap with limited sell-side coverage. Consensus treats test as commodity — physics says test capacity bottlenecks the entire $90B optical TAM through 2028.

> [!todo] 2026-04-28 → Addressed 2026-04-28
> **Prompt:** *Provide more detailed analysis on the test equipment vendors and dynamics at play here*
>
> **Response:** Detailed analysis added as new subsection §Product level analysis → Optical test equipment — wafer-level capacity bottleneck. 9-vendor breakdown (AEHR, FORM, TER, MKSI, KEYS, Anritsu, VIAV, EXFO, captive LITE/COHR) with mkt cap, photonic product line, and 2026 position; plus 5 investment-dynamic conclusions on test as the binding capacity constraint. AEHR is the highest-asymmetry expression — sub-$1B mkt cap with 4-5x revenue scenario at 30% CPO photonic-burn-in penetration; structurally non-consensus given thin sell-side coverage and that photonic test is not separately sized in standard industry forecasts.

11. **Telecom optical re-investment cycle is an unmodeled second wave.** Hyperscaler optics dominates 2024-2027 narrative, but tier-1 telcos (AT&T, Verizon, Deutsche Telekom, NTT, BT) cut optical capex 60%+ from 2018-2023. AI inference deployment requires regional edge data centers + DCI buildout — 400G/800G ZR/ZR+ pluggables are the deployment mechanism. Cisco/Acacia, Ciena, Nokia, Adtran position for this cycle. ZR/ZR+ pluggable shipment forecast 2.4M (2025) → 8.5M (2028). LITE's nano-ITLA tunable lasers, COHR's coherent transceivers, and Marvell's coherent DSP all benefit. Telecom optical re-investment = 2027-2030 secular tailwind not in current 2026 multiples.

12. **The "memory wall" is becoming the "interconnect wall" — and optical is the only solution.** HBM4/HBM5 add 2-4x bandwidth per stack but GPU-to-GPU and rack-to-rack bandwidth scales worse than memory bandwidth. NVLink 5 (1.8 TB/s/GPU bidirectional) and NVLink 6 require optical at >10m reach. CXL 3.0 fabric expansion across racks demands optical interconnect. The next bottleneck after memory is the network, and optical interconnect is the only physics-feasible path. This shifts the "AI bottleneck" trade from HBM (Hynix/Micron/Samsung) to optical interconnect (LITE/COHR/MRVL/AVGO/FN). Multi-year mind-share rotation from memory to optics could expand sector multiples by 30-50% as institutional capital re-categorizes the AI bottleneck thesis.

**Non-consensus framing for portfolio construction:** Optical networking & photonics is a **stratified value chain where different layers have fundamentally different moat durability**. The disciplined portfolio expression:
- **Structural longs**: Lumentum (component-level monopoly; SiPh paradox + OCS + Cloud Light triple expansion; NVIDIA alignment); Fabrinet (optical EMS near-monopoly at volume); IQE (M&A special situation with Western III-V scarcity premium).
- **Avoid middle-layer consolidators without clear moats**: module-only plays (AAOI hyperscaler concentration; Innolight Western-component exposure); DSP-only plays (LPO compression risk).
- **Monitor for inflection**: TFLN volume ramp (HyperLight/UMC/Wavetek); CPO yield improvement (TSMC COUPE, Bailly); Chinese 200G EML localization milestones.
- **Hedging dynamics**: Coherent as partial hedge to Lumentum execution risk (6-inch lead); Broadcom as hedge on vertical integration winning at CPO; Marvell as hedge on DSP continuation + Celestial CPO optionality.

**Cross-cycle valuation context.** The 2000 telecom bubble peaked at JDSU $153B + Nortel $398B = ~$550B optical equipment-and-component sector cap. The 2026 AI photonics sector cap (LITE + COHR + FN + AAOI + MRVL optical share + AVGO optical share + Innolight + Eoptolink + Accelink) ≈ $400-500B at current multiples — approaching but not yet matching the 2000 absolute peak. Critical difference: 2026 optical revenue runs ~$30B vs 2000 peak ~$40B (in nominal dollars; ~$70B inflation-adjusted), but customer concentration is healthier (8+ hyperscalers vs 1990s telco oligopoly), order visibility extends 18-24 months (vs 1990s build-on-spec), and the demand driver is physics-mandatory (vs 1990s speculative dark fiber). The 2000-2002 collapse was a 99% derate over 24 months on an industry that overbuilt 5-7x demand on dark fiber speculation. The 2026 cycle is supply-constrained, not demand-speculative — this asymmetry caps the symmetric downside risk.

## Adjacent applications and TAM extension vectors

Optical networking IP and component supply chain extends across multiple adjacent verticals that compound the supercycle thesis. These are second-order beneficiaries with longer-duration adoption curves but materially expand the addressable market for the same Western III-V chokepoint suppliers.

**1. Optical AI compute (photonic neural networks).**

| Company | Approach | Stage | Backers |
|---|---|---|---|
| **Lightmatter** | Passage photonic interconnect for 3D-stacked compute | $850M Series D at $4.4B valuation | Google Ventures, GV, SIP Global |
| **Lightelligence** | Photonic computing for AI inference (Hummingbird) | Series C | Hopu, Maverick, Baidu |
| **Luminous Computing** | Optical AI accelerator | Series A | Bill Gates, Capricorn, Schmidt Futures |
| **Salience Labs** | Multi-chip wavelength-multiplexed photonic | Series A | Cambridge Innovation Capital |
| **PsiQuantum** | Photonic quantum computer | $665M raised | BlackRock, Microsoft, Temasek |

Photonic computing TAM est. $1B (2026) → $8-10B (2030); commercial inference deployment crosses threshold ~2027. Implication: Lumentum CW lasers + InP photodiodes + IQE epi-wafers feed photonic AI accelerator manufacturing — same chokepoint suppliers, parallel revenue stream.

**2. Quantum networking and photonic quantum compute.**

| Company | Application | Tech basis |
|---|---|---|
| **PsiQuantum** | Photonic quantum compute | SOI silicon photonics + InP single-photon sources |
| **Xanadu** | Photonic quantum processor | TFLN modulators + InGaAs photodetectors |
| **Q-CTRL** | Quantum control software | Hardware-agnostic |
| **IonQ** | Trapped-ion (photonic readout) | InP / TFLN read-out optics |
| **Quantum Computing Inc** | TFLN fabrication for photonic quantum | TFLN process |
| **PsiQuantum (DARPA quantum)** | Defense quantum networking | InP single-photon sources |

Quantum networking is 5-10 year horizon but increases InP and TFLN demand at low volume / high margin. PsiQuantum's $1B+ committed funding signals long-tail demand for InP single-photon emitters — a Lumentum / IQE adjacent revenue line. China's MICIUS satellite (quantum key distribution) drove parallel research at CAS Shanghai, NTNU.

**3. LiDAR and 3D sensing.**

| Application | Volume drivers | III-V dependency |
|---|---|---|
| **Automotive LiDAR** | L4 robotaxi (Waymo, Cruise, Pony.ai) + L2+ ADAS | 905nm and 1550nm InGaAs |
| **Industrial LiDAR** | Robotics, warehouse automation | InGaAs |
| **Consumer 3D sensing** | Apple Face ID + AR glasses + Meta/Apple Vision Pro | GaAs VCSELs (Lumentum/Coherent + IQE epi) |
| **Drone / aerospace LiDAR** | Defense ISR, drone delivery (Zipline, Wing) | InGaAs + GaAs |

VCSEL TAM ~$1.5B (2025) → ~$2.5B (2030). Apple's Vision Pro 2026 generation refresh and Meta's Orion glasses both expand 3D sensing optic content per device. Coherent supplies Apple VCSELs (took share from Lumentum); IQE supplies VCSEL epi for both.

**4. Free-space optical (FSO) and satellite optical.**

| Application | Lead players | Optical content |
|---|---|---|
| **Inter-satellite links (ISL)** | Mynaric, Tesat-Spacecom, BridgeComm, Cailabs | Coherent terminals; gimbal-mounted lasers; Lumentum + Coherent components |
| **Starlink ISL** | SpaceX (laser ISL on Gen2 satellites) | Internal + commercial supply |
| **Project Kuiper** | Amazon (laser ISL planned) | Commercial supply |
| **Direct-to-cell (Starlink, AST Mobile)** | Various | Optical backhaul to gateway stations |
| **Defense FSO (Space Development Agency)** | Mynaric, Tesat, General Atomics | DARPA + SDA Tranche 1/2/3 contracts |

ISL optical terminal market est. $400M (2026) → $2-3B (2030) on SDA Tranche 3 + Starlink Gen3 + Kuiper deployment. Mynaric stock +1,200% from 2024 lows on Tranche 2 awards.

**5. AR/VR and waveguide displays.** GaN microLED epiwafers (IQE-Porotech partnership; 8-inch GaN-on-Si foundry with unnamed consumer multinational). Apple Vision Pro / Meta Orion successor generations + AR glasses (Snap Spectacles, Google AR initiatives) create incremental microLED demand. III-V epi house customer diversification.

**6. Defense / aerospace optical.** GaN RF (radar, electronic warfare, satellite comms) demands sovereign US/UK supply. UK CSconnected Defence & Security Cluster (March 2026 launch, IQE anchor); Wales Investment Zone £160M; US CHIPS Act $10.3M IntelliEPI; AFRL/DARPA programs. Higher margin than commercial (defense CAGR ~8% vs commercial 25-30% in volume cycles, but counter-cyclical and stickier). Coherent/IPG/Lumentum/IQE all have defense exposure; II-VI legacy CO2 laser optics for materials processing also defense-adjacent.

**7. Optical biosensing and medical.** Photonic biosensors (Genalyte, Imec spin-outs), DNA sequencing optics (Illumina, PacBio, Ultima Genomics), surgical laser systems (Coherent legacy), retinal imaging (Lumentum). Smaller TAM (~$2B optical content) but high-margin and counter-cyclical.

**Cross-vertical observation:** the same Western III-V epitaxy chokepoint (IQE + Coherent + Win Semi + LandMark + IntelliEPI + VPEC) supplies datacom optics, automotive LiDAR, AR/VR microLED, defense GaN RF, optical AI compute, quantum networking, and ISL terminals. Aggregate demand from these adjacent verticals could 2-3x the III-V epitaxy TAM through 2030 — IQE's ~£525M market cap captures a fraction of optionality across these verticals. This is the deeper structural reason behind takeover offer interest.

## Related Research
- [[Research/2026-04-15 - LITE COHR - Lumentum vs Coherent Analysis]] — "Great Photonic Divergence" LITE +1,098% vs COHR +328%; pure-play vs integrated value capture; 70.5% Cloud Light module-level gross margin
- [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]] — CPO adoption timeline, NVIDIA $4B dual-investment intervention, OCS market dynamics, photonics investment outcomes
- [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]] — SiPh supply chain architecture for post-copper era; tiered investment framework
- [[Research/2025-11-25 - LITE - Silicon Photonics Supply Chain]] — Full SiPh supply chain mapping: design, fabrication, packaging, testing, transceivers, systems
- [[Research/2026-03-09 - Photonics and CPO Investment Outlook]] — X-sourced photonics investment perspectives; CPO yield dynamics; company-level positioning; IQE takeover speculation
- [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]] — LITE/COHR CPO transition; "arms dealer" component-level positioning; Broadcom/NVIDIA vertical integration advantage; InP CW lasers as critical CPO bottleneck
- [[Research/2026-03-02 - Chinese Silicon Photonics Threat]] — Chinese supply chain competitive analysis; 3% InP localization at 25G+; trade policy impact; Moolenaar-Krishnamoorthi Congressional letter
- [[Research/2025-11-25 - LITE - Silicon Photonics Supply Chain]] — Full SiPh supply chain for 2026-2030 era

## Log
### 2026-04-22
- Initial sector note created via subsector split from [[_Archive/Sectors/Semiconductors]] — pending prompt-fill of sector analysis sections.
- Reordered sections: Active Theses moved to first position per Sector Template / CLAUDE.md §Sector Notes (MOC navigation goes first).
- Sector populated: 7 analytical sections + Active Theses + Related Research filled via web-primary research (optical networking history 1960-2026 from Maiman's ruby laser / JDSU-Nortel telecom bubble / II-VI + Coherent Inc merger 2022 / Lumentum spinoff 2015; AAOI $1B FY26 revenue guidance with $200M 1.6T + $124M 800G hyperscaler orders; Fabrinet $5.39B FY26E / 28% NVDA / 2M sq ft expansion; Innolight ~40% 800G / 50-60% 1.6T share / Western EML + DSP dependency; GlobalFoundries-AMF Nov 2025 largest pure-play SiPh foundry; TSMC COUPE Feb 2026 risk prod with AMD; Lumentum Marvell R300 OCS OFC 2026 demo; LightCounting $26B 2026 Ethernet AI optics / 63M 800G / 22M 1.6T units; HyperLight-UMC-Wavetek TFLN March 2026; Goldman +58% 1.6T revision; 75.9% EML market share top-5; Coherent 6-inch InP 80% complete; NVIDIA $2B dual investments March 2026; Jim Anderson Coherent CEO turnaround) and vault-secondary references to 7 LITE/IQE research notes. Status: draft → active.

### 2026-04-28
- Manual enhancement: deepened sector note across seven dimensions. Added (a) Phase 7 — 2026-2030 forward outlook (1.6T mainstream 2027, 3.2T pilots 2028, 6.4T CPO-only 2029-2030, fab buildout completion timelines, Chinese 200G EML localization milestones); (b) Technology primitives section — 6-architecture modulator comparison table (DML / EML / MZM / TFLN / EOP / Ring resonator), modulation formats (NRZ / PAM4 / PAM6 / QAM / OOK), wavelength assignments (850nm / O-band / C-band / CWDM4 / LAN-WDM), reach categories (AOC / SR / DR / FR / LR / ZR with power draw at 800G), speed-generation timeline + ASP curve table from 100G→6.4T; (c) hyperscaler deployment matrix — Microsoft / AWS / Meta / Google / Oracle / CoreWeave-Crusoe-Nebius / Tencent-Alibaba-Baidu-ByteDance with capex, 800G + 1.6T state, CPO posture, optical strategy; (d) materials concentration detail — indium / gallium / germanium / phosphorus / lithium niobate / rare earths with China share + non-China sources + spot price trajectory + InP wafer pricing + indium criticality math (33 metric tons demand from 1.6T ramp); (e) 4 additional non-consensus framings (#9 Coherent Anderson Lattice playbook, #10 optical test bottleneck Aehr/FormFactor/Teradyne/MKS, #11 telecom optical re-investment 2027-2030 wave, #12 memory-wall to interconnect-wall thesis rotation); (f) cross-cycle valuation context (2000 telecom bubble $550B sector cap vs 2026 ~$400-500B; supply-constrained vs demand-speculative asymmetry caps downside); (g) Adjacent applications section — optical AI compute (Lightmatter/Lightelligence), quantum networking (PsiQuantum/Xanadu), LiDAR + 3D sensing (Apple Vision Pro/automotive), free-space optical/ISL (Mynaric/Tesat/Starlink/Kuiper), AR/VR microLED (IQE-Porotech), defense/aerospace, biosensing/medical — same Western III-V chokepoint suppliers across verticals. No content removed; all additions are analytical depth on existing themes.
- Addressed user callouts: 3 fresh callouts (2 in §Technology primitives, 1 in §Investor heuristics #10) addressed in single pass. (1) MZM material correction — split MZM row into MZM-SiPh and MZM-InP, renamed TFLN row to clarify MZM-topology relationship; added 4-material breakdown (SiPh / InP / TFLN / bulk LiNbO3) with EO-coefficient physics + 3-path CPO modulator analysis (MZM-SiPh dominant ~95%, MRM/Ayar Labs niche, TFLN-MZM future at 3.2T+). (2) Listed-company → architecture mapping table added — 8 architectures × tickers/products/stack-position; key takeaway: LITE/COHR DML+EML "arms-dealer" exposure to entire MZM-SiPh CPO buildout; MZM-InP captured via CIEN/NTT/Fujitsu (telecom optical cycle hedge); TFLN/EOP pre-revenue (QUBT/LWLG); Ayar Labs (private) holds MRM. (3) Optical test equipment deep-dive added as new §Product level analysis subsection — 9-vendor table (AEHR, FORM, TER, MKSI, KEYS, Anritsu, VIAV, EXFO, captive LITE/COHR) + 5 investment dynamics; AEHR identified as highest-asymmetry pure-play (<$1B mkt cap, 4-5x rev scenario at 30% photonic burn-in penetration, structurally non-consensus given thin sell-side coverage). No conviction or status changes; analytical depth only.
