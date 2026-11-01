# Technical Standard (STD)

A technical standard defines precise rules and how to verify them. Create it when a team needs consistent, checkable practice; update it when approved rules, constraints, checks, or exceptions change. A [Policy (POL)](policy.md) provides direction and accountability. A standard can implement that policy, but must not quietly invent its authority.

## Principles

- Define purpose, authority, scope, and the terms needed to interpret each rule.
- Explain the guiding principles, then state distinct rules with their conditions and exceptions.
- Make compliance observable. Give each material rule a concrete test, inspection, or measurement. If the source has no method, propose one derived from the existing rule and label it proposed. Preserve unknown tooling and approval; a proposed check is not a new product obligation or a claim that testing occurred.
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

Read the [Technical Standard (STD) example for Websites Review](../examples/technical_standard.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Read the actual rules and example, not just their headings. Are definitions and principles substantive? Does every rule have an independent compliance check? Verify scope, authority, units, exceptions, and preserved obligations. A standard must explain how a compliant result can be recognized.

## Sources

- [Stanford: governance distinctions](https://uit.stanford.edu/security/policies-standards)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174)
