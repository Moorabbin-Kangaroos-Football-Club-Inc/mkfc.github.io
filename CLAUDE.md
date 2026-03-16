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
| History | `history/index.md` |
| News | `news/index.md` |
| Players | `players/index.md` |
| Sponsors | `sponsors/index.md` |
| Calendar | `calendar/index.md` |
| Contact | `contact/index.md` |

Static assets (logos, favicons, images) live at the repo root and in `assets/`. Club documents (constitution, strategic plans) are in `doc/`. Audio files are in `videos/`.

## Configuration Notes

`_config.yml` contains legacy configuration from a previous "Epsom Software" / "Beautiful Jekyll" theme that is partially overridden. The active theme is **minima**, but the config still includes Beautiful Jekyll-specific settings (social links, colour variables, background images) that may not all take effect under minima. Key active settings:

- `theme: minima`
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-paginate, jekyll-sitemap, jekyll-github-metadata
- Custom navbar/footer/page background images configured at the bottom of the file

## Branding

`branding.md` contains North Melbourne Kangaroos (AFL) brand guidelines used as reference for the club's visual identity — colours (Royal Blue #003B9B, White, Gold #FFCD00) and typography (DIN / Helvetica Neue family).
