# Websites administration architecture

Status: Target architecture for Websites Review, with the existing foundation identified below
Behavior source: [Spec Driven Development document (SDD)](spec_driven_development.md), WEB-01–WEB-12

## Scope, terms, and drivers

This view covers the administrator's website lists and manual category changes. It excludes the internals of categorization providers and confirmation jobs. Those systems supply verification state; this feature reads that state without restarting their work.

Pending and Review describe outstanding work. All remains the existing cited administration population. Active means not deleted. The important drivers are complete queue visibility, one classification rule, attributable manual changes, compatibility with current callers, and honest partial-failure feedback.

## Existing foundation

The React administration interface calls PostgreSQL functions through the existing Supabase integration. Website records hold category and verification state. Citation aggregates provide citation information and determine membership in the current All list. Administrator authorization uses the signed-in user and the existing administrator-role check.

The Websites page and bulk category dialog already exist. The old All query relies on citation aggregates, so it cannot serve as the complete unsettled-work population. The current interface also lacks a dedicated Review surface with consistent inline category assignment.

## Target components and responsibilities

| Component | Responsibility |
| --- | --- |
| Websites page and sub-tabs | Tab/filter state, keyset navigation, counts, and selected IDs |
| Shared category cell and edit hook | One active edit, explicit save/cancel, saving and failure state |
| Bulk category dialog | Category or clear selection, sequential batching, progress and reconciliation |
| Administration read functions | Authorized list, count, and matching-ID results using a shared predicate |
| Central review-state helper | Map verification state to Pending, Review, or neither |
| Category mutation | Authorize and atomically update one request, verification metadata, and journaled changes |
| Website store and change journal | Current category/verification state and attributable change history |

### Website administration read and write relationships

![Website administration components and their read and write relationships](diagrams/website_relationships.svg)

This view shows responsibilities and data relationships, not the order of a request. The numeric references identify components so the table can explain the same elements.

| Component | Explanation |
| --- | --- |
| 1. Administrator | A signed-in administrator browses review tabs and requests category changes. Database authorization still checks each mutation; a visible control alone is not permission. |
| 2. Websites page | The page coordinates tabs, filters, counts and category editing. It requests data from the read functions and sends category changes to the mutation function. |
| 3. Administration reads | The list, count and matching-ID functions answer different page needs using the same filters. Matching IDs identify all websites selected by those filters, including rows outside the current page. |
| 4. Shared visibility and review rules | The shared classifier decides which review tab each website belongs to. The read functions reuse these rules so that the list, count and bulk-selection IDs agree. |
| 5. Websites | Website records hold category and verification state. Reads classify those records, while a permitted mutation updates the selected records. |
| 6. Citation aggregates | Read functions consult citation information when the selected tab or filter needs it. This store supplies evidence for classification rather than accepting category writes. |
| 7. Category mutation | The database API checks administrator access and input, then changes categories and writes history in one transaction. Each request handles at most 500 IDs. |
| 8. Change journal | The journal records who changed a category and what changed. If journaling fails, the request’s website changes roll back as well. |

**Mermaid source**

```text
%% Diagram: Architecture diagram
%% Subtitle: The page uses shared filters to load and select websites. Each category update also records who changed what.
flowchart LR
    accTitle: How the Websites page reads and saves data
    accDescr: The administrator uses the Websites page. Shared read rules keep rows, counts and matching IDs consistent. An authorized mutation commits category changes with their history.
    A("1. Administrator") -->|Browse and edit| UI["2. Websites page"]
    UI -->|Request filtered rows, counts or IDs| R["3. Administration reads"]
    R -->|Apply shared rules| C["4. Shared visibility and review rules"]
    C -->|Evaluate website state| W[("5. Websites")]
    R -->|Read when required| G[("6. Citation aggregates")]
    UI -->|Assign or clear a category| M["7. Category mutation"]
    M -->|Update category and verification| W
    M -->|Record committed changes| J[("8. Change journal")]

class A actor
class UI,R,C,M process
class W,G,J datastore
%% Legend: flow_arrow | Relationship
```

The classifier decides queue state; the shared predicate adds active-row visibility and requested filters. Citation joins remain optional for Pending and Review. All keeps its current aggregate requirement. This distinction prevents uncited websites from disappearing while preserving existing All behavior.

## Runtime and data flow

### Load a review tab

Opening a tab requests its first page and the corresponding counts. The server applies administrator authorization and shared filters. Matching-ID selection uses the same population as the visible page and count. Tab or filter changes discard the previous keyset cursor.

### Save a category change

For an inline assignment, the browser submits one ID to the same mutation used by the bulk dialog. The database validates the caller and category, updates category and verification state in one transaction, and writes change history through the existing journal mechanism. Only a committed response permits the interface to confirm success.

![How the system saves a category change](diagrams/category_save_sequence.svg)

Read this sequence from top to bottom. It separates rejection, transaction failure, confirmed success and a lost response, because those outcomes support different claims about saved data.

