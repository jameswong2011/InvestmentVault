---
title: "Will HBF Create Upside for Sandisk?"
source: Damnang
url: "https://damnang2.substack.com/p/will-hbf-create-upside-for-sandisk"
date: 2026-08-18
publication: Damnang
gmail_id: 1a015b16d6d54444
tags: [research, email-backfill, Damnang, SNDK, 000660, NVDA, HBF, META]
source_type: web-clip
sender: damnang2@substack.com
gmail_full: true
---
# Will HBF Create Upside for Sandisk?

**Pub:** Damnang (Damnang’s Substack)
**URL:** https://damnang2.substack.com/p/will-hbf-create-upside-for-sandisk
**Date:** 2026-08-18
**Sender:** damnang2@substack.com
**Gmail id:** 1a015b16d6d54444
**Email timestamp (Gmail):** 2026-08-18T16:24:36Z (2026-08-19 00:24 CST)
**Subtitle:** Feasibility and adoption across four architectures
**Note:** Live WebFetch of the URL returned a paid-teaser page. This file is the full Gmail-quality body (not a teaser). Image-only figures (FIG. 06 / FIG. 07) are described in the text as scenario charts, not transcribed as a BOM.

## ARTICLE TAKEAWAYS

The most realistic early form of HBF is not a full replacement for HBM but a mixed HBF (+HBM) configuration. Placing read-dominant, high-capacity data such as model weights in HBF while keeping the KV cache, which requires continuous writes and low latency, in HBM aligns best with HBF’s physical characteristics.

HBF’s economics are decided by the system savings that near-compute capacity creates, rather than by NAND’s low bit cost alone. LPDDR, CXL and SSD are valid alternatives, so HBF must reduce additional accelerators and data movement enough to justify its more complex packaging and yield burden.

Customer adoption depends on how much of the system a given operator controls. Google formally participated in HBF standardization and can co-optimize its own TPUs and software, which makes it the most important potential customer. Meta is also extending MTIA into an inference-first full stack, giving it strong structural fit. NVIDIA, by contrast, has little incentive on its currently disclosed roadmap to place HBF in the baseline memory tier of a general-purpose GPU.

In the bottom-up model, the annualized HBF revenue opportunity is roughly $0.95B in the base case and about $4.2B in the scale case. The larger upside, however, may come from second-order effects alongside direct revenue. If repeated hyperscaler design wins expand the high-value AI memory mix, raise NAND wafer demand and increase the share of long-term contracted revenue, they could affect both Sandisk’s earnings power and its cyclicality.

---

HBF's name leads many investors into technical misunderstanding. The technology itself also remains contested, on access latency, endurance under repeated writes, heat and packaging yield.

Earlier this year I reviewed the H3 paper published by SK hynix on what HBF means technically and where its limits are.

This article analyzes the HBF that Sandisk presented at its Investor Day and in related public materials, and estimates bottom up how much the technology could move Sandisk’s share price if it reaches commercial deployment.

The report judges HBF’s commercialization prospects in four steps.

Section 1 compares the four architectures Sandisk presented in terms of data placement, write load and latency, and identifies which configuration is technically most realistic. It focuses on what the presentation did not sufficiently explain, namely KV cache write burden, prefetch, heat and endurance, and examines the conditions under which each architecture holds.

Section 2 examines HBF’s competing technologies, asks why HBF is needed relative to them, and tests whether it can lower system TCO despite its complex packaging cost.

Section 3 compares the platform structures of Google, Meta, Tenstorrent and NVIDIA, and analyzes technically why Google and Meta have a relatively strong incentive to evaluate HBF while NVIDIA is judged unlikely to.

Finally, Section 4 uses accelerator unit pools, HBF attach rates and stacks per accelerator at Google and Meta to derive Sandisk’s direct HBF revenue bottom up, and separates the second-order effects on product mix, NAND wafer absorption and revenue structure that could matter more to the share price.

For investors who have wondered how HBF actually works and what it could mean for Sandisk’s revenue and share price, this article is written for you.

