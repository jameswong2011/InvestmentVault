---
publish: false
date: 2026-06-06
tags: [research, data-center-power, 800VDC, VRT, NVDA, META, deep-dive]
sector: Data Center Power & Cooling
ticker: VRT
source: 'https://substack.com/home/post/p-198743508'
source_type: deep-dive
---

# 800VDC Revolution Part 1 — Datacenter Layout and Equipment Impact

*SemiAnalysis (Nicolas Bontigui), published 2026-05-26. Part 1 of a two-part series; covers datacenter layout and equipment implications. Part 2 will cover power electronics and the semiconductor layer. Contributors: DG Matrix, Novos Power, Aran Industries. Built on SemiAnalysis's Industrials Model (20+ datacenter designs, 70+ equipment types, 500+ suppliers) and Datacenter Model (6,000+ datacenters). Paywall begins at the "Equipment Supplier Impact" section — the winner/loser calls below are SemiAnalysis's proprietary view.*

## Thesis Delta

This is a bottom-up **4-phase 800VDC adoption framework** with phase-specific TAM, equipment-content/MW, and efficiency numbers — the quantitative scaffolding the existing [[Macro & Technology/800VDC Adoption]] note covered only qualitatively. The investment-relevant call: **white-space vendors win over grey-space**, because their content uplift is large, immediate, and tied to a 3–4yr rack-refresh cycle rather than a 10–15yr facility cycle. It sharpens [[Theses/VRT - Vertiv Holdings]] (won Meta's 800V power-rack program alongside Delta; retrofit content is *additive* — legacy UPS stays at ~$1M/MW grey + power rack stacks ~$1M/MW white), names **Delta Electronics (2308 TT)** as the structural winner the vault does not yet hold, and flags **Legrand (LR FP)** as consensus-mispriced (~55% of DC revenue exposed vs management's claimed 20%). Primary sector: [[Sectors/Data Center Power & Cooling]]; adjacent: [[Sectors/Modular Power Conversion Components]] (on-board conversion layer, expanded in Part 2) and [[Sectors/MLCC & Power Semiconductors]] (SiC/GaN, SSCBs, supercaps, passives).

## Summary

The forcing function for 800VDC is **current, not efficiency**. At 600kW per rack (Kyber-class, Vera Rubin Ultra NVL576), a 48–54V bus carries ~12,500A; moving to 800V drops that to ~750A — a 16.7× cut that reduces I²R losses ~278× at constant conductor resistance. A 1MW rack at 48–54V needs ~200kg of copper busbars; at 1GW scale that is hundreds of tons. The efficiency gain (~5% of facility power, ~50MW saved at 1GW IT load) is real but secondary — the equity story is *compute-density unlock*, because cost-per-token is bounded by the size of the NVLink scale-up world you can build, and a single rack bounds the expert layer before all-to-all traffic falls onto a ~8× slower scale-out fabric. Bigger scale-up worlds force denser racks; denser racks force 600kW envelopes; 800VDC makes those envelopes physically possible. SemiAnalysis expects ~39GW of incremental 800VDC capacity by 2030.

The transition runs through **four phases**. Phase 1 (2026/27) is the "White Space Retrofit": a row-level HVDC power rack (sidecar) layers on top of existing AC distribution, deleting nothing, at a content delta of +$400–500k/MW. It is voluntary future-proofing led by Google and Meta through the OCP Mt. Diablo reference design — the chips ramping in 2026/27 (Vera Rubin NVL72, 180–220kW) can still be served by three-phase AC. Phase 2 (2027/28) is the real inflection: 800VDC-native compute (Kyber) arrives with no AC fallback at the rack inlet, the central UPS begins its slide to obsolescence, and the voltage step-down moves onto the compute blade. Phase 3 (late 28/29) rewrites the architecture — a centralized grey-space rectifier converts 415V AC to 800VDC for the whole hall, the "battery rack" replaces the power rack (~$200k/MW, no rectification), and DC busway plus solid-state circuit breakers (SSCBs) replace AC distribution. Phase 4 (>2029) is the SST end-state, collapsing the LV transformer and rectifier into a single MV-to-800VDC device.

