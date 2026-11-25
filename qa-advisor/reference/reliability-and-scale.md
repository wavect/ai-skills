# Retries, persistence and service limits

Draw the state before the operation, after the local write, after a remote acknowledgement and after a lost acknowledgement. At each boundary ask what a retry observes, which operation owns deduplication and how partial work is recovered. In a disposable test, verify persisted state and the caller's result.

Check migration compatibility with existing rows and the order of old and new application versions. Read before proposing a rollback that could discard data. For performance, relate an observed workload to latency percentiles, error rate and saturation. A query in a loop warrants verifying the query count and expected cardinality. Run routine tests locally. Use existing measurements when evaluating production behavior.
