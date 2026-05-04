# Integration Thinking

Determine how new code connects to the existing codebase, tools, and workflows. Identify touch points, dependencies, and the risk of breaking what already works.

## When to use
- Adding a feature to an existing tool
- New code needs to interact with established conventions or shared state
- Changes touch multiple files or systems that other tools depend on

## Guiding questions
1. What existing code does this touch? What are the entry points and call sites?
2. Are there established conventions (naming, file layout, config format) this must follow?
3. What breaks if this integration is wrong — who or what depends on the current interface?
4. Does this change require updates to skill files, aliases, or documentation?
5. Can this be integrated incrementally, or does it require a coordinated switch?

## Output structure
- Touch points in existing code
- Convention compliance checklist
- Blast radius — what could break
- Integration sequence (order of changes)
