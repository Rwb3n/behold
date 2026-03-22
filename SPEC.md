# Behold

**Structure for systems that remember.**

An opinionated specification for building persistent, ceremony-driven workspaces where humans and AI agents collaborate with continuity.

---

## 1. Introduction

### The Problem

AI agents are stateless. Complex systems drift. Humans and agents work in different sessions, at different times, with different context. Without structure, every session starts from zero, knowledge evaporates, and entropy wins.

### The Thesis

Three layers solve this:

1. **Continuity** (foundation) -- persistent, tiered state that survives session boundaries and context loss.
2. **Entropy resistance** (mechanism) -- ceremonies that force observation, reflection, and handoff.
3. **Collaboration structure** (outcome) -- defined actors, boundaries, and feedback loops.

### What Behold Is

- A specification for workspace architecture.
- An opinionated set of patterns, not a software library.
- Language-agnostic, platform-agnostic, agent-agnostic.
- Designed for one human and one or more AI agents, but scales to teams.

### What Behold Is Not

- A framework you `npm install`.
- Tied to any specific AI model or agent platform.
- An agent framework -- no runtime infrastructure, no message buses, no routing services. Behold describes skill design patterns for multi-agent work; it does not provide the mechanism.
- A project management methodology.

---

## 2. Core Concepts

Five foundational concepts underpin every Behold workspace.

### The Workspace

The shared environment where human and agent operate. A directory on a filesystem -- git-tracked, human-readable, agent-readable. The workspace is the map, not the territory. It represents a system but is not the system itself. When the map diverges from reality, that is a bug.

### Actors

Every workspace has at least two actors:

- **The Operator** -- the human. Owns all decisions. Provides intent, approves destructive changes, bridges the gap between map and territory.
- **The Agent** -- the AI. Maintains the map, runs ceremonies, holds continuity across sessions, proposes and executes work. Stateless by nature, made persistent by the framework.

Actors have defined boundaries -- what each owns, what requires the other. These are explicit, not assumed.

### State

All persistent knowledge lives in state, organized into tiers by how often it changes:

| Tier | Changes | Contains | Read |
|------|---------|----------|------|
| Bedrock | Rarely | Principles, identity, environment, boundaries | Every session |
| Shelf | Weekly | Skills, configs, reference docs | On demand |
| Flow | Every session | Checkpoint, goals, logs, active work | On resume |

The tiering tells the agent what to load when, and signals what is safe to change without asking.

### Rhythm

Ceremonies are the heartbeat. They force the workspace to observe itself at regular intervals. Ceremonies are defined by: trigger, cadence, steps, and output. They are not optional rituals -- they are the mechanism by which the system maintains itself.

### Feedback

The system is self-amending. Lessons flow upward: session retros update ceremonies, repeated friction updates principles, stale items get surfaced and resolved. This is the core defense against ossification.

```
BEDROCK ---informs---> SHELF ---structures---> FLOW
   ^                                            |
   |                                         produces
   |                                            v
   \<--- feedback --- OBSERVATIONS <--- CEREMONIES
```

---

## 3. Principles

Seven principles govern every Behold workspace.

### P1: Continuity Over Capability

The ability to pick up where you left off matters more than how much you can do in a single session.

**Implies:**
- Checkpoint before you would regret losing context.
- State persistence is not optional.
- Session boundaries are handled, not ignored.

**Does not mean:**
- Hoard everything -- prune aggressively.
- Sacrifice capability -- continuity enables it.

### P2: Observe Before You Act

Check what exists before building. Read before writing. Look before theorizing.

**Implies:**
- Session Open reads state before proposing work.
- Ceremonies check reality before updating docs.
- Agents verify before assuming.

**Does not mean:**
- Analysis paralysis.
- Never act on instinct.

### P3: Entropy Is the Default

Systems drift toward disorder. Documentation goes stale. State diverges from reality. This is not a risk -- it is a certainty.

**Implies:**
- Staleness sweeps are required, not optional.
- Freshness thresholds are explicit.
- Unobserved state is suspect state.

**Does not mean:**
- Constant churn.
- Rewrite everything every week.

### P4: Earn Complexity

Start with the simplest thing that works. Add structure when the absence of structure causes pain.

**Implies:**
- Do not add ceremonies you do not need yet.
- Do not build tools "just in case."
- Let the system tell you what it needs.

**Does not mean:**
- No planning.
- No upfront structure (the starter kit is the minimum viable structure).

