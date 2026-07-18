---
publish: true
date: 2026-06-07
tags: [macro, technology, semiconductors, packaging, substrates, glass-core, ABF, LIDE, INTC, TSM, 2802, LPKF, BESI]
status: active
sector: ABF Substrates & Advanced Packaging Supply Chain
source: vault synthesis — Intel NEPCON Jan-2026 disclosure (78×77mm glass core, 10 RDL layers, 45µm bump pitch, no SeWaRe), TSMC C.C. Wei CoPoS 2-3yr commercialisation roadmap, Samsung E-M Sejong pilot via SEMCO + Absolics Georgia plant, DNP late-2025 pilot + FY2028 mass production, LPKF AGM Jun-4 2026 + LIDE EU/Korea patents defended 2025, BESI hybrid bonding installed base; cross-referenced against [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]], [[Theses/LPKF - LPKF Laser & Electronics]], [[Theses/INTC - Intel]], [[Theses/2802 - Ajinomoto]]
---

# Organic ABF to Glass-Core Substrate Transition

*Tracker document for the multi-year architectural transition in advanced packaging substrate cores from organic (Ajinomoto Build-up Film + MGC BT resin + glass cloth) to inorganic (glass) at the leading edge of AI accelerator + Foveros + EMIB + CoPoS packaging. Multi-source synthesis intended to be updated as inflection points hit. Companion to [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] which covers the incumbent organic-ABF oligopoly in depth.*

## Thesis Delta

- **The transition is driven by warpage, interconnect density, and reticle-size physics — not cost.** At 100×100mm body size with 14-16 build-up layers, organic ABF substrates exhibit warpage >50µm across 100mm spans vs <20µm for Intel's "Thick Core" glass equivalent (Intel NEPCON Jan-2026 disclosure). Through-glass-vias (TGVs) via LIDE enable ~10× interconnect density vs mechanical drilling in organic, and glass survives reticle-size scaling (120×180mm Intel EMIB-T 2026 → 150×200mm projected Rubin Ultra 2028) that compresses organic-substrate yield geometrically. Cost is initially adverse (glass tooling + LIDE equipment + new manufacturing line cap-ex), turning favourable only when substrate body sizes exceed ~120×120mm at production yield.

- **Three customer S-curves with different timelines — Intel ahead, Samsung middle, TSMC behind — and the market alternates between conflating them and over-distinguishing them.** Intel Chandler Q1 2026 pilot HVM + India $3.3B plant 5-6yr buildout puts Intel structurally first. Samsung E-M Sejong pilot + Absolics Georgia plant target 2027 mass production. TSMC CoPoS at VisEra pilot 2026, small-volume trial 2027, mass production 2028-29 (C.C. Wei explicit "no shortcuts"). DNP early-2026 sample shipments → FY2028 mass production. Rapidus 2027+. The five Tier-1 substrate customer programs span 4-5 years of mass-production timing variance — equipment vendors (LPKF, BESI) see orders 12-24 months before mass production at each customer; substrate vendors and dielectric incumbents (Ajinomoto, Ibiden, Unimicron) lose share at the leading edge over a staged 2027-2032 window, not in a single 2028 cliff.

- **The equipment-S-curve leads the substrate-end S-curve by 12-24 months — and this offset is mispriced bilaterally.** Equipment vendors (LPKF for LIDE, BESI for hybrid bonding, AMAT/LRCX for CMP + deposition) need tool orders 12-24 months before substrate volume production at customers. Glass-substrate enablement implies LPKF tool revenue ramp 2026-2027; substrate-vendor revenue ramp 2028-29; AI accelerator revenue impact 2029-30. Sell-side models compress these three S-curves into a single timeline anchored on substrate-end mass production, which (a) makes equipment vendors look "early" in 2026-27 cash terms and (b) makes substrate-end disruption look "late" in incumbent-displacement terms. The actual sequence creates a 3-year window where equipment vendors compound while incumbent organic-ABF substrate vendors retain peak earnings.

- **For the vault, this is the macro thesis-fabric that connects [[Theses/LPKF - LPKF Laser & Electronics]] (LIDE qualification-gate duopoly), [[Theses/INTC - Intel]] (glass-substrate first-mover + Foveros/EMIB-T enabler), [[Theses/2802 - Ajinomoto]] (incumbent ABF dielectric monopolist — long-term displacement vector but durable through 2030), [[Theses/BESI - BE Semiconductor Industries]] (hybrid bonding adjacency to 3D structures on glass), [[Theses/TSM - Taiwan Semiconductor]] (CoPoS customer for glass), and [[Theses/5332 - TOTO Ltd]] (ceramic substrate adjacent alternative).** It also introduces new monitoring candidates: Corning (NYSE: GLW) glass-panel supplier, Schott AG (private), AGC (5201.T) glass-panel supplier, Absolics (SKC + Hansol Chemical JV), Samsung Electro-Mechanics (009150.KS), and DNP (7912.T).

