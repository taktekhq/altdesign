# altdesign

A design skill for AI coding agents (Claude Code, Codex, Cursor) that builds landing pages and product sites that look made by a senior designer, not by AI.

Most "make it look good" rules fix type, spacing and colour. Those are the floor. What makes a page look made by a designer is **one moving scene** on the first screen (a picture in a named style that puns on the headline, animated into a short loop with an image to video model), **proof** below it (real screenshots, real output, cards that work), **one idea** carried through the page, and one or two **moments** people remember. altdesign makes the agent do those first, then applies a strict visual system, then checks the result with a script and a real browser.

## What is inside

```
skills/altdesign/
  SKILL.md                 the workflow: brief, the scene, proof inventory, direction, system, build, motion, verify, passes
  references/scenes.md     17 of Elaya's screen recordings studied frame by frame; how to make the still and the loop
  references/system.md     every value: two plus one palette, type styles, spacing, radius, surfaces, nav, motion, imagery, states, ship list
  references/portfolio.md  19 landing pages from elaya.design studied and counted, 12 rules for heroes and imagery
  references/sources.md    what each source taught and how their conflicts were resolved
  references/audit.md      redesign audit and fix order for an existing page
  references/blender.md    hero films, scene stills and backdrops rendered in Blender from code, with timings
  assets/tokens.css        starter tokens with a dark and light band flip, text styles, buttons, floating nav, product window, grain
  assets/motion.js         reveals, the tagline word reveal, number roll, scroll scrubbed video; no dependencies
  assets/blender/          film.py and beats.json: a headless Blender film whose beats also drive the page's chapter buttons
  scripts/check.py         mechanical checker (Python standard library), exit 1 on errors
```

## Install

Claude Code, per user:

```bash
git clone https://github.com/taktekhq/altdesign.git
mkdir -p ~/.claude/skills && cp -r altdesign/skills/altdesign ~/.claude/skills/
```

Other agents: copy `skills/altdesign` into the folder your agent reads skills from (`.agents/skills/` for Codex and Cursor), or point your rules file at `SKILL.md`.

Then ask in plain words: "build a landing page for ...", "redesign this page", "this site looks generic".

## The checker

```bash
python3 skills/altdesign/scripts/check.py site/index.html site/pricing.html
python3 skills/altdesign/scripts/check.py --json site/index.html
```

It flags: no product proof (zero raster images or videos), a hero section with no looping video or one missing autoplay, muted, loop, playsinline or a poster, em dashes and filler words, banned default fonts, more than one sans family, ultra bold weights, off scale sizes and spacing, default easing, animating layout properties, motion without a reduced motion rule, too many background gradients, missing lang, title, description, Open Graph, favicon, main, h1, focus style, alt text, links to `#`, and missing structured data. It is a floor: a page can pass it and still look generic. Steps 2, 3 and 8 of the skill are the bar.

## Tests

```bash
python3 -m unittest discover tests
```

## Sources and credit

- The AREZ marketing site (tryarez.com, v33, Nov 2026) by Majid Yassine: the proof, metaphor, moments and many-passes lessons, and his advice to make animations in Blender.
- [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) and [elayadesign/redesign-skill](https://github.com/elayadesign/redesign-skill) by Elaya (MIT): the visual system, intake, content realism, states, audit.
- The portfolio on [elaya.design](https://elaya.design): the hero and imagery rules.
- [Elaya's screen recordings on X](https://x.com/elayadesigns) (17 posts, Oct to Nov 2026): the moving scene, layering art with UI, the image then video workflow.
- Diego Aranda's reel on palettes that look expensive: two colours that get along, one that pops, and the pop only on the button.
- [taste-skill](https://github.com/Leonxlnx/taste-skill) by Leon Lin (MIT), credited by Elaya's skills: one or two moments per page.

MIT licensed. See LICENSE for the adapted notices.
