---
date: 2026-01-17
tags: [research, semiconductors, HBM, AI, compute, memory, gemini-canvas]
status: active
sector: Semiconductors & Photonics
source: Gemini Canvas export
source_type: deep-dive
propagated_to: [NVDA, SNDK, 285A]
---

# The Paradox of Infinite Inference: Architectural Disruption, The Jevons Cycle, and the structurally Persistent HBM Shortage (2025–2027)

## Executive Summary

The global artificial intelligence ecosystem stands at a critical juncture, precipitated by the release of the DeepSeek-V3 and DeepSeek-R1 architectures in early 2025. This report, commissioned to analyze the implications of the research highlighted by domain experts such as Rohan Paul, investigates the profound collision between hyper-efficient software architectures and the rigid physical constraints of the semiconductor supply chain. The central thesis of this analysis challenges the prevailing assumption that algorithmic efficiency—specifically the drastic reduction in memory consumption achieved by DeepSeek’s Multi-Head Latent Attention (MLA)—will alleviate the global shortage of High Bandwidth Memory (HBM).

On the contrary, our comprehensive examination suggests that the industry is entering a "Jevons Paradox" supercycle. While the per-token memory cost of inference has been reduced by over 90% via MLA, this efficiency is driving a nonlinear explosion in induced demand, characterized by the rise of "Reasoning Models" (System 2 AI) that consume inference compute at orders of magnitude higher rates than their predecessors. Furthermore, the physical transition to HBM4 in 2026 introduces a structural contraction in effective DRAM wafer capacity due to the "Three-to-One" production penalty.

This report provides an exhaustive technical and economic analysis of these dynamics. We dissect the specific mechanisms of DeepSeek’s architecture, contrast them with emerging paradigms like Google’s Titans, and map these software variables against the inflexible realities of semiconductor manufacturing. The conclusion is unambiguous: the global HBM shortage will not only persist through 2026 but will likely intensify, morphing from a crisis of *capacity* into a crisis of *bandwidth* and *packaging throughput*, fundamentally altering the investment logic for data center infrastructure and semiconductor capital expenditure.

---

## 1. Introduction: The DeepSeek Shock and the Efficiency Signal

The release of DeepSeek-V3 and its reasoning-optimized derivative, DeepSeek-R1, acted as a seismic event for the AI hardware industry. As noted by AI researcher Rohan Paul and others in the technical community, the specifications of these models seemingly defied the established scaling laws that had governed the 2023-2024 era of Large Language Model (LLM) development.[1, 2] The industry had grown accustomed to a "brute force" trajectory where model performance was linearly correlated with massive increases in parameter counts, training flop-hours, and memory footprint. DeepSeek shattered this correlation by achieving GPT-4 class performance with a training cost of merely $5.576 million and a radically optimized memory architecture.[3]

### 1.1 The Market Reaction and the "DeepSeek Effect"
The immediate reaction to the DeepSeek technical report was a mixture of technical admiration and financial panic. NVIDIA’s market capitalization experienced a significant correction, driven by a superficial reading of the situation: if models become 90% more efficient, does demand for GPUs drop by 90%? This phenomenon, dubbed the "DeepSeek Effect," forced a re-evaluation of the entire AI hardware stack.[4, 5]

However, a deeper analysis reveals that this reaction fundamentally misunderstood the nature of the efficiency gains. The DeepSeek architecture does not merely reduce costs; it alters the *nature* of the compute workload. By training on 2,048 NVIDIA H800 GPUs—chips deliberately crippled in interconnect bandwidth to comply with U.S. export controls—DeepSeek demonstrated that architectural ingenuity could overcome hardware limitations.[3, 6] This success has signaled to the broader market that the bottleneck is shifting. The era of "sparse computation" has arrived, where the primary constraint is no longer just raw FLOPS, but the intelligent routing of data and the maximization of memory bandwidth efficiency.

### 1.2 The Core Research Question
The user’s query posits a fundamental supply chain question: *What is the impact on compute and memory demand of the latest AI models, and will we still be in an HBM shortage?*

To answer this exhaustively, we must move beyond top-level specifications and analyze the microscopic interactions between the model’s operations and the GPU’s memory subsystem. We must quantify the "Thinking Token" phenomenon introduced by DeepSeek-R1, which effectively trades the memory savings of DeepSeek-V3 for a massive increase in compute duration. Finally, we must juxtapose this demand-side revolution against the supply-side reality of the HBM4 transition in 2026—a transition that promises higher performance but comes with severe manufacturing penalties.