- **Real adoption is gated by substrate-customer yield curves, qualification matrix depth, and Ajinomoto's defensive product roadmap — not by laser-process readiness.** LIDE technology has been at production-ready spec since 2023 (LPKF dozens of installed tools globally; Plan Optik smaller scale). The binding constraint is the substrate-customer side: yield ramps at Samsung E-M + Absolics + DNP + TSMC + Intel, qualification cycles 18-36 months per substrate-vendor × customer pair, and Ajinomoto's incentive to develop a glass-core-compatible ABF variant (preserving the dielectric-film monopoly while ceding the core material). Base case adoption: ~5-10% of leading-edge AI substrate volume 2027, ~25-35% by 2030, ~50-65% by 2033. Mainstream foundry/server substrate stays predominantly organic ABF through 2030+ — economics do not pencil below 80×80mm body size.

## Summary

The glass-core substrate transition is the architectural endpoint of three converging physical limits in the organic-ABF substrate stack: (a) **substrate body-size scaling** driven by AI accelerator reticle-size growth (50×50mm Skylake 2015 → 80×100mm B200/B300 2025 → 120×180mm Intel EMIB-T 2026 → 150×200mm projected Rubin Ultra 2028), where organic ABF yield drops geometrically with area at 60-70% on advanced bodies and approaching uneconomic territory above 120mm; (b) **interconnect density requirements** at AI-accelerator-class signal/power density, where 10× density via TGV becomes binding above 14-16 build-up layers and 45µm bump pitch; and (c) **warpage tolerance** at sub-20µm across 100mm spans for hybrid-bonding and ultra-flat HBM stack assembly — glass-cores demonstrate this naturally while organic ABF requires increasing process complexity to control thermal-mechanical stress. Cost is initially adverse (new manufacturing lines + LIDE equipment + glass-panel handling + qualification matrix), turning favourable only as substrate body sizes exceed organic-ABF economic crossover (~120mm) at scaled volume.

The customer ecosystem materialised through 2024-2026 and is now in pilot-to-production transition. **Intel** is structurally first: Chandler Arizona pilot reached HVM in Q1 2026 with the "10-2-10" architecture (78×77mm glass core, 10 RDL layers top and bottom), demonstrated <20µm warpage across 100mm and 45µm bump pitch in zero-microcrack ("no SeWaRe") condition; Intel's $3.3B India plant has a 5-6 year buildout. **Samsung Electronics** is mid-stack: Samsung Electro-Mechanics (SEMCO) operates the Sejong pilot line with Chemtronics + LPKF partnership disclosed May-2024, Absolics (SKC + Hansol Chemical JV) is building the Georgia plant, and 2027 mass production target. **TSMC's CoPoS** is structurally behind: VisEra pilot 2026, small-volume trial 2027, mass production 2028-29 per C.C. Wei's explicit "no shortcuts" 2026 roadmap. **DNP** (Dai Nippon Printing) has TGV glass substrates in late-2025 pilot with early-2026 sample shipments and FY2028 mass production target. **Rapidus** is the Japanese state-backed wildcard at 2027+ via the PACE consortium.

The equipment-side enablement is dominated by the **LIDE process** (Laser-Induced Deep Etching) — the femtosecond-pulse + chemistry-etch combination that creates through-glass-vias without microcracks at production yield. **LPKF + Plan Optik are the only two vendors with proven LIDE-at-scale globally**; LPKF dominates with dozens of installed tools at Tier-1 customers + 12+ year head start + LIDE core patents defended in EU (Apr-2025) and Korea (Sep-2025). A full glass-packaging line consumes a 4-tool LIDE stack (drilling + multilayer-glass bonding + glass-package singulation + CPO waveguide structuring) at ~€13M up-front equipment + €1.5-2M annual service per line — ~3× the consensus single-tool model. **BESI's hybrid bonding** is the complementary process for 3D-stacked structures on glass cores. **Corning + Schott + AGC + Nippon Electric Glass (NEG)** supply the underlying glass panels at sizes up to 550×650mm (AGC), 510×515mm (Schott), 515×515mm (Corning).

