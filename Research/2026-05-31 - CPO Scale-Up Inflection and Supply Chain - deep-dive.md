---
publish: false
date: 2026-05-31
tags: [research, optical-networking, photonics, CPO, advanced-packaging, NVDA, AVGO, TSM, MRVL, LITE]
sector: Optical Networking & Photonics
source: 'https://substack.com/home/post/p-178153689 (SemiAnalysis / Dylan Patel — "Co-Packaged Optics (CPO) Book: Scaling with Light for the Next Wave of Interconnect", published 2026-01-02; clipped to _Inbox 2026-05-31)'
source_type: deep-dive
propagated_to: [NVDA, AVGO, TSM, MRVL, LITE, SIVE, AMD, BESI, IQE, AIXA, AAOI, TER, 6857, FORM, INTC]
---

<!-- Body re-extracted 2026-05-31 from the preserved raw source (_Inbox/processed/) under /ingest's revised retention curve (check #5, Generous: ~25k source words → ~7k body). Original ingest under-extracted (~3k words) due to the flat-floor bug fixed 2026-05-31. Thesis Delta + Contradiction Check preserved verbatim — already propagated via /sync 2026-05-31, so claims must not drift. Pre-reextract snapshot: [[_Archive/Snapshots/2026-05-31 - CPO Scale-Up Inflection and Supply Chain - deep-dive (pre-reextract 2026-05-31-232804)]] -->

# CPO Scale-Up Inflection and Supply Chain

## Thesis Delta

CPO's investable inflection is **scale-up, not the scale-out switches getting all the attention**: scale-out CPO delivers only 2–4% total-cluster power and 3–7% total-cluster cost savings (networking is 9% of cluster power), so Nvidia's 2025–26 Quantum-X/Spectrum-X launch (~10–15k units in 2026) is a supply-chain pipe-cleaner — while the real TAM, already larger than scale-out, lands later-decade in scale-up and is quantified for the first time by [[Theses/MRVL - Marvell Technology]]/Celestial AI's $1B-run-rate-by-CY2028 ramp into AWS Trainium 4. Value capture concentrates at the **TSMC COUPE packaging chokepoint** ([[Theses/TSM - Taiwan Semiconductor]]) and the external-laser layer ([[Theses/LITE - Lumentum]], [[Theses/SIVE - Sivers Semiconductors]]), not at the switch box.

## Summary

The piece reframes the CPO investment debate the market is having backwards. The headline products — Nvidia's GTC 2025 Quantum-X and Spectrum-X co-packaged **scale-out** switches — are explicitly modeled as a low-volume "practice run and pipe-cleaner." At a 3-layer InfiniBand network, switching a GB300 NVL72 cluster from DSP transceivers to CPO cuts networking power 23% but total cluster power only 2%, and networking cost 31% but total cluster cost only 3%. Flattening to two layers (enabled by the switches' high port radix) stretches this to 4% power / 7% cost — still diluted because networking is just 9% of cluster power and 15–18% of cluster cost. Against that thin benefit sit real customer objections: loss of multi-vendor transceiver bargaining power, field-serviceability friction (a failed soldered optical engine can brick a switch; FAU replacement means going inside the chassis), and reliability anxiety on an immature supply chain. Hence "not if and why, but when and how."

The actual prize is **scale-up**. Copper scale-up (NVLink: 7.2 Tbit/s/GPU on Blackwell, 14.4 on Rubin via bi-directional SerDes) is hitting a 2-meter reach wall and a SerDes-doubling grind, capping scale-up "world size" to one or two racks and forcing Nvidia into extreme rack densities (Kyber: 144 GPU packages / 576 dies, 4× GB200 NVL72 density). CPO removes the reach constraint, letting world size grow across racks, and offers four independent bandwidth-scaling vectors (fibers, baud, modulation order, WDM) versus copper's single grinding vector (SerDes speed). Scale-up bandwidth per GPU is ~9× scale-out (900 GByte/s vs 100 GByte/s), so the article asserts scale-up CPO TAM **already dwarfs scale-out** — and the SerDes plateau is framed as a direct risk to Nvidia's NVLink moat, an opening for [[Theses/AMD - Advanced Micro Devices]] and hyperscaler scale-up fabrics.

Value capture migrates to **TSMC COUPE** as the integration option of choice. COUPE's bumpless SoIC hybrid bond delivers >23× the bandwidth density of a bumped optical engine at iso-power, and TSMC is the only foundry running die-to-wafer hybrid bonding at volume (proven on AMD parts). The tell: [[Theses/AVGO - Broadcom]] — the most CPO-experienced vendor, with 50k+ Bailly switches shipped — is abandoning its own SPIL fan-out (FOWLP) approach (capped ~100G/lane by through-mold-via parasitics) and moving its future roadmap to COUPE, forced to "start fresh" on grating coupling + micro-ring modulators versus its incumbent edge-coupling + Mach-Zehnder design. TSMC winning a domain where it was historically weak (GlobalFoundries/Tower led SiPho) is the single biggest competitive-dynamics datapoint here, and it locks customers into TSMC-fabbed PICs (TSMC won't package others' SiPho wafers).

