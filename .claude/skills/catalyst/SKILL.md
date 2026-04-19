---
name: catalyst
description: Extract and maintain a cross-portfolio catalyst calendar from all thesis notes. Use when user says "catalyst", "calendar", "what's coming up", "upcoming events", or "what could move the portfolio".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * defuddle * cp * mkdir *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Build a comprehensive catalyst calendar aggregating every upcoming event across the portfolio.

## Phase 1: Extract Catalysts (Section-Targeted Reading)

Reading all ~40 thesis notes in full will exceed context limits when catalyst extraction only needs 3 sections per note. Use targeted section reads to stay within budget.

1. For each thesis file in Theses/ (every file, not just active — monitoring theses can still have catalysts):
   - Read **only frontmatter + Catalysts section + Risks section + last 5 Log entries**. Stop reading before other sections (Summary, Business Model, Industry Context, Non-consensus Insights, etc. are not needed for catalyst extraction).
   - This yields ~200-500 words per thesis instead of 1,000-3,000 — reducing total input from ~60-120k words to ~8-20k words.
2. For each thesis, extract from the **Catalysts** section:
   - Event description
   - Approximate date or date range (if stated)
   - Expected impact direction (positive / negative / uncertain)
   - Magnitude estimate (major / minor)
3. Also scan the **Log** entries read in step 1 for any recently noted upcoming events
4. Also scan the **Risks** section read in step 1 for risk events with timing (e.g., "regulatory decision expected Q2")
5. Read Macro notes in full for cross-portfolio macro events (small set, ~6 files — rate decisions, geopolitical deadlines, commodity contract expirations)

## Phase 2: Enrich and Deduplicate
- Where catalyst dates are vague ("Q2 2026", "H2"), convert to approximate calendar dates
- Identify catalysts that affect MULTIPLE theses (e.g., an earnings report from a major customer that affects several supplier theses)
- Flag catalysts that are stale — events that appear to have already passed based on their dates vs today's date
- Web search for upcoming earnings dates for all thesis tickers to ensure the calendar is current

## Phase 3: Analyse Catalyst Clusters
- **Concentration risk**: Are there weeks where multiple catalysts cluster? This creates portfolio-level volatility
- **Catalyst gaps**: Which theses have NO near-term catalyst? Flag as thesis drift risk — a position with no catalyst is dead capital
- **Asymmetric events**: Which catalysts have the widest range of possible outcomes? These are the highest-attention-priority events
- **Cross-thesis catalysts**: Events that simultaneously affect 3+ positions (e.g., a macro data release, a major customer's earnings)

## Phase 4: Output

If `_catalyst.md` already exists, snapshot it before overwriting:
```bash
mkdir -p _Archive/Snapshots
cp "_catalyst.md" "_Archive/Snapshots/_catalyst (pre-catalyst YYYY-MM-DD-HHMM).md"
```
Then read the snapshot and add to its frontmatter:
```yaml
snapshot_of: "[[_catalyst]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: catalyst
snapshot_batch: catalyst-YYYY-MM-DD-HHMM
```

Save/update the catalyst calendar at `_catalyst.md` (overwrite each run — this is a regenerated utility file like `_hot.md`, not a research note):
```yaml
---
date: YYYY-MM-DD
tags: [meta, catalyst-calendar]
---
```

### Structure:
**Next 2 Weeks** (day-by-day detail)
| Date | Ticker(s) | Event | Expected Impact | Magnitude | Notes |
|------|-----------|-------|-----------------|-----------|-------|

**Weeks 3-4**
| Week of | Ticker(s) | Event | Expected Impact | Notes |
|---------|-----------|-------|-----------------|-------|

**Month 2-3** (grouped by week)
| Approximate Date | Ticker(s) | Event | Notes |
|-----------------|-----------|-------|-------|

**No Catalyst Identified**
| Ticker | Last Catalyst Date | Days Since | Status |
|--------|-------------------|------------|--------|
[Theses with no upcoming catalyst — flag for attention]

**Stale Catalysts** (events that appear to have passed)
| Ticker | Event | Listed Date | Action Needed |
|--------|-------|-------------|---------------|
[Catalysts whose dates have passed — thesis needs updating]

**Cross-Thesis Events**
[Events affecting 3+ theses, with impact assessment for each]

## Phase 5: Report

Report to user: next 2 weeks of catalysts, any dangerous clusters, and the list of theses with no catalyst (these need attention or pruning).
