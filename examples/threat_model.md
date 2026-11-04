# Website category change threats

Status: Illustrative proposed design; no production inspection, testing or risk acceptance is claimed.
Sources: This example's facts below; related [Low Level Design (LLD)](low_level_design.md).

## Scope and sources

Protect category integrity, authenticated administrator identity and the mutation journal for the administration feature. An administrator changes categories; ordinary members and external callers must not. Automated classification is a separate actor. This example assumes an existing authenticated database API and transactional mutation; it does not select an identity provider or claim its configuration was inspected. Billing and public website content ingestion are outside this change.

## System and trust boundaries

The browser is untrusted input, even when it displays administrator controls. Flow F1 sends website IDs and category intent from browser to database API across the authentication boundary. F2 validates caller/object permission and writes website state plus journal within one database transaction. F3 returns an acknowledgment to the browser; that response can be lost after commit. The automated classifier uses separate service authority, so its access must be reviewed independently of human administrator access.

## Threat scenarios

| ID | Asset/flow and actor | Abuse and consequence | Assessment |
| --- | --- | --- | --- |
| TH-01 | Category integrity, F1; member or forged client | Call the mutation directly, bypassing hidden UI controls, to change categories without administrator rights. | High-impact unauthorized write; exploitability depends on actual API grants and server checks, which are unverified. |
| TH-02 | Journal identity, F2; privileged client | Supply another user's actor value so a valid change is attributed to that user. | Accountability loss; inspect whether actor identity is derived from authentication. |
| TH-03 | State/journal, F2–F3; retrying authorized caller | Repeat an uncertain request after another administrator's later change, overwriting the newer choice. | Integrity and recovery risk; a timeout alone does not prove rollback. |

## Mitigations and residual risk

For TH-01, require server-side administrator/object permission before writes and restrict callable grants; UI restrictions provide usability only. For TH-02, derive the journal actor from the authenticated identity and commit mutation and history together. For TH-03, preserve uncertain outcomes and reconcile current values/history before a retry. These are proposed verification obligations for the example, not evidence that controls passed.

Last-committed-choice semantics still allow an authorized user to replace another choice. This residual exposure is documented, not accepted by this author. A product/security decision must determine whether optimistic conflict rejection is needed. The actual risk owner and decision remain unknown.

## Verification and open decisions

V-01 calls F1 as unauthenticated caller, ordinary member and administrator, then checks both state and history for forbidden writes. V-02 attempts a forged actor field and verifies recorded identity. V-03 interrupts acknowledgment after commit and compares the recovery view before retrying. All checks are planned and unexecuted.

Open decisions: confirm actual database grants, classifier authority and residual-risk owner. Revisit when roles, journal storage or retry behavior changes. This analysis does not claim coverage of the entire service or a secure implementation.
