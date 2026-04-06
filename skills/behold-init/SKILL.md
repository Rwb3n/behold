---
name: behold-init
type: ceremony
trigger: user says "behold init", "scaffold behold", "set up agent", or invokes /behold-init
cadence: once per workspace
depends: none
references: P4 (Earn Complexity)
provenance: bootstrap ceremony -- creates the minimal Behold scaffold in a new workspace
---

# Behold Init

Scaffold a Behold-class agent into any existing repo through a brief interview.

## Guard

Before starting, check for an existing scaffold:

```
if state/bedrock/ exists:
  "This workspace already has a Behold scaffold. Aborting."
  Stop.
```

## Step 1: Auto-Detect

Silently gather what you can from the workspace before asking questions:

- **Repo/directory name** — infer workspace name
- **Git user.name** — infer operator name
- **Package manifest** — read `package.json`, `Cargo.toml`, `go.mod`, `pyproject.toml`, `composer.json`, or equivalent to detect tech stack
- **Existing CLAUDE.md** — note whether one exists (will prepend shim, not overwrite)
- **Existing README.md** — read for project context
- **Recent git log** — understand what the project does

Do not present findings yet. Use them as defaults in the interview.

## Step 2: Interview

Ask these questions **one at a time**. Offer your auto-detected value as the default where possible.

### Q1: Workspace Name

> What should this workspace be called?
>
> I see the repo is named `{repo_name}`. Want to use that, or something else?

### Q2: Agent Role

> What does the agent in this workspace do?
>
> Examples: "builds the Concierge app", "maintains infrastructure docs", "develops a trading bot"

### Q3: Operator Name

> Who is the operator (the human)?
>
> Git config says `{git_user_name}`. Use that?

### Q4: Tech Stack

> What's the tech stack or key context the agent should know about?
>
> I detected: `{detected_stack}`. Anything to add or correct?

## Step 3: Generate

Create all files below. Use interview answers to fill in templates. Do not create files that already exist (except CLAUDE.md — prepend shim line only).

### Entry Points

**`AGENTS.md`:**

```markdown
# {workspace_name}

## Bootstrap

Read in order:

1. `state/bedrock/` — principles, identity, environment, methods (read every session)
2. `state/flow/checkpoint.md` — current position (read on resume)
3. `state/flow/goals.md` — standing and short-term goals
4. `CLAUDE.md` — codebase guide, conventions, gotchas

## State System

\```
Stability tiers (how often it changes):
  bedrock/    rarely        read every session
  shelf/      weekly        load on demand
  flow/       every session read on resume
\```

## Skills

Available skills are in `skills/`. Each directory contains a SKILL.md with trigger conditions, steps, and expected output.

## Quick Reference

[Fill in workspace-specific commands, paths, and conventions]
```

**`CLAUDE.md`** — if one exists, prepend this line at the top:

```
Read [`AGENTS.md`](AGENTS.md) for your full identity, boot sequence, and state system.
```

If no CLAUDE.md exists, create one with just:

```markdown
# CLAUDE.md

Read [`AGENTS.md`](AGENTS.md) for all workspace instructions.
```

### Bedrock

**`state/bedrock/identity.md`:**

```markdown
# Identity

## What This Workspace Is

{one paragraph from interview — what the workspace manages, builds, or operates}

## Actors

### The Operator ({operator_name})

Decision authority. Owns architectural direction, deployment approvals, and scope changes.

### The Agent

{agent_role_from_interview}

**Roles:**
- [Fill in 2-3 specific roles based on the agent's purpose]

## Boundaries

### Agent Owns
- [Fill in based on agent role]

### Operator Owns
- All decision authority
- [Fill in based on context]
```

**`state/bedrock/environment.md`:**

```markdown
# Environment

## Stack

{tech_stack_from_interview}

## Directory Map

[Fill in key paths and what lives where]

## Useful Commands

[Fill in common commands the agent should know]
```

**`state/bedrock/principles.md`** — Behold defaults verbatim (P1-P7). Copy from `behold/starter/state/bedrock/principles.md`.

