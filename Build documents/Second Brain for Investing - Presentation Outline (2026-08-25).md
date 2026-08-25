---
publish: false
date: 2026-08-25
tags: [meta, presentation, second-brain]
status: active
source: generated from Build documents + Website essays + vault state
---

# A Second Brain for Investing — presentation outline and speaker notes

Companion to `Build documents/Second Brain for Investing - Presentation (2026-08-25).pptx` (30 slides, 16:9). Each section below is one slide: on-slide text first, speaker notes second. Usable as an editing outline, or as the prompt pack for regenerating the deck in another tool.

## Slide 1 — A Second Brain for Investing

- OBSIDIAN NOTES + CLAUDE CODE
- What AI can do today, how investors use it, and how a research system that remembers is built.
- An overview for a beginner-to-intermediate audience
- Laniakea Partners  ·  Reo  ·  August 2026

> **Speaker notes:** Four parts: what a language model is and what it can do in 2026; how investors use AI today and which problems of a traditional research process it removes; what a second brain is and how ours is built; and six use cases from our own book. Parts one and two are general; the vault only appears from part three.

## Slide 2 — Four parts, one argument  `Agenda`

- AGENDA
- 01
- What AI is, and what it can do today
- A model in one sentence · the capability ladder · where it still fails
- 02
- How AI is used in investing today
- Adoption · where it sits in the workflow · the problems it solves
- 03
- Inside a second brain
- What it is · how the notes link · context files, mental models, templates, skills · the sensing layer
- 04
- Use cases and the features that matter
- Six use cases from our own book · the eight features that carry the return
- The argument: the model is stateless; a research system is not. The return comes from the system, not the model.

> **Speaker notes:** If time is short, parts three and four carry the content; one and two are context.

## Slide 3 — What AI is, and what it can do today  `Part 1`

- 01
- A language model in one sentence, and the three properties that matter
- The capability ladder: chat → long documents → tools → agents → systems
- What it does well, and where it fails without help

> **Speaker notes:** Deliberately non-technical. Three properties to carry into the rest of the talk: the model reads and writes at a professional level; it is stateless; and it is probabilistic.

## Slide 4 — A language model, in one sentence  `Part 1`

- PART 1 · WHAT AI IS
- A model trained on most of the written internet to predict the next word. The side effect is a general-purpose reader and writer that follows instructions.
- In
- Your question, plus whatever files and rules you put in front of it
- The model
- Predicts the next word, thousands of times, using everything in the window
- Out
- Text, code, a table, or a decision about which tool to use next
- Reads and writes at a professional level
- Summarises, drafts, extracts, compares and reasons across long documents.
- Stateless
- Remembers nothing between sessions unless it is written down and handed back to it.
- Probabilistic
- The same question gets a slightly different answer each time. Without a procedure, the shape of the work drifts.

> **Speaker notes:** The first property is why it is useful at all. The second and third are why a chat window does not become a research system on its own: the model does not know your positions, does not remember yesterday, and will not do the same thing the same way twice unless told exactly how.

## Slide 5 — The capability ladder, 2022 to 2026  `Part 1`

- PART 1 · WHAT AI IS
- 1 · Chat   2022
- Answers questions from what it learnt in training. Impressive, unreliable, forgetful.
- 2 · Long context   2024
- Reads a million tokens, about 2,500 pages, in one prompt: whole filings, whole books.
- 3 · Tools   2024–25
- Browses the web, runs code, reads and writes files, calls data APIs. Computes instead of guessing.
- 4 · Agents   2025–26
- Plans and executes multi-step jobs over minutes or hours; checks its own work; asks when blocked.
- 5 · Systems   2026
- Agents on schedules, teams of agents that verify each other, rules enforced outside the model.
- Each rung is a capability the rung below lacked. Most investment use is still on rung 1.