The balanced read: CPO reliability evidence remains thin. The Meta/Broadcom ECOC 2025 study — cited everywhere as proof — covers just 15 Bailly switches for ~11 months in a lab (the "15M hours" figure is 400G *port*-device-hours ≈ 325 wall-clock days), shows 2.6M-hour MTBF for CPO vs 0.5–1M for 400G 2xFR4 pluggables, and zero uncorrectable codewords to 4M port-device-hours, but the author explicitly calls for far larger field testing before billions are committed. Interoperability is "wild west" (no IEEE/OIF/MSA equivalent yet; vendors push system-level lock-in), and Google — Broadcom's largest ASIC customer — refuses CPO on reliability grounds. The investable conclusions concentrate in the supply chain: external-laser sources (Lumentum sole-source for Nvidia's first batches, Coherent second in late 2026), advanced packaging (TSMC COUPE, hybrid bonding → [[Theses/BESI - BE Semiconductor Industries]]), E/O test (Teradyne, Advantest, FormFactor all named), and III-V epitaxy for the laser bottleneck ([[Theses/IQE - IQE]], [[Theses/AIXA - Aixtron]]).

## Framework / Mental Model

The source advances several reusable analytical frameworks for evaluating any interconnect technology.

**1. Figure of merit: "use copper where you can, optical when you must."** The objective quality of an interconnect = bandwidth density per area per energy consumed, plotted against reach. This FoM degrades exponentially for electrical links as distance rises, and drops ~an order of magnitude when crossing from pure-electrical to optical-electrical conversion (the cost of driving the front-panel SerDes + powering the optical DSP). The CPO FoM curve sits squarely above pluggables over the same reach because it eliminates the long electrical trace and the DSP. Decision rule: copper wins at short reach where available; optical becomes mandatory once the FoM curve crosses — and CPO shifts where that crossover sits. Nvidia embodies the adage by architecting rack-scale GPU systems (GB200 NVL72, Kyber) solely to maximize the GPUs networkable over copper before optics becomes unavoidable.

**2. The four vectors for scaling optical bandwidth.** Total fiber escape bandwidth = (number of fiber pairs) × (speed per lane) × (wavelengths per fiber). This decomposes into four independent scaling levers, versus copper's single lever (SerDes speed):
- **More fiber pairs** — limited by fiber pitch (127µm today = max 8 fibers/mm → 80µm / multicore target) and FAU yield, which degrades with each fiber aligned (still a largely manual process; Ficontec automation suffers low throughput).
- **Baud rate** — symbols/sec; 100 Gbaud today → 200 Gbaud target; stresses the modulator's switching speed (MZM is the most capable here, with a clear path to 200 Gbaud).
- **Modulation order** — bits/symbol; NRZ (1) → PAM4 (2) → PAM6 (~2.58) / PAM8 (3); DP-16QAM (8) for coherent (256 possible signals across 4 amplitudes × 4 phases × 2 polarizations).
- **WDM** — wavelengths/fiber; 8λ/16λ commercial → 64λ (Xscape) / 128λ roadmap; the densest lever, gated by multi-wavelength laser reliability. MRMs handle WDM natively via per-ring tuning.

**3. Fast-and-Narrow vs Slow-and-Wide.** Two opposing port-architecture philosophies for a target aggregate bandwidth: *Fast-and-Narrow* (few fibers — high double-digits at most — high speed per fiber) minimizes FAU complexity but maxes modulator/SerDes difficulty; *Slow-and-Wide* (many fine-pitch fibers, low speed each) eases the electrical/optical speed requirement but maxes fiber-attach/yield difficulty. Each CPO vendor's choice on this axis predicts its supply-chain dependencies.

**4. Modulator typology — MZM vs MRM vs EAM.** Each wavelength needs one modulator; the choice trades size, thermal sensitivity, power, and WDM-nativeness:

| Modulator | Size | Thermal sensitivity | WDM-native | Power | Champion |
|---|---|---|---|---|---|
| **MZM** (Mach-Zehnder) | ~12,000 µm² (mm-scale length) | Low | No | High (large voltage swing, 0–5V) | Nubis; Broadcom (legacy) |
| **MRM** (micro-ring) | 25–225 µm² (5–15µm diameter) | Very high (70–90 pm/°C; collapses at 0.1nm shift = ~2°C) | Yes (built-in mux/demux) | Low (sub-volt) | Nvidia, Ayar, Lightmatter, Ranovus, TSMC COUPE PDK |
| **EAM** (electro-absorption, GeSi) | ~250 µm² (5×50µm) | Moderate (tolerates ~35°C instantaneous, ~80°C ambient) | No (needs external mux) | Low | Celestial AI (only major adopter) |

