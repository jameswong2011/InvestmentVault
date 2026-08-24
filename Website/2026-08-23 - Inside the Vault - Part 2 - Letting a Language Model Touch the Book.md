---
date: 2026-08-23
tags:
  - essay
  - research-process
  - laniakea-partners
  - safety-engineering
  - tooling
status: draft
audience: general-investor
source_note:
  - "[[Build documents/INFRASTRUCTURE]]"
  - "[[Build documents/User Guide]]"
  - "[[Build documents/Vault Explainer]]"
  - "[[Live Portfolio]]"
source: internal synthesis
---

# Inside the vault: letting a language model touch the book

*Part two of three on the research system behind Laniakea Partners. Part one covered the structure: a compiled research wiki maintained by a language model. This part covers the machinery: the named procedures the model works through and the safety engineering that makes a probabilistic writer trustworthy around four months of accumulated work. Part three covers the sensing and adversarial layers.*

**On 4 June 2026 the vault's dependency-graph rebuild ran 57 minutes and died on an output-token limit.** The graph was then produced the obvious way: the model read the book and wrote the file. At 1,300 edges the file outgrew what a model can reliably stream, and the failure was the productive kind, because the fix removed the model from the write path entirely. A Python generator now reads the vault and writes the graph deterministically in about a second, the incident is dated in the generator's own docstring, and later scripts cite it by name as 'the generate_graph.py precedent' when they justify their own existence. Health checks, section extraction, metric arithmetic and chart rendering have all since migrated from model output to code on the same reasoning. The division of labour that fell out of one bad afternoon now governs the whole machine: the model judges, scripts write, and anything derivable without judgement is not the model's job.

## Work happens through named procedures

The model never edits the book freestyle. It works through 27 named procedures ('skills' in the harness vocabulary), each a specification the model must follow: pre-flight checks, a method, a write discipline, and a reporting contract that lists every file modified. The specifications total 9,902 lines; the largest, the propagation procedure `/sync`, runs 968 lines on its own, because propagation is where a research finding fans out into every affected thesis, sector map and macro note, and fan-out is where an undisciplined writer does the most damage.

| Family | Procedures |
|---|---|
| Core loop | ingest, sync, status, graph |
| Building | thesis, deepen, brief, numbers |
| Analytical | surface, stress-test, scenario, compare, catalyst, retro, transcript |
| Diagnostic (read-only) | assumptions, conviction-audit, dependency-map, macro-exposure, value-chain |
| Maintenance | lint, prune, clean, archive-callouts, rollback, rename |
| Publishing | portfolio-snapshot |

The daily loop uses four of them. Raw material is deposited in the inbox; `/ingest` converts it into structured research notes; `/sync` propagates the deltas across every affected note in the book; the graph refreshes itself through an end-of-session hook. `/status`, which executes conviction and status changes, sits outside the automated flow on purpose: the model may recommend a downgrade with as much force as the evidence supports, and it cannot execute one, because a conviction change is an investment decision and every one of them passes through us.

The procedures also read each other's handwriting. Every Log entry begins with a prefix drawn from a registry of about nineteen ('Stress test:', 'Numbers refresh:', 'CLOSED', and so on), and `/sync` classifies recent entries against that registry to decide what counts as new research to propagate versus bookkeeping to skip. A metrics refresh therefore does not ripple through fifty sector notes, and a hand-edit without a recognised prefix is treated as research-driven and propagated, which is the safe default. Two prefixes carry a deliberately significant trailing space so that ordinary prose mentioning the word 'scenario' cannot collide with them.

## The failure mode is enthusiasm

A language model loose in a knowledge base does not fail through malice. It fails through eagerness: overwriting where it should append, scaffolding a section rather than admitting one is absent, completing half of a multi-file rename, or racing a second concurrent session for the same cache file. The vault holds five independent layers against this, and the design assumption behind all five is stated in our own documentation: mistakes cost a snapshot, not data, and the rules are enforced by machinery rather than by trusting the model.

| Layer | Mechanism |
|---|---|
| Change tiers | Protected files (the constitution, templates, procedure specs) refuse modification without explicit instruction; Logs and research bodies are append-only; conviction changes, closures, renames and link removals require human confirmation |
| Pre-flight | Lock files with run-unique tokens, acquired atomically, re-verified before every write batch; a half-finished rename leaves a marker file every other procedure hard-blocks on |
| Transactions | A snapshot before every destructive run (543 currently in the archive, each named for what triggered it, e.g. `SK Hynix (pre-deepen 2026-08-14)`); multi-file operations write a manifest skeleton first and flip it complete only at the end, so a crash is visible rather than silent |
| Harness hooks | A pre-execution guard denies writes to protected paths before the tool call runs, independent of whether the model remembers the rule |
| Health checks | `/lint` runs 65 active checks over structure, freshness and analytical hygiene; the deterministic majority execute in a script in under a second |

