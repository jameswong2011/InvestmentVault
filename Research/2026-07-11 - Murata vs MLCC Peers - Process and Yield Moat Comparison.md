---
date: 2026-07-11
tags: [research, comparison, mlcc, semiconductors, passives, 6981, 009150, 6762, 6976, 2327]
sector: MLCC & Power Semiconductors
source: vault synthesis + web research 2026-07-11
source_type: comparison
propagated_to: [6981]
---

# Murata vs MLCC Peers — Process, Cost & Yield Moat: Magnitude and Attribution

*Focus question: the process-manufacturing / cost / yield moat in MLCCs between [[Theses/6981 - Murata Manufacturing|Murata]] and its primary competitors — the magnitude of the edge, if any, and what it is ascribed to. Peer set (user-confirmed full 3-tier map): Samsung Electro-Mechanics (009150.KS), TDK (6762.T), Taiyo Yuden (6976.T), Yageo (2327.TT), and the Chinese/Taiwanese commodity cohort (Sunlord 002138 / Fenghua 000636 / Chaozhou Three-Circle 300408 / Walsin 2492). All peers web-supplemented — no vault thesis notes. Mental-models lenses applied per CLAUDE.md gate ([[Generalist - Overview]], [[Industry - Semiconductors]], [[Lens - Value Layer Monopoly]], [[Lens - Automation & AI Readiness]]) — held as hypotheses to test, not verdicts.*

## Thesis Delta
The moat is real but it is a **gradient that inverts by tier and is thinnest exactly where demand grows fastest** — a sharper framing than the Murata thesis's flat "makes the part nobody else can." Against the Chinese cohort at the 008004 frontier the edge is huge and structurally capped-open (7–10yr, yield >95% vs 70–85% *and not in volume*); against Samsung Electro-Mechanics (SEMCO) it is only a **5–10pp 008004 yield gap that is narrowing**, and in the AI-server MLCC segment specifically SEMCO already holds ~40% vs Murata ~45%. The "unassailable moat" is unassailable *vs China*; *vs SEMCO at the growth frontier* it is a lead, not a monopoly. No conviction trigger breached → conviction unchanged (high), but the comparison adds two watch-items the thesis under-weights: (1) SEMCO closing the yield gap via captive demand + Chinese merchant powder (Sinocera now in SEMCO's and Yageo's supply chains) + a MLCC+FC-BGA-substrate+silicon-cap bundle Murata cannot mirror; (2) the apparent edge is being inflated by the 2026–27 shortage (units↑ + prices↑). Corroborating external read: Morningstar upgraded Murata's economic moat to **Wide** (MLCC advantage "expands") and Citi to **Buy** in 2026 — the moat-widening view is now partly consensus, which by the READING PROTOCOL is the cue to hunt the disconfirming datapoint (below).

## Summary
MLCC competitive advantage collapses to a **single engineering variable — dielectric layer thickness × layer count × powder particle size** — and every cost, quality, and yield difference cascades from it. Murata and SEMCO ship 0.3–0.5 µm dielectric layers stacked 600–1,000+ high from sub-100 nm barium-titanate powder; the Chinese cohort ships 1–3 µm layers a few hundred high from 150–300 nm powder. That one gap sets a **cost inversion**: China is genuinely cheaper (15–25%) at commodity 0402/0603 where yields are ~90% for everyone, but the advantage *reverses* at 008004 because a 70–85%-yield challenger scrapping 15–30% of output has a higher effective cost per *qualified* part (~35% penalty) than Murata's >95%-yield line — before AEC-Q200 even enters. Murata's magnitude of edge is therefore not one number: it is **largest and most durable vs the Chinese cohort** (a moving 3–4yr-reset frontier they are asymptotic against), **moderate and orthogonal vs TDK and Taiyo Yuden** (premium-capable but sub-scale at 008004, or specialised on a different axis — auto-grade high-temp/high-voltage), and **smallest and narrowing vs SEMCO**, the only genuine second frontier producer. Attribution: four compounding edges — (1) yield at the smallest case sizes (the binding cost lever), (2) in-field DPM <0.1 vs 1–10 (compounds catastrophically at 440k-MLCC rack part counts), (3) a non-transferable AEC-Q200 platform installed base, (4) 80-year trade-secret dielectric/sintering chemistry that is un-copyable by reading patents — all anchored by 100%-in-house sub-100 nm powder that no peer fully matches (SEMCO and Yageo increasingly buy Chinese/merchant powder). The critical caveat the bull case must hold at arm's length: the moat is widest where demand is shrinking (commodity) and vs a competitor Murata barely races (China at the frontier), and thinnest where the growth is (AI-server MLCC vs SEMCO).

