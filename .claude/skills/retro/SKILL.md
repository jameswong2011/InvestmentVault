---
name: retro
description: Generate a backward-looking retrospective of vault activity (addressed callouts + Log entries) over a time window (1w / 1m / 1q), overlay with newsflow + earnings transcripts + price action, and rank trade ideas by the gap between official narrative and market reaction. Output is an immutable Research note. Use when user says "retro", "retrospective", "what did I do this week/month/quarter", "review activity against market", or "recommend trades from recent research".
model: opus
effort: max
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * find * awk * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Produce a retrospective that answers three questions in one artifact:

1. **What was resolved?** Addressed callouts with the user↔Claude exchange.
2. **What is still open?** Fresh callouts left unresolved in the window.
3. **Did the market price the narrative?** Per-ticker overlay of **newsflow + earnings results/transcripts + price action**. Trade ideas rank by the **narrative-price delta** — the gap between what official sources signaled and what the stock did. Biggest gaps are positioning opportunities; alignment is already-priced.

Output is an **immutable Research note** — one new note per run, never overwrite. Trade recommendations are informational (link-back + suggested follow-up skill); this skill never mutates `conviction:` or `status:` (Tier 3 Confirmation-Required per CLAUDE.md).

## Arguments

`$ARGUMENTS` parses to a window keyword. Everything else ignored.

| Input | Canonical window | Day count |
|---|---|---|
| empty, `1w`, `w`, `week`, `weekly`, `7d` | `1w` | 7 |
| `1m`, `m`, `month`, `monthly`, `30d` | `1m` | 30 |
| `1q`, `q`, `quarter`, `quarterly`, `90d` | `1q` | 90 |

Default: `1w`. Anything unrecognized → reject: `❌ /retro unknown window "[input]". Accepts: 1w | 1m | 1q.`

## Step 0: Pre-flight (MANDATORY — runs before Phase 1)

### 0.1: Acquire vault lock

