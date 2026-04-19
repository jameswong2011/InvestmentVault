---
name: brief
description: Generate a concise 1-page investment brief from a thesis — the elevator pitch version. Use when user says "brief", "summarise thesis", "pitch me [TICKER]", "one-pager", or "investment memo".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Distil a thesis into a sharp, 1-page investment brief. This forces clarity — if the case can't be made compellingly in one page, the thesis needs work.

## Arguments
$ARGUMENTS should be a ticker (e.g., "NVDA") or thesis name. If empty, ask the user.

## Phase 1: Load
1. **Duplicate check**: Grep `Research/` for existing briefs for this ticker (`source_type: brief` + matching ticker). If found, warn: `⚠️ Existing brief found: [[Research/existing-brief]]. Regenerating will create a new version. The old brief will remain in the vault.` Proceed — but note the old brief in the output so the user can delete it if desired.
2. Read the thesis note from Theses/
2. Read the 2-3 most recent or most important linked research notes (prioritise by recency and by being referenced in Log entries)
3. Read the relevant Sector Note for competitive context
4. Check Key Metrics for data freshness

## Phase 2: Compress
Distil the thesis into exactly this structure. Every word must earn its place.

---

**[TICKER] — [Company Name]**
*[Sector] · [Status] · Conviction: [Level] · [Date]*

### The Pitch
2-3 sentences maximum. Lead with the non-consensus angle. Why does this opportunity exist? What is the market mispricing and why?

### Why Now
The timing argument in 2-3 bullets. What catalyst, inflection point, or transition makes this relevant today rather than 6 months ago or 6 months from now?

### The Non-Consensus Edge
The single strongest variant perception — one paragraph. This is the insight that, if correct, generates the alpha. State what consensus believes, why they're wrong, and what evidence supports the contrarian view. Cite specific data points.

### Key Numbers
| Metric | Value |
|--------|-------|
| Market Cap | |
| EV/Revenue | |
| Revenue Growth | |
| Gross Margin | |
| FCF Yield | |

### What Kills It
The single biggest risk in 2-3 sentences. Not a laundry list — the ONE thing that, if it happens, invalidates the thesis. Be honest about probability.

### Conviction & Sizing
One line: conviction level, the quality of evidence supporting it, and what would change it (up or down).

---

## Phase 3: Quality Check
Before saving, verify:
- Is the pitch genuinely non-consensus, or is it a restatement of sell-side narrative?
- Does "Why Now" contain a specific catalyst with a date, or is it vague?
- Is "What Kills It" a real risk or a softballed disclaimer?
- Are the Key Numbers current (check data age from thesis)?
- Could someone who has never read the full thesis understand the case from this brief alone?

If any check fails, strengthen that section before saving.

## Phase 4: Output

Save to `Research/YYYY-MM-DD - [TICKER] - Investment Brief.md` with:
```yaml
---
date: YYYY-MM-DD
tags: [research, brief, TICKER]
sector: [from thesis]
ticker: TICKER
source: vault synthesis
source_type: brief
---
```

Do NOT modify the original thesis note (the brief is a derivative product, not a replacement).

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the investment brief in the dependency map.

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: generated [TICKER] investment brief, and any notable gap or weakness the Phase 3 quality check identified. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Open Questions**: If the Phase 3 quality check identified weaknesses (vague catalyst, stale metrics, softballed risk), add as open questions for the ticker

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

Present the brief directly to the user in the response — it should be immediately readable.
