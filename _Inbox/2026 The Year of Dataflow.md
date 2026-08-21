---
title: "2026: The Year of Dataflow"
source: "https://davidhdong.substack.com/p/2026-the-year-of-dataflow"
author:
  - "[[David Dong]]"
published: 2026-08-19
created: 2026-08-20
description: "FlashAttention. Megakernels. Boardfly TPU. Taalas. Extreme co-design. The biggest hardware progressions of the last few years are all converging on dataflow."
tags:
  - "clippings"
---
I was watching Eric Vishria explain why Benchmark invested in Cerebras after a decade of avoiding hardware. His argument was simple: as you add more compute, you also need more memory nearby and more bandwidth between the compute units. Keep scaling all three, and eventually the chip boundary gets in the way. Cerebras’s answer was to make the chip as large as a wafer.

That was 2016, and at the time it looked like an extreme position. In May 2026 Cerebras went public above $56 billion, with a multi-year agreement to deploy 750 megawatts of wafer-scale systems for OpenAI.

The bet aged well because it was never really about wafers. It was about a boundary. Compute kept getting faster, the things feeding it did not, and the cost of crossing between them became the design problem. Cerebras took that observation to its physical limit early. Everyone else has been arriving at the same place ever since, from other directions.

Around 2017, the reason to build accelerators was deep learning. In 2026, it is inference. Both push computer systems toward dataflow.

Deep learning gave hardware an unusually regular workload: large tensor operations, known dependencies, repeated layers, and enough reuse to justify specialized hardware and expensive compilation. Inference pushes this further. The same model may execute billions of times, while latency increasingly depends on where weights and KV cache live, how activations move between stages, and whether communication can overlap with computation.

Once those costs matter, optimizing each operation independently is no longer enough. The producer-consumer edges have to stay visible: which operation produces a value, where that value lives, how it moves, and when the consumer can run.

That is the version of dataflow this series is about. The clearest way to see it is to watch one algorithm get rewritten around a single boundary.

## Same math, same silicon, different execution

