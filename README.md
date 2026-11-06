# tlc-ponytail

A Claude Code plugin that runs the [Tech Leads Club](https://github.com/tech-leads-club/agent-skills)
spec skills, `tlc-spec-lean` and `tlc-spec-driven`, with a `grill-me` interview before every plan
decision, the independent agents they call for at the end of a feature, and a code review from
[Ponytail](https://github.com/DietrichGebert/ponytail).

- **`grill-me`** (skill): loads on its own when a spec starts. Every gap in the plan (gray area,
  assumption, ambiguous term, contradiction with the code) becomes a numbered question with a
  recommendation before anything is decided, and resolved terms go into the repo's glossary.

- **`tlc-verifier`**: the TLC Verifier. A fresh agent that did not build the feature checks the
  obligations, injects mutations and tries examples nobody named.
- **`tlc-screens-judge`**: the TLC screens sub-agent. It compares pictures of the running app with
  the binding captures.
- **`ponytail-reviewer`**: a Ponytail review of the same diff: bugs, risk, real load, missing tests,
  speed and code to cut.

The Verifier answers "did we build what the plan promised, and do the tests bite?". Ponytail answers
"is this code correct, safe and no bigger than it needs to be?". They run in parallel, and their
findings are fixed in one pass.

## Install

Ponytail first, then this plugin. In Claude Code, one command per prompt:

```
/plugin marketplace add DietrichGebert/ponytail
```
```
/plugin install ponytail@ponytail
```
```
/plugin marketplace add ATCamposs/tlc-ponytail
```
```
/plugin install tlc-ponytail@tlc-ponytail
```

Then start a new session. The TLC scripts need Python 3 and git.

## How a spec asks

```mermaid
flowchart TD
  A[tlc-spec-lean or tlc-spec-driven loads] --> H[Hook reminds the session to load grill-me]
  H --> L[Look up facts in the code]
  L --> Q[Round of up to 5 numbered questions, each with a recommendation]
  Q --> R[Answers recorded in plan.md or spec.md in the same turn]
  R --> T[Resolved terms go to GLOSSARY.md]
  T --> E{Frontier empty}
  E -- no --> Q
  E -- yes --> P[Plan presented for approval]
```

The [`grill-me`](skills/grill-me/SKILL.md) skill merges a one-question-per-turn interview with
[`grilling` and `domain-modeling`](https://github.com/mattpocock/skills) from Matt Pocock's skills:

- **No silent assumptions.** TLC lets some defaults pass as assumptions without asking (lean's
  `Confirmed? n`, driven's low-stakes defaults). Here every one is asked; small ones go bundled in a
  single "Assumptions" question, so the round stays short.
- **Rounds, not a quiz.** Up to 5 questions per message, numbered across the session. "yes" accepts
  every recommendation; "Q5 b" changes only Q5.
- **Facts are looked up, decisions are asked.** The session searches the code in the main window by
  default and only spawns a sub-agent for a wide sweep, because sub-agents usually cost more.
- **Glossary and ADRs.** Ambiguous terms are challenged against the repo's glossary and recorded
  once resolved (it asks before creating `GLOSSARY.md`). A decision that is hard to reverse,
  surprising and a real trade-off is offered as an ADR in `docs/adr/`.

Two hooks make this automatic: a SessionStart hook adds [`hooks/tlc-plan.md`](hooks/tlc-plan.md),
and a PostToolUse hook on the Skill tool, [`hooks/grill_on_tlc.py`](hooks/grill_on_tlc.py), reminds
the session to load `grill-me` the moment a `tlc-spec-*` skill loads, including after a compaction.

## How a feature closes

```mermaid
flowchart TD
  A[Build done] --> B[check_proofs.py green]
  B --> V[tlc-verifier]
  B --> S[tlc-screens-judge when a criterion cites a capture]
  B --> P[ponytail-reviewer]
  V --> F[One fix pass]
  S --> F
  P -- Must fix and Should fix --> F
  F --> M[check_proofs.py with mutations.json]
  M --> R[Screens round 2 when the code changed]
  R --> G[Gate and report]
```

The SessionStart hook also adds [`hooks/tlc-close.md`](hooks/tlc-close.md), so the session
dispatches these agents and folds the Ponytail findings into the fix pass:

- Must fix and Should fix join the single fix pass, each with its closing commit in
  `.specs/features/<feature>/ponytail-review.md`. Nice to have goes to the final report.
- An approved plan item counts as requested, so a review finding never cuts it. The plan's checks
  set the test bar; Ponytail's "one small test" is only the floor.

The TLC skills are copied unmodified. This plugin only adds the agents, the `grill-me` skill and
those rules around them.

## Recommended: keep Ponytail's rules out of the judges

Ponytail injects its coding rules into every subagent. A judge should not carry the rules of the
code it judges, so restrict Ponytail with its own matcher in `~/.claude/settings.json`:

```json
{
  "env": {
    "PONYTAIL_SUBAGENT_MATCHER": "^(?!.*(tlc-verifier|tlc-screens-judge|ponytail-reviewer)).*$"
  }
}
```

Ponytail tests this regex, case-insensitive, against each subagent's type. This one lets every
subagent through except the three above.

## Models and language

The three agents run on `opus` (Opus 5.5) with `effort: medium`, set in their frontmatter in
[`agents/`](agents). In our use, that costs less than Sonnet 5.5 at `xhigh` and returns about the
same results. They answer in the language of the prompt that dispatched them.

## Updating the TLC skills

`skills/` holds the upstream folders at the commit named in [`THIRD_PARTY.md`](THIRD_PARTY.md). To
update, replace both folders with the upstream ones at a newer commit, unmodified, record the new
commit there and bump the version in `.claude-plugin/plugin.json`.

## License

MIT for this plugin's own files: agents, hooks, manifests and docs. The TLC skills keep their own
licenses (skill text CC-BY-4.0, scripts MIT), and Ponytail is installed separately under MIT. See
[`THIRD_PARTY.md`](THIRD_PARTY.md).
