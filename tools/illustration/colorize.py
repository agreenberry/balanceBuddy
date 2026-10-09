"""Part-aware colouring of single-colour line art.

Petals, flower centres, leaves and stems each get their own colour:
  1. line mask = opaque pixels
  2. enclosed regions = connected components of non-line pixels not touching the border
  3. classify regions: centre (small + round), petal (in a dense cluster), leaf (elongated, sparse)
  4. group petals into flower heads (single-link clustering on centroids)
  5. fills: pale tint per head / sage for leaves; lines: deeper shade of the nearest part, green for stems
Usage: colorize.py in.png out.png [seed] [--debug]
"""
import sys, math, random
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage import measure

def hx(h): return np.array([int(h[i:i+2], 16) for i in (1, 3, 5)], dtype=np.float32)

# (fill, line) per flower head, from Amanda's palette
HEADS = [
    ("#B9C6E6", "#5A6FA8"),  # periwinkle (favourite, weighted x2 below)
    ("#F2C9C6", "#B06A68"),  # blush
    ("#DCAAAE", "#97575F"),  # dusty rose
    ("#CDB4C2", "#7A566A"),  # mauve
    ("#ECD9B2", "#A0844E"),  # wheat
    ("#D6E2E8", "#667F8F"),  # pale blue-grey
]
WEIGHTS = [3, 2, 2, 1, 1, 1]
THIN = 2
LEAF = ("#C3CBB4", "#2F413C")      # light olive fill, deep green line
LEAF_ALT = ("#B4C2B9", "#3C5248")  # a cooler green for variety
STEM_LINE = "#3E5248"
CENTRE = ("#DEC290", "#6E5A33")    # wheat centre
CENTRE_DARK = ("#7C5866", "#432934")  # aubergine centre

def run(inp, outp, seed=3, debug=False, dense_r=0.035, dense_n=4, head_eps=0.05):
    rng = random.Random(seed)
    im = Image.open(inp).convert("RGBA")
    a = np.asarray(im)[..., 3]
    H, W = a.shape
    diag = math.hypot(H, W)
    line = a > 90
    thin = ndi.binary_erosion(line, iterations=THIN)
    bg = ~line
    lab = measure.label(bg, connectivity=1)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])))
    props = [p for p in measure.regionprops(lab) if p.label not in border and p.area > 30]
    if not props:
        raise SystemExit("no enclosed regions")
    cents = np.array([p.centroid for p in props])
    areas = np.array([p.area for p in props], dtype=float)
    med = np.median(areas)
    # local density: number of region centroids within dense_r * diag
    d = np.sqrt(((cents[:, None, :] - cents[None, :, :]) ** 2).sum(-1))
    dens = (d < dense_r * diag).sum(1) - 1
    kind = {}
    for i, p in enumerate(props):
        ecc = p.eccentricity
        sol = p.solidity
        circ = 4 * math.pi * p.area / max(p.perimeter, 1) ** 2
        if circ > 0.62 and p.area < med * 0.9 and dens[i] >= 2:
            kind[i] = "centre"
        elif ecc > 0.84 and sol > 0.84:
            kind[i] = "leaf"            # long, solid, pointed
        else:
            kind[i] = "petal"           # wide, rounded or crescent
    # group petals into flowers.
    # 1) petals within reach of a centre join that centre's flower
    # 2) remaining petals link to each other only if they nearly touch AND are similar in size
    pet = [i for i in kind if kind[i] in ("petal", "centre")]
    parent = {i: i for i in pet}
    def f(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(x, y): parent[f(x)] = f(y)
    centres = [i for i in pet if kind[i] == "centre"]
    sz = np.sqrt(areas)
    assigned = set()
    for i in pet:
        if kind[i] != "petal" or not centres: continue
        j = min(centres, key=lambda c: d[i, c])
        if d[i, j] < 2.6 * sz[i] + 2.0 * sz[j]:
            union(i, j); assigned.add(i)
    free = [i for i in pet if kind[i] == "petal" and i not in assigned]
    for ii, i in enumerate(free):
        for j in free[ii + 1:]:
            ratio = max(sz[i], sz[j]) / max(min(sz[i], sz[j]), 1)
            if d[i, j] < 1.15 * (sz[i] + sz[j]) and ratio < 2.2:
                union(i, j)
    heads = {}
    for i in pet:
        heads.setdefault(f(i), []).append(i)
    # a "head" with a single small region and no centre is probably leaf detail
    pool = [k for k, w in zip(range(len(HEADS)), WEIGHTS) for _ in range(w)]
    head_col = {}
    last = None
    for h in sorted(heads, key=lambda h: cents[heads[h]].mean(0)[1]):
        c = rng.choice([x for x in pool if x != last]); last = c
        head_col[h] = c
    # paint
    fill = np.zeros((H, W, 4), np.float32)
    region_line = {}  # label -> line colour
    leaf_variant = {}
    for i, p in enumerate(props):
        k = kind[i]
        if k in ("petal", "centre"):
            hc = HEADS[head_col[f(i)]]
            if k == "centre":
                cf, cl = CENTRE if head_col[f(i)] not in (4,) else CENTRE_DARK
            else:
                cf, cl = hc
                # gentle per-petal variation so it reads hand-painted, not flat
                jitter = rng.uniform(-7, 6)
                cf = "#" + "".join(f"{int(max(0, min(255, v + jitter))):02X}" for v in hx(cf))
        else:
            cf, cl = LEAF if rng.random() < 0.7 else LEAF_ALT
        rr, cc = p.coords[:, 0], p.coords[:, 1]
        fill[rr, cc, :3] = hx(cf); fill[rr, cc, 3] = 235
        region_line[p.label] = hx(cl)
    # line colour: nearest enclosed region within reach, else stem green
    known = np.zeros_like(lab)
    for p in props:
        known[lab == p.label] = p.label
    dist, (iy, ix) = ndi.distance_transform_edt(known == 0, return_indices=True)
    reach = 7 * (W / 1800)
    out = fill.copy()
    ys, xs = np.nonzero(thin)
    near = known[iy[ys, xs], ix[ys, xs]]
    dd = dist[ys, xs]
    stem = hx(STEM_LINE)
    cols = np.array([region_line.get(n, stem) if dd_ <= reach else stem for n, dd_ in zip(near, dd)], np.float32)
    out[ys, xs, :3] = cols
    out[ys, xs, 3] = a[ys, xs]
    # removed edge pixels of the old line become fill-coloured gaps: let neighbouring fills grow into them
    gap = line & ~thin
    gy, gx = np.nonzero(gap)
    out[gy, gx, :3] = fill[iy[gy, gx], ix[gy, gx], :3]
    out[gy, gx, 3] = np.where(known[iy[gy, gx], ix[gy, gx]] > 0, 235, 0)
    img = Image.fromarray(out.clip(0, 255).astype(np.uint8), "RGBA")
    bbox = img.getbbox()
    img.crop(bbox).save(outp, optimize=True)
    if debug:
        print(f"regions={len(props)} heads={len(heads)} kinds=", {k: list(kind.values()).count(k) for k in set(kind.values())})

if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    run(args[0], args[1], int(args[2]) if len(args) > 2 else 3, debug="--debug" in sys.argv)
