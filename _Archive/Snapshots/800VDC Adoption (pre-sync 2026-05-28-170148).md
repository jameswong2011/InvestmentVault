---
snapshot_of: "[[Macro & Technology/800VDC Adoption]]"
snapshot_date: 2026-05-28
snapshot_trigger: sync
snapshot_batch: sync-6981-2026-05-28-170148
date: 2026-05-18
tags: [macro, technology, power, 800VDC, data-center, AI-infra, NVDA, VICR, VRT]
status: active
sector: Data Center Power & Cooling
source: vault synthesis — three Claude Deep Research reports (May 2026) on (a) 800VDC institutional equity research, (b) grid-to-rack 800VDC equity map, (c) solid-state transformer bottleneck map; supplemented with May 2026 web search on NVIDIA GTC 2026 announcements, Vertiv/Schneider/Eaton/Delta product launches, OCP Mt. Diablo v0.7.0, Amperesand and Enphase SST commercialization, and Korean transformer trio order book
---

# 800VDC Adoption

*Tracker document for the move from 415/480VAC + 48VDC rack power to 800V DC architectures. Multi-source synthesis intended to be updated as inflection points hit. Sources: [[_Inbox/processed/compass_artifact_wf-60b03808-306c-48ca-9868-6ea5b811bd10_text_markdown|Report A: Institutional Equity Research]], [[_Inbox/processed/compass_artifact_wf-673fe644-ff19-4677-a601-26f9af21d15e_text_markdown|Report B: Grid-to-Rack Equity Map]], [[_Inbox/processed/compass_artifact_wf-f16530a3-3670-4658-b53b-01b9a07ffdba_text_markdown|Report C: SST Bottleneck Map]].*

## Thesis Delta

- **The shift is driven by current, not efficiency.** At 600 kW per rack (Rubin Ultra Kyber, H2 2027), a 48V busbar would carry ~12,500 A — mechanically and thermally infeasible. 800VDC reduces required current 16×, ohmic loss ~256× at the same conductor, and frees ~64U of rack space that 54V PSU shelves would otherwise consume at MW scale. NVIDIA's own marketing claims (5% efficiency, 70% PSU maintenance reduction, 30% TCO) are real but secondary — the equity story is *compute-capacity unlock*, not *efficiency arbitrage*.

- **Two competing architectures wear the "800VDC" label, and hyperscalers will run both in parallel.** NVIDIA's row-rectified single-bus 800VDC is vertically integrated to Rubin/Kyber; OCP Mt. Diablo (Diablo 400 v0.7.0, March 2026 — up from v0.5.2 May 2025) is a *sidecar* power rack co-authored by Google, Meta, Microsoft that outputs ±400V *or* 800V and accepts Trainium, MTIA, Maia, AMD MI, and NVIDIA. Most hyperscalers operate both inside the same estate. Bullish for *total* supplier TAM, bad for any single-architecture bet.

- **For the vault, this is the macro that pulls forward [[Theses/VICR - Vicor Corporation]] structurally**, validates [[Theses/VRT - Vertiv Holdings]] H2 2026 portfolio launch timing, raises adjacency questions for [[Theses/NVDA - Nvidia]] (chip roadmap *sets* 800VDC adoption curve) and [[Theses/6981 - Murata Manufacturing]] (~450,000 MLCCs/rack at GB300, 3.3× FY30 AI-server MLCC demand), and introduces new monitoring candidates (Korean transformer trio HD Hyundai/Hyosung/LS Electric; Eaton ETN; Delta 2308.TW; Disco 6146.T; nanocrystalline core oligopoly Proterial/Qingdao Yunlu).

- **Real adoption is gated by *liquid cooling penetration*, *SST/SiC supply*, *DC protection standards* (UL/IEC/NEC are still maturing), and *operator training* — not by silicon performance.** Sell-side has not yet published architecture-segmented adoption forecasts. Synthesized base case from these three Deep Research reports: ~10–15% of *new* AI-rack capacity in 2027, ~35–45% by 2029, ~65–75% by 2032. General-purpose enterprise stays under 10% on 800VDC through 2030 in every scenario — economics do not pencil at 10–20 kW/rack.

## Summary

800VDC is the architectural endpoint of NVIDIA's chip roadmap colliding with the physics of 48V rack distribution. The chain breaks down at ~250 kW/rack, and the GB200 NVL72 already runs at ~120–132 kW; the Vera Rubin NVL144 (H2 2026) projects to ~250 kW; the Rubin Ultra Kyber NVL576 (H2 2027) targets ~600 kW; post-Kyber Feynman-generation racks trend toward 1 MW+ and potentially ±1500VDC. The decisive number is current density per busbar: at 48V the GB200 already needs ~2,500 A; at 600 kW it would need ~12,500 A, which is mechanically untenable. Stepping voltage 16× cuts current 16× and I²R loss ~256×, and the 45% copper reduction (NVIDIA's most physically defensible claim, vs. the marketing efficiency numbers) becomes a binding capex enabler at gigawatt-class campuses where rack busbar copper alone would be ~200,000 kg.

The supplier ecosystem materialised at OCP October 2025 and was confirmed at NVIDIA GTC 2026 (March 2026) where Eaton's Beam Rubin DSX, Delta's 800 VDC 660 kW in-row power rack with 480 kW BBU, Liteon's 800 VDC + 110 kW power shelf, and STMicroelectronics's 12V and 6V on-rack architectures all moved from concept to co-designed product. Vertiv has stated its 800VDC portfolio ships H2 2026 — "ahead of Kyber/Rubin Ultra." Schneider's sidecar (up to 1.2 MW per rack, unipolar 800V or bipolar ±400V) is validated at Digital Realty Manassas via the AI Factory Research Center. Eaton acquired Resilient Power Systems (August 2025) for SST IP and runs ~24 SST pilots with hyperscalers, expecting first orders late-2026 for 2027 ship. NVIDIA's full silicon ecosystem spans ADI, AOS, EPC, Infineon, Innoscience, MPS, Navitas, onsemi, Power Integrations, Renesas, Richtek, ROHM, STMicro, TI — every meaningful Western and Japanese power-semi house plus the only Chinese GaN name (Innoscience) and the Israeli VPD specialist (Vicor) via separately announced collaborations.

Adoption is gated by four real-world constraints that the market under-prices. (1) **Liquid cooling penetration** is a prerequisite — at 50 W/cm² die heat flux and 600 kW/rack thermal load, direct-to-chip cold plates are non-negotiable. Uptime Institute 2024 reports 22% of operators using DLC, <10% of racks in those facilities. SemiAnalysis treats AI training facilities as 100% DLC; enterprise is far behind. If DLC stalls, 800VDC stalls. (2) **Solid-state transformer maturity** is the upstream bottleneck — Western commercial SSTs (Infineon+SolarEdge 2–5 MW SST building block, Wolfspeed 10 kV SiC MOSFETs, Eaton MV SST post-Resilient) ship late-2026 to 2027 in pilot volumes; the binding constraint is not SiC wafers but *packaged ≥3.3 kV SiC modules* plus *nanocrystalline magnetic cores* (Proterial/Hitachi Metals FINEMET, Qingdao Yunlu, AT&M, VAC control >85% of supply). (3) **DC protection standards** lag deployment — DC arcs have no zero-crossing; NFPA 70E incident-energy formulas were built for AC; resettable circuit breakers in this voltage class are still maturing; UL/IEC/IEEE working groups are running lab tests but standards are 2026–2028 work items. (4) **Operator training and AHJ comfort** — only one widely-cited operational reference (Foxconn Kaohsiung-1, 40 MW in Taiwan) means actuarial pricing for 800VDC datacenter insurance is unbounded.

