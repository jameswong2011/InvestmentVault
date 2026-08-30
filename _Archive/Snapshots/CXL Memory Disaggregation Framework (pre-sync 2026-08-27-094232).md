---
snapshot_of: "[[Macro & Technology/CXL Memory Disaggregation Framework]]"
snapshot_date: 2026-08-27
snapshot_trigger: sync
snapshot_batch: sync-2026-08-27-094232
publish: true
date: 2026-04-26
tags: [macro, technology, CXL, memory-disaggregation, photonics, mental-model, MRVL, AVGO]
status: active
sector: Custom Silicon & Networking Semiconductors
source: vault synthesis — conversation about memory-disaggregation framework + SAN-for-DRAM mental model; builds on [[Research/2026-03-14 - CXL Technology Adoption.md]]
---
> [!question] 2026-05-26 → Addressed 2026-05-26
> **Prompt:** *What is the latest on this trend, can you answer the incremental delta since last research date.*
>
> **Response:** Memory-disaggregation thesis strengthened in the month since the 2026-04-26 base — no Contradiction Check item flipped. The proof point: Astera Labs Q1 (reported May 5) booked a custom CXL **KV-cache** design win + Leo controller ramp on Azure M-series, directly validating the framework's stated #1 driver (agentic-inference KV-cache); Marvell guides CXL+NIC XPU-attach >$2B by FY29 with first Celestial commentary due May 27. Full detail: §Evidence → Incremental delta — May 2026 update.

# CXL Memory Disaggregation Framework

*SAN-for-DRAM mental model + April 2026 vendor + thesis mapping. Builds on [[Research/2026-03-14 - CXL Technology Adoption.md]].*

## Thesis Delta

