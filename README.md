The African Vision — static mirror

This repository is a static mirror of a WordPress site exported with HTTrack and cleaned for static hosting.

Contents:
- Static HTML files (root and subfolders)
- `wp-content/uploads/...` media assets

Notes:
- Dynamic WordPress/PHP functionality (comments, search, admin) has been removed or replaced.
- Contact forms were pointed to Formspree placeholders — update `action` values before going live.

Deployment:
- Cloudflare Pages (recommended):
	1. Push this repository to GitHub (branch `site-mirror` already created).
	2. In Cloudflare dashboard > Pages, create a new project and connect this GitHub repo.
	3. Set build command to empty and build output directory to the repository root (`/`).
	4. (Optional) Set environment variables if you plan to use Workers or R2.

- Wrangler (optional):
	- Install Wrangler: `npm install -g wrangler`
	- Authenticate: `wrangler login`
	- Publish: `wrangler pages publish ./ --project-name=<PROJECT_NAME>`

Notes before going live:
- Verify `action` URLs on contact forms — replace Formspree placeholders with your production endpoint.
- Check `canonical` and `og:url` meta tags to point to `https://theafricanvision.org`.
- If you do not want `.bak` files in the public repo, delete them (done here).
- Use Cloudflare Pages redirects or Workers for any custom rewrites.

Author: prepared by maintainer
