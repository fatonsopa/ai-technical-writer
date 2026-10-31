# Supplied QA evidence: Edition-source import preview

Basis is the agreed IMP-01–IMP-08 behavior below. No original source repository inspection or production testing is available. This input is evidence for a completion assessment, not permission to perform more tests or release software.

IMP-01 edition authorization; IMP-02 non-writing row-validation preview; IMP-03 requester/edition binding and 15-minute expiry with the boundary invalid; IMP-04 atomic mappings/history and current-conflict recheck; IMP-05 repeat confirmation returns the committed result without new writes; IMP-06 exact-text university codes including 0042; IMP-07 honest interface feedback and timeout resolution through preview-ID lookup; IMP-08 attributable success history only.

Test plan exit criteria: every required behavior has passing evidence, all ten cases pass on the final candidate, no open acceptance defect. No release exception has been approved. Scope excludes XLSX, cross-edition imports, automatic correction, undo, and a performance guarantee.

Run IMPORT-R8, build import-candidate-8, isolated staging, 2026-10-29 10:00–12:00 UTC. C1 preview validation passed (IMP-02). C2 edition/role denial passed (IMP-01). C3 expiration boundary failed (IMP-03): confirmation at exactly 15 minutes succeeded. C4 concurrent mapping conflict passed (IMP-04). C5 history-insert rollback blocked (IMP-04): failure injection unavailable. C6 repeated confirmation passed (IMP-05). C7 exact-text code 0042 passed (IMP-06). C8 lost-response status resolution not run (IMP-07). C9 validation-error UI passed (IMP-07). C10 actor/history fields passed (IMP-08).

Totals: 7 passed, 1 failed, 1 blocked, 1 not run. Eight executed. No code-coverage percentage supplied. Evidence locators R8-C1 through R8-C10 correspond to these observations; no live artifact URLs are supplied. Bug IMPORT-B3 captures C3, cause unconfirmed. No fixed build exists yet. Test owner and release decision authority are unassigned. A completion report should preserve these limits and recommend an appropriate next step without claiming approval or success.
