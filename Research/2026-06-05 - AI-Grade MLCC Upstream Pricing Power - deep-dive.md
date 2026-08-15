---
publish: false
date: 2026-06-05
tags: [research, mlcc, semiconductors, passives, supply-chain, 6981, 3402, 4078, 4092, 6146]
sector: MLCC & Power Semiconductors
ticker: 
source: '_Inbox/AI-Grade MLCC Supply Chain.md'
source_type: deep-dive
propagated_to: [6981]
---

# AI-Grade MLCC Upstream Pricing Power — Bottleneck Map

## Thesis Delta
Opens an investable layer the vault has not modelled: the **materials upstream of [[Theses/6981 - Murata Manufacturing|Murata]]**, where single-source oligopolies in release film, sub-100 nm barium titanate, and ultra-fine nickel powder hold more acute pricing power than the MLCC makers themselves — because the maker must pass cost through to the GPU/OEM customer while the single-source material supplier does not. Key question this forces: should the vault open new theses on **Sakai Chemical (4078)**, **Toray (3402)**, or **Disco (6146)** as upstream complements to the Murata position — and does Murata's "100% in-house dielectric powder" moat claim survive the finding that high-spec AI-grade powder is *increasingly* merchant-sourced?

## Summary
The source maps the AI-grade MLCC bill-of-materials and ranks each input by acuteness of pricing power, arguing the cleanest structural-rent capture in the AI-MLCC boom is one layer upstream of the capacitor makers the vault already covers. The mechanism: each premium AI-grade constraint — sub-100 nm dielectric particle size, sub-200 nm nickel powder, sub-25 µm release film with sub-0.1 µm defect control — narrows the qualified merchant supplier set from "many" to "two or three," and because each input is a low-single-digit % of MLCC cost yet binary-critical (one defect destroys a 500–1,000-layer cap), suppliers hold the classic "small cost, high criticality" pricing-power profile. Qualification cycles of 12–24 months per grade per MLCC maker lock the moat in.

