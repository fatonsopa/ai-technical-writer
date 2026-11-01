# Writing Style (WS)

Write as an experienced developer explaining the subject to a colleague. Use natural English, precise technical terms, and enough context to make sense without the original conversation.

Apply this guide to every authored text surface before it is sent or accepted. That includes documents, instructions, titles, headings, tables, templates, examples, references, diagram titles, labels, metadata, legends and explanations, questions and answer options, audit findings, recommendations, comments and delivery messages. No output type, length or workflow stage is exempt. The guide’s preservation rules govern exact literals, code, commands, identifiers, values and quotations; applying style must retain their required meaning and bytes. The document reference defines the structure and required information. For issue titles and descriptions, also use [Issue](issue.md).

## 1. Understand the subject before choosing words

Identify the subject, what happens or is required, and which conditions matter. Explain those facts directly. Replacing words will not repair an explanation whose meaning is still unknown.

Start with what the reader needs to understand. Explain the purpose and behavior before introducing implementation details, unless the reader is looking up an exact interface or identifier.

Each sentence should add useful information or connect ideas. Ask what it tells the reader. If the answer is unclear, return to the source. Identify missing information instead of inventing an explanation.

## 2. Give readers the context they need

Assume readers understand the general field but have not seen this project's conversations, plans, or internal shorthand. Introduce unfamiliar components and explain their role before describing how they interact.

Give enough context where readers need it. A link can provide detail, but the surrounding text should explain why it matters. References such as “the earlier decision” or “step B” cannot be the only explanation of what applies.

Match the detail to the audience. Developers usually know what an API is, but may need an explanation of this application's roles. Explain unfamiliar concepts without turning every document into a beginner's lesson.

## 3. Use familiar words and accurate technical names

Prefer ordinary verbs such as “use,” “save,” “send,” “check,” and “retry” when they express the meaning accurately. Write “review the changes” instead of “carry out a review of the changes.”

Keep established terms that add precision. “Transaction,” “rollback,” “worker,” and “flaky test” can be clearer than improvised substitutes. Define an unfamiliar term once and use it consistently. Retain exact names readers need to find code, commands, settings, or UI controls.

Avoid invented labels, long strings of nouns, slogans, and metaphors that readers must decode. Describe what a process does instead of giving it human motives or calling an intermittent test result “lucky.” Use role names for reusable responsibilities; use a person's name when ownership, attribution, or a historical record requires it.

When referring to a document type, use its full name followed by its acronym in parentheses: “Spec Driven Development document (SDD)” or “High Level Document (HLD).” Use that form each time in prose, headings, tables, link labels and diagrams. Keep the approved names and acronyms consistent with the document catalog or project glossary. Describe the document's purpose separately from its name. If it has no agreed acronym, use its name alone. Preserve literal filenames, code identifiers, accepted input aliases, quotations and external publication titles.

Judge words in context rather than replacing everything a scanner flags.

## 4. Use a friendly, helpful tone

Sound like a knowledgeable colleague who understands what the reader wants to do. Address readers as “you” where useful, and use natural contractions. Allow some personality while keeping the explanation focused on their task.

Write conversationally, then edit out the repetition and digressions common in speech. Vary sentence openings and use transitions that connect ideas. Read awkward passages aloud and revise them.

Be considerate of readers with different backgrounds and levels of English. Avoid cultural references, idioms, internet slang, and jokes that require shared knowledge. Explain steps without calling them easy, obvious, simple, or quick.

Give instructions directly. Routine steps do not need “please,” “please note,” or a “let's” introduction. Avoid hype, scolding, forced humor, and excessive exclamation marks.

Adapt the tone to the document. A tutorial can be encouraging; a reference should make facts easy to find. Standards should state obligations clearly. Friendliness must preserve the meaning and strength of every rule.

## 5. Write connected sentences and paragraphs

Use active voice when readers need to know who acts. Passive voice is useful when the result matters more than the actor: “The file was deleted” can be sufficient when the actor is unknown. Avoid hiding responsibility when it matters.

Keep subjects and verbs close. Resolve ambiguous references such as “it” or “this” when several things could be meant. Place a condition before an instruction when readers need it to decide whether to act, and keep exceptions near the rule they qualify.

Combine related actions when they form a natural explanation. Split sentences that become difficult to follow. Keep related sentences together and start a new paragraph when the subject changes. Use transitions to connect ideas.

Do not impose fixed sentence or paragraph lengths, or an actor at the start of every sentence. Check whether the passage is clear on one reading.

## 6. Make titles and headings specific

A title identifies the document's subject or purpose; a heading describes its section. Use enough words to make that meaning clear.

Use sentence case unless the project requires another convention. Choose a natural noun phrase, question, or instruction that fits the content. Headings do not all need to be complete sentences, numbered claims, or commands.

Preserve the subject and important scope. Do not introduce an unverified cause or result in a title. Conventions for different issue titles belong in [Issue](issue.md).

## 7. Remove text that adds no information

Delete filler, repeated explanations, unnecessary introductions, and summaries that repeat the preceding text. Give reasons that explain decisions or consequences; avoid justifying a rule by saying it is necessary.

State what applies directly. Use a comparison or contrast when readers need it to distinguish meaningful alternatives. Avoid slogans and rhetorical framing that make the reader wait for the point.

Shorten by removing repetition and irrelevant detail. Keep every condition, exception, warning, and distinction that changes the meaning. Brevity must not make the reader guess.

## 8. Preserve meaning and be honest about certainty

