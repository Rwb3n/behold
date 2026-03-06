---
name: staleness-sweep
type: ceremony
trigger: periodic (every N sessions or calendar interval)
cadence: configurable (default every 5 sessions)
depends: none
references: P3 (Entropy Is the Default), P6 (Feedback Over Prescription)
provenance: required ceremony -- entropy is the default (P3); unobserved state is suspect state
---

# Staleness Sweep

Audit state file freshness, flag stale content, and prune expired artifacts.

## Staleness Thresholds

| Layer | Files | Threshold |
|-------|-------|-----------|
| Bedrock | principles.md, identity.md, environment.md | 30 days |
| Shelf | Skill files, configs | 21 days |
| Flow (goals) | goals.md | 14 days |
| Flow (checkpoint) | checkpoint.md | 1 session |
| Docs | Design docs, decision records | 21 days |

## Classification

- **Fresh:** age < 50% of threshold
- **Aging:** age between 50% and 100% of threshold
- **Stale:** age exceeds threshold

## Steps

1. **Scan each state file for last modification date**
   - Use version control history or file timestamps.
   - Calculate days since last touch for each file.

2. **Classify each file**
   - Compare age against the threshold for its layer.
   - Group into fresh, aging, and stale.

3. **Present report**
   - List stale items first (needs attention), then aging (watch list), then fresh (no action).
   - Include age, layer, and threshold for each item.

4. **Operator reviews stale items**
   For each stale item, ask:
   - Update it now?
   - Defer to next sweep?
   - Archive or drop it?
   Wait for operator input before proceeding.

5. **Prune expired artifacts**
   - Remove temporary files, old logs beyond retention period, or workspace-specific expired items.
   - Report what was pruned and how much space was recovered.

6. **Log sweep results**
   - Append summary to today's log.

7. **Commit**
   - Stage and commit any state changes from the sweep.

## Output

```
Staleness Sweep — [date]

Stale (needs attention):
- [file] — [age] days ([layer], threshold: [threshold] days)

Aging (watch list):
- [file] — [age] days ([layer], threshold: [threshold] days)

Fresh (no action):
- [file] — [age] days ([layer])

Pruned: [count] expired artifacts removed

---
Review each stale item above. Update now, defer, or drop?
```

## Notes

- The sweep is the primary defense against entropy. Do not skip it.
- If many items are stale, that's a signal — the workspace may need simpler structure or more frequent maintenance.
- The sweep itself produces feedback: if the same files are always stale, the thresholds may be wrong or the files may not be needed.
