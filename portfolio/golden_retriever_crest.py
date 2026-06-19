from common import save, FONT_TC

SERIF = "Liberation Serif"
SANS = "Liberation Sans"

CREAM = "#f8f1e2"
CREAM_DK = "#ecdfc0"
GOLD = "#cda86a"
GOLD_DK = "#9c7a3e"
GOLD_LT = "#e8caa0"
AMBER = "#b8862c"
AMBER_DK = "#8a6428"
FUR_DARK = "#a9763a"
FUR_MID = "#cf9d56"
FUR_LIGHT = "#f0d8a4"
INK = "#2e2014"
FOREST = "#3a4a36"

S = 900
_DEFS = []

def grad(id_, kind, stops, **attrs):
    attr_str = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    stops_svg = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in stops)
    _DEFS.append(f'<{kind}Gradient id="{id_}" {attr_str}>{stops_svg}</{kind}Gradient>')
    return f"url(#{id_})"

g_bg = grad("g_bg", "radial", [(0, "#fffaf0", 1), (1, CREAM_DK, 1)], cx="0.5", cy="0.4", r="0.8")
g_skull = grad("g_skull", "linear", [(0, FUR_LIGHT, 1), (0.45, FUR_MID, 1), (1, FUR_DARK, 1)], x1="0.2", y1="0", x2="0.85", y2="1")
g_ear = grad("g_ear", "linear", [(0, FUR_MID, 1), (1, AMBER_DK, 1)], x1="0", y1="0", x2="0.3", y2="1")
g_muzzle = grad("g_muzzle", "linear", [(0, FUR_LIGHT, 1), (1, FUR_MID, 1)], x1="0", y1="0", x2="0", y2="1")
g_chest = grad("g_chest", "linear", [(0, "#fff7e6", 1), (1, FUR_LIGHT, 1)], x1="0", y1="0", x2="0", y2="1")


def crest_ring(r=410):
    cx = cy = S / 2
    return f'''
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{AMBER}" stroke-width="6"/>
    <circle cx="{cx}" cy="{cy}" r="{r-18}" fill="none" stroke="{AMBER}" stroke-width="2" opacity="0.7"/>
    '''


def laurel(cx, cy, side=1, scale=1.0):
    leaves = []
    n = 7
    for i in range(n):
        t = i / (n - 1)
        ang = -10 + t * 100
        rad = ang * 3.14159 / 180
        lx = cx + side * (40 + t * 150) * scale
        ly = cy - (10 + t * 95) * scale
        lw = (26 - t * 12) * scale
        rot = side * (60 - t * 70)
        leaves.append(f'<ellipse cx="{lx:.1f}" cy="{ly:.1f}" rx="{lw:.1f}" ry="{lw*0.42:.1f}" fill="{FOREST}" opacity="{0.85-t*0.25:.2f}" transform="rotate({rot:.1f} {lx:.1f} {ly:.1f})"/>')
    stem = f'<path d="M{cx + side*20},{cy+6} Q{cx+side*120*scale},{cy-70*scale} {cx+side*195*scale},{cy-110*scale}" stroke="{FOREST}" stroke-width="3" fill="none" opacity="0.8"/>'
    return stem + "".join(leaves)


