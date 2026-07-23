---
date: 2026-07-17
tags: [meta, infrastructure, automation]
status: superseded
superseded_by: n8n Automations.md (merged 2026-07-19)
---

# n8n Automation Layer — Setup Tutorial & Cost/Benefit

n8n (self-hosted, free) is the vault's **sensory layer**: always-on acquisition, scheduling, and alerting upstream of `/ingest`. The vault today is pull-based — nothing enters `_Inbox/`, no skill runs, no thesis observable gets checked unless Alex acts. Evidence of the gap: [[_catalyst.md]] went 55 days stale (generated 2026-05-23) while its own window ran through 2026-08-21; [[Theses/MRVL - Marvell Technology.md]] carries five dated "first confirming observables" that nothing watches between sessions.

**Division of labor (non-negotiable):**

| Layer | Does | Never does |
|---|---|---|
| n8n | Deterministic acquisition, cron scheduling, threshold alerts, relevance triage | Judgement — it has no mental-models context, no thesis state |
| Vault skills | All analysis, propagation, conviction | Watching the world between sessions |

**Four hard rules** (extend CLAUDE.md change-safety into the automation layer):

1. **n8n writes only NEW files, only into designated output locations** — `Daily Intel/` (dashboard snapshots + daily digests: scanning surfaces, not ingest candidates), `.data/` (machine state), `_Inbox/` (true ingest candidates only). Never Theses/, Research/, metadata files, `_Inbox/processed/`, or any existing file. Anything meant for the research pipeline still flows through `/ingest` exactly like a manual web clip — you paste the links worth ingesting.
2. **Triage yes, analysis no.** n8n AI nodes may relevance-score feed items before deposit. They never summarise, conclude, or write analytical prose — context-free analysis entering the vault laundered as source material is the failure mode. *Sole user-approved exception:* Workflow 5's sentiment layer — **read-vault yes, write-vault no**: it reads thesis sections to compare against crowd posts, and its output lands only in the dated dashboard snapshot in `Daily Intel/`, never in Theses/Research or propagation (Twitter API Build §2.7).
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
| FMP | HTTP Query Auth (`apikey` param) | Copy the key from `.data/config.json` (same one Watchlist / Live Portfolio / skills use) | Workflow 1 — Price Tripwires |
| twitterapi.io | Header Auth (`X-API-Key`) | twitterapi.io dashboard — Twitter API Build §3.1 | Workflows 4–5 |
| Anthropic | Header Auth (`x-api-key`) | console.anthropic.com — separate billing from the Claude Code subscription | Workflow 5 sentiment layer; optional Workflow 3 triage (works unscored without it) |

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

### 2.35 The watcher registry — one file controls everything pulled

**The single most important design decision for keeping this maintainable.** What n8n pulls must NOT live inside n8n's workflow code — every change would mean opening n8n, editing a Code node, saving. Instead, all criteria live in one vault file, [[_watchers.md]], and each workflow reads it on every run. The workflow is built once and never edited again; adding/removing a watch is a markdown-table edit that takes effect on the next scheduled run with no redeploy or restart.

**Schema** (sectioned by consuming workflow — one file, one place to look):

| Section | Drives | Columns |
|---|---|---|
| News & Thematic | Workflow 3 — one RSS query per row | `id, query, thesis, expires, status` |
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

### 2.6 Ticker universe (used by Workflow 3's weekly per-ticker sweep)

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

**Build:**
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

**Build:**
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

---

### Workflow 3 — News Sweep (thematic watchers + optional AI triage)

**What:** 2×/day active search across your thesis themes, deduped across runs, optionally relevance-scored, aggregated into **one daily digest** in `_Inbox/`.

**Mechanism (important):** `news.google.com/rss/search?q=<QUERY>` is Google News's **search-as-RSS** endpoint — NOT your personal Google feed. n8n re-runs each query fresh on every cron tick, so each [[_watchers.md]] row is a *saved search that re-executes on schedule*. Returns headline + snippet + link (not full article); rate-limits under load. Heavier coverage → swap the source node for a news API (GDELT free; NewsAPI/Brave free tiers) with the same downstream chain.

| | |
|---|---|
| Build effort | 3–5 h + query tuning over first two weeks |
| Running cost | $0 without triage; ~$2–8/mo with Haiku triage (~100–200 items/day scored) |
| Maintenance | ~30 min/mo — feed rot, query drift, threshold tuning |
| Benefit | **Medium.** Breadth and latency, but the noise risk is real — unmanaged, this pollutes `_Inbox` and burns `/ingest` runs. The differentiated version: **window-scoped observable watchers** — queries that exist only while a thesis observable is live |
| Status | **Live** — 07:00 + 17:00 digests |

