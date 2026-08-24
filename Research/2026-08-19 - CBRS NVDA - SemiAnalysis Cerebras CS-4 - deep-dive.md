---
date: 2026-08-19
tags: [research, semiconductors, CBRS, NVDA, AVGO, TSM, AMD, ai-inference, wafer-scale]
sector: Compute & AI Compute Accelerators
ticker: CBRS
source: 'https://newsletter.semianalysis.com/p/cerebrass-next-generation-cs-4-fast'
source_type: deep-dive
propagated_to: [CBRS, NVDA]
gmail_id: 1a017a9129d52f60
---

# Cerebras's Next Generation CS-4: Fast Just Got Faster — SemiAnalysis

## Thesis Delta

Consensus still prices [[Theses/CBRS - Cerebras Systems]] Outstanding Question 4 as a **WSE-4 / 3D-stacked SRAM on TSMC N3** capital-efficiency print (late-2026 / 2027) that restores single-device model fit, and treats the 9 August IA mashup as an unvalidated "gen 3.5 power-and-clocks" rumor. This 19 August 2026 SemiAnalysis CS-4 note implies a different map. CS-4 is a **fourth-generation rack around the same third-generation 5nm WSE-3**. Clock 2× via more power and cooling; 44GB SRAM/wafer unchanged; off-wafer I/O 1.2→2.4 Tb/s; switched latency 5→3µs and 2µs on configurable direct wafer-to-wafer links; three backpacks per rack versus two; 125–135kW rack TDP versus CS-3 23kW/wafer; 43 PB/s on-chip SRAM bandwidth; ~4,000 versus ~2,000 tok/s/user at similar BOM-per-wafer TCO. Consensus "new silicon / Nvidia-killer" is the wrong frame. The source implies **a manufacturability and decode-bandwidth refresh that can double token revenue at similar hardware spend while leaving the SRAM-capacity liability intact**, to be papered over by heterogeneous disaggregation (AWS Trainium over EFA, AMD, HBM-based XPUs) — the same topology Nvidia is using for Groq LPUs. That is a **layer-renter** confirmation (AWS owns EFA and routing), not a qualification-gate or capital-efficiency print. [[Theses/NVDA - Nvidia]] Groq Outstanding Question is analogized, not answered: SRAM-first decode is the niche both firms occupy; CS-4 does not put GPU decode within ~3× of CS-3 on the numbers SA publishes. [[Theses/AVGO - Broadcom]] is adjacent only through Ethernet/disagg (the named switch is Arista, not Broadcom). Conviction-trigger touches are flag-only below; **conviction and status are untouched** (CBRS low / draft; NVDA high / active; AVGO high / active).

## Summary

SemiAnalysis's argument is that Cerebras extracted a generation of customer-facing interactivity without a new wafer. CS-4 reuses WSE-3 at 5nm, doubles clock by feeding the wafer more power, and redesigns the rack as modular vertical "backpacks" (power in front, compute in rear; pumps and heat exchangers removed because target data centers are already fully liquid-cooled). Three WSE-3 engines per rack replace CS-3's two. Because SRAM bandwidth scales with clock, the metric customers buy — tokens/s/user — should nearly double, and SA thinks effective BOM per wafer lands similar to CS-3 after simpler assembly offsets the extra power and cooling. Time-to-deploy improves because customers can stand up the power half and socket wafer backpacks on site. More details are promised at Hot Chips.

The unfixed constraint is capacity, not bandwidth. 44GB SRAM per wafer is set by bit-cell count; next-generation silicon is required to move it. A WSE still cannot hold a frontier model's weights on one wafer, so Cerebras keeps **pipeline-parallel inference** as the default: every MoE expert for a given model sits interleaved on a single wafer. Tensor and expert parallelism that shard an expert across wafers are judged not viable. Off-wafer I/O doubles to 2.4 Tb/s via a field-upgradeable FPGA NIC that converts proprietary wafer I/O to standard Ethernet (two modules, north and south). Switched two-layer fat-tree latency (Arista) falls from 5µs to 3µs; direct wafer-to-wafer links, with the FPGA doing configurable routing, reach 2µs. SA calls this a real but modest gain versus competitors quoting nanosecond all-in switch latencies. The 3µs hop plus bandwidth limits still block EP/ETP: token dispatch and combine from router to expert is latency-sensitive, and expert imbalance plus an extra network hop leaves pipeline parallelism as the only working solution.

