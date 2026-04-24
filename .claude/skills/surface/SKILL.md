---
name: surface
description: Surface new insights, potential trades, and research opportunities from existing vault content. Use when user says "surface", "what am I missing", "find opportunities", or "what should I research next".
model: opus
effort: max
context: fork
agent: general-purpose
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

- **`all`** (literal keyword): Full vault, **full-read mode** (comprehensive, legacy pre-2026-04-21 behavior). Reads every thesis, sector, and macro note in full. Use when doing a once-off deep review and willing to pay the larger context cost for maximum signal.
- **Ticker** (e.g., `NVDA`): Read `_graph.md` and resolve the ticker's adjacency set — its thesis, sector note(s), macro note(s), cross-thesis references, and all linked research. Also include theses that share a sector (one ring outward) for competitive context.
- **Sector** (e.g., `semiconductors`): Use `_graph.md` Sector → Theses reverse index to resolve all theses in that sector, plus the sector note, related macro notes, and their linked research.
- **No arguments / empty**: Full vault, **section-targeted mode** (default). Reads bounded per-thesis sections only — fast, lean, suitable for weekly/monthly cadence.

Argument disambiguation: `all` is a reserved keyword (matches `/sync all` precedent). Never a ticker — no archived or live thesis with that filename pattern. Never a sector — no sector note named `all`. `$ARGUMENTS` is case-sensitive for ticker/sector match but `all` is accepted in any case (`all`, `ALL`, `All` all route to full-read mode).

If a non-`all` scope is requested but `_graph.md` does not exist, warn: `⚠️ Graph missing — cannot scope. Run /graph first, or run /surface (default, section-targeted) or /surface all (full-read) without arguments.` Then stop.

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

Design rationale in `.claude/skills/surface/RATIONALE.md` §1.

### Why not auto-run `/graph last`

Design rationale in `.claude/skills/surface/RATIONALE.md` §2.

## Phase 1: Portfolio Scan (mode-dependent read strategy)

Read strategy branches by scope. The two full-vault modes trade completeness against subagent context budget:

| Mode | Thesis reads | Expected read budget | Use when |
|---|---|---|---|
| `/surface` (default) | Section-targeted (frontmatter + 4 sections + last 5 Log) | ~50-80K words | Weekly / monthly cadence; part of a maintenance chain |
| `/surface all` | Full read (entire file per thesis) | ~220K words | Once-off deep review; willing to pay larger context for maximum signal |
| `/surface TICKER` | Full read of scope set | ~20-40K words | Ticker-focused insight discovery |
| `/surface [sector]` | Full read (≤6 theses) or section-targeted (>6 theses) | ~20-80K words | Sector-level review |

### Unscoped default mode — section-targeted reads

1. For each thesis file in `Theses/*.md` (every file — draft, active, monitoring; not just active):
   - Read **only**: frontmatter + `## Summary` + `## Key Non-consensus Insights` + `## Risks` + `## Catalysts` + **last 5 Log entries**
   - Skip: Business Model & Product Description, Industry Context, Key Metrics, Bull Case, Bear Case, Outstanding Questions, Related Research, older Log entries
   - Target: ~800-1,500 words per thesis instead of ~4,000-6,000 — reduces total thesis read from ~175K words to ~35-50K words
   - Extract (Bash targeted awk):

```bash
for f in Theses/*.md; do
  echo "=== $f ==="
  awk '
    # Always emit frontmatter
    /^---$/ && !fm_done { in_fm=!in_fm; print; if(!in_fm) fm_done=1; next }
    in_fm { print; next }
    # Summary / Non-consensus Insights / Risks / Catalysts sections
    /^## Summary/,/^## /        { if($0!~/^## / || $0~/^## Summary/)                  print }
    /^## Key Non-consensus Insights/,/^## /  { if($0!~/^## / || $0~/^## Key Non-consensus/) print }
    /^## Risks/,/^## /          { if($0!~/^## / || $0~/^## Risks/)                    print }
    /^## Catalysts/,/^## /      { if($0!~/^## / || $0~/^## Catalysts/)                print }
    # Log: keep everything from ## Log forward — LLM takes last 5 entries in reasoning layer
    /^## Log/{in_log=1}
    in_log{print}
  ' "$f"
done
```

