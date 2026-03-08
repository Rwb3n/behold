---
name: retro
type: workflow
trigger: end of session (invoked by session-close), or ad-hoc
cadence: every session (via session-close), or on demand
depends: none
references: P6 (Feedback Over Prescription)
provenance: inline keep/stop/start retros produce shallow feedback; the 3-layer structure (reflection, classification, action register) produces actionable items with explicit lifecycle
---

# Retro

Structured retrospective that produces actionable items, not just observations.

## Three Layers

### Layer 1: Reflection

Present observations and discuss with the operator:
- **Keep doing:** What worked well?
- **Stop doing:** What wasted time or caused friction?
- **Start doing:** What was missing or would help next time?
- **What surprised you?** Unexpected outcomes, good or bad.
- **Skill amendment detection:** If a start/stop describes a repeatable ceremony failure, name the skill that should change.

### Layer 2: Classification

Every item from reflection is classified into exactly one bucket:

| Classification | Meaning | Action |
|---------------|---------|--------|
| bug | Broken, fix it | Fix now or queue |
| feature | Working, protect it | Document or test |
| feature request | Missing, build it | Design and queue |
| refactor | Functional but poorly structured | Redesign |
| upgrade | Functional but capped | Enhance |

### Layer 3: Action Register

One row per actionable item from classification.

| # | Item | Priority | Status | Owner | Definition of Done |
|---|------|----------|--------|-------|--------------------|

**Rules:**
- Before writing each action, check if the Definition of Done is already met. If so, mark as `done` immediately.
- Priority: `now` / `next` / `later`.
- Status: `open` or `done`.
- Actions with status `open` are appended to `state/flow/backlog.md` during session-close triage.

## Output

Write the retro to the session log alongside the session's work record.

## Scope

This skill can be invoked at multiple scopes:
- **Session** -- invoked by session-close at end of every session.
- **Feature** -- after completing a milestone or significant piece of work.
- **Ad-hoc** -- when the operator requests reflection at any point.

The scope determines what gets reflected on; the structure remains the same.
