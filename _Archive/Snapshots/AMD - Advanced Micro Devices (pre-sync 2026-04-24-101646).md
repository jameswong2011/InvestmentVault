---
date: 2026-04-21
tags: [thesis, semiconductors, AMD]
status: active
conviction: medium
sector: GPU & AI Compute Accelerators
ticker: AMD
source: AMD Q4 2025 earnings (Feb 2026), MLPerf Inference v6.0 (Apr 1 2026), OpenAI 6GW deal (Oct 2025), Meta 6GW deal (Feb/Mar 2026)
snapshot_of: "[[Theses/AMD - Advanced Micro Devices]]"
snapshot_date: 2026-04-24
snapshot_trigger: sync
snapshot_batch: sync-2026-04-24-101646
---

# AMD - Advanced Micro Devices

## Summary

AMD is the sole merchant full-stack alternative to Nvidia at a moment when every hyperscaler has concluded it cannot afford single-source GPU dependence. The OpenAI 6GW deal and Meta 6GW deal signed inside 5 months were not won on hardware merit — they were engineered by customers who needed a duopoly to restore pricing leverage against Nvidia. AMD traded 10% of its equity (OpenAI warrant at $0.01 over 160M shares) to lock itself in as the structural second source, converting a GPU supply contract into a decade-long capital alignment. At ~$453B market cap and 38–41x forward P/E the stock prices in flawless execution on the MI400/MI450/MI500 roadmap, continued EPYC share capture (41% Q2 2025 tracking toward parity with Intel), and ROCm reaching effective CUDA parity by H2 2026 — each individually plausible, the combination tight. The non-consensus case is that the hyperscaler-initiated diversification mandate is structurally mispriced as a cyclical market-share trade when it is actually a durable rewiring of AI infrastructure procurement. The bear case is that the OpenAI warrant is dilution, the MI400 is one generation behind Rubin, the ROCm asymptote is farther than disclosed, and the valuation embeds a second-source premium that vanishes the moment Nvidia cuts prices.

## Key Non-consensus Insights

**1. The OpenAI/Meta deals reflect hyperscaler-imposed diversification, not GPU merit — and the market prices them as cyclical wins instead of a structural rewiring.** OpenAI and Meta each signed 6GW multi-year commitments inside 5 months despite the MI355X being within single-digit percent of Nvidia B200 on benchmarks and the MI450 being ~1 generation behind Rubin/GB300. The operative variable is not AMD's hardware — it is the hyperscalers' refusal to accept a 70%+ gross-margin supplier as a single source after Nvidia's H200/B200 allocation became the gating constraint on their 2025–2026 capex. The OpenAI warrant structure (160M shares at $0.01, vesting across deployment milestones) is financial engineering that converts procurement into equity alignment — a structure Nvidia cannot replicate because it has no need to. Consensus still models AMD's AI revenue as "share gain vs. total AI TAM" when the correct model is "share gain vs. what hyperscalers are willing to single-source from Nvidia," which is a smaller and more durable denominator. The 10% dilution from OpenAI is not a cost — it is the price of a decade of guaranteed demand that prevents AMD from needing to compete on price against Nvidia's 75%-share volume.

**2. AMD is the only company with the complete Nvidia rack-level stack outside Nvidia itself — and the market still prices it as a GPU-only story.** The Helios rack (Q3 2026, 72 MI455X, 31TB HBM4, 3 AI exaflops) combines EPYC Venice 2nm host CPU, Instinct MI450 accelerator, Pensando Pollara 400 DPU (first UEC-ready AI NIC, already deployed at Azure/Oracle/IBM), and Infinity Fabric scale-up — mirroring Nvidia's Grace + Blackwell + ConnectX + NVLink rack architecture one-for-one. Broadcom has switching silicon but no GPU. Marvell has custom ASIC design services but no merchant accelerator. Intel has no credible AI accelerator and exited merchant switching. ARM CPUs (Ampere, Graviton) lack merchant-market GPUs. AMD is the only company with merchant CPU + merchant GPU + merchant DPU + advanced packaging access + Xilinx FPGA for pre/post-processing. This configuration matters because hyperscalers increasingly buy rack-level not chip-level. Consensus benchmarks AMD vs. Nvidia on chip specs; the competitive surface is actually rack-to-rack integration where AMD is the sole credible merchant alternative to Nvidia's MGX.

