---
publish: true
date: 2026-06-07
tags: [thesis, semiconductors, packaging, glass-substrate, LPKF]
status: draft
conviction: medium
sector: ABF Substrates & Advanced Packaging Supply Chain
ticker: LPKF
fmp_symbol: LPK.DE
source: LPKF Q1 2026 earnings call + AGM 4-Jun-2026 disclosures; cross-referenced against [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]], Intel/Samsung/TSMC glass-substrate roadmaps (Intel NEPCON Jan-2026, TSMC CoPoS C.C. Wei 2026 roadmap, Samsung-Absolics Sejong pilot)
key_metrics_last_refreshed: 2026-07-12
---
> [!question] 2026-06-07 → Addressed 2026-06-07
> **Prompt:** *Provide a more detailed engineering view into LIDE technology including any competing approaches that can achieve the same objective / why LIDE is the only solution feasible.*
>
> **Response:** LIDE's structural advantage is the decoupling of femtosecond-laser modification (parallel write, no thermal damage) from selective wet-chemical etch (batch material removal); every competing approach (mechanical drilling, plasma DRIE, CO₂/UV laser ablation, femtosecond ablation, hybrid laser+etch variants) combines write + removal in a single serial process, so throughput collapses inversely with via count — fatal at the 10⁵–10⁶ TGV per panel + 30:1 aspect ratio + <1ppm microcrack spec required for AI-substrate density. Full process-physics derivation + per-approach failure-mode table in §Business Model & Product Description → LIDE process physics + Competing approaches.

> [!question] 2026-06-07 → Addressed 2026-06-07
> **Prompt:** *Provide a competitive dynamics analysis for LPKF's LIDE products against peers. What is the engineering capabilities that LPKF has over peers that allows it to maintain an advantage. Theoretically this is a small cap company with limited engineering budget that should allow other companies to be able to catch up if they have similar budget.*
>
> **Response:** Semiconductor capital-equipment moats are not built on absolute R&D spend — they are built on four compounding-against-time layers (patent timing 2014→2034, 24–36 month customer qualification cycle, empirical recipe library, strategic-fit cost for incumbents). LPKF's ~€10–15M annual R&D maintains the moat against TRUMPF (~€500M R&D) and the Japanese ABF-drill incumbents because the qualification clock has already closed in LPKF's favor and the incumbents' strategic-fit calculus does not favor entering at meaningful R&D scale until glass-substrate demonstrably scales — at which point the qualification clock has closed. The real direct threat is Plan Optik (similar small-cap structure), not the well-funded incumbents. Full moat-layer table + empirical small-cap-equipment analogues (BESI, Camtek, Onto) + Plan Optik threat assessment in §Industry Context → small-cap engineering-budget paradox.

> [!question] 2026-06-07 → Addressed 2026-06-07
> **Prompt:** *Provide a forecast on revenue, EBIT, and valuation for LPKF based on base, low and upside case adoption scenario for LIDE technology as well as optionality for CPO.*
>
> **Response:** FY2030 modelled implied share prices — low €4.80 (-81%, post-25% dilution), base €27.30 (+9%), upside €77 (+208%) — probability-weighted expected value €34 (+36% vs current ~€25) with asymmetric positive skew consistent with qualification-gate monopoly economics. CPO is the largest discretionary swing factor: €0/€5M/€30M revenue 2030 across low/base/upside (super-upside scenario €75M+ not in base 3 cases). Full revenue build + EBIT margin progression + valuation triangulation against sell-side consensus + Shawarma Capital + CPO-isolated quantification + ±€10/share sensitivity table in §Scenario Forecast.

# LPKF - LPKF Laser & Electronics

## Summary

LPKF is the dominant supplier of the laser process — Laser-Induced Deep Etching (LIDE) — that the entire next-generation advanced-packaging glass-substrate stack depends on for through-glass-vias (TGVs), and the consensus model under-counts the per-line content by ~3× because the Street still treats LPKF as a single-tool TGV drilling vendor when management has actually disclosed a four-step laser process line (drilling + multilayer bonding + singulation + CPO waveguide structuring) priced at ~€13M up-front plus €1.5–2M annual recurring per line. The market is pricing a binary near-term execution risk (€5.8M cash, CEO-promised "production orders by end Q2 2026" at June-4 AGM, activist shareholders demanding capital raise CEO refuses) into a stock that, if 2027 LIDE production ramp materialises on schedule, sits in the only proven LIDE-at-scale duopoly globally (LPKF + Plan Optik) with patent defence affirmed in EU (Apr-2025) + Korea (Sep-2025) for a glass-substrate end-market that Intel + Samsung + TSMC + DNP + Rapidus are simultaneously committing 5–10 year mass-production roadmaps to. Conviction is medium not high because the balance-sheet runway is thin (3–4 quarters at current burn absent a financing event), the timing distance between the equipment-vendor S-curve (LPKF needs tool orders 2026–2027) and the substrate-customer S-curve (TSMC 2028–29, Samsung 2027, Intel 2030) is wider than management's reassurance suggests, and the Solar segment cyclical collapse compounds the operating loss while the CEO is simultaneously refusing the dilution that would buy execution-time optionality.

## Key Non-consensus Insights

- **The Street models tool 1; tools 2/3/4 are not in any sell-side model.** Consensus analyst notes (8 analysts, average PT €15.81) treat LPKF as a single-tool TGV drilling vendor and back out €105–120M FY2026 revenue from the legacy PCB + Welding + Solar mix plus modest LIDE drilling unit sales. LPKF Q4 2025 disclosures and March 2026 product literature describe LIDE-A drilling (€3.5–5M/tool), multilayer-bonding (€2.0–3.5M), glass-singulation (€1.5–2.5M), and CPO waveguide structuring (€2.5–4M) as four distinct tool families per glass-packaging line — total ~€13M up-front equipment + €1.5–2M annual service/consumables. A 100-line global deployment by 2030 (consistent with Intel + Samsung + TSMC + DNP + Rapidus combined roadmap) is €1.3B equipment + €150–200M annual recurring at peak, vs. consensus modelling closer to €300–400M per-tool-only TAM. The 3× per-line content gap is the largest single quantitative gap in the Street model.

- **LPKF is a qualification-gate monopoly hidden behind 2-player share data.** The conventional read is "TGV laser equipment market is competitive — LPKF, 4JET, EKSPLA, TRUMPF, Philoptics combined ~87% share." That share data conflates the broader laser-drilling adjacencies (mechanical-assist + femtosecond ablation methods that produce microcrack defects unacceptable for AI-substrate density) with the LIDE chemistry-then-etch process that Intel + Samsung + TSMC have actually qualified for production glass-core substrate. Per #2 in [[Mental Models/Industry - Semiconductors|Industry mental model]] (qualification-gate monopoly hidden behind share data), LPKF + Plan Optik are the only two vendors with proven LIDE-at-scale globally, and Plan Optik is structurally smaller with no public Tier-1 customer wins. The relevant share denominator is "qualified LIDE tools at hyperscaler-substrate spec" — likely 90%+ LPKF — not "global TGV laser market" headline share.

- **The CPO laser-structuring product is a parallel, undisclosed S-curve riding 7,500× volume expansion.** CEO Klaus Fiedler disclosed at Q4 2025 earnings: "exclusive development on co-packaged optics" with a "well-known larger" US semiconductor partner under "well-funded and paid-for engagement." Triangulating against Intel's 2023 LIDE-CPO patent filings + Intel's Chandler glass-substrate pilot + Intel's Lip-Bu Tan era CPO commitment points to Intel as the most likely exclusive CPO development partner. CPO port volumes scale from ~50K units (2025) to ~380M units (2032) per consensus optics-industry projections — a 7,500× expansion. If LPKF captures 20% of CPO waveguide-structuring equipment by 2030 at €2.5–4M/tool ASP, this layer alone is materially larger than the entire current revenue base. The Street has zero coverage of this product as a distinct revenue line.

