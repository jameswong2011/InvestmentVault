---
publish: true
date: 2026-04-15
tags: [thesis, enterprise-software, AI, defense, PLTR]
status: active
ticker: PLTR
conviction: high
sector: Enterprise Workflow AI & Automation
source: Consolidated from Gemini Canvas (2), ChatGPT (2), Claude (4), Grok (1) research conversations + web research April 2026
key_metrics_last_refreshed: 2026-08-15
---

# PLTR — Palantir Technologies

## Summary

**Q2 2026 (IR Ex. 99.1, reported 2026-08-03):** Revenue $1.935B (+93% YoY / +19% QoQ); U.S. revenue $1.573B (+115%); U.S. commercial $764M (+149% YoY / +28% QoQ); U.S. government $809M (+90%); Rule of 40 155%; adj. FCF $1.220B (63% margin); U.S. commercial RDV $6.238B (+124% YoY); U.S. commercial TCV record $2.132B (+153% YoY). FY2026 guide raised to $8.150–$8.158B (+82%) and U.S. commercial to >$3.424B (≥134%). NDR was disclosed on the call at 157% (+700bps QoQ from Q1's 150%) — the hard NRR falsifier now sits 37pp above the ~120% break level; customer count 1,049 (+24% YoY). See [[Research/2026-08-12 - PLTR - Q2 2026 Earnings IR Verification]].

Q4 2025: $1.41B revenue (+70% YoY), U.S. commercial +137%, Rule of 40 at 127%. Q1 2026 extended the beat-and-raise — $1.63B revenue (+85% YoY), U.S. revenue +104%, EPS $0.33 — with FY2026 guidance raised to $7.65-7.66B (+71%) and U.S. commercial to +120% (~$4.0B adjusted FCF). Palantir's Ontology architecture — a semantic intelligence layer with governed write-back to operational systems of record — is the critical differentiator. Unlike Databricks/Snowflake (analytical read-path) or ServiceNow (workflow automation), Palantir built the operational write-path first and added the data platform underneath, creating structural advantages in complex, regulated, mission-critical environments. The central tension remains valuation — and the terms have now shifted twice: June 2026's worst month on record took the stock ~46% off the $207.52 ATH to a $106 52-week low, compressing the multiple to ~33x forward revenue at the trough (from ~52-79x trailing at authoring); the Q2 print then round-tripped the de-rate — $174.04 at the 2026-08-14 close (~$400B market cap), +64% off the low, 16% below ATH, and back to ~49x forward revenue on the raised $8.15B guide. Multiple mean-reversion ran both directions around a still-compounding business; of the three structural narratives priced in June (AI-agent / usage-based commoditization; European sovereignty rejections in France and the UK; a US defense CR freeze delaying federal revenue 6-9 months), the defense-freeze leg was contradicted by Q2's +90% U.S. government print while the other two remain live. The defense revenue floor (U.S. government $809M in Q2 alone — $3.2B+ annualized, +90% YoY — anchored by the $10B Army Enterprise Agreement and $1.275B Maven ceiling) still provides downside protection pure-play commercial AI companies lack. See [[Research/2026-06-29 - PLTR - June 2026 Sell-Off Through Mental Models - news]].

---

## Key Non-consensus Insights

- **The Ontology is an operational control plane with write-back capability, not a data analytics tool — and the market still partially prices Palantir as a data analytics company.** An Ontology Action atomically updates objects, writes back to source ERPs (SAP, Oracle), and logs the full decision chain with ACID guarantees and cascading updates. Databricks and Snowflake are architected for OLAP reads and bulk writes — fundamentally different workloads. Databricks' Neon acquisition (Lakebase) reveals it understands this gap but solves at the infrastructure layer rather than the semantic layer, representing a 2-3 year product development gap. Building down from the application layer (Palantir's approach) is architecturally easier than building up from the data platform.

- **The "Context Gap" — not model selection — is the real bottleneck for enterprise AI adoption, and Palantir's Ontology-Augmented Generation (OAG) is architecturally LLM-native in a way no competitor's data model is.** OAG goes beyond RAG by giving LLMs access to deterministic logic tools, structured queries over interconnected business objects, and governed write-back actions — all under the same security policies governing human users. Semantic object types with typed properties and named links map naturally to how language models reason, unlike ServiceNow's procedural GlideRecord patterns that require additional abstraction layers. AI outputs grounded in structured, relationship-aware enterprise data substantially reduce hallucination risk vs flat document retrieval.

- **Palantir and ServiceNow are complementary layers of the enterprise AI stack, not competitors — but the market still prices them as substitutes, understating both companies' addressable markets.** ServiceNow's CMDB maps hierarchical service dependencies for closed-loop IT/HR/security automation; Palantir's Ontology maps dynamic semantic relationships across arbitrary entities for cross-domain reasoning and governed action execution. An AI agent reasoning about incident impact needs a service dependency graph (ServiceNow); an AI agent reasoning about supply chain disruption needs to cross-reference manufacturing defects with supplier contracts with warranty claims across siloed domains (Palantir). Complementary positioning effectively doubles the addressable market relative to a competitive framing.

- **The 5-day AIP bootcamp model is a structural distribution disruption that inverts enterprise software economics — and the market hasn't fully modeled its implications for long-term unit economics.** ~75% conversion rate in 5 days vs traditional 6-18 month sales cycles; documented wins include $26M ACV in five weeks and $19M bank expansion in four months. Walgreens deployed to 4,000 stores in 8 months. Net dollar retention 157% (Q2 2026, +700bps QoQ); U.S. commercial RDV up 124% YoY to $6.238B. Professional services declined from ~25% of revenue (2021) to ~18-20% (2025), with AI-powered FDE agent further reducing human dependency. Still early at 1,049 customers (Q2 2026, +24% YoY) vs Databricks' 20,000+, but the pipeline is compounding.

- **DOGE and Pentagon budget scrutiny are paradoxically bullish for Palantir — the market prices federal spending cuts as a headwind, but budget rationalization systematically benefits AI-native platforms and destroys legacy contractors.** Administration directed 8% annual cuts (~$50B) across Pentagon programs but simultaneously requested a record $1.5T defense budget for 2027. $10B Army Enterprise Agreement consolidated 75 legacy contracts into a single Palantir integration; ShipOS demonstrated 160 manual hours to 10 minutes for submarine schedule planning. Warp Speed (L3Harris, GE Aerospace, Boeing), ShipOS ($448M Navy), NOS (Nuclear OS), and $1.275B Maven ceiling create long-duration revenue decoupled from commercial SaaS cycles. NVIDIA Sovereign AI OS Reference Architecture (March 2026) addresses air-gapped AI needs hyperscalers structurally cannot serve.

## Outstanding Questions

- **At what growth deceleration rate does the current multiple compress faster than earnings grow, creating a negative return even with continued strong execution?** Palantir's trailing P/E of ~135x ($174.04, 2026-08-14) embeds expectations of sustained 50%+ revenue growth for multiple years. Historical precedent for high-growth software companies shows that the transition from 60% growth to 40% growth typically triggers 30-50% multiple compression. The FY2026 guide has been raised twice — 61% → 71% → 82% ($8.15B) — and Q2 accelerated to +93%: the normalization curve has not begun, which sharpens rather than retires the question, because ~49x forward revenue and ~110x FY2026 consensus EPS now re-embed acceleration persisting, so the eventual downshift starts from a higher expectations base. The forward PEG of ~0.8 on FY2026 estimates (~1.8 on FY2027, as the growth denominator halves) is reasonable for current growth, but PEG breaks down when growth decelerates because the denominator shrinks faster than the numerator adjusts.

- **How exposed is Palantir's $3.2B+ annualized government revenue base (Q2 2026 U.S. government: $809M, +90% YoY) to DOGE-driven budget rationalization and shifting political priorities?** The $10B Army Enterprise Agreement and $1.275B Maven ceiling provide contractual anchoring, but shared-savings contract structures (like ShipOS) mean revenue realization depends on demonstrated impact metrics. If the 2027 defense budget request of $1.5T faces Congressional opposition or sequestration risk, what's the impact on new contract velocity vs. existing backlog? Palantir's explicit endorsement of budget scrutiny ("tear up our contracts if they don't deliver value") is strategically astute but untested — what happens when specific programs face actual cuts?

- **Can Palantir solve the international commercial stall that saw revenue decline 10% YoY in Q1 2025?** U.S. commercial is the growth engine (+149% YoY in Q2 2026), but international commercial underperformance suggests the bootcamp model and FDE-intensive go-to-market may face structural friction in non-U.S. markets (regulatory complexity, data sovereignty concerns, cultural resistance to American defense-adjacent software). The NVIDIA Sovereign AI partnership addresses the sovereignty concern for government buyers, but commercial expansion in Europe and Asia requires a different playbook. Is international commercial a "fix it later" problem or a structural ceiling on the total addressable market?

- **Does Palantir's 1,049-customer base (Q2 2026) vs. Databricks' 20,000+ reflect early innings or a structural distribution ceiling imposed by the FDE-intensive model?** Former CFO Colin Anderson acknowledged the FDE model "is only financially sustainable for seven-figure contracts and above." This creates a natural mid-market exclusion zone. The AI FDE agent (natural language Foundry operation) and OSDK (developer self-service) are designed to lower this threshold, but the question is whether the platform complexity inherent in semantic ontology modeling can ever be reduced enough to serve the long tail of enterprises that Databricks/Snowflake/ServiceNow capture. If the answer is no, Palantir's TAM may be structurally smaller than the market assumes — hundreds of billions in defense and complex industrial operations, but not the trillions implied by "enterprise AI OS" positioning.

