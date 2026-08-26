# Polish lenses


Use the lenses relevant to the target. They are not separate mandatory phases.

## Flow and hierarchy

- Does the structure follow product priority rather than framework defaults?
- Can the primary, secondary, and major groups be identified with a squint test?
- Are related items close and distinct groups clearly separated?
- Does disclosure match the user's decision sequence?
- Do arrival, transition, completion, and recovery states connect?
- Does the topology fit the actual task or merely expose the framework's default card, sidebar, or grid pattern?

## Layout

- Use a coherent spacing rhythm with meaningful contrast between tight and generous intervals.
- Prefer `gap` for sibling relationships and container-aware components when context changes.
- Test narrow, intermediate, wide, zoomed, and localized states.
- Keep visual, DOM, reading, and focus order aligned.
- Handle long text, empty states, overlays, sticky elements, and safe areas.
- Keep touch targets usable even when their visible mark is small.
- Use depth only when it clarifies state or hierarchy.

## Typography

- Make heading, body, label, metadata, and data roles distinguishable.
- Keep repeated roles consistent.
- Keep ordinary web body text around a 16px floor unless a legitimate dense role requires otherwise.
- Keep prose at a comfortable measure, commonly 45–75 characters.
- Test long headings, fallback fonts, localization, zoom, and font loading.
- Load only font assets and weights the interface uses.
- Tune line height to the actual face, width, language, and contrast rather than applying a universal ratio.
- On dark surfaces, check whether light text needs slightly more leading, tracking, or weight to remain equally legible.

## Color and themes

- Give every color a stable semantic role or deliberate atmospheric purpose.
- Keep primary actions easy to find and semantic meanings stable.
- Treat dark mode as a composition, not a mechanical inversion.
- Verify text at 4.5:1 for ordinary body copy and controls/focus indicators at 3:1 where WCAG applies.
- Never rely on color alone for meaning.
- Do not add a new palette when the task is refinement.
- Build stable roles for canvas, elevated surface, text, action, focus, selection, borders, and semantic states.
- Check computed foreground/background pairs, overlays, text on images, disabled content, and each supported theme.

## Language

- Use specific verbs and stable terminology.
- Put requirements before submission and errors beside their source.
- Make errors answer what failed, why when useful, and how to recover.
- Distinguish first-use, no-results, permission, and failure empty states.
- Keep copy as short as possible without removing meaning, consequence, or recovery.
- Ask before changing claims, legal meaning, or domain terminology.
- Use persistent labels for fields; placeholders are examples, not labels.
- For destructive actions, name the object and consequence. Prefer safe undo to unnecessary confirmation.
- Keep complete translatable messages instead of concatenating fragments.

## Simplification and intensity

When the interface is cluttered:

- name the one primary user goal and the elements required to complete it;
- remove repeated information and decoration that serves no hierarchy or function;
- reduce simultaneous choices, consolidate related actions, and defer optional complexity;
- replace unnecessary containers with proximity, alignment, and spacing;
- preserve necessary functionality, decision context, accessibility, and alternate access paths;
- document any removed feature or option and where users can still reach it.

For a **bolder** request:

- treat the named scope as sovereign; leave neighbors unchanged;
- diagnose which strong move the existing system already owns but the target fails to use;
- amplify that motif, type role, structure, density shift, or pacing instead of adding effects;
- make one decisive move, then quiet its surroundings so the move remains legible;
- perform the skeleton test: with copy removed, the structure should still express the section's job.

For a **quieter** request:

- identify whether intensity comes from saturation, contrast, weight, scale, motion, effects, or simultaneous hierarchy;
- reduce the specific sources rather than flattening everything;
- keep a few anchors so hierarchy and product character survive;
- remove decorative motion before useful feedback;
- verify that restraint did not become generic or low-contrast.

Do not invent new colors, fonts, radii, shadows, or motifs merely to make refinement visible. If the incumbent system cannot express the requested intensity, ask before expanding it.

## Interaction and motion

- Every control needs clear rest, hover, focus, active, disabled, loading, error, and success behavior where applicable.
- Keep keyboard focus visible and touch targets appropriate to the platform.
- Use motion for feedback, state, relationship, or continuity, not as proof of polish.
- Preserve useful feedback under reduced motion while removing unnecessary travel.

## Code and assets

- Replace one-off implementations with shared components only when the shared pattern truly owns the use case.
- Promote repeated values to semantic tokens, not every literal to an abstraction.
- Prevent image layout shift and use appropriate sources, ratios, and alt text.
- Remove temporary artifacts and accidental churn before finishing.

## Evidence at completion

Answer each applicable verification item with rendered behavior, a source location, a computed value, or a test result. A bare “looks good” or “yes” is not evidence.
