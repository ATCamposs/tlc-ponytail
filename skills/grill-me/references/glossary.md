# Glossary format

Adapted from `GLOSSARY-FORMAT.md` in [mattpocock/skills](https://github.com/mattpocock/skills)
(domain-modeling, MIT).

```md
# {Context name}

{1-2 sentences: what this context is and why it exists.}

## Language

**Order**:
{1-2 sentences: what the term IS, not what it does.}
_Avoid_: purchase, transaction
```

## Rules

- **Be opinionated.** Several words for one concept: pick one and list the others under `_Avoid_`.
- **Short definitions**, one or two sentences.
- **Domain terms only.** General programming concepts (timeout, retry, cache) stay out, however
  much the project uses them.
- **No implementation**: no table, field, endpoint or technical decision. Not a spec, not a scratch pad.
- Group under subheadings when natural clusters appear; otherwise a flat list.
- Language: the repo's, labels included (a Portuguese repo writes `## Linguagem`, `_Evitar_`). A name
  the code uses in another language appears as a synonym, not under `_Avoid_`.

## Repo with several contexts

`GLOSSARY-MAP.md` at the root lists the contexts, where each one's `GLOSSARY.md` lives and how they
relate. If the map exists, read it and infer the context of the topic; when unclear, ask. Only a root
glossary: single context. None: ask whether to create the root `GLOSSARY.md` when the first term
closes (SKILL.md § Glossary).
