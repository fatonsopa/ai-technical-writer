#!/usr/bin/env python3
"""Zero-loss check for a rewritten document.

A rewrite may change every sentence; it may not lose a rule or a fact. This script makes that checkable:

  inventory OLD.md [--all] [--out inventory.json]
      Numbers every normative sentence of OLD (a sentence that states a rule, a prohibition, a requirement or a
      definition the reader relies on) as N1, N2, ... With --all it also numbers every other sentence of four words or
      more, and every table row but the header, as F1, F2, ... (facts: counts, settings, measurements, who does what).
      The N numbers are the same with or without --all, so a map built without it keeps working.

  literals OLD.md
      Lists what a rewrite must carry VERBATIM, whatever happens to the sentences: every code span (commands, paths,
      flags, env vars, function and hook names), path-like token, URL, issue id (CG-n / MF-n), date, number with its
      unit, bare number of two digits or more (3,298; 432), clock time (13:05 UTC), version (28.0.4), quoted value, quoted
      passage of three words or more (any length, across line breaks, in italics or not: someone's words), short table
      cell, and heading. (A numbered step is a sentence of the inventory, kept whether or not it carries a rule word.)

  check --old OLD.md --new NEW.md --map map.json [--also FILE ...] [--all] [--refs FILE ...]
      Every numbered sentence must be accounted for in map.json, and each account must hold:
        "N7": "kept: <heading or words in NEW>"        -> the place it names holds the sentence: the heading's section,
                                                          or the section around the cited words, contains every literal
                                                          of the sentence and at least half of its content words (all of
                                                          them when it has three or fewer)
        "N8": "moved: <path>#<heading>"                 -> that file exists and contains that heading
        "N9": "dropped: <why>"                          -> taken at its word, but listed in the report
      With --all (or a map that holds F ids) the F sentences are checked the same way; an F sentence found word for
      word in NEW needs no account.
      Every literal of OLD must appear verbatim in NEW or an --also file, or be accounted for as
        "literal:<the literal>": "kept: <its new words>" | "moved: <path>#<heading>" | "dropped: <why>"
      — so a step or a cell may be reworded, but only by saying so; a command or a path is carried as it is. A quoted
      passage is someone's words: an account that restates or drops it must name where the original words live (an
      issue id or a URL); with no other home they stay.
      --refs FILE ...: every "`<OLD's file name>` §X" in those files (also the short "`NN-MM` §X" of a plan part) must
      find a heading numbered X in NEW, and a heading of OLD numbered X that the map moved must keep its number.
      Generated blocks (<!-- name:begin --> ... <!-- name:end -->) must be byte-identical between OLD and NEW.
      It also prints, without failing: the sentences NEW adds that carry a fact OLD does not hold (ADDED), and the
      size change (SIZE), flagged when NEW is more than a quarter longer than OLD.
      Exit 0 when every sentence and literal is accounted for, every cited section number holds and every block is
      unchanged; exit 1 otherwise.

  added --old OLD.md --new NEW.md [--also FILE ...]
      Lists the sentences of NEW that carry a literal (a number, a command, a path, an issue, a date, a section
      reference, a quote) that OLD and the --also files do not hold: the claims a rewrite added, each of which needs a
      source in the report. A claim without a literal is the writer's to list.

  suggest --old OLD.md --new NEW.md [--also FILE ...] [--all] [--out map.json]
      Pre-fills map.json: for each sentence, the NEW heading whose section holds it word for word, or else the one whose
      text shares the most content words with it (a hint for the writer to confirm or correct — never a verdict).

The repository's scripts/rules/moved_sentences.py proves a VERBATIM move (every old line found unchanged in the new
files) and by design reports a rewritten line as missing. This script is for the rewrite: the words may all change; the
accounting of rules and facts may not. Both read "the same words" the same way: spacing and case ignored, "CLAUDE.md §x"
= "§x".

Only the standard library is used. The normative markers can be widened with --keywords "word,word".
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

SAME_REF = re.compile(r"claude\.md\s+(?=§)")


def norm(text: str) -> str:
    """Lower case, one space between words, and "CLAUDE.md §x" read as "§x". The same reading as the repository's
    scripts/rules/moved_sentences.py uses; kept here so the skill folder installs on its own."""
    return SAME_REF.sub("", " ".join(text.split()).lower())


def flat(text: str) -> str:
    """norm() without the marks that do not change the words: bold, italics and code font."""
    text = re.sub(r"\*\*|__|`|(?<!\w)\*|\*(?!\w)", "", text)
    return norm(text)


DEFAULT_KEYWORDS = (
    "must", "must not", "never", "always", "only", "shall", "required", "requires", "refuse", "refused", "refuses",
    "forbidden", "binding", "cannot", "can not", "may not", "not allowed", "do not", "does not", "is not", "are not",
    "no exception", "before", "after", "until", "unless", "whenever", "every", "each", "exactly one", "at most",
    "at least", "default", "defaults",
)
STOP = set("""a an the and or of to in on for with by at from as is are was were be been being it its this that these
those there their they them we our you your he his she her i if then than so such not no yes do does did done has have
had having will would can could may might shall should must into onto over under up down out about between within
without also any all some one two three first last same other another each every both either neither more most less
least much many very just only even still yet again once when where while how what which who whom whose why""".split())
BLOCK = re.compile(r"^[ \t]*<!--\s*([a-z0-9_-]+):begin\s*-->(.*?)<!--\s*\1:end\s*-->", re.S | re.M)  # at a line's start: an example in a code span is not a block
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$", re.M)
ISSUE_ID = re.compile(r"\b[A-Z]{2,5}-\d+\b")
URL = re.compile(r"https?://[^\s)>\]]+?(?=[.,;:]?(?:\s|$|[)>\]]))")  # a trailing comma or period is punctuation, not the URL


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = BLOCK.sub(" ", text)  # generated blocks are checked byte-for-byte, not sentence by sentence
    return text


def paragraphs(text: str) -> list[str]:
    """Logical paragraphs of a markdown document with hard-wrapped lines joined back together. A paragraph ends at a
    blank line, a heading, a table row or the start of a list item; an indented or plain line that follows a list
    item continues it (the standards wrap at about 120 columns, so a rule often spans three lines)."""
    out: list[str] = []
    cur: list[str] = []
    flush = lambda: (out.append(" ".join(cur)), cur.clear()) if cur else None
    for raw in strip_code(text).splitlines():
        line = raw.strip()
        if not line:
            flush(); continue
        starts_new = bool(re.match(r"^#{1,6}\s|^\||^[-*+]\s|^\d+[.)]\s|^>\s?", line))
        if starts_new:
            flush()
        cur.append(line)
        if line.startswith("|") or re.match(r"^#{1,6}\s", line):
            flush()
    flush()
    return out


RULE_ROW = re.compile(r"\|?[\s:|-]+\|?")


def _sentences(text: str) -> list[tuple[str, bool, bool]]:
    """(sentence, is a numbered step, comes from a table cell or a heading) for a markdown document, table cells and
    bullets included, code and generated blocks excluded. A numbered step is an instruction by its position, so the
    inventory keeps it whether or not it carries a rule word."""
    out: list[tuple[str, bool, bool]] = []
    for para in paragraphs(text):
        if RULE_ROW.fullmatch(para):  # table rule rows
            continue
        step = bool(re.match(r"^\d+[.)]\s", para))
        heading = bool(re.match(r"^#{1,6}\s", para))
        line = re.sub(r"^#{1,6}\s+", "", para)
        line = re.sub(r"^[-*+]\s+|^\d+[.)]\s+|^>\s?", "", line)
        in_cell = line.startswith("|")
        cells = [c.strip() for c in line.split("|")] if in_cell else [line]
        for cell in cells:
            if not cell:
                continue
            for s in re.split(r"(?<=[.;!?])\s+(?=[A-Z*`(\"'])", cell):
                s = re.sub(r"\*\*|(?<!\w)\*|\*(?!\w)", "", s).strip()  # bold and italic marks are not words
                if len(s.split()) >= 4 or (step and s):
                    out.append((s, step, in_cell or heading))  # a heading is a literal; a cell is in its row
    return out


def tagged_sentences(text: str) -> list[tuple[str, bool]]:
    return [(s, step) for s, step, _ in _sentences(text)]


def sentences(text: str) -> list[str]:
    return [s for s, _ in tagged_sentences(text)]


def is_normative(sentence: str, keywords: tuple[str, ...]) -> bool:
    low = f" {sentence.lower()} "
    return any(f" {k} " in low or f" {k}," in low or f" {k}." in low for k in keywords)


def cells_of(row: str) -> list[str]:
    return [re.sub(r"\*\*|(?<!\w)\*|\*(?!\w)", "", c).strip() for c in row.strip().strip("|").split("|")]


def table_rows(text: str) -> list[str]:
    """Every body row of every table, as "cell | cell | …" with bold and italics stripped; header rows are left out
    (their cells are literals already)."""
    paras = paragraphs(text)
    out = []
    for i, para in enumerate(paras):
        if not para.startswith("|") or RULE_ROW.fullmatch(para):
            continue
        if i + 1 < len(paras) and RULE_ROW.fullmatch(paras[i + 1]):
            continue  # a header row
        cells = [c for c in cells_of(para)]
        if any(re.search(r"\w", c) for c in cells):
            out.append(" | ".join(cells))
    return out


def inventory(text: str, keywords: tuple[str, ...], all_facts: bool = False) -> list[dict]:
    """N1, N2, … for the rule sentences (numbered the same with or without all_facts); with all_facts, F1, F2, … for
    every other sentence of four words or more and for every table row (a cell's sentence is covered by its row)."""
    items: list[dict] = []
    n = f = 0
    for s, step, in_cell in _sentences(text):
        if step or is_normative(s, keywords):
            n += 1
            items.append({"id": f"N{n}", "text": s})
        elif all_facts and not in_cell:
            f += 1
            items.append({"id": f"F{f}", "text": s})
    if all_facts:
        for row in table_rows(text):
            f += 1
            items.append({"id": f"F{f}", "text": row, "row": True})
    return items


# What a masked literal leaves behind: a word character, so every pattern below already refuses to read a number or a
# word across it, and not a letter, so no word can be read out of it.
MASK = "_"
CODE_SPAN = re.compile(r"`[^`\n]*`")
LIST_NUMBER = re.compile(r"^[ \t]*(?:[-*+][ \t]+)?\d+[.)](?=[ \t])")


def blank(text: str, rx: re.Pattern[str]) -> str:
    """`text` with every match of `rx` replaced by MASK of the same length. A position never moves and two words never
    become one, so a pattern that runs afterwards can only match a run of characters the document itself holds: cutting
    a match out instead made "1172 import jobs" read "1172 imp" once "or" was cut from it (CG-2631)."""
    return rx.sub(lambda m: MASK * len(m.group(0)), text)


def is_word(ch: str) -> bool:
    return ch.isalnum() or ch == "_"


def blank_tokens(text: str, lits: list[str]) -> str:
    """`text` with every occurrence of each of `lits` masked where it stands as a token of its own, so a literal is
    never masked out of the middle of a longer word. Each literal is looked for in the text as it was given, and the
    masked part is the union over the literals, so the order they come in does not matter."""
    out = list(text)
    for lit in lits:
        head, tail = is_word(lit[0]), is_word(lit[-1])
        i = text.find(lit)
        while i != -1:
            j = i + len(lit)
            if not (head and i and is_word(text[i - 1])) and not (tail and j < len(text) and is_word(text[j])):
                out[i:j] = MASK * len(lit)
            i = text.find(lit, i + 1)
    return "".join(out)


LITERAL_PATTERNS = (
    ("code", re.compile(r"`([^`\n]+)`")),
    ("path", re.compile(r"(?<![\w/.`])((?:\.{0,2}/)?(?:[\w.-]+/)+[\w.-]+\.\w{1,6})(?![\w/])")),
    ("url", URL),
    ("issue", ISSUE_ID),  # an issue id: a team key and a number (CG-1538, MF-810, ADR-0005)
    ("date", re.compile(r"\b(?:\d{4}-\d{2}-\d{2}|\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4})\b")),
    ("number", re.compile(r"(?<![\w.])(\d[\d,.]*\s?(?:%|ms|s|min|minutes?|hours?|days?|lines?|rows?|columns?|chars?|characters?|words?|helpers?|tasks?|agents?|GB|MB|KB|px))\b")),
    ("quoted", re.compile(r"(?<!\w)\"([A-Za-z0-9_][^\"\n]{0,60}?)\"(?!\w)")),  # a short quoted value; three words or more is a "quote"
)
BARE_PATTERNS = (  # found after the literals above are masked, so "10 minutes" is one literal, not two
    ("time", re.compile(r"(?<![\w:.])\d{1,2}:\d{2}(?::\d{2})?(?:\s?UTC)?(?![\w:])")),
    ("version", re.compile(r"(?<![\w.])\d+\.\d+\.\d+(?!\w|\.\d)")),
    # a bare number, with the word it counts when one follows ("16 cores", "432 commits"; "| 16 |" stays "16"). The
    # word is a whole one or none: "1555 api_requests" gives "1555", never the fragment "1555 api" (CG-2631)
    ("count", re.compile(r"(?<![\w.,:#§/-])(?:\d{1,3}(?:,\d{3})+|\d{2,})(?!\w|[.,:]\d)"
                         r"(?:[ \t]+(?!(?:" + "|".join(sorted(STOP | {"am", "pm", "utc"}, key=len, reverse=True))
                         + r")\b)[a-z][a-z-]*[a-z](?![\w-]))?")),
)
NUMERIC = {"count", "time", "version", "cell", "ref"}  # matched as a whole token: "16" is not found inside "1416"


def quotes(para: str) -> list[str]:
    """Quoted passages of three words or more in one paragraph: straight quotes paired in order (a quote inside a code
    span does not count), and curly quotes. Any length; the paragraph's lines are already joined."""
    masked = re.sub(r"`[^`]*`", lambda m: "x" * len(m.group(0)), para)
    at = [i for i, c in enumerate(masked) if c == '"']
    found = [para[a + 1:b] for a, b in zip(at[0::2], at[1::2])]
    found += re.findall(r"“([^”]+)”", masked)
    return [q.strip() for q in found if len(q.split()) >= 3]


def inline_literals(raw: str, paras: list[str] | None = None) -> list[tuple[str, str]]:
    """(kind, literal) in running text: every pattern of LITERAL_PATTERNS over `raw` (code fences included, span by
    span), the quoted passages of each paragraph, then the bare numbers, clock times and versions of the paragraphs that
    are not already part of one of those. `paras` defaults to `raw` as one paragraph (a single sentence)."""
    paras = [raw] if paras is None else paras
    found: list[tuple[str, str]] = []
    seen: set[str] = set()

    def add(kind: str, lit: str) -> None:
        lit = lit.strip()
        if lit and lit not in seen:
            seen.add(lit); found.append((kind, lit))
    for kind, rx in LITERAL_PATTERNS:
        for m in rx.finditer(raw):
            lit = m.group(1) if m.groups() else m.group(0)
            if not (kind == "quoted" and len(lit.split()) >= 3):
                add(kind, lit)
    for para in paras:
        for q in quotes(para):
            add("quote", q)
    masked = [t for t in paras if not re.match(r"^#{1,6}\s", t)]  # a heading's number is in the heading literal
    masked = [blank(t, LIST_NUMBER) for t in masked]  # a list number is position, not a fact
    text = blank("\n".join(masked), CODE_SPAN)
    text = blank_tokens(text, [lit for kind, lit in found if kind != "code"])
    for kind, rx in BARE_PATTERNS:
        for m in rx.finditer(text):
            add(kind, m.group(0))
        text = blank(text, rx)
    return found


def literals(text: str) -> list[tuple[str, str]]:
    """(kind, literal) for everything a rewrite must carry verbatim: code spans, paths, URLs, issue ids, dates, numbers
    with units, bare numbers, clock times, versions, quoted values and passages, short table cells and headings. Code
    fences are included span by span; generated blocks are left out (they are checked byte for byte)."""
    paras = paragraphs(text)
    found = inline_literals(BLOCK.sub(" ", text), paras)
    seen = {lit for _, lit in found}

    def add(kind: str, lit: str) -> None:
        lit = lit.strip()
        if lit and lit not in seen:
            seen.add(lit); found.append((kind, lit))
    for h in headings(text):
        add("heading", h)
    for para in paras:
        if para.startswith("|") and not RULE_ROW.fullmatch(para):
            for cell in para.strip().strip("|").split("|"):
                cell = cell.strip()
                if 1 <= len(cell.split()) <= 6 and not cell.endswith(".") and re.search(r"\w", cell):
                    add("cell", cell)  # a short cell is a value (a status, a label); a long one is a sentence, inventoried as such
    return found  # a numbered step is a sentence of the inventory (tagged_sentences), not a literal


def present(kind: str, lit: str, hay: str) -> bool:
    """`lit` appears in `hay` (already normalised the same way): a number, time, version or table cell as a whole token,
    anything else as a run of characters."""
    n = norm(lit)
    if kind in NUMERIC and not (kind == "cell" and re.search(r"[a-z]", n)):  # a word cell keeps the old reading
        return re.search(rf"(?<![\w.,]){re.escape(n)}(?!\w|[.,]\d)", hay) is not None
    return n in hay


IRREGULAR = dict(pair.split(":") for pair in """kept:keep ran:run made:make took:take taken:take held:hold left:leave
built:build sent:send written:write wrote:write chosen:choose chose:choose found:find gave:give given:give paid:pay
said:say seen:see saw:see shown:show spent:spend told:tell thought:think understood:understand went:go gone:go
broke:break broken:break began:begin begun:begin brought:bring caught:catch drew:draw drawn:draw got:get knew:know
known:know lost:lose meant:mean sold:sell spoke:speak spoken:speak threw:throw thrown:throw led:lead""".split())


def stem(word: str) -> str:
    """A crude stem, enough to match "approves" with "approve", "merged" with "merges" and "kept" with "keeps"."""
    word = IRREGULAR.get(word, word)
    for suf in ("ings", "ing", "ies", "ied", "ed", "es", "s"):
        if word.endswith(suf) and not (suf == "s" and word.endswith("ss")) and len(word) - len(suf) >= 3:
            word = word[: -len(suf)] + ("y" if suf in ("ies", "ied") else "")
            break
    return word[:-1] if word.endswith("e") and len(word) > 3 else word


def content_words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z][a-z0-9_-]{2,}", s.lower()) if w not in STOP}


