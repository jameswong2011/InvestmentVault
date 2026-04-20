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

Two modes:

**Forward mode** (default): `$ARGUMENTS` describes the scenario (e.g., "Fed cuts 150bps", "China invades Taiwan", "oil spikes to $150", "AI capex disappoints by 40%", "major cybersecurity breach at a hyperscaler"). If empty, ask the user what scenario to model.

**Reverse mode**: `$ARGUMENTS` starts with the literal word `reverse` followed by a scenario research note identifier — either the wikilink (`[[Research/2026-04-19 - Scenario - Fed cut]]`), the path (`Research/2026-04-19 - Scenario - Fed cut.md`), or a partial-name disambiguator (e.g., `reverse Fed cut`).

- `/scenario reverse [[Research/2026-04-19 - Scenario - Fed cut]]`
- `/scenario reverse Research/2026-04-19 - Scenario - Fed cut.md`
- `/scenario reverse Fed cut` (skill resolves via grep on `Research/`)

Reverse mode appends a `Scenario REVERSED` Log entry (per `_shared/log-prefixes.md` §14) to every thesis previously affected by the named scenario, signaling that the prior propagation should be treated as no longer applicable. The scenario research note is **not deleted** — it remains as historical record. This respects CLAUDE.md Tier 2 append-only Log convention while providing an audit-trail-preserving undo path.

If `$ARGUMENTS` matches the reverse mode signature, jump to **Reverse Mode Flow** below. Otherwise, proceed to Phase 1 (forward mode).

## Phase 0: Pre-flight (MANDATORY — runs before Phase 1 or Reverse Mode Flow)

