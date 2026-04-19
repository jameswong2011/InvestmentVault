---
name: scenario
description: Propagate a hypothetical macro scenario through the entire portfolio. Use when user says "what if", "scenario", "what happens to my portfolio if", or describes a macro event to model.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Map the impact of a macro scenario across every thesis, sector, and position in the vault.

## Arguments
$ARGUMENTS should describe the scenario (e.g., "Fed cuts 150bps", "China invades Taiwan", "oil spikes to $150", "AI capex disappoints by 40%", "major cybersecurity breach at a hyperscaler"). If empty, ask the user what scenario to model.

## Phase 1: Define the Scenario
- State the scenario precisely with quantitative parameters where possible
- Identify the primary transmission channels: rates, FX, commodity prices, supply chains, demand destruction, regulatory, sentiment, capital flows
- Set a time horizon (default: 6 months from today)
- Assign a rough probability estimate (not for precision, but to calibrate how seriously to take tail risks)

## Phase 2: Read the Portfolio (Two-Pass Triage)

Reading all ~40+ thesis notes in full will exceed context limits. Use a lightweight scan to triage, then deep-read only exposed positions.

### Pass 1 — Lightweight scan
1. Read all Macro notes in full (small set, highest scenario relevance)
2. Read `_graph.md` for portfolio topology and cross-thesis clusters
3. For each thesis in Theses/, read **only frontmatter + Summary section** (stop before ## Key Non-consensus Insights). This yields ~200 words per thesis — manageable for the full set.

### Pass 2 — Triage and deep read
4. Using the summaries, macro context, and the transmission channels from Phase 1, classify each thesis:
   - **High exposure**: direct transmission channel to this position (e.g., rate-sensitive revenue, supply chain disruption, commodity input cost) → read the **full thesis note** + its sector note
   - **Low exposure**: indirect or second-order transmission only → read **Summary + Risks + Bull/Bear Case** sections only
   - **No exposure**: no plausible transmission channel → do NOT read further. Carry forward the summary for the impact matrix (mark as Neutral)
5. Read sector notes **only for sectors with at least one High-exposure thesis** — skip unaffected sectors entirely

This typically reduces the deep-read set from ~58 files to 15-20.

## Phase 3: First-Order Impact Assessment
For each thesis (all, including No-exposure — use Neutral for those), assess direct impact:

| Ticker | Company | Conviction | Direct Impact | Magnitude | Transmission Channel | Key Assumption at Risk |
|--------|---------|------------|---------------|-----------|---------------------|----------------------|
| | | [H/M/L] | [Positive / Negative / Neutral] | [Major / Minor] | [How the scenario affects this specific position] | [Which bull or bear assumption is tested] |

Sort the table by magnitude of impact (major negatives first).

## Phase 4: Second and Third-Order Effects
This is the highest-value phase — trace the cascades:

**Supply chain cascades**
- If Company A is disrupted, who loses a critical supplier? Who gains from the disruption?
- Are there single points of failure in the value chains documented in Sector Notes?

**Demand substitution**
- If one product/sector suffers, where does demand rotate to?
- Which of my theses are on the receiving end of that rotation?

**Relative winners within sectors**
- Within each affected sector, who gains market share from others' weakness?
- Does the scenario accelerate or decelerate the competitive dynamics already documented in sector notes?

**Funding, valuation, and sentiment**
- How do multiples compress or expand across sectors?
- Does risk-off sentiment hit some theses harder due to liquidity, positioning, or narrative fragility?

**Portfolio correlations revealed**
- Which positions that appear diversified are actually correlated under this scenario?
- What is the effective portfolio concentration once you adjust for scenario-driven correlation?

## Phase 5: Portfolio-Level Assessment
- **Net portfolio impact**: Directional estimate with rough magnitude (e.g., "net negative, ~60% of positions face material headwinds")
- **Worst-case cluster**: Which 3-4 theses get hit simultaneously and hardest?
- **Concentration risk exposed**: Does the scenario reveal hidden portfolio concentration?
- **Natural hedges**: Which positions offset each other under this scenario?
- **Hedge gaps**: What would protect the portfolio that isn't currently held?
- **Opportunities created**: Does the scenario create dislocations that become new thesis candidates?

## Phase 6: Output

### 6.1: Write the research note (without `propagated_to:`)

Save to `Research/YYYY-MM-DD - Scenario - [Short Scenario Name].md` with:
```yaml
---
date: YYYY-MM-DD
tags: [research, scenario, macro]
source: vault synthesis
source_type: scenario
# propagated_to: omitted intentionally — set in Phase 6.3 only after all Major-impact Log appends succeed
---
```

Sections:
1. Scenario Definition (parameters, channels, time horizon)
2. Impact Matrix (table from Phase 3)
3. Second-Order Effects (narrative from Phase 4)
4. Portfolio Assessment (from Phase 5)
5. Recommended Actions (specific hedges, position adjustments, research priorities)
6. Related Notes (wikilinks to all theses and macro notes referenced)

### 6.2: Append Log entries to all Major-impact theses

For each thesis rated **Major** impact in the Phase 3 table, attempt to append a Log entry (max 2 lines each):
```
### YYYY-MM-DD
- Scenario [[Research/YYYY-MM-DD - Scenario - Short Name]]: [impact direction via transmission channel] — conviction [unchanged/strengthened/weakened + reason]
```

For each thesis that received a Log entry, add the scenario to its `## Related Research` section (if not already present):
```
- [[Research/YYYY-MM-DD - Scenario - Short Name]]
```

**Track outcomes per ticker**: maintain two lists during this phase — `succeeded: [tickers]` and `failed: [tickers, with reason]`. A failure means the Log append Edit failed (file locked, missing `## Log` section, malformed frontmatter, etc.). Do NOT abort the loop on a single failure — continue attempting the remaining Major-impact theses so partial propagation completes.

### 6.3: Atomicity rule for `propagated_to:` update

**Update the research note's `propagated_to:` frontmatter only after EVERY Major-impact thesis's Log entry has landed successfully.** Mirrors the `/sync` Step 1 atomicity rule.

- **All appends succeeded** (`failed:` list empty): edit the research note's frontmatter to add `propagated_to: [TICKER1, TICKER2, ...]` listing all Major-impact tickers. This signals to subsequent `/sync` runs that producer-side propagation is complete; `/sync` Check 2 will skip these tickers as "already propagated."
- **One or more appends failed** (`failed:` list non-empty): do **NOT** write `propagated_to:` at all. Leave the frontmatter without the field. The next `/sync` (default mode) will detect each Major-impact thesis via the file-direct fallback (the research note's body wikilinks every Major-impact thesis under "Related Notes"), check for today's Log entry per the strict calendar-day rule, and re-attempt the append for the failed targets.

**Why never partial**: A partial `propagated_to:` would claim some failed-target tickers as propagated when their Log entries never landed, creating a permanent audit gap that future `/sync` runs silently skip because the dedup hint says "already done." The all-or-nothing rule trades minor `/sync` re-work (it will re-evaluate succeeded targets and skip them via the per-thesis idempotency check) for guaranteed eventual consistency.

**Per-failure reporting**: list every failed ticker in the Phase 6 report under a new field `Major-impact Log appends — failed: [TICKER1 (reason), TICKER2 (reason)]`. The user can inspect each failure or simply re-run `/sync` to let the universal propagation mechanism catch up.

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the scenario research note and any new cross-thesis correlations in the dependency map.

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: scenario modelled ([short scenario name]), top 3 exposed positions, and the single most important action. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry for each ticker where conviction was strengthened or weakened by the scenario
3. **Open Questions**: Add any research questions the scenario exposed (e.g., unquantified exposures, missing hedges)

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Phase 7: Report

Report to user, in this order:

1. **Top 3 most exposed positions** with transmission channel
2. **The 1 biggest beneficiary** with rationale
3. **The single most important action** to take now
4. **Major-impact propagation status**:
   - `Major-impact theses propagated: [N] of [M]` (succeeded list)
   - `propagated_to: frontmatter` — `set` (all succeeded) | `omitted (one or more appends failed — next /sync will retry)`
   - **Failed appends** (only if any): `[TICKER1 (reason), TICKER2 (reason)]`
5. **Follow-up**: `→ Run /sync to propagate to minor-impact theses and retry any failed Major appends. Then /graph last.`
