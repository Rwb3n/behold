---
name: engineering-router
description: Use when selecting implementation approach — language, architecture, integration strategy, test approach. Invoked before building, after design decisions.
type: tool
depends: []
sub-skills: modes/*.md
provenance: jumped to implementation without considering alternatives
limits:
  reads: []
  writes: []
  forbidden_writes: []
---

# Engineering Router

Select 1-3 engineering modes to apply before implementing a solution.

## Mode Index

| Mode | Lens |
|------|------|
| Language | Which language/runtime fits this task |
| Architecture | Monolith vs modular, pattern selection |
| Integration | Where does this plug into existing code |
| Test-strategy | TDD, smoke test, integration, none |
| Build-vs-reuse | Can existing tools do this? Economy principle |
| Spike-vs-commit | Prototype first or build for keeps |
| Contract-first | Declare the interface / JSON / CLI surface before writing the implementation |

## Routing

### Manual invocation

User requests a mode or says `/engineering-router`. Read the requested mode file(s) from `modes/`, apply them.

### Agent-initiated

When you judge an engineering mode would genuinely add value, select based on task signals:

| Task type | Recommended modes |
|-----------|------------------|
| New CLI tool | Contract-first + Language + Architecture |
| Adding a machine-readable output (JSON/TSV) to existing tool | Contract-first + Integration |
| Adding to existing tool | Integration + Test-strategy |
| Greenfield feature | Build-vs-reuse + Architecture |
| Quick fix / patch | Spike-vs-commit + Integration |
| Exploring unknowns | Spike-vs-commit + Build-vs-reuse |
| Performance work | Language + Test-strategy |

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
