from common import save, FONT_TC

W = H = 1000
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="navy" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0b1f3a"/>
      <stop offset="1" stop-color="#16335c"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#c9a45c"/>
      <stop offset="1" stop-color="#e9d3a3"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="#f7f5f0"/>

  <!-- mark: three ascending peaks forming abstract M / mountain -->
  <g>
    <polygon points="500,300 380,520 620,520" fill="url(#navy)"/>
    <polygon points="380,360 290,520 470,520" fill="#16335c" opacity="0.85"/>
    <polygon points="620,360 530,520 710,520" fill="#16335c" opacity="0.85"/>
    <polygon points="500,300 460,370 540,370" fill="url(#gold)"/>
    <rect x="290" y="520" width="420" height="10" fill="url(#gold)"/>
  </g>

  <text x="500" y="640" font-family="{FONT_TC}" font-weight="700" font-size="74"
        letter-spacing="14" fill="#16335c" text-anchor="middle">MERIDIAN</text>
  <text x="500" y="690" font-family="{FONT_TC}" font-weight="400" font-size="26"
        letter-spacing="6" fill="#c9a45c" text-anchor="middle">STRATEGY · DESIGN · GROWTH</text>

  <line x1="350" y1="715" x2="650" y2="715" stroke="#c9a45c" stroke-width="2"/>
</svg>'''

save("01_logo_meridian", svg)
