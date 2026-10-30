# Technical reference

A reference page answers precise questions while the reader is working. It describes a system, API, setting, command, data model, or error in a predictable order. Readers should be able to find a fact without reading a story first. Use Diátaxis reference principles and make code examples consistent with the actual contract.

## Principles

1. **Choose a bounded subject.** A reference page covers one coherent API, component, command, or configuration group. Split unrelated material.
2. **Use the subject's natural structure.** An API page groups endpoints and fields; a CLI page groups commands, flags, and output; a configuration page lists keys, types, defaults, and effects.
3. **State exact facts.** Give types, valid values, required permissions, defaults, limits, error behavior, and version differences when known.
4. **Make examples correct and minimal.** An example should show valid input and the corresponding output. Mark illustrative or unverified output as such.
5. **Keep descriptions neutral and easy to scan.** Use concise tables and stable headings; move tutorials and explanations to linked pages.
6. **Verify generated material.** Where reference content is generated from code or schemas, link to its source and keep the generated region intact. Do not manually edit generated declarations.
7. **Record uncertainty.** If a default, limit, or response is unknown, label it and inspect the implementation before publication.

## Template

```md
# [API, command, setting or component]

[One sentence identifying what it does and its scope.]

## Syntax or interface
[Exact command, signature, endpoint, or schema.]

## Parameters or fields
| Name | Type | Required | Description | Default |
| --- | --- | --- | --- | --- |
| [Name] | [Type] | [Yes/No] | [Behavior and limits] | [Value/None] |

## Result
[Output, response fields, side effects, status and errors.]

## Example
[Verified minimal input and corresponding result.]

## Related reference
[Permissions, schema, version, related entries.]
```

## Completed example: list workspace members

This is an illustrative API contract, not a claim about an existing endpoint.

### `GET /api/workspaces/{id}/members`

Returns members of one workspace. The caller must have permission to view the workspace.

**Path parameter.** `id` is the workspace identifier and is required.

**Query parameters.**

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `limit` | Integer | No | `20` | Maximum number of results per page, subject to the service limit |
| `cursor` | String | No | None | Opaque cursor from a previous response |

**Success response, HTTP 200.**

```json
{
  "members": [{"id": "u_12", "role": "admin"}],
  "next_cursor": null
}
```

**Errors.** `401` means the request is unauthenticated; `403` means the authenticated caller lacks access; `404` means the requested workspace cannot be found under the chosen access policy. The precise error contract requires implementation verification.

**Example request.** `GET /api/workspaces/ws_42/members?limit=20` with a valid authorization header. The response above uses fictional identifiers.

## Quality check

An experienced developer can locate a field or status quickly, understand its type and conditions, and distinguish verified behavior from example values. Tables and code samples agree with each other.

## Sources

- Diátaxis, reference: https://diataxis.fr/reference/
- Microsoft developer reference guidance: https://learn.microsoft.com/en-us/style-guide/developer-content/
