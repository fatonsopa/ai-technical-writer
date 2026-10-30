# Binding policy or technical standard

A standard records agreed rules that people and automation must follow. It needs a clear scope, precise requirements, exceptions, and a way to check compliance. It should be readable without knowledge of the meeting or issue that created it.

## Principles

1. **Define authority and scope.** State whether the text is binding, who or what it applies to, and which existing rule takes precedence if there is a conflict.
2. **Write one obligation clearly.** Name the actor or system when it matters, the required action, the condition, and any meaningful exception. Separate independently testable rules.
3. **Use requirement words consistently.** For a standard that adopts RFC 2119/8174, define how MUST, MUST NOT, SHOULD, and MAY are interpreted. Do not casually mix advisory language with mandatory rules.
4. **Describe what a compliant result looks like.** Give a practical check, example, or validation method for important rules. Avoid repeating the requirement as its own reason.
5. **Explain reasons where they guide decisions.** A short rationale helps people handle cases not explicitly listed. Move incident history and meeting transcripts to their source records.
6. **Resolve conflicts and duplication.** Keep one source of truth for each rule, link to related standards, and state which document owns which responsibility.
7. **Handle exceptions deliberately.** Define who can approve them, how they are recorded, and their limits when applicable. Do not invent exceptions.
8. **Protect changes.** Preserve every unique requirement, exception, definition, and source in rewrites. Do not silently weaken or strengthen a rule.

## Template

```md
# [Topic] standard

## Purpose and scope
[Who or what the standard covers, authority, exclusions.]

## Requirements
### [Subject]
- [Rule, conditions, exception if any.]
- [Another independently checkable rule.]

## Verification
[How compliance is checked; automated and manual checks.]

## Exceptions and ownership
[Approved exceptions, owner and precedence; only if relevant.]

## Related documents
[Maintained sources of truth.]
```

## Completed example: API request logging

This fictional example is a sample policy; adopting it requires project approval.

### API request logging standard

**Purpose and scope.** These rules apply to the application's production HTTP API. They govern application request logs; infrastructure access logs may follow a separate standard.

**Requirements.**

- The API must record a request ID, HTTP method, route pattern, response status, and request duration for each completed request.
- Application logs must not include access tokens, session cookies, or plaintext passwords.
- Errors reported to users must include a request ID that support staff can use to find the corresponding server log.
- The logging system must use a consistent timestamp format with a stated timezone.

**Verification.** Automated tests send a successful request and a failed request, then check their log fields and confirm secrets are absent. A production sampling check verifies that a reported request ID can be found.

**Ownership and exceptions.** The engineering lead approves any documented exception before release. This example assumes no exception has been granted.

## Quality check

A reviewer can distinguish binding rules from explanations, identify scope and exceptions, and determine how each rule will be checked. Rules do not contradict or duplicate another maintained standard without explaining precedence.

## Sources

- RFC 2119 requirement terminology: https://www.rfc-editor.org/rfc/rfc2119
- RFC 8174 capitalization clarification: https://www.rfc-editor.org/rfc/rfc8174
- Google technical writing guidance: https://developers.google.com/style
