---
name: logo-design
description: Design single-color, geometrically-fused brand marks/logos — especially "dual-image" marks where one continuous silhouette reads as two different subjects at once (e.g. an animal pun, two nouns sharing a contour), and Bauhaus-style marks built only from circles/squares/triangles. Use this whenever the user asks for a logo, brand mark, or icon, wants two concepts/animals/words fused into one symbol, mentions a name that puns on two nouns, or wants a "high-end trademark" look rather than a cartoon illustration. Also use it for iterating on logo drafts, testing small-icon (favicon-scale) legibility, or applying a design-system skill's color tokens to a new mark.
---

# Logo Design

A skill for designing premium, single-color, geometrically-fused logo marks, and for
iterating on them rendered as SVG.

The core belief behind this skill: a logo reads as "high-value trademark" rather than
"cartoon illustration" when (1) it uses as few flat color fills as possible — ideally
one — with **no outline strokes and no illustrative line work**, and (2) every shape
boundary is doing double duty: it's simultaneously the edge of one subject and either
the edge of another subject (dual-image fusion) or a deliberate geometric primitive
(circle/square/triangle) chosen for contrast and "power" rather than smoothed into a
naturalistic curve.

## Golden sample: 魚你象遇 (Yu Ni Xiang Yu)

`assets/golden-sample-yunixiangyu-fish-elephant.png` is the reference standard for this
skill. The brand name puns 魚(fish)+你+象(elephant)+遇 ≈ 與你相遇 ("meet you"), and the
winning mark makes that pun *visible*, not just *named*:

- A single dark ink-colored blob, shaped like a paisley/yin-yang swirl.
- Read the left lobe and you see a **fish** (rounded body, tail-fin curl, one dot eye).
- Read the right lobe and you see an **elephant's head + trunk** (the trunk is the same
  curling line that forms the fish's tail; the elephant has its own dot eye lower down).
- The boundary between positive (ink) and negative (background) space is **one
  continuous curve** shared by both animals — neither animal is "added on top of" the
  other; each animal's silhouette is literally the other's negative space. This is the
  same family of trick as a yin-yang symbol or the hidden arrow in FedEx's wordmark.
- Decoration is minimal: two small dot eyes, nothing else. No outline, no shading, no
  fur/scale texture lines.

