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
> **Content-quality gate** (URL and PDF ingests block on failure; manual local files receive advisory logs):
> - **Structural**: ≥150 word body, absence of paywall/CAPTCHA/anti-bot sentinels, at least 2 of 4 expected body sections populated.
> - **Domain-specific by `source_type:`**:
>   - `earnings` — must contain period tokens (Q1/Q2/Q3/Q4/FY20XX) + 2+ currency figures + ticker/company reference
>   - `analyst-report` — must contain rating token (Buy/Sell/Hold/Overweight/Underweight/etc.) + price-target reference + ticker
>   - `news` — must contain ticker + dated event reference (absolute date or temporal token like "announced"/"reported")
>   - `deep-dive` — ≥500 words + ≥3 substantive sections (higher floor than generic)
>   - `web-clip`, `data` — skip domain checks (no vocabulary expected)
> - **Numerical integrity**: detects OCR corruption patterns (capital-O-as-zero, decimal-dropped currency like `$1 5B`, `II` as `11`).
> - **Title-URL consistency** (URL mode): first heading tokens must overlap ≥50% (Jaccard) with URL path slug — catches redirects to login/subscribe pages.
>
> Failed gate → research note deleted, source retained for re-ingest after resolving access or correcting `source_type:`. Blocks the most damaging silent-corruption path: paywalled or wrong-content URLs propagating into thesis Log entries via `/sync`.
>
> **Source-URL dedup** (Mode A URL, Mode B single-file): exact-match grep against existing `Research/*.md` `source:` frontmatter. Same-day match hard-blocks. Cross-day match prompts skip/re-ingest/cancel. Batch Mode C uses `_Inbox/processed/` filename-based guard instead.

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
> **Multi-signal archive-collision check**: before creating, checks for prior archived analysis via four signals (union):
> - **Signal A** — filename glob `_Archive/TICKER - *.md`
> - **Signal B** — frontmatter `ticker: TICKER` in any `_Archive/*.md` (catches renamed-then-archived theses)
> - **Signal C** — lookup in `.archive_ticker_registry.md` (auto-maintained registry of archival events)
> - **Signal D** — historical `snapshot_of:` references in `_Archive/Snapshots/`
>
> On any match → 4 explicit options: (a) `/rollback TICKER` to restore the prior thesis, (b) proceed with different name suffix to make dual-file state intentional, (c) proceed with proposed name accepting dual files (caveat in initial Log entry), (d) cancel.
>
> **New-sector handling**: if the thesis's `sector:` frontmatter doesn't resolve to any `Sectors/*.md` (via exact, normalized, or substring matching), Step 5 prompts: (a) create a minimal `Sectors/[sector].md` scaffold with this thesis as first Active Thesis, (b) proceed without sector update, (c) cancel to fix the sector value. No silent skip.

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
>
> **Missing section handling**: if the requested section doesn't exist in the thesis (e.g., manually deleted, template drift), skill aborts with options to (a) pick an existing section, (b) auto-detect, (c) manually restore the section from the template, or (d) `/lint TICKER` first. Never silently creates sections.

### Competitive comparison
```
/compare BESI vs AMAT            # two companies
/compare PANW NET CRWD           # three or more
```
> At least one ticker needs a thesis note. Missing tickers use web research (lighter comparison, no vault updates for them). For full-depth comparison, run `/thesis TICKER` first. Comparison updates thesis logs and sector note for tickers with existing theses. Run `/graph last` after to register the comparison research note.
>
> **Cross-sector atomicity**: when compared theses span multiple sectors, sector-note writes are all-or-nothing. Pre-snapshot every target sector → apply edits in sequence → if any sector write fails, roll back all prior successful sector edits from snapshots. Research note and thesis Logs are preserved through the rollback (they landed in earlier phases). `_compare-manifest` sidecar records the transaction for crash recovery.

### Generate a 1-page brief
```
/brief TICKER
```
> Read-only — does not modify the thesis. Creates a derivative `Research/` note. Warns if a previous brief exists (old version preserved).
>
> **Accumulation management**: briefs are not auto-archived by design — each is analytical content that may inform future `/deepen` or `/stress-test` sessions. Over an active ticker's lifetime, 10–20+ briefs accumulate in `/Research`. Recommended cadence: quarterly review via `find Research/ -name '*Investment Brief.md' -mtime +90` and manually `mv` stale ones to `_Archive/Briefs/` (create directory if absent).

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
> Two-pass triage (lightweight scan → deep read only exposed positions). Produces an impact matrix, second-order cascades, portfolio-level assessment, and recommended actions.
>
> **Classification approval gate (Phase 6.1.5)**: before any Log entries or research note write, `/scenario` pauses and presents the Major/Minor/Neutral classification for explicit review. Options: (a) approve and proceed, (b) promote specific Minor/Neutral theses to Major with user-provided rationale, (c) demote Major to Minor, (d) cancel (no files written). Catches LLM misclassification on either side — a Minor-classified thesis that's actually exposed (false negative) or a Major-classified thesis that isn't (false positive, reversible but noisy).
>
> After approval, appends Log entries to all Major-impact theses. `propagated_to:` on the research note is set only if ALL Major-impact Log appends succeed (atomicity rule).

