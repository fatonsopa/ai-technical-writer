#!/usr/bin/env python3
"""Tests for zero_loss.py: a rewrite that loses a rule or a fact fails; one that accounts for every rule passes.

Each group runs on its own and reports PASS or FAIL, so one broken group does not hide the others. The groups F1 to F6
are CG-1585's: the six cases of plan 14's rewrite (scratchpad mutate.py) rebuilt here as small fixtures, each a detail
cut from a draft that passed the check of 21 October 2026.
"""
import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path

ISSUE = "XY-1538"  # an issue id of the shape the inventory recognises; not a real issue

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import zero_loss  # noqa: E402 — the module under test

TESTS = []


def test(fn):
    TESTS.append(fn)
    return fn


class Run:
    def __init__(self, returncode, stdout, stderr=""):
        self.returncode, self.stdout, self.stderr = returncode, stdout, stderr


def run(*args):
    """zero_loss.main on these arguments, with what it printed. An unknown option exits 2, as argparse does."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = zero_loss.main([str(a) for a in args])
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 2
    return Run(code, out.getvalue(), err.getvalue())


def write(d: Path, name: str, text: str) -> Path:
    p = d / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    return p


def mapfile(d: Path, name: str, mapping: dict) -> Path:
    return write(d, name, json.dumps(mapping))


def check(old: Path, new: Path, mp: Path, *more):
    return run("check", "--old", old, "--new", new, "--map", mp, *more)


# --- The contract as it stood before CG-1585: rules counted, literals carried, generated blocks byte-identical. ------

OLD = f"""# Rules
Every push must run its tests first. The owner likes
coffee. Run `bash scripts/pipeline/gate.sh --strict` within 10 minutes; see scripts/pipeline/gate.sh and {ISSUE}.
- **A wrapped bullet** must stay
  one sentence when its lines are joined.
