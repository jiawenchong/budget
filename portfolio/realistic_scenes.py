import math

_DEFS = []

def register_defs():
    return "".join(_DEFS)

def _grad(id_, kind, stops, **attrs):
    attr_str = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    stops_svg = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in stops)
    _DEFS.append(f'<{kind}Gradient id="{id_}" {attr_str}>{stops_svg}</{kind}Gradient>')
    return f"url(#{id_})"

def _blur_filter(id_, dev):
    _DEFS.append(f'<filter id="{id_}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{dev}"/></filter>')
    return f"url(#{id_})"

SHADOW = _blur_filter("softshadow", 14)
SOFTGLOW = _blur_filter("softglow", 6)

def steam(cx, cy, h=140, w=26, opacity=0.35):
    paths = []
    for i, dx in enumerate([-1, 0, 1]):
        x = cx + dx*w
        sway = 18 if i != 1 else -14
        paths.append(
            f'<path d="M{x},{cy} C{x+sway},{cy-h*0.4} {x-sway},{cy-h*0.7} {x},{cy-h}" '
            f'stroke="#ffffff" stroke-width="9" fill="none" stroke-linecap="round" '
            f'opacity="{opacity - i*0.06}" filter="{SOFTGLOW}"/>'
        )
    return "".join(paths)

def shadow_ellipse(cx, cy, rx, ry, opacity=0.28):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#1a0e05" opacity="{opacity}" filter="{SHADOW}"/>'


def dimsum_scene(cx, cy):
    g_basket = _grad("g_basket", "linear", [(0, "#e0b173", 1), (0.5, "#c08a4e", 1), (1, "#8a5a28", 1)], x1="0", y1="0", x2="0", y2="1")
    g_basket_in = _grad("g_basket_in", "radial", [(0, "#fff6e0", 1), (1, "#d9b06a", 1)], cx="0.5", cy="0.35", r="0.7")
    g_har = _grad("g_har", "radial", [(0, "#fffaf2", 0.95), (0.7, "#fce8d6", 0.95), (1, "#e8c49c", 0.9)], cx="0.35", cy="0.3", r="0.8")
    g_shrimp = _grad("g_shrimp", "linear", [(0, "#ffb37a", 1), (1, "#e8773f", 1)], x1="0", y1="0", x2="1", y2="1")
    g_siu_skin = _grad("g_siu_skin", "linear", [(0, "#ffe48a", 1), (1, "#e8b73c", 1)], x1="0", y1="0", x2="0", y2="1")

    weave = "".join(
        f'<path d="M{-150+i*30},-70 q15,140 0,210" stroke="#7a4d22" stroke-width="3" fill="none" opacity="0.35"/>'
        for i in range(11)
    )

    def har_gow(x, y, rot, s):
        pleats = "".join(
            f'<path d="M{px},10 Q{px+11},-20 {px+22},10" stroke="#d8b88a" stroke-width="2.2" fill="none" opacity="0.6"/>'
            for px in range(-42, 32, 14)
        )
        return f'''<g transform="translate({x},{y}) rotate({rot}) scale({s})">
          {shadow_ellipse(0, 26, 46, 12, 0.18)}
          <path d="M-46,8 C-46,-26 46,-26 46,8 C46,30 -46,30 -46,8 Z" fill="{g_har}" stroke="#dcb98a" stroke-width="1.5"/>
          <ellipse cx="0" cy="10" rx="26" ry="11" fill="{g_shrimp}"/>
          {pleats}
          <ellipse cx="-14" cy="-10" rx="10" ry="5" fill="#ffffff" opacity="0.55"/>
        </g>'''

    def siu_mai(x, y, s):
        return f'''<g transform="translate({x},{y}) scale({s})">
          {shadow_ellipse(0, 22, 40, 10, 0.18)}
          <path d="M-34,14 L-28,-22 L28,-22 L34,14 Z" fill="{g_siu_skin}"/>
          <ellipse cx="0" cy="-22" rx="10" ry="8" fill="#e8632f"/>
          <ellipse cx="-7" cy="-20" rx="3.5" ry="2.8" fill="#ffb37a" opacity="0.8"/>
          <circle cx="-15" cy="8" r="5" fill="#e89a2c"/>
          <circle cx="10" cy="10" r="5" fill="#e89a2c"/>
          <ellipse cx="-10" cy="-10" rx="8" ry="4" fill="#fff6cc" opacity="0.5"/>
        </g>'''

    return f'''
    <g transform="translate({cx},{cy})">
      {shadow_ellipse(0, 175, 230, 30, 0.30)}
      <ellipse cx="0" cy="160" rx="220" ry="36" fill="{g_basket}"/>
      <path d="M-220,160 Q-220,40 -150,-10 L150,-10 Q220,40 220,160 Z" fill="{g_basket}"/>
      {weave}
      <ellipse cx="0" cy="-10" rx="150" ry="32" fill="{g_basket_in}" stroke="#7a4d22" stroke-width="3"/>
      {har_gow(-78, -18, -8, 1.0)}
      {har_gow(0, -34, 4, 1.05)}
      {har_gow(80, -16, 10, 1.0)}
      {siu_mai(-32, -42, 0.95)}
      {siu_mai(38, -44, 0.95)}
      {steam(-60, -70, 150, 22, 0.4)}
      {steam(60, -75, 160, 22, 0.38)}
    </g>'''


