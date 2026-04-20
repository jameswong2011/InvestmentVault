---
type: skill-rationale
skill: /scenario
purpose: Design rationale for /scenario — reverse mode archive-aware iteration, classification approval gate, atomicity contract, idempotency via Log state.
last_reviewed: 2026-04-20
---

# /scenario Design Rationale

> SKILL.md contains operational rules. This file explains the Tier 3 archive protection, the 5.1 classification approval gate, the `propagated_to:` atomicity contract, and reverse-mode idempotency via Log-state dedup.

---

## §1 Reverse mode archive-aware iteration (6.2 fix)

### §1.1 Why archived theses are skipped

CLAUDE.md Change Safety Rule #2 (Tier 3) classifies `_Archive/` content as archival record — never modified without explicit instruction. A thesis that received a `Scenario` Log entry and was subsequently closed/archived has its Log preserved as historical audit trail.

Appending a `Scenario REVERSED` entry to the archived thesis would violate Tier 3 by silently editing archive content. The skill instead:
1. Records the skip in `archive_skipped_theses` with full context
2. Surfaces the skip in the R6 report
3. Documents every archive-skipped ticker in the scenario research note body under `## Reversal Notes` with rationale: "Thesis archived on [archive_date] after scenario propagation. Scenario Log entry preserved in archive as historical record. Reversal not applied to respect Tier 3 archive protection."

The scenario research note body carries the complete audit — any future review finds both the live-ticker reversal Log entries AND the documented archive-skipped tickers. No silent gaps.

### §1.2 Why the body-documentation path matters

Without it, a user reading the scenario research note would see only `propagated_to: [A, B, C, D]` and find REVERSED entries on only A and B — C and D would appear to be missing reversals when they were actually deliberately skipped (archived since the scenario). The `## Reversal Notes` section closes that gap.

---

## §2 Reverse mode idempotency via Log state

### §2.1 Why filter on existing REVERSED entries

Re-running `/scenario reverse [same scenario]` (e.g., to retry partial failures from a prior run, or because the user forgot they already reversed) would otherwise append a SECOND REVERSED entry to already-reversed theses.

The original purpose of REVERSED is corrective signal preservation; duplicates inflate Log noise without semantic meaning. The R2 classifier filter (`match_scenario_entry == true AND match_reversed_entry == true → exclude`) makes the operation idempotent — re-running on a fully-reversed scenario is a no-op for already-handled theses; only theses that failed in the prior run (no REVERSED entry yet) are retried.

### §2.2 No retry marker needed

Unlike `/sync`'s producer-skill atomicity (which uses `propagated_to:` to signal "already done"), reverse mode's idempotency is encoded in the Log itself — the existence of `Scenario REVERSED [[Research/...scenario]]` entry on a thesis is the dedup signal that R2's classifier reads on subsequent runs.

A partial failure leaves the failed theses without a REVERSED entry. The next `/scenario reverse [same scenario]` invocation re-classifies them as needing reversal and retries. No sidecar marker needed.

### §2.3 Re-run pattern for partial failures

If R6 reports `reverse_failed: [TICKER1 (reason), TICKER2 (reason)]`, the user runs `/scenario reverse [same scenario]` again:
- R2 classifies TICKER1/TICKER2 as still-needing-reversal (Log has Scenario but not REVERSED)
- R2 classifies all already-succeeded theses as already-reversed (excluded from this run)
- R4 retries only the still-failing targets

Idempotent re-runs converge to fully-reversed state without duplicate REVERSED entries on already-handled theses.

### §2.4 Excluded-from-reverse cases

Three classifications produce "skip this ticker":
- `match_scenario_entry == false` — thesis was body-wikilinked but never received producer Log entry. Nothing to reverse. (Happens when a minor-impact thesis was in Related Notes but excluded from Major set.)
- `match_scenario_entry == true AND match_reversed_entry == true` — already reversed.
- Location `archive` — Tier 3 protection (§1.1).

---

## §3 Classification approval gate (5.1 fix — Phase 6.1.5)

### §3.1 Why explicit approval

Phase 3 classification (Major / Minor / Neutral) is LLM-inferred from transmission-channel analysis. Two failure modes exist:
- **False-negative Major**: thesis should be in Major set but LLM rated Minor → silent miss. Thesis Log misses the propagation.
- **False-positive Major**: thesis rated Major but transmission channel is weak/absent → Log clutter, only reversible via `/scenario reverse`.

Pre-6.1.5 behavior: LLM classification → Log appends → user sees final report only after propagation landed. Mistakes required `/scenario reverse` to clean up.

Post-6.1.5: user reviews classification, can promote/demote tickers, only approves → then propagation lands.

### §3.2 Why the gate runs BEFORE the research note write

Phase ordering: **6.1.5 (approval) → 6.1 (research note write) → 6.2 (Log appends) → 6.3 (propagated_to update)**.

If the user cancels at 6.1.5, no half-written research note lingers. The scenario can be re-run cleanly with different parameters. Prior ordering (6.1 before 6.1.5) would leave orphan research notes on cancellation.

### §3.3 Why this is safe from approval-fatigue

`/scenario` is Tier 3 by nature (propagates to many theses at once). Adding one more explicit gate matches the existing `/prune` approval pattern — users expect `/scenario` to present its plan before executing, not auto-propagate based on LLM classification alone.

The gate also serves as an LLM-error mitigation — if Phase 3's classification is systematically off (e.g., missing a transmission channel), the user catches it once before 20 theses get incorrectly propagated.

