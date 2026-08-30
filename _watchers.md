---
publish: false
date: 2026-08-27
tags: [meta, automation, watcher-registry]
status: active
---

# Watcher Registry

Single source of truth for everything n8n pulls into `_Inbox/`. **Edit this file — never the n8n workflows.** Each workflow reads its own section on every scheduled run and builds its targets from these rows; changes take effect on the next run with no redeploy, no restart, no touching n8n's UI.

**Lifecycle of a watch:**
- `status: active` + within its window → pulled.
- `status: paused` → muted but kept (re-enable later by flipping one word).
- `expires:` a date → auto-retires after that date (windowed watches self-remove — you never have to remember to turn them off). `permanent` → runs until deleted.
- Delete the row → gone for good.

**Discipline:** every watch names a `thesis` so orphaned watches (thesis closed, question resolved) surface at the monthly review. A watch with no thesis is noise waiting to happen.

**Formatting constraint:** no aliased wikilinks (`[[note|alias]]`) inside table cells — the `|` breaks both Obsidian's table render and the n8n parser. Use bare `[[note]]`.

---

## Mailing list

BCC recipients for the daily intel email (Workflow 3 → Send Email node). The Plan parses every real email address it finds in this section and BCCs them — add or remove people here in Obsidian, no n8n edit, effective next run. Everyone is **BCC'd** so recipients never see each other's addresses. An empty list means the email goes only to you (the `To` address on the node).

