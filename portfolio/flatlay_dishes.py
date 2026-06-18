import math
from realistic_scenes import _grad, shadow_ellipse

g_wood = _grad("g_wood", "linear", [(0, "#4a3018", 1), (1, "#241509", 1)], x1="0", y1="0", x2="1", y2="1")
g_vignette = _grad("g_vignette", "radial", [(0, "#000000", 0), (1, "#000000", 0.4)], cx="0.5", cy="0.5", r="0.75")
g_plate = _grad("g_plate", "radial", [(0, "#ffffff", 1), (1, "#e2ddd2", 1)], cx="0.4", cy="0.35", r="0.85")
g_steamer_out = _grad("g_steamer_out", "linear", [(0, "#c9974f", 1), (1, "#8a5a28", 1)], x1="0", y1="0", x2="0", y2="1")
g_steamer_in = _grad("g_steamer_in", "radial", [(0, "#fff6e0", 1), (1, "#d9b06a", 1)], cx="0.5", cy="0.4", r="0.75")
g_har = _grad("g_har2", "radial", [(0, "#fffaf2", 0.95), (0.7, "#fce8d6", 0.95), (1, "#e8c49c", 0.9)], cx="0.35", cy="0.3", r="0.8")
g_shrimp = _grad("g_shrimp2", "linear", [(0, "#ffb37a", 1), (1, "#e8773f", 1)], x1="0", y1="0", x2="1", y2="1")
g_siu_skin = _grad("g_siu_skin2", "linear", [(0, "#ffe48a", 1), (1, "#e8b73c", 1)], x1="0", y1="0", x2="0", y2="1")
g_cheung = _grad("g_cheung", "linear", [(0, "#f8f2e0", 1), (1, "#e8dcc0", 1)], x1="0", y1="0", x2="0", y2="1")
g_bao = _grad("g_bao", "radial", [(0, "#fffaf0", 1), (1, "#e8dcb8", 1)], cx="0.4", cy="0.35", r="0.85")
g_turnip = _grad("g_turnip", "linear", [(0, "#e8b860", 1), (1, "#c0823a", 1)], x1="0", y1="0", x2="0", y2="1")
g_feet = _grad("g_feet", "linear", [(0, "#9c4422", 1), (1, "#5e2208", 1)], x1="0", y1="0", x2="1", y2="1")
g_duck2 = _grad("g_duck3", "linear", [(0, "#c2632a", 1), (1, "#5e2208", 1)], x1="0", y1="0", x2="1", y2="1")
g_broth = _grad("g_broth", "radial", [(0, "#f3d488", 1), (1, "#c98a3c", 1)], cx="0.4", cy="0.35", r="0.85")
g_congee = _grad("g_congee", "radial", [(0, "#fffdf6", 1), (1, "#ecdfc0", 1)], cx="0.4", cy="0.35", r="0.85")
g_tea_top = _grad("g_tea_top", "radial", [(0, "#a8703c", 1), (1, "#5a3318", 1)], cx="0.4", cy="0.35", r="0.85")
g_crust2 = _grad("g_crust2", "linear", [(0, "#eccb84", 1), (1, "#c0823a", 1)], x1="0", y1="0", x2="0", y2="1")
g_custard2 = _grad("g_custard2", "radial", [(0, "#fff0b8", 1), (1, "#eba83c", 1)], cx="0.38", cy="0.32", r="0.75")
g_mango = _grad("g_mango", "radial", [(0, "#ffd98a", 1), (1, "#e8852c", 1)], cx="0.4", cy="0.35", r="0.85")


def wood_table(w, h):
    grain = "".join(
        f'<path d="M0,{y} q{w/4:.0f},{4 if i % 2 == 0 else -4} {w/2:.0f},0 t{w/2:.0f},0" '
        f'stroke="#1c1108" stroke-width="1.4" opacity="0.2" fill="none"/>'
        for i, y in enumerate(range(20, h, 26))
    )
    return f'''
    <rect x="0" y="0" width="{w}" height="{h}" fill="{g_wood}"/>
    {grain}
    <rect x="0" y="0" width="{w}" height="{h}" fill="{g_vignette}"/>
    '''


