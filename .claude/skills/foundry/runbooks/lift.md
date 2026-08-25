# Runbook: lift — bytes enter the repo

Use when a file from a graded upstream becomes part of a skill.

1. Confirm the file's grade and destination in `foundry/derivations/<skill>.md`
   (write the derivation entry first if it doesn't exist).
2. Run the script — never copy content any other way:
   ```
   foundry/scripts/lift.sh --upstream <id> --path <upstream-path> \
     --dest skills/<skill>/references/<name>.md --skill <skill> \
     [--sha <commit>] [--class verbatim|verbatim-minus]
   ```
   Omitting `--sha` pins to the upstream's current HEAD.
3. For `verbatim-minus`: the script stores the pristine copy and an empty patch.
   Now make the cut — edit the SHIPPED file (this is the one sanctioned edit,
   the cut must match the derivation file's stated omissions), then:
   ```
   foundry/scripts/make-patch.sh skills/<skill>/references/<name>.md
   ```
4. Run `foundry/scripts/check-integrity.sh` — must be green.
5. The script already appended the LOG line. PR it.

FORBIDDEN: pasting file content through an editor or model output; lifting a file
not named in a derivation entry; lifting from an upstream not in MANIFEST.