Where the structural alpha sits is not where retail attention is concentrated. The wide-bandgap semi names (Wolfspeed, Navitas, Infineon, onsemi) are mid-cycle plays whose bullishness is well-priced; the *under-priced* oligopolies sit upstream in (a) Korean ultra-high-voltage transformers (HD Hyundai Electric, Hyosung Heavy, LS Electric — combined Q1 2026 backlog >₩32 trillion, orders booked through 2031, 765 kV US transmission ~50% Hyosung share, US-local production tariff-protected), (b) Japan/Korea high-cap MLCC oligopoly (Murata 33% share, Samsung-EM, TDK, Taiyo Yuden — 70–80% combined global share, Murata 15–35% price hike effective April 1 2026, AI-server MLCC demand 3.3× FY30 vs FY25), (c) SiC dicing equipment (Disco, >70% share, every new SiC fab installs Disco tools, ROIC 54% FY25), (d) nanocrystalline magnetic cores (Proterial ~45% global share, Qingdao Yunlu ~16% — the single biggest physical bottleneck for SST scaling), and (e) vertical power delivery on-board where the IP gate is 5–7 years and Vicor's 2nd-gen VPD spec (3 A/mm², 40× current multiplication, 1.5 mm package) currently has no commercial peer. The shared characteristic of these five categories: physical bottlenecks with concentrated suppliers that compound *regardless* of which architecture (NVIDIA row-rectified vs OCP sidecar) ultimately wins.

## Framework / Mental Model

### "Compute-capacity unlock, not efficiency arbitrage"

| Conventional framing | Correct framing |
|---|---|
| 800VDC is more efficient than AC distribution | 800VDC is the *only physically plausible path* above ~250 kW/rack |
| 5% efficiency gain drives adoption economics | 45% copper reduction + 64U rack-space recovery drives adoption physics |
| Adoption curve set by TCO crossover | Adoption curve set by NVIDIA chip roadmap and DLC penetration |
| Bull case: AC datacenters retrofit to 800VDC over 2026–2030 | Bull case: greenfield AI factories deploy 800VDC over 2027–2032; enterprise stays AC under 10 kW/rack |

### Architecture fork: row-rectified (NVIDIA) vs sidecar (Mt. Diablo)

| Dimension | NVIDIA reference | OCP Mt. Diablo (Diablo 400 v0.7.0, Mar 2026) |
|---|---|---|
| Authorship | NVIDIA (Mathias Blake et al., May 2025 blog; Oct 2025 OCP) | Google + Meta + Microsoft |
| Conversion topology | Single-stage: 13.8 kV MV AC → 800VDC at row → 64:1 LLC DC/DC at GPU | Two-stage: AC → ±400V/800V in sidecar rack → DC/DC at compute |
| Accelerator scope | Vertically integrated to Rubin/Kyber | Accelerator-agnostic (Trainium, MTIA, Maia, AMD MI, NVIDIA) |
| Output | Unipolar 800V | Configurable ±400V *or* 800V |
| Retrofit fit | Greenfield-only (single bus to row) | More retrofittable to existing 480VAC plant (sidecar adapts) |
| Strategic intent | Pulls power-infrastructure roadmap into NVIDIA's tempo | Decouples power from any single silicon vendor; supply-chain analog of EV 400V→800V transition |
| Hyperscaler posture | Required for any NVIDIA Kyber-class deployment | Reference for custom-ASIC racks; complements NVIDIA islands in same campus |

The strategic implication is that hyperscalers operate **both architectures in parallel** inside the same estate, partitioned by silicon vendor: NVIDIA islands on row-rectified 800VDC; Trainium/Maia/MTIA islands on Mt. Diablo sidecar. Total supplier TAM expands; any single-architecture bet is fragile.

### Historical analog: 48V displacing 12V in OCP racks

The 48V over 12V transition in Open Compute racks took ~8 years from initial spec (~2014, Google initial proposal) to majority adoption (~2022, when Hopper-era HGX broadly shipped on 48V). The 800VDC transition has the same gating mechanism (architectural shift driven by current density at the compute layer) but moves faster because (a) the silicon vendor is one company (NVIDIA) with roadmap control, vs. multi-vendor 48V which negotiated through OCP, and (b) the rate-limiting factor below is liquid cooling, not the voltage transition itself — DLC has been the binding constraint already, so the incremental 800VDC adoption decision is "easy" once DLC is committed.

### The bottleneck cascade

Five layers, each with a binding constraint that gates the next:

1. **Grid → MV AC**: utility transformer supply (Wood Mackenzie Q2 2025: 128-week lead times for power transformers, 144-week for GSUs; +77% pricing since 2019). Beneficiary: Korean transformer trio (HD Hyundai, Hyosung Heavy, LS Electric).
2. **MV AC → 800VDC perimeter**: solid-state transformer or industrial rectifier (binding: ≥3.3 kV SiC modules + nanocrystalline cores). Beneficiary: Eaton (Resilient), Vertiv, Schneider, ABB, Hitachi Energy, Mitsubishi Electric, Delta.
3. **800VDC distribution → rack**: DC busways, BBUs, DC switchgear, DC arc protection (binding: resettable DC breakers still maturing; DC arc-flash standards in flight). Beneficiary: Vertiv, Schneider, ABB, Eaton, BizLink.
4. **Rack → compute board**: 800V→48V→core-voltage step-down (binding: SiC/GaN front-end + GaN intermediate stages). Beneficiary: Infineon, onsemi, Innoscience, ROHM, MPS, Navitas, ST.
5. **Board → silicon die**: vertical power delivery / current multiplication at >2,000 A (binding: 5–7 year IP gate at the module-fabrication layer). Beneficiary: Vicor (currently the only commercial vendor of 2nd-gen VPD at 3 A/mm² + 40× multiplication + 1.5 mm thickness).

The cascade matters because *the layer with the slowest-moving bottleneck sets the adoption pace for the whole chain*. Today the binding layer is liquid cooling penetration at the operator level; once DLC saturates AI greenfields (likely 2027–2028 per SemiAnalysis), the binding layer rotates to nanocrystalline cores + ≥3.3 kV SiC packaged modules.

## Architecture and rack power trajectory

NVIDIA's published per-rack power, generation by generation:

| Generation | Rack | GPUs/rack | Power | Voltage at rack |
|---|---|---|---|---|
| Hopper H100 | HGX | 8 | ~40 kW | 415VAC → 48V |
| Blackwell GB200 NVL72 (current) | Oberon | 72 | ~120–132 kW | 415VAC → 54V |
| Blackwell Ultra GB300 NVL72 (current) | Oberon | 72 | up to 142 kW | 415VAC → 54V |
| Vera Rubin NVL144 (H2 2026) | Oberon | 144 dies | ~250 kW (est.) | 480VAC → 54V; some 800VDC pilots |
| Rubin Ultra Kyber NVL576 (H2 2027) | Kyber | 576 dies | ~600 kW | 800VDC required |
| Post-Kyber / Feynman (2028+) | TBD | TBD | trending toward 1 MW+ | 800VDC, potentially ±1500VDC |