> **Speaker notes:** Rung two removed the 'it cannot read the whole document' objection. Rung three removed 'it makes up numbers' for anything computable. Rungs four and five are what make an always-on research system possible: the model can be given a job and a schedule rather than a question.

## Slide 6 — What it does well, and where it fails without help  `Part 1`

- PART 1 · WHAT AI IS
- Does well
- Reads a 100-page filing or a two-hour transcript in seconds
- Extracts structured data from messy text
- Drafts in a house style once shown the style
- Writes and runs code, so arithmetic is computed rather than guessed
- Runs multi-step jobs across many files and reports what it touched
- Fails without help
- Knows nothing about your positions unless told
- Forgets everything between sessions
- States wrong facts fluently, with no built-in doubt
- Drifts: the same request gives a differently shaped answer tomorrow
- Overwrites where it should append; fills gaps with plausible invention
- None of the right-hand failures is fixed by a better model. They are fixed by what surrounds it: memory, sources, written procedure and rules enforced outside the model.

> **Speaker notes:** The left column is why every fund now uses it. The right column is why most of that use stays at 'summarise this'. Part three is about the surrounding machinery that fixes the right-hand column.

## Slide 7 — How AI is used in investing today, and what it fixes  `Part 2`

- 02
- Adoption is mainstream; systems are not
- Where AI sits in the research workflow, and what stays human
- The problems of the manual process, and why a chat window does not solve them

> **Speaker notes:** Adoption numbers show the industry already uses the tools; the rest of the section argues the use is shallow, and names the problems a system, as opposed to a chat window, removes.

## Slide 8 — Adoption is mainstream; systems are not  `Part 2`

- PART 2 · AI IN INVESTING TODAY
- 95%
- of fund managers use generative AI in their work, up from 86% in 2023
- AIMA
- 70%
- of buy-side firms use AI to support the front office
- SimCorp InvestOps 2026
- 55%
- of hedge funds have integrated it into the investment process
- Barclays Hedge Fund Outlook 2026
- 58%
- expect to increase use in investment processes next year, up from 20% in 2023
- AIMA
- Most of that use is a chat window: summarise this, draft that, explain this filing.
- It saves reading time. It does not remember what was read, connect it to the positions held, or notice when a new datapoint contradicts an old claim.

> **Speaker notes:** Sources: AIMA front-office GenAI research (95%, 58%); SimCorp InvestOps Report 2026 (70%); Barclays 2026 Hedge Fund Outlook (55%). Adoption is no longer the differentiator; almost everyone has the model.

## Slide 9 — Where AI sits in the research workflow today  `Part 2`

- PART 2 · AI IN INVESTING TODAY
| Stage | What AI does today | What stays human |
|---|---|---|
| Sense | Scans news, filings and social media at volume; scores and clusters what is new | Picks the few stories that matter |
| Read | Summarises transcripts and reports; extracts figures from filings | Decides what the source changes |
| File | Structures the note, cross-links it, updates the affected positions | Corrects the draft |
| Analyse | Drafts bull and bear cases, runs a short-seller pass, models a scenario across a portfolio | Judges the argument |
| Decide | Recommends, with as much force as the evidence supports | Every conviction and sizing decision |
| Review | Overlays what was written against what the price did | Acts, or declines to act, on the gap |
- Sensing is constant and cheap; judgement stays scheduled and human.

> **Speaker notes:** The pattern is the same at every stage: the machine does the reading, filing and first-draft analysis at volume; the analyst does the choosing and the deciding. A system can recommend a downgrade; it should never execute one.

## Slide 10 — The problems it solves over a manual process  `Part 2`

