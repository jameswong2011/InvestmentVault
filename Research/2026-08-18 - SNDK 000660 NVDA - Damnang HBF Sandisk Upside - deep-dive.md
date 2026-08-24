---
date: 2026-08-18
tags: [research, NAND, Memory, SNDK, 000660, NVDA, META, HBF]
sector: NAND Memory & Storage
ticker: SNDK
source: 'https://damnang2.substack.com/p/will-hbf-create-upside-for-sandisk'
source_type: deep-dive
propagated_to: [SNDK, 000660, NVDA]
---

# Will HBF Create Upside for Sandisk? — Damnang

## Thesis Delta
Consensus still prices [[Theses/SNDK - SanDisk]] Insight #1 as a 2027 TAM-creation call option — on-package NAND filling Jensen's "missing middle," SK hynix + OCP killing Betamax, NVIDIA Rubin as the swing customer — and the live book holds SNDK in the Low sleeve (<3.5%) with FY30 HBF still modeled as a small/zero earnings line (July deepen: ~9–10% of 2030 revenue in the base case, not a 2026 print). Investor Day's internal 4 HBF-only vs 8 HBM-only token-throughput demo and the "8x capital efficiency / 2x GPU efficiency" claim are the tape the market is extrapolating into share-price optionality. This 18 August 2026 Damnang bottom-up implies a different map. The commercially realistic early form is mixed HBF (+HBM) with read-dominant weights in HBF and write-heavy KV cache remaining in HBM; HBF Only is judged low-applicability for conversational inference because Li et al. (arXiv:2608.11668, 12 Aug 2026) find write traffic exceeding read across every trace, thermal limits before peak bandwidth, and TLC wear faster than the SSD pool being replaced. Google, not NVIDIA, is ~89% of the $0.95B base-case HBF revenue ($0.84B of $0.95B); NVIDIA's disclosed Rubin stack (288GB HBM4, 22TB/s, Dynamo, Groq 3 LPX SRAM, NVLink Fusion) gives it little incentive to put HBF in a general-purpose GPU baseline. Direct revenue even at the $4.22B scale case (~21% of FY2026 $20.25B) is not the re-rate; second-order mix, 3–4× wafer absorption (Bernstein/Newman, not guidance), and NBM-style cyclicality are. Hypothesis: the Low sleeve is consistent with "option not probability"; the option's strike is Google/Meta attach plus packaging yield, not Rubin HBF confirmation. Conviction-trigger touches: [[Theses/SNDK - SanDisk]] has no registered Conviction Triggers (structural gap). [[Theses/000660 - SK Hynix]] → HIGH/LOW/CLOSE are Rubin/CXMT/Namics handles — HBF does not fire them; Q4 (hyperscaler production by 2027 vs slip to 2028+) is evidence-touched toward Google/Meta as the path, not answered (no production, no MTIA SKU). [[Theses/NVDA - Nvidia]] has no Conviction Triggers section.

## Summary
Damnang's argument is that HBF's name produces a technical misunderstanding, and that Investor Day did not sufficiently explain KV-cache write burden, prefetch, heat, or endurance. The piece is an author-built four-step commercialization test (not a primary BOM): (1) which of four Sandisk architectures is technically realistic, (2) whether HBF lowers system TCO versus LPDDR/CXL/SSD despite packaging cost, (3) which operators have incentive to evaluate it, (4) a Google/Meta bottom-up of Sandisk direct HBF revenue plus second-order mix, wafer absorption, and cyclicality. Scope is disclosed public materials plus identified analytical assumptions (k, data-placement policy, customer attach, stack ASP, Sandisk supply share). Live WebFetch of the URL returned a paid teaser; this note is from the complete Gmail body (id 1a015b16d6d54444, sender damnang2@substack.com, 2026-08-18). FIG. 06/07 cost charts are scenario assumptions, not a production BOM; the author says they cannot support "HBF is cheaper than LPDDR."