### P5: Map and Territory

The workspace is a representation of something real. When the map diverges from reality, the map is wrong.

**Implies:**
- Verify the map against the territory regularly.
- Do not document hypotheticals as facts.
- Agents that can reach the territory should check it directly.

**Does not mean:**
- Document everything in real-time.
- No abstractions or summaries.

### P6: Feedback Over Prescription

The system amends itself. Lessons flow upward into principles. Retros update ceremonies. Friction triggers review.

**Implies:**
- Every ceremony produces observations.
- Observations accumulate into patterns.
- Patterns justify amendments.

**Does not mean:**
- Change things after one data point.
- No stable foundation.

### P7: Boundaries Are Load-Bearing

Explicit boundaries between actors, between state tiers, and between interactive and autonomous agents prevent the wrong thing from changing at the wrong time.

**Implies:**
- Define who owns what.
- Bedrock requires operator approval to change.
- Autonomous agents have stricter constraints than interactive ones.

**Does not mean:**
- Bureaucracy for its own sake.
- Agents cannot act without permission on routine matters.

---

## 4. State Architecture

### Directory Layout

```
workspace/
  state/
    bedrock/
      principles.md
      identity.md
      environment.md
      methods.md
    shelf/
      skills/
      configs/
    flow/
      checkpoint.md
      backlog.md
      goals.md
      log/
      inbox/
  skills/
  tools/
  docs/
    plans/
    decisions/
  AGENTS.md
```

### Session Orientation

Session Open MUST produce orientation: what is active, what happened recently, what is next. This orientation is a prerequisite for planning.

HOW orientation is produced is implementation-specific. Valid approaches include:
- A checkpoint file maintained across sessions.
- A gather script that assembles orientation from git, filesystem, and memory.
- Direct inspection of goals.md, backlog.md, and recent logs.
- Any combination of the above.

If a workspace uses a checkpoint file, it SHOULD be treated as a **cache** (derived state), not a source of truth. It MAY become stale; sessions SHOULD verify it against authoritative sources.

**Source state** (must be persisted, cannot be regenerated):
- `goals.md` -- current intent.
- `backlog.md` -- prioritised work queue.
- `log/` -- append-only session records.
- `bedrock/` -- principles, identity, methods.

**Derived state** (must be available, can be regenerated):
- Checkpoint / orientation briefing.
- Summary indices.
- Cached computations.

When a workspace matures, create shelf-level tracking documents for detailed work breakdowns. The tracking taxonomy is workspace-specific -- epics, sprints, arcs, chapters, or any structure that fits the domain. Behold does not prescribe the vocabulary; it prescribes the tier separation. Detailed tracking is shelf-frequency (changes weekly), not flow-frequency (changes every session).

### The Methods Layer

`state/bedrock/methods.md` declares how work is done -- named process constraints that inform which approaches are valid. Methods are distinct from principles:

- **Principles** say WHY -- values and constraints on thinking. ("Start simple, complicate when forced.")
- **Methods** say HOW WE WORK -- constraints on process. ("Brainstorm before building." "TDD when building tools.")

A principle like "earn complexity" constrains what you build. A method like "design before plan" constrains how you build it. Principles are abstract and rarely change. Methods are concrete and may evolve as the workspace matures.

Methods are bedrock-tier: loaded at session start, changed rarely, protected by operator approval. They do not enforce (skills do that). They declare intent, making process constraints visible and auditable.

Example categories:
- **Development** -- brainstorm before building, design before plan, test before ship.
- **Knowledge** -- curate before storing, synthesise periodically.
- **Operations** -- ceremonies for rhythm, earn complexity.

The specific methods are workspace-defined. Behold prescribes the layer, not the content.

### The Backlog

`state/flow/backlog.md` is the unified queue of open work items. It is fed by retros, sessions, ad-hoc decisions, memory observations, and inbox triage.

The backlog is distinct from:
- **Checkpoint** -- a view of what's active now.
- **Logs** -- a historical record of what happened.
- **Shelf-level tracking** -- detailed story/epic breakdowns.

The backlog answers: what needs to be done that hasn't been started or finished?

### The Bootstrap File

`AGENTS.md` is the agent-agnostic entry point. It points at:
- `state/bedrock/` as the first read.
- `state/flow/checkpoint.md` as the resume point.
- `skills/` for available capabilities.
- Quick-reference commands.