Acquire a `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: **10 minutes** (parallel reads across ~60 files + N parallel WebSearches).

Capture the token at Step 0.1, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block via `rm -f "$LOCK_FILE"`.

### 0.2: Rename-marker pre-flight (warn-only)

Glob `.rename_incomplete.*` at vault root. If any marker exists, emit:

```
⚠️ In-flight rename repair(s) detected: [list markers]. Retro scan will proceed but its Research note's wikilinks to the affected ticker(s) use current filenames. Complete rename repair before running downstream /sync.
```

DO NOT abort. Retro is a read-mostly exploratory operation; its output is a new Research note that does not mutate existing thesis bodies. Mid-rename state does not silently split propagation the way a vault-wide `/sync` would.

### 0.3: Window computation

```bash
# Example for 1m window
DAYS=30
TODAY=$(date +%Y-%m-%d)
WINDOW_START=$(date -v-${DAYS}d +%Y-%m-%d 2>/dev/null || date -d "${DAYS} days ago" +%Y-%m-%d)
echo "WINDOW|$WINDOW_START → $TODAY"
```

Record `WINDOW_START`, `TODAY`, and window label (`1w|1m|1q`) for Phase 6 frontmatter.

### 0.4: Graph primer (optional — read if present)

Read `_graph.md` per `.claude/skills/_shared/graph-primer.md` Mode A (ticker-scoped, applied in aggregate during Phase 4 per-ticker synthesis). If absent or unparseable, proceed without primer — log `ℹ️ _graph.md absent — retro proceeds without cluster context.` Never block.

The graph orients Phase 4 synthesis (which ticker is in which cluster, shared peers) — it never replaces thesis reads.

## Phase 1: Parallel Batch Read

**Issue every file Read as a single parallel tool-call batch** — one message with ~60 Read invocations (~42 theses + ~13 sectors + ~6 macros). Do NOT serialize.

Files to Read in full:
- `Theses/*.md` — every file (draft, active, monitoring, closed-but-not-yet-archived all carry callouts + Log)
- `Sectors/*.md` — full set
- `Macro/*.md` — full set

Research notes are NOT read here — they don't carry callouts by convention, and their Log is implicit via the owning thesis.

## Phase 2: Extraction (parse in-memory from Phase 1 reads)

For each file content, walk the body line-by-line. Track the current `## Heading` at each line (parent-section detection walks back to the nearest `## ` — same approach as `/archive-callouts` Phase 2.2).

### 2.1: Addressed callouts in window

Match callout blocks with header:

```
> [!<type>] <fresh_date> → Addressed <addressed_date>[ <markers>]
> <body line 1>
...
> **Response:** <response line 1>
...
```

Qualify as **in-window addressed** iff `WINDOW_START ≤ addressed_date ≤ TODAY`. Extract per block:

```yaml
- file: [path]
  ticker: [inferred from file — TICKER from "Theses/TICKER - Name.md", or null for sector/macro]
  parent_section: [nearest preceding ## heading]
  type: question | error | tip | todo
  raised_date: YYYY-MM-DD
  addressed_date: YYYY-MM-DD
  body: [joined text, `> ` prefix stripped]
  response: [joined text, `**Response:** ` prefix stripped]
  markers: [[[pinned]]] (informational only — not excluded; legacy [[preserve]] markers during deprecation transition also recorded)
```

**Skip policy**:
- Callouts inside `## Legacy Callouts` — never parse (archive section).
- Callouts inside `## Log` — never parse (defensive; Logs don't carry callouts by convention).
- Malformed headers (unparseable date, unrecognized type) — skip with `ℹ️ Skipped malformed callout in [file]:[parent_section]`.

### 2.2: Fresh callouts in window

Match callouts with header `> [!<type>] <fresh_date>` (NO `→ Addressed` token). Qualify as **in-window fresh** iff `WINDOW_START ≤ fresh_date ≤ TODAY`. Extract same schema as 2.1 with `addressed_date: null` and `response: null`.

Fresh `[[pinned]]` callouts ARE included — pinned means "do not address", not "do not report in retro". They still signal what the user was thinking about.

### 2.3: Log entries in window

Match headers `^### (YYYY-MM-DD)$` within any `## Log` section. For each date header in `[WINDOW_START, TODAY]`, collect every bullet line beneath it until the next `### ` or `## `.

Extract per bullet:

```yaml
- file: [path]
  ticker: [inferred from file]
  date: YYYY-MM-DD
  prefix: [first token-phrase before `:` if present — match against _shared/log-prefixes.md registry]
  text: [full bullet body]
  skill_origin: true | false  # matches any prefix in the skill-origin list
```

Skill-origin classification (matches `_shared/log-prefixes.md` skill-origin list): `Stress test`, `Deepening`, `Deepened`, `↳ CORRECTION: Deepened`, `Conviction reaffirmed`, `Status change:`, `CLOSED`, `Prune upgrade`, `Scenario `, `Initial thesis created`, `ROLLBACK to snapshot`, `Scenario REVERSED`, `Cross-thesis closure:`, `Cross-thesis closures:`, `Renamed file:`, `Comparison `, `Callout sweep:`.

Non-skill-origin entries are manual or user-callout-driven activity — highest signal for retro ("what I actually thought about").

### 2.4: Ticker universe

Compute `TICKER_UNIVERSE = unique set of tickers across 2.1 + 2.2 + 2.3 where ticker is non-null`. This is the set of tickers that had ANY activity in the window and require market overlay.

Sector/macro-file callouts with no clear ticker attach are tracked separately in a `portfolio_level_activity` bucket — surfaced in the output but not ticker-keyed.

### 2.5: Empty-window short-circuit

If `2.1 + 2.2 + 2.3 = 0` entries across all files:

```
No activity found in [1w|1m|1q] window ([WINDOW_START] → [TODAY]).

Possible reasons:
  - No callouts addressed or raised in window
  - No /status, /sync, /stress-test, or manual Log edits in window
  - Window may be too short — try /retro 1m or /retro 1q

No Research note written. Lock released.
```

Release lock per Step 0.1 and exit cleanly.

## Phase 3: Narrative + Price Overlay (parallel WebSearch + targeted fetches)

**Core engine**: per ticker, collect three signals — **newsflow**, **earnings** (if any landed in window), **price action** — then compute the narrative-price delta in Phase 4. Social sentiment is NOT collected (retail chatter, Twitter, Reddit all excluded per prior spec). The narrative channels here are OFFICIAL: press releases, SEC filings, earnings results and call transcripts, analyst upgrades/downgrades, major business news.

### 3.1: Three-channel query plan per ticker

For each `ticker ∈ TICKER_UNIVERSE`, issue three distinct queries. Each channel surfaces a separate input to classification.

| Channel | Query template | Extracts |
|---|---|---|
| **Price** | `[TICKER] stock price [WINDOW_START] to [TODAY] percentage change` | `window_price_move_pct`, intra-window volatility if visible |
| **News** | `[TICKER] news [WINDOW_START] to [TODAY] analyst rating earnings guidance M&A` | Major events (product launches, guidance updates, analyst actions, regulatory, M&A) — each with date + polarity (positive/negative/neutral) |
| **Earnings** | `[TICKER] earnings [WINDOW_START] to [TODAY] results call transcript guidance` | Results vs consensus, guidance direction, call-transcript key themes (only if an earnings event landed in the window) |

### 3.2: Parallel batch issuance

Issue the three queries per ticker **in the same parallel tool-call batch**. For a 42-ticker universe this is ~126 WebSearches; chunk into messages of up to 25 WebSearch invocations per message, producing ~5-6 rounds. Never serialize within a chunk — only between chunks. Mirrors `/catalyst` Phase 2's pattern at 3× the fan-out.

If `TICKER_UNIVERSE` is small (≤5 tickers), all 15 queries fit in one message.

### 3.3: Targeted fetches (earnings transcripts only)

If the Earnings WebSearch surfaces a canonical transcript URL (e.g., Seeking Alpha transcript page, company IR page, Motley Fool coverage), capture the URL but do NOT auto-fetch. Fetch selectively only when:

- An earnings event landed inside the window, AND
- The ticker already appears likely to rank in Top 5 by preliminary narrative-price gap (rough pre-screen on WebSearch snippets), AND
- The vault thesis has an active Log entry or addressed callout from the window (i.e., we care what the earnings said relative to our thinking)

For each qualifying URL, issue `defuddle [URL]` via Bash (preferred for transcript pages — strips navigation and comment noise) or `WebFetch` (fallback). Cap at **5 transcript fetches per retro run** — earnings transcripts are long (~8-15K tokens each); unbounded fetches would blow the subagent context budget. If >5 tickers qualify, fetch the top 5 by preliminary gap magnitude.

### 3.4: Extraction schema per ticker

```yaml
ticker: TICKER

price:
  window_move_pct: [number | null if unavailable]
  direction: up | down | flat | unknown           # threshold: ±3% (see Phase 4)
  max_intraday_move: [if visible in snippets, else null]

news:
  events: 
    - date: YYYY-MM-DD
      headline: [text]
      polarity: positive | negative | neutral
      source: [publication or snippet origin]
  dominant_polarity: positive | negative | neutral | mixed | none
    # Aggregated across events: count polarities, take dominant; none = no material event

earnings:
  event_in_window: true | false
  date: YYYY-MM-DD | null
  surprise_direction: beat | miss | inline | null
  guidance_direction: raised | lowered | maintained | withdrawn | null
  transcript_fetched: true | false
  transcript_themes: [list of 3-5 key themes if transcript was fetched, else null]

source_snippets: [top 2-3 audit-trail snippets per channel]
```

**If a channel returns nothing** (thinly-traded ticker with no news, no earnings in window, etc.), record `null` / `none` — downstream Phase 4 handles null channels without aborting the ticker.

## Phase 4: Three-Dimensional Classification

Per ticker, synthesize across three independent dimensions:

1. **VAULT_DIRECTION** — derived from Phase 2 extraction: `strengthened | weakened | mixed | neutral`
   - Aggregate addressed-callout resolutions + non-skill-origin Log entries. Classify each as strengthen/weaken/neutral. Dominant wins; ties → `mixed`; zero activity → `neutral`.

2. **NEWS_DIRECTION** — from Phase 3.4 `news.dominant_polarity`: `positive | negative | neutral | none`
   - If earnings event in window: roll earnings `surprise_direction` + `guidance_direction` into this bucket (beat + guidance raised → positive; miss + guidance lowered → negative; mixed → neutral).
   - `none` = no material news or earnings event surfaced.

3. **PRICE_DIRECTION** — from Phase 3.4 `price.direction`: `up | down | flat | unknown`
   - Threshold: `up` iff `window_move_pct > +3%`, `down` iff `< -3%`, else `flat`. Window-agnostic (1w, 1m, 1q all use ±3%) because absolute price moves — not annualized rates — determine whether the vault conclusion mattered by window end.

### 4.1: Primary signal — NARRATIVE-PRICE DELTA

The **narrative-price delta** is the core engine's output: compare NEWS_DIRECTION against PRICE_DIRECTION independent of vault stance.

| News direction | Price direction | Delta label | Interpretation |
|---|---|---|---|
| positive | up | **aligned-up** | Narrative priced correctly; limited alpha |
| negative | down | **aligned-down** | Narrative priced correctly; limited alpha |
| positive | down | **inverted-bear** | Good news, stock fell — positioning/forward-risk signal |
| negative | up | **inverted-bull** | Bad news, stock rose — short-covering, capitulation floor, or forward-relief signal |
| positive | flat | **unreactive-good** | Priced in OR market skeptical of narrative |
| negative | flat | **unreactive-bad** | Priced in OR market dismissive of concern |
| none | up (>3%) | **flow-bull** | No news catalyst — positioning, sector rotation, or hidden signal |
| none | down (>3%) | **flow-bear** | No news catalyst — positioning, sector rotation, or hidden signal |
| none | flat | **quiet** | Nothing to say; ticker drops out of ranking |
| neutral | any | **mixed** | News was genuinely mixed; classification inconclusive |
| any | unknown | **data-gap** | Price unavailable; classification inconclusive |

**Gap magnitude** — the ranking key in Phase 5:

```
gap_magnitude = 
  | inverted-bear  → 1.5 × |price_move_pct|   # highest-signal: good news sold into
  | inverted-bull  → 1.5 × |price_move_pct|   # highest-signal: bad news bought
  | flow-bull      → 1.0 × |price_move_pct|   # unsigned flow signal
  | flow-bear      → 1.0 × |price_move_pct|
  | unreactive-*   → 2.0                       # small but directionally relevant
  | aligned-*      → 0                         # already priced, no alpha
  | quiet/mixed/data-gap → 0
```

The 1.5× weight on inverted deltas reflects trader intuition: price rejecting narrative is a stronger signal than price confirming it. Confirmed narrative is consensus; rejected narrative is asymmetric information.

### 4.2: Secondary signal — VAULT STANCE vs DELTA

Once the narrative-price delta is computed, the vault's recent stance determines whether we have alpha or reflection to do.

| Delta | Vault direction | Read |
|---|---|---|
| inverted-bear | weakened | **Vault was right, ahead of market** — recent Log entries / addressed callouts weakened the thesis while market only now reacted. Harvest (trim, lock conviction). |
| inverted-bear | strengthened | **Vault fighting market** — vault strengthened view while market rejects positive narrative. Either vault sees through the surface catalyst (alpha) OR vault is wrong (reflection). Stress test. |
| inverted-bear | neutral / mixed | **Missed signal** — market moved on something vault didn't flag. Deepen the thesis; likely behind. |
| inverted-bull | strengthened | **Vault was right, ahead of market** — vault strengthened through bad news that market bought. Reinforce position. |
| inverted-bull | weakened | **Vault fighting market** — vault weakened while market bought the dip/news. Reassess; either vault too bearish or market wrong. |
| flow-bull / flow-bear | strengthened/weakened aligned | **Vault anticipated flow** — may be leading indicator. Consider action. |
| flow-bull / flow-bear | neutral | **Vault uninformed** — flow happening without vault view. Surface candidate for `/thesis` or `/deepen`. |
| unreactive-* | weakened/strengthened | **Positioning/timing bet** — vault has conviction, market deferring. Catalyst watch (see `/catalyst`). |
| aligned-* | any | **No action** — narrative and price agree; vault context is commentary, not alpha. |

### 4.3: Output schema per ticker

```yaml
ticker: TICKER
vault_direction: strengthened | weakened | mixed | neutral
news_direction: positive | negative | neutral | none
price_direction: up | down | flat | unknown
delta_label: aligned-up | aligned-down | inverted-bear | inverted-bull | unreactive-good | unreactive-bad | flow-bull | flow-bear | quiet | mixed | data-gap
gap_magnitude: [float]
read: [one-sentence interpretation from §4.2 matrix]
earnings_event_in_window: true | false
transcript_themes: [list or null]
```

### 4.4: Graph-primer aggregation

For each ticker with material classification (gap_magnitude > threshold of 3.0), consult the graph primer (if loaded in Step 0.4) for cluster peers. If ≥2 cluster peers share the same delta label → flag as **cluster-level signal** in the trade idea; otherwise idiosyncratic. Cluster-level inverted-bear across 3+ peers = sector rotation signal, not ticker-specific.

## Phase 5: Trade Ideas Ranking

Rank all tickers by `gap_magnitude` descending (from Phase 4.1). Top 3–5 populate the **Trade Ideas** section. Tickers with `gap_magnitude = 0` (aligned, quiet, mixed, data-gap) drop out — they carry no trade signal.

Each trade idea renders:

- **Ticker** + one-liner: `[delta_label] ([news summary] vs [price move]), vault [vault_direction]`
- **Read** (from Phase 4.2 matrix): e.g., "Vault was right, ahead of market — harvest" or "Missed signal — deepen"
- **Narrative detail**: top 1-2 news events with polarity, earnings result if applicable, key transcript theme if fetched
- **Price detail**: window move %, intraday volatility if notable
- **Suggested action** (one of, mapped from §4.2 matrix):
  - `Harvest / trim` — vault was ahead, market just caught up
  - `Reinforce / add` — vault reading contradicted by surface, aligned with price direction
  - `Stress test` — vault fighting market, needs adversarial review → `/stress-test TICKER`
  - `Deepen` — vault missed the signal → `/deepen TICKER [section]`
  - `Monitor for catalyst` — vault conviction + unreactive price → `/catalyst` watch
  - `New thesis candidate` — flow move with no vault view → `/thesis TICKER` or `/ingest`
- **Motivating evidence**: wikilinks to the specific addressed callout(s) + Log entry(ies) + news headline that drove the classification
- **Cluster flag**: if Phase 4.4 surfaced cluster-level signal (`≥2 peers same delta`), prefix the read with `[cluster signal]` and list peers. Sector rotation trumps ticker-specific action.

**Never auto-execute**. Phase 7 optionally appends a `Retro insight:` Log entry to the affected thesis (see §7.1), but conviction and status changes require explicit user `/status` invocation.

## Phase 6: Output — Research Note (immutable)

### 6.1: Filename

`Research/YYYY-MM-DD - Retrospective [window-label] - Synthesis.md`

Examples:
- `Research/2026-04-24 - Retrospective 1w - Synthesis.md`
- `Research/2026-04-24 - Retrospective 1m - Synthesis.md`

If a file with this exact name exists (same window already generated today), append numeric suffix: `... Synthesis 2.md`, `... Synthesis 3.md`. Each retro is a new immutable artifact (per user spec #3).

### 6.2: Frontmatter

```yaml
---
date: YYYY-MM-DD
tags: [research, retrospective, synthesis]
status: active
source: vault retrospective
source_type: retrospective
window: 1w | 1m | 1q
window_start: YYYY-MM-DD
window_end: YYYY-MM-DD
tickers_touched: [TICKER1, TICKER2, ...]
propagated_to: []
---
```

> **Why `propagated_to: []`**: retro notes are exploratory portfolio-level metadata, not per-thesis evidence. The body wikilinks reference many theses for context, NOT to claim each one needs a Log entry from `/sync`. The empty list is a **terminal dedup signal** to `/sync` Step 1 Check 2 — the producer skill (this `/retro` run) explicitly declares "no propagation needed." Without it, the next `/sync` would treat each body wikilink as a propagation target. Mirrors `/surface`'s pattern.

> **Graph update deferred**: `_graph.md` is owned exclusively by `/graph`. After `/retro`, run `/graph last` to register the retro research note in the dependency map.

### 6.3: Body structure

```markdown
# Retrospective: [window-label] ([WINDOW_START] → [TODAY])

## Scope
- Window: [window-label] — [N] days
- Files scanned: [N] theses + [M] sectors + [K] macros
- Tickers with activity: [N]
- Addressed callouts: [N]
- Fresh (unresolved) callouts: [N]
- Log entries (non-skill-origin): [N]

## Trade Ideas (Top 5 by Narrative-Price Gap)
[ranked table — see Phase 5]

## Narrative vs Price vs Vault
[per-ticker table, sorted by gap_magnitude descending]

| Ticker | News | Earnings | Price | Vault | Delta | Gap | Read |
|---|---|---|---|---|---|---|---|
| NVDA | positive (guide raise, 2 upgrades) | beat + raised | -7.2% | weakened | inverted-bear | 10.8 | Vault ahead — harvest |
| BESI | positive (design win) | none | +0.4% | strengthened | unreactive-good | 2.0 | Positioning; catalyst watch |
| APP | none | none | +8.1% | neutral | flow-bull | 8.1 | Missed signal — investigate |
| AMD | negative (guide cut) | miss + lowered | +4.5% | strengthened | inverted-bull | 6.8 | Vault right — reinforce |

Column semantics:
- **News**: dominant polarity + 1-2 key events
- **Earnings**: surprise direction + guidance direction, or `none` if no event in window
- **Price**: window move %, threshold-flagged (`up`/`down`/`flat`) by ±3%
- **Vault**: direction derived from Phase 2 callout + Log aggregation
- **Delta**: label from Phase 4.1 narrative-price matrix
- **Gap**: `gap_magnitude` (ranking key)
- **Read**: one-phrase interpretation from Phase 4.2 vault-stance matrix

## What I Resolved
[per user spec #4 — proportional to window]

## What I Still Have Open
[fresh callouts with wikilink back to source file:section]

## Activity Log
[non-skill-origin Log entries, grouped by ticker then date descending]

## Portfolio-Level Activity
[sector/macro callouts + Log entries not keyed to a single ticker]

## Follow-up Skills
[concrete `/deepen`, `/stress-test`, `/status` commands the user can run next]
```

### 6.4: "What I Resolved" — proportional rendering (user spec #4)

| Window | Rendering per addressed callout |
|---|---|
| `1w` | Full callout body + full response. Grouped by ticker, then by addressed date descending. |
| `1m` | Compressed: `YYYY-MM-DD · [ticker] · [section] — [one-line summary of question] → [one-line summary of response key insight]`. Full text archived via wikilink back to source file. |
| `1q` | Aggregated by ticker: `TICKER: [N] callouts addressed across sections [list]. Top 2 insights: [one-line each, chosen by conviction-impact proxy — prefer entries that surfaced in Trade Ideas ranking].` Full text available via wikilink. |

The rendering tier is a function of window length, not of callout count. A 1w retro with 40 callouts still renders full — the reader chose the tight window to get the full record.

### 6.5: "What I Still Have Open"

Fresh callouts in window, sorted by age descending (oldest fresh = most urgent):

```
- **[YYYY-MM-DD]** · [type] · [[file:section]] — [body one-liner]
```

Pinned fresh callouts render with `· pinned` marker — informational, signals user chose not to address.

### 6.6: Follow-up skills block

For each top-5 Trade Idea, emit the exact command(s) the user would type. Command selection is driven by the Phase 4.2 vault-stance-vs-delta matrix:

```
- [[NVDA - Nvidia]]: inverted-bear (news+, price -7.2%), vault weakened — harvest signal.
  - `/status NVDA conviction high→medium` — lock the read vault already made
  - `/brief NVDA` — generate IC-ready pitch for partial trim sizing

- [[APP - AppLovin]]: flow-bull (no news, price +8.1%), vault neutral — missed signal.
  - `/ingest https://[news-url]` — seed Research with what moved the tape
  - `/thesis APP` — vault has no view; decide whether to formalize

- [[AMD - Advanced Micro Devices]]: inverted-bull (guide cut, price +4.5%), vault strengthened — reinforce.
  - `/deepen AMD "Key Non-consensus Insights"` — articulate why vault sees through the miss

- [[BESI - BE Semiconductor]]: unreactive-good (design win, price +0.4%), vault strengthened — catalyst watch.
  - `/catalyst` — confirm BESI next catalyst date; position ahead
```

The retro never executes any of these — it lists them. The user decides which to run.

## Phase 7: Thesis Log Entries (top 3–5 only)

### 7.1: Scope

Append one `Retro insight:` Log entry to the thesis of each ticker in the Trade Ideas Top 3 (NOT all top-5 — limit Log pollution to the highest-signal divergences). Tickers ranked #4-#5 are surfaced in the retro note only.

### 7.2: Format

```
### <TODAY>
- Retro insight: [1w|1m|1q] retro — [delta_label] (news [+|-|none], price [±X.X%]) vs vault [direction]. [One-sentence read from §4.2 matrix]. See [[Research/YYYY-MM-DD - Retrospective [window] - Synthesis]].
```

Example:
```
- Retro insight: 1w retro — inverted-bear (news +, price -7.2%) vs vault weakened. Vault was ahead of market on hyperscaler demand softening — harvest signal. See [[Research/2026-04-24 - Retrospective 1w - Synthesis]].
```

**Prefix choice**: `Retro insight:` is NOT in `_shared/log-prefixes.md`'s skill-origin list (§47 enumeration). This is deliberate — per CLAUDE.md Workflow Rule 6, a non-skill-origin prefix forces the next `/sync` to treat the entry as research-driven and propagate normally to sector/macro notes. If the retro surfaces a divergence that materially changes sector-level thinking, `/sync` should pick it up.

### 7.3: Edit strategy (same-day append aware)

Use the same Case-4.3c.A / Case-4.3c.B two-path approach documented in `archive-callouts/SKILL.md` Phase 4.3c:

- If `### <TODAY>` header already exists in the thesis's `## Log`, append the bullet under the existing header. Never create a second same-day header; never reorder.
- If no `### <TODAY>` header exists, append a new dated section at end-of-file (Log is always the last section in the thesis template).

After each Edit, re-grep for the new bullet to verify it landed. Silent-failure retry with expanded context, per Phase 4.3c retry rules.

**If Log append fails after retry**: do NOT abort the retro. Body Research note is the primary artifact; Log back-references are a convenience. Report `⚠️ Log back-reference to [[TICKER]] failed — retro note persisted, manual append recommended.`

## Phase 8: `_hot.md` Update

Read `_hot.md` then edit per `_shared/hot-md-contract.md`. If `_hot.md` does not exist, create it per CLAUDE.md Rule #9 schema.

### 8.1: Active Research Thread

- **Same-topic continuation** (existing thread already covers `/retro` work): append a dated line `YYYY-MM-DD: [window] retro completed — top finding: [ticker + classification + key insight one-phrase].`
- **New topic**: compress the outgoing thread into a single `*Previous YYYY-MM-DD:*` line, prepend, then replace thread body with the retro summary above.

### 8.2: Open Questions

For each Top-5 Trade Idea where the delta label signals a vault-market mismatch, add an Open Question. The label → question-template mapping:

| Delta label + vault stance | Open Question template |
|---|---|
| `inverted-bear` + vault strengthened | `[[TICKER]]: narrative+ but price fell ([X%]) over [window] while vault strengthened. What forward risk is the market pricing that vault missed? (flagged by /retro YYYY-MM-DD)` |
| `inverted-bull` + vault weakened | `[[TICKER]]: narrative- but price rose ([X%]) over [window] while vault weakened. Is the bear case already discounted, or is vault over-focused on the miss? (flagged by /retro YYYY-MM-DD)` |
| `flow-bull` / `flow-bear` + vault neutral | `[[TICKER]]: stock moved [X%] over [window] with no catalyst and no vault view. What is the market seeing that vault hasn't formed a view on? (flagged by /retro YYYY-MM-DD)` |
| `unreactive-*` + vault strong direction | `[[TICKER]]: vault [direction] on [narrative] but price flat over [window]. What catalyst is needed to close the gap? (flagged by /retro YYYY-MM-DD)` |

Dedup: suppress only if an existing question contains BOTH the ticker wikilink AND the distinctive fragment `flagged by /retro`. Existing questions from `/thesis`, `/stress-test`, `/surface`, `/catalyst` must NOT suppress this — retro-specific dedup is narrow by design. Same rationale as `/catalyst` Phase 5 dedup logic (§148 of catalyst SKILL.md).

`aligned-*` deltas do NOT generate Open Questions — market agreed with narrative, no puzzle to investigate.

### 8.3: Other sections

- **Latest Sync**: not touched (owned by `/sync`).
- **Sync Archive**: not touched (owned by `/sync`).
- **Recent Conviction Changes**: not touched (owned by `/status`).
- **Portfolio Snapshot**: not touched (owned by `/sync`).

### 8.4: Word cap

After edits, count total. Over 4,000 → run compression trigger order per hot-md contract §Compression trigger order (drop oldest Sync Archive, drop oldest *Previous:* lines, merge duplicate Open Questions). Over 5,000 → abort `_hot.md` update with: `❌ _hot.md exceeds hard cap (5,000 words) after compression — retro note still persisted.`

Retro note write is unconditional; `_hot.md` update is best-effort.

## Phase 9: Release Lock and Report

### 9.1: Release

Final Bash block verifies ownership and releases:

```bash
LOCK_FILE=".vault-lock"
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ==="
else
  echo "⚠️ Lock ownership check failed at release — skipping rm to avoid stealing another skill's lock."
fi
```

Runs unconditionally — success, empty-window, WebSearch failures, Log-append failures all reach this step.

### 9.2: Report to user

```
## /retro [window-label] complete

Window:           [WINDOW_START] → [TODAY] ([N] days)
Files scanned:    [N] theses / [M] sectors / [K] macros
Addressed:        [N] callouts resolved
Still open:       [N] fresh callouts (oldest: [date], ticker: [X])
Log activity:     [N] non-skill-origin entries across [N] tickers
Market data:      [N] tickers with price; [N] news events; [N] earnings events; [N] transcripts fetched

Top narrative-price gaps (see full Research note for details):
  1. [TICKER] — [delta_label] ([news polarity] vs [price move]) — [one-phrase read]
  2. [TICKER] — [delta_label] ([news polarity] vs [price move]) — [one-phrase read]
  3. [TICKER] — [delta_label] ([news polarity] vs [price move]) — [one-phrase read]

Cluster signals: [list if any surfaced in Phase 4.4, else "none"]

Research note: [[Research/YYYY-MM-DD - Retrospective [window] - Synthesis]]
Log back-references appended to: [list up to 3 tickers]
_hot.md: [summary of section updates, or "no updates" if nothing changed]

Next steps:
  → Run /graph last to register the retro note in the dependency graph
  → Review Trade Ideas and decide whether to act via /status, /stress-test, /deepen, /ingest, or /thesis
```

**Runs in forked subagent** (`context: fork`) — main conversation context is shielded from ~60 full-file reads + up to ~126 WebSearch results + up to 5 earnings-transcript fetches (~400K tokens at current vault scale). Only the Phase 9.2 report returns to main session; the Research note persists to disk as the authoritative artifact.

## Invariants

1. **Immutable output** — each run creates a new Research note. Never overwrite an existing retro file; append counter suffix when filename collides.
2. **No conviction/status mutations** — Phase 5 Trade Ideas are informational. `/status` changes require explicit user invocation.
3. **`propagated_to: []` is terminal** — retro notes are metadata, not evidence; do not trigger fanout `/sync` propagation.
4. **`Retro insight:` is NOT a skill-origin prefix** — deliberate choice: allows `/sync` to propagate downstream sector/macro updates if a retro-surfaced divergence materially shifts sector thinking.
5. **Graph-primer is an orientation aid, never a filter** — per `_shared/graph-primer.md` anti-patterns. Retro reads every thesis in full regardless of cluster membership.
6. **Empty window exits cleanly** — Phase 2.5 short-circuit releases the lock and exits without writing.
7. **Lock is vault-wide** — prevents concurrent `/sync`, `/catalyst`, `/surface`, `/prune`, `/graph` from racing on shared reads.

## Failure modes and recovery

| Failure | Recovery |
|---|---|
| Lock acquisition fails | Hard-block with standard `/shared/preflight.md` §1.4 message. User waits or force-unlocks after verifying stale. |
| File Read fails mid-Phase-1 batch | Continue with successful reads; report `⚠️ N files unreadable — retro based on partial vault state.` Reduces signal fidelity, does not block output. |
| Price WebSearch fails for a ticker | Record `price.direction: unknown`; ticker classified as `data-gap`, drops to gap_magnitude = 0, excluded from Trade Ideas. Still appears in the Narrative vs Price table with `price: data unavailable`. |
| News WebSearch fails for a ticker | Record `news.dominant_polarity: none`; ticker uses price-only classification path (`flow-bull` / `flow-bear` / `quiet`). Reduced signal fidelity, still produces trade ideas if price move is material. |
| Earnings WebSearch fails for a ticker | Record `earnings.event_in_window: false` (defensive — we can't confirm). Ticker classified on news + price only. |
| Transcript fetch fails (defuddle / WebFetch) | Record `transcript_fetched: false`, `transcript_themes: null`. Earnings still contribute to `news_direction` via surprise + guidance fields. Note in the retro: `⚠️ transcript unavailable for [TICKER] — classification uses earnings result only.` |
| All Phase 3 WebSearch calls rate-limited | Skill continues; Phase 4 classification emits `data-gap` for every ticker. Market overlay section shows `⚠️ Market data unavailable for this run — retro shows vault activity only, no market classification. Re-run /retro later.` Vault-activity sections (Resolved / Still Open / Activity Log) still populate fully. |
| Phase 7 Log-append fails on a specific thesis | Report the specific file; retro note persists. Manual fix: append `Retro insight:` bullet per Phase 7.2 format. |
| `_hot.md` update fails hard-cap check | Retro note still persists. `_hot.md` unchanged. Report `⚠️ _hot.md at hard cap — skipped update. Manual cleanup needed.` |
| Empty window (no activity) | Phase 2.5 short-circuit — no note written, lock released. |
| Lock ownership lost (`LOCK_STOLEN`) | Abort immediately. Report which Phase was in-flight and whether the retro note landed. If retro note partially written, leave it (reviewable); do NOT attempt cleanup. |

## Cadence (operational suggestion)

Pair with `/cron` (see the `/schedule` skill). Suggested defaults:

- `/retro 1w` — every Friday evening
- `/retro 1m` — first trading day of the month
- `/retro 1q` — first trading day of the quarter

Each run produces an independent immutable artifact. The `/graph last` reconciliation should follow each retro to register the new Research note.

## Design notes

- **Why vault-wide lock (not read-only)**: retro writes a Research note, appends Log entries to 3-5 theses, and updates `_hot.md`. These writes conflict with concurrent `/sync` or `/catalyst`. Read-only lock is insufficient.
- **Why no scoped mode in v1**: single-ticker retro (`/retro 1w NVDA`) is a reasonable v2 extension. The vault-wide view is the v1 use case per the user's original framing ("recommend trades" across the portfolio). Scoped mode would add a resolution path + graph primer switch that v1 doesn't need.
- **Why `context: fork`**: ~60 full-file reads + up to ~126 WebSearch returns (3× ticker fan-out) + up to 5 earnings-transcript fetches = ~400K tokens of upstream material. Forking isolates the main conversation from this context consumption — only the Phase 9.2 report and the final Research note surface to the user's session.
- **Why narrative-price delta is the core engine**: "what did the market say happened vs what did the stock do" is the classical trader signal for positioning opportunities. Aligned narrative + price = already priced, no alpha. Inverted narrative + price = market is pricing something the surface news isn't showing — positioning, forward risk, capitulation, or vault's non-consensus view is right. The vault's recent stance then separates alpha (vault predicted the divergence) from reflection (vault missed it). This is why the 1.5× weight on inverted deltas vs 1.0× on flow-only signals: rejected narrative is asymmetric information, confirmed narrative is consensus.
- **Why exclude social sentiment**: per user spec — official narrative channels (press releases, SEC filings, earnings, analyst actions) are structured, date-anchored, and polarity-classifiable. Social sentiment (X/Twitter/Reddit) is noisy, hard to polarity-classify at scale, and typically echoes official narrative with a lag. Including it would expand WebSearch fan-out 2-3× without proportional signal gain.
- **Why cap transcript fetches at 5 per run**: earnings transcripts are ~8-15K tokens each. An uncapped fetch on a heavy-earnings week (5+ tickers reporting) would blow the subagent context budget. Pre-screen selects the 5 most likely to rank in Trade Ideas Top 5 — low-ranking earnings contribute via the Earnings WebSearch snippet (surprise + guidance direction) without the full transcript read.
- **Why proportional rendering** — per user spec. A 1q retro with 300 addressed callouts rendered in full would exceed the useful signal density of the note. Aggregation at long windows preserves the "what changed" signal without forcing the reader through 300 verbatim exchanges.
