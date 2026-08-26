# Motion performance additions

Distilled from ibelick/ui-skills `fixing-motion-performance` (see MANIFEST for the pin).
Salvage contract: the five rules below, which the rest of the motion references don't
carry. General frame-budget craft lives in `build.md`/`recipes.md` (and the course
performance lane where installed); these are the additions only.

- **Never interleave layout reads and writes in the same frame.** Batch measurement,
  then batch writes. For layout-like effects (position/size changes), prefer
  FLIP-style transitions: measure → apply the end state → animate the inverted
  transform.
- **Pause or stop animations that are off-screen.** Use IntersectionObserver for
  visibility; never poll scroll position for animation.
- **Blur is a budgeted effect.** Keep animated blur ≤ 8px, short and one-time — never
  continuous, never on large surfaces. Reach for opacity and translate first.
- **View transitions are for navigation-level changes.** Avoid them for
  interaction-heavy UI and anywhere interruption/cancellation is required; treat size
  changes as potentially layout-triggering.
- **Do not migrate animation libraries to fix performance** unless explicitly
  requested. Apply fixes within the existing stack.