Section 1's load-bearing claim is data-type, not capacity. HBF Only puts weights and KV on flash with no HBM buffer; the ID demo (4 HBF-only accelerators matching 8 HBM-only on tokens/s) used 192GB HBM and BF16 to get 960GB of weights for a 480B model and eight accelerators once KV was included. FP8 cuts those weights to 480GB; in the 288GB-per-GPU basis this report uses, weights fit in two accelerators' combined HBM. The capacity shortfall the presentation assumes is therefore weaker than stated, without implying two accelerators serve the whole footprint. The binding constraint is writes: KV is written every token and discarded at session end. Li et al. conclude that without SSD-class write management, storing transient KV directly in HBF is not sustainable. Son et al. (arXiv:2608.13868) and Kim et al. (arXiv:2608.14333, 1.94x throughput from splitting immutable weights and mutable KV onto two parallel paths) are simulations that both point to data-type and path separation mattering more than capacity. HBF (+HBM) with weights in HBF and KV in HBM is the author's base case. At assumed k=4, node capacity rises 288GB → 2.2TB while bandwidth falls 22TB/s → 17.4TB/s. Conditions: weights in the hundreds of GB or more, and software that can prefetch around microsecond NAND reads. HBM/HBF Cached still writes KV to flash (fit is high-hit-rate repeated context, not general chat). Disaggregated puts HBF on decode for weights plus KV; decode weights fit, KV still needs write management, and the design must beat non-HBF disaggregation (GDDR7 prefill, SRAM-rack decode) on cost per token.

Section 2 rejects "NAND is cheap therefore HBF wins." SK hynix and [[Theses/MU - Micron Technology]] have disclosed SOCAMM2 modules up to 256GB (up to 2TB per CPU); Micron positions SOCAMM2 as a KV-offload tier from HBM. TB-class capacity therefore exists off-package. HBF's differentiation is location: package-local / near-xPU capacity beyond HBM, not a unique TB answer. Sandisk's 8–16× HBM capacity at similar cost is a vendor target versus HBM, not a demonstrated LPDDR price advantage. SK hynix 256GB SOCAMM2 uses cost-effective wire bonding; HBF needs CBA, multi-die stacking, high-speed I/O, thermal and reliability management. Assembly cost, KGD yield, stack yield, test cost and ASP are undisclosed. Commercial test: (i) xPU-adjacent shortage persists after larger HBM, FP8/FP4, MoE and KV optimization; (ii) adding HBF actually cuts accelerators or data movement rather than swapping HBM for lower bandwidth; (iii) 512GB-class package yield reaches commercial levels. If yield is low, NAND's cell-cost advantage is absorbed in the back end.

Section 3 splits customers by system control, not by UCIe membership (NVIDIA, Google and Meta are all UCIe promoters). Google and Tenstorrent are the two external members named in the 3 August Sandisk/SK hynix standardization announcement. Google designs TPUs and runs XLA, JAX and vLLM; Ironwood is an inference TPU with memory capacity and bandwidth as primary variables (max 9,216-chip Superpod). Participation is system-design validation, not a purchase order; the coherent case is HBF as a secondary near-compute tier on a future TPU or inference derivative, not HBM replacement. Meta's 2026 MTIA roadmap: four generations in two years, recommendation/ranking into GenAI inference, hundreds of thousands of units in its own services, Broadcom custom-silicon partnership with >1GW initial commitment and a planned multi-gigawatt rollout. Meta is structurally able to validate HBF on repeated-read embeddings and reference data inside its own PyTorch stack. The August 3 announcement does not name Meta; Investor Day remarks and reporting are the involvement level; public information does not confirm HBF in MTIA. Tenstorrent's reason to validate is the open chiplet/IP strategy, not captive volume. NVIDIA Rubin: up to 288GB HBM4 and 22TB/s; decode described as memory-subsystem constrained. Dynamo splits prefill/decode and moves KV between GPU memories; Vera Rubin pairs Groq 3 LPX (128GB SRAM, 12TB DDR5) for low-latency decode; NVLink Fusion brings hyperscaler custom XPUs into NVIDIA racks. Author judgment: baseline Rubin memory stays HBM4-centric on the disclosed roadmap. Realistic NVIDIA paths are inference-specific derivatives, semi-custom XPUs, or a separate expansion tier — still requiring 512GB HBF to beat HBM4+SRAM+disaggregation on cost/token, power, or rack density, including token-to-token latency and sustained-KV thermal/endurance data.

