# Dev Lab

## Bootstrap

Read in order:

1. `state/bedrock/` — principles, identity, environment (read every session)
2. `state/flow/checkpoint.md` — what's active right now
3. `state/flow/goals.md` — session and standing goals

## State System

```
Stability tiers:
  bedrock/    rarely        read every session
  shelf/      weekly        load on demand
  flow/       every session read on resume
```

## Skills

Available skills are in `skills/`. Ceremonies:
- `begin-day` — session start (extended session-open with epic scanning)
- `end-day` — session close (extended with epic linking and action extraction)
- `resume-day` — mid-session context recovery
- `staleness-sweep` — periodic freshness audit

Tool skills (load on demand):
- Each tool in `tools/` has a matching skill in `skills/`

## Quick Reference

```bash
# Check syntax before commits
tools/verify

# Universal content ingestion
tools/grab <url>

# Delegate to LLM
tools/delegate "prompt"

# Video idea extraction
tools/videx <url>

# Background layer status
tools/companion status
```