def stems(s: str) -> set[str]:
    return {stem(w) for w in content_words(s)}


def headings(text: str) -> list[str]:
    return [h.strip() for h in HEADING.findall(strip_code(text))]


def blocks(text: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in BLOCK.finditer(text)}


def sections(text: str) -> list[tuple[str, str]]:
    """(heading, body) pairs; the text before the first heading is under ''."""
    parts = re.split(r"^(#{1,6}\s+.*)$", strip_code(text), flags=re.M)
    out = [("", parts[0])]
    for i in range(1, len(parts), 2):
        out.append((re.sub(r"^#{1,6}\s+", "", parts[i]).strip(), parts[i + 1] if i + 1 < len(parts) else ""))
    return out


def contains(text: str, needle: str) -> bool:
    """`needle` is a heading of `text`, or words that appear in it (moved_sentences.norm: spacing and case ignored)."""
    n = norm(needle)
    return n in [norm(h) for h in headings(text)] or n in norm(text)


# --- Where a "kept" account points (CG-1585 F3) ---------------------------------------------------------------------

def units(text: str) -> list[tuple[str, str, int]]:
    """The document as blocks in order: ("heading", text, level), ("code", a whole fence or generated block, 0) and
    ("para", a logical paragraph, 0)."""
    out: list[tuple[str, str, int]] = []
    buf: list[str] = []

    def flush() -> None:
        for p in paragraphs("\n".join(buf)):
            m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", p)
            out.append(("heading", m.group(2), len(m.group(1))) if m else ("para", p, 0))
        buf.clear()
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        gen = re.match(r"^[ \t]*<!--\s*([a-z0-9_-]+):begin\s*-->", line)
        if line.lstrip().startswith("```") or gen:
            flush()
            end = (lambda s: s.lstrip().startswith("```")) if not gen else (lambda s, g=gen.group(1): f"{g}:end" in s)
            j = i + 1 if not (gen and end(line)) else i
            while j < len(lines) and not end(lines[j]):
                j += 1
            out.append(("code", "\n".join(lines[i:j + 1]), 0))
            i = j + 1
            continue
        buf.append(line)
        i += 1
    flush()
    return out


