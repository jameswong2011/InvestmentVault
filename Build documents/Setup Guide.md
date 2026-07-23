---
date: 2026-07-19
tags: [meta, infrastructure, how-to, setup]
status: active
---

# Setup Guide — Zero to Working Vault

> End-to-end replication guide: from a blank machine to the full working system — vault, Claude Code, Claudian, skills, data layer, and the n8n automation stack. Written to be followed top-to-bottom with no prior knowledge. Every step says what you did it for and how to verify it worked.
>
> **Scope boundaries.** Daily operation: [[User Guide]]. Consistency-machinery internals: [[INFRASTRUCTURE]]. Automation layer deep-dive: [[n8n Automations]]. This document owns *installation and configuration only*.

---

## 0. What you're building

Four layers, installed in this order:

| Layer | What it is | Source | Sections |
|---|---|---|---|
| **1 — Vault content + config** | The Obsidian vault: theses, research, mental models, skills, templates, plugins | `git clone` — almost everything ships in the repo | §2–§4 |
| **2 — Claude Code + Claudian** | The agent runtime (CLI) + the Obsidian plugin that hosts it in a chat panel | Installed per machine; plugin ships in the repo | §2, §6 |
| **3 — Data layer** | FMP API key powering `/numbers`, `/transcript`, Live Portfolio | One JSON file, recreated by hand (gitignored) | §7 |
| **4 — Automation (optional)** | n8n + Telegram + X harvesting: the always-on "sensory layer" upstream of `/ingest` | Built per machine following [[n8n Automations]] | §8 |

Layers 1–3 take ~30–45 minutes. Layer 4 is optional and takes ~3–5 hours the first time; the vault is fully functional without it.

---

## 1. Accounts & subscriptions

Open these accounts before starting. Required = the core vault won't work without it.

| Account | Needed for | Cost | Required? |
|---|---|---|---|
| **GitHub** | Cloning the vault repo | Free | ✅ |
| **Anthropic — Claude subscription** (claude.ai, Pro or Max) | Claude Code login (the agent runtime) | Pro ~$20/mo, Max more | ✅ (or API-key billing below) |
| **Obsidian** (obsidian.md) | The app is free; an account is only needed for Obsidian Sync | Free; Sync optional add-on | App ✅ / account ⚪ |
| **Financial Modeling Prep** (financialmodelingprep.com) | `/numbers`, `/transcript`, Live Portfolio refresh, n8n Workflow 1 | Paid plan with API access | ⚪ strongly recommended |
| **Anthropic — Console API** (console.anthropic.com) | n8n Workflow 5 LLM layer (+ optional Workflow 3 triage). **Prepaid credits, billed separately from the Claude subscription** | ~$15–35/mo at daily cadence | ⚪ only for Layer 4 |
| **twitterapi.io** | X/Twitter data for Workflows 4–5 (official X API ruled out — see [[n8n Automations]] §9.1) | ~$2–5/mo, $5 top-ups | ⚪ only for Layer 4 |
| **Telegram** | Alert channel for every n8n workflow | Free | ⚪ only for Layer 4 |

Keep every key you generate in a password manager. §4 says exactly where each one lives on disk; none are committed to git.

---

## 2. Install the core tools (macOS)

The stack is macOS-first (paths like `/opt/homebrew/bin` and the launchd/pm2 autostart assume it). Windows/Linux equivalents exist for everything except the §8 Mac-sleep handling — adapt paths accordingly.

### 2.1 Homebrew, git, Node

```bash
# Homebrew (skip if installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install git node
git --version && node --version   # verify: any recent versions are fine
```

Node here is for Claude Code only. The n8n layer needs Node **22 LTS via nvm** specifically — installed separately in §8, don't worry about it now. `python3` (needed by the skill helper scripts) ships with macOS; if `python3 --version` fails, `brew install python3`.

### 2.2 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version        # verify: prints a version (reference machine: 2.1.212)
which claude            # note this path — Claudian needs it in §6 (typically /opt/homebrew/bin/claude)
```

Alternative: the native installer (`curl -fsSL https://claude.ai/install.sh | bash`) — either works; note whichever binary path results.

Then authenticate:

```bash
claude   # any directory; first launch opens the login flow
```

Log in with the **claude.ai subscription** (recommended — flat-rate) or an API key (usage-billed). Exit with `Ctrl+C` after login succeeds.

### 2.3 Obsidian

1. Download from `https://obsidian.md` → drag to Applications → open.
2. Stop at the vault-picker screen — the vault comes from git in §3, don't create one.

---

## 3. Clone the vault

```bash
cd ~   # or wherever you keep it; reference machine uses the home directory
git clone https://github.com/jameswong2011/InvestmentVault.git
cd InvestmentVault
ls Theses/ | head    # verify: thesis notes appear
```