Compare this to `assets/alt-concept-1-*.png` and `assets/alt-concept-2-*.png` (the same
client's rejected directions): both *literally combine* a fish shape and an elephant
shape side by side or nested — additive, not fused. They read as "an elephant with a
fish-shaped ear," which is a weaker idea than "one curve, two animals." `alt-concept-3`
is a single-line/outline-stroke version, which the client also passed over — it breaks
this skill's "no outline strokes" preference and reads thinner/cheaper.

**The lesson to generalize, not copy literally:** when a brand name puns on two nouns
(or the brief asks to "fuse" two subjects), look first for a **shared-contour / negative
space trick** where one subject's outline doubles as the other's, before falling back to
literally placing two shapes next to each other. The shared-contour version is almost
always the more premium-looking result.

## Technique 2: Bauhaus geometric-primitive fusion

For briefs that ask for a "geometric", "Bauhaus", or "powerful block" look rather than an
organic dual-image swirl, build the subject from **only circles, squares/rects, and
triangles**, in one flat ink color, with **no strokes**. Shapes fuse seamlessly because
overlapping same-color fills never show a seam — only the silhouette boundary against the
background, and any deliberate negative-space cutouts (e.g. an eye as a background-color
diamond), are ever visible.

Practical rules learned from building these (see `references/geometric-fusion.md` for
the worked example and full reasoning):

1. **Predict containment with distance-from-center math before rendering.** For a vertex
   `(x, y)` and a circle at `(cx, cy)` with radius `r`, compute
   `dist = sqrt((x-cx)**2 + (y-cy)**2)`. If `dist < r` the vertex is swallowed by the
   circle (invisible, fused); if `dist > r` it pokes outside (visible, reads as a lobe).
   A shape with only ONE vertex outside a circle will look like a thin spike, not a
   lobe — for a believable "ear" or "limb", make sure the *visible* portion has real
   width, e.g. two outside vertices that are well separated from each other, not both
   converging toward the same point.
2. **Use draw order, not stroke, to fuse joins.** Draw the "background" shape (e.g. a
   head circle) *after* the shape it should swallow part of (e.g. an ear triangle) so the
   overlap is hidden with zero seam. Draw accessory shapes (e.g. cutlery, a held object)
   *before* the block they should appear to emerge from, so only the part sticking out
   past that block stays visible — this reads as "object emerging from / held by" rather
   than "object stuck on top of."
3. **Check every rotated/scaled sub-shape against the FULL silhouette union, not just
   the one shape you anchored it to.** A rotated group's farthest point can swing
   surprisingly far from its anchor (rotation distance ≈ local-distance × scale). If that
   point lands outside every shape that's supposed to cover it, you get a stray spike or
   sliver artifact. This was the single most common bug encountered building these marks
   — always trace where the extreme points of rotated groups actually land before trusting
   it'll be hidden.
4. **Prefer blunt blocks over thin wedges for things that should read as solid parts**
   (a muzzle, a limb, a handle). A triangle wedge that's 90% inside a containing circle
   leaves only a thin sliver visible, which reads as a beak/spike, not a blunt part. A
   rectangle that overlaps the containing shape on one edge and projects a real chunk
   (e.g. 60-100px at full logo scale) past it reads as solid and intentional.

## Workflow

1. **Clarify the brief**: brand name (and whether it puns on two nouns), single accent
   ink color (ask for a hex if not given), and whether the mood is organic/dual-image
   (technique 1) or geometric/Bauhaus (technique 2). If the project has installed
   design-system skills (e.g. `minimal`, `professional` — check `.claude/skills/`), and
   the user references one, pull its color tokens rather than inventing new ones.
2. **Sketch coordinates before coding.** Decide the anchor circle/blob (center + radius)
   first, then place every other shape's vertices with explicit coordinates, running the
   distance-from-center check from rule 1 above on each one. Don't guess-and-check
   blindly in code when the math is one line.
3. **Build as SVG via Python f-strings**, following this project's convention in
   `portfolio/common.py`: write a `build()` function returning an SVG string, call
   `save(name, svg, scale=1.2)` to render both `portfolio/svg/<name>.svg` and
   `portfolio/png/<name>.png` (uses `cairosvg`).
4. **Render, then visually inspect** the PNG (read it directly, and crop tight on the
   mark with `PIL` if the canvas has a lot of margin/wordmark padding around it).
5. **Test small-icon legibility**: crop to just the mark, downsample to 64×64 with
   `Image.LANCZOS`, then upsample with `Image.NEAREST` for inspection. A mark that's only
   legible at full size will fail as a favicon/app icon — simplify until the silhouette
   still reads at 64×64.
6. **Iterate render → inspect → adjust** before showing the user anything. Budget for
   several rounds — getting a fused silhouette to read correctly as the *intended*
   subject(s) with no stray artifacts typically takes multiple passes, even with the
   math from rule 1 done up front.
7. Once satisfied, deliver the PNG to the user and explain in one or two sentences which
   technique was used and why (dual-image fusion vs. geometric-primitive fusion).

## Anti-patterns

- Forcing one shape to literally double as two unrelated objects (e.g. "this triangle is
  both the ear AND part of the knife") just because they happen to be near each other —
  this usually reads as confusing rather than clever. Reserve the "double duty" idea for
  cases where it's a deliberate negative-space/shared-contour trick (technique 1), and
  otherwise keep elements distinct-but-overlap-fused (technique 2).
- Outline strokes or illustrative detail lines "to help it read" — if the silhouette
  needs an outline to be understood, the shapes need to change, not gain a stroke.
- Skipping the small-icon legibility check — a mark that only works at poster size isn't
  done.
