---
publish: false
date: 2026-07-27
tags: [research, Semiconductors, AMD, NVDA]
sector: Custom Silicon & Networking Semiconductors
ticker: AMD
propagated_to: [AMD, NVDA]
source: 'https://bepresearch.substack.com/p/amd-showed-a-15-lead-its-own-slide'
source_type: deep-dive
updated: 2026-08-14
---

# AMD Showed a 15% Lead — Its Own Slide Walks It Back

## Thesis Delta
Consensus prices Advancing AI Helios **+15% vs Vera Rubin** (plus Baird **$1,250** / Jeff Pu **45× 2027E**) as [[Theses/AMD - Advanced Micro Devices]] catching [[Theses/NVDA - Nvidia]] on hardware merit → BEP (long NVDA since 2016, no AMD) reads AMD’s own Moscone slide as a **dense-flops lead that decays with interactivity** toward AMD’s **+6% HBM bandwidth** edge, with NVIDIA answering via Transformer Engine adaptive compression (markets **50 PF/package / 3.6 EF/rack** vs **35 PF dense**) rather than more silicon. [G-13] priced variable is spec-lead share-gain; source variable is interactivity-decay + whether compression is real + the multiple — AMD can take merchant share and still be the expensive way to own the same demand; touches AMD §Outstanding Q#2 and → LOW (gap >25% to GR200) because compression-realized Helios is **−19%**, not yet through the tripwire.

## Summary
Lisa Su’s Moscone chart, titled “AMD Helios Delivers Industry Leading Rack Scale Performance,” plots throughput against interactivity on **Kimi K2 Thinking**, a reasoning model AMD chose. Photographed from the seat, the bars read **+15% / +12% / +10%** at low / medium / high interactivity versus Vera Rubin. Su’s opening frame is the reason the decay matters: 2026 is the first year inference exceeds training, inference is **~60%** of AI compute, and high interactivity is where that work sits — and where Helios is least separated from NVIDIA’s next rack. BEP went looking for a chart trick and found the opposite. Helios ÷ 72 ≈ **40 PF FP4** per GPU; NVIDIA’s Rubin docs put a package at **35 PF dense NVFP4**; 72 × 35 = **2.52 EF**, which is exactly the Vera Rubin number AMD’s +15% credits. Packages against packages, dense against dense. Moor Insights flags MXFP4 vs NVFP4 block-scaling, but AMD took the conservative NVIDIA dense figure and did the arithmetic straight. NVIDIA does not market 35. It markets **50 PF / 3.6 EF**, and that delta is not silicon — it is an adaptive compression engine in the Transformer Engine that strips zeros in flight, replacing the 2:4 structured sparsity NVIDIA used to double marketing numbers. Against 3.6 EF, Helios at **2.9 EF** is **−19%**. BEP will not treat 50 as realized: nobody outside NVIDIA has benchmarked the engine on a real workload. Both sides are vendor numbers on unshipped parts; AMD’s +15% is a specification comparison, held to the same standard as NVIDIA’s 50. Either way the lead is a lead in **dense silicon**, and NVIDIA’s answer is not more silicon.

The decay is on AMD’s slide, not inferred. Endpoints: compute **+15%**, HBM bandwidth **+6%**. Low interactivity is batch-heavy work near peak throughput, so the lead sits near the flops ratio. As interactivity rises, decode latency and memory movement dominate: weights and KV cache move for every token, and the governing number is bandwidth. The line walks from AMD’s compute number toward AMD’s bandwidth number, and the bandwidth number is six. Scale-up bandwidth on the same slide reads **Same**, **260 TB/s**. A recording artifact has Su saying “50% more compute” at this point; the slide and Moor Insights both read 15, so BEP treats 50 as transcription error. Demand-pull color, not silicon: 9:30am keynote with open seats versus hours-long March SAP Center line for Jensen; AMD copied DGX Spark (Gorgon Halo on the exhibit floor).

The $1.4T accelerator TAM does the work in the bull case, BEP’s included. Same event last year: **~$500B by 2028**. This year: **$1.4T by 2030** — horizon moved with the number. Server CPU guide **$60B → >$200B** against a **$25B** base. Su flagged it before the chart: market data is “really hard to put up” because “every few months we’re changing the perspective based on what our customers are saying.” Physical constraint BEP names: capex has to land as megawatts where the grid will not interconnect new load for years. Adoption constraint: Deloitte **11%** of organizations running agents in production versus **38%** piloting. [G-4] / [G-10]: treat the TAM step as a frenzy-phase revision cadence to test, not as a TAM that has already been earned.

