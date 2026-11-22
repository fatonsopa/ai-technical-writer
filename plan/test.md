# Spec Writer handoff test specification

Test basis: [Behavioral specification](./specification.md) and the [approved task records](./tasks.md) in this handoff revision.

Test item: The [execution guide](./README.md), [task list](./tasks.md) and linked Issue records at the same Git revision. Record the candidate used for each observation.

## Coverage and setup

The first two cases test whether a reader can select a task, find its criteria and stop at a real dependency. Use a read-only checkout. Supply hypothetical completion states in the question. Leave the actual task boxes and Issue verdicts untouched. The final two cases exercise different boundaries during implementation. The refund case keeps its existing acceptance run. The three-Issue case checks whether the shipped writer can reproduce and consume the work order in this handoff.

## Cases

| ID / requirement | Preconditions and action | Expected outcome |
| --- | --- | --- |
| W-START · S01.1/S02.1 | Compare the handoff before and after an accepted Builder commit is available. Ask what can start, what proof the first Issue requires and what prior work can be reused. | Until Builder is accepted, hold Writer implementation. Then W01 and W03 can start in parallel. W01.1 requires the literal-derived domain and its consuming cases. Reuse W60’s accepted guide evidence. |
| W-RESUME · S23.1/S30.1 | Assume W40 and W47 have accepted evidence, but W44 is still open. Ask whether W48 can start. Then supply accepted W44 evidence and ask what W48 reads. | Hold W48 until W44 is met. With the three prerequisites met, follow the list to W48 and recover its approved criteria from the Issue. W55–W57 and W51.3 remain outside execution scope. |
| W-CONSUME · A19/A26 | When W40 and W48 ship, use the existing refund assignment through the real writing and implementation entries. Compare the observed selection with the same rule used in this handoff. | Keep W40’s authored list and linked Issues. W48’s actual consumer identifies both parallel rows, holds the dashboard filter for the API result and reads its own Issue when it becomes eligible. Retain that evidence once. |
| W-PACKET · W40.3/W48.3 | As W40 ships, use the ordinary writing entry on a scratch copy of this revision. Supply the specification, delivery plan and just the Issue bodies for W01, W02 and W03. Withhold the checklist, local row numbers, parallel markers and expected answers. Ask for the execution list for those three Issues. When W48 is available, ask its real consumer what it could start, then supply hypothetical accepted W01 evidence and ask again. | Resolve S01.1 and S02.1 in the specification, the approach in the plan and each task criterion in its Issue. The generated list resolves the two opening Issues and their own criteria. A copied acceptance definition or unresolved source fails the affected handoff. A full second case under the same criterion ID counts as a copy even if it includes a link to the original. W02 waits for W01. The consumer reads that actual list, then selects W02 with its own criteria after the prerequisite is met. It neither invents a fourth Issue nor starts an implementation in the read-only exercise. Retain the generated rows and both observed selections. |

## Procedure and cleanup

1. Give the reader the execution guide and the starting state for each of the first two cases. Keep the expected answers with the assessor. Ask for the selected and blocked work, the owning Issue or criterion, and the source of its authority.
2. Compare the returned choices and links with the expected outcomes. Record the candidate, exact sources and observed result in the private JSON execution log. A wrong selection fails the affected case. Reuse the other case while its inputs still match.
3. For the implementation cases, use the named Issue’s checks on its actual candidate. Compare the resolved Issues, behaviors and dependencies. Different wording or local task numbers can be valid. Keep its evidence with that Issue. The reading exercise creates no tracked state to clean up.

## Open prerequisites

W40 must be available for generation. Keep its output for the W48 consumer when that entry is available. A successful reading exercise establishes document usability only.
