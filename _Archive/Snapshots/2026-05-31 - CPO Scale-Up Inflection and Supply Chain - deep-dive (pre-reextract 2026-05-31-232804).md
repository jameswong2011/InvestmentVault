---
date: 2026-05-31
tags: [research, optical-networking, photonics, CPO, advanced-packaging, NVDA, AVGO, TSM, MRVL, LITE]
sector: Optical Networking & Photonics
source: 'https://substack.com/home/post/p-178153689 (SemiAnalysis / Dylan Patel — "Co-Packaged Optics (CPO) Book: Scaling with Light for the Next Wave of Interconnect", published 2026-01-02; clipped to _Inbox 2026-05-31)'
source_type: deep-dive
propagated_to: [NVDA, AVGO, TSM, MRVL, LITE, SIVE, AMD, BESI, IQE, AIXA, AAOI, TER, 6857, FORM, INTC]
---

# CPO Scale-Up Inflection and Supply Chain

## Thesis Delta

CPO's investable inflection is **scale-up, not the scale-out switches getting all the attention**: scale-out CPO delivers only 2–4% total-cluster power and 3–7% total-cluster cost savings (networking is 9% of cluster power), so Nvidia's 2025–26 Quantum-X/Spectrum-X launch (~10–15k units in 2026) is a supply-chain pipe-cleaner — while the real TAM, already larger than scale-out, lands later-decade in scale-up and is quantified for the first time by [[Theses/MRVL - Marvell Technology]]/Celestial AI's $1B-run-rate-by-CY2028 ramp into AWS Trainium 4. Value capture concentrates at the **TSMC COUPE packaging chokepoint** ([[Theses/TSM - Taiwan Semiconductor]]) and the external-laser layer ([[Theses/LITE - Lumentum]], [[Theses/SIVE - Sivers Semiconductors]]), not at the switch box.

## Summary

The piece reframes the CPO investment debate the market is having backwards. The headline products — Nvidia's GTC 2025 Quantum-X and Spectrum-X co-packaged **scale-out** switches — are explicitly modeled as a low-volume "practice run and pipe-cleaner": at a 3-layer InfiniBand network, switching a GB300 NVL72 cluster from DSP transceivers to CPO cuts networking power 23% but total cluster power only 2%, and networking cost 31% but total cluster cost only 3%. Flattening to two layers (enabled by the switches' high port radix) stretches this to 4% power / 7% cost — still diluted because networking is just 9% of cluster power and ~15–18% of cluster cost. Against that thin benefit sit real customer objections: loss of multi-vendor transceiver bargaining power, field-serviceability friction (a failed soldered optical engine can brick a switch; FAU replacement means going inside the chassis), and reliability anxiety on an immature supply chain. Hence "not if and why, but when and how."

The actual prize is **scale-up**. Copper scale-up (NVLink: 7.2 Tbit/s/GPU on Blackwell, 14.4 on Rubin via bi-directional SerDes) is hitting a 2-meter reach wall and a SerDes-doubling grind, capping scale-up "world size" to one or two racks and forcing Nvidia into extreme rack densities (Kyber: 144 GPU packages, 4× GB200 NVL72 density). CPO removes the reach constraint, letting world size grow across racks, and offers four independent bandwidth-scaling vectors (fibers, baud, modulation order, WDM) versus copper's single grinding vector (SerDes speed). Scale-up bandwidth per GPU is ~9× scale-out, so the article asserts scale-up CPO TAM **already dwarfs scale-out** — and SerDes plateau is framed as a direct risk to Nvidia's NVLink moat, an opening for [[Theses/AMD - Advanced Micro Devices]] and hyperscaler scale-up fabrics.

