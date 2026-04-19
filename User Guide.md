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

> **Why `/graph last` after every `/sync`**: Research skills (`/sync`, `/thesis`, `/compare`, etc.) do not write to `_graph.md` — that ownership belongs to `/graph`. `/graph last` is the cheap finalizer that keeps the dependency map current.

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

Then refresh the graph (MANDATORY before any scoped `/surface`) and find opportunities to reallocate attention:
```
/graph last
/surface
```
> **Full chain**: `/sync` → `/graph last` → `/prune` (approve changes in-line) → `/graph last` (consume `.graph_invalidations` from closures BEFORE any scoped read) → `/surface` (new opportunities) → `/graph last` (register the surface scan note)
>
> **Why the mid-chain `/graph last`**: `/prune` closures write neighbor theses to `.graph_invalidations` and archive closed theses' files, but `_graph.md`'s Sector → Theses reverse index still lists the archived theses until `/graph last` rebuilds from current filesystem state. If `/surface [sector]` runs before this `/graph last`, scope resolution includes archived theses in the scope set — `/surface`'s scope-set existence validation now aborts the run in that case to prevent silently-incomplete analysis. Unscoped `/surface` reads `Theses/*.md` directly and is not affected by this gap.

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
/graph last                      # consume .graph_invalidations from prune closures — MANDATORY before scoped reads
/clean                           # delete old snapshots
/surface                         # find new opportunities
/catalyst                        # refresh catalyst calendar
/graph last                      # incremental refresh after /surface, /catalyst touched files
```
> Run in this order. `/sync all` before `/graph` because the sync may change links. `/graph` (full rebuild, not `last`) is correct here because `/sync all` doesn't update `_graph.md` — a full rebuild establishes the fresh baseline. `/lint` after `/graph` because lint checks graph health. `/prune` after `/lint` because lint flags staleness. **The `/graph last` after `/prune` consumes `.graph_invalidations` and rebuilds reverse indexes to exclude archived theses from Sector → Theses entries** — without this, scoped `/surface [sector]` (if the user chooses a scoped variant at the `/surface` slot) would abort with the scope-set existence validation warning. Even for unscoped `/surface`, the intervening `/graph last` keeps lint checks #18/#20/#23 green between now and the final `/graph last`. Final `/graph last` (incremental, cheap) captures changes from `/surface` and `/catalyst`.

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
>
> **Content-quality gate**: URL and PDF ingests are gated on minimum body word count (≥150 words), absence of paywall/CAPTCHA/anti-bot sentinels, and at least 2 of 4 expected body sections containing content. If the gate fails, the research note is auto-deleted (not committed) and the source is retained for re-ingestion after access is resolved. Manual local files (`.md`, `.csv`, `.txt`) receive advisory-only logs — content quality is the user's responsibility for hand-curated sources. This blocks the most damaging silent-corruption path: paywalled URLs that propagate wrong claims into thesis Log entries via `/sync`.

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
>
> **Archive-collision check**: if a closed thesis exists at `_Archive/TICKER - *.md`, the skill pauses and presents 4 explicit options before creating: (a) `/rollback TICKER` to restore the prior thesis instead, (b) proceed with a different name suffix to make dual-file state intentional, (c) proceed with proposed name accepting two distinct files for the same ticker (with caveat in initial Log entry), (d) cancel. Prevents silent dual-thesis state where the archived analysis becomes invisible to graph-assisted skills.

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

### Reverse a previously-propagated scenario
```
/scenario reverse [[Research/2026-04-19 - Scenario - Fed cut]]
/scenario reverse Fed cut
```
> Use when a prior scenario propagation no longer applies (event proved transient, supply chain fears unrealized, etc.). Appends a `Scenario REVERSED` Log entry to every previously-affected thesis with a user-provided rationale. The original `Scenario` Log entries remain (Tier 2 append-only); the reverse entry is the corrective signal. The scenario research note is preserved as historical record. Use this instead of `/rollback`, which cannot undo `/scenario` (no snapshots created).

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
/lint                            # full vault — 40 checks
/lint TICKER                     # scoped — 15 checks on one thesis
```
> **Full**: structural (orphaned notes, broken links, missing frontmatter, partial-write detection), freshness (stale theses, old metrics, pending sync), connection (unlinked mentions, disconnected macro, missing thesis candidates), analytical (conviction-evidence mismatch, bull/bear asymmetry, template drift, verbose log entries), snapshot hygiene, graph health (existence, staleness, missing/ghost entries, broken edges, reverse-index consistency, edge count), utility files (catalyst calendar staleness, `_hot.md` schema integrity), cross-skill contracts (log-prefix registry alignment, sector resolution coverage), and additional integrity checks (#32 orphaned ticker references, #33 closed-thesis files in Theses/, #35 `_hot.md` schema drift, #36 prune batch-manifest state, #37 incomplete-rename markers, #38 state marker hygiene, #39 `propagated_to:` producer contract, #41 sync manifest aging).
> **Scoped**: frontmatter, sections, staleness, financial-data age, inactive research for ticker, conviction-evidence, bull/bear balance, template compliance, verbose logs, graph entry validity for this thesis, broken graph edges, partial-write detection, sector resolution, **`_hot.md` schema integrity (#35 — always runs, vault-global concern)**, and `.rename_incomplete.TICKER` marker (#37) when the marker exists for the scoped ticker. Faster for quick thesis checks.

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
> - `/graph` (no args) — full rebuild. Use after `/sync all` (which writes `.sync_all_fresh` so that even `/graph last` correctly escalates to a full rebuild; the explicit `/graph` in the monthly chain is still recommended for clarity), when `/lint` flags graph corruption, or when `_graph.md` is missing. More expensive but always correct.
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
| **Withdraw a previously-propagated scenario** | `/scenario reverse [scenario-research-note]` → `/graph last` (no /sync needed — append-only Log entries) |
| **See what's coming up** | `/catalyst` |
| **Clean up weak positions** | `/sync` → `/graph last` → `/prune` (approve changes in-line) → `/graph last` → `/surface` → `/graph last` |
| **Run monthly maintenance** | `/sync all` → `/graph` (full) → `/lint` → `/prune` → `/graph last` → `/clean` → `/surface` → `/catalyst` → `/graph last` |
| **Check vault health** | `/lint` (full, 40 checks) or `/lint TICKER` (scoped, 15 checks) |
| **Resolve `/lint` #39 (missing `propagated_to:`)** | For `synthesis`/`brief` notes → add `propagated_to: []` (terminal). For `scenario`/`stress-test`/`comparison` notes → check referenced theses for today-date Log entries; if absent, run `/sync` to trigger retry; if present, manually backfill `propagated_to: [TICKERS]`. Pre-spec notes (date < 2026-04-19) are Nice-to-Have only. |
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

> **Metadata ownership note**: Only `/graph` and `/rename` write to `_graph.md`. Every other skill is content-only — they create or modify research/thesis/sector/macro/`_hot.md` files but never touch `_graph.md`. Run `/graph last` after any skill in the tables below to refresh the dependency map.

### Core Workflow Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/ingest` | none \| URL \| file path | Research note(s) | — | `/sync` → `/graph last` |
| `/sync` | none \| `all` \| TICKER | — | Theses, Sectors, Macro, `_hot.md`. Default/all touch `.last_sync`; **TICKER mode does NOT touch `.last_sync`** (preserves baseline for next default sync) | `/graph last` |
| `/status` | `TICKER field old→new reason` \| `TICKER reaffirm reason` | Snapshot (except draft→active, reaffirm), `.graph_invalidations` on closure | Thesis frontmatter + log, Sector note (Active Theses + Closed/Archived cleanup on reopen), `_hot.md` | `/sync` then `/graph last` (closure especially needs `/graph last` to clean archived thesis from graph + consume the invalidation list) |

### Analytical Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/surface` | none \| TICKER \| sector | Research note (surface scan; `propagated_to: []` — terminal signal blocking `/sync` Log spam to wikilinked theses) | `_hot.md` | `/graph last` then `/deepen` or `/thesis` for opportunities found |
| `/stress-test` | TICKER | Research note (stress test; `propagated_to: [TICKER]` written ATOMICALLY only after Log append succeeds — omitted on failure so `/sync` retries via `ticker:` file-direct fallback) | Thesis log (or omitted on append failure), `_hot.md` | `/status` (if conviction change needed) → `/sync` (also retries failed Log append if any) → `/graph last` |
| `/scenario` | event description \| `reverse [scenario-note]` | Research note (scenario; `propagated_to:` set ONLY if all Major-impact Log appends succeed — atomicity rule). Reverse mode creates no new note — appends `Scenario REVERSED` Log entries to previously-affected theses | Thesis logs (major-impact, or REVERSED entries in reverse mode), `_hot.md` | Forward: `/status` (affected positions) → `/sync` → `/graph last`. Reverse: `/graph last` (no /sync needed — append-only) |
| `/compare` | TICKER vs TICKER [vs ...] | Research note (comparison; `propagated_to: [tickers-with-theses]` written ATOMICALLY all-or-nothing only after every per-thesis Log append succeeds — omitted if any append fails so `/sync` retries via `tags:` file-direct fallback) | Thesis logs (succeeded targets only on partial failure), Sector note, `_hot.md` | `/sync` (if sector note changed OR to retry any failed Log appends) → `/graph last` |
| `/catalyst` | none | `_catalyst.md` (overwrite) | `_hot.md` (Active Research Thread + Open Questions for "no-catalyst" tickers) | `/deepen TICKER Catalysts` for gaps. Subsequent `/sync` auto-resolves the no-catalyst Open Questions if catalysts now exist (per `/sync` Step 6 #5b). |

### Building Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/thesis` | TICKER | Thesis note (draft) | Sector note (if active), `_hot.md` | `/status draft→active` → `/stress-test` → `/sync` → `/graph last` |
| `/deepen` | TICKER [section] | Snapshot + optional Research note | Thesis (target section + log), `_hot.md` | `/sync TICKER` → `/graph last` |
| `/brief` | TICKER | Research note (brief; `propagated_to: []` — terminal signal blocking circular self-propagation) | — (read-only derivative) | `/graph last` to register the brief in the dependency map |

### Maintenance Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/lint` | none \| TICKER | — (report only) | — | Fix flagged issues — auto-fixable graph issues → `/graph last` (or `/graph` for corruption); content issues (#32, #33, #39) require manual triage per the lint output |
| `/prune` | none \| sector \| flag \| sector+flag | Batch manifest in `_Archive/Snapshots/` (auto-deleted on success), `.graph_invalidations` on closures | Theses (closures/upgrades), Sector notes, neighbor theses' Log (Stage 4.2 "Cross-thesis closure" entries), `_hot.md`; macro notes referencing closed theses surfaced (read-only) | `/graph last` then `/surface` (find new opportunities) |
| `/graph` | none \| `last` \| `[N]` (integer days) | `_graph.md` (full rebuild for no-args; incremental for `last` and `[N]`). Consumes `.graph_invalidations` + `.sync_all_fresh` markers if present | — | — |
| `/clean` | none \| days | — | Deletes old snapshots | — |
| `/rollback` | none \| TICKER \| snapshot name | Pre-rollback safety snapshot | Restored note, Sector note, `_hot.md` | `/sync TICKER` → `/graph last` (CRITICAL for recreated-file rollbacks) |
| `/rename` | `TICKER "New Name"` | Pre-rename snapshot; `.rename_incomplete.TICKER` marker if any wikilink Edit fails after mv | Thesis filename, inbound wikilinks across vault, `_graph.md` adjacency header, Sector note Active Theses entry, `_Archive/Snapshots/` `snapshot_of:` fields, `_hot.md` mentions | Pre-flight check (Step 3.5) aborts BEFORE mv if any file is unreachable; on post-mv Edit failure, `.rename_incomplete.TICKER` marker (per-ticker filename — multiple in-flight repairs coexist) tracks repair state and `/lint` #37 surfaces each independently. Step 1.4.5 cross-new_name guard prevents marker corruption when re-running with a different name. Re-run `/rename TICKER "[same_new_name]"` to retry failed Edits — skill detects marker and skips the already-completed mv. (atomic — `/rename` is the one exception that writes `_graph.md` directly) |

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
/sync                                      # graph-assisted: only changed files + adjacencies; touches .last_sync
/sync all                                  # brute-force: reads everything; touches .last_sync; writes .sync_all_fresh marker
/sync NVDA                                 # ticker-scoped: one thesis + all adjacencies, ignores timestamps; does NOT touch .last_sync (preserves baseline for next default /sync)
```
> **Watermark behavior**: `/sync TICKER` deliberately does not advance `.last_sync`. The next default `/sync` then catches up any unrelated changes (other theses, macros, sectors) modified before the ticker-scoped run. First-run exception: if `.last_sync` is absent when `/sync TICKER` runs, an epoch placeholder is created so default sync has a baseline.

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
# Forward mode (model and propagate a scenario)
/scenario Fed cuts 150bps by year-end
/scenario China invades Taiwan
/scenario oil spikes to $150
/scenario AI capex disappoints by 40%
/scenario [any macro event with quantitative parameters]

# Reverse mode (withdraw a previously-propagated scenario)
/scenario reverse [[Research/2026-04-19 - Scenario - Fed cut]]
/scenario reverse Research/2026-04-19 - Scenario - Fed cut.md
/scenario reverse Fed cut                        # partial-name disambiguator
```
> **Reverse mode**: appends a `Scenario REVERSED` Log entry to every previously-affected thesis. The original `Scenario` Log entries remain (Tier 2 append-only) — reverse mode adds a corrective signal rather than deleting history. The scenario research note is preserved as historical record. `/sync` Step 3e drift detection treats `Scenario REVERSED` as drift-exclusion (registry §14) so the reversal doesn't inflate drift signal on the affected theses.

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
/lint                                      # full vault: 40 checks
/lint NVDA                                 # scoped: 15 checks on one thesis (#35 _hot.md schema integrity always runs)
```
> **#35 in scoped mode**: `_hot.md` schema integrity check runs in BOTH full and scoped modes. Schema drift causes silent skill no-ops across 11 skills writing to `_hot.md`; running #35 weekly via scoped lint catches drift within one weekly check rather than waiting for monthly full lint.
>
> **#37 multi-marker**: detects `.rename_incomplete.*` (per-ticker filenames). Multiple in-flight rename repairs surface independently. Scoped mode runs only for the specific ticker's marker if present.
>
> **#38 state marker hygiene**: ages `.sync_all_fresh` and `.graph_invalidations` against expected lifetimes. Surfaces "/graph hasn't run since /sync all" or "/graph last hasn't run since closure" before downstream skills silently use a stale graph.
>
> **#39 `propagated_to:` producer contract**: vault-wide only. For each `Research/*.md`, verifies the field per `source_type`: `synthesis`/`brief` must be `[]` (terminal — Important if absent regardless of date); `scenario`/`stress-test`/`comparison` must be present unless atomicity rule fired (Important if absent and date ≥ 2026-04-19; Nice-to-Have if pre-spec). `deep-dive` and other types: no requirement. Cross-checks with #1 — notes flagged by both are strongest cleanup candidates.

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
- Triage any `/lint` #32 (orphaned ticker), #33 (closed-thesis-in-Theses), #39 (`propagated_to:` producer contract), or #41 (stale sync manifests) findings

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

Updated by: `/sync`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/thesis`, `/deepen`, `/prune`, `/status`, `/rollback`, `/catalyst`. Hard-capped at 2,000 words. `/lint` #35 verifies the canonical six-section schema on full audits — missing sections cause skill-edits to silently no-op.

### `_graph.md` — Vault Dependency Map
Owned exclusively by `/graph`. Three modes:
- **`/graph last`** (run after every `/sync`): true incremental — re-extracts adjacency only for thesis files changed since last graph write. Reverse indexes (Sector → Theses, Macro → Theses), cross-thesis clusters, and orphan list always rebuild from scratch in-memory. This combination is cheap (skip ~30+ unchanged thesis reads) yet drift-free (reverse indexes can never accumulate stale entries because they're never incrementally updated).
- **`/graph [N]`** (e.g., `/graph 7`): catch-up mode if you missed running `/graph last` for a while. Same incremental logic, watermark = today − N days.
- **`/graph`** (no args): full rebuild from scratch (use after `/sync all` or for disaster recovery).

Research skills (`/sync`, `/thesis`, `/compare`, `/scenario`, `/deepen`, etc.) do NOT write to `_graph.md` — they create content and remind you to run `/graph last` afterward.

### `_catalyst.md` — Catalyst Calendar
Regenerated each time `/catalyst` runs. Timeline format: next 2 weeks (daily), weeks 3-4, months 2-3. Flags catalyst gaps and stale events.

### `.last_sync` — Watermark
Touched at the end of every `/sync`. Used by the next `/sync` to detect which files changed since the last run. Never touched by `/graph`.

### `.sync_all_fresh` — Brute-force-sync marker
Touched at the end of `/sync all` only. Read by `/graph` at Watermark Resolution; if present, `/graph` forces a full rebuild regardless of mode (`last`, `[N]`, or no-args) and deletes the marker after a successful write. Reason: `/sync all`'s two-pass triage leaves "No delta" thesis mtimes untouched, so incremental `/graph last` would miss them. The marker closes that gap without letting `/sync` write `_graph.md` directly. No user action — `/graph` manages lifecycle.

### `.graph_invalidations` — Post-closure neighbor list
Written or appended by `/status` Step 7.6 (on `active→closed`) and `/prune` Stage 4.5 (on closure runs). Contains relative paths of thesis files that `[[wikilink]]`-referenced the just-archived thesis; their `cross-thesis:` adjacency entries need re-extraction to clear dangling references. Read by `/graph last`, folded into the changed-thesis bucket, and deleted only after a successful graph write. If the graph write fails, the file persists for the next run. Dedup is via `sort -u`; repeated closures safely accumulate.

### `.rename_incomplete.TICKER` — Failed-rename repair markers (per-ticker)
Written by `/rename` Step 5.5 when one or more wikilink Edits fail mid-run after the file move has already completed. **Per-ticker filename**: each in-flight repair gets its own marker file (`.rename_incomplete.NVDA`, `.rename_incomplete.META`, etc.) so multiple concurrent rename repairs coexist without corrupting each other's state.

Each marker contains the rename context (ticker, old_name, new_name, batch ID) and the list of files whose wikilinks could not be updated. Re-run `/rename TICKER "new_name"` to retry: Step 1.3's repair-detection exception skips the already-completed mv and only re-attempts the failed Edits. The marker shrinks monotonically across repair re-runs (resolved files drop out) until empty, then auto-deletes.

`/rename` Step 1.4.5 includes a cross-new_name guard: if the marker exists with a different `new_name:` than the proposed re-run, the skill aborts with explicit options (finish prior rename first, manually resolve, or accept loss of repair state). Without this guard, two different new_names for the same ticker could overwrite each other's repair targets.

`/lint` #37 globs `.rename_incomplete.*` and surfaces each marker as Important until cleared. Pre-flight check at Step 3.5 prevents most occurrences by aborting BEFORE the mv when files are unreachable.

### `_Archive/Snapshots/_prune-manifest (prune-*).md` — `/prune` crash-recovery breadcrumb
Written by `/prune` Stage 1.5 as a persistable state record of intended closures, upgrades, and sector-note targets for the batch. Frontmatter `status: in-progress` during Stages 2-4.5; flipped to `status: completed` (and `completed_date:` added) at Stage 5 before the skill attempts `rm`. Stage 5 verifies the flip landed before deleting — if verification fails, the manifest stays as `completed` anyway so `/lint` #36 and `/clean` Step 2a surface it as "safe to delete manually". On a genuine crash, the in-progress manifest is the user's pointer to the batch ID for `/rollback` cascade recovery. `/lint` #36's Critical message distinguishes "genuinely failed prune" from "successful prune with stuck status flip" — check the manifest's Intended Closures against actual archive state before running `/rollback`.

### `_Archive/Snapshots/_sync-manifest (sync-*).md` — `/sync` Tier B audit-recovery sidecar
Written by `/sync` Step 7.5 at the end of every non-no-op sync run. Records the full batch state: every Tier A snapshot taken (recoverable via `/rollback` cascade), every Tier B Log append on a thesis WITHOUT a snapshot (cross-thesis propagation, augmented targets — NOT recoverable via cascade content restore), every sector and macro note touched, and every source research note processed. Frontmatter `type: sync-manifest`; carries `date:` not `snapshot_date:` (treated as non-snapshot artifact by `/clean` Step 2a). Consumed by `/rollback` Step 2.5b cascade detection: when the user selects a `pre-sync` snapshot, the manifest is parsed and the Tier B Log entries are surfaced for manual review (option (a) surface-only or option (b) auto-strikethrough with `~~entry~~ → Reverted YYYY-MM-DD: rolled back via /rollback batch sync-...`). Without this manifest, Tier B Log appends would persist as orphan audit entries after rollback (the contract violation the manifest was designed to fix). Aged by `/lint` #41 — Nice to Have at 90+ days, Important at 180+ days, orphan-marked when all corresponding Tier A snapshots have been cleaned.

### `_Archive/Snapshots/` — Version Control
Created automatically before destructive edits by: `/sync` (Tier A section edits), `/deepen`, `/status` (except draft→active), `/compare` (sector note changes, per-sector batch IDs on cross-sector runs), `/prune` (sector note changes), `/catalyst` (overwrites previous calendar), `/rollback` (pre-rollback safety net), `/rename` (pre-rename snapshot). Cleaned by `/clean`, which now skips non-snapshot artifacts (missing `snapshot_date:` or `type:` set to something other than snapshot). Flagged for age by `/lint` #16 and for prune-manifest state by `/lint` #36.

> **Batch ID format**: all snapshot-creating skills use `<trigger>-YYYY-MM-DD-HHMMSS` with 6-digit second-precision (e.g., `sync-2026-04-19-153042`, `prune-2026-04-19-091518`). `/rollback` cascade detection matches snapshots by batch ID prefix.

---

## 15. Architecture Notes & Troubleshooting

### Shared pre-flight layer (new in the T6 hardening release)

Every skill that modifies vault state runs a Step 0 pre-flight before reading or writing anything. The shared contract lives at `.claude/skills/_shared/preflight.md`. Four procedures:

1. **Vault lock** (`.vault-lock*` files at vault root). Prevents concurrent skill invocations from racing on `_hot.md`, thesis Logs, sector notes, `_graph.md`, and marker files. Lock scope depends on skill type — see `preflight.md` §1.2 for the concurrency matrix. `/lint #43` surfaces orphan locks (PID no longer running).
2. **Rename-marker check**. Any ticker-scoped skill operating on TICKER hard-blocks if `.rename_incomplete.TICKER` exists. Vault-wide skills mostly hard-block on any marker. Exceptions: `/lint`, `/rollback` list mode, `/graph`, `/rename` itself.
3. **Name sanitization** (for `/rename` new_name). Whitelist alphanumerics + `-_.,'&()` + spaces; reject `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`, control chars, leading dot, reserved filesystem names, length >100.
4. **Section existence probe** (for `/deepen [section]`). Abort if `## Section` heading is missing in the thesis — never silently create a new section.

### `_hot.md` compression contract (new)

Every skill that writes `_hot.md` follows `.claude/skills/_shared/hot-md-contract.md`. Key rules:
- **Per-section budgets**: Active Research Thread 30%, Latest Sync 15%, Sync Archive 20%, Recent Conviction Changes 15% (NEVER compressed), Open Questions 15%, Portfolio Snapshot 5%.
- **Soft cap 2,000 / hard cap 2,500 words**. Over soft cap, compression trigger order: drop oldest Sync Archive entry → drop oldest *Previous:* line → merge duplicate Open Questions → surface warning. Over hard cap, abort `_hot.md` write (primary operation still proceeds).
- **Truncation markers forbidden**: `...`, `[compressed]`, `[truncated]`, unclosed formatting. `/lint #42` flags.
- **Same-ticker continuation**: same thread stays live (append dated line); different ticker compresses outgoing thread to a single `*Previous:*` line.

### Scenario reversal and archive protection (6.2)

`/scenario reverse` now iterates `propagated_to:` and the body wikilinks, but for each ticker resolves the current location:
- Live thesis in `Theses/` → append `Scenario REVERSED` Log entry.
- Archived thesis in `_Archive/` → **SKIP the Log append** (Tier 3 archive protection) AND document the skip in the scenario research note body's `## Reversal Notes` section.
- Missing file → log in the R6 report; investigate manually.

`/lint #44` verifies reversal completeness — every `propagated_to:` ticker should have either a live REVERSED entry OR a documented archive skip.

### Archive-ticker registry (6.3 support)

`.archive_ticker_registry.md` at vault root is a flat append-only log of thesis archival events, auto-maintained by `/status active→closed` Step 7.5b and `/prune` Stage 2 step 5. Format: `TICKER|archived_filename.md|YYYY-MM-DD|conviction|rationale`.

Consumed by `/thesis` Step 1.2 Signal C (multi-signal archive-collision check) to detect prior archived theses even when their filename no longer matches the `_Archive/TICKER - *.md` pattern (e.g., renamed-then-archived). `/lint #46` validates registry entries against current archive state.

### Compare cross-sector atomicity (6.5)

`/compare TICKER vs TICKER vs TICKER` across different sectors now uses all-or-nothing semantics for sector note writes:
1. Snapshot every target sector note first.
2. Apply sector edits in sequence.
3. If ANY sector write fails, roll back all prior-succeeded sector edits using the pre-compare snapshots.
4. Research note and thesis Logs are preserved through the rollback (they landed in earlier phases with their own atomicity).
5. `_compare-manifest` sidecar records the transaction. `/lint #45` ages stale manifests.

### `/graph last` precise ISO watermark (6.10)

`_graph.md` frontmatter now carries `last_graph_write: YYYY-MM-DDThh:mm:ssZ` in addition to `date: YYYY-MM-DD`. Incremental delta detection uses the precise ISO timestamp when present; falls back to `date:` at 00:00:00 UTC for pre-6.10 graph files (advisory log emitted; next write upgrades the frontmatter).

### `/sync` research-note-path idempotency (6.11)

`/sync` per-thesis idempotency (Step 1 Check 3) now keys on research-note wikilink presence in the thesis Log, not today-date matching. Prevents cross-midnight duplicates: once a research note has propagated to a thesis, the skill treats that as terminal regardless of when or how many times `/sync` runs subsequently.

### `/clean` orphan snapshots (6.9)

`/clean` now classifies snapshots whose `snapshot_of:` source file is missing as **orphan** and PROTECTS them by default. Explicit opt-in required:
- `/clean orphans` — deletes only orphans, any age.
- `/clean [days] --include-orphans` — deletes age-expired snapshots AND orphans.
- `/clean [days]` (default) — age-expired deleted; orphans reported but protected.

### `/status reaffirm` always logs (6.7)

Reaffirm now always appends a Log entry regardless of whether a drift flag is active. Prefix: `Conviction reaffirmed at [level] after [drift review | proactive review] — [rationale]`. The prefix stem is canonical; the suffix (`drift review` vs `proactive review`) depends on whether a flag was cleared. Every reaffirm is visible in the Log audit trail.

### `/catalyst` pre-regenerate snapshot (6.9-adjacent)

`/catalyst` now snapshots `_catalyst.md` before regenerating. If a web-search failure produces a partial calendar, the pre-catalyst snapshot is available via `/rollback` cascade (batch ID `catalyst-YYYY-MM-DD-HHMMSS`). Prior behavior silently overwrote.

### Tier 1–4 residual fixes

**T1.1 — `/ingest` domain-specific content validators**
The post-write verification gate now includes checks #8–13 that run AFTER the generic word-count and sentinel checks. Promoted from advisory to BLOCKING for URL and PDF ingests:
- `source_type: earnings` must contain period tokens (Q1/Q2/Q3/Q4/FY20XX) + 2+ currency figures + ticker/company reference
- `source_type: analyst-report` must contain rating tokens (Buy/Sell/Hold/etc.) + price-target reference + ticker
- `source_type: news` must contain ticker + dated event reference (absolute date or temporal token)
- `source_type: deep-dive` requires ≥500 words + ≥3 substantive sections
- **#12 Numerical integrity probe**: detects OCR corruption (capital-O as zero, `II` as `11`, decimal-dropped currency like `$1 5B`)
- **#13 Title-URL consistency** (URL mode only): verifies first heading matches URL path slug via 50%+ Jaccard token overlap
Blocking failure deletes the just-written note and retains the source in `_Inbox/` for re-ingest after resolving the underlying issue.

**T1.3 — `/sync` drift sensitivity tuning**
Drift false-positive suppression now tighter:
- Deepened-entry exclusion window extended from 7 to 14 days after a Stress test
- Post-stress-test threshold: if a Stress test entry exists within 30 days for this ticker, drift requires 4/5 weakening entries (not 3/5)
- Tunable via optional `.drift-config.md` at vault root (window_size, base_threshold, post_stress_threshold, post_stress_window_days, deepened_exclusion_days)
- Drift message now reports threshold and suppression state: `⚠️ Conviction drift — 3/5 recent updates flagged headwinds (3 required, post-stress-test suppression: no)`

**T2.1 — `/sync` Step 7.5 two-phase manifest write**
Step 2.9 writes the sync manifest SKELETON (`status: in-progress`) BEFORE any Tier A snapshot or Tier B Log append lands. Skeleton write failure hard-aborts the sync pre-mutation. Steps 3–6 append accumulator entries to the manifest as work lands. Step 7.5 flips status to `completed` and verifies. If the flip fails, `/lint #41` flags it as Important (extended check). Eliminates the silent audit gap where a failed end-write used to leave Tier B Log entries invisible to `/rollback` cascade recovery.

**T2.2 — `/status` transaction manifest**
Step 3.0.5 writes a `_status-manifest (status-YYYY-MM-DD-HHMMSS).md` skeleton before any file modifications. Records intended edits: thesis frontmatter change, sector note edit, archive move (closure only), graph invalidations, `_hot.md` update. Step 7.9 flips to completed. `/rollback` Step 2.5e cascade-detects status batches and offers (a) thesis-only restore, (b) full transaction restore (thesis + sector + un-archive + clear invalidations), or (c) cancel. `/lint #48` surfaces in-progress manifests.

**T3.1 — `/stress-test` manifest for rollback cascade**
`/stress-test` Phase 4.6 now writes `_stress-test-manifest (stress-test-YYYY-MM-DD-HHMMSS).md` recording the Log entry text that was appended to the tested thesis. `/rollback` Step 2.5d uses this manifest to surface the Log entry for strikethrough review if the user decides the stress test was invalid. Research note under `Research/` is preserved (same policy as scenario / compare research notes). `/lint #47` handles aging.

### Tier 5 fixes — workflow hardening

#### 5.1 `/scenario` classification approval gate
`/scenario` forward mode now pauses at Phase 6.1.5 — AFTER the Impact Matrix is computed, BEFORE the research note or any Log entries are written. User reviews the Major/Minor classification and can (a) approve, (b) promote Minor/Neutral theses to Major (with rationale), (c) demote Major to Minor, or (d) cancel. Catches LLM misclassification (both false negatives — genuinely exposed theses dropped to Minor — and false positives — Log clutter reversible only via `/scenario reverse`). Reverse mode (R3) has its own confirmation and is unaffected.

#### 5.2 `/prune` manifest 30-day regret-recovery window
`/prune` no longer deletes its manifest at Stage 5. Instead:
- **Days 0–30**: manifest retained with `status: completed`. `/rollback` cascade-detection can surface Tier B "Cross-thesis closure" Log entries on neighbor theses if the user decides to undo an approved closure. `/lint #36` treats as Pass.
- **Days 30+**: `/clean` removes the manifest on any run. `/lint #36` emits Nice to Have from day 30.
- **Regret-recovery flow**: within 30 days of the prune, run `/rollback [any ticker from manifest's Intended Closures]` → select `(pre-prune)` snapshot → cascade (a) restores all files; `/rollback` Step 6.2.5 (5.3 fix) surfaces neighbor Log entries for strikethrough review; manually `rm` the manifest after recovery.
- 30-day window floor is absolute: `/clean 10` does NOT delete a 15-day-old completed prune manifest.

#### 5.3 `/rollback` intervening-neighbor Log scan
Recreated-file rollbacks (reopening a closed thesis) now run a Step 6.2.5 scan: find every Log entry on OTHER theses dated post-closure that cites the just-restored thesis's wikilink. Classify by prefix (`Cross-thesis closure:` = premise-dependent; `Stress test`/`Scenario`/research-note = partial premise). Present four options: surface-only, auto-strikethrough premise-dependent only, auto-strikethrough all matched, or skip. Without this scan, intervening Log entries premised on false closure persist unflagged. Step 2.5b prune-cascade surfacing still works; 6.2.5 is the primary tool for `/status active→closed` reopens (no sync manifest exists for those).

#### 5.4 `/thesis` new-sector handling
If a new thesis's `sector:` frontmatter resolves to `match_confidence: none`, `/thesis` Step 5 now prompts explicitly instead of silent-skipping: (a) create `Sectors/[sector-value].md` from Templates/Sector Template.md with minimal scaffolding and the new thesis as the first Active Thesis entry, (b) proceed without sector update (sector note can be created manually later), or (c) cancel the `/thesis` run entirely (useful if the sector value was a typo). Eliminates the prior silent-failure path where downstream skills emitted no-match warnings for the ticker indefinitely.

#### 5.5 `/ingest` source-URL dedup
`/ingest` Step 0.3 (URL and single-file modes) now greps `Research/*.md` frontmatter for `source:` value matches before writing:
- **Same-day match**: HARD BLOCK — user must delete the existing note if they genuinely want to re-ingest.
- **Cross-day match**: WARN + three-option prompt (skip / re-ingest / cancel). Cross-day re-ingests are useful for live URLs that served materially updated content since the prior ingest.
- **No match**: proceed normally.
- Batch Mode C continues to use the `_Inbox/processed/` filename-based guard.
- No canonical URL normalization (query params, fragments are provider-specific); exact string match only.

#### 5.7 `/brief` accumulation management
`/brief TICKER` creates `Research/YYYY-MM-DD - TICKER - Investment Brief.md` every run; old briefs are preserved. Over an active ticker's lifetime, this can accumulate 10–20+ briefs. Recommended management pattern:

| Cadence | Action |
|---|---|
| **Per-brief** | Latest brief is the most recent; earlier briefs stay for audit trail of narrative evolution |
| **Quarterly** | Review all briefs for a ticker; manually archive stale ones to `_Archive/Briefs/` (create directory if absent): `mv Research/YYYY-MM-DD - TICKER - Investment Brief.md _Archive/Briefs/` |
| **Annually** | Or use `/clean` with a custom threshold: briefs over 180 days old are ageable by `/clean 180` if they have `snapshot_date:` — but briefs are NOT snapshots, so they are NOT auto-cleaned. Manual archival is the canonical path. |

**Why no auto-archival**: briefs carry analytical content that may inform a future `/deepen` or `/stress-test` session. Auto-archiving on brief-recreate would silently hide these from the standard `Research/` search path. Manual archival preserves user agency.

**Finding stale briefs**: `find Research/ -name '* - * - Investment Brief.md' -mtime +90` lists briefs older than 90 days for review.

### `/graph last` cost & precision

| Vault state                       | `/graph last` work                                                       |
| --------------------------------- | ------------------------------------------------------------------------ |
| No files changed since last graph | Skip — zero reads                                                        |
| 1–5 thesis files changed          | Re-extract those theses + read 19 sector/macro files for reverse indexes |
| 30+ thesis files changed          | Approaches the cost of a full rebuild                                    |

**Watermark precision is daily** (`_graph.md` frontmatter `date:` is YYYY-MM-DD). Running `/graph last` twice the same day re-processes files modified between runs — output is idempotent (correct, just wasted compute).

### Common troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `/lint` flags "Graph staleness >7 days" | Forgot to run `/graph last` after recent `/sync` runs | `/graph 7` (or however many days behind) |
| `/lint` flags "Graph staleness >30 days" | Significant gap | `/graph` (full rebuild) |
| `/lint` #37 — `.rename_incomplete.TICKER` marker present | `/rename` completed the file move but failed wikilink Edits on N files (file lock, permission, concurrent edit) | Re-run `/rename TICKER "[new_name]"` — the skill detects the marker, skips the already-completed mv (Step 1.3 exception), and retries failed Edits. Marker shrinks across re-runs and auto-deletes when empty. |
| `/lint` #37 — multiple markers across different tickers | Multiple in-flight rename repairs (each ticker is independent) | Each marker is independent — re-run `/rename` for each ticker to clear its own marker. Per-ticker filename (`.rename_incomplete.NVDA`, `.rename_incomplete.META`) prevents cross-ticker corruption. |
| `/rename` aborts with "In-flight rename conflict for TICKER" | Marker exists with a DIFFERENT `new_name:` than the proposed re-run (e.g., user tried `/rename NVDA "Nvidia Corp"` after a failed `/rename NVDA "Nvidia Inc"`) | Either: (a) finish prior rename first via `/rename TICKER "[marker.new_name]"`, OR (b) manually resolve the failed files in the marker and `rm .rename_incomplete.TICKER`, OR (c) accept loss of repair state (`rm .rename_incomplete.TICKER`) before re-running with the new name. |
| `/lint` #38 — `.sync_all_fresh` >24h old | `/sync all` ran but `/graph` hasn't run since to consume the marker | Run `/graph` (full rebuild) — marker self-cleans on success. |
| `/lint` #38 — `.graph_invalidations` >24h old | Closures (via `/status` or `/prune`) wrote pending neighbor re-extraction list, but `/graph last` hasn't run | Run `/graph last` — file consumed and deleted on success. |
| `/ingest URL` reports "Content-quality gate FAILED" | URL fetch returned a paywall, CAPTCHA, anti-bot page, or near-empty content rather than the article | Resolve access (login, alternate URL, archive.org cache, manual download to `_Inbox/`) and re-run `/ingest`. The skill auto-deleted the contaminated research note to prevent `/sync` from propagating wrong content. |
| `/scenario` report shows "Major-impact Log appends — failed: [...]" | One or more thesis Log appends failed during scenario propagation | `/sync` (default) — the file-direct fallback re-detects the failed targets via the research note's body wikilinks and re-attempts the append. The scenario research note's `propagated_to:` was deliberately not written so dedup doesn't skip the retry. |
| `/graph last` announces "`.sync_all_fresh` marker detected" | Normal — `/sync all` signals `/graph` to force full rebuild; marker self-cleans after the rebuild succeeds | No action |
| `/lint` #32 — research note has `ticker:` matching no thesis | Research deposited before thesis exists, or for an archived thesis | `/thesis [TICKER]` to create, OR edit research frontmatter, OR accept as orphan |
| `/lint` #33 — closed-thesis file still in `Theses/` | Failed `mv` from `/status active→closed` or `/prune` | `mv "Theses/[file]" "_Archive/[file]"` → `/graph last` (complete archive), OR `/status TICKER status closed→active [rationale]` → `/sync TICKER` → `/graph last` (reopen) |
| `/lint` #35 — `_hot.md` missing a required section | Skill-specific Edit silently no-oped, or manual edit removed the heading | Add the missing `##` heading with a `- _pending_` bullet, OR delete `_hot.md` and let next `/sync` auto-create the full schema |
| `/lint` #36 — prune manifest `status: in-progress` | EITHER (1) a genuinely crashed prune, OR (2) a successful prune whose Stage 5 status-flip silently missed | FIRST disambiguate: do the theses in the manifest's "Intended Closures" list live in `_Archive/` with `status: closed`? If yes → cause (2); manually edit the manifest frontmatter to `status: completed`, then `rm` it (do NOT rollback — it would destroy valid work). If theses are still in `Theses/` with original status → cause (1); `/rollback [any ticker from the manifest body]` → select `(pre-prune)` snapshot → cascade (a) to restore all files, then `rm` the manifest. The `/prune` final report's "flip verification failed" message is the cheap tell for cause (2). |
| `/lint` #36 — prune manifest `status: completed` | Prune succeeded but Stage 5 cleanup failed | `rm "_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS).md"` (safe — prune already finished) |
| `/sync TICKER` works but default `/sync` misses propagation | Reopened thesis not yet in `_graph.md` | `/graph last` |
| `/stress-test` report shows "Log append: failed" or "`propagated_to:` frontmatter — omitted" | Phase 4.2 Log append to thesis failed (file lock, missing `## Log` section, malformed frontmatter); atomicity rule (Phase 4.4) correctly omitted `propagated_to:` to prevent permanent audit gap | `/sync` (default) — file-direct fallback resolves the thesis via the research note's `ticker:` frontmatter, today's-date idempotency check passes since no entry was written, retry succeeds. Then `/graph last`. |
| `/compare` report shows "Per-thesis Log appends — failed: [TICKER, ...]" or "`propagated_to:` frontmatter — omitted" | One or more per-thesis Log appends in Phase 5.2 failed; all-or-nothing atomicity rule (Phase 5.4) correctly omitted `propagated_to:` so failed targets get retried | `/sync` (default) — file-direct fallback resolves all compared theses via the research note's `tags:` (containing every TICKER), succeeded targets skipped via per-thesis idempotency (today-date entry exists), failed targets retried. Then `/graph last`. |
| `/lint #39` flags `synthesis` or `brief` note missing `propagated_to: []` | `/surface` or `/brief` produced a note without the terminal-skip signal; next `/sync` would Case-2a-propagate to every body-wikilinked thesis (typically 10+), spamming Logs | Add `propagated_to: []` to the note's frontmatter immediately. Investigate the producer skill — recent runs may not be following the spec. |
| `/lint #39` flags `scenario`/`stress-test`/`comparison` note missing `propagated_to:` (post-spec date) | Either (a) atomicity rule fired correctly because Log appends failed at producer time, or (b) producer skill drift | First check referenced theses' Logs for today-date entries. If entries are present on every expected ticker → manually backfill `propagated_to: [TICKERS]` (atomicity rule edge case). If entries are missing → run `/sync` to trigger the retry path. If producer is consistently broken → investigate SKILL.md spec compliance. |
| `/lint #39` flags pre-spec note (date < 2026-04-19) missing `propagated_to:` | Note created before producer-side contract was introduced — historical gap, not a current bug | Optional backfill: add `propagated_to: [resolved-tickers]` (where resolved-tickers = tickers from the note's `ticker:` frontmatter, ticker-shaped tags, and body wikilinks to `[[Theses/...]]`) if you want to suppress next `/sync TICKER` from writing today-date catch-up Log entries citing months-old research. Otherwise accept one date-stamped catch-up entry per affected thesis on next `/sync`. |
| `/lint #39` cross-flagged with #1 (orphan + missing `propagated_to:`) | Note has no Log audit trail anywhere AND no producer-contract record — strongest cleanup candidate | Either link from a thesis (then `/sync` to integrate, `propagated_to:` auto-populates), OR move to `_Archive/`. Don't leave dangling. |
| `/lint #41` flags stale `_sync-manifest (sync-...)` files in `_Archive/Snapshots/` | Sidecar manifests written by `/sync` Step 7.5; ages out at 90+ days (Nice to Have) and 180+ days (Important). Once corresponding Tier A snapshots are cleaned, the manifest no longer has cascade-recovery utility | `rm "_Archive/Snapshots/_sync-manifest (sync-YYYY-MM-DD-HHMMSS).md"` for each flagged manifest. Safe — `/rollback` cascade only consults manifests within the snapshot retention window. |
| After `/rollback` cascade on a sync batch, neighbor thesis Logs still show entries citing the rolled-back research | Cross-thesis `/sync` Log entries are Tier B (no snapshot). `/rollback` Step 2.5b surfaces these via the sync manifest sidecar | Per-entry decision: (1) leave as historical audit trail, (2) strikethrough with `~~entry~~ → Reverted YYYY-MM-DD: rolled back via /rollback batch sync-...`, (3) manually delete (violates Tier 2 — only for clearly erroneous entries). `/rollback` Step 2.5b option (b) "Cascade + strikethrough" auto-applies option 2 for every Tier B entry. |
| `/rename` warns "❌ In-flight rename conflict for TICKER" with option (c) | User accepted option (c) to delete `.rename_incomplete.TICKER` marker before re-running with a different name | The skill prints the marker's "Failed files" list with explicit warning that those files retain wikilinks to the truly-original name (NOT the prior failed-rename's new_name). Manually grep-replace `[TRULY_ORIGINAL_NAME]` → `[proposed_new_name]` in each listed file BEFORE deleting marker, OR explicitly accept broken-wikilink outcome (caught by `/lint #3`). |
| `/rename` ran but `/graph last` afterward shows "Graph is up to date" despite recent thesis edits | `/rename` Step 6 was previously updating `_graph.md date:` to today, masking pending changes. **Fixed: `/rename` no longer updates the date.** If you encounter this on an old vault, run `/graph` (full rebuild) once. | Run `/graph` (no args) once to recover. Future runs will track changes correctly. |
| `/sync all` skipped a thesis I manually edited (no Log entry) | Pre-fix: Pass 2 classification matrix only checked Log signals. **Fixed: Pass 2 now treats any thesis with own mtime > `.last_sync` as High delta and full-reads it.** | If you need to force re-evaluation now: touch the thesis file (`touch "Theses/[file]"`), then run `/sync TICKER` for that ticker, OR `/sync all` again. |
| Macro note edit didn't propagate to a thesis that wikilinks `[[Macro/X]]` | Pre-fix: `/sync` reverse index for macros only includes theses the macro wikilinks back to. **Fixed: `/sync` Step 1 now includes a body-grep file-direct fallback for changed macros — greps `Theses/*.md` for `[[Macro/[changed-macro]]]` patterns.** | If you encountered this on an old run: re-run `/sync` (default) to re-evaluate. The fallback fires automatically going forward. |
| `/sync` macro note shows duplicate Log entries or compounded analytical edits in same calendar day | Pre-fix: macro updates lacked same-day idempotency. **Fixed: `/sync` Step 5.0 now runs idempotency checks (wikilink presence + Log section + mtime fallback) before each macro edit.** | For existing duplicates: manually consolidate via Edit (Tier 2 append-only convention applies — prefer strikethrough over delete). New duplicates won't occur. |
| `/scenario reverse` ran twice for the same scenario, duplicate REVERSED Log entries on theses | Pre-fix: R2 didn't filter theses with existing REVERSED entries. **Fixed: R2 now classifies tickers and excludes already-reversed theses; re-runs are idempotent.** | For existing duplicates: manually consolidate. New runs will skip already-reversed theses with `ℹ️ Skipped [TICKER] — Scenario REVERSED entry already exists for this scenario.` log. |
| `/graph last` reports "Graph is up to date" but I just edited files | Pre-6.10: files modified before midnight of `_graph.md` `date:` (daily-precision watermark). **Fixed (6.10): `last_graph_write:` carries ISO 8601 timestamp for second-precision.** | Legacy graph: run `/graph` once to upgrade frontmatter; future runs use precise watermark. |
| Multiple syncs in a single day, each running `/graph last` | Idempotent but wasteful under daily precision. Under ISO precision (6.10), only genuinely-changed files are re-processed | Acceptable either way — correctness is preserved. |
| Any skill aborts with `❌ Another skill is running — vault lock held` | Another skill invocation holds `.vault-lock*` (6.12 concurrency control) | Wait for it to finish, OR if the holder crashed: `kill -0 [pid]` returns error → `rm [lockfile_path]` (safe when PID is dead). `/lint #43` also surfaces orphan locks. |
| Ticker-scoped skill aborts with `❌ Rename repair incomplete for TICKER` | `.rename_incomplete.TICKER` present (6.8 — pre-flight marker check) | Complete with `/rename TICKER "[new_name from marker]"` OR accept broken wikilinks by `rm .rename_incomplete.TICKER` then re-run. |
| `/rename` rejects new_name with `❌ Invalid name: [reason]` | Sanitization (6.1): disallowed char, empty, leading dot, reserved name, >100 chars | Use allowed chars only: `[a-zA-Z0-9 \-_.,'&()]`. See the rejection message for specific rule. |
| `/scenario reverse` reports "Archived theses not touched (Tier 3)" | 6.2 archive-aware reverse iteration — archived theses documented in scenario note body instead of modified | Correct behavior; check `## Reversal Notes` section of the scenario research note for full list. |
| `/thesis TICKER` prompts about archived thesis I don't recognize | 6.3 multi-signal archive check found prior analysis via Signal B (frontmatter ticker), C (archive registry), or D (snapshot trail) — not just filename | Inspect the reported archive, then choose option (a) rollback, (b) different name suffix, (c) accept dual-file state, (d) cancel. |
| `/deepen TICKER [section]` aborts with "Section not found" | 6.4 section existence probe — target section doesn't exist in the thesis | Pick an existing section (list shown in error), OR restore missing section from Templates/Thesis Template.md then retry, OR run `/deepen TICKER` for auto-detect. |
| `/compare` aborts mid-run with "Sector note write failed — rolled back" | 6.5 cross-sector atomicity — one sector's Edit failed; all prior sector edits rolled back | Research note and thesis Logs preserved. Resolve the sector file issue (lock, permission), then re-run `/compare` cleanly. |
| `_hot.md` exceeds 2,500 words after a skill runs | Hard cap reached; skill aborted `_hot.md` update (primary operation still succeeded) | Manually trim Sync Archive or `*Previous:*` lines, OR `/lint #35` + `/lint #42` to diagnose drift. |
| `/clean` reports "Orphan snapshots: N protected" | 6.9 — snapshots whose source file is missing default to PROTECTED | Investigate (was source mistakenly deleted?). To delete: `/clean orphans` (any age) or `/clean [days] --include-orphans`. |
| `/catalyst` produced a partial calendar (web search failed) | 6.9-adjacent pre-overwrite snapshot retained the prior calendar | `/rollback` → select `(pre-catalyst YYYY-MM-DD-HHMMSS)` snapshot to restore the prior richer calendar. Re-run `/catalyst` when web access is resolved. |
| `/sync` writes duplicate Log entries across midnight | Pre-6.11: today-date idempotency keyed duplicates at day rollover. **Fixed (6.11): now keyed on research-note wikilink presence in Log.** | If legacy duplicates exist: manually consolidate (strikethrough the duplicate per Tier 2 convention). New runs are idempotent across midnight. |
| `/status TICKER reaffirm` Log entry visible even when no drift flag was active | 6.7 — reaffirm always appends Log entry for audit completeness. Format: `Conviction reaffirmed at [level] after [drift review \| proactive review] — [rationale]` | Correct behavior. Every reaffirm is audit-visible. |
| `/scenario` now pauses at "Classification approval gate" | 5.1 — Phase 6.1.5 added; shows Major/Minor/Neutral classification before any Log appends | Options: (a) approve, (b) promote specific tickers to Major with rationale, (c) demote Major to Minor, (d) cancel (no files written). Correct behavior — catches LLM misclassification. |
| Completed prune manifest persists in `_Archive/Snapshots/` days after prune | 5.2 — 30-day regret-recovery window retention; `/clean` removes after day 30 | Correct behavior. Within 30 days, supports `/rollback` cascade-detection for neighbor Log entries if you decide to undo a closure. `/lint #36` treats as Pass until day 30. |
| `/rollback` of a closed thesis surfaces "Intervening Log entries detected" | 5.3 — Step 6.2.5 scan found post-closure Log entries on neighbor theses citing the just-restored thesis | Options: (a) surface-only, (b) auto-strikethrough `Cross-thesis closure:` premise entries, (c) auto-strikethrough all matched, (d) skip. Choice depends on how confidently you want to invalidate old premise. |
| `/thesis TICKER` prompts about missing sector note | 5.4 — `match_confidence: none` now has explicit 3-option branch instead of silent skip | Options: (a) create `Sectors/[value].md` scaffold with this thesis as first entry, (b) proceed without sector update, (c) cancel to fix the sector value. |
| `/ingest URL` blocked with "Source already ingested today" | 5.5 — Step 0.3 same-day URL dedup | Delete existing note first if you genuinely want to re-process: `rm "Research/[matched-note].md"` then re-run. |
| `/ingest URL` prompts about "previously ingested" (older than today) | 5.5 — cross-day URL match | Options: (a) skip and use existing note, (b) re-ingest as new dated note (coexist cleanly with prior due to T6 6.11 wikilink idempotency), (c) cancel. |
| `/brief TICKER` accumulating many files under `Research/` | 5.7 — no auto-archival by design; briefs are analytical content | Quarterly: `find Research/ -name '*Investment Brief.md' -mtime +90` to list stale; manually `mv` chosen ones to `_Archive/Briefs/` (create dir if absent). |
| `/ingest URL` reports `Content-quality gate FAILED — #8 earnings signature` (or #9/#10/#11) | T1.1 — domain validator flagged missing domain vocabulary for declared `source_type` | Either (a) the fetched content is off-topic (paywall / wrong article) — re-ingest after resolving access, or (b) `source_type` was wrong for the content — edit and re-ingest with correct source_type. Note was NOT created; source retained in `_Inbox/`. |
| `/ingest URL` reports `#12 numerical integrity FAILED` | T1.1 — OCR-style corruption detected (capital-O as zero, decimal-dropped currency, etc.) | PDF source was likely image-based and OCR extracted garbage. Convert PDF to text via a cleaner tool (preview.app, pdftotext) or manually create `.md` from the source. |
| `/ingest URL` reports `#13 title-URL mismatch` | T1.1 — first heading token set has <50% Jaccard overlap with URL path slug | Fetch likely redirected to a login/subscribe/error page with a different title than the intended article. Re-ingest after resolving; use `archive.org` cache if paywalled. |
| `/sync` reports `Conviction drift — 3/5 recent updates flagged headwinds (3 required, post-stress-test suppression: yes)` | T1.3 — drift fired despite stress-test suppression | Threshold was 4/5 not 3/5 — if you see this AND 3/5, the post-stress-test suppression was correctly INACTIVE (no recent stress test). Otherwise genuine drift signal. `/status TICKER reaffirm` to acknowledge, or investigate. |
| `/sync` drift signal never fires despite obvious deterioration | T1.3 — post-stress-test suppression raised threshold to 4/5 | Expected within 30 days of a stress test. If you want base sensitivity back, edit `.drift-config.md` at vault root: `post_stress_threshold: 3` AND `post_stress_window_days: 0`. |
| `/lint #41` reports `In-progress sync manifest` | T2.1 — Step 7.5 flip failed OR /sync crashed mid-run OR /lint ran during active /sync | Inspect manifest body for landed Tier A snapshots and Tier B Log appends. If /sync was interrupted, use `/rollback` on listed snapshots. If /sync completed and only flip failed, manually edit manifest to `status: completed`. |
| `/lint #48` reports `In-progress /status manifest` | T2.2 — Step 7.9 flip failed OR /status crashed mid-transaction | Inspect body for landed stages. Full transaction recovery via `/rollback [batch]` → option (b) cascade restore (thesis + sector + un-archive + invalidations). |
| `/lint #47` reports `In-progress stress-test manifest` | T3.1 — rare; /stress-test normally writes manifest as completed in one step | Verify research note + thesis Log entry both exist. If yes, manually edit to `status: completed`. If either missing, re-run /stress-test. |
| `/rollback` on a stress-test batch ID surfaces the Log entry | T3.1 — Step 2.5d cascade | Choose (b) cascade + strikethrough to rewrite Log entry as `~~...~~ → Reverted YYYY-MM-DD: stress-test judged invalid`. Research note is preserved. |
| `/rollback` on a status batch ID offers "thesis-only" vs "full transaction" | T2.2 — Step 2.5e cascade | Full transaction (b) restores thesis + sector + un-archives (if closure) + clears invalidations. Thesis-only (a) restores frontmatter only. |

