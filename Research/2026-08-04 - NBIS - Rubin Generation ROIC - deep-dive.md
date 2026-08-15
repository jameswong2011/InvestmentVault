---
publish: false
date: 2026-08-04
tags: [research, deep-dive, NBIS, neoclouds, ROIC, vera-rubin]
sector: Neoclouds & GPU-as-a-Service
ticker: NBIS
source: vault synthesis (One Chart framework + Aug-2026 Vera Rubin cost data — Morgan Stanley / Foxconn / Tom's Hardware)
source_type: deep-dive
propagated_to: [NBIS]
---

# NBIS — Rubin Generation ROIC at Held Rental Rates

## Thesis Delta

Answers the question "what ROIC does the incoming Vera Rubin fleet earn if rental rates hold at prior levels, and what does that mean for earnings growth and *perceived* ROIC" — and surfaces a **thesis-changing input**: the Vera Rubin NVL72 rack has **roughly doubled in cost since the thesis was underwritten** (~$7.8–9.1M vs Blackwell GB300 ~$3.9–4.5M) on a **~435% memory-component price surge**, voiding the June [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]] premise that Rubin capex/watt was "barely up." Consequence: at held rental rates the Rubin tranche earns a **~0–9% accounting ROIC (below NBIS's ~15% neocloud hurdle)**, because memory-inflated depreciation (~$7.8B/yr per 1GW) consumes nearly all the revenue the cluster generates. Reported EBITDA and ARR keep hyper-growing (the base quadruples; each Rubin GPU delivers ~3.5× the FP8 FLOPS), so the **market's perceived ROIC — read off a 45% AI-cloud EBITDA margin and $7–9B exit-ARR growth — decouples from the real incremental return on the capital NBIS is actually deploying.** Feeds thesis **Insight #6** and sharpens **Outstanding Q#4** (margin durability) and **Bear Case #3** (margin compression). Held as hypothesis, not verdict — three live offsets (value-based pricing, prepayment-reduced net capital, useful-life extension) can pull the return back toward the hurdle.

## Summary

The user's assumption — "current rental rates remain consistent with prior levels" — is the pessimistic bound, and it is where the Rubin economics break. Neoclouds price GPU-hours; customers buy FLOPS. Rubin roughly doubles the capex per GPU (memory surge) while roughly tripling the FP8 FLOPS per GPU. If NBIS holds the **$/GPU-hour** rental flat onto Rubin (does not raise price to reflect the doubled capital), the extra depreciation lands entirely on NBIS and the incremental return collapses. If instead NBIS prices Rubin to **value** (~$9.6–12/GPU-hr, the ceiling the vault's "One Chart" framework already bounds), the return is preserved — but then rates are *not* holding at prior levels; they have roughly doubled on a $/GPU-hr basis (even as $/FLOP falls). The question therefore resolves into a pricing-power test: can NBIS pass a ~2× capex step-up into $/GPU-hr in a sold-out market, or does competition / hyperscaler bargaining hold rates near the prior level and crush the Rubin ROIC?

The arithmetic (below) says that at held rates a 1GW Rubin cluster — ≈ NBIS's entire YE2026 target — earns essentially nothing after depreciation, a **~0–9% ROIC** depending on rental rate and useful life, versus the ~15% mid-teens hurdle the sector requires. The **perceived-vs-real ROIC gap is the mispricing**: NBIS trades at ~14x FY26 EV/revenue and a ~2.7× premium to CRWV ([[Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison]]) as if it earns a durable, software-like return on capital, but the marginal dollar — the Rubin build that *is* the company's future — earns a hurdle-or-worse return that NVIDIA, the layer owner, can compress further by pricing the memory it monopolizes. The reported metric that hides this is EBITDA: it excludes the very depreciation that doubled. This is the classic growth-that-destroys-value trap — earnings compound while incremental ROIC sits below the cost of capital — and it is invisible to anyone anchoring on ARR growth or EBITDA margin rather than return on invested capital ([[Mental Models/Generalist - Overview|G-7]]).

The offsetting reality keeps conviction at medium, not lower: customer prepayment (Microsoft ~$7B + ~$4.8B deferred revenue) reduces NBIS's *net* invested capital, mechanically lifting ROIC on its own money; GPU useful-life extension to 7–8 years with cluster-resign gross margins >35% ([[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]) lengthens the revenue tail per capex dollar; and NBIS's 2026 build is still mostly cheaper Blackwell/Hopper, so the full Rubin capex intensity bites the *incremental* fleet in 2027+, not the current blended book. The held-rate case is a warning about the direction of the incremental return, not a claim that NBIS's reported ROIC is already zero.

## Framework / Mental Model

**Held-rate ROIC bridge (extends the "One Chart to Rule Them All" cost-floor / value-ceiling framework).** The June framework bounded neocloud pricing between a cost floor (~$4.92/GPU-hr for ~15.6% IRR) and a value ceiling (~$9.63–12.25/GPU-hr at $/FLOP parity) — computed at the *June* Rubin rack cost (~$4M). The August memory surge shifts the entire cost curve **up-and-left**: the same rack now costs ~2×, so the floor rental required to clear the hurdle roughly doubles. NVIDIA guidance/market chatter now pegs Rubin on-demand at **$6–10+/GPU-hr**, versus ~$4.90 in June — the curve has already moved.

