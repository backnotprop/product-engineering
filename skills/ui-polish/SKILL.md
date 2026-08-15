---
name: ui-polish
description: Refine an existing interface to shipping quality without quietly redesigning it. Use when a user asks to polish, clean up, tighten, clarify, align, simplify, improve hierarchy, spacing, typography, color, copy, interaction states, or overall finish in an existing UI. Implement complete fixes and preserve the incumbent product identity, behavior, factual content, and out-of-scope areas.
license: Apache-2.0
metadata:
  provenance: Derived and substantially modified from Impeccable 4.1.1 polish, layout, typeset, colorize, clarify, distill, bolder, and quieter
---

# UI Polish

Bring an existing UI to a consistent quality bar. Polish is refinement, not concealed redesign.

## Establish the boundary

Identify:

- the exact target and user path;
- what must remain unchanged;
- the existing visual and interaction conventions;
- the intended quality bar and shipping constraints.

Read `DESIGN.md` when present, then verify it against tokens, shared components, neighboring flows, and rendered output. If no formal system exists, use coherent project conventions. Ask before changing a binding principle that cannot be inferred.

If the concept or information architecture is fundamentally wrong, explain that polish cannot solve it. Do not smuggle in a replacement visual identity.

Name the surface's job before editing:

- **Persuade**: help a visitor decide and act;
- **Operate**: help a user complete a task efficiently;
- **Read**: support comprehension and sustained reading;
- **Experience**: let the work or artifact lead.

Use the job to resolve trade-offs. A task interface values predictability and scanability differently from a campaign or portfolio.

## Gather evidence

Use the feature at representative sizes and states. Inspect:

- the primary task from arrival through completion or recovery;
- desktop, intermediate, and mobile layouts;
- mouse, keyboard, and touch paths where applicable;
- loading, empty, error, success, disabled, and permission states;
- long, missing, localized, and realistic content;
- relevant source, shared components, tokens, and existing validation.

Read `references/polish-lenses.md` before editing.

Make the experiential assessment before reading mechanical lint or audit findings when possible. Then use existing checks as a second source of evidence. A clean check cannot prove hierarchy, rhythm, specificity, or finish.

## Triage

Fix in this order:

1. blocked tasks, data loss, misleading state, and inaccessible paths;
2. missing operational states and recovery;
3. flow, hierarchy, responsiveness, and system drift;
4. visual, copy, icon, and motion inconsistencies;
5. dead code, accidental duplication, and asset cleanup.

Do not perfect one corner while the rest of the path remains below the same bar.

Classify the cause:

- **local defect**: a narrow implementation error;
- **one-off implementation**: replace with an established shared pattern;
- **missing system primitive**: add a reusable token or component only when repeated use justifies it;
- **conceptual mismatch**: stop and raise the larger product decision.

Fix the cause at the narrowest correct level.

Before implementation, state the primary task or reading path, what should lead and recede, the intended density, and how the target adapts. For explicit simplify, bolder, or quieter requests, use the dedicated decision rules in `references/polish-lenses.md`.

## Implement

- Preserve factual copy and product behavior unless the user authorized changes.
- Keep the primary task and current state obvious.
- Use proximity, reading order, and spacing before adding decoration or containers.
- Make same-role typography, controls, icons, and states consistent.
- Use semantic color roles and verify contrast in every relevant state.
- Complete default, hover, focus, active, disabled, loading, error, and success behavior.
- Keep motion purposeful, interruptible, performant, and respectful of reduced motion.
- Remove debug output, dead styles, unused imports, and polish-created duplication.
- Prefer existing dependencies and patterns. Do not install a new design or motion library for a local refinement.

## Verify

Walk the whole path again. Run the repository's narrow relevant checks and inspect the final diff.

Verify:

- task completion and recovery;
- representative viewport and input paths;
- operational and content-edge states;
- zoom, contrast, focus, semantics, and accessible names;
- console errors, layout shift, interaction latency, and image behavior;
- agreement with the user's scope and the incumbent system.

Use at most two bounded visual verification rounds: inspect, batch the fixes, then confirm. Do not enter an open-ended polishing loop.

## Report

Lead with the outcome. List:

- material improvements;
- files or surfaces changed;
- validation performed;
- any intentional exceptions or unresolved product decisions.
- confirmation that out-of-scope surfaces and product truth were preserved.
