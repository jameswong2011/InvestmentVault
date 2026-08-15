---
publish: false
date: 2026-08-13
tags: [research, semiconductors, INTC, TSM, MRVL]
sector: ABF Substrates & Advanced Packaging Supply Chain
ticker: INTC
source: 'https://newsletter.semianalysis.com/p/ectc2026'
source_type: deep-dive
propagated_to: [INTC, TSM, MRVL, BESI, 2802]
---

## Thesis Delta

Consensus prices TSMC [[Theses/TSM - Taiwan Semiconductor|TSM]] CoWoS as the uncontested chokepoint on large-package AI accelerators and models advanced packaging as a single capacity-scarcity annuity; ECTC 2026 implies the binding constraint has already split into three new scarce layers — package size (circular-interposer + reticle-stitch limits), HBM4E I/O doubling plus in-bridge power delivery, and multi-kilowatt package cooling — where Intel [[Theses/INTC - Intel|EMIB-T]] is now a credible CoWoS *substitute* for the largest accelerators (36 µm pitch validated at 2× reticle, roadmapped to Google TPU v9) even as TSMC extends its lead into the *next* layer (direct-to-silicon microfluidic cooling >5 kW, on-package optics via COUPE). This bears directly on the TSM CoWoS-monopoly-durability leg and the Value-Layer-Monopoly question of whether the packaging layer is widening for the incumbent or being contested and relocated.

## Summary

Transistor-density scaling has slowed, so advanced packaging became the primary scaling vector — and the package itself is now the bottleneck. ECTC 2026 disclosures cluster around three binding limits: circular silicon interposers cap package size and wafer utilization, HBM4E doubles I/O count while raising data rate, and multi-kilowatt packages overwhelm conventional cold-plate cooling. Intel was the largest presenter (12 papers vs TSMC's 3, Samsung's 11) and its headline was EMIB-T — EMIB with through-silicon vias. Intel validated a 36/35 µm bump pitch (a 65% density increase over Granite Rapids' 45 µm) on a 2× reticle package, is extending that pitch to 4.5× reticle packages with certification targeted for end-2026, and showed a 240 mm × 240 mm quarter-panel test vehicle (~67 reticles). The TSVs deliver power directly through the bridge, cutting DC voltage drop 68–80%; on-bridge MIM capacitors (500 fF/µm²) improve PDN AC impedance >82%; simulated HBM4E signaling holds >60% UI eye width to 16 Gb/s. SemiAnalysis frames EMIB-T as the reason Google TPU v9 uses it and "the most credible alternative to TSMC's CoWoS platform for large-package AI accelerators" — while flagging that EMIB-T still trails CoWoS on deployed deep-trench capacitors (DTC/eDTC), integrated voltage regulators, and active LSI. This is the Semis #2 qualification-gate question live: the packaging gate that was single-vendor is narrowing, but not yet crossed at volume.

Marvell [[Theses/MRVL - Marvell Technology|custom HBM]] attacks the JEDEC boundary. By fabricating a custom base die on an advanced logic process, Marvell moves the memory-side interface off the accelerator, cutting the host ASIC footprint dedicated to HBM PHYs and logic by ~60% and shortening the interposer channel from 6.5 mm to 1.5 mm — enough to keep a 4.1 TB/s link (1024 channels @ 32 Gb/s) on a *cheaper organic RDL interposer* rather than silicon. Nvidia's Feynman will use custom HBM for the same reasons (SemiAnalysis estimates ~16% of Rubin GPU die area is HBM logic/PHY). The custom base die also fans out to LPDDR or a second HBM layer, relevant to AMD MI450/MI500. Samsung's interposer paper quantifies the HBM4E tax: 2× the interposer layers of HBM3E, +86% power, and it proposes an 8-layer silicon interposer that claws 20% of layers back. Samsung's thermal work shows hybrid copper bonding (HCB) cutting HBM *stack* thermal resistance 19–29% vs thermal-compression bonding — a lever that matters more as custom HBM pushes power into the base die, directly relevant to [[Theses/000660 - SK Hynix]], [[Theses/MU - Micron Technology]] and the [[Theses/BESI - BE Semiconductor Industries|BESI]] bonding-transition thesis.

Cooling is where TSMC and its hyperscaler partners still lead. TSMC pushed coolant into the silicon: micropillars formed on the backside of the SoC dies on a CoWoS-R (organic-interposer) test vehicle dissipated 4 kW at 4 LPM and 5.3 kW at 8 LPM, with uniform >5 kW across the full 3.3× reticle vehicle — versus 1.9–3.0 kW for conventional lidded/lidless cold plates that saturate beyond 4 LPM because the thermal interface material (TIM) becomes the bottleneck. Microsoft went further, etching straight microchannels into a *real* Nvidia GH200 and reporting 51–60% lower GPU junction-to-inlet thermal resistance and a 50% package-level reduction, with 6 months of reliability data (9 clogging events across ~4370 observations, no silicon erosion). This is the [[Sectors/Data Center Power & Cooling]] inflection: cooling has moved inside the package, and the process integration (micropillar formation post-CoW, new sealants surviving warpage) is a foundry/OSAT capability, not a rack-vendor one.

The fourth vector is on-package optics. Marvell's OMIB embeds a photonic IC in the organic RDL interposer only where needed (electrical bridges elsewhere), claims 1.8 Tbps/mm² bandwidth density, and — via Photonic Fabric (acquired with Celestial AI) — favors substrate-mounted vertically-stacked optical engines near-term (electro-absorption modulators, 224 Gb/s per direction on a 5 nm EIC) because they keep the PIC <5 °C hotter under full XPU load vs ~25 °C on a silicon interposer. Lightmatter's Passage M1000 validated cooling 680 W from a concentrated ~369 mm² test chip (1.47 W/mm²) on a multi-reticle photonic interposer with >95% electrical assembly yield despite ~59 µm reflow warpage. Around these, interposer-less schemes (Intel/SPIL FO-EB, IBM DBrM, Unimicron, panel-scale organic RDL from Resonac/ASE) and a first-of-kind Intel 510 mm × 515 mm 24-layer glass-core panel push toward the panel-level and glass transitions tracked in [[Macro & Technology/CoWoS-to-CoPoS Panel-Level Packaging Transition]] and [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]] — each a pressure point on organic-ABF economics ([[Theses/2802 - Ajinomoto]], [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]]) and OSAT capability ([[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]]). The through-line: Semis #8 — the architecture transition remaps the bottleneck, and the scarce layers are now package size, in-bridge power/signal density, cooling, and on-package optics simultaneously.

