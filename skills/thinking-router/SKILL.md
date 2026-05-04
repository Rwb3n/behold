---
name: thinking-router
description: Use when facing a problem that benefits from structured thinking — debugging, design, risk analysis, trade-off evaluation, or when the user requests a specific thinking mode. Can be manually invoked or agent-initiated.
type: tool
depends: []
sub-skills: modes/*.md
provenance: problem-solving defaulted to one thinking style
limits:
  reads: []
  writes: []
  forbidden_writes: []
---

# Thinking Router

Select 1-3 cognitive thinking modes to apply before working on a problem.

## Mode Index

| Mode | Lens |
|------|------|
| Causal | Trace cause and effect chains |
| Abstract | Extract general principles from specifics |
| Nonlinear | Explore feedback loops and emergent behavior |
| Recursive | Decompose into self-similar subproblems |
| Epistemic | Examine what you know, don't know, and can't know |
| Heuristic | Apply practical rules of thumb and mental shortcuts |
| Bayesian | Update beliefs based on evidence and priors |
| Dialectical | Explore opposing viewpoints to find synthesis |
| Integrative | Hold multiple models simultaneously, find creative resolution |
| Probabilistic | Reason about likelihoods and distributions |
| Hypothetical | Construct and test "what if" scenarios |
| Counterfactual | Examine "what would have happened if" alternatives |
| Investigative | Navigate a data substrate to surface non-obvious patterns |
| Lateral | Generate non-obvious hypotheses — fight the bell curve |
| Falsification | Surface what could contradict your conclusion — then check |

## Routing

### Manual invocation

User requests a mode or says `/thinking-router`. Read the requested mode file(s) from `modes/`, apply them.

### Agent-initiated

When you judge a thinking mode would genuinely add value, select based on task signals:

| Task type | Recommended modes |
|-----------|------------------|
| Debugging | Causal + Hypothetical |
| Design / architecture | Integrative + Abstract |
| Risk / uncertainty | Bayesian + Probabilistic |
| Evaluating trade-offs | Dialectical + Counterfactual |
| Exploring unknowns | Epistemic + Heuristic |
| Decomposing complexity | Recursive + Nonlinear |
| Data investigation | Investigative + Epistemic |
| Designing a playbook | Lateral + Investigative |
| Generating hypotheses from data | Lateral + Hypothetical |
| Committing to a conclusion | Falsification + Epistemic |
| Closing an investigation | Falsification + Bayesian |
| Dismissing an option | Falsification + Counterfactual |

Pick 1-3 modes. Read their files from `modes/` for guiding questions and structure.

## Output Format

For each selected mode, produce a visible reasoning block:

**Thinking [Mode Name]:**
[Work through that mode's guiding questions]

**Thinking [Mode Name 2]:** (if layered)
[Work through second mode's guiding questions]

**Synthesis:** (only when 2+ modes used)
[Integrated conclusion drawing from the modes applied]

Then proceed with the task.

## Constraints

- Max 3 modes per task
- Only apply when it genuinely adds value — not every task needs this
- Read mode files for depth; don't guess the guiding questions
- **Fitness check before applying a mode:** state the base case or trigger that makes this mode fit *this specific context* in one sentence. If you can't state it cleanly, drop the mode and pick another. Performing a mode because it was selected wastes the selection and produces mode theater instead of thinking.