The supplier read is a **share-shift, not a content explosion**: total electrical content per MW stays in a $3.6–4.8M band across four of the five modeled architectures (white-space retrofit is the outlier at $4.8M/MW), with value migrating from grey space to white space. **Delta** is the structural winner — grid-to-chip vertical integration, ~75% AI-server PSU share, and a power-shelf ASP that jumps from ~$40k (AC) to ~$400k (HVDC power rack), a 10× scope expansion. **Vertiv** is the grey-space leader pushing into white space, with a services moat (>20% of revenue) that compounds as 800VDC racks raise commissioning and uptime complexity. The losers are grey-space-levered names where mature 800VDC deletes content: **Legrand** (rPDU/busway exposure), **Forgent (FPS)** (pure grey-space, ~35% of DC revenue at risk), and **ABB** (which itself calls 800VDC a "post-2028 opportunity"). Sidecar TAM peaks ~$11B in 2028 before Phase 3 erodes it; SST TAM reaches ~$13B by 2030.

Adoption is gated by **real-world constraints, not silicon**: regulation (full NEC 800VDC support targets 2029, likely partial, with full maturity at NEC 2032/2035; pre-2029 needs site-by-site AHJ approval), DC arc-flash safety (IEEE 1584 does not cover DC; NFPA 70E has no PPE table for 600–1000VDC), grounding (no industry consensus across HRG / solid / floating / solid-grounded-return), AC-dependent cooling (no DC-native cooling ecosystem exists; chillers/pumps/fans stay on AC), and grid interconnection (NERC's May 2026 Level 3 alert, ERCOT NOGRR282). This is Part 1 (layout + equipment); the on-board power-electronics and semiconductor layer — where [[Theses/VICR - Vicor Corporation]] sits — is reserved for Part 2.

## Framework / Mental Model

### The 4-Phase 800VDC Transition Framework

SemiAnalysis builds adoption bottom-up: chip-by-chip SKU calculation × phase-by-phase adoption timeline × incremental datacenter capacity build. Through Phases 1–2 all addressable capacity is served by **sidecars** (the facility is still AC-distributed, so conversion happens at the power rack). The mix inflects in 2029 as facility-level HVDC distribution becomes viable, shifting the conversion stage upstream from the rack to the SST or MV rectifier.

| Phase | Timing | Core change | Equipment delta | Content/MW | Cumulative efficiency |
|---|---|---|---|---|---|
| 1 — White Space Retrofit | 2026/27 | Row-level HVDC power rack (sidecar) layers on existing AC; grey space untouched (same transformers, UPS, switchgear, ATS) | Adds power rack; deletes nothing | +$400–500k/MW | 83.7% (from 82.0% baseline) |
| 2 — Native Compute | 2027/28 | Kyber 800VDC-native; no AC fallback at rack; central UPS begins obsolescence; on-blade step-down to ~50V | Central UPS (~$1.2M) exits grey space | — | 86.5% (7→5 conversion stages) |
| 3 — Centralized Rectifier | late 2028/29 | AC→DC moves to grey-space/outdoor rectifier; battery rack replaces power rack; DC busway + SSCB protection | Rectifier + DC busway + battery rack (~$200k/MW); LV switchgear, AC floor PDUs eliminated | — | 86.9% |
| 4 — SST End-State | >2029 | SST replaces LV transformer + rectifier with one MV→800VDC device | SST (~$1.0–1.5M/MW) eliminates LV equip (~$0.55M/MW) + Phase-2 rectifier (~$0.20M/MW) | total ~$4.0M/MW | 87.4% |

Adoption is **voluntary in Phase 1, forced in Phase 2**: Phase 1 is hyperscaler future-proofing (Vera Rubin NVL72 tops out at 180–220kW, deliverable on three-phase AC), but Kyber-class racks have no AC fallback, so 800VDC penetration spikes once native silicon ships ahead of facility-level distribution being ready — which is why the retrofit/sidecar phase persists into 2028.

### The white-space vs grey-space heuristic (the investment lens)

The shift from standard AC/DC to HVDC is mainly a **share-shift story, not a content increase** — total electrical content per MW stays roughly flat at $3.7–4.0M/MW across most architectures (white-space retrofit the exception at $4.8M/MW). Prefer **white space** for three reasons: (1) content uplift is large and immediate (vendors move from selling power shelves to selling entire HVDC power racks); (2) white-space vendors already ship into 2025–26 deployments, while grey-space vendors mostly point to 2028; (3) white-space demand is tied to accelerator shipments and a 3–4yr rack-refresh cycle, structurally more attractive than grey-space's 10–15yr facility cycles and lumpy buildouts. Grey-space incumbents face removal of centralized UPS, LV switchgear, and LV transformers, with replacement content (SST) still early and lacking a clear winner — and white-space vendors competing for that future content too.

### The topology fork: single-ended 800V vs bipolar ±400V

"800VDC" denotes two distinct configurations, and the choice cascades into safety engineering, protection-device count, and semiconductor selection. **Single-ended 800V** (Nvidia) is one 800V rail referenced to return plus PE — at 1MW it carries 1,250A, with a simpler bus (no midpoint to sense/regulate) using standard high-voltage devices. **Bipolar ±400V** (OCP Diablo 400 default) splits 800V into two symmetric 400V rails around a grounded midpoint; the load still sees 800V but each rail sits only 400V from ground, letting the system reuse the mature EV 400V supply chain (650V GaN FETs, 400V-class caps/connectors/fuses) — Google's stated rationale at OCP EMEA 2025. The ±400V cost is a third conductor routed/terminated/protected at every rack, adding copper and complicating hot-swap connector sequencing. Diablo 400 permits both; Nvidia sits outside Diablo with a monopolar 800V design.

## Evidence

**TAM and equipment content**

| Item | Value | Note |
|---|---|---|
| Sidecar (power rack) TAM peak | ~$11B in 2028 | Declines as facility-level 800VDC takes share in Phase 3 |
| SST TAM | ~$13B by 2030 | Captures sidecar demand displaced + incremental MV→800VDC; contested by MV rectifiers |
| Power rack ASP | $400–500k/unit (~$500k/MW) | ~10× the ~$40k ASP of standard AC power-rack equipment |
| Battery rack content | ~$200k/MW | Phase 3; rectifiers gone, BBU + supercap content up |
| SST content / cost | $1.25M/MW assumed; ~$1.0–1.5M/MW build cost | Eliminates LV equip ~$0.55M/MW + Phase-2 rectifier ~$0.20M/MW |
| Total electrical content/MW | $3.6–4.8M band | White-space retrofit highest ($4.8M/MW); Phase 4 ~$4.0M/MW |
| Incremental 800VDC capacity | ~39GW by 2030 | Sidecar-served through Phases 1–2; mix inflects 2029 |
| Phase 1 content delta | +$400–500k/MW | HVDC power rack is the large majority |

**Physics (600kW rack, Kyber-class)**

| Voltage | Current | Loss ratio vs 800V |
|---|---|---|
| 54V | ~11,111A | ~219× |
| 48V | 12,500A | ~278× |
| 800V | 750A | 1× (baseline) |

Resistive loss scales with I²; raising V cuts I linearly, so loss falls quadratically. Operators do not pocket the full 219–278×; they shrink copper and bank the weight/cost/routing reduction.

**Efficiency ladder (cumulative, end-to-end)**

| Architecture | Cumulative efficiency | Mechanism |
|---|---|---|
| Baseline AC | 82.0% (7 stages) | VRM (92%) + PSU (94%) the two largest single-stage losses |
| Phase 1 | 83.7% | Power-rack rectifier (97.5%) + DC-DC (97.0%) only marginally beat old single PSU; UPS double-conversion still eats ~3pp |
| Phase 2 | 86.5% | UPS elimination cuts chain 7→5 stages |
| Phase 3 | 86.9% | MW-scale grey-space rectifier + 800VDC hall distribution (no AC skin-effect / reactive loss) |
| Phase 4 | 87.4% | SST replaces two stages with one device |

At 1GW IT load: Phase 2 ≈ 58MW continuous grid savings, Phase 3 ≈ 63MW, Phase 4 ≈ 69MW. Nvidia's ~5% claim ≈ 50MW; SemiAnalysis's Phase-4 5% delta vs baseline matches Nvidia.

**OCP power-rack lineage (the building block)**

| Spec | Voltage | Power | Key change |
|---|---|---|---|
| ORv3 HPR V3 | 50VDC sidecar | up to 300kW | Genesis of "sidecar"; PSU/BBU into dedicated power rack; busbar crosslink limited to ~6,000A |
| ORv3 HPR V4 | ±400VDC (800V) | up to 800kW (≈400kW if CBUs take half BBU slots) | 16× 50kW HVDC cables replace busbars; Meta-developed "pre-Diablo" |
| Diablo 400 (Google+Meta+Microsoft) | ±400V bipolar std / 800V monopolar option | 100kW–1MW/rack | Multi-vendor interop; ≥20ms holdup; 0.1% voltage drop @5m; standardizes 7 areas (connectivity, form factor, PSU topology, DC-DC, redundancy, safety, mgmt backplane) |
| Nvidia reference | monopolar 800V | 660kW | Air-cooled samples + production mid-2026; liquid-cooled VR Ultra late-2026; outside Diablo 400 |

**Hyperscaler 800VDC design divergence (within and beyond Diablo)**

| Operator | Power | Cables / AC input | Note |
|---|---|---|---|
| Meta | 600–800kW | 50kW HVDC cables; 8× 200A AC whips | Mt. Diablo co-author; HPR V4 originator |
| Google | up to 900kW (1.1MW roofline) | 100kW cables; 12 AC whips | Reallocates BBU/supercap space to PSUs |
| Amazon | 800kW | on ±400V | — |
| Microsoft | — | — | Co-authored spec; slower progress per SemiAnalysis |

**Standards / certification status**

| Domain | Status |
|---|---|
| NEC (US code) | Full 800VDC support targets NEC 2029 (likely partial); full maturity est. NEC 2032/2035; pre-2029 = AHJ + per-site UL |
| Arc-flash safety | IEEE 1584 excludes DC; NFPA 70E no PPE table for 600–1000VDC; UL DC Safety Research Consortium launched |
| Busway (UL 857) | Ed.14 (2025) raised ceiling to 1000VDC; Ed.15 in development targets 1500VDC |
| Grid | NERC Level 3 alert (May 2026), Computational Load Entity registration proposed; ERCOT NOGRR282 adds ride-through + PSS/E + PSCAD models |
| SST certification | No vendor has completed UL certification for datacenter SST deployment as of May 2026 |

## Key Segments

### Delta Electronics (2308 TT) — the structural winner

Delta's edge is **grid-to-chip vertical integration**: it can deliver the power shelf, BBU, PCS (incl. supercaps), and liquid cooling as one validated package. As racks scale to MW, procurement becomes engineering-led, and single-vendor delivery cuts integration/qualification burden and finger-pointing at ~600kW/rack. Power-shelf ASP jumps ~$40k (AC) → ~$400k (HVDC power rack), a 10× scope expansion. Delta has ~75% AI-server PSU share and supplies CDUs to MSFT/META/ORCL via ODMs (Foxconn, Wiwynn, Wistron). SemiAnalysis expects Delta to be the main 800VDC power-rack supplier for Nvidia, Meta, and Google at volume by end-2026, and notes that **if a dedicated Kyber 800V-50V sidecar is eliminated, Delta could dominate ~90%** of that market via in-rack PSU expertise. Bear case: minimal grey-space presence (Americas UPS share negligible); the bigger grey-space opportunity (SST) is further out.

### Vertiv (VRT) — grey-space leader pushing into white space

Vertiv **won the Meta 800V HVDC power-rack program alongside Delta**, a step-up from near-zero white-space content (historically ~$0/MW in GB200 racks — no PSU/BBU/DC-DC) toward ~$1M/MW. Crucially the retrofit is **additive, not cannibalistic**: in the Phase-1 whitespace retrofit, legacy UPS stays (~$1M/MW grey space) and the new power rack (~$1M/MW white space) stacks on top. The services business (>20% of revenue) is a structural advantage as 800VDC racks raise commissioning/maintenance/uptime complexity — wallet Delta (component/system supplier) captures less of. Limitation: no server-side white-space power electronics, so its 800VDC content is the power-rack-as-system, exposed to Delta's vertical-integration push and to hyperscaler self-design at Meta/Google. [Reconciles with [[Theses/VRT - Vertiv Holdings]] §Industry Context "800VDC architecture transition" subsection.]

### Lite-On (2301 TT) — #2 in white space

Lite-On is #2 white space, with PSU/BBU share in AWS Trainium servers (Oracle the main NVDA-server customer); SemiAnalysis models this as an at-most HSD% near-term revenue contributor even on strong Trainium 3 ramps. ON Semiconductor (Q4 FY25) confirmed rack-level BBU/PSU designs with both Delta *and* Lite-On. Lite-On has meaningful vertical integration (in-house PDUs, power controls, chassis, cabinets) supporting ~30% GM on AI-server power vs ~22–24% corporate. But it is taking a conservative ~30% 2026 capacity add vs ~50% BBU demand growth — protecting margin over share — while Delta aggressively takes its BBU share at AWS, and its CDU efforts lag (commercial shipments ~Q1 2026).

### Western integrators — Schneider, Eaton, ABB

**Schneider (SU FP)** looks structurally behind Delta/Vertiv; showed an 800VDC sidecar (up to 1.2MW/rack) at OCP 2025 aimed mostly at Oberon not Kyber; HSD organic revenue CAGR guide 2025–30 with datacenters 12–14%; remains global MV-switchgear leader (secure through the transition as upstream 11–33kV grows more complex). **Eaton (ETN)** has *zero* white-space content in GB200; its 800VDC path is grid-to-chip plus the **Resilient Power Systems acquisition** ($55M + $95M earnouts) bringing real SST IP, XLHV supercaps (144V, 62.5F, 420kW/module, 20-yr life), and a $340M Jonesville SC transformer plant (2027) — multi-year SST option value the market may underprice. **ABB (ABB SS)** calls 800VDC a *"post-2028 opportunity,"* no longer sells transformers (→ Hitachi Energy), runs SAM ~$2M/MW (below Eaton ~$2.9M, Vertiv ~$3–3.5M), and leads near-term on MV switchgear (30–35wk lead times, the binding electrical constraint, three-shift operations). FY25 was ABB's best year ($4.6B FCF, 19% EBITA margin).

### Advanced Energy (AEIS) — the orchestration layer at risk

AEIS sits between the winners and losers. Datacenter is ~30% of FY25 revenue; it supplies OCP ORv3 power shelves and is named in Diablo 400 v0.7.0 for firmware that coordinates multi-vendor power shelves (allocation, load-balancing, fault protection). The 48V→800VDC shift makes that coordination far more complex — the key swing factor. At OCP 2025 AEIS + Delta showed an HPR V4 100kW shelf (18kW HVDC-to-DC PSUs, >97.5%); AEIS expects "power shelves will be replaced" by ~Q3 2027 as HVDC goes direct to server, giving ~2 years of relevance before transitioning to HVDC-native products (Airity Technologies GaN acquisition supports this). The real risk is not obsolescence but **Delta's vertical integration** consolidating the sidecar into a single-vendor appliance with proprietary firmware; AEIS's defense is the Diablo 400 multi-vendor interface — conditionally positive only if hyperscalers keep enforcing multi-vendor procurement. AEIS does not appear among Nvidia's 800VDC ecosystem partners.

### Legrand (LR FP) — consensus-mispriced loser

Datacenters are ~26% of Legrand's FY25 revenue. Management argues only PDUs + UPS (~20% of DC segment) face 800VDC displacement; **SemiAnalysis estimates ~55% of DC revenue is exposed by Phases 3–4**, including rPDUs and busway — Legrand's highest-margin products. Phase-1 sidecars already relegate the rPDU to a downstream accessory; Phase-2 Kyber on-blade modules eliminate in-rack DC-DC. Legrand has no sidecar product, no development timeline, no partnerships/acquisitions to close the gap, and is not in Nvidia's 800VDC ecosystem. DC busway/busbar ships by end-2026 (ahead of ABB's 2027) but is a margin-compression story (lower value/MW than AC). M&A is the plausible catch-up path (Legrand entered DC via Raritan 2015, Server Technology 2017, ~30 DC acquisitions in 8 years).