Disclosed by Vertiv: the 800VDC portfolio (centralized rectifiers, DC busways, rack-level DC/DC converters, energy storage integration) releases H2 2026 with explicit alignment to Rubin Ultra in 2027 (Scott Armul, EVP Global Portfolio). Schneider showed an 800VDC sidecar supporting up to 1.2 MW at GTC October 2025 and reaffirmed at GTC March 2026, with the AI Factory Research Center validated at Digital Realty's Manassas, VA site. Delta has shown an 800VDC In-Row 660 kW Power Rack with 480 kW BBU and up to 98% AC-DC efficiency, plus a 1.1 MW "AI Power Cube." Eaton's "Beam Rubin DSX" co-design platform launched at GTC March 2026; ABB and Mitsubishi Electric announced 800VDC partner status at OCP October 13, 2025.

**Every major supplier ships exactly when Rubin Ultra ships.** There is essentially no qualified field experience available to authorities-having-jurisdiction (AHJs) or insurers as of mid-2026. The H2 2026 product GA window is the single most-loaded slip-risk event in the entire timeline; any one of Vertiv/Schneider/Delta/Eaton missing creates a critical-path delay.

## Hyperscaler posture matrix

| Operator | 800VDC posture | Architecture preference | Custom-ASIC roadmap on 800VDC |
|---|---|---|---|
| **Google** | Most aggressive non-NVIDIA hyperscaler. OCP EMEA 2025 ±400VDC for racks up to 1MW; projects >500 kW/rack before 2030 | Mt. Diablo sidecar (co-author) | TPU racks today use 416VAC AC inputs with on-rack rectifiers; transition staged via Diablo |
| **Meta** | Mt. Diablo co-author. ORv3 HPR v3 → 300 kW; v4 targets 400VDC and 800 kW–1 MW | Mt. Diablo sidecar (co-author) | Clemente 1RU compute tray (first ORv3 HPR with sidecar). AMD Helios built on Meta's Open Rack Wide spec |
| **Microsoft** | Mt. Diablo co-author. Maia 200 (216 GB HBM3e, 750 W) in liquid-cooled racks in Iowa, up to 6,144 chips. Less crisp 800VDC commitment than Google | Mt. Diablo sidecar (co-author); some NVIDIA islands | Maia 200 deployed with 2nd-gen closed-loop liquid cooling; no public 800VDC commitment as of May 2026 |
| **AWS** | Laggard. Trainium2 racks at 27 kW air-cooled; Project Rainier in Indiana (~400k Trainium2 for Anthropic, 455 MW Phase 1 + 1,040 MW Phase 2) on conventional 415/480VAC | Not on either roadmap publicly | Reportedly evaluating selling Trainium racks externally. Cost-per-token optimization on lower-density hardware |
| **Oracle / OCI** | Listed in NVIDIA's "designing for 800VDC" attribution; not corroborated by first-party press | NVIDIA row-rectified (implied) | NVIDIA-dependent; no public custom-ASIC roadmap |
| **CoreWeave** | NVIDIA-attributed for 800VDC adoption; first-party commitment is to Rubin specifically. >5 GW of AI factories by 2030 with NVIDIA | NVIDIA row-rectified | None |
| **Lambda / Nebius / Together AI** | NVIDIA-attributed only; no first-party 800VDC press as of May 2026 | NVIDIA row-rectified (presumed) | None |

**The bifurcation is real.** Hyperscalers with mature custom-ASIC programs (Google, Meta, Microsoft) authored Mt. Diablo precisely to avoid tying their non-NVIDIA fleets to NVIDIA's rack architecture. NVIDIA's own design optimizes for Rubin/Kyber and is incompatible with accelerator-agnostic sidecar economics. Equity narratives that assume all hyperscaler AI is "going 800VDC" through one architecture are oversimplified — the question is *which architecture per silicon island*, not *whether*.

## Adoption forecast (synthesized)

No bulge-bracket sell-side analyst has published a specific architecture-segmented adoption forecast for 800VDC. Goldman's November 2025 GS SUSTAIN raised 2030 datacenter power demand to 175% vs. 2023 (~1,350 TWh by 2030) but does not split AC vs DC. Dell'Oro tracks DCPI with high-density-power research projecting DCPI to surpass $80B by 2030 with thermal management ~20% CAGR — paywalled, no DC-architecture split. The MarketsandMarkets US-specific *SST datacenter* sub-segment projects $40.3M (2025) → $154.0M (2030) at 30.8% CAGR — a narrow slice, useful as a SST-specific calibration but not whole-stack.

Synthesized base case (from Report A, sanity-checked against Reports B+C, % of *new* AI-specific rack capacity deployed with native 800VDC):

| Year | Base | Bull | Bear |
|---|---|---|---|
| 2027 | 10–15% | 25–30% | 5–8% |
| 2028 | 25–35% | 50%+ | 10–15% |
| 2029 | 40–50% | 65%+ | 20–25% |
| 2030 | 55–65% | 80%+ | <35% |
| 2032 | 70–80% | — | — |

**General-purpose enterprise** stays under 10% on 800VDC through 2030 in every scenario. The driver is not there at 10–20 kW/rack densities, and retrofit economics are punishing (cooling retrofit alone is $500–$1,500/kW; full electrical retrofit to 800VDC roughly doubles that). 90%+ of 800VDC deployments through 2030 will be greenfield AI factories. Retrofit-serviceable opportunity is ~8–15 GW out of a ~42 GW gross addressable base, concentrated in high-end colocation modernization.

## Inflection points to monitor (chronological)

| Window    | Event                                                                                                      | What it tells us                                                                                                               |
| --------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| H2 2026   | Vertiv / Schneider / Delta / Eaton 800VDC product **GA**                                                   | Slip risk is real; any miss creates critical-path delay. Tracked by company quarterly reports and OCP Summit Oct 2026          |
| H2 2026   | NVIDIA **Vera Rubin NVL144** actual deployment voltage                                                     | If Rubin in 2026 ships on 480VAC/54V (per Schneider reference), 800VDC inflection slips to Rubin Ultra in 2027                 |
| H2 2026   | First non-NVIDIA-marketing first-party 800VDC commitment from US neocloud                                  | Lambda/Nebius/Together AI/OCI press release; absence is suspicious given NVIDIA's loud attribution                             |
| Late 2026 | Eaton SST orders for 2027 shipment                                                                         | First volume SST order book; tells us SST move from pilot to commercial pace                                                   |
| Q1 2027   | OCP "Data Center Facilities Power Distribution" **v2.0**                                                   | v1.0 (Q1 2026, 190+ contributing companies) is directional; v2.0 with technical requirements is operational milestone          |
| Q1 2027   | Mt. Diablo specification **1.0 finalization**                                                              | Currently v0.7.0 (March 2026), v0.5.2 (May 2025). Convergence with NVIDIA on connector/protection interop = strong bull signal |
| H1 2027   | First major insurance carrier publishing 800VDC datacenter actuarial guidance                              | Unlocks broader operator adoption beyond Foxconn-class pioneers                                                                |
| H2 2027   | **Rubin Ultra Kyber** production deployment at a named hyperscaler                                         | Single largest single-event validation in the cycle                                                                            |
| 2027–28   | Federal Circuit decision on Vicor LEO (relevant to [[Theses/VICR - Vicor Corporation]] licensing pipeline) | Narrowing reduces licensing rents from $300M pipeline to $50–100M run-rate                                                     |
| 2027–28   | NEC 2029 cycle and UL listings for 800VDC datacenter equipment                                             | Without these, AHJ approvals remain bespoke; codifies the standard                                                             |
| Any time  | First public DC arc-flash incident                                                                         | Gates personnel-training and PPE economics; could trigger UL/IEC moratorium                                                    |
| Any time  | AMD MI500 (2027) competitive performance per rack on non-800VDC architecture                               | Would undermine NVIDIA's density-forcing thesis and slow Mt. Diablo + NVIDIA adoption alike                                    |

