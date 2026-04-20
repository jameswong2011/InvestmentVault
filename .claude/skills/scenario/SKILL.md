---
name: scenario
description: Propagate a hypothetical macro scenario through the entire portfolio. Use when user says "what if", "scenario", "what happens to my portfolio if", or describes a macro event to model.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * defuddle *)
---

Map the impact of a macro scenario across every thesis, sector, and position in the vault.

Design rationale in `.claude/skills/scenario/RATIONALE.md` (§N.M anchors).

## Arguments

Two modes:

**Forward** (default): `$ARGUMENTS` describes the scenario (e.g., "Fed cuts 150bps", "China invades Taiwan", "oil spikes to $150"). Empty → ask user.

**Reverse**: `$ARGUMENTS` starts with `reverse` + scenario research note identifier — wikilink, path, or partial-name:
- `/scenario reverse [[Research/2026-04-19 - Scenario - Fed cut]]`
- `/scenario reverse Research/2026-04-19 - Scenario - Fed cut.md`
- `/scenario reverse Fed cut` (resolves via grep)

Reverse mode appends `Scenario REVERSED` Log entry (registry §14) to every thesis previously affected. Scenario research note **not deleted** — preserved as historical record per Tier 2 append-only convention (§8). Provides audit-trail-preserving undo path.

Matches `reverse` → jump to **Reverse Mode Flow**. Otherwise → Phase 1.

## Phase 0: Pre-flight

### 0.1: Acquire vault lock

`vault-wide` scope per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout 10 min. Capture token, verify (Procedure 1.5) every subsequent block, release in final.

### 0.2: Vault-wide rename marker check (§7)

Glob `.rename_incomplete.*`. ANY marker → hard-block. All-or-nothing — cannot safely skip individual mid-rename tickers.

---

## Reverse Mode Flow

**Skip Phases 1-6. Separate bounded operation.**

### R1: Locate scenario research note

1. Parse argument (wikilink, path, or partial name).
2. Wikilink/path → read directly. Validate exists under `Research/` with `source_type: scenario`.
3. Partial name → glob `Research/*Scenario*.md`, grep frontmatter for `source_type: scenario`. Match filename or "Scenario - [name]" portion. Multiple → present list, ask user. None → `❌ No scenario research note matching '[partial]' found in Research/.` Stop.
4. Read resolved note in full.

### R2: Identify previously-affected theses (archive-aware — §1)

Union of two source-of-truth sets:
- **`propagated_to:` frontmatter**: every listed ticker received Major-impact Log entry from original run.
- **Body wikilinks**: `[[Theses/TICKER - Name]]` in "Related Notes" or body (Major or Minor exposure).

For each candidate ticker, resolve current location:

```
Try: Glob Theses/TICKER - *.md → if exists, current_path = live path, location = "theses"
Else Glob _Archive/TICKER - *.md → if exists, current_path = archive path, location = "archive"
Else → location = "missing"

If location == "missing":
  Add to R6 report under "Candidate skipped — thesis file not found":
  "[TICKER] was listed in propagated_to or body wikilinks but its file is not in Theses/ or _Archive/. Was it manually deleted?"
  Continue — do NOT add to processing list.

If location == "archive":
  Classify as archive-skipped (§1.1 — Tier 3 protection):
    Read archived thesis's ## Log to confirm original Scenario entry exists (audit completeness for R6).
    Add to `archive_skipped_theses`: {ticker, archived_path, archive_date, had_scenario_entry: bool}.
    Do NOT modify archived file.
  Continue — archived theses bypass R4 Log append loop entirely.

If location == "theses":
  Read thesis's ## Log section.
  Search for "Scenario [[Research/...scenario-name...]]" entry → match_scenario_entry: bool
  Search for "Scenario REVERSED [[Research/...scenario-name...]]" entry → match_reversed_entry: bool
  
  Classify (§2.4):
    - match_scenario_entry == false → exclude (body-wikilinked but never received producer entry; nothing to reverse). Log: `ℹ️ Skipped [TICKER] — no original Scenario Log entry found.`
    - match_scenario_entry == true AND match_reversed_entry == true → exclude (already reversed — §2.1). Log: `ℹ️ Skipped [TICKER] — Scenario REVERSED entry already exists for this scenario.`
    - match_scenario_entry == true AND match_reversed_entry == false → add to `affected_theses_live: [ticker]` with original Scenario entry's date.
```

### R3: Confirm reverse intent (Tier 3 — Mandatory)

