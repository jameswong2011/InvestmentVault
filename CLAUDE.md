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
9. **`_hot.md` auto-create and compression contract** — if `_hot.md` does not exist when a skill needs to update it, create it with sections: `## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`. Use frontmatter: `date: YYYY-MM-DD`, `tags: [meta, hot-cache]`. All writes follow the shared compression contract at `.claude/skills/_shared/hot-md-contract.md` — per-section budgets, soft/hard caps (4,000/5,000 words), and compression trigger order are defined there. `/lint #35` enforces schema; `/lint #42` catches truncation markers.
10. **Pre-flight contract** — every skill that modifies vault state must run the pre-flight checks at `.claude/skills/_shared/preflight.md` at Step 0:
    - **Vault lock acquisition** (Procedure 1) — prevents concurrent skill invocations from racing on shared files. Lock scope depends on skill type: `vault-wide` for `/sync all`, `/graph`, `/prune`, `/lint` (full), `/clean`, `/catalyst`, `/ingest` (any mode), `/scenario`, `/surface` (unscoped/sector), `/rollback` (restore mode); `ticker:TICKER` for ticker-scoped skills; N separate `ticker:TICKER` locks for `/compare` (one per ticker in the compare set — handles hyphen-containing tickers like BRK-B); `read-only` for `/lint TICKER` and `/rollback` (list mode). `/lint #43` enforces.
    - **Rename-marker check** (Procedure 2) — any ticker-scoped skill operating on a TICKER must hard-block if `.rename_incomplete.TICKER` exists at vault root. Vault-wide skills glob `.rename_incomplete.*` — most hard-block, a few (`/ingest`, `/rollback` restore, read-only `/surface`) warn-only per their individual spec. Exceptions: `/lint`, `/rollback` list mode, `/graph` (read-only for theses), `/rename` itself (owns the marker).
    - **Name sanitization** (Procedure 3) — any skill that takes a user-supplied string as a filename (currently `/rename` new_name) runs whitelist + NFC validation. Reject invalid characters, leading dot, reserved names, length >100.
    - **Section existence probe** (Procedure 4) — skills editing a specific `## Heading` abort if the section is absent (e.g., `/deepen` never creates sections that don't exist in the thesis).
11. **Skill-content truncation safeguard** — if the skill's content in a `<system-reminder>` contains a truncation marker (e.g., `[... skill content truncated for compaction ...]`) AND the skill will execute any write phase (Edit / Write / Bash mutation beyond pre-flight probes), Read the full `SKILL.md` at the skill's base directory BEFORE the first mutation. Long skills (`/sync`, `/status`, `/deepen`, `/compare`, `/thesis`, `/rollback`) routinely exceed the system-reminder budget and silently drop later-step rules. Filling dropped rules in from memory or extrapolation is how spec-compliant skills produce non-spec-compliant behavior — the Step 4 sector-propagation gate in `/sync` was missed this exact way on 2026-04-22. One extra Read at Step 0 eliminates this failure class at negligible cost.

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
13. **Legacy Callouts** — Auto-managed archive of addressed callouts swept from their original sections (owned exclusively by `/archive-callouts` — do NOT hand-edit)
14. **Log** — Dated entries tracking thesis evolution (max 2 lines per entry)

### Research Notes (/Research)
- Name format: `YYYY-MM-DD - [Topic or Ticker] - [Source Type].md`
- Source types: earnings, analyst-report, news, deep-dive, data, web-clip, video-transcript, stress-test, synthesis, brief, comparison, scenario
- Always include `source:` in frontmatter with the URL
- **Required body sections** (all 4, regardless of source_type): `## Thesis Delta`, `## Summary`, `## Evidence`, `## Contradiction Check`. Conditional: `## Framework / Mental Model` (when source advances a named framework/scoring scheme/typology), `## Key Segments` (when source >15,000 words), `## Source Excerpts` (may be empty). `## Summary` is prose — 1–2 paragraphs for short-form sources, 2–4 for long-form — capturing the source's actual argument, mechanism, and claim scope (NOT a business description). Full spec: `.claude/skills/ingest/SKILL.md`.
- Body length must be proportional to source length (per `/ingest` check #5): <1,500 source words → ≥300 body words; 1,500–5,000 → ≥800; 5,000–15,000 → ≥1,800; >15,000 → ≥2,500 + `## Key Segments`.
- Extract key data points and quote sparingly
- Add wikilinks to related thesis notes

### Sector Notes (/Sectors)
Each sector note acts as a Map of Content (MOC) and follows this structure:
1. **Active Theses** — Links to all thesis notes in this sector with active status (MOC navigation — goes first so readers can jump straight to the theses)
2. **Key industry questions** — Brief summary of key questions driving sector analysis
3. **Industry history** — Origin to present: founding of major incumbents, competitive consolidation, technological/regulatory/cultural transitions, and how pricing power shifted over time
4. **Competitive dynamics** — Current dynamics between key players: incumbent durability, new entrant threats, strategic shifts, pricing power trajectory (historical, current, forward), and rationale behind market share shifts
5. **Product level analysis** — Technical specifications, market purpose, and success rationale for each major incumbent's highest-volume products
6. **Acquisitions and new entrants** — Historical M&A with strategic objectives and outcomes; new entrant business models, disruption strategies, and impact on incumbent pricing power
7. **Macro shifts** — Macroeconomic variables (technological, geopolitical, regulatory, value chain, socioeconomic) currently or expected to drive material change in the sector
8. **Investor heuristics** — Current investor consensus, what is priced in, where consensus could be wrong, and non-consensus insights from the sector research
9. **Related Research** — Links to research notes relevant to this sector
10. **Legacy Callouts** — Auto-managed archive of addressed callouts swept from their original sections (owned exclusively by `/archive-callouts` — do NOT hand-edit)
11. **Log** — Dated entries tracking sector note evolution

### Macro Notes (/Macro)
- Geopolitical scenarios, commodity frameworks, rates outlook
- Strategies for short to medium term macro shock and trends, sector specific industry dynamics should be left in sector research
- Trading opportunities and portfolio re-allocation strategies in response to newsflow
- Link to affected thesis notes across sectors

### Inline callouts — LLM behavior

Obsidian callouts (`> [!type]`) serve as user-initiated feedback markers within thesis / sector / macro bodies. Four sanctioned types: `[!question]`, `[!error]`, `[!tip]`, `[!todo]`. Full user-facing spec: [[User Guide#Inline callouts — user feedback markers|User Guide §6]].

**Recognise callout state by header**:

| State | Header pattern | Meaning |
|---|---|---|
| **Fresh** | `> [!type] YYYY-MM-DD` alone | Unresolved user objection / question / suggestion |
| **Addressed** | `> [!type] YYYY-MM-DD → Addressed YYYY-MM-DD` + `**Response:**` block inside | Prior user-LLM exchange; resolved audit trail |
| **Pinned** | header contains `[[pinned]]` | Intentionally left open; do NOT address |
| **Preserved** | addressed callout header contains `[[preserve]]` | Addressed but exempt from `/archive-callouts` sweep; stays in original section indefinitely |
| **Legacy** | plain bullet inside `## Legacy Callouts` section | Previously addressed, swept to archive section by `/archive-callouts`; historical read-only record |

**LLM policy when callouts are present in a note being read or edited**:

1. **Never author callouts.** Callouts are user-initiated markers. LLM uncertainty or alternative framings go in prose, wikilinks, or `## Outstanding Questions` — not in callouts.
2. **Fresh callouts are open signals, not ground truth.** The user has flagged the surrounding content as contested. Treat the flagged claim as unresolved.
3. **Addressed callouts are history.** Read the `**Response:**` block for context on prior user-LLM exchanges; do NOT re-address unless explicitly asked.
4. **Pinned callouts opt out of addressing.** "Address all fresh callouts" explicitly skips any callout containing `[[pinned]]`.
5. **Never edit or delete a user's callout unless addressing it.** Even when rewriting sections (via `/deepen`, `/sync`, `/compare`, `/scenario`), preserve fresh and pinned callouts in place.
6. **`## Legacy Callouts` section is read-only archive.** Never hand-edit entries — the section is owned exclusively by `/archive-callouts`. Never re-sweep entries back to their original sections. Never address legacy entries (they are addressed by definition). Read them as historical context when relevant (e.g., `/deepen` evaluating section history, `/surface` scanning for resolved questions).
7. **`[[preserve]]` marker exempts addressed callouts from `/archive-callouts` sweep.** Treat the marker the same as `[[pinned]]` when it comes to `/graph` unresolved-wikilink handling (intentional unresolved link, not broken).

**Skill-specific callout handling**:

- `/brief`: exclude ALL callout content (fresh, addressed, pinned) AND the entire `## Legacy Callouts` section. Briefs are IC-output; callouts and legacy archive are working/audit state.
- `/stress-test`: read fresh `[!error]` as already-identified user weakness; incorporate into the test rather than re-identifying. Do NOT read `## Legacy Callouts` — historical warnings may have become valid again over time; let stress-test re-identify freely.
- `/deepen`: if the target section contains fresh callouts, acknowledge in the rewrite OR address them as part of the deepen (don't silently overwrite). Refuse to operate on `## Legacy Callouts` — it is an automated archive, not a deepen-eligible analytical section.
- `/sync`: reads callout-driven Log entries via Rule #7 prefix classification; does not read callout body content directly. Skips `## Legacy Callouts` during callout-block scans (section contains plain bullets, not `> [!type]` blocks, but the scanner should skip the section defensively).
- `/surface`: unaddressed callouts signal unresolved questions worth flagging in the surface report. `## Legacy Callouts` is optional pattern-analysis input (out of scope for v1).
- `/compare`, `/scenario`: preserve callouts AND `## Legacy Callouts` entries in affected theses verbatim during Log/section updates.
- `/archive-callouts`: owns the `## Legacy Callouts` section. Sweeps addressed callouts older than threshold (default 180 days from `→ Addressed` date) into the section as plain bullets, sorted descending. Creates the section if absent (between `## Related Research` and `## Log`). `[[preserve]]` opt-out per callout.
- `/graph`: treats `[[preserve]]` as intentional unresolved wikilink (same handling as `[[pinned]]`) — never flag as broken.
- `/rollback`: recognizes `pre-callout-sweep` trigger name; standard snapshot restore undoes a sweep.
- `/lint`: enforces archive schema (checks #44–#47) — sweep freshness, stale-fresh callouts, malformed Legacy entries, orphan Legacy sections.

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
6. **After manually editing a thesis body section** (Bull Case, Risks, Industry Context, Bear Case, Key Non-consensus Insights, etc.), **always append a Log entry describing the change**. Without one, `/sync` may classify the run as skill-origin (because the most-recent Log entry is from a prior skill like `/status` or `/stress-test`) and silently skip propagating the edit to sector and macro notes. The Log entry doesn't need a special prefix — any prefix not in `_shared/log-prefixes.md`'s skill-origin list (e.g., `Manual edit:`, `Reviewed:`, `Refined:`) forces `/sync` to treat the change as research-driven and propagate normally.
7. **Inline feedback on LLM output uses the callout convention** — drop `> [!question]`, `> [!error]`, `> [!tip]`, or `> [!todo]` callouts inside any section, then ask Claude to "address fresh callouts in [note(s)]". Claude edits sections, marks callouts addressed, and appends a Log entry with a **non-skill-origin prefix** (recommended: `Addressed user callouts:`) — skill-origin prefixes like `Deepened:`, `Status change:`, or `Stress test:` cause `/sync` to silently skip sector/macro propagation per Rule 6. Full spec: [[User Guide#Inline callouts — user feedback markers|User Guide §6]].
8. **Graph-primer pattern for cross-ticker context** — research skills (`/ingest`, `/compare`, `/thesis`, `/stress-test`, `/brief`, `/deepen`) consume `_graph.md` as a primer for cross-ticker/cross-sector context per `.claude/skills/_shared/graph-primer.md`. The graph orients analysis (cluster peers, shared adjacency, propagation fanout suggestions); it never replaces content reads of target thesis or research files. Anti-pattern to avoid: "skip reading thesis X because graph says X isn't in the cluster." Enforced by `/lint #54` (compliance) and `/lint #55` (anti-pattern detection).

## Core Workflow Loop
The primary vault workflow is an ingest-propagate-graph loop:
1. **Deposit** raw content into `_Inbox/` (web clips, Deep Research PDFs, CSVs, notes)
2. **`/ingest`** processes `_Inbox/` into structured Research notes with wikilinks and thesis Log updates
3. **`/sync`** propagates insights across all affected Theses, Sector Notes, Macro notes, and `_hot.md`
4. **`/graph last`** reconciles `_graph.md` against the just-modified files (true incremental — re-extracts only changed thesis adjacencies, always rebuilds reverse indexes from scratch to prevent drift)
5. **`/status`** executes conviction or status changes after research conclusions (e.g., `/status NVDA conviction medium→low`)
6. **`/surface`** for periodic deep review (blind spots, attention allocation, decay alerts, opportunities)
7. **`/lint`** for periodic health checks (structural, freshness, analytical)

**Metadata ownership**: `_graph.md` is owned exclusively by `/graph` (three modes: full rebuild, `/graph last`, `/graph [N]`). Research skills do not write to `_graph.md` — they create content and remind the user to run `/graph last` afterward. This eliminates cross-skill graph contention that was the source of most metadata edge cases.
