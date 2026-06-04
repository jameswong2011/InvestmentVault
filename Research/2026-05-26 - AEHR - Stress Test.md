---
date: 2026-05-26
tags: [research, stress-test, AEHR]
sector: Semiconductor Capital Equipment
ticker: AEHR
source: vault synthesis
source_type: stress-test
propagated_to: [AEHR]
---

# 2026-05-26 — AEHR Stress Test

## Thesis Delta

The AEHR thesis carries `conviction: high` that no evidence in the note supports. The same note's Summary says "Conviction is medium"; the linked 2026-05-24 portfolio rebalancing classifies AEHR as a Tier-5 convex bet sized 1-2%; and seven Outstanding Questions — including the identity of the customer that is ~88% of revenue — remain open. The high tag was set 2026-05-22 for a position reason ("confirmed as Live Portfolio holding"), not an evidence reason. Stress test outcome: does **not** survive at HIGH; survives at MEDIUM as a downside-bounded convex bet. 5 of 7 bull assumptions rate 🔴.

## Thesis Vulnerability Summary

AEHR is a single-customer SiC-burn-in company whose revenue fell 43.7% YoY to $10.3M, re-rated +973% over twelve months on one quarter's bookings, and now trades ~28-40% **above** the highest published sell-side target ($86.91 vs Street-high Buy $62-68; Stifel Hold $29.50). The entire bull case is a forward bet that signed bookings ($37.2M, one quarter, ~88% one customer) convert into a $200M+ FY28 platform spanning four end markets. Every load-bearing input is unverified: the lead AI customer's identity and unit volume are unknown, the SiPh "kicker" is a single design-in with no systems revenue, the gross margin reset to 36.5% may be a permanent concession, and the moat is conceded to be qualification-time — not IP — at the exact moment the cluster flags ATE-incumbent entry into photonic/WLBI test as a live 2026-2028 event. The thesis fails not because the WLBI TAM is fake, but because HIGH conviction is priced on FY28 revenue that rests on facts the vault does not have.

## Evidence Against

*Idiosyncratic failure modes first (peers do not share these); cluster-wide valuation risk last.*

**1. The customer identity is unknown and the whole case rests on it.** ~88% of Q3 FY26 revenue is one undisclosed AI customer. Outstanding Question #1 concedes "the entire investment case rests on its design pipeline." The Feb 2026 $14M "follow-on" the thesis cites as validation is a **second order from the same customer** — it deepens single-customer dependence, it does not diversify it. No second *AI-processor* customer has been disclosed. The CLOSE trigger (lead customer is a hyperscaler captive shipping <100K units) is both unresolved and unobservable until the FY26 10-K footnote. Mental Model #10 in the 2026-05-24 rebalancing sides with the prosecution: anchor concentration here is "existential, not concentration risk."

**2. The "platform-not-customer" narrative is asserted, not demonstrated.** Insight #4 dismisses concentration as "the wrong thing to focus on" and predicts it "falls naturally" as SiPh/GaN ramp. Every concrete datapoint contradicts the prediction: 88% concentration, one repeat order from the anchor, one SiPh design-in still <5% of revenue. The observed facts are fully consistent with a one-customer SiC-replacement story dressed as a four-market platform.

