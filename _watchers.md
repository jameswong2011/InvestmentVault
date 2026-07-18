---
date: 2026-07-17
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

## News & Thematic (Workflow 3 — News Sweep)

n8n builds one Google News RSS query per active, unexpired row. Rows grouped by cluster for readability — the parser reads every table in this section identically. Populated 2026-07-17 from thesis-extraction pass across all semiconductor-complex theses (active + monitoring) + PLTR/META/NET; every row anchors to a dated observable, falsifier, or catalyst in the linked thesis. Rows marked ⚠ watch the *bear* side of their thesis (disconfirmation coverage per the READING PROTOCOL).

### Custom silicon & compute

| id | query | thesis | expires | status |
|---|---|---|---|---|
| mrvl-fabric | "UALink" OR "NVLink Fusion" OR "ESUN" | [[MRVL - Marvell Technology]] | 2026-10-31 | active |
| mrvl-trainium | "Trainium" AND (Marvell OR Alchip) | [[MRVL - Marvell Technology]] | 2026-12-15 | active |
| rubin-ramp | Nvidia AND ("Vera Rubin" OR Rubin OR Feynman) | [[NVDA - Nvidia]] | 2027-06-30 | active |
| huawei-ascend ⚠ | Huawei AND (Ascend OR "950PR" OR "950DT") | [[NVDA - Nvidia]] | permanent | active |
| openai-xpu | OpenAI AND (XPU OR Broadcom OR "custom chip") | [[AVGO - Broadcom]] | 2027-03-31 | active |
| amd-parity | AMD AND (MI455X OR Helios OR MLPerf OR ROCm) | [[AMD - Advanced Micro Devices]] | 2027-03-31 | active |
| intel-18a | Intel AND ("18A" OR "14A" OR foundry) | [[INTC - Intel]] | permanent | active |

### Foundry & packaging

| id | query | thesis | expires | status |
|---|---|---|---|---|
| tsmc-capex | "TSMC" AND (capex OR "capital expenditure" OR guidance) | [[AI Bubble Risk and Semiconductor Valuations]] | permanent | active |
| tsmc-nodes | TSMC AND (A16 OR Arizona OR N2 OR "2nm") | [[TSM - Taiwan Semiconductor]] | permanent | active |
| cowos | CoWoS | [[TSM - Taiwan Semiconductor]] | permanent | active |
| glass-substrate ⚠ | "glass substrate" AND (TSMC OR Intel OR Samsung) | [[2802 - Ajinomoto]] | permanent | active |
| abf-hanwha ⚠ | Hanwha AND (ABF OR substrate) | [[2802 - Ajinomoto]] | 2027-09-30 | active |

### Memory & storage

| id | query | thesis | expires | status |
|---|---|---|---|---|
| hbm4 | "HBM4" | [[000660 - SK Hynix]] | permanent | active |
| samsung-hbm ⚠ | Samsung AND (HBM4 OR "1c DRAM") | [[000660 - SK Hynix]] | 2027-03-31 | active |
| hybrid-bonding | "hybrid bonding" OR Kinex | [[BESI - BE Semiconductor Industries]] | permanent | active |
| nand-cycle ⚠ | NAND AND (pricing OR YMTC OR oversupply) | [[285A - Kioxia]] | permanent | active |
| hbf-flash | "high bandwidth flash" | [[SNDK - SanDisk]] | permanent | active |
| hbm-test | (Advantest OR Teradyne) AND (HBM OR "wafer test") | [[6857 - Advantest]] | permanent | active |

### Semicap & materials

| id | query | thesis | expires | status |
|---|---|---|---|---|
| tor-selection | ("tool of record" OR "process of record") AND (TSMC OR Samsung) | [[ASMI - ASM International]] | 2027-03-31 | active |
| wfe-china ⚠ | (SMIC OR Naura OR AMEC OR Skyverse OR CXMT) AND (equipment OR inspection OR expansion) | [[KLA - KLA Corporation]] | permanent | active |
| export-controls | ("export control" OR BIS) AND (semiconductor OR chip) | [[AMAT - Applied Materials]] | permanent | active |
| besi-ma | BESI AND (bid OR takeover OR acquisition) | [[BESI - BE Semiconductor Industries]] | 2027-06-30 | active |
| wlbi-test ⚠ | "wafer-level burn-in" OR (Aehr AND customer) | [[AEHR - Aehr Test Systems]] | 2027-01-31 | active |
| mlcc-ai ⚠ | MLCC AND (AI OR "silicon capacitor" OR Yageo) | [[6981 - Murata Manufacturing]] | permanent | active |

### Photonics & optical

| id | query | thesis | expires | status |
|---|---|---|---|---|
| cpo | "co-packaged optics" OR "CPO switch" | [[MRVL - Marvell Technology]] | permanent | active |
| china-optics ⚠ | China AND ("silicon photonics" OR EML OR "optical DSP") | [[LITE - Lumentum]] | permanent | active |
| inp-capacity ⚠ | ("indium phosphide" OR InP) AND (Veeco OR Coherent OR MOCVD) | [[AIXA - Aixtron]] | permanent | active |
| iqe-bid | IQE AND (bid OR takeover OR "strategic review") | [[IQE - IQE]] | 2026-12-31 | active |

### Software & platforms

