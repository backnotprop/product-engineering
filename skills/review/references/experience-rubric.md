# Experience review rubric


## Cognitive load

Classify the load:

- **Intrinsic**: complexity inherent to the task. Structure and scaffold it.
- **Extraneous**: effort created by the interface. Remove it.
- **Germane**: effort that helps users learn. Support it with consistent feedback.

Check:

1. Is there one clear primary focus?
2. Is information grouped into digestible chunks?
3. Are related items visually close and distinct groups separated?
4. Is the hierarchy obvious without reading every word?
5. Can the user make one meaningful decision at a time?
6. Are visible choices kept manageable, usually four or fewer at one decision point?
7. Must the user remember information from another screen?
8. Is complexity revealed when needed rather than all at once?

Zero or one failure is low load, two or three is moderate, and four or more is high. Treat these thresholds as prompts for judgment, not universal laws.

## Nielsen heuristics

Score each applicable heuristic from 0 to 4:

| # | Heuristic | What to inspect |
| --- | --- | --- |
| 1 | Visibility of system status | Loading, progress, confirmation, active location, validation |
| 2 | Match with the real world | Familiar language, natural order, recognizable concepts |
| 3 | User control and freedom | Undo, cancel, back, escape, clear filters |
| 4 | Consistency and standards | Terminology, components, platform conventions, repeated behavior |
| 5 | Error prevention | Constraints, defaults, destructive safeguards, draft recovery |
| 6 | Recognition over recall | Visible actions, labels, history, suggestions, contextual help |
| 7 | Flexibility and efficiency | Keyboard paths, shortcuts, bulk actions, expert acceleration |
| 8 | Aesthetic and minimalist design | Focus, hierarchy, relevance, absence of competing noise |
| 9 | Error recognition and recovery | Specific language, preserved work, actionable recovery |
| 10 | Help and documentation | Discoverable, concise, task-focused, contextual help |

Scoring anchors:

- **0**: absent or actively harmful;
- **1**: major gaps across the primary path;
- **2**: partial support with significant failures;
- **3**: good support with minor gaps;
- **4**: excellent and consistently verified.

Mark a heuristic `n/a` when it genuinely cannot apply. Use the percentage of the applicable maximum:

- 90%+: Excellent
- 70–89%: Good
- 50–69%: Acceptable
- 30–49%: Poor
- below 30%: Critical

Heuristics 7 and 10 are often `n/a` for short persuasive pages, campaigns, portfolios, and other surfaces that do not offer repeated operation or product help. Do not force a score merely to preserve a `/40` total.

## Emotional journey

Trace the path through arrival, uncertainty, commitment, high-stakes action, and completion:

- Does the peak moment reinforce the product's value?
- Does the final state leave clarity and confidence?
- Do payment, deletion, privacy, permission, or irreversible moments provide proportionate reassurance?
- Do delays and errors acknowledge the user's situation without false promises?

## Product specificity

Ask whether an unrelated product could reuse the composition, interaction, language, and visual treatment unchanged. Look for:

- framework-default topology that ignores the product's actual task;
- generic copy or visual motifs;
- missed opportunities to make product mechanisms visible;
- inconsistency between product stakes and emotional tone;
- distinctive choices that are genuinely useful rather than decorative.

## Persona checks

Choose only the two or three relevant perspectives:

- **Power user**: speed, keyboard use, bulk work, interruption by ceremony.
- **First-time user**: first action, terminology, labels, guidance, recovery.
- **Accessibility-dependent user**: keyboard, screen reader, zoom, contrast, motion.
- **Stress tester**: long values, empty and error states, refresh, concurrency, unusual input.
- **Distracted mobile user**: thumb reach, interruption, slow connection, preserved progress.

Walk the actual primary path. Report exact failures, not generic persona descriptions.

Suggested selection:

| Surface | Useful perspectives |
| --- | --- |
| Landing page or marketing | first-time, stress tester, distracted mobile |
| Dashboard, admin, editor | power user, accessibility-dependent, stress tester |
| Checkout or commerce | distracted mobile, stress tester, first-time |
| Onboarding | first-time, distracted mobile, accessibility-dependent |
| Data-heavy UI | power user, accessibility-dependent, stress tester |
| Form or wizard | first-time, accessibility-dependent, distracted mobile |

Derive project-specific perspectives only from confirmed audience evidence. Never invent personas to make the report look complete.

## Severity

- **P0 Blocking**: prevents task completion, causes data loss, or creates a critical safety failure.
- **P1 Major**: significant difficulty, exclusion, WCAG AA failure, or release-blocking confusion.
- **P2 Minor**: meaningful annoyance or inconsistency with a viable workaround.
- **P3 Polish**: low-impact refinement that does not impair completion.

When uncertain between levels, ask whether a user would contact support or abandon the task. If yes, it is usually at least P1.
