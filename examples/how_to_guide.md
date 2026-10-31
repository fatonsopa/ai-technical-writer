# Resolve website categories in Review

## Before you begin

Use this procedure when automation has stopped and you need to make a manual category decision. You need a signed-in administrator account and access to Websites administration.

## Find the websites

1. Open Websites and select **Review**.
2. Read the reason beside the website before choosing a category.
3. Narrow the list with domain search or category. For an ending such as `co.uk`, open **More filters**, enter the ending, and apply it.
4. Confirm the visible rows and selection match the work you intend to change.

Review can include uncited websites that do not appear in All. Pending contains websites still awaiting automation; it is not another name for Review.

## Assign one category

1. Open the row's category editor.
2. Choose an active category.
3. Select Save or press Enter. Wait for the saving state to finish.
4. Confirm the website leaves Review and the count refreshes. A fresh view should show the saved category.

To discard an unsaved choice, select Cancel or press Escape before saving. If saving fails, keep the selected value visible and read the error before retrying. Do not interpret the selected value alone as a saved change.

## Change or clear several categories

1. Select the intended websites and open the bulk category dialog.
2. Choose a category to assign, or choose Clear to remove the category.
3. Confirm the action and wait for its result.
4. Review the reported changed-row count and refreshed queues.

An assignment marks a website manually verified. Clearing returns it to Pending. Deleted websites are skipped, so the changed-row count can be lower than the number of submitted IDs.

## Confirm success

After an assignment, a fresh read shows the saved category and the website leaves Review. After clearing, it appears in Pending without verification metadata. Check the refreshed count and the reported changed rows; submitted IDs alone do not establish success.

## Recover from an interrupted bulk change

Stop when the dialog reports partial or unresolved work. Earlier batches may already have committed. Check confirmed progress, unresolved IDs, and unattempted IDs before taking another action.

If a response was lost, use the reconciliation view to read current values and relevant history. Retry only after reviewing that state; another administrator may have changed a category in the meantime. Do not repeat the original entire selection simply because its last request failed.

If rows or counts remain inconsistent after refresh, preserve the operation details and report the problem. Do not clear categories as a way to repair a display issue.

## Related information

The [explanation](explanation.md) describes queue membership. The [policy](policy.md) covers accountability, and the [specification](spec_driven_development.md) defines expected outcomes.