## Disclaimer

This document is prepared for information purposes using public information and the author’s own analysis, and does not constitute a recommendation to buy or sell any security. Product specifications, participating companies and public roadmaps rely on disclosures from the companies and standards bodies involved. Items that have not been disclosed, including HBF and HBM data placement, cost structure and customer-level adoption likelihood, are identified as analytical assumptions or inference. Specifications, commercialization timing and customer adoption may change, and responsibility for investment decisions and their outcomes rests with the investor.

## CONTENTS

- Technical feasibility: comparing the four configurations
- Economics: alternatives and capacity per package
- Customer adoption
- HBF’s economic impact: a Google and Meta bottom-up model

---

## 1. Technical feasibility: comparing the four configurations

**SECTION 1 TAKEAWAY**

On currently disclosed information, HBF (+HBM) is the most realistic configuration. Placing model weights in HBF and the write-heavy KV cache in HBM uses HBF’s capacity density while limiting the repeated-write burden on flash. HBF Only faces substantial KV cache write, thermal and endurance constraints, while Cached and Disaggregated require evidence on cache policy and token-to-token latency respectively.

The four configurations differ in what data HBF handles and whether HBM remains. HBF Only fills every stack site with HBF and stores both weights and KV cache there. HBF (+HBM) replaces only part of the stacks, splitting the roles with HBM.

HBM/HBF Cached places HBM as a front-end cache and stores weights and KV cache in HBF. Disaggregated separates prefill from decode and puts HBF on the decode accelerator to hold decode weights and KV cache.

The technical assessment that follows uses these data placement differences as its basis.

The first question is what role HBF can play in real inference workloads.

The four configurations differ in the data HBF handles and whether HBM remains. The comparison therefore uses write load, access pattern and latency sensitivity on a common basis rather than capacity alone.

### 1.1 HBF Only

HBF Only fills every stack site with HBF and uses no HBM. Because both model weights and KV cache reside in HBF, the configuration gains capacity but must also absorb the continuous write load of the KV cache directly.

In internal testing presented at Investor Day, four HBF-only accelerators matched the token-per-second throughput of eight HBM-only accelerators.

By the company’s explanation, the performance gap arises when HBM runs short of KV cache capacity, pushing some data into system memory and lowering GPU utilization. HBF relieves that capacity constraint by providing larger on-package capacity.

The company cited this as 8x capital efficiency and 2x GPU efficiency. The comparison is internal, however, and key premises such as GPU capacity and numeric precision may differ from real deployments.

The case for HBF Only therefore has to be verified in two steps.

First, whether the same on-package capacity shortfall still occurs on the latest accelerators and at lower inference precision.

Second, whether HBF can absorb the KV cache write load along with its thermal and endurance requirements.

The first issue is the comparison conditions.

The presentation used 192GB of HBM per GPU and BF16 to derive 960GB of weights for a 480B model, and concluded that eight accelerators were required once KV cache was included. Applying FP8 reduces the same weights to 480GB, and in the 288GB-per-GPU environment this report uses as its basis, the weights themselves fit within the combined HBM capacity of two accelerators.

The HBM left after loading weights can serve KV cache and runtime, though the actual headroom depends on KV cache, activation and runtime configuration. The capacity shortfall the presentation assumes may therefore be weaker than stated, but that does not mean two accelerators are sufficient for the entire serving footprint.

The second issue is the write behavior of the KV cache.

In HBF Only, KV cache is written directly to HBF. New data is written on every token and discarded when the session ends, so unlike read-dominant model weights it produces a continuous write load. NAND flash carries cell endurance limits under repeated writes. Any structure that writes KV cache directly to HBF must therefore treat write lifetime and thermal management as design variables.

The Investor Day materials and keynote disclosed to date do not specify those limits or the management policy.

