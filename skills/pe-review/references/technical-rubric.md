# Technical UI review rubric


For a full web review with adequate evidence, score each applicable dimension from 0 to 4. For a screenshot-only or scoped review, use `not assessed` rather than inferring implementation quality. Verify findings in context.

## Accessibility

Inspect:

- semantic structure and heading order;
- accessible names, roles, values, and states;
- keyboard reachability, order, traps, and focus visibility;
- labels, instructions, validation, and error announcements;
- meaningful alt text and decorative-image handling;
- text, control, and focus contrast;
- zoom, text scaling, and reduced-motion behavior;
- meaning communicated by more than color or motion alone.

For WCAG AA checks, ordinary text generally needs 4.5:1 contrast, large text 3:1, and meaningful controls, icons, and focus indicators 3:1. Use the standard and platform requirements applicable to the project. Automated accessibility results need manual verification.

## Performance

Inspect:

- layout thrashing and unnecessary synchronous measurement;
- avoidable renders and expensive work on interaction paths;
- image sizing, loading, and layout shift;
- unnecessary dependencies or oversized client bundles;
- unbounded filters, shadows, canvas work, or animation;
- broad or permanent `will-change`;
- long lists without an appropriate rendering strategy.

Do not prescribe memoization, lazy loading, or virtualization without evidence that it helps this target.

## Theming

Inspect:

- stable semantic roles for surfaces, text, actions, focus, and status;
- hard-coded values that conflict with an established token system;
- light and dark theme completeness;
- interactive and disabled-state contrast;
- theme changes that leave stale values;
- misuse of primitive versus semantic tokens.

A project without multiple themes does not automatically fail theming.

## Responsive behavior

Inspect:

- narrow, intermediate, and wide layouts;
- content-driven reflow rather than arbitrary breakpoint accumulation;
- overflow, fixed dimensions, and long-content behavior;
- touch targets and pointer assumptions;
- zoom and text expansion;
- DOM, reading, and focus order after visual reordering;
- orientation and safe-area behavior where relevant.

## Implementation integrity

Inspect:

- coherent use of shared components and conventions;
- repeated one-off shortcuts;
- misleading controls or decorative content presented as functional;
- missing states and incomplete paths;
- design-system drift;
- dead code, duplicate styles, and accidental complexity;
- product-specific structure versus interchangeable defaults.

Start the technical report with implementation integrity: does the code express a coherent, product-specific system, or repeated shortcuts and defaults? Then present the score table.

## Scoring anchors

- **0**: systemic failure across the primary path;
- **1**: major repeated failures;
- **2**: partial support with several verified issues;
- **3**: coherent implementation with minor isolated problems;
- **4**: consistently excellent and verified in representative states.

For five assessed dimensions, the maximum is 20:

- 90%+: Excellent
- 70–89%: Good
- 50–69%: Acceptable
- 30–49%: Poor
- below 30%: Critical

If any dimension is `not assessed`, reduce the denominator and state why. `Not assessed` is not the same as a zero.

Always separate:

- observed runtime evidence;
- source-level evidence;
- automated findings;
- unverified risk.

For every scored dimension, cite the element, behavior, file, line, computed value, trace, or test result that supports the score.