**3. SiC — 30-40% of the book — is in a multi-year decline the thesis underweights.** The −43.7% YoY revenue collapse *is* the SiC drain. Yole sees SiC weak through 2027-2028 (OQ#4), versus AEHR's earlier 2026-recovery framing — i.e., management already misjudged this cycle once. A shrinking third of revenue is actively dragging the P&L while the AI leg is one customer deep. [[Sectors/MLCC & Power Semiconductors]] corroborates SiC ASP −30-40% on overcapacity with stabilization only "expected," not observed.

**4. The moat is qualification-time, not IP — and the cluster flags incumbent entry as imminent.** Risk #2 concedes the moat is "qualification time + installed base, not patent." The bridges already exist: Teradyne owns Quantifi Photonics (2023); Advantest and FormFactor already co-develop wafer-level HBM test. [[Sectors/Semiconductor Test Equipment]] Q10 and the [[Sectors/Photonic Metrology]] pinned callout both treat ATE-incumbent acquisition or organic build of photonic/WLBI test as a live **2026-2028** scenario, and explicitly flag "FOX-XP physics is not exotic… a determined Teradyne organic build is technically possible." Per the thesis's own Bear Case, an *announcement* (not a shipping product) re-rates the stock to ~$30. The "4-7 year qualification gap" is asserted with zero vault source.

**5. Valuation exceeds every target, and the HIGH tag was a position decision (idiosyncratic) layered on cluster-wide momentum risk.** At $86.91 the stock trades above the Street-high target and at 30-60x EV/sales on $50M revenue — Insight #5 admits this is "uninvestable on financials alone." The medium→high bump (2026-05-22 Log) reads "portfolio-wide alignment — confirmed as current Live Portfolio holding": a sizing reason, not new evidence. Two days later the 2026-05-24 rebalancing reclassified AEHR to a Tier-5 1-2% convex bet, "pre-chasm," Mental Model #18 (cycle-confused-with-structural) "at maximum risk." **Cluster-wide overlay:** the entire photonic/test convex tail (AEHR +973%, AIXA +337%, IQE, Sivers +1,682%, AAOI +915%) is momentum-extended; sister names FORM (130x P/E), LITE (115x), BESI (68x) all carry "valuation leaves no margin" bear cases. A hyperscaler capex pause in 2H 2026 compresses the whole cluster — and AEHR most violently, given $10M revenue quarters against a $2.94B market cap.

## Assumption Stress Table

| Bull Assumption | What Must Be True | Evidence For | Evidence Against | Fragility |
|---|---|---|---|---|
| Lead AI customer is high-volume (NVIDIA/AMD-class) | Annual accelerator volume scales >100K units | Feb 2026 $14M repeat order | Identity undisclosed; CLOSE trigger fires if captive hyperscaler <100K units (OQ#1) | 🔴 |
| Concentration disperses (platform-not-customer) | ≥2 new AI customers commit by FY27 | Bookings $37.2M, b-t-b >3.5x | 88% one customer; only repeat orders + 1 SiPh design-in observed | 🔴 |
| SiPh design-in converts to systems revenue | Hyperscale CPO volume ramps on bull timeline | March 2026 design-in; [[Theses/LITE - Lumentum]] confirms optical-test bottleneck real | Design-in only, <5% rev, CPO volume 2027-2028, ASP undisclosed (OQ#3) | 🔴 |
| Gross margin recovers to 45%+ | 36.5% was mix/underutilization, not concession | Mgmt framed as mix | May be permanent price concession to win $14M order (OQ#5); swings terminal FCF ~2x | 🔴 |
| Revenue ramps to $200M+ by FY28 | All four end markets scale; multiple → ~15x | Bookings momentum | 4x off $50M base; depends on every row above + equipment lumpiness | 🔴 |
| Incumbents stay out of WLBI | No Advantest/Teradyne announcement in window | No competing WLBI shipped to date | Moat = qual-time not patent; Teradyne-Quantifi + ATE M&A flagged live 2026-28; announcement alone re-rates to ~$30 | 🟡 |
| SiC stabilizes / stops dragging | EV-power demand troughs in 2026 | — | Yole: weak through 2027-28; −43.7% YoY; mgmt misread the cycle once | 🟡 |

**Score: 5 🔴 / 2 🟡 / 0 🟢.** A thesis with five red-rated load-bearing assumptions cannot carry HIGH conviction.

## Research Gaps

What the thesis does not know that a serious short seller would:

- **Lead AI customer identity and unit volume (OQ#1).** A short would run supply-chain attribution / channel checks; the vault has none. This is the single highest-information unknown and it is unresolved.
- **No Q3 FY26 earnings transcript note exists in the vault.** The entire thesis rests on one bookings print that has never been independently parsed (`/transcript` never run on AEHR). Bookings are non-binding for equipment and can be canceled or pushed.
- **No source for the "4-7 year qualification gap."** Repeated as fact across the thesis and sector notes; never evidenced.
- **SiPh systems-revenue conversion timing and ASP delta (OQ#3).** Design-in ≠ revenue; CPO volume is 2027-2028; one customer.
- **Whether hyperscalers solve infant-mortality at the design/process level (Risk #3).** Better DFM, in-fab burn-in, or package-level test improvements would structurally normalize WLBI demand after the Rubin generation — unexamined in the thesis.
- **Gross-margin bridge (OQ#5).** Mix-and-underutilization (recoverable) vs. permanent concession (not) is unresolved and determines whether terminal margin is ~25% or ~12-15%.

## Kill Trigger

**Primary (binary, resolves Jun-Jul 2026):** Q4 FY26 earnings or the FY26 10-K customer-concentration footnote discloses the lead AI customer as a single hyperscaler captive (Google TPU / AWS Trainium-class) with <100K-unit annual accelerator volume, **and** no second AI-processor order >$5M is booked. This collapses the volume-scaling pillar and the platform-not-customer pillar in one print. (The thesis already encodes this as one of six CLOSE triggers; the stress test elevates it to *the* binary.)

**Secondary (faster-acting, observable Jul/Dec 2026):** Advantest or Teradyne announces a native multi-wafer high-power WLBI roadmap or a photonic-WLBI acquisition at SEMICON West (Jul 2026) or SEMICON Japan (Dec 2026). Per the thesis's own Bear Case, the moat narrative compresses and the stock re-rates to ~$30 regardless of ship date.

## Contradiction Check

Steelman — what would make this short wrong:

- **The thesis's own HIGH trigger is observable within 6-8 weeks.** If Q4 FY26 (Jun-Jul 2026) discloses a second AI customer >$5M **and** GM recovers >42% **and** the FY27 guide implies ≥$80M, the platform-not-customer claim is validated and the bear's core (single-customer dependence) collapses. The bear case is time-boxed, not structural.
- **The optical-test TAM is real, not imaginary.** [[Theses/LITE - Lumentum]] (high conviction) and [[Sectors/Photonic Metrology]] independently corroborate that wafer-level optical/electrical test is the CPO yield-closure chokepoint and AEHR FOX-XP is genuinely positioned. Only the timing and AEHR's capture rate are contested.
- **The moat has empirically held.** No incumbent has shipped competing WLBI despite AEHR selling the value proposition since 2023; the qualification gap, while not patent-protected, has not been crossed.

Net: the short is strongest on **conviction level** (HIGH is unsupported today) and weakest on **terminal TAM** (the WLBI/CPO opportunity is credible). The disciplined resolution is a conviction downgrade HIGH→MEDIUM pending Q4 FY26, not a thesis closure. AEHR is a legitimate convex bet sized 1-2% (per the 2026-05-24 rebalancing); it is not a HIGH-conviction holding.

## Related

- [[Theses/AEHR - Aehr Test Systems]] — thesis under test
- [[Sectors/Semiconductor Capital Equipment]] — parent sector; Tier-3 satellite framing
- [[Sectors/Photonic Metrology]] — sub-cluster MOC; ATE-incumbent acquisition pinned callout
- [[Sectors/Semiconductor Test Equipment]] — Q10 ATE-photonic-test consolidation 2026-2028
- [[Theses/6857 - Advantest]] — incumbent that "has not entered WLBI" — the moat's expiry risk
- [[Theses/FORM - FormFactor]] — sister photonic-test pure-play; parallel valuation/concentration bear case
- [[Theses/LITE - Lumentum]] — SiPh demand driver; corroborates optical-test bottleneck
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]] — Tier-5 convex bet, 1-2%, Mental Model #18 at maximum risk
