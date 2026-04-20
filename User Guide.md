# User Guide — Claude Code + Obsidian for Investment Research

> Your vault has **39 theses**, **129 research notes**, **13 sector notes**, and **6 macro notes**. This guide covers every skill, ery argument form, every multi-skill workflow chain, and every natural language query pattern available. Ordered by impact — start at the top.

---

## 0. First Run

If this is a brand new vault (no prior `/sync` runs), run this bootstrap sequence:

```
/sync                            # creates _hot.md + .last_sync, reads all vault files
/graph                           # creates _graph.md from vault state
```

After bootstrap, all skills work. Without it:
- `/sync TICKER` and scoped `/surface` require `_graph.md` — they block if it's missing
- `/prune` pre-flight unsynced-research check has no `.last_sync` baseline to compare against
- Skills that update `_hot.md` will auto-create it (CLAUDE.md rule #9), but `/sync` produces a richer initial version with Latest Sync data and Portfolio Snapshot

> If the vault already has thesis/research/sector notes, `/sync` reads everything on first run (equivalent to `/sync all`). This is expected — it establishes the watermark baseline.

> **`.last_sync` deletion = de facto first run**: if `.last_sync` is ever deleted (manually, accidentally, or via a `git restore` that wipes it), the next `/sync` (any mode) treats the vault as first-run: creates an epoch placeholder, then `find -newer` matches every file. Effect: a `/sync` invocation you expected to finish in ~30 seconds takes 5-10× longer because it re-reads the entire vault. `/prune` Phase 0 also detects this state and now prompts before running (B4 fix). To check before invoking: `ls -la .last_sync` — if missing, expect first-run behavior on next sync. To recover the watermark without a full sync, you can `touch .last_sync` to set it to "now" — but this silently marks all currently-pending files as "synced," which is usually wrong. Prefer letting the next `/sync` create the epoch placeholder and re-process correctly.

---

## 1. The Core Loop

Every session follows the same rhythm: **deposit → ingest → sync**. Everything else extends this loop.

```
_Inbox/ drop  →  /ingest  →  /sync  →  work  →  /sync
```

| Step | What happens | Time |
|------|-------------|------|
| Drop raw content into `_Inbox/` | Web clips, PDFs, CSVs, notes — any format | Between sessions |
| `/ingest` | Transforms `_Inbox/` into structured Research notes with wikilinks | ~2 min |
| `/sync` | Propagates new insights to all affected theses, sector notes, macro notes, `_hot.md` | ~3 min |
| Work | Research, analysis, thesis building, conviction changes | Variable |
| `/sync` | Propagate again after making changes | ~3 min |

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
```
Then:
```
/sync
```
> `/ingest` creates Research notes only. `/sync` propagates the insights to theses, sectors, macro notes. Always run both.

### Earnings season triage
```
Which of my thesis companies report earnings in the next 2 weeks?
For each, list the key metrics and outstanding questions from my thesis
note that the report should answer.
```

---

## 3. Workflow Chains

Multi-skill sequences for common scenarios. Each chain shows the optimal order — skipping steps weakens the outcome.

> **`/graph last` is implicit at every chain end**. Every chain below that creates a thesis, edits a thesis, creates a research note, or closes a position leaves the dependency graph in a pending state — mtime advances on changed files plus any `.graph_invalidations` appended by closure operations. Run `/graph last` once the chain completes (or `/graph` full if the chain included a `/rename` or recreated an archived thesis). Only pure read-only chains (`/brief` alone, `/lint`, `/rollback` list mode) and chains ending in `/graph` itself skip this. §3 chains that already include an explicit `/graph last` step note it inline; all others assume you know to run it at the end.

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
Propagate stress test findings:
```
/sync TICKER
```
> **Full chain**: `/thesis` → `/status draft→active` → `/stress-test` → `/sync TICKER`
> **Optional extension**: Add `/compare TICKER vs COMPETITOR` before `/sync` for competitive context. Add `/deepen TICKER [weakest section]` to fill gaps the stress test identified.

### 3b. New Position — From Existing Research

**When**: You've been collecting research on a ticker and want to formalise a thesis.

```
/ingest                          # process any inbox items first
/sync                            # propagate to existing notes
/thesis TICKER                   # vault research is used automatically
/status TICKER status draft→active [rationale]
/sync TICKER                     # propagate new thesis connections
```

### 3c. Earnings Reaction

**When**: A thesis company just reported earnings.

```
/ingest [transcript or press release URL]
/sync TICKER
```
If the report changes conviction:
```
/status TICKER conviction old→new [what the report revealed]
```
If the report was ambiguous, stress-test first:
```
/stress-test TICKER
```
> **Full chain**: `/ingest URL` → `/sync TICKER` → (assess) → `/status` or `/stress-test` → `/sync`

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
```

**Path C — Investigate with targeted research**:
```
/deepen TICKER [section the drift relates to]
/sync TICKER
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
Propagate all changes:
```
/sync
```
> **Full chain**: `/scenario` → `/status` (most affected) → `/compare` (competitive shifts) → `/sync`

### 3f. Thesis Improvement — Targeted

**When**: A thesis section is weak, stale, or flagged by `/lint`.

```
/deepen TICKER [section name]
/sync TICKER
```
> `/deepen` auto-detects the weakest section if you omit the section name. Always follow with `/sync TICKER` to propagate.

### 3g. Thesis Improvement — Adversarial

**When**: You want to pressure-test conviction before a major decision.

```
/stress-test TICKER
/deepen TICKER [section the stress test identified as weakest]
/sync TICKER
```
> The stress test identifies vulnerabilities. `/deepen` fills the gaps. `/sync` propagates.

### 3h. Competitive Reassessment

**When**: Competitive dynamics in a sector are shifting.

```
/compare A vs B
```
If the comparison changes conviction on either name:
```
/status TICKER conviction old→new [competitive insight]
```
Propagate:
```
/sync
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
> **Full chain**: `/sync` → `/prune` (approve changes in-line) → `/surface` (new opportunities) → `/graph last` (apply graph invalidations from `/prune` closures and the new `/surface` research note)

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
/graph                           # register new sector note in the reverse index
/surface [sector]
/compare [key players in sector]
/sync
```
> `/graph` is required before `/surface` — sector scoping uses `_graph.md`'s Sector → Theses reverse index, which won't include a newly created sector note until `/graph` runs. If building multiple theses in a new sector: create the sector note first, then for each company run `/thesis TICKER` **followed by `/status TICKER status draft→active [rationale]`**, then `/graph`. **Draft theses are intentionally omitted from sector notes' Active Theses sections** (CLAUDE.md Thesis Notes convention), so `/surface [sector]` — which resolves scope via the sector note's Active Theses list — will silently skip any thesis still in draft. Promoting each new thesis to active before the `/graph` rebuild ensures sector-scoped skills see the full cohort.

### 3l. Monthly Maintenance

**When**: Monthly or when the vault feels out of sync.

```
/sync all                        # full brute-force propagation
/graph                           # rebuild dependency graph from scratch
/lint                            # full health audit
/prune                           # portfolio evaluation
/clean                           # delete old snapshots
/surface                         # find new opportunities
/catalyst                        # refresh catalyst calendar
/graph last                      # apply graph invalidations from /surface and /prune
```
> Run in this order. `/sync all` before `/graph` because the sync may change links. `/lint` after `/graph` because lint checks graph health. `/prune` after `/lint` because lint flags staleness. `/surface` near the end because the vault is now clean and complete. Final `/graph last` applies the invalidations `/prune` (closures) appended to `.graph_invalidations` plus any changed-thesis adjacencies the mtime-watermark picks up. Note: `/surface` does NOT write `.graph_invalidations`; a new `/surface` research note becomes visible to the graph on the next full `/graph` (orphan list recompute) or when a thesis is next Edited to wikilink to it.

### 3m. Recovery — Undo a Bad Sync

**When**: `/sync` produced changes you disagree with.

```
/rollback TICKER
```
Select the `(pre-sync)` snapshot. Rollback detects cascade operations — if `/sync` touched multiple files, it offers to restore all of them atomically. For pre-batch-ID snapshots `/rollback` presents a legacy disambiguation prompt; for sync-manifest snapshots it asks how to handle Tier B cross-thesis Log appends (surface only, cascade + strikethrough, or single-file).

After rollback, **scope the re-propagation to match what was restored**:
```
# If the cascade restored a single thesis:
/sync TICKER                     # re-propagate from the restored state

# If the cascade restored multiple theses (the common case for default /sync):
/sync all                        # /sync TICKER only touches one thesis's adjacency,
                                 # leaving the other cascaded files in restored-but-unsync'd state
/graph                           # full rebuild, since cascade may have changed link structure
```
> **Propagated-research caveat**: `/rollback` restores thesis/sector/macro **files** from snapshots, but does **not** rewrite the `propagated_to:` frontmatter of research notes that were consumed during the reverted `/sync`. If the originating research note is still in `Research/` with `propagated_to: [TICKER]`, the next `/sync` will see the dedup flag and skip re-applying the research to that thesis — silently leaving it in the restored (pre-propagation) state. If you need a specific research note re-propagated post-rollback, either (a) remove the relevant ticker from that note's `propagated_to:` list manually, or (b) delete and re-`/ingest` the source.

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
/graph
```

### 3o. Pre-Meeting Prep

**When**: You need to pitch or discuss a position.

```
/brief TICKER
```
For adversarial prep (anticipating pushback):
```
/stress-test TICKER
/brief TICKER
```
> The brief distils the thesis into a 1-page memo. The stress test identifies the weakest points so you can prepare rebuttals.
> **Note**: Both `/stress-test` and `/brief` create research notes. Neither writes to `.graph_invalidations` — `/stress-test` Edits the thesis Log (mtime advance → `/graph last` picks up the adjacency via watermark), `/brief` is purely derivative (research note only, no thesis Edit). For a read-heavy prep workflow, running `/graph last` after the chain refreshes `/stress-test` adjacency; `/brief`'s new note appears in the orphan list only on the next full `/graph`.

### 3p. Research Session — Ad Hoc Topic

**When**: Researching a topic that may affect multiple theses.

```
/ingest [URL1]
/ingest [URL2]
/ingest [URL3]
/sync
```
Or for manual research:
```
Research [TOPIC] for [TICKER]. Focus on [specific angle]. Save to
Research/ and update the relevant thesis log.
```
Then:
```
/sync
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
> **Note**: `/prune` writes to `.graph_invalidations` (closure branch); `/deepen` does not — `/deepen`'s thesis Edit advances the mtime and `/graph last`'s watermark picks it up. Run `/graph last` after the chain either way.

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
> Always follow with `/sync` to propagate. `/ingest` creates the Research note; `/sync` updates theses.
> **Same-source dedup**: `/ingest` hard-blocks a URL already ingested today (identical `source:` frontmatter). Older same-source ingests surface a three-option prompt (append as update, supersede old note, cancel). If you hit a hard-block and the prior note is a stub or wrong, delete it from `Research/` first, then re-run.

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
> Searches vault first (existing research, sector context, macro themes), then web. Creates all 13 required sections. Status defaults to `draft` — promote with `/status TICKER status draft→active` when ready.
> **Archive-collision prompt**: if a prior thesis for this TICKER exists in `_Archive/` (detected via filename match, frontmatter ticker, the archive registry, or an existing snapshot trail), `/thesis` pauses with a four-option menu: (a) exit to `/rollback` the archived thesis instead of starting fresh, (b) proceed with a new thesis noting the archived predecessor in the Log, (c) proceed without note, (d) cancel. Option (a) is the right choice if the archived research is still relevant; option (b) when the old thesis is outdated but its existence should be auditable.
> **`draft→active` has no pre-status snapshot**. The promotion doesn't change analytical content, so `/status` skips the snapshot (this is the documented exception). If you want to reverse a mistaken promotion, there is no `(pre-status)` snapshot to `/rollback` to — you'll need to manually flip frontmatter back to `draft` and trim the `Status change: draft → active` Log entry.

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
> Creates a snapshot before editing. May also create a supporting Research note. Always follow with `/sync TICKER`.

### Competitive comparison
```
/compare BESI vs AMAT            # two companies
/compare PANW NET CRWD           # three or more
```
> At least one ticker needs a thesis note. Missing tickers use web research (lighter comparison, no vault updates for them). For full-depth comparison, run `/thesis TICKER` first. Comparison updates thesis logs and sector note for tickers with existing theses.

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
> `draft→active` skips snapshot (no analytical content changed). `active→closed` triggers archive flow — moves file to `_Archive/`, removes from sector note, cleans up graph.

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
/lint                            # full vault — 47 checks
/lint TICKER                     # scoped — ~16 checks on one thesis (15 always + #42 always + #37 conditional if rename marker present)
```
> **Full**: structural (orphaned notes, broken links, missing frontmatter), freshness (stale theses, old metrics), connection (unlinked mentions, disconnected macro), analytical (conviction-evidence mismatch, bull/bear asymmetry, template drift), snapshot hygiene, graph health.
> **Scoped**: frontmatter, sections, staleness, conviction-evidence, template compliance, graph entry validity. Faster for quick thesis checks.

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

### Rebuild dependency graph
```
/graph
```
> Rebuilds `_graph.md` from scratch by scanning all wikilinks in Theses/, Sectors/, Macro/, Research/. No content files modified. Run after `/sync all`, when `/lint` flags graph issues, or when the graph has drifted.

### Snapshot cleanup
```
/clean                           # delete snapshots older than 180 days (orphans PROTECTED)
/clean 90                        # custom age threshold: 90 days (orphans PROTECTED)
/clean 30                        # aggressive: 30 days (orphans PROTECTED)
/clean orphans                   # delete only orphans (source file missing), any age
/clean 180 --include-orphans     # age-based cleanup PLUS orphan deletion
```
> **Safety net check**: protects snapshots whose source file was modified after the snapshot was taken (even if old). Reports before deleting. Waits for confirmation.
> **Orphans are protected by default**: a snapshot whose `snapshot_of:` target no longer exists is often the only recovery path for a mistakenly-deleted file. Default mode lists them but does not delete. Use `/clean orphans` or `--include-orphans` only when you've explicitly reviewed the list.
> **Do not run `/clean orphans` within ~30 days of `/prune` closures**: the pre-prune snapshots `/prune` created for each closed thesis become orphans the moment the thesis file moves to `_Archive/`. Deleting them destroys the regret-recovery path for the prune itself. (Prune *manifests* are protected under a 30-day regret window automatically; the thesis **snapshots** aren't.) If you're doing monthly maintenance (§3l) and want to reclaim space aggressively, run `/clean orphans` **before** `/prune`, not after.
> **Prune-manifest retention**: completed `_prune-manifest*.md` files are kept 30 days for regret-recovery regardless of age threshold. `/clean` reports them separately.

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
| **Start a session** | Read `_hot.md` → `/ingest` → `/sync` |
| **Clip an article** | `/ingest [URL]` → `/sync` |
| **Process inbox** | `/ingest` → `/sync` |
| **Start covering a new company** | `/thesis TICKER` → `/status draft→active` → `/stress-test` → `/sync` |
| **Improve a weak thesis** | `/deepen TICKER` → `/sync TICKER` |
| **Improve a specific section** | `/deepen TICKER [section]` → `/sync TICKER` |
| **Challenge a thesis** | `/stress-test TICKER` → (decide) → `/status` → `/sync` |
| **Compare competitors** | `/compare A vs B` → `/sync` |
| **Pitch a position** | `/brief TICKER` |
| **React to earnings** | `/ingest [URL]` → `/sync TICKER` → `/status` if needed |
| **React to macro event** | `/scenario [event]` → `/status` (most affected) → `/sync` |
| **Handle conviction drift** | `/status TICKER reaffirm` or `/stress-test` → `/status` |
| **Change conviction** | `/status TICKER conviction old→new [reason]` |
| **Close a position** | `/status TICKER status active→closed [reason]` |
| **Reopen an archived position** | `/rollback TICKER` → (check status — skip `/status` if already active) → `/sync` → `/graph` |
| **Find new ideas** | `/surface` or `/surface [sector]` |
| **Find portfolio blind spots** | `/surface` (unscoped) |
| **Model a "what if"** | `/scenario [event description]` |
| **See what's coming up** | `/catalyst` |
| **Clean up weak positions** | `/sync` → `/prune` (approve changes in-line) → `/surface` → `/graph last` |
| **Run monthly maintenance** | `/sync all` → `/graph` → `/lint` → `/prune` → `/clean` → `/surface` → `/catalyst` → `/graph last` |
| **Check vault health** | `/lint` (full) or `/lint TICKER` (scoped) |
| **Fix graph issues** | `/graph` |
| **Undo a bad sync** | `/rollback TICKER` (offers cascade) → `/sync TICKER` (single-file) or `/sync all` (cascade — see §3m propagated-research caveat) |
| **Undo a conviction change** | `/rollback TICKER` → select `(pre-status)` snapshot |
| **Delete old snapshots** | `/clean`, `/clean [days]`, `/clean orphans`, or `/clean [days] --include-orphans` (see §8 for post-prune safety warning) |
| **Rename a thesis (company name change)** | `/rename TICKER "New Company Name"` (file rename is atomic via `mv`; wikilink rewrites are best-effort with a `.rename_incomplete.TICKER` marker on partial failure — re-run `/rename` to repair, then ticker-scoped skills unblock) |
| **Build a sector note** | Manual creation with Sector Template → `/graph` → `/surface [sector]` → `/sync` |
| **Deep-dive a topic** | "Teach me [TOPIC]" → saved as Research note → `/sync` |

---

## 11. Skill Quick Reference

> **Reading the Modifies column**: `_graph.md` is owned exclusively by `/graph` and `/rename` (the latter surgically rewrites one adjacency header). Other skills signal graph updates indirectly: they edit thesis/sector/macro files (mtime-advance picked up by `/graph last`), append to `.graph_invalidations` on closures, or create research notes that surface in `/graph`'s orphan list on the next rebuild. Those indirect effects are listed explicitly — "modifies `_graph.md`" appears only for direct writers.

### Core Workflow Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/ingest` | none \| URL \| file path | Research note(s) | — (no thesis/sector edits) | `/sync` → `/graph last` |
| `/sync` | none \| `all` \| TICKER | Tier A snapshots, `_sync-manifest` | Theses, Sectors, Macro, `_hot.md`, `.last_sync` (default/all only); advances thesis mtimes for `/graph last` | `/graph last` |
| `/status` | `TICKER field old→new reason` \| `TICKER reaffirm reason` | Snapshot (except draft→active, reaffirm), `_status-manifest` | Thesis frontmatter + Log, Sector note, `_hot.md`; appends `.graph_invalidations` (closure branch only); appends `.archive_ticker_registry.md` (closure) | `/sync` (conviction changes) → `/graph last` |

### Analytical Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/surface` | none \| TICKER \| sector | Research note (surface scan) | `_hot.md` only (new research note appears in graph orphan list on next full `/graph`) | `/deepen` or `/thesis` for opportunities found; `/graph last` |
| `/stress-test` | TICKER | Research note (stress test), `_stress-test-manifest` | Thesis Log + Related Research, `_hot.md`; advances thesis mtime for `/graph last` | `/status` (if conviction change needed) → `/sync` → `/graph last` |
| `/scenario` | event description \| `reverse [note]` | Research note (scenario, forward mode only) | Thesis Logs (Major-impact forward; previously-affected on reverse), `_hot.md`; advances mtimes | `/status` (affected positions) → `/sync` → `/graph last` |
| `/compare` | TICKER vs TICKER [vs ...] | Research note (comparison), sector-level snapshots, `_compare-manifest` | Thesis Logs, Sector note(s), `_hot.md`; advances mtimes | `/sync` (sector note changes) → `/graph last` |
| `/catalyst` | none | `_catalyst.md` (overwrite), pre-catalyst snapshot | `_hot.md` | `/deepen TICKER Catalysts` for gaps |

### Building Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/thesis` | TICKER | Thesis note (draft), `_thesis-manifest` | Sector note (only if status flipped to active), `_hot.md`; advances orphan-research mtimes | `/status draft→active` → `/stress-test` → `/sync` → `/graph last` |
| `/deepen` | TICKER [section] | Pre-deepen snapshot, optional Research note | Thesis (target section + Log two-phase), `_hot.md`; advances thesis mtime | `/sync TICKER` → `/graph last` |
| `/brief` | TICKER | Research note (brief, with `propagated_to: []` terminal dedup) | `_hot.md` only (no thesis edits — fully derivative) | `/graph last` |

### Maintenance Skills

| Skill | Arguments | Creates | Modifies | Follow-up |
|-------|-----------|---------|----------|-----------|
| `/lint` | none \| TICKER | — (report only) | — (read-only) | Fix flagged issues → `/graph` if graph issues |
| `/prune` | none \| sector \| flag \| sector+flag | Snapshots per closure/upgrade, `_prune-manifest` | Theses (closures/upgrades), Sector notes, `_hot.md`; appends `.graph_invalidations` (closure branch); appends `.archive_ticker_registry.md` | `/graph last` (consume invalidations); `/surface` (find new opportunities) |
| `/graph` | none \| `last` \| N (days) | `_graph.md` (full rebuild or incremental merge) | `_graph.md`; clears `.graph_invalidations` and `.sync_all_fresh` on success | — |
| `/clean` | none \| days \| `orphans` \| days `--include-orphans` | — | Deletes old snapshots (age-based by default); deletes orphans only on explicit opt-in | — |
| `/rollback` | none \| TICKER \| snapshot name | Pre-rollback safety snapshot, sector pre-edit snapshot (if sector touched), relocated-archive snapshots (closure restore) | Restored note, Sector note, `_hot.md`; advances restored-file mtime for `/graph last` | `/sync TICKER` or `/sync all` (cascade) → `/graph` (full, if recreated archived thesis) |
| `/rename` | `TICKER "New Name"` | Pre-rename snapshot, `.rename_incomplete.TICKER` on partial failure | Thesis filename, all inbound wikilinks (live + snapshot bodies), `_graph.md` adjacency header (direct surgical write), Sector note Active Theses entry, `_Archive/Snapshots/` `snapshot_of:` fields, `_hot.md` mentions | `/graph` (full, not `last`) — see §12 for rationale |

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
/lint                                      # full vault: 47 checks
/lint NVDA                                 # scoped: ~16 checks on one thesis
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
/clean                                     # default age: 180 days; orphans PROTECTED
/clean 90                                  # custom age threshold; orphans PROTECTED
/clean 30                                  # aggressive age; orphans PROTECTED
/clean orphans                             # delete only orphans (source missing), any age
/clean 180 --include-orphans               # age-based cleanup PLUS orphan deletion
```
> Orphan snapshots (snapshots whose `snapshot_of:` target no longer exists) are **protected by default** — they are often the only recovery path for a mistakenly-deleted file. Opt in to deletion explicitly. See §8 for the post-`/prune` safety warning.

### `/graph`
```
/graph                                     # no arguments — full rebuild
```

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
> Updates: filename (atomic via `mv`), all inbound wikilinks (7 patterns — best-effort across N files), `_graph.md` adjacency entry header, sector note Active Theses entry, `_Archive/Snapshots/` `snapshot_of:` fields, and `_hot.md` mentions. TICKER does not change. To undo: run `/rename TICKER "[OldName]"` (symmetric inverse). Pre-rename snapshot also created for content-only restore via `/rollback`.
>
> **Partial-failure recovery**: if any wikilink-rewrite Edit fails (file lock, malformed wikilink, etc.), `/rename` writes a `.rename_incomplete.TICKER` marker listing the failed files. **Every ticker-scoped skill on TICKER hard-blocks** until the marker clears. To repair: re-run `/rename TICKER "[same new name]"` — the no-op detection skips the already-completed mv and retries only the failed Edits. The marker is removed when all retries succeed.
>
> **Graph follow-up — use `/graph` (full), not `/graph last`**: `/rename` surgically rewrites the adjacency entry header in `_graph.md` for the renamed thesis itself, but does not re-validate headers for unchanged neighbor theses. If the rename was preceded by a manual `mv` of any other thesis (bypassing `/rename` for that one), `/graph last` would carry the stale baseline header forward for that neighbor. Running `/graph` (full rebuild) after `/rename` re-derives every header from current filenames on disk and eliminates this drift class. **Cost**: 30-60 seconds vs ~5 seconds for `/graph last`. **When to skip**: if you are 100% certain no thesis file has been manually renamed since the last `/graph` run, `/graph last` is sufficient.

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
4. Do your work (research, analysis, thesis building)
5. `/sync` again to propagate session work

### Weekly (or after heavy research)
- `/surface` or `/surface [sector you're focused on]`
- `/catalyst` to refresh the calendar
- `/lint TICKER` for any thesis you actively edited

### Monthly
- `/sync all` → `/graph` → `/lint` → `/prune` → `/clean` → `/surface` → `/catalyst` → `/graph last`
- Review `_hot.md` conviction changes and drift flags
- Conviction recalibration prompt for all high-conviction theses

### When prompted by events
| Event | Workflow |
|-------|---------|
| Earnings reported | `/ingest [URL]` → `/sync TICKER` → `/status` if conviction changes |
| Macro shock | `/scenario [event]` → `/status` for affected → `/sync` |
| New stock idea | `/thesis TICKER` → `/status draft→active` → `/stress-test` → `/sync` |
| Conviction flagged | `/status TICKER reaffirm [reason]` or investigate → `/status` change |
| Competitor news | `/ingest [URL]` → `/compare` affected tickers → `/sync` |
| Sector rotation | `/surface [sector]` → `/scenario` if macro-driven → `/compare` key players |

### When conventions change
- Update `CLAUDE.md` if you add new folders, change conventions, or shift research focus

---

## 14. How the Vault Stays Consistent

Understanding the infrastructure helps you trust the automation and diagnose issues.

### `_graph.md` — Dependency Map
Pre-computed wikilink index that `/sync` uses for fast, targeted propagation. Contains:
- **Thesis Adjacency Index**: each thesis's links to sectors, macro, cross-thesis, research
- **Reverse Indexes**: Macro → Theses, Sector → Theses (for reverse propagation)
- **Cross-Thesis Clusters**: bidirectional thesis-to-thesis connections
- **Orphan Research Notes**: research notes not linked from any thesis

Owned by `/graph` (three modes: full rebuild, `/graph last` incremental, `/graph [N]` catch-up). Most other skills do NOT write `_graph.md` directly.

**`.graph_invalidations` producers (actual, as implemented)**: only two skills append neighbor-thesis paths to `.graph_invalidations` — `/status` (closure branch, Step 7.6) and `/prune` (closure branch, Stage 4.5). Both do so to surface theses whose `cross-thesis:` wikilinks now point at a just-archived target. `/rollback` clears matching entries on a status-revert but does not append new ones.

**Other skills that edit thesis files** — `/sync`, `/status` (non-closure), `/stress-test`, `/scenario`, `/compare`, `/deepen`, `/thesis` — do not write `.graph_invalidations`. They instead rely on the file-mtime watermark: any thesis Edit advances its mtime past `_graph.md`'s `last_graph_write:`, so `/graph last`'s `find -newer` picks it up and re-extracts its adjacency on the next run.

**Skills that only create research notes** — `/brief`, `/surface` (unscoped/sector) — neither touch thesis mtimes nor write `.graph_invalidations`. The new research note IS added to `/graph`'s Orphan Research Notes list on the next `/graph` (any mode), because that list recomputes from a disk scan of `Research/*.md`. Cross-thesis research adjacency from a new note only surfaces after the first thesis Edit that wikilinks to it (e.g., a `/sync` run or manual link add). Run `/graph` (full) after a `/brief`- or `/surface`-heavy chain if you need the orphan list updated immediately.

**Exception**: `/rename` surgically updates the adjacency entry header (`### TICKER - [old_name]` → `### TICKER - [new_name]`) directly, since the rename is the only operation that changes how an existing thesis is identified in the graph. `/rename` does NOT advance `_graph.md`'s `last_graph_write:` watermark — that field belongs exclusively to `/graph` and advancing it would mask other pending changes from the next `/graph last` run.

### `_hot.md` — Session Context Cache
Persists context between sessions. Sections:
- **Active Research Thread**: what you're currently working on (auto-compressed history)
- **Latest Sync**: last sync summary
- **Sync Archive**: compressed older syncs (max 3)
- **Recent Conviction Changes**: conviction/status changes and drift flags
- **Open Questions**: unresolved questions across theses
- **Portfolio Snapshot**: high-level portfolio state

Updated by: `/sync`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/thesis`, `/deepen`, `/prune`, `/status`, `/rollback`, `/catalyst`, `/brief` (Active Research Thread + Open Questions only), `/rename` (free-text mentions of the old name). Hard-capped at 5,000 words (soft cap 4,000 — compression rules in `.claude/skills/_shared/hot-md-contract.md`).

> **Concurrency caveat**: the vault lock model permits two ticker-scoped skills on different tickers to run in parallel (e.g., `/deepen NVDA` in one session and `/brief AAPL` in another). Both will Edit `_hot.md` without coordination — the later writer's section edit silently wins. Treat Claudian as **single-session**: do not run multiple Claude Code sessions against the same vault concurrently. Sequential invocations inside one session are safe.

### `.graph_invalidations` — Deferred Graph Updates
Thesis closures (via `/status` closure branch or `/prune` closure branch) record **neighbor theses** in `.graph_invalidations` at vault root — theses whose `cross-thesis:` wikilinks now point at a just-archived target. Each line is a thesis path: `Theses/NVDA - Nvidia.md`. The closure itself never appears in the file (it's gone); only its surviving neighbors do.

All other thesis edits (from `/sync`, `/deepen`, `/stress-test`, `/scenario`, `/compare`, `/thesis`, non-closure `/status`) advance the edited thesis's file mtime past `_graph.md`'s `last_graph_write:` watermark, which `/graph last` picks up via `find -newer` without needing an explicit invalidation entry. `.graph_invalidations` exists specifically to catch the narrow case where a neighbor's adjacency is stale but its own file hasn't been edited (so its mtime is unchanged).

`/graph last` consumes the file:
1. Reads `.graph_invalidations` plus the watermark in `_graph.md`'s `last_graph_write:` frontmatter.
2. Re-extracts adjacency only for changed-since-watermark theses + invalidated neighbors.
3. Always rebuilds reverse indexes (Sector → Theses, Macro → Theses) from scratch to prevent drift.
4. Deletes `.graph_invalidations` on successful write.

This separation eliminates cross-skill graph contention. Multi-skill workflow chains (§3a-3q) accumulate invalidations (closures only) + mtime advances (all thesis edits) as they run; a single `/graph last` at the end applies them in one pass — there is no automatic "finalizer" mechanism, so you must run `/graph last` (or `/graph` for a full rebuild) explicitly.

If a chain ends without running `/graph`, `.graph_invalidations` persists across sessions until the next `/graph last` or `/graph` (full) consumes it. `/lint #38` flags stale invalidation files so they are not forgotten.

### `_catalyst.md` — Catalyst Calendar
Regenerated each time `/catalyst` runs. Timeline format: next 2 weeks (daily), weeks 3-4, months 2-3. Flags catalyst gaps and stale events.

### `.last_sync` — Watermark
Touched at the end of `/sync` (default mode) and `/sync all`. **NOT touched by `/sync TICKER`** — ticker-scoped runs preserve the watermark so the next default `/sync` still picks up unrelated files modified before the ticker run (advancing the watermark would silently mark them as already synced). Used by the next default `/sync` to detect which files changed since the last run via `find -newer .last_sync`.

If `.last_sync` is absent, the next `/sync` (any mode) creates an epoch placeholder (`touch -t 197001010000`) so `find -newer` matches every file — equivalent to `/sync all` in scope. Never touched by `/graph`.

### `_Archive/Snapshots/` — Version Control
Created automatically before destructive edits by: `/sync` (Tier A section edits), `/deepen`, `/status` (except draft→active), `/compare` (sector note changes), `/prune` (sector note changes + per-closure and per-upgrade thesis snapshots), `/catalyst` (overwrites previous calendar), `/rollback` (pre-rollback safety net), `/rename` (pre-rename), `/thesis` (manifest-only). Also houses crash-recovery **manifests**: `_sync-manifest`, `_status-manifest`, `_prune-manifest`, `_thesis-manifest`, `_stress-test-manifest`, `_compare-manifest`. Cleaned by `/clean`. Flagged for age by `/lint` (checks #41, #45, #47, #48, #49; prune manifests covered by #36). Prune manifests with `status: completed` are protected for 30 days (regret-recovery window) regardless of `/clean` age threshold.

### `.archive_ticker_registry.md` — Archive Ledger
Append-only ledger at vault root recording every thesis that transitions to `status: closed` and moves to `_Archive/`. Written by `/status` closure branch and `/prune` Stage 2. Consumed by `/thesis` Step 1.2 as one of four signals in the archive-collision detection (filename match, frontmatter ticker, snapshot trail, and this registry). Read-only for all other skills. `/lint #46` validates entries against current archive state.

### `.sync_all_fresh` — Full-Rebuild Marker
Single-file flag at vault root, written by `/sync all` at its final step. Read by `/graph` (any mode): if present, `/graph` forces a full rebuild regardless of arguments — meaning `/graph last` invoked after `/sync all` will auto-promote to a full rebuild. `/graph` clears the marker after a successful write. `/lint #38` flags the marker as stale if it has aged beyond a week (signals a missed `/graph` run).