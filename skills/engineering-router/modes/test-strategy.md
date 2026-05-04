# Test-Strategy Thinking

Choose the right testing approach for the change. Not everything needs TDD — match the testing investment to the risk, complexity, and expected lifespan of the code.

## When to use
- Before writing implementation, to decide what testing approach fits
- A change touches logic that is easy to get wrong or hard to verify manually
- Deciding between no tests, smoke tests, unit tests, or integration tests

## Guiding questions
1. What is the cost of a bug here — silent data loss, visible error, minor annoyance?
2. Is this logic deterministic and testable, or does it depend on external state (network, filesystem, APIs)?
3. How long will this code live — throwaway script or core infrastructure?
4. Can I test this with a quick manual check, or do I need automated verification?
5. What is the simplest test that would catch the most likely failure mode?

## Output structure
- Risk assessment (what breaks if this is wrong)
- Testing approach (none / manual smoke test / automated unit / integration)
- Key test cases if automated
- Verification command or manual check procedure
