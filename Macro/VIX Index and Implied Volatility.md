---
date: 2026-04-02
tags: [macro, vix]
status: active
source: Claude conversation export
---

# VIX Index and Implied Volatility

## Original Query
> What is the VIX index, is it the IV of some index ?
> What are some risks buying vix index calls.

---

**Why it's called the "fear gauge":** The VIX tends to spike during sell-offs because demand for protective puts surges, driving up option premiums (and thus implied vol). It's structurally mean-reverting — it spikes sharply but tends to decay back toward a long-run average (historically around 18–20, though this shifts over regimes).

**The futures basis problem.** VIX options are priced off VIX *futures*, not VIX spot. This is the single most important thing to understand. If spot VIX is at 15 but the relevant futures contract is at 18, your call strikes are relative to 18, not 15. So even if spot VIX spikes from 15 to 22, the futures contract you're actually exposed to might only move from 18 to 21 — and your out-of-the-money call might still expire worthless. The futures tend to dampen the moves of spot VIX in both directions because they already price in some probability of a spike.

**Term structure matters:** VIX is the 30-day point, but the full term structure (VIXM for mid-term, VIX9D for 9-day, VIX3M, VIX6M) gives you a richer picture of how the market is pricing risk across horizons. A steep contango curve (longer-dated vol higher than near-term) is typical in calm markets; inversion signals acute near-term stress.

Great question — VIX calls are one of those instruments that seem intuitive ("buy calls on fear as a hedge") but have several structural quirks that can erode their value even when your directional read is correct.

More specifically, the VIX (formally the CBOE Volatility Index) measures the market's expectation of 30-day forward-looking volatility, derived from the prices of S&P 500 index options. It's calculated by the Chicago Board Options Exchange (Cboe) using a wide strip of both call and put options across multiple strike prices, weighted in a specific way to capture the market's aggregate expectation of volatility over the next 30 calendar days.

**The spike might not be big enough.** Because futures already embed some risk premium, you need a *larger-than-expected* spike to profit. A moderate VIX move from 15 to 25 in spot might translate to a much smaller move in the futures — not enough to overcome the premium you paid.

**Tradability:** You can't trade the VIX spot directly. VIX futures, options on VIX futures, and ETPs like VXX or UVXY give you exposure, but they all have significant basis and roll dynamics (contango decay in particular) that make them poor long-term holdings and more useful as tactical hedges or short-vol trades.

**Contango decay works against you constantly.** In normal markets, VIX futures trade in contango (upward-sloping term structure). As expiration approaches, the futures contract rolls down toward spot — which is usually lower. This means the underlying your calls are based on is drifting lower over time even if nothing changes. You're fighting gravity.

**Practically speaking**, if you're thinking about this as a tail hedge alongside your geopolitical scenario work, a few alternatives worth considering: SPX put spreads give you more direct exposure to the actual drawdown you're hedging; VIX call spreads (rather than naked calls) reduce cost basis and are less sensitive to the futures basis issue; and sizing matters enormously — most institutional hedgers allocate a small, consistent premium budget rather than making large one-off bets on timing.

**What it actually measures:** It's not a simple average of individual option IVs. It uses a variance swap methodology — essentially aggregating the prices of out-of-the-money puts and calls across the entire strike spectrum to produce an expected annualized volatility figure. So a VIX of 20 implies the market expects roughly ±20% annualized movement in the S&P 500.

**Timing is nearly impossible.** VIX spikes are sudden and short-lived. The index can double in a few sessions then mean-revert within weeks. If you're even slightly early on your entry, you can watch your premium bleed away waiting for the catalyst. And if you're late, premiums are already inflated by the time you buy.

**Settlement mechanics.** VIX options are European-style (no early exercise) and settle to a special opening quotation (SOQ) on expiration morning, not to VIX spot or futures closing prices. The SOQ can diverge meaningfully from where you expect VIX to be, creating settlement risk.

Yes, exactly. The VIX is the implied volatility of the S&P 500 index (SPX).

A few key points worth knowing from an investment perspective:

Is there a specific angle you're looking at — hedging, vol trading, or using it as a macro signal alongside your geopolitical scenario work?

**Theta is brutal.** VIX calls carry high implied vol themselves (vol of vol), which means premiums are expensive. Time decay is aggressive, particularly for out-of-the-money calls. If the spike you're hedging against doesn't materialize within your timeframe, you can lose 100% of the premium quickly.

**Hedging correlation isn't perfect.** Even as a portfolio hedge, VIX calls don't track your actual portfolio losses linearly. A slow, grinding drawdown in equities (like a multi-month bear market) can happen with VIX staying only moderately elevated — you lose on the portfolio *and* on the hedge. VIX calls work best against sharp, sudden dislocations, not slow bleeds.

Want me to walk through the mechanics of any of these alternatives, or compare the payoff profiles?
