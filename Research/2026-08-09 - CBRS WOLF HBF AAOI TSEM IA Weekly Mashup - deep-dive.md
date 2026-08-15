---
publish: false
date: 2026-08-09
updated: 2026-08-14
tags: [research, Semiconductors, AAOI, TSEM, LITE, HBF, CBRS]
sector: Optical Networking & Photonics
ticker: LITE
propagated_to: [CBRS, LITE]
source: 'https://irrationalanalysis.substack.com/p/cbrs-update-wolfnvts-lawsuit-hbf'
source_type: deep-dive
---

# CBRS Update WOLF NVTS Lawsuit HBF

## Thesis Delta
Consensus prices [[Theses/CBRS - Cerebras Systems]] WSE-4 as a gen-4 architecture/decode-speed print, [[Theses/SNDK - SanDisk]] HBF as a NAND-scarcity TAM option with HBM-like I/O, [[Theses/AAOI - Applied Optoelectronics]] as a CPO-laser + Western-transceiver compounder, Tower as one of two interchangeable merchant SiPh foundries versus GF, and SemiAnalysis-adjacent notes as treating micro-LED and micro-VCSEL as peer slow-and-wide paths → Irrational Analysis (IA) reads WSE-4 as a **gen-3.5 power-delivery / parametric-yield** event (Feldman "doubling clocks" = voltage-domain/ripple fix, not a new node), HBF as a NAND-PHY-limited spec that **might work but is not optimal**, AAOI CPO lasers as **2–3 year cope** without public linewidth/phase-noise at full power / 50°C / ELSFP driver (high-power CPO = [[Theses/AVGO - Broadcom]] + [[Theses/LITE - Lumentum]] duopoly), Tower Openlight + 300 mm SiGe as the real foundry/amp read, and micro-LED as a **0% share physics dead-end**. Trading color only. [G-13] the operating variables are parametric yield, NAND-PHY speed, and laser phase noise — not the WSE-4 slide, the HBF TAM, or the AAOI CPO narrative. [Semis #2]/[#8] qualification-gate and architecture-remap hypotheses.

## Summary
IA's week is nine loosely coupled engineering notes, not a single thesis. The binding claim across the optics half is that **public linewidth, phase-noise, BER, and insertion-loss plots** are the only admissible evidence; marketing slides, OFC/OCP live demos without those plots, and sell-side notes that put a hoax technology next to a working one are treated as fraud-adjacent. The compute half is a yield-and-I/O interrogation of Cerebras plus a spec walk of HBF that walks back IA's prior "never works" to "solution looking for a problem."

**Cerebras.** A WSE-4 event is due the same month. IA's inbound is that this is gen **3.5**, not gen 4: most of the work is **power delivery and clocks**. Feldman has been telling finance people he is "doubling the clocks with new power delivery." IA's prior 20% final-yield model [est.] had always killed the wafer at **packaging** (crack, warp). Defect yield is dismissed as easy — 100% of wafers pass stage 1 via NoC + spare cores — and Feldman quoting that number is treated as a tell that he is steering the conversation off stages 2–3. The new read: maybe they **never solved parametric yield**. Too few voltage domains or dirty ripple leave an untunable wafer; cleaner delivery (IA names [[Theses/VICR - Vicor Corporation]] as the possible partner) lets them tune die-by-die the way a conventional wafer map is tuned, and clock doubling is the side-effect of a now-legal shmoo. Disagg rumors are published as unvalidated bait: Cerebras+Trainium "allegedly going very well"; Cerebras+Blackwell "making progress via a third party"; Cerebras+MI450 "fake" (slide made last-minute, engineering not started). IA's own prior is that prefill/decode disagg is **impossible** on published WSE I/O latency ("< 5 µs" vs the 100s-of-ns programmers complain about). The Feldman interrogation list is the investable artifact: why clocks; cleaner ripple vs more voltage domains; packaging vs parametric; cut him off if he returns to defect routing; if he claims yield is good, force GM / COGS / ASP to reconcile with the 20% model; relative yield lift on the new gen; does ASP rise or is capacity already contracted.

**WOLF vs NVTS.** Wolfspeed sued Navitas. IA tours six patents in the press release. The first is **GaN transistors** even though Wolfspeed sells no GaN product, substrate, or epi, and that patent is expected to **expire in ~4 months**. Two chemistry patents get no engineering comment. One patent is called "stupid from an engineering perspective" with no legal view attached. The last is **SiC-specific**; IA's engineering verdict is that all Navitas SiC products are "utter dogshit," so Wolfspeed is fine on that claim. Color, not a vault name.

**HBF.** IA had been "very anti HBF" and now softens to **might-work-not-optimal**. Motive check: a subset of HF NAND bulls want HBF so the trade-ratio sucks NAND bits out of commodity supply the way HBM sucked DRAM; they claim to care about the spec. Public spec is ~130 pages, ~10 interesting. Everyone already has **UCIe 64G** PHYs; those will be qualified in ~6–9 months. HBF just published, so its base die **lags** 64G — and the spec still **omits 64G** and lists a "horrendous slow **8G**" UCIe option. IA's inference: something else in the system (NAND PHY) is the speed limit, and the authors are worried enough to standardize the crawl. Synchronous UCIe channels are clock-forwarded, so they do not fix it. Traditional SSD NAND controllers run hot; some of that digital math was cut. FMS booth: Sandisk employees gave "good answers" on base-die heat after ~5 minutes of probing. Host must supply a **REFCLK** separate from UCIe clock-forwarding for the NAND PHYs; SSC is accepted because the NAND PHY is EMI-sensitive; PPM/jitter look trash because the clock is forwarded. Reliability numbers are all "product specific." Floorplan: 16 copies of UCIe, 64 lanes each, grouped in blocks of four to mitigate crosstalk. Net: IA keeps the same stacking-is-bad argument used against HBM and still prefers **good I/O + fan-out**.

**Aeva / Taalas.** Aeva launched an optical-connectivity business and signed a first customer. IA's prior joke post had floated Aeva's SOA as an NPO/CPO high-power amp. Guess on the customer: **Innolight**. Mid-write confirmation: Innolight, with the hyperscaler **suspected Amazon**. Read-through is the high-power laser / SOA shortage → long [[Theses/LITE - Lumentum]]. Taalas (bought by [[Theses/AMD - Advanced Micro Devices]]) burns model weights into **upper-metal masks**. Leading-edge nodes have 14–18 metal layers; foundries already hold wafers mid-stack so a single-mask edit is cheaper than a full tape-out. Model → chips ~**2–3 months**; Ljubisa claimed **one week** to verify a new weight encoding via EDA-like wrappers that IA analogizes to FPGA LUT mapping. IA told them the product would fail because models update weekly. Public AMD marketing is datacenter AI; IA's meeting residual is **FPGA / niche embedded**, not a disagg-inference solution like Nvidia/Groq.

**AAOI call.** The only story IA will underwrite is **Sugar Land transceiver ramp** at 800G+ with yield. CEO talk of high-power CPO/NPO lasers is read as cope. OFC live demo: **no linewidth**. Lumentum's live demo claimed **0.5 MHz** and Lumentum has published phase-noise and lineshape repeatedly. IA's demand: β-separation effective linewidth at **full power, 50°C, on a small-footprint switching-regulator / ELSFP-compatible driver** — not intrinsic linewidth, not a bulky lab driver. CEO is granted two points: hyperscalers were already moving off Chinese transceivers, and most Chinese laser houses cannot do a **300 mW DWDM** laser. IA's addendum: **AAOI cannot either**. High-power CPO laser market = Broadcom + Lumentum. Coherent has nothing. AAOI has nothing and is **2–3 years** away. Coherent maybe **~18 months** if MOPA is stable.

**Tower call.** Openlight add-on PDK: **20 mW-class** lasers and SOA. As InP gets scarcer, Openlight/Tower hetero transceivers become more attractive on InP **area efficiency** if yields hold. NPO raises Tower content even without advanced packaging: the SiPho PIC is larger; CWDM/DWDM muxing arrives; even single-λ NPO may want a longer MZI for extinction ratio, or a shorter MZI for insertion loss with wider modulator pitch against thermal crosstalk. Russell's GF dunk uses **waveguide insertion loss** as the metric. IA: GF OCI MSA SCALE is empty; Tower crushes GF on insertion loss, bandwidth, frequency-response smoothness, process control, PDK quality, hybrid integration, advanced packaging, and support. Aside: **300 mm SiGe** expansion is for TIA / drivers / CTLE (Semtech / Marvell / Macom). Hyper-bullish Semtech read-through.

**Micro-LED jihad + book.** SemiAnalysis put micro-LED and micro-VCSEL in the same note with comparable 2030 shares (IA cites **27% micro-LED / 35% micro-VCSEL**). IA's recap of OCP March 2026: Coherent **106G PAM4** VCSEL NPO is a good demo, not yet at IA's conference bar of **1e-9 all lanes** for PAM4 (needs FEC); implied optimal VCSEL NPO/CPO rate is **32–64G NRZ**, and 53 Gbaud PAM4 is evidence Coherent can hit that slow-and-wide window. Lumentum 32G VCSEL NPO: no BER, ugly eyes, speckle from amplitude noise that IA attributes to **packaging / electrical crosstalk**, not the VCSELs; estimated **1e-9 to 1e-10** vs a no-FEC bar of **1e-12 all channels** (ideally 1e-14). Optics people want 32G (easier VCSEL/driver); electrical people want 64G (fewer lanes, less crosstalk). Dream: direct-drive via UCIe with sidebands and clock forwarding. Avicena (IA: "Avicina") live demo: **4G NRZ**; best group **7e-9**, worst **7e-5**, typical **~1e-7**. That fails even **RS(544,514)** used on 112G/224G PAM4 Ethernet. MediaTek private "demo" was slides; the same earnings call discusses ring-based SiPho on TSMC COUPE and **does not mention LED**. Credo micro-LED "not going well," evaluating a micro-VCSEL pivot. Physics: LEDs are incoherent; phase noise / jitter is the speed limit; burst errors come from jitter not amplitude noise; a hypothetical 8G breakthrough is still too slow because electrical crosstalk from dense TIAs kills the link below ~32G/lane; chromatic dispersion is catastrophic (IA "generous" reach **<10 m**, practical **1–2 m**). Single-emitter data is treated as concealment of array crosstalk. Lumentum GR-468 is **assembly-level**, not device-level. Micro-VCSEL is better on every axis except cost, and cost does not save a broken link. Trading snapshot labeled **8/8/25**: wants more [[Theses/AEHR - Aehr Test Systems]] / WOLF / AXTI, keeps ≥10% overnight buying-power buffer, small NVDA options as Gavin Baker solidarity, ~$100K CBRS shares covered (wrote calls, ~5%/week IV; assigned at $250 → recycle into AXTI/WOLF/AEHR), one uncovered share as the "activist" Feldman campaign. Might turn bullish on CBRS if the event shows real progress.

## Framework / Mental Model
**Three-stage yield (IA, applied to wafer-scale).** Explicit typology reused as an interrogation script, not a scorecard.

| Stage | Question | IA prior on WSE | Feldman tell |
|---|---|---|---|
| 1 Defects | Does the chip function? | 100% pass via NoC + spare cores | Quotes this number to imply "high yield" |
| 2 Packaging | Does the chip survive packaging? | Where the 20% final-yield model died (crack, warp) | Avoided |
| 3 Parametric | Target speed at acceptable V / P? | Assumed solved (enough knobs) | "Doubling clocks with new power delivery" = maybe this was never solved |

Methodology: ignore stage-1 claims; force stage 2 vs 3; reconcile any "good yield" claim to GM / COGS / ASP. Clock doubling is scored as a **parametric** side-effect (cleaner ripple, more voltage domains, die-level tune + Vicor) until Feldman answers the list.

**No-FEC / FEC BER bar (IA, applied to slow-and-wide optics).**

| Link class | Conference / product bar | Implication if missed |
|---|---|---|
| PAM4 VCSEL (needs FEC) | ≥ **1e-9** all lanes at a show (cherry-picked T/V) | Not robust enough for mass deployment |
| Slow-and-wide NRZ, no FEC | **1e-12** all channels min; **1e-14** for margin | Any worse → light FEC → the no-FEC bull case collapses |
| Micro-LED @ 4G NRZ (Avicena live) | Typical **~1e-7**; best 7e-9; worst 7e-5 | Fails RS(544,514); needs heavy DSP/FEC; not a peer of micro-VCSEL |

Methodology: demand **full-array** BER, phase-noise, and lineshape; reject single-emitter plots; reject intrinsic linewidth measured on a bulky lab driver.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| WSE-4 generation (IA inbound) | Gen 3.5 (power + clocks), not gen 4 | [1×: IA] |
| Feldman claim | "Doubling the clocks with new power delivery" | [1×: IA] |
| Cerebras final yield (IA model) | ~20%; death previously assumed at packaging | [est.] [1×: IA prior posts] |
| Stage-1 (defect) yield (IA) | 100% of wafers | [est.] [1×: IA] |
| Published WSE I/O latency | < 5 µs | [1×: IA / CBRS public] |
| Programmer-complaint latency | 100s of ns | [1×: IA] |
| Disagg rumor: Trainium | "Allegedly going very well" | [1×: IA rumor] |
| Disagg rumor: Blackwell | Progress via third party | [1×: IA rumor] |
| Disagg rumor: MI450 | Slide last-minute; engineering not started | [1×: IA rumor] |
| WOLF–NVTS GaN patent | Expires ~4 months; WOLF sells no GaN | [1×: IA / WOLF PR] |
| WOLF–NVTS SiC patent | NVTS SiC "dogshit" (engineering, not legal) | [1×: IA] |
| HBF spec length | 130 pages; ~10 interesting | [1×: IA] |
| UCIe 64G status | Already running; fully qualified ~6–9 months | [est.] [1×: IA] |
| HBF UCIe options | Includes 8G; omits 64G | [1×: HBF spec / IA] |
| HBF UCIe floorplan | 16 × UCIe, 64 lanes each, groups of 4 | [1×: HBF spec / IA] |
| HBF host clock | Separate REFCLK for NAND PHYs; SSC for EMI | [1×: HBF spec / IA] |
| HBF reliability | "Product specific" — no numbers in spec | [1×: HBF spec / IA] |
| HBF verdict (IA update) | "Might work but is not optimal or even good"; fan-out > stack | [1×: IA] |
| Aeva first optical customer | Innolight (confirmed to IA mid-write) | [1×: IA edit] |
| Aeva hyperscaler (suspected) | Amazon | [est.] [1×: IA] |
| High-power laser / SOA | "Shortage is really bad" → long LITE | [1×: IA] |
| Taalas cycle time | Model → chip ~2–3 months | [1×: IA / Taalas meeting] |
| Taalas weight-encode verify | 1 week (Ljubisa claim) | [1×: IA meeting] |
| Metal stack | 14–18 layers on 7 nm-class and below | [1×: IA] |
| Taalas use-case (IA) | FPGA / niche embedded, not DC AI disagg | [est.] [1×: IA] |
| Lumentum OFC linewidth claim | 0.5 MHz + public phase-noise / lineshape | [1×: IA] |
| AAOI OFC CPO laser demo | No public linewidth / phase-noise | [1×: IA] |
| High-power CPO laser set | Broadcom + Lumentum duopoly; COHR none; AAOI none | [est.] [1×: IA] |
| 300 mW DWDM laser | Most Chinese houses cannot; IA: AAOI also cannot | [1×: IA] |
| AAOI CPO laser timing | 2–3 years | [est.] [1×: IA] |
| COHR MOPA timing | ~18 months if stable | [est.] [1×: IA] |
| Required AAOI plot | β-separation effective LW @ full power, 50°C, ELSFP-footprint switching-regulator driver | [1×: IA] |
| Tower Openlight | 20 mW-class lasers + SOA; InP area-efficiency if yield holds | [1×: IA / TSEM call] |
| NPO PIC | Larger than pluggable; mux + MZI length / pitch trade | [1×: IA] |
| GF OCI MSA SCALE | "Don't have anything"; Tower wins insertion loss + PDK + hybrid + packaging | [1×: IA] |
| 300 mm SiGe | TIA / drivers / CTLE; Semtech "best stuff" | [1×: IA / TSEM call] |
| Coherent VCSEL NPO | 106G PAM4 (53 Gbaud); not yet 1e-9 all lanes | [1×: IA / OCP Mar 2026] |
| Optimal VCSEL NPO/CPO rate (IA) | 32–64G NRZ | [est.] [1×: IA] |
| Lumentum 32G VCSEL NPO | No BER; eyes noisy; IA ~1e-9–1e-10; packaging/xtalk not VCSEL | [est.] [1×: IA] |
| No-FEC BER bar | ≤1e-12 all lanes (1e-14 margin) | [est.] [1×: IA] |
| Avicena micro-LED | 4G NRZ; best 7e-9; typical ~1e-7; worst 7e-5 | [1×: IA live demo] |
| RS(544,514) | Avicena BERs would fail this FEC | [1×: IA] |
| Micro-LED reach | <10 m "generous"; practical 1–2 m | [est.] [1×: IA] |
| SA 2030 share (IA cite) | Micro-LED 27% / micro-VCSEL 35% — IA: LED should be 0 | [1×: IA / SA note] |
| MediaTek | Ring SiPho on TSMC COUPE on earnings call; zero LED mention | [1×: IA / 2454 call] |
| Credo | Micro-LED struggling; evaluating micro-VCSEL pivot | [1×: IA rumor] |
| IA book (labeled 8/8/25) | Add AEHR / WOLF / AXTI; ≥10% BP buffer; NVDA options; $100K CBRS covered @ ~5%/wk; assign $250 | [1×: IA snapshot] |

## Contradiction Check
**[[Theses/CBRS - Cerebras Systems]] §Outstanding Question 4 ("Does WSE-4 fix wafer-scale's capital-efficiency problem?") and §Conviction Triggers → LOW (Rubin+Groq decode within ~3×).** IA does not answer Q4's 3D-SRAM / $/token test. It **re-opens the yield identity**: the 20% model [est.] may have been **parametric**, not packaging, so a clock-doubling event is a Vicor/ripple print, not a decode-architecture print. Supports the thesis's own [Semis #2] **non-fire** (speed is not a qualification gate) and [Semis #10] single-anchor fragility: if GM/COGS/ASP cannot reconcile with "good yield," the hardware unit-economics question (Outstanding Q3) stays open. Disagg rumors are **not** evidence for Insight #3 (SRAM-only decode correctness); IA's prior is that <5 µs I/O **blocks** prefill/decode split. Trainium-going-well, if later confirmed, would be a **layer-renter** outcome (AWS owns the interface). MI450-as-slide, if true, weakens any AMD-paired narrative. Falsifier IA himself names: Feldman walks the interrogation list and shows packaging-not-parametric death, or GM/ASP that only work at high yield. Event is the near-term check; IA's own book is covered-call rental, not a high-conviction long.

**[[Theses/SNDK - SanDisk]] §Insight #1 (HBF as TAM-creation / missing-middle) and §Outstanding Question "Optane graveyard."** Challenges the first-mover/TAM-creation tone. IA's spec read is that **NAND PHY, not UCIe**, is the binding constraint (8G option, 64G omitted), reliability is unspecified, and stacking inherits every HBM argument IA already rejected. Softens only from "never" to "might work, not good"; preferred architecture remains fan-out I/O. **Supports** the later thesis update that HBF is co-led / not owned and that NVIDIA can route around on-package flash ([Semis #8]/[#13], [G-10] Optane base rate). Does **not** speak to SNDK's 78% GM print or NBM contracts. Falsifier: a hyperscaler capacity-tier socket ships HBF at UCIe 64G with disclosed reliability, or the 8G option is documented as a test/bring-up lane rather than a PHY limit.

**[[Theses/AAOI - Applied Optoelectronics]] §Summary / Insight #1 (InP fab does not protect 1.6T; merchant EML) and §Outstanding Question "CPO before 1.6T capex pays back" plus LOW trigger (CPO ≥20% of NVDA+AVGO switch shipments).** Supports the layer-renter read and **tightens** it: CEO CPO-laser talk is cope; the investable AAOI variable is **Sugar Land 800G+ transceiver yield**, not a laser qualification gate. Challenges any residual "Western Innolight that can also sell CPO lasers" narrative. High-power CPO = LITE+AVGO; AAOI 2–3y and no public LW/PN. Does **not** print the GM 29–30% vs 33% HIGH trigger; IA is "done" trading the ticker on the call's laser pivot, which is color, not a vault conviction change. Falsifier: AAOI publishes β-separation effective linewidth at full power / 50°C / ELSFP-footprint driver that matches Lumentum's public 0.5 MHz-class data.

**[[Theses/LITE - Lumentum]] §Insight (SiPh paradox / arms-dealer) and §Bear Case "CPO margin compression — CW DFB relatively standardized."** Supports the shortage/duopoly side: Aeva→Innolight (Amazon suspected) is a SOA/high-power **customer** print, not a LITE displacement; IA's explicit trade is long LITE. Challenges the bear's "standardized CW" leg the same way [[Research/2026-08-12 - LITE Irrational Analysis Q4 FY26 Call Alpha - deep-dive]] does: **phase-noise / linewidth at the ELSFP driver** is the gate [Semis #2], and Lumentum already publishes it. Nuance: Lumentum's own 32G VCSEL NPO demo **fails** IA's 1e-12 no-FEC bar (packaging/xtalk, path to fix); Coherent's 106G PAM4 VCSEL demo is the better slow-and-wide exhibit. VCSEL NPO is a **side** path; the load-bearing LITE claim in this post is **high-power CPO laser**, not VCSEL.

**[[Theses/TSEM - Tower Semiconductor]] §Insight #3 (hedged across architectures, does not own the standard) and §Insight #2 (59% incremental GM / qualification).** Supports merchant-foundry quality vs GF (insertion-loss dunk; Openlight 20 mW + SOA as InP-area hedge) and the NPO-larger-PIC content argument. Does **not** name the $1.3B 2027 book, $290M prepay, or 59% incremental GM — so it does not move TSEM Conviction Triggers (HIGH needs ≥$1.0B 2028 NI and ≥32% 2026 GM). 300 mm SiGe is a Semtech/Marvell/Macom amp read, not a SiPho-wafer print. Falsifier: GF OCI MSA ships a process that matches Tower insertion loss / PDK, or Openlight yields fail as InP shortage tightens.

**[[Theses/VICR - Vicor Corporation]] §Mental Models (CBRS as lead VPD customer; gen-2 VPD samples Q1 2027).** IA's "maybe they (+Vicor) figured it out" is a **hypothesis** that WSE-4 power delivery is a Vicor parametric-yield product, not a socket win at NVIDIA. Supports the thesis split (toll vs socket) only as adjacency. Falsifier: WSE-4 teardown / vendor disclosure names a non-Vicor VPD stack.

**[[Theses/AMD - Advanced Micro Devices]] §Insight #2 (full-stack vs GPU-only).** Taalas-as-FPGA/embedded **challenges** any "datacenter AI inference acquisition" marketing read; MI450-slide rumor, if later confirmed, is adverse to Helios-timeline confidence. Neither is a conviction-trigger print.

**[[Theses/AEHR - Aehr Test Systems]]** — IA wants to add size; no technical claim in this post. Not a contradiction.

Cross-model agreement (LITE duopoly, AAOI layer-renter, micro-LED 0, HBF not-good) is the cue to disconfirm [G-10]: the single falsifying datapoint on the optics half is a third party shipping a high-power CPO laser with public ELSFP-driver linewidth that matches LITE/AVGO; on HBF it is a 64G UCIe base die with published reliability; on CBRS it is a Feldman walkthrough that makes GM and 20% yield mutually exclusive.

## Source Excerpts
> "Maybe the way to read into Andrew Feldman’s claims of 'doubling the clocks' is they fixed parametric yield and as a side effect can double clocks."

> "I am willing to now soften my view from 'HBF is garbage and will never work' to 'this is a solution looking for a problem that might work but is not optimal or even good'."

> "High-power CPO laser market is Broadcom and Lumentum duopoly. Coherent has nothing. AAOI has nothing."

> "WHAT IS YOUR BETA-SEPERATION EFFECTIVE LINEWIDTH AT FULL POWER, 50C, USING A SMALL-FOOTPRINT SWITCHING-REGULATOR BASED LASER DRIVER?"

> "Typical group at lets call it 1e-7. … you need MINIMUM 1e-12 on EVERY SINGLE LANE IN EVERY SINGLE GROUP to run no FEC links."

> "MICRO-LED IS A 0. IT DOES NOT WORK. IT WILL NEVER WORK. … MICRO-VCSEL IS BETTER IN EVERY WAY EXCEPT COST. BUT IT CAN WORK!"