The structural alpha is not where retail attention concentrates. The widely-discussed names (Intel, TSMC, Samsung, NVIDIA via substrate consumption) are correctly priced or hyped; the *under-priced* qualification-gate plays sit at five distinct layers: (a) **LIDE equipment duopoly** (LPKF + Plan Optik) with patent moat and customer-co-qualification stickiness — equipment-S-curve leads substrate-end by 12-24 months; (b) **Glass-panel oligopoly** (Corning + Schott + AGC + NEG) with industrial-glass manufacturing barriers and qualification-history advantages; (c) **Glass substrate fabrication new entrants** (Absolics SKC/Hansol, JNTC Korea, Samsung E-M, DNP) emerging in greenfield economics outside the organic-ABF oligopoly; (d) **Hybrid bonding equipment** (BESI's D2W process) for 3D-stacked structures on glass that don't tolerate microbump-on-organic; (e) **Incumbent organic-ABF stack** (Ajinomoto + MGC + Ibiden + Unimicron + Shinko + Nan Ya + AT&S) facing slow displacement at the leading edge but retaining peak earnings through 2028-2030 due to the multi-vendor × multi-customer requalification matrix. The shared characteristic across these five categories: qualification-gate barriers (12-36 months per pair) compound *regardless* of which customer (Intel vs TSMC vs Samsung) ultimately leads on volume timing.

## Framework / Mental Model

### "Three physics constraints, not cost arbitrage"

| Conventional framing | Correct framing |
|---|---|
| Glass substrates compete with ABF on cost | Glass substrates compete on warpage, density, and reticle-size physics first; cost crossover comes later at scale |
| TSMC/Intel/Samsung all transition in 2027-28 | Intel 2026-30 / Samsung 2027-30 / TSMC 2028-31 — three staggered S-curves |
| Substrate vendors get displaced by glass | Substrate vendors retain organic-ABF revenue at trailing edge; new vendor cohort enters at glass leading edge |
| Bull case: glass substrates dominate by 2030 | Bull case: ~25-35% of leading-edge AI substrate by 2030; organic + glass co-exist for 5-10 years |
| Ajinomoto loses the franchise | Ajinomoto retains the dielectric layer on glass cores via product extension; loses ~20-40% leading-edge volume by 2032 in the displacement scenario |

### Architecture fork: organic-ABF vs glass-core substrates

| Dimension | Organic-ABF substrate (incumbent) | Glass-core substrate (challenger) |
|---|---|---|
| **Core material** | Mitsubishi Gas Chemical BT resin + glass-cloth reinforcement (~400-800µm) | Solid glass plate (AGC / Schott / Corning / NEG) at 200-1000µm |
| **Dielectric film** | Ajinomoto Build-up Film (ABF) — ~95% share at <2 microns precision | Surface dielectric still TBD — could remain Ajinomoto-compatible epoxy buildup OR shift to polyimide/alternative |
| **Through-via process** | Mechanical drilling + plasma etch + Cu plating | LIDE (femtosecond laser modify + chemistry etch + Cu plating) — 10× density at zero microcrack |
| **Body size economic limit** | ~120×120mm at acceptable yield | ~200×300mm projected; reticle-size scaling natural |
| **Layer count** | 14-16 build-up layers typical at AI accelerator class | Sub-20 RDL layers theoretical; 10-RDL demonstrated Intel Q1 2026 |
| **Warpage (per 100mm span)** | >50µm at advanced spec | <20µm demonstrated by Intel "Thick Core" |
| **Bump pitch** | ~45µm at advanced ABF | ~10µm theoretical; 45µm demonstrated Intel Q1 2026 |
| **Substrate vendor cohort** | Ibiden + Unimicron + Nan Ya + Shinko + AT&S (5-player oligopoly) | Samsung E-M + Absolics + SEMCO + DNP + JNTC + TSMC-internal (greenfield entrants) |
| **Equipment vendor** | AMAT/LRCX/KLAC (deposition + etch + inspection) | LPKF + Plan Optik (LIDE duopoly); BESI hybrid bonding; AMAT/LRCX adjacent |
| **Mass-production timing** | Mature; declining at leading edge 2028-30 | Intel 2026 HVM pilot; Samsung 2027; TSMC 2028-29; DNP FY2028 |
| **Hyperscaler/foundry posture** | Required for all advanced packaging through 2030+ | Greenfield AI-substrate enabler for highest-density packaging |

The strategic implication: hyperscalers + foundries operate **both architectures in parallel** — leading-edge AI accelerators on glass-core; trailing-edge AI accelerators + standard server CPUs + memory packages on organic ABF. Total substrate-equipment TAM expands; any single-architecture bet (e.g., "Ajinomoto is dead") is fragile through 2030.

### Historical analog: Ajinomoto Build-up Film displacing ceramic substrates (1996-2008)

The closest historical analog is the previous substrate architectural transition: **ceramic substrates (LTCC/HTCC, dominated by Kyocera + NGK + Ibiden + Shinko, 1980s-1990s) → organic ABF substrates (Ajinomoto + Ibiden Intel partnership)**. Timeline:

- **1996**: Ajinomoto invents ABF dielectric in the "Fine Chemicals" division (originally amino-acid chemistry)
- **1998-1999**: Intel co-qualifies ABF for Pentium III flip-chip BGA substrate; Pentium III ships 1999 as first volume product
- **2000-2005**: Ibiden + Shinko + Unimicron + Nan Ya PCB scale ABF substrate manufacturing capacity; ABF displaces ceramic at flip-chip class
- **2005-2008**: Ceramic substrates retreat to RF + automotive + LTCC-specialty niches; ABF reaches dominant share for high-end flip-chip BGA

**Total transition time: ~10-12 years from invention to dominant share at the leading edge.** Ceramic substrates did NOT disappear — Kyocera retains the LTCC/HTCC franchise in automotive, RF, space, defense to this day. The displacement was confined to the highest-volume flip-chip BGA segment.

**Applied to glass-core transition**: invention of LIDE (Laser-Induced Deep Etching) circa 2013-2015 → first commercial proof-points 2020-2024 → Intel pilot HVM Q1 2026 → Samsung 2027 → TSMC 2028-29 → broad leading-edge displacement 2030-2033. Total transition ~15-18 years on a slightly longer timeline than ABF because (a) glass requires whole-substrate-vendor cohort transition (not just dielectric chemistry), (b) the customer end-market scaling (AI accelerator + Foveros + CoPoS reticle-size growth) is the demand-pull that makes glass economically rational at scale rather than physics-mandatory. The ABF stack does NOT disappear — Ajinomoto + Ibiden + Unimicron retain the trailing-edge organic-ABF franchise through 2030 and likely beyond at server CPU, memory, mid-tier AI accelerator class.

### Historical analog: 48V displacing 12V in OCP racks + 12V→48V industrial transitions

The 48V over 12V transition in Open Compute racks took ~8 years from spec (~2014) to majority adoption (~2022) when Hopper-era HGX broadly shipped on 48V. The substrate architectural shift has the same gating mechanism (architectural change driven by physics at the compute layer) but moves slower because (a) substrate vendors are 5-player oligopoly with multi-year qualification cycles, vs the 48V transition where the silicon vendor (NVIDIA) had direct roadmap control; (b) the rate-limiting factor is downstream substrate-customer yield qualification, not upstream technology readiness.

### The bottleneck cascade

Five layers, each with a binding constraint that gates the next:

1. **Glass-panel supply** (Corning + Schott + AGC + NEG): industrial-glass manufacturing capacity + dimensional precision at panel sizes 500-650mm + qualification-history advantages. Binding constraint: panel-supplier capacity at advanced spec (550×650mm AGC). Beneficiary: Corning (NYSE: GLW), Schott (private), AGC (5201.T), NEG (5214.T).

2. **LIDE equipment installation** (LPKF + Plan Optik): qualification-gate duopoly with patent moat. Binding constraint: customer co-qualification capacity (each customer needs 12-24 month qualification cycle on first tool). Beneficiary: [[Theses/LPKF - LPKF Laser & Electronics]], Plan Optik (private).

3. **Glass-substrate fabrication** (Samsung E-M + Absolics + SEMCO + DNP + JNTC + TSMC-internal): qualification of new substrate vendors at customer end + yield ramp. Binding constraint: substrate-vendor yield maturity + customer multi-vendor qualification matrix (5+ vendors × 5+ customers × 18-36 months per pair). Beneficiary: SKC (011790.KS), Samsung E-M (009150.KS), DNP (7912.T), JNTC (Korean private), various Chinese glass-substrate state-backed entrants.

4. **Hybrid bonding for 3D structures on glass cores** ([[Theses/BESI - BE Semiconductor Industries]]): glass-core enables hybrid-bonded multi-die assemblies that don't tolerate microbump-on-organic at advanced HBM5+ density. Binding constraint: BESI Kinex bonder capacity + customer pull-through from 3D structures. Beneficiary: BESI, AMAT (9% BESI stake).

5. **Customer end-market scaling** (Intel + Samsung + TSMC + DNP + Rapidus → NVIDIA + AMD + AVGO + Apple): AI accelerator reticle-size + signal-density growth that makes glass economically necessary. Binding constraint: AI accelerator volume sustaining the substrate body-size growth curve. Beneficiary: [[Theses/INTC - Intel]] (first-mover at HVM), [[Theses/TSM - Taiwan Semiconductor]] (CoPoS path), [[Theses/NVDA - Nvidia]] (Rubin/Feynman generation substrates consume glass), [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]].

