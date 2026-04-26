---
date: 2026-04-26
tags: [macro, technology, CXL, memory-disaggregation, photonics, mental-model, MRVL, AVGO]
status: active
sector: Custom Silicon & Networking Semiconductors
source: vault synthesis — conversation about memory-disaggregation framework + SAN-for-DRAM mental model; builds on [[Research/2026-03-14 - CXL Technology Adoption.md]]
---

# CXL Memory Disaggregation Framework

*SAN-for-DRAM mental model + April 2026 vendor + thesis mapping. Builds on [[Research/2026-03-14 - CXL Technology Adoption.md]].*

## Thesis Delta

- **MRVL** — Celestial AI Photonic Fabric is the physical-layer enabler for CXL.mem at rack scale (1–10 m reach vs ~30 cm electrical PCIe). Memory disaggregation is the single largest binary upside lever in the MRVL thesis: multi-bagger upside on $3.25B Celestial purchase if 2027–2028 architectural primitive validates ($6–12B FY30 revenue at 30–40% TAM capture); $300M ceiling + goodwill impairment if not. Strengthens existing Non-consensus Insight #2 (Celestial as memory-disaggregation, not CPO re-skin) with the historical-pattern framing — Marvell Celestial is the Brocade/Cisco-MDS analog of the SAN era, with the same multi-decade compounding pattern.

- **AVGO** — Indirect exposure via Broadcom Atlas 3 (PCIe 6.0 / CXL 3.1, 144 lanes, 5nm, sampling) and Atlas 4 (PCIe 7.0, 3nm) PCIe+CXL switch silicon — leverages the 2015 PLX acquisition. Atlas franchise is durable adjacency (~$500M–$1B revenue contribution by 2028) but does not compete with Marvell Photonic Fabric at the rack-scale memory-pool layer. CXL is not the AVGO primary AI bet — Tomahawk / Jericho networking + custom XPUs dominate. CXL Atlas growth is a bull-case adjacency, not a thesis driver.

- **NVDA** — NVLink + NVLink Fusion + NVL576 cross-rack memory addressing is the closed-ecosystem alternative to CXL.mem-over-photonic. If CXL wins the open-fabric layer for non-Nvidia compute, Nvidia loses fabric-economics control on AMD / Intel / custom-ASIC fleets. The $2B Marvell March 2026 deal is the containment move — Nvidia paying to keep merchant photonic-fabric silicon inside the NVLink ecosystem rather than the CXL ecosystem.

- **000660 (SK Hynix)** — CXL pooling expands HBM/DRAM consumption per dollar of compute capex (Jevons effect). Higher utilization through pooling means hyperscalers buy MORE memory in absolute terms, not less; HBM TAM expands rather than contracts. Bull for SK Hynix HBM franchise; same logic applies to Micron (no current thesis) and Samsung.

- **285A (Kioxia), SNDK (SanDisk), PSTG (Pure Storage)** — historical-pattern analog: the SAN-for-DRAM cycle does NOT cannibalise NAND/SSD demand; rather, memory pooling at the DRAM tier increases overall data-pipeline throughput, expanding storage ingest/egress demand. Storage-tier players are unaffected by CXL adoption directly.

- **No-thesis-yet adjacency to evaluate** — Astera Labs (ALAB) is the most direct CXL pure-play (Aries CXL retimer + smart cable + Scorpio Smart Fabric Switch; FY2025 ~$830M revenue from $116M in 2023 — fastest-growing CXL beneficiary). Worth a thesis evaluation given the SAN-for-DRAM framework: Astera occupies the "CXL retimer + cable assembly" niche analogous to QLogic/Emulex in the Fibre Channel era.

## Summary

CXL (Compute Express Link) is the open cache-coherent protocol for memory disaggregation — the architectural primitive that lets compute servers access pooled DRAM/HBM over a fabric, with hardware-maintained cache coherence and load/store semantics. After absorbing Gen-Z (Nov 2021) and OpenCAPI (Aug 2022), CXL is the consolidated industry standard with no fragmentation risk; the 2025–2028 trajectory runs from CXL 2.0 memory expansion (production today, Microsoft Azure Nov 2025 first cloud deployment) → CXL 3.x fabric-attached memory pooling at scale (2027–2028 primary inflection).