| Component | Explanation |
| --- | --- |
| 1. Administrator | The administrator chooses a category and starts the save. No additional confirmation modal is implied by this diagram. |
| 2. Websites page | The page submits the selected IDs and category, shows progress, and interprets the returned result. |
| 3. Database API | The API owns authorization, input checks and the transaction that writes both website state and history. |
| 4. Save selected category | Click Save or press Enter after choosing a category. This starts the request; it is no longer the pre-submission cancellation path. |
| 5. Submit IDs and category | Send the selected website IDs and chosen category. A bulk operation splits the IDs into requests of at most 500. |
| 6. Check access and input | Verify that the current user is an administrator and that IDs and category values are valid before writing. |
| [7. Request denied or invalid] | Follow this branch if access or input checks fail. The API rejects the request before any website or history writes. |
| 8. Reject without writes | Return the rejection to the page. The database has not changed any selected website for this request. |
| 9. Show error and retain selection | Explain why saving failed and keep the selected value available for the administrator’s next action. |
| [10. Request accepted] | Follow this branch only after access and input checks pass. Acceptance here permits the transaction to begin; it is not yet a committed save. |
| 11. Update websites and history together | Apply the category changes and their history entries within the same transaction. |
| [12. Update or history write fails] | A failure in either write prevents a partial commit for this request. |
| 13. Roll back this request | Roll back the website and history writes for the failed request and return an error. Earlier successful bulk batches are separate requests and remain committed. |
| 14. Show error and retain selection | Tell the administrator that this request failed and keep the selection. Do not silently resubmit it. |
| [15. Transaction commits] | Both website changes and history have committed. Whether the page can confirm this depends on the response path below. |
| [16. Page receives committed response] | The page receives usable confirmation of the committed result and can refresh the affected data. |
| 17. Return changed-row count | Return the number of rows changed by the request. A count is confirmation of this request’s result, not evidence about unattempted bulk batches. |
| 18. Refresh affected rows and counts | Reload the affected rows and counts so that tab membership and totals reflect the saved category. |
| 19. Return current results | Return the updated list and count information using the shared filtering and classification rules. |
| 20. Confirm the result | Show the completed save to the administrator after confirmation and refresh. |
| [21. Response is lost] | The database committed, but the page did not receive usable confirmation. This branch illustrates an uncertain client outcome. |
| 22. No usable response | The crossed response arrow represents a lost response in this example. It does not mean that the database rolled back. |
| 23. Outcome uncertain, reconcile before bulk retry | Explain the uncertainty and read current values and relevant history before offering a bulk retry. Do not retry automatically. |

**Mermaid source**

```text
%% Diagram: Sequence diagram
%% Subtitle: The database saves the category and history together. A lost response leaves the page uncertain about the result.
sequenceDiagram
    accTitle: Save a website category
    accDescr: The API checks administrator access and input before writing. Valid changes and history commit together. The page refreshes only after confirmation and reports uncertainty when the committed response is lost.
    actor A as 1. Administrator
    participant UI as 2. Websites page
    participant DB as 3. Database API
    A->>UI: 4. Save selected category
    UI->>DB: 5. Submit IDs and category
    DB->>DB: 6. Check access and input
    alt 7. Request denied or invalid
        DB-->>UI: 8. Reject without writes
        UI-->>A: 9. Show error and retain selection
    else 10. Request accepted
        DB->>DB: 11. Update websites and history together
        alt 12. Update or history write fails
            DB-->>UI: 13. Roll back this request
            UI-->>A: 14. Show error and retain selection
        else 15. Transaction commits
            alt 16. Page receives committed response
                DB-->>UI: 17. Return changed-row count
                UI->>DB: 18. Refresh affected rows and counts
                DB-->>UI: 19. Return current results
                UI-->>A: 20. Confirm the result
            else 21. Response is lost
                DB--xUI: 22. No usable response
                Note over UI: 23. Outcome uncertain, reconcile before bulk retry
            end
        end
    end
%% Legend: lost | Lost response
```

Numbers identify message order within this scenario. The alternative blocks distinguish rejection, transaction failure, confirmed commit and response loss; the crossed response arrow represents a lost message.

### Stop and reconcile a partial bulk change

Bulk selection is a client-coordinated sequence of transactions, each with at most 500 IDs. There is no transaction covering the entire selection. A later failure cannot undo earlier committed batches. The client stops, retains progress, and reconciles an uncertain result before a user chooses a retry.

After confirmed writes, the page invalidates affected rows and counts. A website may leave the current queue; retaining it until the next manual reload would contradict the successful result.

## Trust and data ownership

PostgreSQL owns classification and current category state. The browser may display returned state but does not maintain its own parked rule. The authenticated administrator is the actor; client-supplied text cannot substitute for the authenticated identity.

Read authorization and write authorization apply at the database boundary. Hiding a button is useful interface behavior, but it does not authorize a request. The change journal records committed modifications. No new event service, queue, or independent category store is introduced.

## Deployment and operations

Deploy additive database support before the new browser callers. Keep old read signatures compatible for one release, then remove the superseded Review filter paths separately. Concurrent index builds have their own migration boundaries.

Measure database first-page queries and maximum-size mutation requests against WEB-12. Observe failed mutations, missing actor attribution, and list/count mismatches during rollout. If the interface must be withdrawn, preserve the additive database support and committed category history. Correct erroneous decisions with attributable compensating changes rather than deleting history.

## Decisions and risks

The [Decision Record (DR): architecture](decision_record_architecture.md) records why classification remains in the database. The [Decision Record (DR): component design](decision_record_component_design.md) records why bulk work stops after a failed batch and requires reconciliation.

The main integration risks are a missing parked-state prerequisite, changed grants on replaced functions, optional aggregate joins becoming mandatory, and client feedback that mistakes a lost response for a rollback. The [Low Level Design (LLD)](low_level_design.md) defines the contracts and failure branches; the [Implementation Plan (IP)](implementation_plan.md) owns sequencing.

After implementation, update this document with the verified deployed structure and remove obsolete transition details. Do not label the target view as current merely because the plan was completed.
