from common import save, FONT_TC
import random

W, H = 1000, 1400
random.seed(7)

circles = []
palette = ["#ff6b6b", "#ffd166", "#06d6a0", "#118ab2", "#ef476f"]
for i in range(26):
    cx = random.uniform(0, W)
    cy = random.uniform(0, 520)
    r = random.uniform(8, 30)
    c = random.choice(palette)
    circles.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{c}" opacity="{random.uniform(0.5,0.9):.2f}"/>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2b1055"/>
      <stop offset="0.55" stop-color="#7b2ff7"/>
      <stop offset="1" stop-color="#ff6b6b"/>
    </linearGradient>
    <linearGradient id="sun" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd166"/>
      <stop offset="1" stop-color="#ef476f"/>
    </linearGradient>
  </defs>

  <rect width="{W}" height="{H}" fill="#120822"/>
  <rect width="{W}" height="780" fill="url(#sky)"/>
  <circle cx="500" cy="360" r="190" fill="url(#sun)"/>

  {''.join(circles)}

  <!-- mountains silhouette -->
  <polygon points="0,780 220,560 380,720 520,500 700,700 880,580 1000,780" fill="#1a0e30"/>
  <polygon points="0,780 150,640 320,760 470,610 650,760 820,650 1000,780" fill="#0d0618"/>

  <!-- crowd silhouette -->
  <g fill="#0d0618">
    <circle cx="120" cy="745" r="14"/><rect x="106" y="755" width="28" height="40"/>
    <circle cx="180" cy="750" r="14"/><rect x="166" y="760" width="28" height="36"/>
    <circle cx="260" cy="742" r="16"/><rect x="244" y="754" width="32" height="44"/>
    <circle cx="340" cy="748" r="14"/><rect x="326" y="758" width="28" height="38"/>
    <circle cx="420" cy="744" r="15"/><rect x="405" y="755" width="30" height="42"/>
    <circle cx="520" cy="750" r="14"/><rect x="506" y="760" width="28" height="36"/>
    <circle cx="600" cy="743" r="16"/><rect x="584" y="755" width="32" height="44"/>
    <circle cx="690" cy="748" r="14"/><rect x="676" y="758" width="28" height="38"/>
    <circle cx="770" cy="745" r="15"/><rect x="755" y="756" width="30" height="40"/>
    <circle cx="860" cy="750" r="14"/><rect x="846" y="760" width="28" height="36"/>
  </g>

  <rect x="0" y="780" width="{W}" height="{H-780}" fill="#120822"/>

  <text x="500" y="940" font-family="{FONT_TC}" font-weight="900" font-size="120" letter-spacing="4" fill="#ffffff" text-anchor="middle">SUNSET</text>
  <text x="500" y="1040" font-family="{FONT_TC}" font-weight="900" font-size="74" letter-spacing="10" fill="#ffd166" text-anchor="middle">MUSIC FESTIVAL</text>

  <line x1="260" y1="1090" x2="740" y2="1090" stroke="#ef476f" stroke-width="3"/>

  <text x="500" y="1160" font-family="{FONT_TC}" font-weight="700" font-size="34" letter-spacing="2" fill="#ffffff" text-anchor="middle">AUGUST 14 – 16 · CLEARWATER BAY PARK</text>
  <text x="500" y="1210" font-family="{FONT_TC}" font-weight="400" font-size="26" fill="#c9b8e8" text-anchor="middle">3 STAGES · 40+ ARTISTS · FOOD &amp; ART MARKET</text>

  <rect x="370" y="1255" width="260" height="70" rx="35" fill="#ef476f"/>
  <text x="500" y="1300" font-family="{FONT_TC}" font-weight="700" font-size="30" letter-spacing="2" fill="#ffffff" text-anchor="middle">GET TICKETS</text>
</svg>'''

save("05_poster_festival", svg)
