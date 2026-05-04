# Language Thinking

Choose the right language, runtime, or framework for the task. Consider the existing ecosystem, team familiarity, deployment context, and the nature of the problem being solved.

## When to use
- Starting a new tool or service from scratch
- Considering a rewrite or port of existing functionality
- The task has specific performance, concurrency, or ecosystem requirements

## Guiding questions
1. What does the existing codebase use? Is there a strong reason to diverge?
2. What are the runtime requirements — startup speed, memory, long-running process, one-shot script?
3. Does this need to compose with existing tools via pipes, stdin/stdout, or as a library?
4. What dependencies or ecosystem libraries does this task require? Which language has the best support?
5. Who maintains this after it ships — does the choice match the maintainer's fluency?

## Output structure
- Existing ecosystem context
- Candidate languages with trade-offs
- Recommended choice with rationale
- Migration or interop considerations
