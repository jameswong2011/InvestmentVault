---
date: 2026-04-29
tags: [sector, moc, semiconductors, photonics, photonic-metrology, photonic-test, AEHR, FORM, CPO]
status: draft
sector: Semiconductor Capital Equipment
---
> [!question] 2026-04-29 → Addressed 2026-04-29
> **Prompt:** *Who are AEHR/FORM's customers today, SiPh foundries like GFS and Tower Semi or integrated laser manufacturers like LITE/COHR?*
>
> **Response:** AEHR's photonics customers are integrated laser/transceiver IDMs (LITE / COHR / Cloud Light / Asian laser makers) — burn-in is a back-end step owned by whoever owns the epi process, not the SiPh foundry. FORM's optical-probe customers are foundry-anchored (TSMC / Intel / GFS-Tower / Samsung) since probe qualification is a foundry workflow. The two pure-plays therefore ride two different segments of the same photonic-volume cycle. Full analysis: §Competitive dynamics → Customer base composition.

# Photonic Metrology

> **Map of Content** — The optical wafer-test, burn-in, and metrology sub-stratum of the photonics supply chain. Optical test is the CPO yield bottleneck: characterisation requires full wavelength sweeps and repeated micron-precision alignment per die, with no instant plug-and-test equivalent to electrical probing — driving structurally rising test capex per photonic wafer at exactly the moment 1.6T module volumes scale 8x (2.5M → 20M units, 2025→2026) and CPO yields (60-75%) need to close 15-25 points to reach the >80-85% HVM threshold. **AEHR and FORM are the two public US pure-plays at this chokepoint**, trading at small/mid-cap multiples while the upstream laser/transceiver names (LITE, COHR) have already re-rated 800-900% over 24 months. This note is a sub-cluster of [[Sectors/Semiconductor Capital Equipment]] — focus is the optical-domain test stack, not broader WFE.

## Active Theses

