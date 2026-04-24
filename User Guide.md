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

```
_Inbox/ drop  →  /ingest  →  /sync  →  work  →  /sync
```

| Step | What happens |
|------|-------------|
| Drop raw content into `_Inbox/` | Web clips, PDFs, CSVs, notes — any format, between sessions |
| `/ingest` | Transforms `_Inbox/` into structured Research notes with wikilinks |
| `/sync` | Propagates new insights to affected theses, sector notes, macro notes, `_hot.md` |
| Work | Research, analysis, thesis building, conviction changes |
| `/sync` | Propagate again after making changes |

Every chain that edits theses ends with `/graph last` (or `/graph` full after `/rename` or archive-recreation) to reconcile the dependency map. Read-only chains (`/brief`, `/lint`, `/rollback` list) skip it.

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

Full chain:
```
# Generate or refresh content
/ingest [URL]            # or /stress-test TICKER, /compare A vs B,
                         # /scenario [event], /surface [scope]
/sync TICKER             # or /sync for multi-thesis
/graph last

# Review — open affected thesis/sector/macro, drop callouts
⌘+Option+1   # [!question] — ask for clarification
⌘+Option+2   # [!error]    — flag disagreement or error
⌘+Option+3   # [!tip]      — suggest a change
⌘+Option+4   # [!todo]     — specify a research action

# Address via chat (prefix requirement mandatory — see §6 Propagation contract)
Address fresh callouts in [[Theses/TICKER]]. Prefix the Log entry
"Addressed user callouts:" — do NOT use skill-origin prefixes.

# Propagate
/sync TICKER
/graph last
```

Multi-thesis variant (after `/sync all` or `/surface all`): drop callouts across multiple theses in one session, then *"Address fresh callouts in every thesis I've touched today"* → `/sync` (default) → `/graph last`.

