---
publish: true
date: 2026-08-14
tags: [macro, technology, robotics, humanoid, physical-AI, supply-chain, NVDA, TSM, TER]
status: active
sector: Robotics & Automation
source: vault synthesis — three parallel web-research sweeps (2026-08-14) covering actuation/mechanical, sensing, and compute/power/OEM landscape; anchored on [[Research/2026-08-13 - Unitree Humanoid Robotics China Trajectory - deep-dive]] (SemiAnalysis) and [[Research/2026-08-13 - TSM SONY TSMC Sony vs China CIS Ecosystem - deep-dive]] (TSPA)
---

# Humanoid Robotics Supply Chain

*Tracker document for the humanoid component stack, magnets to VLA models. Answers the open question raised in [[Research/2026-08-13 - Unitree Humanoid Robotics China Trajectory - deep-dive]]: should the vault carry deliberate humanoid exposure, and if so at which layer? Provenance flags throughout: [C] = confirmed/company-reported, [B] = broker/consultant estimate, [R] = rumor/unverified; this sector has a proven fabricated-supplier-list problem, so the flags are load-bearing.*

## Thesis Delta

- **This supply chain has no bottleneck: that is the finding.** Semis #1 (bottleneck = pricing power = alpha) returns empty almost everywhere: Chinese planetary-roller-screw prices fell ~80% in 2025 alone (¥10,000 → ¥2,000/unit) [B], LiDAR fell 99.5% in 8 years ($75k → sub-$200 Hesai ATX) [C], dexterous hands went from $100k+ (Shadow) to $3–8k (Inspire, LinkerBot ~5,000 hands/month) [C], and merchant QDD actuator modules retail at $100–700 (RobStride) [C]. Capacity is being built for millions of units (Shuanghuan ~500k reducers/yr [B], Hengli 2.6M roller screws/yr [B], Tuopu +200k actuators/yr line [C]) against 13,318 humanoids shipped globally in 2025 [B, Omdia]. Supply is arriving roughly two orders of magnitude ahead of demand, the inverse of the AI-datacenter bottleneck economy the vault's other macros track. Merchant component pricing power is structurally impossible in this regime; the obvious component-supplier long is the crowded, wrong trade. The two exceptions sit at the ends of the stack: NdFeB magnets (state-controlled chokepoint) and the autonomy/data layer (Figure's Helix-02 is the only VLA with multi-day third-party-site throughput data).

- **Bifurcation is complete at the finished-robot level, not just the chip level.** Chinese vendors shipped 97% of H1 2026 units; Chinese customers were >85% of demand [B, SAG via Bloomberg 2026-08-10]. The US banned new Chinese humanoid/quadruped imports in July 2026 (FCC Covered-List mechanism) [C]; China's April-2025 rare-earth/magnet licensing regime persists with MP Materials and USA Rare Earth entity-listed 2026-06-22 and a second control wave scheduled 2026-11-10 [C]. Each bloc weaponizes its chokepoint. US: market access + AI silicon; China: magnets + 97% of unit production. Semis #16's parallel-markets frame now applies to entire robots: Chinese humanoid volume is not Western TAM and vice versa. Unresolved contradiction: US flagships still carry Chinese content (Xusheng 603305.SS magnesium shells in Figure [R]; ~70% of Optimus V3 BoM Chinese-sourced [R]).

- **Demand quantity is real; demand quality is not.** H1 2026 shipments ~19,100 units, 3.7× YoY [B, SAG], but the buyers are heavily showcase/education/state-adjacent ("performative rather than functional"; Fortune 2026-06-06). The autonomous-work bar is passed only by Figure–BMW Spartanburg (209k packages sorted, 167 consecutive autonomous hours, company-reported, unaudited), Agility–GXO (paid tote work since 2024), UBTech Walker S2 at Foxconn/BYD [C, company-reported], and one Xiaomi nut-fastening station at 98% [C]. Tesla's own Q4-25 admission: factory Optimus units are "for learning and data collection, not productive tasks." Per [G-10], the sector is pre-chasm; extrapolating Unitree's quadruped cost curve onto humanoid *deployment* is the exact inside-view error the SemiAnalysis note warned against.

- **The vault already holds the durable layer.** [[Theses/NVDA - Nvidia]] owns the Western brain + simulation toll (Jetson Thor in Agility/Boston Dynamics/Figure/Amazon [C]), but TrendForce sizes the entire humanoid chip market at $48M by 2028 [B], so this is option value, not earnings. [[Theses/TSM - Taiwan Semiconductor]] fabs Tesla AI5 (taped out ~2026-04 [C]), Jetson Thor, and the Sony CIS JV. [[Theses/TER - Teradyne]] owns the cobot incumbent (UR, ~$375M real revenue) that the humanoid story must either displace or validate. Actionable additions are watchlist, not buys: Harmonic Drive Systems 6324.T (the only Western-qualified strainwave seat, humanoid orders inflecting), RoboSense 2498.HK / Hesai HSAI / Orbbec 688322.SS (the only sensing names with auditable robotics revenue), AAC 2018.HK / Goertek 002241.SZ (consumer-electronics Tier-1s entering hands/tactile/acoustics: the DJI-pattern absorption signal), and Western magnet proxies (MP, Lynas) as rare-earth theses that humanoids amplify.

## Summary

A humanoid robot is 28–44 actuators, 40–80 motors, 2–8 cameras, 1–3 IMUs, a ~2.5 kWh battery, and 1,000–2,000 semiconductors carrying $1,400–4,000 of silicon [B, mixed]. Current bill of materials: ~$35k China-built (BofA, end-2025; Unitree G1 teardown $8,976 at the extreme low end) versus $50–150k Western-built, a 2–4× bloc cost gap that widens to 3–20× on individual components (hands, screws, coreless motors) [B]. Actuation and transmission take 50–60% of BoM, dexterous hands are projected to reach 19% by 2030 (BofA), sensing runs 10–15% and falling on the China stack, compute bifurcates ($100–500 Rockchip-class in Chinese volume units vs $2,999 Jetson Thor T5000 in Western premium units), battery is mid-single-digit. The structure of this industry is a DJI/BYD-style cost-deflation machine, not an AI-datacenter-style bottleneck economy: every layer where Chinese suppliers operate has seen 50–99% price declines inside 2–8 years, and each merchant capacity announcement is sized for a demand level (millions of units) that is 100× current shipments. [G-13] discipline: the price-implied expectations across the A-share complex span Leaderdrive 688017.SS at >300× trailing earnings to Shuanghuan 002472.SZ at ~26×: the market has not decided whether these are structural growth franchises or capacity-glut cyclicals, and the vault's answer from Semis #3 mechanics is the latter until unit demand catches capacity.