MZM is proven at 200G/lane (400G believed possible on non-coherent PAM) but its size caps modulator density. MRM is compact and WDM-native but 10–100× more temperature-sensitive (Franz-Keldysh-free resonance drift) and non-linear (complicates PAM4/6/8). EAM (GeSi, Franz-Keldysh effect) has better thermal stability than MRM and smaller footprint than MZM, but its band edge sits naturally in C-band (1530–1565nm) not O-band (1310nm) — making it hard to join an open O-band chiplet ecosystem — and it needs a separate multiplexer (4–5 dB insertion loss vs 3–5 dB for MRM/MZM).

The investment-relevant reads from this typology: (i) **MZM** — low thermal sensitivity + high linearity make it the safe, interoperable choice (Nubis) and the only modulator with a clear path to 200 Gbaud, but mm-scale length caps channel density and the 0–5V swing burns driver power. (ii) **MRM** — sub-volt drive + built-in WDM mux make it the density/power winner and the COUPE-PDK default, but 70–90 pm/°C drift (a 2°C shift blows past the 0.1nm collapse threshold) demands precision control circuits. Nvidia's specific edge is *controlling* MRMs; shipping 200G PAM4 MRMs in production disproves the industry's NRZ-only assumption. (iii) **EAM** — tolerates ~35°C instantaneous / ~80°C ambient swings, uniquely enabling Celestial's modulator-beneath-a-hot-XPU-interposer architecture, and Celestial argues GeSi reliability is a known quantity (an EAM is essentially a reversed photodetector); but the C-band band edge locks it out of the O-band open-chiplet ecosystem and off the COUPE PDK, so Marvell must self-integrate EAM into a foundry — the central execution gate.

**5. The packaging ladder (reach-shortening continuum).** Pluggable transceiver (15–30cm electrical trace + DSP) → On-Board Optics (OBO, "worst of both worlds": CPO complexity, pluggable limits) → Near-Packaged Optics (NPO, socketable OE on a separate substrate) → Co-Packaged Copper (CPC, twinax off substrate — a parallel path that could enable 448G SerDes) → CPO on substrate → CPO on interposer (endgame, up to 12.8 Tbit/s per OE, ~4 Tbit/s/mm). Each rung shortens the electrical path, raising the FoM but raising packaging complexity and lowering serviceability. PIC–EIC integration itself climbs a sub-ladder: monolithic (elegant but capped at ~35nm photonics geometry — why Ayar is leaving GF) → heterogeneous bump-bonded → heterogeneous hybrid-bonded (SoIC bumpless, 23× density, the performance endpoint).

## Evidence

**Scale-out CPO TCO/power dilution (vs DSP transceivers, GB300 NVL72):**

| Metric | 3-layer network | 2-layer network |
|---|---|---|
| Transceiver power reduction | −84% | −84% |
| Networking power reduction | −23% | −48% |
| **Total cluster power savings** | **−2%** | **−4%** |
| Total networking cost reduction | −31% | −46% |
| **Total cluster cost savings** | **−3%** | **−7%** |

Context: back-end fabric = 85% of networking cost, 86% of networking power (3-layer GB300 NVL72 on InfiniBand, X800-Q3400 switches). Transceivers = 60% of networking cost, 45% of networking power (3-layer). Networking ≈ 9% of total cluster power; 15% (3-layer) to 18% (4-layer) of total cluster cost. CPO switch costs rise 81% from the margin-stacked OE/ELS content, partially offsetting the 86% transceiver-cost elimination. A 200,000-GPU GB300 NVL72 cluster on a 3-layer network draws 435 MW critical IT power, of which 17 MW is transceivers alone.

**Host-count math (why flattening layers is the real selling point):** max hosts on an L-layer network with k-port switches = 2·(k/2)^L. Port count is exponentiated by layers — so doubling logical ports (slicing 800G into 2×400G via internal shuffle) quadruples hosts on a 2-layer network. Spectrum 6800 (512 ports of 800G) connects 131,072 GPUs on two layers; Spectrum 6810 (128 ports of 800G) connects 8,192. The CPO switch hides the shuffle inside the box (vs external patch panels / octopus cables), presenting high radix "by default."

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

**DSP as "public enemy #1":** ~50% of an 800G SR8 module's power, 20–30% of BoM. An 18k GB300 cluster (2-layer InfiniBand) needs 18,432 800G DR4 + 27,648 1.6T DR8 transceivers; budgeting 6–7W/800G DSP and 12–14W/1.6T DSP = 480 kW of DSP power for the back-end alone (~1.8 kW/rack). Disintermediation ladder: LPO (removes DSP, lets switch SerDes drive optics directly — failed to take off) → CPO (kills DSP by shortening reach to mm).

**Wide I/O vs SerDes:** UCIe-A offers ~10 Tbit/s/mm shoreline density (advanced package, <2mm reach) → up to 330 Tbit/s off a reticle edge; UCIe-S on substrate ~1.8 Tbit/s/mm. Blackwell's 224G SerDes delivers ~0.4 Tbit/s/mm (23.6 Tbit/s total off-package). CPO's already-advanced package makes wide-I/O integration "almost free." SerDes plateau: 224G was hard; true 448G uni-directional uncertain (PAM4 at 244 Gbaud likely untenable on power/loss; may need PAM6/8); Rubin uses bi-directional SerDes (224G Tx + 224G Rx shared channel) as the workaround.

