---
publish: false
date: 2026-08-14
tags: [research, OpticalNetworking, COHR, LITE, AVGO, AIXA]
sector: Optical Networking & Photonics
ticker: COHR
source: 'https://irrationalanalysis.substack.com/p/coherent-q4-fy26-earnings'
source_type: deep-dive
propagated_to: [LITE, AAOI]
---

# Coherent Q4 FY26 — Irrational Analysis (vs Lumentum)

## Thesis Delta
Consensus and sell-side price Coherent's Q4 FY26 print as a mix miss — more transceivers, less lasers — and still treat 6-inch InP as a structural cost/yield lead over [[Theses/LITE - Lumentum]] → Irrational Analysis says the only way the numbers work is bad yield, the CPO laser is "dogshit," and Lumentum is redesigning lasers smaller to lift yield/GM while publishing 50°C CPO laser plots (RIN < −155 dBc/Hz, 80% CPO-laser GM) that Coherent refuses to match. The market assumption that is wrong: wafer diameter = yield = cost winner. [G-13] the operating variable is yield at a named datarate / power class, not CapEx–FCF–GM–growth comps; [Semis #2] CPO laser parametric yield is the qualification gate. No [[Theses/COHR]] note exists — the investable delta sits on LITE (and the LITE/COHR pair in [[Sectors/Optical Networking & Photonics]]). LITE has no `## Conviction Triggers` section to touch.

## Summary
Irrational Analysis (14 Aug 2026) is the Coherent half of the same-week Lumentum pair ([[Research/2026-08-12 - LITE Irrational Analysis Q4 FY26 Call Alpha - deep-dive]]). Lumentum's call was "ultra bullish"; Coherent's "was crap and so were their numbers." The transceiver-mix excuse does not close the gap: Lumentum is shrinking laser dies to raise yield and gross margin in "the greatest optics bull market since the telco bubble," while Coherent "financially self immolates." Finance desks compare the two on CapEx, FCF, gross margin, and revenue growth and cannot explain the divergence. Every analyst is asking the same yield question in a different wrapper. Morgan Stanley's leading form: is the "miniscule" GM expansion vs Lumentum mix, or 6-inch yield? IA's answer: "THE ONLY WAY THE NUMBERS MAKE SENSE IS IF YIELD IS BAD."

The call color IA flags (screenshots in the source; OCR not in the clip — see skill-gap) includes PhotonLink as a possible brand for Coherent VCSEL CPO/NPO, and management talk of 200G PAM4 on VCSEL. IA's engineering rebuttal: the optimal VCSEL NPO/CPO datarate is 32G NRZ or 64G NRZ; 200G PAM4 on a VCSEL fails GR-468 reliability, and even if it passes, energy efficiency is bad (driver complexity, FEC for crosstalk, Rx TIA sensitivity). You cannot cut power/latency by eliminating FEC if each lane is 200G PAM4. The CPO dream is direct-drive with UCIe or similar clock-forwarded die-to-die SerDes. Coherent "has great VCSELS, second only to [[Theses/AVGO - Broadcom]]" — the architecture, not the die, is the miss. Jim Anderson's "WE SELL MORE THAN LASERS" is read as cope: Lumentum takes ~80% GM on the CPO laser; Coherent sells isolators and FAU at ~30–40%.

