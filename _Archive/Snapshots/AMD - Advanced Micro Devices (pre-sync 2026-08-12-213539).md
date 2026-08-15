---
publish: false
date: 2026-04-21
tags: [thesis, semiconductors, AMD]
status: active
conviction: medium
sector: Compute & AI Compute Accelerators
ticker: AMD
source: AMD Q4 2025 earnings (Feb 2026), MLPerf Inference v6.0 (Apr 1 2026), OpenAI 6GW deal (Oct 2025), Meta 6GW deal (Feb/Mar 2026)
key_metrics_last_refreshed: 2026-07-12
snapshot_of: "[[Theses/AMD - Advanced Micro Devices]]"
snapshot_date: 2026-08-12
snapshot_trigger: sync
snapshot_batch: sync-2026-08-12-213539

---

# AMD - Advanced Micro Devices

## Summary

AMD is the sole merchant full-stack alternative to Nvidia at a moment when every hyperscaler has concluded it cannot afford single-source GPU dependence. The OpenAI 6GW deal and Meta 6GW deal signed inside 5 months were not won on hardware merit — they were engineered by customers who needed a duopoly to restore pricing leverage against Nvidia. AMD traded 10% of its equity (OpenAI warrant at $0.01 over 160M shares) to lock itself in as the structural second source, converting a GPU supply contract into a decade-long capital alignment. At ~$910B market cap and ~75x forward P/E the stock has already re-rated past flawless-execution pricing into its own 2028 bull-case zone two years early, continued EPYC share capture (41% Q2 2025 tracking toward parity with Intel), and ROCm reaching effective CUDA parity by H2 2026 — each individually plausible, the combination tight. The non-consensus case is that the hyperscaler-initiated diversification mandate is structurally mispriced as a cyclical market-share trade when it is actually a durable rewiring of AI infrastructure procurement. The bear case is that the OpenAI warrant is dilution, the MI400 is one generation behind Rubin, the ROCm asymptote is farther than disclosed, and the valuation embeds a second-source premium that vanishes the moment Nvidia cuts prices.

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

