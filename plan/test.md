# SpecDev handoff test specification

Use the [governing specification](../openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md) and the candidate's [task list](../openspec/changes/ship-specdev/tasks.md). The first two checks are read-only checks of this handoff. The implementation checks belong to the corresponding Issues and run only on the actual candidate.

## Coverage and setup

Give the reader the handoff commit and requested starting state. Keep the expected answers with the assessor. Reuse the existing refund example, source facts and applicable host evidence. The SpecDev dependency setup must resolve the package pinned in the [manifest](../tools/openspec/package.json) and [lockfile](../tools/openspec/package-lock.json).

For this handoff, inspect the native change status and the task context returned by `openspec instructions apply --change ship-specdev --json`. Compare the row identities, evidence and checked states with the native task list. This read-only check is separate from exercising the future skill.

## Cases

| Case | Action | Required observation |
| --- | --- | --- |
| W-START · S01.1/S02.1 | Ask what can start before and after the accepted Builder commit is available. | Before acceptance, implementation waits. Afterward, W01 and W03 can start independently. The reader finds W01's literal-derived domain and its real consumer and reuses W60's guide evidence. |
| W-RESUME · S30.1 | W47 and W40 have evidence. W44 is open. Ask whether W48 can start, then supply W44's acceptance. | The reader waits for W44. Once eligible, W48 consumes the selected change and its original criteria. Parked proposals confer no authority. |
| W-CONSUME · A19/A26 | Use W40's refund list through the real W48 consumer. A same-numbered task exists in a sibling change. | Native rows 1.1 and 1.2 can start independently. Row 2.2 waits for working API evidence from 2.1. The consumer uses the selected change and the existing Issue only where ownership calls for it. An incorrect permission, stale reference or wrong change fails the relevant check. |
| W-PACKET · W40.3/W48.3 | Ask the normal entry to prepare work from the same source packet with W01, W02 and W03 as independently owned Issues. Read the generated list before and after supplying hypothetical W01 acceptance. | One native checklist resolves the three supplied Issues, preserves their criteria and identifies both opening tasks. W02 waits for W01. No fourth Issue, parallel feature plan or extra acceptance record is created. The exercise ends at document delivery. |
| W-STYLE · A33b | Use W63’s sourced refund task and its scoped specification edit. | A reader identifies the manager-only approval rule and the open retry decision in the saved passages. The selected format and task state survive. [Inputs, rejection cases and evidence](../openspec/changes/ship-specdev/tasks.md#w63-1) |
| S40-INSTALL · A36 | Follow the two [install Issues](../openspec/changes/ship-specdev/tasks.md#w64-issue) from isolated destinations. | Verify the installed release and selected host. Reject a corrupt archive, preserve user content on refresh/removal and distinguish staged package evidence from public availability. |

## Procedure and cleanup

At W47, issue `/specdev init` through the supported host entry in a fresh disposable project. Inspect the native root, empty change list and absence of extra host entries. A plain standalone request in a fresh directory creates no OpenSpec root. Reuse that initialized project for the feature case.

For the new routing cases use the criteria already attached to W35–W37, W47, W53, W58 and W59. They cover native and standalone requests, a short command collision, the W47.1 native verb with no local alias, an unknown verb with no effects, a custom-schema name collision, and upgrade and recovery. Keep the real dispatch, resulting file or native status, candidate and verdict in the existing private run record. A package installation proves the pin only; a host or product outcome needs its own observation.

## Open prerequisites

Capture W40's authorized output once and reuse it at W48. Use both actual hosts for the release claims assigned to W17. Keep unavailable host behavior Not demonstrated.