Add one address per bullet below, written normally (the placeholder `alice[at]example[dot]com` is obfuscated on purpose so it isn't picked up). Recipients:

- will@laniakea.partners
- 11653687@qq.com
- 2278224@qq.com
- vickycheung88@qq.com
- 22425955@qq.com
- 170610374@qq.com
- 280568490@qq.com
- james_juwana77@hotmail.com

---

## News & Thematic (Workflow 3 unified — news queries; GN + GDELT + Brave all read these rows)

The unified Workflow 3 runs each active, unexpired row through Google News RSS, GDELT, and Brave on every sweep (thesis tickers are covered automatically via filename-derived company-name queries — no per-ticker rows needed here). Rows grouped by cluster for readability — the parser reads every table in this section identically. Populated 2026-07-17 from thesis-extraction pass across all semiconductor-complex theses (active + monitoring) + PLTR/META/NET; every row anchors to a dated observable, falsifier, or catalyst in the linked thesis. Rows marked ⚠ watch the *bear* side of their thesis (disconfirmation coverage per the READING PROTOCOL).

Revised 2026-07-26 against the post-07-17 vault state (TSM Q2'26 sync, hyperscaler-guide week Jul 28–31, 07-11 conviction re-rates): added hyperscaler-guides (windowed) + copos-panel + agentic-commerce + first non-semis bear-watches for HIGH names (intu-agentic, uber-av); re-scoped intel-18a (EMIB keywords, re-anchored to TSM reversal-watch), samsung-hbm (+Micron), mlcc-ai (+SEMCO), tiktok-ban (+JV/algorithm/CFIUS); retired net-outage + pltr-nhs (audit trail below).

Revised 2026-08-27 against the Live Portfolio Holdings table (2026-08-25: PLTR + NBIS Full 25%+; 000660 + SPCX High 10–25%; NVDA / NET / AVGO / MRVL Medium; SNDK / 285A / 6857 Low; TSM, LRCX, AMAT, KLA, ASMI, BESI removed from the book). The two largest weights had no thematic coverage at all (NBIS, SPCX: auto ticker queries only), so `{themes}` over-weighted ex-book semicap questions and carried none of the book's live falsifiers. Added a `### Neoclouds & AI infrastructure` cluster (NBIS energisation / funding mix / stake monetisation / anchor-customer in-housing / peer capacity and pricing; SPCX CSA duration / YE26 nameplate / Starlink churn / lock-up supply), PLTR bear-watches at Full weight (sovereignty contagion; governed write-back folded into pltr-rivals), AVGO demand (Tomahawk, Anthropic TPU gigawatts) and bear (VMware/EU, MediaTek ASIC) rows, NVDA InferenceX (the dated ASIC-parity falsifier, Q3 CY26), 000660 process (MR-MUF vs TC-NCF, 16-Hi) / NVHBM base-die / Namics-M15X-Solidigm rows, SNDK LTA-floor durability, Kioxia post-Bain flow catalysts, MRVL Celestial and LPO-share, NET commoditisation watch. Re-scoped: pltr-defense (+Maven, Enterprise Agreement: the CLOSE leg), net-act4 (+Googlebot / Bingbot / Content Signals / Monetization Gateway ahead of the 15 Sep crawler deadline), nand-cycle (+capex, LTA), hyperscaler-guides (re-windowed to 2027-02-15 so it covers the Q3 CY26 prints and the FY27 guides, the AI kill-switch in `_catalyst.md`). Re-anchored export-controls AMAT → NVDA (the Q3 guide is ex-China; AMAT left the book, thesis still active). Nothing retired: rows anchored to ex-book but still-active theses (intel-18a, tsmc-nodes, cowos, x-tsmc → TSM; hybrid-bonding, besi-ma, jedec-hbm → BESI; tor-selection → ASMI; wfe-china → KLA; glass-substrate, abf-hanwha, x-abf → 2802) stay active under the thesis-anchor discipline; pause them here if the book, not the thesis list, should set coverage. Budget: +21 query rows lifts Brave to ~3,600/mo, so `brave_budget_mo` 3500 → 4000 (Tuning).

Revised 2026-08-27 (second pass) against the Watchlist Universe table, every name marked `active` (41 names; the 11 held names were covered in the pass above). Sixteen active names had no thematic row at all (LRCX, PANW, NOW, SHOP, SPOT, TTWO, VICR, APP, CRCL, DUOL, DE, VRT, WTC, CBRS, GAW, CRWV in its own right) and a further twelve carried a single row, so the registry's `{themes}` list under-represented most of the researched-but-not-held book. Added 36 rows, each anchored to a registered Conviction-Trigger leg, a stress-test kill trigger (SHOP, SPOT, GAW, UBER, WTC, LITE, IQE, 2026-08-15 batch) or a dated catalyst, windowed wherever the observable has a date: semicap (lrcx-aether, wfe-forecast, n2-ald-share, amat-legs, kla-metrology, asmi-por, mlcc-008004), foundry (abf-demand), compute (amd-commit, amd-epyc, cbrs-anchor), photonics (lite-ocs, lite-6inch, aixa-mix, iqe-inp, sive-listing), software (panw-platform, now-assist, saas-seats, shop-agentic, shop-rivals, crcl-coinbase, wtc-asic), a new `### Consumer, media & industrial` cluster (spot-ads, gta6-launch, duol-platform, gaw-licensing, uber-fleet, deere-autonomy, applovin-ecom), neoclouds (crwv-credit, gpu-rerent) and a new `### Datacenter power & cooling` cluster (vrt-orders, vrt-cooling, vicr-vpd, 800vdc anchored to the macro note). Re-scoped wlbi-test (+order / bookings / SiPh, the AEHR HIGH and CLOSE legs) and extended it to 2027-03-31. Retired iqe-bid (strategic review closed with no bid 2026-04-27; audit trail below) in favour of iqe-inp. No tripwires added: no watchlist-only thesis states a price-level trigger except 6857's broken-basis CLOSE. Two tracker-versus-frontmatter drifts surfaced and left for the user: SIVE is `active` in the Watchlist column but `monitoring` / low in its thesis (one windowed row added on the user's instruction, the exclusion note below updated), while META, NFLX, PINS and INTU show `monitoring` in the Watchlist column but are `active` / high theses (META and INTU already carry rows; NFLX and PINS carry none and are outside this pass's scope). Budget: the ticker universe also grew to 97 theses today, so Brave now runs ~97 ticker + ~96 theme queries a day, ~5,800/mo; `brave_budget_mo` 4000 → 6000 (Tuning) so the guard does not silently cut coverage mid-month; GDELT spacing adds ~7 min to the W3 run.

### Custom silicon & compute

| id | query | thesis | expires | status |
|---|---|---|---|---|
| mrvl-fabric | "UALink" OR "NVLink Fusion" OR "ESUN" | [[MRVL - Marvell Technology]] | 2026-10-31 | active |
| mrvl-trainium | "Trainium" AND (Marvell OR Alchip) | [[MRVL - Marvell Technology]] | 2026-12-15 | active |
| rubin-ramp | Nvidia AND ("Vera Rubin" OR Rubin OR Feynman) | [[NVDA - Nvidia]] | 2027-06-30 | active |
| huawei-ascend ⚠ | Huawei AND (Ascend OR "950PR" OR "950DT") | [[NVDA - Nvidia]] | permanent | active |
| openai-xpu | OpenAI AND (XPU OR Broadcom OR "custom chip") | [[AVGO - Broadcom]] | 2027-03-31 | active |
| amd-parity | AMD AND (MI455X OR Helios OR MLPerf OR ROCm) | [[AMD - Advanced Micro Devices]] | 2027-03-31 | active |
| intel-18a | Intel AND ("18A" OR "14A" OR foundry OR EMIB OR "advanced packaging") | [[TSM - Taiwan Semiconductor]] | permanent | active |
| inferencex | InferenceX OR (MLPerf AND (Rubin OR "TPU v7" OR MI455X OR Trainium)) | [[NVDA - Nvidia]] | 2026-12-31 | active |
| avgo-demand | "Tomahawk 6" OR "Tomahawk Ultra" OR "Scale-Up Ethernet" OR (Anthropic AND TPU AND (gigawatt OR GW)) | [[AVGO - Broadcom]] | permanent | active |
| avgo-bear ⚠ | (VMware AND (CISPE OR Siemens OR antitrust OR "price increase")) OR (MediaTek AND (TPU OR "AI ASIC")) | [[AVGO - Broadcom]] | permanent | active |
| amd-commit | AMD AND (gigawatt OR GW OR "take-or-pay" OR renegotiation OR CoWoS OR ROCm) | [[AMD - Advanced Micro Devices]] | 2027-03-31 | active |
| amd-epyc ⚠ | (EPYC OR "Clearwater Forest") AND (share OR "market share" OR Intel OR Venice) | [[AMD - Advanced Micro Devices]] | 2027-12-31 | active |
| cbrs-anchor ⚠ | Cerebras AND (OpenAI OR G42 OR MBZUAI OR export OR lockup OR "lock-up" OR Bedrock OR "WSE-4") | [[CBRS - Cerebras Systems]] | 2027-03-31 | active |

### Foundry & packaging

| id | query | thesis | expires | status |
|---|---|---|---|---|
| tsmc-capex | "TSMC" AND (capex OR "capital expenditure" OR guidance) | [[AI Bubble Risk and Semiconductor Valuations]] | permanent | active |
| tsmc-nodes | TSMC AND (A16 OR Arizona OR N2 OR "2nm") | [[TSM - Taiwan Semiconductor]] | permanent | active |
| cowos | CoWoS | [[TSM - Taiwan Semiconductor]] | permanent | active |
| copos-panel | CoPoS OR "panel-level packaging" | [[CoWoS-to-CoPoS Panel-Level Packaging Transition]] | 2027-12-31 | active |
| glass-substrate ⚠ | "glass substrate" AND (TSMC OR Intel OR Samsung) | [[2802 - Ajinomoto]] | permanent | active |
| abf-hanwha ⚠ | Hanwha AND (ABF OR substrate) | [[2802 - Ajinomoto]] | 2027-09-30 | active |
| abf-demand | (ABF OR "build-up film") AND (Ibiden OR Unimicron OR "Nan Ya" OR Rubin OR EMIB OR shortage OR "price increase") | [[2802 - Ajinomoto]] | permanent | active |

### Memory & storage

| id | query | thesis | expires | status |
|---|---|---|---|---|
| hbm4 | "HBM4" | [[000660 - SK Hynix]] | permanent | active |
| samsung-hbm ⚠ | (Samsung OR Micron) AND (HBM4 OR HBM4E OR "1c DRAM") | [[000660 - SK Hynix]] | 2027-03-31 | active |
| hybrid-bonding | "hybrid bonding" OR Kinex | [[BESI - BE Semiconductor Industries]] | permanent | active |
| nand-cycle ⚠ | NAND AND (pricing OR YMTC OR oversupply OR capex OR "long-term agreement") | [[285A - Kioxia]] | permanent | active |
| hbf-flash | "high bandwidth flash" | [[SNDK - SanDisk]] | permanent | active |
| hbm-test | (Advantest OR Teradyne) AND (HBM OR "wafer test") | [[6857 - Advantest]] | permanent | active |
| hbm-process | "MR-MUF" OR "TC-NCF" OR ("SK hynix" AND "hybrid bonding") OR "16-Hi" | [[000660 - SK Hynix]] | 2027-06-30 | active |
| nvhbm-custom ⚠ | NVHBM OR "custom HBM" OR "HBM base die" | [[000660 - SK Hynix]] | permanent | active |
| skh-moat | Namics OR "M15X" OR (Solidigm AND (IPO OR "carve-out")) | [[000660 - SK Hynix]] | 2027-12-31 | active |
| sndk-lta | SanDisk AND ("long-term agreement" OR LTA OR prepay OR "take-or-pay" OR Stargate OR qualification) | [[SNDK - SanDisk]] | permanent | active |
| kioxia-flow | Kioxia AND ("SK hynix" OR stake OR "US listing" OR TOPIX OR buyback OR BiCS10) | [[285A - Kioxia]] | 2027-06-30 | active |

### Semicap & materials

| id | query | thesis | expires | status |
|---|---|---|---|---|
| tor-selection | ("tool of record" OR "process of record") AND (TSMC OR Samsung) | [[ASMI - ASM International]] | 2027-03-31 | active |
| wfe-china ⚠ | (SMIC OR Naura OR AMEC OR Skyverse OR CXMT) AND (equipment OR inspection OR expansion) | [[KLA - KLA Corporation]] | permanent | active |
| export-controls | ("export control" OR BIS) AND (semiconductor OR chip OR H200) | [[NVDA - Nvidia]] | permanent | active |
| besi-ma | BESI AND (bid OR takeover OR acquisition) | [[BESI - BE Semiconductor Industries]] | 2027-06-30 | active |
| wlbi-test ⚠ | "wafer-level burn-in" OR (Aehr AND (customer OR order OR bookings OR SiPh OR "silicon photonics")) | [[AEHR - Aehr Test Systems]] | 2027-03-31 | active |
| mlcc-ai ⚠ | MLCC AND (AI OR "silicon capacitor" OR Yageo OR SEMCO OR "Samsung Electro-Mechanics") | [[6981 - Murata Manufacturing]] | permanent | active |
| mlcc-008004 ⚠ | ("008004" OR "0201" OR "small-case") AND (MLCC OR Yageo OR Sunlord OR Walsin OR "lead time") | [[6981 - Murata Manufacturing]] | permanent | active |
| lrcx-aether | "Lam Research" AND (Aether OR Akara OR "dry resist" OR "selective etch" OR "tool of record" OR "400-layer") | [[LRCX - Lam Research]] | 2027-10-31 | active |
| wfe-forecast | ("wafer fab equipment" OR WFE) AND (2026 OR 2027) AND (forecast OR billion OR outlook) | [[LRCX - Lam Research]] | 2027-02-28 | active |
| n2-ald-share | (ALD OR "atomic layer deposition") AND (TSMC OR "2nm" OR N2 OR "1.4nm" OR A14 OR Samsung) | [[AMAT - Applied Materials]] | 2027-03-31 | active |
| amat-legs | "Applied Materials" AND (ICAPS OR EPIC OR HBM OR "China" OR AMEC OR Gartner) | [[AMAT - Applied Materials]] | permanent | active |
| kla-metrology ⚠ | ("virtual metrology" OR Skyverse OR Camtek OR Onto) AND (inspection OR "process control" OR TSMC OR SMIC) | [[KLA - KLA Corporation]] | permanent | active |
| asmi-por | ("ASM International" OR ASMI OR Trillium OR "ALTUS Halo") AND ("1.4nm" OR A14 OR HKMG OR dipole OR "process of record" OR ASMPT) | [[ASMI - ASM International]] | 2027-06-30 | active |

### Photonics & optical

| id | query | thesis | expires | status |
|---|---|---|---|---|
| cpo | "co-packaged optics" OR "CPO switch" | [[MRVL - Marvell Technology]] | permanent | active |
| china-optics ⚠ | China AND ("silicon photonics" OR EML OR "optical DSP") | [[LITE - Lumentum]] | permanent | active |
| inp-capacity ⚠ | ("indium phosphide" OR InP) AND (Veeco OR Coherent OR MOCVD) | [[AIXA - Aixtron]] | permanent | active |
| mrvl-celestial | "Celestial AI" OR "Photonic Fabric" | [[MRVL - Marvell Technology]] | 2027-03-31 | active |
| lpo-share ⚠ | (LPO OR "linear pluggable" OR "linear drive") AND (1.6T OR DSP OR "short reach") | [[MRVL - Marvell Technology]] | 2027-06-30 | active |
| lite-ocs | Lumentum AND (OCS OR "optical circuit switch" OR "1.6T" OR "Cloud Light" OR "400G" OR Greensboro) | [[LITE - Lumentum]] | 2027-03-31 | active |
| lite-6inch ⚠ | (Coherent OR Lumentum) AND ("6-inch" OR "six-inch" OR "indium phosphide") AND (yield OR margin OR EML) | [[LITE - Lumentum]] | 2027-06-30 | active |
| aixa-mix | Aixtron AND (optoelectronics OR InP OR "order intake" OR guidance OR "gallium nitride" OR "silicon carbide") | [[AIXA - Aixtron]] | 2027-02-28 | active |
| iqe-inp ⚠ | IQE AND (MACOM OR "indium phosphide" OR InP OR epiwafer OR placing OR "equity raise" OR Taiwan) | [[IQE - IQE]] | permanent | active |
| sive-listing ⚠ | Sivers AND (Nasdaq OR listing OR probe OR "Economic Crime" OR "rights issue" OR placing OR POET) | [[SIVE - Sivers Semiconductors]] | 2026-12-31 | active |

### Software & platforms

| id | query | thesis | expires | status |
|---|---|---|---|---|
| pltr-defense | Palantir AND (Army OR NGC2 OR Maven OR "Enterprise Agreement" OR Navy OR NATO OR Anduril) | [[PLTR - Palantir]] | permanent | active |
| pltr-rivals ⚠ | "Genie Ontology" OR "Fabric IQ" OR "DeployCo" OR "Agent Bricks" OR (ontology AND "write-back") | [[PLTR - Palantir]] | permanent | active |
| pltr-sovereignty ⚠ | Palantir AND (NHS OR sovereignty OR "break clause" OR ChapsVision OR Bundeswehr OR "Ministry of Defence" OR Swiss) | [[PLTR - Palantir]] | 2027-03-31 | active |
| meta-capex | Meta AND (capex OR "Meta Compute" OR "data center") | [[META - Meta]] | permanent | active |
| meta-ai | "Meta AI" AND (engagement OR users OR Superintelligence) | [[META - Meta]] | permanent | active |
| tiktok-ban | TikTok AND (ban OR divestiture OR sale OR "joint venture" OR algorithm OR CFIUS) | [[META - Meta]] | permanent | active |
| net-act4 | Cloudflare AND (crawler OR "pay per crawl" OR x402 OR Googlebot OR Bingbot OR "Content Signals" OR "Monetization Gateway") | [[NET - Cloudflare]] | permanent | active |
| net-sase | Cloudflare AND (Gartner OR SASE) | [[NET - Cloudflare]] | permanent | active |
| net-commoditize ⚠ | (CloudFront OR Akamai OR Fastly OR Vercel) AND (x402 OR "AI crawler" OR "pay per crawl" OR "agent payments") | [[NET - Cloudflare]] | permanent | active |
| hyperscaler-guides | (Microsoft OR Amazon OR Alphabet) AND (capex OR "capital expenditure") AND (guidance OR earnings OR 2027) | [[AI Bubble Risk and Semiconductor Valuations]] | 2027-02-15 | active |
| intu-agentic ⚠ | (OpenAI OR ChatGPT OR Anthropic OR Claude OR Gemini) AND (TurboTax OR "tax filing" OR bookkeeping OR QuickBooks) | [[INTU - Intuit]] | permanent | active |
| uber-av ⚠ | Waymo OR robotaxi | [[UBER - Uber]] | permanent | active |
| agentic-commerce | "agentic commerce" OR "agentic checkout" OR x402 | [[Agentic Internet]] | permanent | active |
| panw-platform | "Palo Alto Networks" AND (XSIAM OR CyberArk OR "next-generation security" OR NGS OR "organic growth" OR Wiz OR platformization) | [[PANW - Palo Alto Networks]] | 2027-02-28 | active |
| now-assist | ServiceNow AND ("Now Assist" OR Armis OR "AI Agent" OR "Context Engine" OR seat OR ACV OR "Service Desk") | [[NOW - ServiceNow]] | 2027-02-28 | active |
| saas-seats ⚠ | ("seat compression" OR "per-seat" OR "seat-based") AND (AI OR agent) AND (SaaS OR software) | [[NOW - ServiceNow]] | permanent | active |
| shop-agentic | Shopify AND (agentic OR "Instant Checkout" OR ChatGPT OR "AI agent" OR "Shopify Payments" OR penetration OR GMV) | [[SHOP - Shopify]] | permanent | active |
| shop-rivals ⚠ | (Stripe AND (storefront OR commerce OR IPO)) OR ("TikTok Shop" AND (US OR ban OR GMV)) | [[SHOP - Shopify]] | permanent | active |
| crcl-coinbase ⚠ | USDC AND (Coinbase OR "revenue share" OR "Open USD" OR "GENIUS Act" OR "CLARITY Act" OR Arc) | [[CRCL - Circle Internet Group]] | 2027-03-31 | active |
| wtc-asic ⚠ | WiseTech AND (ASIC OR White OR DSV OR Tango OR E2open OR "organic growth" OR CargoWise) | [[WTC - WiseTech Global]] | permanent | active |

### Consumer, media & industrial

Active Watchlist names outside the semis / software clusters. None carries a Conviction Triggers section except none at all (SPOT, TTWO, DUOL, GAW, UBER, DE, APP all lack one), so the rows anchor to the 2026-08-15 stress-test kill triggers where one exists (SPOT, GAW, UBER) and otherwise to the dated catalyst the thesis names as its next test.

| id | query | thesis | expires | status |
|---|---|---|---|---|
| spot-ads ⚠ | Spotify AND (advertising OR "ad revenue" OR SAX OR programmatic OR "Music Pro" OR superfan OR "price increase") | [[SPOT - Spotify]] | permanent | active |
| gta6-launch | "GTA VI" OR "GTA 6" OR "Grand Theft Auto VI" | [[TTWO - Take-Two Interactive]] | 2027-03-31 | active |
| duol-platform | Duolingo AND (DAU OR "Duolingo Max" OR chess OR "English Test" OR DET OR "class action" OR investigation) | [[DUOL - Duolingo]] | permanent | active |
| gaw-licensing | ("Games Workshop" OR Warhammer) AND (Amazon OR showrunner OR licensing OR "trading update" OR edition OR "Space Marine") | [[GAW - Games Workshop]] | permanent | active |
| uber-fleet | Uber AND (Avride OR WeRide OR Nuro OR Rivian OR "Delivery Hero" OR "Autonomous Solutions" OR Cybercab) | [[UBER - Uber]] | 2027-12-31 | active |
| deere-autonomy | Deere AND (autonomous OR autonomy OR "See & Spray" OR "early order" OR subscription OR "right to repair" OR tariff) | [[DE - John Deere]] | 2027-02-28 | active |
| applovin-ecom | AppLovin AND (SEC OR "e-commerce" OR "self-serve" OR "Muddy Waters" OR incrementality OR AXON OR OpenAI) | [[APP - AppLovin]] | permanent | active |

Row → observable map. spot-ads: kill trigger is two quarters of ad-revenue decline with subscriber growth under 5% and still no paid superfan tier (Music Pro never launched). gta6-launch: 19 Nov 2026 launch, Online a month later, pre-order volume the first quantitative demand read; the only load-bearing event in the thesis, so the row self-retires after the first full quarter. duol-platform: multi-subject DAU milestones, Max tier past 1.5% of MAU, DET institutional growth, the securities investigation. gaw-licensing: FY26 licensing printed £32.9M (−37%, the HIGH pillar missed); the kill trigger is core growth under 6% with licensing under £30M and still no Amazon production start. uber-fleet: the HIGH-side observable the fired Waymo falsifier leaves open, exclusive non-Waymo paid AVs reaching ≥1,000 units by end-2027 (uber-av ⚠ already carries the Waymo side). deere-autonomy: MY27 early-order and autonomy-kit take-rate, the first quantified precision-ag subscription figure, the FTC settlement's 10-year open-access term. applovin-ecom: SEC investigation resolution, e-commerce self-serve GA, third-party incrementality data against the Muddy Waters claims.

### Neoclouds & AI infrastructure

Book weight with no thematic coverage until 2026-08-27: NBIS Full (25%+) at medium conviction, SPCX High (10–25%) at medium. Both theses carry registered Conviction Triggers and every row below maps to a leg. The NBIS auto ticker query resolves from the filename ("Nebius Group"), so these rows use the bare "Nebius" token; the SpaceX auto query returns the launch firehose, so the SPCX rows carve out the four thesis variables the firehose buries.

| id | query | thesis | expires | status |
|---|---|---|---|---|
| nbis-power | Nebius AND (megawatt OR MW OR gigawatt OR energized OR commissioning OR Philadelphia OR Finland) | [[NBIS - Nebius Group]] | 2027-03-31 | active |
| nbis-funding ⚠ | Nebius AND (convertible OR "asset-backed" OR "secured facility" OR "at-the-market" OR dilution OR "GPU-backed") | [[NBIS - Nebius Group]] | permanent | active |
| nbis-stakes | (ClickHouse OR Avride) AND (IPO OR "S-1" OR secondary OR valuation OR funding) | [[NBIS - Nebius Group]] | permanent | active |
| neocloud-inhousing ⚠ | MTIA OR "Microsoft Maia" OR "Meta Compute" | [[NBIS - Nebius Group]] | permanent | active |
| neocloud-peers ⚠ | (CoreWeave OR Nscale OR Lambda OR Crusoe OR IREN) AND (contract OR gigawatt OR offtake OR Rubin OR pricing) | [[NBIS - Nebius Group]] | permanent | active |
| spcx-csa | (Colossus OR xAI) AND (Anthropic OR Microsoft OR Azure OR "Reflection AI" OR "cloud service" OR offtake OR termination) | [[SPCX - SpaceX]] | permanent | active |
| spcx-nameplate | (Colossus OR Terafab OR xAI) AND (gigawatt OR GW OR turbine OR Memphis OR Southaven OR "Grimes County") | [[SPCX - SpaceX]] | 2027-03-31 | active |
| starlink-churn ⚠ | Starlink AND (price OR churn OR ARPU OR "Amazon Leo" OR Kuiper OR outage) | [[SPCX - SpaceX]] | permanent | active |
| spcx-supply ⚠ | SpaceX AND ("lock-up" OR lockup OR unlock OR "share sale" OR secondary) | [[SPCX - SpaceX]] | 2026-12-31 | active |
| crwv-credit ⚠ | CoreWeave AND (Microsoft OR renewal OR DDTL OR covenant OR Moody's OR DBRS OR refinancing OR dilution) | [[CRWV - CoreWeave]] | permanent | active |
| gpu-rerent | (H100 OR Hopper OR H200) AND ("re-rent" OR "rental rate" OR "per hour" OR "second-hand" OR resale OR "spot price") | [[CRWV - CoreWeave]] | 2027-06-30 | active |

Row → trigger map. nbis-power: HIGH ≥600 MW active at the November Q3 print, LOW >20% miss, CLOSE >30% YE26 miss (Pennsylvania first power is end-2027, so the 2026 build is Finland, New Jersey, Kansas City and leased sites; contracted GW is not the metric). nbis-funding: LOW >15%-dilutive raise in any 6-month window (Mar–Aug 2026 already ~22% on a converted basis, definition pending `/conviction-audit`), CLOSE GPU-collateralised debt as the primary funding source. nbis-stakes: HIGH leg 3, ≥$1B cash proceeds from a ClickHouse or Avride sale (ClickHouse IPO guided 2027 at the earliest, so this leg cannot fire at the Q3 print). neocloud-inhousing: CLOSE if the Meta $15B flexible tranche is amended down or undrawn as MTIA ramps; Microsoft Maia is the other anchor's in-house silicon. neocloud-peers: Nscale's $45B Anthropic Rubin ticket (unlisted) and CRWV's Rubin pricing (OQ-158) compete for the same racks and anchor tenants; peer $/GPU-hour prints are the only public read on the cash rate that sets Rubin ROIC (Insight #6: value destruction below ~$8.22/hr at $183K per GPU). spcx-csa: HIGH a long-duration or matched-cohort CSA print, LOW the first termination cascade, CLOSE D&A lives exceeding demonstrated CSA duration; the rumoured Microsoft 3 GW lease is unverified by either party. spcx-nameplate: HIGH/LOW YE26 ≥2 GW on the same definition as the printed 1.4 GW; Memphis turbines must be removed by 2027; Terafab counts only at tool POs. starlink-churn: LOW Connectivity adj. EBITDA margin below ~55% on churn/ARPU after the 18-June price rise; Amazon Leo commercial start slipped to late-2026. spcx-supply: lock-up tranches into December (~40% tradeable by year-end), position risk not thesis risk, self-retires. crwv-credit: HIGH a flat-to-positive Microsoft renewal in Q3–Q4 2026, LOW a >15% cut / GM below 65% / a negative DDTL outlook, CLOSE a covenant breach or >15% dilution in six months (the $2.6B facility already repriced +100–125bp with a 1.35x DSCR covenant). gpu-rerent: the first Hopper cluster re-rent (Q4 2026–Q1 2027) is the single most informative datapoint for DDTL durability (HIGH ≥70% of the original rate) and the same age-six step that sets NBIS's Rubin ROIC (OQ-195); watched here so the merged neocloud-peers row is not asked to carry it.

### Datacenter power & cooling

| id | query | thesis | expires | status |
|---|---|---|---|---|
| vrt-orders | Vertiv AND (orders OR backlog OR organic OR margin OR "liquid cooling" OR OCP) | [[VRT - Vertiv Holdings]] | 2027-03-31 | active |
| vrt-cooling ⚠ | ("liquid cooling" OR "direct-to-chip" OR "immersion cooling") AND (Nvidia OR Meta OR Google OR Microsoft OR "reference design" OR acquisition) | [[VRT - Vertiv Holdings]] | permanent | active |
| vicr-vpd | Vicor AND (Rubin OR "vertical power" OR VPD OR licensing OR "Federal Circuit" OR PTAB OR "Monolithic Power" OR Vinciarelli OR Andover) | [[VICR - Vicor Corporation]] | 2027-06-30 | active |
| 800vdc | "800VDC" OR "800 VDC" OR "800V DC" OR "800-volt" | [[800VDC Adoption]] | permanent | active |

Row → trigger map. vrt-orders: HIGH Q2–Q4 2026 organic orders >50% with liquid-cooling share >35%, LOW two consecutive quarters of negative organic orders or margin under 21%; OCP Global Summit (Oct 2026) publishes the next liquid-cooling standards. vrt-cooling: the CLOSE leg (NVIDIA acquires a liquid-cooling company or ships DGX-integrated thermal management) and the LOW leg (a hyperscaler proprietary cooling reference architecture against Vertiv 360AI). vicr-vpd: HIGH Vera Rubin NVL144 confirms Vicor VPD content plus licensing above $300M and product GM above 50%; LOW the Federal Circuit narrows LEO scope or Rubin Ultra lists Flex / MPS / TI as primary; CLOSE founder departure without an equity-aligned successor, PTAB invalidation, or an MPS clean-sheet vertical PDN. 800vdc: the architecture transition that re-maps the rack power BOM (VICR, VRT, 6981, NVDA); anchored to the macro note, 800VDC GA is the October OCP observable.

**Deliberately excluded** (no silent caps): draft-status theses (33 as of 2026-08-27; no settled questions yet) except NBIS, where the Full (25%+) Live Portfolio weight overrides draft status and the rows anchor to its registered Conviction Triggers (the thesis itself is still `draft` at Full weight; a `/status NBIS draft→active` decision is open and Tier-3, the user's call); EINK dedicated rows (monitoring/low-conviction with slow-moving observables — the weekly per-ticker sweep covers them; SIVE's prior exclusion on the same grounds was lifted 2026-08-27 on the user's instruction to cover every Watchlist-`active` name, with one row windowed to the YE2026 Nasdaq-listing / probe window because the thesis itself is still `monitoring` / low); NFLX and PINS (`active` / high theses that the Watchlist column still marks `monitoring`, so outside the 2026-08-27 Watchlist pass; fix the tracker column or add rows at the next review); a generic *permanent* "AI capex" row (tsmc-capex + meta-capex triangulate the regime variable — the third leg, the taiwan-odm poller, is unbuilt backlog, so the windowed hyperscaler-guides row, now running to 2027-02-15, covers the Q3 CY26 prints and the FY27 guides until it exists or the window lapses); a Starship-cadence row (orbital compute is a 2029+ option and the SpaceX auto query already carries every flight); dedicated rows for Medium/Low-weight names whose theses have no registered Conviction Triggers (NVDA, NET, AVGO, SNDK, 285A) beyond the observables above, because a watch with no trigger to test is noise waiting to happen.

## Outlet Feeds (Workflow 3 unified — LIVE)

Whole-outlet RSS pulls — the firehose complement to the query-scoped News & Thematic watches above. **Live since the unified Workflow 3 build** (header said IN BUILD until 2026-07-27 — stale; the Plan node parses this section every run): outlet feeds + FMP ticker news + GN/GDELT/Brave over every ticker and theme → dedupe → headline triage → defuddle body fetch for survivors → body re-score (Lane A) → story clustering → presentation gate (full entry only at final score ≥ `brief_min`, links-only tail below it — 2026-08-27) → digest-LLM-summarised daily intel brief (`digest_model` cell, currently x-ai/grok-4.6 via OpenRouter; all source links per story) in `Daily Intel/`; **no `_Inbox/` deposits** (Lane C reverted 2026-07-20). Each block's `###` heading (parenthetical stripped) becomes its grouping header in the brief — rename a heading here and the brief's sections follow; the `cluster` column stays as metadata/fallback for rows outside any `###` block. Add/pause/delete rows freely — a row is one line, effective next sweep.

Schema notes:
- `cluster` — scope tag (outlets span names, so no per-thesis anchor). Orphan discipline still applies at cluster level: a cluster with no live vault question is noise.
- `vol` — estimated items/day band: `hi` ≥20 · `med` 5–20 · `lo` <5.
- `triage: yes` — Haiku relevance-scores items before digest inclusion (mandatory for `hi` feeds). `no` — every item passes through (low-volume quality sources; a new post is worth seeing regardless of score).
- All feed URLs verified live 2026-07-20 (fetched, XML confirmed, freshness checked). Source: bookmarks audit, `_Inbox/bookmarks_20_07_2026.html`.
- Body-exempt feeds (paywalled bodies or aggregator-permalink links): listed in `### Tuning → body_exempt` below — headline-only in the digest, never body-fetched. Access handled at `/ingest` time.
- CN-language feeds: 36kr, leiphone — triage model reads Chinese.
- `hn` row is third-party hnrss.org (points-filtered proxy; official `news.ycombinator.com/rss` is unfiltered). `fs` row is the legacy farnamstreetblog.com domain — works, redirect-stable.

### Semis / hardware / datacenter

| id | feed_url | cluster | vol | triage | expires | status |
|---|---|---|---|---|---|---|
| semiengineering | https://semiengineering.com/feed/ | semis | med | no | permanent | active |
| semiwiki | https://semiwiki.com/feed/ | semis | lo | no | permanent | active |
| servethehome | https://www.servethehome.com/feed/ | semis | lo | no | permanent | active |
| nextplatform | https://nextplatform.com/feed | semis | lo | no | permanent | active |
| semiaccurate | https://www.semiaccurate.com/feed/ | semis | lo | no | permanent | active |
| tomshardware | https://www.tomshardware.com/feeds.xml | semis | hi | yes | permanent | active |
| wccftech | https://wccftech.com/feed | semis | hi | yes | permanent | active |
| digitimes | https://www.digitimes.com/rss/daily.xml | semis | hi | yes | permanent | active |
| eetasia | https://eetasia.com/feed | semis | med | no | permanent | active |
| dcd | https://www.datacenterdynamics.com/rss/ | datacenter | med | yes | permanent | active |
| dck | https://datacenterknowledge.com/rss.xml | datacenter | med | no | permanent | active |
| nvidia-dev | https://news.developer.nvidia.com/feed | semis | lo | no | permanent | active |
| gfxspeak | https://gfxspeak.com/blog/feed | semis | lo | no | permanent | active |

### Strategy essays & newsletters

| id | feed_url | cluster | vol | triage | expires | status |
|---|---|---|---|---|---|---|
| stratechery | https://stratechery.com/feed | essays | lo | no | permanent | active |
| ben-evans | https://www.ben-evans.com/benedictevans?format=rss | essays | lo | no | permanent | active |
| thediff | https://www.thediff.co/feed | essays | lo | no | permanent | active |
| netinterest | https://netinterest.substack.com/feed | essays | lo | no | permanent | active |
| thegeneralist | https://thegeneralist.substack.com/feed | essays | lo | no | permanent | active |
| thenonconsensus | https://thenonconsensus.substack.com/feed | essays | lo | no | permanent | active |
| turner | https://turner.substack.com/feed | essays | lo | no | permanent | active |
| venturedesktop | https://venturedesktop.substack.com/feed | essays | lo | no | permanent | active |
| mule | https://mule.substack.com/feed | essays | lo | no | permanent | active |
| hhhypergrowth | https://hhhypergrowth.com/rss/ | essays | lo | no | permanent | active |
| platformonomics | https://platformonomics.com/feed/ | essays | lo | no | permanent | active |
| kwokchain | https://kwokchain.com/feed/ | essays | lo | no | permanent | active |
| reactionwheel | https://reactionwheel.net/feed | essays | lo | no | permanent | active |
| danwang | https://danwang.co/feed/ | essays | lo | no | permanent | active |
| andrewbatson | https://andrewbatson.com/feed/ | china-econ | lo | no | permanent | active |
| collabfund | https://collaborativefund.com/feed | essays | lo | no | permanent | active |
| fs | https://www.farnamstreetblog.com/feed/ | essays | lo | no | permanent | active |
| caseyhandmer | https://caseyhandmer.wordpress.com/feed/ | energy | lo | no | permanent | active |
| thegradient | https://thegradient.pub/rss/ | ai | lo | no | permanent | active |

### Value / finance / macro blogs

| id | feed_url | cluster | vol | triage | expires | status |
|---|---|---|---|---|---|---|
| damodaran | https://aswathdamodaran.blogspot.com/feeds/posts/default | value | lo | no | permanent | active |
| lt3000 | https://lt3000.blogspot.com/feeds/posts/default | value | lo | no | permanent | active |
| footnotesanalyst | https://www.footnotesanalyst.com/feed/ | value | lo | no | permanent | active |
| calculatedrisk | https://www.calculatedriskblog.com/feeds/posts/default | macro | med | no | permanent | active |
| marginalrevolution | https://marginalrevolution.com/feed | macro | med | yes | permanent | active |
| glineq | https://glineq.blogspot.com/feeds/posts/default | macro | lo | no | permanent | active |
| awocs | https://awealthofcommonsense.com/feed/ | value | lo | no | permanent | active |
| stockgumshoe | https://stockgumshoe.com/feed | value | lo | no | permanent | active |
| acquirersmultiple | https://acquirersmultiple.com/feed/ | value | lo | no | permanent | active |
| hellerhs | https://www.hellerhs.com/blog-feed.xml | value | lo | no | permanent | active |
| rvcapital | https://www.rvcapital.ch/blog-feed.xml | value | lo | no | permanent | active |
| oakmark | https://oakmark.com/feed | value | lo | no | permanent | active |
| philecon | https://www.philosophicaleconomics.com/feed/ | macro | lo | no | permanent | active |

### Major outlets (headline scanning surfaces)

| id | feed_url | cluster | vol | triage | expires | status |
|---|---|---|---|---|---|---|
| zerohedge | https://cms.zerohedge.com/fullrss2.xml | macro | hi | yes | permanent | active |
| ft-home | https://www.ft.com/rss/home | macro | hi | yes | permanent | active |
| bbg-tech | https://feeds.bloomberg.com/technology/news.rss | tech-news | hi | yes | permanent | active |
| bbg-econ | https://feeds.bloomberg.com/economics/news.rss | macro | med | yes | permanent | active |
| bbg-markets | https://feeds.bloomberg.com/markets/news.rss | macro | hi | yes | permanent | active |
| wsj-markets | https://feeds.content.dowjones.io/public/rss/RSSMarketsMain | macro | med | yes | permanent | active |
| wsj-tech | https://feeds.content.dowjones.io/public/rss/RSSWSJD | tech-news | med | yes | permanent | active |
| wsj-business | https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness | macro | med | yes | permanent | active |
| econ-finance | https://www.economist.com/finance-and-economics/rss.xml | macro | lo | yes | permanent | active |
| econ-business | https://www.economist.com/business/rss.xml | macro | lo | yes | permanent | active |
| nyt-business | https://rss.nytimes.com/services/xml/rss/nyt/Business.xml | macro | med | yes | permanent | active |
| nyt-tech | https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml | tech-news | med | yes | permanent | active |

### China / Asia

| id | feed_url | cluster | vol | triage | expires | status |
|---|---|---|---|---|---|---|
| scmp-tech | https://www.scmp.com/rss/318208/feed | china-tech | med | yes | permanent | active |
| technode | https://technode.com/feed/ | china-tech | lo | no | permanent | active |
| pandaily | https://pandaily.com/feed | china-tech | med | yes | permanent | active |
| 36kr | https://36kr.com/feed | china-tech | hi | yes | permanent | active |
| leiphone | https://leiphone.com/feed | china-tech | med | yes | permanent | active |
| walkthechat | https://walkthechat.com/feed/ | china-tech | lo | no | permanent | active |

### Industry publications (non-vault sectors — cross-industry sensing)

| id | feed_url | cluster | vol | triage | expires | status |
|---|---|---|---|---|---|---|
| freightwaves | https://freightwaves.com/feed | logistics | hi | yes | permanent | active |
| theloadstar | https://theloadstar.com/feed/ | logistics | med | no | permanent | active |
| supplychaindive | https://www.supplychaindive.com/feeds/news/ | logistics | lo | no | permanent | active |
| ttnews | https://www.ttnews.com/rss.xml/ | logistics | med | yes | permanent | active |
| gamesindustry | https://www.gamesindustry.biz/feed | media | med | yes | permanent | active |
| musically | https://musically.com/feed/ | media | lo | no | permanent | active |
| midia | https://www.midiaresearch.com/rss/blog.xml | media | lo | no | permanent | active |
| musicindustryblog | https://musicindustryblog.wordpress.com/feed/ | media | lo | no | permanent | active |
| mediagazer | https://mediagazer.com/feed.xml | media | hi | yes | permanent | active |
| grocerydive | https://www.grocerydive.com/feeds/news/ | food-retail | lo | no | permanent | paused |
| fooddive | https://www.fooddive.com/feeds/news/ | food-retail | lo | no | permanent | paused |
| hngry | https://www.hngry.tv/articles/rss/ | food-retail | lo | no | permanent | paused |
| skift-table | https://table.skift.com/feed | food-retail | lo | no | permanent | paused |
| adamas | https://adamasintel.com/feed | ev-battery | lo | no | permanent | paused |
| socialmediatoday | https://www.socialmediatoday.com/feeds/news/ | ad-social | med | no | permanent | active |
| sparktoro | https://sparktoro.com/blog/feed | ad-social | lo | no | permanent | active |

*Paused 2026-07-26: `food-retail` cluster (grocerydive, fooddive, hngry, skift-table) + `ev-battery` (adamas) — no live vault question anchors either cluster (orphan-cluster discipline above). Re-enable when a thesis lands there. Also this date: marginalrevolution + pandaily flipped to `triage: yes` — both produced only score-0/1 filler in the 07-25/07-26 briefs.*

### General tech news

| id | feed_url | cluster | vol | triage | expires | status |
|---|---|---|---|---|---|---|
| techmeme | https://www.techmeme.com/feed.xml | tech-news | hi | yes | permanent | active |
| techcrunch | https://techcrunch.com/feed/ | tech-news | hi | yes | permanent | active |
| theverge | https://theverge.com/rss/index.xml | tech-news | hi | yes | permanent | active |
| venturebeat | https://venturebeat.com/feed | tech-news | hi | yes | permanent | active |
| wired | https://www.wired.com/feed/rss | tech-news | med | yes | permanent | active |
| zdnet | https://zdnet.com/rss.xml | tech-news | hi | yes | permanent | active |
| techrepublic | https://www.techrepublic.com/feed/ | tech-news | med | yes | permanent | active |
| siliconangle | https://siliconangle.com/feed/ | tech-news | med | yes | permanent | active |
| networkworld | https://www.networkworld.com/feed/ | tech-news | lo | no | permanent | active |
| diginomica | https://diginomica.com/feed | tech-news | med | no | permanent | active |
| datamation | https://www.datamation.com/feed/ | tech-news | lo | no | permanent | active |
| theinformation | https://theinformation.com/feed | tech-news | med | yes | permanent | active |
| hn | https://hnrss.org/frontpage?points=200 | tech-news | med | yes | permanent | active |
| daringfireball | https://daringfireball.net/feeds/main | tech-news | med | no | permanent | active |
| allthingsdistributed | https://allthingsdistributed.com/atom.xml | tech-news | lo | no | permanent | active |

### Tuning (body pipeline — Workflow 3 unified)

Parsed every run like the X Watchers Tuning table: edit a value, the next run complies — no redeploy. Code keeps identical fallback defaults for missing/malformed rows. (`clip_min`/`max_clips_day` removed 2026-07-20 — Lane C reverted, no `_Inbox/` deposits.)

| param | value | notes |
|---|---|---|
| triage_min | 8 | headline-triage gate — items below are dropped; `triage: no` rows bypass scoring entirely. 7 → 8 on 2026-08-28: GLM-5.2 scores ~1 point more generously than Sonnet 5 on the same rubric (admitted 533 → 732 → 1,020 on like-for-like fetch volumes after the OpenRouter switch); 8 on the GLM scale ≈ 7 on the Sonnet scale |
| triage_model | z-ai/glm-5.2 | headline triage (0–10 scoring vs injected coverage list) — OpenRouter switch 2026-08-27 (was claude-sonnet-5): top open-weights model on the AA index at $0.40/$1.27 per MTok; calls route via openrouter.ai with `data_collection: deny` (ZDR hosts only) |
| cluster_model | claude-opus-5 | ⚠ DEPRECATED 2026-07-23 — the Opus LLM cluster call was **removed**; semantic same-story + cross-run repeat detection now runs on **embeddings** (see `embed_model`) BEFORE the body pipeline, so duplicates never reach Opus rescore (that was the cost driver: ~$10–12/run, mostly rescoring dupes). Row kept for rollback only (n8n Automations §12 changelog); unused by the live pipeline |
| rescore_model | z-ai/glm-5.2 | body-informed re-score (Lane A) — reads full article text and sets final ranking. OpenRouter switch 2026-08-27 (was claude-opus-5): ~$1–2/mo at GLM rates; ZDR-pinned. Step-up if scoring quality slips: x-ai/grok-4.6 |
| digest_model | x-ai/grok-4.6 | analytical brief layer — reads merged excerpts, writes decision-useful analysis with coverage implications (rule-2 rewrite 2026-07-21, trail n8n Automations §11). OpenRouter switch 2026-08-27 (was claude-opus-5): frontier-parity judgement seat at $2/$6 per MTok, ~$2–5/mo post-gate; step-down z-ai/glm-5.2, open-weights alternative moonshotai/kimi-k3; prompt: `#### digest_prompt` in ### Prompts below (registry-editable) |
| body_exempt | digitimes, ft-home, bbg-tech, bbg-econ, bbg-markets, wsj-markets, wsj-tech, wsj-business, econ-finance, econ-business, nyt-business, nyt-tech, theinformation, techmeme, mediagazer | paywalled bodies or aggregator permalinks — headline-only, never body-fetched |
| catalyst_window_d | 10 | catalyst proximity markers — stories on tickers with a `_catalyst.md` event within ±N days get a 📅 T-N tag in the brief |
| max_age_d | 3 | hard age cap — items with a parseable publish date older than N days are dropped at Normalize (counted as `stale` in the funnel); GN search queries also carry `when:Nd` so old relevance-ranked hits never arrive |
| triage_min_pw | 9 | stricter admit bar for paywalled items (flagged `pw` at Normalize) — headline must be material on its own; normal items use triage_min |
| brief_min | 9 | presentation gate (2026-08-27) — full digest-LLM analysis + full brief entry only at final (rescored) score ≥ this; the headline triage_min stays the recall gate, this is the precision gate. 8 → 9 on 2026-08-28: GLM-5.2's rescore scale is inflated vs Opus (≥8 share 21% → 61%, ≥9 share 2% → 22% on the 08-28 run), so 9 on the GLM scale ≈ 8 on the Opus scale — targets ~80–110 full stories/day once dedup runs |
| brief_tail_min | 8 | links-only tail floor — stories scoring ≥ this but < brief_min render as one-line title+link entries in "Below the bar" (no digest-LLM spend); below this, cut from the brief entirely (kept in the .data log for /surface & /retro). 7 → 8 with the 2026-08-28 GLM-scale recalibration |
| brief_tail_max | 50 | tail length cap, highest scores first — overflow counted in the funnel line and retained in the .data log |
| tg_max_msgs | 10 | Telegram fan-out — top-N stories by score, ONE message each (full summary + link; last message carries the brief footer + failure count). Telegram same-chat flood limit is ~1 msg/s — if the Notify node starts collecting 429s, lower this |
| tg_per_subject | 2 | Telegram diversity cap — at most N messages per ticker/theme, so one busy subject (a microcap in the news) can't fill the glance. Raise to allow more per subject, set 1 for maximum spread |
| dedup_ttl_d | 3 | card-12 dedup memory window (static-data store) — a URL OR headline seen within N days is dropped as a repeat. "Non-repeats past N days." **Keep small** (static data reloads every run; do NOT set 30 — see track_window_d for long-horizon tracking). Should be ≥ max_age_d so an article can't re-brief within its own eligible life |
| merge_jaccard | 0.42 | SumPrep within-run near-dup merge threshold (token overlap) — now a **backstop** behind the embeddings layer (catches any same-story pair the vectors missed). LOWER = more aggressive merging of same-event headlines into one story. 0.42 default; drop toward 0.35 if twins persist, raise toward 0.55 if unrelated stories get merged |
| embed_model | voyage-4-lite | semantic-dedup embedder (Voyage) — embeds each admitted item's title+snippet, cosine-clusters same-story dupes into ONE representative **before** the body pipeline so duplicates never get body-fetched or rescored. `voyage-4-lite` = $0.02/M tok with **200M free tok/account** (≈2+ yrs free at this volume); `voyage-4` ($0.06/M) is the quality step-up. Replaces the deprecated `cluster_model`. Requires the `Voyage` n8n credential (n8n Automations §5.1) |
| sim_threshold | 0.83 | cosine ≥ this among NEW items = same story → merged to one representative (all source links preserved). **The primary repeat-suppression dial**: RAISE toward 0.90 if distinct stories get merged; LOWER toward 0.82 if the same event still shows twice. 0.86 → 0.83 on 2026-08-27: same-event different-wording pairs (YMTC IPO 2×, Vera Rubin production 2×, AMI order 2×, COHR SiC 2×) survived 0.86 |
| repeat_threshold | 0.88 | cosine of a NEW item vs a PRIOR briefed story (last `story_memory_days`) ≥ this = follow-up → ♻ links-only section, never re-summarised. Set higher than `sim_threshold` so only near-identical reruns divert |
| embed_max_chars | 1000 | chars of title+snippet fed to the embedder per item — enough for same-story judgement; more just spends tokens |
| track_min_score | 8 | sentiment-tracking relevance floor — `/surface`'s 30-day story-log read counts only stories at/above this final score (since 2026-08-27 the brief itself full-briefs only ≥ brief_min, so the two bars currently coincide; this row still governs the long-horizon trend view independently) |
| track_window_d | 30 | how many days of `.data/news_stories/` logs `/surface` reads for sentiment/coverage tracking. Disk files, not DB — 30 days ≈ 12 MB of plain JSON, trivial. Distinct from story_memory_days (repeat-detection window, stays 3–7) |
| paywall_domains | bloomberg.com, wsj.com, ft.com, economist.com, nytimes.com, theinformation.com, barrons.com | URL-level paywall detection for Brave/GDELT/FMP arrivals — combines with the body_exempt feed ids; pw items skip body-fetch and carry 🔒 in the brief |
| story_memory_days | 7 | cross-run story memory window — briefed stories from the last N days ride into the cluster call; follow-up coverage adding no new facts lands in the brief's ♻ links-only section instead of being re-summarised |
| gdelt_spacing_s | 12 | Wait between GDELT queries. Limiter is 1 req/5s **plus a sticky cooldown that trips after ~4 rapid calls** (re-verified 2026-07-23: even 20s spacing 429'd the 5th call) — 8s was too tight, most of a 110-query run 429'd → returned nothing. 12s gives headroom; the durable fix if GDELT is still weak is fewer queries (see n8n Automations §12.1 GDELT rows / thematic-only Plan option) |
| brave_budget_mo | 6000 | monthly query guard — paid metered tier (2026-07-20); was ≈3,000/mo at ~70 tickers + ~40 themes; 3500 → 4000 on 2026-08-27 for the +21 Live-Portfolio rows, then → 6000 the same day after the second pass: 97 thesis tickers + ~96 theme rows ≈ 193 queries/day ≈ 5,800/mo. Pare back by pausing rows here, not by lowering the guard (a tripped guard drops coverage silently for the rest of the month) |

### Prompts (Workflow 3 unified)

Each `####` block below is the live prompt for one LLM stage — edit freely in Obsidian; the workflow re-reads them every run, no n8n touch required. Rules: **keep the required tokens** — they substitute at runtime (`{items}` = batch payload · `{prior}` = prior-story list · `{tickers}` = coverage tickers · `{themes}` = live research questions · `{context}` = the optional `#### brief_context` block below, digest only); a missing *required* token reverts that stage to the code fallback in §5.3 card 5 (required: triage/rescore/digest `{items}` · cluster `{items}` + `{prior}`). Don't start a line with `#` inside a prompt (terminates the block) and keep the trailing "Return ONLY…" clause — the parsers depend on that output shape. `#### brief_context` is freeform standing priorities for the summariser — your analytical steering wheel; edit or blank it freely, no tokens required.

#### triage_prompt
You score news items for one investor. Coverage tickers: {tickers}. Live research questions: {themes}. Clusters also covered: semis, datacenter, china-tech, macro, AI, futurism, tech philosophy, consumer tech. Score each item 0-10 on NEW information value to this coverage: 9-10 directly material new fact (guidance, capacity, pricing, regulatory, primary technical disclosure); 7-8 clearly relevant development; 4-6 adjacent context; 0-3 noise — listicles, price-target roundups, "stocks to buy", rehash, sponsored. Judge information content, not sentiment. Items flagged pw:1 are paywalled — only the headline is readable; hold them to a stricter bar: 8-10 only if the headline alone discloses a material new fact for this coverage, otherwise 0-3. If an item's title (t) is not in English, add "t_en": a faithful English translation of the headline only (≤ 20 words; drop any trailing " - Publisher" suffix); omit t_en for English titles. Items: {items} — Return ONLY a JSON array [{"i":0,"s":7,"t_en":"..."},...] covering every item (t_en only where translated).

#### rescore_prompt
Re-score these news items 0-10 for NEW information value to an investor covering: {tickers}. Live research questions: {themes}. Each item carries its headline score (hs, may be null for auto-admitted sources) and an article excerpt (x). Confirm the article delivers substance — new numbers, primary quotes, disclosed specifics. Downgrade rehash/opinion; upgrade if the body reveals material specifics the headline undersold. Items flagged pw:1 are paywalled (excerpt is headline-grade only) — keep them high only if that alone is materially new. Items: {items} — Return ONLY a JSON array [{"i":0,"s":7},...] covering every item.

#### cluster_prompt
NEW ITEMS are news items from today, from multiple sources; each carries its headline (t) AND a content excerpt (x). PRIOR STORIES were already briefed to the reader on previous days (label, title, summary). Judge same-story on the EXCERPT's substance — the actors, action, and event it describes — NOT on headline wording; two articles with completely different headlines by different authors are the same story if their excerpts describe the same event. Two tasks. (1) Group NEW items that cover the SAME underlying story or event into clusters. Two items are the same story when they report the same actor + action + timeframe (the same announcement, filing, decision, result, or incident), even if headlines emphasize different aspects, figures, or reactions — multiple outlets covering one event is ONE cluster. Keep items separate only when the underlying events genuinely differ (different actors, different actions, or clearly distinct developments). (2) A NEW item that is follow-up coverage of a PRIOR story AND adds no material new facts beyond that story's summary is a repeat — list it under repeats with the prior label. If it ADVANCES the story (new numbers, official responses, next-step events, a material escalation), it is NOT a repeat — cluster it as new. Bias toward repeat: same event with no NEW specific (a number, a named actor, an official action) beyond the prior summary is a repeat even if the wording, outlet, or angle differs — when torn between repeat and new, choose repeat. NEW ITEMS: {items} PRIOR STORIES: {prior} — Return ONLY JSON: {"clusters":[[indices]],"repeats":[[itemIndex,"P<n>"],...]} with every NEW item index appearing exactly once across clusters and repeats.

#### digest_prompt
You write a daily intelligence brief for one investor. Coverage tickers: {tickers}. Live research questions: {themes}. Each item is one story, possibly reported by several sources (srcs) with merged excerpts. For each item write "sum": 2-5 sentences of decision-useful analysis. Lead with the concrete NEW facts — numbers with the comparison that gives them meaning (vs prior guidance, consensus, rivals), named actors, the mechanism of what changed, and stated timelines or next dates. Then state what it means for the coverage: which ticker or research question it touches and the transmission path (pricing power, capacity, share shift, cost curve, regulation, demand signal), and what would confirm or refute that read. Ground every claim in the provided text; label inference explicitly ("implies", "suggests", "if X then Y"). Where sources disagree on a figure, say so. Some items carry sig — the investor's live signals for the tickers involved (catalyst proximity, crowd sentiment); weave these into the implication when they sharpen it. Standing investor context: {context}. If the text is thin or navigation junk, one sentence restating the headline claim. Items: {items} — Return ONLY a JSON array [{"i":0,"sum":"..."},...] covering every item.

#### brief_context
Live book (Holdings table 2026-08-25): PLTR and NBIS Full (25%+); 000660 and SPCX High (10–25%); NVDA, NET, AVGO, MRVL Medium; SNDK, 285A, 6857 Low. Priorities in weight order: NBIS energised MW versus contracted GW, the funding mix (customer prepay versus converts, ATM equity, GPU-backed debt) and any disclosed Rubin cash rate or contract coverage ahead of the November Q3 print; SPCX Cloud Service Agreement duration versus GPU and turbine depreciation lives, YE26 nameplate on the 1.4 GW definition, Starlink ARPU and churn after the June price rise, lock-up supply; PLTR US-commercial growth holding at or above 100% with RDV up quarter on quarter, any named displacement to Genie Ontology, Fabric IQ or a frontier-lab DeployCo, sovereignty contagion beyond the NHS break clause; 000660 Samsung's share of Rubin HBM4, the NVHBM custom base-die axis, MR-MUF versus TC-NCF on shipping HBM4 cubes, the Namics EMC renewal; hyperscaler Q3 CY26 capex prints (late October) read against the July reset, then the FY27 guides; custom-silicon share versus Nvidia (AVGO Jalapeño, Anthropic TPU gigawatts, Tomahawk; MRVL Google seat, Trainium 3 allocation, Celestial tape-out; the InferenceX Q3 benchmark); memory take-or-pay and LTA floors (SanDisk's $93.9B NBM, Kioxia's 2027–28 POs) against the Goldman oversupply path; Cloudflare Act IV revenue and the 15 September crawler deadline versus AWS CloudFront commoditisation; HBM4 test time per stack for Advantest. Outside the book, keep the bear-watches on Intuit (frontier-lab agents in tax and bookkeeping) and Uber (Waymo direct apps), and read the researched-but-not-held names against their own falsifiers: the semicap tool-of-record dipole (Lam Aether and Akara, Applied versus ASM at N2 and A14, KLA versus virtual metrology), CoreWeave's Microsoft renewal and the first Hopper re-rent, Vertiv orders against any hyperscaler proprietary cooling design, the Coinbase–Circle revenue-share renegotiation, WiseTech's ASIC and DSV overhangs, Games Workshop's Amazon production start, and GTA VI pre-orders into the 19 November launch. Prefer specific implications for covered names over generic sector commentary. Flag anything that looks like an inflection-point datapoint rather than incremental news.

## Price Tripwires (Workflow 1)

n8n batch-quotes these tickers daily and pings when a level is breached. A breach means *read the thesis trigger block* — never an execution signal.

| id | ticker | direction | level | thesis | status |
|---|---|---|---|---|---|
| mrvl-bear | MRVL | below | 163 | [[MRVL - Marvell Technology]] | active |
| mrvl-bull | MRVL | above | 330 | [[MRVL - Marvell Technology]] | active |
| pltr-bear | PLTR | below | 127 | [[PLTR - Palantir]] | active |
| pltr-bull | PLTR | above | 200 | [[PLTR - Palantir]] | active |
| nbis-bear | NBIS | below | 175 | [[NBIS - Nebius Group]] | active |
| nbis-bull | NBIS | above | 300 | [[NBIS - Nebius Group]] | active |
| skh-bear | 000660.KS | below | 1200000 | [[000660 - SK Hynix]] | active |
| skh-bull | 000660.KS | above | 2300000 | [[000660 - SK Hynix]] | active |
| spcx-bear | SPCX | below | 105 | [[SPCX - SpaceX]] | active |
| spcx-bull | SPCX | above | 226 | [[SPCX - SpaceX]] | active |

*Revised 2026-08-27 against the Live Portfolio (spot 2026-08-25). MRVL re-levelled: the old above-210 line had been breached since mid-August (spot $242.87) and would have pinged every morning; the new lines are the 29-July capex-reset trough ($163.40: a retest says the July derate was regime, not digestion, so re-read LOW legs 1 and 4) and the pre-July peak (~$330: a reclaim with HIGH still at one of three legs is multiple, not triggers). Added the four largest weights, each level mapped to its thesis trigger block. PLTR $127 (the mid-July pre-Q2 level: giving back the whole Q2 re-rate repeats the June pattern, the process/sizing → MEDIUM leg) and $200 (above the ~$196 ATH at ~49x forward revenue: the quality-but-priced check at Full weight). NBIS $175 (DA Davidson's low target: the market pricing a build slip before the November print, re-read LOW) and $300 (June ATH reclaim, below the $313 convert strike: Full weight versus medium conviction with no active-MW disclosure, OQ-197). 000660 ₩1,200,000 (a further −28%, the Kioxia-style flows de-rate reaching the HBM leader: re-read LOW, Samsung >35% Rubin share plus HBM ASP −10%) and ₩2,300,000 (the late-May peak region, three-month return −27%: HIGH needs the Q3 Rubin allocation print, not price). SPCX $105 (the 52-week low and −11% capex-print low, the IPO base breaking: re-read LOW termination-cascade and lock-up supply) and $226 (52-week high reclaim: the tape paying the 10 GW aspiration as pipeline, position for the CSA-duration disclosure). KRX symbol as the Live Portfolio fetches it (`000660.KS`, KRW levels); confirm `batch-quote-short` returns it on the first run, a "no quote" line in Telegram is the tell. Medium/Low weights deliberately without tripwires: NVDA, NET, AVGO, SNDK and 285A have no registered Conviction Triggers to map a level to; 6857's own CLOSE price leg (¥10,000) sits on a broken price basis (spot ¥34,450) and needs re-anchoring in the thesis before a tripwire means anything.*

## Alt-Data Pollers (backlog)

The row is an on/off + expiry switch; the fetch logic would be bespoke per source (no consuming workflow is currently built). A future poller checks this table first and skips if its row is paused/expired/absent.

> **Status 2026-07-17: deferred — no pollers are built.** These rows are the *vetted build backlog* (each already carries its observable → source reasoning below), not live coverage. Revive one at a time when a thesis binary makes its leading indicator worth ~1 h of build + standing maintenance. Each row names the thesis observable it *leads* — the identification chain (observable → leading indicator → public machine-readable source) is research output, not n8n output. Build order: API-grade sources first (zero scrape fragility), TWSE MOPS monthlies second (structured disclosures), scrapes last.

| id | source | thesis | expires | status |
|---|---|---|---|---|
| tsmc-rev | tsmc-monthly-revenue | [[AI Bubble Risk and Semiconductor Valuations]] | permanent | active |
| celestial-hiring | greenhouse:celestialai | [[MRVL - Marvell Technology]] | 2027-01-31 | active |
| usaspending-pltr | usaspending-api:recipient-Palantir | [[PLTR - Palantir]] | permanent | active |
| bis-fedreg | federalregister-api:BIS-EAR-semiconductor | [[AMAT - Applied Materials]] | permanent | active |
| alchip-monthly | mops:3661-monthly-revenue | [[MRVL - Marvell Technology]] | permanent | active |
| taiwan-odm | mops:2382+6669-monthly-revenue | [[NVDA - Nvidia]] | permanent | active |
| ase-monthly | mops:3711-monthly-revenue | [[TSM - Taiwan Semiconductor]] | permanent | active |
| korea-exports | korea-customs-semi-exports-20day-flash | [[000660 - SK Hynix]] | permanent | active |
| memory-spot | trendforce-dram-nand-price-releases | [[000660 - SK Hynix]] | permanent | active |
| w3techs-proxy | w3techs-reverse-proxy-share-monthly | [[NET - Cloudflare]] | permanent | active |
| jedec-hbm | jedec-news:HBM4E-HBM5-standards | [[BESI - BE Semiconductor Industries]] | 2027-06-30 | active |
| sec-nbis-6k | sec-edgar-fts:NBIS-6-K | [[NBIS - Nebius Group]] | permanent | active |
| sec-spcx-8k | sec-edgar-fts:SPCX-8-K-10-Q | [[SPCX - SpaceX]] | permanent | active |
| pjm-queue | pjm-queue-point:large-load-interconnection | [[NBIS - Nebius Group]] | 2027-12-31 | active |

**Row rationale** (observable each source leads):
- `usaspending-pltr` — NGC2 prime-creep + ShipOS expansion beyond $448M: federal award API shows task-order flow *before* quarterly gov-segment prints; also catches Anduril displacing PLTR as prime.
- `bis-fedreg` — AMAT China-mix glide, ASMI MATCH Act final rule, NVDA H200/China reopening: Federal Register JSON API is the primary source for every export-control shock; news reports it hours later.
- `alchip-monthly` — MRVL Insight #5 (Trainium 3 ~500K-unit Marvell allocation, unconfirmed): Alchip is Taiwan-listed with monthly revenue disclosure — its ramp slope IS the T3 production read, quarters before AWS says anything.
- `taiwan-odm` — Quanta/Wiwynn monthly revenue = AI-server build rate = the hyperscaler-capex regime variable (MRVL Bear #4, META capex read-through, NVDA Rubin pull) at monthly frequency vs quarterly earnings.
- `ase-monthly` — advanced-packaging utilization proxy for TSM's CoWoS annuity + BESI order timing (Industry model #19: utilization proxies beat book-to-bill).
- `korea-exports` — 20-day flash leads memory pricing/HBM demand by weeks (000660, 285A, SNDK).
- `memory-spot` — Industry model #9: spot tightens first, contract follows 1–2Q, sell-side capitulates 1–2Q later — this row is the front of that chain. TrendForce free releases only; flag fragile.
- `w3techs-proxy` — NET's fired VLM falsifier (AWS x402 commoditization): reverse-proxy share shift is the neutral monthly scoreboard of whether Cloudflare's edge layer is gaining or ceding ground.
- `jedec-hbm` — BESI's "single highest-impact binary": HBM4E/HBM5 stack-thickness standard (late 2026) decides whether hybrid bonding becomes mandatory. Standards-page watch, not news.
- `sec-nbis-6k` — every 2026 funding-mix event (the $4.3B and $5.75B converts, the $2.8B ATM, the $775M secured facility, the 2029-note exchange) printed as a 6-K hours before coverage; EDGAR full-text search is a JSON API, so the LOW (>15% dilution per 6 months) and CLOSE (GPU-collateralised primary funding) legs get a same-day machine read instead of a next-day headline. Added 2026-08-27 (Full weight).
- `sec-spcx-8k` — CSA amendments, termination disclosures, lock-up releases and the Cursor close all land as 8-K/10-Q items; the capital-recovery-clock question (D&A lives versus CSA duration) is answerable only from filings, never from the launch newsflow. Added 2026-08-27 (High weight).
- `pjm-queue` — Nebius's Pennsylvania gigawatt sites sit in PJM (first power end-2027); queue status and large-load agreements lead the 2027+ energisation slope by quarters. API-grade (Queue Point exports). The 2026 Finland / New Jersey sites are outside PJM, so this row watches the 2027 ramp, not the November print. Added 2026-08-27.

**Deliberately skipped**: SEAJ/SEMI equipment billings (Industry model #19 — noisy lagging proxy; the three MOPS monthlies + tsmc-rev cover utilization better); Hanwha ABF qualification pace (no machine-readable source — `abf-hanwha` news row covers); Meta ad-CPM indices (paywalled).

## X Watchers

Drives Workflow 5 — X Harvester (n8n Automations §7). Cashtag clusters are auto-derived from Theses/ frontmatter —
no table needed. Curated terms below cover foreign listings + themes; Claude maintains this table.

### Curated terms

| id | query | min_faves | thesis | expires | status |
|---|---|---|---|---|---|
| x-hbm | "HBM4" OR "SK Hynix" | 30 | [[000660 - SK Hynix]] | permanent | active |
| x-fabric | "UALink" OR "NVLink Fusion" | 30 | [[MRVL - Marvell Technology]] | 2026-12-15 | active |
| x-cpo | "co-packaged optics" | 30 | [[LITE - Lumentum]] | permanent | active |
| x-semicap | "wafer fab equipment" OR "hybrid bonding" | 20 | [[AMAT - Applied Materials]] | permanent | active |
| x-capex | "hyperscaler capex" | 30 | [[AI Bubble Risk and Semiconductor Valuations]] | permanent | active |
| x-kioxia | Kioxia | 20 | [[285A - Kioxia]] | permanent | active |
| x-abf | Ajinomoto OR "ABF substrate" | 20 | [[2802 - Ajinomoto]] | permanent | active |
| x-murata | "Murata Manufacturing" OR "silicon capacitor" | 20 | [[6981 - Murata Manufacturing]] | permanent | active |
| x-elite | "Elite Material" | 20 | [[2383 - Elite Material]] | permanent | active |
| x-jusung | "Jusung Engineering" | 20 | [[036930 - Jusung Engineering]] | permanent | paused |
| x-winway | "WinWay" | 20 | [[6515 - WinWay Technology]] | permanent | paused |
| x-nittobo | "Nitto Boseki" OR Nittobo OR "quartz cloth" | 20 | [[3110 - Nitto Boseki]] | permanent | active |
| x-reliance | "Reliance Industries" | 50 | [[RELIANCE - Reliance Industries]] | permanent | paused |
| x-btc | $BTC | 1000 | [[BTC-CRYPTO - Bitcoin & Digital Assets]] | permanent | paused |
| x-tsmc | TSMC | 100 | [[TSM - Taiwan Semiconductor]] | permanent | active |
| x-robotaxi | Waymo OR robotaxi | 200 | [[UBER - Uber]] | permanent | active |
| x-gaw | "Games Workshop" | 20 | [[GAW - Games Workshop]] | permanent | active |
| x-aixtron | Aixtron | 20 | [[AIXA - Aixtron]] | permanent | active |
| x-agentic | "agentic commerce" OR x402 | 30 | [[Agentic Internet]] | permanent | active |
| x-advantest | Advantest OR V93000 | 20 | [[6857 - Advantest]] | permanent | active |
| x-nebius | Nebius | 50 | [[NBIS - Nebius Group]] | permanent | active |
| x-colossus | Colossus OR Terafab OR Starmind | 50 | [[SPCX - SpaceX]] | permanent | active |
| x-starlink | Starlink OR "Amazon Leo" | 200 | [[SPCX - SpaceX]] | permanent | active |
| x-pltr-rivals | "Fabric IQ" OR "Genie Ontology" | 20 | [[PLTR - Palantir]] | permanent | active |
| x-wisetech | WiseTech OR CargoWise | 20 | [[WTC - WiseTech Global]] | permanent | active |
| x-sivers | "Sivers Semiconductors" OR Sivers | 20 | [[SIVE - Sivers Semiconductors]] | 2026-12-31 | active |
| x-gta6 | "GTA 6" OR "GTA VI" | 300 | [[TTWO - Take-Two Interactive]] | 2027-01-31 | active |

*Revised 2026-07-26. Paused: x-btc + x-reliance (monitoring theses, high noise-to-thesis ratio — re-enable on active work or Jio-IPO newsflow) · x-jusung + x-winway (draft anchors, no near-term falsifier; ambiguous/zero-volume queries). Kept despite draft anchors: x-elite + x-nittobo — live dated kill-triggers (Shengyi/TUC M8 by YE2026; Asahi quartz ≥50% M9 2H'26) that both moved on the 2026-07-24 CoPoS glass-free datapoint. Added: x-tsmc (OQ-141 is a crowd-positioning question; non-cashtag chatter invisible to $TSM cluster), x-robotaxi (UBER terminal bear), x-gaw + x-aixtron (HIGH/active foreign listings without cashtags), x-agentic (protocol adoption surfaces on dev/crypto X first).*

*Revised 2026-08-27 against the Live Portfolio. Added: x-nebius, x-colossus, x-starlink (NBIS Full and SPCX High had cashtag clusters only; "Nebius" and the Colossus / Starlink names carry the non-cashtag crowd narrative, with floors set high because SpaceX chatter is launch-dominated); x-advantest (6857 is a Low-weight foreign listing with no cashtag, split out of x-semicap so it gets its own theme window instead of pooling under $AMAT, which left the book on 2026-08-25); x-pltr-rivals (the Full-weight bear side: Fabric IQ / Genie Ontology chatter is low-volume, high-signal and invisible to the $PLTR cluster). x-semicap re-scoped to WFE + hybrid bonding. x-tsmc kept active (TSM thesis still active/high) although TSM left the book; pause it here if the book should set coverage.*

*Revised 2026-08-27 (second pass) against the Watchlist Universe table. Added: x-wisetech (ASX name whose crowd chatter uses the company and product names, not $WTC; ASIC / DSV positioning is a sentiment question), x-sivers (windowed to the YE2026 Nasdaq-listing window; the Ningi short report gave the name a live retail / short X following), x-gta6 (floor 300: retail expectations into the 19 Nov launch are the positioning read for TTWO, and the chatter is enormous). mega_tickers +CRWV. Not added: x-iqe (chatter too thin to clear any floor), x-cerebras / x-vertiv / x-vicor (US cashtags already auto-derived).*

### Tuning

Trending-engine gates — parsed every run; edit a value, the next pull uses it (no redeploy).
Ratios are percentages (1.5 = 1.5%). A missing/non-numeric row falls back to the code default
(identical values to below). Record the *why* of each change in notes — this file's git history
is the tuning log.

| param              | value                                                           | notes                                                                       |
| ------------------ | --------------------------------------------------------------- | --------------------------------------------------------------------------- |
| floor_mega         | 100                                                             | pull floor (likes), mega-tier cashtag clusters                              |
| floor_std          | 30                                                              | pull floor (likes), standard-tier clusters                                  |
| mega_tickers       | NVDA,AMD,TSM,META,PLTR,AVGO,INTC,NET,NOW,CRWD,UBER,SHOP,NFLX,NBIS,SPCX,CRWV | comma list, no $ — which cashtags get floor_mega (CRWV added 2026-08-27 second pass: active Watchlist name with mega-cap-grade chatter since the $104B backlog print; NBIS + SPCX added 2026-08-27: Full / High Live Portfolio weights with retail-momentum chatter, the mega floor is the noise control; MU dropped 2026-07-26 when no MU thesis existed — a draft MU thesis from 2026-08-13 now auto-derives a $MU cluster at floor_std, re-add here if $MU floods the pull; CRWD kept — cluster live and mega floor is the noise control) |
| since_days         | 2                                                               | search window; keep ≥ cadence + 1 — trimmed 4→2 with daily cadence (2026-07-18) |
| track_min_views    | 3000                                                            | hard gate — ratios below this are noise                                     |
| min_followers      | 200                                                             | hard gate — kills throwaway accounts                                        |
| track_lv_pct       | 1.5                                                             | entry lane: like/view % (≈p50 after calibration)                            |
| track_rv_pct       | 0.5                                                             | entry lane: RT/view %                                                       |
| track_min_likes    | 300                                                             | entry lane: absolute likes                                                  |
| gem_lv_pct         | 3                                                               | gem flag: like/view % (≈p75 after calibration)                              |
| gem_rv_pct         | 0.7                                                             | gem flag: RT/view %                                                         |
| trend_min_delta    | 150                                                             | trending: Δlikes between pulls                                              |
| trend_min_pct      | 60                                                              | trending: % like-growth between pulls                                       |
| trend_min_base     | 50                                                              | %-lane only counts above this like base                                     |
| plateau_flat_likes | 10                                                              | Δlikes below this = flat pull                                               |
| plateau_pulls      | 2                                                               | consecutive flat pulls → prune                                              |
| prune_age_days     | 28                                                              | max observation age — 14→28 (2026-07-18, user): longer trending window, ~2× re-measure reads |
| cap_tracked        | 800                                                             | working-set cap (n8n Automations §7.1)                                      |
| llm_top_n          | 15                                                              | posts per theme fed to the sentiment LLM                                    |
| llm_model          | x-ai/grok-4.6                                                 | sentiment/divergence model — OpenRouter switch 2026-08-27 (was claude-opus-5): judgement seat, structured outputs enforced via `require_parameters`; step-down z-ai/glm-5.2, open-weights alternative moonshotai/kimi-k3 |
| archive_days       | 90                                                              | pruned posts retained in state archive — analysis corpus, never re-measured |
| x_tg_max_msgs      | 8                                                               | Telegram fan-out cap — top-N (divergences first, then flagged posts) sent as ONE message each instead of a single wall of text; clamped 1–15. Telegram ~1 msg/s flood limit — lower if 429s appear |

### LLM prompt

Analytical instructions for the sentiment/divergence call — the fenced block below is read on every
pull (fallback: identical default inside Code X). Output field names/types (`summary`, `sentiment`,
`score`, `perspectives`, `divergence`, plus `glosses` for the TRANSLATE section — 2026-08-27) are pinned by the workflow schema — edit the analytical
guidance freely, never the field list.

```
For each theme below you get MY THESIS (six analytical sections), PRIOR READS (dated sentiment reads produced by this engine over the past 90 days), HISTORICAL ANCHOR POSTS (highest-engagement posts from the 90-day archive, dated, labeled [A1], [A2], …), and CURRENT CROWD POSTS with engagement stats (labeled [P1], [P2], …) — current posts are drawn from every post tracked live for that theme, not just newly pulled ones. Weight CURRENT posts most: they are the consumption signal; use PRIOR READS and ANCHOR POSTS as longitudinal context, not as current evidence. Return per theme: summary — 2-4 sentences synthesising the current crowd narrative: what the crowd believes, where the argument concentrates, what evidence they cite; weight higher-engagement, higher-follower posts more. sentiment (bullish/bearish/mixed/quiet). score (-2..2). shift — 1-2 sentences on how crowd sentiment and the dominant argument have moved versus the PRIOR READS: new arguments appearing, old ones dying, conviction hardening or fading; null if there is no meaningful history or no real change. perspectives — 2-6 distinct crowd arguments; each has text (1-2 sentences carrying the specific numbers, names, and claims from the posts, never generic labels) and refs (the labels of the 1-3 specific posts that argument draws from, e.g. ["P2","A1"] — use only labels that appear above). divergence — ONE synthesis judged across all the posts together, never per post: a specific, substantive crowd argument that contradicts, challenges, or is unaddressed by my thesis. If the crowd merely echoes a risk or bear point my thesis already carries, that is NOT divergence — return null. Judge on substance of claims, not tone; ignore hype and spam; return null unless the tension is genuine. If a TRANSLATE section is present, return glosses: one {ref, en} object per listed [F#] post, where en is a faithful English gloss of that post (≤ 60 words, no commentary); return an empty glosses array when nothing is listed. Positioning gauge, not advice.
```

## Retired / Paused (audit trail)

Move rows here instead of deleting when you want a record of what you used to track and why you stopped. Read-only history.

| id | section | stopped | reason |
|---|---|---|---|
| net-outage | news | 2026-07-26 | redundant — auto Cloudflare ticker query + hi-vol tech feeds surface outages same-day; NET medium post-stress-test |
| pltr-nhs | news | 2026-07-26 | redundant — every NHS story names Palantir, so the auto ticker query already covers it; was windowed to 2027-03-31 |
| iqe-bid | news | 2026-08-27 | stale — strategic review concluded with no bid on 2026-04-27 (per the 2026-08-15 IQE stress test); thesis re-framed to MACOM LTSAs / InP epi; replaced by iqe-inp ⚠ |
| _example_ | news | 2026-07-17 | thesis closed |
