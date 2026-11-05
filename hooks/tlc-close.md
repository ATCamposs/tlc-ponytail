TLC + Ponytail (plugin tlc-ponytail): how a tlc-spec-lean or tlc-spec-driven feature closes.

- The Verifier is this plugin's `tlc-verifier` agent and the screens sub-agent is its `tlc-screens-judge`. Each dispatch names the feature, the files, the diff range and the TLC skill directory.
- In the same turn and in parallel, also dispatch this plugin's `ponytail-reviewer` agent with the same HEAD, diff range and feature name, and log it on the `**Dispatched:**` line.
- Its Must fix and Should fix findings join the single fix pass with the Verifier's, and each one gets its closing commit in `ponytail-review.md`. Nice to have goes to the final report.
- An approved plan item counts as requested, so a finding that would cut it is dropped. Ponytail's "one small test" is the floor: the plan's checks win.