- PART 2 · AI IN INVESTING TODAY
| Problem | Manual process | With a research system |
|---|---|---|
| The firehose | Thousands of items a day; a handful matter; finding them costs the morning | Scored, clustered, and tied to the positions held before the day starts |
| Reading is not filing | Insight stays in the reader's head; cross-references decay within weeks | Every source becomes a structured note, filed where it changes a claim |
| Blind spots across positions | Nobody holds fifty theses in their head; shared assumptions go unexamined | The whole portfolio's research can be searched, and diffed against itself |
| Falsifiers never written down | Positions defended out of loyalty two years in | Raise / cut / close conditions written in advance and tested on every datapoint |
| Hierarchy compresses evidence | Analyst → sector head → PM: three hops and several weeks | Evidence, thesis and falsifier live in one place, read whole |
| Nothing compounds | Context rebuilt every morning, discarded every night | Knowledge written back and cited months later |

> **Speaker notes:** Six failure modes of qualitative research at scale, whether the analyst is one person or a floor. One, two and six are about volume and memory; three and four are about discipline; five is institutional.

## Slide 11 — Chat is not a research system  `Part 2`

- PART 2 · AI IN INVESTING TODAY
|  | Chat window | Search over your files | Compiled research wiki |
|---|---|---|---|
| Memory between sessions | None | An index; nothing is learnt | Written back into the notes |
| Cross-references | None | None | Built at write time, kept current |
| Contradictions | Unflagged | Unflagged | Checked every time a source is filed |
| Audit trail | None | None | Dated, append-only log per position |
- Compilation, not retrieval.
- Andrej Karpathy's 'LLM wiki' pattern (April 2026): the model compiles raw sources into a persistent, interlinked body of notes, built once and kept current rather than re-derived on every question. The note-taking app is the IDE, the model is the programmer, the wiki is the codebase.

> **Speaker notes:** Retrieval fetches fragments at question time and nothing accumulates. Compilation does the cross-referencing and contradiction-checking at write time, so every later question is cheap. The analyst chooses the sources and makes the calls; the model keeps the notes current.

## Slide 12 — Inside a second brain: our own system  `Part 3`

- 03
- What a second brain is: a compiled, interlinked wiki that the model maintains
- How the notes link, and how the model finds its context
- Context files, mental models, templates, skills, and the overnight sensing layer

> **Speaker notes:** From here on, everything shown is our own research system, running on our own book today: 97 theses, 53 sector maps, 12 macro frameworks and 376 research notes, maintained by a language model under a fixed schema.

## Slide 13 — What a second brain is  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
- A persistent, interlinked body of notes that the model maintains, sitting between us and the raw sources. Knowledge is compiled once, cross-referenced when it is written, and kept current, rather than re-derived on every question.
| Layer | Contents | Who writes it |
|---|---|---|
| Raw sources | Inbox deposits, overnight news and X sweeps, market data, our own objections in the margins | The world and us. The model never modifies a source |
| The wiki | 97 theses, 53 sector maps, 12 macro frameworks, 376 research notes, plus the state files: session memory, dependency graph, follow-up register, catalyst calendar | The model, through named skills |
| The schema | A rulebook, four note templates, the skill specifications | Us, rarely |
- Sources are immutable, so provenance survives every rewrite above them. The schema keeps a thousand machine-written files structurally identical, which is what makes them readable as a set rather than one at a time.

> **Speaker notes:** The three layers and who may write to which is the whole discipline. Sources are never edited, so every claim can be traced back. The wiki is what the model maintains. The schema is ours and changes rarely; because every note follows it, the model can treat 97 theses as one dataset rather than 97 documents.

## Slide 14 — Everything is linked: how the model finds its context  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
- Thesis · NVDA
- 15 sections: insights, triggers, bull, bear, log
- Mental Models
- which lenses fired, held as hypotheses
- _graph.md
- compiles every link: 1,926 edges, one block per name
- Research notes · 106 linked
- Related Research and Log entries cite the note that changed the view
- Peer theses · 7
- names that share a mechanism: Broadcom, SanDisk, Lumentum, Palantir…
- Sector maps · 3
- industry history, competitive dynamics, product analysis, investor heuristics
- Macro notes · 5
- AI capex sustainability, 800VDC, AI supply and demand to 2030…
- When the model opens a thesis it follows the links: the evidence behind each claim, the sector context, the macro exposures, the peers that share a mechanism. Its answer is grounded in the book's own evidence rather than generic training knowledge, and a new datapoint finds the handful of files it touches in seconds instead of a scan of 1,500. About 9,700 wikilinks hold the book together.

