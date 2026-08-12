# Claudian Investment Vault — An LLM Wiki for equity research (v6)

*Updated 2026-08-07 from live vault state.*

## Contents

- §1 An LLM Wiki for equity research
- §2 The vault by the numbers
- §3 Four engines
- §4 Mental Models
- §5 State files
- §6 Architecture map
- §7 Templates & writing standards
- §8 The thesis structure
- §9 Skills (27)
- §10 Multi-agent workflows
- §11 The n8n layer
- §12 Safety machinery
- §13 Publishing
- §14 A day in the life
- §15 Workflow chains
- §16 Inline callouts
- §17 FAQ
- §18 Glossary
- [Repo](https://github.com/jameswong2011/InvestmentVault)

---

## §1 · An LLM Wiki for equity research

In April 2026 Andrej Karpathy described a pattern for LLM-maintained knowledge bases: instead of asking a model questions and letting it rediscover the answers each time, have it compile raw sources into a structured wiki that grows with every source added. This vault applies that pattern to one job: non-consensus equity research that compounds over years.

> "The LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources... The knowledge is compiled once and then *kept current*, not re-derived on every query."
> — Andrej Karpathy, [llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · April 2026

RAG retrieves chunks at query time; nothing accumulates. Compilation builds the cross-references, contradictions, and synthesis once, then keeps them current.

### The three layers

| Layer | In this vault | Who writes it |
|---|---|---|
| **Raw sources** (immutable) | `_Inbox/`, `Daily Intel/` (machine-harvested), APIs (FMP, X, GDELT, Brave), your inline callouts | You + the n8n pipeline. Claude never modifies. |
| **The wiki** (LLM-maintained) | `Theses/` `Research/` `Sectors/` `Macro & Technology/` + state files (`_hot.md`, `_graph.md`, …) | Claude, through 27 skills |
| **The schema** (contract) | `CLAUDE.md`, `Templates/`, `.claude/skills/` + 11 shared contracts | You, rarely |

Karpathy's metaphor: Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase. You pick sources, ask questions, and make the final calls. Claude does the maintenance.

A fourth layer runs underneath: hooks, scheduled runs, a 24/7 ingestion pipeline, multi-agent orchestration, and a port that lets a second LLM vendor operate the same vault (§6, §10–§12).

### Six principles

1. **Compounding** — insights from March are integrated and cited in September, not rediscovered.
2. **Human curates, LLM maintains** — maintenance cost drops to zero, so the wiki stays current.
3. **Immutable sources** — `source:` frontmatter is locked at creation; every claim traces back.
4. **Schema as contract** — writing standards, note structures, and safety tiers apply identically in every session.
5. **Ingest · Query · Lint** — Karpathy's three operations, plus finance-specific ones: conviction tracking, retrospectives, stress tests, portfolio sweeps.
6. **Append-only logs** — every thesis has a `## Log`; every conviction shift is dated, reasoned, never edited.

---

## §2 · The vault by the numbers

As of 2026-08-07:

| Content | Automation |
|---|---|
| **88 theses** — 33 active · 31 monitoring · 24 draft | **27 skills** + 11 shared contracts + 15 RATIONALE docs |
| Conviction: 21 high · 57 medium · 10 low | **8 multi-agent workflows** |
| **51 sector notes** · **9 macro frameworks** | **5 n8n pipelines** (news, X ×2, price tripwires, catalyst alerts) |
| **209 research notes** · 6 canvases | 3 hooks · 2 scheduled weekly runs |
| **5 Mental Models files** | 7 Python engines inside skills ("script-first") |
| Live Portfolio (34 holdings) · Watchlist (70 tickers) | `_graph.md`: 1,304 edges · 16 orphans, hook-refreshed |
| 7 website essays · 3 video-script series | 394 snapshots — every destructive edit reversible |

The repo started 2026-04-17 with 17 skills and no automation. Skills grew 17 → 19 (May) → 21 (Jun) → 26 (Jul 23, the commit that added workflows, hooks, and the scheduler) → 27 (Aug 4). See `Vault History - Jul-Aug 2026.md` for the last month.

---

## §3 · Four engines

### 1 · Retro — narrative vs price

`/retro 1w|1m|1q` reads every Log entry, callout, and conviction shift in the window and compares them against price moves, news, and earnings. Each ticker is classified: **aligned** (priced in, weight 0), **inverted** (weight 1.5×), **unreactive** (weight 2×). Output is a ranked trade-idea list. It reads the local `.data/news_stories/` corpus before searching the web, and it scores its own past calls in a calibration file. It never changes conviction. The trades worth making are where what you wrote and what the market did diverge.

### 2 · Cross-thesis synthesis

No one holds 88 theses in their head. Five read-only diagnostic skills (`/assumptions`, `/conviction-audit`, `/dependency-map`, `/macro-exposure`, `/value-chain`) extract structured summaries from any thesis, and eight workflows (§10) run them across the whole book in parallel: which bull cases share one macro bet, where one thesis contradicts another, which conviction labels no longer match their evidence. ~35 manual prompt equivalents are in `User Guide §11`.

### 3 · Stress test

`/stress-test TICKER` reads a thesis as a short-seller. It drafts its short case *before* reading your Bull Case (anti-anchoring), and at high conviction it must gather outside evidence — a banner marks the run if that was skipped. Findings are tagged `[consensus]` or `[vault-blind-spot]`, weak sections are mapped for `/deepen`, and open items go to `_followups.md`. The July NET and INTU stress tests both preceded downgrades.

### 4 · Sensory layer

Five n8n pipelines run every morning before you're at the desk (§11): ~6,500 articles filtered to a ~240-story brief; two X pipelines that flag where crowd sentiment conflicts with a thesis; price tripwires tied to your own trigger levels; catalyst reminders at T-2 and T-0. You read a ranked digest instead of the firehose, and `/ingest --from-brief` promotes the stories that matter into the wiki.

---

## §4 · Mental Models

`/Mental Models` keeps analysis from collapsing into pattern-matching the house style. CLAUDE.md requires reading it before any investment analysis. Mechanical skills (`/numbers`, `/graph`, `/lint`, `/clean`, `/rename`, `/portfolio-snapshot`…) skip it.

| File | Role |
|---|---|
| `Generalist - Overview` | 14 models (G-1…G-14): institutional incentives, capital cycles (Perez), pricing-power taxonomy, ROIIC, cohort economics, expectations investing, base rates, Jevons. Read on every analysis. |
| `Industry - Semiconductors` | Evergreen reasoning tools (bottlenecks, capital cycles, demand architecture, geopolitics, anti-patterns) + a dated "Live Anchors" section holding current falsifiable calls. |
| `Lens - Automation & AI Readiness` | Conviction modifier: is this company structurally positioned for agentic AI? Scoring rubric + falsification conditions. |
| `Lens - Value Layer Monopoly` | Conviction modifier: does it own a layer of the stack everything above must pay to cross, and is that mispriced? |
| `Philosophy - Asset Management Structure` | Tagged `reference-only`; outside the mandatory load. |

The READING PROTOCOL at the top of the Generalist file is the important part: models are lenses and questions, never conclusions. Claims are hypotheses to test. The base-rate view argues against the other models. When every model agrees, that is the cue to hunt the bear case and the single falsifying datapoint — not to commit.

Every thesis and sector note has a `## Mental Models` section where skills record which lenses fired — merged, never overwritten, held as hypotheses.

---

## §5 · State files

LLMs forget everything between sessions. The vault stores memory as Markdown that Claude reads at session start and writes back as it works — nine surfaces:

| File | Role | Owner |
|---|---|---|
| `CLAUDE.md` | The rulebook: writing standards, note schemas, safety tiers. Loaded every session. (`AGENTS.md` is its generated Codex mirror.) | You |
| `_hot.md` | Session memory. Six sections (Active Research Thread · Latest Sync · Sync Archive · Recent Conviction Changes · Open Questions · Portfolio Snapshot) under a 4,000/5,000-word cap. Whole entries drop, never truncate; conviction changes never compress. | ~14 skills |
| `_graph.md` | Dependency map: per-thesis adjacencies + status and log-tail caches. Script-generated, hook-refreshed. Lets `/sync` find the right 5 files instead of re-reading 88. | `/graph` only |
| `_catalyst.md` | Forward calendar: earnings, rulings, launches; catalyst gaps; clustered events ("20 of 34 earnings + FOMC inside 4 days"). | `/catalyst` |
| `_followups.md` | Open-findings register: stress-test weaknesses, crossed triggers, surfaced opportunities. `/status` and `/sync` resolve items; nothing auto-evicts. | Shared |
| `_watchers.md` | Control surface for the n8n layer: queries, RSS outlets, tripwire levels, X terms, model/prompt knobs — all editable tables. | You |
| `_workflows.md` | Auto-generated registry of the 8 workflows. | Generator |
| `.last_sync` + markers | Watermarks and flags: locks, `.graph_dirty`, rename markers, archive registry. | Skills/hooks |
| `_Archive/Snapshots/` | 394 pre-edit copies. `/rollback` restores, including multi-file batches. | Mutating skills |

Every session starts already knowing the 88 theses, the last sync, the open questions, and what the machine has been watching.

---

## §6 · Architecture map

```
L4  ENGINE ROOM      Claudian plugin (chat client, v2.1.2) · 3 hooks · launchd schedule
                     n8n (5 pipelines) · workflow runtime · .agents/.codex dual-harness port
L3  SCHEMA           CLAUDE.md (+AGENTS.md mirror) · 4 Templates + _callouts
                     27 skills · 11 shared contracts · 15 RATIONALE docs
L2  WIKI             Theses (88) · Research (209) · Sectors (51) · Macro & Tech (9)
                     9 state files · Live Portfolio · Watchlist · Canvas
L1  RAW SOURCES      _Inbox · Daily Intel (machine-written) · FMP/X/GDELT/Brave APIs
                     your callouts · transcripts · Deep Research PDFs
```

Raw sources are compiled into the wiki (L1→L2) by skills defined in the schema (L3), run through machinery (L4) that keeps everything fresh and safe.

Ownership rules (full matrix: `INFRASTRUCTURE.md` appendix):
- `_graph.md` has one writer, `/graph` (one narrow `/rename` exception). Its reverse indexes rebuild from scratch every run to prevent drift.
- `## Legacy Callouts` belongs to `/archive-callouts`. `## Log` sections are append-only for everyone.
- n8n only creates new files in `Daily Intel/` and `.data/`. It never touches the wiki spine and never performs Tier-3 operations.
- The interface is the Claudian Obsidian plugin (`realclaudian` v2.1.2): embeds Claude Code, Codex, and other agents with the vault as working directory. `.agents/` and `.codex/` hold a generated port of the skill system for the OpenAI harness (`CLAUDE.md`→`AGENTS.md`, `/skill`→`$skill`), so the vault does not depend on one model vendor.

---

## §7 · Templates & writing standards

Four templates: `Thesis`, `Research`, `Sector`, `Breakdowns` (video scripts, §13), plus `_callouts/` snippets. There is deliberately no Macro template — macro notes are written ad hoc; CLAUDE.md carries their spec (including `publish: true`).

**Research note contract** — four required sections, in order:

```yaml
## Thesis Delta        # what this source changes, for which thesis — always first
## Summary             # the source's actual argument, 1-4 paras
## Evidence            # data points and tables; quote sparingly
## Contradiction Check # what this source contradicts in existing theses
```

Conditional sections: `## Framework / Mental Model`, `## Key Segments` (source >15k words), `## Source Excerpts`. Retention scales with source length: short sources keep ~58%, 60k-word sources ~18%, absolute content always growing. "Thesis Delta first" separates research from clippings. "Contradiction Check" counters confirmation bias.

Figures carry provenance tags: `[FMP]`, `[10-K]`, `[transcript]`, `[web: domain]`, `[1×: source]` (single-source), `[est.]`. `/ingest`'s `verify_note.py` flags high-precision untagged figures and blocks structurally deficient notes on URL/PDF ingests.

**Writing standards** (in CLAUDE.md, applied to every output):
- Lead with the insight or the number
- No hedge words ("importantly", "notably", "it's worth noting"…)
- Tables over prose for comparisons
- Log entries max 2 lines: `[trigger]: [what changed] — [conviction impact + 1 reason]`
- Research notes on existing theses open with the delta, not a company description
- Cut connective tissue

---

## §8 · The thesis structure

Fifteen sections. Each exists because skipping it is how analysts get blindsided:

| # | Section | Job |
|---|---|---|
| 1 | Summary | The case in one paragraph |
| 2 | Key Non-consensus Insights | What the market believes and where it's wrong. Example: ORCL's "Two Oracles" — 16%-GM OpenAI-concentrated OCI vs the mispriced 70%-GM multicloud-DB layer |
| 3 | Outstanding Questions | What a hostile IC would ask |
| 4 | Business Model & Product | Revenue mechanics with technical specs |
| 5 | Industry Context | Competitive dynamics, share, pricing power |
| 6 | Key Metrics | Fixed-schema table, refreshed by `/numbers` from FMP |
| 7–8 | Bull Case / Bear Case | The Bear Case is where the work is |
| 9–10 | Catalysts / Risks | What moves it; what breaks it |
| 11 | Conviction Triggers | Pre-committed if-thens (→HIGH / →LOW / →CLOSE), written before they're needed. HIMS crossed its own GM floor in July; the trigger fired; conviction went to LOW without renegotiation |
| 12 | Mental Models | Which lenses fired, held as hypotheses (§4) |
| 13 | Related Research | Wikilinks feeding the graph |
| 14 | Legacy Callouts | Auto-archived old callouts (§16) |
| 15 | Log | Append-only audit trail |

Sector notes run a parallel 12-section structure, opening with an Active Theses routing table. Their "Investor Heuristics" section — what consensus believes and where it could be wrong — mirrors Key Non-consensus Insights at sector level.

Fixed structure is what the machines run on: `/numbers` can refresh every Key Metrics table unattended because the schema never varies; price tripwires can quote your own trigger block in an alert; `/conviction-audit` can catch a silently-fired trigger because the if-thens were written in advance.

---

## §9 · Skills

A skill is a specification at `.claude/skills/<name>/SKILL.md`: pre-flight checks, procedure, exit conditions. Same command, same behavior, readable in plain text. Three design patterns:

- **Script-first**: seven skills hand deterministic work to Python engines (`generate_graph.py`, `lint.py`, `numbers_compute.py`, `verify_note.py`, `extract_transcript_signals.py`, `build_snapshot.py`, `extract_sections.py`). The LLM plans and judges; the script parses and computes. `/graph` set the precedent in June after LLM extraction hit output-token limits.
- **Shared contracts**: 11 files in `_shared/` define cross-skill law — locks, `_hot.md` compression, Log-prefix semantics (20 registered prefixes), graph usage, followups, provenance tags, wikilink forms, sector resolution, trigger reporting, mental-model merging.
- **RATIONALE.md**: 15 skills carry design-rationale companions (2,400+ lines) that never load at runtime.

Model assignment is per-skill: Opus for analytical work, Sonnet for mechanical work, Sonnet/medium for `/numbers`, Opus/high for the read-only extractors. `/prune`, `/retro`, and `/surface` delegate to subagents to keep bulk reads out of the main conversation.

### The 27 skills, six families

**● Core (4)**
- `/ingest` — URL / file / `_Inbox` batch / `--from-brief` → structured Research notes. Same-source dedup, quality gate.
- `/sync` — propagate research into theses, sectors, macros, `_hot.md`. Graph-assisted targeting; Log-prefix rules decide what propagates; drift detection.
- `/status` — conviction/status changes behind the Tier-3 confirmation gate. `draft→active` is a fast path.
- `/graph` — rebuild `_graph.md` (full · `last` · N days). Also fired automatically by the Stop hook.

**▲ Building (4)**
- `/thesis` — new 15-section thesis; duplicate/archive-collision checks; peer suggestions from the graph.
- `/deepen` — improve one section; `--sync-metrics` reconciles stale figures thesis-wide (table → FMP → web); batch `--all-flagged`.
- `/brief` — 1-page IC memo; read-only; excludes callouts and working state.
- `/numbers` — refresh Key Metrics from FMP; crossed triggers written to `_followups.md`; flags stale Summary framing, never edits it.

**◆ Analytical (7)**
- `/surface` — blind spots and opportunities; opportunities need ≥2 cross-note datapoints, a falsifier, and a priced-in check.
- `/stress-test` — short-seller pass (§3).
- `/scenario` — propagate a hypothetical macro event across the book; reverse mode included.
- `/compare` — side-by-side of 2+ tickers with atomic cross-sector edits.
- `/catalyst` — rebuild the forward calendar.
- `/retro` — narrative-vs-price review with self-calibration (§3).
- `/transcript` — pull earnings call from FMP; hedging/specificity deltas vs prior quarters; delta-first note.

**◇ Diagnostic (5)** — read-only, no locks, no writes
- `/assumptions` · `/conviction-audit` · `/dependency-map` · `/macro-exposure` · `/value-chain`
Each one's `## Method` section is the exact spec its portfolio workflow (§10) fans out.

**◐ Maintenance (6)**
- `/lint` — ~67 health checks; ~45 run deterministically in `lint.py`. Runs unattended every Sunday.
- `/prune` — evaluate weak theses for upgrade / monitor / close.
- `/clean` — purge old snapshots and machine artifacts; 30-day closure-snapshot floor, no override.
- `/archive-callouts` — sweep addressed callouts >180d into `## Legacy Callouts`.
- `/rollback` — restore from snapshot, with batch cascade detection.
- `/rename` — rename a thesis atomically across filename, wikilinks, graph, sector table, snapshots, `_hot.md`.

**■ Portfolio ops (1)**
- `/portfolio-snapshot` — export the live tracker as a static snapshot with SVG charts (§13).

---

## §10 · Multi-agent workflows

"Is my book coherent?" needs every thesis analyzed the same way at once. 88 sequential skill runs would take days; a workflow does it in one run.

Eight scripts in `.claude/workflows/` (registry: `_workflows.md`). All share one shape: enumerate theses → one read-only agent per thesis, each following the matching skill's `## Method` → aggregate and rank → optionally persist through a single writer agent.

| Workflow                     | Question                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------ |
| `portfolio-conviction-audit` | Which names are over-convicted; which triggers fired unactioned                            |
| `portfolio-correlation`      | Which bull cases rest on the same variable                                                 |
| `portfolio-macro-exposure`   | Where the book is concentrated in one macro bet                                            |
| `portfolio-supply-chain`     | Shared suppliers/customers; cross-thesis single points of failure                          |
| `vault-contradictions`       | Where one thesis's bull premise is another's bear premise, adversarially verified          |
| `portfolio-scenario`         | A named macro event assessed across all theses                                             |
| `portfolio-stress-test`      | Every thesis short-sold, findings verified by up to 3 skeptics. Heaviest; run deliberately |
| `portfolio-retro`            | Full-portfolio retro with throttled fan-out                                                |

Guarantees: read-only by default (`persist: true` opts in); when persisting, one writer agent touches shared files so parallel agents never collide; no workflow ever changes `conviction:` or `status:` — that stays with `/status` and you. Invoked in natural language, not as slash commands. A full sweep can spawn ~80 agents; the first run warns you.

Skills are the unit of correctness; workflows are the unit of scale. Improve a skill's method and its portfolio sweep improves with it.

---

## §11 · The n8n layer

A self-hosted n8n instance runs five pipelines each morning. The division of labor is fixed (spec: `n8n Automations.md`): n8n acquires, filters, and alerts; skills analyze and propagate. n8n writes only new files in `Daily Intel/` and `.data/`, and never performs Tier-3 operations.

| Time | Pipeline | What it does | ~Cost/mo |
|---|---|---|---|
| 07:00 | **News Sweep** | 5 channels (RSS outlets, Google News, GDELT, Brave, FMP) → dedupe → headline triage → embedding-based same-story clustering → full-body fetch → rescore + summarise → ranked News Brief + JSON corpus for `/retro` + Telegram. Live daily since Jul 28: ~6,500 fetched → ~240 stories | $60–110 |
| 07:30 | **Catalyst Reminders** | Parses `_catalyst.md`; Telegram at T-2 and T-0; warns if the calendar is stale | $0 |
| 07:35 | **Price Tripwires** | One batch FMP quote vs `_watchers.md` levels; alert cites the thesis trigger block | $0 |
| 08:00 | **X Canary** | Cheap daily probe of the X data provider; alarms before the harvester spends money | ~$0 |
| 08:30 | **X Harvester** | Cashtags (from thesis frontmatter) + curated terms → engagement-delta detection → one model pass against the thesis → X Intel note with divergence flags ("crowd view conflicts with vault view on UBER, SNDK") | $17–40 |

`_watchers.md` is the control surface: queries, outlets, tripwire levels, X terms, and the model/prompt used at each pipeline stage are all editable Obsidian tables. Retargeting the machine is a markdown edit.

The loop closes with `/ingest --from-brief [date]`: stories from a brief become Research notes with thesis deltas, ready for `/sync`. An Aug 7 X Intel divergence flag on UBER became a `/deepen UBER` reassessment the same week.

---

## §12 · Safety machinery

Five independent layers keep the LLM (or you, at 1am) from breaking the vault:

1. **Tiers** (CLAUDE.md): Tier-1 protected files; Tier-2 append-only zones; Tier-3 confirmation-gated investment decisions (conviction, status, archive moves, link removal).
2. **Pre-flight** (every mutating skill): scoped locks (vault-wide / per-ticker / read-only), token-based, never auto-stolen; rename-marker blocks; filename sanitization; section probes.
3. **Transactions**: multi-file operations write a manifest (skeleton → populate → flip); a crashed run is detectable and `/rollback` restores the whole batch. 394 snapshots; closure snapshots keep a 30-day floor no cleanup flag can override.
4. **Hooks**: `guard-protected.py` blocks writes to Tier-1 paths before the tool executes, with a per-turn escape hatch that re-arms itself; `mark-graph-dirty.py` + `refresh-graph.py` regenerate `_graph.md` at turn end whenever a spine file changed — no one runs `/graph` by hand.
5. **Scheduled hygiene** (launchd): Sunday 18:00 `/catalyst`, Sunday 20:00 `/lint`. The lint report publishes itself into `Daily Intel/` as a weekly Vault Health note.

Mistakes cost a snapshot, not data. The rules are enforced by machinery, not by trusting the model.

---

## §13 · Publishing

Research also flows out:

- **Live Portfolio** — 34-holding tracker: `dataviewjs` + FMP quotes, 15 columns; refresh writes the rendered tables back into the note. **Watchlist** covers all 70 thesis tickers and flags which are held.
- **`/portfolio-snapshot`** — exports the tracker to `Portfolio Snapshot/DD-MM-YYYY.md`: static tables, a `## Trades` slot, SVG charts, engine clutter stripped, `Publish_Snapshot: true` for the pipeline.
- **Website sync** — every thesis/sector/macro note carries `publish: true`; a GitHub→website pipeline pulls them. `Website/` is a separate blog pipeline: 7 essays (Jul 22–29) plus 4 pillar statements, each tracing to vault notes via `source_note:`.
- **Thesis Breakdowns** — bilingual (EN/中文) video-script docs (SK Hynix, NVDA, TSMC): 15-episode series maps and an Evidence Ledger grading every claim VF / IE / MC / CH / AI (verified fact → internal inference).

---

## §14 · A day in the life

**07:00–08:30, unattended** — news sweep, catalyst and tripwire alerts to Telegram, X harvest. Today's News Brief and X Intel are waiting in `Daily Intel/`.

**Morning (15–45 min)**
1. Read `_hot.md` — context back in one screen.
2. Read the News Brief and X Intel; check divergence flags.
3. `/ingest --from-brief` the 1–3 stories that matter, or `/ingest` an `_Inbox` drop.
4. `/sync` — deltas flow into theses, sectors, macros. The graph refreshes itself at turn end.

**Working a name** — `/transcript` on earnings day; `/deepen` where the thesis is thin; `/compare` when dynamics shift; callouts wherever you disagree (§16); `/status` when the evidence justifies a change.

**Friday** — `/retro 1w`; act on the top gap candidates.

**Sunday, unattended** — `/catalyst`, then `/lint` → Vault Health note.

**Monthly** — the maintenance chain, in order: `/sync all` → `/graph` → `/lint` → `/prune` → `/clean` → `/surface` → `/catalyst` → `/graph last`. Periodically, one portfolio workflow (§10) as a book-level audit.

---

## §15 · Workflow chains

- **New position** — `/thesis` → `/stress-test` → (optional `/assumptions`, `/compare`) → `/status draft→active` → `/sync`
- **Earnings reaction** — `/transcript` → `/sync` → `/status` only if conviction moved; `/stress-test` in between if unsure
- **Conviction drift** — `/sync` flags drift → `/stress-test` → `/deepen` the weak section → `/status` change or reaffirm (reaffirm leaves a Log entry the retro reads later)
- **Macro shock** — `/scenario` (or `portfolio-scenario` at scale) → `/compare [hurt] vs [helped]` → `/status` → `/sync`
- **Sector deep-dive** — `/surface [sector]` → `/compare [key players]` → `/thesis` per idea → promote before the graph rebuild (drafts are invisible to sector routing)
- **Weekly retro** — `/retro 1w` → stress-test the alpha candidates, deepen the missed signals

Full chain index and the "I want to ___" table: `User Guide §3–§4`.

---

## §16 · Inline callouts

When Claude writes something you disagree with, drop a typed callout next to the sentence, then ask Claude to "address fresh callouts in [[note]]".

Four types, four hotkeys: `[!question]` (⌘⌥1) · `[!error]` (⌘⌥2) · `[!tip]` (⌘⌥3) · `[!todo]` (⌘⌥4).

Lifecycle: **Fresh** → **Addressed** (audit block) → swept to **Legacy Callouts** after 180 days, unless marked `[[pinned]]`, which keeps it alive as a recurring question (re-open by deleting the response block; the marker survives).

Addressed format — your words verbatim in italics, Claude's answer plain:

```markdown
> [!question] 2026-08-07 → Addressed 2026-08-07
> **Prompt:** *Has management given a specific yield number for Q2, or only directional commentary?*
>
> **Response:** Integrated the 58% interim threshold from the Q1 call into §Outstanding Questions. Full analysis in the body.
```

The rule: the body holds the analysis, the callout holds the record. The response is 1–3 sentences plus a pointer. Claude never writes callouts (they are your channel) and never edits yours except to address them. Four `[!error]` callouts on one name in a month is conviction drift, and the system will say so.

---

## §17 · FAQ

**Isn't this just RAG?** No. RAG retrieves from a static index; nothing accumulates. Here the LLM reads *and writes* the artifact: it edits, propagates, snapshots, and audits. The wiki is the memory.

**How is this different from ChatGPT?** Persistence and machinery. Every session starts knowing 88 theses, the graph, recent conviction shifts, and this morning's harvested news. Half the system runs without a chat open at all.

**Do I need to be a programmer?** No. Install Obsidian + the Claudian plugin, clone, run `setup-vault.sh`, type commands. The optional n8n layer is the one technical build — budget hours, not minutes.

**Won't Claude hallucinate into my thesis?** It can; treat every section as a first draft. The mitigations are structural: locked `source:` provenance, provenance tags on figures, the ingest quality gate, callouts as a permanent disagreement channel, `/stress-test`, and the weekly automated lint. Mistakes are auditable and reversible. You are still the analyst.

**What stops it going off-script?** The five layers in §12. Tier-1 protection is enforced by a hook that blocks the write before it executes.

**What does it cost?** Claude subscription plus ~$20–35/mo for the sensory layer at current volume (~$80–145/mo with the full news sweep). Portfolio-wide workflow sweeps are the expensive habit; run them deliberately.

**How long until it's useful?** First thesis: immediately. Compounding shows up around thesis five or six, when cross-thesis patterns appear. At 88 theses, portfolio-level questions are answerable in minutes.

**Only for stocks?** The pattern — context engineering, deterministic skills, append-only logs, rollback, a sensory pipeline feeding a compiled wiki — generalizes to legal research, literature review, competitive intelligence, journalism.

---

## §18 · Glossary

- **Thesis** — 15-section investment case, one per ticker.
- **Research note** — one note per source; opens with the Thesis Delta.
- **Sector note** — 12-section map routing every thesis in a sector.
- **Skill** — deterministic workflow spec in `.claude/skills/`. 27 exist.
- **Workflow** — multi-agent script fanning a skill across the book. 8 exist.
- **Diagnostic skill** — read-only extractor (assumptions, dependencies, macro bets, value chain, conviction audit).
- **Shared contract** — cross-skill rules in `_shared/`. 11 files.
- **Script-first** — a Python engine inside a skill does the deterministic work; the LLM judges.
- **Hook** — harness-level event script: write guard, graph dirty-flag, turn-end refresh.
- **Lens** — Mental Models file applied as hypothesis, never verdict; acts as a conviction modifier.
- **Conviction trigger** — pre-committed if-then (→HIGH/→LOW/→CLOSE) written in advance.
- **Callout** — typed inline pushback; becomes a permanent Prompt/Response record.
- **Watcher** — a row in `_watchers.md` telling n8n what to monitor.
- **Daily Intel** — machine-written folder: News Brief + X Intel daily, Vault Health weekly.
- **Narrative-price gap** — distance between what the vault says and what price did; the retro's ranking metric.
- **Followup** — open finding in `_followups.md`; resolved by `/status` or `/sync`.
- **Snapshot / manifest** — pre-edit copy / multi-file transaction record; together they make operations reversible.
- **Tier-3** — investment decisions gated behind explicit confirmation.
- **Provenance tag** — source grade on a figure: `[FMP]`, `[10-K]`, `[1×: source]`, `[est.]`.
- **Watermark** — `.last_sync` mtime; skills touch only what changed since.
