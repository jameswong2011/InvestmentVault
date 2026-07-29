---
publish: true
date: 2026-06-18
tags: [macro, technology, semiconductors, packaging, advanced-packaging, CoPoS, FOPLP, panel-level, CoWoS, TSM, NVDA, glass-core]
status: active
sector: ABF Substrates & Advanced Packaging Supply Chain
source: vault synthesis (2026-06-18) — TrendForce CoPoS pilot-line + FOPLP/glass-core notes (Apr-13 & Jun-17 2026), TechPowerUp 310×310mm + 750×620mm panel reports, Wedbush/FinancialContent CoPoS rectangular-panel primer (Feb-2026), SemiEngineering "Rise of Panel-Level Packaging", damnang2 "If CoPoS Arrives, Who Makes Money First", wccftech/digitalcitizen NVIDIA Feynman-CoWoS-barrier reporting; cross-referenced against [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]], [[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]], [[Theses/TSM - Taiwan Semiconductor]], [[Theses/NVDA - Nvidia]], [[Theses/BESI - BE Semiconductor Industries]], [[Theses/KLA - KLA Corporation]]
---

# CoWoS-to-CoPoS Panel-Level Packaging Transition

*Tracker for the architectural shift in AI-accelerator advanced packaging from round-300mm-wafer carriers (CoWoS) to large rectangular panels (CoPoS — Chip-on-Panel-on-Substrate). This is a **format** transition (circle → rectangle), distinct from but converging with the **material** transition tracked in the companion note [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]] (organic ABF core → glass core). The two intersect from ~2028 when the 515mm panel generation adopts glass-core substrates. Multi-source synthesis; updated as inflection points hit.*

## Thesis Delta

- **The vault's own record is stale and pointing the wrong direction.** [[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]] and [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]] both encode the March-2026 narrative that TSMC pushed CoPoS "to Q4 2030 minimum." June-2026 reporting **reverses** this: pilot-line tool deliveries began Feb 2026, full pilot line completes ~June 2026 (VisEra), pilot production 2027, mass production H2 2028–29 at the AP7 Chiayi campus — anchored by NVIDIA Rubin (R100, late 2027) and Rubin Ultra (2028), with Feynman (2028+) explicitly designed to break the CoWoS reticle barrier. **The "extended OSAT overflow runway" thesis built on the delay is the single most exposed position in the vault book if the acceleration holds.**

- **CoPoS is a bottleneck-relocation event, not a cost story.** CoWoS-S tops out at ~3.3× reticle (~2,700 mm²) and converts only ~57% of a round 300mm wafer into usable large interposers — the rest is edge waste. A rectangular panel runs >87% area utilization; a 515×510mm panel yields ~20 interposers and supports ~9.5× reticle area — enough for 2+ compute dies plus **12–16 HBM4 stacks** in a single package, physically impossible to yield reliably on a circle. The binding constraint moves *off* the silicon interposer and *onto* panel-format lithography, inspection, placement accuracy, and large-format glass handling. Per [[Mental Models/Industry - Semiconductors]] #8, reading this remap before it is priced is the alpha.

- **"Picking stocks off the word glass leaves you most exposed."** The cleanest equipment exposure is **inspection/metrology**, which is required on *every* path — CoWoS, CoPoS, and CoWoP — and ships *first* (validation/qual stage, 2026), before anyone knows which format or substrate material wins. Glass-carrier and TGV-specific tooling is high-beta to the CoPoS path specifically and dies if timelines slip or competing formats (Intel EMIB-T, panel-on-organic) take share. The vault already owns the golden-coordinate names ([[Theses/KLA - KLA Corporation]]) and the placement/laser layers ([[Theses/BESI - BE Semiconductor Industries]], [[Theses/LPKF - LPKF Laser & Electronics]]); it does **not** own the panel-lithography layer (Onto Innovation) — the highest-leverage gap.

- **The biggest beneficiary set is downstream, not in the supply chain.** CoPoS is a supply-unlock for the AI accelerator buyers. It breaks the CoWoS capacity ceiling that has rationed [[Theses/NVDA - Nvidia]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], and [[Theses/MRVL - Marvell Technology]] since 2023, and it roughly doubles HBM content per package (8–12 → 12–16 stacks), a direct demand multiplier for [[Theses/000660 - SK Hynix]]. More shippable accelerators with more HBM per unit is the second-order trade most investors miss while staring at the equipment names.

