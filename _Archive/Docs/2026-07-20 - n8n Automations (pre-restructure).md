---
publish: false
date: 2026-07-19
tags: [meta, infrastructure, automation, how-to]
status: active
---

# n8n Automations — Platform, Workflows & X Intelligence

> Merged 2026-07-19 from `n8n.md` (platform + Workflows 1–3 → §1–§6) and `Twitter API Build.md` (X intelligence, Workflows 4–5 → §7–§11). Pre-merge originals: `_Archive/Docs/`.

n8n (self-hosted, free) is the vault's **sensory layer**: always-on acquisition, scheduling, and alerting upstream of `/ingest`. The vault today is pull-based — nothing enters `_Inbox/`, no skill runs, no thesis observable gets checked unless Alex acts. Evidence of the gap: [[_catalyst.md]] went 55 days stale (generated 2026-05-23) while its own window ran through 2026-08-21; [[Theses/MRVL - Marvell Technology.md]] carries five dated "first confirming observables" that nothing watches between sessions.

**Division of labor (non-negotiable):**

| Layer | Does | Never does |
|---|---|---|
| n8n | Deterministic acquisition, cron scheduling, threshold alerts, relevance triage | Judgement — it has no mental-models context, no thesis state |
| Vault skills | All analysis, propagation, conviction | Watching the world between sessions |

**Four hard rules** (extend CLAUDE.md change-safety into the automation layer):

1. **n8n writes only NEW files, only into designated output locations** — `Daily Intel/` (dashboard snapshots + daily digests: scanning surfaces, not ingest candidates), `.data/` (machine state), `_Inbox/` (true ingest candidates only). Never Theses/, Research/, metadata files, `_Inbox/processed/`, or any existing file. Anything meant for the research pipeline still flows through `/ingest` exactly like a manual web clip — you paste the links worth ingesting. *Amended 2026-07-20 (Lane C, user decision), REVERTED 2026-07-20 later same day (unified-W3 decision):* no n8n `_Inbox/` deposits of any kind — the unified Workflow 3 outputs a daily intel brief into `Daily Intel/` only; ingest candidates are hand-picked from the brief (curation stays at paste-time). The §2.3 contract remains the spec for any future re-sanctioned deposit.
2. **Triage yes, analysis no.** n8n AI nodes may relevance-score feed items before deposit. They never summarise, conclude, or write analytical prose — context-free analysis entering the vault laundered as source material is the failure mode. *Sole user-approved exception:* Workflow 5's sentiment layer — **read-vault yes, write-vault no**: it reads thesis sections to compare against crowd posts, and its output lands only in the dated dashboard snapshot in `Daily Intel/`, never in Theses/Research or propagation (§8.7). Relevance-scoring may read full article bodies, not just headlines (Lane A, 2026-07-20). *Second sanctioned exception (2026-07-20, user decision — reverses the same-morning Lane B rejection in contained form):* the unified Workflow 3's **digest summary layer** — Sonnet writes 1–2 factual sentences per admitted item (concrete new facts only: numbers, names, guidance, dates; no opinion, no recommendation, no thesis inference), landing exclusively in the `Daily Intel/` brief. Never into Theses/, Research/, or propagation; `/ingest` remains the only analytical summarizer (it alone carries mental-models context).
3. **No Tier 3 operations, ever.** `/status`, `/prune`, conviction changes stay human.
4. **Lock-aware.** Any future headless `claude -p` invocation checks `.vault-lock*` absence first — composing with the preflight contract in [[INFRASTRUCTURE]] §6 instead of racing it.

---

## 1. Base install (~45 min, one-time)

**Free vs paid tiers — read before installing.** n8n's pricing page leads with self-hosted **Business** (€667/mo annual) and **Enterprise** (custom) — these bundle multi-user governance (SSO/SAML/LDAP, Git-based environments, RBAC, dedicated support) that a single-user local install doesn't need. The **Community Edition** — plain `npm install -g n8n`, pulled straight from GitHub under n8n's fair-code license — is free, unlimited executions, no license key, and is what this entire tutorial installs and every workflow below runs on. Cloud Starter/Pro (€20–50/mo) is a third, separate option this doc doesn't use at any price point, because it can't reach the local filesystem (§1 rationale below).

**Why native npm, not Docker:** the workflows need host access — Execute Command (ticker + thesis-section extraction from `Theses/`) and file writes into the vault. A Docker container can do neither without contortions. n8n Cloud (€20+/mo) can't reach the local filesystem at all. Native install: $0, full access.

### 1.1 Install Node 22 LTS + n8n

Machine currently runs Node v25.9.0 (non-LTS; n8n's engine check may refuse it). Install an LTS side-by-side via nvm:

```bash
# nvm (skip if installed)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
# restart terminal, then:
nvm install 22
nvm use 22
npm install -g n8n
n8n --version   # expect 1.x
```

### 1.2 First launch

```bash
GENERIC_TIMEZONE="Australia/Sydney" TZ="Australia/Sydney" n8n start
```

Open `http://localhost:5678` → create the owner account (local credential, pick a real password). Timezone env vars make every cron expression below fire in AEST.

**Security posture:** n8n listens on localhost only — do not port-forward 5678, do not enable tunnelling. API keys are encrypted at rest with the key in `~/.n8n/config` (back it up — credentials are unrecoverable without it).

### 1.3 Keep it running

```bash
npm install -g pm2
GENERIC_TIMEZONE="Australia/Sydney" TZ="Australia/Sydney" NODES_EXCLUDE='["n8n-nodes-base.localFileTrigger"]' pm2 start n8n
pm2 save
pm2 startup   # prints one sudo command — run it to autostart at login
```

`NODES_EXCLUDE` (added 2026-07-18): n8n 2.x excludes **Execute Command** and Local File Trigger by default — a v2 breaking change. Workflow 5 needs Execute Command (ticker + thesis-section extraction), so the override re-enables it while keeping the unused Local File Trigger excluded. Localhost-only listener + the file fence are unaffected.

### 1.4 The Mac-sleep caveat (read this)

Schedules fire only while the Mac is awake. A missed cron does not back-fill. Options, in order of preference:

1. Schedule everything inside reliably-awake hours (06:00–22:00 works for every workflow — nothing here needs 3 a.m.).
2. `sudo pmset repeat wakeorpoweron MTWRFSU 06:25:00` to guarantee the morning block.
3. Accept occasional misses — every workflow below is idempotent (dedup keys, cross-execution memory), so a missed day self-heals on the next run.

### 1.5 Updating

Quarterly, deliberately (not automatically): `pm2 stop n8n && npm update -g n8n && pm2 restart n8n`. Check the changelog first; pin the version if everything works.

---

## 2. Shared building blocks (~1 h, one-time)

### 2.1 Credentials (n8n → Credentials) — create lazily, not up front

This is a reference checklist, **not a sequential step**: create each credential when building its first consuming workflow.

| Credential | Type | Source | Used by |
|---|---|---|---|
| Telegram bot | Telegram API | §2.2 (BotFather) | Every workflow's notifications + the §2.5 watchdog |
| FMP | HTTP Query Auth (`apikey` param) | Copy the key from `.data/config.json` (same one Watchlist / Live Portfolio / skills use) | Workflows 1 (Price Tripwires) + 3 unified (ticker news) |
| twitterapi.io | Header Auth (`X-API-Key`) | twitterapi.io dashboard — §9.1 | Workflows 4–5 |
| Anthropic | Header Auth (`x-api-key`) | console.anthropic.com — separate billing from the Claude Code subscription | Workflow 5 sentiment layer; Workflow 3 (unified) headline triage + body re-score (Haiku) + digest summaries (Sonnet) |
| Brave Search | Header Auth (`X-Subscription-Token`) | brave.com/search/api — **paid metered tier** (user decision 2026-07-20; free 2,000/mo vs ~6,000/mo needed for full ticker+theme daily coverage — verify per-1,000 pricing at upgrade) | Workflow 3 (unified) thematic + per-ticker search channel |

**Everything else is credential-free by design.**

### 2.2 Notification channel: Telegram (~10 min)

Free, reliable mobile push; every workflow terminates in it.

1. Message **@BotFather** → `/newbot` → name it (e.g. `vault_watch_bot`) → copy the token.
2. Send your new bot any message, then open `https://api.telegram.org/bot<TOKEN>/getUpdates` — copy `chat.id`.
3. In workflows: **Telegram node** → Send Message → your chat id.

Local-only fallback while at the Mac: Execute Command → `osascript -e 'display notification "..." with title "Vault"'`.

### 2.3 The `_Inbox/` deposit contract

Every file n8n writes follows this shape so `/ingest` provenance (immutable `source:`) works unmodified:

```markdown
---
source: <URL>
retrieved: YYYY-MM-DD
origin: n8n/<workflow-name>
---
# <Title>

<content or link digest>
```

- Filename: `YYYY-MM-DD - <topic> - <origin>.md`. New files only; never append to or modify an existing file; never touch `_Inbox/processed/`.
- Node chain to write a file: **Code** (assemble string) → **Convert to File** (text → file) → **Read/Write Files from Disk** (Write, path `/Users/alexcohen/InvestmentVault/_Inbox/<name>.md`).
- **Digest mode is the default** for feed-class sources (Workflow 3): one file per day per feed class, not one per item — 70 tickers × per-item deposits would flood `_Inbox` and burn `/ingest` tokens on noise.
- **No live workflow deposits into `_Inbox/` as of 2026-07-20** (Lane C reverted at the W3 unification): this contract is retained as the spec for any future re-sanctioned deposit.

### 2.35 The watcher registry — one file controls everything pulled

**The single most important design decision for keeping this maintainable.** What n8n pulls must NOT live inside n8n's workflow code — every change would mean opening n8n, editing a Code node, saving. Instead, all criteria live in one vault file, [[_watchers.md]], and each workflow reads it on every run. The workflow is built once and never edited again; adding/removing a watch is a markdown-table edit that takes effect on the next scheduled run with no redeploy or restart.

**Schema** (sectioned by consuming workflow — one file, one place to look):

| Section | Drives | Columns |
|---|---|---|
| News & Thematic | Workflow 3 (unified) — each row queried via GN + GDELT + Brave | `id, query, thesis, expires, status` |
| Outlet Feeds | Workflow 3 (unified) — one RSS pull per row; also hosts `### Tuning (body pipeline)` params | `id, url, cluster, vol, triage, expires, status` |
| Price Tripwires | Workflow 1 — batch-quote + breach alert | `id, ticker, direction, level, thesis, status` |
| X Watchers | Workflow 5 — curated X terms (`### Curated terms`) + engine thresholds (`### Tuning`) | `id, query, min_faves, thesis, expires, status` · `param, value, notes` |
| Alt-Data Pollers | *(backlog — no consuming workflow built)* | `id, source, thesis, expires, status` |

**Lifecycle** — the mechanism that stops the list becoming a burden:
- `status: active`/`paused` — mute-but-keep without losing the config.
- `expires:` a date → the parse filter drops the row after it passes (windowed watches self-retire — you never remember to turn them off); `permanent` runs until deleted.
- Delete or move to the Retired section → gone.

**How a workflow reads its section** (Read/Write Files → Extract from File → Code):

```javascript
const md = $json.data;
const today = $now.toFormat('yyyy-MM-dd');
const section = md.split('## News & Thematic')[1]?.split('\n## ')[0] || '';
return [...section.matchAll(/^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|/gm)]
  .map(r => ({ id: r[1].trim(), query: r[2].trim(), expires: r[4].trim(), status: r[5].trim() }))
  .filter(w => w.id !== 'id' && !/^-+$/.test(w.id))
  .filter(w => w.status === 'active')
  .filter(w => w.expires === 'permanent' || w.expires >= today)
  .map(w => ({ json: { id: w.id,
    url: `https://news.google.com/rss/search?q=${encodeURIComponent(w.query)}&hl=en-US&gl=US&ceid=US:en` }}));
```

**Maintenance is a sentence, not a chore.** Because `_watchers.md` is a vault file, the vault assistant maintains it in natural language — "track everything on TSMC" appends a row; "stop tracking TSMC" pauses or deletes it; "what am I watching?" reads it back. n8n's UI stays closed after the one-time build. Constraint: no aliased wikilinks (`[[note|alias]]`) in cells — the `|` breaks the table and the parser; use bare `[[note]]`.

**Anti-accumulation:** auto-expiry retires windowed watches; the `thesis` column forces each watch to justify itself against a live question (orphans surface when a thesis closes); the §5 monthly review prunes the rest.

### 2.5 Error watchdog (build before anything else)

New workflow: **Error Trigger** node → **Telegram** ("⚠️ n8n workflow {{ $json.workflow.name }} failed: {{ $json.execution.error.message }}"). Then set it as the error workflow in every other workflow's settings. Without this, a silently dead watcher is worse than no watcher — you'll trust coverage you don't have.

### 2.6 Ticker universe (used by Workflow 3's ticker channels and Workflow 5)

Derive from thesis filenames — no separate list to maintain:

Execute Command → `ls "/Users/alexcohen/InvestmentVault/Theses" | sed -E 's/ - .*//' | sort -u`

Yields ~70 tickers (hyphenated and numeric Asia listings included). Read-only; safe.

---

## 3. Workflows

### Workflow 1 — Price Tripwires

**What:** Daily quote check of every active row in [[_watchers.md]] §Price Tripwires — Conviction-Trigger levels become live pages.

| | |
|---|---|
| Build effort | ~1 h (one workflow) |
| Running cost | $0 marginal — existing FMP plan; 1 API call/day |
| Maintenance | ~15 min/mo — keep `_watchers.md` tripwire levels in sync with Conviction Triggers as theses evolve |
| Benefit | **High.** Conviction Triggers are falsifiable if/then statements with nothing watching the "if". MRVL example: bear zone $80–110, bull legs $210+, from $188.30 — a -15% two-session move (Jul 15–16) is exactly the event class that should page you same-day |
| Status | **Live** — daily 07:35 AEST (after US close, staggered behind Workflow 2's 07:30) |

**Build** (click-level cards: §13.2)**:**
1. Read the **Price Tripwires** section of [[_watchers.md]] (§2.35) — levels live there, not in the workflow, so you edit them in Obsidian (or via the vault assistant) without touching n8n.
2. Parse active rows (Code node) → **HTTP Request** batch quote (`stable/batch-quote-short?symbols=MRVL,AVGO,...` — comma-joined tickers, one call; v3 endpoints are legacy-dead on this key, verified 2026-07-17) → **Code** compare → **Telegram** on breach, citing the thesis.
3. Discipline: a tripwire firing is a signal to *read the thesis trigger block*, not to act. Update levels in `_watchers.md` whenever `/status` or `/sync` changes a trigger.

---

### Workflow 2 — Catalyst Reminders

**What:** Daily 07:30 — parse [[_catalyst.md]], push Telegram alerts for events today and T-2, and flag when the calendar itself is >30 days old ("run `/catalyst`").

| | |
|---|---|
| Build effort | 1–2 h |
| Running cost | $0 |
| Maintenance | ~0 — parser is coupled to `/catalyst`'s table format; re-check after any `/catalyst` spec change |
| Benefit | **High.** 63 events/13 weeks in the current window; the 55-day staleness episode is the proven failure mode. Dated observables (MRVL Q2 FY27 print late Aug, OCP Oct, re:Invent Nov–Dec) stop depending on memory |
| Status | **Live** — daily 07:30 |

**Build** (click-level cards: §13.3)**:**
1. **Schedule Trigger** — daily · Trigger at Hour `7am` · Trigger at Minute `30`.
2. **Read/Write Files from Disk** (Read) → `_catalyst.md` → **Extract from File** (Text).
3. **Code** node:

```javascript
const md = $input.first().json.data;   // Code node in "Run Once for All Items" mode
const now = new Date();
const out = [];

const fm = md.match(/^date:\s*(\d{4}-\d{2}-\d{2})/m);
const age = fm ? Math.floor((now - new Date(fm[1])) / 86400000) : 999;
if (age > 30) out.push(`⚠️ _catalyst.md is ${age}d old — run /catalyst`);

for (const m of md.matchAll(/\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*\[\[([^\]]+)\]\]\s*\|([^|]*)\|/g)) {
  const diff = Math.round((new Date(m[1]) - now) / 86400000);
  if (diff === 0) out.push(`📅 TODAY: ${m[2]} — ${m[3].trim()}`);
  if (diff === 2) out.push(`⏳ T-2: ${m[2]} — ${m[3].trim()} (${m[1]})`);
}
return out.length ? [{ json: { text: out.join('\n') } }] : [];
```

4. **Telegram** — send `{{ $json.text }}`. Empty array = no message on quiet days.

**Limitation (accepted):** v1 parses only the dated "Next 2 Weeks" table. Week-granularity clusters surface indirectly — the staleness alert forces a `/catalyst` re-run, which promotes approaching events into the dated table.

⚠ **Second limitation, found 2026-07-20 (NOT accepted):** the deployed regex matches only single-wikilink ticker cells — `/catalyst` writes aliased multi-ticker cells (`[[path\|A]], [[path\|B]]`), which the parser skips entirely, so multi-thesis events never alert (the 2026-07-18 GENIUS Act row is a proven miss). Fixed parser in §13.3 card 4 — paste it over the deployed Code node at the next n8n touch.

---

### Workflow 3 — News Sweep (unified: outlet feeds + 4 search engines + body pipeline + Sonnet brief)

**What:** 2×/day sweep of five acquisition channels — the ~94-row `## Outlet Feeds` registry, FMP ticker news, and **GDELT + Brave + Google News each running every thesis ticker AND every News & Thematic row** — → dedupe → headline triage (Haiku) → body pipeline (defuddle full-text fetch + body-informed re-score, Lane A) → **Sonnet-summarised daily intel brief** in `Daily Intel/` + Telegram top-lines. **No `_Inbox/` deposits** (Lane C reverted): the brief is the scanning surface; you hand-pick links for `/ingest`.

