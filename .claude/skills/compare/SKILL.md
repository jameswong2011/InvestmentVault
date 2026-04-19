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

### 5.1: Write the comparison research note (without `propagated_to:`)

Save to `Research/YYYY-MM-DD - [TICKER A] vs [TICKER B] - Competitive Comparison.md` with:
```yaml
---
date: YYYY-MM-DD
tags: [research, comparison, SECTOR, TICKER_A, TICKER_B]
sector: [shared sector]
source: vault synthesis
source_type: comparison
# propagated_to: omitted intentionally — set in Phase 5.4 only after every Log append succeeds
---
```

> **Why omitted at write time**: mirrors `/scenario` Phase 6.1 + 6.3 atomicity. If any per-thesis Log append in Phase 5.2 fails (file lock, missing `## Log` section, malformed thesis frontmatter), pre-writing `propagated_to: [...]` would falsely claim every listed ticker received its Log entry. Future `/sync` Case 2b would skip them all, never retrying the failed appends — permanent audit gap. The all-or-nothing rule trades a single trivial frontmatter Edit at Phase 5.4 for guaranteed eventual consistency.

### 5.2: Per-thesis Log append (track per-ticker outcomes)

**Vault updates** — apply ONLY to tickers with existing thesis notes. Skip for web-supplemented tickers (Phase 0 option a).

For each thesis with an existing thesis note, attempt to append a Log entry (max 2 lines each):
```
### YYYY-MM-DD
- [[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]: [key competitive insight] — conviction [unchanged/strengthened/weakened + reason]
```

**Track per-ticker outcomes**: maintain two lists during this phase — `succeeded: [tickers]` and `failed: [tickers, with reason]`. A failure means the Log append Edit failed (file locked, missing `## Log` section, malformed frontmatter, etc.). Do NOT abort the loop on a single failure — continue attempting the remaining theses so partial propagation completes.

### 5.3: Add to Related Research (independent of Log append outcome)

For each compared thesis with an existing thesis note, add the comparison to its `## Related Research` section (if not already present):
```
- [[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]
```

This is wikilink registration, not a propagation claim — runs regardless of per-thesis 5.2 outcome. Related Research is a presence record; `propagated_to:` is the propagation contract.

### 5.4: Atomicity rule for `propagated_to:` update

**Update the research note's `propagated_to:` frontmatter only after EVERY thesis-with-existing-note Log append has landed successfully.** Mirrors `/scenario` Phase 6.3.

