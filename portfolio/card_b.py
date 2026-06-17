from common import save, FONT_TC
import math

CW, CH = 1000, 600
W = CW*2 + 160 + 200
H = CH + 200
ox1, oy = 100, 100
ox2 = ox1 + CW + 160

def shadow(x, y):
    return f'<rect x="{x+6}" y="{y+10}" width="{CW}" height="{CH}" rx="22" fill="#000" opacity="0.10"/>'

def leaf(cx, cy, angle, r1, r2, size, color):
    a = math.radians(angle)
    x1 = cx + r1*math.cos(a); y1 = cy + r1*math.sin(a)
    x2 = cx + r2*math.cos(a); y2 = cy + r2*math.sin(a)
    nx, ny = -math.sin(a), math.cos(a)
    mx, my = (x1+x2)/2, (y1+y2)/2
    p1 = (mx + nx*size, my + ny*size)
    p2 = (mx - nx*size, my - ny*size)
    return f'<path d="M{x1:.1f},{y1:.1f} Q{p1[0]:.1f},{p1[1]:.1f} {x2:.1f},{y2:.1f} Q{p2[0]:.1f},{p2[1]:.1f} {x1:.1f},{y1:.1f} Z" fill="{color}"/>'

def corner_sprig(cx, cy, base_angle):
    parts = []
    for i in range(6):
        ang = base_angle + i*7
        r1 = 0 + i*8
        r2 = r1 + 46
        color = "#8a9a73" if i % 2 == 0 else "#a7b78e"
        parts.append(leaf(cx, cy, ang, r1, r2, 14, color))
    return "".join(parts)

def wreath(cx, cy, r1, r2):
    parts = []
    n = 22
    for i in range(n):
        ang = i*360/n
        color = "#8a9a73" if i % 2 == 0 else "#a7b78e"
        parts.append(leaf(cx, cy, ang, r1, r2, 16, color))
    return "".join(parts)

front = f'''
  {shadow(ox1, oy)}
  <rect x="{ox1}" y="{oy}" width="{CW}" height="{CH}" rx="22" fill="#fbf6f1"/>
  <rect x="{ox1}" y="{oy}" width="{CW}" height="{CH}" rx="22" fill="none" stroke="#e7cfc8" stroke-width="1.5"/>
  <g transform="translate({ox1+90},{oy+90}) rotate(200)">{corner_sprig(0,0,0)}</g>
  <g transform="translate({ox1+CW-90},{oy+CH-90}) rotate(20)">{corner_sprig(0,0,0)}</g>
  <text x="{ox1+CW/2}" y="{oy+250}" font-family="{FONT_TC}" font-weight="700" font-size="46" letter-spacing="4" fill="#7a4b46" text-anchor="middle">Isabelle Tran</text>
  <text x="{ox1+CW/2}" y="{oy+292}" font-family="{FONT_TC}" font-weight="400" font-size="22" letter-spacing="3" fill="#a7766f" text-anchor="middle">FOUNDER &amp; FLORAL DESIGNER</text>
  <line x1="{ox1+CW/2-90}" y1="{oy+330}" x2="{ox1+CW/2+90}" y2="{oy+330}" stroke="#d8a9a3" stroke-width="1.5"/>
  <text x="{ox1+CW/2}" y="{oy+400}" font-family="{FONT_TC}" font-weight="400" font-size="22" fill="#5c4a46" text-anchor="middle">+852 6234 8890</text>
  <text x="{ox1+CW/2}" y="{oy+436}" font-family="{FONT_TC}" font-weight="400" font-size="22" fill="#5c4a46" text-anchor="middle">hello@bloomandco.hk</text>
  <text x="{ox1+CW/2}" y="{oy+472}" font-family="{FONT_TC}" font-weight="400" font-size="22" fill="#5c4a46" text-anchor="middle">@bloomandco</text>
'''

back = f'''
  {shadow(ox2, oy)}
  <rect x="{ox2}" y="{oy}" width="{CW}" height="{CH}" rx="22" fill="#cfd9c0"/>
  <g transform="translate({ox2+CW/2},{oy+CH/2})">{wreath(0,0,150,185)}</g>
  <text x="{ox2+CW/2}" y="{oy+CH/2-10}" font-family="{FONT_TC}" font-weight="700" font-size="40" letter-spacing="5" fill="#5c4a36" text-anchor="middle">BLOOM</text>
  <text x="{ox2+CW/2}" y="{oy+CH/2+28}" font-family="{FONT_TC}" font-weight="400" font-size="22" letter-spacing="2" fill="#6b5a3c" text-anchor="middle">&amp; CO.</text>
'''

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="#f1ece6"/>
  {front}
  {back}
</svg>'''

save("04_card_bloom", svg)
