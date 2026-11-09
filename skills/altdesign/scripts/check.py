#!/usr/bin/env python3
"""altdesign check: test a built page against the mechanical altdesign rules.

    python3 check.py site/index.html [more.html ...]   # local files; linked local CSS is read too
    python3 check.py --json site/index.html            # machine readable
    python3 check.py --secondary 404.html privacy.html # pages that are not landing pages: no proof or social image required

Exit 0 when there are no errors (warnings allowed), 1 when any error is found.
Standard library only. It reads HTML and CSS as text; it does not run the page.
Run a real browser check as well (390 / 768 / 1440 px, axe, Lighthouse); see SKILL.md, step 7.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

SPACING = {0, 1, 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 120}
TYPE_SCALE = {12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96, 128}
BANNED_FONTS = ["inter", "roboto", "arial", "open sans", "helvetica", "lato", "montserrat", "poppins italic"]
FILLER = ["revolutionize", "revolutionise", "supercharge", "cutting edge", "cutting-edge", "effortless",
          "transform your workflow", "next level", "harness the power", "world class", "world-class",
          "seamless", "unleash", "elevate your", "game changer", "game-changer", "lorem ipsum", "your headline here"]
WEAK_CTA = ["learn more", "submit", "click here", "get started now"]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text, self.styles, self.links, self.scripts = [], [], [], []
        self.meta, self.tags, self.imgs, self.buttons = {}, {}, [], []
        self.title, self.lang = "", None
        self._skip = 0
        self._in = []
        # Hero tracking: media inside the top level section that holds the h1
        self.sec_depth, self.sec_n, self.cur_sec = 0, 0, None
        self.sec_media, self.h1_sec, self.videos = {}, None, []

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag in ("section", "header"):
            self.sec_depth += 1
            if self.sec_depth == 1:
                self.sec_n += 1
                self.cur_sec = self.sec_n
        if tag == "h1" and self.h1_sec is None:
            self.h1_sec = self.cur_sec
        if tag in ("img", "video") and self.cur_sec is not None:
            self.sec_media.setdefault(self.cur_sec, []).append(tag)
        if tag == "video":
            self.videos.append((self.cur_sec, a))
        self.tags[tag] = self.tags.get(tag, 0) + 1
        self._in.append(tag)
        if tag == "html":
            self.lang = a.get("lang")
        if tag in ("script", "style", "noscript", "svg"):
            self._skip += 1
        if tag == "link" and "stylesheet" in (a.get("rel") or ""):
            self.links.append(a.get("href", ""))
        if tag == "script" and a.get("src"):
            self.scripts.append(a["src"])
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.meta[k.lower()] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a.get("href", "")
        if tag == "link" and "icon" in (a.get("rel") or ""):
            self.meta["icon"] = a.get("href", "")
        if tag == "img":
            self.imgs.append(a)
        if tag == "a" and (a.get("href") in ("#", "", None)) and "role" not in a:
            self.buttons.append(("dead-link", a))
        if tag == "a" and "skip" in (a.get("class") or "") + (a.get("href") or ""):
            self.meta["skip"] = "1"
        if a.get("style"):
            self.styles.append("x{" + a["style"] + "}")

    def handle_endtag(self, tag):
        if tag in ("section", "header") and self.sec_depth:
            self.sec_depth -= 1
            if self.sec_depth == 0:
                self.cur_sec = None
        if tag in ("script", "style", "noscript", "svg") and self._skip:
            self._skip -= 1
        if self._in:
            self._in.pop()

    def handle_data(self, d):
        if self._in and self._in[-1] == "style":
            self.styles.append(d)
        elif self._in and self._in[-1] == "title":
            self.title += d
        elif not self._skip and d.strip():
            self.text.append(d.strip())


def px(v):
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", v.strip())
    return float(m.group(1)) if m else None


def check_file(path, secondary=False):
    errors, warns, notes = [], [], []
    html = open(path, encoding="utf-8", errors="replace").read()
    p = Page()
    p.feed(html)
    css = "\n".join(p.styles)
    base = os.path.dirname(path)
    for href in p.links:
        if href.startswith(("http:", "https:", "//")):
            continue
        f = os.path.join(base, href.split("?")[0].lstrip("/")) if not href.startswith("/") else os.path.join(base, href.split("?")[0][1:])
        if os.path.isfile(f):
            css += "\n" + open(f, encoding="utf-8", errors="replace").read()
    css_nc = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    text = " ".join(p.text)
    low = text.lower()

    # Copy
    if "\u2014" in text:
        errors.append(f"em dash in page text ({text.count(chr(0x2014))}x); rewrite as two sentences or a comma")
    if re.search(r"\s–\s|\s-\s", text):
        warns.append("spaced dash used as punctuation in text; rewrite the phrase")
    for w in FILLER:
        if w in low:
            errors.append(f"filler phrase: '{w}'")
    for w in WEAK_CTA:
        if re.search(r"(^|\W)" + re.escape(w) + r"(\W|$)", low):
            warns.append(f"weak call to action text: '{w}'")
    if "!" in text.replace("<!", ""):
        warns.append(f"exclamation marks in copy ({text.count('!')}x)")

    # Type
    for name, val in re.findall(r"(--[\w-]+)\s*:\s*([^;}]+)", css_nc):
        if "var(" not in val:
            css_nc = css_nc.replace(f"var({name})", val)
    fams = set(m.strip().strip("'\"").lower() for decl in re.findall(r"font-family\s*:\s*([^;}]+)", css_nc)
               for m in decl.split(","))
    fams |= set(m.strip().strip("'\"").lower() for decl in re.findall(r"font\s*:[^;}]*?\d+px(?:/[\w.]+)?\s+([^;}]+)", css_nc)
                for m in decl.split(","))
    named = {f for f in fams if f and not f.startswith("var(") and f not in
             ("system-ui", "sans-serif", "serif", "monospace", "ui-monospace", "ui-sans-serif", "inherit", "-apple-system",
              "blinkmacsystemfont", "consolas", "menlo", "segoe ui", "courier new")}
    for b in BANNED_FONTS:
        if b in named:
            errors.append(f"banned default font family: {b}")
    mono = {f for f in named if "mono" in f or "code" in f}
    serif_flourish = {f for f in named if "serif" in f and "sans" not in f or f in ("newsreader", "eb garamond", "georgia", "fraunces")}
    if len(named - mono - serif_flourish) > 1 or len(serif_flourish) > 2:
        warns.append(f"more than one non mono family: {sorted(named - mono)} (one family per site, plus a mono for data)")
    if re.search(r"font-style\s*:\s*italic", css_nc):
        warns.append("italic in use: allowed only for the hero flourish (a serif, 3 words or fewer); elsewhere use weight or colour")
    if re.search(r"font-weight\s*:\s*(800|900|black)", css_nc):
        errors.append("ultra bold weight (800/900); cap at 700")
    sizes = [px(v) for v in re.findall(r"font-size\s*:\s*([\d.]+px)", css_nc)]
    sizes += [px(v) for v in re.findall(r"font\s*:\s*(?:normal\s+)?(?:\d{3}\s+)?([\d.]+px)", css_nc)]
    off = sorted({s for s in sizes if s is not None and s not in TYPE_SCALE})
    if off:
        warns.append(f"font sizes off the type scale: {off}")
    if "text-wrap" not in css_nc:
        warns.append("no text-wrap: balance / pretty; headings may leave orphans")

    # Space
    vals = []
    for prop, v in re.findall(r"(?<![\w-])(padding(?:-[a-z-]+)?|margin(?:-[a-z-]+)?|gap|row-gap|column-gap)\s*:\s*([^;}]+)", css_nc):
        vals += [px(x) for x in v.split() if px(x) is not None]
    offs = sorted({abs(v) for v in vals if abs(v) not in SPACING})
    if offs:
        warns.append(f"spacing values off the scale: {offs[:20]}{' ...' if len(offs) > 20 else ''}")

    # Motion
    for t in re.findall(r"transition\s*:\s*([^;}]+)", css_nc):
        if re.search(r"(?<![-\w])(ease|linear|ease-in-out|ease-in)(?![-\w])", t) and "cubic-bezier" not in t and "var(" not in t:
            warns.append(f"default easing in transition: '{t.strip()[:60]}'; use the base curve")
            break
    if re.search(r"transition\s*:[^;}]*(?<![-\w])(top|left|width|height)(?![-\w])", css_nc):
        warns.append("transition on top/left/width/height; animate transform and opacity")
    has_motion = re.search(r"@keyframes|transition|gsap|animate\(", css_nc + html)
    if has_motion and "prefers-reduced-motion" not in css_nc + html:
        errors.append("motion without a prefers-reduced-motion rule")
    if re.search(r"addEventListener\(\s*['\"]scroll['\"]", html) and "requestAnimationFrame" not in html:
        warns.append("raw scroll listener without requestAnimationFrame; use IntersectionObserver or ScrollTrigger")

    # Surfaces
    bg_grad = re.findall(r"background(?:-image)?\s*:\s*[^;}]*(linear|radial|conic)-gradient", css_nc)
    if len(bg_grad) > 6:
        warns.append(f"{len(bg_grad)} background gradients; keep surfaces flat (gradients only on hero text and image overlays)")
    if re.search(r"#(?:6366f1|8b5cf6|7c3aed|a855f7)\b", css_nc, re.I):
        warns.append("purple/indigo 'AI gradient' colours found")

    # Page completeness
    if not p.lang:
        errors.append("<html> has no lang")
    if not p.title.strip():
        errors.append("no <title>")
    for k in ("description",) if secondary else ("description", "og:image", "og:title"):
        if k not in p.meta:
            errors.append(f"missing meta {k}")
    if "canonical" not in p.meta:
        warns.append("no canonical link")
    if "icon" not in p.meta:
        errors.append("no favicon")
    if "viewport" not in p.meta:
        errors.append("no viewport meta")
    if "skip" not in p.meta:
        warns.append("no skip to content link")
    if not p.tags.get("main"):
        errors.append("no <main> element")
    if not p.tags.get("h1"):
        errors.append("no <h1>")
    elif p.tags["h1"] > 1:
        warns.append(f"{p.tags['h1']} <h1> elements")
    if ":focus-visible" not in css_nc and ":focus" not in css_nc:
        errors.append("no focus style")
    missing_alt = [i.get("src", "?") for i in p.imgs if "alt" not in i]
    if missing_alt:
        errors.append(f"{len(missing_alt)} images without alt: {missing_alt[:3]}")
    dead = [b for b in p.buttons if b[0] == "dead-link"]
    if dead:
        warns.append(f"{len(dead)} links pointing at '#'")
    # Proof: real pictures and film of the product, not drawn stand-ins
    raster = [i for i in p.imgs if re.search(r"\.(png|jpe?g|webp|avif|gif)(\?|$)", i.get("src", "") or i.get("data-src", ""), re.I)]
    media = len(raster) + p.tags.get("video", 0)
    sections = max(p.tags.get("section", 0), 1)
    if secondary:
        pass
    elif media == 0:
        errors.append("no product proof: 0 raster images and 0 videos (screenshots, real output, a film)")
    elif media * 2 < sections:
        warns.append(f"thin proof: {media} images/videos for {sections} sections; aim for one per two sections or better")
    # Scene: the first screen is one moving picture (references/scenes.md)
    if not secondary:
        hero = p.sec_media.get(p.h1_sec, []) if p.h1_sec is not None else []
        if "video" not in hero:
            warns.append("hero has no moving scene: no <video> in the section with the h1; the first screen should be one looping picture that puns on the headline")
        for sec, v in p.videos:
            if sec == p.h1_sec:
                miss = [k for k in ("autoplay", "muted", "loop", "playsinline", "poster") if k not in v]
                if miss:
                    warns.append(f"hero video is missing {', '.join(miss)}; a scene loop needs autoplay muted loop playsinline and a poster")
    # Conversion: at least one call to action must lead somewhere real
    hrefs = re.findall(r'<a\b[^>]*class="[^"]*\b(?:btn|button|cta)[^"]*"[^>]*href="([^"]*)"|<a\b[^>]*href="([^"]*)"[^>]*class="[^"]*\b(?:btn|button|cta)[^"]*"', html)
    targets = [a or b for a, b in hrefs]
    real = [h for h in targets if h and not h.startswith("#")]
    if not secondary and targets and not real and "<form" not in html and "<dialog" not in html and "showModal" not in html:
        errors.append("calls to action are dead ends: every button links to an anchor and the page has no form, dialog or real URL")
    if "ld+json" not in html and not secondary:
        warns.append("no JSON-LD structured data")
    notes.append(f"proof: {len(raster)} raster images, {p.tags.get('video', 0)} videos, {sections} sections")
    notes.append(f"families: {sorted(named) or 'none found'}; sizes used: {sorted({s for s in sizes if s})}")
    return {"file": path, "errors": errors, "warnings": warns, "notes": notes}


def main(argv):
    as_json = "--json" in argv
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 2
    results = [check_file(f, "--secondary" in argv) for f in files]
    if as_json:
        print(json.dumps(results, indent=1))
    else:
        for r in results:
            print(f"== {r['file']}: {len(r['errors'])} errors, {len(r['warnings'])} warnings")
            for e in r["errors"]:
                print("  ERROR ", e)
            for w in r["warnings"]:
                print("  warn  ", w)
            for n in r["notes"]:
                print("  note  ", n)
    return 1 if any(r["errors"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
