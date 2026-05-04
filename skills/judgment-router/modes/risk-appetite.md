# Risk Appetite

Calibrate how careful to be. Not all actions carry equal blast radius — a typo in a log message differs from a typo in a database migration. Match caution to consequence, avoid both recklessness and paralysis.

## When to use
- Deciding whether to take a shortcut or do it properly
- Assessing whether a change needs review, testing, or can go direct
- Choosing between a safe incremental approach and a bold refactor

## Guiding questions
1. What is the blast radius if this goes wrong? (scope: file, repo, system, user-facing)
2. Is the damage reversible? How quickly and at what cost?
3. What is the cost of being extra careful here? Is the caution proportionate?
4. Are there unknowns that increase the real risk beyond what's visible?
5. What is the minimum viable safeguard — the cheapest action that meaningfully reduces risk?

## Output structure
- Blast radius assessment (contained / spreading / catastrophic)
- Reversibility (trivial / costly / irreversible)
- Recommended caution level (move fast / standard care / extra verification)
- Minimum safeguard to apply
