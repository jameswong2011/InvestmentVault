---
name: compare
description: Side-by-side competitive comparison of two or more companies. Use when user says "compare", "X vs Y", "which is better", or asks about competitive dynamics between specific companies.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * cp * mkdir * defuddle *)
---

Build a rigorous side-by-side comparison focused on competitive dynamics and investment merit.

Design rationale in `.claude/skills/compare/RATIONALE.md` (§N.M anchors).

## Arguments

`$ARGUMENTS` = 2+ tickers or company names (e.g., "BESI vs AMAT", "PANW NET CRWD"). Only one ticker provided → identify closest competitors from Sector Note, ask user to confirm before proceeding.

## Phase 0.-1: Pre-flight

### 0.-1.1: Acquire per-ticker locks (C4 — §1)

Parse tickers from `$ARGUMENTS`. Acquire one lock per ticker (`.vault-lock.A`, `.vault-lock.B`, `.vault-lock.C`) per `.claude/skills/_shared/preflight.md` Procedure 1.3c — **per-ticker individual locks, NOT a joint `+`-delimited lock** (§1.1 — breaks on hyphen-containing tickers like `BRK-B`).

Timeout 10 min. Verify ownership every subsequent Bash block via token match (Procedure 1.5). Release all N locks in final reporting block.

**Rollback-on-partial-acquisition** (§1.2): if any per-ticker lock is held by another skill, release all previously-acquired locks in this run and abort. Prevents holding a proper subset while concurrent skill holds the rest.

### 0.-1.2: Rename-marker pre-flight for EACH ticker

For each ticker in `$ARGUMENTS`, run Procedure 2. ANY `.rename_incomplete.TICKER_N` → hard-block per contract 2.3. Split-name state on any one ticker would corrupt the cross-thesis comparison research note's wikilinks.

## Phase 0: Thesis Existence Check

Verify which tickers have existing thesis notes in `Theses/`.

**All tickers have theses** → proceed to Phase 1 (full comparison mode).

**Some tickers lack theses** → report and offer options (§2.2):
```
⚠️ No thesis found for [TICKER(S)]. Options:
  (a) Proceed — use web research for [TICKER(S)] (lighter comparison, no vault updates for missing tickers)
  (b) Stop — run /thesis [TICKER] first for a full-depth comparison
```
Wait for user selection.
- **(a) Web-supplemented mode**: proceed. Missing tickers use web research in Phase 1. Phase 5 vault updates apply ONLY to tickers with existing theses. Report appends: `💡 Consider /thesis [TICKER] to formalize coverage.`
- **(b) Stop**: report missing tickers, stop.

**No tickers have theses** → stop (§2.1). At least one thesis is required as analytical anchor.

## Phase 1: Gather Context

For each company **with a thesis note**:
1. Read thesis note from `Theses/`
2. Read all linked research notes from the thesis
3. Read relevant Sector Note(s) — especially competitive dynamics and value chain sections
4. Search `Research/` and `Macro/` for additional mentions

**Web-supplemented tickers** (Phase 0 option a): skip steps 1-2. Search web for: business model overview, latest financials (revenue, margins, growth), competitive position, key products. Search vault (`Research/`, `Sectors/`, `Macro/`) for existing mentions. Flag sections without vault-depth data with `[web only]`.

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

Use data from vault Key Metrics tables, supplement with web where gaps exist.

## Phase 3: Dynamic Analysis (§8 — where insight lives)

Go beyond static snapshots:

1. **Market share trajectory** — where is share shifting and why? Use vault research notes for evidence. Structural or cyclical?
2. **Pricing power divergence** — whose pricing power is strengthening vs weakening? What drives divergence (technology, regulation, lock-in, commoditisation)?
3. **Technology trajectory** — who is on the right side of the next platform shift? Who is investing in the right areas? Who risks disruption?
4. **Logical tension** — what does each company need to be true that the other's success disproves? (If BESI wins on hybrid bonding, does that mean AMAT's approach fails, or can both win?)
5. **Scenario divergence** — under what macro or industry scenario does the current underdog win? How likely per vault macro notes?
6. **Customer and supplier overlap** — do they share customers? Who has more pricing power in that relationship? Shared suppliers (correlated supply risk)?