def tick_ring(r_in, r_out, n=28, color="#6e4118", width=2.4, opacity=0.4):
    ticks = []
    for i in range(n):
        a = 2 * math.pi * i / n
        x0, y0 = r_in * math.cos(a), r_in * math.sin(a)
        x1, y1 = r_out * math.cos(a), r_out * math.sin(a)
        ticks.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{color}" stroke-width="{width}" opacity="{opacity}"/>')
    return "".join(ticks)


def plate_top(r=150, rx=None, ry=None):
    rx = rx or r
    ry = ry or r
    return f'''
    {shadow_ellipse(0, ry * 0.1, rx * 1.05, ry * 0.32, 0.28)}
    <ellipse cx="0" cy="0" rx="{rx}" ry="{ry}" fill="{g_plate}"/>
    <ellipse cx="0" cy="0" rx="{rx * 0.86}" ry="{ry * 0.86}" fill="none" stroke="#d4cfc4" stroke-width="2.5" opacity="0.7"/>
    '''


def steamer_top(r=150):
    return f'''
    {shadow_ellipse(0, r * 0.1, r * 1.08, r * 0.32, 0.3)}
    <circle cx="0" cy="0" r="{r}" fill="{g_steamer_out}"/>
    {tick_ring(r * 0.78, r * 0.98)}
    <circle cx="0" cy="0" r="{r * 0.78}" fill="{g_steamer_in}" stroke="#7a4d22" stroke-width="3"/>
    '''


def bowl_top(r=150, rim="#8c1f1a", fill=g_broth):
    return f'''
    {shadow_ellipse(0, r * 0.1, r * 1.05, r * 0.3, 0.28)}
    <circle cx="0" cy="0" r="{r}" fill="{rim}"/>
    <circle cx="0" cy="0" r="{r * 0.82}" fill="{fill}"/>
    '''


def cup_top(r=130, rim="#f3e3bd", fill=g_tea_top):
    return f'''
    {shadow_ellipse(0, r * 0.1, r * 1.05, r * 0.3, 0.26)}
    <circle cx="0" cy="0" r="{r}" fill="{rim}"/>
    <circle cx="0" cy="0" r="{r * 0.84}" fill="{fill}"/>
    <path d="M{-r*0.5:.0f},{-r*0.3:.0f} A{r*0.7:.0f},{r*0.5:.0f} 0 0 1 {r*0.15:.0f},{-r*0.6:.0f}" fill="none" stroke="#f3e3bd" stroke-width="6" opacity="0.4"/>
    '''


def har_gow_top(x, y, rot, s=1.0):
    pleats = "".join(
        f'<path d="M{px},6 Q{px+8},-14 {px+16},6" stroke="#d8b88a" stroke-width="1.8" fill="none" opacity="0.6"/>'
        for px in range(-26, 20, 10)
    )
    return f'''<g transform="translate({x},{y}) rotate({rot}) scale({s})">
      <path d="M-30,6 C-30,-18 30,-18 30,6 C30,20 -30,20 -30,6 Z" fill="{g_har}" stroke="#dcb98a" stroke-width="1.2"/>
      <ellipse cx="0" cy="7" rx="17" ry="7.5" fill="{g_shrimp}"/>
      {pleats}
      <ellipse cx="-9" cy="-6" rx="7" ry="3.5" fill="#ffffff" opacity="0.5"/>
    </g>'''