### 0.1: Acquire vault lock
Acquire a `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 10 minutes (scenario propagation can touch many theses). Capture the token, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block.

### 0.2: Rename-marker check
Glob `.rename_incomplete.*` at vault root. If ANY marker exists, hard-block — scenario propagation writes Major-impact Log entries to many theses; one mid-rename ticker in the affected set would have its Log entry keyed to the new name while some inbound references remain under the old name.

## Reverse Mode Flow

**Skip Phases 1–6 entirely. Reverse mode is a separate, bounded operation.**

### R1: Locate the scenario research note

1. Parse the argument (wikilink, path, or partial name).
2. If wikilink or path: read directly. Validate it exists under `Research/` and has `source_type: scenario`.
3. If partial name: glob `Research/*Scenario*.md` and grep frontmatter for `source_type: scenario`. Match the filename or "Scenario - [name]" portion against the partial. If multiple match, present the list and ask user to pick. If none, stop with `❌ No scenario research note matching '[partial]' found in Research/.`
4. Read the resolved note in full.

### R2: Identify previously-affected theses (archive-aware — 6.2 fix)

Two source-of-truth sets (use the union, deduplicate):

- **From `propagated_to:` frontmatter**: if present, every listed ticker received a Major-impact Log entry from the original `/scenario` run.
- **From body wikilinks**: parse the "Related Notes" section (or any `[[Theses/TICKER - Name]]` wikilinks in the body). These were referenced as Major OR Minor exposure.

Build the candidate target set as the union. **For each candidate ticker, first resolve the current location of its thesis file** (may have been archived since the scenario ran):

```
For each candidate ticker:
  Try: Glob Theses/TICKER - *.md → if exists, current_path = live path, location = "theses"
  Else Glob _Archive/TICKER - *.md → if exists, current_path = archive path, location = "archive"
  Else → location = "missing"

  If location == "missing":
    Add to R6 report under "Candidate skipped — thesis file not found": "[TICKER] was listed in propagated_to or body wikilinks but its file is not in Theses/ or _Archive/. Was it manually deleted?"
    Continue — do NOT add to any processing list.

  If location == "archive":
    Classify as archive-skipped:
      Read the archived thesis's ## Log section to confirm the original Scenario entry exists (for audit completeness in the R6 report).
      Add entry to `archive_skipped_theses` list: {ticker, archived_path, archive_date (from filename or frontmatter), had_scenario_entry: bool}.
      Do NOT modify the archived file — Tier 3 archive protection (CLAUDE.md Change Safety Rule).
    Continue — archived theses bypass the R4 Log append loop entirely.

  If location == "theses":
    Read the thesis's ## Log section.
    Search for any "Scenario [[Research/...scenario-name...]]" entry → match_scenario_entry: true | false
    Search for any "Scenario REVERSED [[Research/...scenario-name...]]" entry → match_reversed_entry: true | false
    
    Classify:
      - match_scenario_entry == false → exclude from reversal (thesis was body-wikilinked but never received producer Log entry — nothing to reverse). Log: `ℹ️ Skipped [TICKER] — no original Scenario Log entry found.`
      - match_scenario_entry == true AND match_reversed_entry == true → exclude (already reversed in a prior run). Log: `ℹ️ Skipped [TICKER] — Scenario REVERSED entry already exists for this scenario.`
      - match_scenario_entry == true AND match_reversed_entry == false → add to `affected_theses_live: [ticker]` with original Scenario entry's date.
```

> **Why filter on existing REVERSED entries**: re-running `/scenario reverse [same scenario]` (e.g., to retry partial failures from a prior run, or because the user forgot they already reversed it) would otherwise append a SECOND REVERSED entry to already-reversed theses. The original purpose of REVERSED is corrective signal preservation; duplicates inflate Log noise without semantic meaning. The filter makes the operation idempotent — re-running on a fully-reversed scenario is a no-op for already-handled theses; only theses that failed in the prior run (no REVERSED entry yet) are retried.

> **Why archived theses are skipped (6.2 — Tier 3 archive protection)**: CLAUDE.md Change Safety Rule #2 (Tier 3) classifies `_Archive/` content as archival record — never modified without explicit instruction. A thesis that received a Scenario Log entry and was subsequently closed / archived has its Log preserved as historical audit trail. Appending a `Scenario REVERSED` entry to the archived thesis would violate Tier 3 by silently editing archive content. Instead, the skill:
> 1. Records the skip in `archive_skipped_theses` with full context.
> 2. Surfaces the skip in the R6 report AND adds a "Reversal Notes" section to the scenario research note body documenting every archive-skipped ticker with rationale: "Thesis archived on [archive_date] after scenario propagation. Scenario Log entry preserved in archive as historical record. Reversal not applied to respect Tier 3 archive protection."
> 3. The scenario research note body thus carries the complete audit — any future review of the reversal finds both the live-ticker reversal Log entries AND the documented archive-skipped tickers. No silent gaps.

### R3: Confirm reverse intent (Tier 3 — mandatory)

```
Proposed scenario reversal:
  Scenario: [[Research/YYYY-MM-DD - Scenario - Name]]
  Originally propagated: [N] theses
  Will append "Scenario REVERSED" Log entry to: [list of affected_theses with dates]

  Rationale (required): [user provides one-line reason]

  This does NOT delete the scenario research note (preserved as history).
  This does NOT remove the original "Scenario" Log entries (Tier 2 append-only).
  Each affected thesis will receive a single new Log entry signaling reversal.

  /sync drift detection (Step 3e) treats "Scenario REVERSED" as drift-exclusion
  per _shared/log-prefixes.md §14.

Confirm? (y/n)
```

Wait for user confirmation AND the rationale text. If declined, exit.

### R4: Append reversal Log entries (live theses only — archived ones documented in note body)

**Iterate `affected_theses_live` ONLY** — never touch `archive_skipped_theses`. Archived theses were excluded in R2 for Tier 3 compliance.

For each live affected thesis, append (max 2 lines per CLAUDE.md):

```
### YYYY-MM-DD
- Scenario REVERSED [[Research/YYYY-MM-DD - Scenario - Name]]: original propagation withdrawn — [user rationale]. Original "Scenario" entry on [original-date] remains as historical record per Tier 2.
```

> **Drift coupling**: `/sync` Step 3e excludes entries starting with `"Scenario REVERSED"` from drift detection. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §14. Do not change this prefix without updating the registry and `/sync`; `/lint` check #29 flags drift.

**Failure handling and atomicity tracking**: same per-thesis loop as forward Phase 6.2 — track `reverse_succeeded: [tickers]` and `reverse_failed: [tickers, with reason]`. Do NOT abort on individual append failure; continue and report failures in R6.

### R4.5: Document archive-skipped theses in the scenario research note body (6.2 fix)

For each entry in `archive_skipped_theses` (from R2's archive-aware classification), append a line under a `## Reversal Notes` section in the scenario research note body (create the section if absent):

```
## Reversal Notes

### YYYY-MM-DD — Reversal applied
- Live theses with REVERSED Log entry: [list of tickers from reverse_succeeded]
- Archived theses not touched (Tier 3 archive protection):
  - [[_Archive/TICKER - Name]] — archived YYYY-MM-DD (prior to reversal date). Original Scenario Log entry preserved in archive. [rationale: user_rationale from R3]
  - ...
```

This keeps the scenario research note — the historical record per R5 "preserved as history" rule — as a complete audit. A future review of the reversal finds the live-ticker reversals in the theses AND the documented archive-skipped tickers in the research note body. Symmetry with forward-mode's body-wikilink-based audit trail.

**No retry marker required**: unlike `/sync`'s producer-skill atomicity (which uses `propagated_to:` to signal "already done"), reverse mode's idempotency is encoded in the Log itself — the existence of `Scenario REVERSED [[Research/...scenario]]` entry on a thesis is the dedup signal that R2's classifier reads on subsequent runs. So a partial failure leaves the failed theses without a REVERSED entry, and the next `/scenario reverse [same scenario]` invocation will re-classify them as needing reversal (R2 step `match_scenario_entry == true AND match_reversed_entry == false`) and retry them. No sidecar marker needed.

**Re-run pattern for partial failures**: if R6 reports `reverse_failed: [TICKER1 (reason), TICKER2 (reason)]`, the user runs `/scenario reverse [same scenario]` again. R2 classifies TICKER1/TICKER2 as still-needing-reversal (their Log has Scenario but not REVERSED), classifies all already-succeeded theses as already-reversed (excluded from this run), and R4 retries only the still-failing targets. Idempotent re-runs converge to fully-reversed state without duplicate REVERSED entries on already-handled theses.

### R5: Update _hot.md

Follow `.claude/skills/_shared/hot-md-contract.md`. Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: append a dated line: `YYYY-MM-DD: REVERSED scenario "[name]" across [N] theses — [user rationale]`. Do NOT compress prior thread (this is a corrective action, not a new research direction).
2. **Recent Conviction Changes**: add an entry: `- Scenario REVERSED: [[Research/...scenario-name]] across [N] theses — [user rationale]`
3. **Open Questions**: if the original scenario added questions ("research questions the scenario exposed"), surface them with a strikethrough resolution note: `- ~~[original question]~~ → Resolved YYYY-MM-DD: scenario reversed.`

**Word cap**: follow `.claude/skills/_shared/hot-md-contract.md` §"Compression trigger order" (soft 4,000 / hard 5,000).

### R6: Report

- **Mode**: `reverse`
- **Scenario**: `[[Research/YYYY-MM-DD - Scenario - Name]]` (preserved on disk — not deleted)
- **Theses with reversal Log entry appended (this run)**: [count] — [list of `reverse_succeeded`]
- **Theses skipped — already reversed in prior run**: [count] — [list from R2 classifier]. (No-op for these tickers; idempotent re-run.)
- **Theses skipped — no original Scenario Log entry**: [count] — [list]. (Body wikilinks but never received producer entry; nothing to reverse.)
- **Theses skipped — archived after scenario (Tier 3 protected)** (6.2): [count] — [list from `archive_skipped_theses` with archive_date]. Original Scenario Log entries preserved in archive. Documented in scenario research note body under `## Reversal Notes` section (see R4.5).
- **Candidates skipped — file missing**: [list of tickers whose file was not found in `Theses/` OR `_Archive/`]. These were in `propagated_to:` or body wikilinks but their file is not on disk. Likely manually deleted — investigate.
- **Failed appends (this run)**: [list of `reverse_failed` with reasons]. To retry: re-run `/scenario reverse [same scenario]` — R2's classifier will exclude the already-succeeded theses and retry only the still-failing ones.
- **`_hot.md` updated**: Active Research Thread + Recent Conviction Changes + Open Questions (if applicable)
- **No graph impact** — Log appends only.
- **Follow-up**: `→ Run /graph last to register the (already-changed-mtime) thesis files in incremental adjacency. /status changes (if any conviction was reversed alongside) are separate operations the user must run explicitly.`

**Stop here. Do not continue to forward mode phases.**

---

## Forward Mode (Phases 1–6)

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

> **Phase ordering (5.1 fix)**: Phase 6.1.5 (classification approval gate) runs BEFORE Phase 6.1 (research note write). If the user cancels at 6.1.5, no research note is written and no vault state changes. Execute in this order: **6.1.5 → 6.1 → 6.2 → 6.3**.

### 6.1: Write the research note (without `propagated_to:`)

**Only runs after Phase 6.1.5 approval.**

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

### 6.1.5: Classification approval gate (5.1 fix — mandatory before any Log append)

Before appending any Log entries, present the Phase 3 classification matrix to the user for explicit review. This catches both false-negative Major classifications (silently missing propagation) and false-positive Major classifications (Log clutter reversible only via `/scenario reverse`).

```
Scenario propagation about to begin. Review classification before Log appends land:

Major-impact theses — WILL receive Log entries ([N]):
  - [TICKER1] ([Company]): [transmission channel] — [impact direction + magnitude rationale]
  - [TICKER2] ([Company]): ...
  - ...

Minor-impact theses — will NOT receive Log entries ([M]):
  - [TICKER_a] ([Company]): [weak transmission rationale]
  - [TICKER_b] ([Company]): ...
  - ...

Neutral — no exposure identified ([K]):
  - [TICKER_x], [TICKER_y], ... (collapsed listing)

Options:
  (a) Approve — proceed with Log appends to listed Major-impact theses
  (b) Promote — move specific Minor-impact or Neutral theses to Major (provide comma-separated list)
  (c) Demote — downgrade specific Major-impact theses to Minor (provide comma-separated list)
  (d) Cancel — research note NOT written, no propagation

Confirm (a/b/c/d):
```

**Branch behavior**:
- **(a)**: proceed to 6.2 with the current Major-impact set.
- **(b) Promote**: user supplies tickers to upgrade. Merge into Major set. For each promoted ticker, the user provides a one-line rationale (required) that will appear in that ticker's Log entry in place of the auto-generated Phase 3 rationale. Re-present the updated classification for final (a) approval.
- **(c) Demote**: user supplies tickers to downgrade. Remove from Major set; add to Minor set. Re-present for final (a) approval.
- **(d)**: exit the skill silently. Research note file is NOT written (Phase 6.1 hasn't run yet — see ordering below). No vault state changes.

**Ordering note**: 6.1.5 runs BEFORE 6.1 (research note write). This is a change from prior ordering. Rationale: if the user cancels at 6.1.5, no half-written research note lingers; the scenario can be re-run cleanly with different parameters. Phase 6.1 is moved to after 6.1.5 approval.

**Why this gate is safe from approval fatigue**: `/scenario` is already a Tier 3 operation by nature (propagates to many theses at once). Adding one more explicit gate matches the existing `/prune` approval pattern — users expect `/scenario` to present its plan before executing, not auto-propagate based on LLM classification alone.

**Do NOT proceed silently past 6.1.5.** The gate is mandatory for forward mode; reverse mode (R3) has its own confirmation and is unaffected.

### 6.2: Append Log entries to all Major-impact theses

For each thesis rated **Major** impact in the Phase 3 table **AND approved at Phase 6.1.5**, attempt to append a Log entry (max 2 lines each):
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

**Word cap**: After all `_hot.md` edits, follow the compression trigger order in `.claude/skills/_shared/hot-md-contract.md` §"Compression trigger order": drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → emit warning. Soft cap 4,000 words, hard cap 5,000 words (abort `_hot.md` write on hard-cap breach; `/scenario` primary operation still succeeds).

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

## Phase 8: Release lock

After Phase 7's report (forward mode) or R6 report (reverse mode), release the vault lock per `.claude/skills/_shared/preflight.md` §1.7 as the skill's FINAL Bash block. Runs unconditionally — whether the scenario propagation succeeded, reverse mode completed, or the skill hit a non-fatal error.

```bash
# Lock release — verify ownership before rm (preflight §1.5)
LOCK_FILE=".vault-lock"
EXPECTED_TOKEN="<paste-token-captured-from-Phase-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ==="
else
  echo "⚠️ Lock ownership check failed at release — skipping rm to avoid stealing another skill's lock."
fi
```