def section_text(us: list[tuple[str, str, int]], k: int) -> str:
    """The heading at index k with its own body: every block up to the next heading of any level."""
    parts = [us[k][1]]
    for kind, txt, _ in us[k + 1:]:
        if kind == "heading":
            break
        parts.append(txt)
    return flat("\n".join(parts))


def places(text: str, cited: str) -> list[tuple[str | None, str]]:
    """(heading, the place's text, flattened) for each place in `text` that an account "kept: <cited>" can mean: the
    section of the heading it names, or the section around each occurrence of the cited words. The heading is None for
    the text before the first heading."""
    us = units(text)
    want = flat(cited)
    named = [k for k, (kind, txt, _) in enumerate(us) if kind == "heading" and flat(txt) == want]
    if named:
        return [(us[k][1], section_text(us, k)) for k in named]
    owner: list[int | None] = []  # the heading each block sits under
    last: int | None = None
    for k, (kind, _, _) in enumerate(us):
        last = k if kind == "heading" else last
        owner.append(last)
    joined, spans = "", []
    for k, (_, txt, _) in enumerate(us):
        s = flat(txt)
        spans.append((len(joined), len(joined) + len(s), k))
        joined += s + " "
    out: list[tuple[str | None, str]] = []
    seen: set[int | None] = set()
    start = joined.find(want) if want else -1
    while start != -1:
        for a, b, k in spans:
            h = owner[k]
            if a < start + len(want) and b > start and h not in seen:
                seen.add(h)
                if h is None:
                    out.append((None, flat("\n".join(txt for j, (_, txt, _) in enumerate(us) if owner[j] is None))))
                else:
                    out.append((us[h][1], section_text(us, h)))
        start = joined.find(want, start + 1)
    return out


