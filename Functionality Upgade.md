---
date: 2026-04-19
tags: [meta, architecture, proposal-evaluation]
status: draft
---

# Functionality Upgrade — Metadata/Graph Decoupling Proposal

## Executive Recommendation

**Strongly feasible. Recommend phased adoption.**

Cross-skill contention over `_graph.md`, `_hot.md`, `.last_sync`, and the Session Chain protocol is the root cause of the bug-loop, not symptom of it. Concentrating metadata ownership in `/graph` collapses ~40% of total skill surface area and eliminates 6 of the 7 categories of edge case the user is fighting. The change is large but mechanically straightforward: each skill loses a self-contained section, and `/graph` gains two new modes.

---

## Current Architecture — Quantifying the Metadata Burden

### Skill surface area (3,655 lines total across 17 SKILL.md + 2 shared contracts)

| Skill | Lines | Estimated metadata-related lines | % of file |
|---|---|---|---|
| `/sync` | 605 | ~380 | 63% |
| `/status` | 300 | ~140 | 47% |
| `/prune` | 291 | ~120 | 41% |
| `/lint` | 212 | ~95 (graph + contract checks) | 45% |
| `/rename` | 216 | ~110 | 51% |
| `/rollback` | 313 | ~130 | 42% |
| `/thesis` | 125 | ~45 | 36% |
| `/compare` | 154 | ~50 | 32% |
| `/graph` | 148 | 148 | 100% |
| `/deepen`, `/scenario`, `/stress-test`, `/surface`, `/brief` | ~600 combined | ~150 | 25% |
| `_shared/log-prefixes.md` | 303 | 303 (entire file is a contract) | 100% |
| **Total** | **3,267 (named skills)** | **~1,670** | **~51%** |

**Roughly half the skill code exists to maintain, validate, or coordinate metadata between skills — not to do research.**

### Cross-cutting concerns embedded in every research skill

1. **`_graph.md` incremental updates** — `/sync` Steps 7 Rules 1-10 (~110 lines), plus a graph block in `/thesis`, `/compare`, `/status`, `/scenario`, `/deepen`, `/stress-test`, `/surface`, `/brief`, `/prune`, `/rename`. **10 producers writing to one file.**
2. **Session Chain protocol** — defined in CLAUDE.md (~80 lines), referenced in every research skill with chain-aware blocks (~10-25 lines each). Created specifically to prevent redundant graph writes — pure overhead from current architecture.
3. **Graph Debt accumulation/resolution** — distributed across `/sync`, `/graph`, `/sync all`, plus all chain-participant skills. ~60 lines in `/sync` alone.
4. **`propagated_to:` verification + 4-bucket partial-repair classification** — `/sync` Step 1 (~70 lines) handles the case where producer skills (`/stress-test`, `/scenario`, `/compare`, `/deepen`) crashed between Log append and Related Research append.
5. **Closed-status gates** — duplicated across `/sync` Outcome B, Fallback 1, Fallback 2, Missing-file-resilience, Rule 9, Rule 10. Five separate gates for the same failed-archive-move corruption vector.
6. **Watermark dual-timing** — `.last_sync` (sync watermark) vs `_graph.md` `date:` (graph watermark) require coordination logic in Steps 7 and 8 of `/sync`.
7. **Reverse index consistency** — forward (`thesis → sector`) and reverse (`sector → thesis`) indexes drift; `/lint` check #23 catches the drift, `/graph` rebuilds them, `/sync` Rules 2/3 attempt online maintenance. Three skills, one consistency invariant.
8. **Log-prefix registry** — 303-line contract because 6 skills produce prefixes consumed by 2 skills (`/sync`, `/lint`). Drift detection + partial-write detection both depend on it.

### Edge-case sources directly attributable to this architecture

- Graph poisoning by `/sync all` (`date: 1970-01-01` sentinel)
- Stale chain preservation across session boundaries
- Partial-write repair across 4 verification buckets
- Reverse index drift (forward != reverse)
- Failed archive moves leaving `status: closed` in `Theses/`
- Reconciliation sweeps (Rule 8.i, 8.ii) for dedup-skipped notes
- Chain-deferred `/thesis` invisible to subsequent `/sync TICKER`
- Snapshot batch ID sharing across skills

**Each new edge case adds a guard, the guard interacts with another skill's guard, and the cycle continues.**

---

## Proposed Architecture — Interpreted

### Three-layer separation

| Layer | Owner | Writes to | Concern |
|---|---|---|---|
| **Content** | `/sync`, `/sync all`, `/compare`, `/thesis`, `/deepen`, `/scenario`, `/stress-test`, `/brief`, `/surface`, `/status`, `/prune`, `/rename`, `/rollback` | thesis bodies, sector notes, macro notes, research notes, `_hot.md` | Investment research |
| **Metadata** | `/graph` (three modes) | `_graph.md` only | Vault integrity |
| **Surfacing** | `/lint` | nothing (read-only) | Surfaces issues for manual triage |