---

## 2. Architectural Deconstruction: The Mechanics of Memory Efficiency

The primary driver of the "efficiency narrative" surrounding DeepSeek-V3 is its novel approach to memory management. In traditional Transformer architectures, the Key-Value (KV) cache represents the single largest consumer of High Bandwidth Memory (HBM) during inference, particularly for long-context applications. DeepSeek’s solution, Multi-Head Latent Attention (MLA), is the technical pivot point upon which the HBM demand forecast turns.

### 2.1 The Tyranny of the KV Cache
In a standard Multi-Head Attention (MHA) mechanism, used by models like GPT-3 and Llama 2, the model generates a Query ($Q$), Key ($K$), and Value ($V$) vector for every attention head at every layer. During the decoding (inference) phase, the $K$ and $V$ vectors for all previous tokens must be stored in HBM to generate the next token.

The memory footprint for the KV cache in MHA is calculated as:
$$M_{\text{KV, MHA}} = 2 \times n_{\text{layers}} \times n_{\text{heads}} \times d_{\text{head}} \times L \times P_{\text{bytes}}$$
Where:
*   $n_{\text{layers}}$ is the number of layers.
*   $n_{\text{heads}}$ is the number of attention heads.
*   $d_{\text{head}}$ is the dimension of each head.
*   $L$ is the sequence length (context window).
*   $P_{\text{bytes}}$ is the precision (e.g., 2 bytes for FP16).

For a model with the scale of Llama 3 405B, utilizing a 128k context window, this cache grows to terabytes of data, far exceeding the capacity of a single H100 (80GB) or even an H200 (141GB) GPU. This forces "Model Parallelism," splitting the model across many GPUs solely to hold the cache, which is inefficient and expensive.[7]

### 2.2 Multi-Head Latent Attention (MLA): The Compression Breakthrough
DeepSeek-V3 introduces MLA to fundamentally break this linear scaling relationship. Instead of storing the full high-dimensional $K$ and $V$ vectors for every head, MLA projects these vectors into a low-rank compressed latent space.[8, 9]

#### 2.2.1 The Mechanism of Low-Rank Compression
MLA employs a joint compression strategy. The model learns a compressed latent vector $c_{KV}$ which captures the essential information required for attention. The full Key and Value heads are then dynamically regenerated (upsampled) only when needed during the attention computation.

The memory footprint for the KV cache in MLA is:
$$M_{\text{KV, MLA}} = n_{\text{layers}} \times (d_{\text{latent}} + d_{\text{head}}) \times L \times P_{\text{bytes}}$$

Crucially, the term $d_{\text{latent}}$ is significantly smaller than the aggregate dimension of all heads ($n_{\text{heads}} \times d_{\text{head}}$).
*   **DeepSeek-V3 Implementation:** The model uses a compressed dimension ($d_{\text{latent}}$) of 512. In contrast, a standard MHA equivalent might require storing dimensions equivalent to thousands of integers.
*   **Result:** Research confirms that MLA reduces the KV cache size by approximately **93.3%** compared to MHA, and significantly outperforms even Grouped-Query Attention (GQA), which is used by Llama 3.[6, 10]

**Table 1: Comparative Analysis of Attention Mechanisms and Memory Impact**

| Metric | Multi-Head Attention (MHA) | Grouped-Query Attention (GQA) | Multi-Head Latent Attention (MLA) |
| :--- | :--- | :--- | :--- |
| **Example Models** | GPT-3, Llama 2 | Llama 3, Qwen-2.5 | DeepSeek-V3, DeepSeek-R1 |
| **KV Storage Strategy** | Store full vectors for all heads | Share K/V across groups of heads | Store compressed latent vector |
| **Compression Ratio** | 1x (Baseline) | ~4x - 8x | **~15x - 60x** |
| **KV Cache Size (128k context)** | Extremely High (>100GB/layer) | High (~10-20GB/layer) | **Ultra-Low (<1GB/layer)** |
| **Bandwidth Demand** | Massive (Memory Bound) | High | **Low (Compute Bound)** |
| **Performance Impact** | Best theoretical accuracy | Slight degradation possible | Superior to GQA, matches MHA |

### 2.3 The "Weight Absorption" Trick and Compute-Bound Shift
A critical second-order insight is *how* MLA achieves this without losing accuracy. It uses a mathematical identity often referred to as "matrix absorption." The projection matrices used to decompress the latent vector into the full Key/Value heads can be mathematically absorbed into the Query projection and the interaction matrices during the matrix multiplication steps.[8, 9]