Value capture migrates to **TSMC COUPE** as the integration option of choice. COUPE's bumpless SoIC hybrid bond delivers >23× the bandwidth density of a bumped optical engine at iso-power, and TSMC is the only foundry running die-to-wafer hybrid bonding at volume (proven on AMD parts). The tell: [[Theses/AVGO - Broadcom]] — the most CPO-experienced vendor, with 50k+ Bailly switches shipped — is abandoning its own SPIL fan-out (FOWLP) approach (capped at ~100G/lane by through-mold-via parasitics) and moving its future roadmap to COUPE, forcing it to "start fresh" on grating coupling + micro-ring modulators versus its incumbent edge-coupling + Mach-Zehnder design. TSMC winning a domain where it was historically weak (GlobalFoundries/Tower led SiPho) is the single biggest competitive-dynamics datapoint here, and it locks customers into TSMC-fabbed PICs (TSMC won't package others' SiPho wafers).

The balanced read: CPO reliability evidence remains thin. The Meta/Broadcom ECOC 2025 study — cited everywhere as proof — covers just 15 Bailly switches for ~11 months in a lab (the "15M hours" figure is 400G *port*-device-hours ≈ 325 wall-clock days), shows 2.6M-hour MTBF for CPO vs 0.5–1M for 400G 2xFR4 pluggables, and zero uncorrectable codewords to 4M port-device-hours, but the author explicitly calls for far larger field testing before billions are committed. Interoperability is "wild west" (no IEEE/OIF/MSA equivalent yet; vendors push system-level lock-in), and Google — Broadcom's largest ASIC customer — refuses CPO on reliability grounds. The investable conclusions concentrate in the supply chain: external-laser sources (Lumentum sole-source for Nvidia's first batches, Coherent second in late 2026; Sivers supplies Ayar Labs), advanced packaging (TSMC COUPE, hybrid bonding → [[Theses/BESI - BE Semiconductor Industries]]), E/O test (Teradyne, Advantest, FormFactor all named), and III-V epitaxy for the laser bottleneck ([[Theses/IQE - IQE]], [[Theses/AIXA - Aixtron]]).

## Framework / Mental Model

The source advances several reusable analytical frameworks for evaluating any interconnect technology:

**1. Figure of merit: "use copper where you can, optical when you must."** The objective quality of an interconnect = bandwidth density per area per energy consumed, plotted against reach. This FoM degrades exponentially for electrical links as distance rises, and drops ~an order of magnitude when crossing from pure-electrical to optical-electrical conversion (the cost of driving the front-panel SerDes + powering the optical DSP). The CPO FoM curve sits squarely above pluggables over the same reach because it eliminates the long electrical trace and the DSP. Decision rule: copper wins at short reach where available; optical becomes mandatory once the FoM curve crosses — and CPO shifts where that crossover sits.

**2. The four vectors for scaling optical bandwidth.** Total fiber escape bandwidth = (number of fiber pairs) × (speed per lane) × (wavelengths per fiber). This decomposes into four independent scaling levers, versus copper's single lever (SerDes speed):
- **More fiber pairs** — limited by fiber pitch (127µm today → 80µm / multicore target) and FAU yield, which degrades with each fiber aligned.
- **Baud rate** — symbols/sec; 100 Gbaud today → 200 Gbaud target; stresses the modulator's switching speed.
- **Modulation order** — bits/symbol; NRZ (1) → PAM4 (2) → PAM6 (~2.58) / PAM8 (3); DP-16QAM (8) for coherent.
- **WDM** — wavelengths/fiber; 8λ/16λ commercial → 64λ/128λ roadmap; the densest lever, gated by multi-wavelength laser reliability.

**3. Fast-and-Narrow vs Slow-and-Wide.** Two opposing port-architecture philosophies for a target aggregate bandwidth: *Fast-and-Narrow* (few fibers, high speed per fiber) minimizes FAU complexity but maxes modulator/SerDes difficulty; *Slow-and-Wide* (many fine-pitch fibers, low speed each) eases the electrical/optical speed requirement but maxes fiber-attach/yield difficulty. Each CPO vendor's choice on this axis predicts its supply-chain dependencies.

