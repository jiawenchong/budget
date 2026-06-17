from common import save
from menu_common import W, H, page_frame, header, footer, row
from hk_icons import harkau, siumai, cheung_fun, turnip_cake, bao

items = [
    (harkau(), "蝦餃", "HAR GOW", "Steamed shrimp dumpling, bamboo shoot", "$38"),
    (siumai(), "燒賣", "SIU MAI", "Pork &amp; shrimp dumpling, crab roe top", "$35"),
    (cheung_fun(), "腸粉", "CHEUNG FUN", "Silky rice noodle roll, soy &amp; sesame", "$32"),
    (bao(), "叉燒包", "CHAR SIU BAO", "Fluffy steamed bun, BBQ pork filling", "$30"),
    (turnip_cake(), "蘿蔔糕", "TURNIP CAKE", "Pan-fried radish cake, XO sauce", "$28"),
    (siumai(skin="#e8c46a", shrimp="#c0392b"), "鳳爪", "PHOENIX TALONS", "Braised chicken feet, black bean sauce", "$34"),
]

rows = "".join(row(230 + i*180, icon, cn, en, desc, price) for i, (icon, cn, en, desc, price) in enumerate(items))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {page_frame()}
  {header("點 心", "DIM SUM", "STEAMED &amp; PAN-FRIED · SERVED ALL DAY")}
  {rows}
  {footer("01")}
</svg>'''

save("08_menu_dimsum", svg)