*Scope: Photonic Test Pure-Plays (the sub-cluster's central names)*
- [[Theses/AEHR - Aehr Test Systems]] — **MEDIUM (draft, Apr 29 init).** Sole commercial wafer-level burn-in (WLBI) platform at scale for AI accelerators >600W, SiC, GaN, and silicon-photonics dies. Q3 FY26 print (Apr 22 2026): bookings $37.2M (+5x QoQ), book-to-bill >3.5x, record $50.9M effective backlog, AI processors >35% of mix vs SiC ~80%+ in FY24, March 2026 hyperscale silicon photonics design-in. FOX-XP 9x300mm parallel architecture is the photonic-burn-in chokepoint; 4-7yr competitive qualification gap is the moat.
- [[Theses/FORM - FormFactor]] — **MEDIUM (draft, Apr 29 init).** Sole US-listed pure-play probe-card vendor (~31% global share). Optical probe is a feature added on top of the dominant electrical-probe business — dual electrical+optical probe cards lift per-card ASP 30-60% vs electrical-only. CPO/optical test consolidation window 2026-2028 likely organic-or-M&A; FORM is the only credible candidate with MEMS + existing CPO customer relationships (AVGO/Marvell linkage).

*Adjacent active theses (demand drivers and parent hub):*
- [[Theses/LITE - Lumentum]] — 200G EML monopoly, 6-inch InP transition (San Jose, Caswell, Greensboro), Cloud Light SiPh modules; primary upstream demand source for AEHR burn-in (laser/EML reliability) and FORM optical probe (PIC wafer test).
- [[Theses/AIXA - Aixtron]] — InP MOCVD upstream; same investment logic (picks-and-shovels into the photonics cycle at equipment-cycle multiples vs LITE/COHR thesis-cycle multiples).
- [[Theses/IQE - IQE]] — III-V epi substrate; fellow chokepoint upstream of photonic test.
- [[Sectors/Semiconductor Capital Equipment]] — Parent hub; Insight #6 (AEHR/FORM/TSEM/GFS asymmetric photonics picks-and-shovels) is the basket-level positioning frame.
- [[Sectors/Optical Networking & Photonics]] — Sister sector covering the laser/transceiver/CPO demand side.

## Key industry questions

1. **Is optical wafer test on track to become 8-15% of photonic device cost, or stuck at 3-5%?** Conventional thinking treats test as commoditised back-end overhead. SiPh and CPO change the math — every PIC requires multi-wavelength sweep, alignment loop, thermal soak, and electrical-optical co-stimulus. iST commentary (Q1 2026): "optical test dramatically slower than electrical, hindering design turnaround." If test cost-share doubles into HVM, AEHR/FORM revenue per photonic wafer compounds independently of unit volume.

2. **Does AEHR's photonics customer base broaden beyond the current 2-3 anchors?** Historical AEHR risk is binary customer concentration — SiC burn-in revenue collapsed 2024-2025 when EV inventory corrected. Q3 FY26 (Apr 2026) added a second hyperscale optical-interconnect customer alongside the SiPh transceiver anchor. **A third or fourth photonics customer in FY27 would re-rate the durability-of-revenue narrative.**

3. **Does CPO architecture shift test value from wafer-level (AEHR/FORM) to integration-level (ficonTEC, Fabrinet)?** The optical engine for CPO is co-packaged with the switch ASIC — meaning a test failure post-bonding is far more expensive than a failure caught at the wafer step. This *should* increase AEHR/FORM TAM (wafer-step weed-out becomes mission-critical, "known-good die" becomes table stakes). But if hyperscalers accept higher integration-stage scrap, value migrates to alignment/packaging-stage test instead. **AEHR's Q3 FY26 hyperscaler order suggests the wafer-stage TAM is winning today; the question is durability through 2028.**

4. **How much of the FORM optical probe-card opportunity is captured by the existing electrical probe install base, vs. requiring a separate green-field qualification cycle?** FORM has ~20% global probe-card share, with multi-year qualified positions at every leading foundry. If optical probes can be added as an ASP-uplift to existing probe touchdowns (combining electrical and optical contact in one card), FORM captures the photonics cycle without rebuilding customer relationships. If optical requires a parallel qualification path, the ramp slips 12-24 months.

5. **Where do Teradyne and Advantest stand?** Teradyne stated photonics test "must evolve for high-volume CPO manufacturing" — implicitly conceding the current portfolio is sub-scale. Advantest's FORM partnership on wafer-level HBM is a precedent for photonic equivalents but no announced product. **Do the ATE incumbents acquire AEHR or FORM optical capability, or build organically?**

6. **Does the 6-inch InP wafer transition double the addressable wafer-level burn-in market?** Lumentum Greensboro, Coherent's 3-fab buildout, Nokia/SMART Photonics G10-AsP MOCVD installs — every 6-inch InP fab requires a fresh wafer-level test infrastructure since 3-4 inch tooling is mechanically incompatible. AEHR's FOX-XP 9x 300mm parallel architecture is over-spec'd for current 6-inch but positions for 8-inch InP if/when the industry transitions there in 2028+.

7. **How exposed is the photonic test stack to Chinese domestic substitution?** Unlike pluggable transceivers (Innolight/Eoptolink dominant) or DSPs (Marvell 80%+ share), photonic test equipment is fragmented and Western-led. Chinese entrants (HangXin, EOChip, others) sit at the chip-design layer; **no Chinese photonic test equipment vendor competes at production scale today**. This is a less-discussed asymmetry vs. pluggable-module geopolitics.

---

## Industry history

**Pre-2010 — Lab-grade optical metrology, no production-volume tooling.** Optical test was bench-top instrumentation: Agilent (later Keysight), Anritsu, Yokogawa, EXFO supplied tunable lasers, optical spectrum analysers, optical network analysers. Photonic device manufacturers (Finisar, JDSU, Avago) ran manual fiber-alignment workflows in low-volume tier-1 telecoms applications. **Wafer-level optical test did not meaningfully exist** — test was integration-stage, post-packaging.

**2010-2015 — First-wave volume scaling on 100G transceivers.** Cisco's Acacia acquisition (announced 2016) and the 100G CWDM4 standard pulled photonic devices into volume datacom for the first time. FormFactor entered probe-card territory adjacent to optical test via the **Cascade Microtech acquisition (June 2016, $355M cash + stock)** — Cascade's analytical and engineering probes had heritage in photonic device characterisation that FORM integrated into its probe-card portfolio. Aehr Test, founded 1977 as a DRAM burn-in specialist, was a near-bankrupt sub-$50M-revenue company through 2014 (DRAM burn-in commoditised, parallel test in DRAM had collapsed Aehr's TAM). **Acacia post-acquisition footnote**: Cisco's $4.5B 2021 close was progressively absorbed into Cisco's systems business and did not produce merchant SiPh leadership — coherent-DSP share migrated to Marvell (post-Inphi) and Ciena, integrated PIC/EML to LITE / COHR; Acacia is no longer a meaningfully independent merchant-market node, and is not a directly relevant photonic-test customer or competitor today (Cisco-internal tape-outs run through TSMC/GFS-tested flows, not Acacia-branded test infrastructure). The acquisition is broadly viewed as a strategic loss for Cisco — they removed a leading independent vendor from the merchant market without converting that capability into Cisco-branded SiPh leadership.

> [!question] 2026-04-29 → Addressed 2026-04-29
> **Prompt:** *Where is Acacia today in optical market, are they a relevant player in SiPh? Or has Cisco fundamentally failed with this acquisition.*
>
> **Response:** Acacia was progressively absorbed into Cisco's systems business post the $4.5B 2021 close and is no longer a meaningfully independent merchant-market node — coherent-DSP share migrated to Marvell (post-Inphi) and Ciena, integrated PIC/EML to LITE / COHR. Broadly viewed as a strategic loss for Cisco: they removed a leading independent vendor without converting that capability into Cisco-branded SiPh leadership. Not a relevant photonic-test customer or competitor today. Full footnote: §Industry history → 2010-2015 paragraph (Acacia post-acquisition footnote).

**2016-2020 — Aehr's SiC pivot; FormFactor analytical probe expansion.** Aehr repositioned FOX-XP toward SiC power devices in 2018-2019, riding the EV power-electronics boom. SiC wafer-level burn-in revenue scaled Aehr from ~$30M (FY18) to $80M+ (FY23). FormFactor's MicroProbe and Cascade integrations gave it the only public-market probe vendor with explicit optical-domain capability. Photonic devices at this stage were still sub-scale relative to logic/memory test budgets — the market was waiting for the AI-driven inflection.

**2021-2024 — Pluggable transceiver scale-up, Aehr's first photonics customer.** 400G/800G transceiver shipments scaled into hyperscale datacom. **Aehr disclosed its first major silicon photonics transceiver customer in fiscal 2024** — a multi-system FOX-XP order for wafer-level burn-in of laser/EML photonic dies. SiC revenue began correcting in 2024 on EV inventory glut, exposing Aehr to a one-leg-stool customer-concentration risk that the SiPh ramp partially offset. FormFactor's optical-probe optionality remained an emerging story rather than a meaningful revenue line.

**2025-2026 — Inflection year for photonic test.** Drivers stack: (i) 1.6T module shipments rising 2.5M → 20M units (Nomura, 8x YoY); (ii) silicon photonics share of high-end transceivers projected 50-70% in 2026 (TrendForce); (iii) NVIDIA's $4B March 2026 Coherent + Lumentum capital injection, locking in domestic 6-inch InP capacity that requires new wafer-level test infrastructure; (iv) CPO yield gap (60-75% vs >90% CMOS) explicitly identified by SemiAnalysis and ISSCC 2026 papers as the gating constraint on volume CPO; (v) iST and TSMC commentary at SEMICON Taiwan 2025-2026 elevating optical test as the "highest-risk element" of CPO mass production.

**Aehr Q3 FY2026 (April 22, 2026 earnings).** $37.2M bookings, **3.5x+ book-to-bill ratio**, $50.9M effective backlog. Disclosed one new major silicon photonics transceiver customer (different from the FY2024 anchor) and one hyperscale optical-interconnect follow-on order from March 2026. CoWoS-packaged-device burn-in interest "building" per management. Stock has not yet meaningfully repriced relative to the reported demand pivot — the equipment-cycle valuation arbitrage to LITE/COHR remains open.

---

## Competitive dynamics

### Public-market positioning

| Vendor                | Ticker | Focus                                | Photonic Test Role                                                                          | 2026 Photonic Mix Estimate                                             |
| :-------------------- | :----- | :----------------------------------- | :------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------- |
| **Aehr Test Systems** | AEHR   | Wafer-level burn-in (FOX-XP, FOX-NP) | Pure-play photonics burn-in; reliability stress test for laser/EML/SiPh dies before bonding | **Trending toward 50%+ of FY26 revenue** — pivoting from SiC dominance |
| **FormFactor**        | FORM   | Probe cards (electrical + optical)   | Optical probe cards for PIC wafer test; integrates optical with electrical probe touchdown  | <10% of total revenue today; **fastest-growing segment**               |
| **Teradyne**          | TER    | ATE (UltraFLEX, Magnum)              | Adjacent — needs to evolve portfolio for high-volume CPO test per management commentary     | Sub-scale today                                                        |
| **Advantest**         | 6857.T | ATE (V93000 EXA Scale)               | No production photonic ATE today; FORM partnership on wafer-level HBM is precedent          | Sub-scale today                                                        |
| **Keysight**          | KEYS   | Optical analysers, network test gear | High-speed (200G/400G/800G+) optical link validation; bench/system test, not wafer          | Mid-single-digit % of revenue                                          |
| **EXFO**              | EXFO   | Field/lab optical test               | Optical link testers, OTDRs; field telco-heritage rather than fab-floor                     | N/A (field tooling)                                                    |
| **Cohu**              | COHU   | Test handlers (DIAMONDX)             | Adjacency only — handler integration with optical test cells possible                       | Niche                                                                  |
> [!question] 2026-04-29 → Addressed 2026-04-29
> **Prompt:** *What is the barrier to entry for broader semi-test vendors to enter photonics testing and challenge AEHR. Separately, what is AEHR vs. FORM competitive dynamics look like on a product quality basis in the overlapping categories.*
>
> **Response:** Three structural moats keep ATE incumbents out: 12-24 month process-of-record qualification per customer, 5-10 year co-development cycle for sub-µm optical alignment, and engineering scarcity. Moats apply less to FORM (probe portfolio diluted across electrical), more to AEHR (concentrated photonic burn-in) — AEHR is the more specifically defensible pure-play. AEHR vs FORM product overlap is minimal — they execute sequentially in the same line (probe weeds out functional failures, burn-in weeds out reliability failures); only zone of overlap is the wavelength-sweep step, where AEHR differentiates on parallel-architecture throughput (9x 300mm) and FORM on MEMS + fiber-array integration. Complementary, not competitive. Full analysis: §Competitive dynamics → Barriers to entry and AEHR vs FORM product overlap.
### Private/specialist landscape

| Vendor | Status | Role | Strategic Position |
|:---|:---|:---|:---|
| **ficonTEC** | Private (Germany) | Optical alignment & assembly equipment | Tier-1 supplier to LITE/COHR/Fabrinet for fiber-attach, hex-pod active alignment, packaging-stage photonic test. **Acquisition candidate** — only Western pure-play scale at integration-stage. |
| **Photon Design** | Private | Photonic device simulation/modelling | Upstream of test (design verification), but adjacent ecosystem |
| **MPI Corporation** | Private (Taiwan) | Probe stations + optical wafer probe | Direct FORM competitor at the optical probe-station level; strong in Asia |
| **Aluksen, EOChip, others** | Private (China) | Chinese photonic test entrants | All at chip-design layer today; no production-scale Chinese photonic test equipment vendor |
| **Anritsu / Yokogawa** | Public (Japan) | Optical spectrum analysers, BERTs | Bench instruments; provide measurement standards but not fab-floor wafer test |

### Customer base composition

**AEHR's photonics customers are integrated laser/transceiver manufacturers, not the SiPh foundries.** Wafer-level burn-in for InP-based lasers and EMLs is a workflow step owned by the company that owns the epi process and ships the die — Lumentum, Coherent, II-VI legacy lines, and the Asian laser makers (Mitsubishi, Sumitomo). These IDMs run their own back-end test before shipping bare die to module assemblers. SiPh foundries (GlobalFoundries Fab 1 PIC line, Tower Semiconductor TS18 SiPh process) ship to fabless design-house customers — Marvell, Broadcom, NVIDIA, Cisco-Acacia — who specify their own test flow downstream. **Burn-in equipment is procured by the laser/EML maker, not the SiPh foundry.** AEHR's growth therefore tracks the LITE / COHR / Cloud Light / Caswell-fab capex cycle plus the hyperscaler in-house photonics build (most plausibly the identity of the March 2026 disclosed customer), rather than the GFS / Tower SiPh foundry buildout.

**FORM's optical-probe customer base is more distributed and foundry-anchored.** Probe-card qualification is a foundry-level workflow — FORM's optical probe rides on existing electrical-probe relationships at TSMC (CoWoS-PIC and SoIC), Intel (300mm SiPh), GlobalFoundries (Tower SiPh process post-Nov 2025 GFS-Tower close), and Samsung. The optical-probe ASP-uplift accrues to FORM at the foundry's wafer-acceptance step regardless of which fabless design house owns the tape-out. **GFS-Tower is structurally a more relevant FORM customer than AEHR customer** — exactly inverted from the laser-maker side of the supply chain. The two pure-plays therefore ride two different segments of the same photonic-volume cycle: AEHR rides the IDM laser capex cycle; FORM rides the SiPh foundry capex cycle.

### Pricing power and durability

The defensibility hierarchy in photonic test mirrors the broader semicap pattern: **process-of-record qualification creates 12-24 month switching barriers**, but in optical test the moat is amplified by the alignment-tolerance specificity — a customer's wafer geometry, fiducial markers, optical coupling architecture, and burn-in temperature profile become embedded in the tool. Aehr's FOX-XP wins are typically **multi-system follow-on orders rather than competitive bake-offs** — once the first FOX-XP is qualified for a SiPh wafer line, the second through fifth systems are non-competitive.

FormFactor's optical probe pricing power is more contested today because the optical probe touchdown is a feature added to its broader probe-card business — customer leverage on probe-card pricing carries over. As probe cards become **dual electrical+optical capability**, the per-card ASP rises 30-60% vs. electrical-only, providing margin uplift even where unit volume is flat.

The **incumbent ATE players (Teradyne, Advantest) have not yet entered photonic wafer test at production scale** — a notable absence given their dominance in SoC and HBM test. The likely scenario is acquisition (FORM optical or AEHR FOX-XP) rather than organic build, given the 5-10 year co-development cycle that AEHR and FORM have absorbed.

> [!question] 2026-04-29 [[pinned]] → Addressed 2026-04-29
> **Prompt:** *If AEHR's FOX-XP architecture is genuinely defensible at the photonic burn-in step, why has no incumbent ATE vendor moved to acquire? At AEHR's market cap (~$700M-1B), this should be a sub-1% revenue impact for Teradyne or Advantest. Is the structural answer (a) acquirers waiting for proven SiPh customer broadening, (b) hyperscalers preferring AEHR independent so they can dual-source, or (c) the FOX-XP architecture being less defensible than the public narrative implies?*
>
> **Response:** Net read: **(a) customer-broadening proof gating is dominant**. Pre-Q3 FY26, AEHR was a SiC-revenue-exposed company with one disclosed SiPh anchor and binary-customer-concentration risk that bled the equity in 2024-2025; acquirers prefer paying 2-3x more for visibility than timing the bottom of an in-process pivot. Q3 FY26's second SiPh customer + first hyperscale optical-interconnect order materially de-risk this; acquisition-window opens through FY27 if Q4 FY26 / Q1 FY27 sustain customer broadening. (b) is real but secondary (vendor lock cuts both ways for hyperscalers). (c) is tail-risk worth monitoring — FOX-XP physics is not exotic and a determined Teradyne organic build is technically possible if M&A is judged too expensive at peak. Full analysis: §Investor heuristics → Where consensus could be wrong → #5. Pin retained for revisit when Q4 FY26 / Q1 FY27 prints land.

### Barriers to entry and AEHR vs FORM product overlap

**Three structural moats keep ATE incumbents (Teradyne, Advantest, Cohu) out of photonic test today:**

1. **Process-of-record qualification cycles run 12-24 months per customer per platform.** Once FOX-XP is qualified for a given InP wafer line at a given customer, the alignment fixturing, fiducial markers, fiber-array geometry, and burn-in temperature profile become embedded in customer documentation. A new ATE vendor entering would face the same multi-year requalification penalty per customer — and qualification slots are themselves rationed by customer engineering bandwidth.
2. **5-10 year co-development cycle in optical wafer-handling and alignment.** AEHR has compounded sub-µm alignment know-how on FOX-XP since the SiC pivot in 2018-2019 — seven years of customer-funded R&D embedded in the platform. An ATE incumbent organic-build path absorbs the same cycle from a cold start; the math overwhelmingly favors acquisition over build.
3. **Engineering scarcity.** The pool of engineers with combined optical alignment + thermal stress test + high-volume burn-in fixturing is small and concentrated at AEHR, FORM, ficonTEC, and a handful of customer-side teams (LITE, COHR, TSMC). Hiring out of an entrenched specialist takes years and risks IP entanglement / non-compete enforcement.

These moats apply less to FORM: the optical probe is a feature added on top of the much larger electrical probe-card business, so an ATE acquirer of FORM (most plausibly Advantest given the existing HBM partnership) buys the entire probe portfolio and the photonic capability comes free as a by-product. **AEHR is the more specifically defensible photonic-test pure-play** — its moat is concentrated, not diluted across an electrical-test legacy.

**AEHR vs FORM product overlap is minimal — they sit at different test steps in the same customer flow.** AEHR's FOX-XP / FOX-NP are wafer-level burn-in tools (extended electrical and optical bias under elevated temperature, typically 85-150°C for multi-hour soak, screening laser/EML/SiPh dies for infant-mortality failure). FORM's optical probe cards are wafer-acceptance tools (sub-second functional verification at production speed: wavelength sweep, modulator response, photodetector responsivity). The two tools execute sequentially in the same customer line: probe first to weed out functional failures, burn-in to weed out reliability failures. **They are complementary, not competitive.** The only zone of overlap is at the optical wavelength-sweep step itself, where both tools execute a sweep — but for different purposes (probe = pass/fail at room temp; burn-in = stress + drift characterisation across temperature). On product quality at this overlap: AEHR's parallel-architecture throughput (9x 300mm) is the differentiator at burn-in; FORM's MEMS + fiber-array integration is the differentiator at probe. Neither substitutes for the other, and a portfolio investor in photonic test ideally owns both.

---

## Product level analysis

### Aehr — FOX-XP and FOX-NP wafer-level burn-in

**FOX-XP architecture.** Full-wafer parallel burn-in with electrical and optical co-stimulus. **9x 300mm wafer parallel test capability** — significant because the InP photonics industry is transitioning 3-4 inch → 6-inch wafers (LITE Greensboro, COHR 3-fab ramp) and FOX-XP capacity envelope is over-spec'd for current 6-inch needs while positioned for an 8-inch transition in 2028+.

**Burn-in physics specific to photonic devices.** Lasers and EMLs exhibit infant-mortality failures driven by crystal defects, facet damage, and bond-line stress at temperature. Field reliability of 10⁵+ hours requires accelerated thermal stress (typically 85-150°C, biased operation, multiple thousand hours equivalent compressed into 24-72 hour test) on every die before bonding to expensive switch ASICs or compute packages. This is **mathematically equivalent** to the SiC infant-mortality screening that drove Aehr's 2018-2023 ramp — explaining why the SiC → SiPh pivot was technically straightforward.

**FOX-NP** is the lower-throughput characterisation engineering tool, used by photonic device designers during qualification and process development. Lower revenue contribution but higher attach rate (every customer that qualifies a FOX-XP first runs FOX-NP).

**CoWoS-packaged-device burn-in.** Q3 FY26 management call disclosed "interest building" — this would extend Aehr from wafer-level into post-packaging burn-in for integrated photonic+logic packages. Underdiscussed potential TAM expansion; would require a different tool architecture.

### FormFactor — optical probe cards

**Probe card heritage.** FORM's electrical probe cards are the de facto standard at TSMC, Samsung, Intel, and the memory makers — ~20% global market share. The optical probe card is an extension architecture: traditional electrical pads on a probe card combined with **fiber array units (FAUs)** for optical I/O coupling, allowing simultaneous electrical bias and optical measurement at wafer level.

**Why optical wafer test is hard.** Per iST and TSMC commentary: (i) every die requires a wavelength sweep across the entire C-band (1530-1565nm) or O-band (1310nm) to characterise modulator response, ring resonator wavelength locking, photodetector responsivity; (ii) alignment tolerance is sub-µm (single-mode fiber core 9µm, modulator coupling tolerance often <2µm); (iii) thermal sensitivity means measurements must be repeated across 0-85°C operating range; (iv) **conventional wafer acceptance test tools indicate degradation but cannot localise loss mechanisms** — meaning a failed PIC cannot be diagnosed at wafer stage, forcing scrap rather than rework.

This bottleneck is precisely the gap FORM's optical probe + integrated tester architecture is designed to close. Whether the closure is sufficient at production speeds is the open empirical question.

**FORM-Advantest partnership.** Announced for wafer-level HBM test (electrical-only); precedent for a photonic equivalent partnership where Advantest handles the test electronics and FORM handles the probe interface. **No photonic equivalent announced as of April 2026** — a watch-item.

### Adjacent equipment — ficonTEC, Keysight, Teradyne

**ficonTEC alignment platforms.** Hex-pod active alignment systems for fiber attach and laser-to-PIC bonding. Used downstream of wafer test, at packaging stage — Fabrinet, Lumentum, Coherent are public customers. **Not directly competitive with AEHR or FORM** but captures adjacent value at the integration step.

**Keysight optical instrumentation.** Tunable laser sources, optical network analysers, high-speed bit-error-rate testers (BERTs) — these are bench-top instruments used at design qualification, not fab-floor wafer test. Keysight's photonic exposure is mid-single-digits % of revenue, growing with the 200G/400G/800G/1.6T link validation cycle.

**Teradyne and Advantest.** Both incumbents in SoC and HBM test with no current production photonic test product. Teradyne management has explicitly conceded the portfolio gap. Likely path to address: acquisition.

---

## Acquisitions and new entrants

### Historical M&A

| Year | Deal | Strategic Objective | Outcome |
|:---|:---|:---|:---|
| 2016 | FormFactor + Cascade Microtech ($355M) | Probe-card consolidation; analytical/optical capability | Created today's FORM optical probe portfolio; integrated 2017-2019 |
| 2018 | Advantest + W2BI / partnership for wafer-level test (various) | Wafer-stage test entry | Slow ramp; eventually led to FORM-Advantest HBM partnership |
| 2023 | KLA + several small inspection tuck-ins | Process control breadth | Did not enter photonic test |
| 2024-2025 | No headline photonic test M&A | — | Notable absence given the photonics ramp |

**Strategic pattern.** The photonic test sub-segment has remained **uniquely consolidation-resistant** through the 2020-2026 photonics ramp. Every other photonics-adjacent layer has seen meaningful M&A: Marvell's $3.25B acquisition of Celestial AI (Feb 2026); Cisco-Acacia (2019); Intel-eASIC (2018); GlobalFoundries-AMF (Nov 2025). The fact that Aehr (~$700M-1B market cap) and FormFactor (~$3-4B market cap) remain independent through this cycle is either a coiled-spring opportunity or a signal that the underlying technology is not as defensible as bulls believe.

### New entrants

**Chinese photonic test landscape.** All Chinese activity is at the design and chip layers; **no production-scale Chinese photonic test equipment vendor exists today**. Aluksen, EOChip, HangXin Semitech all sit at the DSP/chip-design level. This is a meaningful asymmetry vs. the broader semicap China-substitution narrative — Beijing's import-substitution program has indigenised etch, deposition, and 28nm DUV but has not yet attacked optical test. Likely 5+ years before a credible Chinese AEHR/FORM equivalent.

**Western specialist scale-up.** ficonTEC has reportedly grown 30%+ annually as photonic packaging volume scales. Private valuations in the photonics test/alignment space have risen sharply — both AEHR-type (wafer-stage burn-in) and ficonTEC-type (integration-stage alignment) targets are likely on incumbent ATE acquisition radars.

**Adjacent semicap entrants.** ASML reportedly evaluating hybrid bonding equipment (TrendForce, March 2026) — if real, signals broader semicap willingness to enter adjacencies. No equivalent ASML/AMAT/LRCX photonic test posture disclosed as of April 2026.

---

## Macro shifts

### Demand-side drivers (2026-2030)

**1.6T module volume scaling.** Nomura projects 1.6T module shipments 2.5M (2025) → **20M (2026)**. Each 1.6T module contains 4-8 photonic dies (laser + modulator + photodetector + driver), implying 80-160M photonic dies tested in 2026 alone. At even modest test cost of $5-15 per die, this is a $400M-2.4B annual photonic test market in 2026 vs. roughly $100-200M two years ago.

**SiPh penetration in 1.6T at 50-70%** (TrendForce, ISSCC 2026). SiPh test is more demanding than legacy III-V (more complex device structures, ring resonator wavelength locking required), so test cost-per-die is rising even before unit volume effects.

**CPO yield closure imperative.** Current heterogeneous integration yields 60-75% vs >90% target for HVM. Closing 15-25 yield points by 2028-2030 (the SemiAnalysis-implied schedule) requires test infrastructure that detects defects at the wafer step before integration. **AEHR FOX-XP and FORM optical probe sit precisely at this yield-closure step** — every percentage point of yield improvement at wafer-level eliminates downstream scrap of bonded packages worth hundreds of dollars apiece.

**6-inch InP wafer transition.** Lumentum Greensboro buildout, Coherent's 3-fab 6-inch ramp, Nokia and SMART Photonics G10-AsP MOCVD installs all require **fresh wafer-level test infrastructure** since legacy 3-4 inch tooling is mechanically incompatible. AEHR's 9x 300mm parallel envelope is overspecified for current 6-inch and positioned for 8-inch InP if/when the industry transitions in 2028+.

**Hyperscaler multi-vendor qualification.** Post-NVIDIA's March 2026 dual investment in Coherent + Lumentum, hyperscaler photonic supply chain security has become explicit board-level mandate. Multi-vendor qualification means duplicated test infrastructure across two or three suppliers per hyperscaler — multiplying installed-base TAM beyond the headline volume forecast.

### Supply-side shifts

**Domestic-fabrication mandate.** Lumentum's Greensboro fab and Coherent's domestic expansion are explicit CHIPS-era localisation. US-located photonic test infrastructure procurement carries Buy American provisions and political pressure favouring domestic suppliers — **structurally favours AEHR (Fremont CA) and FormFactor (Livermore CA) over Asian alternatives**.

**TSMC COUPE platform (CPO foundry).** In risk production with NVIDIA at GTC 2025; volume ramp 2026. TSMC outsourcing of optical-engine packaging is plausible if yields lag — would broaden the CPO test customer base from a TSMC-monopoly to multiple OSAT-stage test customers (ASE, Amkor, Fabrinet).

**6-inch InP MOCVD installs (AIXTRON G10-AsP).** Nokia + SMART Photonics + 3 undisclosed laser makers via Aixtron. See [[Research/2026-04-29 - AIXA VECO - MOCVD Revenue Exposure to InP Photonics Cycle - synthesis]] for upstream MOCVD detail. Each new InP fab is a new photonic test customer.

### Geopolitical

**Section 232 / MATCH Act scope creep.** January 2026 25% tariff on advanced-logic chips and April 2026 MATCH Act DUV/servicing extension target China-bound flows. **Photonic test equipment not yet explicitly named** in either, but the trajectory is restrictive. A future inclusion of photonic test in export controls would benefit AEHR/FORM by entrenching their Western customer base — analogous to ASML's EUV monopoly position post-2022 BIS restrictions.

**Gallium / indium export controls.** Chinese July 2023 export controls on gallium and germanium primarily impact upstream substrate (IQE, Freiberger) but indirectly elevate strategic premium on every Western step of the photonic value chain — including test.

---

## Investor heuristics

### Consensus framing

Sell-side coverage of AEHR is dominated by SiC narrative + photonics call-option — research notes from 2024-2025 consistently lead with SiC weakness and treat photonics as upside optionality. **The Q3 FY26 disclosure inverts this** — photonics is now the dominant revenue line, and SiC is the secondary leg. Sell-side framing has not yet caught up.

FormFactor coverage is dominated by HBM probe-card narrative (genuinely the larger near-term growth vector) with optical probe as a sub-bullet. **Optical-probe revenue is not separately disclosed**, so the consensus undervalues the photonics exposure by construction.

### What is priced in

| Name | Market Cap (Apr 2026) | Forward EV/Revenue | Photonics Discount vs LITE/COHR |
|:---|:---|:---|:---|
| Aehr Test (AEHR) | ~$700M-1B | 4-7x | LITE trades 12-15x forward EV/Revenue; AEHR equipment-cycle multiple is ~50% discount |
| FormFactor (FORM) | ~$3-4B | 2-3x | Diluted by HBM probe; optical-probe segment likely captures 5-7x EV/Revenue if separately disclosed |
| Lumentum (LITE) | ~$30B+ | 12-15x | Reference (post-NVIDIA-investment thesis-cycle multiple) |
| Coherent (COHR) | ~$50B+ | 10-13x | Reference |

**The implicit asymmetry**: a $50M incremental photonic test order is sub-1% revenue impact for LITE or COHR but 8-12% revenue uplift for AEHR. **Capacity tightness in the laser/transceiver layer pulls forward revenue at the test layer faster than the sell-side has modelled.**

### Where consensus could be wrong

1. **Customer concentration is not a 1-leg-stool risk going forward — it's a 2-3 leg stool.** Aehr's Q3 FY26 added a hyperscale optical-interconnect customer alongside the SiPh transceiver anchor and the residual SiC base. The historical "single customer collapses revenue" risk is structurally diminished as photonics customers stack.

2. **Optical test capex is rising as % of photonic device cost, not stable.** The iST commentary on optical test slowdown — "dramatically slower than electrical, hindering design turnaround and delaying production ramp" — is the canary signalling that test cost-share is climbing. If test goes from 3-5% of photonic device cost to 8-15% in HVM, AEHR/FORM revenue per wafer compounds non-linearly.

3. **The CoWoS burn-in TAM is undiscounted.** Aehr's Q3 FY26 disclosure of CoWoS-packaged-device burn-in interest opens a TAM extension into the broader advanced packaging stack — SiC, SiPh, AND CoWoS logic burn-in. Sell-side has not modelled this third leg.

4. **No production-scale Chinese substitute.** Unlike pluggable transceivers (Innolight 50%+ share) or DSPs (Marvell 80%+ share but long-term Chinese pressure), the photonic test stack has no credible Chinese vendor at production scale. The structural Western-share-loss narrative that haunts the broader semicap sector does not apply here.

5. **ATE incumbent acquisition optionality — and why no acquisition has happened yet.** Teradyne and Advantest have both stated photonic-test capability gaps; AEHR's market cap is sub-1% of either acquirer's. Sell-side does not model a take-out scenario at the 2026-2028 cycle peak. The structural reason no acquisition has happened despite the visible 2024-2025 ramp is best explained by **(a) customer-broadening proof gating** — pre-Q3 FY26 (April 2026), AEHR was a SiC-revenue-exposed company with one disclosed SiPh anchor and a binary-customer-concentration risk that bled the equity in 2024-2025; acquirers prefer paying 2-3x more for visibility than timing the bottom of an in-process pivot. The Q3 FY26 print added a second SiPh transceiver customer + the first hyperscale optical-interconnect order, materially de-risking the durability narrative. **Acquisition risk likely rises through FY27** if (i) Q4 FY26 sustains the 3.5x book-to-bill momentum and (ii) a third or fourth photonics customer is disclosed. The hyperscaler-preference-for-independence framing (b) is real but secondary — Teradyne / Advantest both have hyperscaler relationships and a captured AEHR is just as useful to hyperscalers as an independent one (vendor lock cuts both ways at qualification). The defensibility-narrative-overstatement framing (c) is the riskiest counter — the FOX-XP development cycle is real but the underlying physics (electrical+optical bias under temperature) is not exotic, and a determined Teradyne organic build is technically possible if M&A is judged too expensive at peak. **Net read: (a) dominant, (b) secondary, (c) tail risk worth monitoring** — the acquisition-window opens once Q4 FY26 / Q1 FY27 prints validate the customer-broadening trajectory.

### Non-consensus insights

**Picks-and-shovels framing inverted.** The orthodox semicap picks-and-shovels names (KLAC, AMAT, LRCX, ASML) are bid up to 30-50x forward earnings on the AI capex super-cycle. The photonics-specific picks-and-shovels (AEHR, FORM optical, AIXA, IQE) trade at 50-75% discounts to those multiples while exposed to the same demand cycle through a more leveraged, less-diluted product mix. **The photonic test sub-stratum is the most overlooked node of this asymmetry** because (i) AEHR's SiC narrative dominated the prior cycle and (ii) FORM's photonic exposure is buried inside HBM probe-card disclosure.

**Test as the CPO-yield-closure chokepoint.** Yield matters most when integration cost is highest — and CPO has the highest integration cost in the photonics value chain (post-bonding scrap of a CPO module is multi-thousand-dollar per unit). The wafer-level test step is where yield closure is mathematically most efficient. **Whoever owns wafer-level photonic test in the CPO era owns the highest-leverage yield-closure step.** AEHR FOX-XP and FORM optical probe have a 5-10 year head start on this.

**Sequencing of the trade.** The orthodoxy of the photonics trade has been laser/transceiver names first (LITE, COHR, AAOI — done), then upstream MOCVD/substrate (AIXA, IQE — in progress), then test/metrology (AEHR, FORM — not yet). **The test/metrology repricing is the next leg if (i) AEHR Q4 FY26 sustains Q3 bookings momentum and (ii) FORM separately discloses optical-probe revenue**. Both catalysts are within 6-12 months.

---

## Related Research

- [[Research/2025-11-25 - LITE - Silicon Photonics Supply Chain]] — Test layer call-out: Teradyne photonics evolution, AEHR FOX-XP wafer-level burn-in, Keysight optical analysers, ficonTEC private specialist
- [[Research/2025-11-26 - Semis - Gemini Silicon Photonics Canvas]] — SiPh supply chain depth, BESI/AEHR/FORM positioning at packaging+test layer
- [[Research/2026-03-09 - Photonics and CPO Investment Outlook]] — CPO yield gap (60-75% vs 90%+), iST optical test bottleneck quote, PhotonCap framework citing FORM as test/metrology pick
- [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]] — Aehr Test March 2026 follow-on order disclosure; SoIC/CPO packaging maturation requires wafer-level photonic test
- [[Research/2026-03-02 - Chinese Silicon Photonics Threat]] — Asymmetry: Chinese dominance in pluggables/DSPs but absence in photonic test equipment
- [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]] — CPO vendor competitive dynamics; test as gating constraint
- [[Research/2026-04-29 - AIXA VECO - MOCVD Revenue Exposure to InP Photonics Cycle - synthesis]] — Sister upstream-equipment analysis; same picks-and-shovels framing applied to MOCVD layer
- [[Sectors/Semiconductor Capital Equipment]] — Parent hub; Insight #6 (photonics picks-and-shovels) and Section 7 (Test Equipment) provide cross-sector context
- [[Sectors/Optical Networking & Photonics]] — Demand-side sister sector covering laser/transceiver/CPO market dynamics