def roast_scene(cx, cy):
    g_duck = _grad("g_duck", "radial", [(0, "#e8a04a", 1), (0.45, "#b8581f", 1), (1, "#6e2a0c", 1)], cx="0.35", cy="0.3", r="0.85")
    g_char = _grad("g_char", "linear", [(0, "#e85a2a", 1), (0.5, "#b02d12", 1), (1, "#6e1408", 1)], x1="0", y1="0", x2="0", y2="1")
    g_board = _grad("g_board", "linear", [(0, "#c9974f", 1), (1, "#a8723a", 1)], x1="0", y1="0", x2="0", y2="1")

    def duck_body(x, y, s):
        body = ("M-6,-112 C44,-114 84,-72 82,-14 "
                "C80,40 66,82 40,108 "
                "C30,118 36,128 22,134 "
                "C8,139 -2,128 -10,116 "
                "C-40,86 -64,40 -68,-16 "
                "C-72,-72 -40,-110 -6,-112 Z")
        wing = ("M18,-54 C48,-36 56,4 42,52 C34,78 16,92 -4,92 "
                "C12,76 24,44 24,4 C24,-22 18,-42 8,-58 Z")
        return f'''<g transform="translate({x},{y}) scale({s})">
          <path d="M-10,-112 C-8,-142 10,-164 30,-158 C42,-154 45,-140 38,-129" fill="none" stroke="#3a1c08" stroke-width="9" stroke-linecap="round"/>
          <ellipse cx="38" cy="-146" rx="21" ry="18" fill="{g_duck}"/>
          <path d="M56,-148 L86,-138 L56,-126 Z" fill="#e8a13c"/>
          <circle cx="44" cy="-151" r="3.2" fill="#1a0e05"/>
          <path d="{body}" fill="{g_duck}"/>
          <path d="{wing}" fill="#7a3812" opacity="0.5"/>
          <path d="{wing}" fill="none" stroke="#5e2208" stroke-width="2" opacity="0.4"/>
          <path d="M-54,-46 Q-8,-22 38,-42" fill="none" stroke="#5e2208" stroke-width="2.5" opacity="0.4"/>
          <ellipse cx="-30" cy="-50" rx="26" ry="40" fill="#ffd9a0" opacity="0.42"/>
          <path d="{body}" fill="none" stroke="#4a1f0a" stroke-width="3"/>
          <path d="M14,128 Q4,148 -10,150 Q-4,134 -2,120 Z" fill="{g_duck}" stroke="#4a1f0a" stroke-width="2.5"/>
          <ellipse cx="2" cy="158" rx="17" ry="13" fill="#3a1c08"/>
          <path d="M-8,158 q8,16 16,0" fill="none" stroke="#1a0e05" stroke-width="2" opacity="0.5"/>
        </g>'''

    def char_siu_slice(x, y, rot, s):
        return f'''<g transform="translate({x},{y}) rotate({rot}) scale({s})">
          <rect x="-32" y="-17" width="64" height="34" rx="12" fill="{g_char}"/>
          <path d="M-26,-8 q20,-10 40,2" stroke="#f3c89a" stroke-width="4" fill="none" opacity="0.55" stroke-linecap="round"/>
          <path d="M-22,6 q22,-8 36,4" stroke="#f3c89a" stroke-width="3" fill="none" opacity="0.4" stroke-linecap="round"/>
          <ellipse cx="-12" cy="-4" rx="6" ry="3.5" fill="#3a0e02" opacity="0.5"/>
          <ellipse cx="16" cy="8" rx="5" ry="3" fill="#3a0e02" opacity="0.45"/>
          <path d="M-28,-14 q30,-6 56,4" stroke="#ffe0b0" stroke-width="2" fill="none" opacity="0.35"/>
        </g>'''

    return f'''
    <g transform="translate({cx},{cy})">
      {shadow_ellipse(0, 210, 230, 28, 0.30)}
      <rect x="-200" y="172" width="400" height="56" rx="14" fill="{g_board}"/>
      <rect x="-200" y="172" width="400" height="10" rx="5" fill="#e8c98a" opacity="0.4"/>
      {char_siu_slice(-100, 196, -8, 1.05)}
      {char_siu_slice(-34, 204, 6, 1.0)}
      {char_siu_slice(36, 192, -5, 1.05)}
      {char_siu_slice(102, 202, 9, 0.95)}
      <g transform="translate(-10,-160) scale(0.95)">
        <line x1="38" y1="-205" x2="38" y2="-163" stroke="#3a1c08" stroke-width="5"/>
        {duck_body(0, 0, 1.0)}
      </g>
    </g>'''


