# The visual system

Every value on the page resolves through this file and `assets/tokens.css`. Adapted from elaya's `landing-page-design` (MIT) with the changes listed in `sources.md`.

## Colour: two that get along, one that pops

- Pick **a ground and an ink that get along** (cream #F3EEE3 + ink #111111; navy #0F1B3D + white; charcoal #1E1E1C + sand #D8CBB3; deep cedar #0E2219 + ivory #F4EFE6). Then **one pop** (burnt orange #D9541E; hot pink; electric blue #2F6BFF; champagne #C9A96E).
- The pop goes on the primary button, the active state, and at most two small marks on the page (an underline under the hero's key words, a block offset behind the hero image, a live chart line, a status badge). Never on headings, never on a background band, never on body links.
- Neutrals come from one family: all warm (cream, sand, cedar) or all cool (navy, slate). Text has three steps only (`--fg`, `--fg-2`, `--fg-3`).
- Photographs are black and white, duotone or desaturated, so the pop owns the colour. Product screenshots keep their real colours.
- Dark grounds: near black, charcoal or a deep brand hue. Avoid pure `#000` behind long text. Avoid the purple and indigo "AI gradient" look entirely.
- Tokens in two layers: raw palette values in one place, semantic roles (`--base`, `--raised`, `--fg`, `--accent`, `--line`) everywhere else. Name by role, never by hue.
- Contrast: body text 4.5:1, large text (24 px, or 18.7 px bold) and UI edges 3:1, checked on the real ground. On a gradient heading, check the light end. Never colour alone for state.
- Light and dark bands: allowed as a system. Put `class="light"` on a band and every token flips (see tokens.css). Each tone means one thing (dark for the product, light for what it produces). At least three bands; never one stray band.

## Type

- **One sans family** for everything: Manrope or Geist (Satoshi, General Sans, Switzer if licensed). Never Inter, Roboto, Arial, Helvetica, Open Sans as the brand face.
- **One mono** (Geist Mono, JetBrains Mono) only for data, code, numbers in tables, labels and sheet tags.
- **One optional flourish**: the hero's key phrase (3 words or fewer) in a serif italic (Instrument Serif, Newsreader, EB Garamond italic). Nowhere else on the page. Skip it for sober audiences.
- Weights 400, 500, 600 (700 at most). Never 800 or 900. No italic outside the flourish.
- Display: weight 600, line-height 1.0, tracking -0.025em at 60 px, -0.02em at 48 px. Labels in caps: mono 12 px, tracking +0.08em.
- `text-wrap: balance` on headings, `pretty` on body. No orphan on the last line of a heading.
- Hero heading and subheading max width 680 px; break the heading where the thought breaks.
- Body measure 45 to 75 characters. `font-variant-numeric: tabular-nums` on prices and data.

Named text styles (define once as classes, use the names):

| Style | Size / line height | Weight | Use |
|---|---|---|---|
| heading-1 | 60/60 (clamp 40 to 60) | 600 | hero only |
| heading-2 | 48/48 (clamp 30 to 48) | 600 | section headings |
| heading-3 | 36/40 | 600 | tagline section, big card titles |
| heading-4 | 30/36 | 600 | sub sections |
| title-1 | 20/28 | 500 | card titles |
| title-3 | 16/24 | 500 | list titles, nav |
| lede | 18/28 | 400 | subheadings |
| body-3 | 16/24 | 400 | running text |
| body-6 | 14/20 | 400 | secondary text |
| caption-5 | 12/16 | 400 | fine print |
| label | 12/16 mono caps | 500 | tags, table heads |
| button-md / button-sm | 16/24, 14/20 | 600 | buttons |

Sizes come from 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96. Snap anything else to the step below.

## Space and grid

- Spacing tokens: 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96 px; section padding 120 px desktop, 64 px phone. Layout values (padding, gaps, margins) come only from these. A one off optical value inside a small component is allowed if noted in a comment.
- Container 1200 px (1280 max) with 24 px gutters, 16 px under 600 px.
- Two column splits at 5/7 or 4/8, not 6/6. Avoid three equal cards as the default feature row: use a zig zag, a 4/8 split with a list beside a frame, an asymmetric bento, or a pinned step list.
- Inside a group, gaps are at most half the gaps between groups.
- Cards side by side align their titles, prices, lists and buttons on the same lines; buttons pin to the bottom.

## Radius

One rule: buttons and inputs 6 px, cards and windows 8 to 12 px, big media 12 to 16 px, pills 999 px. Nested: inner radius = outer radius minus the gap, when the gap is under 32 px and the result is over 2.

## Surfaces and depth

- Flat grounds. Depth comes from light: large soft shadows tinted toward the ground (0 30px 80px at 35 to 50% on dark), 1 px hairlines at 10 to 28% alpha, a grain overlay at 4 to 8%, a vignette on hero media.
- Allowed gradients: hero heading text; overlays that make text readable on a photo or film; masks that fade a grid or pattern. Nothing else.
- Cards exist only where elevation means something. Otherwise group with space. Never a border on one side of a card.
- Product screenshots sit in a "window" (title bar with the product and view name, hairline border, big shadow), cropped to the part that matters, at 2x.

## Navigation

- Floats 12 px off the top, centred, sized to its content, translucent ground with 16 px blur, hairline border, soft shadow.
- Logo, 4 to 6 links, one small primary button. The current page or section is marked.
- Under 560 px: a menu button whose two lines turn into an X on the base curve; a full height panel with 24 px blur; links rise 24 px and fade in, 60 ms apart, whole sequence under 400 ms.

## Motion

- One curve: `cubic-bezier(.22,1,.36,1)`. 500 ms for movement, 300 ms for colour and opacity, never under 200 ms. No `ease`, `linear` or `ease-in-out` on UI.
- Animate only `transform` and `opacity`.
- Floor (every page): sections rise 32 px and fade in once over 600 to 800 ms (IntersectionObserver); the tagline section's words brighten one by one from 30%; buttons lift 1 px on hover and press to 0.98.
- Moments (one on a short page, two on a long one, never three), each in its own section with a job: a scroll scrubbed product film, a pinned step list with a changing frame, a counter or odometer on a real number, sheets or screenshots that "develop" in, an interactive slider or calculator, a chat or terminal that types a real exchange.
- Heavier libraries (GSAP + ScrollTrigger, Lenis) only for pinned or scrubbed moments, self hosted, loaded deferred.
- Under `prefers-reduced-motion`: no movement, final states shown. Without JavaScript: all content visible.
- Then a **calm pass**: halve anything that loops, cut grain and glow, remove any effect that does not explain or reward.

## Imagery

- Order of preference: real product UI and output; a film or recording of the product doing its job; real photographs of the customer's world (desaturated); a rendered or illustrated scene that carries the product's metaphor; never stock "team at laptop" photos.
- A scene image (a landscape, an object, a creature) works when it states the metaphor of the promise in one look and the product UI sits over it as cards.
- Every hero visual answers: what does the visitor see happening?
- Video: muted, playsinline, poster image, loads when in view, a smaller file for phones. Images: WebP or AVIF, `srcset` with 1x and 2x, width and height set.
- Icons from one set with one stroke weight (Phosphor, Solar, Iconamoon), inline SVG. No rocket for launch, no shield for security.

## Components and states

Every interactive element ships with hover, active, focus (2 px ring at 3:1), disabled; inputs add error and filled; data views add loading (skeleton shaped like the layout), empty (a composed first step) and error (inline, says what failed and what to do). No link points at `#`.

## Content

- Real copy in the product's voice. Specific outcomes with numbers. Sentence case for headings and buttons.
- CTA = verb + what they get ("Start 14 day trial", "Get the sample set"). Never "Learn more", "Submit".
- Never invent facts on a real product's page: prices, stats, customers, quotes and logos come from the client; mark gaps as `{{testimonial}}` and keep the block hidden until filled.
- In demos and mockups use believable specifics: odd final digits, real units, real timestamps, names that fit the audience.
- Banned: revolutionize, supercharge, cutting edge, effortless, seamless, unleash, elevate, transform your workflow, next level, harness the power, world class, game changer. No em dashes, no exclamation marks in system messages.

## Ship list

Branded favicon; `<title>`, meta description, canonical, Open Graph image 1200x630 and Twitter tags; JSON-LD (Organization, the product type, FAQPage from the visible FAQ); privacy and terms in the footer; branded 404 with a way back; skip link; `lang`; semantic landmarks; alt text; client side form validation; cookie consent where the law needs it; `noindex` on ad only pages; sitemap and robots.
