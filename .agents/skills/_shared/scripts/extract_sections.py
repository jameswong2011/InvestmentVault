#!/usr/bin/env python3
"""
extract_sections.py — section-targeted markdown extraction (Fix #4, 2026-07-08).

Replaces the brittle inline awk range-patterns embedded in skill prompts
(`$surface` default-mode Phase 1) with a tested, heading-drift-tolerant
extractor. Emits frontmatter + named `##` sections + last-N Log entries, and
reports which requested sections were missing so the caller can flag template
drift (the exact failure `$lint #14` guards).

NOT for `$catalyst` — that skill deliberately full-reads for cross-section
signal (R7 rejected section-targeting there). Use only where a skill has
opted into section-targeted reads.

Usage:
  python3 extract_sections.py FILE [FILE ...] \
      --sections "Summary,Key Non-consensus Insights,Risks,Catalysts" \
      --log-tail 5

  # heading match is case/whitespace-insensitive and prefix-tolerant, so
  # "Key Non-consensus Insights" matches "## Key Non-consensus Insights (updated)"

Output (per file, machine- and LLM-readable):
  ===== FILE: <path> =====
  --- frontmatter ---
  <yaml block, verbatim including --- fences>
  --- section: <canonical requested name> ---
  <body, or "(MISSING)" if the heading was not found>
  ...
  --- log (last N) ---
  <last N dated ### entries from ## Log, or "(no Log section)">
  --- missing sections: A, B ---   (only printed if any requested section absent)

Exit: 0 always for readable files; 3 if a FILE cannot be read (self-validation).
"""

import argparse
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^(#{2,3})\s+(.*)$")


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def read(p):
    return Path(p).read_text(encoding="utf-8", errors="replace")


def split_frontmatter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[: i + 1]), "\n".join(lines[i + 1 :])
    return "", text


def parse_l2_sections(body):
    """Return ordered list of (heading_text, [body_lines]) for `## ` sections."""
    lines = body.split("\n")
    out, cur, buf = [], None, []
    for ln in lines:
        m = re.match(r"^##\s+(?!#)(.*)$", ln)
        if m:
            if cur is not None:
                out.append((cur, buf))
            cur, buf = m.group(1).strip(), []
        elif cur is not None:
            buf.append(ln)
    if cur is not None:
        out.append((cur, buf))
    return out


def match_section(sections, requested):
    """Exact-normalized match, else prefix match ('Business Model' ~ 'Business Model & ...')."""
    rn = norm(requested)
    for head, buf in sections:
        if norm(head) == rn:
            return head, buf
    for head, buf in sections:
        hn = norm(head)
        if hn.startswith(rn) or rn.startswith(hn):
            return head, buf
    return None, None


def log_tail(sections, n):
    for head, buf in sections:
        if norm(head) == "log":
            text = "\n".join(buf)
            # split on ### date headers, keep last n
            parts = re.split(r"(?m)^(###\s+\d{4}-\d{2}-\d{2}.*)$", text)
            # parts = [pre, hdr1, body1, hdr2, body2, ...]
            entries = []
            for i in range(1, len(parts), 2):
                entries.append(parts[i] + (parts[i + 1] if i + 1 < len(parts) else ""))
            if not entries:
                return text.strip() or "(Log section empty)"
            return "\n".join(e.rstrip() for e in entries[-n:])
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--sections", default="",
                    help="comma-separated section names to extract")
    ap.add_argument("--log-tail", type=int, default=0,
                    help="include the last N dated Log entries")
    args = ap.parse_args()

    requested = [s.strip() for s in args.sections.split(",") if s.strip()]
    rc = 0
    for f in args.files:
        try:
            text = read(f)
        except OSError as e:
            print(f"SELF-VALIDATION FAILED: cannot read {f}: {e}", file=sys.stderr)
            rc = 3
            continue
        fm, body = split_frontmatter(text)
        secs = parse_l2_sections(body)
        print(f"===== FILE: {f} =====")
        if fm:
            print("--- frontmatter ---")
            print(fm)
        missing = []
        for req in requested:
            head, buf = match_section(secs, req)
            print(f"--- section: {req} ---")
            if head is None:
                print("(MISSING)")
                missing.append(req)
            else:
                print("\n".join(buf).strip() or "(empty)")
        if args.log_tail > 0:
            lt = log_tail(secs, args.log_tail)
            print(f"--- log (last {args.log_tail}) ---")
            print(lt if lt is not None else "(no Log section)")
        if missing:
            print(f"--- missing sections: {', '.join(missing)} ---")
        print()
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"SELF-VALIDATION FAILED: extract_sections.py crashed: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
