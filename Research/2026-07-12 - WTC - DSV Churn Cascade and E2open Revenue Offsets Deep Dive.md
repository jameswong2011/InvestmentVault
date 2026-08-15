---
publish: false
date: 2026-07-12
tags: [research, deep-dive, WTC, cargowise, dsv, e2open, churn]
sector: Logistics & Supply Chain Software
ticker: WTC
source: vault synthesis
source_type: deep-dive
propagated_to: [WTC]
---

# WTC — DSV Churn Cascade Risk & E2open Revenue Offsets (Deep Dive)

## Related Theses
- [[Theses/WTC - WiseTech Global]]

## Related Sectors
- [[Sectors/Logistics & Supply Chain Software]]

## Thesis Delta

Supports the existing HIGH conviction (set 2026-07-11) on the churn leg while sharpening two watch items. The DSV-off-CargoWise cascade is **contained, not cracking**: DSV is the sole defection, it is idiosyncratic (inherited a mature TMS, did not build), the deep-lock-in cohort is a minority of the top 25, and the → LOW conviction trigger (a *second core* forwarder evaluating migration) is **untripped** as of July 2026. The P&L impact is an FY2028+ event, not FY2026–27. Feeds §Industry Context §6 (self-build risk, re-underwritten) and new §7 (revenue-offset arithmetic). Two live watch items surfaced: (1) Value Packs' 20–50% price increase is concentrated on the ~30% of CargoWise revenue held by large legacy-contract accounts — the same self-build-capable tier; (2) the "<1% attrition" metric is definitionally blind to slow enterprise migration.

## Summary

DSV's migration off CargoWise onto DB Schenker's in-house **Tango** TMS is the first credible large-forwarder defection in the platform's history, and it is real — but July 2026 web research re-underwrites it as a bounded, idiosyncratic event rather than the leading edge of a cascade. At its **12–13 May 2026 Capital Markets Day**, DSV disclosed a "count-to-one" systems strategy: a slide reading "CargoWise One → Tango" for Air & Sea and "Star" consolidating 25+ Road systems, with **~25% of volumes already on Tango** and the broad rollout beginning 2027. The ~DKr6bn of targeted 2030 savings is an "AI + technology" bucket in which the CargoWise exit is one lever, not the whole figure. WiseTech's **9 July 2026 ASX clarification** confirmed the migration is slow and contractually floored: DSV CargoWise **volumes +20% over six months** (users +3% — deeper automation), a **contract to September 2028**, and renewal talks underway. Sell-side puts the earnings impact no earlier than FY2028 (Jefferies: DSV ~US$150M ≈ 9% of revenue, ~10% of FY2027 EBITDA at long-run risk; Citi: FY2028 CargoWise growth cut to 7%, A$65 PT).

The decisive analytical point is that **DSV did not build Tango — it inherited it**. Tango is DB Schenker's proprietary Air & Ocean platform, built with Capgemini on Riege's "Scope" engine, German-customs-certified, live across ~130 countries after replacing 32+ legacy systems. No other top-25 forwarder has an equivalent on the shelf, and DSV has signalled no intent to commercialize Tango. The reference class for "large forwarder tries to leave/avoid CargoWise via self-build" is a graveyard: DHL's abandoned New Forwarding Environment (€345M write-off, 2015), Panalpina's scrapped SAP-TMS, Nippon Express's >$100M in failed builds — all capitulated *to* CargoWise. The exposed cohort is also smaller than the "24/25" headline: WiseTech's own count is 23/25 (any-module), and Bernstein's operational count is ~13 of the top 25 running CargoWise One as core. Several top-10 names (Expeditors, C.H. Robinson, Maersk, K+N-core) were never core adopters.

