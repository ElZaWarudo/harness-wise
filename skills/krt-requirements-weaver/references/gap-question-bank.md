# Gap Question Bank

Use this reference when the requirements source is incomplete, vague, or contradictory and the next best move is to ask a clarification question.

Ask one question at a time. Prefer the smallest question that unlocks the biggest reduction in ambiguity.

## Priority Rule

Ask first about the gap that most changes:

1. scope
2. core behavior
3. acceptance or validation
4. constraints, integrations, or quality attributes
5. lower-risk detail

## Gap Types And Example Questions

### Problem And Outcome Gap

Use when the request says what to build but not what problem it solves.

- What problem is this feature supposed to solve for the user or business?
- What changes for the user if this works correctly?
- How do people handle this today, and what is wrong with that workaround?

### User And Stakeholder Gap

Use when the actor is vague or there may be more than one approver or user type.

- Who is the primary user of this feature?
- Who decides whether this behavior is correct: end user, client, admin, teacher, or another role?
- Are there different user types that need different permissions or flows?

### Scope Boundary Gap

Use when the request suggests a capability but not what is intentionally excluded.

- What is definitely in scope for this first version?
- What should we explicitly leave out for now?
- Is this meant to solve the full process or only one part of it?

### Behavior Gap

Use when the system action is named but the flow is underspecified.

- What should happen step by step when the user performs this action?
- What input does the user provide, and what output should they receive?
- What should happen after the main action succeeds?

### Edge Case Gap

Use when the happy path is clear but failure or exception paths are not.

- What should happen if the data is invalid, missing, duplicated, or incomplete?
- Are there situations where the system should reject the action?
- What should the user see when something goes wrong?

### Business Rule Gap

Use when policies, conditions, or invariants are implied but not stated.

- Are there rules that always have to be enforced here?
- Are there limits, approvals, uniqueness rules, or eligibility conditions?
- Does this behavior depend on user role, status, date, or another business condition?

### Data Gap

Use when entities or fields are implied but unclear.

- What information needs to be captured, stored, or shown?
- Which fields are required and which are optional?
- Does any value need to be unique, validated, or derived?

### Integration Gap

Use when the requirement touches external systems, notifications, or imported data.

- Does this feature connect to another system, API, service, or database?
- What information must be sent or received from that external dependency?
- What should happen if the external system is unavailable?

### Non-Functional Gap

Use when quality expectations are hinted at but not specified.

- Are there expectations for security, speed, reliability, privacy, or accessibility?
- Is there any limit on response time, volume, concurrency, or data retention?
- Are there legal, institutional, or platform constraints we must respect?

### Acceptance Gap

Use when the requirement exists but there is no visible finish line.

- How will we know this requirement is satisfied?
- Can you give one valid example and one invalid example?
- What result would make you say "yes, this is correct"?

## Output Discipline

- Keep asked questions visible in the artifact when they remain unanswered.
- When a question is answered, capture both the answer and the gap it resolved.
- If the user cannot answer immediately, keep the issue as an open question instead of turning it into a fabricated requirement.
