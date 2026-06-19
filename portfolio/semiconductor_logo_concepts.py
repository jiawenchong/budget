import math
from common import save

SANS = "Liberation Sans"

BG = "#f3f5f8"
NAVY = "#0c2440"
NAVY_DK = "#071829"
STEEL = "#8b99aa"
STEEL_LT = "#cfd7e0"
TECH_BLUE = "#1f6feb"
CYAN = "#2bd9e8"
INK = "#0c2440"

S = 900
_DEFS = []

def grad(id_, kind, stops, **attrs):
    attr_str = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    stops_svg = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in stops)
    _DEFS.append(f'<{kind}Gradient id="{id_}" {attr_str}>{stops_svg}</{kind}Gradient>')
    return f"url(#{id_})"

g_navy = grad("g_navy", "linear", [(0, NAVY, 1), (1, NAVY_DK, 1)], x1="0", y1="0", x2="1", y2="1")
g_accent = grad("g_accent", "linear", [(0, CYAN, 1), (1, TECH_BLUE, 1)], x1="0", y1="0", x2="1", y2="1")
g_steel = grad("g_steel", "linear", [(0, STEEL_LT, 1), (1, STEEL, 1)], x1="0", y1="0", x2="0", y2="1")


def wordmark(name, subtitle, y=730):
    return f'''
    <text x="{S/2}" y="{y}" font-family="{SANS}" font-weight="700" font-size="44" letter-spacing="9" fill="{INK}" text-anchor="middle">{name}</text>
    <line x1="{S/2-150}" y1="{y+26}" x2="{S/2+150}" y2="{y+26}" stroke="{STEEL}" stroke-width="1.5"/>
    <text x="{S/2}" y="{y+54}" font-family="{SANS}" font-weight="400" font-size="15" letter-spacing="4" fill="{STEEL}" text-anchor="middle">{subtitle}</text>
    '''


# ---------- Concept A: chip outline + wafer notch + circuit traces ----------
def concept_a():
    cx, cy = S/2, 360
    chip = 230

    def pins(side):
        out = []
        n = 5
        for i in range(n):
            t = (i + 0.5) / n
            if side in ("l", "r"):
                y = cy - chip + t * chip * 2
                x0 = cx - chip - 28 if side == "l" else cx + chip
                x1 = cx - chip if side == "l" else cx + chip + 28
                out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{NAVY}" stroke-width="7"/>')
            else:
                x = cx - chip + t * chip * 2
                y0 = cy - chip - 28 if side == "t" else cy + chip
                y1 = cy - chip if side == "t" else cy + chip + 28
                out.append(f'<line x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y1}" stroke="{NAVY}" stroke-width="7"/>')
        return "".join(out)

    chip_body = f'''
    <rect x="{cx-chip}" y="{cy-chip}" width="{chip*2}" height="{chip*2}" rx="22" fill="none" stroke="{NAVY}" stroke-width="9"/>
    <rect x="{cx-chip+22}" y="{cy-chip+22}" width="{chip*2-44}" height="{chip*2-44}" rx="10" fill="none" stroke="{STEEL}" stroke-width="2" opacity="0.6"/>
    '''

    wafer_r = 118
    notch = f'''
    <path d="M{cx},{cy-wafer_r} A{wafer_r},{wafer_r} 0 1 1 {cx-0.01},{cy-wafer_r} L{cx-26},{cy-wafer_r+8} A28,28 0 0 0 {cx+26},{cy-wafer_r+8} Z"
          fill="{g_steel}" stroke="{NAVY}" stroke-width="3"/>
    '''
    wafer_lines = "".join(
        f'<line x1="{cx-wafer_r+18}" y1="{cy-wafer_r+18+i*40}" x2="{cx+wafer_r-18}" y2="{cy-wafer_r+18+i*40}" stroke="{NAVY}" stroke-width="1" opacity="0.18"/>'
        for i in range(6)
    )

    traces = f'''
    <path d="M{cx-chip+10},{cy-90} H{cx-wafer_r-30} Q{cx-wafer_r-10},{cy-90} {cx-wafer_r-10},{cy-70} V{cy-30}"
          stroke="{g_accent}" stroke-width="5" fill="none"/>
    <path d="M{cx+chip-10},{cy+90} H{cx+wafer_r+30} Q{cx+wafer_r+10},{cy+90} {cx+wafer_r+10},{cy+70} V{cy+30}"
          stroke="{g_accent}" stroke-width="5" fill="none"/>
    <circle cx="{cx-wafer_r-10}" cy="{cy-30}" r="6" fill="{CYAN}"/>
    <circle cx="{cx+wafer_r+10}" cy="{cy+30}" r="6" fill="{CYAN}"/>
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <defs>{"".join(_DEFS)}</defs>
      <rect width="{S}" height="{S}" fill="{BG}"/>
      {pins('l')}{pins('r')}{pins('t')}{pins('b')}
      {chip_body}
      {traces}
      {notch}
      {wafer_lines}
      {wordmark("ORGANIZATION NAME", "SEMICONDUCTOR · PANEL · IC DESIGN · R&amp;D")}
    </svg>'''


