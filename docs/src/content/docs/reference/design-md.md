---
title: DESIGN.md
description: The format pe-design writes and the other skills read.
sidebar:
  order: 2
---

Use this format when documenting an implemented visual system. It follows the [DESIGN.md format specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md): optional machine-readable YAML frontmatter followed by canonical prose sections.

## Extraction order

Inspect sources in this order and record where each authoritative value comes from:

1. design-token files and CSS custom properties;
2. Tailwind or other framework theme configuration;
3. CSS-in-JS theme objects;
4. shared buttons, inputs, cards, navigation, dialogs, and other representative components;
5. global styles;
6. computed styles and behavior in representative rendered states.

Do not extract every literal. Capture values and patterns that are reused, semantically important, or necessary to reproduce the system.

## Optional token frontmatter

Use frontmatter only when the project has coherent tokens to record:

```yaml
---
name: Project name
description: One-line description of the visual system
colors:
  action-primary: "#b8422e"
  surface-canvas: "#faf7f2"
typography:
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  control: "0.5rem"
spacing:
  compact: "0.5rem"
  default: "1rem"
components:
  button-primary:
    backgroundColor: "{colors.action-primary}"
    textColor: "{colors.surface-canvas}"
    rounded: "{rounded.control}"
    padding: "0.75rem 1rem"
---
```

Rules:

- Preserve the project's canonical names and value format. Do not rename everything to a generic scale.
- Token references use `{path.to.token}`.
- Components may reference primitive tokens; primitive tokens should remain concrete values.
- The portable component properties are `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, and `width`.
- Keep shadows, motion, focus rings, breakpoints, and other unsupported properties in the relevant prose section.
- Omit empty groups. Do not fabricate a complete token system from one-off values.
- Frontmatter values are normative. Prose describes purpose and use without asserting conflicting values.

## Canonical body

Use these headings in this order, omitting only sections that do not apply:

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

### Overview

Describe the observed character, density, material logic, and creative north star. Label interpretation as interpretation unless the user confirms it.

### Colors

Explain semantic roles, themes, contrast behavior, and named rules. Group by role, not by source-file or hex order.

### Typography

Record role, family, fallback, size behavior, weight, line height, tracking, measure, and loading behavior where established.

### Layout

Record containers, grids, spacing rhythm, density, content-driven breakpoints, responsive reflow, and reading/focus order.

### Elevation & Depth

Describe shadows, tonal layering, overlays, borders, and stacking. If the system is flat, state how it communicates depth instead.

### Shapes

Describe radii, borders, clipping, recurring geometry, and silhouette.

### Components

Document only implemented shared components. Include variants, states, shape, color assignment, internal spacing, focus treatment, and distinctive behavior.

### Do's and Don'ts

Write concrete guardrails evidenced by the implementation or explicitly confirmed by the user. Do not promote a one-page composition into a global rule.

## Quality rules

- Lead with descriptive language and put exact values in context.
- Explain where and why a token or pattern is used, not only what it is.
- Prefer memorable named rules when the system has real invariants.
- Preserve conflicts as documented drift rather than inventing coherence.
- Do not paste implementation-specific utility classes as the explanation.
- Do not invent components for an unimplemented system.
- Write only `DESIGN.md` unless the user explicitly requests another artifact.

---

Authored in the kit. Source: [skills/pe-design/references/understand/design-format.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-design/references/understand/design-format.md), rendered as-is at build time.
