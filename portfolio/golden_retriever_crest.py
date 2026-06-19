import math
from common import save

SERIF = "Liberation Serif"
SANS = "Liberation Sans"

CREAM = "#f8f1e2"
CREAM_DK = "#ecdfc0"
GOLD = "#cda86a"
GOLD_DK = "#9c7a3e"
GOLD_LT = "#e8caa0"
AMBER = "#b8862c"
AMBER_DK = "#8a6428"
FUR_SHADOW = "#7a4f22"
FUR_DARK = "#9c6a30"
FUR_MID = "#cf9d56"
FUR_LIGHT = "#f0d8a4"
FUR_PALE = "#fbe9c4"
FUR_HILITE = "#fff6e2"
INK = "#241a12"

S = 900
_DEFS = []

def grad(id_, kind, stops, **attrs):
    attr_str = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    stops_svg = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in stops)
    _DEFS.append(f'<{kind}Gradient id="{id_}" {attr_str}>{stops_svg}</{kind}Gradient>')
    return f"url(#{id_})"

def blur(id_, dev):
    _DEFS.append(f'<filter id="{id_}" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="{dev}"/></filter>')
    return f"url(#{id_})"

g_bg = grad("g_bg", "radial", [(0, "#fffaf0", 1), (1, CREAM_DK, 1)], cx="0.5", cy="0.4", r="0.8")
g_skull = grad("g_skull", "radial", [(0, FUR_LIGHT, 1), (0.55, FUR_MID, 1), (1, FUR_SHADOW, 1)], cx="0.38", cy="0.28", r="0.75")
g_ear = grad("g_ear", "linear", [(0, FUR_MID, 1), (0.6, FUR_DARK, 1), (1, FUR_SHADOW, 1)], x1="0.1", y1="0", x2="0.5", y2="1")
g_muzzle = grad("g_muzzle", "radial", [(0, FUR_HILITE, 1), (0.6, FUR_PALE, 1), (1, FUR_MID, 1)], cx="0.4", cy="0.25", r="0.8")
g_chest = grad("g_chest", "radial", [(0, "#fffaf0", 1), (1, FUR_LIGHT, 1)], cx="0.5", cy="0.1", r="0.9")
g_fork = grad("g_fork", "linear", [(0, "#f3d99a", 1), (0.5, GOLD, 1), (1, AMBER_DK, 1)], x1="0", y1="0", x2="1", y2="1")
g_iris = grad("g_iris", "radial", [(0, "#6b4322", 1), (0.7, "#3a2412", 1), (1, "#1c120a", 1)], cx="0.4", cy="0.35", r="0.7")
g_nose = grad("g_nose", "radial", [(0, "#3a2c22", 1), (0.6, "#221710", 1), (1, "#120b07", 1)], cx="0.35", cy="0.3", r="0.75")
SHADOW = blur("softshadow", 14)


def crest_ring(r=410):
    cx = cy = S / 2
    return f'''
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{AMBER}" stroke-width="6"/>
    <circle cx="{cx}" cy="{cy}" r="{r-18}" fill="none" stroke="{AMBER}" stroke-width="2" opacity="0.7"/>
    '''


def fur_strand(x, y, ang, length, base_w, color, opacity, curve=6, taper=0.92):
    rad = math.radians(ang)
    dx, dy = math.cos(rad) * length, math.sin(rad) * length
    prad = math.radians(ang + 90)
    px, py = math.cos(prad), math.sin(prad)
    bx1, by1 = x + px * base_w / 2, y + py * base_w / 2
    bx2, by2 = x - px * base_w / 2, y - py * base_w / 2
    mx, my = x + dx * 0.55 + px * curve, y + dy * 0.55 + py * curve
    tipx, tipy = x + dx, y + dy
    c1x, c1y = mx + px * base_w * taper * 0.18, my + py * base_w * taper * 0.18
    c2x, c2y = mx - px * base_w * taper * 0.18, my - py * base_w * taper * 0.18
    d = f"M{bx1:.1f},{by1:.1f} Q{c1x:.1f},{c1y:.1f} {tipx:.1f},{tipy:.1f} Q{c2x:.1f},{c2y:.1f} {bx2:.1f},{by2:.1f} Z"
    return f'<path d="{d}" fill="{color}" opacity="{opacity:.2f}"/>'