Long-context KV cache, not parameter count, is the scaling tax SA wants readers to underwrite. Weight memory for one forward pass scales with parameters; KV capacity scales with concurrent users × context window. GPT 5.6 Sol's experts still fit on one 44GB wafer, but SA expects OpenAI to run 5.6 Sol at 256k context rather than the full 1M to keep KV off a ruinous on-wafer footprint. For 1.6T-parameter DeepSeek V4 Pro at 1M context, SA's public tokenomics math is ~20 WSE minimum and ~40 systems at 256 concurrency — over $20M capex and 1MW before a forward pass. CS-4's marketing number is 43 PB/s on-chip bandwidth, framed as ~2,000× Nvidia Rubin; Cerebras brands "up to 30×" GPU interactivity as an "ultrafast" tier. SA's own stack: CS-4 near 4,000 tok/s/user on frontier models, CS-3 at 2,000, Blackwell theoretically 200 tok/s/user (nobody runs there) and a more realistic 100 at reasonable concurrency — 20–40×, so "up to 40×" would have been fair. Nvidia TileRT is named as the GPU-side counter that brings high-throughput / low-interactivity configs into the comparison; the wafer's operating region remains only high-interactivity / low-throughput.

The product bet is open heterogeneous disaggregation from day one. Cerebras is the decode chip (rooflines are wrong for compute-bound prefill) and claims both traditional prefill-decode disaggregation (PDD) and attention-feedforward disaggregation (AFD). Named partners: AMD and AWS Trainium, "with more coming." The I/O module is described as designed especially so AWS can put EFA NICs on CS-4 next to Trainium servers. Pairing CS-4 with HBM-based XPUs to cover capacity is "the same way that Nvidia is positioning the Groq LPUs." SA's warning: every heterogeneous disagg cluster freezes the prefill:decode resource ratio on the day the hardware PO is signed, while a GPU or TPU fleet can be re-sliced as workloads move. Reasoning models pushed decode cost up; agentic cache hits then pushed prefill cost down with decode unchanged. One P:D ratio is unlikely to stay optimal across a 5+ year system life.

Roadmap: the next wafer-scale engine is already co-designed with a rack-scale platform called Nexus, so the CS-4 chassis should carry forward without a major mechanical redesign (CS-5). Stated cadence is roughly 2× performance per year with a 20× throughput target by 2027. Reliability work continues on field tray swaps, error recovery, tray-level redundancy, and on-chip yield harvesting across cores and channels. SA's verdict is impressed on performance, manufacturability, and deployability; capacity is unfixed directly and only indirectly addressed by disagg; 2× bandwidth can be 2× token revenue and ~2× perf/TCO; the firm is still an expensive solution that needs customers to pay up for fast tokens and, later, higher concurrency to bring those tokens to the mass market.

## Framework / Mental Model

**Name:** Same-silicon clock doubling, pipeline-only MoE, and fixed-ratio heterogeneous disaggregation.