**3. The ROCm catch-up is asymmetric and step-function, not asymptotic — the ecosystem gap narrows in framework-release cycles, not compute-parity curves.** Consensus treats ROCm as forever 12–24 months behind CUDA. Empirically, MLPerf Inference 6.0 (April 1, 2026) showed the MI355X hitting 97% of B200 on Llama 2 70B Server, 111% on GPT-OSS-120B Offline, and multi-node 1M+ tokens/sec with 93–98% scale-out efficiency. PyTorch now natively supports ROCm; vLLM, SGLang, Triton inference stacks target ROCm as a first-class backend. Framework-level parity means the marginal workload port from CUDA → ROCm approaches zero friction once the top-5 inference stacks adopt ROCm — which Meta's 6GW production deployment forces to happen by late 2026. Market continues to treat ROCm improvements as asymptotic linear gains when they are actually step-functions tied to each major framework release. The step into "70% of net-new inference workloads are framework-native and GPU-agnostic" has already happened; the market has not repriced it.

**4. Xilinx is free optionality that the market writes down to zero — but sovereign AI and defense buildouts are creating a structural FPGA tailwind the integrated AMD entity can monetize and Xilinx-standalone could not.** Embedded revenue was $823M in Q1 2025, down 2.7% YoY — consensus sees the $49B Xilinx acquisition as destroyed capital. The non-consensus view: sovereign AI programs (EU, UAE, Saudi Humain, India) require US-domiciled reprogrammable silicon for pre/post-processing, signal conditioning, and certification-constrained workloads where ASICs cannot be used. Defense spending on programmable silicon is entering a supercycle (hypersonics, autonomous systems, EW) and the US government will not buy Chinese FPGAs. AMD's integrated GPU+FPGA+CPU offer sells into these workloads as a bundle that Xilinx-standalone could never close. Embedded recovery to +10% growth gets to ~$4B revenue at mid-50% gross margin — a line item the current multiple attributes no value to.

**5. Inference margin economics favor AMD, not Nvidia, once HBM is the scarce input — and the market still prices HBM-per-dollar as a cost disadvantage instead of a strategic allocation advantage.** MI350 ships 288GB HBM3E at 8 TB/s, materially more HBM per package than NVDA H200/B200. For inference workloads, which will be 60–80% of AI compute by 2028, memory capacity — not FLOPS — determines throughput. HBM supply is structurally tight: SK Hynix and Samsung are diverting 40% of advanced wafer capacity from NAND, HBM4 capex in 2026 is $61.3B vs. NAND $22.2B, and NAND fab shortage forces HBM to accept wafer-share tradeoffs. AMD's 11% CoWoS allocation appears small vs. Nvidia's 60–65%, but the effective HBM-per-rack allocation at Helios spec (31TB/rack) is disproportionately large because AMD loaded more HBM per GPU. Consensus sees this as commoditization of inference (bad for Nvidia margins); it is actually a structural reallocation of inference-market spend toward the vendor with more HBM packaged per GPU, which is AMD.

## Outstanding Questions

**1. What is the realized cost of the OpenAI warrant dilution at various share-price realizations, and does management have clawback or milestone-recalibration protection?** 160M shares at $0.01 fully diluted at current $278 is ~$44.5B of value transfer. Warrant vests across deployment milestones through October 2030. If AMD's AI revenue hits the $100B cumulative "related hyperscale" framing OpenAI referenced, the effective cost-of-capital is highly favorable; if AI revenue disappoints, dilution compounds into a falling share price. The 10-K should disclose milestone structure — what cumulative GW deployment triggers which tranche? What is management's cumulative EPS dilution forecast 2026–2030? A "pro forma AI revenue per fully-diluted share" disclosure in the next quarterly filing would resolve most of this.

