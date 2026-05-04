# Build-vs-Reuse Thinking

Apply the economy principle. Before building something new, check whether existing tools, libraries, or compositions of current capabilities already solve the problem. Prefer reuse over invention.

## When to use
- About to create a new tool or script
- A feature request sounds similar to something that already exists
- The solution might be a shell one-liner or a composition of existing tools

## Guiding questions
1. Does an existing tool in the project already do this, or do 80% of it?
2. Can this be solved by composing existing tools with pipes, wrappers, or aliases?
3. Is there a standard Unix tool or well-maintained package that handles this?
4. What is the maintenance cost of building new vs extending existing?
5. If I build new, am I duplicating logic that should live in one place?

## Output structure
- Existing capabilities inventory (what already does part of this)
- Reuse option with gap analysis
- Build option with scope estimate
- Recommendation with economy rationale