- A helper never changes the generated types.
1. Open the board.
2. Type "FORCE DELETE staging" when asked.
<!-- gen:begin -->
| a | b |
<!-- gen:end -->
| When | Rule |
|---|---|
| a run is open | The issue stays In Progress only while the run is open. |
"""
NEW_OK = f"""# Rules
## Tests before a push
Run the tests before every push: `bash scripts/pipeline/gate.sh --strict`, within 10 minutes (scripts/pipeline/gate.sh, {ISSUE}).
Then: 1. Open the board. 2. Type "FORCE DELETE staging" when asked.
## Bullets
A bullet stays one sentence when its wrapped lines are joined.
## Generated types
No helper changes the generated types; the land queue refuses it.
<!-- gen:begin -->
| a | b |
<!-- gen:end -->
## Status while a run is open
An open run keeps its issue In Progress.
"""
NEW_LOST = NEW_OK.replace("## Generated types\nNo helper changes the generated types; the land queue refuses it.\n", "")
NEW_BLOCK_CHANGED = NEW_OK.replace("| a | b |", "| a | c |")


@test
def existing_contract(d: Path):
    old, new = write(d, "old.md", OLD), write(d, "new.md", NEW_OK)
    lost, block = write(d, "lost.md", NEW_LOST), write(d, "block.md", NEW_BLOCK_CHANGED)
    adr = write(d, "adr.md", "# Decision\n## Tests first\nWe decided tests run first.\n")
    url = write(d, "url.md", "See https://diataxis.fr/reference/, read 2026-10-20.\n")

    r = run("literals", old)
    assert r.returncode == 0
    for lit in ["bash scripts/pipeline/gate.sh --strict", "scripts/pipeline/gate.sh", ISSUE, "10 minutes",
                "FORCE DELETE staging", "Rules"]:
        assert lit in r.stdout, f"literal {lit!r} not inventoried:\n{r.stdout}"
    assert "coffee" not in r.stdout
    assert "[url    ] https://diataxis.fr/reference/" in run("literals", url).stdout, "a URL ends before the comma that follows it"

    r = run("inventory", old)
    assert r.returncode == 0, r.stderr
    assert "6 normative sentences" in r.stdout, r.stdout
    assert "Open the board." in r.stdout, "a numbered step is inventoried with or without a rule word: " + r.stdout
    assert "**" not in r.stdout, "bold marks are stripped from an inventoried sentence: " + r.stdout
    assert "A wrapped bullet must stay one sentence when its lines are joined." in r.stdout, "hard-wrapped lines are joined"
    assert "coffee" not in r.stdout, "a sentence with no rule in it is not normative"
    assert "N6" in r.stdout and "In Progress" in r.stdout, "table cells are sentences too"

    good = {"N1": "kept: Tests before a push", "N2": "kept: Bullets", "N3": "kept: Generated types",
            "N4": "kept: Open the board", "N5": "kept: FORCE DELETE staging", "N6": "kept: Status while a run is open"}
    mp = mapfile(d, "map.json", good)
    r = check(old, new, mp)
    assert r.returncode == 0, r.stdout + r.stderr

    r = check(old, lost, mp)
    assert r.returncode == 1 and "N3 kept, but NEW has no heading" in r.stdout, r.stdout

    nocmd = write(d, "nocmd.md", NEW_OK.replace("`bash scripts/pipeline/gate.sh --strict`, within 10 minutes", "the gate, soon"))
    r = check(old, nocmd, mp)
    assert r.returncode == 1, "a paraphrased-away command or number is a loss: " + r.stdout
    assert "literal [code] 'bash scripts/pipeline/gate.sh --strict'" in r.stdout and "'10 minutes'" in r.stdout, r.stdout
    mp7 = mapfile(d, "map7.json", {**good, "literal:bash scripts/pipeline/gate.sh --strict": "dropped: the gate runs by itself now",
                                   "literal:10 minutes": "dropped: no time limit any more"})
    r = check(old, nocmd, mp7)
    assert r.returncode == 0 and "DROPPED  [code] bash scripts/pipeline/gate.sh --strict" in r.stdout, r.stdout

    r = check(old, lost, mapfile(d, "map2.json", {k: v for k, v in good.items() if k != "N3"}))
    assert r.returncode == 1 and "N3 not in map" in r.stdout, r.stdout

    r = check(old, lost, mapfile(d, "map3.json", {**good, "N3": "dropped: types"}))
    assert r.returncode == 1 and "without a reason of at least three words" in r.stdout, r.stdout

    r = check(old, lost, mapfile(d, "map4.json", {**good, "N3": "dropped: the generated types rule moved to CLAUDE.md §3k on 19 Oct"}))
    assert r.returncode == 0 and "DROPPED  N3" in r.stdout, r.stdout

    r = check(old, new, mapfile(d, "map5.json", {**good, "N1": f"moved: {adr}#Tests first"}))
    assert r.returncode == 0, r.stdout
    r = check(old, new, mapfile(d, "map6.json", {**good, "N1": f"moved: {adr}#No such heading"}))
    assert r.returncode == 1 and "no such heading" in r.stdout, r.stdout

    r = check(old, block, mp)
    assert r.returncode == 1 and "gen:begin --> changed" in r.stdout, r.stdout
    ex = write(d, "ex.md", "# Doc\nAn example marker `<!-- name:begin --> … <!-- name:end -->` is only an example.\n")
    assert zero_loss.blocks(ex.read_text()) == {}, "a marker inside a code span is not a generated block"

    r = run("suggest", "--old", old, "--new", new)
    assert r.returncode == 0
    sugg = json.loads(r.stdout)
    assert sugg["N3"] == "kept: Generated types", sugg


# --- F1 (loss L1): a quoted passage is a literal, whatever its length, across line breaks, in italics or not. --------

OLD_Q = """# Moving the repository
Written 21 October 2026.

## Transfer
GitHub says "If you create a new repository or fork at the previous repository location,
the redirects to the transferred repository will be permanently deleted."

Faton, 21 October 2026: *"Does the planning include specific instructions on how to do it on the line? For example,
how to create a GitHub identity for an agent?"*

Type "FORCE DELETE staging" to confirm.
"""
NEW_Q = """# Moving the repository
Written 21 October 2026.

## Transfer
GitHub says "If you create a new repository or fork at the previous repository location, the redirects to the
transferred repository will be permanently deleted."

Faton asked on 21 October 2026: *"Does the planning include specific instructions on how to do it on the line? For
example, how to create a GitHub identity for an agent?"*

