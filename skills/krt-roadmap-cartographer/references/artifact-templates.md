# Artifact Templates

Use these templates when Roadmap Cartographer writes its single primary artifact.

## Roadmap

Path:

```text
docs/roadmaps/YYYY-MM-DD-NNN-<initiative-slug>-roadmap.md
```

Use the next available zero-padded sequence for the date and slug. Resume/update only when explicit; never overwrite silently.

```markdown
---
title: [Roadmap title]
status: active
date: YYYY-MM-DD
source_docs:
  - path/to/source.md
---

# [Roadmap title]

## Context Sufficiency Summary
- [What was found]
- [Why this is enough]

## Source Inventory
| Source | Contribution | Confidence |
|---|---|---|

## Roadmap Items
- RDM-001. **[Item name]**
  - Outcome: [user/system outcome]
  - Why now: [reason from docs]
  - Scope boundary: [included/excluded]
  - Hard depends on: [None / RDM-###]
  - Soft sequencing preference: [None / RDM-###]
  - Blocks/enables: [RDM-###]
  - Risk: [low/medium/high + why]
  - Expected brainstorm: `docs/brainstorms/...`
  - Expected plan: `docs/plans/...`
  - Suggested package: [roadmap-item / split by U-ID later]

## Dependency Graph
[Mermaid graph or bullet dependency map]

## Parallelization Waves
- Wave 1: [independent items]
- Wave 2: [items depending on Wave 1]

## Branch and PR Strategy
| Package candidate | Base branch | PR type | Dependency | Notes |
|---|---|---|---|---|

## Blockers and User Decisions
- [Decision needed before brainstorm/plan/work, or "None"]
```

Dependency rules:

- Hard dependency = cannot safely implement dependent item before prerequisite.
- Soft sequencing = preference, not blocker.
- Mark independent items for possible parallel work.
- If uncertainty affects branch strategy or product behavior, record it as a blocker or user decision.

Closeout shape:

```text
artifact_kind: roadmap
artifact_path: docs/roadmaps/YYYY-MM-DD-NNN-<initiative-slug>-roadmap.md
blockers: No blockers / <concise blockers>
recommended_next_action: Review this roadmap with the caller's document-review role, then continue to the first interactive brainstorm gate.
```

## Readiness Report

Path:

```text
docs/orchestration/YYYY-MM-DD-NNN-<initiative-slug>-readiness-report.md
```

Use the next available zero-padded sequence for the date and slug. A readiness report is terminal for the run; do not also create a roadmap.

```markdown
---
title: [Initiative] Readiness Report
status: blocked
date: YYYY-MM-DD
---

# [Initiative] Readiness Report

## Context Found
| Source | Contribution | Confidence |
|---|---|---|

## Missing Context
- [Missing minimum-context category]: [What is missing]

## Why Roadmap Generation Is Unsafe
- [How the missing context would force invented scope, dependency order, delivery constraints, or product behavior]

## Blocking Questions
- [Minimum question needed to unblock roadmap generation]

## Recommended Documents
- [Concrete doc to create or update, such as `STRATEGY.md`, `docs/architecture.md`, `docs/api-contracts.md`, `docs/data-model.md`, or `docs/delivery-workflow.md`]

## Exact Next Prompt
```text
Use ce:brainstorm to draft <recommended-doc> for <initiative> from docs/orchestration/YYYY-MM-DD-NNN-<initiative-slug>-readiness-report.md
```
```

Closeout shape:

```text
artifact_kind: readiness-report
artifact_path: docs/orchestration/YYYY-MM-DD-NNN-<initiative-slug>-readiness-report.md
blockers: <concise missing context summary>
recommended_next_action: Use ce:brainstorm to draft <recommended-doc> for <initiative> from <artifact_path>
```
