---
name: deepen
description: Targeted deep research to fill a specific gap in an existing thesis. Use when user says "deepen", "flesh out", "expand on", "fill in", or specifies a thesis section to improve.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * cp * mkdir * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Surgically improve one section of an existing thesis with deep research. This is NOT a full thesis rewrite — it's targeted enhancement of the weakest or most requested part.

## Arguments
$ARGUMENTS should be: `[TICKER] [optional: section name]`
- Examples: `NVDA Outstanding Questions`, `BESI Industry Context`, `LITE`, `APP Bull Case`
- If no section is specified, auto-detect the weakest section (see Phase 2)

## Phase 0: Pre-flight (MANDATORY — runs before Phase 1)

### 0.1: Acquire vault lock
Acquire a `ticker:TICKER` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 10 minutes (deep research may be long-running; extend with a `timeout_at` renewal if web research runs over). Release via `trap` on exit.

### 0.2: Rename-marker pre-flight
Run `.claude/skills/_shared/preflight.md` Procedure 2. If `.rename_incomplete.TICKER` exists at vault root, hard-block per the contract's 2.3 collision message. Rewriting a thesis section while wikilinks are split across old and new names would compound the split — the rewrite would embed wikilinks keyed to the current (new) filename while some inbound references still point to the old name.

Both checks must pass before proceeding to Phase 1.

### 0.3: Section existence probe (only if specific section was specified)

If `$ARGUMENTS` includes a section name (not auto-detect mode), run `.claude/skills/_shared/preflight.md` Procedure 4 (section existence probe) against the thesis file with the target `## [Section Name]` heading.

If the section does NOT exist in the thesis:

```
❌ Section "## [requested section]" not found in Theses/TICKER - Name.md.

Sections present in this thesis:
  - ## Summary
  - ## Key Non-consensus Insights
  - ## [list every ## heading found in the thesis]

Sections expected per Templates/Thesis Template.md but missing:
  - ## [missing section 1]
  - ## [missing section 2]
  - ...

Options:
  (a) /deepen TICKER [existing-section]   — deepen a section that exists
  (b) /deepen TICKER                      — auto-detect weakest present section (Phase 2)
  (c) Restore missing section from Templates/Thesis Template.md manually,
      then re-run /deepen TICKER [section]
  (d) /lint TICKER                        — surface all template drift first (check #14)

Aborted — no changes made to the thesis.
```

