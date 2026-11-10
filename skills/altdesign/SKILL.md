---
name: altdesign
description: Designs and builds landing pages, product sites and marketing pages that look made by a senior designer, not by AI. Covers the brief, a full bleed moving scene that acts out the headline (image model, then image to video), the proof assets, a two plus one colour palette, one type family, spacing and motion systems, one or two memorable moments, a checker script and browser verification. Use when building, restyling, redesigning or reviewing any landing page, homepage, product page, marketing site, waitlist or launch page, or when someone says a page looks generic, cheap, unprofessional or AI made. Not for app dashboards built inside a design tool, logos, slide decks or print.
license: MIT
metadata:
  version: 1.2.0
  sources: AREZ site v33 by Majid Yassine; elayadesign/ai-design-skills and redesign-skill (MIT); the elaya.design portfolio; 17 of Elaya's X screen recordings; Diego Aranda's palette reel. See references/sources.md.
---

# altdesign

A page is remembered for **one moving picture** and trusted for **its proof**. The first screen is a single full bleed scene, in a named craft style, that acts out the headline as a pun and moves in one small way (a beam sweeps, clouds pass, a crab walks in). Below the fold the product shows itself: real screenshots, real output, cards that work. Rules for type, space and colour are the floor. The bar is the scene, the proof, the idea and one or two moments people remember.

A page with perfect type and real screenshots and no scene still reads as a developer's page. That is the most common failure: see `references/scenes.md`.

## First: experience or functional

Decide before anything else, and say which in one line.
- **Experience** (a brand, a studio, a shop that sells a feeling): the whole page is one world or one device you use, not a landing page. No standard header, hero copy column, card grid or text manual around it; the experience is the navigation, the proof and the call to action. A shop you walk through and pick from; a handheld whose screen is the site. Copy inside it is short and in character, never meta ("both real", "this site is a handheld"). Build devices and worlds in code so every part can be pressed. Run the scene and proof rules inside the world. Check it with `scripts/check.py --experience`: proof is the real data the world shows (real numbers, real links), and a live region reads each screen.
- **Functional** (a tool, a database, a reference people use daily): plain, fast and clear. Search first, readable type, no story. The rest of this skill applies only lightly: type, spacing, states, the ship list.

A clean, correct landing page for an experience brand reads as boring. That is a failure even when every check passes.

## Critical rules

1. **The first screen is one scene.** A full bleed picture, made with an image model in a style you can name in two words, that is a pun on the headline. Write "the picture shows ___ doing ___" before any layout. Never a screenshot collage, abstract blobs, orbs or mesh gradients.
2. **The scene moves.** A 6 to 10 s seamless loop from an image to video model: static camera, one element moving, and that element is the pun. The UI is small over it and at least one layer crosses the other (art in front of the UI, UI peeking out of the art, or the scene fixed while content scrolls over it).
3. **Proof beside every claim, below the fold.** Real screenshots, real output, cards that show the product working. A page with no raster image or video of the product fails. In the hero, the product appears small (a card, a prompt box, numbers on the scene, a window peeking from the bottom edge), never as the main picture.
4. **One idea through the whole page.** The scene's style and character carry to the footer and the 404; a domain metaphor tags sections.
5. **Two colours that get along, one that pops**, pulled from the scene; the pop goes only on the primary button plus at most two small marks.
6. **One sans family, one mono for data.** Display at weight 600, line-height 1.0, tight tracking. At most one serif italic flourish of three words in the hero.
7. **One primary action per screen.** The second action is a text link.
8. **Real specifics in every mockup**: odd numbers, units, timestamps, names that fit the audience. Never invented facts on a real product's page; mark gaps as `{{placeholder}}` and hide the block.
9. **Scene motion shows the pun, UI motion shows the product working**, on one curve, transform and opacity only, off under reduced motion, content visible without JS.
10. **Many named passes**, each with one goal, then a calm pass that removes what does not explain or reward.
11. **No em dashes, no filler words** (revolutionize, seamless, effortless, unleash, world class), sentence case.

## Workflow

### 1. Brief, in one batch

Ask only for what is missing, in one message: the one action (trial, demo, buy, waitlist, download); the offer exactly; the audience and what they know on arrival; the top three objections; traffic source; proof that exists (logos, numbers, quotes, screenshots, video, sample files); risk reversal (trial, refund, cancel anytime); brand colours and fonts that must stay. If something cannot be answered, assume, say it in one line, continue.

Check: you can write "the first thing they see is ___" and "they leave believing ___".

