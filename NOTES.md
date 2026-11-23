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
- Kit check: ok=true failed=[] (bundle step is the parent's job).
