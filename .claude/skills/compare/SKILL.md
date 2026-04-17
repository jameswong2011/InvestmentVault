---
name: compare
description: Side-by-side competitive comparison of two or more companies. Use when user says "compare", "X vs Y", "which is better", or asks about competitive dynamics between specific companies.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * cp * mkdir * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Build a rigorous side-by-side comparison focused on competitive dynamics and investment merit.

## Arguments
$ARGUMENTS should contain 2+ tickers or company names (e.g., "BESI vs AMAT", "PANW NET CRWD"). If only one ticker is provided, identify its closest competitors from the Sector Note and ask the user to confirm before proceeding.

## Phase 0: Thesis Existence Check
Verify which tickers in $ARGUMENTS have existing thesis notes in Theses/.

**All tickers have theses** → proceed to Phase 1 (full comparison mode).

**Some tickers lack theses** → report and offer options:
```
⚠️ No thesis found for [TICKER(S)]. Options:
  (a) Proceed — use web research for [TICKER(S)] (lighter comparison, no vault updates for missing tickers)
  (b) Stop — run /thesis [TICKER] first for a full-depth comparison
```
Wait for user selection.
- **(a) Web-supplemented mode**: Proceed. Missing tickers use web research in Phase 1. Phase 5 vault updates (Log, Related Research, graph) apply ONLY to tickers with existing theses. Report appends: `💡 Consider /thesis [TICKER] to formalize coverage.`
- **(b) Stop**: Report the missing tickers and stop.

**No tickers have theses** → stop. At least one thesis is required as the analytical anchor.

## Phase 1: Gather Context
For each company **with a thesis note**:
1. Read the thesis note from Theses/
2. Read all linked research notes from the thesis
3. Read the relevant Sector Note(s) — especially competitive dynamics and value chain sections
4. Search Research/ and Macro/ for additional mentions

**Web-supplemented tickers** (Phase 0 option a): Skip steps 1-2. Instead, search the web for: business model overview, latest financials (revenue, margins, growth), competitive position, and key products. Search the vault (Research/, Sectors/, Macro/) for any existing mentions. Flag sections where vault-depth data is unavailable with `[web only]`.

## Phase 2: Structural Comparison

### Business Model Comparison
| Dimension | [TICKER A] | [TICKER B] | Edge |
|-----------|-----------|-----------|------|
| Core revenue model | | | |
| Gross margin structure | | | |
| Customer concentration | | | |
| Recurring vs one-time revenue | | | |
| Geographic mix | | | |
| Capital intensity | | | |
| R&D as % of revenue | | | |

### Competitive Position
| Factor | [TICKER A] | [TICKER B] | Edge |
|--------|-----------|-----------|------|
| Market share (current) | | | |
| Market share trend (direction) | | | |
| Pricing power trajectory | | | |
| Technology moat depth | | | |
| Switching costs | | | |
| Scale / network advantages | | | |
| Management quality / track record | | | |
| Insider alignment | | | |

### Financial Comparison
| Metric | [TICKER A] | [TICKER B] | Notes |
|--------|-----------|-----------|-------|
| Market Cap | | | |
| EV/Revenue | | | |
| Revenue Growth (latest) | | | |
| Revenue CAGR (3yr) | | | |
| Gross Margin | | | |
| Operating Margin | | | |
| FCF Yield | | | |
| Net Cash / Net Debt | | | |

Use data from vault Key Metrics tables, supplement with web research where gaps exist.

## Phase 3: Dynamic Analysis
Go beyond static snapshots — this is where investment insight lives:

1. **Market share trajectory** — Where is share shifting and why? Use vault research notes for evidence. Is the shift structural or cyclical?
2. **Pricing power divergence** — Whose pricing power is strengthening vs. weakening? What drives the divergence (technology, regulation, customer lock-in, commoditisation)?
3. **Technology trajectory** — Who is on the right side of the next platform shift? Who is investing in the right areas? Who risks being disrupted?
4. **Logical tension** — What does each company need to be true that the other company's success disproves? (e.g., if BESI wins on hybrid bonding, does that mean AMAT's approach fails, or can both win?)
5. **Scenario divergence** — Under what macro or industry scenario does the current underdog win? How likely is that scenario based on vault macro notes?
6. **Customer and supplier overlap** — Do they share customers? If so, who has more pricing power in that relationship? Do they share suppliers (creating correlated supply risk)?

## Phase 4: Investment Verdict
- **Risk-adjusted asymmetry**: Not "which is cheaper" but which offers better upside/downside skew given the evidence
- **Portfolio role**: Are these substitutes or complements? Can you own both, or is it one-or-the-other? Does owning both create hidden concentration?
- **Preference trigger**: What specific, observable event would flip the preference? Make it falsifiable
- **Conviction gap**: If one has a thesis and the other doesn't, should it? If both have theses, is the conviction spread justified by the evidence?