### 2. The scene, before any layout

Read `references/scenes.md`. Write the headline (8 words or fewer) and the pun: "the picture shows [subject] [doing its action]". Name the style in two words and the one thing that moves. Then make it:
1. Still: an image model, 16:9 at 2560 px or more, a quiet zone where the copy goes, no text. Make 4 to 8, pick by the pun. A second crop for phones.
2. Loop: an image to video model, motion only in the prompt ("static camera, the beam sweeps slowly, everything else still, seamless loop"), first frame equal to last. Watch it 5 times: no morphing, no new objects, no jump at the seam.
3. Encode: MP4 and WebM, 1 to 3 MB at 1920 wide, a phone file under 1 MB, a poster.
No image model available: say so, and build the hero from a real photograph in the same rules (one subject, a style treatment, one moving layer), never from screenshots.

Check: a stranger who reads only the headline and sees the picture gets the joke in one second.

### 3. Proof inventory

List every asset the page needs: hero film or image, 3 to 6 product screenshots cropped to the part that matters (2x), real output (documents, reports, sheets), a sample file to download, the maker's or team's photo, logos and numbers you are allowed to show. Get them now:
- From a running product: screenshots and a 10 to 20 s screen recording of its one job (Playwright or the OS recorder), cropped and encoded to WebP and H.264 MP4 with a poster.
- Proof goes in the sections below the hero: bento cards where each card is a small working UI, a pinned step list, real output. The hero only gets a small product layer.
- A film of the product's job that a screen recording cannot show (a building, a process, a physical result): render it in Blender from code, following `references/blender.md` and `assets/blender/film.py`.
- A product that exists only as a design (pre launch, a demo): build its real interface in HTML with real looking data, then capture it as screenshots and a recording like a running product. That counts as proof because it is the interface people will get. A drawn stand in is something else: a decorative diagram, icon art or abstract shapes presented as if they were the product. Never ship one.
- Anything you cannot get: a marked placeholder and a line in the hand off list.

Check: every section in the outline has a named asset beside its claim.

### 4. Direction

Write three directions that differ in kind (not in shade), each in one line: the headline and its pun, the scene and its style, what moves, the palette (two plus one, with hex). Make a rough still for each and show those before building anything. Pick one and say why the other two lost. Then fix:
- **Metaphor**: how sections are tagged (sheet numbers, chapter marks, timestamps), the background texture, the 404 line.
- **Palette**: ground, ink, pop. Photographs desaturated so the pop owns colour. Read `references/system.md`, Colour.
- **Type**: the family, the mono, and whether the hero gets the serif flourish.
- **Moments**: one on a short page, two on a long page (8 sections or more), never three. Pick from `references/system.md`, Motion. The hero film is the hero, not a moment; moments live below it.

Check: someone could tell this page apart from a competitor's with the logo covered.

### 5. System

Copy `assets/tokens.css` and set only its first block (ground, raised, pop, three text steps). Check contrast on the real ground: 4.5:1 for text, 3:1 for large text and UI edges. Use the named text styles and spacing tokens from `references/system.md`; never a loose size or an ad hoc gap.

### 6. Build, section by section

Order: hero, proof row, product (how it works), the tagline section, output or gallery, scope or comparison, the second moment, about the maker (only when a named maker or team is part of the trust; otherwise skip it), pricing with risk reversal, FAQ (six to twelve real questions), closing CTA, footer. Drop what the product does not need; keep the order of argument. Build one section, look at it at 390 and 1440 px, then the next. Never rebuild the whole page per change.

Hero recipe: announcement or eyebrow only if it carries news; heading of two lines, eight words or fewer, 48 to 64 px, broken where the thought breaks, max 680 px; one line of how and for whom; one filled button with a verb and what they get, plus a text link; one quiet proof row at the bottom edge (rating, count, logos in one colour, or three stats with hairline dividers); the scene from step 2 full bleed behind it all, the copy in its quiet zone, and a small product layer (a card, a prompt box, a window peeking 80 px up from the bottom). The copy loads in 300 to 600 ms after the scene.

Phone hero: the visual must still say something at 390 px. Swap a wide product window for a cropped detail with text of 12 px or more; never shrink a full screen to unreadable.

Every call to action reaches something real: a form with validation and a success state, a booking dialog, a checkout or a download. A button that only jumps to another anchor is a dead end. Keep the primary action reachable at every width (a small nav button or a sticky bar on phones).