On the ramp, AMD won the “can we build a rack” argument. A February SemiAnalysis note had pushed Helios manufacturing to **Q2 2027**; AMD denied it. Moor Insights put the timing question to Su: **“Declaring production means we are ready to ship,”** ramp through Q4 into **1H 2027**. BEP’s own call: **meaningful volume in 2H 2027**, two quarters past AMD’s window. Helios is 72 MI455X + 18 Venice, UALink-over-Ethernet on Broadcom — AMD’s first Blackwell-style rack, with more external cabling and integration complexity in the part of the stack NVIDIA has spent years learning. Jensen in January: Vera Rubin tray has no cables, no hoses, no fans. Six months later Su held up a Helios tray **>160 lb**. Nick Dorsey (Midnight_Captl) relayed a Wiwynn ODM conversation: MI455 has “lot of challenges,” first rack-scale plus Broadcom scale-up, “see how they come together 2nd half next year”; customers optimistic *if* the rack works. One channel datapoint, not confirmation. BEP’s named falsifier: **material Helios revenue in AMD Q1 or Q2 2027** — a clean Q4 is already guided and would tell him nothing. Evidence against the late-ramp call is what he stood in front of: Supermicro (which he owns) liquid-cooled AMD racks, twenty-year product manager optimistic, build quality good — those were **CPU** racks, not Helios GPU racks, so they show a channel building and cooling AMD silicon at volume. Distinct from [[Research/2026-07-25 - AMD Advancing AI CUDA Moat Helios - deep-dive]]: that SemiAnalysis piece scores Helios as flyover-cable / ~550-retimer / Meta-cut-down manufacturing hell plus CI-gating composability. This BEP piece does not run those counts. It uses the same keynote as a **spec-decay + relative-value** argument.

OpenAI and Meta each hold a performance warrant for up to **160M** AMD shares (~**10%** apiece) vesting on deployment against **6 GW** commitments — together **~320M** shares, close to a fifth of the company, strike a penny. AMD’s up-to-**$5B** Anthropic investment was reported July 22; Tom Brown committed **2 GW** the next day. Warrants vest on deployment, so the incentive is to build; Su says all three are co-developing Helios, deeper than an endorsement. BEP’s precision: AMD’s loudest public validation came from parties holding unusually large equity claims on the outcome they were validating. The hallway counterweight: a neocloud operator, no equity in AMD, whose customers had told him to wait for Helios and who now wants to scale into the **hundreds of megawatts** — demand queued behind availability.

The franchise BEP would not bet against is the CPU, not Helios. Two days earlier NVIDIA’s Vera whitepaper named EPYC Turin **9755** beside a vendor-run estimated SPECrate **925 vs 898**. Forty-eight hours later Su answered: Venice **1.8×** Turin on **512** threads, and **+20%** per-core versus Vera using NVIDIA’s own published data. Each company benchmarked the other’s unshipped part, in public, by name, in the same week. Venice is also placed in a “sandboxes” tier — dedicated CPU capacity for agent steps that are not a forward pass (orchestration, tool calls). Logic holds; she described the tier without showing what runs there or what it costs, and the **>$200B** server-CPU number depends on whether anything does. Physical tell: nobody liquid-cools a CPU rack, as Supermicro had, unless thermal load justifies it. AT&T: **>45B** tokens/day on AMD across **122** production pipelines.

AMD is squeezed from two directions and can gain merchant GPU share while both jaws close on the economics. **Above**: custom silicon. BEP’s prior Google Cloud Next read is that Google is not trying to beat NVIDIA — it is making GCP the neutral venue where **TPU and NVIDIA** both monetize enterprise agents. Two fleets run side by side there, and AMD is in neither. AMD loses the moment the merchant slot is contested rather than expanded. **Below**: a funded field of inference specialists, **~$58B** of private paper (Deedy Das, July 25), Cerebras public at **~$48B**. AMD’s fast-inference answer is a [[Theses/CBRS - Cerebras Systems]] partnership; Cerebras answers to its own shareholders. NVIDIA licensed Groq’s technology outright and hired Jonathan Ross with it. Squeeze-biting observable: merchant GPU share falling while accelerator spend keeps rising. Missing layer: the stack is silicon, interconnect, software, **and models**. AMD launched the first three this week. NVIDIA ships Nemotron as a full development stack with no revenue or user thresholds — a distribution channel into every enterprise building its own AI. [VLM] hypothesis: the layer AMD does not own is the one NVIDIA can give away.

