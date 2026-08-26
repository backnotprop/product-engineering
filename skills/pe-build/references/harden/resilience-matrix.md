# Frontend resilience matrix


Select scenarios based on the product. Do not force irrelevant cases.

## Content

| Dimension | Cases |
| --- | --- |
| Presence | missing, empty, one item, typical, maximum |
| Length | one character, long words, long paragraphs, multiline labels |
| Characters | accents, emoji, CJK, combining marks, bidirectional text |
| Numbers | zero, negative, very large, high precision |
| Collections | duplicates, reordered items, stale entries, pagination boundaries |
| Media | missing, slow, wrong ratio, broken, oversized |

## Network and services

- initial loading;
- slow response;
- timeout;
- offline before action;
- disconnect during action;
- malformed or partial response;
- 400 validation error;
- 401 expired authentication;
- 403 permission change;
- 404 removed resource;
- 409 conflict or concurrent edit;
- 429 rate limit;
- 500-class failure;
- successful request with stale local state.

For every relevant case define: what happened, what remains safe, what the user can do next, and whether their work is preserved.

## Interaction

- rapid repeated activation;
- double submission;
- back/forward navigation;
- refresh during a flow;
- two tabs or clients;
- interruption and resume;
- cancel during loading;
- undo after a destructive action;
- keyboard-only completion;
- screen-reader announcements;
- touch, coarse pointer, and hover absence.

## Layout and environment

- narrow phone;
- intermediate width;
- wide desktop;
- landscape orientation;
- 200% zoom or equivalent text scaling;
- long translated copy;
- RTL direction;
- reduced motion;
- high contrast or forced colors when supported;
- safe-area insets;
- slow or memory-constrained device.

For an adaptation request, compare source assumptions with target reality:

| Question | Examples |
| --- | --- |
| Device and surface | phone, tablet, desktop, TV, print, email |
| Input | touch, mouse, keyboard, stylus, voice, gamepad |
| Attention | quick glance, interrupted mobile use, focused desk work |
| Connectivity | fast, high-latency, intermittent, offline |
| Expectations | platform navigation, back behavior, density, standard controls |

Adapt structure and interaction to the context. Do not merely scale pixels, hide core functionality, or assume desktop means fine pointer and fast hardware.

## Common implementation checks

- Use `min-width: 0` or `min-height: 0` where flex/grid intrinsic sizing prevents intended shrinkage.
- Use `overflow-wrap` for untrusted long strings; do not apply ellipsis without deciding how users access the full value.
- Use logical CSS properties when direction can change.
- Use locale-aware date, time, number, currency, and plural formatting.
- Reserve media dimensions to prevent layout shift and choose responsive sources for their rendered size.
- Prevent duplicate submissions while preserving a clear loading and cancellation state.
- Clean up listeners, timers, subscriptions, observers, and obsolete requests.
- Use feature detection and progressive enhancement rather than browser-name checks.
- Choose pagination, incremental rendering, or virtualization from measured collection behavior, not a fixed item-count superstition.

## Performance evidence

Choose metrics that match the symptom:

- loading: LCP, FCP, request waterfall, asset bytes;
- interaction: INP, long tasks, handler duration;
- layout: CLS, forced layout, repeated measurement;
- rendering: dropped frames, paint area, render count;
- collections: time and memory as item count grows;
- network: request count, payload, caching, duplicate fetches.

For web performance, common “good” Core Web Vitals reference thresholds are LCP at or below 2.5 seconds, INP at or below 200 milliseconds, and CLS at or below 0.1 at the 75th percentile. Treat these as diagnostic references, not guarantees that the interface feels fast or that every project has the same performance contract.

Record the scenario, environment, before value, change, and after value. A faster benchmark that changes behavior is not a valid improvement.

## Completion questions

- Can users understand the state?
- Is their work safe?
- Is there a real recovery action?
- Does the same path work with keyboard, touch, zoom, and assistive technology?
- Does content remain understandable across supported languages and sizes?
- Is the performance claim measured?
