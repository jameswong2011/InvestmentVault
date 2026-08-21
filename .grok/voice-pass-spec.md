# Voice pass spec (meaning-preserving)

Date: 2026-08-20
Workspace: `/Users/alexcohen/InvestmentVault`

This is a diction pass, not analysis. **Do not lose meaning.** If a rewrite would drop, weaken, strengthen, or re-target a claim, keep the original sentence and only fix punctuation.

Voice exemplar (read once): `Mental Models/IGNORE - English - Culture and Management RAW.md`
Writing standards live in `CLAUDE.md` § Writing Standards → Voice. Follow them. This spec adds operational rules so you do not repeat the Thesis One–Four meaning losses.

## Scope

Edit only the files listed in your prompt. They are under `Theses/`, `Sectors/`, or `Macro & Technology/`.

Do not touch: `Research/`, `Website/`, `Mental Models/`, `_hot.md`, `_graph.md`, `_followups.md`, `Live Portfolio.md`, `Templates/`, `CLAUDE.md`, `AGENTS.md`, `.obsidian/`.

## Frozen regions (byte-identical)

Leave these untouched except the single Log append described below:

1. YAML frontmatter (the block between the first two `---` lines)
2. The entire `## Log` section, except appending one new dated entry at the end
3. The entire `## Legacy Callouts` section
4. Every Obsidian callout block (`> [!question]`, `[!error]`, `[!tip]`, `[!todo]`, addressed or fresh or pinned). Copy verbatim, including `>` prefixes and `[[pinned]]`
5. Wikilinks `[[...]]` and embeds `![[...]]` — do not add, remove, rename, or retarget
6. HTML comments `<!-- ... -->`
7. Fenced code blocks
8. Numbers, dates, tickers, percentages, multiples, units, table structure (pipe rows)

If a frozen region contains an em-dash, leave it (Log delimiter is schema).

## What to change (body prose only)

Target LLM furniture, not claims.

**Em-dashes (`—`, U+2014) and spaced double-hyphen clause breaks (` -- `):**
Replace with a comma, colon, semicolon, or full stop, whichever keeps the original syntax. Hyphenated compounds (`long-term`, `silicon-based`) stay. En-dashes in ranges (`$30–40T`, `2015–19`, `8x-669x`) stay. CLI flags (`--all`) stay. More than one em-dash in a rewritten sentence is a defect. A rare aside where a comma is ambiguous may keep one em-dash.

**Banned furniture — recast without dropping the claim behind it:**
- Inversion closers: "X is not Y; it is Z" / "do not merely X" / "This thesis is not an observation; it is a description"
- Labelled insight: "This is the variant perception:" / "The falsifier:" / "Note what does not falsify it:" / "Strip the industry to first principles" / "The disciplined inversion" / "Three traits predict"
- Italic or bold used only as argumentative stress (`share _is_ quality`). Keep bold on real headings and lead terms
- Cute standalone kickers the paragraph does not need
- Dramatic unfalsifiable timing ("about to move violently")
- Second-person LinkedIn instruction. Do **not** blindly rewrite `you` → `we`. If `you` addresses the reader as allocator, keep `you`. If it is empty furniture, recast in the firm's `we` only when the claim is already about Laniakea / the portfolio
- Even punchline cadence: do not add kickers; you may break a staccato run into a nested sentence

**Colour:**
Keep an image if it *is* the claim (named mispricing, a thesis frame used once: lords/serfs, toll road, nervous system, bedrock). Delete decorative colour if the claim survives without it. Do not extend a metaphor. Do not introduce new metaphors.

**Uncommon terms:**
Keep parenthetical definitions (cybernetics, etc.). Do not delete them as "LLM explainers." Do not add student-definitions of terms the note already uses as given.

## Meaning freeze (hard)

From a prior pass that *did* lose meaning. Never repeat these classes of change:

- Framing → assertion ("can be thought of as" → "is") is a meaning change. Keep the original epistemic status
- Do not drop a positive restatement that carries a claim ("everything suggests we are early")
- Do not insert units the source did not have (`30-40T` → `$30–40T`)
- Do not drop contrast markers that pair two claims ("On the other hand")
- Do not drop stipulated definitions
- Do not change metaphor → ontology ("better metaphor" → "better frame") unless the source already treats it as ontology
- Do not replace a transformation verb with a state verb ("become wiring diagrams" → "is a map")
- Do not drop degree words (`entirely`, `only`, `the only question that matters`)
- Do not replace a specific verb with a generic one (`confabulate` → `invent`; `calls it judgment` → `treats it as`; `hedge every sentence` → `sand every sentence`; `fields` → `can field`)
- Do not change who the agent is ("corporations will make the assumption look dated" → "the assumption will age")
- Do not weaken conviction to evidence (`we do not believe` → `we do not see evidence`)
- Do not drop "wearing a strategy" / "enlarge their estates" if that is the claim (costume; expansion). You may recast only if the recast states the same claim
- Do not add financial claims the source did not make (`compounds rather than dilutes`)
- Do not drop "rather than tactical"
- Do not retarget addressee (`you` allocator → `we` firm) if that changes whose standard it is
- Do not drop "the research organisation is itself a firm"
- Do not change artifact vs identity ("live artifact of the machine" vs "the machine")
- Do not change "incentive distortions" to "incentive problem"
- Do not upgrade "disciplined inversion" into "better method" (value judgment)
- Do not add "can" onto a present-tense capability claim
- Do not British-ify or American-ify spelling as a pass. Leave spelling unless you are already rewriting that sentence and the note is already mixed

**Preserve exactly:** every figure, every named company, every wikilink, every table row, every heading text (`##` / `###`), every Conviction Trigger if/then, every status/conviction word in body that matches frontmatter.

## Log append (only mutation allowed in `## Log`)

If `## Log` exists, append (do not edit older entries). If `### 2026-08-20` already exists, add the bullet under it. Otherwise append:

```
### 2026-08-20
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged
```

Max 2 lines. If the note has no `## Log`, skip the append; do not create the section.

## Method

1. Read the exemplar once.
2. For each assigned file, `read_file` the **entire** note before any write.
3. Count before: `##` headings; `[[` wikilinks; em-dashes outside Log/Legacy/frontmatter.
4. Rewrite body in place. Prefer `search_replace` for local furniture if the file is huge and only some paragraphs are dirty. Use `Write` only if you have the full reconstructed file in hand, including frozen regions copied verbatim.
5. After write, re-read the file (or grep headings). Confirm:
   - heading set unchanged
   - wikilink count not decreased
   - frontmatter unchanged
   - Log history unchanged except the new bullet
   - callouts still present
   - no `TODO` / placeholders / truncation markers (`...`, `[rest omitted]`)
6. Process files one at a time. Do not skip a listed file. If a file is already clean (no em-dashes in body, no banned furniture), still add the Log bullet only if you made no body edit — in that case skip the file entirely and report `skipped-already-clean`.

## Report (your final message)

For each file:
- `edited` or `skipped-already-clean`
- body em-dashes before → after
- wikilink count before → after
- heading count before → after
- list any sentence you left dirty because rewriting it would move meaning
- list any meaning-risk you are uncertain about (do not silently guess)
