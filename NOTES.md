# NOTES — news-image-20261122 v2

- Competition: news-image-20261122, $100, closes 24 Nov 2026 07:00 WIB,
  results 7 Dec 2026 08:00 WIB.
- v1: submitted 23 Nov ~10:29 WIB (submission
  01a20673-71f1-7643-826d-1a7bc3e708d1, commit 9688772). Live score
  971,449 (97.14%), rank 3,741/12,530, 10W 2D 0L. Top-10 cutoff 990,650.
- v2 is a judge-driven rebuild (see STRATEGY.md): legibility at 300px,
  strict same-day list, one drone number, fixed tolls. Same 36 stories /
  7 regions; 2 stories replaced (Peru quake, Bulgari out; China margin
  cut, Verstappen Las Vegas win in).
- Title: "Sunday 22 November 2026: 36 sourced stories, 7 regions, all
  from Sunday — rebuilt to read at 300px"
- Build: Muse subagent, new repo Ci3hu1/news-image-20261122-v2.
- Status: built, tests green, kit check green (see below). NOT
  submitted — awaiting Joni's 'Setuju' on the exact entry.

## Build result (23 Nov ~12:05 WIB)

- entry.png 1024x1024, 608,266 bytes, sha256
  1c0b25f07603e0aec423a8bea41bfc15f03e24666b7a8aced10f6e1cdab13505.
- Tests: 6/6 pass (`python3 -m unittest discover -s tests`).
- uid-65534 read-only run: exit 0, byte-identical output.
- Visual fixes (2 rounds, the cap): numbers-strip values/labels
  un-overlapped; small-story meta un-overlapped from headline line 2;
  DATE CHECK items shortened to fit 2 columns; hero 2/3 deck/meta
  spacing fixed; "GULF OF FINLAND" meta shortened to "FINLAND".
- 300px preview: masthead + 3 leads clearly readable; small stories
  and ALSO ON read as a clean list, not a smear.
- Kit check (no transcripts yet): ok=false, failed=[transcripts_present]
  only. All other checks are "submission" status (deferred to the server
  at submit time, not failures): commit 1e5129e IS pushed to master
  (verified via git ls-remote), repo created 23 Nov after the competition
  opened (22 Nov 00:00 UTC), owner Ci3hu1.
- BUNDLE PENDING (blocker): the transcript bundle needs this build
  session's usage rows, but muse.db holds 0 rows for session
  74dfa9a6-eba4-40a9-ac9a-0b6248ad2b63 — usage rows flush only after the
  turn ends (THINKING_PRICED). Follow-up (next turn): re-run the usage
  SELECT for this session, write the deduped/sorted JSONL (0600), run
  the kit bundle (dry-run first) to
  ~/workspace/tools/makefun/bundles/ni22-v2-bundle.tar.gz, then re-run
  kit check with --transcripts until ok=true failed=[].
