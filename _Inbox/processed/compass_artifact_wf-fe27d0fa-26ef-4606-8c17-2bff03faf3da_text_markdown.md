# SK hynix MR-MUF, the Hybrid Bonding Transition, and the HBM Equipment Stack
### Institutional Deep Dive — Technology, Market Structure, and Equipment Beneficiaries (HBM3E → HBM4 → HBM5)

---

## TL;DR

- **MR-MUF is the structural reason SK hynix dominates HBM (~57% revenue share Q3 2025; ~70% of Nvidia Vera Rubin HBM4 allocation), and Advanced MR-MUF will extend through HBM4 12-Hi *and* 16-Hi. Hybrid bonding has been pushed out, mostly to HBM4E/HBM5 (2028–2030).** JEDEC's relaxation of HBM4 module height to 775 µm gave microbump-based stacking another generation of life. SK hynix has *validated* 12-Hi hybrid bonding internally and placed its first mass-production hybrid-bonding inline order from BESI/Applied Materials in March 2026, but management has explicitly told investors it will retain MR-MUF through HBM4 and HBM4E 16-Hi.
- **The equipment opportunity bifurcates: a near-term TCB/MR-MUF cycle (2026–2028) favoring Hanmi, ASMPT, Towa, Disco, and Resonac/Namics; and a longer-cycle hybrid bonding inflection (2028–2030+) favoring BESI, Applied Materials, ASMPT, and Lam Research/Tokyo Electron on the front-end-like flow.** TCB bonder TAM is on track from ~$542M (2025) to $1.5–1.6B (2027–2028); hybrid bonder TAM grows from ~$152M (2025) to ~$2B by 2028 per News1 Korea/Yole. Towa (66% global molding share) and Disco (70–80% grinding/dicing) are the lowest-debate, highest-quality compounders. Hanmi is the highest-conviction long-on-near-term but the most exposed to Hynix dual-sourcing and the hybrid-bonding migration.
- **Note on terminology: "MR-URF" appears to be a typo. There is no distinct MR-URF process in any primary SK hynix, JEDEC, or trade-press source we located. Consensus terminology is MR-MUF (Mass Reflow Molded Underfill) and "Advanced MR-MUF," with the next step described variously as fluxless TCB, hybrid copper bonding (HCB), or simply hybrid bonding.** SK hynix evaluated *fluxless* bonding for HBM4 16-Hi in 4Q 2025 but rejected it for production. We treat MR-MUF and Advanced MR-MUF as the operative SK hynix flow throughout.

---

## Key Findings

1. **Yield differential is the single most important number in HBM packaging**: industry estimates put MR-MUF yield ~20 percentage points above TC-NCF; junction temperature is reported ~14°C lower under identical operating conditions; Samsung's HBM3 yield was reported at 10–20% during the worst phase of NCF struggles, vs. SK hynix at production-grade levels. Advanced MR-MUF on HBM3E delivered a further 10% improvement in heat dissipation vs. HBM3 8-Hi, with a new EMC chemistry providing 1.6× the thermal performance of the prior generation.
2. **MR-MUF's competitive moat is materials, not process equipment**: the liquid Epoxy Molding Compound (EMC) is supplied by **Namics (Japan)** under a long-running de facto exclusive arrangement with SK hynix, with **Nagase ChemteX** as a parallel Liquid Molding Compound (LMC) source and **Resonac (formerly Showa Denko Materials)** as the dominant generic EMC supplier and the alternative Samsung is courting. The Namics agreement is reportedly approaching expiration, which is shaping SK hynix's hybrid-bonding migration timing.
3. **HBM4 packaging structure across the three IDMs is now locked**: SK hynix uses Advanced MR-MUF on 1b-nm DRAM with TSMC-fabricated logic base die; Samsung uses TC-NCF (with Hybrid Copper Bonding "HCB" on a separate Cheonan line for 16-Hi HBM4/HBM4E samples) on 1c-nm DRAM with in-house 4nm Foundry base die; Micron uses TC-NCF on 1β-nm DRAM with TSMC base die. Samsung's 1c-nm yield is reportedly ~50% and its 4nm base die yield ~40%, both materially below SK hynix.
4. **Vera Rubin HBM4 supplier split (multiple sources, Mar 2026): SK hynix ~70%, Samsung ~30%, Micron ~0%**. Samsung's qualification at 10/11 Gbps is a meaningful comeback after three failed HBM3E qualification rounds at Nvidia, but Counterpoint and TrendForce both expect SK hynix to remain dominant through 2026. AMD MI400 and ASIC programs (Broadcom for Google TPU, Apple/OpenAI rumored) provide Samsung secondary lifelines.
5. **The hybrid bonding inflection is a 2028–2030 event for memory, not 2026–2027**. JEDEC raised HBM4 max package height from 720 µm to 775 µm, allowing 16-Hi to be built with refined microbump/MR-MUF flows. Industry consensus (TrendForce, Counterpoint, Yole, KAIST) now points to **HBM4E 16-Hi as a hybrid/micro-bump split, with HBM5 20-Hi (2029) as the first generation requiring hybrid bonding at scale** — wafer-to-wafer (W2W) for the highest-density variants.
6. **The hybrid bonding equipment race is consolidating around BESI/Applied Materials (Kinex) for the W2W/D2W premium tier and ASMPT/EVG, plus a Korean track of Hanwha Semitech (with Prodrive Technologies) and SEMES (Samsung captive)**. Hanmi has explicitly delayed its hybrid bonder roadmap to end-2027 (HBM6), citing TCB sufficiency for HBM4/HBM5 and the cost gap (>KRW10bn/unit hybrid vs. KRW4bn TCB).
7. **Bump pitch roadmap**: legacy C4 ~130 µm → copper pillar ~50 µm → HBM3E microbumps 20–30 µm → HBM4 microbumps target 10 µm → hybrid bonding sub-10 µm in production with sub-2 µm demonstrated by TSMC SoIC R&D and IMEC at 400 nm pitch with 150 nm overlay.
8. **Capex reality**: SK hynix announced a $13B (KRW19tn) P&T7 packaging mega-fab in Cheongju (January 2026), construction starts April 2026, full operations by late 2027 — the largest dedicated HBM packaging investment ever made and a structural commitment to MR-MUF for at least one further generation. Micron's Singapore advanced packaging plant (mass-production 2027) and SK hynix's $3.87B Indiana plant (2028) extend the buildout.
9. **Chinese supply chain is real but constrained**: CXMT is targeting HBM3 mass production by end-2026 *using MR-MUF*, with Innotron's $2.4B Shanghai packaging facility; **Tongfu Microelectronics**, **JCET**, **SJ Semi**, and **Wuhan Xinxin (XMC)** are the OSAT/foundry partners. Industry consensus, including ex-SK hynix VP Shim Dae-yong, places the China memory gap at "more than 5 years" — and China's dependence on Japanese underfill/EMC chemistries (Resonac, Namics) is the binding constraint, not equipment.
10. **The Hanmi vs. Hanwha vs. ASMPT three-way is the single best read on near-term HBM TCB economics**. Hanmi's share of SK hynix TCB orders has fallen from ~100% (pre-2024) to ~40–50% in 2025, with ASMPT at ~50% of the current 50-unit base and Hanwha Semitech entering with multiple 2025/2026 contracts. Macquarie cut Hanmi's FY26 revenue estimate from KRW1.51tn to KRW0.82tn — a ~46% cut.

