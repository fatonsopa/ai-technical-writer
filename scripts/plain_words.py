#!/usr/bin/env python3
"""Advisory wording review for Markdown files.

This script flags phrases that commonly indicate padding or vague writing.
It does not judge whether a sentence is meaningful. Findings are suggestions,
not errors, unless --strict is explicitly requested.

Usage:
    python3 scripts/plain_words.py path/to/doc.md
    python3 scripts/plain_words.py --strict path/to/doc.md
    python3 scripts/plain_words.py --report path/to/doc.md

--anchors is accepted for compatibility with older calls but intentionally has
no effect: the writing standard no longer requires bold anchors on every list.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

SUGGESTIONS = {
    r"\bin order to\b": "Usually 'to' is enough.",
    r"\bdue to the fact that\b": "Usually 'because' is clearer.",
    r"\bat this point in time\b": "Usually 'now' is clearer.",
    r"\bit is important to note that\b": "Say the important fact directly.",
    r"\bit should be noted that\b": "State the fact directly.",
    r"\bin the event that\b": "Usually 'if' is clearer.",
    r"\bfor the purpose of\b": "Usually 'for' or 'to' is clearer.",
    r"\bseamless(?:ly)?\b": "Describe the actual behavior or failure conditions.",
    r"\brobust\b": "Name the concrete reliability property or check.",
    r"\bleverage\b": "Consider 'use'; keep 'leverage' if it has a precise meaning.",
    r"\butiliz(?:e|ation)\b": "Consider 'use'; choose wording based on the sentence.",
    r"\b(?:best-in-class|world-class|cutting-edge)\b": "Remove promotional claims; state verified facts.",
    r"\b(?:provides visibility into|enables visibility into)\b": "Describe exactly what people can see.",
    r"\b(?:ensure seamless|facilitate seamless)\b": "State the real action and measurable result.",
}
COMPILED = [(re.compile(p, re.I), advice) for p, advice in SUGGESTIONS.items()]


def visible_text(text: str) -> str:
    """Mask fenced code, inline code, and links without shifting line numbers."""
    def mask(match: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", match.group(0))
    text = re.sub(r"```.*?```|~~~.*?~~~", mask, text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", mask, text)
    text = re.sub(r"https?://[^\s)>]+", mask, text)
    return text


def findings(text: str) -> list[tuple[int, str, str]]:
    masked = visible_text(text)
    out = []
    for number, line in enumerate(masked.splitlines(), 1):
        if line.lstrip().startswith("|") and any(mark in line for mark in ("Unclear", "Clearer", "Instead of")):
            continue
        for matcher, advice in COMPILED:
            for match in matcher.finditer(line):
                out.append((number, match.group(0), advice))
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--strict", action="store_true", help="Exit nonzero when any phrase is flagged")
    parser.add_argument("--report", action="store_true", help="Keep advisory exit status (compatibility)")
    parser.add_argument("--anchors", action="store_true", help="Legacy flag, ignored")
    args = parser.parse_args(argv)
    total = 0
    for path in args.files:
        if not path.is_file():
            parser.error(f"file does not exist: {path}")
        for number, phrase, advice in findings(path.read_text(encoding="utf-8")):
            print(f"{path}:{number}: {phrase!r}: {advice}")
            total += 1
    print(f"{total} wording suggestion(s) in {len(args.files)} file(s). Review in context.")
    return int(args.strict and not args.report and total > 0)


if __name__ == "__main__":
    raise SystemExit(main())