```
Proposed scenario reversal:
  Scenario: [[Research/YYYY-MM-DD - Scenario - Name]]
  Originally propagated: [N] theses
  Will append "Scenario REVERSED" Log entry to: [list of affected_theses_live with dates]

  Rationale (required): [user provides one-line reason]

  This does NOT delete the scenario research note (preserved as history).
  This does NOT remove the original "Scenario" Log entries (Tier 2 append-only).
  Each affected thesis will receive a single new Log entry signaling reversal.

  /sync drift detection (Step 3e) treats "Scenario REVERSED" as drift-exclusion
  per _shared/log-prefixes.md §14.

Confirm? (y/n)
```

Wait for user confirmation AND rationale text. Declined → exit.

### R4: Append reversal Log entries (live theses only)

**Iterate `affected_theses_live` ONLY** — never touch `archive_skipped_theses` (Tier 3).

Per live affected thesis, append (max 2 lines per CLAUDE.md):

```
### YYYY-MM-DD
- Scenario REVERSED [[Research/YYYY-MM-DD - Scenario - Name]]: original propagation withdrawn — [user rationale]. Original "Scenario" entry on [original-date] remains as historical record per Tier 2.
```

Prefix `"Scenario REVERSED"` — `/sync` Step 3e drift-exclusion (registry §14). Do not change without updating registry + `/sync`; `/lint #29` flags drift.

**Failure handling + atomicity tracking** (§2.3): track `reverse_succeeded: [tickers]` and `reverse_failed: [tickers, reason]`. Do NOT abort on individual append failure; continue and report in R6.

### R4.5: Document archive-skipped theses in scenario research note body (§1.2)

For each entry in `archive_skipped_theses` from R2, append under `## Reversal Notes` in scenario research note body (create section if absent):

```
## Reversal Notes

### YYYY-MM-DD — Reversal applied
- Live theses with REVERSED Log entry: [list from reverse_succeeded]
- Archived theses not touched (Tier 3 archive protection):
  - [[_Archive/TICKER - Name]] — archived YYYY-MM-DD (prior to reversal date). Original Scenario Log entry preserved in archive. [rationale: user_rationale from R3]
  - ...
```

Symmetry with forward-mode's body-wikilink audit trail.

### R5: Update _hot.md

Per `.claude/skills/_shared/hot-md-contract.md` (do NOT touch Latest Sync / Sync Archive):

1. **Active Research Thread**: append dated line `YYYY-MM-DD: REVERSED scenario "[name]" across [N] theses — [user rationale]`. Do NOT compress prior thread (corrective action, not new direction).
2. **Recent Conviction Changes**: add `- Scenario REVERSED: [[Research/...scenario-name]] across [N] theses — [user rationale]`.
3. **Open Questions**: if original scenario added questions, surface with strikethrough: `- ~~[original question]~~ → Resolved YYYY-MM-DD: scenario reversed.`

Word cap: standard 4,000 soft-cap check per `_shared/hot-md-contract.md`; prune Sync Archive (oldest first) if over; abort _hot.md update if over 5,000 hard cap.

### R6: Report

- **Mode**: `reverse`
- **Scenario**: `[[Research/YYYY-MM-DD - Scenario - Name]]` (preserved on disk — not deleted)
- **Theses with reversal Log entry appended (this run)**: [count] — [list of `reverse_succeeded`]
- **Theses skipped — already reversed in prior run**: [count] — [list from R2 classifier]. No-op; idempotent.
- **Theses skipped — no original Scenario Log entry**: [count] — [list]. Body wikilinks only; nothing to reverse.
- **Theses skipped — archived after scenario (Tier 3 protected)**: [count] — [list from `archive_skipped_theses` with archive_date]. Original Scenario Log entries preserved in archive. Documented in scenario note body under `## Reversal Notes` (R4.5).
- **Candidates skipped — file missing**: [list of tickers where file not in Theses/ OR _Archive/]. In propagated_to or body wikilinks but file not on disk. Likely manually deleted — investigate.
- **Failed appends (this run)**: [list of `reverse_failed` with reasons]. To retry: re-run `/scenario reverse [same scenario]` — R2 classifier excludes succeeded, retries still-failing only (§2.3).
- **`_hot.md` updated**: Active Research Thread + Recent Conviction Changes + Open Questions (if applicable)
- **No graph impact** — Log appends only.
- **Follow-up**: `→ Run /graph last to register the (already-changed-mtime) thesis files in incremental adjacency. /status changes (if any conviction was reversed alongside) are separate operations the user must run explicitly.`

