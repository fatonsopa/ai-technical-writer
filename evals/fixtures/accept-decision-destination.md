# Existing excerpt

# Draft

Draft a comment in the existing Feature task. Currently a source mapping can be committed before its import-history record. MAP-01 requires both records to commit together or neither. Option A uses one database transaction. Option B writes history afterward. Recommend A because it meets MAP-01; both writes must fit the same transaction. The design is proposed. No accepted decision or executed test exists.
