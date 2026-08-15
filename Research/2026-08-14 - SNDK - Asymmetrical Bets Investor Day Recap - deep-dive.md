---
publish: false
date: 2026-08-14
tags: [research, NAND, SNDK, MU, HBF, memory]
sector: NAND Memory & Storage
ticker: SNDK
source: 'https://asymmetricalbets.substack.com/p/is-sndk-back-investor-day-recap'
source_type: deep-dive
propagated_to: [SNDK]
---

# SNDK Investor Day Recap — NBM Floors, Withheld Supply, HBF Tape-Out (Asymmetrical Bets)

## Thesis Delta
Consensus still prices [[Theses/SNDK - SanDisk]] as a late-cycle NAND tape at a memory-cyclical multiple — Asymmetrical Bets cites ~6x forward P/E, essentially the same as [[Theses/MU - Micron Technology]] — on the assumption that ~80% gross margin and ~50% FCF are peak-cycle prints that mean-revert once 2027 capacity arrives and customers walk long-term agreements the way they have in every prior NAND bust. This 14 August 2026 recap of the 13 August Investor Day implies the opposite mechanism: a New Business Model book of 10 agreements / 8 customers (3 hyperscalers), ~50% of FY2027 bits and ~two-thirds of FY2028 bits locked with bank-backed minimum guarantees, $93.9B of minimum revenue at floor prices, and management's claim that even the floor is an ~80% gross-margin company every year through the FY28–30 window — while BiCS could grow output per wafer 27% a year and SanDisk chooses to ship only mid-to-high teens. That is a step-function above the thesis's prior NBM book (~$42B / 5 agreements / >1/3 of FY27 bits) and above the "65%+ would be unprecedented" line; HBF die tape-out with 2027 samples is modeled at zero revenue in the FY30 plan, so any commercial ramp is free upside rather than a loaded estimate. Distinct from the same-day Daily Intel IR clip [[Research/2026-08-14 - SNDK - Investor Day 2026 FY28-30 Model - news]] (company PR, no Q4 print, no $93.9B floor dollars, no 27% wafer-output math, no 4-vs-8 GPU benchmark).

## Summary
Asymmetrical Bets treats the 13 August 2026 SanDisk Investor Day as "the most significant event for memory of this year." The stock rose 14% into the close. CEO David Goeckeler opened with the claim that he has "finally gotten to the starting line of where the real value creation is going to happen," grounding that confidence in a contract book that already secures half of fiscal 2027 and two-thirds of fiscal 2028 bits into multi-year contracts that include a minimum guarantee. The recap is organized as a six-part argument: the Q4 print that set the tape, the FY28–30 profitability model, the New Business Model mechanics, the supply-withholding math on the BiCS roadmap, the HBF product and consortium, and the author's own long-memory take with the historical LTA-walk-away caveat.

Nine days before the day, SanDisk reported Q4. Headlines in the recap: revenue $8.97B, up 51% quarter-on-quarter; non-GAAP gross margin 84.6%; EPS $39.25 versus a $30–$33 guide. The load-bearing sentence the authors isolate from the print — and the one they say "explains this full cycle" — is management's mix split: sequential revenue growth was about one-third volume and two-thirds price. NAND supply constraints are giving SanDisk pricing power; the floor prices locked into the new contracts determine how much of that power survives a downturn. That mix is the [[Mental Models/Industry - Semiconductors]] #7 shortage signature (units up + prices up) and sits well above the thesis's own pre-print Q4 guide of $7.75–$8.25B / 79–81% GM / $30–$33 EPS.

