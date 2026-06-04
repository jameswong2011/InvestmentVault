---
date: 2026-05-29
tags: [research, earnings, synthesis, VICR, AEHR, 2802, 6857, AIXA, 6981]
status: active
sector: multiple
source: FMP earning-call-transcript API (Vicor, Aehr, Ajinomoto, Aixtron — latest 4Q each) + Murata IR verbatim transcripts (FYE-Mar-2026 Q1–Q4) + Advantest IR Q&A summaries / presentation notes (FYE-Mar-2026 Q1–Q4)
source_type: synthesis
---

# Earnings Transcripts vs Thesis — 6 Holdings (Murata, Vicor, Aehr, Ajinomoto, Advantest, Aixtron)

## Thesis Delta

Latest-4-quarter earnings transcripts pulled and read against each thesis. The operating cases hold across all six; the failures are in *specifics* — three headline numbers are wrong or mislabelled, and three theses lean on AI-necessity framing management has not yet confirmed.

| Name | Conviction | Core thesis | Verdict | Most material finding |
|---|---|---|---|---|
| [[Theses/6981 - Murata Manufacturing]] | high | AI-server + EV MLCC volume decoupling from smartphones | ✅ **Confirmed, reality ahead** | FY27 guide OP **+34.8% to ¥380B (~19% OPM)** on data-center mix — thesis only models 18% by FY28 |
| [[Theses/VICR - Vicor Corporation]] | high | VPD architecturally required for Rubin; ITC licensing rents | 🟡 Numbers confirmed, **2 framing overstatements** | "Rubin" said **0×** in 4 calls; licensing run-rate ~$60M w/ **new deals paused to 2027**, not "$300M locked through 2026" |
| [[Theses/AEHR - Aehr Test Systems]] | high | WLBI non-substitutable for AI accelerators | 🟡 Numbers confirmed, **1 overstated claim** | CEO: *"most ASICs are not burnt-in"* — adoption curve, not a mandate (also = TAM runway) |
| [[Theses/2802 - Ajinomoto]] | medium | Hidden ~95% ABF monopoly inside a food conglomerate | 🟡 ABF confirmed, **food framing contradicted** | Food *improving* (seasonings driving growth, frozen recovering), not "dragged by margin pressure" |
| [[Theses/6857 - Advantest]] | medium | HBM test-time step-function + V93000 monopoly | 🟡 Operating case intact, **3 specifics wrong** | "10K installed base by 2028" → actually **10K systems/yr capacity, "more likely CY2029"**; share **66%**, not 95% |
| [[Theses/AIXA - Aixtron]] | high | InP-photonics mix-shift; 800V second leg | 🟡 Mix-shift confirmed, **2 specifics contradicted** | FY26 guide is **€520M (−6.6%, "slightly down")**, not the "€560M guide raise" the thesis claims |

## Summary

This note synthesises ~24 earnings transcripts (latest 4 quarters per name) read against the six investment theses. The exercise was as much a **data-hygiene test as a thesis test**: FMP's transcript API had no coverage for Murata (neither the Tokyo line nor the ADR) and was ~13 months stale for Advantest (it stops at the April-2025 / FYE-Mar-2025 call, missing the entire FYE-Mar-2026 year on which the thesis is built). Both gaps were closed by going to primary IR — Murata publishes full verbatim Presentation + Q&A transcripts; Advantest publishes Q&A summaries plus presentation-with-notes. The Advantest gap mattered: assessing on the stale FMP data alone would have produced a materially wrong read, because the thesis's load-bearing claims (the 3K→10K capacity call, the share figures) are only testable against the FYE-Mar-2026 disclosures.

Three cross-cutting patterns emerge. **First, "AI-necessity" framing consistently outruns what management will say.** Vicor never utters "Rubin" across four calls despite the thesis leading with Rubin architectural necessity; Aehr's CEO says burn-in is *"early innings"* with most ASICs not yet burned in, against a thesis that frames WLBI as economically forced; Advantest's realised demand driver is SoC/AI-accelerator test, not the HBM4 test-time explosion that is its thesis's central non-consensus pillar. These are not thesis-breaks — each thesis already flags the relevant uncertainty in its Outstanding Questions — but four quarters of calls provide no management corroboration for the most-cited bull narratives.