Section 4's equation is accelerator unit pool × HBF attach rate × stacks per accelerator × stack ASP × Sandisk supply share. Annualized Sandisk HBF revenue: $0.09B initial, $0.95B base, $4.22B scale. Base is 89% Google. Scale is ~21% of FY2026 $20.25B and requires 30% Google attach, four stacks per accelerator, and meaningful concurrent Meta adoption. FT/Morgan Stanley TPU volume estimates cited: 5 million units in 2027 and 7 million in 2028 — inputs to the pool, not Sandisk guidance. A limited Google design win cannot explain large share-price upside. Second path: FY2026 datacenter revenue +437% YoY; if HBF converts commodity NAND bits into high-value xPU-adjacent AI memory, mix can exceed the HBF line. Bernstein's Mark Newman: HBF may need ~3–4× the wafer capacity of commodity NAND for the same exabytes (estimate, not guidance); at millions of accelerators that would tighten NAND slack and indirectly price other datacenter NAND. Third path: NBM already puts ~50% of FY2027 bits and about two thirds of FY2028 bits under committed volume, minimum financial guarantees and structured pricing. Recurring HBF design wins under similar multi-year structures could make HBF look like accelerator-tied revenue rather than another NAND SKU — earnings-quality (mix + tighter supply + lower cyclicality) before multiple. If attach stays limited, or yield/ASP disappoint, the re-rating case does not hold.

## Framework / Mental Model
**Name:** Four HBF configurations crossed with a TCO test and a system-control adoption screen.

**Configuration axis (what data sits in HBF, and whether HBM remains):**

| Config | HBM remains? | What HBF holds | Write load on flash | Author applicability |
|---|---|---|---|---|
| HBF Only | No; every stack site is HBF | Weights + KV | Continuous KV writes every token; no HBM cache/write buffer | Low for general conversational inference; batch-style limited-KV / repeated-weight reads more plausible |
| HBF (+HBM) | Yes; k of N sites are HBF | Base-case assumption: weights in HBF, KV in HBM (k undisclosed by company) | Weights written at load, then mostly read | Most realistic on disclosed information; needs hundreds-of-GB weights and prefetch that hides µs NAND reads |
| HBM/HBF Cached | HBM as front-end cache | Weights + KV in HBF | KV still lands in flash; access frequency falls only if hit rate is high | Document QA / repeated-codebase; falls in session-unique chat |
| Disaggregated | Prefill uses GDDR in the published diagram | Decode-side HBF: decode weights + KV | Decode weights read-dominant; KV still written every token | Must beat non-HBF disaggregation (GDDR7 prefill, SRAM-rack decode) on cost/token or system efficiency |

**How applied.** Classify any HBF headline on data placement before treating "capacity" as the product. Read-dominant weights are a light endurance burden and match NAND page-level sequential reads; KV is write-heavy, thermal-limited before bandwidth (Li et al.), and TLC-wear exposed. Optimal k trades HBF capacity against HBM capacity and bandwidth (worked example at k=4: 288GB → 2.2TB; 22TB/s → 17.4TB/s).

**TCO test (not a bit-cost test):** HBF is not shown to be cheaper than LPDDR. Differentiation is near-xPU capacity beyond HBM at high read bandwidth, inside HBM-like physical constraints (CBA, multi-die stack, high-speed I/O, thermal/reliability). Alternatives already in customers' hands: more HBM, LPDDR/SOCAMM2, CXL, SSD tiering, software (FP8/FP4, MoE, KV optimization, Dynamo). Three commercial conditions: residual xPU-adjacent shortage after those; measured cut in accelerators or data movement (not a bandwidth-down swap); commercial yield on 512GB-class stacks. Fail any one and NAND cell cost does not reach finished cost or system TCO.

