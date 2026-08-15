---
name: ui-harden
description: Make an existing frontend resilient to real data, failures, devices, languages, accessibility needs, and performance constraints. Use when preparing UI for production, testing edge cases, fixing fragile responsive behavior, handling loading/error/permission/offline states, supporting localization or RTL, preventing lost work, or addressing measured frontend performance problems. Do not use for visual polish alone.
license: Apache-2.0
metadata:
  provenance: Derived and substantially modified from Impeccable 4.1.1 harden, adapt, and optimize
---

# UI Harden

Make the interface survive reality, not only the ideal demo.

## Establish the contract

Identify:

- the target path and primary task;
- the source context and the target context, including where, how, and for how long the product is used;
- supported devices, browsers, platforms, and input methods;
- realistic data ranges and content extremes;
- known network, authentication, permission, and concurrency behavior;
- localization and accessibility requirements;
- measurable performance symptoms, if performance is in scope.

Infer from the repository and existing tests before asking. Do not invent backend behavior or supported environments.

Read `references/resilience-matrix.md` and select the applicable scenarios. If the task changes device, viewport, input, platform, or delivery context, also read `references/adaptation-patterns.md`. If measured or suspected performance is in scope, read `references/performance-diagnostics.md`.

## Build a risk matrix

Cover the highest-risk combinations first:

- frequent or high-value user paths;
- destructive, financial, private, or irreversible actions;
- unsaved work;
- weak network or authentication boundaries;
- large or untrusted user content;
- keyboard, assistive-technology, and mobile paths.

Distinguish:

- **missing behavior** that needs implementation;
- **unknown behavior** that needs product clarification;
- **unsupported behavior** that needs explicit communication;
- **performance suspicion** that needs measurement.

## Implement resilience

### Content and data

- Handle empty, one-item, typical, maximum, and unexpectedly large states.
- Support long, short, missing, multiline, emoji, CJK, and bidirectional text.
- Avoid fixed dimensions that assume English or ideal content.
- Preserve hierarchy and action clarity when content wraps or truncates.
- Use wrapping, clamping, or truncation deliberately. If content is truncated, provide access to the full value when users need it.
- Check shrinking flex and grid children, long unbroken strings, replaced media, and intrinsic minimum sizes rather than patching overflow only at the page edge.

### Failure and recovery

- Provide specific, actionable loading, timeout, offline, validation, authentication, permission, rate-limit, and server-error states.
- Preserve user input and drafts when recovery is possible.
- Prevent duplicate submissions and unsafe concurrent actions.
- Handle stale responses, request cancellation, optimistic rollback, and conflicting edits where the architecture permits them.
- Make retry, cancel, undo, and support paths honest and reachable.
- Never expose internal error details as the primary user message.

### Adaptation and input

- Adapt structure rather than merely scaling it.
- Support narrow, intermediate, wide, zoomed, and text-expanded layouts.
- Remove hover-only dependencies and provide keyboard and touch equivalents.
- Keep visual, reading, and focus order coherent.
- Respect orientation, safe areas, pointer type, and platform conventions when relevant.
- Use feature and input capability detection rather than assuming screen width identifies the device or pointer.

### Localization

- Use complete translatable messages rather than concatenated fragments.
- Use locale-aware date, time, number, currency, and plural formatting.
- Prefer logical CSS properties where direction can change.
- Test expansion and RTL rather than assuming them.

### Validation and trust boundaries

- Make constraints visible before submission and keep client-side validation aligned with server behavior.
- Treat client-side validation and sanitization as UX, not a security boundary.
- Preserve input on validation and recoverable service errors.
- Do not invent server-side policy or change authorization behavior from the frontend.

### Performance

- Measure before optimizing.
- Identify whether the problem is loading, interaction latency, rendering, animation, memory, or network.
- Fix the measured bottleneck at the narrowest level.
- Avoid speculative memoization, virtualization, code splitting, or dependency removal.
- Compare before and after using the same scenario and environment.
- Optimize the largest measured bottleneck first. Do not sacrifice accessibility, correctness, or above-the-fold loading to improve a synthetic score.

## Validate

Add or update the narrowest useful tests for behavior that can regress. Exercise the real UI for scenarios that static tests cannot prove.

Verify:

- no task-ending dead ends;
- preserved work across recoverable failures;
- clear behavior for unsupported cases;
- accessible names, focus, announcements, contrast, zoom, and reduced motion;
- responsive structure and touch behavior;
- localization and directionality;
- measured performance improvement without functional regression.

Run repository checks relevant to changed files. Report untested scenarios honestly.

## Boundaries

- Do not change product policy to make an edge case easier.
- Do not add analytics, storage, retries, or dependencies without considering privacy, cost, and existing architecture.
- Do not claim support for a device, locale, browser, or failure mode that was not verified.
- Do not hide necessary functionality on smaller screens.
- Do not trade accessibility or correctness for performance.
- Keep visual redesign out of scope unless required to make a supported path usable.
