# Reporter evidence

Staging build q-9, workspace administrator, workspace 7. Contract RENAME-1 requires a successful rename to be visible in a fresh read. The reporter submitted New Team in place of Old Team. Five update responses were HTTP 200 with durations 120 ms, 118 ms, 123 ms, 121 ms, and 119 ms. No comparison baseline or performance target is supplied.

For the first attempt only, the reporter supplied two sanitized SQL result snapshots for SELECT id, name FROM workspaces WHERE id = 7:

| Snapshot | id | name |
| --- | --- | --- |
| Before update | 7 | Old Team |
| After update and fresh read | 7 | Old Team |

The HTTP response for that attempt contained New Team. No other SQL snapshots, screenshots, logs, repository inspection, production scope, root cause, fix, or passing tests are available. The writer has not run the queries or requests.
