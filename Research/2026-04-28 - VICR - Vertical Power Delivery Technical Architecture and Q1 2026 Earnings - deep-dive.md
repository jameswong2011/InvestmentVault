---
date: 2026-04-28
tags: [research, power, semiconductors, VICR, NVDA, AVGO, MPWR, CPO, VPD]
sector: Data Center Power & Cooling
ticker: VICR
source: https://photoncap.net/p/p-ir-the-one-line-equation-shaping ; https://photoncap.net/p/the-last-15mm-of-ai-power-three-numbers
source_type: deep-dive
---

# VICR — Vertical Power Delivery Technical Architecture and Q1 2026 Earnings

Combined ingest of two PhotonCap pieces: (1) "P = I²R: The One-Line Equation Shaping AI Infrastructure and Vicor's ($VICR) VPD" (2026-04-13, ~8,400 words) — engineering deep-dive on the Factorized Power Architecture, SAC topology, ChiP packaging, and why CPO structurally requires VPD; (2) "The Last 1.5mm of AI Power: Three Numbers from Vicor's Q1 2026 Earnings Call" (2026-04-22, ~3,200 words) — interpretation of three 2nd-gen VPD specs disclosed for the first time on the April 21 earnings call plus management's structured rebuttal of the 800V→6V architectural alternative.

## Thesis Delta

