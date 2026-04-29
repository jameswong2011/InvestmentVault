---
date: 2026-04-23
tags: [research, meta, surface-scan]
status: active
source: vault synthesis
source_type: synthesis
scope: default
propagated_to: []
---

# Insight Surface Scan — 2026-04-23

Vault state at scan: 43 theses, 36 sector notes, 6 macro notes, 134 research notes, 397 edges, 15 orphan research notes.

## 1. Portfolio Blind Spots

### 1.1 Memory / HBM oligopoly — no direct thesis on the 3 suppliers the vault depends on

The vault has 4 theses directly exposed to HBM4 ramp (NVDA, AMD, AVGO, PSTG) plus 5 more indirect (BESI, SEMICAP, SNDK, 285A, LITE). **No thesis on SK Hynix, Samsung, or Micron** — the three suppliers who collectively own 100% of HBM output.

| Supplier | HBM share (2026) | Vault exposure | Thesis coverage |
|---|---|---|---|
| SK Hynix | ~60% | NVDA Rubin HBM4, BESI Kinex order | None — mentioned in 11 research notes |
| Samsung | ~20% (rising toward 30%) | NVDA HBM4 supply; V10 NAND uses YMTC IP | None — mentioned in 14 research notes |
| Micron | ~21% (overtook Samsung) | NVDA HBM4; AMD MI350 preferred supplier; PCIe 6.0 NAND first-mover | None — mentioned in 9 research notes |

SK Hynix and Micron have been mentioned across 20+ research notes in the vault but appear in zero thesis notes. The Kioxia thesis acknowledges "SK Hynix strategic risk: Convertible bond holder with potential misaligned interests" — but the counterparty is not independently analysed. This is the single clearest implied-but-unwritten thesis in the vault.

**Supply-chain concentration cost**: Every dollar of NVDA Rubin / AMD MI450 / Huawei 950PR depends on HBM4 yield at one of these three. Samsung's 2026 50% capacity surge + Micron's HBM4 sold-out positioning + SK Hynix in-house advancement create a tradeable cycle the vault has no exposure to.

### 1.2 Custom ASIC design services — Broadcom alone, Marvell absent

AVGO thesis captures 55-60% custom ASIC share. Marvell is projected at ~25% share (AWS Trainium 2 lead, partial Trainium 3, Microsoft Maia DPU, Meta DPU, Google inference chip talks per April 2026 disclosure). **Marvell appears in NVDA, LITE, AMD, AVGO research notes** as a competitive / supply chain entity but has no thesis.

Jensen's April 2026 disclosure ("ASIC margins ~65% vs Nvidia ~70%") quantifies that hyperscaler in-sourcing transfers margin from NVDA to Broadcom/Marvell — it does not eliminate silicon-vendor rent. Exposure to this transfer via AVGO is captured; via MRVL is not.

### 1.3 Defense primes — the implied Taiwan + Iran hedge the vault doesn't hold

TSM stress test flagged LMT/RTX/NOC as the market-implied Taiwan hedge (Pelosi 2022 precedent: LMT+RTX+NOC +4-8% while TSM -6% in 72hr). Iran macros recommend RTX, LMT, NOC, AVAV, KTOS as war-trade exposures.

The vault has:
- 5 Iran-direct theses (CCJ, LNG, STNG, RELIANCE, plus PANW as Iranian cyber derivative)
- 0 defense primes despite defense being recommended across 4 macro documents

[[Research/2025-05-10 - Macro - Indian vs Pakistani Defence Stocks]] is orphan — not linked to any thesis despite defense sector signal. This is a discipline gap: the vault models geopolitical risk via oil/uranium/shipping but not via direct defense exposure.

### 1.4 Quantum computing — asymmetric TAM, only captured as risk

BTC-CRYPTO thesis contains quantum as threat vector (BIP 360, post-quantum transition, 3-5yr window). No upside thesis on quantum hardware (IONQ, RGTI, IBM quantum, Alphabet Willow). Quantum compute would also serve as hedge against:
- NVDA GPU commoditization if quantum crosses functional threshold
- BTC security risk (negative-correlated position)
- AI efficiency overshoot (quantum > classical for specific workloads)