**Adoption screen (system control vs merchant GPU):** HBF (+HBM) is a compiler/prefetch/package/scheduling co-design, not a DIMM swap. Vertically integrated ASIC operators (Google TPU + XLA/JAX/vLLM; Meta MTIA + PyTorch; Tenstorrent open chiplet/IP) can tune placement to one inference pattern. A general-purpose GPU that must serve training, post-training, dense, MoE and agentic workloads pays a higher incremental-benefit bar; NVIDIA already has HBM4, NVLink, Dynamo and LPX SRAM on the disclosed roadmap. UCIe promoter membership is not the constraint.

**Revenue identity (direct) and three share-price paths:** Direct = unit pool × attach × stacks/accelerator × stack ASP × Sandisk share. Path 1: that line ($0.09B / $0.95B / $4.22B). Path 2: mix + wafer absorption (Bernstein 3–4× wafers per EB vs commodity NAND). Path 3: NBM-like contracted structure changing cyclicality before the multiple. Methodology constraint: k, placement policy, attach, ASP and share are analytical assumptions; Google consortium membership ≠ PO; Meta ID remarks ≠ MTIA HBF SKU; FIG. 06/07 are sensitivity charts.

## Evidence

### Investor Day demo and author k=4 node

| Item | Figure | Tag |
|---|---|---|
| ID internal demo | 4 HBF-only accelerators matched 8 HBM-only on tokens/s | [1×: Sandisk ID via Damnang] |
| Company efficiency claim | 8x capital efficiency; 2x GPU efficiency | [1×: Sandisk ID via Damnang] |
| ID comparison premises | 192GB HBM/GPU; BF16; 960GB weights for a 480B model; 8 accelerators once KV included | [1×: Sandisk ID via Damnang] |
| FP8 restatement (author) | same weights 480GB | [est.: Damnang] |
| Author GPU basis | 288GB HBM/GPU; weights fit in combined HBM of 2 accelerators | [est.: Damnang] |
| HBF (+HBM) at k=4 | capacity 288GB → 2.2TB; bandwidth 22TB/s → 17.4TB/s | [est.: Damnang; k undisclosed by company] |
| Weight-size condition | hundreds of GB or more, else HBM can hold them | [1×: Damnang] |
| Gen-1 HBF spec (fact sheet) | 512GB/stack; 1.6TB/s read | [IR: Sandisk HBF fact sheet via Damnang] |
| vs HBM capacity (vendor target) | 8 to 16 times HBM capacity at similar cost | [IR: Sandisk via Damnang] |

### KV / endurance literature (Aug 2026)

| Item | Figure | Tag |
|---|---|---|
| Li et al. 2026-08-12 | arXiv:2608.11668; 4 production traces; 5 dense and MoE models | [1×: Li et al. via Damnang] |
| Li et al. traffic | write traffic exceeded read traffic across every trace | [1×: Li et al.] |
| Li et al. thermal | thermal limits reached before peak bandwidth | [1×: Li et al.] |
| Li et al. endurance | TLC wore out faster than the SSD pool being replaced; without SSD-class write management, transient KV in HBF not sustainable | [1×: Li et al.] |
| Son et al. 2026-08-14 | arXiv:2608.13868; HBF can raise batch size/throughput and cut GPU count if read BW ≈ HBM and endurance improves substantially | [1×: Son et al.] |
| Kim et al. 2026-08-14 | arXiv:2608.14333; 1.94x throughput from splitting immutable weights vs mutable KV on two parallel paths (GPU↔HBF and HBF→HBM→GPU) | [1×: Kim et al.] |
| ID write policy | endurance limits and KV management policy not disclosed | [1×: Damnang] |

