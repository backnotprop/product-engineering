# Onboard (activation & first-run design)

The onboard mode of the pe-design skill: first-use onboarding, activation, setup, empty
states, contextual guidance, and feature discovery. Patterns catalog: `patterns.md`.

Get users to real value quickly. Onboarding is not a tour of every feature.

## Establish the activation goal

Determine:

- who is arriving and what they already know;
- their motivation, expected time commitment, and familiar alternatives;
- the job they came to complete;
- the smallest real outcome that proves value;
- the current path and where users hesitate or abandon;
- required setup versus optional enrichment;
- how success can be observed.

Infer what the product and existing evidence make clear. If the value moment or user experience level is genuinely unknown, ask before designing the flow.

Read `patterns.md` before choosing a pattern.

## Map the shortest path

Write the minimum sequence from arrival to first value. For every step ask:

- Is it required before value?
- Can it be inferred, defaulted, deferred, or skipped?
- Can the user learn it by doing real work?
- What feedback proves progress?
- What happens if the user leaves and returns?

Collect only information needed now. Explain requests whose purpose is not obvious. Preserve a direct path for experienced users.

If onboarding itself requires a meaningful time commitment, state it honestly. Do not add a welcome screen when the normal product can make the value and first action clear.

## Choose the lightest effective pattern

Prefer:

1. a clear first action in the normal product;
2. a useful empty state with a real CTA;
3. templates, sample data, or smart defaults;
4. contextual guidance at the moment of need;
5. a short checklist when several independent setup tasks matter;
6. a guided tour only when the interface cannot teach itself;
7. a sandbox only when mistakes are high-risk or concepts require practice.

Do not build a detached tutorial when users can learn through the real product.

## Design the complete lifecycle

Cover:

- first arrival;
- setup and permission requests;
- first success;
- interruption and resume;
- dismissal and skip;
- returning users;
- feature discovery after activation;
- reset or replay when useful.

Distinguish empty states:

- **first use**: explain value and enable creation;
- **user cleared**: acknowledge the state without reteaching;
- **no results**: explain filters or search and provide a reset;
- **no permission**: explain access and the path to request it;
- **failure**: explain what happened and provide recovery.

## Implement safely

- Use existing components, persistence, analytics, and experimentation systems.
- Do not add a tour library or local storage convention without checking the architecture.
- Respect dismissals and completion. Do not repeatedly show guidance.
- Keep tours short, dismissible, replayable when useful, and operable by keyboard and screen reader.
- Preserve user work across interruption.
- Make motion optional and non-blocking.
- Avoid fake progress, invented success claims, or celebration disproportionate to the achievement.
- Keep accessible help and shortcut discovery available after onboarding instead of forcing users to replay it.

## Verify

Test with a new-user state and an experienced-user path. Check:

- first action is clear within a few seconds;
- users reach a real outcome rather than merely finishing instructions;
- setup asks only for what is currently necessary;
- skip and dismissal work;
- interruption does not erase progress;
- empty, error, permission, and returning states are distinct;
- keyboard, screen reader, touch, zoom, localization, and reduced motion work;
- tracking measures meaningful activation, not vanity completion.
- measurement has a defined population, event, and baseline so completion and drop-off rates are interpretable.

Use real user observation or product data when available. Test at least the novice and experienced paths when feasible. Do not claim onboarding succeeds solely because the happy path is implemented.

## Report

State:

- the activation goal;
- the previous and new shortest path;
- what was deferred or removed;
- implementation and accessibility decisions;
- validation and measurement still needed.