### 1.5 Advanced packaging upstream — no OSAT thesis despite CoWoS being the core bottleneck

Multiple theses cite "CoWoS capacity is the single tightest node in the AI stack" (NVDA, AMD, AVGO, BESI, SEMICAP, TSM). TSMC outsources 240-270K wafers annually to Amkor (180-190K) and SPIL (60-80K). **AMKR and SPIL not covered**. Advanced packaging equipment is covered (BESI); capacity is not.

### 1.6 Japanese semi equipment — Tokyo Electron discount ignored

The SEMICAP thesis explicitly identifies TEL as "structural mispricing due to the 'Japan discount' — a 92% coater/developer monopoly essential to every EUV-equipped fab on Earth, trading at lower multiples than Western peers." Cryogenic etch enters HVM 2026 for 400L NAND ($500M → $2B TAM by 2027). This is flagged but no dedicated thesis exists.

## 2. Supply Chain Mapping — hidden correlations

### 2.1 Memory/NAND cluster × AI-semis cluster overlap

The _graph.md shows two separate clusters:
- **Memory/NAND**: 285A, SNDK (2 members)
- **AI/Semis Ecosystem**: AVGO, BESI, LITE, NVDA, PSTG, SEMICAP (6 members)

Cross-linkages reveal these are not independent:
- PSTG sits in both (NAND cost exposure + AI storage TAM)
- SEMICAP sits in both (NAND equipment spend + HBM scaling)
- 285A and SNDK share Flash Ventures JV (hidden 50/50 cost correlation via Kioxia)

Single event that would hit multiple theses simultaneously:

| Event | Primary theses hit | Secondary theses hit | Total exposure |
|---|---|---|---|
| TSMC Taiwan disruption | TSM (already low), NVDA, AMD, AVGO, BESI | SEMICAP, LITE, VRT, META, PSTG | 10 theses |
| HBM4 yield failure | NVDA, AMD, BESI, SEMICAP | AVGO, PSTG, SNDK, META | 8 theses |
| NAND price reset to 2023 levels | SNDK, 285A, PSTG | SEMICAP, NVDA (compute demand), META | 6 theses |
| AI bubble correction (20-30% capex cut) | NVDA, AMD, AVGO, BESI, LITE, VRT | META, PLTR, NOW, PSTG, PANW, CRWD, SEMICAP | 13 theses |
| Hormuz reopens cleanly | STNG, LNG | CCJ, RELIANCE | 4 theses |
| SK Hynix-led HBM oversupply | NVDA (margin), 285A, SNDK | BESI, PSTG | 5 theses |

**The AI bubble scenario hits 13 of 43 theses simultaneously (30% of portfolio).** Macro/AI Bubble Risk note currently enumerates 11 related theses in text but does not construct a quantified portfolio VaR.

### 2.2 The PSTG double-hit

PSTG is the only thesis in both the Memory/NAND cluster (via NAND cost input) and AI/Semis cluster (via AI storage demand). A scenario where NAND prices surge (enterprise SSD COGS up) AND AI capex moderates (AI storage demand down) compresses PSTG from both sides. The thesis acknowledges NAND cost risk at +55-60% QoQ but does not model the joint compression.

### 2.3 Broadcom as platform tax — not a thesis risk, a portfolio asset

AVGO XPU customers include Google (TPU), Meta (MTIA), OpenAI, Anthropic, ByteDance — 5 confirmed. Every hyperscaler custom-ASIC program flows through AVGO. This means AVGO benefits in every single scenario where hyperscaler ASICs gain share from NVDA — including the NVDA bear case. AVGO is a structural hedge for the NVDA position within the same portfolio, and the vault holds both at high conviction (AVGO) and medium (NVDA).

## 3. Macro Exposure Audit

### 3.1 Taiwan Strait — macro note gap is material