**Merge history (2026-07-20, user decision):** v1 News Sweep (GN-only, live 07:00/17:00) and 3b Feed Harvester (in build) merged into this single workflow under the Workflow 3 name — 3b's engine, plus per-ticker coverage replicated across all search channels (v1's weekly per-ticker sweep becomes daily, on four engines). Same-day governance changes: Lane C (auto-clips to `_Inbox/`) **reverted** — output is a brief, not deposits; Lane B **reversed in contained form** — Sonnet authors per-item factual summaries, digest-only (hard rule 2, exception #2). Legacy v1 build preserved at §13.4; it deactivates at §12.5 cutover.

**Mechanism notes:** GN = search-as-RSS headline backstop (redirect-encoded links, `body: false`; decode hack deliberately not built). GDELT free/keyless, 1 req/5s hard limiter → Wait-node pacing; ~100 paced queries put run time at ~15–25 min (fine — it's a background sweep, staggered off other schedules). Brave = paid metered tier (~6,000 queries/mo at full coverage). FMP `stable/news/stock` batch on the existing key — no keyword search (probed conclusively 2026-07-20). **Per-ticker search queries use the company name from the thesis filename, not the raw ticker** — GDELT rejects short quoted terms, and numeric Asia listings ("000660", "2802") are unsearchable as strings while "SK Hynix" and "Ajinomoto" are not.

| | |
|---|---|
| Build effort | ~5–7 h (§12 click-level guide) |
| Running cost | ~$40–75/mo — Haiku triage ~$5–10 (~2–3k items/day post-dedupe) + body re-scores + **Sonnet digest summaries ~$15–35** (every admitted item) + **Brave paid ~$15–25** (metered; verify pricing); GDELT free; FMP existing plan |
| Maintenance | ~20 min/mo — feed rot (zero-item rows in the brief), registry prune, threshold tuning via `### Tuning (body pipeline)` |
| Benefit | **High.** Complete daily coverage — every ticker × 4 engines, every theme × 3 engines, 94 named sources — body-verified scoring, and a readable morning brief instead of a link dump |
| Status | **In build 2026-07-20** — supersedes both v1 (live until cutover) and the 3b plan; §12 build guide, §12.5 cutover |

**Channels:**

| Channel | Intent source | Queries/run | Notes |
|---|---|---|---|
| Outlet feeds | `## Outlet Feeds` rows | ~94 RSS pulls | `triage: no` rows auto-admit; `body_exempt` ids headline-only |
| FMP ticker news | Thesis filenames (ticker prefix, US-listed) | ~3 batch calls | Ticker-scoped only — FMP keyword search conclusively absent |
| GDELT | News & Thematic rows + all ticker company names | ~100, Wait-paced | `gdelt_spacing_s` between calls; quote-drop for terms <5 chars |
| Brave news | Same targets | ~100 | Paid metered tier; `brave_budget_mo` guard raised to 7000 |
| Google News RSS | Same targets | ~100 RSS pulls | Headline-only breadth backstop (`body: false`) |

**Governance:** Rule 1 — writes only new dated files into `Daily Intel/`; `_Inbox/` untouched. Rule 2 — triage and re-score may read bodies (Lane A); the Sonnet summary layer is sanctioned exception #2 (factual per-item sentences, digest-only, no inference). All analysis, propagation, and conviction stay in `/ingest` + skills with full mental-models context.

---

### Workflows 4–5 — X Canary + X Harvester (Twitter intelligence)

X/Twitter intelligence system: all-thesis cashtag harvesting (auto-derived) + AI-curated terms via `_watchers.md § X Watchers`, daily pull cadence, engagement-delta trending detection (→ `Daily Intel/` + Telegram), and dated Obsidian-native dashboards in `Daily Intel/` (newest file = current dashboard) with Opus-graded sentiment, per-theme crowd perspectives, **thesis-divergence detection**, and `_catalyst.md` matching. §7–§11 below are the complete guide — architecture review (§8), then click-level build cards (§9) for **Workflow 4 — X Canary** (§9.4; daily provider-health probe; built first) and **Workflow 5 — X Harvester** (§9.5; the engine; daily, 08:30). **Live since 2026-07-18**: ~$17–40/mo all-in (twitterapi.io ~$2–5 + Anthropic Opus ~$15–35; `llm_model` row is the cost lever). Official X API ruled out (cost + no server-side engagement operators).

---

## 4. What NOT to automate — summary

| Never | Why |
|---|---|
| Direct writes to Theses/Research/Sectors/Macro | Bypasses quality gate, idempotency keys, wikilink-form contract, `propagated_to:` atomicity — the exact failure classes [[INFRASTRUCTURE]] exists to prevent |
| LLM analysis inside n8n | Context asymmetry: no mental models, no READING PROTOCOL, no thesis state. Triage-scoring (headline or full body — Lane A) plus exactly two sanctioned output-side exceptions: Workflow 5's read-only sentiment/divergence layer (dashboard-only) and Workflow 3's Sonnet digest-summary layer (factual per-item sentences, `Daily Intel/` brief only — Lane B rejection reversed in this contained form 2026-07-20). Analytical summarization stays in `/ingest` |
| Tier 3 operations (`/status`, `/prune`, conviction, archive) | Investment decisions with confirmation gates by design |
| Trading actions of any kind | Tripwires are read-the-thesis signals, not execution signals |
| Auto-updating n8n itself | A silently-changed node schema is a silently-dead watcher; update quarterly, deliberately |

---

## 5. Operations

- **Backups (monthly):** `cp -r ~/.n8n ~/n8n-backup-$(date +%F)` — contains the SQLite DB *and* the credential encryption key. Optionally export workflow JSONs into `_Archive/n8n-workflows/` so they version with the vault's git.
- **Watchdog:** §2.5 error workflow is mandatory equipment, not optional.
- **Monthly review (~20 min):** prune expired/orphaned rows in [[_watchers.md]] (move to its Retired section), retune noisy queries, tripwire levels vs current Conviction Triggers, triage threshold, pm2 status. This single file is the whole "what am I tracking" surface — one read tells you everything n8n is pulling.
- **When `/catalyst` or `_catalyst.md` format changes:** re-test the Workflow 2 parser the same day.

### 5.1 Migrating the whole setup to another Mac

The stack is four layers with different transports:

| Layer | Lives in | Moves via |
|---|---|---|
| Knowledge — notes, `_watchers.md`, skills, build docs | GitHub repo | `git clone` |
| Automation — workflows + credentials + their encryption key | `~/.n8n` folder (SQLite DB + config) | copy the folder via AirDrop/USB — **never via the repo**, it contains every API key |
| Local secrets + state — `.data/` | gitignored on purpose | recreate by hand: `config.json` is one line (FMP key); X-harvester state is reseeded per §9.3 — do NOT copy it, it's disposable and sharp again in 2 pulls |
| Runtime — node, n8n, pm2, launchd plist | the old Mac's OS | reinstall per §1 |

Procedure (~30–45 min):

1. **Old Mac — freeze:** `pm2 stop n8n` so nothing writes mid-migration.
2. **Copy `~/.n8n`** to the new Mac. It carries every workflow, every credential, and the encryption key that decrypts them — treat the copy like a password file; wipe the transfer medium after.
3. **New Mac — runtime:** install per §1 (nvm/node → `npm i -g n8n pm2`).
4. **Clone the vault to the same absolute path** `/Users/alexcohen/InvestmentVault`. If the new Mac's username differs, either create a matching account or find-replace the old path in every workflow's file/command nodes, in `N8N_RESTRICT_FILE_ACCESS_TO`, and in the launchd plist — same-username is 10× less error-prone.
5. **Place the `~/.n8n` copy** before n8n's first start.
6. **Recreate `.data/`:** `config.json` with the FMP key (from the FMP dashboard) + reseed the X state file.
7. **Start under pm2 with the §1 env vars** → `pm2 save` → recreate `~/Library/LaunchAgents/pm2.alexcohen.plist` (§1.3) → reboot once to prove auto-start survives.
8. **Verify:** n8n opens → workflows present and still published (the DB carries publish state) → run Workflow 1 — Price Tripwires manually — cheapest end-to-end test of credential + HTTP + Telegram.
9. **Old Mac — decommission the same day:** `pm2 delete n8n` + `launchctl unload -w ~/Library/LaunchAgents/pm2.alexcohen.plist`. **Exactly one machine runs this stack** — two live copies means duplicate Telegram alerts, double API spend, git conflicts on `_Inbox`/dashboard writes, and a forked harvester state.

**Lighter alternative** (no `~/.n8n` copy — sensible if you're changing usernames anyway): export each workflow as JSON (workflow `⋯` → Download) into `_Archive/n8n-workflows/` so they version with the vault, import them on the new machine, and re-paste the four credentials by hand (Telegram, FMP, twitterapi.io, Anthropic). Slower, but forces a hardcoded-path audit as you go.

## 6. Summary — cost & current state

| # | Workflow | Schedule | $/mo | Status |
|---|---|---|---|---|
| 1 | Price Tripwires | daily 07:35 | 0 | **Live** |
| 2 | Catalyst Reminders | daily 07:30 | 0 | **Live** |
| 3 | News Sweep (unified: 5 channels × tickers+themes + body pipeline + Sonnet brief) | 07:00 + 17:00 (07:10/17:10 during calibration) | ~40–75 | **In build** — §12; legacy v1 (GN-only, $0–8) stays live until §12.5 cutover |
| 4 | X Canary | daily 08:00 | ~0 | **Live** — §9.4 |
| 5 | X Harvester | daily 08:30 | ~17–40 | **Live** — §9.5; dated history in `Daily Intel/` |
| — | Error Watchdog | fires by reference | 0 | **Live** — set as Error Workflow in every workflow |

**Totals:** software $0 (n8n Community, fair-code, internal use) · hard running cost typically ~$20–35/mo today (Opus daily is the dominant line; `llm_model` registry row is the lever) — rises to ~$60–110/mo when unified W3 goes live (Sonnet digest summaries + paid Brave join Opus as the dominant lines; `digest_model` registry row is the W3 cost lever) · ongoing maintenance ~30 min/mo (§5 monthly review).

---

## X Intelligence (Workflows 4–5) — overview

Implementation guide for the X/Twitter intelligence system: harvest posts on **every thesis ticker** (cashtags, auto-derived) plus **AI-curated search terms** (registry-driven), pull **daily** with engagement criteria, **diff engagement between pulls** to surface trending posts (`Daily Intel/` + Telegram), and render a **dashboard** with statistics, LLM-gauged sentiment, key crowd perspectives per theme, and **catalyst matching** against [[_catalyst.md]].

**Status: LIVE (built 2026-07-18).** Workflows 4–5 published · daily 08:30 · calibration until 2026-08-01 (§9.8) · dated dashboard history in `Daily Intel/`. Registry: [[_watchers.md]].

---

## 7. Requirements

| # | Requirement | Delivered by |
|---|---|---|
| R1 | Pull on cashtags of ALL thesis docs + AI-curated term list via `_watchers.md` | §8.2 sourcing — auto-derived clusters + `### Curated terms` table |
| R2 | Pull criteria on views/likes/RTs; daily cadence | §8.3 two-stage criteria; daily schedule (3-day during build) |
| R3 | Engagement delta between pulls → trending posts → Telegram + digest in `Daily Intel/` | §8.5 trending engine |
| R4 | Dashboard: stats + LLM sentiment + key perspectives per theme + catalyst matches | §8.6–2.8 dated snapshot in `Daily Intel/` |

---

## 8. Architecture Review

### 8.1 Component map — existing infrastructure vs new setup

| Component | Choice | Status |
|---|---|---|
| Orchestration | n8n under pm2, vault-fenced file access | ✅ **Existing** |
| Notifications | Telegram bot (chat `1779654963`) + Error Watchdog | ✅ **Existing** |
| Config surface | [[_watchers.md]] registry (new `## X Watchers` section: curated terms + `### Tuning` thresholds) | ✅ Existing pattern, new section |
| Ticker universe | `Theses/*.md` frontmatter via Execute Command | ✅ **Existing** (§2.6) |
| Catalyst source | [[_catalyst.md]] (regenerated by `/catalyst`) | ✅ **Existing** |
| Outputs | `Daily Intel/` (snapshots + digests — scanning surfaces) · `.data/` (state). `_Inbox` deliberately unused: digests are not ingest candidates | ✅ Existing pattern |
| Dashboard render | Obsidian-native dated snapshots in `Daily Intel/` — one note per run, newest = current | ✅ Existing app, new folder |
| Tweet DB | JSON state file `.data/x_engagement_state.json` | 🆕 New file, no new software |
| X data | twitterapi.io (third-party API) | 🆕 **New external** — account + ~$1–2/mo |
| Sentiment + thesis-verification LLM | Anthropic API, `claude-opus-4-8`, adaptive thinking, structured outputs | 🆕 **New external** — key + ~$4–8/mo |

**Obsidian-first verdict:** exactly **two** external services (both headless APIs), zero new local software, zero new UI. Every user-facing surface — dashboard, digests, registry — is a vault note: rendered by Obsidian, synced by Obsidian Sync, git-versioned (obsidian-git gives per-pull dashboard history). The state DB is a vault file too but deliberately **machine-local**: `.data/` is gitignored (secrets folder) and dot-folders are invisible to Obsidian Sync.

### 8.2 Sourcing (R1) — two channels, one union

**Channel A — cashtags, zero-maintenance.** Derived at runtime from `Theses/*.md` `ticker:` frontmatter, filtered to US-listed symbols (`^[A-Z]{1,5}$` — foreign listings like `000660.KS` have no liquid cashtag), OR-batched into clusters of 8, with **liquidity-tiered floors** (mega-liquid names drown a low floor; thin names never clear a high one). New thesis → automatically watched next pull. Tier membership = the `mega_tickers` row in `### Tuning` — a judgment list of high-*chatter* cashtags, editable in one cell. Deliberately not auto-derived from market cap: chatter ≠ mcap (PLTR is mega by retail chatter, not size), membership shifts ~yearly, and misclassification self-announces in the dashboard's per-theme volumes for the monthly review to fix.

**Channel B — AI-curated terms, registry-driven.** A `### Curated terms` table inside `_watchers.md § X Watchers`, maintained by Claude in natural language ("track UALink chatter on X"). This is where foreign-listed names (SK Hynix, Advantest…) and thematic phrases live — things cashtags can't express. Same lifecycle mechanics as every registry table: `status`, `expires`, per-row `min_faves`.

### 8.3 Pull criteria & cadence (R2)

**Two-stage criteria** (server-side floor = cost control; client-side gates = quality control):

| Stage | Criterion | Suggested initial value | Rationale |
|---|---|---|---|
| Pull (server-side) | likes ≥ floor | 100 mega-tier · 30 std-tier/terms | Only like-floors are filterable server-side; you never pay for posts below it |
| Track (client-side) | views ≥ 3,000 | hard gate | Ratios on <3k views are statistical noise and trivially fakeable |
| Track | followers ≥ 200 | hard gate | Kills throwaway accounts cheaply |
| Track (any one admits) | like/view ≥ 1.5% · OR RT/view ≥ 0.5% · OR likes ≥ 300 | entry lanes | Ratio lanes find *dense* posts (quality per view); absolute lane keeps already-viral posts trackable |
| Gem flag | like/view ≥ 3% or RT/view ≥ 0.7% | surface immediately | Pre-consensus density — high conversion the attention market hasn't found |

**Thresholds are vault data, not code** (user decision 2026-07-18 — gates will be tested and tuned over time). Every gate above, plus the trending/plateau/prune/cap parameters, is a row in `_watchers.md § X Watchers → ### Tuning` (seeded §9.3), re-parsed on every run: edit the value in Obsidian → the next pull uses it — no redeploy, no n8n UI. The Code nodes keep identical values as **fallback defaults** for missing/malformed rows, so a broken table degrades to seed behavior instead of dying. Ratio gates are percentages in the table (`1.5` = 1.5%). Supporting the tuning loop: the dashboard stamps the active gate set plus a Seen → Admitted funnel every pull (each render attributable to its config), `state.meta.last_cfg` records what ran, and `_watchers.md` git history is the experiment log. All ratio values are priors until calibration (§9.8) resets them at your universe's percentiles.

**Cadence: daily** (raised from every-3-days on 2026-07-18; the 3-day economy setting was the build-phase default). Consequences, honestly stated: reads ~10–20k/mo ≈ $2–5 provider-side; LLM ~$0.5–1.2/pull → ~$15–35/mo; trending-detection latency drops to ~1 day; `since_days` trimmed to 2 (window must stay ≥ cadence + 1). All delta math is cadence-agnostic — it diffs against the previous observation, whenever that was. Cost lever if the bill annoys: flip `llm_model` to `claude-sonnet-4-6` for the daily read and run Opus manually before decisions.

### 8.4 Storage — the tweet DB

**JSON state file: `.data/x_engagement_state.json`.** Schema:

```json
{
  "meta": { "calibration_until": "2026-08-01", "last_run": "", "runs": 0 },
  "posts": { "<tweet_id>": {
      "url": "…", "author": "handle", "followers": 4300,
      "theme": "$MRVL", "text": "first 200 chars…", "first_seen": "…",
      "obs": [["<iso>", 120, 14, 8200]],
      "flags": ["gem"], "plateau_count": 0 } },
  "ratio_log": [[0.031, 0.008]]
}
```

`obs` rows = `[timestamp, likes, RTs, views]`, one appended per pull → the time series that makes delta detection possible (no API sells engagement history; we build it). Lifecycle: admit at entry gates → observe each pull → prune at age > `prune_age_days` (live: 28, raised from the 14 seed on 2026-07-18) or 2 consecutive flat pulls (`plateau_pulls`). **Cap 800 posts** (`cap_tracked`) — all registry-tunable (§8.3).

**Working set, not archive — why the cap is small on purpose.** The state file bounds posts under *simultaneous observation*, not posts ever processed: ~500–1,500 posts flow *through* the tracker monthly (~10–15k/yr). Post-engagement half-life is ~48h — after 14 days a post can never earn another flag, so keeping it buys zero detection power while costing a re-measurement read **every pull** (10k stored posts ≈ $15/mo re-confirming dead posts are dead; the cap keeps cost O(working set)). The durable record of everything that *mattered* lives in the vault already: flagged posts → dated `_Inbox` digests (immutable, git-versioned), aggregates → dashboard, calibration data → `ratio_log`. Sizing: steady state ≈ admissions/pull (~30–150) × residence (~3 pulls) ≈ 100–450; 800 gives earnings-cluster headroom. Known limitation for calibration review: when full, the code refuses new admissions (favors incumbents over new posts — backwards); if the cap is hit in practice, add evict-oldest-plateaued-first.

**Archive-on-prune — built in (user decision 2026-07-18).** At prune time each post's final record (full `obs` engagement history) moves to `state.archive`, retained `archive_days` (Tuning row, default 90) and then dropped. Zero API cost — archived rows never re-enter the re-measurement loop — and bounded: 90 days ≈ 2,500–4,000 records ≈ 2–3 MB of state file, parsed in milliseconds. The LLM still judges only the live working set (recency is the signal); the archive is the retrospective corpus — backtesting crowd sentiment vs price action, decay studies, `Archive:` count in the dashboard header. Want more history? Raise `archive_days`; past ~1 year, graduate to an external append-only store (`.data/x_archive.jsonl` / SQLite) — only at that scale does a separate store earn its keep.

**Rejected alternatives** (the analysis):

| Option | Verdict | Why |
|---|---|---|
| SQLite | ❌ for the working set | n8n Code nodes can't touch it without external dependencies; ceiling here is ~800 posts × ~5 obs ≈ 600 KB — trivially in-memory. SQLite becomes the right answer only for the v2 archive-on-prune corpus (below), which is a separate append-only store, never re-measured |
| External DB / cloud store | ❌ | New infra + credentials for zero benefit at this scale; violates Obsidian-first |
| n8n workflow static data | ❌ | Size-fragile, invisible, not vault-versioned |
| **Vault JSON file** | ✅ | Inside n8n's allowed path, human-inspectable, **machine-local by design** — `.data/` is gitignored (FMP-key folder) and invisible to Obsidian Sync, so no repo churn and no sync-conflict risk against n8n's single-writer updates — and **disposable by design** (loss = cold restart, sharp again in ~2 pulls) |

Single-writer rule: only Workflow 5 (the Harvester) touches it, one scheduled run per day — no locking needed. The dashboard needs **no separate store**: it is regenerated from this state every pull.

### 8.5 Trending engine (R3)

Each pull re-fetches every tracked post (batch lookup, 50 ids/call — provider hard limit) and diffs against the previous observation. Three flags, each fired **once per post per flag** (`flags[]` ledger prevents re-alerts). Conditions shown are seeds — live values are read from the `### Tuning` registry each run (§8.3):

| Signal | Condition (initial) | Delivery |
|---|---|---|
| `gem` | Standalone high engagement-to-view ratio at entry (l/v ≥ 3% or RT/v ≥ 0.7%) | **Pushed** — Telegram + digest (`Daily Intel/`) |
| `trending` | Δlikes ≥ 150 per pull, OR ≥ +60% growth (base ≥ 50) — engagement rising between pulls | **Pushed** — Telegram + digest (`Daily Intel/`) |
| `divergence` | Non-null per-theme divergence from the LLM verification layer (§8.7) | **Pushed** — Telegram `⚠` lines (fires even with zero trending posts) |
| catalyst chatter | Theme ↔ `_catalyst.md` event within ±10 days | **Dashboard-only** — context, never pushed (user decision 2026-07-18) |

The alert stream carries exactly three signal classes — trending delta, standalone high-ratio, genuine thesis divergence — ranked, capped at 12 posts/pull. The digest is a scanning surface; anything substantive still goes through `/ingest` manually.

### 8.6 Dashboard (R4) — architecture decision

| Option | Verdict | Why |
|---|---|---|
| **Obsidian note, regenerated per pull** | ✅ chosen | Native render, zero new tools, versioned, linkable from other notes |
| Obsidian Charts/Dataview plugin | ⚪ optional later | Prettier bars; adds a plugin dependency — v1 uses unicode meters (`▁▃▅▇`) which render everywhere |
| Grafana / Metabase + DB | ❌ | A real dashboarding stack for a ~10-row table; new server, new maintenance, violates Obsidian-first |

**`Daily Intel/` — one dated snapshot per run** (`YYYY-MM-DD HHmm - X Dashboard.md`), written once, never rewritten; the newest file is the current dashboard and the folder is the permanent history (user decision 2026-07-18 — no separate live file). Owned by Workflow 5, never hand-edited. Sections: header stats + gates stamp · compact per-theme table (posts, Σ-likes meter, sentiment, score, trend sparkline — short cells only) · **⚠ Thesis divergence** · **Crowd perspectives** (summary + shift + bullets per theme) · catalyst chatter · flagged-this-pull. Layout rule: long text never goes in table cells — perspectives and divergence render as sections, so the table never needs horizontal scrolling.

**"Can dashboarding genuinely be done in Obsidian?"** — Yes, with proof in this vault: [[Watchlist.md]] is already a live interactive dashboard (DataviewJS, on-click FMP refresh across 70 tickers, holdings chart). The dashboard upgrade ladder: v1 = regenerated tables + unicode meters (native); v1.5 = **Mermaid `xychart-beta`** bar/line charts — the Harvester emits a text block, Obsidian renders it with no plugin; v2 = Obsidian Charts plugin or a DataviewJS interactive view on the state JSON (the Watchlist pattern). What Obsidian can't do — streaming, Grafana-class drill-downs — is irrelevant at a 3-day data cadence. Example v1.5 block the Harvester can emit:

```
mermaid
xychart-beta
  title "Crowd sentiment score by theme"
  x-axis [MRVL, NVDA, AMD, thematic]
  y-axis "score" -2 --> 2
  bar [1, 2, -1, 0]
```
(rendered as a fenced ```mermaid block)

### 8.7 LLM layer — sentiment, perspectives, and thesis verification

Each pull makes **one** n8n HTTP call to the Anthropic API carrying every active theme in a single prompt (upgraded per user decisions 2026-07-18).

**Inputs per theme:**

- **Thesis context** — the six analytical sections (Summary, Key Non-consensus Insights, Bull Case, Bear Case, Risks, Outstanding Questions), shell-extracted at run time, ~5k tokens/theme. Feeding Bear Case + Risks is what makes divergence *genuine*: crowd echoing a risk the thesis already carries is NOT divergence.
- **Crowd posts** — top `llm_top_n` (default 15) for the theme from the **entire tracked DB**: new admissions AND previously tracked posts, each at up to 1,000 chars with follower/like/view stats inline. The model always judges the merged working set, engagement-weighted, never just this pull's tweets.
- **Longitudinal memory** — PRIOR READS: the engine's own dated per-theme reads (`state.sentiment_log`, ≤90 days, ≤30 entries) + HISTORICAL ANCHOR POSTS: top-5 highest-engagement archived posts per theme, dated. Current posts stay the dominant evidence (recency bias by instruction); the memory tiers exist so the model can judge `shift` — how the crowd argument has moved over time.
- Full-document ingestion is possible (~$20–40/mo) but spends most tokens on metrics tables irrelevant to the judgment — one-line change if ever wanted.

**Outputs per theme** (schema-enforced):

| Field | Values |
|---|---|
| `summary` | 2–4 sentences — the crowd narrative synthesised, engagement-weighted |
| `sentiment` | bullish · bearish · mixed · quiet |
| `score` | −2…+2 — numeric read for the dashboard column + the Trend sparkline |
| `shift` | 1–2 sentences — how sentiment and the dominant argument moved vs the prior reads (null if stable/no history) |
| `perspectives` | 2–6 objects `{text, refs}` — the argument (1–2 sentences, the posts' specific numbers/claims) plus the labels of the exact posts it draws from; rendered as author-linked citations on each bullet |
| `divergence` | one substantive crowd argument the thesis doesn't already carry — or null |

`divergence` is **one synthesis per theme, judged across all posts together — never per tweet**: a specific crowd argument that contradicts, challenges, or is unaddressed by the thesis; crowd merely echoing a known risk/bear point → null. This is a crowd-vs-thesis expectations-gap detector ([G-13]); non-null divergence surfaces in the dashboard column and as Telegram `⚠` lines even on pulls with zero trending posts.

**Boundary — read-vault yes, write-vault no** (upgraded from the old "no vault context in n8n's LLM" rule):

- The LLM reads thesis sections *in order to compare*; output lands only in the regenerated dashboard.
- Never into Theses/, never into Research/, never into `/sync` propagation.
- A divergence flag is a *prompt to investigate* (`/stress-test`, `/ingest`, or an attended in-vault Claude session with full mental-models context) — never a verdict, never written into a thesis spine.

**Call shape** (one HTTP call per pull):

- `POST https://api.anthropic.com/v1/messages` · headers `x-api-key` + `anthropic-version: 2023-06-01`
- Model: the `llm_model` row in the Tuning registry — default `claude-opus-4-8` (user decision: stock-sentiment verification needs real reasoning); switch models by cell edit, reason in `notes`. A typo'd model string 400s harmlessly → "LLM unavailable this pull". Runs with `thinking: {type: "adaptive"}` — current-gen models only
- Prompt: the analytical instructions live in `_watchers.md § X Watchers → ### LLM prompt` (fenced block, re-read every pull; Code X holds an identical fallback) — tune the guidance over time like any gate. The output field names/types are pinned by the schema; edit judgment criteria, never the field list
- Structured outputs (`output_config.format` + JSON schema) — response schema-guaranteed even with thinking on; text block extracted by type, so thinking blocks never break parsing
- `max_tokens: 32000` (thinking tokens count against it — 16k proved too small once full theses flowed) · node timeout 600s
- Volume: ~15 themes × (six sections ≤12k chars + prior reads + 5 anchors + top-15 live posts) ≈ 80–200k in / ≤16k out per pull → ~10 pulls/mo at $5/$25 per MTok ≈ **$8–20/mo** at full 90-day memory depth

**Failure isolation:** the LLM node runs On-Error-Continue — if Anthropic errors, the dashboard renders "LLM unavailable this pull"; state, deltas, digest, and catalyst match complete untouched. The verification layer can never kill a harvest. Divergence quality tracks thesis-section freshness — the existing `/numbers` flagging + `/deepen --sync-metrics` hygiene keeps stances current.

### 8.8 Catalyst matching

Pure Code-node logic, no API:

1. **Parse** `_catalyst.md`'s dated table rows (`| YYYY-MM-DD | [[TICKER]] | event |`)
2. **Filter** to events within ±10 days of the pull
3. **Intersect** with themes that currently have tracked posts
4. **Render** as the dashboard's catalyst-chatter section

**Dashboard-only** — context, never the Telegram/`_Inbox` alert stream (user decision 2026-07-18: pushes are reserved for trending, high-ratio, and genuine divergence). Dependency: match quality degrades with a stale calendar — Workflow 2's staleness nag is the existing guard.

### 8.9 Cost & dependency summary

| Item | Monthly | Notes |
|---|---|---|
| twitterapi.io | ~$2–5 | ~350–650 reads/day at daily cadence. Buy: $5 top-ups; refill when near zero, never hold more — provider-death stranding |
| Anthropic API | ~$15–35 | Daily Opus 4.8 + adaptive thinking; thesis sections + 90-day sentiment memory + anchors + top-15 live posts per theme. Cost lever: `llm_model` → Sonnet |
| Software / dashboards / DB | $0 | Obsidian render + n8n + vault JSON state — all existing |
| **Total** | **~$17–40/mo** | Plus the standing monthly review |

---

## 9. Step-by-step build

### 9.0 Order of work & pre-flight

1. Accounts + credentials (§9.1) → 2. Verification calls — **the gate** (§9.2) → 3. Seed state + registry (§9.3) → 4. `Workflow 4 — X Canary` (§9.4, build first) → 5. `Workflow 5 — X Harvester` (§9.5–3.6) → 6. First run + publish (§9.7) → 7. Two-week calibration (§9.8)

**Pre-flight — tick every box before spending a dollar:**

- [ ] n8n up: browser → `http://localhost:5678` shows the editor
- [ ] pm2 healthy: Terminal → `pm2 status` → n8n `online`
- [ ] Vault file fence live: `pm2 status` → note n8n's id number → `pm2 env <id> | grep RESTRICT` → shows `/Users/alexcohen/InvestmentVault`
- [ ] Telegram credential + `Error Watchdog` workflow exist (Workflows 1–3 already use both)
- [ ] `_catalyst.md` fresh (<60d old — otherwise run `/catalyst` first; catalyst matching degrades silently on a stale calendar)
- [ ] Thesis frontmatter complete: Terminal → `grep -L "^ticker:" "/Users/alexcohen/InvestmentVault/Theses/"*.md` — any file it prints has no `ticker:` line and will be invisible to the cashtag channel and the LLM layer (fine for drafts; fix ones you want tracked)

**n8n canvas basics** — the five moves every build card below assumes:

| Move | How |
|---|---|
| Add node | `+` top-right of canvas (or drag off a node's right-edge circle) → search name → click |
| Connect | drag from a node's right-edge circle to the next node's left edge |
| Rename | open the node (double-click) → click its name at the top → type → Enter |
| On Error | open the node → **Settings** tab (beside Parameters) → **On Error** dropdown |
| Expression | hover a field → flick the `fx`/Expression toggle → anything in `{{ }}` now evaluates. Fields stay **Fixed** unless a build card explicitly says "→ Expression" |

**Execute step** (button inside an open node) runs the chain up to and including that node. **Test workflow** (bottom of canvas) runs everything once. Neither requires publishing.

### 9.1 Accounts & credentials (~15 min)

**Step 1 — twitterapi.io account (browser):**

1. Go to `https://twitterapi.io` → **Sign up** (Google login is fine).
2. Open the dashboard — your **API key** (a long string) is displayed there. Keep the tab open.
3. Check for free trial credits (most new accounts get some). If present, **do not top up yet** — trial credits cover §9.2. If absent, top up the minimum (≤$5).
4. On their docs page, note the exact **auth header name** they specify (expected: `X-API-Key`).

**Step 2 — twitterapi.io credential in n8n:**

1. n8n (`http://localhost:5678`) → left sidebar → **Credentials** → **Add credential**.
2. Search **Header Auth** → **Continue**.
3. Fill: credential name (click the title at the top of the window): `TwitterAPI-io` · **Header Name**: `X-API-Key` (whatever Step 1.4 said) · **Header Value**: paste the key → **Save**.

**Step 3 — Anthropic account (browser):**

1. Go to `https://console.anthropic.com` (redirects to the current console) → sign in / sign up.
2. **API Keys** → **Create Key** → name it `n8n-x-harvester` → **copy it NOW** — it is shown exactly once.
3. **Billing** → buy **$10** of prepaid credits. This billing is fully separate from any Claude subscription; the n8n calls draw from these credits.

**Step 4 — Anthropic credential in n8n:**

1. **Credentials** → **Add credential** → **Header Auth** → **Continue**.
2. Name `Anthropic` · **Header Name**: `x-api-key` (exactly this, lowercase) · **Header Value**: paste the key → **Save**.
3. The second required header (`anthropic-version: 2023-06-01`) is NOT part of the credential — it is added per-request inside the HTTP node (§9.5 card 14).

**Key hygiene:** both keys now live only inside n8n credentials — never in chat, never in a vault file.

### 9.2 Verification calls (the gate — ~$0.50, ~30 min)

Five checks that decide whether the project proceeds. Everything here is throwaway.

**Setup:**

1. n8n → **Overview** → **Create Workflow** → click the `My workflow` title → rename `X Verify (throwaway)`.
2. Add the manual trigger: `+` → search `Manual` → pick **"When clicking 'Test workflow'"** (the manual trigger; label varies slightly by version).
3. Add an **HTTP Request** node, connect it, configure:
   - **Method**: `GET`
   - **URL**: `https://api.twitterapi.io/twitter/tweet/advanced_search`
   - **Authentication**: `Generic Credential Type` → **Generic Auth Type**: `Header Auth` → select `TwitterAPI-io`
   - **Send Query Parameters**: ON → **Add Parameter** twice:
     - Name `queryType` · Value `Latest`
     - Name `query` · Value `$MRVL min_faves:100 since:2026-07-11` — plain text, no quotes, date set to ~7 days before your test day
4. Open the node → **Execute step** → output appears on the right; flip between **Table** and **JSON** views to inspect.

**The five checks** (record pass/fail for each):

| # | Do | PASS when |
|---|---|---|
| 1 | Inspect every returned tweet's like count | all ≥ 100 — the server-side floor is honored, not theater |
| 2 | Delete ` min_faves:100` from the query → Execute step again | visibly MORE results — the floor genuinely prunes what you pay for. Restore the query after |
| 3 | Copy one tweet's `url` → open in browser → compare live likes vs the API number | within ±10% — snapshots are fine for thresholds, never for exact figures |
| 4 | Second HTTP node, same auth: URL `https://api.twitterapi.io/twitter/tweets` · query param `tweet_ids` = three ids from check 1, comma-separated → Execute step | all three return, each with engagement metrics — re-measurement depends on this endpoint |
| 5 | In BOTH nodes' outputs, find the view-count field | present, non-null, plausible (views ≥ likes) on essentially every tweet — every ratio gate depends on it |

**While in the JSON view, write down the exact field names** for: tweets array, id, url, text, like count, retweet count, view count, author handle, author followers. Expected: `tweets[]` · `id` · `url` · `text` · `likeCount` · `retweetCount` · `viewCount` · `author.userName` · `author.followers`. If any differ, `norm()` in Code X (§9.6) is the ONLY place they get fixed.

**Anthropic smoke test** — third HTTP node:

- **Method** `POST` · **URL** `https://api.anthropic.com/v1/messages`
- **Authentication**: Header Auth → `Anthropic`
- **Send Headers**: ON → Name `anthropic-version` · Value `2023-06-01`
- **Send Body**: ON → **Body Content Type** `JSON` → **Specify Body** `Using JSON` → paste:

```json
{"model":"claude-opus-4-8","max_tokens":256,"messages":[{"role":"user","content":"Reply with exactly: ok"}]}
```

- **Execute step** → PASS: response contains a `content` array with a text block saying `ok`.

**Decision:** all five pass → top up twitterapi.io to $5 (if still on trial credits) and proceed to §9.3. Any hard fail on 1–5 → repeat this section against the fallback twin **socialdata.tools** (different base URLs + its own credential, same checks) before abandoning. Delete the throwaway workflow when done.

### 9.3 Seed state + registry (~5 min)

**State file** — one paste in Terminal. It creates the folder if needed, seeds the DB with a 14-day calibration window from today, and prints the file back so you can verify in the same step:

```
mkdir -p "/Users/alexcohen/InvestmentVault/.data" && printf '{"meta":{"calibration_until":"%s","last_run":"","runs":0},"posts":{},"ratio_log":[]}' "$(date -v+14d +%F)" > "/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json" && cat "/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json"
```

Expected output: one JSON line ending in `"posts":{},"ratio_log":[]}` with `calibration_until` = today + 14 days. The file is disposable by design — delete it any time and the engine cold-starts.

**Sync note:** this file stays on this Mac only — `.data/` is gitignored (it already holds the FMP key; the ignore predates this build) and dot-folders are invisible to Obsidian Sync. Correct behavior: single-writer (§8.4), disposable, zero sync-conflict risk. The dashboard, digests, and registry are normal notes and sync/version as usual.

**Registry** — append the block below to [[_watchers.md]]: open it in Obsidian → scroll past the end of `## Alt-Data Pollers` → paste. (Or just ask Claude: *"append the §9.3 X Watchers block from n8n Automations.md to _watchers.md"*.)

````markdown
## X Watchers

Drives Workflow 5 — X Harvester (n8n Automations §7–§11). Cashtag clusters are auto-derived from Theses/ frontmatter —
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
| since_days | 2 | search window; keep ≥ cadence + 1 (trimmed 4→2 with daily cadence) |
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
| prune_age_days | 28 | max observation age — 14→28 (2026-07-18, user): longer trending window, ~2× re-measure reads |
| cap_tracked | 800 | working-set cap (§8.4) |
| llm_top_n | 15 | posts per theme fed to the sentiment LLM |
| llm_model | claude-opus-4-8 | sentiment/divergence model; current-gen only (body sends adaptive thinking) |
| archive_days | 90 | pruned posts retained in state archive — analysis corpus, never re-measured |

### LLM prompt

Analytical instructions for the sentiment/divergence call — the fenced block below is read on every
pull (fallback: identical default inside Code X). Output field names/types (`summary`, `sentiment`,
`score`, `perspectives`, `divergence`) are pinned by the workflow schema — edit the analytical
guidance freely, never the field list.

```
For each theme below you get MY THESIS (six analytical sections), PRIOR READS (dated sentiment reads produced by this engine over the past 90 days), HISTORICAL ANCHOR POSTS (highest-engagement posts from the 90-day archive, dated, labeled [A1], [A2], …), and CURRENT CROWD POSTS with engagement stats (labeled [P1], [P2], …) — current posts are drawn from every post tracked live for that theme, not just newly pulled ones. Weight CURRENT posts most: they are the consumption signal; use PRIOR READS and ANCHOR POSTS as longitudinal context, not as current evidence. Return per theme: summary — 2-4 sentences synthesising the current crowd narrative: what the crowd believes, where the argument concentrates, what evidence they cite; weight higher-engagement, higher-follower posts more. sentiment (bullish/bearish/mixed/quiet). score (-2..2). shift — 1-2 sentences on how crowd sentiment and the dominant argument have moved versus the PRIOR READS: new arguments appearing, old ones dying, conviction hardening or fading; null if there is no meaningful history or no real change. perspectives — 2-6 distinct crowd arguments; each has text (1-2 sentences carrying the specific numbers, names, and claims from the posts, never generic labels) and refs (the labels of the 1-3 specific posts that argument draws from, e.g. ["P2","A1"] — use only labels that appear above). divergence — ONE synthesis judged across all the posts together, never per post: a specific, substantive crowd argument that contradicts, challenges, or is unaddressed by my thesis. If the crowd merely echoes a risk or bear point my thesis already carries, that is NOT divergence — return null. Judge on substance of claims, not tone; ignore hype and spam; return null unless the tension is genuine. Positioning gauge, not advice.
```
````

**Verify:** reopen `_watchers.md` in reading view — two tables (`Curated terms`, 5 rows; `Tuning`, 21 rows) plus the `### LLM prompt` fenced block render. Tuning values equal the code defaults, so the engine behaves identically with or without the paste — but only a pasted table is editable per §8.3.

### 9.4 `Workflow 4 — X Canary` (build FIRST; daily 08:00; ~15 min)

Four nodes. Built first because it end-to-end tests credential → search → Telegram before you invest in the big workflow, then stays on as the provider-health probe (silent thin results → loud alert).

1. **Create Workflow** → rename `Workflow 4 — X Canary`.
2. **Node 1 — Schedule Trigger**: **Trigger Interval** `Days` · **Days Between Triggers** `1` · **Trigger at Hour** `8am` · **Trigger at Minute** `0`.
3. **Node 2 — HTTP Request** (connect from 1): **Method** `GET` · **URL** `https://api.twitterapi.io/twitter/tweet/advanced_search` · **Authentication** → Header Auth → `TwitterAPI-io` · **Send Query Parameters** ON:
   - Name `queryType` · Value `Latest`
   - Name `query` · Value → toggle **Expression** (`fx`) → paste: `{{ '$NVDA min_faves:500 since:' + new Date(Date.now() - 3*86400000).toISOString().slice(0,10) }}` — a rolling 3-day window that never needs editing
4. **Node 3 — Code** (connect from 2): **Mode** `Run Once for All Items` → delete the boilerplate → paste:

```javascript
return ($input.first().json.tweets || []).length === 0 ? [{ json: { text: '⚠️ X provider degraded — canary empty' } }] : [];
```

5. **Node 4 — Telegram** (connect from 3): existing Telegram credential · **Chat ID** `1779654963` · **Text** → Expression → `{{ $json.text }}`.
6. Workflow menu (`⋯` top right) → **Settings** → **Error Workflow** → `Error Watchdog` → Save.
7. **Test workflow** once. Success = node 3 outputs **0 items** and Telegram shows as not executed — `$NVDA` at `min_faves:500` always has results when the provider is healthy. If the ⚠️ message DOES arrive, provider or query is broken; fix before building Workflow 5.
8. **Publish**.

### 9.5 `Workflow 5 — X Harvester` — build (~60–90 min)

**Create Workflow** → rename `Workflow 5 — X Harvester`. 23 nodes; the summary table is the reference, the build cards below it walk every click.

**Summary table** (⚠ commands here escape `|` as `\|` for table rendering — copy commands only from the build cards, never from this table):

| #     | Node                                       | Settings                                                                                                                                                                                                                                                                                                                                                           |
| ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Schedule Trigger                           | Days · Days Between Triggers `1` · 8am · min 30                                                                                                                                                                                                                                                                                                                    |
| 2     | Execute Command — `Tickers`                | `grep -h "^ticker:" "/Users/alexcohen/InvestmentVault/Theses/"*.md \| sed 's/^ticker: *//'`                                                                                                                                                                                                                                                                        |
| 2b    | Execute Command — `Summaries`              | `for f in "/Users/alexcohen/InvestmentVault/Theses/"*.md; do t=$(grep -m1 '^ticker:' "$f" \| sed 's/^ticker: *//'); s=$(awk '/^## (Summary\|Key Non-consensus Insights\|Bull Case\|Bear Case\|Risks\|Outstanding Questions)$/{f=1;print;next}/^## /{f=0}f' "$f" \| head -c 20000); printf '### %s\n%s\n' "$t" "$s"; done` — the six analytical sections per thesis |
| 3     | Read/Write Files                           | Read `_watchers.md`                                                                                                                                                                                                                                                                                                                                                |
| 4     | Extract from File — `Extract Watchers`     | Text                                                                                                                                                                                                                                                                                                                                                               |
| 5     | Read/Write Files — `Read State`            | Read `.data/x_engagement_state.json` · On Error: Continue (regular output)                                                                                                                                                                                                                                                                                                          |
| 6     | Extract from File — `Extract State`        | Text · On Error: Continue (regular output)                                                                                                                                                                                                                                                                                                                                          |
| 7     | Read/Write Files                           | Read `_catalyst.md`                                                                                                                                                                                                                                                                                                                                                |
| 8     | Extract from File — `Extract Catalyst`     | Text                                                                                                                                                                                                                                                                                                                                                               |
| 9     | Code — `Plan`                              | **Code P**                                                                                                                                                                                                                                                                                                                                                         |
| 10    | Switch                                     | on `{{ $json.mode }}`: `remeasure` → output 0, `discover` → output 1                                                                                                                                                                                                                                                                                               |
| 11a   | HTTP — `Batch Lookup` (from 0)             | GET `https://api.twitterapi.io/twitter/tweets?tweet_ids={{ $json.ids }}` · `TwitterAPI-io` · Batching 3/1000ms · On Error: Continue (regular output)                                                                                                                                                                                                                                |
| 11b   | HTTP — `Search` (from 1)                   | GET `{{ $json.url }}` · same settings                                                                                                                                                                                                                                                                                                                              |
| 12    | Merge                                      | Append (inputs from 11a + 11b)                                                                                                                                                                                                                                                                                                                                     |
| 13    | Code — `Analyze`                           | **Code X** — the engine                                                                                                                                                                                                                                                                                                                                            |
| 14    | HTTP — `Sentiment` (from 13)               | POST `https://api.anthropic.com/v1/messages` · Header Auth `Anthropic` · add header `anthropic-version: 2023-06-01` · Body: JSON → `={{ JSON.stringify($json.llm_body) }}` · Timeout **600000** (Opus + thinking + long output) · On Error: Continue (regular output)                                                                                                                             |
| 15    | Code — `Assemble` (from 14)                | **Code D** — dashboard + digest                                                                                                                                                                                                                                                                                                                                    |
| 16→17 | Convert to File (`state_json`) → Write     | Path `/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json` — from **15 `Assemble`** (always runs; 14 continues on error), so the write carries the sentiment ledger                                                                                                                                                                                                                        |
| 18→19 | Convert to File (`dash_body`) → Write      | Path → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.dash_fname }}` — one dated file per run; newest = current dashboard                                                                                                                                                                                                |
| 20    | IF (from 15)                               | `{{ $json.text }}` · is not empty                                                                                                                                                                                                                                                                                                                                  |
| 20b   | IF — `If digest` (from 20-true)            | `{{ $json.fname }}` · is not empty — file gate (divergence-only pulls push Telegram but write no digest) |
| 21    | Telegram (IF-true)                         | Chat `1779654963` · `{{ $json.text }}`                                                                                                                                                                                                                                                                                                                             |
| 22→23 | Convert to File (`body`) → Write (from 20b-true) | Path `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.fname }}` |                                                                                                                                                                                                |

> **Node names are load-bearing.** The Code nodes fetch other nodes' data by name: `$('Tickers')`, `$('Summaries')`, `$('Extract Watchers')`, `$('Extract State')`, `$('Extract Catalyst')`, `$('Analyze')`, `$('Assemble')`. Rename each node to the exact name in its card — one character off and the run dies with "Referenced node doesn't exist".

**Wiring map** (what connects to what):

- `1 → 2 → 2b → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10` — one straight chain. Deliberately NOT parallel: the chain exists to guarantee execution order for the by-name `$('…')` lookups (the Code nodes ignore what flows into them), and fanning 2/2b into 3 without a Merge would make n8n run everything downstream once per branch — a double harvest, double LLM call, duplicate alerts
- `10` output **remeasure** → `11a` · output **discover** → `11b`
- `11a` → `12` **Input 1** · `11b` → `12` **Input 2**
- `12 → 13 → 14 → 15`
- `16 → 17` (state save) hangs off **`15 Assemble`** — downstream of the LLM on purpose: the write must include the sentiment ledger, which only exists after the LLM answers. Safe because node 14 is On-Error-Continue, so `Assemble` (and therefore the state write) runs even when the LLM fails
- `15 → 18 → 19` (dashboard snapshot → `Daily Intel/`, one dated file per run) **and** `15 → 20` (IF)
- `20` **true** → `21` (Telegram) **and** `20` **true** → `20b If digest` → **true** → `22 → 23` (digest file) · all **false** branches → nothing. Two gates because the two pushes have different conditions: Telegram fires on `text` (any push, including divergence-only); the file writes only when `fname`/`body` exist (flagged posts present)

**Build cards** — top to bottom; any field not mentioned stays at default:

**1 · Schedule Trigger** — **Trigger Interval** `Days` · **Days Between Triggers** `1` · **Trigger at Hour** `8am` · **Trigger at Minute** `30` (daily since 2026-07-18; `3` was the build-phase economy default).

**2 · Execute Command — rename `Tickers`** — n8n ≥2.0 hides Execute Command by default (v2 breaking change); if it's missing from the node panel, apply the one-time re-enable in §9.7's troubleshooting table, then return here. **Command**:

```
grep -h "^ticker:" "/Users/alexcohen/InvestmentVault/Theses/"*.md | sed 's/^ticker: *//'
```

**2b · Execute Command — rename `Summaries`** — **Command**:

```
for f in "/Users/alexcohen/InvestmentVault/Theses/"*.md; do t=$(grep -m1 '^ticker:' "$f" | sed 's/^ticker: *//'); s=$(awk '/^## (Summary|Key Non-consensus Insights|Bull Case|Bear Case|Risks|Outstanding Questions)$/{f=1;print;next}/^## /{f=0}f' "$f" | head -c 20000); printf '### %s\n%s\n' "$t" "$s"; done
```

**3 · Read/Write Files from Disk** — **Operation** `Read File(s) From Disk` · **File(s) Selector** `/Users/alexcohen/InvestmentVault/_watchers.md`.

**4 · Extract from File — rename `Extract Watchers`** — **Operation** `Text`.

**5 · Read/Write Files from Disk — rename `Read State`** — **Operation** `Read File(s) From Disk` · **File(s) Selector** `/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json` · **Settings → On Error** `Continue (using regular output)` (a missing/corrupt state file must never kill a run — the code cold-starts instead).

**6 · Extract from File — rename `Extract State`** — **Operation** `Text` · **Settings → On Error** `Continue (using regular output)`.

**7 · Read/Write Files from Disk** — **Operation** `Read File(s) From Disk` · **File(s) Selector** `/Users/alexcohen/InvestmentVault/_catalyst.md`.

**8 · Extract from File — rename `Extract Catalyst`** — **Operation** `Text`.

**9 · Code — rename `Plan`** — **Mode** `Run Once for All Items` · paste **Code P** per §9.6.

**10 · Switch** — the sorter: `Plan` emits a mixed stream (re-measure ID batches + discovery search URLs); the Switch reads each item's `mode` field and routes it to the right HTTP node.

1. Add **Switch** (connect from `Plan`) · **Mode**: leave `Rules`.
2. **Routing Rule 1** — the condition row is `[value] [is equal to] [value]`: left box → **Expression** → `{{ $json.mode }}` · middle dropdown stays `is equal to` (String) · right box → type `remeasure` (plain text, Fixed, no braces) · toggle **Rename Output** ON → `remeasure`.
3. **Add Routing Rule** → Rule 2: left box → Expression → `{{ $json.mode }}` · `is equal to` · right box `discover` · Rename Output → `discover`.
4. The node now shows two labeled output dots on its right edge — `remeasure` (→ card 11a) and `discover` (→ card 11b).
5. Sanity: **Execute step** → first run shows `remeasure: 0 items` (nothing tracked yet — correct) and `discover: ~15–20 items`.

**11a · HTTP Request — rename `Batch Lookup`** (connect from the **remeasure** output) — **Method** `GET` · **URL** → Expression → `https://api.twitterapi.io/twitter/tweets?tweet_ids={{ $json.ids }}` · **Authentication** → Header Auth → `TwitterAPI-io` · **Options → Add option → Batching** → Items per Batch `3` · Batch Interval (ms) `1000` · **Settings → On Error** `Continue (using regular output)`.

**11b · HTTP Request — rename `Search`** (connect from the **discover** output) — **Method** `GET` · **URL** → Expression → `{{ $json.url }}` · **Authentication** → Header Auth → `TwitterAPI-io` · **Options → Batching** `3` / `1000` · **Settings → On Error** `Continue (using regular output)`. *(v1 reads only the first result page per query — keeps cost fixed; if a cluster feels thin, raise its floor or split the cluster rather than paginating.)*

**12 · Merge** — **Mode** `Append` · **Number of Inputs** `2` · wire `Batch Lookup` → **Input 1**, `Search` → **Input 2**.

**13 · Code — rename `Analyze`** — **Mode** `Run Once for All Items` · paste **Code X** per §9.6.

**14 · HTTP Request — rename `Sentiment`** (connect from `Analyze`) — **Method** `POST` · **URL** `https://api.anthropic.com/v1/messages` · **Authentication** → Header Auth → `Anthropic` · **Send Headers** ON → Name `anthropic-version` · Value `2023-06-01` · **Send Body** ON → **Body Content Type** `JSON` → **Specify Body** `Using JSON` → JSON field → Expression → `{{ JSON.stringify($json.llm_body) }}` · **Options → Timeout** `600000` · **Settings → On Error** `Continue (using regular output)`.

**15 · Code — rename `Assemble`** (connect from `Sentiment`) — **Mode** `Run Once for All Items` · paste **Code D** per §9.6.

**16 · Convert to File** (drag a SECOND wire off `Assemble`) — **Operation** `Convert to Text File` · **Text Input Field**: type the field name `state_json` — the NAME of the field, not its contents. (Downstream of the LLM so the sentiment ledger is included; `Assemble` always runs because node 14 continues on error.)

**17 · Read/Write Files from Disk** (from 16) — **Operation** `Write File to Disk` · **File Path and Name** `/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json` · **Input Binary Field** `data`.

**18 · Convert to File** (from `Assemble`) — **Operation** `Convert to Text File` · **Text Input Field** `dash_body`.

**19 · Read/Write Files from Disk** (from 18) — **Operation** `Write File to Disk` · **File Path and Name** → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.dash_fname }}` · **Input Binary Field** `data`. One dated file per run — no separate live file; the newest file in `Daily Intel/` IS the current dashboard (date-prefixed names sort chronologically).

**20 · If** — the push gate: `Assemble` ALWAYS outputs the dashboard, but only outputs `text` (Telegram) + `body` (digest) when something was flagged. This node asks "anything to push?" so quiet pulls end silently.

1. Add **If** — drag a SECOND wire off `Assemble`'s output dot (one output feeding many nodes is fine; only converging *inputs* need Merge).
2. Condition row: left box → **Expression** → `{{ $json.text }}` · comparator dropdown → **String → is not empty**. The right-hand box disappears — this operator needs no comparison value.
3. Two outputs: **true** (top) → two wires, to card 21 (Telegram) and card 20b (`If digest`). **false** (bottom) → connect nothing — the silent exit.
4. Sanity: run #1 takes the false path (nothing flagged in calibration) — Telegram skipped = success. If the node complains about types on quiet pulls (`text` undefined), enable its looser type-validation option: undefined counts as empty → routes false.

**20b · If — rename `If digest`** (SECOND wire off card 20's **true**) — the file gate: a divergence-only pull carries Telegram `text` but no digest `body`; without this gate the Convert/Write pair hard-fails on the missing file and aborts the run. Condition: left box → **Expression** → `{{ $json.fname }}` · **String → is not empty**. **true** → card 22 · **false** → nothing.

**21 · Telegram** (from IF **true**) — existing credential · **Chat ID** `1779654963` · **Text** → Expression → `{{ $json.text }}`.

**22 · Convert to File** (from `If digest` **true**) — **Operation** `Convert to Text File` · **Text Input Field** `body`. On Error stays at default (`Stop Workflow`) — behind the gate, an error here is real and should fail loud.

**23 · Read/Write Files from Disk** (from 22) — **Operation** `Write File to Disk` · **File Path and Name** → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.fname }}` · **Input Binary Field** `data`.