- **The non-obvious winner is the display industry crossing into semiconductors.** FOPLP already runs at 620×750mm panels for PMIC/RF, and Taiwan's panel makers own exactly the capability CoPoS needs — large-format glass handling, precision alignment, uniform deposition on rectangular substrates. **Innolux (3481.TW) and Ibiden are named TSMC glass-substrate validation partners**; AUO (2409.TW) sits adjacent via its [[Theses/EINK - E Ink Holdings]] JV and IRIS Optronics arm. This is a capability-migration story straight out of [[Sectors/Display Technology & E-Paper]] — idle/commoditized LCD-fab competence repriced as scarce advanced-packaging competence.

- **CoPoS and glass-core are sequenced, not simultaneous.** Initial CoPoS (2027–28) uses a 310×310mm panel with an organic/RDL build — ABF survives here. The 515mm generation (2028–29) is where glass-core enters the CoPoS frame, linking this note to its companion. Anyone modeling "glass kills Ajinomoto in 2028" is conflating the format shift (now) with the material shift (later) — see [[Theses/2802 - Ajinomoto]] durability.

## Summary

CoWoS — Chip-on-Wafer-on-Substrate — has been the chokepoint of the AI build-out since 2023: every leading-edge accelerator from H100 to Blackwell is assembled on a silicon interposer cut from a round 300mm wafer, and TSMC's inability to add interposer capacity fast enough has rationed GPU supply industry-wide. The architecture has a hard ceiling. CoWoS-S interposers max out near 3.3× reticle (~2,700 mm²); the round wafer wastes ~43% of its area to edge geometry when tiling large rectangular interposers; and the next NVIDIA generations (Rubin Ultra 2028, Feynman 2028+) want packages with 2+ compute dies and 12–16 HBM4 stacks that simply do not fit. CoPoS — Chip-on-Panel-on-Substrate — answers all three by swapping the round wafer for a large rectangular panel: ~87% area utilization, ~9.5× reticle interposer area on a 515mm panel, and a roadmap of panel sizes (310×310mm → 515×510mm → 750×620mm) that scales with reticle growth rather than fighting it.

The timing inflected in 2026 and the vault has not yet caught up. As recently as the March-2026 roadmap revision encoded in [[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]], CoPoS was understood to be slipping toward "Q4 2030 minimum," which underwrote a bullish "pure-play OSAT advanced-packaging franchise extends 18–24 months" read. June-2026 reporting reverses that: TSMC began CoPoS pilot-tool deliveries in February, expects the pilot line complete around June at its VisEra subsidiary, targets pilot production in 2027 and mass production in 2H 2028–2029 at the AP7 Chiayi campus, and NVIDIA has reportedly selected CoPoS as the foundational packaging for Rubin. The "no shortcuts / 2-3 years away" framing from C.C. Wei in early 2026 has compressed into an active 2028 ramp. This is the inflection per [[Mental Models/Industry - Semiconductors]] #1 and #8 — the bottleneck is relocating, and equipment-validation orders pull 12–24 months ahead of the production ramp (#19: do not over-read those orders as production demand, but do read them as a leading timing signal).

The value created splits into five equipment layers plus materials, foundry/OSAT, and downstream demand. The structurally safest equipment exposure is inspection/metrology, which is path-agnostic (needed on CoWoS, CoPoS, and CoWoP alike) and ships first — KLA and the uncovered specialists Camtek and Onto Innovation. The highest-leverage *new* exposure is panel-format lithography, where round-wafer steppers do not physically apply and the field is being defined by Onto Innovation's JetStep, SUSS MicroTec, and adapted Canon/Nikon/SCREEN systems. Placement/bonding (BESI, ASMPT, Kulicke & Soffa), plating/deposition (Applied Materials, Lam, SCREEN, TEL), dicing/grinding (DISCO), and laser through-glass-via (LPKF for the glass-core variant) round out the picks-and-shovels. The losers are the silicon-interposer-centric CoWoS-S supply chain, round-wafer-format-locked tooling, and — if TSMC internalizes CoPoS as it did CoWoS — the pure-play OSAT overflow franchise whose runway the March-2026 delay had appeared to extend.

