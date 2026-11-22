# Discovery Interview Record (DIR)

A discovery interview record keeps what a product owner or stakeholder actually said when their answers change a document's intent or scope. Write one when someone asks for the record, or when the next author needs the answers and wasn't in the conversation. Discovery itself follows [the discovery workflow](../workflows/discover.md); this record is its durable output.

## Principles

- Investigate first. If the sources already settle the question, proceed without an interview and say which source settled it.
- Ask the question that changes the requirement. Explain the evidence, then ask which option applies; for example, "make reviews faster" can mean several different delays. Keep small independent questions together in one turn.
- Record each answer with its source: who said it, where and when. Quote the owner's exact words when they change scope, and keep suggestions apart from answers.
- Restate the outcome in plain words and record whether the owner confirmed that restatement. Only the owner's own reply confirms it. Silence, a timeout or "continue" leaves it open.
- Keep missing values open. If the owner gives no target, such as a latency or a budget, the record says it's unknown, and documents built from it don't invent one.

## Structure

Start with the context and the question that needed an answer. List each question with its answer and source, then the restatement with its confirmation state, the open decisions and the sources. Deliver the record through the checked-delivery workflow when it's requested as a document; otherwise keep the answers in the session and cite them where they're used.

## Template

```md
# [Topic] discovery interview

## Context
[Request, reader, evidence inspected and why it didn't settle the question.]

## Questions and answers
| Question | Answer | Source |
| --- | --- | --- |
| [Question that changes the requirement] | [Owner's answer; exact words where scope changes] | [Who, where, when] |

## Restatement
[Plain restatement of the intended outcome.] Confirmation: [confirmed by the owner, with source / awaiting the owner's reply].

## Open decisions
- [Unanswered question or missing value, and who decides it.]

## Sources
- [Conversation, document or evidence used.]
```

## Completed example

Read the [Discovery Interview Record (DIR) example for faster Websites Review](../examples/discovery_interview.md). It shows an ambiguous request settled by one question, a confirmed restatement and a latency target left open.

## Quality check

Can the next author tell the question, its source, the owner's answer, the restatement and whether the owner confirmed it, without the original conversation? Check that no suggestion is recorded as an answer and no missing value has been filled in.

## Sources

- [Interviewing users, Nielsen Norman Group](https://www.nngroup.com/articles/interviewing-users/)