The decisive mental model: **CXL is SAN for DRAM/HBM**. The architectural pattern is identical — a pool of memory devices in dedicated chassis, accessed by compute servers over a switched fabric, sharing across many consumers, with independent scaling. The historical parallel is exact: SAN did this for NAND/SSD storage 25 years ago (1995–2005), enabled by Fibre Channel and later iSCSI/NVMe-oF; CXL is doing this for DRAM/HBM 25 years later, enabled by PCIe 5.0/6.0 and (for rack-scale reach) photonic interconnect. The two-decade gap reflects the physics tax: DRAM access latency is ~1,000× tighter than NAND latency, so the fabric overhead had to come down to nanosecond scale before disaggregation worked. CXL + photonic fabric is the moment that latency budget closes.

The key sub-distinction: CXL is the **protocol/software** layer (CXL.mem subprotocol on PCIe physical), while the **physical** layer for rack-scale reach is photonic. Marvell Celestial Photonic Fabric is the photonic substrate that extends CXL.mem from ~30 cm electrical PCIe reach to 1–10 m rack-scale reach. CXL and Photonic Fabric are complementary, not substitutes; together they enable rack-scale disaggregation. Standalone CXL on copper PCIe is limited to in-chassis memory expansion (Microsoft's Azure deployment today); CXL+photonic is the rack-scale primitive that captures the trillion-dollar memory-wall workload set.

Investment translation: the same disaggregation cycle that produced the $30B+ SAN switching/array franchise (EMC, NetApp, Brocade, Cisco MDS, QLogic, Emulex) over 1998–2010 is now playing out for memory. **Marvell Celestial is the Brocade/Cisco-MDS analog** (the fabric switch silicon enabling the disaggregation pattern at scale); the photonic interconnect is the Fibre Channel analog (the physical layer that makes the latency tradeoff workable); **Astera Labs is the QLogic/Emulex analog** (HBA / retimer / cable assembly franchise). If the analogy holds, the photonic-fabric-for-memory franchise compounds for a decade once the primitive validates — same as the SAN switching franchise compounded from 1998 onward.

## Framework / Mental Model

### The disaggregation cycle pattern

Resource disaggregation follows a stereotyped pattern. A resource starts local-and-dedicated (per-server SCSI disks, per-server DRAM) — economically inefficient because of stranded capacity (utilization typically 30–50%). The pattern then repeats:

1. **Resource gets too expensive to leave stranded per-server**. Storage hit this in the 1990s; memory hits it in 2025+ — memory is now ~50% of hyperscaler server capex per Microsoft Research, with ~25% stranded at any moment and ~50% of VMs never touching half their allocated memory.

2. **A fabric standard emerges**. Fibre Channel for SAN (1994); CXL for memory (2019, consolidated 2022 after absorbing Gen-Z + OpenCAPI).

3. **Switching silicon vendors emerge to enable scale**. Brocade / McData / QLogic / Emulex for FC SAN (late 1990s); Astera Labs (Aries retimer + Scorpio fabric switch), Marvell XConn ($540M acquisition), Broadcom Atlas, Microchip XpressConnect for CXL (2024+).

4. **Reach extends from in-chassis → rack-scale → cluster-scale**. SAN: Fibre Channel intra-rack → optical FC inter-rack → iSCSI over Ethernet inter-cluster → NVMe-oF over RDMA. CXL: PCIe in-chassis → CXL switches intra-rack → photonic fabric (Marvell Celestial) inter-rack.

5. **Software ecosystem matures over 3–5 years**. SAN required filesystem + multipathing + LVM evolution (1998–2005); CXL needs CUDA / ROCm / JAX driver maturity + Linux CXL Type 2 mainlining + CXL fabric manager standardization (2025–2028).

6. **Utilization gains dominate fabric latency penalty**. SAN added milliseconds to disk access (already milliseconds → ~2× device latency); CXL adds hundreds of nanoseconds to DRAM access (already ~80 ns → ~3–5× device latency) — both clearable by utilization gains because per-server stranded resource is the larger inefficiency.

7. **Industry consolidates onto winners with hyperscaler-direct sales**. Storage: EMC + NetApp captured array-economics; Brocade + Cisco MDS captured switching; QLogic + Emulex captured HBAs. Memory (forward): Samsung / SK Hynix / Micron capture HBM/DRAM economics; Astera Labs / Marvell / Broadcom capture switching/fabric/retimer.

### The fabric-overhead-vs-device-latency ratio

The disaggregation tradeoff is workable when `(device latency + fabric overhead) / device latency` ≤ ~5×. Beyond this ratio, the application latency penalty exceeds what utilization gains can offset.

| Tier | Native device latency | Fabric overhead | Ratio | Disaggregation viable? |
|---|---|---|---|---|
| L1 cache | ~1 ns | (cannot disaggregate) | N/A | No — coherence physics |
| L2/L3 cache | ~10 ns | (cannot disaggregate practically) | N/A | No — coherence physics |
| Local DRAM (DDR5) | ~80 ns | NUMA: 200 ns; CXL: 250–500 ns | 2–5× | **Yes — CXL.mem at edge of viable** |
| HBM (off-package) | ~150 ns | Photonic fabric: 250–500 ns | 1.5–3× | **Yes — Photonic Fabric works** |
| NVMe SSD | ~30–50 μs | NVMe-oF: 50–200 μs | 1.5–5× | Yes — production today |
| NAND (HDD-class era) | ~10 ms | SAN fabric: 10–20 ms | 1–2× | Yes — production for 25 years |

Memory disaggregation sits at the edge of the viable ratio — workable, but with workload-dependent penalty. Microsoft benchmarking found 20% of applications see no penalty, 23% see <5% slowdown, 25% see >20% degradation, and 12% see >30% slowdown. This is precisely why hyperscaler adoption is workload-segmented rather than universal — capacity-bound workloads (large model weights, KV cache, embedding tables) benefit; bandwidth-bound workloads (training compute, real-time inference of small models) do not.

### CXL stack vs alternatives

| Layer | CXL.mem | NVLink + NVL576 | NVMe-oF (storage analog) | RDMA / GPUDirect (incumbent) |
|---|---|---|---|---|
| Protocol semantics | Hardware cache-coherent load/store | Proprietary cache-coherent + memory pooling | Block-level RDMA | RDMA verbs (kernel bypass) |
| Physical layer | PCIe 5.0/6.0 + photonic for rack-scale | NVLink 5.0/6.0 + Nvidia photonic options | Ethernet / InfiniBand | Ethernet / InfiniBand |
| Standard openness | Open, multi-vendor | Closed (Nvidia-controlled, partner-licensed via NVLink Fusion) | Open | Open |
| Coherence domain | Cross-vendor accelerators | Nvidia-only (or NVLink Fusion partner silicon under Nvidia toll) | None — block-level | None — RDMA-aware applications only |
| Software requirements | CXL.mem driver in CUDA / ROCm / JAX | NVLink-Sharp + Magnum IO (mature) | Filesystem + multipathing | Verbs API + application protocol awareness |
| Latency budget end-to-end | ~200–500 ns | ~150 ns NVLink intra-rack | ~50–200 μs | ~1–5 μs |
| Production maturity April 2026 | CXL 2.0 expansion in production (Azure); CXL 3.x switching late 2026 | NVLink 5.0 in production; NVLink 6.0 + NVL576 H2 2026 | Production for 5+ years | Production for 10+ years |

CXL competes with NVLink at the protocol-semantic layer (cache-coherent memory access) but CXL is open-standard while NVLink is proprietary-with-toll. The strategic split: AMD / Intel / hyperscaler-custom-ASIC compute uses CXL.mem for memory disaggregation; Nvidia compute uses NVLink + NVL576 for the equivalent capability. The two coexist as the open-vs-closed ecosystem split, with the same architectural primitive (rack-scale memory pooling) implemented differently.

## Evidence

### CXL versions and capabilities

| Version | Released | Key capability | Physical layer | Production status April 2026 |
|---|---|---|---|---|
| CXL 1.0/1.1 | 2019 | Cache-coherent device-attached memory; CXL.io + CXL.cache + CXL.mem | PCIe 5.0 (32 GT/s) | Mature |
| CXL 2.0 | 2020 | Memory pooling between hosts; switched topology; SR-IOV | PCIe 5.0 | **In production — Microsoft Azure Nov 2025 first cloud deployment** |
| CXL 3.0 | 2022 | Fabric-attached memory; multi-host coherence; switched fabric scaling | PCIe 6.0 (64 GT/s) | Switch silicon sampling (Atlas 3, Marvell XConn) |
| CXL 3.1 | Nov 2023 | TEE-IO security; fabric-scale extensions | PCIe 6.0 | Atlas 3, Montage M88MX6852 sampling 2025–2026 |
| CXL 4.0 | 2026 (expected) | PCIe 7.0 backbone; further fabric extensions | PCIe 7.0 (128 GT/s) | IP-only (Synopsys, Cadence offer 4.0 IP) |

### Latency budgets across the memory hierarchy

| Access type | Latency | Bandwidth |
|---|---|---|
| Local L1 cache | 1 ns | TBs/s per core |
| Local L3 cache | 10–15 ns | ~500 GB/s |
| Local DDR5 DRAM | 80–90 ns | 50 GB/s per channel; 400–600 GB/s aggregate per socket |
| Local HBM3E (in-package) | 100–150 ns | 7.2 TB/s (Hopper / Blackwell-class) |
| NUMA remote-socket DRAM | 200–250 ns | ~50 GB/s via UPI |
| CXL 2.0 attached DRAM (no switch) | 170–250 ns | 50 GB/s (PCIe 5.0 x16) |
| CXL 3.x switched DRAM pool | 250–500 ns | 100 GB/s (PCIe 6.0 x16) |
| Photonic-fabric attached HBM (Marvell Celestial Gen 1) | 100–200 ns | 16 Tbps/chiplet (~2 TB/s) |
| Photonic-fabric Gen 2 (Celestial 2027) | 100–200 ns | 64 Tbps/chiplet (~8 TB/s) |
| NVLink 5.0 intra-rack (NVL72) | 150 ns | 1.8 TB/s bidirectional per GPU |
| NVMe-oF SSD (RDMA) | 50–200 μs | ~10 GB/s |
| Network-attached SSD (TCP/IP iSCSI) | 1–5 ms | ~1 GB/s |

### End-market use cases mapped to fabric viability

| Use case | Memory pool size needed | Workload sensitivity | Best fabric |
|---|---|---|---|
| Trillion-parameter MoE inference (GPT-5 scale, Claude Opus 4+) | 1.5–5 TB per model | Capacity-bound | CXL.mem on copper or photonic |
| Multi-million-token reasoning + agentic | 0.5–2 TB KV cache per session | Bandwidth-mixed | Photonic Fabric required |
| Multi-tenant inference serving | 5–20 TB shared pool | Capacity-bound | CXL.mem switched pool |
| Recommendation embeddings (Meta, TikTok, Google) | 5–50 TB embedding tables | Capacity-bound | CXL.mem switched pool |
| Vector databases / RAG at scale | 10–100 TB per cluster | Capacity-bound | CXL.mem switched pool |
| Frontier model training | 5–50 TB per training cluster | Bandwidth-bound | Photonic Fabric required |
| HPC scientific compute (genomics, weather, seismic) | 1–10 TB per simulation | Mixed | CXL.mem or Photonic Fabric depending on compute layer |

The single most important driver is **reasoning / agentic inference** — as frontier model providers move from chat to agentic deployment, KV cache + activation memory per session grows 10–100× — this is the workload that makes memory disaggregation a 2027–2028 architectural primitive rather than a 2030+ adjunct. The second most important is **recommendation / embedding workloads** at hyperscale where today's per-chip replication of TB-scale tables is a known capex inefficiency hyperscalers have publicly acknowledged.

### TAM scenarios (April 2026 update)

| Layer | 2026 size | 2030 base | 2030 bull |
|---|---|---|---|
| Total CXL ecosystem (Yole) | ~$2B | $15B | $25B |
| HBM market (total — SemiAnalysis) | ~$50B | ~$130B | ~$180B |
| Photonic interconnect (switch + fabric) | ~$1.5B | ~$8B | ~$25B |
| Memory-fabric photonics specifically | <$0.5B | $3–5B | $15–25B |
| Marvell Celestial guide | $500M Q4 FY28 / $1B FY29 | $2–4B FY30 (10–15% capture) | $6–12B FY30 (30–40% capture) |
| Astera Labs Aries (CXL retimer + smart cable) | ~$300M of $830M total FY25 | ~$2B | ~$5B |
| Broadcom Atlas (PCIe + CXL switch) | ~$500M–$1B est | ~$2B | ~$3–4B |

Comparable scale references: Nvidia NVLink franchise generates ~$3–4B in fabric-attached revenue today; the SAN switching market peaked at ~$8B annually in the 2010s; memory-fabric photonics could reach 2–3× current NVLink scale by 2030 if memory disaggregation becomes the dominant scale-up architecture.

### 2026 production milestones (timeline for thesis monitoring)

- **March 2026**: Marvell-Nvidia $2B NVLink Fusion deal — implicit acknowledgment that hyperscalers will mix non-Nvidia compute with Nvidia scale-up; CXL.mem adoption follows the same logic
- **April 2026**: Anthropic-Google-Broadcom 3.5GW deal extends through 2031 — Google TPU + Broadcom networking + (probable) CXL-attached DRAM memory pools
- **Q2 FY27 (May 2026)**: Marvell Q1 FY27 earnings — first Celestial integration commentary
- **June 2026**: OCP Summit — CXL 3.1 fabric switch silicon deployment evidence; UALink vs NVLink Fusion vs SUE evidence
- **Q3 FY27 (Aug 2026)**: Marvell Q2 FY27 earnings — Celestial Photonic Fabric chiplet tape-out status
- **H2 2026**: Nvidia Vera Rubin / NVL576 production launch — NVLink 6.0 with cross-rack memory addressing; sets the closed-ecosystem benchmark CXL.mem must beat
- **November 2026**: AWS re:Invent — likely Trainium 3 production scale + Trainium 4 design partner signal; both will use CXL or proprietary memory architecture
- **2027**: First production CXL 3.x fabric deployments at hyperscale; Linux CXL Type 2 mainlining (per ABI Research, "no earlier than 2027")
- **2028**: Marvell Photonic Fabric first material revenue ($500M Q4 FY28 guide); inflection on whether memory disaggregation is a 2027–2028 primitive or a 2030+ one

### Vendor landscape (April 2026 — updates [[Research/2026-03-14 - CXL Technology Adoption.md]])

| Vendor | Product | CXL/photonic role | SAN-era analog | Investment exposure |
|---|---|---|---|---|
| **Marvell** | Celestial Photonic Fabric (16/64 Tbps chiplet); XConn switch ($540M acquisition); Inphi DSP | Photonic memory-fabric; switching | **Brocade / Cisco MDS** | [[Theses/MRVL - Marvell Technology]] |
| **Astera Labs** | Aries CXL retimer; Scorpio Smart Fabric Switch; smart cable | CXL retimer + cable assembly + switch | **QLogic / Emulex** (HBAs) | No thesis — evaluate |
| **Broadcom** | Atlas 3 (PCIe 6.0/CXL 3.1, 144 lanes, 5nm); Atlas 4 (PCIe 7.0, 3nm) | PCIe + CXL switch silicon | **Cisco MDS** (silicon layer) | [[Theses/AVGO - Broadcom]] |
| **Microchip** | XpressConnect CXL/PCIe retimers; Gen 6 PCIe switches with CXL fabric | CXL retimer + switch | QLogic-adjacent | No thesis |
| **Synopsys / Cadence** | CXL controller IP through 4.0 (~92% market share combined) | IP licensing | Verisign-equivalent for protocols | No thesis |
| **Montage Technology** | World's first MXC (May 2022); CXL 3.1 MXC M88MX6852 (Sep 2025, 70 ns latency) | CXL memory expander controller | Adaptec / LSI | China-listed, no thesis |
| **Samsung** | CMM-D modules (128/256 GB CXL 2.0); CMM-B pooling appliance; CMM-Ax accelerator; SCMC management software | DRAM + module + appliance | EMC / NetApp (array layer) | No thesis |
| **SK Hynix** | 96/128 GB CMM-DDR5 modules (first validated, April 2025); proprietary CXL controller via TSMC for 3.0/3.1 | DRAM + module | EMC-equivalent | [[Theses/000660 - SK Hynix]] |
| **Micron** | CZ120 modules (128/256 GB CXL 2.0); furthest along in volume production | DRAM + module | EMC-equivalent | No thesis |
| **Ayar Labs** | TeraPHY photonic chiplet | Direct Celestial competitor at photonic interconnect layer | Smaller HBA vendors | No thesis |
| **Lightmatter** | Passage photonic interposer | Optical-compute-oriented; adjacent | None | No thesis |
| **Nvidia** | NVLink + NVLink Fusion + NVL576 | Closed-ecosystem alternative | n/a (CISCO-equivalent control of own ecosystem) | [[Theses/NVDA - Nvidia]] |

## Contradiction Check

What could break the SAN-for-DRAM analogy and the memory-disaggregation thesis?

1. **NVLink Fusion captures the open-fabric layer** — if Nvidia's NVLink Fusion + Vera Rubin memory addressing satisfies the disaggregation use cases (inference, agentic, recommendation embeddings) within the Nvidia ecosystem, the CXL.mem TAM compresses to AMD / Intel / custom-ASIC compute (~30–40% of accelerator deployments by 2028). Probability: medium. Marvell Celestial bet still works in this scenario but TAM is ~half of bull case. The strongest contradiction.

2. **Hyperscalers in-source disaggregation** — Google's Apollo OCS already serves a similar inter-pod memory-domain function for TPU. AWS Nitro Memory Fabric (rumored) could bypass merchant CXL switch silicon entirely. Probability: medium. Eliminates merchant CXL switch silicon revenue but does NOT eliminate the underlying memory-fabric photonic primitive — hyperscalers still buy photonic interconnect silicon from Marvell or competitors. SAN-era analog: Google built its own inter-data-center optical transport (B4) but still bought Lumentum / Coherent components.

3. **HBM-on-package scaling outpaces disaggregation need** — if HBM4 (2026–2027, 16-Hi stacks at 32–48 GB per stack, 8–12 stacks per package = 256–576 GB per chip) and HBM5 (2028+, ~1 TB per chip) keep memory in-package faster than workload memory needs grow, disaggregation becomes optional rather than necessary. Probability: low — workload memory needs (trillion-param MoE, multi-million-token agentic) are growing 10–100× per generation, faster than HBM stacking density (~2× per generation).

4. **Photonic latency does not close** — if photonic transceiver + SerDes overhead does not compress to <500 ns total fabric latency, the ratio threshold breaks and CXL.mem disaggregation stays niche. Probability: low — Marvell Celestial OCI architecture targets <100 ns chiplet-to-chiplet, well within budget. Lightmatter and Ayar Labs target similar latencies.

5. **Cost-utilization tradeoff doesn't close** — photonic interconnect at ~$50/Gbps vs electrical ~$10/Gbps requires ≥5× utilization gain to amortize. If real-world utilization gains are smaller (2–3×), the economics don't work outside narrow workload niches. Probability: medium for early years (2026–2028), low for later years (2029+) as photonic component costs compress with volume. SAN analog: Fibre Channel was 5–10× more expensive than SCSI in 1998 but volume drove ~80% cost compression by 2005.

6. **Software ecosystem stalls** — ABI Research expects CXL 3.0/3.1 software ecosystem mature "no earlier than 2027." If CUDA / ROCm / JAX driver support slips beyond 2028, the architectural primitive validates but commercial adoption lags 2–3 years. Probability: medium. This is the most likely real-world friction. SAN analog: the file-system + multipathing + LVM stack took ~5 years (1998–2003) to mature; CXL software stack is on a similar trajectory.

7. **The SAN analogy doesn't actually hold** — counter-argument: NAND access semantics (block-level batched I/O) are fundamentally different from DRAM (load/store byte-level), so the historical pattern may not transfer cleanly. Specifically, applications historically rewrote to batch SAN I/O to hide latency; CPUs cannot batch CXL.mem load/store the same way (latency is per-instruction). Probability: this is a misframing — the analogy holds at the **architectural pattern** level (pool + fabric + sharing + utilization gain + standards consolidation + vendor-economics distribution), not at the semantic level. The semantics are different, but the disaggregation cycle pattern is the same. Counter-argument: hardware prefetching + speculative execution + cache hierarchy hides much of the per-instruction latency, similar to how OS buffering hides per-block SAN latency.

8. **Power consumption breaks the economics** — photonic interconnect at scale could add material rack-power overhead that hyperscalers find prohibitive. Probability: low — photonic actually saves power at high bandwidth (~3× reduction at >100 Tbps per Bailly / TH6-Davisson data), and CXL pooling enables stranded-memory utilization that reduces total rack count.

The strongest contradiction is #1 (NVLink Fusion captures Nvidia compute). But even in that scenario, the open-CXL ecosystem (~30–40% of accelerator deployments by 2028) is large enough to support a multi-billion-dollar Marvell Photonic Fabric franchise. The SAN analogy is robust to most contradictions because the underlying physics + economics drivers (memory wall, stranded-resource economics, fabric latency in viable ratio) are independent of vendor-strategy outcomes.

## Source Excerpts

This note synthesizes prior vault research and conversational framework — no external excerpts.

Cross-references:
- [[Research/2026-03-14 - CXL Technology Adoption.md]] — primary CXL deep-dive (March 2026): standards consolidation, Microsoft Azure Nov 2025 production, Yole $15B 2028 TAM, latency penalty (25% workloads >20% degradation), Astera Labs / Marvell / Broadcom Atlas / Microchip / Synopsys / Cadence / Samsung / SK Hynix / Micron landscape. This note layers the SAN-for-DRAM mental model + April 2026 Marvell Celestial connection on top.
- [[Sectors/Custom Silicon & Networking Semiconductors]] — §Macro shifts → Architectural transition — memory disaggregation / Photonic Fabric; §Investor heuristics → "Non-consensus insight — Photonic Fabric is the asymmetric MRVL upside"
- [[Theses/MRVL - Marvell Technology]] — §Industry Context → Memory disaggregation deep-dive (use-case table + TAM table + upside-constraints list); Bull Case driver #3 (Celestial ramps); Bear Case driver #3 (Celestial integration slips); Non-consensus Insight #2 (Celestial as memory-disaggregation architecture, not CPO re-skin)
- [[Theses/AVGO - Broadcom]] — Atlas franchise (PCIe + CXL switch silicon); Tomahawk / Jericho remain primary AI bet; CXL is bull-case adjacency not core driver
- [[Theses/NVDA - Nvidia]] — NVLink Fusion + NVL576 closed-ecosystem alternative; $2B Marvell containment move
- [[Theses/000660 - SK Hynix]] — HBM consumer beneficiary of CXL pooling expanding memory consumption per dollar of compute capex (Jevons effect)
- [[Theses/PSTG - Pure Storage]] — SAN-era incumbent; not directly affected by CXL but framework-relevant for understanding the pattern
