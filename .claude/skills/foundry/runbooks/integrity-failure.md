# Runbook: integrity failure — CI is red on hashes

Someone or some agent edited a locked file. The diff shows exactly what changed.

1. REVERT FIRST. Restore the file: for verbatim, re-run lift.sh at the recorded
   pin (or `git checkout` the last green commit of that file); for verbatim-minus,
   restore pristine+patch state. Never "accept the improvement" in place.
2. If the edit was actually a good idea, re-route it to where improvements live:
   a ledger ruling (we now disagree with the source), or a PR to the upstream
   author (the source has a bug). Our copies stay mirrors.
3. LOG the incident (`integrity-failure`): what changed, who/what changed it,
   which runbook should have been used.
