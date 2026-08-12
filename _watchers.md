---
date: 2026-07-26
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

### Foundry & packaging

| id | query | thesis | expires | status |
|---|---|---|---|---|
| tsmc-capex | "TSMC" AND (capex OR "capital expenditure" OR guidance) | [[AI Bubble Risk and Semiconductor Valuations]] | permanent | active |
| tsmc-nodes | TSMC AND (A16 OR Arizona OR N2 OR "2nm") | [[TSM - Taiwan Semiconductor]] | permanent | active |
| cowos | CoWoS | [[TSM - Taiwan Semiconductor]] | permanent | active |
| copos-panel | CoPoS OR "panel-level packaging" | [[CoWoS-to-CoPoS Panel-Level Packaging Transition]] | 2027-12-31 | active |
| glass-substrate ⚠ | "glass substrate" AND (TSMC OR Intel OR Samsung) | [[2802 - Ajinomoto]] | permanent | active |
| abf-hanwha ⚠ | Hanwha AND (ABF OR substrate) | [[2802 - Ajinomoto]] | 2027-09-30 | active |

### Memory & storage

| id | query | thesis | expires | status |
|---|---|---|---|---|
| hbm4 | "HBM4" | [[000660 - SK Hynix]] | permanent | active |
| samsung-hbm ⚠ | (Samsung OR Micron) AND (HBM4 OR HBM4E OR "1c DRAM") | [[000660 - SK Hynix]] | 2027-03-31 | active |
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
| mlcc-ai ⚠ | MLCC AND (AI OR "silicon capacitor" OR Yageo OR SEMCO OR "Samsung Electro-Mechanics") | [[6981 - Murata Manufacturing]] | permanent | active |

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
| meta-capex | Meta AND (capex OR "Meta Compute" OR "data center") | [[META - Meta]] | permanent | active |
| meta-ai | "Meta AI" AND (engagement OR users OR Superintelligence) | [[META - Meta]] | permanent | active |
| tiktok-ban | TikTok AND (ban OR divestiture OR sale OR "joint venture" OR algorithm OR CFIUS) | [[META - Meta]] | permanent | active |
| net-act4 | Cloudflare AND (crawler OR "pay per crawl" OR x402) | [[NET - Cloudflare]] | permanent | active |
| net-sase | Cloudflare AND (Gartner OR SASE) | [[NET - Cloudflare]] | permanent | active |
| hyperscaler-guides | (Microsoft OR Amazon OR Alphabet) AND (capex OR "capital expenditure") AND (guidance OR earnings) | [[AI Bubble Risk and Semiconductor Valuations]] | 2026-08-31 | active |
| intu-agentic ⚠ | (OpenAI OR ChatGPT OR Anthropic OR Claude OR Gemini) AND (TurboTax OR "tax filing" OR bookkeeping OR QuickBooks) | [[INTU - Intuit]] | permanent | active |
| uber-av ⚠ | Waymo OR robotaxi | [[UBER - Uber]] | permanent | active |
| agentic-commerce | "agentic commerce" OR "agentic checkout" OR x402 | [[Agentic Internet]] | permanent | active |

**Deliberately excluded** (no silent caps): draft-status theses (14 — no settled questions yet); SIVE and EINK dedicated rows (monitoring/low-conviction with slow-moving observables — the weekly per-ticker sweep covers them); a generic *permanent* "AI capex" row (tsmc-capex + meta-capex triangulate the regime variable — the third leg, the taiwan-odm poller, is unbuilt backlog, so the windowed hyperscaler-guides row covers earnings-season guides until it exists or the window lapses).

## Outlet Feeds (Workflow 3 unified — LIVE)

