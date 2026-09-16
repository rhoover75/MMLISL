# Randy C. Hoover — research site

Static site for Dr. Randy C. Hoover / the Mines Machine Learning and
Intelligent Systems Lab (MMLIS‑L), built to replace the Google Sites page at
`sites.google.com/sdsmt.edu/rhoover/home`. Plain HTML/CSS, no build step —
ready to serve as-is from GitHub Pages.

## Structure

```
index.html            Home — bio, contact info, news
research.html          Current research projects
people.html            Current students & alumni
publications.html      Full publication list, grouped by year
assets/css/style.css   Shared stylesheet
assets/img/            Photo, favicons
```

## Publishing on GitHub Pages

1. Create a new repository (or use an existing one) and upload everything in
   this folder to the repo root, keeping the `assets/` subfolder structure
   intact.
2. In the repo, go to **Settings → Pages**, and under "Build and
   deployment" set the source branch to `main` (or whichever branch you
   uploaded to) and the folder to `/ (root)`. Save.
3. GitHub will publish the site at `https://<username>.github.io/<repo>/`
   within a minute or two.

## Custom domain (optional)

If you want this served from your own domain instead of the default
`github.io` address:

1. **GitHub side:** Settings → Pages → type the domain into "Custom
   domain" → Save. This creates a `CNAME` file in the repo root with just
   the bare domain (no `https://`, no path, no trailing slash).
2. **DNS side (registrar):** delete any default parking-page records, then
   add 4 **A records** (host `@`) pointing at GitHub Pages' IPs —
   `185.199.108.153`, `.109.153`, `.110.153`, `.111.153` — plus one
   **CNAME record** (host `www`) pointing at `<username>.github.io`.
3. DNS propagation can take a little while. If "Enforce HTTPS" stays
   greyed out right after setup, that's normal — GitHub rechecks DNS
   periodically and only requests a certificate once the check passes.

## Updating content

Everything is plain HTML — edit the relevant page directly:

- **News** on the home page: add a new `<li>` inside the first
  `<ol class="timeline">` block (most recent items go in the visible list;
  older ones live inside the `<details>` block further down).
- **Publications**: add a new `<li>` inside the matching `<div
  class="pub-year">` block, or create a new `.pub-year` block for a new
  year (most recent year first).
- **People**: current students use `.person-card` blocks; alumni use
  `.alumni-row` blocks. Copy an existing block and edit the name, avatar
  initials, and detail line. Avatar colors cycle through a small palette
  defined inline — pick any of the existing hex values, or add your own.

## Design

"Contour" theme — bone-white paper background, ink-black text, a single
pine-teal accent (`#1f6f6b`), with ochre (`#a67c2e`) reserved for small
kickers and the faint topographic contour-line motif in each page's hero
(a quiet nod to the manifold/subspace-learning research — level sets of a
function, drawn as literal contour lines). Headings are set in Newsreader
(serif), body text in Public Sans. All of it lives in
`assets/css/style.css` as CSS custom properties at the top of the file —
change a value there to retint the whole site.

## Notes on content transfer

Text content (bio, news, publications, people, research project
descriptions) was transcribed directly from the live Google Site. The
Google-hosted photos on the People and Research pages could not be
reliably re-downloaded (Google's image CDN blocked cross-origin fetches
from the page), so:

- The Home page keeps the one photo that did transfer successfully
  (`assets/img/team-photo.png`).
- People are represented with color-coded initials avatars instead of
  individual photos.
- Research projects use small custom line-art icons instead of the
  original diagrams.

If you'd like the original photos/diagrams included, save them from the
Google Site directly (right-click → Save Image) and drop them into
`assets/img/`, then swap the relevant `<img>` or avatar markup.

Three research projects on the Research page (Covert Video Analytics,
SkipGCN, Temporal Tensor Factorization) had no description text on the
original site — they're marked "Project overview to be added" as a
placeholder.
