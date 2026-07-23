export const meta = {
  name: 'portfolio-supply-chain',
  description: "Map each thesis's value-chain position (via the value-chain skill), then stitch the book into one supply-chain graph — shared suppliers, shared customers, and cross-thesis single points of failure.",
  whenToUse: 'Portfolio value-chain / concentration map. Read-only unless persist:true (writes a note + optional Canvas).',
  phases: [
    { title: 'Enumerate', detail: 'list in-scope theses' },
    { title: 'Position', detail: 'run value-chain SKILL.md per thesis, READ-ONLY (parallel)' },
    { title: 'Stitch', detail: 'assemble the portfolio chain graph + shared nodes + SPOFs' },
    { title: 'Persist', detail: 'single-writer note + optional .canvas (persist:true only)' },
  ],
}

const cfg = args || {}
const STATUS = cfg.status || ['active', 'monitoring']
const MODEL = cfg.model || 'sonnet'
const LIMIT = cfg.limit || null

const ENUM_SCHEMA = { type: 'object', properties: { theses: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, file: { type: 'string' }, company: { type: 'string' }, sector: { type: 'string' } }, required: ['ticker', 'file'] } } }, required: ['theses'] }

const CHAIN_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    upstream: { type: 'array', items: { type: 'string' } },
    layer: { type: 'string' },
    downstream: { type: 'array', items: { type: 'string' } },
    competitors: { type: 'array', items: { type: 'string' } },
    bottleneck: { type: 'string' },
    spofs: { type: 'array', items: { type: 'string' } },
  },
  required: ['ticker', 'upstream', 'downstream'],
}

phase('Enumerate')
const enumerated = await agent(
  `List theses in /Theses. Glob /Theses/*.md, read frontmatter, return {ticker, file (repo-relative), company, sector} for every thesis whose status is one of: ${STATUS.join(', ')}. Return all matches, no cap.`,
  { phase: 'Enumerate', schema: ENUM_SCHEMA, effort: 'low' },
)
let theses = enumerated && enumerated.theses ? enumerated.theses : []
if (LIMIT) theses = theses.slice(0, LIMIT)
log(`Enumerated ${theses.length} theses`)
if (!theses.length) return { error: 'no theses matched', status: STATUS }

phase('Position')
const nodes = (await parallel(theses.map((t) => () =>
  agent(
    `You are ONE of many parallel, READ-ONLY analysts. Map the value-chain position of a single thesis: ${t.ticker} (${t.company || ''}), file ${t.file}.
Read the skill spec at .claude/skills/value-chain/SKILL.md and follow its "## Method" for THIS thesis, honoring its Mental Models gate. You are READ-ONLY: write NOTHING; RETURN the chain node as data. Name real entities in upstream/downstream/competitors, the company's own layer, the bottleneck holder, and single points of failure (spofs).`,
    { label: `chain:${t.ticker}`, phase: 'Position', schema: CHAIN_SCHEMA, model: MODEL },
  ),
))).filter(Boolean)
log(`Positioned ${nodes.length} theses on their chains`)

phase('Stitch')
const report = await agent(
  `You are given ${nodes.length} theses' value-chain nodes (JSON):
${JSON.stringify(nodes, null, 2)}

Stitch them into ONE portfolio supply-chain picture. Produce:
1. Shared-node map — suppliers, customers, or bottleneck holders that appear across MULTIPLE theses (name the node + the theses touching it). These are hidden couplings.
2. Cross-thesis single points of failure — one entity whose disruption hits 2+ positions. Rank by how many theses + their conviction.
3. Pricing-power ledger — per shared node, who holds pricing power and its trajectory.
Follow CLAUDE.md Writing Standards: tables over prose, lead with the most-shared node.`,
  { phase: 'Stitch', model: cfg.model || 'opus', effort: 'high' },
)

const persisted = []
if (cfg.persist) {
  phase('Persist')
  const res = await agent(
    `You are the SOLE writer. Persist this portfolio supply-chain analysis. Get today's date via \`date +%F\`.
1. Write ONE note: "Research/<date> - Portfolio - Supply Chain Map - synthesis.md" (frontmatter source: portfolio-supply-chain workflow, propagated_to: []; sections ## Thesis Delta, ## Summary, ## Evidence, ## Contradiction Check) with the content below.
2. If you can produce valid Obsidian Canvas JSON, ALSO write "Canvas/Portfolio Supply Chain <date>.canvas" with nodes for the shared entities and edges to the theses touching them. If unsure of the schema, skip the canvas rather than write malformed JSON.
Content:
${report}
Report the exact path(s) written.`,
    { phase: 'Persist', model: cfg.model || 'opus' },
  )
  persisted.push(res)
}

return { tested: nodes.length, report, persistedPaths: persisted }
