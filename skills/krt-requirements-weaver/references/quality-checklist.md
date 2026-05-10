# Requirements Quality Checklist

Use this checklist when reviewing requirement statements or deciding whether a requirements packet is ready for validation.

## Statement-Level Checks

Each important requirement should be:

- necessary
- appropriate to the level of abstraction
- unambiguous
- singular
- complete enough to act on
- feasible within stated constraints
- verifiable or validatable
- correct relative to its source
- written with consistent terminology

## Common Smells

Rewrite or challenge statements that contain:

- vague terms like `rapido`, `facil`, `seguro`, `adecuado`, `normal`, `etc.`
- more than one obligation joined by `y`
- no visible actor
- no trigger, condition, or context
- no measurable fit criterion where one is needed
- hidden business rules inside narrative prose
- implementation details pretending to be requirements
- negative wording when a positive measurable behavior would be clearer

## Rewrite Heuristics

- Replace adjectives with measures, thresholds, ranges, or observable outcomes.
- Split one sentence into multiple requirements when it expresses multiple obligations.
- Move rationale or explanation out of the requirement statement unless it is part of the obligation.
- When possible, make the responsible entity the grammatical subject.
- Prefer natural language that a stakeholder can still read without needing architecture knowledge.

## Set-Level Checks

The overall set should be:

- complete enough for the current phase
- internally consistent
- traceable to goals, stakeholders, sources, or higher-level needs
- bounded by visible in-scope and out-of-scope lines
- feasible as a release or increment
- prioritized when tradeoffs or sequencing matter

## Validation Gate

Treat the packet as ready for validation only when most answers are yes:

- Do we know who the primary users and approvers are?
- Do the functional requirements describe observable behavior?
- Do the non-functional requirements capture the quality risks that actually matter?
- Are business rules and constraints separated from features?
- Are acceptance criteria present for the requirements that would otherwise invite interpretation drift?
- Are assumptions and open questions visible instead of hidden?
- Could another agent plan implementation without inventing core product behavior?