Private repo → authenticate with a GitHub personal access token or the `gh` CLI (`brew install gh && gh auth login`).

---

## 4. What git gives you vs. what you recreate

The single most important section. The repo carries everything shareable; three categories of files do NOT come down with the clone and behave differently.

### 4.1 Lifted from GitHub (do nothing — verify presence)

| What | Where | Notes |
|---|---|---|
| All content | `Theses/`, `Research/`, `Sectors/`, `Macro & Technology/`, `Mental Models/`, `Templates/` (incl. `_callouts/`), `Canvas/`, `Thesis Breakdowns/`, `_Archive/`, `_Inbox/` | The knowledge base itself |
| Agent instructions | `CLAUDE.md` (canonical), `AGENTS.md` (generated Codex mirror) | Tier 1 protected — edit only deliberately |
| All 21 skills + shared contracts + helper scripts | `.claude/skills/**` (`SKILL.md`, `RATIONALE.md`, `_shared/*.md`, `*.py`) | The entire behavioral layer |
| Claude Code project config | `.claude/settings.json` (136-entry permissions allowlist), `.claude/agents/vault-explorer.md` | Fewer permission prompts out of the box |
| Obsidian shared config | `.obsidian/`: `community-plugins.json`, `core-plugins.json`, `hotkeys.json`, `app.json`, `appearance.json`, `snippets/pinned-marker.css`, `graph.json` | Callout hotkeys ⌘⌥1–4 pre-bound |
| **All 5 community plugins, binaries included** | `.obsidian/plugins/`: `realclaudian` (Claudian 2.0.x), `templater-obsidian`, `dataview`, `obsidian-git`, `obsidian42-brat` + Templater's `data.json` and BRAT's beta-registry | No marketplace installs needed — only enabling (§5) |
| Metadata layer | `_hot.md`, `_graph.md`, `_catalyst.md`, `_followups.md`, `_watchers.md`, `.archive_ticker_registry.md`, `Live Portfolio.md`, `Watchlist.md` | Arrives populated from the source vault |
| Codex support (optional runtime) | `.agents/` (generated skill tree + `port_claude_skills.py`), `.codex/agents/*.toml` | Only relevant if using the Codex provider |
| Build documents | `Build documents/*.md`, `setup-vault.sh`, `.gitignore`, `.gitattributes` | This guide included |

### 4.2 Gitignored — recreate by hand (the complete list)

| File / dir | Contains | How to recreate | Consumed by |
|---|---|---|---|
| `.data/config.json` | FMP API key: `{"fmp_api_key": "YOUR_KEY"}` | §7.1 (or `bash setup-vault.sh` scaffolds the placeholder) | `/numbers`, `/transcript`, Live Portfolio refresh button, n8n Workflow 1 |
| `.data/x_engagement_state.json` | X harvester tweet DB (machine-local, disposable) | Seeded by [[n8n Automations]] §9.3 — only when building Layer 4 | n8n Workflow 5 |
| `.claudian/` | Claudian plugin settings + chat session history | Reconfigure in the settings UI (§6) — 5 minutes | Claudian plugin |
| `.claude/settings.local.json` | Machine-local Claude Code overrides | Auto-created on demand; nothing to do | Claude Code |
| `.obsidian/workspace.json` (+ mobile/cache) | Open tabs, pane layout | Auto-created when Obsidian opens the vault | Obsidian |
| `.env`, `*.key`, `credentials.json`, etc. | Secret patterns, defensively ignored | Nothing currently uses them at the vault root | — |

**Secrets that live entirely outside the repo folder** (recreated per machine, never in git): Claude Code login (`~/.claude`), n8n's credential store + SQLite DB (`~/.n8n` — the ONE unrecoverable-if-lost artifact; back it up per [[n8n Automations]] §5, transport by AirDrop/USB only per §5.1), Telegram bot token, twitterapi.io + Anthropic API keys (live only inside n8n credentials).

### 4.3 Runtime state — let the system create it (NEVER create by hand)

Ephemeral gitignored markers owned by the skills ([[INFRASTRUCTURE]] §2): `.last_sync`, `.sync_all_fresh`, `.graph_invalidations`, `.vault-lock*`, `.rename_incomplete.*`. They appear on their own as skills run. In particular do **not** `touch .last_sync` to "skip" the slow first sync — that silently marks all pending files as already-synced (User Guide §13).

Also machine-generated, intentionally left out of a fresh clone: `Daily Intel/` dashboards and n8n digest files — the pipeline regenerates them (§8).

> **Quirk worth knowing**: `.gitignore` lists `.claude/settings.json`, but the file was committed before the rule was added, so it IS tracked and ships with the clone (gitignore never applies to already-tracked files). Don't `git rm --cached` it — you'd silently strip the permissions allowlist from every future clone.

---

## 5. First Obsidian launch

