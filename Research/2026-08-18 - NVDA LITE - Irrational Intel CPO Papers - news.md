---
publish: false
date: 2026-08-18
tags: [research, OpticalNetworking, NVDA, LITE, INTC, AEVA, SIVE]
sector: Optical Networking & Photonics
ticker: NVDA
title: 'Intel CPO Group is Alive? + Very Interesting NVDA/LITE/AEVA Bonus Papers'
publication: Irrational Analysis
gmail_id: 1a01312f9faceb6b
source: 'https://irrationalanalysis.substack.com/p/intel-cpo-group-is-alive-very-interesting'
source_type: news
propagated_to: [NVDA, LITE, INTC]

---

# Intel CPO Papers + NVDA/LITE MOPA Array + Aeva SOA — Irrational Analysis

## Thesis Delta
Consensus still prices two things that this 18 August 2026 paper dump moves against. First, Intel SiPho is either written off as attrition-dead or, via [[Theses/INTC - Intel]] Jaguar Shores "silicon photonics interconnects," treated as a credible CPO peer to [[Theses/NVDA - Nvidia]] Spectrum-X/Quantum-X → Irrational Analysis says the group is alive enough to publish, but 8-λ / fake-16-λ BER is garbage versus Nvidia's clock-forwarded bathtub (A+ vs C+/B-): claimed channel BER < 1e-12 is not a 0.47 UI result, SMSR "50 dB" is a clipped 30 dB, and multi-λ SOA four-wave-mixing is the amplitude-noise mechanism. Second, Hurlston's Q4 FY26 co-integrated-laser-for-NPO commentary plus the sell-side NPO-on-engine narrative ([[Research/2026-08-12 - LITE Irrational Analysis Q4 FY26 Call Alpha - deep-dive]]) are read as the next architecture for [[Theses/LITE - Lumentum]] → the Nvidia/Lumentum paper is a monolithic DFB+per-λ-SOA MOPA array (Ayar SuperNova class) with excellent power flatness, spacing, and SMSR and unusable RIN (~−137 dBc/Hz). The market assumption that is wrong: co-integration or "Intel is back in CPO" is the interconnect gate. The operating variables are bathtub BER at a named UI offset, RIN, SMSR, and laser WPE 10%. [G-13] / [Semis #2] qualification is parametric, not a paper count; [Semis #8] CPO remaps the bottleneck onto UHP CW / clock-forwarded engines, not onto a shared-SOA comb. Flag only — do not edit conviction or status. NVDA has no `## Conviction Triggers` section.

## Summary
Irrational Analysis (18 Aug 2026; Gmail `1a01312f9faceb6b`; subscriber full body) is a stream-of-consciousness Hot-Chips-week paper dump, explicitly deprioritized behind a Cerebras event this week and Hot Chips next week. Default 2026 answer on Intel CPO/SiPho was attrition, five re-orgs, dead. Papers today reopen the file without reopening the grade. Intel uses one SOA to amplify all eight modulated wavelengths — the exact multi-λ-into-one-amp geometry [[Research/2026-07-19 - LITE COHR AEVA Practical SOA for CPO NPO - deep-dive]] called fatal on four-wave-mixing. Hybrid-integration lasers (gratings external, etched in silicon; Scintil-adjacent, distinct from Openlight/Tower's single-λ 20 mW / 13 dBm waveguide cap) print ±10 GHz spacing with no TEC wavelength control, which IA flags as fabrication wizardry and as a measurement he does not fully trust. Side-modes are SOA FWM, not laser SMSR: ~30 dB real versus a clipped "50 dB" claim; every pair of wavelengths spawns two FWM tones, and three in-band junk tones sit under each primary line below OSA resolution — you need per-λ filtering, a reference PD, and a low-noise-floor ESA to see the RIN. Ring extinction is a real 5 dB versus the usual 3–4 dB; the worst eye is 1308.3 nm. TIA gain 75 dB. Strange Tx/Rx lane pairing is read as lab-cheesing of ring-filter and thermal setpoints; at scale, worse. Versus Nvidia's clock-forwarded CPO bathtub at the same λ count and per-lane datarate, Intel lanes catastrophically fail at 0.47 UI total sampling offset; a generous 0.2 UI opening would be 1e-10 BER, and Intel will not get that timing without clock forwarding. Grade: Nvidia A+, Intel C+ (B- if coddled). Connector: 1.3 dB average loss with two lenses, accepted as the price of an attachable periscope versus a normal edge-coupling bench.

The "16-wavelength" follow-on is not a 16-λ bus. Tx stays at 8-λ per ring bus (thermal crosstalk); Rx uses three cascaded MZIs to demux, which kills link budget, forces polarization control, and adds a second SOA on the receive path — more FWM into RIN. IA's generous 0.2 UI read on that link is BER 1e-5 against Nvidia's 1e-12 at 0.47 UI clock-forwarded. SMSR on the 16-λ laser array is ~25 dB (mode-hop confidence is poor); a Yokogawa wavemeter plot shows excellent flatness, spacing worse than ±10 GHz on the first line, and suspiciously weaker out-of-band sidemodes that IA reads as lowered SOA power ("CHEEZE"). Paper 20.1 is deferred.

The Nvidia/Lumentum paper is the live-book piece, framed against Hurlston's co-integrated NPO-laser call color. Architecture: monolithic DFB array (Sivers / Ayar SuperNova class — IA's standing hate: yield nightmare, spacing control, reliability) with an individual SOA per channel for gain *and* beam-shaping, so a DFB that normally wants two lenses couples cleaner. It is a MOPA array: ~100 mW/ch out, inferred 20 mW (13 dBm) DFB run a bit hot at 14 dBm, SOA small-signal gain ~6 dB in saturation (the RIN-minimizing region). No FWM, because each SOA sees one wavelength. Die 2.25 mm × 1 mm, 9 wavelengths, single TEC (no thermal spacing control), AR coat on the back facet, **one isolator for the whole array** (isolator + active-alignment cost save), rumored 0.5 dB Lumentum coupling loss, ELSFP packaging for characterization. Power variation, spacing, SMSR: excellent. RIN: shit. One channel has a nasty relaxation-oscillation spike; even stripping it, integrated RIN ~−137 dBc/Hz. Verdict: unusable on a real link; Nvidia Research language is cope. Compare the 14 Aug LITE public CPO-laser book in [[Research/2026-08-14 - COHR LITE - Irrational Analysis Coherent Q4 FY26 - deep-dive]]: LITE discrete plots print RIN < −155 dBc/Hz versus a −145 dBc/Hz CPO spec.

The last third is the "massive alpha" IA had failed to ghetto-model for a year. Laser WPE of 10% is the energy-savings gate for CPO/NPO; below 10% system efficiency degrades exponentially. DWDM power variation < ±0.5 dB is wanted for ring-modulator self-heating (thermal control of the ring bus), not primarily for wall-plug. ±10 GHz spacing accuracy on a 200 GHz DWDM grid is for optical crosstalk, **not** ring-heater power — surprising to IA given 32G modulation and large guard bands. Standard ΔT is 10°C; modeling to 23°C is TEC-runaway territory. Aeva SOA (two zinc-doping variants) prints 22% PCE at 650 mW / 40°C, ASE 40 dB down, FIT < 5 — the same "~650 mW, quite good" device from the 19 Jul primer, now with PCE/FIT numbers, and a Seminex contrast. No AEVA thesis. Charts in the source are images; do not invent paper IDs, OFC/Hot Chips session codes beyond "paper 20.1," or IR dollars.

## Framework / Mental Model
**Three reusable trees (IA). Outputs of applying them sit in Evidence.**

### A. Bathtub BER at a named UI offset
You cannot claim BER from a bathtub at perfect timing. Nvidia specs BER of all lanes at a wide 0.47 UI window *and* clock-forwards (Tx jitter tracked, no PPM). Intel's < 1e-12 claim is the perfect-timing cheat. Methodology: pick the same λ count and per-lane datarate, read BER at 0.47 UI (and at a generous 0.2 UI if the DUT is not clock-forwarded), then grade. Clock-forwarding is the timing architecture, not a footnote.

### B. Multi-λ SOA vs per-λ MOPA (FWM / RIN)
Reuse of the 19 Jul SOA primer, now scored on published comb papers.

| Geometry | What it is | RIN / FWM bind |
|---|---|---|
| Shared SOA on 8 (or 16) modulated λ | Intel CPO | Every pair spawns 2 FWM tones; 3 junk tones under each primary; OSA cannot see them |
| Cascaded-MZI Rx + second SOA | Intel "16-λ" | Extra FWM into RIN; polarization control; link-budget hit |
| Per-channel SOA MOPA | NVDA/LITE array | One λ per SOA → no FWM; RIN can still fail on the DFB+SOA cavity |
| Discrete UHP DFB (no SOA comb) | LITE/AVGO CPO laser book | RIN < −155 dBc/Hz in the 14 Aug public plots |

### C. CPO/NPO energy and ring-bus tolerances
The paper's "massive alpha" — three knobs, only one of which is energy.

| Knob | Spec | Why it binds |
|---|---|---|
| Laser WPE | 10% | Below 10%, CPO/NPO system efficiency degrades exponentially |
| DWDM power variation | < ±0.5 dB | Ring-modulator self-heating / ring-bus thermal stability, not primarily wall-plug |
| Spacing accuracy | ±10 GHz on 200 GHz grid | Optical crosstalk, *not* ring-heater power (IA's prior) |
| TEC ΔT | 10°C standard | 23°C is runaway; single-TEC arrays cannot thermally tune spacing |

Methodology: start from WPE 10%, then ask whether flatness is a ring-thermal problem and whether spacing is a crosstalk problem. Do not collapse all three into "efficiency."

## Evidence

| Claim | Detail | Tag |
|---|---|---|
| Date / format | 18 Aug 2026; stream-of-consciousness; Cerebras this week, Hot Chips next week | [1×: IA] |
| Intel SiPho prior | Attrition, ~5 re-orgs, "dead" | [1×: IA] |
| Intel 8-λ architecture | One SOA amplifies all 8 modulated wavelengths | [1×: IA] |
| Intel laser integration | Hybrid; gratings external / etched in Si; Scintil-similar; Openlight/Tower distinct | [1×: IA] |
| Openlight/Tower λ / power | Single wavelength; max 20 mW (13 dBm) in waveguide | [1×: IA] |
| Intel / Scintil | Multi-wavelength at lower power | [1×: IA] |
| Wavelength control | No TEC λ control on co-integrated lasers; no mention in paper | [1×: IA] |
| Intel spacing (8-λ) | ±10 GHz — "insanely good" | [1×: IA] |
| Intel SMSR claimed | 50 dB (clipped spectrum to hide out-of-band FWM) | [1×: IA] |
| Intel SMSR real | ~30 dB | [1×: IA] |
| FWM accounting | Each λ pair → 2 FWM tones; 3 junk tones under each primary | [1×: IA] |
| How to see in-band junk | Filter each λ; RIN with reference PD + low-noise ESA; OSA insufficient | [1×: IA] |
| Ring extinction | 5 dB on all (usual rings 3–4 dB) | [1×: IA] |
| Worst eye | 1308.3 nm; RIN obviously worse | [1×: IA] |
| TIA gain | 75 dB | [1×: IA] |
| Intel BER claim | All channels < 1e-12 — rejected as perfect-timing bathtub | [1×: IA] |
| Lane pairing | Strange Tx/Rx pairing; lab-cheesed ring filter / thermal setpoints | [1×: IA] |
| FWM confidence | 99.9% that SOA FWM explains lane-to-lane amplitude-noise scatter | [1×: IA] |
| NVDA bathtub | Same λ count, same datarate/lane, clock-forwarded; "god-tier" | [1×: IA] |
| NVDA BER spec | 1e-12 at 0.47 UI sampling offset (total, not ±) | [1×: IA] |
| Intel at 0.47 UI | All lanes would catastrophically fail | [1×: IA] |
| Intel at 0.2 UI (8-λ, generous) | ~1e-10 BER; will not get that timing without clock forwarding | [1×: IA] |
| Grade | Nvidia A+; Intel C+ (B- if coddled) | [1×: IA] |
| Connector loss | 1.3 dB average, two lenses; periscope attach vs edge-coupling bench | [1×: IA] |
| 16-λ array SMSR | ~25 dB; mode-hop tolerance weak | [1×: IA] |
| 16-λ architecture | Not real 16-λ; Tx 8-λ buses (thermal crosstalk); Rx 3 cascaded MZIs + extra SOA | [1×: IA] |
| 16-λ BER (generous 0.2 UI) | 1e-5; two SOAs in path | [1×: IA] |
| Wavemeter plot | Yokogawa; excellent flatness; first λ off ±10 GHz; sidemodes suspiciously weak | [1×: IA] |
| Paper 20.1 | Deferred | [1×: IA] |
| NVDA/LITE architecture | Monolithic DFB array + per-channel SOA (amp + beam-shape); MOPA | [1×: IA] |
| Analog | Sivers / Ayar SuperNova class; IA hates monolithic DFB arrays (yield, spacing, reliability) | [1×: IA] |
| Output / inferred DFB | 100 mW per channel; DFB ~20 mW (13 dBm) run ~14 dBm | [1×: IA] [est.] |
| SOA gain | ~6 dB small-signal in saturation (RIN-min region) | [1×: IA] [est.] |
| FWM on this array | None — one λ per SOA | [1×: IA] |
| Die size / λ count | 2.25 mm × 1 mm InP; 9 wavelengths; yield "horrific" | [1×: IA] |
| TEC / facet | Single TEC (no thermal spacing control); AR coat on back facet | [1×: IA] |
| Isolators | One isolator for the entire array | [1×: IA] |
| Coupling rumor | LITE 0.5 dB — "too good to be true" | [1×: IA] |
| Package | ELSFP for initial characterization | [1×: IA] |
| Power variation / spacing / SMSR | Excellent | [1×: IA] |
| RIN | ~−137 dBc/Hz even after dropping the relaxation-oscillation channel; unusable | [1×: IA] |
| NVDA Research text | Cope; cannot use this monolithic array on a real link | [1×: IA] |
| WPE gate | Laser WPE 10% critical; below 10% system efficiency degrades exponentially | [1×: IA] |
| Power variation spec | < ±0.5 dB because ring self-heating, not primarily efficiency | [1×: IA] |
| Spacing spec | ±10 GHz on 200 GHz DWDM grid = crosstalk, not heater-power | [1×: IA] |
| Modulation / guard | 32G on 200 GHz grid → massive guard bands | [1×: IA] |
| TEC ΔT | Standard 10°C; 23°C model is runaway | [1×: IA] |
| Aeva SOA | Two Zn-doping designs; 22% PCE at 650 mW / 40°C | [1×: IA] |
| Aeva ASE / FIT | Noise floor 40 dB down; FIT < 5 | [1×: IA] |
| Seminex contrast | Named as the bad high-power SOA | [1×: IA] |
| LITE discrete RIN (prior) | < −155 dBc/Hz; CPO spec −145 dBc/Hz | [1×: IA / LITE public, 14 Aug] |
| OFC 2026 ELSFP WPE (prior) | Module 13% vs 10% industry target | [1×: IA, 14 Aug] |
| Paper IDs / IR $ | not in extractable prose (charts are images) | [gap] |

## Contradiction Check
**Supports [[Theses/NVDA - Nvidia]] §Networking / §Industry Context optical interconnects (Spectrum-X/Quantum-X CPO H2 2026; LITE $2B + Ayar + Fabrinet) and §Catalysts "Spectrum-X/Quantum-X CPO platforms ship H2 2026."** The new clause is *engineering grade*, not a ship-date: clock-forwarded bathtub at 1e-12 / 0.47 UI versus Intel's perfect-timing < 1e-12 claim. **Supports** NVDA §Risks #10 offset (own scale-up CPO lead / Kyber) — Intel SiPho publishing does not close the NVLink-durability risk, but it also does not create a merchant CPO peer on these plots. **Supports** the 13 Aug Spectrum-6 shipping note ([[Research/2026-08-13 - NVDA LITE AAOI TSM - Nvidia Spectrum-6 CPO Shipping - news]]) as the production calendar this paper does not restate. NVDA has **no `## Conviction Triggers` section** — nothing to fire; gap still open (Mental Models 2026-07-09). Conviction/status not edited.

**Touches, does not fire, [[Theses/LITE - Lumentum]] §Outstanding Question "How does Lumentum's role change under CPO, and does volume offset margin compression?" and §Bear Case / Risk #3 (CW DFB/ELS as the contestable layer).** The NVDA/LITE MOPA array is a co-integrated NPO experiment that **fails RIN** (~−137 dBc/Hz vs LITE's published discrete < −155 and vs −145 spec). That is evidence *for* the discrete UHP/CW path remaining the qualified layer, and *against* reading Hurlston's co-integrated-NPO commentary as "monolithic arrays are the product." The one-isolator BOM is the cost-save the 19 Jul primer said monolithic MOPA could not buy without on-chip isolation; here they bought it and still lost on RIN. WPE 10% matches the 14 Aug OFC ELSFP 13% vs 10% industry target. LITE has **no Conviction Triggers** — flag only. LITE is not currently in the live 17; keep on the ticker line because the paper is a LITE laser-physics print sitting under the NVDA CPO stack.

**Touches, does not fire, [[Theses/INTC - Intel]] §Conviction Triggers.** HIGH legs are 18A yield / Maia 2 / 14A roster / IFS $500M+$500M; LOW legs are 18A <70% / Maia-AWS cut / AMD EPYC 50% / IFS <$200M/qtr; CLOSE is 14A cancel / Coral Rapids / IFS loss / Paisner. None are photonics BER. Soft color on Jaguar Shores "silicon photonics interconnects" in §DCAI: the SiPho group is not dead, and it is not competitive with Nvidia CPO on these papers. Do not re-rate INTC on a C+/B- paper grade.

**Touches [[Theses/SIVE - Sivers Semiconductors]] §Conviction Triggers → HIGH if (b)** (hyperscaler-named CPO ELS qualification) — evidence-touched, **dir=LOW on the monolithic-array architecture**, not a fire. IA names "Seivers (Ayar Supernova)" as the class of DFB array he hates (yield, spacing, reliability) and then scores this NVDA/LITE instance unusable on RIN. That is not a Sivers PO, not a hyperscaler ELS qualification, and not CLOSE (d) Aeva LiDAR delay. Same direction as the 19 Jul primer / 25 Jul Aeva–Sivers GM math: device-interesting, CPO-ELS-as-product still a stretch. SIVE status monitoring / conviction low; flag only.

**No AEVA thesis.** Aeva SOA 22% PCE @ 650 mW / 40°C, ASE −40 dB, FIT < 5 **confirms** the 19 Jul "quite good / ~650 mW" device rating and does **not** convert it into a CPO ELS business (the 19 Jul 5–20% GM / 56+ alignment ceiling still binds). Seminex is the named negative comp.

**Adjacent:** [[Theses/AVGO - Broadcom]] (discrete CPO-laser peer in the 14 Aug four-plot book; not in this paper); [[Theses/IQE - IQE]] / [[Theses/TSEM - Tower Semiconductor]] (Openlight/Tower single-λ 20 mW as the Intel-hybrid foil); [[Theses/AAOI - Applied Optoelectronics]] → LOW "CPO ≥20% of NVDA+AVGO H2 2026 switch shipments" **untouched** (no share print). [[Sectors/Optical Networking & Photonics]] should take WPE 10% / RIN / SMSR / FWM as the CPO parametric gate on `/sync`.

**[G-1]/[G-13]** the variant perception is bathtub-at-UI and RIN, not "Intel papers exist" or "co-integrated NPO." **[G-10]** a 2.25×1 mm 9-λ InP die with −137 dBc/Hz RIN is the base-rate ugly-photon hack, not a second source. Cross-model agreement (every lens here flatters NVDA clock-forwarded CPO and LITE discrete UHP versus Intel shared-SOA and monolithic MOPA) is the cue to disconfirm. Single falsifying datapoint: Intel (or any shared-SOA comb) prints BER ≤ 1e-12 at 0.47 UI *without* perfect-timing cheesing, or the NVDA/LITE MOPA array prints RIN ≤ −145 dBc/Hz across channels without dropping the relaxation-oscillation lane. Secondary: a hyperscaler qualifies that monolithic array into Spectrum/Quantum/NPO volume. Tertiary: Aeva SOA + discrete DFB ships as a CPO ELSFP at incumbent GM. Do not write or edit any conviction/status field.

## Source Excerpts
> "Several people have asked me about Intel CPO/SiPho group this year and my default answer was “who cares they suffered massive attrition, got re-org-ed like 5 times and are dead”."

> "Intel is using an SOA to amplify all 8 modulated wavelengths. We are going to see RIN problems due to four-wave-mixing."

> "The SMSR is not 50 dB. This is a lie. Real number is 30 dB."

> "The BER of all channels is not < 1e-12."

> "At a (total, not +/-) sampling offset of 0.47 UI, all of the Intel CPO lanes would catastrophically fail. If Intel got 0.2 UI opening, they would hit 1e-10 BER."

> "If Nvidia is an A+, Intel just got a C+, maybe a B- if we want to coddle them."

> "Ok so its not real 16-lambda."

> "Remember Nvidia measured BER of 1e-12 at a 0.47 UI sampling offset and they are clock-forwarding. If I am very generous and set Intel’s results to 0.2 UI sampling offset, BER is at 1e-5."

> "Monolithic DFB laser array like Seivers (Ayar Supernova). I hate monolithic DFB arrays as a reminder. Yield nightmare."

> "What the fuck this entire thing only needs one isolator?!"

> "Even if we remove that, RIN will end up around -137 dBc/Hz which is shit."

> "Translation: This RIN is garbage and we cannot use this monolithic laser array."

> "Laser WPE of 10% is critical for making CPO/NPO make sense from an energy savings perspective. The burden is on the laser power efficiency and the system efficiency exponentially degrades as laser WPE drops below 10%."

> "Power variation (flatness of DWDM laser spectrum) hurts efficiency meaningfully but the real reason people want less than +/- 0.5 dB variation is ring-modulator self-heating."

> "Wavelength spacing accuracy of +/- 10 GHz (on 200 GHz DWDM grid) matters for optical crosstalk but is basically irrelevant for power efficiency."

> "40C is a reasonable operating point for datacenter applications. 22% PCE at 650 mW output power. Excellent."

> "Excellent flatness with ASE (noise floor) 40 dB down. Very very good."

> "FIT < 5 is good."