### Alternatives and cost

| Item | Figure | Tag |
|---|---|---|
| SOCAMM2 capacity | up to 256GB modules; multiple modules → TB-class on CPU/system side; up to 2TB per CPU | [1×: Micron / SK hynix via Damnang] |
| Micron SOCAMM2 positioning | KV-cache offload from HBM | [1×: Micron via Damnang] |
| SK hynix 256GB SOCAMM2 backend | cost-effective wire bonding stack | [1×: SK hynix via Damnang] |
| HBF vs LPDDR finished cost | no public basis for quantitative comparison (ASP, KGD, stack yield, test undisclosed) | [1×: Damnang] |
| FIG. 06 / FIG. 07 | scenario assumptions from prior analysis, not a production BOM; cannot conclude HBF cheaper than LPDDR | [est.: Damnang] |

### Customer / platform facts

| Item | Figure | Tag |
|---|---|---|
| HBF standardization members (Aug 3) | Google and Tenstorrent as consortium members | [IR: Sandisk / SK hynix 2026-08-03 via Damnang] |
| Meta consortium status | named at Investor Day remarks / reporting, not in the Aug 3 announcement; HBF-in-MTIA not confirmed | [1×: Damnang] |
| Google Ironwood | inference-oriented TPU; max 9,216-chip Superpod | [1×: Google via Damnang] |
| FT / Morgan Stanley TPU volumes | 5 million units in 2027; 7 million in 2028 | [1×: FT / MS via Damnang] |
| Meta MTIA 2026 | four generations in two years; rec/ranking → GenAI inference; hundreds of thousands of units in own services | [1×: Meta via Damnang] |
| Meta / Broadcom custom silicon | >1GW initial commitment; planned multi-GW rollout | [1×: Meta / Broadcom via Damnang] |
| NVIDIA Rubin | up to 288GB HBM4; 22TB/s memory bandwidth | [1×: NVIDIA via Damnang] |
| Groq 3 LPX rack | 128GB SRAM; 12TB DDR5; paired with Rubin for low-latency decode | [1×: NVIDIA via Damnang] |
| Dynamo | disaggregated prefill/decode; KV transferred between GPU memories | [1×: NVIDIA via Damnang] |
| NVLink Fusion | hyperscaler custom XPUs into NVIDIA rack architecture | [1×: NVIDIA via Damnang] |
| UCIe promoters | includes NVIDIA, Google, and Meta | [1×: UCIe via Damnang] |
| Author NVIDIA judgment | incentive to put HBF in baseline general-purpose GPU memory tier is low; Rubin baseline likely remains HBM4-centric | [1×: Damnang] |

### Sandisk HBF revenue model and second-order

| Item | Figure | Tag |
|---|---|---|
| Direct-revenue identity | unit pool × attach × stacks/accelerator × stack ASP × Sandisk supply share | [est.: Damnang] |
| Initial adoption | ~$0.09B annualized Sandisk HBF revenue | [est.: Damnang] |
| Base case | ~$0.95B; ~$0.84B (89%) from Google | [est.: Damnang] |
| Scale case | ~$4.22B; ~21% of FY2026 revenue $20.25B | [est.: Damnang]; FY2026 rev [IR: Sandisk Q4] |
| Scale-case premises | 30% Google attach; 4 stacks per accelerator; meaningful concurrent Meta adoption | [est.: Damnang] |
| FY2026 datacenter | +437% YoY | [IR: Sandisk Q4 via Damnang] |
| Bernstein wafer intensity | ~3–4× wafer capacity vs commodity NAND for the same exabytes; estimate, not Sandisk guidance | [1×: Bernstein / Newman via MarketWatch / Damnang] |
| NBM coverage | ~50% of FY2027 bits; about two thirds of FY2028 bits under committed volume, minimum financial guarantees, structured pricing | [IR: Sandisk ID via Damnang] |
| MoE examples (context, not HBF demand) | Kimi K3: 896 experts, 16 selected/token; Qwen3 Coder 480B A35B: 160 experts, 8 selected/token | [1×: Moonshot / Qwen via Damnang] |

