---
date: 2026-07-28
tags: [research, Semiconductors, NVDA, AMD, Optics, CPO]
sector: Custom Silicon & Networking Semiconductors
ticker: NVDA
propagated_to: [LITE, NVDA]
source: 'https://photoncap.net/p/same-split-opposite-directions-where'
source_type: deep-dive
---

## Thesis Delta
Consensus slogan "optics wins either way" on inference disaggregation → PhotonCap argues **where** NVIDIA (AFD inside decode, per-token GPU↔LPU exchange) vs AMD+Cerebras (PD split, per-request KV handoff) cut the rack decides copper vs pluggable vs CPO revenue mix. Total optics likely grow; stock selection hinges on E/O conversion location at each link end. Tightens [[Theses/NVDA - Nvidia]] / [[Theses/AMD - Advanced Micro Devices]] interconnect mapping and [[Theses/LITE - Lumentum]] exposure as mix (module vs CW/ELS) not binary CPO adoption.

## Summary
NVIDIA Groq license (Dec 2025) → LPX rack (256 LPUs, 128GB SRAM / 40 PB/s on-chip BW) beside NVL72; AFD loop exchanges every output token (docs silent on physical medium). AMD Advancing AI (Jul 23): Helios + Cerebras WSE for PD disaggregation; link undisclosed; vendor claim up to 5× tok/s/W vs WSE-only. Prefill (HBM/compute) vs decode (SRAM/latency) physics motivates rack split. In-rack scale-up locked to copper (NVLink 6 spine ~5,000 cables / 260 TB/s; Helios UALoE copper; SemiAnalysis est. ≤85% paths need Broadcom retimers). Scale-out: NVL72 28.8 TB/s bidirectional via ConnectX-9; Helios up to 43.2 TB/s (3×800G Vulcano). Spectrum-6 SPX includes 102.4 Tb/s CPO switch **and** OSFP cages — CPO + pluggable coexist. Multi-rack optical scale-up on roadmap (Vera Rubin Ultra NVL576 copper+direct optics; Kyber NVL1152; AMD MI500 CPC/CPO/NPO per SemiAnalysis est.). March $2B each into COHR/LITE raises demand visibility without disclosing CPO/pluggable mix. Monitoring: NVL72–LPX medium disclosure; Helios+Cerebras deployments H2'26; Vulcano 2-vs-3 NIC; NVL576 optics suppliers; Tower/SiPh orders.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| LPX config | 256 LPUs; 500MB SRAM/chip; 150 TB/s on-chip | [1×: NVIDIA blog / PhotonCap] |
| NVL72 scale-up / scale-out | 260 TB/s / 28.8 TB/s bi | [1×: NVIDIA] |
| Helios max scale-out | 43.2 TB/s bi (3×800G NIC) | [1×: AMD / PhotonCap] |
| DistServe KV example | ~1.1GB / 512-tok; ~90Gbps @10 rps | [1×: DistServe / PhotonCap] |
| Spectrum-6 CPO | 102.4 Tb/s; 512×200G lanes | [1×: NVIDIA] |
| NVDA optics bets | $2B COHR + $2B LITE (Mar 2026) | [1×: NVIDIA NR] |
| AFD cadence | every output token | [1×: NVIDIA LPX blog] |

## Contradiction Check
Challenges blanket "CPO kills modules" and "disaggregation = automatic optics win." Supports vault view that optical revenue is an **allocation inside a growing pie**. Falsifiers: AFD/PD retreat as next-gen HBM absorbs split benefits; NVL72–LPX disclosed as short copper; CPO standardization collapses OSFP faster than base case.

## Framework / Mental Model
Ask not "is the link CPO?" but "where does E/O happen at each end?" Switch-side CPO can coexist with endpoint OSFP on the same link.

## Source Excerpts
> "My conclusion is one notch narrower than 'optics wins either way.' The total volume of optics probably grows. Whether that revenue lands in modules, external lasers, CPO optical engines, or switch silicon is decided by where, on each link, light gets created and turned back into electricity."
