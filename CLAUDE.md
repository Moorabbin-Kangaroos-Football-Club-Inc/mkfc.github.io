# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Official website for the **Moorabbin Kangaroos Football Club** (MKFC), an Australian rules football club in the Southern Football and Netball League. Hosted on GitHub Pages at www.mkfc.org.au.

## Build & Development

```bash
bundle exec jekyll serve
```

This builds the site and serves it locally with live reload. Note: changes to `_config.yml` require a server restart.

There is no Gemfile checked into the repo — GitHub Pages provides the Ruby/Jekyll environment. For local development, you need Ruby, Bundler, and Jekyll installed.

## Architecture

- **Static site generator**: Jekyll with the **Minima** theme
- **Content**: All pages are Markdown files with YAML frontmatter
- **Templating**: Liquid (Jekyll's default template engine)
- **Deployment**: GitHub Pages (automatic on push to `main`)
- **Custom domain**: Configured via `CNAME` file pointing to `www.mkfc.org.au`

## Site Structure

Navigation is defined in `_config.yml` under `header_pages` and maps to:

| Route | File |
|-------|------|
| Home | `index.md` |
| About | `about/index.md` |
| News | `news/index.md` |
| Players | `players/index.md` |
| Gallery | `gallery/index.md` |
| Sponsors | `sponsors/index.md` |
| Calendar | `calendar/index.md` |
| Contact | `contact/index.md` |

Static assets (logos, favicons, images) live at the repo root and in `assets/`. Club documents (constitution, strategic plans) are in `doc/`. Audio files are in `videos/`.

## Configuration Notes

`_config.yml` key settings:

- `theme: minima`
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-paginate, jekyll-sitemap, jekyll-github-metadata
- Navigation order: `header_pages`
- Social links: `minima.social_links` (footer) and `social.links` (SEO/structured data)

Custom styling lives in `assets/main.scss`, which overrides Minima's `$brand-color` before importing the theme. SEO/JSON-LD structured data is in `_includes/custom-head.html`.

## Branding

`branding/index.md` is the canonical brand guide (served at `/branding/`). It documents the colour palette (Royal Blue `#013087` / Pantone 286 C, White, Mid Blue `#1F4DA8`, Light Blue `#C8D6F0`) and typography (DIN / Helvetica Neue family). When changing site styling, align with this doc — the SCSS variables in `assets/main.scss` (`$mkfc-blue`, `$mkfc-mid-blue`, `$mkfc-light-blue`) mirror it.