This has a profound implication for hardware demand:
*   **Shift from Memory to Compute:** By avoiding the retrieval of massive KV caches from HBM, MLA reduces the memory bandwidth pressure. However, it requires *more* Floating Point Operations (FLOPs) to perform the on-the-fly decompression and projection.
*   **The HBM Paradox:** DeepSeek-V3 transforms the inference workload from a **Memory-Bound** process (waiting for data to arrive from HBM) to a **Compute-Bound** process (waiting for the Tensor Cores to finish math).

This shift effectively "unlocks" the stranded compute capacity of GPUs like the NVIDIA H100. In MHA models, the Tensor Cores often sit idle 50% of the time, waiting for memory. In MLA models, the Tensor Cores run at near 100% utilization. This means a single GPU can process far more tokens per second, or handle much larger batch sizes, effectively increasing the "yield" of intelligence from the same hardware.[10]

---

## 3. The Computational Backbone: Mixture-of-Experts and Network Topology

While MLA revolutionizes memory *storage*, the compute engine of DeepSeek-V3 relies on an advanced implementation of Mixture-of-Experts (MoE) and a novel network topology designed to circumvent export controls.

### 3.1 DeepSeekMoE: Decoupling Knowledge from Cost
DeepSeek-V3 scales to 671 billion parameters, yet it activates only 37 billion parameters per token.[11, 12] This massive discrepancy is the heart of its economic advantage.
*   **Parameter Sparsity:** Unlike "dense" models (e.g., Llama 3 405B) where every parameter is used for every token, MoE models route tokens to specific "experts" (sub-networks) specialized in that type of data.
*   **Fine-Grained Experts:** DeepSeek innovated by using a larger number of smaller experts compared to competitors like Mixtral. This finer granularity allows for more precise knowledge isolation.
*   **Shared Experts:** To prevent "knowledge fragmentation," DeepSeek designates certain experts as "shared," meaning they are always activated. This ensures that common linguistic knowledge (grammar, basic logic) is available to every token without redundancy.[13]

### 3.2 The HBM Capacity Requirement for MoE
There is a crucial distinction here between **Memory Bandwidth** and **Memory Capacity**.
*   **Low Bandwidth:** Because only 37B parameters are active, the GPU only needs to move ~74GB of weights per forward pass (in FP16) or ~37GB (in FP8). This is low bandwidth.
*   **High Capacity:** However, the *entire* 671B parameter model must be loaded into the GPU cluster's aggregate memory to be accessible. This means DeepSeek-V3 still requires a massive amount of VRAM (HBM) to *host* the model, roughly 671GB to 1.3TB depending on quantization.[14, 15]

**Insight:** This confirms that while MLA saves memory on the *context* (KV cache), the MoE architecture still demands massive HBM *capacity* to store the model weights. The shortage of VRAM capacity remains a hard constraint for hosting the model, even if the bandwidth constraint is eased.

### 3.3 Overcoming Interconnect Bottlenecks: DualPipe and FP8
DeepSeek-V3 was trained on H800 clusters, which have significantly reduced NVLink bandwidth compared to the US-market H100. To mitigate this, the researchers developed **DualPipe**, a bidirectional pipeline parallelism algorithm that perfectly overlaps the "dispatch" (sending data to experts) and "combine" (receiving results) phases with the actual computation.[6, 16]
*   **Implication for Commodity Hardware:** This proves that ultra-high-speed proprietary interconnects (like top-tier NVLink) are not strictly necessary for training frontier models if the software schedule is optimized. This could drive demand for standard Ethernet-based AI networking (RoCEv2), broadening the hardware supply chain beyond NVIDIA’s walled garden, but simultaneously increasing the demand for high-performance networking gear from vendors like Broadcom and Marvell.[4, 12]
*   **FP8 Precision:** DeepSeek-V3 is natively trained in FP8 (8-bit floating point), reducing memory usage by 50% compared to BF16. This aggressive quantization is essential for fitting the model into limited HBM envelopes and doubling the effective compute throughput of the Tensor Cores.[11, 17]

---

## 4. The Reasoning Paradigm: DeepSeek-R1 and the "Thinking Token" Explosion

If DeepSeek-V3 is a story of efficiency, DeepSeek-R1 is a story of consumption. The introduction of "Reasoning Models" (System 2 AI) introduces a new variable that threatens to undo all the memory savings achieved by MLA.

