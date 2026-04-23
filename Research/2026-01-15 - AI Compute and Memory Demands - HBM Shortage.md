---
date: 2026-01-15
tags: [research, semiconductors]
status: active
sector: Semiconductors
source: Claude conversation export
source_type: deep-dive
---

# AI Compute and Memory Demands - HBM Shortage

## Original Query
> https://x.com/rohanpaul_ai/status/2011453017296617822?s=46

https://x.com/rohanpaul_ai/status/2011450290772599158?s=46

What’s the impact on compute and memory demand of latest AI models from this research paper.

Will we still be in a HBM shortage ?
> Isn’t the paper a DeepSeek paper rather than google ?

---

## Will architectural shifts alleviate or worsen HBM demand?

**Long-term implications** are mixed for HBM suppliers. The paper's vision of hybrid memory hierarchies (SRAM → HBM → HBF → cloud storage) positions HBM as one tier among several rather than the sole solution. This could moderate long-term HBM volume growth while sustaining premium pricing for latency-sensitive workloads. However, total memory silicon demand likely increases as AI deployment scales—the question is which technologies capture incremental growth.

## Investment implications diverge by time horizon

**NVIDIA faces a more complex picture**. The DeepSeek moment in January 2025—when NVIDIA lost $600 billion in market cap in a single day—demonstrated market sensitivity to efficiency innovations. Engram represents continued pressure toward architectural efficiency over brute-force scaling. However, NVIDIA's ICMS announcement shows strategic awareness of memory bottlenecks, and the CUDA ecosystem provides durable competitive advantage.

**Memory suppliers face a paradox**: Engram-style architectures could eventually moderate HBM demand per GPU, but they shift demand to conventional DRAM—which is also severely constrained. Samsung plans a 50% HBM capacity increase by end of 2026, but this won't offset near-term shortages. Bank of America characterizes 2026 as a "supercycle similar to the boom of the 1990s."

The key question is whether **Jevons Paradox** applies: do efficiency gains reduce total demand, or do they make AI economically viable for more applications, increasing aggregate demand? Historical evidence favors the latter. AI inference costs dropped 280x from late 2022 to 2024, yet hyperscaler AI capex is projected at **$602 billion in 2026** (up from $256 billion in 2024). Memory efficiency hasn't reduced spending—it's enabled new use cases.

The financials support this: SK Hynix achieved **47% operating margin** in Q3 2025 (up from 40% YoY); Micron delivered **56.8% gross margin** in Q1 FY2026 (up from 39.5%). HBM provided 77% of SK Hynix's Q2 2025 revenue. All three memory suppliers are in the strongest competitive positions in their histories.

# DeepSeek Engram: Memory efficiency breakthrough challenges HBM thesis—but supply constraints persist

DeepSeek's January 2026 "Engram" paper introduces conditional memory that can offload **100 billion parameters to CPU DRAM with only 3% throughput penalty**, potentially disrupting the HBM scarcity narrative. However, the near-term investment thesis remains intact: all three major memory suppliers are sold out through 2026, HBM3e prices are rising 20%, and new fab capacity won't arrive until late 2027-2028. The more pressing implication is Engram's shift of demand from scarce HBM to conventional DRAM—which is also experiencing severe shortages with prices up 171% YoY. This is evolution, not disruption, of the memory supercycle.

## Conclusion: Evolution of the memory thesis, not disruption

- **NVIDIA**: Cautiously bullish with margin compression risk. 88% market share and CUDA moat provide durable advantage, but architectural efficiency innovations pressure the "more GPUs = better AI" narrative. Expect margins to moderate from 76% toward 65-70% by 2027.

The HBM shortage thesis isn't challenged—it's evolving. Engram and ICMS both redirect memory demand from scarce HBM to other tiers (DRAM, SSD, CXL-attached memory), but these alternatives are also constrained. The net effect in 2026-2027 is more likely **redistribution** of memory pressure than elimination.

The January 2025 "DeepSeek moment" was a sentiment shock; the January 2026 Engram paper is a technical roadmap. Both signal that AI's future is memory-efficient, not memory-intensive—but that future arrives in 2028, not 2026.

## Investment implications across the semiconductor value chain

NVIDIA faces structural margin compression from HBM cost inflation. Memory now represents **~45% of GPU production costs** for B200, with HBM + advanced packaging combined reaching ~65%. SK Hynix and Samsung's announced 20% price hikes for 2026 deliveries directly pressure chip-level gross margins. NVIDIA's defensive response—$45.8 billion in HBM prepayment obligations—secures supply but locks in elevated costs.

Advanced packaging capacity—not wafer fabrication—has become the binding constraint for AI accelerator supply. NVIDIA pre-booked **60-65% of TSMC's 2026 CoWoS output**; AMD secured ~11% for MI400. This "packaging fortress" determines who can ship next-gen AI chips. TSMC's CoWoS capacity is projected at 100,000 wafers/month by end-2026, up from ~40,000 in early 2025, but demand continues to outpace additions.