---

## Details

### 1. MR-MUF / "Advanced MR-MUF" Technology — and a Note on "MR-URF"

**Terminology clarification.** "MR-URF" does not appear in any SK hynix newsroom material, EE Times/IEEE/IEDM proceedings, JEDEC documents, or trade-press coverage we've reviewed. The operative terms are:
- **MR-MUF** (Mass Reflow Molded Underfill) — introduced by SK hynix on HBM2E in 2019.
- **Advanced MR-MUF** — applied from HBM3 12-Hi onward, defined by a new liquid EMC chemistry (co-developed with Namics) delivering ~1.6× the thermal conductivity of original MR-MUF, plus warpage-control improvements that enable 30 µm-thinned DRAM dies for 16-Hi HBM4 within JEDEC's 775 µm height constraint.
- The likely candidates for the user's "MR-URF" are either: (a) a transcription/typo of MR-MUF; (b) confusion with the *Advanced* MR-MUF nomenclature; or (c) a confusion with **fluxless TCB** (sometimes called "AOR TCB" by ASMPT and "APTURA FTC" by Kulicke & Soffa), which SK hynix evaluated for HBM4 16-Hi in 4Q 2025 but ultimately rejected as premature.

We will treat the question as "MR-MUF / Advanced MR-MUF roadmap."

**Process flow vs. TC-NCF.** TC-NCF (Thermal Compression with Non-Conductive Film, Samsung/Micron) lays a polymer film between every chip pair, then thermally bonds one layer at a time — a serial process, with each die requiring a full TCB cycle. Stress on bumps from compressive force constrains thermal-dummy-bump density. MR-MUF places all chips on the substrate via standard bumping, executes a *single* mass reflow to form all solder joints simultaneously, then injects liquid EMC between the now-stacked dies in one molded underfill step. Because the process is bump-pressureless, SK hynix can populate ~4× more thermal-dummy bumps for heat dissipation, and avoid film flow-and-trapping voids that worsen with stack height. Reported metrics: ~20-percentage-point yield uplift, ~14°C lower junction temperature, fewer alignment defects on 12-Hi/16-Hi.

**Materials supply chain (the real moat).**
- **Namics (Japan)** — exclusive liquid EMC supplier to SK hynix for MR-MUF; the contract is reportedly approaching expiration, which is one reason Samsung is now in talks with Namics and one reason SK hynix's hybrid bonding timing matters.
- **Nagase ChemteX (Japan)** — second-source LMC; Samsung initiated talks with Nagase for MUF chemistry in 2024 after publicly conceding the limits of NCF.
- **Resonac (formerly Showa Denko + Hitachi Chemical)** — global No. 1 in semiconductor EMC by volume; positioned as Samsung's primary EMC vendor if/when MUF goes production at Samsung. Resonac has highlighted AI/HBM packaging as a primary growth driver.
- Localization is *not* a near-term option. Per ex-SK hynix VP Shim Dae-yong: "Without stable access to optimized underfill and EMC, 3D stacking becomes a yield nightmare. That is not something you fix with capex alone."

**Equipment in the MR-MUF flow.**
- **TC bonders** are *still required* for the initial chip-to-substrate placement (1st die placement and dummy bump formation), even in an MR-MUF flow — Hanmi is the dominant supplier, with ASMPT and Hanwha Semitech as second/third sources.
- **Mass reflow oven** — commodity.
- **Compression molding system** for the liquid EMC underfill — Towa's CPM series and FFT series dominate. Towa's *Ultra Narrow Gap Mold Underfill* (announced March 2025, sales from August 2025) is targeted at HBM4 16-Hi specifically.
- **TSV etch / fill / reveal** — Lam Research, Tokyo Electron, Applied Materials.
- **Wafer thinning to 30 µm** — Disco (dominant), Tokyo Seimitsu/Accretech (secondary).
- **Singulation, dicing** — Disco.
- **Test and inspection** — Advantest, Teradyne (test); Onto Innovation, Camtek, KLA (metrology).

