---
publish: false
date: 2026-07-19
updated: 2026-08-14
tags: [research, Semiconductors, LITE, COHR, AEVA, Optics]
sector: Custom Silicon & Networking Semiconductors
ticker: LITE
propagated_to: [LITE]
source: 'https://irrationalanalysis.substack.com/p/practical-semiconductor-optical-amplifiers'
source_type: deep-dive
---

# Practical Semiconductor Optical Amplifiers for CPO/NPO

## Thesis Delta
Consensus prices UHP CPO/NPO lasers as a Lumentum/Broadcom volume race, and sell-side pings Aeva as a LiDAR-to-CPO re-rate once a 650 mW SOA exists → Irrational Analysis says the binding variables are cavity length (mode-hop + chips per InP wafer) and whether an isolator can sit between DFB and amplifier; discrete DFB + isolator + SOA is a starved-market kludge at 5–20% ELSFP GM versus incumbent 50–65%, not a substitute for short-cavity UHP DFB. [G-13] the mispriced operating variable is mode-hop-free cavity, not SOA milliwatts; [Semis #2] LITE/AVGO shorter-cavity linewidth is the qualification-gate hypothesis; [Semis #8] CPO remaps the bottleneck from EML to UHP CW; [VLM §1] Faraday isolators (Coherent ~60% world share [est.: IA]) are a second toll layer the discrete path must pay.

## Summary
Irrational Analysis treats Vikram Sekar's InP DFB physics as 90% correct and then adds two missing constraints that determine who can ship CPO/NPO-grade UHP lasers. A DFB is an active region that converts current to light plus gratings that recycle photons until they exit the last mirror. Mode-hop is death: most transceiver link flaps are laser mode hops, which is why vendors hunt "mode-up-free" slices of the LIV curve. Temperature moves wavelength harder than drive current — rule of thumb 0.1 nm/K — so an 8-λ ELSFP designed for 40°C still has each DFB sitting anywhere in a ±10°C window at hundredths-of-a-degree setpoints. Reliability is charge density in the cavity: a shorter cavity at the same output power raises density and burn-out risk. Mode-hop risk scales the other way, with cavity length. [[Theses/LITE - Lumentum]] and [[Theses/AVGO - Broadcom]] hit acceptable CPO/NPO linewidth at roughly the same short cavity; that is more die per InP wafer *and* lower flicker risk. Peers need ~60% longer cavities. That pair — chips/wafer plus mode-hop — is IA's answer to Vik's "alligator-filled moat" question, not a generic UHP brand ranking.

Default optical gain is not a semiconductor. C-band uses EDFA, O-band PDFA: long doped-fiber spools drawn as coils in block diagrams. Gain and noise figure are excellent; cost and physical footprint are not. A semiconductor optical amplifier is a DFB with the gratings deleted — noisier than EDFA/PDFA, tiny, and cheap relative to doped fiber. Power it with no seed and it dumps ASE (amplified spontaneous emission). Seed it and ASE falls. Traditional SOA jobs (long-haul, LiDAR) seed a weak signal, −25 to −5 dBm, and take 20–30 dB small-signal gain to ~13 dBm at most, typically one wavelength through the chip. That single-λ habit is the load-bearing constraint for CPO.

Four-wave mixing is the reason a multi-λ SOA is not a free lunch. Every amplifier adds input noise, driver noise, and nonlinearity; FWM is the optical version that appears in fiber after kilometres and inside an SOA almost immediately. Strength scales quadratic/cubic with input power and cavity length, and rises exponentially as channels pack tighter. Two wavelengths in do not become two louder wavelengths: conjugate junk spikes appear at the difference frequencies with flipped spectra. Useful if the job is wavelength conversion; fatal if the job is a clean multi-λ CPO comb. CW RIN is an integral from 10 MHz to Nyquist — the photodiode/TIA floor, not a cleanliness claim about DC. Traditional datacom only needs 20–100 mW. LiDAR wants 400 mW and above, so the high-power SOA catalogue lives at names pivoting off a failed sensor story. Five investors had already pinged IA on Aeva after sell-side picked up the SOA line. IA's device read is not the equity read: the Aeva SOA is "quite good" — ~650 mW, strong WPE, low ASE — and in theory a 20–100 mW discrete DFB plus that SOA prints a 400 mW CPO-viable source. The finance error is treating that schematic as a business.

Monolithic MOPA (low-power ~100 mW DFB, short waveguide, SOA, one InP die) already exists: Furukawa has a CPO/NPO part; Coherent is pivoting to MOPA after botching UHP DFB. Lumentum and Broadcom do not use it. InP area is higher. The binding failure is the parasitic cavity between DFB and SOA: any back-reflection into the gratings destabilizes the laser. Isolators are one-way Faraday gates (terbium-class, not InP) and cannot sit on a monolithic InP chip. Coherent makes ~60% of world isolators [est.: IA]. Discrete DFB + isolator + SOA breaks the mode-hop loop and is unused because of cost, not physics. A typical drawing shows four lenses and still omits the isolators; an isolator between DFB and SOA input is mandatory, output isolator skippable but "tricky." Every element — DFB, lens, isolator, SOA, fiber, PIC — wants active alignment on FiconTec-class tools to low-single-digit-micron and <2° angle. Napkin BOM for an 8-λ ELSFP on weak DFBs plus LiDAR-class SOA: 8× 20–100 mW DFB, 8× 400–650 mW SOA, 32–40 lenses, 8–16 isolators, 56+ alignments. Incumbent ELSFP GM 50–65%; the LiDAR-SOA path, partnered with TFC or Fabrinet, 5–20% at worse wall-plug efficiency. CPO/NPO is starved enough that functional photons still sell. Open ask: which InP fab Aeva uses (IA: "please let it not be CPFC") and SOA cavity length — both inputs to a COGS/yield model. Follow-on math that names Sivers as the Aeva InP partner lives in [[Research/2026-07-25 - AEVA AXTI Stranded InP SOA ELSFP Math - deep-dive]]; this primer does not name [[Theses/SIVE - Sivers Semiconductors]] or [[Theses/IQE - IQE]].

## Framework / Mental Model
**Amplifier class + MOPA vs discrete SOA (IA primer typology).** Five components, applied as a decision tree rather than a score:

| Component | Definition |
|---|---|
| Default amp | EDFA (C-band) / PDFA (O-band): doped-fiber spool; high gain, low noise, large and expensive |
| SOA | DFB minus gratings; noisy, small, cheap; ASE with no seed; traditional seed −25 to −5 dBm → ≤13 dBm, one λ |
| FWM constraint | Multi-λ through one SOA creates conjugate junk spikes; strength ↑ with power, cavity length, tighter spacing |
| Monolithic MOPA | 100 mW DFB + waveguide + SOA on one InP die; no on-chip isolator; mode-hop from the intra-chip cavity |
| Discrete DFB + isolator + SOA | Isolator kills back-reflection; cost is 4+ lenses, 8–16 isolators, 56+ active alignments on an 8-λ ELSFP |

Methodology: start from the required coupled milliwatts (20–100 mW traditional vs 400 mW+ CPO/LiDAR). If a vendor already holds short-cavity UHP DFB linewidth ([[Theses/LITE - Lumentum]], [[Theses/AVGO - Broadcom]]), skip the amplifier. If not, MOPA looks elegant and fails on isolator physics; discrete SOA works and fails on alignment COGS unless the market is so starved that 5–20% GM still clears. Outputs (cavity +60%, 650 mW, 56+ alignments, GM bands) sit in Evidence.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| IA vs Vik DFB recap | Agrees ~90%; adds reliability + mode-hop | [1×: IA] |
| Wavelength temp drift | ~0.1 nm/K | [1×: IA] |
| 8-λ ELSFP thermal window | Designed 40°C; operates ±10°C at 0.01°C setpoints | [1×: IA] |
| Reliability driver | Charge density in cavity; shorter cavity @ same power → higher density | [1×: IA] |
| Mode-hop driver | Risk scales with cavity length; most link flaps = mode hops | [1×: IA] |
| LITE / AVGO cavity vs peers | Acceptable CPO/NPO linewidth at same short cavity; peers ~+60% length | [1×: IA] |
| Short-cavity economic | More chips per InP wafer | [1×: IA] |
| EDFA / PDFA | C-band / O-band doped-fiber default; excellent NF; large + expensive | [1×: IA] |
| SOA definition | DFB without gratings; noisier; small; relatively cheap | [1×: IA] |
| ASE | Output with electrical bias and no optical seed; falls when seeded | [1×: IA] |
| Traditional SOA seed / gain / out | −25 to −5 dBm in; 20–30 dB SSG; ~13 dBm max | [1×: IA] |
| Traditional λ count into SOA | One wavelength in the vast majority of long-haul / LiDAR uses | [1×: IA] |
| FWM location | Fiber after km; SOA "very quickly" | [1×: IA] |
| FWM scaling | Quadratic/cubic in power and cavity length; exponential in tighter spacing | [1×: IA] |
| FWM output | Extra conjugate-phase junk spikes at the difference frequencies | [1×: IA] |
| FWM use-case | Wavelength conversion (blessing) vs multi-λ CPO comb (curse) | [1×: IA] |
| CW RIN band | Integral 10 MHz → Nyquist (PD/TIA floor) | [1×: IA] |
| Traditional datacom laser power | 20–100 mW | [1×: IA] |
| LiDAR / high-power SOA class | ≥400 mW; catalogue sits at pivoting LiDAR names | [1×: IA] |
| Aeva sell-side traffic | 5 investors had pinged IA | [1×: IA] |
| Aeva SOA rating | ~650 mW; "quite good" WPE and low ASE | [1×: IA] |
| Kludge schematic | 20–100 mW discrete DFB + Aeva-class SOA → ~400 mW CPO-viable | [1×: IA] |
| Monolithic MOPA | ~100 mW DFB + waveguide + SOA, one InP die | [1×: IA] |
| Named MOPA vendors | Furukawa (CPO/NPO part); Coherent pivoting after botched UHP DFB | [1×: IA] |
| Why LITE/AVGO skip MOPA | More InP area + unfixable intra-chip mode-hop (no on-chip isolator) | [1×: IA] |
| Isolator materials | Faraday / terbium-class; not InP | [1×: IA]; [web: coherent.com] |
| Coherent isolator share | ~60% of world | [est.: IA] |
| Discrete path must-have | Isolator between DFB and SOA input; output isolator optional/"tricky" | [1×: IA] |
| Alignment spec | Low-single-digit µm; <2° angle; FiconTec or custom | [1×: IA] |
| 8-λ ELSFP napkin (SOA path) | 8× 20–100 mW DFB; 8× 400–650 mW SOA; 32–40 lenses; 8–16 isolators; 56+ alignments | [est.: IA napkin] |
| Incumbent ELSFP GM | 50–65% | [est.: IA] |
| LiDAR-SOA ELSFP GM | 5–20%; worse WPE; TFC or Fabrinet as OSAT | [est.: IA] |
| Why the ugly path still ships | CPO/NPO "so starved that any functional supply will sell" | [1×: IA] |
| Open COGS inputs | Aeva InP fab (not CPFC?); SOA cavity length | [1×: IA] |

## Contradiction Check
**Supports [[Theses/LITE - Lumentum]] §Summary (physics-gated InP / arms-dealer) and §Key Non-consensus Insight on butt-joint / process mastery over wafer diameter.** IA's added claim is that the CPO/NPO qualifier is short-cavity linewidth (chips/wafer + mode-hop), not a brand-level UHP ranking. That is the same family of gate as the later LIVT-width argument in [[Research/2026-08-12 - LITE Irrational Analysis Q4 FY26 Call Alpha - deep-dive]]. [Semis #2] hypothesis: peers at +60% cavity cannot copy the shrink without already holding the linewidth statistic. [G-6] / [VLM §1] the rent sits in the cavity, not in the SOA die.

**Challenges [[Theses/LITE - Lumentum]] §Bear Case (CPO migrates value to a "relatively standardized and commoditized" CW DFB/ELS layer) and §Risk #3 / §Outstanding Question "how does Lumentum's role change under CPO, and does volume offset margin compression?"** IA's answer is that CW UHP is *not* datasheet-commoditized: cavity length is the gate, and the SOA overflow path clears only at 5–20% GM with 56+ alignments. Volume of ugly photons does not replace 50–65% ELSFP rent. Single falsifier for this support: a peer (Coherent MOPA, Furukawa, or a Chinese CW house) matching LITE/AVGO cavity at held CPO linewidth, or UHP DFB supply normalizing so the 5–20% path never books.

**Challenges [[Theses/SIVE - Sivers Semiconductors]] §Key Non-consensus Insight (only listed ELS overflow / 4-inch is a temporary cost handicap) and §Bull Case (photonics 80–120% as CPO ELS; Aeva LiDAR $53–138M).** This primer never names Sivers. It does rate the Aeva-class SOA as device-good and product-bad: active-alignment hell, isolator BOM, 5–20% GM. That is a ceiling on using Aeva SOA (and whoever fabs it) as a CPO ELS substitute. [[Theses/SIVE - Sivers Semiconductors]] §Conviction Triggers → HIGH requires a hyperscaler-named CPO ELS qualification; this source is the mechanism by which a LiDAR SOA partnership can look like that qualification without clearing module economics. [G-10] base rate: LiDAR names "pivoting" into datacom do not inherit incumbent GM. Follow-up [[Research/2026-07-25 - AEVA AXTI Stranded InP SOA ELSFP Math - deep-dive]] later names Seivers as the Aeva InP partner and prints ~17% vs ~51% GM — same direction, tighter numbers.

**[[Theses/IQE - IQE]] §Key Non-consensus Insight (SiPh paradox / InP epi demand) and §Industry Context InP gap.** Discrete DFB + SOA consumes *more* InP area than a short-cavity UHP DFB (two chips, plus the SOA cavity IA wants to measure). That is volume-positive for independent epi if the kludge ramps; it is not a pricing-power print for IQE. [Semis #1] the binding shortage IA is describing is qualified UHP DFB die, not generic InP starts — MACOM marking IQE at 19.8p rather than buying the company remains the outside-view check.

**[[Theses/NVDA - Nvidia]] §Catalysts (Spectrum-X / Quantum-X CPO H2 2026) and §Risks (photonics stakes as platform envelopment).** Starved CPO/NPO is why NVDA paid to lock LITE/COHR laser lines. This source says the lock is on short-cavity UHP DFB, not on a LiDAR SOA second source; Coherent's MOPA pivot after a botched UHP DFB is the dual-source hedge with a mode-hop asterisk. [Semis #8] / [Semis #10] architecture shift plus anchor allocation: functional SOA supply can fill a hole at 5–20% GM without moving NVDA's qualified laser stack. Falsifier: NVDA (or a hyperscaler) qualifies an Aeva-class discrete-SOA ELSFP into Spectrum/Quantum volume.

**Disconfirming check.** Every lens here flatters LITE/AVGO short-cavity and punishes Aeva-as-CPO — READING PROTOCOL cue to hunt the other side. Steelman: if isolator+alignment COGS falls (passive alignment, fewer lenses, shared collimators) or if monolithic MOPA reliability is solved with on-chip isolation workarounds, the 5–20% path becomes a real second source and the cavity moat is just a cycle. Base rate the thesis must beat: ugly, low-GM photon hacks do ship in shortages and then die when primary capacity unlocks ([Semis #18] cycle vs structural). Dated watch: Aeva fab identity + SOA cavity length (IA's own COGS keys); Coherent MOPA field reliability; LITE/AVGO cavity still ~60% shorter at the next power node.

## Source Excerpts
> "Lumentum and Broadcom can achieve acceptable linewidth for CPO/NPO applications at around the same cavity length. Not only does this save them money (more chips per InP wafer), it also drastically reduces mode-hop risk. All competitors need around 60% longer cavity length which makes the lasers at far higher risk of mode-hop/instability."

> "Mode-hop risk (how likely the laser is to flicker) scales with cavity length."

> "The Aeva SOA is quite good. Rated to about 650 mW output power with excellent properties (WPE, low ASE)."

> "You can’t have an isolator on a monolithic InP MOPA chip because of manufacturing limitations. The isolators are made of materials not InP."

> "If we call Broadcom and Lumentum module-level (ELSFP) gross margins at 50-65%, I can see a half-dead LiDAR shitco partnering with TFC or Fabrinet to sell the same thing with worse power efficiency at 5-20% gross margin."