Live-portfolio context (not Damnang): [[Live Portfolio]] holds [[Theses/SNDK - SanDisk]] in the Low sleeve (<3.5%). [[Theses/000660 - SK Hynix]] is the HBF co-developer option inside the book. [[Theses/NVDA - Nvidia]] is the article's low-incentive platform, not a new HBF customer.

## Contradiction Check
**Supports** [[Theses/SNDK - SanDisk]] Insight #1 only as TAM-creation optionality, not as a 2026 earnings line or a Rubin-led probability. The $0.95B base case is the same order of magnitude as the July deepen's 2027 bear/base ($0.15–0.25B) stepping toward 2028, and the $4.22B scale case sits near the deepen's 2030 base (~$3.3B) pulled forward — but only if 30% Google attach, four stacks, and concurrent Meta all hit. **Challenges the Investor Day 8x/2x efficiency tape and the HBF Only commercial path.** Vault Outstanding Question #1 (Optane graveyard; NVIDIA commit; hyperscaler re-architecture) is the question this source actually answers, and the answer is split: hyperscalers that own ASICs (Google, structurally Meta) are the evaluation set; NVIDIA commit to on-package HBF on Rubin is judged unlikely on the disclosed roadmap. **Supports** SNDK Industry Context finding #2 (NVIDIA is the swing factor and the mid-2026 signal is adverse — ICMS/GIDS/BlueField route-around) and finding #3 (endurance–density–cost trilemma; ~100K-cycle / read-mostly weights). Li et al. is independent corroboration that KV-in-HBF is the unsustainable config; the author's HBF (+HBM) base case is the same "weights not hot KV" confinement the thesis already named. **Supports** Risk #1 (commercialization / NVIDIA adoption) rather than retiring it: packaging yield and realized ASP are still undisclosed, and NVIDIA baseline HBM4 is explicit. **Does not retire** Bear "HBF execution risk" or Risk #4 (Samsung entry) — Samsung is not analyzed here. **Touches** the unwritten SNDK Conviction Triggers only on the suggested HIGH (NBM coverage >50% of FY27 bits): the source restates ~50% FY27 and ~2/3 FY28 under NBM, which is the coverage print, not a new crossing. **Does not** change SNDK conviction or Low-sleeve status.

**Supports** [[Theses/000660 - SK Hynix]] Insight #3 (unpriced HBF option; OCP workstream) and Bull pillar 3 (HBF monetization at OCP-standard deployment 2027+) with a customer-mix correction: the option's first cash is Google/Meta attach, not "Nvidia's post-Rubin architecture selects HBF." SK hynix remains co-standardizer and HBM supplier to the mixed config (KV stays in HBM at k=4). Outstanding Question Q4 (hyperscaler production by 2027 vs 2028+) is not answered; consortium participation and MTIA roadmap are leading indicators, not qualification. **Does not fire** 000660 → HIGH (Rubin ≥60% + HBM4E sole-source + Kinex 16-Hi + Namics ≥2028), → LOW (Samsung >35% Rubin + HBM price −10%), or → CLOSE (CXMT qualified HBM + Samsung HB yield 70% at 16-Hi). HBF is off those handles.

**Supports the vault's NVIDIA route-around, in NVIDIA's own words as used here.** [[Theses/NVDA - Nvidia]] already logs BlueField-4 / ICMS / GIDS as validating NAND-as-AI-memory while routing around HBF-on-package; Dynamo, Groq 3 LPX SRAM, and NVLink Fusion are the serving-side substitutes this source adds. The Catalyst "NVIDIA Rubin architecture reveal / HBF integration" on the SNDK thesis is the item this piece marks as low-probability on current disclosure. No NVDA Conviction Triggers to test. Related: [[Theses/META - Meta]] MTIA/Broadcom >1GW is customer-side capacity, not an HBF SKU. [[Theses/MU - Micron Technology]] SOCAMM2 is named as the off-package KV alternative; that is location competition with HBF, not an HBF standard seat. [[Theses/285A - Kioxia]] is not in this source (vault already has Kioxia declining HBF for XL-Flash; do not import that as Damnang). [[Theses/AVGO - Broadcom]] appears only as Meta's custom-silicon partner (>1GW), not as an HBF beneficiary.