The strongest case *against* BEP’s NVDA-preference is software. His own 2026 prediction was ROCm **3–5 years** behind in tooling maturity. What AMD showed is an attempt to make coding agents developers already use fluent in ROCm — Cursor, Claude, Codex demos. Nobody has to learn AMD’s tooling if the agent already knows it. If that lands, the software gap closes faster than the hardware gap. [Automation Lens B]: that is a vendor-layer hypothesis (agents as the distribution path for ROCm), not a measured CI result — and it is a different object than the SemiAnalysis gating/composability scoreboard.

So what: the market wants a credible second source, and AMD is finally offering one. The question is no longer whether AMD can ship. It is what you pay for the shipping. **10%** of AMD’s own **$1.4T** 2030 accelerator TAM is **$140B/yr** against **$5.8B** data-center revenue in the March quarter — and that 10% assumes the squeeze does not bite and that GPUs stay the vast majority of the market (Su). Wall Street ran the arithmetic the other direction the next day. Baird took its target to a street-high **$1,250 from $625**, modeling **$147B** AMD AI GPU revenue by 2030 on an assumed **15%** share. That is within **$7B** of BEP’s $140B, except Baird calls it 15% and BEP calls it 10%. Fifteen percent of $1.4T is **$210B**, so Baird’s share is being applied to something nearer **$980B**. The most bullish note on the street is implicitly applying AMD’s share to an addressable pool **~30%** below AMD’s headline TAM — custom silicon, or categories not considered available to merchant GPUs, already cut out. The top jaw is embedded inside the bull case. Jeff Pu’s **$640** is explicitly **45× 2027E**. NVIDIA trades high-teens to low-twenties on forward earnings. Same demand, same week, more than twice the multiple for the smaller and later-arriving name.

The warrant cost sits outside that multiple. **320M** penny-strike shares are a customer-acquisition cost that lands in the share count where a P/E cannot see it. Under **ASC 260**, contingently issuable shares stay out of diluted EPS until conditions are met, and these vest on milestones nobody has hit. Illustration, not a BEP target: against **1.65B** shares, full vesting takes **~16%** off per-share earnings, which puts that same 45× nearer **$535** than $640 — and only happens if AMD ships six gigawatts, i.e. has earned the dilution. What would move BEP: an independent inference benchmark that tests NVIDIA’s compression claim against AMD’s dense flops. Helios is credible, customers are real, the market is large enough for AMD to grow. Credible competition is not attractive relative value. AMD is valued as though execution, share, and TAM arrive together. NVIDIA is already delivering into the same demand without promising customers warrants equal to nearly a fifth of its share count. AMD may win. BEP still thinks NVIDIA is the cheaper way to own the outcome. Author book: long NVDA, NOW, LITE, CRDO, TSEM, LSCC, ALAB, WOLF, SMCI, BE, ORCL (2027 LEAPS). Coming calendar he flags: AMD Q2 Aug 4 (tests ramp language); NVIDIA FQ2 Aug 26. Nobody has benchmarked Helios; every number on the comparison slide is a spec or estimate; microbenchmark footnotes cite **1–4 GPUs**; the only live on-stage run was a small model on a single GPU. Venice was called in production, then footnoted as preliminary estimates based on engineering projections; SPEC26 subscores that would settle the CPU fight have not been published.

## Framework / Mental Model
The source names and applies three schemes. They are how BEP wants the keynote read; they are not vault verdicts.

**1. The Lead That Narrows (named section).** A spec lead is not a single number. It is a curve whose x-axis is interactivity. Low-interactivity / batch work runs near peak throughput, so the lead sits near the dense-flops ratio (here +15%, Helios 40 PF vs Rubin 35 PF dense, 2.52 EF). High-interactivity / decode work is bandwidth- and latency-bound (weights + KV moved per token), so the lead walks toward the HBM-bandwidth ratio (here +6%). Scale-up “Same” (260 TB/s) is the silent third endpoint. Methodology: photograph the vendor slide, reconcile the +15% against the incumbent’s *dense* published figure, then refuse to treat the incumbent’s *marketed* compressed figure (50 PF / 3.6 EF) as realized until an independent bench exists. Both endpoints must come from the same slide or the decay is the analyst’s invention.