**Second, several headline numbers are simply wrong or mislabelled** — the kind of error that survives because it sits in the Summary prose rather than the model. Aixtron's "FY2026 €560M guide raise (from €520M)" is backwards: €520M *is* the guide, stated three times, and management explicitly calls FY26 *"slightly down"* from €557M. Advantest's "expand from ~3,000 active systems to ~10,000 by 2028" conflates annual production capacity with installed base and ignores management's explicit slip to *"more likely into CY2029."* Vicor's "$300M of contractually-locked [licensing] revenue through 2026" conflates the $300.6M *backlog* number with licensing, when royalties run ~$60M annualised and new deals are paused until the 2027 ITC determination.

**Third — and offsetting — two bearish thesis framings are contradicted by *improving* reality, and the strongest confirmations come from the Japanese/German names.** Ajinomoto's food segment is accelerating (seasonings driving growth, frozen in recovery, full-year guidance revised up), not the drag the thesis describes; Murata's and Advantest's margins are running *ahead* of their theses (Murata FY27 OP +34.8% to ¥380B; Advantest FY26 gross margin guided ~63% vs thesis "58–60%"). Murata, Ajinomoto's ABF segment, and Aixtron's optoelectronics mix-shift each confirm the *core* of their case in management's own words — the contradictions are at the level of specific numbers and timing, not the central insight.

Net portfolio read: no thesis is broken by its transcripts; two (Aixtron, Advantest) carry factual corrections that should be made before the numbers are used in sizing; two (Vicor, Aehr) carry framing overstatements worth tightening; two (Murata, Ajinomoto) are confirmed with the data running ahead of the written case.

## Evidence

### 🟢 Murata (6981) — confirmed; margins running ahead of thesis
**Coverage:** 4 full IR transcripts, FYE-Mar-2026 Q1–Q4 (Jul'25 / Oct'25 / Feb'26 / Apr'26). Previously unassessable (zero FMP coverage).

**Confirmed:**
- AI-server MLCC pillar, verbatim: *"data center investment centered on AI servers is clearly entering a major expansion cycle"*; *"demand for server-related MLCCs is very strong"*; capacity *"will all be directed there."*
- 800VDC pillar, explicit: management describes *"800 volts input, down converts it to about 50 volts, and DCDC…to run GPUs and TPUs."*
- Small-case share *">50%, as planned"*; capacitor utilisation *"90% to 95%"*; FY25 actuals match thesis (rev ¥1,830B, OP ¥281B).
- **Ahead of thesis:** FY27 (FYE-Mar-2027) guide rev ¥1,960B (+7%), **OP ¥380B (+34.8%, ~19% OPM)**, driven by *"stronger data-center-related demand…capacity utilization and improved product mix."* The thesis only reaches ~18% OPM by FY28.

**Tensions (mostly thesis-acknowledged):**
- Capex guided ¥250B + an *"emergency additional capacity investment…for server-use MLCCs"* of ¥80B — far below the ¥550–700B/yr the thesis's demand-led bull case requires. The supply-capped (~24%-of-sales) path is the live near-term reality (thesis Outstanding Q#4). The "emergency" framing supports the structural-under-build narrative.
- Pricing still a **−¥105B** annual headwind, outrun by volume/utilisation/mix — not the uniform "firming" the prose implies.
- Narrative is AI/datacenter-dominated; EV/auto (a ~28%-of-revenue, 50%-share thesis pillar) gets little airtime — not contradicted, under-emphasised.
- Q3 carried a ¥43.8B SAW-filter/Resonant goodwill impairment (non-MLCC) the thesis doesn't mention.

### 🟡 Vicor (VICR) — numbers confirmed, two framing overstatements
**Coverage:** FMP, Q2-2025 → Q1-2026 (current).

