---
name: golden
type: tool
description: Manage golden suite regression tests — behavioral assertions that gate governance edits and serve as a review lens.
depends: []
limits:
  reads: []
  writes: []
  forbidden_writes: []
---

# Golden Suite

Validated behavioral assertions that gate governance changes and serve as a review lens for all work.

## Concept

A golden suite is a set of behavioral assertions — not code tests, but statements about how the agent should behave that have been validated through experience. They serve three purposes:

1. **Gate:** Before modifying governance (principles, methods, ceremonies), check assertions for conflicts
2. **Lens:** When reviewing plans, designs, or code, use assertions as a checklist
3. **Accumulator:** When corrections happen in-session, propose new assertions

## Data Format

Store assertions in a JSONL file (one per line):

```json
{"uid": "gs000001", "assertion": "Evidence before claims — no completion status without fresh verification output", "category": "operations", "source": "24 failure memories", "sessions": ["s1", "s5"], "promoted": "2026-03-15"}
```

## Categories

| Category | What it covers |
|----------|---------------|
| operations | How we work day-to-day |
| governance | Router discipline, evidence thresholds |
| architecture | Schema, state system, structural rules |
| knowledge | Memory quality, recall discipline |

## Usage

### Proposing assertions

When you observe a correction, a repeated mistake, or a validated pattern:

```
Propose: "Never emit a score without inline evidence"
Category: governance
Source: session where naked scores caused confusion
```

Stage proposals for human review. Never auto-promote.

### Review lens

Before reviewing a plan, design, or PR, load assertions from the relevant category:

1. Read the golden suite file
2. Filter to the category matching the work
3. Use each assertion as a checklist item
4. Flag any work that violates an assertion

### Gating governance changes

Before editing principles, methods, or ceremonies:

1. Load the full suite
2. Check: does the proposed change conflict with any assertion?
3. If conflict: either the change is wrong, or the assertion needs updating — surface the tension explicitly

## Bootstrap

To start a golden suite from scratch:

1. Create the JSONL file in your project's governance directory
2. Seed with 3-5 assertions from your most painful past mistakes
3. Add assertions only when validated by 2+ sessions of evidence
4. Cap at 50 active assertions — if adding one, retire the least-recalled

## Principles

- **Evidence threshold:** 2+ sessions of confirming evidence before promotion
- **Cap:** 50 active assertions max — forces prioritization
- **Human gate:** proposals are staged, never auto-promoted
- **Living document:** assertions that stop being recalled or relevant get retired