**2. Two-jaw squeeze.** AMD can take merchant GPU unit share while economics are compressed from above (custom silicon contesting the merchant *slot*, not just “hyperscalers walk away”) and from below (funded inference specialists; Cerebras partnership vs NVIDIA’s Groq license-and-hire). Observable that the squeeze is biting: merchant GPU share falling while accelerator spend keeps rising. Implication for TAM math: a 10–15% AMD share applied to headline $1.4T already assumes the top jaw does not close; Baird’s $147B-on-15% print shows the street is already applying share to a ~$980B pool.

**3. Incentivized-validator vs unincentivized-queue.** Warrant-linked 6 GW names (OpenAI, Meta) plus cash-linked Anthropic are real demand *and* equity claims on the outcome they validate; weigh them differently from a hallway neocloud with no AMD paper whose customers queued behind Helios availability. Dilution is a CAC that ASC 260 keeps out of the P/E until milestones hit.

## Evidence

### Spec lead and the decay curve
| Item | Figure | Tag |
|---|---|---|
| Helios vs Rubin, Kimi K2 Thinking | +15% / +12% / +10% at low / med / high interactivity | [1×: AMD slide via BEP photo] |
| HBM bandwidth (same slide) | +6% | [1×: AMD slide] |
| Scale-up bandwidth (same slide) | Same, 260 TB/s | [1×: AMD slide] |
| Helios dense math | ~40 PF FP4/GPU; 72 × 40 ≈ 2.9 EF/rack | [1×: BEP arithmetic on AMD slide] |
| Rubin dense (NVIDIA docs) | 35 PF NVFP4/package; 72 × 35 = 2.52 EF | [1×: NVIDIA Rubin docs via BEP] |
| +15% reconciliation | 2.9 / 2.52 ≈ +15% (dense vs dense) | [est.: BEP] |
| NVIDIA marketed | 50 PF/package; 3.6 EF/rack (Transformer Engine adaptive compression; replaces 2:4 sparsity) | [1×: NVIDIA / BEP] |
| Helios vs marketed Rubin | 2.9 vs 3.6 EF = −19% | [est.: BEP] |
| Format caveat | AMD MXFP4 vs NVIDIA NVFP4; block scaling differs | [1×: Moor Insights via BEP] |
| Su “50% more compute” | Treated as transcription artifact; slide + Moor Insights = 15 | [1×: BEP] |
| Inference share of AI compute (Su) | ~60%; 2026 first year inference > training | [1×: AMD keynote via BEP] |
| Workload on the chart | Kimi K2 Thinking (AMD-chosen reasoning model) | [1×: AMD slide] |
| Independent bench status | None. Slide = spec/estimate; footnotes 1–4 GPUs; live demo = small model, single GPU | [1×: BEP] |

### TAM, CPU, and Venice
| Item | Figure | Tag |
|---|---|---|
| Accelerator TAM, Advancing AI 2025 | ~$500B by 2028 | [1×: AMD keynote via BEP] |
| Accelerator TAM, Advancing AI 2026 | $1.4T by 2030 | [1×: AMD keynote via BEP] |
| Server CPU TAM guide | $60B → >$200B vs $25B base | [1×: AMD keynote via BEP] |
| Su on TAM revisions | “every few months we’re changing the perspective” | [1×: AMD keynote] |
| Agents in production vs pilot | 11% / 38% of organizations | [1×: Deloitte via BEP] |
| Vera vs Turin 9755 SPECrate | 925 vs 898 (vendor-run, estimated) | [1×: NVIDIA Vera whitepaper via BEP] |
| Venice vs Turin | 1.8× on 512 threads | [1×: AMD keynote] |
| Venice vs Vera per-core | +20% (using NVIDIA’s published data) | [1×: AMD keynote] |
| Venice production footnote | Called in production; comparison is “preliminary estimates based on engineering projections”; SPEC26 subscores unpublished | [1×: BEP] |
| AT&T on AMD | >45B tokens/day; 122 production pipelines | [1×: AT&T via BEP] |
| Sandboxes tier | Dedicated CPU for non-forward-pass agent work; no workload or cost shown | [1×: AMD keynote via BEP] |

