---
name: altdesign
description: Designs and builds landing pages, product sites and marketing pages that look made by a senior designer, not by AI. Covers the brief, the proof assets, a hero that acts out the headline, a two plus one colour palette, one type family, spacing and motion systems, one or two memorable moments, a checker script and browser verification. Use when building, restyling, redesigning or reviewing any landing page, homepage, product page, marketing site, waitlist or launch page, or when someone says a page looks generic, cheap, unprofessional or AI made. Not for app dashboards built inside a design tool, logos, slide decks or print.
license: MIT
metadata:
  version: 1.0.0
  sources: AREZ site v33 by Majid Yassine; elayadesign/ai-design-skills and redesign-skill (MIT); the elaya.design portfolio; Diego Aranda's palette reel. See references/sources.md.
---

# altdesign

A page earns trust by **showing** the product, not describing it. Good copy with no proof reads as cheap; the same copy beside real screenshots, a film of the product working and a demo you can touch reads as expensive. Rules for type, space and colour are the floor. The bar is the proof, the idea and one or two moments people remember.

## Critical rules

1. **Proof beside every claim.** Real screenshots, real output, a film or recording. A page with no raster image or video of the product fails.
2. **The hero visual acts out the headline.** Say in five words how the picture shows the promise. A product film, the product UI over a scene that is a pun on the headline, or real output. Never abstract blobs, orbs or mesh gradients.
3. **One idea through the whole page.** A domain metaphor that tags sections, shapes the background and names the 404.
4. **Two colours that get along, one that pops**, and the pop goes only on the primary button plus at most two small marks.
5. **One sans family, one mono for data.** Display at weight 600, line-height 1.0, tight tracking. At most one serif italic flourish of three words in the hero.
6. **One primary action per screen.** The second action is a text link.
7. **Real specifics in every mockup**: odd numbers, units, timestamps, names that fit the audience. Never invented facts on a real product's page; mark gaps as `{{placeholder}}` and hide the block.
8. **Motion shows the product working**, on one curve, transform and opacity only, off under reduced motion, content visible without JS.
9. **Many named passes**, each with one goal, then a calm pass that removes what does not explain or reward.
10. **No em dashes, no filler words** (revolutionize, seamless, effortless, unleash, world class), sentence case.

## Workflow

### 1. Brief, in one batch

Ask only for what is missing, in one message: the one action (trial, demo, buy, waitlist, download); the offer exactly; the audience and what they know on arrival; the top three objections; traffic source; proof that exists (logos, numbers, quotes, screenshots, video, sample files); risk reversal (trial, refund, cancel anytime); brand colours and fonts that must stay. If something cannot be answered, assume, say it in one line, continue.

Check: you can write "the first thing they see is ___" and "they leave believing ___".

### 2. Proof inventory, before any layout

List every asset the page needs: hero film or image, 3 to 6 product screenshots cropped to the part that matters (2x), real output (documents, reports, sheets), a sample file to download, the maker's or team's photo, logos and numbers you are allowed to show. Get them now:
- From a running product: screenshots and a 10 to 20 s screen recording of its one job (Playwright or the OS recorder), cropped and encoded to WebP and H.264 MP4 with a poster.
- No product to capture: a rendered scene that states the metaphor (see `references/portfolio.md`, rules 1 to 3), with the UI composed over it from real looking data.
- A film of the product's job that a screen recording cannot show (a building, a process, a physical result): render it in Blender from code, following `references/blender.md` and `assets/blender/film.py`.
- A product that exists only as a design (pre launch, a demo): build its real interface in HTML with real looking data, then capture it as screenshots and a recording like a running product. That counts as proof because it is the interface people will get. A drawn stand in is something else: a decorative diagram, icon art or abstract shapes presented as if they were the product. Never ship one.
- Anything you cannot get: a marked placeholder and a line in the hand off list.

Check: every section in the outline has a named asset beside its claim.

### 3. Direction

Write three directions that differ in kind (not in shade), each in one line: the metaphor, the hero visual, the palette (two plus one, with hex), the art medium if any. Pick one and say why the other two lost. Then fix:
- **Metaphor**: how sections are tagged (sheet numbers, chapter marks, timestamps), the background texture, the 404 line.
- **Palette**: ground, ink, pop. Photographs desaturated so the pop owns colour. Read `references/system.md`, Colour.
- **Type**: the family, the mono, and whether the hero gets the serif flourish.
- **Moments**: one on a short page, two on a long page (8 sections or more), never three. Pick from `references/system.md`, Motion. The hero film is the hero, not a moment; moments live below it.

Check: someone could tell this page apart from a competitor's with the logo covered.

### 4. System

Copy `assets/tokens.css` and set only its first block (ground, raised, pop, three text steps). Check contrast on the real ground: 4.5:1 for text, 3:1 for large text and UI edges. Use the named text styles and spacing tokens from `references/system.md`; never a loose size or an ad hoc gap.