1. Obsidian → **Open folder as vault** → select the cloned `InvestmentVault` folder.
2. The restricted-mode banner appears (vault contains community plugins) → **Turn off restricted mode** → **Enable community plugins**.
3. Settings → **Community plugins** → confirm all five show enabled: **Claudian**, **Templater**, **Dataview**, **Git**, **BRAT**. Toggle on any that aren't.
4. Restart Obsidian once (lets BRAT run its startup update check — it tracks `YishenTu/claudian` and keeps the Claudian plugin current automatically).

**Verify Layer-1 config arrived via git** (all pre-configured, nothing to set up — this is the "later clones inherit" promise of User Guide §6):

| Check | Expected |
|---|---|
| Open any thesis → press `⌘⌥1` | A dated `> [!question]` callout inserts at cursor with today's date |
| Settings → Templater → Template folder | `Templates`, with folder templates mapped for `Theses/`/`Research/` |
| Settings → Appearance → CSS snippets | `pinned-marker` ON |
| Settings → Hotkeys → search "callouts" | Four Templater bindings on `⌘⌥1`–`⌘⌥4` |

If any check fails (typical only when assembling a vault from scratch rather than from this clone): Templater → **Template folder location** `Templates` + enable **Automatic jump to cursor** → **Template Hotkeys** → add the 4 files in `Templates/_callouts/`; then Hotkeys → search `Templater: _callouts/user-<type>` → bind `⌘⌥1`–`⌘⌥4`. Commit `.obsidian/hotkeys.json` + `.obsidian/plugins/templater-obsidian/data.json` so later clones inherit.

**Obsidian Sync note** (optional): core Sync is enabled in the config. If you use it, it syncs *content* to mobile but not dot-folders (`.claude/`, `.claudian/`, `.data/`, most of `.obsidian/`) — **git remains the real transport between desktops**. Skip Sync entirely if you only work on one machine.

**Obsidian Git note**: the obsidian-git plugin is installed but not configured for auto-commit — commits are user-initiated by design (skills never commit). Leave it that way unless you consciously want auto-backup commits.

---

## 6. Configure Claudian

Claudian's settings are machine-local (`.claudian/` is gitignored) — this is the one piece of UI configuration every new machine needs.

1. Open the Claudian panel (right sidebar) → gear icon.
2. **CLI path**: if Claudian doesn't auto-detect the Claude binary, paste the path from §2.2 (`which claude`, e.g. `/opt/homebrew/bin/claude`). This is stored per-device — expected to be re-entered on each machine.
3. Set to taste (reference config): **user name** (how Claude addresses you) · **model** `sonnet` for mechanical sessions, switch up for heavy analysis · **permission mode** — start with `acceptEdits`; relax later once you trust the flow · **chat placement** right sidebar.
4. Send a test message: *"Read [[_hot.md]] and summarise the active research thread."* A correct reply proves: CLI found → login valid → vault-root working directory → CLAUDE.md loaded.

Codex provider (optional): Claudian can also drive OpenAI Codex CLI using the same vault — `AGENTS.md` + `.agents/skills/` (generated mirrors of CLAUDE.md + `.claude/skills/`) ship in the repo. Install the Codex CLI, enable the provider in Claudian settings, done. After ever editing canonical skills, regenerate the mirror: `python3 .agents/port_claude_skills.py`.

---

## 7. Bootstrap the vault

### 7.1 Scaffold local files

```bash
cd ~/InvestmentVault
bash setup-vault.sh
```

The script is idempotent and non-destructive: verifies tooling, creates the untracked working dirs (`Daily Intel/`, `_Inbox/processed/`, `.data/`), and writes a placeholder `.data/config.json` if absent. Then put your real FMP key in:

```bash
open -e .data/config.json    # replace YOUR_FMP_KEY_HERE with the actual key
```

Format (exactly this shape): `{"fmp_api_key": "..."}`.

### 7.2 First-run metadata bootstrap

In Claudian (or `claude` in a terminal at the vault root):

```
/sync        # establishes the .last_sync watermark; reads all vault files
/graph       # full rebuild of _graph.md against this clone
```

Expectations: the first `/sync` re-reads **everything** — on a populated vault this is the 5–10× slow path and is *correct* (it establishes the watermark baseline; User Guide §13). Every later `/sync` is incremental. Without this bootstrap, `/sync TICKER` and scoped `/surface` block (they need a fresh `_graph.md`).

### 7.3 Smoke-test the data layer

```
/numbers NVDA        # any active ticker — verifies the FMP key end-to-end
```

Key missing/invalid → the skill aborts gracefully and tells you; fix `.data/config.json` and re-run.

**Layers 1–3 complete.** The vault is fully operational for daily use ([[User Guide]] takes over from here). Everything below is the optional automation layer.

---

## 8. Layer 4 — n8n automation stack (optional)

