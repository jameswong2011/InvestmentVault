# Claudian Investment Vault — An LLM Wiki for equity research (v5)

*Converted from `claudian-explainer-v5.html`. The original is an interactive single-page explainer; its diagrams, tabbed viewers and terminal simulator are rendered here as static text, with their full content preserved.*

## Contents

- §1 An LLM Wiki for equity research
- §2 Where the edge comes from
- §3 Live context engineering
- §4 Architecture map
- §5 Templates & standards
- §6 The thesis as a forcing function
- §7 Skills — concept & catalogue
- §8 A day in the life
- §9 Workflows map
- §10 Inline callouts
- §11 Try a skill
- §12 FAQ
- §13 Glossary
- [Repo](https://github.com/jameswong2011/InvestmentVault)

---

## §1 · An LLM Wiki for equity research

### Karpathy's LLM Wiki pattern, *applied to investment research.*

In April 2026, Andrej Karpathy described a pattern for using LLMs to maintain personal knowledge bases. Instead of asking an LLM the same question over and over and watching it rediscover the answer each time, you have it *incrementally compile* raw sources into a structured wiki — a persistent, interlinked artifact that gets richer with every source you add. This vault is that pattern, instantiated for one specific job: building defensible, non-consensus equity research that compounds over years.

### §1.1 · Karpathy's core insight — Compilation, not retrieval.

The default LLM-with-documents pattern is RAG: you upload sources, the model retrieves relevant chunks at query time, generates an answer. Each query rediscovers knowledge from scratch. Nothing compounds. Karpathy's reframe was to invert this:

> "The LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then *kept current*, not re-derived on every query."
>
> — Andrej Karpathy, [llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · April 2026

The promise is **compounding knowledge**: the cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. Investment research is exactly the kind of work that benefits — qualitative, multi-year, with ideas that need to be revisited as new evidence arrives.

### §1.2 · The three-layer architecture, applied — Raw sources · Wiki · Schema.

Karpathy's architecture has three layers. Each maps directly to this vault's investment-research instantiation:

#### Raw sources — Layer 1 · immutable

```
/_Inbox/
/Research/ (provenance)
```

**Karpathy:** "Your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them."

**Here:** earnings transcripts, sell-side research, expert calls, regulatory filings, substack pieces. Drop them into `_Inbox/`, the `/ingest` skill processes them, the originals move to `_Inbox/processed/`. The `source:` URL gets locked into frontmatter and is never edited. Provenance has to be auditable for an investment decision you'll defend months later.

#### The wiki — Layer 2 · LLM-maintained

```
/Theses/
/Research/ (summaries)
/Sectors/
/Macro/
```

**Karpathy:** "A directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. You read it; the LLM writes it."

**Here:** the wiki is structured for equity research specifically. Each ticker has a 14-section thesis. Each source becomes a 4-section research note. Each sector has an 11-section overview that links every active position in it. Macro frameworks live in their own folder. The LLM maintains all of it — you curate sources and ask questions; the cross-references, summaries, and Log entries take care of themselves.

#### The schema — Layer 3 · the contract

```
CLAUDE.md
/Templates/
/.claude/skills/
```

**Karpathy:** "A document (e.g. CLAUDE.md for Claude Code) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot."

**Here:** `CLAUDE.md` defines the writing standards (no hedge words, lead with the insight, tables over prose), the safety tiers, and the file conventions. `Templates/` holds the skeletons that force structure on every thesis, research note, and sector. `.claude/skills/` contains 21 deterministic workflow specifications. Together these are the operating contract — they convert Claude from a chatbot into a disciplined research analyst with house style.

Karpathy's metaphor: *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."* That mental model is the right one here too. You're the product manager — you decide what to build, what questions to ask, what sources to add. Claude is the engineer doing the actual maintenance.

### §1.3 · Architectural principles — Six properties that distinguish this from RAG, chat, or a notes app.

These are the load-bearing design decisions inherited from the LLM Wiki pattern and adapted for investment work. The rest of this guide explains how each one is implemented.

#### PRINCIPLE 01 · Persistent, compounding artifact

The wiki is a durable object. It gets richer with every source. Insights from March don't evaporate by September — they're integrated into the synthesis and cited when relevant. This is the single biggest behavioral difference from chat-with-files.

#### PRINCIPLE 02 · Human curates, LLM maintains

You source articles, ask questions, set direction. Claude does the grunt work — summarising, cross-referencing, filing, bookkeeping. The maintenance burden that kills hand-written wikis goes to zero, so the wiki actually stays current.

#### PRINCIPLE 03 · Immutable raw sources

Every claim is traceable to its source. The `source:` URL in frontmatter is locked at creation and never modified. Months later, when defending an investment decision, the audit trail holds up.

#### PRINCIPLE 04 · Schema as operating contract

`CLAUDE.md` + Templates + skill specs are loaded into every session. Writing standards stay enforced. The 14-section thesis structure stays enforced. House style stays consistent across hundreds of notes written over years.

#### PRINCIPLE 05 · Ingest · Query · Lint

Karpathy's three operations. `/ingest` compiles new sources into the wiki. Manual prompts query it. `/lint` periodically audits health — orphans, staleness, contradictions, missing cross-references. The vault adds two finance-specific operations on top: conviction tracking via `/sync` and `/status`, and retrospective review via `/retro`.

#### PRINCIPLE 06 · Append-only audit log

Each thesis has a chronological `## Log` section — never edited, only appended. Karpathy's `log.md` is per-vault; this implementation runs it per-thesis, so every position has its own evolution history. `/retro` reads these logs to surface where your thinking diverged from price.

### §1.4 · Why this matters for investing — The specific problems an LLM Wiki solves better than a notes app.

The generic Karpathy framing covers any long-running knowledge work. Investment research has three specific failure modes that the wiki pattern resolves in a way no spreadsheet, Notion page, or chat interface can.

#### PROBLEM 01 · Conviction drift goes undetected

Without a log, you don't notice that you've quietly downgraded a name three times in two months. The wiki's append-only Log per thesis makes drift mechanical — `/sync` flags it: "4 of your last 5 updates on this name pushed back on the Bull Case. Conviction is drifting whether you've noticed or not."

#### PROBLEM 02 · Cross-thesis blind spots stay invisible

At 40 positions, you can't hold the whole portfolio in your head. The wiki makes synthesis possible at the portfolio level: *"Which of my bull cases share an implicit macro dependency?"* · *"Scan for places one note's bull case depends on what another note's bear case challenges."* These prompts only work when the wiki exists.

#### PROBLEM 03 · Hindsight has no anchor

Three months after a trade you can't remember what your written conviction was when you put it on. The wiki preserves it. The retro engine reads those preserved positions against actual market reaction since — and surfaces the names where narrative and price diverged most. Lessons learned become structural, not aspirational.

The rest of this guide is how the pattern is implemented in practice. The pillars below preview the chapters.

- → §3 + §4 — **Live context engineering & architecture map.** How Claude keeps awareness across sessions: six files (CLAUDE.md, _hot.md, _graph.md, _catalyst.md, .last_sync, snapshots) that turn a stateless LLM into one with persistent memory of your portfolio — laid out visually in the architecture map.
- → §5 — **Templates & standards.** The structural enforcers that make hundreds of notes feel like they came from the same disciplined analyst. Includes the writing standards that ship in CLAUDE.md.
- → §7 + §9 — **Skills & workflows.** Twenty-one deterministic specifications that extend Karpathy's Ingest/Query/Lint with finance-specific operations — and the workflow map showing how they chain together for common scenarios.

---

## §2 · Where the edge comes from

### Three engines that turn a maintained wiki into investment alpha.

A static knowledge base is interesting. A knowledge base whose evolution gets actively interrogated against market reality is a research process. Three mechanisms do that interrogation.

#### ENGINE 01 · The retro engine — narrative-price gap detection

Once a week, `/retro 1w` reads every Log entry, callout, and conviction shift from the past 7 days, overlays it against actual price moves and news flow, and classifies each ticker into a 3×2 grid: aligned (already priced), inverted (positioning signal — strongest single signal, weighted 1.5×), or unreactive (catalyst dismissed or bear case ignored, weighted 2×). The output is a ranked list of trade ideas — alpha harvest candidates, missed signals, stress-test candidates. The retro never auto-changes conviction; it tells you which names deserve the next round of attention.

> **Why it works:** the wiki preserves what you wrote when you were thinking clearly. The retro compares that against what the market actually did. The trades worth making are exactly the names where the two diverge.

#### ENGINE 02 · Cross-thesis synthesis — portfolio-level pattern detection

Once you have 20+ theses, Claude can do things no spreadsheet can: scan for internal contradictions ("places one note's bull case depends on what another's bear case challenges"), surface hidden macro concentration ("which bull cases share an implicit dependency on AI capex, rates, or China decoupling?"), audit stale assumptions ("for my 10 oldest theses, is the Key Non-consensus Insights section still non-consensus today?"). About 40 of these prompts are catalogued in the User Guide. Each one is structurally impossible without the wiki.

> **Why it works:** the wiki gives Claude an immediate, structured view of every position simultaneously. Pattern matching across that surface is where most portfolio-level alpha hides.

#### ENGINE 03 · Adversarial stress test — pre-mortems on demand

`/stress-test TICKER` reads your thesis as a hostile short-seller and writes from that perspective — attacking the Bull Case, identifying break-the-thesis paths, surfacing risks you've been comfortable ignoring. It does *not* change conviction; it produces the material you'd otherwise avoid generating yourself. Pair with the new-position-build chain (§8) to pressure-test every thesis before promotion to active.

> **Why it works:** you can ask yourself "what could go wrong" and your brain gives the comfortable answer. An adversarial outsider gives you the answer you don't want to hear, which is the one that matters.

The retro engine and synthesis prompts are demonstrated interactively in [§10 Try a skill](#try) and in [User Guide §11 (Prompt Library)](https://github.com/jameswong2011/InvestmentVault/blob/main/User_Guide.md#11-prompt-library).

---

## §3 · Live context engineering

### How the vault keeps Claude aware of your ongoing work.

Large language models are amnesiacs by default. Every new conversation starts from scratch. This vault solves that by storing the agent's "memory" as plain Markdown files that Claude reads at the start of every session — and writes back to as it works.

This is what people in the AI engineering community now call **context engineering** — the practice of structuring an LLM's working environment so it behaves as if it has long-term memory and durable behavior. The vault does this with six files. Three of them are the most important; click any card to inspect.

The six files:

#### `CLAUDE.md` — The rulebook

*What kind of analyst Claude is, every time it shows up.*

Loaded into every session as the system prompt. Sets the entire behavioral contract: writing standards (no hedge words, lead with the insight), the 14-section thesis structure, the 4-section research note structure, the safety tiers, the file-naming conventions.

#### `_hot.md` — Short-term memory

*What you were thinking about yesterday.*

A six-section file that skills update after every operation: Active Research Thread, Latest Sync, Sync Archive, Recent Conviction Changes, Open Questions, Portfolio Snapshot. You read it at the start of a session to resume context; Claude reads it to pick up where you left off.

#### `_graph.md` — The relationships

*Which theses connect to which research notes, and why.*

A dependency map of the whole vault. Per-thesis adjacencies plus reverse indexes. Lets `/sync` know which 3-5 thesis files matter when a new research note lands, without re-reading all 40. The skill that owns this file (`/graph`) keeps it incrementally updated.

#### `_catalyst.md` — Forward calendar

*What's coming up across every position.*

Generated by `/catalyst`. Aggregates earnings dates, regulatory milestones, scheduled product launches across all positions. Answers "what is coming up?" without scanning every thesis individually.

#### `.last_sync` — The watermark

*When was the last propagation?*

A tiny file whose modification time is the watermark. `find -newer .last_sync` returns only changed files, so syncs run in ~30 seconds instead of reading the whole vault every time.

#### `_Archive/Snapshots/` — Undo

*Every destructive edit is reversible.*

Pre-edit copies from every skill that mutates a file. `/rollback` restores any of them. Closure snapshots get 30-day protection. The reason aggressive automation feels safe: mistakes cost a snapshot, not real data.

> **Why this matters in practice.** Without these files, Claude is generic — a stateless model that knows nothing about your portfolio. With them, Claude opens every session already aware of your 40 theses, your last sync, your open questions, and the dependency graph between every note. You stop being a context-provider and start being an analyst with a research team that doesn't forget.

---

## §4 · Architecture map

### The vault as a layered system.

§3 named the six files Claude reads on every session. This is what they look like as a system — how they relate, who writes them, who consumes them, and where data flows when a skill runs. Click any node to see its role, ownership, and the contract it enforces.

*Interactive in the original: a layered map whose nodes open a detail panel. The three layer bands and every node detail follow.*

- **LAYER 1 · RAW SOURCES — IMMUTABLE** — Everything you read. Lands in the vault but Claude never modifies it.
- **LAYER 2 · WIKI — LLM-MAINTAINED** — The structured artifact. Theses, research notes, sectors, plus the runtime state files that hold session memory.
- **LAYER 3 · SCHEMA — OPERATING CONTRACT** — Loaded on every session. Defines how everything else works.

#### `_Inbox/` — Layer 1 · Raw source · Immutable

*Where things land before they become research.*

A staging directory at the vault root. You drop raw inputs here — URLs, PDFs, transcripts, screenshots. Nothing about them is structured yet. `/ingest` reads them, generates a Research note for each, and moves the original to `_Inbox/processed/`.

- **Written by:** You (drop files), /ingest (moves to processed/)
- **Read by:** /ingest

```
_Inbox/
├── acme-q1-2026-transcript.pdf
├── nyt-semiconductor-cycle.html
├── expert-call-2026-05-12.txt
└── processed/
    └── lumentum-cpo-deepdive.pdf
```

#### External sources — Layer 1 · Raw source · Immutable

*The transcripts, articles, filings, calls behind every research note.*

External documents Claude reads but never modifies. The `source:` URL or filename is locked into the resulting Research note frontmatter at creation time and never edited — this is the audit chain that lets you defend an investment decision months later.

- **Written by:** (external — not vault-managed)
- **Read by:** /ingest, /transcript

```
Examples:
https://example.com/acme-q1-2026.html
sell-side-research-2026-05.pdf
expert-call-recording.m4a
sec-filing-10-Q.html

# All get a source: locked into the
# resulting Research note frontmatter.
```

#### Your callouts — Layer 1 · Raw source · Immutable

*The questions and corrections you write inline.*

When Claude writes something you disagree with, you drop a typed callout (`[!question]`, `[!error]`, `[!tip]`, `[!todo]`) right next to the suspect line. The callout is a raw input — it stays unchanged until Claude is asked to address it. After addressing, the callout becomes a Prompt/Response audit block that lives inside the thesis permanently.

- **Written by:** You (Mod+Alt+1..4 in Obsidian)
- **Read by:** /sync, Claude (when asked to address)

```
## Outstanding Questions

Q3 SF2 yield needs to clear 65%...

> [!question] 2026-05-23
Has management given a specific
yield number for Q2, or only
directional commentary?
```

#### `Research/` — Layer 2 · Wiki · LLM-maintained

*One structured note per source. Always opens with the delta.*

Every reading becomes a 4-section note: **Thesis Delta** (what changed for which existing thesis), **Summary**, **Evidence**, **Contradiction Check**. The "delta first" rule means a research note that fails to articulate the delta is a clipping, not research.

- **Written by:** /ingest, /transcript, /stress-test, /surface, /compare, /scenario, /retro, /deepen, /catalyst (sometimes)
- **Read by:** /sync (propagates into Thesis Logs), Manual prompts, /retro

```
---
date: 2026-05-15
source_type: earnings
ticker: ACME
source: https://example.com/...
---
## Thesis Delta
## Summary
## Evidence
## Contradiction Check
```

#### `Theses/` — Layer 2 · Wiki · LLM-maintained

*The 14-section investment case for each ticker.*

The central artifact for every position. Has a chronological `## Log` section (append-only) that records every conviction shift, every sync, every stress test. Two months later `/retro` reads these logs to surface where your written thinking diverged from the market.

- **Written by:** /thesis (creates), /sync (Log appends), /status (conviction/status changes), /stress-test (Log + Outstanding Questions), /deepen (single-section enhancement), /scenario, /prune (closure), /rename, /rollback
- **Read by:** /sync, /brief, /compare, /surface, /retro, /stress-test, /lint, /prune, /graph

```
---
status: active
conviction: medium
ticker: ACME
---
## Summary
## Key Non-consensus Insights
## Bull Case · ## Bear Case
## Conviction Triggers
## Log # append-only
```

#### `Sectors/` — Layer 2 · Wiki · LLM-maintained

*One 11-section overview per sector. Routes the sector-scoped skills.*

Each sector note has an **Active Theses** table — the routing table that every sector-scoped skill reads. The **Investor Heuristics** section forces you to write what consensus believes and where it could be wrong, which is the sector-level analogue of "Key Non-consensus Insights" at the thesis level.

- **Written by:** /sync (Macro Shifts, Competitive Dynamics), /surface, /scenario, /compare, /prune
- **Read by:** /sync, /surface, /compare, /lint

```
---
tags: [sector, moc]
sector: Industrial Automation
---
## Active Theses # routing table
## Key Industry Questions
## Industry History
## Competitive Dynamics
## Investor Heuristics # non-consensus
```

#### `_hot.md` — Layer 2 · Wiki · Runtime state

*Session memory. Six sections, load-bearing schema.*

The short-term memory file. **Six required sections**: Active Research Thread · Latest Sync · Sync Archive · Recent Conviction Changes · Open Questions · Portfolio Snapshot. The schema is load-bearing — missing a section causes silent skill no-ops. Compression drops whole entries, never truncates. Recent Conviction Changes is never compressed (every entry is a high-signal audit record).

- **Written by:** /sync, /surface, /stress-test, /scenario, /compare, /thesis, /deepen, /prune, /status, /rollback, /catalyst, /brief, /rename, /retro
- **Read by:** You (start-of-session resume), All skills (pre-flight context load)

```
## Active Research Thread
- 2026-05-23: ACME Q1 ingested...

## Latest Sync
[propagation results]

## Recent Conviction Changes
# never compressed — audit record
## Open Questions
## Portfolio Snapshot
```

#### `_graph.md` — Layer 2 · Wiki · Runtime state

*Dependency map of every thesis ↔ research relationship.*

A complete dependency map. **Owned exclusively by /graph** (one exception: /rename does a surgical adjacency-header update). Each thesis entry carries `cross-thesis:` adjacencies, `same-sector:` peers, plus cache fields (`status:`, `log_tail:`) so `/sync` can classify changes without re-reading every thesis. Lets /sync find the right 3-5 thesis files for a new research note in 30 seconds instead of scanning all 40.

- **Written by:** /graph (owner), /rename (adjacency header only)
- **Read by:** /sync, /lint, /surface, /compare

```
---
last_graph_write: 2026-05-23T18:42:11Z
---
## ACME
status: active
cross-thesis:
  - PERC (perception layer)
  - RBTX (humanoid peer)
same-sector: [Industrial Automation]
log_tail: [3 most recent prefixes]
```

#### `_catalyst.md` — Layer 2 · Wiki · Runtime state

*Forward calendar of earnings dates, rulings, launches.*

Regenerated on each `/catalyst` run. Timeline: next 2 weeks daily · weeks 3-4 weekly · months 2-3 by week. Flags catalyst gaps (theses with no upcoming events) and stale events. Pre-regenerate snapshot makes web-search failure safely recoverable via `/rollback`.

- **Written by:** /catalyst (owner)
- **Read by:** You (forward planning), /lint

```
# Catalyst Calendar — 2026-05-23
## Next 2 weeks
- 2026-05-28: ACME Q1 earnings
- 2026-05-30: TSMC capex update

## Weeks 3-4
- 2026-06-09: Düsseldorf ruling

## Catalyst gaps
- RBTX — no catalysts in next 90d
```

#### `_Archive/Snapshots/` — Layer 2 · Wiki · Runtime state

*Every destructive edit is reversible.*

Pre-edit copies written before any destructive operation. Batch ID is `<trigger>-YYYY-MM-DD-HHMMSS` (second-precision). Closure snapshots get a 30-day floor that no /clean mode can override — the "regret-recovery window". This is why aggressive automation feels safe: mistakes cost a snapshot, not real data.

- **Written by:** /sync (Tier A), /deepen, /status, /compare, /prune, /catalyst, /rollback, /rename
- **Read by:** /rollback (restore), /clean (delete with floors)

```
_Archive/Snapshots/
├── ACME (pre-sync 2026-05-23-2214).md
├── ACME (pre-stress 2026-05-23-1832).md
├── PERC (pre-status 2026-05-22-0941).md
└── _sync-manifest (sync-2026-05-23-2214).md
    # multi-file manifest
```

#### `CLAUDE.md` — Layer 3 · Schema · Operating contract

*Loaded as the system prompt every session.*

The behavioral contract. Defines **writing standards** (lead with the insight, no hedge words, tables over prose), the **14-section thesis structure**, the **4-section research note structure**, **safety tiers** (Tier-3 confirmation gate on conviction changes), file-naming conventions. Edit this file and the behavior of every future skill run changes — no retraining needed.

- **Written by:** You (manually)
- **Read by:** Claude (every session, loaded as system prompt)

```
# Investment Vault — CLAUDE.md
## Writing standards
- Lead with the insight
- No hedge words
- Tables > prose for comparisons

## Thesis structure (14 sections)
1. Summary
2. Key Non-consensus Insights
...

## Safety tiers
```

#### `Templates/` — Layer 3 · Schema · Operating contract

*Four note skeletons that enforce structure.*

One Markdown file per note type: **thesis**, **research**, **sector**, **macro**. Every `/thesis` and `/ingest` run uses the relevant template as the starting skeleton. The structure is rigid by design — sections you would skip on a bad day get filled in regardless.

- **Written by:** You (modify to match your house style)
- **Read by:** /thesis, /ingest, /transcript, /scenario

```
Templates/
├── thesis-template.md   # 14 sections
├── research-template.md # 4 sections
├── sector-template.md   # 11 sections
├── macro-template.md
└── _callouts/  # inline-callout snippets
```

#### `.claude/skills/` — Layer 3 · Schema · Operating contract

*Twenty-one deterministic specifications.*

Each skill is a `SKILL.md` file that tells Claude exactly what to do, step by step — pre-flight checks, the procedure, exit conditions. Skills are **specifications, not prompts**: same command, same output, every time. Each skill declares its **lock scope** (vault-wide or ticker-scoped), its `_hot.md` write contract, its model assignment (Opus or Sonnet), and whether it forks to a subagent. The specs are plain text — read them to understand any behavior.

- **Written by:** You (when editing or authoring a skill)
- **Read by:** Claude (on each skill invocation)

```
.claude/skills/
├── sync/SKILL.md
├── stress-test/SKILL.md
├── retro/SKILL.md
├── thesis/SKILL.md
├── ...
└── _shared/  # cross-skill contracts
    ├── preflight.md
    ├── log-prefixes.md
    └── wikilink-forms.md
```

Deeper architectural reference (per-skill lock scope, manifest contracts, the 12 critical invariants, runtime markers): [INFRASTRUCTURE.md](https://github.com/jameswong2011/InvestmentVault/blob/main/INFRASTRUCTURE.md).

---

## §5 · Templates & writing standards

### How the vault enforces good research habits.

Context engineering tells Claude what state to keep in mind. Templates and writing standards tell Claude how the output has to look. Together they make hundreds of notes written over years feel like they came from the same disciplined analyst.

### Templates: skeletons that enforce structure

The `Templates/` folder contains one Markdown file per note type — thesis, research, sector, macro. Every time you run `/thesis TICKER` or `/ingest [URL]`, the relevant template is used as the starting skeleton. The structure is rigid by design: sections you'd skip on a bad day get filled in regardless.

A look at the four required sections of every research note:

```yaml
---
date: YYYY-MM-DD
source_type: earnings | analyst-report | news | deep-dive | data | video-transcript
ticker: TICKER
source: https://... # immutable; never edited after creation
---
## Thesis Delta # Lead with what this source changes for the existing thesis
## Summary # 1-4 paragraphs capturing the source's argument
## Evidence # Data points, tables, quotes — sparingly
## Contradiction Check# What this source contradicts vs. existing thesis assumptions
```

The "Thesis Delta first" rule matters. Every read opens with what changed for an existing thesis — not a business description. Without this rule, research notes end up restating the company every time and burying the insight. Same goes for "Contradiction Check": forcing yourself to write what an article contradicts is what kills confirmation bias.

### Writing standards in CLAUDE.md

These rules ship as part of the system prompt. Claude follows them on every output — every section it writes, every Log entry, every research note summary.

- **Lead with the insight** — Never with context the reader already has. The first sentence of any section earns its place with a data point, an insight, or a specific claim.
- **No hedge words** — Banned: "importantly", "notably", "significantly", "it's worth noting", "interestingly", "crucially". Each one signals padding around a weak claim.
- **Tables over prose for comparison** — If you're comparing things, the answer is a table. Prose comparisons are slow to read and easy to game.
- **Log entries cap at 2 lines** — Format: `[source/trigger]: [what changed] — [conviction impact: unchanged/strengthened/weakened + 1 reason]`. Anything longer is moved to the body section.
- **Research notes lead with delta, not description** — For existing theses: never restate what the company does. Open with what just changed.
- **Cut connective tissue** — Every sentence earns its place with a data point, an insight, or a specific claim. No transitional padding.

Editing these rules in CLAUDE.md doesn't just affect one chat — it changes how every future skill run and every future manual prompt behaves. The behavior is configurable without retraining.

---

## §6 · The thesis as a forcing function

### Fourteen sections, each one doing a job.

Most research notes are unstructured prose. That's fine for personal scribbling but terrible for analysis you'll need to defend in six months. Each section here exists because skipping it is exactly how analysts get blindsided.

Browse the synthetic ACME thesis below. The Sector tab shows the parallel 11-section structure that overlays the thesis layer. Expand any section to see what work that section forces you to do.

*Interactive in the original: three tabbed sample notes, each section expandable. All three are reproduced below.*

### Sample note — `Theses/ACME - Acme Robotics.md`

```yaml
---
date: 2026-05-23
tags: [thesis, industrial-automation, hardware]
status: active
conviction: medium
sector: Industrial Automation
ticker: ACME
source: synthetic-demo
---
```

#### 1. Summary

ACME manufactures industrial humanoid robots for warehouse picking. It undercuts human labor cost by ~60% at scale with a tightly-integrated hardware/software stack. 2026 shipments tracking 4,800 vs guide 4,000 (+20% beat); ASP holding above $75K. Conviction is **medium** pending SF2 manufacturing yield through Q3.

> **What this section forces:** if you can't say what the company does and why it matters in one paragraph, you don't have a thesis — you have notes.

#### 2. Key Non-consensus Insights

1. **Bundled hardware-software is the moat, not friction.** Most competitors sell either the robot or the software; ACME bundles a closed stack with 94% picking accuracy vs 81% sector median.
2. **EU labor regulation forces adoption.** The 2026 Düsseldorf Accord caps warehouse shift length and forces a 1.4× wage uplift.
3. **Mid-tier ASP discipline.** Refusing to compete below $50K preserves margin while peers race to commodity volume.

> **This is where your alpha lives.** Consensus is already priced. Every insight here must specifically articulate what the market believes and where you think they're wrong. If you can't, the position is just beta.

#### 3. Outstanding Questions

1. Can SF2 manufacturing achieve >65% yield by Q3 2026? Current 51% requires a Q2 process inflection that has slipped twice.
2. How durable is the picking-accuracy lead if competitors close the hardware-software unbundling gap?
3. What is the regulatory tail if the Düsseldorf Accord is challenged in court?

> **The questions you'd be afraid to ask if you had to defend this thesis.** Writing them down forces you to live with them.

#### 4. Business Model & Product Description

Robot + perception stack + warehouse-management integration sold as a unified platform. Subscription tier (ACME Conduct) adds remote tele-supervision for edge cases. Hardware gross margin ~38%; software gross margin >75%.

#### 5. Industry Context

Industrial humanoid TAM 2026E $14B → 2030E $58B per consensus, with bull scenarios materially higher under EU regulatory tailwinds. See `[[Sectors/Industrial Automation]]`.

#### 6. Key Metrics

| Metric | Value | Notes |
| --- | --- | --- |
| Market Cap | $18.2B | −22% from 52-wk high |
| EV/Revenue (NTM) | 8.4× | vs sector median 5.1× |
| Revenue Growth (YoY) | +85% | accelerating from +71% in 2025 |
| Gross Margin | 38% | guide 42–45% post SF2 ramp |
| FCF Yield | −2.1% | reinvestment phase through 2027 |

#### 7. Bull Case

SF2 yield clears 65% by Q3; Düsseldorf Accord enforcement holds; hardware-software bundle stays defensible through 2027. The stock re-rates to peer median EV/Rev as GM trajectory clears 42%.

#### 8. Bear Case

SF2 ramp slips again; competitors close the picking-accuracy gap via open-stack software; mid-tier ASP discipline breaks under volume pressure. GM stalls in low-30s; multiple compresses.

> **The section everyone wants to skip.** The Bull Case writes itself when you like the name. The Bear Case is where the work is. The template enforces it because it's exactly the section that finds your blind spots.

#### 9. Catalysts

- **Q3 2026 earnings** — SF2 yield disclosure (binary)
- **Düsseldorf Accord challenge** — German Constitutional Court ruling, H2 2026
- **Competitor launches** — peer humanoid releases H2 2026

#### 10. Risks

- Yield risk — SF2 process inflection has slipped twice already
- Regulatory risk — Accord challenged in court
- Competitive risk — open-stack unbundling closes the accuracy gap
- Capital risk — reinvestment phase consumes FCF through 2027

#### 11. Conviction Triggers

- → HIGH if SF2 yield exceeds 65% AND Q3 GM > 42%
- → LOW if Q3 unit shipments miss guide by >15% OR competitor breakthrough on hardware-software unbundling
- → CLOSE if EU Accord challenged in court AND labor cost arbitrage compresses below 30%

> **Pre-committed if-then statements.** Today you write down what would change your mind. Six months from now you check whether reality crossed any of these lines — you don't have to renegotiate conviction in the moment.

#### 12. Related Research

- `[[Research/2026-05-15 - ACME - Q1 2026 Earnings]]`
- `[[Research/2026-05-12 - Industrial Automation - Düsseldorf Accord Update]]`
- `[[Research/2026-04-08 - ACME - SF2 Yield Stress Test]]`

#### 13. Legacy Callouts

Auto-managed archive of callouts older than 180 days. Read-only. Empty for this synthetic example.

#### 14. Log

### 2026-05-23  
- Ingested: Q1 transcript — units beat by 33%, GM flat; strengthened, scaling pathway intact### 2026-05-15  
- Stress test: identified SF2 yield risk; conviction unchanged, added to Outstanding Questions### 2026-05-12  
- Manual edit: refined Düsseldorf Accord framing in Industry Context### 2026-04-08  
- Status change: conviction low→medium — Q4 GM beat (+520bps) clears bear-case floor

> **The audit trail that makes the rest of the system work.** Every conviction shift gets a Log entry. `/retro` reads these to rank trade ideas by narrative-price gap.

### Sample note — `Research/2026-05-15 - ACME - Q1 Earnings.md`

```yaml
---
date: 2026-05-15
source_type: earnings
ticker: ACME
sector: Industrial Automation
source: synthetic-demo
---
```

#### 1. Thesis Delta

Q1 unit shipments 1,200 vs guide 800–1,000 (+33% beat). Strengthens Bull Case bullet #1 (scaling pathway). ASP −15% YoY but ABOVE the bear-case floor of $70K. Conviction unchanged; SF2 yield commentary still vague.

> **Every research note opens with this.** Not a business description — the specific delta this source produced for the existing thesis. If a note can't articulate the delta, it's a clipping, not research.

#### 2. Summary

ACME reported Q1 2026 revenue +85% YoY to $124M. Management emphasised SF2 ramp will deliver "structural margin inflection" in H2, declining to commit to a specific yield number despite repeated analyst probing.

#### 3. Evidence

| Metric | Q1 25 | Q1 26 | Delta |
| --- | --- | --- | --- |
| Units shipped | 320 | 1,200 | +275% |
| ASP ($K) | 89 | 76 | −15% |
| Revenue ($M) | 67 | 124 | +85% |
| Gross Margin | 31% | 38% | +700 bps |
| Backlog (units) | 1,800 | 6,200 | +244% |

#### 4. Contradiction Check

The +700 bps GM expansion partially contradicts Bear Case bullet 2 ("ACME's margin trajectory will stall as competitors flood the mid-tier"). Hold the contradiction in tension — competitor pressure is at the <$50K ASP tier, which ACME doesn't serve. Bear case more accurately re-framed as TAM-ceiling, not margin-compression risk.

> **The section that catches confirmation bias.** Every Research note must explicitly check what the new evidence contradicts. Without this section, every reading reinforces the existing view by default.

### Sample note — `Sectors/Industrial Automation.md`

```yaml
---
date: 2026-05-23
tags: [sector, moc]
sector: Industrial Automation
source: synthetic-demo
---
```

#### 1. Active Theses

| Ticker | Conviction | Status |
| --- | --- | --- |
| `[[Theses/ACME - Acme Robotics|ACME]]` | medium | active |
| `[[Theses/RBTX - Robotix Systems|RBTX]]` | low | monitoring |
| `[[Theses/PERC - Perception AI|PERC]]` | high | active |

> **The sector note is a map.** The Active Theses table is the routing table — every sector-scoped skill reads it. Putting it first means "open the sector note" answers "what am I positioned for here?" in one glance.

#### 2. Key Industry Questions

1. Is humanoid robotics a 5-year capex super-cycle or a 15-year infrastructure build-out? The duration of the cycle determines whether to position for re-rating now or compound at peak rates over a decade.
2. Does the EU Düsseldorf Accord set a precedent that the US adopts? US labor regulation has historically followed EU lead with a 4–7 year delay. If it does, ROI curves shift before consensus expects.
3. How concentrated does the value chain become as humanoid + perception converge? Does the integrator win (ACME, RBTX), or does the perception layer (PERC) extract most of the rent?

> **The three questions you'd lose sleep over if this were your only sector.** They drive what research gets prioritised and what catalysts get watched.

#### 3. Industry History

**2010–2018 — Stationary robotics era.** Industrial robots dominated by fixed-position arms (Kuka, Fanuc, ABB). High capex, long install, narrow use case. Pricing power concentrated in industrial-grade brands; volumes consolidated.

**2018–2023 — Wheeled AMR / collaborative robotics.** Wheeled mobile robots (Locus, Geek+) entered DCs. Collaborative arms (Universal Robots) extended to mid-size facilities. Software margin emerged as a distinct moat.

**2023–2025 — Humanoid emergence.** Figure, 1X, Apptronik, Agility took humanoid out of lab demos. Tesla Optimus reset the cost curve. Foundation model integration (Google RT-2, NVIDIA GR00T) gave robots general-purpose perception.

**2026 — Pricing power inflection.** Hardware-software integrators (ACME, RBTX) re-aggregate pricing power. Commodity hardware tier emerges. ASP discipline at $70K+ becomes the moat.

#### 4. Competitive Dynamics

| Player | Pricing power trajectory | Strategic stance |
| --- | --- | --- |
| ACME | High and durable | Integrated hardware-software stack |
| RBTX | Compressing | Hardware-only, racing to volume |
| PERC | Growing fast | Software layer across third-party hardware |
| Generic Asian OEMs | Race to floor | Sub-$50K commodity tier |

Current dynamics: incumbent durability is high in the integrated tier but weak in commodity. New entrant threats come almost entirely from the perception layer trying to disaggregate the bundle. Pricing power is trajectory-divergent — ACME's hardware-software lock-in is consolidating margin at the high end while commodity hardware compresses.

#### 5. Product-Level Analysis

**ACME H1 (the flagship).** Bimanual humanoid, $75K ASP, 94% picking accuracy at human-comparable cycle times. Closed perception stack (proprietary VLM). Target: warehouse picking at mid-to-large DCs (5,000+ sqm). Why it sells: integrated install, 12-month payback at EU labor costs, retraining-by-demonstration cuts deployment time 80%.

**RBTX Worker.** Wheeled mobile + arm. $42K ASP, 78% picking accuracy. Open-stack — integrates with Boston Dynamics, NVIDIA Isaac, third-party perception. Why it sells: cheaper, flexible, but requires more system-integration work; favored by 3PLs that already have software competence.

**PERC Atlas SDK.** Perception layer SaaS. $24K/year per robot subscription. Why it sells: bring-your-own-hardware, lets integrators add 90%+ picking accuracy to commodity arms. Threatens the ACME bundle.

#### 6. Acquisitions & New Entrants

**Historical M&A.** Amazon → Kiva (2012, $775M) — defined the AMR category. Boston Dynamics → Hyundai (2020, $1.1B) — fueled humanoid R&D. Apple → Drive.ai (2019) — perception talent acquihire that ultimately leaked into multiple competitors.

**2025–2026 entrants.** Two well-funded humanoid startups (Reflex, Trine) seeking Series D at $4B+ pre-money. Both target the <$50K commodity tier — direct threat to RBTX, indirect threat to ACME if they vertically integrate.

#### 7. Macro Shifts

EU Düsseldorf Accord (2026) is the largest exogenous tailwind — see `[[Macro & Technology/Düsseldorf Accord]]`. US tariff response watched but not yet active; Chinese export-control regime on perception silicon (Q4 2025) constrains supply.

Second-order effect on labor-intensive 3PL: shift-length caps materially impair operating leverage at high-volume DCs. Logistek (3PL) trades as defensive — likely a sector short opposite ACME long.

#### 8. Investor Heuristics

**What consensus believes:** EU labor regulation is "fully priced in" by mid-2026; humanoid is a 5-year hype cycle that will normalise to industrial-robotics multiples; commodity tier expansion will compress all margins.

**Where consensus could be wrong:**

1. *Enforcement timing.* Düsseldorf Accord enforcement starts H2 2026; consensus assumed delay. Earlier enforcement compresses ROI payback below 9 months.
2. *Bundling durability.* Consensus reads integrated hardware-software as "bundling friction"; vault thesis reads it as the moat. Picking-accuracy gap of 1300bps is empirical, not narrative.
3. *Court-challenge tail risk.* Consensus treats Accord challenge as binary. Vault view: even an adverse ruling delays enforcement 18 months — not invalidates.

> **This is where sector-level alpha emerges.** Writing down what consensus believes — then specifically articulating where consensus could be wrong — is the sector-level analogue of "Key Non-consensus Insights" at the thesis level.

#### 9. Related Research

- `[[Research/2026-05-15 - ACME - Q1 2026 Earnings]]`
- `[[Research/2026-05-12 - Industrial Automation - Düsseldorf Accord Update]]`
- `[[Research/2026-04-22 - PERC - Atlas SDK Launch]]`
- `[[Research/2026-03-15 - Industrial Automation - Capex Cycle Decomposition]]`

#### 10. Legacy Callouts

Auto-managed archive of callouts older than 180 days. Read-only.

#### 11. Log

### 2026-05-23  
- /sync: refreshed Macro Shifts; ACME Q1 propagated into competitive dynamics table### 2026-04-22  
- /surface [Industrial Automation]: identified PERC SDK as commoditising threat to ACME bundle### 2026-03-15  
- Manual edit: revised Industry History to reflect 2023–2025 humanoid emergence; strengthened, pricing power inflection thesis### 2025-12-08  
- /thesis ACME: added to Active Theses (status: active, conviction: medium)

---

## §7 · Skills — concept & catalogue

### The verbs Claude can run on the vault.

Skills are how you actually do work in the vault. Every command you type — `/sync`, `/stress-test`, `/retro` — invokes one. They are the moving parts that turn the static notes into a working system.

### What a skill is

A skill is a plain Markdown file at `.claude/skills/<name>/SKILL.md` that tells Claude exactly what to do, step by step. It is not a prompt — prompts are improvisational. A skill is a specification: pre-flight checks, the procedure, exit conditions. Claude follows it literally.

Three things follow from this design:

- **Same input, same output.** A skill behaves the same way regardless of model temperature or how the conversation went before. This is what makes the system reliable for actual investment decisions instead of being a fancy chat toy.
- **The specification is the source of truth.** If a skill misbehaves, you edit the SKILL.md file. There's no opaque model state to debug.
- **You can read the spec.** Every skill is plain text. If you want to know why `/sync` propagates conviction changes the way it does, you open its SKILL.md and read.

### The 21 skills, four families

Each family corresponds to a different role: **Core** moves information through the vault, **Analytical** generates insight, **Building** creates or extends theses, **Maintenance** keeps the substrate healthy.

#### ● Core (4)

- `/ingest` — URL / file / batch → structured Research notes with same-source dedup.
- `/sync` — Propagate research to theses / sectors / macro / _hot.md (3 modes).
- `/status` — Conviction / status changes with Tier-3 confirmation gate.
- `/graph` — Rebuild dependency map (full · last · catch-up N days).

#### ◆ Analytical (7)

- `/surface` — Find new ideas + blind spots. Forks to subagent, 4 scopes.
- `/stress-test` — Adversarial short-seller review of a thesis.
- `/scenario` — "What if X" propagated through portfolio with impact tagging.
- `/compare` — Side-by-side competitive analysis (2+ tickers).
- `/catalyst` — Refresh _catalyst.md with web-searched earnings dates.
- `/retro` — 1w / 1m / 1q backward review · narrative-price gap ranking.
- `/transcript` — Pull earnings transcript; extract thesis-delta-first note.

#### ▲ Building (4)

- `/thesis` — New thesis · draft · 14 sections · archive-collision detection.
- `/deepen` — Surgical single-section enhancement (never a full rewrite).
- `/brief` — 1-page IC memo · read-only on the thesis.
- `/numbers` — Refresh Key Metrics table from financial-data API.

#### ◐ Maintenance (6)

- `/lint` — Health check: structural, freshness, analytical · forks subagent.
- `/prune` — Evaluate weak theses for upgrade / monitor / close.
- `/clean` — Purge old snapshots with safety nets.
- `/archive-callouts` — Sweep ≥180d addressed callouts to Legacy.
- `/rollback` — Restore from snapshot · cascade detection.
- `/rename` — Company name change · atomic across all wikilinks.

Full reference with arguments, side effects, and follow-up chains: [User Guide §5](https://github.com/jameswong2011/InvestmentVault/blob/main/User_Guide.md#5-skill-reference).

---

## §8 · A day in the life

### What working with the vault actually looks like.

No big ceremony. You open Obsidian, type a command, and a few seconds later you have structured output. Here are the two routines that account for most of the use: a morning ingest run and a Friday-evening retro.

*Interactive in the original: two step-through loop diagrams. Both are reproduced below.*

### A morning: process new info

`You read → /ingest → /sync → You react → /sync (again) → Done`

1. **You read something** — A transcript, an article, a substack post. You drop the URL or file into _Inbox/. Nothing has changed in the vault yet.
2. **/ingest** — Claude reads the source, creates a Research note with four sections (Thesis Delta, Summary, Evidence, Contradiction Check), and wikilinks it to every related thesis it finds.
3. **/sync** — The new research flows into the affected thesis Logs, the sector overview, and _hot.md. Five minutes after you started reading, every relevant thesis knows about this source.
4. **You react** — Open the updated thesis. Drop callouts wherever Claude wrote something you disagree with. Edit the body where you want to refine the argument yourself.
5. **/sync (again)** — Your reactions and callouts flow downstream too. The Log records what you addressed and why; sector and macro notes pick up the implications.
6. **Done** — Your thesis reflects what you just read. Two months from now Claude will still know what you concluded today.

### An evening: review the week

`/retro 1w → Review → /stress-test → /sync → Done`

1. **/retro 1w** — Run weekly. Claude reads every Log entry, callout, and conviction shift from the past 7 days. Overlays each ticker with actual price moves and news flow. Ranks every position by narrative-price gap.
2. **Review** — Read the retro report. Top trade ideas are usually inverted signals — names where news said one thing and price said the opposite. Decide which to act on.
3. **Pick your move** — /stress-test if you suspect your view needs an adversarial check. /deepen if a section is weak. /status if you have enough conviction to formally change your position.
4. **/sync** — Commit the decisions. Conviction changes propagate to sector overviews, your portfolio snapshot, and the Recent Conviction Changes log.
5. **Done** — Next Monday starts with a clean view: what you decided, what you deferred, and what the retro flagged that you haven't addressed.

---

## §9 · Workflows map

### Six chains that cover most of what you'll ever do.

§7 catalogued the 21 skills individually. Real work is rarely a single skill — it's a chain of them. The map below shows the six most common chains, all overlaid on the same skill graph. Click any tab to highlight that chain; the sequence appears at the bottom.

*Interactive in the original: six chains overlaid on one skill graph. Each chain is listed below.*

#### New position from scratch

Friend mentions a company you don't cover. By the end of the evening you want a stress-tested, active thesis propagated to its sector.

`/thesis TICKER` → `/stress-test TICKER` → `/status TICKER draft→active` → `/sync TICKER`

Optional: /compare TICKER vs PEER before /sync for competitive context, or /deepen TICKER [section] to fill gaps the stress test flagged.

#### Earnings reaction

A thesis company just reported. You want the transcript ingested, the thesis updated, and conviction adjusted if warranted.

`/ingest [transcript URL]` → `/sync TICKER` → `/status TICKER conviction old→new`

/status only runs if conviction actually changed. If ambiguous, slot /stress-test TICKER between /sync and /status to pressure-test the read before committing.

#### Conviction drift response

/sync flagged ⚠️ Conviction drift — 4 of 5 recent updates pushed back on the Bull Case. Either confirm or downgrade.

`/stress-test TICKER` → `/deepen TICKER [weakest section]` → `/status TICKER conviction old→new` → `/sync TICKER`

If the stress test reaffirms the thesis: skip /deepen, run /status TICKER reaffirm instead. The reaffirm becomes a permanent Log entry — useful audit when /retro reads back conviction stability six months later.

#### Macro shock propagation

Rate decision, geopolitical event, policy change. You want the implications propagated across every position the event touches.

`/scenario [event with quantitative parameters]` → `/compare [exposed] vs [beneficiary]` → `/status [most affected] conviction old→new` → `/sync`

/scenario propagates the event implications across every thesis it touches; /compare is optional but useful when competitive dynamics shift (e.g., one company is hurt and another benefits from the same event).

#### Sector deep-dive

Entering or re-evaluating a whole sector. Discover what's in the vault already, find gaps, build the new theses.

`/surface [sector]` → `/compare [key players]` → `/thesis TICKER (per new opportunity)` → `/status TICKER draft→active` → `/sync`

Promote each new thesis to active *before* rebuilding the graph — draft theses are intentionally omitted from sector Active Theses tables and will be invisible to subsequent /surface [sector] runs.

#### Weekly retrospective

Friday evening. Run /retro on the past week, read the narrative-price gap ranking, decide which positions deserve a stress test or a deepen.

`/retro 1w` → `/stress-test TICKER (per top-ranked alpha candidate)` → `/deepen TICKER (per missed-signal candidate)`

The retro never auto-changes conviction. It produces a ranked trade-idea list — alpha harvest candidates, missed signals, stress-test candidates. You decide which to act on. Final /sync commits the decisions.

Full chain index (with optional branches, failure-mode footnotes, and ~30 less-common scenarios): [User Guide §3 (Workflow Chains)](https://github.com/jameswong2011/InvestmentVault/blob/main/User_Guide.md#3-workflow-chains) and the ["I want to ___"](https://github.com/jameswong2011/InvestmentVault/blob/main/User_Guide.md#4-decision-guide--i-want-to) intent map in §4.

---

## §10 · Inline callouts

### A way to push back without losing the exchange.

When Claude writes something you don't agree with, you don't argue in chat — you drop a callout right next to the suspect sentence. Later, ask Claude to address fresh callouts and the back-and-forth becomes a permanent record inside the thesis.

Four types, each with its own hotkey: `[!question]` (Mod+Alt+1, ask), `[!error]` (Mod+Alt+2, flag), `[!tip]` (Mod+Alt+3, suggest), `[!todo]` (Mod+Alt+4, action). Use the right type and the system can later tell you "you've raised four `[!error]` callouts on this name in the past month — your conviction is drifting whether you've noticed or not." See [User Guide §6](https://github.com/jameswong2011/InvestmentVault/blob/main/User_Guide.md#6-inline-callouts--user-feedback-markers) for the full callout specification.

#### 1. Drop a callout

Hit `Mod+Alt+1` to ask a question, `2` to flag an error, `3` for a tip, `4` for a todo. The callout lands right next to the line that bothered you.

```markdown
## Outstanding Questions
Q3 SF2 yield needs to clear 65% to validate the H2 GM guide. Current 51% requires a Q2 process inflection that has slipped twice.

> [!question] 2026-05-23
Has management given a specific yield number for Q2, or only directional commentary? The slip pattern means we need a concrete threshold to disconfirm.
```

*You hit Mod+Alt+1 in Obsidian. A question callout drops right below the paragraph that bothered you. The thesis still reads cleanly — you've added a comment, not torn anything apart.*

#### 2. Ask Claude to address it

"Address fresh callouts in [[Theses/ACME]]." Claude rewrites the body where needed and leaves a Prompt/Response audit block in place of the original callout.

```markdown
## Outstanding Questions
Q3 SF2 yield needs to clear 65% to validate the H2 GM guide. Management committed to a 58% interim yield target by end-Q2 on the Q1 call (May 14); a miss against THAT number — not the Q3 65% — is the earliest disconfirming signal.

> [!question] 2026-05-23 → Addressed 2026-05-23
PROMPT: Has management given a specific yield number for Q2, or only directional commentary?
RESPONSE: Integrated the 58% interim threshold from the Q1 call into the section above. Full edit lives in the body; this block preserves the exchange.
```

*You ask Claude to address fresh callouts. The body gets updated; the callout becomes a Prompt/Response audit block.*

#### 3. Pin the ones worth revisiting

Add `[[pinned]]` to mark a callout as something to re-address whenever new data lands — a competitor announcement to watch, a quarterly question to keep asking.

```markdown
## Conviction Triggers
→ LOW if Q3 unit shipments miss guide by >15% OR competitor breakthrough on hardware-software unbundling.

> [!todo] 2026-05-23 [[pinned]] → Addressed 2026-05-23
PROMPT: Track competitor announcements quarterly for hardware-software unbundling signals. Re-address when meaningful news lands.
RESPONSE: Set as a recurring revisit slot. Will re-address with current data on next request. As of 2026-05-20: no qualifying competitor announcements.
```

*Add `[[pinned]]` to mark a callout you want to keep alive. It becomes a recurring question.*

#### 4. The audit trail compounds

Six months later, you can see exactly which arguments you pushed back on, what Claude wrote in response, and how your conviction evolved as the evidence came in.

```markdown
## Legacy Callouts

- [2025-11-12 → Addressed 2025-11-13] Q3 unit shipments tracking — resolved (beat guide by 12%)
- [2025-10-04 → Addressed 2025-10-05] Bear Case revision request — resolved
- [2025-09-22 → Addressed 2025-09-22] Düsseldorf Accord scope clarification — resolved
```

*After 180 days, addressed callouts (without [[pinned]]) get swept into a Legacy Callouts archive.*

---

## §11 · Try a skill

### What running a skill actually looks like.

Each of these is a canned trace — the same kind of output a real session produces on this synthetic ACME thesis. Pick a skill and watch the deterministic output stream past.

*Interactive in the original: a terminal simulator (`claude-code — claudian-vault`). All output is canned and deterministic — same skill, same trace. No API calls, no live data. Fictional ACME — Acme Robotics.*

#### `/ingest [transcript]`

```console
$ /ingest https://example.com/acme-q1-2026-transcript

[Step 1] Fetching source via defuddle extractor
         ✓ 11,420 words extracted · earnings transcript
[Step 2] Checking the vault for context
         · ticker ACME found in 1 thesis · 3 prior research notes
         · sector: Industrial Automation
[Step 3] Writing a Research note
         + Research/2026-05-15 - ACME - Q1 2026 Earnings.md
           Thesis Delta · Summary · Evidence · Contradiction Check
[Step 4] Archiving the source
         ✓ source moved to _Inbox/processed/

[Done] 1 Research note created.
       Next: /sync ACME to flow it into the thesis.
```

#### `/sync ACME`

```console
$ /sync ACME

[Step 1] Reading what's new since last sync
         · 1 new research note found (Q1 earnings)
[Step 2] Working out which files matter
         · Theses/ACME (direct)
         · Sectors/Industrial Automation (parent)
         · _hot.md (your session cache)
[Step 3] Snapshotting before editing
         · ACME (pre-sync 2026-05-23-2214).md saved
[Step 4] Propagating the changes
         ~ Theses/ACME — appended Log entry
         ~ Theses/ACME — refreshed Catalysts table
         ~ Sectors/Industrial Automation — updated Macro Shifts
         ~ _hot.md — added Active Research Thread entry
[Step 5] Checking for conviction drift
         ⚠ 3 of 5 recent updates have flagged headwinds
           Consider /status ACME conviction medium→low

[Done] 2 files modified · 2 snapshots created.
       Next: review the drift signal, then /graph last.
```

#### `/stress-test ACME`

```console
$ /stress-test ACME

[Step 1] Reading the thesis + recent Research (last 90 days)
         · 1 thesis · 8 research notes loaded
[Step 2] Generating the short-seller view
         Hostile reading along five axes:
         · technology risk          · competitive moat decay
         · regulatory reversal      · capital structure stress
         · management credibility
[Step 3] Writing the adversarial note
         + Research/2026-05-23 - ACME - Stress Test.md
           Identified 3 distinct break-the-thesis paths
           Strongest: SF2 yield trajectory + EU regulatory tail
[Step 4] Appending to the thesis Log
         + Theses/ACME ## Log:
           "Stress test: identified SF2 yield risk + EU regulatory tail;
            conviction unchanged, added 2 entries to Outstanding Questions"

[Done] Stress test complete. Conviction not auto-changed.
       Next: read the Outstanding Questions. /status reaffirm or change.
```

#### `/retro 1w`

```console
$ /retro 1w

[Step 1] Aggregating the week (subagent fork)
         · 23 Log entries · 8 addressed callouts · 4 fresh callouts
         · 17 tickers touched
[Step 2] Overlaying price and news per ticker
         · price moves (±3% threshold)
         · newsflow polarity (PR, guidance, M&A)
         · earnings results (beat/miss + guide direction)
[Step 3] Classifying — narrative × news × price
         5 aligned-up    · weight 0    · already priced
         3 aligned-down  · weight 0    · already priced
         4 inverted-bull · weight 1.5× · positioning unwinds
         3 inverted-bear · weight 1.5× · forward-risk signals
         1 unreactive-good · weight 2× · catalyst dismissed
         1 unreactive-bad  · weight 2× · bear case ignored
[Step 4] Ranking the top 3 trade ideas
         1. ACME    · inverted-bear · alpha harvest candidate
         2. NEWCO   · unreactive-bad · stress-test candidate
         3. PERC    · inverted-bull · missed-signal candidate
[Step 5] Writing the retro note + Log entries
         + Research/2026-05-23 - Retrospective 1w - Synthesis.md
         + Theses/ACME Log: "Retro insight: alpha harvest candidate..."
         + Theses/NEWCO Log: "Retro insight: stress-test candidate..."
         + Theses/PERC Log: "Retro insight: missed-signal candidate..."

[Done] Retro complete. Read the synthesis note.
       Next: act on the top 3 ideas per the §3.6 chain in User Guide.
```

---

## §12 · FAQ

### Questions you'd ask if a friend pitched this to you.

#### Isn't this just RAG with extra steps?

No. RAG is retrieval-augmented generation against a static index. The vault is a **stateful, structured, mutually-aware** set of notes that Claude both reads and writes through deterministic workflows.

RAG retrieves passages to inform a single response. The vault is the agent's working memory — its content gets mutated continuously by skills like `/sync` and `/graph` as part of the operating loop. RAG retrieves; this system retrieves, edits, propagates, snapshots, and audits.

#### How is this different from just using ChatGPT?

ChatGPT has no persistent memory of your portfolio. Every conversation starts from zero. You re-paste the transcript, re-explain the company, re-summarise your context — the expensive work of building up forty positions over two years never accumulates because nothing persists.

This vault is the opposite. Claude wakes up every session already knowing your forty theses, your most recent conviction shifts, every callout you've ever dropped, every contradiction you've already spotted ([§3](#context)). You stop being a context-provider and start being an analyst with a research team that doesn't forget.

#### Do I need to be a programmer?

No. You install Obsidian (free), install Claude Code (a CLI for Claude), clone the vault repo, and start typing skill commands. Setup is closer to installing a Notion template than writing software. The 21 skills ([§6](#skills)) are pre-built — you just call them.

You will, however, have to be the kind of person who's comfortable typing `/sync ACME` instead of clicking a menu. If you live in spreadsheets, you'll be fine.

#### Won't Claude just hallucinate things into my thesis?

It can — treat every section it writes as a first draft, not as gospel. The system mitigates this in three ways. First, the source URL is recorded in frontmatter and cannot be edited later — you can always trace a claim back to its source. Second, inline callouts ([§9](#callouts)) let you push back on individual sentences with a permanent record of the disagreement. Third, `/stress-test` exists precisely to surface holes in the thesis from an adversarial perspective.

None of this makes Claude a reliable analyst by itself. It makes Claude a structured research assistant whose mistakes are auditable and reversible. You're still the analyst.

#### What stops the LLM from going off-script and breaking the vault?

Five layers. CLAUDE.md as system prompt sets the conventions. Each skill is a step-by-step specification, not a free-form prompt. Tier-3 confirmations gate investment-grade changes (conviction shifts, status transitions, file deletions). Every destructive operation snapshots before editing. `/lint` audits schema drift across the vault.

Claude can still hallucinate the *contents* of a note — that's a separate problem solved by reading-before-writing and provenance immutability. But it cannot, by construction, silently violate the architectural rules.

#### How long until the vault starts being useful?

The first thesis you write is already more valuable to you than ten random research notes. The compound effect kicks in around thesis number five or six — the first time `/surface` finds cross-thesis patterns you couldn't see yourself, and the first time `/retro` has enough conviction shifts to rank trade ideas by narrative-price gap.

Most users feel the system click after a month of regular use. Before that, it's experienced as structured note-taking. After that, you start noticing the vault catching things you would have missed.

#### Is this only for stocks?

The investment-research version is one instantiation, but the patterns — context engineering, deterministic skills, append-only audit logs, snapshot-based rollback — generalise to any LLM-augmented knowledge work. Legal research, scientific literature review, software architecture documentation, investigative journalism. Same primitives, different note templates and skill specs.

---

## §13 · Glossary

### The handful of terms used throughout.

- **Thesis** — The 14-section investment case for one ticker. Lives in `Theses/`.
- **Research note** — A structured note about one source — transcript, article, stress test. Four required sections. Lives in `Research/`.
- **Sector note** — An 11-section overview of one sector that links every active thesis in it. Lives in `Sectors/`.
- **Skill** — A Markdown spec at `.claude/skills/<name>/SKILL.md` that tells Claude exactly what to do, step by step. Same command, same output.
- **Context engineering** — The discipline of structuring an LLM's working environment so it behaves as if it has memory and durable behavior. The vault does this with six files (see [§3](#context)).
- **Frontmatter** — YAML metadata block at the top of a Markdown file. Defines status, conviction, sector, ticker, source.
- **Wikilink** — `[[note-name]]` syntax for cross-references inside the vault. Lets Claude traverse the graph of related notes.
- **Conviction** — Your stated confidence in a thesis: high, medium, or low. Changes are Tier-3 and require explicit confirmation.
- **Callout** — An inline comment block dropped next to LLM output to push back on it, ask a question, or flag a todo.
- **Non-consensus insight** — A view the market hasn't priced in. The thesis structure forces you to articulate one — it's where alpha actually lives.
- **Narrative-price gap** — The distance between what your vault says about a name and what the market did with the price. The retro engine ranks trade ideas by this gap.
- **Snapshot** — A backup copy of a note taken automatically before any destructive change. Lets you undo any skill that goes wrong.
- **Subagent** — A child Claude instance spawned for an isolated subtask (used by `/lint`, `/prune`, `/surface`, `/retro`). Returns a summary; its read cost stays out of the main conversation.
- **Watermark** — The modification time of `.last_sync`. Lets skills find only the files that changed since the last operation.