## Shared adjacency (graph primer)
`_graph.md` shows Murata with **no cross-thesis links** and none of the peers hold thesis notes — so there is no shared-adjacency baseline to sharpen against; the comparison rests on ticker-specific content reads plus web. Murata's graph neighbourhood is the demand side ([[Sectors/Compute & AI Compute Accelerators]], [[Sectors/Neoclouds & GPU-as-a-Service]]) and the [[Macro & Technology/800VDC Adoption]] cluster, not its MLCC peers — a structural reminder that the vault covers Murata as an *AI-content* play, and this note is the first to benchmark it head-to-head on the *manufacturing* moat that underwrites that play.

## Business model & competitive position

| Dimension | Murata (6981) | Samsung Electro-Mechanics (009150) | TDK (6762) | Taiyo Yuden (6976) | Yageo (2327) | Chinese cohort | Edge |
|---|---|---|---|---|---|---|---|
| MLCC revenue model | Pure-ish passives; MLCC ¥936B (~51% of rev) | Component Solutions div; captive Samsung floor | MLCC ~25% of rev; battery/magnetics/sensors dominate | Auto/industrial-grade MLCC specialist | Broad passive conglomerate (MLCC + tantalum/KEMET + film + resistors) | Commodity MLCC volume | Murata — cleanest premium-MLCC exposure |
| Global MLCC share (2025) | ~28–30% (#1) | ~22–24% (#2) | ~11–13% | ~8–10% | ~7–9% | ~10% combined | Murata |
| 008004 (sub-mm) share | ~50% | ~25–35% | ~15% (trickle vol) | not a volume player | none | none | **Murata** |
| AI-server MLCC share | ~45% | **~40%** | modest | embedded-MLCC entrant | via tantalum/film bypass, not sub-mm | none | Murata, **but gap narrow** |
| Powder integration | 100% in-house BaTiO₃ (+ MF Material JV deepening) | Part in-house, part Sinocera/merchant | TDK-NCI JV (51/49) w/ Nippon Chemical | merchant-sourced | Sinocera + merchant | Sinocera domestic | **Murata (only fully captive)** |
| Component/MLCC OPM | ~18–22% (MLCC); ~14% consolidated | ~8% consolidated | mid-single→low-double, Ni/Pd cost hit | mid-teens | mid-teens (KEMET-diluted) | thin | Murata |
| Customer lock | Apple ~25%, NVIDIA-indirect, auto OEMs | Captive Samsung ~30% + Apple/NVIDIA | diversified | auto Tier-1s | distribution + module BOM | Chinese OEM/Huawei | Murata (breadth) / SEMCO (captive floor) |
| Capital intensity | Capex/rev ~14% (rising) — "the cost of the moat" | R&D +36% YoY, capex-constrained vs demand | diluted across segments | moderate | acquisitive (KEMET/Shibaura) | state-subsidised | tie (both spending into the moat) |

## Financial & scale comparison

| Metric | Murata (6981) | SEMCO (009150) | TDK (6762) | Taiyo Yuden (6976) | Yageo (2327) | Notes |
|---|---|---|---|---|---|---|
| Market cap | ~¥15–17T (~$105–115B) `[web — Murata thesis Key Metrics stale; /numbers 6981 owed]` | ~$10–13B | ~¥7.4T (~$50B) | ~¥2.4T (~$16B) | ~$15–20B (NT$) | Murata is ~10× SEMCO's cap on ~1.3× the MLCC revenue |
| Revenue (latest) | ¥1.83T (+9%) | ~KRW 12.8T (Q1 +17%) | large, MLCC ~25% | ~¥/mid-cap auto-MLCC | AI ~15% of rev (Q1'26) | — |
| MLCC OPM | ~18–22% | ~8% consolidated | compressed −120bps (Ni/Pd) | mid-teens | KEMET-diluted | Murata's margin is the moat's P&L signature |
| Fwd P/E | ~59x NTM (FMP) / ~81x TTM | **~90x fwd** | lower | ~16x | re-rating on AI | SEMCO priced for *future* AI-MLCC catch-up despite ~8% OPM |
| 2026 OP growth | FY27 guide +34.8% | +35.8% (revised up) | guidance cut | rising on auto/AI | AI-led | shortage lifting all |
| Valuation posture | Highest-multiple, highest-margin, widest moat | Fastest re-rate on growth optionality | Cheap but diluted | Cheap, niche | Cheap, breadth | — |

*Figures are directional (web-sourced, wide error bars); the Murata thesis's own Key Metrics (¥4.66T cap / 22.6x P/E) are flagged stale — market cap appears ~3× higher than the note states. Run `/numbers 6981` to refresh.*

## The process / cost / yield moat — magnitude & attribution (core)

### Magnitude — the edge is a gradient that inverts by tier

| Peer                                              | Where it competes                        | Frontier (008004) yield vs Murata        | Cost position                                                        | **Magnitude of Murata's edge**                                                                                                                  | Trajectory                                                      |
| ------------------------------------------------- | ---------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Chinese cohort** (Sunlord/Fenghua/Three-Circle) | Commodity 0402–0603                      | 70–85% *and not in volume* (Murata >95%) | 15–25% *cheaper* at commodity; **inverts** at frontier               | **LARGEST + durable at frontier / NEGATIVE at commodity** — they undercut Murata where it doesn't fight; 7–10yr, structurally capped, at 008004 | Fast-closing at commodity, asymptotic at frontier               |
| **Samsung Electro-Mechanics**                     | Frontier + scale                         | **~85–90% (gap only 5–10pp)**            | Scale + captive Samsung demand ≈ neutralises Murata's unit-cost edge | **SMALLEST + NARROWING** — the only true 008004 peer; ~40% AI-server MLCC share vs ~45%                                                         | Narrowing (captive demand, Sinocera powder, silicon-cap bundle) |
| **TDK**                                           | Premium-capable, sub-scale at frontier   | ~15% share, capable but trickle volume   | Diluted by battery/sensor mix; Ni/Pd margin hit                      | **MODERATE** — chooses portfolio breadth over 008004 depth; a "could but doesn't" gap                                                           | Stable / diluting                                               |
| **Taiyo Yuden**                                   | Auto-grade high-temp / high-V specialist | Not a volume 008004 player               | Niche premium (X8R/X8L, 1000V EV inverter parts)                     | **MODERATE + orthogonal** — races on reliability/voltage axis, not case-size; #1 auto-grade, ahead of Murata *there*                            | Stable in niche                                                 |
| **Yageo (+KEMET)**                                | Commodity MLCC + tantalum/film breadth   | No frontier 008004 presence              | Cost-competitive at commodity; Sinocera-powder dependent             | **LARGE at frontier / N/A** — its AI content is tantalum/film bypass, a *different* socket, not sub-mm MLCC                                     | N/A (different game)                                            |

**Read:** "What is the magnitude of Murata's edge?" has no single answer because Murata's share *rises monotonically with technical difficulty*. The blended ~30% share understates a ~50% frontier position and a near-monopoly-vs-China at 008004; it *overstates* the edge vs SEMCO in the exact AI-server bucket that is compounding. The honest one-liner: **a wide, durable moat against everyone except the one competitor that matters most for the growth story.**

### The cost inversion (why "cheaper China" is wrong at the frontier)

| Lens | Commodity tier (0402/0603) | Frontier tier (008004 / auto-grade) |
|---|---|---|
| Manufacturing cost | China structurally cheaper (labour, subsidised land/power/capex, domestic Sinocera powder) → undercuts Murata **15–25%** | Murata effective cost **lower than any challenger** — >1T units/yr scale + >95% yield + in-house powder beat a 70–85%-yield rival scrapping 15–30% of output; the Chinese cost/qualified-part runs **~35% higher** before overhead |
| Quality | Near-parity (Chinese 0402 X5R meets consumer spec) | Murata/SEMCO only — tighter tolerance, lower ESL/ESR, X7R/X8R at 125–150°C, AEC-Q200; Chinese parts **not qualified** for AI-accelerator or auto safety sockets |
| Yield / defect | Chinese ~90%+ — competitive | Murata >95%, SEMCO ~85–90%, Chinese 70–85% & not-in-volume; geometric yield collapse at 1,000+ layers (0.1%/layer → >50% scrap) is the economic moat |

### Attribution — one root variable, four compounding edges

The edge is **not** "quality, reliability, yield, *or* chemistry" — it is all four, separable and individually measurable, all cascading from the single powder/layer variable:

| Edge | Measurable signal | Murata vs best challenger | Time to close | Why it is Murata's |
|---|---|---|---|---|
| **Yield at smallest case size** | 008004 production yield | >95% vs SEMCO 85–90% vs China 70–85% | 5–10yr (China); ongoing (SEMCO) | Sub-100 nm powder + co-fire shrinkage matching + sintering profile — the binding *cost* lever |
| **In-field DPM** | OEM warranty / FA data | <0.1 vs 1–10 DPM | 7–15yr | At 440k MLCCs/rack, 0.1 DPM → ~4.4% board fail; 5 DPM → >80% — un-tolerable at any price gap |
| **AEC-Q200 platform base** | qualified design count × duration | hundreds over 20yr vs dozens | 3–5yr/platform, non-transferable | Locks stickiness design-by-design across thousands of auto sockets |
| **Dielectric/sinter chemistry IP** | patent thicket + 80yr iteration | decades-deep, **trade-secret not patent** | 10yr+ | Un-copyable by reading filings; reverse-engineering finished parts ≠ the recipe |

**The single root cause and Murata's uniqueness in it:** all four trace to **100%-in-house sub-100 nm barium-titanate powder** grown by proprietary co-precipitation, plus the tacit sintering/co-fire know-how that turns it into a 1,000-layer part at >95% yield. This is the *one* place Murata is genuinely alone: SEMCO is "part in-house, part sourced," Yageo and the commodity cohort buy Sinocera domestic powder, and TDK just built the TDK-NCI JV to *secure merchant* powder rather than internalise it. Murata is even deepening captive supply (MF Material JV, Nobeoka 2027). The moat is a *materials-chemistry* moat wearing a *manufacturing-yield* mask.

## Dynamic analysis

1. **Where the gap is narrowing (the one that matters):** SEMCO. R&D +36% YoY, a KRW 454B AI-MLCC order + KRW ~1.5T silicon-cap contract, final-stage talks to supply a major US cloud provider, and AI-server MLCC share ~40% vs Murata's ~45%. SEMCO's closure path runs through (a) captive Samsung foundry/HBM/Galaxy demand that de-risks aggressive small-case capex, (b) Sinocera powder lowering its input cost, and (c) the only MLCC+FC-BGA-substrate+silicon-cap bundle in the industry — a package-level power-integrity offer Murata *cannot* match without a leading-edge substrate business. The 5–10pp yield gap is "the last moat between the two premium leaders," and yield funds the R&D that protects yield — but SEMCO is the best-capitalised attacker the gap has ever faced.
2. **Where the gap is *not* closing (structurally):** China at 008004. Sunlord doubled capacity to 100B units and Three-Circle added 100B units — but 100% of Chinese share gains are at commodity case sizes; sub-mm stays <5%. As China reaches 008004, Murata resets the frontier to 005003 every ~3–4 years. The frontier is a moving target; the catch-up clock only ever runs against yesterday's frontier.
3. **The one genuine China catch-up vector:** upstream powder. Sinocera has broken Japanese powder dependence at commodity grades and is *already inside SEMCO's and Yageo's supply chains*. If Sinocera cracks sub-100 nm tight-distribution powder at volume, the commodity clock accelerates and SEMCO's cost position improves — but frontier sintering/co-fire know-how is a separate, deeper moat powder alone does not unlock. Watch Sinocera's grade roadmap, not Chinese cap-maker capacity.
4. **Pricing-power divergence:** all five are raising price into the 2026 shortage (Murata +15–35% Apr, Taiyo Yuden +6–13% May, SEMCO up to +10%, Yageo/KEMET +10–20%), lead times 20–40wk, high-end capacity won't meet AI demand before late-2027. But this is **units↑ + prices↑ = shortage** (Industry #7) — the apparent widening of Murata's edge is partly cyclical scarcity, not pure structural monopoly. The durable component is the yield/DPM/qual/chemistry stack; the cyclical component is the shortage premium that the Murata thesis's own model gives back FY30–31.
5. **Logical tension (what each needs the other to be wrong about):** Murata's premium multiple needs the 008004 moat to be a *durable monopoly*; SEMCO's ~90x forward P/E needs that same moat to be a *closing gap* it can cross with captive demand and bundling. Both cannot be fully right. The AI-server share data (~45/40) sides with SEMCO's framing more than the blended (30/23) or 008004 (50/25) data does — the growth segment is the least monopolised.

## Investment verdict

- **Risk-adjusted asymmetry:** Murata remains the highest-*quality* expression of the MLCC manufacturing moat (widest moat, highest margin, only fully-captive powder) — but it is not the highest-*upside* expression on the AI-MLCC theme. SEMCO offers more torque (smaller base, faster share gain, silicon-cap optionality) at more valuation and execution risk (~90x fwd P/E on ~8% OPM). The vault's stress test ([[Research/2026-06-27 - 6981 - Stress Test]]) already flags that Murata's upside is a *re-rate that has largely happened*; this comparison adds that the *moat* underwriting that re-rate is narrowest in the growth segment.
- **Portfolio role:** Murata and SEMCO are **partial substitutes at the frontier, complements across the stack.** Owning both concentrates a single bet — the 008004/AI-server MLCC shortage — twice; the diversifying pair is Murata (moat/quality) vs an *upstream* materials name (Sakai/Toray/Disco per [[Research/2026-06-05 - AI-Grade MLCC Upstream Pricing Power - deep-dive]]), where the shortage rent may accrue more cleanly.
- **Preference trigger (falsifiable):** prefer SEMCO over Murata *if* SEMCO's AI-server MLCC share crosses Murata's (≥45% on any credible 2026–27 supply-chain read) OR SEMCO wins a disclosed AI-accelerator 008004 design-in at a US hyperscaler at Murata's expense. Prefer Murata *if* the 008004 yield gap holds ≥5pp through FY27 AND Sinocera fails to sample sub-100 nm powder to a Tier-1 OEM.
- **Conviction gap:** Murata is the only name here with a thesis; the comparison does not argue for opening SEMCO/TDK/Taiyo Yuden/Yageo theses, but SEMCO now clears the bar for a watch-thesis specifically because it is the one competitor that can compress Murata's growth-segment moat. Conviction on Murata: **unchanged (high)** — no trigger breached; the moat is intact, merely more precisely bounded.

## Evidence

**Share & yield ladder:**
- Overall MLCC 2025: Murata ~28–30%, SEMCO ~22–24%, TDK ~11–13%, Taiyo Yuden ~8–10%, Yageo ~7–9%; top-5 ≈ 72–78%; Chinese cohort ~10% (H2 2024).
- AI-server MLCC: Murata ~45%, **SEMCO ~40%** — the narrowest gap of any segment.
- 008004 yield: Murata >95%, SEMCO ~85–90%, Chinese 70–85% & not-in-volume (vault sector note; corroborated by web "high-end yields significantly lower than standard, tight supply").
- 008004 case-size share: Murata ~50%, SEMCO ~25–35%, TDK ~15%, others <3%.

**Cost / process:**
- Chinese undercut Japanese 15–25% at commodity; excluded from auto + datacenter (AEC-Q200, low-ESL). Cost inverts at 008004 (~35% higher per qualified part at 70% yield).
- Single-variable driver: layer thickness × count × powder size — Murata/SEMCO 0.3–0.5 µm from sub-100 nm powder vs China 1–3 µm from 150–300 nm.
- Root moat: Murata 100% in-house BaTiO₃; SEMCO part-sourced; Yageo/China on Sinocera; TDK secures merchant via TDK-NCI JV. Sinocera now inside SEMCO's + Yageo's supply chains.

**Competitive dynamics (2026):**
- SEMCO: R&D +36%, KRW 454B AI-MLCC order, ~KRW 1.5T silicon-cap contract, US-cloud MLCC talks final-stage, MLCC+substrate+silicon-cap bundle; ~90x fwd P/E, ~8% OPM.
- Taiyo Yuden: embedded MLCCs for AI servers, 1000V MLCC for EV traction inverters — niche/orthogonal frontier.
- TDK: FY26 guidance cut on Ni/Pd +18%, passive margin −120bps, accelerating copper-electrode substitution.
- Yageo: AI ~15% of rev (Q1'26); KEMET tantalum +20%; portfolio +10–15%; no sub-mm MLCC.
- China: Sunlord →100B units, Three-Circle +100B units; commodity only; sub-mm <5% through 2030.
- Shortage: Murata +15–35% (Apr), Taiyo Yuden +6–13% (May), SEMCO ≤10%, lead times 20–40wk, high-end capacity short of AI demand until late-2027.
- External moat reads: Morningstar moat → **Wide** (MLCC advantage "expands"); Citi → **Buy**.

**Sources:** [Passive Components — China MLCC 10% share](https://passive-components.eu/chinas-mlcc-makers-reach-10-market-share/) · [BigGo — SEMCO KRW 454B AI-MLCC order](https://finance.biggo.com/news/fd960002-4c95-4b20-a3dc-6204f3f3be4d) · [Futunn — Murata expands, SEMCO 1.5T KRW](https://news.futunn.com/en/post/74590019/ai-sparks-surge-in-mlcc-demand-murata-aggressively-expands-production) · [TechTimes — SEMCO R&D +36%](https://www.techtimes.com/articles/317337/20260529/samsung-electro-mechanics-ai-server-pivot-rd-surges-36-capacity-cannot-match-big-tech-demand.htm) · [DigiTimes — SEMCO substrate/MLCC AI push](https://www.digitimes.com/news/a20260630VL208/semco-substrate-ai-server-mlcc-capacitor.html) · [LDeepAI — MLCC 2026 China substitution](https://www.ldeepai.com/tech-hub/mlcc-market-2026-ai-server-supply-chain-china-substitution/) · [Storm Media — Yageo AI 15%](https://world.storm.mg/articles/1135950) · [Morningstar — Murata moat upgraded to Wide](https://www.morningstar.com/company-reports/1231429-murata-manufacturing-moat-rating-upgraded-to-wide-mlcc-competitive-advantage-expands) · [DigiTimes — Murata doubles down on quality vs China](https://www.digitimes.com/news/a20250918PD207/murata-mlcc-market-production-efficiency.html) · [Cosolvic — Murata price increase 2026](https://cosolvic.com/blog/murata-mlcc-price-increase-2026-ai-server-impact/)

## Contradiction Check

**Challenge 1 — "Murata's moat is unassailable" (the framing this note tightens).** The stress test and the AI-server share data both cut against a clean-monopoly read: SEMCO at ~40% AI-server MLCC share, closing a 5–10pp yield gap with the best balance sheet the frontier has faced, plus a silicon-cap+substrate bundle Murata can't mirror. **Net: partial refute of "unassailable," full support of "wide moat."** The moat is durable vs China and real vs SEMCO — but a *lead*, not a *monopoly*, in the growth segment.

**Challenge 2 — the "100% in-house powder" attribution.** Per [[Research/2026-06-05 - AI-Grade MLCC Upstream Pricing Power - deep-dive]], high-spec AI-grade sub-100 nm/rare-earth-doped grades are *increasingly merchant-sourced* industry-wide, and single-source upstream suppliers (release film Toray ~87%, BaTiO₃, Ni powder) may hold *more acute* pricing power than the cap makers — Murata pays rent *upward*. Via the [[Lens - Value Layer Monopoly]] filter this makes Murata a **WEAK-to-MODERATE layer monopoly**: it owns the 008004 layer but does not own the layer beneath it. **Net: nuances but does not break the attribution** — Murata is still the *only* fully-captive powder player and is deepening it (MF Material JV); the moat is forward-durable even if spot-overstated.

**Challenge 3 — is the edge structural or cyclical?** [[Lens - Automation & AI Readiness]] §6 (semi split) reads Murata's yield/chemistry edge as *tacit* knowledge (Anti-fit on operator-automation) — which is exactly why it is durable (un-serialisable, un-copyable) but also why margin expansion cannot lean on AI operating leverage, only on mix + shortage. Industry #7 flags the current units↑/prices↑ as *shortage*, i.e. late up-cycle: part of the visible edge is scarcity rent the thesis models giving back FY30–31. **Net: the durable moat is the yield/DPM/qual/chemistry stack; the shortage premium is cyclical and should not be extrapolated.**

**Challenge 4 — base rate / outside view.** A 5–10pp yield gap vs a well-capitalised captive-demand competitor is a *closing* gap in most process-industry reference classes once the follower commits capital and secures materials — which SEMCO has now done. The base-rate prior is that second-source frontier producers converge on the leader's yield over 5–10 years unless a genuine chemistry barrier holds. Murata's trade-secret co-precipitation + tacit sintering is the candidate barrier; whether it holds against SEMCO's captive-funded R&D + Sinocera powder is *the* falsifying question, and it is unresolved. **Net: the disconfirming datapoint to monitor is SEMCO 008004 yield crossing ~92–93%.**

**Supports existing conviction:** the moat is real, measurable across four axes, and widening vs China; AI-MLCC demand (440k/rack, 3.3× by FY30, +15–35% hikes, 20–40wk lead times) is corroborated; Murata's ~18–22% MLCC OPM vs SEMCO's ~8% consolidated is the P&L proof the edge is monetised. No conviction change warranted on this comparison alone.
