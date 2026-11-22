# Faster Websites Review discovery interview

## Context

The product owner asked to "make reviews faster" for the Websites Review page. The specification describes two different delays: a website enters Review only after its automated confirmation stops (the specification calls it parked), and an administrator then edits each Review row inline, one at a time, to assign a category. Neither source says which delay the owner means, so one question was needed before writing a brief.

## Questions and answers

| Question | Answer | Source |
| --- | --- | --- |
| Which delay should the change shorten: the automated checking before a website is parked and enters Review, or the time administrators spend assigning categories once it's there? | "The second one. Admins open every site separately; I want them to clear the queue in one sitting." | Product owner, review-planning chat, 2026-11-18 |
| Should the change also cover clearing a category, or only assigning one? | "Both. Clearing is just as slow." | Product owner, same chat |

## Restatement

Administrators can assign or clear the category of several Review rows at once, so they can clear the Review queue in one sitting. Confirmation: confirmed by the product owner ("Yes, that's it."), same chat.

## Open decisions

- No target time for clearing the queue was given. The owner didn't answer when asked for one, so it stays open for the brief.
- Whether bulk actions need a limit on the number of selected rows is undecided; the owner deferred it to the specification author.

## Sources

- Review-planning chat with the product owner, 2026-11-18.
- [Websites Review behavior specification](spec_driven_development.md), WEB-01 to WEB-06.