**NVLink moat mechanism:** NVLink 5.0 bandwidth is 11× NVLink 1.0, but lane count rose only 32→36 — the gain came almost entirely from a 10× SerDes speed increase (20G→200G). NVLink 6.0 stays at 200G SerDes and doubles effective lanes via bi-directional SerDes. Beyond this, both SerDes speed and shoreline are constrained → escape bandwidth stalls. SemiAnalysis: "For Nvidia, whose NVLink scale up fabric is an important moat, this roadblock could make it easier for competitors such as AMD, and the hyperscalers to catch up."

**Reliability (Meta/Broadcom Bailly 51.2T, ECOC 2025):** 1,049k → up to 15M 400G port-device-hours across 15 switches; zero UCWs to 4M port-device-hours; one instance of FEC bin >10; CPO MTBF 2.6M device-hours vs 400G 2xFR4 0.5–1M (550k globally); 0.06% unserviceable failure rate, blast radius 64× 800G ports. Caveat: 15M port-device-hours = 7,812 wall-clock hours ≈ 325 days across 15 switches — author flags as insufficient for billion-dollar commitment; study used FR optics, next gen is DR. Pluggable failure context: a ~1M-link cluster sees dozens of link interruptions/day; 80% of returned modules are "no trouble found."

**Marvell / Celestial AI — first quantified scale-up CPO ramp:**

| Milestone | Figure |
|---|---|
| Revenue run-rate exiting FY28 (Jan 2028) | $500M |
| Run-rate by end CY2028 | $1B |
| Earn-out trigger | $2.25B payout on $2.0B cumulative revenue by Jan 2029 |
| First payout third | $500M cumulative by Jan 2029 |
| Amazon warrant strike (→ Trainium 4 tell) | $87.0029, vesting on PF purchases through Dec 31 2030 |
| PF Chiplet bandwidth | Gen1 16T → Gen2 64T |
| Link efficiency | ~2.5 pJ/bit (E-O-E) + ~0.7 pJ/bit laser vs ~10 pJ/bit copper (2×5 pJ/bit at 224G) |

Marvell's $1B run-rate is half the $2B earn-out target, implying Celestial must add customers beyond the anchor (Trainium 4) to hit the full payout. Implied product-viability window: ~2 years (to end-2027).

**Nvidia CPO product specs:**

| Switch | Aggregate | OE config | Modulator | Notes |
|---|---|---|---|---|
| Quantum X800-Q3450 (2H25) | 115.2T | 72× 1.6T OE (8ch × 200G) | 8 MRM @ 200G PAM4/OE | 4× 28.8T ASIC multi-plane; 144 MPO ports; PIC N65 + EIC N6, COUPE hybrid bond; 6 detachable sub-assemblies × 3 OE per ASIC; **200G MRM in production disproves NRZ-only notion**; max cluster 746,496 GPUs (3-layer) |
| Spectrum-X 6810 (2H26) | 102.4T | 36× 3.2T OE (16 lanes × 200G) | MRM | MCM: 102.4T ASIC + eight 224G SerDes I/O chiplets (12.8T each, 64 lanes, 4 OE each); 32 active + 4 redundant (soldered, non-replaceable); substrate 110×110mm |
| Spectrum-X 6800 (2H26) | 409.6T | 4× MCM | MRM | 4 Spectrum-6 MCMs in multi-plane internal breakout |

**Broadcom CPO generations:** Humboldt TH4 25.6T (half copper/half optics; 4× 3.2T OE @ 32×100G; SiGe EIC; proof of concept) → Bailly 51.2T (all-optical; 8× 6.4T OE @ 64×100G; 7nm CMOS EIC; FOWLP via ASE/SPIL with TMVs; 50k+ shipped) → Davisson TH6 102.4T (16× 6.4T OE; N3 ASIC; box assembly via Micas/Celestica; NTT buying bare TH6 dies for proprietary OEs) → future roadmap on TSMC COUPE (forces shift from edge-coupling+MZM to grating+MRM). Hot Chips 2024: experimental 6.4T OE co-packaged with logic + 2 HBM + SerDes tile; CoWoS-L (>100mm edge) fits up to 4 OEs = 51.2T.

**External Laser Source (Nvidia Q3450):** 18 ELS modules × 8 CW DFB chips; ~350mW/chip; each laser provides 24.5 dBm to cover connector/coupling/modulator losses; lasers + TECs ≈ 70% of ELS power. Suppliers: **Lumentum (sole, initial batches)**, Coherent (2nd, late 2026), Furukawa, Broadcom; Chinese (Yuanjie, Shijia) longer-term commoditization threat — "still somewhat of a moat" on high-power. Nvidia VLSI laser partners: Lumentum (high-power DFB), Ayar (DFB arrays), Innolume (QD mode-locked combs), Xscape/Enlightra/Iloomina (pumped nonlinear resonant combs); VCSEL arrays explored for "wide-and-slow."

