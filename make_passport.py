"""Draw an invented passport spread as a deterministic 1024x1024 PNG."""
from PIL import Image, ImageDraw, ImageFont
import math, os

W = H = 1024
im = Image.new('RGB', (W, H), (243, 238, 224))
d = ImageDraw.Draw(im)

def font(sz, bold=False):
    for p in (["C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf"] if bold
              else ["C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/consola.ttf"]):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

# Outer cover border and centre gutter
d.rectangle([18, 18, W-18, H-18], outline=(40, 48, 44), width=3)
d.line([(W//2, 28), (W//2, H-28)], fill=(90, 84, 70), width=3)
d.rectangle([24, 24, W//2-16, H-24], outline=(150, 140, 118), width=1)
d.rectangle([W//2+16, 24, W-24, H-24], outline=(150, 140, 118), width=1)

# Left page header
d.text((60, 56), "REPUBLIC OF VERRANIA", font=font(30, True), fill=(28, 38, 46))
d.text((60, 100), "PASSPORT  /  PASSEPORT  /  PASAPORTE", font=font(16), fill=(70, 70, 70))
d.line([(58, 130), (W//2-40, 130)], fill=(40, 48, 44), width=2)
d.text((60, 150), "TYPE", font=font(13), fill=(90, 90, 90))
d.text((150, 150), "COUNTRY CODE", font=font(13), fill=(90, 90, 90))
d.text((300, 150), "PASSPORT NO.", font=font(13), fill=(90, 90, 90))
d.text((60, 170), "P", font=font(26, True), fill=(20, 24, 30))
d.text((150, 170), "VRA", font=font(26, True), fill=(20, 24, 30))
d.text((300, 170), "VRA-0041982", font=font(22, True), fill=(20, 24, 30))

# Portrait frame with a stylised肩/肩-less bust
px, py, pw, ph = 60, 220, 250, 310
d.rectangle([px, py, px+pw, py+ph], outline=(60, 60, 60), width=2)
d.rectangle([px+4, py+4, px+pw-4, py+ph-4], fill=(206, 200, 186))
cx, cy = px+pw//2, py+120
d.ellipse([cx-52, cy-58, cx+52, cy+58], fill=(120, 104, 86))
d.ellipse([cx-50, cy-54, cx+50, cy+50], fill=(186, 150, 118))
d.polygon([(cx-58, cy+56), (cx+58, cy+56), (cx+96, py+ph-8), (cx-96, py+ph-8)], fill=(58, 72, 84))
d.line([(cx-30, cy-6), (cx-10, cy-6)], fill=(60, 45, 35), width=3)
d.line([(cx+10, cy-6), (cx+30, cy-6)], fill=(60, 45, 35), width=3)
d.text((px+8, py+ph-26), "HOLDER: M. ADEYEMI", font=font(12), fill=(40, 40, 40))

# Personal details rows
rows = [
    ("SURNAME / NOM", "ADEYEMI"),
    ("GIVEN NAMES / PRENOMS", "MARISOL ANIKA"),
    ("NATIONALITY", "VERRANIAN"),
    ("DATE OF BIRTH / NE(E) LE", "14 OCT 1991"),
    ("PLACE OF BIRTH", "PORT AURELIO, VRA"),
    ("SEX / SEXE", "F"),
    ("DATE OF ISSUE / DELIVRE LE", "02 MAR 2019"),
    ("DATE OF EXPIRY / EXPIRE LE", "01 MAR 2029"),
    ("AUTHORITY / AUTORITE", "DIRECTORATE OF CIVIL RECORDS"),
]
y = 220
for k, v in rows:
    d.text((330, y), k, font=font(12), fill=(95, 95, 95))
    d.text((330, y+17), v, font=font(17, True), fill=(25, 28, 32))
    d.line([(330, y+40), (W//2-40, y+40)], fill=(205, 198, 182), width=1)
    y += 48

# Machine-readable zone at foot of left page
mrz = "P<VRADEYEMI<<MARISOL<ANIKA<<<<<<<<<<<<<<<<<<<<<<<<<"
mrz2 = "VRA00419822VRA9101014F2903012<<<<<<<<<<<<<<<<<<<<<<04"
d.rectangle([40, 880, W//2-30, H-46], outline=(70, 70, 70), width=1)
d.text((50, 896), mrz, font=font(17), fill=(30, 30, 30))
d.text((50, 922), mrz2, font=font(17), fill=(30, 30, 30))

# Right page: stamps and travel history
rx = W//2 + 50
d.text((rx, 56), "VISA & ENTRY RECORD", font=font(24, True), fill=(28, 38, 46))
d.line([(rx, 94), (W-56, 94)], fill=(40, 48, 44), width=2)
d.text((rx, 110), "This document remains the property of the Republic of Verrania.", font=font(13), fill=(80, 80, 80))

def stamp(x, y, r, title, sub, colour):
    for rr, wd in ((r, 3), (r-7, 1)):
        d.ellipse([x-rr, y-rr, x+rr, y+rr], outline=colour, width=wd)
    d.text((x-70, y-26), title, font=font(18, True), fill=colour)
    d.text((x-52, y+2), sub, font=font(13), fill=colour)
    d.line([(x-60, y+24), (x+60, y+24)], fill=colour, width=1)
    d.text((x-46, y+30), "PORT AURELIO", font=font(11), fill=colour)

stamp(rx+150, 250, 92, "IMMIGRATION", "21 APR 2021", (168, 52, 52))
stamp(rx+340, 430, 86, "CUSTOMS", "03 JUN 2022", (52, 88, 140))
stamp(rx+140, 610, 96, "ENTRY VISA", "TWIN ISLES", (60, 118, 84))

# Stamp ink smudges
for i in range(24):
    ang = i * 0.9
    sx = rx+150 + int(80*math.cos(ang))
    sy = 250 + int(80*math.sin(ang))
    d.ellipse([sx-2, sy-2, sx+2, sy+2], fill=(190, 110, 100))

# Visa details panel
d.rectangle([rx, 760, W-58, 868], outline=(90, 90, 90), width=1)
d.text((rx+12, 770), "VISA CONDITION No. 44-C", font=font(15, True), fill=(40, 40, 40))
d.text((rx+12, 794), "Bearer may reside in the Port Aurelio", font=font(13), fill=(60, 60, 60))
d.text((rx+12, 814), "concession for 180 days; renewal requires", font=font(13), fill=(60, 60, 60))
d.text((rx+12, 834), "a sponsor's seal and a labour fee stamp.", font=font(13), fill=(60, 60, 60))
d.text((rx+12, 884), "FEE PAID  VRA 120  /  CIVIL RECORDS  /  2019", font=font(12), fill=(70, 70, 70))

out = os.environ.get('OUT', '/output/entry.png')
os.makedirs(os.path.dirname(out), exist_ok=True)
im.save(out, 'PNG', optimize=True)
print('wrote', out, os.path.getsize(out))