> **Speaker notes:** This is the mechanism that turns a folder of notes into a second brain. Every note points at its neighbours with wikilinks: a research note names the theses it changes; a thesis lists its research, its sector map and its macro exposures; a sector map lists its theses. A script compiles all of it into a dependency graph the model reads first, so it knows which five files matter for a datapoint. Ask which theses rest on HBM supply and the answer arrives with the file list to verify it against.

## Slide 15 — The four pieces  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
- You
- the analyst
- OBSIDIAN  ·  the viewer
- Claudian plugin
- a chat panel inside Obsidian
- The vault
- ~1,500 plain markdown files: theses, research, sectors, macro, mental models, state files
- The asset. Everything else is replaceable.
- Claude Code
- the engine: reads and writes files, runs scripts, browses, follows the skills
- Overnight pipelines
- news, X, prices, calendar
- The world
- web · filings · market data · X · transcripts
- Obsidian shows the files. Claude Code reads and writes them. The pipelines feed a scanning folder, never the spine. You sit in the loop at the chat panel.

> **Speaker notes:** Obsidian is a free note-taking app that shows a folder of plain-text files; the vault is that folder. Claude Code is Anthropic's agent runtime: a program that reads and edits files, runs scripts and browses. The Claudian plugin puts it inside Obsidian with the vault as its working directory. Nothing here is proprietary infrastructure; the files are the asset.

## Slide 16 — Five ingredients in every prompt  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
- 1
- Typed command
- What you type in the box. Different every time; the only part most people call 'the prompt'.
- You, each time
- 2
- Conversation history
- Everything said earlier in the session. Comes free with the model.
- Free, uncontrolled
- 3
- Context files
- The model's memory and rulebook. Written once, read at the start of every session.
- You, written once
- 4
- Templates
- The shape the answer must take. The model cannot skip the bear case, because the bear case is a section.
- You, written once
- 5
- Skills
- Named procedures the model follows step by step: ingest, propagate, stress-test.
- You, written once
- Prompt quality is mostly what the model already knows before you type. Ingredients 3, 4 and 5 are where the work goes, and they compound.

> **Speaker notes:** The typed command is one of five inputs and usually the smallest. Context files supply memory and rules, templates the shape, skills the procedure. All three are written once and used every session after.

## Slide 17 — Context files and mental models: what it knows before you type  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
| File | What it holds | Why it matters |
|---|---|---|
| CLAUDE.md | The rulebook: vault structure, writing standards, decision rules. Loaded every session. | Every answer inherits the house rules |
| _hot.md | Session memory: active thread, latest sync, recent conviction changes, open questions. | The model resumes mid-thread, not from zero |
| _graph.md | Dependency map: 1,926 edges linking each thesis to sectors, peers and evidence. | Knows which five files matter, instead of re-reading 97 |
| _followups.md | Findings that demand action: stress-test flags, fired triggers. | Nothing auto-forgets; entries leave only when resolved |
| Mental Models/ | The strategy's codified lenses: generalist frames, industry models, cross-sector lenses. | The house edge applied on every pass, not when we remember |
- The mental models are read before any analysis, as lenses and questions, never conclusions. When every lens likes the same name, that is the cue to argue the other side. Learn a mechanism once, write it in, and it shapes everything analysed after.

> **Speaker notes:** This is what the model reads before it reads the user's question. The follow-ups register exists because a stress-test recommendation once dropped out of session memory before anyone acted on it. The mental-models folder is where the strategy itself compounds.