**Nvidia CPO supply chain → listed exposure:**

| Component | Key suppliers | Listed tickers in vault |
|---|---|---|
| External laser source | Lumentum, Coherent, Furukawa, Broadcom | [[Theses/LITE - Lumentum]], [[Theses/AVGO - Broadcom]] |
| Laser supply (Ayar SuperNova) | Sivers (via Ayar) | [[Theses/SIVE - Sivers Semiconductors]] |
| III-V / InP epitaxy + MOCVD | IQE, Aixtron | [[Theses/IQE - IQE]], [[Theses/AIXA - Aixtron]] |
| OE foundry / packaging | TSMC COUPE; hybrid-bond tools | [[Theses/TSM - Taiwan Semiconductor]], [[Theses/BESI - BE Semiconductor Industries]] |
| OSAT (OE + system assembly) | ASE/SPIL (3711.TW), Amkor, Shunsin (6451.TW), Fabrinet, Foxconn (2354.TW) | (AMKR, FN — no thesis) |
| FAU | TFC (300394.SH), Senko (9069.JP), FOCI (3363.TW), Sumitomo, AFR | (no thesis) |
| Coupling / FAU machines | Ficontec (>$300k/unit), All Ring Tech, GMT Global | (no thesis) |
| Shuffle box / MPO / MT ferrule | T&S (300570.SH), Corning, Molex, US Conec | (GLW — no thesis) |
| E/O test equipment | Keysight, Ficontec, **Teradyne, Advantest, FormFactor**, Chroma, Anritsu, Multilane | [[Theses/TER - Teradyne]], [[Theses/6857 - Advantest]], [[Theses/FORM - FormFactor]] |

**CPO-vendor architecture comparison (the choices that predict each vendor's supply-chain dependencies):**

| Vendor | Modulator | Coupling | Laser / ELS | Lead bandwidth | Go-to-market |
|---|---|---|---|---|---|
| Nvidia | MRM, 200G PAM4 | Grating | ELS (Lumentum sole initial) | 1.6T OE → 3.2T | Bookended switch (Quantum/Spectrum) |
| Broadcom | MZM → MRM (on COUPE) | Edge → grating | ELS | 6.4T OE | Switch + customer AI ASIC |
| Ayar Labs | MRM | Edge (GC-capable) | SuperNova 16λ (**Sivers**) | 4T → 13.5T/OE (108T/pkg) | UCIe chiplet, bookended; Alchip/GUC |
| Nubis (Ciena) | MZM | 2D surface (glass FAU, 36 fibers) | ELS (4 laser fibers) | 1.6T → 6.4T | Open/interoperable; Samtec + Amphenol |
| Celestial AI | **EAM (GeSi, C-band)** | Grating | C-band ELS | 16T → 64T chiplet | Bookended; Marvell; → Trainium 4 |
| Lightmatter | MRM, 56G NRZ | — | **GUIDE** (own VLSP, 50T) | 114T M1000 interposer | NPO (2026/27) → CPO → interposer (2029+) |
| Xscape | n/a (laser co.) | — | ChromX 4–128λ programmable, single-fiber | — | Laser source |
| Ranovus | MRM | — | own + merchant | 64×100G PAM4 | Interoperable (Ethernet); MediaTek + AMD |
| Scintil | n/a (laser co.) | — | LEAF Light 8/16λ, III-V-on-SiPho (SHIP) | — | ELSFP laser source |

Read across the table: the modulator + coupling choice cascades into the entire supply chain. MRM+grating (Nvidia, TSMC COUPE, Ayar, Lightmatter, Ranovus) is the consensus path and the one COUPE's PDK supports; MZM (Nubis) and EAM (Celestial) are off-PDK bets that buy specific advantages (interoperability/maturity for MZM; thermal tolerance for EAM-under-interposer) at the cost of foundry self-integration. "Bookended" vendors (Nvidia, Broadcom, Ayar, Celestial) force a full-stack adoption; Nubis and Ranovus court the open/interoperable lane.

## Key Segments

### Part 1 — TCO Analysis (scale-out diluted, scale-up the killer app)
Models the cost/power of co-packaging for scale-out and finds the benefit swamped by the server's dominant share of cluster TCO (tables above). The high-radix "shuffle-in-a-box" (Quantum 3450 = 144× 800G; Spectrum 6800 = 512× 800G) lets customers flatten 3-layer to 2-layer networks (host count scales with port-count^layers), the genuine selling point. Conclusion: limited scale-out adoption near-term — no rapid hyperscaler adoption curve expected. Scale-up is the killer application because copper's 2m reach caps world size and scale-up bandwidth (9× scale-out per GPU) makes its CPO TAM larger. Increasing scale-up world size (GB200 took it from 8 to 72 all-to-all GPUs) unlocks collective-communication gains infeasible on scale-out; optics lets world size grow across racks rather than packing density into one (Kyber). Rubin Ultra targets a 2027 (likely late-2027) launch, but the supply chain can't ship tens of millions of CPO endpoints by then — so **Feynman appears to be the focal point for CPO injection into the Nvidia ecosystem.**

### Part 2 — Why CPO now: SerDes plateau, Wide I/O, and link resiliency
DSP is "public enemy #1": ~50% of an 800G SR8 module's power, 20–30% of BoM. I/O has scaled far slower than FLOPs; off-package bandwidth is bump-count-limited on flip-chip BGA. SerDes is plateauing — 224G was hard; true 448G uni-directional is uncertain (Nvidia uses bi-directional SerDes in Rubin as the workaround). NVLink's 11× gain (1.0→5.0) came almost entirely from 10× SerDes speed (20G→200G), not lane count — so the plateau directly threatens Nvidia's scale-up moat and opens the door to AMD/hyperscalers. Wide I/O (UCIe-A ~10 Tbit/s/mm vs Blackwell's ~0.4) is the escape, and CPO's already-advanced package makes wide-I/O integration nearly free. Co-packaged copper (CPC, twinax off substrate) is flagged as the simpler parallel path that may actually deliver 448G for short-reach in-rack scale-up. **Link resiliency** is an underrated CPO driver: in ~1M-link pluggable clusters there are dozens of interruptions/day, 80% "no trouble found" soft failures from connector/wirebond/contamination variability; CPO removes the human provisioning element (factory-tested known-good), cuts E/O interface count, and improves signal integrity with deterministic package-level design rules.

