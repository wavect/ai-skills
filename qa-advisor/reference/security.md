# Defensive review of trust boundaries

Start with an operation and its intended actor in the supplied source. Trace authentication, server-side authorization, record ownership, validation, secret handling and logging across the call chain. Cite the guard or the specific unguarded path. Check whether middleware or storage policy supplies a control before calling it absent.

For dependencies, match the resolved version and reachable use to a published vendor advisory. Record uncertainty where only a manifest range is available. For a suspected exposed credential, redact the value and point to its location. Recommend revocation and replacement through the owner's process.

Prefer a protective change and an ordinary regression assertion, such as a repository test that a caller can read only records belonging to its account. Keep review examples within the supplied code and existing test interfaces.
