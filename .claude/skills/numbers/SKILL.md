---
name: numbers
description: Refresh the Key Metrics table in a thesis with current data from Financial Modeling Prep. Use when user says "numbers", "refresh metrics", "update key metrics", or "refresh [TICKER]" with no other action implied. Surgical edit only — does NOT create research notes or propagate via /sync.
model: sonnet
effort: medium
allowed-tools: Read Grep Glob Edit Bash(date * cp * mkdir * ls * curl * grep * cat * jq * printf * awk * sed *)
---

Refresh the **`## Key Metrics`** table in a thesis using live FMP data. Hygiene operation, not analysis — the skill changes only numeric cells, never the Notes column, never section text, never frontmatter analytical fields. Solves the staleness problem where every thesis's metrics are wrong 90 days after creation.

**This skill creates no research notes and emits a skill-origin Log prefix — `/sync` will NOT re-propagate to sector or macro notes.** If the refresh surfaces a material delta (e.g., gross margin dropped 500bps), the skill advises the user to follow up with `/deepen` or `/sync` manually.

## Arguments

`$ARGUMENTS` should match one of:

- **Single ticker**: `NVDA` — refresh one thesis
- **All active high-conviction**: `--all` — batch refresh every thesis where `status: active` AND `conviction: high`
- **All active**: `--all-active` — batch refresh every thesis where `status: active` (any conviction)

Ambiguous / empty → ask user to clarify ticker or batch scope.

## Step 0: Pre-flight (MANDATORY)

### 0.1: Acquire vault lock

Per `.claude/skills/_shared/preflight.md` Procedure 1:
- **Single ticker**: `ticker:TICKER` scope. Timeout 3 minutes.
- **`--all` / `--all-active`**: `vault-wide` scope. Timeout 10 minutes (one API cycle per ticker × N tickers, even at FMP wholesale tier).

Capture token at Step 0.1, verify ownership (Procedure 1.5) at every subsequent Bash block, release explicitly in the final block (Step 11).

### 0.2: Rename-marker pre-flight

Procedure 2.
- **Single ticker**: hard-block if `.rename_incomplete.TICKER` exists.
- **Batch modes**: glob `.rename_incomplete.*`; hard-block on any marker. Refresh would write to thesis files whose inbound wikilinks are still split mid-rename — surface for user resolution before proceeding.

### 0.3: FMP API key probe

```bash
if [ ! -f .data/config.json ]; then
  echo "❌ FMP API key config missing: .data/config.json"
  echo "   This skill requires .data/config.json containing fmp_api_key. See Live Portfolio.md for the canonical format."
  exit 1
fi
API_KEY=$(grep -E '"fmp_api_key"\s*:' .data/config.json | sed -E 's/.*"fmp_api_key"\s*:\s*"([^"]+)".*/\1/')
if [ -z "$API_KEY" ] || [ "$API_KEY" = "null" ]; then
  echo "❌ FMP API key missing or empty in .data/config.json"
  exit 1
fi
echo "FMP_KEY_OK"
```

On failure, abort the entire skill — no fallback to web scraping.

### 0.4: Section existence probe (per-thesis)

For every target thesis, run Procedure 4 against the `## Key Metrics` heading:

- **Hard abort** if missing on single-ticker mode: `❌ Section "## Key Metrics" not found in [path]. /numbers refreshes existing tables only — it does NOT create the section. Add the table manually (use Templates/Thesis Template.md as reference) then re-run /numbers.`
- **Graceful skip** in batch modes: log `ℹ️ [TICKER] missing ## Key Metrics — skipped.` and continue. Report skip count in final summary.

## Step 1: Resolve target thesis files

### Single ticker mode

```bash
ls "Theses/$TICKER - "*.md 2>/dev/null
```