**Stop here. Do not continue to forward mode.**

---

## Forward Mode (Phases 1-6)

## Phase 1: Define the Scenario

- State scenario precisely with quantitative parameters where possible
- Identify primary transmission channels: rates, FX, commodity prices, supply chains, demand destruction, regulatory, sentiment, capital flows
- Set time horizon (default: 6 months)
- Rough probability estimate (calibration for tail-risk seriousness)

## Phase 2: Read the Portfolio (Two-Pass Triage — §6)

### Pass 1 — Lightweight scan

1. Read all Macro notes in full (small set, highest scenario relevance).
2. Read `_graph.md` for portfolio topology and cross-thesis clusters.
3. Per thesis in Theses/, read **frontmatter + Summary only** (~200 words per thesis).

### Pass 2 — Triage and deep read

4. Using summaries + macro context + Phase 1 transmission channels, classify each thesis (§6.2):
   - **High exposure**: direct transmission channel → read **full thesis note + sector note**
   - **Low exposure**: indirect or second-order only → read **Summary + Risks + Bull/Bear Case**
   - **No exposure**: no plausible transmission → do NOT read further. Carry summary forward; mark Neutral in Phase 3.

5. Read sector notes ONLY for sectors with at least one High-exposure thesis (§6.3).

Reduces deep-read set from ~58 files to 15-20.

## Phase 3: First-Order Impact Assessment

Per thesis (all, including No-exposure as Neutral):

| Ticker | Company | Conviction | Direct Impact | Magnitude | Transmission Channel | Key Assumption at Risk |
|---|---|---|---|---|---|---|
| | | [H/M/L] | [Positive/Negative/Neutral] | [Major/Minor] | [How scenario affects this position] | [Which bull/bear assumption is tested] |

Sort by magnitude of impact (major negatives first).

## Phase 4: Second and Third-Order Effects

Highest-value phase — trace cascades:

**Supply chain cascades**: If Company A is disrupted, who loses a critical supplier? Who gains? Single points of failure in documented value chains?

**Demand substitution**: If one product/sector suffers, where does demand rotate? Which theses are on the receiving end?

**Relative winners within sectors**: Within each affected sector, who gains market share? Does the scenario accelerate or decelerate competitive dynamics already documented?

**Funding, valuation, sentiment**: How do multiples compress or expand? Does risk-off hit some harder due to liquidity, positioning, narrative fragility?

**Portfolio correlations revealed**: Which positions appear diversified but are actually correlated under this scenario? Effective concentration after scenario-driven correlation?

## Phase 5: Portfolio-Level Assessment

- **Net portfolio impact**: directional estimate + rough magnitude
- **Worst-case cluster**: which 3-4 theses get hit simultaneously and hardest?
- **Concentration risk exposed**: scenario reveal hidden concentration?
- **Natural hedges**: positions that offset each other under this scenario?
- **Hedge gaps**: what would protect portfolio but isn't currently held?
- **Opportunities created**: dislocations that become new thesis candidates?

## Phase 6: Output

**Phase ordering** (§5.1): **6.1.5 → 6.1 → 6.2 → 6.3**. If user cancels at 6.1.5, no research note written (§3.2).

### 6.1.5: Classification approval gate (§3 — Mandatory)

**Before any Log append**, present Phase 3 classification matrix for explicit review. Catches false-negative Majors (silent miss) and false-positive Majors (reversible only via /scenario reverse).

```
Scenario propagation about to begin. Review classification before Log appends land:

Major-impact theses — WILL receive Log entries ([N]):
  - [TICKER1] ([Company]): [transmission channel] — [impact direction + magnitude rationale]
  - [TICKER2] ([Company]): ...

Minor-impact theses — will NOT receive Log entries ([M]):
  - [TICKER_a] ([Company]): [weak transmission rationale]
  - [TICKER_b] ([Company]): ...

Neutral — no exposure identified ([K]):
  - [TICKER_x], [TICKER_y], ... (collapsed listing)

Options:
  (a) Approve — proceed with Log appends to listed Major-impact theses
  (b) Promote — move specific Minor-impact or Neutral theses to Major (provide comma-separated list)
  (c) Demote — downgrade specific Major-impact theses to Minor (provide comma-separated list)
  (d) Cancel — research note NOT written, no propagation

Confirm (a/b/c/d):
```

