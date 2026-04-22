---
name: catalyst
description: Extract and maintain a cross-portfolio catalyst calendar from all thesis notes. Use when user says "catalyst", "calendar", "what's coming up", "upcoming events", or "what could move the portfolio".
model: opus
effort: max
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * defuddle * cp * mkdir *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Build a comprehensive catalyst calendar aggregating every upcoming event across the portfolio.

## Phase 0: Pre-flight (MANDATORY — runs before Phase 1)

### 0.1: Acquire vault lock
Acquire a `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 5 minutes. Capture the token, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block.

### 0.2: Snapshot existing `_catalyst.md` (mandatory pre-regenerate snapshot — H2 fix: hard-abort on failure)

Before regenerating `_catalyst.md`, snapshot the prior version. **If the snapshot cp fails, HARD ABORT `/catalyst`** — do not proceed to regenerate, because a regenerate failure after a failed pre-snapshot loses the prior calendar with no recovery path.

```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
SNAPSHOT_PATH="_Archive/Snapshots/_catalyst (pre-catalyst YYYY-MM-DD-$HHMMSS).md"

if [ -f "_catalyst.md" ]; then
  if ! cp "_catalyst.md" "$SNAPSHOT_PATH"; then
    echo "SNAPSHOT_FAILED|$SNAPSHOT_PATH"
    exit 1
  fi
  # Verify the copy actually landed with non-zero size (cp can silently no-op on some filesystems)
  if [ ! -s "$SNAPSHOT_PATH" ]; then
    echo "SNAPSHOT_EMPTY|$SNAPSHOT_PATH"
    rm -f "$SNAPSHOT_PATH"
    exit 1
  fi
fi
```

Then add snapshot frontmatter to the newly created file:
```yaml
snapshot_of: "[[_catalyst.md]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: catalyst
snapshot_batch: catalyst-YYYY-MM-DD-HHMMSS
```

**Snapshot failure handling (H2)**: if either the cp fails or the resulting file is empty, abort with:

```
❌ /catalyst pre-regenerate snapshot failed: [path]
   Reason: [cp error | empty file after copy]

