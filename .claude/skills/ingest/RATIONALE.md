---
type: skill-rationale
for_skill: /ingest
purpose: Design rationale for `/ingest`. SKILL.md contains operational rules; this file explains why they're shaped this way. References in SKILL.md take the form `§N.M` and map to sections below.
last_reviewed: 2026-04-24
---

# /ingest — Design Rationale

## §1. Why not canonical URL normalization (Step 0.3 dedup)

The obvious dedup strengthening is to normalize URLs (strip trailing slashes, sort query params alphabetically, lowercase hostname) before comparing, so that `https://example.com/path` and `https://Example.com/path/` resolve to the same key. Rejected because:

**(a) URL semantics are provider-specific.** YouTube's `?v=abc123` is the ONLY meaningful part of the URL; stripping it normalizes two different videos to the same key. A blog's `?utm_source=twitter` is meaningless tracking; keeping it produces false-miss dedup on the same article shared from different channels. The skill cannot reliably distinguish which query params carry semantic weight for an arbitrary host.

**(b) Over-normalization produces false dedup matches.** "Two truly distinct articles collapsed as 'same'" is a silent-corruption failure mode — the user expects the second ingest to work and gets blocked instead. Recovery requires manually inspecting why the block fired and either deleting the prior note or editing its frontmatter, both of which add friction for the wrong-direction failure.

**(c) Strict exact match with user-facing confirmation is auditable and recoverable.** The cross-day confirmation prompt (branch (a) skip / (b) re-ingest / (c) cancel) makes the dedup decision explicit and leaves an audit trail. Silent canonical dedup is neither — the user never sees that a block fired for a URL-normalization reason they'd never have chosen manually.

The rule: **exact string equality on the user-supplied URL**, with user-facing confirmation for cross-day cases. Same-day identical-URL re-ingests hard-block (clearly accidental). Cross-day same-URL re-ingests prompt (legitimately ambiguous — the source may have been updated).

## §2. Why two dedup checks (Step 0.3 for Mode A/B, Step 1 for Mode C)

Step 0.3 handles URL and single-file ingests (Modes A/B) with hard-block + prompt semantics. Step 1's inline duplicate check handles Batch Mode C, where inbox files may internally carry source URLs/paths that are identical across differently-named inbox drops (e.g., same article saved twice with different filenames).

The two checks are NOT redundant — they cover different failure surfaces. Mode A/B files through Step 0.3 first (Step 1's check is short-circuited because 0.3 already reported the dedup outcome). Mode C bypasses 0.3 and relies on Step 1.