Platform-specific shims are one-line pointers:
- `CLAUDE.md` -> `AGENTS.md`
- `.cursorrules` -> `AGENTS.md`
- `.github/copilot-instructions.md` -> `AGENTS.md`

### State Hygiene Rules

1. **Bedrock is protected.** Agents do not modify without operator approval.
2. **Flow is append-friendly.** Logs append. Checkpoints overwrite but carry forward unfinished items.
3. **Shelf is load-on-demand.** Do not read everything at boot.
4. **Everything is git-tracked.** State changes are commits.
5. **Staleness thresholds are explicit.**
6. **Distinguish source from derived state.** Derived state that masquerades as source state is a staleness risk. When in doubt, prefer regeneration over persistence.

| Tier | Default Staleness Threshold |
|------|----------------------------|
| Bedrock | 30 days |
| Shelf | 21 days |
| Flow (checkpoint) | 1 session |
| Flow (goals) | 14 days |
| Flow (logs) | N/A (append-only) |

### Common Patterns

**Inbox as External Input Channel.**
`state/flow/inbox/` is an external input channel for items arriving from outside the current session: autonomous agent escalations, inter-agent messages, background process outputs, operator notes left between sessions. Inbox is NOT a triage staging area for internally-generated work -- that goes directly to backlog. Session Open scans inbox; items get triaged to backlog or dismissed.

**Parked vs Active Backlog.**
Workspaces with significant idea volume may distinguish between the active work queue (`state/flow/backlog.md` -- items that will be worked on) and a parking lot (`state/shelf/parked.md` -- ideas deliberately deferred, someday/maybe items). The distinction maps to tier frequency: the backlog changes every session (flow), the parking lot changes monthly at most (shelf).

---

## 5. Ceremony Catalogue

### Required Ceremonies

Five ceremonies are required in every Behold workspace.

#### Session Open

**Trigger:** Start of every session.

**Steps:**
1. Load state (bedrock if cold start, flow always). Bedrock includes principles, identity, environment, and methods.
2. Read checkpoint.
3. Scan backlog (`state/flow/backlog.md`) for items with status `open`. Include open items in the briefing. If the workspace uses an action register (`state/flow/open-actions.md`) instead, scan that.
4. Check inbox (`state/flow/inbox/`). Triage items to backlog or dismiss.
5. Check what happened since last session.
6. Present status, propose plan.
7. Create session log.

**Output:** Agent oriented, operator briefed, open work surfaced, log started.

#### Session Close

**Trigger:** End of every session.

**Steps:**
1. Review accomplishments.
2. Invoke retro skill. If the session was trivial, note "lightweight session -- retro skipped."
3. Triage actions from retro to backlog (`state/flow/backlog.md`). Each actionable item gets an explicit status (`open`). Assign priority: now / next / later. If the workspace uses a separate action register (`state/flow/open-actions.md`), forward there instead.
4. Update checkpoint.
5. Commit state.

**Output:** Checkpoint current, actions tracked, lessons captured, clean handoff.

#### Session Resume

**Trigger:** Context loss mid-session (compression, restart, new conversation).

**Steps:**
1. Read flow state only (NOT bedrock).
2. Scan recent changes.
3. Do NOT re-propose plan.
4. Confirm position with operator.

**Output:** Agent re-synced, no repeated work.

**Key distinction:** Session Open is a cold start with full load. Session Resume is a warm restart with flow only.

#### Staleness Sweep

**Trigger:** Periodic (default every 5 sessions).

**Steps:**
1. Audit state files against freshness thresholds.
2. Classify: fresh / aging / stale.
3. Operator reviews stale items.
4. Prune expired artifacts.

**Output:** Entropy reduced, stale items surfaced.

#### Incident Response

**Trigger:** Ad-hoc, triggered by breakage.

**During:**
- Capture symptoms.
- Document attempts.
- Record resolution.

**Post:**
- Extract root cause.
- Write lesson.
- Update docs.
- Consider prevention.

**Output:** Knowledge preserved from crisis.

### Optional Ceremonies

These are not required but represent patterns that workspaces commonly evolve:

- **Health Check** -- periodic system audit.
- **Morning/Night Brief** -- autonomous background observation.
- **Context Manifest** -- record files loaded and token cost.
- **Monthly Review** -- trends, cost/benefit, roadmap.
- **Principle Review** -- question foundational beliefs.

### Ceremony Anatomy

Every ceremony follows this structure:

```yaml
name:        human-readable identifier
type:        ceremony
trigger:     what initiates it
cadence:     how often
steps:       ordered checklist
output:      what it produces
references:  which principles it serves
```