**7. Is EPYC share gain durable against Intel 18A Clearwater Forest, or does Intel's process lead reclaim share in 2027?** Intel 18A (scheduled 2026 production) and Clearwater Forest E-core server (2027) represent the first credible Intel counterpunch since Zen 3. If Intel 18A delivers on performance/watt claims, AMD's 41% → 50% server share trajectory stalls or reverses. Venice (2nm TSMC) vs. Clearwater Forest (18A) is the next-18-month battle that determines whether EPYC is a structural share gainer or a cyclical one. **Partial update (2026-04-24)**: the agentic-AI workload shift reframes the question. Intel Diamond Rapids removed SMT (192c = 192t), collapsing thread density 2.7x vs AMD Venice Dense (256c = 512t) on exactly the workload that's inflecting (sub-agent orchestration + tool-call parallelism). Intel stranded on Granite Rapids until Coral Rapids (no disclosed date; 2027+ at earliest) per Vik Sekar April 2026 scoring. Intel management was "caught off guard" on CPU demand in Q4 2025 earnings, suggesting Clearwater Forest was not architected for agentic workloads either. The "2027 share trajectory stalls" scenario now requires Intel to restore SMT AND redesign for agentic memory hierarchy — pushing the credible competitive response from 2027 to 2028+. Does not fully resolve the question but shifts the clock in AMD's favor.

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
| Market Cap | ~$910B | Implied ~$560/share ($910B ÷ ~1.63B diluted shares); the $278.39 (Apr 17, 2026) basis is stale — next /numbers price pull will confirm |
| EV/Revenue | ~13x | TTM revenue ~$32B (Q4 2025 run-rate annualized); forward ~$40B+ implies EV/Rev dropping toward 11x |
| Revenue Growth | +34% YoY Q4 2025; +32% YoY Q1 2026 guided | Data Center +40%+ YoY; guided >60% CAGR 3–5 years |
| Gross Margin | ~50% non-GAAP Q4 2025 | 45–55% client/embedded, 55–60% data center, 15–25% gaming drag |
| FCF Yield | ~0.9% | Elevated capex for TSMC/HBM prepayments; OpenAI warrant dilution adds shadow cost |
| Forward P/E | 75x | Sector median ~31x; 23% premium reflects AI growth but embeds execution |
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
3. **EPYC passes 50% server CPU share by end 2026, with Venice Dense specifically taking the agentic-AI action-workload category.** Venice 2nm launch outperforms Intel Clearwater Forest / 18A; AMD becomes the incumbent rather than the challenger. The agentic-AI wave expands the server CPU TAM orthogonally — Vik Sekar's 9-metric reasoning/action scoring framework (April 2026) scored Venice Dense 5/5 on action workloads (256 Zen6c cores, 512 SMT threads, 1GB L3, x86 breadth for tool-call compatibility) vs Intel Diamond Rapids 3/3 (192 cores, 192 threads after Intel's unprecedented SMT removal — a 2.7x thread-density disadvantage vs Venice Dense and a regression from Granite Rapids' 128c/256t). Intel's Diamond Rapids-SP cancellation strands Intel on Granite Rapids through 2028 until Coral Rapids restores SMT. Server CPU revenue doubles by 2028 at mid-cycle; the agentic-AI-driven CPU demand inflection (Dylan Patel's April 2026 observation that CPUs are "completely sold out" driven by RL environments + AI-generated code deployment) provides an additional volume tailwind not in prior thesis models.
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

6. **Semi-cycle macro downturn**. All semiconductor stocks derate in recession; AMD's ~75x P/E and beta to AI narrative amplify drawdowns — the multiple has already consumed the bull case, leaving no cushion for an MI450-vs-Rubin miss.
7. **Hyperscaler capex reset**. If one or more hyperscalers publicly cut AI capex (2022 Meta precedent), all AI-exposed stocks sell off; AMD would trade down even if its share gain story is intact.
8. **Taiwan geopolitical shock**. MI400 series is 100% TSMC Taiwan. Any blockade/invasion signal hits AMD as hard as NVDA.
9. **Warrant vesting mechanics create volatility at each tranche**. Share count increments + announcement dilution cause headline overhangs at each milestone.
10. **Intel turnaround narrative disrupts AMD-share-gain story**. If Intel 18A delivers and US policy favors Intel foundry (CHIPS Act 2.0), AMD's relative-momentum trade unwinds.

## Conviction Triggers

→ **HIGH if**: MLPerf Training v5.0 shows MI455X within 10% of Rubin GR200 on Llama 5-class training workloads, **AND** Meta publicly confirms Llama 5 production-trained on ROCm, **AND** a 3rd hyperscaler (Google, AWS) signs a commitment ≥2GW by end Q3 2026. (Any 2 of 3 qualifies as conviction strengthened; all 3 triggers HIGH.)

→ **LOW if**: MI450/Helios ships with a benchmark gap >25% to Rubin GR200 on published MLPerf results, **OR** OpenAI/Meta renegotiate commitments downward by >30% on realized take-or-pay, **OR** CoWoS 2027 allocation disclosed at <12% (no structural improvement from 2026 bottleneck).

→ **CLOSE if**: AI revenue in FY2027 prints below $20B (vs. "tens of billions" guidance implying $25–40B+), **OR** ROCm is publicly de-prioritized by any top-3 hyperscaler in favor of CUDA-only or ASIC-only workloads, **OR** Intel 18A Clearwater Forest reclaims server CPU share trajectory (AMD EPYC share falls below 35% in any quarter through 2027).

## Mental Models
<!-- Outputs from applying the /Mental Models context files to this opportunity. Per the READING PROTOCOL in [[Generalist - Overview]], these are lenses and questions, never conclusions — every entry is a hypothesis to test against the evidence in this thesis, not a verdict. Populated incrementally: each research pass appends the models it applied and the specific triggers that fired. -->
- **Models applied** (2026-07-09 batch-3 pass, evidence-tested against July-2026 web research): [[Generalist - Overview]] (expectations, base rates) · [[Industry - Semiconductors]] (#13, #14) · [[Lens - Value Layer Monopoly]] (§4)
- **Triggers + evidence status** — hypotheses tested, not verdicts:
	- *#14 second-source reclassification* — CONFIRMED running ahead of thesis: Q1 $10.3B (+38%, beat), DC $5.8B (+57%), record **46.2% server-revenue share** (Mercury Q1), AMD passed Intel in total DC revenue for the first time; Meta added 6GW custom-MI450 (Feb 24) days after expanding its Nvidia commitment — the dual-track procurement mechanic of Insight #1, live. No renegotiation, no ROCm defection, EPYC-share LOW trigger strongly refuted.
	- *Expectations inversion — the multiple consumed the bull case*: re-rated 38–41x → ~59–80x fwd; the stock ($584 peak) entered the thesis's own 2028 bull target zone two years early, and the re-rate was **disproportionately the CPU/agentic story** (Su's ">$120B server-CPU TAM by 2030"; Wells Fargo/Cantor/UBS all citing CPU, not GPU). The unproven leg — MI450 vs Rubin — is therefore the marginal variable at maximum embedded expectations. HIGH trigger: **0 of 3 met**, all resolve H2 2026 (MLPerf Training vs Rubin; Llama-on-ROCm confirmation; 3rd hyperscaler ≥2GW by end-Q3 — Oracle's 50K-MI450 deal is ~10x too small). Proxy evidence mildly positive: MLPerf v6.0 MI355X within 5–6% of B200 single-node, but B300 21–26% faster and AMD skipped the MoE benchmarks.
	- *Dilution correction*: combined OpenAI+Meta warrants = up to **320M shares / ~16.7% max dilution** — 2x the thesis's single-warrant model; first price-milestone tranches near-money at the $584 touch. Rebuild the per-share math before acting on any trigger.
	- *Memoryflation crossover* — upgraded from "modest cost headwind" to guided P&L hit: ~20% H2 gaming revenue decline + Q2 consumer decline on memory costs. Cuts against Insight #5's clean "HBM scarcity favors AMD" — DRAM inflation taxes the ~35% client/gaming book while helping DC.
	- *ASIC denominator compression* — pressure rising on the merchant-GPU TAM: custom ASIC +45% 2026, Google 4-partner inference chain, DeepSeek in-house chip (Jul 8); the thesis's "ROCm work is free to ASIC vendors" asymmetry remains unhedged. Arm crossed ~50% of hyperscaler CPU share — an erosion asterisk under the $120B x86 TAM narrative consensus is ignoring.
- **Disconfirming check** (evidence-updated): fundamentals ran ahead of thesis while price ran ahead of fundamentals — at ~59–80x with 0/3 HIGH legs confirmed, the position is pre-paying for benchmark results that don't exist yet. Base rate: challengers reaching training parity with the incumbent's next generation on the first "no asterisk" attempt are rare; Forrest Norrod's claim is a claim. Single falsifiers, dated: **Advancing AI keynote Jul 22–23** (Helios positioning, possible 3rd-customer news), Q2 print Aug 4, fall MLPerf. -12% in the July rout (macro, not AMD-specific). Batch flag: NVDA and AMD are now opposite expectation trades on the same H2-2026 benchmark event — NVDA at ~21x priced for share loss, AMD at ~70x priced for share gain; the MLPerf print arbitrates both.

## Related Research

- [[Compute & AI Compute Accelerators]] — sector MOC; AI accelerator competitive dynamics
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
- [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]] — Venice Dense 5/5 action score, 2.7x thread-density advantage over Intel Diamond Rapids post-SMT-removal; reframes Outstanding Question #7
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]] — CPUs "completely sold out" via RL environments + AI-generated code deployment; volume tailwind beyond thesis model
- [[Research/2026-04-24 - Iran War Japan Semiconductor Photo Materials Shortage - news]] — indirect HBM4 supply chain exposure for MI450 via Japanese PR/BARC disruption
- [[Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive]] — Vera Rubin HBM4 ~70/30/0 SK Hynix/Samsung/Micron initial split implies MI400/MI450 HBM4 sourcing competes for the SK Hynix-dominated supply pool — supplier diversification path forces AMD toward Samsung (less qualified) or wait for Micron HBM4 12-Hi redesign (late entrant); HBM supply risk for MI450 ramp materially compounded by SK Hynix's primary allocation to Rubin
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]] — Tier 4 cyclical challenger; TRIM Medium→3-4% (sole merchant full-stack alt + aligned-up retro signal, but ROIC 8% on 62x P/E; OpenAI/Meta anchor-binary)
- [[Research/2026-05-31 - CPO Scale-Up Inflection and Supply Chain - deep-dive]] — SemiAnalysis CPO deep-dive: NVLink SerDes plateau opens a scale-up-fabric opportunity for AMD; TSMC COUPE hybrid bonding "proven on AMD parts" — scale-up-fabric optionality vs Nvidia
- [[Research/2026-05-31 - DRAM HBM Memory Supercycle - deep-dive]] — memory supercycle: MI350 288GB→MI400 432GB HBM content step-up supports accelerator demand; memoryflation a modest cost headwind
- [[Research/2026-06-02 - Datacenter CPU Landscape 2026 - deep-dive]] — Venice 256c N2 (1.7x perf/watt vs Turin) widens per-core lead; new SP8 8-channel platform attacks Intel enterprise base as Intel cancels its own 8-channel SKU — EPYC share-gain catalyst into a "strong double digit" CPU-TAM-growth year
- [[Research/2026-06-05 - AI Silicon Shortage - N3 and Memory Constraint - deep-dive]] — SemiAnalysis silicon shortage: MI350X (N3) + MI400 AID/MID tiles (N3) compete inside the binding N3 pool and the SK-Hynix→Nvidia-priority HBM allocation; MI350→MI400 +50% HBM into 3x→4x wafer/bit crowd-out — sharpens the MI450 HBM/N3 supply-gating risk