### Part 3 — Bringing CPO to market: COUPE, coupling, lasers, modulators, scaling
Heterogeneous integration (SiPho PIC + CMOS EIC) beats monolithic (capped at ~35nm — why Ayar is leaving GF for COUPE). **TSMC COUPE** detailed: EIC on N7, PIC on SOI N65, SoIC bumpless bond = 23× bandwidth density vs bumps at iso-power; supports both grating (Si-lens on 770µm Si-carrier + metal reflector, WoW+CoW bond) and edge coupling; full PDK/EDA flow for µLens, 3D floorplan, SoIC-X/TDV/C4. Roadmap: substrate → interposer (12.8T/OE, ~4 Tbit/s/mm). **Coupling:** edge (low loss, polarization-insensitive, broad wavelength, but 1D, no die-stacking, harder fab — GF demoed 32-channel 127µm-pitch SiN edge coupler) vs grating (2D multi-row density, interposer-compatible, easier 2-step etch, but higher loss, narrow band, polarization-sensitive — Nvidia + TSMC prefer it). **Lasers:** on-chip (failure-prone, heat-sensitive, low power) lost to External Light Source consensus (pluggable, serviceable, but 70% of ELS power is lasers+TECs; 24.5 dBm/laser to cover losses). **WDM:** CWDM (~20nm spacing, few channels) vs DWDM (<1nm, 40–100+ channels); MRMs do WDM natively. **Scaling vectors** and Fast-Narrow vs Slow-Wide frameworks introduced here. **Adoption friction:** interoperability is "wild west" — pluggables get electrical (OIF), optical (IEEE 802.3 PMD), mechanical (MSA) interop; CPO has none yet (OIF CPX effort is nascent), so vendors push proprietary system-level lock-in. Serviceability: sub-micron fiber alignment inside a hot, cramped chassis; FAU replacement requires going inside the box without disturbing neighboring fibers — far worse than a front-panel hot-swap.

### Part 4 — Products of today and tomorrow (incumbents)
**Nvidia** (Quantum-X Q3450 115.2T 2H25, Spectrum-X 6810/6800 2H26; MRM 200G PAM4 in production — the key milestone; COUPE hybrid bond; GC preference). **Broadcom** (Humboldt→Bailly→Davisson TH6; abandoning own FOWLP/SPIL → COUPE, must "start fresh" on grating+MRM vs its edge-coupling+MZM heritage; first mass-produced Broadcom CPO likely lands in a customer's AI ASIC — a factor in OpenAI choosing Broadcom; **Google, Broadcom's largest ASIC customer, refuses CPO** on reliability-first grounds). **[[Theses/INTC - Intel]]** (4-stage roadmap: 2023 package-to-package electrical I/O → 2024 OCI chiplet 4T bidir, 64×32G, ~5 pJ/bit on a concept Xeon → 2025 detachable glass optical bridge connector → 2027 3D vertical expanded-beam coupling). **MediaTek** (custom-ASIC house integrating CPO by data-rate: NPC at 200G with >900µm pitch → CPC at 200–300G with >400µm → CPO at 400G+ with ~130µm pitch).

