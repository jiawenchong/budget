import math
from common import save, FONT_TC_BLACK

SANS = "Liberation Sans"

CARAMEL = "#c9893c"
CARAMEL_DK = "#9c6a2c"
CREAM = "#fff6e0"
CREAM_DK = "#f3d98a"
ORANGE = "#e8632f"
ORANGE_DK = "#b8431a"
BROWN = "#5a3a22"
BROWN_DK = "#3a2412"
PINK = "#e87a8a"

S = 900

def badge_ring(fill=CARAMEL, r=420):
    return f'''
    <circle cx="{S/2}" cy="{S/2}" r="{r}" fill="{fill}"/>
    <circle cx="{S/2}" cy="{S/2}" r="{r-16}" fill="none" stroke="{CREAM}" stroke-width="4" opacity="0.6"/>
    '''

def ribbon(text_cn, text_en, y=720, w=560, fill=ORANGE):
    h = 130
    x = S/2 - w/2
    return f'''
    <path d="M{x},{y} L{x+w},{y} L{x+w-22},{y+h} L{x+w*0.5+30},{y+h-18} L{x+w*0.5-30},{y+h-18} L{x+22},{y+h} Z" fill="{fill}"/>
    <path d="M{x},{y} L{x-26},{y+22} L{x+10},{y+40} Z" fill="{ORANGE_DK}"/>
    <path d="M{x+w},{y} L{x+w+26},{y+22} L{x+w-10},{y+40} Z" fill="{ORANGE_DK}"/>
    <text x="{S/2}" y="{y+52}" font-family="{FONT_TC_BLACK}" font-weight="900" font-size="40" fill="{CREAM}" text-anchor="middle">{text_cn}</text>
    <text x="{S/2}" y="{y+88}" font-family="{SANS}" font-weight="700" font-size="20" letter-spacing="3" fill="{CREAM_DK}" text-anchor="middle">{text_en}</text>
    '''

def steam(cx, cy, h=70, w=16, opacity=0.55):
    paths = []
    for dx, sway in [(-1, 10), (0, -8), (1, 10)]:
        x = cx + dx * w
        paths.append(f'<path d="M{x},{cy} C{x+sway},{cy-h*0.4} {x-sway},{cy-h*0.7} {x},{cy-h}" stroke="{CREAM}" stroke-width="7" fill="none" stroke-linecap="round" opacity="{opacity}"/>')
    return "".join(paths)


