"""Semiconductor logo concepts D & E, derived from the installed
`minimal` and `professional` design-system skills (.claude/skills/).
Tokens are taken directly from each skill's SKILL.md Style Foundations.
"""
from common import save

SANS = "Liberation Sans"
S = 900

# ---------- Concept D: tokens from the `minimal` skill ----------
# primary=#0C0C09 secondary=#312C85 surface=#F4F4F1 text=#0C0C09
# Style Foundations: "minimal, clean, bold" -> flat color only, no gradients,
# one accent, maximum whitespace, mark kept small relative to canvas.
D_BG = "#f4f4f1"
D_INK = "#0c0c09"
D_INDIGO = "#312c85"


def concept_d():
    cx, cy = S / 2, 380
    half = 110  # small mark, lots of whitespace per "minimal" rule

    # chip square with one chamfered corner (orientation mark) drawn as a single
    # stroked path - avoids overlay-cut artifacts from a separate notch shape
    x0, x2 = cx - half, cx + half
    y0, y2 = cy - half, cy + half
    x1, y1 = x0 + 34, y0 + 34
    chip = f'''
    <path d="M{x1},{y0} L{x2},{y0} L{x2},{y2} L{x0},{y2} L{x0},{y1} Z"
          fill="none" stroke="{D_INK}" stroke-width="10" stroke-linejoin="miter"/>
    '''

    # one pin per side only - reduced to the essential mark
    pin_len = 30
    pins = f'''
    <line x1="{cx}" y1="{cy-half-pin_len}" x2="{cx}" y2="{cy-half}" stroke="{D_INK}" stroke-width="10"/>
    <line x1="{cx}" y1="{cy+half}" x2="{cx}" y2="{cy+half+pin_len}" stroke="{D_INK}" stroke-width="10"/>
    <line x1="{cx-half-pin_len}" y1="{cy}" x2="{cx-half}" y2="{cy}" stroke="{D_INK}" stroke-width="10"/>
    <line x1="{cx+half}" y1="{cy}" x2="{cx+half+pin_len}" y2="{cy}" stroke="{D_INK}" stroke-width="10"/>
    '''

    # single accent: one indigo node at the center - the one allowed color
    accent = f'<circle cx="{cx}" cy="{cy}" r="14" fill="{D_INDIGO}"/>'

    wordmark = f'''
    <text x="{S/2}" y="{cy+260}" font-family="{SANS}" font-weight="700" font-size="42" letter-spacing="10"
          fill="{D_INK}" text-anchor="middle">ORGANIZATION NAME</text>
    <text x="{S/2}" y="{cy+296}" font-family="{SANS}" font-weight="300" font-size="14" letter-spacing="5"
          fill="{D_INDIGO}" text-anchor="middle">SEMICONDUCTOR &amp; IC DESIGN</text>
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <rect width="{S}" height="{S}" fill="{D_BG}"/>
      {pins}
      {chip}
      {accent}
      {wordmark}
    </svg>'''


# ---------- Concept E: tokens from the `professional` skill ----------
# primary=#FECE14 secondary=#000000 surface=#FFFFFF text=#111827
# Style Foundations: "modern", "structured layouts", "trustworthy visual identity"
# Amber used as a single restrained accent, not a dominant fill, to keep a
# B2B / fab-grade tone rather than a consumer electronics-shop look.
E_BG = "#ffffff"
E_BLACK = "#000000"
E_TEXT = "#111827"
E_AMBER = "#fece14"


def concept_e():
    cx, cy = S / 2, 380
    cell = 34
    gap = 10
    n = 5  # 5x5 structured grid of pins, per "structured layouts"
    grid_w = n * cell + (n - 1) * gap
    x0 = cx - grid_w / 2
    y0 = cy - grid_w / 2

    cells = []
    highlight = (2, 2)  # single amber cell at dead-center: the "active" point
    for r in range(n):
        for c in range(n):
            x = x0 + c * (cell + gap)
            y = y0 + r * (cell + gap)
            fill = E_AMBER if (r, c) == highlight else E_BLACK
            cells.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell}" height="{cell}" rx="3" fill="{fill}"/>')

    frame_pad = 28
    frame = f'''
    <rect x="{x0-frame_pad}" y="{y0-frame_pad}" width="{grid_w+frame_pad*2}" height="{grid_w+frame_pad*2}"
          rx="10" fill="none" stroke="{E_BLACK}" stroke-width="3"/>
    '''

    baseline = f'<line x1="{S/2-200}" y1="{cy+grid_w/2+frame_pad+46}" x2="{S/2+200}" y2="{cy+grid_w/2+frame_pad+46}" stroke="{E_BLACK}" stroke-width="2"/>'

    wordmark = f'''
    <text x="{S/2}" y="{cy+grid_w/2+frame_pad+86}" font-family="{SANS}" font-weight="700" font-size="40" letter-spacing="6"
          fill="{E_TEXT}" text-anchor="middle">ORGANIZATION NAME</text>
    <rect x="{S/2-176}" y="{cy+grid_w/2+frame_pad+100}" width="10" height="10" fill="{E_AMBER}"/>
    <text x="{S/2+6}" y="{cy+grid_w/2+frame_pad+110}" font-family="{SANS}" font-weight="500" font-size="14" letter-spacing="4"
          fill="{E_BLACK}" text-anchor="middle">SEMICONDUCTOR &amp; IC DESIGN</text>
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <rect width="{S}" height="{S}" fill="{E_BG}"/>
      {frame}
      {"".join(cells)}
      {baseline}
      {wordmark}
    </svg>'''


save("22_logo_semicon_minimal_skill", concept_d(), scale=1.2)
save("23_logo_semicon_professional_skill", concept_e(), scale=1.2)
