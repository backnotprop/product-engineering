# Course drop-in (empty on GitHub by design)

This folder receives the purchased animations.dev skill pack on machines that own it.
The files are licensed for personal use only and are gitignored — they must never be
committed. The build skill works without them and prefers them when present (the spine
says so). To install locally:

    COURSE_SRC=~/oss/backnotprop/design/animationsdev foundry/scripts/course-dropin.sh

First run on a machine that owns the pack: add `--record` to store verification hashes.
Mappings live in foundry/MANIFEST.json as entries marked "private": true.