Published on August 12, 2026, Li et al. (2026, arXiv:2608.11668) evaluated HBF-based KV serving using four production traces and five dense and MoE models. Write traffic exceeded read traffic across every trace, thermal limits were reached before peak bandwidth, and TLC configurations wore out faster than the SSD pool being replaced. The conclusion is that without SSD-class write management, storing transient KV cache directly in HBF is not sustainable. HBF Only has no HBM cache or write buffer, so it is the most exposed to that constraint.

Follow-up studies released on August 14 assess HBF in more conditional terms.

Son et al. (2026, arXiv:2608.13868) finds that HBF can raise batch size and throughput and reduce GPU count, but only on the premise of read bandwidth close to HBM and substantial endurance improvement.

Kim et al. (2026, arXiv:2608.14333) reports 1.94x throughput from a structure that separates immutable weights from mutable KV cache and supplies them over two parallel paths. Both are simulations, and both point to data type and movement path separation mattering more than capacity.

Taken together, I judge HBF Only to have low applicability to general conversational inference.

The more plausible fit is batch-style workloads that generate limited KV cache while repeatedly reading large weights or reference data. Where session counts and context lengths keep growing, KV write load rises and the applicable range narrows without additional write-management technology.

### 1.2 HBF (+HBM)

HBF (+HBM) configures k of N stack sites as HBF and keeps the rest as HBM. The essential feature is that data placement between HBF and HBM can be split according to workload characteristics.

This article takes as its base case a configuration that places model weights in HBF and KV cache in HBM. That separates the continuous KV cache write load, the largest constraint in HBF Only, from HBF.

The company has not disclosed the value of k, the data placement criteria between HBF and HBM, or the software policy. The assessment below therefore rests on the analytical assumption that weights sit in HBF and KV cache remains in HBM.

That assumption aligns reasonably well with HBF’s physical characteristics and the access profile of model weights.

First, model weights are written at load time and thereafter mostly read during inference, so the endurance burden from repeated writes is limited.

Second, weight access is dominated by large sequential reads at layer granularity, which matches NAND’s page-level read behavior comparatively well. It wastes less of each page read than small random access would.

Third, where the next required weight location is predictable, prefetch can overlap flash’s microsecond-class read latency with computation. Actual performance depends on prefetch accuracy and software scheduling.

The study cited above likewise assessed read-dominant model weights as a comparatively good fit for HBF, provided that placement is selective and that write budgeting and thermal control are in place.

Under this report’s assumptions, at k=4 node memory capacity rises from 288GB to 2.2TB while total bandwidth falls from 22TB/s to 17.4TB/s. As k increases, HBF capacity expands but HBM capacity and bandwidth decline.

The optimal k therefore depends jointly on weight size, KV cache demand and the bandwidth loss that can be tolerated.

HBF (+HBM) applies best under two conditions.

First, model weights must be large enough, in the hundreds of GB or more, that HBM alone cannot hold them. Second, data placement and prefetch must be optimizable alongside the accelerator software. The remaining item to verify is whether throughput and latency hold at target levels once prefetch is applied.

### 1.3 HBM/HBF Cached

HBM/HBF Cached uses HBM as a low-latency cache tier and stores both model weights and KV cache in HBF. It reduces the frequency of HBF access relative to HBF Only, but the write constraint persists as long as KV data lands in HBF.

This configuration favors services where identical or similar contexts are referenced repeatedly and a high cache hit rate can be sustained. Document-grounded question answering and workloads that repeatedly reference the same codebase are plausible candidates. In general conversational services where context differs sharply by session, HBF access and write load rise and applicability falls.

### 1.4 Disaggregated

The Disaggregated configuration separates prefill and decode accelerators. In the published diagram, GDDR is used on the prefill side while decode-side HBF stores decode weights and KV cache.

The assessment differs by data type. Decode weights are read-dominant after the initial load and fit HBF well. KV cache still requires write management, since new K and V are written on every token even during decode.