The mechanism is [[Mental Models/Generalist - Overview|G-7]] (return on *incremental* invested capital is the variable that matters) crossed with [[Mental Models/Lens - Value Layer Monopoly]] (NBIS is a **layer-renter**, not a layer owner):

1. **Denominator doubles.** Rubin invested capital per GPU ≈ 2× Blackwell (memory is ~$2–3.2M of a ~$7.8–9.1M rack; GPUs ~$4M).
2. **Numerator is capped by the pricing decision.** Held $/GPU-hr → revenue per GPU roughly flat → return halves. Value-priced $/GPU-hr → return preserved, but rates have risen ~2×.
3. **The layer owner harvests the gap.** NVIDIA reprices the scarce memory (SOCAMM ~60% margin) and the rack; the neocloud's take-rate is bounded above by that decision. A supplier price increase "shifts the curve up-and-left," compressing neocloud IRR unless passed through.
4. **EBITDA hides it.** Depreciation is the line that doubled; EBITDA excludes depreciation. So the metric the market watches (EBITDA margin, ARR) is structurally blind to the capital intensity — perceived ROIC stays high while real incremental ROIC falls. This is also [[Mental Models/Generalist - Overview|G-10]] (abnormal ROIC fades toward the cost of capital on a schedule) and [[Mental Models/Generalist - Overview|G-13]] (the price embeds a high ROIC; the mispriced operating variable is Rubin incremental ROIC, not growth).

**Note — this is the inverse of the [G-11] intangibles adjustment.** For asset-light software, expensed intangibles *understate* invested capital and *overstate* ROIC's economics; here, EBITDA *excludes* very-real depreciation on a capital-*heavy* asset, so the headline margin *overstates* the economic return. Both errors mislead — opposite signs. NBIS is the capital-heavy case: honest measurement requires netting the depreciation, i.e. ROIC, not EBITDA.

## Evidence

**Vera Rubin NVL72 rack cost (Aug 2026, post memory surge):**

| Item | Figure | Source |
|---|---|---|
| VR NVL72 rack, total | **~$7.8M** (Morgan Stanley); up to ~$8.8M–9.1M (others) | Morgan Stanley / Tom's Hardware / Foxconn est. |
| vs Blackwell GB300 rack | ~$3.9–4.5M → **"nearly double"** | Morgan Stanley |
| Memory (HBM4 + LPDDR5X) per rack | ~$2.0–3.2M (**~435% memory price surge**) | wccftech / MarketScale |
| GPUs per rack | ~$4M (largest single component) | Futu / Foxconn breakdown |
| June "One Chart" premise (now stale) | capex/W "barely up" $37.4→$38.1/W; rack ~$4M | [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]] |

**1GW Vera Rubin deployment economics (Foxconn / Investing.com):**

| Item | Figure |
|---|---|
| All-in capex per 1GW | **~$47B** (GPUs, HBM, DRAM, NAND, networking, power, cooling, civil) |
| Racks per 1GW | ~3,557 (rack cost alone ~$32.3B) |
| GPUs per 1GW | ~256,000 (3,557 × 72) |
| Annual depreciation | **~$7.8B** (≈6-yr life; **6× the ~$1.3B/yr power bill**) |
| Compute efficiency | 2,520 PFLOPS FP8/rack (~3.5× Blackwell); 105.5 → 189.3 EFLOPS per $1B capex |

**Held-rate ROIC sensitivity (1GW cluster; ~$47B capex; ~256k GPUs; ~90% util ≈ 7,880 billed GPU-hrs/yr; cash opex power $1.3B + other ~$0.7B; 21% tax; vault estimate):**

| Rental $/GPU-hr | Annual revenue | ROIC — 6yr life (dep $7.8B) | ROIC — 8yr life (dep $5.9B) | Regime |
|---:|---:|---:|---:|---|
| **$4.90** (June floor / held) | ~$9.9B | **~0.1%** | ~3.4% | **Held — below hurdle** |
| **$6.00** (held-high) | ~$12.1B | ~3.8% | ~7.1% | **Held — below hurdle** |
| $8.00 | ~$16.1B | ~10.5% | ~13.8% | Approaching hurdle |
| $9.60 (value floor) | ~$19.4B | ~16.1% | — | Clears hurdle |
| $12.00 (value ceiling) | ~$24.2B | ~24.2% | — | Value-priced |

