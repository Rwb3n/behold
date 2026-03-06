---
name: session-open
type: ceremony
trigger: starting a work session
cadence: every session
depends: none
references: P1 (Continuity Over Capability), P2 (Observe Before You Act)
provenance: required ceremony -- session continuity is the foundation of the framework (P1)
---

# Session Open

Orient to current state, brief the operator, and establish session intent.

## Steps

1. **Load bedrock** (if cold start or first session)
   - Read `state/bedrock/principles.md`
   - Read `state/bedrock/identity.md`
   - Read `state/bedrock/environment.md`
   - Skip this step on warm starts where bedrock is already loaded.

2. **Read checkpoint**
   - Read `state/flow/checkpoint.md`
   - Note what's active, what's next, what's later.

3. **Read today's log** (if it exists)
   - Check `state/flow/log/` for today's date.
   - If a log exists, review to understand what's already happened today.

4. **Check inbox**
   - List items in `state/flow/inbox/`.
   - Note anything awaiting operator attention.

5. **Scan action register**
   - If `state/flow/open-actions.md` exists, scan for items with status `open`.
   - Include open actions in the status briefing.
   - If the register does not exist, skip this step.

6. **Check what happened since last session**
   - Review recent version control history.
   - If an autonomous layer is running, check its logs for activity and escalations.

7. **Quick integrity check**
   - Scan for obvious drift: do key files still exist? Do references still resolve?
   - This is a fast fingerprint, not a full staleness sweep.
   - Flag findings — don't fix them yet.

8. **Present status to operator**
   Report concisely:
   - Where we left off (last session summary)
   - Current priorities (from checkpoint)
   - Anything that needs attention (inbox, drift, stale items)
   - Suggested focus for this session

9. **Wait for operator direction**
   - The operator confirms, redirects, or adds context.
   - Do not assume priorities are unchanged.

10. **Create or append to today's log**
    - File: `state/flow/log/YYYY-MM-DD.md`
    - Add a session start entry with timestamp.
    - Record session intent once the operator states it.

## Output

```
Session [N] start — [date] [time]

Active: [from checkpoint]
Inbox: [count or "empty"]
Open actions: [count or "none" or "no register"]
Recent: [summary of changes since last session]

Priorities:
- [from checkpoint, re-evaluated]

Suggested focus: [what to work on this session]
```

## Notes

- If this is the first session of the week, mention that a periodic review may be due.
- If the staleness sweep counter has reached its threshold, note that a sweep is due.
- Lead with the briefing, not with questions. The operator wants to know the state of things before deciding what to do.
