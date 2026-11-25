# Choosing the assertion and the test boundary

Identify a plausible behavior change the test should catch. If changing a returned amount, destination or ownership would leave the assertion green, strengthen the observable assertion. A spy can answer whether an email was queued. A recording adapter or contract test can additionally verify recipient, content and idempotency key.

Use a fake clock for expiration rules, a real disposable database for constraints and transaction behavior, and a contract fixture for an external provider's response shape. Select only the boundary that owns the invariant. For generated inputs, define a property such as conservation of a total and report a minimal counterexample if it fails.

Keep fixtures explicit where a field changes behavior. A builder may supply irrelevant defaults. Snapshot stable public representations when the expected changes can be meaningfully reviewed.

## Example finding

A billing test checks the response status after cancelling a subscription but never reads the renewal schedule. Consequently, a successful HTTP response with a still-active renewal could pass this test. Cite the handler and assertion. Inspect the scheduler and its tests before assigning release severity. A regression assertion can advance a fake clock to the next renewal and verify that no invoice is created, while another active subscription still renews normally.

For a contract test, identify which consumer depends on which provider behavior. Cover field meaning, optional values and error responses using a shared fixture or provider verification. A fixture built entirely by the consumer can drift from the actual provider.
