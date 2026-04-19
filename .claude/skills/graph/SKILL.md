---
name: graph
description: Rebuild the vault dependency graph (_graph.md). Three modes — /graph (full rebuild), /graph last (skip if unchanged since last write, else full rebuild), /graph [N] (skip if unchanged in last N days, else full rebuild). Use /graph last after every /sync, /graph [N] for catch-up, /graph for full disaster-recovery rebuild.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(find * wc * date * grep *)
---

Rebuild `_graph.md` entirely from vault state. This is a structural metadata operation — no content files are modified, no thesis/sector/macro updates, no snapshots, no `_hot.md` changes.

**This skill never touches `.last_sync`.** The watermark is owned exclusively by `/sync`.

## Mode Detection

Parse `$ARGUMENTS` to determine mode:

- **`/graph last`** — **Incremental.** Skip rebuild if no files have changed since `_graph.md`'s `date:` frontmatter. Otherwise, full rebuild. Use after every `/sync` to keep the dependency map current.
- **`/graph [N]`** — **Catch-up incremental.** Skip rebuild if no files have changed in the last N days. Otherwise, full rebuild. Use to catch up after periods without `/graph last` (e.g., `/graph 7` for a week of activity).
- **`/graph`** (no arguments) — **Full rebuild.** Always rebuilds from scratch. Use after `/sync all`, `/lint` flagging graph health issues, or for periodic disaster-recovery rebuilds.

Mode resolution: if `$ARGUMENTS` matches the literal string `last`, use `/graph last` mode. If `$ARGUMENTS` matches an integer N (e.g., `7`, `30`), use `/graph [N]` mode. Otherwise (empty or unrecognized), use full rebuild.

## Watermark Check (incremental modes only — skip for full rebuild)

For `/graph last` and `/graph [N]` modes, perform the watermark check before any other work. If the check passes (no changes since watermark), skip Steps 1–8 entirely.

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
- **One or more files changed**: Proceed to Step 1 to perform a full rebuild against current vault state. The rebuild captures all changes; partial-rebuild is intentionally avoided to prevent reverse-index drift and consistency bugs that plagued the prior architecture.

> **Why "rebuild if changed" instead of true incremental**: A true incremental update (only re-process changed files' adjacencies) requires reverse-index diff logic that is the source of most graph metadata edge cases. The "skip if unchanged, full rebuild if changed" approach preserves the cheap-when-idle property without introducing partial-update bugs. Full rebuild is ~15-20 seconds for a typical vault — negligible compared to the `/sync` it follows.

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
