---
date: {{date}}
tags: [template, thesis-breakdown, video-script]
status: active
source: vault synthesis + incremental web research
---

# Breakdowns Template — B (chain-first)

Use this prompt to create or refresh a beginner-level bilingual video series for one **value chain / theme** (default), one **flagship company**, or one **company profile**. **Each run writes one date-prefixed Markdown file containing the series plan, English scripts, Mandarin translations, and bilingual video metadata.** It never creates a subfolder or separate episode notes.

## What B changes vs [[Templates/Breakdowns Template]]

| Delta | Why |
|---|---|
| Chain series are the default unit; flagship company series are the exception | ~70 of 82 covered names are illegible to beginners as companies but legible as "the firm that owns layer X"; the vault's edge (bottleneck migration, qualification gates) is a chain story |
| Three scale tiers: chain 8–12 eps · flagship 10–15 · profile 1–3 | 82 theses × 15 episodes is impossible at weekly cadence; tiers make the coverage math close |
| Four archetype spines (cyclical / compounder / chain / macro-vehicle) swap the mandatory coverage | One company-debate spine cannot serve WFE cyclicals, software compounders, GLD/BTC/CCJ vehicles, and stack maps |
| Expectations episode mandatory in every archetype | The A-template SK Hynix pilot debated business quality for 15 episodes and never asked what the price assumes — the vault's core discipline (G-13) |
| Coverage Ledger: every source-note risk/question mapped or excluded with a reason | The pilot silently dropped Taiwan tail, FX, and supply-chain risks; triage must be deliberate |
| Watchlist rows cite [[_watchers.md]] / [[_catalyst.md]] instead of forking observables | One falsifier registry, not three |
| Draft-on-schedule: full scripts only inside the freshness horizon; later episodes stay Outlined | The pilot drafted 15 scripts ten days before earnings that staled six of them |
| `plan-slate` mode maintains `Thesis Breakdowns/_Slate.md` (quarterly slate + concept-ownership registry) | Per-run invocation at portfolio scale produces orphaned series and re-taught context |
| Pre-edit snapshot in mutating modes; auto holdings disclosure | Only real data-loss vector; ~27 covered names are live holdings |

Bilingual scripts, video titles/descriptions, and date-prefixed filenames carry over from Template A unchanged.

## How to use this template

- **Editable inputs** are the controls for a specific run. **Execution instructions** are the reusable method — normally leave unchanged.
- Reference this template in chat and provide only input overrides; do not paste the execution block.

### Recommended workflow

```text
Use [[Templates/Breakdowns Template - B]] with these inputs:
mode: full-series
series_type: chain
subject: The Advanced Packaging War
source_note: [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]]
profiled_companies: [BESI, 2802 Ajinomoto, CAMT, ONTO]
core_question: As chips stop shrinking, who gets paid for stitching them together — and which layer is mispriced?
```

Flagship run: `series_type: flagship`, `subject: NVDA`, `source_note: [[Theses/NVDA - Nvidia]]`. Profile run: `series_type: profile`, `subject: 6515 - WinWay Technology`, `parent_series:` the chain breakdown it extends. Ongoing update: `mode: refresh-episodes`, `subject: <existing series>`, `episodes_requested: 3,7`. Quarterly planning: `mode: plan-slate` and nothing else.

## Editable inputs — change these for each run