- **How real is the LLM commoditization threat to the Ontology's value as an orchestration layer?** Open-source models (Llama, Nemotron) now achieve 90%+ of frontier model performance at 84% lower cost. If these models become powerful enough to handle complex, multi-step reasoning without a dedicated ontology — if a sufficiently large context window and a well-constructed prompt can substitute for a structured semantic layer — Palantir's architectural moat narrows. The current evidence suggests the application of the model to messy, real-world data remains a much harder problem than building the model itself, but this assumption requires continuous monitoring. The deeper risk is not that open-source models replicate the Ontology, but that "good enough" semantic layers from Databricks, Microsoft Fabric IQ, or emerging open-source agent frameworks satisfy 80% of enterprise use cases at a fraction of Palantir's cost.

- **Microsoft Fabric IQ directly copies the Ontology concept and was announced in November 2025 — what is the realistic timeline before it becomes production-ready and commoditizes the simpler end of Palantir's commercial market?** Fabric IQ is years from production maturity, but Microsoft's distribution advantage (ubiquitous enterprise relationships, bundled pricing, developer ecosystem) means even a "good enough" semantic layer embedded in the M365/Azure stack could intercept Palantir's commercial land-and-expand at the mid-market tier. Every seam between Microsoft products (SQL Server, Cosmos DB, Dataverse, Power Automate, Fabric IQ) is a place where consistency guarantees break, audit trails fragment, and latency accumulates — but enterprises embedded in the Microsoft ecosystem may accept this friction for the simplicity of a single vendor. This is the "good enough" risk in its most potent form.

- **What does the persistent insider selling pace (~$6M/day in early 2026) signal about management's private assessment of valuation?** Almost all sales occur under pre-scheduled Rule 10b5-1 plans, which structurally reduces the information content of each transaction. But the aggregate pace — $6M daily despite record revenue and earnings — creates persistent technical supply pressure. Institutional accumulation is partly offsetting this (JP Morgan +183%, Vanguard +4%, BlackRock +5%), but the insider/institutional divergence warrants monitoring. The question is whether this represents rational diversification by founders with concentrated positions or a subtle signal about growth sustainability at current multiples.

- **How severe is the customer concentration risk from the top-20 customers generating $124M average TTM revenue each (Q2 2026 10-Q, +67% YoY)?** At ~$6.2B TTM revenue, the top-20 contribute roughly $2.5B or ~40% of total revenue. A single customer loss at this tier would represent a ~$124M revenue hit (~2% of total), but the guidance revision and market reaction would be disproportionate. The bootcamp-driven expansion of the customer base (1,049 total, +24% YoY) is the structural remedy, and the ratio of top-20 revenue to total revenue is the metric to watch — the tail is growing faster than the head for the first time (top-20 TTM +67% vs company +93%), early evidence of diversification but not yet a trend.

## Business Model & Product Description

### The Conceptual Architecture: Nervous System, Not Brain

The simplest analogy for Palantir's business is that it is the enterprise nervous system — the connective tissue between the AI brain (LLMs, which any company can access) and the enterprise body (operational systems like ERPs, industrial controls, logistics networks, and weapons systems). Databricks and Snowflake are the skeletal system — they store and organize data. ServiceNow is the circulatory system — it delivers workflow oxygen to every department. But neither the skeleton nor the circulatory system can sense, decide, and act in real-time across the whole organism. That is the nervous system's job, and it is what Palantir's Ontology provides.

This distinction matters commercially because it means Palantir is complementary to — not competitive with — the major enterprise platforms. Palantir runs on top of Snowflake, Databricks, AWS, Azure, and GCP data stores. It integrates with ServiceNow, SAP, and Oracle workflows. It deploys on NVIDIA infrastructure. It is model-agnostic, supporting GPT, Claude, Gemini, Llama, and Nemotron. The Ontology is the semantic layer that makes all of these components work together for operational decision-making.

### Product Architecture

Palantir's product stack operates in five layers:

**1. Foundry** — The data integration and transformation platform. Foundry ingests data from any source (ERPs, sensors, databases, documents, APIs), transforms it through configurable pipelines (batch or streaming), and stores it in an immutable, versioned data layer (Parquet/Iceberg). Foundry is the "data operating system" — it handles the messy, unglamorous work of cleaning, joining, and governing enterprise data. The Pipeline Builder supports incremental execution to prevent expensive full-dataset reprocessing.

**2. Ontology** — The semantic intelligence layer. The Ontology sits atop Foundry datasets and translates raw data into business-meaningful objects (a Transformer, an Aircraft, a Patient, a Shipment) with typed properties and named relationships. Objects are connected through dynamic semantic links, not hierarchical dependencies, enabling complex cross-domain reasoning. The Ontology uses a Multimodal Data Plane (MMDP) to coordinate read and write operations across heterogeneous infrastructure without requiring massive data replication. OSv2 supports indexing tens of billions of objects per type.

**3. AIP (Artificial Intelligence Platform)** — The AI application layer. AIP provides the tools for building, deploying, and governing AI agents on top of the Ontology. Key components include:
- **AIP Logic**: No-code LLM-powered function builder using Ontology objects as inputs
- **AIP Agent Studio**: Build conversational AI agents powered by any major LLM combined with Ontology context, document context, and custom function-backed context
- **AIP Evals**: Integrated framework for testing agent performance across models and scenarios
- **AIP Document Intelligence**: Advanced chunking and embedding strategies for RAG workflows, using vision-language models and Markdown-optimized chunking for unstructured documents (PDFs, emails, spreadsheets)
- **AI FDE**: Natural language interface for Foundry, converting conversational intent into data transformations, code repository management, and ontology building — effectively an AI-powered Forward Deployed Engineer

**4. Apollo** — The autonomous deployment layer. Apollo allows Palantir software to run in any environment — public cloud, private cloud, air-gapped, classified, or edge — with average patch time of 3.5 minutes. This is the key enabler for defense and sovereign AI deployments where cloud connectivity is either impossible or prohibited.

**5. Rubix** — A hardened, zero-trust Kubernetes substrate for managing compute resources in on-premises deployments. Combined with Apollo, Rubix enables the turnkey AI datacenter architecture that underpins the NVIDIA Sovereign AI OS Reference Architecture.

### Revenue Segmentation

Palantir's revenue divides into four segments with dramatically different growth trajectories:

| Segment | Q4 2025 | YoY Growth | FY2026 Guidance | Character |
|---------|---------|------------|-----------------|-----------|
| **U.S. Commercial** | $507M | +137% | >$3.424B (≥134%) | Hypergrowth engine; AIP bootcamp-driven |
| **U.S. Government** | $570M | +66% | Not disclosed | Structural floor; Army EA + Maven + ShipOS |
| **International Commercial** | Est. ~$150M | Stalled/declining | Not disclosed | Key concern; growth friction outside U.S. |
| **International Government** | Est. ~$180M | Moderate | Not disclosed | NATO Maven + sovereign AI expanding |

The U.S. business surpassed $1B for the first time in Q4, growing 93% YoY and 22% sequentially. The asymmetry between U.S. commercial hypergrowth and international commercial stagnation is the most important segmental dynamic to monitor.

A novel way to segment the revenue is by contract durability:

- **Structural floor (~35-40%)**: Long-duration government contracts with multi-year or decade-scale terms — $10B Army Enterprise Agreement, $1.275B Maven ceiling, $448M ShipOS, £240.6M UK MoD (sole-source). These are quasi-annuity revenue streams with near-zero churn risk and expansion built into contract ceilings.
- **High-growth engine (~40-45%)**: AIP bootcamp-driven commercial revenue with 75% conversion, 157% NDR (Q2 2026), and $6.238B U.S. commercial RDV pipeline. This is where growth comes from, but also where volatility lives.
- **Strategic investments (~15-20%)**: Vertical-specific deployments (Warp Speed manufacturing, NOS nuclear, Mortgage OS financial services) and international expansion efforts. These are lower-revenue but high-optionality bets that could become the next growth engine.

### Go-to-Market Model

Palantir's go-to-market operates through three channels:

**AIP Bootcamps**: 5-day intensive workshops where customers build production-grade AI use cases on their own data. ~75% conversion rate. Over 1,300 completed by late 2024 and continuing to scale. This is the primary commercial growth driver and the mechanism that compressed sales cycles from months to days.

**Forward Deployed Engineers (FDEs)**: Full-stack software engineers embedded in customer environments who build production systems, identify patterns, and feed abstractions back into the platform. FDEs are best understood as a distribution strategy disguised as services — they create operational lock-in and drive NDR of 157% (Q2 2026). The model is "only financially sustainable for seven-figure contracts and above" (former CFO Colin Anderson), which creates a natural mid-market exclusion zone that limits customer count but maximizes revenue per customer.

**OSDK (Ontology Software Development Kit)**: Auto-generated TypeScript, Python, and Java bindings that enable developers to build applications directly on top of the Ontology. This is the self-service channel designed to reduce FDE dependency and enable platform adoption beyond the bootcamp-converted customer base.

### Revenue Model

Revenue is primarily software subscriptions with a declining professional services component (from ~25% of revenue in 2021 to ~18-20% in 2025). The subscription model includes annual escalators and is increasingly consumption-based for AIP workloads. The joint venture strategy (Syndicate 2479 in re-insurance, Aither in software development, TWG Global, Knox in IT consulting) allows Palantir to embed its software in new industries while sharing operational risk with domain experts — an asset-light expansion model that complements the FDE-intensive direct sales approach.

## Industry Context

### The Enterprise AI Platform Landscape: A Three-Front War

