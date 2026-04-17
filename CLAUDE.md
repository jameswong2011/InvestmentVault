# Investment Research Vault

## Approach & Core Purpose (xxx IMPORTANT xxx)

This is a personal knowledge base for institutional-quality equity research, macro analysis, and investment thesis development. The focus is generally on generating qualitative insights that are non-consensus (such as technological / product, management / culture, competitive dynamics / market concentration / pricing power, investor bias, unique business model / business model transition) rather than macro / financial / valuations based research that traditional investors focuses on. The objective of the analysis is to be balanced with a critical perspective (do not to always be positive about every opportunity).

## Vault Structure

```
/_Inbox          — Drop zone for raw content (web clips, Deep Research PDFs, CSVs). Processed by /ingest.
/_Inbox/processed — Archive of already-ingested originals (auto-managed by /ingest)
/Theses          — Synthesized investment cases (one note per ticker or macro theme)
/Research        — Structured research notes created by /ingest or manually
/Sectors         — Sector-level overview notes
/Macro           — Geopolitical analysis, commodity frameworks, rates, FX
/Templates       — Note templates for consistent structure
/_Archive        — Completed or abandoned theses as well as version control backups (Snapshots)
/Canvas          — Visual maps and relationship diagrams
```

## Writing Standards (xxx ALL LLM OUTPUT MUST FOLLOW xxx)
- Lead with the insight or the number, never with context the reader already has
- No hedge words: "importantly", "notably", "significantly", "it's worth noting", "it should be noted", "interestingly", "crucially"
- Every sentence earns its place with a data point, an insight, or a specific claim — cut connective tissue
- Tables over prose for comparative or quantitative content
- Thesis Log entries: max 2 lines. Format: `[source/trigger]: [what changed] — [conviction impact: unchanged/strengthened/weakened + 1 reason]`
- Research notes for existing theses: lead with what changed for the thesis, not a business description
- No restating information that already exists in the thesis note — only deltas

## Change Safety Rules (xxx MANDATORY xxx)

### Tier 1: Protected Files — Never modify without explicit instruction
- `CLAUDE.md` — system instructions; structural changes need explicit ask
- `Templates/*.md` — define vault consistency; changing them alters all future output
- `.obsidian/` — Obsidian config; touch only when asked
- `.claude/skills/` — skill definitions; edit only when asked

### Tier 2: Append-Only Zones
- **Thesis `## Log` sections** — only append new dated entries at the end; never edit, reorder, or delete existing entries
- **`_hot.md` `## Sync Archive`** — prepend new entries, never remove old ones
- **Research notes once created** — treat body content as immutable source record; corrections go in a new note or a thesis log entry

### Tier 3: Confirmation-Required Changes
These changes represent investment decisions, not formatting — confirm with the user before applying:
- `conviction:` frontmatter changes (high → medium, medium → low, etc.)
- `status:` transitions (active → monitoring, active → closed)
- Moving a thesis to `/_Archive`
- Removing any wikilink from a thesis, sector note, or macro note
- Deleting or renaming any file (use archive-not-delete; see below)

### Operational Rules
1. **Read before write** — always read a file before modifying it; never use Write on an existing file without reading it first
2. **Archive, don't delete** — move closed/abandoned notes to `/_Archive` rather than deleting; this preserves log history and link traceability
3. **Frontmatter `source:` is immutable** — source URLs are provenance records; never modify or remove them
4. **New files go to their correct directory** — Research in `/Research`, theses in `/Theses`, macros in `/Macro`, sector notes in `/Sectors`; never create vault content at root level
5. **Follow naming conventions** — Research: `YYYY-MM-DD - [Topic] - [Source Type].md`; Theses: `TICKER - Company Name.md`
6. **Check before creating** — before creating a new thesis or research note, search the vault for existing notes on that ticker/topic to avoid duplicates
7. **Wikilinks are additive** — add new `[[wikilinks]]` freely; removing existing links requires explicit instruction because it breaks discoverability chains
8. **Batch operation transparency** — skills that touch multiple files (`/sync`, `/ingest`, `/lint`) must report every file modified and what changed
9. **`_hot.md` auto-create** — if `_hot.md` does not exist when a skill needs to update it, create it with sections: `## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`, `## Session Chain` (set to `*No active chain.*`). Use frontmatter: `date: YYYY-MM-DD`, `tags: [meta, hot-cache]`. Then proceed with the skill's normal `_hot.md` update

## Conventions