**HBM4 / HBM5 roadmap for MR-MUF.**
- **HBM4 12-Hi (mass production 2H 2026)**: Advanced MR-MUF, on 1b-nm DRAM, with TSMC-fabbed customized logic base die (~12nm). SK hynix announced "world-first HBM4 mass production readiness" in Sep 2025.
- **HBM4 16-Hi (sampling at CES 2026; production 4Q 2026 / 1H 2027)**: Advanced MR-MUF, with DRAM thinned to 30 µm and EMC re-engineered for the narrower gap. Per TrendForce (January 2026), SK hynix will retain MR-MUF through HBM4 *and* HBM4E 16-Hi.
- **HBM5 20-Hi (~2029)**: industry consensus (TrendForce, Counterpoint, Yole) is that hybrid bonding becomes mandatory because of stack height and thermal/IO density, with W2W bonding likely for the highest-density variants. SK hynix has not formally confirmed HBM5 hybrid bonding adoption, but Counterpoint Research projects 2029–2030 transition; SK hynix completed internal validation of a 12-Hi hybrid-bonded HBM stack in April 2026 and placed its first mass-production hybrid-bonding order (BESI/Applied Materials Kinex inline system, ~$15M / KRW20bn) in March 2026.

### 2. Peer Comparison — Samsung, Micron, Chinese Players

**Samsung.** Adopted TC-NCF on HBM1/2/2E/3/3E. Lost three consecutive Nvidia HBM3E qualification rounds, attributed primarily to *front-end* (1a-nm, 1c-nm DRAM) yield issues rather than packaging — but the TC-NCF film-and-stack flow compounded the problem. Samsung's HBM4 strategy:
- TC-NCF for current 12-Hi HBM4 mass production (announced as "world's first HBM4 mass production" via Samsung's Cheonan line; serving Vera Rubin as the ~30% co-supplier).
- *Hybrid Copper Bonding (HCB)* — Samsung's branded hybrid bonding flow, demonstrated at GTC 2026 — claimed: 33% higher stacking, 20% lower thermal resistance, base die temperature reduced by >11% on 12/16-Hi. Samsung is establishing a *dedicated HCB line at Cheonan*, with equipment from BESI (development), Onto Innovation (non-destructive ultrasonic inspection), and crucially **SEMES** (Samsung's captive equipment subsidiary, which produced a 16-layer HBM3 functional sample using internal hybrid bonders in mid-2024).
- Per Samsung CTO Jae-hyuk Song (Semicon Korea 2026), HCB will be "fully mass-produced" from HBM5; HBM4E will be a TCB/HCB hybrid.
- Samsung dropped Shinkawa as a TC bonder supplier in 2025; Hanmi remains uncoupled from Samsung due to a long-standing 2011 SEMES patent dispute (though some thaw is reported).

**Micron.** TC-NCF on 1β-nm DRAM. Maintained adequate yield to qualify for HBM3E with Nvidia (Hopper, early Blackwell). Lost the HBM4 Vera Rubin slot per multiple Korean reports — reportedly redesigned HBM4 in November 2025 to address yield and performance issues but missed the Q1 2026 contract window. Will continue to ship HBM3E and may secure HBM4 inclusion in non-Nvidia platforms (AMD MI400, hyperscaler ASICs); also dominant in LPDDR5X/SOCAMM2 for Vera CPUs. Micron's TC bonder supply chain has rotated: historically Shinkawa + Hanmi, now Hanmi as primary (~50 unit order in 1H 2025, +20–30 in 2H), with **BESI expected to become the sole HBM4 TCB vendor** per supply-chain notes (geopolitical reasons disqualify ASMPT given its Hong Kong domicile).

**CXMT and Chinese supply chain.**
- CXMT has been mass-producing HBM2 since 2024 and is targeting HBM3 mass production by end-2026 — *using MR-MUF*, per DigiTimes (citing Korean sources, November 2025). This is a notable choice: it implies Chinese access to either Namics-equivalent EMC chemistry (likely via Resonac or domestic substitutes) and patent risk on SK hynix's MR-MUF process IP.
- **Innotron (CXMT parent)** announced a $2.4B advanced packaging facility in Shanghai (mid-2026 production, 30k units/month).
- Chinese OSAT ecosystem: **Tongfu Microelectronics** (working with CXMT, also AMD JV partner with packaging IP); **JCET Group** (XDFOI fan-out for HBM); **SJ Semi** and **Wuhan Xinxin (XMC)** ramping HBM2 capacity. Tongfu, SJ Semi, and CXMT have all entered hybrid-bonding patent landscape over the past three years.
- The constraint is *materials and base-die foundry access* (SMIC at sub-7nm equivalent vs. TSMC 12nm base die), not packaging equipment.
- 2029–2030 disruption to the global HBM oligopoly is plausible but more likely confined to mainland AI accelerators (Huawei Ascend, Biren, MetaX, Iluvatar, Moore Threads); penetration of Nvidia/AMD/Broadcom sockets remains a low-probability event over our 2026–2028 horizon.

