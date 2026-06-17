from common import save, FONT_TC

CW, CH = 1000, 600
GAP = 160
W = CW*2 + GAP + 200
H = CH + 200
ox1, oy = 100, 100
ox2 = ox1 + CW + GAP

def shadow(x, y):
    return f'<rect x="{x+6}" y="{y+10}" width="{CW}" height="{CH}" rx="22" fill="#000" opacity="0.12"/>'

mini_mark = lambda x, y, scale=1: f'''
  <g transform="translate({x},{y}) scale({scale})">
    <polygon points="60,0 20,70 100,70" fill="#c9a45c"/>
    <polygon points="60,0 50,20 70,20" fill="#f3e3bd"/>
  </g>'''

front = f'''
  {shadow(ox1, oy)}
  <rect x="{ox1}" y="{oy}" width="{CW}" height="{CH}" rx="22" fill="#fbfaf7"/>
  <rect x="{ox1}" y="{oy}" width="{CW}" height="{CH}" rx="22" fill="none" stroke="#e3ddcf" stroke-width="1.5"/>
  {mini_mark(ox1+60, oy+60, 0.8)}
  <text x="{ox1+220}" y="{oy+108}" font-family="{FONT_TC}" font-weight="700" font-size="34" letter-spacing="3" fill="#16335c">MERIDIAN</text>
  <line x1="{ox1+60}" y1="{oy+260}" x2="{ox1+260}" y2="{oy+260}" stroke="#c9a45c" stroke-width="2"/>
  <text x="{ox1+60}" y="{oy+330}" font-family="{FONT_TC}" font-weight="700" font-size="40" fill="#16335c">Adrian Wells</text>
  <text x="{ox1+60}" y="{oy+372}" font-family="{FONT_TC}" font-weight="400" font-size="24" letter-spacing="2" fill="#9a874f">SENIOR STRATEGY CONSULTANT</text>
  <text x="{ox1+60}" y="{oy+450}" font-family="{FONT_TC}" font-weight="400" font-size="22" fill="#445064">+852 9123 4567</text>
  <text x="{ox1+60}" y="{oy+486}" font-family="{FONT_TC}" font-weight="400" font-size="22" fill="#445064">adrian@meridian-co.com</text>
  <text x="{ox1+60}" y="{oy+522}" font-family="{FONT_TC}" font-weight="400" font-size="22" fill="#445064">meridian-co.com</text>
'''

back = f'''
  {shadow(ox2, oy)}
  <rect x="{ox2}" y="{oy}" width="{CW}" height="{CH}" rx="22" fill="#16335c"/>
  {mini_mark(ox2+CW/2-60, oy+220, 1.0)}
  <text x="{ox2+CW/2}" y="{oy+390}" font-family="{FONT_TC}" font-weight="700" font-size="38" letter-spacing="6" fill="#f3e3bd" text-anchor="middle">MERIDIAN</text>
  <text x="{ox2+CW/2}" y="{oy+426}" font-family="{FONT_TC}" font-weight="400" font-size="18" letter-spacing="3" fill="#c9a45c" text-anchor="middle">STRATEGY · DESIGN · GROWTH</text>
'''

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="#eeece6"/>
  {front}
  {back}
</svg>'''

save("03_card_meridian", svg)
