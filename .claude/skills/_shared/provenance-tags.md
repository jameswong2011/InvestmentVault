# Provenance-Tag Contract

Consumed by: `/ingest` (**writer** — tags Evidence figures), `verify_note.py` (**check #16** — advisory), `/sync` (**preserver** — carries tags on propagation), `/deepen` (**writer** — tags new quantitative claims), `/transcript` (earnings figures inherit the note's `source:` URL).
Owned by: **shared** — any skill that writes a quantitative claim into a Research or thesis body applies the convention.
Governs: terse inline source tags on quantitative claims, so a single-source or high-precision figure cannot acquire false authority as it propagates from a research note into thesis and sector spines.

## Why this exists

The vault's Evidence sections routinely carry precise figures traced to thin sourcing — a defect the skill audit found live: a die-yield `D0 ≈ 0.089` quoted to three decimals, sourced to a single X/Twitter thread, with no flag; peer yields at 5-point precision from a single-pass web search. Precision reads as authority. Worse, once `/sync` propagates such a figure into a thesis Bull Case or a sector competitive-dynamics table, it sheds even its research-note context and becomes an unqualified "fact." The provenance tag makes the sourcing travel *with the number*, everywhere the number goes.

Core principle: **precision must be earned by sourcing.** The more significant digits a figure carries, the stronger its provenance must be. A three-decimal number from one anonymous post is a smell, and the tag surfaces it.

## Tag vocabulary (terse, bracketed, inline)

Place the tag immediately after the figure or at the end of the Evidence row/bullet.

| Tag | Meaning | Sourcing strength |
|---|---|---|
| `[FMP]` | Financial Modeling Prep API | structured, high |
| `[10-K]` `[10-Q]` `[8-K]` | named SEC filing | primary, high |
| `[filing]` | unspecified regulatory filing | primary |
| `[IR]` | company IR deck / press release | primary-ish (company-framed) |
| `[transcript]` | earnings-call transcript | primary |
| `[web: domain]` | a web source, name the domain (`[web: stockanalysis.com]`) | medium |
| `[N sources]` | corroborated across N independent sources (`[3 sources]`) | strength rises with N |
| `[1×: source]` | **single, uncorroborated** source — name it (`[1×: @TheValueist]`) | **weak — the flag that matters** |
| `[est.]` | derived/estimated, not directly sourced (name the derivation if non-obvious) | inferred |

`[1×: …]` is the load-bearing tag: it is how a weakly-sourced number announces itself. Never omit it to make a figure look stronger.

## Rules

1. **Tag every quantitative claim in `## Evidence`.** Prices, margins, yields, share figures, growth rates, counts. Prose sentences that merely reference an already-tagged table figure need not re-tag.
2. **Match precision to sourcing.** If the only source is a single post or a lone web snippet, either (a) round the figure to the precision the source actually supports, or (b) keep the precision but tag `[1×: source]` so the mismatch is visible. Never present single-sourced high precision as bare fact.
3. **Preserve tags on propagation (`/sync`).** When `/sync` writes an Evidence figure into a thesis/sector body, carry its tag. A `[1×: …]` figure must not become an untagged assertion in a thesis spine. If space forbids the full tag inline, at minimum keep `[1×]` / `[est.]` so the weak-sourcing signal survives.
4. **New quantitative claims in thesis bodies (`/deepen`) carry tags too.** A `/deepen` that introduces a fresh number into Bull Case / Industry Context / Risks tags it the same way — the thesis spine is exactly where an untagged number does the most damage.
5. **Frontmatter `source:` is the note-level provenance; tags are the claim-level provenance.** A note whose every figure comes from its one `source:` may use a single uniform tag (e.g. all `[10-K]`); a synthesis pulling from many sources tags per-figure. The two coexist — `source:` is immutable provenance (CLAUDE.md), tags are granular.

## verify_note.py check #16 (advisory, never blocks)

`/ingest`'s post-write gate flags — advisory-only, in the `soft_fail` tier alongside #13/#15 — when the `## Evidence` section contains high-precision figures (≥2 decimal places) but **no** provenance tag anywhere in the section. This catches the exact audit case (precise numbers, zero sourcing tags). It never deletes a note; it surfaces the gap for the user to tag before `/sync` propagates. Skipped for `source_type: web-clip` / `data`.

## Anti-patterns

- **Dropping `[1×: …]` to make a number look authoritative.** The whole point is that weak sourcing travels with the figure.
- **Over-tagging prose.** Tag the Evidence table/data points, not every sentence — a prose reference to an already-tagged figure is fine untagged.
- **Inventing corroboration.** `[3 sources]` means three genuinely independent sources actually checked, not "it's probably right." Aggregators echoing one another are one source.
- **Stripping tags on propagation.** `/sync` and `/deepen` preserve/apply tags; they never launder a `[1×]` figure into bare fact.