- **Read:** held rates (~$4.90–6/GPU-hr) → **~0–9% ROIC**, below the ~15% mid-teens neocloud hurdle. The return only clears the hurdle at ~$8–9.6/hr — i.e. rental ~1.6–2× the held rate, near the value ceiling. **Rates must *not* hold at prior levels for Rubin to earn its cost of capital.**
- **Earnings-growth decoupling:** at held $4.90/hr, cluster EBITDA (revenue − ~$2B cash opex) ≈ $7.9B on ~$9.9B revenue — an ~80% *gross* EBITDA margin (consistent with CRWV's ~85% pre-D&A) — while EBIT after the $7.8B depreciation ≈ $0. The business looks like a high-margin compounder on EBITDA and a zero-return one on ROIC, simultaneously.

**Rental-rate backdrop (does "held" mean falling?):**
- Current-gen on-demand (Jul 2026): H200 median ~$3.49–3.95/hr (range to ~$13.78); B200 avg ~$6.17/hr (low ~$3.35). Blackwell shipping → H200 softening through 2026.
- 1-yr H100 contract rebounded +40% (Oct'25 $1.70 → Mar'26 $2.35) — rates are demand-cyclical, not monotonically falling ([[Research/2026-06-03 - Neoclouds NBIS vs CRWV - deep-dive]]).
- NVIDIA/market Rubin guidance: **$6–10+/GPU-hr** on-demand (unofficial) — already above the June ~$4.90 floor, evidence the curve is repricing upward with cost.

## Addendum — 2026-08-04 same-day (user-directed): 5-year useful-life sensitivity

Original table used **6-yr** life (Foxconn-implied: $47B/GW ÷ ~$7.8B/yr dep) with an 8-yr Patel-extension column. Re-run at **5-yr** (dep $9.4B/yr):

| Rental $/GPU-hr | Revenue | ROIC 5yr | ROIC 6yr | ROIC 8yr |
|---:|---:|---:|---:|---:|
| $4.90 (held/floor) | $9.9B | **−3.2%** (EBIT −$1.5B) | 0.1% | 3.4% |
| $6.00 (held-high) | $12.1B | **1.2%** | 3.8% | 7.1% |
| $8.00 | $16.1B | 8.0% | 10.6% | 13.9% |
| $9.60 (value floor) | $19.4B | 13.4% | 16.0% | 19.3% |
| $12.00 (value ceiling) | $24.2B | 21.5% | 24.2% | 27.5% |

| Life | EBIT-breakeven rental | 15%-ROIC rental |
|---|---:|---:|
| 5yr | **$5.65/hr** | **$10.07/hr** |
| 6yr | $4.87/hr | $9.29/hr |
| 8yr | $3.90/hr | $8.32/hr |

**What changes at 5 years:**
1. **Held rates flip from sub-hurdle to value-destructive.** ~0–9% becomes **~−3% to +1%**; at the $4.92 June floor the cluster posts an outright operating **loss** (~−$1.5B/GW/yr) — not a low return, a negative one.
2. **The June cost floor no longer covers depreciation.** Accounting breakeven ($5.65/hr) sits *above* the old $4.92 IRR floor — at 5-yr life the floor itself must migrate to ~$8–10/hr. Of the projected Rubin on-demand band ($6–10+), the low end earns ~1%, the midpoint ~8%; **only $10+ clears the hurdle**.
3. **The feasible corridor collapses.** Hurdle-clearing rental rises to ~$10.1/hr vs a value ceiling of ~$9.6–12.25 — the zone between "covers cost of capital" and "max customer willingness-to-pay" narrows to ~$10–12/hr. NVIDIA's residual headroom to raise system prices without breaking neocloud economics is largely gone; equivalently, the neocloud must capture nearly the entire value gap to earn its hurdle.
4. **The perception gap widens mechanically.** EBITDA is byte-identical across 5/6/8-yr lives — the single biggest swing variable in real ROIC (worth **$0.78/hr of rental per year of assumed life**; $1.75/hr across the 8→5 debate — larger than most pricing scenarios) has zero signature in the metric the market and the thesis's own LOW trigger (<35% AI-cloud adj EBITDA margin) anchor on. At 5-yr + held rates NBIS could print 40%+ EBITDA margins with negative EBIT indefinitely.
5. **Whose number is 5?** Not arbitrary — NVIDIA's annual cadence (Blackwell→Rubin→Rubin Ultra→Feynman) compresses economic life toward the product cycle, and the Burry-style late-2025 critique argued industry 6-yr extensions overstate AI-infra earnings by hundreds of billions through 2028. Counter-evidence: A100/Hopper re-signing at 7–8yrs, >35% GM ([[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]). The asymmetry the bull must answer: Hopper's long life was earned in a compute-scarce era, and Rubin's own 3.5× FLOPS uplift is precisely the mechanism that shortens predecessors' lives — assuming Rubin gets Hopper's longevity while Rubin's successor does to it what it does to Blackwell holds both sides of a contradiction.
6. **Verify NBIS's booked policy** (20-F): if NBIS depreciates GPUs faster than CRWV's 6-yr (Yandex-era convention was ~4), its *reported* EBIT is more conservative than the peer's — a like-for-like margin comparison flatters CRWV. Unverified — flag for the Aug 12 print.

## Addendum 2 — 2026-08-04 same-day (user-directed): historical generational test (Ampere → Hopper → Blackwell)

Tests the inference "Rubin rentals must ~double ⇒ $/token cannot decline substantially" against the three prior generations' rental and throughput records.

**Launch rental vs prior-gen decayed rental (the transition-window record):**

| Transition | New-gen launch rental | Prior gen decayed (at transition) | Launch premium | HW gain (dense) | $/PFLOP-hr at launch vs decayed prior |
|---|---:|---:|---:|---|---|
| A100→H100 (2023) | $4.70–8+ (hyperscalers >$12) | A100 ~$1.50–2.50 | **~2.5–4×** | 3.2× BF16; FP8 new | H100@8: $8.09 BF16 / $4.04 FP8 vs A100@1.50: $4.81 — **≈parity on FP8, premium on BF16** |
| H100→B200 (2025) | $5–6.5 | H100 ~$2–3 | **~2–3×** | 2.3× BF16/FP8 | B200@6: $2.67/$1.33 vs H100@2.35: $2.38/$1.19 — **≈parity** |
| B200→VR (H2 2026) | $6–10+ projected | B200 $3.35–6.17 | **~1.5–2.5×** | 1.6× BF16, 3.5× FP8 | VR@10: $2.50/$0.57 vs B200@3.35: $1.49/$0.74 — **BF16 regression, FP8 −23%** |

**Finding 1 — launch rentals have ALWAYS ~doubled-or-more vs the decayed prior gen.** Every generation launched at 2–4× the prior generation's then-current rate, at ≈ **$/FLOP parity** — the One Chart's "value ceiling = $/FLOP parity" is not a theoretical bound, it is the *observed launch-pricing norm*. Rubin at $8–10 vs decayed Blackwell is the pattern, not a break. The "doubling" half of the assumption is confirmed and unremarkable.

**Finding 2 — $/token collapsed anyway (~75–300× in 3 years: GPT-4 $30/Mtok Mar-2023 → GPT-4-class ~$0.40/Mtok 2026; ~10×/yr, accelerating to ~200×/yr median 2024–26 per Epoch).** The collapse never came from launch pricing. Four channels, none of which launch premiums block: (a) **within-generation rental decay** — H100 $8→$1.50–3.00 (−64–75% in ~2yrs), A100 −65–80% over 4–5yrs; (b) **software throughput on fixed hardware** — up to 14× tokens/GPU on the same B300 (accrues FREE to customers on GPU-hour contracts); (c) **model efficiency** — same capability tier on less compute (DeepSeek 1/600th); (d) **the aging fleet as marginal supply** — decayed A100s/H100s stay in service and set the commodity-token price. "Rentals double at launch" and "$/token collapses" have *coexisted through every cycle* — the inferred contradiction is false across the cycle, true only at the launch-window snapshot.

**Finding 3 — what actually breaks at Rubin: the windfall buffer is gone.** Gross rental yield on all-in capex/GPU, launch window: A100 ~**125%**/yr ($3.50/hr on ~$22K) · H100 ~**150%** ($8 on ~$42K) · B200 ~**68%** ($6 on ~$70K) · VR ~**43%** at $10 hurdle-rental, ~**21%** at held $4.90 (on ~$183K all-in). Prior generations *pre-earned* their lifetime ROIC in the first 12–24 months, which made the −60–75% decay survivable. Rubin at launch-parity pricing merely *meets* the hurdle during the launch window — **if the historical decay curve then repeats, lifetime ROIC lands far below hurdle at any plausible launch rate.** The requirement is not "launch at 2×" (normal) but "launch at 2× and hold it 5+ years" (unprecedented — the opposite of every observed curve).

**Finding 4 — precision mix matters.** Rubin's gains concentrate in FP8/FP4 (BF16 only 1.6×): at hurdle rental, Rubin is a **$/FLOP regression for BF16-heavy training** vs decayed Blackwell and only −23% for FP8 inference. Implication: training stays on decayed prior-gen fleets; Rubin must fill with FP8/FP4 inference to justify its price — and the marketed "10× lower token cost" is deliverable only at rentals that put the neocloud below hurdle. NVIDIA's two promises (cheap tokens for customers, good returns for cloud partners) cannot both be true at $7.8–9.1M racks. Epoch's "prices fell rapidly but *unequally* across tasks" fits: frontier/capability tokens (rack-scale domain, HBM4 bandwidth) hold price; commodity tokens collapse onto the decayed fleet.

**Decay-flatteners (bull side, why NBIS ≠ spot exposure):** the H100 1-yr contract +40% rebound (Oct'25→Mar'26) and 7–8yr useful life show the decay tail is fatter than 2024–25 assumed; and **multi-year take-or-pay contracts at launch-window rates are the decay-flattening instrument** — NBIS's ~$50B backlog through 2031 converts the decaying spot curve into a flat annuity. This relocates NBIS's risk in time:
1. **Contract-vintage risk (the sharpest new question)**: the Microsoft (~$17.4–19.4B/5yr) and Meta ($12B dedicated) deals were struck **before** the ~435% memory surge repriced Rubin racks. If they embed pre-surge $/GPU-hr with NBIS bearing equipment cost, the Rubin deployments under those contracts are sub-hurdle **by contract** — locked revenue, inflated capex. If they price per-MW or carry cost pass-throughs, NBIS is protected. Undisclosed → primary falsifier (sharpens thesis Outstanding Q#3).
2. **Re-rent risk 2030–31**: when the contracts roll, NBIS meets whatever the decayed Rubin curve looks like — the same second-cycle re-rent problem the vault's [[Theses/CRWV - CoreWeave]] DDTL bear case dates to 2027–28, arriving at NBIS ~4 years later and without the covenant trigger.
3. **AI Studio as the structural escape**: per-token monetization (inference-as-a-service) captures the software-driven throughput gains that GPU-hour contracts give away free — connects thesis Insight #4 (Yandex software stack) to Insight #6 as its hedge, and is testable in AI Studio's disclosed mix.

## Addendum 3 — 2026-08-04 same-day (user-directed): $/watt scrap-threshold model — what actually ends GPU useful life

User framework: economic useful life ends when rental $/W falls below operating cost $/W (electricity + water/cooling + DC opex) — the miner scrap-threshold logic. Per-watt is the correct normalization: **opex is proportional to watts (generation-invariant per W), rentals are not.** All figures vault estimates; facility-level W/GPU = node power × PUE + storage/network share.

**Rental $/W/yr vs the opex floor:**

| Gen (facility W/GPU) | Launch $/W/yr | Current (2026) $/W/yr | Scrap-threshold rental | Coverage today |
|---|---:|---:|---:|---:|
| A100 (~1.1kW) | $25.1 ($3.50/hr) | **$8.6** ($1.20/hr; open-mkt $0.66 → $4.7) | $0.21/hr | **5.7×** (year 6) |
| H100 (~1.6kW) | $39.4 ($8/hr) | **$14.3** ($2.90/hr) | $0.30/hr | **9.5×** (year 3.5) |
| B300 (~2.2kW) | $21.5 ($6/hr) | **$12.0** ($3.35/hr low) | $0.42/hr | **8.0×** (year 1) |
| VR (~3.9kW) | $20.2 @$10 hurdle / $9.9 @held | — | $0.74–0.99/hr | — |

Opex floor: **~$0.97/W/yr Finland-class** ($0.06/kWh, PUE ~1.1, free cooling) · **~$1.49/W/yr US-average** ($0.10/kWh) · **~$2.08/W/yr Foxconn-implied** ($0.175/kWh). Electricity is ~55–70% of the floor.

**Finding 1 — the cash-scrap floor has never bound and is nowhere near binding.** A100, six years post-launch, still covers its floor 5.7× — and its *plateau* decay since 2023 is only ~−7%/yr ($1.50→$1.20), putting floor-contact at **year ~14 (−20%/yr worst case) to ~30 (−7%/yr)**. H100: year ~13.5–34. The decay curve is two-phase: −50–75% scarcity-premium bleed in the first ~2 years, then a near-flat plateau far above opex. **Rental-below-opex is the absolute end of life, but it is not what retires GPUs** — no observed generation has reached it.

**Finding 2 — the actual life-ender is slot opportunity cost, and it is stalling.** When power (the rack slot) is the binding constraint, the replacement test is: swap old→new when new-gen net $/W (revenue − opex − amortized capex) exceeds old-gen *cash* $/W (revenue − opex; capex sunk). The swap-gain series:

| Transition | New-gen net $/W/yr | Old-gen cash $/W/yr | **Swap gain** |
|---|---:|---:|---:|
| 2023 A100→H100 | $33.6 | $9.3 | **+$24.3** — refresh races (observed: 2023–24 H100 land-grab) |
| 2025 H100→B300 | $14.7 | $10.1 | **+$4.6** — moderate (observed: Blackwell deploys AND H100s re-sign at +40%) |
| 2026 →VR @$10 hurdle | $10.4 | $7.1 | **+$3.3** — marginal |
| 2026 →VR @held $4.90 | $0.1 | $7.1 | **−$7.0** — swap destroys value; sweat the old fleet |

Driver: capex/W rose $20 → $26 → $32 → **$47** while launch revenue/W stayed ~flat ex-scarcity ($25 → $39 → $21.5 → $20) → gross payback stretched **0.7–0.8yr → 1.5yr → 2.3yr (hurdle) / 4.7yr (held)**. The model retrodicts all three observed transitions — the refresh engine is decelerating *by economic logic*, which (a) derives the 7–8yr useful-life extension from first principles (it is not a Patel anecdote, it is the slot test weakening), and (b) means at held Rubin rents rational operators under-deploy Rubin and sweat Hopper/Ampere — constraining new supply until rents rise toward the ceiling. Self-correcting, supports the rents-must-rise side.

**Finding 3 — regime split + the NBIS edge.** Power-scarce (now–2027): slot test rules, fleets refresh only where new-gen rents clear ~hurdle. Power-abundant (the 2028–29 digestion scenario): slots stop binding, the cash floor rules, fleets run 10–15yrs, and the old-gen supply overhang caps commodity rents — the bear-case tail. The floor is **operator-specific**: NBIS's Finland flagship (~$0.97/W/yr) sits ~35–50% below US-grid peers (~$1.5–2.1) → in a rental collapse, **NBIS's fleet is among the last cash-viable** (miner logic — the lowest-cost watt survives; same durable-layer logic as the vault's landlord/IREN power thesis). This partially rehabilitates the 8-yr depreciation column *for NBIS specifically* and extends its fleet's terminal-value tail vs peers. Caveats: age-related failure rates (HBM, fans) and CUDA-support horizon are the practical life-enders this cash model omits; NBIS's book is contracted (not spot), so these curves govern its *re-rent* and terminal values, not current revenue.

## Addendum 4 — 2026-08-04 same-day (user-directed): fleet earnings model — descending-then-flat depreciation, 5/7/9/11-yr lives, Rubin scale scenarios

**Model** (vault estimates; validated against reported 2026 financials): Depreciation weights yr1 30% / yr2 22% / yr3 14% (descending, mirrors the observed two-phase rental decay), then flat 34%/(N−3) for yrs 4–N. Life N = economic life: revenue = contract rate yrs 1–5, re-rent at 47% × −7%/yr yrs 6–N, zero (scrapped) after N. Cohorts: CRWV = 130K Hopper ($4.00/hr, $42K, 2024-vintage) + 120K Blackwell ($6.00/hr, $70K, 2026); NBIS = 40K Hopper (2025) + 60K BW (2026) + 140K BW build-cohort (2027) → 200K BW base. Rubin: $8.00/hr central, $183K/GPU, 2027-vintage, units = BW base ×{1, 1.5, 2}. Cash-cost ratios calibrated to reported margins: CRWV old 42%, NBIS old 52%, Rubin marginal 30%. Validation: model 2026 → NBIS +$0.34B EBIT (actual: just crossed adj-EBITDA breakeven ✓); CRWV +$2.4B EBIT − $2.1B interest ≈ breakeven (actual GAAP op −7% — model slightly rosy; excludes A100 legacy + W&B amort).

**T1 — Lifetime avg ROIC by generation × life (avg annual EBIT / initial capex):**

| Gen (rate, capex) | N=5 | N=7 | N=9 | N=11 |
|---|---:|---:|---:|---:|
| Hopper ($4.00, $42K) — CRWV cash basis | 23.5% | 22.5% | 21.3% | 20.1% |
| Blackwell ($6.00, $70K) — CRWV | 19.2% | 18.8% | 18.0% | 17.2% |
| (NBIS cash basis: Hopper ~16%, BW ~13%) | | | | |
| **Rubin @$8.00** | **4.1%** | **6.1%** | **6.8%** | **7.1%** |
| Rubin @$4.90 (held) | −5.2% | −1.8% | −0.1% | +0.8% |
| Rubin @$10 (hurdle-rental) | 10.2% | 11.2% | 11.3% | 11.1% |
| Rubin @$12 | 16.2% | 16.3% | 15.8% | 15.2% |

Two structural results: **(a) life extension does not rescue Rubin** — 5→11 yrs lifts $8/hr ROIC only 4.1%→7.1% (the re-rent tail adds little; the flat-dep tail is small); **only price does** (the ~15% hurdle needs ~$12/hr under this schedule, above the ~$9.6–12.25 value ceiling's midpoint). **(b) The generational collapse is life-invariant**: legacy fleets earn 13–24% at every life; Rubin 4–7% at $8.

**T2 — Rubin per-GPU J-curve (N=7, $8/hr):** yr1 **−5.9%** (EBIT −$10.7K — negative even at $8) → yr2 +2.1% → yr3 +10.1% → yrs4–5 +15.6% → re-rent tail +2–3%.

**T3 — Current-fleet standalone EBIT $B (no Rubin):**

| | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|---:|
| CRWV N=5 | 2.39 | 2.89 | 3.57 | 1.86 | 1.86 | **0.00** |
| CRWV N=7 | 2.39 | 3.36 | 4.03 | 3.23 | 3.15 | 0.83 |
| CRWV N=9/11 | 2.39 | 3.5–3.6 | 4.2–4.3 | 3.6–3.8 | 3.6–3.7 | 1.7–1.9 |
| NBIS N=5 | 0.34 | 1.05 | 2.12 | 2.78 | 2.16 | 1.51 |
| NBIS N=7 | 0.34 | 1.05 | 2.26 | 3.27 | 3.49 | 2.75 |
| NBIS N=9/11 | 0.34 | 1.05 | 2.3 | 3.4–3.5 | 3.9–4.2 | 3.2–3.4 |

Shape: EBIT *rises* through 2028–29 mechanically (cohorts roll into the flat-dep tail) — margin expansion with zero business improvement. Lives are indistinguishable through 2027 (identical descending weights) and decisive 2029–31: at N=5 **CRWV's current fleet revenue hits zero in 2031** (Hopper scrapped 2029, BW 2031); at N=9–11 it still earns $1.7–1.9B. CRWV's $2.1B interest consumes most of its standalone fleet EBIT in every pre-2028 year.

**T4 — Combined (current + Rubin, N=7) revenue / EBIT $B:**

| Scenario | 2027 | 2028 | 2029 |
|---|---|---|---|
| CRWV +120K Rubin (1×) | rev 17.3, EBIT +2.1 (**pretax −1.8**) | 17.3, +4.5 (+0.6) | 15.2, +5.5 (+1.6) |
| CRWV +240K (2×) | rev 24.9, EBIT +0.8 (**pretax −4.8**) | 24.9, +5.0 (**−0.6**) | 22.7, +7.7 (+2.1) |
| NBIS +200K Rubin (1×) | rev 23.3, EBIT **−1.1** | 23.3, +3.0 | 23.3, +7.0 |
| NBIS +400K (2×) | rev 36.0, EBIT **−3.3** | 36.0, +3.8 | 36.0, +10.7 |
| Pair-sum (both 1×) | rev 40.7, EBIT +1.0 | 40.7, +7.5 | 38.5, +12.4 |

(CRWV pretax after interest scaled with Rubin debt: $3.9/4.7/5.6B at 1×/1.5×/2×. NBIS interest ~nil — converts. Full-year cohort convention: "2027" = Rubin cohort's first 12 months, a 2027–28 calendar straddle.)

**Findings:** (1) **The whipsaw**: every scenario prints a 2027 earnings air-pocket (30% yr-1 dep on $22–73B of Rubin capex) → 2028 recovery → 2029 gush — driven by depreciation cadence, not economics; revenue is *flat* across 2027–29 in every row, so the 2028–29 "earnings growth" is pure dep roll-off. (2) **Scale amplifies the J-curve and leverage decides who can run it**: CRWV at 2× is pretax-negative through 2028 — aggressive Rubin scaling is GAAP-unfinanceable on its capital structure; NBIS absorbs the same optics with ~nil interest. The clean balance sheet's real function is the *capacity to run the Rubin J-curve at scale*. (3) **Blended ROIC (2028, 1×): CRWV 12.6% vs NBIS 5.8%** — a vintage-age artifact (NBIS's capital is younger, still in descending-dep years), not a quality gap; both converge toward Rubin's ~6–7% lifetime as Rubin mix rises. (4) Under economically-matched (front-loaded) depreciation, the perceived-vs-real ROIC gap of Insight #6 stops being hidden and prints as the 2027 loss — the market's reaction to that print, against flat revenue and rising EBITDA, is the trade.

## Addendum 5 — 2026-08-05 (user-directed): reconciliation vs "The Economics of a Neocloud" (degentrading, 5 Jul 26, in _Inbox pending /ingest) + error audit of this note's own assumptions

The Inbox note derives **<1yr payback** at the Google→SpaceX/xAI deal rate ($920M/mo ÷ 110K GB200 ÷ 720h = **$11.6/GPU-hr**), ~2yr at $6/hr, on $50B/GW GB200 capex — the source of the "1–2.5yr payback" consensus. Reconciliation bridge, each step quantified:

| Step | Payback | What changes |
|---|---:|---|
| 0. Note as published ($11.6/hr, 83,333 GPUs/100MW at chip TDP) | **0.60yr** | — |
| 1. Buildable density (GB200 ≈2.2kW *facility* incl PUE/network/storage → ~45K GPUs/100MW, capex $110K/GPU) | **1.11yr** | the note's density is unbuildable — its revenue/MW is ~1.8× overstated |
| 2. Wholesale rates (the note's OWN long-term hyperscaler estimate: ~$4/hr; $6 shown too) | **2.2yr ($6) / 3.4yr ($4)** | $11.6 is retail/outlier — the note itself calls the xAI deal "remarkably generous" (Google compute-short; Musk retained recall rights); hyperscalers re-monetize at $12+, neoclouds sell wholesale |
| 3. Rubin capex 2× (the note CONCEDES: "Rubin twice Blackwell… Jensen: $100B/GW realistic") | **3.9yr ($6) / 2.8yr ($8)** | matches this note's Rubin payback |
| 4. Payback → ROIC | — | cash payback ignores capital consumption; a 2yr payback on a 5–7yr asset is hurdle-adequate ONLY if rates hold through yrs 3–7 |

**The note's own wholesale rate + its own Rubin concession + buildable density REPRODUCE this note's bearish arithmetic.** The divergence is anchor-choice (retail outlier vs wholesale), metric-choice (cash payback vs ROIC), and vintage (Blackwell capex vs Rubin capex) — not a model disagreement. Both models agree the CURRENT fleet mints cash (T3's rising EBIT; Addendum 3's 0.7–1.5yr historical launch paybacks). The fight is exclusively over the marginal Rubin dollar.

**The anchor test — NBIS's own numbers pick the wholesale anchor.** Exit ARR $7–9B ÷ 800MW–1GW active = **$7–11/W/yr** → ~$2.00–3.15/GPU-hr wholesale-equivalent at 2.2kW. MSFT deal $17.4–19.4B/5yr on ~300MW (Vineland, press-derived est.) = **$11.6–12.9/W/yr** ≈ $3.35/hr. CRWV realized: $11.4/W/yr. Versus: xAI deal $45.6/W/yr (retail outlier), IREN-MSFT ~$36/W/yr (full-stack-from-owned-power outlier). **NBIS's flagship contracts price at ~1/4 the note's anchor deal** — the wholesale band (~$4–6/hr) this note used for "held rates" is approximately NBIS's actual realized economics, not a bearish invention.

**Errors conceded in this note's model (direction: all previously too bearish):**
1. **Monolithic depreciation on the full $47B/GW at GPU life** — wrong: racks (~$126K/GPU) carry GPU life; shell/power (~$57K) carries 15–30yr + terminal value (re-rackable — the landlord layer survives the GPU). Corrected N=7 lifetime ROIC: **$4.90 → +1.1% (was −1.8%) · $6 → +3.9% · $8 → +9.0% (was 6.1%) · $10 → 14.1% · $12 → 19.1%**. Hurdle-clearing wholesale rental drops from ~$12 to **~$10.5/hr**.
2. **90% billed hours** — take-or-pay pays on availability: 95–100% correct → +~1pt further.
3. **Re-rent haircut (47%) modestly harsh** — the note documents A100s at $1–2/hr open / **$2–3.5 hyperscaler-channel** 6yrs post-launch, above my aggregator-floor anchors → tail revenue +10–20%.
4. **Addendum 4's T3/T4 are economic restatements, not GAAP forecasts** — companies report straight-line (CRWV 6yr SL), so reported prints will be smoother than the modeled 2027 air-pocket; the air-pocket is where *economic* value consumption lands, not where accounting will show it.
5. $47B/GW may be gold-plated for NBIS (Finland power/land, owned build) — though the note's own $50B/GW GB200 and "Jensen $100B/GW Rubin" sit at/above it.

**What survives every correction:** (a) the generational deterioration — even at xAI-outlier rates Rubin pays back 1.9yr vs Blackwell 0.6yr; at wholesale rates 2.8–3.9yr vs 1.1–2.2yr — the doubling of capex/GPU is conceded by the bullish source itself; (b) held wholesale rates (~$4–6) put corrected Rubin lifetime ROIC at **+1–4%** — still far below hurdle; (c) the hurdle needs **~$10.5+/hr wholesale ≈ $38+/W/yr ≈ 3–4× NBIS's current implied contract economics**; (d) the EBITDA-blindness/perceived-ROIC mechanism (Insight #6) is untouched by any correction. The note's claim "compute markets are pricing a severe shortage" is exactly the thesis's crux restated: the 1–2.5yr payback consensus is a *shortage-vintage Blackwell fact*; whether Rubin inherits it is the open bet, and it requires wholesale rates ~3× current NBIS realized.

**Falsifiers that would prove THIS note wrong (watch Aug 12 + H2 disclosures):** a dedicated Rubin contract printed at ≥$12/hr wholesale-equivalent (≥~$40/W/yr); NBIS ARR-per-active-watt inflecting from ~$10 toward $20+; AI-cloud margin *rising* through the Rubin ramp. Recommend `/ingest` of the Inbox note to formalize it as a Research record.

## Contradiction Check

**Supports** thesis Bear Case #3 (margin compression) and Outstanding Q#4 (is the 45% margin durable) with a *mechanism*: the memory surge, not just utilization dilution, is what compresses the incremental return — and it does so on the ROIC line while sparing EBITDA, which is why the compression is easy to miss.

**Tension / offsets (why conviction stays medium, not lower):**
- **Value-based pricing may hold.** Rubin's ~3.5× FP8 FLOPS means a rational customer pays more per Rubin GPU-hr; in a sold-out market (NBIS capacity contracted through 2031) NBIS has the pricing power to pass the capex step-up through. The user's held-rate assumption is deliberately pessimistic. Falsifier of the bear read: NBIS discloses Rubin rentals near the $9–12/hr value band.
- **Prepayment shrinks the denominator.** Microsoft's ~$7B upfront + ~$4.8B deferred revenue fund part of the capex, so ROIC on NBIS's *own* invested capital is higher than the ~$47B gross-asset figure implies (customers carry a slice of the fleet). The macro note counts prepayments as debt-like claims, but for a return-on-capital calculation they still reduce NBIS's net capital at risk.
- **Useful-life extension.** 7–8yr life (vs 6yr Foxconn assumption) with cluster-resign >35% GM lifts lifetime ROIC materially — the 8-yr column above adds ~3–4 points of ROIC at every rental.
- **NBIS's actual per-GW cost is likely below Foxconn's $47B** (Finnish power, owned land/>75% owned capacity, staged Blackwell-heavy 2026 build). The full Rubin memory-inflated intensity hits the *incremental* 2027+ fleet, not the current blended book. This bounds the near-term damage.

**Tension with the NVDA thesis:** the same datapoint that hurts NBIS's ROIC *helps* NVIDIA — the memory markup NVIDIA harvests (SOCAMM ~60% GM) is exactly the neocloud's lost margin. The pair is the value-layer-monopoly trade in miniature: long the layer owner ([[Theses/NVDA - Nvidia]]), skeptical of the layer-renter's returns.

**Cross-thesis:** CRWV faces the identical Rubin capex-intensity step-up; its bear case (credit/DDTL amortization vs re-rent) worsens if held rates leave the new fleet earning below the ~SOFR+450 cost of its collateralized debt. The ROIC-compression read is a *sector* mechanic ([[Sectors/Neoclouds & GPU-as-a-Service]] §Investor heuristics #5, "neoclouds are levered NVIDIA derivatives").

## Source Excerpts

- Morgan Stanley (via Tom's Hardware / Yahoo Finance): a single Vera Rubin NVL72 rack costs **over $7.8M, "nearly double the Blackwell generation."**
- Foxconn (via Investing.com / wccftech): building **1GW of Vera Rubin ≈ $47B**; annual electricity ~$1.3B; **"hardware depreciation is six times the electricity cost"** (⇒ ~$7.8B/yr).
- wccftech: **"~435% memory price surge, pushing HBM4 & LPDDR5X bill to ~$2M of the $7.8M total."**

## Sources

- [Morgan Stanley Vera Rubin rack estimate](https://finance.yahoo.com/sectors/technology/articles/morgan-stanley-estimate-says-single-114101104.html)
- [What it costs to deploy 1GW of Vera Rubin (Investing.com / Foxconn)](https://www.investing.com/news/technology-news/what-it-costs-to-deploy-1gw-of-nvidia-vera-rubin-infrastructure-4740730)
- [Foxconn pegs Vera Rubin at $47B/GW (wccftech)](https://wccftech.com/foxconn-pegs-nvidia-vera-rubin-ai-datacenter-at-47-billion-per-gigawatt/)
- [Vera Rubin rack memory surge (wccftech)](https://wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/)
- [Tom's Hardware — VR NVL72 up to $8.8M](https://www.tomshardware.com/tech-industry/artificial-intelligence/price-of-nvidias-vera-rubin-nvl72-racks-skyrockets-to-as-much-as-usd8-8-million-apiece-but-server-makers-margins-will-be-tight-nvidia-is-moving-closer-to-shipping-entire-full-scale-systems)
- [Nebius to offer Vera Rubin NVL72 H2 2026](https://nebius.com/newsroom/nebius-to-offer-nvidia-vera-rubin-nvl-72-in-us-and-europe-from-h2-2026)

## Related Research
- [[Theses/NBIS - Nebius Group]] · [[Theses/CRWV - CoreWeave]] · [[Theses/NVDA - Nvidia]]
- [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]] (the One Chart floor/ceiling framework this extends)
- [[Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison]] (both peers framed as NVIDIA/grid layer-renters)
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] (useful-life extension, cluster-resign margins)
- [[Sectors/Neoclouds & GPU-as-a-Service]] · [[Macro & Technology/Sustainability of AI Capex]]
