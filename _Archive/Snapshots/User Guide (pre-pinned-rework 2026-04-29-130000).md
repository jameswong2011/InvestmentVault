# User Guide — Claude Code + Obsidian for Investment Research

> Your vault has **40 theses**, **133 research notes**, **13 sector notes**, and **6 macro notes**. This guide covers what to do, in what order, and when to prompt freely instead of invoking a skill.
>
> **How to read this guide.** Start with §0–§2 to get working. Use §3 as a workflow menu. Use §4 to pick a chain from an intent. Use §5 as the skill dictionary. Use §11 (Prompt Library) to supplement skills with free-form prompting. Reach for §13–§14 only when debugging or on first use.

---

## 0. First Run

If this is a brand new vault (no prior `/sync` runs):

```
/sync        # creates _hot.md + .last_sync, reads all vault files
/graph       # creates _graph.md from vault state
```

After bootstrap, all skills work. Without it, `/sync TICKER` and scoped `/surface` block (they need `_graph.md`), and `/prune`'s unsynced-research check has no baseline.

If the vault already has content, `/sync` on first run reads everything (equivalent to `/sync all`) — this is expected.

> If `.last_sync` is ever deleted, the next `/sync` treats the vault as first-run and re-reads every file (5–10× slower). See [[#`.last_sync` deletion|§13 — `.last_sync` deletion]].

---

## 1. The Core Loop

Two complementary loops drive the vault:

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
| `/ingest` | Transforms `_Inbox/` raw material into structured Research notes with wikilinks |
| `/sync` | Propagates new insights to affected theses, sector notes, macro notes, `_hot.md` |
| Work | Research, analysis, thesis building, conviction changes, inline callouts |
| `/retro` | Aggregates the window's addressed callouts + Log entries; overlays newsflow + earnings + price; ranks trade ideas by narrative-price gap |
| `/status` / `/deepen` / `/stress-test` | Act on retro findings — conviction changes, section improvements, adversarial review |
| `/graph last` | Reconcile the dependency map after every write chain |

**Periodic maintenance (cross-cutting)**:

| Skill | Looks | Purpose |
|---|---|---|
| `/surface` | Forward | Find new ideas, portfolio blind spots, contrarian signals |
| `/catalyst` | Forward | Calendar of upcoming events across positions |
| `/retro` | Backward | What happened + what market priced since my last review |
| `/lint` | Now | Vault health check — structural, freshness, analytical |
| `/archive-callouts` | Now | Sweep resolved callouts into per-thesis Legacy archive |

Read-only chains (`/brief`, `/lint`, `/rollback` list) skip `/graph last`.

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
`/ingest` creates Research notes only. `/sync` propagates. Always run both.

### Earnings-season triage
```
Which of my thesis companies report earnings in the next 2 weeks?
For each, list the key metrics and outstanding questions from my
thesis note that the report should answer.
```

### Manual edit protocol (important)

**After manually editing a thesis body section** (Bull Case, Risks, Industry Context, Bear Case, Key Non-consensus Insights, etc.), **always append a Log entry** describing the change. Without one, `/sync` may classify the edit as skill-origin and silently skip propagation.

Any prefix not in the skill-origin registry (e.g., `Manual edit:`, `Reviewed:`, `Refined:`) forces `/sync` to treat the change as research-driven. Example:

```markdown
### 2026-04-20
- Manual edit: tightened Bull Case pricing-power argument — strengthened, added customer concentration data point from Q4 transcript
```

### User callouts — inline feedback on LLM output

Drop hotkey-triggered callout boxes inside any section to comment on what Claude wrote. Four types: `> [!question]` (⌘/Ctrl+Alt+1, yellow, ask), `> [!error]` (⌘/Ctrl+Alt+2, red, flag), `> [!tip]` (⌘/Ctrl+Alt+3, teal, suggest), `> [!todo]` (⌘/Ctrl+Alt+4, blue, action). Ask Claude *"address fresh callouts in [note]"* to have them resolved inline with a `**Response:**` block + Log entry. Periodic `/archive-callouts` sweeps old addressed callouts into a `## Legacy Callouts` archive section (plain-text audit trail, source sections decluttered). `[[preserve]]` marker exempts individual addressed callouts from sweep.

Full spec — lifecycle states, chat prompt template, cross-platform setup: see [[#Inline callouts — user feedback markers|§6 Inline callouts]].

### Referencing content in prompts

Four ways to point Claude at something specific:

| Mechanism | Syntax | Example |
|---|---|---|
| Vault wikilink in a prompt | `[[path/note]]` | "Read [[Theses/NVDA - Nvidia]] and flag stale sections." |
| Chat reference to a file | `@path/note.md` | "Summarise @Research/2026-04-15\ -\ ...\ .md" |
| Editor selection | Auto-attached as `<editor_selection>` | Select text in a note, then prompt — Claude sees the selection. |
| Browser selection (Surfing/web) | Auto-attached as `<browser_selection>` | Select text in an Obsidian browser view, then prompt. |

The current note you're viewing is always attached as `<current_note>`. You don't need to repeat the filename when referring to "this thesis" or "this note".

---

## 3. Workflow Chains

Multi-skill sequences for common scenarios. Each chain lists the minimum steps. Footnotes about failure modes live in [[#13. Caveats & Gotchas|§13 Caveats & Gotchas]].

### 3.1 Starting new work

#### New position — full build
Starting coverage on a new company from scratch.
```
/thesis TICKER
/status TICKER status draft→active [rationale]
/stress-test TICKER
/sync TICKER
```
Optional: `/compare TICKER vs COMPETITOR` before `/sync` for competitive context. `/deepen TICKER [weakest section]` to fill gaps the stress test identifies.

#### New position — from existing research
You've been collecting research on a ticker and want to formalise a thesis.
```
/ingest                                      # any inbox items first
/sync                                        # propagate to existing notes
/thesis TICKER                               # vault research auto-used
/status TICKER status draft→active [rationale]
/sync TICKER
```

#### Idea discovery → new position
Find a new opportunity from existing research.
```
/surface                                     # or /surface [sector]
/thesis TICKER                               # if an opportunity emerges
/compare TICKER vs [existing competitor]
/status TICKER status draft→active [rationale]
/sync
```

#### Acting on a surface finding
`/surface` produces a Research note with multiple opportunities. To act on one:
```
# Identify the opportunity from the latest /surface note, then either:
/thesis TICKER                               # if it's a new name to cover
# OR
/deepen TICKER [section]                     # if it extends an existing thesis
/sync
```

#### Sector deep-dive
Entering or re-evaluating an entire sector.

If the sector note doesn't exist:
```
Create a new Sector Note for [SECTOR] using the Sector Template. Search
the vault for all relevant thesis notes, research notes, and macro
connections. The "Investor heuristics" section should explicitly state
what consensus believes and where they could be wrong.
```
Then:
```
/graph                                       # register the new sector note
/surface [sector]
/compare [key players]
/sync
```

If building multiple theses inside the new sector, promote each to `active` **before** rebuilding the graph — draft theses are intentionally omitted from sector Active Theses and will be invisible to `/surface [sector]`. See [[#Draft theses invisible to sector scope|§13 — Draft theses invisible to sector scope]].

### 3.2 Responding to events

#### Earnings reaction
A thesis company just reported.
```
/ingest [transcript or press release URL]
/sync TICKER
```
If conviction changes:
```
/status TICKER conviction old→new [what the report revealed]
```
If ambiguous:
```
/stress-test TICKER                          # before deciding
```

#### Macro shock
Rate decision, geopolitical event, policy change.
```
/scenario [describe the event with quantitative parameters]
/status TICKER conviction old→new [transmission channel]    # most affected
/compare [exposed] vs [beneficiary]                          # if competitive shifts emerge
/sync
```

#### Conviction drift response
`/sync` flags `⚠️ Conviction drift` on a thesis.

- **Reaffirm** (evidence reviewed, conviction unchanged):
  ```
  /status TICKER reaffirm [why the drift signal is noise]
  ```
- **Investigate first**:
  ```
  /stress-test TICKER
  /status TICKER conviction old→new [rationale]    # or reaffirm
  /sync TICKER
  ```
- **Investigate with targeted research**:
  ```
  /deepen TICKER [section the drift relates to]
  /sync TICKER
  /status TICKER conviction old→new [rationale]
  ```

#### Catalyst-driven review
Preparing for an upcoming catalyst window.
```
/catalyst
/deepen TICKER Catalysts                     # for each imminent catalyst thesis
/prune [sector] stale                        # for theses with no catalysts flagged
```

### 3.3 Improving theses

#### Targeted improvement
A thesis section is weak, stale, or flagged by `/lint`.
```
/deepen TICKER [section]                     # omit section to auto-detect weakest
/sync TICKER
```

#### Adversarial pressure test
Before a major decision.
```
/stress-test TICKER
/deepen TICKER [section the stress test flagged]
/sync TICKER
```

#### Competitive reassessment
Competitive dynamics in a sector are shifting.
```
/compare A vs B                              # or /compare A vs B vs C
/status TICKER conviction old→new [competitive insight]    # if warranted
/sync
```
At least one ticker must have a thesis note. Tickers without theses use web research (lighter analysis, no vault updates for them).

#### Pre-meeting prep
You need to pitch or discuss a position.
```
/brief TICKER                                # 1-page memo
```
Adversarial prep (anticipate pushback):
```
/stress-test TICKER
/brief TICKER
```

#### Ad-hoc research session
Researching a topic that may affect multiple theses.
```
/ingest [URL1]
/ingest [URL2]
/sync
```
Or for manual research:
```
Research [TOPIC] for [TICKER]. Focus on [specific angle]. Save to
Research/ and update the relevant thesis log.
/sync
```

### 3.4 Maintaining the vault

#### Portfolio pruning cycle
Portfolio feels crowded or overdue for cleanup.
```
/sync                                        # first — /prune warns if unsynced research exists
/prune                                       # presents table, asks approval, applies in-line
/surface                                     # find reallocation opportunities
/graph last
```

#### Monthly maintenance
Monthly, or when the vault feels out of sync.
```
/sync all
/graph
/lint
/prune
/clean
/surface                                     # default mode — section-targeted, forks
/catalyst
/graph last
```
Run in this order. `/sync all` before `/graph` because syncs can change links. `/lint` after `/graph` to check graph health. `/prune` after `/lint` because lint flags staleness. `/surface` and `/catalyst` near the end against a clean vault. Final `/graph last` picks up closure-generated `.graph_invalidations`.

**Context note**: `/lint`, `/prune`, and `/surface` fork to a subagent — they don't pollute your main conversation context. This keeps the full chain well under the 1M context limit (~460K on a 41-thesis vault). If you want a once-per-quarter deeper pass, substitute `/surface all` for `/surface` — more comprehensive analysis at ~4× the subagent read cost, still forked so main context is unaffected.

#### Recovery — undo a bad sync
`/sync` produced changes you disagree with.
```
/rollback TICKER                             # pick the (pre-sync) snapshot
```
Rollback detects cascade operations — if `/sync` touched multiple files, it offers to restore all atomically. After rollback:
```
# Single-file cascade:
/sync TICKER
# Multi-file cascade (the common default-sync case):
/sync all
/graph
```
See [[#Propagated-research caveat after rollback|§13 — Propagated-research caveat after rollback]].

#### Recovery — undo a closure
A thesis was archived but you want to reopen it.
```
/rollback TICKER
```
The archived thesis returns to its original path. Check the restored `status:` frontmatter:
- `status: active` (typical): skip `/status`.
- `status: closed` (rare): `/status TICKER status closed→active [rationale]`.

Then:
```
/sync TICKER
/graph                                       # full — thesis structure changed
```

### 3.5 Callout-driven review

Reviewing LLM output after a content-generation skill; drop callouts inline and have Claude address them.

```
/ingest [URL] | /stress-test | /compare | /scenario | /surface [scope]
/sync TICKER → /graph last
Drop callouts (Mod+Alt+1..4) in affected thesis
"Address fresh callouts in [[Theses/TICKER]]. Prefix Log entry 'Addressed user callouts:'"
/sync TICKER → /graph last
```

Multi-thesis: drop callouts across notes, then *"Address fresh callouts in every thesis I've touched today"* → `/sync` → `/graph last`.

For large rewrites from `[!todo]` callouts, use `/deepen TICKER [section]` first for snapshot safety ([[#When to use /deepen instead|§6]]).

**Periodic hygiene**: quarterly (or when `/lint #50` flags), run `/archive-callouts` dry-run, then `/archive-callouts 180` to sweep ≥180d callouts into `## Legacy Callouts`. Full spec: [[#Sweeping addressed callouts into Legacy Callouts|§6]].

### 3.6 Retrospective review

Periodic backward-looking review. Pairs with §3.5 — callouts are mid-flight feedback; retro is the periodic aggregation of that feedback against market reaction.

```
/retro 1w                                    # weekly — full callout bodies rendered
/retro 1m                                    # monthly — compressed one-liner per callout
/retro 1q                                    # quarterly — aggregated by ticker
```

**What it scans**: addressed callouts resolved in window (with Claude's `**Response:**` text), fresh callouts still open, and `## Log` entries — split by skill-origin vs manual/user-driven.

**What it overlays per ticker**: window price move (±3% threshold), newsflow polarity (press releases, guidance, analyst actions, M&A), earnings results (beat/miss + guidance direction + transcript themes if fetched).

**What it ranks — narrative-price delta** (the core engine):

| Delta | Meaning | Weight |
|---|---|---|
| aligned-up / aligned-down | Narrative + price agree — already priced, no alpha | 0 |
| **inverted-bear** | Good news, price fell — positioning / forward-risk signal | 1.5× |
| **inverted-bull** | Bad news, price rose — capitulation / short-cover / forward-relief | 1.5× |
| flow-bull / flow-bear | No catalyst, price moved — hidden signal or positioning | 1.0× |
| unreactive-good / unreactive-bad | Event occurred, price flat — priced in or dismissed | 2.0 (fixed) |

Vault stance then determines the read: **alpha harvest** (vault predicted the gap), **missed signal** (market saw something vault didn't), or **stress-test candidate** (vault fighting the market).

**Follow-up chain** (you choose, retro never auto-executes):
```
/status TICKER conviction X→Y [reason]      # for harvest signals
/stress-test TICKER                         # for vault-fighting-market cases
/deepen TICKER [section]                    # for missed-signal cases
/thesis TICKER                              # for flow-bull/bear with no vault view
/sync → /graph last                         # after any of the above
```

**Immutable output**: each run writes a new Research note (`YYYY-MM-DD - Retrospective Xw - Synthesis.md`), never overwrites a prior retro. The historical trail of how thinking evolved vs market is the secondary output.

Retro auto-appends a `Retro insight:` Log entry to the thesis of each Top-3 trade idea (non-skill-origin prefix — `/sync` propagates downstream sector/macro updates normally per Workflow Rule 6).

Cadence: see [[#12. Cadence Guide|§12]] — `/retro 1w` Friday, `/retro 1m` month-end, `/retro 1q` quarter-end.

---

## 4. Decision Guide — "I Want To..."

> Notation: `skill field old→new [reason]`. See [[#5. Skill Reference|§5 Skill Reference]] for full argument forms.

| I want to... | Do this |
|---|---|
| **Start a session** | Read `_hot.md` → `/ingest` → `/sync` |
| **Clip an article** | `/ingest [URL]` → `/sync` |
| **Process inbox** | `/ingest` → `/sync` |
| **Start covering a new company** | [[#New position — full build|§3.1 New position — full build]] |
| **Formalise collected research into a thesis** | [[#New position — from existing research|§3.1 New position — from existing research]] |
| **Improve a weak thesis** | `/deepen TICKER` → `/sync TICKER` |
| **Improve a specific section** | `/deepen TICKER [section]` → `/sync TICKER` |
| **Review & feedback on LLM output** | Drop callouts (⌘+Option+1..4) → "address callouts in [[note]]" → `/sync TICKER` → `/graph last`. See [[#3.5 Callout-driven review\|§3.5]]. |
| **Challenge a thesis** | `/stress-test TICKER` → (decide) → `/status` → `/sync` |
| **Compare competitors** | `/compare A vs B` → `/sync` |
| **Pitch a position** | `/brief TICKER` |
| **React to earnings** | `/ingest [URL]` → `/sync TICKER` → `/status` if needed |
| **React to macro event** | `/scenario [event]` → `/status` (most affected) → `/sync` |
| **Handle conviction drift** | [[#Conviction drift response|§3.2 Conviction drift response]] |
| **Change conviction** | `/status TICKER conviction old→new [reason]` |
| **Close a position** | `/status TICKER status active→closed [reason]` |
| **Reopen an archived position** | [[#Recovery — undo a closure|§3.4 Recovery — undo a closure]] |
| **Find new ideas** | `/surface` (default) or `/surface [sector]` |
| **Find portfolio blind spots** | `/surface` (section-targeted) or `/surface all` (comprehensive deep review) |
| **Act on a surface finding** | [[#Acting on a surface finding|§3.1 Acting on a surface finding]] |
| **Review what I did this week / month / quarter** | `/retro 1w` / `/retro 1m` / `/retro 1q` |
| **Recommend trades from recent research** | `/retro [window]` — ranks by narrative-price gap; see [[#3.6 Retrospective review\|§3.6]] |
| **Check where market disagrees with my thinking** | `/retro [window]` — inverted-bear/bull deltas are the positioning signal |
| **Model a "what if"** | `/scenario [event]` |
| **See what's coming up** | `/catalyst` |
| **Clean up weak positions** | [[#Portfolio pruning cycle|§3.4 Portfolio pruning cycle]] |
| **Run monthly maintenance** | [[#Monthly maintenance|§3.4 Monthly maintenance]] |
| **Check vault health** | `/lint` (full) or `/lint TICKER` (scoped) |
| **Fix graph issues** | `/graph` |
| **Undo a bad sync** | [[#Recovery — undo a bad sync|§3.4 Recovery — undo a bad sync]] |
| **Undo a conviction change** | `/rollback TICKER` → select `(pre-status)` snapshot |
| **Delete old snapshots** | `/clean` (see [[#`/clean`|§5 /clean]] for all modes) |
| **Rename a thesis (company name change)** | `/rename TICKER "New Name"` (see [[#Renaming a thesis|§10 Renaming a thesis]]) |
| **Build a sector note** | [[#Sector deep-dive|§3.1 Sector deep-dive]] |
| **Deep-dive a topic** | "Teach me [TOPIC]" → Research note → `/sync` (see [[#7. Research & Thesis Building|§7]]) |
| **Explore free-form** | [[#11. Prompt Library|§11 Prompt Library]] |

---

## 5. Skill Reference

One canonical entry per skill: arguments, what it creates, what it modifies, follow-up. Grouped by role.

**Model + context assignment**: see [[#Skill execution matrix|§14 execution matrix]]. Mechanical skills run Sonnet max; `/lint`, `/prune`, `/surface` fork to a subagent (heavy reads stay off your main-context budget).

### Core workflow

#### `/ingest`
```
/ingest                                    # batch: everything in _Inbox/
/ingest https://example.com/article        # single URL
/ingest /path/to/file.pdf                  # local file (.md, .pdf, .csv, .txt)
```
- **Creates**: Research note(s). Moves source to `_Inbox/processed/`.
- **Modifies**: none (no thesis/sector edits).
- **Follow-up**: `/sync` → `/graph last`.
- **Same-source dedup**: hard-blocks a URL ingested today with identical `source:`. Older same-source ingests surface a three-option prompt (append / supersede / cancel). Delete the prior note from `Research/` first if it's a stub or wrong.

#### `/sync`
```
/sync                                      # graph-assisted: changed files + adjacencies
/sync all                                  # brute-force: reads everything (slow)
/sync NVDA                                 # ticker-scoped: one thesis + adjacencies
```
- **Creates**: Tier A snapshots, `_sync-manifest`.
- **Modifies**: Theses, Sectors, Macro, `_hot.md`, `.last_sync` (default/all only).
- **Follow-up**: `/graph last`.

Which mode?

| Situation | Mode |
|---|---|
| Just edited one thesis or one ticker's research | `/sync TICKER` |
| Ingested or edited research touching multiple tickers | `/sync` (default) |
| Monthly cadence, or vault feels stale/inconsistent | `/sync all` |

#### `/status`
```
# Conviction change
/status NVDA conviction medium→low China risk unhedgeable

# Status transition
/status NVDA status draft→active thesis meets quality bar
/status NVDA status active→monitoring awaiting catalyst
/status NVDA status monitoring→active catalyst emerged
/status NVDA status active→closed thesis invalidated by [reason]

# Drift acknowledgment
/status NVDA reaffirm earnings miss was one-time, position unchanged
```
- **Creates**: Snapshot (except `draft→active` and `reaffirm`), `_status-manifest`.
- **Modifies**: Thesis frontmatter + Log, sector note, `_hot.md`; appends `.graph_invalidations` on closure; appends `.archive_ticker_registry.md` on closure.
- **Follow-up**: `/sync` (conviction changes), `/graph last`.
- Mandatory Tier 3 confirmation before applying, **except** `draft→active` which takes a fast-path (one-line FYI, no confirm prompt, no pre-status snapshot — see [[_Archive/Docs/Changelog.md]]).

### Analytical

#### `/surface`
```
/surface                                   # full vault, section-targeted (default — fast)
/surface all                               # full vault, full reads (comprehensive, deeper)
/surface NVDA                              # ticker + adjacencies + sector peers
/surface semiconductors                    # all theses in sector + sector + macro
```
- **Creates**: Research note (filename reflects mode — `(all)` suffix for `all`).
- **Modifies**: `_hot.md`.
- **Runs in subagent** (`context: fork`): main conversation context is shielded from the vault read. Only the final top-3-insights summary returns to main.
- **Follow-up**: `/deepen` or `/thesis` on opportunities; `/graph last`.

Which mode?

| Situation | Mode |
|---|---|
| Weekly / monthly cadence, or `/surface` as part of a maintenance chain | `/surface` (default — section-targeted, ~50-80K words read) |
| Once-off quarterly/annual deep review; exploring cross-section patterns | `/surface all` (~220K words read — legacy pre-2026-04-21 behavior) |
| Focused on a single ticker | `/surface TICKER` |
| Focused on a single sector | `/surface [sector]` |

Default mode delivers ~95% of `all`'s insight signal at ~25% of the read cost. Reach for `/surface all` only when you suspect section-targeting is missing a cross-section pattern.

#### `/stress-test`
```
/stress-test NVDA
```
- **Creates**: Research note, `_stress-test-manifest`.
- **Modifies**: Thesis Log + Related Research, `_hot.md`.
- Acts as a short seller. Flags for conviction reassessment but does NOT change conviction — that requires `/status`.
- **Follow-up**: `/status` (if needed) → `/sync` → `/graph last`.

#### `/scenario`
```
/scenario Fed cuts 150bps by year-end
/scenario China invades Taiwan
/scenario oil spikes to $150
/scenario AI capex disappoints by 40%
/scenario reverse [[Research/2026-04-19 - Scenario - Fed cut]]    # propagate an existing scenario note
```
- **Creates**: Research note (forward mode only), `_scenario-manifest`.
- **Modifies**: Thesis Logs for Major-impact positions, `_hot.md`.
- **Follow-up**: `/status` (affected) → `/sync` → `/graph last`.

#### `/compare`
```
/compare BESI vs AMAT                      # two
/compare PANW NET CRWD                     # 3+
```
- **Creates**: Research note (comparison), `_compare-manifest`, sector snapshot if sector note edited.
- **Modifies**: Thesis Logs, sector note(s), `_hot.md`.
- At least one ticker must have a thesis note. Missing tickers use web research (lighter; no vault updates for them).
- **Follow-up**: `/sync` → `/graph last`.

#### `/catalyst`
```
/catalyst
```
- **Creates**: `_catalyst.md` (overwrites), pre-catalyst snapshot.
- **Modifies**: `_hot.md`.
- Enriches with web-searched earnings dates. Flags catalyst clusters and gaps.
- **Follow-up**: `/deepen TICKER Catalysts` for any gap thesis.

#### `/retro`
```
/retro                                     # default: 1w window
/retro 1w                                  # weekly
/retro 1m                                  # monthly
/retro 1q                                  # quarterly
```
- **Creates**: Research note (immutable — new file per run; counter suffix on same-window same-day collisions).
- **Modifies**: Thesis Logs (Top 3 trade ideas only, `Retro insight:` prefix), `_hot.md` (Active Research Thread + Open Questions).
- **Runs in subagent** (`context: fork`): ~60 file reads + up to ~126 WebSearches (price + news + earnings per ticker) + up to 5 earnings-transcript fetches stay off main context.
- Three-dimensional classification: vault direction × news polarity × price move. Ranks by **narrative-price gap magnitude** (inverted deltas weighted 1.5×). Never auto-mutates conviction or status — Tier 3 Confirmation-Required.
- Complementary to `/surface`: retro is backward (review), surface is forward (new ideas). Run both at monthly/quarterly cadence.
- **Follow-up**: act on Top 3-5 trade ideas per [[#3.6 Retrospective review|§3.6]] → `/sync` → `/graph last`.

### Building

#### `/thesis`
```
/thesis NVDA
```
- **Creates**: Thesis note (draft, 13 sections), `_thesis-manifest`.
- **Modifies**: Sector note (only if promoted to active in same flow), `_hot.md`.
- Searches vault first (existing research, sector, macro), then web.
- Archive-collision detection: if an archived thesis exists for TICKER, pauses with a 4-option menu. See [[#Archive-collision prompt|§13 — Archive-collision prompt]].
- **Follow-up**: `/status draft→active` → `/stress-test` → `/sync` → `/graph last`.

#### `/deepen`
```
/deepen NVDA                               # auto-detects weakest section
/deepen NVDA Summary
/deepen NVDA Key Non-consensus Insights
/deepen NVDA Outstanding Questions
/deepen NVDA Business Model
/deepen NVDA Industry Context
/deepen NVDA Key Metrics
/deepen NVDA Bull Case
/deepen NVDA Bear Case
/deepen NVDA Catalysts
/deepen NVDA Risks
/deepen NVDA Conviction Triggers
```
- **Creates**: Pre-deepen snapshot, optional supporting Research note.
- **Modifies**: Thesis (target section + Log), `_hot.md`.
- Surgical — NOT a full rewrite. Enhances one section at a time.
- **Follow-up**: `/sync TICKER` → `/graph last`.

#### `/brief`
```
/brief NVDA
```
- **Creates**: Research note (1-page brief).
- **Modifies**: `_hot.md` only (no thesis edit — fully derivative).
- Read-only on the thesis. Warns if a previous brief exists.
- **Follow-up**: `/graph last` (optional — brief is derivative).

### Maintenance

#### `/lint`
```
/lint                                      # full vault
/lint NVDA                                 # scoped to one thesis
```
- **Creates**: none (read-only report).
- Full: structural (orphaned notes, broken links, missing frontmatter), freshness, connection, analytical (conviction-evidence mismatch, template drift), snapshot hygiene, graph health.
- Scoped: frontmatter, sections, staleness, conviction-evidence, template compliance, graph entry validity. Faster.
- **Follow-up**: Fix flagged issues; `/graph` if graph health issues.

#### `/prune`
```
/prune                                     # all theses
/prune semiconductors                      # sector filter
/prune stale                               # flag: last log >60 days
/prune low                                 # flag: conviction low
/prune draft                               # flag: status draft
/prune monitoring                          # flag: status monitoring
/prune semiconductors stale                # combined
```
- **Creates**: Per-closure / per-upgrade snapshots, `_prune-manifest`.
- **Modifies**: Theses (closures/upgrades), sector notes, `_hot.md`; appends `.graph_invalidations`, `.archive_ticker_registry.md` on closures.
- Checks for unsynced research first (warns if `/sync` needed). Waits for approval before executing. Approved changes applied in-line — do NOT run `/status` afterward.
- **Follow-up**: `/graph last`; `/surface` to reallocate attention.

#### `/graph`
```
/graph                                     # full rebuild (from scratch)
/graph last                                # incremental: changed theses + .graph_invalidations
/graph 3                                   # catch-up: from N days ago
```
- **Creates**/**Modifies**: `_graph.md`; clears `.graph_invalidations` and `.sync_all_fresh` on success.
- No content files modified, no snapshots.
- `/graph last` is the default post-chain reconciliation. `/graph` (full) after `/rename` or any manual thesis `mv`.

#### `/clean`
```
/clean                                     # default age 180 days; orphans PROTECTED
/clean 90                                  # custom age
/clean 30                                  # aggressive
/clean orphans                             # delete only orphans (source missing)
/clean 180 --include-orphans               # age cleanup + orphan deletion
```
- Deletes old snapshots from `_Archive/Snapshots/`.
- **Safety nets**:
  - **Orphan protection by default**: snapshots whose source file is missing are kept unless explicitly opted in.
  - **Closure-snapshot 30-day floor** (universal across all modes): pre-closure snapshots from `/prune` Stage 1 or `/status active→closed` are PROTECTED for 30 days from the manifest's `completed_date:`, regardless of `/clean` arguments. The only override is to wait or `rm` manually.
  - **Modified-source net**: snapshots whose source was modified after the snapshot was taken are protected even if old.
  - **Prune-manifest retention**: completed manifests kept 30 days for regret-recovery.

#### `/archive-callouts`
```
/archive-callouts                          # vault-wide dry-run preview, 180d default
/archive-callouts 180                      # execute vault-wide sweep
/archive-callouts NVDA                     # scoped dry-run preview (NVDA only)
/archive-callouts NVDA 90                  # scoped execute, 90d threshold
/archive-callouts 180 dry-run              # explicit dry-run with threshold
```
- Sweeps addressed callouts older than threshold (default 180d from `→ Addressed` date) into target's `## Legacy Callouts` section.
- **Creates**: Per-file `(pre-callout-sweep ...)` snapshot; `## Legacy Callouts` section (if absent); shared batch ID `callout-sweep-YYYY-MM-DD-HHMMSS`.
- **Modifies**: Target file body (callout blocks removed from source sections, plain bullets added to `## Legacy Callouts` sorted descending), frontmatter `last_callout_sweep:`, `## Log` entry prefixed `Callout sweep:`.
- **Excludes**: Fresh callouts (never eligible), `[[pinned]]` markers, `[[preserve]]` markers. Research/ notes skipped entirely (Tier 2 immutable).
- **No side effects**: zero sector propagation, zero macro propagation, zero `_hot.md` update, zero `_graph.md` update. Sweep is thesis-local hygiene.
- **Undo**: `/rollback [TICKER]` → select `(pre-callout-sweep ...)` snapshot. Vault-wide run: `/rollback callout-sweep-YYYY-MM-DD-HHMMSS` → cascade (a).
- **Dry-run default**: empty arguments or missing threshold default to preview — never silent execute.
- **No automation**: manual-only invocation. Weekly/monthly schedules must be set up via `/schedule` externally if desired.

#### `/rollback`
```
/rollback                                  # list all snapshots
/rollback NVDA                             # list snapshots for NVDA
/rollback NVDA - Nvidia (pre-sync 2026-04-16-2115)    # restore specific snapshot
```
- **Creates**: Pre-rollback safety snapshot.
- **Modifies**: Restored note, sector note (if touched), `_hot.md`; clears matching `.graph_invalidations` entries on status-revert.
- Cascade detection: multi-file sync operations offered for atomic restore. Shows diff before confirming.
- **Follow-up**: `/sync TICKER` or `/sync all` (cascade); `/graph` (full) if closure recreated.

#### `/rename`
```
/rename META "Meta Platforms"              # rename Theses/META - Meta.md
/rename SQ "Block"                         # post-rebrand
/rename SHOP "Shopify Inc"                 # add corporate suffix
```
- **Creates**: Pre-rename snapshot; `.rename_incomplete.TICKER` marker on partial failure.
- **Modifies**: Filename (atomic `mv`), all inbound wikilinks (7 patterns), `_graph.md` adjacency header, sector note Active Theses entry, `_Archive/Snapshots/` `snapshot_of:` fields, `_hot.md` mentions.
- TICKER does NOT change — only the name segment after ` - `. To undo: `/rename TICKER "[OldName]"` (symmetric).
- **Partial-failure repair**: if any wikilink Edit fails, a `.rename_incomplete.TICKER` marker is written; every ticker-scoped skill on TICKER hard-blocks until cleared. Re-run `/rename TICKER "[same new name]"` to retry failed Edits.
- **Follow-up**: `/graph` (full — not `last`). See [[#`/graph last` vs `/graph` after `/rename`|§13 — `/graph last` vs `/graph` after rename]].

---

## 6. Anatomy of Vault Content

Understanding the canonical structure helps you read, write, and prompt against vault notes without breaking conventions.

### Thesis note (13 sections)
Stored in `/Theses`. File name: `TICKER - Company Name.md`.

1. Summary — one-paragraph investment case
2. Key Non-consensus Insights — 3–5 paragraphs on what the market is missing
3. Outstanding Questions — 3–10 questions a skeptical IC would ask
4. Business Model & Product Description — deep business model breakdown
5. Industry Context — competitive dynamics, market share, value chain
6. Key Metrics — table (Market Cap, EV/Revenue, Revenue Growth, Gross Margin, FCF Yield)
7. Bull Case
8. Bear Case
9. Catalysts
10. Risks
11. Conviction Triggers — falsifiable `→ HIGH if` / `→ LOW if` / `→ CLOSE if`
12. Related Research — wikilinks to supporting notes
13. Log — dated entries, max 2 lines each

Frontmatter: `date`, `tags`, `status` (draft|active|monitoring|closed), `conviction` (high|medium|low), `sector`, `ticker`, `source`.

### Research note (4 sections)
Stored in `/Research`. File name: `YYYY-MM-DD - [Topic or Ticker] - [Source Type].md`.

1. **Thesis Delta** — 1–2 sentences: what this changes for the investment case. If no thesis exists, the key question raised.
2. **Evidence** — data points only. Tables preferred. No narrative.
3. **Contradiction Check** — does this support or challenge existing conviction? Be specific about which assumption.
4. **Source Excerpts** — only quotes with specific numbers or claims not captured above. Delete if empty.

Frontmatter: `date`, `tags`, `status`, `sector`, `ticker`, `source`, `source_type` (earnings|analyst-report|news|deep-dive|data|web-clip|stress-test|synthesis|brief|comparison|scenario|video-transcript).

A well-written Research note is dense and decision-oriented. It is NOT a summary of a source — it is a thesis-centric interpretation of what the source means.

### Sector note (10 sections)
Stored in `/Sectors`. Acts as a Map of Content for a sector.

1. Key industry questions
2. Industry history
3. Competitive dynamics
4. Product level analysis
5. Acquisitions and new entrants
6. Macro shifts
7. Investor heuristics — what's priced in vs where consensus could be wrong
8. Active Theses — links to active thesis notes in this sector
9. Related Research
10. Log

### Macro note
Stored in `/Macro`. Freeform by design — covers geopolitical scenarios, commodity frameworks, rates, FX. Strategies for macro shock and trends go here; sector-specific industry dynamics belong in sector notes.

### Inline callouts — user feedback markers

Visual markers for feedback on LLM-generated content. Drop a callout inside any section of a thesis, sector, or macro note; Claude addresses fresh callouts on demand. Opt-in — zero template changes, co-located with the edit they comment on.

#### The 4 types

| Callout | Hotkey | Color | Use when |
|---|---|---|---|
| `> [!question]` | `Mod+Alt+1` | Yellow ❓ | Ask a question |
| `> [!error]` | `Mod+Alt+2` | Red ⚡ | Flag disagreement |
| `> [!tip]` | `Mod+Alt+3` | Teal 🔥 | Suggest a change |
| `> [!todo]` | `Mod+Alt+4` | Blue ☑ | Specify an action |

`Mod` = ⌘ on macOS, Ctrl on Windows/Linux. Templates at `Templates/_callouts/user-*.md`. Filename `user-warning.md` inserts `[!error]` — filename is the Templater slot label (stable across color iterations).

#### Lifecycle

| State | Syntax | Meaning |
|---|---|---|
| **Fresh** | `> [!question] 2026-04-21` | Unresolved |
| **Addressed** | `... → Addressed 2026-04-22` + `**Prompt:** *...*` line (bold label, italic body) + `**Response:**` block | Claude handled it |
| **Pinned** | `... 2026-04-21 [[pinned]]` | Never address (contingent on external event) |
| **Preserved** | `... → Addressed ... [[preserve]]` | Addressed, exempt from `/archive-callouts` sweep |
| **Legacy** | plain bullet inside `## Legacy Callouts` | Swept by `/archive-callouts`; read-only archive |

**Pin / preserve / unpin** are manual text edits — no hotkey, no skill. Add or remove `[[pinned]]` (fresh callouts) or `[[preserve]]` (addressed callouts) in the header. Don't create `pinned.md` or `preserve.md` — the wikilinks are intentionally unresolved markers; Obsidian renders them with lighter style, `/graph` and `/lint` skip them.

**Re-opening an addressed callout**: delete the `→ Addressed YYYY-MM-DD` token, the `**Prompt:** *...*` line, and the `**Response:**` block.

#### Addressed-callout format contract

Every addressed callout — thesis, sector, or macro — follows this layout:

```markdown
> [!type] YYYY-MM-DD → Addressed YYYY-MM-DD
> **Prompt:** *<verbatim original user prompt, body italicised>*
>
> **Response:** <1-3 sentence conclusion>. <Pointer to body location: §Section → Subsection>.
```

- `**Prompt:**` and `**Response:**` labels are both bold — matched pair, visually aligned when scanning a note.
- The user's original prompt body is wrapped in `*...*` italic markers; the response body is plain prose. The label is identical; the body styling is what tells you which is user input vs. Claude output.
- Preserve the user's original wording verbatim — no paraphrasing, no typo correction.
- One blank `>`-prefixed line between the Prompt line and the Response block.
- Multi-line user prompts collapse into a single italicised body (Obsidian renders italics across wrapped lines cleanly; across paragraph breaks inconsistently).
- Retroactive only when re-touching — don't sweep old addressed callouts purely to apply the format.

#### Callout-is-ledger / body-is-deliverable rule

Callouts are an audit trail of the user-Claude exchange, not appendix storage for analysis. Evergreen insights belong in the note's spine.

| Situation | Where the analysis goes | What the Response block contains |
|---|---|---|
| Analytical question with a multi-paragraph answer | Existing body section (prefer) or new subsection (only if orthogonal) | 1-3 sentence conclusion + `§Section → Subsection` pointer |
| Concrete edit request ("put this in a table", "fix typo", "rename heading") | The edit IS the integration | Description of the edit in situ |
| Analysis has no natural body home and creating one is out-of-scope | Full analysis stays in the callout | Full content, plus flag in Log entry: `Addressed user callouts: ... — response retained in callout, no natural body home` |

**Why the rule:** `/archive-callouts` sweeps addressed callouts to `## Legacy Callouts` after 180 days. Content living only in callouts is invisible to `/brief`, `/deepen`, `/graph`, `/sync`, and to any reader scanning the note's spine. Placing the full analysis in a body section makes it immediately propagatable and scannable; the callout becomes a compact pointer to the evergreen content it seeded.

**Length smell-test:** a Response block with a table, multi-paragraph reasoning, or >3 sentences is a signal the integration did not happen. Tighten the Response and move the substance to a body section.

#### Workflow

```
1. Drop callouts inline (hotkey Mod+Alt+1..4)
2. Ask Claude to address fresh callouts
3. Claude edits sections, marks callouts addressed, writes Log entry
4. /sync TICKER | /sync | /sync all
5. /graph last
```

Before/after on one callout:

```markdown
> [!question] 2026-04-21                      > [!question] 2026-04-21 → Addressed 2026-04-22
> Pricing-power argument is thin.             > **Prompt:** *Pricing-power argument is thin.*
                                              >
                                              > **Response:** Integrated Q4 Stagwell economics
                                              > (+46% ROAS) into Bull Case bullet #1. See Log.
```

#### Chat prompt template

Copy-paste, swap the target:

> Read [[Theses/TICKER - Company Name]] and address every fresh `[!question]`, `[!error]`, `[!tip]`, and `[!todo]` callout. For each: (1) place the full analysis in the most natural body section (existing or new subsection if genuinely orthogonal); (2) rewrite the callout header to `→ Addressed YYYY-MM-DD`; (3) insert `> **Prompt:** *<verbatim original user prompt>*` (bold label, italic body); (4) write a brief `**Response:**` block — 1-3 sentences of conclusion + pointer to body location (`§Section → Subsection`). Editorial-only callouts (formatting, typos, renames) skip the body integration — the edit IS the integration. Append ONE Log entry prefixed exactly `Addressed user callouts:` summarizing all edits. Do NOT use skill-origin prefixes like `Deepened:`, `Status change:`, or `Stress test:`.

Multi-note variant: replace the wikilink with *"every thesis I've touched since [date]"* or *"every thesis in [[Sectors/X]]"*.

#### Propagation contract

`/sync` classifies Log entries by prefix. Callout-addressing MUST use a non-skill-origin prefix:

| Prefix | Propagation |
|---|---|
| `Addressed user callouts:` (recommended), `Manual edit:`, `Reviewed:`, `Refined:` | ✅ sector/macro propagate |
| `Deepened:`, `Status change:`, `Conviction reaffirmed`, `Stress test:` | ❌ silently skipped |

**Silent failure**: skill-origin prefix → thesis updates but sector/macro stay stale; no error surfaced. Detect by scanning `/sync` output for `Skill-origin classified theses:`. Fix by appending a `Manual edit: reinforcing callout addressing` Log entry and re-running `/sync TICKER`. Prevention: don't strip the prefix clause from the chat template above.

#### When to use /deepen instead

Callout-addressing has **no pre-edit snapshot**. If you regret the rewrite, only `git checkout HEAD~1 -- Theses/TICKER.md` recovers.

| Situation | Use |
|---|---|
| Rewrite >3 paragraphs | `/deepen TICKER [section]` (snapshot + manifest) |
| Single bullet / sentence / data point | Callout → address → `/sync TICKER` |
| "Claude, pick what to fix" | `/deepen` (auto-detects weakness) |
| "Add X, Y, Z" (concrete asks) | `[!todo]` callout |

Override for safety: prefix with *"Before addressing, copy [[Theses/TICKER]] to `_Archive/Snapshots/TICKER (pre-callouts YYYY-MM-DD-HHMMSS).md` with `snapshot_trigger: callouts`, then address."*

#### Sweeping addressed callouts into Legacy Callouts

Addressed callouts accumulate. `/archive-callouts` consolidates old ones into a `## Legacy Callouts` section (above `## Log`) as compact plain-text bullets. Usage in [[#`/archive-callouts`|§5 /archive-callouts]].

Swept entry format:

```markdown
## Legacy Callouts

- **2026-01-15** · warning · Bull Case · raised 2025-06-14 → Moat claim disputed — need Q4 evidence.
  - **Response:** Integrated Q4 Stagwell economics into Bull Case bullet #1. See Log 2026-01-15.
```

Entries sorted descending by addressed date. `[!error]` → `warning` (matches template filename). Full body + Response preserved verbatim.

Sweep writes a Log entry prefixed `Callout sweep:` — classified as skill-origin (no sector/macro propagation) and drift-excluded. Pure body hygiene, zero analytical content.

**Undo**: `/rollback TICKER` → pick `(pre-callout-sweep ...)` snapshot. For vault-wide: `/rollback callout-sweep-YYYY-MM-DD-HHMMSS` cascades all swept files.

**When NOT to sweep**: if you're about to quote a >180d-old Response in a `/deepen` run, either `[[preserve]]` it first or sweep after `/deepen`. Swept entries are still readable in Legacy Callouts — this only matters for heavy quoting workflows.

#### Conviction drift integration

Callouts are a bottom-up conviction channel. `/sync` Step 3e drift detection counts callout-driven Log entries toward the drift window:

- Week 1: 2 `[!error]` on Bull Case addressed → *"Addressed user callouts: weakened moat claim"*
- Week 2: 2 `[!error]` on Catalysts addressed → *"Addressed user callouts: catalyst delayed"*
- Next `/sync`: ⚠️ **Conviction drift — 4/5 recent updates flagged headwinds**

Natural next step: `/status TICKER conviction high→medium [callout-driven]`. Parallels the `/stress-test` → `/status` top-down path.

#### Skill combos

| Skill | Pattern |
|---|---|
| `/ingest`, `/stress-test`, `/compare`, `/scenario`, `/surface` | Drop callouts on affected thesis after propagation; addressing = post-skill quality gate |
| `/status` | Pattern of `[!error]` addressing + drift flag → natural conviction-change trigger |
| `/brief`, `/catalyst` | **Don't callout these** — ephemeral output; callout the source thesis |
| `/archive-callouts` | Periodic hygiene; dry-run first (`/archive-callouts`) then execute (`/archive-callouts 180`) |
| `/rollback` | No callout snapshot (use `/deepen` for regret-safety). Sweep DOES snapshot. |
| `/deepen "Legacy Callouts"` | Refused — auto-managed archive |
| `/graph last` | Always run after callout `/sync`; NOT needed after `/archive-callouts` |

#### Anti-patterns

| Pattern | Fix |
|---|---|
| Drop callouts, never address | Weekly clearance, or `[[pinned]]` intentional deferrals |
| Address, never `/sync` | Always `/sync TICKER` after addressing |
| `[!todo]` for whole-section rewrite | `/deepen TICKER [section]` instead |
| `[!error]` on every other bullet | Thesis broken — `/stress-test` → reconsider conviction |
| Callout in `_catalyst.md`, `/brief`, Research notes | Callout the thesis they relate to |
| Callout in archived thesis | `/rollback` first to reopen |
| Callout-addressing + `/status` in same chat | Address → `/sync` → then `/status` |
| Hand-edit `## Legacy Callouts` | `/rollback` to pre-sweep, use `[[preserve]]` instead |
| Run `/archive-callouts` during active callout session | Let 24h pass after addressing before sweeping |
| Skip dry-run on `/archive-callouts 180` | Always preview first (no-threshold = dry-run default) |

#### Setup (one-time per vault clone)

Only required on the FIRST machine — later clones inherit via git.

1. Templater → **Template folder location** → `Templates`; enable **Automatic jump to cursor**
2. Templater → **Template Hotkeys** → add all 4 files in `Templates/_callouts/`
3. Hotkeys → search `Templater: _callouts/user-<type>` → bind `Mod+Alt+1..4`

Commit `.obsidian/hotkeys.json` and `.obsidian/plugins/templater-obsidian/data.json` (both git-tracked). Obsidian auto-maps `Mod` to ⌘ on macOS, Ctrl on Windows/Linux.

---

## 7. Research & Thesis Building

Skill reference: [[#5. Skill Reference|§5]] (`/thesis`, `/deepen`, `/compare`, `/brief`).

### Earnings analysis
Automated:
```
/ingest [transcript URL]
/sync TICKER
```
Manual (when you want more control):
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
the physics level" or "the economics of LNG spot vs contract pricing"].
Write a comprehensive explainer using my vault content as starting
context, supplement with your knowledge, and save as a research note.
Link to every relevant thesis. Write for an investment analyst — focus
on why it matters for pricing power and competitive moats.
```

### Source-type recipes

#### YouTube transcripts (via Gemini)
YouTube URLs can't be `/ingest`ed directly. Use Gemini first.

1. Open Gemini, paste the YouTube URL.
2. Paste the prompt below (swap the URL).
3. Save the output as `YYYY-MM-DD - [Channel Name | Video Title] - video-transcript.md` in `_Inbox/`.
4. Run `/ingest` (batch mode — it picks up everything in `_Inbox/`), then `/sync`.

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
Drop into `_Inbox/`, run `/ingest`. For >10-page PDFs, `/ingest` auto-chunks by page ranges. Figures don't auto-extract — if a figure is load-bearing, screenshot and embed manually with `![[filename.png]]` in the resulting Research note.

#### Paywalled articles
Extract with Safari Reader or defuddle, save as `.md` in `_Inbox/`, then `/ingest` (batch or path).

---

## 8. Portfolio-Level Analysis

Skill reference: [[#5. Skill Reference|§5]] (`/surface`, `/scenario`, `/stress-test`, `/catalyst`, `/retro`).

Two modes: **structured** (turnkey skills with deterministic output) and **free-form** (manual prompts for exploratory synthesis).

### 8.1 Structured periodic review

```
/retro 1w                                  # backward — callout + market reaction review
/surface                                   # forward — new ideas, blind spots
/catalyst                                  # forward — event calendar
/retro 1m                                  # monthly backward aggregated
/retro 1q                                  # quarterly portfolio retrospective
```

`/retro` pairs naturally with `/surface` — one looks backward at what your thinking and the market did, the other looks forward at what to research next. Run both at monthly cadence for full portfolio visibility. At quarterly cadence, additionally run `/surface all` for deep cross-section pattern detection.

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

Skill reference: [[#5. Skill Reference|§5]] (`/lint`, `/prune`, `/graph`, `/clean`, `/rollback`, `/rename`).

### Renaming a thesis
When a company's name changes (e.g., Square → Block, FB → META).

```
/rename TICKER "New Name"
```

TICKER stays the same — only the name portion after ` - ` changes. The skill:
1. Renames the file atomically (`mv`).
2. Rewrites every inbound wikilink across the vault (7 patterns).
3. Updates `_graph.md`'s adjacency header surgically.
4. Updates sector note Active Theses entry.
5. Updates `_Archive/Snapshots/` `snapshot_of:` fields.
6. Updates `_hot.md` free-text mentions.
7. Creates a pre-rename snapshot for content-only rollback.

If any wikilink rewrite fails, `/rename` drops a `.rename_incomplete.TICKER` marker and **every ticker-scoped skill on TICKER hard-blocks** until it clears. Recover by re-running `/rename TICKER "[same new name]"` — no-op detection skips the completed `mv` and retries only failed Edits.

**Always run `/graph` (full) after `/rename`**, not `/graph last`. See [[#`/graph last` vs `/graph` after `/rename`|§13]] for rationale.

To undo: `/rename TICKER "[OldName]"` (symmetric inverse).

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

High-value free-form prompts that don't invoke skills. Copy, paste, adapt. Use these to supplement the skill surface — many of the best research moves are conversational, not procedural.

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
```
Read _hot.md. Summarise what I was working on, what's unresolved, and
suggest what to focus on today.
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
Non-consensus Insights" section is still non-consensus in April 2026.
Which have been absorbed into the market narrative?
```
```
Scan my vault for internal contradictions — places where one note's
bull case depends on an assumption that another note's bear case
challenges. List each contradiction with links to both notes.
```
```
Read the [SECTOR] notes and all linked thesis notes. For each company,
assess what the current conviction level implies about market
expectations vs. my non-consensus view. Flag any thesis where
conviction has drifted from the evidence.
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
Given my 20+ active theses, force a 5-bucket ranking based on
conviction × catalyst horizon × liquidity × macro correlation. No
optimisation — just surface the order I'd have to defend.
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
<selected text from a research source>
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
```
Read my [SECTOR]-related theses. Map the supply chain as a canvas —
who supplies whom, who competes with whom, where the bottlenecks are.
```

---

## 12. Cadence Guide

Cadence builds on top of the two loops (§1). Each tier layers backward review (`/retro`) with forward discovery (`/surface`, `/catalyst`) and health checks (`/lint`).

### Weekly (Friday evening, or after heavy research)
- `/retro 1w` — what you resolved, what the market priced, trade ideas from the gap
- `/surface` or `/surface [sector]` on whatever you've been focused on
- `/catalyst` to refresh the forward calendar
- `/lint TICKER` for any thesis you actively edited

### Monthly (first trading day of month)
- `/retro 1m` — aggregated monthly retrospective (one-liner per callout; links to full exchanges)
- Run [[#Monthly maintenance|§3.4 Monthly maintenance]]
- Review `_hot.md` conviction changes and drift flags
- Run the "Conviction recalibration" prompt from [[#Conviction recalibration (manual)|§9]]

### Quarterly (first trading day of quarter)
- `/retro 1q` — portfolio-wide quarterly retrospective (aggregated by ticker; Top-2 insights per)
- `/surface all` — once-off deep portfolio review with cross-section pattern detection
- `/prune` — evaluate weak or drifting theses for upgrade/monitoring/closure
- `/archive-callouts 180` — sweep ≥180-day addressed callouts into `## Legacy Callouts`

### Event-triggered

| Event | Workflow |
|-------|---------|
| Earnings reported | [[#Earnings reaction|§3.2 Earnings reaction]] |
| Macro shock | [[#Macro shock|§3.2 Macro shock]] |
| New stock idea | [[#New position — full build|§3.1 New position — full build]] |
| Conviction flagged by `/sync` | [[#Conviction drift response|§3.2 Conviction drift response]] |
| Competitor news | `/ingest [URL]` → `/compare` affected tickers → `/sync` |
| Sector rotation | `/surface [sector]` → `/scenario` if macro-driven → `/compare` key players |
| `/retro` surfaces inverted-bear on a position | `/stress-test TICKER` → `/status` if warranted → `/sync` |
| `/retro` surfaces flow-bull on uncovered ticker | `/ingest [news URL]` → `/thesis TICKER` |

### When conventions change
- Update `CLAUDE.md` if you add new folders, change conventions, or shift research focus.

---

## 13. Caveats & Gotchas

Known edge cases, organised by where they bite.

### `.last_sync` deletion
If `.last_sync` is deleted (manually, via `git restore`, or accidentally), the next `/sync` treats the vault as first-run: creates an epoch placeholder, then `find -newer` matches every file. Effect: a `/sync` expected to finish in ~30 seconds takes 5–10× longer. `/prune` Phase 0 detects this state and prompts before running.

To check: `ls -la .last_sync`. To recover without re-reading the full vault, `touch .last_sync` sets it to "now" — but this silently marks all currently-pending files as "synced," which is usually wrong. Preferred: let the next `/sync` re-process correctly.

### First-run `/sync` on populated vaults
On a vault that already has thesis/research/sector notes, the first `/sync` (any mode) reads everything. This is equivalent to `/sync all` in scope — expected, not a bug. Establishes the watermark baseline.

### Draft→active has no snapshot
`/status TICKER status draft→active` creates no pre-status snapshot and skips the Tier 3 confirm prompt (additive transition, no analytical content change). To reverse a mistaken promotion: manually flip frontmatter back to `draft` and trim the `Status change: draft → active` Log entry. There is no `(pre-status)` snapshot to `/rollback` to.

### Archive-collision prompt
When you run `/thesis TICKER` and a prior thesis for TICKER exists in `_Archive/` (detected via filename, frontmatter ticker, archive registry, or snapshot trail), `/thesis` pauses with four options:

| Option | When to pick |
|---|---|
| **a.** Exit to `/rollback` | Archived research is still relevant; you want continuity |
| **b.** Proceed, note predecessor in Log | Old thesis is outdated but its existence should be auditable |
| **c.** Proceed without note | Starting fresh, no audit trail needed |
| **d.** Cancel | Reconsidering |

### Propagated-research caveat after rollback
`/rollback` restores thesis/sector/macro **files** from snapshots, but does NOT rewrite `propagated_to:` frontmatter on Research notes that were consumed during the reverted `/sync`. If the originating Research note is still in `Research/` with `propagated_to: [TICKER]`, the next `/sync` sees the dedup flag and skips re-propagation — silently leaving the thesis in the restored (pre-propagation) state.

To force re-propagation post-rollback, either:
- (a) remove the ticker from that note's `propagated_to:` list manually, or
- (b) delete the source Research note and re-`/ingest`.

### `/graph last` vs `/graph` after `/rename`
`/rename` surgically rewrites the adjacency entry header for the renamed thesis but doesn't re-validate headers for unchanged neighbor theses. If a manual `mv` ever happened on another thesis (bypassing `/rename`), `/graph last` carries the stale baseline forward. `/graph` (full) re-derives every header from current filenames and eliminates this drift class.

Cost: 30–60 seconds vs ~5 seconds for `/graph last`. Skip only if you're 100% certain no thesis file has been manually renamed since the last `/graph` run.

### Draft theses invisible to sector scope
Draft theses are intentionally omitted from sector notes' Active Theses sections (CLAUDE.md convention). `/surface [sector]`, `/prune [sector]`, and other sector-scoped skills resolve scope via that list — they silently skip any thesis still in `draft`. When building multiple theses in a new sector, promote each to `active` before running sector-scoped skills or `/graph` (see [[#Sector deep-dive|§3.1 Sector deep-dive]]).

### Concurrency (single-session rule)
The vault lock model permits two ticker-scoped skills on different tickers to run in parallel. Both will Edit `_hot.md` without coordination — the later writer's section edit silently wins. **Treat Claudian as single-session**: do not run multiple Claude Code sessions against the same vault concurrently. Sequential invocations in one session are safe.

### `/ingest` same-source hard-block
`/ingest` hard-blocks a URL already ingested today (identical `source:` frontmatter). Older same-source ingests surface a three-option prompt (append as update / supersede old note / cancel). If you hit a hard-block and the prior note is a stub or wrong, delete it from `Research/` first, then re-run.

### `/brief` and `/surface` don't fully refresh the graph
Both create Research notes but don't advance thesis mtimes or write `.graph_invalidations`. New notes appear in `/graph`'s Orphan Research list only on the next full `/graph` rebuild — `/graph last` won't pick them up until a thesis Edit wikilinks to one. For a brief- or surface-heavy chain, run `/graph` (full) if you need the orphan list updated immediately.

### Dated infrastructure changes
Time-boxed rollouts (2026-04-21 Sonnet downgrade, `/surface` section-targeting, `/status` fast-path, parallel-batch refactor; 2026-04-22 WebSearch batching) live in [[_Archive/Docs/Changelog.md]]. This section holds only evergreen caveats.

### Pending graph work persists across sessions
If a chain ends without running `/graph`, `.graph_invalidations` persists across sessions until the next `/graph last` or `/graph` consumes it. `/lint` flags stale invalidation files so they're not forgotten.

---

## 14. How the Vault Stays Consistent

Short reference. Deep mechanics live in [[INFRASTRUCTURE.md]].

| File | Role | Owned by | Short story |
|---|---|---|---|
| `_graph.md` | Dependency map (thesis→sector, reverse indexes, orphans) | `/graph` | Rebuilt by `/graph` (three modes). Every other skill either advances a thesis mtime or appends to `.graph_invalidations` on closure. |
| `_hot.md` | Session context cache (6 sections) | Shared (13 writers) | Soft cap 4,000 / hard cap 5,000 words. Compression rules in `_shared/hot-md-contract.md`. Never truncates — drops whole entries. |
| `_catalyst.md` | Catalyst calendar | `/catalyst` | Regenerated each run. Pre-regenerate snapshot protects against mid-run failures. |
| `.last_sync` | Sync watermark | `/sync` (default, all) | Ticker-scoped `/sync` preserves the watermark. `/graph` never touches it. |
| `.sync_all_fresh` | Full-rebuild marker | `/sync all` → `/graph` | Forces next `/graph` (any mode) into full rebuild. Cleared on successful graph write. |
| `.graph_invalidations` | Deferred neighbor-adjacency updates | `/status` (closure), `/prune` (closure) | Consumed and deleted by `/graph last`. Cleared matching entries on `/rollback` status-revert. |
| `.rename_incomplete.TICKER` | Failed-rename repair marker | `/rename` | Hard-blocks ticker-scoped skills on TICKER until cleared. Re-run `/rename` to repair. |
| `_Archive/Snapshots/` | Version control | Shared | Pre-edit snapshots from destructive skills. Cleaned by `/clean` with closure-snapshot 30-day floor protection. Houses crash-recovery manifests. |
| `.archive_ticker_registry.md` | Archive ledger | `/status` closure, `/prune` closure | Append-only. Consumed by `/thesis` for archive-collision detection. |

**Key invariants**:
- `_graph.md` is written only by `/graph` (and `/rename` for one surgical header update). Research skills signal via mtime or `.graph_invalidations`.
- `.last_sync` is written only by `/sync` default and `/sync all`. `/sync TICKER` preserves it; `/graph` never touches it.
- Every destructive skill creates a pre-edit snapshot. Recovery path: `/rollback`.
- Every skill that modifies vault state runs a pre-flight (vault lock + rename-marker check + name sanitization + section probe). Contract: `.claude/skills/_shared/preflight.md`.

### Skill execution matrix

| Skill | Model | Context |
|---|---|---|
| `/sync`, `/ingest`, `/thesis`, `/deepen`, `/stress-test`, `/compare`, `/scenario`, `/brief`, `/catalyst` | Opus 4.7 max | Main |
| `/surface` (all modes), `/retro`, `/lint`, `/prune` | Opus 4.7 max | Forked subagent |
| `/graph`, `/rename`, `/rollback`, `/status`, `/clean` | Sonnet max | Main |

Sonnet-max skills are mechanical (extraction, file-renames, frontmatter nudges, snapshot cp) — ~40-60% faster with no correctness impact observed. Watch for regressions on `/status` trigger-conflict detection and `/rollback` multi-file cascade classification. Rollout history: [[_Archive/Docs/Changelog.md]].

For operational nuance lint and skill authors depend on, read [[INFRASTRUCTURE.md]].
