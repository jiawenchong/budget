from PIL import Image, ImageDraw

ACCENT = '#2f7d6b'

def make_icon(size, path):
    img = Image.new('RGB', (size, size), ACCENT)
    draw = ImageDraw.Draw(img)
    cx, cy = size / 2, size / 2
    r = size * 0.30
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill='white')
    r2 = r * 0.8
    ring_w = max(2, int(size * 0.03))
    draw.ellipse([cx - r2, cy - r2, cx + r2, cy + r2], outline=ACCENT, width=ring_w)
    bar_w = r * 0.9
    bar_t = size * 0.045
    draw.rectangle([cx - bar_w / 2, cy - bar_t / 2, cx + bar_w / 2, cy + bar_t / 2], fill=ACCENT)
    img.save(path)

make_icon(192, '/home/user/budget/icon-192.png')
make_icon(512, '/home/user/budget/icon-512.png')
make_icon(180, '/home/user/budget/icon-180.png')
print('done')