CFO Luis Visoso's FY2028–FY2030 framework is the day's second load-bearing block. Aggregating 2028 through 2030, management expects mid-to-high-teens revenue growth "consistent with [bit] growth," non-GAAP gross margin around 80%, non-GAAP operating margin 75%, OpEx about 5% of revenue, and 50% adjusted free-cash-flow margin after taxes, working capital, and capital spending. Asymmetrical Bets' inference from "revenue consistent with bit growth" is that the company is not modelling future price hikes — pricing stays roughly flat for three years, so the 80/75/50 stack has to be earned on mix, cost, and contract floors rather than another ASP spike. Goeckeler adds that mid-to-high-teens volume growth is a commitment and an input to "a whole fab strategy," and that they think it is "sustainable over long periods of time" when they look at the whole market. The authors extend Street revenue of $48.9B for FY27 and $58.3B for FY28 along management's CAGR to approximately $79B in FY30; at a 50% FCF margin that is ~$40B of annual FCF against a $227B market cap on the day of the recap. Visoso on cash return: "There is no trick. It's 100% of the cash. Excess cash will go back to shareholders." Last quarter the company generated $5 billion and returned $4.5 billion.

The New Business Model is the proposed stabilizer. A hyperscaler commits to a fixed volume of bits for a stated number of years; the trade is backed by financial guarantees at prices that have a floor; the customer gets supply security; SanDisk gets revenue insurance for the downturn. Visoso: these deals go to "the highest level of the companies," require board approval, and are negotiated with CFOs, treasurers, and CEOs. The live book is 10 agreements with 8 customers, 3 of them hyperscalers; minimum revenue at floor pricing is $93.9B; average contract length is around 4 years. Asked what happens to margins if spot prices crash to those floors, Visoso said that even at the lowest floor price, "at any point in time, we don't expect these to be below 80%... every single year over the period, we should be able to be, even at floor pricing, around 80%." The authors' one-line restatement: the downside scenario is an 80% gross-margin company.

Supply discipline is the mechanism that is supposed to keep those floors from being arbitraged away. Goeckeler walked the BiCS (Bit-Cost Scalable) roadmap on stage: through innovation, output per wafer can grow 27% a year, "which, by the way, tells you, you can't just release nodes whenever they're available. Otherwise you're going to flood the market with supply and you're going to have another 23' situation." The authors translate: the technology *could* grow output 27% a year; SanDisk chooses to ship mid-to-high teens; the gap is withheld supply for pricing. That is why most NAND growth through 2027 is framed as upgrading existing factories — each new process squeezes more storage out of the same wafer — rather than greenfield wafer starts. On the demand side, the fastest-growing AI workload cited is KV cache (the memory that lets a chatbot remember a conversation). SanDisk puts that workload at a zettabyte of storage by 2030. The recap defines a zettabyte as 1 trillion gigabytes, "nearly as much flash as the entire industry will ship this year (in phones, data centres, etc.)." Withheld supply plus a zettabyte-scale KV-cache call is the pricing argument in one paragraph. Adjacent to [[Macro & Technology/DRAM Memory Cycle - Duration, Peak Timing and Second-Order Effects]] and [[Sectors/NAND Memory & Storage]].

HBF is presented as HBM with NAND stacked instead of DRAM, at 8–16x the capacity. Announced ~1.5 years ago to a confused audience; the consortium now named is [[Theses/000660 - SK Hynix|SKHY]], Google, Tencent, and — updated the week of the recap — [[Theses/META - Meta]]. The benchmark the authors call "pretty insane": a coding agent on a 490-billion-parameter model, where "with four HBF GPUs we are able to match the performance of eight HBM GPUs." Mechanism: when KV cache outgrows HBM, the GPU fetches from slower memory and spends almost half its time waiting; HBF is sized so cache never has to leave. On timing, CTO Alper Ilkbahar: "I'm happy to share with you today that we actually taped out our first HBF memory die." First samples go to customers in 2027. None of this sits in the FY30 model — HBF is financed inside the already-guided opex and capex, and HBF revenue is modeled at zero, so a working product is free upside. The authors' second-order claim: when HBM ramped it absorbed DRAM production and made commodity DRAM scarce and expensive; if HBF ramps the same way, shorts in NAND names face an analogous squeeze. This is a different source and a fuller recap than the same-day tape-out clip [[Research/2026-08-14 - SNDK 000660 - HBF Die Tape-out 2027 Samples - news]]. Cross-links [[Theses/NVDA - Nvidia]] (HBM GPU comparison; the thesis already flags NVIDIA's ICMS/GIDS path as a route-around) and [[Theses/285A - Kioxia]] (shared BiCS / Flash Ventures wafer path).