def item_literals(item: dict) -> list[tuple[str, str]]:
    lits = inline_literals(item["text"])
    if item.get("row"):
        for cell in item["text"].split(" | "):
            cell = cell.strip()
            if cell and 1 <= len(cell.split()) <= 6 and not cell.endswith(".") and re.search(r"\w", cell):
                lits.append(("cell", cell))
    return lits


def place_shortfall(item: dict, place: str, accounted: frozenset = frozenset()) -> str:
    """'' when `place` holds the item: every literal of it and at least half of its content words (all of them when it
    has three or fewer); otherwise what the place lacks. A literal the map accounts for ("literal:<x>") is not required:
    the writer already said where it went or why it changed."""
    missing = [lit for kind, lit in item_literals(item)
               if lit not in accounted and not present(kind, flat(lit), place)]
    words = stems(re.sub(r"https?://\S+", " ", item["text"]))
    have = stems(place)
    hit = len(words & have)
    need = len(words) if len(words) <= 3 else math.ceil(len(words) / 2)
    why = []
    if missing:
        why.append("lacks " + ", ".join(repr(m) for m in missing))
    if hit < need:
        why.append(f"holds only {hit} of its {len(words)} content words (needs {need})")
    return "; ".join(why)


def kept_gap(item: dict, rest: str, new: str, also: dict[str, str], accounted: frozenset = frozenset()) -> str:
    """'' when an account "kept: <rest>" names a place that holds the item, else the gap line."""
    found: list[tuple[str, str]] = []
    for name, text in [("NEW", new)] + list(also.items()):
        found += [(f"section {h!r} of {name}" if h is not None else f"the text before the first heading of {name}", p)
                  for h, p in places(text, rest)]
    if not found:
        return f"{item['id']} kept at {rest!r}, but NEW has no heading or words that say where: {item['text']}"
    shortfalls = [(w, place_shortfall(item, p, accounted)) for w, p in found]
    if any(not s for _, s in shortfalls):
        return ""
    w, s = shortfalls[0]
    return f"{item['id']} kept at {w}, but that place {s}: {item['text']}"


