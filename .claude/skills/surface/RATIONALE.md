---
type: skill-rationale
for_skill: /surface
purpose: Design rationale for `/surface`. SKILL.md contains operational rules; this file explains why they're shaped this way. References in SKILL.md take the form `§N.M` and map to sections below.
last_reviewed: 2026-04-24
---

# /surface — Design Rationale

## §1. Why stop rather than best-effort continue on missing-thesis scope (ticker-scoped and sector-scoped modes)

Scoped modes depend on complete scope coverage. A best-effort continuation would:

- **Read `Theses/TICKER - Name.md` and fail silently**, skipping that thesis from Phase 1–3 analysis. Portfolio-level output (research velocity ranking, attention allocation, decay alerts) is scoped metadata — a missing thesis silently under-reports these metrics without flagging the gap. The user sees a sector review that looks complete but quietly omitted one of the positions.

- **Produce a surface-scan research note that under-reports the sector** (missing the archived thesis's historical context, even though its adjacency influenced the sector's dynamics until closure). Downstream readers of the research note cannot distinguish "archived thesis correctly omitted" from "thesis silently skipped due to stale graph."

- **Write `propagated_to: []` on the research note**, which blocks `/sync` from auto-healing by retry. The `[]` terminal-skip marker is correct for a complete scope; on an incomplete scope it permanently hides the missing-coverage fact from later runs.

The fail-fast path forces `/graph last` explicitly — cost is one extra command; benefit is correct scope coverage on retry. A user who knows scope is incomplete can make an informed choice (run `/graph last` first, or drop to unscoped `/surface` which correctly handles archived theses via `Theses/*.md` glob).

## §2. Why `/surface` does not auto-run `/graph last`

`/surface` is an analytical read-only skill that writes a synthesis research note and `_hot.md`. It does not write `_graph.md`. Auto-running `/graph last` would violate the metadata-ownership boundary (only `/graph` and `/rename` write `_graph.md`).

User explicitly invokes `/graph last` — one extra command is the correct cost for ownership clarity. The alternative (every analytical skill auto-running `/graph last` at the end) creates cross-skill contention on `_graph.md` writes and makes the write pathway implicit rather than explicit.

`/lint #38` (`.graph_invalidations` aging) catches the chronic case where users forget to run `/graph last` — the user gets a clear diagnostic instead of a silent stale-graph failure mode.