## Legacy Callouts

<!-- Auto-managed by /archive-callouts. Addressed callouts older than the sweep threshold (default 180 days) are moved here from their original sections as plain bulleted entries: `- **<addressed-date>** · <type> · <section> · raised <fresh-date> → <body>` with a `**Response:**` sub-bullet. Sorted descending (newest first). Do NOT hand-edit. To exempt a callout from sweeping, add `[[pinned]]` to its header in-place. -->

## Log

### 2026-04-29

- Initial sector note created — focused sub-cluster of [[Sectors/Semiconductor Capital Equipment]] covering the optical wafer-test, burn-in, and metrology stratum. Parent hub had already identified AEHR/FORM as Insight #6 photonics picks-and-shovels; this note formalises the sub-sector with industry history, competitive dynamics, product analysis, and investor heuristics. No AEHR or FORM thesis notes exist yet — this MOC is the working surface; thesis promotion gated on (i) AEHR Q4 FY26 sustaining record bookings momentum and (ii) FORM disclosing optical-probe revenue mix separately.
- Two pinned questions seeded for revisit: (1) Industry questions §2 — AEHR ATE-incumbent take-out optionality and why no acquisition has happened yet at sub-1% revenue impact for Teradyne/Advantest; (2) Competitive dynamics — same line of inquiry from the moat-defensibility angle.

