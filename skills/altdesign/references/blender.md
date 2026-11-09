# Blender for films, scenes and backdrops

Majid made the AREZ hero film in Blender and recommends it for any animation a page needs. A rendered film shows the product's one job in 12 to 16 seconds, which no paragraph does. Use Blender for:

- **The hero film**: the promise happening, in 4 to 6 beats (AREZ: model, cladding peels off, load path pulses, beam B-204 fails at 1.18 and passes at 0.71 after the resize, the camera rises to a top down plan, the plan dissolves into sheet S-101).
- **A scene still**: the picture that acts out the headline (see `portfolio.md`, rule 1), when the subject can be modelled.
- **Backdrops**: soft stills behind the tagline and closing bands, at 20 to 30% opacity under a ground colour overlay (AREZ: framing and aerial renders).
- **Loops and product renders**: a short seamless loop for a section, a product object on a studio ground.
- **The Open Graph image**: a frame of the film at 1200x630.

## Pipeline

Everything is code, so the film can be re-rendered after any product change. Start from `assets/blender/film.py` and `assets/blender/beats.json`.

1. **Storyboard as beats.** Write `beats.json`: a name, seconds and a camera position per beat, 12 to 16 s in total, each beat one idea that matches a chapter on the page. The same file gives the page its chapter buttons (`chapters.json` with start times).
2. **Build the subject from real data.** Replace `build_subject()` with the product's own subject, generated from its real data where possible (AREZ built a procedural 7,000 sf wood frame house and coloured each member by its real utilisation ratio). Avoid generic shapes standing in for the product.
3. **Palette from the page.** Ground, ink and pop come from the page tokens. The pop marks only the moment that matters (the failing member, the matched row, the signed sheet).
4. **Light and camera.** One key light from above, a soft fill, a rim: the same light direction as the page's shadows. One camera move per beat, eased (Bezier keys, never linear). Hold the last beat so the film rests on its payoff.
5. **No text in the frames.** Captions, numbers and labels go in HTML beside or over the video, so they stay sharp, translatable, accessible and indexable.
6. **Preview, then render.** `--preview` renders every 4th frame at half size; make a contact sheet and check the story before the full render. Render a still of the payoff frame with `--still <frame>` for the poster.
7. **Encode.**

```bash
blender -b --factory-startup -P film.py -- --beats beats.json --out frames --preview   # check the story
blender -b --factory-startup -P film.py -- --beats beats.json --out frames            # full render
blender -b --factory-startup -P film.py -- --beats beats.json --out poster --still 260
ffmpeg -framerate 24 -i frames/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 23 -preset slow -movflags +faststart -an hero-film.mp4
ffmpeg -framerate 24 -i frames/f%04d.png -vf scale=720:-2 -c:v libx264 -pix_fmt yuv420p -crf 26 -preset slow -movflags +faststart -an hero-film-mobile.mp4
ffmpeg -i poster/still.png -c:v libwebp -quality 82 hero-film-poster.webp
```

Targets: desktop 1280x720 about 5 MB for 15 s; phone 720 px wide about 1.5 MB; poster WebP under 100 KB.

8. **On the page.** `<video muted playsinline preload="none" poster="hero-film-poster.webp">` with a phone source and a desktop source; load and play only when in view; chapter buttons seek `currentTime` and show the caption; the poster is the payoff frame (the result), never frame 1, because a static screenshot, a slow phone and reduced motion users all see the poster. Under reduced motion, show the poster and the chapter captions, no playback.
9. **Keep the source.** Commit `film.py`, `beats.json` and a README with the render commands. Do not commit frames or `.blend` files.

## Measured on our machine (XPS, Blender 5.2.3, Intel UHD 630, no discrete GPU)

- EEVEE works headless and needs real GPU access: run it outside any sandbox. The `EGL_BAD_MATCH` warnings it prints are harmless.
- The template scene: about 3 s a frame at 1280x720 for a still; a 12 s preview (72 frames at half size) took 4 min 16 s. A full 15 s film at 720p takes about 20 to 30 minutes for a simple scene. Plan the preview step.
- Cycles runs on CPU only here (6 s a still at 16 samples); use it for stills, not films.
- Never render on a small laptop; use the build machine.

## Common problems

| Symptom | Fix |
|---|---|
| The camera flips or rolls at a top down beat | offset the camera a hair on Y (the template uses -0.01) or animate an up vector |
| The film looks empty in screenshots | the poster and the first visible frame must be the payoff, not the start of the run |
| Unreadable on a phone | a phone cut that frames the key part closer, and captions in HTML |
| Banding in dark gradients | add the page grain over the video, or raise the bitrate on dark scenes |
| Looks like a tech demo | build the subject from the product's real data and give each beat one idea from the headline |
