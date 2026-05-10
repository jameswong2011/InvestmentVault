---
date: 2026-04-24
tags: [research, ai-compute, hyperscaler, NVDA, AVGO, AMD, MRVL, INTC, NET, CRWD, PANW, NOW, PLTR, PSTG]
sector: Compute & AI Compute Accelerators
source: https://www.youtube.com/watch?v=bNdiBwXbLNw
source_type: video-transcript
propagated_to: [NVDA, AVGO, AMD, MRVL, INTC, NET, CRWD, PANW, NOW, PLTR, PSTG]
---

# Thomas Kurian on TPU Capacity, Anthropic Hosting, and Agentic Chip Design

## Thesis Delta

Google Cloud CEO confirms TPU capacity is the structural advantage that the rest of the industry is paying for: *"we have more demand than we can possibly meet from all the other AI labs"* and Gemini Enterprise token volume jumped from **10B/min (January 2026) → 16B/min (April 2026)** with enterprise users **+40% sequentially**. Three first-order investment reads: (1) [[Theses/AVGO - Broadcom]] thesis strengthens — Broadcom is the silicon design partner for Google's 8th-gen TPU split (8T training pod = 9,600 chips, 8I inference pod = 1,152 chips), and Google's capex-driven TPU production schedule directly funnels Broadcom revenue; (2) [[Theses/NVDA - Nvidia]] competitive pressure on hyperscale workloads is real but bounded — Anthropic continues to host on Google TPU even while training on NVIDIA, validating multi-vendor compute reality not single-vendor lock; (3) cybersecurity ([[Theses/NET - Cloudflare]], [[Theses/CRWD - CrowdStrike Holdings]], [[Theses/PANW - Palo Alto Networks]]) — Kurian explicitly previews "continuous red teaming" agent products from the Wiz acquisition, confirming the cybersecurity-platform agentic pivot is a Google Cloud strategic priority not just a niche.

## Summary

Matthew Berman interviews Google Cloud CEO Thomas Kurian on the Google Cloud Campus immediately ahead of Google Cloud Next 2026. The conversation covers seven investment-relevant blocks: (1) TPU capacity and monetization architecture, (2) the 8th-gen TPU split into 8T (training) and 8I (inference), (3) hosting Anthropic as a structural competitor, (4) Mythos / 10-trillion-parameter model serving capability, (5) agentic AI and how agent design is reshaping chip architecture, (6) the Wiz acquisition's cybersecurity agent roadmap, and (7) Google's coding-productivity model (Jet Ski internal harness).

The dominant message is that Google has *11 years of TPU compounding* and explicit strategy diversification — they monetize tokens directly (Gemini), tokens through other models (Anthropic, Apple), and TPUs as a chip product (Citadel for capital markets, Department of Energy for HPC). Kurian's claim that *"Citadel uses TPUs"* and *"DOE high-performance computing customers talk about it"* is the structural pivot that reframes TPUs from "Google AI chips" to *general-purpose accelerator infrastructure that competes with NVIDIA on TCO not just internal usage*. Combined with the explicit confirmation that *"if we were much more expensive [Anthropic and other labs] would not be asking for TPU"* — this is a head-to-head TCO claim against NVIDIA that has not previously been this direct from a Google executive.

The agentic AI section is the most architecturally specific. Kurian describes how agent workflows (long-running, multi-tool, hours-to-days) reshaped TPU design: KV cache lifetime requirements drove memory-architecture changes, classical-compute coexistence drove their ARM-chip program (Axion), agent inference distribution drove the 8I air-cooled variant for non-water-cooled data centers. The reading: Google has been co-designing chips for the agentic-AI workload for at least 2-3 years before the public's "agent era" framing emerged in late 2025 / early 2026. This validates the [[Theses/NOW - ServiceNow]] / [[Theses/PLTR - Palantir]] thesis that agentic AI architectural moats sit at the integration layer between model + system + data, not at any single layer.

