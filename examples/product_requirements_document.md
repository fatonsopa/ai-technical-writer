# Websites Review and category editing

Status: Approved product baseline for the first release
Audience: Product, administration, engineering, and QA
Related work: [Feature](issue.md), [Spec Driven Development document (SDD)](spec_driven_development.md), [Implementation Plan (IP)](implementation_plan.md)

## Problem and users

Administrators need a reliable way to find websites whose automated category confirmation has stopped and resolve them by hand. The current Websites page combines several needs in one list. An administrator can see a category without knowing whether automation is still working on it, has confirmed it, or has stopped trying. A website with no citation aggregate can also be absent from the list, even though it still needs attention.

These gaps create two kinds of wasted work. Administrators inspect websites that automation has not finished processing, and they miss websites that automation will no longer resolve. When they do identify a wrong category, editing it does not provide a consistent way to complete the review and record who made the change.

The primary users are administrators responsible for website classification. They need to inspect a domain, understand why it needs attention, choose a category, and move on with confidence that their decision was saved. Engineering and support also need enough history to explain a category change. Ordinary application users do not gain access to the administration interface through this feature.

## Goals and success criteria

The release should make manual review a distinct, manageable activity while preserving the existing general-purpose Websites view.

| Goal | How we will assess it | Release expectation |
| --- | --- | --- |
| Make stopped work visible | Compare the Review list with the authoritative parked-website classification, including uncited websites | Every active qualifying website is discoverable under matching filters |
| Keep ongoing automation separate | Inspect Pending and Review with the same controlled dataset | A website belongs to one of these queues, never both |
| Make manual decisions reliable | Follow an inline save and a bulk change through refresh and history inspection | Saved categories persist, queue membership updates, and the acting administrator is attributable |
| Reduce unnecessary navigation | Observe an administrator correcting one row from each tab | A category can be assigned without leaving the list |
| Handle large selections honestly | Interrupt a multi-batch change | The interface reports completed progress and remaining work without claiming total success |

Operational adoption will be assessed after rollout through completed reviews, unresolved Review volume, and administrator feedback. Queue volume alone is not a productivity measure: new websites and changes in automated processing affect it. No numerical reduction target or historical completion-rate baseline has been agreed. Product will set those targets after collecting comparable observations.

## Scope and priorities

The first release includes three tabs: **All**, **Pending**, and **Review**. All remains the existing general-purpose listing. Pending contains websites that still await automated categorization or confirmation. Review contains unverified websites that the confirmation process has parked for human attention. The labels describe work remaining, rather than three exhaustive website statuses.

The following capabilities are required for release:

- Show a count for each tab and keep the displayed rows, count, and selected IDs consistent under the same filters.
- Include qualifying uncited websites in Pending and Review. Preserve All's existing citation-based visibility so that this feature does not unexpectedly redefine the general list.
- Show the reason a website is in Review. Administrators should not need to infer the reason from a category label or an unsuccessful automated action.
- Support domain search, category filtering, and a typed domain-ending filter in all three tabs. Put the domain-ending field in More filters so the primary toolbar remains usable.
- Let administrators assign a category inline from any tab and assign or clear categories through the existing bulk dialog.
- Preserve administrator attribution and refresh affected rows and counts after a successful change.

The following are outside this release: changing automated categorization rules, restarting parked websites, backfilling historical categories, adding a Reason filter, replacing All's citation-based population, and building a domain-ending pick-list with counts. School filtering and citation-population actions stay on All. A clear-category action remains in the bulk dialog; the inline control is for assigning a category.

## User journeys

### Review a parked website

An administrator opens Review and sees the reason each listed website needs attention. They inspect the domain, choose the correct category, and save it inline. While the request runs, the control shows progress and prevents another save for that row. After success, the website leaves Review because a person's confirmed category has resolved the outstanding review. A fresh read shows the same saved category.

If the save fails, the interface keeps the selected category and the row in edit mode. The administrator can understand that the change was not confirmed and retry or cancel. The interface must not silently discard the selection or announce success.

### Find a group of related domains

An administrator opens More filters and enters `co.uk`. The current tab shows matching domain endings while preserving the active category and domain search filters. Entering `.CN`, ` cn `, or `cn.` selects the same ending. Wildcard expressions are rejected rather than interpreted as broader searches. The filter is a typed ending, not an inventory of every domain ending in the database.

### Correct many categories

An administrator selects websites and opens the bulk category dialog. Assigning a category confirms those websites as reviewed. Clearing a category removes the existing classification and returns the website to Pending for automated work. Clearing does not mark a website as verified.

For a selection larger than one request allows, the application divides the work into batches. If a later batch fails, earlier completed changes remain saved. The administrator sees how much work completed and which IDs remain unresolved. The application does not retry a write automatically when the result might be uncertain.

## Product rules and constraints

Only signed-in administrators can read the administration lists or change categories. Interface visibility is not the permission boundary; direct requests must enforce the same restriction.

A deleted website must not appear in the active lists or be modified through these controls. A category assignment must use an existing active category. Manual category decisions must identify the administrator in change history. If two administrators save different categories for the same website, the last committed choice becomes current and both changes remain attributable.

Pending and Review default to newest-added order to make the unsettled lists practical to open. All keeps its existing sort behavior. The specification defines the database performance check separately from browser rendering; neither a fast SQL probe nor a small test dataset establishes the complete user experience.

## Dependencies, risks, and decisions

The feature depends on the shared parked-state helper from the confirmation work. Review must use that definition rather than introducing a second interpretation in the browser. The actor-aware category mutation must also be available before the new controls are enabled.

The main risks are missing uncited rows, disagreement between counts and selection, loss of attribution, and misleading feedback after a partial bulk failure. Testing must exercise these cases directly. The [Decision Record (DR): architecture](decision_record_architecture.md) keeps classification in one database helper; the [Decision Record (DR): component design](decision_record_component_design.md) defines bulk failure handling.

The first release uses parked websites only for Review and places the domain-ending field in More filters. Broader review signals and a Reason filter can be considered later without changing this release's acceptance baseline.

## Acceptance and follow-up

The [Spec Driven Development document (SDD)](spec_driven_development.md) owns detailed requirements WEB-01 through WEB-12. QA must demonstrate each requirement against the agreed fixtures and record any residual risk. Product review covers tab language, filter placement, the manual-review journey, and partial-failure feedback. Engineering review covers compatibility, authorization, attribution, and recovery.

After rollout, collect feedback on review clarity and repeat the queue-completeness checks on the released version. Update product goals only through an explicit scope decision; an implementation shortcut does not change the accepted behavior.