## Phase 4: Investment Verdict

- **Risk-adjusted asymmetry**: not "which is cheaper" but which offers better upside/downside skew given the evidence
- **Portfolio role**: substitutes or complements? Can you own both, or one-or-the-other? Does owning both create hidden concentration?
- **Preference trigger**: specific, observable event that would flip preference. Make it falsifiable.
- **Conviction gap**: if one has a thesis and the other doesn't, should it? If both have theses, is the conviction spread justified by the evidence?

## Phase 5: Output

### 5.0: Write manifest skeleton (M2 — skeleton before destructive edits)

Generate `HHMMSS` once for the entire Phase 5 run. All downstream per-file writes (research note, sector snapshots, manifest) reuse it.

```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
```

Before any destructive mutation (5.1 research-note write, 5.2 Log appends, 5.5b sector edits), write a manifest skeleton at `_Archive/Snapshots/_compare-manifest (compare-YYYY-MM-DD-HHMMSS).md` with `status: in-progress` (§3 invariant: skeleton → populate → flip):

```yaml
---
type: compare-manifest
batch: compare-YYYY-MM-DD-HHMMSS
status: in-progress
date: YYYY-MM-DD
---

# Compare Batch Manifest

> **If `status: in-progress`**, `/compare` crashed between Phase 5.0 (skeleton)
> and Phase 5.5c (flip). Check the vault for partial state:
>   - Research note at `Research/YYYY-MM-DD - [tickers] - Competitive Comparison.md` may or may not exist.
>   - Thesis Logs may have partial appends (filter by today's date + comparison wikilink).
>   - Sector notes may have been edited (Phase 5.5b rolls back on failure, but crash mid-5.5b leaves partial edits).
> Recovery: `/rollback compare-YYYY-MM-DD-HHMMSS` → cascade through each affected sector snapshot in Phase 5.5a.
>
> **If `status: completed`**, Phase 5 finished with all sector writes succeeding atomically.
> **If `status: rolled-back`**, Phase 5.5b atomicity fired — sectors restored from 5.5a snapshots; research note and thesis Logs preserved.

## Tickers compared
- *(filled in Phase 5.5c flip)*

## Sector writes attempted
- *(filled in Phase 5.5c flip with per-sector outcomes)*

## Sector writes rolled back (if any)
- *(filled in Phase 5.5c flip — empty if status: completed)*

## Thesis Log appends
- *(filled in Phase 5.5c flip with per-ticker outcomes)*

## Research note
- *(filled in Phase 5.5c flip with path and propagated_to status)*
```

Skeleton write failure → hard abort Phase 5 before any destructive edit. Locks remain held until the final reporting block; report to user and release.

### 5.1: Write comparison research note (without `propagated_to:` — §3.1)

Save to `Research/YYYY-MM-DD - [TICKER A] vs [TICKER B] - Competitive Comparison.md`:
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

**Omitted at write time**: mirrors `/scenario` Phase 6.1 + 6.3 atomicity (§3). If any Phase 5.2 Log append fails, pre-writing `propagated_to:` would falsely claim every ticker received its Log entry → permanent audit gap.

### 5.2: Per-thesis Log append (track per-ticker outcomes)

**Vault updates** — ONLY for tickers with existing thesis notes. Skip web-supplemented tickers (§2.3).

For each thesis with existing note, attempt Log append (max 2 lines):
```
### YYYY-MM-DD
- [[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]: [key competitive insight] — conviction [unchanged/strengthened/weakened + reason]
```

**Track per-ticker outcomes**: `succeeded: [tickers]` and `failed: [tickers, reason]`. Failure = Log append Edit failed (file locked, missing `## Log`, malformed frontmatter). Do NOT abort loop on single failure.

### 5.3: Add to Related Research (independent of Log outcome — §3.3)

For each compared thesis with existing note, add comparison to `## Related Research` (if not already present):
```
- [[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]
```

Wikilink registration, not propagation claim — runs regardless of 5.2 outcome.

### 5.4: Atomicity rule for `propagated_to:` (§3.2)

Update research note's `propagated_to:` **only after EVERY thesis-with-existing-note Log append has landed**.

