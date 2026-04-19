---
name: surface
description: Surface new insights, potential trades, and research opportunities from existing vault content. Use when user says "surface", "what am I missing", "find opportunities", or "what should I research next".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * find * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Perform deep insight discovery across the vault. This is the highest-value operation — finding connections and opportunities the user hasn't seen yet.

## Scope Resolution

Parse `$ARGUMENTS` to determine scope:

- **Ticker** (e.g., `NVDA`): Read `_graph.md` and resolve the ticker's adjacency set — its thesis, sector note(s), macro note(s), cross-thesis references, and all linked research. Also include theses that share a sector (one ring outward) for competitive context.
- **Sector** (e.g., `semiconductors`): Use `_graph.md` Sector → Theses reverse index to resolve all theses in that sector, plus the sector note, related macro notes, and their linked research.
- **No arguments / empty**: Full vault — no scoping (reads everything).

If a scope is requested but `_graph.md` does not exist, warn: `⚠️ Graph missing — cannot scope. Run /graph first, or run /surface without arguments for full vault scan.` Then stop.

## Phase 1: Portfolio Scan

**Scoped mode**: Read only files resolved in Scope Resolution. Skip vault-wide checks that require full portfolio coverage (Attention Allocation ranking, Research Velocity ranking across all theses — these need the full set to be meaningful).

**Unscoped mode**: Read all Sector Notes and all active thesis notes (focus on Non-consensus Insights, Risks, and recent Log entries).

## Phase 2: Connection Analysis

**Portfolio Blind Spots**
- Identify sectors or sub-sectors the vault's theses imply are important but have NO coverage. (e.g., if you hold BESI + LITE + NVDA, you're implicitly betting on advanced packaging — do you cover the substrate suppliers? The test equipment vendors? The materials companies?)
- Flag value chain nodes that appear in multiple theses' Risk sections but have no dedicated research — these are unmonitored dependencies
- Check for "implied but unwritten" theses — tickers mentioned in 3+ research notes that still have no Thesis note. These are ideas the vault has been circling without committing to
- Identify adjacent companies that vault research strongly implies should be covered based on competitive dynamics in Sector Notes

**Supply Chain Mapping**
- Which thesis companies are suppliers, customers, or competitors of each other?
- Are there hidden portfolio correlations? (e.g., multiple bets on the same underlying trend)
- Would a single event break multiple theses simultaneously?

**Macro Exposure Audit**
- Map each thesis against current macro scenarios (Iran conflict, AI bubble risk, rate expectations)
- Flag theses with unacknowledged macro sensitivity
- Identify natural hedges within the portfolio

**Catalyst Calendar**
- What upcoming events could move multiple positions?
- Are there clustered earnings dates that create portfolio risk?
- Any regulatory, geopolitical, or technology milestones approaching?

**Contrarian Signal Detection**
- Where does the vault's thesis directly contradict current sell-side consensus?
- Which positions have the widest gap between vault conviction and market pricing?
- These are the highest-alpha opportunities — flag them prominently

**Research Freshness Audit**
- Which theses have the oldest research? (Longest time since last Research/ note)
- What developments might have occurred that aren't reflected?
- Search the web for 2-3 most material recent developments

**Thesis Velocity & Attention Allocation**
- **Research velocity ranking**: Which theses received the most research activity recently (new Research/ notes, Log entries, edits)? Which received zero? Rank all active theses by volume of recent activity.
- **Attention vs conviction alignment**: Compare where research time was spent against conviction levels. Flag any mismatch — disproportionate time on low-conviction ideas while high-conviction theses go unattended is a resource allocation error.
- **Decay alert**: List any active thesis that hasn't been touched (no Log entry, no new linked research) in 30+ days. These are candidates for `/deepen` or `/prune`.

## Phase 3: Opportunity Generation

Generate 3-5 specific, actionable research prompts ranked by potential conviction impact:

For each opportunity:
- **Topic**: What to research
- **Why now**: What triggered this being relevant
- **Vault connection**: Which existing notes it builds on
- **Expected impact**: High/Medium/Low potential to change a conviction level
- **Suggested approach**: Specific research steps

## Phase 4: Output

Save findings to:
- **Unscoped**: `Research/YYYY-MM-DD - Insight Surface Scan.md`
- **Ticker-scoped**: `Research/YYYY-MM-DD - [TICKER] - Surface Scan.md`
- **Sector-scoped**: `Research/YYYY-MM-DD - [Sector] - Surface Scan.md`

If the file already exists, append a counter (`...2.md`, `...3.md`). Save with:
```yaml
---
date: YYYY-MM-DD
tags: [research, meta, surface-scan]
status: active
source: vault synthesis
source_type: synthesis
---
```

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the surface scan research note, new cross-thesis connections, and any implied-but-unwritten thesis candidates in the dependency map.

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

> **Chain-aware**: Per CLAUDE.md Session Chain Protocol — if joining an active chain: append `YYYY-MM-DD: /surface — [scoped/unscoped], top insight` to Active Research Thread only (skip compress/Previous), mark step ✅, then proceed to remaining sections. If starting or no chain, set Session Chain and apply full update below. **Stale-chain preservation** (before overwriting): if existing Session Chain has `Date:` ≠ today AND `Graph deferred: [N]` with N > 0, FIRST convert to Graph Debt per CLAUDE.md § Stale Chain — write `**⚠️ Graph debt**: [N] deferred from [stale-date] ([stale-skill-list]). Run /graph to capture.` below `*No active chain.*` (accumulate count and skill list with any pre-existing Graph Debt line rather than overwriting it). Only after preservation, overwrite the active-chain block with this skill as Step 1.

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: surface scan completed [scoped/unscoped], top insight found, and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Open Questions**: Add any critical blind spots or research gaps the scan exposed

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

Also report a concise summary to the user highlighting the top 3 most actionable insights.
