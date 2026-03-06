---
name: incident-response
type: ceremony
trigger: breakage, outage, significant malfunction, or unexpected behavior
cadence: ad-hoc
depends: none
references: P2 (Observe Before You Act), P5 (Map and Territory), P6 (Feedback Over Prescription)
provenance: required ceremony -- crisis knowledge evaporates fastest; structured capture preserves it (P2, P6)
---

# Incident Response

Structured response to breakage. Capture knowledge during the crisis, not after it fades.

## During the Incident

1. **Note start time**
   - Record when the incident was detected.

2. **Capture symptoms before fixing**
   - What's broken? What's the observable behavior?
   - What was expected instead?
   - Document the state as-is before changing anything.
   - Copy error messages, logs, and relevant output verbatim.

3. **Document what you try**
   - Record every attempt — including failures.
   - Failed approaches are valuable: they narrow the problem space.
   - Format: what was tried, what happened, what was learned.

4. **Record resolution**
   - What fixed it? Note the exact change.
   - Note the resolution time.

## Post-Incident

5. **Extract root cause**
   - Why did this happen? Go beyond the immediate fix.
   - Distinguish between the trigger (what caused it this time) and the root cause (why it was possible at all).

6. **Write lesson**
   - Add to `docs/decisions/` or workspace equivalent.
   - Include: what happened, root cause, fix, prevention.

7. **Update documentation**
   - If the incident revealed gaps in existing docs, fix them now.
   - If a new troubleshooting pattern was discovered, document it.

8. **Consider prevention**
   - Could this have been prevented?
   - If yes: propose a skill change, ceremony addition, or monitoring improvement.
   - If no: document why, so the same analysis doesn't repeat next time.

## Output

```
Incident Report — [date]

Detected: [time]
Resolved: [time]
Duration: [elapsed]

Symptoms:
- [what was observed]

Timeline:
- [time] [what was tried] — [result]

Root cause: [why it happened]
Fix: [what resolved it]

Lesson: [what was learned]
Prevention: [proposed change, or "not preventable — documented"]
```

## Notes

- Speed of resolution matters, but not at the expense of documentation. Capture symptoms BEFORE fixing — you won't remember the exact error message later.
- Failed attempts are not wasted. They're negative results that help future incidents.
- Every incident is a feedback opportunity. If the same class of incident happens twice, the prevention step failed — escalate to a ceremony or principle change.