Separate from technical feasibility, the economics against competing architectures also need checking. The comparison cases in this report already include disaggregated designs that use no HBF, such as a GDDR7-based prefill accelerator and an SRAM rack for decode. For an HBF-based disaggregated design to be adopted, it must demonstrate an advantage in cost per token or system efficiency over those designs.

### 1.5 Assessment across the four configurations

The relative appeal of the four configurations comes down to what data sits in HBF and how much writing that data generates. Placing read-dominant model weights in HBF carries a light endurance burden, while writing KV cache directly to HBF adds write management and thermal control on top.

The following sections provide an in depth analysis of the HBF architecture.

The analysis examines alternative technologies that could compete with HBF, the technical factors that could nevertheless support HBF adoption, the types of customers most likely to deploy it, and whether NVIDIA could become one of them.

Finally, a proprietary analytical model is used to assess how HBF commercialization could affect Sandisk’s share price.

---

## 2. Why HBF: not price, but near-compute capacity and system TCO

**SECTION 2 TAKEAWAY**

Public materials give no basis for concluding that HBF is cheaper than LPDDR. HBF’s differentiation lies in delivering far more capacity than HBM, at high read bandwidth, within the limited space next to the xPU. That structure requires complex packaging with CBA, multi-die stacking, high-speed I/O and thermal and reliability management. HBF’s economics must therefore be tested not on NAND’s low bit cost but on actual packaging yield, finished-product cost, and system TCO including how much it reduces additional accelerators and data movement.

Technical feasibility alone does not produce adoption. Customers already hold alternatives in added HBM, LPDDR, CXL, SSD tiering and software optimization. This section compares memory location, capacity per package, bandwidth, back-end difficulty and total system cost rather than component price alone.

### 2.1 LPDDR is a valid alternative. The difference is location rather than price

LPDDR cannot be treated as a simple downgrade from HBF. As of 2026, SK hynix and Micron have disclosed SOCAMM2 modules of up to 256GB, and multiple modules can build TB-class capacity on the CPU or system memory side. Micron positions SOCAMM2 directly as a tier for offloading KV cache from HBM.

The claim that HBF is the only option when TB-class capacity is needed therefore does not hold.

HBF and SOCAMM2 are not the same form factor competing at the same location, however. HBF targets a package-local or near-compute tier very close to the xPU, whereas SOCAMM2 expands large DRAM capacity on the board or CPU side. HBF matters not simply when a lot of memory is needed, but when large read-mostly data must stay close to the xPU at a capacity beyond what HBM can hold.

Conversely, if performance loss is limited when the data sits in a more distant tier, LPDDR, CXL or SSD tiering is the simpler answer.

### 2.2 A NAND base does not automatically lower finished-product cost

HBF’s NAND bit cost is likely lower than DRAM. Finished-product cost is not set by cell price alone, however. HBF is less a matter of putting cheap NAND into an existing package than a high-end package that must deliver high parallelism and bandwidth within physical constraints similar to HBM.

SK hynix, by contrast, states that its 256GB SOCAMM2 uses cost-effective wire bonding stack solution. Even where the LPDDR die itself carries a higher bit cost, module size and back-end conditions differ from HBF.

Given that structural difference, HBF may carry a heavier back-end burden than an LPDDR module in early production because of stacking, bonding, test, thermal management and package yield.

HBF’s assembly cost, known-good-die yield, stack yield, test cost and actual ASP are not disclosed, so there is as yet no public basis for a quantitative finished-cost comparison between HBF and LPDDR.

How to read the cost charts.

The cost splits and relative cost per GB in FIG. 06 and FIG. 07 below are scenario assumptions carried over from prior analysis, not an actual HBF production BOM or contract pricing. Because HBF’s real packaging yield and finished cost are undisclosed, these charts cannot support a conclusion that HBF is cheaper than LPDDR. Both figures are used only as a sensitivity illustration of how the economics shift when the balance between cell cost and packaging cost changes.

Sandisk states that HBF can use NAND’s low cost per bit to deliver 8 to 16 times the capacity of HBM at similar cost. That is a comparison against HBM, and at this stage it is closer to a vendor product target.