**Finish:** Workflow menu (`⋯`) → **Settings** → **Error Workflow** → `Error Watchdog` → Save. **Do NOT Publish yet** — §9.7's manual first run comes first.

### 9.6 The three Code nodes

Paste rules, identical for all three: open the node → **Mode** `Run Once for All Items` → select ALL boilerplate in the editor → delete → paste the block → Save. The code reaches other nodes via `$('Name')`, so the §9.5 node names must already be exact. If the editor shows red underlines after pasting, the paste was partial — clear and re-paste the whole block.

**Code P** (`Plan`):

```javascript
// ---- FALLBACK DEFAULTS — live values come from _watchers.md § X Watchers → ### Tuning ----
const DEF = { floor_mega: 100, floor_std: 30, since_days: 4, prune_age_days: 14, plateau_pulls: 2,
  mega_tickers: 'NVDA,AMD,TSM,META,PLTR,AVGO,INTC,NET,NOW,CRWD,UBER,SHOP,NFLX,MU' };
const cfgOf = (md, def) => {
  const c = { ...def }, sec = (md.split('### Tuning')[1] || '').split(/\n#{2,3} /)[0];
  for (const m of sec.matchAll(/^\|\s*([A-Za-z_]+)\s*\|\s*([^|]+?)\s*\|/gm)) {
    const k = m[1].toLowerCase(), v = m[2].trim();
    if (k in def && v !== '') c[k] = typeof def[k] === 'string' ? v : (isFinite(+v) ? +v : def[k]);
  }
  return c;
};
const wmd = $('Extract Watchers').first().json.data || '';
const cfg = cfgOf(wmd, DEF);
const MEGA = String(cfg.mega_tickers).split(',').map(s => s.trim().toUpperCase()).filter(Boolean);
// -----------------------------------------------------------------------------------------
let state = {};
try { state = JSON.parse($('Extract State').first().json.data); } catch (e) {}
const posts = state.posts || {};
const now = Date.now();
const out = [];

// 1. Re-measure tracked posts (within prune_age_days, not plateaued) — batches of 50
// (provider hard limit: max 50 tweet_ids/call — 400s above that; hit live 2026-07-19 at 108 tracked)
const ids = Object.entries(posts)
  .filter(([, p]) => (now - new Date(p.first_seen)) < cfg.prune_age_days * 86400000 && (p.plateau_count || 0) < cfg.plateau_pulls)
  .map(([id]) => id);
for (let i = 0; i < ids.length; i += 50)
  out.push({ json: { mode: 'remeasure', ids: ids.slice(i, i + 50).join(',') } });

// 2. Cashtag clusters auto-derived from Theses/ frontmatter (US-listed only)
const tickers = [...new Set(($('Tickers').first().json.stdout || '').split('\n')
  .map(t => t.trim().toUpperCase()).filter(t => /^[A-Z]{1,5}$/.test(t)))];
const since = new Date(now - cfg.since_days * 86400000).toISOString().slice(0, 10);
const chunk = (a, n) => Array.from({ length: Math.ceil(a.length / n) }, (_, i) => a.slice(i * n, i * n + n));
const addQ = (q, floor) => out.push({ json: { mode: 'discover',
  url: 'https://api.twitterapi.io/twitter/tweet/advanced_search?queryType=Latest&query=' +
    encodeURIComponent(`${q} min_faves:${floor} -filter:retweets lang:en since:${since}`) } });
chunk(tickers.filter(t => MEGA.includes(t)), 8).forEach(c => addQ(c.map(t => '$' + t).join(' OR '), cfg.floor_mega));
chunk(tickers.filter(t => !MEGA.includes(t)), 8).forEach(c => addQ(c.map(t => '$' + t).join(' OR '), cfg.floor_std));

// 3. AI-curated terms from _watchers.md → ### Curated terms
const today = new Date().toISOString().slice(0, 10);
const sec = wmd.split('### Curated terms')[1]?.split(/\n#{2,3} /)[0] || '';
[...sec.matchAll(/^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([^|]*?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|/gm)]
  .map(r => ({ id: r[1].trim(), query: r[2].trim(), floor: +r[3], expires: r[5].trim(), status: r[6].trim().toLowerCase() }))
  .filter(w => w.id !== 'id' && w.status === 'active')
  .filter(w => w.expires === 'permanent' || w.expires >= today)
  .forEach(w => addQ(w.query, w.floor));

return out;
```

