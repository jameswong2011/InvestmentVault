---
name: graph
description: Rebuild the vault dependency graph (_graph.md). Three modes — /graph (full rebuild), /graph last (true incremental: re-extract only changed thesis adjacencies, always rebuild reverse indexes), /graph [N] (catch-up incremental from N days ago). Use /graph last after every /sync, /graph [N] for catch-up, /graph for full disaster-recovery rebuild.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(find * wc * date * grep *)
---

Rebuild `_graph.md` entirely from vault state. This is a structural metadata operation — no content files are modified, no thesis/sector/macro updates, no snapshots, no `_hot.md` changes.

**This skill never touches `.last_sync`.** The watermark is owned exclusively by `/sync`.

## Mode Detection

Parse `$ARGUMENTS` to determine mode:

- **`/graph last`** — **True incremental.** Skip if no files changed since `_graph.md`'s `date:`. Otherwise re-extract adjacency for **changed thesis files only**; always rebuild reverse indexes, clusters, and orphan list from scratch. Use after every `/sync`.
- **`/graph [N]`** — **Catch-up incremental.** Same logic as `/graph last` but watermark = today − N days. Use to catch up after periods without `/graph last` (e.g., `/graph 7` for a week).
- **`/graph`** (no arguments) — **Full rebuild.** Re-extract adjacency for ALL theses. Use after `/sync all`, when `/lint` flags graph health issues, or for periodic disaster-recovery rebuilds.

Mode resolution: if `$ARGUMENTS` matches the literal string `last`, use `/graph last`. If `$ARGUMENTS` matches an integer N (e.g., `7`, `30`), use `/graph [N]`. Otherwise (empty or unrecognized), use full rebuild.

> **Drift-safety design**: Forward adjacency (per-thesis links) updates incrementally — only re-extracted for changed theses. Reverse indexes (Macro → Theses, Sector → Theses) ALWAYS rebuild fully from `Sectors/*.md` + `Macro/*.md` files. This combination eliminates the reverse-index drift that motivated the metadata-cull architecture: incremental updates can't accumulate drift in reverse indexes because reverse indexes are never incrementally updated. Cross-thesis clusters and orphan list also always recompute from the in-memory adjacency state.

## Watermark Check (incremental modes only — skip for full rebuild)

For `/graph last` and `/graph [N]`, check the watermark before any other work. If the check passes (no changes since watermark), skip the Incremental Path and Steps 1-8 entirely.

### Watermark Resolution

- **`/graph last`**: Read `_graph.md`. If the file does not exist, warn `⚠️ _graph.md missing — falling back to full rebuild` and proceed to Step 1. If `date:` frontmatter is `1970-01-01` (poisoned by a prior `/sync all`), warn `⚠️ _graph.md poisoned by prior /sync all — full rebuild required` and proceed to Step 1. Otherwise, watermark = the `date:` value from frontmatter.
- **`/graph [N]`**: Watermark = `today - N days`. If `_graph.md` does not exist, warn `⚠️ _graph.md missing — falling back to full rebuild` and proceed to Step 1.

### Change Detection

Find files modified after the watermark across all four content directories:

```bash
find Theses/ Research/ Sectors/ Macro/ -name '*.md' -newermt "WATERMARK_DATE"
```

Substitute `WATERMARK_DATE` with the resolved watermark in `YYYY-MM-DD` format.

- **No files changed**: Report `Graph is up to date — no changes since [watermark date].` and stop. Do NOT write `_graph.md` (preserve existing date frontmatter and content).
- **One or more files changed**: Proceed to the **Incremental Path** below. The Incremental Path re-extracts adjacency only for changed thesis files; reverse indexes always rebuild fully to prevent drift. **Do NOT proceed to Steps 1-8** — those are the full rebuild path used by `/graph` (no args) and as a fallback when `_graph.md` is missing/poisoned.

## Incremental Path (for /graph last and /graph [N] when changes detected)

Forward adjacency updates per changed thesis; reverse indexes, clusters, and orphans always rebuild fully from in-memory state. This is the cheap path when most theses are untouched.

### Step I.1: Parse Existing Graph

Read `_graph.md` and parse:
- Thesis Adjacency Index → map of `TICKER - Name → {sectors, macros, cross-thesis, research}`
- Existing orphan list (used for diff reporting)
- Existing cluster table (used for diff reporting)

This becomes the **baseline** for incremental updates. If parsing fails (corrupt file), warn `⚠️ _graph.md unparseable — falling back to full rebuild` and proceed to Step 1.

### Step I.2: Bucket the Changed Files