- **All succeeded** (`failed:` empty): edit frontmatter to add `propagated_to: [TICKER1, TICKER2, ...]` (all tickers with existing theses). Insertion: immediately before closing `---`. `/sync` Case 2b skips as already-propagated.
- **One or more failed** (`failed:` non-empty): do NOT write `propagated_to:` at all. Next `/sync` detects each via file-direct fallback (research note `tags:` + body wikilinks list each ticker), per-thesis idempotency check re-attempts failed; succeeded targets skipped via per-thesis idempotency.

**Per-failure reporting**: list every failed ticker in Phase 6 report under `Per-thesis Log appends — failed: [TICKER1 (reason), TICKER2 (reason)]`.

### 5.5: Cross-sector atomic sector-note updates (6.5 — §4)

Cross-sector ALL-OR-NOTHING semantics. Any sector note's edit failure mid-transaction → roll back all preceding successful sector edits using per-sector snapshots.

**Resolve target sector set**: for each compared thesis with existing note, resolve sector via `.claude/skills/_shared/sector-resolution.md`. Dedup. Yields `target_sectors: [(thesis_list, sector_note_path, match_confidence), ...]`.

**Confidence handling per resolved sector** (§4.3):
- `match_confidence: none`: emit no-match warning. Remove sector from atomic transaction set. Comparison still completes for resolved sectors.
- `match_confidence: substring`: emit `log_message` AND pause for explicit user confirmation before modifying analytical text. Declined → remove from transaction set.
- `match_confidence: normalized | exact`: proceed silently (normalized logs in final report, no prompt).

### 5.5a: Pre-snapshot ALL target sectors FIRST (§4.2)

Before any sector note write, snapshot every target sector. Any snapshot fails → abort immediately (no destructive modifications yet):

```bash
# For each (thesis_list, sector_note_path, _) in target_sectors:
SECTOR_SLUG=$(echo "Sector Name" | tr '[:upper:]' '[:lower:]' | tr ' &/' '--')
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-compare YYYY-MM-DD-HHMMSS).md"
```

Add frontmatter to each snapshot with per-sector batch ID (§5.1 — distinct per sector):
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: compare
snapshot_batch: compare-[sector-slug]-YYYY-MM-DD-HHMMSS
```

Store `snapshot_map: {sector_note_path → snapshot_path}` for potential rollback in 5.5b.

### 5.5b: Apply sector edits; on failure, roll back all prior successes (§4.2)

```
attempted_and_succeeded: []
attempted_and_failed: []

for sector_note_path, thesis_list, confidence in target_sectors:
    try:
        apply_sector_edit(sector_note_path, thesis_list, comparison_insight)
        attempted_and_succeeded.append(sector_note_path)
    except EditFailure as e:
        # Roll back ALL prior succeeded sector edits
        for prior_sector in attempted_and_succeeded:
            copy_from(snapshot_map[prior_sector], prior_sector)  # restore from snapshot
        
        attempted_and_failed.append((sector_note_path, str(e)))
        abort_transaction(
            reason=f"Sector note write failed: {sector_note_path} ({e}). "
                   f"Rolled back: {attempted_and_succeeded}. "
                   f"Research note and thesis Logs preserved. "
                   f"Re-run /compare after resolving the sector write issue.")
```

**`apply_sector_edit`**: targeted `Edit` operations on sector note — competitive dynamics, value chain, comparison tables. Each Edit is atomic; single Edit failure triggers outer abort + rollback.

**`abort_transaction` surfaces** (§4.4):
- Sectors successfully edited (now rolled back to pre-compare state): list
- Sector that failed: path + reason
- Research note status: preserved (5.1 already wrote it)
- Thesis Logs status: preserved (5.2 already wrote them)
- `propagated_to:` status: depends on 5.4 — set (if all 5.2 succeeded) or omitted (atomicity fired)

### 5.5c: Populate + flip compare manifest (M2 — skeleton → populate → flip)

Manifest skeleton was written at Phase 5.0 with `status: in-progress`. Phase 5.5c populates the body placeholders with actual outcomes from 5.1-5.5b and flips status.

**Populate body** (Edit the Phase 5.0 skeleton, replacing `*(filled in Phase 5.5c flip)*` placeholders):

```markdown
## Tickers compared
- TICKER_A, TICKER_B, TICKER_C

## Sector writes attempted
- Sectors/X.md — succeeded (snapshot: [[_Archive/Snapshots/X (pre-compare ...)]])
- Sectors/Y.md — succeeded (snapshot: [[_Archive/Snapshots/Y (pre-compare ...)]])

## Sector writes rolled back (if any)
- (none if status: completed)

## Thesis Log appends
- TICKER_A: succeeded
- TICKER_B: succeeded
- TICKER_C: failed (reason) — will be retried by next /sync via file-direct fallback

## Research note
- [[Research/YYYY-MM-DD - TICKER_A vs TICKER_B vs TICKER_C - Competitive Comparison]]
- propagated_to: set | omitted (atomicity — Log append failed for at least one ticker)
```

**Flip frontmatter**:
- All sector writes succeeded: `status: in-progress` → `status: completed`. Add `completed_date: YYYY-MM-DD`.
- Phase 5.5b rollback fired: `status: in-progress` → `status: rolled-back`. Add `completed_date: YYYY-MM-DD`.

**Verify flip landed**: re-read manifest frontmatter. Confirm `status:` is no longer `in-progress`. On verification failure: report `⚠️ Compare manifest status flip failed — manifest remains status: in-progress despite completion. /lint #45 will flag this as Critical. Manual fix: edit manifest frontmatter to the correct terminal status.` Continue to 5.5 Sector edits.

`status: rolled-back` indicates clean abort (Phase 5.5b rollback fired). `status: completed` indicates atomic success. `status: in-progress` surfaced as Critical by `/lint #45` (§6.2).

### Sector edits — targeted `Edit` operations

Modify original sector notes using targeted `Edit` (atomic string replacement per section), NOT full-file `Write`. Each `Edit` call succeeds atomically or leaves the section unchanged — blast radius of mid-edit failure is zero. Apply one `Edit` per modified section (e.g., one for competitive dynamics, one for value chain).

**Post-edit verification**: after all edits, re-read modified sector note. Per edited section, verify:
- Ends with complete sentence (no mid-word, mid-sentence, unclosed formatting)
- No incomplete table rows (line starts `|` but doesn't end `|`)

Any fail: `⚠️ Sector note may contain a partial edit in [section]. Snapshot available: [[_Archive/Snapshots/...]]. Review manually or /rollback.`

### Graph update deferred

`_graph.md` owned exclusively by `/graph`. Run `/graph last` after this skill to register comparison research note and new cross-thesis connections.

### _hot.md update

Per `.claude/skills/_shared/hot-md-contract.md` (do NOT touch Latest Sync / Sync Archive):

1. **Active Research Thread**: same-ticker continuation per contract. Write: compared [TICKER A] vs [TICKER B], key competitive insight, logical next research step.
2. **Recent Conviction Changes**: add entry per ticker where conviction was strengthened or weakened.
3. **Open Questions**: add unresolved competitive questions comparison surfaced.

Word cap: after edits, over 4,000 (soft cap per `_shared/hot-md-contract.md`) → prune `## Sync Archive` (oldest first) then `*Previous:*` lines. Abort if over 5,000 hard cap.

## Phase 6: Report

1. **Comparison research note**: `[[Research/YYYY-MM-DD - A vs B - Competitive Comparison]]`
2. **Single most important competitive insight** and whether it changes conviction on either name.
3. **Per-thesis Log appends** (5.2 outcome):
   - `Theses with existing notes propagated: [N] of [M]` (succeeded list)
   - `propagated_to: frontmatter` — `set ([TICKER1, TICKER2, ...])` (all succeeded) | `omitted (one or more appends failed — next /sync will retry)`
   - **Failed appends** (if any): `[TICKER1 (reason), TICKER2 (reason)]`
4. **Web-supplemented tickers** (if any from Phase 0 option a): `[TICKER1, TICKER2] — used web research, no vault updates. Consider /thesis [TICKER] to formalize coverage.`
5. **Sector notes updated**: per-sector list with snapshot path, or "no snapshot (link addition only)".
6. **Transaction state**: `completed` | `rolled-back: [sectors rolled back, reason]`
7. **Follow-up**: `→ Run /sync to propagate sector note changes and retry failed Log appends. Then /graph last.`
