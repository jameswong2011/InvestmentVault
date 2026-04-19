# User Guide — Claude Code + Obsidian for Investment Research

> Your vault has **39 theses**, **132 research notes**, **13 sector notes**, and **6 macro notes**. This guide covers every skill, every argument form, every multi-skill workflow chain, and every natural language query pattern available. Ordered by impact — start at the top.

---

## 0. First Run

If this is a brand new vault (no prior `/sync` runs), run this bootstrap sequence:

```
/sync                            # creates _hot.md + .last_sync, reads all vault files
/graph last                      # creates _graph.md from vault state (falls back to full rebuild on first run)
```

After bootstrap, all skills work. Without it:
- Scoped `/surface` (ticker or sector) requires `_graph.md` — it blocks if missing
- `/prune` pre-flight unsynced-research check has no `.last_sync` baseline to compare against
- Skills that update `_hot.md` will auto-create it (CLAUDE.md rule #9), but `/sync` produces a richer initial version with Latest Sync data and Portfolio Snapshot

> `/sync TICKER` does NOT require `_graph.md` — it reconstructs adjacency directly from the thesis file. Safe to run before bootstrap.

> If the vault already has thesis/research/sector notes, `/sync` reads everything on first run (equivalent to `/sync all`). This is expected — it establishes the watermark baseline.

---

## 1. The Core Loop

Every session follows the same rhythm: **deposit → ingest → sync → graph**. Everything else extends this loop.

```
_Inbox/ drop  →  /ingest  →  /sync  →  /graph last  →  work  →  /sync  →  /graph last
```

| Step | What happens | Time |
|------|-------------|------|
| Drop raw content into `_Inbox/` | Web clips, PDFs, CSVs, notes — any format | Between sessions |
| `/ingest` | Transforms `_Inbox/` into structured Research notes with wikilinks | ~2 min |
| `/sync` | Propagates new insights to theses, sector notes, macro notes, `_hot.md`. Does NOT touch `_graph.md`. | ~3 min |
| `/graph last` | Reconciles `_graph.md` against just-modified files (true incremental — only re-extracts changed thesis adjacencies) | ~10 sec |
| Work | Research, analysis, thesis building, conviction changes | Variable |
| `/sync` → `/graph last` | Propagate session work, then refresh dependency map | ~3 min total |

> **Why `/graph last` after every `/sync`**: Research skills (`/sync`, `/thesis`, `/compare`, etc.) no longer write to `_graph.md` — that ownership is concentrated in `/graph` to eliminate cross-skill metadata contention. `/graph last` is the cheap finalizer that keeps the dependency map current.

---

## 2. Session Start

### Resume context
```
Read _hot.md. Summarise what I was working on,
what's unresolved, and suggest what to focus on today.
```

### Process inbox
```
/ingest
/sync
/graph last
```
> `/ingest` creates Research notes only. `/sync` propagates the insights to theses, sectors, macro notes (no `_graph.md` writes). `/graph last` reconciles the dependency map. Always run all three.

### Earnings season triage
```
Which of my thesis companies report earnings in the next 2 weeks?
For each, list the key metrics and outstanding questions from my thesis
note that the report should answer.
```

---

## 3. Workflow Chains

Multi-skill sequences for common scenarios. Each chain shows the optimal order — skipping steps weakens the outcome.

### 3a. New Position — Full Build

**When**: Starting coverage on a new company from scratch.

```
/thesis TICKER
```
Review the draft. When ready to promote:
```
/status TICKER status draft→active [rationale]
```
Stress-test immediately while the thesis is fresh:
```
/stress-test TICKER
```
Propagate stress test findings, then refresh the dependency map:
```
/sync TICKER
/graph last
```
> **Full chain**: `/thesis` → `/status draft→active` → `/stress-test` → `/sync TICKER` → `/graph last`
> **Optional extension**: Add `/compare TICKER vs COMPETITOR` before `/sync` for competitive context. Add `/deepen TICKER [weakest section]` to fill gaps the stress test identified.

### 3b. New Position — From Existing Research

**When**: You've been collecting research on a ticker and want to formalise a thesis.

```
/ingest                          # process any inbox items first
/sync                            # propagate to existing notes
/graph last                      # register inbox-derived research in graph
/thesis TICKER                   # vault research is used automatically
/status TICKER status draft→active [rationale]
/sync TICKER                     # propagate new thesis connections
/graph last                      # register new thesis adjacency in graph
```

### 3c. Earnings Reaction

**When**: A thesis company just reported earnings.

```
/ingest [transcript or press release URL]
/sync TICKER
/graph last
```
If the report changes conviction:
```
/status TICKER conviction old→new [what the report revealed]
```
If the report was ambiguous, stress-test first:
```
/stress-test TICKER
```
> **Full chain**: `/ingest URL` → `/sync TICKER` → `/graph last` → (assess) → `/status` or `/stress-test` → `/sync` → `/graph last`

### 3d. Conviction Drift Response

**When**: `/sync` flags `⚠️ Conviction drift` on a thesis.

**Path A — Reaffirm** (evidence reviewed, conviction unchanged):
```
/status TICKER reaffirm [rationale why the drift signal is noise]
```

**Path B — Investigate first**:
```
/stress-test TICKER
```
Review findings, then either reaffirm or change:
```
/status TICKER conviction old→new [rationale from stress test]
/sync TICKER
/graph last
```

**Path C — Investigate with targeted research**:
```
/deepen TICKER [section the drift relates to]
/sync TICKER
/graph last
```
Then decide:
```
/status TICKER conviction old→new [rationale]
```

### 3e. Macro Shock Response

**When**: A major macro event occurs (rate decision, geopolitical event, policy change).

```
/scenario [describe the event with quantitative parameters]
```
For the most exposed positions:
```
/status TICKER conviction old→new [transmission channel from scenario]
```
If the scenario reveals competitive dynamics worth exploring:
```
/compare [exposed ticker] vs [beneficiary ticker]
```
Propagate all changes, then refresh dependency map:
```
/sync
/graph last
```
> **Full chain**: `/scenario` → `/status` (most affected) → `/compare` (competitive shifts) → `/sync` → `/graph last`

### 3f. Thesis Improvement — Targeted

**When**: A thesis section is weak, stale, or flagged by `/lint`.

```
/deepen TICKER [section name]
/sync TICKER
/graph last
```
> `/deepen` auto-detects the weakest section if you omit the section name. Always follow with `/sync TICKER` to propagate, then `/graph last` to register any new research note in the dependency map.

### 3g. Thesis Improvement — Adversarial

**When**: You want to pressure-test conviction before a major decision.

```
/stress-test TICKER
/deepen TICKER [section the stress test identified as weakest]
/sync TICKER
/graph last
```
> The stress test identifies vulnerabilities. `/deepen` fills the gaps. `/sync` propagates. `/graph last` registers the new research notes in the dependency map.

### 3h. Competitive Reassessment

**When**: Competitive dynamics in a sector are shifting.

```
/compare A vs B
```
If the comparison changes conviction on either name:
```
/status TICKER conviction old→new [competitive insight]
```
Propagate, then refresh dependency map:
```
/sync
/graph last
```
> **Variant**: `/compare A vs B vs C` works for 3+ companies. At least one ticker must have a thesis note. Tickers without theses use web research (lighter analysis, no vault updates for that ticker). For full-depth comparison, run `/thesis TICKER` first.

### 3i. Portfolio Pruning Cycle

**When**: Portfolio feels crowded, attention is spread thin, or it's time for periodic cleanup.

```
/prune
```
> Warns if unsynced research exists — always `/sync` first. `/prune` presents a recommendation table, then asks for approval before executing. Approved closures and upgrades are applied directly by `/prune` — do not run `/status` afterward (the files have already been moved or updated).

Then find opportunities to reallocate attention:
```
/surface
```
> **Full chain**: `/sync` → `/graph last` → `/prune` (approve changes in-line) → `/surface` (new opportunities) → `/graph last` (register the surface scan note + reflect any closures/upgrades from /prune)

### 3j. Idea Discovery → New Position

**When**: You want to find new opportunities from existing research.

```
/surface
```
or scoped:
```
/surface semiconductors
```
If an opportunity emerges:
```
/thesis TICKER
/compare TICKER vs [existing competitor in sector]
/status TICKER status draft→active [rationale]
/sync
/graph last
```

### 3k. Sector Deep-Dive

**When**: Entering or re-evaluating an entire sector.

If sector note doesn't exist yet:
```
Create a new Sector Note for [SECTOR] using the Sector Template. Search
the vault for all relevant thesis notes, research notes, and macro
connections. The "Investor heuristics" section should explicitly state
what consensus believes and where they could be wrong.
```
Then:
```
/graph last                      # register new sector note in the reverse index
/surface [sector]
/compare [key players in sector]
/sync
/graph last
```
> `/graph last` is required before `/surface [sector]` — sector scoping uses `_graph.md`'s Sector → Theses reverse index, which won't include a newly created sector note until `/graph last` reads the new sector file (Step I.5 always rebuilds reverse indexes from current `Sectors/*.md` files). If building multiple theses in a new sector: create the sector note first, then `/thesis` for each company, then `/graph last` to refresh adjacencies, then `/surface [sector]`.

### 3l. Monthly Maintenance

**When**: Monthly or when the vault feels out of sync.

```
/sync all                        # full brute-force propagation
/graph                           # full rebuild (after /sync all the watermark is reset)
/lint                            # full health audit
/prune                           # portfolio evaluation
/clean                           # delete old snapshots
/surface                         # find new opportunities
/catalyst                        # refresh catalyst calendar
/graph last                      # incremental refresh after /surface, /catalyst, /prune touched files
```
> Run in this order. `/sync all` before `/graph` because the sync may change links. `/graph` (full rebuild, not `last`) is correct here because `/sync all` doesn't update `_graph.md` — a full rebuild establishes the fresh baseline. `/lint` after `/graph` because lint checks graph health. `/prune` after `/lint` because lint flags staleness. `/surface` near the end because the vault is now clean and complete. Final `/graph last` (incremental, cheap) captures changes from `/surface`, `/catalyst`, and `/prune`.

### 3m. Recovery — Undo a Bad Sync

**When**: `/sync` produced changes you disagree with.

```
/rollback TICKER
```
Select the `(pre-sync)` snapshot. Rollback detects cascade operations — if `/sync` touched multiple files, it offers to restore all of them atomically.

After rollback:
```
/sync TICKER                     # re-propagate from the restored state
/graph last                      # capture the restored adjacency
```

### 3n. Recovery — Undo a Closure

**When**: A thesis was closed/archived but you want to reopen it.

```
/rollback TICKER
```
The archived thesis will be recreated at its original path. The archived copy moves to Snapshots. `/rollback` restores the pre-closure snapshot — check the restored note's `status:` frontmatter before proceeding:

- **If `status: active`** (typical — snapshot was taken before closure): skip `/status`, the note is already active.
- **If `status: closed`** (rare — snapshot was taken after closure): run `/status TICKER status closed→active [rationale]`.

Then propagate:
```
/sync TICKER
/graph last
```
> **Critical for recreated-file rollbacks**: `/graph last` MUST run before any default `/sync` or scoped `/surface` for this ticker. Without it, the recreated thesis exists on disk but is invisible to graph-assisted lookups. (`/sync TICKER` works because it uses file-direct adjacency, but a default `/sync` could miss propagation paths.)

### 3o. Pre-Meeting Prep

**When**: You need to pitch or discuss a position.

```
/brief TICKER
```
For adversarial prep (anticipating pushback):
```
/stress-test TICKER
/sync TICKER
/brief TICKER
/graph last
```
> The stress test identifies the weakest points so you can prepare rebuttals — but it only writes a research note + a Log entry on the single thesis. `/sync TICKER` propagates those findings to the sector note, macro notes, and any cross-thesis references the stress test surfaced, so the brief picks up a consistent post-stress-test vault state rather than a half-updated one. The brief then distils the thesis into a 1-page memo. `/graph last` registers both the stress test and brief research notes in the dependency map.
>
> **Skip `/sync TICKER` only if**: the stress test explicitly returned "thesis survives stress testing" with no `🔴` assumption fragilities and no cross-thesis implications. In that case the propagation has nothing to carry, and `/stress-test` → `/brief` → `/graph last` is sufficient.

### 3p. Research Session — Ad Hoc Topic

**When**: Researching a topic that may affect multiple theses.

```
/ingest [URL1]
/ingest [URL2]
/ingest [URL3]
/sync
/graph last
```
Or for manual research:
```
Research [TOPIC] for [TICKER]. Focus on [specific angle]. Save to
Research/ and update the relevant thesis log.
```
Then:
```
/sync
/graph last
```

### 3q. Catalyst-Driven Review

**When**: Preparing for an upcoming catalyst window.

```
/catalyst
```
For each thesis with imminent catalysts:
```
/deepen TICKER Catalysts
```
For theses with no catalysts flagged:
```
/prune [sector] stale
```
End the chain with a graph refresh:
```
/graph last
```
> `/deepen` and `/prune` modify thesis files; `/graph last` captures these changes in the dependency map.

---

## 4. Non-Consensus Insight Generation

The highest-value prompts. These force synthesis across the vault to surface ideas the market isn't pricing. None of these map to a single skill — they require Claude to reason across the full vault.

### Cross-thesis pattern detection
```
Read all my thesis notes. Identify 3-5 non-obvious connections between
companies in different sectors that share a common dependency, risk,
or catalyst the market is likely pricing independently. For each,
explain why the correlation matters and what trade it implies.
```

### Consensus stress test (manual, more control than /stress-test)
```
Read my thesis for [TICKER]. Now act as a skeptical short-seller.
Using only information already in my vault (research notes, sector notes,
macro notes), build the strongest possible bear case. Identify which of
my bull assumptions is weakest and where my research has gaps.
```
> For the automated, vault-updating version, use `/stress-test TICKER` instead.

### "What is priced in?" audit
```
Read the [SECTOR] notes and all linked thesis notes. For each company,
assess what the current conviction level implies about market
expectations vs. my non-consensus view. Flag any thesis where my
conviction has drifted from the evidence in my research notes.
```

### Second-order effects mapping
```
Read my macro note on [TOPIC]. Trace the second and third-order effects
through my sector notes and thesis notes. Which thesis is most exposed
to a risk I haven't written down? Which company benefits from a dynamic
I've documented in a different sector but haven't linked?
```

### Invert the thesis
```
Read my [TICKER] thesis. Assume the bear case plays out fully.
Which of my OTHER theses benefits most from that scenario? Map the
hedging relationships across my portfolio using only vault content.
```

### Cross-vault contradiction check
```
Scan my vault for internal contradictions — places where one note's
bull case depends on an assumption that another note's bear case
challenges. List each contradiction with links to both notes.
```

---

## 5. Research & Thesis Building

### Ingest from any source
```
/ingest [URL]                    # single web page
/ingest [file path]              # local PDF, MD, CSV, TXT
/ingest                          # batch — everything in _Inbox/
```
> Always follow with `/sync` then `/graph last`. `/ingest` creates the Research note; `/sync` updates theses; `/graph last` registers the new research in the dependency map.

### YouTube video transcripts via Gemini

YouTube URLs can't be `/ingest`ed directly. Use Gemini to generate a transcript first, then ingest the resulting markdown file.

1. Open Gemini and paste the YouTube URL
2. Paste the prompt below (replacing the URL placeholder) after the URL
3. Save Gemini's output as `YYYY-MM-DD - [Channel Name | Video Title] - video-transcript.md` in `_Inbox/`
4. Run `/ingest` to process into a Research note, then `/sync` to propagate

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

### Build a thesis from scratch
```
/thesis TICKER
```
> Searches vault first (existing research, sector context, macro themes), then web. Creates all 13 required sections. Status defaults to `draft` — promote with `/status TICKER status draft→active` when ready. Run `/graph last` after promotion to register the new thesis in the dependency map.

### Deepen a weak section
```
/deepen TICKER                   # auto-detects weakest section
/deepen TICKER Outstanding Questions
/deepen TICKER Key Non-consensus Insights
/deepen TICKER Industry Context
/deepen TICKER Bull Case
/deepen TICKER Bear Case
/deepen TICKER Key Metrics
/deepen TICKER Catalysts
/deepen TICKER Risks
/deepen TICKER Conviction Triggers
/deepen TICKER Business Model
```
> Creates a snapshot before editing. May also create a supporting Research note. Always follow with `/sync TICKER` → `/graph last`.

### Competitive comparison
```
/compare BESI vs AMAT            # two companies
/compare PANW NET CRWD           # three or more
```
> At least one ticker needs a thesis note. Missing tickers use web research (lighter comparison, no vault updates for them). For full-depth comparison, run `/thesis TICKER` first. Comparison updates thesis logs and sector note for tickers with existing theses. Run `/graph last` after to register the comparison research note.

### Generate a 1-page brief
```
/brief TICKER
```
> Read-only — does not modify the thesis. Creates a derivative `Research/` note. Warns if a previous brief exists (old version preserved).

### Earnings analysis (manual)
```
Fetch [TICKER]'s latest earnings transcript from [URL]. Extract: revenue
by segment, margin trends, management guidance changes, and anything
that contradicts or strengthens my thesis. Save as a research note and
append a thesis log entry with conviction impact.
```
> Or use `/ingest [URL]` → `/sync TICKER` for the automated version.

### Research a specific angle (manual)
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

### Historical analogy finder
```
Read my thesis for [TICKER]. Find the closest historical analogy —
a company in a similar position (market structure, technology transition,
investor sentiment) 5-15 years ago. What happened, and what does the
analogy imply for [TICKER]'s trajectory? What breaks the analogy?
```

### Management quality assessment
```
Research the management team of [TICKER]. Focus on: capital allocation
track record, insider ownership, previous roles, and compensation
alignment. Save as a research note and update the thesis.
```

### TAM reality check
```
Read my [TICKER] thesis. Decompose the TAM bottom-up: who are the
actual customers, what do they pay today, what would need to change
for [TICKER] to capture X%, and what's the realistic timeline? Compare
to the top-down narrative. Save as a research note.
```

---

## 6. Portfolio-Level Analysis

### Surface insights and opportunities
```
/surface                         # full vault — blind spots, correlations, research gaps
/surface NVDA                    # ticker-scoped — one thesis and graph adjacencies
/surface semiconductors          # sector-scoped — all theses in a sector
```
> Full scan: attention allocation, research velocity, decay alerts, contrarian signals, catalyst calendar, macro exposure. Saves a Research note. Scoped modes are faster but skip portfolio-wide rankings.

### Macro scenario propagation
```
/scenario Fed cuts 150bps by year-end
/scenario China invades Taiwan
/scenario oil spikes to $150
/scenario AI capex disappoints by 40%
/scenario major cybersecurity breach at a hyperscaler
```
> Two-pass triage (lightweight scan → deep read only exposed positions). Produces an impact matrix, second-order cascades, portfolio-level assessment, and recommended actions. Appends log entries to all Major-impact theses.

### Adversarial stress test
```
/stress-test TICKER
```
> Acts as a short seller. Scans for internal contradictions, builds an assumption fragility table, identifies research gaps, and proposes a falsifiable kill trigger. Flags for conviction reassessment but does NOT change conviction — that requires `/status`.

### Catalyst calendar
```
/catalyst
```
> Extracts every catalyst from every thesis (including monitoring-status). Enriches with web-searched earnings dates. Analyses catalyst clusters, gaps, and cross-thesis events. Saves/updates `_catalyst.md`.

### Portfolio exposure heatmap (manual)
```
Read all active thesis notes. Categorise each by: primary sector,
geographic exposure, macro sensitivity (rates, FX, commodity,
geopolitical), and position in the technology adoption curve. Identify
unintentional concentration risks — am I overexposed to any single
factor across multiple "independent" theses?
```

### "What am I missing?" (manual)
```
Read my sector notes and thesis notes. Based on the industries I'm
already tracking, which adjacent companies or sub-sectors am I NOT
covering that my existing research implies I should be? Prioritise by
how directly my existing theses depend on them.
```

### Value chain mapping (manual)
```
Read my [SECTOR]-related thesis notes. Map the supply chain — who is
whose customer, supplier, or competitor. Identify single points of
failure and which thesis benefits most from a bottleneck at each node.
Output as a canvas file.
```

---

## 7. Conviction & Status Management

### Change conviction
```
/status NVDA conviction medium→low China risk unhedgeable
/status BESI conviction low→medium photonics design wins accelerating
/status LITE conviction medium→high CPO attach rate above 60%
```
> Mandatory confirmation before applying. Creates pre-change snapshot. Updates sector note and `_hot.md`. Checks for trigger conflicts.

### Change status
```
/status TICKER status draft→active thesis meets quality bar
/status TICKER status active→monitoring awaiting Q3 earnings catalyst
/status TICKER status monitoring→active new catalyst emerged
/status TICKER status active→closed thesis invalidated by [reason]
```
> `draft→active` skips snapshot (no analytical content changed). `active→closed` triggers archive flow — moves file to `_Archive/`, removes from sector note. Graph cleanup is deferred to `/graph last` (run it after closure to remove the archived thesis from the adjacency index, reverse indexes, and cross-thesis clusters).

### Reaffirm after drift
```
/status NVDA reaffirm earnings miss was one-time; competitive position unchanged
/status BESI reaffirm hybrid bonding thesis intact despite cycle weakness
```
> Lightweight operation — no frontmatter change, no snapshot. Resets the drift detection window so future `/sync` runs don't keep flagging the same pattern.

### Conviction recalibration (manual, portfolio-wide)
```
Read all thesis notes with conviction: high. For each, check the most
recent log entry date. If the last update was more than 60 days ago,
flag it as stale. Summarise what has likely changed since the last
update based on the sector note and recent research.
```

---

## 8. Vault Maintenance

### Health check
```
/lint                            # full vault — 36 checks
/lint TICKER                     # scoped — 14 checks on one thesis
```
> **Full**: structural (orphaned notes, broken links, missing frontmatter, partial-write detection), freshness (stale theses, old metrics, pending sync), connection (unlinked mentions, disconnected macro, missing thesis candidates), analytical (conviction-evidence mismatch, bull/bear asymmetry, template drift, verbose log entries), snapshot hygiene, graph health (existence, staleness, missing/ghost entries, broken edges, reverse-index consistency, edge count), utility files (catalyst calendar staleness, `_hot.md` schema integrity), cross-skill contracts (log-prefix registry alignment, sector resolution coverage), and the metadata-cull surfacing checks (#32 orphaned ticker references, #33 closed-thesis files in Theses/, #35 `_hot.md` schema drift, #36 prune batch-manifest state).
> **Scoped**: frontmatter, sections, staleness, financial-data age, inactive research for ticker, conviction-evidence, bull/bear balance, template compliance, verbose logs, graph entry validity for this thesis, broken graph edges, partial-write detection, sector resolution. Faster for quick thesis checks.

### Portfolio pruning
```
/prune                           # all theses
/prune semiconductors            # sector-scoped
/prune stale                     # flag: last log entry >60 days
/prune low                       # flag: conviction low
/prune draft                     # flag: status draft
/prune monitoring                # flag: status monitoring
/prune semiconductors stale      # combined: sector + flag
```
> Checks for unsynced research first (warns if `/sync` needed). Evaluates each candidate on evidence trajectory, thesis integrity, opportunity cost, catalyst horizon, and vault connectivity. Recommends upgrade, keep monitoring, or close. Waits for approval before executing.

### Refresh / rebuild dependency graph
```
/graph last                      # incremental: re-extract changed thesis adjacencies, rebuild reverse indexes (default — run after every /sync)
/graph 7                         # catch-up incremental: same logic, watermark = today − 7 days
/graph                           # full rebuild from scratch (after /sync all or for disaster recovery)
```
> **Three modes** — choose based on how much has changed since the last graph write:
> - `/graph last` — the everyday command. Skips entirely if nothing changed; otherwise re-extracts adjacency only for changed thesis files and rebuilds reverse indexes from scratch. Cheap.
> - `/graph [N]` — catch-up after periods without `/graph last`. Same incremental logic, but watermark is today minus N days.
> - `/graph` (no args) — full rebuild. Use after `/sync all` (which intentionally doesn't update the graph), when `/lint` flags graph corruption, or when `_graph.md` is missing/poisoned. More expensive but always correct.
>
> No content files modified by any mode.

### Snapshot cleanup
```
/clean                           # delete snapshots older than 180 days
/clean 90                        # custom threshold: 90 days
/clean 30                        # aggressive: 30 days
```
> Safety net check: protects snapshots whose source file was modified after the snapshot was taken (even if old). Reports before deleting. Waits for confirmation.

### Rollback to a previous version
```
/rollback                        # list all available snapshots
/rollback TICKER                 # list snapshots for that ticker
/rollback [exact snapshot name]  # restore a specific snapshot
```
> Cascade detection: if the snapshot was created by a multi-file operation (e.g., `/sync`), offers to restore all related files atomically. Creates a pre-rollback safety snapshot (the rollback itself is reversible). Shows diff summary before confirming.

### Find orphaned research (manual)
```
List all research notes in Research/ that are not wikilinked from any
thesis or sector note. For each, suggest which thesis or sector it
should connect to, and why.
```

### Frontmatter audit (manual)
```
Scan all notes in Theses/ and Research/. List any missing required
frontmatter fields. Flag thesis notes where status is "draft" but the
note has 3+ log entries — these are probably "active".
```

### Tag taxonomy cleanup (manual)
```
List all unique tags across the vault. Flag duplicates or inconsistencies
(e.g. #semi vs #semiconductors). Suggest a consolidated tag list.
```

### Template compliance check (manual)
```
Compare each thesis note against the Thesis Template. List missing
sections — especially Key Non-consensus Insights and Outstanding
Questions. For each gap, suggest which Research/ notes could fill it.
```

---

## 9. Canvas & Visual

### Relationship map
```
Create a canvas showing all active theses grouped by sector, with edges
showing supply chain relationships, competitive dynamics, and shared
macro exposures. Colour-code by conviction level.
```

### Thesis evolution timeline
```
Create a canvas for [TICKER] showing the evolution of my thesis over
time. Use the Log entries as nodes, with annotations showing how
conviction and key arguments changed at each point.
```

### Value chain canvas
```
Read my [SECTOR]-related theses. Map the supply chain as a canvas —
who supplies whom, who competes with whom, where the bottlenecks are.
```

---

## 10. Decision Guide — "I Want To..."

| I want to... | Do this |
|---|---|
| **Start a session** | Read `_hot.md` → `/ingest` → `/sync` → `/graph last` |
| **Clip an article** | `/ingest [URL]` → `/sync` → `/graph last` |
| **Process inbox** | `/ingest` → `/sync` → `/graph last` |
| **Start covering a new company** | `/thesis TICKER` → `/status draft→active` → `/stress-test` → `/sync` → `/graph last` |
| **Improve a weak thesis** | `/deepen TICKER` → `/sync TICKER` → `/graph last` |
| **Improve a specific section** | `/deepen TICKER [section]` → `/sync TICKER` → `/graph last` |
| **Challenge a thesis** | `/stress-test TICKER` → (decide) → `/status` → `/sync` → `/graph last` |
| **Compare competitors** | `/compare A vs B` → `/sync` → `/graph last` |
| **Pitch a position** | `/brief TICKER` → `/graph last` |
| **React to earnings** | `/ingest [URL]` → `/sync TICKER` → `/graph last` → `/status` if needed |
| **React to macro event** | `/scenario [event]` → `/status` (most affected) → `/sync` → `/graph last` |
| **Handle conviction drift** | `/status TICKER reaffirm` or `/stress-test` → `/status` → `/sync TICKER` → `/graph last` |
| **Change conviction** | `/status TICKER conviction old→new [reason]` |
| **Close a position** | `/status TICKER status active→closed [reason]` → `/graph last` (cleans archived thesis from graph) |
| **Reopen an archived position** | `/rollback TICKER` → (check status — skip `/status` if already active) → `/sync TICKER` → `/graph last` (critical for recreated-file rollbacks) |
| **Find new ideas** | `/surface` or `/surface [sector]` → `/graph last` |
| **Find portfolio blind spots** | `/surface` (unscoped) → `/graph last` |
| **Model a "what if"** | `/scenario [event description]` → `/sync` → `/graph last` |
| **See what's coming up** | `/catalyst` |
| **Clean up weak positions** | `/sync` → `/graph last` → `/prune` (approve changes in-line) → `/surface` → `/graph last` |
| **Run monthly maintenance** | `/sync all` → `/graph` (full) → `/lint` → `/prune` → `/clean` → `/surface` → `/catalyst` → `/graph last` |
| **Check vault health** | `/lint` (full, 36 checks) or `/lint TICKER` (scoped, 14 checks) |
| **Update graph after recent edits** | `/graph last` (everyday refresh, cheap) |
| **Catch up after a week without /graph last** | `/graph 7` (or however many days) |
| **Fix graph corruption** | `/graph` (full rebuild) |
| **Undo a bad sync** | `/rollback TICKER` (offers cascade) → `/sync TICKER` → `/graph last` |
| **Undo a conviction change** | `/rollback TICKER` → select `(pre-status)` snapshot |
| **Delete old snapshots** | `/clean` or `/clean [days]` |
| **Rename a thesis (company name change)** | `/rename TICKER "New Company Name"` (atomic — handles wikilinks, graph, sector note, snapshots) |
| **Build a sector note** | Manual creation with Sector Template → `/graph last` → `/surface [sector]` → `/sync` → `/graph last` |
| **Deep-dive a topic** | "Teach me [TOPIC]" → saved as Research note → `/sync` → `/graph last` |
| **Resolve `/lint` #32 (orphaned ticker)** | Either `/thesis [TICKER]` to create the missing thesis, OR edit the research note's `ticker:` frontmatter to a valid ticker, OR accept as orphan |
| **Resolve `/lint` #33 (closed thesis still in `Theses/`)** | Either `mv "Theses/[file]" "_Archive/[file]"` → `/graph last` (complete the archive), OR `/status TICKER status closed→active [rationale]` → `/sync TICKER` → `/graph last` (reopen) |

---

## 11. Skill Quick Reference

> **Metadata ownership note**: After the metadata-cull architecture, only `/graph` and `/rename` write to `_graph.md`. Every other skill is content-only — they create or modify research/thesis/sector/macro/`_hot.md` files but never touch `_graph.md`. Run `/graph last` after any skill in the tables below to refresh the dependency map.

### Core Workflow Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/ingest` | none \| URL \| file path | Research note(s) | — | `/sync` → `/graph last` |
| `/sync` | none \| `all` \| TICKER | — | Theses, Sectors, Macro, `_hot.md` | `/graph last` |
| `/status` | `TICKER field old→new reason` \| `TICKER reaffirm reason` | Snapshot (except draft→active, reaffirm) | Thesis frontmatter + log, Sector note, `_hot.md` | `/sync` then `/graph last` (closure especially needs `/graph last` to clean archived thesis from graph) |

### Analytical Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/surface` | none \| TICKER \| sector | Research note (surface scan) | `_hot.md` | `/graph last` then `/deepen` or `/thesis` for opportunities found |
| `/stress-test` | TICKER | Research note (stress test) | Thesis log, `_hot.md` | `/status` (if conviction change needed) → `/sync` → `/graph last` |
| `/scenario` | event description | Research note (scenario) | Thesis logs (major-impact), `_hot.md` | `/status` (affected positions) → `/sync` → `/graph last` |
| `/compare` | TICKER vs TICKER [vs ...] | Research note (comparison) | Thesis logs, Sector note, `_hot.md` | `/sync` (if sector note changed) → `/graph last` |
| `/catalyst` | none | `_catalyst.md` (overwrite) | — | `/deepen TICKER Catalysts` for gaps |

### Building Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/thesis` | TICKER | Thesis note (draft) | Sector note (if active), `_hot.md` | `/status draft→active` → `/stress-test` → `/sync` → `/graph last` |
| `/deepen` | TICKER [section] | Snapshot + optional Research note | Thesis (target section + log), `_hot.md` | `/sync TICKER` → `/graph last` |
| `/brief` | TICKER | Research note (brief) | — (read-only derivative) | `/graph last` to register the brief in the dependency map |

### Maintenance Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/lint` | none \| TICKER | — (report only) | — | Fix flagged issues — auto-fixable graph issues → `/graph last` (or `/graph` for corruption); content issues (#32, #33) require manual triage per the lint output |
| `/prune` | none \| sector \| flag \| sector+flag | — | Theses (closures/upgrades), Sector notes, `_hot.md` | `/graph last` then `/surface` (find new opportunities) |
| `/graph` | none \| `last` \| `[N]` (integer days) | `_graph.md` (full rebuild for no-args; incremental for `last` and `[N]`) | — | — |
| `/clean` | none \| days | — | Deletes old snapshots | — |
| `/rollback` | none \| TICKER \| snapshot name | Pre-rollback safety snapshot | Restored note, Sector note, `_hot.md` | `/sync TICKER` → `/graph last` (CRITICAL for recreated-file rollbacks) |
| `/rename` | `TICKER "New Name"` | Pre-rename snapshot | Thesis filename, inbound wikilinks across vault, `_graph.md` adjacency header, Sector note Active Theses entry, `_Archive/Snapshots/` `snapshot_of:` fields, `_hot.md` mentions | — (atomic — `/rename` is the one exception that writes `_graph.md` directly) |

---

## 12. All Skill Argument Forms

### `/ingest`
```
/ingest                                    # batch: everything in _Inbox/
/ingest https://example.com/article        # single URL
/ingest /path/to/file.pdf                  # local file (PDF, MD, CSV, TXT)
```

### `/sync`
```
/sync                                      # graph-assisted: only changed files + adjacencies
/sync all                                  # brute-force: reads everything, follow with /graph
/sync NVDA                                 # ticker-scoped: one thesis + all adjacencies, ignores timestamps
```

### `/surface`
```
/surface                                   # full vault scan
/surface NVDA                              # ticker-scoped: thesis + graph adjacencies + sector peers
/surface semiconductors                    # sector-scoped: all theses in sector + sector note + macro
```

### `/stress-test`
```
/stress-test NVDA                          # single ticker
```

### `/scenario`
```
/scenario Fed cuts 150bps by year-end
/scenario China invades Taiwan
/scenario oil spikes to $150
/scenario AI capex disappoints by 40%
/scenario [any macro event with quantitative parameters]
```

### `/compare`
```
/compare BESI vs AMAT                      # two companies
/compare PANW NET CRWD                     # three or more (all need thesis notes)
```

### `/thesis`
```
/thesis NVDA                               # ticker (company name resolved automatically)
```

### `/deepen`
```
/deepen NVDA                               # auto-detects weakest section
/deepen NVDA Outstanding Questions         # specific section
/deepen NVDA Key Non-consensus Insights    # specific section
/deepen NVDA Industry Context              # specific section
/deepen NVDA Business Model                # specific section
/deepen NVDA Bull Case                     # specific section
/deepen NVDA Bear Case                     # specific section
/deepen NVDA Key Metrics                   # specific section
/deepen NVDA Catalysts                     # specific section
/deepen NVDA Risks                         # specific section
/deepen NVDA Conviction Triggers           # specific section
```

### `/brief`
```
/brief NVDA                                # single ticker
```

### `/catalyst`
```
/catalyst                                  # no arguments — scans all theses
```

### `/lint`
```
/lint                                      # full vault: 36 checks
/lint NVDA                                 # scoped: 14 checks on one thesis
```

### `/prune`
```
/prune                                     # all theses
/prune semiconductors                      # sector filter
/prune stale                               # flag: last log >60 days
/prune low                                 # flag: conviction low
/prune draft                               # flag: status draft
/prune monitoring                          # flag: status monitoring
/prune semiconductors stale                # combined: sector + flag
/prune semiconductors low                  # combined: sector + flag
```

### `/clean`
```
/clean                                     # default: 180 days
/clean 90                                  # custom threshold
/clean 30                                  # aggressive
```

### `/graph`
```
/graph                                     # full rebuild from scratch (use after /sync all or for disaster recovery)
/graph last                                # incremental: re-extract changed thesis adjacencies, rebuild reverse indexes (default — run after every /sync)
/graph 7                                   # catch-up incremental: same logic, watermark = today − 7 days
/graph 30                                  # catch-up for ~monthly missed periods
/graph 1                                   # narrow window: only files touched today
```
> Mode resolution: literal `last` → `/graph last`. Integer N → `/graph [N]`. Empty/unrecognized → full rebuild. All modes write `_graph.md` only — no content files modified.

### `/rollback`
```
/rollback                                  # list all snapshots
/rollback NVDA                             # list snapshots for NVDA
/rollback NVDA - Nvidia (pre-sync 2026-04-16-2115)   # restore specific snapshot
```

### `/rename`
```
/rename META "Meta Platforms"              # rename Theses/META - Meta.md → Theses/META - Meta Platforms.md
/rename SQ "Block"                         # post-rebrand: Theses/SQ - Square.md → Theses/SQ - Block.md
/rename SHOP "Shopify Inc"                 # add corporate suffix
```
> Atomic operation — updates filename, all inbound wikilinks (7 patterns), `_graph.md` adjacency header, sector note Active Theses entry, `_Archive/Snapshots/` `snapshot_of:` fields, and `_hot.md` mentions. TICKER does not change. To undo: run `/rename TICKER "[OldName]"` (symmetric inverse). Pre-rename snapshot also created for content-only restore via `/rollback`.

### `/status`
```
# Conviction changes
/status NVDA conviction medium→low China risk unhedgeable
/status NVDA conviction low→medium design win pipeline expanding
/status NVDA conviction medium→high all triggers met

# Status changes
/status NVDA status draft→active thesis meets quality bar
/status NVDA status active→monitoring awaiting catalyst
/status NVDA status monitoring→active catalyst emerged
/status NVDA status active→closed thesis invalidated

# Drift acknowledgment
/status NVDA reaffirm earnings miss was one-time, competitive position unchanged
```

---

## 13. Cadence Guide

### Every session
1. Read `_hot.md` for context
2. `/ingest` to process inbox
3. `/sync` to propagate
4. `/graph last` to refresh dependency map
5. Do your work (research, analysis, thesis building)
6. `/sync` again to propagate session work
7. `/graph last` again to capture session changes

### Weekly (or after heavy research)
- `/surface` or `/surface [sector you're focused on]`
- `/catalyst` to refresh the calendar
- `/lint TICKER` for any thesis you actively edited
- `/graph last` to refresh after the above
- If you missed running `/graph last` for several days: `/graph 7` (or however many days)

### Monthly
- `/sync all` → `/graph` (full) → `/lint` → `/prune` → `/clean` → `/surface` → `/catalyst` → `/graph last`
- Review `_hot.md` conviction changes and drift flags
- Conviction recalibration prompt for all high-conviction theses
- Triage any `/lint` #32 (orphaned ticker) or #33 (closed-thesis-in-Theses) findings

### When prompted by events
| Event                     | Workflow                                                                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Earnings reported         | `/ingest [URL]` → `/sync TICKER` → `/graph last` → `/status` if conviction changes                                                              |
| Macro shock               | `/scenario [event]` → `/status` for affected → `/sync` → `/graph last`                                                                          |
| New stock idea            | `/thesis TICKER` → `/status draft→active` → `/stress-test` → `/sync` → `/graph last`                                                            |
| Conviction flagged        | `/status TICKER reaffirm [reason]` (lightweight, no graph touch needed) OR investigate → `/status` change → `/sync TICKER` → `/graph last`      |
| Competitor news           | `/ingest [URL]` → `/compare` affected tickers → `/sync` → `/graph last`                                                                         |
| Sector rotation           | `/surface [sector]` → `/scenario` if macro-driven → `/compare` key players → `/sync` → `/graph last`                                            |
| Thesis closure            | `/status TICKER status active→closed [reason]` → `/graph last` (cleans archived thesis from graph adjacency, reverse indexes, clusters)         |
| Reopening archived thesis | `/rollback TICKER` → `/sync TICKER` → `/graph last` (CRITICAL — without `/graph last`, recreated thesis is invisible to graph-assisted lookups) |

### When conventions change
- Update `CLAUDE.md` if you add new folders, change conventions, or shift research focus

---

## 14. How the Vault Stays Consistent

Understanding the infrastructure helps you trust the automation and diagnose issues.

### `_hot.md` — Session Context Cache
Persists context between sessions. Sections:
- **Active Research Thread**: what you're currently working on (auto-compressed history)
- **Latest Sync**: last sync summary
- **Sync Archive**: compressed older syncs (max 3)
- **Recent Conviction Changes**: conviction/status changes and drift flags
- **Open Questions**: unresolved questions across theses
- **Portfolio Snapshot**: high-level portfolio state

Updated by: `/sync`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/thesis`, `/deepen`, `/prune`, `/status`, `/rollback`. Hard-capped at 2,000 words.

### `_graph.md` — Vault Dependency Map
Owned exclusively by `/graph`. Three modes:
- **`/graph last`** (run after every `/sync`): true incremental — re-extracts adjacency only for thesis files changed since last graph write. Reverse indexes (Sector → Theses, Macro → Theses), cross-thesis clusters, and orphan list always rebuild from scratch in-memory. This combination is cheap (skip ~30+ unchanged thesis reads) yet drift-free (reverse indexes can never accumulate stale entries because they're never incrementally updated).
- **`/graph [N]`** (e.g., `/graph 7`): catch-up mode if you missed running `/graph last` for a while. Same incremental logic, watermark = today − N days.
- **`/graph`** (no args): full rebuild from scratch (use after `/sync all` or for disaster recovery).

Research skills (`/sync`, `/thesis`, `/compare`, `/scenario`, `/deepen`, etc.) do NOT write to `_graph.md` — they create content and remind you to run `/graph last` afterward. This eliminates cross-skill graph contention.

### `_catalyst.md` — Catalyst Calendar
Regenerated each time `/catalyst` runs. Timeline format: next 2 weeks (daily), weeks 3-4, months 2-3. Flags catalyst gaps and stale events.

### `.last_sync` — Watermark
Touched at the end of every `/sync`. Used by the next `/sync` to detect which files changed since the last run. Never touched by `/graph`.

### `_Archive/Snapshots/` — Version Control
Created automatically before destructive edits by: `/sync` (Tier A section edits), `/deepen`, `/status` (except draft→active), `/compare` (sector note changes), `/prune` (sector note changes), `/catalyst` (overwrites previous calendar), `/rollback` (pre-rollback safety net). Cleaned by `/clean`. Flagged for age by `/lint`.

---

## 15. Architecture Notes & Troubleshooting

### Why `_graph.md` is owned only by `/graph`

Before the metadata-cull refactor, ten skills wrote to `_graph.md` (every research skill plus `/sync`). The result was constant cross-skill contention: a `/sync` partial-write could leave the graph half-updated, a chain of skills required a Session Chain Protocol to coordinate deferred writes, and edge cases (poisoning, drift, ghost entries) accumulated faster than they could be patched.

Concentrating ownership in `/graph` eliminated:
- **Reverse-index drift**: forward `thesis → sector` and reverse `sector → thesis` indexes are always rebuilt together from current source files
- **Session Chain Protocol**: ~80 lines of coordination logic deleted from CLAUDE.md
- **Graph Debt**: deferred-write tracking deleted (no deferred writes exist)
- **Closure-immediate exception, recreated-file exception, propagated_to 4-bucket verification**: all gone

Trade-off: you must run `/graph last` after `/sync` (or any thesis-modifying skill). Forgetting it leaves the graph stale until the next run. `/lint` check #18 surfaces this if it persists. The cost is one extra command per session.

### `/graph last` cost & precision

| Vault state | `/graph last` work |
|---|---|
| No files changed since last graph | Skip — zero reads |
| 1–5 thesis files changed | Re-extract those theses + read 19 sector/macro files for reverse indexes |
| 30+ thesis files changed | Approaches the cost of a full rebuild |

**Watermark precision is daily** (`_graph.md` frontmatter `date:` is YYYY-MM-DD). Running `/graph last` twice the same day re-processes files modified between runs — output is idempotent (correct, just wasted compute).

### Common troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `/lint` flags "Graph staleness >7 days" | Forgot to run `/graph last` after recent `/sync` runs | `/graph 7` (or however many days behind) |
| `/lint` flags "Graph staleness >30 days" | Significant gap | `/graph` (full rebuild) |
| `/graph last` announces "`.sync_all_fresh` marker detected" | Normal — `/sync all` signals `/graph` to force full rebuild; marker self-cleans after the rebuild succeeds | No action |
| `/lint` #32 — research note has `ticker:` matching no thesis | Research deposited before thesis exists, or for an archived thesis | `/thesis [TICKER]` to create, OR edit research frontmatter, OR accept as orphan |
| `/lint` #33 — closed-thesis file still in `Theses/` | Failed `mv` from `/status active→closed` or `/prune` | `mv "Theses/[file]" "_Archive/[file]"` → `/graph last` (complete archive), OR `/status TICKER status closed→active [rationale]` → `/sync TICKER` → `/graph last` (reopen) |
| `/lint` #35 — `_hot.md` missing a required section | Skill-specific Edit silently no-oped, or manual edit removed the heading | Add the missing `##` heading with a `- _pending_` bullet, OR delete `_hot.md` and let next `/sync` auto-create the full schema |
| `/lint` #36 — prune manifest `status: in-progress` | A `/prune` run crashed mid-execution | `/rollback [any ticker from the manifest body]` → select `(pre-prune)` snapshot → cascade (a) to restore all files, then `rm` the manifest |
| `/lint` #36 — prune manifest `status: completed` | Prune succeeded but Stage 5 cleanup failed | `rm "_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMM).md"` (safe — prune already finished) |
| `/sync TICKER` works but default `/sync` misses propagation | Reopened thesis not yet in `_graph.md` | `/graph last` |
| `/graph last` reports "Graph is up to date" but I just edited files | Files modified before midnight of `_graph.md` `date:` (rare timestamp ordering) | `/graph` (force full rebuild) or wait for next change to trigger |
| Multiple syncs in a single day, each running `/graph last` | Idempotent but wasteful | Acceptable — daily watermark precision means later runs may re-process earlier files |

### Architectural change vs. pre-refactor user guide

If you're returning to a workflow you used before the metadata-cull refactor:
- **No more "/graph required"** in `/sync TICKER` workflows — file-direct adjacency makes it independent
- **No Session Chain protocol** — chains run naturally; `/graph last` at the end captures everything
- **`/sync all` no longer rebuilds graph** — follow with `/graph` (full rebuild) explicitly per the monthly maintenance chain
- **Closure no longer cleans graph inline** — run `/graph last` after `/status active→closed`
- **Rollback recreating archived theses** — MUST run `/graph last` before any default `/sync` for that ticker