### Reverse a previously-propagated scenario
```
/scenario reverse [[Research/2026-04-19 - Scenario - Fed cut]]
/scenario reverse Fed cut
```
> Use when a prior scenario propagation no longer applies (event proved transient, supply chain fears unrealized, etc.). Appends a `Scenario REVERSED` Log entry to every previously-affected thesis with a user-provided rationale. The original `Scenario` Log entries remain (Tier 2 append-only); the reverse entry is the corrective signal. The scenario research note is preserved as historical record. Use this instead of `/rollback`, which cannot undo `/scenario` (no snapshots created).
>
> **Archive-aware iteration**: R2 resolves each previously-affected ticker's current location. Live theses in `/Theses` receive the REVERSED Log entry. Theses archived since the scenario propagated are NOT modified (Tier 3 archive protection) — the archive-skip is instead documented in a `## Reversal Notes` section appended to the scenario research note body. Full audit preserved across both reopened and archived sides.

### Adversarial stress test
```
/stress-test TICKER
```
> Acts as a short seller. Scans for internal contradictions, builds an assumption fragility table, identifies research gaps, and proposes a falsifiable kill trigger. Flags for conviction reassessment but does NOT change conviction — that requires `/status`.
>
> **Rollback cascade support**: writes a `_stress-test-manifest` sidecar recording the Log entry text appended to the tested thesis. If the stress test was based on wrong input and the user wants to reverse it, `/rollback stress-test-YYYY-MM-DD-HHMMSS` → Step 2.5d cascade surfaces the Log entry for strikethrough review. Research note is preserved as historical record.

### Catalyst calendar
```
/catalyst
```
> Extracts every catalyst from every thesis (including monitoring-status). Enriches with web-searched earnings dates. Analyses catalyst clusters, gaps, and cross-thesis events. Saves/updates `_catalyst.md`. Pre-regenerate snapshot protects the prior calendar if web search fails mid-run — recover via `/rollback` batch `catalyst-YYYY-MM-DD-HHMMSS`.

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
> Mandatory confirmation before applying. Creates pre-change snapshot. Updates sector note and `_hot.md`. Checks for trigger conflicts. A `_status-manifest` sidecar records the transaction for `/rollback` cascade recovery (thesis + sector + `_hot.md`; archive move and invalidations for closures).

### Change status
```
/status TICKER status draft→active thesis meets quality bar
/status TICKER status active→monitoring awaiting Q3 earnings catalyst
/status TICKER status monitoring→active new catalyst emerged
/status TICKER status active→closed thesis invalidated by [reason]
```
> `draft→active` skips thesis snapshot (no analytical content changed; sector note still snapshots if an edit is planned). `active→closed` triggers archive flow — moves file to `_Archive/`, removes from sector note, appends to `.archive_ticker_registry.md`, writes `.graph_invalidations`. Graph cleanup is deferred to `/graph last` (run it after closure to remove the archived thesis from adjacency index, reverse indexes, and cross-thesis clusters).