def siu_mai_top(x, y, s=1.0):
    return f'''<g transform="translate({x},{y}) scale({s})">
      <path d="M-24,10 L-20,-16 L20,-16 L24,10 Z" fill="{g_siu_skin}"/>
      <ellipse cx="0" cy="-16" rx="7" ry="5.5" fill="#e8632f"/>
      <circle cx="-10" cy="6" r="3.5" fill="#e89a2c"/>
      <circle cx="7" cy="7" r="3.5" fill="#e89a2c"/>
      <ellipse cx="-7" cy="-7" rx="5.5" ry="2.8" fill="#fff6cc" opacity="0.5"/>
    </g>'''


def har_gow_cluster(s=1.0):
    return f'''<g transform="scale({s})">
      {har_gow_top(-38, -14, -8)}
      {har_gow_top(36, -10, 9)}
      {har_gow_top(0, 36, 2)}
      <g transform="translate(40,42)">{siu_mai_top(0,0,0.92)}</g>
      <g transform="translate(-42,40)">{siu_mai_top(0,0,0.9)}</g>
    </g>'''


def siu_mai_cluster(s=1.0):
    return f'''<g transform="scale({s})">
      {siu_mai_top(-34, -10)}
      {siu_mai_top(34, -8, )}
      {siu_mai_top(0, 38)}
      <g transform="translate(0,-44)">{har_gow_top(0,0,4,0.85)}</g>
    </g>'''


def cheung_fun_top(x, y, rot, s, soy="#4a2a12"):
    return f'''<g transform="translate({x},{y}) rotate({rot}) scale({s})">
      <rect x="-58" y="-22" width="116" height="44" rx="20" fill="{g_cheung}"/>
      <path d="M-50,-12 Q0,-20 50,-12" stroke="#e8dcc0" stroke-width="2" fill="none" opacity="0.6"/>
      <path d="M-22,-4 q7,9 0,18 M4,-5 q7,9 0,18 M28,-6 q7,9 0,18" stroke="{soy}" stroke-width="3.5" stroke-linecap="round" opacity="0.85"/>
      <circle cx="-34" cy="6" r="2.2" fill="#ffffff" opacity="0.8"/>
      <circle cx="14" cy="9" r="2.2" fill="#ffffff" opacity="0.8"/>
      <circle cx="40" cy="2" r="2.2" fill="#5a8a3c" opacity="0.7"/>
    </g>'''


def cheung_fun_plate(s=1.0):
    return f'''<g transform="scale({s})">
      {cheung_fun_top(-4, -26, -3, 1.0)}
      {cheung_fun_top(2, 14, 4, 1.0)}
      {cheung_fun_top(8, 50, -2, 0.95)}
    </g>'''


def bao_top(x, y, s=1.0):
    return f'''<g transform="translate({x},{y}) scale({s})">
      <circle cx="0" cy="0" r="44" fill="{g_bao}"/>
      <circle cx="0" cy="0" r="44" fill="none" stroke="#e8dcc0" stroke-width="2" opacity="0.6"/>
      <circle cx="0" cy="0" r="5" fill="#d8c89c"/>
      <path d="M-28,10 q28,13 56,0" stroke="#e8dcc0" stroke-width="2" fill="none" opacity="0.5"/>
      <path d="M-20,-20 q20,-10 40,0" stroke="#e8dcc0" stroke-width="2" fill="none" opacity="0.45"/>
    </g>'''


def bao_cluster(s=1.0):
    return f'''<g transform="scale({s})">
      {bao_top(-44, -10)}
      {bao_top(40, -16, 0.95)}
      {bao_top(-2, 48, 0.92)}
    </g>'''


def turnip_cake_cluster(s=1.0):
    def slc(dx, dy, rot):
        return f'''<g transform="translate({dx},{dy}) rotate({rot})">
          <rect x="-34" y="-24" width="68" height="48" rx="6" fill="{g_turnip}"/>
          <path d="M-30,-18 L30,-18 M-30,18 L30,18" stroke="#8a5a28" stroke-width="2" opacity="0.4"/>
          <circle cx="-12" cy="-4" r="3" fill="#7a4a2e"/>
          <circle cx="10" cy="6" r="3" fill="#c0392b"/>
        </g>'''
    return f'''<g transform="scale({s})">
      {slc(-26, 20, -6)}
      {slc(20, 0, 5)}
      {slc(-6, -28, -2)}
    </g>'''