**Code X** (`Analyze`):

```javascript
// ---- FALLBACK DEFAULTS — live gates come from _watchers.md § X Watchers → ### Tuning ----
// Ratio params are PERCENTAGES (1.5 = 1.5%). Tune in the table, not here; this block only
// catches missing/malformed rows. Recalibrate per §9.8.
const DEF = { track_min_views: 3000, track_lv_pct: 1.5, track_rv_pct: 0.5, track_min_likes: 300,
  gem_lv_pct: 3, gem_rv_pct: 0.7, trend_min_delta: 150, trend_min_pct: 60, trend_min_base: 50,
  min_followers: 200, cap_tracked: 800, prune_age_days: 14, plateau_flat_likes: 10,
  plateau_pulls: 2, llm_top_n: 15, llm_model: 'claude-opus-4-8', archive_days: 90 };
const cfgOf = (md, def) => {
  const c = { ...def }, sec = (md.split('### Tuning')[1] || '').split(/\n#{2,3} /)[0];
  for (const m of sec.matchAll(/^\|\s*([A-Za-z_]+)\s*\|\s*([^|]+?)\s*\|/gm)) {
    const k = m[1].toLowerCase(), v = m[2].trim();
    if (k in def && v !== '') c[k] = typeof def[k] === 'string' ? v : (isFinite(+v) ? +v : def[k]);
  }
  return c;
};
const wmd = $('Extract Watchers').first().json.data || '';
const cfg = cfgOf(wmd, DEF);
const LV = cfg.track_lv_pct / 100, RV = cfg.track_rv_pct / 100,
  GLV = cfg.gem_lv_pct / 100, GRV = cfg.gem_rv_pct / 100, TPCT = cfg.trend_min_pct / 100;
// -----------------------------------------------------------------------------------------
let state = {};
try { state = JSON.parse($('Extract State').first().json.data); } catch (e) {}
state.posts = state.posts || {}; state.meta = state.meta || {}; state.ratio_log = state.ratio_log || [];
const nowIso = new Date().toISOString(), nowMs = Date.now();
const calib = (state.meta.calibration_until || '') >= nowIso.slice(0, 10);

// Normalize provider tweets — if verification shows different field names, fix ONLY here
const norm = t => ({ id: String(t.id), url: t.url || '', text: (t.text || '').slice(0, 1000),
  author: t.author?.userName || '?', followers: t.author?.followers || 0,
  likes: t.likeCount || 0, rts: t.retweetCount || 0, views: Number(t.viewCount) || 0 });
const tweets = [];
for (const item of $input.all()) {
  const j = item.json || {};
  for (const t of (j.tweets || (Array.isArray(j) ? j : []))) tweets.push(norm(t));
}
// Dedupe by id — a tracked post returned by BOTH batch-lookup and a search would otherwise be
// processed twice per run (second pass Δ=0 → false plateau++ → premature prune)
const seenIds = new Set();
const uniq = tweets.filter(t => t.id && !seenIds.has(t.id) && seenIds.add(t.id));

const themeOf = txt => (txt.match(/\$[A-Za-z]{1,5}\b/) || ['thematic'])[0].toUpperCase();
const surfaced = [];
let admitted = 0;
const flag = (p, f, why) => { if (!p.flags.includes(f)) { p.flags.push(f); surfaced.push({ p, f, why }); } };

for (const t of uniq) {
  const p = state.posts[t.id];
  if (p) {                                        // RE-MEASURE → delta vs previous pull
    const prev = p.obs[p.obs.length - 1];
    p.obs.push([nowIso, t.likes, t.rts, t.views]);
    const d = t.likes - prev[1];
    p.plateau_count = d < cfg.plateau_flat_likes ? (p.plateau_count || 0) + 1 : 0;
    if (d >= cfg.trend_min_delta || (prev[1] >= cfg.trend_min_base && d / prev[1] >= TPCT))
      flag(p, 'trending', `+${d} likes since last pull`);
    p.last_likes = t.likes;
  } else {                                        // DISCOVERY → entry gates
    const lv = t.views > 0 ? t.likes / t.views : 0, rv = t.views > 0 ? t.rts / t.views : 0;
    if (state.ratio_log.length < 2000) state.ratio_log.push([+lv.toFixed(4), +rv.toFixed(4)]);
    if (t.followers < cfg.min_followers || t.views < cfg.track_min_views) continue;
    if (!(lv >= LV || rv >= RV || t.likes >= cfg.track_min_likes || calib)) continue;
    if (Object.keys(state.posts).length >= cfg.cap_tracked) continue;
    const np = state.posts[t.id] = { url: t.url, author: t.author, followers: t.followers,
      theme: themeOf(t.text), text: t.text, first_seen: nowIso,
      obs: [[nowIso, t.likes, t.rts, t.views]], flags: [], plateau_count: 0, last_likes: t.likes };
    admitted++;
    if (!calib && (lv >= GLV || rv >= GRV)) flag(np, 'gem', `l/v ${(100 * lv).toFixed(1)}% @ ${t.views} views`);
  }
}

// Prune → archive (working set stays small; archive keeps archive_days of history, never re-measured)
state.archive = state.archive || [];
for (const [id, p] of Object.entries(state.posts))
  if ((nowMs - new Date(p.first_seen)) > cfg.prune_age_days * 86400000 || (p.plateau_count || 0) >= cfg.plateau_pulls) {
    state.archive.push({ id, archived: nowIso, ...p });
    delete state.posts[id];
  }
const cut = nowMs - cfg.archive_days * 86400000;
state.archive = state.archive.filter(r => new Date(r.archived) >= cut);

// Catalyst matching (±10d) from _catalyst.md
let catalystHits = [];
try {
  const cal = $('Extract Catalyst').first().json.data || '';
  const events = [...cal.matchAll(/\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*\[\[([^\]|]+)\]\]\s*\|([^|]*)\|/g)]
    .map(m => ({ date: m[1], ticker: m[2].split(' ')[0].toUpperCase(), what: m[3].trim() }))
    .filter(e => Math.abs(new Date(e.date) - nowMs) < 10 * 86400000);
  const active = new Set(Object.values(state.posts).map(p => p.theme.replace('$', '')));
  catalystHits = events.filter(e => active.has(e.ticker));
  // dashboard-only context — deliberately NOT flagged into the alert stream
} catch (e) {}

// Per-theme aggregates + LLM payload
const themes = {};
for (const p of Object.values(state.posts)) {
  const th = themes[p.theme] = themes[p.theme] || { posts: 0, likes: 0, top: [] };
  th.posts++; th.likes += p.obs[p.obs.length - 1][1]; th.top.push(p);
}
for (const th of Object.values(themes))
  th.top = th.top.sort((a, b) => b.obs[b.obs.length - 1][1] - a.obs[a.obs.length - 1][1]).slice(0, cfg.llm_top_n);
// Thesis stances for verification (from Execute Command 'Summaries')
const sumBlob = $('Summaries').first().json.stdout || '';
const sumMap = {};
for (const part of sumBlob.split(/\n(?=### )/)) {
  const m = part.match(/^### (\S+)\n([\s\S]*)/);
  if (m) sumMap[m[1].split('.')[0].toUpperCase()] = m[2].trim().slice(0, 12000);
}

const refUrls = {};
const llmInput = Object.entries(themes).map(([name, th]) => {
  const stance = sumMap[name.replace('$', '')];
  const hist = (state.sentiment_log || []).filter(r => r.name === name).slice(-30);
  const themeArch = state.archive.filter(r => r.theme === name);
  const anchors = themeArch.sort((a, b) => b.obs[b.obs.length - 1][1] - a.obs[a.obs.length - 1][1]).slice(0, 5);
  const rm = refUrls[name] = {};
  anchors.forEach((p, i) => { rm['A' + (i + 1)] = { u: p.url, a: p.author }; });
  th.top.forEach((p, i) => { rm['P' + (i + 1)] = { u: p.url, a: p.author }; });
  return `## ${name} (${th.posts} tracked live · ${themeArch.length} archived)\n` +
    `MY THESIS:\n${stance || '(no thesis sections found for this theme)'}\n` +
    (hist.length ? 'PRIOR READS (oldest first):\n' + hist.map(r =>
      `- ${r.d}: ${r.sentiment}(${r.score >= 0 ? '+' + r.score : r.score})${r.divergence ? ' · div: ' + r.divergence : ''} — ${r.summary}`).join('\n') + '\n' : '') +
    (anchors.length ? 'HISTORICAL ANCHOR POSTS (from the 90-day archive):\n' + anchors.map((p, i) =>
      `- [A${i + 1}] [${String(p.first_seen).slice(0, 10)}] @${p.author} (${p.obs[p.obs.length - 1][1]} likes): ${p.text.slice(0, 300)}`).join('\n') + '\n' : '') +
    `CURRENT CROWD POSTS (top ${th.top.length} live, with engagement):\n` +
    th.top.map((p, i) => { const o = p.obs[p.obs.length - 1];
      return `- [P${i + 1}] @${p.author} (${p.followers} fo · ${o[1]} likes · ${o[3]} views): ${p.text}`; }).join('\n');
}).join('\n\n');