**4. Modulator typology — MZM vs MRM vs EAM.** Each wavelength needs one modulator; the choice trades size, thermal sensitivity, power, and WDM-nativeness:

| Modulator | Size | Thermal sensitivity | WDM-native | Power | Champion |
|---|---|---|---|---|---|
| **MZM** (Mach-Zehnder) | ~12,000 µm² (mm-scale length) | Low | No | High (large voltage swing) | Nubis; Broadcom (legacy) |
| **MRM** (micro-ring) | 25–225 µm² | Very high (70–90 pm/°C; collapses at 0.1nm shift) | Yes (built-in mux) | Low (sub-volt) | Nvidia, Ayar, Lightmatter, Ranovus, TSMC COUPE PDK |
| **EAM** (electro-absorption, GeSi) | ~250 µm² | Moderate (tolerates ~35°C instantaneous) | No (needs external mux) | Low | Celestial AI (only major adopter) |

**5. The packaging ladder (reach-shortening continuum).** Pluggable transceiver (15–30cm electrical trace + DSP) → On-Board Optics (OBO, "worst of both worlds") → Near-Packaged Optics (NPO, socketable OE on separate substrate) → Co-Packaged Copper (CPC, twinax off substrate — a parallel path that could enable 448G SerDes) → CPO on substrate → CPO on interposer (endgame, ~4 Tbit/s/mm). Each rung shortens the electrical path, raising the FoM but raising packaging complexity and lowering serviceability.

## Evidence

**Scale-out CPO TCO/power dilution (vs DSP transceivers, GB300 NVL72):**

| Metric | 3-layer network | 2-layer network |
|---|---|---|
| Transceiver power reduction | −84% | −84% |
| Networking power reduction | −23% | −48% |
| **Total cluster power savings** | **−2%** | **−4%** |
| Total networking cost reduction | −31% | −46% |
| **Total cluster cost savings** | **−3%** | **−7%** |

Context: back-end fabric = 85% of networking cost, 86% of networking power (3-layer GB300 NVL72 on InfiniBand). Transceivers = 60% of networking cost, 45% of networking power (3-layer). Networking ≈ 9% of total cluster power; 15% (3-layer) to 18% (4-layer) of total cluster cost.

**Per-800G power, pluggable vs CPO:**

| Source | Pluggable | CPO (OE + ELS) | Savings |
|---|---|---|---|
| SemiAnalysis (Nvidia Q3450) | 16–17W (800G DR4) | 4–5W | 73% |
| Meta/Broadcom Bailly (ECOC 2025) | 15W (800G 2xFR4) | 5.4W | 65% |

**Optical-engine cost (Nvidia X800-Q3450), CPO vs transceiver:**

| | CPO | Transceiver |
|---|---|---|
| Hardware BOM | $35–40k (36× 3.2T OE @ ~$1,000 incl. FAU) | $72k (72× 1.6T twin-port @ ~$1,000) |
| **To end-buyer (60% GM markup on CPO)** | **$80–90k** | ~$72k |

The margin stack on co-packaged components can make CPO *more* expensive to the buyer than transceivers — a core reason scale-out adoption is slow.

**Reliability (Meta/Broadcom Bailly 51.2T, ECOC 2025):** 1,049k → up to 15M 400G port-device-hours across 15 switches; zero UCWs to 4M port-device-hours; 1 instance of FEC bin >10; CPO MTBF 2.6M device-hours vs 400G 2xFR4 0.5–1M (550k globally); 0.06% unserviceable failure rate, blast radius 64× 800G ports. Caveat: 15M port-device-hours ≈ 325 wall-clock days in a lab — author flags as insufficient for billion-dollar commitment.

**Marvell / Celestial AI — first quantified scale-up CPO ramp:**