def fur_field(x0, y0, x1, y1, base_ang, n, length_range, colors, base_w=3.4, arc=0, jitter_amt=10, layered=True):
    out = []
    for i in range(n):
        t = i / (n - 1) if n > 1 else 0.5
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + math.sin(t * math.pi) * arc
        jitter = math.sin(i * 2.7) * jitter_amt
        ang = base_ang + jitter
        length = length_range[0] + (length_range[1] - length_range[0]) * ((math.sin(i * 1.3) + 1) / 2)
        if layered:
            shadow_color = colors[-1] if len(colors) > 1 else colors[0]
            out.append(fur_strand(x, y, ang + 3, length * 1.08, base_w * 1.15, shadow_color, 0.32))
        color = colors[i % len(colors)]
        op = 0.55 + 0.35 * ((math.cos(i * 0.9) + 1) / 2)
        out.append(fur_strand(x, y, ang, length, base_w, color, op))
        if layered and i % 2 == 0:
            hi = colors[0]
            out.append(fur_strand(x - 1, y - 1, ang - 4, length * 0.6, base_w * 0.5, hi, 0.4))
    return "".join(out)


def crossed_cutlery(cx, cy, scale=1.0):
    def knife(rot):
        return f'''<g transform="rotate({rot})">
          <path d="M-9,-150 Q14,-128 9,-26 L-9,-26 Z" fill="{g_fork}"/>
          <path d="M-9,-150 Q14,-128 9,-26 L-9,-26 Z" fill="none" stroke="{AMBER_DK}" stroke-width="1.5" opacity="0.5"/>
          <rect x="-8" y="-26" width="16" height="128" rx="7" fill="{AMBER_DK}"/>
          <rect x="-3" y="-18" width="6" height="112" rx="3" fill="{GOLD_LT}" opacity="0.5"/>
        </g>'''

    def fork(rot):
        return f'''<g transform="rotate({rot})">
          <path d="M-18,-150 L-18,-84 M-6,-156 L-6,-84 M6,-156 L6,-84 M18,-150 L18,-84" stroke="{g_fork}" stroke-width="9" stroke-linecap="round"/>
          <path d="M-21,-84 Q0,-64 21,-84 L18,-66 Q0,-50 -18,-66 Z" fill="{g_fork}"/>
          <rect x="-8" y="-72" width="16" height="118" rx="7" fill="{AMBER_DK}"/>
          <rect x="-3" y="-64" width="6" height="100" rx="3" fill="{GOLD_LT}" opacity="0.5"/>
        </g>'''

    return f'''<g transform="translate({cx},{cy}) scale({scale})">
      {fork(-26)}
      {knife(26)}
    </g>'''