## Log

### 2026-04-21
- Initial thesis created. Conviction: medium — AMD is the sole merchant full-stack Nvidia alternative (CPU+GPU+DPU+FPGA) benefiting from hyperscaler-imposed diversification (OpenAI 6GW + Meta 6GW = 12GW signed in 5 months), but valuation at 38–41x forward P/E embeds flawless execution across MI400/MI450 hardware parity, ROCm training-parity, EPYC 50% share capture, and CoWoS allocation expansion — each plausible, the combination demanding.
- Status change: draft → active — promoted to active portfolio consideration after initial thesis review. Thesis snapshot skipped (no analytical content change); sector snapshot: [[_Archive/Snapshots/Semiconductors (pre-status 2026-04-21-112827)]]

### 2026-04-22
- Sector re-scoped: Semiconductors → GPU & AI Compute Accelerators (vault-wide subsector taxonomy reorganization).
- Wikilink cleanup: replaced stale [[Sectors/Semiconductors]] with [[Compute & AI Compute Accelerators]] in Related Research (aligned with frontmatter sector field and new sector-note sector fill). Conviction unchanged; pure wikilink hygiene.

### 2026-05-11 (/sync)
- [[Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive]]: Vera Rubin HBM4 ~70% SK Hynix / ~30% Samsung / 0% Micron initial split is adverse for MI400/MI450 — SK Hynix HBM4 supply primarily allocated to Nvidia Rubin in first-shipment quarters, forcing AMD toward Samsung (less qualified at 1c yield ~50%) or wait-and-watch on Micron HBM4 12-Hi redesign (late entrant). HBM4 supplier diversification path is structurally harder than thesis modeled. Conviction directionally weakened on MI450 ramp velocity (HBM supply gating); unchanged on full-stack hyperscaler-diversification thesis.