### Executable Components

Ceremony steps MAY be partially automated via executable scripts that perform observation, data gathering, or formatting. Automation reduces token cost and increases consistency. The ceremony's judgment steps (propose plan, triage, decide) remain with the agent.

The pattern: **scripts gather facts, agent applies judgment.**

Example: a `gather` script that checks system status, git history, backlog state, and memory index -- producing a structured briefing that the agent interprets rather than assembling from scratch.

Guidelines for executable ceremony components:
1. Scripts MUST be idempotent and side-effect-free (read-only observation).
2. Scripts SHOULD produce structured output (sections, labels) that the agent can parse.
3. Scripts MUST NOT make decisions, prioritise, or filter -- that is the agent's role.
4. Failed scripts MUST NOT block the ceremony; the agent falls back to manual observation.
5. The ceremony definition SHOULD document which steps are automated and which require judgment.

---

## 6. Skills and Tools

### Skills

Skills are executable knowledge -- documents that teach the agent how to do repeatable things. A skill is a document, not code.

#### Skill Anatomy

```yaml
name:        human-readable identifier
type:        ceremony | tool | workflow
trigger:     what activates it
depends:     external requirements
provenance:  why this skill exists -- what failure or friction created it
---
[Steps, instructions, output format]
```

The `provenance` field traces the skill back to its origin: a real failure, a repeated friction, or an explicit operator request. It answers "why does this exist instead of being done ad-hoc?"

Complex skills SHOULD also include a "Why This Exists" section in the body. The YAML provenance is the one-liner; the body section documents the full story -- what failure mode the skill prevents, how many times the problem occurred, and what the cost was. Skills that cannot articulate their provenance are candidates for pruning.

Every skill is:
- A directory under `skills/` containing at least a `SKILL.md`.
- Agent-agnostic.
- Self-contained.
- Discoverable.

#### Skill Directory Structure

```
skills/
  my-skill/
    SKILL.md              <- Level 1: instructions (always loaded)
    references/           <- Level 2: mechanical details (loaded on demand)
      template.md
      format-guide.md
```

**Level 1 (SKILL.md):** Orchestration logic -- what to do, in what order, what to validate. This is what the agent reads first. Keep it lean.

**Level 2 (references/):** Mechanical details -- templates, format specifications, check definitions, examples. Loaded on demand by agents or sub-agents when needed.

The rule: if removing a block from SKILL.md would not change the orchestration flow, it belongs in `references/`. Templates, exact table formats, and validation check definitions are references. Sequencing, gate criteria, and error recovery stay in SKILL.md.

Progressive disclosure keeps skills readable regardless of complexity. It benefits single-agent workspaces (humans can scan SKILL.md without wading through templates) and multi-agent workspaces (workers are dispatched with specific reference files, not the entire skill).

#### Skill Types

| Type | Purpose | Example |
|------|---------|---------|
| Ceremony | Recurring rhythm | session-open, staleness-sweep |
| Tool | Wraps external capability | fetch-url, transcribe-audio |
| Workflow | Multi-step process | brainstorm -> design -> plan, retro |

Workflow-type skills can be invoked at multiple scopes. For example, a retro skill may be invoked at session scope (by session-close), feature scope (after completing a milestone), or ad-hoc (when the operator requests reflection). The skill is the same; the scope determines what gets reflected on.

Workflow skills MAY include a `methods:` field in their frontmatter, linking the workflow to the methods it enforces. This creates an auditable chain: methods declare process constraints, workflows compose skills into sequences that honour those constraints, skills contain the hard gates. Workspaces that do not yet use methods.md can omit this field.

### Multi-Agent Skill Architecture

When a skill involves sub-agents, the main context SHOULD act as an orchestrator -- dispatching, gating, and validating -- rather than doing the work itself.

#### Roles

| Role | Reads | Writes | Decides |
|------|-------|--------|---------|
| Orchestrator (main context) | Checklists, manifests, validation reports | Agent prompts, gate decisions | Sequencing, quality gates, error recovery |
| Worker (sub-agent) | Source files from disk | Output files to disk | Content within its scoped assignment |
| Validator (sub-agent) | Output files + specs | Validation report | Pass/fail per check |

#### Rules

