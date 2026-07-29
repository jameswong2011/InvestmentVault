#!/usr/bin/env python3
"""Extract text from a local PDF with optional 1-indexed page ranges."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_pages(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(total))
    selected: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start_text, end_text = token.split("-", 1)
            start, end = int(start_text), int(end_text)
        else:
            start = end = int(token)
        if start < 1 or end < start or end > total:
            raise ValueError(
                f"invalid page range {token!r}; PDF contains {total} page(s)"
            )
        selected.update(range(start - 1, end))
    if not selected:
        raise ValueError("page selection is empty")
    return sorted(selected)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument(
        "--pages",
        help='1-indexed pages, for example "1-10" or "1,3,7-9"',
    )
    parser.add_argument(
        "--page-count",
        action="store_true",
        help="print the number of pages and exit",
    )
    args = parser.parse_args()

    try:
        from pypdf import PdfReader
    except ImportError:
        print(
            "pypdf is required for PDF ingestion: python3 -m pip install pypdf",
            file=sys.stderr,
        )
        return 2

    if not args.pdf.is_file():
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        return 2

    try:
        reader = PdfReader(str(args.pdf))
        total = len(reader.pages)
        if args.page_count:
            print(total)
            return 0
        indexes = parse_pages(args.pages, total)
        for index in indexes:
            text = reader.pages[index].extract_text() or ""
            print(f"\n===== PAGE {index + 1} / {total} =====\n")
            print(text.rstrip())
    except Exception as exc:
        print(f"PDF extraction failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