def drinks_scene(cx, cy):
    g_tea = _grad("g_tea", "linear", [(0, "#8a5a32", 1), (1, "#4a2a12", 1)], x1="0", y1="0", x2="0", y2="1")
    g_milk = _grad("g_milk", "linear", [(0, "#f3e3c4", 1), (1, "#d9b87a", 1)], x1="0", y1="0", x2="0", y2="1")
    g_pot = _grad("g_pot", "linear", [(0, "#fdfdfb", 1), (0.5, "#cfd2d6", 1), (1, "#8a8f96", 1)], x1="0", y1="0", x2="1", y2="1")
    g_crust = _grad("g_crust", "linear", [(0, "#eccb84", 1), (1, "#c0823a", 1)], x1="0", y1="0", x2="0", y2="1")
    g_custard = _grad("g_custard", "radial", [(0, "#fff0b8", 1), (1, "#eba83c", 1)], cx="0.38", cy="0.32", r="0.75")

    def flute(rx, ry, n=16):
        pts = []
        for i in range(n + 1):
            a = math.pi * i / n
            x = math.cos(a) * rx
            yb = math.sin(a) * ry * 0.25
            pts.append((x, yb))
        d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f} "
        for i in range(n):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + 9
            d += f"Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f} "
        return d

    stream = '''<path d="M-92,-178 C-60,-130 -10,-96 26,-58" stroke="#4a2a12" stroke-width="11" fill="none" stroke-linecap="round" opacity="0.92"/>
      <path d="M-92,-178 C-60,-130 -10,-96 26,-58" stroke="#c9a06c" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.65"/>'''

    droplets = "".join(
        f'<circle cx="{26+dx}" cy="{-58+dy}" r="{r}" fill="#4a2a12" opacity="0.5"/>'
        for dx, dy, r in [(12, 10, 4), (-8, 18, 3), (20, 26, 3.5)]
    )

    cup = f'''<g transform="translate(-110,-200) rotate(-28)">
      <path d="M-34,-8 Q-58,-2 -56,18 Q-54,32 -30,28" fill="none" stroke="{g_pot}" stroke-width="9"/>
      <path d="M-32,-34 L32,-34 L24,28 Q0,38 -24,28 Z" fill="{g_pot}"/>
      <ellipse cx="0" cy="-34" rx="32" ry="9" fill="#e8eaec"/>
      <ellipse cx="0" cy="-34" rx="32" ry="9" fill="none" stroke="#9aa0a6" stroke-width="2"/>
      <path d="M-18,-26 L-12,18" stroke="#ffffff" stroke-width="5" opacity="0.6"/>
    </g>'''

    glass = f'''<g transform="translate(40,40)">
      <path d="M-44,-104 L-34,84 L34,84 L44,-104 Z" fill="#fdfdfb" opacity="0.16"/>
      <path d="M-38,-58 L-31,80 L31,80 L38,-58 Z" fill="{g_tea}"/>
      <path d="M-38,-58 L-35,-34 L35,-34 L38,-58 Z" fill="{g_milk}"/>
      <ellipse cx="0" cy="-58" rx="38" ry="8" fill="#e8d4a8"/>
      <ellipse cx="0" cy="-34" rx="36.5" ry="6" fill="#fff6e0" opacity="0.55"/>
      <path d="M-38,-58 L-44,-104 L44,-104 L38,-58 Z" fill="none" stroke="#d8dadc" stroke-width="3"/>
      <path d="M-22,-90 L-12,40" stroke="#ffffff" stroke-width="9" opacity="0.5"/>
      {shadow_ellipse(0, 88, 48, 10, 0.18)}
    </g>'''

    tart = f'''<g transform="translate(190,130)">
      {shadow_ellipse(0, 46, 64, 14, 0.18)}
      <path d="M-60,16 {flute(60, 36)} Z" fill="{g_crust}"/>
      <path d="M-60,16 Q0,42 60,16 Q0,2 -60,16 Z" fill="{g_crust}"/>
      <path d="M-50,8 q10,10 0,18 M-26,2 q10,12 0,20 M0,0 q10,12 0,20 M26,4 q10,11 0,19 M48,10 q10,9 0,17"
            stroke="#a8702c" stroke-width="2.2" fill="none" opacity="0.45"/>
      <ellipse cx="-4" cy="-8" rx="42" ry="21" fill="{g_custard}"/>
      <ellipse cx="-16" cy="-16" rx="13" ry="6.5" fill="#fffae0" opacity="0.75"/>
    </g>'''

    return f'''
    <g transform="translate({cx},{cy})">
      {shadow_ellipse(20, 178, 240, 30, 0.26)}
      {cup}
      {stream}
      {droplets}
      {glass}
      {tart}
    </g>'''
