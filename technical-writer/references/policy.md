# Policy (POL)

A policy states an organization's direction, broad obligations, and accountability. Create it when governance needs an explicit agreement; update it when the authorized direction, scope, or responsibilities change. A [technical standard](technical_standard.md) turns that direction into precise, verifiable rules. Both can be binding; specificity and responsibility distinguish them.

## Principles

- Establish purpose, authority, scope, and precedence from real sources. Drafting a policy does not approve it.
- Define terms that affect interpretation and state the principles behind the obligations.
- Explain what people or systems are responsible for, why it matters, and how compliance is assessed. Detailed implementation steps belong in procedures.
- Identify who owns the policy and can approve exceptions when that authority is known. Preserve existing exceptions and their limits.
- Keep one owner for each obligation. Link standards and procedures rather than copying them.
- Use clear obligation words and keep proposal status explicit. Do not invent regulatory duties, review dates, owners, or approval.

## Structure

For this package, both the template and completed policy include Definitions and Principles. Add purpose/scope, obligations, responsibilities, compliance, exceptions, ownership/review, and related documents. A draft can identify missing authority rather than pretend it is adopted.

## Template

```md
# [Subject] policy
Status/authority: [Draft or confirmed adoption source]
## Purpose and scope
[Outcome, who/what is covered, exclusions]
## Definitions
[Terms that determine how obligations apply]
## Principles
[Guiding reasons and priorities]
## Policy obligations
[Required outcomes and broad responsibilities]
## Responsibilities and compliance
[Known accountable roles, assessment, response to gaps]
## Exceptions
[Actual approval authority, process, limits]
## Ownership, review, and related standards
[Known owner/triggers and linked detailed rules]
```

## Completed example

Fictional governance proposal. Its role assignments and obligations are assumptions for this example, not rules adopted by the user's project.

```md
# Application logging policy
Status/authority: Draft for review by the engineering lead.

## Purpose and scope
Application logs support diagnosis while protecting account data. This proposal covers production application logs; infrastructure access logs are outside its scope.

## Definitions
Request metadata describes a request without its confidential contents. Credentials include access tokens, session cookies, and passwords.

## Principles
Collect only information needed to diagnose service behavior. Keep requests traceable without exposing credentials.

## Policy obligations
Service teams must provide enough request metadata to investigate failures. Credentials must not appear in application logs. Detailed field and verification rules belong in the application logging standard.

## Responsibilities and compliance
Service owners review their logging behavior and remedy gaps found through tests and operational reviews. The engineering lead reviews policy changes.

## Exceptions
The engineering lead may approve additional non-sensitive diagnostic context for a documented incident. That approval does not permit logging credentials. The incident record must state the scope and end condition.

## Ownership, review, and related standards
The engineering lead owns this draft. Review it when logging architecture or data handling changes. The proposed application logging standard defines exact fields and checks; approval remains pending.
```

## Quality check

Can a reader identify the policy's purpose, authority, definitions, guiding principles, obligations, accountable roles, and exception limits? Confirm the example actually demonstrates those sections. Distinguish approved rules from a draft and broad direction from detailed standard requirements.

## Sources

- [Stanford: policies, standards, and guidelines](https://uit.stanford.edu/security/policies-standards)
- [University of Arizona: policy style and structure](https://policy.arizona.edu/policy-style-guide)
- Definitions and Principles are explicitly required by the user for this package's governance formats.
