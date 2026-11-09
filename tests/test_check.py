"""Tests for skills/altdesign/scripts/check.py.  Run: python3 -m unittest discover tests"""
import os, subprocess, sys, tempfile, unittest

CHECK = os.path.join(os.path.dirname(__file__), "..", "skills", "altdesign", "scripts", "check.py")
sys.path.insert(0, os.path.dirname(CHECK))
import check  # noqa: E402

GOOD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Ledgerline</title>
<meta name="description" content="Close the books in two days."><meta property="og:title" content="Ledgerline">
<meta property="og:image" content="https://example.com/og.jpg"><link rel="canonical" href="https://example.com/">
<link rel="icon" href="icon.svg"><script type="application/ld+json">{}</script>
<style>body{font-family:"Manrope",sans-serif;font-size:16px;padding:24px;text-wrap:pretty}
h1{font:600 60px/1 "Manrope",sans-serif;text-wrap:balance}
.btn{transition:transform .5s cubic-bezier(.22,1,.36,1)}:focus-visible{outline:2px solid}
@media (prefers-reduced-motion:reduce){*{transition:none}}</style></head>
<body><a class="skip" href="#main">Skip to content</a><main id="main"><section><h1>Close the books in two days.</h1>
<img src="shot.webp" alt="The reconciliation view"><video src="film.mp4" autoplay muted loop playsinline poster="film.webp"></video>
<a class="btn" href="/trial">Start 14 day trial</a></section></main></body></html>"""

BAD = """<html><head><style>body{font-family:Inter,Roboto;font-weight:900;padding:13px;
transition:all .2s ease}</style></head><body><h1>Revolutionize your workflow — seamlessly!</h1>
<img src="hero.svg"><a href="#">Learn more</a></body></html>"""


def run(html):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    try:
        return check.check_file(f.name)
    finally:
        os.unlink(f.name)


class CheckTest(unittest.TestCase):
    def test_good_page_has_no_errors(self):
        r = run(GOOD)
        self.assertEqual(r["errors"], [], r)

    def test_bad_page_errors(self):
        errs = " ".join(run(BAD)["errors"])
        for needle in ["em dash", "revolutionize", "seamless", "banned default font", "ultra bold",
                       "no product proof", "lang", "<main>", "favicon", "reduced-motion"]:
            self.assertIn(needle, errs)

    def test_bad_page_warnings(self):
        warns = " ".join(run(BAD)["warnings"])
        for needle in ["learn more", "spacing values off the scale", "default easing", "'#'"]:
            self.assertIn(needle, warns)

    def test_var_font_resolved(self):
        r = run(GOOD.replace('font-family:"Manrope",sans-serif', 'font-family:var(--f)').replace("<style>", "<style>:root{--f:Inter,sans-serif}"))
        self.assertTrue(any("inter" in e for e in r["errors"]), r)

    def test_secondary_page_needs_no_proof(self):
        page = GOOD.replace('<img src="shot.webp" alt="The reconciliation view"><video src="film.mp4" autoplay muted loop playsinline poster="film.webp"></video>', "")
        page = page.replace('<meta property="og:image" content="https://example.com/og.jpg">', "")
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
            f.write(page)
        try:
            self.assertEqual(check.check_file(f.name, secondary=True)["errors"], [])
            self.assertTrue(check.check_file(f.name)["errors"])
        finally:
            os.unlink(f.name)

    def test_hero_scene(self):
        self.assertFalse([w for w in run(GOOD)["warnings"] if "hero" in w])
        no_film = GOOD.replace('<video src="film.mp4" autoplay muted loop playsinline poster="film.webp"></video>', "")
        self.assertTrue(any("no moving scene" in w for w in run(no_film)["warnings"]))
        bare = GOOD.replace(' autoplay muted loop playsinline poster="film.webp"', "")
        self.assertTrue(any("missing autoplay" in w for w in run(bare)["warnings"]))
        below = GOOD.replace('<video src="film.mp4" autoplay muted loop playsinline poster="film.webp"></video>', "").replace("</main>", '<section><video src="f.mp4"></video></section></main>')
        self.assertTrue(any("no moving scene" in w for w in run(below)["warnings"]))

    def test_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            g, b = os.path.join(d, "g.html"), os.path.join(d, "b.html")
            open(g, "w").write(GOOD)
            open(b, "w").write(BAD)
            self.assertEqual(subprocess.run([sys.executable, CHECK, g], capture_output=True).returncode, 0)
            self.assertEqual(subprocess.run([sys.executable, CHECK, b], capture_output=True).returncode, 1)


if __name__ == "__main__":
    unittest.main()
