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
FUR_DARK = "#9c6a30"
FUR_MID = "#cf9d56"
FUR_LIGHT = "#f0d8a4"
FUR_PALE = "#fbe9c4"
INK = "#2e2014"

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
g_muzzle = grad("g_muzzle", "linear", [(0, FUR_PALE, 1), (1, FUR_MID, 1)], x1="0", y1="0", x2="0", y2="1")
g_chest = grad("g_chest", "linear", [(0, "#fff7e6", 1), (1, FUR_LIGHT, 1)], x1="0", y1="0", x2="0", y2="1")
g_fork = grad("g_fork", "linear", [(0, "#f3d99a", 1), (0.5, GOLD, 1), (1, AMBER_DK, 1)], x1="0", y1="0", x2="1", y2="1")


def crest_ring(r=410):
    cx = cy = S / 2
    return f'''
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{AMBER}" stroke-width="6"/>
    <circle cx="{cx}" cy="{cy}" r="{r-18}" fill="none" stroke="{AMBER}" stroke-width="2" opacity="0.7"/>
    '''


def fur_strand(x, y, ang, length, width, color, opacity, curve=8):
    rad = math.radians(ang)
    dx, dy = math.cos(rad) * length, math.sin(rad) * length
    prad = math.radians(ang + 90)
    mx = x + dx * 0.5 + math.cos(prad) * curve
    my = y + dy * 0.5 + math.sin(prad) * curve
    return f'<path d="M{x:.1f},{y:.1f} Q{mx:.1f},{my:.1f} {x+dx:.1f},{y+dy:.1f}" stroke="{color}" stroke-width="{width:.1f}" fill="none" stroke-linecap="round" opacity="{opacity:.2f}"/>'


def fur_field(x0, y0, x1, y1, base_ang, n, length_range, colors, width=3.2, arc=0):
    strokes = []
    for i in range(n):
        t = i / (n - 1) if n > 1 else 0.5
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + math.sin(t * math.pi) * arc
        jitter = math.sin(i * 2.7) * 10
        ang = base_ang + jitter
        length = length_range[0] + (length_range[1] - length_range[0]) * ((math.sin(i * 1.3) + 1) / 2)
        color = colors[i % len(colors)]
        op = 0.55 + 0.35 * ((math.cos(i * 0.9) + 1) / 2)
        strokes.append(fur_strand(x, y, ang, length, width, color, op))
    return "".join(strokes)


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
    chest = f'''
    <path d="M-160,150 Q-130,250 0,282 Q130,250 160,150
              Q120,100 0,90 Q-120,100 -160,150 Z" fill="{g_chest}"/>
    '''
    chest_fur = fur_field(-120, 175, 120, 175, 95, 17, (22, 42), ["#fff7e6", FUR_PALE, FUR_LIGHT], width=3.4, arc=22)

    skull = f'''
    <path d="M-128,-25 Q-150,-160 -38,-208 Q0,-222 38,-208 Q150,-160 128,-25
              Q118,48 58,78 Q0,94 -58,78 Q-118,48 -128,-25 Z" fill="{g_skull}"/>
    '''
    forehead_fur = fur_field(-85, -130, 85, -130, 100, 17, (12, 22), [FUR_DARK, FUR_MID, FUR_LIGHT], width=2.6, arc=-14)
    crown_fur = fur_field(-45, -175, 45, -175, 100, 8, (8, 14), [FUR_PALE, FUR_LIGHT], width=2.2, arc=-6)

    # left-side hanging ear (mirrored for the right side)
    ear_left = f'''
    <path d="M-95,-168 Q-185,-130 -188,-25 Q-190,68 -128,102
              Q-96,82 -92,28 Q-88,-72 -95,-168 Z" fill="{g_ear}"/>
    '''
    ear_fur_left = fur_field(-180, -130, -132, 90, 105, 14, (20, 36), [FUR_DARK, AMBER_DK, FUR_MID], width=3.2, arc=-18)

    eye_left = f'''
    <ellipse cx="-36" cy="-6" rx="20" ry="22" fill="{INK}"/>
    <circle cx="-42" cy="-14" r="6" fill="#fff" opacity="0.8"/>
    <path d="M-68,-22 Q-36,-40 -2,-22" stroke="{AMBER_DK}" stroke-width="3" fill="none" opacity="0.5"/>
    '''

    brow_left = f'''<path d="M-95,-58 Q-58,-78 -22,-62" stroke="{FUR_LIGHT}" stroke-width="4" fill="none" opacity="0.45"/>'''

    cheek_fur_left = fur_field(-118, 0, -78, 70, 150, 9, (16, 28), [FUR_LIGHT, FUR_MID, FUR_DARK], width=2.8, arc=10)

    muzzle = f'''
    <path d="M0,28 Q48,36 60,82 Q66,138 18,166
              Q0,174 -18,166 Q-66,138 -60,82 Q-48,36 0,28 Z" fill="{g_muzzle}"/>
    <path d="M-60,82 Q-30,76 0,82 Q30,76 60,82" stroke="{AMBER_DK}" stroke-width="2.5" fill="none" opacity="0.4"/>
    '''
    muzzle_fur_left = fur_field(-52, 60, -16, 150, 110, 7, (12, 20), [FUR_PALE, FUR_LIGHT], width=2.2, arc=6)

    nose = f'''
    <path d="M-24,136 Q0,124 24,136 Q32,160 8,176 Q0,180 -8,176 Q-32,160 -24,136 Z" fill="{INK}"/>
    <ellipse cx="-9" cy="146" rx="6" ry="4" fill="#fff" opacity="0.35"/>
    '''

    mouth = f'''
    <path d="M0,174 Q0,190 -26,198" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.85"/>
    <path d="M0,174 Q0,190 26,198" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.85"/>
    '''

    ear_side = ear_left + ear_fur_left
    ear_side_r = f'<g transform="scale(-1,1)">{ear_side}</g>'
    face_side = eye_left + brow_left + cheek_fur_left + muzzle_fur_left
    face_side_r = f'<g transform="scale(-1,1)">{face_side}</g>'

    return f'''<g transform="translate({cx},{cy}) scale({scale})">
      {chest}
      {chest_fur}
      {ear_side}
      {ear_side_r}
      {skull}
      {forehead_fur}
      {crown_fur}
      {muzzle}
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
