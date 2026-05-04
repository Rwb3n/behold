---
name: session-router
description: Route session activities through the right skills in the right order. Ensures process consistency and surfaces optimisation opportunities. The meta-router — routes the work, not the thinking.
type: tool
depends: [thinking-router, judgment-router, engineering-router]
limits:
  reads: []
  writes: []
  forbidden_writes: []
---

# Session Router

Routes session activities through the right process at the right time. The three faculty routers (thinking, judgment, engineering) route *how* you think. Session router routes *what* you do and in *what order*.

## Mode Index

| Mode | When to use |
|------|-------------|
| explore | "What should we look at?" — no hypothesis yet, just curiosity |
| spike | "Does this work?" — validate an API, data source, or approach before building |
| design | "What are we building?" — brainstorming, spec, review |
| build | "Let's build it." — plan, execute, test, commit |
| fix | "Something's broken." — systematic debugging, verify, commit |
| review | "Is this right?" — falsification, code review, spec review |
| triage | "Classify and route." — inbox, backlog, sweeps, priorities |
| ship | "We're done." — docs, cleanup, commit |

## Routing Table

| User signal | Mode | Process |
|-------------|------|---------|
| "What's out there?" / "What APIs exist?" | explore | web search, repo exploration |
| "Does this work?" / "Let's spike it" | spike | validate approach before committing |
| "I want to build X" / "Let's design" | design | brainstorming, then writing plans |
| "Build it" / "Let's go" | build | follow the plan, execute, test |
| "Something's broken" / "Hunt for bugs" | fix | systematic debugging, verify, commit |
| "Is this right?" / "Review this" | review | falsification, code review |
| "Triage inbox" / "Backlog" / "Sweeps" | triage | classify, prioritize, route |
| "Ship it" / "Wrap up" | ship | docs, cleanup, commit |

## Process Chains

Common multi-mode sequences that should flow naturally:

### New feature
```
explore → spike → design → build → ship
```
Each transition has a gate:
- explore → spike: "we found something worth testing"
- spike → design: "it works, let's design around it"
- design → build: "spec approved"
- build → ship: "tests pass, docs updated"

### New data source for existing system
```
spike → review → build → ship
```
Gate: spike validates the source before any code.

### Knowledge session
```
explore → triage → (optionally) design
```
Absorb material, then classify what's actionable. If it surfaces a buildable idea, transition to design.

### Bug fix session
```
fix → review → ship
```
Systematic debugging, verify the fix, commit.

## Anti-patterns this router prevents

| Anti-pattern | What happens | Session router fix |
|---|---|---|
| Build before spike | Write adapter for API that doesn't work | spike mode gates design mode |
| Design without research | Reinvent patterns already solved | design mode checks prior art |
| Build without plan | Ad-hoc coding, missed edge cases | build mode requires a plan |
| Ship without docs | Stale documentation, context lost | ship mode includes doc update |
| Router fatigue | Invoke all 3 routers on every tiny decision | Session router selects which routers matter per mode |

## Router composition per mode

Not every mode needs all three faculty routers. This table prevents over-routing:

| Session mode | Thinking router | Judgment router | Engineering router |
|---|---|---|---|
| explore | Lateral, Curiosity | Curiosity | — |
| spike | Falsification | Risk-appetite | Build-vs-reuse |
| design | Integrative, Abstract | Taste, Prioritization | Architecture, Contract-first |
| build | — (plan is the guide) | — | Integration, Test-strategy |
| fix | Causal, Hypothetical | — | Integration |
| review | Falsification | Evaluation | Integration |
| triage | Heuristic | Triage, Prioritization | — |
| ship | — | Evaluation | — |

"—" means: don't invoke that router for this mode unless the user explicitly asks.

## Usage

Session router is advisory, not enforced. It's consulted at mode transitions. The user can override at any time — "just build it" skips design if they've already thought it through.

The value is in **making the process visible** so it can be iterated on. An invisible process can't be improved.
