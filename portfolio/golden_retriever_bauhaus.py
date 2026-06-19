"""Bauhaus-style geometric mark: a golden retriever profile built only from
circles, squares and triangles, fused with crossed fork+knife, in a single
ink color. No outline strokes, no illustrative line work - silhouette reads
purely through overlapping flat blocks of one color.
"""
from common import save

SANS = "Liberation Sans"
S = 900
BG = "#f6f4ef"
C = "#0f2c59"  # classic blue


def poly(*pts, fill=C):
    s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{s}" fill="{fill}"/>'


def circle(cx, cy, r, fill=C):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'


def rect(x, y, w, h, fill=C):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}"/>'


def crossed_cutlery(cx, cy, scale=1.0):
    def knife(rot):
        return f'''<g transform="rotate({rot})">
          <polygon points="0,-150 16,-32 -16,-32" fill="{C}"/>
          <rect x="-9" y="-32" width="18" height="120" fill="{C}"/>
        </g>'''

    def fork(rot):
        tines = []
        n, w, gap = 4, 11, 8
        total = n * w + (n - 1) * gap
        x0 = -total / 2
        for i in range(n):
            x = x0 + i * (w + gap)
            tines.append(f'<rect x="{x:.1f}" y="-150" width="{w}" height="70" fill="{C}"/>')
        neck = f'<polygon points="{x0:.1f},-80 {-x0:.1f},-80 14,-34 -14,-34" fill="{C}"/>'
        handle = f'<rect x="-9" y="-34" width="18" height="122" fill="{C}"/>'
        return f'<g transform="rotate({rot})">{"".join(tines)}{neck}{handle}</g>'

    # rotated 180deg from the "natural" reading so the handles tuck UP
    # into the collar (hidden) and the blade/tines hang DOWN, visible,
    # crossing in a clean X beneath the jaw
    return f'''<g transform="translate({cx},{cy}) scale({scale})">
      {fork(154)}
      {knife(206)}
    </g>'''


def build():
    hx, hy, hr = 430, 340, 170

    # skull
    head = circle(hx, hy, hr)

    # floppy ear: single-point hinge tucked inside the skull rim, flaring
    # into a wide triangular lobe that falls outside the skull and hangs
    # below it, capped with a circle for a blunt, rounded tip
    ear_body = poly((390, 200), (260, 430), (320, 560))
    ear_tip = circle(320, 560, 30)

    # muzzle: a true square block (blunt retriever muzzle, not a beak) that
    # overlaps deep into the skull on its left edge so the join has zero
    # visible seam, with a nose circle fused onto its leading face
    snout = rect(500, 270, 190, 140)
    nose = circle(682, 340, 40)

    # chin/collar block: square anchor the crossed cutlery's handles tuck
    # into, fused tight against the skull+muzzle above with zero seam
    jaw = rect(480, 400, 150, 135)

    # eye: negative-space diamond cut from the solid mass
    eye = poly((500, 278), (522, 300), (500, 322), (478, 300), fill=BG)

    # anchored inside the collar so the handles are swallowed by it and
    # only the blade + tines hang down below the jawline, crossing in an X
    cutlery = crossed_cutlery(555, 465, 1.45)

    wordmark = f'''
    <text x="{S/2}" y="800" font-family="{SANS}" font-weight="700" font-size="46" letter-spacing="11"
          fill="{C}" text-anchor="middle">GOLDEN HOUR</text>
    <line x1="{S/2-150}" y1="826" x2="{S/2+150}" y2="826" stroke="{C}" stroke-width="2"/>
    <text x="{S/2}" y="852" font-family="{SANS}" font-weight="400" font-size="15" letter-spacing="6"
          fill="{C}" text-anchor="middle">FINE DINING</text>
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <rect width="{S}" height="{S}" fill="{BG}"/>
      {ear_body}
      {ear_tip}
      {cutlery}
      {head}
      {snout}
      {jaw}
      {nose}
      {eye}
      {wordmark}
    </svg>'''


save("24_logo_golden_bauhaus", build(), scale=1.2)
