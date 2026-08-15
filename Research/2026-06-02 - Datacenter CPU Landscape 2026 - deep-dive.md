---
publish: false
date: 2026-06-02
tags: [research, semiconductors, datacenter-CPU, server-CPU, INTC, AMD, NVDA, TSM]
sector: Compute & AI Compute Accelerators
source: 'https://substack.com/home/post/p-187132686'
source_type: deep-dive
propagated_to: [INTC, NVDA, AMD, TSM, AVGO, 000660, 285A, SNDK, MRVL]
---

# Datacenter CPU Landscape 2026 — SemiAnalysis "CPUs are Back"

## Thesis Delta
The "CPUs are back" inflection — RL training environments + agentic tool-use creating a new datacenter-CPU demand leg distinct from GPUs — most directly **widens AMD's structural lead over [[Theses/INTC - Intel]]** (Venice 256-core Zen6c vs a Diamond Rapids that ships *without SMT* and whose 8-channel mainstream variant was cancelled), and opens two memory side-effects: a new NAND demand vector ([[Theses/NVDA - Nvidia]] Bluefield-4 KV-cache offload to high-speed NAND) and accelerating datacenter LPDDR adoption (Grace/Vera/ARM Venom → LPDDR5X/SOCAMM/LPDDR6), both reinforcing the DRAM-shortage allocation dynamic already in the [[Theses/000660 - SK Hynix]] thesis.

## Summary
SemiAnalysis (Gerald Wong, published 2026-02-10, ingested 2026-06-02) reframes a consensus that has held since 2023 — "GPUs and networking are king; the CPU is a stranded support role." The non-consensus claim: over the prior ~6 months datacenter CPU demand inflected upward, driven by two AI paradigms that are CPU-intensive rather than GPU-intensive. **Reinforcement learning** loops need large, high-performance CPU clusters co-located with GPUs to run the "RL Environment" — code compilation, verification, interpretation, tool use, physics simulation, synthetic-data verification — to keep GPUs from idling. **Agentic / RAG inference** has each agent hitting the internet via tool calls and database queries far more intensively than a human, driving general-purpose CPU buildouts. The concrete tell: Microsoft's "Fairwater" OpenAI datacenter pairs a **48MW CPU+storage building with a 295MW GPU cluster** (~1:6 CPU:GPU power), a ratio the author expects to *rise* with Rubin because accelerators improve perf/watt faster than CPUs. Frontier labs are now "running out of CPUs" for RL and competing directly with cloud providers for commodity x86; Intel's Q4'25 print showed an unexpected datacenter-CPU demand uptick, prompting it to raise 2026 capex and divert wafers from PC to server.

The competitive core is an **Intel-vs-AMD divergence that this cycle widens rather than narrows**. AMD Venice (TSMC N2, 256 Zen6c cores, EMIB-equivalent advanced packaging, 16-channel MRDIMM-12800 at 1.64TB/s, claimed 1.7× perf/watt over 192-core Turin) extends a per-core lead AMD already holds (96-core Turin matches 128-core Granite Rapids). Intel Diamond Rapids commits two self-inflicted wounds: it ships **without SMT** (a post-Spectre/Meltdown core-design choice carried from Lion Cove), capping the flagship at 192 cores / 192 threads and an estimated ~40% gain over Granite Rapids; and Intel **cancelled the mainstream 8-channel Diamond Rapids-SP entirely**, leaving its highest-volume server market with no new generation until at least 2028. AMD is doing the opposite — launching a new 8-channel Venice SP8 platform to attack Intel's enterprise stronghold (Siena successor, up to 128 dense Zen6c cores). The SMT fix doesn't arrive at Intel until Coral Rapids (2028-2029, on 14A or a ported 18A-Ultra). Clearwater Forest, Intel's 288-core E-core part and lead vehicle for Foveros Direct hybrid bonding, is characterized as a near-failure: delayed H2'25→H1'26 on hybrid-bonding integration, only **17% faster than Sierra Forest** despite new core/node/packaging, low hybrid-bonding yields hurting margins — read by the author as a yield-learning vehicle Intel doesn't want to ship in volume (and its successor is cancelled).