## Slide 18 — Templates and skills: judgement into procedure  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
- Templates fix the anatomy of an argument
- Thesis: 15 fixed sections, one per ticker.  Each non-consensus insight must name the consensus it disputes, the observable that would confirm it and the datapoint that would falsify it
- Conviction triggers  → HIGH if · → LOW if · → CLOSE if, written before we hold a settled view
- Log  append-only, dated, two lines per entry
- Research note: 4 sections.  Thesis Delta first, Contradiction Check mandatory, source locked at creation
- Skills are specifications, not prompts
- Pre-flight checks → method → write discipline → a report of every file touched
- 27 skills: the core loop, building, analytical, diagnostic and publishing families
- Same command, same shape of output, whatever the model's mood; plain text you can open and read
- 8 workflows fan one skill across every thesis at once; findings are attacked by sceptic agents before we see them; none may touch a conviction
- The machine cannot produce a thesis without a bear case, because the bear case is a section. 97 identical skeletons can be diffed; 97 bespoke documents cannot.

> **Speaker notes:** Templates put the discipline in the file rather than in the prompt. Skills are written procedures the model must follow, so the same command behaves the same way, and when it misbehaves you edit the file. The daily loop uses four of them: ingest, sync, status, graph.

## Slide 19 — The most powerful skills  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
| Skill | What it does | From the book |
|---|---|---|
| /ingest → /sync | Turns any source into a research note that leads with the thesis delta, then fans it into every affected thesis, sector and macro note | 21 Aug: one deep-dive, four theses updated in one pass |
| /stress-test | A short-seller pass on one thesis; reads our objections first; idiosyncratic risk before sector risk | Cloudflare, 10 Jul: high → medium the next day |
| /scenario | A hypothetical traced through the whole book: transmission channels, winners, losers, theses missing a line | Iran ground invasion, 23 Apr: 11 major impacts named |
| /transcript | Diffs an earnings call against the thesis: what moved, hedging shifts, tone of the Q&A | Six holdings, 29 May: three headline numbers corrected |
| /compare | Two names side by side on shared adjacency: pricing power, balance sheet, the forced choice | NBIS vs CRWV, 4 Aug: better balance sheet vs better operating machine |
| /surface | What are we missing: decayed theses, open questions, names held without a thesis | 13 Aug: a live holding with no thesis note |
| /retro | The week's research against price action; narrative-price gaps ranked as trade ideas | 24 May: AMD +10% the week the vault turned high; a coverage gap surfaced |
| /catalyst | Every dated event across the book, read jointly | 26 Jul: 34 earnings in 14 days, treated as one event |
- Also: /deepen fills one thin section; /brief writes the one-page memo; /status is the human gate on every conviction change.

> **Speaker notes:** Eight skills carry most of the value. The first row is the daily loop. Stress-test and scenario are the adversarial pair. Transcript and compare are the earnings-season and competitive tools. Surface, retro and catalyst are the ones that look across the whole book rather than at one name.

## Slide 20 — The overnight sensing layer  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
| When | Pipeline | What we see at 07:35 |
|---|---|---|
| 07:00 | News sweep: ~6,800 items read, deduplicated, scored, clustered | A morning brief by theme, top stories on the phone |
| 07:30 | Catalyst reminders parsed from the calendar | Alerts at T-2 and T-0 for every dated event |
| 07:35 | Price tripwires against pre-set levels | An alert that quotes the thesis trigger it threatens |
| 08:30 | X harvest: cashtags derived from the theses | A divergence section: where the crowd disagrees with us |
- What it caught
- Early August: a divergence flag on Uber became a full thesis reassessment the same week
- Mid August: the crowd's bull case on a memory name rested on an out-year commitment our thesis did not engage; a gap in our own argument
- Late July: 34 earnings dates inside 14 days, 20 in four days with the FOMC; treated as one correlated event, not 34 reads
- Nothing from this layer enters the book by itself. The pipelines write only into a scanning folder; we pick the one to three stories that matter and ingest them. Running cost: $20–35 a month.