The authors' own take leans on Melius's Ben Reitzes: he has been going to tech conferences and analyst days since about 1992 and has "never seen a company guide for a year three years out and be trading at less than three times that number." They agree. SNDK at ~6x forward P/E matches MU and, in their view, does not make sense versus WDC or STX even on growth alone. The honest bear they keep: every prior memory crash, customers found a way out of LTAs; [[Theses/000660 - SK Hynix|SKHY]] and others add new capacity starting in 2027; these floors have not faced a test. The bull they keep: if the company wanted to convince memory investors that the old cycle is gone, the proof would look like this — withheld supply, floor pricing, bank guarantees, upgrade-not-expand. Closing line: "We're long memory, and yesterday only reassured that."

## Framework / Mental Model
**New Business Model (NBM) — SanDisk Investor Day, as reconstructed by Asymmetrical Bets.** A named commercial architecture, not just a backlog number. Components: (1) **Committed volume** — the customer contracts for a fixed quantity of bits over a stated term (average ~4 years in the live book). (2) **Floor price** — structured pricing with a contractual minimum; spot can print above the floor, not below it, for contracted bits. (3) **Financial guarantee** — the trade is backed by bank / third-party guarantees, not a handshake LTA; Visoso says the packages require board approval and are negotiated with CFOs, treasurers, and CEOs. (4) **Bilateral insurance** — customer gets supply security in a shortage; SanDisk gets a revenue floor in a downturn. (5) **Margin claim at the floor** — management's application of the framework to the current book is that even the lowest floor still produces ~80% gross margin in every year of the FY28–30 window. Methodology: count agreements and customers (10 / 8, of which 3 hyperscalers), convert the book to a minimum-revenue dollar figure at floor prices ($93.9B), state bit-coverage by fiscal year (~50% FY27, ~two-thirds FY28), and then stress the P&L at the floor rather than at spot. Distinct from Evidence: Evidence records the current book's outputs; this section is the reusable test — a future NBM print is "more structural" only if coverage, guarantee quality, and floor-GM all hold, not if revenue merely rises.