### 2026-04-24 (/sync)
- [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]]: Rewrote Bull Case #3 to integrate Venice Dense 2.7x thread-density vs Intel Diamond Rapids (SMT removed); updated Outstanding Question #7 with partial-resolution framing (Intel's credible agentic-AI response pushed to 2028+ on SMT+Coral Rapids). Conviction strengthened — Bull #3 durability improved on structural, not cyclical, CPU positioning. Snapshot: [[_Archive/Snapshots/AMD - Advanced Micro Devices (pre-sync 2026-04-24-101646)]]
- [[Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript]]: "CPUs completely sold out" via RL environments + AI-generated code deployment — direct validation of Venice Dense demand trajectory and EPYC capture rate. Conviction unchanged (already captured in Bull #3 rewrite).
- [[Research/2026-04-24 - Iran War Japan Semiconductor Photo Materials Shortage - news]]: Indirect MI450 HBM4 supply-chain exposure via Japanese PR/BARC; adds to Risks #8 Taiwan tail as a non-kinetic material-input tail. Conviction unchanged.

### 2026-05-01 (/sync)
- [[Research/2026-04-24 - Luo Fuli on OpenClaw and Agent-Era Compute Reallocation - video-transcript]]: 3:1:1 research:pre-train:post-train framework + 1T-model entry ticket structurally expand the total compute fleet — second-source AMD addressable share grows even at constant share-of-fleet. Conviction unchanged — strengthens demand-floor pillar.
- [[Research/2026-04-24 - Thomas Kurian on TPU Capacity Anthropic Hosting and Agentic Chip Design - video-transcript]]: Cross-hyperscaler capacity tightness (Google Cloud "more demand than we can possibly meet" from frontier AI labs) signals industry-wide GPU under-supply spilling beyond NVDA — second-source MI400/MI500 ramp benefits. Conviction unchanged.

### 2026-05-12 (/sync)
- [[Research/2026-05-11 - INTC - Institutional Equity Research - deep-dive]]: Intel **Diamond Rapids slipped 2026 → mid-2027** (Jaykihn Apr 2026) + Coral Rapids SMT restoration mid-2028 = no competitive Intel P-core response for ~20 quarters; AMD already at **41.3% Q4 2025 server revenue / 28.8% units (Mercury — first quarter ever >40%)** with 12.5-pt quality-of-share gap pointing to ASP-richer enterprise/sovereign deals. 50% server share by mid-2026 now Intel's own Bear Case baseline. Conviction strengthened on Venice/Zen 6 share-capture window — Intel's structural absence at the P-core agentic-AI inflection now spans 2026–mid-2028.
- [[Research/2026-05-11 - INTC - Institutional Equity Research - deep-dive]]: Intel EMIB cost-arb ($900–1,000 CoWoS Rubin-class vs "low hundreds" EMIB) is the first quantified external-packaging cost-pressure datapoint on AMD's MI400/MI450 CoWoS dependency; combined with TSMC CoWoS 35K→130K WPM at +20% pricing and NVDA pre-booking 60–65%, AMD risks marginal-AI-customer packaging-cost squeeze even before any EMIB customer migration. Watch for AMD packaging diversification commentary in next 2 quarters. Conviction unchanged on Bull Case core; weakens MI400/MI450 unit-economics tail.

### 2026-05-19 (/sync)
- Cross-thesis propagation from [[Macro & Technology/800VDC Adoption]]: Macro note covers 800VDC rack-architecture transition (NVIDIA Kyber row-rectified ±400V/800V March 2026 + OCP Mt. Diablo sidecar Meta/Google co-authored) with new quant-screening framework (AI-DC Rev/OP %, ROIC/EV-EBIT) across ~50 value-chain beneficiaries. AMD listed under §Adjacent exposure in the macro: Helios MI455X H2 2026 *explicitly sidesteps* 800VDC by going double-wide OCP form factor (a hyperscaler-imposed Mt. Diablo accommodation, not Kyber-style integration); MI500 (2027) must compete at Kyber-equivalent density per processor if NVIDIA Rubin Ultra (600 kW/rack) sets the standard. The architectural-density question rises in importance through 2027-2028 — if AMD cannot match Rubin Ultra power-delivery scale, Helios stays sub-Kyber and the rack-level integration gap widens at hyperscalers running both architectures in parallel. Conviction unchanged at medium — adds a 2027-2028 power-density execution risk that consensus underweights vs the chip-level MI455X/MI500 benchmark narrative.

### 2026-05-22 (manual)
- Status change: portfolio-wide alignment — confirmed as current Live Portfolio holding; conviction medium→high.

### 2026-05-24
- Retro insight: 1w retrospective — AMD is the cleanest aligned-up confirmation of the 5-22 medium→high realignment ($417→$462, +10% week) driven by Meta $60B AI infra deal + OpenAI 6GW commitment + MI400/Helios merchant-GPU validation; gap magnitude rated **high** with vault and price both pointing same direction. Next tests: AVGO Jun 3 (custom-silicon TAM commentary as read-across), Computex 2026 (early-June Vera competitive framing), AMD Aug 4 Q-print (MI400 binary). [[Research/2026-05-24 - Retrospective 1w - Synthesis]]

### 2026-05-26
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]]: Rebalancing flags TRIM to 3-4% (structural second-source thesis real + aligned-up signal, but ROIC 8% on 62x P/E uncomfortable) — sizing call; conviction unchanged (high).