- 0 matches → `❌ No thesis found for [TICKER] in Theses/. Run /thesis [TICKER] first.`
- 1 match → proceed.
- 2+ matches → `❌ Ambiguous ticker [TICKER] — multiple thesis files match. Disambiguate manually.`

### Batch modes

```bash
# Filter active theses by frontmatter
for f in Theses/*.md; do
  status=$(awk '/^---/{c++; if(c==2) exit} c==1 && /^status:/{print $2}' "$f")
  conviction=$(awk '/^---/{c++; if(c==2) exit} c==1 && /^conviction:/{print $2}' "$f")
  if [ "$status" = "active" ]; then
    # --all → only high-conviction
    # --all-active → any conviction
    if [ "$MODE" = "--all" ] && [ "$conviction" != "high" ]; then continue; fi
    echo "$f"
  fi
done
```

Output a deterministic list of targets. Empty list → `ℹ️ No theses match filter. Nothing to refresh.` Exit cleanly (release lock).

## Step 2: Parse existing Key Metrics table

For each target thesis, read the `## Key Metrics` section. Parse every body row (skip the header row and the separator row). For each row capture:

| Field | Notes |
|---|---|
| `metric_label` | Cell 1 verbatim (e.g., `Market Cap`, `EV/Revenue (TTM)`, `Forward P/E`) |
| `value_raw` | Cell 2 verbatim (e.g., `~$4.6T`, `18.3x`, `+65% YoY`) |
| `notes_raw` | Cell 3 verbatim — **MUST be preserved unchanged** through the entire flow |
| `format_hints` | Parsed from `value_raw`: tilde prefix, sign prefix, currency symbol, magnitude letter (T/B/M/K), decimal precision, suffix (`x`, `%`, ` YoY`, ` TTM`) |

The skill's edit operations target the **Value cell only**. Notes cells are pass-through. Metric labels are pass-through (the skill does not rename rows or reorder them).

## Step 3: Map metric labels to FMP fields

Maintain an internal mapping table. Match is case-insensitive on the label after stripping parenthetical qualifiers like `(TTM)`, `(GAAP)`, `(Non-GAAP)`:

| Canonical label | FMP endpoint + field | Format default |
|---|---|---|
| `Market Cap`, `Market Capitalization` | `/stable/quote` → `marketCap` | `$X.XT` / `$XB` (magnitude-scale on USD; native currency for non-USD) |
| `Stock Price`, `Price`, `Share Price` | `/stable/quote` → `price` | `$X.XX` (USD) / native unit |
| `EV/Revenue`, `EV/Sales` | `/stable/ratios-ttm` → `evToSalesTTM` (or `enterpriseValueOverRevenueTTM` if present) | `X.Xx` |
| `EV/EBITDA` | `/stable/ratios-ttm` → `evToEbitdaTTM` (or `enterpriseValueOverEBITDATTM`) | `X.Xx` |
| `Trailing P/E`, `P/E`, `P/E (TTM)` | `/stable/ratios-ttm` → `peRatioTTM` | `X.Xx` |
| `Forward P/E`, `P/E (Forward)`, `NTM P/E` | derived: `quote.price ÷ analyst-estimates.eps (next FY)` | `X.Xx` |
| `Revenue Growth`, `Revenue Growth (YoY)`, `Sales Growth` | `/stable/income-statement-growth` → most-recent annual `growthRevenue` | `+X.X% YoY` |
| `Gross Margin`, `Gross Margin (GAAP)` | `/stable/ratios-ttm` → `grossProfitMarginTTM` | `XX.X%` |
| `Operating Margin`, `Op Margin` | `/stable/ratios-ttm` → `operatingProfitMarginTTM` | `XX.X%` |
| `Net Margin` | `/stable/ratios-ttm` → `netProfitMarginTTM` | `XX.X%` |
| `FCF Yield`, `Free Cash Flow Yield` | `/stable/key-metrics-ttm` → `freeCashFlowYieldTTM` | `X.X%` |
| `FCF Margin`, `Free Cash Flow Margin` | derived: `freeCashFlowTTM ÷ revenueTTM` | `XX.X%` |
| `Net Debt / EBITDA`, `Leverage` | `/stable/key-metrics-ttm` → `netDebtToEBITDATTM` | `X.Xx` |
| `Dividend Yield` | `/stable/ratios-ttm` → `dividendYieldTTM` | `X.X%` |
| `FY[YYYY] Revenue`, `[YYYY] Revenue` | `/stable/income-statement?period=annual` → matching FY's `revenue` | `$X.XB` |

