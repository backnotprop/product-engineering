---
title: Vercel
description: The guidelines checklist, pinned.
sidebar:
  order: 5
---

[vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) (MIT) · [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (MIT)

**Carried:** 6 files, 5 verbatim, 1 verbatim-minus, each hash-locked to a pinned upstream commit.  
**Lives in:** [pe-build](/skills/pe-build) 5 · [pe-review](/skills/pe-review) 1  
**Rulings:** [L-11](#l-11) involve this work; each is below.  
**Watcher:** compared against upstream weekly; when a carried file changes upstream, an issue opens in the kit.

## Rulings

### L-11 · Guidelines house taste

vercel web-interface-guidelines: Title Case headings, "&" over "and", autocomplete stated both ways vs jakubkrehel: "evidence, not taste."  
**Ruling:** the evidence bar. House-taste rows are cut from the vendored copy (via its patch); the autocomplete tension resolves to: autocomplete on purposeful fields, off only for non-auth-sensitive cases.

## Receipts

Every row links to the upstream file at its pinned commit and to the kit's copy. Verbatim rows are the same bytes; verbatim-minus rows carry a recorded patch beside a pristine copy; distilled rows are authored from the source and say so.

| File in the kit | Class | Skill | Upstream |
| --- | --- | --- | --- |
| [motion/view-transitions/css-recipes.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/view-transitions/css-recipes.md) | verbatim | [pe-build](/skills/pe-build) | [skills/react-view-transitions/references/css-recipes.md](https://github.com/vercel-labs/agent-skills/blob/dd089a8c752c966dee8bf0f27cb625ba193ffd9e/skills/react-view-transitions/references/css-recipes.md) |
| [motion/view-transitions/implementation.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/view-transitions/implementation.md) | verbatim | [pe-build](/skills/pe-build) | [skills/react-view-transitions/references/implementation.md](https://github.com/vercel-labs/agent-skills/blob/dd089a8c752c966dee8bf0f27cb625ba193ffd9e/skills/react-view-transitions/references/implementation.md) |
| [motion/view-transitions/index.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/view-transitions/index.md) | verbatim | [pe-build](/skills/pe-build) | [skills/react-view-transitions/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/dd089a8c752c966dee8bf0f27cb625ba193ffd9e/skills/react-view-transitions/SKILL.md) |
| [motion/view-transitions/nextjs.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/view-transitions/nextjs.md) | verbatim | [pe-build](/skills/pe-build) | [skills/react-view-transitions/references/nextjs.md](https://github.com/vercel-labs/agent-skills/blob/dd089a8c752c966dee8bf0f27cb625ba193ffd9e/skills/react-view-transitions/references/nextjs.md) |
| [motion/view-transitions/patterns.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-build/references/motion/view-transitions/patterns.md) | verbatim | [pe-build](/skills/pe-build) | [skills/react-view-transitions/references/patterns.md](https://github.com/vercel-labs/agent-skills/blob/dd089a8c752c966dee8bf0f27cb625ba193ffd9e/skills/react-view-transitions/references/patterns.md) |
| [web-interface-guidelines.md](https://github.com/backnotprop/product-engineering/blob/main/skills/pe-review/references/web-interface-guidelines.md) | verbatim-minus (patched) | [pe-review](/skills/pe-review) | [command.md](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/command.md) |
