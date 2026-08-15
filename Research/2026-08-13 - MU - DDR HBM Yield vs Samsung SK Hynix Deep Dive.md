---
publish: false
date: 2026-08-13
tags: [research, deep-dive, MU]
sector: DRAM & HBM Memory
ticker: MU
source: vault synthesis
source_type: deep-dive
propagated_to: [MU, 000660]
---

# MU — DDR DRAM and HBM Yield vs Samsung and SK Hynix

## Thesis Delta

[[Theses/MU - Micron Technology]] §Industry Context had no yield table. The missing number is not a hidden MU advantage: **Samsung HBM4 headline stack yield printed ~80% on 10 Aug (from <60% at Feb MP); SK Hynix HBM4 is also ~80%; Micron has no public HBM4 %.** DDR/1c die yield is table-stakes (>80% at both Koreans; MU 1β/1γ undisclosed). Yield parity at the Korean pair **removes yield as the excuse for MU's empty first-wave Rubin slot** — it does not fill the slot. Conviction unchanged (low). 000660's kill (Samsung >35% Rubin) is the file that moves on the Samsung 80% print, not MU.

## Summary

Vendors do not publish a single comparable "yield." Three different numbers travel under that word: (1) front-end DRAM die yield on the latest node (1c at Samsung/SKH, 1β/1γ at Micron); (2) headline HBM stack yield after TSV + bonding + final test; (3) reliability-test yield on the next SKU (Samsung HBM4E >70%). Headline ≠ effective. Effective stack yield is (die yield)^N × TSV × microbump × base-die × stack test; at 16-Hi, 95% per-die still compounds to ~44% ([[Sectors/DRAM & HBM Memory]] §Yield Deltas).

On the current public tape (as of 13 Aug 2026): Samsung and SK Hynix have both reached the industry's "golden" **~80% HBM4 headline stack yield**. Samsung did it in six months of TC-NCF + 1c die-yield work (Sedaily / TrendForce 10 Aug). SK Hynix is there on mature MR-MUF (Infostock Daily). Micron's HBM4 12H 36GB ships on **1β**, not 1γ, and IR will only say "mature yields faster than HBM3E" and "high-yield ramp" for Q2 calendar 2026. No percentage. Late-2025 vault modelling (50–70% once ramped) is a scenario, not a 2026 measurement. HBM3E-era colour — SemiAnalysis calling MU HBM margin-accretive, 12-Hi yields beating 8-Hi — is the closest public MU signal, and it is a cost/margin read, not a Rubin attach print.

On DDR/commodity die yield the picture is the same shape. SK Hynix 1c cleared 60%→>80% by April 2025 and is the vault's ~80–90% working range. Samsung 1c die yield is **>80%** as of early 2026 (ETNews via TrendForce 10 Aug), with 1b already >80% at both Koreans (Chosun 24 Feb). Micron prints **no die-yield %** on mature 1β or ramping 1γ (16Gb LPDDR5X in HVP; 256GB DDR5 RDIMM sampled). 84.6% FQ3 blended GM is consistent with a mature 1β commodity book plus HBM mix; it is not a 1γ or HBM4 stack-yield disclosure. CXMT is the only named DRAM name still off the mature-yield standard (HBM3 8-Hi modelled ~25% overall).

## Evidence

