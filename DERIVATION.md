# Derivation review

This repository was reviewed against the installed Impeccable skill bundle at version 4.1.1. The comparison covered the original root workflow and every reference named below.

The extraction rule was:

1. retain judgment, decision rules, rubrics, safeguards, implementation guidance, and validation criteria;
2. rewrite them so each resulting skill can start and finish on its own;
3. remove mechanics whose value depends on Impeccable's runtime, scripts, storage, routing, or other commands;
4. state deliberate omissions instead of presenting a compressed rewrite as complete parity.

## `project-context`

Sources: `init`, `document`.

Retained:

- inspect the repository before interviewing;
- separate durable product truth from visual-system documentation;
- require confirmation for consequential inferred product facts;
- preserve existing context and distinguish refresh, merge, and replacement;
- keep speculative claims and visual recipes out of `PRODUCT.md`;
- scan tokens, themes, components, global styles, and rendered output;
- use the canonical `DESIGN.md` headings and portable token frontmatter;
- keep token values normative and prose explanatory;
- document conflicts rather than inventing system coherence.

Removed:

- `context.mjs` and inherited-path resolution;
- Impeccable schema comments and staleness machinery;
- `.impeccable/config.json` workflow defaults;
- live-mode setup;
- `.impeccable/design.json`, which exists for Impeccable's live panel;
- seed mode's dependency on `new-work` and surface briefs.

The standalone skill documents an implemented or explicitly approved system. It does not silently turn documentation into visual-world generation.

## `ui-review`

Sources: `critique`, `audit`.

Retained:

- a design/experience assessment completed before mechanical evidence can anchor it;
- product-specificity judgment;
- all ten Nielsen heuristics with applicable-denominator scoring;
- cognitive-load classification and checklist;
- emotional-journey and high-stakes-state review;
- persona-based path testing;
- five technical dimensions: accessibility, performance, theming, responsive behavior, and implementation integrity;
- 0–4 scoring, rating bands, P0–P3 severity, positive findings, systemic patterns, and actionable evidence.

Removed:

- mandatory detector execution;
- required browser overlay injection and live server;
- mandatory subagent orchestration and degraded banners;
- critique snapshots, target slugs, trends, ignore files, and temp-file protocol;
- recommendations expressed as Impeccable commands.

The standalone replacement preserves independence of judgment through sequential passes or optional separate agents. It works with browser evidence, source, existing project checks, screenshots, or an explicitly limited combination.

## `ui-polish`

Sources: `polish`, `layout`, `typeset`, `colorize`, `clarify`, `distill`, `bolder`, `quieter`.

Retained:

- refinement preserves the incumbent identity, behavior, factual copy, and out-of-scope surfaces;
- surface-job distinctions for persuasive, operational, reading, and experiential UI;
- causal triage across local defects, one-offs, missing primitives, and conceptual mismatch;
- whole-path priority order and bounded two-round visual verification;
- spatial thesis, squint test, grouping, rhythm, density, adaptation, and source/rendered evidence;
- typographic roles, measure, loading, fallback, localization, and dark-surface legibility;
- semantic color roles, contrast, dark-theme composition, and non-color cues;
- functional copy rules for actions, forms, errors, permissions, empty states, and localization;
- simplification without feature loss;
- bolder as amplification of existing system strengths within a sovereign scope;
- quieter as selective intensity reduction without erasing hierarchy or character.

Removed:

- detector commands and scope flags;
- stored critique lookup;
- live-mode signature parameters;
- command-to-command handoffs.

## `ui-harden`

Sources: `harden`, `adapt`, `optimize`.

Retained:

- extreme-content, service-failure, concurrency, interruption, accessibility, and localization testing;
- honest recovery and preservation of user work;
- structural adaptation based on device, input, attention, connectivity, and platform expectations;
- feature and pointer capability detection, safe areas, responsive media, and real-device checks;
- client validation as UX rather than a security boundary;
- measurement-first performance diagnosis across loading, interaction, layout, rendering, collections, and network;
- before/after evidence and protection against speculative optimization.

Removed:

- native-platform command routing;
- prescribed framework and library choices;
- bundled detector and tool assumptions;
- command handoffs.

## `ui-onboarding`

Source: `onboard`.

Retained:

- the aha moment and time to first value as the governing outcome;
- novice, expert, motivation, time, and prior-knowledge context;
- shortest-path analysis and deferral of nonessential setup;
- teach through real work, optionality, progressive disclosure, and respect for user intelligence;
- empty states, templates, contextual hints, checklists, tours, sandboxes, returning-user education, and persistent help;
- interruption, resume, skip, dismissal, replay, accessibility, and localization;
- activation, drop-off, time-to-value, and retained-use measurement.

Removed:

- prescribed tooltip and tour libraries;
- direct `localStorage` recipes;
- command handoffs.

The standalone skill requires the project's existing persistence and analytics architecture to be considered before adding new state or tracking.