**Competitive socket-by-socket scoreboard (as of May 2026)**:
| Customer/Platform | HBM3E 12-Hi | HBM4 12-Hi | HBM4 16-Hi |
|---|---|---|---|
| Nvidia Blackwell/Blackwell Ultra | SK hynix dominant; Micron secondary | n/a | n/a |
| Nvidia Vera Rubin (VR200 NVL72) | n/a | SK hynix ~70%; Samsung ~30% | SK hynix lead, sample |
| AMD MI350 | Samsung, Micron | n/a | n/a |
| AMD MI400/MI450 | n/a | Samsung, Micron, SK hynix | TBD |
| Broadcom (Google TPU, Apple, OpenAI) | Samsung HBM3E 8-Hi (rumored) | TBD | TBD |

### 3. Hybrid Bonding Transition: HBM4 → HBM5

**When.** JEDEC's HBM4 height extension to 775 µm (from HBM3E's 720 µm) gave microbump bonding ~50 µm of additional vertical headroom — enough to support 16-Hi within a refined MR-MUF/TC-NCF flow, provided DRAM dies are thinned to ~30 µm. That single decision pushed back the hybrid-bonding necessity by one full generation. Consensus now:
- HBM4 12-Hi (2026): microbump (MR-MUF or TC-NCF).
- HBM4 16-Hi (2H26–2027): microbump still adequate; SK hynix retains MR-MUF, Samsung uses TC-NCF with HCB optionality on a parallel line.
- HBM4E 16-Hi (~2027–2028): mixed; Samsung pushes HCB on selected SKUs; SK hynix evaluates fluxless TCB and hybrid bonding as backup.
- **HBM5 20-Hi (2028–2030, paired with Nvidia Feynman): hybrid bonding mandatory**; W2W expected for premium variants, D2W for standard SKUs. KAIST's roadmap shows HBM5 may even require *immersion cooling* given the logic-die heat load.

**Why hybrid bonding eventually wins.** Microbump pitch limits collapse below 10 µm due to plating uniformity and solder reflow variability. Hybrid bonding (Cu-Cu / SiO₂-SiO₂ direct bonding) supports sub-10 µm pitch in production today, with sub-2 µm demonstrated. Stack thickness is reduced by eliminating bump volume entirely. Power efficiency improves from lower interconnect resistance. For HBM5 with 4,096-bit I/O (double HBM4) and per-stack bandwidth >4 TB/s, hybrid bonding is required not optional.

**Why hybrid bonding has been delayed.**
1. Cost: hybrid bonders are ~$3M+ each (Hanmi cites >KRW10bn/$7M, ~2.5× TCB).
2. Cleanroom requirements migrate from OSAT-class to fab-class (ISO 3 / Class 1 minimum, with TSMC pursuing ISO 1/2). This blows up TCO.
3. Hybrid bonding is W2W or D2W; W2W requires the base die and DRAM die to share identical chip dimensions, shifting some control to TSMC away from the memory IDMs — a strategic disincentive for SK hynix and Samsung.
4. Yield risk: per Inha University's Prof. Yoon, "If 1 of 8 wafers fails in W2W, all 8 must be scrapped," with current 16-Hi W2W yields ~10%.

**SK hynix's posture.** Validated 12-Hi hybrid bonding internally (announced April 2026 at Beyond HBM, Seoul). Placed first commercial hybrid bonding inline order from Applied Materials/BESI Kinex (March 2026, ~$15M). Has explicit messaging: "MR-MUF first, hybrid bonding when economics work." Counterpoint expects production hybrid bonding at SK hynix in 2029–2030, with HBM5.

**Samsung's posture.** More aggressive on stated roadmap — HCB line being equipped at Cheonan with March 2026 equipment receipts, evaluating BESI for development plus internal SEMES bonders. CTO has indicated HBM4E mixed adoption, full HCB at HBM5. Execution credibility remains the question.

### 4. Equipment Beneficiaries

#### (a) Hybrid bonding tool ecosystem

**BESI (Euronext: BESI)** — *Most differentiated single-name on the HBM5 thesis.*
- **Position.** ~42% global die-attach share. Datacon 8800 CHAMEO ultra plus AC platform delivers ±100 nm @ 3σ alignment; Gen-2 (50 nm precision, <4 µm bump pitch, 3,000 UPH) shipping Q4 2025–Q1 2026 with first delivery to a Taiwanese leading-edge foundry. Co-developed Kinex inline hybrid bonding platform with Applied Materials (CMP + plasma + bonder).
- **Customers.** TSMC (SoIC), Intel (Foveros), AMD (3D V-Cache via TSMC), Sony (CIS); SK hynix mass-production order March 2026 (first); Samsung evaluating for HCB line; Micron expected to adopt BESI as sole HBM4 TCB vendor longer term.
- **Financials.** FY2025 revenue €591.3M (down slightly YoY), gross margin 63.3%. H2 2025 orders +63.6% vs. H1, driven by HBM4 advanced packaging bookings. Q1 2026 revenue €184.9M (+28.3% YoY); Q2 2026 guidance +30–40% QoQ implying ~€250M. Investor Day (June 2025): five-year revenue target €1.5–1.9B, gross margin ≥66%.
- **Risk.** Order intake decelerated 6.5% YoY in 9M 2025; backlog ~€400M at end-March 2026; the rhythm of hybrid bonding adoption could slip if MR-MUF/TC-NCF extend further. Customer concentration (foundry-heavy through 2026, memory adoption only from 2027/2028).
- **View: BULLISH.** Highest pure-play exposure to HBM5 hybrid bonding inflection. Trades on 2028 hybrid bonding optionality; current quarterly cadence already inflecting positively.