### Ramp, validators, squeeze, valuation
| Item | Figure | Tag |
|---|---|---|
| SemiAnalysis Feb manufacturing call | Helios ramp pushed to Q2 2027; AMD denied | [1×: BEP citing SemiAnalysis] |
| Su / Moor Insights | “Declaring production means we are ready to ship”; ramp through Q4 into 1H 2027 | [1×: Moor Insights / Su] |
| BEP volume call | Meaningful Helios volume 2H 2027 (two quarters past AMD window) | [est.: BEP] |
| Helios config | 72 MI455X + 18 Venice; UALink over Ethernet on Broadcom | [1×: AMD / BEP] |
| Helios tray | >160 lb; more external cabling than Rubin | [1×: Su / BEP] |
| Rubin tray (Jan) | No cables, no hoses, no fans | [1×: Jensen via BEP] |
| Wiwynn via Dorsey | MI455 “lot of challenges”; first rack-scale + Broadcom scale-up; “2nd half next year”; customers buy *if* rack works | [1×: @Midnight_Captl] |
| BEP ramp falsifier | Material Helios revenue in AMD Q1 or Q2 2027 (clean Q4 already guided) | [est.: BEP] |
| SMCI floor | Liquid-cooled AMD **CPU** racks; PM optimistic; not Helios GPU | [1×: BEP, long SMCI] |
| OpenAI / Meta warrants | 160M shares each (~10% apiece), $0.01, vest on 6 GW deployment; 320M combined ≈ one-fifth of AMD | [1×: BEP] |
| Anthropic | AMD invests up to $5B (Jul 22); Tom Brown 2 GW next day; all three co-developing Helios (Su) | [1×: BEP] |
| Hallway neocloud | Customers held for Helios; wants hundreds of MW; no AMD equity | [1×: BEP] |
| Custom-silicon jaw | GCP as TPU + NVIDIA venue; AMD in neither fleet | [1×: BEP prior GCP Next note] |
| Inference-specialist jaw | ~$58B private paper (Das Jul 25); Cerebras ~$48B public | [1×: @deedydas / BEP] |
| Fast-inference answers | AMD–Cerebras partnership vs NVIDIA Groq license + Jonathan Ross hire | [1×: BEP] |
| Squeeze observable | Merchant GPU share falling while accelerator spend rises | [est.: BEP] |
| Missing layer | Nemotron shipped as free full dev stack; AMD launched silicon + interconnect + software, not models | [1×: BEP] |
| Prior ROCm call | 3–5 years behind tooling maturity | [1×: BEP 2026 predictions] |
| Agent-fluent ROCm | Cursor / Claude / Codex demos; no one learns AMD tooling if the agent knows it | [1×: AMD keynote via BEP] |
| AMD DC revenue (Mar qtr) | $5.8B | [1×: BEP] |
| 10% of $1.4T TAM | $140B/yr AMD accelerator revenue | [est.: BEP on AMD TAM] |
| Baird | PT $1,250 from $625; $147B 2030 AI GPU on 15% share | [1×: Baird via BEP] |
| Implied Baird pool | $147B / 15% ≈ $980B (~30% below $1.4T); 15% × $1.4T = $210B | [est.: BEP] |
| Jeff Pu | $640 = 45× 2027E | [1×: Pu via BEP] |
| NVDA multiple | High-teens to low-twenties forward earnings | [1×: BEP] |
| ASC 260 | Contingent shares out of diluted EPS until milestones met | [1×: BEP] |
| Dilution illustration | 320M / 1.65B → ~16% off EPS; 45× $640 → ~$535 | [est.: BEP on Pu] |
| BEP move-me | Independent inference bench: NVIDIA compression vs AMD dense flops | [est.: BEP] |
| Print dates | AMD Q2 Aug 4; NVIDIA FQ2 Aug 26 | [1×: BEP] |
| Author book | Long NVDA, NOW, LITE, CRDO, TSEM, LSCC, ALAB, WOLF, SMCI, BE, ORCL 2027 LEAPS; no AMD | [1×: BEP disclosure] |

