# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **dependency-free static website** ("Nhà Bếp Của Mẹ — Our Family Kitchen", a Vietnamese family-recipe site). It is plain HTML/CSS/vanilla JS with no package manager, no build step, no backend, and no database.

- **Run (dev):** serve the repo root with any static file server, e.g. `python3 -m http.server 8000` from `/workspace`, then open `http://localhost:8000/index.html`. `python3` is preinstalled.
- **Build:** none. Files are served as-is. `index.html` uses a manual `?v=N` cache-busting query string on `css/style.css` (hand-edited, not tooling-generated).
- **Test:** no automated test suite exists. Verify changes by loading pages in a browser.
- **Lint:** no linter is configured in-repo.
- **Core interactive behavior** lives in `js/main.js`: the mobile menu toggle and the recipe category filtering on `recipes.html` (filter tabs + `?#category` deep links via `data-filter`/`data-category`). Test filtering by serving over HTTP and clicking a category tab.
- Recipe detail pages are individual static files under `recipes/*.html`; images are in `images/` (handwritten scans under `images/scans/`).