**ASMPT (HKEX: 0522)** — *Best-positioned for the bridge years (TCB now, HB later).*
- **Position.** Leader in TCB (record 2025 revenue, ~146% YoY growth, advanced packaging revenue $532.1M, +30.2% YoY). TAM revised to $1.6B by 2028 (30% CAGR). Second-generation HB platform shipping Q3 2025 to first HBM customer; AOR fluxless TCB qualified at SK hynix for HBM4 16-Hi sampling.
- **HBM customer base.** SK hynix (currently ~50% of the 50-unit deployed TCB base for HBM4, 7-unit ~$30M order December 2025); IBM partnership for chiplet bonding methods.
- **Risk.** Hong Kong domicile is a structural impediment to Micron qualification, leaving Samsung/SK hynix/Chinese makers as the addressable customer set.
- **View: BULLISH.** Most under-appreciated TCB/HB optionality; 2nd-gen hybrid bonder credibility growing.

**Shibaura Mechatronics (TSE: 6590)** — *Specialty hybrid bonder TFC-6700/6800 platform.*
- Highest market share in 2.5D high-end flip-chip bonders (per company self-disclosure, in advanced packaging). TFC-6700/6800 is a chip-to-wafer hybrid bonder/fusion platform.
- Customer set: primarily Japanese OSATs and image-sensor (Sony) flow; not yet a structural HBM player.
- **View: NEUTRAL.** Optionality, not core thesis.

**Applied Materials (NASDAQ: AMAT)** — *The CMP/plasma/etch beneficiary of Kinex.*
- Co-developer of Kinex inline hybrid bonding system with BESI; supplies CMP and plasma processing tools that flank the bonder. Joint R&D agreement with SK hynix announced March 2026 at the new EPIC Center, Silicon Valley.
- Etch business crossed $1B/quarter for the first time in late 2025 with new advanced DRAM wins (HBM TSV reveal).
- **View: BULLISH (within US WFE).** Indirect exposure but the beneficiary list is small.

**Lam Research (NASDAQ: LRCX)** — *Indirect HBM4/HBM5 leverage via TSV etch and dry-resist.*
- Industry leadership in TSV etch and electroplating; advanced packaging business expected to grow >40% in 2026 vs. WFE growth. Q3 2025 (Sep): record $5.32B revenue, DRAM mix increased to 16% of systems revenue from 14% on HBM investment. Aether dry-resist deposition is a HBM "tool of record" win.
- **View: BULLISH (within US WFE).** Indirect but durable HBM exposure; gross margin inflection adds a fundamental tailwind beyond the HBM thesis.

#### (b) TCB/MR-MUF/molding/underfill