With no disclosed production cost, it should not be extended into a price advantage over LPDDR. In particular, if HBF stacking and packaging yields do not improve sufficiently, much of NAND’s low cell cost can be absorbed by back-end expense.

### 2.3 Economics are decided by system TCO, not component cost

For HBF to matter commercially, three things must hold.

First, a shortage of xPU-adjacent memory must persist even after larger HBM capacity, FP8 and FP4, MoE and KV cache optimization are applied. Sizing HBF demand from model size alone risks overstating the capacity actually required.

Second, adding HBF must reduce accelerator count or data movement in practice.

Swapping HBM for HBF while only lowering bandwidth would worsen system efficiency.

If instead the high-bandwidth HBM execution path is preserved while HBF keeps large weights or frequently referenced data near the xPU, reducing extra GPUs, host-memory round trips and storage reloads, total system cost can fall even at a somewhat higher component price. This is why Sandisk and SK hynix describe HBF as a technology that improves power, performance and TCO through larger near-compute memory capacity.

Third, packaging yield must reach commercial levels.

If package yield on 512GB-class multi-die stacks is low, HBF’s NAND bit-cost advantage will not carry through to finished cost.

The conclusion of Section 2 is therefore not that HBF is cheaper than LPDDR, but whether the system cost saved by near-compute capacity exceeds the additional cost of adopting a more complex HBF package.

---

## 3. Customer adoption: vertically integrated operators and general-purpose platforms have different interests

**SECTION 3 TAKEAWAY**

Early adoption of HBF is more likely among operators that control their own accelerators and software and can tune the memory hierarchy to a specific inference workload. Google and Tenstorrent are officially confirmed as participants in HBF standardization, and Meta is expanding its own MTIA into an inference-first full stack, giving it the system control needed to validate HBF. For NVIDIA, the constraint is not UCIe participation but the fact that it already has a roadmap optimizing memory capacity, bandwidth and serving structure within its own platform through HBM4, NVLink, Dynamo and LPX.

On the currently disclosed roadmap, I judge the incentive to adopt HBF in the baseline memory tier of a general-purpose GPU to be low.

HBF (+HBM) is not a simple memory swap but a system design that requires coordinating the accelerator interface, package layout, compiler, prefetch and service scheduling. Adoption likelihood by customer therefore depends less on the HBF specification itself than on how directly each operator controls hardware and software, and how strong its existing alternatives are.

### 3.1 Google: standardization participation and a vertically integrated TPU stack

The August 3 announcement from Sandisk and SK hynix states that Google and Tenstorrent participated as consortium members in HBF standardization, contributing to technical validation and standard development. Google’s participation is better read as system-design validation than as an intent to purchase memory.

Google designs its own TPUs and operates the software stack, including XLA, JAX and vLLM, alongside large-scale inference services.

That structure connects directly to the co-optimization HBF (+HBM) requires. Which weights to place in HBF, when to prefetch them and how much HBM to leave for KV cache can all be tuned at the compiler and runtime level.

Google also designed Ironwood as an inference-oriented TPU with memory capacity and bandwidth as primary design variables. Rather than HBF replacing HBM, there is a coherent case for evaluating it as a secondary tier providing larger near-compute capacity in a future TPU or an inference-specific derivative.

### 3.2 Meta: inference-first MTIA and iterative full-stack co-design

Meta disclosed its 2026 MTIA roadmap, committing to develop and deploy four generations of in-house silicon over two years and to extend coverage from recommendation and ranking into GenAI inference.

The strategy Meta emphasizes is fast iteration, inference-first design and adoption built on industry standards. Deploying hundreds of thousands of MTIA units in its own services is also a different condition from a merchant GPU vendor that must satisfy every external customer.

Meta is therefore well placed to validate HBF’s strengths and weaknesses on specific workloads. Recommendation and ranking, along with parts of GenAI inference, involve heavy repeated reads of large models, embeddings and reference data, and data placement can be adjusted within Meta’s own PyTorch and infrastructure stack.

