# GRIT website — draft

A simple static site (no build step needed) styled after sdgoed.com, with the real
GRIT logo dropped in. Built for a quick GitHub Pages host so the task force can
review it as a live link.

## What's here

- `index.html` — Home (hero, "Getting Started", mission teaser)
- `about.html` — About GRIT (mission, how GRIT was formed, partnerships, FAQ)
- `lifelines.html` — Critical Lifelines overview (phase 1)
- `resources.html` — Resources / Preparedness stub (phase 1, content pending)
- `energy.html`, `water.html`, `transportation.html`, `communications.html` —
  Phase 2 sector stub pages, linked from the "Sectors" dropdown in the nav
- `assets/styles.css`, `assets/script.js` — shared styles and nav behavior
- `assets/img/grit-logo-full.png`, `assets/img/grit-icon.png` — the logo (full
  lockup and a cropped icon-only mark used in the nav/footer)
- `build_site.py` — regenerates all the HTML pages from shared templates, so
  header/footer/nav only need to be edited in one place. Run `python3
  build_site.py` after editing it.

## Two things flagged for confirmation (see the on-page notes too)

1. **Task force name** — the site uses "Governor's Resilient Infrastructure
   Task Force" to match the logo and the original About GRIT draft. Press
   coverage of the executive order called it the "Governor's Resilience and
   Infrastructure Task Force" — worth a quick check with comms on which is
   correct going forward.
2. **Signing date** — used June 2, 2025 for Executive Order 2025-06; press
   coverage was inconsistent (reports ranged June 2–5). Worth confirming
   against the signed order.

There's an orange "DRAFT SITE" banner at the top of every page and a couple of
inline notes marked "Internal note" — delete the banner `<div>` in
`build_site.py`'s `page()` function and the `.note` blocks in `about.html`
(or in `build_site.py`, then rebuild) once everything is confirmed.

## Hosting it on GitHub Pages

1. Push this folder to a new (or existing) GitHub repo.
2. In the repo settings → Pages, set the source to the branch/root you pushed to.
3. GitHub gives you a URL like `https://<username>.github.io/<repo>/` — that's
   a shareable link straight to `index.html`. `about.html` is reachable at
   `https://<username>.github.io/<repo>/about.html`.

No build tools, frameworks or npm install required — it's plain HTML/CSS/JS.

## Still to do (Phase 2 / later)

- Real photography to replace the abstract hero background pattern
- Content for the Resources page (72-hour kit, family plan, seasonal prep,
  financial readiness, pets, downloads)
- Full sector pages (Energy, Water, Transportation, Communications) — leads
  noted on each stub page
- Task force member list / headshots on the About page
- Remaining empty FAQ answers on the About page