## Evidence

Provenance convention: `[web: semianalysis]` = figure reported in the SemiAnalysis ECTC 2026 roundup citing the underlying ECTC papers; `[1×: SemiAnalysis]` = SemiAnalysis first-party observation; `[est.]` = SemiAnalysis estimate.

### Intel EMIB-T — bump-pitch, package-size, and bridge scaling

| Parameter | Value | Provenance |
|---|---|---|
| Validated bump pitch (2× reticle package) | 36/35 µm | [web: semianalysis] |
| Prior pitch (Granite Rapids) | 45 µm | [web: semianalysis] |
| Bump-density gain, 45 → 36 µm | +65% | [web: semianalysis] |
| Granite Rapids-AP package size | 70 mm × 105 mm (~<9 reticles) | [web: semianalysis] |
| Pitch scaling in progress | 4.5× reticle silicon, cert targeted end-2026 | [web: semianalysis] |
| Next pitch step (under test) | 25 µm, two 1-reticle dies via one 3 mm × 18 mm bridge | [web: semianalysis] |
| Limiter below 25 µm | shifts from bridge routing density → bump formation / placement / assembly yield | [web: semianalysis] |
| Largest test vehicle | 240 mm × 240 mm quarter-panel (~67 reticles) | [web: semianalysis] |
| Quarter-panel caveat | severe warpage on booth sample | [1×: SemiAnalysis] |
| Bridge stack-up | 10 metal layers (4 routing), MIM caps between M1–M2 | [web: semianalysis] |
| DC voltage-drop reduction from TSVs | 68–80% | [web: semianalysis] |
| On-bridge MIM cap density | 500 fF/µm² (500 nF/mm²), ~= Intel 18A MIM | [web: semianalysis] |
| PDN AC-impedance improvement w/ bridge MIM | >82% | [web: semianalysis] |
| HBM4E eye width @ 12 Gb/s | ~67% UI (no EQ) → ~72.5% (1-tap DFE) | [web: semianalysis] |
| HBM4E eye width @ 12.8 / 14 / 16 Gb/s | >60% UI at all speeds | [web: semianalysis] |
| Signal routing strategy | M9 ~28% of longest channel in tightest region; M3 ~84% but shorter | [web: semianalysis] |
| Named accelerator | Google TPU v9 ("expected to use it") | [web: semianalysis] |
| Vectors still behind CoWoS | DTC/eDTC deployed, integrated voltage regulators, active LSI | [web: semianalysis] |

