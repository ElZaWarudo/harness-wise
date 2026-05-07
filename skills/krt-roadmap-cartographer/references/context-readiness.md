# Context Readiness

Use this reference before deciding whether to generate a roadmap.

## Minimum Context

Roadmap generation is safe only when these categories are sufficiently covered:

1. Product intent: target problem, users/personas, outcomes, success criteria, non-goals.
2. Current system shape: major modules/services, core flows, integration boundaries.
3. Technical execution context: stack, package managers, run/test/build commands, conventions.
4. Data/interface context when applicable: schemas, migrations, APIs/events, auth/permissions.
5. Delivery context: branch/release conventions, CI expectations, deployment constraints, tracker conventions.
6. Existing scope context: backlog/roadmap/known gaps or enough specs to identify missing work without inventing direction.

## Sufficiency Rules

- A category is sufficient when the roadmap can make bounded, source-backed decisions without inventing product behavior or execution constraints.
- Missing context is blocking when it would change roadmap items, dependency order, branch/PR strategy, or product scope.
- Existing docs may be enough even when they are imperfect, but label weak areas with confidence and risks.
- If only one focused user decision is missing and the rest of the context is strong, ask that question before deciding.
- If multiple minimum-context categories are missing, write a readiness report instead of asking a long question list.

## Source Confidence

Use confidence labels in roadmap source inventory:

- **High:** current source file, current project doc, accepted plan, or explicit user decision.
- **Medium:** older project doc that still matches current code, inferred pattern from multiple nearby examples, or user-provided context that has not been verified.
- **Low:** stale doc, single weak signal, inferred direction, or unverified assumption.

Low-confidence items may appear as risks or user decisions, but they should not become roadmap commitments unless the roadmap clearly marks them as assumptions to confirm during brainstorm.