**Anything not in this table is skipped.** Custom user-defined metrics (e.g., `Q1 FY2027 Guidance`, `Data Center Revenue`, `Sovereign AI Bookings`) have no FMP mapping — leave them untouched and report in the per-thesis output: `⏭ Skipped: [N] custom metrics with no FMP mapping — refresh manually if needed: [list of labels]`.

**Format-detection-overrides-default**: if `value_raw` parsing reveals a non-default format (e.g., user wrote `$215.9B` for FY2026 Revenue rather than `$0.2T`), reuse the detected format precisely — only swap the numeric portion.

## Step 4: Fetch FMP data (one parallel batch per ticker)

Per ticker, issue parallel curl calls:

```bash
TICKER_URL=$(printf '%s' "$RAW_TICKER" | jq -sRr @uri)
BASE="https://financialmodelingprep.com/stable"

curl -sf "$BASE/quote?symbol=$TICKER_URL&apikey=$API_KEY" > /tmp/numbers_${TICKER}_quote.json &
curl -sf "$BASE/ratios-ttm?symbol=$TICKER_URL&apikey=$API_KEY" > /tmp/numbers_${TICKER}_ratios.json &
curl -sf "$BASE/key-metrics-ttm?symbol=$TICKER_URL&apikey=$API_KEY" > /tmp/numbers_${TICKER}_km.json &
curl -sf "$BASE/income-statement-growth?symbol=$TICKER_URL&apikey=$API_KEY" > /tmp/numbers_${TICKER}_growth.json &
curl -sf "$BASE/income-statement?symbol=$TICKER_URL&period=annual&limit=3&apikey=$API_KEY" > /tmp/numbers_${TICKER}_income.json &
# Forward P/E only if Forward P/E is in the parsed table — guard the call
curl -sf "$BASE/analyst-estimates?symbol=$TICKER_URL&period=annual&apikey=$API_KEY" > /tmp/numbers_${TICKER}_est.json &
wait
```

**API failure handling**:
- HTTP error (4xx/5xx, non-empty stderr): retry once after 2s.
- Second failure: skip this ticker, report `⚠️ [TICKER] FMP fetch failed: [endpoint] [status]. Skipping refresh.` Continue to next ticker in batch mode; abort in single mode.
- Empty JSON array `[]` (FMP "no data" pattern): same as failure — FMP doesn't always return 404 for unknown tickers.

**Currency handling**:
- FMP returns market cap and revenue in the listing's native currency (KRW for `000660.KS`, JPY for `6981.T`, GBp for `GAW.L`, EUR for `BESI.AS`, etc. — confirmed via Live Portfolio).
- Format magnitude with the existing thesis's convention: if `value_raw` used `$X.XT`, output `$X.XT`; if it used `¥XB` or `£X.XB` or no currency symbol, preserve that.

## Step 5: Compute deltas and classify materiality

For every row that mapped successfully:

| Metric | Δ classification | Material if |
|---|---|---|
| Market Cap | percent change | \|Δ\| > 25% |
| Stock Price | percent change | \|Δ\| > 25% (usually moves with Market Cap; redundant — pick one anchor) |
| Revenue Growth | percentage-point change | \|Δ\| > 10pp |
| Gross Margin | percentage-point change | \|Δ\| > 3pp |
| Operating Margin | percentage-point change | \|Δ\| > 3pp |
| Net Margin | percentage-point change | \|Δ\| > 3pp |
| FCF Yield | percentage-point change | \|Δ\| > 1pp |
| FCF Margin | percentage-point change | \|Δ\| > 3pp |
| EV/Revenue, EV/EBITDA, P/E | percent change | \|Δ\| > 25% |
| Net Debt / EBITDA | absolute change | \|Δ\| > 0.5x |
| FY Revenue | percent change | \|Δ\| > 5% |
| Dividend Yield | percentage-point change | \|Δ\| > 0.5pp |

Aggregate per-thesis: `material_count`, `material_metrics: [list of labels]`. Used in Step 6 (user confirmation), Step 9 (Log entry text), and Step 10 (advisories).

## Step 6: Present deltas; confirm if material

**Single ticker, no material deltas**: skip confirmation; proceed silently to Step 7.

**Single ticker, ≥1 material delta**: pause and present:

```
[TICKER] Key Metrics — proposed updates:

| Metric         | Old      | New      | Δ        | Material |
|---|---|---|---|---|
| Market Cap     | ~$4.6T   | ~$5.8T   | +26.1%   | ⚠️       |
| EV/Revenue     | 18.3x    | 16.2x    | -2.1x    |          |
| Revenue Growth | +65% YoY | +42% YoY | -23pp    | ⚠️       |
| Gross Margin   | 71.1%    | 71.4%    | +0.3pp   |          |

⚠️ 2 material deltas — review before applying.
Notes column unchanged. Skipped: 5 custom metrics with no FMP mapping.

Confirm? (y/n)
```

Wait for explicit y/n. (n) → abort cleanly (release lock; no edits).

**Batch modes**: do not prompt per-ticker. Present aggregated material-delta summary at the END of the run (Step 12 report) so the user can decide which theses to `/deepen` or `/sync` after. The batch flow's safety net is the snapshot taken in Step 7.

## Step 7: Snapshot (mandatory)

For every thesis the skill is about to edit, take a snapshot:

```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
cp "Theses/$TICKER - $NAME.md" "_Archive/Snapshots/$TICKER - $NAME (pre-numbers $YYYYMMDD-$HHMMSS).md"
```

Add snapshot frontmatter on the copy:

```yaml
snapshot_of: "[[Theses/TICKER - Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: numbers
snapshot_batch: numbers-YYYY-MM-DD-HHMMSS
```

Batch ID format (single-ticker): `numbers-TICKER-YYYY-MM-DD-HHMMSS`.
Batch ID format (`--all` / `--all-active`): `numbers-batch-YYYY-MM-DD-HHMMSS` (shared across all theses in the batch — atomic cascade rollback via `/rollback`).

Snapshot is mandatory because the edit touches multiple table rows and a partial-write failure (rare but possible) without rollback path would corrupt the thesis's Key Metrics section.

## Step 8: Apply edits to the Key Metrics table

For each mapped row with a new value:

```
Edit:
  old_string: | [metric_label] | [value_raw] | [notes_raw] |
  new_string: | [metric_label] | [value_new] | [notes_raw] |
```

**Edit batching**: when ≥3 rows need updating in the same thesis, emit all Edits in a single tool-call block as independent parallel invocations. The harness serializes same-file Edits on the server side; this saves N round-trips vs. sequential Edits.

**Validation**: every `old_string` must contain the table-row's exact whitespace and pipe layout as read in Step 2 — no normalization, no whitespace re-collapsing. If the Edit returns `old_string not found`, do NOT retry with a normalized variant; instead abort the per-ticker edit, restore from snapshot, and report `⚠️ [TICKER] table-row Edit failed: row "[metric_label]" had unexpected layout. Snapshot retained at [path]. Skipping refresh.` Continue to next ticker in batch mode.