Consortium participation and an actual HBF-bearing product should be kept separate, however. The August 3 standard announcement names Google and Tenstorrent, while Meta’s involvement has been referenced at the level of Investor Day remarks and reporting. Public information alone does not confirm HBF adoption in MTIA.

### 3.3 Tenstorrent: an open chiplet strategy is itself a reason to validate standards

Tenstorrent is one of the two external members officially confirmed in HBF standardization. Its product strategy emphasizes RISC-V, open-source software, licensable IP and an open chiplet ecosystem. Under that model, validating a new standard interface and chiplet option early is itself a source of competitiveness, more so than large-scale internal purchasing of any single memory technology.

If HBF develops into an open memory tier built on OCP and UCIe, Tenstorrent can add an option not only for its own accelerators but for IP customers’ inference designs. Inference-specific designs with a narrow workload range can optimize data placement and prefetch policy more tightly than a general-purpose GPU, which makes HBF’s latency and write constraints comparatively easier to manage.

### 3.4 NVIDIA: the incentive for a general-purpose GPU to adopt HBF is low

The important difference is NVIDIA’s memory and system roadmap.

Rubin GPUs provide up to 288GB of HBM4 and 22TB/s of memory bandwidth, and NVIDIA describes decode as heavily constrained by the memory subsystem.

For a single general-purpose GPU supporting training, post-training, dense and MoE inference and agentic workloads, HBF’s capacity benefit comes bundled with microsecond-class latency and write constraints. Introducing a memory tier premised on one inference pattern into a general-purpose GPU demands a larger incremental benefit than it would in a vertically integrated ASIC.

NVIDIA has also secured multiple ways to relieve memory capacity and serving efficiency constraints without HBF. Dynamo separates prefill and decode into distinct workers and transfers KV cache directly between GPU memories.

The Vera Rubin platform pairs the low-latency SRAM of the Groq 3 LPX inference rack with Rubin GPUs to accelerate decode, and NVLink Fusion allows hyperscalers’ custom XPUs to be integrated into NVIDIA rack architecture.

For NVIDIA to adopt HBF, it would have to go beyond providing more capacity and show a clear advantage over the existing HBM4, SRAM and disaggregated serving combination in at least one of cost per token, power or rack density.

If the currently disclosed roadmap holds, I judge that the baseline memory tier of general-purpose Rubin GPUs is likely to remain HBM4-centric.

The realistic paths for HBF into the NVIDIA ecosystem are inference-specific derivatives, semi-custom XPUs or a separate memory expansion tier. Those paths still require that 512GB HBF’s effective bandwidth, token-to-token latency versus HBM, and thermal and endurance data under sustained KV writes show a clear system advantage over the existing architecture.

---

## 4. How much it matters to Sandisk: direct revenue and second-order effects

**SECTION 4 TAKEAWAY**

In the bottom-up model, Sandisk’s annualized HBF revenue opportunity is about $0.09B under initial adoption, $0.95B in the base case and $4.22B in the scale case. The base case alone is unlikely to re-rate the company. Additional upside opens if HBF expands the high-value AI memory mix, absorbs additional NAND wafer capacity and affects the supply structure, and improves revenue visibility and business cyclicality through repeated hyperscaler design wins.

The approach first derives direct revenue from customer adoption, then asks whether there are second-order effects that could change the quality of Sandisk’s business.

The base equation for the direct revenue model is

accelerator unit pool x HBF attach rate x stacks per accelerator x stack ASP x Sandisk supply share.

On direct revenue alone, Google is the key variable.

Of the roughly $0.95B base case, about $0.84B, or 89%, comes from Google.

The $4.22B scale case equals about 21% of Sandisk’s FY2026 revenue of $20.25B, but it requires a 30% Google attach rate, four stacks per accelerator and meaningful concurrent adoption at Meta. A limited Google design win alone therefore cannot explain large share-price upside; real upside requires evidence of repeat adoption and rising content per accelerator.

