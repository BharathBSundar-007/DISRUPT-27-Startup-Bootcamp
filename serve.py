#!/usr/bin/env python3
"""Tiny local server so module scripts (and therefore animations) can run.
Usage: python3 serve.py [port]   (defaults to 8000)
"""
import http.server, socketserver, sys, webbrowser

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), handler) as httpd:
    url = f"http://localhost:{port}/index.html"
    print(f"Serving at {url}")
    webbrowser.open(url)
    httpd.serve_forever()
