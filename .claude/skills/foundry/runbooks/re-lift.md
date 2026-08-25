# Runbook: re-lift — an upstream changed a vendored file

Usually triggered by an upstream-watch PR/issue; also valid manually.

1. Check the LEDGER first: if the upstream change conflicts with an active ruling
   (e.g. an exact value we ruled on), STOP — this is a new-ruling situation, not a
   re-lift. Open an adjudicate issue.
2. Re-run lift.sh with the same dest and the new `--sha`. It overwrites the file,
   updates the manifest pin and hash, and logs.
3. For verbatim-minus files: after the re-lift, re-apply the cut (edit + make-patch.sh).
   If the patch no longer makes sense against the new text, that's a derivation
   update — record it.
4. Review the upstream diff in the PR like a dependency bump. Merge only with a
   human's approval.
