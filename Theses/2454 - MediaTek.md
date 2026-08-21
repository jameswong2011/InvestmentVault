---
publish: true
date: 2026-08-04
tags: [thesis, semiconductors, custom-silicon, mobile-soc, 2454]
status: draft
conviction: medium
sector: Custom Silicon & Networking Semiconductors
ticker: 2454
source: MediaTek Q2 2026 earnings (2026-07-31) + web research (TrendForce, SemiAnalysis, Digitimes, companiesmarketcap); internal synthesis with [[Macro & Technology/Sustainability of AI Capex]]
---

# 2454 - MediaTek

## Summary

MediaTek, the world's #1 smartphone-chip vendor by volume, has been re-rated from a US$70B mobile-cyclical (end-2024) to a US$190B "custom-AI-silicon winner" (~55x trailing P/E on FY25 net income that fell 1% YoY). The entire move is multiple expansion, and it embeds ASIC success the economics have not yet proven. The differentiated read: MediaTek is Google's designated **cost-down vehicle** to break Broadcom's TPU pricing power: it designs the inference-optimized TPU v8i "Zebrafish" at 20-30% below Broadcom's training part, and has escalated into the leading-edge v9 "Triggerfish." That is a genuine, multi-billion-dollar convex option on AI-inference volume, funded by a still-cash-generative mobile base. But MediaTek is the commoditizer of a custom-ASIC layer it does not own: its economics are structurally second-seat, single-customer-concentrated on Google, and likely margin-dilutive as they scale, while the mobile cash cow funding the bet erodes under OEM vertical integration (Xiaomi XRing) and a ~200% memory-cost squeeze. Own it as a convex bet on inference-silicon volume at a sensible price, not as a toll-layer compounder at 55x.

## Key Non-consensus Insights

**1. "Second-source" is the business model rather than a weakness: MediaTek is Google's pricing-power lever against Broadcom.**
- **Consensus:** The market (and the vault's own Custom Silicon sector note) prices MediaTek's ASIC entry as a marginal, low-margin "third seat" behind Broadcom and Marvell: subscale, mobile-first, limited HPC SerDes IP, ~2-5% share, worth little.
- **Variant:** MediaTek is the vehicle for Google's stated goal to "ditch Broadcom by 2027" and cut AI-chip cost "by billions", not a marginal third source. It has escalated from the cost-optimized v8i inference part to the leading-edge v9 "Triggerfish": scope expansion, not a one-off. At ~10-11M TPU units in 2027 and a chosen price 20-30% below Broadcom, the second seat is a multi-$B pool that compounds as inference (not training) becomes the dominant TPU workload. The customer sustains the second source precisely to cap the incumbent's price (the AMD-in-GPUs / Marvell-in-switches equilibrium; Semi L3).
- **First confirming observable [2026-Q4]:** first MediaTek AI accelerator enters mass production; data-center revenue prints toward the $2B FY26 target.
- **Fails if:** Google re-consolidates TPU design toward Broadcom or in-sources, or MediaTek's share of 2027 TPU units lands below ~15% (→ LOW trigger).

**2. The re-rating already happened: the mispriced variable is ASIC margin/mix, not ASIC existence.**
- **Consensus:** MediaTek is an AI-ASIC winner; the ~2.7x re-rate since end-2024 to ~55x trailing P/E reflects a structural transformation the market has embraced.
- **Variant:** The multiple prices ASIC revenue as if it carries mobile-like economics and lands at MediaTek's aspirational scale; both are contestable. On margin: the vault's own estimate (MRVL thesis) puts MediaTek ASIC gross margin at ~45%, roughly in line with the ~46% group blended, so dilution is mild if that holds, but a turnkey book heavy in HBM/CoWoS pass-through trends toward the Alchip ~30% pure-implementation floor and drags group GM into the low-40s. On magnitude: MediaTek guides to $7-12B for 2027 (15-20% of an $80B SAM), while sell-side models embedded in the vault's [[Theses/AVGO - Broadcom]] thesis carry only **~$3.2B 2027E**: a 2-4x gap between ambition and modeled reality. The two levers the 55x misprices are the blended gross-margin path and the realized (not guided) ASIC ramp ([G-13]: isolate the operating levers the price gets wrong).
- **First confirming observable [2026-Q4 → 2027-H1]:** group gross margin as data-center mix scales: does GM hold ~46% or drift toward the low-40s?
- **Fails if:** data-center GM disclosed/inferable at ≥45% with group GM stable as ASIC scales → ASIC is margin-neutral-to-accretive and the variant is wrong.

**3. MediaTek is the commoditizer of a layer it does not own (Value Layer Monopoly, adversarial).**
- **Consensus:** MediaTek is climbing the AI value chain into high-value custom silicon.
- **Variant:** MediaTek's structural role is to dissolve the custom-ASIC layer's pricing power for its customer, not to own it. The qualification gate (224G/448G SerDes, CoWoS-L orchestration, HBM4 integration) is Broadcom's moat; MediaTek wins exactly the scope where that gate is lowest (cost-optimized inference) by underpricing, while renting the Arm ISA above and TSMC fabrication below. Its ASIC pricing power is therefore structurally capped and its durability low. This is a convex volume option, not a toll-layer annuity, and must be valued as such, not at a Broadcom-like multiple.
- **First confirming observable [2027]:** whether MediaTek captures any IP-defensible, higher-margin scope (own SerDes / packaging / interconnect IP) vs remaining turnkey implementation.
- **Fails if:** MediaTek demonstrates a defensible IP layer (competitive 224G+ SerDes or proprietary packaging edge) that sustains ≥60% ASIC gross margin → it is becoming a layer-owner; upgrade.

**4. The mobile cash cow is eroding exactly as it is needed to fund the ASIC bet.**
- **Consensus:** Mobile is a stable, cash-generative base that comfortably funds diversification; #1 volume share is defensible.
- **Variant:** MediaTek's mobile franchise faces simultaneous volume and margin compression the diversification story obscures: Xiaomi's in-house XRing (O1 shipping in the 15S Pro; O2 on TSMC N3P in Q2 2026) removes a top-customer's flagship sockets, Chinese self-developed SoC share rises from ~30% to ~60% by 2026, and a ~200% YoY memory-cost surge (memory now 30-40% of a phone's BOM, up from 10-15%) is squeezing both customer demand and MediaTek's own margin (GM −2.9pp YoY; mobile revenue −~20% YoY in Q2 2026). The bet is being funded from a weakening base.
- **First confirming observable [2026-H2]:** mobile revenue trajectory + China smartphone units post-subsidy; MediaTek flagship socket wins/losses at Xiaomi/Oppo/Vivo.
- **Fails if:** mobile revenue restabilizes (flat-to-up YoY) through 2026-H2 with flagship share gains at a major Chinese OEM → funding base intact.

