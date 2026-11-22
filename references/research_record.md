# Research Record (RR)

A research record answers a question that a design or decision depends on. It states the question, the sources actually consulted, what they show, what remains uncertain and who owns the decision. Write one when a design choice needs evidence first; record the choice itself in a [Decision Record (DR)](decision_record.md).

## Principles

- State the question so that the answer would change the design. A general topic isn't a research question.
- Cite each source you actually read or were given, with its revision or date. Quote or link the governing passage, not a paraphrase of it. A summary or symptom report is evidence of what someone said, not of the rule.
- Keep findings, inferences and uncertainty apart. A likely cause stays an inference until a source confirms it.
- Compare the real alternatives and say what each source shows about them.
- A recommendation is not a decision. A study or working prototype shows what is possible; approval stays with the decision owner. Name that owner and the decision's state.
- If a governing source is missing or unreadable, record the gap and keep every conclusion that depends on it open.

## Structure

Start with the question and why it matters, then the sources, findings, alternatives, uncertainty and gaps, the recommendation and the decision owner with the decision's state.

## Template

```md
# [Question in a few words]

## Question
[The question, and the design or decision that depends on it.]

## Sources
- [Source, revision or date, and what was read.]

## Findings
[What the sources show, citing the governing passage.]

## Alternatives
| Option | What the evidence shows |
| --- | --- |
| [Option] | [Support, conflict or gap, with source] |

## Uncertainty and gaps
[What is unknown, missing or inferred, and which conclusions it affects.]

## Recommendation and decision owner
[Supported recommendation. Decision owner and state: open, accepted, superseded.]
```

## Completed example

Read the [Research Record (RR) example for bulk-edit retries](../examples/research_record.md). It traces a paraphrased symptom report back to WEB-09 and leaves the decision with its owner.

## Quality check

Can a designer follow each finding to its source and see which decision is still open and who owns it? Check that no paraphrase stands in for the governing passage, no inference is presented as a finding and no recommendation is presented as approved.

## Sources

- [GOV.UK Service Manual: user research](https://www.gov.uk/service-manual/user-research)
