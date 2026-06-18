from common import save, FONT_TC, FONT_TC_BLACK
from realistic_scenes import register_defs
from flatlay_dishes import flatlay_spread

W, H = 1600, 2220
CREAM = "#fbf3e3"
RED = "#8c1f1a"
GOLD = "#c9893c"
DARK = "#4a2d18"

def corner_motif(x, y, rot):
    return f'''<g transform="translate({x},{y}) rotate({rot})">
      <path d="M0,0 L90,0 L90,14 L14,14 L14,90 L0,90 Z" fill="{GOLD}"/>
      <circle cx="40" cy="40" r="6" fill="{GOLD}"/></g>'''

def col_title(x, y, w, cn, en):
    return f'''
    <rect x="{x}" y="{y}" width="{w}" height="64" fill="{RED}"/>
    <text x="{x+24}" y="{y+42}" font-family="{FONT_TC_BLACK}" font-weight="900" font-size="28" fill="#f3e3bd">{cn}</text>
    <text x="{x+w-20}" y="{y+42}" font-family="{FONT_TC}" font-weight="700" font-size="16" letter-spacing="2" fill="{GOLD}" text-anchor="end">{en}</text>
    '''

def item_row(x, y, w, cn, en, desc, price):
    return f'''
    <g transform="translate({x},{y})">
      <text x="0" y="0" font-family="{FONT_TC}" font-weight="700" font-size="24" fill="{DARK}">{cn}</text>
      <text x="{w}" y="0" font-family="{FONT_TC}" font-weight="700" font-size="22" fill="{RED}" text-anchor="end">{price}</text>
      <text x="0" y="26" font-family="{FONT_TC}" font-weight="400" font-size="14" letter-spacing="1" fill="{GOLD}">{en}</text>
      <text x="0" y="49" font-family="{FONT_TC}" font-weight="400" font-size="13" fill="#8a7460">{desc}</text>
      <line x1="0" y1="68" x2="{w}" y2="68" stroke="#e0cda0" stroke-width="1.5"/>
    </g>'''

def column(x, y, w, cn, en, items):
    parts = [col_title(x, y, w, cn, en)]
    list_y = y + 100
    for i, (cn_, en_, desc, price) in enumerate(items):
        parts.append(item_row(x, list_y + i * 92, w, cn_, en_, desc, price))
    return "".join(parts)

dimsum_items = [
    ("蝦餃", "HAR GOW", "Steamed shrimp dumpling, bamboo shoot", "$38"),
    ("燒賣", "SIU MAI", "Pork &amp; shrimp dumpling, crab roe top", "$35"),
    ("腸粉", "CHEUNG FUN", "Silky rice noodle roll, soy &amp; sesame", "$32"),
    ("叉燒包", "CHAR SIU BAO", "Fluffy steamed bun, BBQ pork filling", "$30"),
    ("蘿蔔糕", "TURNIP CAKE", "Pan-fried radish cake, XO sauce", "$28"),
    ("鳳爪", "PHOENIX TALONS", "Braised chicken feet, black bean sauce", "$34"),
]

rice_items = [
    ("燒鵲飯", "ROAST DUCK RICE", "Crispy skin roast duck on steamed rice", "$58"),
    ("叉燒飯", "CHAR SIU RICE", "Honey-glazed BBQ pork on steamed rice", "$52"),
    ("雲吞麵", "WONTON NOODLES", "Shrimp wontons, egg noodles, clear broth", "$42"),
    ("干炒牛河", "BEEF CHOW FUN", "Wok-fried rice noodles, beef &amp; bean sprouts", "$56"),
    ("皮蛋瘦肉粥", "CENTURY EGG CONGEE", "Silky rice congee, pork &amp; preserved egg", "$38"),
    ("星洲炒米", "SINGAPORE NOODLES", "Curry-spiced rice vermicelli, prawns &amp; egg", "$48"),
]

drinks_items = [
    ("港式奶茶", "HK MILK TEA", "Silk-stocking brewed black tea &amp; evaporated milk", "$22"),
    ("檸檬茶", "LEMON TEA", "Hot or iced, fresh lemon slices", "$20"),
    ("鴛鴦", "YIN YEUNG", "Coffee &amp; tea blend, evaporated milk", "$24"),
    ("蛋撻", "EGG TART", "Flaky crust, warm silky custard", "$14"),
    ("楊枝甘露", "MANGO SAGO POMELO", "Chilled mango cream, sago &amp; pomelo", "$32"),
    ("凍檸水", "ICED LEMON WATER", "Refreshing iced water, fresh lemon", "$18"),
]

hero_x, hero_y, hero_w, hero_h = 60, 290, W - 120, 1000
spread = flatlay_spread(hero_w, hero_h)

col_w = (W - 120 - 2 * 50) / 3
col_xs = [60, 60 + col_w + 50, 60 + 2 * (col_w + 50)]
cols_top = hero_y + hero_h + 50

body = "".join([
    column(col_xs[0], cols_top, col_w, "點 心", "DIM SUM", dimsum_items),
    column(col_xs[1], cols_top, col_w, "粥麵飯 · 燒味", "RICE &amp; ROAST", rice_items),
    column(col_xs[2], cols_top, col_w, "飲品 · 甜品", "DRINKS &amp; DESSERTS", drinks_items),
])

footer_y = cols_top + 100 + 6 * 92 + 40

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>{register_defs()}</defs>
  <rect width="{W}" height="{H}" fill="{CREAM}"/>
  <rect x="26" y="26" width="{W-52}" height="{H-52}" fill="none" stroke="{GOLD}" stroke-width="2"/>
  {corner_motif(36, 36, 0)}
  {corner_motif(W-36, 36, 90)}
  {corner_motif(W-36, H-36, 180)}
  {corner_motif(36, H-36, 270)}

  <rect x="60" y="60" width="{W-120}" height="200" fill="{RED}"/>
  <text x="{W/2}" y="125" font-family="{FONT_TC}" font-weight="400" font-size="22" letter-spacing="6" fill="#e9c98a" text-anchor="middle">EST. 1968 · HONG KONG STYLE</text>
  <text x="{W/2}" y="205" font-family="{FONT_TC_BLACK}" font-weight="900" font-size="92" fill="#f3e3bd" text-anchor="middle">龍鳳冰室 LUNG FUNG CAFE</text>

  <g transform="translate({hero_x},{hero_y})">
    <clipPath id="heroClip"><rect x="0" y="0" width="{hero_w}" height="{hero_h}" rx="18"/></clipPath>
    <g clip-path="url(#heroClip)">{spread}</g>
    <rect x="0" y="0" width="{hero_w}" height="{hero_h}" rx="18" fill="none" stroke="{GOLD}" stroke-width="4"/>
  </g>

  {body}

  <line x1="80" y1="{footer_y}" x2="{W-80}" y2="{footer_y}" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="{W/2}" y="{footer_y+50}" font-family="{FONT_TC}" font-weight="700" font-size="26" letter-spacing="3" fill="{RED}" text-anchor="middle">港 式 茶 餐 廳</text>
  <text x="{W/2}" y="{footer_y+90}" font-family="{FONT_TC}" font-weight="400" font-size="19" fill="{DARK}" text-anchor="middle">SHOP 8, KING&#39;S ROAD, NORTH POINT, HONG KONG · +852 2345 6789</text>
</svg>'''

save("12_menu_flatlay", svg, scale=1.5)
print(W, H, footer_y)
