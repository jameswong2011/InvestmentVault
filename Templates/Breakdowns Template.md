---
publish: true
date: {{date}}
tags: [template, thesis-breakdown, video-script]
status: active
source: vault synthesis + incremental web research
---

# Breakdowns Template

Use this prompt to create or refresh an audience-calibrated bilingual video series for a **value chain / theme** (chain), a **single company carrying a full arc** (flagship), or a **short company profile** (profile). **Each run writes one date-prefixed Markdown file containing the series plan, English scripts, Mandarin Chinese translations, and bilingual video metadata.** It never creates a subfolder or separate episode notes. These are entertainment/broadcast videos built on existing research — topical selection, not IC coverage.

## How to use this template

### Pick the series type first

| series_type | Use when | source_note | Episodes |
|---|---|---|---|
| **chain** | The story is a stack or theme — several covered companies each own a layer (packaging war, memory supercycle, datacenter power) | Sector or Macro & Technology note | 8–12 |
| **flagship** | One recognizable company can carry a full arc alone | Thesis | 10–15 |
| **profile** | One niche name — "which layer does it own, why does it win it, what breaks it" | Thesis (+ optional `parent_series` chain breakdown) | 1–3 |

### What the two blocks do

- **Editable inputs** are the controls for a specific run: series type, subject, file date, episode count, angle, runtime, languages, and mode. Change these values each run.
- **Execution instructions** are the reusable method the LLM follows: internal-note research, web refresh, series design, script rules, output format, and validation. Normally leave this block unchanged.

You do **not** need to paste the execution instructions into chat when the LLM can read this workspace. Reference this template and provide only the input overrides.

### HeyGen production prompt — paste above one video script

Replace the bracketed fields — pulling the video title, series text, and thumbnail hook from whichever language (English or Mandarin) matches the script you are about to paste, and attaching a reference photo of yourself if the selected HeyGen avatar is not already your own likeness — then paste one completed English or Mandarin script between the markers.

```text
Create one polished presenter-led video from the exact script below.

VIDEO SETUP
Format: 9:16 portrait
Video title: [PASTE THE HEYGEN VIDEO TITLE IN THE SAME LANGUAGE AS THE SCRIPT BELOW — TICKER OR TOPIC NAME ONLY]
Series text: [PASTE THE HEYGEN SERIES TEXT IN THE SAME LANGUAGE AS THE SCRIPT BELOW]
Thumbnail hook: [PASTE THE THUMBNAIL HOOK IN THE SAME LANGUAGE AS THE SCRIPT BELOW]
Brand style: natural video-call aesthetic with one fixed neutral presenter background; opening cut-in uses a dark neutral card with a photo of the presenter’s real face, white text, and one accent colour — the same real likeness used in the exported thumbnail, never a stock or generic face

PRODUCTION REQUIREMENTS
- Speak only the text between SCRIPT START and SCRIPT END. Do not rewrite, summarise, pad, or add claims, greetings, disclaimers, calls to action, or teasers.
- Use the selected avatar and voice. After the opening cut-in, keep the presenter in one continuous video-call-style medium shot: static camera, direct eye contact with natural periodic blinking (roughly every 3-5 seconds, varied not metronomic, never a fixed unblinking stare), natural webcam framing, one unchanged background, consistent lighting, calm delivery, restrained gestures, clear pronunciation, and pacing matched to the script.
- The only graphic insert or non-presenter shot allowed is a clean two-second opening cut-in showing a photo of the presenter’s real face plus the exact video title, exact series text, and exact thumbnail hook, all three in the same language as the script. Use the presenter’s real likeness only — the attached reference photo, or the same identity as the selected avatar — never a stock, generic, or newly generated face. Keep all four elements inside safe margins. Cut once from this opening card to the presenter.
- After that single opening cut, never cut away from the presenter. Do not add B-roll, stock footage, charts, diagrams, product shots, screenshots, animations, graphic cutscenes, split screens, picture-in-picture, scene changes, background changes, camera-angle changes, zooms, pans, transitions, or full-screen text.
- Treat every company, product, number, analogy, and event mentioned in the script as spoken content only, never as a cue to generate an illustrative visual or cutaway.
- Apart from burned-in captions, show no text after the opening cut-in. Do not add the publishing title, series title, episode title, ticker expansion, slogan, persistent badge, lower third, callout, statistic overlay, or any other copy.
- Add accurate rolling burned-in captions in the script’s language: high contrast, sentence case, no more than two lines, and never covering the presenter’s face.
- Synchronise captions at word level. Keep all caption text white except the word currently being spoken — or the current natural word token in Mandarin — which uses the same accent colour as the opening cut-in. Move the accent highlight word by word with the audio; highlight only one word/token at a time. Use colour only, with no bounce, scaling, background box, glow, or other caption animation.
- End on the script’s final line with no generated outro or end card unless the script contains one.

THUMBNAIL
- Create a separate cover image matching the selected video format: the presenter’s real face (the attached reference photo, or the same identity as the selected avatar — never a stock, generic, or newly generated face) plus one subject-relevant visual, the exact thumbnail hook, exact video title, and exact series text, all three in the same language as the paired video.
- Use one focal point, strong contrast, large mobile-readable hook text, safe margins, and no other claims or copy.
- If a separate thumbnail cannot be exported, use this design as the opening frame and return the exact still-image prompt needed to recreate it in HeyGen’s Image Generator — the still-image prompt must explicitly specify the presenter’s real likeness, not a generated face.

DELIVERABLES
1. Final 1080p video.
2. Separate thumbnail/cover image, or the fallback still-image prompt.

[SCRIPT START — SPEAK ONLY THE TEXT BELOW]

[PASTE VIDEO SCRIPT HERE]

[SCRIPT END]
```

