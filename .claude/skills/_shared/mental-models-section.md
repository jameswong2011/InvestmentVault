# Mental Models Section Contract

Consumed by: `/sync` (Step 3b / 3c / 4b — **writer**), `/deepen` (Phase 2.5 / Phase 5 — **writer**), `/ingest` (Step 1 / Step 4 — **identifier only, never writes thesis/sector bodies**)
Section owner: **shared** — any research-driven skill that applies the `/Mental Models` files may populate it. NOT skill-exclusive (contrast `## Legacy Callouts`, owned solely by `/archive-callouts`).
Governs: the `## Mental Models` section present in every Thesis and Sector note (added to both templates + backfilled 2026-06-24).

## What the section is

A per-note ledger of the OUTPUT of applying the `/Mental Models` context files to this opportunity / sector — specifically **which model triggers were pertinent**. It is NOT a place to re-argue the thesis. Three bullets, from the template:

- **Models applied** — which context files were consulted: `[[Generalist - Overview]]` (always), the matching `Industry -` note, any relevant `Lens -` note.
- **Triggers that fired** — each pertinent trigger / test / lens / disqualifier: name it, the model it came from, and the one-line read it produced — **held as a hypothesis to test, never a verdict**.
- **Disconfirming check** — where models agree, the bear case / the single falsifying datapoint / the base-rate the thesis (or sector consensus) must beat.

## MANDATORY reading gate (every writer)

Per CLAUDE.md ("Read the Mental Models folder before any investment analysis"), any skill that WRITES this section MUST first read the relevant `/Mental Models` files and apply the READING PROTOCOL at the top of `[[Generalist - Overview]]`:

- Models are **lenses and questions, never conclusions**. Every entry is a hypothesis to test against this note's own evidence.
- Run the base-rate / outside view **adversarially** against the other models.
- **Agreement across models is a trigger to disconfirm** (hunt the bear case + the single falsifying datapoint), not to commit.

Read scope: `[[Generalist - Overview]]` always; the matching `[[Industry - X]]` for the note's sector(s); any `[[Lens - X]]` whose theme the source / thesis touches. Batch/multi-note runs read these files ONCE and cache across the run (mirror the graph-primer single-Read discipline).

## Write procedure (merge, never overwrite)

1. **Trigger identification.** From the new research / analysis, determine which model triggers are newly pertinent or whose read changed. A "trigger" is a named test / lens / disqualifier / threshold in a `/Mental Models` file (e.g. Value Layer Monopoly §1 "Interface / standard control", Generalist "mean-reversion vs trend-continuation", a `Lens` readiness test).
2. **Selectivity — same bar as the rest of the note.** Update ONLY when a model trigger is newly activated, retired, or its read materially changed. Do NOT restate triggers already present; do NOT add one on trivial delta. **An unchanged section is the correct outcome for most runs** (mirrors `/sync` Step 3b "Do NOT update sections where the delta is trivial").
3. **Merge into the existing bullets.** Append the new trigger under **Triggers that fired** as one line — `<model> · <trigger name> — <one-line hypothesis read>`; add the consulted file to **Models applied** if absent; add / refine the **Disconfirming check** when models newly agree. **Idempotent**: never duplicate an entry already present (key on model + trigger name).
4. **Retire stale reads, never silently delete.** If new evidence falsifies a recorded trigger read, strike through with resolution — `~~<entry>~~ → Retired YYYY-MM-DD: <why>` (same convention as resolved Outstanding Questions). The section is an evolving analytical record.
5. **Optional dated attribution.** A trigger line may carry a trailing source pointer `(per [[Research/...]], YYYY-MM-DD)`. Keep terse — the note's `## Log` entry already carries the audit trail.

## Snapshot tier (snapshotting writers — `/sync` Step 3c, `/deepen` Phase 4)

Mirror `## Conviction Triggers`:
- First-population from the scaffold OR appending a NEW trigger line → **Tier B** (additive, no snapshot).
- Rewriting / striking through EXISTING populated entries → **Tier A** (snapshot required). `/deepen`'s Phase 4 whole-file `cp` already covers any Mental Models side-update.

## Callout compliance

Obeys the global callout policy. Writers **never author callouts** here — LLM uncertainty / alternative framings go in the prose of the three bullets, not in `> [!type]` blocks. Fresh / pinned callouts a USER places in the section are addressed / preserved per the normal callout rules.

## Per-skill responsibilities

- **`/sync` (primary writer)** — treats `## Mental Models` as a row in the Step 3b thesis impact map and an analogous sector update in Step 4b. Reads `/Mental Models` (gate above) during Step 2; writes per the merge procedure in Step 3d / 4b; the Step 3f Log entry covers it (no new prefix). High selectivity — most syncs leave it untouched.
- **`/deepen` (writer)** — two paths: (a) user targets it directly (`/deepen TICKER Mental Models`) → rewrite per Phase 5 like any section; (b) a deepen of ANY section whose Phase 3 research fires a model trigger records it here as a **secondary** update (covered by the Phase 4 snapshot). The section is in the Phase 2.5 comparative-whitelist (peer Mental Models sections are useful primer) but **excluded from Phase 2 auto-detect** (scaffold-empty by design — never auto-target it).
- **`/ingest` (identifier, NOT writer)** — ingest creates Research notes only; it NEVER edits thesis / sector bodies. During Step 1 framework detection it ALSO identifies which `/Mental Models` triggers the source activates, records them where natural in the research note, and surfaces "Mental-model triggers fired: […]" in the Step 4 report so the subsequent `/sync` performs the actual write. The thesis/sector write happens in `/sync`, never in `/ingest`.

## Anti-patterns

- Recording conclusions / verdicts instead of hypotheses-to-test (violates the READING PROTOCOL).
- Re-deriving the whole section every run (churn; breaks merge + idempotency).
- Treating model agreement as a buy signal rather than a disconfirm trigger.
- Authoring callouts in the section.
- `/ingest` editing a thesis / sector `## Mental Models` directly (wrong skill — ingest never writes thesis/sector bodies; route via `/sync`).
- Auto-targeting the section in `/deepen` weakness detection because the scaffold looks "empty."
