from common import save
from menu_common import W, H, page_frame, header, footer, row
from hk_icons import duck, char_siu_bowl, noodle_bowl

items = [
    (duck(), "燒鵲飯", "ROAST DUCK RICE", "Crispy skin roast duck on steamed rice", "$58"),
    (char_siu_bowl(), "叉燒飯", "CHAR SIU RICE", "Honey-glazed BBQ pork on steamed rice", "$52"),
    (noodle_bowl(), "雲吞麵", "WONTON NOODLES", "Shrimp wontons, egg noodles, clear broth", "$42"),
    (noodle_bowl(bowl="#a8431f", broth="#7a4a2e", noodle="#f3d98a"), "干炒牛河", "BEEF CHOW FUN", "Wok-fried rice noodles, beef &amp; bean sprouts", "$56"),
    (char_siu_bowl(rice="#e8e0c4", meat="#d8a13c", bowl="#8c1f1a"), "皮蛋瘦肉粥", "CENTURY EGG CONGEE", "Silky rice congee, pork &amp; preserved egg", "$38"),
    (noodle_bowl(bowl="#c9893c", broth="#e8c46a"), "星洲炒米", "SINGAPORE NOODLES", "Curry-spiced rice vermicelli, prawns &amp; egg", "$48"),
]

rows = "".join(row(230 + i*180, icon, cn, en, desc, price) for i, (icon, cn, en, desc, price) in enumerate(items))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {page_frame()}
  {header("粥麵飯 · 燒味", "RICE, NOODLES &amp; ROAST MEATS", "WOK-FRIED · SLOW-ROASTED · COMFORT BOWLS")}
  {rows}
  {footer("02")}
</svg>'''

save("09_menu_rice_roast", svg)