### 2026-05-31 (/sync)
- [[Research/2026-05-31 - CPO Scale-Up Inflection and Supply Chain - deep-dive]]: NVLink SerDes plateau (copper 2m reach wall) opens a scale-up-fabric opening for AMD; COUPE hybrid bonding "proven on AMD parts". Early optionality, not yet a thesis driver — no body edit. Conviction unchanged (high).

### 2026-06-01 (/sync)
- [[Research/2026-05-31 - DRAM HBM Memory Supercycle - deep-dive]]: MI350 288GB→MI400 432GB HBM content step-up supports accelerator demand; memoryflation a modest cost headwind (passed through) — conviction unchanged (high).

### 2026-06-02 (/sync)
- [[Research/2026-06-02 - Datacenter CPU Landscape 2026 - deep-dive]]: Venice (256c N2, 1.7x perf/watt vs Turin) widens the per-core lead while Intel cancels its 8-channel Diamond Rapids-SP — AMD's new 8-channel Venice SP8 attacks Intel's enterprise stronghold exactly as Intel exits it; "strong double digit" 2026 server-CPU TAM growth. Reinforces existing Bull #3 (Venice Dense agentic-action lead); conviction unchanged (high).

### 2026-06-06 (/sync)
- [[Research/2026-06-05 - AI Silicon Shortage - N3 and Memory Constraint - deep-dive]]: MI350X (N3) + MI400 AID/MID tiles (N3, XCD on N2) compete inside the binding N3 pool (AI 60%→86% of N3 output 2026→2027) and the SK-Hynix→Nvidia-priority HBM allocation; +50% HBM MI350→MI400 lands into the 3x→4x wafer/bit crowd-out. Reinforces the existing MI450 HBM/N3 supply-gating risk (06-01 log) — second-source-via-Samsung path stays structurally harder. Conviction unchanged (high).