Habits that read as stock AI, avoid them by default: an all caps eyebrow over every heading (use a tag only where it carries the metaphor, in sentence case); an arrow icon on every button (only on a link that leaves the page); a fade in on every block (reveal section heads and the moments, not every card); a serif italic word in every heading (the hero only).

Tagline section: one large statement of the core promise (two lines or more), its words brightening one by one from 30% as it scrolls into view (`data-tagline` in `assets/motion.js`).

### 7. Motion pass, then calm pass

The scene loop is the hero, not a moment. Add the layer move (art over UI, UI out of art, or fixed scene under scrolling content). Add the floor (reveals, tagline, button feedback) with `assets/motion.js`. Add the moments; use GSAP with ScrollTrigger and Lenis only for pinned or scrubbed moments, self hosted. Each animation must name the product fact it shows; if it cannot, cut it. Then the calm pass: halve loops, cut grain and glow, remove one effect.

### 8. Verify

1. `python3 scripts/check.py path/to/index.html`, and `python3 scripts/check.py --secondary 404.html privacy.html` for pages that are not landing pages. Zero errors. Read every warning and fix it or write why it stays.
2. A real browser at 390, 768 and 1440 px, scrolled through so reveals and pinned sections run, and once more as a plain capture without scrolling (crawlers, link previews and print see that one, so nothing important may stay invisible): no horizontal scroll, the primary action visible in the first screen on a phone, nothing clipped, no orphans. Look at every screenshot yourself.
3. axe: zero violations, also with reduced motion.
4. Lighthouse mobile: performance 90 or more, accessibility, best practices and SEO 100. Video loads only in view, phones get a smaller film, fonts and libraries self hosted (Google Fonts links are fine for a prototype, never for production).
5. Every link and form works; forms validate; the 404 renders.

### 9. Critique and passes

Compare the first screen with the 17 recordings in `references/scenes.md` and the works in `references/portfolio.md` side by side at the same width. If yours is the only one without a moving scene, that is the first fix. Name what is weaker, fix it as a named pass ("proof pass", "motion pass v2", "calm pass"), and keep a changelog of passes in the hand off notes. Stop when a fresh reviewer cannot point to anything that reads as generic, not when a score is reached.

## Redesigning an existing page

Run `references/audit.md`: diagnose, report, let the owner veto, then fix in its order (scene first, then proof, type, colour, states, layout, motion, components, copy, ship list). Work inside the existing stack.

## References

- `references/scenes.md`: the moving scene: 17 recordings, 12 rules, how to make the still and the loop. Read in step 2.
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
| Passes every check, still looks generic | no scene, no idea | step 2; the checker is a floor |
| Owner loves the device or world but calls the page boring | standard web layout (header, hero copy, cards, manual) around the experience | make the experience the whole page; move the text version to a separate accessible route or a live region |
| Owner says "not a fan" of a clean, correct page | the hero is screenshots or type, not a picture | one moving scene that puns on the headline; proof moves below the fold |
| The scene looks like stock or AI slop | no pun, no named style, too many subjects | one subject doing one action, a two word style, two colours |
| The loop distracts | camera moves, several things move, or it jumps at the seam | static camera, one moving element, first frame equals last, slower |
| `no product proof` error | drawn or stock visuals only | real screenshots or a recording; a scene image with real UI over it |
| Looks busy | more than two moments, accent everywhere | calm pass; pop only on the button and two marks |
| Hero headline wraps to four lines on a phone | heading too long | eight words or fewer, clamp the size, balance |
| Lighthouse under 90 | video or analytics on load | load video in view, smaller phone file, analytics on first interaction |
| No horizontal scroll reported, but text is cut off on a phone | `overflow-x:clip` (used for a bleeding hero) hides overflow from `scrollWidth` | check element edges against the viewport; give grid and flex children `min-width:0` |
| A bleeding window hides the point of the screenshot | the bleed crops the newest or key part (latest data, RTL headings on the right) | crop the source so the key part is inside the frame; bleed only empty or old parts |
| The hero film looks empty in screenshots and on slow phones | the poster or first frame is the start of the run | the poster is the payoff frame; captions in HTML |
| A full page screenshot shows a big empty band | a pinned or scroll scrubbed section captured without scrolling | scroll through before capturing, or judge pinned sections in viewport shots |
| Inactive steps or tabs fail contrast | dimmed with opacity | dim with the `--fg-3` colour step, never opacity, and check 4.5:1 |
| A counter or mockup shows half finished numbers in a capture | the animation was caught mid run | render the final state by default and animate from it only in view; keep every number consistent across the page |
