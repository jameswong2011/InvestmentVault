export const meta = {
  name: 'portfolio-macro-exposure',
  description: "Tag every thesis's implicit macro bets (via the macro-exposure skill), then find where the book is concentrated in a single macro variable dressed up as diversification.",
  whenToUse: 'Portfolio macro-concentration audit. Read-only unless persist:true.',
  phases: [
    { title: 'Enumerate', detail: 'list in-scope theses' },
    { title: 'Tag', detail: 'run macro-exposure SKILL.md per thesis, READ-ONLY (parallel)' },
    { title: 'Aggregate', detail: 'concentration by macro variable (conviction-weighted)' },
    { title: 'Persist', detail: 'single-writer synthesis note (persist:true only)' },
  ],
}

const cfg = args || {}
const STATUS = cfg.status || ['active', 'monitoring']
const MODEL = cfg.model || 'sonnet'
const LIMIT = cfg.limit || null

const ENUM_SCHEMA = { type: 'object', properties: { theses: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, file: { type: 'string' }, company: { type: 'string' }, conviction: { type: 'string' } }, required: ['ticker', 'file'] } } }, required: ['theses'] }

const MACRO_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    conviction: { type: 'string' },
    bets: { type: 'array', items: { type: 'object', properties: { variable: { type: 'string' }, direction: { type: 'string' }, magnitude: { type: 'string' }, horizon: { type: 'string' }, stated: { type: 'boolean' } }, required: ['variable', 'direction'] } },
    biggestUnstated: { type: 'string' },
  },
  required: ['ticker', 'bets'],
}

phase('Enumerate')
const enumerated = await agent(
  `List theses in /Theses. Glob /Theses/*.md, read frontmatter, return {ticker, file (repo-relative), company, conviction} for every thesis whose status is one of: ${STATUS.join(', ')}. Return all matches, no cap.`,
  { phase: 'Enumerate', schema: ENUM_SCHEMA, effort: 'low' },
)
let theses = enumerated && enumerated.theses ? enumerated.theses : []
if (LIMIT) theses = theses.slice(0, LIMIT)
log(`Enumerated ${theses.length} theses`)
if (!theses.length) return { error: 'no theses matched', status: STATUS }

phase('Tag')
const tagged = (await parallel(theses.map((t) => () =>
  agent(
    `You are ONE of many parallel, READ-ONLY analysts. Tag the implicit macro bets of a single thesis: ${t.ticker} (${t.company || ''}, conviction ${t.conviction || '?'}), file ${t.file}.
Read the skill spec at .claude/skills/macro-exposure/SKILL.md and follow its "## Method" for THIS thesis, honoring its Mental Models gate. You are READ-ONLY: write NOTHING; RETURN the tags as data. Include the thesis conviction in the 'conviction' field and name the biggestUnstated macro bet.`,
    { label: `macro:${t.ticker}`, phase: 'Tag', schema: MACRO_SCHEMA, model: MODEL },
  ),
))).filter(Boolean)
log(`Tagged ${tagged.length} theses`)

phase('Aggregate')
const compact = tagged.map((m) => ({ ticker: m.ticker, conviction: m.conviction, bets: (m.bets || []).map((b) => ({ v: b.variable, dir: b.direction, mag: b.magnitude })), unstated: m.biggestUnstated }))
const report = await agent(
  `You are given ${compact.length} theses' implicit macro bets (JSON):
${JSON.stringify(compact, null, 2)}

Aggregate into a macro-CONCENTRATION view. Normalize variable wording. Produce:
1. Ranked concentration table — macro variable | # theses | conviction-weighted exposure (high=3/med=2/low=1) | net direction (are they all the same way, or offsetting?). Lead with the variable the book is most concentrated in.
2. The single largest UNHEDGED bet — the variable where the most conviction rides the same direction with no offsetting position.
3. Hidden bets — variables that show up mostly as 'unstated' across theses (the exposures the book is running without admitting).
Follow CLAUDE.md Writing Standards: tables over prose, lead with the number.`,
  { phase: 'Aggregate', model: cfg.model || 'opus', effort: 'high' },
)

const persisted = []
if (cfg.persist) {
  phase('Persist')
  const res = await agent(
    `You are the SOLE writer. Persist this portfolio macro-exposure analysis as ONE note in "Macro & Technology/". Get today's date via \`date +%F\`. Path: "Macro & Technology/<date> - Portfolio Macro Exposure.md". Frontmatter: date, tags [macro, portfolio, meta], source: portfolio-macro-exposure workflow. Body content:
${report}
Report the exact path written.`,
    { phase: 'Persist', model: cfg.model || 'opus' },
  )
  persisted.push(res)
}

return { tested: tagged.length, report, persistedPaths: persisted }