### HBM4E interconnect + interposer scaling (Samsung)

| Parameter | Value | Provenance |
|---|---|---|
| HBM4E data rate | 12 Gb/s and above | [web: semianalysis] |
| I/O pin count | 2× vs HBM3 (HBM4 doubles pins) | [web: semianalysis] |
| Interposer layers | ~2× HBM3E, ~5× HBM2 | [web: semianalysis] |
| Power vs prior gens | +86% vs HBM3E, 5.6× vs HBM2 | [web: semianalysis] |
| Samsung interposer | 8 layers, 20% fewer than estimate; 2-signal/1-ground; 75% layers signal | [web: semianalysis] |

### HBM hybrid-bonding thermals (Samsung, TCB vs HCB)

| Metric | Value | Provenance |
|---|---|---|
| Internal HBM thermal resistance | −12.2% (air) / −12.9% (liquid) | [web: semianalysis] |
| Total HBM thermal resistance | −3.5% (air) / −7.7% (liquid) | [web: semianalysis] |
| Stack-level Rth (baseline HCB vs TCB) | −19% | [web: semianalysis] |
| Stack-level Rth at 2× / 4× HCB pad density | −22.3% / −29.1% | [web: semianalysis] |
| GPU-to-HBM crosstalk share, 1× → 3× base-die power | 13% → 5% | [web: semianalysis] |
| HCB headroom | inlet +1–2 °C @ const power, or ~+4% power @ const temp; cooling power −~7% | [web: semianalysis] |

### Cooling — direct-to-silicon microfluidic

| Approach | Result | Provenance |
|---|---|---|
| TSMC conventional lidded cold plate (1–2 LPM, 40 °C DI) | 1.9–2.3 kW | [web: semianalysis] |
| TSMC lidless cold plate | 2.5–3.0 kW; saturates >4 LPM (TIM-limited) | [web: semianalysis] |
| TSMC micropillar direct-to-silicon | 4 kW @ 4 LPM; 5.3 kW @ 8 LPM; >5 kW uniform full vehicle | [web: semianalysis] |
| TSMC test vehicle | CoWoS-R, 3.3× reticle, 4 SoC dies + 8 HBM; passed MSL4 | [web: semianalysis] |
| Microsoft microchannel (real GH200) | GPU junction-to-inlet Rth −51–60% @ 1 LPM | [web: semianalysis] |
| Microsoft HBM (still cold-plate + TIM) | −27–37% | [web: semianalysis] |
| Microsoft package-level Rth | −50% | [web: semianalysis] |
| Microsoft reliability | 9 clogging events / ~4370 obs over 6 months; no silicon erosion | [web: semianalysis] |
| ECTC paper count | Intel 12, Samsung 11, TSMC 3 | [web: semianalysis] |

### Custom HBM + on-package optics (Marvell) and photonic interposer (Lightmatter)

