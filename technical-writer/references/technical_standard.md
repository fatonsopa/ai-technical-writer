# Technical Standard (STD)

A technical standard defines precise rules and how to verify them. Create it when a team needs consistent, checkable practice; update it when approved rules, constraints, checks, or exceptions change. A [policy](policy.md) provides direction and accountability. A standard can implement that policy, but must not quietly invent its authority.

## Principles

- Define purpose, authority, scope, and the terms needed to interpret each rule.
- Explain the guiding principles, then state distinct rules with their conditions and exceptions.
- Make compliance observable. Give each material rule a concrete test, inspection, or measurement.
- Preserve obligation strength and exact contracts when editing. Use RFC uppercase terms only when the document explicitly adopts them.
- Keep useful rationale near a difficult rule; remove repeated justification and incident history.
- Record actual exception authority and limits. Link the governing policy and owned procedures rather than repeating them.

## Structure

Both the template and completed example must include Definitions, Principles, Rules, and Verification. Also establish purpose/scope, authority, responsibilities, exceptions, and ownership/review. Use ordinary language unless a defined normative convention is needed.

## Template

```md
# [Subject] standard
Status/authority: [Source and adoption state]
## Purpose and scope
[Who/what must comply; relevant exclusions]
## Definitions
[Terms and units affecting the rules]
## Principles
[Reasons that guide the choices]
## Rules
- [ID]: [Precise obligation, conditions, exceptions]
## Verification
| Rule | Method and compliant result |
| --- | --- |
| [ID] | [Test/inspection/measurement] |
## Responsibilities and exceptions
[Known authority, approved deviations, limits]
## Ownership, review, and related policy
[Owner, review triggers, governing links]
```

## Completed example

Fictional standard proposed under the logging policy example; its values are illustrative agreements, not universal recommendations.

```md
# Application request logging standard
Status/authority: Proposed under the application logging policy.

## Purpose and scope
These rules cover completed production HTTP requests recorded by the application. Infrastructure access logs follow separate rules.

## Definitions
A request ID links one request's records. A route pattern is the matched route template, not a URL containing user-supplied values. Duration is elapsed processing time in milliseconds.

## Principles
Make failures traceable while minimizing captured data. Use consistent fields so automated checks can identify missing information.

## Rules
- LOG-01: Each completed request must record its request ID, method, route pattern, response status, and duration in milliseconds.
- LOG-02: Application logs must not contain access tokens, session cookies, or plaintext passwords.
- LOG-03: Recorded timestamps must identify UTC.
- LOG-04: A user-visible API error must include the request ID needed to find its server record.

## Verification
| Rule | Method and compliant result |
| --- | --- |
| LOG-01 | Send a successful and failed request; each record contains all five fields with the stated duration unit. |
| LOG-02 | Send distinctive synthetic credential values; none appears in captured application logs. |
| LOG-03 | Inspect those records; every timestamp explicitly identifies UTC. |
| LOG-04 | Trigger an API error; its request ID locates the corresponding server record. |

## Responsibilities and exceptions
Service owners maintain the checks. The policy's incident exception permits additional non-sensitive context only; it cannot waive LOG-02. No exception has been approved in this example.

## Ownership, review, and related policy
The engineering lead owns this proposal. Review it when logging contracts change. The proposed application logging policy supplies its direction; neither document is claimed as adopted.
```

## Quality check

Read the actual rules and example, not just their headings. Are definitions and principles substantive? Does every rule have an independent compliance check? Verify scope, authority, units, exceptions, and preserved obligations. A standard must explain how a compliant result can be recognized.

## Sources

- [Stanford: governance distinctions](https://uit.stanford.edu/security/policies-standards)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174)