## Phase 5: Output

Save to `Research/YYYY-MM-DD - [TICKER A] vs [TICKER B] - Competitive Comparison.md` with:
```yaml
---
date: YYYY-MM-DD
tags: [research, comparison, SECTOR, TICKER_A, TICKER_B]
sector: [shared sector]
source: vault synthesis
source_type: comparison
propagated_to: [only tickers with existing thesis notes]
---
```

**Vault updates** — apply ONLY to tickers with existing thesis notes. Skip for web-supplemented tickers.

Update affected thesis notes with Log entries (max 2 lines each):
```
### YYYY-MM-DD
- [[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]: [key competitive insight] — conviction [unchanged/strengthened/weakened + reason]
```

For each compared thesis, add the comparison to its `## Related Research` section (if not already present):
```
- [[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]
```

Update the Sector Note if the comparison reveals competitive dynamics not already documented. Resolve the sector note via canonical procedure **`.claude/skills/_shared/sector-resolution.md`** using the shared `sector:` frontmatter (use the first compared thesis's sector if the compared theses share one; if they differ, resolve each separately and update both). If `match_confidence` is `none`, emit the contract's no-match warning and skip to the graph update below. If `match_confidence` is `normalized` or `substring`, emit the contract's `log_message` in the report; if `substring`, additionally pause for explicit user confirmation before modifying analytical text (the contract restricts substring-resolved sector notes from receiving destructive edits without confirmation). If modifying existing analytical text (competitive dynamics, value chain, company comparisons) — not just adding links — snapshot first:
```bash
mkdir -p _Archive/Snapshots
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-compare YYYY-MM-DD-HHMM).md"
```
Read the newly created snapshot, then add `snapshot_of`, `snapshot_date`, `snapshot_trigger: compare`, `snapshot_batch: compare-YYYY-MM-DD-HHMM` to its frontmatter.

**Modify the original sector note using targeted `Edit` operations (atomic string replacement per section), NOT full-file `Write`.** Each `Edit` call either succeeds atomically or leaves the section unchanged — this limits the blast radius of a mid-edit failure to zero (partial writes cannot occur). Apply one `Edit` per modified section (e.g., one for competitive dynamics, one for value chain).

**Post-edit verification**: After all edits, re-read the modified sector note. For each edited section, verify it ends with a complete sentence (not mid-word, mid-sentence, or with unclosed formatting markers). If verification fails: `⚠️ Sector note may contain a partial edit in [section]. Snapshot available: [[_Archive/Snapshots/...]]. Review manually or /rollback.`

> **Chain-aware**: Per CLAUDE.md Session Chain Protocol — if joining an active chain, SKIP graph update below and increment `Graph deferred`. If starting or no chain, proceed.

Update `_graph.md` (skip if it does not exist):
- Add the new comparison research note to each compared thesis's `research:` list in the Thesis Adjacency Index
- If the comparison revealed a new cross-thesis connection not already in Cross-Thesis Clusters, add it
- Update `date:` in frontmatter

**Graph validation**: After all graph edits, re-read the modified section and verify: (1) no unclosed `[[` brackets introduced, (2) `theses:` frontmatter count still within ±2 of actual `Theses/` file count. If either check fails: `⚠️ Graph may be corrupted — [specific failure]. Run /graph to rebuild.`

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

> **Chain-aware**: Per CLAUDE.md Session Chain Protocol — if joining an active chain: append `YYYY-MM-DD: /compare — [TICKER A] vs [TICKER B], key insight` to Active Research Thread only (skip compress/Previous), mark step ✅, then proceed to remaining sections. If starting or no chain, set Session Chain and apply full update below. **Stale-chain preservation** (before overwriting): if existing Session Chain has `Date:` ≠ today AND `Graph deferred: [N]` with N > 0, FIRST convert to Graph Debt per CLAUDE.md § Stale Chain — write `**⚠️ Graph debt**: [N] deferred from [stale-date] ([stale-skill-list]). Run /graph to capture.` below `*No active chain.*` (accumulate count and skill list with any pre-existing Graph Debt line rather than overwriting it). Only after preservation, overwrite the active-chain block with this skill as Step 1.

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: compared [TICKER A] vs [TICKER B], key competitive insight, and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry for each ticker where conviction was strengthened or weakened
3. **Open Questions**: Add any unresolved competitive questions the comparison surfaced

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

Report to user: the single most important competitive insight and whether it changes conviction on either name.