**5. MediaTek is levered to the inference/cost-down phase of the AI cycle, not the training land-grab.**
- **Consensus (AI-capex bears):** AI-exposed silicon gets repriced in the 2028-29 capex digestion; single-customer second-source design-services is exactly what the digestion punishes (per [[Macro & Technology/Sustainability of AI Capex]]).
- **Variant:** Within ASIC, MediaTek is inference- and cost-weighted (v8i, v9 for agentic inference; explicitly the low-cost partner). The same essay argues token/inference volume keeps compounding through the digestion while capex-per-unit falls and the industry rewards efficiency. Google leans on its cheapest inference-silicon partner more, not less, when capex discipline binds, so MediaTek can be a relative winner inside the ASIC downcycle precisely because it is the cost leader, even as leverage-funded training capacity reprices.
- **First confirming observable [Jan-Feb 2027 guidance window]:** hyperscaler capex guides + Google TPU mix shifting toward inference/cost-optimized parts.
- **Fails if:** Google cuts TPU volume or defers v8i/v9 in a capex pullback → cost-leadership does not insulate MediaTek; its ASIC backlog reprices like any other second-source.

## Outstanding Questions

1. **What is the actual gross margin of data-center ASIC revenue?** Is "ASIC surpasses mobile by 2027" accretive or dilutive at the group level? Answered by segment disclosure, or inferred from group GM as mix shifts through 2026-27. This is the single most thesis-determinative unknown.
2. **How concentrated is the ASIC book on Google, and is a second hyperscaler anchor credible?** A near-sole-anchor program is a binary survival test (Semi #10), not "concentration to monitor." A signed second anchor (Meta / Amazon / Microsoft) would de-risk materially.
3. **Does MediaTek own defensible IP in the ASIC stack (SerDes, packaging, interconnect), or is it pure turnkey implementation?** Determines whether the second-seat position is durable or a temporary cost-arbitrage that TSMC-adjacent rivals (Alchip, GUC) can replicate. Critically: has "Zebrafish" cleared the specific packaging-execution bar (the HBM/RDL-interposer hand-off) that tripped Marvell off the Trainium 3 socket (lost to Alchip on interposer defects)? Winning an RFP is not the same as clearing the qualification gate.
4. **What is the ROIIC on the data-center build?** How much of the $5B financing capitalizes into IP/mask/prepayments vs opex, and what incremental return does it earn vs the mobile base ([G-7])?
5. **How durable is the mobile franchise against OEM vertical integration?** What share of mobile revenue sits with customers (Xiaomi today; potentially Oppo/Vivo/Samsung) building their own SoCs, and how fast does Chinese domestic substitution advance?
6. **How do Arm v9 royalty economics and Arm's move up-stack (Compute Subsystems; potential own-chip) affect MediaTek's cost structure and differentiation?** MediaTek rents the ISA it builds on; a royalty step-up or an Arm-designed reference SoC compresses the fabless margin.
7. **What ASIC outcome is priced at ~55x trailing / ~9x EV/Revenue, and what is the downside multiple** if the ramp disappoints or the AI-capex digestion (2028-29) arrives? A reversion toward the 15-20x history halves the stock even on flat revenue ([G-13]).
8. **Can the Nvidia N1X PC and Dimensity Auto optionalities become material,** or are they low-probability call options given weak early N1X benchmarks and long automotive design-in cycles?

## Business Model & Product Description

MediaTek (founded 1997, spun out of UMC; Hsinchu, Taiwan) is a fabless SoC designer: it designs the chip, TSMC and others fabricate it. The intuitive frame: MediaTek is the **"Android of mobile silicon"**, the high-volume, cost-optimized merchant SoC vendor to the world's non-Apple, non-in-house handset makers, versus Qualcomm's premium/US-flagship position. The economic engine is monetizing Arm IP + leading-edge TSMC process at scale and cost-efficiency; the mobile moat is scale, reference-design breadth, and China-OEM relationships, not a qualification-gate monopoly.

**Revenue segmentation (heuristic):**

| Segment | ~% of revenue | Content |
|---|---|---|
| Mobile Phone | ~45-50% | Dimensity 9000-series flagship (9500/9500s), Dimensity mainstream, legacy Helio. #1 global smartphone SoC by volume (~35-40% share). Customers: Xiaomi, Oppo, Vivo, Transsion, Samsung (tablets/select phones), emerging-market OEMs |
| Smart Edge Platforms | ~40-45% | Merchant WiFi/connectivity (share leader), broadband, smart-TV SoCs (share leader), Chromebook, tablets; plus the new custom-ASIC and automotive lines |
| Power IC | ~10% | Power management silicon |
| Data-center ASIC | Emerging (→ $2B FY26 target) | Google TPU v8i "Zebrafish"; escalating to v9 "Triggerfish"; Nvidia N1X PC; Dimensity Auto |

**Product technical detail:**
- **Dimensity 9500 / 9500s**: TSMC N3-class flagship SoC; premium Arm cores + on-device generative-AI NPU. Benchmarks at CPU/GPU parity with Qualcomm's Snapdragon 8 Gen 5, with an efficiency edge in some tests; trails on single-core peak and US-market/ecosystem prestige. MediaTek targets 40% smartphone-SoC share on the back of the 9000-series.
- **Google TPU v8i "Zebrafish"** (MediaTek-designed), inference-optimized: single compute die + 1 IO die + 6× HBM3E, TSMC N2, late-2027 target, engineered for 20-30% lower cost than Broadcom's v8t "Sunfish" (2 compute dies, 8× HBM3E). MediaTek is also tapped for **TPU v9 "Triggerfish"** (CPU + compute die fused in one package for agentic AI): a step up the complexity curve.
- **Nvidia N1X / N1** (co-developed): Arm PC SoC for Windows-on-Arm: up to 20 Arm cores + Nvidia Blackwell GPU (48 SM) + up to 128GB unified memory, 180-200 AI TOPS; H2 2026 with Dell/HP/Lenovo/Asus. Second Nvidia collaboration after the GB10 (DGX Spark) superchip. Early benchmarks underwhelming: a call option, not a base-case driver.
- **Dimensity Auto Cockpit C-X1**: TSMC N3 + integrated Nvidia Blackwell GPU + deep-learning accelerator; >$1B cumulative automotive design wins; auto revenue more than doubled YoY in Q4 2025; traction with Chinese automakers, expanding to Europe/India.

## Industry Context

**Value-chain position.** MediaTek sits in fabless design, renting the Arm ISA above and TSMC fabrication below: it owns neither the instruction-set layer nor the manufacturing layer where the durable semiconductor rents concentrate. In **mobile** it is the merchant volume leader against Qualcomm (premium/US), while Apple (in-house) and now Xiaomi (XRing in-house) remove sockets at the top of the market. In **custom ASIC** it is the emerging second/third source (~5-8% share, vault estimate) behind Broadcom (~60-70%; the SerDes/packaging qualification gate), Marvell (~13-25%), and fast-growing Alchip (~15%): the procurement-driven multi-sourcing dynamic where hyperscalers refuse single-vendor lock-in (Semi L3; the vault's [[Sectors/Custom Silicon & Networking Semiconductors]] note). Notably, the vault's MRVL thesis ranks MediaTek (Zebrafish) ahead of Marvell in Google's inference-silicon queue: MediaTek is a more credible Google inference partner than its ~5-8% headline share implies.

**Where the leverage sits:** (a) Broadcom: the analog/SerDes + CoWoS-L orchestration moat; (b) TSMC: foundry allocation and CoWoS/advanced-packaging access, the gate every fabless ASIC player must pass; (c) the hyperscaler customer: Google, which deliberately plays partners against each other to cut its own cost. MediaTek's leverage is narrow but real: lowest cost, deep TSMC integration, and willingness to underprice the incumbent. The true qualification gate is not RTL design but packaging execution: the HBM/RDL-interposer hand-off that cost Marvell the Trainium 3 socket (defects Alchip had to fix); MediaTek's Zebrafish must clear that same bar, and its smaller inference volumes give it weaker CoWoS-queue priority at TSMC than Broadcom's training volumes.

**Structural forces reshaping the industry:**
- AI inference migrating from merchant GPU to custom ASIC (TrendForce: custom-ASIC revenue +45% in 2026 vs GPU +16%), enlarging the design-services TAM MediaTek is entering (management's 2027 SAM estimate: ~$80B; data-center ASIC market ~$70B by 2028).
- Hyperscaler multi-sourcing fragmenting the ASIC design-partner base: a pricing-power risk to Broadcom and the opportunity for MediaTek (Google now runs a four-partner chain: Broadcom + MediaTek + Marvell + TSMC).
- Mobile SoC commoditizing under Chinese vertical integration (XRing and peers), pushing self-developed silicon from ~30% to ~60% of Chinese-brand volume and forcing an expected 10-15% decline in merchant mobile-chip prices.

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | ~US$190B (NT$5.85T), Aug 2026 | Up from US$69.5B end-2024 (~2.7x); ~world's 100th-largest company. Shares out ~1.59B |
| EV/Revenue | ~9x | EV ~US$181B (net-cash balance sheet) / ~US$19.5B TTM revenue |
| Revenue Growth | FY25 +~12% YoY (NT$596B record); FY26E high-single-digit (USD) | Q2'26 +1.2% YoY; data-center ASIC is the FY27+ swing factor |
| Gross Margin | 46.2% (Q2'26), −2.9pp YoY | Memory-BOM inflation + mix; ASIC-mix dilution the forward risk |
| FCF Yield | ~1.3% | FY25 operating cash flow NT$98.3B; low yield = growth premium; dividend yield ~2.5% |
| P/E (trailing) | ~55x | vs ~15-20x historical; entire re-rate is multiple expansion (FY25 net income NT$106.1B, −1% YoY; EPS ~NT$66) |

*Metrics are web-sourced estimates as of Aug 2026: run `/numbers 2454` to refresh against Financial Modeling Prep.*

## Management and culture

Hypothesis: Inert on [[Lens - Management and Culture]]. Gate 1 passes (TPU v8i/v9, Dimensity, N1X, Auto is a high-frequency optionality feed); Gate 2 fails: the ~2.7× re-rate to ~55× trailing already prices the ASIC pipeline as a transformation, not as capital destruction. Conversion capacity is not the mispriced variable; grade the name on [G-13]/[G-7]. [MC-2] 114 AR (print 2026-02-28): founder-chairman Ming-Kai Tsai 2.61% plus spouse 2.45%; CEO Rick Tsai 0.05%; Board-adopted 2022 exec ownership guidelines; 2025 named-manager pay NT$2.20B (2.09% of NI) with RSA vesting on TW50 relative TSR (25–40%), revenue growth 7–12%, operating margin 15–18%: operating metrics, not ROIC or ASIC product-volume; 2025–26 share-count increases coincide with RSA vesting, not clustered open-market buys. [MC-7] 22,869 employees YE2025 (R&D 20,123), product/functional at ~4× the matrix scaling heuristic; 1 Aug 2026 VPs Mingxi Fan (ex-Qualcomm) and Ankireddy Nalamalpu (ex-Intel DC/AI Fellow) are talent import into data-center, not a §4 org-regime pivot. [MC-6]/[G-10]: 7.5-year average tenure and 5.2% 2024 global turnover do not beat the entropy / new-venture-destruction base rate on a second-source ASIC book the price already owns. Swing variable: RSA adding ASIC-GM or product-volume metrics, and P&L ownership for the 2026 ASIC hires, only if the multiple compresses and Gate 2 re-opens.

## Bull Case

Data-center ASIC compounds from ~$2B (2026) toward $7-12B (2027, at a 10-15% share of an $80B SAM) and beyond, as MediaTek's TPU scope escalates v8i → v9 and Google's explicit cost-down mandate entrenches it as the durable low-cost partner. ASIC + Nvidia-PC + automotive diversify the group away from mobile cyclicality, structurally justifying a higher multiple. Mobile stabilizes as Dimensity flagships reach Snapdragon parity outside the US and MediaTek pushes toward 40% share. The fabless model, net-cash balance sheet, and ~46% gross margin fund the entire build without dilution. Framework: the bull needs the aspirational end of the range (2027 data-center revenue near $8-10B vs the ~$3.2B in current sell-side models, at even 35-40% gross margin, with mobile holding) for group revenue to reach ~US$27-30B growing 20%+ and a sustained 40-50x multiple to leave room above US$190B. The bull requires ASIC to become a durable, margin-respectable $10B+ franchise: the outcome that retroactively earns the 55x.

## Bear Case

The ~2.7x re-rate reverses. ASIC revenue scales but at 30-40% turnkey gross margin (HBM/CoWoS pass-through), diluting group GM toward the low-40s; "ASIC > mobile by 2027" proves revenue-vanity with flat EPS. Google (the near-sole anchor, and by design the party whose whole purpose in hiring MediaTek is to cap silicon pricing) dual-sources aggressively and, in the 2028-29 AI-capex digestion ([[Macro & Technology/Sustainability of AI Capex]]), trims TPU volume; MediaTek's single-customer design-services backlog reprices like every other second-source. Simultaneously the mobile base erodes: Xiaomi XRing plus Chinese self-development (30%→60%) strip flagship sockets, the ~200% memory-cost surge and 10-15% price declines compress margins, and China subsidy-fade triggers an inventory correction. Growth decelerates, margins fall, and the multiple compresses from 55x toward its 15-20x history: the stock halves even if revenue grows. The $5B financing amplifies the downside if ASIC ROIIC disappoints.

## Catalysts

- **Q4 2026 (Oct-2026 print → Jan-2027):** first MediaTek AI accelerator mass production; data-center revenue toward the $2B FY26 target; initial FY27 ASIC guidance. (+/−)
- **Jan-Feb 2027:** hyperscaler calendar-2027 capex guidance, the key window in the AI-capex-sustainability framework; Google TPU volume/mix signal. (+/−)
- **2026-H2:** Nvidia N1X Arm-PC launch (Dell/HP/Lenovo/Asus); PC-TAM optionality. (+)
- **Q2-Q4 2026:** China smartphone demand post-subsidy + memory-cost trajectory, direct read on mobile margin. (−)
- **Late 2027:** TPU v8i "Zebrafish" mass production on TSMC N2; v9 "Triggerfish" progress. (+)
- **Q2 2026 onward:** Xiaomi XRing O2 (N3P) socket displacement at a major MediaTek customer. (−)

## Risks

- **Thesis risk (ASIC margin dilution):** data-center revenue scales at structurally lower gross margin than the group, making diversification revenue-accretive but value-neutral or dilutive. Breaks the "re-rate to compounder multiple" case.
- **Thesis risk (single-customer concentration, Google):** the data-center story rests on one anchor; loss, renegotiation, or a volume cut is existential to that leg (Semi #10 binary survival test).
- **Thesis risk (mobile erosion):** OEM vertical integration (Xiaomi XRing), Chinese domestic substitution, and the memory-cost squeeze structurally shrink both the funding base and core earnings.
- **Position risk (multiple compression):** at ~55x trailing on flat earnings, the stock is a duration bet; any AI-capex de-rating (the 2028-29 digestion) compresses the multiple regardless of MediaTek's own execution.
- **Structural dependency (Arm royalties):** MediaTek almost certainly licenses off-the-shelf Arm cores (TLA/CSS), not a custom ALA core like Qualcomm's Oryon, so it sits on the rising side of Arm's royalty-mix shift (Armv9 ~5% of ASP, CSS >10%, vs v8 ~2.5-3%) exactly as smartphone units are guided to flatten/decline. Royalty-per-unit rises while volume stalls; a move by Arm further up-stack (Compute Subsystems, own reference SoC) compounds it.
- **Structural dependency (TSMC two-front squeeze):** MediaTek's core smartphone platform is a shrinking TSMC segment (−4% QoQ; AI is pushing N3 allocation toward ~86% AI by 2027), while its ASIC ramp must win scarce CoWoS/advanced-packaging capacity TSMC reserves for higher-ASP anchors (NVDA pre-booked >50% of 2026 CoWoS at +20% pricing). Smaller TPU-inference volumes risk a structural packaging-queue disadvantage vs Broadcom: a headwind absent from consensus.
- **Geopolitical:** Taiwan concentration; US-China chip policy affecting Chinese-OEM customers and potential export constraints on advanced-node ASIC.

## Conviction Triggers

- **→ HIGH if:** data-center ASIC gross margin is disclosed/inferable at ≥45% AND a second hyperscaler ASIC anchor beyond Google is signed AND 2027 data-center revenue tracks ≥$8B — the franchise is durable, margin-respectable, and diversified.
- **→ LOW if:** group gross margin drifts below 43% as ASIC mix rises (turnkey-dilution confirmed), OR MediaTek's share of 2027 TPU units lands below ~15% (Broadcom re-consolidation), OR mobile revenue declines >15% YoY for two consecutive quarters on OEM in-sourcing.
- **→ CLOSE if:** Google materially re-consolidates TPU design to Broadcom or in-house and cuts MediaTek's data-center guidance, AND the mobile franchise loses a top-3 Chinese OEM's flagship socket to in-house silicon — both legs break together.

## Mental Models

- **Models applied:** [[Mental Models/Generalist - Overview]] ([G-13] expectations-investing, [G-7] ROIIC × runway, [G-3] mean-reversion vs trend, [G-10] base rates, [G-9] barbell/convexity, [G-4] Perez); [[Mental Models/Industry - Semiconductors]] (#2 qualification-gate monopoly, #10 anchor-customer concentration, #13/#14 classification, L3 second-source equilibrium, #15 subsidized-oligopoly margin dilution); [[Mental Models/Lens - Value Layer Monopoly]]; [[Mental Models/Lens - Automation & AI Readiness]] (Lens B: vendor of compute for the automation buildout); [[Lens - Management and Culture]].
- **Triggers that fired (hypotheses to test, not verdicts):**
  - Semi L3 · second-source equilibrium: *Google sustains MediaTek as the cost-down second source to cap Broadcom's TPU pricing (AMD-in-GPU / Marvell-in-switch analogue); MediaTek earns volume at second-seat margin. Test: does Broadcom retaliate on price or Google re-consolidate?*
  - Semi #10 · anchor-customer concentration: *data-center ASIC is ~single-anchor (Google): a binary survival test on that program, not diversification-grade revenue.*
  - Semi #13/#14 · classification: *market is reclassifying MediaTek from consumer-cyclical mobile toward compounder multiple (55x) on the ASIC narrative. Hypothesis: multiple has run ahead of proven economics; base rate ([G-10]) says abnormal multiples fade absent a durable earnings inflection.*
  - Value Layer Monopoly · layer identification: *MediaTek is a layer-RENTER (Arm ISA + TSMC fab below) and an ASIC second-source; NO/WEAK layer-monopoly fit. It is the commoditizer, not the toll-collector: a disconfirming datapoint against a toll-layer multiple.*
  - Generalist [G-13] · expectations-investing: *price embeds aggressive ASIC success at high margin; the mispriced variable is ASIC margin/mix + Google concentration + mobile erosion, not ASIC existence.*
  - Generalist [G-9]/[G-4] · convex option / Perez: *MediaTek is a convex bet on the AI-inference buildout funded by a mobile cash cow; the AI-capex digestion (2028-29) is the falsifier window for second-source design-services multiples.*
  - Management & Culture [MC-1] · gates: Gate 1 pass (ASIC/Dimensity/TPU/N1X feed); Gate 2 fail (~55× already prices the pipeline). Hypothesis: lens inert; conversion capacity is not the mispriced variable.
  - Management & Culture [MC-2] · incentive duration: 2025 RSA vests on TW50 relative TSR + revenue growth + operating margin, not ROIC or ASIC volume; founder ~5% residual, CEO 0.05%; no clustered open-market buys.
  - Management & Culture [MC-7] · product vs matrix: 22.9k employees YE2025, product/functional; Aug-2026 Intel/Qualcomm VP hires are talent import, not a matrix/product regime shift.
  - Management & Culture [MC-6] · bureaucratic entropy: 7.5-year tenure / 5.2% 2024 turnover at ~23k scale is the attractor, not evidence of fighting it.
- **Disconfirming check:** every momentum model (ASIC ramp, TPU v9 scope win, diversification) points the same way ("buy the transformation"), which per the READING PROTOCOL is the trigger to disconfirm, not to commit. The single falsifying datapoint is **data-center gross margin**: if the ASIC book is turnkey (HBM/CoWoS pass-through), group GM dilutes below ~46% as ASIC scales and "ASIC surpasses mobile by 2027" becomes revenue-up / value-flat. The base rate the thesis must beat: ~55x trailing on flat earnings is a multiple that reverts unless ASIC earnings inflect fast and durably, and the mobile cash cow funding that inflection is simultaneously eroding (Xiaomi vertical integration + memory squeeze). This is why conviction is medium, not high. The [MC-6] entropy plus [G-10] new-venture-destruction base rate is the default on a second-source ASIC build funded from an eroding mobile cash cow; Gate 2 already closed, so organisational conversion cannot raise conviction until the multiple no longer embeds the pipeline.

## Related Research

- [[Sectors/Custom Silicon & Networking Semiconductors]]: sector MOC; MediaTek framed as Google's third XPU partner / NVLink Fusion partner
- [[Theses/AVGO - Broadcom]]: TPU incumbent MediaTek is displacing at the cost-optimized end; the pricing-power counterparty
- [[Theses/MRVL - Marvell Technology]]: the other second-source design-services peer; second-seat margin template
- [[Theses/ARM - Arm Holdings]]: MediaTek's ISA licensor; royalty economics + up-stack competition risk
- [[Theses/TSM - Taiwan Semiconductor]]: foundry + CoWoS/advanced-packaging dependency for both mobile and ASIC
- [[Theses/NVDA - Nvidia]]: partner (N1X PC, GB10, Dimensity Auto, NVLink Fusion) and the GPU incumbent TPUs contest
- [[Macro & Technology/Sustainability of AI Capex]]: the digestion framework; MediaTek's inference/cost-down positioning tested against it
- [[Research/2026-07-10 - MRVL vs AVGO - Competitive Comparison]]: custom-ASIC competitive set
- [[Research/2026-06-05 - AI Silicon Shortage - N3 and Memory Constraint - deep-dive]]: MediaTek's exact foundry + memory-cost pressure
- [[Research/2026-05-31 - CPO Scale-Up Inflection and Supply Chain - deep-dive]]: scale-up fabric / NVLink Fusion context
- [[Research/2026-04-24 - Thomas Kurian on TPU Capacity Anthropic Hosting and Agentic Chip Design - video-transcript]]: Google TPU strategy + agentic chip design
- [[Research/2026-06-02 - Datacenter CPU Landscape 2026 - deep-dive]]: Arm PC / server-CPU context for N1X

## Log

### 2026-08-04
- Initial thesis created. Conviction: medium — Google TPU v8i→v9 scope escalation + cost-down mandate is a credible multi-$B convex option funded by a cash-generative mobile base, but the ~2.7x re-rate to ~55x already prices ASIC success while ASIC margin/mix is unproven and likely dilutive, revenue is single-customer-concentrated on Google, and the mobile funding base is eroding (Xiaomi XRing + memory squeeze) — does not clear the high bar.

### 2026-08-20
- Lens backfill: ## Management and culture from [[Lens - Management and Culture]] — hypothesis inert (Gate 2 fail); 55x already prices ASIC pipeline. Conviction unchanged.
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged
