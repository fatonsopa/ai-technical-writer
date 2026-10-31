# Source facts

Proposed mail flow: API records accepted work, worker takes it from Queue, contacts external Mail provider and records outcome. A slow provider must not keep the user request open. Queue operation, duplicates and delivery monitoring add work. Retry limits undecided. Accepting work, provider delivery and recipient reading are distinct.

## Existing draft for editing/review/rewriting

# Draft

The following information is provided for the purpose of facilitating understanding of the subject.

Proposed mail flow: API records accepted work, worker takes it from Queue, contacts external Mail provider and records outcome. A slow provider must not keep the user request open. Queue operation, duplicates and delivery monitoring add work. Retry limits undecided. Accepting work, provider delivery and recipient reading are distinct.