def chicken_feet_cluster(s=1.0):
    def claw(dx, dy, rot, s2=1.0):
        return f'''<path d="M0,0 Q20,-8 24,14 Q26,30 10,32 Q-4,33 -6,18 Q-8,4 0,0 Z" fill="{g_feet}"
          transform="translate({dx},{dy}) rotate({rot}) scale({s2})"/>'''
    chili = "".join(
        f'<ellipse cx="{dx}" cy="{dy}" rx="6" ry="2.4" fill="#c0392b" transform="rotate({rot})" opacity="0.85"/>'
        for dx, dy, rot in [(-10, 30, 20), (18, -20, -30), (5, 6, 60)]
    )
    return f'''<g transform="scale({s})">
      {claw(-30, -20, -20)}
      {claw(0, -28, 10)}
      {claw(28, -14, 35)}
      {claw(-18, 14, -50, 0.95)}
      {claw(14, 18, 60, 0.95)}
      {chili}
    </g>'''


def duck_slices_oval(s=1.0):
    def slc(dx, dy, rot):
        return f'''<g transform="translate({dx},{dy}) rotate({rot})">
          <rect x="-38" y="-15" width="76" height="30" rx="11" fill="{g_duck2}"/>
          <path d="M-30,-8 q30,-6 60,0" stroke="#e8a05a" stroke-width="2.5" opacity="0.5" fill="none"/>
        </g>'''
    return f'''<g transform="scale({s})">
      {slc(-86, 10, -16)}
      {slc(-30, -8, -6)}
      {slc(28, 6, 4)}
      {slc(86, -6, 16)}
    </g>'''


def noodle_bowl_top(s=1.0):
    noodles = "".join(
        f'<path d="M{-70+i*14},{-30+(i%2)*10} q14,-22 28,0 q14,22 28,0" stroke="#f3d98a" stroke-width="4.5" fill="none" opacity="0.85"/>'
        for i in range(5)
    )
    garnish = "".join(
        f'<circle cx="{dx}" cy="{dy}" r="3" fill="#5a8a3c"/>'
        for dx, dy in [(-40, 20), (10, 30), (50, 10), (-10, -10)]
    )
    return f'''<g transform="scale({s})">
      {noodles}
      <g transform="translate(-50,40)">{siu_mai_top(0,0,0.6)}</g>
      <g transform="translate(55,36)">{siu_mai_top(0,0,0.55)}</g>
      {garnish}
    </g>'''


def congee_bowl_top(s=1.0):
    bits = "".join(
        f'<ellipse cx="{dx}" cy="{dy}" rx="5" ry="3" fill="#4a4030" opacity="0.6" transform="rotate({rot})"/>'
        for dx, dy, rot in [(-30, -10, 10), (20, 20, -15), (10, -25, 25), (-15, 25, 5)]
    )
    shreds = "".join(
        f'<path d="M{dx},{dy} q10,4 20,0" stroke="#d8a564" stroke-width="3" fill="none" opacity="0.7"/>'
        for dx, dy in [(-35, 10), (5, -8), (15, 28)]
    )
    scallion = "".join(f'<circle cx="{dx}" cy="{dy}" r="2.4" fill="#5a8a3c"/>' for dx, dy in [(-10, 5), (25, -5), (-25, -20)])
    return f'<g transform="scale({s})">{bits}{shreds}{scallion}</g>'


def milk_tea_swirl(s=1.0):
    return f'''<g transform="scale({s})">
      <path d="M-60,-30 A75,55 0 0 1 20,-65" fill="none" stroke="#f3e3bd" stroke-width="9" opacity="0.45" stroke-linecap="round"/>
    </g>'''