## Contradiction Check
**[[Theses/AMD - Advanced Micro Devices]] §Key Non-consensus Insight #2 (sole merchant full-stack; market still prices GPU-only; competitive surface is rack-to-rack).** Does not deny Helios is a real rack. Challenges the implication that rack-level comparison is already a 15-point win: AMD’s own slide walks +15% compute to +6% HBM bandwidth as interactivity rises, and scale-up is **Same at 260 TB/s**. The number the market just bid (Baird $1,250) is the low-interactivity intercept Su’s own 60%-inference frame says is the less relevant end. [Industry #8] hypothesis: architecture/workload shift remaps the bottleneck from dense FLOPs to bandwidth; test on independent high-interactivity benches, not this slide.

**AMD §Insight #5 (HBM-per-dollar / memory capacity wins inference).** This source’s decay endpoint is **bandwidth +6%**, not capacity. Capacity may still favor AMD; that is a different note ([[Research/2026-07-25 - AMD Advancing AI CUDA Moat Helios - deep-dive]] 432 GB / 12-Hi vs 288 GB). BEP’s slide does not print a capacity win that would carry the 60% inference mix. Challenges treating Helios as an inference-memory *bandwidth* win on the axis Su said is the work.

**AMD §Insight #3 (ROCm catch-up is step-function via framework releases; “already happened”).** BEP’s strongest case *against his own NVDA preference* is a different mechanism: agent-fluent ROCm (Cursor/Claude/Codex) so nobody learns AMD tooling. That is not Meta-forced framework-native parity and is not measured. Does not confirm Insight #3’s “already happened.” [Automation Lens B] / [G-6]: if agents collapse the tooling gap faster than 3–5 years, BEP’s relative-value read worsens; the SemiAnalysis note’s object (gating tests, WideEP composition) can still be red while this demo is green.

**AMD §Outstanding Q#2 (Helios rack-for-rack vs Rubin/GR200 at H2 2026 launch) and → LOW (published MLPerf gap >25% to GR200).** Ramp: BEP’s base is **2H 2027 meaningful volume**, two quarters past Su/Moor “ready to ship / through Q4 into 1H27.” That delays the “ships against Rubin in H2 2026” frame. Gap: if NVIDIA’s 50 PF / 3.6 EF compression is realized, Helios 2.9 EF is **−19%** — inside the 25% LOW trigger, not through it. If only dense 35 PF holds, AMD is +15% and LOW is not close. The trigger’s named observable is published MLPerf, not this spec slide. BEP’s own falsifiers: independent compression-vs-dense inference bench; material Helios revenue in **Q1 or Q2 2027**.

**AMD → HIGH (MLPerf Training v5.0 within 10% of Rubin AND Meta Llama 5 on ROCm AND 3rd hyperscaler ≥2 GW by end-Q3 2026).** Anthropic 2 GW + Tom Brown is a third *name* at 2 GW, but HIGH is written as Google/AWS-class plus MLPerf plus Llama-on-ROCm. Warrants are incentivized validators, not the independent bench. 0/3 HIGH still unmet on this source.

**AMD §Summary / §Mental Models “multiple consumed the bull case” and dilution correction (320M / ~16.7%).** Supports. Pu **45× 2027E** vs NVDA high-teens/low-20s is the same-week multiple gap; Baird $1,250 on **15% of a ~$980B implicit pool** is the street already haircutting Su’s $1.4T. BEP’s ASC 260 illustration (**~16%** off, $640 → ~$535) matches the thesis’s already-recorded 320M / ~16.7% max dilution. [G-1] / [G-13]: $140B at 10% of $1.4T against $5.8B March-quarter DC is the endgame the price is being asked to pre-pay. [G-10]: first-attempt next-gen spec-to-system parity on unshipped parts is a rare reference class.

**AMD §Bear Case #1 (Helios launches against Rubin, not Blackwell) and §Risks #4 (6 GW → 2–3 GW realized).** Directionally supports the timing/quality half (2H27 volume, first-rack cabling, Wiwynn challenges). Does not print a take-or-pay renegotiation. The hallway neocloud (hundreds of MW, no equity) cuts against a pure “commitments evaporate” read.

