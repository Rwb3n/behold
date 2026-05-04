# Contract-First

Declare the public surface before writing the implementation. For any tool with consumers beyond the author — CLI flags, JSON output, exit codes, stderr semantics, skill wrappers — write the contract in SKILL.md first, then implement to the spec.

The bedrock rule: **forward-looking interfaces, simple implementations**. Interfaces are cheap declarations, implementations are expensive. Consumers code against the finished contract; the internals catch up later.

## When to use

- About to build a new CLI tool that other skills or ceremonies will invoke
- Adding a new subcommand or flag to an existing tool
- Defining a machine-readable output shape (JSON, TSV, structured logs) that other tools will parse
- Designing a new ceremony or workflow that will be called by other ceremonies

## Guiding questions

1. What commands, subcommands, and flags does this tool expose? Write them as usage lines.
2. For each flag, what does it mean, what's the default, and when would a caller use it?
3. What does the output look like in each mode? For JSON: write out every field and its type. For text: write out the exact format.
4. What exit codes does it return and under what conditions?
5. What goes to stderr vs stdout?
6. Who will call this tool? Name the consumers. If you can't name a consumer, you don't yet have a contract — defer and wait for the real need.
7. What does the skill wrapper promise about invocation discipline (when to use, when not to use)?

## Output structure

Draft the SKILL.md body in order:

1. **Usage** — one line per command, copy-pasteable
2. **Output shapes** — full JSON schema OR exact text format for every mode
3. **Exit codes** — table of codes and their meanings
4. **Consumers** — list of skills/ceremonies/tools that invoke this, and from where
5. **When to use / when not to use** — invocation discipline

Only after the SKILL.md body is drafted should implementation begin. The bash/python should be a mechanical translation of the declared contract, not a creative act.

## Anti-pattern this prevents

Code-first ordering, where implementation ships and documentation chases across subsequent commits. Symptoms:
- Skill doc added in a commit after the tool
- JSON field names changed once (implementation), then the doc updated in a follow-up commit
- Doc partial match to actual output shape (some fields documented, others emitted silently)

If you find yourself committing a code change and then committing a doc update to match, the order was wrong. The signal is specific enough to be its own smoke test: a ship sequence that has `code` before `docs` for the same surface is a contract-first violation.

## Constraint

Contract-first does not mean big-design-up-front. The contract is minimal — only the surface the first real consumer needs. Future extensions follow the same discipline: declare the extension in SKILL.md, then implement.
