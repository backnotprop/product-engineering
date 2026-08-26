# Context templates


Use only the sections supported by real information. Omit empty sections.

## PRODUCT.md

```markdown
# Product

## Platform

[web, iOS, Android, desktop, cross-platform, or another factual target]

## Stack

[For a greenfield project only: the confirmed implementation stack and any deployment constraint that materially shaped it. Omit when the repository already answers this.]

## Users

[Primary users, their situation, and their job.]

## Product Purpose

[What the product makes possible and what success means.]

## Positioning

[A real mechanism or position that distinguishes the product. Omit if unknown.]

## Operating Context

[Workflows, environments, documents, tools, and domain terminology.]

## Capabilities and Constraints

[Confirmed functionality, limits, technical constraints, and open decisions.]

## Brand Commitments

[Confirmed name, voice, identity constraints, and assets.]

## Evidence on Hand

[Real data, demonstrations, testimonials, research, or assets. Never invent these.]

## Product Principles

[Three to five durable principles derived from confirmed facts.]

## Accessibility and Inclusion

[Known user needs or required standards.]
```

## DESIGN.md

```markdown
# Design System

## Overview

[The observed visual character, density, and system logic.]

## Colors

[Canonical values, semantic roles, themes, and contrast rules.]

## Typography

[Families, roles, scale, measure, line height, weight, and fallback behavior.]

## Layout

[Containers, grid, spacing rhythm, density, breakpoints, and adaptation.]

## Elevation & Depth

[Shadows, tonal layers, overlays, borders, and stacking conventions.]

## Shapes

[Radii, borders, clipping, and recurring geometry.]

## Components

[Shared components, variants, states, and interaction conventions.]

## Do's and Don'ts

[Specific rules evidenced by the implementation.]
```

When machine-readable tokens are useful, add YAML frontmatter using the project's actual token names and canonical values. Follow `design-format.md`; do not create a second token source that can drift from the code.