# ---------- Concept A: dog-head plate + bone cutlery ----------
def concept_a():
    cx, cy = S/2, 380
    plate_r = 200
    ear = f'''
    <path d="M{cx-150},{cy-150} Q{cx-230},{cy-260} {cx-110},{cy-230} Q{cx-90},{cy-180} {cx-110},{cy-130} Z" fill="{CARAMEL_DK}"/>
    <path d="M{cx+150},{cy-150} Q{cx+230},{cy-260} {cx+110},{cy-230} Q{cx+90},{cy-180} {cx+110},{cy-130} Z" fill="{CARAMEL_DK}"/>
    '''
    plate = f'''
    <ellipse cx="{cx}" cy="{cy+18}" rx="{plate_r+10}" ry="{plate_r-10}" fill="{BROWN}" opacity="0.18"/>
    <circle cx="{cx}" cy="{cy}" r="{plate_r}" fill="{CREAM}"/>
    <circle cx="{cx}" cy="{cy}" r="{plate_r-26}" fill="none" stroke="{CREAM_DK}" stroke-width="6"/>
    '''
    face = f'''
    <ellipse cx="{cx-66}" cy="{cy-28}" rx="16" ry="20" fill="{BROWN_DK}"/>
    <ellipse cx="{cx+66}" cy="{cy-28}" rx="16" ry="20" fill="{BROWN_DK}"/>
    <ellipse cx="{cx-60}" cy="{cy-34}" rx="5" ry="6" fill="#fff" opacity="0.8"/>
    <ellipse cx="{cx+72}" cy="{cy-34}" rx="5" ry="6" fill="#fff" opacity="0.8"/>
    <ellipse cx="{cx}" cy="{cy+30}" rx="26" ry="18" fill="{BROWN_DK}"/>
    <path d="M{cx-40},{cy+50} Q{cx},{cy+86} {cx+40},{cy+50}" stroke="{BROWN_DK}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <ellipse cx="{cx-10}" cy="{cy+22}" rx="6" ry="4" fill="#fff" opacity="0.7"/>
    '''
    def bone(x, y, rot, scale=1.0, fill=CREAM):
        return f'''<g transform="translate({x},{y}) rotate({rot}) scale({scale})">
          <rect x="-70" y="-13" width="140" height="26" rx="13" fill="{fill}"/>
          <circle cx="-70" cy="-13" r="16" fill="{fill}"/><circle cx="-70" cy="13" r="16" fill="{fill}"/>
          <circle cx="70" cy="-13" r="16" fill="{fill}"/><circle cx="70" cy="13" r="16" fill="{fill}"/>
        </g>'''
    cutlery_y = 660
    fork = f'''<g transform="translate({cx-90},{cutlery_y}) rotate(-18)">
      <rect x="-6" y="-90" width="12" height="150" rx="6" fill="{BROWN}"/>
      <path d="M-22,-150 L-22,-95 M-7,-150 L-7,-95 M8,-150 L8,-95 M23,-150 L23,-95" stroke="{BROWN}" stroke-width="9" stroke-linecap="round"/>
      <path d="M-26,-95 Q0,-75 26,-95 L24,-80 Q0,-62 -24,-80 Z" fill="{BROWN}"/>
    </g>'''
    knife = f'''<g transform="translate({cx+90},{cutlery_y}) rotate(18)">
      <rect x="-6" y="-30" width="12" height="120" rx="6" fill="{BROWN}"/>
      <path d="M-14,-150 Q24,-130 14,-36 L-14,-36 Z" fill="{BROWN}"/>
    </g>'''
    bone_under = bone(cx, cutlery_y+10, 0, 1.0, CREAM_DK)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <rect width="{S}" height="{S}" fill="{CREAM}"/>
      {badge_ring()}
      {steam(cx-70, cy-220, 60, 14)}
      {steam(cx+70, cy-225, 65, 14)}
      {ear}
      {plate}
      {face}
      {bone_under}
      {fork}
      {knife}
      {ribbon("旺福食堂", "WAG &amp; DINE")}
    </svg>'''


# ---------- Concept B: chef-hat dog, tongue out ----------
def concept_b():
    cx, cy = S/2, 360
    head_r = 165
    ears = f'''
    <path d="M{cx-120},{cy-70} Q{cx-205},{cy-25} {cx-178},{cy+62} Q{cx-152},{cy+92} {cx-115},{cy+48} Q{cx-98},{cy-12} {cx-120},{cy-70} Z" fill="{CARAMEL_DK}"/>
    <path d="M{cx+120},{cy-70} Q{cx+205},{cy-25} {cx+178},{cy+62} Q{cx+152},{cy+92} {cx+115},{cy+48} Q{cx+98},{cy-12} {cx+120},{cy-70} Z" fill="{CARAMEL_DK}"/>
    '''
    head = f'<circle cx="{cx}" cy="{cy}" r="{head_r}" fill="{CARAMEL}"/>'
    muzzle = f'<ellipse cx="{cx}" cy="{cy+55}" rx="92" ry="68" fill="{CREAM}"/>'
    eyes = f'''
    <ellipse cx="{cx-58}" cy="{cy-20}" rx="15" ry="19" fill="{BROWN_DK}"/>
    <ellipse cx="{cx+58}" cy="{cy-20}" rx="15" ry="19" fill="{BROWN_DK}"/>
    <circle cx="{cx-52}" cy="{cy-26}" r="5" fill="#fff" opacity="0.85"/>
    <circle cx="{cx+64}" cy="{cy-26}" r="5" fill="#fff" opacity="0.85"/>
    <ellipse cx="{cx-90}" cy="{cy+18}" rx="20" ry="13" fill="{PINK}" opacity="0.55"/>
    <ellipse cx="{cx+90}" cy="{cy+18}" rx="20" ry="13" fill="{PINK}" opacity="0.55"/>
    '''
    nose = f'<ellipse cx="{cx}" cy="{cy+34}" rx="22" ry="16" fill="{BROWN_DK}"/><ellipse cx="{cx-7}" cy="{cy+28}" rx="6" ry="4" fill="#fff" opacity="0.6"/>'
    mouth = f'<path d="M{cx},{cy+48} Q{cx},{cy+62} {cx-20},{cy+66}" stroke="{BROWN_DK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    tongue = f'''<path d="M{cx-4},{cy+58} Q{cx-4},{cy+92} {cx+5},{cy+98} Q{cx+22},{cy+92} {cx+10},{cy+62} Z" fill="{PINK}"/>
      <line x1="{cx+3}" y1="{cy+72}" x2="{cx+3}" y2="{cy+88}" stroke="#c85a6e" stroke-width="3" opacity="0.6"/>'''
    chef_hat = f'''
    <rect x="{cx-72}" y="{cy-188}" width="144" height="40" rx="10" fill="#ffffff"/>
    <rect x="{cx-72}" y="{cy-150}" width="144" height="14" fill="{CARAMEL_DK}"/>
    <path d="M{cx-70},{cy-188} Q{cx-100},{cy-260} {cx-30},{cy-230} Q{cx},{cy-270} {cx+30},{cy-230} Q{cx+100},{cy-260} {cx+70},{cy-188} Z" fill="#ffffff"/>
    <circle cx="{cx-40}" cy="{cy-225}" r="22" fill="#ffffff"/>
    <circle cx="{cx+40}" cy="{cy-225}" r="22" fill="#ffffff"/>
    <circle cx="{cx}" cy="{cy-240}" r="24" fill="#ffffff"/>
    '''
    bowl = f'''
    <ellipse cx="{cx}" cy="{cy+205}" rx="120" ry="26" fill="{BROWN}"/>
    <path d="M{cx-120},{cy+195} Q{cx},{cy+250} {cx+120},{cy+195} L{cx+108},{cy+205} Q{cx},{cy+240} {cx-108},{cy+205} Z" fill="{ORANGE}"/>
    <ellipse cx="{cx}" cy="{cy+195}" rx="108" ry="20" fill="{CREAM_DK}"/>
    {steam(cx, cy+178, 50, 16, 0.5)}
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <rect width="{S}" height="{S}" fill="{CREAM}"/>
      {badge_ring(fill=ORANGE)}
      {ears}
      {head}
      {muzzle}
      {eyes}
      {nose}
      {mouth}
      {tongue}
      {chef_hat}
      {bowl}
      {ribbon("旺福食堂", "WAG &amp; DINE", y=700)}
    </svg>'''


# ---------- Concept C: abstract paw print + cutlery ----------
def concept_c():
    cx, cy = S/2, 380

    def toe(dx, dy, rx, ry, rot):
        return f'<ellipse cx="{dx}" cy="{dy}" rx="{rx}" ry="{ry}" fill="{CARAMEL_DK}" transform="rotate({rot} {dx} {dy})"/>'

    pad = f'<path d="M{cx-95},{cy+40} Q{cx},{cy-40} {cx+95},{cy+40} Q{cx+70},{cy+150} {cx},{cy+150} Q{cx-70},{cy+150} {cx-95},{cy+40} Z" fill="{CARAMEL_DK}"/>'

    toes = (
        toe(cx-110, cy-90, 34, 44, -18)
        + toe(cx-40, cy-130, 34, 46, -4)
        + toe(cx+40, cy-130, 34, 46, 4)
        + toe(cx+110, cy-90, 34, 44, 18)
    )

    spoon = f'''<g transform="translate({cx-40},{cy+10}) rotate(-8)">
      <ellipse cx="0" cy="-92" rx="26" ry="36" fill="{CREAM}"/>
      <rect x="-7" y="-60" width="14" height="170" rx="7" fill="{CREAM}"/>
    </g>'''
    fork = f'''<g transform="translate({cx+40},{cy+10}) rotate(8)">
      <path d="M-20,-130 L-20,-78 M-7,-132 L-7,-78 M7,-132 L7,-78 M20,-130 L20,-78" stroke="{CREAM}" stroke-width="11" stroke-linecap="round"/>
      <path d="M-24,-78 Q0,-58 24,-78 L22,-62 Q0,-46 -22,-62 Z" fill="{CREAM}"/>
      <rect x="-7" y="-66" width="14" height="156" rx="7" fill="{CREAM}"/>
    </g>'''

    ear_tri = f'''
    <path d="M{cx-150},{cy-220} L{cx-60},{cy-220} L{cx-130},{cy-90} Z" fill="{ORANGE}"/>
    <path d="M{cx+150},{cy-220} L{cx+60},{cy-220} L{cx+130},{cy-90} Z" fill="{ORANGE}"/>
    '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
      <rect width="{S}" height="{S}" fill="{CREAM}"/>
      {badge_ring(fill=CARAMEL)}
      {ear_tri}
      {pad}
      {toes}
      {spoon}{fork}
      {ribbon("旺福食堂", "WAG &amp; DINE", y=700)}
    </svg>'''


save("15_logo_dog_concept_a", concept_a(), scale=1.2)
save("16_logo_dog_concept_b", concept_b(), scale=1.2)
save("17_logo_dog_concept_c", concept_c(), scale=1.2)
