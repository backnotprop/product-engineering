---
title: Emil Kowalski
description: Motion build, review standards, audits, the craft canon, the variant picker.
sidebar:
  order: 1
---

[emilkowalski/skills](https://github.com/emilkowalski/skills) (MIT)

**Carried:** 14 files, 13 verbatim, 1 verbatim-minus, each hash-locked to a pinned upstream commit.  
**Lives in:** [pe-build](/skills/pe-build) 6 · [pe-review](/skills/pe-review) 6 · [pe-design](/skills/pe-design) 2  
**Not distributed:** 20 files from the animations.dev course pack are mapped for owners to install locally and are never committed.  
**Rulings:** [L-01](#l-01), [L-02](#l-02), [L-03](#l-03), [L-04](#l-04), [L-05](#l-05), [L-06](#l-06), [L-07](#l-07) involve this work; each is below.  
**Watcher:** compared against upstream weekly; when a carried file changes upstream, an issue opens in the kit.

## Rulings

### L-01 · Press scale

jakubkrehel: exactly `0.96` vs emilkowalski: `0.95–0.98` range.  
**Ruling:** 0.96 exact. An exact value is enforceable; a range invites drift. Emil's range noted as tolerance.

### L-02 · Spring bounce

jakubkrehel: always `0` vs emilkowalski: subtle `0.1–0.3` when used.  
**Ruling:** bounce 0 by default; nonzero only when the design direction's register explicitly calls for playful.

### L-03 · Reduced motion

emil monolith: gentler-not-zero, keep opacity/color vs animationsdev refs: disable all, no exceptions.  
**Ruling:** gentler-not-zero. Matches the two-variant doctrine; blanket disable is the lazier reading.

### L-04 · Exit easing

jakubkrehel + emil monolith: ease-out both directions vs emil design-rules: accelerate away (ease-in).  
**Ruling:** ease-out for exits by default. Two of three sources, including Emil against himself. Accelerate-away allowed as a deliberate, stated choice.

### L-05 · will-change

animationsdev: apply proactively vs jakubkrehel: only on observed first-frame stutter vs ibelick baseline: never outside an active animation.  
**Ruling:** reactive (jakub) — evidence-driven application only. Baseline's phrasing survives as the generation guardrail.

### L-06 · Custom easing curves

emilkowalski: "built-ins are too weak" vs ibelick baseline: "never introduce custom curves."  
**Ruling:** split by intent. Custom curves from the kit's named set: yes. Inventing novel curves ad hoc: no.

### L-07 · Stagger

emilkowalski: 30–80ms per item vs jakubkrehel: ~100ms per group.  
**Ruling:** both — the units differ (list items vs semantic chunks). Reconciled in one paragraph; not a conflict.

## Receipts

Every row links to the upstream file at its pinned commit and to the kit's copy. Verbatim rows are the same bytes; verbatim-minus rows carry a recorded patch beside a pristine copy; distilled rows are authored from the source and say so.

| File in the kit | Class | Skill | Upstream |
| --- | --- | --- | --- |
| [craft/emil-craft.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/craft/emil-craft.md) | verbatim-minus (patched) | [pe-build](/skills/pe-build) | [skills/emil-design-eng/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/emil-design-eng/SKILL.md) |
| [craft/library-choices.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/craft/library-choices.md) | verbatim | [pe-build](/skills/pe-build) | [skills/pick-ui-library/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/pick-ui-library/SKILL.md) |
| [motion/apple-design.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/apple-design.md) | verbatim | [pe-build](/skills/pe-build) | [skills/apple-design/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/apple-design/SKILL.md) |
| [motion/build.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/build.md) | verbatim | [pe-build](/skills/pe-build) | [skills/animate/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/animate/SKILL.md) |
| [motion/recipes.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/recipes.md) | verbatim | [pe-build](/skills/pe-build) | [skills/animate/RECIPES.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/animate/RECIPES.md) |
| [motion/vocabulary.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/vocabulary.md) | verbatim | [pe-build](/skills/pe-build) | [skills/animation-vocabulary/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/animation-vocabulary/SKILL.md) |
| [vary/index.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-design/references/vary/index.md) | verbatim | [pe-design](/skills/pe-design) | [skills/prototype/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/prototype/SKILL.md) |
| [vary/picker.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-design/references/vary/picker.md) | verbatim | [pe-design](/skills/pe-design) | [skills/prototype/PICKER.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/prototype/PICKER.md) |
| [motion-audit-signals.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/motion-audit-signals.md) | verbatim | [pe-review](/skills/pe-review) | [skills/improve-animations/AUDIT.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/improve-animations/AUDIT.md) |
| [motion-audit.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/motion-audit.md) | verbatim | [pe-review](/skills/pe-review) | [skills/improve-animations/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/improve-animations/SKILL.md) |
| [motion-opportunities.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/motion-opportunities.md) | verbatim | [pe-review](/skills/pe-review) | [skills/find-animation-opportunities/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/find-animation-opportunities/SKILL.md) |
| [motion-review.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/motion-review.md) | verbatim | [pe-review](/skills/pe-review) | [skills/review-animations/SKILL.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/review-animations/SKILL.md) |
| [motion-standards.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/motion-standards.md) | verbatim | [pe-review](/skills/pe-review) | [skills/review-animations/STANDARDS.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/review-animations/STANDARDS.md) |
| [plan-template.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/plan-template.md) | verbatim | [pe-review](/skills/pe-review) | [skills/improve-animations/PLAN-TEMPLATE.md](https://github.com/emilkowalski/skills/blob/d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7/skills/improve-animations/PLAN-TEMPLATE.md) |