// Analytical instructions — LIVE copy in _watchers.md § X Watchers → ### LLM prompt (first fenced block).
// Edit there; this constant is only the fallback. Output field names/types are pinned by SCHEMA below —
// edit the guidance, never the field list.
const DEF_PROMPT = 'For each theme below you get MY THESIS (six analytical sections), PRIOR READS (dated sentiment reads produced by this engine over the past 90 days), HISTORICAL ANCHOR POSTS (highest-engagement posts from the 90-day archive, dated, labeled [A1], [A2], …), and CURRENT CROWD POSTS with engagement stats (labeled [P1], [P2], …) — current posts are drawn from every post tracked live for that theme, not just newly pulled ones. Weight CURRENT posts most: they are the consumption signal; use PRIOR READS and ANCHOR POSTS as longitudinal context, not as current evidence. Return per theme: summary — 2-4 sentences synthesising the current crowd narrative: what the crowd believes, where the argument concentrates, what evidence they cite; weight higher-engagement, higher-follower posts more. sentiment (bullish/bearish/mixed/quiet). score (-2..2). shift — 1-2 sentences on how crowd sentiment and the dominant argument have moved versus the PRIOR READS: new arguments appearing, old ones dying, conviction hardening or fading; null if there is no meaningful history or no real change. perspectives — 2-6 distinct crowd arguments; each has text (1-2 sentences carrying the specific numbers, names, and claims from the posts, never generic labels) and refs (the labels of the 1-3 specific posts that argument draws from, e.g. ["P2","A1"] — use only labels that appear above). divergence — ONE synthesis judged across all the posts together, never per post: a specific, substantive crowd argument that contradicts, challenges, or is unaddressed by my thesis. If the crowd merely echoes a risk or bear point my thesis already carries, that is NOT divergence — return null. Judge on substance of claims, not tone; ignore hype and spam; return null unless the tension is genuine. Positioning gauge, not advice.';
const F3 = '`'.repeat(3);
const pmatch = wmd.match(new RegExp('### LLM prompt[\\s\\S]*?' + F3 + '[a-z]*\\n([\\s\\S]*?)' + F3));
const PROMPT = pmatch ? pmatch[1].trim() : DEF_PROMPT;

const SCHEMA = { type: 'object', additionalProperties: false, required: ['themes'], properties: {
  themes: { type: 'array', items: { type: 'object', additionalProperties: false,
    required: ['name', 'summary', 'sentiment', 'score', 'shift', 'perspectives', 'divergence'], properties: {
      name: { type: 'string' },
      summary: { type: 'string' },
      shift: { anyOf: [{ type: 'string' }, { type: 'null' }] },
      sentiment: { type: 'string', enum: ['bullish', 'bearish', 'mixed', 'quiet'] },
      score: { type: 'integer', enum: [-2, -1, 0, 1, 2] },
      perspectives: { type: 'array', items: { type: 'object', additionalProperties: false,
        required: ['text', 'refs'], properties: {
          text: { type: 'string' },
          refs: { type: 'array', items: { type: 'string' } } } } },
      divergence: { anyOf: [{ type: 'string' }, { type: 'null' }] } } } } } };

state.meta.last_run = nowIso; state.meta.runs = (state.meta.runs || 0) + 1; state.meta.last_cfg = cfg;

return [{ json: {
  state_json: JSON.stringify(state),
  ref_urls: refUrls,
  llm_body: { model: cfg.llm_model, max_tokens: 32000,
    thinking: { type: 'adaptive' },
    output_config: { format: { type: 'json_schema', schema: SCHEMA } },
    messages: [{ role: 'user', content: PROMPT + '\n\n' + llmInput }] },
  surfaced: surfaced.map(({ p, f, why }) => ({ f, why, author: p.author, followers: p.followers,
    theme: p.theme, text: p.text, url: p.url, likes: p.last_likes })),
  stats: { tracked: Object.keys(state.posts).length, seen: uniq.length, admitted, archived: state.archive.length, calib, catalystHits, cfg,
    themes: Object.fromEntries(Object.entries(themes).map(([k, v]) => [k, { posts: v.posts, likes: v.likes }])) }
} }];
```

**Code D** (`Assemble`):

```javascript
const a = $('Analyze').first().json;
let senti = null;
try {
  const txt = ($input.first().json.content || []).find(b => b.type === 'text')?.text || '';
  senti = JSON.parse(txt).themes;
} catch (e) {}
const d0 = new Date(); // local time — TZ is Australia/Sydney; toISOString would date morning runs as yesterday (UTC)
const today = `${d0.getFullYear()}-${String(d0.getMonth() + 1).padStart(2, '0')}-${String(d0.getDate()).padStart(2, '0')}`;
const hm = String(d0.getHours()).padStart(2, '0') + String(d0.getMinutes()).padStart(2, '0');
const bar = n => '▁▂▃▄▅▆▇'[Math.max(0, Math.min(6, Math.round(n)))];

const c = a.stats.cfg || {};
const ordered = Object.entries(a.stats.themes).sort((x, y) => y[1].likes - x[1].likes);
const sOf = name => (senti || []).find(v => v.name === name);
const divs = (senti || []).filter(v => v.divergence);

// Sentiment ledger — append today's reads into state; nodes 16→17 write state FROM THIS NODE
let st = null;
try { st = JSON.parse(a.state_json); } catch (e) {}
if (st && senti) {
  st.sentiment_log = st.sentiment_log || [];
  for (const s of senti) st.sentiment_log.push({ d: today, name: s.name, sentiment: s.sentiment,
    score: s.score, summary: s.summary || '', divergence: s.divergence || null });
  const cutL = Date.now() - (c.archive_days || 90) * 86400000;
  st.sentiment_log = st.sentiment_log.filter(r => new Date(r.d) >= cutL);
}
const SPARK = { '-2': '▁', '-1': '▂', '0': '▄', '1': '▆', '2': '█' };
const trend = n => ((st && st.sentiment_log) || []).filter(r => r.name === n).slice(-8)
  .map(r => SPARK[String(r.score)] || '·').join('');

let dash = `---\ndate: ${today}\ntags: [meta, x-dashboard]\n---\n# X Dashboard — ${today}\n\n> Snapshot by Workflow 5 (X Harvester) — one file per run, never rewritten; do not hand-edit. Positioning gauge, not research; anything substantive goes through /ingest.\n\n**Tracked:** ${a.stats.tracked} posts · **Seen this pull:** ${a.stats.seen} · **Admitted:** ${a.stats.admitted ?? 0} · **Archive:** ${a.stats.archived ?? 0}${a.stats.calib ? ' · **CALIBRATION MODE**' : ''}\n> Gates this pull: views≥${c.track_min_views} · fo≥${c.min_followers} · l/v≥${c.track_lv_pct}% · rt/v≥${c.track_rv_pct}% · likes≥${c.track_min_likes} — gem ${c.gem_lv_pct}%/${c.gem_rv_pct}% — trend Δ≥${c.trend_min_delta} or +${c.trend_min_pct}% — cap ${c.cap_tracked} · llm ${c.llm_model} · edit in _watchers.md § Tuning\n\n## Themes\n\n| Theme | Posts | Σ likes | Sentiment | Score | Trend |\n|---|---|---|---|---|---|\n`;
for (const [name, t] of ordered) {
  const s = sOf(name) || {};
  dash += `| ${name} | ${t.posts} | ${t.likes} ${bar(Math.log10(t.likes + 1) * 1.6)} | ${s.sentiment || '—'} | ${s.score ?? '—'} | ${trend(name) || '—'} |\n`;
}
if (!senti) dash += `\n**LLM unavailable this pull** — sentiment, perspectives, and divergence not refreshed.\n`;

dash += `\n## ⚠ Thesis divergence\n\n` + (divs.length
  ? divs.map(d => `**${d.name}** — ${d.divergence}`).join('\n\n')
  : '- none this pull') + '\n';

if (senti) {
  dash += `\n## Crowd perspectives\n\n`;
  const rlink = (name, refs) => (refs || []).map(r => {
    const m = (a.ref_urls && a.ref_urls[name] || {})[r];
    return m ? `[@${m.a}](${m.u})` : null;
  }).filter(Boolean).join(' · ');
  for (const [name] of ordered) {
    const s = sOf(name);
    if (!s || !(s.perspectives || []).length) continue;
    dash += `**${name}** — ${s.sentiment} · score ${s.score}\n${s.summary ? s.summary + '\n' : ''}${s.shift ? '↝ Shift: ' + s.shift + '\n' : ''}` +
      s.perspectives.map(p => { const t = p.text || p, l = rlink(name, p.refs);
        return `- ${t}${l ? ' — ' + l : ''}`; }).join('\n') + '\n\n';
  }
}

dash += `\n## Catalyst chatter (±10d vs _catalyst.md)\n\n` + (a.stats.catalystHits.length
  ? a.stats.catalystHits.map(e => `- **${e.ticker}** ${e.date} — ${e.what}: active post cluster`).join('\n')
  : '- none') + '\n';
if (a.surfaced.length) {
  dash += `\n## Flagged this pull\n\n`;
  for (const s of a.surfaced.slice(0, 20))
    dash += `- **[${s.f}]** ${s.theme} @${s.author} (${s.followers} fo, ${s.likes} likes) — ${s.why}\n  ${s.text}\n  ${s.url}\n`;
}

const out = { dash_body: dash, state_json: st ? JSON.stringify(st) : a.state_json,
  dash_fname: `${today} ${hm} - X Dashboard.md` };
