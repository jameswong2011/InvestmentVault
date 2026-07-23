export const meta = {
  name: 'portfolio-retro',
  description: "Portfolio-scale retrospective (via the retro skill's method): fan out the per-ticker price/news/earnings overlay with throttled concurrency (fixes the ~126-query rate-limit that makes unscoped /retro return data-gap), then rank trade ideas by the narrative-price gap.",
  whenToUse: 'Full-portfolio retro without the WebSearch rate-limit. args.window = 1w|1m|1q (default 1w). Read-only unless persist:true.',
  phases: [
    { title: 'Universe', detail: 'run retro SKILL.md Step 0 + Phases 1-2 to get in-window active tickers' },
    { title: 'Overlay', detail: 'per-ticker price/news/earnings overlay, throttled (parallel)' },
    { title: 'Rank', detail: 'rank trade ideas by weighted narrative-price delta' },
    { title: 'Persist', detail: 'single-writer immutable note + Top-3 Log back-refs + _followups (persist:true)' },
  ],
}

const cfg = args || {}
const WINDOW = cfg.window || '1w'
const MODEL = cfg.model || 'sonnet'
const LIMIT = cfg.limit || null

const UNIVERSE_SCHEMA = {
  type: 'object',
  properties: {
    windowStart: { type: 'string' },
    today: { type: 'string' },
    tickers: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, file: { type: 'string' }, activity: { type: 'string' } }, required: ['ticker'] } },
  },
  required: ['tickers'],
}

const OVERLAY_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    priceMove: { type: 'string' },
    newsPolarity: { type: 'string' },
    earnings: { type: 'string' },
    delta: { type: 'string' },
    weight: { type: 'number' },
    stance: { type: 'string' },
  },
  required: ['ticker', 'delta'],
}

phase('Universe')
const universe = await agent(
  `Determine the retro ticker universe for window ${WINDOW}. Read the skill spec at .claude/skills/retro/SKILL.md and apply its Step 0 (window computation) + Phases 1-2 (activity-gated read + extraction) ONLY: find the tickers with in-window activity (addressed callouts + manual Log entries) across Theses/Sectors/Macro. READ-ONLY — no writes, no lock. Return windowStart, today, and tickers with {ticker, file, activity (one line on why in-window)}.`,
  { phase: 'Universe', schema: UNIVERSE_SCHEMA, model: cfg.model || 'opus', effort: 'high' },
)
let tickers = universe && universe.tickers ? universe.tickers : []
if (LIMIT) tickers = tickers.slice(0, LIMIT)
log(`Retro window ${WINDOW}: ${tickers.length} active tickers`)
if (!tickers.length) return { window: WINDOW, note: 'no in-window activity', report: 'No thesis activity in window — nothing to retro.' }

phase('Overlay')
const overlays = (await parallel(tickers.map((t) => () =>
  agent(
    `You are ONE of many parallel, READ-ONLY analysts running a retrospective overlay for ONE ticker: ${t.ticker} (file ${t.file || '?'}), window since ${universe.windowStart || WINDOW}.
Read the skill spec at .claude/skills/retro/SKILL.md and apply its Phase 3 (3-channel overlay: price action, newsflow polarity, earnings/transcript) + Phase 4 (narrative-price delta classification) for THIS ticker only, honoring its Mental Models gate. Issue at most ONE small WebSearch batch (you are one of many — do NOT burst; this is what avoids the rate-limit). READ-ONLY: no note, no Log, no _followups.
Return priceMove, newsPolarity, earnings, the delta class (aligned-up/aligned-down/inverted-bear/inverted-bull/flow-bull/flow-bear/unreactive-good/unreactive-bad/data-gap), the weight (0-2 per retro's scheme), and vault stance (alpha-harvest|missed-signal|stress-test-candidate).`,
    { label: `retro:${t.ticker}`, phase: 'Overlay', schema: OVERLAY_SCHEMA, model: MODEL },
  ),
))).filter(Boolean)
log(`Overlaid ${overlays.length} tickers`)

phase('Rank')
const ranked = overlays.slice().sort((a, b) => (b.weight || 0) - (a.weight || 0))
const report = await agent(
  `Portfolio retro, window ${WINDOW}. Per-ticker narrative-price overlays (JSON):
${JSON.stringify(ranked, null, 2)}

Produce the retro trade-ideas report per retro's ranking: lead with the highest narrative-price-gap names (inverted-bear/inverted-bull weighted 1.5x, unreactive weighted 2x). For each top idea: ticker | delta | what happened | vault stance (alpha-harvest / missed-signal / stress-test-candidate) | suggested follow-up skill. List any data-gap tickers separately (not signal). Follow CLAUDE.md Writing Standards: tables over prose, lead with the count.`,
  { phase: 'Rank', model: cfg.model || 'opus', effort: 'high' },
)

const persisted = []
if (cfg.persist) {
  phase('Persist')
  const res = await agent(
    `You are the SOLE writer. Persist this portfolio retro as retro's IMMUTABLE Research note (new file, never overwrite). Get date via \`date +%F\`. Path "Research/<date> - Portfolio Retro ${WINDOW} - retrospective.md" (source_type: retrospective, propagated_to: []). Then append a "Retro insight:" Log entry to each of the Top-3 trade-idea theses (non-skill-origin, <=2 lines), and add the top ideas to _followups.md "## Open". Do these writes ONE AT A TIME. Content:
${report}
Report the exact paths written.`,
    { phase: 'Persist', model: cfg.model || 'opus' },
  )
  persisted.push(res)
}

return { window: WINDOW, tickers: overlays.length, report, persistedPaths: persisted }
