---
name: grill-me
description: >-
  Interviews the user in numbered rounds, each question with a recommendation,
  until no decision is left silently assumed: walks the decision tree, looks up
  facts in the code instead of asking, cross-checks claims against the code,
  keeps the repo glossary and closes with outcome and proof, without editing
  code. Load it on your own, unasked, when entering the Plan phase of
  tlc-spec-lean or the Specify/Discuss phase of tlc-spec-driven, and before
  implementing a request with several approaches, payments/auth or fuzzy scope.
  Also use for grill me, interview me, stress-test this plan, or an ambiguous term.
---

# Grill me

Interview the user until you share an understanding, deciding nothing for them. Merges a
one-question interview with `grilling` and `domain-modeling` from
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT).

Enter this mode when the request shows complexity (several approaches, blast radius, payments or
auth, fuzzy scope) and is not ready to build, unless the user explicitly opts out. A feature headed
for `tlc-spec-*`: the interview happens inside Plan/Specify (§ TLC), unasked: any gap (gray area,
assumption, ambiguous term, contradiction with the code) becomes a round before the plan decides.
Do not run one interview before and another inside it.

**Edits no code.** It writes only records: the session note, the glossary, the TLC files and, once
approved, the business-rules doc, the ADR and any memory the host keeps (§ Where each decision goes).

## Facts are yours, decisions are the user's

- A fact the repo, a tool or the web can answer: look it up, never ask. By default in the main
  window (`rg`, `fd`, reading the excerpt), because you need the excerpt to write the question. A
  search sub-agent only for a wide sweep (more than ~10 reads) where the conclusion is enough; then
  in the background, sending the questions that do not depend on it right away. A sub-agent pays a
  fixed cost and re-reads what you already read; resuming one carries its whole conversation.
- A user claim about how something works: check the code before accepting it. A contradiction
  becomes a question: *"you said X, but `foo.ts:42` does Y — which one holds?"*
- A decision (scope, priority, behaviour, trade-off, assumption, name): always asked, with a
  recommendation. Nothing that is the user's becomes a silent assumption to save a question; small
  assumptions go bundled (§ The round), but they go.

## Tree and frontier

List the explicit and implicit decisions (scope, actors, failure, contract, data, deploy, terms).
Only facts (searchable) and chores stay out of the tree; everything else goes in and gets asked,
the small ones in the Assumptions question. Mark each `open`, `closed`, `delegated` ("you decide")
or `deferred`. The **frontier** is the open ones whose dependencies are closed. A question that
depends on another in the same round goes to the next round.

The tree does not go to the chat; it goes to the **session note**, `grill-<topic>.md` in the
session's scratch directory (none: the system temp directory; never inside the repo): each Q with
number, status and answer, the last number used and the decisions still without a destination.
After a compaction, re-read this skill and the note before asking again. The note does not survive
into another session: what must last goes to the destinations in § Where each decision goes.

## The round

Open with one progress line: *"Round 2 — ~6 decisions left, about 2 rounds."* Send the frontier,
**up to 5 questions** (the Assumptions question does not count), the ones that unblock the most
branches first; the rest go next round (5 keeps the round readable in a chat; not measured, change
it if the user asks). Number across the session (Q1, Q2… never restart). Each question:

```
❓ **Q4 - <short title>**: <context in 1-2 sentences: which branch and why it matters now>.
<the question, worded so that "yes" accepts the recommendation>
Options: (a) … (b) … (c) you decide

➡️ <recommendation> — <one line of why: trade-off, risk or evidence from the repo>

---
```

Options only when more than one answer is defensible. Small, reversible decisions with local
impact (an internal name, an obvious default) do not get a Q each: they go together in a last
question of the round, *"Q8 - Assumptions: I will go with A, B and C. Yes accepts all; name a
letter to change it."* Close the round with the footer: *"'yes' accepts every recommendation;
'Q5 b' changes only Q5 and accepts the rest."*

- The footer is the rule: "yes" accepts all; naming a Q with another option changes that one and
  accepts the rest. A reply that only comments on or asks about a Q accepts nothing: answer the
  doubt and ask for the round's answer, without resending the questions.
- "You decide" is an answer: keep the recommendation, recorded as **delegated**, not as the user's
  choice (in TLC: `Confirmed? y` with `user delegated`).
- "Later" or a refusal: mark `deferred` and do not insist; it goes as an open question (§ TLC) or to
  the closing list. It never becomes your assumption.
- Record each answer in the turn it arrives (note, glossary, TLC file): a compaction keeps files,
  not chat.