### Recommended workflows

Copy a block, edit the required values, and delete any optional chunk you do not want to override.

#### New series

```text
Use [[Templates/Breakdowns Template]] with these inputs:
# REQUIRED
mode: full-series
series_type: chain # chain | flagship | profile
subject: "<theme, TICKER, or company>"
source_note: "<sector/macro note for chain; thesis for flagship/profile>"

# CHAIN ONLY — delete for flagship/profile
profiled_companies: [<tickers in rough episode order>]

# PROFILE ONLY — delete for chain/flagship
parent_series: "<existing chain breakdown>"

# OPTIONAL ANALYSIS CONTROLS — delete this chunk to use defaults
archetype: auto # auto | cyclical | compounder | chain | macro-vehicle
temperature: balanced # bearish | balanced | bullish
complexity: beginner # illiterate | beginner | intermediate
episode_count: auto # auto | integer
target_runtime: 1.5-2.5 minutes

# OPTIONAL EDITORIAL OVERRIDES — delete this chunk if unused
core_question: "<question the series should resolve>"
angle_overrides: ["<emphasis or per-episode runtime override>"]
must_include: ["<topic, source, risk, or question>"]
must_avoid: ["<topic, framing, jargon, or claim>"]

# OPTIONAL FORMAT CONTROLS — delete this chunk to use defaults
series_title: auto # auto | "<custom series title>"
disclaimer_delivery: description-only # description-only | spoken-finale | none
intro_outro: series-branded # series-branded | none
mandarin_variant: Simplified Chinese # Simplified Chinese | Traditional Chinese
hashtags_per_video: 3-5 # appended to each language's description; episode-specific, not generic boilerplate
heygen_video_title: auto # recognizable ticker or topic name only; fixed across the series; generated in both English and Mandarin (identical unless a standard Chinese name is more natural)
thumbnail_hook_length: 3-7 English words # Mandarin hook is a natural transcreation targeting roughly 6-12 Chinese characters, not a literal translation
```

#### Existing series

```text
Use [[Templates/Breakdowns Template]] with these inputs:
# REQUIRED
mode: refresh-episodes # next-episode | refresh-episodes | replan-series
subject: "<theme, TICKER, or company>"
episodes_requested: 6,10,15 # next | all | 3,5,8 | 6-10
as_of_date: today

# OPTIONAL ANALYSIS CONTROLS — delete this chunk to retain the existing settings
archetype: auto # auto | cyclical | compounder | chain | macro-vehicle
temperature: balanced # bearish | balanced | bullish
complexity: beginner # illiterate | beginner | intermediate
episode_count: auto # auto | integer
target_runtime: 1.5-2.5 minutes

# OPTIONAL EDITORIAL OVERRIDES — delete this chunk if unused
core_question: "<replacement question>"
angle_overrides: ["<emphasis or per-episode runtime override>"]
must_include: ["<topic, source, risk, or question>"]
must_avoid: ["<topic, framing, jargon, or claim>"]

# OPTIONAL FORMAT CONTROLS — delete this chunk to retain the existing settings
disclaimer_delivery: description-only # description-only | spoken-finale | none
intro_outro: series-branded # series-branded | none
mandarin_variant: Simplified Chinese # Simplified Chinese | Traditional Chinese
hashtags_per_video: 3-5 # appended to each language's description; episode-specific, not generic boilerplate
heygen_video_title: auto # recognizable ticker or topic name only; fixed across the series; generated in both English and Mandarin (identical unless a standard Chinese name is more natural)
thumbnail_hook_length: 3-7 English words # Mandarin hook is a natural transcreation targeting roughly 6-12 Chinese characters, not a literal translation
```

### Alternative workflow

You may edit the **Editable inputs** block below and ask, "Run [[Templates/Breakdowns Template]]." This mutates the master template, so the override-in-chat method above is cleaner for repeated use.

## Editable inputs — change these for each run

