---
name: surface
description: Surface new insights, potential trades, and research opportunities from existing vault content. Use when user says "surface", "what am I missing", "find opportunities", or "what should I research next".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * find * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Perform deep insight discovery across the vault. This is the highest-value operation — finding connections and opportunities the user hasn't seen yet.

## Step 0: Pre-flight (MANDATORY — runs before Scope Resolution)

### 0.1: Acquire vault lock
- **Unscoped `/surface`** (full vault): acquire a `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 10 minutes.
- **Scoped `/surface TICKER`**: acquire a `ticker:TICKER` scope lock. Timeout budget: 5 minutes.
- **Scoped `/surface [sector]`**: acquire a `vault-wide` scope lock (the sector set spans multiple tickers; concurrent ticker-scoped writers would race on sector note edits). Timeout budget: 10 minutes.

Capture the token emitted at Step 0.1, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block via `rm -f "$LOCK_FILE"`.

### 0.2: Rename-marker pre-flight (ticker-scoped mode only)
For `/surface TICKER`, run `.claude/skills/_shared/preflight.md` Procedure 2. If `.rename_incomplete.TICKER` exists, hard-block per contract 2.3. For unscoped and sector-scoped modes, check `.rename_incomplete.*` at vault root; if any marker exists, emit a warning but DO NOT abort (surface is read-mostly for these modes — it writes a research note but does not edit thesis wikilinks). Warning text: `⚠️ In-flight rename repair(s) detected: [list markers]. Surface scan will proceed but its research note's wikilinks to the affected ticker(s) use current filenames. Complete rename repair before running downstream /sync.`

## Scope Resolution

Parse `$ARGUMENTS` to determine scope:

- **Ticker** (e.g., `NVDA`): Read `_graph.md` and resolve the ticker's adjacency set — its thesis, sector note(s), macro note(s), cross-thesis references, and all linked research. Also include theses that share a sector (one ring outward) for competitive context.
- **Sector** (e.g., `semiconductors`): Use `_graph.md` Sector → Theses reverse index to resolve all theses in that sector, plus the sector note, related macro notes, and their linked research.
- **No arguments / empty**: Full vault — no scoping (reads everything).

If a scope is requested but `_graph.md` does not exist, warn: `⚠️ Graph missing — cannot scope. Run /graph first, or run /surface without arguments for full vault scan.` Then stop.

### Scope-set existence validation (ticker-scoped and sector-scoped modes only)

After resolving the scope set from `_graph.md` and before reading any thesis files, validate that every resolved thesis's file still exists on disk. `_graph.md`'s reverse indexes and adjacency entries reflect the last `/graph` run's filesystem state; closures via `/status active→closed` or `/prune` between that run and now mv files to `_Archive/` without touching `_graph.md`. Scoped `/surface` would otherwise resolve archived theses into the scope set and fail when reading them — producing silently incomplete analysis.

Validation rule:

1. Collect `resolved_theses: [Theses/TICKER - Name.md, ...]` from Scope Resolution output.
2. For each path, test existence:
   ```bash
   for path in resolved_theses:
       [ -f "$path" ] || record_as_missing "$path"
   ```
3. If `missing: [ ]` is empty → proceed to Phase 1 normally.

4. If `missing: [ ]` is non-empty:

   **Sector-scoped mode**: stop the skill immediately. Do NOT proceed with a partial scope — scoped portfolio-level output (research velocity ranking, attention allocation, decay alerts) depends on complete coverage; a partial scope silently under-reports these metrics without flagging the gap. Report:
   ```
   ⚠️ Scope resolution via _graph.md found [N] thesis(es) still listed in the Sector → Theses reverse index but no longer present in Theses/:
     - [missing path 1]
     - [missing path 2]
     ...

   _graph.md is stale relative to filesystem state — likely a /status active→closed or /prune closure since the last /graph run.

   Resolution: run /graph last (consumes .graph_invalidations, rebuilds reverse indexes from current filesystem state, excludes archived theses). Then re-run /surface [sector].

   No surface-scan research note was written for this run.
   ```

   **Ticker-scoped mode**: if the scoped ticker itself is in `missing:`, report:
   ```
   ⚠️ /surface [TICKER] — thesis file not found at Theses/[TICKER] - *.md. Likely archived since the last /graph run.

   Options:
     (a) Run /rollback [TICKER] to reopen the archived thesis (then /sync TICKER → /graph last → re-run /surface [TICKER]).
     (b) Run /surface without arguments for a vault-wide scan that will correctly exclude the archived ticker.
     (c) Run /graph last to rebuild indexes from current filesystem state, then re-run /surface [TICKER] — but expect the same error if the thesis is archived.

   No surface-scan research note was written for this run.
   ```
   Stop the skill in either ticker-scoped sub-case.

### Why stop rather than best-effort continue

Scoped modes depend on complete scope coverage. A best-effort continuation would:
- Read `Theses/TICKER - Name.md` and fail silently, skipping that thesis from Phase 1–3 analysis.
- Produce a surface-scan research note that under-reports the sector (missing the archived thesis's historical context, even though its adjacency influenced the sector's dynamics until closure).
- Write `propagated_to: []` on the research note, which blocks `/sync` from auto-healing by retry.

The fail-fast path forces `/graph last` explicitly — cost is one extra command; benefit is correct scope coverage on retry.

### Why not auto-run `/graph last`

`/surface` is an analytical read-only skill that writes a synthesis research note and `_hot.md`. It does not write `_graph.md`. Auto-running `/graph last` would violate the metadata-ownership boundary (only `/graph` and `/rename` write `_graph.md`). User explicitly invokes `/graph last` — one extra command is the correct cost for ownership clarity. `/lint` #38 (`.graph_invalidations` aging) catches the chronic case where users forget to run it.

