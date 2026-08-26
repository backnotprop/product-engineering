# Understand (product & design context)

The understand mode of the design skill: capture durable product context in
PRODUCT.md and document a visual system in DESIGN.md. Provenance: our legacy
project-context skill (derived and substantially modified from Impeccable 4.1.1
init + document), converted to a mode reference. For URL-mode extraction and
machine validation see `url-and-validation.md`; for greenfield generated systems
see `generated-mode.md`.

Create durable context without making other skills depend on it.

`PRODUCT.md` records product truth. `DESIGN.md` records an observed or explicitly chosen visual system. Keep them separate because they change for different reasons.

## Default workflow

1. Resolve the project root and read any existing `PRODUCT.md`, `DESIGN.md`, product documentation, package metadata, routes, representative UI, tokens, and shared components.
2. Identify the requested mode: product context, design documentation, or both. Decide independently whether each file should be created, refreshed, or left alone.
3. Infer only what the repository supports. Treat code as evidence, not user approval.
4. Ask only about material product facts or visual commitments that cannot be inferred.
5. Before changing an existing context file, explain whether the operation is a refresh, merge, or replacement. Never silently overwrite it.
6. Write the smallest accurate document. Mark unresolved decisions instead of inventing answers.
7. Report what was created or changed, what evidence supported it, and what remains unknown.

Read `templates.md` before writing either file. When writing `DESIGN.md`, also read `design-format.md`; it contains the portable token schema, extraction order, and canonical headings.

## PRODUCT.md

Create or update `PRODUCT.md` when durable product knowledge would help future work:

- primary users and their situation;
- the job they are trying to complete;
- product purpose and success;
- capabilities and constraints;
- operating context and terminology;
- confirmed positioning, evidence, and brand commitments;
- platform and accessibility requirements.

Do not put palettes, typography, components, page concepts, or speculative marketing claims in `PRODUCT.md`.

For an existing product, inspect before interviewing. Ask users only for consequential gaps. For a new product, obtain at least one real confirmation before treating inferred facts as settled. If the project is greenfield and its stack is not already chosen, treat that choice as a user decision and record it only after confirmation.

## DESIGN.md

Create or update `DESIGN.md` only when there is a visual system to document:

- an existing interface with coherent conventions;
- explicit design tokens or a component library;
- a selected and implemented visual direction;
- a user-approved design system that is ready to record.

Do not fabricate `DESIGN.md` for an unimplemented project. A missing file is not a defect.

Document observed:

- colors and semantic roles;
- typography roles and reading behavior;
- spacing, density, containers, and responsive structure;
- elevation, borders, radii, and shape language;
- recurring components and their states;
- interaction and motion conventions;
- concrete do/don't rules supported by the implementation.

Prefer the project's canonical token values and names. If multiple conflicting implementations exist, document the conflict instead of pretending a coherent system exists.

Scan in this order: token files and CSS custom properties, framework theme configuration, shared components, global styles, then representative rendered output. Code identifies values and patterns; the rendered interface verifies how they behave.

Use the canonical `DESIGN.md` section names and order from `design-format.md`. Machine-readable frontmatter is normative when included. Prose explains where and why to use the tokens without creating a second source of truth.

Ask for qualitative language only when it adds durable guidance that code cannot provide, such as the system's creative north star, atmosphere, or a confirmed anti-reference. Do not disguise an agent's interpretation as user-confirmed brand language.

## Refresh rules

Refresh context only when durable truth changed:

- update `PRODUCT.md` for changed users, capabilities, constraints, positioning, or terminology;
- update `DESIGN.md` for changed shared tokens, typography roles, component patterns, or system-wide visual rules;
- do not refresh `DESIGN.md` for a local component change that follows existing conventions.

## Boundaries

- Do not initialize hooks, runtime services, hidden state, or project-specific workflow configuration.
- Do not require either file before another skill can run.
- Do not replace factual copy or brand commitments without confirmation.
- Do not turn a descriptive document into a redesign proposal.
- Do not create a design brief; this skill records durable context, not a temporary implementation plan.
- Do not create Impeccable sidecars or config files. The portable output is `PRODUCT.md`, `DESIGN.md`, or both.

## Completion

A context pass is complete when each written claim is supported by repository evidence or explicit user confirmation, existing files were preserved or deliberately updated, and absent information is honestly absent.
