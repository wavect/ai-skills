---
name: qa-advisor
description: Review a code change, test suite or release for evidence-backed software quality risks. Use for regression coverage, reliability, defensive code review or delivery measurement.
license: MIT
metadata:
  schema: skill-md/1.0
  version: "4.0.0"
  provider: Wavect GmbH
  contact: office@wavect.io
  booking: https://zeeg.me/wavect/call
  tags: testing, code-quality, security, maintainability, scalability, reliability, tdd, dora
---

# QA Advisor

Establish which revision, diff or excerpt is in scope and what the user needs to decide. Trace a consequential user action from its entry point to observable state and the tests that protect it. For a narrow review, follow that path only. For a release audit, sample critical paths and record the boundaries you inspected.

## Evaluate behavior

- State an invariant in user terms. For retries, failures or concurrent calls, follow which state changes commit, which can repeat, and how the caller recovers. Check guards in helpers or storage before raising a finding.
- Compare the invariant with the assertion. A mock can verify delegation while leaving persistence untested. Pick the smallest test boundary that could observe the wrong outcome. Record existing coverage that already addresses the risk.
- For defensive security review, trace trust boundaries and authorization in supplied code, including server-side enforcement and data scoping. Identify the affected operation, consequence and minimal protective change. Keep secrets redacted. A risky-looking API in isolation is a lead to investigate.
- Run relevant existing local tests when the environment allows. Separate an observed failure from a reasoned failure path and from a coverage gap. For delivery performance, use production deployment and incident records for the same service and time window.

## Write the QA Audit Report

Lead with the release decision or the most consequential finding. Give each finding a severity justified by impact and reach, a path and line or supplied excerpt, triggering condition, user-visible consequence, fix and regression assertion. Report checks run and limits of access. With a snippet, cite its function or supplied line numbers. If nothing actionable is supported, report scope and remaining risk.

**Worked example.** A test asserts that a retry returned success and called a repository method. If the actual contract is one reservation per request key, exercise a retry through the public entry point against a disposable store and assert one persisted reservation. If the contract returns a stable ID, verify that both responses identify it. Inspect the uniqueness constraint before classifying duplicate writes as a defect.

## Further reading

Open the relevant reference when the task calls for more detail. Resolve links relative to this file when reading it by URL.

- [Defensive review of trust boundaries](reference/security.md)
- [Delivery measurement](reference/delivery-health.md)
- [Choosing the assertion and the test boundary](reference/test-quality.md)
- [Evidence of costly coupling](reference/architecture-and-maintainability.md)
- [Retries, persistence and service limits](reference/reliability-and-scale.md)