### 5. Build, section by section

Order: hero, proof row, product (how it works), the tagline section, output or gallery, scope or comparison, the second moment, about the maker (only when a named maker or team is part of the trust; otherwise skip it), pricing with risk reversal, FAQ (six to twelve real questions), closing CTA, footer. Drop what the product does not need; keep the order of argument. Build one section, look at it at 390 and 1440 px, then the next. Never rebuild the whole page per change.

Hero recipe: announcement or eyebrow only if it carries news; heading of two lines, eight words or fewer, 48 to 64 px, broken where the thought breaks, max 680 px; one line of how and for whom; one filled button with a verb and what they get, plus a text link; one quiet proof line (rating, count, logos in one colour); the visual from step 2, with product UI as floating cards over a scene or a window that bleeds off the edge.

Tagline section: one large statement of the core promise (two lines or more), its words brightening one by one from 30% as it scrolls into view (`data-tagline` in `assets/motion.js`).

### 6. Motion pass, then calm pass

Add the floor (reveals, tagline, button feedback) with `assets/motion.js`. Add the chosen moments; use GSAP with ScrollTrigger and Lenis only for pinned or scrubbed moments, self hosted. Each animation must name the product fact it shows; if it cannot, cut it. Then the calm pass: halve loops, cut grain and glow, remove one effect.

### 7. Verify

1. `python3 scripts/check.py path/to/index.html`, and `python3 scripts/check.py --secondary 404.html privacy.html` for pages that are not landing pages. Zero errors. Read every warning and fix it or write why it stays.
2. A real browser at 390, 768 and 1440 px: no horizontal scroll, the primary action visible in the first screen on a phone, nothing clipped, no orphans. Look at every screenshot yourself.
3. axe: zero violations, also with reduced motion.
4. Lighthouse mobile: performance 90 or more, accessibility, best practices and SEO 100. Video loads only in view, phones get a smaller film, fonts and libraries self hosted (Google Fonts links are fine for a prototype, never for production).
5. Every link and form works; forms validate; the 404 renders.

### 8. Critique and passes

Compare the page with the references in `references/sources.md` (AREZ v33, the elaya.design works) side by side at the same width. Name what is weaker, fix it as a named pass ("proof pass", "motion pass v2", "calm pass"), and keep a changelog of passes in the hand off notes. Stop when a fresh reviewer cannot point to anything that reads as generic, not when a score is reached.

## Redesigning an existing page

Run `references/audit.md`: diagnose, report, let the owner veto, then fix in its order (proof first, then type, colour, states, layout, motion, components, copy, ship list). Work inside the existing stack.

## References

- `references/system.md`: every value (colour, type styles, spacing, radius, surfaces, nav, motion, imagery, states, content, ship list). Read before step 4.
- `references/portfolio.md`: 19 works from elaya.design, counted patterns, 12 rules for heroes and imagery. Read in step 3.
- `references/sources.md`: what each source taught, the AREZ case, the palette reel, and how conflicts between sources were resolved.
- `references/audit.md`: the redesign audit and fix order.
- `references/blender.md`: films, scene stills and backdrops rendered in Blender from code; timings and commands. Read in step 2 when the hero needs a film.
- `assets/tokens.css`: starter tokens with the dark and light band flip, text styles, buttons, nav, window, grain.
- `assets/motion.js`: reveals, tagline words, number roll, scroll scrubbed video. No dependencies.
- `assets/blender/film.py` and `beats.json`: a scripted headless Blender film with beats that also feed the page's chapter buttons.
- `scripts/check.py`: the mechanical checker (standard library Python).

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Passes every check, still looks generic | no proof, no idea | steps 2 and 3; the checker is a floor |
| `no product proof` error | drawn or stock visuals only | real screenshots or a recording; a scene image with real UI over it |
| Looks busy | more than two moments, accent everywhere | calm pass; pop only on the button and two marks |
| Hero headline wraps to four lines on a phone | heading too long | eight words or fewer, clamp the size, balance |
| Lighthouse under 90 | video or analytics on load | load video in view, smaller phone file, analytics on first interaction |
| No horizontal scroll reported, but text is cut off on a phone | `overflow-x:clip` (used for a bleeding hero) hides overflow from `scrollWidth` | check element edges against the viewport; give grid and flex children `min-width:0` |
| A bleeding window hides the point of the screenshot | the bleed crops the newest or key part (latest data, RTL headings on the right) | crop the source so the key part is inside the frame; bleed only empty or old parts |
| The hero film looks empty in screenshots and on slow phones | the poster or first frame is the start of the run | the poster is the payoff frame; captions in HTML |
| A full page screenshot shows a big empty band | a pinned or scroll scrubbed section captured without scrolling | scroll through before capturing, or judge pinned sections in viewport shots |
| Inactive steps or tabs fail contrast | dimmed with opacity | dim with the `--fg-3` colour step, never opacity, and check 4.5:1 |