| Milestone | Figure |
|---|---|
| Revenue run-rate exiting FY28 (Jan 2028) | $500M |
| Run-rate by end CY2028 | $1B |
| Earn-out trigger | $2.25B payout on $2.0B cumulative revenue by Jan 2029 |
| First payout third | $500M cumulative by Jan 2029 |
| Amazon warrant strike (→ Trainium 4 tell) | $87.0029, vesting on PF purchases through Dec 31 2030 |
| PF Chiplet bandwidth | Gen1 16T → Gen2 64T |
| Link efficiency | ~2.5 pJ/bit (E-O-E) + ~0.7 pJ/bit laser vs ~10 pJ/bit copper |

**Nvidia CPO product specs:**

| Switch | Aggregate | OE config | Modulator | Notes |
|---|---|---|---|---|
| Quantum X800-Q3450 (2H25) | 115.2T | 72× 1.6T OE (8ch × 200G) | 8 MRM @ 200G PAM4/OE | 4× 28.8T ASIC; 144 MPO ports; PIC N65 + EIC N6, COUPE hybrid bond; **200G MRM in production disproves NRZ-only notion** |
| Spectrum-X 6810 (2H26) | 102.4T | 36× 3.2T OE (16 lanes × 200G) | MRM | 32 active + 4 redundant (soldered, non-replaceable) |
| Spectrum-X 6800 (2H26) | 409.6T | 4× MCM | MRM | 224G SerDes I/O chiplets, 12.8T each |

**Broadcom CPO generations:** Humboldt 25.6T (half copper/half optics; 4× 3.2T OE @ 32×100G; SiGe EIC) → Bailly 51.2T (8× 6.4T OE @ 64×100G; 7nm CMOS EIC; FOWLP/SPIL; 50k+ shipped) → Davisson TH6 102.4T (16× 6.4T OE; N3) → future roadmap on TSMC COUPE.

**External Laser Source (Nvidia Q3450):** 18 ELS modules × 8 CW DFB chips; ~350mW/chip; each laser provides 24.5 dBm to cover losses; lasers + TECs ≈ 70% of ELS power. Suppliers: **Lumentum (sole, initial batches)**, Coherent (2nd, late 2026), Furukawa, Broadcom; Chinese (Yuanjie, Shijia) longer-term commoditization threat — "still somewhat of a moat" on high-power.

**Nvidia CPO supply chain → listed exposure:**

| Component | Key suppliers | Listed tickers in vault |
|---|---|---|
| External laser source | Lumentum, Coherent, Furukawa, Broadcom | [[Theses/LITE - Lumentum]], [[Theses/AVGO - Broadcom]] |
| Laser supply (Ayar SuperNova) | Sivers (via Ayar) | [[Theses/SIVE - Sivers Semiconductors]] |
| III-V / InP epitaxy + MOCVD | IQE, Aixtron | [[Theses/IQE - IQE]], [[Theses/AIXA - Aixtron]] |
| OE foundry / packaging | TSMC COUPE; hybrid-bond tools | [[Theses/TSM - Taiwan Semiconductor]], [[Theses/BESI - BE Semiconductor Industries]] |
| OSAT (OE + system assembly) | ASE/SPIL (3711.TW), Amkor, Shunsin, Fabrinet, Foxconn | (AMKR, FN — no thesis) |
| FAU | TFC (300394.SH), Senko (9069.JP), FOCI (3363.TW), Sumitomo, AFR | (no thesis) |
| Coupling / FAU machines | Ficontec (>$300k/unit), All Ring Tech, GMT Global | (no thesis) |
| Shuffle box / MPO / MT ferrule | T&S (300570.SH), Corning, Molex, US Conec | (GLW — no thesis) |
| E/O test equipment | Keysight, Ficontec, **Teradyne, Advantest, FormFactor**, Chroma, Anritsu, Multilane | [[Theses/TER - Teradyne]], [[Theses/6857 - Advantest]], [[Theses/FORM - FormFactor]] |

## Key Segments

