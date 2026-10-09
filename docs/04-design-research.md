# BalanceBuddy — Design Research & Direction

> Status: **Sneak preview (v0)** · Oct 9, 2026
> Moodboard: [Paper · BalanceBuddy · Moodboard](https://app.paper.design/file/01M4FEC8M50M7Y2T7YZG7NKJDH)

## Working direction: "Herbarium"

The direction is a 1910s pressed-flower album. Every debt is a labelled specimen; paying one off presses it into the album for good. It ties the visual language to the mirth skill's motif library.

### Palette (each colour comes from the scene)
| Token | Hex | Source | Role |
|---|---|---|---|
| `--color-paper` | `#F6F8FC` | mist | ground: cool-tinted white (**no beige grounds**, D-010) |
| *(card)* | `#FFFFFF` | archival white card | raised surfaces |
| `--color-ink` | `#1D2233` | blue-black ink (fresh iron-gall) | text, line work |
| `--color-ink-soft` | `#4B5368` | slate ink | secondary text |
| `--color-cornflower` | `#4F6E9C` | pressed cornflower | the single accent: actions, key figures |
| `--color-foxglove` | `#B4677A` | foxglove | promos, deadlines, gentle attention |
| `--color-moss` | `#6A7A4A` | pressed moss | stems, growth, progress |
| `--color-silver` | `#A3ACBF` | silverpoint | fine rules and frames only |

### Type
| Role | Face | Notes |
|---|---|---|
| Display | IM Fell English (+ SC for labels) | Letterpress revival |
| Body | Sorts Mill Goudy | Goudy Oldstyle, a 1915 design; 11/15 at default |
| Flourish | Pinyon Script | Hand-lettered notes; never for numbers |
| Figures | Cormorant Garamond SemiBold | Lining, tabular figures: crisp numbers inside ornate frames |

Default scale is dense on purpose (decision D-002): body 11px, labels 9px small caps.

**Revision, Oct 9:** the rag-paper beige ground was rejected. Beige may appear as a small accent, never as a background. The ground is now archival white. The warm brown ink and gold rules also read as sepia, so they moved to blue-black ink and silver rules. The palette now has no beige, tan or gold anywhere. Pure white still *read* beige next to the cool inks, a simultaneous-contrast effect, so the ground is tinted slightly blue (`#F6F8FC`) and cards are pure white. **Rule: neutral grounds lean cool, never warm.**

## Field notes (sources to expand in the full research pass)

1. **Curves over corners.** People prefer curved objects to sharp-angled ones, and sharp contours are linked to heightened amygdala activity (Bar & Neta, 2006/2007). → Scallops, tendrils, rounded frames. [MGH](https://www.nmr.mgh.harvard.edu/publications/journal_articles/882) · [PDF](https://canlab.unl.edu/sites/unl.edu.cas.psychology.cognitive-and-affective-neuroscience/files/media/file/BarNetaNeuropsych2007.pdf)
2. **Nature's fractals soothe.** Mid-complexity natural fractals reduce physiological stress (Richard Taylor, Univ. of Oregon). → Botanical ornament is the calming part, not noise. [Smithsonian](https://www.smithsonianmag.com/innovation/fractal-patterns-nature-and-art-are-aesthetically-pleasing-and-stress-reducing-180962738/) · [UO](https://design.uoregon.edu/studying-fractals-nature-fractal-patterns-nature-relieve-stress-and-mental-fatigue)
3. **The handmade effect.** Handmade products are perceived as containing "love" (Fuchs, Schreier & van Osselaer, 2015). → A hand-drawn interface reads as care. [Univ. of Vienna](https://mib.univie.ac.at/en/research/recent-publications/publikationen-detailansicht/pure/b4c66f26-9ce8-4460-a816-7f46a6c4cd0c/show/publ/Pure)
4. **Nostalgia as comfort.** Nostalgia raises positive mood, optimism and social connectedness, and buffers against threat (Sedikides & Wildschut). → Period type and ledger forms borrow that warmth. [Southampton](https://www.southampton.ac.uk/~crsi/Sedikides%20and%20Wildschut%202016.pdf)
5. **Ornate frame, crisp figures** (our rule, to test). Lace and flourish live in the margins; every number sits in clean ink on plain paper.

## Direction update (Oct 9, later): Ledger & Lace (board V)

Supersedes the Invitation Suite as the lead (see D-012). The board shows:
- **Amanda's palette** as paint chips: periwinkle is the favourite; wheat and teal are accents only.
- **Square ledger tiles** with lace-scroll corners: fine periwinkle curls, sage leaves, blush buds and dotted tracery, inspired by the curves of embroidered lace. Each tile has a dual-colour offset shadow (mist + blush, rose or periwinkle).
- **Multi-colour bars:** an account's balance split by rate, a paycheck split by destination, and every debt as a stacked bar.
- **Parts-coloured bouquets:** Amanda's line-art SVGs recoloured by `tools/illustration/colorize.py`. It finds enclosed shapes and sorts them into petals, centres and leaves by shape, groups petals around flower centres, and colours each part separately (green stems and leaves, palette petals, wheat or aubergine centres), with each line in the deeper shade of the part it borders.

**Known issues to fix next:**
- The flowers are still bolder than the tiles. Thin the lines further and scale them down to match the intricacy.
- Some blooms still mix colours across their petals (the poppy, the daisies), and some petals get read as leaves.
- Long term, a cleaner route is per-path SVG recolouring, so the output stays vector.

## Earlier: The Invitation Suite (board IV, superseded)

Wedding stationery is now the lead reference (D-011). The Paper moodboard has five boards:
- **v0 Herbarium:** the original
- **I Sweet-Pea Organza**, **II Peony Veil**, **III Meadow Ribbon:** organza explorations
- **IV The Invitation Suite:** the current lead

| Role | Hex |
|---|---|
| Pastel indigo / deep indigo | `#9AA3E0` / `#5560A3` |
| Pink / rose | `#F2B6C6` / `#B5607D` |
| Butter yellow | `#F5DC8C` |
| Pale salmon | `#F6C2AE` |
| Faded dark green | `#55705A` |
| Ink | `#2B2F4A` |
| Paper / table | `#FFFFFF` / `#F4F4F9` |

**Illustration technique:** the engravings are *hand-tinted* in code. The linework is dilated and closed into a colour wash, the bloom colour fades to faded green over the stems and leaves, and the ink line sits on top. This is how 19th-century botanical prints were coloured, and it lets one licensed set of engravings carry the whole palette. Output: `~/Downloads/flowers/balancebuddy-tinted/suite/`.

**Lace kit:** scalloped card edges (12px scallops), a round doily with pinhole rings, a wax-seal monogram, and a sage ribbon.

**Type, invitation style:** Cormorant Garamond caps with letter-spacing of about 0.28–0.36em for names and headings, Pinyon Script for the joining words ("is to be", "for the paycheck of the fifteenth"), and Cormorant SemiBold for figures.

## Illustration library (Amanda's collection)

About 100 pieces in `~/Downloads/flowers` (not in the repo). Tinted copies for the moodboard are in `~/Downloads/flowers/balancebuddy-tinted/`; the originals are untouched.

| Set | Style | Fit |
|---|---|---|
| Sepia engravings (`1–21.png`: snowdrop, lily of the valley, pansy, primrose, daffodil, hyacinth…) | Fine 19th-century engraving | **Best fit.** True herbarium specimens. Tint to ink, cornflower or moss. One per account card? |
| Peony line art (8) | Delicate single-weight line | Good for large, quiet moments (paid-off "bloom") |
| Wildflower outline rows (6) | Light line, rows of stems | Borders, dividers, empty states |
| Autumn sprays (4) | Very fine, airy | Header ornaments, seasonal variation (G5) |
| Floral alphabet (A–Z, 0–9, &) | Serif initials wrapped in florals | Drop caps, monograms, maybe the logo "B" |
| Flower & Leaf set (19) | Bolder, cartoonish line | Weakest fit: too heavy for the delicate direction |

**Licence:** the packs are "POD License Included" (print on demand). That usually covers physical products, not use inside a web app, where SVGs can be downloaded from the page. Check each pack's licence text or ask the seller before shipping them in the app. Moodboard use is fine.

## Still to do (full research pass)
- [ ] Colour and anxiety: what research says about warm vs. cool, saturation and calm
- [ ] Density done well: dense ornate references (seed catalogues, banknotes, ledgers, specimen sheets) and what keeps them legible
- [ ] Contrast check: every text/background pair against WCAG AA at the dense default sizes
- [ ] Two contrasting alternative directions to compare against Herbarium
- [ ] Illustration approach: hand-drawn SVG line work vs. commissioned art; a vocabulary of flourishes
- [ ] Reduced-motion versions of each "small ceremony" (animations are on by default, with a setting to turn them off)
- [ ] Dark-mode art direction ("night garden"?), built on the same tokens
- [ ] Confirm each illustration pack's licence covers in-app/web use (they're POD licences)