**Hanmi Semiconductor (KRX: 042700)** — *Highest near-term EPS leverage; highest 2026–2027 disruption risk.*
- **Position.** ~71% global TC bonder market share (TechInsights); >90% of HBM3E 12-Hi TCB shipments. Has been SK hynix's exclusive TC bonder supplier since 2017 until Q4 2024.
- **Recent dynamics (2025–2026)** materially negative for the Hanmi-SK hynix axis:
  - SK hynix added ASMPT (Q4 2024) and Hanwha Semitech (early 2025) as second/third sources.
  - Hanmi raised TCB prices to SK hynix by 25–28% and recalled 60 service engineers in April 2025.
  - SK hynix was reportedly considering full diversification of all Hanmi-supplied equipment (not just TCB) per Financial News.
  - **Macquarie cut Hanmi FY26 revenue forecast from KRW1.514tn to KRW822bn (-46%) and FY27 from KRW2.184tn to KRW1.045tn (-52%).** PT cut from KRW170,000 to KRW90,000 with downgrade to Neutral.
  - Hanmi compensated with major Micron orders (~50 units 1H 2025, ~30 unit follow-on in 2H, at 30–40% price premium to SK hynix because Micron's TC-NCF requires higher-spec bonding heads).
  - Hanmi Chairman Kwak: TC bonders are "sufficient for HBM4 and HBM5"; hybrid bonder for HBM6 only by end-2027. KRW100bn invested in 7th plant (hybrid-bonder-dedicated, 14,600 m², H1 2026 opening).
- **Valuation.** Stock has performed phenomenally (>4× over 12 months), trading at ~KRW375,500 with KRW34.9tn market cap (May 2026). Analyst consensus 12M PT KRW186,532 — well below current price. Forward consensus revenue 2026: KRW793bn (-16% from earlier consensus); operating margin still ~40%+. Implied trading multiple in the 30–40× FY26 P/E range — punchy.
- **View: NEUTRAL trending BEARISH.** The market is pricing Hanmi like a structural compounder, but the order trajectory at SK hynix is structurally weakening, hybrid bonder is a 2027 launch (post-competition), and Micron's potential migration to BESI on HBM4 truncates the second growth engine. Take profits into strength.

**Hanwha Semitech (Hanwha Vision: KRX: 023910)** — *Disruptor on the way up.*
- TC bonder supply to SK hynix from 2025: KRW21bn deal (14 units), KRW42bn follow-on. Engaged in patent litigation with Hanmi (filed Dec 2024; countersuit in May 2025; first hearing April 2026).
- SHB2 Nano hybrid bonder (co-developed with Prodrive Technologies, Netherlands), ±100 nm alignment, designed to match BESI Datacon 8800 CHAMEO; first article shipped to Korea March 2026 for SK hynix qualification testing.
- 2024 TCB revenue: ~KRW90bn; 2025 ramp expected. Hanwha Group exploring M&A in semiconductor equipment via Vice Chairman Kim's strategic unit.
- **View: BULLISH but execution-dependent.** Less liquid than Hanmi but with much steeper relative upside if SHB2 Nano qualifies at SK hynix in 2026.

**Towa Corporation (TSE: 6315)** — *Highest-quality, lowest-debate HBM packaging compounder.*
- 66% global molding equipment market share (TechInsights). Compression molding (CPM/FFT/PMC series) is the core MR-MUF flow tool. Ultra Narrow Gap Mold Underfill technology launched March 2025 specifically for HBM4 16-Hi — sales from August 2025.
- South Korea factory acquired April 2024 to support SK hynix and Samsung; capacity for ~JPY80bn of orders; Suzhou and Nantong (China) facilities also expanding.
- FY2025 (March 2025) revenue ~JPY54bn; FY2026 guidance +31% YoY to JPY71bn (~$474M). Market cap ~$1.2B (May 2026); 2,284 employees.
- **View: BULLISH.** Nearly monopolistic position, direct HBM4 product leadership, low headline valuation vs. Hanmi/BESI, secular tailwind regardless of MR-MUF/TC-NCF mix.

**Shinkawa (Yamaha Motor)** — *Eroding TCB position.*
- Acquired by Yamaha; service/maintenance reportedly degraded post-acquisition. Samsung dropped Shinkawa in 2025 in favor of SEMES; Micron moved most volume to Hanmi. For HBM4, expected to lose Micron's volume to BESI.
- **View: BEARISH.** Trapped between captive Korean (SEMES, Hanmi/Hanwha) and global (BESI, ASMPT) players with no obvious path back into HBM TCB.

**Kulicke & Soffa (NASDAQ: KLIC)** — *Logic-packaging-heavy; HBM optionality.*
- APTURA FTC fluxless TCB platform with sub-1 µm placement, <10 µm bump pitch — competes with ASMPT's AOR. Position primarily in logic/2.5D rather than HBM stacking.
- **View: NEUTRAL.** Tangential HBM exposure.

#### (c) Full-stack: TSV/grinding/dicing/test

**Disco Corporation (TSE: 6146)** — *Quintessential HBM picks-and-shovels compounder.*
- 70–80% global wafer dicing/grinding market share. Critical to HBM TSV reveal grinding (post-TSV plating, wafer thinned to 30 µm), dicing of bumped wafers, and HBM stack singulation.
- Q1 FY2026 (April 2026 quarter) revenue $838M (+27% beat vs. consensus $660M); FY2025 TTM revenue $2.74B. Market cap ~$50B. 30–35% of revenue is high-margin consumables (razor-and-blade model). Gross margin 69.7%.
- Multiple tool families (DGP grinder series, DFD/DFM dicers, DFL laser saws) all benefit from HBM intensity.
- **View: BULLISH.** Highest-quality compounder in the entire HBM equipment stack. Trades at ~56× P/E — premium but justified by monopolistic position, AI/HBM tailwind, and consumables annuity.

**Tokyo Seimitsu / Accretech (TSE: 7729)** — *Distant second to Disco.*
- Polish grinders, high-rigidity grinders, dicers, CMP, edge grinders, probers. Less HBM-specific market share but a credible alternative for memory IDMs seeking dual-source.
- **View: NEUTRAL.** Quality business but Disco is the primary HBM beneficiary; differentiated end-market (probers, metrology) provides some diversification.

**Tokyo Electron (TSE: 8035)** — *Diversified WFE giant; HBM exposure via TSV etch and temporary bond/debond.*
- Etch leadership across logic and DRAM; SUSS Microtec is the specialist temp-bond/debond player for HBM, but TEL participates broadly.
- **View: NEUTRAL/BULLISH.** HBM is incremental, not core, but the broader AI-driven WFE cycle is the relevant thesis.

**SUSS MicroTec (XETRA: SMHN)** — *Niche temp-bond/debond + W2W permanent bonding.*
- Active in both hybrid bonding (W2W permanent bonding) and temporary bonding for HBM TSV reveal flow.
- **View: BULLISH on the small/mid-cap.** High-conviction asymmetric exposure to memory hybrid bonding adoption from HBM4E onward.

**EV Group (private, Austria)** — Permanent W2W bonding leader; partnered with ASMPT. Not investable directly.

#### (d) Test & metrology

**Onto Innovation (NYSE: ONTO)** — Selected by Samsung for non-destructive ultrasonic inspection of hybrid bonding interfaces (PULSE metrology). Major HBM4 ramp inspection design win on the Dragonfly G5. **BULLISH but smaller.**

**Camtek (NASDAQ: CAMT)**, **KLA (NASDAQ: KLAC)** — incremental beneficiaries via inspection tightening as bump pitch shrinks and hybrid bonding overlay budgets fall to <50 nm. KLA more diversified; Camtek more pure-play HBM/advanced packaging.

**Advantest (TSE: 6857)** — Test, primarily logic but increasing HBM stack-level test exposure. **BULLISH (broader AI/HBM thesis).**

### 5. Materials Beneficiaries

| Material | Application | Suppliers (HBM relevance) |
|---|---|---|
| Liquid Epoxy Molding Compound (EMC) for MR-MUF | Encapsulation between stacked dies | **Namics** (SK hynix exclusive, contract approaching expiration); **Nagase ChemteX** (LMC); **Resonac** (global EMC leader, Samsung-aligned) |
| Non-Conductive Film (NCF) | TC-NCF flow, Samsung/Micron | Resonac, Sumitomo Bakelite, Nagase |
| Capillary underfill | TCB-CUF flows | Henkel, Namics, Nagase |
| ABF (Ajinomoto Build-up Film) | Substrate dielectric | **Ajinomoto** (98% IP licensing control); buyers: Unimicron, Ibiden, Shinko, Nan Ya, Kinsus, AT&S |
| Substrate (high-end ABF) | HBM/CoWoS organic substrate | **Ibiden** (~19% share); **Shinko Electric** (~12%); **Unimicron** (~22%); Nan Ya (~14%); Kinsus, AT&S, Semco |

**Investment angle.**
- **Resonac (TSE: 4004)** — under-owned EMC name with broad HBM/AI exposure; arguably the highest-leverage *materials* play if Samsung's MUF migration accelerates and SK hynix's Namics exclusivity ends. **BULLISH.**
- **Ibiden (TSE: 4062)** — ABF substrate beneficiary; AI server substrate revenue projected ~3× prior year per company commentary. **BULLISH.**
- **Shinko Electric (TSE: 6967)** — pending JIC privatization; strong AI substrate franchise. **NEUTRAL** pending deal completion.
- **Unimicron (TWSE: 3037)** — Taiwan ABF leader, broadest exposure to AI substrate ramp. **BULLISH.**
- **Nan Ya PCB (TWSE: 8046)** — value end of the ABF complex. **NEUTRAL.**

### 6. Investment Implications — Directional Views

| Name | Ticker | Position | View | Rationale |
|---|---|---|---|---|
| **BESI** | ENXTAM:BESI | Hybrid bonder (Kinex) | **Bullish** | Only pure-play on HBM5 hybrid bonding; Q4 25 / H1 26 inflection visible in orders; €1.5–1.9B 2030 target. |
| **ASMPT** | HKEX:0522 | TCB + 2nd-gen HB | **Bullish** | Best bridge: TCB market leader, HB credibility growing; $1.6B TCB TAM by 2028. |
| **Disco** | TSE:6146 | Grinding/dicing | **Bullish** | Monopolistic; 30%+ consumables annuity; 27% revenue beat in Q1 FY26; secular HBM intensity. |
| **Towa** | TSE:6315 | Compression molding (MR-MUF/MUF) | **Bullish** | 66% global share; HBM4 narrow-gap MUF launched; Korea factory + China expansion. |
| **Hanmi Semiconductor** | KRX:042700 | TCB | **Neutral / take profits** | Macquarie's -46% FY26 revenue cut; SK hynix dual-sourcing; hybrid bonder delayed to HBM6 (end-2027); rich valuation. |
| **Hanwha Semitech (Hanwha Vision)** | KRX:023910 | TCB + HB | **Bullish (speculative)** | Asymmetric upside if SHB2 Nano qualifies at SK hynix in 2H 2026. |
| **Shinkawa (Yamaha Motor)** | TSE:7951 | TCB | **Bearish (within Yamaha)** | Lost Samsung; losing Micron HBM4 to BESI; service/maintenance erosion. |
| **Shibaura Mechatronics** | TSE:6590 | Hybrid bonder, flip chip | **Neutral** | Optionality only. |
| **Tokyo Seimitsu** | TSE:7729 | Grinding/dicing | **Neutral** | Quality but Disco-overshadowed. |
| **Applied Materials** | NASDAQ:AMAT | CMP/etch/Kinex | **Bullish** (US WFE pick) | Direct hybrid bonding line revenue + DRAM HBM TSV. |
| **Lam Research** | NASDAQ:LRCX | TSV etch / deposition | **Bullish** (US WFE pick) | Advanced packaging +40% in 2026; record margins. |
| **Onto Innovation** | NYSE:ONTO | HB inspection | **Bullish (small cap)** | Samsung HCB + Dragonfly G5 HBM4 design wins. |
| **SUSS MicroTec** | XETRA:SMHN | Temp bond + W2W permanent | **Bullish (small cap)** | Niche structural play on HBM4E/HBM5. |
| **Camtek** | NASDAQ:CAMT | Advanced packaging metrology | **Bullish** | Pure-play HBM beneficiary. |
| **Advantest** | TSE:6857 | Test | **Bullish** | Broad AI/HBM tailwind. |
| **Resonac** | TSE:4004 | EMC, CMP slurry | **Bullish** | Leverage if Samsung's MUF migration accelerates. |
| **Ibiden** | TSE:4062 | ABF substrate | **Bullish** | AI server substrate >3× revenue uplift. |
| **Unimicron** | TWSE:3037 | ABF substrate | **Bullish** | Broadest Taiwan AI substrate exposure. |
| **TF Microelectronics** | SHE:002156 | OSAT/HBM packaging | **Neutral (China-only)** | Real but constrained CXMT-AMD axis. |
| **JCET** | SHA:600584 | OSAT/XDFOI HBM | **Neutral (China-only)** | Domestic AI accelerator support. |

**Highest-conviction long ideas, ranked**:
1. **Disco** — quality + HBM secular + consumables annuity. Lowest debate.
2. **Towa** — direct MR-MUF/MUF beneficiary; not crowded; HBM4 product cycle just starting.
3. **BESI** — best torque to HBM5 hybrid bonding; Q4 25/H1 26 order inflection now confirmed.
4. **ASMPT** — best bridge from TCB to HB; record TCB revenue; Hanmi disruption is ASMPT's gain.
5. **Resonac / Ibiden** — materials/substrate plays under-owned by AI-momentum capital.

**At-risk if hybrid bonding ramps faster than expected**: Hanmi (HBM6 timeline misses), Shinkawa, Kulicke & Soffa (TCB-tilted).
**At-risk if hybrid bonding ramps slower than expected**: BESI (already under that scenario in 2025; Q4 25 recovery suggests adoption is back on track for 2027+); Hanwha Semitech.

### 7. Key Risks and Debates

1. **MR-MUF longevity risk (favoring SK hynix incumbents).** SK hynix's $13B P&T7 capex and the explicit retention of MR-MUF for HBM4 16-Hi and HBM4E mean MR-MUF could carry production volumes through 2028. This favors Towa, Disco, Resonac/Namics/Nagase, and TCB-side suppliers (Hanmi/ASMPT/Hanwha) at the expense of hybrid bonder vendors' near-term order rates. BESI's 2025 order softness validates this risk; the 4Q 25 / 1Q 26 recovery suggests the inflection is delayed but not derailed.
2. **Samsung HCB execution risk.** Samsung has been the loudest proponent of hybrid bonding for HBM4/HBM4E but has a multi-year track record of aggressive technology positioning followed by execution shortfalls (HBM3E qualification failures × 3, 1c-nm yield ~50%, 4nm base die yield ~40%). HCB qualification at Nvidia for HBM4E in 2027 is *not* the base case; if it fails, MR-MUF's window extends another generation.
3. **Chinese commoditization risk.** CXMT's 2026 HBM3 launch using MR-MUF is a real threat to *non-leading-edge* HBM pricing in 2027–2028, but the 5+ year gap to leading edge is genuine. Equipment-side, Tongfu/JCET drive incremental Towa/Disco/SUSS sales without displacing Korean/US demand. Macro risk: if Beijing forces faster localization of EMC/NCF away from Resonac/Namics/Nagase, that materials moat erodes.
4. **Memory cycle timing.** HBM is structurally less cyclical than commodity DRAM (1-year forward contract pricing) but is not acyclical. A demand correction in 2H 2026 — driven by hyperscaler digestion or AI accelerator over-order — would defer TCB and HB equipment orders by 2–4 quarters. Hanmi (Macquarie's call) is the canary; broader equipment names would follow with a lag.
5. **Vendor dual-sourcing dynamics.** SK hynix has demonstrated willingness to dual/triple-source TCB (Hanmi → +ASMPT → +Hanwha). The same pattern is likely on MUF (Namics → +Nagase → +Resonac), molding (Towa → +ASMPT/BESI), and ultimately hybrid bonding (BESI → +ASMPT → +Hanwha → +SEMES at Samsung). This compresses pricing power for incumbents over the 2026–2028 window.
6. **JEDEC standards risk.** The HBM4 height extension to 775 µm was the single most consequential HBM packaging decision of the past three years. Future JEDEC accommodations (HBM4E or HBM5) could either accelerate or decelerate hybrid bonding adoption; current signal is HBM5 will be height-constrained, forcing the transition.
7. **Geopolitics and the BESI / Applied / Lam / TEL "front-end" framing.** Hybrid bonding's classification as front-end-like (ISO 1–3 cleanrooms, fab-class CMP/etch) means it eventually falls under US export-controls scope to China. CXMT/Tongfu's hybrid bonding ambitions face equipment denial risk that microbump TCB does not.

---

## Caveats

- **Note on dating and forward-looking statements.** This report draws on trade-press and primary-source material spanning early 2024 through May 2026. Several specific items are predictions or projections (e.g., "Macquarie projects hybrid bonder market $2.8tn KRW by 2028"; "Counterpoint expects HBM5 hybrid bonding 2029–2030"; SK hynix HBM5 strategy is described by industry research firms, not formally announced). We have flagged "expected/projected" wherever applicable and recommend triangulating these with sell-side primary research.
- **Yield numbers are estimates, not disclosed figures.** The widely cited "20% yield differential" between MR-MUF and TC-NCF, and Samsung's "10–20% HBM3 yield" figure (Reuters, March 2024), are sourced from anonymous supply-chain channels rather than company disclosure. Treat directionally.
- **Hanmi vs. Hanwha vs. ASMPT order share at SK hynix is fluid.** Reported splits (Hanmi 40–50%, ASMPT 50%, Hanwha entering) reflect the deployed *base* of HBM4 TCB tools, not forward order share. The March 2026 100-unit order from SK hynix will reset these mathematically.
- **Samsung "world-first HBM4 mass production" claim** (February 2026) is contested in the trade press; SK hynix announced HBM4 mass-production *readiness* in September 2025. Both are competing for first-mover narrative around Vera Rubin shipments; actual high-volume qualification at Nvidia remains the more meaningful milestone.
- **Macquarie's Hanmi cuts are aggressive vs. consensus.** Other houses (some Korean brokers) maintain Buy with PTs above KRW400,000. Sell-side dispersion on Hanmi is among the widest in the Korean equipment complex; the Macquarie thesis (TCB diversification + hybrid-bonder lateness) is one credible bear case but not the universal view.
- **"MR-URF" usage in the user prompt:** as noted, no such process exists in our reviewed primary sources. The closest distinct concepts are (a) Advanced MR-MUF and (b) fluxless TCB / HCB. We've covered all three exhaustively.
- **Bump pitch numbers** (50 µm → 25 µm → sub-10 µm) are consensus industry roadmap figures from Yole, Semianalysis, and Semiconductor Engineering; specific HBM4 microbump pitch is generally cited at ~10 µm with hybrid bonding sub-10 µm in production.
- **Multiples cited (Disco 56× P/E, Hanmi 30–40× FY26 P/E)** are point-in-time as of the dates referenced in source material (Q1–Q2 2026); these will move materially with stock price action and consensus revisions.
- **Vera Rubin HBM4 supply split (SK hynix 70% / Samsung 30%)** is from Korean trade press citing industry sources (March 2026); Nvidia has not formally confirmed allocation. The split could shift materially based on Samsung's HCB execution and any Micron re-qualification.
- This report is research, not investment advice. Position sizing, hedging, and risk management around any single name should reflect the considerable execution and timing uncertainty in HBM4 → HBM5 transition.