# --- Section numbers other files cite (CG-1585 F4) ------------------------------------------------------------------

SEC = r"\d+[a-z]?(?:\.\d+[a-z]?)*"


def heading_number(h: str) -> str | None:
    m = re.match(rf"^§?\s*({SEC})[.):]?(?:\s|$)", h.strip())
    return m.group(1) if m else None


def cited_sections(ref_text: str, old_path: str) -> list[tuple[int, str, str]]:
    """(line, the name used, section number) for every "`<name>` §X" in ref_text that names OLD: its file name, its
    name without ".md", or a plan part's "NN-MM"."""
    base = Path(old_path).name
    stem_ = base[:-3] if base.endswith(".md") else base
    names = {base, stem_}
    part = re.match(r"^(\d{2}-\d{2})-", stem_)
    if part:
        names.add(part.group(1))
    alt = "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True))
    rx = re.compile(rf"(?<![\w.-])`?({alt})`?(?![\w-])\s*((?:§\s?{SEC})(?:\s*(?:,\s*and|,|and|or)\s*§\s?{SEC})*)")
    out = []
    for n, line in enumerate(ref_text.splitlines(), 1):
        for m in rx.finditer(line):
            for x in re.findall(rf"§\s?({SEC})", m.group(2)):
                out.append((n, m.group(1), x))
    return out