### `/graph` modes (proposed)

| Mode | Trigger | Scope | Cost |
|---|---|---|---|
| `/graph last` | After every `/sync` (or chain-end) | Files with `mtime > _graph.md.date` | Cheap (typical: 3-15 files) |
| `/graph [N]` | User catch-up | Files with `mtime > today - N days` | Medium (covers gap periods) |
| `/graph` (no args) | Periodic full rebuild, or after `/sync all` | All vault files | Expensive (current behavior) |

### Workflow loop (proposed)

```
/ingest  →  /sync  →  /graph last
   |         |          |
   writes    propagates updates _graph.md
   research  insights   from recent file mtimes
```

Long-gap recovery: `/graph 7` reconciles a week of activity. Disaster recovery: `/graph` rebuilds from scratch.

---

## Side-by-Side Comparison

| Concern | Current Architecture | Proposed Architecture |
|---|---|---|
| **Graph writers** | 10 skills | 1 skill |
| **Graph write paths** | Incremental (per-skill) + full rebuild | Three explicit modes, all in `/graph` |
| **Session Chain protocol** | ~80 lines in CLAUDE.md + per-skill chain blocks | **Deleted** — no contention to coordinate |
| **Graph Debt mechanism** | Tracks chain-deferred writes | **Deleted** — no deferred writes exist |
| **`propagated_to:` verification** | 70 lines in `/sync` Step 1 | Stays only as content idempotency check (much simpler) |
| **Closed-status gates** | 5 sites in `/sync` | 1 site in `/graph last` (cheaper to recompute than to gate) |
| **Reverse index maintenance** | `/sync` online + `/graph` rebuild + `/lint` drift check | `/graph` rebuilds atomically every time |
| **Watermark** | `.last_sync` (sync) + `_graph.md` `date:` (graph) | Same two, but no coordination logic — independent clocks |
| **Failure isolation** | A failed `/sync` can corrupt graph mid-update | A failed `/sync` cannot touch graph |
| **Cognitive load per skill** | Must understand chain protocol, snapshot batches, drift contracts, graph schema | Each skill reviews in isolation against its own purpose |
| **`/lint` role** | Detects + recommends fix skill | Surfaces issues; user resolves manually with Claude queries |

### Estimated post-change line counts

| Skill | Now | After | Delta |
|---|---|---|---|
| `/sync` | 605 | ~250 | **-355** |
| `/status` | 300 | ~180 | -120 |
| `/prune` | 291 | ~190 | -100 |
| `/rename` | 216 | ~120 | -96 |
| `/rollback` | 313 | ~210 | -103 |
| `/thesis` | 125 | ~80 | -45 |
| `/compare` | 154 | ~110 | -44 |
| `/graph` | 148 | ~220 (three modes) | +72 |
| `/lint` | 212 | ~190 (drops some checks, adds gap-flag checks) | -22 |
| Other research skills (combined) | ~600 | ~450 | -150 |
| CLAUDE.md (Session Chain section) | ~80 | 0 | -80 |
| **Net reduction** | | | **~-1,043 lines** |

---

## Key Risks & Mitigations

### Risk 1: Eventual consistency on graph state

**Scenario**: User runs `/thesis NVDA`, then `/sync NVDA` immediately, without `/graph last` between them. `/sync NVDA` looks up NVDA in `_graph.md` adjacency index — not found.

**Current handling**: Outcome B reconstruction (~30 lines) reads the thesis file directly and reconstructs adjacency.

**Proposed handling**: `/sync TICKER` *always* uses the file-direct fallback (Outcome B becomes the only path, eliminating Outcome A entirely). The graph becomes purely an optimization for `/sync` (default mode) and `/lint`.

**Trade-off**: `/sync TICKER` always pays a small adjacency-rebuild cost on every run. Benefit: no need to keep graph synchronized between `/thesis` and the next `/sync`.

### Risk 2: Discipline of running `/graph last`

**Scenario**: User forgets `/graph last` after `/sync`. Graph drifts. Next `/sync` (default mode) misses propagation paths.

**Mitigations**:
- `/sync` final report: prominent reminder `→ Run /graph last to update vault dependency map`
- `/lint` check #18 (graph staleness >7 days = Important) already exists
- Optional: meta-skill `/research-cycle` runs `/ingest → /sync → /graph last` as one chain

### Risk 3: `/lint` becomes overloaded as the only safety net

**Scenario**: With no inline validation in research skills, broken YAML, malformed wikilinks, missing frontmatter only surface at `/lint` time.

**Mitigations**:
- `/graph last` validates wikilinks during reconciliation (it already extracts them) — surfaces broken-link errors at graph-write time, not weeks later at `/lint`
- Keep per-skill snapshot+post-edit verification (this is per-skill safety, not vault metadata)
- `/lint` already does this — the change is removing it from the *write path*, not from the *audit path*

### Risk 4: Drift detection in `/sync` depends on log-prefix contract

**Scenario**: User assumes log-prefix registry is also dropped in cleanup.