### Reaffirm after drift
```
/status NVDA reaffirm earnings miss was one-time; competitive position unchanged
/status BESI reaffirm hybrid bonding thesis intact despite cycle weakness
```
> Lightweight operation — no frontmatter change, no snapshot. Resets the drift detection window so future `/sync` runs don't keep flagging the same pattern.
>
> **Always logs** — reaffirm is idempotent-safe and always appends a Log entry regardless of drift state, for audit-trail completeness. Format: `Conviction reaffirmed at [level] after [drift review | proactive review] — [rationale]`. "drift review" when a flag was active (and now cleared); "proactive review" when no flag was active (user reaffirming preemptively). Both preserve the canonical `"Conviction reaffirmed"` prefix that `/sync` drift detection uses as a window anchor.

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
/clean                                     # default: 180 days (orphans PROTECTED)
/clean 90                                  # custom threshold (orphans PROTECTED)
/clean 30                                  # aggressive (orphans PROTECTED)
/clean orphans                             # delete orphans only (any age), no age-based cleanup
/clean 180 --include-orphans               # age-based cleanup + delete orphans too
```
> **Orphan snapshots** (source file missing) default to PROTECTED — listed in the report but not deleted. Explicit opt-in required via `orphans` mode or `--include-orphans` flag. Fail-safe default because a deleted source may have been deleted in error, and the snapshot is the only recovery path.
>
> **Completed prune manifests** age out after a 30-day regret-recovery window past `completed_date:` — they are PROTECTED regardless of age threshold within that window. The regret-recovery window supports `/rollback` cascade-detection for neighbor Tier B Log entries from Stage 4.2 closures.

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

### Content caches & metadata files

#### `_hot.md` — Session Context Cache
Persists context between sessions. Canonical six-section schema:
- **Active Research Thread**: what you're currently working on (auto-compressed history)
- **Latest Sync**: last sync summary
- **Sync Archive**: compressed older syncs (max 3)
- **Recent Conviction Changes**: conviction/status changes and drift flags
- **Open Questions**: unresolved questions across theses
- **Portfolio Snapshot**: high-level portfolio state

Updated by 11 skills: `/sync`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/thesis`, `/deepen`, `/prune`, `/status`, `/rollback`, `/catalyst`. All writers follow the compression contract in `.claude/skills/_shared/hot-md-contract.md`:
- **Per-section budgets** (% of soft cap): Active Research Thread 30%, Latest Sync 15%, Sync Archive 20%, Recent Conviction Changes 15% (NEVER compressed), Open Questions 15%, Portfolio Snapshot 5%.
- **Soft cap 2,000 words / hard cap 2,500 words**. Over soft cap, compression trigger order: drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → warn in skill report. Over hard cap, skill aborts the `_hot.md` write (primary operation still succeeds).
- **Truncation markers forbidden** (`...` trailing bullets, `[compressed]`, `[truncated]`, unclosed formatting) — compression drops whole entries rather than truncating individual ones.
- **Same-ticker continuation**: same-ticker thread stays live (append dated line); different-ticker compresses outgoing thread to a single `*Previous:*` line.

`/lint #35` verifies the six-section schema (missing sections cause silent skill no-ops). `/lint #42` catches truncation-marker drift.

#### `_graph.md` — Vault Dependency Map
Owned exclusively by `/graph`. Three modes:
- **`/graph last`** (run after every `/sync`): true incremental — re-extracts adjacency only for thesis files changed since last graph write. Reverse indexes (Sector → Theses, Macro → Theses), cross-thesis clusters, and orphan list always rebuild from scratch in-memory. Cheap (skips ~30+ unchanged thesis reads) yet drift-free.
- **`/graph [N]`** (e.g., `/graph 7`): catch-up mode — same incremental logic, watermark = today − N days.
- **`/graph`** (no args): full rebuild (use after `/sync all` or disaster recovery).

**Precise ISO watermark**: frontmatter carries `last_graph_write: YYYY-MM-DDThh:mm:ssZ` in addition to `date: YYYY-MM-DD`. Change detection uses the ISO timestamp for second-precision — no edge cases at midnight rollovers. Legacy graph files without `last_graph_write:` fall back to `date:` at 00:00:00 UTC (conservative; next write upgrades the frontmatter).

Research skills (`/sync`, `/thesis`, `/compare`, `/scenario`, `/deepen`, etc.) do NOT write to `_graph.md` — they create content and remind you to run `/graph last` afterward. `/rename` is the sole exception (updates the adjacency entry header atomically with the filename mv).

#### `_catalyst.md` — Catalyst Calendar
Regenerated each time `/catalyst` runs. Timeline format: next 2 weeks (daily), weeks 3-4, months 2-3. Flags catalyst gaps and stale events. **Pre-regenerate snapshot** protects the prior calendar — if web search fails mid-run, recover via `/rollback` batch `catalyst-YYYY-MM-DD-HHMMSS`.

### Watermarks & state markers

#### `.last_sync` — Watermark
Touched at the end of every default `/sync` and `/sync all`. Used by the next `/sync` to detect changed files via `find -newer .last_sync`. **Never touched by `/sync TICKER`** (ticker-scoped mode preserves the baseline for the next default sync) and **never touched by `/graph`**.

**Idempotency keying**: `/sync`'s per-thesis idempotency check keys on **research-note wikilink presence** in the thesis Log — not today-date match. Once a research note has propagated to a thesis, that is terminal: subsequent `/sync` runs skip the propagation regardless of calendar day. Eliminates the midnight-rollover duplicate pattern where an 11:59pm `/sync` and a 12:01am re-run would both write Log entries.

