# Worked example: Bauhaus geometric-primitive fusion

This walks through building a real mark (a "GOLDEN HOUR" restaurant logo: a golden
retriever side-profile fused with crossed fork+knife, single color `#0f2c59`, only
circles/squares/triangles, no strokes) so the reasoning in `SKILL.md` technique 2 has a
concrete reference instead of just abstract rules.

## The math that should happen before any code is written

Pick the anchor circle first: `hx, hy, hr = 430, 340, 170` (the skull).

For every other shape's vertices, compute distance from `(hx, hy)` and compare to `hr`
to predict what will actually render:

```
dist(x, y) = sqrt((x - hx)**2 + (y - hy)**2)
```

- `dist < hr` → swallowed by the head circle, invisible (fine for hinge/anchor points).
- `dist > hr` → pokes outside, visible (fine for the parts that should read as a limb).

The first three attempts at the floppy ear failed for predictable reasons once checked
against this formula:

1. **Attempt 1** — the ear triangle had only one vertex outside the circle and the
   other two deep inside (`dist` ~100-120 vs `hr=150` in that draft). Only a thin
   tapering sliver was visible outside the circle — it read as a stalk with a ball on
   the end, not a floppy ear.
2. **Attempt 2** — pushed two vertices outside, but they were placed at almost the same
   height, so the visible region spread sideways into a kite/sail shape instead of
   hanging downward.
3. **Attempt 3 (final)** — `ear_body = poly((390, 200), (260, 430), (320, 560))`:
   - hinge `(390, 200)`: `dist = sqrt(40² + 140²) ≈ 145.6 < 170` → inside, hidden anchor.
   - bulge `(260, 430)`: `dist = sqrt(170² + 90²) ≈ 192.4 > 170` → outside, visible.
   - tip `(320, 560)`: `dist = sqrt(110² + 220²) ≈ 246.3 > 170` → outside, visible, and
     well below the head's own bottom edge (`hy + hr = 510`), so it genuinely hangs down
     rather than just poking sideways.
   - A capping circle `circle(320, 560, 30)` rounds the bottom tip so it doesn't end in
     a sharp triangle corner.

The same kind of check applies to the muzzle: a thin wedge triangle from the head's edge
to a nose tip left almost the entire wedge inside the head circle (only a tiny sliver
visible), which read as a beak. Replacing it with a **rectangle** (`rect(500, 270, 190,
140)`) that overlaps the head on its left edge and projects ~80-100px past the head's
silhouette on the right gave a real, blunt, visibly-rectangular muzzle block instead —
rule 4 in `SKILL.md` ("prefer blunt blocks over thin wedges").

## Draw order is the only fusion mechanism

Because every shape is the same flat fill with no stroke, the *only* thing that
determines whether a join looks seamless is which shape is drawn (and therefore
painted) last. In `build()`:

```python
return f'''<svg ...>
  <rect .../>      <!-- background -->
  {ear_body}
  {ear_tip}
  {cutlery}        <!-- drawn BEFORE jaw/head/snout so they can cover its top half -->
  {head}
  {snout}
  {jaw}             <!-- drawn AFTER cutlery: swallows the handles, leaves blade+tines -->
  {nose}
  {eye}             <!-- background-colored cutout, must be drawn last to "punch through" -->
  {wordmark}
</svg>'''
```

The crossed cutlery is the clearest example of this. `crossed_cutlery()` builds a
fork+knife pointing "up" from their anchor by default. Rather than trying to carefully
trim the shapes, the whole group is rotated 180° (`fork(154)`, `knife(206)` instead of
`fork(-26)`, `knife(26)`) so the **handles** point toward the anchor (which sits inside
the jaw block) and the **blade/tines** point away from it. Drawing the cutlery first and
the jaw block afterward then automatically swallows the handle ends — no trimming, no
clipping path, just paint order.

## The recurring bug: rotated groups reaching further than expected

The single most common failure across iterations was a stray spike or sliver appearing
near the snout/head junction. Cause: the cutlery group is wrapped in
`translate(cx,cy) scale(s)` plus an inner `rotate(deg)`. A point at local distance `L`
from the anchor (e.g. a blade tip at `L=150` in local units) ends up at actual distance
`L * scale` from the anchor after scaling — at `scale=1.6` that's `240px`, easily
reaching into a region of the silhouette (e.g. up near the snout) that nothing else
covers. The fix wasn't a clipping trick — it was: (a) keep `scale` modest (the final
version uses `1.45`), (b) **flip the rotation 180°** so the long blade/tine reach points
*away* from the rest of the silhouette into open space below, where it's *supposed* to
be visible, rather than *toward* the silhouette, where it pokes out as an artifact, and
(c) double check the farthest point's absolute coordinates against every shape that's
meant to cover it, not just the one shape you anchored to.

## Iteration discipline

This mark took roughly six render → inspect → adjust passes to land. Each pass fixed one
problem and sometimes revealed or reintroduced another (fixing the ear's invisibility
revealed the kite-shape problem; increasing cutlery scale for visibility reintroduced the
stray-spike bug). Budget for this — don't expect a geometric fusion mark to look right on
the first render. Crop+inspect after every change rather than batching multiple
speculative coordinate changes together, so it's clear which change caused which visual
effect.
