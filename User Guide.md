# User Guide — Claude Code + Obsidian for Investment Research

> Your vault has **39 theses**, **132 research notes**, **13 sector notes**, and **6 macro notes**. This guide covers every skill, every workflow, and every high-value manual prompt. Ordered by how often you'll use it — start at the top.

> **Deep infrastructure details** (manifest internals, lock semantics, watermark mechanics) live in [[INFRASTRUCTURE.md]]. This guide is the user-facing surface.

---

## 0. First Run

If this is a brand new vault (no prior `/sync` runs), run this bootstrap sequence:

```
/sync                            # creates _hot.md + .last_sync, reads all vault files
/graph last                      # creates _graph.md from vault state (falls back to full rebuild on first run)
```

After bootstrap, all skills work. Without it:
- Scoped `/surface` (ticker or sector) requires `_graph.md` — blocks if missing
- `/prune` pre-flight unsynced-research check has no `.last_sync` baseline
- Skills that update `_hot.md` auto-create it (CLAUDE.md rule #9), but `/sync` produces a richer initial version

> `/sync TICKER` does NOT require `_graph.md` — safe to run before bootstrap. `/sync` on an existing vault reads everything on first run (equivalent to `/sync all`) to establish the watermark baseline.

---

## 1. Mental Model

The vault is not a filing cabinet. It is a **synthesis engine** optimized for generating non-consensus qualitative insights on equity investments. Every skill, every prompt, every file layout serves one question:

> **"What does my research imply that the market isn't pricing?"**

### Three meta-operations

Every skill maps to one of three jobs:

| Meta-op | Skills | What it does |
|---|---|---|
| **Absorb** | `/ingest` | Turn raw external content into structured vault notes |
| **Synthesize** | `/thesis`, `/deepen`, `/stress-test`, `/compare`, `/scenario`, `/surface`, `/brief`, `/catalyst` | Transform vault content into sharper conviction |
| **Decide** | `/status`, `/prune` | Commit analytical conclusions to conviction and status |

Plus one support layer:

| Meta-op | Skills | What it does |
|---|---|---|
| **Reconcile** | `/sync`, `/graph`, `/lint`, `/clean`, `/rename`, `/rollback` | Keep the vault internally consistent |

### The synthesis flywheel

```
Absorb  →  Reconcile  →  Synthesize  →  Decide  →  Reconcile
 ingest     sync+graph    think/write     status      sync+graph
```

You never skip the Reconcile step between Absorb and Synthesize. Insights that live in `_Inbox/` or in a newly-created Research note but haven't propagated to theses yet are **not yet part of your mental model** — they haven't been priced into conviction.

### What the vault optimizes for (and what it doesn't)

**Optimizes for:**
- Non-consensus qualitative insights — product, management, competitive dynamics, business model transitions
- Durable synthesis across sectors, macros, and time
- Adversarial self-correction (stress tests, drift detection, pruning weak theses)

**Does NOT optimize for:**
- Spot valuation snapshots — use a terminal
- Quantitative backtesting — use Python
- News aggregation — use an RSS reader and ingest only what merits a research note
- Real-time anything — the vault is a slow, deliberate thinking tool

### Three session archetypes

Most sessions fall into one of three shapes (see §3):
- **A. React** — new information arrived; process it, propagate it, decide if conviction moves
- **B. Deepen/Challenge** — existing thesis needs strengthening or adversarial testing
- **C. Portfolio view** — zoom out: find gaps, clusters, opportunities, or prune dead weight

---

## 2. The Core Loop

Every session follows the same rhythm: **deposit → ingest → sync → graph**.

```
_Inbox/ drop  →  /ingest  →  /sync  →  /graph last  →  work  →  /sync  →  /graph last
```

| Step | What happens | Time |
|------|-------------|------|
| Drop raw content into `_Inbox/` | Web clips, PDFs, CSVs — any format | Between sessions |
| `/ingest` | Transforms `_Inbox/` into structured Research notes with wikilinks | ~2 min |
| `/sync` | Propagates insights to theses, sectors, macro notes, `_hot.md`. Does NOT touch `_graph.md`. | ~3 min |
| `/graph last` | Reconciles `_graph.md` against changed files (incremental, cheap) | ~10 sec |
| Work | Research, thesis building, conviction changes | Variable |
| `/sync` → `/graph last` | Propagate session work, refresh dependency map | ~3 min |

> **Why `/graph last` after every `/sync`**: research skills never write to `_graph.md`. `/graph last` is the cheap finalizer that keeps the dependency map current. Skip it and scoped `/surface`, `/lint` graph checks, and conviction-drift diagnostics silently degrade.

---

## 3. Session Archetypes

Seven patterns cover the vast majority of sessions. Pick the archetype, run the chain.

### A. React — New information arrived

**Trigger**: earnings hit, macro shock, news item, Deep Research delivery, competitor event.

**Minimal chain**:
```
/ingest [URL or file]            # or just /ingest for everything in _Inbox/
/sync
/graph last
```

**If the content changes conviction**:
```
/status TICKER conviction old→new [transmission channel from source]
```

**If the content is ambiguous — stress-test before deciding**:
```
/stress-test TICKER
/sync TICKER
/graph last
```

**Macro variant** — event affects multiple positions:
```
/scenario [event description with quantitative parameters]
/status TICKER conviction old→new [per-thesis transmission channel]
/sync
/graph last
```

> The scenario classification approval gate lets you promote/demote any thesis before Log entries land. Use it — LLMs misclassify exposure in both directions.

### B. Build or Strengthen — New or weak thesis

**New coverage from scratch**:
```
/thesis TICKER                   # searches vault first, then web; creates all 13 sections
/status TICKER status draft→active [rationale]
/stress-test TICKER              # immediately, while thesis is fresh
/sync TICKER
/graph last
```

**Optional extensions**:
- `/compare TICKER vs COMPETITOR` for competitive context before `/sync`
- `/deepen TICKER [section]` to fill gaps the stress test identified

**Strengthen an existing thesis**:
```
/deepen TICKER                   # auto-detects weakest section; or name it explicitly
/sync TICKER
/graph last
```

**Adversarial pressure test** (before a major decision or allocation):
```
/stress-test TICKER
/deepen TICKER [weakest section surfaced by stress test]
/sync TICKER
/graph last
```

### C. Challenge — Test conviction

**Drift response** (`/sync` flagged `⚠️ Conviction drift`):

Path A — reaffirm (you've reviewed, conviction holds):
```
/status TICKER reaffirm [why the drift signal is noise]
```

Path B — investigate, then decide:
```
/stress-test TICKER              # or /deepen TICKER [drifted section]
/sync TICKER
/graph last
/status TICKER conviction old→new [rationale from investigation]
```

**Competitive reassessment**:
```
/compare A vs B                  # or A vs B vs C
/status TICKER conviction old→new [competitive insight]
/sync
/graph last
```

**Post-event review** (after a catalyst you previously modelled):
```
/scenario reverse [original scenario note]    # if the event proved transient
```
Then check drift — if a thesis you flagged as exposed has continued deteriorating, the scenario was right but you didn't act; re-surface with `/stress-test`.

### D. Portfolio view — Zoom out

**Find opportunities and gaps**:
```
/surface                         # full vault — blind spots, correlations, research gaps
/surface [sector]                # sector-scoped, faster
/surface TICKER                  # one thesis + adjacencies
```

**See what's coming**:
```
/catalyst                        # regenerates _catalyst.md with day-by-day calendar
```

**Prune crowded portfolio**:
```
/sync                            # propagate first — prune warns otherwise
/graph last
/prune                           # or /prune [sector/flag]; approve changes inline
/graph last                      # MANDATORY: consume invalidations before next scoped /surface
/surface                         # reallocate attention to opportunities
/graph last
```

**Sector deep-dive**:
```
# If sector note doesn't exist, create it manually (prompt in §6.4)
/graph last                      # register new sector in reverse index
/surface [sector]
/compare [key players]
/sync
/graph last
```

### E. Decide — Commit conclusions

**Conviction change**:
```
/status TICKER conviction medium→low [specific reason]
```

**Status transitions**:
```
/status TICKER status draft→active [rationale]
/status TICKER status active→monitoring [awaiting catalyst]
/status TICKER status active→closed [what invalidated the thesis]
```

**Pre-meeting prep**:
```
/brief TICKER                    # 1-page memo; read-only
```
For adversarial prep:
```
/stress-test TICKER              # identify weakest points to anticipate pushback
/sync TICKER                     # skip only if stress test returned "thesis survives" with zero 🔴 findings
/brief TICKER
/graph last
```

### F. Recover — Undo a bad operation

**Undo a sync**:
```
/rollback TICKER                 # select (pre-sync) snapshot; cascade detection offers atomic multi-file restore
/sync TICKER                     # re-propagate from restored state
/graph last
```

**Undo a closure** (reopen archived thesis):
```
/rollback TICKER                 # recreates file at original path; archived copy moves to Snapshots
# Check restored status: frontmatter — skip /status if already active
/sync TICKER
/graph last                      # CRITICAL for recreated-file rollbacks; without it, file is invisible to graph-assisted lookups
```

**Undo a conviction change**:
```
/rollback TICKER                 # select (pre-status) snapshot
```

**Undo a `/scenario` propagation** (scenarios don't snapshot — use reverse mode):
```
/scenario reverse [scenario-research-note]
/graph last                      # no /sync needed — append-only Log entries
```

### G. Maintain — Monthly (or when vault feels out of sync)

```
/sync all                        # full brute-force propagation
/graph                           # full rebuild (follows /sync all)
/lint                            # 40-check audit
/prune                           # evaluate all theses
/graph last                      # consume .graph_invalidations from closures — MANDATORY before next scoped read
/clean                           # delete old snapshots
/surface                         # find new opportunities
/catalyst                        # refresh calendar
/graph last                      # incremental refresh after /surface + /catalyst
```

> Run in this order. `/sync all` before `/graph` (full) because sync may change links. `/lint` after `/graph` because lint checks graph health. `/prune` after `/lint` because lint flags staleness. The mid-chain `/graph last` after `/prune` is non-negotiable — it consumes `.graph_invalidations` and excludes archived theses from reverse indexes; without it, scoped `/surface [sector]` would abort with scope-set validation.

---

## 4. By Goal — Decision Tree

When you don't know which archetype fits, trace the tree.

### "I want to capture new information"
- **URL / PDF / file** → `/ingest [source]` → `/sync` → `/graph last`
- **YouTube video** → Gemini prompt (§6.1) → save to `_Inbox/` → `/ingest` → `/sync` → `/graph last`
- **My own research / notes** → write directly to `Research/` → `/sync` → `/graph last`

### "I want to understand something better"
- **New company** → `/thesis TICKER`
- **Existing thesis has a weak section** → `/deepen TICKER [section]`
- **Historical analogy** → manual prompt (§6.2.6)
- **TAM reality check** → manual prompt (§6.2.8)
- **Management quality** → manual prompt (§6.2.7)
- **Teach me a topic** → manual prompt (§6.2.5)

### "I want to pressure-test my thinking"
- **One thesis** → `/stress-test TICKER`
- **Cross-thesis contradictions** → manual prompt (§6.3.5)
- **What is priced in** → manual prompt (§6.3.2)
- **Invert a thesis** → manual prompt (§6.3.4)

### "I want to see the portfolio"
- **New opportunities** → `/surface`
- **One sector** → `/surface [sector]`
- **What's coming up** → `/catalyst`
- **Concentration risk** → manual prompt (§6.4.3)
- **Blind spots** → manual prompt (§6.4.2)
- **Value chain map** → manual prompt (§6.5.3)

### "I want to compare or decide"
- **Compare companies** → `/compare A vs B` (or `A vs B vs C`)
- **Change conviction** → `/status TICKER conviction old→new [reason]`
- **Open/close/monitor** → `/status TICKER status old→new [reason]`
- **Reaffirm after drift** → `/status TICKER reaffirm [reason]`
- **Prune weak positions** → `/prune` (or scoped variants)

### "I want to model a what-if"
- **Macro event** → `/scenario [event description]`
- **Withdraw a scenario** → `/scenario reverse [scenario-note]`

### "I want to prepare or present"
- **1-page memo** → `/brief TICKER`
- **Adversarial prep** → `/stress-test` → `/sync TICKER` → `/brief TICKER`
- **Relationship map canvas** → manual prompt (§10)
- **Evolution timeline canvas** → manual prompt (§10)

### "Something broke"
- **Undo anything** → `/rollback` (see §3.F)
- **Graph looks wrong** → `/graph` (full rebuild)
- **Vault feels stale** → §3.G Monthly chain
- **Specific symptom** → §12 Troubleshooting

---

## 5. Skill Reference

Every skill, every argument form. Paired with what it creates, what it modifies, and what to run next.

> **Metadata ownership**: only `/graph` and `/rename` write to `_graph.md`. Every other skill is content-only. Run `/graph last` after any skill below to refresh the dependency map.

### 5.1 Absorb

#### `/ingest`
```
/ingest                                    # batch: everything in _Inbox/
/ingest https://example.com/article        # single URL
/ingest /path/to/file.pdf                  # local file (PDF, MD, CSV, TXT)
```
**Creates**: Research note(s). **Modifies**: — . **Follow-up**: `/sync` → `/graph last`.

Content-quality gate blocks paywall/CAPTCHA/anti-bot returns, wrong-source-type content, OCR-corrupted numbers, and redirects. Failed gate → research note deleted, source retained for re-ingest. Source-URL dedup: same-day exact-match hard blocks; cross-day match prompts skip/re-ingest/cancel.

### 5.2 Synthesize

#### `/thesis`
```
/thesis NVDA                               # company name resolved automatically
```
**Creates**: Thesis note (draft). **Modifies**: Sector note, `_hot.md`. **Follow-up**: `/status draft→active` → `/stress-test` → `/sync` → `/graph last`.

Multi-signal archive-collision check (filename glob + frontmatter ticker + registry + snapshot trail) surfaces prior archived theses. New-sector handling prompts scaffold creation rather than silent skip.

#### `/deepen`
```
/deepen NVDA                               # auto-detects weakest section
/deepen NVDA [section name]                # explicit section
```
Sections: Outstanding Questions, Key Non-consensus Insights, Industry Context, Business Model, Bull Case, Bear Case, Key Metrics, Catalysts, Risks, Conviction Triggers.

**Creates**: Snapshot + optional Research note. **Modifies**: Thesis (target section + log), `_hot.md`. **Follow-up**: `/sync TICKER` → `/graph last`.

Missing-section handling aborts with options rather than silently creating — preserves template integrity.

#### `/stress-test`
```
/stress-test NVDA                          # single ticker
```
**Creates**: Research note (stress test). **Modifies**: Thesis log, `_hot.md`. **Follow-up**: `/status` (if conviction change) → `/sync` → `/graph last`.

Acts as a skeptical short-seller. Builds assumption-fragility table, identifies research gaps, proposes falsifiable kill trigger. Flags for reassessment but does NOT change conviction — that requires `/status`.

#### `/compare`
```
/compare BESI vs AMAT                      # two companies
/compare PANW NET CRWD                     # three or more
```
**Creates**: Research note (comparison). **Modifies**: Thesis logs, Sector note, `_hot.md`. **Follow-up**: `/sync` → `/graph last`.

At least one ticker must have a thesis. Missing tickers use web research (lighter). Cross-sector atomicity: sector-note writes are all-or-nothing.

#### `/scenario`
```
/scenario Fed cuts 150bps by year-end       # forward mode
/scenario oil spikes to $150
/scenario reverse [scenario-research-note]  # withdraw a prior propagation
/scenario reverse Fed cut                   # partial-name disambiguator
```
**Creates**: Research note (scenario; reverse mode creates no new note). **Modifies**: Thesis logs (major-impact tickers), `_hot.md`. **Follow-up**: forward → `/status` → `/sync` → `/graph last`; reverse → `/graph last` only.

Classification approval gate (Phase 6.1.5) pauses before Log entries to let you promote/demote. Reverse mode appends `Scenario REVERSED` Log entries (Tier 2 append-only, original entries remain).

#### `/surface`
```
/surface                                   # full vault scan
/surface NVDA                              # ticker-scoped
/surface semiconductors                    # sector-scoped
```
**Creates**: Research note (surface scan, `propagated_to: []`). **Modifies**: `_hot.md`. **Follow-up**: `/graph last` → `/deepen` or `/thesis` for opportunities.

Full scan: attention allocation, research velocity, decay alerts, contrarian signals, catalyst calendar, macro exposure. Scoped modes skip portfolio-wide rankings.

#### `/brief`
```
/brief NVDA                                # 1-page memo
```
**Creates**: Research note (brief, `propagated_to: []`, read-only derivative). **Modifies**: — . **Follow-up**: `/graph last`.

Briefs accumulate (not auto-archived — each is a dated snapshot of thesis state). Quarterly cleanup: `find Research/ -name '*Investment Brief.md' -mtime +90` → manually `mv` stale ones to `_Archive/Briefs/`.

#### `/catalyst`
```
/catalyst                                  # regenerate _catalyst.md
```
**Creates**: `_catalyst.md` (overwrite). **Modifies**: `_hot.md` (Active Research Thread + Open Questions for no-catalyst tickers). **Follow-up**: `/deepen TICKER Catalysts` for gaps.

Pre-regenerate snapshot protects prior calendar — hard-aborts if snapshot fails (prior calendar preserved). Recover via `/rollback` batch `catalyst-YYYY-MM-DD-HHMMSS`.

### 5.3 Decide

#### `/status`
```
# Conviction changes
/status NVDA conviction medium→low [reason]

# Status changes
/status NVDA status draft→active [rationale]
/status NVDA status active→monitoring [awaiting catalyst]
/status NVDA status monitoring→active [catalyst emerged]
/status NVDA status active→closed [what invalidated thesis]

# Drift acknowledgment
/status NVDA reaffirm [why drift signal is noise]
```
**Creates**: Snapshot (except draft→active and reaffirm), `.graph_invalidations` on closure. **Modifies**: Thesis frontmatter + log, Sector note, `_hot.md`. **Follow-up**: `/sync` → `/graph last` (closure especially needs `/graph last` to purge archived thesis from graph).

`draft→active` skips thesis snapshot (no analytical content changed). `active→closed` archives file, appends to `.archive_ticker_registry.md`, writes `.graph_invalidations` for neighbor cleanup.

**Reaffirm always logs** (idempotent-safe, preserves audit trail). Format: `Conviction reaffirmed at [level] after [drift review | proactive review] — [rationale]`.

#### `/prune`
```
/prune                                     # all theses
/prune semiconductors                      # sector filter
/prune stale                               # flag: last log >60 days
/prune low                                 # flag: conviction low
/prune draft | /prune monitoring           # flag: status
/prune semiconductors stale                # combined
```
**Creates**: Batch manifest (30-day regret window), `.graph_invalidations`. **Modifies**: Theses (closures/upgrades), Sector notes, neighbor Logs, `_hot.md`. **Follow-up**: `/graph last` → `/surface`.

Warns if unsynced research exists. Evaluates evidence trajectory, thesis integrity, opportunity cost, catalyst horizon, vault connectivity. Waits for approval before executing.

### 5.4 Reconcile

#### `/sync`
```
/sync                                      # graph-assisted incremental; touches .last_sync
/sync all                                  # brute-force; touches .last_sync; writes .sync_all_fresh
/sync NVDA                                 # ticker-scoped; does NOT touch .last_sync
```
**Creates**: `_sync-manifest`, snapshots (Tier A section edits). **Modifies**: Theses, Sectors, Macro, `_hot.md`. **Follow-up**: `/graph last`.

`/sync TICKER` preserves the default-sync baseline — the next `/sync` catches up unrelated changes. First-run: epoch placeholder created if `.last_sync` absent.

Idempotency keys on research-note wikilink presence in thesis Log (H4: plus secondary keys — source URL, date+ticker, tags — preserving idempotency across renames/moves). Eliminates midnight-rollover duplicates and rename-induced re-propagation.

#### `/graph`
```
/graph last                                # incremental: default after every /sync; cheap
/graph 7                                   # catch-up: watermark = today − 7 days
/graph 30                                  # catch-up: ~monthly
/graph                                     # full rebuild (after /sync all or corruption)
```
**Creates**: `_graph.md`. **Modifies**: — . **Follow-up**: — .

`.sync_all_fresh` marker forces full rebuild. `.graph_invalidations` from closures folded into changed-thesis bucket. No content files modified by any mode.

#### `/lint`
```
/lint                                      # full vault: 40 checks
/lint NVDA                                 # scoped: 15 checks on one thesis
```
**Creates**: — (report only). **Modifies**: — . **Follow-up**: fix flagged issues — graph issues → `/graph last` (or `/graph` for corruption); content issues require manual triage.

Scoped mode always runs #35 (`_hot.md` schema) and #37 (rename marker) if applicable — these are vault-global concerns. Key checks: #32 orphaned tickers, #33 closed-thesis files in `Theses/`, #35 `_hot.md` schema, #37 rename markers, #38 state marker hygiene, #39 `propagated_to:` producer contract, #41/#47/#48/#49 manifest aging.

#### `/clean`
```
/clean                                     # default 180 days (orphans PROTECTED)
/clean 90 | /clean 30                      # custom threshold (orphans PROTECTED)
/clean orphans                             # delete orphans only (any age)
/clean 180 --include-orphans               # age + orphans
```
**Creates**: — . **Modifies**: deletes old snapshots. **Follow-up**: — .

Safety net protects snapshots whose source was modified after snapshot (even if old). Orphans (source missing) default PROTECTED — fail-safe reversal from legacy. Completed prune manifests: 30-day floor regardless of threshold.

#### `/rollback`
```
/rollback                                  # list all snapshots
/rollback NVDA                             # list snapshots for NVDA
/rollback NVDA - Nvidia (pre-sync 2026-04-16-2115)   # restore specific
```
**Creates**: Pre-rollback safety snapshot. **Modifies**: Restored note, Sector note, `_hot.md`. **Follow-up**: `/sync TICKER` → `/graph last` (CRITICAL for recreated-file rollbacks).

Cascade detection: multi-file operations (sync, prune, status, compare, stress-test, thesis, catalyst batches) offer atomic multi-file restore. Neighbor-citation scan (H3) surfaces Macro and Sector prose references to closed theses for manual review. Intervening-entries check surfaces post-closure Log entries on neighbor theses for strikethrough review.

#### `/rename`
```
/rename META "Meta Platforms"              # rename Theses/META - Meta.md → Theses/META - Meta Platforms.md
/rename SQ "Block"                         # post-rebrand
```
**Creates**: Pre-rename snapshot; `.rename_incomplete.TICKER` marker on partial failure. **Modifies**: Thesis filename, inbound wikilinks (7 patterns), `_graph.md`, Sector note, `_Archive/Snapshots/` `snapshot_of:`, `_hot.md`. **Follow-up**: re-run `/rename TICKER "[same name]"` to retry failed Edits; marker auto-deletes when empty.

Atomic operation. TICKER does not change. To undo: `/rename TICKER "[OldName]"` (symmetric inverse). `/rename` is the sole exception that writes `_graph.md` directly.

---

## 6. Prompt Library

Manual prompts for synthesis that doesn't fit a single skill. Copy, adapt, paste.

### 6.1 Ingest from unusual sources

#### YouTube transcripts via Gemini

YouTube URLs can't be `/ingest`ed directly. Use Gemini to generate a transcript first.

1. Open Gemini and paste the YouTube URL
2. Paste the prompt below (replacing the URL placeholder) after the URL
3. Save Gemini's output as `YYYY-MM-DD - [Channel Name | Video Title] - video-transcript.md` in `_Inbox/`
4. Run `/ingest` → `/sync` → `/graph last`

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

### 6.2 Research deep-dives

#### 6.2.1 Session resumption
```
Read _hot.md. Summarise what I was working on, what's unresolved, and suggest what to focus on today.
```

#### 6.2.2 Earnings season triage
```
Which of my thesis companies report earnings in the next 2 weeks? For each, list the key metrics and outstanding questions from my thesis note that the report should answer.
```

#### 6.2.3 Earnings analysis (manual alternative to /ingest)
```
Fetch [TICKER]'s latest earnings transcript from [URL]. Extract: revenue by segment, margin trends, management guidance changes, and anything that contradicts or strengthens my thesis. Save as a research note and append a thesis log entry with conviction impact.
```

#### 6.2.4 Targeted angle research
```
Research [TOPIC] for [TICKER]. Focus on [specific angle: e.g. "pricing power durability", "customer concentration risk", "management capital allocation"]. Save to Research/ and update the relevant thesis log.
```

#### 6.2.5 "Teach me" deep-dive
```
I want to deeply understand [TOPIC: e.g. "how hybrid bonding works at the physics level" or "the economics of LNG spot vs contract pricing"]. Write a comprehensive explainer using my vault content as starting context, supplement with your knowledge, and save as a research note. Link to every relevant thesis. Write for an investment analyst — focus on why it matters for pricing power and competitive moats.
```

#### 6.2.6 Historical analogy finder
```
Read my thesis for [TICKER]. Find the closest historical analogy — a company in a similar position (market structure, technology transition, investor sentiment) 5-15 years ago. What happened, and what does the analogy imply for [TICKER]'s trajectory? What breaks the analogy?
```

#### 6.2.7 Management quality assessment
```
Research the management team of [TICKER]. Focus on: capital allocation track record, insider ownership, previous roles, and compensation alignment. Save as a research note and update the thesis.
```

#### 6.2.8 TAM reality check
```
Read my [TICKER] thesis. Decompose the TAM bottom-up: who are the actual customers, what do they pay today, what would need to change for [TICKER] to capture X%, and what's the realistic timeline? Compare to the top-down narrative. Save as a research note.
```

### 6.3 Adversarial synthesis

These are the highest-value prompts — force cross-vault synthesis to surface non-consensus insights.

#### 6.3.1 Cross-thesis pattern detection
```
Read all my thesis notes. Identify 3-5 non-obvious connections between companies in different sectors that share a common dependency, risk, or catalyst the market is likely pricing independently. For each, explain why the correlation matters and what trade it implies.
```

#### 6.3.2 "What is priced in?" audit
```
Read the [SECTOR] notes and all linked thesis notes. For each company, assess what the current conviction level implies about market expectations vs. my non-consensus view. Flag any thesis where my conviction has drifted from the evidence in my research notes.
```

#### 6.3.3 Second-order effects mapping
```
Read my macro note on [TOPIC]. Trace the second and third-order effects through my sector notes and thesis notes. Which thesis is most exposed to a risk I haven't written down? Which company benefits from a dynamic I've documented in a different sector but haven't linked?
```

#### 6.3.4 Invert the thesis
```
Read my [TICKER] thesis. Assume the bear case plays out fully. Which of my OTHER theses benefits most from that scenario? Map the hedging relationships across my portfolio using only vault content.
```

#### 6.3.5 Cross-vault contradiction check
```
Scan my vault for internal contradictions — places where one note's bull case depends on an assumption that another note's bear case challenges. List each contradiction with links to both notes.
```

#### 6.3.6 Manual consensus stress test (more control than /stress-test)
```
Read my thesis for [TICKER]. Now act as a skeptical short-seller. Using only information already in my vault (research notes, sector notes, macro notes), build the strongest possible bear case. Identify which of my bull assumptions is weakest and where my research has gaps.
```

### 6.4 Portfolio-level manual synthesis

#### 6.4.1 Sector note creation
```
Create a new Sector Note for [SECTOR] using the Sector Template. Search the vault for all relevant thesis notes, research notes, and macro connections. The "Investor heuristics" section should explicitly state what consensus believes and where they could be wrong.
```

#### 6.4.2 "What am I missing?"
```
Read my sector notes and thesis notes. Based on the industries I'm already tracking, which adjacent companies or sub-sectors am I NOT covering that my existing research implies I should be? Prioritise by how directly my existing theses depend on them.
```

#### 6.4.3 Portfolio exposure heatmap
```
Read all active thesis notes. Categorise each by: primary sector, geographic exposure, macro sensitivity (rates, FX, commodity, geopolitical), and position in the technology adoption curve. Identify unintentional concentration risks — am I overexposed to any single factor across multiple "independent" theses?
```

#### 6.4.4 Conviction recalibration
```
Read all thesis notes with conviction: high. For each, check the most recent log entry date. If the last update was more than 60 days ago, flag it as stale. Summarise what has likely changed since the last update based on the sector note and recent research.
```

#### 6.4.5 Conviction arc (visualize evolution)
```
Read [TICKER]'s Log entries. Build a conviction arc — plot every conviction change, reaffirm, and drift flag on a timeline. Annotate each with the trigger and rationale. Identify inflection points and whether the most recent trajectory is converging or diverging from thesis fundamentals.
```

### 6.5 Value chain & structural

#### 6.5.1 Find orphaned research
```
List all research notes in Research/ that are not wikilinked from any thesis or sector note. For each, suggest which thesis or sector it should connect to, and why.
```

#### 6.5.2 Frontmatter audit
```
Scan all notes in Theses/ and Research/. List any missing required frontmatter fields. Flag thesis notes where status is "draft" but the note has 3+ log entries — these are probably "active".
```

#### 6.5.3 Value chain mapping
```
Read my [SECTOR]-related thesis notes. Map the supply chain — who is whose customer, supplier, or competitor. Identify single points of failure and which thesis benefits most from a bottleneck at each node. Output as a canvas file.
```

#### 6.5.4 Tag taxonomy cleanup
```
List all unique tags across the vault. Flag duplicates or inconsistencies (e.g. #semi vs #semiconductors). Suggest a consolidated tag list.
```

#### 6.5.5 Template compliance check
```
Compare each thesis note against the Thesis Template. List missing sections — especially Key Non-consensus Insights and Outstanding Questions. For each gap, suggest which Research/ notes could fill it.
```

---

## 7. Cadence & Rhythm

### Every session
1. Read `_hot.md` (or §6.2.1 prompt for structured summary)
2. `/ingest` → `/sync` → `/graph last`
3. Work (research, analysis, thesis building)
4. `/sync` → `/graph last` again

### Weekly (or after heavy research)
- `/surface` (or scoped variant)
- `/catalyst` — refresh calendar
- `/lint TICKER` for any thesis actively edited
- `/graph last`
- If you missed `/graph last` for several days: `/graph 7` (or N days)

### Monthly (archetype G in §3)
- `/sync all` → `/graph` (full) → `/lint` → `/prune` → `/graph last` → `/clean` → `/surface` → `/catalyst` → `/graph last`
- Review `_hot.md` conviction changes and drift flags
- Conviction recalibration (§6.4.4) for all high-conviction theses
- Triage `/lint` #32, #33, #39, #41, #47, #48, #49 findings

### Event-triggered

| Event | Archetype | Chain |
|---|---|---|
| Earnings reported | A | `/ingest [URL]` → `/sync TICKER` → `/graph last` → `/status` if needed |
| Macro shock | A | `/scenario [event]` → `/status` for affected → `/sync` → `/graph last` |
| New stock idea | B | `/thesis TICKER` → `/status draft→active` → `/stress-test` → `/sync` → `/graph last` |
| Conviction drift flagged | C | `/status TICKER reaffirm` OR `/stress-test` → `/status` → `/sync TICKER` → `/graph last` |
| Competitor news | A | `/ingest [URL]` → `/compare` affected → `/sync` → `/graph last` |
| Sector rotation | D | `/surface [sector]` → `/scenario` if macro-driven → `/compare` key players → `/sync` → `/graph last` |
| Thesis closure | E | `/status TICKER status active→closed [reason]` → `/graph last` |
| Reopening archived thesis | F | `/rollback TICKER` → `/sync TICKER` → `/graph last` (critical) |

### When conventions change
- Update `CLAUDE.md` if you add new folders, change conventions, or shift research focus

---

## 8. Vault Hygiene — Anti-Patterns

What not to do, and why.

### Anti-pattern: Skip `/graph last`
**Why it's tempting**: "I just synced — why refresh the graph?"
**What breaks**: scoped `/surface [sector]` aborts with scope-validation. `/lint` flags graph staleness. Conviction drift detection misses cross-thesis signals.
**Fix**: make `/sync → /graph last` a single unit in your muscle memory.

### Anti-pattern: Write directly to `_graph.md` or `_catalyst.md`
**Why it's tempting**: "I'll just add this one edge manually."
**What breaks**: next `/graph last` overwrites. Next `/catalyst` regenerates from scratch. Your edit is silently lost.
**Fix**: `_graph.md` is owned by `/graph`, `_catalyst.md` by `/catalyst`. Never manually edit. Add the underlying signal (thesis wikilink, Catalysts section entry) and regenerate.

### Anti-pattern: Edit existing thesis Log entries
**Why it's tempting**: "Last week's log entry was wrong."
**What breaks**: Logs are Tier 2 append-only (CLAUDE.md rule #9 / Change Safety Rules). Drift detection, rollback cascade, and audit trail all assume monotonic append. Editing breaks `/sync` idempotency keys.
**Fix**: append a new dated entry that corrects the prior one (`Correction to [date]: [what was wrong]`). Or strikethrough via `/rollback` cascade if the original was systemic.

### Anti-pattern: Delete a thesis instead of archiving
**Why it's tempting**: "I'm done with this name forever."
**What breaks**: Log history lost. Wikilinks from sector/macro/research notes become orphans. Future `/thesis TICKER` re-creation loses the multi-signal archive collision check's ability to surface prior analysis. Violates CLAUDE.md rule #2.
**Fix**: `/status TICKER status active→closed [reason]` moves it to `_Archive/` with full history, updates the registry, and lets `/graph last` cleanly purge the graph.

### Anti-pattern: Run `/sync all` "just to be safe"
**Why it's tempting**: "I want to be sure nothing's stale."
**What breaks**: writes `.sync_all_fresh` which forces the next `/graph` to do a full rebuild (expensive). Re-reads every thesis, even unchanged ones. Can take 10+ minutes on a mature vault.
**Fix**: default `/sync` is graph-assisted incremental — fast and correct for 95% of cases. Reserve `/sync all` for the monthly maintenance chain or when `/lint` explicitly flags graph corruption.

### Anti-pattern: Stress-test without propagating
**Why it's tempting**: "The stress test just updated one thesis log — why sync?"
**What breaks**: `/stress-test` writes a research note that may surface cross-thesis implications. Without `/sync TICKER`, the sector note, macro notes, and cross-thesis Logs miss those signals. Next `/brief` or `/compare` reads a half-updated state.
**Fix**: always `/sync TICKER` after `/stress-test` unless it explicitly returned "thesis survives stress testing" with zero 🔴 findings.

### Anti-pattern: Ignore drift flags
**Why it's tempting**: "I know this thesis; the signal's noise."
**What breaks**: drift flags compound silently until the thesis quietly dies. `/sync` keeps flagging, you keep ignoring, and eventually you close a position 6 months late.
**Fix**: always choose one of three paths: (a) `/status TICKER reaffirm [why it's noise]`, (b) `/stress-test TICKER`, or (c) `/deepen TICKER [drifted section]`. Never leave a drift flag unacknowledged for more than a week.

### Anti-pattern: Accumulate briefs without pruning
**Why it's tempting**: "Each brief is a snapshot — they're all useful."
**What breaks**: 20+ briefs per ticker pollute `/Research`. `/sync` has more candidates to scan. Surface scans include stale briefs as "active research". Signal-to-noise drops.
**Fix**: quarterly — `find Research/ -name '*Investment Brief.md' -mtime +90` → review and manually `mv` stale ones to `_Archive/Briefs/`.

### Anti-pattern: Manually edit `_hot.md` sections
**Why it's tempting**: "I'll just remove this stale entry."
**What breaks**: `/lint #35` flags schema drift. `/lint #42` flags truncation markers. Next skill write may compound the manual edit with its own compression, producing garbled state.
**Fix**: let skills manage `_hot.md`. If something is genuinely wrong, delete the file entirely and let the next `/sync` auto-create with the full six-section schema.

### Anti-pattern: Chase every inbox item
**Why it's tempting**: "It's in `_Inbox/`, I should `/ingest` it."
**What breaks**: ingesting everything floods the graph with low-signal research notes. `/sync` slows. `/surface` surfaces noise. The vault drifts from synthesis engine toward bookmark manager.
**Fix**: curate `_Inbox/` before `/ingest`. Delete items that don't add non-consensus signal. Ingest only what will meaningfully update a thesis or sector.

---

## 9. Healthy Vault Signals

What "working well" looks like. Use as a quarterly checklist.

### Quantitative signals
- **`/lint` passes clean**: 0 Important-tier flags; only Nice-to-Have manifest aging
- **Graph freshness**: `/lint #38` green — `.sync_all_fresh` <24h, `.graph_invalidations` <24h
- **Conviction coverage**: every thesis has a Log entry within the last 60 days (or an active `/status` reaffirm)
- **Catalyst calendar density**: every active thesis has at least one forward catalyst within 90 days in `_catalyst.md`
- **Research-thesis linkage**: `/lint #32` flags <5% of Research notes as orphans
- **Drift-flag latency**: flags acknowledged within 7 days (reaffirm, stress-test, or status change)

### Qualitative signals
- **Non-consensus insight density**: `/surface` reports at least one contrarian signal per scoped run. If every run says "no blind spots", you're either too concentrated or not challenging enough.
- **Cross-sector linkage**: macro notes link to 5+ theses each; no macro note is a sector silo
- **Stress-test cadence**: each active thesis stress-tested within last 180 days (or actively deepened)
- **Archive hygiene**: closed theses have final-Log entries explaining what invalidated them (not just a date stamp)
- **`_hot.md` readability**: Active Research Thread tells a coherent story, not a list of disjointed syncs

### Warning signs (early)
- More than 3 theses in `monitoring` status for >60 days → prune decision overdue
- `_catalyst.md` "No Catalyst Identified" section has 5+ tickers → thesis drift
- Sector notes have >30 days between Log entries → sector thinking has stalled
- `_hot.md` Active Research Thread has the same ticker for >4 weeks → either a deep project (good) or stuck (investigate)
- `/lint` flags same Important issue two runs in a row → resolve before anything else

### Warning signs (late)
- `/surface` surfaces opportunities you've already surfaced → research velocity has decayed
- `/compare` outputs feel formulaic → either the comparisons are stale or the theses have converged (check divergence)
- Briefs outnumber thesis Log entries → you're presenting more than thinking

---

## 10. Canvas & Visual

### Relationship map
```
Create a canvas showing all active theses grouped by sector, with edges showing supply chain relationships, competitive dynamics, and shared macro exposures. Colour-code by conviction level.
```

### Thesis evolution timeline
```
Create a canvas for [TICKER] showing the evolution of my thesis over time. Use the Log entries as nodes, with annotations showing how conviction and key arguments changed at each point.
```

### Value chain canvas
```
Read my [SECTOR]-related theses. Map the supply chain as a canvas — who supplies whom, who competes with whom, where the bottlenecks are.
```

---

## 11. Infrastructure (User-Facing)

What you need to know to trust the automation. **Deep technical details are in [[INFRASTRUCTURE.md]]**.

### Key files you'll see

| File | Owner | Purpose |
|---|---|---|
| `_hot.md` | all 11 write-enabled skills | Session context cache — what you're working on, recent changes, open questions |
| `_graph.md` | `/graph`, `/rename` | Dependency map — used by `/surface`, `/prune`, `/lint`, `/sync` |
| `_catalyst.md` | `/catalyst` | Portfolio catalyst calendar — regenerated each run |
| `.last_sync` | `/sync`, `/sync all` | Watermark for incremental sync |
| `.sync_all_fresh` | `/sync all` | Forces next `/graph` to full rebuild; self-cleans |
| `.graph_invalidations` | `/status` (closure), `/prune` | Neighbor list for `/graph last` cleanup; self-cleans |
| `.rename_incomplete.TICKER` | `/rename` | Failed-rename repair state; auto-clears when fixed |
| `.archive_ticker_registry.md` | `/status`, `/prune` (closures) | Archive lookup table; consumed by `/thesis` collision check |
| `.vault-lock*` | all state-modifying skills | Concurrency lock; prevents races |
| `.drift-config.md` (optional) | user | `/sync` drift detection tuning |
| `_Archive/Snapshots/` | auto-created by destructive skills | Rollback point for `/rollback` |

### Key concepts

**Snapshot-before-edit**: every destructive skill snapshots the target file before editing. `_Archive/Snapshots/` is your universal undo buffer. `/rollback` cascades detect multi-file operations (sync, prune, status, compare, stress-test, thesis, catalyst) and offer atomic restore.

**Manifest lifecycle**: multi-file skills use skeleton → populate → flip. `in-progress` manifests are `/lint`'s signal that a skill crashed or the final flip missed. Completed manifests age out per `/lint` #36/#41/#45/#47/#48/#49. Prune manifests have a 30-day regret-recovery window.

**Atomicity**: `/scenario` / `/stress-test` / `/compare` write `propagated_to:` ONLY after all Log appends succeed — the field's absence is the signal for `/sync` to retry. `/lint #39` verifies producer contract.

**Idempotency**: `/sync` propagation keys on research-note wikilink presence (primary) plus source URL, date+ticker, tags (secondary — H4 fix for rename/move resilience). Once propagated, always propagated; rename-safe.

**Locks**: every state-modifying skill acquires a `.vault-lock*` at Step 0 and verifies ownership at every subsequent Bash block. Token-based (not PID-based) because Claude Code's Bash is stateless. Scope: vault-wide, ticker, multi-ticker (N separate per-ticker locks for `/compare`), or read-only.

**Rename safety**: `/rename` pre-flight (Step 3.5) Read/Write-probes every inbound wikilink reachable before the `mv`. Any Edit failure post-mv writes `.rename_incomplete.TICKER` for idempotent retry. Cross-new_name guard prevents two different target names from corrupting each other's repair state.

**Drift config** (optional, `.drift-config.md`):
```yaml
window_size: 5                 # default 5; min 3, max 10
base_threshold: 3              # default 3
post_stress_threshold: 4       # default 4
post_stress_window_days: 30    # default 30
deepened_exclusion_days: 14    # default 14
```

For manifest schemas, lock internals, watermark precision rules, H1-H4 atomicity details, and every edge case the skills handle, see [[INFRASTRUCTURE.md]].

---

## 12. Troubleshooting

Alphabetical by symptom. For architectural context, see [[INFRASTRUCTURE.md]].

### `.graph_invalidations` old (>24h) — `/lint #38`
Closures written but `/graph last` hasn't consumed. → `/graph last` (file consumed and deleted on success).

### `.sync_all_fresh` old (>24h) — `/lint #38`
`/sync all` ran but `/graph` hasn't consumed. → `/graph` (full rebuild; marker self-cleans).

### Brief accumulation — too many in Research/
Design choice: briefs aren't auto-archived. → Quarterly: `find Research/ -name '*Investment Brief.md' -mtime +90` → `mv` stale ones to `_Archive/Briefs/`.

### `/catalyst` aborts with "pre-regenerate snapshot failed"
Disk full / permissions / `_Archive/Snapshots/` unwritable. → Prior `_catalyst.md` unchanged. Fix filesystem issue and re-run. Hard-abort (H2) guarantees prior calendar is never lost.

### `/catalyst` produced a partial calendar (web search failed mid-run)
Pre-regenerate snapshot retained the prior calendar. → `/rollback` → `(pre-catalyst YYYY-MM-DD-HHMMSS)` snapshot. Re-run `/catalyst` when web access resolved.

### `/clean` reports "Orphan snapshots: N protected"
Default fail-safe — orphans (source file missing) aren't deleted. → Investigate (was source deleted in error?). To delete: `/clean orphans` (any age) or `/clean [days] --include-orphans`.

### Closed-thesis file still in `Theses/` — `/lint #33`
Failed `mv` from `/status active→closed` or `/prune`. → Either complete archive: `mv "Theses/[file]" "_Archive/[file]"` → `/graph last`. Or reopen: `/status TICKER status closed→active [rationale]` → `/sync TICKER` → `/graph last`.

### `/compare` aborts with partial lock acquisition
Some target ticker has an active lock; `/compare` rolled back its already-acquired peer locks. → Wait for conflicting ticker lock, re-run. Rollback guarantees we never hold a proper subset.

### `/compare` aborts with "Sector note write failed — rolled back"
Cross-sector atomicity fired. → Research note and thesis Logs preserved. Resolve sector file issue (lock, permission), re-run.

### Content-quality gate failed on `/ingest`
`#5 body word count` / `#6 sentinel` → paywall/CAPTCHA/empty page. Resolve access, re-run. `#8-#11 domain signature` → either content off-topic (re-ingest after fix) or `source_type` wrong (edit). `#12 numerical integrity` → OCR corruption; re-extract with cleaner tool. `#13 title-URL mismatch` → likely redirect to login; use archive.org. Research note auto-deleted; source retained.

### `/deepen TICKER [section]` aborts with "Section not found"
Target section doesn't exist (manually deleted or template drift). → Pick an existing section, OR restore from template, OR `/deepen TICKER` auto-detect.

### Drift signal never fires despite obvious deterioration
Post-stress-test suppression raised threshold to 4/5 within 30-day window. → Expected. To restore base sensitivity: edit `.drift-config.md` → `post_stress_threshold: 3`, `post_stress_window_days: 0`.

### Drift signal fires despite recent stress test
Suppression didn't apply (stress test >30 days old, or no Stress test Log entry). → If genuine: `/status TICKER reaffirm`. To customize: edit `.drift-config.md`.

### `/graph last` announces `.sync_all_fresh marker detected`
Normal — signals forced full rebuild. → No action; marker self-cleans.

### `/graph last` reports "Graph is up to date" but you just edited files
Legacy graph file without precise ISO watermark OR files modified before midnight of graph's `date:`. → Run `/graph` once to upgrade frontmatter to `last_graph_write:` ISO format; future runs use second-precision.

### Graph staleness >7 days — `/lint`
`/graph last` hasn't run after recent `/sync` runs. → `/graph 7` (or N days behind) to catch up.

### Graph staleness >30 days — `/lint`
Significant gap. → `/graph` (full rebuild).

### `/ingest` — "Source already ingested today" (hard block)
Same-day URL dedup matched existing research. → Delete existing note first if genuinely re-processing: `rm "Research/[matched-note].md"` then re-run.

### `/ingest` — "Source previously ingested" (cross-day prompt)
URL matches prior ingest from earlier day. → (a) skip and use existing, (b) re-ingest as new dated note (coexists), (c) cancel.

### `/lint #32` — orphaned ticker reference
Research `ticker:` matches no thesis. → `/thesis [TICKER]` to create, OR edit research frontmatter, OR accept as orphan.

### `/lint #35` — `_hot.md` missing required section
Skill-specific Edit silently no-oped OR manual edit removed heading. → Add missing `##` heading with `- _pending_` bullet. Or delete `_hot.md` and let next `/sync` auto-create full schema.

### `/lint #36` — prune manifest `in-progress`
Genuinely crashed prune OR successful prune whose Stage 5 flip silently missed. → Disambiguate first: do intended closures live in `_Archive/` with `status: closed`? Yes → flip-missed; edit manifest to `completed`, rm. No → crashed; `/rollback [ticker from manifest]` → `(pre-prune)` → cascade (a). `/prune` report's "flip verification failed" is cheap tell for flip-missed.

### `/lint #37` — rename marker present
`.rename_incomplete.TICKER` from failed `/rename`. Multiple markers = multiple in-flight repairs. → Run `/rename TICKER "[new_name from marker]"` for each.

### `/lint #39` — missing `propagated_to:`
`synthesis`/`brief` missing `[]` → producer didn't emit terminal-skip signal; add `propagated_to: []` immediately and investigate producer. `scenario`/`stress-test`/`comparison` missing (post-spec, date ≥ 2026-04-19) → check referenced theses' Logs; if present, manually backfill; if absent, `/sync` to trigger retry. Pre-spec (< 2026-04-19) → optional backfill to suppress catch-up entries.

### `/lint #41` / `/#48` — sync/status manifest `in-progress`
Flip failed OR skill crashed OR `/lint` ran during active run. → Inspect body for landed stages. If only flip failed: manually edit to `completed`. If incomplete: `/rollback [batch]` → option (b) cascade restore.

### `/lint #43` — stale lock
Lock's `timeout_at` expired. Auto-steal removed intentionally. → Choose: wait (may be long-running); manually `rm` if confirmed abandonment; consult manifests via `/lint #36/#41/#47/#48/#49` first.

### `/lint #47` — stress-test manifest `in-progress`
Rare — `/stress-test` writes as completed in one step. → Verify research note + thesis Log entry exist. If yes, manually edit to `completed`. If either missing, re-run `/stress-test`.

### `/lint #49` — thesis manifest `in-progress`
`/thesis` Step 7.5 flip failed OR `/thesis` crashed. → If thesis file exists AND all listed sections landed: edit manifest to `completed`. If partial: either manually complete remaining steps OR `/rollback [batch]` → option (b) full cascade (deletes thesis + reverts sector/hot.md).

### `LOCK_LOST` / `LOCK_STOLEN` mid-skill
Another skill or user `rm` removed/overwrote the lockfile after Step 0.1 acquired it. → Skill aborts; in-progress manifests remain for `/rollback` recovery. Investigate what stole the lock (likely concurrent session).

### Manifest completed but stale — `/lint #36/41/47/48/49`
Aging past useful window. → Prune: safe after 30-day regret. Others: safe after 90 days (Nice to Have) or 180 days (Important). `rm` flagged file.

### Name rejected by `/rename` — "Invalid name"
Disallowed char (`/\:*?"<>|`), leading dot, reserved name, >100 chars. → Use `[a-zA-Z0-9 \-_.,'&()]` only.

### `/prune` vault-lock timeout
Normal `/prune` is long-running. → Wait or increase timeout if legitimately taking hours on a huge vault.

### Rename conflict — `/rename` aborts with "In-flight rename conflict"
Marker exists with different `new_name:` than proposed. → Finish prior rename with marker's `new_name:`, OR manually resolve listed files + `rm` marker, OR accept loss of repair state.

### Rename marker blocking ticker-scoped skill — `❌ Rename repair incomplete for TICKER`
`.rename_incomplete.TICKER` present. → Complete repair: `/rename TICKER "[new_name from marker]"`. OR accept broken wikilinks: `rm .rename_incomplete.TICKER` then re-run target skill.

### `/rollback` neighbor scan flags macro or sector citations (H3)
Extended scan — macros and sectors may cite the restored thesis in body prose outside Logs. → Review each citation for post-closure premise. Macros with prose like "LITE's closure removes..." need manual edit. Use classification tag (premise-dependent vs contextual) to prioritize.

### `/rollback` of closed thesis surfaces "Intervening Log entries"
Step 6.2.5 scan found post-closure entries on neighbor theses. → (a) surface-only, (b) auto-strikethrough `Cross-thesis closure:` premises, (c) auto-strikethrough all, (d) skip.

### `/rollback` on status batch offers "thesis-only" vs "full transaction"
Step 2.5e cascade. → (a) thesis-only restores frontmatter only. (b) full restores thesis + sector + un-archives + clears invalidations.

### `/rollback` on stress-test batch surfaces the Log entry
Step 2.5d cascade. → (b) cascade + strikethrough rewrites as `~~entry~~ → Reverted YYYY-MM-DD: stress-test judged invalid`. Research note preserved.

### `/rollback` on sync/compare batch surfaces Tier B Log entries
Cross-thesis Log appends are Tier B (no per-file snapshot). → Per-entry: (1) leave as historical, (2) strikethrough, (3) manually delete (erroneous only). Option (b) in cascade prompt auto-applies (2).

### `/rollback` on thesis batch offers "delete thesis only" vs "full cascade"
Step 2.5f cascade — `/thesis` creates new files (no pre-state). → (a) Delete thesis only — leaves sector + `_hot.md` edits dangling (manual cleanup). (b) Full cascade — deletes thesis + reverts all associated edits. Consider saving thesis content elsewhere first.

### Silent `_hot.md` skill no-ops
Missing required section in `_hot.md`. 11 skills write to `_hot.md`; schema drift causes silent skips. → `/lint #35` to detect. Fix: add missing heading with `- _pending_` bullet, or delete `_hot.md` and let next `/sync` recreate.

### Snapshots stale (>180 days) — `/lint #16`
Normal aging. → `/clean` default 180 days. Active safety nets (source modified after snapshot) auto-protected.

### `/sync` propagates research note twice after renaming
Pre-H4: wikilink-only idempotency broke on rename. Post-H4: secondary keys (source URL, date+ticker, tags) preserve idempotency across renames/moves. → New runs handle renames correctly. Legacy duplicates: manually consolidate via strikethrough.

### `/sync TICKER` works but default `/sync` misses propagation
Reopened thesis not yet in `_graph.md`. → `/graph last` registers the restored adjacency.

### `/thesis TICKER` prompts about archived thesis
Multi-signal archive-collision check matched (filename/frontmatter ticker/registry/snapshot trail). → (a) `/rollback TICKER` to restore, (b) different name suffix for dual-file, (c) accept dual-file state, (d) cancel.

### `/thesis TICKER` prompts about missing sector note
Sector `match_confidence: none`. → (a) Create `Sectors/[value].md` scaffold with this thesis as first entry, (b) proceed without sector update, (c) cancel to fix sector value.

### Truncation markers in `_hot.md` — `/lint #42`
Manual edit or buggy skill left `...`, `[compressed]`, `[truncated]`, or unclosed formatting. → Manually remove. Investigate: if skill-produced, check compression-contract compliance.

### Vault lock held — any skill aborts
`.vault-lock*` actively held. → Wait for holder. If confirmed crashed: manually `rm [lockfile_path]`.

### `_hot.md` exceeds 2,500 words after skill runs
Hard cap reached; skill aborted `_hot.md` update (primary operation still succeeded). → Manually trim Sync Archive or `*Previous:*` lines. `/lint #35` + `#42` diagnose drift.