Whole-outlet RSS pulls — the firehose complement to the query-scoped News & Thematic watches above. **Live since the unified Workflow 3 build** (header said IN BUILD until 2026-07-27 — stale; the Plan node parses this section every run): outlet feeds + FMP ticker news + GN/GDELT/Brave over every ticker and theme → dedupe → headline triage → defuddle body fetch for survivors → body re-score (Lane A) → story clustering → Opus-summarised daily intel brief (one entry per story, all source links) in `Daily Intel/`; **no `_Inbox/` deposits** (Lane C reverted 2026-07-20). Each block's `###` heading (parenthetical stripped) becomes its grouping header in the brief — rename a heading here and the brief's sections follow; the `cluster` column stays as metadata/fallback for rows outside any `###` block. Add/pause/delete rows freely — a row is one line, effective next sweep.

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
| triage_min | 7 | headline-triage gate — items below are dropped; `triage: no` rows bypass scoring entirely |
| triage_model | claude-sonnet-5 | headline triage (0–10 scoring vs injected coverage list) — capability at the gate; de-escalate to claude-haiku-4-5 (~$15–25/mo saving) if the calibration triage-band audit (§5.5f) shows the 5–6 band is clean noise |
| cluster_model | claude-opus-5 | ⚠ DEPRECATED 2026-07-23 — the Opus LLM cluster call was **removed**; semantic same-story + cross-run repeat detection now runs on **embeddings** (see `embed_model`) BEFORE the body pipeline, so duplicates never reach Opus rescore (that was the cost driver: ~$10–12/run, mostly rescoring dupes). Row kept for rollback only (n8n Automations §12 changelog); unused by the live pipeline |
| rescore_model | claude-opus-5 | body-informed re-score (Lane A) — reads full article text and sets final ranking (~$10–15/mo); claude-sonnet-5 is the step-down |
| digest_model | claude-opus-5 | analytical brief layer — reads merged excerpts, writes decision-useful analysis with coverage implications (rule-2 rewrite 2026-07-21, trail n8n Automations §11; ~$25–50/mo); claude-sonnet-5 is the step-down; prompt: `#### digest_prompt` in ### Prompts below (registry-editable) |
| body_exempt | digitimes, ft-home, bbg-tech, bbg-econ, bbg-markets, wsj-markets, wsj-tech, wsj-business, econ-finance, econ-business, nyt-business, nyt-tech, theinformation, techmeme, mediagazer | paywalled bodies or aggregator permalinks — headline-only, never body-fetched |
| catalyst_window_d | 10 | catalyst proximity markers — stories on tickers with a `_catalyst.md` event within ±N days get a 📅 T-N tag in the brief |
| max_age_d | 3 | hard age cap — items with a parseable publish date older than N days are dropped at Normalize (counted as `stale` in the funnel); GN search queries also carry `when:Nd` so old relevance-ranked hits never arrive |
| triage_min_pw | 9 | stricter admit bar for paywalled items (flagged `pw` at Normalize) — headline must be material on its own; normal items use triage_min |
| tg_max_msgs | 10 | Telegram fan-out — top-N stories by score, ONE message each (full summary + link; last message carries the brief footer + failure count). Telegram same-chat flood limit is ~1 msg/s — if the Notify node starts collecting 429s, lower this |
| tg_per_subject | 2 | Telegram diversity cap — at most N messages per ticker/theme, so one busy subject (a microcap in the news) can't fill the glance. Raise to allow more per subject, set 1 for maximum spread |
| dedup_ttl_d | 3 | card-12 dedup memory window (static-data store) — a URL OR headline seen within N days is dropped as a repeat. "Non-repeats past N days." **Keep small** (static data reloads every run; do NOT set 30 — see track_window_d for long-horizon tracking). Should be ≥ max_age_d so an article can't re-brief within its own eligible life |
| merge_jaccard | 0.42 | SumPrep within-run near-dup merge threshold (token overlap) — now a **backstop** behind the embeddings layer (catches any same-story pair the vectors missed). LOWER = more aggressive merging of same-event headlines into one story. 0.42 default; drop toward 0.35 if twins persist, raise toward 0.55 if unrelated stories get merged |
| embed_model | voyage-4-lite | semantic-dedup embedder (Voyage) — embeds each admitted item's title+snippet, cosine-clusters same-story dupes into ONE representative **before** the Opus body pipeline so duplicates never get body-fetched or rescored. `voyage-4-lite` = $0.02/M tok with **200M free tok/account** (≈2+ yrs free at this volume); `voyage-4` ($0.06/M) is the quality step-up. Replaces the deprecated `cluster_model`. Requires the `Voyage` n8n credential (n8n Automations §5.1) |
| sim_threshold | 0.86 | cosine ≥ this among NEW items = same story → merged to one representative (all source links preserved). **The primary repeat-suppression dial**: RAISE toward 0.90 if distinct stories get merged; LOWER toward 0.82 if the same event still shows twice |
| repeat_threshold | 0.88 | cosine of a NEW item vs a PRIOR briefed story (last `story_memory_days`) ≥ this = follow-up → ♻ links-only section, never re-summarised. Set higher than `sim_threshold` so only near-identical reruns divert |
| embed_max_chars | 1000 | chars of title+snippet fed to the embedder per item — enough for same-story judgement; more just spends tokens |
| track_min_score | 8 | sentiment-tracking relevance floor — `/surface`'s 30-day story-log read counts only stories at/above this final score (the daily brief still shows everything ≥ triage_min; this is a stricter bar for the long-horizon trend view) |
| track_window_d | 30 | how many days of `.data/news_stories/` logs `/surface` reads for sentiment/coverage tracking. Disk files, not DB — 30 days ≈ 12 MB of plain JSON, trivial. Distinct from story_memory_days (repeat-detection window, stays 3–7) |
| paywall_domains | bloomberg.com, wsj.com, ft.com, economist.com, nytimes.com, theinformation.com, barrons.com | URL-level paywall detection for Brave/GDELT/FMP arrivals — combines with the body_exempt feed ids; pw items skip body-fetch and carry 🔒 in the brief |
| story_memory_days | 7 | cross-run story memory window — briefed stories from the last N days ride into the cluster call; follow-up coverage adding no new facts lands in the brief's ♻ links-only section instead of being re-summarised |
| gdelt_spacing_s | 12 | Wait between GDELT queries. Limiter is 1 req/5s **plus a sticky cooldown that trips after ~4 rapid calls** (re-verified 2026-07-23: even 20s spacing 429'd the 5th call) — 8s was too tight, most of a 110-query run 429'd → returned nothing. 12s gives headroom; the durable fix if GDELT is still weak is fewer queries (see n8n Automations §12.1 GDELT rows / thematic-only Plan option) |
| brave_budget_mo | 3500 | monthly query guard — paid metered tier (2026-07-20); full ticker+theme coverage at 1×/day ≈ 3,000/mo |

### Prompts (Workflow 3 unified)

Each `####` block below is the live prompt for one LLM stage — edit freely in Obsidian; the workflow re-reads them every run, no n8n touch required. Rules: **keep the required tokens** — they substitute at runtime (`{items}` = batch payload · `{prior}` = prior-story list · `{tickers}` = coverage tickers · `{themes}` = live research questions · `{context}` = the optional `#### brief_context` block below, digest only); a missing *required* token reverts that stage to the code fallback in §5.3 card 5 (required: triage/rescore/digest `{items}` · cluster `{items}` + `{prior}`). Don't start a line with `#` inside a prompt (terminates the block) and keep the trailing "Return ONLY…" clause — the parsers depend on that output shape. `#### brief_context` is freeform standing priorities for the summariser — your analytical steering wheel; edit or blank it freely, no tokens required.

#### triage_prompt
You score news items for one investor. Coverage tickers: {tickers}. Live research questions: {themes}. Clusters also covered: semis, datacenter, china-tech, macro, AI, futurism, tech philosophy, consumer tech. Score each item 0-10 on NEW information value to this coverage: 9-10 directly material new fact (guidance, capacity, pricing, regulatory, primary technical disclosure); 7-8 clearly relevant development; 4-6 adjacent context; 0-3 noise — listicles, price-target roundups, "stocks to buy", rehash, sponsored. Judge information content, not sentiment. Items flagged pw:1 are paywalled — only the headline is readable; hold them to a stricter bar: 8-10 only if the headline alone discloses a material new fact for this coverage, otherwise 0-3. Items: {items} — Return ONLY a JSON array [{"i":0,"s":7},...] covering every item.

#### rescore_prompt
Re-score these news items 0-10 for NEW information value to an investor covering: {tickers}. Live research questions: {themes}. Each item carries its headline score (hs, may be null for auto-admitted sources) and an article excerpt (x). Confirm the article delivers substance — new numbers, primary quotes, disclosed specifics. Downgrade rehash/opinion; upgrade if the body reveals material specifics the headline undersold. Items flagged pw:1 are paywalled (excerpt is headline-grade only) — keep them high only if that alone is materially new. Items: {items} — Return ONLY a JSON array [{"i":0,"s":7},...] covering every item.

#### cluster_prompt
NEW ITEMS are news items from today, from multiple sources; each carries its headline (t) AND a content excerpt (x). PRIOR STORIES were already briefed to the reader on previous days (label, title, summary). Judge same-story on the EXCERPT's substance — the actors, action, and event it describes — NOT on headline wording; two articles with completely different headlines by different authors are the same story if their excerpts describe the same event. Two tasks. (1) Group NEW items that cover the SAME underlying story or event into clusters. Two items are the same story when they report the same actor + action + timeframe (the same announcement, filing, decision, result, or incident), even if headlines emphasize different aspects, figures, or reactions — multiple outlets covering one event is ONE cluster. Keep items separate only when the underlying events genuinely differ (different actors, different actions, or clearly distinct developments). (2) A NEW item that is follow-up coverage of a PRIOR story AND adds no material new facts beyond that story's summary is a repeat — list it under repeats with the prior label. If it ADVANCES the story (new numbers, official responses, next-step events, a material escalation), it is NOT a repeat — cluster it as new. Bias toward repeat: same event with no NEW specific (a number, a named actor, an official action) beyond the prior summary is a repeat even if the wording, outlet, or angle differs — when torn between repeat and new, choose repeat. NEW ITEMS: {items} PRIOR STORIES: {prior} — Return ONLY JSON: {"clusters":[[indices]],"repeats":[[itemIndex,"P<n>"],...]} with every NEW item index appearing exactly once across clusters and repeats.

#### digest_prompt
You write a daily intelligence brief for one investor. Coverage tickers: {tickers}. Live research questions: {themes}. Each item is one story, possibly reported by several sources (srcs) with merged excerpts. For each item write "sum": 2-5 sentences of decision-useful analysis. Lead with the concrete NEW facts — numbers with the comparison that gives them meaning (vs prior guidance, consensus, rivals), named actors, the mechanism of what changed, and stated timelines or next dates. Then state what it means for the coverage: which ticker or research question it touches and the transmission path (pricing power, capacity, share shift, cost curve, regulation, demand signal), and what would confirm or refute that read. Ground every claim in the provided text; label inference explicitly ("implies", "suggests", "if X then Y"). Where sources disagree on a figure, say so. Some items carry sig — the investor's live signals for the tickers involved (catalyst proximity, crowd sentiment); weave these into the implication when they sharpen it. Standing investor context: {context}. If the text is thin or navigation junk, one sentence restating the headline claim. Items: {items} — Return ONLY a JSON array [{"i":0,"sum":"..."},...] covering every item.

#### brief_context
Priorities: AI datacenter supply-chain inflections ahead of consensus; custom-silicon share shifts vs Nvidia (MRVL, AVGO); HBM/memory pricing power (000660, SNDK, 285A); semicap + export-control second-order effects; photonics/CPO adoption timing; hyperscaler capex guides (Jul 28–31 window — read against the TSM sell-the-beat question); CoPoS/panel-level packaging timing; agentic-commerce protocol adoption (x402/checkout rails); AV-robotaxi expansion vs Uber; frontier-lab agents entering tax/bookkeeping (Intuit bear-watch). Prefer specific implications for covered names over generic sector commentary. Flag anything that looks like an inflection-point datapoint rather than incremental news.

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

Drives Workflow 5 — X Harvester (n8n Automations §7). Cashtag clusters are auto-derived from Theses/ frontmatter —
no table needed. Curated terms below cover foreign listings + themes; Claude maintains this table.

### Curated terms

| id | query | min_faves | thesis | expires | status |
|---|---|---|---|---|---|
| x-hbm | "HBM4" OR "SK Hynix" | 30 | [[000660 - SK Hynix]] | permanent | active |
| x-fabric | "UALink" OR "NVLink Fusion" | 30 | [[MRVL - Marvell Technology]] | 2026-12-15 | active |
| x-cpo | "co-packaged optics" | 30 | [[LITE - Lumentum]] | permanent | active |
| x-semicap | "wafer fab equipment" OR Advantest OR "hybrid bonding" | 20 | [[AMAT - Applied Materials]] | permanent | active |
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

*Revised 2026-07-26. Paused: x-btc + x-reliance (monitoring theses, high noise-to-thesis ratio — re-enable on active work or Jio-IPO newsflow) · x-jusung + x-winway (draft anchors, no near-term falsifier; ambiguous/zero-volume queries). Kept despite draft anchors: x-elite + x-nittobo — live dated kill-triggers (Shengyi/TUC M8 by YE2026; Asahi quartz ≥50% M9 2H'26) that both moved on the 2026-07-24 CoPoS glass-free datapoint. Added: x-tsmc (OQ-141 is a crowd-positioning question; non-cashtag chatter invisible to $TSM cluster), x-robotaxi (UBER terminal bear), x-gaw + x-aixtron (HIGH/active foreign listings without cashtags), x-agentic (protocol adoption surfaces on dev/crypto X first).*

### Tuning

Trending-engine gates — parsed every run; edit a value, the next pull uses it (no redeploy).
Ratios are percentages (1.5 = 1.5%). A missing/non-numeric row falls back to the code default
(identical values to below). Record the *why* of each change in notes — this file's git history
is the tuning log.

| param              | value                                                           | notes                                                                       |
| ------------------ | --------------------------------------------------------------- | --------------------------------------------------------------------------- |
| floor_mega         | 100                                                             | pull floor (likes), mega-tier cashtag clusters                              |
| floor_std          | 30                                                              | pull floor (likes), standard-tier clusters                                  |
| mega_tickers       | NVDA,AMD,TSM,META,PLTR,AVGO,INTC,NET,NOW,CRWD,UBER,SHOP,NFLX | comma list, no $ — which cashtags get floor_mega (MU dropped 2026-07-26: no MU thesis → no cluster, dead entry; CRWD kept — cluster live and mega floor is the noise control) |
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
| llm_model          | claude-opus-5                                                 | sentiment/divergence model; current-gen only (body sends adaptive thinking) |
| archive_days       | 90                                                              | pruned posts retained in state archive — analysis corpus, never re-measured |
| x_tg_max_msgs      | 8                                                               | Telegram fan-out cap — top-N (divergences first, then flagged posts) sent as ONE message each instead of a single wall of text; clamped 1–15. Telegram ~1 msg/s flood limit — lower if 429s appear |

### LLM prompt

Analytical instructions for the sentiment/divergence call — the fenced block below is read on every
pull (fallback: identical default inside Code X). Output field names/types (`summary`, `sentiment`,
`score`, `perspectives`, `divergence`) are pinned by the workflow schema — edit the analytical
guidance freely, never the field list.

```
For each theme below you get MY THESIS (six analytical sections), PRIOR READS (dated sentiment reads produced by this engine over the past 90 days), HISTORICAL ANCHOR POSTS (highest-engagement posts from the 90-day archive, dated, labeled [A1], [A2], …), and CURRENT CROWD POSTS with engagement stats (labeled [P1], [P2], …) — current posts are drawn from every post tracked live for that theme, not just newly pulled ones. Weight CURRENT posts most: they are the consumption signal; use PRIOR READS and ANCHOR POSTS as longitudinal context, not as current evidence. Return per theme: summary — 2-4 sentences synthesising the current crowd narrative: what the crowd believes, where the argument concentrates, what evidence they cite; weight higher-engagement, higher-follower posts more. sentiment (bullish/bearish/mixed/quiet). score (-2..2). shift — 1-2 sentences on how crowd sentiment and the dominant argument have moved versus the PRIOR READS: new arguments appearing, old ones dying, conviction hardening or fading; null if there is no meaningful history or no real change. perspectives — 2-6 distinct crowd arguments; each has text (1-2 sentences carrying the specific numbers, names, and claims from the posts, never generic labels) and refs (the labels of the 1-3 specific posts that argument draws from, e.g. ["P2","A1"] — use only labels that appear above). divergence — ONE synthesis judged across all the posts together, never per post: a specific, substantive crowd argument that contradicts, challenges, or is unaddressed by my thesis. If the crowd merely echoes a risk or bear point my thesis already carries, that is NOT divergence — return null. Judge on substance of claims, not tone; ignore hype and spam; return null unless the tension is genuine. Positioning gauge, not advice.
```

## Retired / Paused (audit trail)

Move rows here instead of deleting when you want a record of what you used to track and why you stopped. Read-only history.

| id | section | stopped | reason |
|---|---|---|---|
| net-outage | news | 2026-07-26 | redundant — auto Cloudflare ticker query + hi-vol tech feeds surface outages same-day; NET medium post-stress-test |
| pltr-nhs | news | 2026-07-26 | redundant — every NHS story names Palantir, so the auto ticker query already covers it; was windowed to 2027-03-31 |
| _example_ | news | 2026-07-17 | thesis closed |