### 2026-04-29 (/sync — Active Theses promoted from "no active thesis" to AEHR + FORM draft theses)
- /sync run reconciled the sector note's working-surface framing against actual vault state: [[Theses/AEHR - Aehr Test Systems]] and [[Theses/FORM - FormFactor]] both created today (`/thesis` runs, conviction MEDIUM each, `status: draft`). `## Active Theses` updated to list both as Photonic Test Pure-Plays at the top, with adjacent demand-driver theses (LITE, AIXA, IQE) preserved unchanged. Original gating language ("no active AEHR or FORM thesis notes yet") removed — the gating conditions described (AEHR Q4 FY26 bookings sustainability + FORM optical-probe revenue disclosure) now describe `draft → active` promotion rather than thesis creation; both remain valid post-creation triggers and are tracked in the respective thesis Conviction Triggers / Open Questions sections. Conviction at sector level: unchanged (sector remains `status: draft`). No analytical body content modified beyond the Active Theses block.

### 2026-04-29 (Addressed user callouts)
- Addressed user callouts: 4 fresh `[!question]` callouts (3 unpinned + 1 pinned). Body integration: (1) Customer-base question (top of file) → new §Competitive dynamics → Customer base composition subsection — AEHR rides IDM laser-maker capex (LITE/COHR/Cloud Light); FORM rides foundry capex (TSMC/Intel/GFS-Tower). (2) Acacia status (§Industry history) → footnote appended to 2010-2015 paragraph — Cisco-Acacia broadly viewed as strategic loss; not relevant photonic-test node today. (3) Barriers to entry + AEHR vs FORM overlap (§Competitive dynamics) → new "Barriers to entry and AEHR vs FORM product overlap" subsection — three structural moats (PoR qualification, 5-10yr co-dev, engineering scarcity); AEHR more defensible pure-play; AEHR / FORM complementary not competitive. (4) PINNED ATE-acquisition timing (§Competitive dynamics) → expanded §Investor heuristics → Where consensus could be wrong → #5 — net read (a) customer-broadening proof gating dominant, (b) hyperscaler-independence secondary, (c) defensibility-overstatement tail risk; pin retained for revisit when Q4 FY26 / Q1 FY27 prints land. Conviction at sector level: unchanged.