### 4.1 Chain-of-Thought (CoT) as a Compute Multiplier
DeepSeek-R1 utilizes large-scale Reinforcement Learning (RL) to develop emergent reasoning capabilities. Unlike standard models that try to predict the answer immediately, R1 generates a "Chain of Thought"—a long internal monologue where it breaks down the problem, verifies its own assumptions, and backtracks if necessary—before emitting the final answer.[18, 19]

*   **The Hidden Cost:** A user might ask a query that requires a 500-token answer. A standard model generates 500 tokens. DeepSeek-R1 might generate 10,000 "thinking tokens" to derive that answer, and then the 500-token output.
*   **Inference Economics:** This increases the inference compute cost by a factor of 20x for the same user query.
*   **Implications for HBM:** While MLA reduces the memory footprint *per token*, R1 increases the *number of tokens* by an order of magnitude. The aggregate memory bandwidth consumed (Bytes per Second) remains astronomical because the GPU is running at full tilt for 20x longer.[20]

### 4.2 From "Chatbots" to "Agentic Workflows"
The low cost of DeepSeek-V3 (due to MoE and MLA) enables "Agentic" workflows—autonomous loops where an AI performs multi-step tasks.
*   **Example:** "Analyze the stock market."
    *   *Standard LLM:* Reads a summary, gives an opinion. (1 inference call).
    *   *Agentic R1:* Spawns 50 sub-agents to read 50 different financial reports. Each agent thinks for 5,000 tokens. They debate each other. They synthesize a master report. (50 x 5,000 = 250,000 tokens).
*   **Jevons Paradox:** Because the "cost per token" has dropped, the "tokens per task" has exploded. The total demand for HBM bandwidth does not decrease; it shifts from supporting *many users doing simple things* to supporting *fewer agents doing massive things*. This keeps the pressure on HBM supply critically high.[5, 21]

---

## 5. The Physical Layer: The 2026 HBM Supply Chain Crisis

Having established that demand for inference compute and memory capacity is structurally increasing (driven by R1 and Agents) despite per-token efficiency (V3/MLA), we must turn to the supply side. The physical constraints of manufacturing HBM4 in 2025-2027 present a bottleneck that software cannot optimize away.

### 5.1 HBM3E vs. HBM4: The Generational Leap
The industry is currently transitioning from HBM3E (extended version of HBM3) to HBM4.
*   **HBM3E:** The current standard for Nvidia H200 and Blackwell. Uses a 1024-bit interface. Stack heights of 8-Hi and 12-Hi.
*   **HBM4 (2026):** A radical redesign. The interface width doubles to 2048-bit. The base die (logic die) is no longer a simple buffer but a custom logic chip (often made on 5nm or 3nm processes) that can perform computation. Stack heights increase to 16-Hi.[22]

### 5.2 The "Three-to-One" Wafer Penalty
A critical and often overlooked metric in semiconductor manufacturing is the "bit density per wafer" relative to production complexity. Industry analysis for the 2026 outlook identifies a "Three-to-One" rule:
*   **The Trade-off:** To produce one wafer of high-capacity HBM4, a manufacturer (SK Hynix, Micron, Samsung) must sacrifice the capacity equivalent to three wafers of standard DDR5 DRAM.
*   **Why?** HBM requires extensive TSV (Through-Silicon Via) formation, complex micro-bumping, and significantly longer cycle times in the fab. The die size is also larger due to the wide IO interfaces.[23, 24]
*   **Result:** As AI demand forces manufacturers to shift wafer starts toward HBM, the global supply of standard memory (for PCs, servers, phones) evaporates. This creates a secondary shortage in the commodity market, driving up costs for all electronics.[25]

### 5.3 The Packaging Bottleneck (CoWoS and Hybrid Bonding)
The true bottleneck for HBM is not just the memory chips themselves, but the **Advanced Packaging**.
*   **CoWoS:** Nvidia GPUs use TSMC’s CoWoS (Chip-on-Wafer-on-Substrate) to connect the GPU die to the HBM stacks. Capacity for CoWoS is growing but remains the primary limiter on total GPU supply.
*   **Yield Issues with 16-Hi:** Moving to 16-Hi stacks for HBM4 introduces severe yield challenges. If the 15th die in a stack is defective, the entire stack (and the previous 14 good dies) is often lost. This "compound yield loss" effectively reduces the total bits available to the market, even if wafer starts increase.[22, 26]
*   **Thermal Constraints:** Stacking 16 dies creates a "thermal tower." Dissipating heat from the bottom dies through 16 layers of silicon requires new thermal interface materials (TIMs) and potentially limits the clock speeds, putting a physical ceiling on performance that software efficiency must compensate for.[26]