The cascade matters because *the layer with the slowest-moving bottleneck sets the adoption pace for the whole chain*. Today the binding layer is **substrate-customer yield qualification at Samsung E-M / Absolics / SEMCO / DNP / Intel Chandler** — the equipment is ready (LPKF), the glass panels are ready (Corning/Schott/AGC), but the substrate-vendor-level yield ramp is the choke point that determines whether 2027 mass production happens on schedule.

## Substrate body-size and architecture trajectory

| Generation (year) | AI accelerator | Body size | Layer count | Yield (mature) | Substrate generation |
|---|---|---|---|---|---|
| Skylake-EP (2015) | Intel Xeon | 50×50mm | 8-10 | 90-95% | Consumer CPU ABF |
| Sapphire Rapids (2022) | Intel Xeon | 70×70mm | 12-14 | 80-90% | Server CPU ABF |
| H100 (2022) | NVIDIA Hopper | 70×80mm | 12-14 | 75-85% | Standard AI accelerator ABF |
| B100/B200 (2024) | NVIDIA Blackwell | 80×80mm | 14-16 | 70-80% | Advanced AI accelerator ABF |
| B300 / Hopper Ultra (2025) | NVIDIA | 80×100mm | 14-16 | 65-75% | Advanced AI accelerator ABF |
| Intel EMIB-T (2026) | Intel 24-HBM-stack | 120×180mm | 16+ | 55-65% est | Intel + ABF + EMIB-T |
| Rubin (2026) | NVIDIA Rubin | 100×100mm | 14-16 | 60-70% | Advanced AI accelerator ABF |
| Intel Glass Pilot (Q1 2026) | Intel 10-2-10 | 78×77mm | 10 RDL × 2 | Pilot scale | **Glass core** |
| Samsung 2027 target | Samsung internal + 3rd party | ~100×100mm | 12-16 | Pre-HVM | **Glass core** |
| TSMC CoPoS 2027 | TSMC for hyperscaler ASICs | 100×100mm+ | 14+ | Pre-HVM | Glass core (panel-level) |
| Rubin Ultra Kyber (H2 2027) | NVIDIA NVL576 | ~120×120mm projected | 16+ | 50-60% est | Mixed ABF + Glass |
| Feynman generation (2028+) | NVIDIA | 150×200mm projected | 18+ | n/a | **Glass core dominant** |