### Part 4b — The seven CPO-focused companies
**Ayar Labs** — TeraPHY UCIe optical-retimer chiplet (the world's first). Gen1 2T / Gen2 4T ("Eagle": 8× 512G ports, 32G NRZ × 16λ via MRM, edge-coupled, SuperNova ELS supplied by **Sivers**, 24 fibers/chiplet). Gen3 13.5T/OE pivots to TSMC COUPE at 200G/lambda PAM4; 8 OEs = ~108T/package in the Ayar–Alchip/GUC XPU reference. Backers: GlobalFoundries, Intel Capital, Nvidia, AMD, TSMC, Lockheed Martin, Applied Materials, Downing. Bookended (customer adopts full stack). The Hot Chips 2025 thermal test is the key MRM-resilience de-risking datapoint: Ayar emulated a 0→500W power step by sweeping the laser wavelength (a 20nm/s sweep ≈ 320°C/s equivalent), showing zero bit errors to 800°C/s — directly answering the worry that ring modulators can't survive the rapid thermal excursions of a co-packaged environment.

**Nubis** (acquired by Ciena Oct 2025) — Vesta 100 1.6T NPX socketable OE (16×100G, 6×7mm), **MZM** chosen for interoperability/reliability/maturity, IEEE/OIF-compliant electrical interface. Differentiator: densest 2D FAU shipping today — 36 fibers (16 Tx, 16 Rx, 4 laser) surface-coupled via a laser-drilled glass block + Sumitomo FlexBeamGuidE 90°-bend fiber; enables multi-row OEs around the ASIC. April 2025: 16×200G PIC at 0.5 Tbps/mm; Samtec partnership for a 32×200G (6.4T) snap-in compatible with Si-Fly HD co-packaged-copper connector (common copper/optical footprint → potential open pluggable-CPO ecosystem). Nitro linear redriver (with Amphenol) extends 200G active copper cables to several meters.

**Celestial AI** — "Photonic Fabric" (PF): TSMC 5nm PF Chiplets (UCIe/MAX PHY; Gen1 16T → Gen2 64T) co-packaged with customer XPUs; OMIB optical multichip interconnect bridge (CoWoS-L/EMIB-style, photonics on the embedded bridge, center-of-die I/O bypassing shoreline); and PFMA Photonic Fabric Memory Appliance (115.2T, 16 ASICs × 7.2T, **world's first silicon with center-of-die optical I/O**, each ASIC = 2×36GB HBM3E + 8× external DDR5 — a "warm" KV-cache memory tier). Uses **EAM** modulation (the only major adopter) — better thermal tolerance (35°C instantaneous) for an interposer beneath a hundreds-of-watts XPU, but C-band band-edge (hard to shift to O-band), needs a separate mux, and — critically — **lacks a TSMC COUPE PDK, so Marvell must integrate EAM into a foundry itself** (other vendors lean on COUPE's MRM+heater PDK). Link efficiency ~2.5 pJ/bit E-O-E + ~0.7 laser vs ~10 copper. Adjacent to the [[Macro & Technology/CXL Memory Disaggregation Framework|memory-disaggregation]] thesis. Amazon warrant ($87.0029, vesting on PF purchases through Dec 2030) ties the ramp to Trainium 4. The systems pitch beyond the chiplet: the PFMA is a 2U box of 16 PF ASICs (each 2×36GB HBM3E + 8× external DDR5) acting as a 16-radix all-to-all switch where the FAU fans out *inside* the box, so each XPU needs only one external fiber. Center-of-die optical I/O frees the shoreline that physical I/O normally consumes, letting each ASIC double as router *and* memory endpoint — sidestepping the HBM-stacks-per-XPU beachfront limit and serving a shared HBM pool via all-reduce. That router-plus-memory duality is the architectural difference from NVLink's NVL576 (where NVSwitch only routes), and the reason Celestial reads as a memory-disaggregation play, not merely a CPO one.

**Lightmatter** — Passage M1000: 4,000 mm² optical interposer beneath the host, 114T aggregate via 1,024 compact 112G SerDes (~8× smaller), 256 fibers × 16λ DWDM (1–1.6T/fiber), MRMs (~15µm) at 56G NRZ, built-in OCS for redundancy/rerouting, UCIe edge-stitching. Develops its own **GUIDE** laser — the first Very Large Scale Photonics (VLSP) source integrating hundreds of InP lasers on one silicon chip (up to 50T, self-repairing via over-provisioning; two GUIDE units replace Nvidia Q3450's 18 ELSs). First to market is NPO OEs (2026/27, up to 3×40-fiber FAUs); COUPE-based CPO 2027–28; M1000 flagship 2029+. Thermal debate (MRMs beneath a hot XPU) countered with control loops handling 2,000°C/s excursions, 0–105°C.

**Xscape Photonics** — ChromX programmable laser, 4–16λ now → up to 128λ roadmap, single fiber (external III-V laser + on-chip multicolor generator). Programmability flexes wavelengths per workload; single-laser/single-fiber design sidesteps the multi-laser power and multi-fiber coupling complexity that plagues most CPO. EagleX eval kit shipping; product announcements targeted 2026.

**Ranovus** — Odin OE: MRM (microring resonator), up to 64×100G PAM4; **interoperability-first** (Ethernet-standard, 8×100G DR8 interop demoed with MediaTek at OCP 2024 against third-party pluggables). Taped out monolithic CPO at GF and a PIC at TSMC; demonstrated 800G-chiplet interop with AMD; MediaTek partnership for Odin direct-drive CPO 3.0 chiplet for hyperscaler custom XPUs.

**Scintil** — LEAF Light PSoC (KGD die or module), 8 or 16 lasers at 100/200 GHz spacing for single-fiber DWDM, ELSFP (OIF) reference module. SHIP process bonds unpatterned III-V onto a flipped standard SiPho wafer, then patterns lasers lithographically — wafer-level III-V-on-SiPho integration giving tighter DWDM channel control than E-beam-patterned discrete InP lasers, plus power efficiency (generate+mux many colors on one chip vs high-power discrete lasers + combiner). Pairs naturally with ring-modulator CPO.

### Part 5 — Nvidia's CPO supply chain (component-by-component)
**Optical engines:** 72× 1.6T (or later 36× 3.2T) @ ~$1,000/unit incl. FAU = $35–40k BOM for the Q3450. **ELS:** 18 modules × 8 CW DFB @ 350mW; Lumentum sole initial supplier, Coherent 2nd late 2026, Yuanjie/Shijia the commoditization threat (high-power "still somewhat of a moat"). **FAU:** TFC Optical (300394.SH — Nvidia partner ~3yr, Suzhou advanced-packaging build-out), Senko (9069.JP — SEAT detachable FAU, GF edge-coupling collaboration; likely for Spectrum-X + Broadcom TH6), FOCI (3363.TW); Sumitomo, AFR (close to Broadcom). Each 1.6T OE FAU = 20 fibers (8 Tx, 8 Rx, 4 laser) → 1,440 fibers/system (1,152 Tx/Rx); testing is ~10–15 min/FAU manual labor (Corning estimate) — a throughput bottleneck. **Coupling/FAU machines:** Ficontec (Germany, >$300k/unit, industry-leading accuracy + double-sided wafer-level PIC test), All Ring Tech (Taiwan, traction from 2026), GMT Global (Taiwan, ~75% cheaper than $200–250k Japanese tools). **Shuffle box:** >1,000 fibers/Q3450 → ~$3,000+; T&S Communications (300570.SH, patented automated alignment, Corning subcontracts to them), Molex (~20% pricier). **MPO connectors:** 144/switch; US Conec, T&S, Senko, Broadex, Optec. **MT ferrules:** US Conec (30+ yr), Fukushima, Sumitomo, plus FOCI/TFC/T&S (in-house for vertical integration). **OSAT:** ASE/SPIL (3711.TW — key Nvidia supplier incl. future Rubin-rack CPO), Amkor, Shunsin (6451.TW — Broadcom ties), Fabrinet (FN — Nvidia module assembler building OE packaging/test/system assembly; candidate for Broadcom too), Foxconn (2354.TW). **E/O test (un-standardized battleground):** Keysight (premium high-speed, new 1.6T scopes), Ficontec (wafer-level photonic test), **Teradyne ("very serious," acquired a packaged-optical-test startup)**, Advantest, FormFactor, Chroma, Anritsu, Multilane.

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

> "By adopting TSMC's COUPE solution, customers effectively commit to using TSMC-manufactured PICs, as TSMC does not package SiPho wafers from other foundries."

> "Despite Broadcom having the most CPO experience, this change in technical approach means that Broadcom must essentially start fresh on some aspects of their technology."

> "For Nvidia, whose NVLink scale up fabric is an important moat, this roadblock [SerDes plateau] could make it easier for competitors such as AMD, and the hyperscalers to catch up."

> "We do not expect Google to adopt CPO any time soon." — Google's reliability-first philosophy makes CPO "a deal breaker."

> "The industry needs far more than just 15 CPO switches tested for 11 months in a lab setting before it pivots towards CPO scale-out switching and commits billions of dollars to this technology."

> Celestial/Marvell: "$1B by the end of Calendar Year 2028 ... an additional $2.25B of payout to Celestial AI's equity holders is contingent upon the company achieving a cumulative revenue of at least $2.0 billion by January 2029."

> On the Amazon warrants: vesting "based on Amazon's purchases of Photonic Fabric products, indirectly or directly, through December 31, 2030" — "strongly suggesting that AWS's Trainium will be the target product as this starts to ramp in late 2027."

> "Nvidia's scale-out CPO product launch is serving as a practice run and pipe-cleaner for the real high-volume deployment ... far more sizable and impactful for scale up."

> "CW laser sources are considered relatively standardized and commoditized in general, but there is still somewhat of a moat around building the high power laser sources that are required for CPO applications."

> Teradyne "has been 'very serious' about getting into photonic testing ... recently acquired a startup specializing in packaged optical testing."