### Part 1 — TCO Analysis (scale-out diluted, scale-up the killer app)
Models the cost/power of co-packaging for scale-out and finds the benefit swamped by the server's dominant share of cluster TCO (tables above). The high-radix "shuffle-in-a-box" (Quantum 3450 = 144× 800G; Spectrum 6800 = 512× 800G) lets customers flatten 3-layer to 2-layer networks (host count scales with port-count^layers), the genuine selling point. Conclusion: limited scale-out adoption near-term; scale-up is the killer application because copper's 2m reach caps world size and scale-up bandwidth (9× scale-out per GPU) makes its CPO TAM larger.

### Part 2 — Why CPO now: SerDes plateau and Wide I/O
DSP is "public enemy #1": ~50% of an 800G SR8 module's power, 20–30% of BoM. The disintermediation ladder is LPO (failed to take off) → CPO (kills the DSP by shortening reach to mm). I/O has scaled far slower than FLOPs; off-package bandwidth is bump-count-limited. SerDes is plateauing — 224G was hard; true 448G uni-directional is uncertain (Nvidia uses bi-directional SerDes in Rubin as the workaround). NVLink's 11× gain (1.0→5.0) came almost entirely from 10× SerDes speed (20G→200G), not lane count — so the plateau directly threatens Nvidia's scale-up moat. Wide I/O (UCIe-A ~10 Tbit/s/mm vs Blackwell's ~0.4) is the escape, and CPO's already-advanced package makes wide-I/O integration "almost free." Co-packaged copper (CPC) is flagged as the simpler parallel path that may actually deliver 448G.

### Part 3 — Bringing CPO to market: COUPE, coupling, modulators, scaling
Heterogeneous integration (SiPho PIC + CMOS EIC) beats monolithic (capped at ~35nm, why Ayar is leaving GF for COUPE). TSMC COUPE detailed: EIC N7 + PIC SOI N65, SoIC bumpless bond = 23× bandwidth density vs bumps; supports both grating (Si-lens + metal reflector) and edge coupling; roadmap substrate → interposer (12.8T/OE). Coupling: edge (low loss, 1D, no die-stacking) vs grating (2D multi-row density, interposer-compatible, polarization-sensitive — Nvidia + TSMC prefer it). Lasers: on-chip (failure-prone, heat-sensitive) lost to External Light Source consensus (pluggable, serviceable). Modulator typology (MZM/MRM/EAM table above). Bandwidth-scaling vectors and Fast-Narrow vs Slow-Wide frameworks introduced here.

### Part 4 — Products of today and tomorrow
**Nvidia** (MRM 200G in production — key milestone), **Broadcom** (Bailly→COUPE pivot), **[[Theses/INTC - Intel]]** (4-stage roadmap: OCI chiplet 4T bidir @ ~5pJ/bit 2024 → glass optical bridge 2025 → 3D vertical coupling 2027), **MediaTek** (NPC→CPC→CPO by data-rate). The seven CPO-focused names: **Ayar Labs** (TeraPHY UCIe optical retimer; gen2 4T "Eagle" w/ Sivers SuperNova laser; gen3 13.5T on COUPE, 108T/package w/ Alchip/GUC; backed by Nvidia, AMD, TSMC, GF, Intel, Applied Materials), **Nubis** (acquired by Ciena Oct 2025; MZM, densest 2D FAU @ 36 fibers; Samtec 6.4T snap-in; Nitro ACC redriver w/ Amphenol), **Celestial AI** (EAM + optical interposer/Photonic Fabric; Trainium 4; memory appliance with center-of-die optical I/O — a [[Macro & Technology/CXL Memory Disaggregation Framework|memory-disaggregation]] adjacency), **Lightmatter** (Passage M1000 4,000mm² interposer, 114T, 1,024× 112G SerDes, GUIDE VLSP laser), **Xscape** (ChromX programmable 4–128λ laser, single fiber), **Ranovus** (Odin MRM, Ethernet-interoperable, AMD + MediaTek), **Scintil** (LEAF Light wafer-level III-V-on-SiPho DWDM laser).