- **All appends succeeded** (`failed:` list empty): edit the research note's frontmatter to add `propagated_to: [TICKER1, TICKER2, ...]` listing all tickers that had existing thesis notes. Insertion point: immediately before the closing `---` of frontmatter. This signals to subsequent `/sync` runs that producer-side propagation is complete; `/sync` Case 2b will skip these tickers as already-propagated.
- **One or more appends failed** (`failed:` list non-empty): do **NOT** write `propagated_to:` at all. Leave the frontmatter without the field. The next `/sync` (default mode) will detect each thesis-with-existing-note via the file-direct fallback (research note's `tags:` and body wikilinks list each compared ticker), check today's-date idempotency per thesis, and re-attempt the append for the failed targets. Succeeded targets are skipped via the per-thesis idempotency check (today-date entry exists).

> **Why never partial**: A partial `propagated_to:` would claim some failed-target tickers as propagated when their Log entries never landed, creating a permanent audit gap that future `/sync` runs silently skip. The all-or-nothing rule trades minor `/sync` re-work (succeeded targets get re-evaluated and skipped via per-thesis idempotency) for guaranteed eventual consistency.

**Per-failure reporting**: list every failed ticker in the Phase 6 report (final user-facing summary) under a new field `Per-thesis Log appends — failed: [TICKER1 (reason), TICKER2 (reason)]`. The user can inspect each failure or simply re-run `/sync` to let the universal propagation mechanism catch up.

Update the Sector Note if the comparison reveals competitive dynamics not already documented. Resolve the sector note via canonical procedure **`.claude/skills/_shared/sector-resolution.md`** using each compared thesis's `sector:` frontmatter.

**Resolution rules:**
- **All compared theses share the same sector** → resolve once, update one sector note. Single-sector batch.
- **Compared theses span different sectors** → resolve each unique sector separately. Update each corresponding sector note independently. **Cross-sector batch**: sector updates are logically independent — a future `/rollback` on one sector should NOT cascade into the other.

**Confidence handling** (same rules per resolved sector note): if `match_confidence` is `none` for a given sector, emit the contract's no-match warning for that sector and skip sector update for those theses (but continue processing other sectors). If `normalized` or `substring`, emit the contract's `log_message`; if `substring`, additionally pause for explicit user confirmation before modifying analytical text.

### Snapshot batch ID — per sector, not per run

If modifying existing analytical text (competitive dynamics, value chain, company comparisons) — not just adding links — snapshot first. Generate a DISTINCT `snapshot_batch` value for EACH sector note being modified. The batch ID template embeds the sector slug so cascade detection scopes cleanly to one sector:

```bash
mkdir -p _Archive/Snapshots
HHMMSS=$(date +%H%M%S)
# For each sector note being updated, use its own slug:
SECTOR_SLUG=$(echo "Sector Name" | tr '[:upper:]' '[:lower:]' | tr ' &/' '--')
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-compare YYYY-MM-DD-HHMMSSSS).md"
```
> **6-digit second-precision** (HHMMSS) prevents same-minute snapshot batch collisions across skills.
Read each newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: compare
snapshot_batch: compare-[sector-slug]-YYYY-MM-DD-HHMMSS
```

**Why the slug matters**: `/rollback` Step 2.5 groups snapshots by `snapshot_batch` for cascade detection. If two sector notes share the batch `compare-2026-04-19-1530`, a rollback of one offers to cascade-restore the other — coupling unrelated sectors. By scoping the batch to `compare-semiconductors-2026-04-19-1530` vs. `compare-cybersecurity-2026-04-19-1530`, cascade detection only couples snapshots that truly belong together (e.g., if a future skill snapshots the same semiconductors sector note in the same run, it would share the semiconductors-scoped batch).

**Single-sector case**: when all compared theses share one sector, there's only one sector note and the slug is still included for consistency (`compare-semiconductors-YYYY-MM-DD-HHMMSS`) — this keeps the batch-ID format uniform regardless of sector count.

**Thesis log entries**: across all compared theses — regardless of sector — use a shared sessional tag in the Log entries for audit readability (e.g., referencing the same research note wikilink). Thesis Log entries do not use `snapshot_batch` (they aren't snapshots), so there's no cascade-coupling risk at the Log-entry level.

**Modify the original sector note using targeted `Edit` operations (atomic string replacement per section), NOT full-file `Write`.** Each `Edit` call either succeeds atomically or leaves the section unchanged — this limits the blast radius of a mid-edit failure to zero (partial writes cannot occur). Apply one `Edit` per modified section (e.g., one for competitive dynamics, one for value chain).

**Post-edit verification**: After all edits, re-read the modified sector note. For each edited section, verify it ends with a complete sentence (not mid-word, mid-sentence, or with unclosed formatting markers). If verification fails: `⚠️ Sector note may contain a partial edit in [section]. Snapshot available: [[_Archive/Snapshots/...]]. Review manually or /rollback.`

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the comparison research note and any new cross-thesis connections in the dependency map.

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: compared [TICKER A] vs [TICKER B], key competitive insight, and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry for each ticker where conviction was strengthened or weakened
3. **Open Questions**: Add any unresolved competitive questions the comparison surfaced

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Phase 6: Report

Report to user, including:

1. **Comparison research note**: `[[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]`
2. **The single most important competitive insight** and whether it changes conviction on either name.
3. **Per-thesis Log appends** (Phase 5.2 outcome):
   - `Theses with existing notes propagated: [N] of [M]` (succeeded list)
   - `propagated_to: frontmatter` — `set ([TICKER1, TICKER2, ...])` (all succeeded) | `omitted (one or more appends failed — next /sync will retry)`
   - **Failed appends** (only if any): `[TICKER1 (reason), TICKER2 (reason)]`
4. **Web-supplemented tickers** (only if any from Phase 0 option a): `[TICKER1, TICKER2] — used web research, no vault updates. Consider /thesis [TICKER] to formalize coverage.`
5. **Sector notes updated**: list per sector with snapshot path or "no snapshot (link addition only)".
6. **Follow-up**: `→ Run /sync to propagate any sector note changes and retry failed Log appends. Then /graph last.`
