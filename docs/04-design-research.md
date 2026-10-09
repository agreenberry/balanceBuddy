# BalanceBuddy — Design Research & Direction

> Status: **Sneak preview (v0)** · Oct 9, 2026
> Moodboard: [Paper · BalanceBuddy · Moodboard](https://app.paper.design/file/01M4FEC8M50M7Y2T7YZG7NKJDH)

## Working direction: "Herbarium"

The direction is a 1910s pressed-flower album. Every debt is a labelled specimen; paying one off presses it into the album for good. It ties the visual language to the mirth skill's motif library.

### Palette (each colour comes from the scene)
| Token | Hex | Source | Role |
|---|---|---|---|
| `--color-paper` | `#F5EFE2` | rag paper | ground |
| `--color-ink` | `#2B231D` | iron-gall ink | text, line work |
| `--color-ink-soft` | `#5C5048` | faded ink | secondary text |
| `--color-cornflower` | `#4F6E9C` | pressed cornflower | the single accent: actions, key figures |
| `--color-foxglove` | `#B4677A` | foxglove | promos, deadlines, gentle attention |
| `--color-moss` | `#6A7A4A` | pressed moss | stems, growth, progress |
| `--color-gilt` | `#B08D57` | gilt page edge | fine rules and frames only |

### Type
| Role | Face | Notes |
|---|---|---|
| Display | IM Fell English (+ SC for labels) | Letterpress revival |
| Body | Sorts Mill Goudy | Goudy Oldstyle, a 1915 design; 11/15 at default |
| Flourish | Pinyon Script | Hand-lettered notes; never for numbers |
| Figures | Cormorant Garamond SemiBold | Lining, tabular figures: crisp numbers inside ornate frames |

Default scale is dense on purpose (decision D-002): body 11px, labels 9px small caps.

## Field notes (sources to expand in the full research pass)

1. **Curves over corners.** People prefer curved objects to sharp-angled ones, and sharp contours are linked to heightened amygdala activity (Bar & Neta, 2006/2007). → Scallops, tendrils, rounded frames. [MGH](https://www.nmr.mgh.harvard.edu/publications/journal_articles/882) · [PDF](https://canlab.unl.edu/sites/unl.edu.cas.psychology.cognitive-and-affective-neuroscience/files/media/file/BarNetaNeuropsych2007.pdf)
2. **Nature's fractals soothe.** Mid-complexity natural fractals reduce physiological stress (Richard Taylor, Univ. of Oregon). → Botanical ornament is the calming part, not noise. [Smithsonian](https://www.smithsonianmag.com/innovation/fractal-patterns-nature-and-art-are-aesthetically-pleasing-and-stress-reducing-180962738/) · [UO](https://design.uoregon.edu/studying-fractals-nature-fractal-patterns-nature-relieve-stress-and-mental-fatigue)
3. **The handmade effect.** Handmade products are perceived as containing "love" (Fuchs, Schreier & van Osselaer, 2015). → A hand-drawn interface reads as care. [Univ. of Vienna](https://mib.univie.ac.at/en/research/recent-publications/publikationen-detailansicht/pure/b4c66f26-9ce8-4460-a816-7f46a6c4cd0c/show/publ/Pure)
4. **Nostalgia as comfort.** Nostalgia raises positive mood, optimism and social connectedness, and buffers against threat (Sedikides & Wildschut). → Period type and ledger forms borrow that warmth. [Southampton](https://www.southampton.ac.uk/~crsi/Sedikides%20and%20Wildschut%202016.pdf)
5. **Ornate frame, crisp figures** (our rule, to test). Lace and flourish live in the margins; every number sits in clean ink on plain paper.

## Still to do (full research pass)
- [ ] Colour and anxiety: what research says about warm vs. cool, saturation and calm
- [ ] Density done well: dense ornate references (seed catalogues, banknotes, ledgers, specimen sheets) and what keeps them legible
- [ ] Contrast check: every text/background pair against WCAG AA at the dense default sizes
- [ ] Two contrasting alternative directions to compare against Herbarium
- [ ] Illustration approach: hand-drawn SVG line work vs. commissioned art; a vocabulary of flourishes
- [ ] Reduced-motion versions of each "small ceremony"