if (a.surfaced.length || divs.length) {
  const top = a.surfaced.slice(0, 12);
  out.text = (`𝕏 ${a.surfaced.length} flagged (${a.stats.tracked} tracked)` +
    (top.length ? '\n' + top.slice(0, 5).map(s => `[${s.f}] ${s.theme} @${s.author}: ${s.text.slice(0, 300)}${s.text.length > 300 ? '…' : ''}\n${s.url}`).join('\n\n') : '') +
    (divs.length ? '\n\n⚠ Thesis divergence:\n' + divs.map(d => `${d.name} — ${d.divergence}`).join('\n').slice(0, 1200) : '')).slice(0, 3900);
  if (top.length) {
    out.fname = `${today} - X trending digest - n8n.md`;
    out.body = `---\nsource: x-harvester (twitterapi.io)\nretrieved: ${today}\norigin: n8n/x-harvester\n---\n# X trending — ${today}\n\n` +
      top.map(s => `## [${s.f}] ${s.theme} — @${s.author}\n${s.text}\n- ${s.why} · ${s.likes} likes\n- ${s.url}\n`).join('\n');
  }
}
return [{ json: out }];
```

### 9.7 First run & what to expect

1. Open `Workflow 5 — X Harvester` → **Test workflow**. Runtime 1–4 min (HTTP batching + Opus thinking time).
2. Green ticks appear node by node. First-run expectations:

| Node | Expect on run #1 |
|---|---|
| `Plan` | ~13–18 items, all `mode: discover` — state is empty, so zero re-measure batches |
| `Batch Lookup` | 0 items — nothing tracked yet, normal |
| `Search` | 1 item per query, each holding a `tweets` array |
| `Analyze` | 1 item: long `state_json` string + `llm_body` + `stats`; `surfaced` likely empty (calibration suppresses gem alerts) |
| `Sentiment` | 1 item with a `content` array — 60–180s, Opus is thinking |
| `Assemble` | `dash_body` present; `text`/`fname` usually absent on run #1 |
| `IF` → Telegram / digest | usually skipped — trending needs two pulls to diff |

3. Verify on disk: a dated file appears in `Daily Intel/` — header shows **CALIBRATION MODE**, the Seen → Admitted funnel, and the gates stamp; the Themes table has sentiment + perspectives + divergence, flags empty. `.data/x_engagement_state.json` shows `"runs":1` and a populated `posts` map.
4. **Publish.** Calibration mode admits loosely for two weeks; **the system becomes meaningful at pull #2 and sharp from pull #3.**

**Troubleshooting** (the failures that actually happen):

| Symptom | Cause → fix |
|---|---|
| Execute Command missing from the node panel | n8n 2.x excludes it by default (v2 breaking change) → save open work, then `export NODES_EXCLUDE='["n8n-nodes-base.localFileTrigger"]'` → `pm2 restart n8n --update-env` → `pm2 save` → hard-refresh the editor. Keeps the unused Local File Trigger excluded |
| Everything after a node is skipped, yet the run shows "success" | Its On Error is `Continue (using error output)` — failures exit via an unconnected error connector; zero items silently ends the branch → set **Continue (using regular output)** everywhere this guide says Continue, re-run, then read the failing node's output panel for the real API error |
| Divergence feels generic — thesis never referenced | Verify the payload, not the wiring: open the execution → `Sentiment` → input → search `MY THESIS` — it must be followed by full section text, not just a heading. (2026-07-18 bug class: a multiline-`$` regex truncated every thesis to its first line) |
| `Access to the file is not allowed. Allowed paths: …` | File fence env var not live → verify `N8N_RESTRICT_FILE_ACCESS_TO=/Users/alexcohen/InvestmentVault` in the pm2 env, then `pm2 restart n8n --update-env` |
| `Referenced node doesn't exist` | A node name ≠ its `$('…')` reference → rename to the exact §9.5 card name |
| Code node error involving `$json` on line 1 | Wrong mode → set `Run Once for All Items` |
| Every `Search` item has `tweets: []` | Provider degraded (did the Canary fire?) or query mangled → open one `url` from `Plan`'s output in a browser to eyeball it |
| 401/403 on twitterapi.io nodes | Header name ≠ provider spec, or key typo → fix the `TwitterAPI-io` credential |
| Anthropic 405 Method Not Allowed | `Sentiment`'s Method left at default `GET` → set **POST** (card 14, first field) |
| Anthropic 401 | Credential header must be exactly `x-api-key` → re-check, re-paste key |
| Anthropic 400 | Model string must be exactly `claude-opus-4-8`; body must come via `JSON.stringify($json.llm_body)` |
| `Sentiment` times out | Long thinking + large output → confirm Timeout is `600000`; if persistent, lower `llm_top_n` or pause noisy themes |
| Dashboard says "LLM unavailable" but the API call succeeded | `stop_reason: max_tokens` — truncated JSON fails to parse. Check the execution's Sentiment output for `stop_reason`; raise `max_tokens` in Code X (thinking counts against it) |
| Node 23: "expects the node's input data to contain a binary file 'data'" | The digest branch ran on a divergence-only pull (Telegram text, no `body`) — the `If digest` gate (card 20b) is missing or mis-wired → wire 20-true → 20b (`{{ $json.fname }}` is not empty) → 22 → 23. A hard fail here also aborts the state/dashboard writes, losing the pull |
| No Telegram, ever | Nothing flagged yet — normal until pull #2–3; the dashboard is the pulse meanwhile |

### 9.8 Calibration & tuning runbook

- **Weeks 1–2:** calibration mode on (`calibration_until` in the state file). `ratio_log` accumulates your universe's real conversion distribution.
- **At calibration end:** ask Claude to compute p50/p75 of `ratio_log` → set `track_lv_pct`/`track_rv_pct` ≈ p50 and `gem_lv_pct`/`gem_rv_pct` ≈ p75 **in the Tuning table** → clear `calibration_until`. No code edit, no redeploy.
- **Tunables map — single source `_watchers.md § X Watchers`:** every engine gate (pull floors, MEGA list, entry lanes, gem, trending, plateau/prune, cap, LLM top-N) → `### Tuning` rows · curated terms → `### Curated terms` · cadence → Schedule node (raise `since_days` with it). Code headers hold fallback defaults only — they fire on a missing/non-numeric row, never override the table.
- **Threshold experiments:** change one gate at a time; write the why in the row's `notes`; judge on the next 2–3 pulls via the dashboard funnel (Seen → Admitted → flagged) — the header stamps the active gates each pull, so every render is attributable to its config. Git history of `_watchers.md` is the experiment log.
- **Monthly review add-ons:** prune expired term rows; check per-pull read volume (target 500–1,000 — adjust floors); skim dashboard themes for junk attribution (a noisy cashtag → raise `floor_mega`/`floor_std`).

---

## 10. Failure modes & resilience

| Mode | Caught by | Response |
|---|---|---|
| X internal churn breaks provider (hours–days, every few weeks) | Watchdog (hard errors) / **Canary** (empty results) | Wait for provider patch |
| Silent thin results | Canary | Check provider status; fallback twin socialdata.tools (2 URLs + credential + `norm()` fields ≈ 30 min swap) |
| Anthropic API failure | On-Error-Continue on node 14 | Dashboard renders "LLM unavailable"; harvest unaffected |
| State file corrupted/deleted | try/catch fallback to `{}` | Cold restart; sharp again in 2 pulls — disposable by design |
| `_catalyst.md` stale | Workflow 2 staleness nag (existing) | Catalyst matching degrades gracefully to "none" |
| Provider dies commercially | Canary + top-up failure | Balance ≤$5 caps the loss |
| Legal | — | Public-data scraping risk sits with the provider (X v. Bright Data dismissed 2024); your X account is never involved |

## 11. Decision log