**Confirmed:** Q1'26 rev $113M (+20.2% YoY), GM 55.2%, backlog $300.6M (+70% QoQ), book-to-bill >2x. Cited moat quotes accurate: *"1.5 millimeter, we're going thinner"*; *"800-volt to 6-volt is frankly ill conceived."*

**Contradicted / overstated:**
- **"Rubin" appears 0× across all four calls.** The thesis leads with "VPD structurally required for NVIDIA Rubin." Management references only generic *"hyperscaler customers"* / *"follow-on VPD customers"* (ASIC-led), and frames NVIDIA as setting specs for *suppliers* (plural: *"NVIDIA and Google asking suppliers to hit 3 millimeters"*) — consistent with multi-sourcing, not sole-source Vicor content.
- **Licensing "$300M locked through 2026" overstates reality.** Royalty revenue ~$15M/quarter (~$60M annualised); the $570M FY26 guide is *"based on conservative assumptions…we will not enter into new licensing agreements until our second ITC case gets its final determination in 2027."* The $300M in the transcript is *backlog*. The thesis's own forecast table correctly uses $60M — only the Summary/Insight prose is wrong.

### 🟡 Aehr Test (AEHR) — numbers confirmed, one overstated necessity claim
**Coverage:** FMP, Q4-FY25 → Q3-FY26 (current).

**Confirmed exactly:** bookings $37.2M, book-to-bill >3.5x, effective backlog $50.9M (record), GM 36.5%, FY26 guide $45–50M high side, Q4 non-GAAP profitability, H2 bookings $60–80M high side.

**Contradicted / softened:**
- Insight #2 ("WLBI structurally non-substitutable for AI accelerators above ~600W") is softer in management's words. CEO Erickson: *"most ASICs are not burnt-in"* (~5–20%), only *"maybe half"* of AI accelerators do burn-in, *"surprised at how many devices are not yet doing production burn-in,"* *"early innings."* It is an in-progress adoption curve, not a physics-forced mandate today — which also reads bullishly as TAM runway.
- Soft flag: the lead AI customer is *"taking longer than we originally expected."*
- Silicon photonics is *ahead* of the thesis framing — a real *"initial order for multiple high-power FOX-XP systems,"* not just the "design-in" the thesis describes.

