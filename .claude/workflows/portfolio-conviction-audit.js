export const meta = {
  name: 'portfolio-conviction-audit',
  description: "Audit every thesis for conviction-evidence mismatch and silently-fired Conviction Triggers (via the conviction-audit skill); rank the book by over-conviction + unactioned triggers and feed /status.",
  whenToUse: 'Periodic conviction hygiene — find over-convicted names and triggers that fired without action. Read-only unless persist:true (writes _followups only; never conviction).',
  phases: [
    { title: 'Enumerate', detail: 'list in-scope theses' },
    { title: 'Audit', detail: 'run conviction-audit SKILL.md per thesis, READ-ONLY (parallel)' },
    { title: 'Rank', detail: 'rank by over-conviction + fired triggers' },
    { title: 'Persist', detail: 'single-writer _followups entries for flagged names (persist:true; never touches conviction)' },
  ],
}

const cfg = args || {}
const STATUS = cfg.status || ['active', 'monitoring']
const MODEL = cfg.model || 'sonnet'
const LIMIT = cfg.limit || null

const ENUM_SCHEMA = { type: 'object', properties: { theses: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, file: { type: 'string' }, company: { type: 'string' }, conviction: { type: 'string' } }, required: ['ticker', 'file'] } } }, required: ['theses'] }

const AUDIT_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    statedConviction: { type: 'string' },
    verdict: { type: 'string' },
    firedTriggers: { type: 'array', items: { type: 'object', properties: { trigger: { type: 'string' }, currentValue: { type: 'string' } }, required: ['trigger'] } },
    recommendedStatus: { type: 'string' },
    staleDays: { type: 'integer' },
  },
  required: ['ticker', 'verdict'],
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

phase('Audit')
const audits = (await parallel(theses.map((t) => () =>
  agent(
    `You are ONE of many parallel, READ-ONLY analysts. Audit the conviction of a single thesis: ${t.ticker} (${t.company || ''}, stated conviction ${t.conviction || '?'}), file ${t.file}.
Read the skill spec at .claude/skills/conviction-audit/SKILL.md and follow its "## Method" for THIS thesis, honoring its Mental Models gate. You are READ-ONLY: write NOTHING; RETURN the audit as data. Report verdict (supported|over-convicted|under-convicted), any firedTriggers (condition met but conviction unchanged), staleDays, and the recommendedStatus action (or "none").`,
    { label: `conv:${t.ticker}`, phase: 'Audit', schema: AUDIT_SCHEMA, model: MODEL },
  ),
))).filter(Boolean)
log(`Audited ${audits.length} theses`)

phase('Rank')
const flagged = audits.filter((a) => a.verdict !== 'supported' || (a.firedTriggers || []).length)
const report = await agent(
  `Portfolio conviction audit results (JSON):
${JSON.stringify(audits, null, 2)}

Write a ranked report:
1. FIRED TRIGGERS first — theses where a Conviction Trigger's condition is met but conviction was never changed (the most actionable). For each: ticker, trigger, current value, recommended /status.
2. OVER-CONVICTED — high conviction on thin/stale evidence. Ticker | conviction | why unsupported | recommended /status.
3. UNDER-CONVICTED — brief list.
Lead with the counts. Follow CLAUDE.md Writing Standards: tables over prose. These feed /status (this workflow never changes conviction itself).`,
  { phase: 'Rank', model: cfg.model || 'opus', effort: 'high' },
)

const persisted = []
if (cfg.persist && flagged.length) {
  phase('Persist')
  const res = await agent(
    `You are the SOLE writer. Append one _followups.md "## Open" entry per flagged thesis below, per the followups contract (newest first, one line each: the recommended /status action + trigger/reason). Do NOT modify any thesis or its conviction. Flagged (JSON):
${JSON.stringify(flagged.map((a) => ({ ticker: a.ticker, verdict: a.verdict, firedTriggers: a.firedTriggers, recommendedStatus: a.recommendedStatus })), null, 2)}
Report how many entries you wrote.`,
    { phase: 'Persist', model: cfg.model || 'opus' },
  )
  persisted.push(res)
}

return { tested: audits.length, flagged: flagged.length, report, persistedPaths: persisted }
