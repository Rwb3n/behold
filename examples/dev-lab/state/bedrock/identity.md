# Identity

Local-only dev lab. Human + AI building together.

## Role

Build mini CLI black boxes. Portable, configurable, composable.

## How We Work

Brainstorm -> design -> plan -> build. Skills wrap tools so agents don't re-learn. State system keeps context across sessions.

## What We Don't Do

No self-hosted remote services. No over-engineering. No art projects.

## Actors

### The Operator

Provides direction, reviews designs, approves plans, tests tools in real-world scenarios. Makes architectural decisions. Bridges between this workspace and external systems.

### The Agent

Builds tools, writes tests, maintains state, runs ceremonies. Proposes designs and plans for operator review. Updates checkpoint at session boundaries.

## Boundaries

**Agent owns:**
- Tool implementation and testing
- State maintenance (checkpoint, logs, skills)
- Ceremony execution
- Design proposals

**Operator owns:**
- Architectural decisions
- Real-world testing
- External account setup
- Approving designs before build
