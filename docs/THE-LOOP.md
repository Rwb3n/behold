# The Loop

The Loop is a fractal governance pattern. It describes how any system -- a project, an agent, a task, a single tool call -- organises itself to do work, produce value, and learn from what it produces. It is the theoretical foundation beneath the Behold framework. Behold is an instance of The Loop at workspace scale.

---

## The Pattern

```
BELIEFS --constrain--> METHODS --structure--> GATES
    ^                                            |
    |                                         trigger
    |                                            v
    \<--feedback---- PRODUCTS <--produce-- ACTIONS
                                            (units -> procedures
                                             -> atomic operations)
```

Five layers, connected in a loop:

### Beliefs

What you hold to be true. Core principles, identity, constraints, values. Beliefs do not describe work -- they constrain which approaches to work are valid and which are not. They are the most stable layer. They change rarely, and only when Products provide evidence that they should.

### Methods

How work is organised. Methods have a special role: they **select and adapt the framework** that shapes everything below them. Agile, Kanban, TDD, object-oriented design, "breathe don't run" -- these are all Methods-layer choices. Changing your Methods reshapes your Gates and Actions without requiring a change in Beliefs. This is the system's primary adaptation mechanism.

Methods are constrained by Beliefs. A Belief like "start simple, complicate when forced" rules out Methods that front-load complexity. A Belief like "async is default" rules out synchronous-only workflows.

### Gates

State transitions. A Gate marks the boundary between before and after -- a ceremony, a checkpoint, an approval step, a breath cycle. Gates do not do work. They trigger Actions, and they enforce the conditions under which Actions may begin or end.

Gates are structured by Methods. An Agile Method creates sprint boundaries and standups. A "breathe don't run" Method creates the wake-process-checkpoint-exit cycle. Different Methods produce different Gates from the same Beliefs.

### Actions

The work itself. Actions are where value is created. They have a defining structural property: **Actions always nest**.

- **Units** -- the coarse grain of work (an activity, an execution step, a pipeline stage)
- **Procedures** -- reusable sequences within a unit (a skill, a subroutine, a recipe)
- **Atomic operations** -- the smallest indivisible capability (a tool call, an API request, a shell command)

This nesting is not incidental. It appears at every scale where The Loop is instantiated. It is how complex work decomposes without losing coherence.

### Products

What was produced. Files, artifacts, decisions, memories, logs, lessons learned. Products are not just outputs -- they are **evidence**. They carry information about whether the system is working as intended.

Products feed back into Beliefs through two paths:

- **Validation** -- Products reflect Beliefs. When they do, the system is healthy. When they don't, something in the Methods, Gates, or Actions chain has drifted. Fix the drift.
- **Amendment** -- Products reveal that a Belief is wrong or incomplete. A lesson learned contradicts a principle. A working prototype proves an assumption was false. The Belief itself is revised.

Validation is the default. Amendment is the exception. But amendment is what makes The Loop a loop and not a hierarchy. Without it, you have a top-down command chain. With it, you have a system that learns.

---

## Properties

### Fractal

The Loop recurs at every scale. The same 5-layer pattern governs a project, an agent within that project, a task within that agent, and a tool call within that task.

| Layer | Project | Agent | Task | Tool Call |
|-------|---------|-------|------|-----------|
| Beliefs | Principles | Bedrock (identity + principles) | Context document (constraints, goals) | System prompt |
| Methods | Ways of working | Agent config (models, budgets, scoping) | Workflow config (step definitions) | Permission mode |
| Gates | Ceremonies | Session boundaries (open -> work -> close) | Step boundaries | Approval gate |
| Actions | Activities (contain skills contain tools) | Execution steps (contain substeps contain tool calls) | Step function (reads input, calls LLM/tools, produces output) | Tool execution |
| Products | Assets | Logs, memories, outbox items | Output blocks | Tool result |

Each level composes instances of the level below it. A Ceremony triggers Activities. An Activity invokes Skills. A Skill calls Tools. The nesting is recursive -- each level is a Loop made of smaller Loops.

### Self-Amending

The system revises itself through its own operation. Products feed back into Beliefs. Beliefs are themselves Products (a Principles document is an asset). This means the system is subject to its own governance -- it can change its own rules, but only through the processes those rules define.

This is not a bug. It is the core property. A system that cannot amend its own Beliefs becomes rigid. A system that can amend them without process becomes chaotic. The Loop provides the structure for disciplined self-revision: produce evidence, evaluate evidence against Beliefs, amend when warranted.

### Actions Nest

The Actions layer always decomposes into units -> procedures -> atomic operations. This is true at every scale:

| Scale | Units | Procedures | Atomic Operations |
|-------|-------|------------|-------------------|
| Project | Activities | Skills | Tools |
| Agent | Execution steps | Substeps | Tool calls / API calls |
| Task | Pipeline stages | Stage functions | Shell commands / LLM calls |

The nesting provides composability. Procedures can be reused across units. Atomic operations can be reused across procedures. This is how a system scales its capabilities without scaling its complexity proportionally.

---

## Behold as an Instance

Behold instantiates The Loop at workspace scale:

```
PRINCIPLES --inform--> WAYS OF WORKING --structure--> CEREMONIES
     ^                                                      |
     |                                                   trigger
     |                                                      v
     \<--feedback--- ASSETS <--produce--- SKILLS/ACTIVITIES
```

| Loop Layer | Behold Concept | Location |
|------------|---------------|----------|
| Beliefs | Principles (P1-P7) | `state/bedrock/principles.md` |
| Methods | Ways of working, environment config | `state/bedrock/` |
| Gates | Ceremonies (session-open, session-close, staleness-sweep, etc.) | `skills/` (ceremony-type skills) |
| Actions | Skills (workflow/tool types) and the work they perform | `skills/` |
| Products | State files, logs, checkpoint, backlog, lessons | `state/flow/`, `docs/` |

The system is **self-amending**: Principles are themselves assets (Products), subject to revision through the very ceremonies (Gates) they govern. This is Behold's implementation of P6 (Feedback Over Prescription).