The decisive number is **substrate-body area divided by mature-yield**: organic ABF at 120×180mm × 55-65% yield produces 35-45% scrapped material per panel — uneconomic at scale. Glass cores at 78×77mm × pilot-scale yield (Intel Q1 2026) demonstrate the warpage + density advantages but have not yet proven HVM yield economics at the 100mm+ body sizes that Rubin / Rubin Ultra / Feynman generation actually require. The 2026-2028 window is the proving period: equipment vendors compound on installation revenue; substrate-end vendors prove yield; AI accelerator customers commit volume.

## Customer adoption timeline and capex commitments

| Customer | Pilot start | First HVM target | Mass production target | Capex commitment (est) | Equipment / substrate partners |
|---|---|---|---|---|---|
| **Intel** | 2023 R&D; Chandler pilot 2024 | Q1 2026 Chandler HVM pilot ($1B+ Chandler) | 2030+ for full HVM at 18A/14A class | $3.3B India plant (5-6yr buildout); Chandler $1B+ pilot; total $5-7B 2024-2030 | LPKF + Schott (Mar-2024 BusinessKorea); Absolics Arizona pilot |
| **Samsung Electronics** | Samsung E-M Sejong pilot 2023-24 | Sejong full pilot 2026 | 2027 mass production target | $2-4B est across Samsung E-M + Absolics Georgia + SEMCO | LPKF + Chemtronics May-2024 partnership; Absolics Georgia plant |
| **TSMC CoPoS** | VisEra pilot 2026 (per C.C. Wei Mar-2026 roadmap) | Small-volume trial 2027 | 2028-29 mass production | $5-8B est across CoPoS-specific lines (within $52-56B FY26 capex) | PACE consortium qualification; likely LPKF + Plan Optik LIDE |
| **DNP (Dai Nippon Printing)** | Late-2025 pilot | Early-2026 sample shipments | FY2028 mass production | $1-2B est | Likely LPKF; PACE consortium |
| **Rapidus** | Japanese state-backed pilot 2026 | 2027 small volume | 2028+ | $5-7B Japanese state capital allocation (BLOC fund) | Likely LPKF + Tier-1 Japanese substrate partners |
| **Absolics (SKC + Hansol Chemical JV)** | Sejong 2024 + Georgia 2025 | 2027 Georgia HVM | 2028-29 mass production | $1.4B+ Georgia plant capex | SKC + Hansol Chemical; LPKF-aligned for LIDE |
| **JNTC Korea** | Vitrion-foundry partnership early-2025 | Already shipping low-volume substrates via Vitrion | 2027-28 mass production | $0.5-1B est | LPKF (Vitrion partnership) |
| **Chinese state-backed entrants** | 2025-26 pilot | 2027-28 small volume | 2030+ for domestic-China substrate | $3-5B state capital | Locked out of LPKF/Plan Optik; alternative TGV processes |

**Total committed capex through 2030: ~$18-30B across announced glass-substrate manufacturing programs.** This is roughly 3-5× the equipment-vendor TAM that LPKF + BESI + Corning + Schott + AGC capture at the highest level of the value chain. Substrate-vendor revenue ramp is back-loaded to 2028-2030; AI accelerator customer cost-savings materialize 2029-2032.

## Where the structural alpha sits

The widely-discussed glass-substrate names (Intel as customer, NVIDIA via reticle-size scaling) are correctly priced or hyped via downstream demand-pull. The under-priced opportunities concentrate in qualification-gate sub-layers:

### Equipment-side (12-24 month lead on substrate-end S-curve)

**[[Theses/LPKF - LPKF Laser & Electronics]] — LIDE qualification-gate duopoly.** ~€590M mcap; 5x EV/Rev; CEO refused capital raise at June-4-2026 AGM. The thesis: Street models tool-1 only (~€3.5-5M LIDE-A drilling); LPKF disclosed 4-tool line (drilling + bonding + singulation + CPO waveguide structuring) ~€13M + €1.5-2M annual = ~3× per-line content gap; LPKF + Plan Optik only proven LIDE-at-scale (patents defended EU Apr-2025 + Korea Sep-2025). Binary Q2-2026 LIDE production orders setup; €5.8M cash with CEO refusal-of-dilution bet. Conviction MEDIUM at draft.