### Note Format
- All notes use YAML frontmatter with these properties:
  - `date`: YYYY-MM-DD
  - `tags`: array format, e.g. [thesis, semiconductors, LRCX]
  - `status`: draft | active | monitoring | closed
  - `conviction`: high | medium | low (for thesis notes)
  - `sector`: the primary sector classification
  - `source`: URL or description of primary source
- Use `[[wikilinks]]` for all internal references
- Use `![[embeds]]` to pull in related content
- Tag taxonomy: #thesis, #research, #macro, #earnings, #catalyst, #risk, #sector/[name]

### Thesis Notes (/Theses)
Each thesis note follows this structure:
1. **Summary** — One-paragraph investment case
2. **Key Non-consensus Insights** — 3-5 one-paragraph summaries of critical perspectives the market is missing, drawing from Research, Macro, and Sector folders
3. **Outstanding Questions** — 3-10 one-paragraph summaries of what a skeptical investment committee would ask before approving the investment
4. **Business Model & Product Description** — In-depth breakdown of the business model with analogies/comparisons, key revenue/profit-generating products with technical specs, and revenue segmentation (by reported segment or a novel heuristic)
5. **Industry Context** — Competitive dynamics, market share / pricing power shifts, and value chain analysis
6. **Key Metrics** — Table format with columns: Metric, Value, Notes (Market Cap, EV/Revenue, Revenue Growth, Gross Margin, FCF Yield)
7. **Bull Case** — Explicit upside scenario
8. **Bear Case** — Explicit downside scenario
9. **Catalysts** — Near-term events that could move the stock
10. **Risks** — What breaks the thesis
11. **Conviction Triggers** — Pre-defined, falsifiable if/then statements: → HIGH if, → LOW if, → CLOSE if
12. **Related Research** — Wikilinks to supporting research notes
13. **Log** — Dated entries tracking thesis evolution (max 2 lines per entry)

### Research Notes (/Research)
- Name format: `YYYY-MM-DD - [Topic or Ticker] - [Source Type].md`
- Source types: earnings, analyst-report, news, deep-dive, data, web-clip, stress-test, synthesis, brief, comparison, scenario
- Always include `source:` in frontmatter with the URL
- Extract key data points and quote sparingly
- Add wikilinks to related thesis notes

### Sector Notes (/Sectors)
Each sector note acts as a Map of Content (MOC) and follows this structure:
1. **Key industry questions** — Brief summary of key questions driving sector analysis
2. **Industry history** — Origin to present: founding of major incumbents, competitive consolidation, technological/regulatory/cultural transitions, and how pricing power shifted over time
3. **Competitive dynamics** — Current dynamics between key players: incumbent durability, new entrant threats, strategic shifts, pricing power trajectory (historical, current, forward), and rationale behind market share shifts
4. **Product level analysis** — Technical specifications, market purpose, and success rationale for each major incumbent's highest-volume products
5. **Acquisitions and new entrants** — Historical M&A with strategic objectives and outcomes; new entrant business models, disruption strategies, and impact on incumbent pricing power
6. **Macro shifts** — Macroeconomic variables (technological, geopolitical, regulatory, value chain, socioeconomic) currently or expected to drive material change in the sector
7. **Investor heuristics** — Current investor consensus, what is priced in, where consensus could be wrong, and non-consensus insights from the sector research
8. **Active Theses** — Links to all thesis notes in this sector with active status
9. **Related Research** — Links to research notes relevant to this sector
10. **Log** — Dated entries tracking sector note evolution

### Macro Notes (/Macro)
- Geopolitical scenarios, commodity frameworks, rates outlook
- Strategies for short to medium term macro shock and trends, sector specific industry dynamics should be left in sector research
- Trading opportunities and portfolio re-allocation strategies in response to newsflow
- Link to affected thesis notes across sectors

## Active Context
- [[_hot.md]] — recent context and open questions, updated by `/sync` and other skills

## Compaction Rules
When compacting, preserve information in this priority order:
### Critical (never drop)
- Current research objective and which thesis/ticker is being actively worked
- Conviction level changes with the reasoning behind them
- Specific data points with numbers (prices, ratios, dates, percentages, growth rates)
- Decisions made or conclusions reached during this session, with brief rationale
- Unanswered questions or follow-up research tasks (these drive the next session)
### Important (preserve if space allows)
- Full list of files read and modified in this session
- Wikilinks created or suggested between notes
- Ticker symbols and company names discussed
- Key disagreements or tensions found in the research (bull vs bear signals)
### Format
- Use bullet points, not prose — density matters in compacted context
- Group by ticker/theme, not chronologically
- Prefix actionable items with `TODO:` so they're scannable
- End with a one-line "Next step:" to make session resumption instant