The Wiz / cybersecurity preview is concrete: Google previewed three agent products — *continuous attacker* (always-on red team), *prioritization agent* (which vulnerabilities to fix first), and *fixer agent* (autonomous patching). Plus a separate agent for "finding all the places the old code was running and removing it" after a patch. This is direct competition for [[Theses/CRWD - CrowdStrike Holdings]] Falcon Exposure Management + [[Theses/PANW - Palo Alto Networks]] Cortex XSIAM autonomous-SOC + [[Theses/NET - Cloudflare]] Zero Trust positioning. Material risk vector for the cybersecurity sector if Google bundles these agents into Workspace / Cloud Identity for free or near-free.

## Framework / Mental Model

**TPU Monetization Layers (Kurian's diversification framework)**

Google monetizes the same TPU silicon across three distinct revenue paths, each with different unit economics:

| Layer | Customer type | Monetization | Margin profile |
|---|---|---|---|
| **L1: First-party model + chip** | Google Gemini (consumer + enterprise) | Token-priced via API + Gemini Enterprise + ad-attached search | Highest — Google captures both model and chip margin |
| **L2: Third-party model on Google chip** | Anthropic, Apple (model contract), other AI labs | TPU rental at compute-hour rates; customer's model runs the inference | Medium — chip margin only, no model margin; offset by lower capex risk (utilization filled by external demand) |
| **L3: Chip-as-a-product** | Citadel (capital markets), DOE (HPC), others on roadmap | TPU machines deployed in customer's own data center for latency-sensitive workloads | Variable — direct chip sale + maintenance, less recurring than L1/L2 but unlocks workloads (algo trading) where Google Cloud doesn't have a customer relationship |

Methodology: Google deliberately balances allocation across L1/L2/L3 because (i) supply-chain leverage (vendor pricing favors Google's combined volume), (ii) revenue diversification reduces capex-funding risk, (iii) different customer segments validate TPU competitiveness more broadly than internal usage alone.

**Agent-Era Chip Co-Design (Kurian's three-vector framework)**

Agent workloads differ from Chat workloads on three axes that drove TPU architectural decisions:

1. **KV cache lifetime**: agent tasks run 6-12+ hours; KV cache must be pinned to keep context-shuffling costs from dominating. Drove memory-architecture choices in 8I.
2. **Classical-compute coexistence**: agents operate computers (browser use, OS-level tasks, virtual machines) — Google built ARM CPUs (Axion) alongside TPUs because these workloads are not GPU/TPU-native. The implication is hyperscalers need a CPU-and-accelerator combined offering, not pure-AI silicon.
3. **Inference distribution**: agents need low latency in many locations to manage user experience; 8I chip can run in **non-water-cooled (air-cooled) mode**, expanding deployment site count vs water-cooled-only training pods. Air-cooling enables co-location in many traditional enterprise data centers.

Methodology: Kurian describes this as "co-design across the whole system" — TPU silicon, Axion CPUs, Lustre + Rapid Storage networking, JAX/PyTorch/XLA software all evolve together based on workload-shape feedback.

## Evidence

| Metric / claim | Value | Investment relevance |
|---|---|---|
| Gemini Enterprise tokens/min, January 2026 | 10 billion/min | Baseline for tracking demand growth |
| Gemini Enterprise tokens/min, April 2026 | 16 billion/min | +60% in 3 months — implies enterprise inference demand growth far exceeds model price-per-token decline |
| Gemini Enterprise users, sequential growth | +40% (one quarter) | Enterprise adoption velocity |
| 8T (training) chips per pod | 9,600 | Largest training pod in industry per Kurian |
| 8I (inference) chips per pod | 1,152 | Inference-optimized smaller scale |
| 8T memory per system | 2 petabytes | "100x the size of all the Library of Congress digitized" |
| Network architecture | Single optical Torus | "Super predictable latency across all chips in a pod" |
| TPU history | 11 years, 8 generations | Compounding moat — "things compounded over time" |
| Cloud share of Alphabet capex | ~50% | And growing because Cloud is fastest-growing segment |
| Demand-supply state | "More demand than we can possibly meet from all the other AI labs" for the next 10 years | Persistent supply shortage = pricing power |
| TPU customers outside AI labs | Citadel (capital markets, algo trading), DOE (HPC) | TPUs becoming general-purpose accelerator, not just AI |
| Apple model contract | Confirmed signed with Google | Apple Intelligence backend partner |
| Mythos rumor | First 10-trillion-parameter model | Kurian: "we would not design a model that we couldn't serve... very confident TPUs can serve the largest models in the world" via disagregated serving |
| Pre-training scaling | "We're not seeing [a slowdown] from the point of view of chip design or system design or lack of capacity or any of that" | Aligns with [[Research/2026-04-24 - Luo Fuli on OpenClaw and Agent-Era Compute Reallocation - video-transcript]] |
| Storage announcement: managed Lustre | 10 TB/s throughput | Designed for large-scale training fleets |
| Storage announcement: Rapid Storage | 15 TB/s for inference | Forward proxy near inference chips for ultra-low latency |
| New networking: Virgo | Ultra-low connectivity speed across giant cluster | Common backbone for storage + compute |
| Wiz acquisition agent products | (1) continuous attacker / red team agent, (2) prioritization agent, (3) fixer agent | Direct competition for CRWD / PANW / NET cybersecurity platform agents |
| Google Cloud hiring | "Adding people for products and sales... go-to-market organization... deployed engineers... new product capability" | Despite AI productivity, headcount expanding |
| Block (Jack Dorsey) layoff context | "Block laid off half their organization, blamed AI" — Kurian: "every company has demand for its products and services and each CEO makes their own decisions" | Implicit — Google's revenue trajectory supports headcount expansion; Block's does not |
| Internal coding tool | Jet Ski harness | Direct feedback loop from Google engineers into DeepMind Gemini quality |

## Contradiction Check

**Strongly supports**:
- [[Theses/AVGO - Broadcom]] — Broadcom is the silicon design partner for Google TPU. The 8T/8I split announcement at Google Cloud Next 2026 directly correlates with AVGO custom-silicon revenue. Kurian's confirmation that TPU demand exceeds supply means AVGO production schedule is sold out for the foreseeable future. The non-AI-lab customer expansion (Citadel, DOE) extends the AVGO addressable revenue beyond the hyperscaler-AI cycle.
- [[Theses/MRVL - Marvell Technology]] — Networking + memory IP for hyperscaler custom silicon scales with TPU production, even though Marvell is not the primary Google partner. Kurian's emphasis on "single optical Torus network", "Virgo" networking, and "managed Lustre 10 TB/s" all point to networking/IO buildout where Marvell has IP exposure.
- [[Theses/PSTG - Pure Storage]] — Counter-intuitively, Google's own **Rapid Storage at 15 TB/s for inference** is a competitive pressure on PSTG enterprise-storage positioning, but Kurian's framing of "ultra-low latency for inference is the new bottleneck" confirms PSTG's FlashBlade//EXA thesis (>10 TB/s for AI workloads). The category exists; the question is whether enterprise customers buy from PSTG vs Google's managed offering.
- [[Theses/NOW - ServiceNow]] / [[Theses/PLTR - Palantir]] — Kurian's agent-era framing aligns with the integration-layer-as-moat thesis. Workday, ServiceNow, Palantir all sit between model and enterprise data; Kurian explicitly frames "models became really good at dealing with the abstractions of the world" as the gateway to agent workflows. Validates the [[Sectors/Enterprise Workflow AI & Automation]] sector thesis.

**Strongly challenges**:
- [[Theses/NVDA - Nvidia]] — Direct head-to-head TCO claim from Google ("we are the best TCO" + "Anthropic would not be asking for TPU if we were much more expensive"). The non-AI-lab TPU customer expansion (Citadel, DOE) is a structural threat — TPUs migrating from "Google's AI chip" to "general-purpose accelerator" widens NVIDIA's competitive surface. **However**: Kurian's own admission that Google has "diversification in monetization" because its supply-chain volume is higher when external customers buy means external demand is incremental, not displacing. NVIDIA continues to win on developer ecosystem (CUDA), training flexibility, and supplier-customer-relationship breadth. Net: marginal pressure on NVIDIA's hyperscale-inference share, no thesis-killer.
- [[Theses/CRWD - CrowdStrike Holdings]] / [[Theses/PANW - Palo Alto Networks]] / [[Theses/NET - Cloudflare]] — Google's three Wiz-powered agent products (continuous red team, prioritization, fixer) are direct overlap with Falcon Exposure Management, Cortex XSIAM autonomous SOC, and Cloudflare One Zero Trust. If Google bundles these agents into Workspace / Cloud Identity at zero or near-zero marginal cost (the Microsoft cybersecurity playbook), the mid-market cybersecurity TAM compresses. **However**: enterprise cybersecurity sales are 5-7 year procurement cycles with deep workflow integration; Google Cloud's penetration in non-Workspace enterprises is a fraction of Microsoft's, limiting bundle leverage outside the existing GCP base. Net: pressure on CNAPP/SecOps adjacencies in GCP-heavy customers; less impact in AWS/Azure-dominant accounts.
- [[Theses/AMD - Advanced Micro Devices]] — AMD's MI series competes for the same hyperscaler workloads where Google now offers TPUs externally. The "TPUs become general-purpose accelerator" framing potentially compresses AMD's share-take from NVIDIA, since some workloads previously expected to go to AMD MI may now go to Google TPU (Citadel-type customers in particular). **However**: Google does not sell TPUs into all the same data centers AMD targets (Microsoft Azure won't run Google TPUs), so the addressable overlap is limited.

**Specific assumptions affected**:
- Bear thesis on NVDA: "hyperscalers will increasingly use custom silicon, compressing NVIDIA's share" — Kurian's data is the strongest direct evidence for this in 2026 (confirmed Anthropic on TPU, Apple on Google model contract, Citadel on TPU, DOE on TPU). The thesis is now empirical, not speculative.
- Bull thesis on AVGO: "Broadcom captures custom-silicon design margin from hyperscaler ASICs" — Kurian's 8th-gen TPU split + token-volume growth + supply-shortage statements all directly increase the Broadcom revenue trajectory. Supports moving AVGO conviction higher if the Q3/Q4 2026 earnings confirm corresponding revenue growth.
- Pre-training-is-dead thesis: directly refuted by Kurian (same conclusion as Luo Fuli in the parallel research note above).

## Source Excerpts

> "if you have your own chip if you don't you're reselling other people's stuff and in a capacity constrained environment your unit economics get more expensive and in our case because we control the chip the unit economics remain attractive so that is going to be an advantage for us because we own the silicon" — Kurian on TPU vertical integration

> "we have more demand than we can possibly meet from all the other AI labs and so I would just tell you that uh they would not be asking for TPU if we were much more expensive" — Kurian directly on TCO vs NVIDIA

> "you'll see Citadel for example in capital markets talking about how they using our TPUs you'll see department of energy and high performance computing customers talk about it so we're also seeing TPUs becoming more general purpose infrastructure not just for AI algorithms" — Kurian on TPU expansion beyond AI labs

> "8 [generation TPU] has 9600 chips uh 8i is I think 1152 all on a single optical Torus network so there's incredibly high bandwidth super predictable latency across all the the the chips in a pod" — 8th gen TPU specs

> "between January and now our token count has jumped from 10 billion a minute to 16 billion a minute and the number of enterprise users of Gemini Enterprise has jumped by 40% sequentially" — Kurian on demand growth

> "we're not seeing that [pre-training slowdown] from the point of view of chip design or system design or lack of capacity or any of that" — Kurian refuting pre-training-plateau narrative

> "we're going to show three different types of agents an agent that continually attacks you to make sure your vulnerabilities are being fixed and you don't get caught off guard which you couldn't do before an agent that prioritizes the issues that are being discovered so that you can get okay these are the ones I really need to fix and then a third one that helps you fix them" — Wiz cybersecurity agents

> "it's not just I can talk to a computer but I need to be able to respond to the information the computer gives me... that's then led to this notion of agent" — Kurian framing the agent-era thesis

> "people asked us why did you build 8I you know the inference chip it's because it's we've seen that as you eventually no matter how rich you are you cannot fund training without making money on inference and so you have to at least cover the cost of your training from a break even point of view over time" — Kurian on inference economics

> "broadrush I think we don't talk about the details so I'm not going to go through every element sure but broadbrush if you look in macro cloud is about half of Alphabet's capital and it's growing because it's growing much faster" — Kurian on Cloud capex share

> "we would not design a model that we couldn't serve and so we're very confident TPUs can serve the largest models in the world" — Kurian on Mythos / 10T-parameter serving capability via disagregated serving