**[[Theses/BESI - BE Semiconductor Industries]] — D2W hybrid bonding for 3D structures on glass.** ~67% D2W hybrid-bonding share; 150+ installed bonders at 18 customers; March 2026 SK Hynix mass-production Kinex order. Glass-core substrates enable hybrid-bonded multi-die assemblies that don't tolerate microbump-on-organic at advanced density. BESI structurally benefits from both the HBM hybrid-bonding transition (HBM5 2028-29) and the glass-core enablement of 3D structures (Foveros Direct / SoIC variants). MEDIUM conviction in current vault book.

**Corning (NYSE: GLW) — uncovered glass-panel supplier.** Specialty glass at 515×515mm panel size with EAGLE XG® formulations. Industrial-glass manufacturing barrier + customer qualification history. Not in current vault book; candidate for `/thesis GLW` after Intel HVM volume confirms substrate-end demand.

**Schott AG (private) — uncovered glass-panel supplier.** BF 33 glass substrate for laser drilling; 510×515mm panels. Privately held; no listed-equity exposure path. Industrial context only.

**AGC (5201.T) — uncovered Japanese glass-panel supplier at largest panel size.** 550×650mm panels. Largest format among glass-panel suppliers; enables panel-level packaging economics. Candidate for `/thesis 5201` if Samsung Sejong + TSMC CoPoS volume confirms panel-level packaging demand.

### Substrate-vendor side (greenfield entrants at the leading edge)

**Absolics (private JV — SKC 011790.KS + Hansol Chemical 014680.KS).** Georgia plant; Intel-aligned. Listed-equity exposure via SKC (50%+ stake in Absolics) and Hansol Chemical. Both Korean mid-caps with mixed exposure to other businesses. Candidate for /thesis SKC or Hansol after first glass-substrate revenue prints.

**Samsung Electro-Mechanics (009150.KS) — uncovered Korean substrate vendor.** Captive Samsung Galaxy AP + Exynos substrate plus external substrate business; ~3-4% global ABF substrate share + emerging glass-substrate position via SEMCO Sejong pilot. Listed mid-cap; cleaner equity exposure than Absolics. Candidate for `/thesis 009150`.

**DNP (7912.T) — uncovered Japanese printing conglomerate with glass substrate exposure.** Glass-substrate program in late-2025 pilot + early-2026 sample shipments + FY2028 mass production. DNP is a diversified ¥1.5T revenue printing + electronics + packaging conglomerate; glass substrates would be a small but high-growth segment. Listed large-cap with significant non-substrate exposure. Candidate for /thesis 7912 if glass-substrate volume materializes.

### Incumbent organic-ABF stack (slow displacement; durable through 2028-2030)

**[[Theses/2802 - Ajinomoto]] — incumbent ABF dielectric monopolist.** ~95% share; Kawasaki single-facility; trade-secret-protected chemistry IP. Per [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] §ABF monopoly durability, glass-core substrate scaling at the leading edge from 2030+ is the most credible structural-bearish path if Ajinomoto fails to develop a glass-core-compatible variant (epoxy buildup over glass). 4+ year window for Ajinomoto product extension. Monitoring conviction; long-term displacement risk priced low.

**Ibiden (4062.T, uncovered) — ABF substrate #1 (~30-35% global share).** Intel-anchor partnership 1998-present; 16-layer high-end AI substrate process. Loses Intel substrate volume gradually 2027-30 as Intel transitions to glass at top accelerator class; retains server CPU + lower-end AI substrate franchise through 2030+. Candidate for `/thesis 4062` from the "incumbent durability + displacement timing" angle.

**Unimicron (3037.TT, uncovered) — ABF substrate #2 (~22-25% global share).** TSMC CoWoS carrier-substrate primary supplier. TSMC CoPoS at 2028-29 mass production = direct Unimicron displacement risk at advanced AI substrate class. Candidate for `/thesis 3037` from the same angle.

**Mitsubishi Gas Chemical (4182.T, uncovered) — BT resin core supplier ~70-80% global share.** BT resin is the structural inner core for organic ABF; glass-core substrates entirely replace this material at the leading edge. Smaller revenue contribution than Ajinomoto but structurally similar monopoly. Candidate for `/thesis 4182` from the "second monopoly within the substrate stack" angle.

### Foundry / IDM end-customer side (timing-arbitrage)

**[[Theses/INTC - Intel]] — glass-substrate first-mover at HVM.** Chandler pilot Q1 2026 HVM + India $3.3B 5-6yr buildout. EMIB-T at 120×180mm 24-HBM-stack package at $120-180/package (Bernstein) vs CoWoS-L $900-1,000 = potential cost leadership in advanced packaging if glass + EMIB-T converges to scale. Per [[Theses/INTC - Intel]], MEDIUM conviction in current book.