#### `.sync_all_fresh` — Brute-force-sync marker
Touched at the end of `/sync all` only. Read by `/graph` at Watermark Resolution; if present, `/graph` forces a full rebuild regardless of mode and deletes the marker after a successful write. Closes the gap where `/sync all`'s two-pass triage leaves "No delta" thesis mtimes untouched (incremental `/graph last` would otherwise miss them). No user action — `/graph` manages lifecycle.

#### `.graph_invalidations` — Post-closure neighbor list
Written or appended by `/status` Step 7.6 (on `active→closed`) and `/prune` Stage 4.5 (on closure runs). Contains relative paths of neighbor thesis files that `[[wikilink]]`-referenced the just-archived thesis; their `cross-thesis:` adjacency entries need re-extraction to clear dangling references. Read by `/graph last`, folded into the changed-thesis bucket, and deleted only after a successful graph write. Dedup via `sort -u`; repeated closures safely accumulate.

#### `.rename_incomplete.TICKER` — Failed-rename repair markers (per-ticker)
Written by `/rename` Step 5.5 when one or more wikilink Edits fail after the file move completed. **Per-ticker filename** so multiple concurrent rename repairs coexist without corrupting each other.

Marker contains rename context (ticker, old_name, new_name, batch ID) and the failed-file list. Re-run `/rename TICKER "new_name"` to retry: repair-detection exception skips the already-completed mv and only re-attempts failed Edits. Marker shrinks monotonically across re-runs until empty, then auto-deletes.

**Cross-new_name guard**: if the marker exists with a different `new_name:` than the proposed re-run, `/rename` aborts with explicit options — prevents corruption where two different target names would overwrite each other's repair state.

`/lint #37` globs `.rename_incomplete.*` and surfaces each marker as Important until cleared. Pre-flight Read/Write probe (Step 3.5) prevents most occurrences by aborting BEFORE the mv when files are unreachable.

**Pre-flight marker check** in all ticker-scoped skills: `/status`, `/sync TICKER`, `/stress-test`, `/compare` (per-ticker), `/deepen`, `/brief`, `/surface TICKER`, `/thesis` hard-block on an active marker for their ticker. Vault-wide skills (`/sync`, `/sync all`, `/prune`, `/scenario`) hard-block on ANY active marker. Prevents propagation edits keyed to a mid-rename filename state. Exceptions: `/lint`, `/rollback`, `/graph` (read-only), `/rename` (owns the marker), `/ingest` (advisory only).

#### `.archive_ticker_registry.md` — Archive-ticker lookup table
Flat append-only log of thesis archival events, auto-maintained by `/status` Step 7.5b (on closure) and `/prune` Stage 2 (on closure runs). One line per archive event:
```
TICKER|archived_filename.md|YYYY-MM-DD|conviction_at_closure|closure_rationale
```
Consumed by `/thesis` Step 1.2 multi-signal archive-collision check (Signal C) to detect prior archived theses even when the archived filename no longer matches the `_Archive/TICKER - *.md` pattern (renamed-then-archived cases). `/lint #46` validates registry entries against current `_Archive/` state; stale entries (file no longer exists at listed path) are tolerated — `/thesis` verifies existence before treating a registry entry as a match.

#### `.vault-lock*` — Concurrency locks
Acquired at Step 0 of every skill that modifies vault state, per the contract in `.claude/skills/_shared/preflight.md`. Prevents concurrent skill invocations from racing on `_hot.md`, thesis Logs, sector notes, `_graph.md`, and marker files.

Lock scopes:
- **Vault-wide** (`.vault-lock`): `/sync all`, `/graph`, `/prune`, `/lint` full, `/clean`, `/catalyst`, `/ingest` (all modes), `/scenario`, `/surface` (unscoped/sector), `/rollback` restore mode
- **Ticker** (`.vault-lock.TICKER`): `/sync TICKER`, `/deepen`, `/stress-test`, `/status TICKER`, `/brief`, `/rename`, `/thesis`, `/surface TICKER`
- **Multi-ticker** (`.vault-lock.A+B+C` alphabetically sorted): `/compare`
- **Read-only** (`.vault-lock.readonly`): `/lint TICKER`, `/rollback` list mode

Each lock carries `pid:`, `skill:`, `scope:`, `started_at:`, `timeout_at:` in YAML frontmatter. Released via `trap` on skill exit (success, failure, interrupt). Stale lock detection: if `pid` is not running OR `timeout_at` < now, the lock is auto-reclaimed with a warning. `/lint #43` surfaces orphan locks whose PID no longer exists.