**Table 2: The HBM Supply-Demand Forecast (2025-2027)**

| Year | Primary Technology | Manufacturing Constraint | Market Status |
| :--- | :--- | :--- | :--- |
| **2025** | HBM3E (12-Hi) | CoWoS Capacity | **Severe Shortage** (Sold out 12+ months out) |
| **2026** | HBM4 (Transition) | 16-Hi Yields & "3:1" Wafer Penalty | **Structural Deficit** (HBM4 complexity reduces throughput) |
| **2027** | HBM4E / HBM5 | Hybrid Bonding Maturity | **Potential Stabilization** (Only if capacity triples) |

---

## 6. Market Dynamics: Sovereign Clouds and the Democratization of Demand

The "DeepSeek Effect" has a geopolitical dimension that exacerbates the HBM shortage. By proving that high-performance models can be trained and run on restricted or commodity hardware, DeepSeek has democratized the ambition of "Sovereign AI."

### 6.1 The Rise of Sovereign Clouds
Prior to DeepSeek, building a GPT-4 class model was perceived as a \$100M+ endeavor requiring thousands of prohibited H100s. DeepSeek demonstrated it could be done for \$5.6M on H800s.
*   **The Multiplier:** This implies that nation-states (France, UAE, Saudi Arabia, Japan, India) and mid-sized enterprises can now afford to build their own "Domestic Intelligence" infrastructures.
*   **Demand Impact:** Instead of demand being concentrated in 4-5 US hyperscalers (Google, Microsoft, Meta, Amazon, OpenAI), demand is now fragmented across hundreds of smaller entities. While each entity buys fewer GPUs than Microsoft, the aggregate "long tail" demand creates massive pressure on the supply chain.[27, 28]

### 6.2 Export Controls and the Black Market
The DeepSeek paper revealed that U.S. export controls (restricting interconnect speed) were ineffective at stopping model scaling. This will likely lead to:
1.  **Tighter Controls:** The U.S. may expand restrictions to HBM memory chips themselves or lower the performance thresholds further.
2.  **Hoarding:** Chinese firms, anticipating tighter bans, will aggressively hoard HBM3E and HBM4 chips, soaking up global supply and creating "shadow shortages".[3, 29, 30]

---

## 7. Beyond DeepSeek: Google’s Titans and Future Architectures

While DeepSeek-V3 optimizes the Transformer, research is already moving toward architectures that replace the Transformer’s memory mechanism entirely.

### 7.1 Google’s "Titans" and Neural Memory
A potential disruption to the HBM demand curve is the "Titans" architecture proposed by Google Research. Titans introduces a **Neural Memory Module** that learns to memorize context at test time.[31, 32]
*   **The Difference:** MLA compresses the KV cache (linear complexity, just smaller slope). Titans attempts to compress the *entire history* into a fixed-size neural state (constant complexity, O(1)).
*   **Implication:** If Titans-like architectures become production-viable in 2026, they could theoretically decouple inference from context length entirely. A 10M token context would use the same memory as a 4k token context.
*   **Reality Check:** As of 2025/2026, Titans is still in the research phase. The industry momentum is behind Transformers (DeepSeek/Llama). Therefore, for the relevant forecast period of this report, the Transformer’s linear memory dependency (even with MLA compression) remains the dominant driver of HBM demand.[33]

---

## 8. Forecast 2026: The Verdict on Shortage

Based on the synthesis of architectural, physical, and economic data, we can construct a high-confidence forecast for 2026.

### 8.1 Will we still be in an HBM Shortage? **YES.**

The DeepSeek architecture does not solve the HBM shortage; it *transforms* it.

1.  **Efficiency Induces Consumption (Jevons Paradox):** By reducing the memory cost per token by ~95%, DeepSeek has made "Reasoning Models" (R1) and "Agentic Workflows" economically viable. These applications consume 10x-100x more tokens per task, offsetting the per-token savings. The net result is a massive increase in demand for inference throughput.
2.  **The Supply Cliff (HBM4):** The transition to HBM4 in 2026 physically reduces the number of memory bits the industry can produce per wafer. The "Three-to-One" penalty means that even as manufacturers invest billions in new fabs, the effective output grows slower than demand.[23]
3.  **Capacity vs. Bandwidth:** DeepSeek-V3 is a "Capacity Hog" (needs 671GB+ to load weights) and R1 is a "Bandwidth Hog" (needs continuous streaming for thinking tokens). The combination keeps pressure on both the size of the memory modules (requiring 12-Hi/16-Hi stacks) and the speed of the interface.