**`state/bedrock/methods.md`:**

```markdown
# Methods

*How we work -- named process constraints. Principles say WHY; methods say HOW WE WORK.*

## Development

- [Add methods as patterns stabilise.]

## Operations

- Ceremonies for rhythm -- session lifecycle is managed, not ad-hoc.
- Earn complexity -- add structure when its absence causes pain, not before.
```

### Flow

**`state/flow/checkpoint.md`:**

```markdown
# Checkpoint

Last updated: {today}

## Active

[To be filled at first session]

## Next

[To be filled at first session]

## Later

[To be filled at first session]
```

**`state/flow/goals.md`:**

```markdown
# Goals

## This Week

- [To be filled at first session]

## Standing

- [To be filled at first session]
```

**`state/flow/backlog.md`:**

```markdown
# Backlog

*Unified queue of open work items. Fed by retros, sessions, inbox triage.*

## Open

| # | Item | Source | Priority | Status |
|---|------|--------|----------|--------|

## Done

*Completed items. Audit trail, not active work.*
```

**`state/flow/inbox/.gitkeep`** — empty
**`state/flow/log/.gitkeep`** — empty

### Shelf

**`state/shelf/.gitkeep`** — empty placeholder

### Skills

Copy these 3 ceremony skills verbatim from the Behold starter kit:

**`skills/session-open/SKILL.md`** — from `behold/starter/skills/session-open/SKILL.md`
**`skills/session-close/SKILL.md`** — from `behold/starter/skills/session-close/SKILL.md`
**`skills/session-resume/SKILL.md`** — from `behold/starter/skills/session-resume/SKILL.md`

## Step 4: Present Summary

Show the operator what was generated:

```
Behold scaffold created for "{workspace_name}":

Entry points:  AGENTS.md, CLAUDE.md (shim)
Bedrock:       identity.md, environment.md, principles.md, methods.md
Flow:          checkpoint.md, goals.md, backlog.md, inbox/, log/
Skills:        session-open, session-close, session-resume
Shelf:         placeholder (.gitkeep)

{count} files created. Review and approve to commit?
```

## Step 5: Commit

On approval:

```bash
git add AGENTS.md CLAUDE.md state/ skills/
git commit -m "feat: scaffold Behold agent state system"
```

## Wrap Mode

For existing codebases that want Behold structure without reorganization.

**Trigger:** user says "behold init --wrap", "wrap this repo", or the workspace has significant existing code.

**Guard change:** Instead of aborting when `state/bedrock/` exists, abort only when `state/bedrock/principles.md` exists (a wrapped repo may have a `state/` directory for other purposes).

**Differences from standard init:**

1. **Does NOT move existing files** into `state/`. The Behold scaffold sits alongside the existing project structure.
2. **Does NOT modify** `src/`, `lib/`, `app/`, or any existing code directories.
3. **Prepends shim** to existing `CLAUDE.md` / `.cursorrules` / `copilot-instructions.md` (same as standard).
4. **Creates `AGENTS.md`** or updates existing with bootstrap section.
5. **Interview includes:** "What existing directories should the agent know about?" — answer populates `environment.md`.

Everything else is identical to standard init. The scaffold is additive — it creates `state/`, `skills/`, and entry points without touching the existing project layout.

**When to use wrap vs standard:**
- **Standard:** New workspace, greenfield, or repo with no existing conventions.
- **Wrap:** Existing codebase with established structure. The team wants ceremony and continuity without reorganizing their project.

## Notes

- **Minimal scaffold per P4.** Only 3 ceremony skills. Retro, staleness-sweep, incident-response are earned when needed.
- **Principles are Behold defaults.** The operator amends them later if needed. Do not customize during init.
- **Identity and environment are drafts.** The agent should refine them in its first session as it learns the workspace. Good enough > perfect.
- **Never overwrite.** If a file already exists (other than CLAUDE.md shim prepend), skip it and note it in the summary.
- **BEHOLD_VERSION.** Init creates a `BEHOLD_VERSION` file containing the current spec version. See Section 10 of the spec.