### 2026-07-09
- Sector re-scoped: frontmatter `sector:` aligned to [[Sectors/Compute & AI Compute Accelerators]] (prior value resolved to no sector note, so sector propagation was silently skipped) — conviction unchanged; metadata hygiene per [[_Archive/Docs/2026-07-09 - Skills Audit Report]].
- Mental models pass: batch-3 evidence sweep populated ## Mental Models — fundamentals ran ahead (46.2% server share, DC crossover vs Intel, Meta 6GW) but multiple consumed the 2028 bull target 2yrs early (38-41x → 59-80x) on the CPU story while the GPU proof (MI450 vs Rubin) stays unproven; HIGH 0/3, all resolve H2-26; warrants = 16.7% max dilution (2x thesis model) — conviction unchanged; Advancing AI Jul 22-23, Q2 Aug 4.

### 2026-07-11
- Status change: conviction high → medium — vault-wide multi-agent valuation scoreboard: stock sits inside the thesis's own 2028 bull target two years early at 59-80x fwd with 0/3 HIGH triggers met; the unproven MI450-vs-Rubin leg is the marginal variable at maximum embedded expectations. Snapshot: [[_Archive/Snapshots/AMD - Advanced Micro Devices (pre-status 2026-07-11-063211)]]

### 2026-07-12
- Numbers refresh: 4 metrics updated, 3 material. Forward P/E 38-41x→75x (multiple nearly doubled — confirms Mental Models' "multiple consumed the bull case" read). Revenue Growth left unedited (unchanged after rounding). Snapshot: [[_Archive/Snapshots/AMD - Advanced Micro Devices (pre-numbers 20260712-174116)]]

### 2026-07-12 (/numbers)
- Numbers refresh (2nd same-day pass): 0 metrics changed — all 5 mapped rows (Market Cap, Revenue Growth, Gross Margin, FCF Yield, Forward P/E) render identical to prior refresh after rounding; data confirmed stable intraday. Snapshot: [[_Archive/Snapshots/AMD - Advanced Micro Devices (pre-numbers 20260712-184120)]]

### 2026-07-12 (/deepen --sync-metrics)
- Metrics synced: market cap / fwd P/E $453B/38-41x → $910B/75x across Summary, Risks #6, Key Metrics Notes — stock has re-rated into its own 2028 bull-case zone two years early. Snapshot: [[_Archive/Snapshots/AMD - Advanced Micro Devices (pre-deepen-metrics-sync 2026-07-12-203456)]]

### 2026-07-24 (/sync)
- [[Research/2026-07-24 - TSM Q2 2026 Results - earnings]]: AI demand "multi-year" (2029-30), N2 sold out (Venice is N2), CoWoS/SoIC still allocation-constrained; A14 pre-prod 2027/HVM 2028 keeps the MI400/COUPE runway intact (A16 unmentioned on the call) — conviction unchanged (medium); MI400 volume hinges on packaging allocation as much as demand.
