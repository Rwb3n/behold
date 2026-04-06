# Changelog

## v5 — Workspace Ownership and Extension Points

### Spec changes
- Added Section 10: Workspace Ownership (two-zone model, file ownership table, BEHOLD_VERSION marker)
- Added Section 11: Extension Points (9 validated patterns from the reference implementation)
- Renumbered Lineage from Section 10 to Section 12

### Starter changes
- Added `BEHOLD_VERSION` file containing "5"
- Updated `AGENTS.md` template with version reference

### Migration from v4
- Create a `BEHOLD_VERSION` file containing `5` in your workspace root
- Review Section 11 extension points for patterns worth adopting
- No breaking changes — existing v4 workspaces are valid v5

## v4 — Methods Layer, Memory Architecture, Autonomous Layer

### Spec changes
- Added methods.md to bedrock tier (Section 4: Methods Layer)
- Added Section 8: Memory Architecture (index/cache/synthesis, active intelligence)
- Added Section 9: The Autonomous Layer (gather/evaluate/escalate)
- Clarified checkpoint as derived state, not source of truth
- Added executable ceremony components (Section 5)
- Added multi-agent skill architecture (Section 6)

### Starter changes
- Added `state/bedrock/methods.md` to starter
- Updated ceremony skills with methods references

### Migration from v3
- Create `state/bedrock/methods.md` with workspace-specific development constraints
- Review Section 8 for memory patterns worth adopting
- No breaking changes — existing v3 workspaces are valid v4
