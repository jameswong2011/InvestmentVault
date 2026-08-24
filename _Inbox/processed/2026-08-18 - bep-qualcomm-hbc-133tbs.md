---
title: "The Tax Dodge: Qualcomm's 133 TB/s Isn't What You Think"
source: 'https://bepresearch.substack.com/p/the-tax-dodge-qualcomms-133-tbs-isnt'
date: 2026-08-18
publication: BEP Research
gmail_id: 1a01501051b76b61
sender: bepresearch@substack.com
source_type: web-clip
tags: [research, email-backfill, BEP, memory, QCOM, HBC, NVDA, TSM, BESI, 000660, SNDK]
gmail_full: true
---

# The Tax Dodge: Qualcomm's 133 TB/s Isn't What You Think

**Source:** [BEP Research](https://bepresearch.substack.com/p/the-tax-dodge-qualcomms-133-tbs-isnt) — co-authored with Rui "Rick" Xie; second installment in the free memory series. Gmail `1a01501051b76b61` from `bepresearch@substack.com` dated 2026-08-18T13:05:32Z (21:05 Asia/Shanghai). Full free article.

**Subtitle:** Qualcomm's answer to HBM is bearish the large-interposer premium, not the memory.

Co-authored with Rui "Rick" Xie (rickxie.cn), a memory-systems researcher with a PhD from Rensselaer Polytechnic Institute whose work runs from DRAM to SSDs. This is the second installment in our memory series. Rick leads the engineering and standards analysis; Ben Pouladian leads the investment framing.

Six weeks ago Rick and I published [The Bandwidth Tax](https://bepresearch.substack.com) and argued that the real cost of HBM is levied on the system, not the stack: the interposer, the base die, the packaging, the cooling, everything a platform pays around each cube to turn a faster stack into delivered bandwidth. We said the durable trade was one level up from the DRAM cell: long the constraint, and long whoever gets paid to relieve it.

On June 24, at its Investor Day, Qualcomm put a commercial roadmap behind an architecture built to reduce its dependence on the conventional HBM interposer. It stacks the accelerator under the memory, and Qualcomm says the silicon interposer is no longer needed.

Rick's verification and my framing point in different directions, so let me be exact about what we are underwriting. Not HBC working: Rick's read, below, is that the headline numbers are unproven and the base case is a niche. We are underwriting something narrower and more actionable: the packaging premium is currently priced as though nobody is trying to route around it, and that is no longer true.

## What Qualcomm Actually Announced

The announcement that moved the stock was the guidance: non-handset revenue expectations for FY29 nearly doubled, from $22 billion to $40 billion, with data center as the major driver. The market is processing that number through a familiar template, which is whether Qualcomm can pull off the MediaTek trade, out of the handset doghouse and into a data-center re-rating. Citrini Research made that case in July in "All Along the AI Watchtower," and described the hardware side as "taking detours around the HBM toll booth." The metaphor is theirs; the detour is worth mapping.

It has a name: High Bandwidth Compute. Instead of an accelerator die connected sideways to HBM stacks across a silicon interposer, HBC takes the AI accelerator out of the SoC and places it directly beneath a DRAM stack, connected vertically by through-silicon vias. Bandwidth flows up through the whole die area rather than out through the edges. Qualcomm says multiple HBC stacks can be deployed using standard packaging, without the HBM silicon interposer. The AI200 rack ships this year without HBC. HBC debuts with AI250 in 2027, ahead of an AI300 and a server CPU in 2028.

One thing Qualcomm has not said is what that memory actually is. The company has never identified HBC's DRAM as LPDDR, and the coverage has assumed it, including our own first draft of this piece. Hold that thought, because the entire investment leg below turns on it.

The claimed numbers, from the Investor Day: 6x the bandwidth per watt of HBM. 200x the capacity per watt of SRAM. 4–8x better decode performance per watt and on a TCO basis. A headline figure of 133 TB/s. Tony Pialis, who runs Qualcomm's data center business, describes the result as SRAM-like performance with stacked-memory density, built out of everything a mobile-chip designer was forced to get good at: low power, small area, no exotic packaging.

Every one of those numbers is Qualcomm's own.

## The Claims That Don't Survive Contact

Qualcomm's four headline numbers, and the boundary each one is actually drawn inside.

Qualcomm describes 133 TB/s as effective memory bandwidth, and explains that HBC makes internal memory bandwidth available to local computation while the main accelerator keeps the orchestration-heavy work. Read it as workload bandwidth consumed inside HBC, not raw bandwidth exposed to the main accelerator.

No defensible sustained number can be reconstructed from LPDDR5X or LPDDR6 pin rates, which is the first thing we tried and the first thing that failed. Qualcomm has disclosed neither the HBC memory protocol nor its interface width, channel structure, or stack configuration. Pin-level arithmetic would add precision the public architecture does not support.

Qualcomm defines the sixfold bandwidth-per-watt figure as an internal estimate against competing published specifications, normalized at card level. The two-hundredfold SRAM comparison normalizes at rack level. Different boundaries, so the two numbers were never a common benchmark and cannot be quoted as one. The baseline will also move before HBC samples: Micron currently specifies more than 2.8 TB/s for HBM4 and Samsung up to 3.6 TB/s for HBM4E, so any efficiency claim should be retested against the HBM systems shipping when AI250 becomes available.

Classification is where the investment case and the engineering case meet. HBC is near-memory compute, not processing-in-memory. Qualcomm describes a compute die handling data-bound operations beneath DRAM bonded directly onto logic, which puts a separate logic layer under the memory rather than computation inside the DRAM array. That distinction is not pedantry, and it is one this newsletter has been on the record about since January, quoting Patterson in The Hierarchy Rewrites: "better suited for LLM inference than processing-in-memory (PIM) because shards can be 1,000× larger."

Which makes software the central test, not bandwidth. Qualcomm has not detailed operator coverage, compiler partitioning, or fallback behavior. HBC creates system value only when the traffic it eliminates locally exceeds the coordination cost of getting work to it. And the dodge is partial by construction: it may remove the large silicon interposer, but it still needs direct DRAM-to-logic bonding and 3D integration, which relocates packaging complexity into the vertical stack rather than deleting it.

The decisive evidence will be sustained end-to-end tokens per joule under disclosed workload and thermal conditions. Until Qualcomm publishes the bandwidth boundary, the workload methodology, and measured system results, the architecture is credible and the headline numbers are not.

## Why Every Previous Attempt Died

Processing-in-memory has produced good benchmark numbers for a decade without producing a platform. Samsung reported almost 2.5x higher system performance and more than 60% lower energy from HBM-PIM. SK Hynix was still demonstrating AiMX on H100s with vLLM in 2025. UPMEM shipped programmable DRAM modules and a real software stack. None of it reached a named hyperscale deployment, which shows technical viability alone was never enough to build a platform.

It was ownership and software. The economics asked a memory vendor to sell compute it had no ecosystem to support, and the programming model asked customers to restructure their code for the memory's benefit. HBC addresses part of the ownership problem: one vendor now designs the memory-side compute, the accelerator, the runtime, and the rack, which is a genuinely different starting position than SK Hynix bolting AiMX onto someone else's H100. That integration reduces friction. It does not remove the software, execution, and ecosystem constraints that limited the earlier systems.

The second problem is untouched. CUDA is not a compiler. It is a decade of optimized libraries, profilers, and deployment tooling that customers have already built their models, their reliability processes, and their hiring around. ROCm is a thinner version of the same thing and it has taken AMD years to get that far. Against that, an incremental bandwidth or energy advantage does not clear the migration bar, and HBC still splits every real model across two compute domains. The variable that matters is the fraction of the token path that stays inside HBC after partitioning, because high internal bandwidth buys little when control keeps returning to the main accelerator.

Then there is heat, and this is where the architecture is most exposed. HBC parks active logic in direct three-dimensional proximity to temperature-sensitive DRAM, which is precisely the separation the interposer was providing. Prior die-stacked research used an 85°C DRAM threshold, modeled refresh doubling for each additional 10°C, and found allowable logic power ranging from about 8.5 W under passive cooling to about 55 W under active cooling. Those numbers do not predict HBC. They do establish that cooling and stack orientation set a ceiling on how much compute can run under a DRAM tower, and Qualcomm has disclosed no logic power, no DRAM junction temperature, and no sustained performance after thermal steady state.

Rick's base case: HBC becomes a specialized decode or offload tier inside selected Qualcomm systems while GPU and HBM platforms keep the broader inference market. Qualcomm has built a more integrated version of the PIM proposition, and most of the conditions that stopped earlier systems from becoming platforms are still standing.

## Everyone Is Routing Around Something

That base case is survivable for the trade, because the trade does not depend on Qualcomm winning. It depends on Qualcomm not being alone, and it isn't.

HBC is not the first architecture built to avoid the HBM bill, and this newsletter documented an earlier one under its own byline. From The Fourth Piece Ships in March: "The Groq V3 uses on-chip SRAM on what appears to be a standard packaging process. No CoWoS interposer. No HBM stacks." Positron got there with commodity LPDDR before that. Qualcomm's version is the largest and best-funded instance of a move already in progress, which is a stronger fact for the thesis than being first would have been. One company routing around advanced packaging is a science project. Three is a pattern.

Three accelerator architectures route around the HBM and interposer stack directly. Vera instead validates datacenter LPDDR as a CPU memory tier, in systems whose GPUs still run HBM4.

The pattern is the one this newsletter has been tracking all year. As I wrote in The Memory Wars: "NVIDIA Feynman (2028) won't fight SRAM physics. It routes around them: 3D-stacked SRAM using AMD X3D-style hybrid bonding." Memory vendors are routing around thermal compression bonding with hybrid bonding; NVIDIA is routing around SRAM scaling with stacked cache. Qualcomm's version is the most aggressive, and it takes on a whole new cost structure in logic-memory integration to get there.

Four weeks after the Investor Day, NVIDIA supplied the data point the LPDDR argument was missing. Vera pairs 88 custom cores with SOCAMM2 LPDDR5X at up to 1.2 TB/s per socket, 256 GB to 1.5 TB per socket, field-replaceable, multi-vendor sourcing explicitly enabled. As I wrote in NVIDIA Vera: When CPU Latency Becomes GPU Economics: "Datacenter LPDDR is now a named product line." At maximum configuration that is 384 TB of LPDDR5X in one rack.

Vera is not itself a dodge, and it matters not to file it as one. It is a CPU, and the Rubin GPUs beside it still run HBM4. What it establishes is narrower and more useful: the largest accelerator vendor in the world has qualified datacenter LPDDR as a real memory tier, with multi-vendor sourcing, at rack scale. The question NVIDIA left open is whether that capacity becomes addressable KV cache. If it does, the tier stops being one company's bet.

The Bandwidth Tax gave the pattern its rule: you route around a wall rather than push through it, and you pay for the route. Hybrid bonding pays in packaging complexity, stacked SRAM in bonding yield, and both bills come due at the same suppliers. So the question for HBC is not whether the tax disappears, since our thesis says it never does, but where it gets collected instead.

## Who Collects If It Works

HBC is bearish the large-interposer premium and neutral-to-bullish the memory oligopoly. Those are not the same trade, and the market is pricing them as one.

The layer it disintermediates is the layer collecting today: the large interposer, CoWoS capacity, and the 30%-plus HBM4 manufacturing premium we documented in the parent piece. An architecture that tiles accelerator-memory stacks without a large silicon interposer is a direct attack on that premium, arriving exactly as the premium is at its highest.

But whatever DRAM ends up inside an HBC stack, it is high-density memory, and high-density memory is sold by Micron, Samsung, and SK Hynix. The same three vendors. The bear case for HBM packaging is not a bear case for DRAM. It is a mix-shift within the oligopoly's own product lines, and the incumbents have already told us how that story goes: as I wrote in Micron Just Proved the Memory Thesis, "Sanjay confirmed that non-HBM margins are currently higher than HBM margins." If the next bandwidth architecture consumes non-HBM DRAM at data-center scale, the same vendors sell the dodge with one hand while they sell the tax with the other.

Now the part that keeps this from being a clean short. Qualcomm has not identified the memory technology, named a DRAM supplier, or said who performs final logic-and-memory integration, so treat the mix-shift as a scenario with a supplier list still missing from it. And the dodge may partially refund what it avoids: even skipping large interposers and some CoWoS capacity, HBC still consumes wafer thinning, bonding, known-good-die infrastructure, and advanced test. The pressure falls on the scarcity premium attached to large interposers and conventional accelerator-to-HBM integration. It does not fall on packaging as an activity.

The tax moves. It does not disappear.

Which is why this is a migration, not a disappearance, and the destination is one we have already named. The Hierarchy Rewrites put the candidates for exactly this direction on the page in January: TSMC SoIC, Intel Foveros, and the hybrid-bonding equipment suppliers, Besi, EVG and SUSS. Direct DRAM-to-logic bonding is their process, not CoWoS's, which makes them plausible beneficiaries rather than confirmed ones, since Qualcomm has disclosed neither its assembly flow nor its suppliers. If HBC and the architectures chasing it scale, value moves from interposer area toward bonding tools, stack yield, thermal integration, and test. The packaging layer deserves the scarcity premium it is charging today, 2027 is a long way out, and CoWoS is sold out regardless. None of that changes the fact that the most valuable customers in the world are now engineering their way off that particular tax roll, and toll roads get repriced on the first credible detour, not the last car through.

On Qualcomm itself: the re-rating comp is MediaTek, which came into the year under 20x NTM earnings and re-rated hard once TPU exposure pulled it out of the handset bucket. The credibility gap is real, since this is the company that shipped Centriq in 2017 and walked away, but the validation stack is different now: Alphawave for SerDes, two hyperscaler custom-silicon programs contributing in FY27, a multi-generation Meta CPU agreement with production in 2H28, and the pending Modular acquisition for the software layer. The data-center line is more than $15 billion of that $40 billion, not additive to it: Qualcomm's own bridge is $10 billion automotive, more than $14 billion IoT, and more than $15 billion data center. TD Cowen's read, which Qualcomm has not confirmed, is that the target counts only existing customers. Named customers and measured system performance are the evidence; the guidance is the option.

## Where This Breaks

The graveyard wins again. Every number in this piece is Qualcomm's own, with zero third-party benchmarks and first silicon in 2027, from a management team whose last data-center entry ended in a walkaway. The specific failure mode is high internal bandwidth that never becomes end-to-end inference, with operator coverage, partitioning, fallback execution, and thermal throttling eating the local gain. In that case the AI250 launch is a slide deck with a good chart in it, and the packaging premium keeps collecting uninterrupted.

The stack outruns the dodge. Our own correction from the parent piece cuts against the urgency here: HBM is improving per stack, per watt, and per delivered TB/s every generation, and it is sold out through the exact window in which HBC must prove itself. The competition is not only HBM4E and hybrid bonding. Larger caches, lower-precision weights, speculative decoding, and KV-cache optimization each shrink the value of near-memory execution before AI250 reaches production. The dodge only pays if the tax keeps rising.

HBC works and the incumbents still collect. High-density DRAM from the same memory oligopoly, potential overlap with the same constrained stacking and test capacity, and a bill of materials that reroutes dollars rather than removing them. Bonding, stack yield, test, cooling, and customer validation could absorb everything saved by deleting the interposer. In that outcome the architecture survives, our asymmetry holds, and the profit pool barely moves. A reader can accept this entire piece and still conclude the only durable longs are the memory vendors and foundries they already own.

What would change our mind. Two conditions, by end-2027. Qualcomm discloses how effective bandwidth is calculated, in enough detail to separate raw DRAM bandwidth from locally consumed traffic from bandwidth visible to the accelerator. And independent testing confirms at least half the claimed decode perf/watt advantage against contemporary HBM systems under matched model quality, latency, and thermal conditions, with at least one named hyperscaler or frontier lab in production. Both, and the packaging-premium leg activates. Either one missing, and we write the follow-up saying the tax held.

## Stop Asking Whether Qualcomm Catches NVIDIA

That is not what the Investor Day was about, and Qualcomm does not need to catch NVIDIA for HBC to matter. What matters is that the cost of moving data is now determining the shape of the machine, and three separate accelerator teams have concluded that the cheapest way to pay the bandwidth tax is to build something that owes less of it.

The Bandwidth Tax said the money made around each HBM stack is growing faster than the money made inside it. HBC tests the corollary: when the tax gets high enough, someone builds a machine that doesn't pay it. Whether this particular machine works is still unproven, and the graveyard puts the burden of proof on Qualcomm. The direction is set regardless.

The tax may move. Qualcomm still has to prove the detour is cheaper, and until it does, stay long the constraint.

Like The Bandwidth Tax before it, this piece is free and citable on purpose. The thesis is the marketing. The trade expression, the names and entries across the collection-point migration, goes to paid subscribers in the follow-up.

## The Next Detour

While this piece was in final review, the tier below started making the same argument. SanDisk calls it High Bandwidth Flash: NAND stacked and interfaced like HBM, pitched as memory rather than storage, and it ran through the company's investor day last week. The pitch writes itself, which is exactly why it gets the same treatment Qualcomm got here.

Rick and I are already working it, and the boundaries preview the piece. HBF is moving from a concept into a standards and sampling story, and NAND endurance is not solved, so the honest question is not whether flash can deliver more bandwidth. It is which AI bytes actually belong on NAND. Model weights are read-mostly and plausible. KV cache could be the far larger demand pool, but it is a write stream, and the write stream carries endurance, placement, and reload costs the slide decks do not price. HBF ends up one test case inside the bigger story, which is AI pulling NAND into memory tiers it has never had to serve. If the tax moves down the hierarchy, we will map who collects there too.

That will be the third installment. The first two lived on the DRAM side of Rick's research. The next one crosses to flash, which is the other half of it.

A housekeeping note: I will be at Hot Chips next week, where the memory track argues several of this piece's open questions in public. If you will be there, say hello. Field notes to follow.

## What to Watch

- AI200 rack deployments this year: named customers, not press releases. HBC is not in this product.
- Any HBC silicon disclosure with sustained rather than aggregate bandwidth, and the first third-party benchmark.
- DRAM supplier disclosures for HBC, and data-center qualification signals from Micron, Samsung, and SK Hynix: the mix-shift tell.
- Meta C1000 production ramp in 2H28, and whether either hyperscaler custom program is publicly named in FY27.
- Whether NVIDIA and AMD answer with LPDDR tiers or near-memory configurations of their own.
- CoWoS pricing at the margin in 2027, and hybrid-bonding tool orders at Besi, EVG and SUSS as the offset.

## Sources

- Qualcomm Investor Day materials, June 24, 2026 (FY29 guidance, HBC architecture, AI roadmap)
- Qualcomm Investor Day press release, June 24, 2026 — FY29 segment bridge: $10B automotive, >$14B IoT, >$15B data center within the $40B non-handset target
- Qualcomm, "HBC near-memory computing" (OnQ, July 2026)
- Qualcomm AI accelerators, product/expertise page
- Citrini Research, "All Along the AI Watchtower" (July 19, 2026) — source of the "toll booth" framing
- BEP Research, "The Bandwidth Tax" (July 9, 2026) — HBM4/HBM4E vendor disclosures, JEDEC JESD238B.01/JESD270-4, TrendForce HBM4 premium
- Samsung, in-memory processing (HBM-PIM)
- SK Hynix, AI Infra Summit 2025 (AiMX with H100 / vLLM)
- SK Hynix, back-end process series, wafer-level packaging / TSV stacking
- UPMEM technology overview
- Micron HBM2E technical marketing brief (known-good stacked die)
- Eckert et al., die-stacked PIM thermal analysis (85°C threshold, refresh doubling, 8.5 W passive / 55 W active)
- NVIDIA CUDA Toolkit
- AMD ROCm documentation
- TD Cowen coverage of Qualcomm Investor Day (as reported)

## Related BEP Research

- The Bandwidth Tax
- The Fourth Piece Ships: NVIDIA's Groq
- The Hierarchy Rewrites
- NVIDIA Vera: When CPU Latency Becomes GPU Economics
- The Packaging Paradox: Why CoWoS, Not 2nm, Is the Real AI Bottleneck
- The Shoreline Problem: A Bear Case on HBM

## About the Authors

Rui "Rick" Xie is a researcher in computer systems, memory architecture, and AI infrastructure (rickxie.cn). He holds a PhD from Rensselaer Polytechnic Institute, where his research focused on memory architecture and computer systems, with a particular interest in DRAM and SSDs. For this piece he worked from Qualcomm's public HBC disclosures and the prior near-memory literature directly, established the different measurement boundaries sitting behind the headline numbers, refused a sustained-bandwidth reconstruction the public architecture does not support, and set the conditions under which the architecture would be proven. His views and analysis are his own and do not represent his employer.

Ben Pouladian is the publisher of BEP Research and CEO of BEP Holdings. He led the investment framing and the margin-capture analysis. Framings are credited to their originators throughout. More at www.bepresearch.com

**Disclosure:** The author holds positions in NVDA, NOW, LITE, CRDO, TSEM, ALAB, WOLF, SMCI, BE, NBIS, and ORCL (2027 LEAPS). No position in QCOM. This is investment research, not investment advice. Do your own work.