On the growth side, WiseTech is opening new CargoWise revenue faster than the execution layer erodes. Value Packs (~95% migrated, ~+6% CargoWise revenue per Jefferies) reprices around AI by charging per-transaction — so AI-driven productivity grows revenue rather than cannibalizing seats (AI usage up 2–5x since launch). CTO/landside, the WMS Value Pack, Neo (shipper portal, Web Tracker retired 1 Apr 2026), ComplianceWise/CBAM, and LatAm mid-market are additional vectors. E2open converts churn risk into a moat: owning the shipper-planning node (~500,000 partners, ~250 blue-chip incl. Dell, Nvidia, Ford, L'Oréal, Schneider Electric) *and* the forwarder-execution node raises switching costs, while INTTRA (~18.5% of global ocean bookings) + Bolero eBL trade-finance automation is the concrete synergy shipping in 2026, and the US$50M cost synergy landed ~18 months early.

## Framework / Mental Model

**The [[Lens - Value Layer Monopoly]] two-layer split** (held as a hypothesis to test, per the READING PROTOCOL in [[Generalist - Overview]]) is the organizing frame for the churn diagnosis. CargoWise occupies two stacked layers with opposite AI-era signs:

- **Forwarder-execution layer** (bookings, documentation, workflow) — **contestable / moat-dissolving**. DSV proves a scaled forwarder with an inherited stack can leave; generative AI lowers the cost of rebuilding execution workflows. This is the §2 "falling switching costs / melting asset" pattern, confined to the top 5–10 forwarders where self-build economics cross over.
- **Customs/compliance layer** (160+ country databases, ~75% of global customs data, ~80% of manufactured trade flows) — **durable / moat-widening**. Even Kuehne+Nagel, running its own core TMS, *rents* CargoWise for customs. Every CBAM, sanctions, and tariff change is a fixed-cost update the incumbent amortizes and sub-scale entrants cannot. This is the §1B regulatory fixed-cost moat.

The thesis error the lens warns against: crediting the *whole* platform as durable infrastructure when only the compliance sub-layer is. The bull's "monopoly" and the bear's "cracking" are both right — about different layers. The net revenue trajectory depends on whether the compliance-plus-shipper-node franchise compounds faster than the execution layer bleeds; through FY2027 the arithmetic favors growth.

## Evidence

### DSV migration — factual status (July 2026)
- **12–13 May 2026 Capital Markets Day** ("Leverage to Lead", Hedehusene): "count-to-one" strategy; target-architecture slide "CargoWise One → Tango" (Air & Sea "2 TMSs → 1 TMS"); Road → "Star" (25+ systems consolidated). ~**25% of DSV volumes on Tango**; broad rollout from 2027. ~DKr9bn total 2030 productivity target split ~DKr6bn "AI + technology" (incl. Tango/Star migration) + ~DKr3bn network optimization.
- **9–10 July 2026 WiseTech ASX "Clarification regarding relationship with DSV"**: DSV an active customer; CargoWise **volumes +20% over six months**, **users +3%**; "substantial financial commitment" **contract to September 2028**; talks ongoing for post-2028 collaboration on AI tooling. WTC ~A$34, ~-50% YTD on the day.
- CEO **Jens Lund**: "very likely that we will, over time, gravitate towards our own solution."
- **Tango** = DB Schenker "Transport And Global Operations"; built with Capgemini on Riege "Scope" engine; German-customs-certified; ~130 countries; replaced 32+ legacy systems. Inherited via the €14.3B DB Schenker deal (closed Apr 2025). **No stated intent to commercialize externally.**

### Economics
- **Bernstein**: DSV CargoWise spend ~US$78M/yr pre-Schenker, >US$125M post; "up to 15% of EBITDA at peak" (Schenker volume scaling onto CargoWise before migrating off — a transient peak).
- **Jefferies (13 May 2026)**: DSV contract ~US$150M (~A$207M) ≈ ~9% of WTC revenue, ~10% of FY2027 EBITDA at long-run risk.
- **Citi (Jul 2026)**: cut FY2028 CargoWise growth forecast to 7% (stripping ~US$80M); DSV-exit hit lands no earlier than FY2028; PT A$65.35.
- Consensus PT dispersion wide (~A$52 to ~A$100+; ~A$87 midpoint); no sell-side analyst calls DSV thesis-breaking.

### Forwarder-by-forwarder cascade read
- **K+N (#2)**: in-house core (KN FreightNet / RoadLOG); CargoWise customs module only, into production 1H26; "Roadmap 2026" builds own TMS → deepening on CW customs, not leaving.
- **DHL GF (#3)**: deep CargoWise core (myDHLi); prior self-build "NFE" **scrapped 2015, €345M write-off**; "don't have to do everything ourselves."
- **CEVA/CMA CGM (#6)**: migrated acquired Bolloré *onto* CargoWise; loyalist.
- **Expeditors (#7), C.H. Robinson (#8), Maersk (#11)**: long-standing in-house non-adopters — equilibria, not defections.
- **Nippon Express (#5), Panalpina**: >$100M / scrapped self-builds → capitulated to CargoWise.
- **GEODIS (#9)**: current TMS posture unverified (largest open gap on a top-10 name).

### New CargoWise revenue vectors
- **Value Packs** (Dec 2025, ~95% migrated): ~+6% CargoWise revenue FY26–27 (Jefferies); ~$19.95/full import container, ~$9.95/standalone customs entry; ~30% of CargoWise revenue still on legacy commitment agreements yet to transition.
- **Embedded AI**: ACE agent, ComplianceWise (agentic Oct 2025), Classification Assistant, Document Ingestion; usage 2–5x since launch; per-transaction pricing means AI grows revenue.
- **CTO (landside)** ACFS launch partner — FY2027+; **WMS Value Pack** per-order-line; **Neo** shipper portal (Web Tracker retired 1 Apr 2026); **ComplianceWise/CBAM** (certificate obligation ramps 2026→Feb 2027); **LatAm** (Editrade, Opentecnología).

### E2open synergies
- **INTTRA** (~18.5% of global ocean bookings) + **Bolero eBL** → documentary/trade-finance automation — shipped 2026 (most concrete synergy).
- Cross-sell CargoWise execution/customs into ~5,600 E2open shippers (250+ blue-chip); cross-sell E2open GTM/planning into forwarders.
- Combined compliance: Amber Road GTM (~68B annual restricted-party screenings, 230+ jurisdictions) + ComplianceWise.
- **US$50M cost synergy achieved Jan 2026 (~18 months early)**; E2open EBITDA 34% ex-restructuring (+6pp vs. pro forma) in 5 months; 1H26 E2open revenue $249.4M.
- **FY2026 group guidance** (reaffirmed 25 Feb 2026): revenue US$1.39–1.44B, EBITDA US$550–585M (40–41% margin), exit run-rate 43–44%.

## Contradiction Check

Run adversarially, per the closing check in [[Generalist - Overview]]:

1. **The "contained cascade" read may be the bull anchoring on its own house aesthetic.** The self-build graveyard is real, but it is history; AI has since lowered the execution-rebuild cost, and DSV has now *demonstrated* a scaled forwarder can run off a proprietary stack. "It failed before" is a weak base rate if the underlying cost curve has moved. The honest position: the *execution* layer is more contestable in 2026 than in 2015, even if no second forwarder is evaluating yet.
2. **The single falsifying datapoint** (already the thesis's → LOW trigger): a second top-10 *core* forwarder — realistically a shipping-line integrator (CMA CGM/CEVA or Maersk) with vertical-integration logic — publicly evaluating migration. Untripped July 2026, but CEVA/CMA CGM is the credible tail path and warrants monitoring.
3. **Value Packs is a two-sided bet, not a clean positive.** The ~+6% revenue uplift and the concentrated churn exposure are the *same* fact: the price increase lands hardest on the ~30% legacy cohort that is also the most self-build-capable. If pushback spreads (mid-market demo surge at GoFreight/Magaya/Riege is real; a June 17 2026 CargoWise outage reignited support-quality concerns while WiseTech cuts up to 50% of product/support headcount), the uplift and the churn could arrive together.
4. **The retention metric cannot see the risk.** "<1% attrition" excludes non-CargoWise accounts and counts churn only after ≥4 months of zero use — a slow migrator (DSV, still +20% volume on ~70% un-migrated) never registers. The bull's favorite number is structurally blind to a slow enterprise bleed; do not treat continued <1% attrition as evidence the cascade is not happening.
5. **Base rate on E2open revenue synergies**: no named cross-sell win disclosed yet; the $30–50M/yr figure is analyst estimate, not company guidance. Enterprise cross-sell cycles run 18–36 months — 2026 synergy revenue is likely back-half-weighted into FY2027+. Treat the two-node moat as a durability *hypothesis* pending a disclosed cross-sell win.

## Source Excerpts

> WiseTech (9 Jul 2026 ASX clarification): DSV CargoWise volumes +20% over six months, users +3%; contract to September 2028; renewal talks underway. (Loadstar; TipRanks; Capital Brief; Rask Media; Motley Fool AU)

> DSV Capital Markets Day (12–13 May 2026): "CargoWise One → Tango" (Air & Sea); "Star" for Road (25+ systems); ~25% of volumes on Tango; broad rollout 2027; ~DKr9bn productivity by 2030 (~DKr6bn AI+technology / ~DKr3bn network). (GlobeNewswire primary; Air Cargo News; The Loadstar)

> Jens Lund (DSV CEO): "it's very likely that we will, over time, gravitate towards our own solution." (Loadstar / Transport Intelligence)

**Key primary anchors**: WiseTech 1H26 results (25 Feb 2026, ASX release + presentation + scripts); DSV Capital Markets Day (12–13 May 2026, GlobeNewswire); WiseTech "Clarification regarding relationship with DSV" (9–10 Jul 2026); Capgemini/DB Schenker Tango case study; E2open acquisition investor presentation (26 May 2025). FY2026 full-year results due 26 Aug 2026.

*Sourcing caveat: The Loadstar (primary trade outlet on the DSV story) hard-blocks fetching (HTTP 403); its verbatims here are via search snippets/mirrors cross-checked across multiple outlets and WiseTech/DSV primary filings. GEODIS's current TMS posture and DSV's exact CargoWise spend remain unverified.*