```yaml
mode: full-series # full-series | next-episode | refresh-episodes | replan-series
series_type: chain # chain | flagship | profile — pick explicitly per the selector table
archetype: auto # auto | cyclical | compounder | chain | macro-vehicle
temperature: balanced # editorial analysis tilt, not model randomness: bearish | balanced | bullish
subject: "<theme, TICKER, or company>"
source_note: "<internal note path — sector/macro note for chain, thesis for flagship/profile>"
profiled_companies: [] # chain only: covered tickers profiled per layer, rough episode order
parent_series: "<optional — existing chain breakdown a profile extends>"
series_title: auto # auto-generates "<Company> Stock Breakdown", "<Company> Investment Case", or "<Theme> Breakdown"; string overrides
episode_count: auto # chain 8-12 | flagship 10-15 | profile 1-3; integer overrides
episodes_requested: all # all | next | 3,5,8 | 6-10
complexity: beginner # illiterate | beginner | intermediate; internal control, never an audience-facing label
audience: general investor # complexity sets assumed knowledge and analytical depth
target_runtime: 1.5-2.5 minutes # default per episode; NO upper cap for genuinely topical episodes — set longer runtimes here or per episode via angle_overrides
spoken_wpm: 140
cadence: one video every 3 days
tone: conversational, calm, direct, concise, plain English
presenter_format: one continuous video-call-style presenter shot after a single two-second opening title cut-in; no B-roll, graphics, or further cuts
freshness_window_days: 45
as_of_date: today
file_date: today # used in the filename when the series is first created
geography_or_listing: "<optional>"
core_question: "<optional; chain series default to the source note's key questions>"
angle_overrides:
  - "<optional emphasis, or per-episode runtime overrides>"
must_include:
  - "<optional topic, source, risk, or question>"
must_avoid:
  - "<optional topic, framing, jargon, or claim>"
disclaimer_delivery: description-only # description-only | spoken-finale | none
intro_outro: series-branded # series-branded | none — series-position greeting + follow/like outro in both languages, wording varied every episode (rules in STEP 5)
languages: [English, Mandarin Chinese]
mandarin_variant: Simplified Chinese # zh-CN; ask explicitly for Traditional Chinese if preferred
translation_style: natural, concise spoken Mandarin; meaning-preserving; similar runtime
video_title_style: concise, specific, non-clickbait
video_description_length: 50-90 English words (prefer 50-65), excluding hashtags, plus a concise Mandarin translation
hashtags_per_video: 3-5 # separate final line in each description; tailored to that episode's actual subject and claim
heygen_video_title: auto # recognizable ticker or topic name only; fixed across the series; generated in both English and Mandarin (identical unless a standard Chinese name is more natural, e.g. SK海力士)
heygen_series_text: "Series X of Y" # English format, e.g. "Series 3 of 14"; Mandarin uses "第X集，共Y集", e.g. "第3集，共14集"
thumbnail_hook_length: 3-7 English words # Mandarin hook is a natural transcreation targeting roughly 6-12 Chinese characters, not a literal translation
output_root: "Thesis Breakdowns"
output_filename: auto # "YYYY-MM-DD - <Subject>.md"; profile files append " - Profile"
```

## Execution instructions — normally leave unchanged