## Workflow Rules
1. When creating new research notes, always check if a thesis note exists for that ticker — if so, add a wikilink
2. When updating a thesis, append to the Log section with today's date
3. When asked to research a topic, search the vault first before going to the web
4. Use defuddle for all web content extraction to keep notes clean
5. After creating research notes, suggest which thesis notes should be updated

## Session Chain Protocol

Multi-skill workflow chains (User Guide §3) cause redundant `_graph.md` writes and `_hot.md` Active Research Thread thrashing when each skill independently reads/writes these files. The `## Session Chain` section in `_hot.md` coordinates skills within a chain.

### Chain State (in `_hot.md`)
```
## Session Chain
- **Scope**: [ticker | sector | vault-wide]
- **Date**: YYYY-MM-DD
- **Steps**: /skill1 ✅, /skill2 ✅, /skill3 (next)
- **Graph deferred**: [count] — [summary of deferred changes]
```
When inactive: `*No active chain.*`

When inactive with **Graph Debt** (deferred changes from a cleared chain, not yet captured):
```
*No active chain.*
**⚠️ Graph debt**: [N] deferred from [YYYY-MM-DD] (/skill1, /skill2). Run `/graph` to capture.
```
Graph Debt persists across sessions until `/sync` (default/ticker mode) or `/graph` resolves it.

### Rules for Participant Skills
Every skill that updates `_hot.md` or `_graph.md` reads `## Session Chain` first:

| Condition | Action |
|-----------|--------|
| Active chain, overlapping scope, same date | Join: defer graph write, append short thread line, mark step ✅ |
| Active chain, non-overlapping scope | Convert old chain's deferred count to Graph Debt if > 0. Start new chain. |
| No chain or stale date (≠ today) | Convert stale chain's deferred count to Graph Debt if > 0. Start new chain. If Graph Debt already present, warn in report: `⚠️ [N] graph changes uncaptured from [date]. Run /graph.` |

Scope overlap: same ticker, ticker within chain's sector, both vault-wide, or either is vault-wide.

**When joining a chain:**
- **`_graph.md`**: SKIP update. Increment `Graph deferred` count. The finalizer captures changes from vault state.
- **Active Research Thread**: Append only `YYYY-MM-DD: /[skill] — [one-line result]`. No compress/Previous rotation.
- **Other `_hot.md` sections** (Recent Conviction Changes, Open Questions, etc.): update normally.

**When starting a chain:** Set Scope, Date, this skill as Step 1, Graph deferred: 0. If Graph Debt exists, emit `⚠️ [N] graph changes uncaptured from [date]. Run /graph.` in the skill report and replace the Graph Debt line with the new chain state. Then proceed with full `_graph.md` and `_hot.md` updates as normal (first skill in a chain pays the full cost).

### Chain Finalizers
- **`/sync`** (default/ticker mode): Applies its own incremental graph update (naturally captures all deferred changes from vault state). Clears Session Chain to `*No active chain.*` **and removes any Graph Debt line**.
- **`/sync all`**: Skips incremental graph update. If chain has `Graph deferred` > 0, **convert to Graph Debt** instead of discarding. Clears the active chain steps but the Graph Debt line persists until resolved by `/sync` (default/ticker) or `/graph`. If Graph Debt already exists from a prior chain, accumulate the counts.
- **`/graph`**: Rebuilds from scratch (all deferred changes captured from vault state). Clears Session Chain to `*No active chain.*` **and removes any Graph Debt line**.

### Stale Chain
If Session Chain `Date` ≠ today, the chain crossed a session boundary. If `Graph deferred` > 0, **convert to Graph Debt** before clearing — write the deferred count, date, and skill names from the stale chain into the Graph Debt line. Then clear the chain steps and treat as no active chain.

This prevents silent loss of deferred graph changes when a session ends mid-chain without a finalizer.

## Core Workflow Loop
The primary vault workflow is a two-step ingest-propagate loop:
1. **Deposit** raw content into `_Inbox/` (web clips, Deep Research PDFs, CSVs, notes)
2. **`/ingest`** processes `_Inbox/` into structured Research notes with wikilinks and thesis Log updates
3. **`/sync`** propagates insights across all affected Theses, Sector Notes, Macro notes, and _hot.md
4. **`/status`** executes conviction or status changes after research conclusions (e.g., `/status NVDA conviction medium→low`)
5. **`/surface`** for periodic deep review (blind spots, attention allocation, decay alerts, opportunities)
6. **`/lint`** for periodic health checks (structural, freshness, analytical)