**[[Theses/TSM - Taiwan Semiconductor]] — CoPoS path to glass.** VisEra pilot 2026 + small-volume trial 2027 + mass production 2028-29. TSMC retains CoWoS franchise through the transition; CoPoS is incremental rather than displacement. LOW conviction in current book due to Taiwan tail + concentration; glass-core adds optionality on TSMC's substrate vertical-integration scenario.

## Catalysts and signposts

**Near-term (next 90 days):**
- **End Q2 2026 (30-Jun-2026)**: [[Theses/LPKF - LPKF Laser & Electronics]] LIDE production orders disclosure — CEO committed at June-4 AGM. Binary near-term setup; named-customer + unit count would validate equipment-S-curve timing.
- **Samsung Q2 2026 earnings + capex update** (late July) — Sejong pilot progress + Absolics Georgia ramp commentary
- **TSMC Q2 2026 earnings** (mid-July) — any CoPoS roadmap update beyond C.C. Wei's "2-3 years away" March 2026 commentary

**Medium-term (3-12 months):**
- **Q3 2026 (October-November)**: first quarter to reflect post-AGM LIDE order pull-through; second post-Intel-HVM-pilot quarter
- **Intel Q3 2026 + Q4 2026 earnings** — Chandler pilot yield progress; any India plant timeline updates
- **DNP H1 FY2026 results** (Japan H1 ends Sep, reports Oct) — sample shipment volume disclosure
- **SEMICON West July 2026 + SEMICON Japan Dec 2026** — substrate vendor product disclosures; LPKF/Plan Optik competitive intelligence
- **Annual reports / investor days** (March-April 2027) — first full-year glass-substrate revenue disclosure at multiple substrate vendors

**Long-term (12-36 months):**
- **2027 mass production starts**: Samsung E-M target; first credible substrate-end S-curve validation
- **TSMC CoPoS small-volume trial 2027** — TSMC substrate-end demand confirmation
- **2028-29 TSMC CoPoS mass production + Samsung scaling + DNP FY2028** — peak substrate-end demand
- **Rubin Ultra Kyber substrate decisions H2 2027** — NVIDIA's decision on whether Rubin Ultra ships on organic ABF + EMIB-T or glass core directly is the key AI-accelerator timing pivot
- **2030+ Feynman generation** — projected glass-core dominance at top AI accelerator class
- **Ajinomoto glass-core-compatible dielectric variant announcement** — would preserve Ajinomoto franchise through 2030+; absence would confirm displacement vector

**Negative catalysts (downside paths for the transition):**
- TSMC explicitly defers CoPoS beyond 2030 (would push entire transition right 12-24 months)
- Intel India plant timeline slip / cancellation (would compress Intel first-mover advantage)
- Samsung 2027 mass production target slip to 2028-29 (would compress equipment-S-curve revenue)
- LPKF patent challenge in US or Japan (Plan Optik or new entrant patent litigation)
- Plan Optik wins a Tier-1 customer evaluation that LPKF was triangulated to (would split the duopoly into a contested market)
- TRUMPF (largest industrial laser company at ~€5B revenue) develops and qualifies a LIDE-equivalent process (would change duopoly to oligopoly by 2028)
- Ajinomoto announces glass-core-compatible ABF variant qualified at multiple substrate customers (would extend organic-ABF franchise through 2032-2035)
- AI accelerator demand cycle inflection (per [[Macro & Technology/AI Bubble Risk and Semiconductor Valuations]]) compresses substrate body-size growth and removes the physics-mandate for glass

## Trading and portfolio implications

**Long the equipment-S-curve, neutral the substrate-vendor cohort, gradually short the dielectric monopoly through 2030+:**

- **Long [[Theses/LPKF - LPKF Laser & Electronics]] (draft MEDIUM)** as the cleanest equipment-S-curve play — 12-24 months earlier than substrate-end revenue; qualification-gate duopoly with patent moat. Position-size for binary Q2-2026 risk; activate via `/status LPKF draft→active` after Q2 disclosure.

- **Long [[Theses/BESI - BE Semiconductor Industries]] (active MEDIUM)** as complementary equipment-side play — hybrid bonding adjacency to 3D structures on glass. Already in book; structural conviction holds.

- **Watchlist Corning (GLW) + AGC (5201.T)** as glass-panel supplier optionality. Initiate /thesis after first substrate-end mass production confirmations 2027.

- **Monitor [[Theses/INTC - Intel]] (active MEDIUM)** as glass-substrate first-mover. Chandler HVM Q1 2026 pilot + India $3.3B plant is the structural catalyst on top of existing Intel thesis.

- **Reduce/monitor [[Theses/2802 - Ajinomoto]] (monitoring MEDIUM)** as long-term displacement vector. Time horizon 2030+; current position appropriate given multi-year displacement timeline.

- **Watchlist Ibiden (4062.T) + Unimicron (3037.TT) + MGC (4182.T)** as incumbent organic-ABF stack — durable through 2028-2030 but displacement risk in 2030+ window. Initiate /thesis if cyclical downturn provides entry at <1.5x P/B.

