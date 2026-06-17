from common import save, FONT_TC, FONT_TC_BLACK
from realistic_scenes import dimsum_scene, roast_scene, drinks_scene, register_defs

W, H = 1600, 2650
CREAM = "#fbf3e3"
RED = "#8c1f1a"
GOLD = "#c9893c"
DARK = "#4a2d18"

def corner_motif(x, y, rot):
    return f'''<g transform="translate({x},{y}) rotate({rot})">
      <path d="M0,0 L90,0 L90,14 L14,14 L14,90 L0,90 Z" fill="{GOLD}"/>
      <circle cx="40" cy="40" r="6" fill="{GOLD}"/></g>'''

def section_title(y, cn, en, sub):
    return f'''
    <rect x="60" y="{y}" width="{W-120}" height="78" fill="{RED}"/>
    <path d="M60,{y+78} L{W-60},{y+78} L{W-60},{y+92} L60,{y+64} Z" fill="{RED}"/>
    <text x="150" y="{y+52}" font-family="{FONT_TC_BLACK}" font-weight="900" font-size="44" fill="#f3e3bd">{cn}</text>
    <text x="{W-150}" y="{y+38}" font-family="{FONT_TC}" font-weight="700" font-size="26" letter-spacing="3" fill="{GOLD}" text-anchor="end">{en}</text>
    <text x="{W-150}" y="{y+66}" font-family="{FONT_TC}" font-weight="400" font-size="17" letter-spacing="1" fill="#e9c98a" text-anchor="end">{sub}</text>
    '''

def item_row(x, y, w, cn, en, desc, price):
    return f'''
    <g transform="translate({x},{y})">
      <text x="0" y="0" font-family="{FONT_TC}" font-weight="700" font-size="29" fill="{DARK}">{cn}</text>
      <text x="0" y="30" font-family="{FONT_TC}" font-weight="400" font-size="17" letter-spacing="1" fill="{GOLD}">{en}</text>
      <text x="0" y="56" font-family="{FONT_TC}" font-weight="400" font-size="15" fill="#8a7460">{desc}</text>
      <text x="{w}" y="20" font-family="{FONT_TC}" font-weight="700" font-size="27" fill="{RED}" text-anchor="end">{price}</text>
      <line x1="0" y1="78" x2="{w}" y2="78" stroke="#e0cda0" stroke-width="1.5"/>
    </g>'''

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

def section(y_top, cn, en, sub, items, scene_svg):
    parts = [section_title(y_top, cn, en, sub)]
    list_y = y_top + 130
    for i, (cn_, en_, desc, price) in enumerate(items):
        parts.append(item_row(740, list_y + i*90, 720, cn_, en_, desc, price))
    parts.append(f'<g>{scene_svg}</g>')
    return "".join(parts)

SEC_H = 700
sec1_top = 300
sec2_top = sec1_top + SEC_H
sec3_top = sec2_top + SEC_H

dimsum_svg = dimsum_scene(390, sec1_top + 420)
roast_svg = roast_scene(390, sec2_top + 440)
drinks_svg = drinks_scene(390, sec3_top + 430)

body = "".join([
    section(sec1_top, "點 心", "DIM SUM", "STEAMED &amp; PAN-FRIED", dimsum_items, dimsum_svg),
    section(sec2_top, "粥麵飯 · 燒味", "RICE, NOODLES &amp; ROAST MEATS", "WOK-FRIED · SLOW-ROASTED", rice_items, roast_svg),
    section(sec3_top, "飲品 · 甜品", "DRINKS &amp; DESSERTS", "HK STYLE BEVERAGES", drinks_items, drinks_svg),
])

footer_y = sec3_top + SEC_H
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

  {body}

  <line x1="80" y1="{footer_y+40}" x2="{W-80}" y2="{footer_y+40}" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="{W/2}" y="{footer_y+90}" font-family="{FONT_TC}" font-weight="700" font-size="26" letter-spacing="3" fill="{RED}" text-anchor="middle">港 式 茶 餐 廳</text>
  <text x="{W/2}" y="{footer_y+130}" font-family="{FONT_TC}" font-weight="400" font-size="19" fill="{DARK}" text-anchor="middle">SHOP 8, KING&#39;S ROAD, NORTH POINT, HONG KONG · +852 2345 6789</text>
</svg>'''

save("11_menu_full_page", svg, scale=1.5)
print(W, H)
