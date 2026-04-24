---
type: skill-rationale
for_skill: /stress-test
purpose: Design rationale for `/stress-test`. SKILL.md contains operational rules; this file explains why they're shaped this way. References in SKILL.md take the form `§N.M` and map to sections below.
last_reviewed: 2026-04-24
---

# /stress-test — Design Rationale

## §1. Why never partial `propagated_to:` (Phase 4.4 atomicity)

Matches `/scenario` Phase 6.3 rationale — a partial `propagated_to:` would create a permanent audit gap that future `/sync` runs silently skip because the dedup hint says "already done."

For single-ticker `/stress-test`, the partial case is binary (either present-with-TICKER or absent), but the rule is the same: **omit on failure, write only on success**. If we wrote `propagated_to: [TICKER]` speculatively at Phase 4.1 and the Log append at Phase 4.2 failed, the next `/sync` (Case 2b) would see `propagated_to:` listing TICKER, skip the retry, and never fix the missing Log entry. The thesis would stay out of sync forever without any surfaced error.

Omitting the field on failure keeps the file in a state the next `/sync` can repair — the file-direct fallback (research note's `ticker: TICKER` frontmatter) resolves to the thesis, the per-thesis idempotency check sees no today-dated entry, and the Log append retries.

## §2. Why the manifest exists (Phase 4.6)

`/stress-test` writes a Log entry to the tested thesis (**Tier B — no pre-edit snapshot** because the Log is append-only) and a research note. If the user later decides the stress test was invalid (wrong input, stale vault state, experimental run), there's no `/rollback` cascade path to restore the pre-stress-test thesis state. Manual strikethrough of the Log entry is the only remedy.

The manifest provides `/rollback` cascade-detection with the Log entry text so the user can choose per-entry annotation — same pattern as `/sync` Tier B sidecar and `/compare` manifest. Without the manifest, `/rollback` Step 2.5d has no way to surface the Log entry for review.

## §3. Batch ID format: why TICKER is embedded (C4 fix)

Ticker-scoped skills include TICKER in the batch ID to prevent collisions when two concurrent `/stress-test` runs on different tickers hit the same HHMMSS.

- **Prior format** `stress-test-YYYY-MM-DD-HHMMSS` could collide between simultaneous `/stress-test NVDA` and `/stress-test AMAT` runs that both generated the same timestamp. Per-ticker locks prevent the runs from literally overwriting each other's files, but the batch IDs would be identical — `/rollback` would match both runs under the same batch identifier and present mixed cascade options.
- **Current format** `stress-test-NVDA-YYYY-MM-DD-HHMMSS` and `stress-test-AMAT-YYYY-MM-DD-HHMMSS` are distinct. `/rollback` Step 2.5d cascade detection matches by the `stress-test-` prefix AND the `ticker:` frontmatter field of the manifest.

## §4. Recovery guidance — included in manifest body

The manifest body includes a `## Recovery guidance` block with the exact `/rollback` invocation and the three per-entry annotation options (leave as historical, strikethrough with reversal date, manually delete). Having the recovery text inline in the manifest means the user discovers it exactly when they need it — during `/rollback` inspection — instead of having to remember which SKILL.md section describes the flow.

The research note at `Research/YYYY-MM-DD - TICKER - Stress Test.md` is NOT deleted by rollback — it persists as historical record (same rule as scenario research notes). The rollback scope is the Log entry annotation only.
