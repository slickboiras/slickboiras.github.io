# farras · portfolio

Half designer, half engineer. An interactive portfolio built like a design app:
infinite canvas, working tools (pen, eyedropper, zoom), live dither textures,
and a TECH mode that shows how everything is built.

Live: https://slickboiras.github.io

## Edit
1. Change content in `src/template.html` (the `CONTENT` block at the top of the script:
   profile, designs, photos, projects, music, contact).
2. Put new images in `src/img/` and reference them as `'__IMG:name__'` with `ratio: __R:name__`.
3. Rebuild: `python3 src/build.py` (needs Pillow) → writes `index.html`.
4. Commit and push. GitHub Pages updates in a minute or two.

## Shortcuts
`V` move · `H` hand · `P` pen · `I` eyedropper · `Z` zoom · `T` art/tech · `1–6` boards · `0` fit all · `Q` quick view