| id | query | thesis | expires | status |
|---|---|---|---|---|
| pltr-defense | Palantir AND (Army OR NGC2 OR Navy OR NATO OR Anduril) | [[PLTR - Palantir]] | permanent | active |
| pltr-rivals ⚠ | "Genie Ontology" OR "Fabric IQ" OR "DeployCo" | [[PLTR - Palantir]] | permanent | active |
| pltr-nhs ⚠ | Palantir AND NHS | [[PLTR - Palantir]] | 2027-03-31 | active |
| meta-capex | Meta AND (capex OR "Meta Compute" OR "data center") | [[META - Meta]] | permanent | active |
| meta-ai | "Meta AI" AND (engagement OR users OR Superintelligence) | [[META - Meta]] | permanent | active |
| tiktok-ban | TikTok AND (ban OR divestiture OR sale) | [[META - Meta]] | permanent | active |
| net-act4 | Cloudflare AND (crawler OR "pay per crawl" OR x402) | [[NET - Cloudflare]] | permanent | active |
| net-sase | Cloudflare AND (Gartner OR SASE) | [[NET - Cloudflare]] | permanent | active |
| net-outage ⚠ | Cloudflare AND outage | [[NET - Cloudflare]] | permanent | active |

**Deliberately excluded** (no silent caps): draft-status theses (14 — no settled questions yet); SIVE and EINK dedicated rows (monitoring/low-conviction with slow-moving observables — the weekly per-ticker sweep covers them); a generic "AI capex" row (tsmc-capex + meta-capex + the Taiwan ODM poller below triangulate the same regime variable with less noise).

## Price Tripwires (Workflow 1)

n8n batch-quotes these tickers daily and pings when a level is breached. A breach means *read the thesis trigger block* — never an execution signal.

| id | ticker | direction | level | thesis | status |
|---|---|---|---|---|---|
| mrvl-bear | MRVL | below | 110 | [[MRVL - Marvell Technology]] | active |
| mrvl-bull | MRVL | above | 210 | [[MRVL - Marvell Technology]] | active |

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

**Deliberately skipped**: SEAJ/SEMI equipment billings (Industry model #19 — noisy lagging proxy; the three MOPS monthlies + tsmc-rev cover utilization better); Hanwha ABF qualification pace (no machine-readable source — `abf-hanwha` news row covers); Meta ad-CPM indices (paywalled).

## X Watchers

Drives Workflow 5 — X Harvester (Twitter API Build). Cashtag clusters are auto-derived from Theses/ frontmatter —
no table needed. Curated terms below cover foreign listings + themes; Claude maintains this table.

### Curated terms

| id | query | min_faves | thesis | expires | status |
|---|---|---|---|---|---|
| x-hbm | "HBM4" OR "SK Hynix" | 30 | [[000660 - SK Hynix]] | permanent | active |
| x-fabric | "UALink" OR "NVLink Fusion" | 30 | [[MRVL - Marvell Technology]] | 2026-12-15 | active |
| x-cpo | "co-packaged optics" | 30 | [[LITE - Lumentum]] | permanent | active |
| x-semicap | "wafer fab equipment" OR Advantest OR "hybrid bonding" | 20 | [[AMAT - Applied Materials]] | permanent | active |
| x-capex | "hyperscaler capex" | 30 | [[AI Bubble Risk and Semiconductor Valuations]] | permanent | active |

### Tuning

Trending-engine gates — parsed every run; edit a value, the next pull uses it (no redeploy).
Ratios are percentages (1.5 = 1.5%). A missing/non-numeric row falls back to the code default
(identical values to below). Record the *why* of each change in notes — this file's git history
is the tuning log.

| param | value | notes |
|---|---|---|
| floor_mega | 100 | pull floor (likes), mega-tier cashtag clusters |
| floor_std | 30 | pull floor (likes), standard-tier clusters |
| mega_tickers | NVDA,AMD,TSM,META,PLTR,AVGO,INTC,NET,NOW,CRWD,UBER,SHOP,NFLX,MU | comma list, no $ — which cashtags get floor_mega |
| since_days | 4 | search window; keep ≥ cadence + 1 |
| track_min_views | 3000 | hard gate — ratios below this are noise |
| min_followers | 200 | hard gate — kills throwaway accounts |
| track_lv_pct | 1.5 | entry lane: like/view % (≈p50 after calibration) |
| track_rv_pct | 0.5 | entry lane: RT/view % |
| track_min_likes | 300 | entry lane: absolute likes |
| gem_lv_pct | 3 | gem flag: like/view % (≈p75 after calibration) |
| gem_rv_pct | 0.7 | gem flag: RT/view % |
| trend_min_delta | 150 | trending: Δlikes between pulls |
| trend_min_pct | 60 | trending: % like-growth between pulls |
| trend_min_base | 50 | %-lane only counts above this like base |
| plateau_flat_likes | 10 | Δlikes below this = flat pull |
| plateau_pulls | 2 | consecutive flat pulls → prune |
| prune_age_days | 14 | max observation age |
| cap_tracked | 800 | working-set cap (§2.4) |
| llm_top_n | 10 | posts per theme fed to the sentiment LLM |

## Retired / Paused (audit trail)

Move rows here instead of deleting when you want a record of what you used to track and why you stopped. Read-only history.

| id | section | stopped | reason |
|---|---|---|---|
| _example_ | news | 2026-07-17 | thesis closed |