Per _hot.md Q9 and NVDA/AVGO/BESI/SEMICAP/TSM log entries (2026-04-19 stress test sync), the vault has zero dedicated Macro analysis on Taiwan invasion/blockade despite:
- TSM already downgraded MEDIUM → LOW on this risk
- NVDA/AVGO/BESI/SEMICAP cross-thesis Taiwan exposure already propagated
- TSM stress test quantified -85-95% permanent impairment downside
- "Destroy the fabs" US contingency publicly disclosed (Bloomberg Mar 2023)

Iran has 3 dedicated macro notes. Taiwan has 0. This is the single highest-priority macro gap in the vault. A dedicated `Macro/Taiwan Strait Geopolitical Risk.md` note would anchor cross-sector analysis the way Iran Macros anchor STNG/LNG/CCJ/RELIANCE.

### 3.2 Macro/VIX Index is orphan — no thesis links

The VIX macro note has zero theses in the reverse index per _graph.md. It describes VIX mechanics generically (contango decay, settlement, term structure) without any portfolio application. Either (a) candidate for archival, or (b) should be rewritten as "Portfolio VIX Hedging Framework" tied to AI bubble + Iran + Taiwan scenarios.

### 3.3 AI Bubble Risk macro is under-connected relative to scale

The macro note has 11 linked theses but 13+ are empirically exposed (see 2.1). Missing from its reverse index: CRWD (cybersec as AI capex derivative — flagged in cybersec sector note but not in the macro's reverse index), NET (edge AI infra), VRT (AI data center), IOT (physical AI / Samsara).

### 3.4 Iran theses are concentrated and may already be priced out

CCJ (high), LNG (high), STNG (medium), RELIANCE (medium), plus PANW as derivative — 5 positions all long the same scenario. April 8 ceasefire collapsed April 12 per STNG log; if resolution occurs, 4 theses compress simultaneously. The portfolio lacks an explicit Iran-resolution hedge. The sector spread (uranium + LNG + shipping + cybersec + Indian conglomerate) provides some scenario hedging but not diplomatic-resolution hedging.

### 3.5 Stablecoin / Crypto regulation macro connects only 2 theses

Stablecoin Regulation macro links BTC-CRYPTO and CRCL only. Vault has no COIN thesis despite COIN being the largest equity beneficiary of USDC adoption (USDC revenue-sharing, Base L2 settlement, x402 protocol developer).

## 4. Catalyst Calendar — clustered risk

### 4.1 Q1 2026 earnings cluster — April 21-May 14

Within 24 days, 16 of 43 theses (37%) report Q1 earnings:

| Date | Ticker | Key watch |
|---|---|---|
| Apr 21 | ISRG | dV5 margin recovery, procedure growth |
| Apr 22 | NOW | Now Assist $1B ACV progress, Armis timeline |
| Apr 23 | BESI | Order momentum post-SK Hynix Kinex, HB backlog |
| Apr 28 | CSGP | Homes.com traffic, EBITDA margin expansion |
| Apr 29 | META | Capex plateau signal, Advantage+ monetization |
| Apr 29 | SPOT | SAX programmatic ad growth, MLC lawsuit |
| Apr 30 | CCJ | Contract price, Westinghouse EBITDA |
| Apr 30 | SNDK | 65-67% GM execution, HBF milestones |
| May 1 | STNG | Q2 LR2 bookings at $101k/day, 16% fixed |
| May 6 | APP | SEC disclosure, e-commerce self-serve GA |
| May 6 | UBER | AV data business disclosure |
| May 6/7 | SHOP / LNG | Shopify AI-agent orders, Cheniere post-ceasefire |
| May 11 | HIMS / CRCL | DOJ commentary, Coinbase renegotiation |
| May 14 | 285A | Q4 FY2025, BiCS10 production start |
| Late May | NVDA / CRWD | Q1 FY2027, post-$5B ARR durability |

Clustering implications:
- **Single earnings miss week** (Apr 28 - May 6) hits 11 positions
- META and NVDA on same day (Apr 29) — if META capex signal disappoints, NVDA gets hit by proxy
- Memory theses (SNDK Apr 30, 285A May 14) book-end a single NAND pricing narrative — a late-April disappointment sets up early-May NAND cluster drawdown

### 4.2 Multi-thesis catalysts in 2026

| Catalyst | Theses affected | Timing |
|---|---|---|
| Anthropic-Google TPU ramp | NVDA, AVGO, TSM | H2 2026 |
| Meta 6GW AMD deployment start | AMD, META, AVGO, BESI | Q3 2026 |
| Vera Rubin cloud availability | NVDA, LITE, BESI, VRT, PSTG | H2 2026 |
| GTA VI launch | TTWO | Nov 19, 2026 |
| US midterms (Nov 3, 2026) | CRCL (CLARITY), DE (tariffs), CCJ (Westinghouse), BTC | H2 2026 |
| Jio IPO | RELIANCE | By Jul 2026 |
| Xi 2027 PLA readiness deadline | NVDA, AMD, AVGO, BESI, TSM, SEMICAP, LITE | 2027 tail |

The Xi 2027 deadline matters more than any single earnings cluster — it would trigger every Taiwan-exposed thesis simultaneously.

## 5. Contrarian Signal Detection — conviction vs consensus gaps

### 5.1 High-conviction, wide consensus gap positions

| Thesis | Conviction | Consensus | Delta | Why market wrong |
|---|---|---|---|---|
| WTC | medium | 100%+ implied upside (unanimous Strong Buy A$80-90 vs stock A$37) | 100% | Governance crisis priced as business impairment; business is accelerating (76% rev growth, E2open 18mo ahead) |
| CCJ | high | Cyclical commodity producer | Structural | Re-rating from commodity producer to fuel-cycle monopoly; Westinghouse recurring services undervalued |
| LNG | high | Temporary disruption (Brent Dec 2026 at $80) | Physical | Ras Laffan 3-5yr repair, insurance normalization lag multi-quarter, crude-LNG divergence |
| UBER | high | Mature utility at 21x fwd P/E | Platform | Completing operator-to-platform-tax-collector transition, $2B+ advertising business at pure margin |
| AVGO | high | 28x forward on 100%+ AI growth | Contractual | Hock Tan's $100B+ 2027 AI target has 5 confirmed XPU customers; Anthropic-Google 2031 lock-in |

### 5.2 Medium-conviction asymmetric setups

| Thesis | Conviction | Asymmetry driver |
|---|---|---|
| HIMS | medium | 46% short interest + 1.5x P/S + 4 binary catalysts (DOJ, peptide, Eucalyptus, Q1 earnings May 11) |
| SNDK | medium | HBF at $1/GB bridging $0.10/GB SSD and $8/GB HBM — TAM creation event not TAM capture |
| 285A | medium | Market fixates on layer count (218 vs 286/276/321); CBA at 29 Gb/mm² equivalent to 400+ layer competitors |
| EDEL | medium | SOTP at ₹11,500 crore vs ₹10,000 crore market cap — 4 value-crystallization events lined up |

### 5.3 Low-conviction with embedded call option

| Thesis | Conviction | Option structure |
|---|---|---|
| OPEN | low | $40M Rabois insider buy + warrant dividend structure + Jane Street +1,184% — asymmetric tail with insolvency 3-4yr removed |
| IQE | low | Stock rallied 4.7p → 52.5p (1,000%+) but EV/Revenue now at peer parity — M&A optionality largely priced in |
| MTN | low | Structural climate + public-vs-private ownership asymmetry — governance-trap no management can resolve |
| TSM | low | Downgraded Apr 19 on Taiwan tail — option on Taiwan de-escalation |

## 6. Research Freshness Audit — decay alerts

### 6.1 Theses with zero recent research (no new research notes in 45+ days)

| Thesis | Last new research | Conviction | Status |
|---|---|---|---|
| KAMBI | None linked in graph | medium | 2026 FIFA World Cup catalyst 5 weeks out |
| TTWO | None linked in graph | medium | GTA VI Nov 2026 — binary event |
| UBER | 2025-11-29 (on OPEN, not UBER) | high | No dedicated UBER research despite high conviction |
| DUOL | 2025-09-22 | medium | Guidance cut + 83% drawdown — needs stress test |
| OPEN | 2025-12-04 | low | ~$4.93 on retail momentum — needs update |
| MTN | 2025-12-15 | low | Rockies at 30-year-low snow — needs Q3 FY26 update |
| SPOT | 2026-04-15 | medium | Q1 earnings Apr 29 — needs pre-earnings check |
| NFLX | 2026-03-21 | medium | Q1 Apr 17, then WBD-Paramount close Q3 2026 |

**UBER is the most acute attention-allocation mismatch**: high conviction, no dedicated research note, catalyst Q1 earnings May 6.

### 6.2 Theses with heavy research velocity but no recent thesis update

| Thesis | Research velocity | Last thesis edit | Gap |
|---|---|---|---|
| NVDA | 15 research notes, 3 in April | 2026-04-23 (wikilink cleanup) | Active but last substantive edit Apr 19 |
| PSTG | Only 1 research note | 2026-04-15 | Single-note support for medium conviction on complex thesis |

PSTG is the opposite problem: complex platform-pivot thesis (Everpure rebrand, 1touch integration, VAST Data competition) supported by 1 research note. Research depth doesn't match thesis complexity.

## 7. Thesis Velocity & Attention Allocation

### 7.1 Research velocity ranking (by Research/ notes in _graph.md adjacency, April 2026)

| Rank | Thesis | Research notes | Conviction | Allocation signal |
|---|---|---|---|---|
| 1 | NVDA | 15 | medium | Aligned — complex story warranting depth |
| 2 | 285A / SNDK / BESI | 10-13 each | medium | Aligned — memory cycle intense |
| 4 | PLTR | 9 | medium | Aligned |
| 5 | NOW | 9 | medium | Aligned |
| 6 | BTC-CRYPTO | 12 | medium | Possibly over-allocated — medium conviction, deep research |
| 7 | PANW / CRWD / NET | 2-6 each | medium | Aligned |
| 8 | WTC | 4 | medium | Wide consensus gap warrants more |
| 9 | KAMBI / TTWO | 0 | medium | Under-allocated |
| 10 | UBER | 1 (on OPEN) | **high** | **Severely under-allocated** |
| 11 | CCJ / LNG | 5 each | **high** | Adequate |

### 7.2 Attention-conviction mismatches

**Under-researched high-conviction**:
- UBER (high, 1 indirect research note) — most severe
- EINK (high, 0 research notes) — only thesis mentions, no dedicated research
- SEMICAP (high, 7 research notes) — acceptable but thesis is a sector-level pick list covering 5 tickers

**Over-researched low-conviction**:
- IQE (low, 6 research notes) — M&A optionality largely priced in; research effort now marginal
- MTN (low, 1 research note) — proportionate
- TSM (low, 4 research notes) — proportionate given recent downgrade

### 7.3 Decay alerts (active thesis, zero log activity in 14+ days)

No thesis has been untouched for 14+ days — every thesis received at least a wikilink-cleanup log entry on 2026-04-22 via the sector-taxonomy reorg. Genuine content decay is masked by the systemic edit. Re-running this check after 30+ days would surface actual dormancy.

## 8. Opportunity Generation — 5 research prompts ranked by conviction impact

### Opportunity 1 — Create Macro/Taiwan Strait Geopolitical Risk note [HIGH impact]

**Topic**: Full macro analysis of Taiwan invasion/blockade scenarios, parallel to the 3 Iran macros.

**Why now**: Xi 2027 PLA readiness deadline is inside the AI capex thesis horizon. TSM already downgraded on this risk; NVDA/AVGO/BESI/SEMICAP log entries from Apr 19 stress test sync reference Taiwan tail but have no macro anchor. Q9 in _hot.md explicitly flags this gap.

**Vault connection**: Anchors [[Theses/TSM - Taiwan Semiconductor]], [[Theses/NVDA - Nvidia]], [[Theses/AVGO - Broadcom]], [[Theses/BESI - BE Semiconductor Industries]], [[Sectors/Semiconductor Capital Equipment]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/LITE - Lumentum]]. Creates the Iran-parallel macro thesis structure.