The third structural force is **hyperscaler ARM vertical integration permanently closing Intel's addressable market**. AWS Graviton5 (192 Neoverse V3, TSMC 3nm, now the head node for Trainium3), Microsoft Cobalt 200 (132 Neoverse V3), Google Axion (custom 3nm, migrating Gmail/YouTube/Play off x86), and now **ARM itself becoming a chip vendor** with Phoenix (Meta first customer, also OpenAI via Stargate, Cloudflare) mean ARM now competes directly with its own Neoverse licensees. Over 1B Neoverse cores are deployed across 21 CSS licenses / 12 companies; ARM projects CSS >50% of royalty revenue within a couple years. Ampere — the original merchant-ARM champion — was absorbed by SoftBank ($6.5B, 2025) after Oracle divested a business whose CPU purchases collapsed from $48M (FY23) to $3.7M (FY25); execution/timing killed it. Net: the merchant x86 TAM Intel once owned is being eaten from above (AMD per-core lead) and below (hyperscaler + ARM in-house silicon), even as total CPU demand grows.

Finally, the piece ties the CPU cycle to the **DRAM/NAND supercycle**. The 2026 DDR5 shortage means "server CPU allocation will be prioritized to those who can prove a secure memory supply" — accelerating consolidation toward OpenAI, CoreWeave, and the hyperscalers with DRAM negotiating power. AI head nodes (512GB-1TB/socket) are most exposed since memory cost dwarfs CPU cost; cloud/throughput CPUs less so; low-end storage/edge CPUs may be deprioritized as vendors push high-margin SKUs. Two forward memory vectors: NVIDIA's **Bluefield-4 Context Memory Storage Platform** co-packages a Grace CPU + ConnectX-9 to offload model KV-cache to high-speed NAND — a "third network" beyond East-West and North-South, and a net-new NAND demand source ([[Theses/285A - Kioxia]], [[Theses/SNDK - SanDisk]]); and datacenter **LPDDR adoption** (Grace LPDDR5X, Vera SOCAMM, ARM Venom LPDDR6) shifting DRAM mix toward mobile-class parts for power/density.

## Framework / Mental Model
The source advances three reusable frameworks for evaluating datacenter CPUs.

**1. CPU role taxonomy (and its forward trifurcation).** As GPUs captured datacenter power budgets, the CPU split into two roles, now becoming three:
- **Head node** — manages/feeds GPUs; wants high per-core performance, large cache, high memory + IO bandwidth to minimize tail latency. Typically 1 CPU : 2-4 GPUs (1 Vera : 2 Rubin; 1 Venice : 4 MI455X; 1 Graviton5 : 4 Trainium3; 2 x86 : 8 TPUv7). Coherent CPU-GPU memory (NVLink-C2C) lets GPUs use CPU DRAM as KV-cache expansion.
- **Cloud-native socket consolidation** — maximize throughput/requests-per-socket per Watt; retire old inefficient servers (millions of Cascade Lake) and replace with far fewer dense cores at <⅕ power, freeing power budget for GPUs. Consolidation ratios reach 10:1+. Design: high core count, area/power-efficient medium cores, less cache/IO (Intel Sierra Forest Atom cores; AMD Bergamo Zen4c; AWS Graviton; Ampere).
- **Forward trifurcation** — designs are diverging into (a) high-density efficient cloud CPUs (Graviton5), (b) high-perf-per-core + high-bandwidth coherent-memory head nodes (Vera), (c) data-processing/networking CPUs+DPUs for AI data movement and context offload (Bluefield-4). The blur between "NIC with CPU" and "CPU with networking" is widening.

