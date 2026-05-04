---
name: judgment-router
description: Use when making quality, priority, or taste decisions — evaluating outputs, curating content, triaging work, assessing risk. The scarce faculty.
type: tool
depends: []
sub-skills: modes/*.md
provenance: taste decisions happened implicitly without structured consideration
limits:
  reads: []
  writes: []
  forbidden_writes: []
---

# Judgment Router

Select 1-3 judgment modes to apply before making quality, priority, or taste decisions.

## Mode Index

| Mode | Lens |
|------|------|
| Evaluation | Is this output good enough? Quality gate |
| Prioritization | What matters most right now? Constraint-first |
| Curation | Worth keeping, ingesting, remembering? |
| Risk-appetite | How careful should we be? Blast radius |
| Taste | Does this feel right? Aesthetic/design coherence |
| Triage | Classify, route, disposition |
| Curiosity | What's worth looking at next? Attention direction |

## Routing

### Manual invocation

User requests a mode or says `/judgment-router`. Read the requested mode file(s) from `modes/`, apply them.

### Agent-initiated

When you judge a judgment mode would genuinely add value, select based on task signals:

| Task type | Recommended modes |
|-----------|------------------|
| Reviewing output / code | Evaluation + Taste |
| Backlog / sprint planning | Prioritization + Risk-appetite |
| Content ingestion | Curation + Evaluation |
| Memory dream triage | Curation + Triage |
| Design decisions | Taste + Risk-appetite |
| Inbox processing | Triage + Prioritization |
| Exploration / direction-finding | Curiosity + Prioritization |
| Post-investigation | Curiosity + Curation |

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
