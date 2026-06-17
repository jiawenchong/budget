from common import save
from menu_common import W, H, page_frame, header, footer, row
from hk_icons import milk_tea, egg_tart

def mango_sago():
    return '''
    <ellipse cx="0" cy="20" rx="48" ry="26" fill="#e8b84a"/>
    <circle cx="-14" cy="0" r="9" fill="#fbe8c8"/>
    <circle cx="10" cy="-6" r="9" fill="#fbe8c8"/>
    <circle cx="0" cy="10" r="9" fill="#fbe8c8"/>
    <path d="M -40,10 Q 0,-26 40,10" fill="none" stroke="#d8902c" stroke-width="4"/>
    '''

def lemon_tea():
    return '''
    <path d="M -30,-30 L -22,40 L 22,40 L 30,-30 Z" fill="#f3e3bd"/>
    <ellipse cx="0" cy="-30" rx="30" ry="8" fill="#9c7a2e"/>
    <circle cx="-8" cy="0" r="10" fill="#e8c94a"/>
    <circle cx="10" cy="14" r="9" fill="#e8c94a"/>
    '''

def yinyeung():
    return '''
    <ellipse cx="0" cy="48" rx="46" ry="10" fill="#8c1f1a"/>
    <path d="M -30,-28 L -22,40 L 22,40 L 30,-28 Z" fill="#f3e3bd"/>
    <path d="M -30,-28 a 30,10 0 0 0 60,0 Z" fill="#5a3a22"/>
    <path d="M -10,-28 a 30,10 0 0 0 20,0 Z" fill="#c08a4e"/>
    '''

def lemon_water():
    return '''
    <path d="M -26,-32 L -20,40 L 20,40 L 26,-32 Z" fill="#dff0e8" opacity="0.85"/>
    <ellipse cx="0" cy="-32" rx="26" ry="7" fill="#bfe0d0"/>
    <circle cx="0" cy="6" r="10" fill="#e8c94a"/>
    <circle cx="-12" cy="-8" r="4" fill="#ffffff"/>
    <circle cx="10" cy="20" r="4" fill="#ffffff"/>
    '''

items = [
    (milk_tea(), "港式奶茶", "HK MILK TEA", "Silk-stocking brewed black tea &amp; evaporated milk", "$22"),
    (lemon_tea(), "檸檬茶", "LEMON TEA", "Hot or iced, fresh lemon slices", "$20"),
    (yinyeung(), "鴛鴦", "YIN YEUNG", "Coffee &amp; tea blend, evaporated milk", "$24"),
    (egg_tart(), "蛋撻", "EGG TART", "Flaky crust, warm silky custard", "$14"),
    (mango_sago(), "楊枝甘露", "MANGO SAGO POMELO", "Chilled mango cream, sago &amp; pomelo", "$32"),
    (lemon_water(), "凍檸水", "ICED LEMON WATER", "Refreshing iced water, fresh lemon", "$18"),
]

rows = "".join(row(230 + i*180, icon, cn, en, desc, price) for i, (icon, cn, en, desc, price) in enumerate(items))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {page_frame()}
  {header("飲品 · 甜品", "DRINKS &amp; DESSERTS", "HK STYLE BEVERAGES &amp; SWEET TREATS")}
  {rows}
  {footer("03")}
</svg>'''

save("10_menu_drinks", svg)