# ---------- Concept B: connected node network ----------
def concept_b():
    cx, cy = S/2, 360
    R = 175

    nodes = []
    n = 6
    pts = []
    for i in range(n):
        ang = math.radians(-90 + i * 360 / n)
        pts.append((cx + R * math.cos(ang), cy + R * math.sin(ang)))

    lines = []
    for i in range(n):
        x1, y1 = pts[i]
        lines.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{STEEL}" stroke-width="3"/>')
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        lines.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{STEEL}" stroke-width="2" opacity="0.55"/>')

    outer_nodes = []
    labels_r = ["IC", "SW", "HW", "FAB", "PNL", "ATP"]
    for i, (x, y) in enumerate(pts):
        outer_nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="26" fill="{g_accent}"/>')
        outer_nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="26" fill="none" stroke="{NAVY}" stroke-width="2"/>')
        outer_nodes.append(f'<text x="{x:.1f}" y="{y+5:.1f}" font-family="{SANS}" font-weight="700" font-size="14" letter-spacing="1" fill="#ffffff" text-anchor="middle">{labels_r[i]}</text>')

    center_node = f'''
    <circle cx="{cx}" cy="{cy}" r="56" fill="{g_navy}"/>
    <circle cx="{cx}" cy="{cy}" r="56" fill="none" stroke="{STEEL}" stroke-width="2" opacity="0.6"/>
    '''

    ring = f'<circle cx="{cx}" cy="{cy}" r="{R+62}" fill="none" stroke="{STEEL_LT}" stroke-width="1.5" opacity="0.7"/>'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <defs>{"".join(_DEFS)}</defs>
      <rect width="{S}" height="{S}" fill="{BG}"/>
      {ring}
      {"".join(lines)}
      {center_node}
      {"".join(outer_nodes)}
      {wordmark("ORGANIZATION NAME", "SEMICONDUCTOR · PANEL · IC DESIGN · R&amp;D")}
    </svg>'''


# ---------- Concept C: measurement bracket + modular stack ----------
def concept_c():
    cx, cy = S/2, 370

    def corner_bracket(x, y, rot, size=70, w=10):
        return f'''<g transform="translate({x},{y}) rotate({rot})">
          <path d="M0,{size} V0 H{size}" stroke="{NAVY}" stroke-width="{w}" fill="none" stroke-linecap="square"/>
        </g>'''

    bx0, by0, bx1, by1 = cx - 220, cy - 200, cx + 220, cy + 200
    brackets = (
        corner_bracket(bx0, by0, 0)
        + corner_bracket(bx1, by0, 90)
        + corner_bracket(bx1, by1, 180)
        + corner_bracket(bx0, by1, 270)
    )

    ticks = []
    for i in range(9):
        y = by0 + 30 + i * 18
        if y > by1 - 30:
            break
        length = 16 if i % 2 == 0 else 9
        ticks.append(f'<line x1="{bx0-4}" y1="{y:.1f}" x2="{bx0-4-length}" y2="{y:.1f}" stroke="{STEEL}" stroke-width="3"/>')
    for i in range(9):
        x = bx0 + 30 + i * 18
        if x > bx1 - 30:
            break
        length = 16 if i % 2 == 0 else 9
        ticks.append(f'<line x1="{x:.1f}" y1="{by0-4}" x2="{x:.1f}" y2="{by0-4-length}" stroke="{STEEL}" stroke-width="3"/>')

    stack = []
    widths = [260, 200, 140, 80]
    colors = [g_steel, g_navy, g_accent, NAVY]
    base_y = cy + 110
    for i, w in enumerate(widths):
        y = base_y - i * 46
        stack.append(f'<rect x="{cx-w/2}" y="{y-30}" width="{w}" height="40" rx="4" fill="{colors[i]}" stroke="{NAVY_DK}" stroke-width="1.5" opacity="{0.95 if i>0 else 1}"/>')

    crosshair = f'''
    <line x1="{cx-18}" y1="{cy-260}" x2="{cx+18}" y2="{cy-260}" stroke="{STEEL}" stroke-width="3"/>
    <line x1="{cx}" y1="{cy-274}" x2="{cx}" y2="{cy-246}" stroke="{STEEL}" stroke-width="3"/>
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <defs>{"".join(_DEFS)}</defs>
      <rect width="{S}" height="{S}" fill="{BG}"/>
      {brackets}
      {"".join(ticks)}
      {crosshair}
      {"".join(stack)}
      {wordmark("ORGANIZATION NAME", "SEMICONDUCTOR · PANEL · IC DESIGN · R&amp;D")}
    </svg>'''


save("19_logo_semicon_concept_a", concept_a(), scale=1.2)
save("20_logo_semicon_concept_b", concept_b(), scale=1.2)
save("21_logo_semicon_concept_c", concept_c(), scale=1.2)