def ref_gaps(old_path: str, old: str, new: str, mapping: dict, refs: list[str]) -> list[str]:
    numbers_new = {heading_number(h): h for h in headings(new) if heading_number(h)}
    flat_new = {flat(h) for h in headings(new)}
    gaps = []
    for ref in refs:
        for line, used, x in cited_sections(read(ref), old_path):
            where = f"{ref}:{line} cites `{used}` §{x}"
            if x not in numbers_new:
                gaps.append(f"{where}, and NEW has no heading numbered {x}")
                continue
            for h in headings(old):
                if heading_number(h) != x or flat(h) in flat_new:
                    continue
                kind, _, rest = mapping.get(f"literal:{h}", "").partition(":")
                rest, kind = rest.strip(), kind.strip().lower()
                y = heading_number(rest) if kind == "kept" else None
                if kind == "kept" and flat(rest) in flat_new and y != x:
                    gaps.append(f"{where}, but OLD's §{x} {h!r} is {rest!r} in NEW")
                elif kind in ("moved", "dropped"):
                    gaps.append(f"{where}, but OLD's §{x} {h!r} was {kind} ({rest})")
    return gaps


# --- What a rewrite added, and how much it grew (CG-1585 F5, F6) -----------------------------------------------------

def added(old: str, new: str, also: list[str]) -> list[tuple[str, list[str]]]:
    """(sentence of NEW, the literals in it that OLD and the --also files do not hold)."""
    hay = norm(old + "\n" + "\n".join(also))
    out = []
    for s in sentences(new):
        lits = inline_literals(s) + [("ref", r) for r in re.findall(rf"§\s?{SEC}", s)]
        new_lits = [l for k, l in lits if not present(k, norm(l), hay)]
        if new_lits:
            out.append((s, new_lits))
    return out


def size_line(old: str, new: str) -> str:
    a, b = len(old.splitlines()), len(new.splitlines())
    pct = round((b - a) * 100 / a) if a else 0
    line = f"SIZE     {a} → {b} lines ({pct:+d}%)"
    if a and b > a * 1.25:
        line += ": NEW is more than a quarter longer than OLD — the report says why (SKILL.md Step 5)"
    return line