## Phase 1: Portfolio Scan

**Scoped mode**: Read only files resolved in Scope Resolution. Skip vault-wide checks that require full portfolio coverage (Attention Allocation ranking, Research Velocity ranking across all theses — these need the full set to be meaningful).

**Unscoped mode**: Read all Sector Notes and all active thesis notes (focus on Non-consensus Insights, Risks, and recent Log entries).

## Phase 2: Connection Analysis

**Portfolio Blind Spots**
- Identify sectors or sub-sectors the vault's theses imply are important but have NO coverage. (e.g., if you hold BESI + LITE + NVDA, you're implicitly betting on advanced packaging — do you cover the substrate suppliers? The test equipment vendors? The materials companies?)
- Flag value chain nodes that appear in multiple theses' Risk sections but have no dedicated research — these are unmonitored dependencies
- Check for "implied but unwritten" theses — tickers mentioned in 3+ research notes that still have no Thesis note. These are ideas the vault has been circling without committing to
- Identify adjacent companies that vault research strongly implies should be covered based on competitive dynamics in Sector Notes

**Supply Chain Mapping**
- Which thesis companies are suppliers, customers, or competitors of each other?
- Are there hidden portfolio correlations? (e.g., multiple bets on the same underlying trend)
- Would a single event break multiple theses simultaneously?

**Macro Exposure Audit**
- Map each thesis against current macro scenarios (Iran conflict, AI bubble risk, rate expectations)
- Flag theses with unacknowledged macro sensitivity
- Identify natural hedges within the portfolio

**Catalyst Calendar**
- What upcoming events could move multiple positions?
- Are there clustered earnings dates that create portfolio risk?
- Any regulatory, geopolitical, or technology milestones approaching?

**Contrarian Signal Detection**
- Where does the vault's thesis directly contradict current sell-side consensus?
- Which positions have the widest gap between vault conviction and market pricing?
- These are the highest-alpha opportunities — flag them prominently

**Research Freshness Audit**
- Which theses have the oldest research? (Longest time since last Research/ note)
- What developments might have occurred that aren't reflected?
- Search the web for 2-3 most material recent developments

**Thesis Velocity & Attention Allocation**
- **Research velocity ranking**: Which theses received the most research activity recently (new Research/ notes, Log entries, edits)? Which received zero? Rank all active theses by volume of recent activity.
- **Attention vs conviction alignment**: Compare where research time was spent against conviction levels. Flag any mismatch — disproportionate time on low-conviction ideas while high-conviction theses go unattended is a resource allocation error.
- **Decay alert**: List any active thesis that hasn't been touched (no Log entry, no new linked research) in 30+ days. These are candidates for `/deepen` or `/prune`.

## Phase 3: Opportunity Generation

Generate 3-5 specific, actionable research prompts ranked by potential conviction impact:

For each opportunity:
- **Topic**: What to research
- **Why now**: What triggered this being relevant
- **Vault connection**: Which existing notes it builds on
- **Expected impact**: High/Medium/Low potential to change a conviction level
- **Suggested approach**: Specific research steps

## Phase 4: Output

Save findings to:
- **Unscoped**: `Research/YYYY-MM-DD - Insight Surface Scan.md`
- **Ticker-scoped**: `Research/YYYY-MM-DD - [TICKER] - Surface Scan.md`
- **Sector-scoped**: `Research/YYYY-MM-DD - [Sector] - Surface Scan.md`

If the file already exists, append a counter (`...2.md`, `...3.md`). Save with:
```yaml
---
date: YYYY-MM-DD
tags: [research, meta, surface-scan]
status: active
source: vault synthesis
source_type: synthesis
propagated_to: []
---
```

> **Why `propagated_to: []`**: Surface scans are exploratory portfolio-level metadata, not per-thesis evidence. Their body wikilinks reference many theses for context, NOT to claim each one needs a Log entry. The empty list is a **terminal dedup signal** to `/sync` Check 2 — the producer skill (this `/surface` run) explicitly declares "no propagation needed." Without this, the next `/sync` would treat each body wikilink as a propagation target and spam Log entries across 10+ theses with shallow scan-derived insights. See `/sync` Step 1 Check 2 for the empty-list semantics.

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the surface scan research note, new cross-thesis connections, and any implied-but-unwritten thesis candidates in the dependency map.

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: surface scan completed [scoped/unscoped], top insight found, and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Open Questions**: Add any critical blind spots or research gaps the scan exposed

**Word cap**: After all `_hot.md` edits, follow the compression trigger order in `.claude/skills/_shared/hot-md-contract.md` §"Compression trigger order": drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → emit warning. Soft cap 4,000 words, hard cap 5,000 words (abort `_hot.md` write on hard-cap breach; `/surface` primary operation still succeeds).

Also report a concise summary to the user highlighting the top 3 most actionable insights.

## Phase 5: Release lock

After Phase 4's report is complete, release the vault lock per `.claude/skills/_shared/preflight.md` §1.7 as the skill's FINAL Bash block. Lock scope depends on mode acquired in Step 0.1:
- Unscoped or sector-scoped → `.vault-lock`
- Ticker-scoped → `.vault-lock.TICKER`

Runs unconditionally — whether the scan produced findings or ran clean.

```bash
# Lock release — verify ownership before rm (preflight §1.5)
# LOCK_FILE path depends on mode:
#   unscoped / sector → .vault-lock
#   ticker            → .vault-lock.TICKER
LOCK_FILE="<paste-from-Step-0.1>"                # e.g., .vault-lock or .vault-lock.NVDA
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ($LOCK_FILE) ==="
else
  echo "⚠️ Lock ownership check failed at release ($LOCK_FILE) — skipping rm to avoid stealing another skill's lock."
fi
```