Samsung faces execution risk but offers recovery potential from depressed HBM share. The integrated foundry-memory model could prove advantageous as HBM4 base dies require logic processing. Watch for HBM4 qualification progress through H1 2026.

SK Hynix offers the purest exposure to the memory bandwidth bottleneck with 57-62% HBM revenue share, first-mover HBM4 advantage, and the strategic HBF partnership. Bank of America designates it their "Top Pick" for the 2026 memory supercycle. UBS projects ~70% HBM4 market share for NVIDIA's Rubin platform. The company's partnership with TSMC on advanced packaging strengthens its competitive moat. HBM products account for **54% of DRAM operating profit**.

Micron presents compelling value as the #2 HBM player with critical differentiation: **30% lower power consumption** versus competitors directly addresses TCO concerns for hyperscalers facing rising electricity costs. Micron is the preferred vendor for NVIDIA GB200 systems and key supplier for AMD MI350. The company has successfully transformed from cyclical DRAM player to AI-optimized full-stack memory provider.

The Patterson paper's recommendations could benefit NVIDIA long-term if the company pivots toward hybrid memory architectures. NVIDIA's Context Memory Storage Platform for KV cache management demonstrates early adaptation to memory-bound realities.

AMD offers strategic exposure to the inference memory thesis. The MI350 series (288GB HBM3E, up to 8 TB/s bandwidth) positions AMD as the memory-density leader—offering more HBM per dollar than NVIDIA. At 27-28x forward earnings with 64% projected 2026 EPS growth and 60% analyst price target upside, AMD presents compelling risk-reward for investors seeking inference-optimized GPU exposure.

## Data center infrastructure implications

**Power/Cooling**: Memory-centric architectures could moderate power growth relative to compute-centric scaling, but the paper's emphasis on 3D stacking introduces new thermal challenges. Rack power is rising from 40kW to 140kW+, with AI data centers projected to consume ~90 TWh by 2026.

The Patterson paper implies hyperscalers should recalibrate infrastructure priorities from FLOPS maximization toward memory bandwidth, capacity, and interconnect latency optimization. This has cascading effects:

## Conclusion: Memory is the new compute

The Patterson-Ma paper represents a paradigm shift in how the investment community should evaluate AI semiconductor opportunities. The conclusion is unambiguous: "LLM inference is no longer fundamentally compute-bound; memory bandwidth, capacity, and network latency are now the decisive factors."

The $600+ billion hyperscaler CapEx wave in 2026 flows through these bottlenecks. Companies solving the memory problem—not the compute problem—will capture disproportionate value in the next phase of AI infrastructure buildout.

# LLM Inference Has a Memory Problem—Not a Compute Problem

The paper's central finding is decisive: while GPU FLOPS increased **80× from 2012-2022**, memory bandwidth grew only **17×**, creating a structural mismatch that makes current accelerators inefficient for inference workloads. Companies like OpenAI reportedly lose $5 billion annually on inference costs, with the decode phase—where models generate one token at a time while constantly accessing memory—emerging as the economic chokepoint of AI deployment.

## Four architectural shifts proposed to break the memory wall

**Processing-Near-Memory (PNM)** places compute logic on separate but closely coupled dies near memory, avoiding the restrictive area and power constraints that throttle Processing-In-Memory (PIM) approaches. PNM enables **1000× larger memory partitions** compared to bank-level PIM sharding, simplifying software while maintaining high bandwidth. The paper favors PNM for datacenter-scale inference, reserving PIM for mobile devices where tighter energy constraints justify the complexity.

## The bigger picture: memory as the new compute bottleneck

Engram represents a paradigm shift from "how to calculate less" (MoE) to "don't calculate blindly"—recognizing that much of what models compute is static pattern retrieval that doesn't require neural computation. As @rohanpaul_ai articulated: "A typical AI model treats 'knowing' like a workout. Even for basic facts, it flexes a bunch of compute, like someone who has to do a complicated mental trick just to spell their own name each time."

---

## Related
- [[Sectors/Semiconductors]]

## Related Sectors
- [[Sectors/GPU & AI Compute Accelerators]] — Back-reference: cited in sector fill under Macro shifts (HBM triopoly pricing dynamics; inference economics framework) and Competitive dynamics (AMD MI350 288GB HBM3E per package vs B200 192GB — memory-capacity-per-GPU advantage that persists into MI450 HBM4 31TB/Helios rack).
- [[Sectors/Semiconductor Capital Equipment]] — Back-reference: cited in sector fill under Macro shifts (HBM shortage driving memory-side equipment demand floor; DRAM equipment +15.1% CY2026 per SEMI).
