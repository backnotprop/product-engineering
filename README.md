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

## Derivation map

Each skill is a deliberate extraction rather than a generic rewrite:

| Skill | Impeccable 4.1.1 sources | Substantive guidance retained | Framework coupling removed |
| --- | --- | --- | --- |
| `project-context` | `init`, `document` | inspect-before-interview, confirmed product truth, refresh safety, token extraction, canonical `DESIGN.md` structure | `context.mjs`, `.impeccable` config and sidecar, live-mode setup, command continuation |
| `ui-review` | `critique`, `audit` | unanchored experience pass, technical evidence pass, Nielsen scoring, cognitive load, personas, specificity, severity, implementation integrity | required detector, browser overlay, mandatory subagents, snapshots, trends, command routing |
| `ui-polish` | `polish`, `layout`, `typeset`, `colorize`, `clarify`, `distill`, `bolder`, `quieter` | preservation boundary, causal triage, whole-path refinement, spatial/type/color/copy lenses, intensity control, bounded verification | detector commands, live-mode parameters, stored critique dependency, command handoffs |
| `ui-harden` | `harden`, `adapt`, `optimize` | edge-case matrix, recovery, localization, structural adaptation, accessibility resilience, measurement-first performance work | bundled tooling, platform routing, prescribed libraries, command handoffs |
| `ui-onboarding` | `onboard` | activation goal, shortest path to value, contextual patterns, empty-state taxonomy, returning-user lifecycle, measurement | prescribed tour libraries, storage recipes, command handoffs |

The removed parts are integration mechanics, not replacements for the design and engineering judgment retained here.

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