# --- Commands -------------------------------------------------------------------------------------------------------

def cmd_inventory(a) -> int:
    inv = inventory(read(a.old), a.keywords, a.all)
    out = json.dumps(inv, indent=2, ensure_ascii=False)
    if a.out:
        Path(a.out).write_text(out + "\n", encoding="utf-8")
    n = sum(1 for i in inv if i["id"].startswith("N"))
    facts = f" and {len(inv) - n} fact sentences and rows" if a.all else ""
    print(f"{n} normative sentences{facts} in {a.old}" + (f" -> {a.out}" if a.out else ""))
    if not a.out:
        for item in inv:
            print(f"  {item['id']}: {item['text']}")
    return 0


def cmd_literals(a) -> int:
    lits = literals(read(a.old))
    print(f"{len(lits)} literals in {a.old} that a rewrite carries verbatim")
    for kind, lit in lits:
        print(f"  [{kind:7}] {lit}")
    return 0


def cmd_suggest(a) -> int:
    inv = inventory(read(a.old), a.keywords, a.all)
    new = read(a.new)
    targets = [(f"kept: {h}", content_words(h + " " + body), flat(h + " " + body)) for h, body in sections(new) if h]
    for extra in a.also:
        targets += [(f"moved: {extra}#{h}", content_words(h + " " + body), flat(h + " " + body))
                    for h, body in sections(read(extra)) if h]
    mapping = {}
    for item in inv:
        here = [h for h, _ in places(new, item["text"]) if h]
        if here:  # found word for word: name the section that holds it
            mapping[item["id"]] = f"kept: {here[0]}"
            continue
        words = content_words(item["text"])
        lits = item_literals(item)

        def score(t) -> float:  # shared content words, plus the share of the item's literals the section holds
            held = sum(present(k, flat(l), t[2]) for k, l in lits) / len(lits) if lits else 0
            return len(words & t[1]) / (len(words) or 1) + held
        best = max(targets, key=score, default=None)
        overlap = len(words & best[1]) / (len(words) or 1) if best else 0
        mapping[item["id"]] = best[0] if best and overlap >= 0.5 else "UNMAPPED: confirm or write dropped: <why>"
    out = json.dumps(mapping, indent=2, ensure_ascii=False)
    if a.out:
        Path(a.out).write_text(out + "\n", encoding="utf-8")
    print(out if not a.out else f"{len(mapping)} entries -> {a.out}")
    return 0


def cmd_added(a) -> int:
    found = added(read(a.old), read(a.new), [read(p) for p in a.also])
    print(f"{len(found)} sentence(s) of {a.new} carry a fact {a.old} does not hold — list each under "
          f"\"Added claims, with their sources\", or take it out")
    for s, lits in found:
        print(f"  ADDED    {s}  [new: {', '.join(lits)}]")
    return 0


