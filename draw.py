#!/usr/bin/env python3
"""Draw the 22 Nov 2026 morning-edition front page (1024x1024)."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (26, 26, 26)
RED = (163, 30, 34)
NAVY = (31, 56, 100)
GOLD = (201, 162, 39)
GREEN = (46, 125, 50)
AMBER = (176, 124, 0)
BLUE = (31, 95, 168)
GRAY = (90, 90, 90)
SEA = (207, 227, 242)
LAND = (217, 196, 143)
LANDLINE = (150, 128, 80)

F = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(F + name, size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def text(x, y, s, f, fill=INK, anchor="la"):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor)

def wrap(s, f, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def badge(x, y, label, color, f=None, pad=5, h=16):
    f = f or SANS_B(10)
    w = int(d.textlength(label, font=f)) + pad * 2
    d.rounded_rectangle([x, y, x + w, y + h], radius=3, fill=color)
    d.text((x + pad, y + 2), label, font=f, fill=(255, 255, 255))
    return w

def fit(s, f, maxw):
    while s and d.textlength(s, font=f) > maxw:
        s = s[:-1]
    return s

# ---- top rule + masthead ----
d.rectangle([0, 0, W, 6], fill=RED)
text(24, 14, "THE WORLD TODAY", SERIF_B(54))
text(1000, 30, "SUNDAY 22 NOVEMBER 2026", SANS_B(20), fill=RED, anchor="ra")
d.line([24, 72, 1000, 72], fill=INK, width=2)

# ---- kicker ----
text(24, 80, "MORNING EDITION  ·  WHAT HAPPENED OVERNIGHT + WHAT TO WATCH TODAY",
     SANS_B(14))
text(1000, 80, "33 STORIES · 6 REGIONS", SANS_B(14), anchor="ra")
text(24, 100, "EVERY ITEM FIRST REPORTED 22 NOV", SANS(11))
lx = 1000
for label, color in [("ONGOING", BLUE), ("CLAIM", AMBER), ("REPORTED", GREEN)]:
    w = int(d.textlength(label, font=SANS_B(10))) + 10
    lx -= w + 6
    badge(lx, 99, label, color)
text(lx - 8, 101, "HOW WE KNOW EACH STORY —", SANS(11), anchor="ra")

# ---- hero panels ----
heroes = [
    dict(x=24,  color=NAVY, kick="CONFLICT · STRAIT OF HORMUZ", time="17:13 UTC",
         head="2 TANKERS HIT",
         body="Two supertankers hit mines east of the Strait; both on fire. First reported 17:13 UTC.",
         src="Iran navy · AP", kind="tanker"),
    dict(x=355, color=(139, 26, 26), kick="CLIMATE · ANTALYA", time="EVENING",
         head="NO DEAL",
         body="COP31 collapses; EU + ~130 parties reject text with no fossil fuels. First failure since 2009.",
         src="CNN · Reuters", kind="globe"),
    dict(x=686, color=NAVY, kick="POLITICS · WASHINGTON", time="18:00 UTC",
         head="258",
         body="Dems win House, largest majority since 1992; Hubbard beats Foxx by 330 in NC.",
         src="AP · Reuters", kind="dome"),
]
HY, HW, HH = 122, 314, 176
for h in heroes:
    x = h["x"]
    d.rectangle([x, HY, x + HW, HY + HH], outline=INK, width=1, fill=(255, 255, 255))
    d.rectangle([x, HY, x + HW, HY + 26], fill=h["color"])
    text(x + 8, HY + 5, h["kick"], SANS_B(11), fill=(255, 255, 255))
    text(x + HW - 8, HY + 5, h["time"], SANS(11), fill=(255, 255, 255), anchor="ra")
    # illustration band
    iy, ih = HY + 26, 62
    if h["kind"] == "tanker":
        d.rectangle([x, iy, x + HW, iy + ih], fill=NAVY)
        d.rectangle([x, iy + 40, x + HW, iy + ih], fill=(38, 90, 140))
        d.rectangle([x + 40, iy + 18, x + 200, iy + 40], fill=(230, 110, 30))
        d.rectangle([x + 200, iy + 8, x + 224, iy + 40], fill=(240, 240, 240))
        d.rectangle([x + 60, iy + 22, x + 90, iy + 30], fill=(255, 255, 255))
        for ang in range(0, 360, 45):
            import math
            r1 = 16
            x1 = x + 262 + int(r1 * math.cos(math.radians(ang)))
            y1 = iy + 30 + int(r1 * math.sin(math.radians(ang)))
            d.line([x + 262, iy + 30, x1, y1], fill=(20, 20, 20), width=3)
        d.ellipse([x + 254, iy + 22, x + 270, iy + 38], fill=(20, 20, 20))
        d.ellipse([x + 90, iy + 6, x + 112, iy + 28], fill=(255, 200, 40))
    elif h["kind"] == "globe":
        d.rectangle([x, iy, x + HW, iy + ih], fill=(139, 26, 26))
        cx, cy, r = x + 157, iy + 31, 26
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(230, 230, 220), outline=(20, 20, 20), width=2)
        d.ellipse([cx - 16, cy - 18, cx - 2, cy - 4], fill=(90, 160, 90))
        d.ellipse([cx + 2, cy + 4, cx + 16, cy + 18], fill=(90, 160, 90))
        d.ellipse([cx + 6, cy - 20, cx + 18, cy - 8], fill=(90, 160, 90))
        d.line([cx - 4, cy - 26, cx + 2, cy - 8, cx - 6, cy + 6, cx + 4, cy + 26],
               fill=(20, 20, 20), width=3)
    else:
        d.rectangle([x, iy, x + HW, iy + ih], fill=NAVY)
        for sx in (x + 30, x + 250):
            for sy in (iy + 8, iy + 30):
                d.text((sx, sy), "*", font=SANS_B(14), fill=(255, 220, 80))
        d.rectangle([x + 100, iy + 34, x + 214, iy + 62], fill=(240, 240, 240))
        d.pieslice([x + 122, iy + 2, x + 192, iy + 40], 180, 360, fill=(240, 240, 240))
        d.rectangle([x + 152, iy - 2, x + 162, iy + 8], fill=(240, 240, 240))
        for i in range(5):
            d.rectangle([x + 110 + i * 20, iy + 42, x + 122 + i * 20, iy + 56], fill=NAVY)
    text(x + 10, HY + 92, h["head"], SANS_B(30))
    lines = wrap(h["body"], SANS(12), HW - 20)
    for i, ln in enumerate(lines[:2]):
        text(x + 10, HY + 128 + i * 15, ln, SANS(12))
    badge(x + 10, HY + HH - 20, "REPORTED", GREEN)
    text(x + 84, HY + HH - 18, h["src"], SANS(11))

# ---- big-number strip ----
d.rectangle([24, 306, 1000, 338], fill=NAVY)
nums = [("258", "House seats"), ("2", "tankers hit"), ("194", "COP31 parties"),
        ("330", "votes in NC"), ("36", "missing in Banten"), ("1,661", "Gaza toll")]
nx = 40
for n, lab in nums:
    text(nx, 311, n, SANS_B(20), fill=GOLD)
    nx += int(d.textlength(n, font=SANS_B(20))) + 8
    text(nx, 317, lab, SANS(11), fill=(255, 255, 255))
    nx += int(d.textlength(lab, font=SANS(11))) + 34

# ---- map ----
text(24, 346, "WHERE IT HAPPENED — EVERY HERO PINNED", SANS_B(14))
MAP = (24, 366, 600, 500)  # x0,y0,x1,y1
d.rectangle(MAP, fill=SEA, outline=INK, width=1)
# rough continents
def poly(pts, fill=LAND):
    d.polygon(pts, fill=fill, outline=LANDLINE)
poly([(40, 400), (90, 382), (150, 386), (185, 400), (170, 420), (120, 432), (70, 428), (38, 414)])  # N America
poly([(120, 448), (160, 444), (180, 462), (168, 492), (140, 496), (122, 472)])  # S America
poly([(340, 388), (380, 380), (415, 388), (410, 408), (372, 412), (344, 402)])  # Europe
poly([(345, 420), (395, 418), (415, 436), (405, 478), (380, 492), (355, 470), (340, 442)])  # Africa
poly([(420, 386), (480, 378), (545, 386), (575, 404), (560, 432), (520, 448), (470, 446), (430, 424), (418, 402)])  # Asia
poly([(520, 468), (560, 462), (578, 476), (560, 492), (528, 490)])  # Australia
pins = {
    1: (452, 448), 2: (378, 406), 3: (118, 412), 4: (360, 442),
    5: (392, 468), 6: (398, 392), 7: (512, 470), 8: (414, 430),
}
for n, (px, py) in pins.items():
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED, outline=(255, 255, 255), width=1)
    d.text((px, py), str(n), font=SANS_B(11), fill=(255, 255, 255), anchor="mm")
# pin key
text(620, 366, "PIN KEY", SANS_B(13))
key = [
    "1  Hormuz — 2 tankers hit mines, 17:13",
    "2  Antalya — COP31 collapses, no deal",
    "3  Washington — Dems reach 258, 18:00",
    "4  Benghazi — Russian ship hit, depot blast",
    "5  Khartoum — drones kill 4, UN hit",
    "6  Kyiv — Dymer drone strike, 7 killed",
    "7  Banten — factory fire, 36 missing",
    "8  Gaza — toll 1,661 since Oct 2025",
]
for i, k in enumerate(key):
    text(620, 386 + i * 15, k, SANS(11.5))

# ---- story sections ----
def story_row(x, y, num, head, sub, src, claim=False, w=482):
    text(x, y, f"{num:02d}", SANS_B(13), fill=RED)
    hx = x + 26
    htxt = fit(head, SANS_B(13), w - 26 - (int(d.textlength(src, font=SANS(10))) + 8 if src else 0))
    text(hx, y, htxt, SANS_B(13))
    if src:
        text(x + w, y + 1, src, SANS(10), fill=GRAY, anchor="ra")
    if claim:
        badge(x + w - 46, y + 16, "CLAIM", AMBER, h=13)
    text(hx, y + 15, fit(sub, SANS(10.5), w - 26 - (50 if claim else 0)), SANS(10.5), fill=(60, 60, 60))

overnight = [
    (4, "Dymer drone hits flats", "7 killed near Kyiv; boy pulled alive from rubble", "Al Jazeera", False),
    (5, "Merkury hit at Benghazi", "Russian corvette sunk, satellite images show", "France 24", True),
    (6, "Khartoum drones kill 4", "Strikes blamed on RSF; UN building damaged", "AP", True),
    (7, "Zelenskyy pleads for Patriots", "Russia fired ~2,700 drones in a week", "BBC", False),
    (8, "Iran shows missile city", "Underground base unveiled on state TV", "IRGC media", False),
    (9, "Saudis stop Houthi attack", "Drone+missile downed; Rabigh claimed", "Reuters", True),
    (10, "Bahrain blames Iran", "Industrial site struck; UAE condemns", "France 24", False),
    (11, "UAE condemns Bahrain strike", "Calls it a sovereignty violation", "WAM", False),
    (12, "Europe protests, day 3", "Cost-of-living marches; 144 held in France", "AP", False),
    (13, "Settlers burn West Bank cars", "12 vehicles torched near Ramallah", "Guardian", False),
    (14, "Benghazi depot blast", "Ammo depot explodes inside naval base", "Local auth.", False),
    (15, "Unity talks stall", "Eisenkot–Likud meet; wide gap on unity govt", "Israeli media", False),
]
text(24, 510, "WHAT HAPPENED OVERNIGHT — STORIES 04–15", SANS_B(14))
text(1000, 510, "ALL TIMES UTC", SANS(11), fill=GRAY, anchor="ra")
for i, (n, h, s, src, cl) in enumerate(overnight):
    col, row = i % 2, i // 2
    story_row(24 + col * 494, 532 + row * 30, n, h, s, src, cl, w=482)

watch = [
    (16, "Finland: war spills over", "Baltic shipping at risk as drones spread", "Finnish govt", False),
    (17, "Gaza aid van strike", "WCK: three killed were not its team", "WCK", False),
    (18, "Banten factory fire", "3 dead, 36 missing after candy-plant blaze", "BBC", False),
    (19, "Fidan: Israel may use Druze", "Ankara warns of Syria operation pretext", "Anadolu", True),
    (20, "Fidan: war fallout hits markets", "US–Israel war burden threatens trade", "Anadolu", False),
    (21, "Mongolia snap vote", "Presidential vote called after resignation", "Euronews", False),
    (22, "Mexico cartel boss captured", "11 killed in the operation", "Al Jazeera", False),
    (23, "Russian cargo ship burns", "Fire aboard vessel in the Baltic", "Al Jazeera", False),
    (24, "EU–Indonesia trade deal", "Pact signed after years of talks", "EU", False),
    (25, "Asian stocks slide", "War fears hit markets across the region", "SCMP", False),
    (26, "Korea minister quits over AI cheat", "111 test takers caught with devices", "BBC", False),
    (27, "Gaza: 350,000 homeless", "Families displaced near Yellow Line", "Al Jazeera", False),
    (28, "Settlers attack homes in Hebron", "Homes attacked; tear gas fired", "WAFA", False),
    (29, "Gaza homes blocked", "Turkey: Israel blocks container homes", "Anadolu", True),
    (30, "Germany urged to arrest soldier", "Hind Rajab Foundation files complaint", "HRF", False),
    (31, "Fred Nile dies at 92", "NSW figurehead; died 21 Nov, announced 22 Nov", "Guardian", False),
    (32, "Gamer rescues missing girl", "Teen, 16, and mother help FBI free girl", "FBI", False),
    (33, "Gaza toll 1,661", "Death toll since Oct 2025 ceasefire", "Gaza health min.", False),
]
text(24, 718, "WHAT TO WATCH TODAY — STORIES 16–33", SANS_B(14))
text(1000, 718, "ALL TIMES UTC", SANS(11), fill=GRAY, anchor="ra")
for i, (n, h, s, src, cl) in enumerate(watch):
    col, row = i % 3, i // 3
    story_row(24 + col * 330, 740 + row * 34, n, h, s, src, cl, w=318)

# ---- NOT YET strip ----
d.rectangle([24, 950, 1000, 968], fill=(247, 233, 160), outline=INK, width=1)
text(32, 954, "NOT YET — DO NOT READ AS DONE:  4 House races uncalled  ·  COP32 venue not set  ·  Gaza ceasefire talks: no deal announced",
     SANS_B(11.5))

# ---- footer ----
fy = 974
for ln in wrap("DATE CHECK — Every story above was first reported on 22 Nov, unless its kicker says otherwise.  EXCLUDED: El Chapo Isidro captured 20 Nov · BepiColombo Mercury orbit 21 Nov · ICJ Myanmar ruling 19 Nov · Wall St rout 20 Nov · FBI NCIC hack first reported 21 Nov.", SANS(9.5), 976):
    text(24, fy, ln, SANS(9.5), fill=GRAY)
    fy += 12
for ln in wrap("LEGEND: REPORTED = confirmed by 2+ sources · CLAIM = one side alleges, unverified · ONGOING = still developing.     SOURCES: AP · Reuters · BBC · CNN · France 24 · Al Jazeera · Guardian · SCMP · IRNA · Anadolu · WAFA · HRF · WCK · CNBC · The Hindu", SANS(9.5), 976):
    text(24, fy, ln, SANS(9.5), fill=GRAY)
    fy += 12

img.save("entry.png", optimize=True)
print("saved entry.png")