## Value chain map and named beneficiaries

*Financial columns below — **AI-DC Rev / OP** (% of consolidated revenue and operating profit attributable to AI-datacenter demand) and **ROIC / EV/EBIT (LTM)** — are directional estimates synthesized from May 2026 public disclosures, segment splits, and sell-side coverage. Most names do not formally disclose AI-DC segment economics, so figures should be read as ranges, not point estimates. Private companies marked `n/a`. Unprofitable / pre-revenue names marked `n/m`.*

### Layer 1 — Grid and MV switchgear (AC side, structural shortage)

| Name | Ticker | AI-DC Rev / OP | ROIC / EV/EBIT (LTM) | Exposure | Why it matters |
|---|---|---|---|---|---|
| **HD Hyundai Electric** | 267260.KS | ~30% / ~35% | ~25% / ~12x | Korean transformer trio | Q1 2026 orders $1.797B (42.6% of FY target in 3 months); backlog $7.888B; Alabama plant expanding for 765 kV by 2027 |
| **Hyosung Heavy Industries** | 298040.KS | ~25% / ~30% | ~18% / ~11x | Korean transformer trio | Q1 2026 orders ₩4.17T (largest ever); 765 kV US transmission ~50% share; ₩330B HVDC plant in Changwon |
| **LS Electric** | 010120.KS | ~15% / ~20% | ~14% / ~11x | Korean transformer trio | Busan expansion; AWS switchgear contract ₩170B; Bloom Energy distribution ₩319B |
| **Hitachi (Hitachi Energy)** | 6501.T | ~10% / ~15% | ~9% / ~14x | NVIDIA 800VDC partner | $1B+ US investment incl. $457M South Boston VA new large-power-transformer plant (operational 2028, largest in US); 40-month lead times still unclosed |
| **Eaton** | ETN | ~15% / ~20% | ~17% / ~23x | NVIDIA partner + traditional MV | Q1 FY26: $7.5B (+17%), datacenter orders +240%, 228 GW backlog (~12 years at 2025 build rates); Beam Rubin DSX + ~24 SST pilots |
| **Siemens Energy** | ENR.DE | ~5% / ~8% | ~6% / ~15x | NVIDIA partner | $150M North Carolina transformer plant; less aggressive on SST than ABB/Hitachi |
| **ABB** | ABBN.SW | ~8% / ~12% | ~16% / ~18x | NVIDIA partner | DC-rated breakers + busways for 800V/1MW racks; MegaFlex UPS line; Siemens Energy power-electronics asset acquisition strengthens SST stack |
| **GE Vernova** | GEV | ~8% / ~10% | ~10% / ~20x | NVIDIA partner | No productized SST yet — most-likely large-cap acquirer of private SST IP (Heron Power candidate) |
| **China XD** | 601179.SS | ~8% / ~10% | ~7% / ~10x | China MV power electronics | Subsidiary Xi'an XD Power Electronics delivered 2.4 MW SST to "East Data West Computing"; best Chinese listed SST proxy |

### Layer 2 — Solid-state transformer / industrial rectifier (perimeter conversion)

| Name | Ticker | AI-DC Rev / OP | ROIC / EV/EBIT (LTM) | Exposure |
|---|---|---|---|---|
| **Vertiv** | VRT | ~65% / ~75% | ~25% / ~28x | [[Theses/VRT - Vertiv Holdings]]. Named NVIDIA 800VDC reference partner. Portfolio launch H2 2026. ~15–20% HVDC share. 4,000+ FSEs as switching-cost moat. (Note: source reports vary between 4,000+ and 5,000+; Vertiv Dec 2025 fact sheet states >5,000 FSEs globally.) |
| **Schneider Electric** | SU.PA / SBGSY | ~15% / ~20% | ~15% / ~22x | Co-developed with NVIDIA at GTC Paris June 2025 + OCP Oct 2025; Motivair-based integrated power+cooling control framework (March 2025 acquisition); EU AI Continent Action Plan anchor |
| **Delta Electronics** | 2308.TW | ~35% / ~45% | ~17% / ~22x | OCP 800VDC whitepaper author; ~60–65% HVDC share (Insightology); ~50%+ AI server PSU share (Goldman/Yole). Per-server revenue path $43,800 (GB200) → $90,600 (GB300) → ~$171,000 (Rubin Ultra). "Panama Power" MV-DC co-developed with Alibaba |
| **Mitsubishi Electric** | 6503.T | ~5% / ~8% | ~10% / ~13x | Sole vertically-integrated SST player globally (MV SiC modules + MV switchgear + integration). 3.3 kV UnifullTM SBD-embedded SiC MOSFETs at 200/400/800A; 6.5 kV demonstrated 9.3 kVA/cm³ |
| **Hitachi Energy** | (within 6501.T) | ~10% / ~15% | ~9% / ~14x | March 2026 next-gen MV SST development announcement for US AI hyperscalers |
| **Eaton (post-Resilient)** | ETN | ~15% / ~20% | ~17% / ~23x | August 2025 Resilient Power Systems acquisition; ~24 SST pilots; first orders late-2026 for 2027 ship |
| **Amperesand** | private | n/a | n/a | $80M Series A Nov 2025 (Walden Catalyst + Temasek, TDK Ventures strategic); 30 MW commercial deliveries 2026 starting Port of Singapore + hyperscaler pilots |
| **Heron Power** | private | n/a | n/a | $140M Series B Feb 2026 (a16z American Dynamism + Breakthrough Energy); $183M total; 40 GW factory plan; likely strategic acquirer 2026–27 |
| **DG Matrix** | private | n/a | n/a | $60M Series A Feb 2026 (Engine Ventures led, Mitsubishi Heavy + ABB strategic); multi-port SST |
| **Enphase Energy** | ENPH | <5% / n/m | n/m / ~30x | IQ SST announced May 4 2026 — entered AI datacenter power market; demos late 2026, pilots 2027, commercial 2028 |
| **SolarEdge** | SEDG | <5% / n/m | n/m / n/m | November 2025 SolarEdge–Infineon SST building block (2–5 MW, 13.8–34.5 kV AC → 800–1500 V DC, >99% efficiency) |

### Layer 3 — DC distribution, busways, DC switchgear, BBU/supercap