**Recommendation**: **Keep it.** Drift detection is content-propagation logic (qualitative — does recent thesis history show conviction deterioration?), not metadata. The 303-line registry stays as-is. The simplification is removing the *graph* contracts, not the *log-prefix* contracts.

### Risk 5: Snapshot system is misclassified as metadata

**Scenario**: User assumes snapshots also move to `/graph`.

**Recommendation**: **Snapshots stay per-skill.** They are per-edit safety (allow rollback), not vault-wide integrity (allow consistent traversal). Snapshot batch IDs and `snapshot_trigger:` frontmatter remain unchanged.

---

## Recommended Modifications to the Proposal

| User's proposal | Recommendation |
|---|---|
| Strip metadata from research skills | ✅ Adopt for `_graph.md` only. Keep snapshots, drift detection, `_hot.md` updates in research skills. |
| `/graph last` after every `/sync` | ✅ Adopt. Define watermark as `_graph.md` `date:` frontmatter. |
| `/graph [days]` for catch-up | ✅ Adopt. Define as "scan files with mtime > today - N days, reconcile incrementally". |
| Drop graph instructions from research skills | ✅ Adopt for incremental graph updates. Keep wikilink-add behavior in skills (this is content). |
| `/lint` surfaces issues for manual triage | ✅ Adopt. Add a new check category: `🔧 Auto-fixable by /graph` vs `👤 Requires manual review`. |
| (implicit) Delete Session Chain protocol | ✅ Confirm — no contention to coordinate after change. |
| (not in proposal) Drop log-prefix registry | ❌ **Keep** — drift detection is content logic, not metadata. |
| (not in proposal) Drop snapshots | ❌ **Keep** — per-edit safety, not metadata. |
| (not in proposal) Move `_hot.md` to `/graph` | ❌ **Keep distributed** — context cache, simpler without chain protocol. |
| (improve) `/prune` archives stale research | ✅ Adopt as separate workstream — orthogonal to graph cleanup, addresses context-window burden. |

---

## Migration Path (Phased)

**Phase 1 — Additive (low risk)**
- Implement `/graph last` and `/graph [N]` modes alongside existing full rebuild
- Add `→ Run /graph last` reminder to `/sync` final report
- Update `/lint` check #18 thresholds (if graph last < 24h, treat as fresh)

**Phase 2 — Subtractive (one skill at a time)**
- Remove graph block from `/thesis` (smallest blast radius)
- Verify `/graph last` reconciles new theses correctly
- Remove graph block from `/compare`, `/scenario`, `/deepen`, `/stress-test`, `/surface`, `/brief` one at a time
- Remove chain-aware blocks from each as graph blocks come out

**Phase 3 — `/sync` simplification**
- Remove Step 7 Rules 1-10 (incremental graph update)
- Remove Step 7.5 graph-date reset logic
- Simplify Step 0 — graph becomes optional optimization, not a fallback trigger
- Remove Step 1 propagated-to verification's 4-bucket classification (replace with simple "have we propagated this note to this thesis already?" check)
- Eliminate Outcome A (graph entry exists) → always use Outcome B (read file directly)

**Phase 4 — Contract cleanup**
- Delete Session Chain protocol from CLAUDE.md
- Delete Graph Debt section
- Update `/rollback`, `/rename`, `/status`, `/prune` to remove chain-aware blocks
- Keep `_shared/log-prefixes.md` and `_shared/sector-resolution.md` — both are content contracts

**Phase 5 — Lint augmentation**
- Add `/lint` checks for issues that previously self-healed inline:
  - Research note with `ticker:` matching no thesis (was Step 1 Fallback 1 path)
  - Thesis file in `Theses/` with `status: closed` (was 5 different gates)
  - Any unresolved wikilinks (was post-edit verification)
- Group these as `### Manual Triage Required` so user knows what `/graph` cannot fix

---

## What This Does NOT Solve

- **Snapshot accumulation** — `/clean` already exists, orthogonal concern
- **Research note bloat** — user's separate proposal to have `/prune` archive stale research is the right answer
- **Mid-edit failures** — per-skill snapshots already address this, no change
- **Context window overflow** — needs separate triage; partially addressed by removing inline metadata from skill prompts (each skill becomes shorter)

---

## Verdict

**Adopt.** The proposal correctly identifies that metadata management bleeding into research skills is the root cause of the bug-loop. Concentrating ownership in `/graph` (with three modes) eliminates ~1,000 lines of contention logic and makes each skill independently reviewable.

The two refinements worth confirming with the user before implementation:
1. **Snapshots, drift detection, and `_hot.md` stay in research skills** — they are not graph metadata; conflating them muddies the cleanup
2. **`/sync TICKER` always uses file-direct fallback** — eliminates the need to keep graph synchronized between `/thesis` and `/sync`

Recommend a 5-phase rollout starting with additive `/graph` modes (Phase 1) before any subtraction. Phase 1 alone is reversible and provides the workflow primitive needed to validate the rest.
