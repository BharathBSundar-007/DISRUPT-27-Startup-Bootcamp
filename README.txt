Pages captured: 1
Mode: Live Clone
Scope: Entire site (multi-page crawl)
Exported at: 2026-08-23T17:36:05.553Z

Pages:
- https://disrupt26.framer.website  ->  index.html

This is a LIVE clone: all <script> tags were kept and asset URLs were
absolutized, so Framer Motion / scroll / hover animations should run
normally when opened. A watchdog script also actively removes Framer's
"On-Page Editing" button if it tries to re-appear.

IMPORTANT: Chrome blocks ES module scripts (<script type="module">) from
executing over file:// URLs. Framer almost always uses module scripts,
so double-clicking a page will likely show static markup with no
animation. Serve the folder over local HTTP instead:

  python3 -m http.server 8000
  (then open http://localhost:8000/index.html)

A tiny serve.py helper is included for convenience — just run:
  python3 serve.py

Scripts and images still load live from the original site's CDN, so an
internet connection is required when viewing the export.