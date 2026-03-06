# Example: Development Lab

A Behold workspace for building composable CLI tools with an AI agent. Features an autonomous background layer that watches, triages, and escalates between sessions.

## What This Demonstrates

- **Bedrock/shelf/flow tiering in practice:** Principles and identity rarely change, skills evolve weekly, checkpoint and logs change every session.
- **Composable tool building:** Each tool is a standalone CLI, stdin/stdout composable, with a skill wrapper teaching the agent how to use it.
- **Autonomous background layer:** A background process runs on timers — gathering signals, evaluating relevance, escalating to the operator's inbox when needed. Follows the GATHER -> EVALUATE -> ESCALATE pipeline.
- **Structured memory:** A memory system that accumulates ideas, questions, and syntheses with cross-pollination at ingestion time and directed synthesis ("dreaming") at retrieval time.
- **Epic lifecycle tracking:** Work items flow through investigate -> decide -> build -> protect stages with explicit status tracking.
- **Session counting and staleness triggers:** Every 5 sessions, a staleness sweep is triggered automatically.

## Workspace Structure

This example shows only the Behold state layer. The full workspace would also contain tool source code, tests, and documentation.

## Key Adaptation

The default Behold principles were replaced with domain-specific ones focused on pragmatic building:
- Function over art (will this change behavior?)
- Economy before building (can existing tools do this?)
- Bugs get tests (regression tests on every fix)