Sharpens two [[Theses/VICR - Vicor Corporation]] non-consensus insights with engineering specificity: (1) the Q1 call put hard numbers on 2nd-gen VPD (**3 A/mm² density, 40× current multiplication, 1.5mm thickness**) — combined, no public competitor spec sheet matches; (2) the CPO topology adds a *thermo-optic* reason for VPD adoption that is independent of the current-density argument — silicon micro-rings shift 80 pm/°C and a lateral converter dumping heat into the photonic chiplets makes wavelength tuning unstable. Strengthens conviction on architectural-necessity insight (#1 in thesis); does not change "founder concentration" or "LEO durability" risk assessments.

## Summary

PhotonCap's framing reframes the Vicor case as primarily a *physics-and-packaging* story rather than a market-share story. The first piece anchors on **P = I²R** — power loss through the PCB's "last inch" of copper scales with the square of current. At 0.7V × 1000-2000A core supply (Hopper through Rubin generations), 800A through 70µΩ of trace resistance dissipates 45W as heat *before* the current reaches the die. This is architectural, not solvable by silicon process improvements. The industry response — multiphase buck and TLVR (trans-inductor voltage regulator) — scales by adding phases (~20 phases for 1000A at 50A/phase), but each phase consumes PCB area, which pushes the converter farther from the processor, which raises Z_pcb, which raises the very loss that drove the need for more phases. The argument is that this self-contradiction has no algorithmic fix; only an architecture that places the converter on the *opposite* side of the PCB directly under the processor (Vicor's VPD) escapes the loop. Vicor's Factorized Power Architecture (FPA) achieves this by physically separating regulation (PRM, can sit anywhere) from transformation (VTM/GCM, sits under the processor), with the SAC (sine amplitude converter) topology delivering the conversion under ZCS+ZVS at 97% efficiency and <1µs response — the dynamics that make 2000A/µs transients tractable.

The second-half thesis is that co-packaged optics (CPO) — NVIDIA Quantum-X (early 2026), Spectrum-X Photonics (2H 2026) — re-rates VPD's value because CPO claims the package topside for optical I/O (~18 optical engines + 1,000+ fibers around the ASIC for a 28.8 Tbps Quantum-X switch), leaving no room for the lateral multiphase converters that won the H100 socket. More subtly, silicon micro-ring resonators shift 80 pm/°C in resonant wavelength, and a 100GHz WDM channel is only 800 pm wide — a 5–10°C thermal disturbance from a lateral converter is enough to require active heater compensation, which costs more power. VPD on the package bottom routes converter heat away from the photonic chiplets through a separate cooling path, decoupling the thermal domains. The author's read: the "cost and manufacturing ease" criteria that favored Monolithic Power Systems (MPWR) in the H100 era flip to "space and thermal" in the CPO era — same NVIDIA ecosystem, opposite winner.

The Q1 2026 earnings piece adds three layers. First, **2nd-gen VPD specs** (3 A/mm² current density / 40× current multiplication / 1.5mm thickness) were disclosed for the first time. The 40× number is the structural differentiator versus IVR (Integrated Voltage Regulator) approaches that achieve only ~2× multiplication: at 40×, delivering 2000A to the processor requires only a 50A bus feed, eliminating the thick-wiring + thermal-management problem that 1000A buses create. Second, management offered a structured rebuttal of the **800V→6V** distribution architecture circulating in some industry research. The key argument is that distribution voltage (Axis 1) and converter physical placement (Axis 2) are orthogonal — Vicor *supports* 800V upstream distribution and holds the 800V→48V bus conversion IP — but going directly from 800V to 6V near the processor recreates the high-current zone the architecture was supposed to eliminate (6V vs 48V baseline = 8× current = 64× wiring loss; a 2V IVR-style implementation hits ~526× per Phil Davies). Patrizio's framing: "frankly ill-conceived." Third, FY2026 guidance of $570M assumes **zero new licensing agreements** — Vicor is intentionally delaying settlements until after the second ITC final determination expected in 2027, betting that exclusion-order leverage produces materially better terms than pre-determination negotiation. Patrizio also hinted at a third ITC case ("In Italy we say there is no two without three"). Royalty margin is "nearly 100%" and management's prior long-term framing is that royalty *could* reach 50% of product revenue at the upper bound (~$255M on a $510M product base).

## Framework / Mental Model

PhotonCap's analytical scaffold combines four distinct frameworks that should be retained for re-application to other power architectures.

### Framework 1 — P = I²R as the binding physical constraint

**Premise**: Power loss through any resistive element scales with the square of current, so doubling the current quadruples the loss while halving the resistance only halves the loss. At AI-accelerator current levels (1000A steady-state, 2000A peak at 0.7V core), the dominant loss term is wiring resistance in the "last inch" of copper between the converter and the processor.

**Application logic**: For any proposed power architecture, decompose total PDN impedance as `Z_total = Z_distribution + Z_regulator + Z_pcb + Z_package + Z_die`, then identify which segment carries the highest current and whether it can be physically shortened. Long high-current paths are structurally lossy; short high-current paths require the converter to be physically near the processor.

### Framework 2 — Factorized Power Architecture (FPA) decomposition

**Premise**: Voltage regulation and voltage transformation are different engineering problems with conflicting placement requirements. Regulation needs a stable feedback loop (controller benefits from being away from the processor's switching noise). Transformation handles large current and heat (benefits from being directly under the processor to minimize PDN distance). A monolithic regulator cannot optimize for both.

**Components**:
- **PRM (Pre-Regulator Module)**: takes input voltage (e.g., 48V from rack PSU), produces a stable "Factorized Bus" (e.g., 48V regulated). Optimized for response speed and accuracy. Can sit anywhere on the motherboard.
- **VTM (Voltage Transformation Module) / GCM (Geared Current Multiplier)**: takes the Factorized Bus, applies a fixed K-factor (e.g., K=1/48), outputs core voltage at K× current. Optimized for current density and PDN proximity. Sits next to (LPD) or directly under (VPD) the processor.

**Methodology**: Calculate K = V_in / V_out. Output current = K × Input current. Output impedance reflected back to input scales as K². For K=1/48 with 1mΩ output impedance, the reflected input impedance is 2.3Ω (1mΩ × 2304) — a key reason the bus side stays manageable.

### Framework 3 — SAC (Sine Amplitude Converter) topology vs PWM buck

**Premise**: PWM hard-switches transistors when both current and voltage are large, producing switching loss and EMI. A resonant converter at fixed ratio with switching timed to current/voltage zero crossings (ZCS+ZVS) eliminates switching loss and produces a sinusoidal current waveform with low harmonic content.

**Methodology**: Form an LC tank from a transformer + resonant capacitor. Operate at the natural resonant frequency. Use a fixed conversion ratio (no variable feedback loop). Result: 97% efficiency, ~3.5 MHz effective switching frequency, output impedance flat to ~1 MHz, sub-microsecond load step response. Trade-off: cannot adjust output voltage variably — need PRM upstream for regulation.

### Framework 4 — Two-axis power architecture taxonomy

**Premise**: Architectural debates conflate two independent design choices.

| Axis | Question | Options |
|---|---|---|
| **Axis 1 (distribution voltage)** | At what voltage do you carry power from PSU to vicinity of processor? | 12V, 48V, 400V, 800V |
| **Axis 2 (final converter placement)** | Where does the final converter sit relative to processor? | Lateral (next to), Vertical (underneath = VPD) |

**Application**: 800V→6V is an Axis-1 proposal; VPD is an Axis-2 innovation. They are not competing alternatives — they address different problems. The 800V→6V camp's error is using a low-loss distribution choice to justify a high-loss final-segment choice. Correct framing: choose distribution voltage based on rack-to-processor *distance* (long → high voltage), choose final converter placement based on the last-inch *current density* (high → vertical).

**Stress-test heuristic**: For any proposed architecture, ask "where does the current spike to its peak value, and how long is the wire at that point?" If the high-current zone is anything more than a few millimeters, P = I²R will dominate regardless of upstream choices.

## Evidence

### Physics and architecture quantification

| Quantity | Value | Source / Notes |
|---|---|---|
| AI accelerator core voltage (4nm class) | ~0.7 V | Transistor reliability ceiling; cannot go materially lower |
| AI accelerator current (steady / peak) | 1,000 A / 2,000 A | Per-processor; H100-Blackwell-Rubin range |
| Transient slew rate | 2,000 A/µs | Load step from 0 to 2,000A in <1µs; voltage must stay within ±10% (~70 mV) |
| Decoupling capacitance required | ~3 mF | Directly under processor package |
| PCB trace loss example | 800A × 70µΩ = **45 W** | Single PCB segment, 100°C |
| PCB trace loss at 1,000A / 1,500A (same R) | 70 W / 158 W | Quadratic scaling |
| VTM output impedance | 0.8 mΩ | An order of magnitude below conventional multiphase |
| FPA system efficiency | 90–95% (PRM+VTM combined) | Vicor white paper FPA101 |
| SAC efficiency | 97% | Single-stage, ZCS+ZVS |
| SAC effective switching frequency | ~3.5 MHz | Output Z flat to ~1 MHz |
| SAC load step response | <1 µs | Decisive for 2,000 A/µs transients |
| LPD effective current ceiling | ~800 A | Beyond this, VPD required |
| VPD PDN impedance reduction | 20× vs lateral; **50× vs multiphase buck** | Vicor reports |
| VPD loss reduction vs TLVR lateral | **95%** | Vicor 1200A ChiP-set press release |
| Power saved per accelerator module | ~100 W (VPD vs TLVR) | Vicor / Electronic Design |
| Per 20,000-accelerator supercomputer | 2 MW continuous = 17.5 GWh/yr | Industrial-power-rate $-millions/yr |
| Power density progress | -25% loss every 2.5 years | Brick-form 1990s → stacked ChiP 2025 |

### 2nd-gen VPD specs (FIRST DISCLOSED Q1 2026)

| Spec | 2nd-gen VPD | Comparison point |
|---|---|---|
| **Current density** | **3 A/mm²** | Gen 4 was 2 A/mm²; competitor "inadequate" per management |
| **Current multiplication** | **40×** | IVR competitors achieve ~2× |
| **Package thickness** | **1.5 mm** | Industry buyers (NVIDIA, Google per APEC analyst) asking suppliers for <3 mm; 1.5 mm is half that |
| Roadmap | Thinner than 1.5 mm | "We're not stopping at 1.5 mm, we're going thinner" — Vinciarelli |
| Lead-customer Gen4→Gen5 transition | H2 2026, ramp before YE | Likely Cerebras (wafer-scale-engine reference, unconfirmed) |
| Additional HPC customers on 2nd-gen | After lead customer transition | "Hyperscalers" referenced in plural, undisclosed |

### CPO + VPD thermal coupling

| Quantity | Value | Note |
|---|---|---|
| Silicon thermo-optic coefficient (1550nm, 300K) | 1.8 × 10⁻⁴/K | Komma et al. 2012 |
| Micro-ring resonator wavelength shift | ~80 pm/°C | Padmaraju et al. |
| 100GHz WDM channel width near 1550nm | ~800 pm | 10°C thermal swing = full-channel shift |
| 200GHz WDM channel width | ~1,600 pm | 10°C thermal swing = half-channel shift |
| Lateral converter temp rise into adjacent photonic chiplet | 5–10°C | Forces 400–800 pm tuning correction |
| VPD thermal isolation benefit | Routes converter heat through opposite-side heat sink | Decouples thermal domains |
| Required laser power increase per 1 dB coupling/insertion loss | ~26% (10^0.1 - 1) | Translates to ELS electrical consumption |

### Q1 2026 financial / operational disclosures

| Metric | Q1 2026 | Notes |
|---|---|---|
| Revenue | $113 M | |
| Backlog | **$301 M** | +70% sequential, 2.7× quarterly revenue |
| Royalty revenue | $15 M Q1 ($60 M annualized run-rate) | "Nearly 100%" gross margin |
| FY2026 revenue guide | **$570 M** | Combined product + royalty |
| FY2026 product (implied) | ~$510 M | $570 M − ~$60 M existing royalties |
| New licensing assumed in FY26 guide | **Zero** | Intentional — waiting on 2027 ITC final determination |
| Q1 OCF one-time item | -$28.6 M outflow | Past litigation award payment |

### Capacity expansion

| Asset | Prior plan | Updated Q1 2026 view |
|---|---|---|
| Andover CHiP Fab 1 | $1 B/yr nameplate | **$1.5 B/yr** — 50% above plan via cycle-time reduction + adjacent-building offload |
| Second 3Di line | TBD | Q3/Q4 2026 installation |
| Fab 2 strategy | New land acquisition | Switched to existing-building approach (speed) |
| Capacity utilization commentary | "Sold out for the foreseeable future" — Vinciarelli | Demand structurally ahead of supply |

### Royalty / IP enforcement strategy

| Item | Status |
|---|---|
| 1st ITC case | Resolved — Limited Exclusion Order (LEO) granted; $45M Delta/Cyntec/Foxconn settlement booked 2025 |
| 2nd ITC case | Final determination expected **2027** |
| 3rd ITC case | Hinted at by Patrizio: "In Italy we say there is no two without three" |
| Royalty 50% framing | Long-term upper-bound framing per management ($255M+ on $510M product base) — not committed guidance |
| 800V→6V IP exposure | Vicor holds IP; if industry adopts that path, opens additional royalty stream |

### 800V→6V architectural debate (with quantification)

| Distribution voltage | Current ratio vs 48V baseline | I²R loss ratio |
|---|---|---|
| 48V (baseline) | 1× | 1× |
| 6V | 8× | **64×** |
| 2V (IVR-style) | 24× | 576× simple math; **526× cited by Phil Davies** (assumptions undisclosed) |

Vicor's preferred path: PSU → 800V distribution → [800V→48V bus conversion via Vicor IP] → 48V distribution all the way under processor → [48V→0.7V VPD in 1.5 mm] → Processor.

Reasons 48V is the inflection point (PhotonCap's read, not management):
- **SELV (Safety Extra-Low Voltage) ceiling = 60V**. Crossing it triggers different insulation/connector/maintenance regime with material cost rise.
- **1.5mm converter thickness only feasible from 48V input**. Going 800V→<1V in one step demands transformer turn ratios, insulation clearance, and switching devices that don't fit a thin package.
- **800V advantages are distance-dependent**. Useful rack-to-rack and inside-rack vertical busbars; irrelevant across the few mm directly under the processor.

### Competitive positioning (PMIC market shares cited)

| Player | Cited share / position | Relevance |
|---|---|---|
| Texas Instruments (TXN) | ~12.5% global PMIC revenue | Broad catalog, automotive/industrial bases |
| Monolithic Power Systems (MPWR) | "Larger socket" in AI accelerator power; 15–20% est. AI accelerator power (FinancialContent) | Won H100 with multiphase buck on cost + lateral integration ease |
| Vicor (VICR) | Differentiated, in-U.S. vertically integrated, IP-rich | Patent base around FPA/SAC/ChiP; 800V distribution stronghold |
| ADI / IFNNY / RNECY / STM / NXPI | Integrated semiconductor IDMs | Auto/industrial focus, breadth over density |
| Power Integrations (POWI) | Power-specialized | Smaller competitor in same category |

### Governance facts

| Item | Value |
|---|---|
| Vinciarelli Class B shares (2025-12-31) | 11,726,718 (10 votes/share) |
| Common shares | 45,910,601 |
| Vinciarelli economic interest | ~47% |
| Vinciarelli voting power | **~80%** |
| Founder tenure | 44 years |
| IEEE recognition | 2019 William E. Newell Power Electronics Award |

## Key Segments

### Segment A — The "last inch" problem (PhotonCap #1 §3)

The fundamental claim: every power architecture eventually has to step a high-voltage bus down to ~0.7V at the processor. That conversion either happens far from the processor (creating a long high-current PCB trace with quadratic losses) or close to it (which forces the converter into the 60×60mm package footprint). Multiphase buck regulators chose the first path and now hit a self-limiting wall — adding phases to scale current consumes the very PCB area that drove the loss problem. TLVR (trans-inductor voltage regulator) is a magnetic-coupling refinement of the same approach but does not change the fundamental geometry. The escape route is to put the converter on the *opposite* side of the PCB directly under the processor — Vicor VPD. This re-categorizes the architectural debate from "what efficiency gains are possible" to "what physical placement is achievable."

### Segment B — FPA + SAC + ChiP as a manufacturable system (PhotonCap #1 §4)

Three innovations have to work together for VPD to be a real product, not just a topology paper. (1) **FPA** physically separates regulation from transformation so each can be optimally placed. (2) **SAC** topology delivers the transformation at 97% efficiency under ZCS+ZVS with sub-microsecond response — fast enough for 2,000 A/µs transients without massive decoupling capacitance. (3) **ChiP packaging** uses panel-level manufacturing (wafer-fab-style yield management), double-sided cooling (halves thermal impedance), grounded metal shielding for EMI, and stacked ChiP for the multilayer integration that GCM requires. Stacked ChiP is what makes a single module the size of a small chip deliver 1,000A — and Vicor's claim is that the manufacturing process is what competitors cannot reverse-engineer in <5 years.

### Segment C — Why CPO bound to VPD (PhotonCap #1 §5)

CPO (co-packaged optics) introduces *new* constraints that flip the H100-era architecture choice. (1) **Topside space**: Quantum-X needs 18 optical engines + 1,000+ fiber exits per ASIC — there's no room for lateral multiphase converters even if they were efficient enough. (2) **Thermal sensitivity**: silicon micro-ring modulators shift 80 pm/°C in resonant wavelength; a lateral converter dumping heat into adjacent photonic chiplets raises required heater power and reduces stability margin. (3) **Current density requirement**: 28.8 Tbps Quantum-X ASIC + integrated photonic engines pushes total package power to multi-kW, and current density >2 A/mm² is a regime conventional multiphase struggles to reach. None of these constraints existed for H100; all of them favor VPD architecturally for the next-generation switch and accelerator silicon.

### Segment D — Q1 2026 capacity bottleneck (PhotonCap #2 §2)

The supply-side story dominates the call. Andover Fab 1 runs to $1.5B/yr (50% above plan) via cycle-time reduction at bottleneck steps + relocating some steps to an adjacent building. A second 3Di line goes in Q3/Q4. Fab 2 strategy shifted from greenfield land acquisition to existing-building retrofit for speed. Vinciarelli's verbatim: "We see ourselves being essentially sold out in terms of capacity for the foreseeable future." Backlog at $301M (+70% sequential, 2.7× revenue) confirms demand is structurally ahead of supply. Customer mix on the call: lead = wafer-scale-engine maker (PhotonCap reads as Cerebras, unconfirmed by Vicor); hyperscalers in plural (undisclosed); industrial/defense/ATE continuing to place strong orders.

### Segment E — 2nd-gen VPD specs and the 800V→6V rebuttal (PhotonCap #2 §3-4)

Three specs disclosed for the first time: 3 A/mm² current density, 40× current multiplication, 1.5mm thickness. The 40× number is the structural moat — IVR competitors achieve ~2×, meaning 2,000A to processor requires 1,000A bus feed (impractical thermals + thick wiring); at 40×, the same load needs only a 50A feed. The 1.5mm thickness already half the <3mm spec NVIDIA/Google reportedly require per APEC discussion, with thinner on the roadmap for chiplet/CoWoS-class packaging. Patrizio's 800V→6V rebuttal: distribution voltage and converter placement are independent axes; Vicor *supports* 800V upstream and built the 800V→48V bus conversion IP. The opposed step is 800V→6V near the processor because 6V vs 48V on the final segment = 8× current = 64× wiring loss, and 2V (IVR-style) hits 526× per Phil Davies. Even in the bear case where 800V→6V wins, Vicor's IP exposure opens a royalty path. Vinciarelli: "frankly ill-conceived."

### Segment F — Royalty strategy and the 2027 ITC inflection (PhotonCap #2 §5)

FY2026 guide of $570M assumes zero new licensing. Reason: the 2nd ITC case has a 2027 final determination; settling early sacrifices exclusion-order leverage. Q1 royalty was $15M ($60M annualized) at "nearly 100%" gross margin. Management's prior framing (Phil Davies, multiple appearances) is that royalty *could* reach 50% of product revenue at the upper bound — on a $510M product base, that's $255M of ~100% margin revenue. The author's three scenarios: base = $60M royalty; upside = $100M+ post-2027 settlement(s); stretch = $250M+ over multiple years. Patrizio's "no two without three" comment hints at a 3rd ITC case in queue.

## Contradiction Check

**Supports** the [[Theses/VICR - Vicor Corporation]] non-consensus insights without revision. Specific reinforcements:

- **Insight #1 (Vicor lost H100, narrative is stale)** — Now reframed with explicit physics (P = I²R, last-inch geometry) and a *second* reason the H100 story doesn't repeat: CPO's topside is occupied by optical I/O. Even setting current-density aside, the architectural geometry favors VPD.
- **Insight #2 (LEO is structural rents, not one-time)** — Strengthened by management's *deliberate delay* of new licensing pending 2027 ITC determination + 3rd-case hint. The 50% framing on royalty/product is the most explicit upper-bound articulation yet.
- **Insight #3 (5-7yr IP moat)** — The 2nd-gen VPD specs (3 A/mm² + 40× + 1.5mm combined) are a concrete data point on what competitors would have to match. The "competitors go lateral with a bit of vertical" line from Phil Davies is a tell that Gen-1 VPD copies are structurally blocked from Gen-2.
- **Insight #4 (founder discipline + dual-class)** — Quantified: ~47% economic / **~80% voting power**. The dual-class structure (10 votes/share for Class B) is more entrenched than thesis previously stated.
- **Insight #5 (capacity from constraint to enabler)** — Confirmed: Fab 1 nameplate revised $1B → $1.5B/yr; Fab 2 strategy switched to existing-building for speed; "sold out for foreseeable future."

**Tensions / open items**:
- Thesis "Outstanding Question #4" (why did Vicor walk away from H100) — PhotonCap supports the management framing (a) (margin discipline) but does not resolve the technical-exclusion alternative (b). Both can be partially true.
- Thesis "Outstanding Question #1" (Vera Rubin socket content) — PhotonCap explicitly disclaims that NVIDIA hasn't disclosed Quantum-X power vendor and the article argues "VPD fits CPO well" not "Vicor is in Quantum-X." This tightens the unresolved-content question rather than answering it.
- Thesis "Outstanding Question #6" (gross margin durability) — The "nearly 100%" royalty margin combined with 2027-delayed licensing creates a step-function in FY27/28 GM if 2nd ITC settles favorably. Could push blended GM past 60% if licensing mix rises sharply.

**No challenges** to existing conviction. Conviction stays at **medium** — the engineering depth confirms the moat but does not retire founder/Federal-Circuit/socket-content risks.

## Source Excerpts

> "P = I²R, the one most of us learned back in school. ... This one equation from physics class now defines the physical limits of AI infrastructure. The bottleneck is not only FLOPS. Compute performance and memory bandwidth are already well-known constraints, and power delivery itself has joined them as a first-order limit." — PhotonCap #1 §1

> "Adding phases to handle more power ends up increasing the loss that drove the need." — PhotonCap #1 §3.3 (on multiphase buck self-contradiction)

> "For 1,000 systems, CPO alone is 3 MW, or roughly 26 GWh annually at 24/7 operation. ... VPD's additional effect stacks on top at the incremental tens-of-megawatts scale." — PhotonCap #1 §5.5

> "We see ourselves being essentially sold out in terms of capacity for the foreseeable future." — Vinciarelli, Q1 2026 call (per PhotonCap #2 §2)

> "We're not stopping at 1.5 millimeter, we're going thinner." — Vinciarelli, Q1 2026 call

> "Vicor has proprietary technology at 800 volts. We did a lot of pioneering developments with respect to bus conversion from 800 volts." — Vinciarelli (rebutting framing that Vicor is anti-800V)

> "frankly ill-conceived" — Vinciarelli on the 800V→6V architecture

> "Competitors go lateral with a bit of vertical." — Phil Davies (on Gen-1 VPD copies' structural ceiling)

> "In Italy we say there is no two without three." — Vinciarelli (3rd ITC case hint)

> Royalty margin: "nearly 100%" — Phil Davies, Q1 2026 call

## Related

- [[Theses/VICR - Vicor Corporation]] — primary thesis; this research sharpens Insights #1, #2, #3, #4, #5 and refines Outstanding Questions #1, #4, #6
- [[Theses/NVDA - Nvidia]] — Quantum-X / Spectrum-X CPO context; Vera Rubin power architecture
- [[Theses/AVGO - Broadcom]] — Tomahawk Bailly (MZM) / Davisson (modulator undisclosed) comparison reference; AVGO is the merchant-switching-silicon counterpoint to NVIDIA's CPO architecture
- [[Sectors/Data Center Power & Cooling]] — sector context; this note adds chip-level power architecture detail that complements the rack/facility analysis already in the sector note
- [[Sectors/Custom Silicon & Networking Semiconductors]] — Quantum-X / Spectrum-X context overlaps with this sector's CPO discussion