The rest of the post is a reusable CPO-laser yield model, not a P&L recap. Section 2 is a 6-inch InP conspiracy: 6-inch *should* yield better (new [[Theses/AIXA - Aixtron]] MOCVD, semi-modern ASML litho vs ancient no-name tools) — so why is Coherent's yield still bad? Hypothesis: the 6-inch InP *wafers* have bad uniformity. AXTI (best substrate house) does not ship 6-inch InP; that is still R&D. Blame may sit with Sumitomo; AXTI 6-inch shipments would be the unlock. Section 3 walks Lumentum's *public* CPO laser four-plot (50°C, pessimistic): 400 mW drive current 1.2–~1.38 A; PCE 21–24% (peak at 150–200 mW); target 25–30% hit at 40°C; OFC 2026 ELSFP live demo module WPE 13% vs 10% industry target (30°C diodes, aggressive cooling; realistic 40°C die / 50°C coldplate → 10–11% WPE); linewidth best at 200 mW, worst at 150 mW and 400 mW; RIN < −155 dBc/Hz vs −145 dBc/Hz CPO spec (10× lower noise); relaxation oscillation ~3 GHz plus a 15 GHz feature. Section 4 is why CPO yield is a moat: CWDM spacing is lax; DWDM CPO needs ±30 GHz (~±0.17 nm); InP process variation lands off-grid; thermal tune is ~0.1 nm/K; an 11°C retune (1311 nm target at 40°C, printed 1309.9 nm → 51°C) puts the TEC into reverse/heating against a 50°C hot side, so environmental shifts flip heat/cool, power and PCE fall, and thermal leakage becomes electrical then optical noise. Section 5: Coherent has the same plots internally and will not publish them. A −155 vs −135 dBc/Hz gap is 20 dB = 100× amplitude noise. The China-flood-of-lasers narrative is the thing IA is screaming at.

Staged markdown and the live Substack fetch both drop the earnings-call screenshot text. No COHR revenue, GM, EPS, or guide figures appear in extractable prose. Do not invent them.

## Framework / Mental Model
**Three reusable trees (IA). Outputs of applying them to LITE/COHR sit in Evidence.**

### A. Four-plot CPO laser characterization
What a vendor must publish before a CPO-laser claim is falsifiable. Lumentum did; Coherent did not.

| Plot | What it shows | Why it binds |
|---|---|---|
| L–I (optical power vs drive current) | Process spread of current needed to hit a power class (here 400 mW) | Sets driver headroom and thermal load |
| PCE vs power | Electrical-in / optical-out; process band + peak-efficiency power | Peak is mid-power, not max-power |
| Lineshape / linewidth vs power | Phase-noise proxy across 150 / 200 / 400 mW | Mid-power is quietest; too-low and too-high both elevate noise |
| RIN vs frequency | Integrate 10 MHz → Nyquist to one number (dBc/Hz) | CPO spec −145 dBc/Hz; LITE prints < −155 |

Missing piece IA still wants: raw phase-noise plots (lineshape is derived; raw is easier to read). Temperature must be specified; 50°C is a pessimistic case. Lower temp → higher power and higher efficiency.

### B. Practical CPO laser yield (wavelength → TEC)
CPO lasers are not transceiver CWDM lasers.

| Component | Definition |
|---|---|
| CWDM (legacy datacom) | Wavelength spacing "super lax"; competent printers pass |
| DWDM CPO | ±30 GHz ≈ ±0.17 nm spacing accuracy |
| Process miss | High probability the printed λ is off-grid (InP variation) |
| Thermal tune | TEC cold-side temp shifts λ; rule of thumb ~0.1 nm per kelvin |
| Worked miss | Want 1311 nm @ 40°C die; printed 1309.9 nm → run 11°C hotter → 51°C |
| TEC reverse | Hot side 50°C, cold side 51°C → TEC *heats* (less efficient) |
| Mode chatter | Tiny ΔT → environmental shifts flip heat ↔ cool → stability/noise hit |
| Second-order | Optical power + PCE worse; thermal leakage into drive/control → electrical noise → optical noise |

Methodology: start from the grid spec, measure printed λ, compute the kelvin retune, then ask whether the TEC is still in cooling mode with margin. High-power CPO yield is "a nightmare." That is the moat. Characterization budget IA names: $100K CapEx or $30K rental + samples + a few hours.

### C. VCSEL CPO/NPO datarate
| Choice | IA verdict |
|---|---|
| 32G NRZ or 64G NRZ | Optimal for VCSEL NPO/CPO |
| 200G PAM4 on VCSEL | Fails GR-468 reliability; even if it passes, stupid on energy (driver complexity, FEC for crosstalk, Rx TIA burden) |
| FEC elimination | Impossible at 200G PAM4/lane — the whole point of CPO power/latency |
| CPO dream | Direct-drive, UCIe or similar clock-forwarded die-to-die SerDes |
| Coherent VCSEL die | "Great," #2 to Broadcom — build at the optimal rate and it could be great |

