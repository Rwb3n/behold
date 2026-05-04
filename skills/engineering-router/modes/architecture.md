# Architecture Thinking

Select structural patterns for the implementation. Decide between monolith and modular, choose layering strategy, and identify the right level of abstraction for the problem size.

## When to use
- Building something with more than one responsibility
- Deciding how to organize a new tool's internals
- A feature is growing beyond its original structure and needs reshaping

## Guiding questions
1. How many distinct responsibilities does this have? Can they be separated cleanly?
2. What is the expected growth trajectory — will this stay small or accumulate features?
3. Does this need a plugin or extension model, or is a single-file script sufficient?
4. What are the data flow patterns — pipeline, request-response, event-driven, batch?
5. Where does configuration live — flags, env vars, config file, hardcoded — and does the architecture support changing that later?

## Output structure
- Responsibility inventory
- Structural pattern recommendation (single script / module / layered / pipeline)
- Key boundaries and interfaces
- Complexity budget — is the structure proportional to the problem?
