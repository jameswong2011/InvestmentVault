---
publish: false
date: 2026-08-27
tags: [research, AI-infra, NVDA, AVGO, MRVL, 000660, SNDK, SPCX, LITE, COHR, VICR, FORM, 6857, CPO]
sector: Semiconductors
ticker: NVDA
source: 'https://photoncap.net/p/ai-infrastructure-value-chain-the'
source_type: deep-dive
---

# AI Infrastructure Value Chain: The PhotonCap Reading List (8/27/2026)

## Thesis Delta

Consensus still prices NVIDIA guidance as a GPU-demand / Data Center silicon print: the tape treats [[Theses/NVDA - Nvidia]] as hardware sales plus hyperscaler capex, and treats [[Theses/AVGO - Broadcom]] and [[Theses/MRVL - Marvell Technology]] as the ASIC-and-Ethernet overlay on that same compute bill. This 27 August 2026 PhotonCap subscriber reading list inverts the signal. NVIDIA guidance is read as evidence that bottlenecks are spreading across memory, packaging, networking, optics, power, cooling, grid capacity, and datacenter construction, not as proof of stronger GPU units alone. NVIDIA revenue growth itself does not prove silicon-photonics adoption; the load-bearing claim is that larger clusters, higher bandwidth, and denser racks push electrical interconnects toward a physical limit, which raises the pressure toward optical I/O, CPO, and scale-across architectures. Flag only (do not fire HIGH/LOW/CLOSE): NVDA has no registered Conviction Triggers; AVGO has none. The map does not print MRVL HIGH (signed Google MPU/inference contract + Trainium 3 ≥400K packaged units + Celestial PO or on-schedule end-2026 tape-out), LOW, or CLOSE; does not print 000660 HIGH (Rubin share ≥60% + HBM4E sole-source + Kinex 16-Hi + Namics renewal), LOW (Samsung >35% of first two Rubin shipping quarters), or CLOSE; does not print SPCX HIGH/LOW/CLOSE (YE26 nameplate, CSA duration, Connectivity margin); does not print 6857 HIGH/LOW/CLOSE (HBM4 production test-time >14 hours, Teradyne HBM5 qualification). Touches NVDA Outstanding Q on ASIC share and Spectrum-X CPO shipping H2 2026 as adjacency, not a tok/s or MLPerf print. Touches AVGO Insight #1 (Tomahawk sits in the data path regardless of compute vendor) and Insight #4 (Ethernet vs InfiniBand already tipped). Touches MRVL Insight #2 (Celestial is memory-disaggregation, not a CPO re-skin) and Insight #4 (1.6T LPO/DSP as the owned optical layer). Touches 000660 Insight #3 (do not merge the CPO track into HBF). Touches SNDK HBF Insight (layer 19) with no Conviction Triggers to test. Touches SPCX Insight that 10GW of orbital compute is an alternative to powered land, not a YE26 nameplate print. Touches 6857 test-time Insight only as layer-5 adjacency. MU is named on layers 2 and 19 and is a thesis name, not a live-book holding. Live-book names on this map: NVDA Medium, AVGO Medium, MRVL Medium, 000660.KS High, SNDK Low, SPCX High, 6857.T Low. [[Theses/LITE - Lumentum]], [[Theses/COHR - Coherent]], [[Theses/VICR - Vicor Corporation]], and [[Theses/FORM - FormFactor]] have theses and sit on named layers; they are not in the live book.

## Summary

PhotonCap opened on NVIDIA's latest guide and refused the obvious reading. The guide is treated as a system-level tell, not a GPU-unit tell. If cluster size, required bandwidth, and rack power density keep rising, copper reach, thermal envelope, and site power stop being second-order constraints and become the binding ones. That is why the author says NVIDIA revenue growth does not prove silicon photonics adoption: a rising GPU bill can still be an electrical-interconnect build. The stronger mechanism is physical. Electrical I/O hits a wall; the pressure then moves to optical I/O, co-packaged optics, and eventually scale-across (campus-to-campus coherent), which is a different layer from switch-face CPO. The one-line conclusion is that AI is no longer just a semiconductor buildout. It is a memory, networking, optics, power, and physical-infrastructure buildout.

