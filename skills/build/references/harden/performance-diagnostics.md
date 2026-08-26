# Performance diagnostics

> Derivative work adapted and substantially modified from Impeccable 4.1.1 `optimize`.

Use this reference only when the task includes a measured or suspected performance problem.

## Diagnose before prescribing

Define:

- the user-visible symptom;
- the affected users, devices, and network;
- a repeatable scenario;
- the metric that represents the symptom;
- the current value and evidence source.

Classify the bottleneck:

| Area | Useful evidence |
| --- | --- |
| Initial loading | LCP, FCP, request waterfall, critical assets, server response |
| Interaction | INP, long tasks, handler duration, main-thread blocking |
| Layout stability | CLS, missing dimensions, injected content, font reflow |
| Rendering | frame time, paint area, forced layout, component renders |
| Memory | retained nodes, listeners, subscriptions, detached resources |
| Network | request count, payload, caching, duplicate or serial requests |
| Collections | time and memory as item count grows |

Fix the largest proven cause first.

## Loading

- Deliver correctly sized modern media and reserve dimensions.
- Load below-the-fold assets lazily; do not lazy-load the primary above-the-fold content.
- Load only used font families, subsets, and weights with a fallback strategy that avoids invisible text and disruptive metric changes.
- Defer or split noncritical code only when traces or bundle evidence justify it.
- Remove unused dependencies and third-party scripts when their cost is material.
- Use caching, compression, and resource priority appropriate to the architecture.

## Interaction and rendering

- Batch layout reads and writes instead of alternating them in loops.
- Break up long main-thread work and move genuinely independent computation off the interaction path.
- Avoid repeated renders caused by unstable state or subscriptions.
- Use memoization only for measured expensive work.
- Use bounded paint effects and avoid casual animation of layout-driving properties.
- Apply `will-change` only around a known expensive transition and remove it at rest.
- Choose pagination, incremental rendering, `content-visibility`, or virtualization from observed collection behavior.

## Animation

- Measure on representative hardware.
- Prefer transforms and opacity for routine movement while allowing other effects when their visual value justifies the measured cost.
- Keep JavaScript animation aligned with the rendering frame.
- Reduce or replace motion that delays input, drops frames, blocks reading, or conflicts with reduced-motion preferences.

## Reference thresholds

For web surfaces, common “good” Core Web Vitals thresholds at the 75th percentile are:

- LCP at or below 2.5 seconds;
- INP at or below 200 milliseconds;
- CLS at or below 0.1.

These are reference thresholds, not a substitute for the project's own performance contract or user-perceived behavior.

## Verify

Repeat the same scenario in the same environment and report:

- before value;
- implemented change;
- after value;
- functional, visual, and accessibility regression checks;
- limitations of the measurement.

A synthetic-score increase without movement in the user-facing symptom is not a successful optimization.
