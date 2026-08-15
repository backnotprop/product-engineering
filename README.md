# UI Skills

Five standalone skills for understanding, reviewing, refining, hardening, and onboarding user interfaces.

Each skill works independently. `PRODUCT.md` and `DESIGN.md` are useful context when they exist, but no review or implementation skill requires them.

| Skill | Purpose |
| --- | --- |
| `project-context` | Capture durable product context and document an existing visual system |
| `ui-review` | Review a UI's design, usability, accessibility, responsiveness, and implementation |
| `ui-polish` | Refine an existing UI without quietly redesigning it |
| `ui-harden` | Make a UI resilient to real data, failures, devices, languages, and input methods |
| `ui-onboarding` | Get new and returning users to useful product value quickly |

The collection intentionally contains no installer, hooks, background processes, live-mode runtime, critique history, or required command sequence.

## Install

```bash
npx skills add backnotprop/ui-skills
```

List the available skills:

```bash
npx skills add backnotprop/ui-skills --list
```

Install one skill:

```bash
npx skills add backnotprop/ui-skills --skill ui-review
```

The repository uses the portable multi-skill layout:

```text
skills/<skill-name>/SKILL.md
```

It can be consumed by any Agent Skills-compatible client or installer. `skills.sh.json` groups the five public skills for skills.sh discovery. No client-specific plugin runtime is required.

## Provenance

These skills are derivative works based on selected guidance from [Impeccable](https://github.com/pbakaus/impeccable), principally skill version 4.1.1. They preserve its useful review rubrics, decision rules, and implementation disciplines while removing Impeccable-specific orchestration, storage, hooks, command routing, and runtime assumptions.

See `DERIVATION.md` for the source-by-source comparison, plus `NOTICE` and `LICENSE`.
