# Source Literature

This skill is grounded in mainstream requirements-engineering literature and standards. It is intentionally practical: the workflow translates the literature into a compact agent-friendly procedure for intake, refinement, and validation.

## Primary Basis

- ISO/IEC/IEEE 29148 requirements engineering standard (`https://standards.ieee.org/ieee/29148/6937/`): defines requirements-engineering processes and describes the construct and characteristics of a good requirement across the lifecycle.
- SWEBOK Guide V4 (`https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf`): treats requirements development as elicitation, analysis, specification, and validation, and emphasizes stakeholder analysis, multiple elicitation techniques, acceptance-criteria-based specification, and scope matching.
- INCOSE Guide to Writing Requirements materials (`https://www.incose.org/docs/default-source/working-groups/requirements-wg/shared_gtwr/gtwr_characteristics_section_4_050423.pdf?sfvrsn=9a7548c7_2`): provides practical rules for writing well-formed requirements, including structured statements, active voice, measurable performance, avoidance of vague terms, and explicit verification and validation activities.

## Supporting Basis

- SEBoK System Requirements Definition (`https://sebokwiki.org/wiki/System_Requirements_Definition`): emphasizes close stakeholder coordination, measurable characteristics, and maintained traceability when transforming needs into requirements.
- Volere Requirements Specification Template (`https://www.volere.org/templates/volere-requirements-specification-template/`): contributes a practical artifact structure around goals, stakeholders, constraints, glossary, business rules, fit criteria, open issues, and waiting-room items.
- Femmer et al., "Empirical research on requirements quality: a systematic mapping study" (`https://link.springer.com/article/10.1007/s00766-021-00367-z`): useful reminder that requirements quality is not just wording quality; it also concerns measurable attributes, review practices, and defects that escape downstream.

## Practical Translation

The skill deliberately applies the literature in these ways:

- **Reception and analysis** use SWEBOK, SEBoK, and Volere to force early clarity on problem, stakeholders, goals, constraints, and missing information.
- **Refinement** uses ISO/IEC/IEEE 29148 and INCOSE quality characteristics so vague statements are rewritten into clearer, more testable obligations.
- **Validation** follows the literature's distinction between writing good requirements and confirming that they are the right requirements for stakeholders.
- **Output shaping** borrows from Volere and modern agile specification practice: use only the lightest artifacts that reduce ambiguity, but do not skip acceptance criteria when later planning or testing would otherwise guess.
