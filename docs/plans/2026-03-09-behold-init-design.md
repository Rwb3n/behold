# behold-init Skill Design

**Status:** approved
**Date:** 2026-03-09

## Summary

Interactive skill that scaffolds a Behold-class agent into any existing repo. Brief interview (4 questions), then generates a minimal scaffold, presents for approval, commits.

## Trigger

User says "behold init", "scaffold behold", "set up agent", or invokes `/behold-init`.

## Interview (one question at a time)

1. **Workspace name** — "What should this workspace be called?" (default: infer from repo/directory name)
2. **Agent role** — "What does the agent in this workspace do?"
3. **Operator name** — "Who is the operator?" (default: infer from git config)
4. **Tech stack / key context** — "What's the tech stack or key context?" (auto-detect from package.json, Cargo.toml, etc.; operator confirms or corrects)

## Output (minimal viable scaffold)

| File | Source | Notes |
|------|--------|-------|
| `AGENTS.md` | Generated from interview | Boot sequence entry point |
| `CLAUDE.md` update | Prepend shim line | Only if CLAUDE.md exists; create shim if not |
| `state/bedrock/identity.md` | Generated from interview | Workspace purpose, actors, boundaries |
| `state/bedrock/environment.md` | Generated from auto-detect + interview | Stack, directory map, commands |
| `state/bedrock/principles.md` | Behold defaults verbatim | P1-P7 |
| `state/bedrock/methods.md` | Skeleton + 1-2 contextual methods | From interview context |
| `state/flow/checkpoint.md` | Empty template | |
| `state/flow/goals.md` | Empty template | |
| `state/flow/backlog.md` | Empty template | |
| `state/flow/inbox/.gitkeep` | Empty | |
| `state/flow/log/.gitkeep` | Empty | |
| `state/shelf/.gitkeep` | Empty | |
| `skills/session-open/SKILL.md` | From Behold starter kit | |
| `skills/session-close/SKILL.md` | From Behold starter kit | |
| `skills/session-resume/SKILL.md` | From Behold starter kit | |

## Process Flow

1. Check for existing scaffold (`state/bedrock/` exists → abort with message)
2. Auto-detect: repo name, git user.name, package.json / Cargo.toml / go.mod / pyproject.toml
3. Interview: 4 questions, one at a time, defaults from auto-detect
4. Generate all files from interview answers
5. Present summary for approval
6. On approval: create files, commit

## Design Decisions

- **Minimal scaffold per P4.** Only 3 ceremony skills (open, close, resume). Retro, staleness-sweep, incident-response earned later.
- **Interview over inference.** Brief interview (brainstorm-style) is more reliable than pure auto-detection and gives the operator control.
- **Skill lives in Behold repo.** Natural home, framework-specific, keeps Behold self-contained.
- **Principles are verbatim.** Not customized during init. The operator amends them later if needed.