- Contradiction between answers: one question only to reconcile, next round.
- An adjacent request: *"That sounds like another feature. I'll note it as a deferred idea and stay
  in the current scope."*

## Glossary

Works in any repo; the point is to speak the project's language, not to document a project.

- Before the first round, look for the repo glossary: `GLOSSARY.md`, `GLOSSARY-MAP.md`, or a
  `CONTEXT.md`/`docs/glossary*` that already has a terms section (follow the format it uses).
- No glossary: when the first term closes, ask (with a recommendation) whether to create
  `GLOSSARY.md` at the root. Refused: the terms stay in the session note.
- A user term that conflicts with the glossary, or an ambiguous one ("account": the login one or the
  billing one?), becomes a question with the canonical term as the recommendation. Invent an edge
  scenario that forces the boundary between two concepts.
- A closed term goes into the glossary at once, in the format of
  [references/glossary.md](references/glossary.md): domain terms only, in the repo's language
  (labels too), no implementation detail.
- Commit: in TLC, the glossary goes into the first Build commit (otherwise `check_proofs.py` reports
  a dirty tree); elsewhere, into the commit of the change.

## Where each decision goes

| Decision | During the interview | Final destination |
|---|---|---|
| Product or business rule | note (or TLC file) | the rules doc the repo's CLAUDE.md/AGENTS.md points to (none: `docs/business-rules.md`), in the commit that applies the rule |
| Hard-to-reverse architecture | note | ADR in `docs/adr/`, offered and approved (§ ADR); refused or failing the gate: stays in the note and the closing |
| Feature in `tlc-spec-*` | TLC file, in the turn (§ TLC) | the same |
| Term | glossary, in the turn | the same |
| Anything else (scope, approach, contract) | note | the closing bullets; with a plan, the plan |

If the implementation will not continue in this session, at the closing move what was only in the
note to wherever the host keeps project memory, including any business rule marked "pending in the
rules doc".

## TLC

Inside Plan (`tlc-spec-lean`) or Specify/Discuss (`tlc-spec-driven`), this skill is the format of
the questions and overrides their "How to ask" and "Ask them".

- Gray areas and every assumption go out in the rounds above. The driven rule that a low-stakes
  default is "stated as an assumption, never asked" and "Medium = log the rest as assumptions" do
  not apply: they become the Assumptions question.
- Destination in the turn: lean in `plan.md` (criterion, `Assumptions` row with `y`, `AD-NNN` in
  `.specs/STATE.md`); on lean's short path (under ~3 files, no one-way door), `checks.md`
  `## Intent`; driven in `spec.md` (`## Assumptions & Open Questions`).
- Deferred: in lean, an open question `blocks`, `blocks go-live` or `open`; in driven, a `user
  declined` row with your default and `Confirmed? n`. It is the only `n` the plan presents.
- An open architectural bet (two viable architectures), or a door that passes the 3 ADR criteria:
  ask whether it becomes an ADR **before** the plan and link it in `Sources`, as TLC requires. Other
  doors: a row in `## Landing`; `AD-NNN` in `STATE.md` only if it reaches past the feature.
- A business rule decided in the plan: the Build commit that applies it also adds the line to the
  rules doc.
- TLC's stop (present the plan and wait for approval) replaces § Closing.

## Closing

Stop when the frontier is empty: every branch visited, nothing silently assumed, no contradiction.
Restate in short bullets:

- **Outcome**: what will be true when done.
- **Proof**: the command, test, CI or artifact that shows it.
- **Threshold**: binary criterion or metric, when it fits.
- **Out of scope** and deferred ideas, if any.
- **Stop condition**: what makes you stop and ask again.

Ask whether the tree is closed, whether anything is missing, or whether to proceed. **Do not act
before the confirmation.** If the interview reveals a new feature: stop, open `tlc-spec-lean` (or
`tlc-spec-driven` for legacy code or a detailed design), run its "Before asking anything" and go on
in Plan, reusing the note without repeating questions.

## ADR (after the confirmation)

Offer one only if all 3 criteria hold: hard to reverse, surprising without context, the result of a
real trade-off. What usually qualifies, and the format: [references/adr.md](references/adr.md).
Draft it in the chat; write it only after the user approves text and number. Refused: do not offer
again in the session. In TLC, § TLC sets the timing.

## What this skill is not

- Not implementation: it edits no code.
- Not a formal spec: the output is alignment, glossary and bullets; the plan belongs to `tlc-spec-*`.
- Not exhaustive product discovery.