| Name | Ticker | AI-DC Rev / OP | ROIC / EV/EBIT (LTM) | Exposure |
|---|---|---|---|---|
| **Vertiv** | VRT | ~65% / ~75% | ~25% / ~28x | Centralized rectifiers, DC busways, rack-level DC/DC, DC-compatible BBUs |
| **BizLink** | 3665.TW | ~40% / ~50% | ~18% / ~15x | NVIDIA-named partner; 800V busway, liquid-cooled rack busbar, OCP ORv3 connectors; BzLisa S series for power-shelf interconnection |
| **Amphenol** | APH | ~15% / ~20% | ~18% / ~22x | Connector adjacency |
| **TE Connectivity** | TEL | ~10% / ~13% | ~12% / ~17x | Liquid-cooled busbar shown at OCP 2025 |
| **EnerSys** | ENS | ~10% / ~12% | ~10% / ~12x | BBU/supercap content. 30%+ transient load steps on GPUs in microseconds force in-rack BBU |
| **Mersen** | MRN.PA | ~10% / ~15% | ~12% / ~12x | DC fuses |
| **Littelfuse** | LFUS | ~10% / ~13% | ~14% / ~17x | DC protection |
| **Sungrow** | 300274.SZ | ~5% / ~10% | ~18% / ~14x | China AIDC division established May 2025; products 2026 |

### Layer 4 — Wide-bandgap silicon (SiC for front-end, GaN for high-frequency intermediate / PoL)

| Name | Ticker | AI-DC Rev / OP | ROIC / EV/EBIT (LTM) | Exposure | Notes |
|---|---|---|---|---|---|
| **Infineon** | IFX.DE / IFNNY | ~12% / ~18% | ~12% / ~22x | Broadest Si/SiC/GaN portfolio on NVIDIA silicon list. CoolGaN G5 (650V) + G3 medium-voltage on 8-inch lines (Kulim, Villach); 12-inch GaN transition planned | Cleanest large-cap wide-bandgap play. Power GaN market $355M (2024) → ~$3B by 2030 at 42% CAGR (Yole *Power GaN 2025*) |
| **onsemi** | ON | ~10% / ~15% | ~15% / ~14x | EliteSiC platform; Dec 2 2025 MoU with Innoscience (200mm GaN-on-Si); GlobalFoundries parallel collaboration; Sept 23 2025 Aura Semiconductor Vcore IP acquisition explicitly targeting 800VDC | Sampling 1H 2026; heavy-auto SiC offset |
| **Innoscience** | 2577.HK | ~30% / ~50% | n/m / n/m | Only Chinese supplier on NVIDIA silicon list. Suzhou 8-inch GaN-on-Si IDM at 15,000 wpm (97% yield); Google design-in Feb 3 2026; onsemi MoU Dec 2 2025 | Geopolitical/export-control risk partially de-risked by Google + onsemi commercial relationships |
| **ROHM** | 6963.T | ~5% / ~5% | ~3% / ~25x | NVIDIA silicon list; co-published 800VDC technical white paper at OCP Oct 20 2025; SiC trench MOSFET differentiation strong | Earnings weighed by SiC EV softness |
| **STMicroelectronics** | STM | ~8% / ~12% | ~10% / ~16x | NVIDIA silicon list; new 12V and 6V on-rack architectures announced at GTC March 2026; Sanan JV + Catania mega-fab | Consensus-bearish on SiC EV slump; 800VDC datacenter is optionality |
| **Wolfspeed** | WOLF | ~20% / n/m | n/m / n/m | Emerged Ch.11 Sept 29 2025. 33.7% SiC substrate share. CPM3-10000-0300A 10 kV SiC MOSFET commercial March 5 2026 (industry first). Q1 FY26: $197M rev, $926M cash, ~70% debt reduction. AI datacenter revenue +50% sequential | Post-emergence dilution + execution risk dominates next 12 months |
| **Coherent** | COHR | ~40% / ~50% | ~8% / ~25x | SiC substrate franchise (75% Coherent / 12.5% Denso / 12.5% Mitsubishi). 300mm SiC platform announced Dec 3 2025; 10 kV thick-epi April 9 2026 | Stopped disclosing SiC revenue separately after July 2025 segment changes |
| **Mitsubishi Electric** | 6503.T | ~5% / ~8% | ~10% / ~13x | 3.3 kV SiC MOSFET volume leader (Unifull, FMF800DC-66BEW); Kumamoto SiC fab Oct 2025; 12.5% Coherent SiC stakeholder | Most vertically-integrated SST player |
| **Navitas** | NVTS | ~40% / ~60% | n/m / n/m | NVIDIA 800V HVDC collaborator May 21 2025; demonstrated 800V→6V PDB + 250 kW SST. Q1 FY26: $8.6M rev (+18% seq, -38.6% YoY), $221M cash, no debt; AI infra +50% seq | Stock +868% TTM into Q1 print, mcap $4.49B; multiple already aggressive |
| **MPS** | MPWR | ~35% / ~45% | ~22% / ~50x | Replaced Vicor in H100 socket; primary VPD supplier for Blackwell; on-track for Vera Rubin late-2026 | ~$78B mcap; lateral architecture works under ~1,500A but physics-gated above 2,000A. Direct competitor to [[Theses/VICR - Vicor Corporation]] |
| **Power Integrations** | POWI | ~8% / ~10% | ~12% / ~25x | Gate drivers + AC-DC controllers | Cited in NVIDIA silicon list |
| **EPC** | private | n/a | n/a | GaN power devices | NVIDIA silicon list |
| **Analog Devices** | ADI | ~18% / ~23% | ~13% / ~25x | High-performance analog; some μModule franchise | Lateral multiphase; limited HPC density |
| **Renesas** | 6723.T | ~5% / ~8% | ~10% / ~15x | Power MCU + analog | NVIDIA silicon list |
| **Texas Instruments** | TXN | ~10% / ~15% | ~22% / ~25x | Diversified PMIC | NVIDIA silicon list; broad portfolio |
| **Richtek** | (under MediaTek 2454.TW) | ~25% / ~30% (MTK consolidated) | ~22% / ~14x | Power management ICs | NVIDIA silicon list |

### Layer 5 — Last 1.5 mm / on-board Vertical Power Delivery

| Name | Ticker | AI-DC Rev / OP | ROIC / EV/EBIT (LTM) | Exposure |
|---|---|---|---|---|
| **Vicor** | VICR | ~60% / ~70% | ~10% / ~50x | [[Theses/VICR - Vicor Corporation]]. 2nd-gen VPD: 3 A/mm², 40× current multiplication, 1.5 mm thickness. Only commercial vendor at this spec. Q1 FY26 $113M (+20% YoY), book-to-bill >2x. Compal Rubin NVL8 GTC March 2026 demo confirmed VPD architecture-fit. ITC LEO licensing engine on top |
| **Flex (own VPD)** | FLEX | ~25% / ~30% (Cloud segment) | ~15% / ~12x | Announced VPD product line 2025 — only other vertical-architecture vendor; manufacturing-led not IP-led |
| **Murata (VPD module)** | 6981.T | ~28% / ~33% | ~10% / ~14x | [[Theses/6981 - Murata Manufacturing]]. Begins VPD power-module mass production 2026 with cloud-provider engagement; ¥50B revenue target cumulative through FY27 |

### Layer 6 — Passives, magnetics, substrates, tools (the under-priced oligopolies)

