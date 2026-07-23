export const meta = {
  name: 'portfolio-stress-test',
  description: 'Adversarially stress-test every active/monitoring thesis, verify each weakness with independent skeptics, and rank the portfolio by confirmed downside risk.',
  whenToUse: 'Periodic portfolio-wide risk sweep. Heavy (one stress agent per thesis + up to 3 verifiers per at-risk name). Run deliberately, not routinely.',
  phases: [
    { title: 'Enumerate', detail: 'list in-scope theses from /Theses by status' },
    { title: 'Stress', detail: 'run stress-test SKILL.md Phases 1-3 per thesis, READ-ONLY (parallel, pipelined)' },
    { title: 'Verify', detail: 'independent skeptics try to refute each flagged weakness' },
    { title: 'Synthesize', detail: 'rank by confirmed severity into one consolidated report' },
    { title: 'Persist', detail: 'SEQUENTIAL single-writer: skill-faithful per-thesis notes + Log + _followups (persist:true only)' },
  ],
}

// ------------------------------------------------------------------ args (all optional)
//   tickers          : explicit ticker list to test (overrides status filter)
//   status           : status values to include        (default ['active','monitoring'])
//   limit            : cap number of theses tested      (default: no cap)
//   model            : model for stress/verify agents   (default 'sonnet' — affordable at scale)
//   severityToVerify : min severity 1-5 to trigger the verify pass (default 3)
//   persist          : true => SEQUENTIALLY write skill-faithful stress-test notes + Log + _followups for at-risk names (default false = read-only)
const cfg = args || {}
const STATUS = cfg.status || ['active', 'monitoring']
const MODEL = cfg.model || 'sonnet'
const SEV_VERIFY = cfg.severityToVerify || 3
const LIMIT = cfg.limit || null

// ------------------------------------------------------------------ schemas
const ENUM_SCHEMA = {
  type: 'object',
  properties: {
    theses: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          ticker: { type: 'string' },
          file: { type: 'string' },
          company: { type: 'string' },
          conviction: { type: 'string' },
          status: { type: 'string' },
        },
        required: ['ticker', 'file'],
      },
    },
  },
  required: ['theses'],
}

const STRESS_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    weakestPoints: { type: 'array', items: { type: 'string' } },
    breakingCatalysts: { type: 'array', items: { type: 'string' } },
    bearThesis: { type: 'string' },
    survivesScrutiny: { type: 'boolean' },
    severity: { type: 'integer' },              // 1 robust .. 5 thesis breaks
    recommendedAction: { type: 'string' },      // hold | monitor | trim | downgrade | close
    externalEvidence: { type: 'string' },       // performed | waived-high | skipped-med-low (skill Phase 2.5)
    shortCaseMarkdown: { type: 'string' },      // full Phase 3 short case — the deliverable the writer persists
  },
  required: ['ticker', 'severity', 'survivesScrutiny', 'weakestPoints', 'recommendedAction', 'shortCaseMarkdown'],
}

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    refuted: { type: 'boolean' },               // true => weakness rebutted (thesis defended)
    reasoning: { type: 'string' },
    residualRisk: { type: 'string' },
  },
  required: ['refuted', 'reasoning'],
}

// ------------------------------------------------------------------ Phase 1: enumerate scope
phase('Enumerate')
const enumPrompt = `List investment theses in the /Theses directory to stress-test.
Glob /Theses/*.md. For each, read the YAML frontmatter and return {ticker, file (repo-relative path like "Theses/AMD - Advanced Micro Devices.md"), company, conviction, status}.
${cfg.tickers
    ? `Include ONLY these tickers: ${cfg.tickers.join(', ')}.`
    : `Include ONLY theses whose status frontmatter is one of: ${STATUS.join(', ')}.`}
Return every match — do not sample, cap, or truncate.`
const enumerated = await agent(enumPrompt, { phase: 'Enumerate', schema: ENUM_SCHEMA, effort: 'low' })

let theses = enumerated && enumerated.theses ? enumerated.theses : []
if (LIMIT) theses = theses.slice(0, LIMIT)
log(`Enumerated ${theses.length} in-scope theses${LIMIT ? ` (capped at ${LIMIT})` : ''}`)
if (!theses.length) {
  return { error: 'no theses matched scope', scope: { status: STATUS, tickers: cfg.tickers || null } }
}

