# Third-party content

## Tech Leads Club agent skills

- `skills/tlc-spec-lean/` and `skills/tlc-spec-driven/` are copied unmodified from
  [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills), path
  `packages/skills-catalog/skills/(development)/`, commit
  `738451e40785750a8e8de5bce8112675f5f0df02`.
- Author: Tech Leads Club. The skill text (`SKILL.md` and its references) is licensed
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/); the scripts are under the MIT License.
  The upstream license, with its dual-licensing note, is in
  [`licenses/tech-leads-club-agent-skills-LICENSE`](licenses/tech-leads-club-agent-skills-LICENSE).
- Nothing in these folders was changed. This plugin adds agents, the `grill-me` skill and session
  rules around them.

## Matt Pocock's skills

- `skills/grill-me/` adapts the `grilling` and `domain-modeling` skills (including
  `GLOSSARY-FORMAT.md` and `ADR-FORMAT.md`) from [mattpocock/skills](https://github.com/mattpocock/skills),
  commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`, under the MIT License. The text was rewritten
  and merged with a one-question interview; the round format, glossary rules and ADR gate come from there.

## Ponytail

- Not bundled. The `ponytail-reviewer` agent loads the `ponytail-review` skill from the
  [Ponytail](https://github.com/DietrichGebert/ponytail) plugin (MIT), which you install separately.