The widely-discussed names (NVIDIA as the demand anchor, TSMC as the developer) are correctly priced or hyped. The under-priced exposure sits where it always does in an architecture transition: the qualification-gated equipment layers that compound 12–24 months before the foundry ramp, and the adjacent-industry capability migration (Taiwan display-panel makers and glass suppliers) that the semiconductor sell-side does not cover.

## Framework / Mental Model

### Conventional framing vs correct framing

| Conventional framing | Correct framing |
|---|---|
| CoPoS is a cheaper version of CoWoS | CoPoS is a *capacity-and-size unlock*; cost crossover comes later, the binding driver is reticle/area physics and HBM-stack count |
| "Glass" is the CoPoS trade | Glass is one *high-beta* slice; the durable trade is path-agnostic inspection/metrology + panel litho that wins on CoWoS, CoPoS *and* CoWoP |
| CoPoS displaces CoWoS in 2028 | CoWoS, CoPoS and CoWoP **coexist**; CoPoS takes the largest/highest-HBM packages first, CoWoS retains mid-tier through 2030+ |
| CoPoS delayed to 2030 (March-2026 vault record) | Reversed — Feb-2026 tool deliveries, ~June-2026 pilot line, 2028–29 mass production, NVIDIA Rubin anchor |
| Glass-core kills Ajinomoto when CoPoS ramps | Format shift (now) ≠ material shift (515mm panel, 2028–29); ABF survives the first CoPoS generation |
| Panel packaging is a foundry/OSAT story | Equipment + adjacent display-industry capability capture most of the transition-year value |

### Architecture fork: CoWoS (wafer) vs CoPoS (panel)

| Dimension | CoWoS (incumbent) | CoPoS (challenger) |
|---|---|---|
| **Carrier format** | Round 300mm silicon wafer | Rectangular panel: 310×310mm → 515×510mm → 750×620mm |
| **Area utilization (large interposers)** | ~57% (edge waste) | >87% |
| **Interposer reticle limit** | ~3.3× reticle (~2,700 mm²) on CoWoS-S | ~9.5× reticle on 515mm panel |
| **HBM stacks per package** | 8–12 (Blackwell/early Rubin) | 12–16 (Rubin Ultra / Feynman class) |
| **Interposer material** | Silicon (wafer-fabbed) — capital-intensive, capacity-constrained | RDL-on-panel / organic (2027) → glass-core (2028–29) |
| **Litho** | Wafer steppers (ASML/Canon/Nikon) | Panel litho — Onto JetStep, SUSS, adapted Canon/Nikon/SCREEN |
| **First mass production** | Shipping since 2017 | 2H 2028–29 (TSMC AP7 Chiayi); pilot 2027 (VisEra) |
| **Anchor customer** | NVIDIA, AMD, AVGO, hyperscaler ASICs | NVIDIA Rubin / Feynman (reported) |

### Historical analogs

1. **200mm → 300mm wafer transition (late-1990s–2000s).** The last time the industry changed substrate *format*. Equipment had to be re-tooled wholesale; vendors who made the jump (AMAT, TEL, ASML) compounded, those who stayed 200mm-only were stranded. Lesson per [[Mental Models/Industry - Semiconductors]] #13/#14: a wafer-format-locked supplier that fails the panel transition *reclassifies down*; a panel-native vendor (Onto JetStep) *reclassifies up*. CoPoS is the first format change of comparable magnitude in 25 years, confined to advanced packaging rather than the full fab.

2. **Display/PCB panel-level manufacturing → semiconductor packaging (capability migration).** FOPLP did not invent panel handling — it imported it from the FPD and PCB industries, which have run Gen-class rectangular glass panels for decades. This is why **Taiwan's display ecosystem (AUO, Innolux) and glass suppliers (Corning, AGC, NEG) are structural CoPoS beneficiaries**: their large-format-glass alignment and uniform-deposition competence, commoditized in LCD, is scarce in semiconductors. Cross-industry capability migration is the under-modeled vector — see [[Sectors/Display Technology & E-Paper]].

3. **CoWoS itself displacing MCM/laminate (2.5D adoption, 2017–2023).** When 2.5D arrived, TSMC captured the value by verticalizing the interposer rather than ceding it to OSATs — the InFO/CoWoS playbook. The base rate says TSMC does the same with CoPoS: internalize at AP7 Chiayi, leave OSATs the overflow only until capacity catches up. This is the bearish read on the pure-play OSAT "panel franchise" hope in [[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]] Q3.

4. **S-curve location.** CoPoS sits **pre-chasm to early-chasm** (pilot 2026–27, HVM 2028–29) — binary outcome distribution, highest-edge zone for long-horizon capital, and equipment vendors lead the foundry ramp by 12–24 months. Per #18, decompose any CoPoS-driven move into the cycle component (AI capex) vs the structural component (format transition); the structural component is what the market underprices.

### The bottleneck cascade

Five layers, each gating the next; today's binding layer is **panel-format process maturity at TSMC's pilot line + panel-litho qualification** — not glass supply (ready) or demand (NVIDIA committed):

1. **Glass / panel supply** (Corning, AGC, NEG, Schott; Taiwan AUO/Innolux): large-format dimensional precision. Ready today for 310mm; 515mm+ is the qual frontier.
2. **Panel lithography + temporary bond/debond** (Onto JetStep, SUSS MicroTec, adapted Canon/Nikon/SCREEN): die-shift, CTE-mismatch and panel-warpage correction that round-wafer steppers cannot do. **The binding equipment layer.**
3. **Inspection / metrology** (KLA, Camtek, Onto): path-agnostic, ships first; the layer that earns regardless of which format/material wins.
4. **Placement, bonding, RDL formation, dicing, TGV** (BESI, ASMPT, K&S; AMAT/Lam/SCREEN/TEL; DISCO; LPKF for glass): panel-scale accuracy and throughput.
5. **Foundry/OSAT integration + downstream pull** (TSMC AP7 Chiayi; OSAT overflow; NVIDIA/AMD/AVGO/MRVL + SK Hynix HBM): the demand that makes the panel economically necessary.

## Panel-size and area-utilization trajectory

| Generation | Panel / carrier | Approx. area vs 300mm wafer | Interposer reticle area | HBM stacks | Status / customer |
|---|---|---|---|---|---|
| CoWoS-S (2023–) | 300mm round Si wafer | 1.0× (≈57% usable) | ~3.3× reticle | 8 | Mass production — H100/B200 |
| CoWoS-L (2024–26) | 300mm round Si wafer + RDL | 1.0× | ~3.3–5.5× reticle | 8–12 | Mass production — Blackwell/early Rubin |
| CoPoS Gen-1 (2027 pilot) | 310×310mm panel (organic/RDL) | ~1.4× | larger, sub-9.5× | 12+ | TSMC VisEra pilot |
| CoPoS Gen-2 (2028–29 HVM) | 515×510mm panel (+ glass-core) | ~3× | ~9.5× reticle (~20 interposers/panel) | 12–16 | TSMC AP7 Chiayi — NVIDIA Rubin Ultra |
| CoPoS Gen-3 (post-2030) | 750×620mm panel (glass-core) | ~4× | reticle-scaling-natural | 16+ | Projected — Feynman class |
| FOPLP (today) | up to 620×750mm panel | ~4× | n/a (fan-out) | n/a | Volume production — PMIC/RF/low-end |

The decisive number is HBM stacks × usable area per package: a 515mm panel supports the 12–16-stack HBM4 configurations that Rubin Ultra and Feynman require and that no round wafer can yield economically. The 2026–28 window is the proving period — panel litho/inspection vendors compound on validation+qual orders, TSMC proves panel yield, NVIDIA commits volume.

## Value chain — beneficiaries by layer

Legend: **[VAULT]** = existing thesis; **[WATCH]** = on [[Watchlist]] / monitored; **[NEW]** = surface candidate, not yet covered.

| Layer | Beneficiary | Vault status | Why it wins on CoPoS |
|---|---|---|---|
| **Panel lithography** | Onto Innovation (ONTO) | **[NEW]** | JetStep S3500/G purpose-built for PLP — corrects die-shift, CTE mismatch, panel warpage that wafer steppers cannot. Highest-leverage uncovered name. |
| | SUSS MicroTec (SMHN.DE) | **[NEW]** | Panel litho (mask aligners/coaters) + temporary bond/debond for panel carriers. |
| | Canon (7751.T) / Nikon (7731.T) | **[NEW]** | Adapting steppers + nanoimprint to panel format; relative share *shifts* from pure wafer steppers. |
| **Inspection / metrology** ("golden coordinate") | [[Theses/KLA - KLA Corporation]] (KLAC) | **[VAULT]** | Path-agnostic — needed on CoWoS, CoPoS, CoWoP; ships first at validation/qual. Qualification-gate moat per #2. |
| | Camtek (CAMT) | **[NEW]** | Advanced-packaging / panel inspection pure-play; the cleanest mid-cap PLP inspection beta. |
| | Onto Innovation (ONTO) | **[NEW]** | Dragonfly inspection + metrology in addition to litho — double exposure. |
| **Placement / bonding / hybrid bond** | [[Theses/BESI - BE Semiconductor Industries]] (BESI.AS) | **[VAULT]** | Die placement accuracy + D2W hybrid bonding; panel-scale placement is a content-per-tool expansion. |
| | ASMPT (0522.HK), Kulicke & Soffa (KLIC) | **[NEW]** | Panel die-attach / TCB at throughput. |
| **Deposition / plating / etch (RDL)** | [[Theses/AMAT - Applied Materials]] (AMAT) | **[VAULT]** | Panel-format PVD/plating; existing PLP tool exposure. |
| | [[Theses/LRCX - Lam Research]] (LRCX) | **[VAULT]** | Cu plating (SABRE) + etch for panel RDL. |
| | SCREEN (7735.T), Tokyo Electron (8035.T) | **[NEW]** | Coater/developer + wet process scaled to panels. |
| | [[Theses/ASMI - ASM International]] (ASM.AS) | **[VAULT]** | ALD — more front-end-weighted; neutral-to-modest panel pull. |
| **Dicing / grinding** | DISCO (6146.T) | **[NEW]** | Dominant in AP grinding/dicing; panel singulation is incremental TAM. |
| **Laser / through-glass-via** | [[Theses/LPKF - LPKF Laser & Electronics]] (LPK.DE) | **[VAULT/draft]** | LIDE TGV + panel singulation for the *glass-core* CoPoS variant (2028–29). Cross-ref glass-core note. |
| **Glass / panel material** | Corning (GLW), AGC (5201.T), NEG (5214.T), Schott | **[NEW]** | Large-format glass panels/carriers; industrial-glass qualification moat. |
| | AUO (2409.TW), Innolux (3481.TW) | **[NEW]** | Taiwan display-panel makers; **Innolux a named TSMC glass-substrate validation partner**; large-format-glass capability migration. |
| | UV-tape / temporary-bond / molding materials (Resonac, Brewer Science, Nagase, [[Theses/2802 - Ajinomoto]] ABF extension) | mixed | Consumables for panel handling + RDL dielectric; ABF persists in Gen-1 organic CoPoS. |
| **Test** | [[Theses/FORM - FormFactor]] (FORM) | **[WATCH]** | Probe cards — panel-level probe is a new high-value opportunity. |
| | [[Theses/6857 - Advantest]] (6857.T), [[Theses/TER - Teradyne]] (TER), 6515 WinWay (6515.TW) | **[VAULT/WATCH]** | Final/SLT test + interface for larger, higher-HBM packages. |
| **Foundry / OSAT** | [[Theses/TSM - Taiwan Semiconductor]] (TSM) | **[VAULT]** | CoPoS owner; verticalizes the next interposer franchise, breaks its *own* CoWoS bottleneck. |
| | ASE (3711.TW), Amkor (AMKR), Powertech (6239.TW) | **[NEW]** | *Conditional* — win only if they reach panel HVM before TSMC internalizes (Powertech FOPLP pilot at 600×600mm is the hedge). |

## Downstream adoption — winners and losers

### Downstream winners (CoPoS as a supply-and-size unlock)

| Beneficiary | Vault status | Mechanism |
|---|---|---|
| [[Theses/NVDA - Nvidia]] | **[VAULT]** | Rubin/Feynman anchored on CoPoS; breaks the CoWoS capacity ceiling that rationed GPU supply since 2023; larger packages = more compute + HBM per accelerator. |
| [[Theses/000660 - SK Hynix]] | **[VAULT]** | 8–12 → 12–16 HBM stacks per package ≈ HBM content multiplier per accelerator; biggest second-order memory winner. Per [[Sectors/DRAM & HBM Memory]]. |
| [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell Technology]] | **[VAULT]** | More interposer area for chiplet + HBM scaling on MI400-class and custom hyperscaler ASICs; relieves the shared CoWoS allocation fight. |
| [[Theses/META - Meta]] + hyperscalers; [[Theses/NBIS - Nebius Group]], [[Theses/CRWV - CoreWeave]] | **[VAULT/WATCH]** | More AI compute shippable per TSMC packaging dollar = more accelerators into racks; neocloud supply eases. |
| Kioxia / SanDisk ([[Theses/285A - Kioxia]], [[Theses/SNDK - SanDisk]]) | **[VAULT/WATCH]** | Indirect — larger AI systems pull more co-located NAND; smaller than the HBM read. |

### Losers / at-risk

| At-risk | Vault status | Mechanism |
|---|---|---|
| **Silicon-interposer / CoWoS-S supply chain** | partial | CoPoS substitutes RDL-on-panel / glass for large Si interposers; per-package silicon-interposer wafer consumption falls at the high end. The capital-intensive, capacity-constrained CoWoS-S interposer is the thing CoPoS is built to escape. |
| **Round-wafer-format-locked equipment** | mixed | Tools that cannot scale to rectangular panels lose share to panel-native vendors. **ASML**: EUV/DUV front-end unaffected, but packaging-litho share is contestable to Onto/SUSS/Canon on panels (relative, not absolute, risk). |
| **Pure-play OSAT overflow franchise** | **[NEW]** | If TSMC internalizes CoPoS (CoWoS base rate), the "delay extends overflow 18–24 months" thesis in [[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]] reverses; ASE/Amkor advanced-packaging runway compresses. |
| **ABF substrate incumbents (long-term)** | **[VAULT]** | Glass-core within the 515mm CoPoS generation (2028–29) is the slow displacement vector for [[Theses/2802 - Ajinomoto]] / Ibiden / Unimicron — *gradual*, per the companion glass-core note; ABF survives Gen-1 CoPoS. |
| **High-end wafer-level fan-out (InFO/FOWLP)** | n/a | Panel-level supersedes wafer-level fan-out for the *largest* packages; wafer-level retains mobile/edge/smaller die. |
| **Wafer-level burn-in test format** | **[VAULT]** | [[Theses/AEHR - Aehr Test Systems]] WaferPak is wafer-format; a shift of test steps to panel level is a watch-item (niche, not core — flag only). |

## Where the structural alpha sits

The transition-year value concentrates in qualification-gated equipment layers 12–24 months ahead of the 2028–29 foundry ramp. Ranked by edge:

1. **Panel lithography — the uncovered gap.** Onto Innovation (ONTO) is the cleanest expression: JetStep is purpose-built for PLP and round-wafer steppers physically do not apply. **Candidate for `/thesis ONTO`.** SUSS MicroTec (SMHN.DE) is the secondary litho+bond play.
2. **Path-agnostic inspection.** [[Theses/KLA - KLA Corporation]] (owned) wins regardless of format/material and ships first. Camtek (CAMT) is the uncovered mid-cap beta — **candidate for `/thesis CAMT`.**
3. **Owned equipment layers with CoPoS optionality.** [[Theses/BESI - BE Semiconductor Industries]] (placement/hybrid bond), [[Theses/AMAT - Applied Materials]] + [[Theses/LRCX - Lam Research]] (panel plating/depo), [[Theses/LPKF - LPKF Laser & Electronics]] (glass TGV) — CoPoS is incremental upside to existing theses; revisit position sizing on the acceleration.
4. **Adjacent-industry capability migration.** Glass (Corning/AGC/NEG) + Taiwan panel makers (AUO/Innolux). Initiate after first CoPoS panel-yield confirmation 2027. DISCO (6146.T) for dicing/grinding.
5. **Downstream re-rate.** The owned accelerator + HBM book ([[Theses/NVDA - Nvidia]], [[Theses/000660 - SK Hynix]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell Technology]]) is the largest beneficiary by dollars — CoPoS is a supply-ceiling removal, not just an equipment trade.

## Catalysts and signposts

**Near-term (next 90 days):**
- **~June 2026: TSMC CoPoS pilot-line completion at VisEra** — the marquee signpost; any disclosure on panel yield / size confirms the acceleration.
- **TSMC Q2 2026 earnings (mid-July)** — CoPoS roadmap update vs the "2-3 years away" March-2026 framing; AP7 Chiayi capex.
- **NVIDIA commentary** — confirmation/denial that Rubin/Rubin Ultra is on CoPoS.
- **SEMICON West (July 2026)** — Onto / SUSS / Camtek / DISCO panel-tool disclosures; competitive intelligence on the litho/inspection battleground.

**Medium-term (3–12 months):**
- Equipment-validation order flow at panel-litho/inspection vendors (read as timing signal per #19, not production demand).
- Innolux / AUO / Ibiden glass-substrate qualification milestones with TSMC.
- Powertech / ASE FOPLP-panel pilot progress (the OSAT hedge against internalization).

**Long-term (12–36 months):**
- **2027: CoPoS pilot production**; NVIDIA Rubin R100 (late 2027) first volume.
- **2028–29: mass production at AP7 Chiayi**; 515mm panel + glass-core convergence; Rubin Ultra.
- **Post-2030: 750×620mm panels**; Feynman-class glass-core CoPoS.

**Negative catalysts (transition slips right):**
- TSMC panel-yield miss pushes HVM past 2029 (re-validates the OSAT-overflow extension).
- NVIDIA keeps Rubin on CoWoS-L + reticle-stitching, defers CoPoS to Feynman only.
- Intel EMIB-T / panel-on-organic takes the large-package share CoPoS targets.
- AI-accelerator demand inflection (per [[AI Bubble Risk and Semiconductor Valuations]]) removes the package-size growth that makes panels necessary.

## Trading and portfolio implications

- **Audit the stale OSAT read first.** [[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]] and [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]] encode "CoPoS to Q4 2030." If the June-2026 acceleration holds, the bullish OSAT-overflow-extension thesis weakens — run `/sync` to propagate this delta, or revisit OSAT sizing manually.
- **Initiate the uncovered equipment layer.** `/thesis ONTO` (panel litho — the cleanest gap) and `/thesis CAMT` (path-agnostic panel inspection). Both lead the 2028–29 ramp by 12–24 months and are absent from the book.
- **Re-rate owned CoPoS optionality.** [[Theses/KLA - KLA Corporation]], [[Theses/BESI - BE Semiconductor Industries]], [[Theses/AMAT - Applied Materials]], [[Theses/LRCX - Lam Research]], [[Theses/LPKF - LPKF Laser & Electronics]] — CoPoS is incremental upside not yet in consensus models.
- **Hold the downstream beneficiaries for the supply-unlock.** [[Theses/NVDA - Nvidia]] + [[Theses/000660 - SK Hynix]] are the largest-dollar winners (capacity ceiling removed + HBM-per-package multiplier).
- **Watchlist the capability-migration names.** Corning (GLW), AGC (5201.T), AUO (2409.TW), Innolux (3481.TW), DISCO (6146.T) — initiate after 2027 panel-yield confirmation.
- **Key portfolio question 2026–2030:** how much capital to the equipment-S-curve (Onto/Camtek/KLA/BESI, 12–24 months early) vs the downstream supply-unlock (NVDA/SK Hynix). The 200→300mm and CoWoS base rates say equipment vendors capture the majority of *transition-year* value creation; the downstream names capture the larger but later earnings pool.

## Related theses + sectors

- [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]] — **companion note**; material shift (glass core) that converges with this format shift at the 515mm panel generation (2028–29)
- [[Sectors/OSAT - Outsourced Semiconductor Assembly & Test]] — CoPoS internalization vs OSAT overflow; **stale "Q4 2030" timing to reconcile**
- [[Sectors/Semiconductor Capital Equipment]] — equipment picks-and-shovels framework (no CoPoS coverage yet — gap)
- [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] — incumbent substrate stack; displacement timing
- [[Sectors/Display Technology & E-Paper]] — Taiwan panel-maker capability migration into packaging (AUO/Innolux)
- [[Sectors/Semiconductor Test Equipment]] — panel-level test demand
- [[Sectors/DRAM & HBM Memory]] — HBM-stacks-per-package multiplier
- [[Theses/TSM - Taiwan Semiconductor]] — CoPoS developer (AP7 Chiayi / VisEra pilot)
- [[Theses/NVDA - Nvidia]] — Rubin/Feynman anchor customer; capacity-ceiling unlock
- [[Theses/000660 - SK Hynix]] — HBM content multiplier
- [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell Technology]] — accelerator beneficiaries
- [[Theses/KLA - KLA Corporation]] — path-agnostic inspection (golden coordinate)
- [[Theses/BESI - BE Semiconductor Industries]] — placement / hybrid bonding
- [[Theses/AMAT - Applied Materials]], [[Theses/LRCX - Lam Research]], [[Theses/ASMI - ASM International]] — panel deposition/plating/etch
- [[Theses/LPKF - LPKF Laser & Electronics]] — glass TGV for glass-core CoPoS
- [[Theses/FORM - FormFactor]], [[Theses/6857 - Advantest]], [[Theses/TER - Teradyne]], [[Theses/6515 - WinWay Technology]] — test layer
- [[Theses/2802 - Ajinomoto]] — ABF incumbent; survives Gen-1 CoPoS, slow glass-core displacement
- [[Theses/AEHR - Aehr Test Systems]] — wafer-level burn-in format watch-item
- [[Theses/EINK - E Ink Holdings]] — AUO JV adjacency to display-panel capability migration
- [[Theses/INTC - Intel]] — competing panel/EMIB-T approach
- [[Mental Models/Industry - Semiconductors]] — #1 (emerging bottleneck = pricing power), #2 (qualification-gate monopolies — inspection/litho), #8 (architecture transitions remap the bottleneck), #13/#14 (format-locked vendors reclassify down; panel-native up), #17/#19 (inelastic supply; equipment orders lead, don't over-read)
- [[AI Bubble Risk and Semiconductor Valuations]] — demand overlay gating package-size growth

## Log

### 2026-06-18
- Initial macro note created. Documents the CoWoS→CoPoS panel-level packaging format transition (round 300mm wafer → 310/515/750mm rectangular panels), distinct from but converging with the companion glass-core *material* transition note at the 515mm generation (2028–29). Captured the **timing reversal**: vault record (OSAT sector + glass-core note) encodes March-2026 "CoPoS to Q4 2030 minimum"; June-2026 reporting shows acceleration — Feb-2026 tool deliveries, ~June-2026 VisEra pilot line, 2027 pilot production, 2H 2028–29 mass production at AP7 Chiayi, NVIDIA Rubin/Feynman anchor. Mapped beneficiaries across 8 value-chain layers + downstream winners/losers. Flagged 3 uncovered surface candidates: Onto Innovation (ONTO, panel litho — highest-leverage gap), Camtek (CAMT, path-agnostic inspection), DISCO (6146.T, dicing). Key non-consensus framing: inspection/metrology is the "golden coordinate" (wins on CoWoS/CoPoS/CoWoP, ships first); display-industry capability migration (AUO/Innolux/glass) is the under-modeled vector. Action items surfaced for user: reconcile stale OSAT timing via `/sync`; consider `/thesis ONTO` and `/thesis CAMT`. Run `/graph last` to register new wikilinks.

### 2026-07-14 (/sync)
- [[Research/2026-07-14 - Intel Foveros Direct vs CoWoS Advanced Packaging - deep-dive]]: Corroborates the "Intel EMIB-T / panel-on-organic as competing large-package path" negative-catalyst and the inspection/metrology-is-path-agnostic framing. Adds the EMIB-vs-CoWoS structural trade-off (EMIB lower-cost but edge-shoreline routing only; CoWoS any-point + embedded interposer capacitance) and the Foveros-Direct-3D yield-parity gate (D0<0.1 vs early ~0.2-0.25). No timing/framework change to the CoPoS transition.
