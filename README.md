# Behold

*"Structure for systems that remember."*

AI agents are stateless. Systems drift. Sessions start from zero. Behold solves this with three layers: **continuity** (persistent, tiered state that survives every session boundary), **entropy resistance** (ceremonies that force observation before action), and **collaboration structure** (defined actors with explicit feedback loops). The result is a workspace where humans and AI agents build on what came before instead of rebuilding from scratch.

---

## What Behold Is

- A **specification** for workspace architecture.
- An opinionated set of **patterns**, not a software library.
- Language-agnostic, platform-agnostic, agent-agnostic.
- Designed for one human + one or more AI agents.

## What Behold Is Not

- Something you `npm install`.
- Tied to any specific AI model or platform.
- An agent framework (no routing, orchestration, or message passing).
- A project management methodology.

---

## Core Concepts

**Workspace** -- A project directory structured according to the Behold specification. The unit of continuity.

**Actors** -- The participants in a workspace. Typically one human (the operator) and one or more AI agents (stewards). Each has a defined role and boundaries.

**State** -- Persistent knowledge, organized in three tiers by how often it changes:
- **Bedrock** -- Principles, identity, environment. Rarely changes. Read every session.
- **Shelf** -- Skills, configs, reference docs. Changes weekly. Loaded on demand.
- **Flow** -- Checkpoint, goals, logs, inbox. Changes every session. Read on resume.

**Rhythm** -- Ceremonies that structure how work happens. Session open, session close, periodic reviews. These force observation and prevent drift.

**Feedback** -- The system amends itself. Retros produce lessons; lessons update shelf state; shelf state changes future behavior. The workspace gets better over time.

---

## Quick Start

1. Clone or copy `starter/` into your project.
2. Copy the appropriate shim to your project root (e.g., `shims/CLAUDE.md` to `./CLAUDE.md`).
3. Fill in `state/bedrock/identity.md` -- who the agent is, what the project is.
4. Fill in `state/bedrock/environment.md` -- infrastructure, tooling, access.
5. Edit `state/bedrock/principles.md` -- adopt, adapt, or replace the defaults.
6. Start a session. The agent reads the bootstrap file, loads bedrock, and you are running.

---

## Repo Structure

```
behold/
  README.md
  SPEC.md
  starter/              # Clone this to start a workspace
    AGENTS.md
    shims/
    state/
      bedrock/
      shelf/
      flow/
    skills/
    tools/
    docs/
  examples/
    infrastructure-ops/
    dev-lab/
```

---

## Links

- Full specification: [`SPEC.md`](SPEC.md)
- Examples: [`examples/`](examples/)

---

## License

MIT