// ------------------------------------------------------------------ Phases 2+3: find -> verify (pipelined per thesis)
const results = await pipeline(
  theses,

  // Stage 1 — run the /stress-test skill's ANALYSIS (Phases 1-3) on one thesis, READ-ONLY.
  (t) => agent(
    `You are ONE of many parallel, READ-ONLY analysts stress-testing a portfolio. Stress-test a single thesis: ${t.ticker} (${t.company || ''}), file ${t.file}.

Read the skill spec at .claude/skills/stress-test/SKILL.md and follow its methodology for THIS thesis: Phase 1 (load thesis + all supporting evidence), Phase 2 (internal contradiction scan), Phase 2.4 (cluster-peer graph primer), Phase 2.6 (independent short-hypothesis draft, anti-anchoring), Phase 3 (build the short case). Honor its MANDATORY Mental Models reading gate and the READING PROTOCOL. Following the live SKILL.md is deliberate — it keeps this sweep identical to the single-name /stress-test and inherits its future edits.

CRITICAL — you are strictly READ-ONLY. Do NOT run the skill's Step 0 (no vault lock) and do NOT run its Phase 4 "Update the Vault": write NO manifest, NO snapshot, NO Research note, NO thesis Log entry, NO _followups.md, NO _hot.md. Produce ANALYSIS ONLY and RETURN it as data — a single downstream writer persists everything sequentially. This read-only rule is what stops the parallel analysts from racing on the shared _followups.md / _hot.md files.

Phase 2.5 (external evidence): to avoid portfolio-wide rate limits, issue AT MOST one small WebSearch batch, and only if the thesis looks genuinely fragile; otherwise stay vault-only. Record which in externalEvidence.

Return the full Phase 3 short case as markdown in shortCaseMarkdown, plus the structured ranking fields.`,
    { label: `stress:${t.ticker}`, phase: 'Stress', schema: STRESS_SCHEMA, model: MODEL },
  ),

  // Stage 2 — independent skeptics try to REFUTE the weakness (only for flagged names)
  (stress, t) => {
    if (!stress || stress.severity < SEV_VERIFY) {
      return { ...(stress || { ticker: t.ticker }), verified: false, confirmedSeverity: stress ? stress.severity : 0 }
    }
    const SKEPTICS = 3
    return parallel(Array.from({ length: SKEPTICS }, (_, i) => () =>
      agent(
        `A short-seller argues the ${t.ticker} thesis is at risk (severity ${stress.severity}/5). Their case:
${(stress.weakestPoints || []).map((w) => `- ${w}`).join('\n')}
Bear thesis: ${stress.bearThesis || '(see points above)'}
You are skeptic #${i + 1}. Try HARD to REFUTE this bear case — defend the thesis using ${t.file}, its Related Research, and current evidence. Set refuted=true ONLY if you can rebut the weakness with specific evidence; default refuted=false when the weakness genuinely holds. Note any residual risk.`,
        { label: `verify:${t.ticker}#${i + 1}`, phase: 'Verify', schema: VERIFY_SCHEMA, model: MODEL },
      ),
    )).then((votes) => {
      const v = votes.filter(Boolean)
      const rebutted = v.filter((x) => x.refuted).length
      // majority could NOT refute => weakness is real => keep full severity
      const survivesDefense = rebutted < Math.ceil(v.length / 2)
      return {
        ...stress,
        verified: true,
        skepticVotes: v.length,
        rebutted,
        confirmedSeverity: survivesDefense ? stress.severity : Math.max(1, stress.severity - 2),
        residualRisk: v.map((x) => x.residualRisk).filter(Boolean),
      }
    })
  },
)

const clean = results.filter(Boolean)

// ------------------------------------------------------------------ Phase 4: synthesize ONE consolidated report (compact)
phase('Synthesize')
const ranked = clean.slice().sort((a, b) => (b.confirmedSeverity || 0) - (a.confirmedSeverity || 0))
const atRisk = ranked.filter((r) => (r.confirmedSeverity || 0) >= SEV_VERIFY)
log(`${atRisk.length} of ${clean.length} theses at confirmed severity >= ${SEV_VERIFY}`)

// Feed the synthesizer a COMPACT projection only — never the full per-thesis short cases
// (N x long markdown would blow its context). Full short cases persist per-thesis below.
const rankedCompact = ranked.map((r) => ({
  ticker: r.ticker,
  severity: r.severity,
  confirmedSeverity: r.confirmedSeverity,
  action: r.recommendedAction,
  verified: !!r.verified,
  topWeakness: (r.weakestPoints || [])[0] || '',
}))

const synthPrompt = `Synthesize a portfolio stress-test from this compact ranking of ${clean.length} theses (severity 1-5 + verification):
${JSON.stringify(rankedCompact, null, 2)}

Produce ONE ranked portfolio-risk report:
1. Lead with the ${atRisk.length} theses at confirmed severity >= ${SEV_VERIFY} — each: single most-likely breaking weakness + recommended action.
2. Then a one-line-per-name table for the rest (ticker | severity | action).
Follow CLAUDE.md Writing Standards: lead with the number/insight, no hedge words, tables over prose.`
const report = await agent(synthPrompt, { phase: 'Synthesize', model: cfg.model || 'opus', effort: 'high' })

// ------------------------------------------------------------------ Phase 5: persist (SEQUENTIAL single-writer)
// Fan-out (Stress) was analysis-only. ALL writes happen here, ONE thesis at a time, so shared
// files (_followups.md, _hot.md) and per-thesis Logs never race — the whole point of the split.
const persisted = []
if (cfg.persist) {
  phase('Persist')
  const toWrite = atRisk.length ? atRisk : ranked.slice(0, 1)
  for (const r of toWrite) {                     // SEQUENTIAL await — do NOT parallelize writes
    const res = await agent(
      `You are the SOLE writer running right now, so writing vault files is safe. Persist the stress-test result for ${r.ticker} following .claude/skills/stress-test/SKILL.md Phase 4 ("Update the Vault") EXACTLY, using the PRE-COMPUTED short case below (do NOT re-run the analysis):

${r.shortCaseMarkdown || '(no short case captured — reconstruct a brief one from the thesis + ranking)'}

Per the skill's Phase 4: (1) write the stress-test Research note (Phase 4.1 format + its propagated_to atomicity); (2) append the thesis "## Log" entry (Phase 4.2, "Stress test:" prefix, <=2 lines); (3) add one _followups.md "## Open" entry per the followups contract. SKIP the per-thesis manifest and snapshot — this is a single batch run. Report the exact vault paths written.`,
      { label: `persist:${r.ticker}`, phase: 'Persist', model: cfg.model || 'opus' },
    )
    persisted.push({ ticker: r.ticker, result: res })
  }
  log(`Persisted ${persisted.length} skill-faithful stress-test note(s), sequentially`)
}

return {
  scope: { basis: cfg.tickers ? 'explicit tickers' : STATUS, tested: clean.length, verifyThreshold: SEV_VERIFY, persisted: cfg.persist ? persisted.length : 0 },
  atRiskCount: atRisk.length,
  ranked: rankedCompact,
  report,
  persistedPaths: persisted,
}
