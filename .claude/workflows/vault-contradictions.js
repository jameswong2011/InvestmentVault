export const meta = {
  name: 'vault-contradictions',
  description: "Extract every thesis's load-bearing assumptions (via the assumptions skill), find cross-thesis clashes (one thesis's bull premise = another's bear premise), and adversarially verify each is a real contradiction, not a framing difference.",
  whenToUse: 'Portfolio coherence audit — where do two positions bet opposite ways on the same industry claim. Read-only unless persist:true.',
  phases: [
    { title: 'Enumerate', detail: 'list in-scope theses' },
    { title: 'Extract', detail: 'run assumptions SKILL.md per thesis, READ-ONLY (parallel)' },
    { title: 'Pair', detail: 'find candidate cross-thesis assumption clashes' },
    { title: 'Verify', detail: 'adversarially confirm each clash is real (parallel)' },
    { title: 'Persist', detail: 'single-writer synthesis note (persist:true only)' },
  ],
}

const cfg = args || {}
const STATUS = cfg.status || ['active', 'monitoring']
const MODEL = cfg.model || 'sonnet'
const LIMIT = cfg.limit || null

const ENUM_SCHEMA = { type: 'object', properties: { theses: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, file: { type: 'string' }, company: { type: 'string' } }, required: ['ticker', 'file'] } } }, required: ['theses'] }

const ASSUM_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    assumptions: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, falsifier: { type: 'string' }, criticality: { type: 'string' }, industryLevel: { type: 'boolean' } }, required: ['claim'] } },
  },
  required: ['ticker', 'assumptions'],
}

const PAIR_SCHEMA = {
  type: 'object',
  properties: {
    candidates: { type: 'array', items: { type: 'object', properties: { topic: { type: 'string' }, thesisA: { type: 'string' }, claimA: { type: 'string' }, thesisB: { type: 'string' }, claimB: { type: 'string' } }, required: ['thesisA', 'claimA', 'thesisB', 'claimB'] } },
  },
  required: ['candidates'],
}

const VERDICT_SCHEMA = { type: 'object', properties: { real: { type: 'boolean' }, reasoning: { type: 'string' } }, required: ['real'] }

phase('Enumerate')
const enumerated = await agent(
  `List theses in /Theses. Glob /Theses/*.md, read frontmatter, return {ticker, file (repo-relative), company} for every thesis whose status is one of: ${STATUS.join(', ')}. Return all matches, no cap.`,
  { phase: 'Enumerate', schema: ENUM_SCHEMA, effort: 'low' },
)
let theses = enumerated && enumerated.theses ? enumerated.theses : []
if (LIMIT) theses = theses.slice(0, LIMIT)
log(`Enumerated ${theses.length} theses`)
if (!theses.length) return { error: 'no theses matched', status: STATUS }

phase('Extract')
const extracted = (await parallel(theses.map((t) => () =>
  agent(
    `You are ONE of many parallel, READ-ONLY analysts. Extract the load-bearing assumptions of a single thesis: ${t.ticker} (${t.company || ''}), file ${t.file}.
Read the skill spec at .claude/skills/assumptions/SKILL.md and follow its "## Method" for THIS thesis, honoring its Mental Models gate. You are READ-ONLY: write NOTHING; RETURN the assumptions ledger as data. Set industryLevel=true for claims about the INDUSTRY (not just this company) — those are the ones that clash across theses.`,
    { label: `assume:${t.ticker}`, phase: 'Extract', schema: ASSUM_SCHEMA, model: MODEL },
  ),
))).filter(Boolean)
log(`Extracted assumptions from ${extracted.length} theses`)

phase('Pair')
// Only industry-level assumptions can clash across theses — project those.
const industry = extracted.map((e) => ({ ticker: e.ticker, claims: (e.assumptions || []).filter((a) => a.industryLevel).map((a) => a.claim) })).filter((e) => e.claims.length)
const paired = await agent(
  `You are given industry-level assumptions per thesis (JSON):
${JSON.stringify(industry, null, 2)}

Find CANDIDATE CONTRADICTIONS: pairs of theses that bet OPPOSITE ways on the same industry claim (thesis A needs X true, thesis B needs X false). Group by topic. Only surface genuine opposites on the SAME variable — not merely different topics. Return the candidate pairs.`,
  { phase: 'Pair', schema: PAIR_SCHEMA, model: cfg.model || 'opus', effort: 'high' },
)
const candidates = paired && paired.candidates ? paired.candidates : []
log(`${candidates.length} candidate cross-thesis clashes`)

phase('Verify')
const verified = (await parallel(candidates.map((c) => () =>
  agent(
    `Adversarially verify a claimed portfolio contradiction. Topic: ${c.topic || '(untitled)'}.
- ${c.thesisA} assumes: ${c.claimA}
- ${c.thesisB} assumes: ${c.claimB}
Is this a REAL contradiction — the two positions cannot both be right on the same variable — or just a framing/timing/segment difference that reconciles? Read both theses if needed. Set real=true ONLY if genuinely irreconcilable.`,
    { label: `verify:${c.thesisA}~${c.thesisB}`, phase: 'Verify', schema: VERDICT_SCHEMA, model: MODEL },
  ),
))).map((v, i) => ({ ...candidates[i], verdict: v })).filter((x) => x.verdict && x.verdict.real)
log(`${verified.length} confirmed cross-thesis contradictions`)

phase('Synthesize')
const report = await agent(
  `Confirmed cross-thesis contradictions (JSON):
${JSON.stringify(verified, null, 2)}

Write a portfolio coherence report: each confirmed contradiction — the shared variable, the two theses + their opposite bets, and which one the recent evidence favors (so the user knows which side to pressure-test). If none survived, say so plainly. Follow CLAUDE.md Writing Standards: lead with the count, tables over prose.`,
  { phase: 'Synthesize', model: cfg.model || 'opus', effort: 'high' },
)

const persisted = []
if (cfg.persist) {
  phase('Persist')
  const res = await agent(
    `You are the SOLE writer. Persist this portfolio contradiction audit as ONE Research note. Get today's date via \`date +%F\`. Path: "Research/<date> - Portfolio - Contradiction Audit - synthesis.md" (frontmatter source: vault-contradictions workflow, propagated_to: []; sections ## Thesis Delta, ## Summary, ## Evidence, ## Contradiction Check). Body content:
${report}
Report the exact path written.`,
    { phase: 'Persist', model: cfg.model || 'opus' },
  )
  persisted.push(res)
}

return { tested: extracted.length, candidates: candidates.length, confirmed: verified.length, report, persistedPaths: persisted }
