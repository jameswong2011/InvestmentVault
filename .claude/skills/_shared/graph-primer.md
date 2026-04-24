# Graph Primer Contract

Consumed by: `/ingest`, `/compare`, `/thesis`, `/stress-test`, `/brief`, `/deepen`
Also referenced: `/scenario` (existing consumer), `/surface` (existing consumer)
Owned by: `/graph` (exclusive writer of `_graph.md`)

## Core principle

Graph is a PRIMER, never a FILTER. It tells you WHO is connected; content reads tell you WHAT those connections mean. Skills using the primer to SKIP content reads degrade research quality. Skills using it to ORIENT content reads preserve quality and gain cross-ticker correctness.

## Invocation

Single Read of `_graph.md` at the skill's declared primer step. Parse once in-memory. Never re-Read within the same skill run. Always issue the Read in parallel with the skill's other mandatory Reads (thesis, research notes) to absorb into one tool-call round-trip.

## Data structures (in-memory, post-parse)

After parsing `_graph.md`, expose to the skill's reasoning layer:

- `adjacency_index`: `Map[TICKER → {sectors, macros, cross-thesis, research, status, log_tail}]`
- `macro_reverse`: `Map[MacroName → List[TICKER]]`
- `sector_reverse`: `Map[SectorName → List[TICKER]]`
- `clusters`: `List[{name, members, link_type}]`
- `orphans`: `Set[ResearchNoteName]`

## Extraction modes

### Mode A: Ticker-scoped primer

Used by: `/brief`, `/stress-test`, `/deepen`, `/thesis`

Given target TICKER, extract:
- `entry = adjacency_index[TICKER]` (or null if absent — see Missing-graph fallback + new-thesis special handling)
- `cluster` = first cluster in `clusters` where `TICKER ∈ cluster.members`
- `cluster_peers = cluster.members - {TICKER}` (empty if no cluster)
- `sector_peers = union over s ∈ entry.sectors of sector_reverse[s] - {TICKER}`
- `macro_peers = union over m ∈ entry.macros of macro_reverse[m] - {TICKER}`

Return `{entry, cluster, cluster_peers, sector_peers, macro_peers}`.

**New-thesis special handling** (for `/thesis`): if `entry` is null (target TICKER not yet in graph), infer `sectors` and `macros` from vault research gathered upstream in the skill. Compute `candidate_sector_peers` from `sector_reverse[s]` for each inferred sector, same for macro. Surface as suggestions for user review.

### Mode B: Compare primer

Used by: `/compare`

Given targets `A`, `B` (and `C`, `D`, ... for N>2):
- `entry_a = adjacency_index[A]`, `entry_b = adjacency_index[B]`, ...
- `shared_sectors = entry_a.sectors ∩ entry_b.sectors`
- `shared_macros = entry_a.macros ∩ entry_b.macros`
- `shared_research = entry_a.research ∩ entry_b.research`
- `cross_thesis_link` = `(B ∈ entry_a.cross-thesis, A ∈ entry_b.cross-thesis)` → `both | A→B | B→A | none`
- `cluster_co_member` = `∃ c ∈ clusters where {A, B} ⊆ c.members`

For N>2: compute pairwise for all pairs. Aggregate `common_sectors = intersection across all entries` and `common_macros = intersection across all entries`.

Return `{shared_sectors, shared_macros, shared_research, cross_thesis_link, cluster_co_member}` per pair, plus aggregate for N>2.

### Mode C: Propagation-fanout primer

Used by: `/ingest`

Given a new research note with primary ticker `T`, sector `S`, macro references `M` (any may be null):
- `direct_targets` = theses already matched in the skill's prior step (ticker/topic grep results from ingest Step 3)
- `sector_fanout = sector_reverse[S]` if S else `[]`
- `sector_candidates = sector_fanout - direct_targets`
- `macro_fanout = union over each m ∈ M of macro_reverse[m]`
- `macro_candidates = macro_fanout - direct_targets - sector_candidates`

Return `{direct_targets, sector_candidates, macro_candidates}`.

All three sets surface to the user in the skill's report as strong / weak-match-sector / weak-match-macro. User decides whether to wikilink before `/sync`.

### Mode D: Scenario primer (existing)

Used by: `/scenario`

Existing use of `_graph.md` for portfolio topology and cluster retrieval. No change — documented here for completeness.

## Missing-graph fallback

`_graph.md` absent or unparseable → log at `ℹ️` severity:
```
ℹ️ _graph.md absent/unparseable — graph primer skipped. Skill proceeds file-direct.
   Run /graph after this skill to enable primer on next run.
```

Never block. Research skills must function standalone. All post-primer steps (content reads, analysis, writes) execute regardless.

## Staleness

Graph reflects state at `last_graph_write:`. Between rebuilds, adjacency may underrepresent real wikilinks (user edits + pending `/graph last`).

Mitigations (all consumer skills MUST follow):

1. **Treat graph as LOWER BOUND of connectivity.** Graph absence of X→Y means "not yet registered," never "not connected." Skills must design around this invariant.
2. **For any propagation decision that writes content** (e.g., `/sync` Step 4/5 sector/macro gate), validate via targeted Grep of current file state. The graph is the fast path; the Grep is the correctness path.
3. **Stale-graph advisory**: if `last_graph_write:` > 24h old, emit
   ```
   ℹ️ graph is [N]h stale — primer may underrepresent recent connectivity.
      Consider /graph last.
   ```
   Do not block.

## Anti-patterns (lint-enforced via `/lint #55`)

The following phrases or equivalent logic MUST NOT appear in consumer SKILL.md files:

- "Skip reading thesis X because graph says X isn't in the cluster"
- "Only process tickers in the same cluster as TICKER"
- "Use `log_tail:` as substitute for reading the Log section"
- "Trust graph `cross-thesis:` as complete list"
- "If graph doesn't list peer Y, skip peer Y"

These turn primer into filter. Research quality depends on content reads; the graph accelerates orientation, never replaces reading.

## Confirmation-bias mitigations (skill-specific — surfaced here for discoverability)

- **`/stress-test`**: if cluster peers show parallel stress signals, explicitly surface idiosyncratic failure modes FIRST in report, cluster-wide second. Counter the primer's natural bias toward cluster framing.
- **`/deepen`** (comparative sections only): peer-dominance mitigation — if target section is sparse and peer sections are rich, surface "what's in peer X that's missing from target, and why does the target's positioning differ?" rather than importing peer content. Divergence is analytically valuable.
- **`/brief`**: Related Developments section is footnote-only, appended after the core 6-section structure. Pitch / What Kills It / Conviction must reflect target's own thesis evidence without primer influence.

## Schema dependencies

This contract depends on `_graph.md` frontmatter + sections:
- Frontmatter: `last_graph_write:` (ISO 8601, T6.10+)
- Sections: `## Thesis Adjacency Index` (with T7.3 `status:` + `log_tail:` per-entry fields), `## Reverse Index: Macro → Theses`, `## Reverse Index: Sector → Theses`, `## Cross-Thesis Clusters`, `## Orphan Research Notes`

Schema changes to `_graph.md` cascade to this contract; consumer skills reference the contract, not the graph directly, so schema-change blast radius is localized to `/graph` + this file + `/lint`.