1. **Disk is the interface.** Workers read input from files and write output to files. The orchestrator routes by telling workers which files to read -- not by pasting content into prompts.
2. **Gate between phases.** The orchestrator validates worker output before dispatching the next phase. A gate checks: did the output land? Is it complete? Does it contradict prior phase output?
3. **Context is finite.** The orchestrator's context window is a shared resource. Delegating file reads to workers preserves it. When context approaches limits, dispatch remaining work as background agents rather than trying to recover inline.

These rules apply when workspaces use sub-agents for complex, multi-step skills. Workspaces that operate with a single agent context can ignore this subsection entirely.

### Tools

Composable executables that extend what the agent can do.

- Live in `tools/` (or `bin/`).
- stdin/stdout composable where possible.
- Get skill wrappers -- the skill teaches the agent how to use the tool.
- Documented by their skill, not a separate README.

A tool does the work. A skill teaches the agent how to use it.

```
skills/fetch-url/       <- skill (instructions)
  SKILL.md
tools/fetch             <- tool (executable)
```

---

## 7. Feedback and Self-Amendment

### The Feedback Loop

```
observe -> reflect -> extract -> amend -> observe
```

| Ceremony | Observation Type | Feeds Into |
|----------|-----------------|------------|
| Session Close | Retro (keep/stop/start) | Skills, ceremonies, goals |
| Staleness Sweep | Drift report | State hygiene |
| Incident Response | Root cause + lesson | Bedrock or shelf |
| Session Open | Integrity check | State accuracy |

### Amendment Levels

| Tier | Threshold | Process |
|------|-----------|---------|
| Flow | Agent discretion | Update freely |
| Shelf | Pattern observed twice | Agent proposes, operator approves |
| Bedrock | Repeated pattern + operator approval | Explicit decision, logged |

The more stable the tier, the more evidence required to change it.

### Action Register Lifecycle

Retro actions tend to evaporate. They are written during Session Close, noted in the log, and never revisited. The backlog lifecycle prevents this.

```
observation -> action (open) -> backlog -> active (checkpoint) -> done
```

**The pattern:**
- Session Close (via retro skill) produces actions with an explicit status (`open` or `done`).
- Triage (during Session Close) forwards actions to the backlog (`state/flow/backlog.md`), with operator review.
- Session Open scans the backlog and surfaces open items in the briefing.
- Done actions move to the Done section for audit trail, not deleted.

**Rules:**
1. Every action MUST have a status field to enable mechanical scanning.
2. Actions flow from retros to the backlog during triage -- the operator decides which to forward.
3. Session Open surfaces open actions. They do not get lost between sessions.
4. The backlog file is included in the starter kit and present from workspace bootstrap.
5. Workspaces with low action volume may keep actions inline in the checkpoint instead of a separate backlog. The lifecycle pattern is prescribed; the file structure is recommended.
6. Workspaces that prefer a separate `state/flow/open-actions.md` register may still use one. The backlog is the simpler default.

### Lessons as First-Class Artifacts

Lifecycle: observation -> lesson -> pattern -> amendment.

- Captured during Session Close, Incident Response, or ad-hoc.
- Stored in `docs/decisions/`.
- Reviewed during sweeps.
- Promoted when patterns emerge.

### The Self-Amendment Contract

Nothing in the system is sacred except the feedback loop itself. Principles can change. Ceremonies can change. Skills can change. The commitment to observe, reflect, and amend does not change.

---

## 8. Memory Architecture

Agent memory files tend to accumulate facts that duplicate authoritative sources elsewhere in the workspace. When facts change, they must be updated in multiple places -- and they will not be, because entropy is the default (P3). The memory file becomes a source of stale data masquerading as truth.

### The Principle

**Memory is an index, not a store.** If a fact has an authoritative home, point to it. If the fact has no other home, store it directly.

### Three Roles

| Role | Contains | Example |
|------|----------|---------|
| **Index** | Pointers to where truth lives | "Current priorities: see `state/flow/checkpoint.md`" |
| **Cache** | Hard-won knowledge with no other home | "Always single-quote SSH commands from this OS -- double quotes leak PATH variables" |
| **Synthesis** | Cross-pollinated connections, rationale, standing queries | "Dream finding: ceremony scripts + pinocchio timers = same gather pattern" |

The test for index vs cache: **could this fact go stale while remaining in memory?** If yes, it should be a pointer to wherever the fact gets maintained. If no (because it is a stable pattern or quirk), store it directly.

The test for synthesis: **did this knowledge exist before the agent combined its inputs?** If no -- if it is a novel connection, a design rationale, or a question that arose from juxtaposing sources -- it is synthesis. Synthesis is original intellectual product of the agent's work and compounds in value over time.