PhotonLink, if it is the VCSEL CPO/NPO brand, is interesting *if* the datarate is 32/64G NRZ, not 200G PAM4.

## Evidence

| Claim | Detail | Tag |
|---|---|---|
| Lumentum Q4 FY26 call | "Ultra bullish" (prior post 12 Aug) | [1×: IA] |
| Coherent Q4 FY26 call + numbers | "Crap" | [1×: IA] |
| Mix excuse | "Higher revenue mix is transceivers" — not enough | [1×: IA] [transcript] |
| Lumentum laser redesign | Lasers redesigned *smaller* to improve yield and GM | [1×: IA] |
| Cycle color | "Greatest optics bull market since the telco bubble" | [1×: IA] |
| Comp set (finance) | CapEx, FCF, gross margins, revenue growth — LITE improving more | [1×: IA] |
| Yield questions (unanswered) | EML yield at *what datarate*? CW yield at *what power class*? | [1×: IA] |
| Yield inference | "THE ONLY WAY THE NUMBERS MAKE SENSE IS IF YIELD IS BAD" | [1×: IA] |
| MS leading Q | Miniscule GM expansion vs LITE — mix shift or 6-inch yield? | [1×: IA] [transcript] |
| CPO laser (COHR) | "Dogshit" | [1×: IA] |
| Anderson cope | "WE SELL MORE THAN LASERS" | [1×: IA] [transcript] |
| LITE CPO-laser GM | ~80% | [1×: IA] [est.] |
| COHR isolator / FAU GM | ~30–40% | [1×: IA] [est.] |
| PhotonLink | Possible brand for VCSEL CPO/NPO; IA wants the presentation | [1×: IA] |
| VCSEL rank | COHR #2 to [[Theses/AVGO - Broadcom]] | [1×: IA] |
| Optimal VCSEL CPO/NPO rate | 32G NRZ or 64G NRZ | [1×: IA] |
| 200G PAM4 VCSEL | Will fail GR-468; energy/FEC/TIA case is bad even if it passes | [1×: IA] |
| FEC vs 200G PAM4 | Cannot eliminate FEC at 200G PAM4/lane | [1×: IA] |
| CPO electrical dream | Direct-drive, UCIe or similar clock-forwarded D2D SerDes | [1×: IA] |
| 6-inch *should* yield better | Better tools: new-gen Aixtron MOCVD (6-inch); semi-modern ASML vs ancient no-name litho | [1×: IA] |
| 6-inch wafer hypothesis | 6-inch InP wafers may have bad uniformity | [1×: IA] |
| AXTI 6-inch | Best substrate supplier; 6-inch InP still R&D, not shipping | [1×: IA] |
| Sumitomo hypothesis | Yield miss "maybe Sumitomo's fault"; AXTI 6-inch shipments would lift COHR yield | [1×: IA] |
| LITE public CPO plots | Temp specified; 50°C (pessimistic); noise vs power; process variation of Pout and PCE | [1×: IA / LITE public] |
| Missing plot | Raw phase noise (lineshape is derived) | [1×: IA] |
| 400 mW drive current | Min 1.2 A, max ~1.38 A | [1×: IA / LITE public] |
| PCE band @ 50°C | 21–24% | [1×: IA / LITE public] |
| PCE peak | 150–200 mW optical | [1×: IA / LITE public] |
| Industry PCE want | 25–30%; LITE hits at 40°C | [1×: IA] |
| Temp rule | Lower temp → higher power and higher efficiency | [1×: IA] |
| OFC 2026 ELSFP WPE | Module-level 13% vs 10% industry target | [1×: IA] |
| OFC demo thermal | Diodes held 30°C; "aggressive (unrealistic)" cooling | [1×: IA] |
| Realistic WPE | 40°C die / 50°C liquid-cooling coldplate → 10–11% | [1×: IA] [est.] |
| Linewidth vs power | Best at 200 mW (purple); worst (tied) at 150 mW and 400 mW | [1×: IA / LITE public] |
| Mid-power rule | Too-low power (vs design) elevates noise; mid-power optimal for both PCE and phase noise | [1×: IA] |
| LITE RIN | < −155 dBc/Hz average across power (10 MHz → Nyquist) | [1×: IA / LITE public] |
| CPO RIN spec | −145 dBc/Hz; LITE "over 10× lower noise than spec" | [1×: IA] |
| Typical RIN shape | High noise at very low f → relaxation oscillation → then good | [1×: IA] |
| LITE RIN features | Relaxation oscillation ~3 GHz; second feature ~15 GHz (curious, "not a problem") | [1×: IA / LITE public] |
| CWDM vs DWDM CPO | CWDM spacing lax; DWDM CPO ±30 GHz ≈ ±0.17 nm | [1×: IA] |
| InP λ tune | ~0.1 nm/K for a modern InP CW laser | [1×: IA] |
| Worked example | 1311 nm @ 40°C target; printed 1309.9 nm → +11°C → 51°C | [1×: IA] |
| TEC reverse | Hot 50°C / cold 51°C → heating mode, less efficient | [1×: IA] |
| TEC chatter | Small ΔT → heat↔cool flips on environmental shift → stability/noise | [1×: IA] |
| High-power CPO yield | "Nightmare"; "real competitive moats" | [1×: IA] |
| China-flood claim | IA rejects a coming flood of Chinese (and other) competition for LITE and AVGO lasers | [1×: IA] |
| Characterization budget | $100K CapEx or $30K rental + samples + a few hours | [1×: IA] |
| COHR data hide | Same four plots exist inside COHR; "at most one day" to publish; they will not | [1×: IA] |
| dB example | −155 vs −135 dBc/Hz = 20 dB = 100× amplitude noise | [1×: IA] |
| Extractable COHR print | No revenue / GM / EPS / guide in prose (charts are images) | [gap] |