**2. The multi-core interconnect scaling ladder.** Core-count growth forces successive interconnect topologies, each trading latency uniformity for scalability — the lens through which the 2026 designs are read:
- **Crossbar** (all-to-all): connections scale combinatorially (2c=1, 4c=6, 6c=15, 8c=28); practical limit ~4-6 cores.
- **Ring bus** (Intel Nehalem-EX 2010): ring stops in L3 slices; non-uniform latency; counter-rotating dual rings; scales to ~10-24 cores via virtual/dual rings, at the cost of NUMA penalties (intra-ring <50ns vs cross-ring >100ns).
- **Mesh** (Intel Skylake-X 2017→): 2D grid, distributed home agents; Sub-NUMA Clustering to tame latency; scales to ~40 cores monolithic before reticle limit (~26×33mm).
- **Disaggregated mesh** (Intel Sapphire Rapids EMIB → Xeon 6 heterogeneous IO/compute split): chiplets carry the mesh across dies to pass the reticle limit; logically monolithic but latency degrades (47ns Skylake → 59ns SPR), pushing more on-die L2.
- **Vertical / hybrid-bonded disaggregation** (Intel Clearwater Forest / Diamond Rapids Foveros Direct; AMD always-chiplet): stack compute dies on a base die holding mesh+L3+IO, moving cores to the leading node while cache/IO stay on a trailing node.
- **AMD's alternative** — small reusable CCD chiplets around a central IO die (Rome 2019→), a single CCD tapeout serving the whole SKU stack with superior yield/time-to-market vs Intel's large multi-tapeout mesh dies. The structural cost-and-agility advantage behind AMD's share gains.

**3. Socket-consolidation economics.** The replacement math: decommission N old servers, replace with far fewer new dense CPUs that meet the *same total throughput* at a fraction of the power — lowering opex AND freeing datacenter power for GPUs. This is why the CPU refresh is non-discretionary even in a GPU-prioritized capex regime: the power saved is redeployable to accelerators, so a CPU upgrade is effectively a GPU-capacity unlock.