- **The cash-burn-CEO-standoff is being misread as governance dysfunction; it's a deliberate refusal-of-dilution bet.** Activist shareholders at the June-4-2026 AGM demanded a capital raise to accelerate LIDE commercialisation; CEO Fiedler refused, citing "North Star" cost-reduction and financial-independence rationale. Discharge votes passed at 99.71% (management) and 93.57% (supervisory) so the conflict is non-binding; appointment of Dr. Arne Schneider (CEO Elmos Semiconductor) to the supervisory board signals deeper semiconductor competency entering governance. Reframed: management is making an explicit bet that 2026 LIDE order flow + Welding/PCB segment cash generation can carry the company across the substrate-customer-ramp Valley of Death without dilution, preserving optionality for current shareholders. If correct, this is the right capital-allocation call; if wrong (Q2 orders slip + cash falls below ~€3M without bridge financing), it becomes a distressed-equity event. The market is pricing this as a coin flip; the asymmetric upside if management is right is several times the downside if wrong because dilution at sub-€20/share would be value-destructive vs. patient capital surviving to the 2027 ramp.

- **Two parallel S-curves operate on different timelines, and the market collapses them into one.** The substrate-side S-curve (glass-core substrate adoption at Intel + TSMC + Samsung + DNP) reaches early-production 2027 → mid-volume 2028 → mass production 2029–2030. The equipment-side S-curve (LPKF tool sales) leads the substrate-side by 12–24 months because customers must install tools before producing substrates. LPKF should see meaningful tool revenue inflection in H2 2026–2027 even if substrate-end mass production is not until 2029. The Street is modelling tool revenue contemporaneously with substrate revenue and thus pushing LPKF's inflection date 2 years too late, compressing the discounted-value of intermediate-period orders into the bear narrative. The corollary: if Q2/Q3 2026 LIDE production orders land on schedule, the multiple should rerate immediately because it validates the equipment-S-curve timing model — independent of any substrate-end shipment number.

## Outstanding Questions