## Contradiction Check
**Supports [[Theses/LITE - Lumentum]] §Key Non-consensus Insight (butt-joint / physics-gated laser layer; SiPh paradox — every PIC still needs InP light) and §Summary arms-dealer read.** The Aug 12 IA call-alpha ([[Research/2026-08-12 - LITE Irrational Analysis Q4 FY26 Call Alpha - deep-dive]]) said the unpriced statistic is production-sample mode-hop-free LIVT width plus a cavity shrink at held linewidth, with UHP GM 80–90% [est.]. This post is the other shoe: Lumentum *published* the four-plot CPO-laser book (RIN, PCE, linewidth, L–I) and is shrinking dies; Coherent will not publish and is selling 30–40% isolators/FAU. Same 80% CPO-laser GM figure, now as a contrast to COHR mix, not just a BOM. [Semis #2] the gate is parametric (λ accuracy, RIN, PCE, TEC mode), not wafer diameter. [VLM §1/§3] the CPO CW/UHP layer is the candidate toll; [VLM §4] the alpha test is whether that layer is still priced as a contestable commodity.

**Directly addresses LITE §Outstanding Question "If Coherent's 6-inch InP yields exceed legacy 3-inch, why does Coherent still buy EMLs from Lumentum?"** IA's working answer: they *don't* exceed on the metrics that matter. 6-inch tools ([[Theses/AIXA - Aixtron]] G10-AsP, ASML litho) *should* help; the residual is wafer uniformity (AXTI 6-inch still R&D; Sumitomo as the possible culprit) plus a CPO laser IA calls garbage. This is a hypothesis, not a fab tour. Adjacent: [[Research/2026-08-02 - AXTI LITE InP Substrate LTA Prepay Chain - deep-dive]] (AXT LTA / prepay) and [[Theses/IQE - IQE]] (Western InP epi). AXTI has no thesis.

**Challenges LITE §Bear Case (Coherent 6-inch InP lead / 4× devices per wafer / cost parity at 200G) and §Risk #4 (6-inch gap).** Wafer-diameter lead ≠ yield lead. Also challenges §Bear Case (CPO migrates value to a "relatively standardized and commoditized" CW DFB/ELS layer) and §Risk #3 (CW lower-ASP than EML): IA's claim is that high-power DWDM CPO yield (±0.17 nm, TEC reverse-mode, RIN 10× inside spec) is a moat, and the China-flood story is the one he is screaming at. [Semis #17] new-entrant-at-tight-prices anti-pattern. Complements [[Research/2026-08-08 - LITE COHR Laser Market Repriced by Scale-Up CPO - deep-dive]] (scale-up die CAGR) and [[Research/2026-07-19 - LITE COHR AEVA Practical SOA for CPO NPO - deep-dive]] (SOA/DFB physics).

**Challenges [[Sectors/Optical Networking & Photonics]] key industry question on whether Coherent's 6-inch lead collapses Lumentum pricing power by 2027–2028 even without yield parity.** IA's frame inverts the question: without yield *at the CPO parametric spec*, the 6-inch cost story does not print in GM. Sector COHR product table ("6-inch InP production leader… 2+ year lead") is the consensus IA is attacking.

**Partially answers LITE §Outstanding Question "how does Lumentum's role change under CPO, and does volume offset margin compression?"** Mix, not just volume: 80% GM on the CPO laser vs 30–40% on the things Coherent is proud of selling. Contingent on the 80% figure (single-source, not IR-confirmed; PhotonCap refused the 80–90% BOM on 12 Aug). Does not size CPO TAM, OCS, or Cloud Light module margin.

**VCSEL/PhotonLink is a new LITE adjacency, not a restatement.** LITE thesis already lists 1060 nm VCSELs for UCIe/PCIe scale-up. IA says Coherent's VCSEL *die* is #2 to [[Theses/AVGO - Broadcom]] and the miss is 200G PAM4 vs 32/64G NRZ + FEC. If PhotonLink is real and ships at the optimal rate, COHR has a VCSEL-CPO path that does not require winning the InP CW/EML yield war. That is the disconfirm for a pure "COHR CPO laser is garbage → LITE wins all CPO" read.

**[[Theses/AVGO - Broadcom]]:** named twice — VCSEL #1, and co-target of the China-flood claim with LITE. No AVGO `## Conviction Triggers` section. Does not speak to Tomahawk/XPU/VMware.

**[[Theses/AIXA - Aixtron]]:** 6-inch MOCVD is the tool that *should* have fixed yield and did not, per IA. Soft touch on AIXA's Outstanding Question (what happens if LITE/COHR push out 6-inch; customer yield). Does **not** cross AIXA `→ HIGH if` (≥60% opto orders / guide / Q3 mix) or `→ LOW if` (Veeco 6-inch product). If wafers (AXTI/Sumitomo) are the limiter, reactor quality is not the binding constraint — a hypothesis that cuts against "G10-AsP is the ASML of InP" as a *yield* story while leaving it intact as a *capacity* story.

**[[Theses/SIVE - Sivers Semiconductors]]:** not named. CPO ELS yield-as-moat is evidence-touched on SIVE `→ HIGH if (b)` (hyperscaler-named CPO ELS qualification) — direction LOW. IA's claim is that high-power DWDM CPO yield is a nightmare only LITE/AVGO currently clear; a Tier-2 ELS name faces a harder gate, not a sold-out commodity. SIVE CLOSE legs (probe / dilution / POET / Aeva / Photonics YoY) are untouched.

**[[Theses/AAOI - Applied Optoelectronics]]:** not named. AAOI `→ LOW if` CPO ≥20% of NVDA+AVGO switch shipments is untouched (this post is laser quality, not CPO unit share).

**[[Theses/IQE - IQE]]:** not named. Weak InP-epi adjacency via the AXTI/Sumitomo wafer hypothesis. IQE has no `## Conviction Triggers` section.

**Does not speak to** LITE's $1B FQ4 print, $1.225–1.275B / 39.5–40.5% OM FQ1'27 guide, OCS dates, Greensboro timing, or NVIDIA $2B convert — those live in [[Research/2026-08-12 - LITE PhotonCap FQ4 2026 First 1B Quarter - deep-dive]] and [[Research/2026-08-13 - LITE AAOI - Lumentum Q4 FY26 1.25B Guide - news]]. Complementary, not substitutable. Pair with [[Research/2026-04-15 - LITE COHR - Lumentum vs Coherent Analysis]] (the "Great Photonic Divergence" frame this print extends).

**[G-1] / [G-13] the variant perception is a messaging/yield gap, not a model gap.** Sell-side comps CapEx/FCF/GM/growth and accepts mix; IA's unsaid sentence is "yield at what datarate / power class, and show the four plots." [G-5] Anderson/comms-systems jab is culture color, not a thesis input. [G-6] 80% GM on a physical laser is the pricing-power print *if* real. [G-10] 80% GM is a base-rate outlier (abnormal ROIC fades); the thesis must beat fade with a qualification gate, not with "sold out this quarter." Cross-model agreement (every lens here flatters LITE vs COHR) is the cue to disconfirm. Single falsifying datapoint: Coherent publishes the same four plots at 50°C with RIN near −155 dBc/Hz, PCE in the 21–24% band at 400 mW, and a GM print that expands without a mix crutch — or a hyperscaler qualifies COHR CPO lasers at volume. Secondary falsifier: AXTI ships uniform 6-inch InP and COHR yield/GM inflects, which would retire the wafer-conspiracy leg and leave only the "hide the plots" leg. Tertiary: PhotonLink ships 32/64G NRZ VCSEL CPO that works, which is a COHR path around the InP CW yield war. LITE has **no Conviction Triggers** to fire; that is a filer/`/status` gap, not a silent pass.

## Source Excerpts
> "Coherent's call was crap and so were their numbers."

> "Guys the \"higher revenue mix is transceivers\" excuse is not enough to explain this mess."

> "Lumentum is RE-DESIGING LASERS TO BE SMALLER to improve yield and gross margins while Coherent financially self immolates in the greatest optics bull market since the telco bubble."

> "YIELD EML AT WHAT DATARATE? YIELD CW LASER AT WHAT POWER CLASS?"

> "Idiot the optimal datarate for VCSEL NPO/CPO is 32G NRZ or 64G NRZ."

> "200G PAM4 on a VCSEL will not work from a reliability perspective. You fools are going to fail GR-468."

> "You cannot eliminate FEC if each lane is running 200G PAM4!"

> "THE ONLY WAY THE NUMBERS MAKE SENSE IS IF YIELD IS BAD."

> "Is your miniscule gross margin expansion comparison [relative to Lumentum] because of mix shift or 6in yield?"

> "Lumentum is making 80% gross margins on their CPO laser but congrats Jim you get to sell isolators and FAU at like 30-40% margin."

> "One conspiracy theory I want to throw out there is that maybe the 6-in InP wafers themselves have bad uniformity. For example, the best supplier (AXTI) does not have 6-inch InP wafers. That is still under R&D."

> "DWDM CPO systems are much more strict, requiring +/- 30 GHz spacing accuracy. This translates to around +/- 0.17 nm."

> "As a rule of thumb, a modern InP CW laser will shift around 0.1 nm per kelvin."

> "You want to run a laser at 1311 nm at 40C die temp. Turns out, it is at 1309.9 nm. To tune the laser to the correct wavelength, you have to run it 11C hotter, thus operate at 51C. This is a huge problem."

> "Lumentum shows a RIN across power levels averaging less than -155 dBc/Hz which is EXCEPTIONAL. The general spec for CPO lasers is -145 dBc/Hz."

> "at OFC 2026, Lumentum's live CPO ELSFP demo showed a module-level WPE (wall-plug efficiency) of 13% which is very good given the industry target is 10%."

> "So if one laser is -155 dBc/Hz and the other is -135 dBc/Hz, the second laser is 20 dB worse and thus 100x higher amplitude noise."

> "IF I HEAR ONE MORE SPREADSHEET POD MONKEY BULLSHIT ABOUT HOW A FLOOD OF COMPETITION FROM CHINA AND ELSEWHERE IS COMING FOR LUMENTUM AND BROADCOM LASERS I SHALL SCREAM."
