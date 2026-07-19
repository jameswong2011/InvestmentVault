# User Guide — Claude Code + Obsidian for Investment Research

> What to do, in what order, and when to prompt freely instead of invoking a skill.
>
> **How to read.** Fresh machine or clone? [[Setup Guide]] first. Then: §0–§2 to get working. §3 = workflow menu. §4 = intent → chain. §5 = skill dictionary. §11 = free-form prompt library. §13–§14 only when debugging or on first use.

---

## 0. First Run

Machine and vault setup — installs, clone, plugins, Claudian config, API keys — lives in [[Setup Guide]]. This guide assumes a configured environment.

One-time metadata bootstrap on any fresh vault or clone ([[Setup Guide#7. Bootstrap the vault|Setup Guide §7]]):

```
/sync        # establishes the .last_sync watermark; first run reads all vault files
/graph       # rebuilds _graph.md from vault state
```

Without this bootstrap, `/sync TICKER` and scoped `/surface` block (they need `_graph.md`). On a vault that already has content, the first `/sync` reads everything — expected, not a bug.

> If `.last_sync` is ever deleted, the next `/sync` re-reads every file (5–10× slower). See [[#`.last_sync` deletion|§13 — `.last_sync` deletion]].

---

## 1. The Core Loop

**Forward loop — new info in**:
```
_Inbox/ drop  →  /ingest  →  /sync  →  work  →  /sync  →  /graph last
```

**Backward loop — thinking vs market**:
```
/retro [1w|1m|1q]  →  review  →  /status · /deepen · /stress-test  →  /sync  →  /graph last
```

| Step | What happens |
|---|---|
| `/ingest` | `_Inbox/` raw material → structured Research notes with wikilinks |
| `/sync` | Propagates insights to theses, sector notes, macro notes, `_hot.md` |
| Work | Research, thesis building, conviction changes, inline callouts |
| `/retro` | Aggregates the window's activity; overlays newsflow + earnings + price; ranks trade ideas by narrative-price gap |
| `/graph last` | Reconciles the dependency map after every write chain |

**Periodic maintenance**: `/surface` (forward — ideas, blind spots), `/catalyst` (forward — event calendar), `/retro` (backward — market vs thinking), `/lint` (now — health check), `/archive-callouts` (now — sweep resolved callouts). Read-only chains (`/brief`, `/lint`, `/rollback` list) skip `/graph last`.

---

## 2. Session Start

### Resume context
```
Read _hot.md. Summarise what I was working on, what's unresolved,
and suggest what to focus on today.
```

### Process inbox
```
/ingest
/sync
```
`/ingest` creates Research notes only; `/sync` propagates. Always run both.

### Earnings-season triage
```
Which of my thesis companies report earnings in the next 2 weeks?
For each, list the key metrics and outstanding questions from my
thesis note that the report should answer.
```

### Manual edit protocol (important)

**After manually editing a thesis body section, always append a Log entry.** Without one, `/sync` may classify the edit as skill-origin and silently skip propagation. Any prefix not in the skill-origin registry works (`Manual edit:`, `Reviewed:`, `Refined:`):

```markdown
### 2026-04-20
- Manual edit: tightened Bull Case pricing-power argument — strengthened, added customer concentration data point from Q4 transcript
```

### User callouts — inline feedback on LLM output

Drop hotkey-triggered callouts inside any section: `> [!question]` (⌘/Ctrl+Alt+1), `> [!error]` (+2), `> [!tip]` (+3), `> [!todo]` (+4). Ask *"address fresh callouts in [note]"* to resolve them inline. `/archive-callouts` periodically sweeps old addressed callouts to a `## Legacy Callouts` archive; `[[pinned]]` exempts a callout from sweep. Full spec: [[#Inline callouts — user feedback markers|§6 Inline callouts]].

### Referencing content in prompts

| Mechanism | Syntax |
|---|---|
| Vault wikilink | `[[Theses/NVDA - Nvidia]]` |
| Chat file reference | `@Research/2026-04-15 - ....md` |
| Editor selection | Select text, then prompt — auto-attached |
| Browser selection (Surfing) | Select in an Obsidian browser view, then prompt |

The note you're viewing is always attached as `<current_note>` — "this thesis" works without naming the file.

---

## 3. Workflow Chains

Minimum steps per scenario. Failure-mode footnotes: [[#13. Caveats & Gotchas|§13]].

### 3.1 Starting new work

#### New position — full build
```
/thesis TICKER
/status TICKER status draft→active [rationale]
/stress-test TICKER
/sync TICKER
```
Optional: `/compare TICKER vs COMPETITOR` before `/sync`; `/deepen TICKER [weakest section]` for gaps the stress test flags.

#### New position — from existing research
```
/ingest                                      # any inbox items first
/sync
/thesis TICKER                               # vault research auto-used
/status TICKER status draft→active [rationale]
/sync TICKER
```

#### Idea discovery → new position
```
/surface                                     # or /surface [sector]
/thesis TICKER
/compare TICKER vs [existing competitor]
/status TICKER status draft→active [rationale]
/sync
```

#### Acting on a surface finding
From the latest `/surface` note: `/thesis TICKER` (new name) OR `/deepen TICKER [section]` (extends an existing thesis), then `/sync`.

#### Sector deep-dive
If the sector note doesn't exist:
```
Create a new Sector Note for [SECTOR] using the Sector Template. Search
the vault for all relevant thesis notes, research notes, and macro
connections. The "Investor heuristics" section should explicitly state
what consensus believes and where they could be wrong.
```
Then: `/graph` → `/surface [sector]` → `/compare [key players]` → `/sync`.

If building multiple theses in the new sector, promote each to `active` **before** rebuilding the graph — draft theses are invisible to sector-scoped skills. See [[#Draft theses invisible to sector scope|§13]].

### 3.2 Responding to events

#### Earnings reaction
```
/ingest [transcript or press release URL]
/sync TICKER
```
Conviction changed → `/status TICKER conviction old→new [what the report revealed]`. Ambiguous → `/stress-test TICKER` first.

#### Macro shock
```
/scenario [describe the event with quantitative parameters]
/status TICKER conviction old→new [transmission channel]    # most affected
/compare [exposed] vs [beneficiary]                          # if competitive shifts emerge
/sync
```

#### Conviction drift response
`/sync` flagged `⚠️ Conviction drift` on a thesis:

- **Reaffirm**: `/status TICKER reaffirm [why the drift signal is noise]`
- **Investigate**: `/stress-test TICKER` → `/status` (change or reaffirm) → `/sync TICKER`
- **Investigate with research**: `/deepen TICKER [section the drift relates to]` → `/sync TICKER` → `/status`

#### Catalyst-driven review
```
/catalyst
/deepen TICKER Catalysts                     # each imminent-catalyst thesis
/prune [sector] stale                        # theses with no catalysts flagged
```

### 3.3 Improving theses

| Situation | Chain |
|---|---|
| Weak/stale section | `/deepen TICKER [section]` (omit section → auto-detect weakest) → `/sync TICKER` |
| Before a major decision | `/stress-test TICKER` → `/deepen TICKER [flagged section]` → `/sync TICKER` |
| Competitive shift | `/compare A vs B` → `/status` if warranted → `/sync` |
| Pitch prep | `/brief TICKER`; adversarial prep: `/stress-test TICKER` → `/brief TICKER` |
| Ad-hoc multi-ticker research | `/ingest [URL1]` → `/ingest [URL2]` → `/sync` |

`/compare` needs at least one ticker with a thesis; tickers without theses use web research (lighter, no vault updates for them).

### 3.4 Maintaining the vault

#### Portfolio pruning cycle
```
/sync                                        # first — /prune warns if unsynced research exists
/prune                                       # presents table, asks approval, applies in-line
/surface                                     # reallocation opportunities
/graph last
```

#### Monthly maintenance
```
/sync all
/graph
/lint
/prune
/clean
/surface
/catalyst
/graph last
```
Order matters: `/sync all` before `/graph` (syncs change links); `/lint` after `/graph` (checks graph health); `/prune` after `/lint` (lint flags staleness); `/surface`/`/catalyst` against a clean vault; final `/graph last` picks up closure `.graph_invalidations`.

`/surface` and `/retro` delegate their whole run to a subagent; `/prune` delegates only its read/analysis half (mutations stay in the main thread behind the approval gate); `/lint` runs its mechanical checks via `lint.py` and reads only flagged files. Either way, heavy reads stay off your main conversation context. Quarterly, substitute `/surface all` for a deeper pass (~4× subagent read cost). (`/catalyst` still runs in the main thread — see the execution matrix note in §14.)

#### Recovery — undo a bad sync
```
/rollback TICKER                             # pick the (pre-sync) snapshot
```
Rollback detects multi-file cascades and offers atomic restore. After: `/sync TICKER` (single-file) or `/sync all` + `/graph` (multi-file). See [[#Propagated-research caveat after rollback|§13]].

#### Recovery — undo a closure
```
/rollback TICKER
```
The archived thesis returns to its original path. Check restored `status:`: `active` (typical) → done; `closed` (rare) → `/status TICKER status closed→active [rationale]`. Then `/sync TICKER` → `/graph` (full — thesis structure changed).

### 3.5 Callout-driven review

Post-skill quality gate: drop callouts on LLM output, have Claude address them.

```
/ingest [URL] | /stress-test | /compare | /scenario | /surface [scope]
/sync TICKER → /graph last
Drop callouts (Mod+Alt+1..4) in the affected thesis
"Address fresh callouts in [[Theses/TICKER]]. Prefix Log entry 'Addressed user callouts:'"
/sync TICKER → /graph last
```

Multi-thesis: *"Address fresh callouts in every thesis I've touched today"* → `/sync` → `/graph last`. For rewrites >3 paragraphs, use `/deepen` instead for snapshot safety ([[#When to use /deepen instead|§6]]).

**Periodic hygiene**: quarterly, `/archive-callouts` (dry-run) then `/archive-callouts 180` to sweep ≥180d callouts into `## Legacy Callouts` ([[#Sweeping addressed callouts into Legacy Callouts|§6]]).

### 3.6 Retrospective review

Backward-looking periodic review — callouts are mid-flight feedback; retro aggregates them against market reaction.

```
/retro 1w      # weekly — full callout bodies
/retro 1m      # monthly — one-liner per callout
/retro 1q      # quarterly — aggregated by ticker
```

**Scans**: in-window addressed callouts (with Responses), open fresh callouts, `## Log` entries (skill-origin vs manual split). **Overlays per ticker**: price move (±3% threshold), newsflow polarity, earnings results. **Ranks by narrative-price delta**:

| Delta | Meaning | Weight |
|---|---|---|
| aligned-up / aligned-down | Narrative + price agree — priced, no alpha | 0 |
| **inverted-bear** | Good news, price fell — positioning / forward-risk signal | 1.5× |
| **inverted-bull** | Bad news, price rose — capitulation / forward-relief | 1.5× |
| flow-bull / flow-bear | No catalyst, price moved — hidden signal | 1.0× |
| unreactive-good / unreactive-bad | Event occurred, price flat — priced in or dismissed | 2.0 (fixed) |

Vault stance determines the read: **alpha harvest** (vault predicted the gap), **missed signal** (market saw something vault didn't), or **stress-test candidate** (vault fighting the market).

**Follow-up** (retro never auto-executes): `/status` for harvest signals · `/stress-test` for vault-fighting-market · `/deepen` for missed signals · `/thesis` for flow moves on uncovered names → `/sync` → `/graph last`.

**Output is immutable**: each run writes a new Research note; the historical trail of thinking-vs-market is the secondary product. Retro appends a `Retro insight:` Log entry to each Top-3 trade-idea thesis (non-skill-origin — `/sync` propagates normally). Cadence: [[#12. Cadence Guide|§12]].

---

## 4. Decision Guide — "I Want To..."

> Notation: `skill field old→new [reason]`. Full argument forms: [[#5. Skill Reference|§5]].

| I want to... | Do this |
|---|---|
| **Start a session** | Read `_hot.md` → `/ingest` → `/sync` |
| **Clip an article / process inbox** | `/ingest [URL]` or `/ingest` → `/sync` |
| **Start covering a new company** | [[#New position — full build|§3.1]] |
| **Formalise collected research** | [[#New position — from existing research|§3.1]] |
| **Improve a thesis (or section)** | `/deepen TICKER [section]` → `/sync TICKER` |
| **Review & feedback on LLM output** | Callouts → "address callouts in [[note]]" → `/sync TICKER` → `/graph last` ([[#3.5 Callout-driven review\|§3.5]]) |
| **Challenge a thesis** | `/stress-test TICKER` → `/status` → `/sync` |
| **Compare competitors** | `/compare A vs B` → `/sync` |
| **Pitch a position** | `/brief TICKER` |
| **React to earnings** | `/ingest [URL]` → `/sync TICKER` → `/status` if needed |
| **React to macro event** | `/scenario [event]` → `/status` (most affected) → `/sync` |
| **Handle conviction drift** | [[#Conviction drift response|§3.2]] |
| **Change conviction** | `/status TICKER conviction old→new [reason]` |
| **Close a position** | `/status TICKER status active→closed [reason]` |
| **Reopen an archived position** | [[#Recovery — undo a closure|§3.4]] |
| **Find new ideas / blind spots** | `/surface`, `/surface [sector]`, or `/surface all` (deep) |
| **Review the week / month / quarter** | `/retro 1w` / `1m` / `1q` ([[#3.6 Retrospective review\|§3.6]]) |
| **See where market disagrees with me** | `/retro [window]` — inverted deltas are the signal |
| **Model a "what if"** | `/scenario [event]` |
| **See what's coming up** | `/catalyst` |
| **Clean up weak positions** | [[#Portfolio pruning cycle|§3.4]] |
| **Run monthly maintenance** | [[#Monthly maintenance|§3.4]] |
| **Check vault health** | `/lint` (full) or `/lint TICKER` (scoped) |
| **Undo a bad sync** | [[#Recovery — undo a bad sync|§3.4]] |
| **Undo a conviction change** | `/rollback TICKER` → `(pre-status)` snapshot |
| **Delete old snapshots** | `/clean` ([[#`/clean`|§5 /clean]]) |
| **Rename a thesis** | `/rename TICKER "New Name"` ([[#Renaming a thesis|§10]]) |
| **Build a sector note** | [[#Sector deep-dive|§3.1]] |
| **Deep-dive a topic** | "Teach me [TOPIC]" → Research note → `/sync` ([[#7. Research & Thesis Building|§7]]) |
| **Explore free-form** | [[#11. Prompt Library|§11]] |

---

## 5. Skill Reference

One entry per skill: arguments, creates, modifies, follow-up. Model + context assignment: [[#Skill execution matrix|§14]].

### Core workflow

#### `/ingest`
```
/ingest                                    # batch: everything in _Inbox/
/ingest https://example.com/article        # single URL
/ingest /path/to/file.pdf                  # local file (.md, .pdf, .csv, .txt)
```
- **Creates**: Research note(s); moves sources to `_Inbox/processed/`. **Modifies**: nothing else.
- **Follow-up**: `/sync` → `/graph last`.
- Same-source dedup: same-day identical `source:` hard-blocks; older ingests prompt append/supersede/cancel. Quality gate (`verify_note.py`) deletes failed notes (paywall, OCR corruption, or body below the length-scaling retention floor — min 300 words, higher for longer sources) and retains the source.

#### `/sync`
```
/sync                                      # graph-assisted: changed files + adjacencies
/sync all                                  # brute-force: reads everything (slow)
/sync NVDA                                 # ticker-scoped: one thesis + adjacencies
```
- **Creates**: Tier A snapshots, `_sync-manifest`. **Modifies**: Theses, Sectors, Macro, `_hot.md`, `.last_sync` (default/all only).
- **Follow-up**: `/graph last`.
- Mode choice: one ticker touched → `TICKER`; multi-ticker research → default; monthly or vault feels stale → `all`.

#### `/status`
```
/status NVDA conviction medium→low China risk unhedgeable
/status NVDA status draft→active thesis meets quality bar
/status NVDA status active→monitoring awaiting catalyst
/status NVDA status active→closed thesis invalidated by [reason]
/status NVDA reaffirm earnings miss was one-time, position unchanged
```
- **Creates**: snapshot (except `draft→active` and `reaffirm`), `_status-manifest`. **Modifies**: thesis frontmatter + Log, sector note, `_hot.md`; on closure: archive move, `.graph_invalidations`, `.archive_ticker_registry.md`.
- **Follow-up**: `/sync` (conviction changes), `/graph last`.
- Tier 3 confirmation before applying, **except** `draft→active` (fast-path: one-line FYI, no prompt, no snapshot).

### Analytical

#### `/surface`
```
/surface                                   # full vault, section-targeted (default — fast)
/surface all                               # full reads (quarterly deep review)
/surface NVDA                              # ticker + adjacencies + sector peers
/surface semiconductors                    # sector-scoped
```
- **Creates**: Research note (`(all)` suffix for deep runs). **Modifies**: `_hot.md`.
- **Forked**: only the top-3-insights summary returns to your conversation.
- **Follow-up**: `/deepen` or `/thesis` on opportunities; `/graph last`.
- Default delivers ~95% of `all`'s signal at ~25% of the read cost; reach for `all` only when section-targeting may miss a cross-section pattern.

#### `/stress-test`
```
/stress-test NVDA
```
- **Creates**: Research note, `_stress-test-manifest`. **Modifies**: thesis Log + Related Research, `_hot.md`.
- Acts as a short seller. Flags for reassessment but never changes conviction — that requires `/status`.
- **Follow-up**: `/status` if needed → `/sync` → `/graph last`.

#### `/scenario`
```
/scenario Fed cuts 150bps by year-end
/scenario China invades Taiwan
/scenario reverse [[Research/2026-04-19 - Scenario - Fed cut]]
```
- **Creates**: Research note (forward mode). **Modifies**: thesis Logs of Major-impact positions, `_hot.md`.
- Classification approval gate before any Log write (promote/demote/cancel).
- **Follow-up**: `/status` (affected) → `/sync` → `/graph last`.

#### `/compare`
```
/compare BESI vs AMAT                      # two
/compare PANW NET CRWD                     # 3+
```
- **Creates**: comparison Research note, `_compare-manifest`, sector snapshot(s). **Modifies**: thesis Logs, sector note(s), `_hot.md`.
- ≥1 ticker must have a thesis; the rest use web research (no vault updates for them). Cross-sector edits are all-or-nothing.
- **Follow-up**: `/sync` → `/graph last`.

#### `/catalyst`
```
/catalyst
```
- **Creates**: `_catalyst.md` (overwrites; pre-regenerate snapshot). **Modifies**: `_hot.md`. Forked.
- Web-searches earnings dates; flags catalyst clusters, gaps, and stale events.
- **Follow-up**: `/deepen TICKER Catalysts` for gap theses.

#### `/retro`
```
/retro [1w|1m|1q]                          # default 1w
```
- **Creates**: immutable Research note (new file per run). **Modifies**: thesis Logs (Top-3 ideas only, `Retro insight:`), `_hot.md`. Forked (~60 reads + up to ~126 WebSearches stay off main context).
- Never auto-mutates conviction/status. Full mechanics + follow-up chains: [[#3.6 Retrospective review|§3.6]].

### Building

#### `/thesis`
```
/thesis NVDA
```
- **Creates**: draft thesis note, `_thesis-manifest`. **Modifies**: sector note (if promoted active), `_hot.md`.
- Searches vault first, then web. Archive collision → 4-option pause ([[#Archive-collision prompt|§13]]).
- **Follow-up**: `/status draft→active` → `/stress-test` → `/sync` → `/graph last`.

#### `/deepen`
```
/deepen NVDA                               # auto-detects weakest section
/deepen NVDA [section]                     # any thesis section by name (Bull Case, Risks, ...)
```
- **Creates**: pre-deepen snapshot, `_deepen-manifest`, optional supporting Research note. **Modifies**: thesis (target section + Log), `_hot.md`.
- Surgical — one section at a time, never a full rewrite. Aborts if the named section is absent; refuses `Legacy Callouts` and `Log`.
- **Follow-up**: `/sync TICKER` → `/graph last`.

#### `/brief`
```
/brief NVDA
```
- **Creates**: 1-page Research note. **Modifies**: `_hot.md` only — read-only on the thesis. Warns if a prior brief exists.
- **Follow-up**: `/graph last` optional (brief is derivative; see [[#`/brief` and `/surface` don't fully refresh the graph|§13]]).

### Maintenance

#### `/lint`
```
/lint                                      # full vault (~56 checks)
/lint NVDA                                 # scoped, faster
```
- Read-only report (forked): structural, freshness, connection, analytical, snapshot/manifest hygiene, graph health, callout hygiene.
- **Follow-up**: fix flagged issues; `/graph` for graph-health flags.

#### `/prune`
```
/prune [sector] [flag]                     # flags: stale | low | draft | monitoring
```
- **Creates**: per-closure/upgrade snapshots, `_prune-manifest`. **Modifies**: theses, sector notes, `_hot.md`; closures append `.graph_invalidations` + registry. Forked.
- Warns on unsynced research; waits for approval; applies changes in-line — do NOT run `/status` afterward. 30-day regret window via `/rollback`.
- **Follow-up**: `/graph last`; `/surface` to reallocate attention.

#### `/graph`
```
/graph                                     # full rebuild
/graph last                                # incremental: changed theses + invalidations
/graph 3                                   # catch-up from N days ago
```
- Writes `_graph.md` only; clears `.graph_invalidations` and `.sync_all_fresh` on success. No content edits, no snapshots.
- `last` is the default post-chain reconciliation; full rebuild after `/rename` or any manual thesis `mv`.

#### `/clean`
```
/clean [days]                              # default 180; orphans PROTECTED
/clean orphans                             # delete only orphans (source missing)
/clean 180 --include-orphans               # age + orphan deletion
/clean inbox [days]                        # clear old _Inbox/processed/ files
```
- Deletes old snapshots from `_Archive/Snapshots/` after confirmation.
- **Safety nets**: orphan protection by default; **closure-snapshot 30-day floor** (pre-closure snapshots from `/prune` or `/status active→closed` survive ALL modes for 30 days — no flag override); modified-source protection; completed prune manifests kept 30 days.

#### `/archive-callouts`
```
/archive-callouts                          # vault-wide dry-run preview, 180d default
/archive-callouts 180                      # execute vault-wide sweep
/archive-callouts NVDA [90]                # scoped preview / execute
```
- Sweeps addressed callouts older than the threshold into `## Legacy Callouts` as plain bullets (sorted descending). Skips fresh callouts, anything `[[pinned]]`, and all of `Research/`.
- **Creates**: per-file `(pre-callout-sweep ...)` snapshots. **Modifies**: target bodies + `Callout sweep:` Log entry. Zero sector/macro/`_hot.md`/graph side effects.
- Empty/missing threshold = dry-run — never silently executes. Undo: `/rollback [TICKER]` → `(pre-callout-sweep ...)` snapshot, or `/rollback callout-sweep-YYYY-MM-DD-HHMMSS` for the whole batch.

#### `/rollback`
```
/rollback                                  # list all snapshots
/rollback NVDA                             # list snapshots for NVDA
/rollback NVDA - Nvidia (pre-sync 2026-04-16-2115)    # restore specific snapshot
```
- **Creates**: pre-rollback safety snapshot. **Modifies**: restored note, sector note (if touched), `_hot.md`; clears matching `.graph_invalidations` on status-revert.
- Detects multi-file cascades and offers atomic restore; shows a diff before confirming.
- **Follow-up**: `/sync TICKER` or `/sync all` (cascade); `/graph` (full) if a closure was recreated.

#### `/rename`
```
/rename META "Meta Platforms"
```
- Renames `Theses/TICKER - Old.md` → `TICKER - New.md` and rewrites every inbound reference. TICKER itself never changes. Details: [[#Renaming a thesis|§10]].
- **Follow-up**: `/graph` (full — not `last`; see [[#`/graph last` vs `/graph` after `/rename`|§13]]). Undo: `/rename TICKER "[OldName]"`.

### Data refresh

#### `/transcript`
```
/transcript NVDA                           # latest quarter vs prior 2 (default)
/transcript NVDA Q1-2027                    # specific quarter
/transcript NVDA --list                     # list available FMP transcript quarters
```
- Pulls the earnings-call transcript from Financial Modeling Prep, splits prepared-remarks vs Q&A, and extracts management-commentary deltas (new/dropped language, hedging density, specificity, Q&A skeptical tone, guidance shape) vs the prior 2 quarters. **Creates**: thesis-delta Research note (`source_type: earnings`). **Modifies**: thesis Log (`Transcript ingested:` — non-skill-origin, so `/sync` propagates) + `_hot.md` (ART + OQ).
- Requires an FMP key in `.data/config.json`; aborts gracefully without it. Foreign tickers use the thesis frontmatter `ticker:` (e.g. `000660.KS`) as the FMP symbol.
- **Follow-up**: `/sync TICKER` → `/graph last`.

#### `/numbers`
```
/numbers NVDA                              # refresh one thesis's Key Metrics table
/numbers --all                             # refresh every active thesis (vault-wide lock)
```
- Surgical refresh of the `## Key Metrics` table from FMP (market cap, multiples, margins, growth, forward P/E, FY revenue) with materiality flagging. Delegates the label→field mapping + delta math to `numbers_compute.py`; the LLM renders currency-correct cells. **Creates**: per-thesis pre-edit snapshot. **Modifies**: Key Metrics table + `key_metrics_last_refreshed:` frontmatter only — does NOT create Research notes or propagate.
- Custom / forward-period / non-FMP-mapped rows are left untouched. Requires the FMP key.
- **Follow-up**: none required (surgical); `/sync TICKER` only if a material delta changes the thesis.

---

## 6. Anatomy of Vault Content

### Thesis note (15 sections)
`/Theses`, named `TICKER - Company Name.md`. Frontmatter: `date`, `tags`, `status` (draft|active|monitoring|closed), `conviction` (high|medium|low), `sector`, `ticker`, `source`.

1. Summary · 2. Key Non-consensus Insights (3–5, what the market misses) · 3. Outstanding Questions (skeptical-IC questions) · 4. Business Model & Product Description · 5. Industry Context · 6. Key Metrics (table) · 7. Bull Case · 8. Bear Case · 9. Catalysts · 10. Risks · 11. Conviction Triggers (falsifiable `→ HIGH if` / `→ LOW if` / `→ CLOSE if`) · 12. Mental Models (fired triggers as hypotheses-to-test; self-populating) · 13. Related Research · 14. Legacy Callouts (auto-managed by `/archive-callouts` — never hand-edit) · 15. Log (dated entries, max 2 lines each)

### Research note
`/Research`, named `YYYY-MM-DD - [Topic or Ticker] - [Source Type].md`. Frontmatter: `date`, `tags`, `status`, `sector`, `ticker`, `source` (immutable), `source_type`.

Required sections (all source types): **Thesis Delta** (what this changes for the investment case), **Summary** (the source's actual argument and mechanism — prose, not a business description), **Evidence** (data points, tables preferred), **Contradiction Check** (which specific assumption this supports or challenges). Conditional: **Framework / Mental Model** (source advances a named framework), **Key Segments** (source >15,000 words), **Source Excerpts** (sparing quotes). Body length scales with source length — full curve in `.claude/skills/ingest/SKILL.md` check #5.

A good Research note is a thesis-centric interpretation of what the source means — not a summary of the source.

### Sector note (12 sections)
`/Sectors` — a Map of Content per sector: 1. Active Theses (MOC navigation, first) · 2. Key industry questions · 3. Industry history · 4. Competitive dynamics · 5. Product level analysis · 6. Acquisitions and new entrants · 7. Macro shifts · 8. Investor heuristics (what's priced in vs where consensus is wrong) · 9. Mental Models · 10. Related Research · 11. Legacy Callouts · 12. Log

### Macro note
`/Macro & Technology` — freeform: geopolitical scenarios, commodity frameworks, rates/FX, technology trends with adoption frameworks and re-rating catalysts. Sector-specific dynamics belong in sector notes.

### Inline callouts — user feedback markers

Visual markers for feedback on LLM-generated content, dropped inside any thesis/sector/macro section. Opt-in, co-located with the content they comment on.

#### The 4 types

| Callout | Hotkey | Use when |
|---|---|---|
| `> [!question]` | `Mod+Alt+1` (yellow ❓) | Ask a question |
| `> [!error]` | `Mod+Alt+2` (red ⚡) | Flag disagreement |
| `> [!tip]` | `Mod+Alt+3` (teal 🔥) | Suggest a change |
| `> [!todo]` | `Mod+Alt+4` (blue ☑) | Specify an action |

`Mod` = ⌘ on macOS, Ctrl on Windows/Linux. Templates: `Templates/_callouts/user-*.md` (`user-warning.md` inserts `[!error]` — the filename is the stable hotkey slot).

#### Lifecycle

| State | Syntax | Meaning |
|---|---|---|
| **Fresh** | `> [!question] 2026-04-21` | Unresolved |
| **Addressed** | `... → Addressed 2026-04-22` + `**Prompt:**` + `**Response:**` | Claude handled it |
| **Pinned** | header contains `[[pinned]]` (fresh or addressed) | Exempt from sweep — persistent revisit slot |
| **Legacy** | plain bullet in `## Legacy Callouts` | Swept archive; read-only |

**Pin / unpin** = manual text edit of `[[pinned]]` in the header. Don't create `pinned.md` — it's an intentionally unresolved wikilink (`/graph` and `/lint` skip it). Use for questions you want to re-answer periodically as new data arrives (e.g. *"Will Samsung SF2P sustain >70% yield through HBM4 16-Hi ramp?"* — re-address each earnings). Claude addresses pinned callouts normally; the marker only governs sweep behavior.

**Re-opening an addressed callout**: delete the `→ Addressed` token, `**Prompt:**` line, and `**Response:**` block (the `[[pinned]]` marker stays). Next "address" request re-answers with current data.

> `[[preserve]]` is **deprecated** (2026-04-29) — replace with `[[pinned]]`; `/lint` flags stragglers.

#### Addressed-callout format contract

```markdown
> [!type] YYYY-MM-DD → Addressed YYYY-MM-DD
> **Prompt:** *<verbatim original user prompt, body italicised>*
>
> **Response:** <1-3 sentence conclusion>. <Pointer to body location: §Section → Subsection>.
```

- Both labels bold; user prompt italicised, response plain — the body styling distinguishes user input from Claude output.
- User wording preserved verbatim (no paraphrase, no typo fixes); multi-line prompts collapse to one italic line.
- One blank `>`-prefixed line between Prompt and Response.
- Retroactive only when re-touching a callout — don't sweep old ones purely to reformat.

#### Callout-is-ledger / body-is-deliverable rule

Callouts are an audit trail, not appendix storage. Evergreen analysis belongs in the note's spine:

| Situation | Analysis goes | Response block contains |
|---|---|---|
| Analytical question, multi-paragraph answer | Existing body section (or new subsection only if orthogonal) | 1-3 sentence conclusion + `§Section → Subsection` pointer |
| Editorial ask (table, typo, rename) | The edit IS the integration | Description of the edit |
| No natural body home, creating one out-of-scope | Stays in the callout | Full content + Log flag: `... — response retained in callout, no natural body home` |

**Why**: swept callouts become invisible to `/brief`, `/deepen`, `/graph`, `/sync`, and to anyone scanning the spine. **Smell test**: a Response with a table or >3 sentences means the integration didn't happen.

#### Workflow

1. Drop callouts (Mod+Alt+1..4) → 2. Ask Claude to address fresh callouts → 3. Claude edits sections, marks addressed, appends Log entry → 4. `/sync TICKER` → 5. `/graph last`

#### Chat prompt template

Copy-paste, swap the target:

> Read [[Theses/TICKER - Company Name]] and address every fresh `[!question]`, `[!error]`, `[!tip]`, and `[!todo]` callout. For each: (1) place the full analysis in the most natural body section (existing or new subsection if genuinely orthogonal); (2) rewrite the callout header to `→ Addressed YYYY-MM-DD`; (3) insert `> **Prompt:** *<verbatim original user prompt>*` (bold label, italic body); (4) write a brief `**Response:**` block — 1-3 sentences of conclusion + pointer to body location (`§Section → Subsection`). Editorial-only callouts (formatting, typos, renames) skip the body integration — the edit IS the integration. Append ONE Log entry prefixed exactly `Addressed user callouts:` summarizing all edits. Do NOT use skill-origin prefixes like `Deepened:`, `Status change:`, or `Stress test:`.

Multi-note variant: *"every thesis I've touched since [date]"* or *"every thesis in [[Sectors/X]]"*.

#### Propagation contract

`/sync` classifies Log entries by prefix — callout-addressing MUST use a non-skill-origin prefix:

| Prefix | Propagation |
|---|---|
| `Addressed user callouts:` (recommended), `Manual edit:`, `Reviewed:`, `Refined:` | ✅ sector/macro propagate |
| `Deepened:`, `Status change:`, `Conviction reaffirmed`, `Stress test:` | ❌ silently skipped |

**Silent failure**: skill-origin prefix → thesis updates but sector/macro stay stale, no error. Detect via `Skill-origin classified theses:` in `/sync` output; fix with a `Manual edit:` Log entry + re-`/sync TICKER`.

#### When to use /deepen instead

Callout-addressing has **no pre-edit snapshot** — regret recovery is `git checkout` only.

| Situation | Use |
|---|---|
| Rewrite >3 paragraphs | `/deepen TICKER [section]` (snapshot + manifest) |
| Single bullet / sentence / data point | Callout → address → `/sync TICKER` |
| "Claude, pick what to fix" | `/deepen` (auto-detects weakness) |
| Concrete asks ("add X, Y, Z") | `[!todo]` callout |

Safety override: prefix the request with *"Before addressing, copy [[Theses/TICKER]] to `_Archive/Snapshots/TICKER (pre-callouts YYYY-MM-DD-HHMMSS).md` with `snapshot_trigger: callouts`, then address."*

#### Sweeping addressed callouts into Legacy Callouts

`/archive-callouts` consolidates old addressed callouts into `## Legacy Callouts` (above `## Log`) as compact bullets, sorted descending — full body + Response preserved, `[!error]` labelled `warning`:

```markdown
- **2026-01-15** · warning · Bull Case · raised 2025-06-14 → Moat claim disputed — need Q4 evidence.
  - **Response:** Integrated Q4 Stagwell economics into Bull Case bullet #1. See Log 2026-01-15.
```

The sweep Log entry (`Callout sweep:`) is skill-origin and drift-excluded — pure hygiene. Undo: `/rollback TICKER` → `(pre-callout-sweep ...)` snapshot. If you plan to quote a >180d Response in an upcoming `/deepen`, pin it first or sweep after.

#### Conviction drift integration

Sequential `[!error]` addressing accumulates weakening Log entries that count toward `/sync`'s drift window (e.g. 4/5 recent updates flagged headwinds → ⚠️ drift flag). Natural next step: `/status TICKER conviction high→medium [callout-driven]` — the bottom-up parallel to the `/stress-test` → `/status` path.

#### Skill combos

| Skill | Pattern |
|---|---|
| `/ingest`, `/stress-test`, `/compare`, `/scenario`, `/surface` | Drop callouts on affected theses after propagation — addressing = post-skill quality gate |
| `/brief`, `/catalyst` | Don't callout these (ephemeral output) — callout the source thesis |
| `/deepen "Legacy Callouts"` | Refused — auto-managed archive |
| `/graph last` | Run after callout `/sync`; NOT needed after `/archive-callouts` |

#### Anti-patterns

| Pattern | Fix |
|---|---|
| Drop callouts, never address | Weekly clearance, or `[[pinned]]` for revisit slots |
| Address, never `/sync` | Always `/sync TICKER` after addressing |
| `[!todo]` for a whole-section rewrite | `/deepen TICKER [section]` |
| `[!error]` on every other bullet | Thesis is broken — `/stress-test` → reconsider conviction |
| Callouts in `_catalyst.md`, briefs, Research notes, archived theses | Callout the live thesis (or `/rollback` to reopen first) |
| Hand-edit `## Legacy Callouts` | `/rollback` to pre-sweep; use `[[pinned]]` |
| Sweep during an active callout session / skip dry-run | Let 24h pass; always preview first |

#### Setup (one-time per vault clone)

Hotkey and Templater configuration ships via git — new clones inherit it with zero setup. Verification table and from-scratch rebind steps: [[Setup Guide#5. First Obsidian launch|Setup Guide §5]].

---

## 7. Research & Thesis Building

Skill reference: [[#5. Skill Reference|§5]].

### Earnings analysis
Automated: `/transcript TICKER` (pulls the FMP transcript, extracts management-commentary deltas / hedging / Q&A tone vs the prior 2 quarters, writes a thesis-delta Research note) → `/sync TICKER`. For a non-FMP transcript URL, `/ingest [URL]` → `/sync TICKER` still works. Manual (more control):
```
Fetch [TICKER]'s latest earnings transcript from [URL]. Extract: revenue
by segment, margin trends, management guidance changes, and anything
that contradicts or strengthens my thesis. Save as a research note and
append a thesis log entry with conviction impact.
```

### Research a specific angle
```
Research [TOPIC] for [TICKER]. Focus on [specific angle: e.g. "pricing
power durability", "customer concentration risk", "management capital
allocation"]. Save to Research/ and update the relevant thesis log.
```

### "Teach me" deep-dive
```
I want to deeply understand [TOPIC: e.g. "how hybrid bonding works at
the physics level"]. Write a comprehensive explainer using my vault
content as starting context, supplement with your knowledge, and save
as a research note. Link to every relevant thesis. Write for an
investment analyst — focus on why it matters for pricing power and
competitive moats.
```

### Source-type recipes

#### YouTube transcripts (via Gemini)
YouTube URLs can't be `/ingest`ed directly. Open Gemini, paste the URL + the prompt below, save the output as `YYYY-MM-DD - [Channel Name | Video Title] - video-transcript.md` in `_Inbox/`, then `/ingest` → `/sync`.

**Gemini prompt** (copy verbatim, swap the URL):

~~~
Transcribe this YouTube video ([YOUTUBE_URL]) in full. Output in the exact format below — no deviations, no additions. Save your output as a .md file (in this format: `[Video Upload Date in YYYY-MM-DD format] - [Channel Name | Video Title] - video-transcript.md`) that can be downloaded.

Start with this YAML frontmatter block (fill in every field):

date: [YYYY-MM-DD]
source: [the YouTube URL]
source_type: video-transcript
channel: [YouTube channel name]
video title: [Video title]
speakers: [comma-separated list of speakers identified in the video]
topics: [3-5 keyword tags describing the core subjects covered]
duration: [video length in MM:SS or HH:MM:SS]

Then two sections:

Summary
3-5 sentences describing what the video covers. No analysis or opinion — just scope and subject matter. Include who is speaking and in what context (interview, presentation, panel, podcast, etc.).

Transcript
The full transcript of the video. Follow these rules exactly:

Label speakers in bold where identifiable (e.g., Host:, Jensen Huang:). If a speaker's name is unknown, use a consistent label (e.g., Interviewer:, Guest:).
Insert paragraph breaks at natural topic shifts — do not output a wall of text.
Preserve exact phrasing, numbers, company names, ticker symbols, and financial terminology. Do not paraphrase or clean up spoken language beyond basic readability.
Do not add timestamps.
Do not add section headers within the transcript.
Do not add commentary, annotations, or analysis.
If a word or phrase is unclear in the audio, write [inaudible] rather than guessing.
~~~

#### Deep Research PDFs
Drop into `_Inbox/`, run `/ingest` (auto-chunks >10-page PDFs). Figures don't auto-extract — screenshot load-bearing figures and embed with `![[filename.png]]`.

#### Paywalled articles
Extract with Safari Reader or defuddle, save as `.md` in `_Inbox/`, then `/ingest`.

---

## 8. Portfolio-Level Analysis

Skill reference: [[#5. Skill Reference|§5]].

### 8.1 Structured periodic review

`/retro` (backward — what thinking and market did) pairs with `/surface` (forward — what to research next) and `/catalyst` (forward — event calendar). Run all at monthly cadence; add `/surface all` quarterly for cross-section pattern detection.

### 8.2 Manual portfolio prompts
Exposure heatmap:
```
Read all active thesis notes. Categorise each by: primary sector,
geographic exposure, macro sensitivity (rates, FX, commodity,
geopolitical), and position in the technology adoption curve. Identify
unintentional concentration risks — am I overexposed to any single
factor across multiple "independent" theses?
```

"What am I missing?":
```
Read my sector notes and thesis notes. Based on the industries I'm
already tracking, which adjacent companies or sub-sectors am I NOT
covering that my existing research implies I should be? Prioritise by
how directly my existing theses depend on them.
```

Value chain canvas:
```
Read my [SECTOR]-related thesis notes. Map the supply chain — who is
whose customer, supplier, or competitor. Identify single points of
failure and which thesis benefits most from a bottleneck at each node.
Output as a canvas file.
```

---

## 9. Conviction & Status Management

Skill reference: [[#`/status`|§5 /status]].

### Conviction recalibration (manual)
```
Read all thesis notes with conviction: high. For each, check the most
recent log entry date. If the last update was more than 60 days ago,
flag it as stale. Summarise what has likely changed since the last
update based on the sector note and recent research.
```

---

## 10. Vault Maintenance

Skill reference: [[#5. Skill Reference|§5]].

### Renaming a thesis
When a company's name changes (Square → Block):

```
/rename TICKER "New Name"
```

TICKER stays; only the name after ` - ` changes. Atomically: renames the file, rewrites every inbound wikilink (7 patterns), updates `_graph.md` adjacency header, sector Active Theses, snapshot `snapshot_of:` fields, and `_hot.md` mentions; creates a pre-rename snapshot.

If any wikilink rewrite fails, a `.rename_incomplete.TICKER` marker drops and **every ticker-scoped skill on TICKER hard-blocks** until cleared. Recover: re-run `/rename TICKER "[same new name]"` — the completed `mv` is skipped, only failed edits retry.

**Always run `/graph` (full) after `/rename`**, not `/graph last` ([[#`/graph last` vs `/graph` after `/rename`|§13]]). Undo: `/rename TICKER "[OldName]"`.

### Manual audit prompts

Find orphaned research:
```
List all research notes in Research/ that are not wikilinked from any
thesis or sector note. For each, suggest which thesis or sector it
should connect to, and why.
```

Frontmatter audit:
```
Scan all notes in Theses/ and Research/. List any missing required
frontmatter fields. Flag thesis notes where status is "draft" but the
note has 3+ log entries — these are probably "active".
```

Tag taxonomy cleanup:
```
List all unique tags across the vault. Flag duplicates or inconsistencies
(e.g. #semi vs #semiconductors). Suggest a consolidated tag list.
```

Template compliance:
```
Compare each thesis note against the Thesis Template. List missing
sections — especially Key Non-consensus Insights and Outstanding
Questions. For each gap, suggest which Research/ notes could fill it.
```

Learning from closed theses:
```
Read my last 5 closed theses in _Archive/. For each, what evidence was
in the vault 90 days before closure that, in hindsight, should have
triggered closure sooner? Build a "lagging indicator I ignored" list
I should scan for on active positions quarterly.
```

---

## 11. Prompt Library

High-value free-form prompts. Copy, paste, adapt — many of the best research moves are conversational, not procedural.

### A. Session framing
```
I have 2 hours. Based on _hot.md and the last 7 days of Log entries
across my theses, rank the three highest-value things I could do right
now. For each, estimate time cost and the specific decision it would
unblock.
```
```
What research assumption have I been leaning on across 3+ theses that
I haven't re-validated in the last 6 months? For each, cite the theses
it props up and the evidence decay risk.
```

### B. Thesis revision & self-audit
```
Review my [TICKER] thesis as if writing it from scratch today using
only current research. Flag the sections where the original framing
no longer matches the evidence — list the specific sentences that
need rewriting.
```
```
For [TICKER], extract every falsifiable prediction embedded in the
thesis (explicit and implicit). For each, state: what would have to
happen to falsify, has it happened, and how would I know.
```
```
Compare my stated investment philosophy in CLAUDE.md ("qualitative,
non-consensus") to the substance of my last 10 thesis edits. Where am
I drifting from my own principles?
```

### C. Cross-thesis synthesis (non-consensus insight generation)
```
Read all my thesis notes. Identify 3-5 non-obvious connections between
companies in different sectors that share a common dependency, risk,
or catalyst the market is likely pricing independently. For each,
explain why the correlation matters and what trade it implies.
```
```
Find all thesis notes where I assert pricing power. For each, cite the
specific evidence in Research/ supporting the claim and flag any
thesis where "pricing power" appears in the Summary but has no
evidentiary base.
```
```
Which of my bull cases share an implicit macro dependency (AI capex,
rates path, dollar trajectory, China tech decoupling)? Group by
dependency and assess whether I'm double-counting diversification.
```
```
Read my 10 oldest thesis notes. For each, challenge whether the "Key
Non-consensus Insights" section is still non-consensus today. Which
have been absorbed into the market narrative?
```
```
Scan my vault for internal contradictions — places where one note's
bull case depends on an assumption that another note's bear case
challenges. List each contradiction with links to both notes.
```
```
Read my macro note on [TOPIC]. Trace second and third-order effects
through my sector notes and thesis notes. Which thesis is most
exposed to a risk I haven't written down? Which company benefits
from a dynamic I've documented in a different sector but haven't linked?
```
```
Read my [TICKER] thesis. Assume the bear case plays out fully. Which
of my OTHER theses benefits most from that scenario? Map the hedging
relationships across my portfolio using only vault content.
```

### D. Memo & communication
```
Draft a Sunday-night email to myself: the 5 highest-signal vault events
of the past week, the 3 open decisions for Monday, and the 1 thing
I'm procrastinating on.
```
```
Write an IC meeting agenda for my top-3 highest-conviction positions.
For each: one-slide pitch, 3 catalysts, 1 falsification trigger.
```
```
Given my [TICKER] thesis, write the "I was wrong" post-mortem I'd
write 18 months from now if the thesis broke. Identify the evidence
currently in my vault that this post-mortem would cite.
```
```
I want to explain [TICKER]'s moat in 60 seconds. Draft three versions:
for a PM, for a junior analyst, and for a non-specialist friend.
```

### E. Portfolio construction
```
Given my active theses, force a 5-bucket ranking based on conviction ×
catalyst horizon × liquidity × macro correlation. No optimisation —
just surface the order I'd have to defend.
```
```
If I could only hold 5 of my current active theses for 12 months,
which 5 and why? Apply the "can I still sleep if this drops 30%"
test to each survivor.
```
```
Reverse-engineer the worldview my portfolio encodes. List 5 non-obvious
macro assumptions my current positioning implicitly bets on.
```

### F. Pattern & heuristic extraction
```
Read my 5 most recent /stress-test Research notes. What failure modes
recur? Turn the pattern into a pre-thesis checklist I should apply
before promoting any new draft to active.
```
```
Read all Log entries from the past 90 days across the portfolio. What
recurring types of evidence drive conviction changes? Turn the top 3
into a watchlist I should auto-check on every new thesis.
```
```
Read my 5 most recent /surface Research notes. Which opportunities
that I flagged have I NOT acted on? For each, assess whether the
opportunity is still live and why I might be avoiding it.
```

### G. Source triangulation
```
Before I read [long article/book], summarise what the vault already
knows about [TOPIC] so I can read actively and only note new
information.
```
```
I'm about to read [source]. Given my current [TICKER] thesis, generate
3 questions I should try to get answers to from this source.
```
```
Read the latest Research note on [TOPIC]. What's the single most
important follow-up source I should try to find? Give me a specific
search query or document type.
```

### H. Selection-driven (use with editor/browser selection)
```
Read this. Which of my theses does it update? Draft a 2-line Log entry
per affected thesis with conviction impact.
```
```
Given the selected text from [TICKER]'s earnings transcript, extract
only the pieces that contradict or strengthen a specific sentence in
my thesis. Ignore everything else.
```
```
The selection is an analyst note I disagree with. Read my [TICKER]
thesis, then write a point-by-point rebuttal grounded only in my
vault evidence.
```

### I. Debate & pre-decision (lighter than /stress-test)
```
Argue against my decision to downgrade [TICKER]. Use only vault
content. Don't be polite — tell me which specific evidence I'm
discounting.
```
```
My gut says sell [TICKER]. Before I act, steelman holding. What in
the vault argues for patience that my gut is dismissing?
```
```
I'm considering sizing up [TICKER]. Before I do, read the thesis and
list the 3 pieces of evidence I should re-verify within 48 hours of
adding.
```

### J. Historical analogy & management quality
```
Read my thesis for [TICKER]. Find the closest historical analogy —
a company in a similar position (market structure, technology
transition, investor sentiment) 5-15 years ago. What happened, and
what does the analogy imply? What breaks the analogy?
```
```
Research the management team of [TICKER]. Focus on: capital allocation
track record, insider ownership, previous roles, and compensation
alignment. Save as a research note and update the thesis.
```
```
Read my [TICKER] thesis. Decompose the TAM bottom-up: who are the
actual customers, what do they pay today, what would need to change
for [TICKER] to capture X%, and what's the realistic timeline?
Compare to the top-down narrative. Save as a research note.
```

### K. Canvas & visual
```
Create a canvas showing all active theses grouped by sector, with
edges showing supply chain relationships, competitive dynamics, and
shared macro exposures. Colour-code by conviction level.
```
```
Create a canvas for [TICKER] showing the evolution of my thesis over
time. Use the Log entries as nodes, with annotations showing how
conviction and key arguments changed at each point.
```

---

## 12. Cadence Guide

### Weekly (Friday evening, or after heavy research)
- `/retro 1w` — what you resolved, what the market priced, trade ideas from the gap
- `/surface` or `/surface [sector]` on your current focus
- `/catalyst` to refresh the forward calendar
- `/lint TICKER` for any thesis you actively edited

### Monthly (first trading day)
- `/retro 1m`
- [[#Monthly maintenance|§3.4 Monthly maintenance]]
- Review `_hot.md` conviction changes and drift flags
- "Conviction recalibration" prompt from [[#Conviction recalibration (manual)|§9]]

### Quarterly (first trading day)
- `/retro 1q` · `/surface all` (deep cross-section review) · `/prune` · `/archive-callouts 180`

### Event-triggered

| Event | Workflow |
|-------|---------|
| Earnings reported | [[#Earnings reaction|§3.2]] |
| Macro shock | [[#Macro shock|§3.2]] |
| New stock idea | [[#New position — full build|§3.1]] |
| Drift flagged by `/sync` | [[#Conviction drift response|§3.2]] |
| Competitor news | `/ingest [URL]` → `/compare` affected → `/sync` |
| Sector rotation | `/surface [sector]` → `/scenario` if macro-driven → `/compare` key players |
| `/retro` inverted-bear on a position | `/stress-test TICKER` → `/status` if warranted → `/sync` |
| `/retro` flow-bull on an uncovered ticker | `/ingest [news URL]` → `/thesis TICKER` |

Update `CLAUDE.md` whenever you add folders, change conventions, or shift research focus.

---

## 13. Caveats & Gotchas

### `.last_sync` deletion
If deleted, the next `/sync` treats the vault as first-run and re-reads every file (5–10× slower). `/prune` detects this and prompts. `touch .last_sync` recovers speed but silently marks pending files as synced — usually wrong; prefer letting the next `/sync` re-process.

### First-run `/sync` on populated vaults
The first `/sync` on an existing vault reads everything — expected; it establishes the watermark baseline.

### Draft→active has no snapshot
`/status TICKER status draft→active` skips the confirm prompt and creates no snapshot. To reverse: manually flip frontmatter back to `draft` and trim the Log entry — there is no `(pre-status)` snapshot to roll back to.

### Archive-collision prompt
`/thesis TICKER` with a prior archived thesis (detected via filename, frontmatter, registry, or snapshot trail) pauses with four options: **(a)** exit to `/rollback` (want continuity) · **(b)** proceed, note predecessor in Log (auditable) · **(c)** proceed clean · **(d)** cancel.

### Propagated-research caveat after rollback
`/rollback` restores files but does NOT rewrite `propagated_to:` on Research notes consumed by the reverted `/sync` — so the next `/sync` skips re-propagation, silently leaving the thesis pre-propagation. Force re-propagation: remove the ticker from that note's `propagated_to:` list, or delete the note and re-`/ingest`.

### `/graph last` vs `/graph` after `/rename`
`/rename` rewrites only the renamed thesis's adjacency header; if any other thesis was ever manually `mv`'d, `/graph last` carries that stale baseline forward. `/graph` (full) re-derives every header (30–60s vs ~5s). Skip only if certain no manual renames happened.

### Draft theses invisible to sector scope
Draft theses are omitted from sector Active Theses lists, which sector-scoped skills (`/surface [sector]`, `/prune [sector]`) use to resolve scope — drafts are silently skipped. Promote to `active` before sector-scoped runs.

### Concurrency (single-session rule)
Two ticker-scoped skills on different tickers can hold locks in parallel, but both Edit `_hot.md` uncoordinated — the later write wins. **Treat Claudian as single-session**; sequential invocations in one session are safe.

### `/ingest` same-source hard-block
A URL already ingested today hard-blocks; older same-source ingests prompt append/supersede/cancel. If the prior note is a stub, delete it from `Research/` first.

### `/brief` and `/surface` don't fully refresh the graph
Both create Research notes without advancing thesis mtimes or `.graph_invalidations` — new notes appear in the Orphan Research list only on the next full `/graph` rebuild (or once a thesis Edit wikilinks them).

### Pending graph work persists across sessions
`.graph_invalidations` persists until the next `/graph last` or `/graph` consumes it; `/lint` flags stale files.

### Dated infrastructure changes
Time-boxed rollouts live in [[_Archive/Docs/Changelog.md]] — this section holds only evergreen caveats.

---

## 14. How the Vault Stays Consistent

Short reference; deep mechanics in [[INFRASTRUCTURE]].

| File | Role | Owned by | Short story |
|---|---|---|---|
| `_graph.md` | Dependency map | `/graph` | Rebuilt by `/graph` (3 modes). Other skills signal via thesis mtime or `.graph_invalidations`. |
| `_hot.md` | Session context cache (6 sections) | Shared (14 writers) | Soft cap 4,000 / hard 5,000 words. Compression drops whole entries, never truncates (`_shared/hot-md-contract.md`). |
| `_catalyst.md` | Catalyst calendar | `/catalyst` | Regenerated each run; pre-regenerate snapshot protects against mid-run failure. |
| `.last_sync` | Sync watermark | `/sync` (default, all) | `/sync TICKER` preserves it; `/graph` never touches it. |
| `.sync_all_fresh` | Full-rebuild marker | `/sync all` → `/graph` | Forces the next `/graph` into full rebuild; cleared on success. |
| `.graph_invalidations` | Deferred neighbor updates | `/status`, `/prune` (closures) | Consumed and deleted by `/graph last`. |
| `.rename_incomplete.TICKER` | Failed-rename repair marker | `/rename` | Hard-blocks ticker-scoped skills until cleared; re-run `/rename` to repair. |
| `_Archive/Snapshots/` | Version control | Shared | Pre-edit snapshots + crash-recovery manifests. Cleaned by `/clean` (30-day closure floor). |
| `.archive_ticker_registry.md` | Archive ledger | `/status`, `/prune` closures | Append-only; consumed by `/thesis` collision detection. |

**Key invariants**:
- `_graph.md` is written only by `/graph` (plus one surgical `/rename` header update).
- Every destructive skill snapshots first; recovery is `/rollback`.
- Every state-modifying skill runs pre-flight (lock + rename-marker + sanitization + section probe): `.claude/skills/_shared/preflight.md`.

### Skill execution matrix

| Skill | Model | Context |
|---|---|---|
| `/sync`, `/ingest`, `/thesis`, `/deepen`, `/stress-test`, `/compare`, `/scenario`, `/brief`, `/catalyst`, `/transcript` | Opus max | Main |
| `/surface`, `/retro` | Opus max | Delegated subagent (Agent tool; report re-emitted verbatim) |
| `/prune` | Opus max | Split — analysis delegated, mutation in main thread under the approval gate |
| `/lint` | Opus max | Main — mechanical checks run by `lint.py` (~40 of 55); judgment pass reads only flagged files |
| `/graph`, `/rename`, `/rollback`, `/status`, `/clean`, `/archive-callouts` | Sonnet max | Main |
| `/numbers` | Sonnet (effort medium) | Main — arithmetic delegated to `numbers_compute.py` |

**Execution mechanism (2026-07-08)**: "Delegated" / "Split" skills use **Agent-tool delegation**, not frontmatter `context: fork` — the latter was reverted 2026-06-07 (it returned the report as unrendered stdout, leaving the chat panel blank). Under delegation the subagent does the heavy reads and returns the report as a tool result, which the main thread re-emits verbatim; rendering is preserved and main-context cost is just the returned report. `/catalyst` still runs inline (its mandatory live-progress contract conflicts with delegation — pending a decision). Each skill's own SKILL.md "Execution context" section is the source of truth.

Sonnet-max skills are mechanical (extraction, renames, frontmatter, age math) — faster with no observed correctness impact; watch `/status` trigger-conflict detection and `/rollback` cascade classification for regressions. Rollout history: [[_Archive/Docs/Changelog.md]].