2. **Issue steps 2-4 as a single parallel tool-call batch** (after Step 1's awk block lands): all Sector Note Reads (~13) + all Macro Note Reads (~6) + all heavily-cited research note Reads (~10-20) in ONE message with multiple Read invocations. Do NOT serialize. Total ~30-40 Reads lands in one round-trip.
3. Read all **Sector Notes** in full (bounded set, ~13 files). Competitive dynamics, value chain analysis, and investor heuristics are needed in full.
4. Read all **Macro Notes** in full (bounded set, ~6 files). Scenario frameworks require complete context.
5. For heavily cited research notes (appearing in ≥3 theses' Related Research via `_graph.md` orphan+adjacency lookup): read in full. All other research notes: trust the thesis Log citations as summaries.

**Expected read budget**: ~50-80K words total (was ~220K words pre-R2). Reclaim: ~170K words = ~225K tokens per unscoped run.

### `/surface all` mode — full-read comprehensive scan

Use when the user wants maximum analytical depth for a once-off deep review. Reads every thesis file in full — accepts the larger subagent context cost for richer cross-thesis connection detection (particularly valuable for Business Model and Industry Context cross-referencing that section-targeted mode misses).

**Issue ALL reads in steps 1-3 as a single parallel tool-call batch** — one message with every thesis Read (~42), every Sector Read (~13), and every Macro Read (~6) firing in parallel. Do NOT serialize. Typical batch: ~61 Reads landing in one round-trip instead of 61 sequential rounds. Step 4's heavily-cited research reads join the same parallel batch when `_graph.md` adjacency is already loaded; otherwise they land in a second parallel batch after the Step 1-3 batch returns.

1. Read every `Theses/*.md` in full (all 13 thesis sections). No awk extraction.
2. Read all Sector Notes in full.
3. Read all Macro Notes in full.
4. For heavily cited research notes (≥3 theses in `_graph.md` adjacency): read in full — include in the parallel batch with steps 1-3 (one round-trip). For others: read on-demand when Phase 2 analysis surfaces a specific question about them.

**Expected read budget**: ~220K words total (matches pre-R2 behavior). Subagent context consumption: ~290K tokens. Still comfortably under the subagent budget because `context: fork` isolates this from main session context.

**Output differentiation**: `/surface all` research notes carry `source_type: synthesis` with `scope: all` in a `scope:` frontmatter field, so downstream review can distinguish deep-scan outputs from routine `/surface` scans. Filename: `Research/YYYY-MM-DD - Insight Surface Scan (all).md`.

**When to prefer `/surface` over `/surface all`**: unless you're explicitly doing a quarterly/annual portfolio deep-review, default mode is strictly better — same insight signal at 25% the read cost. `/surface all` is the escape hatch for cases where section-targeting empirically misses a cross-section pattern.

### Scoped mode — reads bounded by scope resolution

**Ticker-scoped `/surface TICKER`**: read the resolved ticker + adjacencies (thesis, sector, macros, cross-thesis, linked research, sector peers). Set is small (1 focal thesis + 2-6 peers); section-targeting not needed — read all files in full for full competitive context.

**Sector-scoped `/surface [sector]`**: read the sector note + all theses in that sector + linked macros + their research. Typical set is 3-8 theses; apply section-targeting (as in default mode above) only if the sector has >6 theses.

Skip vault-wide checks that require full portfolio coverage (Attention Allocation ranking, Research Velocity ranking across all theses — these need the full set to be meaningful).

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
- **Unscoped default**: `Research/YYYY-MM-DD - Insight Surface Scan.md`
- **Unscoped `all`**: `Research/YYYY-MM-DD - Insight Surface Scan (all).md`
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
scope: default | all | ticker:TICKER | sector:[Sector]
propagated_to: []
---
```

The `scope:` frontmatter field records which mode produced the note — lets downstream review (and `/lint`) distinguish a routine section-targeted scan from a deep `all` scan or a scoped run.

> **Why `propagated_to: []`**: Surface scans are exploratory portfolio-level metadata, not per-thesis evidence. Their body wikilinks reference many theses for context, NOT to claim each one needs a Log entry. The empty list is a **terminal dedup signal** to `/sync` Check 2 — the producer skill (this `/surface` run) explicitly declares "no propagation needed." Without this, the next `/sync` would treat each body wikilink as a propagation target and spam Log entries across 10+ theses with shallow scan-derived insights. See `/sync` Step 1 Check 2 for the empty-list semantics.

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the surface scan research note, new cross-thesis connections, and any implied-but-unwritten thesis candidates in the dependency map.

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: surface scan completed [scoped/unscoped], top insight found, and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Open Questions**: Add any critical blind spots or research gaps the scan exposed

**Word cap**: After all `_hot.md` edits, check total word count. If over 4,000 words (soft cap per `_shared/hot-md-contract.md`), prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap. If over 5,000 (hard cap), abort `_hot.md` update per contract.

Also report a concise summary to the user highlighting the top 3 most actionable insights.