- **2026-07-17** — Initial design: official X API ruled out (Feb-2026 pay-per-use ≈ $125/mo at our volume + no server-side engagement operators → third-party-or-nothing). Velocity engine designed (state-file snapshot-diff — no API sells engagement time-series). Ratio-as-entry-gate / velocity-as-alarm two-factor structure.
- **2026-07-18** — Renamed to Twitter API Build; converted to full implementation guide per expanded requirements: all-thesis cashtag sourcing (auto-derived) + AI-curated terms table; 3-day cadence (cost ↓3×, ≤3-day latency accepted); dashboard added (`_x_dashboard.md`, Obsidian-native — Grafana/SQLite rejected); LLM sentiment layer; catalyst matching vs `_catalyst.md`. **Still parked** at §9.1 — trial signup is the gate.
- **2026-07-18 (later)** — Storage cap 400→800 after working-set-vs-archive review; archive-on-prune documented as v2. LLM upgraded per user decision: `claude-haiku-4-5` → **`claude-opus-4-8`** + adaptive thinking, and the layer became **thesis verification** — thesis context fed alongside crowd posts, new `divergence` field, dashboard column + Telegram `⚠` alerts (divergence alone triggers notification). Boundary restated: **read-vault yes, write-vault no**. Dashboard capability question answered with the vault's own precedent ([[Watchlist.md]] DataviewJS) + Mermaid xychart upgrade path.
- **2026-07-18 (final refinements)** — Divergence semantics pinned: **one synthesis per theme over the whole tracked DB** (new + re-measured posts, top 10 as evidence), never per-tweet. Thesis context widened from Summary-only to the **six analytical sections** (Summary, Key Non-consensus Insights, Bull, Bear, Risks, OQ) — chosen over full-document ingestion (possible, ~$20–40/mo, mostly wasted tokens) because Bear/Risks context is what makes divergence *genuine* (crowd echoing a known risk ≠ divergence). Alert stream narrowed to exactly three push classes: **trending delta, standalone high-ratio (gem), genuine divergence**; catalyst matching demoted to dashboard-only context. LLM cost ~$4–8/mo, system total ~$5–10/mo.
- **2026-07-18 (thresholds → vault data)** — Every trending-engine gate moved from Code-node constants to a `### Tuning` table in `_watchers.md § X Watchers` (19 params: pull floors + MEGA list, `since_days`, entry lanes, gem, trending, plateau/prune, cap, `llm_top_n`), re-parsed each run — edit in Obsidian, next pull complies, no redeploy. Code keeps identical values as fallback defaults only (missing/non-numeric row → seed behavior, never a dead engine). To support tuning over time (user requirement): dashboard header now prints the pull funnel (Seen → Admitted) plus an active-gates stamp, `state.meta.last_cfg` records what each run used, and `_watchers.md` git history doubles as the experiment log. Ratios expressed as percentages in the table (1.5 = 1.5%).
- **2026-07-18 (build guide expanded)** — §9 rewritten to click-level "for dummies" detail: pre-flight checklist + canvas-basics table (§9.0), stepwise account/credential setup (§9.1), verification calls as a build-and-check procedure with field-name recording (§9.2), one-paste state seeding with auto-dated calibration (§9.3), Canary as 8 numbered steps (§9.4), the harvester as 23 build cards + wiring map + load-bearing-names warning (§9.5), Code-node paste rules (§9.6), first-run expectation table + troubleshooting matrix (§9.7). One functional tweak: node 22 gains **On Error: Continue** so divergence-only pulls (Telegram text, no digest file) can't block the alert path. Design unchanged; still parked at §9.1.
- **2026-07-18 (renumbered + un-parked)** — Vault-wide workflow numbering adopted per user: **Workflow 1 Price Tripwires, 2 Catalyst Reminders, 3 News Sweep, 4 X Canary, 5 X Harvester** (formerly UC2b / UC1 / UC4 / UC8b / UC8a). UC5 (newsletters), UC6 (alt-data), UC7 (headless skills) sections deleted from the n8n doc per user decision — recoverable from git history; the Alt-Data registry rows remain in [[_watchers.md]] as unlabeled backlog. Status PARKED → **IN BUILD**: §9.1 credentials created, §9.2 verification skipped by user decision (checks fold into first runs), §9.3 state + registry seeded by Claude. Digest `origin:` stamp changed `n8n/uc8a` → `n8n/x-harvester`.
- **2026-07-18 (llm_model → registry)** — Sentiment/divergence model moved to an `llm_model` row in `### Tuning` (20 params now): switch models by cell edit, reason in `notes`, git-logged. Code X falls back to `claude-opus-4-8`; the dashboard gates stamp now prints the active model, so every render is attributable to the model that produced it. A typo'd model string fails harmlessly (node 14 On-Error-Continue → "LLM unavailable this pull"; harvest unaffected).
- **2026-07-19 (Telegram depth)** — Alert posts were capped at 60 chars (pointer design); raised to 300 chars/post + 1,200 divergence with a 3,900 global cap — Telegram rejects >4,096-char messages outright rather than truncating, so the budget is a delivery guarantee, not stinginess. Full text still lives in the digest + dashboard.
- **2026-07-19 (batch-size 400)** — First scheduled daily run fired on time but died output-side: provider rejects >50 `tweet_ids` per batch call (`400 max 50 tweet_ids per request`); the design assumed 100 and every prior run had ≤50 tracked posts, so it only surfaced when the working set reached 108. Code P chunks 100→50. This is the exact failure §9.2 verification check #4 was written to catch pre-build — skipped by user decision, invoiced one day later. Reminder recorded: schedule triggers are calendar timers; manual runs never delay them.
- **2026-07-18 (inline citations)** — Perspectives upgraded from strings to `{text, refs}` objects: every post in the prompt carries a short label (`[P1]` live, `[A1]` anchor), the schema forces each argument to cite the labels it draws from, and Code D resolves labels → author-linked URLs per bullet (replacing the generic Sources line). Design rule: never ask the LLM to emit URLs — label-copying is near-perfect and schema-enforced; unknown labels resolve to nothing rather than broken links. Folder renamed `X Dashboards` → `Daily Intel`.
- **2026-07-18 (digests + source links)** — Digests relocated `_Inbox` → `Daily Intel/` (News Sweep daily digest + X trending digest): they are scanning surfaces, not ingest candidates — keeps the ingest queue pure and co-locates every daily read in one folder. Post links surfaced: each theme's perspectives block ends with a `→ Sources:` line (top-5 tracked posts, author-linked with like counts), and Telegram alert lines now carry the post URL. Flagged-this-pull entries and digests already carried URLs.
- **2026-07-18 (snapshot-only dashboards)** — User simplification accepted: no separate live `_x_dashboard.md`; node 19 writes the dated snapshot directly (planned node 24 dropped before being built). Newest file in `Daily Intel/` = current dashboard; the root file was retired into the folder as the first snapshot. Registry-prompt precedence verified against the live n8n DB: the running `Analyze` node carries the parse and the `_watchers.md` fence extracts cleanly (1,615 chars) — Code X's prompt is fallback only.
- **2026-07-18 (daily + history + dedupe)** — Cadence 3-day → **daily** (user; ~$17–40/mo all-in, `llm_model` row is the cost lever; `since_days` 4→2). **Dated dashboard history**: node 24 (`Snapshot`, off node 19) writes `Daily Intel/YYYY-MM-DD HHmm - X Dashboard.md` every run — `_x_dashboard.md` stays the live surface, the folder is the record (answers "each run overwrites my past outputs"). **Dedupe bug fixed**: a tracked post returned by both batch-lookup AND a search was processed twice per run — second pass Δ=0 → false plateau++ → premature prune (a contributor to the shrinking working set during test-hammering; would worsen at daily cadence). Code D dates switched to local time (UTC dating stamps morning-AEST runs as yesterday). Doc-move splice at the top of this file repaired. Ticker-coverage audit: 71 US-listed auto-covered by cashtags; 9 curated rows added for foreign listings (Kioxia, Ajinomoto, Murata, Elite Material, Jusung, WinWay, Nitto Boseki, Reliance, BTC).
- **2026-07-18 (max_tokens truncation)** — First run with full thesis context: input 59k tokens (~6× pre-fix — proof the theses flow), but `stop_reason: max_tokens` at 16k output (adaptive thinking counts against the cap) truncated the JSON mid-string → parse fail → "LLM unavailable" despite a successful, visibly deeper response. `max_tokens` 16k→32k, node 14 timeout 300s→600s. Diagnostic habit codified in troubleshooting: check `stop_reason` before blaming the pipeline.
- **2026-07-18 (thesis-context bug — caught by user challenge)** — User asked for proof that Opus compares theses against tweets; payload inspection of execution 25 showed `MY THESIS:` carried only the literal heading `## Summary` for every theme. Root cause: `sumMap` regex `([\s\S]*?)(?=\n### |$)` with the `m` flag — `$` matches every line end, truncating each thesis to its first line. Every divergence produced before this fix was crowd-only inference, not thesis-verified. Fixed with split-based parsing; verification method added to troubleshooting (read the actual Sentiment payload, not the wiring).
- **2026-07-18 (longitudinal memory)** — Per user: the LLM must analyse the 90-day corpus, not just live posts. Implemented as three evidence tiers per theme — CURRENT posts (dominant, recency-biased by instruction), PRIOR READS (`state.sentiment_log`: the engine's own dated reads, written by Code D and fed back by Code X — compressed analytical memory), HISTORICAL ANCHORS (top-5 archived posts, dated). New schema field `shift` (sentiment/argument movement vs prior reads) + dashboard **Trend** sparkline column from score history. Raw-90-day-dump rejected (~$50+/mo of stale tokens; the ledger carries the time series at ~2k tokens/theme). State write rewired 13→16 to **15→16** so the ledger persists — safe because 14 is On-Error-Continue. LLM ~$8–20/mo, total ~$9–22/mo.
- **2026-07-18 (prompt → registry, 90-day archive)** — Confirmed for the user: the LLM always judges the merged working set (re-measured tracked posts + new admissions), never just the pull. Analytical prompt externalised to a `### LLM prompt` fenced block in `_watchers.md § X Watchers` (re-read every pull; schema pins the field list, guidance freely editable). Archive-on-prune promoted from v2-option to built-in: pruned posts move to `state.archive` with full engagement history, retained `archive_days` (Tuning row, default 90, ~2–3 MB) — zero API cost, LLM unaffected (recency stays the signal), dashboard header shows archive depth. 21 Tuning params.
- **2026-07-18 (depth upgrade)** — First-pull output judged too light; root cause was input starvation, not the model: `norm()` truncated posts to 200 chars, no engagement context reached the LLM, and most themes carried 1–2 posts on day one. Fixes: post text 200→1,000 chars; follower/like/view stats inlined per post; new required `summary` field (2–4 sentence engagement-weighted crowd narrative, rendered above the perspective bullets); perspectives 1–3 one-liners → 2–6 arguments with the posts' specific numbers; `llm_top_n` 10→15; `max_tokens` 8k→16k; node 14 timeout 300s. LLM cost ~$5–15/mo, total ~$6–17/mo. Remaining depth arrives free as the working set matures at 3-day cadence.
- **2026-07-18 (build live-fire fixes)** — Found during the real build: n8n 2.x hides Execute Command by default (fixed via `NODES_EXCLUDE` override, persisted in pm2); `Sentiment` Method must be POST (405 otherwise); the swallowed-error design on the digest branch was wrong — a divergence-only pull (first live divergence fired this day) passed a binary-less item to node 23, whose hard fail **aborted the state and dashboard writes**. Replaced with an explicit `If digest` gate (card 20b, `fname` not empty): Telegram gates on `text`, file writes gate on `fname`, no swallowed errors anywhere. Also documented: back-to-back test runs falsely plateau-prune the working set (minutes-apart deltas < `plateau_flat_likes`) — set `plateau_flat_likes` to 0 in Tuning while testing, restore after.
- **2026-07-20 (Workflow 3b spec'd — bookmarks audit → Outlet Feeds registry + body pipeline)** — 381-bookmark export audited: ~220 content domains probed (homepage link-tag discovery + CMS-convention paths + last-post freshness), ~150 live feeds verified, dormant/dead flagged (Protocol, AnandTech, Eugene Wei, cdixon, 25iq et al.), 94 rows kept per user cluster selection → new `## Outlet Feeds` section in [[_watchers.md]] (rows inert until build; user prunes manually). Channel verification: ZeroHedge `cms.zerohedge.com/fullrss2.xml` live; majors' off-domain feeds captured (feeds.bloomberg.com, feeds.content.dowjones.io, rss.nytimes.com, ft.com/rss/home, economist.com per-section); FMP news works on the existing key (ticker-scoped + general-latest; **keyword search conclusively absent** — probe stubs return `[]` even for "Nvidia"); GDELT viable but limiter is 1 req/5s with sticky IP cooldown → build with Wait-node spacing; Brave selected as thematic gap-fill (free key, signup pending). Body pipeline decided by user: **Lane A** (body-informed re-scoring) + **Lane C** (verbatim defuddle auto-clip → `_Inbox/` at ≥`clip_min`, `max_clips_day` cap) approved; **Lane B rejected** — no n8n-authored prose anywhere. Rule 1 amended (sanctioned verbatim clips); Rule 2 unchanged. New `### Tuning (body pipeline)` registry table (triage_min · clip_min · max_clips_day · body_exempt · gdelt_spacing_s · brave_budget_mo). defuddle CLI v0.7.0 confirmed installed (vault's standard extractor). Google News decode hack deliberately not built.
- **2026-07-20 (3b absorbs 3 — user challenge)** — User asked what the point of keeping Workflow 3 is once 3b exists. Correct — none, long-term: both read the same News & Thematic rows through different engines with separate dedupe stores → permanent double-surfacing; and 3b's FMP ticker channel strictly supersedes W3's weekly per-ticker GN sweep. GN absorbed as 3b's fifth channel (headline backstop, `body: false`). W3 kept live only through 3b calibration (proven baseline while 3b shakes out), then **deactivated, not deleted** — §12.5 cutover checklist. Brave key created by user; bookmarks export archived to `_Inbox/processed/`. §12 click-level build guide written.
- **2026-07-20 (retro-documentation — Workflows 1–3 + Error Watchdog)** — Reconciliation pass (user request): §9 covers Workflows 4–5 and §12 covers 3b at click level, but Workflows 1–3 + the watchdog had only summary-card build notes — unbuildable from the doc alone, which breaks the §5.1 lighter-alternative migration path and disaster rebuild. New §13: click-level build cards reconstructed from the §3 specs + this decision log (NOT from a live-instance export — running instance is authoritative on any other divergence). Two divergences flagged: (a) known — W3's Write node still targets `_Inbox/`; §13.4 documents the decided `Daily Intel/` path; (b) **new finding** — W2's parser regex silently skips multi-ticker catalyst rows (aliased `[[path\|TICKER]]` cells break the `]]\s*\|` match; the 2026-07-18 GENIUS Act row proved the miss). Fix code in §13.3; apply to the deployed Code node at next n8n touch.
- **2026-07-20 (W3 unification — merge 3+3b, per-ticker everywhere, brief-not-clips, Lane B reversed)** — User directives: (1) merge 3 and 3b into one workflow named `Workflow 3 — News Sweep`, (2) replicate per-ticker search across 3b's full engine set, (3) output a daily intel summary instead of `_Inbox/` auto-clips. Implemented in doc: GN/GDELT/Brave each now query **every thesis ticker (company name from filename — numeric Asia listings unsearchable as strings) AND every News & Thematic row**, both daily runs; FMP + outlet feeds unchanged. **Lane C reverted** (same-day): no n8n `_Inbox/` deposits — clip params dropped from Plan/Tuning; §2.3 contract retained as spec only. **Lane B reversed in contained form** (user choice via explicit trade-off prompt): new SumPrep→Summarise stage (cards 18a/18b), `claude-sonnet-4-6` (user: Sonnet, not Haiku) writes 1–2 factual sentences per admitted item — digest-only, hard rule 2 exception #2; new `digest_model` Tuning row is the cost lever. **Brave → paid metered tier** (user choice; ~6k queries/mo vs 2k free cap; `brave_budget_mo` guard 2000→7000). Run time ~15–25 min (GDELT pacing ~100 targets). Cost ~$40–75/mo (Sonnet summaries + Brave are the new lines). §12 retitled + amended (⬥-marked deltas); §3 cards merged; §13.4 relabeled legacy v1; hallucination spot-check added to §12.4 first-run protocol.

---

## 12. Workflow 3 — News Sweep (unified) — step-by-step build

> Originally authored as the Workflow 3b (Feed Harvester) guide; amended 2026-07-20 per the unification decision (§3 merge-history): per-ticker queries added to the GN/GDELT/Brave channels, Lane C clip output removed, Sonnet digest-summary stage added (cards 18a/18b), Brave moved to paid tier. Deltas from the 3b spec are marked ⬥ on the affected cards.

### 12.0 Pre-build verification (~10 min — do NOT skip: §9.2's skipped checks invoiced one day later, 2026-07-19)

Terminal, one at a time; record anything that deviates:

1. **defuddle flag check**: `defuddle parse 'https://www.zerohedge.com/markets' --markdown 2>&1 | head -20` — expect clean markdown. If `--markdown` is unrecognized, run `defuddle --help` and substitute the real flag in card 15. (CLI v0.7.0 confirmed installed 2026-07-20.)
2. **Brave key**: `curl -s -H 'X-Subscription-Token: <KEY>' -H 'Accept: application/json' 'https://api.search.brave.com/res/v1/news/search?q=TSMC%20capex&count=3&freshness=pd' | head -c 600` — expect JSON `results[]`. Note the field names (card 11 parses `title/url/description/age/meta_url.hostname` defensively).
3. **GDELT** (the 2026-07-20 probe cooldown should have lapsed): `curl -s 'https://api.gdeltproject.org/api/v2/doc/doc?query=TSMC%20capex&mode=artlist&format=json&maxrecords=3&timespan=24h'` — expect `{articles:[...]}`. If the rate-limit text appears instead: wait 10 min, retry once, never burst.
4. **FMP batch size**: 25-symbol `stable/news/stock?symbols=...` call — if it errors, set `FMP_CHUNK = 10` in card 7's code.
5. n8n up, pm2 `online`, Execute Command available (§1.3 `NODES_EXCLUDE` override in place — same requirement as Workflow 5).

### 12.1 Credentials

- **Brave Search** — new Header Auth: name `X-Subscription-Token`, value = key (§2.1 row). ⬥ **Upgrade to the paid metered tier before first run** (user decision 2026-07-20): full ticker+theme coverage ≈ 6,000 queries/mo vs the 2,000 free cap — verify per-1,000 pricing on the dashboard at upgrade.
- FMP (Query Auth) and Anthropic (Header Auth) — already exist.

### 12.2 Build cards

New workflow `Workflow 3 — News Sweep (unified)` → Settings → Error Workflow: `Error Watchdog`.

**1 · Schedule Trigger** — two rules: 07:10 and 17:10. (§12.5 cutover moves these to 07:00/17:00.)

**2 · Execute Command "Tickers"** — ⬥ Command:
`ls /Users/alexcohen/InvestmentVault/Theses | sed 's/\.md$//'`
On Error: Continue. Emits one `TICKER - Company Name` line per thesis: the ticker prefix drives the FMP channel (US-listed filter applied in Plan); the company name drives the per-ticker GN/GDELT/Brave queries — names beat raw tickers in news search, and numeric Asia listings ("000660", "2802") are unsearchable as strings while "SK Hynix" and "Ajinomoto" are not.

**3 · Read/Write Files from Disk "ReadReg"** — Read, `/Users/alexcohen/InvestmentVault/_watchers.md`. Wire 1→2→3.

**4 · Extract from File "RegText"** — Operation: Text.

**5 · Code "Plan"** (Run Once for All Items) — ⬥ parses both registry sections + Tuning, emits one task item per source call. Delta from the 3b spec: per-ticker search targets (company names) added to GN/GDELT/Brave; Brave runs both daily sweeps (paid tier — no morning gate); clip params dropped; `digest_model` param added:

```javascript
const DEF = { triage_min:7, gdelt_spacing_s:8, brave_budget_mo:7000, digest_model:'claude-sonnet-4-6',
  body_exempt:['digitimes','ft-home','bbg-tech','bbg-econ','bbg-markets','wsj-markets','wsj-tech','wsj-business','econ-finance','econ-business','nyt-business','nyt-tech','theinformation','techmeme','mediagazer'] };
const md = $('RegText').first().json.data || '';
const now = new Date();
const today = `${now.getFullYear()}-${String(now.getMonth()+1).padStart(2,'0')}-${String(now.getDate()).padStart(2,'0')}`;
const section = h => (md.split('## '+h)[1] || '').split(/\n## /)[0];

// Tuning params (fallback = DEF)
const tun = section('Outlet Feeds');
const cfg = {...DEF};
for (const k of ['triage_min','gdelt_spacing_s','brave_budget_mo']) {
  const m = tun.match(new RegExp('\\|\\s*'+k+'\\s*\\|\\s*([^|]+?)\\s*\\|'));
  if (m && !isNaN(parseFloat(m[1]))) cfg[k] = parseFloat(m[1]);
}
const dm = tun.match(/\|\s*digest_model\s*\|\s*([^|]+?)\s*\|/);
if (dm) cfg.digest_model = dm[1].trim();
const ex = tun.match(/\|\s*body_exempt\s*\|\s*([^|]+?)\s*\|/);
if (ex) cfg.body_exempt = ex[1].split(',').map(s=>s.trim()).filter(Boolean);

const tasks = [];
// Channel 1 — outlet feeds (7-col rows; url col anchors the match, so Tuning rows never match)
for (const r of tun.matchAll(/^\|\s*([^|]+?)\s*\|\s*(https?:\/\/[^|\s]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$/gm)) {
  const [,id,url,cluster,vol,triage,expires,status] = r.map(x=>String(x).trim());
  if (id==='id' || /^-+$/.test(id) || status!=='active') continue;
  if (expires!=='permanent' && expires < today) continue;
  tasks.push({ ch:'feed', id, url, cluster, bypass: triage==='no', body: !cfg.body_exempt.includes(id) });
}
// Search targets — every thematic row PLUS one per-ticker query per thesis (quoted company name)
const targets = [];
for (const r of section('News & Thematic').matchAll(/^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$/gm)) {
  const [,idRaw,q,thesis,expires,status] = r.map(x=>String(x).trim());
  const id = idRaw.replace(/\s*⚠\s*$/,'');
  if (id==='id' || /^-+$/.test(id) || status!=='active') continue;
  if (expires!=='permanent' && expires < today) continue;
  targets.push({ id, q, cluster:'thematic' });
}
const files = ($('Tickers').first()?.json?.stdout || '').split('\n').map(s=>s.trim()).filter(Boolean);
const tickers = [];
for (const f of files) {
  const i = f.indexOf(' - '); if (i < 0) continue;
  const tk = f.slice(0,i).trim(), name = f.slice(i+3).trim();
  tickers.push(tk);
  targets.push({ id:'tk-'+tk.toLowerCase(), q:`"${name}"`, cluster:'ticker' });
}
// Channels 2–4 — GN + GDELT + Brave for EVERY target (themes AND tickers, both daily runs)
for (const t of targets) {
  tasks.push({ ch:'gn', id:t.id, cluster:t.cluster, bypass:false, body:false,
    url:`https://news.google.com/rss/search?q=${encodeURIComponent(t.q)}&hl=en-US&gl=US&ceid=US:en` });
  let g = t.q.replace(/\bAND\b/g,' ').replace(/"([^"]{1,4})"/g,'$1').replace(/\s+/g,' ').trim();
  if (/\bOR\b/.test(g) && !g.startsWith('(')) g = '('+g+')';
  tasks.push({ ch:'gdelt', id:t.id, cluster:t.cluster, bypass:false, body:true, q:g });
  tasks.push({ ch:'brave', id:t.id, cluster:t.cluster, bypass:false, body:true, q:t.q.replace(/\bAND\b/g,' ') });
}
// Channel 5 — FMP ticker news (US-listed ticker prefixes only; chunk 25 — 12.0 check 4)
const FMP_CHUNK = 25;
const us = tickers.filter(s=>/^[A-Z]{1,5}$/.test(s));
for (let i=0;i<us.length;i+=FMP_CHUNK)
  tasks.push({ ch:'fmp', id:'fmp-'+(1+i/FMP_CHUNK), cluster:'ticker', bypass:false, body:true, symbols:us.slice(i,i+FMP_CHUNK).join(',') });

if (!tasks.length) throw new Error('Plan: 0 tasks — registry parse failed');
cfg.tickers = tickers.join(',');
cfg.themes = targets.filter(t=>t.cluster==='thematic').map(t=>`${t.id}: ${t.q}`).join(' · ');
return tasks.map(t => ({ json: {...t, cfg} }));
```

**6 · Switch "Route"** — Rules on `{{ $json.ch }}` (String, equals): `feed`→0, `gn`→1, `gdelt`→2, `brave`→3, `fmp`→4.

**7 · RSS Read "Feeds"** — from Route outputs 0 AND 1 (two connections into one node). URL → Expression → `{{ $json.url }}`. On Error: **Continue (using error output)**. Main output → card 11; error output → card 11 too (Normalize detects error items and logs the feed id as a warning — feed-rot surfacing).

**8 · GDELT loop** (from Route 2): **Loop Over Items "GdeltLoop"** (batch 1) → **HTTP "Gdelt"** (GET, URL → Expression → `https://api.gdeltproject.org/api/v2/doc/doc?query={{ encodeURIComponent($json.q) }}&mode=artlist&format=json&maxrecords=50&timespan=24h`, On Error: Continue) → **Code "GParse"**:
```javascript
const t = $('GdeltLoop').first().json;
const arts = ($json.articles) || [];
return arts.map(a => ({ json: { ch:'gdelt', feedId:t.id, cluster:t.cluster, bypass:false, fetchBody:true,
  title:a.title, url:a.url, snippet:'', published:a.seendate||'', source:a.domain||'' } }));
```
→ **Wait "Pace"** (Seconds → Expression → `{{ $('Plan').first().json.cfg.gdelt_spacing_s }}`) → back into GdeltLoop. GdeltLoop **done** output → card 11.

**9 · Brave loop** (from Route 3): same shape — **Loop "BraveLoop"** (batch 1) → **HTTP "Brave"** (GET `https://api.search.brave.com/res/v1/news/search?q={{ encodeURIComponent($json.q) }}&count=20&freshness=pd`, Credential: Brave Header Auth, extra header `Accept: application/json`, On Error: Continue) → **Code "BParse"**:
```javascript
const t = $('BraveLoop').first().json;
const arts = ($json.results) || [];
return arts.map(a => ({ json: { ch:'brave', feedId:t.id, cluster:t.cluster, bypass:false, fetchBody:true,
  title:a.title, url:a.url, snippet:a.description||'', published:a.age||'', source:(a.meta_url&&a.meta_url.hostname)||'' } }));
```
→ **Wait** 2 s → loop. Done → card 11.

**10 · HTTP "FMP"** (from Route 4) — GET `https://financialmodelingprep.com/stable/news/stock?symbols={{ $json.symbols }}&limit=50`, Credential: FMP Query Auth, On Error: Continue → card 11.

**11 · Code "Normalize"** (Run Once for All Items) — unify, canonicalize, in-run title dedupe, collect warnings:

```javascript
const plan = $('Plan').all();
const out = [], warn = [], seen = new Set();
const canon = u => { try { const x=new URL(u); x.hash='';
  ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','fbclid','gclid'].forEach(p=>x.searchParams.delete(p));
  return x.toString(); } catch(e){ return null; } };
const tkey = t => (t||'').toLowerCase().replace(/[^a-z0-9 ]/g,'').split(/\s+/).filter(w=>w.length>3).sort().slice(0,8).join(' ');

for (const it of $input.all()) {
  const j = it.json;
  // pre-tagged items from GParse/BParse arrive article-shaped with ch set
  if (j.ch && j.url && j.title) { add(j.title, j.url, j.snippet, j.published, j.source, j); continue; }
  let s; try { s = plan[it.pairedItem?.item ?? 0].json; } catch(e) { s = plan[0].json; }
  if (j.error) { warn.push(`${s.ch}:${s.id} failed`); continue; }
  if (s.ch==='feed' || s.ch==='gn')
    add(j.title, j.link, j.contentSnippet || '', j.isoDate || j.pubDate || '', j.creator || s.id, {ch:s.ch, feedId:s.id, cluster:s.cluster, bypass:s.bypass, fetchBody:s.body && s.ch==='feed'});
  else if (s.ch==='fmp') { const arr = Array.isArray(j) ? j : [j];
    for (const a of arr) if (a && a.url) add(a.title, a.url, a.text || '', a.publishedDate || '', a.site || '', {ch:'fmp', feedId:s.id, cluster:'ticker', bypass:false, fetchBody:true, sym:a.symbol}); }
}
function add(title, url, snippet, published, source, meta) {
  const cu = canon(url); if (!cu || !/^https?:\/\//.test(cu)) return;
  const tk = tkey(title); if (tk && seen.has(tk)) return; if (tk) seen.add(tk);
  out.push({ json: { title:(title||'').slice(0,300), curl:cu, snippet:(snippet||'').slice(0,500),
    published, source, ch:meta.ch, feedId:meta.feedId, cluster:meta.cluster,
    bypass:!!meta.bypass, fetchBody:!!meta.fetchBody } });
}
out.push({ json: { _warnings: warn, curl: 'internal:warnings:' + Math.random() } });
return out;
```

**12 · Remove Duplicates "Dedupe"** — Operation: *Remove Items Processed in Previous Executions* · Value to Dedupe On → Expression → `{{ $json.curl }}`.

**13 · Code "TriagePrep"** (Run Once for All Items) — bypass rows skip scoring; the rest chunk into 120-item batches:

```javascript
const cfg = $('Plan').first().json.cfg;
const all = $input.all().map(i=>i.json);
const out = all.filter(j=>j._warnings || j.bypass).map(j=>({json: j._warnings ? j : {...j, s:null, admitted:true}}));
const score = all.filter(j=>!j._warnings && !j.bypass);
for (let i=0;i<score.length;i+=120) {
  const chunk = score.slice(i,i+120);
  out.push({ json: { _batch: chunk,
    _payload: JSON.stringify(chunk.map((j,k)=>({i:k, t:j.title, src:j.source||j.feedId, sn:(j.snippet||'').slice(0,180)}))) } });
}
return out;
```

**14 · IF "IsBatch"** — `{{ $json._batch !== undefined }}` is true → card 14a; false → card 18 (Merge input 2).

**14a · HTTP "Triage"** — POST `https://api.anthropic.com/v1/messages` · Credential: Anthropic Header Auth · header `anthropic-version: 2023-06-01` · On Error: Continue · Body (JSON, Expression):
model `claude-haiku-4-5`, `max_tokens` 8000, temperature 0, single user message:
`You score news items for one investor. Coverage tickers: {{ $('Plan').first().json.cfg.tickers }}. Live research questions: {{ $('Plan').first().json.cfg.themes }}. Clusters also covered: semis, datacenter, china-tech, macro, logistics, media, essays, general tech. Score each item 0-10 on NEW information value to this coverage: 9-10 directly material new fact (guidance, capacity, pricing, regulatory, primary technical disclosure); 7-8 clearly relevant development; 4-6 adjacent context; 0-3 noise — listicles, price-target roundups, "stocks to buy", rehash, sponsored. Judge information content, not sentiment. Items: {{ $json._payload }} — Return ONLY a JSON array [{"i":0,"s":7},...] covering every item.`

**15 · Code "Admit"** (Run Once for All Items, from Triage) — parse scores, flatten batches, gate at `triage_min`, mark body eligibility:

```javascript
const cfg = $('Plan').first().json.cfg;
const out = [];
for (const it of $input.all()) {
  const j = it.json;
  const batch = $('TriagePrep').all()[it.pairedItem?.item ?? 0]?.json?._batch || [];
  let scores = {};
  try { const txt = (j.content||[]).filter(b=>b.type==='text').map(b=>b.text).join('');
    for (const r of JSON.parse(txt.match(/\[[\s\S]*\]/)[0])) scores[r.i] = r.s; } catch(e) {}
  batch.forEach((b,k) => { const s = scores[k] ?? 0;
    if (s >= cfg.triage_min) out.push({ json: {...b, s, admitted:true} }); });
}
return out;
```

**16 · IF "Body?"** (from Admit) — `{{ $json.fetchBody === true }}` → true: card 17; false: card 18 (Merge input 1... see wiring map — both IF-false streams and the body stream converge on Merge).

**17 · Body chain**: **Loop "BodyLoop"** (batch 1) → **Execute Command "Defuddle"** — Command → Expression:
`defuddle parse '{{ $json.curl.replace(/'/g, "") }}' --markdown`
On Error: Continue → **Code "Body1"**: `const t=$('BodyLoop').first().json; const txt=($json.stdout||'').trim(); return [{json:{...t, bodyOk: txt.length>400, bodyText: txt.slice(0,60000)}}];` → back into BodyLoop. Done output → **Code "RescorePrep"** (chunk 10, excerpt 4,000 chars, same payload pattern as card 13) → **HTTP "Rescore"** (same Anthropic call; prompt adds: *"Re-score with the article body excerpt: confirm the headline delivers substance — new numbers, primary quotes, disclosed specifics. Downgrade rehash/opinion; upgrade if the body reveals material specifics the headline undersold."*) → **Code "Final"** (same parse as Admit; sets `s2`; items with failed fetch keep headline score and `bodyOk:false`).

**18 · Merge "Rejoin"** — Mode: Append, 3 inputs: bypass/warn stream (14-false), no-body admitted stream (16-false), body stream (17 Final).

**18a · Code "SumPrep"** (Run Once for All Items, from Rejoin) — ⬥ NEW: chunks every admitted item for the summary call (12/batch, 3,000-char body excerpt — headline+snippet where no body); carries source-failure warnings through:

```javascript
const all = $input.all().map(i=>i.json);
const warn = (all.find(j=>j._warnings)||{})._warnings || [];
const items = all.filter(j=>!j._warnings && (j.admitted || j.bypass));
const out = [];
for (let i=0;i<items.length;i+=12) {
  out.push({ json: { _batch: items.slice(i,i+12), _warnings: i===0 ? warn : [],
    _payload: JSON.stringify(items.slice(i,i+12).map((j,k)=>({i:k, t:j.title, src:j.source||j.feedId,
      x:(j.bodyOk ? j.bodyText : (j.snippet||'')).slice(0,3000)}))) } });
}
return out.length ? out : [{ json: { _batch: [], _warnings: warn, _payload: '[]' } }];
```

**18b · HTTP "Summarise"** (from SumPrep) — ⬥ NEW: POST `https://api.anthropic.com/v1/messages` · Credential: Anthropic Header Auth · header `anthropic-version: 2023-06-01` · On Error: Continue (an LLM failure degrades to headline-only digest lines, never kills the run) · Body (JSON, Expression): model → `{{ $('Plan').first().json.cfg.digest_model }}` (default `claude-sonnet-4-6` — user decision 2026-07-20: the summary IS the product; registry `digest_model` row is the cost lever), `max_tokens` 4000, temperature 0, single user message:
`You write a factual news brief for one investor. Coverage tickers: {{ $('Plan').first().json.cfg.tickers }}. Live research questions: {{ $('Plan').first().json.cfg.themes }}. For each item write "sum": 1-2 sentences stating the concrete NEW facts in the text — numbers, names, guidance, dates, disclosed specifics. No opinion, no recommendation, no thesis inference, no adjectives of significance. If the text is thin or navigation junk, restate the headline claim only. Items: {{ $json._payload }} — Return ONLY a JSON array [{"i":0,"sum":"..."},...] covering every item.`

**19 · Code "Assemble"** (Run Once for All Items, from Summarise) — ⬥ rewritten: parse summaries, build the daily intel brief + Telegram; no clip lane:

```javascript
const items = [], warn = [];
$input.all().forEach((it, idx) => {
  const j = it.json;
  const src = $('SumPrep').all()[it.pairedItem?.item ?? idx]?.json || {};
  warn.push(...(src._warnings||[]));
  let sums = {};
  try { const txt=(j.content||[]).filter(b=>b.type==='text').map(b=>b.text).join('');
    for (const r of JSON.parse(txt.match(/\[[\s\S]*\]/)[0])) sums[r.i]=r.sum; } catch(e) {}
  (src._batch||[]).forEach((b,k)=> items.push({...b, sum: sums[k] || null}));
});
const fin = j => (j.s2 !== undefined && j.s2 !== null) ? j.s2 : j.s;
const now = new Date(); const p = n => String(n).padStart(2,'0');
const d = `${now.getFullYear()}-${p(now.getMonth()+1)}-${p(now.getDate())}`;
const hm = `${p(now.getHours())}${p(now.getMinutes())}`;
const by = {};
for (const j of items) (by[j.cluster] = by[j.cluster] || []).push(j);
let md = `---\ndate: ${d}\ntags: [meta, daily-intel]\norigin: n8n/news-sweep\n---\n\n# Daily intel — ${d} ${hm}\n\n`;
md += `${items.length} items admitted this run.`;
if (warn.length) md += `\n⚠ Source failures: ${warn.join(', ')}`;
md += '\n\n';
for (const cl of Object.keys(by).sort()) {
  md += `## ${cl}\n\n`;
  for (const j of by[cl].sort((a,b)=>(fin(b)??0)-(fin(a)??0))) {
    md += `- [${(j.s!==null?fin(j):'—')}] **${j.title}** — ${j.source||j.feedId} — ${j.curl}\n`;
    if (j.sum) md += `  ${j.sum}${j.bodyOk ? '' : ' *(headline only)*'}\n`;
  }
  md += '\n';
}
const out = [{ json: { type:'digest', fname:`${d} ${hm} - Daily intel - n8n.md`, content: md } }];
const top = [...items].sort((a,b)=>(fin(b)??0)-(fin(a)??0)).slice(0,5);
let tg = `W3: ${items.length} items in today's intel brief (Daily Intel/)`;
for (const t of top) tg += `\n[${fin(t)}] ${t.title.slice(0,90)}\n${t.curl}`;
if (warn.length) tg += `\n⚠ ${warn.length} source failures`;
out.push({ json: { type:'tg', text: tg.slice(0,3900) } });
return out;
```

**20 · Switch "Out"** on `{{ $json.type }}`: ⬥ two lanes only — `digest` → **Convert to File** (Text, source `content`) → **Read/Write "WriteDigest"** (Write, path → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $json.fname }}`) · `tg` → **Telegram "Notify"** (chat `1779654963`, text `{{ $json.text }}`). No clip lane, no `_Inbox/` writes (Lane C reverted 2026-07-20).