**4. The two-vendor packaging convergence (and its NUMA cost).** A subtler framework runs through the architecture sections: Intel and AMD are *converging* on the same physical structure — compute chiplets around central IO die(s) — from opposite directions, and both pay a NUMA-latency tax for it. AMD started disaggregated (Naples 2017 was "four glued-together desktop die" with four NUMA domains: intra-CCX, inter-CCX, die-to-die MCM, inter-socket) and spent four generations *reducing* NUMA penalty (Rome 2019 centralized all inter-CCX traffic through one IO die → 2 NUMA domains but VMs capped at 4 cores; Milan 2021 widened the CCX to 8 cores via ring bus; Venice 2026 finally adopts EMIB-class advanced packaging for CCD↔IO links and a within-CCD mesh). Intel started monolithic (single-mesh Skylake→Ice Lake) and was *forced* into disaggregation by the reticle limit (Sapphire Rapids EMIB 2023 → Xeon 6 IO/compute split → Diamond Rapids' four CBB dies + two IMH dies). The investment-relevant read: Diamond Rapids "almost looks like a copy of AMD's designs," but Intel's version drops EMIB for cheaper long-substrate traces (worse cross-CBB latency) AND drops SMT, so the convergence lands Intel at AMD's *2017-era* NUMA structure with *2026* costs. Whoever has "the best data fabric" wins — and AMD's small-reusable-CCD model gives it a structural yield, cost, and time-to-market edge that the framework treats as durable.

## Evidence

**Datacenter-CPU era history (the demand-driver arc):**
| Era | Period | CPU growth driver | Design response |
|---|---|---|---|
| PC | 1990s | "mainframe replacement" — PC processors displace DEC/IBM workstations | Pentium Pro (1995) MCM with L2 cache dies; Xeon brand (1998) |
| Dot-com | 2000s | serving the world's internet traffic (Web 2.0, e-commerce, search, 3G) | end of Dennard scaling → multi-core; integrated memory controller + PCIe; SMT; multi-socket (Intel QPI, AMD HyperTransight) |
| Virtualization / cloud | late-2000s-2010s | CapEx→OpEx shift (Great Recession), pay-as-you-use; AWS | hardware virtualization (VMs on hypervisors like VMware ESXi); core partitioning + live migration |
| AI GPU + CPU consolidation | 2022-2025 (post-ChatGPT) | GPUs capture compute; CPU relegated to support | split into head-node vs cloud-native CPUs; socket consolidation 10:1+ |
| RL + Agentic | 2025-2026 (now) | RL environments + agentic tool-use + KV-cache management | CPU demand re-accelerates beyond head nodes; new data/networking CPU class (Bluefield-4) |

Cloud-era context: virtualization is the load-bearing primitive (a single CPU runs many secure VMs via the hypervisor, migratable across cores/sockets/servers for utilization). It was also the attack surface for Spectre/Meltdown — the security event that propagates into Intel's 2026 SMT decision.

**Why RL and agentic workloads are CPU-intensive (the demand mechanism):**
- **RL training loop** — the "RL Environment" must *execute* model-generated actions and *compute the reward*. In coding/math domains this means parallel CPU clusters doing code compilation, verification, interpretation, and tool use; CPUs also run complex physics simulations and verify synthetic data at high precision. Because accelerators improve perf/watt far faster than CPUs, scaling RL widens the CPU:GPU ratio over time — the new bottleneck is keeping GPUs busy, which needs *more* high-performance CPU close to the GPU cluster.
- **Agentic / RAG inference** — RAG models search and use the internet; agentic models invoke tools and query databases. Each agent uses the internet far more intensively than a human (parallel API calls vs. sequential Google searches), driving general-purpose CPU buildouts at AWS (Graviton/Cobalt) and Azure plus incremental x86 purchases for the step-up in internet traffic.
- **Pre-training / fine-tuning** — CPUs store, shard, and index data fed to GPU clusters; also image/video decode for multimodal (though fixed-function media is migrating onto GPUs).

**The "CPUs are back" demand signal:**
| Datapoint | Value |
|---|---|
| Microsoft Fairwater CPU:GPU power | 48MW CPU+storage : 295MW GPU (~1:6, rising) |
| Intel Xeon Scalable shipped (5yr pre-ChatGPT) | >100M units to cloud + enterprise |
| Intel Q4'25 DCAI | unexpected datacenter-CPU demand uptick → raised 2026 capex, PC→server wafer reprioritization |
| AMD 2026 server CPU TAM growth (mgmt) | "strong double digits" |
| Frontier-lab status | "running out of CPUs" for RL; competing with clouds for commodity x86 |

**Intel Diamond Rapids vs AMD Venice (2026 flagships):**
| Attribute | Intel Diamond Rapids | AMD Venice |
|---|---|---|
| Max cores (printed / enabled) | 256 / ~192 mainline | 256 (8× N2 CCDs) / 96 high-freq -F |
| SMT | **None** (P-core, post-Spectre) | Yes |
| Est. perf vs prior gen | ~40% over 128c Granite Rapids | 1.7× perf/watt over 192c Turin |
| Cores per LLC / module | 2 cores share L2 (DCM) | 32 Zen6c in 4×8 mesh per CCD; 4MB L3/core |
| Memory | 16-ch DDR5 | 16-ch MRDIMM-12800 = 1.64TB/s (2.67× Turin) |
| Packaging | Foveros Direct hybrid bond (18A-P on Intel 3-PT) + substrate die-to-die | CoWoS-L / EMIB-equivalent CCD↔IO |
| Mainstream 8-channel SKU | **Cancelled** (no mainstream gen to 2028) | **New SP8 platform** (up to 128 Zen6c) |
| Node | 18A-P cores / Intel 3-PT base | TSMC N2 CCDs / N6 IO |

**The SMT-removal causal chain (Intel's self-inflicted wound):** Spectre/Meltdown (2018) exploited SMT — two threads on one physical core let an attacker snoop the other thread via branch-prediction side channels. Cloud providers rushed to disable SMT, eating up to **30% performance loss**. Intel's core team responded by designing P-cores *without* SMT starting with Lion Cove (2024 client), rationalizing that the saved area improves efficiency — acceptable on PCs because integrated E-cores backstop multi-thread throughput. Carried into Diamond Rapids, this caps the datacenter flagship at 192 threads on 192 cores precisely where datacenter workloads most reward maximum throughput. AMD, less affected by Spectre/Meltdown, kept SMT — so the security event of 2018 propagates into a 2026 competitive gap.

**AMD Zen interconnect evolution (the chiplet learning curve):**
| Gen (year) | Structure | NUMA / limitation |
|---|---|---|
| Naples 7001 (2017) | 4× Zeppelin MCM, 32c, single reusable die (desktop+server+embedded) | 4 NUMA domains; "inconsistent performance" on latency-sensitive code |
| Rome (2019) | 8× N7 CCD around central GF-12nm IO die, 64c; all inter-CCX via IO die | 2 NUMA domains but VMs capped at 4c (16× 4-core nodes) |
| Milan (2021) | CCX widened to 8c via ring bus, reused Rome IO die | VM 4-core cap removed |
| Genoa (2022) / Turin (2024) | 12 → 16 CCDs, DDR5/PCIe5 IO die; Bergamo Zen4c / 192c Turin-Dense Zen5c | core-density variants on shared IO die |
| Venice (2026) | 8× N2 CCD, within-CCD 4×8 mesh, EMIB-class CCD↔IO, split dual-IO die | new die-to-die hop (extra NUMA domain) but far higher per-core perf |

The structural point: AMD offers the full SKU stack from a *single CCD tapeout* (plus IO-die variants), yielding better economics and earlier node migration than Intel's mesh, which needs reticle-sized dies and multiple tapeouts per core-count tier.

**Intel mesh scaling history (reticle wall → disaggregation):** Skylake-X (2017) 28c 6×6 mesh at reticle limit → Ice Lake (2021) 40c 8×7 on 10nm → Sapphire Rapids (2023) forced to 4-die EMIB ("logically monolithic," ~1600mm², latency 47→59ns, more L2 than L3) → Emerald Rapids (2023) cut to 2 dies, 64c, 320MB L3 → Xeon 6 (2024) heterogeneous IO/compute split (IO on Intel 7, compute on Intel 3), Granite Rapids-AP 128c across 5 dies (10×19 mesh). Diamond Rapids breaks the single mesh entirely: 4 CBB + 2 IMH dies, 2 cores share L2 (DCM) — a return to 2008 Dunnington-style core pairing.

**Intel execution flags:**
| Product | Issue |
|---|---|
| Clearwater Forest (288 E-core, 18A) | delayed H2'25→H1'26 (Foveros Direct); only **+17% vs Sierra Forest**; low hybrid-bond yield → margin drag; "yield-learning vehicle," not volume; successor (Rouge River / DMR-HD) **cancelled** |
| Sierra Forest (144 E-core) | limited adoption; 288-core -AP never reached GA (off-roadmap low-volume) |
| Diamond Rapids-SP (8-ch mainstream) | cancelled — abandons highest-volume core market |
| Coral Rapids (SMT returns) | 14A → late 2028 / early 2029 at earliest; may port to 18A-Ultra to pull in |

**ARM / hyperscaler in-house CPUs (the TAM-closure vector):**
| CPU | Cores / Core IP | Node | Role / note |
|---|---|---|---|
| NVIDIA Grace | 72 Neoverse V2 | — | head node; 480GB LPDDR5X, NVLink-C2C 900GB/s; branch-predictor bottleneck slows GB200/GB300 |
| NVIDIA Vera (2026) | 88 custom Olympus (SMT) | 3nm | C2C 1.8TB/s, 1.5TB SOCAMM @1.2TB/s; 2× Grace |
| AWS Graviton5 | 192 Neoverse V3 | TSMC 3nm | now Trainium3 head node; 172B transistors; 12-ch DDR5-8800 |
| MS Cobalt 200 | 132 Neoverse V3 | TSMC 3nm | general-purpose only (Maia 200 uses Intel Granite Rapids) |
| Google Axion C4A/N4A | 72 V2 / 64 N3 | 5nm/3nm | migrating Gmail/YouTube/Play off x86; future TPU head nodes |
| ARM Phoenix | 128 Neoverse V3 | TSMC 3nm | **ARM-as-chip-vendor**; Meta first customer, OpenAI (Stargate), Cloudflare |
| Huawei Kunpeng 950 (2026) | 192 LinxiCore (SMT) | SMIC N+3 | TaiShan 950 SuperPoD; Oracle Exadata + China finance |

**ARM ecosystem scale:** >1B Neoverse cores deployed; 21 CSS licenses / 12 companies; datacenter royalty >2× YoY; CSS projected >50% of royalty revenue. Ampere acquired by SoftBank $6.5B (2025); Oracle Ampere spend $48M (FY23) → $3M (FY24) → $3.7M (FY25).

**The Grace branch-predictor bottleneck (concrete NVDA installed-base drag):** Grace uses ARM Neoverse V2 cores whose branch-target buffer organizes instructions into 32× 2MB virtual address regions. Performance "drops off massively" once the buffer fills beyond 24 regions (hot code churns the buffer → mispredicts); past 32 regions the entire 64MB buffer flushes, the predictor forgets all prior branches, and the front-end starves the ALUs. NVIDIA's own tuning guide shows ~50% speedups from code-locality optimization. This is *why AI workloads are currently slowed by Grace in GB200/GB300* — and why Vera abandons stock Neoverse for a custom SMT-capable Olympus core (6× 128b FP ports vs 4 on V2, 2MB L2/core doubled from Grace, claimed 2× Grace).

**Head-node coherent-memory mechanics:** NVLink-C2C gives the GPU full-bandwidth access to CPU memory as KV-cache expansion beyond HBM's capacity limit — Grace 900GB/s bi-directional to 480GB LPDDR5X; Vera doubles to 1.8TB/s with 1.5TB SOCAMM. This coherent-memory role (not raw CPU perf) is the design center for NVIDIA/ARM head-node CPUs, and the reason head nodes carry 512GB-1TB/socket — the segment most exposed to DRAM-shortage cost inflation.

**Huawei / China CPU vector:** Kunpeng 920 (2019, 64c, first CPU on TSMC CoWoS-S) → Kunpeng 920B (2024, 80c/160t SMT, redesigned for SMIC N+2 after sanctions, 5-year gap) → Kunpeng 950 (2026, 192 LinxiCore SMT, SMIC N+3 per Kirin 9030, 2.9× OLTP over 920B, TaiShan 950 SuperPoD for Oracle Exadata + China finance) → Kunpeng 960 (2028, 96c perf + 256c density variants). US sanctions repeatedly disrupted the roadmap, but Huawei is positioned to take significant Chinese hyperscaler CPU share — a domestic-substitution vector that erodes the addressable market for AMD/Intel in China specifically.

**Merchant-ARM and re-entrant detail:**
- **Ampere** (the cautionary tale): Altra (80c N1) / Altra Max (128c) / AmpereOne (192c 5nm, custom density-optimized core, 2MB L2 to mute noisy-neighbor mesh contention) / AmpereOne-MX roadmap (256c 3nm) / Aurora (512c, AI). Failed on timing — Altra arrived before software was ARM-native; AmpereOne shipped late (Oracle A2 H2'24) just as hyperscalers' own ARM silicon ramped and AMD matched 192c at 3-4× per-core perf. SoftBank bought it ($6.5B) for design talent (Stargate), not the product line.
- **Qualcomm SD2** (2027 re-entry): NUVIA Oryon cores (Gerard Williams III / ex-Apple talent acquired 2021), NVLink Fusion coherent interconnect, Alphawave Semi acquisition (2025) for SerDes/chiplet IP, anchored by Saudi HUMAIN. Risk flag: Williams III + NUVIA team departed Jan 2026; ARM lawsuit won (license preserved). First datacenter foray (Centriq 2400, 2017, 48 Falkor cores) failed — arrived before ARM software readiness, same pattern as Ampere Altra.
- **The merchant-ARM lesson** repeated across Ampere Altra, Qualcomm Centriq, and ARM Phoenix's timing: hyperscalers can co-design software for their own ARM silicon instantly; the *merchant* general-purpose/enterprise market moves far slower to port off x86 — which is why hyperscaler in-house ARM succeeded where merchant ARM (Ampere) stalled.

**Roadmap to 2028:**
| Vendor | 2027 | 2028 |
|---|---|---|
| AMD | Verano (Zen6, ~256c, new 3nm IO die, PCIe7, 200G Ethernet SerDes for MI500/UALoE) | Florence (Zen7, ACE matrix engine, AVX10, A16 backside power, ~320c) |
| Intel | custom Xeon + NVLink-C2C chiplet | Coral Rapids (SMT returns, 14A) late-28/29 |
| ARM | Venom (228 Neoverse V4, N2, **LPDDR6**, PCIe7 AEK) | — |
| Qualcomm | SD2 (NUVIA Oryon, NVLink Fusion, HUMAIN Saudi) ships for revenue | — (NUVIA's G. Williams III departed Jan 2026) |

**Future CPU trends / long-tail disruption (the "does the CPU survive?" question):**
- **Data fabric is the deciding variable.** As sockets and core counts grow with wider/faster memory and IO, NoC designers must deliver very high bisection bandwidth across thousands of mm² of silicon and multiple chiplet crossings while holding full coherency at lower latency than GPU fabrics. "The winning design will come from the one that has the best data fabric" — a direct read-through to AMD's chiplet-fabric lead.
- **Memory architecture divergence** — some designs lean on gigabytes of cache to hide latency; others on CXL memory expanders; possible **return of HBM-on-CPU** (last seen in Sapphire Rapids Xeon Max and AMD MI300C).
- **APU disruption risk to the CPU head-node itself** — AMD's MI300A (integrated CPU+GPU, unified memory) points to a future where APUs remove the discrete CPU head node entirely; RL-specific accelerators could run the RL Environment locally with unified memory, cutting the round-trip to general-purpose CPU clusters. CPO + memory disaggregation (JBOM "Just a Bunch of HBM," Credo Omniconnect gearboxes) could lower CPU attach ratios toward 1 CPU per *rack* of accelerators. The CPU may also end up integrated as the core of a >400T switch. Net: the CPU "lives on as the fundamental core" but its packaging and attach ratio are contested — a long-horizon risk to the merchant CPU unit-volume story even as per-unit content rises.

**CPU BOM-costing framework (SemiAnalysis methodology, behind paywall — structure only):** cost decomposes into (1) active silicon (die sizes × process/metal layers × yielded dies-per-wafer × wafer cost × dies-per-package — e.g., 256c Venice = 8× N2 compute + 2× N6 IO), (2) advanced packaging (CoWoS-L for Venice, EMIB + Foveros Direct 3D for Diamond Rapids; interposer/hybrid-bond area, die-to-die link count, KGD test; packaging yield loss accrues as wasted-good-die cost), (3) traditional packaging (substrate material/layers/area, IPDs, TIM, lid), (4) test (ATE/SLT + burn-in, binning loss). The advanced-packaging-yield-loss term is where Intel's Foveros Direct immaturity (Clearwater Forest) most hurts cost vs AMD's mature CoWoS-L.

**Memory / DRAM-shortage transmission to CPUs:**
| Mechanism | Detail |
|---|---|
| CPU allocation gating | "prioritized to those who can prove secure memory supply" → consolidation to OpenAI/CoreWeave/hyperscalers |
| Most-exposed segment | AI head nodes (512GB-1TB/socket) — memory cost ≫ CPU cost |
| Bluefield-4 (new NAND vector) | Grace + ConnectX-9 co-packaged; KV-cache offload to high-speed NAND; 4× BF4 per Context Memory Storage Platform; "third network" |
| Datacenter LPDDR shift | Grace LPDDR5X, Vera SOCAMM, ARM Venom LPDDR6 — mobile-class DRAM into servers for power/density |
| Future memory expansion | CXL3 (Diamond Rapids), JBOM "Just a Bunch of HBM," Credo Omniconnect gearboxes, possible HBM-on-CPU return (cf. Sapphire Rapids Xeon Max, MI300C) |

## Contradiction Check
- **Supports but complicates [[Theses/INTC - Intel]].** The Q4'25 demand uptick + capex raise + PC→server wafer shift is a near-term revenue positive (the bull-case "DCAI stabilization" leg). But the structural read is negative and *specific*: SMT-less Diamond Rapids (~40% gen-on-gen vs AMD's widening per-core lead), the cancelled 8-channel mainstream SKU (cedes the highest-volume market to AMD SP8 until 2028), Clearwater Forest as a +17% yield-learning vehicle, and Coral Rapids' SMT fix arriving only 2028-2029. Affected assumption: that Intel 18A + foundry turnaround restores *product* competitiveness in server CPUs — the article argues the core-design and SKU-rationalization decisions keep Intel a generation behind in its own x86 stronghold regardless of node. Net: tactical demand tailwind, strategic share erosion.
- **Strengthens [[Theses/AMD - Advanced Micro Devices]].** Venice widens the per-core and platform lead (256c N2, 1.7× perf/watt, MRDIMM 1.64TB/s), and the SP8 8-channel launch directly attacks Intel's enterprise base exactly as Intel exits it — a share-gain catalyst in a "strong double digit"-growth TAM. The chiplet model's structural cost/yield/time-to-market edge over Intel's mesh is reaffirmed. Affected assumption (AMD server-share trajectory): the CPU-demand inflection + Intel self-harm support continued share capture beyond consensus.
- **Adds a net-new bull vector + a risk for [[Theses/NVDA - Nvidia]].** Bull: Vera ($200B-TAM CPU per the prior NVDA thesis) gets 2× Grace perf + custom SMT Olympus core; Bluefield-4 makes the CPU a networking/context-storage anchor, expanding NVIDIA's per-rack silicon content. Risk: Grace's Neoverse-V2 branch-predictor bottleneck is *currently slowing AI workloads on GB200/GB300* — a concrete, under-discussed performance drag on the installed Blackwell base until Vera ships.
- **Reinforces [[Theses/000660 - SK Hynix]] / DRAM supercycle.** DRAM shortage now gates *CPU* allocation (demand-side confirmation of structural tightness), and datacenter LPDDR adoption (Grace/Vera/Venom) adds a server LPDDR demand leg beyond HBM + commodity DDR5. Consistent with the 2026-05-31 "Memory Mania" ingest.
- **Net-new NAND demand vector for [[Theses/285A - Kioxia]] / [[Theses/SNDK - SanDisk]].** Bluefield-4 KV-cache offload to high-speed NAND is a genuinely new high-performance-NAND use case ("third network"). Not in either NAND thesis yet — small today but architecturally significant (model-context tiering to NAND).
- **Foundry beneficiary [[Theses/TSM - Taiwan Semiconductor]].** Nearly every competitive 2026 CPU is TSMC N2/N3 (AMD Venice N2, Graviton5/Cobalt/Axion/Phoenix 3nm, Venom N2, Florence A16); even Intel's mesh/IO leans on Intel 3 while only cores move to 18A. Reinforces TSMC's leading-edge logic monopoly across the CPU vendor set.
- **Tangential [[Theses/AVGO - Broadcom]] / [[Theses/MRVL - Marvell Technology]].** The DPU/networking-CPU convergence (Bluefield-4) and custom-silicon design-services angle (ARM/hyperscaler CPUs need SerDes/IP) touch both, but no direct thesis delta — the article's networking content is NVIDIA-centric.
- **Macro linkages.** [[AI Bubble Risk and Semiconductor Valuations]]: "CPUs are back" is a *new* AI-capex leg (RL + agentic), strengthening the demand-floor pillar — but also adds CPU+DRAM to the cost base behind the $650B monetization threshold. [[Macro & Technology/CXL Memory Disaggregation Framework]]: CXL3, JBOM, Omniconnect, Bluefield-4 context storage are direct memory-disaggregation evidence. [[Macro & Technology/Agentic Internet]]: agentic tool-use as the explicit CPU-demand driver.
- **No-thesis names surfaced:** Ampere (now SoftBank), ARM Holdings (Phoenix/Venom chip-vendor pivot is a business-model transition worth its own coverage), Qualcomm (SD2 datacenter re-entry), Credo (Omniconnect memory gearbox). ARM-as-merchant-chip-vendor is the most thesis-worthy gap.

## Source Excerpts
> "Over the last 6 months this has changed massively… CPUs are now relevant again."
> "A future GPU generation such as Rubin may require an even higher ratio of CPU to GPU power than the 1:6 ratio seen in Fairwater."
> "Frontier AI labs are running out of CPUs for their RL Training needs and are scrambling for CPU allocation by competing directly with the cloud providers for commodity x86 CPU servers."
> "We expect the main 192 core, 192 thread Diamond Rapids to be only around 40% faster… exposing Intel for another generation with lower performance than AMD."
> "Intel has cancelled the mainstream 8-channel Diamond Rapids-SP platform entirely, leaving their highest volume core market without a new generation into at least 2028."
> "Intel showed Clearwater Forest as being only 17% faster than Sierra Forest at the same core counts… Our take is that Intel does not want to produce these chips in high volumes."
> "AMD will introduce a new 8-channel Venice SP8 platform… AMD will see large share gains in the enterprise markets, a traditional Intel stronghold."
> "ARM is taking things further in 2026 and will be offering full datacenter CPU designs, with Meta as its first customer… ARM will now compete directly with its customers who license the Neoverse CSS architecture."
> "This is why AI workloads are currently being slowed by the Grace CPUs in GB200 and GB300."
> "Server CPU allocation will be prioritized to those who can prove to have a secure and available memory supply."
> "Model KV-Cache offload and storage represents a third network being added to the current AI network topology of East-West… and North-South."
