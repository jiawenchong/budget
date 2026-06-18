import math
from common import save

W, H = 1200, 1500
SERIF = "Liberation Serif"
SANS = "Liberation Sans"

BLUSH_DARK = "#caa089"
BLUSH = "#e8c4ad"
CREAM = "#f6eade"
GOLD = "#cda86a"
GOLD_DK = "#9c7a3e"
LIPSTICK = "#a8243a"
LIPSTICK_DK = "#6e1322"
LIPSTICK_LT = "#d24a5c"
INK = "#2a1a14"

_DEFS = []

def grad(id_, kind, stops, **attrs):
    attr_str = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    stops_svg = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in stops)
    _DEFS.append(f'<{kind}Gradient id="{id_}" {attr_str}>{stops_svg}</{kind}Gradient>')
    return f"url(#{id_})"

def blur(id_, dev):
    _DEFS.append(f'<filter id="{id_}" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="{dev}"/></filter>')
    return f"url(#{id_})"

SHADOW = blur("shadow", 18)
GLOW = blur("glow", 10)

g_bg = grad("g_bg", "radial", [(0, "#fff7ee", 1), (0.6, BLUSH, 1), (1, BLUSH_DARK, 1)], cx="0.5", cy="0.32", r="0.85")
g_gold_tube = grad("g_gold_tube", "linear",
    [(0, "#fff3d6", 1), (0.18, "#e8c578", 1), (0.45, "#c9a258", 1), (0.55, "#a87d3a", 1), (0.78, "#e8c578", 1), (1, "#8a6428", 1)],
    x1="0", y1="0", x2="1", y2="0")
g_gold_cap = grad("g_gold_cap", "linear",
    [(0, "#fff8e4", 1), (0.2, "#eccf8c", 1), (0.5, "#c9a258", 1), (0.8, "#eccf8c", 1), (1, "#8a6428", 1)],
    x1="0", y1="0", x2="1", y2="0")
g_lip = grad("g_lip", "linear",
    [(0, LIPSTICK_LT, 1), (0.45, LIPSTICK, 1), (1, LIPSTICK_DK, 1)], x1="0", y1="0", x2="1", y2="1")
g_lip_tip = grad("g_lip_tip", "radial",
    [(0, "#f08a98", 1), (0.5, LIPSTICK_LT, 1), (1, LIPSTICK_DK, 1)], cx="0.35", cy="0.3", r="0.8")
g_smear = grad("g_smear", "linear",
    [(0, LIPSTICK_LT, 1), (1, LIPSTICK_DK, 1)], x1="0", y1="0", x2="1", y2="1")
g_vign = grad("g_vign", "radial", [(0, "#000000", 0), (1, "#000000", 0.28)], cx="0.5", cy="0.45", r="0.75")


def sparkle(x, y, s, op=0.85):
    return f'''<g transform="translate({x},{y}) scale({s})" opacity="{op}" filter="{GLOW}">
      <path d="M0,-22 L4,-4 L22,0 L4,4 L0,22 L-4,4 L-22,0 L-4,-4 Z" fill="#fff6e0"/>
    </g>'''


def lipstick_product(cx, cy):
    tube_w, tube_h = 96, 300
    cap_w, cap_h = 112, 230

    tube = f'''<g transform="translate({cx},{cy})">
      <ellipse cx="0" cy="{tube_h/2+6}" rx="{tube_w/2*0.92}" ry="14" fill="#000" opacity="0.18" filter="{SHADOW}"/>
      <rect x="{-tube_w/2}" y="{-tube_h/2}" width="{tube_w}" height="{tube_h}" rx="14" fill="{g_gold_tube}"/>
      <rect x="{-tube_w/2}" y="{-tube_h/2}" width="{tube_w}" height="{tube_h}" rx="14" fill="none" stroke="#7a5a22" stroke-width="1.5" opacity="0.5"/>
      <rect x="{-tube_w/2+10}" y="{-tube_h/2+18}" width="6" height="{tube_h-36}" rx="3" fill="#fff8e4" opacity="0.55"/>
      <rect x="{-tube_w/2}" y="{-tube_h/2+34}" width="{tube_w}" height="3" fill="#7a5a22" opacity="0.4"/>
      <text x="0" y="{tube_h/2-26}" font-family="{SERIF}" font-size="19" letter-spacing="3" fill="#5a4018" text-anchor="middle" opacity="0.75">PUREE</text>
    </g>'''

    bullet_h = 150
    bullet = f'''<g transform="translate({cx},{cy-tube_h/2})">
      <path d="M{-tube_w/2+6},0 L{tube_w/2-6},0 L{tube_w/2-16},{-bullet_h*0.62} L{18},{-bullet_h} L{-tube_w/2+22},{-bullet_h*0.78} Z" fill="{g_lip}"/>
      <path d="M{-tube_w/2+22},{-bullet_h*0.78} L{18},{-bullet_h} L{tube_w/2-16},{-bullet_h*0.62}" fill="{g_lip_tip}" opacity="0.9"/>
      <ellipse cx="-6" cy="{-bullet_h*0.74}" rx="16" ry="9" fill="#ffd0d8" opacity="0.55"/>
      <path d="M{-tube_w/2+6},0 L{tube_w/2-6},0 L{tube_w/2-16},{-bullet_h*0.62} L{18},{-bullet_h} L{-tube_w/2+22},{-bullet_h*0.78} Z" fill="none" stroke="{LIPSTICK_DK}" stroke-width="1.5" opacity="0.4"/>
    </g>'''

    cap = f'''<g transform="translate({cx+178},{cy+58}) rotate(14)">
      <ellipse cx="0" cy="{cap_h/2+8}" rx="{cap_w/2*0.92}" ry="16" fill="#000" opacity="0.16" filter="{SHADOW}"/>
      <rect x="{-cap_w/2}" y="{-cap_h/2}" width="{cap_w}" height="{cap_h}" rx="{cap_w/2}" fill="{g_gold_cap}"/>
      <ellipse cx="0" cy="{-cap_h/2+4}" rx="{cap_w/2-6}" ry="14" fill="#3a2a10"/>
      <ellipse cx="0" cy="{-cap_h/2+4}" rx="{cap_w/2-14}" ry="9" fill="#1a1208"/>
      <rect x="{-cap_w/2+12}" y="{-cap_h/2+30}" width="7" height="{cap_h-60}" rx="3.5" fill="#fff8e4" opacity="0.5"/>
    </g>'''

    return tube + bullet + cap


