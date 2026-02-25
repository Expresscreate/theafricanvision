The African Vision — static mirror

This repository is a static mirror of a WordPress site exported with HTTrack and cleaned for static hosting.

Contents:
- Static HTML files (root and subfolders)
- `wp-content/uploads/...` media assets

Notes:
- Dynamic WordPress/PHP functionality (comments, search, admin) has been removed or replaced.
- Contact forms were pointed to Formspree placeholders — update `action` values before going live.

Deployment:
- Recommended: Cloudflare Pages — connect this repository and set the build directory to the repo root.
- Or use `wrangler pages publish ./` to deploy via Cloudflare Wrangler.

Author: prepared by maintainer
