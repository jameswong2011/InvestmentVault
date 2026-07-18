# Conviction-Trigger Touch Contract

Consumed by: `/numbers` (Step 5b — **primary/concrete consumer**), `/transcript` (Step 6.3 — **origin pattern**), `/sync` (Step 3e), `/deepen` (Phase 3), `/ingest` (Step 1 identifier)
Owned by: **shared** — any skill that produces a new datapoint about a thesis may run the touch check. Not skill-exclusive.
Governs: the mechanical comparison of NEW evidence/metrics against a thesis's own pre-registered `## Conviction Triggers`, and the mandatory `Trigger touch:` report line that results.

## Why this exists

A thesis's `## Conviction Triggers` are pre-registered falsifiable if/then statements (`→ HIGH if …`, `→ LOW if …`, `→ CLOSE if …`). They are the vault's falsification machinery — but they only work if something checks new data against them. Before this contract, `/transcript` (Step 6.3) was the only skill that did: it flags a trigger as "touched" when a transcript provides evidence on the trigger's named variable. Every other skill that produces new datapoints — `/numbers` computing a fresh gross-margin delta, `/sync` propagating a new Bear-case datapoint, `/deepen` researching a section — had the exact numbers in hand and never diffed them against the triggers. A trigger that has quietly fired sits unnoticed until the next full human review.

This contract generalises Step 6.3 into a reusable check so any producer skill closes the loop.

## The check (mechanical — never a judgement call to auto-execute)

Given a target thesis and one or more NEW datapoints the skill just produced:

1. **Parse the triggers.** Read `## Conviction Triggers`. Extract each `→ HIGH if` / `→ LOW if` / `→ CLOSE if` statement verbatim. A single bullet may carry a multi-condition trigger (`… AND … AND …`) — keep the whole condition together; a trigger fires only when ALL its conjuncts hold, touches when any single conjunct is met.
2. **Extract each trigger's testable handle.** For each trigger, identify:
   - **Numeric threshold** — a number + comparator (`GM < 42%`, `revenue growth below 20%`, `net debt/EBITDA > 2.0x`, `share ≥ 60%`). This is the machine-checkable case `/numbers` owns.
   - **Named observable** — a dated/named event with a binary outcome (`Microsoft Maia 2 commercial launch`, `loses the Apple N2 anchor`, `EUV competitor qualifies`). This is the case `/transcript`, `/sync`, `/deepen`, `/ingest` own — evidence bears on it without a number.
3. **Diff the new datapoint against each trigger handle.**
   - **Numeric** (`/numbers`): compare the refreshed value to the threshold. Classify: `CROSSED` (value is now on the trigger side of the threshold), `approaching` (moved ≥ halfway toward the threshold from the old value this run, not yet crossed), or `no-touch`.
   - **Observable** (evidence skills): does the new evidence provide a datapoint on the trigger's named variable? If yes → `touched`, with a direction (toward HIGH / LOW / CLOSE). Whether it *fires* the trigger is a judgement the skill states, not auto-resolves.
4. **Emit the report line (MANDATORY when any trigger is touched/crossed).** Never silently swallow a touch — the whole point is visibility.

## Report line format

```
Trigger touch: [TICKER] → "[verbatim trigger, e.g. → LOW if GM < 42%]" — [handle] now [value] ([CROSSED | approaching | evidence-touched, dir=LOW]). [pointer to the datapoint]. Consider /status.
```

Examples:
- `/numbers`: `Trigger touch: LRCX → "→ LOW if gross margin < 44%" — GM refreshed 47.1%→43.6% (CROSSED). Consider /status LRCX conviction high→medium.`
- `/transcript`: `Trigger touch: NVDA → "→ LOW if hyperscaler capex guides flat 2 consecutive Qs" — Q1 call: 1st flat-guide quarter (approaching, dir=LOW). One more print confirms.`

## Consumer responsibilities

- **`/numbers` (Step 5b — primary):** after Step 5 computes deltas, diff every refreshed value against the thesis's own numeric triggers. `numbers_compute.py` already holds `new_value_numeric` + `old_value_numeric`; the threshold parse is the only new work. A `CROSSED` result is surfaced in the Step 12 report AND written as an open-findings entry per `_shared/followups-contract.md`. **Flag-only** — never edit `conviction:` (Design constraint #8 territory: this is a conviction decision, Tier-3, human-gated).
- **`/transcript` (Step 6.3 — origin):** already compliant. Its "touched trigger with direction" output IS this contract; this file documents the shared pattern it seeded. No behavioural change — re-pointed here for discoverability.
- **`/sync` (Step 3e):** sync's existing trigger-hit detection is this check applied to propagated research. When a propagated datapoint touches a trigger, emit the line and (if actionable) an open-findings entry. Do not conflate with drift detection (Step 3e's 3/5 Log-sentiment window) — a trigger touch is a single-datapoint event, drift is an aggregate.
- **`/deepen` (Phase 3):** when section research surfaces a datapoint bearing on a trigger, emit the line in the Phase 8 report. A `--sync-metrics` run that moves a numeric value across a threshold follows the `/numbers` numeric path.
- **`/ingest` (Step 1 identifier):** ingest never edits theses. It may NOTE in the research note's `## Thesis Delta` that a datapoint touches a named trigger, and surface it for the subsequent `/sync` to action — mirroring how ingest identifies mental-model triggers for `/sync` to write.

## Anti-patterns

- **Auto-executing `/status`.** A trigger touch is a flag, never an action. Conviction/status changes are Tier-3 (CLAUDE.md) — human-confirmed. The check surfaces; the user decides.
- **Treating "approaching" as "fired."** Approaching is a watch signal. Only a crossed numeric threshold or a satisfied observable is a fire, and even a fire only *suggests* `/status`.
- **Firing on a big-but-explained delta.** Same discipline as `/numbers` Step 4b: a large real move is signal, not error. A trigger legitimately fires on a real threshold cross — do not suppress it — but do not invent a touch where the new value simply moved a lot without crossing a registered threshold.
- **Skipping the check when triggers are absent.** A thesis with no `## Conviction Triggers`, or an empty scaffold, cannot be touch-checked — surface that gap (`no triggers to test`) rather than silently passing. `/lint #60` enforces trigger existence/falsifiability separately.

## Lint coupling

`/lint #60` checks that active theses carry non-empty, falsifiable Conviction Triggers — the precondition this check depends on. A thesis that fails #60 is one this contract cannot protect.