The always-on acquisition tier: price tripwires, catalyst reminders, news sweeps, X/Twitter harvesting — all feeding `_Inbox/`, `Daily Intel/`, and Telegram, all controlled from one vault file (`_watchers.md`, which ships in the repo already populated). **Exactly one machine runs this stack** — never two clones concurrently.

Work through [[n8n Automations]] *in this order* (it is click-level; this guide only sequences the sections):

| Step | Doc + section | What you build | Time |
|---|---|---|---|
| 1 | [[n8n Automations]] §1 | Node 22 LTS via nvm, n8n Community Edition (npm, not Docker), pm2 keep-alive + autostart, Mac-sleep `pmset` handling, timezone env | ~45 min |
| 2 | [[n8n Automations]] §2 | Telegram bot (BotFather), credential store, **Error Watchdog first**, `_Inbox/` deposit contract, ticker-universe extraction | ~1 h |
| 3 | [[n8n Automations]] §3 | Workflows 1–3: Price Tripwires, Catalyst Reminders, News Sweep | ~1–2 h |
| 4 | [[n8n Automations]] §9.1–9.2 | twitterapi.io + Anthropic Console accounts, n8n credentials, verification calls (don't skip — §9.2 is the gate that catches provider field-drift) | ~45 min |
| 5 | [[n8n Automations]] §9.3–9.7 | Seed `.data/x_engagement_state.json`, Workflow 4 (X Canary), Workflow 5 (X Harvester, 23 nodes) | ~1.5–2 h |
| 6 | [[n8n Automations]] §9.8 | Two-week calibration of the trending-engine thresholds | passive |

Notes for a fresh replica:
- The n8n workflows exist only in the source machine's `~/.n8n` database — **they are not in the git repo**. Either rebuild them from the build cards (the docs are written for exactly this), or have the source machine export each workflow as JSON (n8n UI → workflow → Export) and import; store exports in `_Archive/n8n-workflows/` if you want them versioned.
- All tuning thresholds live in `_watchers.md § X Watchers → ### Tuning` (vault data, ships via git) — a rebuilt workflow picks up the source vault's calibrated values automatically. Code-node fallback defaults only fire if the table is damaged.
- Migrating the stack later (new laptop): [[n8n Automations]] §5.1 is the complete four-layer runbook.

---

## 9. Full verification checklist

Run top to bottom; every line should pass before calling the setup done.

| # | Check | Pass looks like |
|---|---|---|
| 1 | `claude --version` in terminal | Version prints |
| 2 | Obsidian → 5 community plugins enabled | Claudian, Templater, Dataview, Git, BRAT |
| 3 | `⌘⌥1` in a note | Dated `[!question]` callout inserts |
| 4 | Claudian test message (§6.4) | Reply references `_hot.md` content |
| 5 | `/sync` then `/graph` completed once | `.last_sync` exists at vault root; `_graph.md` frontmatter `last_graph_write:` is today |
| 6 | `/numbers TICKER` | Key Metrics table refreshes (or graceful no-key abort if you skipped FMP) |
| 7 | `/lint` | Report runs; no Critical findings (Important findings about the source vault's content are normal) |
| 8 | *(Layer 4)* `pm2 status` | `n8n` online; `localhost:5678` loads |
| 9 | *(Layer 4)* Telegram | Canary/watchdog messages arrive on schedule |
| 10 | *(Layer 4)* next morning | New dated dashboard in `Daily Intel/` |

---

## Appendix — `.gitignore` inventory (what each ignore rule protects)

| Rule(s) | Why ignored |
|---|---|
| `.obsidian/workspace*`, `.obsidian/cache`, `.trash/` | Personal UI state — differs per machine, churns constantly |
| `.claudian/` | Claudian settings + full chat history — machine-local, contains session content |
| `.claude/settings.local.json`, `.claude.json.backup` | Machine-local Claude Code overrides |
| `.last_sync`, `.sync_all_fresh`, `.graph_invalidations`, `.vault-lock*`, `.rename_incomplete.*` | Skill runtime markers — committing a live lock would block every machine that pulls ([[INFRASTRUCTURE]] §2, §11) |
| `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.json` | Defensive secret patterns |
| `.data/` | FMP key + X harvester state — the repo can go public; this folder stays local |
| `.DS_Store` etc., `Thumbs.db` etc., `*.tmp`/`*.swp`/`~$*` | OS + editor noise |
| `/*.zip` (root only) | Bulk exports; `_Archive/Backups/*.zip` stays tracked |
| `.claude/settings.json` *(listed but tracked — see §4.3 quirk)* | Vestigial entry; file ships with the repo |

Intentionally **not** ignored despite being dot-files: `.archive_ticker_registry.md` (append-only archive ledger), `.drift-config.md` (optional drift tuning) — both are persistent content, not runtime state.
