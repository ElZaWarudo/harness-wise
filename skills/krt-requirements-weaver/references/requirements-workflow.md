# Requirements Workflow

Use this workflow to move from a rough brief to a validated requirements packet without jumping into solution design too early.

## 1. Reception And Analysis

Capture the minimum frame first:

- source artifact or conversation
- business or user problem
- primary stakeholder
- target users
- success outcome
- known scope
- known constraints
- unknowns and contradictions

Answer these questions as early as possible:

- What problem are we solving?
- Who will use or approve the system?
- What must the system do?
- What constraints already exist?
- What is unclear, missing, or contradictory?

If the input mixes requirements with solution ideas, split them:

- keep the need as a requirement candidate
- keep the proposed solution as a suggestion or constraint only if the source truly mandates it

## 2. Elicitation And Refinement

Move from vague intention to concrete, reviewable statements.

### Refinement moves

- turn generic goals into observable behavior
- split compound requirements into single obligations
- make conditions explicit
- surface business rules hidden inside prose
- attach measurable acceptance criteria when the requirement will later be tested
- convert implied exclusions into explicit out-of-scope notes

### Choose the lightest useful artifact

- Use **functional requirements** for capabilities the system must provide.
- Use **non-functional requirements** for quality attributes and constraints such as performance, security, privacy, reliability, compliance, accessibility, and usability.
- Use **user stories** when stakeholder value and user perspective are the clearest framing.
- Use **use cases** when the interaction flow, alternate paths, or actor handoffs matter.
- Use **business rules** when a policy or invariant applies across multiple functions.
- Use **acceptance criteria** when implementation or testing will need an unambiguous finish line.

### Refinement example

Initial statement:

`El sistema debe permitir registrar usuarios.`

Refined result:

- The user shall be able to register with email and password.
- The system shall reject an email address that already exists.
- The password shall contain at least 8 characters.
- When registration succeeds, the system shall confirm that the account was created.
- Acceptance criteria:
  - Given a new email and a valid password, when the user submits the form, then the account is created.
  - Given an existing email, when the user submits the form, then the system shows that the email is already in use.
  - Given a password shorter than 8 characters, when the user submits the form, then the system rejects the registration.

## 3. Validation

Validate before planning or coding. The point is not only to improve wording, but to confirm that the team understood the right thing.

Run a final stakeholder-facing confirmation:

`Esto es lo que vamos a construir. Esto es lo que queda fuera. Estas son las dudas o supuestos pendientes.`

Check:

- Does each major requirement map to a stakeholder need, rule, or constraint?
- Can a designer, developer, or tester act without guessing hidden behavior?
- Are conflicts between stakeholders or rules called out explicitly?
- Are acceptance criteria present where ambiguity would otherwise survive?
- Is the scope boundary visible?

## 4. Default Deliverable

Unless the user asks for a different artifact, produce a compact packet with:

1. Problem and goal
2. Stakeholders and users
3. Scope in
4. Scope out
5. Constraints
6. Functional requirements
7. Non-functional requirements
8. Business rules
9. Acceptance criteria
10. Assumptions and open questions
11. Validation status

## 5. Handoff Rule

Stop at validated requirements unless the user explicitly asks for planning or implementation.

Requirements work ends when:

- the main ambiguities are removed or explicitly tracked
- the scope boundary is visible
- the user or stakeholder can confirm or correct the packet

If those conditions are not true, stay in elicitation or validation instead of pretending the work is ready.
