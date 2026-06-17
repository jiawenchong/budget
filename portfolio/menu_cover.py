from common import save, FONT_TC, FONT_TC_BLACK
from hk_icons import g, teapot, steamer, duck, milk_tea

W, H = 1000, 1400

def corner_motif(x, y, rot):
    return f'''
    <g transform="translate({x},{y}) rotate({rot})">
      <path d="M0,0 L90,0 L90,14 L14,14 L14,90 L0,90 Z" fill="#d8a13c"/>
      <circle cx="40" cy="40" r="6" fill="#d8a13c"/>
    </g>'''

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="redbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8c1f1a"/>
      <stop offset="1" stop-color="#5e120f"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#redbg)"/>

  <rect x="36" y="36" width="{W-72}" height="{H-72}" fill="none" stroke="#d8a13c" stroke-width="3"/>
  {corner_motif(36, 36, 0)}
  {corner_motif(W-36, 36, 90)}
  {corner_motif(W-36, H-36, 180)}
  {corner_motif(36, H-36, 270)}

  <text x="500" y="170" font-family="{FONT_TC}" font-weight="400" font-size="26" letter-spacing="8" fill="#e9c98a" text-anchor="middle">EST. 1968 · HONG KONG STYLE</text>

  <text x="500" y="330" font-family="{FONT_TC_BLACK}" font-weight="900" font-size="150" fill="#f3e3bd" text-anchor="middle">龍鳳冰室</text>
  <text x="500" y="400" font-family="{FONT_TC}" font-weight="700" font-size="42" letter-spacing="10" fill="#d8a13c" text-anchor="middle">LUNG FUNG CAFE</text>

  <line x1="280" y1="450" x2="720" y2="450" stroke="#d8a13c" stroke-width="2"/>

  {g(290, 700, 1.05, teapot())}
  {g(500, 720, 1.0, steamer())}
  {g(710, 700, 0.95, duck())}
  {g(395, 920, 0.85, milk_tea())}
  {g(610, 920, 0.85, milk_tea())}

  <line x1="280" y1="1080" x2="720" y2="1080" stroke="#d8a13c" stroke-width="2"/>

  <text x="500" y="1170" font-family="{FONT_TC}" font-weight="700" font-size="50" letter-spacing="4" fill="#f3e3bd" text-anchor="middle">港 式 茶 餐 廳</text>
  <text x="500" y="1220" font-family="{FONT_TC}" font-weight="400" font-size="26" letter-spacing="3" fill="#e9c98a" text-anchor="middle">DIM SUM · RICE &amp; NOODLES · ROAST MEATS · DRINKS</text>

  <text x="500" y="1320" font-family="{FONT_TC}" font-weight="400" font-size="22" fill="#c79a5c" text-anchor="middle">SHOP 8, KING&#39;S ROAD, NORTH POINT, HONG KONG</text>
</svg>'''

save("07_menu_cover", svg)