- **What is the actual unit count and ASP of the LIDE production orders LPKF promised to disclose by end of Q2 2026?** Management committed at the June-4-2026 AGM to first LIDE production orders before end Q2. This is binary — either the orders materialise (and the equipment-S-curve timing model is validated, see Non-consensus #5), or they slip (and the cash-burn + activist-shareholder pressure compounds). Specific data: number of tools, customer identity (Samsung Electro-Mechanics / Absolics-Intel / DNP / JNTC / Rapidus / TSMC), unit ASP, delivery schedule.

- **What is the cash runway under realistic 2026 burn scenarios?** Cash declined from €7.0M (end Dec 2025) to €5.8M (end Q1 2026) — €1.2M Q1 burn. FY2026 EBIT guide range -€3.6M to +€5.4M (midpoint roughly breakeven) does not include LIDE-production-order-driven revenue. Solar segment is loss-making and being wound down per restructuring; PCB + Welding generate the operating cash that buffers the LIDE R&D investment. Required clarity: (a) operating cash flow split by segment, (b) Solar wind-down timeline + restructuring cost, (c) bridge-financing facility availability (credit lines, factoring, working-capital optimisation) before cash falls below ~€3M, (d) terms under which management would accept a capital raise if Q2 orders slip.

- **Is the Intel "exclusive" CPO development agreement enforceable post-Intel-strategy-reset?** CEO Fiedler's Q4 2025 "exclusive development on co-packaged optics" disclosure was made before Intel's Lip-Bu Tan strategy reset, foundry retrenchment risk, and reported India $3.3B plant 5–6 year buildout. If Intel narrows CPO investment scope, what are LPKF's rights — termination compensation, IP retention, freedom to engage other CPO customers (Broadcom + TSMC COUPE + Marvell)? Per [[Theses/INTC - Intel]] and [[Sectors/Optical Networking & Photonics|Optical Networking sector]], the CPO opportunity has multiple credible buyers; even an Intel pull-back leaves a market — but LPKF's exclusive structure could be a constraint, not an asset.

- **What is Plan Optik's actual competitive position and could they undercut on price at customer evaluation?** Plan Optik is the "much smaller German competitor" with proven LIDE-at-scale per industry sources. Plan Optik's ownership structure (private, family-controlled), capital base, and customer mix are not publicly disclosed at depth. Key risk: a financially-constrained Plan Optik underbids on a key Samsung or Intel evaluation purely on tool ASP, losing money to capture share — and LPKF discovers it on a Q3 2026 earnings call. Specific clarity needed: any publicly-known Plan Optik customer wins, their patent position relative to LPKF (Plan Optik may have orthogonal patents that survived LPKF's EU/Korea patent defence), Plan Optik's installed-base at Tier-1 substrate vendors.

- **Does the substrate-end mass-production timeline of 2028–2030 survive any macro/cycle scenario?** TSMC CoPoS at 2028–29 mass production assumes (a) AI accelerator demand sustains through cycle inflections, (b) glass-core technical issues at TSMC + Samsung + Intel + DNP resolve on schedule, (c) substrate-vendor yield curves on glass-cores reach economic crossover with organic ABF substrate. Per [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] §Competitive dynamics → ABF monopoly durability, Ajinomoto + Mitsubishi Gas Chemical + Ibiden have strong incentive to slow-walk glass-core qualification while organic ABF stack still has runway through 2030. What happens if mass production slips to 2030–31? LPKF needs ~12–24 months of equipment-S-curve lead time, so a 12-month substrate-end slip implies LPKF's equipment ramp slips ~12 months too — punishing in a thin-cash scenario.

- **Is the consensus €15.81 analyst PT (-36% downside) a credible base case or an extrapolation of FY2026 weak guidance into a permanent narrative?** 8 analysts cover the stock; ad-hoc-news, NewsCase, marketscreener, simplywall.st all flag the bearish consensus. Need to understand: which analysts have raised PTs since the June-4-2026 AGM "Q2 LIDE orders" commitment? Is the bear consensus model assuming zero CPO revenue + zero tool-2/3/4 content + 2030 substrate-mass-production slip combined — i.e., is each individual bear assumption defensible but the combined model unreasonably pessimistic? Or is each assumption reasonable individually and the combined bear case is correctly priced at €15.81?

- **What's the cross-customer concentration risk in a 4-tool line architecture?** A €13M up-front + €1.5–2M annual line implies that 5 lines = €65M one-time + €7.5–10M annual recurring. If LPKF's 2027–2030 deployment is 20 lines globally, customer concentration becomes acute — Samsung E-M alone could be 20–30% of revenue. Per #10 in [[Mental Models/Industry - Semiconductors|Industry mental model]] (anchor customer concentration is a binary survival test), what does LPKF do if Samsung discontinues their Sejong pilot, or Intel restructures CPO away from the LPKF agreement? The customer-concentration analysis at the 2027–2030 equipment-S-curve peak is the highest-value modelling exercise to complete before activating this thesis.

## Business Model & Product Description

LPKF is a 50-year-old (founded 1976) German precision laser equipment manufacturer that builds specialist laser systems for four end-market segments, with a single emerging product family (LIDE — Laser-Induced Deep Etching) representing the entire forward equity case while the legacy three segments fund the LIDE investment and stabilise group-level cash flow.

**Segment economics (FY2025 actual + Q1 2026 reported):**

| Segment | What it makes | FY2025 revenue (est) | 2026 trajectory | Strategic role |
|---|---|---|---|---|
| **Development** | LIDE-A glass-via drilling tools + multilayer bonding + glass singulation + CPO waveguide structuring + Vitrion in-house foundry service | ~€20–30M (estimated, mostly pre-production LIDE) | High-growth — Q2 2026 first production orders promised | The entire forward equity case |
| **Electronics** | ProtoLaser (PCB prototyping for R&D labs + SMT (stencil-mask laser-cutting for PCB assembly) | ~€40–50M | Stable mid-single digit growth | Cash-generative cushion that funds LIDE R&D |
| **Welding** | Laser-transmission welding equipment for plastic component assembly (automotive sensors + medical devices + consumer electronics) | ~€20–30M | Growing per Q1 2026 commentary | Cash-generative, low-cyclicality offset |
| **Solar** | Laser scribing equipment for thin-film solar module production | ~€15–25M (steep decline) | Wind-down per restructuring; near-zero by 2027 | Loss-making; restructuring driving operating margin recovery |
| **Group** | | ~€115–125M FY2025 | €105–120M FY2026 guide (excludes LIDE production volumes) | |

**LIDE technology architecture — what makes it a qualification-gate monopoly:**

LIDE (Laser-Induced Deep Etching) is a two-step process: a femtosecond pulsed laser modifies the glass structure along a precise vertical path (creating a "modification track"), then a chemistry etch selectively removes the modified glass, producing through-glass-vias with (a) zero microcracking at the via wall, (b) sub-µm dimensional precision, (c) high aspect ratios (depth/diameter up to 30:1), (d) tens-of-thousands-of-vias per panel production rate. The competing mechanical-drill, plasma-etch, and femtosecond-ablation methods all produce some combination of microcracks, dimensional drift, lower aspect ratio, or sub-economic throughput. AI accelerator glass-core substrates require ~10× the interconnect density of organic ABF substrates per Intel NEPCON Jan-2026 disclosure — that density is fundamentally not achievable at production yield without LIDE-class via quality.

**LIDE process physics — two-step decoupling is the structural advantage.**

*Step 1 — femtosecond laser modification.* A ~1030nm (or frequency-doubled 515nm) ultrashort-pulse laser, pulse duration ~300fs–1ps, repetition rate in the kHz–MHz range, pulse energy in the µJ range, is focused inside the glass volume at the desired via path. The pulse is too short for thermal diffusion to occur during energy deposition (heat-affected zone <1µm), and nonlinear multiphoton absorption concentrates energy at the focal volume — so glass that is transparent to the laser wavelength absorbs energy only at the precise focal point. The deposited energy creates structural defects (densification, refractive-index change, point defects) along a vertical column without removing material. A single laser shot writes a complete vertical "modification track" through the glass thickness; the beam is then scanned across the panel to write all vias in parallel rows.

*Step 2 — selective wet-chemical etch.* The panel is immersed in a fluoride-based etch bath (HF or KOH chemistry, typical concentration 5–25%, temperature 20–60°C). The modified glass etches 10–1000× faster than unmodified glass, producing through-vias with sub-µm sidewall roughness, zero microcracking, and aspect ratios up to 30:1. The entire panel etches in batch — throughput is independent of via count.

The decoupling of laser-write from material-removal is the structural advantage: the laser need only address the via centers (parallel scan), and chemistry removes material uniformly across the panel. Every competing approach combines write + removal in a single serial process, so throughput scales inversely with via count — fatal economics at AI-substrate density.

**Competing approaches and why none replace LIDE at AI-substrate density.**

| Approach | Process | Failure mode at AI-substrate spec | Status |
|---|---|---|---|
| **Mechanical drilling** | CNC-controlled drill bit | Cannot achieve <100µm diameter; mechanical stress causes microcracks; aspect ratios <10:1 | Used at organic-ABF density; fundamentally incompatible with glass-substrate via density |
| **Plasma etch (DRIE / Bosch process)** | Alternating SF₆/C₄F₈ plasma cycles | Hours per substrate; requires mask + photolithography; chemistry attacks glass non-uniformly; sub-30:1 aspect ratios in glass | Used in MEMS at low throughput; not viable at substrate volume |
| **CO₂ laser drilling (~10.6µm)** | Long-wavelength CO₂ laser ablation | Long wavelength is strongly absorbed; thermal damage at via wall (microcracking); serial throughput | Used in organic-ABF UV/CO₂ drill; fails glass-substrate microcrack spec |
| **UV laser ablation (~355nm)** | Direct material removal via UV nanosecond pulses | High defect rate (5–20% microcrack at AI density); residual thermal damage; serial throughput | Sub-economic yield at production volume |
| **Femtosecond laser ablation (no etch step)** | Direct material removal via femtosecond pulses | Sidewall redeposition of ablated material; serial throughput proportional to via count; aspect ratio <20:1 | Pilot work only; fails throughput economics |
| **Hybrid laser + etch (4JET, EKSPLA, Philoptics variants)** | Modification + etch with different laser/chemistry parameters | Process-quality competitive at pilot scale; no public Tier-1 production qualification | Competes in broader laser-drilling adjacency; not at LIDE chemistry-etch quality + scale |

The throughput-and-quality combination at AI-substrate density (10⁵–10⁶ TGVs per 600×600mm panel, <10µm via diameter, 30:1 aspect ratio, <1ppm microcrack defect rate, <30 min/panel for economic production) is achievable only by the chemistry-decoupled LIDE process. This is not a tunable engineering parameter — it is a process-physics constraint emerging from the inability to combine high serial-write speed, high throughput, and zero thermal damage in a single-step process. The corollary: a competitor cannot displace LIDE by spending more R&D on better lasers or better chemistry alone; they must invent a second-step decoupling of comparable yield characteristics, which is what the LPKF patent estate covers.

The four LIDE product families per the disclosed roadmap:

| Tool family | Process step | ASP (per Shawarma Capital analysis) | Strategic position |
|---|---|---|---|
| **LIDE-A drilling (M5000 Gen2, S5000 Gen2 series)** | Through-glass-vias for substrate-core interconnect | €3.5–5M per tool | The original product; patents defended EU Apr-2025 + Korea Sep-2025 |
| **Multilayer-glass bonding** | Bonds 2-N glass plates for thick-core substrate stack-ups | €2.0–3.5M per tool | Required for 400–800µm glass cores; second-generation product |
| **Glass-package singulation** | Cuts finished glass-substrate panels into individual packages | €1.5–2.5M per tool | Required for panel-to-package separation; second-generation product |
| **CPO waveguide structuring** | Creates optical waveguide structures in glass for co-packaged optics integration | €2.5–4M per tool | Orthogonal S-curve; tied to Intel exclusive development agreement |
| **Total line** | Full 4-step glass-packaging production line | ~€13M up-front + €1.5–2M/yr service | The new economic unit per customer |

**The Vitrion foundry strategy.** LPKF launched Vitrion (in-house glass-microprocessing foundry brand) as a parallel go-to-market that lets customers buy finished LIDE-processed glass parts rather than buy and operate LIDE tools themselves. This serves three purposes: (a) accelerates qualification by lowering customer up-front capex commitment (€100k–€1M part orders rather than €13M tool orders), (b) generates margin on consumables + service in addition to equipment, (c) preserves LPKF's process know-how when customers eventually move to in-house tool operation. The Vitrion business is currently sub-scale (<€10M revenue) but provides the customer-onboarding mechanism for tool purchases 12–24 months later.

**Capital structure.** ~22.55M shares outstanding (per company-disclosed end-2025 figure; some sources report ~24.5M reflecting authorisation; cross-check at next reporting). Net cash position (€5.8M cash, ~€5M debt per Q1 2026 disclosure) but cash buffer is thin — operating burn rate of ~€1.2M/quarter at current trajectory implies 4–5 quarters runway before bridge financing required, conditional on PCB + Welding cash generation continuing. Insider stock purchase by CEO and management around the AGM signals internal confidence but represents minor capital relative to dilution risk.

## Industry Context

LPKF sits at a triple intersection: (a) the advanced-packaging substrate transition from organic ABF to glass-core, (b) the co-packaged optics (CPO) buildout for next-generation networking, and (c) the broader semiconductor capital-equipment cycle. The competitive position is dramatically different at each intersection.

**Glass-substrate advanced packaging — LPKF is one of the picks-and-shovels duopoly.**

Per [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] §Competitive dynamics and the substrate-vendor competitive matrix, the substrate manufacturing layer is a 5-player oligopoly (Ibiden + Unimicron + Nan Ya + Shinko + AT&S) on organic ABF substrates with Ajinomoto monopolising the dielectric film. Glass-core substrates open a parallel architecture, with these customer/supplier pairs in active qualification:

| Substrate customer | Glass-core program | Mass-production target | LPKF qualification status (triangulated) |
|---|---|---|---|
| **Intel** | Chandler pilot line (Q1 2026 announced HVM); India $3.3B plant 5–6 year buildout; 3DGS architecture | 2030+ for full HVM; pilot from 2026 | Intel + Schott + LPKF reported via Mar-2024 BusinessKorea; LIDE patents cited in Intel CPO filings (2023) |
| **Samsung Electronics + Samsung Electro-Mechanics + SEMCO + SKC Absolics JV** | Sejong pilot via SEMCO; Absolics Georgia plant; mass-production 2027 target | 2027 mass production | Confirmed: Samsung E-M Sejong pilot disclosed LPKF + Chemtronics partnership May 2024 |
| **TSMC** | CoPoS panel-level packaging; VisEra pilot 2026; small-volume trial 2027; mass production 2028–29 | 2028–29 mass production | Likely qualified via PACE consortium; not publicly confirmed |
| **DNP (Dai Nippon Printing)** | TGV glass substrate program; late-2025 pilot line, early-2026 sample shipments | FY2028 mass production | Likely qualified via PACE consortium |
| **Rapidus** | Japanese state-backed advanced-packaging program | 2027+ | Likely qualified via PACE consortium |
| **Absolics (SKC + Hansol Chemical)** | Georgia plant; Intel-aligned | 2027–28 | Strong indication: Intel/Absolics Arizona pilot named in Shawarma Capital triangulation |

Of the visible Tier-1 glass-substrate programs, none has publicly named a non-LIDE TGV process for mass production. The two companies with proven LIDE-at-scale are LPKF (multi-decade head start, dozens of installed tools globally) and Plan Optik (smaller German, less customer disclosure). The competitive dynamic is a duopoly with sharply asymmetric scale — LPKF is the default qualified vendor for new entrants.

**The broader TGV laser equipment market shares (LPKF, 4JET, EKSPLA, TRUMPF, Philoptics = 87.21% of the global market in 2024 per Valuates report)** include broader laser-drilling adjacencies that are not LIDE-quality at hyperscaler-substrate spec. The relevant share denominator for the AI-substrate end-market is "LIDE-qualified tools at Intel + Samsung + TSMC + DNP," which is dominantly LPKF.

**The small-cap engineering-budget paradox — why LPKF holds the moat despite €10–15M annual R&D.**

The first-principles objection is sharp: LPKF spends ~€10–15M/year on R&D against TRUMPF (~€5B revenue, ~€500M R&D), Mitsubishi Electric Industrial Automation, Hitachi Via Mechanics, and Disco — each with engineering budgets 30–50× larger. A market-cap-€590M small-cap should not be able to maintain a moat against this competitive set on raw engineering capacity. The reason it can is that semiconductor capital-equipment moats are not built on absolute R&D spend; they are built on the four layers below, each of which compounds against time rather than capital:

| Moat layer | LPKF advantage | Why a well-funded competitor cannot quickly close it |
|---|---|---|
| **Patent estate + timing** | Core LIDE patents filed from 2014 (Schott collaboration); defended in EU Apr-2025 and Korea Sep-2025 against invalidation challenges; covers two-step modification-then-etch process across multiple laser-parameter + etch-chemistry combinations | Inventing around requires either a different process physics with non-equivalent quality (so far none has been demonstrated at production yield) or license negotiation with LPKF. The patent clock runs in LPKF's favor through ~2034 |
| **Customer qualification cycle** | Qualification at Samsung Electro-Mechanics ongoing since ~2022; Intel + Vitrion engagements since ~2023; pending qualifications at TSMC, DNP, Absolics, Rapidus | Substrate qualification is 24–36 months end-to-end (electrical test, reliability, thermal cycling, fab MES integration, operator training). A competitor entering qualification in 2026 reaches production qualification in 2028–29 — exactly when LPKF's tool revenue inflection materialises. The qualification clock favors the incumbent regardless of engineering budget |
| **Process recipe library** | Thousands of customer/glass/via-spec recipe variations accumulated across pilot programs (laser power, pulse rep rate, scan speed, beam shape, etch concentration, etch temperature, etch time) | Recipe tuning is empirical not derivable — it is institutional know-how that doesn't transfer with hire-poaching. A well-capitalised competitor must run the same empirical-tuning loop against the same customer panels to reach equivalent yield |
| **Strategic-fit cost for incumbents** | TRUMPF's core business is sheet-metal laser cutting (~€2B), automotive welding (~€500M), and EUV pulse-laser modules for ASML (~€500M–1B). Japanese laser-drill incumbents (Mitsubishi, Hitachi Via Mechanics, Disco) dominate organic-ABF UV-laser drilling | Entering substrate-glass equipment requires a parallel R&D track + customer relationship build + qualification time at a sub-€500M near-term TAM. For TRUMPF, the ROI is low vs. growing the EUV business with ASML. For Japanese ABF drillers, entering glass would risk cannibalising their organic-ABF installed base. None has publicly disclosed a LIDE-equivalent R&D program — strategic incentive is to wait until glass actually scales |

**Empirical analogues.** The structure replicates in [[Theses/BESI - BE Semiconductor Industries]] (advanced packaging, ~€700M revenue, ~70% hybrid-bonding share against competitors 10× larger), Camtek (substrate inspection, ~€450M revenue, dominant share against ASML/Applied Materials adjacencies), and Onto Innovation (substrate metrology, similar profile). All are small-cap equipment vendors that have maintained dominant share in narrow process niches against much larger competitors precisely because (a) the customer-specific qualification cycle protects the incumbent, and (b) the larger competitor's strategic-fit calculus does not favor entering at meaningful R&D scale until the niche is demonstrably worth it — at which point the qualification clock has already closed. Per Mental Models #2 (qualification-gate monopoly hidden behind share data) and #10 (anchor customer concentration is binary survival test), this is the canonical small-cap-equipment moat structure in semiconductors.

**The real direct threat is not TRUMPF — it is Plan Optik.** Plan Optik is a private German competitor with proven LIDE-at-scale per industry sources. R&D budget, patent estate, and customer-engagement history are not publicly disclosed at depth. Two scenarios bracket the threat: (a) Plan Optik has lost the qualification race at Tier-1 customers and is selling to second-tier customers — i.e., LPKF is operationally winning the duopoly; or (b) Plan Optik has won customer engagements not yet publicly disclosed because the customers have not announced production plans — i.e., a market share split is coming. The Q2 2026 LIDE production order disclosure materially updates the prior on which scenario is closer to truth; see Outstanding Question #4 for the open intelligence task.

**Pricing power trajectory.** The 4-tool line economics (€13M + €1.5–2M/year) plus the duopoly structure plus the patent moat (defended EU + Korea 2025) plus the multi-year customer co-qualification cycle implies pricing power should expand sharply through 2026–2028 as the first 5–10 customer lines lock in. The base risk to pricing power is Plan Optik undercutting on tool ASP to capture share at a key customer evaluation — but this is bounded by Plan Optik's smaller capital base and inability to support the global service network.

**Value chain position.** LPKF is in the second-derivative of the glass-substrate supply chain: substrate-customer (Intel/TSMC/Samsung/etc.) → substrate-vendor (Samsung E-M / Absolics / SEMCO / DNP / TSMC-internal) → LPKF equipment + Vitrion foundry → glass-panel-supplier (AGC, Schott, Corning). LPKF captures a thin slice of the substrate-vendor BOM (equipment depreciation + consumables) but the slice has dramatically more pricing power than the underlying glass-panel or labour costs.

**Co-packaged optics — adjacent S-curve with separate competitive dynamics.**

Per [[Sectors/Optical Networking & Photonics|Optical Networking sector]] and the CPO scale-up research, the CPO transition for hyperscaler networking is driven by NVIDIA NVL576 + Broadcom CPO + Marvell + Intel networking initiatives. LPKF's CPO waveguide-structuring product is an orthogonal tool category — it does not compete with photonic-integrated-circuit (PIC) fabricators ([[Theses/LITE - Lumentum]], [[Theses/AIXA - Aixtron]] MOCVD, [[Theses/AAOI - Applied Optoelectronics]]) — it competes with whatever process forms the waveguide structure that connects PIC to substrate. Currently this is dominated by polymer waveguides + advanced lithography; LPKF is positioning LIDE-modified glass as a higher-performance alternative.

**Competitive dynamics — the CPO product alone is binary**. If Intel + Broadcom + Marvell adopt LIDE-CPO at the production stage, LPKF captures a meaningful share of the 7,500× volume scale-up by 2032. If they retain polymer waveguide approaches, the CPO product never reaches scale despite the disclosed exclusive Intel development.

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | ~€426M (~$680M) | At €24.80/share × ~22.55M shares (Morningstar 16-May-2026). Stock has risen >100% YTD on glass-substrate narrative; sat at €10 in late 2025 |
| EV/Revenue | ~5x FY2026E | EV ~€590M (~€5M net cash) / €110M revenue midpoint of guide. Compares to industrial-laser peers (Han's 1.4x, IPG 2.1x) and semicap peers (Onto 6.8x, Camtek 8.4x, Disco 7.2x, Lasertec 14.5x); LPKF priced between industrial laser and semicap |
| Revenue Growth | -6.2% Q1 2026 YoY (€17.1M vs €25.3M); FY2026 guide -3% to -9% (€105–120M vs €115–125M FY2025) | Decline driven by Solar wind-down; LIDE production orders NOT included in guide — upside optionality |
| Gross Margin | ~19% (estimated; LPKF does not disclose at segment level explicitly) | Industrial laser equipment typical range; should expand as LIDE mix grows (higher margin) and Solar mix shrinks (lower margin) |
| FCF Yield | Negative (-€4 to -€8M FCF estimated FY2026) | Cash burning; €1.2M/quarter Q1 burn rate; €5.8M cash at end Q1 = 4–5 quarter runway absent bridge financing |
| Order intake (Q1 2026) | €24.1M (+17% YoY) | Book-to-bill 1.4 — leading indicator that revenue inflection is approaching |
| Cash | €5.8M end Q1 2026 (down from €7.0M end 2025) | Thin buffer; CEO refusing capital raise; Welding + PCB cash flow must offset Development + Solar losses |
| Net debt | ~€0 (slightly negative net cash position) | Technically net cash but only €0.5–1M net positive |
| Short interest | Voleon Capital 2.13%; Marshall Wace also registered short | Concentrated short setup creates squeeze risk on positive Q2 LIDE news |
| Analyst consensus PT | €15.81 (avg of 8 analysts) | -36% implied downside vs current ~€24.80; bear consensus model assumes either Q2 order slip or 2030 substrate slip or both |

## Scenario Forecast

Three-scenario forecast of revenue, EBIT, and valuation at FY2027 (year of expected revenue inflection) and FY2030 (peak deployment year). Base case is the modal trajectory if the equipment-S-curve materialises on schedule with measured customer ramp; upside captures full LIDE + CPO inflection compounding; low captures Q2 2026 order slip + substrate-end delay + Plan Optik share loss + forced capital raise. Common assumptions across cases: Solar wound down to ~€0 by FY2027, Welding stable at ~€25M, PCB (Electronics) stable at ~€45M, ~22.55M shares outstanding pre-dilution.

**Scenario assumptions in plain language.**

| Driver | Low | Base | Upside |
|---|---|---|---|
| Q2 2026 LIDE production orders | Slip past 30-Sep-2026 | Materialise on schedule — 4–5 tools across 2 customers | Materialise + exceed — 8–10 tools across 3–4 customers |
| 2030 customer lines deployed | 2–3 partial lines | 5–6 full lines | 10–12 full lines |
| Per-line content captured | LIDE-A drilling tool only (€4M) | 3-tool partial line (drilling + bonding + singulation, ~€10M) | Full 4-tool line including CPO (€13M) |
| Substrate-end mass production | 12+ month slip across Tier-1 customers | On schedule (Samsung 2027, TSMC 2028–29) | On schedule + accelerated 2029 ramp |
| Plan Optik competitive outcome | Wins Samsung or Absolics pilot evaluation; LPKF loses anchor customer reference | LPKF retains Tier-1 customers; Plan Optik at second tier | LPKF dominant across Tier-1; Plan Optik in narrow niche |
| CPO product commercial outcome | No commercial deployment | Intel pilot ramping, modest revenue | Intel commercial + Broadcom/Marvell follow-on |
| Capital structure | Dilutive raise Q4 2026 at €18 strike (+5.65M shares → 28.2M total) | No dilution | No dilution |

**Revenue build (€M).**

| Year | Line item | Low | Base | Upside |
|---|---|---|---|---|
| **FY2027E** | LIDE equipment | 5 | 18 | 35 |
| | LIDE service/recurring | 1 | 3 | 5 |
| | Vitrion foundry | 3 | 5 | 10 |
| | CPO | 0 | 0 | 0 |
| | Welding + PCB (legacy) | 70 | 70 | 72 |
| | Solar (wind-down tail) | 2 | 0 | 0 |
| | **Total revenue** | **81** | **96** | **122** |
| **FY2030E** | LIDE equipment | 18 | 40 | 80 |
| | LIDE service/recurring | 5 | 10 | 18 |
| | Vitrion foundry | 5 | 15 | 25 |
| | CPO | 0 | 5 | 30 |
| | Welding + PCB (legacy) | 65 | 70 | 75 |
| | Solar | 0 | 0 | 0 |
| | **Total revenue** | **93** | **140** | **228** |

LIDE equipment in FY2030 reflects blended one-time tool revenue across deployed lines (low: 2–3 lines × ~€4M LIDE-A only = €18M; base: 5–6 lines × ~€7M average partial-line content = €40M; upside: 10–12 lines × ~€7M average full-line content recognising amortisation across deployment years = €80M). Service revenue scales with installed-base lines at ~€1.75M/line/yr. CPO is the largest discretionary swing — quantified separately below.

**EBIT margin and EBIT (€M).**

| Year | Metric | Low | Base | Upside |
|---|---|---|---|---|
| FY2027E | EBIT margin | -4% | 8% | 15% |
| FY2027E | EBIT (€M) | -3 | 8 | 18 |
| FY2030E | EBIT margin | 10% | 20% | 27% |
| FY2030E | EBIT (€M) | 9 | 28 | 62 |

EBIT margin progression: LIDE (higher margin) growing in mix while legacy (mid-margin) stays flat, Solar (loss-making) eliminated by 2027, Vitrion contributing service/consumables margin. Upside captures operating leverage on the CPO ramp + scale-driven SG&A absorption.

**FY2030 valuation.**

| Metric | Low | Base | Upside |
|---|---|---|---|
| EBIT (€M) | 9 | 28 | 62 |
| P/E multiple | 15x | 22x | 28x |
| Implied market cap (€M) | 135 | 616 | 1,736 |
| Shares outstanding (M) | 28.2 (post-dilution) | 22.55 | 22.55 |
| **Implied share price (€)** | **4.80** | **27.30** | **77** |
| **Return vs current ~€25** | **-81%** | **+9%** | **+208%** |

Multiple selection: low case is post-distress mid-cap industrial multiple (15x reflects damaged narrative + thin moat); base case is semicap mid-multiple consistent with LRCX/AMAT 5-year average; upside case is high-conviction qualification-gate monopoly multiple consistent with [[Theses/BESI - BE Semiconductor Industries]] / Camtek peak.

**Probability-weighted expected value.**

| Scenario | Probability | Share price (€) | EV contribution (€) |
|---|---|---|---|
| Low | 25% | 4.80 | 1.20 |
| Base | 50% | 27.30 | 13.65 |
| Upside | 25% | 77.00 | 19.25 |
| **Expected value** | | | **34.10** |

Expected value €34 vs current ~€25 = **+36% expected return**, with asymmetric +208% upside vs -81% downside skewed positive. The asymmetry is consistent with qualification-gate monopoly economics — if the moat holds, deployment compounds across multiple customer lines; if it breaks, the moat doesn't partially fail. Probability split skews 50% base because the equipment-S-curve timing model is the modal trajectory if Q2 2026 orders land — and that disclosure is structurally binary, so the resolution comes within 4 weeks of this thesis date.

**Triangulation against external models.**

| Model | 2030 revenue | 2030 MC | Per share | Note |
|---|---|---|---|---|
| Sell-side consensus (8 analysts) | implied via €15.81 PT | ~€360M | €15.81 | Bear-consensus model assumes either Q2 order slip OR substrate-end slip OR both; no CPO contribution; no tool-2/3/4 content |
| Shawarma Capital substack | €600–820M | €2.5–5B | €110–220 | Aggressive — assumes ~50-line global deployment; my upside (10–12 lines) is more conservative |
| **This thesis — base** | **€140M** | **€616M** | **€27.30** | Modal trajectory if equipment-S-curve materialises on schedule |
| **This thesis — upside** | **€228M** | **€1.74B** | **€77** | Full LIDE + meaningful CPO contribution |

Sell-side is well below even my low-case revenue but at similar share price — reflects multiple-compression bear assumption. Shawarma is well above my upside — reflects more aggressive customer-line count assumption. My base sits between consensus pessimism and Shawarma optimism.

**CPO optionality — quantified separately because it's the largest discretionary swing.**

| CPO scenario | 2030 CPO revenue | Mapped to scenario |
|---|---|---|
| Zero commercial deployment | €0 | Low |
| Intel exclusive pilot ramping, no other customers | €5M | Base |
| Intel commercial + Broadcom/Marvell follow-on (~10–12 tools at €3M) | €30M | Upside |
| Intel commercial + Broadcom + 20% market share through 2030 (~25 tools at €3M) | €75M+ | Super-upside (not in 3-case set) |

The 7,500× volume scaling from 50K → 380M CPO ports 2025–2032 means even 5–10% market share at €3M ASP per tool over a 100-tool 2025–2032 deployment is €15–30M/yr at peak. The base case captures only ~10% of credible CPO scenarios; the upside captures ~50%. CPO is optionality that compounds asymmetrically in the upside but is appropriately discounted in base/low.

**Sensitivity table — what moves the base case ±€10/share.**

| Variable | Base assumption | Sensitivity to +€10/share | Sensitivity to -€10/share |
|---|---|---|---|
| 2030 customer lines deployed | 5–6 | 8 lines | 4 lines |
| Per-line content captured | ~€10M (3 of 4 tools) | €12M (closer to full line) | €7M (drilling-only continued) |
| EBIT margin at 2030 | 20% | 23% | 17% |
| P/E multiple | 22x | 25x | 19x |
| CPO 2030 revenue | €5M | €15M | €0 |

The single largest sensitivity is customer-line count — a 2-line difference shifts the share price ~€10. Per-line content captured is second largest — driven by how quickly customers move from drilling-only (LIDE-A) to full 4-tool lines. EBIT margin and multiple are tertiary because they compound but at lower elasticity.

## Bull Case

The bull case requires three conditions to compound:

1. **Q2 2026 LIDE production orders land at promised scale and quality.** Management committed at June-4 AGM to first production orders by end Q2. If 2+ orders materialise at named Tier-1 customers (Samsung E-M, Absolics-Intel, DNP, JNTC, or TSMC) at unit ASPs consistent with disclosed €3.5–5M LIDE-A range and unit counts implying meaningful 2027 revenue contribution (e.g., 4+ tools = €15–20M+ in 2027), the equipment-S-curve timing model validates and the multiple rerates immediately. Short squeeze on Voleon + Marshall Wace positions amplifies. Stock target €40–60 in 6 months on rerating to semicap mid-multiple (~8x P/S) on €130–150M 2027 revenue projection.

2. **Per-line content expands toward disclosed 4-tool architecture.** As customer lines transition from pilot (1 LIDE-A drilling tool) to production (4-tool full line at €13M + €1.5–2M annual), the implied revenue per customer compounds 3×. With 10 customer lines deployed by 2029 — Samsung × 2, Intel/Absolics × 2, TSMC × 2, DNP × 2, JNTC × 1, Rapidus × 1 — equipment revenue is €130M one-time per year over 5 years (€26M/yr LIDE) plus €15–20M annual recurring at peak. Add the legacy €70M PCB + Welding base (Solar wound down) and total revenue at 2029 is ~€110–115M with much higher LIDE mix and >25% EBIT margin per Shawarma Capital scenario. Stock target €100–150 at 6x P/S on €130M revenue + 25% EBIT margin (€32M EBIT × ~25× P/E = €800M MC = ~€35/share, plus optionality), implying further upside if CPO contributes.

3. **CPO product reaches commercial deployment with Intel and/or Broadcom by 2028.** The 7,500× volume scaling from 50K → 380M CPO ports 2025–2032 creates substantial equipment demand if LPKF captures even 10–20% of the CPO waveguide-structuring market. At 20% share + €2.5–4M tool ASP + ~100 tools over the decade, this is €250–400M equipment + meaningful service. The bull case adds €20–30M annual run-rate from CPO by 2030, layering on top of the substrate-LIDE business.

**Probability-weighted bull case framework (per Shawarma Capital analysis adapted):** base 2030 revenue €600–820M, EBIT margin 22–28%, applies a 20–30x P/E multiple on the equipment-quality earnings stream → implied 2030 market cap €2.5–5B → 4–8x current, plus optionality on tool 4 (CPO).

**Bull case rationale leverages:**
- Patent-defended duopoly (per #2 mental model — qualification-gate monopoly hidden behind share data)
- Mid-chasm S-curve technology (per #18 mental model — high-edge zone for long-term capital)
- Architecture transition remapping bottleneck (per #8 — substrate-side transition to glass)
- "Picks and shovels" exposure to AI accelerator buildout without the cyclicality of substrate-vendor pricing

## Bear Case

The bear case is genuinely existential and has three independent paths to materialising:

1. **Q2 2026 LIDE production orders slip or arrive at sub-scale.** If the promised orders materialise but at 1 tool to 1 customer (a continuation of pilot phase rather than production phase), the equipment-S-curve thesis loses 12+ months of progress. Combined with the cash burn trajectory (€1.2M/quarter Q1), the equity enters a distressed scenario where management must accept dilutive financing — likely at sub-€20/share, destroying 30–50% of current equity value before any operational turnaround. Stock target €10–15 on order-slip + capital-raise narrative within 6–9 months.

2. **The substrate-end mass production timeline slips by 12+ months.** TSMC has been explicit that CoPoS mass production is "2-3 years away" — implying 2028–29 only if no further slip. Glass-core substrate technical issues (warpage, yield, thermal cycling reliability) could push mass production to 2030–31 across all Tier-1 customers. Per #17 mental model (new entrants don't materialise at tight prices) and the broader CHIPS-Act-funded capacity addition timing, multi-region glass-substrate ramp could be slower than the Street currently assumes. LPKF's equipment-S-curve needs 12–24 month lead time so a 12-month substrate slip implies a 12-month tool-revenue slip — punishing in a thin-cash position. Stock target €12–18 over 18 months if substrate-end visibly slips.

3. **Plan Optik undercuts on a key customer evaluation, or a new entrant (TRUMPF, EKSPLA) cracks LIDE-equivalent quality.** Plan Optik is a much smaller German private company with proven LIDE-at-scale per industry sources. A financially-constrained Plan Optik could rationally underbid to capture share — if Samsung E-M or Absolics chooses Plan Optik on price (saying "any LIDE-class vendor will do at our pilot volume"), LPKF loses the anchor customer reference for the 2027–2030 production ramp. Separately, TRUMPF (the largest industrial laser company globally, ~€5B revenue) has not publicly disclosed a LIDE-equivalent product but has the engineering capacity to develop one if the substrate market reaches the €1B+ TAM scale. The combined "lose to Plan Optik on price + TRUMPF enters in 2027–28" path collapses the duopoly thesis and forces LPKF's pricing power 50%+ down. Stock target €8–12 in 12–24 months.

**Compounded bear case** (per Mental Models #18 — conflating cycle and structural shifts is a bear-case error mode):
- Q2 2026 order slip → activist shareholder forced capital raise at distress price
- Solar wind-down extracts more restructuring cost than guided
- Cash falls below €3M → emergency bridge financing at distress terms
- Substrate-end slips to 2030–31 → LIDE production volumes never reach disclosed line economics
- Plan Optik captures Samsung pilot → reference customer lost
- TRUMPF enters in 2028 → duopoly becomes oligopoly

Combined: equity falls 60–75% from €25 to €6–10 within 18 months. The €15.81 analyst consensus PT can be read as roughly priced for items 1 (order slip) + 2 (substrate slip) but not 3 (competitive entry). The full bear case is €8–12.

## Catalysts

**Near-term (next 90 days):**
- **End of Q2 2026 (by 30-Jun-2026): LIDE production orders disclosure** — management committed at June-4 AGM to first production orders by Q2-end. Binary near-term setup. Possibly accompanied by named customer disclosure.
- **H1 2026 financial report (late July / early August 2026)** — Q2 numbers, order intake trajectory, cash position, FY2026 guide refresh

**Medium-term (3–12 months):**
- **Q3 2026 earnings (October–November 2026)** — first quarter to reflect post-AGM-disclosure order pull-through; segment revenue trajectory
- **Solar segment wind-down completion announcement (H2 2026)** — restructuring cost crystallisation; cleaner financial trajectory after
- **Substrate-vendor capacity announcements** — Samsung E-M next-phase Sejong investment, Absolics Georgia capacity confirmation, Intel India plant timeline updates
- **CPO partnership disclosure events** — if Intel restructures or expands CPO commitments, LPKF visibility into pipeline
- **Annual report 2026 (March 2027)** — first full-year LIDE production revenue disclosure; investor day

**Long-term (12–36 months):**
- **2027 LIDE production ramp** — per management commentary, this is when revenue inflection materialises
- **TSMC CoPoS small-volume trial (2027)** — substrate-end demand validation
- **Samsung 2027 mass production target** — if achieved, validates substrate-end S-curve
- **Patent enforcement events** — Plan Optik or TRUMPF patent challenges could trigger material legal events
- **2028–29 TSMC CoPoS mass production** — peak substrate-end demand

**Negative catalysts (could trigger downside):**
- Q2 2026 order slip or below-expectation disclosure
- Capital raise announcement at sub-€20 strike
- Short seller report (Voleon, Marshall Wace are quantitative funds but a directional short report is possible)
- Solar segment restructuring cost overrun
- Plan Optik or TRUMPF wins a major customer evaluation

## Risks

**Thesis risks (the investment case is wrong):**

1. **Substrate transition arrives slower or doesn't reach scale.** The base assumption that 10+ glass-substrate production lines deploy globally by 2030 requires Intel + Samsung + TSMC + DNP + Rapidus to all execute on their announced mass-production roadmaps. Per [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] §ABF monopoly durability — failure modes — the credible 2027–2030+ candidates for glass-core acknowledge significant uncertainty on whether glass actually displaces organic ABF at scale. If glass-core remains a niche (1–2 production lines for specific high-end applications, not 10+ across all Tier-1 customers), the LIDE TAM compresses 70%+.

2. **CPO doesn't transition to glass-waveguide structuring at production scale.** Polymer-waveguide approaches at TSMC COUPE, Broadcom, Marvell could remain dominant if cost-effective. The Intel CPO development is a real exclusive but its conversion to volume production is not guaranteed.

3. **Per-tool ASPs compress as customers gain leverage.** First-customer ASPs are set in a "we need LIDE-class equipment, you're the only qualified vendor" negotiation. By the third or fourth customer line, customers have leverage to negotiate ASPs down 20–30%. The €13M/line economics could compress to €8–10M/line at scale.

**Position risks (thesis is right but stock goes down anyway):**

4. **Cash runway insufficient to bridge to 2027 ramp.** Even if the equipment-S-curve materialises on schedule, LPKF could be forced into a dilutive capital raise in 2026–27 at sub-€20 strike. The dilution destroys 20–40% of equity value even if the operational thesis plays out.

5. **Multiple compression on macro / sector de-rating.** Even if LPKF executes on guidance, semicap multiples could compress in a broader AI-bubble correction (per [[Macro & Technology/AI Bubble Risk and Semiconductor Valuations]]). Multiple compression from current ~5x P/S to 3x P/S on €130M 2027 revenue = €390M MC = €17/share, a -30% drawdown despite operational success.

6. **German micro-cap liquidity and float dynamics.** Thin XETRA trading + US OTC limited volume means a 5% holder exit can pressure the stock 10–15%. The substantial substack-driven retail interest creates positioning fragility — if retail rolls out before the institutional accumulation materialises, the stock could trade at a discount to fundamental value for an extended period.

7. **Activist shareholder forcing extreme outcomes.** The June-4 AGM revealed a faction of shareholders willing to push for management changes, capital raises, or strategy shifts that may not align with long-term equity value. A successful activist push for dilutive raise (the shareholders demanded one) destroys value even if it accelerates LIDE.

8. **Currency translation.** Stock trades in EUR; revenue is multi-currency (EUR + KRW + USD + JPY). EUR strength compresses translated revenue without operational change.

## Conviction Triggers

- **→ HIGH if**: By end Q3 2026, LPKF discloses 2+ LIDE production orders at Tier-1 named customers (any combination of Samsung Electro-Mechanics, Absolics, Intel, DNP, TSMC, Rapidus, JNTC) at unit counts totalling 6+ tools and ASPs consistent with disclosed €3.5–5M LIDE-A range, AND cash position holds above €4M without bridge financing required. Validates equipment-S-curve timing model and removes near-term distress risk.

- **→ LOW if**: Q2 2026 LIDE production orders slip past 30-Sep-2026 OR cash falls below €3M without committed bridge financing facility OR Plan Optik (or any other LIDE-equivalent competitor) wins a publicly-disclosed Tier-1 customer evaluation that LPKF was competing for.

- **→ CLOSE if**: LIDE core patent successfully invalidated in any major jurisdiction (EU, Korea, US, Japan) OR a major substrate customer (Intel, TSMC, Samsung) publicly de-prioritises glass-core substrate investment in favour of organic ABF extension OR LPKF management announces a dilutive capital raise at sub-€15 strike (signals distressed financing rather than growth investment).

## Mental Models
<!-- Outputs from applying the /Mental Models context files to this opportunity. Per the READING PROTOCOL in [[Generalist - Overview]], these are lenses and questions, never conclusions — every entry is a hypothesis to test against the evidence in this thesis, not a verdict. Populated incrementally: each research pass appends the models it applied and the specific triggers that fired. -->
- **Models applied** (2026-07-09 batch-2 pass, evidence-tested against July-2026 web research): [[Generalist - Overview]] (S-curve, reflexivity, barbell) · [[Industry - Semiconductors]] (#2, #8, #19) · [[Lens - Value Layer Monopoly]]
- **Triggers + evidence status** — hypotheses tested, not verdicts:
	- *#19 orders signal — the binary went against, softly*: the CEO's "production orders by end Q2 2026" deadline passed Jun 30 with no series order (test installations only); goalposts moved ~6 months to "before end of 2026"; stock -28% from the €30.20 ATH into the miss, -46% at the Jul 8 low. A first LIDE capacity-expansion order WAS booked in Q1 with talks ongoing — the thesis's equipment-S-curve is alive but its timing model just slipped one notch. LOW-trigger clock runs to Sep 30; H1 report **Jul 23**.
	- *#8 bottleneck relocation — AGAINST the layer thesis, from the CEO's own mouth*: LIDE/TGV is "no longer the bottleneck" — glass-substrate yield now gates on *metallization* (Cu-adhesion/CTE, Atotech-MKS territory). VLM implication: the scarce layer may be migrating off LPKF's layer just as the wave arrives. Pair with the CEO's concession of TGV share 80%→70% and his naming TRUMPF+SCHMID full-line as the top threat — the thesis's moat-layer-4 ("TRUMPF waits") is contradicted by the primary source.
	- *S-curve geography re-drawn*: Korea-first confirmed — Absolics mass production targeted end-2026 with equipment POs expected by year-end (the nearest concrete volume trigger), Samsung glass to business-unit status (2027 ramp), JNTC 16 paying sample customers; but TSMC glass-CORE slipped past 2030 (CoPoS panel 2H28 is a different product) — the biggest single customer leg of the 2028–29 bull case moved out ~2 years.
	- *Cash-runway math REFUTED*: Q1 burn €4.3M (thesis: €1.2M/qtr), FCF -€7.6M, cash €5.8M ≈ ~1 quarter at Q1 pace — but a committed €12.5M undrawn line (facility to Dec-2028) exists, making the LOW cash-leg structurally hard to trip while the CFO "left the door open" to a raise (CLOSE trigger watch: sub-€15 strike). Update Key Metrics: end-2025 cash was ~€10.1M, not €7.0M.
	- *CPO parallel S-curve (Insight #3)* — CONFIRMED and ahead: production-ready 3D optical-waveguide-in-glass equipment already delivered and installed (The Elec, Apr 28); NEXAR panel-level tool line launching 2026 — publicly corroborating the multi-tool architecture behind Insight #1.
	- *Reflexivity* — the +329% spike was SDAX-inclusion flows + substack virality, not sell-side (consensus PT still €12–15.50, zero upgrades); short book rotated (Voleon down, Qube/SIH in, MW Group flipped to 3.14% long). Pre-chasm + funding-fragile → barbell says convex-bet sizing only, if at all, while status stays draft.
- **Disconfirming check** (evidence-updated): the thesis's two-S-curves insight is half-right — equipment orders DO lead substrates, but the equipment orders themselves slipped, and the CEO relocated the scarcity narrative downstream. Base rate: pre-revenue-inflection equipment names that miss their own first order deadline deliver the re-cut deadline <50% of the time — the "before end of 2026" promise is now the thesis. Single falsifiers: Absolics equipment POs by year-end (bull); a TRUMPF+SCHMID or Philoptics Tier-1 LIDE-equivalent win (bear, LOW leg 3); a sub-€15 raise (CLOSE). Watch-not-add until the Jul 23 H1 report shows order-pipeline specifics; the batch's only distress-adjacent name.

## Related Research

- [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] — primary sector; sets context for the substrate transition LPKF rides
- [[Sectors/Semiconductor Capital Equipment]] — equipment-cycle classification framework; LPKF as picks-and-shovels
- [[Sectors/Optical Networking & Photonics]] — CPO context for the tool-4 product family
- [[Theses/INTC - Intel]] — primary triangulated customer; Chandler glass pilot + India plant + CPO exclusive development partner
- [[Theses/2802 - Ajinomoto]] — incumbent ABF dielectric monopolist; glass-core substrate is the long-term displacement vector for the durable ABF franchise
- [[Theses/5332 - TOTO Ltd]] — ceramics substrate adjacent material play; orthogonal substrate-stack alternative
- [[Theses/TSM - Taiwan Semiconductor]] — CoPoS panel-level packaging customer; substrate-end demand
- [[Theses/BESI - BE Semiconductor Industries]] — advanced packaging equipment peer; comparable qualification-gate monopoly framework
- [[Theses/AMAT - Applied Materials]] — semicap WFE peer; multiple framework comparison
- [[Theses/LITE - Lumentum]] — photonics adjacent for CPO context
- [[Mental Models/Industry - Semiconductors]] — #1 (emerging bottlenecks), #2 (qualification-gate monopolies hidden behind share data), #8 (architecture transitions remap bottleneck), #10 (anchor customer concentration is binary survival test), #13 (compounder vs cyclical misclassification), #18 (cycle vs structural shifts)
- [[Macro & Technology/AI Bubble Risk and Semiconductor Valuations]] — multiple compression risk overlay

## Legacy Callouts
<!-- Auto-managed by /archive-callouts. Do NOT hand-edit. -->

## Log
### 2026-06-07
- Initial thesis created. Conviction: medium — LIDE qualification-gate duopoly with Intel/Samsung/TSMC substrate customer triangulation and CPO optionality, offset by binary Q2 2026 order setup, €5.8M cash buffer, and €15.81 sell-side consensus PT (-36% vs ~€25 current).
- Addressed user callouts: LIDE engineering deep-dive + competing-approach failure modes integrated into §Business Model → LIDE process physics + Competing approaches subsections; small-cap engineering-budget paradox + four-layer moat structure + Plan Optik vs TRUMPF threat decomposition integrated into §Industry Context — conviction unchanged (deeper substantiation of the qualification-gate moat thesis, not a delta to the investment case).
- Addressed user callouts: 3-scenario forecast (low/base/upside) added as new §Scenario Forecast section between Key Metrics and Bull Case — FY2030 implied share prices €4.80 / €27.30 / €77 with probability-weighted EV €34 (+36% vs current ~€25); CPO optionality quantified separately as the largest discretionary swing (€0/€5M/€30M 2030 revenue across cases); triangulated against sell-side consensus €15.81 PT and Shawarma Capital €110–220/share aggressive case. Conviction unchanged (quantification of existing thesis structure, not a new investment claim).

### 2026-07-09
- Mental models pass: batch-2 evidence sweep populated ## Mental Models — Q2 order deadline missed (goalposts → end-2026), CEO conceded share 80→70% + named TRUMPF/SCHMID top threat + relocated bottleneck to metallization (against the layer thesis); burn math refuted (€4.3M/qtr not €1.2M, €12.5M committed line is the real bridge); CPO leg confirmed ahead; Korea-first (Absolics POs by year-end = nearest trigger), TSMC glass-core slipped past 2030 — conviction unchanged (medium, draft); H1 report Jul 23, LOW clock to Sep 30.

### 2026-07-12
- Numbers refresh: 3 metrics updated, 3 material. Gross Margin ~35-40%→~19% (estimated margin roughly halved). FCF Yield left unedited — old_value_numeric in fetch data anomalous (4e12), format/data uncertain. Snapshot: [[_Archive/Snapshots/LPKF - LPKF Laser & Electronics (pre-numbers 20260712-174116)]]

### 2026-07-12 (/numbers)
- Numbers refresh (second same-day pass, fmp_symbol LPK.DE confirmed correct exchange-suffix mapping): 0 metrics changed. Market Cap (~€426M) and Gross Margin (~19%) render identically after rounding. Revenue Growth (compound Q1/FY26-guide string) left unedited — format uncertain. FCF Yield again left unedited — same data anomaly as prior pass (fetch value pairs a qualitative "Negative (-€4 to -€8M...)" cell with a corrupted numeric old-value ~€4T; do not apply). Snapshot: [[_Archive/Snapshots/LPKF - LPKF Laser & Electronics (pre-numbers 20260712-184147)]]
