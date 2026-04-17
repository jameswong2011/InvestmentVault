---
date: 2026-04-14
tags: [research, meta, claude-code, workflow, deep-dive]
status: active
source: Claude Code synthesis + web research
source_type: deep-dive
---

# Claude Code Mastery Guide for Investment Research

> A practitioner's guide to implementing Karpathy's LLM Knowledge Base pattern inside this vault, optimized for institutional-quality equity research and macro analysis.

---

## Part 1: The Karpathy Framework — Applied to Investment Research

### What Karpathy Actually Said

On April 3, 2026, Andrej Karpathy [shared his workflow](https://x.com/karpathy/status/2039805659525644595) for using LLMs to build personal knowledge bases. The core insight: **"A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge."**

His [llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) describes a three-layer architecture:

| Layer | Purpose | Your Vault Equivalent |
|-------|---------|----------------------|
| **Raw sources** | Immutable curated documents | `/Research` notes, web clips, earnings transcripts |
| **The wiki** | LLM-generated synthesis with cross-references | `/Theses`, `/Sectors`, `/Macro`, `Non-Consensus Insights Map` |
| **The schema** | Configuration defining structure and workflows | `CLAUDE.md` + `.claude/skills/` |

**Key operations:**
1. **Ingest** — Drop new sources; LLM reads, extracts entities, writes summary, updates indexes, appends to log
2. **Query** — Ask questions against the wiki; LLM synthesizes answers with citations from your own notes
3. **Lint** — Periodically check for contradictions, stale claims, orphan pages, missing cross-references

**Why it works for investment research:** "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping." The LLM handles the mechanical work (updating wikilinks, maintaining sector notes, appending to thesis logs, flagging contradictions between notes) while you focus on insight generation and conviction-building.

### Your Vault Today — What's Working and What's Missing

**Current state (90 notes):**
- `/Theses`: 30 thesis notes — well-structured with frontmatter, non-consensus insights, bull/bear cases
- `/Research`: 34 research notes — good naming convention, linked to theses
- `/Sectors`: 6 MOC notes — functional but shallow (Key Dynamics and Watchlist sections mostly empty)
- `/Macro`: 14 macro notes — richly detailed Iran scenario analysis, commodity frameworks
- `/Templates`: 4 templates — solid foundation
- **`Non-Consensus Insights Map`** — this is your best Karpathy-style "compiled wiki" page. It cross-references 7 thematic buckets across all theses

**Gaps to close:**
- `/Daily` and `/Weekly` are **completely empty** — no journal entries, no weekly reviews
- `/Canvas` is empty — no visual relationship maps
- `/Archive` is empty — no thesis lifecycle tracking
- `.claude/skills/`, `.claude/commands/`, `.claude/agents/` are **all empty** — no automation configured
- Sector Note "Key Dynamics" and "Watchlist" sections are unfilled
- No automated lint process to catch stale data or broken thesis logic
- No system for surfacing cross-thesis connections automatically

---

## Part 2: Prompt Engineering for Investment Research

### The Hierarchy of Prompt Quality

**Level 1 — Vague (wastes tokens, produces generic output):**
> "Research ServiceNow"

**Level 2 — Scoped (better, but still undirected):**
> "Research ServiceNow's competitive position in agentic AI"

**Level 3 — Contextualized (references existing knowledge):**
> "Read [[Theses/NOW - ServiceNow]] and [[Research/2026-04-05 - ServiceNow CMDB vs Palantir Ontology]]. The thesis argues CMDB is a structural advantage for AI automation. Search the web for recent ServiceNow vs Microsoft Copilot competitive dynamics — specifically, are enterprises choosing ServiceNow's Now Assist or Microsoft Copilot for IT workflow automation? Save findings to Research/ and update the thesis Log section."

**Level 4 — Adversarial (highest alpha generation):**
> "Read [[Theses/NOW - ServiceNow]] and its bear case. Steel-man the argument that Microsoft Copilot will commoditize ServiceNow's AI assistant layer. Find concrete evidence: enterprise adoption surveys, Gartner/Forrester reports, Reddit r/servicenow threads about Copilot vs Now Assist. If the evidence weakens the thesis, update the bear case and reduce conviction. If the evidence strengthens it, explain why and update the bull case."

### Investment-Specific Prompt Patterns

**Pattern 1: Thesis Stress-Test**
```
Read [[Theses/TICKER]]. Identify the single strongest bear argument 
that isn't currently listed. Search the web for evidence supporting 
that argument. If compelling, add it to the Risks section with today's 
date and reassess conviction level.
```

**Pattern 2: Cross-Thesis Connection Discovery**
```
Read all notes in /Theses and /Macro. Identify non-obvious connections 
between positions — e.g., shared supply chain dependencies, correlated 
macro exposures, or contradictory assumptions across theses. Create a 
new section in [[Non-Consensus Insights Map]] documenting these.
```

**Pattern 3: Earnings Catalyst Prep**
```
Read [[Theses/TICKER]]. The company reports earnings on [DATE]. 
Create a pre-earnings checklist:
1. What specific metrics would upgrade/downgrade conviction?
2. What management commentary would signal thesis acceleration/breakdown?
3. What consensus expectations am I betting against?
Save to Research/ as "YYYY-MM-DD - TICKER - Earnings Preview.md"
```

**Pattern 4: Source Ingestion (Karpathy-style)**
```
Fetch [URL] and save as a clean research note. Extract:
- 3-5 key data points with specific numbers
- Any information that challenges or supports existing theses
- Wikilinks to every relevant thesis and macro note
After saving, tell me which thesis notes should be updated and why.
```

### Prompting Rules of Thumb

1. **Always reference existing notes** — `Read [[note]]` before asking Claude to write. Context from your own vault is higher-signal than generic web results.
2. **Specify the output location** — "Save to Research/" or "Update the Log section of [[Theses/X]]"
3. **Request adversarial analysis** — "What breaks this thesis?" generates more alpha than "Why is this a good investment?"
4. **Chain ingestion to synthesis** — Don't just clip articles. Always end with "How does this change the thesis?"
5. **Use the AskUserQuestion pattern for conviction calls** — "Interview me about my STNG position. Challenge my assumptions about Hormuz duration using historical precedents."

---

## Part 3: Token Optimization and Context Window Management

### Understanding the Economics

Your vault is currently ~90 notes. At an average of ~2,000 tokens per note, that's ~180K tokens if Claude read everything. **Claude cannot and should not read the entire vault in one session.** The context window (200K for standard Opus, up to 1M with extended context) must be managed surgically.

### The Token Budget Framework

| Token Source | Approx. Cost | Frequency |
|---|---|---|
| CLAUDE.md (auto-loaded) | ~1,500 tokens | Every session |
| Each skill description (auto-loaded) | ~50-100 tokens each | Every session |
| Full skill content (on invocation) | 500-2,000 tokens | On demand |
| Reading one thesis note | 2,000-5,000 tokens | Per file read |
| Reading one research note | 1,500-3,000 tokens | Per file read |
| Web fetch result | 1,000-3,000 tokens | Per fetch |
| Your prompt + Claude's response per turn | 500-2,000 tokens | Per turn |

### Token Optimization Strategies

**1. Keep CLAUDE.md Under 100 Lines**
Every line loads into every session. Ask yourself: "Would removing this line cause Claude to make a mistake?" If not, cut it. Your current CLAUDE.md is good but could be tighter — move the active sectors list and workflow rules into skills that load on demand.

**2. Use the Index-First Pattern (Karpathy's "Hot Cache")**
Instead of reading 30 thesis notes, read the Sector Notes first. They're indexes. If the [[Sectors/Semiconductors]] MOC tells you which notes exist, Claude can selectively read only the 2-3 that matter for your question.

```
Read [[Sectors/Enterprise Software]] to understand what's there.
Then read only [[Theses/NOW - ServiceNow]] and 
[[Theses/PLTR - Palantir]] — I want to compare their AI automation 
approaches.
```

**3. Surgical File Reading**
When you know which part of a file matters, tell Claude:

```
Read lines 15-45 of [[Theses/NOW - ServiceNow]] (the Non-consensus 
Insights section only).
```

**4. Use Subagents for Research**
Subagents run in separate context windows and return only summaries:

```
Use a subagent to read all 14 notes in /Macro and summarize which 
ones mention oil price assumptions above $100. Report back tickers 
and notes affected.
```

This keeps your main context clean while the subagent does the heavy reading.

**5. Compact Strategically**
- Run `/compact` after completing a research task but before starting the next
- Use `/compact Focus on the thesis updates and data points discovered` to direct what survives compaction
- Add to CLAUDE.md: `When compacting, always preserve: ticker names, conviction changes, data points with numbers, and file paths of modified notes.`

**6. Clear Between Tasks**
Investment research naturally chunks into sessions:
- Session 1: Research a specific ticker → `/clear`
- Session 2: Update macro scenario → `/clear`
- Session 3: Weekly review synthesis

**7. The 80% Rule**
Stop complex multi-file work (like updating multiple theses from a single macro insight) when context hits ~80% full. Complex cross-referencing degrades in quality past this point.

### Compaction Instructions for CLAUDE.md

Add this to your CLAUDE.md:

```markdown
## Compaction Rules
When compacting, always preserve:
- The full list of files read and modified in this session
- Any specific data points with numbers (prices, ratios, dates)
- Conviction level changes on any thesis
- Wikilinks created or suggested
- Unanswered questions or follow-up tasks
```

---

## Part 4: Model Selection — When to Use Sonnet vs Opus

### The Decision Framework

As of April 2026, [Sonnet 4.6 and Opus 4.6 are within 1.2 percentage points on SWE-bench](https://www.nxcode.io/resources/news/claude-sonnet-4-6-vs-opus-4-6-which-model-to-choose-2026), but Opus costs 5x more ($15/$75 per million tokens vs $3/$15). For your investment research workflow:

### Use Sonnet (default 90% of the time) for:

| Task | Why Sonnet | Example |
|------|-----------|---------|
| **Research note creation** | Structured extraction from a single source | "Fetch this article and save as a research note" |
| **Single thesis updates** | Appending to Log, updating a specific section | "Add today's earnings data to [[Theses/SPOT - Spotify]]" |
| **Web clipping and ingestion** | Mechanical extraction and formatting | "Clip this URL and link to relevant theses" |
| **Template application** | Following existing patterns | "Create a new thesis note for TICKER using the template" |
| **Simple vault queries** | "Which theses mention HBM?" | Grep + read + summarize |
| **Daily note creation** | Structured journaling | "/daily" |
| **Frontmatter fixes and batch ops** | Mechanical file updates | "Add missing conviction fields to all thesis notes" |

### Use Opus (the other 10%) for:

| Task | Why Opus | Example |
|------|----------|---------|
| **Cross-thesis synthesis** | Requires holding 5-10 documents in memory and finding non-obvious connections | "Read all semiconductor theses and the AI Bubble Risk macro note. Identify contradictory assumptions." |
| **Thesis creation from scratch** | Deep reasoning about investment logic, bull/bear framing, scenario analysis | "Build a full thesis for a new ticker based on 3 research notes" |
| **Adversarial stress-testing** | Requires genuine reasoning depth to steel-man bear cases | "Find the strongest argument against my LITE thesis" |
| **Macro scenario modeling** | Complex second-order thinking across multiple positions | "If Iran conflict escalates to Scenario A, which of my 30 positions are most exposed?" |
| **Non-Consensus Insights Map updates** | Synthesizing patterns across the entire portfolio | "Review all theses and update the insight map with new connections" |
| **Weekly reviews** | Pattern recognition across a week's worth of activity | "/weekly-review" |
| **Deep Recon / multi-agent research** | Multiple agents exploring different angles | "/deep-recon [topic]" |

### Thinking Effort Levels

Your current config: `"thinkingBudget": "medium"`. For investment research, consider:

- **Low effort**: Mechanical tasks (fixing frontmatter, creating empty templates, simple file operations)
- **Medium effort** (your default): Single-note research, standard ingestion, routine updates
- **High effort**: Thesis creation, earnings analysis, cross-document synthesis
- **Max effort** (Opus only): Portfolio-wide synthesis, scenario analysis, identifying non-consensus insights

You can set effort per-skill in the skill's frontmatter:
```yaml
---
name: weekly-review
effort: max
model: opus
---
```

### When to Start a New Chat Window

Start fresh (`/clear` or new terminal) when:

1. **Switching tickers** — Don't research STNG tanker rates in the same session as NOW's AI strategy. The context pollution will degrade both.
2. **Moving from research to synthesis** — Read sources in Session 1, then start Session 2 with "Read the 3 notes I just created and synthesize a thesis."
3. **After ingesting 5+ documents** — Each web fetch or file read consumes 2-5K tokens. After 5-6, context is 30%+ full of raw source material.
4. **When Claude starts repeating itself** — This is the clearest signal of context degradation.
5. **Before a high-stakes task** — Thesis creation, conviction changes, or portfolio-level synthesis deserve clean context.
6. **After `/compact` feels insufficient** — If you've compacted twice in one session, the summary-of-summaries is losing fidelity. Start fresh.

**Don't start fresh when:**
- You're in a multi-step workflow (research → update thesis → update MOC) — keep the thread alive
- Claude just read 5 files you need it to reference — that context is expensive to rebuild
- You're iterating on a specific section of a note — the revision history in context helps

---

## Part 5: Setting Up Claude Code Skills for Investment Research

Your `.claude/skills/`, `.claude/commands/`, and `.claude/agents/` directories are currently empty. Here are the high-value skills to create:

### Skill 1: `/ingest` — Source Ingestion Pipeline

```yaml
# .claude/skills/ingest/SKILL.md
---
name: ingest
description: Ingest a URL or document into the vault as a structured research note. Use when the user shares a URL, mentions saving an article, or says "clip this" or "ingest this."
allowed-tools: Read Grep Glob Edit Write WebFetch Bash(date *)
---

Ingest a source into the vault following the Karpathy pattern:

1. **Fetch and extract** the content from $ARGUMENTS (URL or file path)
2. **Create a research note** at `Research/YYYY-MM-DD - [Topic] - [Source Type].md` using the Research Template format
3. **Extract key data points** — specific numbers, dates, quotes (max 5-7, prioritize quantitative)
4. **Check for existing theses** — Read the Sectors MOCs to find related thesis notes
5. **Add wikilinks** to every related thesis and macro note
6. **Update the thesis Log** — For each linked thesis, append a dated entry to its Log section: `### YYYY-MM-DD\n- New research: [[Research/note-name]] — [one-line summary of relevance]`
7. **Update the Sector Note** — Add the new research note to the appropriate Sector Note's Research Notes section
8. **Report back**: List what was created, which theses were updated, and any insights that might change conviction levels

Always use the `defuddle` skill for web content extraction when available.
```

### Skill 2: `/thesis` — New Thesis Creation

```yaml
# .claude/skills/thesis/SKILL.md
---
name: thesis
description: Create a new investment thesis note with full analysis. Use when user says "create thesis", "new thesis", or "build a case for TICKER"
model: opus
effort: high
disable-model-invocation: true
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date *)
---

Create a comprehensive thesis note for $ARGUMENTS:

1. **Search the vault first** — Read the relevant Sector Note and any existing Research notes mentioning this ticker
2. **Search the web** — Find recent earnings, analyst consensus, key metrics, and competitive dynamics
3. **Create the thesis** at `Theses/TICKER - Company Name.md` following the Thesis Template:
   - Frontmatter: date, tags (include [thesis, SECTOR, TICKER]), status: draft, conviction: (assess), sector, ticker
   - Summary: One paragraph investment case
   - Key Non-consensus Insights: 3-5 perspectives foreign to the mainstream narrative (this is the MOST IMPORTANT section — think deeply)
   - Catalysts: Near-term events with approximate dates
   - Key Metrics: Table with Market Cap, EV/Revenue, Revenue Growth, Gross Margin, FCF Yield
   - Bull Case / Bear Case: Explicit scenario analysis
   - Risks: What breaks the thesis (be genuinely adversarial)
   - Position Sizing: Conviction level with reasoning
   - Related Research: Wikilinks to all vault notes mentioning this ticker
   - Log: Initial entry with today's date
4. **Update the Sector Note** — Add the new thesis to the Active Theses section
5. **Suggest next research** — What 2-3 research questions would increase or decrease conviction?
```

### Skill 3: `/daily` — Daily Research Journal

```yaml
# .claude/skills/daily/SKILL.md
---
name: daily
description: Create or update today's daily research journal. Use when user says "daily", "journal", "what did I do today", or at the start of a session.
allowed-tools: Read Grep Glob Edit Write Bash(date *)
---

Create or update today's daily note at `Daily/!`date +%Y-%m-%d`.md`:

1. **Check if today's note exists** — If yes, read it and append. If no, create from Daily Template.
2. **Scan recent activity** — Check git log for files modified today, or ask the user what they worked on
3. **Market Context** — Ask the user for 2-3 bullet points on market conditions, or note any macro events
4. **Research Done** — List research notes created/modified today with wikilinks
5. **Thesis Updates** — List any thesis notes updated today, noting conviction changes
6. **Tasks** — Carry forward incomplete tasks from yesterday's daily note (if it exists)
7. **Notes** — Capture any freeform observations

Keep entries concise. Each bullet should be actionable or contain a specific insight.
```

### Skill 4: `/weekly-review` — Weekly Synthesis

```yaml
# .claude/skills/weekly-review/SKILL.md
---
name: weekly-review
description: Generate a weekly review synthesizing all research activity. Use on Fridays or when user says "weekly review".
model: opus
effort: high
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Edit Write Bash(date * find * wc *)
---

Generate a weekly review for the current week:

1. **Read all daily notes** from this week in /Daily (Monday through today)
2. **Scan modified files** — Use git log to find all notes modified this week
3. **Synthesize by section:**
   - **Thesis Activity**: Which theses were created, updated, or had conviction changes? Quote specific Log entries.
   - **Key Research**: The 3-5 most important research notes created this week. Why do they matter?
   - **Market Observations**: Macro themes from daily notes. What patterns emerged?
   - **Cross-Thesis Patterns**: Did this week's research reveal connections between positions? New risks? New opportunities?
   - **Conviction Changes**: Any upgrades or downgrades? What drove them?
   - **Next Week Priorities**: Based on upcoming catalysts, earnings dates, or open research questions
4. **Save to** `Weekly/YYYY-WW - Week of YYYY-MM-DD.md` with proper frontmatter
5. **Update Non-Consensus Insights Map** if any new cross-thesis patterns were discovered
```

### Skill 5: `/lint` — Vault Health Check (Karpathy's Lint)

```yaml
# .claude/skills/lint/SKILL.md
---
name: lint
description: Run health checks on the vault to find inconsistencies, stale data, orphaned notes, and missing connections. Use periodically or when user says "lint", "health check", or "audit the vault".
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Bash(find * wc * date *)
---

Perform a comprehensive health audit of the vault:

## Structural Checks
1. **Orphaned research notes** — Research notes not linked from any Thesis or Sector Note
2. **Thesis notes missing from Sector Notes** — Theses that exist but aren't listed in their sector
3. **Broken wikilinks** — Links pointing to notes that don't exist
4. **Missing frontmatter fields** — Notes without required fields (date, tags, status, conviction for theses)
5. **Stale theses** — Thesis notes with status: active but no Log entry in the last 30 days

## Content Checks
6. **Contradictory claims** — Data points that conflict across notes (e.g., different revenue numbers for the same company)
7. **Stale data** — Financial metrics that are >6 months old
8. **Empty sections** — Thesis notes with unfilled Key Metrics tables or empty Bull/Bear cases
9. **Disconnected macro notes** — Macro notes not linked from any thesis

## Synthesis Opportunities
10. **Unlinked connections** — Notes that mention the same concepts/tickers but aren't linked to each other
11. **Missing thesis candidates** — Tickers mentioned in 3+ research notes but without a dedicated thesis

Report findings as a checklist with file paths and specific issues. Prioritize by impact on research quality.
```

### Skill 6: `/surface` — Insight Discovery

```yaml
# .claude/skills/surface/SKILL.md
---
name: surface
description: Surface new insights and potential trades from existing vault content. Use when user says "surface", "what am I missing", "find opportunities", or "what should I research next".
model: opus
effort: max
allowed-tools: Read Grep Glob WebSearch WebFetch Bash(date *)
---

Perform deep insight discovery across the vault:

1. **Read the Non-Consensus Insights Map** and all Sector Notes to understand current portfolio positioning
2. **Read all active thesis notes** (status: active or draft)
3. **Identify gaps and opportunities:**

   a. **Supply chain connections**: Which thesis companies are suppliers/customers of each other? Are there hidden correlations in the portfolio?
   
   b. **Macro exposure mapping**: Given current macro notes (Iran scenario, AI bubble risk, commodity outlook), which theses have unacknowledged macro sensitivity?
   
   c. **Catalyst calendar**: What upcoming events (earnings, product launches, regulatory decisions) could move multiple positions simultaneously?
   
   d. **Contrarian signals**: Where does the vault's thesis directly contradict current sell-side consensus? These are the highest-alpha opportunities.
   
   e. **Research freshness**: Which theses have the oldest research? What new developments might have occurred?

4. **Search the web** for recent developments on the 3 most "stale" theses
5. **Generate 3-5 specific research prompts** that would produce the highest-value new insights
6. **Output as a prioritized list** with estimated conviction impact (high/medium/low) for each

Save findings to `Research/YYYY-MM-DD - Insight Surface Scan.md`
```

### Skill 7: `/sync` — Cross-Document Synchronization

```yaml
# .claude/skills/sync/SKILL.md
---
name: sync
description: Synchronize learnings across theses and macro documents after new research. Use when user says "sync", "propagate", "update everything", or after completing a research session.
allowed-tools: Read Grep Glob Edit Write Bash(date * find *)
---

Synchronize recent research insights across all affected documents:

1. **Identify recent changes** — Check git log for notes modified in the last session (or use $ARGUMENTS to specify which notes to propagate from)
2. **Extract propagatable insights** — From modified notes, identify:
   - New data points that affect other theses
   - Macro developments that impact multiple positions
   - Competitive dynamics relevant to other sector names
   - Updated financial metrics
3. **For each affected thesis:**
   - Append a dated Log entry citing the source research note
   - Update Key Metrics if new numbers are available
   - Add/update wikilinks to the new research
   - Flag if conviction should be reassessed
4. **Update Sector Notes:**
   - Add new research notes to the Research Notes section
   - Update Key Dynamics if sector-level observations emerged
5. **Update Macro notes:**
   - Cross-reference new data points into relevant macro frameworks
6. **Update Non-Consensus Insights Map** if new cross-thesis patterns were discovered
7. **Report**: Summary of all changes made, with counts of files updated and any conviction flags raised
```

### Agent: Vault Research Explorer

```yaml
# .claude/agents/vault-explorer.md
---
name: vault-explorer
description: Explores the vault to answer questions about existing research, find connections, and summarize positions
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a research analyst assistant exploring an investment research vault.

When asked a question:
1. First read the relevant Sector Note to understand what notes exist
2. Then read specific thesis and research notes relevant to the question
3. Synthesize findings with specific citations to vault notes using [[wikilinks]]
4. Highlight any contradictions or gaps you discover

Always cite specific notes and data points. Never make claims without vault evidence.
```

---

## Part 6: Answering Your Three Key Questions

### Question 1: How to Synchronize Daily Learnings Across Multiple Theses and Macro Documents

This is the **highest-value automation** for your vault and directly implements Karpathy's "ingest + update" pattern.

**The Problem:** You research ServiceNow's CMDB advantage, which has implications for Palantir (competitive threat), the Enterprise Software sector (AI automation dynamics), and the AI Bubble Risk macro note (enterprise AI monetization). Currently, you'd need to manually update 4+ documents.

**The Solution — Three-Layer Sync System:**

**Layer 1: Session-Level Sync (the `/sync` skill above)**
After each research session, invoke `/sync` to propagate insights. This reads your recent changes and updates all affected documents. It's manual but comprehensive.

**Layer 2: Automated Ingestion with Propagation (the `/ingest` skill)**
When ingesting any new source, the skill automatically: checks for related theses → updates their Log sections → updates Sector Notes. This means every article you clip ripples through the vault.

**Layer 3: Daily Journaling + Weekly Synthesis**
```
Morning:  /daily → captures market context, carries forward tasks
Evening:  /sync → propagates the day's research across documents
Friday:   /weekly-review → synthesizes patterns, surfaces connections
Monthly:  /lint → catches anything that fell through the cracks
```

**Implementation Priority:**
1. Create the `/ingest` and `/sync` skills (immediate — biggest ROI)
2. Create the `/daily` skill and start journaling (build the habit)
3. Create `/weekly-review` to close the loop (creates the compounding effect)
4. Create `/lint` for periodic maintenance (monthly cadence)

**Hook for Automatic Reminders:**
Add to `.claude/settings.json`:
```json
{
  "hooks": {
    "SessionStart": [{
      "type": "command",
      "command": "echo 'Reminder: Run /sync at end of session to propagate learnings'"
    }]
  }
}
```

### Question 2: How to Pull Deep Research Insights from Claude Web into Obsidian

Claude's Deep Research feature (available on claude.ai but not in Claude Code) produces long-form research reports. Here's how to bridge the gap:

**Method 1: Chrome Extension (Fastest)**
Install the [Claude to Obsidian & Markdown Export](https://chromewebstore.google.com/detail/claude-to-obsidian-markdo/ehacefdknbaacgjcikcpkogkocemcdil) Chrome extension. It:
- One-click exports Claude conversations to Obsidian-ready Markdown
- Preserves structure (headers, code blocks, lists)
- Bulk exports multiple chats
- You can save directly to your vault's `/Research` folder

**Workflow:**
1. Run Deep Research on claude.ai for your topic
2. Click the extension's export button → save to `InvestmentVault/Research/`
3. Open Claude Code and run:
```
/ingest Research/[the-exported-file].md
```
The ingest skill will: clean up formatting → extract key data points → link to existing theses → update MOCs.

**Method 2: Manual Copy-Paste with `/ingest`**
1. Run Deep Research on claude.ai
2. Copy the output
3. In Claude Code: "Here's a Deep Research report on [topic]. Save this as a research note and propagate insights to all relevant theses."
4. Paste the content

**Method 3: Automated Pipeline (Most Scalable)**
Create a "drop folder" workflow:
1. Create a `_inbox/` folder in your vault
2. Save Deep Research exports there (manually or via extension)
3. Create a skill that processes the inbox:

```yaml
# .claude/skills/process-inbox/SKILL.md
---
name: process-inbox
description: Process all unprocessed files in _inbox/. Convert to proper research notes with links.
disable-model-invocation: true
---

Process all files in _inbox/:
1. For each .md file in _inbox/:
   a. Read the content and identify the topic, ticker(s), and source type
   b. Create a properly formatted research note in Research/
   c. Run the ingest pipeline (extract data points, link to theses, update MOCs)
   d. Move the original file to _inbox/processed/
2. Report: list of notes created and theses updated
```

**Method 4: Deep Recon (Claude Code Alternative to Deep Research)**
The [Deep Recon skill](https://forum.obsidian.md/t/deep-recon-claude-skill-for-obsidian/111369) runs multi-agent research directly in Claude Code:
- 4 agents (Explorer, Associator, Critic, Synthesizer) work in parallel
- Searches both your vault AND the web
- Produces 3-5 competing framings of a topic
- Costs ~800K-1M tokens per session, takes 20-30 minutes
- Requires Opus

This is the closest to Deep Research inside Claude Code. Install it for topics where you want comprehensive, multi-perspective analysis.

### Question 3: How to Surface New Insights and Potential Trades from Existing Research

This is the **compound interest** of the Karpathy approach — your vault gets smarter over time.

**Strategy 1: The `/surface` Skill (On-Demand Insight Discovery)**
See the skill definition above. This reads your entire portfolio and actively hunts for:
- Unacknowledged macro exposures
- Supply chain connections between holdings
- Contrarian signals vs sell-side consensus
- Stale theses that need refreshing

**Strategy 2: Scheduled Research Loops**
Use the `/loop` or `/schedule` bundled skills to run periodic insight generation:

```
/loop 24h /surface
```

This runs the surface scan every 24 hours, producing a fresh insight report.

**Strategy 3: The "What Would Disprove This?" Protocol**
For each active thesis, periodically run:

```
Read [[Theses/LITE - Lumentum]]. Search the web for the most recent 
developments. What has changed since the thesis was last updated? 
What new information would DISPROVE the thesis? Focus on:
- Competitive developments (new entrants, customer shifts)
- Technology risks (alternative approaches, obsolescence)  
- Financial deterioration (margin compression, revenue misses)
If anything material is found, update the thesis with a dated Log entry.
```

**Strategy 4: Cross-Pollination from Macro Events**
When a macro event occurs (e.g., new tariff announcement, earnings season starts):

```
A new [EVENT] has occurred. Read all active thesis notes and the 
relevant macro notes. For each thesis, assess:
1. Is this thesis directly affected? (first-order)
2. Are there second-order effects through supply chains or demand?
3. Does this create a new catalyst or risk?
Create a Research note documenting the impact analysis and update 
affected thesis Log sections.
```

**Strategy 5: The Watchlist-to-Thesis Pipeline**
The Sector Note "Watchlist" sections are empty. Populate them:

```
Read [[Sectors/Semiconductors]]. Search the web for the top 5 
semiconductor companies by YTD stock performance that I DON'T 
already have a thesis for. For each, write a 2-sentence summary 
and add to the Watchlist section. Flag any that overlap with 
existing theses' competitive dynamics.
```

Then, when a watchlist name accumulates 2-3 research mentions, the `/lint` skill will flag it as a "Missing thesis candidate."

---

## Part 7: Advanced Patterns and Community Implementations

### Key GitHub Repos to Reference

| Repo | What It Does | Relevance |
|------|-------------|-----------|
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Full Karpathy pattern implementation: /wiki, /save, /autoresearch, /lint, hot cache, visual canvases | Most complete implementation — study its skills/ architecture |
| [rvk7895/llm-knowledge-bases](https://github.com/rvk7895/llm-knowledge-bases) | Claude Code plugin for building LLM-maintained Obsidian wikis from raw research | Compile, query, lint cycle |
| [AcWiz/my-claude-scholar](https://github.com/AcWiz/my-claude-scholar) | Semi-automated research assistant for academic research | Research pipeline patterns |
| [pablo-mano/Obsidian-CLI-skill](https://github.com/pablo-mano/Obsidian-CLI-skill) | Obsidian Skill for Claude Code using Obsidian CLI | Vault manipulation patterns |
| [YishenTu/claudian](https://github.com/YishenTu/claudian) | Obsidian plugin embedding Claude Code as AI collaborator | In-vault Claude integration |

### The Hot Cache Pattern (from claude-obsidian)

Create a `_hot.md` file that Claude updates at the end of every session:

```markdown
# Hot Cache — Last Updated: 2026-04-14

## Active Research Thread
Currently investigating ServiceNow's CMDB vs Palantir's Ontology for 
enterprise AI automation. Key question: does CMDB's installed base 
advantage outweigh Ontology's flexibility?

## Recent Conviction Changes
- NOW: medium → considering upgrade if Moveworks integration metrics strong
- LITE: high (unchanged) — 200G EML thesis intact

## Open Questions
1. What's the actual enterprise adoption rate for Now Assist vs Copilot?
2. Is the Ras Laffan repair timeline being revised?
3. BESI hybrid bonding revenue contribution — when does it inflect?

## Modified Files This Session
- Research/2026-04-14 - ServiceNow CMDB vs Palantir Ontology.md (created)
- Theses/NOW - ServiceNow.md (Log updated)
- Theses/PLTR - Palantir.md (Log updated)
- Sectors/Enterprise Software.md (Research Notes updated)
```

This persists recent context between sessions. Start new sessions with "Read _hot.md" to instantly regain context.

### Implementation Roadmap

**Week 1: Foundation**
- [ ] Create the 7 skills defined above
- [ ] Create the vault-explorer agent
- [ ] Add compaction rules to CLAUDE.md
- [ ] Create `_inbox/` folder and `_hot.md`
- [ ] Start daily journaling with `/daily`

**Week 2: Ingestion Pipeline**
- [ ] Install [Claude to Obsidian Chrome extension](https://chromewebstore.google.com/detail/claude-to-obsidian-markdo/ehacefdknbaacgjcikcpkogkocemcdil)
- [ ] Process 5 Deep Research reports through the `/ingest` pipeline
- [ ] Run `/sync` after each research session
- [ ] Run `/lint` for the first time — fix all flagged issues

**Week 3: Synthesis Layer**
- [ ] Run first `/weekly-review`
- [ ] Run first `/surface` scan
- [ ] Populate Sector Note "Key Dynamics" and "Watchlist" sections
- [ ] Update Non-Consensus Insights Map with new connections

**Week 4: Optimization**
- [ ] Review which skills need tuning based on output quality
- [ ] Prune CLAUDE.md — move anything that's now handled by skills
- [ ] Establish cadence: daily journal, post-session sync, weekly review, monthly lint
- [ ] Assess Sonnet vs Opus allocation — are you using Opus only for synthesis tasks?

---

## Part 8: Key Reference Links

- [Karpathy's LLM Knowledge Bases tweet](https://x.com/karpathy/status/2039805659525644595)
- [Karpathy's llm-wiki gist (methodology)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [VentureBeat coverage](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)
- [Claude Code Skills documentation](https://code.claude.com/docs/en/skills)
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [Claude Code + Obsidian guide (DEV Community)](https://dev.to/mibii/claude-code-obsidian-build-a-second-brain-that-actually-thinks-d61)
- [Context window management deep-dive](https://claudefa.st/blog/guide/mechanics/context-management)
- [Sonnet vs Opus decision guide](https://www.nxcode.io/resources/news/claude-sonnet-4-6-vs-opus-4-6-which-model-to-choose-2026)
- [Deep Recon skill (Obsidian Forum)](https://forum.obsidian.md/t/deep-recon-claude-skill-for-obsidian/111369)
- [claude-obsidian GitHub (Karpathy pattern implementation)](https://github.com/AgriciDaniel/claude-obsidian)
- [MindStudio: Building Karpathy's LLM Wiki](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)
- [How Claude Code manages context (token buffer)](https://claudefa.st/blog/guide/mechanics/context-buffer-management)