Distinguish observed behavior, requirements, proposals, assumptions, and possible explanations. Use tense and wording that preserve their status: a proposed change has not already happened, and an observed symptom does not establish its cause.

Keep obligations and permissions intact. Changing “may” to “must,” dropping “only,” or omitting an exception can change a requirement. The [Spec Driven Development document (SDD) guide](spec_driven_development.md) owns requirement wording. A specification states intended behavior; a plan states implementation; a test report states observed results. Keep those roles and their certainty intact.

Preserve material values, units, dates, commands, identifiers, and exact error messages. Distinguish what a source reports from what you independently checked. Never invent evidence, measurements, file paths, test results, or approval.

Specific wording still needs support. Do not replace “improve performance” with a numerical target unless the source supplies it. Do not turn a vague instruction into a specific fix without evidence. Say what remains unknown and how it affects the explanation.

Quote original wording accurately when it matters and identify its source. Otherwise, explain the relevant decision in the document's own prose. Label illustrative examples once, state the assumptions they need, and make them consistent with the rule they demonstrate.

## 9. Choose a format that helps readers

Use paragraphs to explain connected ideas, numbered lists for ordered actions, bullets for separate items, and tables for information readers need to compare. Use code blocks for commands, code, and literal output. Distinguish placeholders from values to enter exactly.

Use bold sparingly and code formatting for literal names and values. Bullets do not need bold opening labels. Follow the project's Markdown formatting conventions; this guide does not impose a line width or a universal page layout.

Use examples that help explain the point. Include enough detail to demonstrate it; a useful example may be longer than the rule.

## Explain diagrams in the reader’s language

Review diagram titles, subtitles, labels, legends and explanations. Use established notation terms. Repeat each complete visible number and label exactly in its table row, with relevant trigger, action, feedback and next path. “The system checks whether the signed-in user is an administrator. Yes permits the edit; No denies access.” Do not imply a confirmation modal. A lost response does not prove rollback. [Visual Guidance (VG)](visuals.md) owns the numbering and notation rules.

## Examples

These wording examples preserve the original information and make no claims about the current project.

| Original | Revised |
| --- | --- |
| The application is responsible for saving updated workspace names in the database. | The application saves updated workspace names in the database. |
| Please note that downloading the report requires you to click Download. | To download the report, click Download. |
| Awesome! Just click Save to save your changes. It's that easy! | Click Save to save your changes. |
| The dashboard provides visibility into whether each import succeeded or failed. | The dashboard shows whether each import succeeded or failed. |
| The scheduler performs a task eligibility assessment before task assignment. | The scheduler checks whether a task can be assigned before assigning it. |
| Every request must include a token because a token is required for every request. | Every request must include a token. |
| The API receives an event. It adds a job to the queue. A worker reads the job. The worker sends the email. | The API receives an event and adds a job to the queue. A worker reads the job and sends the email. |
| Workers record task status: an explanation of how workers record task status | How workers record task status |

### Examples from the Linear exports

These suggestions use the full descriptions in the supplied exports. They show how to name the actual subject and behavior, keep useful technical terms, and replace wording that readers have to decode. Apply the same language principles to other documents.

| Existing title | Suggested title |
| --- | --- |
| CG-474: Add one rule for where a website stands for a person | Define website review status in one database function |
| CG-276: Ask the database who is staff in every staff edge function | Check staff roles and sign-in state in staff edge functions |
| CG-3031: Watch tells the session the same unchanged condition every tick | Monitor repeats notifications for an unchanged condition |
| CG-3006: Refused merge throws away every test result it had already proven | Rejected merges discard passing test results |
| CG-3029: Lint fails when the design-system download needs an SSH key this machine lacks | Lint fails to download the design system without a GitHub SSH key |
| CG-3033: Answers wait weeks in the read stage past the declared limit | Some answers wait weeks for extraction despite the stage time limit |

The IDs identify the source issues; they are not part of the suggested titles. These are wording examples, not complete issue rewrites. Keep the supporting facts, conditions, and unresolved questions in the description. Use [Issue](issue.md) for the detailed issue-writing conventions.

## Review before delivery

For substantial writing, review the complete document in three passes. For a small edit, review the affected text and enough surrounding content to check its meaning.

1. Meaning and accuracy: Explain the passage in your own words without relying on its phrasing or the original conversation. Check the subject, behavior, conditions, source support, and uncertainty. Repair gaps rather than guessing.
2. Language and tone: Read the text as if helping a colleague. Check that it sounds approachable and natural. Replace awkward phrasing, unnecessary jargon, condescending language, ambiguous references, and disconnected sentences. Check titles, headings, templates, and examples as well as paragraphs.
3. Repetition and preservation: Remove text that adds nothing, then compare with the source. Confirm that shortening has preserved important facts, requirements, exceptions, and technical details.

For important or repeatedly misunderstood documents, ask an intended reader to explain a passage or use its instructions. Revise text that requires extra explanations from the author.

A wording checker can identify phrases to review. A clean scan or a readable heading outline does not prove that the whole document is understandable.

## Sources

- [Google: voice and tone](https://developers.google.com/style/tone)
- [Google: terminology and word choice](https://developers.google.com/tech-writing/one/words)
- [Google: audience](https://developers.google.com/tech-writing/one/audience)
- [Google: active and passive voice](https://developers.google.com/style/voice)
- [Google: paragraphs](https://developers.google.com/tech-writing/one/paragraphs)
- [Google: headings and titles](https://developers.google.com/style/headings)
- [Digital.gov: testing for understanding](https://digital.gov/guides/plain-language/test)