| Name | Ticker | AI-DC Rev / OP | ROIC / EV/EBIT (LTM) | Exposure |
|---|---|---|---|---|
| **Murata** | 6981.T | ~28% / ~33% | ~10% / ~14x | [[Theses/6981 - Murata Manufacturing]]. High-cap MLCC ~33% global share. 15–35% price hike effective April 1, 2026 (TrendForce/Liberty Times). FY30 AI-server MLCC demand 3.3× FY25. GB300 server uses ~30,000 MLCCs; rack ~450,000 |
| **Samsung Electro-Mechanics** | 009150.KS | ~18% / ~23% | ~12% / ~12x | MLCC oligopoly. Signaling 5–10% price hikes |
| **TDK** | 6762.T | ~12% / ~17% | ~10% / ~12x | MLCC + film/DC-link capacitors. Strategic in Amperesand (TDK Ventures) |
| **Taiyo Yuden** | 6976.T | ~15% / ~20% | ~8% / ~12x | MLCC. +6–13% price hike May 2026 |
| **Disco** | 6146.T | ~30% / ~35% | ~54% / ~30x | >70% wafer dicing share. Every SiC fab installs Disco tools. ROIC 54% FY25; debt-free; FY24 revenue ¥393.3B (+27.9% YoY). P/E ~38–40, premium justified by structural moat |
| **Proterial (ex-Hitachi Metals)** | 5563.T | ~10% / ~15% | ~5% / ~10x | Nanocrystalline magnetic cores (FINEMET). ~45% global share. *The single biggest physical bottleneck for SST scaling at MW.* In-market since 1988 |
| **Qingdao Yunlu** | 688190.SS | ~18% / ~22% | ~15% / ~25x | ~16% nanocrystalline share; #1 amorphous globally (~55%). FY24 rev RMB 1.90B (+7.24%), NI RMB 361M (+8.73%). China A-share proxy at lower multiples than Proterial |
| **AT&M** | 000969.SZ | ~10% / ~15% | ~8% / ~25x | ~14% nanocrystalline share; primarily State Grid |
| **Vacuumschmelze (VAC)** | private (Apollo) | n/a | n/a | ~12% nanocrystalline share (VITROPERM). Not directly investable; reason public SST products are 12–24 months out |
| **Aixtron** | AIXA.DE | ~35% / ~45% | ~12% / ~20x | [[Theses/AIXA - Aixtron]]. MOCVD reactor duopoly with Veeco — gates GaN epi capacity |
| **Veeco** | VECO | ~30% / ~35% | ~10% / ~15x | MOCVD duopoly partner |
| **LEM Holding** | LEHN.SW | ~10% / ~15% | ~20% / ~18x | Hall-effect / Rogowski current and voltage sensors. Datacenter tailwind beginning post China EV / renewables pricing pressure |

## Affected vault theses and sector notes

### Direct exposure (existing vault theses)

| Vault entity | Direction of 800VDC impact | Conviction sensitivity |
|---|---|---|
| [[Theses/VICR - Vicor Corporation]] | Structurally positive: 800VDC → 48V → core-voltage chain creates more conversion content per system, not less. The 800V→6V single-step debate is the only architectural challenge; even if it materializes, I²R penalty at 6V vs 48V (~64× wiring loss) likely keeps 48V on-board. Rubin Ultra forces vertical PDN above 2,000A | Currently **medium** — 800VDC adoption pace is one of the strongest near-term positive triggers; Federal Circuit LEO scope is the offsetting risk |
| [[Theses/VRT - Vertiv Holdings]] | Direct: 800VDC portfolio launch H2 2026 is the company's central product roadmap. ~24 SST pilots not Vertiv-owned (those are Eaton); but Vertiv has rectifier + DC busway + rack-level DC/DC + DC BBU + service moat | Conviction sensitivity: any product slip beyond H2 2026 cuts FY27 earnings expectations 15–20% |
| [[Theses/NVDA - Nvidia]] | NVIDIA is the *cause*, not the *exposure* — chip roadmap drives 800VDC adoption curve. Indirect benefit: vertically-integrated reference architecture deepens NVIDIA's ecosystem control over hyperscaler estate (vs. Mt. Diablo's accelerator-agnostic design) | Adoption-curve risk is downside to Rubin Ultra revenue ramp, not core demand |
| [[Theses/6981 - Murata Manufacturing]] | High-cap MLCC oligopoly + VPD module entry (2026 mass production, ¥50B cumulative FY27). 800VDC → multi-conversion stages → more MLCCs per rack | Conviction-positive; April 2026 price hike already priced |
| [[Theses/AIXA - Aixtron]] | MOCVD reactor duopoly (with Veeco) gates SiC/GaN epi capacity. 800VDC ramp → SiC/GaN fab capex → Aixtron tool orders | Conviction-positive; structural |

### Adjacent exposure (theses that touch the chain)

| Vault entity | Connection |
|---|---|
| [[Theses/AVGO - Broadcom]] | Custom ASIC programs (XPUs at hyperscalers) — incremental high-current power delivery demand parallel to NVIDIA GPUs |
| [[Theses/AMD - Advanced Micro Devices]] | Helios MI455X H2 2026 — explicitly *sidesteps* 800VDC by going double-wide. MI500 (2027) must compete at Kyber-equivalent density |
| [[Theses/TSM - Taiwan Semiconductor]] | Foundry for NVIDIA Rubin/Rubin Ultra. Power-delivery thermal envelope decisions affect CoWoS substrate design |
| [[Theses/AMAT - Applied Materials]], [[Theses/LRCX - Lam Research]], [[Theses/ASMI - ASM International]], [[Theses/KLA - KLA Corporation]] | Semi capex tools — every SiC fab adds tool orders. Indirect but real |
| [[Theses/BESI - BE Semiconductor Industries]] | Hybrid bonders for advanced packaging (CoWoS, 3D stacking) — power-density requirements drive new packaging tools |
| [[Theses/INTC - Intel]] | Intel Foundry / CPUs are downstream consumers of any power architecture; lower direct exposure |

### Sector notes that incorporate the framework

- [[Sectors/Data Center Power & Cooling]] — primary MoC. The 800VDC question (existing §Macro shifts list) is the central framework; this Macro & Technology note is its detailed source.
- [[Sectors/Modular Power Conversion Components]] — chip-level layer (Layer 5 above). The 800V→6V architectural debate referenced in this sector's key industry questions is partially addressed by this note's bottleneck cascade analysis.
- [[Sectors/MLCC & Power Semiconductors]] — Layers 4 + 6 (wide-bandgap + passives). Murata thesis is the cleanest sector pure-play.
- [[Sectors/Compute & AI Compute Accelerators]] — NVIDIA / AMD chip roadmap as the demand driver setting 800VDC adoption pace.
- [[Sectors/Semiconductor Capital Equipment]] / [[Sectors/Semiconductor Foundries]] — upstream SiC/GaN fab buildout.

## Trade implications and portfolio positioning

The reports converge on a similar structural picture but diverge on emphasis. Synthesised positioning framework:

**Tier 1 — Highest-conviction, lowest valuation risk (multi-year backlog visibility, tariff-protected, oligopoly):**

- **Korean transformer trio basket** — HD Hyundai Electric (267260.KS) + Hyosung Heavy (298040.KS) + LS Electric (010120.KS). Combined Q1 2026 backlog ₩32T+. US-local production (Memphis, Alabama) tariff-protected. Order books extend through 2031. Wood Mackenzie's "deficit narrows by 2030" is the bear case but lead times are 128+ weeks today.
- **Eaton (ETN)** — 228 GW backlog, +240% YoY datacenter orders, Beam Rubin DSX co-design, ~24 SST pilots, Resilient Power IP, Boyd Thermal liquid-cooling acquisition. The cleanest, fastest-compounding, most-defensible name across both architectures.

**Tier 2 — Direct 800VDC pure-plays (catalyst-rich, valuation already partial):**

