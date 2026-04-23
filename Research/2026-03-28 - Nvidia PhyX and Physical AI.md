---
date: 2026-03-28
tags: [research, semiconductors]
status: active
sector: Semiconductors
source: Claude conversation export
source_type: deep-dive
---

# Nvidia PhyX and Physical AI

## Original Query
> Evaluate the importance, primacy and competitive dynamics of Nvidia's Omniverse and PhyX engine in influencing its success in building physical AI and world model based AI.

Are there any other alternatives to Nvidia's PhyX engine. Describe how the PhyX engine is improved over time.

---

## Nearly every potential competitor has become a partner instead

Nvidia's moat rests on several reinforcing pillars. First, **full-stack vertical integration**: Nvidia is the only company that owns GPU hardware, physics engines (PhysX, Newton), rendering (RTX), a simulation platform (Omniverse), AI foundation models (Cosmos, GR00T, Alpamayo), and edge computing (Jetson) — spanning the complete training-to-deployment pipeline. Second, **OpenUSD ecosystem gravity**: by championing OpenUSD as the "HTML of 3D," Nvidia made Omniverse the interoperability hub that every major industrial software vendor connects through. Third, **GPU compute monopoly**: no competitor can match the raw GPU compute needed for large-scale parallel physics simulation, rendering, and AI training simultaneously. Fourth, **network effects**: with 82+ application connectors, partnerships with every major industrial PLM vendor, and an expanding developer base of **2 million+ robotics developers**, each new integration makes the platform more valuable.

The vulnerabilities are real but limited. **Tesla** builds proprietary simulation tools internally, generating training data from its fleet of millions of vehicles — a unique data advantage Nvidia cannot replicate. **Open-source alternatives** like Genesis (a newer generative physics engine) could reduce dependency on Nvidia-specific tools. **Export restrictions** limit Nvidia's reach in China, the world's largest manufacturing economy. And **MuJoCo still outperforms PhysX** in contact dynamics accuracy for constrained robotic systems, though Newton's integration of MuJoCo Warp addresses this gap.

The realistic assessment is that replicating Nvidia's stack would require a consortium approach — perhaps Google Cloud + MuJoCo + Unreal Engine + an industrial PLM vendor — but the coordination challenges make this improbable in the near term. The combination of hardware, software, models, and partnerships has been built over more than a decade and represents what may be the deepest technology moat in the AI industry.

The most remarkable feature of the competitive landscape is how systematically Nvidia has converted potential rivals into platform partners. **Siemens** has committed hundreds of industrial AI experts to the partnership, integrating Omniverse libraries into its Teamcenter Digital Reality Viewer and accelerating its Simcenter Star-CCM+ with Blackwell GPUs. **Dassault Systèmes** announced a long-term strategic partnership in February 2026, integrating Omniverse physical AI libraries into DELMIA Virtual Twin and co-developing "Industry World Models." **Ansys** adopted Omniverse Cloud APIs for AVxcelerate and Fluent. **Google DeepMind** co-developed Newton rather than building a competing platform. Microsoft Azure is a primary cloud host for Omniverse.

## How the competitive alternatives stack up against Nvidia's physics ecosystem

Among specialized engines, **Drake** (Toyota Research Institute / MIT) stands out for manipulation and grasping applications with its hydroelastic contact model providing the highest fidelity for dexterous manipulation — but it is CPU-only. **DART** (Georgia Tech) offers strong accuracy through Lie group formulation but is limited to academic use. **Brax** (Google), a JAX-based differentiable physics engine, is being deprecated in favor of MuJoCo Playground and MJX. **Jolt Physics**, an open-source MIT-licensed engine powering Horizon Forbidden West and now integrated into Godot 4.4, is rising as a lightweight alternative for games. **AMD has no GPU-accelerated physics engine** comparable to PhysX — its FEMFX (2019) is a CPU-only FEM library, and while PhysX's April 2025 full GPU kernel open-sourcing theoretically enables AMD ports, the effort required is enormous.

**Havok (Microsoft)**, founded in 1998, remains the premier gaming physics engine with deployment in **600+ games and 12 of the top 20 best-selling US games in 2023**. Acquired by Intel in 2007 for $110 million, then by Microsoft in 2015, Havok now integrates as a full engine-level replacement for Chaos Physics in Unreal Engine 5 and as a DOTS/ECS backend in Unity. However, Havok remains **CPU-only** with no meaningful GPU acceleration and has **no presence in AI/robotics simulation**. Its latest version (2025.1) supports Nintendo Switch 2 but does not address the differentiable physics or massive parallelism needed for robot learning.

**Bullet Physics / PyBullet**, created by Erwin Coumans, was once the standard for robotics RL research but is now **classified as inactive** with no major releases since late 2021. Researchers have largely migrated to MuJoCo. PyBullet sees roughly 23,000 weekly PyPI downloads but lacks the GPU acceleration, accuracy, and active development of its competitors.

**Unreal Engine's Chaos Physics** replaced PhysX as the default in UE5, driven by Epic's desire for full control over the physics pipeline, large world coordinate support, and tighter integration with its destruction and VFX systems. However, developers report **ongoing stability issues and performance gaps** compared to UE4-era PhysX, and several AAA studios use Havok's Unreal integration instead. Chaos has no relevance to AI/robotics simulation.