```text
Create or update a short-form investment-breakdown series using the inputs above.
Merge chat overrides into the Editable inputs; unspecified fields keep template defaults.

OBJECTIVE
Turn existing research plus an incremental current-web check into audience-calibrated bilingual spoken scripts — English original plus natural Mandarin translation per episode, with bilingual publishing metadata and three ready-to-paste HeyGen text elements per video. This is broadcast content built on institutional research: choose the episodes a curious viewer wants, not the coverage an investment committee requires. Every episode is a complete standalone product; the sequence moves from understanding the subject to debating the investment case. The arc comes from topic selection and ordering, never from spoken handoffs, teasers, or cliffhangers — the sole exception is the sanctioned intro/outro framing blocks when intro_outro: series-branded. Maximise information density in both languages: every sentence must add a fact, mechanism, inference, counterpoint, or conclusion. Generate the complete requested set — full scripts, not outlines — unless mode says next-episode, refresh-episodes, or replan-series.

STEP 1 — PREFLIGHT AND INTERNAL-RESEARCH-FIRST WORK
1. Get the actual current date; never infer it from note dates.
2. Read source_note in full. Chain series: the sector/macro note's key questions seed core_question and its structure seeds the map; also read the thesis of every profiled company. Flagship/profile: read the thesis in full, then the most decision-relevant linked notes. Resolve the subject against Theses/, Sectors/, Research/, Macro & Technology/, _hot.md, and _graph.md; never treat _graph.md as a substitute for reading source notes.
3. Read [[Mental Models/Generalist - Overview]] and the relevant industry/lens notes. Apply them as questions, not conclusions. Run the base rate against the thesis and state the single falsifying datapoint.
4. Read the subject's rows in _watchers.md and _catalyst.md — these are the canonical observables; the series Watchlist cites them rather than reinventing them.
5. Check Thesis Breakdowns/ for the subject's existing file (ongoing modes read it in full before editing) AND scan other series' "concepts owned" lines in their Narrative Rails, so shared concepts are not re-taught deeply here.
6. Do not alter theses, sector notes, macro notes, Research notes, _watchers.md, or _catalyst.md. If web research contradicts an internal note, record the conflict in the Evidence Ledger and flag it to the user; never edit source notes from this template.

STEP 2 — INCREMENTAL WEB RESEARCH
1. Browse for changes since the newest internal material and within freshness_window_days, in this order: (a) company filings, IR, earnings, product/engineering releases; (b) customer and competitor primary sources; (c) regulators, standards bodies, high-quality industry data; (d) reputable reporting and trade publications; (e) social or thematic chatter only to identify current questions, sentiment, or framing — never as proof. Chain series: run the check per profiled company, scaled to its episode weight.
2. Classify every candidate claim: VERIFIED FACT, INDUSTRY ESTIMATE, MANAGEMENT CLAIM, MARKET CHATTER, or ANALYTICAL INFERENCE.
3. Compare web findings with internal research. Surface conflicts explicitly; prefer the fresher primary source, but preserve the disagreement when the fact remains unsettled.
4. Add a dated hook only where it changes the explanation, stakes, or timing. If nothing material changed, say "No material freshness update" in production notes.
5. Every episode gets a non-spoken Sources section with 2-6 decision-relevant links and an as-of date. No citations in the spoken flow.

STEP 3 — SERIES DESIGN BY TYPE AND ARCHETYPE
Episode budgets: chain 8-12, flagship 10-15, profile 1-3. Choose the count by information density and topicality — do not stretch a thin subject, compress a dense one, or cover internal material that is not topical. Skipping non-topical internal content is correct, not a gap.

archetype: auto resolves as — chain series → chain; commodity/asset subjects with no operating company → macro-vehicle; companies classified per [[Mental Models/Industry - Semiconductors]] #13 where applicable (true cyclical or semi-cyclical → cyclical; structural compounder → compounder). State the classification in the series preamble as a hypothesis; a good series may argue it.

Four-act spine as rails, not a rigid table: ACT I — UNDERSTAND · ACT II — ECONOMICS & COMPETITION · ACT III — VARIANT & QUESTIONS · ACT IV — DECIDE. Archetype, temperature, and complexity adjust the emphasis.

TEMPERATURE CONTROL — editorial analysis tilt, not model sampling randomness:
- balanced (default): allocate comparable analytical weight to upside and downside; steelman both; let the evidence determine the synthesis.
- bearish: foreground fragility, adverse base rates, competitive pressure, supply response, expectations risk, failure modes, and disconfirming evidence. Retain the strongest bullish evidence and catalysts; do not force a negative verdict.
- bullish: foreground durability, pricing power, moat evidence, growth runway, optionality, catalysts, and potentially underappreciated upside. Retain the strongest bearish evidence and failure modes; do not force a positive verdict.
- Temperature may change episode selection, ordering, titles, hooks, and airtime. It never changes facts, evidence classification, uncertainty, material counterevidence, or the evidence-weighted conclusion. It never creates a recommendation or price target. If the evidence contradicts the requested tilt, say so.

COMPLEXITY CONTROL — assumed knowledge, vocabulary, and analytical scope:
- illiterate: internal setting name only; never print this label in audience-facing text. Assume no investing, accounting, or industry knowledge. Use the lower end of the episode budget. Spend most airtime on what the company sells, why customers buy it, who pays, how revenue and profit are made, the simplest industry map, main competitors, and one plain-language risk. Use everyday words and concrete examples. Avoid technical terms; when one is unavoidable, define it immediately before using it again. Avoid unexplained acronyms. Market positioning, valuation, variant perception, capital allocation, complex cycle signals, and full bull/bear debates are optional and usually omitted. Current news appears only when it helps explain the business. The goal is basic understanding, not complete analytical coverage.
- beginner (default): assume no company-specific knowledge but basic familiarity with revenue, profit, shares, and competition. Explain the business and mechanism before discussing pricing power, market expectations, variant perception, risks, and the bull/bear debate. Define sector terms on first use. Split airtime between understanding the business and understanding the investment debate.
- intermediate: assume the business model and broad industry structure are already understood. Compress basic context to the minimum needed for standalone viewing. Concentrate on live market debates, non-consensus insights, outstanding questions, expectations embedded in the price, competitive inflections, catalysts, and the most decision-relevant current web news. Use sector terminology when standard; define only obscure or company-specific terms.
- Interaction rule: complexity decides which subjects and vocabulary are appropriate; temperature decides emphasis within that scope. An illiterate-bearish run explains simple business fragilities rather than importing unexplained valuation or market-structure commentary. Evidence integrity overrides both controls.

The standard four-act spine applies to beginner and intermediate runs. Intermediate compresses Act I and expands Acts III–IV. Illiterate uses a simpler spine: WHAT IT DOES · WHO BUYS · HOW IT MAKES MONEY · WHAT COULD HELP OR HURT.

Analytical coverage for beginner and intermediate (every archetype; illiterate uses the simplified coverage above):
- Subject and why now.
- Product/technology or causal mechanism explained for a beginner.
- Where pricing power or value capture sits.
- EXPECTATIONS EPISODE: what the current price already assumes, positioning/crowding where observable, and the single variable the market is most likely mispricing. Never a price target — the episode teaches the gap between a good business and a good investment.
- At least one variant-perception episode and one adversarial episode.
- Outstanding questions with observable answers.
- Bull case, bear case, and a finale debate with an evidence-weighted synthesis and the 1-2 observables that decide it.

Archetype-specific mandatory coverage for beginner and intermediate (on top of the analytical coverage above):
- cyclical: cycle mechanics and the base rate of prior cycles; where in the cycle the evidence says we are; the price second derivative as a watchlist item; capital-response tracking (capex vs demand durability).
- compounder: moat type and durability tested against its named failure mode; ROIIC and reinvestment runway in beginner terms; management quality and capital-allocation record (mandatory here, optional elsewhere).
- chain: the stack-map episode first (name every layer and who owns it); layer economics (who takes margin and why); bottleneck migration (where scarcity moves next and what architecture shift moves it); which layer the market misprices.
- macro-vehicle: what actually drives the price (mechanism, not narrative); regime identification and what would end the regime; what is priced in; flows/positioning as an evidence class.

Profiles (1-3 episodes) answer exactly: which layer does this company own, why does it win that layer, and what breaks it. Restate the minimum parent-chain context in one self-contained sentence; never mention the parent series, a prior episode, or another video, and never re-teach the full concept.

The subject decides episode titles and order. Merge overlapping roles; split only when one episode would carry more than one core claim. Variant perception and unresolved questions sit between the overview and finale, not appended as an afterthought.

STEP 4 — STANDALONE + ARC + CROSS-SERIES CONTRACT
STANDALONE TEST — a first-time viewer can answer: what is this episode about; why does it matter to the investment case; what evidence or mechanism supports the claim; what could make it wrong.
STANDALONE CLOSE TEST — the final 1-2 spoken sentences answer the opening hook and deliver a complete takeaway. The final sentence is declarative, not a question, invitation, promise, or unresolved handoff. A viewer who never watches another video must still receive the full analytical payoff.
NO-HANDOFF RULE — no spoken script may mention, preview, or depend on another episode, video, part, or instalment. Forbidden handoffs include "next episode," "next video," "in part X," "we'll cover/explore/see," "that leads to the next question," "come back/follow to find out," "stay tuned," and Mandarin equivalents such as "下一集", "下期", "下一个视频", "下次我们", "敬请期待", or "关注后续". A genuine unresolved investment question may remain only if this episode also states the current best answer and the observable that would resolve it; it cannot be used as a teaser.
ARC TEST — a returning viewer gets one new analytical layer without a recap. The arc lives in the Series Map, episode selection, and ordering — not in spoken continuity. A recurring fact may be restated in one sentence without calling it a callback or referring to earlier coverage.
Within a series: no duplicate hooks, analogies, or conclusions; reuse a statistic in at most 3 episodes, and only when it does a different analytical job each time.
Across series: a shared concept (HBM, EUV, CoWoS, the memory cycle) is taught deeply in exactly one series; every other series uses a one-sentence version and gets on with its own claim. Record what this series owns vs borrows in Narrative Rails.

STEP 5 — SCRIPT CONTRACT
Write both language versions for one presenter speaking to camera.

PUBLIC-FACING SOURCE-NEUTRALITY RULE — applies to the series preamble, Evidence Ledger commentary, Watchlist commentary, titles, descriptions, scripts, and Production Notes:
- Never mention the internal research system or use phrases such as "the vault," "vault research," "vault estimate," "our vault," or Mandarin equivalents such as “资料库研究” and “知识库研究”. Never mention Obsidian.
- State facts, mechanisms, and conclusions directly. Do not add attribution filler such as "according to our research," "per our analysis," "our opinion is," “根据我们的研究”, or “我们认为” when the sentence works without it.
- Attribution is allowed only when it changes epistemic meaning. Use the shortest accurate form: a named source for a reported fact or estimate ("the company reported," "TrendForce estimates") or one concise analytical marker ("our estimate," "our view"; “我们的估计”, “我们的观点”). Do not repeat the marker. Use "the market recognises" only for observable consensus or pricing, never as a generic substitute.
- Internal-note wikilinks belong only in non-spoken Sources sections under the neutral label "Internal Sources". They never appear in titles, descriptions, scripts, or other audience-facing prose.

INTRO/OUTRO BLOCKS — applies when intro_outro: series-branded (default); skip entirely when none:
- Opening line: a short greeting stating the series position. Episode 1 uses a series-launch framing ("over the next few weeks I'm breaking down one of the most consequential companies of our era — <subject>"). Later episodes state the video number and series subject ("welcome back — video five in the series on <subject>").
- Closing line: a follow/like call-to-action referencing the series ("follow the channel or like this video to see more of this series").
- Write both blocks in both languages with meaning parity.
- Vary the wording of every intro and every outro across the series — no two episodes reuse the same phrasing in either language; rotate the greeting, the ordinal form, and the call-to-action structure.
- These blocks are the ONLY sanctioned exception to the no-handoff and declarative-ending rules. The analytical takeaway still lands immediately before the outro, and script interiors still never reference other episodes.
- Intro and outro words/characters count toward the episode's runtime band.

English script:
- Default 210-350 spoken words per episode at about 140 wpm. Use the shortest complete script; standard episodes should usually land near 210-280 words rather than fill the range. target_runtime governs: genuinely topical episodes may run long with NO upper cap, but every extra minute must carry new evidence or mechanism. Never pad to reach a duration or word count. Flag long-form episodes as topical in production notes.
- Lead with the insight or tension in the first sentence after any sanctioned intro block; no other greetings or throat-clearing.
- Maximise information density: every sentence adds a fact, mechanism, inference, counterpoint, or conclusion. Cut scene-setting, audience-address, rhetorical scaffolding, duplicate explanation, and transitions that carry no analytical content.
- Use direct subject-verb-object sentences, concrete nouns, and strong verbs. Minimise fillers such as "basically," "essentially," "actually," "really," "just," "in other words," "the key thing is," "what this means is," "it is important to note," "interestingly," "let us look at," "here is the thing," "at the end of the day," and "to be clear." Keep one only when removing it changes meaning or spoken clarity.
- Short spoken sentences, contractions, plain English. Complexity governs vocabulary: illiterate uses at most one essential new technical term and avoids acronyms where an ordinary phrase works; beginner defines every sector term on first use and uses at most two new acronyms; intermediate may use standard sector terms but defines obscure ones. Max one analogy per episode.
- One episode = one core claim. Use 1-3 supporting facts, then the strongest counterpoint.
- Explain numbers by meaning, not by reading a table aloud. Number density follows complexity: illiterate uses only 0-2 essential, easy-to-interpret numbers; beginner usually uses 1-3; intermediate uses the decision-relevant figures needed to test the debate. Never add numbers to satisfy a quota.
- Distinguish fact from estimate with the shortest necessary label: "the company reported" or "TrendForce estimates." State analytical conclusions directly when context is clear; otherwise use one brief marker such as "our estimate" or "our view."
- No hype, certainty theatre, price targets, or personalised recommendations. The bull case is never the narrator's verdict; the finale's evidence-weighted classification is allowed and must name its falsifiers.
- No citations, stage directions, or markdown links inside the spoken script.
- Finish the analytical body with a declarative, self-contained answer to the opening hook, followed only by the sanctioned outro when intro_outro: series-branded. Beyond these blocks, no question, teaser, invitation, or promise of later coverage; never mention another episode, video, or part — including in the finale.

Mandarin Chinese script:
- Use concise, natural spoken Mandarin in Simplified Chinese (zh-CN), not literal translation syntax. Match the selected complexity: simplify or retain technical vocabulary to the same degree as English, and never introduce a harder Chinese term than the English script requires.
- Maximise information density. Prefer short clauses, direct verbs, and compact Chinese phrasing; omit repeated subjects and pronouns when the meaning stays clear. Do not mirror English rhetorical scaffolding sentence by sentence.
- Minimise fillers such as “那么”、“其实”、“基本上”、“可以说”、“值得注意的是”、“需要指出的是”、“换句话说”、“大家可以看到”、“从某种程度上说”、“总的来说” and “接下来”. Keep one only when it changes meaning, emphasis, or spoken clarity.
- Preserve the English script's thesis, facts, numbers, dates, uncertainty labels, counterpoint, and conclusion. Do not add or remove an investment claim.
- Explain or transliterate company names and technical terms naturally on first use; retain standard English acronyms (HBM, DRAM, NAND, GPU) where a Chinese investor expects them.
- Match the episode's English runtime using the shortest complete translation. At the default runtime, estimate about 250 Chinese characters per minute and target roughly 375-625 characters; scale proportionally for long-form episodes. Never expand Mandarin to mirror the English sentence count or reach a character quota.
- Translate the meaning of analogies rather than their exact wording when a direct translation sounds unnatural.
- Apply the same standalone-close and no-handoff rules in Mandarin. The final Mandarin sentence must be a declarative takeaway, never a cross-video teaser or forward-looking question.
- Apply the same source-neutrality rule in Mandarin. Prefer direct statements; use “我们的估计” or “我们的观点” only when needed to stop an inference being mistaken for fact.
- Parity check: every number, named company, causal claim, counterpoint, and falsifier in English has an equivalent in Mandarin.

Series, video, and production-text naming — automatic:
- Resolve `series_title: auto` once before scripting and keep it unchanged across every episode. Use the recognizable company name rather than its note filename.
- Company-led educational or business-model arcs default to **“<Company> Stock Breakdown”**. Thesis-led arcs centred on expectations, catalysts, bull/bear evidence, and investability default to **“<Company> Investment Case”**. Chain, sector, macro, and technology subjects default to **“<Theme> Breakdown”**. Vary the formula only when the result is awkward or misleading.
- Generate a natural Mandarin series title with the same meaning. Neither language uses hype, dates, episode numbers, or unexplained tickers in the series title.
- Generate each episode’s English video title from that episode’s actual core claim or live debate, then write a natural meaning-equivalent Mandarin title. Do not reuse the series title as the episode title, prepend “Episode X,” or use generic labels such as “Overview” when a specific content-led title is available.

HeyGen production text — mandatory and distinct from publishing titles:
- Generate exactly three bilingual field pairs per episode — English and Mandarin: `HeyGen video title`, `HeyGen series text`, and `Thumbnail hook`. Only the field pair matching a given video's script language is pasted into that video's HeyGen prompt; never mix languages within one opening cut-in or thumbnail.
- `HeyGen video title` is only the recognizable ticker or topic name, with no episode title, company expansion, series title, punctuation, or other copy. Resolve it once and keep it identical across the series. Prefer a widely recognized ticker for a listed company (`NVDA`, `TSMC`); otherwise use the shortest recognizable topic or company name (`SK hynix`, `Advanced Packaging`). The Mandarin field (`HeyGen 视频标题（简体中文）`) uses the identical string unless a standard Chinese name is more recognizable to a Mandarin audience (e.g. `SK海力士` for SK hynix); tickers never translate.
- `HeyGen series text` uses the exact format `Series X of Y`, populated with that episode number and the final episode count. Do not add the series name or repeat the ticker/topic. The Mandarin field (`HeyGen 系列文字（简体中文）`) uses the exact format `第X集，共Y集` with the same two numbers and the same restriction.
- `Thumbnail hook` is a specific 3-7-word English phrase derived from that episode's core tension, mechanism, or conclusion. Count whitespace-delimited words; hyphenated compounds count as one. Make it mobile-readable, complementary to the publishing title, and understandable without another episode. It may be a concise question when the episode answers it. The Mandarin field (`缩略图钩子（简体中文）`) is a natural transcreation of the same tension, not a literal translation, targeting roughly 6-12 Chinese characters; equally mobile-readable, complementary to the Mandarin publishing title, and understandable without another episode.
- Neither language's hook may introduce an unsupported claim, price target, recommendation, hype, generic curiosity bait, episode number, series name, or call to action. Do not pad the English hook with articles merely to reach three words, or the Mandarin hook merely to reach the character target. Each video's HeyGen prompt opening cut-in may display only its own language's video title, series text, and thumbnail hook as on-screen text, plus a photo of the presenter's real face, apart from burned-in captions.

Video title and description — mandatory bilingual publishing metadata:
- Every episode must contain four non-empty metadata fields: an English title, a Mandarin title, an English video description, and a Mandarin video description. Never omit the Mandarin title or description.
- Write a concise, specific, standalone, non-clickbait English title and a natural Simplified-Chinese title. The Mandarin title should read as native Chinese publishing copy, not a literal word-for-word translation, while preserving the same core claim.
- Write an English description of 50-90 words and a meaning-equivalent Mandarin description. Use the shortest complete version, usually 50-65 English words. Both descriptions must independently state what the viewer will learn and the live debate. The Mandarin description must repeat any educational disclaimer in Chinese; it cannot rely on the English description for context.
- Append `hashtags_per_video` relevant hashtags on a separate final line of each language's description. Hashtags do not count toward the description word limit. Select them from the episode's actual content: prioritize one recognizable subject/company/ticker tag, one tag for the episode's distinct claim or mechanism, and one sector/theme tag; use the remaining slots only for genuinely useful discovery terms.
- Tailor the set episode by episode rather than repeating series boilerplate. At least two hashtags must reflect that episode's distinct content. Use readable PascalCase for multi-word English tags, no spaces or punctuation inside a tag, no duplicates or near-duplicates, and no spam or hype tags such as `#FYP`, `#Viral`, or `#GuaranteedReturns`. Mandarin tags should express the same discovery intent naturally while retaining widely recognized Latin-script company, ticker, or technical tags when clearer.
- Use direct, compressed sentences with no promotional filler. Both descriptions must stand alone and cannot preview or refer viewers to another instalment. Do not include personal ownership or position statements in titles, descriptions, scripts, or Production Notes.
- Titles and descriptions are publishing metadata, not part of the spoken runtime.

