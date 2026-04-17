---
name: graph
description: Rebuild the vault dependency graph (_graph.md) from scratch. Use after /sync all, when /lint flags graph health issues, or when the graph has drifted from vault state.
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(find * wc * date * grep *)
---

Rebuild `_graph.md` entirely from vault state. This is a structural metadata operation — no content files are modified, no thesis/sector/macro updates, no snapshots, no `_hot.md` changes.

**This skill never touches `.last_sync`.** The watermark is owned exclusively by `/sync`.

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

**Chain finalization**: Read `_hot.md` and clear `## Session Chain` to `*No active chain.*` — **removing any Graph Debt line**. The full rebuild captures all deferred changes from vault state, resolving both the active chain's deferred count and any accumulated Graph Debt.