**Unity Physics** offers three pathways: legacy PhysX-based physics, custom DOTS/ECS physics, and Havok for Unity. Unity's ML-Agents toolkit enables RL training but lacks the physics fidelity and scalability of Isaac Lab or MuJoCo for serious robotics research. Unity's business challenges (runtime fee controversy, CEO change) have further weakened its position as a simulation platform.

**MuJoCo (Google DeepMind)** is the most important alternative in the AI/robotics domain. Created by Emo Todorov and open-sourced by DeepMind in 2022 under Apache 2.0, MuJoCo uses generalized (joint) coordinates optimized for articulated robots and features specialized contact dynamics with soft contact models. It is the **most cited physics engine in ML literature** and the standard for reinforcement learning research through OpenAI Gym/Gymnasium environments. Its GPU-accelerated variant **MJX-JAX** achieves ~950K steps/sec on an A100 with batch size 8192. MuJoCo's primary weakness relative to PhysX is handling large-scale gaming scenarios with many disconnected bodies. Critically, rather than competing, DeepMind collaborated with Nvidia to create MuJoCo Warp within the Newton framework.

## Conclusion

Nvidia has executed a masterful platform strategy in physical AI simulation: PhysX evolved from a gaming physics card into a comprehensive multi-physics engine, Omniverse transformed from a 3D collaboration tool into the operating system for physical AI, and strategic moves like Newton (embracing MuJoCo rather than fighting it) and Cosmos (generating synthetic training data at unprecedented scale) have closed key capability gaps. The April 2025 full open-sourcing of PhysX GPU kernels was a confidence move — Nvidia's advantage lies not in proprietary code but in ecosystem integration that no single open-source contribution can replicate. The competitive landscape reveals an almost gravitational dynamic: companies that might challenge Nvidia find it more rational to build on its infrastructure than to build alternatives. Whether this dominance persists depends largely on whether GPU compute remains the bottleneck for physical AI — and with training requirements growing exponentially, that bottleneck shows no sign of easing.

### Newton brings differentiable physics to the Nvidia ecosystem

Announced at **GTC 2025** and released in beta at **CoRL 2025 (September 2025)**, **Newton** is an open-source, GPU-accelerated physics engine co-developed by Nvidia, Google DeepMind, and Disney Research, managed by the Linux Foundation. Built on **NVIDIA Warp** — an open-source Python framework for GPU-accelerated simulation created by Miles Macklin (the same developer behind FleX) — Newton supports multiple physics solvers including XPBD, MuJoCo, Featherstone, and SemiImplicit approaches.

Newton's key innovation is **differentiable physics**: the ability to compute gradients through simulation, enabling gradient-based optimization for robot design and control. It integrates **MuJoCo Warp** — a GPU-accelerated version of Google DeepMind's MuJoCo physics engine built on NVIDIA Warp — which achieves **70x+ acceleration** over MuJoCo's existing MJX GPU simulator. Newton is compatible with both MuJoCo Playground and NVIDIA Isaac Lab, and policies trained in Newton have been successfully transferred to PhysX and deployed on real robots.

## Omniverse evolved from a 3D collaboration tool into the backbone of physical AI

Nvidia Omniverse began as a collaborative 3D design platform but has been re-architected into a modular, cloud-native collection of libraries, microservices, and APIs purpose-built for physical AI applications. Built on **Pixar's OpenUSD** (Universal Scene Description) as its foundational scene-description language, Omniverse enables seamless interoperability across 82+ third-party applications from vendors like Siemens, Autodesk, Bentley, and Adobe.

### PhysX 5.x represents a generational leap in simulation capabilities

The GPU/CPU feature split is notable. Rigid body dynamics, articulations, collision detection, character controllers, and vehicle dynamics run on both CPU and GPU. However, FEM soft bodies, PBD particles/fluids, cloth simulation, and Signed Distance Field (SDF) collision detection are **GPU-only features requiring CUDA-capable hardware** (SM6.0/Pascal or later). This architectural choice leverages Nvidia's hardware advantage while ensuring broad CPU compatibility for basic physics.

# Nvidia's physics simulation empire powers the physical AI era

Nvidia has built what is arguably the most defensible competitive position in technology today — a vertically integrated stack spanning GPU hardware, physics engines, simulation platforms, AI foundation models, and edge computing — all designed to train machines that interact with the physical world. **Omniverse, the company's "operating system for physical AI," combined with PhysX, the Newton physics engine, and Cosmos world foundation models, creates an end-to-end pipeline no competitor can replicate.** The strategic significance is immense: Jensen Huang frames physical AI as a **$50 trillion opportunity** across manufacturing, logistics, autonomous vehicles, and robotics. What makes Nvidia's moat particularly striking is that nearly every potential competitor — Siemens, Dassault Systèmes, Ansys, Google DeepMind, Microsoft — has chosen to build on top of Nvidia's infrastructure rather than compete against it. The few exceptions, like Tesla's proprietary simulation stack, validate the approach by building analogous systems internally at enormous cost.

---

## Related
- [[Sectors/Semiconductors]]

## Related Sectors
- [[Sectors/GPU & AI Compute Accelerators]] — Back-reference: cited in sector fill under Competitive dynamics (PhysX 5 GPU-only features requiring CUDA SM6.0+ widen performance gap with each hardware generation — Havok/MuJoCo/Drake/Brax/Genesis comparative analysis shows no merchant alternative), Acquisitions/new entrants ("partnership conversion" strategy: Siemens/Dassault/Ansys/DeepMind/Microsoft all build on Nvidia's infrastructure rather than compete), and Investor heuristics #5 (Physical AI $50T opportunity framing per Jensen).