Internal rhythm (adapt, never label in speech): cold open 1-2 sentences → minimum context 2-4 sentences → core mechanism and evidence → counterweight → complete takeaway and declarative standalone close. No sentence exists only to connect these beats.

STEP 6 — OUTPUT STRUCTURE
Create or update exactly one file:

Thesis Breakdowns/YYYY-MM-DD - <Subject>.md   (profiles: "YYYY-MM-DD - <Subject> - Profile.md")

Use file_date for the prefix at creation. Ongoing modes locate and update the existing dated file — never create a new dated copy or rename because the refresh date changed. No subfolders, no per-episode notes.

Single-file requirements:
- Frontmatter: date, tags, status, series_type, series_title, series_title_zh, archetype, temperature, complexity, subject, source_note, profiled_companies (chain), parent_series (profile), as_of, episode_count, languages, mandarin_variant, source. Use neutral source wording such as "internal analysis + incremental web research"; never expose the internal research system.
- Display `**Series title:**` and `**系列名称（简体中文）:**` immediately below frontmatter, followed by the one-sentence series promise, the investment question the arc resolves, and the archetype classification stated as a hypothesis. Record temperature and complexity in frontmatter and Narrative Rails, but never call the audience "illiterate" outside frontmatter/internal Production Notes.
- ## Series Map — table: #, act, episode/title, standalone question, role in arc, current hook, status, last refreshed. Episode titles are headings inside this file, not wikilinks to separate notes.
- ## Narrative Rails — temperature and complexity choices, the intro_outro setting, repeated-context rule, standalone/arc balance, the no-spoken-handoff rule and its intro/outro exemption, the bilingual concision/no-filler rule, the public-facing source-neutrality rule, disclaimer placement, and concepts this series owns vs borrows.
- ## Evidence Ledger — verified facts, estimates, management claims, chatter, and open conflicts (including internal-vs-web conflicts flagged for the user). Must contain every load-bearing claim: any claim whose correction would force an episode re-record.
- ## Watchlist — observable, expected window, source, bull reading, bear reading, episodes affected, registry ref (_watchers.md row / _catalyst.md entry, or "NEW — candidate watcher row" for the user to add; never edit the registries from this template).
- ## Scripts — every episode in sequence, exact hierarchy:

  ### Episode 01 — <Title>
  **Series role:** ...
  **Standalone promise:** ...
  **Freshness hook:** ...
  **Suggested video title:** <automatically generated from this episode's core claim or debate>
  **建议视频标题（简体中文）:** ...
  **HeyGen video title:** <ticker or topic name only; fixed across the series>
  **HeyGen 视频标题（简体中文）:** <identical, or the standard Chinese name if more recognizable; fixed across the series>
  **HeyGen series text:** Series <X> of <Y>
  **HeyGen 系列文字（简体中文）:** 第<X>集，共<Y>集
  **Thumbnail hook:** <3-7 words specific to this episode>
  **缩略图钩子（简体中文）:** <natural Mandarin transcreation specific to this episode>

  #### Video Description
  <English publishing description>

  <3-5 episode-specific English hashtags on one line>

  #### 视频简介（简体中文）
  <Mandarin publishing description>

  <3-5 episode-specific Mandarin/discovery-standard hashtags on one line>

  #### English Script
  <English spoken words only>

  #### 中文脚本（普通话，简体）
  <Mandarin spoken script only>

  #### Production Notes
  <English and Mandarin runtime estimates, static video-call framing, opening-card layout, word-level caption timing and accent-highlight check, pronunciation, educational disclaimer, standalone-close check, bilingual concision check, freshness classification, topical/long-form flag where used; never propose B-roll, graphics, or cutaways>

  #### Sources
  <internal-note wikilinks and direct web links; label internal links neutrally>

  #### Episode Revision Log
  <append-only dated changes>

