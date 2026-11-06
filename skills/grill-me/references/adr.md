# ADR

Adapted from `ADR-FORMAT.md` in [mattpocock/skills](https://github.com/mattpocock/skills)
(domain-modeling, MIT).

## Where

`docs/adr/NNNN-slug.md`, numbered after the highest existing number. Create `docs/adr/` only when
the first ADR is approved. A repo with `GLOSSARY-MAP.md` and several contexts: a decision of one
context goes in that context's `docs/adr/`; one that crosses contexts, in the root one. A repo that
already has another ADR format: follow it.

## Minimal format

```md
# {Short title of the decision}

{1-3 sentences: the context, what we decided and why.}
```

Optional sections, only when they add something:

- **Status** in frontmatter (`proposed | accepted | deprecated | superseded by ADR-NNNN`): when the
  decision may be revisited.
- **Considered options**: when the rejected alternative is worth remembering.
- **Consequences**: when there is a non-obvious downstream effect.

## What usually passes the 3-criteria gate

- **Architectural shape**: a monorepo; event-sourced writes with a read model projected into Postgres.
- **Integration between contexts**: domain events instead of synchronous HTTP.
- **Technology with lock-in**: database, message bus, auth provider, deploy target (not every library).
- **Boundary and scope**: who owns which data; the explicit no's count as much as the yes's.
- **Deliberate deviation from the obvious**: hand-written SQL instead of an ORM, for a reason. Stops
  someone from "fixing" it.
- **Constraints the code does not show**: compliance, a partner's latency contract, a cost ceiling.
- **An alternative rejected for a subtle reason**: otherwise someone suggests it again in six months.

Easy to reverse, unsurprising, or with no real alternative: not an ADR.