For large rewrites initiated by `[!todo]` callouts, consider switching to `/deepen TICKER [section]` before the rewrite (snapshot safety — see [[#When to use /deepen instead|§6 When to use /deepen instead]]).

**Periodic hygiene**: addressed callouts pile up over time. Run `/archive-callouts` (dry-run preview, vault-wide) quarterly or whenever `/lint #50` flags pending sweeps. Executing `/archive-callouts 180` consolidates callouts ≥180d old into each thesis's `## Legacy Callouts` section as compact plain-text bullets — full audit trail preserved, source sections decluttered. Full spec: [[#Sweeping addressed callouts into Legacy Callouts|§6 Sweeping addressed callouts into Legacy Callouts]].

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

**Model assignment** (updated 2026-04-21): skills run on **Opus 4.7 max effort** unless noted below. Mechanical skills (`/graph`, `/rename`, `/rollback`, `/status`, `/clean`) run on **Sonnet max effort** — ~40-60% faster on their core operations with no loss of correctness. If you ever see a regression (e.g., `/status` missing a trigger conflict, `/rollback` cascade mis-classified), flag it — the downgrade is revertible with a one-line edit per skill.

**Subagent skills** (`context: fork`): `/lint`, `/prune`, `/surface` — the skill executes in an isolated subagent context, only a concise report returns to your main conversation. This is how heavy reads stay off your context budget.

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
- Mandatory Tier 3 confirmation before applying, **except** `draft→active` which takes a fast-path (see [[#/status draft→active fast-path|§13]]). `draft→active` has no pre-status snapshot either.

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

Visual markers for user feedback on LLM-generated content. Drop a callout inside any section of a thesis, sector note, or macro note; Claude addresses fresh callouts on demand via chat. Zero template changes to existing notes — callouts are opt-in markers the user adds after the LLM has written.

#### The 4 types

| Callout | Hotkey (macOS / Windows) | Color + icon | Use when |
|---|---|---|---|
| `> [!question]` | `⌘+Option+1` / `Ctrl+Alt+1` | Yellow ❓ | Ask a question Claude should answer |
| `> [!error]` | `⌘+Option+2` / `Ctrl+Alt+2` | Red ⚡ | Flag disagreement or critical context |
| `> [!tip]` | `⌘+Option+3` / `Ctrl+Alt+3` | Teal 🔥 | Suggest a change to the section |
| `> [!todo]` | `⌘+Option+4` / `Ctrl+Alt+4` | Blue ☑ | Specify an action (research X, add Y, fetch Z) |

Mnemonic: 1 asks, 2 flags, 3 suggests, 4 demands action. Source templates live at `Templates/_callouts/user-*.md`.

Filename note: `user-warning.md` inserts a `[!error]` callout. Filename is the Templater slot label (kept stable so hotkey bindings don't break); the callout type inside determines rendering.

#### Lifecycle

| State | Syntax | When |
|---|---|---|
| **Fresh** | `> [!question] 2026-04-21` | Just dropped, waiting for response |
| **Addressed** | `> [!question] 2026-04-21 → Addressed 2026-04-22` + `**Response:**` block | Claude handled it |
| **Pinned** | `> [!question] 2026-04-21 [[pinned]]` | Intentionally left open (never addressed) |
| **Preserved** | `> [!question] 2026-04-21 → Addressed 2026-04-22 [[preserve]]` | Addressed but exempt from `/archive-callouts` sweep — stays in-section indefinitely |
| **Legacy** | plain bullet inside `## Legacy Callouts` section, format: `- **<date>** · <type> · <section> · raised <date> → <body>` + `**Response:**` sub-bullet | Previously addressed, swept to archive by `/archive-callouts` — historical read-only |

#### Pinning and unpinning

Pinning is a manual text edit — no hotkey, no skill. Add `[[pinned]]` to the callout header to block addressing; delete it to return to fresh state.

**To pin**: add `[[pinned]]` after the date in the header:

```markdown
> [!question] 2026-04-21 [[pinned]]
> Revisit only after SEC resolution.
```

**To unpin**: delete `[[pinned]]` from the header. Callout returns to fresh state; next "address fresh callouts" request will resolve it.

**Don't create a `pinned.md` file.** The wikilink is intentionally unresolved — it's just a marker Claude looks for. Obsidian renders unresolved wikilinks with a lighter style, making pinned callouts visually distinct in reading view.

**Use cases**:
- Question contingent on an external event (SEC ruling, earnings, regulatory decision)
- Research you're deliberately deferring to next quarter
- Philosophical question without a falsifiable answer — standing reminder

**Re-opening an addressed callout**: delete the `→ Addressed YYYY-MM-DD` token from the header AND the `**Response:**` block from the body. The callout returns to fresh state. Add `[[pinned]]` if you want it parked until a specific trigger before re-addressing.

#### Preserving (exempt from auto-sweep)

`[[preserve]]` is a manual text edit parallel to `[[pinned]]`, applied to **addressed** callouts. It exempts the callout from `/archive-callouts` sweep regardless of age.

**To preserve**: add `[[preserve]]` after the `→ Addressed YYYY-MM-DD` token:

```markdown
> [!error] 2025-06-14 → Addressed 2025-06-18 [[preserve]]
> Moat claim disputed — user integrated countervailing evidence.
>
> **Response:** Rewrote Bull Case bullet #2 to acknowledge...
```

Use cases for `[[preserve]]`:
- Foundational historical exchanges worth keeping visible in their source section
- Contested-then-resolved reasoning you want readers to see without digging into Legacy Callouts
- Key pedagogical markers — "this is why we don't use sell-side consensus here"

**Don't create a `preserve.md` file.** Like `[[pinned]]`, the wikilink is intentionally unresolved — it's a marker Claude (and `/archive-callouts`) looks for. Obsidian renders it with lighter style for visual distinction. `/graph` and `/lint #3` exclude it from broken-link flags.

**To un-preserve**: delete `[[preserve]]` from the header. The callout becomes eligible for sweep on the next `/archive-callouts` run if it's also past the threshold.

#### Sweeping addressed callouts into Legacy Callouts

Addressed callouts accumulate over time. Leaving hundreds of `→ Addressed` blocks inline clutters the thesis without value once the response text has been absorbed. `/archive-callouts` consolidates old ones into a `## Legacy Callouts` section at the bottom of the note (above `## Log`).

```
/archive-callouts                  # vault-wide dry-run preview, 180d default
/archive-callouts 180              # execute vault-wide sweep, 180d threshold
/archive-callouts NVDA             # scoped dry-run preview
/archive-callouts NVDA 90          # scoped execute, 90d threshold
/archive-callouts 180 dry-run      # explicit dry-run even with threshold
```

**What gets swept**: addressed callouts where `today - addressed_date >= threshold`, excluding `[[preserve]]`-marked and `[[pinned]]`-marked entries. Fresh callouts are never eligible.

**What the section looks like**:

```markdown
## Legacy Callouts

- **2026-01-15** · warning · Bull Case · raised 2025-06-14 → Moat claim disputed — need Q4 transcript evidence.
  - **Response:** Integrated Q4 Stagwell economics (+46% ROAS) into Bull Case bullet #1. See Log 2026-01-15.
- **2025-12-18** · todo · Catalysts · raised 2025-06-20 → Add SEMICON West 2026 timing and BESI booth presence.
  - **Response:** Confirmed booth 4231, added Jul 14-16 2026 to Catalysts.
- **2025-10-03** · question · Industry Context · raised 2025-04-01 → How does hybrid bonding yield compare to TCB at 3nm?
  - **Response:** Imec data shows HB yields 4-6% better at 3nm; added to Industry Context §4.
```

Entries are sorted **descending** by addressed date — newest sweep at top. Callout formatting is stripped; the bullet format is deliberately compact. Full original body + Response are preserved verbatim.

**Type label translation**: `[!error]` → `warning` (matches the `user-warning.md` hotkey template filename — human-natural). Other types unchanged.

**Sweep writes a Log entry** prefixed `Callout sweep:`:

```
### 2026-04-24
- Callout sweep: 14 addressed callouts ≥180d swept to ## Legacy Callouts. Sections touched: Bull Case (6), Catalysts (4), Industry Context (3), Risks (1). Safety snapshot: [[_Archive/Snapshots/NVDA - Nvidia (pre-callout-sweep 2026-04-24-143055)]]
```

This prefix is classified by `/sync` Step 2.5 as skill-origin (no sector/macro propagation) and drift-excluded at Step 3e (no impact on conviction-drift detection). A sweep has zero analytical content — it is pure body hygiene.

**Undo**: `/rollback [TICKER]` → select the `(pre-callout-sweep ...)` snapshot. To undo a whole vault-wide run in one transaction, use the batch ID from the Log entry's safety-snapshot path: `/rollback callout-sweep-YYYY-MM-DD-HHMMSS` → cascade (a) restores every swept file.

**When NOT to sweep**: never sweep callouts you're actively referencing in ongoing work. If a `[!error]` was addressed 200 days ago but you're about to use the Response in a `/deepen` run, pin it first with `[[preserve]]` or run `/archive-callouts` AFTER the deepen completes. Swept entries survive in Legacy Callouts — readable but compact — so this is only a concern for heavy quoting workflows.

**Fresh → addressed example.** Before:

```markdown
> [!question] 2026-04-21
> Pricing-power argument is thin — need Q4 transcript evidence.
```

After Claude addresses it:

```markdown
> [!question] 2026-04-21 → Addressed 2026-04-22
> Pricing-power argument is thin — need Q4 transcript evidence.
> 
> **Response:** Integrated Q4 Stagwell economics (+46% ROAS, 57% go-live
> conversion) into Bull Case bullet #1. See Log 2026-04-22.
```

The callout persists — visual audit trail co-located with the edit. Delete addressed callouts or keep them; both patterns work.

#### Workflow

```
1. Drop callouts inline (hotkey ⌘/Ctrl+Alt+1..4)
2. Ask Claude to address fresh callouts
3. Claude edits sections, marks callouts addressed, writes Log entries
4. /sync TICKER  (one thesis) | /sync (multiple) | /sync all (whole vault)
5. /graph last
```

#### Chat prompt template

Copy-paste, swap the target:

> Read [[Theses/TICKER - Company Name]] and address every fresh `[!question]`, `[!error]`, `[!tip]`, and `[!todo]` callout. For each: edit the surrounding section to incorporate the feedback, rewrite the callout header to `→ Addressed YYYY-MM-DD` with a `**Response:**` block inside the callout, then append ONE Log entry prefixed exactly `Addressed user callouts:` summarizing all edits. Do NOT use skill-origin prefixes like `Deepened:`, `Status change:`, or `Stress test:`.

For multi-note scope, replace the wikilink with *"every thesis I've touched since [date]"* or *"every thesis in [[Sectors/X]]"*.

#### Propagation contract

`/sync` classifies every Log entry by its prefix and uses the classification to decide whether to propagate changes to sector and macro notes. Callout-addressing MUST use a non-skill-origin prefix.

| Prefix | Classification | Propagation |
|---|---|---|
| `Addressed user callouts:` (recommended) | non-skill-origin | ✅ |
| `Manual edit:`, `Reviewed:`, `Refined:` | non-skill-origin | ✅ |
| `Deepened [Section]:` | skill-origin (`/deepen`) | ❌ silently skipped |
| `Status change:`, `Conviction reaffirmed` | skill-origin (`/status`) | ❌ silently skipped |
| `Stress test:` | skill-origin (`/stress-test`) | ❌ silently skipped |

**Silent failure mode**: if Claude uses a skill-origin prefix after callout addressing, the thesis is updated but sector/macro stay stale after `/sync` — no error, no warning.

**Detection**: after `/sync`, scan the report for `Skill-origin classified theses:`. If your callout-addressed thesis appears there, add a Log entry with `Manual edit: reinforcing callout addressing` and re-run `/sync TICKER`.

**Prevention**: the chat prompt template above bakes the prefix requirement into the prompt. Don't strip that clause.

#### When to use /deepen instead

**Callout-addressing has no pre-edit snapshot.** If Claude rewrites a section based on `[!todo]` callouts and you regret the result, `/rollback` won't help — only git history (`git checkout HEAD~1 -- Theses/TICKER.md`) can restore.

Boundary:

| Situation | Use |
|---|---|
| Rewrite >3 paragraphs in one section | `/deepen TICKER [section]` — creates pre-edit snapshot + manifest |
| Single bullet fix, sentence edit, data-point add | Callout → address → `/sync TICKER` |
| "This section is weak, Claude pick how to fix" | `/deepen` (auto-detects weakness) |
| "Specifically add X, Y, Z" with concrete asks | `[!todo]` callout |

Override: if you want snapshot safety for a large callout-driven rewrite, prefix your chat request with *"Before addressing, copy [[Theses/TICKER]] to `_Archive/Snapshots/TICKER (pre-callouts YYYY-MM-DD-HHMMSS).md`, add `snapshot_trigger: callouts` frontmatter, then address."*

#### Skill combos at a glance

| Skill | Combo pattern |
|---|---|
| `/ingest` | After ingest + sync, drop callouts to refine Claude's propagation. Callouts = post-ingest quality gate. |
| `/stress-test` | `[!error]` where stress-test overreaches. Multiple `[!error]` accumulating → escalate to a fresh `/stress-test`. |
| `/compare` | Callout the affected thesis (NOT the comparison note); Claude addresses → `/sync` propagates to sector. |
| `/scenario` | `[!error]` on scenario assumptions you dispute; Claude refines per-thesis scenario impact. |
| `/surface` | `[!todo]` on leads; Claude does targeted follow-up research. |
| `/status` | Pattern of `[!error]` addressing + drift flag → natural trigger for conviction change. |
| `/graph last` | Always run after callout-driven `/sync` — new wikilinks need reconciling. `/archive-callouts` does NOT require `/graph last` (sweep creates no new wikilinks). |
| `/brief`, `/catalyst` | **Don't callout these** — ephemeral / regenerated. Callout the source thesis. `/brief` excludes both callouts AND `## Legacy Callouts` from output. |
| `/archive-callouts` | Periodic hygiene. Dry-run first (`/archive-callouts`) to preview, then execute with explicit threshold (`/archive-callouts 180`). Per-file snapshot enables `/rollback`. Owns `## Legacy Callouts` exclusively — never hand-edit entries. |
| `/rollback` | Callout-addressing has no snapshot — use `/deepen` for rewrites you might regret. `/archive-callouts` DOES snapshot — full rollback available per file or per batch. |
| `/deepen` | `/deepen [TICKER] "Legacy Callouts"` is REFUSED — section is auto-managed archive, not deepen-eligible analytical content. |
| `/lint` | Checks #50-#53 enforce Legacy Callouts schema + flag stale fresh callouts piling up. |

#### Conviction drift integration

Callouts are a **bottom-up conviction-change channel**. `/sync` Step 3e drift detection reads Log-tail patterns; each callout-driven Log entry counts toward the drift window. Pattern:

- Week 1: 2 `[!error]` on Bull Case → addressed → Log: *"Addressed user callouts: weakened moat claim, added countervailing evidence"*
- Week 2: 2 `[!error]` on Catalysts → addressed → Log: *"Addressed user callouts: catalyst resolution delayed"*
- Next `/sync`: ⚠️ **Conviction drift — 4/5 recent updates flagged headwinds**

Natural next step: `/status TICKER conviction high→medium [callout-driven]`. Parallels the `/stress-test` → `/status` top-down path.

#### Anti-patterns

| Pattern | Why it breaks | Fix |
|---|---|---|
| Drop callouts, never address | Pile up, clutter thesis; `/lint #51` flags after 90d / 180d | Weekly callout clearance OR pin intentional deferrals |
| Address callouts, never `/sync` | Sector/macro stale; drift signal missed | Always `/sync TICKER` after addressing |
| `[!todo]` for whole-section rewrite | No snapshot, no rollback path | `/deepen TICKER [section]` instead |
| `[!error]` on every other bullet | Thesis fundamentally broken — callouts won't save it | `/stress-test` → `/deepen` → reconsider conviction |
| Callout in `_catalyst.md`, `/brief` output, Research notes | Ephemeral / source-record immutable | Callout the thesis they relate to |
| Callout in archived thesis | `/sync` skips `_Archive/` | `/rollback` first to reopen |
| Mix callout-addressing with `/status` in same chat | Log entry ordering collisions | Address → `/sync` → then `/status` |
| Hand-edit `## Legacy Callouts` entries | Breaks `/lint #52` schema; next sweep re-sorts | `/rollback` to pre-sweep snapshot and use `[[preserve]]` to exempt specific callouts instead |
| Delete `## Legacy Callouts` section without Log restoration | `/lint #53c` flags Callout-sweep Log entries referencing missing section | `/rollback` to pre-sweep snapshot, or accept the flag as harmless |
| Run `/archive-callouts` during active callout-addressing session | Race condition — fresh addressings get swept if addressed_date is backdated | Address → `/sync` → let 24h pass → then `/archive-callouts` |
| Skip dry-run, run `/archive-callouts 180` blind | Can sweep hundreds of callouts you didn't realize existed | Always preview with `/archive-callouts` (no threshold = dry-run default) before executing |

#### Setup (one-time per vault clone)

Only required on the FIRST machine — later clones inherit via git.

1. Settings → Templater → **Template folder location** → `Templates`
2. Settings → Templater → enable **Automatic jump to cursor**
3. Settings → Templater → **Template Hotkeys** → add all 4 files in `Templates/_callouts/`
4. Settings → Hotkeys → search `Templater: _callouts/user-<type>` → bind `⌘/Ctrl+Alt+1..4`

Commit `.obsidian/hotkeys.json` and `.obsidian/plugins/templater-obsidian/data.json` — both git-tracked. On another Mac after git pull, hotkeys and templates work immediately.

#### Cross-platform notes

- Hotkeys store in `.obsidian/hotkeys.json` as `Mod+Alt+<N>`. Obsidian auto-maps `Mod` to `⌘` on macOS, `Ctrl` on Windows/Linux; `Alt` maps to `Option` on macOS.
- Avoids `⌘+Shift+3/4/5` which macOS reserves for screenshots.
- Templater template registration in `.obsidian/plugins/templater-obsidian/data.json` — identical behavior across platforms.

#### Why callouts, not sections

Co-located visual provenance — you see what you wrote vs what the LLM wrote at the exact decision point. Zero template changes, zero skill changes, cross-platform via git. Section-based feedback (e.g., "Outstanding Input" at top of note) would force structure on 61 notes, duplicate `## Outstanding Questions` and `## Log`, and separate comments from the edit they relate to.

---

## 7. Research & Thesis Building

### Skill shortcuts — see §5 for canonical reference

| Action | Command | Notes |
|---|---|---|
| Build a thesis from scratch | `/thesis TICKER` | Status defaults to `draft`; promote with `/status draft→active`. See [[#Archive-collision prompt\|§13]] if ticker was previously archived. |
| Deepen a weak section | `/deepen TICKER [section]` | Omit section to auto-detect weakest. Full section list: [[#`/deepen`\|§5]]. |
| Competitive comparison | `/compare A vs B` | `/compare A vs B vs C` for 3+ tickers. |
| Generate a 1-page brief | `/brief TICKER` | Read-only on the thesis. |

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

### Skill shortcuts — see §5 for canonical reference

| Action | Command | Notes |
|---|---|---|
| Surface insights / opportunities | `/surface` | `/surface all` (comprehensive), `/surface TICKER`, `/surface [sector]`. Forks to subagent. [[#`/surface`\|§5]]. |
| Macro scenario propagation | `/scenario [event]` | `/scenario reverse [[Research/...]]` to reverse-propagate. [[#`/scenario`\|§5]]. |
| Adversarial stress test | `/stress-test TICKER` | [[#`/stress-test`\|§5]]. |
| Catalyst calendar | `/catalyst` | Regenerated each run. [[#`/catalyst`\|§5]]. |

### Manual portfolio prompts
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

### Skill shortcuts — see [[#`/status`|§5 /status]] for canonical reference

| Operation | Syntax | Notes |
|---|---|---|
| Change conviction | `/status TICKER conviction old→new [reason]` | Mandatory confirmation. Pre-change snapshot + sector note + `_hot.md` updated. Trigger conflicts checked. |
| Change status | `/status TICKER status old→new [reason]` | Transitions: `draft→active`, `active→monitoring`, `monitoring→active`, `active→closed`. `draft→active` skips snapshot + confirmation (fast-path). `active→closed` moves file to `_Archive/`. |
| Reaffirm after drift | `/status TICKER reaffirm [why drift was noise]` | Lightweight — no frontmatter change, no snapshot. Resets the drift detection window. |

### Conviction recalibration (manual)
```
Read all thesis notes with conviction: high. For each, check the most
recent log entry date. If the last update was more than 60 days ago,
flag it as stale. Summarise what has likely changed since the last
update based on the sector note and recent research.
```

---

## 10. Vault Maintenance

### Skill shortcuts — see §5 for canonical reference

| Action | Command | Notes |
|---|---|---|
| Health check | `/lint` | `/lint TICKER` for scoped. Forks to subagent. [[#`/lint`\|§5]]. |
| Portfolio pruning | `/prune` | Sector/status filter variants — [[#`/prune`\|§5]]. |
| Rebuild dependency graph | `/graph last` | Default post-chain. `/graph` (full) after `/rename` or disaster recovery. `/graph [N]` for catch-up. [[#`/graph`\|§5]]. |
| Snapshot cleanup | `/clean` | Defaults 180d with orphan protection. All modes + safety nets: [[#`/clean`\|§5]]. |
| Rollback | `/rollback TICKER` | Lists snapshots. `/rollback [exact name]` to restore. Cascade-aware for multi-file sync/prune. [[#`/rollback`\|§5]]. |

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

### Weekly (or after heavy research)
- `/surface` or `/surface [sector]` on whatever you've been focused on
- `/catalyst` to refresh the calendar
- `/lint TICKER` for any thesis you actively edited

### Monthly
Run [[#Monthly maintenance|§3.4 Monthly maintenance]]. Also:
- Review `_hot.md` conviction changes and drift flags
- Run the "Conviction recalibration" prompt from [[#Conviction recalibration (manual)|§9]]

### Event-triggered

| Event | Workflow |
|-------|---------|
| Earnings reported | [[#Earnings reaction|§3.2 Earnings reaction]] |
| Macro shock | [[#Macro shock|§3.2 Macro shock]] |
| New stock idea | [[#New position — full build|§3.1 New position — full build]] |
| Conviction flagged by `/sync` | [[#Conviction drift response|§3.2 Conviction drift response]] |
| Competitor news | `/ingest [URL]` → `/compare` affected tickers → `/sync` |
| Sector rotation | `/surface [sector]` → `/scenario` if macro-driven → `/compare` key players |

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
`/status TICKER status draft→active` does not create a pre-status snapshot (no analytical content changed). To reverse a mistaken promotion: manually flip frontmatter back to `draft` and trim the `Status change: draft → active` Log entry. There is no `(pre-status)` snapshot to `/rollback` to. Same run also takes the Step 2F fast-path (see [[#/status draft→active fast-path|§13 entry]] above) — the two exemptions share the same underlying insight: this transition is additive, not analytical.

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

### `/surface` section-targeting vs `/surface all` (2026-04-21 change)
Default `/surface` now reads only 4 sections per thesis (Summary, Non-consensus Insights, Risks, Catalysts) + last 5 Log entries — ~25% of the token cost of the pre-2026-04-21 behavior. Use `/surface all` if you explicitly want the legacy full-read behavior (e.g., once-off quarterly deep review). Both modes fork to a subagent, so main-context impact is the same either way. If a cross-section pattern (e.g., a Business Model similarity across 3 theses) seems systematically missed by default mode, switch to `/surface all` for that run.

### `/thesis` parallel probe batch (2026-04-21 change)
`/thesis` Step 0+1 duplicate-detection probes (rename-marker, active-thesis glob, 4 archive-collision signals, research-context grep) now fan out as a single parallel tool-call batch after lock acquisition instead of running sequentially. Same semantics, same 4-option archive-collision prompt, same priority-order short-circuit — just fewer round-trips. Expected ~5–8% end-to-end wall-clock improvement on `/thesis TICKER` runs with no user-visible behavior change. Full rationale: `.claude/skills/thesis/RATIONALE.md §9`.

### /status draft→active fast-path (2026-04-21 change)
`/status TICKER status draft→active` now **skips the Tier 3 `"Confirm? (y/n)"` gate** and proceeds directly after a one-line FYI message. Every other safety mechanic (manifest skeleton, sector snapshot, Log entry, manifest flip) runs identically — only the user prompt is elided. Scope is narrow: ONLY `draft→active`. All other transitions (`active→monitoring`, `active→closed`, `monitoring→active`, `closed→active`, conviction changes) still require the Tier 3 confirmation.

Why the exemption is safe for this specific transition: CLAUDE.md Tier 3's examples are all reductions (`active→monitoring`, `active→closed`); `draft→active` is additive (adds coverage, doesn't remove). No analytical content changes. No cascade implications (no sector-list removal, no graph invalidations, no `_hot.md` demotion). Easily reversible via manual frontmatter flip (the draft→active path has never had a pre-status snapshot anyway — see previous entry). Full analysis: `.claude/skills/status/RATIONALE.md §9`.

Combined with the Step 1/5b/7.9 parallelization refactor, a typical `/status TICKER draft→active` should now complete in ~30–50s (down from ~3min). To opt back into the prompt for a specific run, interrupt after the Step 2F FYI message prints.

### Parallel-batch refactor across 10 skills (2026-04-21 change)
Ten skills (`/catalyst`, `/stress-test`, `/deepen`, `/compare`, `/scenario`, `/sync all`, `/surface`, `/prune`, `/lint`, `/clean`) had their multi-file read phases converted from serial loops to parallel tool-call batches. For `/catalyst`, `/prune`, `/scenario`, full-file Reads are preserved (research-quality gated). Expected ~30–60% wall-clock speedup on monthly maintenance chain; no user-visible behavior change. Per-skill breakdown, context-impact analysis, and regression recovery: [[INFRASTRUCTURE.md]] §12.6.

### WebSearch batching extension (2026-04-22 change)
Two web-research speed wins, both mirror the `/catalyst` Phase 2 batched-WebSearch pattern:

1. **`/catalyst` WebSearch batch cap raised 10 → 25.** Same parallel pattern, larger per-batch fan-out. For ~42 tickers, Phase 2 earnings enrichment drops from ~4-5 rounds of ~5s each to ~2 rounds. Expected ~40-60% wall-clock reduction on the Phase 2 step — previously the single biggest cost in the monthly maintenance chain.

2. **`/thesis` Step 3 Web Research now explicitly batches WebSearch/WebFetch calls** (up to 25 per message, independent searches only; follow-ups with data dependency fire in subsequent batches). Step 2 vault Reads and Step 3 web searches are also now explicitly parallel — no ordering dependency. Expected ~30-50% wall-clock reduction on `/thesis TICKER` runs, which were previously dominated by serial web-research round-trips.

3. **`/stress-test` Phase 2.5 (new, optional) documents the batching pattern** for any opportunistic external-evidence lookups. Does NOT mandate web research — `/stress-test` remains vault-content-driven by default — but codifies the batching rule in case the run requires current-market context (fresh analyst downgrades, short-interest, pending litigation).

No behavior changes beyond parallelization — same prompts, same research quality, fewer serial round-trips. Regression recovery: revert to serial if a batch-too-large error surfaces (unlikely at cap=25; the tool-runtime ceiling is higher).

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

### Skill execution matrix (2026-04-21 update)

| Skill | Model | Context |
|---|---|---|
| `/sync`, `/ingest`, `/thesis`, `/deepen`, `/stress-test`, `/compare`, `/scenario`, `/brief`, `/catalyst` | Opus 4.7 max | Main |
| **`/surface`** (all modes) | Opus 4.7 max | **Forked subagent** |
| `/lint`, `/prune` | Opus 4.7 max | Forked subagent |
| **`/graph`, `/rename`, `/rollback`, `/status`** | **Sonnet max** | Main |
| `/clean` | Sonnet max | Main |

Bold rows = 2026-04-21 changes. The Sonnet-max skills are mechanical (extraction, file-renames, frontmatter nudges, snapshot cp) — no deep analytical reasoning needed, so Sonnet delivers ~40-60% faster wall time with no correctness impact observed to date. Watch for regressions on `/status` trigger-conflict detection and `/rollback` multi-file cascade classification — the first two skills to revert if Sonnet proves insufficient.

For the operational nuance lint and skill authors depend on, read [[INFRASTRUCTURE.md]].