#### `.drift-config.md` (optional) — `/sync` drift detection tuning
Optional vault-root file for tuning `/sync` Step 3e conviction-drift heuristics. Format:
```yaml
---
window_size: 5                 # default 5; min 3, max 10
base_threshold: 3              # default 3 weakening entries in window fires drift
post_stress_threshold: 4       # default 4 (suppresses drift within 30 days of stress test)
post_stress_window_days: 30    # default 30
deepened_exclusion_days: 14    # default 14 (was 7 pre-tuning update)
---
```
Missing file → use defaults. Malformed → log warning and proceed with defaults.

**Default drift rules**: base 3/5 weakening triggers drift flag; if a `"Stress test"` Log entry exists within 30 days for the ticker, threshold raises to 4/5 (post-stress-test suppression). Deepened entries within 14 days of a Stress test are excluded from the window. The drift flag text reports threshold state: `⚠️ Conviction drift — 3/5 recent updates flagged headwinds (post-stress-test suppression: no)`.

### Snapshots & transaction manifests

Every multi-file skill uses the **skeleton → populate → flip** pattern to enable crash-recovery and cascade rollback. Manifests are written BEFORE any destructive mutation lands, populated incrementally, then flipped to `status: completed` at the end. An `in-progress` manifest is `/lint`'s signal that the skill crashed or the final flip silently missed.

#### `_Archive/Snapshots/` — Version Control
Created automatically before destructive edits by: `/sync` (Tier A section edits), `/deepen`, `/status` (except draft→active), `/compare` (sector note changes, per-sector batch IDs on cross-sector runs), `/prune` (sector note changes), `/catalyst` (pre-regenerate), `/rollback` (pre-rollback safety net), `/rename` (pre-rename snapshot). Cleaned by `/clean`; non-snapshot artifacts (manifests) are skipped by age-based cleanup and handled per artifact type.

**Batch ID format**: `<trigger>-YYYY-MM-DD-HHMMSS` with 6-digit second-precision. `/rollback` cascade detection matches snapshots by batch ID prefix.

**Orphan protection**: snapshots whose `snapshot_of:` source file is missing default to PROTECTED by `/clean`. Explicit opt-in via `/clean orphans` (orphans only, any age) or `/clean [days] --include-orphans` (age-based + orphans). Fail-safe default because a deleted source may have been removed in error, and the snapshot is the only recovery path.

#### `_prune-manifest (prune-*).md`
Written by `/prune` Stage 1.5 before any closure/upgrade lands. Records intended closures, upgrades, affected sector notes, and Stage 4.2 neighbor targets. Flipped to `status: completed` + `completed_date:` at Stage 5.

**30-day regret-recovery window**: the manifest is retained for 30 days after `completed_date:`. Within this window, `/rollback` cascade-detection can surface Tier B "Cross-thesis closure" Log entries on neighbor theses (which have no per-neighbor snapshots) for strikethrough review. `/lint #36` treats as Pass within 30 days, Nice to Have after. `/clean` removes manifests once both the age threshold AND the 30-day floor are satisfied — a user running `/clean 10` does NOT delete a 15-day-old completed manifest.

#### `_sync-manifest (sync-*).md`
Two-phase write. Step 2.9 (new) writes the skeleton with `status: in-progress` BEFORE any Tier A snapshot or Tier B Log append lands — skeleton write failure hard-aborts the sync pre-mutation, preventing any silent audit gap. Steps 3–6 append accumulator entries (Tier A snapshots, Tier B Log appends on neighbor theses without snapshots, sector/macro edits, source research notes) incrementally. Step 7.5 flips status to `completed` + verifies the flip landed.

Consumed by `/rollback` Step 2.5b cascade detection: when the user selects a pre-sync snapshot, the manifest's Tier B Log entries are surfaced for review with options (surface-only, auto-strikethrough, manual). Without the manifest, Tier B appends would persist as orphan audit entries after rollback.

`/lint #41` classifies by `status:`: `in-progress` → Important (crash or flip failure), `completed` → age-based tiers (90+ days Nice to Have, 180+ days Important).

#### `_compare-manifest (compare-*).md`
Written by `/compare` Phase 5.5c after the cross-sector atomic transaction. Records sectors successfully edited, sectors rolled back (if atomicity fired), thesis Log append outcomes, and the research note path. `status: completed | rolled-back`. `/lint #45` handles aging.

#### `_stress-test-manifest (stress-test-*).md`
Written by `/stress-test` Phase 4.6 recording the Log entry text appended to the tested thesis. Enables `/rollback` Step 2.5d cascade for strikethrough annotation of the append-only Log entry. Research note at `Research/` is preserved (same policy as scenario and compare research notes). `/lint #47` handles aging + status.