The demand backdrop is confirming, not speculative. A GB200 NVL72 rack consumes ~440,000 MLCCs (≈30× a smartphone's content); Murata's IR Day 2025 guides AI-server MLCC demand to 3.3× FY2025 by FY2030 (~30% CAGR). Pricing is now moving: Murata announced a 15–35% AI-server/auto-grade/RF MLCC price increase effective 1 April 2026; Taiyo Yuden 6–13% from 1 May; Samsung Electro-Mechanics evaluating up to 10%. Premium-part lead times have stretched from 8 weeks to 24–40 weeks, and neither auto-grade requalification (18–24 months) nor greenfield MLCC capacity (18–24 months) can flex fast — so the shortage converts to upstream materials pricing power before capacity arrives. This is the supply-side counterpart to the [[Macro & Technology/800VDC Adoption|800VDC]] demand-profile up-mix already modelled in the Murata thesis.

The central trade-off the source surfaces is an **investability paradox**: the single most acute bottleneck — specialty PET release film, where Toray leads a 5-firm oligopoly holding ~87% share — is also the one where the leading player carries the *least* concentrated equity exposure (MLCC film ≈5% of Toray's revenue, undisclosed, buried in Functional Chemicals). Conversely the cleanest small-cap pure-plays — Sakai Chemical and Nippon Chemical Industrial in barium titanate — sit in a bottleneck that is real but already *partially captive-served* (Murata and Samsung EM make some powder in-house), and both are illiquid (¥76 bn and ¥48 bn caps). The nickel-powder tier has no clean vehicle at all: the pure-play (Shoei Chemical) is private, the cleanest listed name (Toho Titanium, 5727) is being delisted by parent JX Advanced Metals via a simplified share exchange announced 25 Feb 2026, and the survivors (Sumitomo Metal Mining, JFE) are dominantly base-metals companies where MLCC powder is rounding-error. "A real bottleneck with no clean public-market vehicle" is itself the source's conclusion for tier 3.

Two corporate-structure datapoints validate the merchant-moat read against the captive-displacement risk: TDK established **TDK-NCI Advanced Materials** (TDK 51% / Nippon Chemical 49%) on 1 April 2026 for MLCC ceramic materials, and **MF Material** (Murata 35% / Fuji Titanium 55% / Ishihara 10%) is expanding barium-titanate capacity at Nobeoka for 2027 — i.e., even the largest captive-capable MLCC makers are deepening reliance on Japanese merchant powder chemistry rather than fully internalising it.

## Framework / Mental Model
**Name:** Ranked-by-acuteness supply-chain pricing-power map, with an investability overlay.

**Component 1 — the acuteness axis.** Each input's pricing power is scored on four reinforcing factors:
1. **Qualified-supplier-set width** — how far the premium spec (particle size, defect density, purity) collapses the merchant list. Narrower = more acute. Release film → 5 firms; BaTiO₃ → 3; Ni powder → 4 industrialised.
2. **Qualification-cycle length / switching cost** — months of statistical yield validation a new grade needs at each MLCC maker before design-in (release film: multi-year; Ni powder: 12–18 mo; BaTiO₃: similar). Longer = stickier.
3. **Criticality-to-cost ratio** — input is a low-single-digit % of BOM but binary-critical (one defect = one dead multi-layer cap). High ratio = "small cost, high criticality" → maker pays up rather than risk yield.
4. **Merchant share of demand** — the captive-vs-merchant split. Merchant suppliers sell only into the *gap* between captive supply and total demand; a high-captive input (BaTiO₃) dilutes the merchant pricing signal even when the bottleneck is physically real.

**Component 2 — the five-tier output** (ranked, most acute first): (1) specialty PET release film; (2) sub-100 nm hydrothermal BaTiO₃; (3) ultra-fine Ni internal-electrode powder; (4) conductive/electrode/termination paste; (5) precision dicing/singulation equipment. Tiers 1–3 narrow the merchant set to 2–3 names; tiers 4–5 have more qualified suppliers (8+ paste formulators) or a single near-monopoly with diversified end-demand (Disco).

**Component 3 — the investability overlay (methodology to re-apply).** Acuteness alone is not investable. Overlay three filters on each tier's listed names: (a) **pure-play %** — what fraction of the vehicle's revenue/EV is the bottleneck (Toray ~5%, Sakai ~15–20%, Disco low-double-digit); (b) **liquidity** — small-cap pure-plays (Sakai ¥76 bn, NCI ¥48 bn) cap institutional size; (c) **listing status** — private (Shoei) or delisting (Toho) zeroes access. The investable frontier is where acuteness × pure-play % × liquidity × listing-access is jointly high — which the source finds is *nowhere perfectly*, producing the central paradox: most acute bottleneck ↔ least concentrated equity; cleanest pure-play ↔ partially-captive bottleneck. Re-applicable to any oligopoly supply chain (e.g. HBM photoresist, CoWoS underfill) to locate where a real choke point is also cleanly buyable.

## Evidence

**Bottleneck ranking (framework output):**

| Rank | Bottleneck | Premium spec | Concentration | Top merchant names | Cleanest listed vehicle |
|---|---|---|---|---|---|
| 1 | Specialty PET release film | <25 µm, <0.1 µm defect, ±1% thickness for <1 µm green sheet | Top-5 ≈ 87% share (QY Research); top-7 ≈ 70% | **Toray** (#1), Toyobo, Mitsui Chem, LINTEC, SKC, Mitsubishi Chem, Nan Ya | Toray (3402) — diluted |
| 2 | Sub-100 nm hydrothermal BaTiO₃ | <100 nm grain, sub-ppm Fe/Si/Na | 3-firm JP oligopoly + captive | **Sakai** (~25%), Nippon Chemical, Fuji Titanium (MF Material JV) | Sakai (4078), NCI (4092) |
| 3 | Ultra-fine Ni electrode powder | <200 nm (→<150 nm), 0.3–3.0 wt% O₂ | 4 industrialised at MLCC grade | SMM (~18%), JFE Mineral (~14%), Toho Titanium, **Shoei** | Toho (5727) — delisting |
| 4 | Conductive/electrode/termination paste | screen-print <1 µm, survive 1,000–1,300°C co-fire | Top-4 ≈ 60% | **Shoei** (#1 Ni paste), SMM, Noritake, Ferro/Vibrantz, Heraeus | None clean (Shoei private) |
| 5 | Precision dicing/singulation | sub-µm tolerance at 008004 (0.25×0.125 mm) | Disco >80% MLCC (est) | **Disco**, Tokyo Seimitsu (#2) | Disco (6146) — diluted |

**Investable names — financials & caveats:**

| Name | Ticker | Mkt cap | Exposure | Key financials | Caveat |
|---|---|---|---|---|---|
| Sakai Chemical | TSE 4078 | ¥76 bn (~$500 M) | Sub-100 nm BaTiO₃, ~25% merchant share | FY26 rev ¥81.4 bn, NI ¥2.75 bn, PE 15.9x, yld 2.94%; +18% vs Nikkei 6 mo, +50% vs 200-DMA | Electronic Materials ~15–20% of group; illiquid |
| Nippon Chemical Industrial | TSE 4092 | ¥48.5 bn (~$320 M) | BaTiO₃; TDK-NCI JV (TDK 51/NCI 49) Apr 2026 | ¥5,560, ~17x PE, yld 2.55%, EPS ¥331 | Smaller/less diversified; forward-conviction via TDK JV |
| Toray Industries | TSE 3402 | ¥1.57–1.96 T (~$10–13 bn) | #1 MLCC release film (Lumirror); Gifu +60% capacity 2025 (¥8 bn) | FY26 rev ¥2,585 bn (+0.9%), NI ¥79.5 bn | MLCC film ~5% of rev (est, undisclosed); conglomerate |
| Disco | TSE 6146 | ¥7.06–7.59 T (~$43–48 bn) | Dicing/singulation, 60–70% semi / >80% MLCC | FY26 rev ¥436.9 bn (+11%), NI ¥135.5 bn, GM >65%, OPM >40%, PE ~52x | MLCC = low-double-digit % rev; primarily AI-semis play |
| Sumitomo Metal Mining | TSE 5713 | ¥2.6 T (~$16.3 bn) | Ni powder ~18% share; Materials seg ~15–20% rev | FY25 battery-materials impairments | Diversified base-metals; nickel-price play |
| Ishihara Sangyo | TSE 4028 | ¥94.6 bn (~$620 M) | 55% of MF Material (BaTiO₃) via Fuji Titanium | — | TiO₂/agrochem dominant; "Murata captive" tracker |
| Toho Titanium | TSE 5727 | ¥188 bn (~$1.2 bn) | Cleanest Ni-powder pure-play; No.4 Wakamatsu plant (¥7.5 bn) | — | **Being delisted** by JX Advanced Metals (share exchange ann. 25 Feb 2026) → rotate to JX |

**Demand & pricing datapoints:**

| Metric | Value | Source |
|---|---|---|
| GB200 NVL72 MLCC content | ~440,000 units (≈30× a smartphone; enterprise server ~1,000) | TradingKey, May 2026 |
| AI-server MLCC demand FY2030 | 3.3× FY2025; ~30% CAGR FY25–30 | Murata IR Day, 1 Dec 2025 (via TrendForce/Kyodo) |
| Murata price increase | +15–35%, eff. 1 Apr 2026 (AI-server high-cap, auto-grade, RF/µwave) | TrendForce, 17 Mar 2026 |
| Taiyo Yuden price increase | +6–13%, eff. 1 May 2026 | SemiMedia / TrendForce, 15 Apr 2026 |
| Samsung Electro-Mechanics | up to 10% (evaluating) | trade press |
| Premium part lead times | 8 wk → 24–40 wk | source |
| Requal / greenfield lead time | 18–24 mo each | source |
| Ceramic powder cost share | 20–25% low-cap MLCC; 35–45% high-cap | source |
| Sub-100 nm BaTiO₃ premium | +35–60% vs standard high-purity | Dataintelo |

**Corporate-structure events:**
- **TDK-NCI Advanced Materials** (TDK 51% / Nippon Chemical 49%), MLCC ceramic materials, established 1 Apr 2026 — locks NCI as TDK's strategic powder partner.
- **MF Material Co.** — Murata 35% / Fuji Titanium 55% / Ishihara 10%; BaTiO₃ capacity expansion at Nobeoka, Miyazaki for 2027 commissioning.
- **Toho Titanium delisting** — JX Advanced Metals simplified share exchange announced 25 Feb 2026; listed equity disappears; exposure must rotate to JX Advanced Metals (ENEOS metals spinout, listed Mar 2025).
- **Toray Lumirror** — ¥8 bn investment, +60% release-film capacity at Gifu Plant, online 2025.

**Illustrative upstream model portfolio (source's, not vault-endorsed):** Toray 30% / Sakai 20% / Disco 20% / NCI 15% / JX Advanced Metals 10% / SMM 5%.

**Identifier traps flagged:** "Shoei" listed entities **Shoei Co. (7839, helmets)** and **Shoei Yakuhin (3537, chemical trader)** have **no MLCC exposure** — not substitutes for the private Shoei Chemical.

## Contradiction Check
**Assumption challenged — Murata's "100% in-house dielectric powder" vertical-integration moat.** The [[Theses/6981 - Murata Manufacturing]] thesis rests heavily on Murata making its own barium titanate (§Value chain: "integrated upstream into its own dielectric slurry production… the principal cost and quality differentiator"). This source nuances rather than breaks it: Murata produces *some* powder in-house, but high-spec AI-grade sub-100 nm and rare-earth-doped grades are "increasingly sourced from the Japanese merchant players" (Sakai, NCI). If true at the AI-grade frontier, the captive-integration claim is partly overstated for the exact parts the thesis says are growing fastest. **Net: weak challenge** — and partly self-cancelling, because Murata is *deepening* captive supply via the MF Material JV (Murata 35%), which supports the integration narrative on a forward basis.

**Assumption challenged — that Murata is the best vehicle for the AI-MLCC theme.** The source's core claim — "in tight supply, upstream BOM suppliers with single-source positions often extract more rent than the MLCC makers, who must still pass through to the GPU/OEM customer" — directly contests the relative-attractiveness conclusion in [[Sectors/MLCC & Power Semiconductors]] §Investor heuristics (barbell: Murata core 40% / Aixtron / Infineon / Wolfspeed / POWI). It proposes a *different, non-overlapping* surface (release film / BaTiO₃ / Ni powder) the sector note has not scored. **Net: additive, not contradictory** — but it means the sector's "where to deploy in this space" answer is incomplete on the upstream-materials axis.

**Supports existing conviction:** the AI-MLCC demand ramp (440k/rack, 3.3× by FY2030, confirmed price hikes, 24–40 wk lead times) corroborates the Murata thesis's structural-volume pillar and the 2027–29 small-case shortage call. No conviction change to Murata warranted on this source alone; it is a lateral expansion of the opportunity set.

## Source Excerpts
- "Global top five companies account for nearly 87% of market share" — QY Research, *Global MLCC Release Film Sales Market Report 2026–2032*.
- "Toray leads the global MLCC mold release film market, producing these offerings at the Mishima and Gifu plants in Japan, Penfibre Sdn. Berhad in Malaysia, and Toray Advanced Materials Korea Inc." — Toray press release, Oct 2022.
- "Sakai Chemical dominates the global MLCC dielectric powder market with approximately 25% share." — Chemical Research Insight.
- "a standard enterprise-grade server requires about 1,000 units, an Nvidia GB200 NVL72 rack requires approximately 440,000 — a quantity 30 times that of a smartphone." — TradingKey, May 2026.
- "Murata Manufacturing said demand for MLCCs used in AI servers is projected to be 3.3 times higher in fiscal 2030 than in fiscal 2025, with an average annual growth rate of approximately 30%…" — Murata IR Day 2025 (via TrendForce/Kyodo).
- "JX Advanced Metals announced February 25, 2026 a simplified share exchange to take Toho Titanium private as a wholly-owned subsidiary. The listed equity will disappear."
- "the most acute bottleneck — release film — is also the one where the leading player (Toray) has the *least* concentrated equity exposure… Conversely, the pure-plays (Sakai, NCI) are in BaTiO3, where the bottleneck is real but the merchant market is already partially captive-served." — source, central trade-off.