- **MRVL:** Celestial AI Photonic Fabric is the physical-layer enabler for CXL.mem at rack scale (1–10 m reach vs ~30 cm electrical PCIe). Memory disaggregation is the single largest binary upside lever in the MRVL thesis: multi-bagger upside on $3.25B Celestial purchase if 2027–2028 architectural primitive validates ($6–12B FY30 revenue at 30–40% TAM capture); $300M ceiling + goodwill impairment if not. Strengthens existing Non-consensus Insight #2 (Celestial as memory-disaggregation, not CPO re-skin) with the historical-pattern framing: Marvell Celestial is the Brocade/Cisco-MDS analog of the SAN era, with the same multi-decade compounding pattern.
	- **Update 2026-07-10:** Celestial gen-1 chiplet "already selected by a tier 1 hyperscaler for its next-generation XPU scale-up networks" (May 27 call, the note's flagged milestone, landed positive; scale-up optics outlook >2× the prior ~$150M). UBS (Jun 30, PT $230→$340) is the first sell-side underwriting of MRVL CXL as a P&L line: ~$1B CY27 / ~$2B CY28 via XPU-attach at two US hyperscalers. Offsets: the Dec-2025 ">$2B CXL+NIC by FY29" guide was NOT restated (replaced by ambiguous ">$1B" XPU-attach phrasing), XConn guided to only ~$100M FY28, Structera has zero disclosed customers with sampling starting CQ3 2026, and the stock re-rated first (~70x fwd P/E, consensus PT ~$249 below price, S&P 500 add Jun 22). Full detail: §Evidence → Incremental delta, July 2026.

- **AVGO:** Indirect exposure via Broadcom Atlas 3 (PCIe 6.0 / CXL 3.1, 144 lanes, 5nm, sampling) and Atlas 4 (PCIe 7.0, 3nm) PCIe+CXL switch silicon; leverages the 2015 PLX acquisition. Atlas franchise is durable adjacency (~$500M–$1B revenue contribution by 2028) but does not compete with Marvell Photonic Fabric at the rack-scale memory-pool layer. CXL is not the AVGO primary AI bet: Tomahawk / Jericho networking + custom XPUs dominate. CXL Atlas growth is a bull-case adjacency, not a thesis driver.

- **NVDA:** NVLink + NVLink Fusion + NVL576 cross-rack memory addressing is the closed-ecosystem alternative to CXL.mem-over-photonic. If CXL wins the open-fabric layer for non-Nvidia compute, Nvidia loses fabric-economics control on AMD / Intel / custom-ASIC fleets. The $2B Marvell March 2026 deal is the containment move: Nvidia paying to keep merchant photonic-fabric silicon inside the NVLink ecosystem rather than the CXL ecosystem.
	- **Update 2026-07-10:** containment visibly succeeding. The marquee GPU-adjacent KV-cache socket is standardized on Ethernet-attached NAND (CMX / BlueField-4, H2 2026, zero CXL in the partner stack), Rubin CPX was cancelled in favour of Groq LPX SRAM (~$20B license), Enfabrica (the one shipping Ethernet+CXL memory fabric) was absorbed for ~$900M, and NVLink Fusion added Marvell ("first Fusion partner"), Lightmatter, and ALAB itself. CXL's inference beachhead is confined to the x86 CPU-attached middle tier.

- **000660 (SK Hynix):** CXL pooling expands HBM/DRAM consumption per dollar of compute capex (Jevons effect). Higher utilization through pooling means hyperscalers buy MORE memory in absolute terms, not less; HBM TAM expands rather than contracts. Bull for SK Hynix HBM franchise; same logic applies to Micron (no current thesis) and Samsung.

- **285A (Kioxia), SNDK (SanDisk), PSTG (Pure Storage):** historical-pattern analog: the SAN-for-DRAM cycle does NOT cannibalise NAND/SSD demand; rather, memory pooling at the DRAM tier increases overall data-pipeline throughput, expanding storage ingest/egress demand. Storage-tier players are unaffected by CXL adoption directly.
	- **Revision 2026-07-10:** "unaffected" no longer holds. NAND is now competing FOR the KV-cache capacity tier, not sitting below it. HBF (SK Hynix + SanDisk OCP standardization Feb 2026; >1.6 TB/s, 512 GB/stack, 18.8× concurrent-query simulation on 10M-token KV cache; AIN samples H2 2026) plus Nvidia CMX Ethernet-NAND target exactly the pool CXL DRAM wants. SNDK gains a direct new lever from the inference memory wall; Kioxia has no disclosed HBF seat (monitor). Recorded as new Contradiction #9.

- **No-thesis-yet adjacency to evaluate:** Astera Labs (ALAB) is the most direct CXL pure-play (Aries CXL retimer + smart cable + Scorpio Smart Fabric Switch; FY2025 ~$830M revenue from $116M in 2023, fastest-growing CXL beneficiary). Worth a thesis evaluation given the SAN-for-DRAM framework: Astera occupies the "CXL retimer + cable assembly" niche analogous to QLogic/Emulex in the Fibre Channel era.
	- **Update 2026-07-10:** evaluation resolves **validated-but-priced**. Validation: Leo on Azure M-series (private beta → GA by YE2026, the only public-cloud CXL deployment), hyperscaler KV-cache custom-Leo win (ships 2027), Scorpio X 320-lane fabric switch ramping 2H26. Price: $71.6B mcap / ~70× EV/S TTM / ~123× fwd P/E / +352% 52-wk, chairman's $60.5M sale (Jul 1), BofA + UBS neutral even at raised PTs. Moat: retimer niche is crowding (Broadcom retimer+switch bundling, Microchip <12 ns XpressConnect, Marvell Alaska P), and the note's own QLogic/Emulex analog commoditized within ~5 years of the SAN build-out peak, which argues against paying peak multiples for the HBA layer. No entry at current price; re-look on material derating. Checkpoint: Q2 print Aug 4.

- **PENG (Penguin Solutions), new adjacency to evaluate (2026-07-10):** the only company with in-window P&L-visible AI-inference CXL revenue: FQ3 (reported Jul 7) revenue $478.7M +48% YoY, Integrated Memory segment $275M +111% YoY, CXL expansion cards "generating both revenue and new bookings," a tier-1 financial-services customer repeat-ordering KV-cache servers (11 TB DDR5+CXL, built on ALAB Leo controllers), FY26 growth guide raised 12%→22%, preliminary FY27 ~30%. Critical frame: systems integrator / layer-renter on merchant CXL silicon (Value-Layer-Monopoly: no owned layer, SMART Modular commodity heritage). Treat as the cleanest 'demand tell' for inference-pulled CXL and a possible small convex position, not a compounder. Worth a `/thesis` pass with valuation work.

## Summary

CXL (Compute Express Link) is the open cache-coherent protocol for memory disaggregation, the architectural primitive that lets compute servers access pooled DRAM/HBM over a fabric, with hardware-maintained cache coherence and load/store semantics. After absorbing Gen-Z (Nov 2021) and OpenCAPI (Aug 2022), CXL is the consolidated industry standard with no fragmentation risk; the 2025–2028 trajectory runs from CXL 2.0 memory expansion (production today, Microsoft Azure Nov 2025 first cloud deployment) → CXL 3.x fabric-attached memory pooling at scale (2027–2028 primary inflection).

The decisive mental model: **CXL is SAN for DRAM/HBM**. The architectural pattern is identical: a pool of memory devices in dedicated chassis, accessed by compute servers over a switched fabric, sharing across many consumers, with independent scaling. The historical parallel is exact: SAN did this for NAND/SSD storage 25 years ago (1995–2005), enabled by Fibre Channel and later iSCSI/NVMe-oF; CXL is doing this for DRAM/HBM 25 years later, enabled by PCIe 5.0/6.0 and (for rack-scale reach) photonic interconnect. The two-decade gap reflects the physics tax: DRAM access latency is ~1,000× tighter than NAND latency, so the fabric overhead had to come down to nanosecond scale before disaggregation worked. CXL + photonic fabric is the moment that latency budget closes.

The key sub-distinction: CXL is the **protocol/software** layer (CXL.mem subprotocol on PCIe physical), while the **physical** layer for rack-scale reach is photonic. Marvell Celestial Photonic Fabric is the photonic substrate that extends CXL.mem from ~30 cm electrical PCIe reach to 1–10 m rack-scale reach. CXL and Photonic Fabric are complementary, not substitutes; together they enable rack-scale disaggregation. Standalone CXL on copper PCIe is limited to in-chassis memory expansion (Microsoft's Azure deployment today); CXL+photonic is the rack-scale primitive that captures the trillion-dollar memory-wall workload set.

Investment translation: the same disaggregation cycle that produced the $30B+ SAN switching/array franchise (EMC, NetApp, Brocade, Cisco MDS, QLogic, Emulex) over 1998–2010 is now playing out for memory. **Marvell Celestial is the Brocade/Cisco-MDS analog** (the fabric switch silicon enabling the disaggregation pattern at scale); the photonic interconnect is the Fibre Channel analog (the physical layer that makes the latency tradeoff workable); **Astera Labs is the QLogic/Emulex analog** (HBA / retimer / cable assembly franchise). If the analogy holds, the photonic-fabric-for-memory franchise compounds for a decade once the primitive validates, same as the SAN switching franchise compounded from 1998 onward.

## Framework / Mental Model

### The disaggregation cycle pattern

Resource disaggregation follows a stereotyped pattern. A resource starts local-and-dedicated (per-server SCSI disks, per-server DRAM), economically inefficient because of stranded capacity (utilization typically 30–50%). The pattern then repeats:

1. **Resource gets too expensive to leave stranded per-server**. Storage hit this in the 1990s; memory hits it in 2025+: memory is now ~50% of hyperscaler server capex per Microsoft Research, with ~25% stranded at any moment and ~50% of VMs never touching half their allocated memory.

2. **A fabric standard emerges**. Fibre Channel for SAN (1994); CXL for memory (2019, consolidated 2022 after absorbing Gen-Z + OpenCAPI).

3. **Switching silicon vendors emerge to enable scale**. Brocade / McData / QLogic / Emulex for FC SAN (late 1990s); Astera Labs (Aries retimer + Scorpio fabric switch), Marvell XConn ($540M acquisition), Broadcom Atlas, Microchip XpressConnect for CXL (2024+).

4. **Reach extends from in-chassis → rack-scale → cluster-scale**. SAN: Fibre Channel intra-rack → optical FC inter-rack → iSCSI over Ethernet inter-cluster → NVMe-oF over RDMA. CXL: PCIe in-chassis → CXL switches intra-rack → photonic fabric (Marvell Celestial) inter-rack.

5. **Software ecosystem matures over 3–5 years**. SAN required filesystem + multipathing + LVM evolution (1998–2005); CXL needs CUDA / ROCm / JAX driver maturity + Linux CXL Type 2 mainlining + CXL fabric manager standardization (2025–2028).

6. **Utilization gains dominate fabric latency penalty**. SAN added milliseconds to disk access (already milliseconds → ~2× device latency); CXL adds hundreds of nanoseconds to DRAM access (already ~80 ns → ~3–5× device latency); both clearable by utilization gains because per-server stranded resource is the larger inefficiency.

7. **Industry consolidates onto winners with hyperscaler-direct sales**. Storage: EMC + NetApp captured array-economics; Brocade + Cisco MDS captured switching; QLogic + Emulex captured HBAs. Memory (forward): Samsung / SK Hynix / Micron capture HBM/DRAM economics; Astera Labs / Marvell / Broadcom capture switching/fabric/retimer.

### The fabric-overhead-vs-device-latency ratio

The disaggregation tradeoff is workable when `(device latency + fabric overhead) / device latency` ≤ ~5×. Beyond this ratio, the application latency penalty exceeds what utilization gains can offset.

| Tier | Native device latency | Fabric overhead | Ratio | Disaggregation viable? |
|---|---|---|---|---|
| L1 cache | ~1 ns | (cannot disaggregate) | N/A | No: coherence physics |
| L2/L3 cache | ~10 ns | (cannot disaggregate practically) | N/A | No: coherence physics |
| Local DRAM (DDR5) | ~80 ns | NUMA: 200 ns; CXL: 250–500 ns | 2–5× | **Yes: CXL.mem at edge of viable** |
| HBM (off-package) | ~150 ns | Photonic fabric: 250–500 ns | 1.5–3× | **Yes: Photonic Fabric works** |
| NVMe SSD | ~30–50 μs | NVMe-oF: 50–200 μs | 1.5–5× | Yes: production today |
| NAND (HDD-class era) | ~10 ms | SAN fabric: 10–20 ms | 1–2× | Yes: production for 25 years |

Memory disaggregation sits at the edge of the viable ratio: workable, but with workload-dependent penalty. Microsoft benchmarking found 20% of applications see no penalty, 23% see <5% slowdown, 25% see >20% degradation, and 12% see >30% slowdown. This is precisely why hyperscaler adoption is workload-segmented rather than universal: capacity-bound workloads (large model weights, KV cache, embedding tables) benefit; bandwidth-bound workloads (training compute, real-time inference of small models) do not.

### CXL stack vs alternatives

| Layer | CXL.mem | NVLink + NVL576 | NVMe-oF (storage analog) | RDMA / GPUDirect (incumbent) |
|---|---|---|---|---|
| Protocol semantics | Hardware cache-coherent load/store | Proprietary cache-coherent + memory pooling | Block-level RDMA | RDMA verbs (kernel bypass) |
| Physical layer | PCIe 5.0/6.0 + photonic for rack-scale | NVLink 5.0/6.0 + Nvidia photonic options | Ethernet / InfiniBand | Ethernet / InfiniBand |
| Standard openness | Open, multi-vendor | Closed (Nvidia-controlled, partner-licensed via NVLink Fusion) | Open | Open |
| Coherence domain | Cross-vendor accelerators | Nvidia-only (or NVLink Fusion partner silicon under Nvidia toll) | None: block-level | None: RDMA-aware applications only |
| Software requirements | CXL.mem driver in CUDA / ROCm / JAX | NVLink-Sharp + Magnum IO (mature) | Filesystem + multipathing | Verbs API + application protocol awareness |
| Latency budget end-to-end | ~200–500 ns | ~150 ns NVLink intra-rack | ~50–200 μs | ~1–5 μs |
| Production maturity April 2026 | CXL 2.0 expansion in production (Azure); CXL 3.x switching late 2026 | NVLink 5.0 in production; NVLink 6.0 + NVL576 H2 2026 | Production for 5+ years | Production for 10+ years |

CXL competes with NVLink at the protocol-semantic layer (cache-coherent memory access) but CXL is open-standard while NVLink is proprietary-with-toll. The strategic split: AMD / Intel / hyperscaler-custom-ASIC compute uses CXL.mem for memory disaggregation; Nvidia compute uses NVLink + NVL576 for the equivalent capability. The two coexist as the open-vs-closed ecosystem split, with the same architectural primitive (rack-scale memory pooling) implemented differently.

## Evidence

### CXL versions and capabilities

| Version | Released | Key capability | Physical layer | Production status April 2026 |
|---|---|---|---|---|
| CXL 1.0/1.1 | 2019 | Cache-coherent device-attached memory; CXL.io + CXL.cache + CXL.mem | PCIe 5.0 (32 GT/s) | Mature |
| CXL 2.0 | 2020 | Memory pooling between hosts; switched topology; SR-IOV | PCIe 5.0 | **In production: Microsoft Azure Nov 2025 first cloud deployment** |
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

The single most important driver is **reasoning / agentic inference**: as frontier model providers move from chat to agentic deployment, KV cache + activation memory per session grows 10–100×. This is the workload that makes memory disaggregation a 2027–2028 architectural primitive rather than a 2030+ adjunct. The second most important is **recommendation / embedding workloads** at hyperscale where today's per-chip replication of TB-scale tables is a known capex inefficiency hyperscalers have publicly acknowledged.

### TAM scenarios (April 2026 update)

| Layer | 2026 size | 2030 base | 2030 bull |
|---|---|---|---|
| Total CXL ecosystem (Yole) | ~$2B | $15B | $25B |
| HBM market (total, SemiAnalysis) | ~$50B | ~$130B | ~$180B |
| Photonic interconnect (switch + fabric) | ~$1.5B | ~$8B | ~$25B |
| Memory-fabric photonics specifically | <$0.5B | $3–5B | $15–25B |
| Marvell Celestial guide | $500M Q4 FY28 / $1B FY29 | $2–4B FY30 (10–15% capture) | $6–12B FY30 (30–40% capture) |
| Astera Labs Aries (CXL retimer + smart cable) | ~$300M of $830M total FY25 | ~$2B | ~$5B |
| Broadcom Atlas (PCIe + CXL switch) | ~$500M–$1B est | ~$2B | ~$3–4B |

Comparable scale references: Nvidia NVLink franchise generates ~$3–4B in fabric-attached revenue today; the SAN switching market peaked at ~$8B annually in the 2010s; memory-fabric photonics could reach 2–3× current NVLink scale by 2030 if memory disaggregation becomes the dominant scale-up architecture.

### 2026 production milestones (timeline for thesis monitoring)

- **March 2026**: Marvell-Nvidia $2B NVLink Fusion deal: implicit acknowledgment that hyperscalers will mix non-Nvidia compute with Nvidia scale-up; CXL.mem adoption follows the same logic
- **April 2026**: Anthropic-Google-Broadcom 3.5GW deal extends through 2031: Google TPU + Broadcom networking + (probable) CXL-attached DRAM memory pools
- **Q2 FY27 (May 2026)**: Marvell Q1 FY27 earnings: first Celestial integration commentary
- **June 2026**: OCP Summit: CXL 3.1 fabric switch silicon deployment evidence; UALink vs NVLink Fusion vs SUE evidence
- **Q3 FY27 (Aug 2026)**: Marvell Q2 FY27 earnings: Celestial Photonic Fabric chiplet tape-out status
- **H2 2026**: Nvidia Vera Rubin / NVL576 production launch: NVLink 6.0 with cross-rack memory addressing; sets the closed-ecosystem benchmark CXL.mem must beat
- **November 2026**: AWS re:Invent: likely Trainium 3 production scale + Trainium 4 design partner signal; both will use CXL or proprietary memory architecture
- **2027**: First production CXL 3.x fabric deployments at hyperscale; Linux CXL Type 2 mainlining (per ABI Research, "no earlier than 2027")
- **2028**: Marvell Photonic Fabric first material revenue ($500M Q4 FY28 guide); inflection on whether memory disaggregation is a 2027–2028 primitive or a 2030+ one

### Vendor landscape (April 2026 — updates [[Research/2026-03-14 - CXL Technology Adoption.md]])

| Vendor | Product | CXL/photonic role | SAN-era analog | Investment exposure |
|---|---|---|---|---|
| **Marvell** | Celestial Photonic Fabric (16/64 Tbps chiplet); XConn switch ($540M acquisition); Inphi DSP | Photonic memory-fabric; switching | **Brocade / Cisco MDS** | [[Theses/MRVL - Marvell Technology]] |
| **Astera Labs** | Aries CXL retimer; Scorpio Smart Fabric Switch; smart cable | CXL retimer + cable assembly + switch | **QLogic / Emulex** (HBAs) | No thesis: evaluate |
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

### Incremental delta — May 2026 update (since 2026-04-26)

One month of newsflow strengthens the core claim: memory disaggregation driven by KV-cache / agentic inference is arriving on the 2027–2028 schedule, not as a 2030+ adjunct. Astera Labs is the first clean public-market proof point, and Marvell's own-brand CXL silicon plus its CXL-attach revenue guide reframe Marvell CXL from pure Celestial optionality toward a near-term attach annuity. No Contradiction Check item flipped.

**Astera Labs Q1 CY2026 (reported May 5): the QLogic/Emulex analog validates the framework**

| Metric | Q1 CY2026 | Read vs note's FY25 base |
|---|---|---|
| Revenue | $308.4M (+93% YoY, +14% QoQ) | run-rate ~$1.3–1.5B vs note's ~$830M FY25, pulled forward ~2 years |
| Non-GAAP gross margin | 76.4% (+150 bp YoY) | structural, not cyclical |
| EPS | $0.61 (large beat) | - |
| Q2 guide | $355–365M vs ~$310M consensus | +15% above Street |

- **New custom CXL design win for a KV-cache application:** direct validation of the framework's stated #1 driver (reasoning / agentic inference KV-cache as the workload that makes disaggregation a 2027–2028 primitive). The note predicted this workload pulls the cycle forward; Astera booked the design win.
- **Leo CXL memory controller** ramping with **Microsoft Azure M-series VMs:** extends the note's "Azure = first cloud CXL deployment" thread from in-chassis expansion toward custom memory-attach silicon.
- Scorpio P-Series to ≥2 additional major hyperscalers by end-2026, broader 2027: the switching-layer ramp the SAN-pattern step #3 predicts.

**Marvell: reports Q1 FY27 on May 27 (the monitoring milestone this note flagged)**
- Guide $2.4B revenue (+27% YoY), EPS $0.79; custom silicon $1.5B in FY26 (doubled YoY).
- **New disclosure: CXL + NIC XPU-attach products alone could exceed $2B revenue by FY2029:** first explicit Marvell CXL-scale datapoint; sits above the note's vendor-landscape framing and reframes CXL from binary-Celestial-only optionality toward a near-term attach annuity.
- First Celestial integration commentary expected on the May 27 call, the note's own "Q2 FY27 (May 2026)" monitoring milestone, landing on schedule.

**Marvell Structera S 30260: own-brand CXL switch the note's vendor table missed** (announced March 17, 2026)
- 260-lane, CXL 3.0, 4 TB/s aggregate, rack-level memory pooling; sampling Q3 2026; CXL 2.0 variant (S 20256) already in production. Marvell engineering frames it explicitly around KV-cache LLM inference: "near-local shared memory pool, sub-microsecond access, eliminates multi-hop data movement."
- Implication: Marvell now occupies the CXL switching layer with branded silicon (Structera) **in addition to** the XConn acquisition and Celestial photonic fabric: three stacked positions at the Brocade / Cisco-MDS layer, not one. Reinforces the "Marvell = SAN-switching-franchise analog" framing.

**Celestial AI roadmap refinement** (vs note's timeline)
- First silicon tape-outs by end-2026; early-access cloud-provider samples early 2027; first semi-custom reference designs pairing Marvell 1.6T optical interconnect with Nvidia Rubin by Q3 2026, consistent with the note's 2027–2028 inflection. Fully-loaded deal value reported up to $5.5B (vs $3.25B headline cash+stock).

**Industry / standards:** CXL 3.1 in broad 2026 deployment on the PCIe 6.x physical layer; >90% of newly shipped servers CXL-capable; ecosystem ~$1.8–2.5B in 2026 (brackets the note's ~$2B). Confirmatory; no thesis change.

### Incremental delta — July 2026 update (since 2026-06-02): AI-inference pull revisited

Five weeks resolved the note's flagged milestone (May 27 Celestial commentary: positive) and delivered the first hyperscale production CXL deployment (Meta), but this pass breaks the streak of clean confirmations. Contradiction #2 (hyperscaler in-sourcing) is now **partially confirmed**, a new NAND-from-below contradiction enters as #9, and the character of the near-term pull has shifted: **the DRAM famine is the 2026 CXL demand driver; the KV-cache fabric thesis is real but confined to a contested middle tier**. Adoption is accelerating while value capture migrates, a different statement than "thesis strengthened."

**1. Marvell Q1 FY27 (May 27): flagged resolution datapoint, resolved mixed-positive**

| Datapoint | Detail | Read |
|---|---|---|
| Celestial validation | Gen-1 Photonic Fabric chiplet "already selected by a tier 1 hyperscaler for its next-generation XPU scale-up networks"; scale-up optics outlook >2× prior ~$150M, ramping FY28 | First commercial validation of the $3.25B deal: the Brocade-analog leg is on schedule |
| CXL guide | Dec-2025 ">$2B CXL+NIC by FY29" NOT restated; replaced by ">$1B" XPU-attach with transcripts disagreeing on timeframe ("next few quarters" run-rate vs "next couple of years") | Ambiguity where precision existed: mild negative |
| XConn | Guided to only ~$100M revenue by FY28 (deal closed Feb 10, $540M) | Market cleared the flagship merchant CXL switch asset at option value, not wave value |
| Structera | Zero disclosed customers/production anywhere as of Jul 10; S 30260 sampling starts CQ3 2026; DDR4-reclaim cards + 2:1 inline LZ4 compression are the famine products | Evidence base is still supplier announcements |
| Demand attribution | Management: DRAM shortage "driving additional adoption of CXL-based design" + "increasing inference and KV caching requirements" | Marvell itself leads with the famine, not the fabric |
| Sell-side | UBS Jun 30 (PT $230→$340): MRVL CXL ~$1B CY27 / ~$2B CY28 via XPU-attach at two US hyperscalers; CXL TAM $4.5B 2027 → $7–10B 2030 | First street underwriting of CXL as a Marvell P&L line, and the clearest falsifiable model |
| Valuation | ~70× fwd P/E, consensus mean PT ~$249 below price, +~200% YTD, S&P 500 add Jun 22; no investor day held despite the 2026 promise; CFO change Jun 15 (Durn in) | The stock re-rated ahead of the disclosed evidence |

**2. Meta Vistara (Jun 29, ISCA 2026): first hyperscale production CXL, and it's in-house**
- Custom CXL 2.0 Type-3 ASIC recycling decommissioned DDR4 into DDR5-only servers (2×72-bit DDR4-3200 channels, 256 GB/chip, PCIe Gen5 x16; ~1 TB/server MemServer with EPYC Turin). **In production at hyperscale.**
- Quantified TCO: up to **25% fewer servers for disaggregated ML inference, 29% lower average latency for distributed caches, 33% fewer out-of-memory failures**, despite the CXL tier running ~10× lower bandwidth / +60% latency vs local DRAM.
- Read: the strongest architectural validation of pooling economics yet disclosed AND the strongest merchant-silicon bear datapoint in one event. Meta bypassed every merchant CXL controller vendor. Contradiction #2 fired at the controller layer; the SAN-era precedent (Google B4 building transport but buying components) says the photonic/component layer stays merchant: that boundary is now the live question.

**3. The KV-cache socket is being tiered: CXL holds the middle, contested**

| Tier | Winning architecture (Jul 2026) | Evidence | CXL relevance |
|---|---|---|---|
| Hot (active decode) | GPU HBM + NVLink/NVLink-C2C + SOCAMM LPDDR on Grace/Vera | SK Hynix 192 GB SOCAMM in MP since Apr 2026; P/D-disaggregation KV transfer runs NVLink/RDMA/NIXL | Excluded |
| Warm (KV reuse, multi-turn/agentic) | x86 CPU-attached CXL DRAM pools behind vLLM/LMCache | Samsung Jun 2026 white paper: ~92% of DRAM performance, 1 TB CMM-D pool behind CXL switch; PENG production 11 TB KV-cache server (Mar); ALAB custom-Leo hyperscaler win (ships 2027) | **The beachhead: real, revenue-bearing, single-design-win scale** |
| Cold (context at rest) | Ethernet-attached NAND | Nvidia CMX/BlueField-4 (~150 TB/DPU, H2 2026, partner list is a storage roll call, zero CXL); HBF samples H2 2026 | Squeezed from below |

- Rubin CPX **cancelled** at GTC (Mar 2026): Nvidia's long-context answer is Groq LPX SRAM (~$20B non-exclusive license), neither GDDR7 nor CXL. The April framework's "CXL.mem or Photonic Fabric required" mapping for agentic KV-cache was too binary: the workload's memory pull is real (Google: 3.2 quadrillion tokens/month, +7× YoY; memory ≈30% of hyperscaler DC spend, ~4× the 2023 share) but it is being **routed across HBM/LPDDR/NAND tiers**, with CXL capturing only the CPU-side reuse tier.
- Software tell: CXL is absent from Dynamo/KVBM and LMCache first-class tier lists (experimental only via Samsung); MLPerf Inference v6.0 (Apr 2026) had zero CXL submissions. Azure remains the **only** public-cloud CXL deployment; AWS/Google/Oracle silent.

**4. The actual near-term pull is the DRAM famine, not the fabric**
- Contract DRAM +~95% QoQ in Q1 2026, +58–63% guided Q2, still +13–18% (server) in Q3; DDR5 RDIMM $27–37/GB (+300–400% since mid-2025); ~70% order fill rates, >30-week lead times; OpenAI/Stargate locks up to 900k wafers/month (~40% of global DRAM output) through 2029.
- Every 2026 production CXL use case is **stranded/legacy-DRAM cost arbitrage**: Meta's DDR4 reclamation, Structera DDR4 cards, inline compression halving $/GB. This is a famine product finding immediate ROI: a different and earlier adoption driver than the April framework's disaggregation primitive, and it front-loads CXL attach into 2026–2027 rather than waiting for CXL 3.x fabrics.
- Cross-current the pooling bulls skip: CXL expanders compete for the same scarce DDR5 dice at 30–60% cost premiums; suppliers prioritize HBM/RDIMM lines over CMM output (Samsung slipped CMM-D 3.0 sampling to protect 2.0 output: "CXL 3.1 ecosystem yet to mature").

**5. Ecosystem scorecard (Jun 1 – Jul 10)**

| Vendor | Delta | Signal |
|---|---|---|
| Astera Labs | Azure M-series private beta → GA by YE26; Nasdaq-100 add; +41% in June; Q2 print Aug 4 | Pipeline intact; valuation ran ahead |
| Penguin Solutions | FQ3 (Jul 7): Integrated Memory +111% YoY; CXL cards revenue + bookings; tier-1 financial KV-cache repeat order | **Only in-window CXL revenue datapoint** |
| Samsung | CMM-D 3.1 samples Q3, MP target Q4 2026; 3.0 sample slippage; 92%-of-DRAM KV-offload white paper | Qualification-stage; 2.0 sampled to 40+ incl. all top hyperscalers |
| SK Hynix | 256 GB CXL 3.2 module shown at HPE Discover (Jun 19); "HBM alone cannot solve AI's memory problem" | Module roadmap ahead of demand disclosure |
| Micron | CZ122 in production, Red Hat-certified; zero CXL revenue disclosure at record FQ3 | CXL immaterial vs HBM for all three DRAM makers |
| Microchip / Broadcom | <12 ns PCIe 6.0/CXL 3.1 retimers (Jun 2); Atlas 4 + retimer-switch bundling | Aries niche crowding: retimer commoditization vector |
| Montage / Panmnesia / UnifabriX / MemVerge | Still testing-stage / sub-scale; no 2026 funding rounds found | Long tail not converting |

**6. Investment opportunity map, July 2026 (ranked by evidence-adjusted attractiveness)**

| # | Vehicle | Case | Verdict | Falsifier / checkpoint |
|---|---|---|---|---|
| 1 | **MRVL** (held, HIGH) | Only three-layer CXL+photonic stack (Structera + XConn + Celestial); tier-1 Celestial win; UBS $1B/CY27 → $2B/CY28 | Thesis already carries the lever; **no add** at ~70× fwd with zero Structera customer disclosure | CQ3 Structera sampling → named wins; Celestial tape-out by end-2026 |
| 2 | **PENG** (no thesis) | Only P&L-visible inference-CXL revenue; +111% segment growth at an integrator multiple | **Evaluate via `/thesis`**: demand-tell / convex candidate, not a compounder (layer-renter on ALAB silicon) | FQ4 (Oct) CXL mix; loss of the ALAB Leo supply relationship |
| 3 | **000660 + SNDK** (held) | Fabric-agnostic winners: HBM/SOCAMM/HBF capture the inference memory pull under every fabric outcome; HBF is a new direct SNDK lever | Reinforces existing theses; the highest-confidence expression of the memory-wall insight | HBF 18.8× sim vs real benchmarks (AIN samples H2 2026) |
| 4 | **ALAB** (no thesis) | Validated (Azure GA, KV-cache win) but $71.6B / ~70× EV/S / crowding retimer moat / insider sale; QLogic-analog endgame is commoditization | **Watch, don't buy**: entry only on material derating | Aug 4 Q2: Leo/Scorpio mix + any second cloud CXL win |
| 5 | **NVDA** (held) | Owns hot + cold KV tiers end-to-end; containment succeeding | Confirms thesis; no CXL-specific action | A top-5 hyperscaler deploying CXL KV-pooling at fleet scale would dent fabric-economics control |
| - | Montage, private long tail | Testing-stage / sub-scale | Not actionable | - |

**7. Framework re-test (mental-models pass: hypotheses, not verdicts)**
- *Semis #1 (emerging bottleneck → pricing power)*: fired for the **DRAM complex**, not for merchant CXL silicon: the famine pulls CXL attach but the pricing power accrues to memory makers (DRAM +95% QoQ vs CXL silicon still pre-revenue at most vendors).
- *Semis #8 (architecture transition remaps the bottleneck)*: NAND-tier capture (CMX + HBF) is a live remap the April framework missed. The viability table assumed NAND stays at μs latencies; HBM-stacked NAND at >1.6 TB/s breaks that assumption. Added as Contradiction #9.
- *Value-Layer-Monopoly*: **no merchant vendor owns the CXL layer as of July 2026**. The standard is open by design, the controller/retimer layer has four credible vendors and is crowding, and Meta demonstrated in-house bypass. The surviving layer-monopoly candidates are the photonic substrate (Celestial, unproven until tape-out) and the DRAM oligopoly above the fabric. ALAB fails the emerging-monopoly test at its current price; PENG never takes it.
- *Disconfirm-on-agreement trigger*: three consecutive prior updates read "strengthened, no contradiction flipped". This pass deliberately hunted the bear case and found two contradiction upgrades (#1, #2) plus one new contradiction (#9). Net honest read: **CXL adoption is accelerating and pulled forward by the DRAM famine, but the marquee AI-inference socket is being captured by NVLink + NAND tiering, and merchant value capture is narrower than the SAN analogy's midpoint implied.**

**Vault-internal tension (cross-reference):** [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]] recommends **EXIT MRVL** on the Trainium 3 socket loss to Alchip (custom-silicon execution credibility gap). The framework's central upside vehicle is under portfolio-construction pressure for reasons unrelated to memory disaggregation, yet the disaggregation lever itself (this note's subject) is independently strengthening via Astera's KV-cache win and Marvell's own Structera + CXL-attach guidance. The binary Celestial upside is intact; the vehicle carrying it is contested. Resolution datapoint: the May 27 Celestial commentary.

### Incremental delta — August 2026 (Damnang Part 3)

Damnang (21 Aug) treats CXL pooling and Photonic Fabric as the high-optionality / low-P&L bucket (Memory scored 3.0 proven / 2.0 in FY27–28 earnings / 5.0 upside [est.]) and **separates CMM-Ax from PF**: CMM-Ax is Structera A PNM + SK hynix memory + SK hynix software, validation-stage at FMS 2026, no disclosed production customer [1×: Damnang]. Three pairwise collaborations (NVIDIA–Marvell, NVIDIA–SK hynix, Marvell–SK hynix) are confirmed; a three-party integrated program is not. No evidence SK hynix or NVIDIA adopted Photonic Fabric. KV-cache growth with context length and agentic steps remains the demand driver for capacity *outside local HBM* — consistent with this framework and with the July KV-cache-socket-capture caution. Confirmation for a PF–DRAM inference is still first disclosed PF customer and memory partner.

## Contradiction Check

What could break the SAN-for-DRAM analogy and the memory-disaggregation thesis?

1. **NVLink Fusion captures the open-fabric layer:** if Nvidia's NVLink Fusion + Vera Rubin memory addressing satisfies the disaggregation use cases (inference, agentic, recommendation embeddings) within the Nvidia ecosystem, the CXL.mem TAM compresses to AMD / Intel / custom-ASIC compute (~30–40% of accelerator deployments by 2028). Probability: medium. Marvell Celestial bet still works in this scenario but TAM is ~half of bull case. The strongest contradiction.

2. **Hyperscalers in-source disaggregation:** Google's Apollo OCS already serves a similar inter-pod memory-domain function for TPU. AWS Nitro Memory Fabric (rumored) could bypass merchant CXL switch silicon entirely. Probability: medium. Eliminates merchant CXL switch silicon revenue but does NOT eliminate the underlying memory-fabric photonic primitive: hyperscalers still buy photonic interconnect silicon from Marvell or competitors. SAN-era analog: Google built its own inter-data-center optical transport (B4) but still bought Lumentum / Coherent components.

3. **HBM-on-package scaling outpaces disaggregation need:** if HBM4 (2026–2027, 16-Hi stacks at 32–48 GB per stack, 8–12 stacks per package = 256–576 GB per chip) and HBM5 (2028+, ~1 TB per chip) keep memory in-package faster than workload memory needs grow, disaggregation becomes optional rather than necessary. Probability: low. Workload memory needs (trillion-param MoE, multi-million-token agentic) are growing 10–100× per generation, faster than HBM stacking density (~2× per generation).

4. **Photonic latency does not close:** if photonic transceiver + SerDes overhead does not compress to <500 ns total fabric latency, the ratio threshold breaks and CXL.mem disaggregation stays niche. Probability: low. Marvell Celestial OCI architecture targets <100 ns chiplet-to-chiplet, well within budget. Lightmatter and Ayar Labs target similar latencies.

5. **Cost-utilization tradeoff doesn't close:** photonic interconnect at ~$50/Gbps vs electrical ~$10/Gbps requires ≥5× utilization gain to amortize. If real-world utilization gains are smaller (2–3×), the economics don't work outside narrow workload niches. Probability: medium for early years (2026–2028), low for later years (2029+) as photonic component costs compress with volume. SAN analog: Fibre Channel was 5–10× more expensive than SCSI in 1998 but volume drove ~80% cost compression by 2005.

6. **Software ecosystem stalls:** ABI Research expects CXL 3.0/3.1 software ecosystem mature "no earlier than 2027." If CUDA / ROCm / JAX driver support slips beyond 2028, the architectural primitive validates but commercial adoption lags 2–3 years. Probability: medium. This is the most likely real-world friction. SAN analog: the file-system + multipathing + LVM stack took ~5 years (1998–2003) to mature; CXL software stack is on a similar trajectory.

7. **The SAN analogy doesn't actually hold:** counter-argument: NAND access semantics (block-level batched I/O) are fundamentally different from DRAM (load/store byte-level), so the historical pattern may not transfer cleanly. Specifically, applications historically rewrote to batch SAN I/O to hide latency; CPUs cannot batch CXL.mem load/store the same way (latency is per-instruction). Probability: this is a misframing. The analogy holds at the **architectural pattern** level (pool + fabric + sharing + utilization gain + standards consolidation + vendor-economics distribution), not at the semantic level. The semantics are different, but the disaggregation cycle pattern is the same. Counter-argument: hardware prefetching + speculative execution + cache hierarchy hides much of the per-instruction latency, similar to how OS buffering hides per-block SAN latency.

8. **Power consumption breaks the economics:** photonic interconnect at scale could add material rack-power overhead that hyperscalers find prohibitive. Probability: low. Photonic actually saves power at high bandwidth (~3× reduction at >100 Tbps per Bailly / TH6-Davisson data), and CXL pooling enables stranded-memory utilization that reduces total rack count.

The strongest contradiction is #1 (NVLink Fusion captures Nvidia compute). But even in that scenario, the open-CXL ecosystem (~30–40% of accelerator deployments by 2028) is large enough to support a multi-billion-dollar Marvell Photonic Fabric franchise. The SAN analogy is robust to most contradictions because the underlying physics + economics drivers (memory wall, stranded-resource economics, fabric latency in viable ratio) are independent of vendor-strategy outcomes.

### July 2026 re-test (dated addendum — items above preserved as written April 2026)

- **#1 NVLink Fusion captures the open-fabric layer: probability medium → medium-high.** Fusion added Marvell (the "first NVLink Fusion partner," $2B Nvidia investment restated at Computex Jun 2), Lightmatter (Jun 3), SiFive, Samsung Foundry, and ALAB itself now builds Fusion silicon. Enfabrica (~$900M, the one shipping Ethernet+CXL memory fabric) absorbed into Nvidia's CMX roadmap. Scale-up value is consolidating inside the proprietary domain faster than the April read.
- **#2 Hyperscalers in-source disaggregation: PARTIALLY CONFIRMED at the controller layer.** Meta Vistara (Jun 29): in-house CXL 2.0 ASIC in production at hyperscale, bypassing every merchant controller vendor. The April framing survives at the component layer (SAN-era B4/Lumentum analog: hyperscalers build systems, buy silicon), but the boundary between "system" and "silicon" just moved down one layer. Merchant TAM haircut, not thesis kill.
- **#6 Software ecosystem stalls: mixed, leaning negative.** CXL still absent from Dynamo/KVBM and LMCache first-class tiers and from MLPerf v6.0; offset by Samsung's 92%-of-DRAM white paper showing the gap is closable per-vendor with custom kernels. The "no earlier than 2027" ABI call is tracking on schedule.
- **#9 (NEW) NAND captures the capacity tier from below.** Nvidia CMX standardizes KV-cache offload on Ethernet-attached NAND (H2 2026, ~150 TB/DPU); HBF (SK Hynix + SanDisk, OCP standardization Feb 2026, >1.6 TB/s stacked, 18.8× concurrent-query simulation) arrives 2027 targeting exactly the long-context KV/weights tier CXL DRAM wants; the DRAM famine pushes hyperscalers toward cheaper NAND tiers rather than pooled DRAM. Probability: medium. This attacks the viability-table assumption that NAND stays at μs latencies: the fabric-overhead ratio framework itself needs a NAND-tier row refresh once HBF samples benchmark. Falsifier for #9: HBF failing real-workload benchmarks vs its simulation. Falsifier for CXL: no top-5 hyperscaler deploying CXL KV-cache pooling at fleet scale by end-2027 (none public as of July 2026; Azure expansion is the only cloud deployment).
- Items #3, #4, #5, #7, #8: no new evidence either way; probabilities unchanged.

## Source Excerpts

This note synthesizes prior vault research and conversational framework: no external excerpts.

Cross-references:
- [[Research/2026-03-14 - CXL Technology Adoption.md]]: primary CXL deep-dive (March 2026): standards consolidation, Microsoft Azure Nov 2025 production, Yole $15B 2028 TAM, latency penalty (25% workloads >20% degradation), Astera Labs / Marvell / Broadcom Atlas / Microchip / Synopsys / Cadence / Samsung / SK Hynix / Micron landscape. This note layers the SAN-for-DRAM mental model + April 2026 Marvell Celestial connection on top.
- [[Sectors/Custom Silicon & Networking Semiconductors]]: §Macro shifts → Architectural transition, memory disaggregation / Photonic Fabric; §Investor heuristics → "Non-consensus insight — Photonic Fabric is the asymmetric MRVL upside"
- [[Theses/MRVL - Marvell Technology]]: §Industry Context → Memory disaggregation deep-dive (use-case table + TAM table + upside-constraints list); Bull Case driver #3 (Celestial ramps); Bear Case driver #3 (Celestial integration slips); Non-consensus Insight #2 (Celestial as memory-disaggregation architecture, not CPO re-skin)
- [[Theses/AVGO - Broadcom]]: Atlas franchise (PCIe + CXL switch silicon); Tomahawk / Jericho remain primary AI bet; CXL is bull-case adjacency not core driver
- [[Theses/NVDA - Nvidia]]: NVLink Fusion + NVL576 closed-ecosystem alternative; $2B Marvell containment move
- [[Theses/000660 - SK Hynix]]: HBM consumer beneficiary of CXL pooling expanding memory consumption per dollar of compute capex (Jevons effect)
- [[Theses/PSTG - Pure Storage]]: SAN-era incumbent; not directly affected by CXL but framework-relevant for understanding the pattern
- [[Research/2026-05-31 - CPO Scale-Up Inflection and Supply Chain - deep-dive]]: SemiAnalysis CPO "book": corroborates Celestial Photonic Fabric as the memory-disaggregation vehicle (EAM modulator + optical interposer; $1B CY2028 run-rate into AWS Trainium 4; Amazon warrant strike $87.0029 = Trainium 4 tell; center-of-die optical-I/O memory appliance); scale-up CPO TAM > scale-out
- [[Research/2026-06-02 - Datacenter CPU Landscape 2026 - deep-dive]]: SemiAnalysis "CPUs are Back": server-CPU-side memory-disaggregation evidence, CXL3 on Intel Diamond Rapids, JBOM ("Just a Bunch of HBM") + Credo Omniconnect gearboxes, Bluefield-4 KV-cache-to-NAND "third network"; datacenter LPDDR shift + possible HBM-on-CPU return. Confirmatory; no Contradiction Check item flipped.

**May 2026 delta, external sources:**
- Astera Labs Q1 CY2026 earnings, reported 2026-05-05: [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/05/05/astera-labs-alab-q1-2026-earnings-transcript/), [Futurum](https://futurumgroup.com/insights/astera-labs-q1-fy-2026-earnings-highlight-scale-up-switching-ramp/), [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-q1-2026-earnings-beat-expectations-93CH-4661270)
- Marvell Q1 FY27 preview, custom-silicon + CXL/NIC attach guidance: [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/261924282-marvell-mrvl-earnings-ai-optical-datacenter-trainium-analyst-upgrades-valuation-tradingkey), [Yahoo/Zacks](https://uk.finance.yahoo.com/news/mrvl-post-q1-earnings-time-144300668.html)
- Marvell Structera S 30260 CXL switch, announced 2026-03-17: [Marvell newsroom](https://www.marvell.com/company/newsroom/marvell-next-gen-cxl-switch-memory-pooling-breaks-ai-memory-wall.html)
- Celestial AI acquisition + Photonic Fabric roadmap: [Optica OPN](https://www.optica-opn.org/home/industry/2025/december/marvell_looks_to_acquire_celestial_ai/), [Tom's Hardware](https://www.tomshardware.com/tech-industry/marvells-celestial-ai-acquisition-expands-its-role-in-ai-data-center-hardware)

**July 2026 delta, external sources:**
- Marvell Q1 FY27 call (2026-05-27): [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/05/27/marvell-mrvl-q1-2027-earnings-transcript/), [8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001835632/000183563226000014/q127_8kx522026ex-991.htm); UBS CXL PT raise (2026-06-30): [Yahoo](https://finance.yahoo.com/markets/stocks/articles/marvells-cxl-outlook-brightens-120824153.html), [TIKR](https://www.tikr.com/blog/marvell-stock-rose-7-after-ubs-backed-a-340-target-on-cxl-heres-where-the-stock-could-go); Computex keynote: [Marvell newsroom](https://www.marvell.com/company/newsroom/marvell-keynote-computex-2026-future-of-scaling-ai-depends-on-connectivity.html)
- Meta Vistara CXL ASIC (ISCA, 2026-06-29): [The Register](https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483), [Tom's Hardware](https://www.tomshardware.com/pc-components/dram/meta-fights-soaring-hardware-costs-by-reusing-old-ddr4-server-memory-in-new-ddr5-only-servers-custom-cxl-2-0-chip-marries-legacy-ddr4-2400-with-cutting-edge-ddr5-6400)
- Penguin Solutions FQ3 (2026-07-07): [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-penguin-solutions-tops-q3-2026-estimates-raises-outlook-93CH-4780386); production CXL KV-cache server (2026-03-16): [HPCwire](https://www.hpcwire.com/off-the-wire/penguin-solutions-introduces-industrys-first-production-ready-cxl-based-kv-cache-server/)
- Nvidia CMX/BlueField-4 KV-cache-on-NAND: [Nvidia newsroom](https://nvidianews.nvidia.com/news/nvidia-bluefield-4-powers-new-class-of-ai-native-storage-infrastructure-for-the-next-frontier-of-ai), [Blocks & Files](https://blocksandfiles.com/2026/01/06/nvidia-standardizes-gpu-cluster-kv-cache-offload-to-nvme-ssds/); Rubin CPX cancellation: [Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/nvidia-removes-rubin-cpx-accelerators-from-its-roadmap-groq-3-lpus-take-center-stage-as-cpx-is-removed)
- HBF standardization (SK Hynix + SanDisk, 2026-02-25): [SanDisk PR](https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf), [Blocks & Files HBM+HBF hybrid](https://www.blocksandfiles.com/flash/2026/02/16/sk-hynix-proposes-hbm-and-hbf-hybrid-for-llm-inference/4091326)
- Samsung CMM-D KV-cache white paper (June 2026): [PDF](https://download.semiconductor.samsung.com/resources/white-paper/Optimizing_KV_Cache_Offloading_to_CMM-D_in_a_CXL_Switch-based_Memory_Pool.pdf); CMM-D 3.1 roadmap: [Korea Herald](https://www.koreaherald.com/article/10737182); sample slippage: [The Elec](https://www.thelec.net/news/articleView.html?idxno=11999)
- ALAB June/July: [Motley Fool](https://www.fool.com/investing/2026/07/08/why-astera-labs-stock-skyrocketed-last-month/), [stockanalysis.com](https://stockanalysis.com/stocks/alab/statistics/); retimer crowding: [ServeTheHome](https://www.servethehome.com/broadcom-fires-a-shot-at-astera-labs-and-more-with-new-pcie-and-cxl-retimers/)
- DRAM famine: [TrendForce 3Q26](https://www.trendforce.com/presscenter/news/20260703-13134.html), [Micron FQ3 prepared remarks](https://investors.micron.com/static-files/e089f8c0-065d-47b8-9d02-bfa863cdb357); Google token volume: [Google I/O 2026](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)

## Log

- 2026-05-26 — Addressed user callout (latest/delta request): added §Evidence → "Incremental delta — May 2026 update". Astera Q1 KV-cache CXL design win + Leo/Azure ramp; Marvell CXL+NIC attach >$2B FY29 guide + first Celestial commentary due May 27; Structera S 30260 switch; Celestial roadmap refinement. Core thesis strengthened, no Contradiction Check item flipped; flagged MRVL EXIT recommendation from [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]].
- 2026-05-31 (/sync) — [[Research/2026-05-31 - CPO Scale-Up Inflection and Supply Chain - deep-dive]]: SemiAnalysis CPO deep-dive corroborates the Celestial Photonic Fabric vehicle — first *quantified* scale-up ramp ($1B CY2028 into AWS Trainium 4; Amazon warrant strike $87.0029 = Trainium 4 tell), EAM-modulator + optical-interposer physical layer, center-of-die optical-I/O memory appliance. No Contradiction Check item flipped; reinforces the 2027-2028 inflection timing. Added to cross-references.
- 2026-06-02 (/sync) — [[Research/2026-06-02 - Datacenter CPU Landscape 2026 - deep-dive]]: SemiAnalysis "CPUs are Back" supplies direct server-CPU-side memory-disaggregation evidence — CXL3 on Intel Diamond Rapids (mainstream x86 CXL adoption), JBOM ("Just a Bunch of HBM") + Credo Omniconnect gearboxes as new disaggregation primitives, NVIDIA Bluefield-4 Context Memory Storage Platform (KV-cache offload to high-speed NAND = a "third network") extending the pattern to the NAND tier. Datacenter LPDDR shift (Grace/Vera/Venom) + possible HBM-on-CPU return are adjacent vectors. Confirmatory; no Contradiction Check item flipped. Added to cross-references.
- 2026-07-10 — Revisit (user request, AI-inference pull): added §Evidence → July 2026 delta + Contradiction re-test + opportunity map. Celestial tier-1 win + UBS $2B/CY28 CXL underwriting vs Meta Vistara in-housing + NVLink/NAND capturing the marquee KV socket — Contradiction #2 partially confirmed, new #9 (NAND-from-below) added, storage-unaffected claim revised (HBF); opportunities ranked MRVL (held, no add) / PENG (evaluate) / 000660+SNDK (reinforced) / ALAB (validated-but-priced, watch).
### 2026-08-20
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged
### 2026-08-21
- [[Research/2026-08-20 - 000660 NVDA MRVL - Damnang HBM Density Peak - deep-dive]]: Rubin Ultra 8-Hi + NVL576 makes data movement the bind; CMM-Ax / Celestial 32TB/50m are the electrical-then-optical disagg path. Vendor targets, not a PO.
- [[Research/2026-08-20 - 000660 NVDA MRVL - PhotonCap SKHY CPO Track - deep-dive]]: Avicena LightBundle / micro-LED on all three memory-maker cap tables; optical memory-link protocol still the priceable moment.
### 2026-08-22
- [[Research/2026-08-21 - MRVL NVDA 000660 - Damnang Marvell Part 3 - deep-dive]]: CXL pooling / Photonic Fabric still little P&L; CMM-Ax is Structera A CXL-PNM (validation, no production customer); no PF adoption at NVIDIA/SK hynix; KV-cache growth remains the demand story for capacity outside local HBM.
