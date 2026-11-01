# Review omits parked websites without citation aggregates

Type: Bug
Status: Open at the pre-change baseline

## Description

The administration website list omits an active parked website when it has no citation aggregate. The same parked state is visible when a website has a citation aggregate. This prevents administrators from finding all websites that need manual review.

## Environment

Isolated baseline database and administration build before the new queue contracts. Signed-in administrator; functional fixture revision WR-1. The issue concerns the current listing behavior, not production-wide impact.

## Prerequisites

Seed U3 and U3H from the [Test Specification (TS)](test_specification.md). Both are active, unverified, and parked. U3 has a citation aggregate; U3H does not. Confirm both records exist through an authorized database read.

## How to reproduce

1. Open website administration as the seeded administrator.
2. Set Review Status to Under Review and enter `__test_wrs` in domain search, then apply the filters.
3. Look for U3 and U3H in the returned list.
4. Compare the result with an authorized read of their verification and deletion state.

## Expected result

The dedicated Review population defined by WEB-02 includes both active parked websites, even when a website has no citation aggregate. All keeps its existing citation-based behavior.

## Actual result

U3 is returned and U3H is absent. A direct read confirms that U3H is active and parked. The current listing cannot represent the complete Review population.

## Reproduction frequency

Reproduced in three fresh baseline runs with the same fixture.

## Severity and impact

Affected administrators cannot discover the omitted websites through this listing. The number of affected real websites is not established by this fixture. Priority and formal severity are awaiting triage. An authorized direct database read can expose the omitted records; no equivalent list-interface workaround is known.

## Evidence

Baseline capture WR-B01 records the returned IDs and the comparison read. The fixture differs in citation presence while holding active parked state constant.

## Relevant files

- `_admin_websites_predicate` and `list_admin_websites_page` database definitions
- `src/pages/admin/websites/AdminWebsitesPage.tsx`

These locations come from the supplied baseline investigation. The existing inner join to citation aggregates is a candidate cause to inspect. This report does not establish the final code change.

## Verification

T03 must return U3, U3H, and User Story (US) for active Review, four expected Pending rows, and the six existing All rows. T06 must show matching list/count/ID populations. Repeat after the read-contract change.