### Structure

```markdown
## Session Bridge
[Pointers to flow state -- last session, open threads reference, flags]

## Workspace Index
[Pointers to authoritative sources -- tracker, registry, configs, designs]

## Operator
[Preferences, communication style, patterns -- memory IS the authority]

## Agent Lessons
[Operational patterns learned across sessions -- memory IS the authority]

## Gotchas
[Project-specific quirks and traps -- memory IS the authority]
```

### Rules

1. **Never duplicate a tracked fact.** If the checkpoint tracks active work, do not repeat it in memory.
2. **Pointers are cheap.** One line referencing a file is better than copying its contents.
3. **Cache entries earn their place.** A gotcha must have caused a real problem at least once. Do not preemptively cache.
4. **Session bridge is minimal.** Last session reference, pointer to open threads, and flags (uncommitted work, overdue sweeps). Not a project summary.
5. **Review cache on staleness sweep.** Gotchas and lessons go stale too. Verify they are still relevant.

### Memory as Active Intelligence (Optional)

Memory can function not just as storage but as an active intelligence layer. This is optional but, when implemented, provides a different entropy resistance mechanism: not maintaining state, but growing understanding.

Components:

- **Standing questions**: persistent queries that match against future knowledge. When new information enters the system, it is tested against open questions. Answered questions are closed and their resolutions recorded.

- **Undirected synthesis**: random or semi-random pairing of memories to surface emergent connections. This is the "dream" operation -- low-cost, high-optionality. Most pairings produce nothing; occasional pairings surface structural insights invisible to directed search.

- **Corpus maintenance**: periodic review to close answered questions, remove duplicates, merge related entries, and promote recurring patterns to principles. This is the "tend" operation -- entropy resistance applied to memory itself.

- **Design rationale**: WHY decisions were made, stored as queryable entries. Future sessions facing similar decisions can recall prior reasoning rather than re-deriving it. This is the highest-value memory type per byte stored.

The pattern across all components: memory is not a log to be read but a corpus to be queried. Recalling relevant memories before design decisions is as important as reading git history before code changes.

---

## 9. The Autonomous Layer (Optional)

A background agent process that operates between human sessions. Not every workspace needs it, but Behold codifies the pattern.

### When You Need It

- The workspace manages something that changes while the operator is away.
- The operator wants to arrive already briefed.
- There are repetitive observation tasks that do not need human judgment.

### Architecture

```
GATHER -> EVALUATE -> ESCALATE
(cheap)    (cheap)    (expensive only if needed)
```

- **Gather:** collect signals. Minimal cost, no LLM needed.
- **Evaluate:** is this worth attention? Cheap model. Most signals die here.
- **Escalate:** write to `inbox/`, send notification. Expensive model only when judgment is required.

### Constraints

1. Never modify bedrock.
2. Never make irreversible changes.
3. Escalate over act. When uncertain, write to `state/flow/inbox/` and stop. The interactive agent triages inbox items to the backlog during Session Open.
4. Log everything. Every run produces an audit trail.
5. Fail silent, not loud.

### Implementation Pattern

Behold prescribes the interface, not the implementation (systemd, cron, cloud functions, etc.):

- **Trigger:** scheduled or event-driven.
- **Input:** workspace state (read-only `flow/`).
- **Output:** `inbox/` items, log entries, notifications.
- **Identity:** separate file defining the autonomous agent's role and constraints.

### Separation of Concerns

```
           OPERATOR (human)
          Decides, approves, directs
                  |
     +------------+-------------+
     |                          |
 INTERACTIVE              AUTONOMOUS
   AGENT                    AGENT
 Collaborates              Watches
 Proposes                  Triages
 Executes                  Escalates
 Full access               Read + inbox
     |                          |
     +------------+-------------+
                  |
               STATE
              (shared)
```

The interactive agent and autonomous agent share state but not identity.

---

## 10. Lineage

An infrastructure operations workspace managing physical servers evolved governance-first patterns: principles, ceremonies, activities, assets, and a self-amending feedback loop. It developed map-and-territory separation, health check ceremonies, SSH-based territory verification, and a five-document service pattern.

A development lab building CLI tools with an AI agent evolved state-first patterns: tiered persistence, composable tools, an autonomous background layer, structured memory with cross-pollination, and context-aware session management.

Both systems converged independently on the same deep patterns. Behold is the abstraction of what they share.