### Forgent Power Solutions (FPS) — pure grey-space speed play

Forgent is a pure grey-space supplier (transformers, switchgear, PDUs, prefab enclosures), a Neos Partners roll-up (MGM Transformers, PwrQ, States Manufacturing, VanTran) that IPO'd January 2026; datacenter ~42% of revenue, skewed colo/neocloud. Its edge is **availability**: ~$3.5B spare grey-space capacity (~75% headroom vs 15–25% at majors), 8–20wk lead times vs 40+wk at Eaton/Schneider/ABB — the fastest path to power where equipment availability (not construction) is the binding constraint. But ~35% of its DC revenue (UPS eHouses, LV switchgear, ATS, LV transformers) is exposed to mature 800VDC; grey-space MV switchgear and substation transformers should persist (MV distribution upstream of DC conversion remains).

### BBU / supercapacitor layer — Panasonic (6752 JT) and Musashi (7220)

**Panasonic Energy** holds ~80% datacenter-BBU share (600M+ Li-ion cells shipped, no critical safety incident); BBU revenue scaling fast (FY25 ~upper ¥200B → FY29 target ¥800B at 20%+ ROIC, >80% of FY29 already secured via design wins), with capital-light expansion (converting underutilized EV battery lines). It is developing Capacitor Backup Units (CBUs — a proprietary supercap, form-factor-compatible with BBU shelves) that position it as a challenger to Musashi, plus high-voltage BBUs for 800V racks (NCA over LFP on density). **Musashi Seimitsu**, via Musashi Energy Solutions, holds an effective **supercapacitor monopoly** — a hybrid supercapacitor (HSC, lithium pre-doped negative electrode, higher capacitance than standard EDLC), ~¥10B HSC sales (LSD% of FY26), scaling with 800VDC from next year. Contracts signed with Flex (US) and Delta (Taiwan); Bloom Energy pairs ~3MW fuel cells with ~2MW supercaps in its "Energy Stamp," implying supercap content in grey space too. BBU module wattage rises 5.5kW → 8–12kW (Infineon: 4kW PPC cards → 12kW at up to 99.5%; Delta GTC 2026: 110kW shelves embedding 80kW BBU, 480kW per six-shelf rack).

