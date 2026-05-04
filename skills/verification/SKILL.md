---
type: ceremony
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
limits:
  reads: []
  writes: []
  forbidden_writes: []
---

# Verification Before Completion

## Gate

| Field | Value |
|-------|-------|
| event | Before claiming work is complete, fixed, or passing |
| mandatory | yes |
| scope | method |
| user signals | "done", "fixed", "tests pass", "all good", about to commit or create a PR |

## Steps

```
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, not verifying
```

## Exit

exit: resume → evidence confirms or denies the claim. Conditions that must hold before resuming:
- Verification command run in this message (not a prior run)
- Output read completely, exit code checked
- Claim matches actual output

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you haven't run the verification command in this message, you cannot claim it passes.

## Common Failures

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test command output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check, extrapolation |
| Build succeeds | Build command: exit 0 | Linter passing, logs look good |
| Bug fixed | Test original symptom: passes | Code changed, assumed fixed |
| Regression test works | Red-green cycle verified | Test passes once |
| Agent completed | VCS diff shows changes | Agent reports "success" |
| Requirements met | Line-by-line checklist | Tests passing |

## Self-Deception Classes

### Class I — Scope narrowing

Convenient framing makes a problem smaller than it is. "My session's files" when the residue spans weeks. "The edits I made" when the consumers were never checked.

**Check:** name the excluded set in one sentence. Is the exclusion load-bearing for the claim? If removing the exclusion would change the verdict, the scope is dishonest.

### Class II — Verifying vs reporting

Trusting the intermediate log instead of the actual output. Grepping the committed string instead of rendering the page. Reading the build log instead of running the smoke test.

**Check:** paste the raw external evidence — the HTTP response, the screenshot, the post-action state — not the command you ran or the log it produced.

### Class III — Consumer blast radius

Shipping a change without tracing its effect on callers. Schema change without grep. API rename without cascade.

**Check:** run `grep -rln <changed-symbol>` across the project before claiming the change is landed. List the hits. Zero hits means the surface is unused or the grep was wrong — both are real answers.

### Class IV — Router mode theater

Invoking a thinking/judgment/engineering mode that does not fit the current problem, then performing it anyway for completeness.

**Check:** for every router mode used, state the base case in one sentence. If it's a stretch, the mode's conclusions are theater and should not support a claim of done.

### Class V — Confirmatory-only validation

Running an experiment against a positive-case population, observing the design fits, writing a verdict before any adversarial case has run.

**Check:** before writing any verdict, name the negative-control population or breaking exemplar, and the observed result of running the design against it. If either is missing, the verdict is unverified.

### Class VI — Post-verdict artifact work crowding out the action gate

After a verdict lands naming an action gate, artifact work continues. Each piece is defensible in isolation. The pattern only shows at EOD: gate unmoved, session ended.

**Check:** before starting non-gate work after a verdict, name: (a) the action gate verbatim; (b) a time-box on artifact work. At expiry, either the gate has moved or artifact work stops.

### Class VII — Cross-function seam bugs

Edits touching multiple locations create dependencies local reasoning misses. Each edit looks correct alone. Bugs live in the seams.

**Check:** before committing, read the full `git diff` as a connected whole. For each modified function, trace shared variables, state, and return shapes to every other changed function.

## Red Flags - STOP

- Using "should", "probably", "seems to"
- Expressing satisfaction before verification
- About to commit/push/PR without verification
- Trusting agent success reports
- Relying on partial verification
- ANY wording implying success without having run verification

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Linter passed" | Linter ≠ compiler |
| "Agent said success" | Verify independently |
| "Partial check is enough" | Partial proves nothing |

## The Bottom Line

**No shortcuts for verification.**

Run the command. Read the output. THEN claim the result.

This is non-negotiable.