**Notes-column preservation invariant**: after all edits, re-read the thesis. For every metric row, verify the Notes cell content matches the captured `notes_raw` exactly. Mismatch → restore from snapshot, hard-abort: `❌ Notes column preservation invariant FAILED for [TICKER]. Restored from snapshot. This indicates a parsing bug — please report.`

## Step 9: Append Log entry

Append to the thesis `## Log` section (max 2 lines):

```
### YYYY-MM-DD
- Numbers refresh: [N] metrics updated[, M material]. [single most-significant Δ in plain prose, e.g., "revenue growth decel +65%→+42%"]. Snapshot: [[_Archive/Snapshots/...]]
```

**Prefix `Numbers refresh:` is canonical** — registered in `_shared/log-prefixes.md` §18 as **skill-origin**. `/sync` Step 2.5 will see this prefix and skip sector / macro re-propagation for the thesis. Drift detection (Step 3e) also excludes it (refresh entries carry no conviction sentiment). Do not change the prefix; `/lint #29` enforces alignment.

When zero material deltas: still write the Log entry — its presence is the audit trail. Example: `Numbers refresh: 7 metrics updated, 0 material. Largest Δ: EV/Revenue 18.3x→16.2x (-11.5%). Snapshot: [[...]]`.

## Step 10: Material-delta advisories (single-ticker mode only)

After the Log entry lands, if `material_count ≥ 1`, surface targeted suggestions per metric. These are SUGGESTIONS, not auto-executed.

| Material delta | Suggested follow-up |
|---|---|
| Revenue Growth dropped >10pp | `/deepen [TICKER] --section "Bull Case"` (growth slowdown reframes the bull case) |
| Gross Margin dropped >3pp | `/deepen [TICKER] --section "Industry Context"` (pricing power inflection) |
| Operating Margin or FCF Margin dropped >3pp | `/stress-test [TICKER]` (operating leverage thesis at risk) |
| EV/Revenue or P/E compressed >25% | `/brief [TICKER]` (re-evaluate vs. consensus) — possible market disagreement signal |
| Net Debt/EBITDA crossed >2.0x or up >0.5x | `/deepen [TICKER] --section "Risks"` (leverage shift) |
| Forward P/E expanded >25% | `/stress-test [TICKER]` (multiple expansion thesis vulnerable to consensus revision) |

Output these as `→ Consider: [suggestion]` lines in the final report. Never auto-run.

**Skip in batch modes** — batch advisories print in Step 12 aggregate report instead.

## Step 11: Update `key_metrics_last_refreshed` (frontmatter)

Add or update a frontmatter field:

```yaml
key_metrics_last_refreshed: YYYY-MM-DD
```

If absent, add as the last frontmatter field before the closing `---`. If present, update in place.

This field is consumed by `/lint` (future check) to flag theses with stale Key Metrics — recommended threshold: 90 days. Until that lint check exists, the field is still useful as a visible thesis-level signal in dataview queries.

## Step 12: Release lock and report

Release lock per preflight §1.7 in the final Bash block. Then output the report.

### Single ticker report

```
✓ /numbers [TICKER] complete

Thesis updated:    [[Theses/TICKER - Name]]
Snapshot:          [[_Archive/Snapshots/TICKER - Name (pre-numbers YYYY-MM-DD-HHMMSS)]]
Batch ID:          numbers-TICKER-YYYY-MM-DD-HHMMSS

Metrics refreshed:  [N]  ([M] material — see deltas above)
Custom metrics skipped: [K]  ([list of labels, or "none"])
FMP fetch failures:     [F]  ([list, or "none"])

Log entry:        appended ("Numbers refresh:")
Propagation:      /sync will SKIP this thesis (skill-origin prefix)
Frontmatter:      key_metrics_last_refreshed: YYYY-MM-DD

→ Consider: [Step 10 advisories, if any]
```

### Batch report

```
✓ /numbers [--all | --all-active] complete

Tickers processed:   [total]
  Refreshed cleanly: [N]
  Skipped (no Key Metrics section): [N]
  Failed (FMP errors): [N]

Material-delta theses ([count]):
  [TICKER1]: [top 1-2 material deltas in one line]
  [TICKER2]: [...]
  ...

Suggested follow-ups (single-ticker /deepen, /stress-test, /brief):
  [list, max 5; if more, suggest "Run /numbers TICKER for per-thesis advisories"]

Batch ID:           numbers-batch-YYYY-MM-DD-HHMMSS
Snapshot directory: _Archive/Snapshots/
Rollback:           /rollback numbers-batch-YYYY-MM-DD-HHMMSS (cascade across all touched theses)
```

### Final Bash block (lock release)

```bash
LOCK_FILE="<paste-from-Step-0.1>"
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ($LOCK_FILE) ==="
else
  echo "⚠️ Lock ownership check failed at release — skipping rm."
fi
# Clean up FMP temp files
rm -f /tmp/numbers_*.json
```

Runs unconditionally — whether all targets refreshed cleanly, some failed FMP fetches, or section-existence-probe excluded some theses.

## Recommended frequency

- **`conviction: high` theses**: monthly. Capital concentrated here moves with the numbers — a 20%+ market-cap drift, a 10pp revenue-growth deceleration, or a 300bps margin compression is a real signal. Pair with `/loop 1m /numbers --all` if the user wants automated recurrence.
- **`conviction: medium` theses**: quarterly (post-earnings). Lower stakes; the qualitative thesis hasn't reached the conviction inflection where every quarterly number matters.
- **`conviction: low` theses**: opportunistically (when running `/surface`, `/prune`, or `/brief`). Keep numbers fresh only when actively reviewing.
- **`status: monitoring` theses**: monthly is fine — the watchlist exists to catch inflections, and stale Key Metrics defeat the purpose.
- **`status: closed` theses**: never. Closed theses are archived; their Key Metrics tables are historical records.

This cadence is the basis for `/sync` Step 3e's drift-window exclusion of `Numbers refresh:` entries (per `_shared/log-prefixes.md` §18) — monthly refresh on a high-conviction thesis would otherwise consume every slot of the 5-entry drift window.

## Design constraints (xxx DO NOT VIOLATE xxx)

1. **Never edit a Notes column cell.** The Notes column holds the user's analytical context — `data center segment +217% YoY`, `multiple compression risk`, `up from 65% pre-AI cycle`. Overwriting it destroys the thesis's interpretive layer. Validated by Step 8's post-edit invariant check.

2. **Never create a `## Key Metrics` section.** If absent, skip (batch) or hard-abort (single) per Step 0.4. Structural thesis changes require explicit user action.

3. **Never create a Research note.** The Log entry IS the audit trail. A refresh has no source URL, no qualitative claim, nothing to remember beyond the snapshot. Polluting `/Research/` with N refresh notes per quarter destroys the folder's signal-to-noise.

4. **Never reorder or rename metric rows.** The skill is row-value-cell-only. If a user has `EV/Revenue` and `EV/Revenue (TTM)` as separate rows (e.g., as a record of methodology change), the skill matches and refreshes both independently.

5. **Never propagate via /sync.** The `Numbers refresh:` prefix is skill-origin (registry §18). Material deltas surface as advisories for the user to act on — auto-propagation of routine metric refreshes would flood sector notes with "TICKER market cap updated" entries.

6. **Wholesale tier is the assumed entitlement.** The skill issues 6 endpoint calls per ticker in parallel; lower FMP tiers may rate-limit. Add per-ticker retry logic but do not silently downshift to fewer endpoints — that produces silently-incomplete refreshes.

7. **Snapshot before every per-thesis edit.** Even though the edit is small, partial-write recovery is the rollback path. Snapshot is the only guarantee that the user can `/rollback` if a Notes-column invariant trips.