### Part 5 — Nvidia's CPO supply chain
Component-by-component BOM and supplier map (table above). E/O test is an emerging, un-standardized battleground — Teradyne is "very serious" and acquired a packaged-optical-test startup; Advantest, FormFactor, Keysight, Ficontec, Chroma all positioning. FAU testing is still ~10–15 min/unit manual labor (Corning estimate). Lumentum sole ELS for first batches.

## Contradiction Check

- **Supports [[Theses/TSM - Taiwan Semiconductor]] (advanced-packaging value capture):** strengthens the COUPE-as-chokepoint case; Broadcom's forced migration to COUPE + customer lock-in to TSMC PICs is new evidence TSMC extends packaging dominance into optics. Affects the assumption that CPO value disperses across SiPho foundries — this argues it concentrates at TSMC.
- **Supports but qualifies [[Theses/LITE - Lumentum]] / [[Theses/SIVE - Sivers Semiconductors]] (ELS exposure):** confirms Lumentum as Nvidia's sole initial ELS supplier and Sivers as Ayar's laser source. But challenges the durability assumption — the article calls CW DFB lasers "relatively standardized and commoditized," with Chinese vendors (Yuanjie, Shijia) as a forward threat. ELS is a more contestable layer than the 200G EML monopoly the [[Sectors/Optical Networking & Photonics]] note anchors on.
- **Risk flag for [[Theses/NVDA - Nvidia]] (NVLink moat):** SerDes plateau as the explicit mechanism by which AMD/hyperscalers close the scale-up gap is a bear datapoint for the NVLink-fabric moat — partially offset by Nvidia's own 200G-MRM CPO lead and Kyber density.
- **Supports [[Theses/MRVL - Marvell Technology]] but execution-gated:** Celestial AI gives Marvell the first quantified scale-up CPO revenue path ($1B run-rate CY2028, Trainium 4), but on a unique EAM modulator that lacks TSMC COUPE PDK support (Marvell must integrate EAM into a foundry itself) and a 2-year-to-viability timeline.
- **Displacement risk for [[Theses/AAOI - Applied Optoelectronics]] and merchant module makers:** CPO erodes bleeding-edge pluggable TAM by 2027–28 — but the slow scale-out adoption curve and serviceability friction mean the pluggable runway is longer than CPO bulls assume.
- **Net-new for [[Theses/TER - Teradyne]] / [[Theses/6857 - Advantest]] / [[Theses/FORM - FormFactor]]:** E/O photonic test as an un-standardized, emerging TAM with all three named — not yet a sizing in their theses.
- **Tangential to [[Theses/BESI - BE Semiconductor Industries]]:** TSMC SoIC die-to-wafer hybrid bonding is the performance-critical CPO bond; reinforces hybrid-bonding tool demand, though the article credits TSMC's internal capability rather than naming merchant tool vendors.

## Source Excerpts

> "CPO will be the main driver of bandwidth increases in scale-up networking for the latter part of this decade and beyond."

> "Switching to use CPO for a three-layer network lowers networking power by 23% but only delivers 2% total cluster power savings. Moving to a two-layer network delivers 48% lower networking [power], but only 4% total cluster power savings."

> "At iso-power, SoIC based OEs offer more than 23x the bandwidth density of an OE integrated with bumps." (TSMC)

> "We do not expect Google to adopt CPO any time soon." — Google's reliability-first philosophy makes CPO "a deal breaker."

> Celestial/Marvell: "$1B by the end of Calendar Year 2028 ... an additional $2.25B of payout to Celestial AI's equity holders is contingent upon the company achieving a cumulative revenue of at least $2.0 billion by January 2029."

> "Nvidia's scale-out CPO product launch is serving as a practice run and pipe-cleaner for the real high-volume deployment ... far more sizable and impactful for scale up."
