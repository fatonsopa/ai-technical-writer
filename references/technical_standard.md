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

These are information requirements, not a requirement to repeat “Applicability,” “Inspection,” or “Expected evidence” under every rule. Follow [Writing Style (WS)](writing_style.md) when choosing prose, bullets and tables. Keep rule IDs when they support traceability; let each rule's complexity determine its presentation. A fixed record layout is useful when an actual reader or machine consumer needs those fields.

Keep one coherent standard together by default, with linked contents when navigation warrants it. Separate material only for a distinct purpose, audience, owner or loading need that justifies the extra navigation. Common verification and exception rules belong once with their owner; retain control-specific conditions and checks beside the control. Do not repeat the same evidence instructions in both each rule and a verification table.

For example, an access-control rule can combine a requirement with independent checks:

> **ACCESS-01 — Object authorization**
>
> Protected objects must be accessible only to callers authorized for the requested action.
>
> - Trace trusted caller and tenant identity to the authorization decision before the protected effect.
> - Inspect alternate APIs, background jobs and cache hits that can reach the same object.
> - Compare an unauthorized request with a legitimate request that must remain permitted.
>
> Authentication or an opaque object identifier alone does not establish authorization.

This illustrates a hypothetical rule's layout, not a new obligation for every project. Preserve the actual project's scope and the source's conditions. Keep relevant sources and versions compact and traceable; citations neither approve a rule nor establish its implementation.

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

Can a practitioner find the rule and assess its separate checks without decoding a dense paragraph or repetitive form? Compare shortened rules with their source, including exceptions and counterexamples. Do not remove necessary detail to meet a size target.

## Sources

- [Stanford: governance distinctions](https://uit.stanford.edu/security/policies-standards)
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174)