**Clock-doubling identity (what "CS-4" is).** Treat a Cerebras generation label as a *rack and power* event until a new wafer is named. CS-4 = WSE-3 5nm reuse + 2× clock from power/cooling + backpack mechanics. SRAM *bandwidth* and peak FLOPs and off-wafer I/O scale with clock; SRAM *capacity* does not. Marketing "2,000× Rubin bandwidth" is the clock-scaled on-wafer SRAM number (43 PB/s); customer-facing interactivity is the much smaller tok/s/user multiple (~2× vs CS-3, ~20–40× vs Blackwell on SA's stack).

| Axis | Scales with 2× clock on WSE-3 | Does not scale (needs next silicon) |
|---|---|---|
| On-wafer SRAM bandwidth | Yes → 43 PB/s marketed | — |
| Peak theoretical FLOPs | Yes | — |
| Off-wafer I/O | Yes → 1.2 to 2.4 Tb/s | — |
| Tokens/s/user (all else equal) | Near-double | — |
| SRAM capacity | — | 44GB/wafer, bit-cell limited |
| Expert-shard-across-wafers | — | Still blocked by µs-class I/O |

**Parallelism screen (why pipeline is the only WSE strategy).** GPUs commonly use tensor and expert parallelism so a big model fits in HBM; WSE cannot hold full weights in 44GB, but also cannot afford EP/ETP because token dispatch/combine is latency-sensitive and 3µs switched / 2µs direct is still orders of magnitude slower than competitors' nanosecond switch claims. Result: every MoE expert sits on one wafer, interleaved; GPT 5.6 Sol still fits that pattern. GPU comparison is therefore config-dependent: GPUs span high-throughput/low-interactivity through high-interactivity/low-throughput; the wafer only lives in the latter. TileRT is the GPU tool that populates the high-throughput corner SA wants in the comparison set.

**KV versus weights (the capacity tax).** Weight footprint ∝ parameters. KV footprint ∝ concurrent users × request context. Long-context + high concurrency is what forces wafer count, capex, and power — not "can the model run at all." Worked SA case: DeepSeek V4 Pro 1.6T at 1M ctx ≈ 20 WSE min, ≈ 40 at 256 concurrency, ~$20M + 1MW before a forward pass. Predicted customer response (OpenAI / 5.6 Sol): cut context (256k not 1M) to save on-wafer KV.

**Disagg topology and the PO-ratio trap.**

| Topology | What CS-4 does | Who owns the interface | Economic catch |
|---|---|---|---|
| Homogeneous WSE pipeline | Decode (and whatever fits) on wafers | Cerebras SwarmX / CSoft | Capacity wall; 44GB; KV tax |
| PDD (prefill-decode disagg) | WSE = decode; HBM XPU / Trainium / AMD = prefill | AWS EFA, or other orchestrator | P:D ratio frozen at PO; 5+ year mismatch risk |
| AFD (attention-feedforward disagg) | WSE paired with HBM XPUs for capacity | Same | Same freeze; analogized to Nvidia Groq LPU + GPU |
| GPU/TPU only | Dynamic re-slice of the same fleet | Nvidia / Google / AWS | Lower peak interactivity; flexible mix |

Methodology: classify any CS-4 headline on (1) same silicon or new wafer, (2) bandwidth versus capacity, (3) which disagg topology, (4) who owns the NIC/routing layer, (5) whether tok/s/user is a same-model measurement or a vendor/SA stack. Do not treat 43 PB/s or "2,000× Rubin" as the investable multiple; tok/s/user and TCO per token are.

This is [[Industry - Semiconductors]] #8 (architecture remaps the bottleneck at decode) without proving #2 (qualification gate). It activates [[Lens - Value Layer Monopoly]] as a **layer-renter** hypothesis (TSMC below, AWS/Nvidia interface above) and [[Generalist - Overview]] [G-14] only on *latency* elasticity: 2× tokens/s at similar TCO is the WTP-for-speed bet, not a cheap-token bet. [G-10] merchant-challenger base rate remains the adversarial check.

## Evidence

All figures below are single-sourced to the 19 August 2026 SemiAnalysis CS-4 post unless tagged otherwise. Gmail `1a017a9129d52f60`, sender `semianalysis@substack.com`, 2026-08-19T01:32:08Z. [1×: SemiAnalysis]

### Silicon, clock, I/O, SRAM

| Item | Figure | Tag |
|---|---|---|
| Silicon | Same 5nm WSE-3 as CS-3; CS-4 is 4th-gen *rack* | [1×: SemiAnalysis] |
| Clock | 2× vs CS-3, via more power + improved power delivery and cooling | [1×: SemiAnalysis] |
| SRAM capacity | 44GB per wafer, bit-cell limited; no change this gen | [1×: SemiAnalysis] |
| On-chip SRAM bandwidth (Cerebras) | 43 PB/s total | [IR: Cerebras via SA] |
| vs Rubin bandwidth (Cerebras marketing) | ~2,000× | [IR: Cerebras via SA] |
| Off-wafer I/O | 1.2 Tb/s (CS-3) → 2.4 Tb/s (CS-4) | [1×: SemiAnalysis] |
| I/O hardware | Field-upgradeable FPGA NIC; proprietary wafer I/O → standard Ethernet; 2 modules, north and south of wafer | [1×: SemiAnalysis] |
| Switched fabric latency | 5µs (CS-3) → 3µs (CS-4); 2-layer fat-tree, Arista Ethernet | [1×: SemiAnalysis] |
| Direct wafer-to-wafer | 2µs; FPGA has switching/routing across wafers | [1×: SemiAnalysis] |
| SA view of networking | Modest vs competitors quoting nanosecond all-in switch latency; 3µs + BW still blocks EP/ETP | [1×: SemiAnalysis] |
| Workload fit | SRAM architecture for low arithmetic-intensity kernels; low-batch decode | [1×: SemiAnalysis] |

### Rack, power, cost

| Item | Figure | Tag |
|---|---|---|
| CS-3 wafers/rack | 2 | [1×: SemiAnalysis] |
| CS-4 wafers/rack | 3 backpacks; one WSE each | [1×: SemiAnalysis] |
| Backpack split | Front half power, rear half compute; vertical WSE; power from wafer front (same as CS-3); cooling from rear; I/O on top and bottom edges | [1×: SemiAnalysis] |
| Facility cooling | Pump and heat exchangers removed from rack; assumes fully liquid-cooled data centers | [1×: SemiAnalysis] |
| CS-4 rack TDP | 125–135kW | [1×: SemiAnalysis] |
| CS-3 power | 23kW per wafer | [1×: SemiAnalysis] |
| Implied CS-4 kW/wafer | 125–135kW / 3 ≈ 42–45kW ≈ ~1.8–2.0× CS-3 23kW | [est.: rack TDP / 3 backpacks] |
| Performance/W | At best a slight improvement vs CS-3 | [1×: SemiAnalysis] |
| BOM per wafer | SA: similar to CS-3; simpler assembly offsets extra power/cooling | [est.: SemiAnalysis] |
| Customer TCO claim | Nearly 2× interactivity and token revenue at similar TCO; 2× perf/TCO | [est.: SemiAnalysis] |
| Deploy | Power rack first, socket wafer backpacks on site | [1×: SemiAnalysis] |

### Interactivity (tok/s/user)

| Item | Figure | Tag |
|---|---|---|
| CS-3 | ~2,000 tok/s/user | [1×: SemiAnalysis] |
| CS-4 (SA) | near 4,000 tok/s/user on frontier models | [est.: SemiAnalysis] |
| Cerebras GPU interactivity claim | up to 30×; branded "ultrafast" tier | [IR: Cerebras via SA] |
| Blackwell theoretical | 200 tok/s/user (SA: nobody actually runs there) | [est.: SemiAnalysis] |
| Blackwell realistic | 100 tok/s/user at reasonable concurrency | [est.: SemiAnalysis] |
| SA implied CS-4 vs GPU | 20–40×; "why not up to 40×" | [est.: SemiAnalysis] |
| GPU operating range | High-throughput/low-interactivity through high-interactivity/low-throughput; TileRT populates the former | [1×: SemiAnalysis] |
| WSE operating range | Only high-interactivity / low-throughput | [1×: SemiAnalysis] |

### Models, KV, capex

| Item | Figure | Tag |
|---|---|---|
| MoE mapping | Every expert for a given model on a single wafer, interleaved; pipeline parallel default | [1×: SemiAnalysis] |
| GPT 5.6 Sol | Experts still fit on one 44GB wafer; no cross-wafer expert shard yet | [1×: SemiAnalysis] |
| OpenAI context (SA expectation) | 5.6 Sol at 256k context, not full 1M, to save on-wafer KV | [est.: SemiAnalysis] |
| KV scaling law (SA) | KV memory ∝ concurrent users × context; weights ∝ parameters | [1×: SemiAnalysis] |
| DeepSeek V4 Pro | 1.6T parameters | [1×: SemiAnalysis] |
| V4 Pro @ 1M ctx, min | ~20 WSE | [est.: SemiAnalysis tokenomics] |
| V4 Pro @ 1M ctx, 256 concurrency | ~40 WSE | [est.: SemiAnalysis tokenomics] |
| Upfront for that config | over $20M capex + 1MW before a forward pass | [est.: SemiAnalysis tokenomics] |

### Disagg, partners, roadmap

| Item | Figure | Tag |
|---|---|---|
| Partners named | AMD and AWS Trainium; more coming | [1×: SemiAnalysis] |
| CS-4 role | Decode chip; rooflines not optimal for compute-bound prefill | [1×: SemiAnalysis] |
| Modes claimed | PDD and AFD | [IR: Cerebras via SA] |
| AWS-specific | EFA NICs on CS-4 to interface with Trainium servers; "designed especially for AWS" | [1×: SemiAnalysis] |
| Nvidia analogue | Pair CS-4 with HBM XPUs "in the same way that Nvidia is positioning the Groq LPUs" | [1×: SemiAnalysis] |
| Disagg catch | Prefill:decode resource ratio fixed at hardware PO; GPU/TPU fleets re-slice dynamically; 5+ year life | [1×: SemiAnalysis] |
| Workload mix shift (SA) | Reasoning raised decode cost; then agentic cache hits cut prefill cost, decode stayed | [1×: SemiAnalysis] |
| Next platform | Nexus rack-scale; CS-4 chassis likely carries to CS-5 / next wafer without major mechanical redesign | [1×: SemiAnalysis] |
| Cadence | ~2× performance every year; 20× throughput by 2027 | [IR: Cerebras via SA] |
| Reliability | Field tray swaps, error recovery, tray-level redundancy, yield harvesting on cores and channels | [1×: SemiAnalysis] |
| More detail | Hot Chips (forthcoming) | [1×: SemiAnalysis] |

## Contradiction Check

**[[Theses/CBRS - Cerebras Systems]] §Outstanding Question 4 ("Does WSE-4 fix wafer-scale's capital-efficiency problem?") and §Catalysts "WSE-4 launch (late 2026 / early 2027)."** This source **does not answer Q4.** CS-4 is not WSE-4 and not 3D-stacked SRAM on N3. 44GB/wafer is unchanged; SRAM-only capital inefficiency is unfixed. What moved is clock, rack density, I/O, and assembly cost. SA's "BOM per wafer similar, ~2× tok/s/user" is a *TCO-per-token* improvement via power/clock, not a capacity or $/token architecture fix. Supports the 9 August IA mashup ([[Research/2026-08-09 - CBRS WOLF HBF AAOI TSEM IA Weekly Mashup - deep-dive]]) gen-3.5 power/clocks read (Feldman "doubling the clocks with new power delivery") more than the thesis's WSE-4 framing. Falsifier for "this *is* the capital-efficiency print": a subsequent Hot Chips or CS-5/Nexus wafer that actually adds SRAM density or 3D stack, with disclosed $/token.

**[[Theses/CBRS - Cerebras Systems]] Insight #3 (SRAM-only is the architecturally correct decode bet) and §Business Model (low-batch decode appliance; 1.2 Tb/s I/O vs 21 PB/s on-wafer).** Supports the decode-appliance identity and updates the I/O floor: 2.4 Tb/s and 3µs/2µs. Does **not** make fine-grained tensor split viable; SA still blocks EP/ETP. The 43 PB/s / 2,000× Rubin headline is the number that will lead coverage; the thesis already warned that peak SRAM bandwidth is not the economic object — tok/s/user, utilization, and workflow Amdahl are. CS-4's ~2× tok/s/user at similar TCO is the first clean gen-on-gen of that object.

**[[Theses/CBRS - Cerebras Systems]] Insight #3 / heterogeneous interconnect (AWS Trainium3 prefill → EFA KV handoff → CS-3 decode) and [[Lens - Value Layer Monopoly]] WEAK FIT.** Supports and tightens the layer-renter read. CS-4 I/O is "designed especially for AWS" EFA + Trainium; AMD is a named second partner; Cerebras claims AFD as well as PDD. Interface and P:D ratio sit with the orchestrator who signs the PO. IA's prior that <5µs I/O *blocks* prefill/decode split is weakened on latency (now 3µs/2µs) but SA still does not call the hop cheap — only "easier to interface." Trainium-going-well is now a SemiAnalysis engineering claim, not only an IA rumor.

**[[Theses/CBRS - Cerebras Systems]] §Conviction Triggers → LOW if "Nvidia Rubin + Groq LPU demonstrates decode within ~3× of CS-3 on mainstream open models."** Evidence-touched, **dir = away from LOW / not fired.** SA stack: CS-3 ~2,000 tok/s/user, CS-4 ~4,000; Blackwell 200 theoretical / 100 realistic. That is 10–20× (CS-3 vs GPU) and 20–40× (CS-4 vs GPU), not ~3×. Caveats that keep it from firing the other way: not a same-model open-weights benchmark; "frontier models" unnamed; Groq LPU tok/s absent from this piece; TileRT is flagged as the GPU config that must be in the next comparison. HIGH (OpenAI ≥~$300M by FY2027 AND UAE <50% AND cloud GM >35% two quarters) and CLOSE (export / OpenAI 750MW cut / UAE >70% by end-2027) are **no-touch**.

**[[Theses/CBRS - Cerebras Systems]] Outstanding Question 5 (Nvidia or AWS foreclosure of fast decode) and Question 6 (TSMC capacity / no LTA).** Q5: CS-4 is built to live *inside* AWS (EFA) and next to AMD, while Nvidia occupies the same SRAM-decode niche with Groq LPUs. That is coexistence / foreclosure-by-interface, not a measured Groq-within-3× print. Q6: CS-4 **does not pull a new TSMC node** — 5nm WSE-3 reuse — so this generation does not tighten the N3/N2 queue risk; it also does not create an LTA. [[Theses/TSM - Taiwan Semiconductor]] re-armed HIGH/LOW/CLOSE (FY26 growth, GM, 2027 capex, HPC growth, Arizona N2, Intel 18A) are **no-touch**.

**[[Theses/NVDA - Nvidia]] Outstanding Question on the Groq LPX deal; no Conviction Triggers section (structural gap).** Supports the thesis's own admission that GPU architecture is not optimal for dedicated low-latency decode: SA treats Groq LPU + HBM XPU as the Nvidia-side analogue of CS-4 + HBM XPU, and treats TileRT as the GPU answer on the *throughput* corner. Does not speak to CUDA, Omniverse, or MLPerf Training. Flag: NVDA still has no registered Conviction Triggers to touch.

**[[Theses/AVGO - Broadcom]] (live book, Ethernet / custom XPU).** Weak adjacency only. The named CS-4 fabric is **Arista** Ethernet, not Tomahawk/Jericho. Trainium is an AWS partner in this piece, not a Broadcom XPU socket. No AVGO Conviction Triggers section exists. Do not propagate as an AVGO evidence print.

**[[Theses/AMD - Advanced Micro Devices]] §Conviction Triggers HIGH (3rd hyperscaler ≥2GW / MLPerf / Llama-on-ROCm) and the 9 August IA "MI450 slide, engineering not started" rumor.** Named "working with AMD … as partners" is a Cerebras-side disagg claim, **not** a GW commit, MLPerf print, or Helios ship. Does not fire AMD HIGH or LOW. Softly challenges IA's "Cerebras+MI450 is fake" only as a partnership mention; no engineering evidence here.

Mental-model triggers for a later `/sync` (ingest does not write thesis bodies): Semis #8 decode remap — fires, clock-scaled SRAM BW. Semis #2 qualification gate — still does not fire (speed ≠ gate). Semis #10 anchor concentration — OpenAI named only as a 256k-vs-1M KV customer, no mix/revenue print. VLM layer-renter — fires harder via AWS EFA design-in. [G-14] latency elasticity — 2× tok/s at similar TCO is the WTP test. [G-10] merchant-challenger base rate — unchanged; SA still calls the product very expensive.

## Source Excerpts

> "CS-4 is their fourth-generation rack built around the same third generation 5nm wafer-scale engine: WSE-3." [1×: SemiAnalysis]

> "The CS-4 uses the same 5nm WSE-3 as the CS-3, but Cerebras is extracting double the performance by doubling clock speeds. … the CS-4 to upgrade to 2.4Tb/s of off-wafer I/O from 1.2Tb/s with CS-3. However, what remains the same is 44GB of SRAM capacity per wafer." [1×: SemiAnalysis]

> "latency through the 2 layer fat-tree network (using Arista ethernet switches) is reduced to 3 microseconds from 5 microseconds for CS-3. … direct wafer to wafer links … further reduces latency to 2 microseconds." [1×: SemiAnalysis]

> "We believe this 3µs and bandwidth limitations continues to be a bottleneck that prevents parallelism setups such as EP and ETP. … pipeline parallelism the only viable solution." [1×: SemiAnalysis]

> "a CS-4 rack holds three of them, up from two wafers per rack in CS-3. … One CS-4 rack lands at 125-135kW TDP, which is up around or just short of double the 23kW power draw of a single CS-3." [1×: SemiAnalysis]

> "Cerebras’s favorite number for CS-4 is 43 PB/s of total on-chip memory bandwidth, which the company markets as roughly 2,000x more memory bandwidth than Nvidia’s Rubin." [IR: Cerebras via SA]

> "We believe CS-4 will hit near 4,000 tok/sec/user on frontier models, while CS-3 hits 2,000 tok/sec/user. Meanwhile we expect Blackwell GPUs will continue to top out at a theoretical 200 tok/sec/user … and a more realistic 100 tok/sec/user for reasonable amounts of concurrency." [est.: SemiAnalysis]

> "the minimum number of Cerebras WSE’s needed to run this model [1.6T DeepSeek V4 Pro] at 1M ctx is around 20 systems, and at a reasonable concurrency of 256 requests, its around 40 systems. That’s over $20M of CAPEX and 1MW of power consumption before you can get a forward pass on a frontier model." [est.: SemiAnalysis]

> "This seems to be designed especially for AWS in mind, who would like to have its EFA NICs on CS-4 to interface with Trainium servers for disaggregated inference." [1×: SemiAnalysis]

> "Pairing the CS-4 with HBM-based XPUs in a disaggregated attention feed-forward network setup is one way to overcome the CS-4’s low memory capacity, in the same way that Nvidia is positioning the Groq LPUs." [1×: SemiAnalysis]

> "the ratio of Prefill to Decode resources in your cluster is fixed the day that the hardware PO is signed." [1×: SemiAnalysis]

> "roughly 2x faster performance every year, with a specific target of 20x throughput improvement by 2027." [IR: Cerebras via SA]

> "Double the bandwidth can double customers’ token revenue and result in a 2x perf/TCO improvement. However, Cerebras is still a very expensive solution that is betting on customers’ willingness to pay significantly more for fast tokens." [1×: SemiAnalysis]