The rest of the piece is a map, not a new primary investigation. PhotonCap splits AI infrastructure into nineteen layers and, where the archive allows, hangs up to three already-published articles on each: one entry point, one structural piece, one current read. Selection is coverage, not chronology. All links resolve to published PhotonCap notes. Many of those notes are already in the vault (memory-wall routes, rack-split optics paypoints, SKHY CPO track, Samsung/SK optical ranking, HBF vs optics, Lumentum's first $1B quarter, Coherent FQ4 InP/CPO, FormFactor 29 July, SpaceX first earnings / 10GW hardware chain, UMC/Tower 300mm SiPh, Corning fiber, Ciena/Nokia/Cisco scale-across correction). This note does not re-summarize them. The new object is the frame: which layers the archive actually covers, which ones it only glances at, and what that coverage pattern implies for how a book should be read against a spreading-bottleneck cycle.

Coverage is uneven in a way the author flags rather than papers over. Layers 1 through 11 (compute silicon through networking systems / DCI) each carry a full three-article set. Layer 12 (high-density power conversion, Vicor / MPS) is thin: two articles, not three. Layers 13, 14, and 15 (datacenter power infrastructure, cooling, grid) have no dedicated article; nearest coverage is borrowed from the optical-axis thermal/800V HVDC piece, the GPU-repricing / hyperscaler-capex piece, and the nuclear-cycle map. Layer 16 (power generation) has two articles. Layer 17 (datacenter construction: Quanta Services, EMCOR, Comfort Systems) is a clean coverage gap: no PhotonCap article sits on it. Layers 18 and 19 (powered land / orbital compute, and storage / memory disaggregation) return to a full three-article set. Across the whole chain the author points at the $580B cloud-capex hardware map, the equipment "drilling rigs" piece, and a portfolio quarterly review (1Y +124%, four months behind by 10.4pp). Three cycles sit outside the map on purpose: LEO / satellite optical links, quantum (they all buy the same light), and defense / humanoid.

The investment implication is taxonomic, not a print. A book concentrated in compute, HBM, custom silicon, and optics is long the layers PhotonCap has researched; it is short the layers the archive has not yet written (site power, cooling, grid, construction). That is a research-coverage statement, not a recommendation to rotate. The same map also stops a common category error: there is no such thing as a single "CPO stock," scale-across is coherent rather than CPO, and HBF / optical memory pooling live on layer 19, not inside the HBM line. Those distinctions already sit in the vault's MRVL, 000660, and SNDK theses. The reading list does not add a new number that would fire a registered trigger. It does change how NVIDIA guidance should be read the next time the tape treats it as GPU demand alone.

## Framework / Mental Model

**Name:** Nineteen-layer AI infrastructure value chain, scored by PhotonCap archive coverage versus gap.

Re-applicable whenever a guide, capex print, or "CPO / power / memory" headline is being scored: ask which layer the bottleneck actually moved to, whether PhotonCap (or the vault) has a dedicated note on that layer, and whether the named ticker is doing that layer's job or an adjacent one. NVIDIA guidance is the entry test. If the guide is read as GPU units, the book stays on layer 1. If the guide is read as spreading constraints, layers 2 through 19 come into the same cycle.

| # | Layer | Named names | Dedicated PhotonCap coverage | Job of the layer |
|---|---|---|---|---|
| 1 | Compute silicon | NVDA, AMD, AVGO, MRVL | Yes (3). Vault already has rack-split and copper-wall notes | Accelerators and custom silicon that set cluster size and the optics bill |
| 2 | HBM / DRAM | SK Hynix (000660), MU, Samsung | Yes (3). Memory-wall routes, SOCAMM misread, optical ranking already ingested | Capacity and bandwidth wall at the package |
| 3 | Advanced packaging | TSMC, Amkor, ASE | Yes (3) | Assembly-side bottleneck for HBM4 and CPO (bonding, glass, hybrid bond) |
| 4 | Semiconductor equipment | ASML, AMAT, LRCX, KLAC, TEL | Yes (3) | Tools behind silicon and optics; pick-and-shovel, not the end GPU |
| 5 | Test / probe | FORM | Yes (3). FORM 29 July already ingested | Test-time as the CPO / HBM volume constraint |
| 6 | AI networking | NVDA, AVGO, MRVL, Arista | Yes (3) | Fabric that scales the cluster. CPO does not map to one ticker |
| 7 | Optical transceivers / engines | COHR, LITE, AAOI, Innolight | Yes (3). LITE $1B quarter and Innolight/FCC notes ingested | Pluggable and engine form factors (DSP / LPO / NPO / CPO) |
| 8 | InP / lasers | LITE, COHR, AXTI, Sumitomo | Yes (3). COHR FQ4 InP already ingested | Light source. SiPh foundries raise InP demand; substrate scarcity is contractual |
| 9 | Silicon photonics / CPO | MRVL, AVGO, Intel, TSMC, TSEM, GFS | Yes (3). UMC/Tower 300mm note ingested | Optical I/O on the package; silicon volume and InP volume move together |
| 10 | Optical fiber / connectivity | GLW, Fujikura, Furukawa, Sumitomo | Yes (3). Corning/fiber notes ingested | Fiber carries the light. Same cycle, different bottleneck, different price |
| 11 | Networking systems / DCI | Arista, Cisco, Nokia, CIEN | Yes (3). Scale-across correction ingested | Scale-across belongs to coherent optics, not CPO |
| 12 | High-density power conversion | VICR, MPS | Thin (2, not 3) | Last-millimeter conversion. P = I²R; vertical power delivery |
| 13 | Datacenter power infrastructure | Vertiv, Eaton | **Gap.** Nearest: 800V HVDC aside; GPU-repricing / hyperscaler capex | Site and rack power distribution once the dollar leaves the GPU line |
| 14 | Cooling | Vertiv, Modine, Schneider | **Gap.** Nearest: thermal budget treated as a first-class constraint | Heat as a binding rack budget, not a facilities afterthought |
| 15 | Grid infrastructure | GE Vernova, Eaton, Quanta Services | **Gap.** Nearest: nuclear-cycle map (grid as siting constraint) | Interconnect and transmission that decide where a campus can exist |
| 16 | Power generation | GE Vernova, Siemens Energy, CEG, Vistra, Cameco | Partial (2) | Generation that feeds the sites (nuclear chain; perovskite dual use) |
| 17 | Datacenter construction | Quanta Services, EMCOR, Comfort Systems | **Gap. No article.** | Physical build of the halls |
| 18 | Datacenter / powered land | Equinix, Digital Realty, hyperscalers, SPCX | Yes (3). SpaceX 10GW hardware-chain note ingested | Powered land versus 10GW orbital compute as an alternative siting |
| 19 | Storage / memory disaggregation | MRVL, MU, SNDK, CXL | Yes (3). HBF vs optics already ingested | HBF, optical memory pooling, CXL. Not the HBM line |

**Methodology.** Rank by layer job, not by ticker narrative. One entry + one structural + one current per layer, wherever the archive allows. Do not promote a nearest-coverage aside on layers 13–15 into a dedicated power / cooling / grid thesis. Do not treat layer 17 as researched. Do not fold layer 19 (HBF / pooling) into layer 2 (HBM). Do not fold layer 11 (scale-across / coherent) into layer 9 (CPO). NVIDIA revenue is not a SiPh adoption print.

**Outside this map (named, not scored):** LEO / satellite optical links (26-company map); quantum (superconducting or trapped ion, they buy the same light); defense and humanoid (20-company map).

## Evidence

All figures below are single-sourced to this 2026-08-27 PhotonCap subscriber essay (canonical URL as frontmatter; full paid body; WebFetch returned complete text). Every quantitative claim is tagged [1×: PhotonCap] or [web: photoncap.net]. This source is a map of prior PhotonCap work; it is not a new primary dataset.

| Item | Figure | Tag |
|---|---|---|
| Source access / length | Full paid article; ~1502 words | [1×: PhotonCap / WebFetch] |
| Layer count | 19 layers; up to 3 archive articles each; picked for coverage, not chronology | [1×: PhotonCap] |
| Full 3-article layers | 1–11, 18, 19 | [1×: PhotonCap] |
| Thin layer | Layer 12 (VICR / MPS): 2 articles, not 3; "archive is thin on this layer" | [1×: PhotonCap] |
| Dedicated-article gaps | Layers 13, 14, 15: no dedicated article. Layer 17: no PhotonCap article | [1×: PhotonCap] |
| Layer 13 nearest | 800V HVDC / rack power distribution (optical-axis piece); GPU-repricing / Q2 hyperscaler earnings | [1×: PhotonCap] |
| Layer 14 nearest | Thermal budget as a first-class constraint (same optical-axis piece) | [1×: PhotonCap] |
| Layer 15 nearest | Nuclear-cycle map: 13 listed companies beyond Constellation and Cameco | [1×: PhotonCap] |
| Cloud capex map | Azure +40%, AWS +28%, GCP +63%; hardware supply chain behind $580B cloud capex | [1×: PhotonCap] |
| Portfolio review (across-chain) | 1Y +124%; four months behind by 10.4pp | [1×: PhotonCap] |
| Layer 11 correction | Ciena, Nokia, Cisco down 40%, 40%, and 14% in six weeks | [1×: PhotonCap] |
| Layer 7 current read | Lumentum first $1B quarter (FQ4 2026); Innolight $6.8B then FCC ban draft | [1×: PhotonCap] |
| Layer 5 constraint | 100-second bottleneck behind NVIDIA CPO; 7 companies on a 4-stage test stack | [1×: PhotonCap] |
| Layer 3 constraint | 7 bonding-equipment companies behind HBM4 and CPO | [1×: PhotonCap] |
| Layer 7 architectures | Four optical architectures: DSP, LPO, NPO, CPO | [1×: PhotonCap] |
| Layer 12 equation | P = I²R; "last 1.5mm" of AI power; three numbers from Vicor Q1 2026 | [1×: PhotonCap] |
| Layer 18 alternative | SpaceX first earnings; hardware value chain behind 10GW | [1×: PhotonCap] |
| Outside-map maps | 26 companies in LEO satellite cycle; 20 companies in humanoid cycle | [1×: PhotonCap] |
| Load-bearing non-claim | NVIDIA revenue growth does not prove silicon photonics adoption | [1×: PhotonCap] |
| Load-bearing claim | Continued AI growth increases cluster size, bandwidth, and rack power density, pushing electrical interconnects toward physical limits | [1×: PhotonCap] |
| Already-ingested vault notes (do not re-summarize) | Memory-wall routes; rack-split optics; SKHY CPO track; Samsung/SK optical vs MU; HBF vs optics; LITE $1B; COHR FQ4 InP; FORM 29 July; SPCX 10GW; UMC/TSEM 300mm; fiber bottleneck; scale-across correction | [[Research/2026-07-26 - QCOM NVDA MU PhotonCap Three Memory Wall Routes - deep-dive]]; [[Research/2026-07-28 - NVDA AMD PhotonCap Rack Split Optics Paypoints - deep-dive]]; [[Research/2026-08-20 - 000660 NVDA MRVL - PhotonCap SKHY CPO Track - deep-dive]]; [[Research/2026-08-23 - MU 000660 - PhotonCap Samsung SK Hynix Went Optical - deep-dive]]; [[Research/2026-08-16 - SNDK MU 000660 - PhotonCap HBF vs Optics - deep-dive]]; [[Research/2026-08-12 - LITE PhotonCap FQ4 2026 First 1B Quarter - deep-dive]]; [[Research/2026-08-14 - COHR LITE AAOI - PhotonCap Coherent FQ4 InP CPO - deep-dive]]; [[Research/2026-07-30 - FORM PhotonCap July 29 HBM CPO Probe Cards - deep-dive]]; [[Research/2026-08-10 - SPCX PhotonCap First Earnings 10GW Hardware Chain - deep-dive]]; [[Research/2026-07-16 - UMC TSEM LITE PhotonCap SiPh Capacity InP Paradox - deep-dive]]; [[Research/2026-07-17 - GLW APH PhotonCap AI Datacenter Fiber Bottleneck - deep-dive]]; [[Research/2026-07-19 - CIEN NOK CSCO PhotonCap Scale-Across Correction - deep-dive]] |
| Live book on this map (Holdings table, 2026-08-25 refresh) | NVDA Medium; AVGO Medium; MRVL Medium; 000660.KS High; SNDK Low; SPCX High; 6857.T Low. MU not in the book. LITE / COHR / VICR / FORM not in the book | [vault: Live Portfolio Holdings] |

## Contradiction Check

- **Supports a spreading-bottleneck reading of [[Theses/NVDA - Nvidia]] and does not touch a registered trigger.** The thesis Summary already prices GPU hardware plus hyperscaler capex, with the deeper moat on CUDA / Omniverse / Physical AI. Networking copy already has Spectrum-X CPO platforms shipping H2 2026. This source does not add a unit, ASP, or CPO attach print. It reclassifies the guide: bottlenecks spreading, not GPU demand alone. NVDA has **no `## Conviction Triggers`**. Outstanding Q on ASIC share / InferenceX and on Jevons vs efficiency are untouched. **Does not fire** NVDA → HIGH / LOW / CLOSE. Live-book holding; conviction/status unchanged.

- **Supports [[Theses/AVGO - Broadcom]] Insight #1 and Insight #4 without a 2027-target print.** Layer 1 and layer 6 put AVGO on compute silicon *and* merchant networking. That matches "Tomahawk sits regardless of compute vendor" and "Ethernet vs InfiniBand already tipped." Layer 9 (SiPh / CPO) is adjacency to Bailly / COUPE, not a Tomahawk-6 or FQ3 AI-guide number. AVGO has **no `## Conviction Triggers`**. **Does not fire** AVGO → HIGH / LOW / CLOSE.

- **Supports [[Theses/MRVL - Marvell Technology]] Insight #2 and Insight #4; no HIGH/LOW/CLOSE print.** The map puts Marvell on layers 1, 6, 9, and 19, which is the thesis's own split (rented custom seat, owned DSP/LPO, bought memory-fabric option). "There is no such thing as a CPO stock" and "scale-across is coherent, not CPO" are the same hygiene as Insight #2 (Celestial ≠ switch-I/O CPO). Copper-wall / 1.6T is Insight #4 adjacency. **Does not fire** HIGH (Google commercial agreement is already an 8-K; this piece adds no T3 ≥400K and no Celestial PO/tape-out), LOW, or CLOSE.

- **Supports [[Theses/000660 - SK Hynix]] Insight #3 hygiene; no allocation print.** Layer 2 is HBM/DRAM; layer 19 is HBF / optical pooling. The list keeps them apart, which is the instruction not to merge the 20 August CPO track into HBF. Optical-memory ranking is already in [[Research/2026-08-23 - MU 000660 - PhotonCap Samsung SK Hynix Went Optical - deep-dive]]. **Does not fire** 000660 → HIGH / LOW / CLOSE (no Rubin share %, no Namics, no CXMT, no Kinex 16-Hi). Live-book holding; conviction/status unchanged. MU appears on layers 2 and 19 as a named memory maker; MU is a thesis name, not a live-book holding.

- **Supports [[Theses/SNDK - SanDisk]] HBF Insight as a layer-19 object, not a 2026 earnings line.** HBF and optical memory pooling are listed under storage / memory disaggregation, which matches "TAM creation, Google-not-NVIDIA attach, not a Rubin baseline." SNDK has **no `## Conviction Triggers`**. Flag only.

- **[[Theses/SPCX - SpaceX]] layer-18 adjacency only.** The third layer-18 article is the already-ingested first-earnings / 10GW hardware-chain note. That is the thesis's "orbital compute as alternative to powered land" option, cadence-gated, not a YE26 nameplate or CSA-duration print. **Does not fire** SPCX → HIGH / LOW / CLOSE.

- **[[Theses/6857 - Advantest]] layer-5 adjacency only.** The 100-second / 4-stage CPO test stack and FORM's probe-card cycle sit next to the HBM test-time thesis; they are not HBM4 production test-time >14 hours and not a Teradyne HBM5 qualification. **Does not fire** 6857 → HIGH / LOW / CLOSE. FORM Insight #3 (toll booth on test-time regardless of ATE vendor) and Insight #4 (SiPh wafer test) are the matching layer-5 claims; FORM is not in the live book.

- **Optics and power theses (not live book).** [[Theses/LITE - Lumentum]] Insight on SiPh foundry buildout being bullish for InP, and the arms-dealer EML position, are the layer 7–9 mechanism. [[Theses/COHR - Coherent]] Insight that CPO vs NPO is the wrong axis (content lands either way) is the layer 7–9 / 11 mechanism. [[Theses/VICR - Vicor Corporation]] P = I²R / last-1.5mm VPD is layer 12; the archive is thin there, which matches a two-article shelf, not a new socket disclosure.

- Honest low-signal caveat: this is an annotated bibliography, not new primary research. No Rubin allocation %, no HBM test-time in production, no Celestial PO, no CSA duration, no 6-inch InP share, no VPD socket confirmation. The only new claim is taxonomic (19 layers; gaps at 13–14–15–17; NVIDIA guide = spreading bottlenecks). Do not promote the map into a conviction or status change on any name.

## Source Excerpts

> "NVIDIA’s guidance points to something much broader than stronger GPU demand. The key signal is that AI infrastructure bottlenecks are spreading across memory, packaging, networking, optics, power, cooling, grid capacity, and datacenter construction."

> "NVIDIA’s revenue growth itself does not prove silicon photonics adoption."

> "The stronger argument is that continued AI growth increases cluster size, bandwidth requirements and rack power density, pushing electrical interconnects closer to their physical limits."

> "AI is no longer just a semiconductor buildout. It is becoming a memory, networking, optics, power and physical-infrastructure buildout."

> "Nineteen layers, up to three articles each. Picked for coverage, not chronology: one entry point, one structural piece, one current read wherever the archive allows."

> "No dedicated article yet." (layers 13, 14, 15)

> "Coverage gap. No PhotonCap article sits on this layer." (layer 17, datacenter construction)
