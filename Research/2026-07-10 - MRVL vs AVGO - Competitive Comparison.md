---
date: 2026-07-10
tags: [research, comparison, custom-silicon, semiconductors, MRVL, AVGO]
sector: Custom Silicon & Networking Semiconductors
source: vault synthesis
source_type: comparison
propagated_to: [MRVL, AVGO]
---
 
# MRVL vs AVGO — Competitive Comparison

## Thesis Delta

**AVGO owns the layers of the AI-datacenter stack that everyone else must pay to traverse; MRVL owns exactly one durable layer and *rents* the layer where most of its growth story sits.** Broadcom decisively owns two — merchant Ethernet switching silicon (80–90% share, Tomahawk 6 two generations ahead) and the hardest custom-ASIC IP (224G SerDes analog franchise + CoWoS-L/HBM4 orchestration, ~60–70% ASIC share) — plus a third VMware software-annuity layer. Marvell owns one genuine layer (80%+ 800G optical DSP, the Inphi analog franchise) and occupies a *second-source procurement slot* at the custom-ASIC layer that is structurally capped ~5pp below Broadcom on gross margin. The July-2026 guide raises (AVGO FY26 AI $56B +180%, Q3 $16B +200%; MRVL FY28 $16.5B, custom silicon >$10B FY29) prove the second-source **category is compounding as fast as the incumbent** — so the AVGO-vs-MRVL gap is a **quality/margin gap, not a growth gap**.

Conviction implication: reaffirms both at high, but the conviction *spread* (AVGO = lower-variance compounder; MRVL = higher-variance, binary-optionality challenger) is justified by **layer ownership**, not by growth trajectory. Two vault framings fail on contact with the layer analysis: the May Rebalancing "EXIT MRVL" (stale — MRVL's numbers inverted positive since) and any "MRVL catching AVGO in custom ASIC" bull frame (wrong axis — MRVL's real forward edge is a *new* layer, memory-fabric photonics, that AVGO does not contest).

## Summary

Broadcom and Marvell are the two merchant silicon partners hyperscalers use to build non-Nvidia AI infrastructure, and they anchor the same sector note, share six research notes, and share a customer set (Google, Meta, AWS, Microsoft, OpenAI/Anthropic) and a supplier (TSMC). Against that shared baseline the divergence is unusually clean and structural: Broadcom is a cross-franchise incumbent whose switching + ASIC-IP + software layers reinforce each other (shared SerDes IP, shared packaging, shared TSMC allocation, shared hyperscaler relationships), and Marvell is a single-franchise-deep specialist attacking two of those layers separately while betting a third (memory disaggregation) becomes the next platform.

The financial signature confirms the structural read: Broadcom carries ~75% non-GAAP gross margin, 68% adjusted EBITDA, ~44% FCF conversion, and ~35% of revenue in recurring software; Marvell carries ~60% non-GAAP gross margin (Q1 FY27 58.9%), no software annuity, and 100% cyclical-semis exposure. Broadcom's ASIC margin (~65%) is the empirical proof that hyperscalers switching off Nvidia GPUs still pay most of the architectural rent to Broadcom; Marvell's ~60% ASIC margin is the second-seat ceiling, and its first-mover 1.6T LPO chipset is deliberately compressing its own ~65% DSP margin toward ~55% to retain unit share through the optical transition.