- ## Series Sources — use `### Internal Sources` and `### Web Sources`; never label internal material with audience-facing system language.
- ## Series Revision Log — append-only, at the end.
- Keep all scripts, production notes, sources, and revision history inside this one file.

STEP 7 — MODE-SPECIFIC BEHAVIOUR
- full-series: design the arc and write the map, bilingual publishing metadata, all three bilingual HeyGen production-text field pairs, and every complete English/Mandarin script into one new dated file — the complete set in one pass, so flow and content placement can be reviewed together.
- next-episode: refresh the web, read the existing dated breakdown, append the next unpublished bilingual episode section to the same file, and update its map and Series Revision Log.
- refresh-episodes: re-check only facts that can have changed; revise the named English scripts, Mandarin translations, four bilingual publishing fields, and three bilingual HeyGen production-text field pairs in the same file. When an English title, description, or episode angle changes, update its Mandarin counterpart, both hashtag sets, and both language hooks in the same run; preserve each episode's core role unless evidence forces a replan; append what changed to each Episode Revision Log.
- replan-series: preserve existing script sections, rewrite the map in the same file showing old → new ordering, and identify which episode sections need revision before changing them.
- Toggle persistence: ongoing modes retain the file's existing temperature and complexity unless the user overrides them. A changed complexity normally triggers replan-series because it changes topic scope and vocabulary; a changed temperature requires reweighting the map and affected scripts without changing evidence.