**2. Is the MI450/Helios actually rack-for-rack competitive with Rubin/GR200, or one generation behind at H2 2026 launch?** Helios specs (3 AI exaflops/rack, 72 MI455X, 31TB HBM4) compare favorably to NVL72 Blackwell Ultra on paper but Nvidia will be shipping Rubin GR200 racks in H2 2026 with substantially higher performance per rack and 10x lower inference cost per token. If Helios ships against Rubin (not against Blackwell), AMD's 5–8% AI share target for 2026 is at risk even with OpenAI/Meta commitments. A direct MLPerf Training v5.0 result from both platforms at launch would resolve — but AMD has historically under-submitted to Training benchmarks, suggesting the gap is real.

**3. How contractually firm are the OpenAI and Meta 6GW commitments — take-or-pay, best-efforts, or cancellable on hardware underperformance?** A 6GW nominal commitment that converts to 2GW actual deployment if MI450 underdelivers is worth one-third of the headline. Hyperscaler GPU orders historically contain performance-adjustment clauses tied to MLPerf or internal benchmarks. Meta specifically has a track record of canceling supplier commitments (see Broadcom's 25.6 Tbps switch cancellation, MTIA delays). If 6GW is <50% take-or-pay, the OpenAI warrant is structurally mispriced. Management has not disclosed the firmness breakdown.

**4. Can AMD capture >15% CoWoS allocation for 2027, or is Nvidia's 60–65% share structurally defended via TSMC prepayments?** Nvidia has $45B+ in HBM prepayments with SK Hynix/Samsung plus multi-year CoWoS capacity reservations with TSMC. AMD's 11% 2026 allocation suggests continued subordinate positioning even with OpenAI/Meta demand. If AMD cannot grow CoWoS share to 20%+ by 2027, the $100B AI revenue framing is arithmetically impossible — at current wafer economics, AMD's AI TAM capture is capped by packaging capacity, not demand. Quarterly TSMC capacity disclosures (via earnings call color commentary) will be the leading indicator.

**5. Will ROCm reach training parity (not just inference) by end-2026, or does training remain a CUDA-locked workload through 2027?** MLPerf Inference 6.0 showed 93–111% of B200 performance on specific workloads, but AMD notably did not submit MLPerf Training v4.0 results in 2025. Training workloads require substantially more framework integration, distributed scaling, and mixed-precision optimization than inference. If training remains CUDA-locked through 2027, AMD's share gain caps at the inference segment — large but not transformational at AMD's current market cap embedding. Meta's ROCm-based production training of Llama 5 would be the proof point; absent that, training-parity claims should be discounted.

**6. What is the steady-state gross margin impact of the OpenAI/Meta deals — cost-plus pricing, volume discount, or full margin?** Hyperscalers historically extract 10–20% gross-margin concessions on multi-year volume commitments. If AMD's 55% non-GAAP gross margin contracts to 45% on hyperscaler-weighted mix, EPS growth decelerates even with revenue scaling. Consensus models 57% gross margin expansion through 2027 — the 6GW deal structure may preclude this.

**7. Is EPYC share gain durable against Intel 18A Clearwater Forest, or does Intel's process lead reclaim share in 2027?** Intel 18A (scheduled 2026 production) and Clearwater Forest E-core server (2027) represent the first credible Intel counterpunch since Zen 3. If Intel 18A delivers on performance/watt claims, AMD's 41% → 50% server share trajectory stalls or reverses. Venice (2nm TSMC) vs. Clearwater Forest (18A) is the next-18-month battle that determines whether EPYC is a structural share gainer or a cyclical one.

**8. What happens to AMD's client/gaming segment if Nvidia enters PC gaming CPUs via the Arm+MediaTek stack in 2026–2027?** Nvidia + MediaTek announced a consumer PC CPU+GPU+NPU chip (Project Digits derivatives). If this ships in 2027 and captures 10% of premium gaming PCs, AMD's Ryzen monopoly on enthusiast PC gaming erodes. Client segment is ~25% of revenue and ~50% of stock beta; share loss here offsets data-center gains.

## Business Model & Product Description

AMD designs and licenses x86 CPUs, discrete GPUs, AI accelerators, DPUs, and FPGAs, with fabrication outsourced entirely to TSMC (leading-edge) and Samsung (legacy). The closest analogy is Nvidia's fabless model — AMD is more vertically integrated into CPU and FPGA than Nvidia but less integrated on software/platforms. Compared to Intel, AMD is more capital-light and more process-agile (TSMC N2 in 2026 vs. Intel 18A) but dependent on foundry allocation.

**Four reported segments (Q4 2025 mix):**

| Segment | Share of revenue | Primary products | Economics |
|---|---|---|---|
| **Data Center** | ~52% | EPYC server CPUs (Milan/Genoa/Turin/Venice), Instinct AI accelerators (MI300/MI350/MI355/MI400 series), Pensando DPUs | Gross margin 55–60%, growing 40%+ YoY, primary AI/hyperscaler exposure |
| **Client** | ~25% | Ryzen desktop CPUs (Zen 4/5/6), Ryzen mobile APUs, Ryzen AI NPU | Gross margin 45–50%, cyclical, premium consumer/enthusiast PC exposure |
| **Gaming** | ~12% | Radeon RX discrete GPUs, semi-custom SoCs (PlayStation 5/6, Xbox Series X/S), Navi architecture | Gross margin 15–25%, low-margin volume console royalties + merchant discrete GPU |
| **Embedded** | ~11% | Xilinx FPGAs (Versal, UltraScale+), adaptive SoCs (VP1902), aerospace/defense/industrial | Gross margin 60%+, cyclical recovery from 2024 trough |

**Revenue-generating product tiers within Data Center:**

- **EPYC server CPUs**: Top-of-stack Genoa/Turin/Venice target hyperscaler and enterprise compute — competes directly with Intel Xeon, capturing share on core count (128+ cores), memory channels (12), and energy efficiency. 41% server CPU market share Q2 2025, tracking toward parity with Intel by 2026. EPYC Venice on TSMC N2 (2026) is the next architectural leap.
- **Instinct MI series**: MI300X/MI325X shipping at scale with 2–3 hyperscalers (Azure, Oracle, Saudi Humain) contributing 5–8% of AI GPU share. MI350/MI355X (CDNA4, 288GB HBM3E, 8 TB/s, 2026) is the current flagship — MLPerf-validated within single-digit % of B200. MI400/MI450/MI455X (2026 launch, H2) target rack-scale deployment with Helios. MI500 promised for 2027 with "1000x AI performance" marketing claim.
- **Pensando DPU**: 400G networking silicon (Pollara 400) deployed at Microsoft Azure, Oracle Cloud, IBM Cloud. First Ultra Ethernet Consortium-ready AI NIC. Competes in the DPU category with Nvidia BlueField, AWS Nitro (captive), and Broadcom Jericho3/Tomahawk5 (switching-adjacent).

**Helios rack-scale product (Q3 2026 launch)**: Double-wide rack with 72 MI455X accelerators, 31TB HBM4, 3 AI exaflops per rack. Direct competitor to Nvidia GB200 NVL72 / GB300 / Rubin GR200 racks. Combines EPYC Venice host + MI455X + Pensando + Infinity Fabric scale-up. This is the first rack-scale product where AMD owns the full stack top-to-bottom and the market for competitive comparison is rack-to-rack, not chip-to-chip.

**Commercial model**: Direct to hyperscaler (ODM-integrated), OEM channel (Dell/HPE/Lenovo/Supermicro), and increasingly direct SKU sales at megadeal scale (OpenAI, Meta 6GW). Warrant-linked megadeals (OpenAI 160M shares at $0.01) are a novel commercial innovation converting volume commitments into equity alignment.

## Industry Context

**Competitive structure**: AI accelerator market is a consolidating duopoly (Nvidia ~75% share, AMD 5–8%, ASICs 15–20%) with hyperscalers actively working to prevent further Nvidia consolidation. Server CPU is a duopoly tracking to 50/50 by 2026 (AMD/Intel). Discrete GPU consumer is Nvidia-dominant (~85%); discrete GPU enterprise is the AI accelerator market. DPU is a fragmented oligopoly. FPGA is a duopoly (AMD/Xilinx + Altera standalone after Intel spin).

**Value-chain leverage**:

| Layer | Who has leverage | AMD position |
|---|---|---|
| Fab capacity (TSMC N3/N2) | TSMC — allocates to NVDA 60–65% of 2026 CoWoS, AMD 11% | Subordinate |
| Advanced packaging (CoWoS) | TSMC (monopoly), BESI (42% die attach) | Subordinate to NVDA allocation |
| HBM supply | SK Hynix 57%, Samsung, Micron | AMD preferred on MI350 for Micron — structural advantage |
| Network fabric | Nvidia (NVLink/NVSwitch captive), Broadcom, AMD Pensando | Merchant alternative to Nvidia |
| Software stack | Nvidia CUDA (5.9M dev) vs. AMD ROCm (improving) vs. open-source/vendor-specific | Closing gap via framework-native adoption |
| Physics/simulation | Nvidia PhysX/Warp/Omniverse — no merchant equivalent | No product, no roadmap |
| Sovereign AI | US-domiciled suppliers only | Strong (US-HQ, no China exposure) |

**Structural forces reshaping the industry**:

1. **Hyperscaler-enforced diversification**: OpenAI, Meta, Oracle, and Azure have publicly committed to dual-sourcing AI compute. This is a mandate-driven revenue stream for AMD that would not exist on hardware merit alone.
2. **ASIC threat to merchant GPU**: Google TPU v7 (~70% cost reduction), Trainium 30–40% better price-performance, Meta MTIA (delayed but coming), Groq LPU. ASICs chip away at inference-optimized merchant GPU share. AMD is structurally exposed to this — ROCm being open-source means any ASIC vendor can use AMD's ecosystem work without compensating AMD.
3. **CoWoS-centric supply curve**: Packaging capacity, not wafer fabrication, is the binding constraint. Whoever has CoWoS allocation ships; whoever doesn't defers. NVDA locked in 60–65%; AMD has 11%. Share expansion at AMD requires TSMC to build more CoWoS capacity than NVDA reserves.
4. **ROCm step-function adoption**: Framework-native support (PyTorch, vLLM, SGLang, Triton) converts ecosystem parity from multi-year to multi-quarter timelines.
5. **Taiwan geopolitical tail**: MI400 series manufactured at TSMC N3/N2. Any Taiwan disruption hits AMD's AI revenue as severely as it hits NVDA's — and AMD has less Arizona/Japan optionality.

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | ~$453B | Price $278.39 (April 17, 2026), ~1.63B shares diluted pre-warrant |
| EV/Revenue | ~13x | TTM revenue ~$32B (Q4 2025 run-rate annualized); forward ~$40B+ implies EV/Rev dropping toward 11x |
| Revenue Growth | +34% YoY Q4 2025; +32% YoY Q1 2026 guided | Data Center +40%+ YoY; guided >60% CAGR 3–5 years |
| Gross Margin | ~55% non-GAAP Q4 2025 | 45–55% client/embedded, 55–60% data center, 15–25% gaming drag |
| FCF Yield | ~1.5% | Elevated capex for TSMC/HBM prepayments; OpenAI warrant dilution adds shadow cost |
| Forward P/E | 38–41x | Sector median ~31x; 23% premium reflects AI growth but embeds execution |
| AI Revenue Guidance | "Tens of billions" FY2027; $100B cumulative with hyperscaler bucket | OpenAI management framing, not formal guidance |
| Data Center share of revenue | >50% | First quarter in AMD history |
| Server CPU market share | 41% Q2 2025 | Tracking to parity with Intel by 2026 (Mercury Research) |
| AI GPU market share | 5–8% | Target 15–20% by end-2026 (Lisa Su public framing) |
| CoWoS allocation (2026) | ~11% | Nvidia 60–65%; structural bottleneck on AI revenue ceiling |

## Bull Case

**Price target framework**: If AMD captures 15% AI GPU share by end-2027 on a $400B AI accelerator TAM, AI revenue alone is $60B. At 55% gross margin and 35% operating margin, AI operating income is ~$21B. Combined with $30B of CPU/client/embedded operating income at mid-cycle, total operating income is $50B+. At a 30x multiple (derate from current on scale normalization), market cap is $1.5T — up >3x from $453B over 2–3 years.

**Drivers that have to go right**:

1. **OpenAI 6GW deploys on schedule H2 2026 → full ramp 2028**: MI450 and Helios hit deployment milestones; OpenAI warrant vests; other hyperscalers (Google, AWS, Microsoft expanded) follow the OpenAI precedent and sign similar megadeals. Each major hyperscaler commitment is worth $20–30B over 3–5 years.
2. **ROCm reaches de facto CUDA parity for training by end 2027**: Meta deploys Llama 5 on ROCm at scale; AWS adds ROCm support in Bedrock; enterprise adoption follows. Inference-first adoption compounds into training adoption once framework-native parity becomes production-proven.
3. **EPYC passes 50% server CPU share by end 2026**: Venice 2nm launch outperforms Intel Clearwater Forest / 18A; AMD becomes the incumbent rather than the challenger. Server CPU revenue doubles by 2028 at mid-cycle.
4. **Pensando DPU scales to a $2–3B business by 2027**: UEC standardization drives hyperscaler adoption beyond Azure/Oracle/IBM to Google and AWS (displacing Nitro captives at the margins). Ultra Ethernet becomes the dominant AI rack fabric.
5. **Xilinx embedded returns to 10%+ growth via sovereign AI and defense**: Current $3.2B annualized run-rate grows to $5B+ by 2028 at 60%+ gross margin as EU, UAE, Saudi, Indian sovereign programs order US-domiciled FPGAs.
6. **Inference becomes the dominant workload (60–80% of AI compute by 2028) and AMD's memory-per-dollar advantage wins**: MI350/MI400 HBM capacity advantage positions AMD as the inference-optimized merchant choice. ROCm is sufficient for inference even if training stays CUDA-dominant.

**Valuation anchor**: 25x 2028E EPS of $22–25 implies $550–625 share price, approximately 2x upside on a 2-year horizon. Plus-case of ROCm full parity + ASIC containment + EPYC 60% share implies $700+.

## Bear Case

**Downside scenario**: AMD ships MI450 into a Rubin/GR200 market, OpenAI warrant overhang compounds dilution, ROCm plateaus at 85% CUDA parity without crossing the training threshold, ASIC inference share (Google TPU, Trainium, Groq) scales faster than AMD's merchant GPU share, EPYC share gains slow as Intel 18A ships, and the 38x forward P/E derates to sector median 25x as growth rate decelerates.

**Drivers that cause this**:

1. **MI450 Helios launches against Rubin, not Blackwell**: Nvidia's Rubin GR200 ships H2 2026 with materially better performance per rack than Helios. Hyperscalers that made commitments on "second source" strategy discover the second source is 30% slower at similar cost, and take-or-pay clauses are renegotiated. Apparent 6GW deals convert to 2–3GW realized.
2. **ROCm hits the training wall**: Inference parity is achievable; training parity is a different problem involving distributed scaling, mixed-precision communication, and 100k+ GPU cluster stability. If ROCm plateaus at 70% of CUDA training performance by end 2027, AMD caps at inference-only share (maybe 10–12% of a smaller denominator).
3. **OpenAI warrant becomes a dilution death spiral**: Each tranche vests regardless of AMD share price; if AI revenue misses and AMD falls to $150, dilution is less nominal but more real as book value compresses and the company trades closer to a cyclical semi (15x P/E) than a growth semi (35x+). Fully diluted share count could be ~10% higher by 2030.
4. **ASICs eat inference faster than consensus**: Google TPU v7 + v8, Trainium 3 + 4, Meta MTIA (if it ever ships), Apple AXP, and Groq all target inference. If 40% of 2028 inference is ASIC-served, merchant GPU TAM compresses and AMD's 15% share becomes 15% of a smaller pie.
5. **Intel 18A Clearwater Forest is legitimate**: If Intel delivers on 18A performance/watt, AMD's 41% server share peaks and drifts to 35% by 2028. Given CPU is 25%+ of revenue, this flattens the integrated story.
6. **Taiwan tail**: Any blockade or disruption at TSMC N3/N2 fabs directly hits MI450/MI500 supply. AMD has less Arizona optionality than Nvidia (which has Arizona + Japan capacity reservations).
7. **Valuation compression**: At 38x forward P/E and sector median 31x, AMD is pricing in 25%+ structural growth persistence. If AI revenue flattens in 2028 at $40B (not $80B), the multiple compresses to 22x on $15 EPS = $330 share price, ~18% downside from current.

**Bear-case price target**: $180–220 on 2-year horizon if 2–3 of the above materialize.

## Catalysts

| Date | Catalyst | Direction |
|---|---|---|
| Early May 2026 | Q1 2026 earnings (~$9.8B guide) | ±5% on DC beat/miss |
| Q2 2026 | MI355X volume ramp progress at Meta/OpenAI | + on hyperscaler-confirmed deployment |
| July–Aug 2026 | Q2 2026 earnings + updated AI revenue forecast | Magnitude of AI revenue scaling |
| Q3 2026 | Helios/MI455X launch + OpenAI 1GW deployment start | + on execution; - on hardware delay |
| Q3 2026 | Zen 6 Venice EPYC launch on TSMC N2 | + on performance leadership vs. Intel Clearwater Forest |
| Fall 2026 | MLPerf Training v5.0 results | Proof point for ROCm training parity (positive catalyst if competitive, negative if absent/weak) |
| Q4 2026 | Potential 3rd hyperscaler megadeal (Google, AWS, Azure) | + on market validation of second-source thesis |
| Early 2027 | Intel 18A Clearwater Forest server launch | - risk to EPYC share gain trajectory |
| 2027 | MI500 architectural disclosure | Critical — determines competitive position vs. Nvidia Feynman |
| Ongoing | TSMC CoWoS capacity allocation commentary (earnings calls) | Leading indicator for AI revenue ceiling |
| Tail | Taiwan disruption (any form) | -30–50% to AI revenue trajectory |

## Risks

**Thesis risks (investment case is wrong)**:

1. **Nvidia cuts AI GPU pricing and erases the second-source premium**. Nvidia's gross margin has room from 75% to 60% before compression hurts; cutting prices 20–30% closes the price gap that justifies AMD's second-source premium. Consensus assumes Nvidia defends margin; contrarian case is Nvidia defends share.
2. **ROCm never crosses training parity**. Inference parity is achievable at framework-level integration; training parity requires distributed systems work where CUDA has decade-plus lead. If training stays CUDA-locked, AMD's share caps at inference only.
3. **ASIC substitution for inference outpaces merchant GPU**. 60–80% of 2028 AI compute is inference; if 40% of inference is ASIC-served, merchant GPU TAM compresses faster than AMD gains share.
4. **OpenAI/Meta commitments convert to lower realized take**. 6GW nominal → 2–3GW actual if performance or cost terms renegotiate. Warrant dilution does not adjust.
5. **CoWoS allocation ceiling**. AMD's 11% 2026 allocation caps AI revenue regardless of demand. If TSMC doesn't add capacity faster than Nvidia reserves it, AMD's share is bounded.

**Position risks (thesis is right but stock goes down anyway)**:

6. **Semi-cycle macro downturn**. All semiconductor stocks derate in recession; AMD's 38x P/E and beta to AI narrative amplify drawdowns.
7. **Hyperscaler capex reset**. If one or more hyperscalers publicly cut AI capex (2022 Meta precedent), all AI-exposed stocks sell off; AMD would trade down even if its share gain story is intact.
8. **Taiwan geopolitical shock**. MI400 series is 100% TSMC Taiwan. Any blockade/invasion signal hits AMD as hard as NVDA.
9. **Warrant vesting mechanics create volatility at each tranche**. Share count increments + announcement dilution cause headline overhangs at each milestone.
10. **Intel turnaround narrative disrupts AMD-share-gain story**. If Intel 18A delivers and US policy favors Intel foundry (CHIPS Act 2.0), AMD's relative-momentum trade unwinds.

## Conviction Triggers

→ **HIGH if**: MLPerf Training v5.0 shows MI455X within 10% of Rubin GR200 on Llama 5-class training workloads, **AND** Meta publicly confirms Llama 5 production-trained on ROCm, **AND** a 3rd hyperscaler (Google, AWS) signs a commitment ≥2GW by end Q3 2026. (Any 2 of 3 qualifies as conviction strengthened; all 3 triggers HIGH.)

→ **LOW if**: MI450/Helios ships with a benchmark gap >25% to Rubin GR200 on published MLPerf results, **OR** OpenAI/Meta renegotiate commitments downward by >30% on realized take-or-pay, **OR** CoWoS 2027 allocation disclosed at <12% (no structural improvement from 2026 bottleneck).

→ **CLOSE if**: AI revenue in FY2027 prints below $20B (vs. "tens of billions" guidance implying $25–40B+), **OR** ROCm is publicly de-prioritized by any top-3 hyperscaler in favor of CUDA-only or ASIC-only workloads, **OR** Intel 18A Clearwater Forest reclaims server CPU share trajectory (AMD EPYC share falls below 35% in any quarter through 2027).

## Related Research

- [[Sectors/GPU & AI Compute Accelerators]] — sector MOC; AI accelerator competitive dynamics
- [[Theses/NVDA - Nvidia]] — primary GPU competitor; AMD 5–8% vs. NVDA 75% share; vertical software stack comparison
- [[Theses/AVGO - Broadcom]] — custom ASIC competitor; Pensando vs. Broadcom networking/switching competitive context
- [[Theses/TSM - Taiwan Semiconductor]] — fab dependency; CoWoS allocation + Taiwan geopolitical tail
- [[Theses/SNDK - SanDisk]] — HBF memory tier; AMD is preferred GB200/MI350 memory-density customer
- [[Theses/285A - Kioxia]] — NAND/memory supply chain
- [[Theses/IQE - IQE]] — III-V epitaxy for photonics; relevant to CPO transition where TSMC COUPE entered risk production with AMD Feb 2026
- [[Theses/LITE - Lumentum]] — photonics/CPO supply; AMD CPO adoption via TSMC COUPE
- [[AI Bubble Risk and Semiconductor Valuations]] — AI capex cycle framework; AMD valuation in bubble scenarios
- [[Research/2026-01-15 - AI Compute and Memory Demands - HBM Shortage]] — HBM supply context, MI350 288GB positioning
- [[Research/2026-04-19 - TSM - Stress Test]] — Taiwan geopolitical tail exposure for MI400 series
- [[Research/2026-03-18 - CPO Market Entry for Pluggable Optics]] — TSMC COUPE AMD risk production Feb 2026
- [[Research/2025-11-27 - Broadcom Data Center Opportunity]] — DPU competitive context (Pensando vs. Nvidia BlueField vs. AWS Nitro)
- [[Research/2026-03-14 - CXL Technology Adoption]] — CXL relevance to EPYC server memory architecture

## Log

### 2026-04-21
- Initial thesis created. Conviction: medium — AMD is the sole merchant full-stack Nvidia alternative (CPU+GPU+DPU+FPGA) benefiting from hyperscaler-imposed diversification (OpenAI 6GW + Meta 6GW = 12GW signed in 5 months), but valuation at 38–41x forward P/E embeds flawless execution across MI400/MI450 hardware parity, ROCm training-parity, EPYC 50% share capture, and CoWoS allocation expansion — each plausible, the combination demanding.
- Status change: draft → active — promoted to active portfolio consideration after initial thesis review. Thesis snapshot skipped (no analytical content change); sector snapshot: [[_Archive/Snapshots/Semiconductors (pre-status 2026-04-21-112827)]]

### 2026-04-22
- Sector re-scoped: Semiconductors → GPU & AI Compute Accelerators (vault-wide subsector taxonomy reorganization).
- Wikilink cleanup: replaced stale [[Sectors/Semiconductors]] with [[Sectors/GPU & AI Compute Accelerators]] in Related Research (aligned with frontmatter sector field and new sector-note sector fill). Conviction unchanged; pure wikilink hygiene.