def dog_head(cx, cy, scale=1.0):
    # local (un-mirrored) coordinates, x=0 is the head's center line
    ground_shadow = f'<ellipse cx="0" cy="300" rx="170" ry="34" fill="{INK}" opacity="0.16" filter="{SHADOW}"/>'

    chest = f'''
    <path d="M-160,150 Q-130,255 0,288 Q130,255 160,150
              Q120,98 0,88 Q-120,98 -160,150 Z" fill="{g_chest}"/>
    '''
    chest_fur = fur_field(-130, 165, 130, 165, 96, 22, (28, 50), [FUR_HILITE, FUR_PALE, FUR_LIGHT], base_w=4.0, arc=26, jitter_amt=7)

    skull = f'''
    <path d="M-130,-20 Q-156,-158 -40,-210 Q0,-224 40,-210 Q156,-158 130,-20
              Q120,52 60,80 Q0,96 -60,80 Q-120,52 -130,-20 Z" fill="{g_skull}"/>
    '''
    forehead_fur = fur_field(-92, -125, 92, -125, 100, 22, (10, 20), [FUR_DARK, FUR_MID, FUR_LIGHT], base_w=3.0, arc=-12, jitter_amt=8)
    crown_fur = fur_field(-50, -172, 50, -172, 100, 10, (7, 13), [FUR_PALE, FUR_LIGHT], base_w=2.4, arc=-5, jitter_amt=6, layered=False)
    skull_shade = f'<ellipse cx="48" cy="20" rx="80" ry="100" fill="{FUR_SHADOW}" opacity="0.18"/>'

    # left-side hanging ear (mirrored for the right side)
    ear_left = f'''
    <path d="M-92,-160 Q-178,-118 -182,-15 Q-184,72 -126,104
              Q-98,84 -94,30 Q-90,-66 -92,-160 Z" fill="{g_ear}"/>
    <path d="M-92,-160 Q-178,-118 -182,-15 Q-184,72 -126,104 Q-98,84 -94,30 Q-90,-66 -92,-160 Z" fill="none" stroke="{FUR_SHADOW}" stroke-width="2" opacity="0.3"/>
    '''
    ear_fur_left = fur_field(-176, -120, -128, 94, 108, 18, (18, 34), [FUR_DARK, AMBER_DK, FUR_MID], base_w=3.4, arc=-16, jitter_amt=9)

    eye_left = f'''
    <ellipse cx="-37" cy="-4" rx="21" ry="23" fill="{INK}" opacity="0.9"/>
    <ellipse cx="-37" cy="-4" rx="16" ry="18" fill="{g_iris}"/>
    <circle cx="-37" cy="-4" r="8" fill="#0d0805"/>
    <circle cx="-43" cy="-12" r="5.5" fill="#fff" opacity="0.85"/>
    <circle cx="-30" cy="2" r="2.5" fill="#fff" opacity="0.35"/>
    <path d="M-62,-20 Q-37,-34 -10,-18" stroke="{FUR_SHADOW}" stroke-width="4" fill="none" opacity="0.4" stroke-linecap="round"/>
    <path d="M-60,12 Q-37,22 -14,14" stroke="{AMBER_DK}" stroke-width="2" fill="none" opacity="0.3" stroke-linecap="round"/>
    '''

    brow_fur_left = fur_field(-88, -64, -16, -54, 110, 6, (10, 16), [FUR_LIGHT, FUR_PALE], base_w=2.2, arc=-8, jitter_amt=6, layered=False)

    cheek_fur_left = fur_field(-122, -10, -82, 66, 152, 11, (16, 30), [FUR_LIGHT, FUR_MID, FUR_DARK], base_w=3.0, arc=12, jitter_amt=9)

    muzzle = f'''
    <path d="M0,26 Q50,34 62,82 Q68,140 18,168
              Q0,176 -18,168 Q-68,140 -62,82 Q-50,34 0,26 Z" fill="{g_muzzle}"/>
    <path d="M-62,82 Q-30,75 0,82 Q30,75 62,82" stroke="{AMBER_DK}" stroke-width="2.5" fill="none" opacity="0.35"/>
    <ellipse cx="-14" cy="64" rx="22" ry="14" fill="{FUR_HILITE}" opacity="0.5"/>
    '''
    muzzle_fur_left = fur_field(-54, 56, -14, 148, 112, 9, (10, 18), [FUR_PALE, FUR_LIGHT], base_w=2.0, arc=6, jitter_amt=6, layered=False)
    chin_shade = f'<ellipse cx="0" cy="150" rx="48" ry="22" fill="{FUR_MID}" opacity="0.3"/>'

    nose = f'''
    <path d="M-25,134 Q0,120 25,134 Q34,160 8,178 Q0,182 -8,178 Q-34,160 -25,134 Z" fill="{g_nose}"/>
    <path d="M-25,134 Q0,120 25,134" stroke="#000" stroke-width="1" opacity="0.3" fill="none"/>
    <ellipse cx="-10" cy="142" rx="6" ry="4" fill="#fff" opacity="0.4"/>
    <ellipse cx="-13" cy="158" rx="3.5" ry="5" fill="#000" opacity="0.5"/>
    <ellipse cx="13" cy="158" rx="3.5" ry="5" fill="#000" opacity="0.5"/>
    '''

    mouth = f'''
    <path d="M0,172 Q0,188 -27,197" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round" opacity="0.8"/>
    <path d="M0,172 Q0,188 27,197" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round" opacity="0.8"/>
    <path d="M-27,197 Q-30,204 -22,208" stroke="{INK}" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.5"/>
    <path d="M27,197 Q30,204 22,208" stroke="{INK}" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.5"/>
    '''

    ear_side = ear_left + ear_fur_left
    ear_side_r = f'<g transform="scale(-1,1)">{ear_side}</g>'
    face_side = eye_left + brow_fur_left + cheek_fur_left + muzzle_fur_left
    face_side_r = f'<g transform="scale(-1,1)">{face_side}</g>'

    return f'''<g transform="translate({cx},{cy}) scale({scale})">
      {ground_shadow}
      {chest}
      {chest_fur}
      {ear_side}
      {ear_side_r}
      {skull}
      {skull_shade}
      {forehead_fur}
      {crown_fur}
      {muzzle}
      {chin_shade}
      {face_side}
      {face_side_r}
      {nose}
      {mouth}
    </g>'''


def wordmark(name_en, y_top=170):
    return f'''
    <text x="{S/2}" y="{y_top}" font-family="{SERIF}" font-weight="700" font-size="58" letter-spacing="10" fill="{INK}" text-anchor="middle">{name_en}</text>
    <text x="{S/2}" y="{y_top+36}" font-family="{SANS}" font-size="15" letter-spacing="6" fill="{AMBER_DK}" text-anchor="middle">FINE DINING</text>
    '''


def build(name_en):
    cx, cy = S/2, 360
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <defs>{"".join(_DEFS)}</defs>
      <rect width="{S}" height="{S}" fill="{g_bg}"/>
      {crest_ring()}
      {dog_head(cx, cy, 1.05)}
      {crossed_cutlery(S/2, 660, 1.35)}
      {wordmark(name_en)}
    </svg>'''


save("18_logo_golden_crest", build("GOLDEN HOUR"), scale=1.2)
