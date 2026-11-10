# Tech Tales With Abhi — Instagram Posts

Source, rendered slides, and publishing packages for [@techtaleswithabhi](https://instagram.com/techtaleswithabhi).
Slide images here are served publicly (via `raw.githubusercontent.com`) so Metricool can schedule them.

## Layout

```
engine/                 Renderer and brand system
  render.py             post.json → 1080×1350 PNG slides
  brand.css             Instagram version of the site's Blueprint Monochrome system
  config.json           Handle, repo URLs, posting time, Metricool brand id, review window
  package.json          Fonts (Space Grotesk, Source Serif 4, IBM Plex Mono)
posts/YYYY/MM/YYYY-MM-DD-slug/
  post.json             Slide content and per-slide theme
  caption.md            Caption, hashtags, alt text, sources
  slides/slide-NN.png   Rendered carousel
drafts/<slug>/           Finished posts not yet published (same structure)
POSTS.md                Index of published posts and drafts
```

## Render a post

```bash
cd engine && npm install && pip install playwright
cd .. && python3 engine/render.py posts/2026/11/2026-11-10-ai-felt-faster/post.json
```

## Visual system

- Greyscale plus one accent: Beacon Blue `#2F5FE8` (`#7C9BF2` on dark).
- Space Grotesk for headlines, Source Serif for body, IBM Plex Mono for labels and technical terms.
- The **Trace Line** runs down the left margin of every slide and fills as the carousel progresses.
- Not used: cream/terracotta palettes, gradients, rounded card grids.

## Content rules

- Practical engineering and delivery, no AI hype, no tool roundups.
- Every factual claim gets a source in `caption.md`. Illustrative examples are labelled as such.