#### `_status-manifest (status-*).md`
Two-phase write matching `/sync`. Step 3.0.5 writes skeleton before any file modification; records intended thesis frontmatter change, sector note edit, archive move (closure only), graph invalidations, `_hot.md` update. Step 7.9 flips status. `/rollback` Step 2.5e cascade offers (a) thesis-only restore or (b) full transaction restore (thesis + sector + un-archive + clear invalidations). Reaffirm flow does NOT write a manifest (no multi-file transaction). `/lint #48` handles aging + in-progress detection.

---

## 15. Architecture Notes & Troubleshooting

### `/graph last` cost & precision

| Vault state                       | `/graph last` work                                                       |
| --------------------------------- | ------------------------------------------------------------------------ |
| No files changed since last graph | Skip — zero reads                                                        |
| 1–5 thesis files changed          | Re-extract those theses + read 19 sector/macro files for reverse indexes |
| 30+ thesis files changed          | Approaches the cost of a full rebuild                                    |

**Watermark precision is daily** (`_graph.md` frontmatter `date:` is YYYY-MM-DD). Running `/graph last` twice the same day re-processes files modified between runs — output is idempotent (correct, just wasted compute).

### Troubleshooting

Grouped by symptom category. Each row: observed symptom → likely cause → fix.

#### Vault locks & concurrency

| Symptom | Likely cause | Fix |
|---|---|---|
| Any skill aborts with `❌ Another skill is running — vault lock held` | `.vault-lock*` file at vault root held by another skill (or a crashed process) | Wait for the holder to finish. If holder PID is not running (`kill -0 [pid]` errors), remove lock: `rm [lockfile_path]`. `/lint #43` also surfaces orphan locks. |
| `/lint #43` flags orphan lock | Skill crashed without releasing the lock (trap did not fire) | `rm` the flagged lockfile. Safe when the listed PID is no longer running. |

#### Rename repair state

| Symptom | Likely cause | Fix |
|---|---|---|
| Ticker-scoped skill aborts with `❌ Rename repair incomplete for TICKER` | `.rename_incomplete.TICKER` present from a failed `/rename` | Complete repair: `/rename TICKER "[new_name from marker]"` (retries failed Edits). OR accept broken wikilinks: `rm .rename_incomplete.TICKER` then re-run target skill. |
| `/lint #37` — marker present | Same as above. Multiple markers = multiple in-flight repairs; each independent | Run `/rename` for each marker's ticker to clear. |
| `/rename` aborts with `In-flight rename conflict` | Marker exists with a different `new_name:` than the proposed re-run | Finish prior rename with the marker's `new_name:`, OR manually resolve listed files + `rm` marker, OR accept loss of repair state (manually fix listed files first to avoid broken wikilinks). |
| `/rename` rejects name with `❌ Invalid name: [reason]` | Name sanitization: disallowed char (`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`), leading dot, reserved name, >100 chars | Use allowed chars only: `[a-zA-Z0-9 \-_.,'&()]`. See the rejection message for the specific rule. |

#### Graph / sync state markers

| Symptom | Likely cause | Fix |
|---|---|---|
| `/lint` flags graph staleness (>7 days) | `/graph last` hasn't run after recent `/sync` runs | `/graph 7` (or N days behind) to catch up. |
| `/lint` flags graph staleness (>30 days) | Significant gap | `/graph` (full rebuild). |
| `/graph last` reports "Graph is up to date" but you just edited files | Legacy graph file without precise ISO watermark, OR files modified before midnight of graph's `date:` (rare) | Run `/graph` once to upgrade frontmatter to `last_graph_write:` ISO format; future runs use second-precision. |
| `/lint #38` — `.sync_all_fresh` >24h old | `/sync all` ran but `/graph` hasn't consumed the marker | `/graph` (full rebuild) — marker self-cleans on success. |
| `/lint #38` — `.graph_invalidations` >24h old | Closures written but `/graph last` hasn't consumed the list | `/graph last` — file consumed and deleted on success. |
| `/sync TICKER` works but default `/sync` misses propagation | Reopened thesis not yet in `_graph.md` | `/graph last` registers the restored adjacency. |
| `/graph last` announces `.sync_all_fresh marker detected` | Normal — signals forced full rebuild | No action; marker self-cleans. |

#### Thesis lifecycle (close / reopen / rename)

