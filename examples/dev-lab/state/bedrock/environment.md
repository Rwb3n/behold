# Environment

Local-only lab. No self-hosted remote services. Remote APIs used where cheap and expedient.

## Stack

- Python 3.13, Node.js 22, Go 1.24
- Git (local only)

## Directory Map

```
state/              State system (bedrock, shelf, flow)
tools/              CLI tools (standalone executables)
skills/             Skill definitions (one per tool + ceremonies)
workspace/          Project code (separate repos)
docs/plans/         Design docs and implementation plans
```

## Hooks

Ambient hook on session start — injects time, CPU, memory, disk, working directory into context.

## Useful Commands

```bash
tools/verify              # Check syntax before commits
tools/verify --all        # Check all source files
tools/grab <url>          # Universal content ingestion
tools/delegate "prompt"   # Send prompt to LLM backend
tools/videx <url>         # Video idea extraction pipeline
tools/companion status    # Autonomous layer status
tools/companion trigger   # One-shot autonomous prompt
tools/memory add          # Add to structured memory
tools/memory dream        # Undirected synthesis
```
