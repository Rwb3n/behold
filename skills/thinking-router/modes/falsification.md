# Falsification Thinking

Surface what could contradict your current conclusion — then check. The active counterpart to Epistemic: where Epistemic maps the boundary of knowledge, Falsification crosses it by identifying testable assumptions and available-but-unchecked data sources.

## When to use
- About to commit to a conclusion, design, or recommendation
- An investigation feels "done" but hasn't been stress-tested
- Working with partial data and treating assumptions as facts
- After a finding surprises you — what else might be wrong?
- Designing an instrument or system that depends on external data — what sources were dismissed without checking?

## The problem this solves

Conclusions accumulate assumptions silently. "Alibaba has no viable API" becomes accepted after one investigator reports it. "Review count is dead" becomes permanent after one data source confirms it. Each unchecked assumption narrows the solution space. Falsification reverses the direction: instead of building on what you believe, it asks what would demolish what you believe — and whether the demolition evidence is accessible.

LLMs are especially vulnerable here. We generate coherent narratives from partial evidence and treat our own confidence as signal. Falsification is the circuit breaker.

## Guiding questions

1. **What am I concluding?** State the belief, finding, or design decision explicitly. If you can't state it as a falsifiable claim, it's not ready to test.

2. **What assumptions does this conclusion rest on?** List them. Each assumption is a potential failure point. Common hidden assumptions:
   - "This data source doesn't exist" (checked how?)
   - "This signal is reliable" (validated against what?)
   - "This cost is fixed" (for how long? under what conditions?)
   - "These are the only options" (who said so?)

3. **For each assumption: what data would contradict it?** Not "could someone disagree" — what specific, observable evidence would prove the assumption wrong?

4. **Does that contradicting data exist and is it accessible?** This is the key move. Don't just imagine what could disprove you — check whether the disproof is sitting in an API, a database, a document, or a conversation you haven't had. The gap between "unknown" and "unchecked" is where value hides.

5. **What's the cost of being wrong here?** Not all assumptions are equal. A wrong assumption about import duty swings margin by £0.80/unit. A wrong assumption about listing quality might not matter at all. Prioritise checking assumptions by the cost of being wrong about them.

## Anti-patterns

- **Don't falsify for completeness.** The goal is not to list every possible objection. It's to find the 1-2 assumptions that, if wrong, would change your decision. Focus on decision-relevant falsification.
- **Don't confuse skepticism with falsification.** Skepticism says "I doubt this." Falsification says "here's what would prove me wrong, and I'm going to look." One is a posture, the other is an action.
- **Don't stop at the list.** Identifying unchecked assumptions without checking them is Epistemic mode. Falsification means you go look — or explicitly decide not to and record why.

## Output structure
- Conclusion stated as falsifiable claim
- Assumptions enumerated (with confidence: high/medium/low)
- Contradicting evidence identified (what would disprove each)
- Data availability check (exists / accessible / checked / unchecked)
- Cost-of-wrong ranking (which assumptions matter most)
- Action: what to check next, or explicit decision to accept the risk
