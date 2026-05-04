# Investigative Thinking

Navigate a data substrate to surface non-obvious patterns. Move between filtering, traversal, enrichment, and pattern matching. The value is in the sequence of moves, not any single query.

## When to use
- Exploring a dataset for patterns, anomalies, or opportunities
- Building an investigation chain from a starting hypothesis
- Deciding what to query next given what you've already found
- Designing a new playbook (reusable investigation pattern)

## Moves

These are the atomic operations in a data investigation. Chain them.

| Move | What | When |
|------|------|------|
| Filter | Narrow the universe by criteria | Start here — reduce 5M to hundreds |
| Traverse | Follow connections between entities | When you have a specific entity to explore |
| Cluster | Group by shared attribute (address, person, SIC, postcode) | When looking for hidden connections |
| Enrich | Pull additional data for specific entities | When local data is insufficient for a decision |
| Timeline | Order events chronologically for an entity | When sequence matters (incorporation → filing → distress) |
| Match | Find supply/demand, similarity, or contrast between two sets | When you have candidates and want counterparties |
| Anomaly | Look for statistical outliers in a field | When the interesting thing is what's unusual |

## Guiding questions
1. What is the starting hypothesis? What would confirm or refute it?
2. Which move reduces uncertainty the most with the least cost?
3. What did the last result reveal — does it suggest a new direction or confirm the current one?
4. Am I going broad (more candidates) or deep (more detail on fewer)? Which is right for this stage?
5. Is there a reusable pattern here — could this investigation become a playbook?

## Investigation shapes

Common multi-move patterns:

**Funnel:** Filter → Filter → Filter → Enrich → Decide
Use when: universe is large, you need to narrow to actionable set

**Spider:** Entity → Traverse → Traverse → Cluster
Use when: starting from one entity, want to map its network

**Matchmaker:** Filter(supply) → Filter(demand) → Match by proximity
Use when: looking for counterparty opportunities (buyer/seller, acquirer/target)

**Watchdog:** Filter(baseline) → Timeline → Anomaly → Escalate
Use when: monitoring for changes that signal opportunity or risk

**Archaeologist:** Entity → Timeline → Enrich → Enrich → Reconstruct
Use when: investigating a specific entity's history and relationships

## Output structure
- Starting hypothesis
- Investigation chain (moves taken, in order, with results at each step)
- Pattern identified (or null result — also valuable)
- Playbook candidate? (yes/no — is this worth saving for replay)