![](https://substackcdn.com/image/fetch/$s_!gpEP!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9554949-d2e4-46fc-9121-1fa172e783a7_1400x788.png)

A straightforward implementation writes the attention score matrix to HBM, reads it back for softmax, then writes and reads another large intermediate before multiplying by V. FlashAttention works on tiles instead. Q, K, and V blocks are brought into SRAM, a block of scores is computed, softmax state is updated, and the result is consumed while the data is still on chip. The full attention matrix never needs to exist in HBM. On the backward pass it recomputes values rather than storing and reloading them, because on a modern accelerator extra arithmetic can be cheaper than another trip through memory.

The important point is not that data stops moving. It is that the producer-consumer chain is reorganized around the memory hierarchy: values stay close to the computation long enough to be reused, and are consumed before they have to be written back. Same attention, different physical execution.

That is one boundary: HBM to SRAM. There are four others.

## The seam ladder

A seam is a producer-consumer edge that crosses a physical boundary. The boundary may sit inside an operation, between memory tiers, between operators, between chips, or between racks. For each edge, the system has to decide where the value lives, how it moves, and when its consumer can run. Placement and scheduling are coupled: where the value lives affects when it arrives, and when it is consumed affects how long it must stay live.

Five seams organize almost everything that follows. I will refer to them by number for the rest of this series.

![](https://substackcdn.com/image/fetch/$s_!IHXl!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4ef9291-a03b-4dc7-b6f5-b6bcb93cee51_1448x1086.png)

I use *seam* because no single existing term spans all five boundaries. The individual ideas already have their own literatures — memory I/O, communication-avoiding algorithms, placement and routing — but the producer-consumer path is the common object.

Follow these seams outward and the design target gets larger: from movement inside an operation, to communication between operators and chips, and eventually to the path a token takes through several kinds of machines.

## Why the seams matter

**Every time a dependency crosses a seam, it acquires a physical bill.** The farther the seam reaches, the more things can enter that bill: distance, serialization, buffering, retiming, switching, protocol, and synchronization.

![](https://substackcdn.com/image/fetch/$s_!b6cM!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcadc25b6-5fb5-4697-af67-dba6d880c210_1168x784.jpeg)

The cost does not increase perfectly with the seam number—a good chip-to-chip link can be cheaper than an HBM access. What does increase is **how much machinery sits between producer and consumer**.

As arithmetic gets faster, those boundaries matter more. That is why AI systems keep pulling the expensive seams into the architecture.

## Why deep learning made an old idea economical

Dataflow is much older than the current accelerator industry. In the classical model, an operation becomes executable when its inputs are available. Execution follows producer-consumer dependencies rather than a program counter walking through a fixed sequence of instructions.

A ───┐

ADD ───► C

B ───┘

That firing rule is a statement about causality: ADD cannot run until A and B exist. A dataflow machine carries that dependency into execution itself. Values are produced, routed, stored, matched with their consumers, and then enable the next work.

Researchers built machines around this idea decades ago. Dennis’s static dataflow model, the MIT tagged-token architecture, and the Manchester Dataflow Machine differed in how they represented and scheduled dependencies, but they shared the same problem: the unit of work was small. If every scalar operation needs operand matching, token storage, routing, and scheduling, the machinery around the arithmetic can cost as much as the arithmetic itself.

Deep learning changed that economics. The unit governed by one placement or scheduling decision can now be a tensor tile, a fused operator, or an entire pipeline stage containing millions of operations. The graphs are unusually regular and repeat at an enormous scale. Spending minutes or hours compiling a model makes sense when the resulting mapping runs billions of times.

Another way to say the same thing is to change perspective. Instead of starting with a unit and asking what it executes, follow the value: where it is produced, how it is transformed and routed, and where it is consumed next.

So the working definition for this series: a dataflow-oriented system keeps producer-consumer dependencies explicit into execution, so placement, storage, movement, and scheduling can be organized around them. The seam ladder tracks how far that dependency reaches physically.

## Four architectures, four taxes

The chips that emerged after 2016 get grouped together as dataflow accelerators. That hides the interesting part. Each attacks a different tax that a conventional machine pays.

#### TPU hard-wires the inner loop.

![](https://substackcdn.com/image/fetch/$s_!ewON!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44d4e03d-3e32-425b-a986-3a533d7edf91_370x540.png)

A TPU core is built around Matrix Multiply Units. Inside each MXU, operands flow through a systolic array and are reused as they move from one multiply-accumulate cell to the next. The compiler tiles larger tensor operations onto those units and keeps them fed. The tax removed is operand movement inside dense matrix multiplication: values stay close to the arithmetic instead of repeatedly traveling through a general memory hierarchy. TPU made S1 architectural.

#### SambaNova maps the model onto a spatial machine.

![Sambanova vs Nvidia: AI Chipsets Compared | SambaNova](https://substackcdn.com/image/fetch/$s_!e0_d!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bb64e6c-e3e0-4ebc-8a55-18ad3104eb58_1024x587.png)

Sambanova vs Nvidia: AI Chipsets Compared | SambaNova

An RDU is a fabric of compute units, SRAM memory units, and configurable switches. The compiler decides where each operation runs, where intermediate tensors live, and how values move between them. Different regions of the chip execute different parts of the model at the same time; an activation can stream directly into its consumer instead of becoming a kernel output that later has to be read back. TPU fixed the flow inside one dominant operator. SambaNova made the compiler responsible for the pipeline across operators — which buys cross-operator locality and overlap, and makes physical placement part of the compile. SambaNova made S3 a compiler target.

#### Groq turns the model into a timetable.

![](https://substackcdn.com/image/fetch/$s_!cz20!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff86b86bd-0620-48a7-b63f-f0b94e8d3b89_800x386.jpeg)

Groq gives the compiler similar authority and extends it to exact timing. SRAM is primary storage rather than a cache, and computation, memory access, and inter-chip communication are scheduled before execution. The compiler decides when a value is read, when a matrix operation starts, when a result is transmitted, and when the next chip consumes it. The result is deterministic latency: cache misses, dynamic arbitration, and much of runtime scheduling leave the critical path. SambaNova makes placement and routing explicit; Groq goes further and fixes the arrival schedule ahead of time.

#### Cerebras moves inter-chip communication onto the wafer.

![](https://substackcdn.com/image/fetch/$s_!is1a!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c457cb1-4cd5-4c85-ba8d-7ad67ae58ad2_2194x1243.jpeg)

Cerebras also does compile-time placement and routing, but the substrate is different. The Wafer-Scale Engine is a large two-dimensional mesh of processing elements, each with local SRAM and a router. A conventional accelerator cluster repeatedly leaves one package, crosses SerDes and switches, and enters another. Cerebras stretches the on-chip mesh across the wafer, turning a large class of transfers that would have been network communication into short on-wafer movement. Cerebras made S4 a silicon decision.

Worth noting what Cerebras did not absorb. WSE-3 carries around 44 GB of on-chip SRAM, which is not enough for a frontier model’s weights, so weights live in an external MemoryX appliance and stream onto the wafer layer by layer while activations stay resident. The most aggressive S4 answer in the industry deliberately keeps an S2-style seam. Hold onto that; it is the whole question the last post is about.

**The four taxes:**

- **TPU** → reduce operand movement around matrix compute
- **SambaNova** → reduce the memory and scheduling cost between operators
- **Groq** → remove runtime timing uncertainty
- **Cerebras** → remove package and network distance

The seams are different. The reason for pulling them into the design is the same.

*(This is not about hardware architecture, so there are a lot of details I am not going into. For deeper dive, [Irrational Analysis](https://open.substack.com/users/135313705-irrational-analysis?utm_source=mentions) is always a good source. Like the following)*[Irrational Analysis](https://irrationalanalysis.substack.com/p/unfinished-draft-its-the-dataflow?utm_source=substack&utm_campaign=post_embed&utm_medium=web&embedding_publication_id=6880266)

[

Irrational Analysis is heavily invested in the semiconductor industry…

](https://irrationalanalysis.substack.com/p/unfinished-draft-its-the-dataflow?utm_source=substack&utm_campaign=post_embed&utm_medium=web&embedding_publication_id=6880266)

## Inference changes the balance

Those architectures were built during the training era, when flexibility and aggregate throughput dominated. Inference changes the optimization target.

A production model can remain stable for months while executing billions of times, making more compilation and specialization worthwhile. But it runs under dynamic demand and is judged on time to first token, time per output token, tail latency, tokens per dollar, and tokens per watt.

Autoregressive decode repeats nearly the same graph for every token. The compute graph is highly predictable. The state moving through it is not. Requests arrive at different times. Output lengths are unknown. Batches change every iteration. KV caches grow and disappear. Prefix reuse varies. MoE routing depends on the current token.

> **stable compute graph + dynamic state and demand**

This creates a natural tension. The compiler can specialize tensor layouts, kernel pipelines, model partitioning, communication schedules, and hardware placement. The runtime must still handle request admission, batch composition, KV allocation, cache routing, expert imbalance, and failures.

The industry is not moving that boundary in one direction. It is redrawing it, and the workload is doing the drawing.

## What that cost us at SambaNova

I spent years on these problems at SambaNova, where our compiler placed computation, memory, and communication routes onto a physical fabric. Spatial place-and-route worked best with static shapes. Production inference brought variable sequence lengths, batch sizes, and parallelism choices.

We covered the gap with a library of precompiled mappings. Every new model and context length multiplied the combinations we had to generate and validate. Eventually we rebuilt around dynamic tensors and moved more binding and scheduling into the runtime, trading static efficiency for a system that could adapt.

That is the honest version of this story. Pulling a seam into the machine is not free, and production dynamism can push it back out. What was unusual then now shows up everywhere, from GPU kernels to rack-scale systems.

## The seam moved inside the GPU

The GPU remains a SIMT machine. Around its performance-critical path, NVIDIA has steadily turned data movement and tensor execution into explicit producer-consumer pipelines.

On Hopper, the Tensor Memory Accelerator moves multidimensional tiles between global and shared memory asynchronously; one thread initiates movement while the rest of the block keeps working, and warps specialize into producers and consumers. Blackwell extends the separation: fifth-generation Tensor Core operations can be issued by a single thread, execute asynchronously, and store accumulators in dedicated Tensor Memory, with adjacent CTAs cooperating on larger matrix operations.

A small number of threads increasingly issue asynchronous memory and tensor operations while dedicated hardware engines execute them. The programming model is following. CuTe and CUDA Tile expose tiles, layouts, copies, MMA operations, and pipelines as explicit concepts, and Tile IR lets the compiler choose warp specialization, TMA use, prefetch depth, register pressure, and shared-memory staging. The useful question moved from what does this thread execute to how does this tile travel through the machine. Post 2 is entirely about this.

Software is converging on the same answer from above. TileRT — from the group behind the TileLang DSL — decomposes LLM operators into tile-level tasks and schedules compute, I/O, and communication together across multiple GPUs, compiling the decode graph into a single persistent megakernel. Work that used to be coordinated between kernel launches is now scheduled inside one long-running GPU program. It currently targets specific frontier models on eight-B200 systems, and has adopted a split where vLLM handles prefill and TileRT handles latency-sensitive decode.

This is worth being precise about, because it is the point of the whole series. TileRT is not a dataflow chip. It is a dataflow representation, on a SIMT substrate, doing what a spatial compiler does: making the operator-to-operator edge explicit and scheduling movement against computation. The operator boundary still exists; it no longer has to be a kernel-launch boundary. It is still an S3 edge, now controlled from inside the GPU.

The same shift reached the network earlier than most people assume. SHARP in-network reduction arrived in the NVLink domain with third-generation NVSwitch on Hopper in 2022 — portions of all-reduce, reduce-scatter, and all-gather executing inside the switch fabric. NVLink 6 extends it. The switch no longer only forwards collective traffic; it performs part of the reduction.

Then the design boundary reaches the rack and the building. NVIDIA’s Vera Rubin DSX reference architecture treats compute, networking, storage, power, cooling, simulation, and operations as one co-designed system, with tokens per watt and time to production as the target metrics.

Stack the progression:

![](https://substackcdn.com/image/fetch/$s_!qKrk!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ff63b2b-1944-453f-b80b-e7c2e55570fb_1168x784.jpeg)

SIMT remains the flexible control substrate, handling irregular code, dynamic behavior, and the long tail of operations. Dataflow mechanisms shape the hot path, where locality, overlap, and predictable dependencies dominate. The convergence is layered, not wholesale.

## The graph now crosses processor types

Once the producer-consumer path is explicit, there is no reason every stage has to run on the same kind of processor. Prefill values dense computation and memory capacity. Decode attention repeatedly reads a growing KV cache. MoE feed-forward execution values low-latency weight access and fast expert communication. Agentic workloads add CPU-based tools, retrieval, storage, and long-lived context. One homogeneous accelerator can execute all of these. Their physical needs are increasingly different.

Google’s eighth-generation TPUs show this at the product level. TPU 8t targets large-scale training. TPU 8i targets sampling, serving, and reasoning. Dense training favors the regular neighbor communication of a torus; MoE serving and reasoning benefit from a flatter network with fewer hops. So 8i triples on-chip SRAM to 384 MB — enough to hold much of a reasoning model’s KV working set on silicon — doubles ICI bandwidth to 19.2 Tb/s, adds a dedicated Collectives Acceleration Engine in place of the previous generation’s SparseCores, and abandons the 3D torus for a hierarchical, Dragonfly-inspired topology called Boardfly. Four-chip building blocks aggregate into groups over copper; groups connect through optical circuit switches. Maximum network diameter drops from sixteen hops to seven across a 1,024-active-chip pod. That is S5 being pulled into the compilation target: the topology was chosen by the shape of the model’s communication graph.

![TPU 8t and TPU 8i technical deep dive | Google Cloud Blog](https://substackcdn.com/image/fetch/$s_!IJjn!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4a4e2bc-4c2d-4dbb-9608-471aeee9e625_1300x459.png)

TPU 8t and TPU 8i technical deep dive | Google Cloud Blog

The clearest signal is in what 8i gave up. It has lower peak FP4 throughput than 8t, 10.1 PFLOPs against 12.6, and more HBM, 288 GB against 216. The inference chip traded arithmetic for memory and collectives.

NVIDIA’s Vera Rubin platform splits work across processor types inside a single decode loop. Rubin GPUs handle prefill and decode attention, where memory capacity and dense throughput matter. The LPX system — 256 LPUs across 32 liquid-cooled trays, derived from Groq’s LPU — handles latency-sensitive FFN and MoE expert execution. NVIDIA calls it attention-FFN disaggregation, and describes GPUs and LPUs as jointly computing every layer of the model for every output token. For a forty-layer model, that is forty round trips per token across the seam: NVIDIA is betting that FFN weights resident in SRAM at rack scale beats the cost of crossing that boundary eighty times. Look at the energy table and you can see exactly what is being traded against what.

![Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the  NVIDIA Vera Rubin Platform | NVIDIA Technical Blog](https://substackcdn.com/image/fetch/$s_!IQN_!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93dc5727-2873-4b5b-8002-e099e2487607_1972x1560.webp)

Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform | NVIDIA Technical Blog

Two details make the bet legible. Rubin CPX, NVIDIA’s own long-context inference GPU announced in 2025, was deprioritized once LPX arrived — the homegrown phase-specialized part lost to licensed dataflow silicon. And inside the LPX rack, eight-chip all-to-all clusters form the local groups of a dragonfly topology. Google reached for Dragonfly for MoE all-to-all in the same year, independently. When two teams with nothing in common pick the same topology, the workload is doing the choosing.

The unit of design is no longer one accelerator. It is the path taken by one token through several kinds of machines.

## The product boundary keeps moving

Etched’s product reflects the same movement. It is now a “frontier inference cluster,” with chips, packages, boards, cooling, interconnects, memory hierarchy, software, and manufacturing co-designed for prefill and decode — low-voltage inference and a cluster-scale HBM/SRAM memory system offered as system-level answers to power density, memory latency, and large-model capacity. These are company claims and still need independent validation, but the boundary of the product is the revealing part. Etched is not selling a chip that drops into a conventional rack.

At the far extreme, Taalas turned an individual model into custom silicon. Its thesis was “the model is the computer”: the compiler’s output becomes hard-wired hardware, with some adaptation retained through fine-tuning, and only a couple of metal layers customized per model. In August 2026, AMD agreed to acquire it.

What AMD actually wants is not yet clear, and the ambiguity is the interesting part. It might be the chips — hardwired decode silicon sitting alongside Instinct GPUs in a Helios rack, a third instance of the same heterogeneous split. Or it might be the flow: a design methodology that turns a trained model into taped-out silicon in roughly two months. The second reading is the consequential one, because it would mean the asset was never the hardware. It was the compiler, extended all the way through fabrication.

Either way, within eight months two aggressive forms of specialization — compile-time scheduling of computation and communication, and model-specific silicon — were absorbed by GPU vendors and aimed at inference. NVIDIA took Groq’s team, assets, and a license rather than the company. AMD bought Taalas outright.

## Where does dataflow stop?

Not every seam should be pulled into the machine. And how to pull also matters significantly. Tighter coupling improves locality and predictability, and costs flexibility. Inference makes that trade messy: sequence lengths are unknown, MoE routing is token-dependent, speculative decoding is stochastic, architectures keep changing. Cerebras keeps an S2 seam on purpose. We gave back static efficiency at SambaNova to survive production. The stopping condition should be computable from the frequency, volume, and predictability of each edge — which is the question for the last post, and the reason the series has one.

What makes dataflow a useful systems lens in 2026 is that it no longer identifies a family of accelerators. It describes the repeated process through which AI turns logical dependencies into physical architecture.

The first accelerator era asked which chip should run the graph. The next one asks how far the graph should extend into the machine.

## The series

Five posts, following the seams from the chip to the datacenter.

**S2 — the GPU.** How the thread stopped being the unit of work: TMA, warp specialization, Tensor Memory, persistent kernels, and what tile-level programming models actually change.

**S3 — the programming model.** Why AI compilers increasingly place computation, memory, and communication before execution, what can be decided statically, and what has to remain dynamic.

**S4 — scale-up.** NVLink, ICI, wafer-scale fabrics, in-network compute, and how tightly coupled accelerators execute one graph together.

**S5 — the system.** Disaggregated inference, dynamic routing, unknown lengths, and the stopping condition: when tighter coupling helps, and when the system should deliberately keep a seam.