```yaml
mode: full-series # full-series | next-episode | refresh-episodes | replan-series | plan-slate
series_type: auto # chain | flagship | profile | auto (resolution rules in STEP 0)
archetype: auto # cyclical | compounder | chain | macro-vehicle | auto
subject: "<theme, TICKER, or company>"
source_note: "<vault path — sector/macro note for chain, thesis for flagship/profile>"
profiled_companies: [] # chain series: vault tickers profiled per layer, in rough episode order
parent_series: "<optional — existing chain breakdown a profile extends>"
series_title: "<optional; let the LLM propose one if blank>"
episode_count: auto # chain 8-12 | flagship 10-15 | profile 1-3; integer overrides
episodes_requested: all # all | next | 3,5,8 | 6-10
audience: beginner investor
target_runtime: 1.5-2.5 minutes
spoken_wpm: 140
cadence: weekly
tone: conversational, calm, curious, plain English
presenter_format: one person sitting down and explaining directly to camera
freshness_window_days: 45
draft_horizon: auto # full scripts only for episodes airing within freshness_window_days at `cadence`; later episodes stay Outlined. `all` forces full drafting.
as_of_date: today
file_date: today # used in the filename when the series is first created
geography_or_listing: "<optional>"
core_question: "<optional; chain series default to the source sector note's Key Industry Questions>"
angle_overrides:
  - "<optional emphasis>"
must_include:
  - "<optional topic, source, risk, or question>"
must_avoid:
  - "<optional topic, framing, jargon, or claim>"
disclaimer_delivery: description-only # description-only | spoken-finale | none
holdings_disclosure: auto # auto = mandatory whenever subject or any profiled company appears in Live Portfolio.md or Watchlist.md
languages: [English, Mandarin Chinese]
mandarin_variant: Simplified Chinese # zh-CN; ask explicitly for Traditional Chinese if preferred
translation_style: natural spoken Mandarin, meaning-preserving, similar runtime
video_title_style: concise, specific, non-clickbait
video_description_length: 50-90 English words plus a Mandarin translation
output_root: "Thesis Breakdowns"
output_filename: auto # "YYYY-MM-DD - <Subject>.md"; profile files append " - Profile"
```

## Execution instructions — normally leave unchanged

