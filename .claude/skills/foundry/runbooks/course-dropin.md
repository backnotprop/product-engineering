# Runbook: course drop-in — purchased content, local machines only

The animations.dev pack is purchased and unlicensed for redistribution. It NEVER
enters a commit. The public skills work without it and prefer it when present.

1. Install/refresh locally:
   `COURSE_SRC=~/oss/backnotprop/design/animationsdev foundry/scripts/course-dropin.sh`
   First run on a machine that owns the pack: add `--record` to store private hashes.
2. Quarterly: re-install the pack from the course, diff one agent dir (the 8 copies
   are identical), re-run with `--record` if the course updated. LOG it.
3. Adding a new mapping: create the manifest entry by hand (class as its grade,
   `"private": true`, upstream `animationsdev`, upstream_path relative to the pack),
   then run the script. The .gitignore fence must stay intact — the script refuses
   to run without it.