> [!question] 2026-04-27 → Addressed 2026-04-27
> **Prompt:** *Why are competitors unable to clone Palantir's technology especially its ontology and writeback functionalities. Is this due to patent protection? If so, whats the duration.*
>
> **Response:** Patent protection is the weakest layer of the moat — Palantir's foundational Foundry/Ontology architecture patents (filed circa 2010-2015) carry a 20-year statutory term and expire 2030-2035, but software patents have narrow claims that competitors routinely engineer around. The real replication barriers are structural: architectural inversion (top-down vs bottom-up build), MMDP atomic write-back across heterogeneous source systems, the customer-flywheel ontology library, security certifications (DoD IL6, FedRAMP High, Apollo air-gapped deployment), and FDE talent — none patent-dependent, all compound with every deployment. See §Industry Context → Why the Ontology Resists Replication for full analysis.

Palantir is fighting a competitive war on three distinct fronts, each with different dynamics and different competitive advantages:

**Front 1: The "Build Your Own" Threat (Databricks, Snowflake).** Databricks is the most credible threat to Palantir's commercial ambitions, and the competitive picture moved materially in mid-2026. Databricks reached a **$6.9B annualized run-rate (+80% YoY, June 2026, up from $5.4B / +65% in January)**, is raising at a **$165-175B valuation** (from $134B), and its AI product line hit a **$1.4B run-rate (~25% of total revenue, on track to be the majority within 2-3 years)**. At its June 2026 Data + AI Summit it stopped positioning as a data platform and reframed the lakehouse as an **"agentic enterprise control plane"** — a four-layer stack (live data: Lakebase / Lakehouse//RT / Lakeflow; **context: "Genie Ontology" + Unity Catalog**; execution: Agent Bricks / Genie One / Omnigent; runtime governance: Unity AI Gateway / Lakewatch) that deliberately mirrors Palantir's Foundry→Ontology→AIP→governance architecture. **Agent Bricks has built 100,000+ agents processing 1+ quadrillion tokens/year** (AstraZeneca, 7-Eleven, Fox, Block), and Databricks now sells Palantir's own thesis back to the market: *"the company with the best context layer will have a larger AI advantage than the company with the most data."* **This is the single most important competitive update since the thesis was authored: the semantic/context-layer gap bulls priced at "2-3 years" has narrowed to months** — Genie Ontology is GA, branded, and adopted by marquee enterprises. What has *not* closed is the operational layer: Bain's summit review notes Databricks showed "no explicit write-back or operational action examples beyond abstract workflow triggering," and its agent "action" remains code-execution-in-a-sandbox with Unity Catalog access-downscoping, not governed atomic write-back to source ERPs with cross-object ACID guarantees. Lakebase (Postgres via Neon) persists agent state but has no awareness of business objects, relationships, or domain rules — the write-path/read-path architectural line from [[Research/2026-03-31 - Databricks Threat to Palantir]] holds, because governed transactional write-back is a distributed-systems problem that neither better models nor a shipped semantic layer solve. The Databricks-Palantir partnership (100+ joint customers within seven months) still signals a "best-of-both" market: Databricks' open data + semantics, Palantir's operational/action layer + certified deployment; Snowflake's native-AIP integration reinforces the same structure. **Net: Databricks closed the context gap and remains structurally behind on governed action and defense — the moat compressed at the simple/analytical end and held at the operational/regulated end.**

**Front 2: The Ecosystem Play (Microsoft, AWS, Google).** Hyperscalers use their ubiquity to offer "good enough" analytics that come practically free with existing cloud contracts. Microsoft's Fabric IQ, announced November 2025, directly copies the Ontology concept but is years from production maturity. Wiring a Fabric IQ ontology entity to a Power Automate flow that validates business rules and writes back to Dynamics 365 is technically possible today — but it is a multi-product integration exercise, not a single-platform atomic operation. Every seam between products is a place where consistency guarantees break. Microsoft's distribution advantage (M365/Azure relationships across most enterprises) means even a "good enough" semantic layer could intercept Palantir's mid-market expansion. AWS and Google compete less directly — their AI offerings (Bedrock, Vertex) focus on model serving and inference rather than operational decision-making. The key risk is not that Microsoft builds a perfect Ontology replica — they won't need to. The risk is that "good enough" satisfies 80% of use cases at a fraction of Palantir's cost.

**Front 3: The Defense/Government Moat (No viable competitor at scale).** In classified, air-gapped, and sovereign environments, Palantir has no peer. The company holds DoD Impact Level 6 provisional authorization (one of only six cloud providers), FedRAMP High baseline, CMMC Level 2 certification, and the ability to deploy in fully air-gapped environments through Apollo. The $10B Army Enterprise Agreement consolidates 75 existing contracts. Maven Smart System ($1.275B ceiling) has 20,000+ active users across 35+ military entities in three security domains. TITAN — where Palantir is the first software company to serve as primary contractor on a major hardware program — delivered its first two prototypes on time and on budget. NATO adopted Maven in "one of the most expeditious" acquisitions in its history. The UK MoD awarded £240.6M without competitive tender. These certifications and operational dependencies took 20+ years and hundreds of millions of dollars to build. In classified environments, switching providers is virtually impossible due to security certification requirements, training dependencies, and operational continuity needs.

### Model Evolution and the Viability of Agentic Workloads (2024 → mid-2026)

Whether recent model evolution made agentic workloads viable — and whether that helps or hurts Palantir — resolves to the mental-models crux (Value-Layer-Monopoly §3, Automation-Lens §7): does cheap, capable intelligence make Palantir's curated context layer *more* necessary (infrastructure, moat-widening) or *optional* (application, moat-dissolving)? The mid-2026 evidence splits the answer by workload difficulty, and that split maps directly onto the bull/bear divide.

**What model evolution delivered by mid-2026 (viability up).** Reasoning-RL models (the o-series, the DeepSeek R1 lineage, extended-thinking Claude/Gemini) crossed the single-shot enterprise-usefulness threshold: leading agentic models now score **95%+ on function-calling reliability (IFBench)**, and evaluation itself migrated from academic benchmarks (MMLU) to agentic ones — **Terminal-Bench Hard, τ²-Bench (enterprise tool use), IFBench**. Inference cost fell **~67% per model generation**, and open-source models (Llama 4, Qwen, DeepSeek) reached rough frontier parity, making model selection **orthogonal to platform selection**. Workflows that were research demos in 2024 are production-deployable in 2026. This is unambiguously TAM-expansionary for a model-agnostic deployment layer: AIP routes any of GPT/Claude/Gemini/Llama/Nemotron, so cheaper and better models lower the cost of every agent *deployed on Palantir* and enlarge the set of automatable workflows. Frontier-lab insiders frame the agent moat itself as **"meticulously orchestrated context," not model weights** ([[Research/2026-04-24 - Luo Fuli on OpenClaw and Agent-Era Compute Reallocation - video-transcript]]) — a direct validation of the Ontology-as-context-substrate thesis.

**What model evolution did not deliver (the reliability gap that preserves the premium).** Enterprise-grade agentic reliability remains the binding constraint, and it is not a model-capability problem that scale closes:

| Failure mode | mid-2026 datapoint | Implication |
|---|---|---|
| Lab-vs-production gap | ~37% drop from benchmark score to real deployment | Capability ≠ deployability |
| Consistency across runs | 60% single-run → **25% at 8-run consistency** | Non-determinism is fatal for mission-critical action |
| Cost variance | ~50x spread for equal accuracy | ROI needs governed routing, not raw model access |
| Multi-agent coordination | errors amplify ~10x; O(n²) coordination; 30-35% multi-step completion | Orchestration/governance is the value, not the agent |
| Code safety | 45% of AI-generated code carries vulnerabilities | Human-in-the-loop + audit are non-negotiable |

These are exactly the conditions under which the deterministic-tools + typed-objects + governed-write-back + causal-lineage substrate earns its premium: the model got smarter; the *system around the model* is still where production reliability comes from. Gartner's forecast that **40% of agentic-AI projects will be cancelled by 2027** is a demand signal for the grounding/governance layer, not against the category — and consistent with the bounded-disruption framing in [[Research/2026-04-14 - NOW - AI Disruption Risk - deep-dive]].

**The kill-switch has not fired (long context is a "trap").** The single most-watched falsification trigger (Automation-Lens §7) is whether context windows become large-and-cheap enough that curated ontologies become optional. Mid-2026 data cuts the other way: for enterprise synthesis, structured retrieval is **~67% more accurate, ~8x lower latency, and up to ~1,250x cheaper per query** than stuffing a 1M-token window, and enterprise agent queries consume **50,000-100,000 tokens on schema, lineage, and governance policy before the model reasons at all**. Bigger context does not replace a governed semantic layer — it *raises* the value of deciding what trustworthy, policy-compliant context to place in the window. The Ontology is that decision, made once and reused across agents. That **Databricks, Microsoft, ServiceNow, and Salesforce all converged on the identical "context is the moat" framing in 2026 confirms the thesis mechanism even as it commoditizes the label.**

