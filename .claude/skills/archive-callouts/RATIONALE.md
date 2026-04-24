---
type: skill-rationale
for_skill: /archive-callouts
purpose: Design rationale for `/archive-callouts`. SKILL.md contains operational rules; this file explains why they're shaped this way. References in SKILL.md take the form `§N.M` and map to sections below.
last_reviewed: 2026-04-24
---

# /archive-callouts — Design Rationale

## §1. Why in-note archive, not external `_Archive/Callouts/*.md`

- **Co-located audit trail** matches the original "why callouts" design goal (visual provenance at the decision point). The callout was added inside the Bull Case section; its archive belongs inside the same thesis file, one section below, not in a separate archive directory.
- **Rollback uses standard thesis snapshot** — no separate archive-file restoration path. `/rollback` already recognizes `snapshot_trigger: callout-sweep`; adding a sibling archive-file restore path would duplicate the cascade mechanism for no quality benefit.
- **`/rename` already rewrites wikilinks across thesis body** — no additional consumer needed. External archive files would require a new `/rename` code path to track their provenance.
- **Zero file sprawl** — a 40-thesis vault avoids accumulating 40 separate archive files, each with its own frontmatter, date discipline, and lifecycle.

## §2. Why descending sort (newest first)

- **Latest sweep visible immediately on scroll**; most-recent context dominates. A user landing on `## Legacy Callouts` during a `/deepen` run cares about recently-swept entries (closest to current analysis context), not entries from 2 years ago.
- **Aligns with `## Log` convention** where newest activity is what readers typically scan. (`## Log` itself is append-only bottom-up because it's immutable; `## Legacy Callouts` is bulk-rewritten each sweep, so top-newest is the reading-order choice without conflicting with Log's append discipline.)

## §3. Why 180-day default threshold

- User-chosen after weighing:
  - **90d** — too aggressive; sweeps still-contextual exchanges that the user may still be referencing in adjacent research.
  - **365d** — barely removes clutter; addressed callouts pile up across multiple quarters before any hygiene applies.
- **Aligns with `/clean` default snapshot retention (180d)** — consistent hygiene cadence across skills. Users who run one periodic cleanup typically run both; matching thresholds avoids surprising mixed-age artifacts.

## §4. Why `warning` label for `[!error]` callout type

- Matches hotkey template filename `user-warning.md` (Templater slot label). The filename is what users see when they customize the hotkey; the Obsidian internal callout type (`[!error]`) is an implementation detail.
- Human-facing vocabulary is more natural than `error` (which implies Claude was wrong, not just disputed). "warning" captures the user's intent in most cases — "I'm flagging this as contestable" rather than "this is incorrect."
- Consistent with how users describe the hotkey in practice ("hit warning on this bullet" rather than "hit error on this bullet").
