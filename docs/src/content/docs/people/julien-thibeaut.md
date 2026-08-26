---
title: Julien Thibeaut
description: Audit method, a11y ordering, metadata checklist, generation guardrails.
sidebar:
  order: 3
---

[ibelick/ui-skills](https://github.com/ibelick/ui-skills) (MIT)

**Carried:** 6 files, 3 distilled, 2 verbatim, 1 verbatim-minus, each hash-locked to a pinned upstream commit.  
**Lives in:** [pe-build](/skills/pe-build) 3 · [pe-review](/skills/pe-review) 2 · [pe-design](/skills/pe-design) 1  
**Rulings:** [L-05](#l-05), [L-06](#l-06), [L-08](#l-08), [L-09](#l-09) involve this work; each is below.  
**Watcher:** compared against upstream weekly; when a carried file changes upstream, an issue opens in the kit.

## Rulings

### L-05 · will-change

animationsdev: apply proactively vs jakubkrehel: only on observed first-frame stutter vs ibelick baseline: never outside an active animation.  
**Ruling:** reactive (jakub) — evidence-driven application only. Baseline's phrasing survives as the generation guardrail.

### L-06 · Custom easing curves

emilkowalski: "built-ins are too weak" vs ibelick baseline: "never introduce custom curves."  
**Ruling:** split by intent. Custom curves from the kit's named set: yes. Inventing novel curves ad hoc: no.

### L-08 · Disabled submit buttons

ibelick: explain why disabled vs jakubkrehel: never disable; validate on submit.  
**Ruling:** never disable. Wins on accessibility evidence — an enabled button that validates is discoverable; a disabled one is a dead end.

### L-09 · Accessibility findings in audits

ibelick improve-ui: "discard a11y findings unless requested" vs every other source.  
**Ruling:** a11y findings are never discarded. improve-ui's falsification pass survives without its discard rule.

## Receipts

Every row links to the upstream file at its pinned commit and to the kit's copy. Verbatim rows are the same bytes; verbatim-minus rows carry a recorded patch beside a pristine copy; distilled rows are authored from the source and say so.

| File in the kit | Class | Skill | Upstream |
| --- | --- | --- | --- |
| [craft/generation-guardrails.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/craft/generation-guardrails.md) | verbatim | [pe-build](/skills/pe-build) | [skills/baseline-ui/SKILL.md](https://github.com/ibelick/ui-skills/blob/ff7ca0a475e0dbb26a2db458beb03081b3dfd892/skills/baseline-ui/SKILL.md) |
| [harden/metadata.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/harden/metadata.md) | verbatim | [pe-build](/skills/pe-build) | [skills/fixing-metadata/SKILL.md](https://github.com/ibelick/ui-skills/blob/ff7ca0a475e0dbb26a2db458beb03081b3dfd892/skills/fixing-metadata/SKILL.md) |
| [motion/perf-additions.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/perf-additions.md) | distilled | [pe-build](/skills/pe-build) | [skills/fixing-motion-performance/SKILL.md](https://github.com/ibelick/ui-skills/blob/ff7ca0a475e0dbb26a2db458beb03081b3dfd892/skills/fixing-motion-performance/SKILL.md) |
| [understand/url-and-validation.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-design/references/understand/url-and-validation.md) | distilled | [pe-design](/skills/pe-design) | [skills/create-design-md/SKILL.md](https://github.com/ibelick/ui-skills/blob/ff7ca0a475e0dbb26a2db458beb03081b3dfd892/skills/create-design-md/SKILL.md) |
| [a11y-audit.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/a11y-audit.md) | distilled | [pe-review](/skills/pe-review) | [skills/fixing-accessibility/SKILL.md](https://github.com/ibelick/ui-skills/blob/ff7ca0a475e0dbb26a2db458beb03081b3dfd892/skills/fixing-accessibility/SKILL.md) |
| [audit-method.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/audit-method.md) | verbatim-minus (patched) | [pe-review](/skills/pe-review) | [skills/improve-ui/SKILL.md](https://github.com/ibelick/ui-skills/blob/ff7ca0a475e0dbb26a2db458beb03081b3dfd892/skills/improve-ui/SKILL.md) |