A second, thinner framework sits on the supply side: **withheld-node release**. Goeckeler's 27% output-per-wafer capability versus a mid-to-high-teens ship target is an explicit choice not to release every node the moment it is available, because doing so recreates "another 23' situation." Application: attribute 2026–27 bit growth to factory upgrades (more bits per existing wafer) rather than new wafer starts; treat the 27-minus-teens gap as the pricing-support residual.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Event / stock reaction | Investor Day 13 Aug 2026; SNDK +14% on the day | [1×: Asymmetrical Bets] |
| Q4 revenue | $8.97B, +51% QoQ | [1×: Asymmetrical Bets] |
| Q4 non-GAAP GM | 84.6% | [1×: Asymmetrical Bets] |
| Q4 EPS vs guide | $39.25 vs $30–$33 | [1×: Asymmetrical Bets] |
| Q4 sequential mix | ~1/3 volume, ~2/3 price | [1×: Asymmetrical Bets] |
| FY28–30 revenue growth | mid-to-high teens, "consistent with bit growth" (implied flat ASP) | [IR] / [1×: Asymmetrical Bets] |
| FY28–30 non-GAAP GM | ~80% | [IR] |
| FY28–30 non-GAAP OM | 75% | [IR] |
| OpEx / sales | ~5% | [IR] |
| Adj. FCF margin | 50% after tax, WC, capex | [IR] |
| Street FY27 / FY28 revenue | $48.9B / $58.3B | [1×: Asymmetrical Bets] |
| Author FY30 revenue ext. | ~$79B (management CAGR extended) | [est.] [1×: Asymmetrical Bets] |
| Implied FY30 FCF | ~$40B at 50% FCF margin | [est.] [1×: Asymmetrical Bets] |
| Market cap cited | $227B | [1×: Asymmetrical Bets] |
| Cash return policy | 100% of excess cash | [IR] |
| Last-quarter cash | $5B generated; $4.5B returned | [1×: Asymmetrical Bets] |
| NBM book | 10 agreements, 8 customers, 3 hyperscalers | [1×: Asymmetrical Bets] |
| NBM bit coverage | ~50% FY27 bits; ~2/3 FY28 bits | [IR] |
| NBM min revenue at floor | $93.9B | [1×: Asymmetrical Bets] |
| Average contract length | ~4 years | [1×: Asymmetrical Bets] |
| GM at floor prices | ~80% every year in the period | [1×: Asymmetrical Bets] |
| BiCS output/wafer capability | 27% / year | [1×: Asymmetrical Bets] |
| Chosen bit-ship growth | mid-to-high teens (gap = withheld supply) | [1×: Asymmetrical Bets] |
| 2026–27 supply path | mostly upgrades of existing factories, not new wafer starts | [1×: Asymmetrical Bets] |
| KV-cache storage call | 1 zettabyte by 2030 (= 1 trillion GB; ~one year of industry flash) | [1×: Asymmetrical Bets] |
| HBF vs HBM capacity | 8–16x | [1×: Asymmetrical Bets] |
| HBF consortium | SKHY, GOOG, Tencent, META (META added the week of the recap) | [1×: Asymmetrical Bets] |
| HBF benchmark | 4 HBF GPUs match 8 HBM GPUs on a 490B-param coding agent | [1×: Asymmetrical Bets] |
| HBF KV-cache wait | GPU waits ~half the time once cache spills from HBM | [1×: Asymmetrical Bets] |
| HBF tape-out | first HBF memory die taped out (Ilkbahar) | [1×: Asymmetrical Bets] |
| HBF samples | 2027 to customers | [1×: Asymmetrical Bets] |
| HBF in FY30 model | $0 revenue; funded inside guided opex/capex | [1×: Asymmetrical Bets] |
| Forward multiple | ~6x fwd P/E, ≈ MU; authors contrast WDC / STX | [1×: Asymmetrical Bets] |
| Author stance | long memory; 2027 SKHY+ capacity and historical LTA walk-aways are the untested risk | [1×: Asymmetrical Bets] |

Prior vault NBM book for comparison (not this source): ~$42B minimum / 5 agreements / >1/3 of FY27 bits targeting >50%, per [[Theses/SNDK - SanDisk]] Industry Context. This recap's $93.9B / 10 agreements / 50% FY27 is the first dollar-and-count update since that $42B figure.

