# Sources and what each one taught

altdesign merges four sources. Each rule in SKILL.md traces to one of them. Where they disagree, the resolution is written here.

## 1. AREZ marketing site v33 (tryarez.com), by Majid Yassine, Nov 2026

A product site for structural engineering software that a non-designer client called "insane". It kept the copy of an earlier version almost word for word, so everything that changed was design. Measured:

- **Proof**: 9 raster images and 2 videos across 14 sections; real app screenshots cropped to the part that matters, five real drawing sheets that open full size, a downloadable 15 sheet PDF, a 15.5 s rendered film of the product's one job (model, check, fail, fix, sheet) as the hero, with 5 clickable chapters.
- **One metaphor everywhere**: each section carries a drawing sheet number (S-001 Product, S-801 FAQ); a faint drafting grid behind the hero; the 404 is "This sheet is not in the set".
- **Demos you operate**: a step list pinned while the screenshot changes, a slider that updates a schedule row, a chat mock with a real change and Apply / Dismiss.
- **Real numbers in mockups**: beam B-204 fails at 1.18, passes at 0.71 after the resize.
- **Type**: Manrope 600 for display at line-height 1.0 and tracking -0.025em; Geist Mono for sheet numbers and data; nothing else.
- **Bands**: dark bands for the product, light "paper" bands for what it produces; under `.paper` every token flips so components keep their markup.
- **Depth**: floating blurred pill nav, product windows with title bars and 0 30px 80px shadows, 1px hairlines at 10 to 28% alpha, film grain cut to 6% in a "calm pass".
- **Motion**: GSAP + Lenis, self hosted; word reveal on headings, progress bar, odometer price, sheets that "plot" in, pinned steps, magnetic primary buttons, 3D tilt, cursor spotlight; all off under reduced motion; everything visible without JS.
- **Process**: 33 versions, each pass named with a goal and a changelog; final pass tested at 390/768/1440 px, W3C validator, axe (0 violations), Lighthouse mobile 96/100/100/100, LCP 2.0 s, 527 KB first load.
- It was built with Claude and the elaya `landing-page-design` skill (named in its CSS), plus patterns from React Bits (Split Text, Spotlight Card) and 21st.dev (magnetic button).

## 2. elayadesign/ai-design-skills and elayadesign/redesign-skill (MIT, © 2026 Elaya)

https://github.com/elayadesign/ai-design-skills (`landing-page-design`, `figma-designer`) and https://github.com/elayadesign/redesign-skill (`redesign-existing-projects`). Adapted with credit. What we kept:

- Intake in one batch; one offer, one audience, one primary action; layout types A to D; page structure; build order section by section.
- The visual system: one family, named text styles on the Tailwind scale, spacing scale 2 to 96 px, nested radius formula, one accent under 80% saturation, flat surfaces, hero heading gradient on text only, 680 px measure for hero copy, floating blurred nav, full height mobile menu with 60 ms staggered links, one easing curve cubic-bezier(.22,1,.36,1), scroll reveals 32 px over 600 to 800 ms via IntersectionObserver, the mandatory tagline reveal section.
- Content realism and banned filler; full state set; ship requirements; the redesign audit and its fix order; two layer colour tokens from the Figma skill.

Elaya's skills credit taste-skill by Leon Lin (MIT) for the audit structure, content realism, motion and nav ideas. taste-skill also gave us one idea directly: a page gets one or two "moments" (a section a visitor remembers), never three.

## 3. elaya.design portfolio (19 works shown on the site, Nov 2026)

See `portfolio.md` for the per work study and counted patterns.

## 4. Diego Aranda, "website color palettes that look expensive" (Instagram reel, 7 Nov 2026)

https://www.instagram.com/reel/Dfc-Q-0yy0W/ . Rule: **two colours that get along, one that does not, and that one only goes on the button.** Three palettes, each shown on a full hero:

| Pair that gets along | The pop | Reads as | Example hero |
|---|---|---|---|
| Cream #F3EEE3 + ink black #111111 | burnt orange #D9541E | startup | "The ops teammate that *never sleeps.*" |
| Navy #0F1B3D + white #FFFFFF | hot pink (about #FF3D8B) | consumer app ("corporate" until the pink) | "Split the bill before the *check lands.*" |
| Charcoal #1E1E1C + sand #D8CBB3 | electric blue (about #2F6BFF) | Series A infrastructure | "The grid, rebuilt for the *AI era.*" |

What the three example heroes also show:
- Photographs are black and white or duotone so the pop colour owns all the colour on the page.
- The pop appears on the primary button and at most one or two small marks (an underline stroke under the key words, a block offset behind the photo, a status badge, a live chart line). Never on headings or backgrounds.
- The headline is a heavy grotesque with tight tracking, and the emotional words switch to a serif italic ("*never sleeps.*").
- Product UI floats over the photo as cards with real looking data (11.5 hrs saved, 2:14 AM timestamps, $186.40 split three ways at $46.60, 2,139 MW live load).
- An announcement bar on top, a proof line beside the CTA (avatars and 4,000+ founders, 4.9 from 80K reviews), a logo row of mixed wordmark styles, a stats row (4.1 GW, 38%, 11).

## Conflicts and how altdesign resolves them

| Topic | elaya | Majid / reel | altdesign |
|---|---|---|---|
| Italic | never | reel: serif italic for 2 to 3 words of the hero | Default none. One optional flourish per page: the hero's key phrase in a serif italic, 3 words or fewer. Nowhere else. |
| Second typeface | never unless asked | reel: serif accent; Majid: mono for data | One sans family; a mono for data and labels; a serif only for the hero flourish above. |
| Background gradients | never | Majid: gradient masks and image overlays | Surfaces flat. Gradients allowed only on hero text, on overlays that make text readable on a photo or film, and as masks that fade a pattern. |
| Dark section in a light page | an accident | Majid: deliberate alternation | Alternate bands only as a system (token flip, at least 3 bands, each band means one thing). Never one stray band. |
| One side borders | never on cards | Majid: dividers between trio items | Never on cards. Row and column dividers are fine. |
| Spacing values | only the 13 tokens | Majid: 14 px, 18 px, 22 px in places | Tokens for layout (padding, gaps, margins). Optical one off values inside small components are allowed and noted. |
| Accent | one, under 80% saturation | reel: a pop that clashes on purpose | One accent. It may be loud (the reel's pop) if it sits only on actions and one or two marks, and the other two colours are calm. |
| Motion | reveals and the tagline | Majid: a full motion layer | Reveals and the tagline are the floor. Add one or two moments with a job (taste-skill rule), then a calm pass. |