- **Sector-level reads** via [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] (organic incumbents) + [[Sectors/Semiconductor Capital Equipment]] (equipment-side) + [[Sectors/Optical Networking & Photonics]] (CPO waveguide adjacency).

**Key portfolio question for 2026-2030**: how much capital to allocate to the equipment-S-curve (LPKF, BESI, Corning candidates) vs the substrate-vendor cohort (Samsung E-M, Absolics, DNP candidates) vs incumbent durability (Ibiden, Unimicron, Ajinomoto, MGC). The base-rate observation from the ABF-replacing-ceramic transition is that *equipment vendors captured 80%+ of the value created during the transition years*, while substrate vendors captured residual share at lower multiples, and the dielectric monopolist retained peak earnings until displacement crossed ~30% of leading-edge volume.

## Related theses + sectors

- [[Macro & Technology/CoWoS-to-CoPoS Panel-Level Packaging Transition]] — **companion macro note**; the panel-level *format* transition (round wafer → rectangular panel) that converges with this glass-core *material* transition at the 515mm panel generation (2028–29). Read together — CoPoS = carrier format, glass-core = core material.
- [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] — primary companion sector note; covers incumbent organic-ABF oligopoly in depth
- [[Sectors/Semiconductor Capital Equipment]] — covers equipment-side picks-and-shovels framework
- [[Sectors/Optical Networking & Photonics]] — CPO waveguide adjacency for LPKF 4-tool line
- [[Sectors/Display Technology & E-Paper]] — adjacent glass-processing context (LPKF Vitrion serves display + semiconductor)
- [[Theses/LPKF - LPKF Laser & Electronics]] — LIDE qualification-gate duopoly equipment play (draft MEDIUM, Jun-2026)
- [[Theses/INTC - Intel]] — glass-substrate first-mover at HVM (Chandler pilot Q1 2026)
- [[Theses/2802 - Ajinomoto]] — incumbent ABF dielectric monopolist; long-term displacement vector
- [[Theses/5332 - TOTO Ltd]] — ceramic substrate adjacent alternative material play
- [[Theses/BESI - BE Semiconductor Industries]] — hybrid bonding equipment for 3D structures on glass
- [[Theses/TSM - Taiwan Semiconductor]] — CoPoS path consumer; 2028-29 mass production
- [[Theses/NVDA - Nvidia]] — substrate consumer; Rubin Ultra / Feynman generation substrate decisions
- [[Theses/AMD - Advanced Micro Devices]] — substrate consumer
- [[Theses/AVGO - Broadcom]] — substrate consumer
- [[Theses/AMAT - Applied Materials]] — semicap equipment adjacent (CMP, deposition); 9% BESI stake
- [[Theses/LRCX - Lam Research]] — semicap equipment adjacent (etch, deposition)
- [[Mental Models/Industry - Semiconductors]] — #1 (emerging bottlenecks), #2 (qualification-gate monopolies hidden behind share data), #8 (architecture transitions remap bottleneck), #13/14 (compounder vs cyclical classification; reclassification triggers), #18 (cycle vs structural shifts)
- [[Macro & Technology/AI Bubble Risk and Semiconductor Valuations]] — AI accelerator demand cycle overlay; substrate-body-size growth gated by AI demand

## Log

### 2026-06-07
- Initial macro note created consolidating glass-core substrate transition framework from research generated during /thesis LPKF (Jun-2026). Synthesized customer-program timelines, equipment-S-curve framework, historical ABF-replacing-ceramic analog, and bottleneck cascade across 5 layers. Coverage includes Intel Chandler pilot Q1 2026 HVM, Samsung E-M Sejong + Absolics Georgia 2027 target, TSMC CoPoS 2028-29 per C.C. Wei March-2026 roadmap, DNP FY2028, Rapidus 2027+. Identified 4 new monitoring candidates (Corning, AGC, Samsung E-M, DNP) beyond existing vault coverage.

### 2026-06-18
- [[Macro & Technology/CoWoS-to-CoPoS Panel-Level Packaging Transition]] created as companion note (panel-level *format* transition vs this note's glass-core *material* transition); cross-link added to Related theses + sectors. This note's CoPoS timing (VisEra pilot 2026, 2028–29 mass production) is consistent with June-2026 reporting — no body reconciliation needed here. The stale "Q4 2030" CoPoS-delay claim lived in the OSAT + Semicap sector notes (which mis-cited this note) and was corrected in the same /sync.

### 2026-07-14 (/sync)
- [[Research/2026-07-14 - Intel Foveros Direct vs CoWoS Advanced Packaging - deep-dive]]: Corroborates the Intel-first-mover framing on advanced packaging but adds a skeptical read on external monetization — Foveros Direct is a "credible-but-evidence-light" second-source option gated by yield economics (D0<0.1 parity vs early ~0.2-0.25, 18-24mo learning window) and named-customer production, not by tooling readiness. TSMC owns the current packaging profit pool. No change to the glass-core transition timeline/framework.
