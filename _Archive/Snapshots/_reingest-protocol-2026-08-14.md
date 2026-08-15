# Re-ingest rewrite protocol (2026-08-14)

Authorized rewrite of existing Research notes. Originals snapshotted under `_Archive/Backups/Research/* (pre-rewrite 2026-08-14).md`. Do not create a second research note.

## Hard constraints

1. Rewrite ONLY the assigned `Research/*.md` file. Do not edit theses, sectors, macros, `_hot.md`, `_graph.md`, `_Inbox/**`, or other research notes.
2. Do NOT acquire a vault lock (`.vault-lock*`). Parent coordinates concurrency.
3. Do NOT delete the research note if verification fails — expand and re-verify.
4. Preserve frontmatter `date:`, `source:`, `source_type:`, `tags:`, `ticker:`, `sector:`. Single-quote `source:`. Add `updated: 2026-08-14`. Do not invent a new filename.
5. Never author `> [!type]` callouts. Preserve any existing user callouts in place.
6. Research notes do not get a `## Log` section unless one already exists.

## Why this exists

A prior batch ingest crushed long Inbox articles into 200–400 word notes. Retention must scale with source length (ingest check #5). The Inbox file is the full source. Read it completely before writing.

## Retention floor (mandatory)

| source_words | R | floor | Key Segments |
|---|---|---|---|
| < 800 | 0.65 (min 300) | ≥300 | — |
| 800–2,000 | 0.58 | | — |
| 2,000–5,000 | 0.46 | | — |
| 5,000–15,000 | 0.36 | | — |
| 15,000–30,000 | 0.28 | required ≥3 subs | |
| 30,000–60,000 | 0.22 | required ≥4 | |
| > 60,000 | 0.18 | required ≥5 | |

Floor = R × actual source_words. No cap. Synthesis, not transcription.

`source_words` = word count of Inbox body after stripping YAML frontmatter and fenced code.

## Required body order

1. Optional `# Title` (keep existing title if present)
2. `## Thesis Delta` — 1–2 sentences. Mandatory consensus contrast: "consensus assumes/prices X → this source implies Y". Name the market assumption. Do not re-describe the business.
3. `## Summary` — source's argument, mechanism, claim scope. 2–4 paragraphs for long-form; more if the source is long. Not a business description.
4. `## Framework / Mental Model` — ONLY if the source names a framework / scoring scheme / typology / sliding scale. Capture name, components, methodology. Omit otherwise.
5. `## Evidence` — data points, tables preferred, no narrative. Provenance-tag every quantitative claim: `[1×: source-name]`, `[web: domain]`, `[est.]`. Match precision to sourcing.
6. `## Key Segments` — required only if source_words > 15,000. 3–8 H2-mirroring subsections, 2–5 sentences each.
7. `## Contradiction Check` — name the specific `[[Theses/TICKER - Name]]` §section / Conviction Trigger / Non-consensus Insight. "Supports the thesis" with no named target is a fail.
8. `## Source Excerpts` — quotes with numbers/framework claims not fully captured above. Delete if empty.

Writing: lead with the insight or number. No hedge words (importantly, notably, significantly, it's worth noting). Every sentence earns its place. Tables over prose for comparative/quantitative content.

## Mental models (mandatory before write)

Read, as lenses not verdicts:
- `/Users/alexcohen/InvestmentVault/Mental Models/Generalist - Overview.md` (always)
- `/Users/alexcohen/InvestmentVault/Mental Models/Industry - Semiconductors.md` if semis / datacenter / HBM / optics / packaging
- `/Users/alexcohen/InvestmentVault/Mental Models/Lens - Automation & AI Readiness.md` if AI/automation demand is load-bearing
- `/Users/alexcohen/InvestmentVault/Mental Models/Lens - Value Layer Monopoly.md` if the edge is owning a layer others must pay to traverse

Record fired triggers compactly inside Thesis Delta / Contradiction Check as hypotheses (`[G-n]`, `#1`…), never verdicts.

## Vault connection

- Grep `/Theses` for tickers in the note. Wikilink every related thesis as `[[Theses/TICKER - Company Name]]`.
- Read the thesis `## Summary` and `## Conviction Triggers` for Contradiction Check targeting (do not edit the thesis).
- Read the relevant `Sectors/*.md` heading + Active Theses if needed for sector context.
- Graph is orientation only: you may grep `_graph.md` for the ticker; do not skip a thesis because the graph omits it.

## Execution

1. Count `source_words` on the Inbox file (body only). Confirm it is within ~15% of the assigned count; if wildly different, recount and use your number.
2. Read the Inbox source in full. If >1,000 lines, read in chunks until the last line.
3. Read the existing research note (thin draft — keep any unique wikilinks or claims that remain true; do not keep the compression).
4. Read mental models + matching thesis Summary/Conviction Triggers.
5. Write the full research note with the Write tool (overwrite the same path).
6. Verify:
   ```
   python3 .agents/skills/ingest/scripts/verify_note.py "Research/<file>.md" \
     --mode local --source-type "<source_type>" --source-words <N>
   ```
7. If check #5 (retention) or #7 (empty sections) fails: expand the note and re-verify. Do not stop at a thin pass.
8. Re-read the written note. Fix YAML (quote `source:`). Ensure last line is a complete sentence.

## Report back (required)

- path
- source_words, body_words, floor, verdict (PASS/ADVISORY + which checks)
- strong-match theses wikilinked
- mental-model triggers fired
- whether Key Segments was required/written
- any source-content problem (paywall, truncated inbox clip)
