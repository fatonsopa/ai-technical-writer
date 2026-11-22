# Requirements-Quality Checklist (RQC)

A requirements-quality checklist tells an implementer which requirements are ready to build and which still need a decision. Each row checks one quality question against the requirement's text, cites the evidence and gives a verdict and the correction needed. It judges the requirements, not the code: a ticked row never means something was built or tested.

## Principles

- Check the requirement text at a named revision. Use [coverage resolution](implementation_plan.md#check-coverage-against-its-source) for references and judge meaning here.
- Ask one question per row, such as "Is it clear who may retry?" or "Is the limit measurable?".
- Quote or link the passage that answers it, give a verdict of Ready, Needs decision or Defect, and state the correction or the owner who decides.
- When a requirement changes, update only the affected rows and keep the earlier verdict with its revision.
- Don't record implementation or test status here; link those records instead.

## Structure

Name the specification and revision, then one row per question, then notes on decisions still needed.

## Template

```md
# [Specification] requirements-quality checklist

Specification: [Link], revision [revision].

## Checks
| Requirement | Question | Evidence | Verdict | Correction or owner |
| --- | --- | --- | --- | --- |
| [ID] | [Quality question] | [Quoted or linked passage] | [Ready / Needs decision / Defect] | [What must change, or who decides] |

## History
- [Revision and date: earlier verdict and what changed.]
```

## Completed example

Read the [Requirements-Quality Checklist (RQC) example for Websites Review](../examples/requirements_checklist.md). It finds an ambiguous retry rule and records its verdict before and after the clarification.

## Quality check

Can an implementer tell which requirements are ready and what blocks the rest? Check that each verdict cites its evidence and revision, and that every row judges the requirement text rather than reporting build or test status.

## Sources

- [ISO/IEC/IEEE 29148: characteristics of good requirements](https://www.iso.org/standard/72089.html)