> **Speaker notes:** By 07:30 the vault has read about 6,800 items and kept a couple of hundred. Sensing is cheap and constant; judgement is scarce and human-scheduled, and the divergence flags are where the first is allowed to summon the second. The whole layer is governed from one file of tables in Obsidian.

## Slide 21 — Why context beats clever prompting  `Part 3`

- PART 3 · INSIDE A SECOND BRAIN
- The same question, typed into both:  “What did this morning's news actually touch?”
- Bare model
- A tidy summary of the headlines
- No idea which names we hold or why
- Cannot say which claim in which thesis changed
- Gone by tomorrow; the context has to be rebuilt
- Vault-loaded model
- Reads session memory, the scored brief and the dependency graph first
- Names the four theses touched, and why each
- Tests each story against the thesis's own conviction triggers
- Appends a dated log entry per thesis, linked to the source
- Same model. The difference is what it already knew, and what it was allowed to write.

> **Speaker notes:** The question is trivial; the difference in the answers is entirely the surrounding context and procedure. The right-hand column is what this morning's propagation run did with a new macro note.

## Slide 22 — Use cases from our own book, and the features that matter  `Part 4`

- 04
- The daily loop, earnings season, and a scenario through the whole book
- The system argues back, and we argue in the margins
- Asking the book questions, and the eight features that carry the return

> **Speaker notes:** Every example is a real run from our vault, with dates.

## Slide 23 — Use case 1 · From 6,798 items to four thesis updates  `Part 4`

- PART 4 · USE CASES
- Fetched overnight
- 6,798
- New (not seen before)
- 3,635
- Admitted after triage
- 281
- Stories after clustering
- 226
- Ingested by hand
- 1–3 stories, chosen by us
- One morning brief, 15 August 2026. Nothing from the overnight layer enters the book by itself; the sensing stays wide and the spine stays curated.
- 21 Aug · source
- A subscriber deep-dive on Marvell arrives by email
- /ingest → research note
- Leads with what changed for the thesis; tests the datapoint against the pre-registered triggers: touched, not fired
- /sync → four theses
- Dated log entries in Marvell, Nvidia, SK Hynix and Broadcom, each linking back to the note; conviction unchanged on all four
- By the time we have read a source, the book already reflects it everywhere it matters.

> **Speaker notes:** Left: the funnel from one real morning brief. Right: one real source going through the loop. The research note leads with what changed for the position; propagation fans the delta into every thesis it touches with a two-line dated log entry that links back to the note, so the evidence chain is one click away.

## Slide 24 — Use case 2 · Earnings season: transcripts read against the thesis  `Part 4`

- PART 4 · USE CASES
- 29 May 2026: about 24 transcripts, the latest four quarters for six holdings, pulled and diffed against what each thesis said management would say.
| Name | Verdict | Most material finding |
|---|---|---|
| Murata | Confirmed, reality ahead | FY27 operating profit guided +35% on data-centre mix; the thesis modelled less |
| Vicor | Numbers hold; framing overstated | 'Rubin' said zero times in four calls; new licensing deals paused to 2027 |
| Aehr | Numbers hold; one claim overstated | CEO: 'most ASICs are not burnt-in'; an adoption curve, not a mandate |
| Ajinomoto | ABF confirmed; food framing wrong | The food segment is improving, not the drag the thesis described |
| Advantest | Case intact; three specifics wrong | '10k systems by 2028' was annual capacity, not installed base; share 66%, not 95% |
| Aixtron | Mix-shift confirmed; guide misquoted | FY26 guide is €520M, 'slightly down', not the raise the thesis claimed |
- No thesis broken; three headline numbers corrected before they were used in sizing. The recurring pattern: 'AI-necessity' framing consistently outruns what management will actually say.

> **Speaker notes:** The transcript procedure exists to keep our written case honest against what management actually said. The exercise found no broken thesis but six specific corrections, and one pattern worth generalising: our theses tended to frame our companies' products as economically forced when management described adoption as early. On earnings day a single-name version of this runs within the hour of the call.

## Slide 25 — Use case 3 · What if? A scenario through the whole book  `Part 4`

- PART 4 · USE CASES
- 23 Apr 2026 · /scenario
- Iran ceasefire collapses; US ground invasion in May
- Brent $120–150; Strait of Hormuz 20–40% disrupted
- VIX 40+; equity risk premium +150–200bp; rupee −5 to −10%
- Ten transmission channels traced: oil, shipping, rates, dollar, India, defence, cyber, LNG…
- Probability ~5–10% over six months; the asymmetric payoff justifies the preparation
| Major impact | Thesis | Channel |
|---|---|---|
| Negative | Opendoor | Oil-driven inflation → mortgage rates +100bp → housing transactions collapse |
| Negative | Vail Resorts · Take-Two | Gasoline and sentiment shock; a binary game launch into a recession |
| Negative | Reliance · Edelweiss | India's 85% oil-import dependence, rupee pressure, IPO timing |
| Positive | Cheniere · Scorpio Tankers | Sustained LNG premium; Hormuz closure sends tanker rates past $100k/day |
| Positive | Cameco | Energy sovereignty: nuclear is the only non-chokepoint baseload |
| Positive | CrowdStrike · Palo Alto · Palantir | Cyber retaliation and defence procurement pull-forward |
- Eleven major-impact theses received a dated log entry; the positions whose theses lacked a line for the scenario were named.

> **Speaker notes:** A scenario run takes a hypothetical with explicit parameters and traces it through every thesis via named transmission channels, ranking winners and losers and, most usefully, listing the theses that have no sentence covering the event. A portfolio-scale version fans the same method across all 97 theses in parallel.

## Slide 26 — Use case 4 · The system argues back  `Part 4`

- PART 4 · USE CASES
- 10 Jul 2026
- Stress test on Cloudflare
- A short-seller pass on a name we held at HIGH: the growth leg the premium rested on had no disclosed revenue, a rival had cloned it for free, and the stock sat at the consensus target at ~200x earnings. 3 of 7 bull assumptions rated red.
- 11 Jul 2026
- Downgrade, executed by us
- The recommendation passed through the confirmation gate and conviction went high → medium: log entry appended, sector map and session memory updated.
- 15 Aug 2026
- Six flags waiting in the register
- Six later stress tests each name the conviction change they are waiting on. They stay open until actioned or dismissed; nothing auto-evicts.
- At book scale.  A July sweep found the same unexamined assumption about software moats sitting identically in five semiconductor theses. One finding, five corrections, and a class of groupthink made visible because the book is uniform enough to be diffed against itself.

> **Speaker notes:** The boundary is the point of the timeline: the machine produced the short case and the recommendation on the 10th; a human executed the downgrade on the 11th. 'Tested against the triggers, none fired' is also logged with a date, so a position's history is a record of survived falsification attempts.

## Slide 27 — Use case 5 · Arguing in the margins  `Part 4`

- PART 4 · USE CASES
- [!question] 2026-06-10 → Addressed 2026-06-10
- Prompt: How much of the early 2026 price hike comes from passing through input costs vs. genuine pricing power given shortages?
- Response: Mostly pricing power. The input is ~15–20% of cost, so a 20–30% supplier hike explains ~3–6 points of a 20–40% price rise; gross margin expanded through the hike. Full decomposition in §Industry Context.
- From the Elite Material thesis; four such exchanges addressed in one session.
- How it works
- A hotkey drops a typed objection at the exact paragraph it concerns
- 'Address fresh callouts' sends the model back through them: it rewrites the body, then records our wording verbatim with a dated reply
- The body is the deliverable; the callout is the ledger
- Four error callouts on one name in a month reads as conviction drift
- Most of the book's text is machine-drafted. Every disagreement we have ever had with the machine is preserved next to the claim it concerned.

