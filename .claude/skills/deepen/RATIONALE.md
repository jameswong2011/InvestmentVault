---
type: skill-rationale
for_skill: /deepen
purpose: Design rationale for `/deepen`. SKILL.md contains operational rules; this file explains why they're shaped this way. References in SKILL.md take the form `§N.M` and map to sections below.
last_reviewed: 2026-04-24
---

# /deepen — Design Rationale

## §1. Why the deepen manifest exists (M3 — Phase 4.5)

`/deepen` is a multi-file transaction — it edits the thesis (Phase 5) AND creates a research note (Phase 6) AND updates `_hot.md` (Phase 7). Prior spec had only the thesis snapshot as a recovery anchor.

A crash mid-Phase-6 would leave:
- The thesis with its target section rewritten AND a provisional `Deepening` Log entry (Phase 5a),
- No research note (Phase 6 never completed),
- No manifest trail for `/rollback` cascade detection to find the batch.

The manifest + skeleton-before-flip pattern (§3 invariant) provides:
- **Crash detection via `/lint #50`** — surfaces `in-progress` manifests after a crash.
- **Batch-level cascade via `/rollback` Step 2.5g** — lets the user restore the thesis from the pre-deepen snapshot AND (optionally) delete the supporting research note in one transaction.

Without the manifest, the user has to manually inspect the Log for stuck `Deepening` entries and decide per-file what to restore.

## §2. Batch ID format: why TICKER is embedded

`deepen-TICKER-YYYY-MM-DD-HHMMSS` — TICKER embedded to prevent collisions between concurrent `/deepen` runs on different tickers that hit the same HHMMSS. Matches `/stress-test` pattern (§3 of stress-test RATIONALE).

Per-ticker locks prevent literal file overwrites, but batch IDs without TICKER would alias two concurrent runs under the same manifest identifier — `/rollback` Step 2.5g would present cross-ticker cascade options.

## §3. Phase 5c verify-and-retry — why a provisional-Log audit trail

Phase 5a appends a provisional `Deepening [Section Name] — in progress` Log entry BEFORE rewriting the section. This ensures an audit trail exists even if the rewrite fails mid-Edit.

If the rewrite succeeds but the finalization Edit at 5c fails silently (Edit reports success but the replacement didn't land — observed in practice on rare anchor-mismatch edge cases), the provisional entry stays in the Log. `/lint #28` catches this via the `"Deepening"` prefix presence check.

The retry-and-append fallback handles the case where Edit genuinely cannot match the provisional text for replacement:
1. First retry uses expanded context (date header + provisional line) to ensure uniqueness.
2. Second failure appends a `↳ CORRECTION: Deepened ...` entry below the stuck provisional entry.

This preserves the append-only Log contract (Tier 2 — never edit or delete existing entries) while ensuring the audit trail is always complete. `/sync` drift detection recognizes both `"Deepened"` and `"↳ CORRECTION: Deepened"` prefixes; `/lint #28` downgrades to Nice to Have when both entries co-exist (the corrective audit trail is complete).

## §4. Drift coupling — why these prefixes must not change

`/sync` Step 3e excludes entries starting with `"Deepened"` within 7 days of a stress test from drift detection. The rationale: deepening gap-fills evidence that would otherwise look like drift (more entries, mostly negative sentiment because deepening often reveals weaknesses). Without exclusion, every `/deepen` following a `/stress-test` would fire a false drift warning.

Registry entries: `.claude/skills/_shared/log-prefixes.md` §2 (Deepening provisional), §3 (Deepened), §4 (↳ CORRECTION: Deepened). Changing any of these three prefixes without updating the registry and `/sync` breaks drift detection silently. `/lint #29` verifies registry/producer/consumer alignment.

## §5. Phase 2.5 peer-section cross-read — anti-pattern guards

**Orientation not filter** (contract §Anti-patterns): do NOT substitute peer content for target-specific depth. The deepen's Phase 5 rewrite must be target-thesis-driven — peer content shapes the gap analysis, not the content itself.

**Peer-dominance mitigation** (contract §Confirmation-bias mitigations): if the target section is sparse and peer sections are rich, Phase 5 must explicitly surface "what's in peer X that's missing from target, and why does the target's positioning differ?" rather than importing peer content. Divergence is analytically valuable.

These two guards matter because the primer's natural bias is toward cluster framing ("peers all say X, so target should too"). For Bull Case / Bear Case / Industry Context / Non-consensus Insights specifically, the target's DIVERGENCE from peers is often the thesis itself — forcing it into alignment with peers destroys the non-consensus edge that justifies the position.