```text
Create or update a short-form investment-breakdown series using the inputs above.
Merge chat overrides into the Editable inputs; unspecified fields keep template defaults.

OBJECTIVE
Turn existing vault research plus an incremental current-web check into coherent 1.5-2.5 minute beginner-level spoken scripts — English original plus natural Mandarin translation per episode, with bilingual video titles and descriptions. Every episode stands alone; the sequence moves from understanding the subject to debating what the price assumes. Write complete scripts only within draft_horizon; later episodes are Outlined by design, not omission.

STEP 0 — RESOLVE MODE, SERIES TYPE, ARCHETYPE
1. mode: plan-slate → skip to STEP 7 (no series file is created or edited).
2. series_type auto-resolution: source_note is a sector or macro note → chain. Thesis subject with active status, high conviction, and mainstream name recognition → flagship. Any other single company → profile.
3. archetype auto-resolution: chain series → chain. Macro vehicles and commodity/asset subjects (no operating company) → macro-vehicle. Companies: classify per [[Mental Models/Industry - Semiconductors]] #13 where applicable — true cyclical or semi-cyclical → cyclical spine; structural compounder → compounder spine. State the classification in the Series Map preamble; it is a hypothesis, and a good series may argue it.

STEP 1 — PREFLIGHT AND VAULT-FIRST RESEARCH
1. Get the actual current date; never infer it from note dates.
2. Read source_note in full. Chain series: the sector note's Key Industry Questions seed core_question; its History, Competitive Dynamics, and Product-Level sections seed the map; read the thesis of every profiled company. Flagship/profile: read the thesis in full, then the most decision-relevant linked notes. Resolve the subject against Theses/, Sectors/, Research/, Macro & Technology/, _hot.md, and _graph.md; never treat _graph.md as a substitute for reading source notes.
3. Read [[Mental Models/Generalist - Overview]] and the relevant industry/lens notes. Apply them as questions, not conclusions. Run the base rate against the thesis and state the single falsifying datapoint.
4. Read the subject's rows in _watchers.md and _catalyst.md. These are the canonical observables — the series Watchlist cites them rather than reinventing them.
5. Holdings check: if the subject or any profiled company appears in Live Portfolio.md or Watchlist.md, holdings disclosure is mandatory in every episode description (and in the spoken finale when disclaimer_delivery is spoken-finale).
6. Ongoing modes (next-episode, refresh-episodes, replan-series): read the entire existing breakdown file, then copy it to _Archive/Snapshots/<filename> (pre-breakdown-refresh YYYY-MM-DD-HHMMSS).md BEFORE the first edit.
7. Do not alter theses, sector notes, macro notes, Research notes, _watchers.md, or _catalyst.md. If web research contradicts a vault note, record the conflict in the Evidence Ledger and flag it for the user; never fix the vault from this template.

STEP 2 — INCREMENTAL WEB RESEARCH
1. Browse for changes since the newest vault material and within freshness_window_days, in this order: (a) company filings, IR, earnings, product releases; (b) customer and competitor primary sources; (c) regulators, standards bodies, industry data; (d) reputable reporting; (e) social/thematic chatter only to identify current questions and sentiment — never as proof. Chain series: run the check per profiled company, scaled to its episode weight.
2. Classify every candidate claim: VERIFIED FACT, INDUSTRY ESTIMATE, MANAGEMENT CLAIM, MARKET CHATTER, or ANALYTICAL INFERENCE.
3. Compare web against vault. Surface conflicts explicitly; prefer the fresher primary source but preserve unsettled disagreements.
4. Add a dated hook only where it changes explanation, stakes, or timing; otherwise write "No material freshness update" in production notes.
5. Every episode gets a non-spoken Sources section: 2-6 decision-relevant links plus an as-of date. No citations in spoken flow.

STEP 3 — SERIES DESIGN BY ARCHETYPE
Episode budgets: chain 8-12, flagship 10-15, profile 1-3. Do not stretch a thin subject or compress a dense one. The four-act spine is rails, not a table: ACT I — UNDERSTAND · ACT II — ECONOMICS & COMPETITION · ACT III — VARIANT & QUESTIONS · ACT IV — DECIDE.

Universal mandatory coverage (every archetype):
- Subject and why now.
- Product/technology or causal mechanism explained for a beginner.
- Where pricing power or value capture sits.
- EXPECTATIONS EPISODE: what the current price already assumes, positioning/crowding where observable, and the single operating variable the market is most likely mispricing. Never a price target — the episode teaches the gap between a good business and a good investment.
- At least one variant-perception episode and one adversarial episode.
- Outstanding questions with observable answers.
- Bull case, bear case, and a finale debate with an evidence-weighted synthesis and the 1-2 observables that decide it.

Archetype-specific mandatory coverage (swap in, on top of universal):
- cyclical: cycle mechanics and the base rate of prior cycles; where in the cycle the evidence says we are; the price second derivative as a watchlist item; capital-response tracking (capex vs demand durability).
- compounder: moat type and durability tested against its named failure mode; ROIIC and reinvestment runway in beginner terms; management quality and capital-allocation record (mandatory here, optional elsewhere).
- chain: the stack map episode first (name every layer, who owns it); layer economics (who takes margin and why); bottleneck-migration episode (where scarcity moves next and what architecture shift moves it); which layer the market misprices.
- macro-vehicle: what actually drives the price (mechanism, not narrative); regime identification and what would end the regime; what is priced in; flows/positioning as evidence class.

Profiles (1-3 episodes) answer exactly: which layer does this company own, why does it win that layer, and what breaks it. Inherit the parent chain series' context in one sentence; never re-teach it.

RISK RECONCILIATION — before writing scripts, diff the planned map against the source note's Risks and Outstanding Questions (thesis) or Key Industry Questions and Macro Shifts (sector/macro note). Every item is either mapped to an episode or listed in ## Coverage Ledger as excluded with a one-line reason. Silent omission is a quality-gate failure.

Order: the subject decides episode titles and order; merge overlapping roles; one core claim per episode; variant and unresolved questions sit between overview and finale, not appended.

STEP 4 — STANDALONE + ARC + CROSS-SERIES CONTRACT
STANDALONE TEST — a first-time viewer can answer: what is this about; why does it matter to the investment case; what evidence supports the claim; what could make it wrong.
ARC TEST — a returning viewer gets one new layer without a recap; callbacks are one sentence and restate context; end on an open loop, never "you had to watch part X."
Within a series: no duplicate hooks, analogies, or conclusions; reuse a statistic in at most 3 episodes, and only when it does a different analytical job each time.
Across series: check the Concept Ownership registry in Thesis Breakdowns/_Slate.md. A shared concept (HBM, EUV, CoWoS, the memory cycle) is taught deeply in exactly one owning series; every other series uses a one-sentence version. Claim newly-taught concepts in the registry via plan-slate or note them in the Series Revision Log for the next slate pass.

STEP 5 — SCRIPT CONTRACT
Write both language versions for one presenter speaking to camera.

English script:
- 210-350 spoken words at ~140 wpm; prefer 240-310.
- Lead with the insight or tension; no greetings or throat-clearing.
- Short spoken sentences, contractions, plain English. Define acronyms on first use; max two new acronyms and one analogy per episode.
- One core claim, 1-3 supporting facts, then the strongest counterpoint.
- Explain numbers by meaning — but carry at least two concrete numbers per episode; credibility lives in specifics.
- Distinguish fact from estimate in the wording: "the company reported," "TrendForce estimates," "investors are debating," "my read is."
- No hype, certainty theatre, price targets, or personalised recommendations. The bull case is never the narrator's verdict; the finale's evidence-weighted classification is allowed and must name its falsifiers.
- No citations, stage directions, or markdown links in spoken text.
- Close by answering the hook plus (except the finale) a one-sentence bridge.

Mandarin Chinese script:
- Natural spoken Mandarin in Simplified Chinese (zh-CN), not literal translation syntax.
- Preserve the English script's thesis, facts, numbers, dates, uncertainty labels, counterpoint, and conclusion. Do not add or remove an investment claim.
- Explain or transliterate names and technical terms naturally on first use; retain standard English acronyms (HBM, DRAM, NAND, GPU) where a Chinese investor expects them.
- Target the same 1.5-2.5 minute delivery; roughly 450-700 characters, adjusted for natural cadence.
- Translate the meaning of analogies, not their exact wording, when direct translation sounds unnatural.
- Parity check: every number, named company, causal claim, counterpoint, and falsifier in English has an equivalent in Mandarin.

Video title and description:
- Every episode: suggested English title + natural Simplified-Chinese title — concise, specific, standalone, non-clickbait.
- Every episode: English description of 50-90 words + meaning-equivalent Mandarin description. State what the viewer learns, the live debate, the educational/not-advice disclaimer per disclaimer_delivery, and — when holdings_disclosure applies — a plain holdings statement ("I hold a position in X" / 「本人持有X的仓位」).
- Titles and descriptions are publishing metadata, outside spoken runtime.

Internal rhythm (adapt, never label in speech): cold open 1-2 sentences → minimum context 2-4 → core mechanism and evidence → counterweight → takeaway and bridge.

STEP 6 — OUTPUT STRUCTURE
Create or update exactly one file:

Thesis Breakdowns/YYYY-MM-DD - <Subject>.md   (profiles: "YYYY-MM-DD - <Subject> - Profile.md")

Use file_date for the prefix at creation. Ongoing modes locate and update the existing dated file — never create a new dated copy or rename because the refresh date changed. No subfolders, no per-episode notes.

Single-file requirements:
- Frontmatter: date, tags, status, series_type, archetype, subject, source_note, profiled_companies (chain), parent_series (profile), as_of, episode_count, languages, mandarin_variant, source.
- One-sentence series promise + the investment question the arc resolves + the archetype classification stated as a hypothesis.
- ## Series Map — table: #, act, episode/title, standalone question, role in arc, current hook, status (Outlined | Draft | Provisional | Final), last refreshed. Episodes beyond draft_horizon are Outlined (role, promise, evidence pointers — no scripts). Mark a drafted episode Provisional when a Watchlist observable is scheduled to resolve before its air date.
- ## Narrative Rails — repeated-context rule, standalone/arc balance, disclaimer placement, concepts this series owns vs borrows.
- ## Evidence Ledger — verified facts, estimates, management claims, chatter, open conflicts. It must contain every load-bearing claim: any claim whose correction would force an episode re-record. Include vault-vs-web conflicts flagged for the user.
- ## Coverage Ledger — every source-note risk/question → episode # or "excluded: <reason>".
- ## Watchlist — observable, expected window, source, bull reading, bear reading, episodes affected, registry ref (_watchers.md row / _catalyst.md entry, or "NEW — candidate watcher row" for the user to add; never edit the registries from this template).
- ## Scripts — every episode in sequence, exact hierarchy:

  ### Episode 01 — <Title>
  **Series role:** ...
  **Standalone promise:** ...
  **Freshness hook:** ...
  **Suggested video title:** ...
  **建议视频标题（简体中文）:** ...

  #### Video Description
  <English publishing description>

  #### 视频简介（简体中文）
  <Mandarin publishing description>

  #### English Script
  <English spoken words only>

  #### 中文脚本（普通话，简体）
  <Mandarin spoken script only>

  #### Production Notes
  <English and Mandarin runtime estimates, visual, pronunciation, disclaimer + holdings line, bridge, freshness classification>

  #### Sources
  <vault wikilinks and direct web links>

  #### Episode Revision Log
  <append-only dated changes>

  (Outlined episodes stop after the header block plus a 3-5 bullet evidence outline — no Description/Script sections until a next-episode run converts them.)

- ## Series Sources — vault and web source ledger.
- ## Series Revision Log — append-only, at the end.

STEP 7 — MODE-SPECIFIC BEHAVIOUR
- full-series: design the arc; write map, bilingual metadata, and complete bilingual scripts for episodes within draft_horizon; Outline the rest.
- next-episode: refresh the web for that episode's claims, convert the next Outlined episode to a full bilingual draft in the same file, update map + Series Revision Log.
- refresh-episodes: re-check only facts that can have changed; revise the named English scripts, Mandarin translations, titles, and descriptions in place; preserve each episode's core role unless evidence forces a replan; append to each Episode Revision Log. Snapshot first (STEP 1.6).
- replan-series: preserve existing script sections; rewrite the map in the same file showing old → new ordering; identify which episodes need revision before changing them. Snapshot first.
- plan-slate: read Theses/ frontmatter (status, conviction), Sectors/, Macro & Technology/, _catalyst.md, and every existing file in Thesis Breakdowns/. Write or update Thesis Breakdowns/_Slate.md containing: (1) coverage math — episodes/year at cadence vs proposed commitments; (2) next-quarter slate table — series, series_type, archetype, source_note, episode budget, catalyst-aligned start window, rationale; (3) Concept Ownership registry — concept → owning series; (4) orphaned or stale series flags (as_of older than freshness_window_days, Outlined episodes overdue, Provisional episodes whose observable has resolved). Recommend, never auto-start, new series.

STEP 8 — QUALITY GATE
Before finishing:
1. English word count per episode within 210-350 (unless runtime overridden); at least two concrete numbers per script.
2. Mandarin character count and runtime estimate within target without dropping analytical content.
3. English-to-Mandarin parity on all numbers, names, dates, uncertainty language, counterpoints, falsifiers.
4. Every drafted episode has English and Mandarin title, description, and script; every Outlined episode has none of these and says so in the map.
5. Every episode has a counterpoint and stands alone in either language.
6. Universal + archetype-mandatory coverage present — including the expectations episode; sequence has no repeated explanations; no statistic appears in more than 3 episodes.
7. Coverage Ledger accounts for every source-note risk/question (mapped or excluded-with-reason).
8. Watchlist rows carry registry refs or an explicit NEW flag.
9. All vault wikilinks and web URLs verified; estimates, chatter, and unresolved conflicts flagged, never promoted to fact.
10. Finale argues both sides and names the 1-2 deciding observables; holdings disclosure present wherever required.
11. Filename begins with YYYY-MM-DD; exactly one breakdown file created or updated, no per-episode files; mutating modes took a snapshot (report its path).
12. Report every file created or modified.
```

## Design rule in one line

**Fix the analytical roles and quality gates; let the subject pick the archetype, the archetype pick the coverage, and the company decide titles, order, and weight — teach every shared concept exactly once.**