| Parameter | Value | Provenance |
|---|---|---|
| Host ASIC HBM-PHY/logic area saved (custom HBM) | ~60% | [web: semianalysis] |
| Custom-HBM link | 1024 ch @ 32 Gb/s = 4.1 TB/s (= 2048-bit JEDEC @ 16 Gb/s) | [web: semianalysis] |
| Interposer channel length | 6.5 mm → 1.5 mm; keeps 9 layers, 2/2 µm L/S | [web: semianalysis] |
| Rubin GPU die area on HBM logic/PHY | ~16% | [est.] |
| OMIB bandwidth density | 1.8 Tbps/mm² | [web: semianalysis] |
| OMIB test vehicle | 1 XPU + 6 EIC; 6 PIC + 6 bridge + 12 DTC embedded; ~2× reticle RDL, 4 layers 2/2 µm | [web: semianalysis] |
| Photonic Fabric optical engine | 5 nm EIC, 4× 56 Gb/s TX-RX = 224 Gb/s/direction; EAM (not MRM) | [web: semianalysis] |
| PIC temp rise under full XPU load | <5 °C (substrate) vs ~25 °C (interposer) / ~20 °C (bridge) | [web: semianalysis] |
| PIC transient heating | ~10 °C/s (substrate) vs ~100 °C/s (bridge) / ~120 °C/s (interposer) | [web: semianalysis] |
| Lightmatter M1000 | 15 ASIC chiplets on 4-tile interposer; ~2100 mm² (< 1/3 of 7200 mm² substrate) | [est.] |
| M1000 thermal validation | 4× 170 W quadrants = 1.47 W/mm² over 369 mm²; PIC ~100 °C @ 25 °C coolant, 1.8 LPM/kW | [web: semianalysis] |
| M1000 warpage / yield | ~59 µm @ 260 °C reflow; >95% electrical assembly yield (magnetic fixture) | [web: semianalysis] |

### Hybrid bonding, interposer alternatives, TIM, glass, RDL, stacked memory

| Item | Value | Provenance |
|---|---|---|
| Mitsui/ASE Cu-polymer bond | pressure-less, 200 °C, 10 µm pitch | [web: semianalysis] |
| TOK/NYCU bond | 10 seconds @ 150 °C | [web: semianalysis] |
| Intel fine-grain Cu (W2W) | uniform bond after 175 °C / 200 °C; ~60% electrical yield (2 of 3; lower bound) | [web: semianalysis] |
| Applied Materials + EV Group | 450 nm pitch W2W, 98% yield across 20M links | [web: semianalysis] |
| CEA-Leti | >97% yield after 100 °C anneal, no plasma | [web: semianalysis] |
| Intel/SPIL FO-EB (SRAM chiplet) | 25 µm pitch microbumps; >265 GB/s/mm² @ 0.24 pJ/b | [web: semianalysis] |
| IBM DBrM | 30 µm pitch Si bridge; >30 N bending (vs 0.2 N underfill-only) | [web: semianalysis] |
| SPIL TIM (55×55mm FO-EB) | HS-TIM 5.7 W/m·K, HCF-TIM 10 W/m·K vs 4 W/m·K commercial | [web: semianalysis] |
| TIM reliability (1000 hr @ 150 °C) | HCF-TIM 95% coverage vs HS-TIM 75% | [web: semianalysis] |
| Nanocrystalline-diamond microbump layer | 500–600 W/m·K (~20× conventional) | [web: semianalysis] |
| Intel glass-core panel | 510 mm × 515 mm, 24-layer (10-2-10), Cu-filled TGVs, 2 embedded EMIB, optical waveguides; no SeWaRe post thermal-shock | [web: semianalysis] |
| STATS ChipPAC glass-core (74×74mm) | edge coating required; warpage −33.5% coated vs uncoated | [web: semianalysis] |
| RDL roadmap | 10/10 µm (2015) → 2/2 µm today → 1/1 µm next; UCIe 3.0 up to 64 GT/s | [web: semianalysis] |
| GUC + TSMC CoWoS-R RDL | 8-layer, UCIe-A x64 @ 16–36 GT/s, 45 µm bump pitch; 0.77 UI @ 32 GT/s | [web: semianalysis] |
| Samsung VCS stacked DRAM | <56 µm pitch Cu posts; power −41% (0.646 W → 0.384 W iso-speed); 8.6 → 11.8 Gb/s; footprint −40%, BW +2.6×, I/O +6× | [web: semianalysis] |