Type "FORCE DELETE staging" to confirm.
"""
VENDOR = ("If you create a new repository or fork at the previous repository location, the redirects to the transferred "
          "repository will be permanently deleted.")
OWNER = ("Does the planning include specific instructions on how to do it on the line? For example, how to create a "
         "GitHub identity for an agent?")


@test
def f1_quotes_are_literals(d: Path):
    lits = {lit: kind for kind, lit in zero_loss.literals(OLD_Q)}
    assert lits.get(VENDOR) == "quote", "a two-line vendor quote of any length is a literal: " + json.dumps(lits, indent=1)
    assert lits.get(OWNER) == "quote", "an italic quote *\"…\"* is a literal: " + json.dumps(lits, indent=1)
    old, ok, empty = write(d, "old.md", OLD_Q), write(d, "new.md", NEW_Q), mapfile(d, "map.json", {})
    r = check(old, ok, empty)
    assert r.returncode == 0, "a quote carried word for word, wrapped anew, passes: " + r.stdout

    # mutate.py case 3: GitHub's two-line warning paraphrased away.
    vendor_lost = write(d, "vendor.md", NEW_Q.replace(
        'GitHub says "If you create a new repository or fork at the previous repository location, the redirects to the\n'
        'transferred repository will be permanently deleted."', "GitHub warns against it."))
    r = check(old, vendor_lost, empty)
    assert r.returncode == 1 and "literal [quote]" in r.stdout, "a lost vendor quote is a gap: " + r.stdout

    # loss L1: the owner's words restated, and the only copy of them gone.
    owner_lost = write(d, "owner.md", NEW_Q.replace(
        'Faton asked on 21 October 2026: *"Does the planning include specific instructions on how to do it on the line? For\n'
        'example, how to create a GitHub identity for an agent?"*', "On 21 October 2026 Faton asked for the steps one click at a time."))
    r = check(old, owner_lost, empty)
    assert r.returncode == 1 and "literal [quote]" in r.stdout, "the owner's paraphrased quote is a gap: " + r.stdout

    r = check(old, owner_lost, mapfile(d, "nohome.json", {f"literal:{OWNER}": "dropped: restated in plain words in the guide"}))
    assert r.returncode == 1 and "where the original words live" in r.stdout, "a quote dropped with no other home is a gap: " + r.stdout
    r = check(old, owner_lost, mapfile(d, "home.json", {f"literal:{OWNER}": "dropped: his words stay in XY-1561's description"}))
    assert r.returncode == 0 and "DROPPED  [quote]" in r.stdout, "a quote whose account names its home passes: " + r.stdout
    r = check(old, owner_lost, mapfile(d, "url.json", {
        f"literal:{OWNER}": "kept: restated; the words are at https://linear.app/x/issue/XY-1561#comment-1"}))
    assert r.returncode == 0, "a restated quote whose account names a URL passes: " + r.stdout


# --- F2 (loss L2): facts with no rule word are counted (--all), and bare numbers, clock times, versions are literals. --

OLD_F = """# The test machine
Written 21 October 2026.

## Counts
`src/test` holds 3,298 test files and about 12,468 test cases (counted 21 October 2026).
The runner has 16 cores (AMD EPYC-Milan) and 61 GB RAM.
The last run ended at 13:05 UTC on Docker 28.0.4.

## Branch protection
On the rule for `dev`: **Require a pull request before merging**; **Require approvals** = 1; **Require review from Code Owners**.
"""
NEW_F = """# The test machine
Written 21 October 2026.

## Counts
`src/test` holds 3,298 test files and about 12,468 test cases (counted 21 October 2026).
The runner has 16 cores (AMD EPYC-Milan) and 61 GB RAM.
The last run ended at 13:05 UTC on Docker 28.0.4.

## Branch protection
On the rule for `dev`, set these options:

| Option | Setting |
|---|---|
| **Require a pull request before merging** | on |
| **Require approvals** | 1 |
| **Require review from Code Owners** | on |
"""


@test
def f2_facts_and_numbers(d: Path):
    lits = set(zero_loss.literals(OLD_F))
    for want in [("count", "3,298 test"), ("count", "12,468 test"), ("count", "16 cores"), ("time", "13:05 UTC"), ("version", "28.0.4")]:
        assert want in lits, f"{want} is a literal: {sorted(lits)}"
    assert ("count", "10") not in set(zero_loss.literals("Run it within 10 minutes.\n")), "a number with its unit is one literal"
    old, ok = write(d, "old.md", OLD_F), write(d, "new.md", NEW_F)
    rules = mapfile(d, "rules.json", {"N1": "kept: Branch protection"})
    r = check(old, ok, rules)
    assert r.returncode == 0, "the honest rewrite passes with a rules-only map: " + r.stdout

    # mutate.py case 1: the test-file counts, a fact with no rule word.
    counts = write(d, "counts.md", NEW_F.replace(
        "`src/test` holds 3,298 test files and about 12,468 test cases (counted 21 October 2026).", "`src/test` holds many test files."))
    r = check(old, counts, rules)
    assert r.returncode == 1 and "'3,298 test'" in r.stdout and "'12,468 test'" in r.stdout, "lost counts are gaps: " + r.stdout

    # mutate.py case 4: a measurement whose unit word is on no list.
    # The real draft also holds "| 16 | 64 GB |" in a table of machine sizes, so the number alone is still there.
    cores = write(d, "cores.md", NEW_F.replace("16 cores (AMD EPYC-Milan) and 61 GB RAM", "a large machine with 61 GB RAM")
                  + "\n| Cores | Memory |\n|---|---|\n| 16 | 64 GB |\n")
    r = check(old, cores, rules)
    assert r.returncode == 1 and "literal [count] '16 cores'" in r.stdout, "a lost '16 cores' is a gap: " + r.stdout

    when = write(d, "when.md", NEW_F.replace("ended at 13:05 UTC on Docker 28.0.4", "ended in the afternoon on a recent Docker"))
    r = check(old, when, rules)
    assert r.returncode == 1 and "'13:05 UTC'" in r.stdout and "'28.0.4'" in r.stdout, "a lost time and version are gaps: " + r.stdout

    r = run("inventory", old)
    assert "Require approvals = 1;" not in r.stdout, "without --all, a fact sentence is not counted: " + r.stdout
    r = run("inventory", "--all", old)
    assert r.returncode == 0 and "F" in r.stdout and "Require approvals = 1;" in r.stdout, "--all counts every sentence: " + r.stdout
    assert "The runner has 16 cores (AMD EPYC-Milan) and 61 GB RAM." in r.stdout, r.stdout
    assert "N1: On the rule for `dev`: Require a pull request before merging;" in r.stdout, "N ids do not move under --all: " + r.stdout

    # mutate.py case 2: a setting with no rule word, "Require approvals = 1", cut from the new table.
    r = run("suggest", "--all", "--old", old, "--new", ok)
    assert r.returncode == 0, r.stdout
    full = json.loads(r.stdout)
    assert any(k.startswith("F") for k in full), "suggest --all pre-fills the fact sentences: " + r.stdout
    mp = mapfile(d, "all.json", full)
    r = check(old, ok, mp, "--all")
    assert r.returncode == 0, "suggest's map on the honest draft passes --all: " + r.stdout
    no_row = write(d, "norow.md", NEW_F.replace("| **Require approvals** | 1 |\n", ""))
    r = check(old, no_row, mp, "--all")
    assert r.returncode == 1 and "Require approvals = 1" in r.stdout, "the cut setting is a gap under --all: " + r.stdout
    r = check(old, no_row, mp)
    assert r.returncode == 1, "a map that holds F ids is checked as --all even without the flag: " + r.stdout

    tabled = write(d, "tabled.md", "# T\n\n| Step | Who |\n|---|---|\n| S1 | Faton |\n| S2 | the AI |\n")
    r = run("inventory", "--all", tabled)
    assert "S1 | Faton" in r.stdout and "Step | Who" not in r.stdout, "--all counts every table row but the header: " + r.stdout


# --- F3 (loss L3): a "kept" account must name the place that holds the sentence's content. --------------------------

OLD_V = """# Move the repository
## S3 — Move the repository into the organization
1. Open the repository's **Settings**.
2. Click **Transfer**.

TODO: verify that Vercel's Git connection for the staging and production projects follows the transfer, before the
transfer: a deploy that stops is the risk.

## S4 — Point the laptop at the new address
Run `git remote set-url origin <new URL>` before the next fetch.
"""
NEW_V = """# Move the repository
## S3 — Move the repository into the organization (Faton)
**Vercel first.** TODO: verify that Vercel's Git connection for the staging and production projects follows the
transfer. Check it before the transfer, because the risk is that deploys stop.

1. Open the repository's **Settings**.
2. Click **Transfer**.

