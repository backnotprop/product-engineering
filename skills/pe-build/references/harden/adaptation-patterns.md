# Adaptation patterns


Use this reference only when a UI must work in a different device, viewport, input, platform, or delivery context.

## Compare contexts first

Record:

- source and target device or surface;
- pointer, keyboard, touch, voice, or other input;
- screen, orientation, safe-area, and text-scaling constraints;
- attention, interruption, and session length;
- connectivity and hardware assumptions;
- platform conventions users expect;
- source strengths that should survive.

The adaptation plan must identify what reflows, reorders, collapses, becomes persistent, changes interaction, or needs a different asset. “Make it smaller” is not a plan.

## Phone

- Prioritize one primary path and use progressive disclosure for secondary material.
- Reflow multi-column structures; do not hide core functionality.
- Put frequent actions within practical reach without violating platform patterns.
- Remove hover dependencies and preserve visible pressed, focus, loading, and error states.
- Use content-sized controls with a platform-appropriate target area, commonly at least 44 by 44 CSS pixels on touch web UI.
- Preserve progress across interruption and onscreen-keyboard changes.

Do not automatically choose a hamburger, bottom navigation, or bottom sheet. Use the pattern that matches information architecture and platform expectations.

## Tablet and hybrid input

- Support both touch and fine pointer rather than treating tablet as a large phone.
- Re-evaluate master-detail, side panels, and multi-column forms in both orientations.
- Preserve usable targets while allowing density appropriate to the task.
- Test external keyboard navigation and focus as well as touch.

## Desktop and wide screens

- Use additional space for useful comparison, context, and expert acceleration, not empty stretching.
- Bound reading measure and content width where unlimited expansion hurts comprehension.
- Add hover enhancement only when all functionality remains available without hover.
- Consider shortcuts, bulk actions, multi-select, and richer simultaneous context when the task supports them.
- Test touch-capable desktops and zoomed layouts.

## Print

- Remove navigation and controls that have no printed meaning.
- Add logical page breaks, print margins, and identifying metadata.
- Expand content hidden behind interaction when it is required in the document.
- Make URLs and data understandable on paper.
- Verify grayscale or limited-color legibility.

## Email

- Treat client support as a distinct implementation contract.
- Use a narrow, single-column reading path and robust email-compatible markup.
- Keep actions large and explicit, and move complex interaction to a linked application surface.
- Test the target client matrix rather than assuming browser CSS support.

## Responsive implementation

- Prefer content-driven breakpoints over device-name breakpoints.
- Use container queries when a component's available space, not the viewport, controls its behavior.
- Use fluid sizing with bounded `clamp()` only where interpolation is meaningful.
- Detect `pointer` and `hover` capabilities independently of width.
- Use logical properties and safe-area environment values where applicable.
- Use responsive image candidates for resolution changes and `<picture>`-style art direction when composition must change.
- Keep DOM, visual, reading, and focus order aligned when layout changes.

## Verification

Test representative real contexts when available. Emulation does not prove touch behavior, browser chrome, software keyboard, font rendering, memory pressure, or real network behavior.

Verify:

- source-context strengths survived;
- target-context expectations are met;
- all core functionality remains;
- orientation, zoom, localization, and long content hold;
- pointer, keyboard, touch, and assistive-technology paths work;
- no target was claimed as supported without evidence.