## Contradiction Check

The source bears on three theses. The central question — does EMIB-T as a credible CoWoS alternative strengthen or challenge the TSM-CoWoS-monopoly view — resolves to *challenges it at the incumbent 2.5D large-package layer, but does not fire the kill trigger, and is offset by TSMC enveloping the adjacent scarce layers (cooling, optics)*.

**[[Theses/TSM - Taiwan Semiconductor]] — CHALLENGES, but partially and offset.**
- §Key Non-consensus Insights #1 ("CoWoS is a $10B+ separable revenue annuity") asserts "Intel Foveros and Samsung I-Cube are >2 generations behind in capacity and yield." The source directly *pressures* this: EMIB-T is validated at 2× reticle with 36 µm pitch, roadmapped to 4.5× reticle by end-2026, and is called "the most credible alternative to TSMC's CoWoS platform for large-package AI accelerators." A ">2 generations behind" framing is hard to sustain against a named Google TPU v9 design win. This is the Semis #2 qualification-gate lens firing as a *hypothesis to test*: the single-vendor packaging gate is contestable at the large-package tier.
- §Conviction Triggers → "→ LOW if: a named production-scale CoWoS-alternative win (e.g., Google TPU v9 volume on Intel EMIB-T)." The source is the strongest evidence yet toward this trigger — but does **not** fire it: EMIB-T is "expected to be used" in TPU v9, framed as roadmap/evaluation, not confirmed volume production. Treat as a pre-trigger signal to monitor, not a fired trigger (consistent with the thesis's own 2026-07-24 Mental Models note: "overflow deliberately routed to EMIB-T/OSATs … falsifier: a named at-scale CoWoS-alternative production win").
- §Mental Models (Semis #1, bottleneck relocated to packaging — "CONFIRMED binding") is *reinforced and extended*: the source shows the bottleneck has fractured beyond CoWoS interposer capacity into HBM4E I/O/power and multi-kW cooling. Crucially, TSMC leads the *next* layer — direct-to-silicon micropillar cooling >5 kW and COUPE-style stacked optics — so under Semis #8 (architecture transition remaps the bottleneck) and the Value-Layer-Monopoly platform-envelopment reading, TSMC's layer position may be *relocating* (interposer → cooling/optics) rather than dissolving. The source itself concedes EMIB-T "is still behind TSMC's CoWoS platform on several vectors" (DTC/eDTC, IVRs, active LSI). Net: the CoWoS-annuity durability leg is *nicked, not broken*; conviction impact on TSM = unchanged, watch-item sharpened.

**[[Theses/INTC - Intel]] — STRENGTHENS the structural-second-source / EMIB-external path.**
- §Industry Context → "Advanced packaging: Foveros as competitive moat, not standalone differentiator" distinguishes external EMIB (2.5D bridge, ~90% yields) from internal-only Foveros Direct (3D). The source adds fresh, specific validation to the EMIB leg: 2× reticle @ 36 µm today, 4.5× reticle cert end-2026, 240 mm × 240 mm quarter-panel, 68–80% Vdrop cut from TSVs, HBM4E 12+ Gb/s. This substantiates non-consensus Insight #3 (structural second source) at the technical level and extends [[Research/2026-07-14 - Intel Foveros Direct vs CoWoS Advanced Packaging - deep-dive]] with the EMIB-T pitch/reticle roadmap.
- §Catalysts → "H2 2026: EMIB-T launches (120×180mm 24-HBM-stack packaging)" and §Key Metrics ("EMIB-T H2 2026") are corroborated on timing.
- §Mental Models (2026-07-24) already logged "Google booked Intel for packaging >3M TPUs in 2028 … the packaging-only-at-scale path the thesis called foreclosed is materializing via EMIB." The source's Google TPU v9 datapoint compounds this. Caveat preserved: the thesis's structural objections (no packaging-only economics without die manufacturing; Foveros step-yield undisclosed) are untouched — and the source confirms EMIB-T still trails CoWoS, so this is credibility-building, not a re-rate. Conviction impact = unchanged (medium, per current thesis).

**[[Theses/BESI - BE Semiconductor Industries]] — NEUTRAL-to-SUPPORTIVE for the secular thesis; no direct BESI mention.**
- §Industry Context → "Hybrid Bonding Technology Landscape" / "Three-Vendor Bonding Philosophies": the source's hybrid-bonding highlights advance the low-temperature / fine-pitch roadmap that underpins BESI's D2W qualification moat — Intel fine-grain Cu (175/200 °C anneals), Applied Materials + EV Group 450 nm pitch W2W at 98% yield, CEA-Leti >97% at 100 °C, Mitsui/ASE and TOK Cu/polymer at 150–200 °C. Caveat: these are predominantly *wafer-to-wafer* and material/equipment-vendor demonstrations, not the die-to-wafer production BESI leads — supportive of the direction of travel, not a demand datapoint. Applied Materials (BESI's Kinex partner, 9% stakeholder) appearing on the aggressive-pitch W2W result is a mild read-through.
- §Business Model → "Silicon Photonics & Co-Packaged Optics": Samsung HCB stack-thermal data (−19% to −29% vs TCB) and the base-die-power-shift finding support the HCB-pivot narrative in Three-Vendor Philosophies and the thermal rationale for hybrid bonding as HBM base dies absorb more power (custom HBM). Conviction impact = unchanged; consistent with the existing bull secular case.

Mental-model triggers held as hypotheses (per READING PROTOCOL, not verdicts): **Semis #8** — architecture transition remaps the bottleneck to package size + in-bridge power/signal + cooling + on-package optics; **Semis #1** — HBM4E I/O doubling and multi-kW package cooling are now the binding constraints where pricing power will accrue; **Semis #2** — EMIB-T tests whether TSMC's packaging qualification gate is contestable at the large-package tier; **Value-Layer-Monopoly** — advanced packaging is an infrastructure layer (moat-widening under the AI-era overlay), but a focused challenger (EMIB-T) reaching competitive capability is exactly the VLM kill-signal to monitor, while TSMC's move into cooling/optics is the platform-envelopment counter.

## Source Excerpts

> "Intel has validated EMIB-T at a 36/35 µm bump pitch on a package with 2× reticle-sized silicon. This is a reduction over the 45 µm pitch used in Granite Rapids, and a 65% increase in bump density."

> "Their disclosures show why EMIB-T is expected to be used in Google's TPU v9, and why it is the most credible alternative to TSMC's CoWoS platform for large-package AI accelerators."

> "Intel claims that DC voltage drop can be reduced by 68-80% with these TSVs."

> "EMIB-T is still behind TSMC's CoWoS platform on several vectors. TSMC has already deployed DTC/eDTC integration and is further along on integrated voltage regulators and active local silicon interconnect (LSI). EMIB-T narrows the gap, but Intel is still catching up to an ecosystem that has been executing in volume for years."

> "Marvell claims this reduces the host ASIC footprint dedicated to HBM PHYs and associated logic by ~60%, directly freeing up area for more compute, cache or I/O."

> "The micropillar test vehicle matched the lidless cold plate result at 2 LPM, then pulled ahead at higher flow rates, dissipating 4 kW at 4 LPM and 5.3 kW at 8 LPM. Across the full test vehicle, TSMC reported uniform power dissipation above 5 kW."

> "Across these workloads, Microsoft reports 51-60% lower junction-to-inlet thermal resistance for the GPU at a 1 LPM flow rate… Overall, this results in a 50% reduction in thermal resistance for the package."

> "Marvell cites a bandwidth density of 1.8 Tbps/mm² with this approach."

> "While TSMC's CoWoS-R and CoWoS-L remain limited by the circular wafer on which their RDLs are fabricated, constraining package size and wafer utilization, these alternatives shift integration to panel-level or reconstituted formats or eliminate the interposer entirely."
