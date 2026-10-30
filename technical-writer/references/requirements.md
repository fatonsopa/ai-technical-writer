# Writing individual requirements

Use this reference to write or review a requirement within a specification, issue, policy, or standard. Use `references/spec.md` for a complete behavioral specification. This file supplies the wording and verification method; it does not define a competing spec.

## Principles

- Give each requirement one clear obligation or constraint. Split independently verifiable results while keeping their shared condition explicit.
- State the relevant actor, trigger, input, outcome, and exception. Include error and permission conditions when they change the behavior.
- Use stable IDs within the governing document. Keep an ID when rewording the same requirement; do not reuse a retired ID for different behavior.
- Distinguish functional behavior, measurable quality constraints, and mandated design constraints. Do not prescribe a technology merely to fill in an unknown.
- Preserve obligation strength. “Must” states an obligation, “should” a recommendation, and “may” a permission in ordinary usage. Use RFC 2119/8174 capitalization only when the document adopts it.
- Specify how to verify the result. A test, measurement, inspection, or analysis must have an observable success condition.
- Keep the source and status visible. An assumption or proposed requirement is not an agreed product decision.

An optional EARS pattern is “When [event], the [system] must [response].” Use natural wording that preserves all conditions; do not force every requirement into one sentence pattern.

## Document structure

A requirement entry needs an ID, status/source, a precise statement, and a verification method. Add definitions and rationale when necessary to interpret it. The parent document owns overall scope, definitions, approvals, and change history.

For quality constraints, provide units and operating conditions: the dataset, load, measurement point, and threshold when agreed. Record an unknown threshold as a decision, not an invented number. A requirement that says only “fast,” “secure,” or “easy to use” needs clarification.

## Template

```md
### [Requirement ID]: [Short subject]

Status and source: [Agreed/proposed; exact spec section or decision]
Statement: [Condition, obligation or constraint, and exception]
Verification: [Inputs or setup, action, and expected result]
Rationale: [Useful reason, if it affects interpretation]
```

## Completed example

This fictional entry assumes the stated source requirement is agreed. It demonstrates one requirement rather than a complete feature spec.

```md
### REQ-02: Retain a saved workspace name

Status and source: Agreed in the workspace-renaming specification.
Statement: After a successful name update, a new workspace read must return the saved name.
Verification: Rename a workspace from Marketing Team to Growth Team, then read it in a new request. The read returns Growth Team.
Rationale: A success response must correspond to a change that later reads can observe.
```

## Quality check

Can a reviewer determine whether this requirement passes or fails? Check its source, status, conditions, units, exceptions, and requirement-to-verification mapping. Confirm that simplifying the wording did not change “only,” “unless,” “may,” or another boundary. Identify contradictions in the governing document rather than silently choosing a meaning.

## Sources

- [EARS: requirement patterns](https://alistairmavin.com/ears/)
- [RFC 2119: requirement levels](https://www.rfc-editor.org/rfc/rfc2119)
- [RFC 8174: capitalization and normative text](https://www.rfc-editor.org/rfc/rfc8174.txt)
