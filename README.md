# farras · portfolio

Graphic designer and Computer Engineering student. A blue-and-white halftone
portfolio: posters, documentation, embedded systems and software.

Live: https://slickboiras.github.io (previous canvas version: /v1/)

## Edit
1. Change content in `src/page.html`, in the `CONTENT` block at the top of the script
   (projects, skills, persona texts). Section text (About, Path, Contact) is plain HTML above it.
2. Put new images in `src/img/` as `.jpg` and reference them as `__IMG:filename__`.
3. Rebuild: `python3 src/build.py` writes `index.html` with the images inlined.
4. Commit and push. GitHub Pages updates in a minute or two.

## Interactions
Halftone name reacts to the cursor (click for a ripple) · headline letters widen under the cursor ·
skills columns open like an accordion · project cards open a detail view (←/→ to step, Esc to close) ·
`Invert` swaps to white-on-blue.