**Do NOT silently create the section.** Structural changes to thesis templates must be explicit user action. The thesis's current section inventory is the user's (or a prior skill's) intentional state; `/deepen` deepens existing sections, never authors new ones from nothing.

If auto-detect mode (`$ARGUMENTS` is just TICKER), skip this probe — Phase 2 evaluates only sections that actually exist and scores their weakness.

## Phase 1: Load Context
1. Read the thesis note from Theses/
2. Read ALL research notes linked from the thesis (Related Research + Log entries)
3. Read the relevant Sector Note
4. Read any Macro notes relevant to the thesis sector
5. Grep for the ticker across the vault to find mentions in notes not yet linked

## Phase 2: Identify the Target
If a section was specified in $ARGUMENTS, use that. Otherwise, auto-detect:

**Weakness scoring** (check each, flag the worst):
- **Empty or stub sections**: sections with just `-` or `<!-- -->` placeholder comments
- **Key Non-consensus Insights**: if fewer than 3 substantive paragraphs, this is the priority (CLAUDE.md marks this as the most important section)
- **Outstanding Questions**: if fewer than 3 questions, the thesis hasn't been properly challenged
- **Business Model & Product Description**: if under 200 words, the understanding is superficial
- **Industry Context**: if missing value chain analysis or competitive dynamics
- **Key Metrics**: if the table has empty cells or data older than 6 months
- **Bull/Bear Case imbalance**: if one is dramatically shorter than the other (suggests bias)
- **Risks**: if fewer than 3 risks, the thesis is underprotected
- **Catalysts**: if empty or all dates have passed
- **Conviction Triggers**: if missing or vague (not falsifiable)

Tell the user which section you're targeting and why before proceeding.

## Phase 3: Deep Research
1. **Vault research first**: Extract every relevant data point from existing research notes, sector notes, and macro notes. Do not duplicate what's already captured.
2. **Web research**: Search for recent developments specific to the target section:
   - For Key Non-consensus Insights: search for sell-side consensus, then find evidence that contradicts it
   - For Outstanding Questions: search for answers to existing questions AND identify new questions a skeptical investor would ask
   - For Business Model: search for revenue breakdowns, segment reporting, product specs, analyst commentary on business model
   - For Industry Context: search for market share data, competitive dynamics, recent M&A, new entrants
   - For Key Metrics: search for latest financial data (quarterly earnings, guidance)
   - For Bull/Bear Case: search for the strongest version of whichever side is underweight
   - For Risks: search for bear cases, short seller reports, regulatory risks, technological disruption
   - For Catalysts: search for upcoming earnings dates, product launches, regulatory decisions, industry events
   - For Conviction Triggers: search for the most likely binary events that would decisively change the thesis
3. **Cross-reference**: Check if new findings affect other theses in the vault

## Phase 4: Pre-Edit Safety — Snapshot

Before rewriting the target section, snapshot the thesis:

1. Create snapshot directory if needed:
   ```bash
   mkdir -p _Archive/Snapshots
   ```
2. Copy the current thesis note:
   ```bash
   cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-deepen YYYY-MM-DD-HHMMSS).md"
   ```
3. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Theses/TICKER - Company Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: deepen
   snapshot_batch: deepen-YYYY-MM-DD-HHMMSS
   ```

## Phase 5: Rewrite the Target Section

### 5a: Pre-announce Log entry (audit trail before destructive edit)
Append a provisional Log entry to the thesis BEFORE rewriting the section. This ensures an audit trail exists even if the skill fails mid-rewrite:
```
### YYYY-MM-DD
- Deepening [Section Name] — in progress. Snapshot: [[_Archive/Snapshots/...]]
```

### 5b: Rewrite the section
- Rewrite the section in-place, preserving the thesis note's overall structure
- Follow the conventions from CLAUDE.md and the Thesis Template:
  - Non-consensus Insights: 3-5 one-paragraph summaries of what the market is missing
  - Outstanding Questions: 3-10 one-paragraph summaries of what a skeptical IC would ask
  - Business Model: in-depth with analogies, product specs, revenue segmentation
  - Industry Context: competitive dynamics, market share shifts, value chain analysis
  - Conviction Triggers: concrete, falsifiable if/then statements with specific thresholds
- **Integrate, don't append** — the section should read as a coherent whole, not show seams between old and new content
- Bold any genuinely new data points or insights not previously in the vault
- Add wikilinks to any vault notes referenced

### 5c: Finalize Log entry
After the rewrite succeeds, use `Edit` to atomically replace the provisional Log entry with the final version:
```
### YYYY-MM-DD
- Deepened [Section Name]: [key finding] — conviction [unchanged/strengthened/weakened + reason]. Snapshot: [[_Archive/Snapshots/...]]
```
Replace `Deepening [Section Name] — in progress` with `Deepened [Section Name]: [key finding] — conviction [impact + reason]`.

**Verify and retry**: After the Edit, re-read the thesis `## Log` section and confirm the provisional text (`Deepening [Section Name] — in progress`) is gone:

1. **Edit succeeded** → provisional text absent → proceed to Phase 6.
2. **Edit failed** (provisional text still present) → retry with broader context:
   - Include the full `### YYYY-MM-DD` date header AND the provisional line as `old_string` to ensure uniqueness.
3. **Retry also failed** → append a corrective entry immediately below the stuck provisional entry:
   ```
   - ↳ CORRECTION: Deepened [Section Name]: [key finding] — conviction [impact + reason]. Supersedes incomplete entry above.
   ```
   This preserves the append-only Log contract while ensuring the audit trail is always complete. `/sync` drift detection recognizes both `"Deepened"` and `"↳ CORRECTION: Deepened"` prefixes.

> **Drift coupling**: `/sync` Step 3e excludes entries starting with `"Deepened"` within 7 days of a stress test from drift detection. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §3 (Deepened) + §2 (Deepening) + §4 (↳ CORRECTION: Deepened). Do not change these prefixes without updating the registry and `/sync`; `/lint` check #29 flags drift.

> **Failure states**: If the skill fails after 5a but before 5b → Log shows "Deepening... in progress" but section is unchanged; snapshot is unnecessary (thesis body intact). If it fails after 5b but before 5c → Log shows "Deepening... in progress" with section already rewritten; the verify-and-retry mechanism (above) will correct the Log entry. Both states are recoverable via snapshot. `/lint` #28 (partial write detection) flags the `"Deepening"` prefix as an indicator — if the corrective entry exists alongside it, lint should downgrade to Nice to Have.

## Phase 6: Update the Vault
1. If new research was substantial, also save a supporting research note to Research/:
   `Research/YYYY-MM-DD - [TICKER] - [Section Topic] Deep Dive.md`
   ```yaml
   ---
   date: YYYY-MM-DD
   tags: [research, deep-dive, TICKER]
   sector: [from thesis]
   ticker: TICKER
   source: vault synthesis
   source_type: deep-dive
   propagated_to: [TICKER]
   ---
   ```
2. Add any new wikilinks to the thesis Related Research section

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register any new research note in the dependency map.

## Phase 7: Update _hot.md

Follow `.claude/skills/_shared/hot-md-contract.md` — compression policy, per-section budgets, truncation-marker avoidance, and cap handling are centralized there. Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: deepened [TICKER] [Section Name], key finding, and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry if conviction was changed or flagged for reassessment
3. **Open Questions**: Mark resolved any questions this research answered; add new questions raised

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Phase 8: Report
Tell the user:
- Which section was deepened and why it was the priority
- Snapshot saved to: `[[_Archive/Snapshots/...]]`
- The 2-3 most important new findings
- Whether conviction should be reassessed based on what was found
- Theses requiring `/sync`: [list any tickers where cross-references suggest propagation is needed]
- **Run `/sync` to propagate these findings to affected sector notes, macro notes, and cross-thesis references.**
