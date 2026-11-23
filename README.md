# Sunday 22 November 2026 — 36 sourced stories, 7 regions, all from Sunday

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Ci3hu1/news-image-20261122-v2/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Ci3hu1/news-image-20261122-v2/reward.svg)](https://make.fun/bounty/news-image-20261122)

A one-image front page summing up **Sunday 22 November 2026** — 36 sourced
stories across 7 regions, every one of them happened or was first reported
that Sunday. COP31 collapses in Antalya, 186 drones hit Ukraine, Iran
claims strikes on US bases in Bahrain.

This is v2 of our entry. v1 scored 971,449 (97.14%, rank 3,741/12,530) and
the judge's own written reasons named exactly what to fix — so v2 fixes it:

- **Readable at 300px.** The judge reads at ~300px and called v1's dense
  text "unreadable smears". v2 uses much bigger type everywhere (masthead
  46px, hero headlines 28/21px, featured headlines 17px, the ALSO ON list
  15px) with airy leading. A 300px preview is rendered and checked.
- **Strict same-day list.** v1's header said "ALL FROM SUNDAY" while its
  DATE CHECK admitted 20–21 Nov stories. v2 moves the Peru quake (20 Nov)
  and Paolo Bulgari (died 21 Nov) out of the main list into DATE CHECK,
  and rewords the Iran line to the actual Sunday event (new double
  missile launcher shown on Fars video). The header is now true.
- **One drone number.** 186 launched / 161 shot down everywhere; the
  400-drone barrage (20 Nov) is named only in DATE CHECK.
- **Fixed tolls.** Dymer: 4 killed, 14 missing. Delta delays: 1,169 in
  both the story and the KPI strip.

Kept from v1 (the judge praised these): the explicit date, 36 stories /
7 regions, sourcing with claimed-vs-confirmed labels, the honest DATE
CHECK panel, the UTC timeline and the world map.

## Entry

- **Competition:** [news-image-20261122 — Sum up 22 November's world news in one image](https://make.fun/bounty/news-image-20261122) ($100, closes 24 Nov 2026 07:00 WIB, results 7 Dec 2026)
- **Program:** `main.py` (pure Python stdlib) copies the bundled `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png`, then `/output/entry.png`, then
  `output.png` — first success wins, SHA-256 verified.
- **Poster:** `entry.png` (1024×1024, rendered by `render_poster.py` at
  build time from the editorial-illustration library; the grader has no
  Pillow, so the image ships in the repo).
- **Referral:** built for make.fun — [join with cc7tcnw6](https://make.fun/bounty/news-image-20261122?ref=cc7tcnw6)

## Verify

```sh
python3 render_poster.py          # rebuild entry.png + preview-300.png
python3 -m unittest discover -s tests -v
```

## Licence

MIT — see [LICENSE](LICENSE).