### Phase 3 grey-space mechanics and DC protection

In Phase 3 the grey space splits. MV transformers and MV switchgear stay (the utility feed is still AC, and 11–34kV infrastructure grows more complex at gigawatt scale); LV transformers remain to feed the upstream rectifier. But the 480V AC switchgear between LV transformers and PDUs has no role once 800VDC flows through the busway, and AC floor PDUs are eliminated with it. The rule: everything above the AC-DC conversion point stays; everything below it, designed for AC distribution, goes. The AC switchboard's function — splitting one feed into multiple protected outputs — lands in one of three product categories: (i) MW-scale rectifiers with multiple outputs and integrated SSCB protection per output (the rectifier becomes its own distribution device); (ii) DC busway with breaker-equipped tap-off boxes; or (iii) prefabricated grey-space pods bundling rectifier + switchboard + busway into a factory skid for hyperscaler procurement. Early deployments favor **feeder-only busway** because at 800VDC, interrupting current under load creates a sustained arc that does not self-extinguish — DC has no zero-crossing, unlike AC which crosses zero 100–120×/sec — and DC-rated tap-offs with adequate arc interruption are still physically oversized. The protection answer is **Solid State Circuit Breakers (SSCBs)**: SiC/GaN switches that interrupt fault current in microseconds with no contact separation, so there is no arc to extinguish. Already commercialized — ABB Emax 2 (1500VDC), SACE Infinitus (solid-state 1000V/2500A, Nvidia datacenter adaptation Oct 2025), and LS Electric's UL-certified 1500V DC molded-case breaker. Why rectify at LV not MV? Rectifying from 13.8/34.5kV needs devices above 10kV, which barely exist commercially — though the gap is closing (Wolfspeed's 10kV SiC MOSFET shipped as bare die March 2026). An LV-input SST sidesteps the 3,300V-class SiC supply constraint that gates MV-input SSTs, making it the earlier-to-market variant. Grounding is among the most consequential early design choices: the Siemens/Nvidia "Protections for Data Centers Powered by Direct Current" paper lists four options (high-resistance grounding, solid grounding, floating with per-branch insulation monitoring, solid-grounded return), with no industry consensus — making the choice a vendor-ecosystem commitment, not just a technical one.

### UPS obsolescence and the layered backup hierarchy

Central low-voltage UPS is the most contested piece of infrastructure in the transition. SemiAnalysis expects centralized LV UPS to progressively lose its role and eventually become obsolete: the power rack sits directly on the 800VDC bus and houses BBU modules (seconds-to-minutes ride-through) and supercapacitors (millisecond GPU transients), both natively DC-coupled — replacing the central UPS's ride-through function without the 2–3% AC-DC-AC conversion loss. Google and Meta already took this "distributed UPS" path years ago, which also halves total battery capacity (no separate A-side and B-side UPS). But distributed UPS is operationally harder to manage, so non-vertically-integrated operators — especially colocation providers serving mixed workloads (CPU racks, storage, networking, legacy GPU racks still on AC) — are expected to keep LV UPS for redundancy at least medium-term, keeping grey-space AC intact for everything but their densest AI racks. New alternatives are emerging: **Medium-Voltage UPS** at the grid connection point (ABB HiPerGuard at 98% efficiency, deployed at Applied Digital's 400MW North Dakota campus; ON.energy's recently-patented MV double-conversion architecture), and **facility-level BESS** (MW-to-hundreds-of-MW, 1–4hr duration, increasingly shrinking or replacing the diesel generator). Generator architecture is already loosening independently of 800VDC — Meta likely bypassing generators at new sites, Microsoft using partial coverage — and 800VDC could accelerate it as supercaps, BBUs, and BESS form a distributed backup hierarchy absorbing functions generators once owned.

### SST economics, programmability, and reliability

Beyond efficiency, SSTs add capabilities a passive transformer cannot: **programmability** (active output regulation under load vs a fixed ratio), **bidirectional power flow** (grid demand response, BESS charging), and **multi-port topology** (one device aggregating utility AC + on-site generation + DC sources, routing across outputs in software) — though bidirectional + integrated BESS may trigger DER reclassification by the utility, requiring IEEE 1547/2800 compliance. **Reliability is the open question**: conventional transformers last 30–40 years passively, while no SST vendor has published field-reliability data at datacenter scale (the longest deployment is the Hitachi-ABB PETT on Swiss Federal Railways, running since 2011); SSTs concentrate heat in semiconductor junctions and require active cooling (DG Matrix liquid, Novos air). The category bifurcates by input: DG Matrix and Amperesand pursue both, starting with LV-input SST skids (3.2–4.8MW) deployable today alongside AC distribution, then MV-input as 3,300V SiC matures; Heron and Novos concentrate on MV-direct units that collapse the LV transformer + rectifier. On layout economics, the SST eliminates LV equipment (~$0.55M/MW) and the Phase-2 rectifier (~$0.20M/MW) at an estimated cost of ~$1.0–1.5M/MW — an upfront capex premium over directly-replaced equipment that the efficiency savings repay over the asset life.

### SST end-state, vendor landscape, and the four challenges

SSTs (three-stage: MV AC→DC via 3,300V+ SiC, HF isolation transformer ~20kHz shrinking the core ~90%, output 800VDC) target up to 15% system-efficiency improvement (82–85% → 97%+) and Infineon-claimed 40× weight / 14× size reduction. Best public benchmark: ETH Zurich 98% at 400kW (13.2kVAC→800VDC, INTELEC 2025); vendors converge on a ~98.5% ceiling (DG Matrix, Amperesand, Heron, Novos) but datacenters need 3–6MW units at 99%+. **DG Matrix** (ABB-backed, Infineon SiC, only SST in Nvidia's MGX reference) targets UL cert by end-Q2 2026; Amperesand targets 30MW in 2026; Heron building a 40GW US facility; Eaton acquired Resilient. >$320M flowed into SST startups in the 12 months to March 2026; ETH Zurich's caveat is that a line-frequency transformer + SiC rectifier can match SST efficiency, and no SST vendor has field-reliability data at datacenter scale. **The four adoption challenges**: (1) regulation — NEC 2029 partial, full 2032/35, pre-2029 bespoke AHJ approval; (2) cooling — largest AC load, no DC-native ecosystem (Danfoss Turbocor runs internally 700–813V, VACON NXP accepts 640–1200VDC, Delta unveiled a 2.4MW 800VDC In-Row CDU at GTC 2026, but chillers/pumps/fire/lighting stay AC, so Nvidia retains an AC auxiliary bus); (3) supply-chain standards lag codification; (4) grid interconnection moves grid-facing behavior into software-defined power electronics, raising the modeling burden and spawning AI-native EPCs (Aran Industries) for PE-stampable 800VDC packages.

## Contradiction Check

**Supports [[Theses/VRT - Vertiv Holdings]] — with a sharpened caveat.** The article corroborates the existing thesis (additive retrofit content, Meta program win, services-moat durability) and quantifies the white-space step-up (~$0 → ~$1M/MW). But it adds a genuine tension: Vertiv has **zero server-side white-space power electronics** (no PSU/BBU/DC-DC), so its 800VDC content is the power-rack-as-system — directly exposed to Delta's vertical-integration push (~75% PSU share) and to hyperscaler self-design. The "white space > grey space" framing is a mild challenge to Vertiv's grey-space heritage: it must *execute* the white-space push or cede the high-value pool. Assumption affected: VRT's "physics-limited moat" holds for liquid cooling, but the 800VDC power-rack content is more contestable than the cooling moat. Conviction-neutral, monitoring-relevant.

**Supports [[Theses/NVDA - Nvidia]] as architect, not exposure.** Confirms Nvidia's monopolar 800V 660kW reference (air-cooled mid-2026, liquid-cooled VR Ultra late-2026) sitting outside Diablo 400 — consistent with the existing "Nvidia is the cause" framing. The Kyber density-forcing logic (single rack bounds the expert layer; scale-out ~8× slower than NVLink) reinforces the demand thesis.

**Supports [[Theses/META - Meta]] as a power-architecture standards-setter.** Meta is a Mt. Diablo co-author, HPR V4 originator (600–800kW, 50kW cables, 8× 200A whips), and the *buyer* that awarded Vertiv + Delta the 800V power-rack program — consistent with the OCP-authorship framing in both the META and VRT theses.

**Indirect for [[Theses/VICR - Vicor Corporation]].** The article confirms the **50V on-board bus persists** even under 800VDC (a DC-DC power shelf steps HVDC→50V; VRMs convert 50V→sub-1V), so on-board conversion content survives — mildly supportive. But Part 1 is not VICR-centric; the on-board VPD layer is explicitly held for Part 2. No conviction change; flag Part 2 for the VICR-relevant read.

**New name the vault does not hold: Delta Electronics (2308 TT).** Named the structural winner — the cleanest 800VDC white-space pure-play per this source (10× ASP uplift, ~75% PSU share, potential ~90% of the Kyber sidecar market). Candidate for a new thesis; currently absent from the vault.

**Consensus challenges to flag:** Legrand management's 20%-at-risk claim vs SemiAnalysis's ~55%; Forgent ~35% at risk; ABB's own "post-2028" framing tempers near-term DC enthusiasm.

**Source-credibility caveat:** this is paywalled, model-promoting SemiAnalysis research; the winner/loser calls are their proprietary Industrials Model view (they claim a track record of "calling winners before anyone else"). Directionally consistent with the vault's existing [[Macro & Technology/800VDC Adoption]] note, but the phase-TAM numbers use a different denominator than the macro note's "% of new AI racks" adoption curve — worth reconciling at `/sync`.

## Source Excerpts

- "We estimate the ASP for the Power Rack to reach $400-500k per unit, roughly 10x the ~$40k ASP of standard AC power-rack equipment. On a deployed-MW basis, that lands near $500k/MW."
- "We expect sidecar TAM to peak at ~$11B in 2028 before declining as facility-level 800VDC takes share in Phase 3… By 2030, we expect SST TAM to reach ~$13B."
- "We expect total incremental capacity powered by 800VDC to reach ~39GW by 2030."
- Google (OCP EMEA 2025): "selecting 400 VDC as the nominal voltage allows us to leverage the supply chain established by electric vehicles, for greater economies of scale, more efficient manufacturing, and improved quality and scale."
- Vertiv retrofit math: "the legacy UPS stays in place (~$1M/MW grey space), and the new power rack (~$1M/MW white space) stacks on top which is a near-term tailwind."
- Delta: "Power shelf ASPs jump from roughly $40k per rack in a standard AC-DC configuration to roughly $400k for an HVDC power rack, a 10x increase driven by scope expansion."
- ABB: "Current strong orders are for existing AC power architecture; new 800-volt DC architecture with Nvidia is a post-2028 opportunity." (Expects DC 40–50% of datacenter capacity by 2030.)
- Legrand exposure: management says only PDUs + UPS (~20% of DC segment revenue) face displacement; "We think that materially understates the risk… roughly 55% of DC revenue is exposed."
- AEIS (OCP 2025): by Q3 2027 "power shelves will be replaced" as HVDC goes direct to server.
- Efficiency: baseline AC path 82.0% across seven stages; Phase 4 87.4%; "At 1GW of IT load, the Phase 2 gain translates to roughly 58MW… Phase 3… 63MW and Phase 4 to 69MW."