STEP 8 — QUALITY GATE
Before finishing:
1. Validate controls: temperature is bearish, balanced, or bullish (default balanced); complexity is illiterate, beginner, or intermediate (default beginner). Store both in frontmatter and Narrative Rails.
2. English word counts match target_runtime using the shortest complete version. Long-form episodes are flagged topical. Number density follows complexity; never force a number quota.
3. Mandarin character counts and runtime estimates match each episode's English runtime without dropping analytical content or increasing conceptual difficulty; never add words to meet a character quota.
4. English-to-Mandarin parity holds for all numbers, names, dates, uncertainty language, counterpoints, falsifiers, temperature, and complexity.
5. The series has non-empty English and Mandarin titles following the automatic naming rule. Every episode has four non-empty publishing fields — a content-led English title, Mandarin title, English description, Mandarin description — plus both spoken scripts. Mandarin metadata preserves the core claim and educational disclaimer without relying on the English text. Each description ends with `hashtags_per_video` valid hashtags on one separate line; at least two are specific to that episode, the two language sets have equivalent discovery intent, and neither set contains irrelevant, duplicate, spam, hype, or internal-system tags. Every episode also has exactly three bilingual non-empty HeyGen production-text field pairs: an English/Mandarin video title containing only the resolved ticker/topic name (identical in both languages unless a standard Chinese name is more recognizable), English/Mandarin series text exactly matching `Series X of Y` / `第X集，共Y集`, and a distinct English 3-7-word thumbnail hook plus its natural, non-literal Mandarin transcreation, both supported by the episode. Confirm each video's HeyGen prompt requests no other metadata text beyond its own language's set.
6. Every episode contains an appropriate counterweight and stands alone in either language; its final 1-2 analytical sentences answer the hook, and the last sentence before any sanctioned outro block is a declarative takeaway. In illiterate mode, the counterweight may be one simple business risk rather than a market debate.
7. Run a no-handoff scan on both spoken scripts and descriptions. Reject and rewrite any cross-video reference, cliffhanger, teaser, promise of future coverage, closing rhetorical question, or equivalent phrase such as "next episode/video," "we'll cover," "stay tuned," "下一集", "下期", or "敬请期待". Sanctioned intro/outro blocks are exempt: when intro_outro is series-branded, instead verify both blocks exist in both languages in every episode, that no intro or outro phrasing repeats across episodes in either language, and that no other handoff language appears in script interiors.
8. Run a bilingual compression pass. Every sentence must add a fact, mechanism, inference, counterpoint, or conclusion. Delete filler, empty transitions, repeated setup, redundant qualifiers, and any sentence whose removal leaves meaning and spoken clarity unchanged. Never pad either language to reach the runtime ceiling.
9. Run a source-neutrality scan across the entire generated file. Reject and rewrite references to the internal research system, including "the vault," "vault research," "vault estimate," "资料库研究," and "知识库研究." Remove attribution phrases such as "per our analysis" or "our opinion is" unless needed to distinguish inference from fact. Confirm no personal ownership or position statement appears.
10. Temperature check: the requested tilt is visible in selection, order, hooks, and airtime, but material opposing evidence remains and the final synthesis follows evidence. Reject forced bullish or bearish verdicts, hype, recommendations, and selective omission.
11. Complexity check: illiterate prioritises business understanding, has no unexplained technical terms or acronyms, omits nonessential market analysis, and never prints the label in audience-facing text; beginner explains the business before the debate and defines sector terms; intermediate compresses basic context and prioritises live news, non-consensus insights, market debates, and outstanding questions.
12. Coverage matches complexity: beginner and intermediate satisfy the analytical + archetype coverage; illiterate satisfies the simplified business-first coverage and is not padded with omitted analytical roles. No repeated explanations across the sequence; no statistic appears in more than 3 episodes; concepts owned by another series get one-sentence treatment only.
13. All internal wikilinks and web URLs are verified; estimates, chatter, and unresolved source conflicts are flagged, never promoted to fact.
14. Beginner/intermediate finales argue both sides and name the 1-2 observables that decide the debate. Illiterate closes with a simple business summary and one clear risk; a full bull/bear debate is optional.
15. Filename begins with YYYY-MM-DD; the run created or updated exactly one breakdown Markdown file, no per-episode files.
16. HeyGen visual-mode check: the only non-presenter visual is the two-second opening cut-in containing a photo of the presenter's real face plus the exact video title, series text, and thumbnail hook in the script's own language — confirm the face matches the attached reference photo or the selected avatar's real identity, never a generic or newly generated face, and confirm no English/Mandarin field mixing. After it, the entire video is one continuous static video-call-style presenter shot with no B-roll, graphic cutscenes, charts, animations, overlays beyond captions, scene changes, camera moves, or further cuts. Captions are rolling and word-synchronised: exactly the current spoken word/token uses the opening-card accent colour while every other caption word remains white.
17. Report every file created or modified.
```

## Design rule in one line

**Fix the analytical roles and quality gates; let the subject pick the archetype, the archetype pick the coverage, and the company decide titles, order, and weight — teach every shared concept exactly once.**