Architecture forks decide supplier fates before volume arrives (Semis #8). In rotary joints, high-ratio strainwave/harmonic drives (Tesla arms/waist, Figure, most Chinese OEMs) compete against Unitree's quasi-direct-drive planetary bet: QDD deliberately routes around the 20-year flexspline tacit-knowledge moat rather than crossing it, trading positioning precision for cost, backdrivability, and weeks-scale iteration. Gate-deletion-by-architecture is the recurring China pattern: QDD deletes the harmonic gate, motor-current torque estimation deletes the six-axis force-torque sensor, vision-first stacks demote LiDAR (UBTech Walker S2 explicitly moved away from "expensive LiDAR-reliant" prototypes [C]). In linear actuation, planetary roller screws (Tesla hips/knees; BofA reference architecture: 14 linear + 16 rotary per robot) were the 2024–25 bottleneck story via µm-tolerance thread-grinding machines; that bottleneck broke in China through domestic grinder integration (Shuanglin's Kezhixin acquisition cut per-line capex ¥10M→¥3M [C/B]) and process substitution (thread rolling/whirling), which is what the −80% price collapse measures. Hands are the frontier subsystem: tendon-driven through-forearm designs (Optimus V3: ~22 DoF/hand, actuators relocated to forearm, per Oct-2024 patents published 2026 [C for patents]) against linkage designs, with hand redesign the component that delayed Optimus V3 [R, widely reported] and the highest redesign churn in the stack.

Sensing is running two opposite trends simultaneously. Exteroception is consolidating toward cameras (Tesla pure-vision (~8 cameras [R]), UBTech vision-first, Unitree in-housing LiDAR at 30–40% of merchant cost) while manipulation sensing proliferates: Figure 03 added a palm camera per hand plus in-house fingertip tactile resolving 3 grams of force, built in-house after surveying merchant options and rejecting all of them [C], which is the supply-chain finding: there is no at-scale merchant tactile vendor anywhere in the world as of August 2026. PaXini (private, Shenzhen; 1,140-taxel hands) is the closest pure-play; AAC Technologies and Goertek, consumer-electronics Tier-1s with precision-assembly scale, both debuted humanoid subsystem lines (hands, tactile, acoustics) at CES 2026 [C]. LiDAR and six-axis F/T sensors are the squeezed middle: Hesai guides only "5-digit" humanoid-segment units for 2026 [C] against 240k robotics units shipped in 2025 (lawnmowers and AMRs dominate), and RoboSense's humanoid share of its RMB 709M robotics revenue is undisclosed. The Sony–TSMC Kumamoto JV (definitive 2026-08-11) is smartphone-CIS-first with physical-AI framing only (no robotics-specific CIS product exists [C]), consistent with the vault's existing read: do not invent a CIS-volume trigger for [[Theses/TSM - Taiwan Semiconductor]].

The magnet layer is where pricing power actually lives, and it is state-controlled. A humanoid carries ~2–4 kg of NdFeB (estimates span 1.3–6 kg [B], a 4.6× error bar) versus 1–3 kg per EV; China refines/sinters ~90% of global magnet output. The control regime: April 2025 MOFCOM licensing on 7 medium/heavy rare earths + downstream magnets (never lifted); October 2025 sweeping expansion suspended for one year post-Busan (until 2026-11-10) but with the licensing infrastructure preserved; MP Materials and USA Rare Earth entity-listed 2026-06-22 (worldwide transfer ban) days after the G7 agreed to cap single-country RE imports at <60% by 2030; zero June-2026 shipments of Ga/Dy/Tb/Y to Japan: throttling as enforcement [all C]. Military end-use is a de facto embargo; US defense sourcing rules bar Chinese-origin NdFeB through the full chain from 2027-01-01. Western response capacity (MP 10X ~10kt/yr commissioning 2028 with a $110/kg NdPr DoD floor and 100% DoD offtake; Lynas–JS Link Malaysia 3kt Q4 2027; Neo Narva operating) arrives 2027–28 at ~10–20kt against ~190kt of Chinese NdFeB blank capacity in 2026 [B]. Magnets are the only humanoid layer passing both VLM clusters (structural advantage and durability), and the equity expression is policy-floored Western producers as rare-earth theses that humanoids amplify, not humanoid theses per se.

Demand, capital, and policy carry the full [G-4] frenzy-phase signature. Units: 13.3–18k shipped 2025 [B, conflicting counts], ~19.1k in H1 2026 (Agibot ~8,400 / 44% share, Unitree ~5,900 / 31% [B, SAG]), 50–90k consensus for FY2026. Capital: humanoid VC at $8.7B YTD 2026, already 2× the full-year 2025 record; Unitree's STAR IPO priced 2026-08-06 at ~$9.04B (~$904M raise, ~8,000× oversubscribed) [C], against the ~$42B valuation talk circulating in the SemiAnalysis piece two days earlier; the gap resolves on debut (STAR pricing caps make a large pop likely; treat neither number as the market's verdict yet). Agibot is back-dooring onto STAR via Swancor control (~RMB 2.1B for ≥63.6%) [C]; NEURA raised up to $1.4B led by Tether [C]. Policy: robotics is one of eight strategic emerging industries in the 15th Five-Year Plan; ~$20B direct subsidies (Merics); Q1 2026 alone saw 210 embodied-AI financings >RMB 30B [B]. Against this: the slipped-target ledger. Tesla delivered hundreds against a 5–10k 2025 target, V3 reveal and production slipped twice into Aug 2026 with Musk calling the rate "literally impossible to predict" [C]; Apptronik pushed its first true commercial product (Apollo 3) to 2027 [C]; 1X shipped a $20k home robot whose launch reviews found zero autonomous task completion (teleoperators seeing inside homes) [C]; Sanctuary abandoned its humanoid entirely and pivoted to software, the cycle's first capitulation [C]. Installation-phase over-funding building capacity ahead of production capital's ability to absorb it is exactly Perez's frenzy, which implies the durable winners get picked after the shakeout, and history says they are rarely the component makers who funded the build-out.

## Framework / Mental Model

### Value stack — where margin can survive

