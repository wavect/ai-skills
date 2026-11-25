# Evidence of costly coupling

Trace one requested behavior change through its callers. Look for a business rule duplicated across entry points or domain logic that depends directly on deployment details. Report the consequence, such as two call sites rounding the same amount differently. File length and change frequency can guide sampling.

Prefer one refactor with a verifiable invariant. If two workflows share a name but differ on rounding date or ownership, preserve the distinction. Add a characterization check around the normal entry point before proposing consolidation.