**Does not** change conviction or status on SNDK, 000660, or NVDA. **Does not** write to the vault.

Mental-model triggers for a later `/sync` (ingest identifies only): [[Mental Models/Lens - Value Layer Monopoly]] §1 interface/standard control — HBF is an open OCP/UCIe tier the GPU platform can route around (NVIDIA HBM4+Dynamo+LPX); weak layer-monopoly fit, already the SNDK deepen's finding #1. [[Mental Models/Industry - Semiconductors]] #13 classification — NBM (~50% FY27 / ~2/3 FY28 bits) plus hypothetical recurring HBF design wins are the semi-cyclical argument; the $0.95B base case does not reclassify SNDK off the NAND cycle. [[Mental Models/Generalist - Overview]] [G-13] mispriced operating lever — mix, 3–4× wafer absorption, and cyclicality, not the HBF revenue line. [[Mental Models/Industry - Semiconductors]] Optane analog / endurance — Li et al. is the named-observable on KV-in-flash unsustainability.

## Source Excerpts
> "The most realistic early form of HBF is not a full replacement for HBM but a mixed HBF (+HBM) configuration. Placing read-dominant, high-capacity data such as model weights in HBF while keeping the KV cache, which requires continuous writes and low latency, in HBM aligns best with HBF’s physical characteristics."

> "NVIDIA, by contrast, has little incentive on its currently disclosed roadmap to place HBF in the baseline memory tier of a general-purpose GPU."

> "In the bottom-up model, the annualized HBF revenue opportunity is roughly $0.95B in the base case and about $4.2B in the scale case."

> "In internal testing presented at Investor Day, four HBF-only accelerators matched the token-per-second throughput of eight HBM-only accelerators. … The company cited this as 8x capital efficiency and 2x GPU efficiency."

> "The presentation used 192GB of HBM per GPU and BF16 to derive 960GB of weights for a 480B model, and concluded that eight accelerators were required once KV cache was included. Applying FP8 reduces the same weights to 480GB, and in the 288GB-per-GPU environment this report uses as its basis, the weights themselves fit within the combined HBM capacity of two accelerators."

> "Write traffic exceeded read traffic across every trace, thermal limits were reached before peak bandwidth, and TLC configurations wore out faster than the SSD pool being replaced. The conclusion is that without SSD-class write management, storing transient KV cache directly in HBF is not sustainable."

> "Under this report’s assumptions, at k=4 node memory capacity rises from 288GB to 2.2TB while total bandwidth falls from 22TB/s to 17.4TB/s."

> "Public materials give no basis for concluding that HBF is cheaper than LPDDR."

> "Of the roughly $0.95B base case, about $0.84B, or 89%, comes from Google. The $4.22B scale case equals about 21% of Sandisk’s FY2026 revenue of $20.25B, but it requires a 30% Google attach rate, four stacks per accelerator and meaningful concurrent adoption at Meta."

> "Bernstein’s Mark Newman has estimated that HBF may require roughly three to four times the wafer capacity of commodity NAND to produce the same exabytes. … The three-to-four-times figure is an estimate, not Sandisk guidance."

> "Sandisk states that its NBM contracts place roughly 50% of FY2027 bits and about two thirds of FY2028 bits under committed volume, minimum financial guarantees and a structured pricing mechanism."

> "If the currently disclosed roadmap holds, I judge that the baseline memory tier of general-purpose Rubin GPUs is likely to remain HBM4-centric."
