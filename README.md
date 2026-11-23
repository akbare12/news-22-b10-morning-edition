[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/akbare12/news-22-b10-morning-edition/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/akbare12/news-22-b10-morning-edition/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# THE WORLD TODAY — Morning Edition, Sunday 22 November 2026

A one-image morning briefing of the world's news of Sunday 22 November 2026:
**WHAT HAPPENED OVERNIGHT** (stories 04–15) + **WHAT TO WATCH TODAY** (stories 16–33),
led by the three overnight leads: 2 tankers hit by mines in the Strait of Hormuz,
COP31 collapsing with no deal in Antalya, and Democrats reaching 258 House seats.

33 stories, 6 regions, every item first reported on 22 November 2026, each with a
named source and a verification badge (REPORTED / CLAIM / ONGOING). A pinned map,
a big-number strip, a NOT YET strip, and a footer date-check naming the items
deliberately excluded with their dates.

## The three leads

1. **2 TANKERS HIT — Strait of Hormuz, 17:13 UTC.** Two supertankers hit naval
   mines east of the Strait, north of Ghanam Island; both caught fire.
   (Iran navy · AP)
2. **NO DEAL — COP31, Antalya.** The climate summit collapsed: the EU and
   ~130 parties rejected a text with no mention of fossil fuels. Longest COP
   ever; first failure since 2009. (CNN · Reuters)
3. **258 — Washington.** Democrats win the House: Hubbard beats Foxx by 330
   votes in the NC recount; largest Democratic majority since 1992. GOP 173,
   4 races uncalled. (AP · Reuters)

## Stories 04–33

- 04 Dymer drone hits flats — 7 killed near Kyiv; boy pulled alive (Al Jazeera)
- 05 Merkury hit at Benghazi [CLAIM] — Russian corvette sunk, satellite images (France 24)
- 06 Khartoum drones kill 4 [CLAIM] — strikes blamed on RSF; UN building hit (AP)
- 07 Zelenskyy pleads for Patriots — Russia fired ~2,700 drones in a week (BBC)
- 08 Iran shows missile city — underground base unveiled on state TV (IRGC media)
- 09 Saudis stop Houthi attack [CLAIM] — drone+missile downed; Rabigh claimed (Reuters)
- 10 Bahrain blames Iran — industrial site struck; UAE condemns (France 24)
- 11 UAE condemns Bahrain strike — calls it a sovereignty violation (WAM)
- 12 Europe protests, day 3 — cost-of-living marches; 144 held in France (AP)
- 13 Settlers burn West Bank cars — 12 vehicles torched near Ramallah (Guardian)
- 14 Benghazi depot blast — ammo depot explodes inside naval base (Local auth.)
- 15 Unity talks stall — Eisenkot–Likud meet; wide gap on unity govt (Israeli media)
- 16 Finland: war spills over — Baltic shipping at risk as drones spread (Finnish govt)
- 17 Gaza aid van strike — WCK: three killed were not its team (WCK)
- 18 Banten factory fire — 3 dead, 36 missing after candy-plant blaze (BBC)
- 19 Fidan: Israel may use Druze [CLAIM] — Ankara warns of Syria pretext (Anadolu)
- 20 Fidan: war fallout hits markets — US–Israel war burden threatens trade (Anadolu)
- 21 Mongolia snap vote — presidential vote called after resignation (Euronews)
- 22 Mexico cartel boss captured — 11 killed in the operation (Al Jazeera)
- 23 Russian cargo ship burns — fire aboard vessel in the Baltic (Al Jazeera)
- 24 EU–Indonesia trade deal — pact signed after years of talks (EU)
- 25 Asian stocks slide — war fears hit markets across the region (SCMP)
- 26 Korea minister quits over AI cheat — 111 test takers caught with devices (BBC)
- 27 Gaza: 350,000 homeless — families displaced near Yellow Line (Al Jazeera)
- 28 Settlers attack homes in Hebron — homes attacked; tear gas fired (WAFA)
- 29 Gaza homes blocked [CLAIM] — Turkey: Israel blocks container homes (Anadolu)
- 30 Germany urged to arrest soldier — Hind Rajab Foundation files complaint (HRF)
- 31 Fred Nile dies at 92 — NSW figurehead; died 21 Nov, announced 22 Nov (Guardian)
- 32 Gamer rescues missing girl — teen, 16, and mother help FBI free girl (FBI)
- 33 Gaza toll 1,661 — death toll since Oct 2025 ceasefire (Gaza health min.)

## Date check

Every story above was first reported on 22 November 2026, unless its kicker says
otherwise. Deliberately excluded: El Chapo Isidro captured 20 Nov · BepiColombo
Mercury orbit 21 Nov · ICJ Myanmar ruling 19 Nov · Wall St rout 20 Nov · FBI
NCIC hack first reported 21 Nov. (Nvidia's reinstatement of Jensen Huang was
announced Monday 23 Nov, so it is not in this image.)

## How it is built

`draw.py` draws `entry.png` (1024×1024, PIL only) from the researched story list.
`main.py` is a stdlib-only copy program: it verifies the PNG magic, size
(≤1 MiB) and dimensions (1024×1024), then copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`), verifying the copy's sha256.
Two runs produce byte-identical output (sha256
`5888471e85cb472bf58d4a6414df8b439814b68e81b98469db77d2fcab89f33a`).

The image was zoom-checked at full size and at 300 px: all text legible, no
overlaps, no clipping, no garbled text. The map is a sketch with numbered pins
and a PIN KEY; the Middle East pin cluster is fanned out so every number reads.

SPDX-License-Identifier: MIT
