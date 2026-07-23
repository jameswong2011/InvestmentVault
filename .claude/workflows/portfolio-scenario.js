export const meta = {
  name: 'portfolio-scenario',
  description: "Model a named macro event across the whole book in parallel (via the scenario skill's impact method): fan out per-thesis impact assessment, rank winners/losers + transmission channels, and (persist) write Major-impact Log entries + one scenario note.",
  whenToUse: 'Model a specific macro event ("Fed cuts 150bps", "Taiwan blockade") across all theses fast. Requires args.event. Read-only unless persist:true.',
  phases: [
    { title: 'Enumerate', detail: 'list in-scope theses' },
    { title: 'Assess', detail: 'run scenario SKILL.md impact method per thesis, READ-ONLY (parallel)' },
    { title: 'Synthesize', detail: 'winners/losers + second-order + Major/Minor/Neutral classification' },
    { title: 'Persist', detail: 'sequential single-writer: Major-impact Logs + one scenario note (persist:true)' },
  ],
}

const cfg = args || {}
const EVENT = cfg.event || cfg.scenario || null
const STATUS = cfg.status || ['active', 'monitoring']
const MODEL = cfg.model || 'sonnet'
const LIMIT = cfg.limit || null

if (!EVENT) return { error: 'portfolio-scenario needs an event. Pass args.event, e.g. {event:"Fed cuts 150bps by year-end"}.' }

const ENUM_SCHEMA = { type: 'object', properties: { theses: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, file: { type: 'string' }, company: { type: 'string' } }, required: ['ticker', 'file'] } } }, required: ['theses'] }

const IMPACT_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    impact: { type: 'string' },
    direction: { type: 'string' },
    magnitude: { type: 'string' },
    transmission: { type: 'string' },
    secondOrder: { type: 'string' },
  },
  required: ['ticker', 'impact', 'direction'],
}

phase('Enumerate')
const enumerated = await agent(
  `List theses in /Theses. Glob /Theses/*.md, read frontmatter, return {ticker, file (repo-relative), company} for every thesis whose status is one of: ${STATUS.join(', ')}. Return all matches, no cap.`,
  { phase: 'Enumerate', schema: ENUM_SCHEMA, effort: 'low' },
)
let theses = enumerated && enumerated.theses ? enumerated.theses : []
if (LIMIT) theses = theses.slice(0, LIMIT)
log(`Enumerated ${theses.length} theses for scenario: "${EVENT}"`)
if (!theses.length) return { error: 'no theses matched', status: STATUS }

phase('Assess')
const impacts = (await parallel(theses.map((t) => () =>
  agent(
    `You are ONE of many parallel, READ-ONLY analysts modeling a macro scenario across a portfolio.
SCENARIO / EVENT: ${EVENT}
Assess this event's impact on a single thesis: ${t.ticker} (${t.company || ''}), file ${t.file}.
Read the skill spec at .claude/skills/scenario/SKILL.md and apply its FORWARD-MODE per-thesis impact method (transmission channel, first- and second-order effects on THIS thesis), honoring its Mental Models gate. You are READ-ONLY: do NOT run its Phase 0 lock, its classification-approval gate, or any Phase 4+ writes (no Log entry, no research note, no _hot.md). RETURN the impact as data.
Classify impact major|minor|neutral, direction positive|negative|mixed, magnitude, the transmission channel, and the biggest second-order effect.`,
    { label: `scen:${t.ticker}`, phase: 'Assess', schema: IMPACT_SCHEMA, model: MODEL },
  ),
))).filter(Boolean)
log(`Assessed ${impacts.length} theses`)

phase('Synthesize')
const compact = impacts.map((m) => ({ ticker: m.ticker, impact: m.impact, dir: m.direction, mag: m.magnitude, via: m.transmission }))
const report = await agent(
  `Portfolio scenario: "${EVENT}". Per-thesis impact assessments (JSON):
${JSON.stringify(compact, null, 2)}

Produce the scenario report:
1. Classification table — Major / Minor / Neutral per thesis (this is the approval-gate content the user reviews before persisting).
2. Ranked WINNERS and LOSERS (by magnitude x direction), each with its transmission channel.
3. Second-order / cross-thesis effects and any natural hedges the event creates.
Lead with the counts (X Major, Y Minor). Follow CLAUDE.md Writing Standards: tables over prose.`,
  { phase: 'Synthesize', model: cfg.model || 'opus', effort: 'high' },
)

const persisted = []
if (cfg.persist) {
  phase('Persist')
  const majors = impacts.filter((m) => (m.impact || '').toLowerCase() === 'major')
  const res = await agent(
    `You are the SOLE writer (no other agent is running), so vault writes are safe. Persist this scenario per .claude/skills/scenario/SKILL.md Phase 4-6 output format, using the pre-computed results (do NOT re-run analysis). SCENARIO: ${EVENT}
1. Write ONE scenario Research note (source_type: scenario; get date via \`date +%F\`; path "Research/<date> - Scenario - <short label>.md") containing the classification + winners/losers below.
2. For each MAJOR-impact thesis, append a "## Log" entry (Scenario prefix per log-prefixes.md, <=2 lines) — do these ONE AT A TIME.
Majors: ${JSON.stringify(majors.map((m) => m.ticker))}
Report content:
${report}
Report the exact paths written.`,
    { phase: 'Persist', model: cfg.model || 'opus' },
  )
  persisted.push(res)
}

return { event: EVENT, tested: impacts.length, majors: impacts.filter((m) => (m.impact || '').toLowerCase() === 'major').length, report, persistedPaths: persisted }