**Build:**
1. **Schedule Trigger** — two rules, 7am and 5pm (the Schedule node rejects multi-time cron like `0 7,17 * * *`) → **Read/Write Files** (`_watchers.md`) → **Extract from File** → **Code** (the §2.35 parser) emitting one RSS URL per active, unexpired row of the News section. Queries live in [[_watchers.md]], never in this node — that is what makes "add TSMC / drop TSMC" a table edit instead of a workflow edit. The seed rows already encode live MRVL observables (fabric war → OCP Oct window, Trainium → re:Invent window) alongside standing themes (HBM4, TSMC capex).
2. **RSS Read** (URL from expression) → **Remove Duplicates** (cross-execution, key: link).
3. Optional triage: **Basic LLM Chain** + Anthropic credential (Haiku): *"Score 0–10 relevance to: custom silicon (MRVL/AVGO), HBM/memory, semicap, photonics/CPO, scale-up fabrics (UALink/NVLink/ESUN), CXL/memory disaggregation, AI datacenter power. Return JSON {score, tickers, reason}."* → **Filter** score ≥ 7. Scoring only — no summarisation (Rule 2).
4. **Code** — one digest: title, source, link, feed description (verbatim, not LLM), triage score → deposit `YYYY-MM-DD - News digest - n8n.md` into `Daily Intel/` (moved from `_Inbox` 2026-07-18 — digests are scanning surfaces, not ingest candidates) → **Telegram** one-line count.

**Workflow intent:** the digest is a *scanning surface*. You pick the 1–3 links worth full `/ingest` (paste URL as usual). Auto-ingesting news bodies wholesale would create junk Research notes and pollute propagation — deliberately not built.

**Optional — weekly per-ticker coverage sweep.** Thematic queries miss company-specific news for tickers not covered by a theme. Add a second Schedule Trigger (weekly, Monday 08:00) that reads the §2.6 ticker universe, runs one `"<Company>" stock` search per ticker, and appends to the same weekly digest. Weekly + digested (never per-item, never daily) keeps it from flooding `_Inbox`. This gives complete coverage without daily ticker-carpet-bombing.

---

### Workflows 4–5 — X Canary + X Harvester (Twitter intelligence)

X/Twitter intelligence system: all-thesis cashtag harvesting (auto-derived) + AI-curated terms via `_watchers.md § X Watchers`, daily pull cadence, engagement-delta trending detection (→ `Daily Intel/` + Telegram), and dated Obsidian-native dashboards in `Daily Intel/` (newest file = current dashboard) with Opus-graded sentiment, per-theme crowd perspectives, **thesis-divergence detection**, and `_catalyst.md` matching. [[Twitter API Build]] is the complete guide — architecture review, then click-level build cards for **Workflow 4 — X Canary** (daily provider-health probe; built first) and **Workflow 5 — X Harvester** (the engine; daily, 08:30). **Live since 2026-07-18**: ~$17–40/mo all-in (twitterapi.io ~$2–5 + Anthropic Opus ~$15–35; `llm_model` row is the cost lever). Official X API ruled out (cost + no server-side engagement operators).

---

## 4. What NOT to automate — summary

| Never | Why |
|---|---|
| Direct writes to Theses/Research/Sectors/Macro | Bypasses quality gate, idempotency keys, wikilink-form contract, `propagated_to:` atomicity — the exact failure classes [[INFRASTRUCTURE]] exists to prevent |
| LLM analysis inside n8n | Context asymmetry: no mental models, no READING PROTOCOL, no thesis state. Triage-scoring only — sole exception: Workflow 5's read-only sentiment/divergence layer, dashboard-output only (hard rule 2) |
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
| Local secrets + state — `.data/` | gitignored on purpose | recreate by hand: `config.json` is one line (FMP key); X-harvester state is reseeded per Twitter API Build §3.3 — do NOT copy it, it's disposable and sharp again in 2 pulls |
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
| 3 | News Sweep | 07:00 + 17:00 | 0–8 (optional triage) | **Live** |
| 4 | X Canary | daily 08:00 | ~0 | **Live** — [[Twitter API Build]] §3.4 |
| 5 | X Harvester | daily 08:30 | ~17–40 | **Live** — [[Twitter API Build]]; dated history in `Daily Intel/` |
| — | Error Watchdog | fires by reference | 0 | **Live** — set as Error Workflow in every workflow |

**Totals:** software $0 (n8n Community, fair-code, internal use) · hard running cost typically ~$20–35/mo (Opus daily is the dominant line; `llm_model` registry row is the lever) · ongoing maintenance ~30 min/mo (§5 monthly review).
