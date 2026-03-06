# Infrastructure Operations

## Bootstrap

Read in order:

1. `state/bedrock/` — principles, identity, environment (read every session)
2. `state/flow/checkpoint.md` — current position (read on resume)
3. `state/flow/goals.md` — standing and short-term goals

## State System

```
bedrock/    rarely        read every session
shelf/      weekly        load on demand
flow/       every session read on resume
```

## Skills

Available skills are in `skills/`. Key ceremonies:
- `session-open` — briefing and orientation
- `session-close` — retro and checkpoint update
- `health-check` — weekly infrastructure audit (custom)

## Quick Reference

- SSH to host: `ssh admin@host`
- Check guest status: `ssh admin@host 'guest-status'`
- Service docs: `services/<name>/README.md`