def cmd_check(a) -> int:
    old, new = read(a.old), read(a.new)
    mapping = json.loads(read(a.map)) if a.map else {}
    all_facts = a.all or any(re.fullmatch(r"F\d+", k) for k in mapping)
    inv = inventory(old, a.keywords, all_facts)
    also = {p: read(p) for p in a.also}
    flat_hay = flat(new) + " " + " ".join(flat(t) for t in also.values())
    accounted = frozenset(k[len("literal:"):] for k in mapping if k.startswith("literal:"))
    gaps: list[str] = []
    item_gaps = 0
    dropped: list[str] = []
    for item in inv:
        before = len(gaps)
        acc = mapping.get(item["id"])
        if not acc and item["id"].startswith("F") and flat(item["text"]) in flat_hay:
            continue  # a fact carried word for word needs no account
        if not acc or not isinstance(acc, str):
            gaps.append(f"{item['id']} not in map: {item['text']}")
        else:
            kind, _, rest = acc.partition(":")
            kind, rest = kind.strip().lower(), rest.strip()
            if kind == "kept":
                if not rest or not (contains(new, rest) or any(contains(t, rest) for t in also.values())) \
                        and not any(places(t, rest) for t in [new, *also.values()]):
                    gaps.append(f"{item['id']} kept, but NEW has no heading or words {rest!r}: {item['text']}")
                else:
                    g = kept_gap(item, rest, new, also, accounted)
                    if g:
                        gaps.append(g)
            elif kind == "moved":
                path, _, anchor = rest.partition("#")
                target = also.get(path) if path in also else (read(path) if Path(path).exists() else None)
                if target is None:
                    gaps.append(f"{item['id']} moved to {path!r}, which does not exist: {item['text']}")
                elif anchor and not contains(target, anchor):
                    gaps.append(f"{item['id']} moved to {path}#{anchor}, but that file has no such heading or words")
            elif kind == "dropped":
                if len(rest.split()) < 3:
                    gaps.append(f"{item['id']} dropped without a reason of at least three words: {item['text']}")
                else:
                    dropped.append(f"{item['id']} dropped: {rest} — {item['text']}")
            else:
                gaps.append(f"{item['id']} has an unknown account {acc!r} (kept: / moved: / dropped:)")
        item_gaps += len(gaps) > before
    haystack = norm(new) + " " + " ".join(norm(t) for t in also.values())
    lit_dropped: list[str] = []
    old_lits = literals(old)
    for kind, lit in old_lits:
        if present(kind, norm(lit), haystack):
            continue
        acc = mapping.get(f"literal:{lit}", "")
        k, _, rest = acc.partition(":")
        k, rest = k.strip().lower(), rest.strip()
        if kind == "quote" and acc:
            if not (ISSUE_ID.search(rest) or URL.search(rest)):
                gaps.append(f"literal [quote] {lit!r} is someone's words: it stays word for word, or its account names "
                            f"where the original words live (an issue id or a URL); this account names none: {acc!r}")
            else:
                lit_dropped.append(f"[quote] {lit} — {acc}")
        elif k == "dropped" and len(rest.split()) >= 3:
            lit_dropped.append(f"[{kind}] {lit} — {rest}")
        elif k == "kept" and rest and (contains(new, rest) or any(contains(t, rest) for t in also.values())):
            continue
        elif k == "moved" and rest.partition("#")[0] in also and contains(also[rest.partition("#")[0]], rest.partition("#")[2]):
            continue
        else:
            home = " — a quote's account also names where its words live" if kind == "quote" else ""
            gaps.append(f"literal [{kind}] {lit!r} is in OLD but nowhere in NEW or --also (a literal is carried verbatim, or "
                        f"mapped \"literal:{lit}\": \"kept: <its new words>\" / \"moved: <path>#<heading>\" / \"dropped: <why>\"{home})")
    unknown = sorted(set(mapping) - {i["id"] for i in inv} - {f"literal:{l}" for _, l in old_lits})
    if unknown:
        gaps.append(f"map names ids the inventory does not have: {', '.join(unknown)}")
    ob, nb = blocks(old), blocks(new)
    for name, body in ob.items():
        if name not in nb:
            gaps.append(f"generated block <!-- {name}:begin --> is missing from NEW")
        elif nb[name] != body:
            gaps.append(f"generated block <!-- {name}:begin --> changed in NEW (it must be byte-identical)")
    gaps += ref_gaps(a.old, old, new, mapping, a.refs)
    n_rules = sum(1 for i in inv if i["id"].startswith("N"))
    what = f"{n_rules} normative sentences" + (f" and {len(inv) - n_rules} fact sentences and rows" if all_facts else "")
    print(f"{what}; {len(inv) - item_gaps} accounted for; {len(dropped)} dropped with a reason; {len(old_lits)} literals, "
          f"{len(lit_dropped)} dropped with a reason; {len(gaps)} gap(s)")
    for d in dropped + lit_dropped:
        print(f"  DROPPED  {d}")
    for g in gaps:
        print(f"  GAP      {g}")
    print(f"  {size_line(old, new)}")
    for s, lits in added(old, new, list(also.values())):
        print(f"  ADDED    {s}  [new: {', '.join(lits)}]")
    return 1 if gaps else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--keywords", default="", help="extra normative markers, comma-separated")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("inventory"); s.add_argument("old"); s.add_argument("--out"); s.add_argument("--all", action="store_true")
    s = sub.add_parser("literals"); s.add_argument("old")
    s = sub.add_parser("suggest"); s.add_argument("--old", required=True); s.add_argument("--new", required=True)
    s.add_argument("--also", nargs="*", default=[]); s.add_argument("--out"); s.add_argument("--all", action="store_true")
    s = sub.add_parser("added"); s.add_argument("--old", required=True); s.add_argument("--new", required=True)
    s.add_argument("--also", nargs="*", default=[])
    s = sub.add_parser("check"); s.add_argument("--old", required=True); s.add_argument("--new", required=True)
    s.add_argument("--map", required=True); s.add_argument("--also", nargs="*", default=[])
    s.add_argument("--all", action="store_true", help="account for every sentence and table row, not only the rules")
    s.add_argument("--refs", nargs="*", default=[], help="files whose `<OLD's name>` §X references must stay valid")
    a = p.parse_args(argv)
    a.keywords = DEFAULT_KEYWORDS + tuple(k.strip().lower() for k in a.keywords.split(",") if k.strip())
    return {"inventory": cmd_inventory, "literals": cmd_literals, "suggest": cmd_suggest, "added": cmd_added,
            "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