**[[Theses/NVDA - Nvidia]] §Summary and Insight #1 (CUDA/software generality; Transformer Engine; market over-punished NVDA into the cheapest AI multiple).** Supports. NVIDIA answers a dense-silicon deficit with **in-flight compression in the Transformer Engine**, not more transistors — the same “stack inherits the workload” claim, measured here as marketed 50 vs dense 35 PF. [Industry #2] / [VLM interface-control]: lock-in this generation is the compression/software layer, not the FLOP count. Distinct from [[Research/2026-07-25 - AMD Advancing AI CUDA Moat Helios - deep-dive]], which scores CUDA as **CI gating + composable disaggregated inference**, not as an adaptive-compression marketing-vs-dense gap. NVDA has no Conviction Triggers section; this source does not create one. On NVDA Outstanding Q (87% → 75% → 60% share): BEP says AMD can gain merchant share while both jaws close on *AMD’s* economics, and NVDA is the cheaper way to own the same demand — supports “absolute revenue grows as share moderates” *if* the TAM is real; does not resolve ASIC software maturation.

**[[Theses/CBRS - Cerebras Systems]] §Summary (last independent fast-inference after Groq).** Weak, two-sided. BEP sizes the below-jaw at ~$58B private + Cerebras ~$48B public and notes AMD’s answer is a partnership (Cerebras answers to its own shareholders) versus NVIDIA’s license-and-hire. Supports CBRS as a live inference specialist; does not score wafer-scale SRAM vs GPU.

**Disconfirming check (READING PROTOCOL).** BEP, the SemiAnalysis CUDA-moat note, and the NVDA thesis all point the same way (system/software > spec lead). That agreement is the cue to hunt the single falsifier, not to raise NVDA or cut AMD. This source’s own holes: every Helios-vs-Rubin number is an unshipped spec; compression 50 PF is unverified; Wiwynn is one X-relayed conversation; 2H27 volume is the author’s call; Baird’s $980B pool is inferred; $535 is arithmetic on Pu, not a BEP target; author is long NVDA and not AMD. [G-3] expensive error: treating AMD share-gain *trend* as a reason to pay 45× when the second-source is supposed to be the cheap way to own diversification.

## Source Excerpts
> “The advantage over NVIDIA’s Vera Rubin runs **+15% at low interactivity, +12% at medium, +10% at high**, on Kimi K2 Thinking, a reasoning model AMD picked.”

> “NVIDIA’s own Rubin documentation puts a Rubin package at **35 petaflops of dense NVFP4**, and 72 of those is 2.52 exaflops, exactly what AMD’s +15% credits Vera Rubin with.”

> “NVIDIA does not market 35. It markets **50 petaflops per package, 3.6 exaflops per rack**, and that delta is not silicon. It is an adaptive compression engine in the Transformer Engine that strips zeros out of the data stream in flight.”

> “Against that figure, Helios at 2.9 exaflops is 19% behind. I will not treat the 50 as realized performance, because nobody outside NVIDIA has benchmarked what that engine delivers on a real workload.”

> “The line is walking from AMD’s compute number toward AMD’s bandwidth number, and the bandwidth number is six.”

> “Scale-up bandwidth on the same slide reads **Same**, at 260 TB/s. Nobody said that out loud.”

> “it’s really hard to put this market data up because I feel like every few months we’re changing the perspective based on what our customers are saying.” — Lisa Su, before the $1.4T chart

> “Declaring production means we are ready to ship.” — Su, to Moor Insights; BEP: “My call is that meaningful volume lands in the second half of 2027, two quarters past AMD’s own window.”

> “He said mi455 has lot of challenges right now… first rack scale solution and it will have Broadcom scale up networking… we will see how they come together 2nd half next year.” — Wiwynn via Nick Dorsey

> “Google is not trying to beat NVIDIA. Google is making Google Cloud the neutral venue where TPU and NVIDIA both monetize enterprise agents.” — BEP, prior GCP Next note; this piece: two fleets, AMD in neither.

> “Fifteen percent of $1.4 trillion is $210 billion, so Baird’s share is being applied to something nearer $980 billion. The most bullish note on the street is implicitly applying AMD’s share to an addressable pool roughly 30% below AMD’s headline TAM.”

> “Against 1.65 billion shares, full vesting takes roughly 16% off per-share earnings, which puts that same 45 times nearer $535 than $640.”

> “What would move me is an independent inference benchmark that tests NVIDIA’s compression claim against AMD’s dense flops.”

> “AMD may win. I still think NVIDIA is the cheaper way to own the outcome.”