### 🟡 Ajinomoto (2802) — ABF confirmed, food-segment framing contradicted
**Coverage:** FMP, through Q3 FYE-Mar-2026 (Oct–Dec 2025, reported Feb'26). The thesis's headline FY2025 actuals come from the May-7-2026 full-year release — *after* the latest available transcript.

**Confirmed (ABF / Functional Materials):** Q3 segment sales +42%, profit ~+57% (+¥5.3B); full-year ABF guided +28% (actual landed +31%); *"Sales of ABF for high-performance boards used in AI servers and networks have been performing strongly, leading us to revise our initial growth plan upward"*; Gunma facility online Oct 2025 producing ABF for cutting-edge applications.

**Contradicted:**
- The thesis says food is *"dragged by margin pressure in Asian seasonings and US frozen foods."* Management reports the opposite: Japan + overseas seasonings *driving* sales/profit growth, frozen foods in a *"profit recovery phase…steadily improving,"* food business meeting/beating plan, full-year forecast revised **up**.
- Nuance: the headline profit upward-revision was partly a one-time *"gain on partial sale of fixed assets,"* not pure operating strength.

### 🟡 Advantest (6857) — operating case intact, three specifics wrong
**Coverage:** Round 1 used stale FMP (FYE-Mar-2025). Round 2 pulled FYE-Mar-2026 Q&A + notes from Advantest IR — the year the thesis is actually built on.

**Confirmed:** record FY results (Q4 rev ¥328B, EPS ¥174.55 vs ¥138.67 expected); FY26 *"record highs,"* tester market >$9B; share *gaining*; demand AI-driven. **Favourable miss:** FY26 gross margin guided **~63%**, above the thesis's "58–60%" trajectory.

**Contradicted / mislabelled:**
- **"3,000 → 10,000 installed base by 2028"** is a mischaracterisation. Management describes annual **production capacity** stepping 5,000 → 7,500 → **10,000 systems/year**, *"targeting to be ready by the end of CY2028, but more likely into CY2029."* Capacity-per-year ≠ installed base, and the date slips.
- **Share is 66%, not 80%/95%.** *"Our market share is estimated to have risen to 66%, an increase of around 10 percentage points…In the AI accelerator market…a majority share."* The thesis's "80% high-end logic / 95% HBM final test" are sell-side sub-segment estimates management does not corroborate (consistent with the ">60% memory" figure from the April-2025 call).
- **The HBM4 14–18h test-time pillar is not corroborated**, and the realised demand driver / capacity step-up is **SoC/AI-accelerator test**, not HBM memory test. Tokyo Seimitsu MoU and the "services >30% by FY27" target do not appear in the quarterly docs. Stock fell on conservative top-line guidance (consistent with the thesis's multiple-risk framing).

### 🟡 Aixtron (AIXA) — mix-shift confirmed, two specifics contradicted
**Coverage:** FMP, FY2025 Q1–Q4 (latest = FY25 results, Feb-26-2026). The thesis's "Q1 2026 65% opto orders / −38% EBIT" reference the Apr-30-2026 call, *after* the latest transcript.

**Confirmed (core mix-shift):** optoelectronics = **23% of FY25 equipment revenue** (exact match); guided to *"more than double year-over-year…into 2026"*; 150mm InP transition and *"photonics orders have significantly increased."*

**Contradicted:**
- **"FY2026 €560M guide raise (from €520M)"** is wrong. The actual guide is **€520M ±€30M** (stated three times; GM 41–42%, EBIT 16–19%), and management explicitly frames it as *"slightly down numbers from the…€557 million we had in '25"* — a ~6.6% decline, not a raise. This undercuts Insight #1's framing that the mix-shift is "mechanically driving the FY2026 guide raise."
- **800V second leg pushed out.** Thesis times data-center GaN orders for "late 2026 / 1H 2027." Management: *"800-volt GaN ramp is really starting, we are not there yet,"* and the power market is *"still some time out into the future,"* a *"'27, '28, '29 cycle."*
- Minor: app-split is 57% power / 15% LED (thesis says 50% / 22%); Q1'26 guided ~€65M (thesis assumed €100–110M); FY25 order intake €544M *"slightly weaker than last year."*

## Contradiction Check

Explicit list of thesis assumptions the transcripts contradict, with the section each hits:

| # | Thesis | Assumption (location) | Transcript reality | Severity |
|---|---|---|---|---|
| 1 | Aixtron | "FY2026 €560M guide raise (from €520M)" (§Summary, Insight #1) | FY26 guide €520M ±€30M, "slightly down" from €557M | **High** — factual error, load-bearing |
| 2 | Advantest | "~3,000 → ~10,000 installed base by 2028" (§Summary, §Key Metrics) | 10,000 systems/yr *capacity*; ready "more likely CY2029" | **High** — metric + timing error |
| 3 | Advantest | "~95% HBM final test / ~80% high-end logic share" (§Summary, §Key Metrics) | 66% overall (+10pp); "majority" in AI accelerators | Medium — uncorroborated; mgmt more modest |
| 4 | Vicor | "$300M licensing locked through 2026" (§Summary, Insight #2) | ~$60M annualised; new deals paused to 2027 | Medium — prose vs. own model ($60M) |
| 5 | Ajinomoto | Food "dragged by margin pressure in Asian seasonings / US frozen" (Insight #1) | Seasonings driving growth; frozen recovering; FY guide raised | Medium — directionally reversed |
| 6 | Aixtron | 800V second leg lands "late 2026 / 1H 2027" (Insight #5, Bull Case) | "Not there yet…some time out"; "'27–'29 cycle" | Medium — timing slip |
| 7 | Aehr | WLBI "structurally non-substitutable" for AI accelerators now (Insight #2) | "Most ASICs not burnt-in"; "maybe half" of accelerators; "early innings" | Low–Med — adoption curve, cuts both ways |
| 8 | Vicor | Rubin architectural-necessity → Vicor content (§Summary, Insight #1) | "Rubin" 0× in 4 calls; demand ASIC-led; NVIDIA multi-sources | Low–Med — uncorroborated, thesis flags it |
| 9 | Advantest | HBM4 14–18h test-time step-function (§Summary, Insight #1) | Not stated; realised driver is SoC/AI accelerators | Low–Med — forward call, not yet visible |

**Confirmations worth recording (reality at/ahead of thesis):**
- Murata FY27 OP guide **+34.8% to ¥380B (~19% OPM)** vs thesis ~18% by FY28 — margin ramp early.
- Advantest FY26 gross margin **~63%** vs thesis "58–60%" — under-modelled.
- Ajinomoto ABF full-year **+31%** (guided +28%), growth plan revised up — segment ahead.
- Aixtron optoelectronics guided to **"more than double"** into 2026 — mix-shift intact.
- Aehr silicon-photonics converted to a **systems order**, ahead of the "design-in" framing.

**Data-hygiene finding:** FMP transcript coverage is unreliable for non-US listings — zero for Murata, and a full year stale for Advantest (its API returns FYE-Mar-2025 as the latest, silently). Both required primary-IR retrieval. The Advantest staleness specifically would have produced a wrong assessment of its live thesis. (Separately, the `/transcript` skill's Step 0.4 API-key extraction uses `sed` with `\s`, which fails on macOS BSD `sed` and captures the whole config line as the key — it would break on this machine; the Live Portfolio dataviewjs is fine because it uses `JSON.parse`.)

## Source Excerpts

> **Murata (FY27 guide):** "We will still face price declines and higher fixed costs, but stronger data-center-related demand should lead to gains in capacity utilization and an improved product mix, so we are also planning a 34.8% increase in operating profit to JPY380 billion."

> **Murata (800VDC):** "…800 volts input, down converts it to about 50 volts, and DCDC converts it to run GPUs and TPUs…"

> **Vicor (licensing pause):** "This guidance is based on conservative assumptions about our licensing practice, specifically that we will not enter into new licensing agreements until our second ITC case gets its final determination in 2027."

> **Aehr (CEO Erickson, burn-in adoption):** "I think on ASICs…I don't know if it's 20%, maybe it's 5%…so most ASICs are not burnt-in. I would say on the AI accelerators…maybe half… this is still at the kind of the beginning phases."

> **Ajinomoto (ABF + food):** "Sales of ABF for high-performance boards used in AI servers and networks have been performing strongly, leading us to revise our initial growth plan upward and expect a 28% increase in sales for the full year." / "Frozen Foods business shifted into a profit recovery phase in the third quarter and performance is steadily improving."

> **Advantest (capacity step, slip):** "We are now moving to a third step, which will be 10,000 systems per year which we are targeting to be ready by the end of CY2028, but more likely into CY2029." / "Our market share is estimated to have risen to 66%, an increase of around 10 percentage points from the prior year."

> **Aixtron (guide + 800V timing):** "We expect revenues to come in at EUR 520 million in a range of plus/minus EUR 30 million…" / "The 800-volt GaN ramp is really starting, we are not there yet, but then I expect to have these discussions with customers."

## Related Research
- [[Theses/6981 - Murata Manufacturing]] · [[Theses/VICR - Vicor Corporation]] · [[Theses/AEHR - Aehr Test Systems]] · [[Theses/2802 - Ajinomoto]] · [[Theses/6857 - Advantest]] · [[Theses/AIXA - Aixtron]]
- [[Research/2026-05-24 - 2802 vs 6857 - Competitive Comparison]] — Ajinomoto vs Advantest; AI-purity vs conglomerate-discount
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]] — sizing context for all six (Tier 4–5)
- [[Research/2026-05-26 - AEHR - Stress Test]] — prior adversarial test; this note's burn-in-adoption finding reinforces the moat-timing flag
- [[Macro & Technology/800VDC Adoption]] — the 800VDC forcing function referenced by Murata, Vicor, Aixtron theses