From the change-detection set, separate by directory:
- **Changed Thesis files** (`Theses/*.md`): re-extract their adjacency entries in Step I.4
- **Changed Sector / Macro files** (`Sectors/*.md`, `Macro/*.md`): no per-file action needed — reverse indexes rebuild fully in Step I.5
- **Changed Research files** (`Research/*.md`): no per-file action needed — orphan list recomputes in Step I.7. (Research note edits don't affect thesis adjacency; only their existence does.)

### Step I.3: Detect Thesis Additions and Removals

Compare current `Theses/*.md` files on disk against baseline adjacency entries:
- **Added theses** (file exists on disk, no entry in baseline): mark for fresh adjacency extraction in Step I.4
- **Removed theses** (entry in baseline, file does not exist on disk): remove entry from baseline in-memory map. These also disappear from cross-thesis cluster recomputation in Step I.6.

### Step I.4: Re-extract Adjacency for Changed + Added Theses

For each thesis flagged in Step I.2 (changed) or Step I.3 (added):
1. Extract outbound `[[wikilinks]]` from the thesis file
2. Categorize each link:
   - Target in `Sectors/` → sector adjacency
   - Target in `Macro/` → macro adjacency
   - Target in `Theses/` → cross-thesis adjacency
   - Target in `Research/` → research adjacency
3. Replace the baseline adjacency entry for this thesis with the new categorization

Unchanged theses retain their baseline adjacency entries — no re-read required.

### Step I.5: Rebuild Reverse Indexes (Always Full)

Read every `Sectors/*.md` and `Macro/*.md` file unconditionally (~13 + 6 = 19 files, bounded and cheap):

#### Macro → Theses
For each `Macro/*.md`:
1. Extract outbound `[[wikilinks]]` targeting `Theses/`
2. Build mapping: `Macro/Note → sorted [tickers]`

#### Sector → Theses
For each `Sectors/*.md`:
1. Extract outbound `[[wikilinks]]` targeting `Theses/`
2. Build mapping: `Sectors/Name → sorted [tickers]`

This step always runs full — even if zero sector/macro files changed — so reverse indexes can never accumulate drift from the forward index.

### Step I.6: Recompute Cross-Thesis Clusters

Cross-thesis clusters depend only on forward adjacency `cross-thesis:` fields, which are fully current in the in-memory map after Step I.4. Recompute from scratch:
1. Build pairs (A, B) where A's `cross-thesis:` includes B AND B's `cross-thesis:` includes A
2. Group connected pairs into clusters via union-find
3. Format as the cluster table

### Step I.7: Recompute Orphan List

From the in-memory adjacency map:
1. Collect all research note wikilinks across every thesis's `research:` field → set `linked_research`
2. Inventory `Research/*.md` files on disk → set `all_research`
3. Orphans = `all_research − linked_research`, sorted

### Step I.8: Recount Edges

Sum from updated in-memory state:
- Forward adjacency: per thesis, count of `sectors + macros + cross-thesis + research`
- Reverse indexes: per row, count of theses listed

### Step I.9: Write Updated _graph.md

Write the merged graph using the same format as full rebuild:
- Frontmatter `date:` → today; counts updated
- `## Thesis Adjacency Index` → all entries (changed + added + unchanged), sorted
- `## Reverse Index: Macro → Theses` → from Step I.5
- `## Reverse Index: Sector → Theses` → from Step I.5
- `## Cross-Thesis Clusters` → from Step I.6
- `## Orphan Research Notes` → from Step I.7

### Step I.10: Validate (same as Step 7.5)

Re-read `_graph.md` and run the validation checks listed in Step 7.5. If any structural check (1-2) fails, the file is corrupt — restore from git or run `/graph` (no args) for full rebuild. If content checks (3-6) fail, log warnings and recommend full rebuild.

### Step I.11: Report

- **Mode**: `/graph last` from [watermark date] | `/graph [N]` from [N] days ago
- **Changed thesis adjacencies re-extracted**: [count]
- **Theses added**: [list, or "none"]
- **Theses removed**: [list, or "none"]
- **Reverse indexes**: rebuilt from scratch (always)
- **Cross-thesis clusters**: [list new/dissolved, or "no structural changes"]
- **Orphan deltas**: [N newly orphaned, M no-longer-orphaned]
- **Edges**: [old → new]
- **Validation**: passed | [list specific failures]
- **No content files modified** — graph update only

## Step 1: Inventory Vault

List all files that participate in the graph:

```bash
find Theses/ -name '*.md' | sort
find Research/ -name '*.md' | sort
find Sectors/ -name '*.md' | sort
find Macro/ -name '*.md' | sort
```

Record counts for frontmatter: theses, sectors, macro, research.

## Step 2: Extract Thesis Adjacency

For each thesis in `Theses/`:
1. Extract all outbound `[[wikilinks]]`:
   ```bash
   grep -oE '\[\[[^\]]+\]\]' "Theses/TICKER - Company.md"
   ```
2. Categorize each link:
   - Target in `Sectors/` → sector link
   - Target in `Macro/` → macro link
   - Target in `Theses/` → cross-thesis link
   - Target in `Research/` → research link
   - Other targets → ignore (templates, archives, etc.)
3. Build the adjacency entry:
   ```
   ### TICKER - Company Name
   - sector: [[Sectors/Sector Name]]
   - macro: [[Macro/Note1]], [[Macro/Note2]]
   - cross-thesis: [[Theses/OTHER - Company]]
   - research: [[Research/2026-01-15 - Topic - Source.md]], ...
   ```

## Step 3: Build Reverse Indexes

### Macro → Theses
For each file in `Macro/`:
1. Extract all outbound `[[wikilinks]]` that target `Theses/`
2. Build the reverse mapping: which theses does each macro note link TO

### Sector → Theses
For each file in `Sectors/`:
1. Extract all outbound `[[wikilinks]]` that target `Theses/`
2. Build the reverse mapping: which theses does each sector note link TO

**Consistency note:** Forward indexes (thesis → sector/macro) and reverse indexes (sector/macro → thesis) are built independently from their respective source files. They may disagree — this is expected and `/lint` check #23 catches it. The graph records both directions faithfully without attempting reconciliation.

## Step 4: Build Cross-Thesis Clusters

Scan the adjacency index for bidirectional cross-thesis references:
- If Thesis A lists Thesis B in `cross-thesis:` AND Thesis B lists Thesis A → bidirectional cluster (↔)
- If only one direction → unidirectional reference (→), note but don't cluster

Format as a table:
```
| Cluster | Members | Link Type |
|---|---|---|
| AI Compute | [[NVDA]], [[AVGO]], [[MRVL]] | ↔ |
| Memory | [[MU]], [[SNDK]] | ↔ |
```

## Step 5: Identify Orphan Research Notes

Scan all `Research/*.md` files. A research note is orphaned if it is NOT listed in ANY thesis's `research:` field in the adjacency index.

```bash
# For each research note, check if any thesis links to it
grep -rl "Research/note-name" Theses/
```

List orphans in the graph. These are research notes with no thesis connection — candidates for linking or archival.

## Step 6: Count Edges

Count total unique directional wikilinks extracted from thesis + sector + macro files. This is the `edges:` frontmatter value.

Method: sum all wikilinks extracted in Steps 2–3 (deduplicated per source file, but the same target linked from two different files counts as two edges).

## Step 7: Write _graph.md

**Before overwriting**: If `_graph.md` already exists, read it now and retain the old content for comparison in Step 8. Extract: thesis count, edge count, orphan count, list of adjacency entries, and cluster table.

Write the complete `_graph.md` with this structure:

```yaml
---
type: vault-graph
date: YYYY-MM-DD
theses: [count]
sectors: [count]
macro: [count]
research: [count]
edges: [count]
orphans: [count]
---
```

Sections:
1. `## Thesis Adjacency Index` — all entries from Step 2
2. `## Reverse Index: Macro → Theses` — from Step 3
3. `## Reverse Index: Sector → Theses` — from Step 3
4. `## Cross-Thesis Clusters` — from Step 4
5. `## Orphan Research Notes` — from Step 5

## Step 7.5: Validate Written Graph

Re-read `_graph.md` after writing and verify structural integrity:
1. YAML frontmatter parses without error — all expected fields present (`type`, `date`, `theses`, `sectors`, `macro`, `research`, `edges`, `orphans`)
2. All five section headings exist: `## Thesis Adjacency Index`, `## Reverse Index: Macro → Theses`, `## Reverse Index: Sector → Theses`, `## Cross-Thesis Clusters`, `## Orphan Research Notes`
3. Every `### TICKER - Name` entry in the adjacency index has at least a `sector:` field
4. All wikilinks have valid `[[...]]` syntax (no unclosed brackets)
5. Frontmatter counts match actual content: `theses:` equals the number of `###` entries in Adjacency Index, `orphans:` equals the number of items in Orphan list
6. Every file listed in an adjacency entry actually exists on disk (spot-check: verify the first and last entry, plus any entry that was newly added or changed from the previous graph)

If any check fails:
- Checks 1-2 (structural): `❌ Graph rebuild produced a corrupt file — [specific failure]. Re-run /graph.`
- Checks 3-6 (content): `⚠️ Graph rebuilt with minor issues — [specific failure]. Review and re-run /graph if needed.`

Include validation results in the Step 8 report.

## Step 8: Report

- **Nodes**: [count] (theses + sectors + macro + research)
- **Edges**: [count]
- **Orphans**: [count]
- **Changes from previous graph** (if old graph was captured in Step 7):
  - Theses added/removed: [list]
  - Edges added: [count] | Edges removed: [count]
  - Orphans resolved: [list] | New orphans: [list]
  - Reverse index corrections: [count]
  - Cluster changes: [list any new or dissolved clusters]
- **No content files were modified** — graph rebuild only
