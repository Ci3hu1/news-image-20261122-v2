# BRIEF — news-image-20261122 v2 (judge-driven rebuild)

**Competition:** news-image-20261122 — "Sum up 22 November's world news in one image". $100 total (50 paid places), free entry. **Closes 24 Nov 2026 07:00 WIB** (2026-11-24T00:00:00Z). Results 7 Dec 2026. Harness program/v1, bundle-type (transcript bundle via kit CLI, no `record`).

**v1 live score:** 971,449 (97.14%), rank 3,741/12,530, 10W 2D 0L. Top-10 cutoff 990,650. Gap 19,201.

## Why v2 exists — the judge's written reasons on v1

Read from `GET /api/submissions/01a20673-71f1-7643-826d-1a7bc3e708d1`,
`scores[0].judge.heat.matches[].calls[].reason`. Criteria: (1) one day's
news naming that day; (2) selection and breadth; (3) it reads; (4)
faithful; (5) craft, legible at ~300px.

**Fixes (all four are in this build):**
1. Legibility at 300px — v1's 8–13px text was "unreadable smears".
   v2 type: masthead 46px, hero headlines 28/21px, featured 17px,
   ALSO ON 15px, DATE CHECK 11px, footer 10px. 300px preview checked.
2. Header contradicted DATE CHECK — Peru quake (20 Nov) and Paolo
   Bulgari (died 21 Nov) are OUT of the main list, into DATE CHECK.
   Iran line reworded to the Sunday event (new double launcher, Fars
   video 22 Nov; unveiling was 10 Nov). Header "ALL FROM SUNDAY" is
   now true.
3. Off-day stories — replaced with verified Sunday stories: China cuts
   stock margin ratio to 80%; Verstappen wins Las Vegas Grand Prix.
   Count stays 36.
4. Consistency — 186 launched / 161 shot down everywhere; Dymer toll
   4 killed, 14 missing; Delta delays 1,169 in story and KPI strip.

**Kept:** explicit date, 36 stories / 7 regions, sourcing +
claimed-vs-confirmed labels, honest DATE CHECK, UTC timeline, world map,
COP31 collapse lead (not "near a deal"), 186 drones (not the 20 Nov
400-drone barrage).

## Story list (36, 7 regions)

- Leads (3): COP31 collapses (Antalya), 186 drones / Dymer, Iran claims
  strikes on US bases in Bahrain.
- Featured (10): Benghazi ship blast, Sparta II towed, Hong Kong votes
  98.79%, India 720/9 Pant 128, Cikande fire, Gaza, Seoul minister quits,
  Delta ground stop 1,169 late, Lahore AQI 538, Riyadh Houthi claim.
- ALSO ON (14–36): Bahrain asks UN, Eisenkot–Likud, Bondi hero, France
  squad, Iran double launcher, Iran rationing, Zelenskyy Patriots, China
  spy campaign, Taiwan–Canada, Youth Congress / Meta, Pakistan minister
  Delhi, Trump / China nuclear, Pugh Hormuz swim, West Bank settlers,
  Guatemala arrest, China margin cut, AP Democrats 258, Poland debris,
  Brazil calamity, Verstappen, Cook Islands gale, Google Duplex, FinCEN
  MEXC.
- DATE CHECK (excluded): Peru M6.7 quake 20 Nov, 400-drone barrage
  20 Nov, robot-weapons talks 21 Nov, UK–EU youth deal 20 Nov,
  Paolo Bulgari dies 21 Nov. Not yet: COP32 Nov 2027, HK chief exec
  vote Mar 2027.
- Regions: Europe 5, Middle East 8, Asia 10, Africa 1, Americas 6,
  Oceania 2, Global 4 = 36.

## Technical

- Python stdlib ONLY for the graded program (`main.py` copies the
  bundled `entry.png`, SHA-256 verified). Render at build time
  (`render_poster.py`, needs Pillow + editorial-illustration library).
- Test as uid 65534 on a read-only copy; output byte-identical.
- Title: "Sunday 22 November 2026: 36 sourced stories, 7 regions, all
  from Sunday — rebuilt to read at 300px"
- Do NOT submit without Joni's 'Setuju' on the exact entry.