def egg_tart_top(s=1.0):
    def flute(rx, n=18):
        pts = []
        for i in range(n + 1):
            a = 2 * math.pi * i / n
            pts.append((rx * math.cos(a), rx * math.sin(a)))
        d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f} "
        for i in range(n):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            nx, ny = mx * 1.16, my * 1.16
            d += f"Q{nx:.1f},{ny:.1f} {x1:.1f},{y1:.1f} "
        return d + "Z"
    return f'''<g transform="scale({s})">
      <path d="{flute(118)}" fill="{g_crust2}"/>
      <circle cx="0" cy="0" r="84" fill="{g_custard2}"/>
      <ellipse cx="-22" cy="-22" rx="26" ry="13" fill="#fffae0" opacity="0.65"/>
    </g>'''


def mango_sago_top(s=1.0):
    sago = "".join(
        f'<circle cx="{dx}" cy="{dy}" r="6" fill="#fbe8c8"/>'
        for dx, dy in [(-30, -10), (10, -20), (35, 5), (0, 20), (-20, 25), (25, 30)]
    )
    return f'<g transform="scale({s})">{sago}</g>'


def flatlay_spread(w, h, label_color="#f3e3bd"):
    def cell(cx, cy, rot, container, topping, label):
        return f'''<g transform="translate({cx},{cy}) rotate({rot})">
          {container}
          <g transform="rotate({-rot})">{topping}</g>
        </g>
        <text x="{cx}" y="{cy + 168}" font-size="20" letter-spacing="2" fill="{label_color}" text-anchor="middle" opacity="0.85">{label}</text>'''

    items = [
        (150, 175, -6, steamer_top(128), har_gow_cluster(0.92), "HAR GOW · SIU MAI"),
        (510, 165, 4, steamer_top(128), siu_mai_cluster(0.92), "SIU MAI"),
        (875, 175, -3, plate_top(140), cheung_fun_plate(0.95), "CHEUNG FUN"),
        (1240, 165, 6, plate_top(130), bao_cluster(0.95), "CHAR SIU BAO"),
        (140, 485, 5, plate_top(130), turnip_cake_cluster(0.95), "TURNIP CAKE"),
        (500, 480, -7, plate_top(130), chicken_feet_cluster(0.95), "PHOENIX TALONS"),
        (905, 485, 3, None, None, "ROAST DUCK"),
        (1290, 480, -4, bowl_top(135, fill=g_broth), noodle_bowl_top(0.95), "WONTON NOODLES"),
        (160, 800, 6, bowl_top(130, fill=g_congee), congee_bowl_top(1.0), "CENTURY EGG CONGEE"),
        (520, 795, -5, cup_top(120), milk_tea_swirl(1.0), "HK MILK TEA"),
        (895, 800, 4, None, None, "EGG TART"),
        (1280, 795, -6, cup_top(120, rim="#fdf6ea", fill=g_mango), mango_sago_top(0.85), "MANGO SAGO"),
    ]

    parts = [wood_table(w, h)]
    for cx, cy, rot, container, topping, label in items:
        if label == "ROAST DUCK":
            parts.append(f'''<g transform="translate({cx},{cy}) rotate({rot})">
              {plate_top(rx=185, ry=128)}
              {duck_slices_oval(0.85)}
            </g>
            <text x="{cx}" y="{cy + 168}" font-size="20" letter-spacing="2" fill="{label_color}" text-anchor="middle" opacity="0.85">{label}</text>''')
        elif label == "EGG TART":
            parts.append(f'''<g transform="translate({cx},{cy}) rotate({rot})">
              {plate_top(135)}
              {egg_tart_top(0.78)}
            </g>
            <text x="{cx}" y="{cy + 168}" font-size="20" letter-spacing="2" fill="{label_color}" text-anchor="middle" opacity="0.85">{label}</text>''')
        else:
            parts.append(cell(cx, cy, rot, container, topping, label))
    return "".join(parts)