### 12.3 Wiring map

`1→2→3→4→5→6` · 6:{0,1}→7 · 6:2→8(loop: Gdelt→GParse→Wait→loop) · 6:3→9(loop: Brave→BParse→Wait→loop) · 6:4→10 · {7 main, 7 error, 8 done, 9 done, 10}→11→12→13→14 · 14-true→14a→15→16 · 16-true→17(BodyLoop: Defuddle→Body1→loop; done→RescorePrep→Rescore→Final) · {14-false, 16-false, 17-Final}→18→18a→18b→19→20→{ConvertDigest→WriteDigest · Notify}

### 12.4 First run

Manual **Execute Workflow** (a manual run never delays the schedule — §11 2026-07-19 lesson). Expected: run completes in **~15–25 min** (GDELT Wait-pacing across ~100 targets dominates; body loop second) · one brief in `Daily Intel/` with per-item Sonnet summaries grouped by cluster · Telegram top-5. Then check: (a) admitted count sane (tens, not hundreds — if hundreds, raise `triage_min`), (b) **spot-check 3 summaries against their articles** — every stated fact must appear in the source text (hallucination check; `*(headline only)*` items get least trust), (c) summaries are factual, not editorial — if Sonnet is opining, tighten the 18b prompt, (d) `⚠ Source failures` list — dead feeds to prune from the registry, (e) ticker-cluster items resolve to the right companies (a wrong-company match means the thesis filename's company name is ambiguous — add a distinguishing word to the filename or a thematic row). Publish (Active toggle) only after one clean manual run. First scheduled runs re-surface some items legacy W3 already showed — fresh dedupe store, self-heals in a day.

### 12.5 Cutover checklist (after ~5–7 clean scheduled runs)

1. n8n → Workflows → **deactivate legacy Workflow 3 v1** (toggle off — do not delete; it is the instant-fallback baseline, and §13.4 preserves its build).
2. If v1's optional Monday per-ticker trigger was built, it retires with it (the unified ticker channels supersede it on four engines, daily).
3. Rename this workflow to `Workflow 3 — News Sweep` and move its schedule 07:10/17:10 → 07:00/17:00 (v1's vacated slots).
4. Update §6 table (3 → Live unified) + decision-log entry.
5. `_watchers.md` needs no change — same rows, new consumer.

### 12.6 Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Plan throws `0 tasks` | Registry section headers renamed or table malformed | Headers must contain `## Outlet Feeds` / `## News & Thematic`; check a row's pipe count |
| GDELT items = 0, response is prose | Rate-limit text (HTTP 200!) | Raise `gdelt_spacing_s`; never retry in-run |
| Brave 401 / 429 | Bad key / paid tier not active / burst | Re-check credential + confirm metered plan on the Brave dashboard; Wait ≥2 s |
| Body text is nav junk / cookie banner | defuddle failed on that site's DOM | Accept (score drops at rescore) or add feed id to `body_exempt` |
| Summaries editorialize or infer thesis impact | Sonnet drifting past the factual-brief prompt | Tighten 18b prompt (the "no adjectives of significance" line is the lever); spot-check against source |
| Summary states a fact not in the article | Hallucination on a thin excerpt | Raise SumPrep excerpt length; treat `*(headline only)*` items as unverified by definition — never quote a brief summary into research without opening the link |
| Run takes >30 min | GDELT pacing × ~100 targets | Lower `gdelt_spacing_s` toward 6 (never <5 — sticky IP cooldown); otherwise accept, it's a background sweep |
| `Paired item data unavailable` in Normalize | n8n lost pairing through RSS Read | Falls back to `plan[0]` (mislabeled feedId only — cosmetic); if frequent, insert a Set node stamping `feedId` before RSS Read |
| Telegram send fails | >4,096 chars | Already capped at 3,900 (card 19) — check for multi-byte overflow, trim top list to 3 |
| Same story twice in digest | Different URLs, title-dedupe missed (reworded headlines) | Accept v1; tighten `tkey` word count if chronic |

---

## 13. Workflows 1–3 + Error Watchdog — click-level build (retro-documented 2026-07-20)

Workflows 1–3 and the watchdog went live before this doc adopted §9's click-level standard — their §3 cards summarise the design but cannot rebuild it. This section closes the gap for the §5.1 migration lighter-alternative (rebuild from doc + JSON export) and disaster recovery. **Reconstructed from the §3 specs + §11 decision log, not from a live-instance export** — where a rebuilt node differs from the running instance, the running instance is authoritative, EXCEPT the two flagged divergences, where this section documents the *decided* behavior:

- ⚠ **W3 digest path** — deployed Write node still targets `_Inbox/` (known since 2026-07-19); §13.4 card 10 uses the decided `Daily Intel/` path.
- ⚠ **W2 multi-ticker parser gap** — found in this reconciliation; §13.3 card 4 carries the fix.

§9.0's canvas-basics table and §9.6's paste rules apply to every card below. Every Code node: **Mode** `Run Once for All Items`. Every workflow: `⋯` → **Settings** → **Error Workflow** → `Error Watchdog` before publishing.

### 13.1 Error Watchdog (build first — every other workflow references it)

1. **Create Workflow** → rename `Error Watchdog`.
2. **Node 1 — Error Trigger** (search "Error Trigger"; no schedule — it fires when any referencing workflow fails).
3. **Node 2 — Telegram** (connect from 1) — existing credential · **Chat ID** `1779654963` · **Text** → Expression → `⚠️ n8n workflow {{ $json.workflow.name }} failed: {{ $json.execution.error.message }}`.
4. Registration is per-consumer and easy to forget: a workflow without the Error Workflow setting fails silently — audit the setting whenever a workflow is created or imported.
5. Test: temporarily point any workflow's Read node at a nonexistent path → run → ⚠️ arrives → revert.

### 13.2 Workflow 1 — Price Tripwires (daily 07:35 · 7 nodes · ~30 min)

Node name `Rows` is load-bearing (`$('Rows')` in card 6).

**1 · Schedule Trigger** — **Trigger Interval** `Days` · **Days Between Triggers** `1` · **Trigger at Hour** `7am` · **Trigger at Minute** `35` (staggered behind Workflow 2's 07:30).

**2 · Read/Write Files from Disk** — **Operation** `Read File(s) From Disk` · **File(s) Selector** `/Users/alexcohen/InvestmentVault/_watchers.md`.

**3 · Extract from File** — **Operation** `Text`.

**4 · Code — rename `Rows`** — parses the 6-column Price Tripwires table (bare wikilinks only in cells, per the §2.35 constraint):

```javascript
const md = $json.data;
const section = md.split('## Price Tripwires')[1]?.split('\n## ')[0] || '';
const rows = [...section.matchAll(/^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|/gm)]
  .map(r => ({ id: r[1].trim(), ticker: r[2].trim(), direction: r[3].trim(),
               level: +r[4], thesis: r[5].trim(), status: r[6].trim() }))
  .filter(w => w.id !== 'id' && !/^-+$/.test(w.id) && w.status === 'active' && isFinite(w.level));
if (!rows.length) return [];
return [{ json: { rows, symbols: [...new Set(rows.map(w => w.ticker))].join(',') } }];
```

**5 · HTTP Request — rename `Quotes`** — **Method** `GET` · **URL** → Expression → `https://financialmodelingprep.com/stable/batch-quote-short?symbols={{ $json.symbols }}` · **Authentication** → Generic Credential Type → **Query Auth** → FMP credential (param name `apikey`, key from `.data/config.json`). One call for the whole table; `stable/` only — v3 endpoints are legacy-dead on this key (verified 2026-07-17).

**6 · Code — rename `Compare`**:

```javascript
const rows = $('Rows').first().json.rows;
const quotes = {};
for (const q of $input.all().map(i => i.json)) quotes[q.symbol] = q.price;
const out = [];
for (const w of rows) {
  const p = quotes[w.ticker];
  if (p === undefined) { out.push(`⚠️ ${w.id}: no quote for ${w.ticker} — check symbol/plan`); continue; }
  if (w.direction === 'below' && p <= w.level) out.push(`🔻 ${w.ticker} ${p} ≤ ${w.level} (${w.id}) — read the trigger block: ${w.thesis}`);
  if (w.direction === 'above' && p >= w.level) out.push(`🔺 ${w.ticker} ${p} ≥ ${w.level} (${w.id}) — read the trigger block: ${w.thesis}`);
}
return out.length ? [{ json: { text: out.join('\n') } }] : [];
```

**7 · Telegram** — **Chat ID** `1779654963` · **Text** → Expression → `{{ $json.text }}`. Empty Compare output = silent day.

**Test:** with the current registry (MRVL below-110 / above-210) expect silence; temporarily move a level through spot to force a breach line, verify Telegram, revert. **Discipline:** a tripwire firing = read the thesis Conviction Triggers block, never an execution signal; update levels whenever `/status` or `/sync` changes a trigger.

### 13.3 Workflow 2 — Catalyst Reminders (daily 07:30 · 5 nodes · ~30 min)

**1 · Schedule Trigger** — `Days` · `1` · Hour `7am` · Minute `30`.

**2 · Read/Write Files from Disk** — Read · `/Users/alexcohen/InvestmentVault/_catalyst.md`.

**3 · Extract from File** — `Text`.

**4 · Code** — ⚠ the §3 code is what's deployed; the block below is the **fixed parser** (apply at next n8n touch). Deployed-regex failure mode: `\[\[([^\]]+)\]\]\s*\|` requires the ticker cell to be exactly one wikilink — `/catalyst` writes aliased multi-ticker cells (`[[Theses/…\|CRCL]], [[Theses/…\|BTC]]`), which never match, so multi-thesis events are silently skipped (2026-07-18 GENIUS Act row: proven miss). Fix: collapse wikilinks to their alias BEFORE cell-splitting — the alias `\|` inside `[[path\|TICKER]]` is exactly what breaks naive pipe-splitting:

```javascript
const md = $input.first().json.data;
const now = new Date();
const out = [];

const fm = md.match(/^date:\s*(\d{4}-\d{2}-\d{2})/m);
const age = fm ? Math.floor((now - new Date(fm[1])) / 86400000) : 999;
if (age > 30) out.push(`⚠️ _catalyst.md is ${age}d old — run /catalyst`);

for (const line of md.split('\n')) {
  if (!/^\|\s*\d{4}-\d{2}-\d{2}\s*\|/.test(line)) continue;
  const cells = line.replace(/\[\[(?:[^\]|]*\|)?([^\]|]+)\]\]/g, '$1').split('|').map(s => s.trim());
  const diff = Math.round((new Date(cells[1]) - now) / 86400000);
  if (diff === 0) out.push(`📅 TODAY: ${cells[2]} — ${cells[3]}`);
  if (diff === 2) out.push(`⏳ T-2: ${cells[2]} — ${cells[3]} (${cells[1]})`);
}
return out.length ? [{ json: { text: out.join('\n') } }] : [];
```

**5 · Telegram** — Chat ID `1779654963` · Text → Expression → `{{ $json.text }}`. Empty output = no message.

**Coupling reminder (§5):** this parser is bound to `/catalyst`'s table format — re-test the same day any `/catalyst` spec change lands.

### 13.4 Workflow 3 v1 — legacy GN-only News Sweep (07:00 + 17:00 · superseded 2026-07-20 by the unified §12 build)

Legacy record. The unified Workflow 3 (§12) replaces this build entirely; rebuild v1 only as calibration-baseline insurance while the unified build shakes out — §12.5 deactivates it. Node name `Digest` is load-bearing if you split the tail differently; as wired below no by-name lookups are needed.

**1 · Schedule Trigger** — **two rules** (the node rejects multi-time cron like `0 7,17 * * *`): Rule 1 `Days`·`1`·`7am`·`0`; **Add Rule** → Rule 2 `Days`·`1`·`5pm`·`0`.

**2 · Read/Write Files from Disk** — Read · `/Users/alexcohen/InvestmentVault/_watchers.md`. **3 · Extract from File** — `Text`.

**4 · Code — rename `Queries`** — the §2.35 parser verbatim (emits one Google News search-as-RSS URL per active, unexpired `## News & Thematic` row; `paused` and past-`expires` rows drop out automatically — the whole lifecycle lives in the registry, never in this node).

**5 · RSS Read** — **URL** → Expression → `{{ $json.url }}` (runs once per query) · **Settings → On Error** `Continue` — one rate-limited query must not kill the sweep.

**6 · Remove Duplicates** — **Operation** `Remove Items Processed in Previous Executions` · **Value to Dedupe On** → Expression → `{{ $json.link }}`. Cross-execution memory is what makes the 07:00/17:00 runs non-overlapping and missed Mac-asleep days self-healing.

**7 · (optional triage) Basic LLM Chain — rename `Triage`** — Anthropic credential · model `claude-haiku-4-5` · prompt: *"Score 0–10 relevance to: custom silicon (MRVL/AVGO), HBM/memory, semicap, photonics/CPO, scale-up fabrics (UALink/NVLink/ESUN), CXL/memory disaggregation, AI datacenter power. Title: {{ $json.title }} — {{ $json.contentSnippet }}. Return ONLY JSON {"score": n, "tickers": [], "reason": ""}."* Scoring only — no summarisation (hard rule 2). Skip cards 7–8 to run unscored at $0.

**8 · Code — rename `Score`** — parse + gate at 7; a broken triage degrades to unscored, never to a silent feed:

```javascript
return $input.all().map(i => {
  let s = null, t = [];
  try { const j = JSON.parse((i.json.text || '').replace(/```json?|```/g, '')); s = j.score; t = j.tickers || []; } catch (e) {}
  return { json: { ...i.json, score: s, tickers: t } };
}).filter(i => i.json.score === null || i.json.score >= 7);
```

**9 · Code — rename `Digest`** — one file per run; feed description stays verbatim (never LLM text):

```javascript
const d = $now.toFormat('yyyy-MM-dd'), hm = $now.toFormat('HHmm');
const items = $input.all().map(i => i.json);
if (!items.length) return [];
let md = `---\nsource: n8n aggregate\nretrieved: ${d}\norigin: n8n/news-sweep\n---\n\n# News digest — ${d} ${hm}\n\n`;
for (const j of items.sort((a, b) => (b.score ?? 0) - (a.score ?? 0)))
  md += `- [${j.score ?? '—'}] ${j.title} — ${j.link}\n  ${(j.contentSnippet || j.content || '').slice(0, 300)}\n`;
return [{ json: { fname: `${d} ${hm} - News digest - n8n.md`, content: md,
  text: `📰 News sweep: ${items.length} items → Daily Intel/` } }];
```

**10 · Convert to File** — `Convert to Text File` · **Text Input Field** `content` → **11 · Read/Write Files from Disk** — Write · **File Path and Name** → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $json.fname }}` · **Input Binary Field** `data`. ⚠ This is the *decided* path (2026-07-18 relocation); the deployed instance still writes `_Inbox/` — fix that one field rather than rebuilding.

**12 · Telegram** (second wire off `Digest`) — Chat ID `1779654963` · `{{ $json.text }}`.

**Wiring:** `1→2→3→4→5→6[→7→8]→9` · `9 → 10→11` and `9 → 12`.

**Optional Monday 08:00 per-ticker sweep** (§2.6 universe → one `"<Company>" stock` query per ticker → same downstream chain, weekly digest): superseded by the unified W3's daily four-engine ticker channels — do **not** build new; documented only because the deployed instance may carry it.

**Intent guard:** the digest is a scanning surface — you pick the 1–3 links worth a manual `/ingest`. Auto-ingesting news bodies wholesale is deliberately not built (and Lane C auto-clips were reverted at the 2026-07-20 unification).