**Branch behavior** (§3.4):
- **(a)**: proceed to 6.1 with current Major-impact set.
- **(b) Promote**: user supplies tickers. Merge into Major set. Per promoted ticker, user supplies one-line rationale (required) replacing auto-generated Phase 3 rationale in Log entry. Re-present for final (a) approval.
- **(c) Demote**: user supplies tickers. Remove from Major; add to Minor. Re-present for final (a) approval.
- **(d)**: exit silently. Research note NOT written. No vault changes.

**Do NOT proceed silently past 6.1.5.** Mandatory for forward mode; reverse mode (R3) has its own confirmation.

### 6.1: Write the research note

**Only runs after Phase 6.1.5 approval.**

Save to `Research/YYYY-MM-DD - Scenario - [Short Scenario Name].md`:
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
2. Impact Matrix (Phase 3 table)
3. Second-Order Effects (Phase 4 narrative)
4. Portfolio Assessment (Phase 5)
5. Recommended Actions (specific hedges, position adjustments, research priorities)
6. Related Notes (wikilinks to all theses and macro notes referenced)

### 6.2: Append Log entries to all Major-impact theses

For each Major-impact thesis AND approved at 6.1.5, attempt Log append (max 2 lines):

```
### YYYY-MM-DD
- Scenario [[Research/YYYY-MM-DD - Scenario - Short Name]]: [impact direction via transmission channel] — conviction [unchanged/strengthened/weakened + reason]
```

For each that received Log entry, add scenario to `## Related Research` (if not already present):
```
- [[Research/YYYY-MM-DD - Scenario - Short Name]]
```

**Track outcomes per ticker**: maintain `succeeded: [tickers]` and `failed: [tickers, reason]`. Failure = Log append Edit failed (file locked, missing `## Log` section, malformed frontmatter). Do NOT abort loop on single failure — continue attempting remaining Major targets.

### 6.3: Atomicity rule for `propagated_to:` (§4)

Update research note's `propagated_to:` frontmatter **only after EVERY Major-impact thesis's Log entry has landed successfully**.

- **All appends succeeded** (`failed:` empty): edit research note frontmatter → add `propagated_to: [TICKER1, TICKER2, ...]`. Signals to subsequent `/sync` that producer-side propagation is complete; `/sync` Case 2b skips as already-propagated.
- **One or more failed** (`failed:` non-empty): do **NOT** write `propagated_to:` at all. Leave field absent. Next `/sync` detects each Major-impact thesis via file-direct fallback (research note body wikilinks every Major under "Related Notes"), checks per-thesis idempotency (wikilink-presence in Log), re-attempts append for failed targets.

**Why never partial** (§4.1-§4.2): partial `propagated_to:` would claim failed-target tickers as propagated when their Log entries never landed → permanent audit gap → future `/sync` silently skips. All-or-nothing trades minor `/sync` re-work for guaranteed eventual consistency.

**Per-failure reporting**: list every failed ticker in Phase 7 report under `Major-impact Log appends — failed: [TICKER1 (reason), TICKER2 (reason)]`.

### _hot.md update

Per `.claude/skills/_shared/hot-md-contract.md` (do NOT touch Latest Sync / Sync Archive):

1. **Active Research Thread**: same-ticker continuation per contract. Write: scenario modelled ([short name]), top 3 exposed positions, single most important action.
2. **Recent Conviction Changes**: add entry per ticker where conviction was strengthened or weakened.
3. **Open Questions**: add research questions scenario exposed (unquantified exposures, missing hedges).

Word cap: after edits, total >4,000 (soft cap per `_shared/hot-md-contract.md`) → prune `## Sync Archive` (oldest first) then `*Previous:*` lines. Abort if over 5,000 hard cap.

**Graph update deferred**: `_graph.md` owned exclusively by `/graph`. Run `/graph last` to register scenario research note and new cross-thesis correlations.

## Phase 7: Report

1. **Top 3 most exposed positions** with transmission channel.
2. **Biggest beneficiary** with rationale.
3. **Single most important action** to take now.
4. **Major-impact propagation status**:
   - `Major-impact theses propagated: [N] of [M]` (succeeded list)
   - `propagated_to: frontmatter` — `set` (all succeeded) | `omitted (one or more appends failed — next /sync will retry)`
   - **Failed appends** (only if any): `[TICKER1 (reason), TICKER2 (reason)]`
5. **Follow-up**: `→ Run /sync to propagate to minor-impact theses and retry any failed Major appends. Then /graph last.`
