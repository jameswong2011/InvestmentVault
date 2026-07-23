export const meta = {
  name: 'portfolio-correlation',
  description: "Map every thesis's dependency fingerprint (via the dependency-map skill), then find names whose bull cases secretly rest on the same variable — correlated bets the market prices independently.",
  whenToUse: 'Find hidden cross-name correlation / concentration in the book. Read-only unless persist:true.',
  phases: [
    { title: 'Enumerate', detail: 'list in-scope theses' },
    { title: 'Extract', detail: 'run dependency-map SKILL.md per thesis, READ-ONLY (parallel)' },
    { title: 'Correlate', detail: 'cluster shared load-bearing dependencies into correlated-bet groups' },
    { title: 'Persist', detail: 'single-writer synthesis note (persist:true only)' },
  ],
}

const cfg = args || {}
const STATUS = cfg.status || ['active', 'monitoring']
const MODEL = cfg.model || 'sonnet'
const LIMIT = cfg.limit || null

const ENUM_SCHEMA = { type: 'object', properties: { theses: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, file: { type: 'string' }, company: { type: 'string' }, conviction: { type: 'string' } }, required: ['ticker', 'file'] } } }, required: ['theses'] }

const DEP_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    loadBearing: { type: 'array', items: { type: 'object', properties: { variable: { type: 'string' }, bucket: { type: 'string' }, direction: { type: 'string' }, magnitude: { type: 'string' }, stated: { type: 'boolean' } }, required: ['variable'] } },
    owned: { type: 'array', items: { type: 'string' } },
  },
  required: ['ticker', 'loadBearing'],
}

phase('Enumerate')
const enumerated = await agent(
  `List theses in /Theses to analyze. Glob /Theses/*.md, read frontmatter, return {ticker, file (repo-relative), company, conviction} for every thesis whose status is one of: ${STATUS.join(', ')}. Return all matches, no cap.`,
  { phase: 'Enumerate', schema: ENUM_SCHEMA, effort: 'low' },
)
let theses = enumerated && enumerated.theses ? enumerated.theses : []
if (LIMIT) theses = theses.slice(0, LIMIT)
log(`Enumerated ${theses.length} theses`)
if (!theses.length) return { error: 'no theses matched', status: STATUS }

phase('Extract')
const fingerprints = (await parallel(theses.map((t) => () =>
  agent(
    `You are ONE of many parallel, READ-ONLY analysts. Extract the dependency fingerprint of a single thesis: ${t.ticker} (${t.company || ''}), file ${t.file}.
Read the skill spec at .claude/skills/dependency-map/SKILL.md and follow its "## Method" for THIS thesis, honoring its Mental Models gate. You are READ-ONLY: write NOTHING to the vault; RETURN the fingerprint as data.
Return loadBearing (the 2-3 variables that break the thesis if they move) with variable/bucket/direction/magnitude/stated, plus owned (dependencies the company itself owns — value-layer).`,
    { label: `dep:${t.ticker}`, phase: 'Extract', schema: DEP_SCHEMA, model: MODEL },
  ),
))).filter(Boolean)
log(`Extracted ${fingerprints.length} dependency fingerprints`)

phase('Correlate')
const compact = fingerprints.map((f) => ({ ticker: f.ticker, vars: (f.loadBearing || []).map((d) => ({ v: d.variable, dir: d.direction, mag: d.magnitude })), owned: f.owned || [] }))
const report = await agent(
  `You are given ${compact.length} theses' load-bearing dependency fingerprints (JSON):
${JSON.stringify(compact, null, 2)}

Find CORRELATED BETS: groups of theses whose bull cases depend on the SAME underlying variable (same customer, same input, same tech transition, same macro driver), especially where the market treats the names as independent. Normalize variable wording (e.g. "AI datacenter capex" == "hyperscaler accelerator spend").
Produce:
1. Ranked correlated-bet clusters — each: the shared variable, the theses in it (with direction), why the coupling is non-obvious. Rank by cluster size x conviction.
2. Concentration flags — the 3 variables the largest share of the book rides on.
3. Natural hedges — pairs depending on the SAME variable in OPPOSITE directions.
Follow CLAUDE.md Writing Standards: lead with the cluster + count, tables over prose.`,
  { phase: 'Correlate', model: cfg.model || 'opus', effort: 'high' },
)

const persisted = []
if (cfg.persist) {
  phase('Persist')
  const res = await agent(
    `You are the SOLE writer. Persist this portfolio dependency-correlation analysis as ONE Research note. Get today's date via \`date +%F\`. Path: "Research/<date> - Portfolio - Dependency Correlation - synthesis.md". Follow vault Research-note conventions (frontmatter source: portfolio-correlation workflow, propagated_to: []; sections ## Thesis Delta, ## Summary, ## Evidence, ## Contradiction Check). Body content:
${report}
Report the exact path written.`,
    { phase: 'Persist', model: cfg.model || 'opus' },
  )
  persisted.push(res)
}

return { tested: fingerprints.length, report, persistedPaths: persisted }