| Layer | Content per robot | Cost trajectory | Merchant structure | Pricing-power verdict |
|---|---|---|---|---|
| NdFeB magnets | 2–4 kg [B, 1.3–6 range] | Rising ex-China (EU Dy 6× China price) | China ~90%; state-licensed | **Durable: the only chokepoint.** Accrues to policy-floored Western producers |
| Harmonic reducers | ~16 rotary joints [B] | Leaderdrive 40–60% below HDS [B] | HDS vs 3+ Chinese + QDD substitution | Bifurcated: HDS holds Western qualification gate; China side commoditizing |
| Roller screws | ~14 linear joints [B] | −80% in China in 2025 | >6 Chinese entrants + Japanese/Swiss | None: capacity glut forming |
| Frameless motors | 40–80/robot | Moons' at maxon spec, fraction of price [C claim] | Crowded, no confirmed flagship wins | None |
| Encoders | ~2/precision joint → 40–80 ch | Chip-level $1–10 [low-confidence] | RLS/Heidenhain/ams/MPS + Chinese | Thin; MPS integrated-joint angle is the interesting one |
| Dexterous hands | 2 (up to 19% of 2030 BoM [B]) | $100k+ → $3–8k | LinkerBot ~5k/mo, Inspire ~10k cum. | Eroding fast; micro-drive modules (Zhaowei) the residual |
| Cameras/CIS | 2–8 | Smartphone-scale pricing | Sony/OmniVision/onsemi | None incremental: rides existing scale; volumes trivial vs phones |
| Depth modules | 1–3 | Falling | RealSense (claims 80% humanoid share [C, unaudited]), Orbbec | Weak; Orbbec has real revenue + Jetson Thor validation |
| LiDAR | 0–1 (China stack only) | −99.5% in 8 yrs | Hesai/RoboSense/Livox/in-house | None; squeezed middle: Tesla/UBTech deleting it |
| Tactile | 0 → 1,000+ taxels | n/a | **Vacant: no at-scale merchant vendor** [C, Figure rejected all] | The open layer; watch AAC/Goertek/PaXini |
| 6-axis F/T | 0–4 | Chinese undercutting | ATI/Novanta "Varo" + Chinese | Weak; deletion-by-current-sensing trend |
| IMU | 1–3 | $5–50 | Bosch/TDK/ST (Optimus [R]) | None |
| Brain compute | 1 | $100–500 China / $2,999 Thor | NVIDIA vs Rockchip/Horizon vs in-house (Tesla AI5) | NVIDIA tolls the Western 3% of units; China socket commoditized |
| VLA/autonomy software | — | — | GR00T/pi-0 open vs Helix vertical | **The contested layer where the eventual monopoly forms** |
| Battery | ~2.5 kWh | EV/power-tool cell reuse | CATL/EVE/Samsung SDI/LG | None on cells; solid-state marketed robot-first because robots tolerate high $/kWh |
| MLCC/passives | EV-class thousands [B, no official count] | Tight from AI servers, not robots | Murata/SEMCO/Taiyo Yuden oligopoly | Real but humanoids are a 2027+ increment: do not double-count with 800VDC MLCC thesis |
| Structure (Mg-Al, PEEK) | Frame + shells | Falling | Tuopu/Xusheng + castings base | None |

### Bottleneck migration map (Semis #1 applied — always re-locate)

| Period | Binding constraint | Status Aug 2026 |
|---|---|---|
| 2024–H1 2025 | Roller-screw thread-grinding machines (Swiss/German/Japanese lead times) | **Broken**: Chinese grinder integration + thread-rolling substitution; the −80% price collapse is the evidence |
| 2025–2026 | Hand micro-actuation (delayed Optimus V3); Japanese-grade flexsplines/flexible bearings for the Western chain | Live: hands are the highest-churn subsystem; HDS single-supplier for non-Chinese strainwave |
| 2026–2027 | NdFeB magnets ex-China (political, not industrial); reliability data (no OEM publishes MTBF); autonomy data flywheels | Live: the Nov 10, 2026 second-wave decision is the single scheduled catalyst |
| Never bottleneck | Cameras, IMU, MLCC, battery cells | Ride existing smartphone/EV scale |

### Two parallel stacks (Semis #16 at system level)

| Dimension     | Western stack                                                                                               | China stack                                                                                                          |
| ------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Brain         | Jetson Thor $2,999 / Tesla AI5 (TSMC, volume 2027)                                                          | Rockchip RK3588-class $100–150; Horizon/D-Robotics; Black Sesame                                                     |
| Rotary joint  | Harmonic (HDS qualification gate)                                                                           | Harmonic (Leaderdrive/Shuanghuan) or QDD (Unitree: gate deleted)                                                    |
| Sensor suite  | Cameras + tactile, LiDAR-free trend                                                                         | Cameras + LiDAR + depth (Orbbec/Hesai/RoboSense), in-housing trend                                                   |
| Magnet access | Licensed/throttled; DoD floors from 2027–28                                                                 | Native, ~90% of global supply                                                                                        |
| Market access | US ban on Chinese finished robots (Jul 2026)                                                                | >85% of global demand is domestic                                                                                    |
| Unit volume   | ~3% of H1 2026 shipments                                                                                    | 97% of H1 2026 shipments                                                                                             |
| BoM           | $50–150k                                                                                                    | ~$35k (G1 teardown $8,976)                                                                                           |
| Contradiction | Chinese content inside US flagships (Xusheng→Figure [R]; ~70% of Optimus BoM [R]) unresolved as of Aug 2026 | Jetson still in premium Chinese units; "could shift if Chinese edge accelerators become more capable" (SemiAnalysis) |

### Maturity ladder (the Seeing-Stack discipline applied to robots)