### 8.2 Strategic Outlook
*   **For Data Center Builders:** The "DeepSeek Era" favors GPUs with massive memory bandwidth and efficient Tensor Cores (e.g., NVIDIA H200, Blackwell B200). The ability to run MLA efficiently will be the primary benchmark for TCO (Total Cost of Ownership).
*   **For the Supply Chain:** The bottleneck shifts to **Advanced Packaging**. The constraint is not the silicon die, but the CoWoS interposer and the vertical bonding of the HBM stack. Companies dominating this niche will hold the keys to the AI kingdom.
*   **For the Consumer:** Expect rising prices for SSDs and DDR5 RAM in 2026. The "Three-to-One" rule ensures that the AI industry will cannibalize the consumer memory supply to feed the insatiable demand for HBM.[25, 34]

In conclusion, DeepSeek-V3 and R1 are architectural marvels that saved the industry from a "Memory Wall" that would have made GPT-5 impossible. However, by saving us from the wall, they have accelerated us down the road of "Infinite Inference," ensuring that the hunger for High Bandwidth Memory remains the defining constraint of the silicon age for years to come.

---

## 9. Detailed Technical Addendum: Implementing MLA and MoE

### 9.1 MLA Implementation Details
DeepSeek’s implementation of MLA fundamentally changes the arithmetic intensity of the decoding step.
*   **Standard MHA Attention Score:**
    $$A = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$
    Here, $K$ and $V$ are retrieved from HBM. The data movement is massive.
*   **MLA Attention Score:**
    $$K = c_{KV} W_{UK}$$
    $$A = \text{Softmax}\left(\frac{Q (c_{KV} W_{UK})^T}{\sqrt{d_k}}\right) (c_{KV} W_{UV})$$
    DeepSeek optimizes this by absorbing $W_{UK}$ into $Q$.
    $$Q_{\text{absorbed}} = Q W_{UK}^T$$
    $$A = \text{Softmax}\left(\frac{Q_{\text{absorbed}} c_{KV}^T}{\sqrt{d_k}}\right) (c_{KV} W_{UV})$$
    This allows the attention score to be computed directly against the compressed latent vector $c_{KV}$, bypassing the need to ever materialize the full Key matrix in memory. This is the "secret sauce" that reduces bandwidth demand by ~64x.[10]

### 9.2 Training Stability and FP8
DeepSeek-V3’s training stability is notable. Despite using FP8 (a notoriously unstable format due to limited dynamic range), they achieved a training run with **zero loss spikes** and **no rollbacks**.[35] This was achieved by:
*   **Fine-grained Quantization:** Using different scaling factors for different tensors.
*   **High-Precision Master Weights:** Keeping the "master copy" of weights in higher precision (BF16 or FP32) while doing the heavy lifting in FP8.
This validates FP8 as the standard for future large-scale training, effectively doubling the memory capacity of existing GPUs for training tasks.[6]

---
*End of Report.*
Jan 15, 2026, 8:09:23 PM AEST
Products:
 Gemini Apps
Why is this here?
 This activity was saved to your Google Account because the following settings were on: Gemini Apps Activity. You can control these settings  here.Gemini Apps

---

## Related
- [[Theses/NVDA - Nvidia]] — GPU compute demand and HBM architecture
- [[Theses/SNDK - SanDisk]] — HBM capacity diversion affecting NAND supply
- [[Theses/285A - Kioxia]] — NAND supply beneficiary of HBM diversion
- [[Sectors/Semiconductors]]

## Related Sectors
- [[Sectors/GPU & AI Compute Accelerators]] — Back-reference: cited in sector fill under Macro shifts (HBM4 supply ramp, Jevons Paradox in compute demand, inference economics) and Investor heuristics (Jevons-inflection risk framework — compound efficiency gains vs aggregate GPU demand).
- [[Sectors/Semiconductor Capital Equipment]] — Back-reference: cited in sector fill under Macro shifts (AI compute demand driving HBM capacity expansion and hyperscaler capex floor; DRAM/HBM equipment intensity through 2028).
