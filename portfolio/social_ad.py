from common import save, FONT_TC

W = H = 1080

def bottle(x, y, scale, cap, body):
    return f'''
    <g transform="translate({x},{y}) scale({scale})">
      <rect x="-46" y="-10" width="92" height="230" rx="20" fill="{body}"/>
      <rect x="-30" y="-46" width="60" height="46" rx="10" fill="{cap}"/>
      <rect x="-14" y="-66" width="28" height="26" rx="6" fill="{cap}"/>
      <rect x="-30" y="60" width="60" height="60" rx="8" fill="#ffffff" opacity="0.85"/>
    </g>'''

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="bg" cx="0.3" cy="0.25" r="1">
      <stop offset="0" stop-color="#fef3ea"/>
      <stop offset="1" stop-color="#f3d9c9"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>

  <circle cx="860" cy="180" r="260" fill="#f6c9a8" opacity="0.55"/>
  <circle cx="120" cy="920" r="220" fill="#e7a98c" opacity="0.45"/>

  <text x="90" y="160" font-family="{FONT_TC}" font-weight="700" font-size="34" letter-spacing="6" fill="#7a4a2e">AURA SKINCARE</text>

  <text x="90" y="320" font-family="{FONT_TC}" font-weight="900" font-size="96" fill="#4a2c1a">NEW</text>
  <text x="90" y="420" font-family="{FONT_TC}" font-weight="900" font-size="96" fill="#4a2c1a">GLOW</text>
  <text x="90" y="500" font-family="{FONT_TC}" font-weight="900" font-size="96" fill="#4a2c1a">SERUM</text>

  <rect x="90" y="540" width="230" height="64" rx="32" fill="#c9683c"/>
  <text x="205" y="582" font-family="{FONT_TC}" font-weight="700" font-size="28" letter-spacing="2" fill="#ffffff" text-anchor="middle">30% OFF</text>

  <text x="90" y="700" font-family="{FONT_TC}" font-weight="400" font-size="24" fill="#7a4a2e">Launch week only · while stocks last</text>

  {bottle(820, 700, 1.5, '#c9683c', '#fbe6d8')}
  {bottle(700, 760, 1.2, '#9c5230', '#f3d3bb')}

  <text x="90" y="980" font-family="{FONT_TC}" font-weight="700" font-size="28" letter-spacing="3" fill="#7a4a2e">SHOP NOW AT AURASKIN.CO</text>
</svg>'''

save("06_social_ad_aura", svg)