## S4 — Point the laptop at the new address (AI)
Run `git remote set-url origin <new URL>` before the next fetch.
"""


@test
def f3_kept_names_the_place(d: Path):
    old, ok = write(d, "old.md", OLD_V), write(d, "new.md", NEW_V)
    honest = {"N1": "kept: Open the repository's", "N2": "kept: Click **Transfer**",
              "N3": "kept: that Vercel's Git connection for the staging and production projects follows the transfer",
              "N4": "kept: S4 — Point the laptop at the new address (AI)"}
    r = check(old, ok, mapfile(d, "honest.json", honest))
    assert r.returncode == 0, "accounts that name where the content sits pass: " + r.stdout
    r = check(old, ok, mapfile(d, "heading.json", {**honest, "N3": "kept: S3 — Move the repository into the organization (Faton)"}))
    assert r.returncode == 0, "a heading whose section holds the content passes: " + r.stdout

    # mutate.py case 6: the TODO sentence cut, its account pointed at the S3 heading, which still exists.
    cut = write(d, "cut.md", NEW_V.replace(
        "**Vercel first.** TODO: verify that Vercel's Git connection for the staging and production projects follows the\n"
        "transfer. Check it before the transfer, because the risk is that deploys stop.\n", ""))
    r = check(old, cut, mapfile(d, "cut.json", {**honest, "N3": "kept: S3 — Move the repository into the organization (Faton)"}))
    assert r.returncode == 1 and "N3 kept" in r.stdout and "content words" in r.stdout, "the place lacks the sentence: " + r.stdout

    # the place must hold the sentence's literals too, not only words that exist somewhere else in NEW.
    moved_cmd = write(d, "cmd.md", NEW_V.replace("Run `git remote set-url origin <new URL>` before the next fetch.",
                                                 "Run the remote command before the next fetch.")
                      + "\n## Commands\n`git remote set-url origin <new URL>`\n")
    r = check(old, moved_cmd, mapfile(d, "cmd.json", {**honest, "N4": "kept: before the next fetch"}))
    assert r.returncode == 1 and "git remote set-url origin <new URL>" in r.stdout and "N4 kept" in r.stdout, \
        "the place that holds the cited words lacks the sentence's command: " + r.stdout


# --- F4 (loss L4): section numbers other files cite still name a section of NEW. -------------------------------------

OLD_R = """# Testing in CI
## 1. Where the tests run
Every suite runs on its own database.
## 2a. The suites' databases, today and in GitHub
Each suite gets a fresh database.
"""
NEW_R_RENUMBERED = """# Testing in CI
## 1. Where the tests run
Every suite runs on its own database.
## 3. The suites' databases, today and in GitHub
Each suite gets a fresh database.
"""
MASTER = "# Master\nThe suites run on their own database (`01-02-spec-testing-in-ci.md` §2a); see `01-02` §1 and §2a.\n"


@test
def f4_cited_section_numbers(d: Path):
    old = write(d, "old/01-02-spec-testing-in-ci.md", OLD_R)
    same = write(d, "same/01-02-spec-testing-in-ci.md", OLD_R)
    renum = write(d, "new/01-02-spec-testing-in-ci.md", NEW_R_RENUMBERED)
    master = write(d, "00-master.md", MASTER)
    # mutate.py case 5, with the map updated the way the writer updates it: both accounts follow the new number.
    mp = mapfile(d, "map.json", {"N1": "kept: 1. Where the tests run", "N2": "kept: 3. The suites' databases, today and in GitHub",
                                 "literal:2a. The suites' databases, today and in GitHub": "kept: 3. The suites' databases, today and in GitHub"})
    r = check(old, renum, mp)
    assert r.returncode == 0, "without --refs the renumbering passes, as it did on 21 October: " + r.stdout
    r = check(old, renum, mp, "--refs", master)
    assert r.returncode == 1 and "§2a" in r.stdout and "00-master.md:2" in r.stdout, "a cited number that moved is a gap: " + r.stdout
    assert "§1" not in r.stdout.split("gap(s)")[1], "a cited number that still holds is not reported: " + r.stdout
    r = check(old, same, mapfile(d, "same.json", {"N1": "kept: 1. Where the tests run", "N2": "kept: Each suite gets"}), "--refs", master)
    assert r.returncode == 0, "unchanged numbers pass --refs: " + r.stdout


# --- F5 (loss L5): the sentences a rewrite adds that carry a fact the old document did not hold are listed. ----------

@test
def f5_added_claims_are_listed(d: Path):
    old = write(d, "old.md", "# Flow\n## Stages\nThe author opens a draft pull request into `dev`.\nThe staging workflow deploys every merge.\n")
    new = write(d, "new.md", "# Flow\n## Stages\nThe author opens a draft pull request into `dev`.\nThe staging workflow deploys every merge.\n"
                             "The table in `01-02` §1 follows this recommendation.\nThe staging run takes 12 minutes on GitHub's machines.\n")
    r = run("added", "--old", old, "--new", new)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "The table in `01-02` §1 follows this recommendation." in r.stdout, "an added cross-reference is listed: " + r.stdout
    assert "The staging run takes 12 minutes on GitHub's machines." in r.stdout, "an added measurement is listed: " + r.stdout
    assert "draft pull request" not in r.stdout, "a sentence OLD already held is not listed: " + r.stdout
    r = check(old, new, mapfile(d, "map.json", {"N1": "kept: The staging workflow deploys every merge"}))
    assert r.returncode == 0 and "ADDED" in r.stdout and "12 minutes" in r.stdout, "check lists added claims too: " + r.stdout


# --- F6 (loss L6): the check reports how much the rewrite grew. ------------------------------------------------------

@test
def f6_growth_is_reported(d: Path):
    old = write(d, "old.md", "# Flow\nThe staging workflow deploys every merge.\n")
    new = write(d, "new.md", "# Flow\n\n## Stages\n\nThe staging workflow deploys every merge.\n\n## More\n\nMore words.\n")
    r = check(old, new, mapfile(d, "map.json", {"N1": "kept: The staging workflow deploys every merge"}))
    assert r.returncode == 0, r.stdout
    assert "SIZE" in r.stdout and "2 → 9 lines" in r.stdout and "more than a quarter" in r.stdout, "growth is reported: " + r.stdout
    r = check(new, old, mapfile(d, "map2.json", {"N1": "kept: The staging workflow deploys every merge"}))
    assert "more than a quarter" not in r.stdout, "a rewrite that shrank needs no reason: " + r.stdout


# --- CG-2631: a document compared with itself holds every one of its own literals. ----------------------------------

SELF = """# Wipe