def lip_smear(cx, cy, w):
    pts = []
    n = 26
    for i in range(n + 1):
        t = i / n
        x = cx - w/2 + t * w
        y = cy + math.sin(t * math.pi) * -34 + math.sin(t * math.pi * 5) * 6
        pts.append((x, y))
    top = " ".join(f"L{x:.1f},{y:.1f}" for x, y in pts)
    bot_pts = pts[::-1]
    bot = " ".join(f"L{x:.1f},{y-30:.1f}" for x, y in bot_pts)
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f} {top} {bot} Z"
    highlight = " ".join(f"L{x:.1f},{y-10:.1f}" for x, y in pts[2:-2])
    return f'''<g opacity="0.92">
      <path d="{d}" fill="{g_smear}"/>
      <path d="M{pts[2][0]:.1f},{pts[2][1]-10:.1f} {highlight}" fill="none" stroke="#f3a0ac" stroke-width="6" opacity="0.45" stroke-linecap="round"/>
    </g>'''


smear = lip_smear(W/2, 1230, 560)
product = lipstick_product(W/2 - 10, 760)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>{"".join(_DEFS)}</defs>
  <rect width="{W}" height="{H}" fill="{g_bg}"/>
  <rect width="{W}" height="{H}" fill="{g_vign}"/>

  <rect x="40" y="40" width="{W-80}" height="{H-80}" fill="none" stroke="{GOLD}" stroke-width="2" opacity="0.6"/>

  <text x="{W/2}" y="200" font-family="{SANS}" font-size="16" letter-spacing="8" fill="{GOLD_DK}" text-anchor="middle" opacity="0.85">INTRODUCING THE NEW SHADE</text>
  <text x="{W/2}" y="305" font-family="{SERIF}" font-weight="700" font-size="118" letter-spacing="6" fill="{INK}" text-anchor="middle">PUREE</text>
  <text x="{W/2}" y="350" font-family="{SANS}" font-size="20" letter-spacing="6" fill="{GOLD_DK}" text-anchor="middle">LUXE MATTE LIPSTICK</text>

  {sparkle(W/2-260, 480, 1.1)}
  {sparkle(W/2+300, 560, 0.8)}
  {sparkle(W/2+260, 1000, 0.9)}

  {smear}
  {product}

  <text x="{W/2}" y="1340" font-family="{SERIF}" font-style="italic" font-size="34" fill="{INK}" text-anchor="middle">&#8220;Bare skin, bold lips.&#8221;</text>
  <text x="{W/2}" y="1390" font-family="{SANS}" font-size="17" letter-spacing="4" fill="{LIPSTICK_DK}" text-anchor="middle">SHADE 04 &#8212; CRIMSON SILK</text>

  <line x1="{W/2-90}" y1="1420" x2="{W/2+90}" y2="1420" stroke="{GOLD}" stroke-width="1.5" opacity="0.7"/>
  <text x="{W/2}" y="1452" font-family="{SANS}" font-size="15" letter-spacing="3" fill="{INK}" text-anchor="middle" opacity="0.75">PUREE COSMETICS · AVAILABLE NOW AT PUREE.COM</text>
</svg>'''

save("14_poster_puree_lipstick", svg, scale=1.6)
print(W, H)