### §3.4 Promote/demote mechanics

User options beyond approve/cancel:
- **(b) Promote**: user supplies tickers to upgrade. Merge into Major set. For each promoted ticker, user provides one-line rationale (required) that replaces the auto-generated Phase 3 rationale in that ticker's Log entry. Re-present updated classification for final approval.
- **(c) Demote**: user supplies tickers to downgrade. Remove from Major set; add to Minor. Re-present for final approval.

The rationale requirement on promotion ensures the Log entry remains auditable — "user manually promoted" is documented via the supplied text.

---

## §4 `propagated_to:` atomicity contract (Phase 6.3)

### §4.1 Why all-or-nothing

A partial `propagated_to:` would claim some failed-target tickers as propagated when their Log entries never landed — creating a permanent audit gap that future `/sync` runs silently skip because the dedup hint says "already done."

All-or-nothing:
- **All appends succeeded** → write `propagated_to: [TICKER1, TICKER2, ...]`. `/sync` Case 2b skips these as already propagated.
- **One or more failed** → do NOT write `propagated_to:` at all. Next `/sync` (default mode) detects each Major-impact thesis via file-direct fallback (research note body wikilinks Major theses under "Related Notes") and re-attempts via strict calendar-day idempotency check.

### §4.2 Trade-off: minor /sync re-work vs guaranteed consistency

All-or-nothing means `/sync` re-evaluates succeeded targets on retry (Case 2a wikilink-match scan). This is fine — the per-thesis idempotency check finds the existing Log entry and skips, producing no duplicate Log entry.

The cost is minor `/sync` re-work; the benefit is guaranteed eventual consistency (no silent audit gaps).

### §4.3 Why /sync's retry path actually works

`/sync`'s file-direct fallback resolves Major-impact theses via the research note's body wikilinks (every Major ticker is in "Related Notes" by Phase 6.1 construction). Per-thesis idempotency via wikilink-presence in `## Log` handles the dedup — succeeded targets already have today-dated Log entries; `/sync` Case 2a "Log-history backfill" finds them and skips.

Only failed-targets (no Log entry yet) trigger the retry path → Log entry lands → `propagated_to:` updated on the research note via `/sync`'s Case 2a backfill-update mechanism.

---

## §5 Phase ordering hygiene

### §5.1 Forward mode phase chain

**1 → 2 → 3 → 4 → 5 → 6.1.5 (approval) → 6.1 (research note) → 6.2 (Log appends) → 6.3 (propagated_to) → _hot.md → 7 (report)**

Each transition is a natural checkpoint:
- 1-5: read-only analysis (no vault changes possible)
- 6.1.5: first user gate (cancel-safe, no state written)
- 6.1: research note written (but no cross-file propagation yet)
- 6.2: cross-file Log appends (per-ticker failures tracked)
- 6.3: atomicity decision (frontmatter update based on 6.2 outcomes)
- _hot.md: session cache (failure here doesn't block primary work)
- 7: report (surfaces failures + retry instructions)

### §5.2 Reverse mode phase chain

**0 (pre-flight) → R1 (locate) → R2 (classify archive-aware) → R3 (confirm) → R4 (live Log appends) → R4.5 (document archive-skips in note body) → R5 (_hot.md) → R6 (report)**

Separation of R4 (live theses only) from R4.5 (archived ticker body documentation) enforces Tier 3 — archived theses never receive Log appends; they only appear in the scenario research note body.

---

## §6 Two-pass triage (Phase 2)

### §6.1 Why lightweight scan first

Reading all ~40+ thesis notes in full would exceed context limits. Most transmission-channel assessments can be made from Summary + frontmatter alone — exposure to rate changes, supply chain, commodity inputs is typically signaled in the Summary section.

Pass 1 reads ~200 words per thesis (frontmatter + Summary). Pass 2 deep-reads only High/Low exposure theses.

### §6.2 Three exposure tiers

- **High exposure**: direct transmission channel → read full thesis + sector note.
- **Low exposure**: indirect or second-order only → read Summary + Risks + Bull/Bear Case (skip Business Model, Industry Context, Key Metrics).
- **No exposure**: no plausible transmission → do NOT read further. Carry summary forward; mark Neutral in impact matrix.

Reduces deep-read set from ~58 files to 15-20.

### §6.3 Sector notes read on-demand

Read sector notes ONLY for sectors with at least one High-exposure thesis. Unaffected sectors skipped entirely. This couples sector-note reads to actionable propagation targets rather than reading every sector note defensively.

---

## §7 Rename-marker vault-wide hard block (Phase 0.2)

Same rationale as `/prune` Phase 0.0.2: scenario propagation writes Log entries to many theses; one mid-rename ticker in the affected set would have its Log entry keyed to the NEW name while some inbound references remain under the OLD name.

All-or-nothing block — cannot safely skip individual tickers mid-rename because the impact matrix and the `propagated_to:` atomicity rule both depend on a closed set of affected tickers decided at Phase 3.

---

## §8 Why scenario research notes are preserved, never deleted

Reverse mode explicitly does NOT delete the scenario research note. Rationale:
- The note is a historical record of the analysis performed — its Impact Matrix and Second-Order Effects sections are useful context even after the scenario is "reversed"
- Deleting would break `_graph.md` adjacency (research note wikilinks from Log entries would become broken links)
- Future scenarios that repeat similar transmission patterns benefit from comparison against the prior analysis

CLAUDE.md Tier 2 rule "research notes are immutable source records" applies — reverse mode signals "no longer applies" without erasing the original analysis.