def dog_head(cx, cy, scale=1.0):
    # local (un-mirrored) coordinates, x=0 is the head's center line
    chest = f'''
    <path d="M-160,150 Q-130,250 0,282 Q130,250 160,150
              Q120,100 0,90 Q-120,100 -160,150 Z" fill="{g_chest}"/>
    '''

    skull = f'''
    <path d="M-128,-25 Q-150,-160 -38,-208 Q0,-222 38,-208 Q150,-160 128,-25
              Q118,48 58,78 Q0,94 -58,78 Q-118,48 -128,-25 Z" fill="{g_skull}"/>
    '''

    # left-side hanging ear (will be mirrored for the right side)
    ear_left = f'''
    <path d="M-95,-168 Q-185,-130 -188,-25 Q-190,68 -128,102
              Q-96,82 -92,28 Q-88,-72 -95,-168 Z" fill="{g_ear}"/>
    <path d="M-150,-90 Q-160,-10 -140,55" stroke="{AMBER_DK}" stroke-width="3" fill="none" opacity="0.45"/>
    <path d="M-128,-50 Q-136,15 -122,72" stroke="{AMBER_DK}" stroke-width="2.5" fill="none" opacity="0.35"/>
    '''

    eye_left = f'''
    <path d="M-62,-28 Q-36,-44 -10,-30 Q-32,-10 -62,-28 Z" fill="{INK}"/>
    <circle cx="-38" cy="-32" r="4.5" fill="#fff" opacity="0.75"/>
    <path d="M-66,-42 Q-34,-58 -4,-42" stroke="{AMBER_DK}" stroke-width="3" fill="none" opacity="0.5"/>
    '''

    brow_left = f'''<path d="M-95,-100 Q-58,-120 -22,-104" stroke="{FUR_LIGHT}" stroke-width="4" fill="none" opacity="0.45"/>'''

    cheek_fur_left = f'''
    <path d="M-100,10 Q-80,40 -90,75" stroke="{FUR_LIGHT}" stroke-width="3" fill="none" opacity="0.4"/>
    '''

    muzzle = f'''
    <path d="M0,28 Q48,36 60,82 Q66,138 18,166
              Q0,174 -18,166 Q-66,138 -60,82 Q-48,36 0,28 Z" fill="{g_muzzle}"/>
    <path d="M-60,82 Q-30,76 0,82 Q30,76 60,82" stroke="{AMBER_DK}" stroke-width="2.5" fill="none" opacity="0.4"/>
    '''

    nose = f'''
    <path d="M-24,136 Q0,124 24,136 Q32,160 8,176 Q0,180 -8,176 Q-32,160 -24,136 Z" fill="{INK}"/>
    <ellipse cx="-9" cy="146" rx="6" ry="4" fill="#fff" opacity="0.35"/>
    '''

    mouth = f'''
    <path d="M0,174 Q0,190 -26,198" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.85"/>
    <path d="M0,174 Q0,190 26,198" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.85"/>
    '''

    left_side = ear_left + eye_left + brow_left + cheek_fur_left
    right_side = f'<g transform="scale(-1,1)">{left_side}</g>'

    return f'''<g transform="translate({cx},{cy}) scale({scale})">
      {chest}
      {left_side}
      {right_side}
      {skull}
      {muzzle}
      {nose}
      {mouth}
    </g>'''


def wordmark(name_en, name_cn, y_top=178, y_bottom=722):
    return f'''
    <text x="{S/2}" y="{y_top}" font-family="{SERIF}" font-weight="700" font-size="58" letter-spacing="10" fill="{INK}" text-anchor="middle">{name_en}</text>
    <text x="{S/2}" y="{y_top+38}" font-family="{SANS}" font-size="15" letter-spacing="6" fill="{AMBER_DK}" text-anchor="middle">EST. FINE DINING</text>
    <line x1="{S/2-130}" y1="{y_bottom-46}" x2="{S/2+130}" y2="{y_bottom-46}" stroke="{AMBER}" stroke-width="1.5" opacity="0.7"/>
    <text x="{S/2}" y="{y_bottom}" font-family="{FONT_TC}" font-weight="700" font-size="26" letter-spacing="6" fill="{INK}" text-anchor="middle">{name_cn}</text>
    '''


def build(name_en, name_cn):
    cx, cy = S/2, 410
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <defs>{"".join(_DEFS)}</defs>
      <rect width="{S}" height="{S}" fill="{g_bg}"/>
      {crest_ring()}
      {laurel(S/2, 700, -1, 1.0)}
      {laurel(S/2, 700, 1, 1.0)}
      {dog_head(cx, cy, 1.05)}
      {wordmark(name_en, name_cn)}
    </svg>'''


save("18_logo_golden_crest", build("GOLDEN HOUR", "黃 金 時 刻"), scale=1.2)
