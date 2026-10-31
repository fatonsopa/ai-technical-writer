# Manual website category review policy

Status: Adopted for the Websites Review release
Authority and owner: Engineering lead, with product ownership of classification outcomes

## Purpose and scope

Manual review should resolve website classification problems without losing accountability for human decisions. This policy covers administrators assigning or clearing categories through website administration. It does not define automated provider rules or authorize changes to those rules.

## Definitions

**Manual decision** means an authenticated administrator's committed category assignment or clear action. **Change history** connects a modification to its actor and changed values. **Review** is the parked, unverified queue defined by the specification; it is not a general label for every imperfect website.

## Principles

Human decisions must be attributable. The interface must describe the actual outcome, including partial or uncertain completion. Review tools should expose outstanding work without changing existing lists' meaning. Recovery should preserve history and minimize unrelated changes.

## Policy obligations

Only authorized administrators may make manual category decisions. Every committed decision must retain enough history to identify the actor and understand the change. A technical failure must not be presented as a confirmed successful decision.

Administrators must inspect the intended scope before a bulk action. When an operation stops partway through, confirmed changes must remain distinguishable from unresolved work. A later correction must be recorded as another attributable change rather than erasing the original decision.

Engineering must keep queue classification consistent across readers. Product owns decisions that change what Review or Pending means. A design or implementation change cannot silently redefine those expectations.

## Responsibilities and compliance

Administrators are responsible for their selected category and target websites. Engineering owns permission enforcement, persistence, and change-history integrity. QA assesses the [technical standard](technical_standard.md) and SDD checks. Product reviews scope and administrator-facing language.

Release review must consider authorization failures, missing attribution, misleading partial results, and queue omissions. An unresolved failure requires a documented hold or an explicitly authorized scope decision. A green build alone does not demonstrate compliance.

## Exceptions

The engineering lead may approve a temporary alternative interface when the primary tool is unavailable. The exception must identify scope, duration or end condition, and verification. It cannot waive administrator authorization or attributable history.

An emergency correction still requires an identifiable actor and retained evidence. Incident urgency does not authorize deleting history or restoring unrelated records.

## Ownership, review, and related standards

Review this policy when manual-review roles, queue meaning, or mutation paths change. The [technical standard](technical_standard.md) defines enforcement checks, the [how-to](how_to_guide.md) describes administrator actions, and the [SDD](spec_driven_development.md) owns feature behavior.