> **Speaker notes:** Delegation without losing the argument: read a machine-drafted section, drop a callout at the sentence you disagree with, ask for the callouts to be addressed. The analysis lands in the note's spine; the margin keeps a three-sentence record and a pointer.

## Slide 28 — Use case 6 · Asking the book questions  `Part 4`

- PART 4 · USE CASES
| Question | Skill | What comes back |
|---|---|---|
| What must be true for this thesis to work? | /assumptions | The load-bearing claims, each with its falsifier, and where the thesis argues against itself |
| What does the bull case actually rest on? | /dependency-map | Key customers, inputs, technology transitions, single points of failure |
| What macro bet are we secretly making? | /macro-exposure | The implicit macro variables the position is levered to, with direction and size |
| Where does the company sit in its chain? | /value-chain | Who it buys from and sells to; where the bottleneck and pricing power sit |
| Is our stated conviction still earned? | /conviction-audit | Whether the evidence matches the label, and whether a trigger has fired unactioned |
- Or just ask, in plain English
- “Which of my bull cases share an implicit macro dependency? Am I double-counting diversification?”
- “Read my macro note on 800VDC. Which thesis is most exposed to a risk I haven't written down?”
- “Which theses rest on HBM supply? Where does one supplier appear across the book?”
- Answers arrive in minutes with the file list to verify them against, because the cross-referencing was done when the notes were written. A portfolio-scale version of each question fans out across all 97 theses; findings are attacked by sceptic agents before we see them.

> **Speaker notes:** This is the payoff of the wiki structure from part three. Because every note is structurally identical and already linked to its sectors, macro exposures, peers and evidence, cross-sectional questions that used to cost an afternoon cost minutes. Five read-only diagnostics turn the common ones into one-command routines; free-form questions work just as well.

## Slide 29 — The eight features that carry the return  `Part 4`

- PART 4 · USE CASES
- 1
- Compilation, not retrieval
- Knowledge written back into the notes; March's insight cited in September.
- 2
- Interlinked context
- Every note knows its neighbours; a datapoint finds the handful of files it touches.
- 3
- Pre-registered triggers
- Raise / cut / close conditions written before the market has an opinion.
- 4
- Propagation
- One source updates every affected note in one pass, with dated log entries.
- 5
- Adversarial procedures
- Stress tests, scenarios and sweeps whose purpose is to attack the book they maintain.
- 6
- A register that never forgets
- Findings that demand action persist until resolved.
- 7
- Callouts
- Disagreement preserved next to the claim it concerned.
- 8
- The sensing layer
- Thousands of items a night reduced to a brief; divergence flags against the crowd.
- None of them is the model. All of them are what surrounds it.

> **Speaker notes:** If the audience remembers one slide, this is it. Roughly ranked by contribution to the return. None of the eight is the model; every one is machinery around the model.

## Slide 30 — The model is stateless.

- We choose the sources, drop the objections and take every conviction decision. The machinery holds the memory, the reconciliation and the standing instruction to disagree.
- To start:  Obsidian (free), a Claude subscription and a cloned folder of markdown; 30–45 minutes for the core, the overnight layer optional. First thesis immediately; compounding shows up around thesis five or six. The pattern generalises beyond stocks: legal research, literature review, competitive intelligence.
- laniakea.io/system  ·  leo@laniakea.io
- Pattern: Andrej Karpathy's LLM wiki (April 2026)

> **Speaker notes:** Close on the one-line argument. Questions usually go to cost, hallucination risk and 'do I need to be a programmer': the core runs on a laptop with two free-or-subscription tools; hallucination is contained structurally (locked sources, contradiction checks, stress tests) and you remain the analyst; no programming is needed for the core, only for the optional overnight layer.