Demo ≠ pilot ≠ teleoperated deployment ≠ autonomous deployment ≠ paid autonomous work ≠ scaled fleet with published reliability. Collapsing these states is the recurring sell-side error (BofA "mass adoption starts 2028"): it treats pilots as production. Current census: **paid autonomous work**: Agility–GXO (100k+ totes, paying contracts with Toyota/Mercado Libre); **autonomous deployment, company-reported**: Figure–BMW (30k vehicles' parts loaded, Helix-02 fleet), UBTech at Foxconn/BYD/Geely/Airbus, Xiaomi single-station; **teleoperated deployment**: most Unitree labor pilots (~250 units per SemiAnalysis), 1X NEO in homes; **demo/showcase**: the majority of the 19k H1 2026 units. No OEM at any tier publishes MTBF or fleet-uptime data.

### Mental models applied (hypotheses to test, per the READING PROTOCOL — not verdicts)

- **[G-4] Perez frenzy signature**: capacity 100× demand, IPO wave (Unitree 8,000× oversubscribed), VC 2× record YTD, state subsidy torrent. Hypothesis: installation-phase over-build → shakeout → deployment-phase winners are operators/appliers, not the component makers funding the build-out. Counter-hypothesis: China's state absorption (15th FYP) sustains the build-out long enough for unit economics to arrive, EV-style; the 2015–2020 China EV subsidy bridge is the precedent that worked.
- **[G-10] base rate**: BofA's 90k (2026) → 1.2M (2030) requires a 4-year 91% unit CAGR. Reference class: global EVs took 6 years for the same multiple (2011–2017) with purchase subsidies and an existing dealer/fuel infrastructure; drones did it faster but at 1/20th the unit price. The forecast is possible only under China-EV-style state absorption, which the 15th FYP explicitly provides. Both directions live.
- **[G-13] expectations spread**: Leaderdrive >300× trailing vs Shuanghuan ~26× vs Sanhua 20–25× core-plus-free-option: the same component category priced as three different businesses. The research question is not "is humanoid real" but "which of these prices survives the first capacity-glut down-cycle."
- **[G-14] Jevons for labor**: SemiAnalysis's conservative teleop case already passes below $30/hr human labor. Each robot-hour cost tier crossed unlocks a categorically larger labor pool; this is the mechanism that makes the demand S-curve convex if autonomy arrives.
- **Semis #2 inverted, gate deletion**: China's repeated move is not crossing the qualification gate but choosing architectures that delete it (QDD vs flexspline, current-sensing vs F/T, vision vs LiDAR). The test for any "moat" claim in this chain is whether an architecture change can delete the gate entirely.
- **Semis #3/#17**: inventory-and-capacity cycle mechanics with supply *leading* demand: the glut arrives without a demand shock. Component ASPs have no floor until consolidation; treat every Chinese component name as a true cyclical pre-shakeout (Semis #13 classification), whatever the growth narrative.
- **[[Lens - Value Layer Monopoly]]**: run the filter: merchant components = NO FIT (commoditizing layer, collapsing switching costs); magnets = STRONG FIT but state-owned (investable only via Western policy-floored proxies); NVIDIA sim+brain = toll-collector on the Western stack only; tactile = vacant layer (no incumbent to disqualify); VLA/data layer = the emerging-monopoly candidate (Helix's proprietary deployment data vs open GR00T/pi-0, unresolved). The only emerging, investable, mispriced layer candidates are tactile industrialization and the VLA data flywheel; everything else is either priced, state-owned, or commoditizing.
- **[[Lens - Automation & AI Readiness]] §6 heavy-physical bound**: automation of physical work is real but capped and slow; the lens's Lens-B inversion (sell the layer, don't own the automation) survives, but with the correction that the picks-and-shovels themselves are commoditizing. The durable Lens-B seats are simulation/training infrastructure (NVDA) and whichever tactile/data layers concentrate.

## Value chain map

### Layer 1 — Actuation & transmission (~50–60% of BoM)

**Rotary/reducers.** Harmonic Drive Systems 6324.T: humanoid orders ~¥1.3B booked fiscal Q2 2025, ¥2.5B expected FY3/26, company guides possible 2–3× in FY3/27 on "US client prototype visibility" [C]; Jun-2026 quarter total orders ¥24.1B +56% YoY [C]. The unnamed US clients are speculated Figure/Apptronik [R]. Leaderdrive 688017.SS: 2025 revenue ¥570.7M +47%, NP ¥124.4M [C]; claimed Tesla/Figure supply-chain entry [R]; >300× trailing P/E. Shuanghuan 002472.SZ: supplies Unitree [B], ~26× trailing (diluted by auto-gear core). Nabtesco 6268.T RV gears largely absent from humanoids (weight). Unitree: in-house QDD (motor + <20:1 planetary), no merchant reducer purchase: the anti-harmonic architecture, 95–98% efficiency vs 85–90% strainwave, up to 80% cheaper (per SemiAnalysis, already in vault).

**Linear/screws.** The 2024–25 grinding-machine bottleneck is substantially eased [B]: Shuanglin 300100.SZ acquired grinder-maker Kezhixin (per-line capex ¥10M→¥3M, efficiency +75% [C/B]); Hengli 601100.SS completed a roller-screw plant end-2025 (2.6M sets/yr claimed [B]; Morningstar: near-term humanoid revenue immaterial [B]); Beite 603009.SS built a $260M dedicated factory [C]. China screw price ¥2,000 (~$280) vs European multi-$1,000s. IPO-hype marker: Xinjian Transmission raising ¥2.8B on Tesla-robot narrative with ball-screw revenue <10% of sales [C from prospectus coverage].

**Motors, encoders, bearings.** No merchant frameless-motor supplier has a confirmed Optimus win: Tesla motor design is in-house [B consensus]. Moons' 603728.SS claims maxon-comparable coreless at a fraction of price [C marketing]. MPS (MPWR) is the quiet integrated play: MagAlpha position sensing + joint modules, CEO on Q2 2026 call: US and China robot programs "are all using MPS solutions" [C]. Encoders: dual per precision joint → 40–80 channels/robot; RLS/Renishaw, Heidenhain, ams-Osram, Chinese chip-on-board [cost data weak]. Bearings are the quietest link: 14–20 crossed-roller per robot; flexible (thin-race) bearings for harmonic drives are a hidden precision choke with few qualified makers outside HDS in-house [B].

**Magnets**: see Summary ¶4 and Geopolitical overlay. The one layer with durable pricing power; not investable inside China; Western expression: MP (DoD $110/kg NdPr floor + 100% 10X offtake, and entity-listed by MOFCOM, so now a political football), Lynas LYC.AX, Neo NEO.TO (record Q2 2026 EBITDA "amid rare earth supply crisis" [C]), JL MAG 300748.SZ (humanoid magnet-assembly unit run by the CEO, initial mass production [C]) on the China side.

### Layer 2 — Dexterous hands (the frontier subsystem)

The hand is where the reliability, cost, and architecture problems concentrate: it delayed Optimus V3 [R], it is the least mature and fastest-churning subsystem, and BofA projects it at 19% of 2030 BoM [B]. Tesla V3: tendon-driven, ~22 DoF/hand, ~25 actuators per forearm [C patents; production config unconfirmed]. Figure 03: DoF unpublished; palm camera + 3-gram tactile per hand [C]. China volume: LinkerBot ~5,000 hands/month claimed across 5 factories, sub-$5k models [C claims]; Inspire ~10,000 cumulative at $3–8k [B/C]; Wonik Allegro <$25k; Shadow >$100k as the Western anchor. The listed merchant angle is not the hand but the finger micro-drive: Zhaowei 003021.SZ/2692.HK (HK IPO 2026-03-09) sells integrated micro-motor + planetary + micro-ball-screw finger modules [C]; Optimus status [R].

### Layer 3 — Sensing (~10–15% of BoM, falling on the China stack)

**Cameras/CIS.** Global shutter is the robot requirement; camera counts 2–8. OmniVision (Will Semi 603501.SS) has the most explicit humanoid product line (OG02B10 GS + OAX4000 on Jetson [C]); Sony's robotics CIS presence is real but research-grade (Ace table-tennis robot: 9× IMX273 GS + 3× IMX636 event sensors [C]); onsemi Hyperlux SG is marketing-stage. The Sony–TSMC Kumamoto JV targets smartphone sensors first; physical-AI is framing, no robotics CIS product announced [C]. Scale check: 60k robots × 5 cameras = 300k sensors/yr, a rounding error against 1B+ phone CIS units. CIS becomes a humanoid earnings line only above ~10M robots/yr, which no broker base case reaches before 2030.

**Depth.** RealSense (spun out of Intel 2025-07, $50M, NVIDIA collaboration) claims presence in 80% of humanoids [C, unaudited]: the G1's D435i is the flagship socket, but Unitree is in-housing. Orbbec 688322.SS is the real-revenue name: FY2025 RMB 941M +66.7%, first profitability, Gemini 330 validated on Jetson Thor, wrist-mount Gemini 305 for manipulation at CES 2026 [C].

**LiDAR: the squeezed middle.** Hesai FY2025: RMB 3.03B revenue, 1.62M total units of which ~240k robotics; Q1 2026 robotics 118k units +138% YoY; humanoid segment guided to only "5-digit" 2026 units [all C]; robotics LiDAR volume today is lawnmowers and AMRs, and humanoid attach is a China-stack feature worth ~$10–20M revenue. RoboSense 2498.HK: robotics division RMB 709M FY2025 at 39.7% GM, first quarterly profit, Q1 2026 robotics shipments +1,459% YoY [C]; also building its own embodied hardware (Papert 2.0 hand, Active Camera AC1/AC2 with a "leading European humanoid" mass-production order [C via Gasgoo]). Tesla and UBTech run without/with-demoted LiDAR; Unitree sells its own L2 at $419 retail. LiDAR long-term humanoid attach is a live short-thesis question, not a growth assumption.

**Tactile: the vacant layer.** Figure surveyed all merchant fingertip options and rejected them on durability/reliability, building in-house [C]: direct evidence no at-scale vendor exists. PaXini (DexH13 1,140 taxels; TORA-ONE 2,000+), Tashan (haptic ASIC approach), GelSight/Meta Digit 360 (research economics) are the field; Keli 603662.SS tactile is "research and verification stage" [C]. AAC 2018.HK and Goertek 002241.SZ entering via CES 2026 humanoid subsystem lines is the signal to watch: the smartphone-supply-chain-absorbs-the-category pattern that produced DJI's component base.

**F/T, IMU, audio.** Six-axis F/T at wrists/ankles persists in most commercial designs (Walker S2, Optimus feet [R]) while the deletion trend runs through architecture (QDD current-sensing); ATI/Novanta launched the humanoid-specific "Varo" sensor [C]; Chinese entrants (Kunwei, Blue Point, Keli serial 6-axis [C]) undercut. IMUs 1–3 per robot; STMicro reported as Optimus IMU supplier [R]. Audio: 4-mic arrays standard (G1, Walker S2 [C]).

### Layer 4 — Compute & autonomy

**Brain socket.** Jetson Thor GA 2025-08-25: 2,070 FP4 TFLOPS, 128GB, $2,999/module at 1k volume; named adopters Agility (Digit 6th-gen), Boston Dynamics Atlas, Figure, Amazon Robotics [C]. Chinese volume humanoids run Rockchip RK3588-class ($100–150) + MCU cerebellum [B]; Horizon's D-Robotics and Black Sesame's edge pivot compete for the domestic socket; Qualcomm entered at CES 2026 with Dragonwing IQ10 (700 TOPS, Figure named an ecosystem partner [C]). Tesla AI5 taped out ~April 2026, TSMC primary with Samsung following, volume 2027 [C], which contradicts "V3 production summer 2026" unless early V3 units carry AI4-class or interim silicon; Tesla has never said [confirmed timeline gap]. TrendForce sizes the humanoid chip market at just $48M by 2028 [B]: the brain socket is a rounding error for [[Theses/NVDA - Nvidia]] earnings; the NVDA expression remains simulation/training (Isaac, Cosmos, GR00T N2 claiming >2× VLA task success, available end-2026 [C]) and the option on Western unit inflection.

**VLA layer.** Base models commoditizing (GR00T open, pi-0/0.5 open-source, $600M at $5.6B for Physical Intelligence [C]); deployed performance concentrating in vertical stacks: Helix-02 is the only VLA with multi-day, third-party-site, throughput-quantified autonomous operation (167 hrs / 209k packages / 24-hr nonstop run, all company-reported [C]). Hyperscalers are option-buying across the layer: DeepMind→Apptronik + Boston Dynamics, OpenAI→1X, NVIDIA→everyone. Where the data flywheel consolidates (OEM-vertical vs merchant) is the single most important unresolved question for eventual layer-monopoly formation.

### Layer 5 — Power, passives, structure

Battery: average <2.5 kWh (Optimus ~2.3 kWh EV-grade cells [B teardown]; Unitree H1 0.86 kWh); runtime and thermals, not cell cost, are the binding constraint (10–15 min heavy work on G1 per the vault's SemiAnalysis note; real-world 2–6 hr light duty). Fourier ships hot-swap packs; Figure 03 inductively charges through its feet [C]. Samsung SDI showed the first pouch all-solid-state battery explicitly for humanoids (InterBattery 2026-03, MP target 2H 2027) with a Hyundai/Kia robot-battery MoU [C]; EVE's Longquan solid-state line targets humanoids [C]; CATL/BYD are publicly less optimistic on solid-state economics [C]; solid-state is being marketed robot-first because robots tolerate high $/kWh, a niche-beachhead pattern worth tracking for [[Theses/CATL - Contemporary Amperex Technology]] (whose thesis currently contains zero robot content, a gap). GaN: EPC shipped the first GaN-IC humanoid joint reference designs (EPC91118/91122, 66% smaller than Si [C]); Infineon platform live, no flagship win named. MLCC: no official per-humanoid count exists [confirmed absence]; EV-class thousands is the working triangulation: 60k robots ≈ low-hundreds-of-millions of MLCCs, immaterial against AI-server demand already straining [[Theses/6981 - Murata Manufacturing]] / [[Theses/6976 - Taiyo Yuden]] capacity; humanoids are a 2027+ increment, not a current driver. Structure: Tuopu 601689.SS ("Tier 0.5" Optimus actuator-assembly + structural claims, Tesla = 35–40% of revenue via autos [B/R]); Xusheng 603305.SS magnesium shells reportedly inside Figure [R].

## OEM landscape and demand reality (Aug 2026)

| OEM | Cumulative/2025 | H1 2026 / status | Reality check |
|---|---|---|---|
| Agibot/Zhiyuan | 10,000th unit Mar 2026 [C] | ~8,400 units, 44% share: #1 [B, SAG] | Domestic industrial/commercial + state-adjacent; STAR back-door via Swancor closing [C] |
| Unitree | 5,500 humanoids 2025, RMB 1.7B revenue 4× YoY, ~60% GM [C prospectus] | ~5,900 units, 31% share; IPO priced $9.04B, 8,000× oversubscribed [C] | Buyers mostly developers/education/showcase; R1 at $5,900 |
| UBTech 9880.HK | 1,079 shipped 2025 [C] | Walker S2 mass production; orders RMB 800M→~$195M; Foxconn/BYD/Geely/Airbus [C] | The most industrial Chinese deployment book; 2026 capacity target 5k |
| Tesla | Hundreds vs 5–10k target [C miss] | V3 production start slipped to late Jul/Aug 2026; rate "impossible to predict" (Musk) [C] | Q4-25 admission: internal units do learning/data collection, not productive work; AI5 volume silicon 2027 |
| Figure | Few hundred [B] | BotQ 1 robot/90 min, doubling monthly; $39B post Series C [C] | BMW Spartanburg deployment real but company-reported; customer #2 (UPS) [R] |
| Agility | Small fleet | Digit 6th-gen on Thor | The only paid autonomous work claim: GXO 100k+ totes, Toyota/Mercado Libre contracts [C] |
| Apptronik | Pilots (Mercedes, GXO, Jabil) | Apollo 2 = data platform; Apollo 3 = first commercial product, 2027 [C admission] | +$520M 2026 |
| Boston Dynamics | Low volume | All 2026 Atlas committed: Hyundai Metaplant + DeepMind [C] | Hyundai-internal absorption |
| 1X | First NEO deliveries 2026, $20k | Launch reviews: zero autonomous completion, heavy teleop [C hostile reviews] | The consumer-teleop cautionary tale |
| Xpeng / Xiaomi / BYD | 0 commercial / internal pilots / ~150 prototypes | IRON trial production, MP "end-2026" [C claim]; Xiaomi 98% single station [C]; BYD debut Aug 2026, "20k in 2026" [R] | Auto-OEM internal absorption is China's demand backstop |
| Sanctuary | — | Abandoned humanoid; software pivot [C] | First capitulation of the cycle |

**Forecast spread** (all [B]): Morgan Stanley $5T/1B units by 2050, China 446k units/yr by 2030 (doubled Jun 2026); Goldman $38B by 2035; BofA 1.2M units 2030, 10M/yr 2035, 3B in service 2060; UBS $1.4–1.7T by 2050; Citi $7T. The 2050 estimates disagree by 5×. Near-term consensus clusters at 50–90k units for 2026, against which SAG's ~$1.6B 2026 industry revenue implies a ~$27k blended ASP, already deflating.

## Geopolitical overlay

| Date | Action | Bloc |
|---|---|---|
| 2025-04-04 | MOFCOM licensing on 7 medium/heavy REEs + magnets; Musk confirms Optimus production affected (Apr 23) | CN |
| 2025-10-09 | Sweeping expansion (0.1% de-minimis, extraterritorial) | CN |
| 2025-11 | Post-Busan: Oct package suspended 1 yr (to 2026-11-10); April controls + licensing infrastructure preserved | CN |
| 2026-01-01 | Sm/Gd/Lu compounds added to licensing catalogue | CN |
| 2026-06-17 | G7 Paris: cap single-country RE imports <60% by 2030 | West |
| 2026-06-22 | MP Materials + USA Rare Earth entity-listed (worldwide transfer ban) | CN |
| 2026-07-20 | Reuters: zero June Ga/Dy/Tb/Y shipments to Japan: throttling as enforcement | CN |
| 2026-07-29 | US bans new Chinese humanoid/quadruped imports (FCC Covered List); NDAA narrows GUARD Act to military-procurement ban | US |
| 2026-11-10 | **Scheduled**: second control wave (Ho, Er, Tm, Eu, Yb) takes effect unless re-suspended | CN |
| 2027-01-01 | US defense sourcing bars Chinese-origin NdFeB through full chain | US |

The standoff structure: China holds magnets (~90%) and unit production (97%); the US holds finished-robot market access and leading-edge AI silicon. Both flagship Western programs carry unresolved Chinese content exposure [R], and the Chinese premium stack still carries NVIDIA silicon: mutual dependence that each control wave ratchets down. Semis #15 corollary: subsidized magnet-capacity duplication (MP/Lynas/Neo vs 190kt China) bakes in a structurally lower-margin Western magnet supply unless policy floors (the $110/kg NdPr model) persist, which converts magnet proxies into policy-duration bets.

## Adoption framework — dating the S-curve

Pre-chasm (per [G-4]/[G-10]): binary outcome distribution, demand dominated by early-adopter/showcase buyers, no reliability data, teleop dependence. Falsifiable chasm-crossing markers, in expected order:

1. **Any OEM publishes MTBF / fleet-uptime data**: the industry-wide silence is the tell; first publication signals confidence, not marketing (parallel: the 800VDC insurance-actuarial gate).
2. **A non-Chinese, non-state customer reorders >100 units**: Figure–BMW expansion, UPS confirmation, or a GXO fleet order would be the first arms-length repeat-purchase evidence.
3. **Robot-hour all-in cost < $10/hr at two-shift utilization**: SemiAnalysis's <$30/hr teleop case must survive de-teleoping (operator ratios disclosed <1:10).
4. **Duty-cycle parity**: sustained 6–8 hr work shifts (vs 10–15 min heavy-work thermal ceilings today); watch actuator thermal design and battery swap logistics, not demo reels.
5. **An insurance/warranty market forms** for humanoid fleets.

Scenario spine for 2030 global units: bear ~200–300k (China-only absorption, autonomy stalls at teleop, Western programs consolidate to 2–3 survivors); base ~500k–1M (Goldman/MS-China trajectory: state-absorbed Chinese volume + narrow-task Western logistics fleets); bull 1.2M+ (BofA: requires markers 1–4 all firing by 2028). In every scenario the component layer consolidates: the shakeout among ~200 Chinese humanoid makers and their suppliers is a when, not if; position for post-shakeout survivors, not pre-shakeout capacity.

## Affected vault theses and sector notes

### Direct exposure

| Vault entity | Impact | Read |
|---|---|---|
| [[Theses/NVDA - Nvidia]] | Physical-AI pillar: Thor design wins (Agility/BD/Figure/Amazon) + GR00T N2 + Isaac/Cosmos | Confirms the §Bull Case physical-AI narrative as an option, not earnings: $48M 2028 chip TAM [B] vs $5T 2050 narratives is the widest near/terminal gap in the vault. China-domestic compute substitution flag (already planted by the Unitree note) unchanged: 97% of units don't carry NVIDIA |
| [[Theses/TSM - Taiwan Semiconductor]] | Fabs Tesla AI5 (taped out, volume 2027) + Thor + Sony CIS JV | Supportive color on the platform-export leg; CIS robot volumes trivial before 2030, per the existing CIS note: no new trigger, do not invent a CIS-volume HIGH |
| [[Theses/TER - Teradyne]] | UR cobots = the incumbent automation the humanoid TAM must displace; same factory-automation demand near-term | Two-sided: humanoid frenzy re-rates robotics-adjacent multiples (supportive) but UBTech Walker S2 at Foxconn is the first humanoid landing on electronics assembly, UR's home turf. Watch cobot vs humanoid win-rates at shared customers from 2027 |
| [[Theses/ISRG - Intuitive Surgical]] | Risk #11 (humanoid long-tail convergence) | Cost-curve datapoint only; regulatory/clinical walls unchanged: no probability update |
| [[Theses/CATL - Contemporary Amperex Technology]] | Robot batteries + solid-state niche-beachhead + robotics ecosystem investments | **Thesis gap: zero robot content today.** Samsung SDI is moving first (dedicated robot cells, solid-state 2H 2027 MP target); flag for next CATL /sync or /deepen |
| [[Theses/6981 - Murata Manufacturing]] / [[Theses/6976 - Taiyo Yuden]] | EV-class thousands of MLCCs per robot | Immaterial vs AI-server demand through 2027+; do not double-count with the 800VDC MLCC thesis |
| [[Theses/ARM - Arm Holdings]] | Cortex-M cerebellum + joint MCUs across both blocs | Royalty content per robot is small; volume story only at multi-million units |
| [[Theses/NBIS - Nebius Group]] | Avride delivery robots: >600k deliveries, monetizing today | Supports the form-factor caveat below: wheeled task-specific robots are absorbing the near-term economic use cases while humanoids demo |

### Sector notes

- [[Sectors/Compute & AI Compute Accelerators]]: edge-inference socket bifurcation (Thor vs RK3588-class) belongs in §Macro shifts
- [[Sectors/Surgical Robotics]]: convergence-risk horizon unchanged; cost-curve data updated here
- [[Sectors/Batteries & Energy Storage]]: solid-state robot-first beachhead pattern (Samsung SDI, EVE) vs CATL/BYD skepticism
- [[Sectors/MLCC & Power Semiconductors]]: humanoid MLCC/GaN content as a 2027+ increment
- [[Sectors/Semiconductor Foundries]]: AI5/Thor/CIS all traverse TSMC
- No Robotics sector note exists; this macro note serves as the MOC until a direct position justifies one

## Trade implications and monitoring

**No new position now.** The vault already holds the durable layer (NVDA simulation/brain toll, TSM as the fab everything traverses, TER cobot incumbency). Direct humanoid exposure fails the [G-13] test today: every pure-play either has no earnings (Western OEMs), untested public financials (Unitree lists this month), or price-implied expectations assuming the capacity glut never arrives (A-share component complex).

**Watchlist: real revenue, defined triggers:**

| Name | Why | Trigger to act |
|---|---|---|
| Harmonic Drive Systems 6324.T | Only Western-qualified strainwave seat; humanoid orders ¥2.5B FY3/26 guided to possibly 2–3× FY3/27 [C] | FY3/27 guidance confirms the 2–3×; named US customer disclosure. Risk: QDD architecture-substitution is the standing short thesis |
| RoboSense 2498.HK | Robotics RMB 709M at 39.7% GM, first profit, +1,459% Q1 shipments [C]; hands+cameras+LiDAR full-stack pivot | Humanoid revenue broken out ≥20% of robotics segment |
| Hesai HSAI | Robotics 240k units FY25; Q2 print 2026-08-18 (four days out) | Humanoid guidance raised above "5-digit" units; robotics GM disclosure |
| Orbbec 688322.SS | The de-facto China depth standard; profitable, +67% [C] | Non-China OEM design win (would break the bloc wall) |
| Unitree (STAR, post-IPO) | The vertically-integrated BYD-pattern play; 60% GM at $16k ASP if prospectus holds | First two public quarters confirm GM and non-showcase customer mix |
| AAC 2018.HK / Goertek 002241.SZ | Consumer-electronics Tier-1s entering hands/tactile/acoustics: the DJI-absorption pattern | First humanoid OEM design win disclosed with volume |
| MP / Lynas LYC.AX / Neo NEO.TO | The only durable-pricing-power layer, policy-floored | Nov 10, 2026 second-wave outcome; treat as rare-earth theses humanoids amplify |
| Zhaowei 003021.SZ | Finger micro-drive merchant module play | Confirmed (non-rumor) flagship hand-module PO |

**Avoid list:** Leaderdrive at >300× trailing; the A-share Optimus-rumor complex wholesale (Sanhua formally denied the $685M order rumor [C], and the Sanhua-rotary vs Tuopu-"exclusive rotary" contradiction proves the circulating supplier lists contain fabrication); Xinjian-style narrative IPOs (<10% revenue relevance); consumer teleop plays (1X pattern).

**Kill-criteria / framework-change triggers:**

| Trigger | Impact |
|---|---|
| Nov 10, 2026: second control wave takes effect | Western actuator costs step up; magnet proxies re-rate; Western OEM BoM targets slip |
| Unitree first public prints miss prospectus GM (60%) | The China cost-structure thesis (SemiAnalysis) takes direct damage; component glut confirms faster |
| Tesla V3 exits 2026 below ~5k cumulative units | A-share supplier complex de-rates; watch for the capitulation entry into post-shakeout survivors |
| Figure customer #2 confirmed + BMW expansion | First arms-length repeat-purchase evidence; Western stack (HDS, Thor chain) upgrades |
| Any OEM publishes MTBF/uptime data | Chasm-marker #1 fires; move watchlist names to active evaluation |
| A Chinese edge-accelerator displaces Jetson in a premium Chinese humanoid | NVDA physical-AI option value haircut (the flag the Unitree note planted) |
| GR00T-class open VLA matches Helix-02 deployment metrics at a third-party site | Data-flywheel-as-moat hypothesis weakens; software layer commoditizes like the hardware |

## Caveats and open questions

1. **Every Optimus supplier identification in circulation is unverified.** Tesla confirms nothing; Sanhua denied the headline order rumor; the Sanhua/Tuopu "exclusive rotary" contradiction is arithmetic proof of fabrication somewhere in the lists. Chinese A-shares have repeatedly limit-upped on fake supplier lists through Jul 2026.
2. **Shipment counts conflict at the 2× level** (Omdia 13.3k vs alternates 18k for 2025; SAG 19.1k H1 2026 global vs CMRA >30k China-only). All share and growth claims inherit this methodology chaos.
3. **Deployment metrics are company-reported without independent audit**: Figure's hours/packages, UBTech's order book, Agility's tote counts. No third-party verification exists anywhere in the sector.
4. **BoM decompositions are broker teardowns with wide error bars**: magnet content spans 1.3–6 kg/robot (4.6×); encoder costs are inference; MLCC counts are unpublished.
5. **The near-term/terminal gap is the widest of any vault macro**: $48M humanoid chip TAM by 2028 [B, TrendForce] against $5–7T 2050 market narratives. Any position sized on the terminal number is sized on faith.
6. **Humanoid may be the wrong abstraction.** Wheeled and task-specific embodied platforms (Galbot retail pickers, AI2 Robotics, Avride delivery, all monetizing now) may absorb the economic use cases while bipeds solve balance and thermals. The humanoid-form premium is itself an unproven hypothesis; the labor TAM does not care about legs.
7. **Reliability data vacuum**: no OEM publishes MTBF, service intervals, or fleet uptime. Until one does, every deployment claim is a demo with better production values.
8. **This note is built on three same-day web sweeps plus two vault deep-dives**; single-source claims are flagged but not independently verified. Q2/Q3 2026 prints (Hesai Aug 18, Unitree debut, HDS H1) will retire or harden multiple load-bearing numbers within weeks.

## Open Questions

- **Should the vault ever own the robot makers, or only the layers?** Current answer: layers. Revisit only if Unitree's public prints validate 60% GM at falling ASPs (which would make it the BYD of the category) or a Western OEM shows arms-length repeat purchases.
- **Does the tactile vacancy get filled by consumer-electronics Tier-1s** (AAC, Goertek, Luxshare), and does that produce the next Sunny-Optical-pattern re-rate, or does in-house (Figure, Tesla) capture it permanently?
- **Where does the autonomy data flywheel consolidate**, OEM-vertical (Helix) or merchant (GR00T/pi-0)? This decides whether a VLA layer monopoly forms and who owns it. The hyperscaler option-buying (DeepMind, OpenAI, NVIDIA) suggests they think it's the former and are hedging.
- **Does Optimus V3's actual H2 2026 run-rate validate or kill the A-share supplier complex?** The AI5-silicon-timing contradiction (volume 2027) argues for slower than Musk's 50–150k 2026 guidance by an order of magnitude.
- **What does the Nov 10, 2026 decision reveal about China's magnet strategy**: ratchet (second wave proceeds), hold (re-suspension), or trade (linked to US robot-import-ban relief)? Each path re-prices the Western magnet proxies differently.
- **When does humanoid CIS demand become a Sony/TSMC earnings line?** Requires ~10M+ robots/yr at 5–8 cameras, post-2030 in every broker base case; the JV's physical-AI framing is a 2029+ option, consistent with the vault's existing no-new-trigger stance.

## Related Research

- [[Research/2026-08-13 - Unitree Humanoid Robotics China Trajectory - deep-dive]]: the cost-structure anchor (QDD, $8,976 BoM, BYD/DJI playbook); this note answers its closing research question
- [[Research/2026-08-13 - TSM SONY TSMC Sony vs China CIS Ecosystem - deep-dive]]: the sensing-stack geopolitics anchor (four-ecosystem CIS split, physical-AI chain: sensor → connectivity → memory → compute → software → actuator)
- [[Research/2026-08-13 - Superposition Seeing Stack Map US JP KR EU - deep-dive]]: the maturity-ladder discipline (capability ≠ program linkage ≠ control ≠ profit pool) applied here to robot deployments
- [[Research/2026-04-23 - ISRG - Industrial Robotics Convergence Risk - deep-dive]]: the surgical-robotics convergence horizon this note's cost curves feed
- [[Research/2026-04-23 - NVDA - CUDA Moat and Omniverse Upside - deep-dive]]: the simulation/training layer where NVDA's durable robotics seat sits

## Log

### 2026-08-14
- Initial macro note created from three parallel web-research sweeps (actuation/mechanical; sensing; compute/power/OEM landscape) synthesized against the two 2026-08-13 vault deep-dives (SemiAnalysis Unitree, TSPA CIS). Core frame: no-bottleneck supply chain (capacity ~100× demand, −80% screw / −99.5% LiDAR price collapses) → merchant component pricing power structurally absent; durable layers are NdFeB magnets (state chokepoint; Nov 10, 2026 second-wave decision is the scheduled catalyst) and the VLA/data layer (Helix-02 the only audited-adjacent deployment record). Two-bloc bifurcation complete at robot level (97% China units, US import ban Jul 2026, MP/USAR entity-listed Jun 2026). Verdict: no new position; vault already holds the durable layer via NVDA/TSM/TER; 8-name watchlist with defined triggers (HDS FY3/27 guidance, Hesai Aug 18 print, Unitree post-IPO prints, RoboSense humanoid breakout, AAC/Goertek design wins, Zhaowei confirmed PO, magnet proxies on Nov 10 outcome). Thesis gap flagged: [[Theses/CATL - Contemporary Amperex Technology]] contains zero robot-battery content while Samsung SDI moves first. Propagation candidates for next /sync: NVDA (physical-AI option framing + $48M 2028 chip TAM), TSM (no new trigger, supportive color), TER (cobot-vs-humanoid collision watch at Foxconn), CATL (gap fill), Murata/Taiyo Yuden (do-not-double-count guard). Suggest /graph last after propagation.

### 2026-08-14 (/sync all)
- Propagation completed to affected theses: TER (Risk #6 — humanoid-on-electronics-assembly vs UR cobot turf), CATL (Outstanding Question — robot-battery / solid-state gap vs Samsung SDI/EVE robot-first), NVDA (Log — physical-AI-as-option, $48M 2028 chip TAM, 97% non-NVDA units). TSM / 6981 / 6976 / ISRG / ARM / NBIS considered — no material delta per this note's own no-new-trigger / immaterial / do-not-double-count guidance. Sector notes (Compute & AI Accelerators, Batteries & Energy Storage, MLCC & Power, Surgical Robotics, Semiconductor Foundries) deferred as 2027+ increments — candidates for future /deepen, not this sync. Run /graph last to reconcile the new thesis↔macro edges.

### 2026-08-20
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged
