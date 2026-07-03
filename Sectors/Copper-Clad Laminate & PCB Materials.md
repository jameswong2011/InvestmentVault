---
date: 2026-06-10
tags: [sector, moc, copper-clad-laminate]
status: active
sector: Copper-Clad Laminate & PCB Materials
---

# Copper-Clad Laminate & PCB Materials

High-speed copper-clad laminate (CCL) and prepreg — the glass-fabric-reinforced, copper-foil-clad dielectric that forms the printed circuit boards beneath AI accelerators (GPU baseboards, HGX/UBB carriers, 1.6T switch trays, NIC cards). The "M-grade" loss spec (M4→M9, now M10) governs signal integrity at 112G/224G/448G SerDes. CCL sits one layer below [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] (the IC-package carrier) and is gated upstream by a low-Dk glass-cloth near-monopoly ([[Theses/3110 - Nitto Boseki]]). The organizing insight: a ~US$17B CCL market has **bifurcated into two industries** — a ~$13B commodity FR-4 base (China-led, cyclical, ~6% CAGR) and a ~$4B high-speed/AI premium (Taiwan/Japan-led, de-commoditizing, ~10% CAGR with the AI-server sub-slice compounding ~20%+) — and the market still prices the second through the lens of the first. Specialty AI/radar grades already carry 30–50% price premiums over commodity FR-4, and that spread is widening, not mean-reverting.

The deeper structural read: AI did not just grow CCL demand, it **moved the bottleneck up the stack**. The binding constraint is no longer the laminator's press — it is the three scarce inputs the laminator is *allocated* (low-Dk glass cloth, HVLP copper foil, low-loss PPE resin), each a Japan/Taiwan oligopoly, each sold out, each compounding the leaders' moat ([[Mental Models/Industry - Semiconductors]] #1, #8). This note maps all four layers — glass/foil/resin → CCL → PCB fab → ODM — because the AI-PCB value pool is being fought over at every one.

## Active Theses
- [[Theses/2383 - Elite Material]] (2383.TW, draft → MEDIUM) — global #1 *high-speed* CCL (~28% share); the toll road under hyperscaler ASIC + 1.6T switch boards (~100% Meta MTIA, ~80% AWS Trainium, ~50% Google TPU). Pending promotion via `/status`.
- [[Theses/3110 - Nitto Boseki]] (3110.JP, draft → MEDIUM) — the upstream glass-cloth near-monopoly (~90% T-glass, ~60–70% NER-glass) that gates this sector *and* the ABF-substrate stack. Pending promotion via `/status`.

*Adjacent investable names not yet in book (watchlist — see §Investor heuristics → Cross-vault attractiveness): Panasonic (6752.JP, Megtron benchmark), TUC (6274.TW), ITEQ (6213.TW), Shengyi (600183.SS, the China high-end wildcard), Kingboard (0148.HK, vertical-integration play), Mitsui Mining & Smelting (5706.JP, #1 HVLP foil), Zhen Ding (4958.TW)/Victory Giant (HK-listed, NVIDIA AI-PCB share-gainer) at the PCB-fab layer.*

## Key industry questions
- **Does the high-end premium survive the synchronized 2027 capacity vintage?** EMC, TUC, ITEQ, Panasonic, Shengyi and Nan Ya are all adding high-end lines, bunched into one ~2027 start-up wave by the ~2-year equipment lead (vacuum-press/treater orders are now booked through 2028). High-end specialty premia have historically compressed once capacity catches demand — the central tension of the sector ([[Mental Models/Industry - Semiconductors]] #6, #17).
- **Does the China *volume* cohort (Kingboard, Shengyi) climb the grade curve to contest the Taiwan/Japan *quality* leaders?** Shengyi is already NVIDIA-qualified (Synamic9GN) and reportedly progressing toward M10; state-backed, captive China demand. Qualified M8 at a *Western* hyperscaler by 2027 would cap the incumbents' China TAM and anchor high-end price.
- **Does the upstream input bottleneck stay a moat-widener or flip to margin compression?** Three scarce inputs (Nittobo glass, HVLP copper foil, PPE resin) entrench the largest CCL buyers today; if mid-2027 capacity across all three lands while AI demand cools, pass-through cover and the allocation barrier disappear together.
- **Does architecture substitution erode CCL content?** Glass-core substrates (the layer above), CPO/optics, and panel-level packaging could each reduce PCB layer count and per-board CCL content at the very leading edge — long-dated (2027–2030+) but real ([[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]]).
- **Where in the AI-PCB chain does the value actually pool — material, fabricator, or foil?** CCL is ~30–40% of a high-layer-count AI board's bill of materials, but the PCB fabricator (Zhen Ding, Victory Giant, Unimicron) captures the assembly margin and the foil/glass/resin makers capture the scarce-input rent. The investable question is which layer holds pricing power through the cycle.
- **What is the ROIC of the supply response to 2030?** The variable that decides whether the capacity build is disciplined (high-ROIC, price-supportive) or destructive (ROIC-insensitive state-backed supply compressing ASP).

## Industry history

### Origin: a Western invention standardized as FR-4
CCL is a mid-20th-century invention — woven fiberglass impregnated with epoxy resin and clad in copper foil — that became the universal PCB substrate as **"FR-4"** (the NEMA-graded flame-retardant epoxy-glass spec, "FR" = flame retardant). The franchise was originally **Western**: Park Electrochemical entered in 1961 by buying New England Laminates ("Nelco," Stamford CT); Isola (Germany/US), Rogers and Taconic built the early high-performance and RF/PTFE niches that still anchor the highest-frequency end today. For three decades CCL was a low-differentiation industrial commodity sold on copper and resin spreads.

### The center of gravity migrated east in three waves
1. **Japan (1970s–1990s) — the quality franchise.** Panasonic/Matsushita, Hitachi Chemical (now Resonac), and Mitsubishi Gas Chemical industrialized high-reliability laminate. Panasonic's **Megtron** line became — and remains — the low-loss quality benchmark; the industry's "M-grade" loss shorthand is anchored to Megtron generations (M4→M6→M7→M8).
2. **Taiwan (1990s–2010s) — the specialist cluster.** Nan Ya Plastics (Formosa group), **Elite Material (EMC)**, Taiwan Union Technology (TUC) and ITEQ built a high-speed cluster co-located with the world's PCB and ODM base (Zhen Ding, Unimicron, Foxconn, Quanta). EMC became the largest **halogen-free** CCL supplier in 2013 — a reliability/thermal/ESG edge that compounded at hyperscaler scale and is materially harder to engineer than the halogenated shortcut.
3. **China (2000s–present) — the commodity volume base.** **Kingboard** (first laminate plant 1988, Shenzhen) and **Shengyi/SYTECH** (founded 1985, Guangdong) won commodity FR-4 on scale, cost and deep vertical integration (own copper foil, glass yarn, glass fabric, resin). By Prismark's count Shengyi has been the **world's #2 CCL maker by volume since 2013**, behind Kingboard — both still commodity-weighted.

### The Western legacy consolidated into Asia
AGC (Japan) bought Park/Nelco in 2018–19 (~$150M) and Taconic in 2019, folding both into "AGC Multi Materials" for high-end high-speed CCL; Park exited to aerospace (now Park Aerospace). Doosan had earlier absorbed Kolon Electronics (1998) to form Doosan Electro-Materials (high-end laminate, RF). The net result by the mid-2020s: a durable **volume-vs-quality split** — Chinese makers dominate FR-4 tonnage; a Taiwan/Japan cluster dominates the low-loss high-speed grades; the West is a residual tier-2 in RF/PTFE.

### The AI inflection (2023–2026) turned a niche into a chokepoint
As accelerator boards went to 28–34 layers at 112G/224G SerDes, low-loss CCL (M7→M9) became the binding material under every GPU and custom-ASIC board. The signature of the shift: pricing power emerged where none had existed (20–40% high-end hikes through early 2026), gross margins at the leaders *expanded* into a capacity build (EMC 30.1%, +3.1pp YoY), PCB raw-material prices rose up to 40%, and the true bottleneck moved *upstream* to the three scarce inputs — Nittobo low-Dk glass cloth, HVLP copper foil (Goldman calls the shortfall a "new normal" 3-year crisis), and PPE/PPO resin. The market is still re-rating the sector from "cyclical laminate commodity" toward "AI materials oligopoly," and that re-rating is incomplete — the core mispricing this sector trades on.

## Competitive dynamics

The sector is **two competitive arenas that share a name**:

**Arena 1 — commodity FR-4 (volume game, China-led).** Won on scale, cost and vertical integration. Cyclical, priced on copper/resin spreads, ~6% CAGR. ~$13B of the ~$17B total.

**Arena 2 — high-speed / AI CCL (spec-in game, Taiwan/Japan-led).** Won on resin chemistry, qualification, first-mover and scarce-input allocation. De-commoditizing, margin-expanding, ~10% CAGR with the AI-server sub-slice ~20%+. ~$4B and the entire profit-growth engine.

### Market sizing — the bifurcation in numbers

| Segment | 2025 size | Trajectory | Economics |
|---|---|---|---|
| **Total CCL** | ~US$16.8B | → ~$24B by 2031 (~6% CAGR) | Blended; commodity-weighted |
| Commodity FR-4 (bulk) | ~$12–13B | ~5–6% CAGR | Cyclical, copper/resin spread, low-margin |
| **High-freq/high-speed CCL** | ~$4.1B | → ~$10.9B by 2035 (~10% CAGR) | Spec-in; 30–50% price premium |
| — AI-server CCL sub-slice | ~$1.5–2B (est.) | → ~$3.5B by 2031 (~20% CAGR) | Fastest slice; high-30s% incremental GM |
| Downstream PCB (for scale) | ~$96B | → ~$127B by 2031 | 40+ layer AI boards ~4× the ASP of 8-layer boards |

The market still applies a blended ~6%-CAGR commodity lens to a high-speed franchise compounding 2–3× faster at expanding margin — the durability of the *margin*, not the growth, is what is mispriced.

### Competitive matrix

| Player | Listing | Arena strength | AI / high-speed position |
|---|---|---|---|
| **Kingboard Laminates** | 0148.HK | #1 by *total volume*; fully integrated (copper foil, glass yarn/fabric, resin) | Commodity-weighted; climbing high-speed slowly; investing into e-grade glass yarn/fabric (Shixing, ~$260M) |
| **Shengyi / SYTECH** | 600183.SS | #2 by volume since 2013; state-backed; total CCL capacity → >100M m²/yr | NVIDIA-qualified (Synamic9GN), reportedly progressing to M10; the China high-end wildcard for 2027 |
| **Nan Ya Plastics** | 1303.TW | Top-3 volume (Formosa scale); also makes copper foil + glass cloth | Secondary high-speed; licensed ~20% of Nittobo specialty glass by 2027 |
| **Elite Material (EMC)** | 2383.TW | **#1 high-speed (~28% global high-speed share)**; halogen-free leader since 2013 | ~100% Meta MTIA, ~80% AWS Trainium, ~50% Google TPU, 50–60% 800G/1.6T switch; M7+ >60% of rev |
| **Panasonic (Megtron)** | 6752.JP | The **quality benchmark** (Megtron 8 Df ~0.0015), capacity-constrained, higher-cost | Premium incumbent; doubling Megtron capacity in Thailand (~$110M/5yr) |
| **TUC (Taiwan Union)** | 6274.TW | #2 Taiwan high-speed; ThunderClad 200G/400G/800G (2021) | Strong on NVIDIA GPU boards; ~1/3 EMC's scale, growing ~28% |
| **ITEQ** | 6213.TW | #3 Taiwan; high-speed + RF | TUC+ITEQ together ~18% of global high-frequency/high-speed |
| **AGC Multi Materials / Doosan / Isola / Rogers / Resonac** | various | Legacy high-performance (PTFE, RF) | Tier-2 AI exposure; strongest at the RF/switch PTFE end |

### The real leading-edge replicator set is only ~3
At M8/M8.5/M9 qualified for Western-hyperscaler ASIC + Rubin boards, only **EMC, Panasonic and TUC** genuinely compete today — far narrower than the eight-name matrix implies. Panasonic is the quality peer but capacity-constrained and higher-cost; TUC is a credible half-step behind at ~1/3 EMC's scale. **Shengyi is the most likely fourth entrant by 2027** — the state-backed, captive-China structural threat. This is the qualification-gate-monopoly pattern hidden behind tonnage share data ([[Mental Models/Industry - Semiconductors]] #2): screens that rank CCL by volume surface Kingboard/Shengyi and miss that the AI-relevant franchise is a 3-player high-speed oligopoly gated by a near-monopoly input.

### The M9 node contest: quartz breaks Nittobo's glass-chemistry gate, and the impact splits sharply across the two names
M9 (NVIDIA's internal spec: **Df ≤0.0007, Dk <3.0 at 10 GHz**; mass production **2H 2026**; mandated for the **78-layer Rubin Ultra orthogonal backplane** and 1.6T switch/backplane trays) is the first grade where the reinforcement changes *material class*, not just formulation. M8/M8.5 ran on evolved low-Dk **glass fiber** (Nittobo NE/NER, "Low Dk1/Dk2"); M9 ("Low Dk3") moves to **quartz cloth — ~99.9%-silica "Q-glass"** — a different material that bypasses the borosilicate glass-chemistry gate Nittobo's ~90% share is built on. This is [[Mental Models/Industry - Semiconductors]] #8 (architecture transition remaps the bottleneck) firing one layer below CCL.

| Attribute | Nittobo **NEZ** (evolved glass fiber) | Asahi-cohort **Q-glass** (quartz) |
|---|---|---|
| Composition | low-Dk borosilicate | **~99.9% silica (quartz)** |
| Dk @ 10 GHz | ~**4.0** | ~**3.7** |
| Df @ 10 GHz | ~0.001-class | ~**0.0005** (intrinsic quartz → ~0.0002) |
| CTE | low | ~**0.5 ppm/°C** (near-zero) |
| Cost | ~**$25–30/m** | ~**$50/m (1.7–2×)** |
| Processing | mature | **harder — drill-bit wear + residual fiber protrusion in vias → copper-plating yield risk** |

M9 CCL runs **~15–20× FR-4** (M8 ~10–15×, M7 ~6–9×); M9/Q-glass lead times are **20+ weeks, allocation-only**.

**The upstream layer does not hand off — it fragments.** Nittobo's ~90% dominance is in T-glass (substrate, Low CTE) and NER-glass (Low Dk2, M8-class); at the quartz tier it is not the franchise. Per TrendForce, "Low Dk3 (Q-glass)" is a **cohort — Asahi Kasei, Shin-Etsu (SQX), Glotech, Feilihua, Taishan Fiberglass, Hong Ho — "collectively capturing the majority share in the early stages" of M9.** Nittobo's M9 answer, NEZ, is an evolved *glass fiber* (Dk ~4.0), a structural half-step behind quartz on both loss and CTE, backstopped by a next-gen T-glass slated for 2028. The "Asahi quartz takes the early M9 majority" read is therefore directionally right but more precisely a **quartz-cohort** story — and the next node is **less monopolistic upstream**, not a monopoly changing hands.

**Nittobo (3110): existential to the leading edge, bounded elsewhere.** Quartz taking the early M9 majority fires the thesis's own **→ LOW trigger** and is the single falsifying datapoint its stress test flagged ([[Research/2026-06-26 - 3110 - Stress Test]]): the ~90% share is **node-bound**, and the qualification-gate moat ([[Mental Models/Industry - Semiconductors]] #2) does not reach a chemistry Nittobo does not lead. Damage bounds: M9 is the *smallest, newest* slice (switch-tray/backplane, not the larger M8/M8.5 compute-tray volume that stays on glass fiber); quartz's ~2× cost and harder processing keep glass fiber in cost-sensitive layers; and the T-glass substrate franchise is a *separate* contest where quartz's 0.5 ppm/°C CTE is a longer-dated second front, not an immediate one. Net: quartz caps Nittobo at the trailing-grade ceiling at the exact node that sets forward value, without erasing the M8-class + substrate base — a monopoly multiple on an oligopoly franchise, not a franchise gone.

**EMC (2383): moat-modifier, sign ambiguous-to-negative — and more contested than "it just changes our supplier."** Three effects, not one. (1) **Allocation-moat erosion** — EMC's Insight-#3 edge (scarce *Nittobo* glass allocated to the largest qualified buyer, starving sub-scale rivals) weakens, because the quartz cohort adds *new* qualified suppliers who can feed EMC's competitors; the chokepoint that entrenched EMC dissolves into a 6-supplier quartz field. (2) **Supply-diversification upside** — EMC grows less hostage to Nittobo's 40–55% price hikes. (3) **The negative the vault missed: a material-class change resets CCL qualification, and EMC is not clearly ahead at M9.** Halogen-free *resin* IP does not confer *quartz-lamination* mastery (a different drilling/plating yield problem). Per Digitimes (Nov 2025), **Doosan (DS-7409 M9Q) emerged as the early M9-quartz volume leader and is "poised to secure exclusive Nvidia Rubin CCL supply as EMC failed a GB300 test,"** with EMC pushing **EM-896K3** to close the gap and Shengyi developing equivalents. This updates the replicator set above for the M9 sub-node: the "EMC/Panasonic/TUC-only" leading edge gains **Doosan as the early M9 front-runner**, and EMC's incumbency is not a given. Hold as a hypothesis to test — single channel-check source, and Goldman's Sept-2025 check had EMC "benefiting most" on Rubin; the contradiction is itself the signal that the M9 socket is live, not settled.

**Cross-thesis synthesis (value-layer-monopoly lens).** The M9/quartz transition is adverse for *both halves of the toll road at once*: upstream the rent **disperses** (fragmented quartz cohort vs Nittobo's clean glass monopoly); downstream the CCL leadership **reshuffles** (Doosan up, EMC contested). The node the bull case prices as more content-per-board (true) is also **less monopolistic at the layer that mattered** — the toll booth relocates from Nittobo's loom to a contested quartz field, and neither incumbent automatically collects it. Falsifiable signals: M9 design-win splits (Nittobo NEZ vs quartz cohort) as 224G qualifies through 2026–27; EMC EM-896K3 qualification on Rubin switch trays; confirmation or reversal of Doosan's Rubin exclusivity; and whether quartz's cost/yield penalty caps it at the switch-tray niche while M8/M8.5 glass-fiber volume (and Nittobo's allocation moat) holds through 2027.

### Anchor-customer concentration is a survival test, not a footnote
EMC's ~100% share on Meta MTIA, ~80% on AWS Trainium and 50–60% on 1.6T switch fabric is the qualification-gate moat *and* the binary risk ([[Mental Models/Industry - Semiconductors]] #10): a 6–18-month qualification locks the socket for the product's life, but the loss of a single flagship socket (MTIA, Trainium) to Shengyi at M8 would be the confirmation the moat broke at the leading edge — the CLOSE trigger in the EMC thesis. Concentration cuts both ways: it locks sockets in but hands large customers leverage on price in a soft demand window.

### Capacity roadmap — the synchronized 2027 vintage

| Player | Expansion | Timing | Note |
|---|---|---|---|
| **EMC** | → 9.45M sheets/month (Taiwan + China + Malaysia); Guanyin NT$12.4B + Taoyuan high-end build | Peak ramp 2027 | The volume + breadth leader |
| **Panasonic** | Doubling Megtron capacity, Thailand (~$110M/5yr) | 2026–2027 | Quality benchmark, deliberately paced |
| **Shengyi** | Multi-site; total CCL → >100M m²/yr; high-frequency ramping since 1H 2025 | 2026–2027 | State-backed; the ROIC-insensitive marginal supplier |
| **TUC / ITEQ / Nan Ya** | All adding high-end lines | 2026–2027 | Bunched by ~2yr equipment lead |
| **Equipment (vacuum press + treater)** | Orders booked through 2028; ~2-year delivery | — | The pacing constraint *and* a 2027 oversupply trigger |

Everyone is building high-end lines at once, and the ~2-year equipment lead synchronizes the start-ups into a single **2027 vintage** — the first real read on whether the high-end specialty premium survives capacity catching demand. This is the classic semi capital-cycle setup: a delayed, equipment-gated supply response calibrated to inflated shortage prices, where the down-leg risk is sharpest precisely when the build lands into the first plausible AI digestion ([[Mental Models/Industry - Semiconductors]] #3, #17).

### Pricing-power trajectory and the price-hike decomposition
High-end is de-commoditizing — margin *expanding* into the build (EMC GM 30.1%, +3.1pp YoY) while 20–40% price hikes stick — versus commodity FR-4 reverting to spread economics in any downturn. The hikes are mostly genuine pricing power, not glass pass-through: glass is only ~15–20% of high-end material cost, so a +20–30% Nittobo hike is ~3–6% of COGS, leaving the bulk of a 20–40% price increase as margin capture. Pure pass-through never expands margin; margin expansion through rising input costs is the tell. The honest caveat: part of the capture is cyclical shortage-rent (allocation power while inputs are sold out) versus structural spec-in pricing — and that split is the entire durability question into the 2027 vintage.

### The ROIC bifurcation (the sector's central tension)
Incremental high-end capacity earns >25–30% ROIC today in a sold-out market — which is *why* everyone builds. To 2030 it splits: the disciplined leaders (EMC, Panasonic) defend a premium-ROIC core, but the *industry marginal* ROIC is set by the least-disciplined entrant. **State-backed Chinese capacity (Shengyi) is structurally ROIC-insensitive** — it adds high-end lines for sovereignty reasons even below cost of capital — and that is the mechanism that compresses high-end ASP and turns a high-ROIC specialty into a mid-ROIC cyclical if AI demand decelerates as the 2027 vintage lands. The gap between EMC's *defended* ROIC and the *compressing industry marginal* ROIC is the MEDIUM-versus-HIGH conviction question for the whole sector.

### Process-moat depth, calibrated
CCL's process moat is real but ~1–2 orders of magnitude shallower than a leading-edge foundry or memory maker (capex ~$0.5B/line vs $15–30B/fab; ~7–10 process steps vs hundreds-to-1,500; 5–6 rivals vs 2–3). Durability rests on a re-compounding *stack* — materials-IP + per-node qualification + first-mover + scarce-input allocation — not irreproducible process physics. The calibration the whole sector hangs on: **wider than "commodity laminate," narrower than "TSMC-grade monopoly."** It classifies as a *semi-cyclical compounder*, not a structural compounder ([[Mental Models/Industry - Semiconductors]] #13) — the qualification gate keeps the down-cycle margin shallower than the FR-4 template, but the 5–6-player oligopoly and ROIC-insensitive marginal supplier prevent the monopoly economics the bulls imply.

### The value chain and where margin pools sit

| Layer | Key players | Pricing power | AI rent capture |
|---|---|---|---|
| **Raw batch** (silica sand, boron, electrolytic copper, petrochemical resin precursors) | Commodity miners/chemicals | None | None |
| **Low-Dk glass cloth** | **Nittobo (~90% T-glass)**, Asahi Kasei (quartz), Taiwan Glass, Nan Ya | **Highest** — sole-source at top grade | Deepest monopoly; smallest market (~$4B) |
| **HVLP copper foil** | Mitsui Mining & Smelting (#1), JX Nippon, Furukawa, ILJIN, Circuit Foil, Chang Chun, Nan Ya | High — sold out, 3-yr shortfall | Scarce-input rent; vertical integrators (Chang Chun, Nan Ya) capture both layers |
| **Low-loss resin** (PPE/PPO oligomer, BMI, hydrocarbon, PTFE) | SABIC (NORYL SA9000), Asahi Kasei, Mitsubishi Chemical | High at PPE oligomer | The chemistry IP layer; tight, expanding capacity |
| **CCL / prepreg** | **EMC, Panasonic, TUC, ITEQ, Shengyi, Kingboard, Nan Ya** | High at high-speed; low at FR-4 | The spec-in toll road; ~30–40% of board BOM |
| **PCB fabrication** | **Zhen Ding (#1), Unimicron, Victory Giant, Tripod, Compeq, WUS, Shennan, AT&S, Meiko** | Medium — assembly margin, capex-heavy | Captures board-build margin; 40+ layer ASP ~4× standard |
| **ODM / system** | Foxconn/Hon Hai, Quanta, Wistron/Wiwynn | Low — pass-through assemblers | Volume, thin margin |
| **End customer** | NVIDIA + hyperscalers (Meta, AWS, Google, Microsoft) | Sets the spec; pays the bill | Funds the whole chain via AI capex |

The structural read: **pricing power concentrates at the two most-upstream scarce-input layers (glass, foil) and at the spec-in CCL layer — and is inversely proportional to position size in the market.** The deepest monopoly (Nittobo, ~$4.2B mcap) is the smallest and least-owned; the most-owned names sit downstream where the moat is shallower. Own the *stack*, not a single layer ([[Mental Models/Industry - Semiconductors]] #1, #2).

## Product level analysis

### The M-grade loss ladder
"M-grade" (M4→M6→M7→M8→M8.5→M9, now M10) is a loss classification anchored to Panasonic's Megtron generations and used as an industry-wide shorthand. Each step lowers the **dissipation factor (Df / loss tangent)** at the relevant Nyquist frequency; **Dk (dielectric constant)** sets impedance and signal velocity, Df sets insertion loss per inch. The grade required is driven by **SerDes data rate × layer count × board size** — all three compounding the loss budget at once. (Df is frequency-dependent; values below are approximate vendor-equivalent tiers, not a single spec.)

| Grade tier | Approx. Df | SerDes era | Frequency (Nyquist) | Application | Volume era |
|---|---|---|---|---|---|
| FR-4 (standard) | ~0.02 | ≤10G NRZ | low | Consumer/server commodity | Legacy |
| M4 (Megtron 4-class) | ~0.005 | 25–56G | ~14 GHz | Mid-loss networking | 2015–2020 |
| M6 (Megtron 6-class) | ~0.002–0.004 | 56–112G entry | ~28 GHz | High-speed server/switch | 2019–2023 |
| **M7** | ~0.0015–0.002 | **112G PAM4** | ~28 GHz | **NVIDIA GB300 (28–34 layers)** | 2024–2026 |
| **M8 / M8.5** | **~0.0015** | **112G→224G** | ~28–56 GHz | GPU/ASIC boards, 1.6T switch | 2025–2027 |
| **M9 / M10** | ~0.001 and below | **224G PAM4 / 448G** | ~56 GHz+ | **Rubin, next-gen switch** | 2026–2028 |

Concrete product datapoints: EMC's EM-S532K cuts Df to ~0.0037 at 80 GHz (vs EM-S526's 0.0081) — a >35% insertion-loss reduction; Panasonic Megtron 8 is Df ~0.0015. M7-and-above is already >60% of EMC revenue and rising. Shengyi's reported NVIDIA M10 progression shows the China cohort chasing the very top of the ladder.

### Three materials levers set the composite loss (ascending difficulty to replicate)
1. **Resin system — the core IP.** Low-loss thermoset chemistry: modified hydrocarbon, **PPE/PPO** (polyphenylene-ether — SABIC NORYL SA9000 oligomer is the merchant flagship; Asahi Kasei, Mitsubishi Chemical expanding, new grades Tg >230°C / Df <0.0018), BMI blends, and **PTFE** at the highest-frequency RF/switch end (e.g., PTFE-based CCL in NVIDIA GB300). Halogen-free (EMC since 2013) is materially harder than the halogenated shortcut. This is where EMC's edge concentrates and the hardest layer to reverse-engineer.
2. **Low-Dk/Df glass cloth — the binding bottleneck.** Supplied by [[Theses/3110 - Nitto Boseki]] (~90% T-glass, ~60–70% NER-glass); a flat/spread weave suppresses the "glass-weave skew" that corrupts impedance. CCL makers are *allocated* this, not vertically integrated into it (except partly Kingboard/Nan Ya). At M9 ("Low Dk3") the reinforcement changes material class to **quartz "Q-glass" (~99.9% silica)**, supplied by a cohort (Asahi Kasei, Shin-Etsu, Glotech, Feilihua et al.) taking the **early M9 majority** and bypassing Nittobo's glass-chemistry gate — see §Competitive dynamics → *The M9 node contest* for the spec/cost gap and the asymmetric impact on Nittobo vs EMC.
3. **Ultra-low-profile copper foil — the second squeeze.** At 112G/224G, conductor loss dominates as skin effect crowds current into the rough foil surface; **HVLP (hyper-very-low-profile)** foil cuts that loss. HVLP4 is the new mainstream for the most advanced AI boards. Top-5 (Mitsui Mining & Smelting, JX Nippon, Furukawa, ILJIN, Circuit Foil) hold ~58% of HVLP capacity; Chang Chun and Nan Ya vertically integrate foil + laminate. Goldman frames a 3-year HVLP shortfall as the "new normal" — a second allocation moat layered on the glass one.

### Manufacturing flow (~7–10 stages)
Varnish compounding (the Dk/Df IP step — resin, curing agents, accelerators, halogen-free flame retardants, silica fillers blended into solvent varnish) → impregnation/B-stage treating of glass cloth into prepreg (resin-content + cure uniformity across a wide web = the #1 high-grade yield lever) → lay-up of copper-foil + prepreg plies → vacuum lamination/C-stage cure (void-free flow, thickness/Dk uniformity, low warpage, copper-peel adhesion; difficulty rises steeply with 28–34 layers and panel size) → post-cure, trim, QC (Dk/Df, peel strength, Tg/Td, thermal-reliability test). The greenfield build is gated by equipment (large vacuum presses + treater lines, ~2-yr lead); the high-grade *yield* is gated by varnish formulation, treating uniformity and void-free lamination — which is why commodity-to-high-grade brownfield conversion is "a relief valve that bleeds, not a switch that flips" (input- and qualification-gated, not footprint-gated). See [[Theses/2383 - Elite Material]] for the step-by-step process-moat decomposition vs TSMC/SK Hynix, and [[Sectors/Semiconductor Capital Equipment]] for the press/treater equipment layer.

### End applications and content-per-board economics
End applications: GPU/ASIC baseboards, HGX/UBB carriers, midplane/backplane systems, 1.6T network switch trays, NIC cards. M7 is spec'd into NVIDIA GB300 (28–34 layers); M8/M8.5/M9 are the spec target for Rubin and 1.6T switching. The content-per-board tailwind compounds on **three axes at once** — board count × layer count × material grade ($/layer). A 112 Gbps-per-lane platform requires 40+ layer backplanes carrying ~4× the ASP of an 8-layer board, and CCL is ~30–40% of that board's bill of materials. EMC's CCL revenue per AI rack therefore grows even if accelerator *units* decelerate — the content-escalation tailwind is largely independent of the unit-growth S-curve everyone watches.

## Acquisitions and new entrants

### Western roll-up into Asia (high-end consolidation)
- **AGC (Japan)** acquired Park Electrochemical's Nelco business (2018, ~$150M; closed 2019) and **Taconic** (2019), combining them into **AGC Multi Materials** for next-gen high-speed CCL. Park exited electronics entirely (now Park Aerospace).
- **Doosan** absorbed Kolon Electronics (1998) → Doosan Electro-Materials (high-end laminate, RF).

### China vertical integration climbing the stack
- **Shengyi (China)** — the most credible new high-end entrant: NVIDIA-qualified ultra-low-loss CCL, reportedly progressing to M10, state-backed localization, captive China AI-server demand, total CCL capacity heading >100M m²/yr. The 2027 Western-hyperscaler M8 question is the sector's key competitive swing.
- **Kingboard (China)** — pushing vertical integration *upstream*: a ~RMB2B (~$260M) Shixing investment in electronic-grade fiberglass fabric + electronic yarn (onstream mid-2026, ~RMB1.05B/yr output), extending its owned-input base (copper foil, resin) into the glass layer to attack the one input it does not control.

### Upstream entrants matter more than downstream ones
- **Glass cloth:** Nittobo is licensing ~20% of its specialty glass-fiber volume to **Nan Ya** by 2027 (capacity relief without ceding IP); **Asahi Kasei** (Digitimes, Apr 2026) is entering with *quartz* "Q-glass" to challenge Nittobo's 90%, leading a quartz cohort (Shin-Etsu, Glotech, Feilihua, Taishan, Hong Ho) taking the **early M9 majority**; downstream at the CCL layer, **Doosan's DS-7409 M9Q** has emerged as the early M9-quartz volume leader (reportedly poised for exclusive Rubin CCL after EMC stumbled a GB300 test). **Taiwan Glass** and **Fulltech** are qualifying lower-grade volume. (Full analysis: §Competitive dynamics → *The M9 node contest*; [[Theses/3110 - Nitto Boseki]].)
- **Copper foil:** **Co-Tech** (Taiwan) is halting standard foil to double down on AI/5G HVLP specialty — emblematic of the commodity-to-specialty pivot across the foil layer as the 3-year shortfall pulls capacity toward the high end.

### The PCB-fabricator layer is consolidating around AI
The customer one layer downstream from CCL is itself re-ranking fast: **Victory Giant** (Huizhou) surged from 1.7% to **13.8% of global AI/HPC PCB revenue** in a single year as a direct NVIDIA supplier (RMB19.3B / ~$2.8B 2025 revenue, +70% forecast 2026, HK$20.1B IPO — the largest in Hong Kong in 2026; early mass production of 24-layer 6th-gen HDI). **Zhen Ding** (#1 PCB) is steering toward ~70% AI revenue with NT$100B of two-year capex; **Unimicron** holds ~18–22% of AI-server PCB and >50% of certain ASIC substrates; **WUS** and **Shennan Circuits** are gaining HPC share. This matters to the CCL thesis two ways: it concentrates EMC's demand into a handful of qualified, scaling fabricators (locking sockets but adding customer leverage), and the fabricators' own margin capture is the competing claim on the AI-PCB value pool.

## Macro shifts

- **AI board-complexity escalation** — content-per-board compounds on three axes (board count × layer count × material grade); CCL revenue per AI rack grows even if accelerator *units* decelerate. The cleanest content-escalation tailwind in the AI hardware stack, and largely orthogonal to the unit-growth S-curve.
- **The SerDes data-rate ladder** (112G/~28GHz → 224G/~56GHz → 448G) drives the grade ladder (M7→M9→M10→beyond) on a roughly per-generation cadence; material that was leading-edge two years ago is mid-tier today. This is the architecture transition that keeps re-locating the bottleneck and re-compounding the leaders' qualification lead ([[Mental Models/Industry - Semiconductors]] #8).
- **Custom-silicon ASIC migration** — the high-speed CCL leaders are the toll road paid whether NVIDIA *or* hyperscaler ASICs win (EMC dominant on Meta MTIA / AWS Trainium / Google TPU). A rare hedge against the most-debated question in the AI trade. Cross-reference [[Sectors/Custom Silicon & Networking Semiconductors]], [[Sectors/Compute & AI Compute Accelerators]].
- **Triple upstream input bottleneck** — (1) Nittobo low-Dk glass cloth (~90% T-glass, sold out through end-2026, capacity mid-2027 earliest); (2) HVLP copper foil (Goldman's "new normal" 3-year shortfall); (3) PPE/PPO resin (tight, expanding). Each is a Japan/Taiwan oligopoly, each is the leaders' allocation moat *and* a cost risk if pass-through stalls.
- **Architecture-substitution risk** — glass-core substrates ([[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]]), CPO/optical interconnect ([[Sectors/Optical Networking & Photonics]]) and panel-level packaging could each plateau PCB layer count and per-board CCL content at the leading edge (2027–2030+). Glass-core hits the *substrate* layer above CCL first; CPO moves some 224G electrical routing onto optics inside the rack — the long-dated bear vector on content escalation.
- **China localization / geopolitical bifurcation** — state-backed Chinese CCL is the ROIC-insensitive supply that anchors high-end price down; a captive China AI-server market (Chinese AI chips ~41% of local AI-server shipments in 2025) walls off TAM into a parallel market with independent supply/demand ([[Mental Models/Industry - Semiconductors]] #16). Shengyi + Victory Giant + Kingboard are building a vertically-integrated domestic stack from glass to board.
- **The synchronized 2027 capacity vintage** — equipment lead times (~2 years on vacuum presses + treater lines, booked through 2028) bunch the industry's adds into one wave; 2027 is the first read on high-end oversupply / ASP direction. The single most important dated catalyst for the sector.
- **Where on the S-curve** — high-speed AI CCL sits *mid-chasm*: the S-curve is secured (every AI board needs it) but timing and margin durability are uncertain — the highest-edge zone for long-term capital, and the zone where the cycle-vs-structural decomposition matters most ([[Mental Models/Generalist - Overview]] #4, [[Mental Models/Industry - Semiconductors]] #18). The error to avoid is reading the 2024–2026 margin expansion as either pure cycle (it has a structural spec-in component) or pure structure (it has a real shortage-rent component).

## Investor heuristics

### Current consensus and what is priced in
Consensus still half-prices CCL as a cyclical commodity laminate (the FR-4 / copper-spread frame) despite the high-end de-commoditizing. The growth is seen; the *durability of the high-end margin* through the 2027 vintage is not — that is the mispricing. The high-speed leaders are crowded longs (EMC sell-side 14 buy / 0 sell), so the marginal-bull risk sits downstream at the most-owned names; the upstream monopoly (Nittobo) is more balanced (Goldman Neutral) and far less owned.

### The screen traps
- **Volume leadership ≠ quality leadership.** Tonnage screens surface Kingboard/Shengyi; the AI-relevant franchise is the Taiwan/Japan high-speed cluster (EMC, Panasonic, TUC) and the upstream glass monopoly (Nittobo).
- **Trailing P/E is a mirage at the upstream names.** Nittobo's trailing ~16x is inflated by one-off asset-sale gains; the clean number is ~35x forward — diligence the recurring margin, not the headline.
- **"AI server units" undercounts CCL.** Content-per-board escalation (layer × grade × board count) grows CCL revenue independent of unit growth; unit-pegged models understate the franchise.

### Own the toll-road stack, not a single layer
The most-upstream chokepoint (Nittobo glass, ~90% share, ~$4.2B mcap) is far smaller than its downstream customer (EMC, ~28% high-speed share, ~$57B) — the deepest monopoly is the least-owned. Pricing power is inversely proportional to market-cap position in this chain. The two are an upstream/downstream pair on one toll road; the foil layer (Mitsui et al.) is a third, even-less-owned scarce-input rent.

### Cross-vault attractiveness assessment
Ranking the investable layers by moat depth × under-ownership × AI-rent capture:

| Name | Layer | Moat | Setup | Vault status |
|---|---|---|---|---|
| **Nittobo (3110.JP)** | Glass cloth | Deepest (~90% T-glass, sole-source) | Most under-owned ($4.2B); node risk (Asahi quartz at M9) | **Thesis, draft MEDIUM** |
| **EMC (2383.TW)** | High-speed CCL | Strong (#1, ~28%, anchor sockets) | Crowded (+542% LTM, ~47x fwd); 2027-vintage risk | **Thesis, draft MEDIUM** |
| Panasonic (6752.JP) | CCL (Megtron) | Quality benchmark | Buried in a conglomerate; capacity-constrained | Watchlist |
| Mitsui M&S (5706.JP) | HVLP foil | High (#1 foil, sold out) | Under-discussed; 3-yr shortfall | Watchlist — `/thesis` candidate |
| Shengyi (600183.SS) | CCL (China) | Rising; state-backed | The bear's instrument (ROIC-insensitive marginal) | Monitor (competitive swing) |
| Victory Giant / Zhen Ding | PCB fab | Medium (assembly margin) | Victory Giant +70% rev '26; concentration risk | Watchlist — value-pool claim |

The cleanest structural play is the *least-owned upstream monopoly* (Nittobo); the highest-quality downstream franchise (EMC) is correctly identified but richly priced into a synchronized build. The HVLP foil layer (Mitsui) is the under-covered third scarce input worth a `/thesis`.

### Non-consensus reads
1. **Margin durability through the 2027 vintage** is the debate, not growth — and it decomposes into shortage-rent (fades) + structural spec-in (persists); the split is the call.
2. **The upstream input bottleneck is a moat-widener, not just a cost headwind** — scarce glass/foil/resin is allocated to the largest qualified buyers, starving sub-scale rivals of inputs they cannot qualify around inside two years.
3. **The ROIC bifurcation** — a defended-leader premium ROIC vs an ROIC-insensitive state-backed marginal supplier — is what converts (or doesn't) a high-ROIC specialty into a mid-ROIC cyclical.
4. **The moat is materials-IP + qualification + first-mover + scarce-input allocation** — wider than commodity, narrower than monopoly — which is why the high-speed names warrant MEDIUM, not HIGH, conviction into a synchronized capacity build, and classify as semi-cyclical compounders rather than structural compounders ([[Mental Models/Industry - Semiconductors]] #13).
5. **Value pools at the scarce-input layers** (glass > foil > resin) more durably than at CCL or PCB fab — and those layers are the least-owned in the vault.

## Mental Models
<!-- Outputs from applying the /Mental Models context files to this sector. Per the READING PROTOCOL in [[Generalist - Overview]], these are lenses and questions, never conclusions — every entry is a hypothesis to test against the sector evidence above, not a verdict. Populated incrementally: each research pass appends the models it applied and the specific triggers that fired. -->
- **Models applied**: [[Mental Models/Generalist - Overview]] (always) · [[Mental Models/Industry - Semiconductors]] · [[Mental Models/Lens - Value Layer Monopoly]] *(first-populated 2026-06-27 from the M9-quartz deepen; scoped to that research — a fuller sector pass remains for /sync or /surface)*
- **Triggers that fired** *(each a hypothesis to test, not a verdict)*:
  - **Industry-Semis #8 · architecture transition remaps the bottleneck** — M9's shift from low-Dk *glass fiber* to *quartz* ("Low Dk3") relocates the reinforcement bottleneck off Nittobo's glass-chemistry gate onto a fragmented quartz cohort. *Test:* Nittobo NEZ vs quartz M9 design-win splits as 224G qualifies 2026–27.
  - **Value Layer Monopoly §2 · falling switching costs / commoditizing layer** — the upstream rent *disperses* at M9 (≥6-supplier quartz field) instead of handing off as a clean monopoly; the toll booth relocates rather than changing owner. *Test:* does any single quartz supplier consolidate M9, or does it stay fragmented (rent competed away)?
  - **Industry-Semis #2/#13 · qualification-gate node-boundedness + classification** — a material-class change resets qualification at the CCL layer too (Doosan DS-7409 M9Q early lead; EMC GB300 stumble), so both upstream and downstream leadership read node-bound, not structural — reinforcing the sector's semi-cyclical classification over a structural-compounder multiple. *Test:* EMC EM-896K3 vs Doosan M9Q on Rubin switch trays.
  - **Generalist · base rate / single falsifying datapoint** — quartz taking the early M9 majority is the datapoint that breaks "Nittobo's 90% extends to the next node"; the outside view (specialty premia compress as capacity catches demand; monopolies are node-specific) beats the trend-continuation bull on a +244% / +542% LTM pair. *Test:* M9 ASP + share direction through 2027.
- **Disconfirming check**: The cross-model read agrees — both halves of the toll road weaken at M9 (upstream rent disperses, downstream leadership reshuffles). Per the READING PROTOCOL, agreement is the trigger to disconfirm: the bear's own falsifiable hole is that quartz's ~2× cost + harder processing (drill-bit wear, plating-yield risk) caps it at the switch-tray/backplane niche, leaving the larger M8/M8.5 glass-fiber volume — and Nittobo's allocation moat — intact through 2027. The node contest is real but may be *smaller than the multiple implies in either direction*. (Per [[Research/2026-06-27 - M9 Quartz vs Low-Dk Glass - deep-dive]].)

## Related Research

- Theses (sector): [[Theses/2383 - Elite Material]], [[Theses/3110 - Nitto Boseki]]
- Research (M9 node contest, 2026-06): [[Research/2026-06-27 - M9 Quartz vs Low-Dk Glass - deep-dive]], [[Research/2026-06-26 - 3110 - Stress Test]], [[Research/2026-06-27 - 2383 - Stress Test]]
- Adjacent layer (above): [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]], materials-monopoly analog [[Theses/2802 - Ajinomoto]]
- Adjacent demand sectors: [[Sectors/Custom Silicon & Networking Semiconductors]], [[Sectors/Optical Networking & Photonics]], [[Sectors/Compute & AI Compute Accelerators]]
- Equipment layer: [[Sectors/Semiconductor Capital Equipment]] (vacuum presses + treater lines)
- Macro: [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]] (substitution vector), [[Macro & Technology/AI Bubble Risk and Semiconductor Valuations]] (demand overlay)
- Demand-driver theses: [[Theses/NVDA - Nvidia]], [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell Technology]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/TSM - Taiwan Semiconductor]]
- Mental models: [[Mental Models/Industry - Semiconductors]] (#1 bottlenecks/pricing power, #2 qualification-gate monopolies, #3/#6/#17 capital cycle, #8 architecture transitions, #10 anchor customers, #13 classification, #16 geopolitical bifurcation, #18 cycle-vs-structural), [[Mental Models/Generalist - Overview]] (#4 S-curves, #9 ROIC)

## Legacy Callouts
<!-- Auto-managed by /archive-callouts. Addressed callouts older than the sweep threshold (default 180 days) are moved here from their original sections as plain bulleted entries: `- **<addressed-date>** · <type> · <section> · raised <fresh-date> → <body>` with a `**Response:**` sub-bullet. Sorted descending (newest first). Do NOT hand-edit. To exempt a callout from sweeping, add `[[pinned]]` to its header in-place. -->

## Log
### 2026-06-10
- Sector note created by /thesis 2383 — first thesis in this sector. Scaffold-only; analytical content to be added via /deepen or /surface.
- Sector MOC built out (all 10 sections authored). Synthesized from [[Theses/2383 - Elite Material]] (5 callout-round depth: engineering moat, price-hike decomposition, manufacturing, process-moat-vs-TSMC/SK-Hynix, supply-ramp/ROIC), [[Theses/3110 - Nitto Boseki]] (upstream glass), [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]], plus web research (market sizing, industry history, M&A trail, China rise). Core frame: CCL bifurcated into commodity FR-4 (China-volume) vs high-speed/AI (Taiwan/Japan-quality + Nittobo-glass-gated). status draft→active. Both theses draft — promote via `/status` to formalize Active Theses.
- Substantial enhancement (manual + web research). Roughly doubled note depth with: market-sizing table (total CCL ~$16.8B / high-speed ~$4.1B→$10.9B by 2035 / AI sub-slice ~20% CAGR; specialty 30–50% premium); full **value-chain map with margin pools** across 4 input layers → CCL → PCB fab → ODM → hyperscaler; named the **copper-foil** layer (Mitsui M&S #1, JX/Furukawa/ILJIN/Circuit Foil — top-5 ~58% HVLP; Goldman 3-yr shortfall) and **resin** layer (SABIC NORYL SA9000 PPE oligomer, Asahi Kasei, Mitsubishi Chemical) the theses omitted; M-grade ladder table (Df/Dk × SerDes era, M4→M10); capacity roadmap table (EMC 9.45M sheets/mo, Shengyi >100M m²/yr, equipment booked through 2028); expanded industry history (FR-4/NEMA origin, 3-wave migration, halogen-free, Western roll-up); PCB-fabricator consolidation (Victory Giant 1.7%→13.8% AI/HPC share, Zhen Ding, Unimicron). Wove in [[Mental Models/Industry - Semiconductors]] #1/#2/#3/#6/#8/#10/#13/#16/#18 + [[Mental Models/Generalist - Overview]] #4/#9 explicitly. Added watchlist names (Mitsui foil, Victory Giant PCB) + cross-vault attractiveness ranking. New external sources: Mordor/FMI/Strategic Market Research (sizing), Digitimes/futunn (capacity, equipment lead), Taiwan News/DataIntelo (HVLP foil), SABIC/Indian Chemical News (resin), Bamboo Works/UGPCB (China CCL), The Edge/MLQ (Victory Giant). No conviction/status changes; both theses remain draft MEDIUM. TODO: run `/graph last` to register the sector's adjacencies (not yet in _graph.md, last rebuilt 2026-06-05).

### 2026-06-27
- Deepened Competitive dynamics — new subsection *The M9 node contest* (+ consistency edits to §Product level analysis lever #2 and §Acquisitions glass-cloth bullet). M9 ("Low Dk3") shifts reinforcement to **quartz** (Asahi-led cohort — Shin-Etsu/Glotech/Feilihua/Taishan/Hong Ho — taking the early majority per TrendForce; Q-glass Dk 3.7 / Df 0.0005 / CTE 0.5ppm vs Nittobo NEZ Dk 4.0, but ~2× cost + harder drilling/plating), bypassing Nittobo's glass-chemistry gate. **Asymmetric impact**: existential to Nittobo's leading-edge franchise (fires its →LOW trigger; ~90% share is T-glass/NER, node-bound at quartz) yet bounded (M9 = smallest/newest slice; M8 + substrate base intact); for EMC a moat-modifier, ambiguous-to-negative (allocation-moat erosion + supply-diversification upside, but EMC's own M9 lead is contested — Doosan DS-7409 M9Q early volume leader, EMC reportedly failed a GB300 test, Digitimes Nov-2025). Cross-thesis: both halves of the toll road weaken at M9 (upstream rent disperses, downstream leadership reshuffles). Conviction not changed here (sector note; thesis conviction is a /status call) — evidence net-negative for both names at the leading edge. Mental Models first-populated (Semis #8/#2/#13, Value Layer Monopoly §2, Generalist base-rate). Supporting research: [[Research/2026-06-27 - M9 Quartz vs Low-Dk Glass - deep-dive]]. Snapshot: [[_Archive/Snapshots/Copper-Clad Laminate & PCB Materials (pre-deepen 2026-06-27-173257)]]. TODO: `/sync` to propagate to [[Theses/3110 - Nitto Boseki]] + [[Theses/2383 - Elite Material]]; `/graph last` to register the new research note.
- [[Research/2026-06-27 - M9 Quartz vs Low-Dk Glass - deep-dive]] (/sync 2026-06-27): propagated the M9-quartz analysis to [[Theses/3110 - Nitto Boseki]] (→LOW trigger substantially confirmed, bounded — conviction weakened) + [[Theses/2383 - Elite Material]] (allocation-moat erosion + M9 lead contested by Doosan DS-7409 M9Q — conviction weakened). §Competitive dynamics already carried this (deepen, above) — no analytical re-edit; linked 3110/2383 stress tests + M9 deep-dive in Related Research. AEHR stress-test + AI-Bubble macro deferred (unrelated backlog); watermark not advanced.