Some of the detail rewards attention. Locks come in three scopes (vault-wide, per-ticker, read-only) with timeouts from two to fifteen minutes, and a stale lock is never auto-stolen: recovery is always a human decision, because the one scenario worse than a blocked run is two runs that both believe they own the file. The comparison procedure acquires N separate per-ticker locks rather than one joint lock, with reverse-order rollback if acquisition partially fails, a design chosen because tickers like BRK-B contain the character a joint lock would have used as a delimiter. Snapshots feed `/rollback`, which can restore any thesis, sector or macro note to its pre-edit state; the rename branch of it offers a symmetric reverse-rename rather than a duplicate restore when the original filename no longer exists.

The health checks are the layer that grew the most. Among the 65: a stale-lock sweep, schema validation on the session cache, a check that every conviction trigger is actually falsifiable as written, a staleness alarm on any key-metrics table older than 90 days, and a critical alert if the backlog of unpropagated work exceeds 20% of the book, the signal that the loop itself has broken down. One check enforces the house prose style, banning hedge words from analytical spines: a style guide with its own linter. Every Sunday evening a scheduler runs the full battery headless and publishes the results as a dated health note, so the system files a report on itself whether or not anyone opened it that week.

## Even memory has a budget

Between sessions the model's working memory is a single file, the session cache: six fixed sections covering the active research thread, recent syncs, conviction changes, open questions and a portfolio snapshot. It carries a word budget (8,000 soft, 10,000 hard) and a seven-step compression order that specifies exactly what gets dropped first as it fills: oldest sync-archive entry, then oldest thread line, then merged duplicate questions, and so on down to an aggressive fallback. The compression is self-documenting; the file accumulates dated comments confessing each squeeze, and one from mid-August ends 'file remains over the soft cap — flagged for cleanup'. A working memory that admits it is over budget, in writing, is a small thing that prevents a large one: silent truncation is how systems forget without noticing, and two of the 65 health checks exist purely to catch truncation markers and schema drift in this one file.

## Every rule has a date attached

The specifications read less like design documents than like scar tissue, because most rules were written the day something failed.

A key-extraction one-liner used a regex feature that exists in GNU tools and silently does nothing on macOS, so the procedure printed a confident `FMP_KEY_OK` while carrying an entire JSON blob as its API key; the rule is now 'parse JSON with a JSON parser'. A shell defaults difference meant the multi-ticker lock loop once created a single lock file literally named `.vault-lock.NVDA AAPL`, quietly defeating the concurrency control it implemented. A JavaScript string-replace treated `$` in fetched market data as a backreference and corrupted the portfolio tracker's earnings table across refreshes; every replace in the trackers now uses function form. The callout-archiving procedure refuses to classify its arguments by regex at all, because our tickers include 000660 and 2383 and no character class can tell a Korean ticker from a day-count threshold; it checks the filesystem instead. The rename sanitiser rejects Windows reserved device names on a vault that will never leave macOS, which costs one line and closes a class of bug permanently. And a rule from 22 April requires any procedure whose specification was truncated for context reasons to re-read the full spec from disk before its first write, because on that date a propagation gate fell out of a compacted spec and the model, seeing no rule, invented a plausible behaviour in its place. Plausible-in-place-of-specified is the characteristic model failure, and it is why the specs are treated as the product.

The same hard-won quality extends to how work is delegated. An early mechanism for running heavy procedures in a forked context was reverted within a month (the fork returned its report as unrendered output: a blank panel), replaced by explicit sub-agent delegation in which a disposable reader does the heavy scanning and returns a compact report. An unscoped vault survey that would burn roughly 380,000 tokens of main-thread context now costs the main thread about 15,000, which is the difference between a procedure that gets run and one that gets avoided.

## Numbers earn their precision

Market data enters through one gate: a Financial Modeling Prep integration whose key lives in a git-ignored config file. `/numbers` refreshes a thesis's key-metrics table as a surgical edit, pausing for confirmation on any material delta, and a scoped web-search fallback covers only named per-field gaps, tagged as such. Quantitative claims in analytical prose carry provenance tags ([FMP], [10-K], [est.], and [1×: source] for anything single-sourced), a convention created after an audit found a die-yield figure quoted to three decimal places whose entire provenance was one X thread. Precision must be earned by sourcing; the tag makes unearned precision visible at a glance.

The trackers close the loop between book and portfolio. The live portfolio note and the 70-ticker watchlist are interactive documents: a refresh button pulls quotes, estimates and price history in one batch, renders returns and forward multiples, and rewrites a marker-delimited table in place. The rendered table, and never the config array behind it, is the source of truth: delete a row and the name stays deleted on every future refresh, which means the document is edited like a document even though it behaves like an application.

None of this ceremony is free, and all of it prices the same risk: a system whose value is accumulated state can afford almost any overhead except doubt about that state. The locks, snapshots, manifests and 65 checks buy one property, which is that any question can be asked of the book, by us or by the model, without wondering whether the answer sits on quietly corrupted ground. Part three covers what gets built on that trust: the overnight sensing layer, the feedback loop where we argue with the machine in the margins of our own notes, and the adversarial procedures whose entire purpose is to attack the book they maintain.