The verdict is not "which is cheaper" but which offers the better risk-adjusted skew. Broadcom is the higher-floor, lower-variance case: cheapest AI-complex name at ~23x forward, the hardest 2027 revenue visibility in the group ($73B backlog, ~3x book-to-bill), a switching-silicon chokepoint with near-zero in-sourcing risk, and a software annuity that decouples ~35% of revenue from the semi cycle. Marvell is the higher-convexity case: it trades at ~54x forward (≈2.3x Broadcom's multiple), pricing the bull path, and its asymmetry lives almost entirely in one binary — whether Celestial AI Photonic Fabric makes memory-pool disaggregation the 2027–2028 rack primitive and Marvell owns the only merchant scale-up-optical layer outside Nvidia NVLink. They are complements at the layer level (different bets) but substitutes at the risk-factor level (correlated Taiwan/TSMC tail and AI-capex beta) — owning both doubles those factors rather than diversifying them.

## Evidence

### Business Model Comparison

| Dimension | MRVL (Marvell) | AVGO (Broadcom) | Edge |
|-----------|-----------|-----------|------|
| Core revenue model | Fabless design-services + analog/optical IP; ~75% Data Center (custom-ASIC design services + optical DSP + Celestial photonic fabric) | Dual-engine: ~65% semis (custom XPU + 80–90% merchant switching) + ~35% infrastructure software (VMware/CA/Symantec recurring) | **AVGO** — software annuity decouples ~35% of revenue from semi cyclicality |
| Gross margin structure | ~60% non-GAAP (GAAP ~45%); Q1 FY27 58.9%; blended compression from custom-mix + LPO | ~75% non-GAAP; software GM 93%; ASIC ~65% | **AVGO** — ~15pp blended lead; second-seat ceiling caps MRVL |
| Customer concentration | AWS/Microsoft/Meta/Google across custom silicon; each seat contestable (lost Trainium 3 primary to Alchip) | 5+ XPU customers (Google, Meta, ByteDance, OpenAI, Anthropic) >60% AI rev; Apple RF ~15–20% | Even — both concentrated; different failure modes (in-sourcing vs seat-churn) |
| Recurring vs one-time | Low — design-services + chip shipments, cyclical | ~35% recurring subscription (VMware ARR +17–19%) + multi-year XPU roadmaps | **AVGO** decisively |
| Geographic mix | Global; ~100% leading-edge tapeouts on TSMC | China ~20% ($10.5B FY24); ~100% leading-edge on TSMC | Even (both carry the Taiwan tail) |
| Capital intensity | Fabless; elevated capex for Celestial integration + tapeouts | Fabless; FCF conversion ~44% | **AVGO** |
| R&D as % of revenue | High (design-services model) | Disciplined (Hock Tan playbook; ~$1.6M revenue/employee) | **AVGO** (capital-allocation discipline) |

### Competitive Position

| Factor | MRVL | AVGO | Edge |
|--------|-----------|-----------|------|
| Market share (custom ASIC) | ~13–25% (#2; Counterpoint ~25% by 2027) | ~60–70% (#1, undisputed) | **AVGO** |
| Market share trend | Second-source *category* growing; individual seats churn (lost Trainium 3) | Stable-to-widening; Google-share the one erosion vector (Macquarie models 95%→65% by 2028) | **AVGO** durable; MRVL category compounding |
| Pricing power trajectory | Capped at second-seat (~60% GM); LPO self-cannibalizes DSP (~65%→55% over 24mo) | Strengthening both franchises; 224G SerDes + CoWoS-L orchestration rent | **AVGO** |
| Technology moat depth | Long-reach optical DSP (Inphi 5-yr analog lead, 80%+ 800G) genuine; switching 2 gens behind (12.8T vs 102.4T) | 224G-SerDes analog franchise + switch-SoC integration; Tomahawk 6 2 gens ahead; CPO (Bailly/Davisson 50K+ shipped) | **AVGO** on switching/SerDes; **MRVL** on long-reach DSP |
| Switching costs | Moderate (design-in per program) | High + rising (per-generation ASIC architectural lock-in; VMware migration measured in years) | **AVGO** |
| Scale / network advantages | Sub-scale switching (Teralynx ~1.8M units cum. by 2028 vs Tomahawk tens of millions/gen) | Cross-franchise leverage (shared SerDes/packaging/TSMC allocation/hyperscaler relationships) | **AVGO** |
| Management quality / track record | Matt Murphy roll-up; Trainium 3 execution miss (RDL interposer defects) is a competence flag | Hock Tan — no missed major strategic target in 20 yrs; largest software-M&A margin expansion ever recorded | **AVGO** decisively |
| Insider alignment | CFO transition (Durn, ex-AMAT); outgoing CFO ~$60M Form 144 near the top | CEO comp tied to $60–120B AI-revenue milestones 2028–2030 | **AVGO** |

### Financial Comparison

| Metric | MRVL | AVGO | Notes |
|--------|-----------|-----------|-------|
| Market Cap | ~$215–272B (~$233 vault) | ~$1.81T | AVGO ~7–8x larger |
| Price (Jul 2026) | ~$233–310 (−27% off $329 peak) | ~$380 | Both re-rated then de-rated in the last ~5 weeks |
| Forward P/E | **~54x** (some sources 76x) | **~23x** (post Jun-3 derate) | MRVL ≈ 2.3x AVGO's multiple |
| Revenue growth (latest) | +28% YoY Q1 FY27 ($2.418B) | +48% YoY Q2 FY26 ($22.2B) | Both accelerating |
| Forward revenue | FY27 ~$11.5B (+40%); FY28 $16.5B (+45%); custom >$10B FY29 | FY26 AI $56B (+180%); Q3 AI $16B; >$100B FY27 AI | AVGO larger absolute; MRVL faster off a ~8x smaller base |
| Gross margin | ~59% (Q1 FY27) | ~75% non-GAAP | AVGO +16pp |
| Operating margin | Lower (design-services mix) | 68% adj. EBITDA | **AVGO** |
| FCF yield / conversion | ~1.5–2% yield (Apr vault) | ~44% FCF conversion | **AVGO** |
| Net cash / debt | — | VMware debt deleveraging, serviced by software FCF | **AVGO** |

> Both thesis Key Metrics tables are April-2026 vintage and flagged for refresh in their own Mental Models maintenance notes; the forward multiples above are July-2026 web-grounded. Run `/numbers MRVL` and `/numbers AVGO` to reconcile.

### Dynamic Analysis

**1. Market-share trajectory — structural or cyclical?** Both ride a structural tailwind (custom-ASIC TAM +45% CY26, ~$118B by 2033). Broadcom's ~60–70% share is defended by IP depth (224G SerDes, CoWoS-L orchestration, per-generation architectural lock-in) — structural. Marvell's second-source slot is *also* structural, but defended by procurement logic (no hyperscaler accepts single-vendor lock-in), not product merit — and the same logic that hands Marvell the slot caps its margin. Individual seats are contestable: Alchip won the Trainium 3 primary on Marvell's RDL-interposer miss. Net: both structurally advantaged; only Broadcom's share is defended by an un-replicable asset.

**2. Pricing-power divergence.** Broadcom strengthening across both franchises; Jensen Huang's own "ASIC margin ~65% vs Nvidia ~70% — what are you really saving?" is the unintended tell that Broadcom captures the Nvidia rent hyperscalers thought in-sourcing would eliminate. Marvell is structurally capped at the second-seat (~60% GM) *and* is deliberately compressing its own DSP margin (65%→55% blended over 24 months) by shipping 1.6T LPO first to retain unit share. Divergence driver = layer ownership: Broadcom prices the hard IP; Marvell trades margin for share retention.

**3. Technology trajectory — who is on the right side of the next platform shift?** Three contested layers. (i) Scale-out switching → **Broadcom owns it** (Tomahawk 6, Jericho 4 scale-across, Davisson CPO). (ii) Scale-up fabric → NVLink Fusion (Marvell captive via the $2B Nvidia deal) vs UALink vs Broadcom's SUE/Tomahawk Ultra — Broadcom is the only merchant scale-up silicon shipping in volume and is hedged; Marvell is *contained* inside NVLink (and quietly hedging via the XConn/UALink acquisition). (iii) Memory-fabric photonics → **Marvell's genuine asymmetric edge** (Celestial AI Photonic Fabric, the only merchant scale-up-optical option outside NVLink; a tier-1 hyperscaler selected the Gen-1 chiplet, per the May-27 call) — a layer where Broadcom is *not present*. Marvell's forward edge is a NEW layer, not catching Broadcom on existing layers.

**4. Logical tension — what must each need true that the other's success disproves?** Marvell's bull needs memory disaggregation to become the 2027–2028 rack primitive with Celestial owning the merchant layer — Broadcom's success does not disprove this (Broadcom isn't in memory-fabric). Broadcom's bull needs switching + ASIC-IP layer ownership to hold — Marvell's DSP/memory-fabric success does not disprove it. **They can both win** because they win different layers. The zero-sum "MRVL catching AVGO in custom ASIC" frame is the wrong axis; Marvell's real binary (Celestial) is orthogonal to Broadcom.

**5. Scenario divergence — when does the underdog win bigger?** If memory disaggregation validates 2027–2028 and Celestial is the merchant winner, Marvell captures a *new* $15–25B 2030 TAM at 30–40% → multi-bagger on the $3.25B purchase; that is the one scenario where Marvell out-returns Broadcom. But the July CXL update is a caution flag: NVLink + Ethernet-attached NAND (Nvidia CMX/BlueField-4) and HBF are capturing the marquee KV-cache socket, confining CXL/photonic to a contested middle tier (contradictions #2/#9 upgraded). Broadcom wins the base case (rack stays copper + NVLink + HBM-on-package) via switching dominance regardless of the memory-fabric outcome.

**6. Customer & supplier overlap.** Shared customers: Google, Meta, AWS, Microsoft, OpenAI/Anthropic (all XPU). At Google specifically Broadcom holds a through-2031 co-lead lock while Marvell is third-seat behind MediaTek — Broadcom has more pricing power in the shared relationship. Shared supplier: TSMC (~100% of both companies' leading-edge tapeouts) → **correlated Taiwan tail** (−85–95% permanent impairment in an invasion scenario, per the TSM stress test) and correlated HBM/CoWoS allocation risk. Owning both concentrates, not diversifies, this exposure.

## Framework / Mental Model

Applies [[Mental Models/Lens - Value Layer Monopoly]] (load-bearing here), [[Mental Models/Industry - Semiconductors]], and [[Mental Models/Generalist - Overview]] as lenses — entries are hypotheses to test, not verdicts (per the READING PROTOCOL).

- **Value Layer Monopoly.** AVGO = **STRONG FIT**: owns the switching-silicon layer (interface/standard control via UEC) + the hardest-ASIC-IP layer (224G SerDes); infrastructure layer → moat *widening* under cheap intelligence; disqualifier flag = the political/geopolitical ceiling (VMware antitrust/CISPE, China, strategic salience at $1.8T). MRVL = **layer-renter at the ASIC seat** (rents hyperscaler sockets above, sits inside the Nvidia NVLink perimeter beside) but **STRONG at the narrower optical-DSP layer** and running a binary bet on *owning* the emerging memory-fabric layer (Celestial). Hypothesis to test: Marvell's real owned layer is the optics/DCI franchise (~$1B DCI FY28, 70–80% DSP share), not the ASIC seats.
- **Industry-Semiconductors #2 (qualification-gate monopoly):** both hold genuine gates — AVGO's 224G-SerDes analog franchise (BER <1e-15 vs ~1e-12, <500 senior >100G-PAM4 designers worldwide) and MRVL's Inphi optical-DSP lead. **#13 classification:** AVGO = structural compounder (dual semis + software); MRVL = semi-cyclical challenger. **#10 anchor concentration:** binary at top customers for both.
- **Generalist [G-6] monopoly characteristics:** AVGO scores higher — switching silicon is software-like (near-zero marginal cost, standard control). **[G-13] expectations:** the market prices MRVL (~54x fwd) for the bull path and AVGO (~23x fwd) for base-case-plus; the operating variable that must resolve for MRVL to earn its multiple is Celestial/memory-fabric validation, not custom-ASIC share.
- **Disconfirming check (models agree AVGO is higher-quality → hunt the flip):** MRVL's business ran *ahead* of its own bull case since May (FY28 raised to $16.5B, custom >$10B FY29), the memory-fabric layer is a new TAM AVGO does not contest, and Jensen calling MRVL a "trillion-dollar candidate" is a reflexive tailwind ([G-3]). The single falsifier of "AVGO strictly better": Celestial memory-fabric becomes the 2027–2028 rack primitive and MRVL owns the merchant layer.

## Investment Verdict

- **Risk-adjusted asymmetry:** AVGO = higher-floor, lower-variance compounder (software annuity + switching monopoly + hardest 2027 visibility, cheapest AI-complex name at ~23x fwd). MRVL = higher-variance, binary-optionality challenger (memory-fabric upside real but contested; ~54x fwd already prices the bull path; second-seat margin ceiling). AVGO offers better downside protection; MRVL offers more convexity *conditional on* Celestial validating.
- **Portfolio role — complements at the layer level, substitutes at the risk-factor level.** Different bets (AVGO: switching + ASIC-IP + software; MRVL: DSP + memory-fabric) but correlated Taiwan/TSMC tail and AI-capex beta. Owning both doubles those factors = hidden concentration, not diversification. Core-compounder sleeve → AVGO; MRVL only as a sized convex bet on memory disaggregation.
- **Preference trigger (falsifiable):** shift *toward MRVL* if (a) Celestial books a **second** named tier-1 scale-up win + on-schedule end-2026 tape-out AND (b) Structera/CXL attach converts to disclosed customers — evidencing Marvell owns the emerging memory-fabric layer. Shift *further toward AVGO* if Google discloses Broadcom custom-ASIC share **<70% for 2027** (the one crack in AVGO's layer ownership), OR AVGO FQ3 (~early Sept) reaffirms >$100B 2027 AI on the chips-only basis.
- **Conviction gap:** both high; the spread is justified by layer ownership (AVGO low-variance owned layers + software; MRVL high-variance business-outrunning-thesis + binary Celestial). The May Rebalancing EXIT-MRVL call is stale (MRVL's numbers inverted positive on the Q1 FY27 beat + guide raise), but its *relative* ranking (AVGO higher-quality) survives the layer analysis. Maintenance: reconcile MRVL Summary "medium" text vs `high` frontmatter; `/numbers` both to refresh April-vintage Key Metrics.

## Contradiction Check

- **Flips toward MRVL:** memory disaggregation validates as the 2027–2028 primitive with Celestial as merchant winner — *but* the July CXL update shows NVLink + Ethernet-NAND capturing the marquee KV socket, narrowing the merchant memory-fabric TAM ([[Macro & Technology/CXL Memory Disaggregation Framework]] contradictions #2/#9). Probability medium.
- **Flips further toward AVGO:** Google-share migration proves priced/overblown, and the chips-only revenue pivot is confirmed margin-accretive/optics-negative (bookings >$30B vs $10.8B shipped, ~3x b2b, say demand intact — the Jun-3 −12.6% was optics not demand).
- **Stale-data risk:** the May Rebalancing figures used to rank MRVL "EXIT" (negative ROIC NTM, −0.1% rev growth) are pre-Q1-FY27-beat and inverted; this verdict uses July web-grounded multiples, flagged. Both Key Metrics tables need `/numbers`.
- **Correlated-risk caveat:** owning both is not diversification — shared TSMC/Taiwan tail, shared HBM/CoWoS allocation, shared AI-capex beta, overlapping hyperscaler customer set.

## Related Research

- [[Theses/MRVL - Marvell Technology]] — thesis A anchor
- [[Theses/AVGO - Broadcom]] — thesis B anchor
- [[Sectors/Custom Silicon & Networking Semiconductors]] — shared sector MOC (competitive dynamics, second-source-ceiling framing, value-chain table)
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]] — ranked AVGO UPSIZE / MRVL EXIT (May vintage — MRVL leg since inverted by guide raise)
- [[Research/2026-05-31 - CPO Scale-Up Inflection and Supply Chain - deep-dive]] — scale-up CPO; Celestial $1B CY2028 into Trainium 4; Broadcom → TSMC COUPE migration
- [[Macro & Technology/CXL Memory Disaggregation Framework]] — memory-disaggregation TAM + July contradiction upgrades (NVLink/NAND capturing KV socket)
- [[Research/2025-11-29 - AVGO - Gemini Investment Analysis Canvas]] — "Android to Nvidia's Apple"; Hock Tan aggregation playbook; AVGO/MRVL forward-multiple context