No regeneration attempted. The current _catalyst.md is unchanged. Fix the
underlying filesystem issue (disk space, permissions, _Archive/Snapshots/
directory writability) and re-run /catalyst. Prior calendar is intact.
```

Exit the skill cleanly — do NOT proceed to Phase 1. The prior `_catalyst.md` is preserved at its current path; the next successful `/catalyst` run will snapshot and regenerate.

**Frontmatter-add failure**: if the cp succeeds but the subsequent frontmatter Edit fails, proceed with regeneration anyway — the snapshot file content is preserved (bit-exact copy of the prior `_catalyst.md`), just without the `snapshot_of:` metadata. `/rollback` can still restore it via direct cp-back; it won't appear in `/rollback` cascade detection by batch ID, but the user can locate it by filename pattern (`_catalyst (pre-catalyst *)`).

**Why the hard abort matters**: prior behavior proceeded with regeneration after silent cp failure. If web search then failed mid-regenerate, the partial calendar overwrote the prior version with no snapshot to roll back to. Daily backup was the only fallback. Hard-abort guarantees the prior calendar is always recoverable from the pre-regenerate snapshot before any destructive write.

If no prior `_catalyst.md` exists (first run), skip the snapshot step (the `[ -f "_catalyst.md" ]` guard handles this) and proceed to Phase 1.

## Phase 1: Load the Portfolio (Parallel Full Reads)

**Issue all thesis Reads AND all macro Reads in a single parallel tool-call batch** — one message with ~48 Read invocations (42 theses + 6 macros), not serial loops. This collapses the I/O into one round-trip while preserving full-file context: the LLM sees every thesis body in full so cross-section catalyst signal (e.g., a regulatory date mentioned in Bull Case, a product launch referenced in Business Model) isn't lost to over-aggressive section pre-filtering.

### 1.1 Parallel batch composition

- **Read** every `Theses/*.md` in full (all files — draft, active, monitoring; every thesis can carry catalysts).
- **Read** every `Macro/*.md` in full (bounded set, ~6 files — rate decisions, geopolitical deadlines, commodity contract expirations).

All reads land in one round-trip. Do NOT serialize per-file.

### 1.2 Extract from the pulled content

Within each thesis, prioritize **Catalysts**, **Risks**, and the last 5 **Log** entries (highest-density sections for event extraction) but **maintain peripheral awareness of other sections** — a catalyst may surface in Bull/Bear Case, Summary, or Business Model when the author didn't duplicate it into the Catalysts list. Full-file context is kept intentionally; `/catalyst` favors completeness over narrow extraction.

Per thesis:
- **Catalysts** section: event description, approximate date or date range (if stated), expected impact direction (positive / negative / uncertain), magnitude estimate (major / minor).
- **Log** entries: recently noted upcoming events (scan the last ~5 date headers; older entries typically describe past events).
- **Risks** section: risk events with timing (e.g., "regulatory decision expected Q2").
- **Elsewhere in the thesis**: flag any date-anchored event or upcoming catalyst mentioned in Bull Case, Bear Case, Summary, Industry Context, or Business Model that's absent from the Catalysts section — surface these as candidates the thesis may need to formalize.
- **Macro notes**: cross-portfolio macro events (rate decisions, geopolitical deadlines, commodity contract expirations).

## Phase 2: Enrich and Deduplicate
- Where catalyst dates are vague ("Q2 2026", "H2"), convert to approximate calendar dates
- Identify catalysts that affect MULTIPLE theses (e.g., an earnings report from a major customer that affects several supplier theses)
- Flag catalysts that are stale — events that appear to have already passed based on their dates vs today's date
- **Web search for upcoming earnings dates for all thesis tickers, issued in parallel batches.** Send one message containing up to 10 WebSearch invocations, then the next message with the next 10, and so on. For ~42 tickers this is ~4-5 rounds of ~5s each instead of ~42 serial rounds. Never serialize WebSearches that have no data dependency on each other. Do NOT cap the total number of searches — every ticker with `status: active | monitoring` gets a search.

## Phase 3: Analyse Catalyst Clusters
- **Concentration risk**: Are there weeks where multiple catalysts cluster? This creates portfolio-level volatility
- **Catalyst gaps**: Which theses have NO near-term catalyst? Flag as thesis drift risk — a position with no catalyst is dead capital
- **Asymmetric events**: Which catalysts have the widest range of possible outcomes? These are the highest-attention-priority events
- **Cross-thesis catalysts**: Events that simultaneously affect 3+ positions (e.g., a macro data release, a major customer's earnings)

## Phase 4: Output

> **Snapshot already taken in Phase 0.2** with the mandatory hard-abort guard (§1.3 invariant). Do NOT re-snapshot here — a second `cp` without the hard-abort/non-empty check would silently overwrite Phase 0.2's protective snapshot under filesystem pressure, destroying the recovery path. The Phase 0.2 snapshot covers the pre-regenerate state for the entire run.

Save/update the catalyst calendar at `_catalyst.md` (overwrite each run — this is a regenerated utility file like `_hot.md`, not a research note):
```yaml
---
date: YYYY-MM-DD
tags: [meta, catalyst-calendar]
---
```

### Structure:
**Next 2 Weeks** (day-by-day detail)
| Date | Ticker(s) | Event | Expected Impact | Magnitude | Notes |
|------|-----------|-------|-----------------|-----------|-------|

**Weeks 3-4**
| Week of | Ticker(s) | Event | Expected Impact | Notes |
|---------|-----------|-------|-----------------|-------|

**Month 2-3** (grouped by week)
| Approximate Date | Ticker(s) | Event | Notes |
|-----------------|-----------|-------|-------|

**No Catalyst Identified**
| Ticker | Last Catalyst Date | Days Since | Status |
|--------|-------------------|------------|--------|
[Theses with no upcoming catalyst — flag for attention]

**Stale Catalysts** (events that appear to have passed)
| Ticker | Event | Listed Date | Action Needed |
|--------|-------|-------------|---------------|
[Catalysts whose dates have passed — thesis needs updating]

**Cross-Thesis Events**
[Events affecting 3+ theses, with impact assessment for each]

## Phase 5: Update `_hot.md`

Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — those are `/sync`-owned). If `_hot.md` does not exist, create it per the CLAUDE.md Rule #9 schema.

1. **Active Research Thread**: **Same-topic continuation** — if the current thread already covers catalyst-calendar work, append a dated line (`YYYY-MM-DD: refreshed catalyst calendar — [key takeaway, e.g. "2 dense weeks ahead, 3 theses with no catalyst"]`). **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write the new thread focused on catalyst state: `YYYY-MM-DD: refreshed catalyst calendar — next 2 weeks = [N] catalysts across [M] theses; [K] no-catalyst theses flagged for review.` Append `*Previous:*` line(s) — max 5, drop oldest.

2. **Open Questions**: For every ticker flagged under "No Catalyst Identified" in the catalyst calendar output, add a question (if not already present): `- [[TICKER]]: what catalyst in next 90 days could reignite this thesis? (flagged by /catalyst YYYY-MM-DD)`. **Dedupe by question pattern, not by ticker presence** — only suppress this entry if an existing Open Question already contains BOTH the ticker wikilink AND the substring `catalyst in next 90 days could reignite this thesis`. Other pre-existing questions about the ticker (e.g., from `/thesis`, `/stress-test`, `/surface`) must not suppress the catalyst-specific question; a thesis can legitimately have multiple open questions at once, and over-broad dedup would silently drop the catalyst gap from the user's attention surface.

3. **Recent Conviction Changes**: not touched by `/catalyst`.

4. **Portfolio Snapshot**: not touched by `/catalyst`.

**Word cap**: After edits, check total word count. If over 4,000 words (soft cap per `_shared/hot-md-contract.md`), prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap. If over 5,000 (hard cap), abort `_hot.md` update per contract.

## Phase 6: Report

**Runs in forked subagent** (`context: fork`) — main conversation context is shielded from the ~48 full thesis + macro reads (~400K tokens at current vault scale). Only the Phase 6 report text below returns to the user's main session; `_catalyst.md` persists to disk as the authoritative calendar for later reading.

Report to user: next 2 weeks of catalysts, any dangerous clusters, and the list of theses with no catalyst (these need attention or pruning). Include one line summarizing the `_hot.md` update: `_hot.md: Active Research Thread refreshed; [K] no-catalyst tickers added to Open Questions.` Point the user to `[[_catalyst.md]]` for the full calendar tables (Next 2 Weeks, Weeks 3-4, Month 2-3, No Catalyst Identified, Stale Catalysts, Cross-Thesis Events).
