---
date: 2026-07-20
tags: [meta, infrastructure, automation, how-to]
status: active
---

# n8n Automations — Build & Operations

So the basic architecture is this:

Read my vaults .md files for the LLM prompts and the tickers and themes I’m looking to search as well as parameters on filtering and analysis sensitivity and styles

Runs parallel news searches across Google RSS, Brave database, an open source news aggregation database and news from financial markets subscription platform and also specific websites I’ve selected.

LLM filters out duplicates from past searches from my json database by scoring it for new information surfaced.

LLM grades the articles for quality of content and filters out clickbait and AI slop. 

LLM groups articles that report the same story into a single cluster of information and also tags follow up coverage of prior outputted stories

Final LLM produces the summary and analysis of each story that was surfaced.

Outputs are a news summary report based on the selected topics and tickers as well as a telegram message with top x stories and an entry into my past news covered database

> Provenance, merge history, and change log: **§11** (bottom of this doc).

n8n (self-hosted, free) is the vault's **sensory layer**: always-on acquisition, scheduling, and alerting upstream of `/ingest` — the vault is otherwise pull-based, with nothing watching thesis observables between sessions.

**Division of labor (non-negotiable):**

| Layer | Does | Never does |
|---|---|---|
| n8n | Deterministic acquisition, cron scheduling, threshold alerts, relevance triage | Judgement — it has no mental-models context, no thesis state |
| Vault skills | All analysis, propagation, conviction | Watching the world between sessions |

**Four hard rules** (extend CLAUDE.md change-safety into the automation layer):

1. **n8n writes only NEW files, only into designated output locations** — `Daily Intel/` (dashboard snapshots + daily digests: scanning surfaces, not ingest candidates), `.data/` (machine state), `_Inbox/` (true ingest candidates only). Never Theses/, Research/, metadata files, `_Inbox/processed/`, or any existing file. Anything meant for the research pipeline still flows through `/ingest` exactly like a manual web clip — you paste the links worth ingesting. **No n8n `_Inbox/` deposits of any kind**: the unified Workflow 3 outputs a daily intel brief into `Daily Intel/` only; ingest candidates are hand-picked from the brief (curation stays at paste-time). The §2.3 contract remains the spec for any future re-sanctioned deposit. (Amendment trail: §11.)
2. **Analysis lives in the brief; the vault spine stays human-curated.** n8n LLM stages may read full article bodies and write analytical prose — scores, summaries, implications for the coverage — into their `Daily Intel/` outputs (W3 brief + Telegram top story; W5 dashboard, which also reads thesis sections for its divergence compare, §7.1). The boundary is rule 1's **write surface**, not the content: nothing n8n produces enters Theses/, Research/, sector/macro notes, or propagation, and `/ingest` (which alone carries mental-models context) remains the only path into the vault spine. Briefs are dated, disposable context — `/clean daily-intel` prunes them; nothing downstream treats them as source material. Analytical quality bar: every claim grounded in the provided text, inference labeled — the layer may opine, never invent. *(Original "triage yes, analysis no" rule removed by user decision 2026-07-21 — trail §11.)*
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

`NODES_EXCLUDE`: n8n 2.x excludes **Execute Command** and Local File Trigger by default — a v2 breaking change. Workflow 5 needs Execute Command (ticker + thesis-section extraction), so the override re-enables it while keeping the unused Local File Trigger excluded. Localhost-only listener + the file fence are unaffected.

### 1.4 The Mac-sleep caveat (read this)

Schedules fire only while the Mac is awake. A missed cron does not back-fill. Options, in order of preference:

1. Schedule everything inside reliably-awake hours (06:00–22:00 works for every workflow — nothing here needs 3 a.m.).
2. `sudo pmset repeat wakeorpoweron MTWRFSU 06:25:00` to guarantee the morning block — **and** `sudo pmset -c sleep 0` (never idle-sleep on AC) as prophylaxis for an always-on automation host: the wake event gets the Mac up but does not keep it up, so a machine that idle-sleeps between workflows would fire later schedules into sleep (missed crons don't back-fill). Display sleep can stay on — screen off doesn't stop n8n.
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
| twitterapi.io | Header Auth (`X-API-Key`) | twitterapi.io dashboard — §6.1 | Workflows 4–5 |
| Anthropic | Header Auth (`x-api-key`) | console.anthropic.com — separate billing from the Claude Code subscription | Workflow 5 sentiment layer (Opus); Workflow 3 (unified) — triage + clustering (Sonnet), body re-score + story summaries (Opus); all per the §2.4 registry table |
| Brave Search | Header Auth (`X-Subscription-Token`) | brave.com/search/api — **paid metered tier** (free 2,000/mo vs ~3,000/mo needed for full ticker+theme daily coverage — verify per-1,000 pricing at upgrade) | Workflow 3 (unified) thematic + per-ticker search channel |
| Voyage | Header Auth (`Authorization`, value `Bearer <key>`) | voyageai.com/dashboard → API Keys — **200M free tokens/account**, then $0.02/M (`voyage-4-lite`); effectively free at this volume for ~2+ yrs | Workflow 3 (unified) — embeddings semantic-dedup layer (card 15d), replaces the old Opus cluster call |

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
- **No live workflow deposits into `_Inbox/`** (Lane C reverted — §11): this contract is retained as the spec for any future re-sanctioned deposit.

### 2.4 The watcher registry — one file controls everything pulled

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

**Anti-accumulation:** auto-expiry retires windowed watches; the `thesis` column forces each watch to justify itself against a live question (orphans surface when a thesis closes); the §8 monthly review prunes the rest.

**Model AND prompt selection — every LLM knob is an Obsidian cell.** No model string or prompt text in the automation layer requires touching n8n: each stage reads its model from a [[_watchers.md]] Tuning row and its prompt from a `####` block under `## Outlet Feeds → ### Prompts` on every run, and the Code nodes hold identical fallback defaults (a deleted/typo'd row or a prompt block missing its required token degrades to the default — or, for a bad model string, a harmless 400 the workflow continues past — never a dead run). The full surface:

| Registry key | Lives in | Default | Drives |
|---|---|---|---|
| `triage_model` | `## Outlet Feeds → ### Tuning` | `claude-sonnet-5` | W3 headline triage (§5.3 card 14a) |
| `cluster_model` | `## Outlet Feeds → ### Tuning` | `claude-opus-4-8` | ⚠ DEPRECATED 2026-07-23 — card 18b deleted; clustering replaced by embeddings (`embed_model`). Registry row kept for rollback only |
| `embed_model` | `## Outlet Feeds → ### Tuning` | `voyage-4-lite` | W3 semantic-dedup embedder (§5.3 card 15d) — Voyage, collapses same-story dupes pre-body |
| `rescore_model` | `## Outlet Feeds → ### Tuning` | `claude-opus-4-8` | W3 body re-score (§5.3 card 17) |
| `digest_model` | `## Outlet Feeds → ### Tuning` | `claude-opus-4-8` | W3 story summaries (§5.3 card 18d) |
| `llm_model` | `## X Watchers → ### Tuning` | `claude-opus-4-8` | W5 sentiment / thesis-divergence (§7.2 card 14) |
| `triage_prompt` | `## Outlet Feeds → ### Prompts` | card-5 `DEF_P` fallback | W3 triage scoring rubric (tokens: `{tickers}` `{themes}` `{items}`) |
| `rescore_prompt` | `## Outlet Feeds → ### Prompts` | card-5 `DEF_P` fallback | W3 body re-score rubric (same tokens) |
| `cluster_prompt` | `## Outlet Feeds → ### Prompts` | card-5 `DEF_P` fallback | ⚠ DEPRECATED 2026-07-23 — no LLM cluster call remains (embeddings replaced it); prompt unused, kept for rollback |
| `digest_prompt` | `## Outlet Feeds → ### Prompts` | card-5 `DEF_P` fallback | W3 per-story summary style (tokens: `{tickers}` `{themes}` `{items}`) |

The only hardcoded model strings anywhere are the throwaway §6.2 verification calls and the in-code fallback defaults mirroring this table. Prompt-editing contract (tokens, required vs optional, formatting rules) is documented in the registry section itself.

### 2.5 Error watchdog (build before anything else)

1. **Create Workflow** → rename `Error Watchdog`.
2. **Node 1 — Error Trigger** (no schedule — it fires when any referencing workflow fails).
3. **Node 2 — Telegram** (connect from 1) — existing credential · **Chat ID** `1779654963` · **Text** → Expression → `⚠️ n8n workflow {{ $json.workflow.name }} failed: {{ $json.execution.error.message }}`.
4. Registration is per-consumer and easy to forget: every workflow's `⋯` → **Settings** → **Error Workflow** → `Error Watchdog`. A workflow without the setting fails silently — audit it whenever a workflow is created or imported.
5. Test: temporarily point any workflow's Read node at a nonexistent path → run → the ⚠️ arrives → revert.

Without this, a silently dead watcher is worse than no watcher — you'll trust coverage you don't have.

### 2.6 Ticker universe (used by Workflow 3's ticker channels and Workflow 5)

Derive from thesis filenames — no separate list to maintain:

Execute Command → `ls "/Users/alexcohen/InvestmentVault/Theses" | sed -E 's/ - .*//' | sort -u`

Yields ~70 tickers (hyphenated and numeric Asia listings included). Read-only; safe.

---

## 3. Workflow 1 — Price Tripwires

**What:** Daily quote check of every active row in [[_watchers.md]] §Price Tripwires — Conviction-Trigger levels become live pages.

| | |
|---|---|
| Build effort | ~1 h (one workflow) |
| Running cost | $0 marginal — existing FMP plan; 1 API call/day |
| Maintenance | ~15 min/mo — keep `_watchers.md` tripwire levels in sync with Conviction Triggers as theses evolve |
| Benefit | **High.** Conviction Triggers are falsifiable if/then statements with nothing watching the "if". MRVL example: bear zone $80–110, bull legs $210+, from $188.30 — a -15% two-session move (Jul 15–16) is exactly the event class that should page you same-day |
| Status | **Live** — daily 07:35 AEST (after US close, staggered behind Workflow 2's 07:30) |

**Build** (click-level cards: §3.1)**:**
1. Read the **Price Tripwires** section of [[_watchers.md]] (§2.4) — levels live there, not in the workflow, so you edit them in Obsidian (or via the vault assistant) without touching n8n.
2. Parse active rows (Code node) → **HTTP Request** batch quote (`stable/batch-quote-short?symbols=MRVL,AVGO,...` — comma-joined tickers, one call; v3 endpoints are legacy-dead on this key) → **Code** compare → **Telegram** on breach, citing the thesis.
3. Discipline: a tripwire firing is a signal to *read the thesis trigger block*, not to act. Update levels in `_watchers.md` whenever `/status` or `/sync` changes a trigger.

---

### 3.1 Build cards (daily 07:35 · 7 nodes · ~30 min)

Node name `Rows` is load-bearing (`$('Rows')` in card 6).

**1 · Schedule Trigger** — **Trigger Interval** `Days` · **Days Between Triggers** `1` · **Trigger at Hour** `7am` · **Trigger at Minute** `35` (staggered behind Workflow 2's 07:30).

**2 · Read/Write Files from Disk** — **Operation** `Read File(s) From Disk` · **File(s) Selector** `/Users/alexcohen/InvestmentVault/_watchers.md`.

**3 · Extract from File** — **Operation** `Text`.

**4 · Code — rename `Rows`** — parses the 6-column Price Tripwires table (bare wikilinks only in cells, per the §2.4 constraint):

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

**5 · HTTP Request — rename `Quotes`** — **Method** `GET` · **URL** → Expression → `https://financialmodelingprep.com/stable/batch-quote-short?symbols={{ $json.symbols }}` · **Authentication** → Generic Credential Type → **Query Auth** → FMP credential (param name `apikey`, key from `.data/config.json`). One call for the whole table; `stable/` only — v3 endpoints are legacy-dead on this key.

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

---

## 4. Workflow 2 — Catalyst Reminders

**What:** Daily 07:30 — parse [[_catalyst.md]], push Telegram alerts for events today and T-2, and flag when the calendar itself is >30 days old ("run `/catalyst`").

| | |
|---|---|
| Build effort | 1–2 h |
| Running cost | $0 |
| Maintenance | ~0 — parser is coupled to `/catalyst`'s table format; re-check after any `/catalyst` spec change |
| Benefit | **High.** 63 events/13 weeks in the current window; the 55-day staleness episode is the proven failure mode. Dated observables (MRVL Q2 FY27 print late Aug, OCP Oct, re:Invent Nov–Dec) stop depending on memory |
| Status | **Live** — daily 07:30 |

**Build** (click-level cards: §4.1)**:**
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

⚠ **Second limitation (NOT accepted):** the deployed regex matches only single-wikilink ticker cells — `/catalyst` writes aliased multi-ticker cells (`[[path\|A]], [[path\|B]]`), which the parser skips entirely, so multi-thesis events never alert (the GENIUS Act deadline row is a proven miss — §11). Fixed parser in §4.1 card 4 — paste it over the deployed Code node at the next n8n touch.

---

### 4.1 Build cards (daily 07:30 · 5 nodes · ~30 min)

**1 · Schedule Trigger** — `Days` · `1` · Hour `7am` · Minute `30`.

**2 · Read/Write Files from Disk** — Read · `/Users/alexcohen/InvestmentVault/_catalyst.md`.

**3 · Extract from File** — `Text`.

**4 · Code** — ⚠ the step-3 parser in the card above is what's deployed; the block below is the **fixed parser** (apply at next n8n touch). Deployed-regex failure mode: `\[\[([^\]]+)\]\]\s*\|` requires the ticker cell to be exactly one wikilink — `/catalyst` writes aliased multi-ticker cells (`[[Theses/…\|CRCL]], [[Theses/…\|BTC]]`), which never match, so multi-thesis events are silently skipped (the GENIUS Act deadline row: proven miss). Fix: collapse wikilinks to their alias BEFORE cell-splitting — the alias `\|` inside `[[path\|TICKER]]` is exactly what breaks naive pipe-splitting:

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

**Coupling reminder (§8):** this parser is bound to `/catalyst`'s table format — re-test the same day any `/catalyst` spec change lands.

---

## 5. Workflow 3 — News Sweep (unified: outlet feeds + 4 search engines + body pipeline + story clustering + Opus brief)

**What:** daily morning sweep (single run) of five acquisition channels — the ~94-row `## Outlet Feeds` registry, FMP ticker news, and **GDELT + Brave + Google News each running every thesis ticker AND every News & Thematic row** — → dedupe → headline triage (Sonnet) → body pipeline (defuddle full-text fetch + body-informed re-score, Opus — Lane A) → **story clustering** (the same event reported by several outlets consolidates into one entry) → **Opus-summarised daily intel brief** — one summary per story with links to every source article — in `Daily Intel/` + Telegram top-lines. **No `_Inbox/` deposits** (Lane C reverted): the brief is the scanning surface; you hand-pick links for `/ingest`.

**Merge history & decisions:** §11. Legacy v1 build preserved at §5.8; it deactivates at §5.6 cutover.

**Mechanism notes:** GN = search-as-RSS headline backstop (redirect-encoded links, `body: false`; decode hack deliberately not built). GDELT free/keyless, 1 req/5s hard limiter → Wait-node pacing; ~100 paced queries put run time at ~15–25 min (fine — it's a background sweep, staggered off other schedules). Brave = paid metered tier (~3,000 queries/mo at full coverage, 1×/day — still above the 2,000 free cap). FMP `stable/news/stock` batch on the existing key — no keyword search (probed conclusively). **Per-ticker search queries use the company name from the thesis filename, not the raw ticker** — GDELT rejects short quoted terms, and numeric Asia listings ("000660", "2802") are unsearchable as strings while "SK Hynix" and "Ajinomoto" are not.

|              |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Build effort | ~5–7 h (§5.1–§5.7 below)                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Running cost | ~$60–110/mo (capability-forward tiering — §11) — **Sonnet headline triage ~$15–30** (widest stage, ~2k items/day) + Sonnet clustering ~$1–2 + **Opus body re-score ~$10–15** + **Opus story summaries ~$25–50** + **Brave paid ~$8–15** (~3,000 queries/mo metered; verify pricing); GDELT free; FMP existing plan. All four models are §2.4 registry cells — de-escalate (Haiku triage, Sonnet summaries) if the bill outgrows the value |
| Maintenance  | ~20 min/mo — feed rot (zero-item rows in the brief), registry prune, threshold tuning via `### Tuning (body pipeline)`                                                                                                                                                                                                                                                                                                                                        |
| Benefit      | **High.** Complete daily coverage — every ticker × 4 engines, every theme × 3 engines, 94 named sources — body-verified scoring, and a readable morning brief instead of a link dump                                                                                                                                                                                                                                                                          |
| Status       | **In build** — supersedes both v1 (live until cutover) and the 3b plan; build §5.1–§5.7, cutover §5.6                                                                                                                                                                                                                                                                                                                                              |

**Channels:**

| Channel | Intent source | Queries/run | Notes |
|---|---|---|---|
| Outlet feeds | `## Outlet Feeds` rows | ~94 RSS pulls | `triage: no` rows auto-admit; `body_exempt` ids headline-only |
| FMP ticker news | Thesis filenames (ticker prefix, US-listed) | ~7 batch calls (chunk 10, limit 250 + date window) | Ticker-scoped only — FMP keyword search conclusively absent; US symbols only (foreign listings via GN/GDELT/Brave) |
| GDELT | News & Thematic rows + all ticker company names | ~100, Wait-paced | `gdelt_spacing_s` between calls; quote-drop for terms <5 chars |
| Brave news | Same targets | ~100 | Paid metered tier; `brave_budget_mo` guard 3500 |
| Google News RSS | Same targets | ~100 RSS pulls | Headline-only breadth backstop (`body: false`) |

**Governance:** Rule 1 — writes only new dated files into `Daily Intel/`; `_Inbox/` untouched. Rule 2 (2026-07-21 form) — LLM stages read bodies and write analytical summaries with coverage implications, brief-only; grounded-in-source with labeled inference. Vault ingestion, propagation, and conviction stay in `/ingest` + skills with full mental-models context.

---

**Step-by-step build** — §5.1–§5.7:

> ⬥ on a card marks a delta from the original Workflow 3b spec this guide was authored as — full amendment history in §11.

### 5.1 Pre-build verification (~15–20 min — do NOT skip; §11 records what skipping the §6.2 checks cost last time)

Ten checks, Terminal + browser, in order. Each has a command, what PASS looks like, and the fix on FAIL. Record anything that deviates — a deviation here is one cheap fix; the same deviation discovered mid-build is an hour of node archaeology. Failures in checks 1–7 block the build; 8–10 degrade specific features only.

**How to run these.** Every ` ```bash ` block gets pasted into **Terminal** on this Mac (Cmd-Space → "Terminal"), one block at a time; output prints directly below the command. Anything in `<angle brackets>` is a placeholder — replace it with the real value *before* pressing Enter. Where each key comes from:

| Key | Where to get it | Check |
|---|---|---|
| Anthropic | console.anthropic.com → API Keys. n8n **masks** stored credentials — you cannot copy a key back out of n8n, so if it isn't saved anywhere else, create a fresh key there (and update the n8n credential to match) | 4 |
| Brave | brave.com/search/api → API Keys tab | 5 |
| FMP | already on disk in `.data/config.json` — check 7's command reads it for you, nothing to paste | 7 |

Checks 4 and 5 set the key as a shell variable on the first line (`..._KEY='paste-here'`) so you substitute it exactly once and the curl lines run untouched; the variable exists only in that Terminal window and vanishes when you close it — nothing is written to any file. Checks 1, 6, 8, 9, 10 need no key at all — paste as-is.

**1 · Runtime up.**
```bash
pm2 status
```
PASS: n8n row shows `online`. Then browser → `http://localhost:5678` → the workflow editor loads. FAIL: `pm2 restart n8n`; if the process is missing entirely, redo §1.3.

**2 · Execute Command node available.** In n8n: open any workflow → `+` → search `Execute Command` → the node appears in the panel. This build uses it four times (Tickers, PriorStories, Catalyst, XDash) plus Defuddle. FAIL: the §1.3 `NODES_EXCLUDE` override is missing from the pm2 environment — re-apply it, `pm2 restart n8n`, re-check.

**3 · Credentials + watchdog present.** n8n → **Credentials**: `Telegram`, `FMP` (Query Auth, param `apikey`), `Anthropic` (Header Auth, `x-api-key`) all listed. n8n → **Workflows**: `Error Watchdog` exists and is published (§2.5). FAIL: create the missing piece before proceeding — every card that needs one references these by name, and the watchdog must exist before card 1 sets it as the error workflow.

**4 · Anthropic key, models, and balance.** The workflow calls **both** tiers — Sonnet (triage, clustering) and Opus (re-score, summaries) — so test both. In line 1, replace `paste-key-here` with your Anthropic key (keep the single quotes); then paste the whole block into Terminal at once — the two curls reuse the key set on line 1 and hit each model in turn:
```bash
ANTH_KEY='paste-key-here'
curl -s https://api.anthropic.com/v1/messages -H "x-api-key: $ANTH_KEY" \
  -H "anthropic-version: 2023-06-01" -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-5","max_tokens":16,"messages":[{"role":"user","content":"Reply with exactly: ok"}]}'
curl -s https://api.anthropic.com/v1/messages -H "x-api-key: $ANTH_KEY" \
  -H "anthropic-version: 2023-06-01" -H "content-type: application/json" \
  -d '{"model":"claude-opus-4-8","max_tokens":16,"messages":[{"role":"user","content":"Reply with exactly: ok"}]}'
```
PASS: each of the two responses is JSON with a `content` array whose text block says `ok`. FAIL: `authentication_error`/401 → wrong key; `not_found_error`/404 on a model → the §2.4 registry cell names a model this key can't reach — fix the cell or the account. **Then check the prepaid balance at console.anthropic.com** — an exhausted balance does not break the build, it silently 400s every LLM node at runtime (On-Error-Continue) and ships headline-only briefs.

**5 · Brave paid tier + key.** Dashboard first: browser → brave.com/search/api → log in → confirm the subscription shows a **paid metered plan** (free 2,000/mo < the ~3,000/mo this workflow issues — a free key passes the curl below and then dies mid-month). Then in Terminal — replace `paste-key-here` on line 1 with your Brave key (API Keys tab on that same dashboard), then paste the whole block:
```bash
BRAVE_KEY='paste-key-here'
curl -s -H "X-Subscription-Token: $BRAVE_KEY" -H 'Accept: application/json' \
  'https://api.search.brave.com/res/v1/news/search?q=TSMC%20capex&count=3&freshness=pd' | head -c 600
```
PASS: JSON with `results[]` whose entries carry `title` / `url` / `description` / `age` / `meta_url.hostname` (card 9's BParse reads exactly these — if Brave renamed a field, BParse is the ONLY place to fix it). FAIL: 401 → key; 429 → burst or still on free tier.

**6 · GDELT reachable from THIS machine.** No key — GDELT is a free open API; paste the block exactly as-is. The limiter is per-IP and the n8n host is this Mac — testing from anywhere else proves nothing. Mind the sticky cooldown if you probed recently:
```bash
curl -s 'https://api.gdeltproject.org/api/v2/doc/doc?query=TSMC%20capex&mode=artlist&format=json&maxrecords=3&timespan=24h'
```
PASS: `{"articles":[...]}` with `title` / `url` / `seendate` / `domain` (card 8's GParse fields). FAIL: prose rate-limit text (HTTP 200!) → wait 10 min, retry ONCE, never burst — a burst extends the cooldown.

**7 · FMP batch size on this key.** Nothing to paste in by hand — line 1 reads the key straight out of `.data/config.json`, line 2 builds a 25-ticker test batch from your actual thesis filenames, line 3 fires the call. Paste all three lines as one block:
```bash
FMP_KEY=$(sed -E 's/.*"fmp_api_key"[[:space:]]*:[[:space:]]*"([^"]+)".*/\1/' /Users/alexcohen/InvestmentVault/.data/config.json)
SYMS=$(ls /Users/alexcohen/InvestmentVault/Theses | sed 's/ - .*//' | grep -E '^[A-Z]{1,5}$' | head -25 | paste -sd, -)
curl -s "https://financialmodelingprep.com/stable/news/stock?symbols=$SYMS&limit=5&apikey=$FMP_KEY" | head -c 500
```
PASS: JSON array of articles with `symbol` / `title` / `url` / `text` / `publishedDate` / `site` (card 11's FMP branch fields). FAIL: `Invalid API KEY` → the `.data/config.json` key is stale — fix it there AND in the n8n FMP credential. FAIL on the 25-symbol call but success with 5 symbols (re-run line 2 with `head -5`) → set `FMP_CHUNK = 10` in **card 5's Plan code** (the constant lives there, nowhere else).

**8 · defuddle CLI + flag.**
```bash
defuddle parse 'https://www.zerohedge.com/markets' --markdown 2>&1 | head -20
```
PASS: clean markdown (headlines as text, no `<div>` soup). FAIL: `command not found` → `npm install -g defuddle`; `--markdown` unrecognized → `defuddle --help`, substitute the real flag in **card 17's Defuddle node**. (v0.7.0 confirmed working.)

**9 · Registry parse targets.** Plan splits `_watchers.md` on exact section headers and reads six model/threshold rows plus four prompt blocks — verify all three survive whatever editing the registry has had:
```bash
grep -c '^## Outlet Feeds\|^## News & Thematic' /Users/alexcohen/InvestmentVault/_watchers.md
grep -c 'triage_model\|cluster_model\|rescore_model\|digest_model\|story_memory_days\|catalyst_window_d' /Users/alexcohen/InvestmentVault/_watchers.md
grep -cE '^#### (triage|rescore|cluster|digest)_prompt' /Users/alexcohen/InvestmentVault/_watchers.md
```
PASS: first ≥2, second ≥6, third =4. FAIL: a renamed header = `Plan: 0 tasks` at first run; a missing Tuning row silently falls back to the code default — restore the §2.4 rows; a missing/misspelled `####` prompt header (or a prompt missing its required `{items}` / `{prior}` token) silently reverts that stage to the card-5 `DEF_P` default — your registry edits stop taking effect with no error.

**10 · Feature inputs + output folder.** Three one-liners:
```bash
head -3 /Users/alexcohen/InvestmentVault/_catalyst.md          # date: within ~30d, else 📅 markers will be empty → run /catalyst
ls -t "/Users/alexcohen/InvestmentVault/Daily Intel/"*"X Dashboard.md" 2>/dev/null | head -1   # any hit → 𝕏 markers live; none → they stay silent until W5 runs
mkdir -p "/Users/alexcohen/InvestmentVault/.data/news_stories"  # card-20 log lane target — the Write node does not create parent directories
```
The first two degrade gracefully (missing input = missing markers, never a failed run) — this check just tells you what to expect in the first brief. Also eyeball `ls /Users/alexcohen/InvestmentVault/Theses | head -5` → filenames follow `TICKER - Company Name.md`; anything without ` - ` (macro theses) is skipped by the ticker channels by design.

### 5.2 Credentials

- **Brave Search** — new Header Auth: name `X-Subscription-Token`, value = key (§2.1 row). ⬥ **Upgrade to the paid metered tier before first run**: full ticker+theme coverage ≈ 3,000 queries/mo at 1×/day vs the 2,000 free cap — verify per-1,000 pricing on the dashboard at upgrade.
- **Voyage** (embeddings dedup — card 15d) — new Header Auth. **Name** `Authorization` · **Value** `Bearer <your-voyage-key>` (the literal word `Bearer`, a space, then the key). Get the key at voyageai.com/dashboard → API Keys. n8n masks it after save, same as Anthropic — keep a copy in your password manager. ⬥ **Do NOT paste the key into this doc, into Obsidian, or into chat** — it lives only in the n8n credential store (encrypted at rest per §1.2). Verify it works before building (replace the placeholder, paste the whole block into Terminal):
```bash
VOYAGE_KEY='paste-key-here'
curl -s https://api.voyageai.com/v1/embeddings -H "Authorization: Bearer $VOYAGE_KEY" \
  -H "content-type: application/json" \
  -d '{"model":"voyage-4-lite","input":["two articles about the same event","the same event, reworded headline"],"input_type":"document"}' \
  | head -c 300; echo
```
  PASS: JSON with a `data` array of two objects each carrying an `embedding` array + a `usage.total_tokens` count. FAIL: `401`/`invalid api key` → wrong key; `model not found` → check the model string is exactly `voyage-4-lite`. (The two sample strings are near-duplicates by design — the whole layer rests on their vectors landing close.)
- FMP (Query Auth) and Anthropic (Header Auth) — already exist.

### 5.3 Build cards

New workflow `Workflow 3 — News Sweep (unified)` → Settings → Error Workflow: `Error Watchdog`.

**Reading the cards — the `{{ … }}` convention.** Any text in double curly braces is an **n8n expression**: the literal string you paste into a node's field after flipping that field from *Fixed* to **Expression** (the small fx/toggle on the field). n8n evaluates it at runtime — `{{ $json.ch }}` reads the current item's `ch` value, and so on. These are **not unfilled placeholders**; the doc is complete — paste them exactly as printed, braces included, nothing to substitute. Longer expressions sit in their own code blocks under the field they belong to; copy the whole line. Never prefix an equals sign in the expression editor (n8n adds one internally when saving). **Node names are load-bearing**: the quoted name on each card (`"Tickers"`, `"BodyLoop"`, `"SumPrep"`, …) is referenced by other nodes' code as an exact string (`$('BodyLoop')`) — a default name or typo produces `Referenced node doesn't exist` the first time that path executes (often days later, when the branch first carries items). Name every node exactly as carded. **Re-arm after every edit**: n8n 2.x does NOT reliably re-register a scheduled workflow's cron trigger on Save — after editing/re-pasting any node in an *active* scheduled workflow (W1–W5), finish by toggling **Active OFF→ON**, or the next scheduled run silently won't fire (the workflow stays `active=1` but the cron is dropped — confirmed live on W5 07-21). Manual "Execute Workflow" keeps working, which masks it.

**1 · Schedule Trigger** — one rule: **Trigger Interval** `Days` · **Days Between Triggers** `1` · **Trigger at Hour** `7am` · **Trigger at Minute** `10`. Daily morning run only (cadence decision: §11). §5.6 cutover moves it to 07:00.

**2 · Execute Command "Tickers"** — ⬥ Command:
`ls /Users/alexcohen/InvestmentVault/Theses | sed 's/\.md$//'`
On Error: Continue. Emits one `TICKER - Company Name` line per thesis: the ticker prefix drives the FMP channel (US-listed filter applied in Plan); the company name drives the per-ticker GN/GDELT/Brave queries — names beat raw tickers in news search, and numeric Asia listings ("000660", "2802") are unsearchable as strings while "SK Hynix" and "Ajinomoto" are not.

**2b · Execute Command "PriorStories"** — ⬥ story memory: reads the recent run logs the card-20 `log` lane wrote, so clustering can recognise follow-up coverage of already-briefed stories. On Error: Continue (empty on first run — no memory, no repeats detection, run proceeds). Command:

```
cd /Users/alexcohen/InvestmentVault/.data/news_stories 2>/dev/null && for f in $(ls -t *.json 2>/dev/null | head -14); do cat "$f"; printf '\n@@@\n'; done
```

**2c · Execute Command "Catalyst"** — ⬥ catalyst proximity: `cat /Users/alexcohen/InvestmentVault/_catalyst.md` · On Error: Continue (missing/stale calendar → no 📅 markers, run proceeds; Workflow 2's staleness nag is the freshness guard).

**2d · Execute Command "XDash"** — ⬥ X attention overlay: `ls -t "/Users/alexcohen/InvestmentVault/Daily Intel/"*"X Dashboard.md" 2>/dev/null | head -1 | xargs cat 2>/dev/null` · On Error: Continue (no dashboard → no 𝕏 markers).

**3 · Read/Write Files from Disk "ReadReg"** — Read, `/Users/alexcohen/InvestmentVault/_watchers.md`. Wire 1→2→2b→2c→2d→3.

**4 · Extract from File "RegText"** — Operation: Text.

**5 · Code "Plan"** (Run Once for All Items) — ⬥ parses both registry sections + Tuning, emits one task item per source call. Delta from the 3b spec: per-ticker search targets (company names) added to GN/GDELT/Brave; Brave runs both daily sweeps (paid tier — no morning gate); clip params dropped; `digest_model` param added:

```javascript
const DEF = { triage_min:7, triage_min_pw:9, gdelt_spacing_s:8, brave_budget_mo:3500, story_memory_days:7, catalyst_window_d:10, max_age_d:3, tg_max_msgs:10, tg_per_subject:2, dedup_ttl_d:3, track_min_score:8, track_window_d:30, merge_jaccard:0.42,
  sim_threshold:0.86, repeat_threshold:0.88, embed_max_chars:1000,
  triage_model:'claude-sonnet-5', cluster_model:'claude-opus-4-8', embed_model:'voyage-4-lite',
  rescore_model:'claude-opus-4-8', digest_model:'claude-opus-4-8',
  paywall_domains:['bloomberg.com','wsj.com','ft.com','economist.com','nytimes.com','theinformation.com','barrons.com'],
  body_exempt:['digitimes','ft-home','bbg-tech','bbg-econ','bbg-markets','wsj-markets','wsj-tech','wsj-business','econ-finance','econ-business','nyt-business','nyt-tech','theinformation','techmeme','mediagazer'] };
const md = $('RegText').first().json.data || '';
const now = new Date();
const today = `${now.getFullYear()}-${String(now.getMonth()+1).padStart(2,'0')}-${String(now.getDate()).padStart(2,'0')}`;
const section = h => (md.split('## '+h)[1] || '').split(/\n## /)[0];

// Tuning params (fallback = DEF)
const tun = section('Outlet Feeds');
const cfg = {...DEF};
for (const k of ['triage_min','triage_min_pw','gdelt_spacing_s','brave_budget_mo','story_memory_days','catalyst_window_d','max_age_d','tg_max_msgs','tg_per_subject','dedup_ttl_d','track_min_score','track_window_d','merge_jaccard','sim_threshold','repeat_threshold','embed_max_chars']) {
  const m = tun.match(new RegExp('\\|\\s*'+k+'\\s*\\|\\s*([^|]+?)\\s*\\|'));
  if (m && !isNaN(parseFloat(m[1]))) cfg[k] = parseFloat(m[1]);
}
for (const k of ['triage_model','cluster_model','rescore_model','digest_model','embed_model']) {
  const m = tun.match(new RegExp('\\|\\s*'+k+'\\s*\\|\\s*([^|]+?)\\s*\\|'));
  if (m) cfg[k] = m[1].trim();
}
const ex = tun.match(/\|\s*body_exempt\s*\|\s*([^|]+?)\s*\|/);
if (ex) cfg.body_exempt = ex[1].split(',').map(s=>s.trim()).filter(Boolean);
const pwd = tun.match(/\|\s*paywall_domains\s*\|\s*([^|]+?)\s*\|/);
if (pwd) cfg.paywall_domains = pwd[1].split(',').map(s=>s.trim()).filter(Boolean);

// LLM prompts — registry-editable (### Prompts → #### blocks); missing block or missing REQUIRED token → code fallback
const DEF_P = {
  triage_prompt:`You score news items for one investor. Coverage tickers: {tickers}. Live research questions: {themes}. Clusters also covered: semis, datacenter, china-tech, macro, AI, futurism, tech philosophy, consumer tech. Score each item 0-10 on NEW information value to this coverage: 9-10 directly material new fact (guidance, capacity, pricing, regulatory, primary technical disclosure); 7-8 clearly relevant development; 4-6 adjacent context; 0-3 noise — listicles, price-target roundups, "stocks to buy", rehash, sponsored. Judge information content, not sentiment. Items flagged pw:1 are paywalled — only the headline is readable; hold them to a stricter bar: 8-10 only if the headline alone discloses a material new fact for this coverage, otherwise 0-3. Items: {items} — Return ONLY a JSON array [{"i":0,"s":7},...] covering every item.`,
  rescore_prompt:`Re-score these news items 0-10 for NEW information value to an investor covering: {tickers}. Live research questions: {themes}. Each item carries its headline score (hs, may be null for auto-admitted sources) and an article excerpt (x). Confirm the article delivers substance — new numbers, primary quotes, disclosed specifics. Downgrade rehash/opinion; upgrade if the body reveals material specifics the headline undersold. Items flagged pw:1 are paywalled (excerpt is headline-grade only) — keep them high only if that alone is materially new. Items: {items} — Return ONLY a JSON array [{"i":0,"s":7},...] covering every item.`,
  cluster_prompt:`NEW ITEMS are news items from today, from multiple sources; each carries its headline (t) AND a content excerpt (x). PRIOR STORIES were already briefed to the reader on previous days (label, title, summary). Judge same-story on the EXCERPT's substance — the actors, action, and event it describes — NOT on headline wording; two articles with completely different headlines by different authors are the same story if their excerpts describe the same event. Two tasks. (1) Group NEW items that cover the SAME underlying story or event into clusters. Two items are the same story when they report the same actor + action + timeframe (the same announcement, filing, decision, result, or incident), even if headlines emphasize different aspects, figures, or reactions — multiple outlets covering one event is ONE cluster. Keep items separate only when the underlying events genuinely differ (different actors, different actions, or clearly distinct developments). (2) A NEW item that is follow-up coverage of a PRIOR story AND adds no material new facts beyond that story's summary is a repeat — list it under repeats with the prior label. If it ADVANCES the story (new numbers, official responses, next-step events, a material escalation), it is NOT a repeat — cluster it as new. Bias toward repeat: same event with no NEW specific (a number, a named actor, an official action) beyond the prior summary is a repeat even if the wording, outlet, or angle differs — when torn between repeat and new, choose repeat. NEW ITEMS: {items} PRIOR STORIES: {prior} — Return ONLY JSON: {"clusters":[[indices]],"repeats":[[itemIndex,"P<n>"],...]} with every NEW item index appearing exactly once across clusters and repeats.`,
  digest_prompt:`You write a daily intelligence brief for one investor. Coverage tickers: {tickers}. Live research questions: {themes}. Each item is one story, possibly reported by several sources (srcs) with merged excerpts. For each item write "sum": 2-5 sentences of decision-useful analysis. Lead with the concrete NEW facts — numbers with the comparison that gives them meaning (vs prior guidance, consensus, rivals), named actors, the mechanism of what changed, and stated timelines or next dates. Then state what it means for the coverage: which ticker or research question it touches and the transmission path (pricing power, capacity, share shift, cost curve, regulation, demand signal), and what would confirm or refute that read. Ground every claim in the provided text; label inference explicitly ("implies", "suggests", "if X then Y"). Where sources disagree on a figure, say so. Some items carry sig — the investor's live signals for the tickers involved (catalyst proximity, crowd sentiment); weave these into the implication when they sharpen it. Standing investor context: {context}. If the text is thin or navigation junk, one sentence restating the headline claim. Items: {items} — Return ONLY a JSON array [{"i":0,"sum":"..."},...] covering every item.` };
const REQ_P = { triage_prompt:['{items}'], rescore_prompt:['{items}'], cluster_prompt:['{items}','{prior}'], digest_prompt:['{items}'] };
for (const k of Object.keys(DEF_P)) {
  const m = tun.match(new RegExp('#### '+k+'\\s*\\n([\\s\\S]*?)(?=\\n#{2,4} |$)'));
  const txt = m ? m[1].trim() : '';
  cfg[k] = (txt && REQ_P[k].every(t=>txt.includes(t))) ? txt : DEF_P[k];
}
const bc = tun.match(new RegExp('#### brief_context\\s*\\n([\\s\\S]*?)(?=\\n#{2,4} |$)'));
cfg.brief_context = bc ? bc[1].trim() : '';   // optional standing-priorities block → digest {context}; absent = fine

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
const tickers = [], tickerFiles = {};
for (const f of files) {
  const i = f.indexOf(' - '); if (i < 0) continue;
  const tk = f.slice(0,i).trim(), name = f.slice(i+3).trim();
  tickers.push(tk);
  tickerFiles[tk] = f;   // "MRVL" → "MRVL - Marvell Technology" — lets Assemble wikilink stories to theses
  targets.push({ id:'tk-'+tk.toLowerCase(), q:`"${name}"`, cluster:'ticker' });
}
// GDELT rate-limit priority: its budget dies after ~4 rapid calls, so order the queue to spend it on GDELT's unique edge —
// FOREIGN tickers first (intl coverage GN/FMP lack), then themes; US tickers last (GDELT-skipped below, kept here for GN/Brave)
const gdeltRank = t => (t.cluster === 'ticker')
  ? (/^[A-Z]{1,5}$/.test(t.id.slice(3).toUpperCase()) ? 2 : 0)   // US ticker → 2 (last); foreign ticker → 0 (first)
  : 1;                                                            // thematic → 1 (middle)
targets.sort((a,b) => gdeltRank(a) - gdeltRank(b));               // stable sort (Node/V8) — preserves registry/file order within each rank
// Channels 2–4 — GN + GDELT + Brave for EVERY target (themes AND tickers, both daily runs)
for (const t of targets) {
  tasks.push({ ch:'gn', id:t.id, cluster:t.cluster, bypass:false, body:false,
    url:`https://news.google.com/rss/search?q=${encodeURIComponent(t.q + ' when:' + (cfg.max_age_d || 3) + 'd')}&hl=en-US&gl=US&ceid=US:en` });
  let g = t.q.replace(/\bAND\b/g,' ').replace(/"([^"]{1,4})"/g,'$1').replace(/\s+/g,' ').trim();
  if (/\bOR\b/.test(g) && !g.startsWith('(')) g = '('+g+')';
  const usTicker = t.cluster === 'ticker' && /^[A-Z]{1,5}$/.test(t.id.slice(3).toUpperCase());   // same rule as FMP's `us` filter
  if (!usTicker)   // GDELT: keep themes + FOREIGN tickers (its unique intl edge); drop US tickers — GN+FMP already blanket them, and GDELT's ~4-call rate-limit budget is better spent on coverage the other channels lack
    tasks.push({ ch:'gdelt', id:t.id, cluster:t.cluster, bypass:false, body:true, q:g });
  tasks.push({ ch:'brave', id:t.id, cluster:t.cluster, bypass:false, body:true, q:t.q.replace(/\bAND\b/g,' ') });
}
// Channel 5 — FMP ticker news (US-listed ticker prefixes only; chunk 10, limit+window in card 10)
const FMP_CHUNK = 10;                                        // 25→10 (2026-07-23); coverage lever is limit+window in card 10, not chunk size
const FMP_ALIAS = { KLA: 'KLAC' };                           // filename prefix → FMP symbol where they differ (KLA is KLAC on Nasdaq; add a row if a US name silently returns 0 in the brief's fmp count)
const us = tickers.filter(s=>/^[A-Z]{1,5}$/.test(s)).map(s=>FMP_ALIAS[s] || s);
const fmpTo = new Date().toISOString().slice(0,10);          // FMP news/stock caps at 250/call across the batch, recency-sorted — the window keeps the 250 in-scope, not spent on stale items
const fmpFrom = new Date(Date.now() - (cfg.max_age_d || 3) * 86400000).toISOString().slice(0,10);
for (let i=0;i<us.length;i+=FMP_CHUNK)
  tasks.push({ ch:'fmp', id:'fmp-'+(1+i/FMP_CHUNK), cluster:'ticker', bypass:false, body:true, symbols:us.slice(i,i+FMP_CHUNK).join(','), from:fmpFrom, to:fmpTo });

if (!tasks.length) throw new Error('Plan: 0 tasks — registry parse failed');
cfg.tickers = tickers.join(',');
cfg.ticker_files = tickerFiles;
// Catalyst proximity (±catalyst_window_d days) — alias-safe row parse, same technique as Workflow 2's fixed parser
const cmd = ((($('Catalyst').first() || {}).json || {}).stdout) || '';
const catalysts = {};
for (const line of cmd.split('\n')) {
  if (!/^\|\s*\d{4}-\d{2}-\d{2}\s*\|/.test(line)) continue;
  const cells = line.replace(/\[\[(?:[^\]|]*\|)?([^\]|]+)\]\]/g, '$1').split('|').map(s=>s.trim());
  const diff = Math.round((new Date(cells[1]) - now) / 86400000);
  if (Math.abs(diff) > cfg.catalyst_window_d) continue;
  for (const t of (cells[2]||'').split(',').map(s=>s.trim()).filter(Boolean))
    (catalysts[t] = catalysts[t] || []).push({ ev: (cells[3]||'').slice(0,60), diff });
}
cfg.catalysts = catalysts;
// X attention overlay — per-theme sentiment scraped from the latest W5 dashboard (text match; absent → no markers)
const xdash = ((($('XDash').first() || {}).json || {}).stdout) || '';
const xread = {};
for (const m of xdash.matchAll(/^\|\s*\$?([A-Z0-9.\-]{1,12})\s*\|.*?(bullish|bearish|mixed|quiet)/gim))
  xread[m[1].toUpperCase()] = m[2].toLowerCase();
cfg.x_read = xread;
cfg.themes = targets.filter(t=>t.cluster==='thematic').map(t=>`${t.id}: ${t.q}`).join(' · ');
return tasks.map(t => ({ json: {...t, cfg} }));
```

**6 · Switch "Route"** — Rules on `{{ $json.ch }}` (String, equals): `feed`→0, `gn`→1, `gdelt`→2, `brave`→3, `fmp`→4 · Options → **Fallback Output: None** (Plan only emits those five values; a stray one should vanish visibly, not contaminate a channel). Output destinations: **0 AND 1 → 6b FeedTasks** (never directly into Feeds — two wires into one node execute it per delivery) · 2 → GdeltLoop (8.1) · 3 → BraveLoop (9.1) · 4 → FMP (10).

**6b · Merge "FeedTasks"** — Mode: Append · **Number of Inputs `2`** · Input 1 ← Route output 0 (`feed`) · Input 2 ← Route output 1 (`gn`) · output → Feeds (card 7). Collapses the two RSS task streams into ONE delivery so the RSS node executes once. Without it (observed, first build 2026-07-20), two wires into Feeds run the RSS node twice — and each delivery separately re-executes the entire Normalize→digest chain downstream. Both Route outputs always carry tasks, so neither input can starve this Merge.

**7 · RSS Read "Feeds"** — from FeedTasks (single wire — feeds and Google News are both RSS URLs, read by the same node). URL → Expression → `{{ $json.url }}`. On Error: **Continue (using error output)**. This node has **two outputs, and both wire into PreNormalize (card 10b)**: the **main** output (→ input 1) carries fetched articles; the **error** output (→ input 2) carries failed-feed items, which Normalize detects and logs as feed-rot warnings (dead feeds surface instead of vanishing).

**8 · GDELT loop** (from Route output 2) — GDELT enforces a **1 request / 5 s per-IP** limiter with a sticky cooldown (proven in §5.1 check 6), so GDELT tasks cannot fan out in parallel like the other channels. This card serialises them through a batch loop with a pacing Wait between calls. **Four nodes**, built in order:

**8.1 · Loop Over Items "GdeltLoop"** — node type **Loop Over Items** (older n8n labels it **Split In Batches** — same node). **Batch Size `1`.** Wire **Route output 2 → GdeltLoop input**. The node has **two outputs**, which n8n labels by name (wire by the name, not by top/bottom position):
- **`loop`** — emits one batch (one GDELT task) per pass; feeds the fetch chain below.
- **`done`** — fires once, after the last batch is processed; feeds Normalize.

**8.2 · HTTP Request "Gdelt"** — from GdeltLoop's **`loop`** output. Method **GET**, no credential (open API). URL → toggle to **Expression** → paste:
```
https://api.gdeltproject.org/api/v2/doc/doc?query={{ encodeURIComponent($json.q) }}&mode=artlist&format=json&maxrecords=250&timespan={{ (Number($('Plan').first().json.cfg.max_age_d) || 3) * 24 }}h
```
**On Error: Continue.** (GDELT returns HTTP 200 with *prose* when rate-limited, not an HTTP error — GParse's `|| []` absorbs that; On-Error-Continue only guards a genuine network drop so one bad call never kills the run.)

**8.3 · Code "GParse"** (Run Once for All Items) — from Gdelt. Converts GDELT's `articles[]` into the normalized item shape every channel shares, stamping each article with the task metadata (`feedId`, `cluster`) of the query that produced it:
```javascript
const t = $('GdeltLoop').first().json;
const arts = ($json.articles) || [];
return arts.map(a => ({ json: { ch:'gdelt', feedId:t.id, cluster:t.cluster, bypass:false, fetchBody:true,
  title:a.title, url:a.url, snippet:'', published:a.seendate||'', source:a.domain||'' } }));
```
`$('GdeltLoop').first()` resolves to the single item of the *current* batch (because Batch Size is 1) — that's how GParse knows which theme/ticker this article set belongs to. `arts` defaults to `[]`, so a rate-limited response (no `articles` key) yields zero items instead of throwing. **Settings → Always Output Data ON** — mandatory: a zero-result iteration otherwise feeds zero items back into GdeltLoop and the loop freezes mid-list, never reaching `done` (observed, first build 2026-07-20). With it ON, an empty iteration emits one `{}` placeholder that keeps the loop advancing; Normalize's URL guard drops placeholders silently.

**8.4 · Wait "Pace"** — from GParse. **Wait Amount → Unit: Seconds**, value → toggle to **Expression** → paste:
```
{{ Number($('Plan').first().json.cfg.gdelt_spacing_s) || 8 }}
```
(registry default 8 — safely above GDELT's 5 s floor; the code fallback matches). The `Number()` wrapper is required: n8n's strict type validation rejects expression results that arrive as strings in number-typed fields (`'amount' expects a number but we got '8'` — hit live, first build); `|| 8` covers a missing/unparseable registry value. Then **wire Pace's output back into GdeltLoop's input** — this back-connection is what advances the loop to the next query. It is not an infinite loop: GdeltLoop tracks which items it has emitted and routes to `done` once the task list is exhausted.

**Wiring recap for card 8:**
- Route out 2 → **GdeltLoop** (input)
- GdeltLoop **`loop`** → Gdelt → GParse → Pace → **back to GdeltLoop** (input)
- GdeltLoop **`done`** → **PreNormalize (card 10b) input 3** — the fetch-stage fan-in

**What to expect at runtime:** the loop runs once per GDELT task (one per thematic + ticker target), ~8 s apart — so *N* GDELT queries take ≈ *N* × 8 s. This is the workflow's slowest leg by design; the overnight schedule absorbs it. Each pass emits 0–50 normalized items; the `done` output itself carries no article data, it only signals "all batches finished, continue downstream."

**Pitfalls (each has a distinct symptom):**
- **`done` → PreNormalize wire missing** → the loop runs but its results reach nothing; the brief has no GDELT stories and no error.
- **Batch Size ≠ 1** → several GDELT calls fire per pass → 429 + IP cooldown (check 6's exact failure).
- **Fetch chain wired off `done` instead of `loop`** → Gdelt never receives items; loop completes instantly with zero output.
- **Loop stalls partway and `done` never fires** → a zero-result iteration fed `[]` back into the loop input. Always Output Data ON on GParse (8.3) is the guard — verify the toggle survived.
- **`gdelt_spacing_s` below ~6** → intermittent 429s that look like random missing coverage. Keep it ≥ 6; 8 is the safe default.

**9 · Brave loop** (from Route output 3) — **same loop shape as GDELT** (card 8), because Brave also has a per-second rate ceiling. The difference: Brave's limit is a *soft per-second throttle*, not GDELT's sticky IP cooldown, so the pace is a **fixed 2 s courtesy gap** rather than a registry knob — and Brave, unlike GDELT, needs a **credential**. **Four nodes:**

**9.1 · Loop Over Items "BraveLoop"** — node type **Loop Over Items** (older n8n: **Split In Batches**). **Batch Size `1`.** Wire **Route output 3 → BraveLoop input**. Two outputs, wire by name:
- **`loop`** — one Brave task per pass; feeds the fetch chain.
- **`done`** — fires once after the last batch; feeds Normalize.

**9.2 · HTTP Request "Brave"** — from BraveLoop's **`loop`** output. Method **GET**. **Credential: Brave Header Auth** (this is what supplies the `X-Subscription-Token` key — §5.2; it's the piece GDELT didn't need). Add one **extra header** under Options → Header Parameters: name `Accept`, value `application/json`. URL → toggle to **Expression** → paste:
```
https://api.search.brave.com/res/v1/news/search?q={{ encodeURIComponent($json.q) }}&count=20&freshness=pd
```
`count=20` caps results per query; `freshness=pd` restricts to the past day. **On Error: Continue** (a 429 or key error returns no `results` — BParse's `|| []` absorbs it — and must not kill the run).

**9.3 · Code "BParse"** (Run Once for All Items) — from Brave. Converts Brave's `results[]` into the shared normalized shape. **Field names differ from GDELT** — Brave uses `description` (→ snippet), `age` (→ published), and `meta_url.hostname` (→ source):
```javascript
const t = $('BraveLoop').first().json;
const arts = ($json.results) || [];
return arts.map(a => ({ json: { ch:'brave', feedId:t.id, cluster:t.cluster, bypass:false, fetchBody:true,
  title:a.title, url:a.url, snippet:a.description||'', published:a.age||'', source:(a.meta_url&&a.meta_url.hostname)||'' } }));
```
As in GParse, `$('BraveLoop').first()` = the current batch's single item, tagging each article with its theme/ticker. `a.meta_url.hostname` is guarded by `a.meta_url && …` because Brave occasionally omits the `meta_url` object — without the guard that would throw and lose the whole query's results. **Settings → Always Output Data ON** — mandatory, same stall guard as GParse (8.3): a past-day query with zero news hits is *routine* (weekends especially) and returns `[]`; without this the first quiet query freezes the whole Brave channel.

**9.4 · Wait "BravePace"** — from BParse. **Wait Amount → Unit: Seconds**, value **`2`** — a **plain fixed number, not an expression** (Brave has no sticky cooldown, so it needs no registry knob). Give it a name distinct from GDELT's `Pace` — n8n requires unique node names within a workflow. Then **wire BravePace's output back into BraveLoop's input** to advance the loop.

**Wiring recap for card 9:**
- Route out 3 → **BraveLoop** (input)
- BraveLoop **`loop`** → Brave → BParse → BravePace → **back to BraveLoop** (input)
- BraveLoop **`done`** → **PreNormalize (card 10b) input 4** — same fan-in as GDELT

**What to expect at runtime:** one pass per Brave task (thematic + ticker targets), ~2 s apart — so *N* Brave queries take ≈ *N* × 2 s, far faster than GDELT's leg. Each pass emits 0–20 normalized items; `done` carries no article data, only the completion signal.

**Pitfalls (Brave-specific first, then the shared loop traps):**
- **`Accept: application/json` header missing** → Brave can return a non-JSON body n8n won't parse → BParse sees no `results` and the channel silently yields nothing.
- **Credential not attached / wrong header name** → 401 on every call (contrast: check 5 passed because the curl sent the header explicitly).
- **Free-tier key** → passes early runs, then 429s mid-month once you cross 2,000 queries (the check-5 warning — verify the paid plan on the dashboard).
- **Reusing the name `Pace`** → n8n rejects the duplicate; that's why 9.4 is `BravePace`.
- **`done` → PreNormalize wire missing**, **Batch Size ≠ 1**, **fetch chain wired off `done` instead of `loop`**, or **loop stalls on a zero-result query** (Always Output Data OFF on BParse) → same silent failures as GDELT (card 8).

**10 · HTTP "FMP"** (from Route output 4) — a plain HTTP node, **no loop** (FMP accepts all tickers of a chunk in one call, and the paid key has no per-second cooldown to pace around). Method **GET** · **Credential: FMP Query Auth** · **On Error: Continue** · URL → toggle to **Expression** → paste:
```
https://financialmodelingprep.com/stable/news/stock?symbols={{ $json.symbols }}&from={{ $json.from }}&to={{ $json.to }}&limit=250
```
Its **main output wires into PreNormalize (card 10b) input 5** — the last of the five fetch wires. The node fires **once per chunk** (Plan emits ceil(US-tickers/`FMP_CHUNK`) fmp tasks — ~7 at chunk 10), no loop node needed.

⬥ **`limit=250` + `from`/`to` window** (2026-07-23, was `limit=50`): FMP `news/stock` returns the 250 newest articles **across the whole batch**, recency-sorted — **NOT 250 per ticker**, and 250 is the endpoint's hard ceiling (verified: `limit=1000` still returns 250). The date window (= `max_age_d`) keeps those 250 in-scope instead of spent on stale items. Two coverage limits are structural, not tunable: (1) **US-listed symbols only** — foreign listings (Amsterdam/London/Tokyo/Toronto/Sydney) don't resolve in FMP's US news feed at any limit; they ride the GN/GDELT/Brave company-name channels instead. (2) **filename-prefix ≠ exchange-ticker** mismatches silently return 0 (e.g. KLA is KLAC on Nasdaq) — fixed by the `FMP_ALIAS` map in card 5's Plan; add a row when a US name shows `fmp 0` in the brief.

**10b · Merge "PreNormalize"** — Mode: Append · **Number of Inputs `5`** · output → Normalize (card 11). The fetch-stage fan-in — every channel ends here, one input port each:

| Input | From node | Output to wire | Carries |
|---|---|---|---|
| 1 | **Feeds** (card 7) | **main** | outlet-feed + Google-News articles |
| 2 | **Feeds** (card 7) | **error** | failed-feed items → logged as feed-rot warnings |
| 3 | **GdeltLoop** (card 8.1) | **`done`** | all GDELT articles, once the loop finishes |
| 4 | **BraveLoop** (card 9.1) | **`done`** | all Brave articles, once the loop finishes |
| 5 | **FMP** (card 10) | **main** | FMP ticker-news articles |

**After wiring, verify Normalize has EXACTLY ONE inbound connection** (from PreNormalize). A leftover direct wire from the pre-10b topology — Feeds error is the easy one to miss — makes Normalize fire early on that wire's tiny delivery, and the resulting skeleton lineage sprints to the output stage and can hard-fail the run before the real 30k-item delivery is ever processed (observed live: 2-second post-PreNormalize sprint, Normalize showing only the warnings sentinel, run dead at WriteDigest).

Why an explicit Merge and not five wires into Normalize's single port: **observed on this instance (first build, 2026-07-20)** — direct wiring executed Normalize once per inbound delivery (three partial pipelines in one run, each dragging the full downstream chain, ending in the empty-lineage null-body 400 at Summarise). The Merge delivers ONE combined stream so Normalize executes exactly once — same rule as FeedTasks (6b), PreBody (15b), and Rejoin (18). Two notes:
- **The loops send `done`, never `loop`.** `loop` stays *inside* the loop driving the fetcher; `done` fires once at the end carrying the accumulated articles. Wiring off `loop` feeds task items instead of articles.
- **A legitimately-empty input** (no feed errors; a stalled-then-fixed channel) should settle on modern n8n; if the run instead hangs at PreNormalize, apply the §5.7 branch-keeper row.

**11 · Code "Normalize"** (Run Once for All Items) — **from PreNormalize (10b)**. Unify, canonicalize, in-run title dedupe, collect warnings. Classification is **by item shape, never by pairing** — pairing metadata does not survive the 10b Merge (learned live: the pairing-based version silently dropped an entire 30k-item run). GParse/BParse items carry `ch`; FMP items carry `symbol`+`publishedDate`; anything with `title` + a link-like field is an RSS article, split gn-vs-feed by hostname, outlet labels/bypass/body flags recovered via a feed-URL hostname map. Unclassifiable or bad-URL items are counted and surfaced in the sentinel as `normalize:dropped:N keys:…` — a drop names its own shape in the brief's warning list instead of vanishing:

```javascript
const plan = $('Plan').all();
const out = [], warn = [], seen = new Set();
let dropped = 0, sample = null, stale = 0;
const cfg0 = (plan[0] && plan[0].json && plan[0].json.cfg) || {};
const maxAgeMs = (cfg0.max_age_d || 3) * 86400000;
const pwIds = new Set(cfg0.body_exempt || []);        // paywall detection: feed-row ids + URL domains
const pwDoms = cfg0.paywall_domains || [];
// no `new URL()` anywhere — the URL global does not exist in this n8n Code sandbox (discovered live: every
// URL "failed" parsing and the run zeroed; canon/hostOf are pure regex for that reason — keep them that way)
const canon = u => { let s = String(u || '').trim();
  if (!/^https?:\/\//i.test(s)) return null;
  s = s.split('#')[0]
       .replace(/([?&])(utm_source|utm_medium|utm_campaign|utm_term|utm_content|fbclid|gclid)=[^&]*/gi, '$1')
       .replace(/\?&/, '?').replace(/&&+/g, '&').replace(/[?&]+$/, '');
  return s; };
const hostOf = u => { const m = String(u || '').match(/^https?:\/\/([^\/?#]+)/i);
  return m ? m[1].toLowerCase().replace(/^www\./, '').replace(/:\d+$/, '') : ''; };
const tkey = t => String(t||'').replace(/\s+[-–—|]\s+[^-–—|]{2,40}$/,'').toLowerCase().replace(/[^a-z0-9 ]/g,'').split(/\s+/).filter(w=>w.length>3).sort().slice(0,8).join(' ');   // strips trailing " - Publisher" so GN variants of one headline share a key
// outlet-task lookup by BASE domain (feeds.arstechnica.com → arstechnica.com; digitimes.com.tw kept whole) —
// labels/bypass/body flags survive without item pairing, and subdomain-hosted feeds still match
const bd = h => { const seg = String(h).split('.'); if (seg.length <= 2) return h;
  const sld = seg[seg.length-2] + '.' + seg[seg.length-1];
  return /^(co|com|net|org|ac|gov|or)\.[a-z]{2}$/.test(sld) ? seg.slice(-3).join('.') : seg.slice(-2).join('.'); };
const hostTask = {};
for (const pl of plan) { const t = pl.json; if (t.ch !== 'feed') continue;
  const h = hostOf(t.url); if (h) hostTask[bd(h)] = t; }
const chCount = { feed:0, gn:0, gdelt:0, brave:0, fmp:0 };

for (const it of $input.all()) {
  const j = it.json || {};
  if (Object.keys(j).length === 0) continue;                       // AOD placeholders from empty loop iterations
  // 1) GParse/BParse items arrive pre-tagged
  if (j.ch && j.url && j.title) { add(j.title, j.url, j.snippet, j.published, j.source, j); continue; }
  // 2) error items (Feeds error lane / FMP failure)
  if (j.error) { const em = typeof j.error === 'string' ? j.error : (j.error && (j.error.message || j.error.description)) || '?';
    warn.push(`src fail: ${String(em).slice(0,80)}`); continue; }
  // 3) FMP articles (HTTP node splits the response array into items; whole-array kept as fallback)
  if (Array.isArray(j)) { for (const a of j) if (a && a.url) add(a.title, a.url, a.text || '', a.publishedDate || '', a.site || '', {ch:'fmp', feedId:'fmp', cluster:'ticker', bypass:false, fetchBody:true, sym:a.symbol}); continue; }
  if (j.symbol && j.publishedDate && j.url) { add(j.title, j.url, j.text || '', j.publishedDate, j.site || '', {ch:'fmp', feedId:'fmp', cluster:'ticker', bypass:false, fetchBody:true, sym:j.symbol}); continue; }
  // 4) RSS articles (feed + gn) — classified by SHAPE
  let link = j.link || j.url || (typeof j.guid === 'string' && j.guid.startsWith('http') ? j.guid : '');
  if (link && typeof link === 'object') link = link.href || '';
  if (j.title && link) {
    const host = hostOf(link);
    const isGN = /news\.google\./.test(host);
    const t = !isGN ? (hostTask[bd(host)] || null) : null;
    add(j.title, link, j.contentSnippet || j.snippet || '', j.isoDate || j.pubDate || '', j.creator || (t && t.id) || host || 'rss',
      { ch: isGN ? 'gn' : 'feed', feedId: (t && t.id) || (isGN ? 'gn' : host || 'feed'),
        cluster: (t && t.cluster) || 'thematic', bypass: !!(t && t.bypass), fetchBody: t ? !!t.body : !isGN });
    continue;
  }
  dropped++; if (!sample) sample = 'keys:' + (Object.keys(j).slice(0,12).join(',') || 'EMPTY');
}
if (dropped) warn.push(`normalize:dropped:${dropped} ${sample || ''}`);
function add(title, url, snippet, published, source, meta) {
  const cu = canon(url); if (!cu) { dropped++; if (!sample) sample = 'badurl:' + String(url).slice(0,60); return; }
  if (published) { const ts = Date.parse(String(published));           // age gate — provably-old items drop, undated/unparseable stay (fail-open)
    if (!isNaN(ts) && (Date.now() - ts) > maxAgeMs) { stale++; return; } }
  const tk = tkey(title); if (tk && seen.has(tk)) return; if (tk) seen.add(tk);
  const ah = hostOf(cu);
  const pw = pwIds.has(meta.feedId) || pwDoms.some(d => ah === d || ah.endsWith('.' + d));
  chCount[meta.ch] = (chCount[meta.ch] || 0) + 1;
  out.push({ json: { title:String(title||'').slice(0,300), curl:cu, snippet:String(snippet||'').slice(0,500),
    published, source, ch:meta.ch, feedId:meta.feedId, cluster:meta.cluster,
    bypass:!!meta.bypass, pw, fetchBody:!!meta.fetchBody && !pw } });
}
out.push({ json: { _warnings: warn, _seen: out.length, _ch: chCount, _stale: stale, curl: 'internal:warnings:' + Math.random() } });
return out;
```

Label-fidelity note: outlet rows whose feed URL host differs from their article host (feedburner-style) miss the hostname map and degrade to generic `feed` labels — they lose `bypass`/`body_exempt` handling (get triaged and body-fetched like any article) but are never dropped. GN articles are recognised by their `news.google.*` links.

**12 · Code "Dedupe"** (Run Once for All Items) — cross-execution URL dedup in a **TTL-bounded static-data store** (replaces n8n's Remove Duplicates node, whose count-capped history grows without eviction and throws "exceeded cap" — Google News redirect URLs churn every fetch, so the old store ballooned by ~10k throwaway keys per run and overflowed 50k in a few runs). This version is bounded by *time*, not count: it forgets any URL older than `max_age_d + 2` days every run, so it physically cannot overflow and needs no manual clearing.
```javascript
const cfg = $('Plan').first().json.cfg;
const store = $getWorkflowStaticData('global');
const seen = store.seenUrls || (store.seenUrls = {});
const now = Date.now();
const ttl = (cfg.dedup_ttl_d || 3) * 86400000;   // "non-repeats past N days" — registry knob, default 3; keep it small (static data reloads every run — do NOT set 30)
for (const k in seen) if (now - seen[k] > ttl) delete seen[k];   // TTL eviction — the whole point
const out = [];
for (const it of $input.all()) {
  const j = it.json || {};
  if (j._warnings) { out.push(it); continue; }        // sentinel always passes, never stored
  const k = j.curl; if (!k) { out.push(it); continue; }
  if (seen[k]) continue;                                // seen within TTL → drop exact-URL re-processing
  seen[k] = now; out.push(it);
}
return out;
```
Notes: `$getWorkflowStaticData` is sandbox-available (unlike `new URL`); the store persists across *scheduled* runs and stays bounded at `dedup_ttl_d` days of URLs (self-pruning). This node only stops **exact-URL re-processing** from the stable channels (feed/GDELT/Brave/FMP) — it does NOT deduplicate *stories*. Cross-run and semantic same-story dedup belong to the embeddings SemCluster (15e), not here (see §12 2026-07-23 changelog). Hard-reset: `$getWorkflowStaticData('global').seenUrls = {}`.

**13 · Code "TriagePrep"** (Run Once for All Items) — bypass rows skip scoring; the rest chunk into 120-item batches:

```javascript
const cfg = $('Plan').first().json.cfg;
const sub = (t,m)=>Object.entries(m).reduce((s,[k,v])=>s.split(k).join(v ?? ''), t);
const all = $input.all().map(i=>i.json);
// warnings sentinel passes through with the post-dedupe count stamped; bypass rows auto-admit
const out = all.filter(j=>j._warnings || j.bypass).map(j=>({json: j._warnings ? {...j, _new: all.length-1} : {...j, s:null, admitted:true}}));
const score = all.filter(j=>!j._warnings && !j.bypass);
for (let i=0;i<score.length;i+=120) {
  const chunk = score.slice(i,i+120);
  const payload = JSON.stringify(chunk.map((j,k)=>({i:k, t:j.title, src:j.source||j.feedId, pw:j.pw?1:0, sn:(j.snippet||'').slice(0,180)})));
  out.push({ json: { _batch: chunk, _llm_body: {
    model: cfg.triage_model, max_tokens: 8000,
    messages: [{ role: 'user', content: sub(cfg.triage_prompt,
      {'{tickers}':cfg.tickers, '{themes}':cfg.themes, '{items}':payload}) }] } } });
}
if (score.length === 0) out.push({ json: { _batch: [], _llm_body: null } });  // keep the Triage→Admit branch alive on all-bypass days — a starved PreBody input stalls the Merge
return out;
```

> **Design note — nothing to build in this box.** The three LLM calls (Triage 14a · Rescore 17.5 · Summarise 18d) share one contract. (1) The request body is **built as a plain object in the preceding Code node** (cards 13, 17.4, 18c each set `_llm_body`); the HTTP node only stringifies it via the card-14a Expression paste, identical on all three — never assemble JSON by string-templating, because a quote character in any headline would produce invalid JSON. (2) **No `temperature` on any call**: Opus-family models reject sampling parameters with a 400, which On-Error-Continue would swallow into a silent headline-only digest; omitting it everywhere keeps every §2.4 model cell freely swappable. **Adaptive thinking rides on Rescore and Summarise** (`thinking: { type: 'adaptive' }` — a reasoning control, not a sampling param; valid on Opus 4.8 and Sonnet 5, and the parsers already filter to `text` blocks so thinking blocks pass through harmlessly); Triage stays plain — it's the volume stage. (3) **Models come from the registry** (§2.4) via Plan's `cfg` — currently triage `claude-sonnet-5`, rescore + digest `claude-opus-4-8`; de-escalation levers in §2.4 and the §5.5f audit. (4) **Prompts come from the registry too** — `## Outlet Feeds → ### Prompts` `####` blocks, parsed by Plan into `cfg` with runtime token substitution (`{tickers}` `{themes}` `{items}`); a block missing its required token reverts to the card-5 `DEF_P` fallback. Edit prompts in Obsidian, never in the Code nodes. (The old Cluster call at 18b was deleted 2026-07-23 — semantic dedup moved to the embeddings layer, cards 15c–15e.)

**14 · IF "IsBatch"** — one condition · Value 1 → Expression (Boolean · **is true**):
```
{{ $json._batch !== undefined }}
```
true → card 14a · **false → card 15b input 2** (bypass rows and the warnings sentinel head for the body gate: `triage: no` sources with `fetchBody` get real bodies, scores, and summaries instead of riding headline-only; the sentinel fails the card-16 condition and flows through to Rejoin).

**14a · HTTP "Triage"** — the template LLM node; build it once, then copy-paste for 17.5/18d:
- **Method `POST`** (change from n8n's GET default — Anthropic is POST-only; GET returns 405 Method Not Allowed)
- **URL** `https://api.anthropic.com/v1/messages`
- **Credential:** Anthropic Header Auth (supplies `x-api-key` automatically — never add it by hand)
- **Header:** Send Headers ON → Add Parameter → **Name** `anthropic-version` · **Value** `2023-06-01` (both plain strings, no Expression)
- **On Error: Continue**
- **Body:** Send Body ON → Body Content Type `JSON` → Specify Body **`Using JSON`** (if you see Name/Value fields here, you're in `Using Fields Below` — switch it; the correct mode shows ONE unnamed JSON field) → toggle that JSON field to **Expression** → paste:
```
{{ JSON.stringify($json._llm_body) }}
```
Prompt and model live in card 13's `_llm_body` — this field never changes across the three LLM nodes. All three are **POST** with this identical body Expression; the fastest build is to finish this node, then copy-paste it for Rescore (17.5) / Summarise (18d) and swap nothing inside — the differing payload comes from each one's preceding Code node. (The Voyage `Embed` node at 15d is built separately per card 15d, not from this template.) **Wire Triage's output → card 15 (Admit).**

**15 · Code "Admit"** (Run Once for All Items) — **input: wired from card 14a "Triage"** (the only wire in; Triage is Admit's sole upstream node). **Settings → Always Output Data ON** (a zero-admission day must still deliver an empty item to PreBody, or the Merge stalls; the empty `{}` item is filtered out downstream). Parse scores, flatten batches, gate at `triage_min`. ⚠ The lookup filters TriagePrep's output to `_batch` items first — `pairedItem.item` indexes Triage's *input* stream (batches only), while `$('TriagePrep').all()` is the mixed output (bypass + sentinel first); indexing it raw would offset every lookup and silently admit nothing:

```javascript
const cfg = $('Plan').first().json.cfg;
const preps = $('TriagePrep').all().map(x=>x.json).filter(x=>x._batch);
const out = [];
$input.all().forEach((it, idx) => {
  const j = it.json;
  const batch = preps[it.pairedItem?.item ?? idx]?._batch || [];
  let scores = {};
  try { const txt = (j.content||[]).filter(b=>b.type==='text').map(b=>b.text).join('');
    for (const r of JSON.parse(txt.match(/\[[\s\S]*\]/)[0])) scores[r.i] = r.s; } catch(e) {}
  batch.forEach((b,k) => { const s = scores[k] ?? 0;
    const min = b.pw ? (cfg.triage_min_pw ?? 9) : cfg.triage_min;   // paywalled items clear a higher bar
    if (s >= min) out.push({ json: {...b, s, admitted:true} }); });
});
return out;
```

**How Admit is structured** — it zips two parallel streams, then gates. This is the pattern to hold in your head while reading the code:

| Stream | Source | Holds |
|---|---|---|
| `preps` | card 13 TriagePrep, `.filter(x=>x._batch)` | the ≤120-item batches, in the order they were sent to score |
| `$input.all()` | the wire from card 14a Triage | one LLM response per batch, in the **same** order |

1. **Re-pair each response to its batch** — `preps[it.pairedItem?.item ?? idx]`: `pairedItem.item` is n8n's record of which input item produced this response, so it fetches that batch's original articles (positional `idx` is the fallback if pairing metadata is dropped).
2. **Parse the scores** — the response's `content` is Anthropic's block format; join the text blocks, regex out the `[{"i":0,"s":7},…]` array, build `scores` keyed by the in-batch index `i`.
3. **Gate at the threshold** — for each article `b` at position `k`, read `scores[k]` (default `0` if the model skipped it) and admit only when `s >= cfg.triage_min`, stamping `s` and `admitted:true`.
4. **Output = admitted articles only** — everything below `triage_min` is dropped here; a zero-admission day emits nothing, which is exactly why **Always Output Data ON** supplies the empty keep-alive item for PreBody.

The ⚠ above is the one place this structure breaks silently: the two streams are indexed differently — `pairedItem.item` counts only the batches fed *into* Triage, but `$('TriagePrep').all()` also carries the bypass + sentinel items it emitted first, so without the `.filter(x=>x._batch)` every score maps to the wrong article and nothing clears the gate.

**15b · Merge "PreBody"** — Mode: Append, 2 inputs: Admit (scored stream) → Input 1 · 14-false (bypass + warnings sentinel) → Input 2. An explicit Merge — not two wires into card 16's single port — guarantees the body gate executes exactly once regardless of n8n's branch-convergence semantics; two wires into one port can execute the downstream chain once per branch → two digests per run.

**15c · Code "EmbedPrep"** (Run Once for All Items) — **from PreBody (15b)** · **→ Embed (15d)**. ⬥ NEW (2026-07-23 — embeddings dedup layer). Builds ONE Voyage request: the admitted + bypass items (each as `title. snippet`) followed by the last `story_memory_days` of prior briefed stories (embedded in the *same* call so cross-run repeats are caught for free). The warnings sentinel and the empty keep-alive item are set aside on `_sentinel` and re-emitted by SemCluster — they are never embedded.

```javascript
const cfg = $('Plan').first().json.cfg;
const all = $input.all().map(i=>i.json);
const sentinel = all.find(j=>j._warnings) || null;
const items = all.filter(j=>!j._warnings && j.title && j.curl);   // admitted + bypass real stories (drops empty keep-alive)
const cap = cfg.embed_max_chars || 1000;
const etext = (t,s) => ((String(t||'') + '. ' + String(s||'')).replace(/\s+/g,' ').trim().slice(0,cap)) || 'untitled';
const texts = items.map(j => etext(j.title, j.snippet));
// PRIOR briefed stories (card 2b run logs) — embedded in the SAME call for cross-run repeat detection
const memDays = cfg.story_memory_days ?? 7;
const cutoff = new Date(Date.now() - memDays*86400000).toISOString().slice(0,10);
const prior = [];
((($('PriorStories').first() || {}).json || {}).stdout || '').split('@@@').forEach(seg => {
  try { const run = JSON.parse(seg.trim());
    if (run.date >= cutoff) for (const s of (run.stories||[])) prior.push({ t:s.title, sum:(s.sum||'').slice(0,150) });
  } catch(e) {}
});
const priorList = prior.slice(0,250);
const priorTexts = priorList.map(p => etext(p.t, p.sum));
const input = texts.concat(priorTexts);
return [{ json: {
  _items: items, _priorList: priorList, _nNew: items.length, _sentinel: sentinel,
  _emb_body: input.length ? { model: cfg.embed_model || 'voyage-4-lite', input_type: 'document', input } : null
} }];
```

**15d · HTTP "Embed"** — **from EmbedPrep (15c)** · **→ SemCluster (15e)**. The embeddings call — same build pattern as the Anthropic nodes, but the Voyage credential and no version header:
- Method **POST** · URL `https://api.voyageai.com/v1/embeddings`
- **Credential:** Generic Credential Type → **Header Auth → Voyage** (§5.2 — supplies `Authorization: Bearer …` automatically; do **not** add it by hand)
- **Send Headers OFF** — Voyage needs no `anthropic-version` header; n8n sets `content-type: application/json` automatically for a JSON body
- **On Error: Continue** (a Voyage failure degrades to *no dedup* — SemCluster passes every item through as a singleton — never kills the run)
- **Body** — Send Body ON → Body Content Type **JSON** → Specify Body **Using JSON** → toggle to **Expression** → paste:
```
{{ JSON.stringify($json._emb_body) }}
```

**15e · Code "SemCluster"** (Run Once for All Items) — **from Embed (15d)** · **→ Body? (16)**. ⬥ NEW. Reads the Voyage vectors and does the whole semantic job the old Opus cluster call did — but deterministically and pre-body: (1) cosine-clusters same-story admitted items into ONE representative each (`sim_threshold`), preserving every source link on `_members`; (2) diverts NEW items that echo a prior briefed story (`repeat_threshold` OR exact title-key) to the ♻ follow-ups list; (3) picks each cluster's representative as the best body-fetchable, non-paywalled, highest-triage-scored member — so only representatives flow into the body pipeline. Self-reports `semcluster: N admitted → M stories (K repeats)` into the funnel. **Embeddings failure = graceful pass-through** (every item becomes its own story, no dedup that run).

```javascript
const cfg = $('Plan').first().json.cfg;
const prep = $('EmbedPrep').first().json;
const items = prep._items || [];
const priorList = prep._priorList || [];
const nNew = prep._nNew || 0;
const simT = cfg.sim_threshold || 0.86;
const repT = cfg.repeat_threshold || 0.88;
const base = prep._sentinel ? {...prep._sentinel} : { _warnings: [], curl: 'internal:warnings:0' };
const emit = (reps, followups, note) => {
  const out = reps.map(r => ({ json: r }));
  base._warnings = (base._warnings || []).concat(note);
  base._stats = { seen: base._seen ?? null, fresh: base._new ?? null, admitted: nNew, ch: base._ch || null, stale: base._stale ?? 0 };
  base._followups = followups;
  out.push({ json: base });
  return out;
};
// pull embeddings from the Voyage response (ordered by index)
let vecs = null;
try { const data = ($input.first().json.data) || []; vecs = data.slice().sort((a,b)=>a.index-b.index).map(d=>d.embedding); } catch(e) {}
// nothing to cluster / embed failed → pass items through as singletons (never drop, never crash the run)
if (nNew === 0) return emit([], [], 'semcluster: 0 admitted → 0 stories');
if (!vecs || vecs.length < nNew) {
  const reps = items.map(j => ({ ...j, _members:[{title:j.title,curl:j.curl,source:j.source,feedId:j.feedId,ch:j.ch}], _clusterSize:1 }));
  return emit(reps, [], `semcluster:embed-failed → no dedup this run (${items.length} singletons)`);
}
const norm = v => { let n=0; for (const x of v) n += x*x; n = Math.sqrt(n) || 1; return v.map(x=>x/n); };
const nv = vecs.slice(0, nNew).map(norm), pv = vecs.slice(nNew).map(norm);
const cos = (a,b) => { let d=0; for (let i=0;i<a.length;i++) d += a[i]*b[i]; return d; };
const tkey = t => String(t||'').replace(/\s+[-–—|]\s+[^-–—|]{2,40}$/,'').toLowerCase().replace(/[^a-z0-9 ]/g,'').split(/\s+/).filter(w=>w.length>3).sort().slice(0,8).join(' ');
const priorKeys = new Map(priorList.map(p=>[tkey(p.t), p.t]).filter(([k])=>k));
// cross-run repeat: NEW item echoes a PRIOR briefed story (title-key OR cosine)
const repeatOf = new Array(nNew).fill(null);
for (let i=0;i<nNew;i++) {
  const k = tkey(items[i].title);
  if (k && priorKeys.has(k)) { repeatOf[i] = priorKeys.get(k); continue; }
  let best=-1, bi=-1;
  for (let j=0;j<pv.length;j++){ const c = cos(nv[i], pv[j]); if (c>best){ best=c; bi=j; } }
  if (best >= repT && bi>=0) repeatOf[i] = priorList[bi].t;
}
// union-find same-story among NEW non-repeat items
const par = items.map((_,i)=>i); const find = x => par[x]===x ? x : (par[x]=find(par[x]));
for (let i=0;i<nNew;i++){ if (repeatOf[i]) continue;
  for (let j=i+1;j<nNew;j++){ if (repeatOf[j]) continue; if (cos(nv[i], nv[j]) >= simT) par[find(j)] = find(i); } }
const comp = {};
for (let i=0;i<nNew;i++){ if (repeatOf[i]) continue; (comp[find(i)] = comp[find(i)] || []).push(i); }
const fin = j => (j.s2 != null) ? j.s2 : (j.s != null ? j.s : null);
const reps = [];
for (const idxs of Object.values(comp)) {
  const mem = idxs.map(n=>items[n]);
  const best = [...mem].sort((a,b)=> ((b.fetchBody?1:0)-(a.fetchBody?1:0)) || ((a.pw?1:0)-(b.pw?1:0)) || ((fin(b)??0)-(fin(a)??0)) )[0];
  reps.push({ ...best, _members: mem.map(m=>({title:m.title,curl:m.curl,source:m.source,feedId:m.feedId,ch:m.ch})), _clusterSize: mem.length });
}
const followups = [];
for (let i=0;i<nNew;i++) if (repeatOf[i]) followups.push({ title:items[i].title, curl:items[i].curl, source:items[i].source||items[i].feedId, prior:repeatOf[i] });
return emit(reps, followups, `semcluster: ${nNew} admitted → ${reps.length} stories (${followups.length} cross-run repeats)`);
```

**16 · IF "Body?"** (from SemCluster (15e)) — one condition · Value 1 → Expression (Boolean · **is true**):
```
{{ $json.fetchBody === true }}
```
true → card 17 · false → card 18 (Merge input 1; carries no-body representatives, headline-only bypass rows, and the warnings sentinel). ⬥ Only representatives reach this gate now — same-story duplicates were folded into `_members` upstream and never get body-fetched or rescored.

**17 · Body chain** — the article-body pipeline: fetch full text for every `fetchBody` item, then let Opus re-score with the body in hand. Same loop pattern as cards 8/9. **Four nodes:**

**17.1 · Loop Over Items "BodyLoop"** — Batch Size `1` · from card 16's **true** output. Two outputs: **`loop`** feeds the fetch chain; **`done`** → RescorePrep (17.4).

**17.2 · Execute Command "Defuddle"** — from BodyLoop's **`loop`** output. Command → toggle to **Expression** → paste:
```
defuddle parse '{{ $json.curl.replace(/'/g, "") }}' --markdown
```
**On Error: Continue** (a paywalled or dead page yields empty stdout; Body1 downgrades it to headline-only rather than killing the run).

**17.3 · Code "Body1"** — from Defuddle:
```javascript
const t = $('BodyLoop').first().json;
const txt = ($json.stdout || '').trim();
return [{ json: { ...t, bodyOk: txt.length > 400, bodyText: txt.slice(0, 60000) } }];
```
Wire Body1's output **back into BodyLoop's input** to advance the loop (same back-wire as cards 8/9 — no Wait node here; defuddle is local, nothing to rate-limit).

**17.4 · Code "RescorePrep"** (Run Once for All Items) — from BodyLoop's **`done`** output. Emits `_batch` items ONLY, keeping the card-15 pairing rule; bypass items re-score here too, gaining real ranks:

```javascript
const cfg = $('Plan').first().json.cfg;
const sub = (t,m)=>Object.entries(m).reduce((s,[k,v])=>s.split(k).join(v ?? ''), t);
const items = $input.all().map(i=>i.json);
const out = [];
for (let i=0;i<items.length;i+=10) {
  const chunk = items.slice(i,i+10);
  const payload = JSON.stringify(chunk.map((j,k)=>({i:k, t:j.title, hs:j.s, pw:j.pw?1:0,
    x:(j.bodyOk ? j.bodyText : (j.snippet||'')).slice(0,6000)})));
  out.push({ json: { _batch: chunk, _llm_body: {
    model: cfg.rescore_model, max_tokens: 8000, thinking: { type: 'adaptive' },
    messages: [{ role: 'user', content: sub(cfg.rescore_prompt,
      {'{tickers}':cfg.tickers, '{themes}':cfg.themes, '{items}':payload}) }] } } });
}
return out;
```

**17.5 · HTTP "Rescore"** — **from RescorePrep (17.4)** · **→ Final (17.6)**. Same node shape as card 14a: POST `https://api.anthropic.com/v1/messages` · Anthropic Header Auth credential · header `anthropic-version: 2023-06-01` · On Error: Continue · Send Body ON → JSON → Expression → the identical paste as 14a, `{{ JSON.stringify($json._llm_body) }}`. This is the **body-informed re-score**: `rescore_model` (default `claude-opus-4-8`) reads each article's full text — the `x` excerpt RescorePrep packed from defuddle's output — and sets the final rank `s2`, correcting headline-only triage. A dull headline hiding a material disclosure gets upgraded; a punchy headline over thin content gets cut. ~40 items/day ≈ $10–15/mo.

**17.6 · Code "Final"** (Run Once for All Items) — **from Rescore (17.5)** · **→ Rejoin (18) input 2**. **Settings → Always Output Data ON** (same stall guard as Admit — a zero-body day must still feed the Merge). Zips the two streams exactly like Admit (card 15): `preps` = RescorePrep's batches (17.4, `_batch`-filtered) · `$input.all()` = Rescore's responses, paired by `pairedItem.item`; writes each article's new score to `s2` (`null` when the response can't be parsed):

```javascript
const preps = $('RescorePrep').all().map(x=>x.json).filter(x=>x._batch);
const out = [];
$input.all().forEach((it, idx) => {
  const j = it.json;
  const batch = preps[it.pairedItem?.item ?? idx]?._batch || [];
  let scores = {};
  try { const txt=(j.content||[]).filter(b=>b.type==='text').map(b=>b.text).join('');
    for (const r of JSON.parse(txt.match(/\[[\s\S]*\]/)[0])) scores[r.i]=r.s; } catch(e) {}
  batch.forEach((b,k)=> out.push({ json: {...b, s2: scores[k] ?? null} }));
});
return out;
```

**18 · Merge "Rejoin"** — Mode: Append. Reunites the two lanes the pipeline split at card 16 (Body?) back into one admitted-items stream.
- **Input 1 ← card 16 "false" output** — items that skipped the body pipeline: no-body admitted items, headline-only bypass rows, and the warnings sentinel.
- **Input 2 ← card 17.6 "Final"** — the body-pipeline stream, each item now carrying its `s2` body-informed re-score.
- **Output → card 18c "SumPrep"** — the single merged stream (every representative, body and no-body together, plus the sentinel carrying `_stats`/`_followups`). ⬥ Wires **straight to SumPrep** now — the old 18a ClusterPrep and 18b Cluster nodes are **deleted** (2026-07-23; clustering moved upstream to SemCluster 15e).

Append mode (not a keyed merge) because the two lanes hold *different* items, not two halves of the same item — Rejoin concatenates them. Like PreBody (15b), an explicit Merge here — not two wires into SumPrep's single port — keeps SumPrep executing once, not once per lane.

**18a "ClusterPrep" + 18b "Cluster" — DELETED (2026-07-23).** These two nodes were the Opus LLM cluster call. Clustering + cross-run repeat detection moved **upstream to SemCluster (15e)** on embeddings, so both are removed: **Rejoin (18) now wires straight to SumPrep (18c)**. In n8n: delete the `ClusterPrep` and `Cluster` nodes, then drag a wire from `Rejoin` to `SumPrep`. Rationale in §12 changelog — this is the whole cost fix (duplicates no longer reach the body pipeline; the Opus cluster call is gone). Old card kept in the `_Archive/Docs` snapshot for rollback.

**18c · Code "SumPrep"** (Run Once for All Items, **from Rejoin (18)**) — ⬥ REWRITTEN 2026-07-23. Clustering already ran upstream (SemCluster 15e), so this node no longer parses an LLM response — it reads Rejoin's representatives directly: splits any cross-run repeats to ♻ (carried on the sentinel's `_followups`), builds one summary payload per representative (8 stories/batch), and keeps the Jaccard union-find as a **cheap backstop** for any same-story pair the embeddings missed. Output shape is unchanged, so Summarise (18d) and Assemble (19) need no edits:

```javascript
const cfg = $('Plan').first().json.cfg;
const sub = (t,m)=>Object.entries(m).reduce((s,[k,v])=>s.split(k).join(v ?? ''), t);
const all = $input.all().map(i=>i.json);
const sentinel = all.find(j=>j._warnings) || {};
const reps = all.filter(j=>!j._warnings && (j.admitted || j.bypass) && j._members);
const followups = (sentinel._followups || []).slice();
const fin = j => (j.s2 != null) ? j.s2 : (j.s != null ? j.s : null);
// clustering already ran upstream (embeddings); Jaccard here is a cheap backstop for any same-story pair embeddings missed
const normT = t => String(t||'').replace(/\s+[-–—|]\s+[^-–—|]{2,40}$/,'').toLowerCase().replace(/[^a-z0-9 ]/g,' ').split(/\s+/).filter(w=>w.length>3);
const sets = reps.map(j=>new Set(normT(j.title)));
const par = reps.map((_,i)=>i); const find = x => par[x]===x ? x : (par[x]=find(par[x]));
for (let a=0;a<reps.length;a++) for (let b=a+1;b<reps.length;b++){ if (find(a)===find(b)) continue;
  const A=sets[a], B=sets[b]; if (A.size<3 || B.size<3) continue; let inter=0; for (const w of A) if (B.has(w)) inter++;
  if (inter/(A.size+B.size-inter) >= (cfg.merge_jaccard || 0.42)) par[find(b)] = find(a); }
const comp = {}; reps.forEach((_,n)=>{ (comp[find(n)] = comp[find(n)] || []).push(n); });
const cats = cfg.catalysts || {}, xr = cfg.x_read || {};
const stories = Object.values(comp).map(idxs => {
  const group = idxs.map(n=>reps[n]);
  const best = [...group].sort((a,b)=>((b.bodyOk?1:0)-(a.bodyOk?1:0)) || ((fin(b)??0)-(fin(a)??0)))[0];
  const members = group.flatMap(g=>g._members || []);
  const scores = group.map(fin).filter(s=>s!=null);
  const sTick = [...new Set(members.map(m=>(m.feedId||'').startsWith('tk-')?m.feedId.slice(3).toUpperCase():null).filter(Boolean))];
  const sig = sTick.map(t=>{ const c=(cats[t]||[])[0]; const x=xr[t];
    return (c||x) ? t+(c?` catalyst ${c.diff===0?'TODAY':(c.diff>0?'T-'+c.diff:'T+'+(-c.diff))}: ${c.ev}`:'')+(x?` | X ${x}`:'') : null;
  }).filter(Boolean).join('; ');
  return { members, title: best.title, cluster: best.cluster, sig,
    score: scores.length ? Math.max(...scores) : null, bodyOk: group.some(g=>g.bodyOk),
    x: [...group].sort((a,b)=>((b.bodyOk?1:0)-(a.bodyOk?1:0))).slice(0,2).map(m=>(m.bodyOk?m.bodyText:(m.snippet||'')).slice(0,4500)).join('\n---\n') };
});
const out = [];
for (let i=0;i<stories.length;i+=8) {
  const chunk = stories.slice(i,i+8);
  const payload = JSON.stringify(chunk.map((s,k)=>({i:k, t:s.title,
    srcs:[...new Set(s.members.map(m=>m.source||m.feedId))].join(', '), sig:s.sig||undefined, x:s.x.slice(0,9000)})));
  out.push({ json: { _batch: chunk.map(({x, ...rest})=>rest),
    _warnings: i===0 ? (sentinel._warnings||[]) : [], _stats: i===0 ? (sentinel._stats||null) : null,
    _followups: i===0 ? followups : null,
    _llm_body: { model: cfg.digest_model, max_tokens: 8000, thinking: { type: 'adaptive' },
      messages: [{ role: 'user', content: sub(cfg.digest_prompt,
        {'{tickers}':cfg.tickers, '{themes}':cfg.themes, '{context}': cfg.brief_context || 'none provided', '{items}':payload}) }] } } });
}
return out.length ? out : [{ json: { _batch: [], _warnings: sentinel._warnings||[], _stats: sentinel._stats||null, _followups: followups, _llm_body: null } }];
```

**18d · HTTP "Summarise"** — **from SumPrep (18c)** · **→ Assemble (19)**. ⬥ Same node shape as card 14a — build it identically:
- **Method `POST`** (change from GET — Anthropic is POST-only; GET → 405 Method Not Allowed)
- URL `https://api.anthropic.com/v1/messages`
- **Credential:** Anthropic Header Auth · **Header** Name `anthropic-version` Value `2023-06-01`
- **On Error: Continue** (an LLM failure — or the empty-run null body — degrades to headline-only digest lines, never kills the run)
- **Body** — Send Body ON → JSON → Using JSON → Expression → `{{ JSON.stringify($json._llm_body) }}`

`digest_model` defaults to `claude-opus-4-8` — the summary IS the product; `claude-sonnet-5` is the step-down cell.

**19 · Code "Assemble"** (Run Once for All Items, from Summarise) — ⬥ parse summaries; build the brief (**one entry per story, funnel header, thesis wikilinks on ticker stories, links to every source article**), the Telegram push, and a machine-readable story log for `.data/`:

```javascript
const cfg = $('Plan').first().json.cfg;
const stories = [], warn = [], fups = [];
let stats = null;
const preps = $('SumPrep').all().map(x=>x.json);   // SumPrep emits batch items only — indices align
$input.all().forEach((it, idx) => {
  const j = it.json;
  const src = preps[it.pairedItem?.item ?? idx] || {};
  warn.push(...(src._warnings||[]));
  if (src._stats) stats = src._stats;
  if (src._followups) fups.push(...src._followups);
  let sums = {};
  try { const txt=(j.content||[]).filter(b=>b.type==='text').map(b=>b.text).join('');
    for (const r of JSON.parse(txt.match(/\[[\s\S]*\]/)[0])) sums[r.i]=r.sum; } catch(e) {}
  (src._batch||[]).forEach((s,k)=> stories.push({...s, sum: sums[k] || null}));
});
const tf = cfg.ticker_files || {}, cats = cfg.catalysts || {}, xr = cfg.x_read || {};
const lock = new Set(cfg.body_exempt || []);   // paywalled/exempt rows → 🔒 on their source links
const tickersOf = s => [...new Set(s.members
  .map(m=>(m.feedId||'').startsWith('tk-') ? m.feedId.slice(3).toUpperCase() : null).filter(Boolean))];
const wl = ts => { const links = ts.map(t=>tf[t]).filter(Boolean).map(f=>`[[Theses/${f}]]`);
  return links.length ? ' → ' + links.join(' · ') : ''; };
const cat = ts => { const evs = ts.flatMap(t=>cats[t]||[]);
  return evs.length ? ' · ' + evs.slice(0,2).map(e=>`📅 ${e.diff===0?'TODAY':(e.diff>0?'T-'+e.diff:'T+'+(-e.diff))}: ${e.ev}`).join(' · ') : ''; };
const xm = (ts, score) => { const reads = ts.map(t=>xr[t]).filter(Boolean);
  if (reads.length) return ` · 𝕏 ${reads[0]}`;
  const us = ts.some(t=>/^[A-Z]{1,5}$/.test(t));   // only claim X-quiet for cashtag-tracked (US-listed) names
  return (Object.keys(xr).length && us && score !== null && score >= 8) ? ' · 𝕏 quiet' : ''; };
const now = new Date(); const p = n => String(n).padStart(2,'0');
const d = `${now.getFullYear()}-${p(now.getMonth()+1)}-${p(now.getDate())}`;
const hm = `${p(now.getHours())}${p(now.getMinutes())}`;
const by = {};
for (const s of stories) (by[s.cluster] = by[s.cluster] || []).push(s);
const nItems = stories.reduce((a,s)=>a+s.members.length,0);
let md = `---\ndate: ${d}\ntags: [meta, daily-intel]\norigin: n8n/news-sweep\n---\n\n# Daily intel — ${d} ${hm}\n\n`;
md += `Funnel: ${stats?.seen ?? '?'} fetched → ${stats?.fresh ?? '?'} new → ${stats?.admitted ?? nItems} admitted → ${stories.length} stories${fups.length ? ` (+${fups.length} follow-ups)` : ''}.`;
if (stats?.ch) md += `\nChannels: ${['feed','gn','gdelt','brave','fmp'].map(c=>`${c} ${stats.ch[c] ?? 0}`).join(' · ')}${stats?.stale ? ` · stale ${stats.stale}` : ''}`;
if (warn.length) md += `\n⚠ Source failures: ${warn.join(', ')}`;
md += '\n\n';
for (const cl of Object.keys(by).sort()) {
  md += `## ${cl}\n\n`;
  for (const s of by[cl].sort((a,b)=>(b.score??-1)-(a.score??-1))) {
    const ts = tickersOf(s);
    md += `- \`${s.score ?? '—'}\` **${s.title}**${wl(ts)}${cat(ts)}${xm(ts, s.score)}\n`;
    if (s.sum) md += `  ${s.sum}${s.bodyOk ? '' : ' *(headline only)*'}\n`;
    md += `  Sources: ${s.members.map(m=>`${lock.has(m.feedId)?'🔒 ':''}[${m.source||m.feedId}](${m.curl})`).join(' · ')}\n`;
  }
  md += '\n';
}
if (fups.length) {
  md += `## ♻ Follow-up coverage (already briefed — links only)\n\n`;
  for (const f of fups) md += `- [${f.source}](${f.curl}) — ${f.title}${f.prior ? ` *(prior: ${f.prior})*` : ''}\n`;
  md += '\n';
}
const out = [{ json: { type:'digest', fname:`${d} ${hm} - Daily intel - n8n.md`, content: md } }];
out.push({ json: { type:'log', fname:`${d}-${hm}.json`,
  content: JSON.stringify({ date: d, time: hm, stats, warnings: warn, stories, followups: fups }, null, 1) } });
// Telegram fan-out — top-N stories, one message each (tg_max_msgs cap), with a per-subject diversity cap so no single ticker/theme dominates the glance
const ranked = [...stories].sort((a,b)=>(b.score??-1)-(a.score??-1));
const nMsg = Math.max(1, Math.min(20, Math.round(cfg.tg_max_msgs ?? 10)));
const perSub = Math.max(1, Math.round(cfg.tg_per_subject ?? 2));
const subCnt = {}, picks = [];
for (const s of ranked) {
  if (picks.length >= nMsg) break;
  const ts = tickersOf(s); const sub = ts[0] || s.cluster || '?';   // subject = primary ticker, else cluster
  if ((subCnt[sub] || 0) >= perSub) continue;                        // diversity cap: skip once this subject has its quota
  subCnt[sub] = (subCnt[sub] || 0) + 1; picks.push(s);
}
if (picks.length) {
  picks.forEach((t, i) => {
    let tg = `★ ${t.title}`;
    if (t.sum) tg += `\n${t.sum}`;
    tg += `\n${t.members[0].curl}`;
    if (i === picks.length - 1) {                          // footer + failures ride the last message only
      tg += `\n— ${stories.length} stories in today's brief (Daily Intel)`;
      if (warn.length) tg += `\n⚠ ${warn.length} source failures`;
    }
    out.push({ json: { type:'tg', text: tg.slice(0,3900) } });
  });
} else {
  let tg = 'W3: quiet run — 0 stories admitted';
  if (warn.length) tg += `\n⚠ ${warn.length} source failures`;
  out.push({ json: { type:'tg', text: tg.slice(0,3900) } });
}
return out;
```

**20 · Switch "Out"** — ⬥ three lanes, same Switch pattern as card 6's Route. Rules on Value 1 → Expression:
```
{{ $json.type }}
```
String **is equal to**: `digest` → output 0 · `log` → output 1 · `tg` → output 2.

Each of the three outputs feeds its sink in **card 21**. No clip lane, no `_Inbox/` writes (Lane C reverted — §11).

**21 · Output sinks** — the three lanes end differently: `digest` and `log` each **write a file** (a **Convert to File → Read/Write Files** pair), `tg` **posts to Telegram**. Wire each Switch output to its sink below.

**21a · `digest` sink** — from Switch output 0 (`digest`):
- **Convert to File "ConvertDigest"** — Operation **Convert to Text File** · **Text Input Field** `content`. Emits the text as a binary in property `data`.
- **Read/Write Files from Disk "WriteDigest"** — Operation **Write File to Disk** · Input Binary Field `data` · File Path → Expression (by-name — Convert to File **strips the item's JSON on this instance** (confirmed first build), so `$json.fname` arrives empty and the path collapses to the bare directory → "path is a directory" error; the by-name form reaches past the Convert node to Assemble, where the JSON still exists):
```
/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').all()[0].json.fname }}
```

**21b · `log` sink** — from Switch output 1 (`log`): the same two-node pair, values identical to 21a:
- **Convert to File "ConvertLog"** — Operation **Convert to Text File** · **Text Input Field** `content` (not `data` — same source field as the digest lane) → binary property `data`.
- **Read/Write Files from Disk "WriteLog"** — Operation **Write File to Disk** · Input Binary Field `data` · File Path → Expression (`[1]` = Assemble's log item):
```
/Users/alexcohen/InvestmentVault/.data/news_stories/{{ $('Assemble').all()[1].json.fname }}
```
One dated JSON per run — the machine-readable newsflow corpus for `/retro` backtests; `.data/` is a sanctioned rule-1 location, gitignored, invisible to Obsidian Sync.

**21c · `tg` sink** — from Switch output 2 (`tg`): **Telegram "Notify"** — no file conversion (Telegram takes text directly) · Chat ID `1779654963` · Text → Expression below. Assemble emits **up to `tg_max_msgs` tg items** (top-N stories, rank order, one per item — the registry cap); the Telegram node sends **one message per input item**, so the fan-out needs no loop and no extra nodes. Full summary rides each message (per-message 3,900-char guard); the run footer + failure count ride the last message only.
```
{{ $json.text }}
```

**What "Convert to File — Text, source `content`" means.** "Text" is the node's **Convert to Text File** operation (as opposed to Convert to CSV/JSON/etc.); "source `content`" is its **Text Input Field** parameter — *which field of the incoming item holds the string to write*. Assemble (card 19) emits each file item as `{ type, fname, content }`, so `content` holds the finished output (the markdown brief for `digest`, the JSON log string for `log`) and `fname` holds the filename. Convert to File turns that `content` string into a **binary** (property `data`); the Read/Write node then writes that binary to disk. The `tg` lane skips this entirely — its item is `{ type, text }`, and Telegram consumes `text` as a string, no file needed. The write paths use the by-name `$('Assemble')` form rather than `$json.fname` because Convert to File drops the item's JSON during conversion (confirmed live) — `$json` is empty on the far side of it.

### 5.4 Wiring map

`1→2→2b→2c→2d→3→4→5→6` · **6:{0,1}→6b(Merge FeedTasks)→7** · 6:2→8(loop: Gdelt→GParse→Wait→loop) · 6:3→9(loop: Brave→BParse→Wait→loop) · 6:4→10 · **{7 main→in1, 7 error→in2, 8 done→in3, 9 done→in4, 10→in5}→10b(Merge PreNormalize)→11**→12→13→14 · 14-true→14a→15→15b(input 1) · **14-false→15b(input 2)** · **15b→15c(EmbedPrep)→15d(Embed HTTP, Voyage)→15e(SemCluster)→16** · 16-true→17(BodyLoop: Defuddle→Body1→loop; done→RescorePrep→Rescore→Final) · {16-false, 17-Final}→18→**18c(SumPrep)**→18d→19→20(Switch Out)→**21 sinks**{0:ConvertDigest→WriteDigest · 1:ConvertLog→WriteLog · 2:Notify}. ⬥ **18a ClusterPrep + 18b Cluster deleted 2026-07-23** — Rejoin (18) wires straight to SumPrep (18c); semantic dedup now runs at 15c–15e (embeddings) before the body pipeline. The 6b/10b Merges are mandatory, not optional: per-branch execution of multi-wire nodes was observed on this instance at first build (2026-07-20) — direct wiring runs Normalize (and the whole chain after it) once per delivery.

### 5.5 First run

**LLM-stage timing profile** (what "normal" looks like per node — durations scale with content volume, so incremental re-runs are legitimately fast): Triage = ceil(scored/120) calls, seconds-to-minutes · **Embed = ONE Voyage call** (~1–3s; SemCluster itself is pure JS, sub-second — a response with no `data` array = embed failed → pass-through singletons) · Body loop = one defuddle per **representative** (fewer than admitted now — duplicates collapsed upstream at 15e) · Rescore = ceil(bodyReps/10) calls at ~3–5s each (a 5s Rescore = one thin batch, normal on incremental runs) · Summarise = ceil(stories/8) calls, the slowest stage post-analytical-prompt. Fast stages on a small run are health, not failure — the funnel counts, not the clock, are the diagnostic. With adaptive thinking on Rescore/Summarise, expect those two stages to run 2–4× longer than the plain-call baselines above — reasoning tokens, not a hang.

**Run it:** Execute Workflow (a manual run never delays the schedule). Expect **~25–35 min** — channels run *sequentially* (n8n does one branch at a time): RSS first, then GDELT (the ~18-min dominant leg, 8s × ~119 targets), Brave, FMP; PreNormalize holds until all five deliver. Output: one brief in `Daily Intel/` + the Telegram fan-out.

**First-run checklist:**

- **(a) Admitted count** — tens, not hundreds. Hundreds → raise `triage_min`.
- **(b) Grounding** — spot-check 3 summaries: every fact must trace to the source text; `*(headline only)*` items are unverified by definition.
- **(c) Channels line** — all five non-zero on a weekday; a zero names the broken channel.
- **(d) Source failures** — the `⚠` list flags dead feeds to prune.
- **(e) Ticker matches** — cluster items resolve to the right company (wrong match = ambiguous thesis filename; add a distinguishing word).
- **(f) Triage-band audit** (calibration) — open `Admit` input, scan items scored 5–6 for anything material; real misses → lower `triage_min`.
- **(g) Loop output** — GdeltLoop `done` must be article-shaped (`title`/`url`), not tasks (same for BodyLoop).
- **(h) Write lanes** — dated brief in `Daily Intel/` AND dated JSON in `.data/news_stories/`.
- **(i) Funnel header** populated (`N fetched → M new`); blank = sentinel lost upstream.
- **(j) Exactly one** digest + Telegram + story log; duplicates = a multi-wire node ran per branch (verify 6b/10b Merges).
- **(k) Story memory** (day 2+) — SemCluster (15e) funnel note reads `… (K cross-run repeats)` with K matching the ♻ count; `PriorStories` (2b) stdout non-empty.
- **(m) Embeddings dedup** — SemCluster funnel note `semcluster: N admitted → M stories` with M < N on any day with duplicate coverage; `Embed` (15d) response is a `data` array of vectors (not an error).
- **(l) Context markers** — 📅 catalyst / 𝕏 sentiment tags appear where the data exists.

**Publish** (Active toggle) only after one clean run. First scheduled runs re-surface a few legacy items (fresh dedupe store, self-heals in a day); the first brief is large (GN backlog, one-time ~$5–10) — raise `triage_min` to 8 for run 1 if that bothers.

### 5.6 Cutover checklist (after ~5–7 clean scheduled runs)

1. n8n → Workflows → **deactivate legacy Workflow 3 v1** (toggle off — do not delete; it is the instant-fallback baseline, and §5.8 preserves its build).
2. If v1's optional Monday per-ticker trigger was built, it retires with it (the unified ticker channels supersede it on four engines, daily).
3. Rename this workflow to `Workflow 3 — News Sweep` and move its schedule 07:10 → 07:00 (v1's vacated morning slot).
4. Update §10 table (3 → Live unified) + decision-log entry.
5. `_watchers.md` needs no change — same rows, new consumer.

### 5.7 Troubleshooting

The Workflow-3 symptom → fix reference moved to **§12.1** at the document bottom (all troubleshooting consolidated there).

---

### 5.8 Legacy v1 (GN-only News Sweep · superseded by §5 · live until §5.6 cutover)

Legacy record. The unified Workflow 3 (§5) replaces this build entirely; rebuild v1 only as calibration-baseline insurance while the unified build shakes out — §5.6 deactivates it. Node name `Digest` is load-bearing if you split the tail differently; as wired below no by-name lookups are needed.

**1 · Schedule Trigger** — **two rules** (the node rejects multi-time cron like `0 7,17 * * *`): Rule 1 `Days`·`1`·`7am`·`0`; **Add Rule** → Rule 2 `Days`·`1`·`5pm`·`0`.

**2 · Read/Write Files from Disk** — Read · `/Users/alexcohen/InvestmentVault/_watchers.md`. **3 · Extract from File** — `Text`.

**4 · Code — rename `Queries`** — the §2.4 parser verbatim (emits one Google News search-as-RSS URL per active, unexpired `## News & Thematic` row; `paused` and past-`expires` rows drop out automatically — the whole lifecycle lives in the registry, never in this node).

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

**10 · Convert to File** — `Convert to Text File` · **Text Input Field** `content` → **11 · Read/Write Files from Disk** — Write · **File Path and Name** → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $json.fname }}` · **Input Binary Field** `data`. ⚠ This is the *decided* path; the deployed instance still writes `_Inbox/` — fix that one field rather than rebuilding (trail: §11).

**12 · Telegram** (second wire off `Digest`) — Chat ID `1779654963` · `{{ $json.text }}`.

**Wiring:** `1→2→3→4→5→6[→7→8]→9` · `9 → 10→11` and `9 → 12`.

**Optional Monday 08:00 per-ticker sweep** (§2.6 universe → one `"<Company>" stock` query per ticker → same downstream chain, weekly digest): superseded by the unified W3's daily four-engine ticker channels — do **not** build new; documented only because the deployed instance may carry it.

**Intent guard:** the digest is a scanning surface — you pick the 1–3 links worth a manual `/ingest`. Auto-ingesting news bodies wholesale is deliberately not built (Lane C auto-clips reverted — §11).

---

## 6. Workflow 4 — X Canary (+ shared X setup)

Daily provider-health probe for the X stack — 4 nodes, built first because it end-to-end tests credential → search → Telegram before the big workflow investment, then stays on as the canary (silent thin results → loud alert). §6.0–§6.3 are one-time setup shared with Workflow 5. Both **live** (§11 for dates).

### 6.0 Order of work & pre-flight

1. Accounts + credentials (§6.1) → 2. Verification calls — **the gate** (§6.2) → 3. Seed state + registry (§6.3) → 4. `Workflow 4 — X Canary` (§6.4, build first) → 5. `Workflow 5 — X Harvester` (§7.2–§7.3) → 6. First run + publish (§7.4) → 7. Two-week calibration (§7.5)

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

### 6.1 Accounts & credentials (~15 min)

**Step 1 — twitterapi.io account (browser):**

1. Go to `https://twitterapi.io` → **Sign up** (Google login is fine).
2. Open the dashboard — your **API key** (a long string) is displayed there. Keep the tab open.
3. Check for free trial credits (most new accounts get some). If present, **do not top up yet** — trial credits cover §6.2. If absent, top up the minimum (≤$5).
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
3. The second required header (`anthropic-version: 2023-06-01`) is NOT part of the credential — it is added per-request inside the HTTP node (§7.2 card 14).

**Key hygiene:** both keys now live only inside n8n credentials — never in chat, never in a vault file.

### 6.2 Verification calls (the gate — ~$0.50, ~30 min)

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
     - Name `query` · Value `$MRVL min_faves:100 since:<date ~7 days before your test day>` — plain text, no quotes
4. Open the node → **Execute step** → output appears on the right; flip between **Table** and **JSON** views to inspect.

**The five checks** (record pass/fail for each):

| # | Do | PASS when |
|---|---|---|
| 1 | Inspect every returned tweet's like count | all ≥ 100 — the server-side floor is honored, not theater |
| 2 | Delete ` min_faves:100` from the query → Execute step again | visibly MORE results — the floor genuinely prunes what you pay for. Restore the query after |
| 3 | Copy one tweet's `url` → open in browser → compare live likes vs the API number | within ±10% — snapshots are fine for thresholds, never for exact figures |
| 4 | Second HTTP node, same auth: URL `https://api.twitterapi.io/twitter/tweets` · query param `tweet_ids` = three ids from check 1, comma-separated → Execute step | all three return, each with engagement metrics — re-measurement depends on this endpoint |
| 5 | In BOTH nodes' outputs, find the view-count field | present, non-null, plausible (views ≥ likes) on essentially every tweet — every ratio gate depends on it |

**While in the JSON view, write down the exact field names** for: tweets array, id, url, text, like count, retweet count, view count, author handle, author followers. Expected: `tweets[]` · `id` · `url` · `text` · `likeCount` · `retweetCount` · `viewCount` · `author.userName` · `author.followers`. If any differ, `norm()` in Code X (§7.3) is the ONLY place they get fixed.

**Anthropic smoke test** — third HTTP node:

- **Method** `POST` · **URL** `https://api.anthropic.com/v1/messages`
- **Authentication**: Header Auth → `Anthropic`
- **Send Headers**: ON → Name `anthropic-version` · Value `2023-06-01`
- **Send Body**: ON → **Body Content Type** `JSON` → **Specify Body** `Using JSON` → paste:

```json
{"model":"claude-opus-4-8","max_tokens":256,"messages":[{"role":"user","content":"Reply with exactly: ok"}]}
```

- **Execute step** → PASS: response contains a `content` array with a text block saying `ok`.

**Decision:** all five pass → top up twitterapi.io to $5 (if still on trial credits) and proceed to §6.3. Any hard fail on 1–5 → repeat this section against the fallback twin **socialdata.tools** (different base URLs + its own credential, same checks) before abandoning. Delete the throwaway workflow when done.

### 6.3 Seed state + registry (~5 min)

**State file** — one paste in Terminal. It creates the folder if needed, seeds the DB with a 14-day calibration window from today, and prints the file back so you can verify in the same step:

```
mkdir -p "/Users/alexcohen/InvestmentVault/.data" && printf '{"meta":{"calibration_until":"%s","last_run":"","runs":0},"posts":{},"ratio_log":[]}' "$(date -v+14d +%F)" > "/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json" && cat "/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json"
```

Expected output: one JSON line ending in `"posts":{},"ratio_log":[]}` with `calibration_until` = today + 14 days. The file is disposable by design — delete it any time and the engine cold-starts.

**Sync note:** this file stays on this Mac only — `.data/` is gitignored (it already holds the FMP key; the ignore predates this build) and dot-folders are invisible to Obsidian Sync. Correct behavior: single-writer (§7.1), disposable, zero sync-conflict risk. The dashboard, digests, and registry are normal notes and sync/version as usual.

**Registry** — append the block below to [[_watchers.md]]: open it in Obsidian → scroll past the end of `## Alt-Data Pollers` → paste. (Or just ask Claude: *"append the §6.3 X Watchers block from n8n Automations.md to _watchers.md"*.)

````markdown
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
| prune_age_days | 28 | max observation age — raised from the 14 seed: longer trending window, ~2× re-measure reads |
| cap_tracked | 800 | working-set cap (§7.1) |
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

**Verify:** reopen `_watchers.md` in reading view — two tables (`Curated terms`, 5 rows; `Tuning`, 21 rows) plus the `### LLM prompt` fenced block render. Tuning values equal the code defaults, so the engine behaves identically with or without the paste — but only a pasted table is editable per §7.1.

### 6.4 Build cards (daily 08:00 · ~15 min)

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

---

## 7. Workflow 5 — X Harvester

The engine: daily 08:30 pull of every thesis cashtag + curated X terms, engagement-delta trending detection, Opus-graded sentiment/divergence, dated dashboard in `Daily Intel/`. **Live**, ~$17–40/mo all-in. Registry: `_watchers.md § X Watchers`. Official X API ruled out (cost + no server-side engagement operators) — provider is twitterapi.io.

### 7.1 Operating contracts (reference for the build cards)

**Sourcing — two channels, one union.** Channel A: cashtags auto-derived at runtime from `Theses/*.md` `ticker:` frontmatter, US-listed filter (`^[A-Z]{1,5}$`), OR-batched into clusters of 8, liquidity-tiered like-floors (`mega_tickers` Tuning row — a judgment list of high-chatter names, edited in one cell). New thesis → automatically watched next pull. Channel B: `### Curated terms` table in `_watchers.md § X Watchers` — foreign listings + thematic phrases cashtags can't express; same `status`/`expires` lifecycle as every registry table.

**Pull criteria — two-stage (server-side floor = cost control; client-side gates = quality control).** Every value is a `### Tuning` registry row, re-parsed each run; the Code nodes hold identical fallback defaults:

| Stage | Criterion | Seed value |
|---|---|---|
| Pull (server-side) | likes ≥ floor | 100 mega-tier · 30 std-tier/terms |
| Track (hard gates) | views ≥ 3,000 · followers ≥ 200 | ratios below these are noise / throwaway accounts |
| Track (any one admits) | like/view ≥ 1.5% · RT/view ≥ 0.5% · likes ≥ 300 | ratio lanes find dense posts; absolute lane keeps viral posts |
| Gem flag | like/view ≥ 3% or RT/view ≥ 0.7% | pre-consensus density — surface immediately |

Cadence: daily. `since_days` must stay ≥ cadence + 1.

**State — `.data/x_engagement_state.json`.** Single writer (this workflow only), machine-local (`.data/` gitignored, invisible to Obsidian Sync), disposable by design (loss = cold restart, sharp again in ~2 pulls). Schema:

```json
{
  "meta": { "calibration_until": "<seed date + 14d>", "last_run": "", "runs": 0 },
  "posts": { "<tweet_id>": {
      "url": "…", "author": "handle", "followers": 4300,
      "theme": "$MRVL", "text": "first 1000 chars…", "first_seen": "…",
      "obs": [["<iso>", 120, 14, 8200]],
      "flags": ["gem"], "plateau_count": 0 } },
  "ratio_log": [[0.031, 0.008]]
}
```

`obs` rows = `[timestamp, likes, RTs, views]`, one per pull — the time series that makes delta detection possible. Lifecycle: admit at entry gates → re-measure each pull → prune at age > `prune_age_days` (28) or `plateau_pulls` (2) consecutive flat pulls → pruned posts move to `state.archive` (retained `archive_days`, default 90; never re-measured). Working-set cap `cap_tracked` (800). Known limitation: at cap the code refuses new admissions — if hit in practice, add evict-oldest-plateaued-first.

**Trending engine.** Each pull batch-re-fetches every tracked post (50 ids/call — provider hard limit) and diffs against the previous observation. Each flag fires once per post (`flags[]` ledger):

| Signal | Condition (seed) | Delivery |
|---|---|---|
| `gem` | l/v ≥ 3% or RT/v ≥ 0.7% at entry | Pushed — Telegram + digest |
| `trending` | Δlikes ≥ 150/pull OR ≥ +60% growth (base ≥ 50) | Pushed — Telegram + digest |
| `divergence` | Non-null per-theme LLM divergence | Pushed — Telegram `⚠` lines |
| catalyst chatter | Theme ↔ `_catalyst.md` event ±10 days | Dashboard-only, never pushed |

Alert stream capped at 12 posts/pull. Digests are scanning surfaces — anything substantive goes through `/ingest` manually.

**Dashboard.** One dated snapshot per run — `Daily Intel/YYYY-MM-DD HHmm - X Dashboard.md`, written once, never rewritten; newest file = current dashboard, folder = permanent history. Sections: header stats + active-gates stamp + Seen→Admitted funnel · per-theme table (posts, Σ-likes meter, sentiment, score, trend sparkline) · ⚠ Thesis divergence · Crowd perspectives (with `[P#]`/`[A#]` citations) · catalyst chatter · flagged-this-pull. Layout rule: long text never in table cells.

**LLM layer — one Anthropic call per pull (node 14).** Inputs per theme: the six thesis analytical sections (Summary, Key Non-consensus Insights, Bull, Bear, Risks, OQ — shell-extracted; Bear/Risks context is what makes divergence *genuine*) + top `llm_top_n` tracked posts (1,000 chars + follower/like/view stats) + PRIOR READS (`state.sentiment_log`, ≤90d, ≤30 entries) + top-5 archived anchor posts. Output schema (field list pinned by structured outputs; analytical guidance editable in `_watchers.md § X Watchers → ### LLM prompt`):

| Field | Values |
|---|---|
| `summary` | 2–4 sentences — engagement-weighted crowd narrative |
| `sentiment` / `score` | bullish · bearish · mixed · quiet / −2…+2 |
| `shift` | movement vs prior reads (null if stable) |
| `perspectives` | 2–6 `{text, refs}` objects citing post labels |
| `divergence` | ONE synthesis per theme across all posts — a crowd argument the thesis doesn't carry; echo of a known risk → null |

Call shape: POST `/v1/messages` · model = `llm_model` Tuning row (default `claude-opus-4-8`) · `thinking: {type: "adaptive"}` · structured outputs · `max_tokens` 32000 · timeout 600s · On-Error-Continue → "LLM unavailable this pull", harvest unaffected. Boundary: **read-vault yes, write-vault no** — output lands only in the dashboard; a divergence flag is a prompt to investigate (`/stress-test`, `/ingest`), never written into a thesis.

**Catalyst matching.** Pure Code logic: parse `_catalyst.md` dated rows → filter ±10 days of pull → intersect with themes holding tracked posts → dashboard section. Degrades gracefully on a stale calendar (Workflow 2's staleness nag is the guard).

**Cost.** twitterapi.io ~$2–5/mo (top up ≤$5 at a time — provider-death stranding) + Anthropic ~$15–35/mo (Opus daily; `llm_model` row is the lever) ≈ **$17–40/mo**.

### 7.2 Build cards (~60–90 min)

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
| 14    | HTTP — `Sentiment` (from 13)               | POST `https://api.anthropic.com/v1/messages` · Header Auth `Anthropic` · add header `anthropic-version: 2023-06-01` · Body: JSON → Expression → `{{ JSON.stringify($json.llm_body) }}` · Timeout **600000** (Opus + thinking + long output) · On Error: Continue (regular output)                                                                                                                             |
| 15    | Code — `Assemble` (from 14)                | **Code D** — dashboard + digest                                                                                                                                                                                                                                                                                                                                    |
| 16→17 | Convert to File (`state_json`) → Write     | Path `/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json` — from **15 `Assemble`** (always runs; 14 continues on error), so the write carries the sentiment ledger                                                                                                                                                                                                                        |
| 18→19 | Convert to File (`dash_body`) → Write      | Path → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.dash_fname }}` — one dated file per run; newest = current dashboard                                                                                                                                                                                                |
| 20    | IF (from 15)                               | `{{ $json.text }}` · is not empty                                                                                                                                                                                                                                                                                                                                  |
| 20b   | IF — `If digest` (from 20-true)            | `{{ $json.fname }}` · is not empty — file gate (divergence-only pulls push Telegram but write no digest) |
| 20c   | Code — `XFanout` (from 20-true)            | expands `tg_msgs` array → one item per message (fan-out to 5–10 Telegram sends)                                                                                                                                                                                                                                                                                    |
| 21    | Telegram (from `XFanout`)                  | Chat `1779654963` · `{{ $json.text }}` — one message per input item                                                                                                                                                                                                                                                                                                |
| 22→23 | Convert to File (`body`) → Write (from 20b-true) | Path `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.fname }}` |                                                                                                                                                                                                |

> **Node names are load-bearing.** The Code nodes fetch other nodes' data by name: `$('Tickers')`, `$('Summaries')`, `$('Extract Watchers')`, `$('Extract State')`, `$('Extract Catalyst')`, `$('Analyze')`, `$('Assemble')`. Rename each node to the exact name in its card — one character off and the run dies with "Referenced node doesn't exist".

**Wiring map** (what connects to what):

- `1 → 2 → 2b → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10` — one straight chain. Deliberately NOT parallel: the chain exists to guarantee execution order for the by-name `$('…')` lookups (the Code nodes ignore what flows into them), and fanning 2/2b into 3 without a Merge would make n8n run everything downstream once per branch — a double harvest, double LLM call, duplicate alerts
- `10` output **remeasure** → `11a` · output **discover** → `11b`
- `11a` → `12` **Input 1** · `11b` → `12` **Input 2**
- `12 → 13 → 14 → 15`
- `16 → 17` (state save) hangs off **`15 Assemble`** — downstream of the LLM on purpose: the write must include the sentiment ledger, which only exists after the LLM answers. Safe because node 14 is On-Error-Continue, so `Assemble` (and therefore the state write) runs even when the LLM fails
- `15 → 18 → 19` (dashboard snapshot → `Daily Intel/`, one dated file per run) **and** `15 → 20` (IF)
- `20` **true** → `20c XFanout` → `21` (Telegram) **and** `20` **true** → `20b If digest` → **true** → `22 → 23` (digest file) · all **false** branches → nothing. Two gates because the two pushes have different conditions: Telegram fires on `text` (any push, including divergence-only) then fans out to N messages via 20c; the file writes only when `fname`/`body` exist (flagged posts present)

**Build cards** — top to bottom; any field not mentioned stays at default:

**1 · Schedule Trigger** — **Trigger Interval** `Days` · **Days Between Triggers** `1` · **Trigger at Hour** `8am` · **Trigger at Minute** `30` (daily is the live cadence; `3` days was the build-phase economy default).

**2 · Execute Command — rename `Tickers`** — n8n ≥2.0 hides Execute Command by default (v2 breaking change); if it's missing from the node panel, apply the one-time re-enable in §7.4's troubleshooting table, then return here. **Command**:

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

**9 · Code — rename `Plan`** — **Mode** `Run Once for All Items` · paste **Code P** per §7.3.

**10 · Switch** — the sorter: `Plan` emits a mixed stream (re-measure ID batches + discovery search URLs); the Switch reads each item's `mode` field and routes it to the right HTTP node.

1. Add **Switch** (connect from `Plan`) · **Mode**: leave `Rules`.
2. **Routing Rule 1** — the condition row is `[value] [is equal to] [value]`: left box → **Expression** → `{{ $json.mode }}` · middle dropdown stays `is equal to` (String) · right box → type `remeasure` (plain text, Fixed, no braces) · toggle **Rename Output** ON → `remeasure`.
3. **Add Routing Rule** → Rule 2: left box → Expression → `{{ $json.mode }}` · `is equal to` · right box `discover` · Rename Output → `discover`.
4. The node now shows two labeled output dots on its right edge — `remeasure` (→ card 11a) and `discover` (→ card 11b).
5. Sanity: **Execute step** → first run shows `remeasure: 0 items` (nothing tracked yet — correct) and `discover: ~15–20 items`.

**11a · HTTP Request — rename `Batch Lookup`** (connect from the **remeasure** output) — **Method** `GET` · **URL** → Expression → `https://api.twitterapi.io/twitter/tweets?tweet_ids={{ $json.ids }}` · **Authentication** → Header Auth → `TwitterAPI-io` · **Options → Add option → Batching** → Items per Batch `3` · Batch Interval (ms) `1000` · **Settings → On Error** `Continue (using regular output)`.

**11b · HTTP Request — rename `Search`** (connect from the **discover** output) — **Method** `GET` · **URL** → Expression → `{{ $json.url }}` · **Authentication** → Header Auth → `TwitterAPI-io` · **Options → Batching** `3` / `1000` · **Settings → On Error** `Continue (using regular output)`. *(v1 reads only the first result page per query — keeps cost fixed; if a cluster feels thin, raise its floor or split the cluster rather than paginating.)*

**12 · Merge** — **Mode** `Append` · **Number of Inputs** `2` · wire `Batch Lookup` → **Input 1**, `Search` → **Input 2**.

**13 · Code — rename `Analyze`** — **Mode** `Run Once for All Items` · paste **Code X** per §7.3.

**14 · HTTP Request — rename `Sentiment`** (connect from `Analyze`) — **Method** `POST` · **URL** `https://api.anthropic.com/v1/messages` · **Authentication** → Header Auth → `Anthropic` · **Send Headers** ON → Name `anthropic-version` · Value `2023-06-01` · **Send Body** ON → **Body Content Type** `JSON` → **Specify Body** `Using JSON` → JSON field → Expression → `{{ JSON.stringify($json.llm_body) }}` · **Options → Timeout** `600000` · **Settings → On Error** `Continue (using regular output)`.

**15 · Code — rename `Assemble`** (connect from `Sentiment`) — **Mode** `Run Once for All Items` · paste **Code D** per §7.3.

**16 · Convert to File** (drag a SECOND wire off `Assemble`) — **Operation** `Convert to Text File` · **Text Input Field**: type the field name `state_json` — the NAME of the field, not its contents. (Downstream of the LLM so the sentiment ledger is included; `Assemble` always runs because node 14 continues on error.)

**17 · Read/Write Files from Disk** (from 16) — **Operation** `Write File to Disk` · **File Path and Name** `/Users/alexcohen/InvestmentVault/.data/x_engagement_state.json` · **Input Binary Field** `data`.

**18 · Convert to File** (from `Assemble`) — **Operation** `Convert to Text File` · **Text Input Field** `dash_body`.

**19 · Read/Write Files from Disk** (from 18) — **Operation** `Write File to Disk` · **File Path and Name** → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.dash_fname }}` · **Input Binary Field** `data`. One dated file per run — no separate live file; the newest file in `Daily Intel/` IS the current dashboard (date-prefixed names sort chronologically).

**20 · If** — the push gate: `Assemble` ALWAYS outputs the dashboard, but only outputs `text` (Telegram) + `body` (digest) when something was flagged. This node asks "anything to push?" so quiet pulls end silently.

1. Add **If** — drag a SECOND wire off `Assemble`'s output dot (one output feeding many nodes is fine; only converging *inputs* need Merge).
2. Condition row: left box → **Expression** → `{{ $json.text }}` · comparator dropdown → **String → is not empty**. The right-hand box disappears — this operator needs no comparison value.
3. Two outputs: **true** (top) → two wires, to card 20c (`XFanout` → Telegram) and card 20b (`If digest`). **false** (bottom) → connect nothing — the silent exit.
4. Sanity: run #1 takes the false path (nothing flagged in calibration) — Telegram skipped = success. If the node complains about types on quiet pulls (`text` undefined), enable its looser type-validation option: undefined counts as empty → routes false.

**20b · If — rename `If digest`** (SECOND wire off card 20's **true**) — the file gate: a divergence-only pull carries Telegram `text` but no digest `body`; without this gate the Convert/Write pair hard-fails on the missing file and aborts the run. Condition: left box → **Expression** → `{{ $json.fname }}` · **String → is not empty**. **true** → card 22 · **false** → nothing.

**20c · Code — `XFanout`** (FIRST wire off card 20's **true**, feeding card 21) — **Run Once for All Items** — expands Assemble's `tg_msgs` array into one item per message so the Telegram node sends 5–10 separate messages (one per divergence + flagged post, `x_tg_max_msgs` cap) instead of a single wall of text. Falls back to the single `text` if `tg_msgs` is absent (older Assemble paste):
```javascript
const src = $('Assemble').first().json;
const msgs = (Array.isArray(src.tg_msgs) && src.tg_msgs.length) ? src.tg_msgs : (src.text ? [src.text] : []);
return msgs.map(m => ({ json: { text: String(m).slice(0, 3900) } }));
```

**21 · Telegram** (from `XFanout`) — existing credential · **Chat ID** `1779654963` · **Text** → Expression → `{{ $json.text }}`. Sends one message per input item (the fan-out) — Telegram's ~1 msg/s flood limit means ≤10 is safe; if 429s appear, lower `x_tg_max_msgs`.

**22 · Convert to File** (from `If digest` **true**) — **Operation** `Convert to Text File` · **Text Input Field** `body`. On Error stays at default (`Stop Workflow`) — behind the gate, an error here is real and should fail loud.

**23 · Read/Write Files from Disk** (from 22) — **Operation** `Write File to Disk` · **File Path and Name** → Expression → `/Users/alexcohen/InvestmentVault/Daily Intel/{{ $('Assemble').first().json.fname }}` · **Input Binary Field** `data`.

**Finish:** Workflow menu (`⋯`) → **Settings** → **Error Workflow** → `Error Watchdog` → Save. **Do NOT Publish yet** — §7.4's manual first run comes first.

### 7.3 The three Code nodes

Paste rules, identical for all three: open the node → **Mode** `Run Once for All Items` → select ALL boilerplate in the editor → delete → paste the block → Save. The code reaches other nodes via `$('Name')`, so the §7.2 node names must already be exact. If the editor shows red underlines after pasting, the paste was partial — clear and re-paste the whole block.

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
// (provider hard limit: max 50 tweet_ids/call — 400s above that; discovered live at 108 tracked posts)
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
// catches missing/malformed rows. Recalibrate per §7.5.
const DEF = { track_min_views: 3000, track_lv_pct: 1.5, track_rv_pct: 0.5, track_min_likes: 300,
  gem_lv_pct: 3, gem_rv_pct: 0.7, trend_min_delta: 150, trend_min_pct: 60, trend_min_base: 50,
  min_followers: 200, cap_tracked: 800, prune_age_days: 14, plateau_flat_likes: 10,
  plateau_pulls: 2, llm_top_n: 15, llm_model: 'claude-opus-4-8', archive_days: 90, x_tg_max_msgs: 8 };
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
    // strip LONE UTF-16 surrogates — emoji in tweets are surrogate PAIRS; a fixed-length .slice() can cut one in half,
    // leaving a lone \uD8xx that JSON.stringify emits as invalid JSON → Anthropic 400 "no low surrogate" → whole call dies
    messages: [{ role: 'user', content: (PROMPT + '\n\n' + llmInput).replace(/[\uD800-\uDBFF](?![\uDC00-\uDFFF])|(?<![\uD800-\uDBFF])[\uDC00-\uDFFF]/g, '') }] },
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
  // Telegram fan-out array — one message per divergence + per flagged post (XFanout node expands into N sends)
  const xcap = Math.max(1, Math.min(15, Math.round(c.x_tg_max_msgs || 8)));
  const tgm = [`𝕏 ${a.surfaced.length} flagged · ${divs.length} divergence${divs.length === 1 ? '' : 's'} · ${a.stats.tracked} tracked`];
  for (const d of divs) tgm.push(`⚠ ${d.name} — thesis divergence\n${d.divergence}`.slice(0, 3900));
  for (const s of a.surfaced) tgm.push(`[${s.f}] ${s.theme} · @${s.author} (${s.followers} fo · ${s.likes} likes)\n${s.text}\n${s.url}`.slice(0, 3900));
  out.tg_msgs = tgm.slice(0, xcap);
}
return [{ json: out }];
```

### 7.4 First run & what to expect

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
| Scheduled run silently missing — but only for a workflow you recently edited and saved | Saving a published workflow re-registers its trigger in memory, and that can fail silently: the DB still shows active but the live scheduler lost it (observed live: every untouched workflow fired, the freshly-saved one didn't) → `pm2 restart n8n`, then confirm the boot log lists every workflow as "Activated". Habit: after any editing session on a published workflow, glance at the next morning's Executions list |
| Everything after a node is skipped, yet the run shows "success" | Its On Error is `Continue (using error output)` — failures exit via an unconnected error connector; zero items silently ends the branch → set **Continue (using regular output)** everywhere this guide says Continue, re-run, then read the failing node's output panel for the real API error |
| Divergence feels generic — thesis never referenced | Verify the payload, not the wiring: open the execution → `Sentiment` → input → search `MY THESIS` — it must be followed by full section text, not just a heading. (known bug class: a multiline-`$` regex truncated every thesis to its first line) |
| `Access to the file is not allowed. Allowed paths: …` | File fence env var not live → verify `N8N_RESTRICT_FILE_ACCESS_TO=/Users/alexcohen/InvestmentVault` in the pm2 env, then `pm2 restart n8n --update-env` |
| `Referenced node doesn't exist` | A node name ≠ its `$('…')` reference → rename to the exact §7.2 card name |
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

### 7.5 Calibration & tuning runbook

- **Weeks 1–2:** calibration mode on (`calibration_until` in the state file). `ratio_log` accumulates your universe's real conversion distribution.
- **At calibration end:** ask Claude to compute p50/p75 of `ratio_log` → set `track_lv_pct`/`track_rv_pct` ≈ p50 and `gem_lv_pct`/`gem_rv_pct` ≈ p75 **in the Tuning table** → clear `calibration_until`. No code edit, no redeploy.
- **Tunables map — single source `_watchers.md § X Watchers`:** every engine gate (pull floors, MEGA list, entry lanes, gem, trending, plateau/prune, cap, LLM top-N) → `### Tuning` rows · curated terms → `### Curated terms` · cadence → Schedule node (raise `since_days` with it). Code headers hold fallback defaults only — they fire on a missing/non-numeric row, never override the table.
- **Threshold experiments:** change one gate at a time; write the why in the row's `notes`; judge on the next 2–3 pulls via the dashboard funnel (Seen → Admitted → flagged) — the header stamps the active gates each pull, so every render is attributable to its config. Git history of `_watchers.md` is the experiment log.
- **Monthly review add-ons:** prune expired term rows; check per-pull read volume (target 500–1,000 — adjust floors); skim dashboard themes for junk attribution (a noisy cashtag → raise `floor_mega`/`floor_std`).

---

## 8. Operations

- **Backups (monthly):** `cp -r ~/.n8n ~/n8n-backup-$(date +%F)` — contains the SQLite DB *and* the credential encryption key. Optionally export workflow JSONs into `_Archive/n8n-workflows/` so they version with the vault's git.
- **Watchdog:** §2.5 error workflow is mandatory equipment, not optional.
- **Monthly review (~20 min):** prune expired/orphaned rows in [[_watchers.md]] (move to its Retired section), retune noisy queries, tripwire levels vs current Conviction Triggers, triage threshold, pm2 status. This single file is the whole "what am I tracking" surface — one read tells you everything n8n is pulling. (The W3 Dedupe store self-prunes via TTL — no manual clearing needed since the card-12 rebuild.)
- **After ANY registry edit — row-shape validation** (malformed rows are skipped silently by Plan; these print offenders, silence = clean):
```bash
sed -n '/^## Outlet Feeds/,/^## Price/p' /Users/alexcohen/InvestmentVault/_watchers.md | awk -F'|' '/^\|/ && /https?:\/\// && NF!=9 {print "BAD feed row (needs 7 cols): "$0}'
sed -n '/^## News & Thematic/,/^## /p' /Users/alexcohen/InvestmentVault/_watchers.md | awk -F'|' '/^\|/ && NF!=7 {print "BAD thematic row (needs 5 cols): "$0}'
```
Also: `expires` cells must be `permanent` or `YYYY-MM-DD` exactly — the comparison is lexicographic, so `Aug 1` or `2026/08/01` mis-compares silently. New feed rows want the RSS/Atom **feed URL**, not the homepage (a homepage still fails visibly as a `⚠ Source failures` entry — check the next brief after adding). Daily confirmation that a new source is alive: its articles move the brief's `Channels: feed …` count.
- **When `/catalyst` or `_catalyst.md` format changes:** re-test the Workflow 2 parser the same day.

### 8.1 Migrating the whole setup to another Mac

The stack is four layers with different transports:

| Layer | Lives in | Moves via |
|---|---|---|
| Knowledge — notes, `_watchers.md`, skills, build docs | GitHub repo | `git clone` |
| Automation — workflows + credentials + their encryption key | `~/.n8n` folder (SQLite DB + config) | copy the folder via AirDrop/USB — **never via the repo**, it contains every API key |
| Local secrets + state — `.data/` | gitignored on purpose | recreate by hand: `config.json` is one line (FMP key); X-harvester state is reseeded per §6.3 — do NOT copy it, it's disposable and sharp again in 2 pulls |
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

### 8.2 Failure modes & resilience

**Concurrency (schedule overlap is safe by design).** The daily map: 07:10 W3 (25–45 min) · 07:30 W2 · 07:35 W1 (both fire *inside* W3's window, harmlessly) · 08:00 W4 · 08:30 W5 (clear of W3 normally). n8n interleaves concurrent executions in one process; every shared file is read-only or written as a new dated file (the no-editing-existing-files rule is what makes overlap safe); per-node state (dedupe store, W5 engagement ledger) has a single owner; W3's FMP calls (~07:12) finish before W1's quote call (07:35). Two real edges: (1) **hung-run collision** — a stuck W3 would still be "running" at the next day's 07:10; set W3's Workflow Settings → **Timeout 5400s** as insurance; (2) **Anthropic rate limits pool** across W3 and W5 — only relevant if W3 overruns into 08:30, failing silently as 429s behind On-Error-Continue (thin outputs). Operator rule: never manually Execute W3 while a scheduled run is active — two live executions race the dedupe store and split the day's articles across two briefs.

The X-workflow / platform failure-mode table moved to **§12.2** at the document bottom.

---

## 9. What NOT to automate

| Never | Why |
|---|---|
| Direct writes to Theses/Research/Sectors/Macro | Bypasses quality gate, idempotency keys, wikilink-form contract, `propagated_to:` atomicity — the exact failure classes [[INFRASTRUCTURE]] exists to prevent |
| LLM analysis inside n8n | Context asymmetry: no mental models, no READING PROTOCOL, no thesis state. Triage-scoring (headline or full body — Lane A) plus exactly two sanctioned output-side exceptions: Workflow 5's read-only sentiment/divergence layer (dashboard-only) and Workflow 3's digest-summary layer (`digest_model` — factual per-story sentences, `Daily Intel/` brief only; Lane B reversal trail: §11). Analytical summarization stays in `/ingest` |
| Tier 3 operations (`/status`, `/prune`, conviction, archive) | Investment decisions with confirmation gates by design |
| Trading actions of any kind | Tripwires are read-the-thesis signals, not execution signals |
| Auto-updating n8n itself | A silently-changed node schema is a silently-dead watcher; update quarterly, deliberately |

---

## 10. Summary — cost & current state

| # | Workflow | Schedule | $/mo | Status |
|---|---|---|---|---|
| 1 | Price Tripwires | daily 07:35 | 0 | **Live** |
| 2 | Catalyst Reminders | daily 07:30 | 0 | **Live** |
| 3 | News Sweep (unified: 5 channels × tickers+themes + body pipeline + story clustering + Opus brief) | daily 07:00 (07:10 during calibration) | ~60–110 | **In build** — §5; legacy v1 (GN-only, $0–8) stays live until §5.6 cutover |
| 4 | X Canary | daily 08:00 | ~0 | **Live** — §6.4 |
| 5 | X Harvester | daily 08:30 | ~17–40 | **Live** — §7.2; dated history in `Daily Intel/` |
| — | Error Watchdog | fires by reference | 0 | **Live** — set as Error Workflow in every workflow |

**Totals:** software $0 (n8n Community, fair-code, internal use) · hard running cost typically ~$20–35/mo today (Opus daily is the dominant line; `llm_model` registry row is the lever) — rises to ~$80–145/mo when unified W3 goes live (Opus story summaries + re-score and Sonnet triage are the dominant lines; the four §2.4 W3 model cells are the levers) · ongoing maintenance ~30 min/mo (§8 monthly review).

---

## 11. Provenance, merge history & change log

**Archived material:** the original decision log (25 dated entries, 2026-07-17 → 2026-07-20), the X-intelligence requirements table, and the full architecture-review rationale (storage/dashboard alternatives analyses) were removed in the 2026-07-20 restructure — preserved verbatim in [[_Archive/Docs/2026-07-20 - n8n Automations (pre-restructure)]], alongside the pre-merge originals. New entries append below.

- **2026-07-19 (doc merge)** — This doc merged from `n8n.md` (platform + Workflows 1–3) and `Twitter API Build.md` (X intelligence, Workflows 4–5). Pre-merge originals: `_Archive/Docs/`.
- **2026-07-20 (restructure)** — Doc rebuilt into sequential per-workflow build order (install → shared blocks → Workflows 1–5 each with card + build → operations → governance → summary); decision log, requirements table, and architecture rationale archived per the pointer above; all cross-references renumbered.
- **2026-07-20 (W3 unification, user decision)** — v1 News Sweep (GN-only, live 07:00/17:00) and 3b Feed Harvester (in build) merged into one workflow under the Workflow 3 name — 3b's engine, plus per-ticker coverage replicated across all search channels (v1's weekly per-ticker sweep became daily, on four engines). Same-day governance changes: Lane C (auto-clips to `_Inbox/`) **reverted** — output is a brief, not deposits; Lane B **reversed in contained form** — the digest summary layer authors factual per-story sentences, digest-only (hard rule 2, exception #2). §5's build guide was originally authored as the 3b guide and amended per this decision — per-ticker GN/GDELT/Brave queries added, Lane C clip output removed, Brave moved to paid tier; ⬥ marks the amended cards.
- **2026-07-20 (governance amendments, user decisions)** — Hard rule 1: Lane C briefly sanctioned verbatim `_Inbox/` auto-clips, reverted later the same day at the W3 unification — current law: no n8n `_Inbox/` deposits. Hard rule 2: Lane A approved (relevance-scoring may read full article bodies); Workflow 5's read-vault sentiment layer approved as exception #1 (2026-07-18); W3's digest summary layer approved as exception #2 (reversing the same-morning Lane B rejection). Brave moved to paid metered tier.
- **2026-07-20 (cadence, user decision)** — W3 set to 1×/day morning (replaces the planned 2×/day): afternoon/evening news lands in the next morning's brief; cross-execution dedupe makes the single run lossless, only slower. Brave volume halved (~3,000/mo; `brave_budget_mo` 3500).
- **2026-07-20 (story clustering, user request)** — Cards 18a–18d added: one cheap LLM call groups admitted items covering the same event across outlets; one summary per story; digest entries link every source article. Fixes the 5-channel duplicate-surfacing gap (URL dedupe can't catch reworded headlines). Cluster failure degrades to singletons, never a dead run.
- **2026-07-20 (model re-tier, user decision)** — Registry defaults raised: `triage_model` + `cluster_model` Haiku → **Sonnet**; `rescore_model` + `digest_model` Sonnet → **Opus** (capability-forward tiering; supersedes the same-day funnel-economics defaults). W3 running cost ~$60–110/mo; the four §2.4 cells are the de-escalation levers, and the §5.5f triage-band audit is the evidence for stepping `triage_model` back down.
- **2026-07-20 (pre-build hardening — full diagnosis before first build)** — Defects fixed in §5.3: Admit/Final item-pairing bug (raw `$('TriagePrep').all()[i]` indexing was offset by bypass+sentinel items → would have silently admitted zero scored items; now filters to `_batch` items first); `temperature` removed from all LLM bodies (Opus rejects sampling params → silent 400 under On-Error-Continue); all four Anthropic request bodies moved to the `_llm_body` pattern (built in Code, sent as one `JSON.stringify` expression — kills the quote-escaping failure class). Improvements: bypass (`triage: no`) rows routed through the body pipeline (real bodies, Opus re-scores, real ranks — was headline-only, score 0); thesis wikilinks on ticker stories (`cfg.ticker_files` map → `[[Theses/…]]` in the brief); funnel telemetry header (`fetched → new → admitted → stories` via the warnings sentinel); unscored stories render `—` and sort last; new `log` output lane writes one dated JSON per run to `.data/news_stories/` (machine-readable newsflow corpus for `/retro`); first-run checks (g)–(j) + three troubleshooting rows added. Second diagnosis pass caught a defect introduced by the bypass-routing fix itself: two wires into IF 16's single port risked per-branch double execution (two digests/run) — replaced with explicit Merge "PreBody" (card 15b); same convergence caution documented for Normalize's 5 inbound wires.
- **2026-07-20 (cross-run story memory, user request)** — URL dedupe + within-run clustering couldn't stop the same story re-surfacing across days as slower outlets published their own takes. New card 2b (PriorStories) reads the last `story_memory_days` (Tuning row, default 7) of `.data/news_stories/` run logs; the 18a cluster call now judges NEW items against PRIOR briefed stories (title + summary) and diverts no-new-facts follow-up coverage to a links-only ♻ section at the brief's tail — never re-summarised, never silently dropped, never pushed to Telegram. Items that advance a prior story (new numbers, responses, escalations) are briefed as new. First-run check (k) + two troubleshooting rows cover both failure directions (echo leaking through vs. developments wrongly parked).
- **2026-07-20 (post-diagnosis feature set, user decision — all six Part-2 suggestions)** — In W3: **catalyst proximity markers** (card 2c reads `_catalyst.md`; Plan builds `cfg.catalysts` within ±`catalyst_window_d` (new Tuning row, 10); Assemble tags ticker stories `📅 T-N: event`) and **X attention overlay** (card 2d reads the latest W5 dashboard; per-theme sentiment scraped to `cfg.x_read`; stories tagged `𝕏 bullish/bearish/mixed/quiet` — `𝕏 quiet` on a score ≥8 cashtag-tracked name flags the pre-consensus case); both degrade to no-markers on missing inputs; first-run check (l). In the vault skills (explicit user authorization for `.claude/skills/` edits): `/surface` Phase 2.5 mines `.data/news_stories/` for registry drift (recurring high-score subjects with no watcher row; dead rows with zero stories); `/retro` Phase 3.0 reads the same corpus as a local newsflow channel + the high-score/flat-price signal; `/ingest --from-brief [date]` (Mode D) turns brief stories into pick-list ingestion with multi-source retry; `/clean daily-intel [days]` prunes n8n scanning surfaces from `Daily Intel/` (default 90d; n8n-pattern filenames only; `.data/news_stories/` corpus explicitly protected).
- **2026-07-20 (final diagnosis — empty-branch stall guards)** — Third pass targeted execution-order edges: on quiet/all-bypass/zero-body days a legitimately-empty branch starves a Merge input (PreBody or Rejoin) and stalls the run. Guards: TriagePrep always emits ≥1 batch (empty + null body); Always Output Data ON for Admit and Final; troubleshooting row with the pass-through branch-keeper fallback for the never-executed card-17 chain.
- **2026-07-20 (Sonnet 5 for triage + cluster, user decision)** — `triage_model` + `cluster_model` moved `claude-sonnet-4-6` → **`claude-sonnet-5`** (newer, and cheaper during intro pricing — $2/$10 per MTok through 2026-08-31 vs 4.6's flat $3/$15). Changed in all six spots: registry cells 245–246 + code `DEF` fallback (card 5) + §2.4 model-selection table + `_llm_body` contract note (§5.3) + card 18b default note. Consistency edits made in the same pass: the `rescore_model`/`digest_model` Sonnet **step-down** references (`_watchers.md` 247–248, §5.3 cards, contract note) repointed `claude-sonnet-4-6` → `claude-sonnet-5` so the doc names one Sonnet throughout; the §5.7 "same story appears twice" troubleshooting lever changed from "flip `cluster_model` to `claude-sonnet-4-6`" (a no-op once cluster defaults to Sonnet) to "escalate to `claude-opus-4-8`" (the intent-preserving upgrade path). §5.1 check-4 curl now smoke-tests `claude-sonnet-5` — reachability on this key still to be confirmed before first run.
- **2026-07-20 (Dataview inline-query collision fix, mid-build)** — the LLM-body snippets were written as inline code beginning with an equals sign (Dataview's inline-query trigger), which the vault's Dataview plugin intercepts and renders as evaluation errors — visible as "bugged formatting" from §5.3 card 13 onward (contract note, cards 14a/Rescore/18b/18d, one §5.7 row) plus W5's node-table row 14 (pre-existing since that build). Leading equals sign dropped from all 7 spans; wording repointed to "toggle to Expression → paste `{{ … }}`". Doubles as a paste-trap fix: an equals sign typed into n8n's expression editor prepends it literally to the rendered body → invalid JSON → silent 400 under On-Error-Continue (the headline-only-digest failure mode).
- **2026-07-20 (registry-editable LLM prompts, user request)** — all four W3 prompts (triage, rescore, cluster, digest) moved from hardcoded template literals in the Code nodes to `####` blocks under `## Outlet Feeds → ### Prompts` in `_watchers.md`, extending the §2.4 "every LLM knob is an Obsidian cell" convention from models to prompts. Mechanics: Plan (card 5) parses the blocks into `cfg` with a `DEF_P` code fallback mirroring the registry text; runtime values ride as literal tokens (`{tickers}` `{themes}` `{items}` `{prior}`) substituted by a split/join `sub()` helper in cards 13/17.4/18a/18c (split/join, not regex replace — dollar signs in payload text would corrupt regex replacement); a block missing its required token silently reverts that stage to `DEF_P` (broken prompt ≠ dead run). Enforcement: §5.1 check 9 gained a third grep (prompt headers = 4); §5.7 gained the no-effect troubleshooting row. The user's hand-edited triage cluster list (AI, futurism, tech philosophy, consumer tech — replacing logistics/media/essays/general-tech) was taken as canonical in both registry and fallback; "philosphy" typo corrected.
- **2026-07-20 (first-build shakedown — W3 unified, four defects found live)** — (1) **405 Method Not Allowed** at Summarise: HTTP nodes were built GET (n8n default; prior X-harvester fetch nodes were legitimately GET) — all four Anthropic nodes are POST-only; cards 14a/17.5/18b/18d now state Method explicitly + §5.7 row. (2) **Per-branch multi-execution CONFIRMED on this instance**: two wires into Feeds ran RSS twice; five wires into Normalize ran the downstream chain 3× as partial pipelines, the emptiest lineage ending in SumPrep's null-body fallback → 400 at Summarise. Fix promoted from conditional advice to mandatory cards: **6b Merge FeedTasks** (Route 0/1 → one RSS delivery) and **10b Merge PreNormalize** (5 fetch wires → one Normalize execution); wiring map + check (j) updated. (3) **Zero-item loop-back stall**: a no-result GDELT/Brave query returned `[]`, freezing Loop Over Items mid-list (`done` never fired — Brave died on iteration 1, Sunday past-day queries being routinely empty). Fix: Always Output Data ON for GParse/BParse; Normalize's URL guard drops the `{}` placeholders. (4) **Debug-run dedupe poisoning**: earlier failed runs registered URLs in the card-12 cross-execution store, emptying subsequent test runs — Clear Deduplication History procedure added to §5.7. Summarise also lacked On Error: Continue (built from the pre-expansion card), turning the benign empty-day 400 into a run-stopper.
- **2026-07-20 (shakedown wave 2 — Normalize rewritten shape-based)** — With the 10b Merge in place and single-wire topology confirmed, a full run still delivered ~30k items into Normalize and got only the warnings sentinel out: the original Normalize classified non-pre-tagged items by `pairedItem`→Plan-task lookup, and pairing metadata does not survive a Merge — items landed in wrong/no branches and were dropped silently. Card 11 rewritten: classification by item shape (ch-tagged / `error` / `symbol`+`publishedDate` / `title`+link-like), gn-vs-feed split by hostname, outlet labels via feed-URL hostname map, link-field fallbacks (`link`/`url`/`guid`/object-href), AOD-placeholder skip, and a self-reporting drop counter (`normalize:dropped:N keys:…` in the sentinel warnings — future drops name their own shape in the brief). WriteDigest/WriteLog by-name paths promoted to primary (Convert to File strips item JSON on this instance — "path is a directory" on `$json.fname`). Debug-detach procedure documented (§5.7): unplug the 4 GDELT/Brave wires for ~3–5 min iterations.
- **2026-07-20 (future-source hardening, user request)** — Four gaps closed so registry additions can't silently degrade the pipeline: (1) **Dedupe History Size 10,000 → 50,000** (card 12) — the default evicted after ~1–2 days of flow, re-briefing evicted URLs as new, worsening with every added source; (2) **hostname map → base-domain matching** in Normalize (cc-SLD aware: `digitimes.com.tw` kept whole) — subdomain-hosted feeds (`feeds.…`/`rss.…`, the common case for new adds) now retain their `bypass`/`body_exempt` labels; (3) **per-channel counters** — Normalize sentinel `_ch` → ClusterPrep `_stats.ch` → brief renders `Channels: feed · gn · gdelt · brave · fmp` under the funnel line; a channel at 0 is visible every morning (check (i) extended); (4) **row-shape validation commands** in §8 — malformed rows (wrong column count, bad `expires` format) are skipped silently by Plan; the awk pair prints offenders after any registry edit.
- **2026-07-20 (shakedown wave 3 — the actual root cause: no `URL` global in the Code sandbox)** — The self-reporting drop counter added in wave 2 paid off on its first run: `normalize:dropped:30594 badurl:<valid URL>` — a valid URL failing parse means the parser itself is absent. This n8n's Code sandbox does not provide the `URL` global; `new URL()` threw on every call, canon's try/catch returned null, and every article in every run was rejected as a bad URL — the true cause of ALL of today's empty pipelines (the original pairing-based Normalize used `new URL()` too, so no run ever worked; the dedupe-poisoning theory was moot — nothing ever registered). Card 11 rewritten URL-free: regex `canon` (protocol check, fragment strip, tracking-param removal) + regex `hostOf`; error-lane warnings now carry the actual error text instead of `src:? failed`. Audited: no other W3 Code node uses `new URL()`. §5.7 row added — never introduce browser/Node globals into Code nodes without a one-line sandbox test.
- **2026-07-21 (first-brief feedback round, user requests)** — Four output-quality changes after reading the first real brief: (1) **age gate** — GN search RSS is relevance-ranked and surfaced months-old items; every GN query now carries `when:Nd` and Normalize drops provably-old items (`max_age_d` Tuning row, default 3; `stale N` count rendered on the Channels line; undated items fail open); (2) **score pill** — `- [9]` rendered as a themed checkbox in Obsidian (single-char bracket = custom checkbox state), scores now render as backtick code pills; (3) **Telegram re-cut** — top-5-titles push replaced by the single highest-scored story + its summary (≤700 chars) + link + one-line footer, per user request; (4) **🔒 paywall markers** — source links whose feedId is in `body_exempt` carry a lock so paywalled clicks are flagged upfront. Also: `digest_prompt` default upgraded (registry + `DEF_P`) — 2–4 sentences of maximum factual density with comparisons/mechanism/timelines and fact-linkage significance ("first ever", "reverses prior guidance"), still zero opinion/inference per hard rule 2; the brief remains a scanning surface by governance — thesis-relevance commentary would be a rule-2 amendment requiring explicit user decision (offered, not taken).
- **2026-07-21 (hard rule 2 removed, user decision)** — "Triage yes, analysis no" repealed: the user wants the LLM to read articles and produce actionable intelligence, not factual stenography. Rule 2 rewritten as a **write-surface boundary instead of a content prohibition**: n8n LLM stages may now analyze freely (facts → coverage implications → transmission path → confirm/refute markers) but their output remains confined to `Daily Intel/` + `.data/` (rule 1); nothing n8n writes enters Theses/Research/propagation, `/ingest` stays the only vault-ingestion path, briefs remain dated disposable context pruned by `/clean daily-intel`. Residual quality bar: grounded-in-source, inference labeled — opine, never invent (first-run check (c) rewritten from "factual, not editorial" to a grounding/hallucination check). `digest_prompt` rewritten in registry + `DEF_P` to the decision-useful form. Telegram push simplified per same message: score dropped, summary allowance raised to 900 chars (title + summary + link + footer only). The original rule's rationale — context-free LLM prose laundered into the vault as source material — is now guarded entirely by the write boundary rather than by content restrictions.
- **2026-07-21 (paywall de-emphasis, user request)** — Paywalled content now clears a stricter bar or vanishes: (1) Normalize stamps `pw` on items whose feed row is in `body_exempt` OR whose URL lands on a `paywall_domains` domain (new Tuning row — catches Bloomberg/WSJ/FT arriving via Brave/GDELT, not just own-feed rows); pw items also skip body-fetch (paywall pages return junk); (2) triage + rescore prompts see `pw:1` with a headline-must-be-material instruction (registry + `DEF_P`); (3) Admit enforces `triage_min_pw` (new Tuning row, default 9 vs normal 7) — deterministic, so mid-relevance paywalled stories never reach the brief; (4) the three paywalled bypass rows (`econ-finance`, `econ-business`, `theinformation`) flipped `triage: no → yes` so nothing paywalled auto-admits. Survivors keep the 🔒 marker. Limitation: paywalled outlets arriving through Google News redirects are undetectable pre-click (opaque URLs) — mitigated by the pw-gate catching the same story's direct-URL variant from other channels.
- **2026-07-21 (Telegram fan-out, user request)** — single capped push replaced by top-N story messages: Assemble emits up to `tg_max_msgs` (new Tuning row, default 10, clamped 1–20) `tg` items, rank order, one full summary + link per message; footer + failure count on the last message; quiet-run message preserved. No architecture change — the Telegram node already sends one message per input item, so the Switch/Notify wiring is untouched. Flood caveat documented in the registry row (Telegram same-chat ~1 msg/s; lower the cap if 429s appear).
- **2026-07-21 (analysis-depth round, user sense-check)** — User hypothesis "sub-minute LLM stages = shallow analysis" adjudicated half-right: latency reflected thin incremental inputs, not model effort — but four real depth ceilings existed and were lifted. (1) **Adaptive thinking** (`thinking:{type:'adaptive'}`) enabled on Rescore/Cluster/Summarise with max_tokens 4000→8000 (Triage stays plain — volume stage; parsers already filter to text blocks so thinking blocks are transparent). (2) **Excerpt budgets raised**: rescore 4k→6k chars/item; digest member slice 2k→4.5k, per-story cap 3.5k→9k. (3) **Digest batches 12→8** stories/call for per-story attention. (4) **Context injection**: per-story `sig` field (catalyst proximity + X sentiment from cfg — data that existed but never reached the summariser) + new optional `#### brief_context` registry block → `{context}` token in digest_prompt — the user's standing priorities as an analytical steering wheel, editable without touching prompts. Cost impact ≈ +$10–20/mo (thinking tokens + larger excerpts). Honest-eval note: today's incremental runs cannot demonstrate depth (29/31 headline-only); the first fair test is a full-channel morning run with bodies.
- **2026-07-21 (repeat suppression hardened, user report)** — Same stories re-appearing in digest + Telegram across same-day test runs: cross-run dedupe had relied entirely on the cluster LLM's repeat judgment (URL dedupe can't catch a story resurfacing under fresh URLs). Two-layer fix: (1) **deterministic title-key guard** in ClusterPrep — new items whose normalized title key (same `tkey` as Normalize's in-run dedupe) matches a prior story auto-divert to the ♻ follow-ups list BEFORE the LLM votes (`_preFollowups`, seeded into SumPrep's list; funnel `admitted` now counts pre-diversion candidates); (2) **bias-toward-repeat clause** added to cluster_prompt (registry + `DEF_P`) — same event with no new specific is a repeat regardless of wording/outlet/angle. ♻ items never reach Telegram (unchanged). Diagnostic note: `_prior` empty in an execution = PriorStories (2b) broken, the other root cause for repeats.
- **2026-07-21 (deployed-node drift discovered + grouping sharpened)** — `_prior` missing entirely (not empty) from ClusterPrep's execution output proved the deployed node ran a pre-story-memory paste: the memory feature had NEVER executed live — PriorStories collected logs no consumer read, fully explaining the cross-run repeat leak. Lesson institutionalised as a §5.7 row: a missing output field names its stale node (doc edits never auto-sync; field presence in the next execution is the resync verification). Full 8-node resync prescribed. Separately, within-brief duplicates (same event, two outlets, two entries) traced to the cluster prompt's own "when unsure, keep separate" clause — replaced (registry + `DEF_P`) with an actor+action+timeframe same-story test: one event from multiple outlets is ONE cluster; split only on genuinely distinct developments. Escalation ladder if still chronic: `cluster_model` → `claude-opus-4-8` (thinking already enabled).
- **2026-07-21 (deterministic near-dup merge — grouping stops relying on the LLM for string similarity)** — Similar-headline duplicates still rendering as separate stories after the prompt sharpening: root insight is that mechanical similarity is not a judgment call and should never have been delegated to the model. Three code layers: (1) both `tkey` copies (Normalize in-run dedupe, ClusterPrep cross-run guard) strip trailing `" - Publisher"` segments so GN variants of one headline share a key; (2) SumPrep's grouping rebuilt as union-find — LLM clusters seed the unions, then a Jaccard pass (token overlap ≥ 0.5, tail-stripped, ≥3 significant words) force-merges near-identical headlines the model split; components become stories, LLM gaps become singletons automatically; (3) the LLM's remaining role is genuinely-reworded same-event grouping only, with `cluster_model` → Opus as the documented last lever. Threshold 0.5 hardcoded in SumPrep (tighten→0.6 if false merges appear, loosen→0.4 if twins persist).
- **2026-07-21 (dedup rearchitected — count-cap → TTL, user-identified architectural bug)** — "Number of entries exceeded cap" after only a few runs (50k already set) exposed the real defect: n8n's Remove Duplicates node has a count-based history with NO eviction, and Google News redirect URLs churn every fetch (~10k throwaway keys/run), so the store ballooned and overflowed regardless of History Size — raising the cap only delays it. Card 12 rebuilt as a **Code node using TTL-bounded static data** (`$getWorkflowStaticData`): evicts URLs older than `max_age_d + 2` days each run, bounded by time not count, physically cannot overflow, self-clearing (monthly-clear ops task and all Clear-History troubleshooting removed as obsolete). Cross-run GN *story* repeats remain 18a story-memory's job; card 12 only stops exact-URL re-processing from stable channels. Note recorded: n8n's count-capped dedup is unsuitable for any source with unstable URLs.
- **2026-07-21 (retention windows separated — dedup vs sentiment tracking, user request)** — User wanted 30-day sentiment tracking + score-filtered + 3-day-non-repeat storage, initially by extending the dedup store. Disentangled into the correct two stores: dedup (`seenUrls`, static data, DB) stays short via new `dedup_ttl_d` (default 3 = "non-repeats past 3 days"); 30-day sentiment tracking lives in the `.data/news_stories/` disk logs (already retained 90d by `/clean`, already storing admitted stories with scores + 𝕏/catalyst markers = sentiment substrate). New knobs `track_min_score` (8) + `track_window_d` (30) make `/surface`'s already-existing 30-day story-log read tunable, and Phase 2.5 extended to surface sentiment trajectory (𝕏 flips, score trends) not just registry drift. DB-cost verdict recorded: 30-day dedup in static data ≈ 5–8 MB reloaded every run (onerous, rejected); 30-day disk logs ≈ 12 MB of files nothing reloads (trivial). No new n8n write lane — the substrate already existed.
- **2026-07-21 (W5 Telegram fan-out, user request)** — X Harvester's single Telegram wall-of-text replaced by 5–10 separate messages (divergences first, then flagged gems/trending posts). Code D (Assemble) now also emits `out.tg_msgs` (array, capped at new `x_tg_max_msgs` Tuning row default 8, clamped 1–15); new **card 20c `XFanout`** Code node sits between the push gate (20-true) and Telegram (21), expanding the array into one item per message — Telegram sends one per item. `out.text` retained so the push gate still fires; XFanout falls back to `[text]` if `tg_msgs` absent. Same pattern as W3's Assemble fan-out (2026-07-21). Wiring: 20-true→20c→21 (was 20-true→21); 20-true→20b unchanged. Flood caveat (~1 msg/s) documented in the Tuning row.
- **2026-07-21 (readability cleanup, user request)** — Snapshot `_Archive/Docs/2026-07-21 - n8n Automations (pre-cleanup)`. Four-part pass: (1) all troubleshooting consolidated into new **§12** at the document bottom (§5.7 W3 table → §12.1, §8.2 failure-mode table → §12.2; both original locations left a one-line pointer; §5.7 heading + §8.2 concurrency-resilience prose kept so cross-references and operational design survive) — troubleshooting no longer tails individual sections. (2) §5.5 first-run rewritten from a single ~600-word paragraph into a scannable (a)–(l) checklist. (3) Code-placement audited — all 58 code blocks already sit directly under their introducing card (0 displaced). (4) Idiot-proofing confirmed already in place from the 2026-07-20/21 build rounds (click-level Method/Send-Body/credential steps, wiring recaps, first-run checks). Card and § numbers preserved throughout (active build in progress). Further prose-density reduction across §5.3/§7 remains available section-by-section on request.
- **2026-07-21 (repeat suppression — deterministic title layer tried then REVERTED per user)** — First attempt added a card-12 cross-run title-key store (`seenTitles`); user correctly rejected it: string-matching on headlines cannot detect two articles with *different* headlines and *different* wording that are the same underlying story (different authors, same event) — that is inherently a semantic judgement, and the layer was also redundant with 18a's existing deterministic title guard. Reverted card 12 to URL-only. Kept: SumPrep's `merge_jaccard` knob (0.5 → 0.42, within-run near-dup backstop only — same lexical limitation, acknowledged). **Correct home for same-story dedup is the cluster/story-memory LLM (18a/18b)** — the real weakness there is that the cluster call sees new items as *title + source only*, not article excerpts, so its grouping is headline-limited; the durable fix is to feed it excerpts + Opus so it judges same-story on content. Deferred pending user direction.
- **2026-07-21 (semantic same-story dedup — cluster call fed excerpts + Opus, user direction)** — Root fix for "same story, different headlines/authors" repeats: the cluster LLM was seeing new items as title+source only, so its grouping was headline-limited. ClusterPrep now packs a **content excerpt** per item into the payload (`x` = body text if fetched, else snippet, ≤600 chars); cluster_prompt (registry + `DEF_P`) instructs judging same-story on the excerpt's substance (actors/action/event), not headline wording. `cluster_model` moved sonnet-5 → **claude-opus-4-8** for the semantic lift (updated in all refs: registry cell, card-5 DEF, §2.4 table, card 18b note). Cost ~$1–2 → ~$8–12/mo. This is the correct architecture per the reverted-title-layer analysis: string-matching can't detect semantic same-story; the LLM can, but only if it sees content. Honest ceiling: imperfect (occasional split/merge), residual caught by the ♻ links-only section; embeddings-based clustering (new provider) is the next lever if needed.
- **2026-07-22 (cluster-truncation fix — the real bug; + Telegram diversity backstop, user report)** — Excerpt+Opus cluster still shipped same-story dupes: 2 TSMC price-raise articles AND 5 articles on one IQE earnings report, all unmerged. Both are the SAME failure, not two problems — the IQE case (5 outlets, one earnings event, the easiest possible cluster) proves clustering wasn't running at all. Root cause: the cluster call ran `max_tokens: 8000` WITH adaptive thinking — thinking consumed the budget and truncated the `{clusters,repeats}` JSON, SumPrep's parse failed, and it fell back to one-story-per-item (no clustering). Fix: cluster `max_tokens` 8000 → 24000 (headroom for thinking + JSON) — this alone resolves both symptoms. Added as a general backstop (NOT the IQE fix, which was pure clustering failure): a per-subject diversity cap on the Telegram fan-out (`tg_per_subject`, default 2) for the separate future case where a subject legitimately has many distinct stories. Diagnostic: Cluster (18b) OUTPUT — error/empty/truncated = degrade-to-singletons; valid `{clusters,repeats}` = grouping ran.
- **2026-07-22 (W5 morning no-fire — dropped schedule trigger, not timezone)** — Diagnosed via the n8n DB: all schedules fire at correct Sydney times (`GENERIC_TIMEZONE=Australia/Sydney` confirmed in the pm2 dump; execution `startedAt` is UTC — a +14h misread initially pointed at America/New_York, corrected by converting UTC→AEST, which matched the configured 07:10/07:30/07:35/08:00). Real cause: W5's schedule trigger was silently dropped when the workflow was edited 07-21 (Sentiment-POST/XFanout work) — n8n kept `active=1` but didn't re-arm the cron, so the 07-22 08:30 run never fired (it fired fine 07-19 and 07-21, before the edit). Fix: toggle Active OFF→ON. Operational rule added to §5.3 convention note + §12.2: **cycle the Active toggle after editing any active scheduled workflow** — Save does not reliably re-register the cron in n8n 2.x, and manual runs mask it. §12.2 also gained a UTC-timestamp row so the storage-tz gotcha isn't repeated.
- **2026-07-22 (W5 Sentiment 400 — lone UTF-16 surrogate, user-provided node error)** — W5 finished in 26s with a garbage dashboard (all sentiment `—`, "LLM unavailable"). Pull was healthy (419 seen / 70 admitted); the Sentiment Opus call 400'd: `"The request body is not valid JSON: no low surrogate in string: char 209201"`. Cause: tweets are emoji-dense, emoji are UTF-16 surrogate pairs, and the Analyze node's fixed-length `.slice()` calls (tweet text 1000, anchors 300, thesis 12000) cut one pair in half → a lone high surrogate → `JSON.stringify` emits invalid JSON → Anthropic rejects the whole call → On-Error-Continue swallows it → "LLM unavailable". Fix: Analyze node strips lone surrogates from the payload content before send (regex on the `content` string, line ~1920) — complete emoji preserved, only broken halves removed. W5-specific in practice (news text isn't emoji-dense); flagged as a latent W3 risk in §12.2. Not a temperature/method/timeout issue — the node's own 400 response was the tell.
- **2026-07-23 (embeddings semantic-dedup layer — the "next lever/new provider," + cost diagnosis, user request)** — User reported ~$15–20/day Claude bill + residual duplicate articles. Measured actual per-run cost from the n8n execution store (`execution_data.usage`): **W3 ≈ $10–12/run** (exec 88: 1.06M in / 219k out; exec 85: 1.26M in / 243k out — ~95% of the bill), **W5 ≈ $0.85/run** (exec 92). Driver was **volume through the Opus body pipeline**: ~200–400 admitted items, ~23+ Opus rescore calls/run — and same-story duplicates were being body-fetched + rescored + summarised *before* the post-body cluster call collapsed them. Fix executes the embeddings lever flagged 2026-07-21: semantic same-story + cross-run repeat detection moved to **Voyage embeddings** (`voyage-4-lite`, $0.02/M with 200M free tok/account ≈ free at this volume) and **upstream of the body pipeline** so duplicates never reach Opus. New cards **15c EmbedPrep · 15d Embed (HTTP, Voyage cred) · 15e SemCluster** (cosine union-find → one representative per story, all source links preserved on `_members`; cross-run repeats → ♻ via `repeat_threshold` OR title-key); the old Opus **18a ClusterPrep + 18b Cluster deleted**, **Rejoin (18) → SumPrep (18c)** direct, **SumPrep rewritten** to read pre-collapsed reps (Jaccard kept as backstop). Registry: `embed_model`/`sim_threshold`(0.86)/`repeat_threshold`(0.88)/`embed_max_chars`(1000) added; `cluster_model` deprecated (kept for rollback). Cost impact: Opus cluster call gone (~$8–12/mo) + body/rescore volume cut by the dup ratio (~20–40% on dup-heavy days); embeddings ≈ $0. Both new Code nodes + the SumPrep rewrite unit-tested off-workflow (5 SemCluster assertions: merge, representative-picks-non-paywalled, singleton, cross-run divert, stats; 5 SumPrep assertions: source-links preserved, sig markers, excerpt-strip, no-temperature, token-substitution — all pass). Same-story dedup is now deterministic (one `sim_threshold` dial), no LLM-truncation failure mode. NOT taken this round (offered, remains available as the biggest lossless lever): `rescore_model` Opus→Sonnet + drop adaptive thinking on the scoring stages.
- **2026-07-23 (FMP coverage — limit cap + symbol resolution, user question)** — User asked why FMP returns exactly 150 items/run. Diagnosed live against the key: `stable/news/stock?symbols=…&limit=50` returns the 50 newest articles **across the whole 25-ticker batch, recency-sorted — not 50 per ticker**; 71 US tickers → 3 chunks × 50 = 150, stable every run. One batch covered only 10/25 symbols (AMD alone ate 24/50; 15 tickers got zero). Fixes (card 5 Plan + card 10 URL): `limit` 50→**250** (the endpoint's hard ceiling — `limit=1000` also returns 250) + a `from`/`to` **date window** (= `max_age_d`, so the 250 cap isn't wasted on stale items) + `FMP_CHUNK` 25→**10**. Measured effect: coverage ~30%→**77% of tickers** (54/70), items 150→~910/run. Chunk size proved **irrelevant to coverage** (chunk 10 and 5 both = 54/70, identical missing set) — the binding constraint is that the other ~16 don't resolve in FMP's US news feed: ~11 foreign-listed (Amsterdam/London/Tokyo/Toronto/Sydney — covered by the GN/GDELT/Brave company-name channels by design), 4 genuinely thin on FMP (OPEN/PCOR/PSTG/SOI, correct symbol/0 articles), and **1 real bug — KLA is KLAC on Nasdaq** (`KLA: NOT FOUND` / `KLAC: KLA Corporation`), now fixed via a new `FMP_ALIAS` map in Plan (extensible for future prefix≠ticker mismatches). Cost note (post the same-day embeddings cost cut): the ~6× item bump lands almost entirely on triage (cheap Sonnet, ~7 batched calls) + free embeddings; `triage_min` gates the FMP PR-wire noise before Opus. Plan block validated off-workflow (alias applied, foreign excluded, from/to = 3-day window — all pass).
- **2026-07-23 (GDELT underperformance — window + maxrecords + sticky rate-limit, user question)** — GDELT was ~2% of fetch (155 items / ~1.4 per query) vs GN's 68%. Diagnosed live: three compounding causes. (1) **`timespan=24h`** while the pipeline keeps 3 days (`max_age_d`) and GN uses `when:3d` — GDELT saw 1/3 the window; fixed to `{{ (max_age_d)*24 }}h` (registry-driven, card 8.2 URL). (2) **`maxrecords=50`** capped busy queries — `Nvidia` returns 250+ (the endpoint max); raised 50→250. (3) **Sticky rate limit** — GDELT 429s after ~4 rapid calls *even at 20s spacing* (re-verified), so of ~110 paced queries only the first ~4 succeed and the rest 429→0 (fully explains the 155). `gdelt_spacing_s` 8→12 for headroom; durable fix if still weak is cutting query volume (thematic-only Plan gate → ~40 not ~110, or a small priority set) — GN already covers 68%, so GDELT's value is its differentiated international/thematic index, not raw volume. Query FORMAT confirmed healthy (OR-groups return articles, just niche). Live retest: `Nvidia` 250 at every window; thematic OR-group 5; 5th call 429'd. Stage-2 implemented in card 5 Plan: GDELT now skips US tickers (`/^[A-Z]{1,5}$/` — the same rule as FMP's `us` filter), keeping themes + foreign-listed tickers where GDELT's international index is the differentiated channel; cuts ~110→~55 queries so the rate-limit budget lands on coverage GN/FMP lack.
- **Status history** — W1 Price Tripwires + W2 Catalyst Reminders live 2026-07-17/18. W4 X Canary + W5 X Harvester live 2026-07-18; X cadence 3-day → daily and `prune_age_days` 14 → 28 on 2026-07-18; X calibration window through 2026-08-01; digests relocated `_Inbox/` → `Daily Intel/` (decision 2026-07-18). Legacy W3 v1 live 2026-07-18, superseded 2026-07-20 by the unified build (in build since 2026-07-20); v1's digest Write node was never repointed post-relocation — known since 2026-07-19, still writing `_Inbox/` at supersession.
- **Verification & lesson timestamps (swept from the body 2026-07-20 for a clean read)** — FMP v3 endpoints verified legacy-dead on this key 2026-07-17. FMP keyword news search probed conclusively absent 2026-07-20. GDELT 1 req/5s hard limiter + sticky IP cooldown verified 2026-07-20. defuddle CLI v0.7.0 confirmed installed 2026-07-20. `NODES_EXCLUDE` Execute-Command re-enable added 2026-07-18. twitterapi.io 50-id batch cap hit live 2026-07-19 at 108 tracked posts — the exact failure the §6.2 verification checks (skipped by user decision 2026-07-18) were written to catch; invoiced one day later. W5 thesis-truncation regex bug (multiline-`$`) found and fixed 2026-07-18. Manual-run-never-delays-schedule lesson 2026-07-19. Trigger re-registration silent-failure observed 2026-07-20. W2 multi-ticker parser gap found 2026-07-20 (the 2026-07-18 GENIUS Act catalyst row was the proven miss). All 94 Outlet Feeds URLs verified live 2026-07-20 (381-bookmark audit).

---

## 12. Troubleshooting (all workflows)

Symptom → cause → fix. Build steps are in §1–§7; this is the "something's wrong" lookup, consolidated here so no section carries its own troubleshooting tail.

### 12.1 Workflow 3 — News Sweep

| Symptom | Cause | Fix |
|---|---|---|
| Plan throws `0 tasks` | Registry section headers renamed or table malformed | Headers must contain `## Outlet Feeds` / `## News & Thematic`; check a row's pipe count |
| GDELT items = 0, response is prose | Rate-limit text (HTTP 200!) | Raise `gdelt_spacing_s`; never retry in-run |
| GDELT is a tiny fraction of fetch (`gdelt N` small vs `gn`) | Three causes (fixed 2026-07-23): `timespan=24h` (→ `max_age_d`×24 h), `maxrecords=50` (→ 250), and a **sticky rate limit** that 429s after ~4 rapid calls so most of a ~110-query run returns nothing | Re-paste the card 8.2 Gdelt URL (window + maxrecords). If still small, cut query volume: gate GDELT to `cluster==='thematic'` in card 5's Plan (~110→~40), or a smaller priority set — GN covers the bulk regardless |
| Brave 401 / 429 | Bad key / paid tier not active / burst | Re-check credential + confirm metered plan on the Brave dashboard; Wait ≥2 s |
| Body text is nav junk / cookie banner | defuddle failed on that site's DOM | Accept (score drops at rescore) or add feed id to `body_exempt` |
| Summary states a fact not in the article | Hallucination on a thin excerpt | Raise SumPrep excerpt length; treat `*(headline only)*` items as unverified — never quote a brief summary into research without opening the link |
| Run takes >35 min | GDELT pacing × ~120 targets | Lower `gdelt_spacing_s` toward 6 (never <5 — sticky IP cooldown); otherwise accept, it's a background sweep |
| `Paired item data unavailable` in Normalize | n8n lost pairing through RSS Read | Cosmetic (mislabeled feedId); Normalize classifies by shape now, not pairing — safe to ignore |
| Zero admitted despite plausible triage responses | Admit/Final pairing broken — lookup must filter to `_batch` items first (cards 15/17) | Verify the `preps = ….filter(x=>x._batch)` line survived the paste; raw `.all()[i]` indexing is off-by-the-bypass-count |
| Every story `*(headline only)*`, no summaries | An LLM node is 400ing silently (On-Error-Continue) — a sampling param on an Opus model, a malformed body, or exhausted balance | Open the execution → failing HTTP node → response. All bodies must be Expression `{{ JSON.stringify($json._llm_body) }}` with NO `temperature`; check console.anthropic.com balance |
| `Method Not Allowed` / 405 on an LLM node | The HTTP node's **Method** is still n8n's GET default — Anthropic and Voyage are POST-only | Set **Method: POST**. Applies to the three Anthropic nodes (Triage/Rescore/Summarise) AND the Voyage `Embed` node (15d) |
| `Bad request … zero-length document` on an LLM node | POST set but **Send Body** OFF / JSON field empty (GET-built node) | Send Body ON → JSON → Using JSON → Expression → the card-14a paste |
| Ticker stories missing thesis wikilinks | `cfg.ticker_files` empty (Tickers command failed) or feedId prefix mismatch | Check Tickers stdout; wikilinks only attach to `tk-*` member stories |
| Same story re-briefed across runs/days | PriorStories (2b) broken (nothing to compare against) OR `repeat_threshold` too high | SemCluster's funnel note should read `… (K cross-run repeats)` with K>0 when follow-ups exist; confirm `PriorStories` stdout is non-empty; LOWER `repeat_threshold` toward 0.85 if reruns leak through; widen `story_memory_days` for a longer memory |
| Registry prompt edit has no effect | `####` header misspelled or required token deleted (`{items}`; cluster also `{prior}`) — Plan silently reverted to `DEF_P` | §5.1 check 9's third grep must return 4; restore the exact header/token |
| Real development buried in ♻ Follow-up coverage | `repeat_threshold` too low — an advancing story looks too similar to its prior | RAISE `repeat_threshold` toward 0.92; the ♻ link is kept either way — nothing lost, only unsummarised |
| Funnel note `semcluster:embed-failed → no dedup this run` | Voyage call failed (On-Error-Continue) — bad key, rate limit, or malformed body | Open the `Embed` (15d) execution → response; check the Voyage credential (`Authorization: Bearer …`) and that `_emb_body` is valid JSON. Run degrades to singletons (no dedup), never dies |
| Every item a singleton, no merging ever (but Embed shows 200) | SemCluster reading the wrong response field | Voyage returns `{data:[{embedding:[…],index:0},…]}`; SemCluster reads `$input.first().json.data` — if n8n nested it (e.g. under `body`), adjust that path |
| Distinct stories wrongly merged into one | `sim_threshold` too low | RAISE `sim_threshold` toward 0.90 (the primary dial); a specific stubborn pair is genuinely close — accept or raise further |
| Run hangs at PreBody or Rejoin | A zero-item branch starved a Merge (quiet/all-bypass/zero-body day) | Verify TriagePrep's guaranteed-batch line + Always Output Data ON for Admit + Final; last resort, wire 16-true through a pass-through Code node as branch-keeper |
| Search loop stops partway; `done` never fires | A zero-result/rate-limited query returned `[]` — the empty loop-back froze Loop Over Items (routine on weekends) | Always Output Data ON on GParse (8.3) + BParse (9.3); re-run |
| Normalize (+ chain) ran 3–5× in one run; partial digests or null-body 400 | Multi-wire per-branch execution — confirmed on this instance | 6b FeedTasks + 10b PreNormalize Merges must exist and carry ALL listed wires (§5.4) |
| PreNormalize shows thousands but Normalize outputs only the sentinel; stages sprint in seconds | A leftover pre-10b direct wire into Normalize fired it early on a near-empty delivery | Normalize must have EXACTLY ONE inbound wire (from PreNormalize) — count on the canvas, delete extras |
| `normalize:dropped:N badurl:` on obviously VALID URLs | The Code node used `new URL()` — the **URL global doesn't exist in this sandbox** (it zeroed a 30k run) | Card 11's canon/hostOf are pure regex for this reason; never use `new URL()` in a W3 Code node |
| `normalize:dropped:N keys:…` | Normalize met an unclassifiable item shape (the sample names its keys) | Match the keys against card 11's branches; extend the link-field fallbacks |
| `Referenced node doesn't exist` (may wrap as `Cannot assign to read only property 'name'`) | A `$('Name')` lookup doesn't match any node title — the misnamed node sat harmless until this branch first carried items | Rename the node to the exact carded name (rename the node, not the code); audit load-bearing names (§5.3 convention note) |
| `Channels: … fmp 0` + `401 Invalid API KEY` | n8n FMP credential holds a stale key (check 7 tests `.data/config.json`, which can differ) | Update the n8n FMP credential to match `.data/config.json` (Query Auth, param `apikey`) |
| A specific **US** ticker never appears in the FMP lane | Filename prefix ≠ exchange ticker — FMP `news/stock` returns 0 for an unknown symbol (e.g. KLA, real symbol KLAC) | Add the mapping to `FMP_ALIAS` in card 5's Plan (`{ KLA:'KLAC', … }`); confirm with `curl …/stable/profile?symbol=<TICKER>` → `NOT FOUND` means wrong symbol |
| A **foreign-listed** ticker never appears in the FMP lane | By design — FMP `news/stock` is US-symbol-only; Amsterdam/London/Tokyo/etc. don't resolve | Not an FMP fix — those names are covered by the GN/GDELT/Brave company-name queries (Plan uses the thesis filename's company name for those channels) |
| FMP items feel capped / a busy ticker crowds out quiet ones | `news/stock` returns ≤250 newest **across the batch**, recency-sorted — not per-ticker | 250 is the hard endpoint ceiling; lower `FMP_CHUNK` only if a batch's busy names starve quiet ones (coverage is otherwise chunk-independent) — the date window already keeps the 250 in-scope |
| Nearly every story `*(headline only)*` but summaries ARE present | Story mix is Google-News-dominated (GN redirect URLs are body-exempt) — usually because GDELT/Brave/FMP contributed 0 | Check the `Channels:` line; restore the zero channels |
| `expects a number but we got '8'` on a number field | n8n strict type validation — expression results can arrive as strings | Wrap in `Number(…)` with a `\|\| <default>` fallback (card 8.4 Pace is the known case) |
| Same story appears as two entries in ONE brief | Embeddings `sim_threshold` too high — the two vectors landed just below it | LOWER `sim_threshold` toward 0.82 (primary dial); SumPrep's Jaccard `merge_jaccard` backstop catches lexically-near twins — lower it toward 0.35 as the second lever |
| A feature behaves as if absent (output field missing entirely from a node's execution) | **Deployed-node drift** — the node runs an older paste; doc edits never auto-sync | The missing field NAMES the stale node; re-paste that card. After any code round, resync every changed node |
| "Number of entries exceeded cap"; run dies at Dedupe | The old Remove Duplicates node is still there — count-cap overflows from GN URL churn | Replace with the card-12 **Code "Dedupe"** (TTL-bounded static store) — architecture fix, not a setting |
| Re-test comes up empty (Dedupe kills everything) | Card-12 static store holds URLs from a run <`dedup_ttl_d` days ago | Rare since the TTL rebuild; force-reset with a one-line Code node `$getWorkflowStaticData('global').seenUrls = {}` |
| Debugging needs fast iterations | Full runs cost ~30 min in GDELT/Brave pacing | Detach the 4 GDELT/Brave wires (Route 2/3 → loops, both `done` → PreNormalize in3/in4 — delete at the Merge end too); run = RSS+FMP+LLM ≈ 3–5 min; re-attach per §5.4 |
| Telegram send fails | >4,096 chars | Capped at 3,900/message; check multi-byte overflow or lower `tg_max_msgs` |

### 12.2 X workflows (W4 Canary / W5 Harvester) & platform

| Symptom | Cause | Fix |
|---|---|---|
| Scheduled workflow silently produces nothing | Disambiguate via Executions list: **no row + workflow edited recently** = the edit silently dropped the schedule trigger (n8n keeps `active=1` but doesn't re-arm the cron — confirmed 07-21 on W5) → **toggle Active OFF→ON**; **no row + not edited** = never fired (Mac asleep — `pmset -c sleep 0`, §1.4); **row ran fast, no output** = quiet-path gate false (legitimate) OR silent LLM failure | Re-register via the Active toggle; else open the execution and check the LLM node |
| Execution `startedAt` looks offset by hours | DB stores `startedAt` in **UTC** — convert to local (Sydney = UTC+10) before judging schedule times. Scheduler TZ is `GENERIC_TIMEZONE` (in the pm2 dump); to apply a dump-env change to the *running* process: `pm2 delete n8n && pm2 resurrect` | — |
| Node params show POST but execution ran GET | Execution is a historical snapshot — the POST edit postdates the run, or the workflow wasn't **saved** | Re-save, re-Execute, read the FRESH execution. If still GET, check the URL for a trailing space/slash (3xx downgrades POST→GET) |
| X internal churn breaks provider (every few weeks) | Watchdog (hard errors) / Canary (empty results) | Wait for provider patch; Canary is the early-warning |
| Silent thin results | Canary | Check provider status; fallback twin socialdata.tools (~30 min swap) |
| Anthropic API failure (W5) | On-Error-Continue on Sentiment node | Dashboard renders "LLM unavailable"; harvest unaffected. Open the Sentiment node's output for the real error |
| W5 `400 … "no low surrogate in string"` → dashboard "LLM unavailable", all sentiment `—`, run ~26s | A tweet's emoji (a UTF-16 surrogate PAIR) got cut in half by a fixed-length `.slice()` in the Analyze node → lone `\uD8xx` → invalid JSON → Anthropic 400s the whole Sentiment call | Analyze node strips lone surrogates from the payload content (the `.replace(/[\uD800-\uDBFF](?![\uDC00-\uDFFF])…/g,'')` on line ~1920). If W3's LLM calls ever 400 the same way, apply the identical strip to that payload builder |
| State file corrupted/deleted | try/catch fallback to `{}` | Cold restart; sharp again in 2 pulls — disposable by design |
| `_catalyst.md` stale | Workflow 2 staleness nag | Catalyst matching degrades to "none" |
| Provider dies commercially | Canary + top-up failure | Balance ≤$5 caps the loss |
| Hung-run collision (a stuck run still "running" at next schedule) | No per-run timeout | Set Workflow Settings → **Timeout** (W3: 5400s) |