- **Vertiv (VRT)** — H2 2026 portfolio launch, +252% Q4 2025 organic orders, FSE service moat, NVIDIA reference partner. Risk: valuation reflects most of the AI-power thesis.
- **Delta Electronics (2308.TW)** — OCP 800VDC whitepaper author, ~60–65% HVDC share, per-server revenue $43,800 (GB200) → $171,000 (Rubin Ultra). Most asymmetric upside on revenue-per-server math.
- **Schneider (SU.PA)** — Co-design with NVIDIA, EU AI Continent anchor.

**Tier 3 — Oligopoly bottlenecks (under-priced, physical scarcity):**

- **Disco (6146.T)** — >70% SiC dicing/grinding. Picks-and-shovels on every SiC fab built. P/E ~38–40 premium justified.
- **Murata (6981.T)** — [[Theses/6981 - Murata Manufacturing]]. 33% MLCC share + April 2026 price hike + VPD module entry. Already a vault thesis.
- **Proterial (5563.T)** — Nanocrystalline FINEMET cores at ~45% global share. *The single biggest physical bottleneck for SST scaling.* Low-multiple Japanese small-cap.

**Tier 4 — Vertical Power Delivery on-board (existing vault thesis, structurally positive):**

- **Vicor (VICR)** — [[Theses/VICR - Vicor Corporation]]. 2nd-gen VPD spec + ITC LEO licensing. Conviction medium currently; 800VDC adoption pace is a strong-positive trigger that could push to high if (a) NVIDIA Rubin Ultra confirms Vicor socket content and (b) Federal Circuit LEO survives intact.

**Tier 5 — Wide-bandgap semis (paired, sized smaller):**

- **Infineon (IFX)** + **onsemi (ON)** for broad SiC/GaN merchant exposure.
- **Innoscience (2577.HK)** for higher-beta Chinese GaN with Google + onsemi de-risk.
- **Coherent (COHR)** for 200/300mm SiC substrate + broader datacomms ramp.
- **Navitas (NVTS)** as high-beta sleeve only — stock +868% TTM into Q1 FY26 print at $4.49B mcap already prices aggressive design-win expectations.
- **Wolfspeed (WOLF)** as post-emergence turnaround sleeve only — execution risk dominates next 12 months.

**Tier 6 — Equipment / tools (indirect):**

- **Aixtron (AIXA)** — [[Theses/AIXA - Aixtron]]. MOCVD duopoly gates SiC/GaN epi.
- **Veeco (VECO)** — MOCVD duopoly partner.

**Strategic losers / shrinking pools:**
- Legacy AC PDU and AC-mode UPS-only vendors (no Rubin-class capability).
- Low-voltage copper cable suppliers (45% copper reduction is a real volume headwind even with dollar TAM growth).
- Silicon MOSFET/IGBT vendors not transitioning to wide-bandgap.

**Triggers that would change the framework:**