## Contradiction Check
**Supports** [[Theses/SNDK - SanDisk]] Insight #2 (margin trajectory is structural, not cyclical) and the Industry Context NBM paragraph — Visoso's "80% GM even at the floor, every year" plus $93.9B of guaranteed minimum revenue is the strongest contracted-markets evidence the thesis has received, and it lands on the exact #13 classification tension (true cyclical vs semi-cyclical) the Mental Models section called "the classification call of the whole vault." **Supports** Insight #1 (HBF as TAM creation) on process, not on revenue: tape-out + 2027 samples + a 4-vs-8 GPU benchmark + META joining the consortium, with FY30 HBF revenue still modeled at zero — which is consistent with the thesis's own "call option, not a 2030 revenue engine" framing and with [[Research/2026-07-12 - SNDK - Industry Context (Cost, HBF, Supply-Demand to 2030) Deep Dive]]. **Challenges** the thesis's caution that 65%+ GM would be unprecedented, the 2026-05-24 rebalancing "Tier 3 true cyclical, CUT" label, and the Mental Models disconfirming check that "no NAND vendor has held >70% GM for more than 3 consecutive quarters": the Q4 print at 84.6% and a three-year 80% floor-GM guide are an explicit bet against that base rate. **Challenges** the Catalysts line that still lists "HBF sampling milestone (H2 2026)" — Ilkbahar moved first samples to 2027, so the H2 2026 sample window the Outstanding Questions treat as a kill-switch has already slipped; the authors treat the slip as acceptable because the FY30 model does not need HBF. **Does not retire** Bear Case cycle-timing or Risk #2 (margin reversion): the authors themselves keep the historical LTA-walk-away record and flag [[Theses/000660 - SK Hynix]] / peer capacity additions from 2027 as the first real test the floors have not yet faced — that is [[Mental Models/Industry - Semiconductors]] #3 (capex-lagged supply response) and #7 (watch the second derivative when units still rise but price stops). **Supports** [[Theses/285A - Kioxia]] only as JV-roadmap color (BiCS upgrade-not-expand; Flash Ventures is the wafer path behind 27% output/wafer). **Does not touch** [[Theses/MU - Micron Technology]] Conviction Triggers (Rubin board meter / GM compression / DRAM destock) — the 6x-vs-MU multiple comparison is valuation color, not a named MU handle. **Does not touch** [[Theses/000660 - SK Hynix]] HIGH/LOW/CLOSE (Rubin HBM share / Samsung HBM4 / CXMT HBM). [[Theses/SNDK - SanDisk]] has **no formal Conviction Triggers section** (structural gap the thesis already flags; suggested HIGH in Mental Models was "NBM coverage >50% of FY27 bits at fixed pricing," which this source now claims as a fact, but that is not a registered trigger). [[Theses/META - Meta]] also has no Conviction Triggers; META-as-HBF-consortium is a named-observable add, not a trigger fire. **Does not** change conviction or status.

## Source Excerpts
> "as I stand here today, I feel like I've finally gotten to the starting line of where the real value creation is going to happen." — David Goeckeler

> "Sequential revenue growth came about one third from an increase in volume, and two thirds from an increase in price."

> "When you aggregate all of that for 2028 through 2030, we expect to grow revenue mid to high teens, consistent with [bit] growth... We expect non-GAAP gross margin to be around 80%. We expect non-GAAP operating margin to be 75%. How do we get there? We expect to spend about 5% in OpEx... And then you get to 50% adjusted FCF after paying for taxes, working capital, capital spending." — Luis Visoso

> "We're committed to this kind of mid to high teens volume growth. When we look at the whole market, we think this is sustainable over long periods of time... it's an input to a process of developing a whole fab strategy." — Goeckeler

> "There is no trick. It's 100% of the cash. Excess cash will go back to shareholders. You look at last quarter, we generated $5 billion. How much did we return to you? 4.5." — Visoso

> "These go to the highest level of the companies. They require board approval. We're talking to CFOs, we're talking to treasurers, we're talking to CEOs." — Visoso

> "Even at the lowest price, at the floor pricing, at any point in time, we don't expect these to be below 80%... every single year over the period, we should be able to be, even at floor pricing, around 80%." — Visoso

> "Through the application of innovation, we can grow output per wafer at a rate of 27% a year. Which, by the way, tells you, you can't just release nodes whenever they're available. Otherwise you're going to flood the market with supply and you're going to have another 23' situation." — Goeckeler

> "With four HBF GPUs we are able to match the performance of eight HBM GPUs."

> "I'm happy to share with you today that we actually taped out our first HBF memory die." — Alper Ilkbahar

> "I've been going to tech conferences and analyst days since about 1992, and I've never seen a company guide for a year three years out and be trading at less than three times that number." — Ben Reitzes, Melius
