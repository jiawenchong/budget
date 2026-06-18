import cairosvg, os

OUT_SVG = os.path.join(os.path.dirname(__file__), "svg")
OUT_PNG = os.path.join(os.path.dirname(__file__), "png")
os.makedirs(OUT_SVG, exist_ok=True)
os.makedirs(OUT_PNG, exist_ok=True)

FONT_TC = "Noto Sans CJK TC"
FONT_TC_BLACK = "Noto Sans CJK TC Black"

def save(name, svg, scale=2):
    svg_path = os.path.join(OUT_SVG, f"{name}.svg")
    png_path = os.path.join(OUT_PNG, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    cairosvg.svg2png(url=svg_path, write_to=png_path, scale=scale, unsafe=True)
    print("rendered", png_path)
