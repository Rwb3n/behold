# Spike-vs-Commit Thinking

Decide whether to prototype first to learn, or build directly for keeps. Spikes reduce risk when the problem is unclear; committed builds avoid throwaway work when the path is known.

## When to use
- Uncertainty about whether an approach will work
- Using an unfamiliar API, library, or technique for the first time
- The scope is clear enough that prototyping might be wasted effort

## Guiding questions
1. How well do I understand the problem? Can I describe the solution before writing code?
2. What is the biggest technical risk — and can a 30-minute spike resolve it?
3. If I spike, what specific question will the spike answer?
4. Is the cost of rework (building wrong then fixing) higher than the cost of spiking first?
5. Can I structure the committed build so the risky part is isolated and replaceable?

## Output structure
- Uncertainty inventory (what is unknown)
- Spike definition (if spiking: time-box, specific question to answer, exit criteria)
- Commit plan (if committing: structure that isolates risk)
- Decision with rationale