The more important second path is product mix and wafer absorption.

Sandisk’s FY2026 results were shaped heavily by a higher-value customer mix and price increases, with datacenter revenue up 437% year over year. If HBF converts commodity NAND bits into high-value AI memory adjacent to the xPU, the mix effect could exceed direct HBF revenue.

Bernstein’s Mark Newman has estimated that HBF may require roughly three to four times the wafer capacity of commodity NAND to produce the same exabytes. If that holds and HBF adoption scales to millions of accelerators, HBF demand itself would reduce NAND supply slack and indirectly affect pricing and profitability for other datacenter NAND.

The three-to-four-times figure is an estimate, not Sandisk guidance.

The third path is whether business cyclicality changes before the valuation multiple does. Sandisk states that its NBM contracts place roughly 50% of FY2027 bits and about two thirds of FY2028 bits under committed volume, minimum financial guarantees and a structured pricing mechanism.

If HBF design wins recur under similar multi-year structures, the market could treat HBF not as another NAND product but as a more predictable revenue stream tied to AI accelerators. In that case share-price upside would not scale with HBF revenue alone but would come more from the earnings-quality improvement created together by a higher-value mix, tighter supply and lower cyclicality.

If customer adoption stays limited, or packaging yield and realized ASP fall short, that re-rating case does not hold.

---

## Key Sources and Verification

- Sandisk FY2026 Q4 Results. FY2026 revenue and adjusted free cash flow.
- Sandisk 2026 Investor Day. NBM contract structure, long term financial model, and HBF roadmap.
- Sandisk HBF OCP Announcement. HBF specifications and the participation of Google and Tenstorrent in HBF standardization.
- Sandisk HBF Fact Sheet. Gen1 specifications, including 512GB capacity and 1.6TB/s read bandwidth, and Sandisk cost positioning relative to HBM.
- Google Ironwood. Inference focused TPU architecture and the maximum 9,216 chip Superpod configuration.
- Micron 256GB SOCAMM2. 256GB modules, up to 2TB per CPU, and KV cache offload as an alternative memory architecture.
- Financial Times / Morgan Stanley. Estimates of Google TPU production volumes of 5 million units in 2027 and 7 million units in 2028.
- Meta MTIA Roadmap. Deployment of hundreds of thousands of MTIA accelerators and plans for four additional generations.
- Meta and Broadcom Custom Silicon Partnership. Initial commitment of more than 1GW and the planned multi gigawatt rollout.
- NVIDIA Rubin Architecture. 288GB HBM4 capacity, 22TB/s memory bandwidth, and the Rubin memory architecture.
- NVIDIA Groq 3 LPX. Rack level configuration of 128GB SRAM and 12TB DDR5, and the low latency decode path.
- NVIDIA Dynamo. Disaggregated prefill and decode inference serving architecture.
- NVIDIA NVLink Fusion. Semi custom infrastructure path, including hyperscaler custom XPUs. Source type: Company disclosure.
- UCIe Consortium Membership. Promoter membership including NVIDIA, Google, and Meta.
- Li et al. (2026), arXiv:2608.11668. Write intensity, thermal constraints, and endurance limitations in KV centric HBF serving.
- Son et al. (2026), arXiv:2608.13868. Potential benefits to batch size and throughput, together with read bandwidth and endurance requirements.
- Kim et al. (2026), arXiv:2608.14333. Parallel MoE weight delivery through direct GPU to HBF and HBF to HBM to GPU paths.
- Moonshot AI Kimi K3. Model architecture with 896 experts and 16 experts selected per token.
- Qwen3 Coder 480B A35B Configuration. Model architecture with 160 experts and 8 experts selected per token.
- MarketWatch / Bernstein. Bernstein estimate that HBF could require approximately 3 to 4 times more wafer capacity per exabyte than conventional NAND.
- Proprietary Analysis. Data placement, cost structure, customer adoption incentives, the bottom up HBF revenue model, and second order economic effects.