| Symptom | Likely cause | Fix |
|---|---|---|
| `/lint #33` — closed-thesis file still in `Theses/` | Failed `mv` from `/status active→closed` or `/prune` | Complete archive: `mv "Theses/[file]" "_Archive/[file]"` → `/graph last`. OR reopen: `/status TICKER status closed→active [rationale]` → `/sync TICKER` → `/graph last`. |
| `/thesis TICKER` prompts about archived thesis | Multi-signal archive-collision check matched via filename / frontmatter ticker / archive registry / snapshot trail | Inspect reported archive. Options: (a) `/rollback TICKER` to restore, (b) different name suffix for dual-file, (c) accept dual-file state, (d) cancel. |
| `/thesis TICKER` prompts about missing sector note | Sector's `match_confidence: none` | (a) Create `Sectors/[value].md` scaffold with this thesis as first entry, (b) proceed without sector update, (c) cancel to fix the sector value. |
| `/rollback` of a closed thesis surfaces "Intervening Log entries detected" | Step 6.2.5 scan found post-closure Log entries on neighbor theses | (a) surface-only, (b) auto-strikethrough `Cross-thesis closure:` premise entries, (c) auto-strikethrough all, (d) skip. |
| `/deepen TICKER [section]` aborts with "Section not found" | Target section doesn't exist in the thesis | Pick an existing section (listed in error), OR restore the missing section from the template, OR `/deepen TICKER` (auto-detect). |
| `/lint #32` — research note `ticker:` matches no thesis | Research deposited before thesis, or for an archived thesis | `/thesis [TICKER]` to create, OR edit research frontmatter, OR accept as orphan. |

#### Content quality — `/ingest`

| Symptom | Likely cause | Fix |
|---|---|---|
| `Content-quality gate FAILED — #5 body word count` or #6 sentinel | Fetch returned paywall, CAPTCHA, anti-bot, or empty page | Resolve access (login, alternate URL, archive.org, manual download). Re-run `/ingest`. Research note was auto-deleted; source retained for retry. |
| `#8/#9/#10/#11 domain signature` failed | source_type-specific vocabulary missing (earnings period tokens, analyst rating tokens, news dated event, deep-dive word count) | Either content is off-topic → re-ingest after resolving, OR `source_type` is wrong → edit to correct type. |
| `#12 numerical integrity FAILED` | OCR-style corruption (capital-O as zero, decimal-dropped currency, `II` as `11`) | Re-extract PDF with a cleaner tool (preview.app, pdftotext), OR manually create `.md` from the source. |
| `#13 title-URL mismatch` | First heading tokens have <50% Jaccard overlap with URL path slug | Fetch likely redirected to login/subscribe/error page. Re-ingest after resolving access (archive.org cache if paywalled). |
| `⚠️ Source already ingested today` (hard block) | Same-day URL dedup matched an existing research note | Delete the existing note first if you genuinely want to re-process: `rm "Research/[matched-note].md"` then re-run. |
| `⚠️ Source previously ingested` (cross-day prompt) | URL matches a prior ingest from an earlier day | (a) skip and use existing, (b) re-ingest as new dated note (coexists cleanly), (c) cancel. |

#### Manifest lifecycle (sync / status / prune / compare / stress-test)

| Symptom | Likely cause | Fix |
|---|---|---|
| `/lint #36` — prune manifest `status: in-progress` | Either (1) genuinely crashed prune, OR (2) successful prune whose Stage 5 flip silently missed | Disambiguate FIRST: do manifest's Intended Closures live in `_Archive/` with `status: closed`? Yes → cause (2); edit manifest to `status: completed` and `rm` (do NOT rollback — destroys valid work). No → cause (1); `/rollback [ticker from manifest]` → `(pre-prune)` snapshot → cascade (a). `/prune` report's "flip verification failed" is the cheap tell for cause (2). |
| `/lint #41` / `#48` — sync/status manifest `status: in-progress` | Flip failed at end of run OR skill crashed mid-run OR `/lint` ran during active run | Inspect body for landed stages. If skill completed and only flip failed, manually edit to `status: completed`. If incomplete, `/rollback [batch]` → option (b) cascade restore. |
| `/lint #47` — stress-test manifest `status: in-progress` | Rare — /stress-test writes manifest as completed in one step | Verify research note + thesis Log entry exist. If yes, manually edit to `completed`. If either missing, re-run /stress-test. |
| `/lint #36/41/47/48` — manifest `status: completed` and stale | Aging out past its useful window | For prune: safe to delete after 30-day regret window. For sync/status/compare/stress-test: safe after 90 days (Nice to Have) or 180 days (Important). `rm` the flagged file. |
| Completed prune manifest persists days after prune | 30-day regret-recovery retention — by design | `/rollback` cascade-detection within this window surfaces Tier B neighbor Log entries. After day 30, `/clean` removes. |
| `/rollback` on a sync/compare batch surfaces Tier B Log entries | Cross-thesis Log appends are Tier B (no per-file snapshot); cascade detection surfaces them for review | Per-entry decision: (1) leave as historical, (2) strikethrough (`~~entry~~ → Reverted YYYY-MM-DD: ...`), (3) manually delete (only for clearly erroneous entries). Option (b) in the cascade prompt auto-applies (2). |
| `/rollback` on a stress-test batch surfaces the Log entry | Step 2.5d cascade | (b) cascade + strikethrough rewrites as `~~entry~~ → Reverted YYYY-MM-DD: stress-test judged invalid`. Research note preserved. |
| `/rollback` on a status batch offers "thesis-only" vs "full transaction" | Step 2.5e cascade | (b) Full restores thesis + sector + un-archives + clears invalidations. (a) thesis-only restores frontmatter only. |
| `/compare` aborts with "Sector note write failed — rolled back" | Cross-sector atomicity fired | Research note and thesis Logs preserved. Resolve sector file issue (lock, permission), then re-run `/compare`. |

