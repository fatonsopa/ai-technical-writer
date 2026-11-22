# Critical Journeys (CJ)

A critical journey is a user path that matters enough to check end to end: losing it would hurt users, data or the business. Each journey names its actor, the ordered steps on mapped surfaces, the observable end state, why it is critical and the check that proves it. Write them so a tester can reach every screen and run every check.

## Principles

- Build each journey on surfaces from a [Feature Map (FM)](feature_map.md) or equivalent evidence. A step on an unknown screen stays unresolved until the screen is located.
- Give each journey a stable ID, the actor, numbered steps and the end state a tester can observe.
- Say why the journey is critical, with its source: a requirement, an incident or a reported risk.
- Link the test that checks it. If no test exists, say so; a planned or unrun test isn't a pass.
- Report results only from actual runs, with the run's date and candidate.

## Structure

Under a Journeys section, give each journey its own subsection with its ID and title, then the actor, criticality and source, steps, end state and check.

## Template

```md
# [Product area] critical journeys

## Journeys

### [CJ-1]: [Journey name]
Actor: [Who]. Criticality: [Why it matters, with source].
1. [Step on a mapped surface.]
End state: [What the tester observes.]
Check: [Test reference, or "No check exists yet".] Result: [Only from an actual run, with date and candidate.]
```

## Completed example

Read the [Critical Journeys (CJ) example for Websites Review](../examples/critical_journeys.md). Its journeys use the feature map's surfaces and test specification checks, and one keeps a missing check visible.

## Quality check

Can a tester find each screen from the feature map and run the named check? Check that every journey states its source of criticality and that nothing reports a pass without an actual run.

## Sources

- [Google Testing Blog: Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
