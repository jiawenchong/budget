"""'黄金时刻' (Golden Hour) dog-restaurant mark: a golden retriever head fused
with a sunburst (the 'golden hour' sun behind the head) and a bone held at
the jaw (the restaurant/food cue). Built only from circles, rects/squares
and triangles in a single warm ink color, no outline strokes - silhouette
reads purely through overlapping flat blocks (Bauhaus geometric fusion).
"""
import math
from common import save, FONT_TC

SANS = "Liberation Sans"
S = 900
BG = "#FBF3E6"
C = "#8C5212"  # warm amber-gold ink


def poly(*pts, fill=C):
    s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{s}" fill="{fill}"/>'


def circle(cx, cy, r, fill=C):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"/>'


def rect(x, y, w, h, fill=C):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}"/>'


def ellipse(cx, cy, rx, ry, rot=0, fill=C):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}"{t}/>'


def bone(cx, cy, length, thickness, angle_deg, fill=C):
    half = length / 2
    knob_r = thickness * 0.62
    off = thickness * 0.5
    return f'''<g transform="translate({cx},{cy}) rotate({angle_deg})">
      <rect x="{-half:.1f}" y="{-thickness/2:.1f}" width="{length:.1f}" height="{thickness:.1f}" fill="{fill}"/>
      <circle cx="{-half:.1f}" cy="{-off:.1f}" r="{knob_r:.1f}" fill="{fill}"/>
      <circle cx="{-half:.1f}" cy="{off:.1f}" r="{knob_r:.1f}" fill="{fill}"/>
      <circle cx="{half:.1f}" cy="{-off:.1f}" r="{knob_r:.1f}" fill="{fill}"/>
      <circle cx="{half:.1f}" cy="{off:.1f}" r="{knob_r:.1f}" fill="{fill}"/>
    </g>'''


def sun_rays(hx, hy, hr, n=5, start_deg=-148, end_deg=-32, inner=0.95, outer=42, spread_deg=6, tip_r=7):
    """Thin triangular rays, rounded at the tip, fanned around the top arc
    of the head circle - a calm sunburst halo (golden-hour sun) confined to
    the top of the head, clear of the ear (left) and muzzle (right)."""
    rays = []
    for i in range(n):
        a = math.radians(start_deg + (end_deg - start_deg) * i / (n - 1))
        a1 = a - math.radians(spread_deg)
        a2 = a + math.radians(spread_deg)
        bx1 = hx + hr * inner * math.cos(a1)
        by1 = hy + hr * inner * math.sin(a1)
        bx2 = hx + hr * inner * math.cos(a2)
        by2 = hy + hr * inner * math.sin(a2)
        tx = hx + (hr + outer) * math.cos(a)
        ty = hy + (hr + outer) * math.sin(a)
        rays.append(poly((bx1, by1), (bx2, by2), (tx, ty)))
        rays.append(circle(tx, ty, tip_r))
    return "".join(rays)


def build():
    hx, hy, hr = 440, 380, 175

    rays = sun_rays(hx, hy, hr)

    # floppy ear: an ellipse whose top lobe tucks inside the head circle
    # (hidden once the head is drawn on top) and whose bottom/outer lobe
    # hangs well clear of the head, reading as a rounded retriever ear
    ear = ellipse(300, 440, 50, 150, rot=-8)

    head = circle(hx, hy, hr)

    # muzzle: blunt rectangle block overlapping deep into the head on its
    # left edge, projecting a real chunk past the head's silhouette
    snout = rect(560, 305, 195, 135)
    nose = circle(752, 372, 42)

    # jaw/collar block beneath the muzzle - the bone's near end tucks under
    # this and is swallowed, leaving only the far end + knobs visible,
    # reading as "held in the mouth" rather than "stuck on"
    jaw = rect(520, 430, 150, 95)

    # bone (the restaurant/food cue) drawn before the jaw so its near end
    # is hidden by the jaw block painted on top
    dog_bone = bone(660, 545, 230, 56, 32)

    eye = poly((478, 330), (500, 352), (478, 374), (456, 352), fill=BG)

    wordmark = f'''
    <text x="{S/2}" y="800" font-family="{FONT_TC}" font-weight="900" font-size="58" letter-spacing="14"
          fill="{C}" text-anchor="middle">黄金时刻</text>
    <line x1="{S/2-160}" y1="826" x2="{S/2+160}" y2="826" stroke="{C}" stroke-width="2"/>
    <text x="{S/2}" y="852" font-family="{SANS}" font-weight="400" font-size="15" letter-spacing="5"
          fill="{C}" text-anchor="middle">GOLDEN HOUR &#183; DOG BISTRO</text>
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <rect width="{S}" height="{S}" fill="{BG}"/>
      {rays}
      {ear}
      {dog_bone}
      {head}
      {snout}
      {jaw}
      {nose}
      {eye}
      {wordmark}
    </svg>'''


save("25_logo_golden_hour_dog_cn", build(), scale=1.2)