The run deleted 1172 import jobs, 1555 api_requests and 231339 import_logs.

A verdict of "or" leaves the row alone, and 223 guard files carried the old line.
"""


def self_literal_gaps(text: str) -> list[str]:
    """The literals of `text` that the check would report missing from `text` itself. A literal is a run of characters
    the document holds, so this list is empty for every document; a literal that is not is one the extraction made up."""
    hay = zero_loss.norm(text)
    return [f"[{kind}] {lit!r}" for kind, lit in zero_loss.literals(text)
            if not zero_loss.present(kind, zero_loss.norm(lit), hay)]


@test
def self_comparison_reports_nothing_missing(d: Path):
    """A document compared with itself must report nothing missing. Before the fix the bare-number scan ran over text
    whose already-found literals had been cut out with a single space, so it read fragments of real words: "1172 import
    jobs" became "1172 imp" once the quoted value "or" was cut from "import", and "223 guard files" became "223 files".
    The trailing word also stopped at an underscore, so "1555 api_requests" became "1555 api" — a fragment the check
    then looked for as a whole token and never found."""
    doc = write(d, "self.md", SELF)
    r = check(doc, doc, mapfile(d, "map.json", {}))
    literal_gaps = [l.strip() for l in r.stdout.splitlines() if "GAP" in l and "literal [" in l]
    assert not literal_gaps, f"a document compared with itself lost {len(literal_gaps)} literal(s):\n" + "\n".join(literal_gaps)
    assert self_literal_gaps(SELF) == [], self_literal_gaps(SELF)


@test
def self_comparison_holds_for_the_repositorys_own_documents(d: Path):
    """The property above is true of every document, so it runs over the real ones: this repository's standards, its
    CLAUDE.md and the skill's own pages. (The skill folder also installs on its own, so a missing repository is no
    failure.)"""
    repo = HERE.parents[3]
    files = sorted(repo.glob(".claude/standards/*.md")) + sorted((HERE.parent / "references").glob("*.md"))
    for name in ("CLAUDE.md", ".claude/skills/technical-writer/SKILL.md"):
        if (repo / name).exists():
            files.append(repo / name)
    if not files:
        return
    gaps = [f"{f.relative_to(repo)}: {g}" for f in files for g in self_literal_gaps(f.read_text(encoding="utf-8"))]
    assert not gaps, (f"{len(gaps)} literal(s) are missing from the very file they were read from, over {len(files)} "
                      "documents:\n" + "\n".join(gaps[:12]))


def main() -> int:
    failed = []
    for fn in TESTS:
        with tempfile.TemporaryDirectory() as d:
            try:
                fn(Path(d))
                print(f"PASS  {fn.__name__}")
            except Exception as e:  # noqa: BLE001 — every failure is reported, then the run fails
                failed.append(fn.__name__)
                print(f"FAIL  {fn.__name__}: {type(e).__name__}: {e}")
    if failed:
        print(f"zero_loss.test.py: {len(failed)} of {len(TESTS)} groups failed: {', '.join(failed)}")
        return 1
    print(f"zero_loss.test.py: {len(TESTS)} groups passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