#### Propagation retries

| Symptom | Likely cause | Fix |
|---|---|---|
| `/scenario` / `/stress-test` / `/compare` report "Log appends — failed" AND "`propagated_to:` omitted" | Atomicity rule correctly omitted `propagated_to:` so `/sync` retries the failed target | `/sync` (default) — file-direct fallback resolves failed targets via research note's frontmatter and retries. Then `/graph last`. |
| `/lint #39` flags `synthesis`/`brief` missing `propagated_to: []` | Producer didn't emit the terminal-skip signal; next `/sync` would spam 10+ theses | Add `propagated_to: []` to frontmatter immediately. Investigate the producer skill. |
| `/lint #39` flags `scenario`/`stress-test`/`comparison` missing `propagated_to:` (post-spec) | Either atomicity rule fired (expected) OR producer drift | Check referenced theses' Logs. If entries exist on all expected tickers → manually backfill `propagated_to: [TICKERS]`. If missing → `/sync` to trigger retry. |
| `/lint #39` pre-spec note (< 2026-04-19) missing `propagated_to:` | Note created before producer-side contract was introduced | Optional backfill with resolved-ticker list to suppress date-stamped catch-up entries on next `/sync`. Otherwise accept a single catch-up entry per affected thesis. |

#### Drift detection

| Symptom | Likely cause | Fix |
|---|---|---|
| `/sync` reports drift despite recent stress test | Suppression didn't apply (e.g., stress test >30 days old, or no Stress test Log entry) | If genuine signal → `/status TICKER reaffirm` to acknowledge. To customize thresholds, edit `.drift-config.md`. |
| Drift signal never fires despite obvious deterioration | Post-stress-test suppression raised threshold to 4/5 within the 30-day window | Expected. For base sensitivity, edit `.drift-config.md`: `post_stress_threshold: 3` AND `post_stress_window_days: 0`. |

#### `_hot.md` schema / compression

| Symptom | Likely cause | Fix |
|---|---|---|
| `/lint #35` — `_hot.md` missing a required section | Skill-specific Edit silently no-oped, OR manual edit removed the heading | Add the missing `##` heading with `- _pending_` bullet. Or delete `_hot.md` and let next `/sync` auto-create the full schema. |
| `/lint #42` — truncation markers in `_hot.md` | Manual edit or buggy skill left `...`, `[compressed]`, `[truncated]`, or unclosed formatting | Manually remove markers. Investigate: if a skill produced them, check compression-contract compliance. |
| `_hot.md` exceeds 2,500 words after a skill runs | Hard cap reached; skill aborted the `_hot.md` update (primary operation still succeeded) | Manually trim Sync Archive or `*Previous:*` lines. `/lint #35` + `#42` diagnose drift. |

#### Snapshot management

| Symptom | Likely cause | Fix |
|---|---|---|
| `/clean` reports "Orphan snapshots: N protected" | Snapshots whose source file is missing default to PROTECTED (fail-safe) | Investigate (was source deleted in error?). To delete: `/clean orphans` (orphans only, any age) or `/clean [days] --include-orphans`. |
| `/catalyst` produced a partial calendar (web search failed) | Pre-regenerate snapshot retained the prior calendar | `/rollback` → select `(pre-catalyst YYYY-MM-DD-HHMMSS)` snapshot. Re-run `/catalyst` when web access is resolved. |
| `/lint #16` — stale snapshots (>180 days) | Normal aging; snapshots accumulate over time | `/clean` with default threshold (180 days). Active safety nets (source modified after snapshot) are auto-protected. |