| Layer | SK Hynix | Samsung | Micron | Source |
|---|---|---|---|---|
| HBM4 headline stack yield | **~80%** | **~80%** (from <60% Feb MP) | **no public %** | Sedaily 10 Aug; Infostock Daily via [TrendForce 10 Aug](https://www.trendforce.com/news/2026/08/10/news-samsungs-hbm4-yield-reportedly-hits-80-as-race-to-supply-vera-rubin-heats-up-sk-hynix-labor-talks-add-a-twist/); [[Research/2026-08-12 - 000660 NVDA AMD - Samsung HBM4 Golden Yield 80pct - news]] |
| HBM4E / next-SKU | MR-MUF through 16-Hi | Reliability-test yield **>70%**; 12H samples late May for Rubin Ultra | HBM4E on 1γ + TSMC base-die, volume CY27 | Sedaily / Wccftech 10 Aug; MU 16 Mar IR |
| HBM3E (prior, for MU colour) | ~80% (MR-MUF; sector working number) | ~50% pilot then catch-up; thermal/noise miss was stack-level, not die | 12-Hi yields > 8-Hi; SemiAnalysis: HBM **margin-accretive** (same bucket as SKH) | [[Sectors/DRAM & HBM Memory]]; [SemiAnalysis 11 Aug 2025](https://newsletter.semianalysis.com/p/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm); ZDNet via TrendForce Aug 2025 |
| Latest-node DRAM die (DDR5 / HBM core) | 1c **>80%** (60%→80% by Apr-25); vault ~80–90%; 1b >80% | 1c **>80%** early 2026; 1b >80% | 1β mature, 1γ ramping — **both undisclosed** | TweakTown/Hanhooki Apr 2025; ETNews via TrendForce 10 Aug; Chosun 24 Feb 2026 |
| Packaging | Advanced MR-MUF | TC-NCF (cited as the HBM4 yield driver alongside 1c) | TC-NCF pragmatic; in-house CMOS base-die (not TSMC N12 / SF4) | TrendForce 10 Aug; SemiAnalysis ISSCC 2026 |
| Rubin first-wave bits | ~70% | ~30% | **~0%** | Thesis / [[Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive]] |
| HBM4 share read | Trimmed in TrendForce June vs prior | Raised sharply on qual + shipments | **"relatively stable given limited HBM4 exposure"** | TrendForce 10 Aug |

**Definition check (do not mix columns).** Chosun (24 Feb 2026) is explicit that 12-Hi stacking makes die yield the binding input: if 1c die yield is weak, stack yield cannot print 80%. Samsung's Aug HBM4 80% print is therefore a *joint* claim — 1c die already >80% *and* TC-NCF stack yield at golden. Micron's HBM4 is on **1β**, so its die-yield problem (if any) is a mature-node problem, not a 1c-ramp problem. The public silence is still silence.

**MU IR quotes (no percentage attached).**

- FQ2-26 materials: "With our HBM4 production ramp and volume shipments underway, we expect to reach mature yields faster than HBM3E."
- Dec-25 earnings (TrendForce 9 Jan 2026 recap): HBM4 on 1-beta, >11 Gbps, "on track for high-yield ramp-up in the second quarter of 2026"; base logic and DRAM core dies designed and manufactured in-house.

**Stale numbers to retire.** Sector §Yield Deltas "Samsung ~50% pilot / MU 60–70%" is HBM3E-vintage. Feb 2026 SemiWiki "Samsung 1c stuck ~60%" is superseded by ETNews 1c>80% + Sedaily HBM4 80%. [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]] Samsung 1c ~50% / MU HBM4 50–70% modelled is late-2025.

## Contradiction Check

Does **not** challenge MU's core variant (qualified third ≠ allocated; first-wave ~70/30/0 until Q3 meter). It **eliminates a competing explanation**: that MU is off the board because its HBM4 yield is the documented laggard. The documented laggard on HBM3E was Samsung; Samsung has now printed golden yield on HBM4 and already holds the dual-source slot (AMD MI400 attach is live). MU's empty slot after a Korean yield tie is allocation / pin-speed, or capacity (TrendForce: limited HBM4 exposure), not a measured Nvidia yield reject.

Does **not** promote MU. Samsung 80% is a [[Theses/000660 - SK Hynix]] kill-window input (Samsung >35% Rubin), already ingested 12 Aug. Yield parity at 80%/80% is the dual-source condition the 000660 thesis named; it is not a MU HIGH-leg.

**Falsifiers for this note's yield table:** (1) MU IR or a channel print of HBM4 stack yield — any number. (2) A teardown / Nvidia comment that cites MU pin-speed or stack-yield as the reject (converts the hypothesis into a measured fact). (3) Samsung HBM4 80% revealed as die-only, not stack (would reopen the 30-point effective-yield gap). (4) Two TrendForce DRAM prints −20%+ with rising OEM days — destock analog, orthogonal to yield.

## Framework / Mental Model

- **Industry #2 · qualification-gate** — hypothesis: once all three are qualified, remaining scarcity is allocation. Aug-26 80%/80%/undisclosed print is the test: yield is no longer the discriminator at the Korean pair; MU's 0% first-wave survived the yield catch-up. Held as hypothesis, not verdict.
- **Industry L1 · DRAM less cyclical** — not tested by yield prints. HBM LTAs lengthen the queue; they do not retire destock.
- **Automation · tacit yield knowledge** — Samsung closed ~20pp of HBM4 stack yield in six months once 1c die yield was there. Hypothesis: the 12-year MR-MUF learning-curve moat is shallower at HBM4 than HBM3E once the die node is mature; catch-up is possible inside a year. Does not retire tacitness (still un-serialisable); it bounds how long the gap lasts.
- **[G-10] base rates / [G-3] mean-reversion vs trend** — agreement still cues disconfirm. Peak GM + peak capex + peak price have not held 24 months. Yield catch-up is the mid-cycle competitive mean-reversion *inside* the cycle, not evidence the cycle itself has been retired.

## Source Excerpts

> "Samsung Electronics' HBM4 yield has recently approached the 80% mark, moving close to achieving a 'golden yield.' The yield, which stood below 60% in the early stages of mass production this February, has soared to its original year-end target within half a year." — Sedaily via Wccftech / TrendForce, 10 Aug 2026

> "Samsung had already pushed 1c DRAM yields above 80% early this year, establishing a stable production base that has helped lift HBM4 yields." — ETNews via TrendForce, 10 Aug 2026

> "Infostock Daily notes that industry insiders estimate SK hynix's HBM4 yield has already reached the 80% range." — TrendForce, 10 Aug 2026

> "Micron's share is likely to remain relatively stable given its limited HBM4 exposure." — TrendForce, 10 Aug 2026

> "With our HBM4 production ramp and volume shipments underway, we expect to reach mature yields faster than HBM3E." — Micron FQ2-26 IR

> "For SK and Micron, yield loss is more than made up for by high pricing, and hence, HBM is margin accretive. For Samsung, yields are even worse." — SemiAnalysis, 11 Aug 2025 (HBM3E-vintage; Samsung HBM4 print supersedes the Samsung half)