| Trigger | Impact |
|---|---|
| Rubin Ultra slips from 2027 to 2028+ | Compresses immediate 800VDC ramp; reduce wide-bandgap + Vertiv exposure; Korean transformer trio + Eaton thesis intact (AC grid demand independent) |
| Hyperscalers move to in-house custom power modules at scale | Largest risk to MPS, Vicor, Navitas |
| SiC substrate price war from Chinese over-capacity (San'an, Hua Hong, TankeBlue, SICC) | Compresses Wolfspeed/Coherent unit economics; structurally bullish for Disco (tool sales independent of substrate ASP) |
| China export-control escalation | Most negative for Innoscience; net positive for ex-China (Infineon, Navitas, Wolfspeed, Coherent, onsemi) |
| Major Vertiv/Schneider/Delta/Eaton 800VDC product slip >2 quarters past H2 2026 | De-risk supplier earnings expectations by 15–20% |
| AMD MI500 competitive on non-800VDC architecture | Undermines NVIDIA density-forcing thesis; slows Mt. Diablo + NVIDIA alike |
| Serious DC arc-flash safety incident at any 800VDC deployment | Multi-quarter regulatory pause; UL/IEC moratorium risk |
| Korean tariff escalation on transformers | Thesis insulated by US-local Memphis/Alabama production |

## Caveats and open questions

1. **NVIDIA's economics claims (5% efficiency, 70% maintenance reduction, 30% TCO) are NVIDIA's own marketing.** Not independently audited; assume ideal greenfield. Real-world figures lower. The 45% copper reduction is the most physically defensible claim.

2. **The "20+ customers designing for 800VDC" framing flows entirely through NVIDIA's October 2025 blog.** No first-party 800VDC commitments from Lambda, Nebius, OCI, or Together AI as of May 2026. CoreWeave's commitment is to Rubin specifically, not to 800VDC. Treat the neocloud commitment list as soft.

3. **Vertiv/Schneider/Delta/Eaton 800VDC products are in design and qualification, not in volume production.** Slip risk between announcement and GA is non-trivial; H2 2026 dates should be treated as targets, not commitments.

4. **Sell-side has not published architecture-segmented adoption forecasts.** Goldman, Morgan Stanley, Bernstein quantify aggregate datacenter GW demand but do not split AC vs DC. Dell'Oro's high-density-power research is paywalled. The MarketsandMarkets US-specific SST datacenter projection ($40.3M → $154M at 30.8% CAGR by 2030) is one of the cleanest narrow-segment forecasts but is the SST slice, not whole-stack 800VDC.

5. **The Mt. Diablo vs NVIDIA architecture split is genuinely contested.** Hyperscalers will likely operate both in parallel rather than choose; good for total supplier TAM, bad for any single-architecture bet.

6. **Liquid cooling adoption is a prerequisite gate.** Uptime Institute 2024: 22% of operators using DLC, <10% of racks in those facilities. SemiAnalysis: AI training near 100% DLC, enterprise far behind. If DLC penetration disappoints, 800VDC follows.

7. **Foxconn Kaohsiung-1 at 40 MW is the only widely-cited operational 800VDC datacenter as of early 2026.** Any general statement about "deployed reality" of 800VDC is essentially a statement about *one facility*. Field reliability data is too thin to support actuarial confidence.

8. **General-purpose enterprise datacenters will not transition.** Economics do not pencil at 10–20 kW/rack. 800VDC is overwhelmingly an AI-factory phenomenon; forecasts that blend will systematically overstate.

9. **Custom-ASIC programs (Google TPU, AWS Trainium, Microsoft Maia, Meta MTIA) are largely *not* on 800VDC today.** They will move on different timelines and to different voltage targets. Equity narratives that assume all hyperscaler AI is "going 800VDC" are oversimplified.

10. **NEC, UL, and IEC standards lag the deployment timeline.** A serious arc-flash incident in the next 24–36 months is plausible and could trigger regulatory pause similar to early lithium-ion battery facility incidents. Single biggest non-supply-chain downside risk.

11. **The 800V→6V single-step distribution debate** is unresolved. If adopted (some industry research circulates this option), it bypasses the 48V on-board tier where Vicor's VPD lives — but I²R penalty at 6V vs 48V (~64× wiring loss at same wattage) likely makes 48V on-board the persistent endpoint even with 800V upstream. Worth monitoring at the OCP and NVIDIA spec releases through 2027.

## Open Questions

- **Will NVIDIA Rubin NVL144 in H2 2026 actually ship on 800VDC, or stay on 480VAC/54V** as the Schneider reference design suggests, pushing the architectural inflection to Rubin Ultra Kyber in 2027? This is the single most decisive timing question for the entire chain.

- **Which neocloud first signs a first-party 800VDC commitment**? CoreWeave's Rubin commitment is the closest; Lambda / Nebius / OCI / Together AI are NVIDIA-attributed only. First non-NVIDIA-attribution press release is a strong validation signal.

- **What is the Mt. Diablo 1.0 final connector and protection spec**, and does it converge with NVIDIA's reference at GTC 2027? Standardization risk currently bounded but real; convergence is a strong-bull signal.

- **Will any major insurance carrier publish 800VDC actuarial guidance before 2028**? Foxconn Kaohsiung-1 is one facility; reliability data is too thin for confidence pricing.

- **VAC (Vacuumschmelze) nanocrystalline capacity expansion** — the single biggest physical bottleneck for SST scaling at MW, and private to Apollo. Not directly investable; should be tracked via Proterial (5563.T) capacity disclosures and any VAC capex announcements through Apollo's portfolio reporting.

- **Hyperscaler-specific 800VDC adoption commitments** (Microsoft, Meta, Google, Amazon, Oracle) at first-party press detail level — material to the slope of the ramp. AWS specifically is the laggard worth monitoring for capitulation.

## Related Research

- Source A: [[_Inbox/processed/compass_artifact_wf-60b03808-306c-48ca-9868-6ea5b811bd10_text_markdown]] — Institutional equity research note on 800VDC adoption with detailed forecast scenarios (base/bull/bear) and inflection points
- Source B: [[_Inbox/processed/compass_artifact_wf-673fe644-ff19-4677-a601-26f9af21d15e_text_markdown]] — Grid-to-rack equity map (FY26–FY30) with deep coverage of Korean transformer trio, MLCC oligopoly, Disco, nanocrystalline cores
- Source C: [[_Inbox/processed/compass_artifact_wf-f16530a3-3670-4658-b53b-01b9a07ffdba_text_markdown]] — Solid-state transformer bottleneck map with MV SiC module concentration analysis, M&A target identification, China SST landscape
- Related: [[Research/2026-04-28 - VICR - Vertical Power Delivery Technical Architecture and Q1 2026 Earnings - deep-dive]] — chip-level on-board layer (the "last 1.5 mm" of the 800VDC chain)
- Related: [[Macro & Technology/CXL Memory Disaggregation Framework]] — parallel architectural-primitive macro for AI infrastructure
- Related: [[AI Bubble Risk and Semiconductor Valuations]] — risk context for the whole AI capex cycle that 800VDC monetizes
- [[Research/2026-05-24 - Retrospective 1w - Synthesis]] — Mid-cycle rotation: structural-long capex floor reaffirmed (NVDA $1T Blackwell+Rubin visibility 2025-2027 + CreditSights $750B 2026 hyperscaler capex) keeps 800VDC adoption trajectory on the base-case 10-15% 2027 → 65-75% 2032 curve; no contradiction with existing adoption gates (liquid cooling, SST/nanocrystalline supply, DC standards)

## Log

### 2026-05-18
- Initial macro note created from synthesis of three May 2026 Claude Deep Research reports + web search for May 2026 supplementation (NVIDIA GTC March 2026 announcements, Mt. Diablo v0.7.0, Amperesand $80M Series A, Enphase IQ SST, Korean trio order book through 2031, Vertiv H2 2026 readiness statement). Conviction frame: structural positive for [[Theses/VICR - Vicor Corporation]] (2nd-gen VPD is the only commercial vendor at 3 A/mm² + 40× + 1.5 mm spec), [[Theses/VRT - Vertiv Holdings]] (H2 2026 800VDC portfolio is central roadmap), [[Theses/6981 - Murata Manufacturing]] (high-cap MLCC oligopoly + April 2026 price hike + VPD module entry), [[Theses/AIXA - Aixtron]] (MOCVD duopoly gates SiC/GaN epi). Adoption gates: liquid cooling penetration (primary), SST/nanocrystalline core supply (secondary), DC standards (UL/IEC/NEC still maturing), operator training. Base case: 10–15% of new AI-rack capacity 2027, 65–75% by 2032; enterprise stays <10% on 800VDC through 2030 in all scenarios. Three new monitoring candidates not currently in vault: Korean transformer trio (HD Hyundai 267260.KS, Hyosung 298040.KS, LS Electric 010120.KS), Eaton (ETN), Disco (6146.T) — flagged for thesis-evaluation candidacy if AI-power positioning becomes a vault priority. Next sync should propagate to VICR thesis (architectural-necessity reinforcement), VRT thesis (Vertiv H2 2026 product readiness + service moat numbers), NVDA thesis (Rubin/Rubin Ultra power roadmap), Murata thesis (MLCC + VPD module entry), and the three sector notes (Data Center Power & Cooling, Modular Power Conversion Components, MLCC & Power Semiconductors).
- Manual edit: added two financial columns (AI-DC Rev / OP exposure %, ROIC / EV/EBIT LTM) to all six Layer tables in §Value chain map and named beneficiaries; figures are directional May 2026 synthesized estimates (most names do not disclose AI-DC segment economics) and should be verified before sizing. Cross-tier scan from the new data: Tier-1 names (Korean trio, Eaton) hold the best ROIC/EV-EBIT pairs at the highest AI-DC exposure; Vertiv (~65% / ~75% AI-DC, ~25% ROIC / ~28x) and Disco (~30% / ~35% AI-DC, ~54% ROIC / ~30x) screen as the highest-quality concentrated exposures; MPS (~35% / ~45% AI-DC, ~50x) and Vicor (~60% / ~70% AI-DC, ~50x) carry the richest multiples in Layers 4–5; Wolfspeed/Navitas/Innoscience are n/m on ROIC despite high AI-DC mix — beta sleeves, not core. Conviction impact: unchanged for existing vault theses; reinforces relative attractiveness of Disco + Korean trio as monitoring candidates flagged in initial entry.

### 2026-05-24 (/sync all)
- [[Research/2026-05-24 - Retrospective 1w - Synthesis]]: Mid-cycle rotation retrospective frames structural-long capex floor as reaffirmed through 2027 — NVDA Q1 FY2027 print ($1T Blackwell+Rubin visibility 2025-2027, $82B Q1 +85% YoY, $91B Q2 guide, "AI is now a necessity" Jevons reframe) + CreditSights $750B 2026 hyperscaler capex print (+67% YoY) are the two highest-credibility datapoints anchoring AI-rack demand through the 800VDC adoption window. Net for adoption forecast: base-case **10-15% of new AI racks 2027 → 65-75% by 2032** trajectory holds — capex floor anchors Vertiv H2 2026 portfolio readiness, Murata MLCC + VPD module entry, Vicor 2nd-gen VPD architectural-necessity framing, and Aixtron MOCVD duopoly for SiC/GaN epi-tools. No contradiction with existing adoption gates (liquid cooling penetration as primary bottleneck, SST/nanocrystalline core supply as secondary, DC standards UL/IEC/NEC maturation, operator training). Three monitoring candidates flagged in initial entry (Korean transformer trio, Eaton, Disco) gain incremental support from the broader retrospective's "no contradiction with existing structural longs" frame. Conviction unchanged for [[Theses/VICR - Vicor Corporation]] / [[Theses/VRT - Vertiv Holdings]] / [[Theses/6981 - Murata Manufacturing]] / [[Theses/AIXA - Aixtron]] at the macro-link level.
