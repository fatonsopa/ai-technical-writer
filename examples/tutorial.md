# Website category editing tutorial

Learn why All is not the sum of Pending and Review. You will inspect returned queue state and compare active populations without connecting to the application or a database.

## Before you begin

Use Python 3 and a terminal in an empty folder. The exercise uses a local JSON file. Its `review_state` values stand in for values already returned by the server; you will not reimplement the parked-state rule.

## Steps

1. Create `websites.json` containing:

    ```json
    [
      {"id":"V","active":true,"cited":true,"review_state":null},
      {"id":"P","active":true,"cited":true,"review_state":"pending"},
      {"id":"PC","active":true,"cited":false,"review_state":"pending"},
      {"id":"U0","active":true,"cited":true,"review_state":"pending"},
      {"id":"U2H","active":true,"cited":true,"review_state":"pending"},
      {"id":"U3","active":true,"cited":true,"review_state":"review"},
      {"id":"U3H","active":true,"cited":false,"review_state":"review"},
      {"id":"US","active":true,"cited":true,"review_state":"review"},
      {"id":"UD","active":false,"cited":true,"review_state":"review"}
    ]
    ```

2. Print active Review IDs:

    ```sh
    python3 -c 'import json; rows=json.load(open("websites.json")); print(", ".join(r["id"] for r in rows if r["active"] and r["review_state"]=="review"))'
    ```

    Expected output:

    ```text
    U3, U3H, US
    ```

    U3H is present even though it is uncited. UD has Review classification but is excluded because it is inactive.

3. Compare all three totals:

    ```sh
    python3 -c 'import json; rows=[r for r in json.load(open("websites.json")) if r["active"]]; print("All:", sum(r["cited"] for r in rows)); print("Pending:", sum(r["review_state"]=="pending" for r in rows)); print("Review:", sum(r["review_state"]=="review" for r in rows))'
    ```

    Expected output:

    ```text
    All: 6
    Pending: 4
    Review: 3
    ```

## Check your result

Both commands and their displayed outputs were checked from an empty temporary folder with Python 3. This validates the local exercise only.

Confirm the three Review IDs and totals above. If the file is missing, check the terminal's folder. If a total differs, compare each row's active, cited, and returned state values.

All contains cited active websites, including verified V. Pending and Review contain outstanding work and can include uncited websites. The totals answer different questions.

## What you learned

You separated queue classification from active visibility and citation membership. Next, read [Explanation (EXP)](explanation.md), then follow the [How-to Guide (HTG)](how_to_guide.md) in an authorized environment.
