---
date: 2026-04-01
tags: [research, crypto, MSTR, preferred-stock, capital-structure]
status: active
sector: Consumer & Digital
source: ChatGPT conversation export (Conv 99)
---

# Strategy (MicroStrategy) Preferred Stock Capital Stack Analysis

## Summary

Breakdown of Strategy Inc.'s (formerly MicroStrategy) complete capital stack across its 5 publicly traded securities: MSTR (common), STRK, STRF, STRC, and STRD. These instruments sit at different points in the capital stack and trade off upside vs income vs seniority. Understanding the stack is critical for evaluating bitcoin exposure vehicles and corporate bitcoin treasury strategies.

## Capital Stack Hierarchy

**Debt > STRF > STRC > STRK > STRD > MSTR/common**

This ordering is inferred from the stated senior/junior relationships in Strategy's offering documents. All securities are below existing and future indebtedness, and all preferreds are structurally junior to subsidiary liabilities.

## Security-by-Security Breakdown

### MSTR — Common Stock
- **Position**: Bottom of stack
- **Dividend**: None; Strategy has never paid cash dividends on common stock and does not intend to
- **Character**: Purest exposure to Strategy's residual upside and downside
- **Use case**: Maximum upside/downside; leveraged bitcoin exposure through corporate balance sheet

### STRK — Series A Perpetual Strife Preferred Stock (Convertible)
- **Position**: Above STRD and MSTR; below STRF, STRC, and debt
- **Dividend**: 8% fixed; cumulative
- **Payment**: Cash, MSTR shares, or a mix (at company's discretion)
- **Conversion**: Each share convertible into 0.1 shares of MSTR
- **Character**: Hybrid — income plus upside participation if common stock rises
- **Use case**: Income with some equity optionality

### STRF — Series A Perpetual Strife Preferred Stock (Senior Fixed)
- **Position**: Senior-most preferred; above STRC, STRK, STRD, and common; below debt and subsidiary liabilities
- **Dividend**: 10% fixed, paid quarterly in cash; cumulative
- **Protections**: Missed payments trigger step-up penalties; governance rights activated on non-payment
- **Character**: Most defensive preferred in the stack
- **Use case**: Safest preferred; prioritise income protection and seniority

### STRC — Variable Rate Series A Perpetual "Stretch" Preferred Stock
- **Position**: Above STRK, STRD, and common; below STRF and debt
- **Dividend**: Variable rate, adjusted monthly; **11.50% annualised as of April 2026**; paid monthly in cash; cumulative
- **Par value**: $100 stated amount; rate adjustment designed to keep price near par
- **Compounding**: Unpaid dividends can compound monthly
- **Collateral**: **NOT collateralised by Strategy's bitcoin holdings**; holders have preferred claim on residual assets
- **Character**: Highest current cash income with monthly reset and near-par design; described as "Short Duration High Yield Credit"
- **Use case**: Income-maximising with price stability near par; cash-flow focused investors

### STRD — Junior Preferred Stock
- **Position**: Most junior preferred; above common stock only; below STRF, STRC, STRK, and debt
- **Dividend**: 10% fixed, paid quarterly
- **Key risk**: Dividend is **non-cumulative** — if the board skips a payment, it does NOT accrue
- **Character**: Yield-focused but weakest preferred protections
- **Use case**: Yield-seeking investors willing to accept weakest structural protections

## Comparative Summary Table

| Security | Type | Dividend Rate | Frequency | Cumulative? | Seniority Rank | Key Feature |
|----------|------|--------------|-----------|-------------|----------------|-------------|
| **STRF** | Fixed preferred | 10% | Quarterly | Yes (+ step-up) | 1st (below debt) | Most defensive; governance rights |
| **STRC** | Variable preferred | 11.50% (Apr 2026) | Monthly | Yes (+ compounding) | 2nd | Near-par design; highest current yield |
| **STRK** | Convertible preferred | 8% | Quarterly | Yes | 3rd | Converts to 0.1 MSTR/share |
| **STRD** | Fixed preferred | 10% | Quarterly | **No** | 4th | Non-cumulative; weakest protections |
| **MSTR** | Common stock | None | N/A | N/A | 5th (last) | Pure bitcoin leverage |

## Decision Framework: "Which One to Own for Which View"

| Investor View | Best Security | Rationale |
|---------------|---------------|-----------|
| Bitcoin bull, want maximum exposure | **MSTR** | Pure equity upside; leveraged to BTC price |
| Want income + some BTC upside | **STRK** | 8% yield + conversion option to MSTR shares |
| Want safest cash flow, don't care about upside | **STRF** | Senior-most, cumulative with step-up penalties |
| Want highest current income, price stability | **STRC** | 11.50% variable monthly; near-par design |
| Want yield, comfortable with risk | **STRD** | 10% but non-cumulative — cheapest for a reason |

## Critical Observations

1. **No BTC collateral**: STRC (and presumably other preferreds) are NOT collateralised by Strategy's bitcoin holdings — a key misconception to dispel
2. **Variable vs fixed risk**: STRC's monthly reset means income fluctuates but price should track near $100; STRF/STRD fixed rates mean price volatility as rates move
3. **Non-cumulative trap**: STRD's non-cumulative dividend is a meaningful structural weakness — the board can skip payments without obligation to make them up
4. **Cumulative with compounding**: STRC's unpaid dividends compound monthly — this is a stronger protection than simple cumulative
5. **Structural subordination**: All preferreds are junior to debt AND subsidiary liabilities — in a distress scenario, recovery for preferred holders depends on bitcoin value far exceeding debt obligations

## Connections to Thesis

- Directly supports [[Theses/BTC-CRYPTO - Bitcoin & Digital Assets]] — Outstanding Questions section on leveraged BTC exposure vehicles
- Relevant to Strategy's 713,502 BTC position and corporate bitcoin treasury strategy discussed in thesis
- Complements institutional demand analysis: Strategy's preferred issuance is a mechanism for raising capital to acquire more BTC

## Source Notes

- ChatGPT conversation export; Q&A format comparing Strategy's full capital stack
- Data points from Strategy's offering documents and company website (April 2026)
- Ticker descriptions based on Nasdaq listings
