from common import FONT_TC, FONT_TC_BLACK

W, H = 1000, 1400
CREAM = "#fbf3e3"
RED = "#8c1f1a"
GOLD = "#c9893c"
DARK = "#4a2d18"

def page_frame():
    return f'''
  <rect width="{W}" height="{H}" fill="{CREAM}"/>
  <rect x="26" y="26" width="{W-52}" height="{H-52}" fill="none" stroke="{GOLD}" stroke-width="2"/>
  '''

def header(title_cn, title_en, subtitle):
    return f'''
  <rect x="0" y="0" width="{W}" height="230" fill="{RED}"/>
  <path d="M0,230 L1000,230 L1000,246 L0,210 Z" fill="{RED}"/>
  <text x="500" y="110" font-family="{FONT_TC_BLACK}" font-weight="900" font-size="64" fill="#f3e3bd" text-anchor="middle">{title_cn}</text>
  <text x="500" y="158" font-family="{FONT_TC}" font-weight="700" font-size="30" letter-spacing="6" fill="{GOLD}" text-anchor="middle">{title_en}</text>
  <text x="500" y="195" font-family="{FONT_TC}" font-weight="400" font-size="20" letter-spacing="2" fill="#e9c98a" text-anchor="middle">{subtitle}</text>
  '''

def footer(page_no):
    return f'''
  <line x1="80" y1="{H-90}" x2="{W-80}" y2="{H-90}" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="500" y="{H-55}" font-family="{FONT_TC}" font-weight="400" font-size="20" letter-spacing="3" fill="{GOLD}" text-anchor="middle">龍鳳冰室 · LUNG FUNG CAFE</text>
  <text x="{W-80}" y="{H-55}" font-family="{FONT_TC}" font-weight="400" font-size="20" fill="{GOLD}" text-anchor="end">{page_no}</text>
  '''

def row(y, icon_svg, cn, en, desc, price):
    return f'''
  <g transform="translate(0,{y})">
    <circle cx="120" cy="60" r="68" fill="#f3e3c4"/>
    {icon_svg.replace('translate(', 'translate(' ) if False else f'<g transform="translate(120,60) scale(0.62)">{icon_svg}</g>'}
    <text x="232" y="42" font-family="{FONT_TC}" font-weight="700" font-size="34" fill="{DARK}">{cn}</text>
    <text x="232" y="74" font-family="{FONT_TC}" font-weight="400" font-size="21" letter-spacing="1" fill="{GOLD}">{en}</text>
    <text x="232" y="104" font-family="{FONT_TC}" font-weight="400" font-size="18" fill="#8a7460">{desc}</text>
    <text x="{W-90}" y="60" font-family="{FONT_TC}" font-weight="700" font-size="32" fill="{RED}" text-anchor="end">{price}</text>
    <line x1="100" y1="160" x2="{W-90}" y2="160" stroke="#e0cda0" stroke-width="1.5"/>
  </g>'''