**Expected impact**: HIGH — conviction-level changes on 2+ theses. Enables formal portfolio VaR on Taiwan. Surfaces Joint Sword 2024 metrics, "destroy the fabs" contingency, silicon shield vs Ukraine/Nord Stream 2 precedent, Taiwan sovereign CDS, Japan METI protocol.

**Suggested approach**:
1. Web research on Joint Sword 2024/2025 PLA blockade rehearsal specifics
2. Declassified / public "destroy the fabs" protocol references (Bloomberg Mar 2023, O'Brien testimony)
3. Taiwan sovereign CDS historical movement during prior crises
4. Japan METI export-control leading indicators
5. Document cross-reference in every Taiwan-exposed thesis

### Opportunity 2 — Create HBM supplier thesis (SK Hynix, Samsung Memory, or Micron) [HIGH impact]

**Topic**: Pick one of the three HBM suppliers as the cleanest expression of HBM4 ramp.

**Why now**: Every AI-semis thesis in the vault (9+ theses) depends on HBM4 execution. Zero theses on the suppliers. Samsung HBM4 30%+ of Nvidia supply (up from 0), Micron HBM4 2026 sold out, SK Hynix H3 architecture demonstrated 2.69x perf/watt with HBF integration.

**Vault connection**: Completes the memory value chain — equipment (BESI, SEMICAP), NAND (285A, SNDK), NAND downstream (PSTG), enterprise/consumer SSD (SNDK), HBM (missing). SK Hynix specifically has direct cross-thesis implications via HBF co-development with SNDK.

**Expected impact**: HIGH — adds a memory-cycle-long position with structurally different economics (HBM margins 50%+ vs NAND 15-30%); potential natural hedge against NAND thesis downside (SNDK / 285A / PSTG).

**Suggested approach**:
1. Screen 3 candidates on: HBM-only exposure vs foundry/logic overhang, Taiwan concentration, capex discipline, customer concentration
2. Micron likely winner for US-listed clean HBM exposure
3. Map against existing AI-semis theses to identify optimal hedge/complement structure
4. Web research on HBM4 16-Hi yield curves per supplier
5. Build thesis emphasising Nvidia multi-sourcing (dilutes single-supplier premium but creates 3 duopoly beneficiaries)

### Opportunity 3 — Create defense prime thesis (RTX, LMT, or NOC) [MEDIUM-HIGH impact]

**Topic**: Single defense prime thesis as natural Taiwan + Iran hedge.

**Why now**: Both active macros (Iran direct; Taiwan pending) recommend defense primes. TSM stress test explicitly named LMT/RTX/NOC as market-implied hedge (Pelosi 2022: LMT+RTX+NOC +4-8% vs TSM -6% in 72hr). Vault has 5 Iran-direct theses and 0 defense primes.

**Vault connection**: Iran macros (3), Taiwan macro (pending). Portfolio-level hedge against correlated Iran and Taiwan tail. PLTR already connects to defense via Warp Speed / ShipOS but as software, not hardware.

**Expected impact**: MEDIUM-HIGH — not a non-consensus alpha trade (defense valuations already elevated), but a portfolio-construction fix for a systematic under-exposure.

**Suggested approach**:
1. Screen: RTX (Tomahawk + Patriot + $217B backlog, ~37-42x P/E) vs LMT (F-35 + THAAD, 17x P/E cheapest) vs NOC (B-21 + Sentinel, 23-25x P/E)
2. Frame thesis around dual-trigger (Iran + Taiwan) rather than single-event
3. LMT cheapest multiple; NOC best risk-adjusted per Iran macro; RTX most direct Iran
4. Avoid overlap with existing Iran theses (uranium, LNG, tankers) — hedge vs double-up

### Opportunity 4 — Stress-test KAMBI and TTWO ahead of binary 2026 catalysts [MEDIUM impact]

**Topic**: Adversarial stress-test on the two medium-conviction theses with zero current research depth, both facing major 2026 catalysts.

**Why now**: KAMBI's FIFA World Cup (June-July 2026, 5 weeks out) and TTWO's GTA VI (Nov 19, 2026) are binary catalysts. Zero research notes linked to KAMBI in _graph.md; zero linked to TTWO. Medium conviction ratings are unstress-tested.

**Vault connection**: Both orphan-cluster theses (no cross-thesis links). Stress-testing forces explicit decision: upgrade to full conviction with research depth, or demote to low/monitoring.

**Expected impact**: MEDIUM — unlikely to surface hidden insight at the conviction-change level for either, but forces conviction discipline ahead of binary events.

**Suggested approach**:
1. KAMBI: Sportradar ORAKO competitive threat, Flutter in-house risk, World Cup AI trading first-test, Becher strategy pivot
2. TTWO: RDR2 analog for GTA VI, Rockstar labor crisis execution risk, UGC creator marketplace thesis probability
3. Each `/stress-test TICKER` generates the adversarial brief

### Opportunity 5 — Create Marvell thesis as Broadcom complement [MEDIUM impact]

**Topic**: Marvell as #2 custom ASIC designer (~25% share), complement to AVGO.

**Why now**: April 2026 disclosure (Google inference chip talks) signals Marvell share gain in hyperscaler ASIC mix. Jensen's 65% ASIC margin claim applies to Marvell as much as Broadcom — both capture NVDA's lost margin in hyperscaler in-sourcing.

**Vault connection**: AVGO (direct competitor), NVDA (ASIC risk quantified), TSM (Marvell is TSMC customer), LITE (Marvell fabless for optical DSPs).

**Expected impact**: MEDIUM — Marvell at lower scale than AVGO, so adding both may over-weight custom ASIC. Evaluate as AVGO substitute rather than additive position.

**Suggested approach**:
1. AWS Trainium 2 lead → Trainium 3 partial share with Alchip
2. Microsoft Maia DPU + Meta DPU + potential Google inference chip
3. Optical DSP / coherent DSP positioning vs BESI/LITE via photonics cross-reference
4. Size positioning relative to AVGO weight

## 9. Additional signals for follow-up

### 9.1 Orphan research worth integrating

- [[Research/2025-06-09 - CRWV - CoreWeave Deep Dive]] — CoreWeave appears in NVDA research (strategic investment), META ($21B deal), VRT (liquid cooling customer). Implied-but-unwritten thesis candidate, GPU-cloud category.
- [[Research/2026-03-21 - Betting on Inflation Trades]] — no thesis link despite inflation being implicit in Iran macros.
- [[Research/2026-03-27 - TurboQuant Impact on Memory Demand]] — algorithmic efficiency risk flagged in 285A / SNDK / NVDA, but orphan.
- [[Research/2026-03-30 - FROG - Universal Artifact Management]] — JFrog is enterprise software adjacency, no thesis.

### 9.2 VIX macro note — candidate for rewrite or archival

Zero thesis links, generic content on VIX mechanics. Either rewrite as "Portfolio Volatility Hedging Framework" linking to AI bubble / Iran / Taiwan macros, or archive.

### 9.3 Sector-level insights suggesting standalone research

- Cybersecurity sector identifies architectural-purity + commercial-model + integration-risk as three distinct bets. Worth a dedicated comparison research note on best-of-breed vs platform via Wiz IPO timing as resolving event.
- GPU & AI Compute sector identifies Broadcom/Marvell capturing 65% ASIC margins as structural silicon-economics observation. Candidate for standalone silicon-rent-economics note.

## 10. Next Steps for `/graph last`

After this scan, run `/graph last` to register:
- This research note's adjacency to every thesis referenced (most of the vault — this is a synthesis note so expect wide adjacency)
- Implied-but-unwritten thesis candidates: SK Hynix, Samsung Memory, Micron, Marvell, RTX/LMT/NOC, CoreWeave, IONQ/Rigetti
- Cross-sector linkages flagged in Portfolio Blind Spots section

## Related

- [[_hot.md]]
- [[_graph.md]]
- [[AI Bubble Risk and Semiconductor Valuations]]
- [[Macro & Technology/Iran War Trading Playbook]]
- [[Stablecoin Regulation as Geopolitical Infrastructure]]
- [[Compute & AI Compute Accelerators]]
- [[Sectors/Semiconductor Capital Equipment]]
- [[Sectors/NAND Memory & Storage]]
- [[Sectors/Cybersecurity]]
