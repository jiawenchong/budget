from common import save, FONT_TC
import math

W = H = 1000
cx, cy = 500, 500

def leaf(cx, cy, angle, r1, r2, size, color):
    a = math.radians(angle)
    x1 = cx + r1*math.cos(a); y1 = cy + r1*math.sin(a)
    x2 = cx + r2*math.cos(a); y2 = cy + r2*math.sin(a)
    nx, ny = -math.sin(a), math.cos(a)
    mx, my = (x1+x2)/2, (y1+y2)/2
    cxp1, cyp1 = mx + nx*size, my + ny*size
    cxp2, cyp2 = mx - nx*size, my - ny*size
    return f'<path d="M{x1:.1f},{y1:.1f} Q{cxp1:.1f},{cyp1:.1f} {x2:.1f},{y2:.1f} Q{cxp2:.1f},{cyp2:.1f} {x1:.1f},{y1:.1f} Z" fill="{color}"/>'

leaves = []
n = 28
for i in range(n):
    angle = i * 360 / n
    color = "#8a9a73" if i % 2 == 0 else "#a7b78e"
    leaves.append(leaf(cx, cy, angle, 330, 390, 22, color))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="#fbf6f1"/>
  <circle cx="{cx}" cy="{cy}" r="420" fill="none" stroke="#d8a9a3" stroke-width="2"/>
  <circle cx="{cx}" cy="{cy}" r="300" fill="none" stroke="#d8a9a3" stroke-width="1.5"/>

  <g>{''.join(leaves)}</g>

  <circle cx="{cx}" cy="{cy}" r="230" fill="#fbf6f1"/>

  <text x="{cx}" y="{cy-18}" font-family="{FONT_TC}" font-weight="700" font-size="58"
        letter-spacing="6" fill="#7a4b46" text-anchor="middle">BLOOM</text>
  <g>
    <line x1="{cx-60}" y1="{cy+18}" x2="{cx-20}" y2="{cy+18}" stroke="#d8a9a3" stroke-width="2"/>
    <text x="{cx}" y="{cy+28}" font-family="{FONT_TC}" font-weight="400" font-size="30"
          fill="#a7766f" text-anchor="middle">&amp; CO.</text>
    <line x1="{cx+20}" y1="{cy+18}" x2="{cx+60}" y2="{cy+18}" stroke="#d8a9a3" stroke-width="2"/>
  </g>
  <text x="{cx}" y="{cy+70}" font-family="{FONT_TC}" font-weight="400" font-size="20"
        letter-spacing="3" fill="#a7766f" text-anchor="middle">FLORALS · GIFTS · STATIONERY</text>
</svg>'''

save("02_logo_bloom", svg)
