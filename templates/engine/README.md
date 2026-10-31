# Slide engine

Deterministic HTML to JPG renderer for VZLA Rising carousels (1080 x 1350).

Setup in a fresh workspace:
```
cd templates/engine && npm install && node map.mjs   # fonts (Cormorant Garamond, Inter) and map data
pip install playwright --break-system-packages        # Chrome at /usr/bin/google-chrome
```

- `slides.py`: templates `cover`, `fact`, `vbars`, `venmap`, `margmap`, `listslide`, `hbars_custom` and `render()`.
- `posts.py`: the first week (Nov 2-6, 2026) as worked examples. Copy its pattern for new posts.
- `map.mjs`: projects Venezuela (world-atlas 10m) and point coordinates into `maps.json`. Add new places there.
- `logo.py`: extracts the wordmark variants from the original logo (already done, results in `brand/logo/`).

Photo slides are not rendered: the workspace cannot download photos. They go into Metricool as direct CDN URLs, cropped by the CDN to 4:5:
- Pexels: `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=1080&h=1350&fit=crop`
- Unsplash: `https://images.unsplash.com/<photo-path>?w=1080&h=1350&fit=crop&q=85&fm=jpg`

Designed slides are published from this repo as `https://raw.githubusercontent.com/maffegabry-coder/vzla-rising-instagram-content-media-repository/main/<path>`.