**Where this leaves Palantir (the balanced read, held as hypothesis-to-test).** Model evolution is **net-positive for the hard end and net-negative for the simple end** of Palantir's market — the infrastructure-vs-application split running straight through the company:
- *Widening (infrastructure-like):* operational write-back, air-gapped/IL6/FedRAMP-certified deployment, multi-domain cross-system reasoning, decision-level audit. Better and cheaper models make these workloads *more* deployable while none of the model advances close the distributed-systems or certification gaps competitors face. Palantir's U.S. commercial **+149% (Q2 2026)** and the U.S. government floor sit here.
- *Contesting (application-like):* single-domain analytics, document-QA, and mid-market semantic modeling, where Databricks' Genie Ontology, Microsoft Fabric IQ, and vertical agents now offer "good enough" at lower cost.
- *The genuinely new threat vector is not Databricks but the frontier labs going direct* — Anthropic/OpenAI enterprise GTM, where better models make thinner integration layers viable and intercept first-time AI budgets (the live driver of the June 2026 sell-off's commoditization narrative, per [[Research/2026-06-29 - PLTR - June 2026 Sell-Off Through Mental Models - news]]). Karp's "tokenmaxxing" rebuttal — labs burn tokens but "implementation is where the value is," and "most of Anthropic's public projects run on Palantir" ([[Research/2026-06-11 - PLTR - Karp on Frontier Lab Discontent - news]]) — is the bull rejoinder, but from a self-serving, unverified source.

Per the READING PROTOCOL, the falsifying datapoint to monitor is unchanged and **has not fired**: a U.S.-commercial NRR break below ~120%, or a *named* mid-market displacement to Genie Ontology / Fabric IQ / a frontier-lab-direct deal. Genie Ontology's marquee logos (AstraZeneca, Block) are the closest yet — none is a disclosed Palantir loss, but they are the population from which the first falsifying datapoint would come. Full analysis: [[Research/2026-07-09 - PLTR - Model Evolution and Agentic Workload Viability Deep Dive]].

### Why the Ontology Resists Replication: Structural Moats vs. Patent Protection

Patent protection is the weakest layer of the moat. Palantir holds an extensive patent portfolio covering specific implementations of Foundry, Ontology, and AIP, but software patents have narrow claims that competitors routinely engineer around — the foundational architecture patents (filed circa 2010-2015) carry a 20-year statutory term and expire 2030-2035, by which time the structural barriers below will have compounded enough that legal protection is irrelevant to thesis-relevant horizons. The replication barriers are architectural and operational, not legal:

**1. Architectural inversion.** Palantir built top-down — operational decision-making first (intelligence, counter-terrorism, and fraud-detection workflows from 2003 onward), then the data infrastructure underneath. Competitors built bottom-up: Databricks started with Apache Spark (data engineering), Snowflake with cloud data warehouse (analytical reads), ServiceNow with ITSM workflows (procedural automation). Inverting the stack requires rebuilding foundational layers, not bolting capabilities on top. Databricks' Lakebase (Postgres for transactional state) and Unity Catalog (governance metadata) are credible bottom-up attempts but represent a 2-3 year product gap precisely because they add operational capabilities onto an analytical core rather than rebuilding from the operational layer outward.

**2. Multimodal Data Plane (MMDP) and atomic write-back.** An Ontology Action atomically updates objects, writes back to source systems of record (SAP, Oracle, custom ERPs), and logs the decision chain — with ACID guarantees across heterogeneous infrastructure. Each source system has different APIs, consistency models, and failure semantics; achieving atomic, governed write-back requires custom integrations with hundreds of source systems, a distributed rules engine that reconciles business logic across them, and two-phase commit-style coordination across systems that don't natively support it. Databricks' Lakebase gives agents a place to persist state, but it remains a Postgres instance with no semantic awareness of business objects or cross-system rules — the bridge from "fast transactional database" to "governed semantic action layer" is not a patentable feature, it is a decade of distributed-systems engineering.

**3. Customer-data flywheel and ontology library.** 20+ years of FDE deployments in classified, manufacturing, healthcare, and financial-services environments produced an institutional library of pre-built object types and relationships — defense logistics ontologies, pharmaceutical supply chain ontologies, naval shipyard ontologies, fraud-detection ontologies. Competitors don't have these. Even if Microsoft Fabric IQ achieves technical parity with the Ontology architecture, it lacks the domain-specific semantic models that took thousands of FDE-years to build. This is the moat that widens with every customer deployment and is impossible to replicate via legal IP — domain knowledge embedded in production ontologies is trade secret, not patent.

**4. Security certifications and air-gapped deployment.** DoD Impact Level 6 provisional authorization (one of six cloud providers), FedRAMP High baseline, CMMC Level 2, and the Apollo deployment system enabling air-gapped execution with 3.5-minute average patch times. These certifications take 5-10 years and tens of millions of dollars to obtain — they are not patent-protected but are practically replication-proof on relevant timescales. Databricks holds none, Snowflake holds none, Microsoft has Azure Government but nothing comparable to Apollo's edge/classified deployment capability. A competitor starting the IL6 process today would not reach parity until 2032+.

**5. FDE talent and engineering culture.** The Forward Deployed Engineer model — full-stack engineers embedded in customer environments who build production systems and feed abstractions back to the platform — has been refined over two decades. The talent pool that can do this work is small, and Palantir has trained the largest cohort. Competitors hiring senior FDEs face non-competes, and inheriting individual engineers does not transfer the institutional patterns (project structuring, abstraction harvesting, ontology design heuristics) that make the model financially viable at $1M+ ACVs.

**Patent duration is not the binding constraint.** The relevant question is not when Palantir's 2010-2015 architecture patents expire, but whether the structural moats degrade faster than competitor execution closes the gap. The Databricks-Palantir partnership (100+ joint customers within seven months of announcement) and the Snowflake native AIP integration suggest the market is converging on a "best of both" model — open data layer + proprietary semantic/operational layer — which preserves Palantir's competitive positioning even as the build-your-own narrative loses steam. The moats to monitor are not legal but operational: erosion in NRR (157% as of Q2 2026), customer count growth versus Databricks (1,049 vs 20,000+), and any successful Microsoft Fabric IQ commercial wins at the mid-market tier.

### Value Chain Positioning

The enterprise AI value chain can be decomposed into four layers:

| Layer | Function | Key Players | Palantir's Position |
|-------|----------|-------------|---------------------|
| **Infrastructure** | Compute, storage, networking | NVIDIA, AWS, Azure, GCP | Consumer (runs on all); NVIDIA partnership for sovereign |
| **Data Platform** | Data storage, transformation, governance | Databricks, Snowflake, Microsoft Fabric | Sits atop all; Foundry integrates via MMDP |
| **Semantic/Intelligence** | Object modeling, AI reasoning, decision logic | **Palantir (Ontology + AIP)** | **Core competitive position** |
| **Workflow/Action** | Process automation, task management | ServiceNow, Salesforce | Complementary; Ontology feeds into workflow systems |

Palantir occupies the semantic/intelligence layer — the layer that translates raw data into business-meaningful context and enables AI-driven decisions that write back to operational systems. This is the highest-value layer because it is where data becomes actionable intelligence, and it is the layer with the fewest credible competitors. The key architectural moat is that Palantir built its platform from the top down (starting with operational decision-making and adding data infrastructure underneath), while every competitor is building from the bottom up (starting with data platforms and trying to add operational capabilities on top).

### Competitive Differentiation by Dimension

| Capability | Palantir | Databricks | Microsoft Fabric IQ | ServiceNow |
|-----------|----------|------------|---------------------|------------|
| Semantic object modeling | **Native (Ontology)** | **Genie Ontology + Unity Catalog (GA 2026)** | Preview (announced Nov 2025) | CMDB (hierarchical CIs) |
| Write-back to operational systems | **Full (Actions → ERP/SAP)** | Lakebase (Postgres, no semantic awareness) | Multi-product integration | RaptorDB (transactional ITSM) |
| AI agent orchestration | **AIP Agent Studio + Evals** | Agent Bricks + Omnigent (100k+ agents) | Copilot agents (early) | Now Assist + AI Agent Fabric |
| Classified/air-gapped deployment | **Apollo + Rubix (IL6, FedRAMP)** | None | Azure Gov (limited) | Cloud-only (excluded) |
| Scale (objects/entities) | **Tens of billions per type** | Petabytes of data (different metric) | Large (unclear semantic scale) | 1-7M CIs (degrades >2.3M) |
| Customer base | 1,049 | 20,000+ | Millions (M365) | 8,200+ (85% of Fortune 500) |
| Go-to-market model | Bootcamps + FDEs | Self-service + partners | Bundled with M365/Azure | Multi-year roadmaps + partners |
| Token efficiency for LLMs | **High (typed objects, named links)** | Moderate (tabular, schema-on-read) | Unknown | Low (GlideRecord → SELECT *) |

### Key Market Dynamics

The enterprise AI market is evolving toward **multi-vendor strategies** rather than single-platform dominance. Organizations are adopting Palantir for core intelligence work (complex, cross-domain, regulated), Databricks or Snowflake for general analytics and data engineering, ServiceNow for workflow automation and IT operations, and Microsoft for productivity and collaboration. This fragmentation benefits Palantir's positioning as the semantic/intelligence layer that connects all other platforms, but it also limits Palantir's ability to capture the full enterprise AI wallet. The partnership approach (Databricks 100+ joint customers, Snowflake native integration, NVIDIA sovereign AI architecture) reflects a strategic acceptance of this market structure — Palantir wins by being the indispensable layer, not by replacing everything else.

The governance dimension is becoming increasingly decisive. As AI regulation fragments (the 10-year federal moratorium on state AI laws was stripped by a 99-1 Senate vote in July 2025, leaving a patchwork of state rules), enterprises need platforms with built-in compliance tooling. Palantir's "causal lineage" — the ability to trace every AI agent action back to specific data, logic, and governance rules — was originally designed for classified defense environments but is becoming a commercial differentiator as state-level AI laws proliferate. Competitors without built-in compliance architecture face rising friction costs that widen Palantir's moat incrementally with each new regulation.

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | ~$400B | Mid-April 2026; volatile (tariff/DOGE sell-off from $207 ATH) |
| Share Price | $174.04 | Closed $148.46 Apr 3; declined since; highly volatile |
| EV/Revenue (trailing) | ~64.6x | On FY2025 $4.48B; depends on recent price |
| EV/Revenue (forward) | ~49x | On FY2026 guide $7.19B |
| Revenue Growth | +93% YoY (Q2) / +71% prior FY guide → +82% FY26 guide | Q2 2026 actual +93% YoY to $1.935B; FY26 guide raised to $8.150–$8.158B (+82%) |
| Gross Margin | ~84.7% | Q2 2026 (gross profit $1.639B / rev $1.935B) |
| GAAP Operating Margin | 47% | Q2 2026 ($912M income from ops) |
| Adj. Operating Margin | 62% | Q2 2026 ($1.194B adj income from ops) |
| FCF Yield (trailing) | ~0.8% | FY2025 FCF >$2.2B / market cap |
| FCF Yield (forward) | ~1.1-1.2% | FY2026 FCF guide $4.025B / market cap |
| Q4 2025 Revenue | $1.41B | +70% YoY; beat high-end guidance by 900+ bps |
| Q2 2026 Revenue (actual) | $1.935B | +93% YoY / +19% QoQ (IR Ex. 99.1, 2026-08-03); prior Q1 was $1.63B (+85%) |
| FY2026 Revenue Guidance | $8.150–$8.158B | +82% YoY (raised at Q2 from ~$7.65–7.66B / +71%) |
| FY2026 U.S. Commercial Guide | >$3.424B (≥134% YoY) | Raised at Q2 (prior >$3.224B / +120%) |
| FY2026 Adj. FCF Guidance | $4.5–$4.7B | Raised at Q2 (prior $4.025B) |
| Rule of 40 | 155% | Q2 2026 (rev growth + adj op margin); 12th consecutive expanding print |
| Customer Count | 1,049 | +34% YoY |
| U.S. Commercial RDV | $6.238B | +124% YoY / +27% QoQ (Q2); prior $4.38B (+145% at earlier pass) |
| Net Revenue Retention | 157% | Strong expansion within existing customers |
| Bootcamp Conversion | ~75% | 5-day cycle; $1M+ average deal size |
| Top 20 Customer Avg Rev | $124M | Concentration risk (~42% of revenue) |
| Forward PEG | ~0.8-1.8 | At recent prices; vs SNOW at 3.3x |
| Analyst Consensus | Moderate Buy | Median target ~$197; range $70-$255 |
| Insider Selling Pace | ~$6M/day | Rule 10b5-1 plans; persistent technical supply |

## Bull Case

- **AI adoption is still early innings**: AIP bootcamp flywheel accelerates into 2027+ as the ~75% conversion rate compounds against a growing pipeline; $6.238B U.S. commercial RDV (+124% YoY, Q2 2026) provides multi-year visibility
- **Sovereign AI becomes standard for NATO nations**: The NVIDIA partnership (Blackwell Ultra + Rubix + Apollo + AIP) opens a massive government TAM currently dominated by legacy defense IT that cannot deploy AI in classified environments
- **U.S. commercial sustains 100%+ growth**: Ontology becomes the de facto enterprise AI deployment architecture; customer base grows from 1,049 toward 2,000+ as AI FDE and OSDK lower the adoption threshold
- **Defense revenue floor provides downside protection**: $10B Army EA + $1.275B Maven + $448M ShipOS + NATO + UK MoD create an annuity-like base now running $3.2B+ annualized (Q2 U.S. government: $809M, +90% YoY) that pure-play commercial AI companies lack
- **DOGE reshuffles defense IT spending in Palantir's favor**: Budget scrutiny eliminates legacy contractors; Palantir's demonstrated ROI metrics (160 hrs → 10 min at Electric Boat) make it the winner of every cost-benefit analysis
- **Warp Speed and ShipOS create a new "Industrial OS" category**: Manufacturing MES + supply chain + naval production worth tens of billions in TAM; early wins with L3Harris, GE Aerospace, Boeing, Lear validate the category
- **Forward PEG at recent prices (~0.8-1.8) is cheaper than Snowflake (3.3x)**: Growth-adjusted valuation is reasonable relative to enterprise software peers; any acceleration in commercial revenue would compress PEG further
- **Complementary positioning with ServiceNow expands addressable market**: Market re-rates from "competitive" to "complementary" framing, benefiting both companies
- **Price target range**: Consensus ~$192 (Moderate Buy, 21 analysts) — only ~10% above the $174.04 tape after the +64% rebound, so the Street no longer underwrites material upside from here; post-Q2 raises: Citi $245, Phillip Securities $215, DA Davidson $200; high $255

## Bear Case

- **Extreme valuation requires near-perfect execution**: The June correction has fully round-tripped — at $174.04 (2026-08-14) trailing P/E is ~135x and EV/revenue ~65x trailing / ~49x forward — leaving little room for growth deceleration, margin compression, or guidance misses; any quarter of sub-50% revenue growth likely triggers severe multiple compression
- **The June 2026 sell-off proves the valuation risk is not hypothetical**: a Q1 beat-and-raise (+85% revenue, U.S. revenue +104%) still produced the worst month on record (~−25-30%, fresh $106 low) because the multiple — not the business — was the position; the post-Q2 rebound to ~$400B rebuilt the same multiple-hostage exposure at ~49x forward. Three structural bear narratives crystallized at once: European sovereignty rejections (France→ChapsVision; UK NHS Feb-2027 break-clause pressure + blocked £50M Met Police deal), the AI-agent / usage-based commoditization story (Anthropic winning first-time enterprise deals; Burry puts), and a US defense CR freeze delaying federal revenue 6-9 months. See [[Research/2026-06-29 - PLTR - June 2026 Sell-Off Through Mental Models - news]]
- **Insider selling at ~$6M/day creates persistent downward pressure**: Scheduled or not, the aggregate selling pace exceeds institutional accumulation and creates a technical headwind that amplifies any fundamental weakness
- **Customer concentration risk is acute**: Top-20 customers generate ~40% of TTM revenue ($124M average each, Q2 2026 10-Q); a single loss in this tier would not only impact financials but erode the "N of 1" narrative
- **LLM commoditization narrows the Ontology moat over time**: Open-source models at 90%+ of frontier performance + "good enough" semantic layers from Databricks/Microsoft Fabric IQ could satisfy 80% of commercial use cases at a fraction of Palantir's cost, limiting TAM to the complex/regulated/defense niche
- **International commercial stall may be structural**: -10% YoY international commercial growth (Q1 2025) suggests the bootcamp model and defense-adjacent brand carry material friction outside the U.S.; geopolitical exposure (IDF contracts, NHS controversy) limits European expansion
- **SBC dilution erodes per-share value**: $1.57B in FY2025 stock-based compensation was ~35% of that year's revenue, but the argument is fading as revenue outruns grants — TTM SBC/revenue is ~14% (FMP) and the GAAP vs. adjusted margin divergence narrowed to 47% vs 62% (Q2 2026)
- **1,049 customers vs. 20,000+ for Databricks**: Distribution ceiling imposed by FDE model may be structural rather than temporary; the long tail of enterprise AI spend may never be addressable at Palantir's price point
- **Price risk**: The June support map ($95-100, capitulation below $90) now sits ~45% under the $174.04 tape; nearest technical references are the 200-day (~$152) and 50-day (~$135) averages — the live risk is a rerun of June-scale multiple compression from a higher base, and the stock has already shown it can lose ~46% in a month without a fundamental break

## Catalysts

- **Q2 2026 earnings** (reported 2026-08-03): confirmed beat-and-raise — $1.935B (+93%), U.S. commercial +149%, FY26 guide to $8.150–$8.158B (+82%), U.S. commercial guide ≥134%. **Q2 held the tape** — +37% from mid-July ($126.79) to $174.04 by Aug 14, breaking the June pattern; **next test is Q3 2026** guide $2.160–$2.164B. Q1 context: $1.63B (+85%), then June multiple stress-test
- **NVIDIA Sovereign AI OS deployments ramping through 2026**: First production installations in NATO allies and Five Eyes nations could unlock large new government contracts
- **ShipOS expansion beyond initial $448M**: Success at General Dynamics Electric Boat creates a playbook for the broader maritime industrial base and defense prime contractors
- **Warp Speed adoption by additional industrial enterprises**: Manufacturing MES deployments at GE Aerospace, Boeing, Lear expanding into broader industrial categories
- **AI FDE general availability**: Democratizes Foundry operation via natural language; if successful, addresses the distribution ceiling concern by reducing FDE dependency
- **FY2026 U.S. commercial revenue exceeding $3.424B guide** (≥134% YoY): Continued acceleration would force the market to price sustained hypergrowth rather than deceleration
- **International commercial inflection**: Any evidence of bootcamp success outside the U.S. would address the most significant growth concern
- **S&P 500 weight increase**: Continued market cap growth drives passive index buying
- **Potential DOGE-driven defense contract wins**: Legacy contractor displacement flowing to AI-native platforms

## Risks

1. **Valuation risk**: Extreme multiples require sustained hyper-growth; any quarter of sub-50% revenue growth triggers disproportionate drawdown. June 2026's ~46% drawdown — and its +64% round-trip by mid-August — demonstrates this dynamic runs in both directions.
2. **Insider selling**: ~$6M/day selling pace despite record fundamentals creates persistent technical headwind and raises questions about management's private valuation assessment
3. **Customer concentration**: Top-20 customers at $124M average TTM each (~40% of TTM revenue, Q2 2026 10-Q); a single loss materially impacts guidance and narrative
4. **LLM commoditization / "good enough" threat**: Databricks' Lakebase + Agent Bricks, Microsoft Fabric IQ, and open-source agent frameworks could commoditize the simpler commercial end of Palantir's market within 2-3 years
5. **Geopolitical/reputational risk**: IDF contracts and NHS controversy create brand liability in European commercial markets; "defense-adjacent" positioning limits TAM in ESG-sensitive sectors
6. **SBC dilution**: $1.57B in FY2025 (~35% of revenue) but ~14% of TTM revenue as growth outran grants; GAAP operating margin of 47% vs adjusted 62% (Q2 2026) reflects the remaining economic dilution
7. **International commercial stagnation**: -10% YoY growth suggests structural friction, not temporary headwinds
8. **DOGE/federal budget risk**: Despite structural benefits, near-term Pentagon program cuts could create revenue gaps before defense budget growth materializes in 2027-2028
9. **FDE model scalability**: 1,049 customers vs. 20,000+ peers; AI FDE and OSDK are designed to address this but remain unproven at scale
10. **Macro/tariff risk**: Broad market sell-off driven by trade war escalation compresses all growth multiples regardless of company-specific fundamentals

## Conviction Triggers

> Formalized 2026-08-12 from the bull vs bear debate ([[Research/2026-08-12 - PLTR - Bull vs Bear Debate Synthesis]]) + Q2 2026 IR verification ([[Research/2026-08-12 - PLTR - Q2 2026 Earnings IR Verification]]). These are decision rules, not automatic status flips — user runs `/status`.

- **→ HOLD HIGH (or reaffirm) if**: Next reported quarter shows U.S. commercial revenue growth still ≥100% YoY **and** U.S. commercial RDV still growing QoQ **and** no named marquee mid-market displacement to Databricks Genie Ontology / Microsoft Fabric IQ / frontier-lab DeployCo (Anthropic JV / OpenAI DeployCo). Q2 2026 already clears the growth leg (US commercial +149% YoY to $764M; US commercial RDV $6.238B, +124% YoY / +27% QoQ per IR Ex. 99.1).

- **→ HIGH sizing ok (Live Portfolio sleeve not cut) if**: Conviction Triggers section stays current **and** FY2026 revenue guide holds ≥$8.0B after any subsequent print **and** Rule of 40 stays ≥130%. (Q2: Rule of 40 = 155%; FY26 rev guide $8.150–$8.158B.)

- **→ MEDIUM if**: (a) One quarter of U.S. commercial NRR/NDR breaking below ~120–130%, **or** (b) a *named* mid-market / marquee commercial loss to Genie Ontology / Fabric IQ / lab-direct DeployCo, **or** (c) FY revenue growth guide cut to ≤50% YoY while forward EV/Revenue stays >25x, **or** (d) NHS Feb-2027 break-clause executes *and* a second allied-government sovereignty rejection lands in the same two quarters (contagion, not one-off).

- **→ MEDIUM (process/sizing path — even if ops hold) if**: User elects to treat the name as quality-but-priced after a beat-and-raise still fails to hold the tape for a second consecutive earnings print (June 2026 pattern repeating on Q2 or Q3), absent a stated variant perception on moat *duration/width* beyond “falsifiers haven’t fired.”

- **→ LOW if**: Competitor ships **governed cross-object transactional write-back to source ERPs** with decision-level audit that closes the Bain-noted gap, **and** U.S. commercial growth decelerates below 60% YoY in the same half — hard-end moat and commercial engine both cracking together.

- **→ CLOSE / exit review if**: Army Enterprise Agreement or Maven program-of-record ceilings are materially cut without offsetting awards, **or** a top-20 logo loss (~42% revenue concentration) is disclosed, **or** sustained sub-40% revenue growth for two consecutive quarters (base-rate fade wins Outstanding Q#1).

## Mental Models
- **Models applied**: [[Generalist - Overview]] (always) · [[Lens - Automation & AI Readiness]] (PLTR is the archetypal context/ontology vendor) · [[Lens - Value Layer Monopoly]] (thesis rests on owning the semantic/intelligence layer). [[Industry - Semiconductors]] deliberately not applied — enterprise software/defense, no fab or hardware-process exposure.
- **Triggers that fired** (each a hypothesis to test against this note's own evidence, not a verdict):
	- *Value Layer Monopoly §3 · AI-era overlay — infrastructure vs application* — the crux. Is the Ontology a toll-collected **infrastructure** layer AI-enabled challengers must rent (moat widening), or a sophisticated **application** layer cheap intelligence now lets smaller teams assemble (moat dissolving)? Hypothesis: defense / air-gapped / certified deployment behaves as infrastructure (widening); the commercial ontology behaves as application (contestable) — the split maps almost 1:1 onto the bull vs bear case.
	- *Automation & AI Readiness §7 · context-window down-weight* — the live kill-switch. If frontier context windows get large + cheap enough that curated ontologies become optional for ~80% of commercial use cases, the Lens B/C **commercial** moat compresses while the organizational / defense leg persists. Outstanding Q#5 restated as a falsification trigger — monitor model-context economics directly.
	- *Automation & AI Readiness §2 · the moat is two moats, not one* — defense context (IL6 / FedRAMP, 20-yr ontology library, FDE patterns) passes the "what can't be bought with the same model + same money" test and is genuinely un-rentable; commercial context is more replicable (Fabric IQ "good enough"). Do not score moat durability as a single number.
	- *Value Layer Monopoly §2 · layer-renter disqualifier* — sharpest structural test: PLTR runs on AWS / Azure / GCP / Snowflake / Databricks / NVIDIA. Does it pay rent to the compute layer below and sit hostage to its pricing? 84% gross margin says not squeezed today — but this is the disqualifier to monitor, not to assume away.
	- *Generalist · data network effect vs scale economy* — is the "ontology-library flywheel" a genuine **data network effect** (cross-customer learning compounds) or a bespoke per-customer **scale economy** mislabeled as one? If ontologies are siloed per client, the moat is switching-cost (durable, non-compounding), not network-effect (compounding) — materially changes the terminal-value math.
	- *Generalist · base rates / outside view (run adversarially)* — top-decile-or-rarer of software firms sustain >20% revenue CAGR for a decade off a $4.5B+ base; the FY2026 guide is +82% (raised twice from +61%). The base-rate fade (toward 30–40% by FY27–28) is the thing the bull case must **beat**, not ignore; PLTR earns its multiple only as a *justified* outlier.
	- *Generalist · mean-reversion vs trend-continuation* — the business can compound (trend) while the multiple mean-reverts — the "negative return even with strong execution" risk in Outstanding Q#1. Test which object is actually reverting: the fundamentals, or the ~49x forward-revenue multiple (June's compression to ~33x round-tripped by mid-August).
	- *Generalist · reflexivity in high-growth equities* — SBC ≈ 35% of FY2025 revenue (~14% TTM as growth outran grants) + ~$6M/day insider selling means the talent / comp engine is partly reflexively dependent on an elevated share price; a deep, sustained drawdown could impair the FDE / JV expansion model — a feedback loop a static DCF misses.
	- *Value Layer Monopoly §2 · political / geopolitical ceiling* — the binding constraint on the most dominant, strategically-salient layers is political, not economic; PLTR's defense / surveillance salience (IDF, NHS, ICE) is a tailwind under the current administration and a two-sided risk on a political turn.
	- *Generalist (Expectations Investing) · isolate the single mispriced variable* — the re-rating hinges on U.S. commercial RDV conversion + NRR holding ≥~130%, not on defense (the floor, not the swing). Reverse-DCF endgame: today's ~$400B market cap needs ~$40–45B revenue / ~$15B+ FCF by ~2035 — plausible only if commercial hypergrowth persists well past the base-rate fade.
	- *2026-06 real-world test (the sell-off)* — the June de-rate fired the **mean-reversion** (business +85% in Q1 vs the multiple −46% off ATH), **political-ceiling** (France→ChapsVision; UK NHS break-clause), and **crowding-already-priced** (Wolfe resumes *Neutral*: "valuation already reflects the outlook") triggers; the **application-layer / context-window** crux is now being *priced* via the Anthropic / usage-based commoditization narrative, though unproven in the numbers. The *US-commercial* falsifying datapoint did **not** fire (US commercial accelerated to +104%, guide raised +120%) — the bear is running through the political + valuation channels, not (yet) the moat-commoditization channel. Per [[Research/2026-06-29 - PLTR - June 2026 Sell-Off Through Mental Models - news]].
- **Disconfirming check**: All three files converge bullish — Generalist's software-monopoly / pricing-power profile, Automation Lens B/C strong-fit, and a clean Value-Layer identification — and per the READING PROTOCOL that very agreement is the cue to hunt hardest, not to commit. (1) **Single falsifying datapoint**: one quarter of U.S. commercial NRR breaking below ~120%, *or* a marquee mid-market displacement to Microsoft Fabric IQ / Databricks "good enough" — either confirms the application-layer (moat-dissolving) read over the infrastructure read. *(2026-06 update: this datapoint has NOT fired — Q1 2026 US commercial accelerated to +104%, guide raised to +120%. The June sell-off ran through the political-ceiling + multiple-reversion channels instead; the moat-commoditization channel remains narrative, not data — keep watching NRR and any named enterprise loss to Anthropic / usage-based players.)* (2) **Base rate to beat**: sustaining >20% revenue CAGR for a decade off a $4.5B+ base is a top-decile-or-rarer outcome; ~$400B implies that *and* no net multiple compression — outlier status must be earned, not assumed. (3) **Crowding trap**: "context is the moat" is now consensus and richly priced at ~49x forward revenue; the Automation Lens's own warning is that the edge is gone where already priced — even a *correct* moat read is not alpha unless the variant perception is that the moat's **duration / width** (sovereign-AI + defense annuity) exceeds what consensus discounts. If that variant perception can't be stated, this is "quality but priced."
- **Evidence update (2026-07-10 batch-6 pass, evidence-tested against July-2026 web research)**: the hard falsifiers moved further AWAY from firing — Q1 2026 (May 4) NDR jumped 139%→150%, US commercial +133%, RPO $4.5B +134%, remaining deal value $11.8B +98%; no named commercial displacement found. The bear kept running through exactly the predicted channels, now wider: political-ceiling ACCELERATING (France→ChapsVision confirmed Jun 17 with €655M sovereign pledge; UK NHS "unacceptable point of weakness" committee report drove the Jul 8 drop ahead of the Feb-2027 break clause; Swiss court loss; Met Police £50M block; Germany reviewing). Two NEW vectors this section must absorb: (1) the frontier labs CAPITALIZED the deployment layer — Anthropic's $1.5B enterprise-services JV (Blackstone/H&F/Goldman) + OpenAI's $4B "DeployCo" institutionalize the FDE model against PLTR, converting the moat-commoditization channel from narrative into funded structure; (2) the Army named Anduril LEAD for the NGC2 common data layer (Jun 22, under its 10-yr/$20B ELA) with PLTR as partner-not-prime — a hierarchy demotion inside the defense-moat leg (partially offset: Maven becoming a Pentagon program of record, ~$100M July NGC2 award, USG revenue +84%). Meta Compute (Jul 1) left PLTR unharmed — the asset-light deployment layer rebounded ~11% in early July while compute names cratered; cheaper compute is arguably a tailwind. Insider selling continues (~$130M recent; Karp + Sankar 10b5-1). Pre-Q2 (~Aug 10) maintenance action: formalize the missing Conviction Triggers section around the NDR floor, a named lab-direct displacement, NHS break-clause execution, and Anduril prime-creep.
## Related Research

- [[Research/2026-03-21 - PLTR - Gemini Strategy Canvas]] — Comprehensive strategy, product, financial, and valuation analysis (Gemini Canvas export)
- [[Research/2026-03-29 - PLTR - Gemini Automation Platforms Canvas]] — Palantir Ontology vs ServiceNow CMDB deep-dive: complementary not competitive
- [[Research/2026-03-29 - Palantir Comparison]] — Claude conversation: Palantir vs ServiceNow end-to-end automation platform analysis
- [[Research/2026-03-31 - Databricks Threat to Palantir]] — Claude conversation: Databricks competitive threat assessment, write-back gap analysis, Microsoft Fabric IQ convergence
- [[Research/2026-04-05 - ServiceNow CMDB vs Palantir Ontology]] — Claude conversation: Database architecture deep-dive, LLM-native data model comparison
- [[Research/2026-04-09 - ServiceNow CMDB Dependency and Limitations]] — Claude conversation: CMDB constraints, Knowledge Graph evolution, Salesforce Agentforce comparison
- [[Research/2026-04-15 - PLTR - Competitive Win Scenarios]] — Win scenario analysis: defense, supply chain, healthcare, manufacturing IoT
- [[Research/2025-02-19 - PLTR - Palantir Valuation Analysis]] — Grok valuation analysis: P/E 655 (Feb 2025), analyst consensus Hold, early growth data
- [[Research/2026-04-14 - NOW - AI Disruption Risk - deep-dive]] — AI disruption framework validating orchestration layer thesis; MCP/A2A protocol dynamics
- [[Theses/NOW - ServiceNow]] — Complementary enterprise AI positioning (Ontology vs CMDB)
- [[Theses/NET - Cloudflare]] — Adjacent enterprise software / edge AI thesis
- [[Sectors/Enterprise Workflow AI & Automation]]
- [[AI Bubble Risk and Semiconductor Valuations]]
- [[Research/2026-04-23 - Scenario - Iran Ground Invasion May 2026]] — Scenario: kinetic conflict accelerates defense procurement (Maven, Warp Speed, Alpamayo, ShipOS); NATO sovereign AI expansion
- [[Research/2026-05-11 - Private Credit BDC Redemption Gating Wave - news]] — Tangential: AI-driven margin compression on private-credit-financed software borrowers (TCPC ~33% of Q1 markdowns software-related); public-market platforms with strong FCF (PLTR Ontology) are the credit-cycle echo of the productivity-disruption beneficiary thesis
- [[Research/2026-06-04 - AI Dark Output GDP Measurement Gap - deep-dive]] — Macro lens: AI output is real but largely unmeasurable; "Captured AI Output" requires pricing power. Supports PLTR as the deployment layer that makes enterprise AI output visible/capturable (Ontology governed write-back); PLTR's own value capture rests on consumption pricing + 139% NRR holding
- [[Research/2026-06-11 - PLTR - Karp on Frontier Lab Discontent - news]] — Karp (CNBC): enterprises "unhappy" with frontier labs ("tokenmaxxing"), "implementation is where the value is" (next 7yrs), "most of Anthropic's public projects run on Palantir" — CEO-level color for the deployment-layer value-capture insight; self-serving source, Anthropic-on-PLTR claim unverified
- [[Research/2026-06-29 - PLTR - June 2026 Sell-Off Through Mental Models - news]] — Why the worst month on record is multiple mean-reversion (Q1 beat-and-raise, ~−46% off ATH) amplified by three structural narratives (AI-agent commoditization, France/UK sovereignty rejections, US defense CR freeze); mental-models read of which bear channel is actually firing (political + valuation, not yet US-commercial commoditization)
- [[Research/2026-07-09 - PLTR - Model Evolution and Agentic Workload Viability Deep Dive]] — Backs §Industry Context deepen: mid-2026 model evolution made agentic workloads production-viable (95%+ function-calling) but the reliability gap (60%→25% single-run→8-run consistency) and long-context "trap" (~1,250x costlier than structured retrieval) mean the context-window kill-switch has NOT fired; Databricks closed the semantic-layer gap in months (Genie Ontology / "agentic control plane," $6.9B ARR +80%) yet governed write-back + defense gaps persist — moat compressed at the analytical end, held at the operational end
- [[Research/2026-07-12 - Enterprise AI Adoption - Gating Factors Critique, 2030 Trajectory, Winners-Losers - synthesis]] — Macro synthesis: the durable gate on enterprise AI adoption is organizational (workforce/process redesign, decade-scale — Celonis "60% can't adapt operations fast enough"), not model capability; PLTR's FDE-led process redesign sells the gate's resolution. Ranks PLTR a Tier-3 consumption-converted winner; the #120 agentic-moat falsification watch remains unfired (Q1 NDR 150%, US commercial +133%)

- [[Research/2026-08-12 - PLTR - Bull vs Bear Debate Synthesis]] — Adversarial Bull vs Bear R1–R2 synthesis: hard-end write-back/IL6 + unfired NRR falsifiers still stand; semantic monopoly / international-as-deferred / June-as-value broken; conviction pressure is sizing/process (reassess) not a forced business short — conviction unchanged (high), flagged for user `/status`
- [[Research/2026-08-14 - PLTR - Pentagon 244M No-Bid Memo - news]]
- [[Research/2026-08-15 - PLTR - HHS Biometric Sponsor Vetting - news]] — HHS/ORR Horizon = existing ACF Foundry instance (ATO); draft PWS integration plane, not a new Palantir $ award

## Log

### 2026-08-12 (/status-prep — Q2 IR + Conviction Triggers)
- [IR verification]: [[Research/2026-08-12 - PLTR - Q2 2026 Earnings IR Verification]] — Daily Intel 08-12 headlines checked against Palantir IR / SEC Ex. 99.1 (2026-08-03). **Confirmed:** Q2 rev +93% to $1.935B; US commercial +149% to $764M; FY26 guide $8.150–$8.158B (+82%); US commercial guide >$3.424B (≥134%); Rule of 40 155%; US commercial RDV $6.238B (+124% YoY). **Partial/not IR:** DoD ~$244M Feinberg memo = The Register exclusive on draft planning memo (not a finalized award); Japan Palantir+Anduril = Nikkei/policy consideration, not a signed contract. ICE/LexisNexis = third-party data feed narrative (no PLTR revenue in IR).
- [Conviction Triggers]: §Conviction Triggers formalized (gap since 2026-07-10 log). Key Metrics + Summary + Catalysts refreshed for Q2. **Conviction unchanged (high)** — ops falsifiers moved further away; sizing/process two-sided flag from [[Research/2026-08-12 - PLTR - Bull vs Bear Debate Synthesis]] still stands for user `/status` (multiple-hostage / Triggers now written).


### 2026-08-12
- [Bull vs bear debate]: [[Research/2026-08-12 - PLTR - Bull vs Bear Debate Synthesis]] — multi-agent Round 1–2 (InvestmentVault Bull / Bear). Converged: hard-end moat + unfired NRR falsifiers intact; June multiple-hostage + semantic months-not-years catch-up + structural sovereignty conceded. Conviction unchanged (high) — **flagged for user `/status`** on sizing/process (Conviction Triggers still missing; Live Portfolio sleeve). No metrics edited; Daily Intel 08-12 PLTR headlines unused as ops.

### 2026-04-15
- [Major thesis restructure]: Complete rewrite to Thesis Template; consolidated 9 research sources (Gemini/ChatGPT/Claude/Grok); added all template-required sections; updated metrics to April 2026 — conviction unchanged (medium), status draft to active.

### 2026-04-15 (earlier)
- [Research sync]: Linked [[Research/2026-04-15 - PLTR - Competitive Win Scenarios]] — win scenarios across defense, supply chain, healthcare, manufacturing IoT — conviction unchanged.

### 2026-04-14
- [ChatGPT research integration]: Added insights from PLTR vs NOW AI comparison, AI regulation, AI bubble risk — conviction unchanged.
- [NOW research sync]: AI disruption analysis reinforces complementary thesis; MCP 97M monthly SDK downloads, multi-agent error amplification ~10x — strengthened (governance moat validation).
- [Grok ingestion]: Valuation analysis (P/E 655 Feb 2025, $74.59 avg target) — conviction unchanged.

### 2026-04-13
- [Initial thesis]: Created from two Gemini canvases (Strategy, Automation Platforms); Ontology as operational control plane with write-back, complementary to ServiceNow — conviction set at medium.

### 2026-04-22
- Sector re-scoped: Enterprise Software & Defense → Enterprise Workflow AI & Automation (vault-wide subsector taxonomy reorganization).
- Wikilink cleanup: Replaced `[[Sectors/Enterprise Software]]` and `[[Sectors/Defense & Geopolitics]]` → `[[Sectors/Enterprise Workflow AI & Automation]]` in Related Research section during sector-fill of [[Sectors/Enterprise Workflow AI & Automation]].

### 2026-04-23
- Scenario [[Research/2026-04-23 - Scenario - Iran Ground Invasion May 2026]]: positive via kinetic-conflict defense procurement acceleration (Maven, Warp Speed, Alpamayo, ShipOS, TITAN); NATO sovereign AI $30B+ expansion — conviction strengthened: ground invasion is textbook demand trigger for AI-native defense platforms; DOGE budget rationalization + active-threat combine to favor Palantir's demonstrated-ROI model over legacy contractors.

### 2026-04-27
- Addressed user callouts: PLTR — addressed `[!question]` on competitive moat / patent protection in §Industry Context; added new subsection "Why the Ontology Resists Replication: Structural Moats vs. Patent Protection" covering 5 structural barriers (architectural inversion, MMDP atomic write-back, ontology library flywheel, security certifications, FDE talent) — conviction unchanged: structural moats compound faster than 2010-2015 architecture patents expire (2030-2035), making patent duration non-determinative for thesis horizon.

### 2026-05-01 (/sync)
- [[Research/2026-04-24 - Luo Fuli on OpenClaw and Agent-Era Compute Reallocation - video-transcript]]: Frontier-lab framing of agent moat as "meticulously orchestrated context engineering" directly validates Ontology-as-control-plane thesis — context-substrate moat compounds in agent era. Conviction unchanged.
- [[Research/2026-04-24 - Thomas Kurian on TPU Capacity Anthropic Hosting and Agentic Chip Design - video-transcript]]: Hyperscaler agentic-chip co-design (Wiz cybersecurity agents, Gemini Enterprise +60% in 3 months) signals enterprise-AI inflection; PLTR's defense-grade Ontology positioned ahead of commoditized agent layer. Conviction unchanged.
- [[Research/2026-04-22 - Marc Andreessen on Internet Media Fragmentation and Outrage Cycles - video-transcript]]: Tangential AI-policy/dark-money mention; no thesis-moving evidence. Conviction unchanged.

### 2026-05-11 (/sync)
- [[Research/2026-05-11 - Private Credit BDC Redemption Gating Wave - news]]: Tangential — AI productivity disruption destroying private-credit-financed cash-burning software borrowers (TCPC ~33% of Q1 markdowns software-related); public-market platforms with strong FCF (PLTR Ontology) are the credit-cycle echo of the productivity-disruption beneficiary thesis. Conviction unchanged — no direct PLTR operating signal.

### 2026-05-22 (manual)
- Status change: portfolio-wide alignment — confirmed as current Live Portfolio holding; conviction medium→high.

### 2026-06-05 (/sync)
- [[Research/2026-06-04 - AI Dark Output GDP Measurement Gap - deep-dive]]: SemiAnalysis "Dark Output" reframes the bubble's monetization gap as a capture (not output) problem — supports PLTR's deployment-layer "extract-ROI" positioning; value capture rests on Ontology pricing power + 139% NRR holding. Conviction unchanged (high) — macro framing, no direct PLTR signal.

### 2026-06-11 (/sync)
- [[Research/2026-06-11 - PLTR - Karp on Frontier Lab Discontent - news]]: Karp (CNBC) — enterprises "unhappy" with frontier-lab "tokenmaxxing," "implementation is where the value is," "most of Anthropic's public projects run on Palantir" — CEO-level corroboration of the deployment-layer value-capture insight. Conviction unchanged (high) — self-serving source, Anthropic-on-PLTR unverified, no new operating signal.

### 2026-06-29
- Mental Models populated: first-fill of §Mental Models via [[Generalist - Overview]] + [[Lens - Automation & AI Readiness]] + [[Lens - Value Layer Monopoly]] — 10 triggers logged as hypotheses-to-test (crux: AI-era infrastructure-vs-application split; kill-switch: context-window commoditization; adversarial: layer-renter + base-rate fade + crowding-already-priced). Conviction unchanged (high) — lenses, not verdicts.

### 2026-06-29 (/numbers)
- Numbers refresh: 7 metrics updated, 2 material (Revenue Growth re-based to FY2025 annual +56.2% from the Q4-+70%/+61%-guide composite; Gross Margin ~81%→84.1%, +3.1pp). Also MktCap ~$259B, Px $112.93, EV/Rev ~49.2x, GAAP op margin 38.1%, FCF yield ~1.0%. Snapshot: [[_Archive/Snapshots/PLTR - Palantir (pre-numbers 2026-06-29-203032)]]

### 2026-06-29 (sell-off analysis)
- Sell-off analysis: [[Research/2026-06-29 - PLTR - June 2026 Sell-Off Through Mental Models - news]] — June 2026 worst month on record (~−25-30%, $106 52-wk low, ~−46% off ATH) is multiple mean-reversion, NOT a fundamental break (Q1 was a beat-and-raise: +85% rev, US commercial +104%, FY guide raised +71%/+120%), amplified by AI-agent commoditization narrative (Anthropic), France/UK sovereignty rejections (ChapsVision; NHS Feb-2027 break-clause), and US defense CR freeze (federal revenue delay 6-9mo). Updated Summary / Bear Case / Catalysts / Key Metrics (Q1 actuals + raised guide); merged §Mental Models real-world test (political + valuation channels firing, not yet US-commercial commoditization).
- Conviction unchanged (high) — **flagged for user `/status`**: risk/reward genuinely two-sided (fundamentals accelerated + multiple now ~33x fwd rev vs. sovereignty + commoditization risks crystallizing). Snapshot: [[_Archive/Snapshots/PLTR - Palantir (pre-selloff-update 2026-06-29-204412)]]

### 2026-07-09
- Wikilink cleanup: 5× [[Research/2026-06-29 - PLTR - June 2026 Sell-Off Through Mental Models - news]] references repaired (links omitted the ` - news` filename suffix — rename-only fix preserving all content; restores /sync idempotency-key match). Conviction unchanged.

### 2026-07-09 (/deepen)
- Deepened Industry Context: added model-evolution→agentic-viability thread + refreshed Databricks front to mid-2026 (Genie Ontology / "agentic control plane," $6.9B ARR +80%, Agent Bricks 100k+ agents). Key finding — the reliability gap (60%→25% single-run to 8-run consistency) and long-context "trap" (~1,250x costlier than structured retrieval) mean the context-window kill-switch has NOT fired; model gains expand the deployment-layer TAM at the hard end faster than they commoditize it.
- Conviction unchanged (high), two-sided: bear "good enough" validated (Databricks closed the semantic-layer gap in months, not years) but governed-write-back + IL6/air-gap gaps persist and are not model-solvable. Falsifying datapoint (US-commercial NRR <120% or named mid-market loss) still unfired. Snapshot: [[_Archive/Snapshots/PLTR - Palantir (pre-deepen 2026-07-09-130950)]]

### 2026-07-10
- Mental models pass: batch-6 evidence sweep appended evidence-update to ## Mental Models — NDR 150% (falsifiers moving away), political channel accelerating (NHS/France/Swiss), NEW: labs capitalized deployment layer (Anthropic $1.5B JV, OpenAI $4B DeployCo) + Anduril named NGC2 lead — conviction unchanged (high); formalize Conviction Triggers before Q2 (~Aug 10).

### 2026-07-12 (/sync)
- [[Research/2026-07-12 - Enterprise AI Adoption - Gating Factors Critique, 2030 Trajectory, Winners-Losers - synthesis]]: Macro adoption synthesis — the binding enterprise-AI gate is workforce/process redesign (PLTR's forward-deployed demand driver), not model capability; #120 falsification watch unfired (Q1 rev +85%, US commercial +133%, NDR 150% > 120% threshold). Conviction unchanged (high) — reinforces, no new operating signal.

### 2026-07-12 (/numbers)
- Numbers refresh: 2 metrics updated, 0 material. Market cap ~$259B→~$291B (+12.4%), share price $112.93→$126.79 (+12.3%) — both below the 25% materiality threshold. Revenue growth (+56.2%→+56.18%) and gross margin (84.1%→84.07%) round to identical displayed text — left unedited (no-op). FY2026 revenue guidance fetch_gap. Remaining rows (EV/Revenue, operating margins, FCF yield, quarterly revenue, Rule of 40, customer count, RDV, NRR, bootcamp conversion, PEG, analyst consensus, insider selling) are custom metrics — left unedited. Snapshot: [[_Archive/Snapshots/PLTR - Palantir (pre-numbers 20260712-173930)]]

### 2026-07-12 (/numbers)
- Numbers refresh: 0 metrics changed (second same-day pass, ~1hr after prior refresh) — Market Cap, Share Price, Revenue Growth, Gross Margin all identical to prior refresh after rounding. FY2026 revenue guidance still fetch_gap. Snapshot: [[_Archive/Snapshots/PLTR - Palantir (pre-numbers 20260712-183935)]]

### 2026-08-14
- [[Research/2026-08-14 - PLTR - Pentagon 244M No-Bid Memo - news]]: Feinberg memo up to $243.9M through Mar-2027 + options to Dec-2028; follows $10B Army pact — opposite of EA/Maven cut; → CLOSE unfired — conviction unchanged (high).

### 2026-08-15
- [[Research/2026-08-15 - PLTR - HHS Biometric Sponsor Vetting - news]]: Horizon named as ACF Foundry with ATO; biometric contractor + FBI NGI, not Palantir collection; no $ / vehicle; ICE 460k/12k is VLM §2 political-ceiling color — HOLD HIGH / CLOSE unfired — conviction unchanged (high).
- Metrics synced: 50 figures updated across 11 sections (FMP market data + Q2 call/10-Q via web). June de-rate round-tripped — $174.04 / ~$400B / ~49x fwd revenue on the raised guide, with Q2 disclosures landing NDR 157% (table said 139%) and customers 1,049. Snapshot: [[_Archive/Snapshots/PLTR - Palantir (pre-metrics-pass 2026-08-15-194220)]]
