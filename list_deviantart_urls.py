#!/usr/bin/env python3
"""
List all artwork URLs from a DeviantArt gallery.

Usage:
    python list_deviantart_urls.py onojk123 > deviantart_urls.txt
"""

import sys
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_GALLERY_URL = "https://www.deviantart.com/{username}/gallery/?page={page}"

# Change this if you want to be extra polite
REQUEST_DELAY_SECONDS = 2.0

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; DeviantArtURLCollector/1.0)"
}


def fetch_gallery_page(username: str, page: int) -> str | None:
    url = BASE_GALLERY_URL.format(username=username, page=page)
    resp = requests.get(url, headers=HEADERS, timeout=15)
    if resp.status_code != 200:
        print(f"# Stopping: got status {resp.status_code} for {url}", file=sys.stderr)
        return None
    return resp.text


def extract_artwork_urls(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    urls: list[str] = []

    # DeviantArt gallery thumbnails are usually links to /username/art/Title-123456789
    # We grab all <a> tags that look like art links.
    for a in soup.find_all("a", href=True):
        href = a["href"]

        # Skip non-art URLs
        if "/art/" not in href:
            continue

        # Skip things like /prints/ etc if needed
        if "/prints/" in href:
            continue

        # Ensure full URL
        full_url = urljoin("https://www.deviantart.com", href)
        if full_url not in urls:
            urls.append(full_url)

    return urls


def crawl_gallery(username: str) -> list[str]:
    all_urls: list[str] = []
    page = 1

    while True:
        print(f"# Fetching page {page}...", file=sys.stderr)
        html = fetch_gallery_page(username, page)
        if not html:
            break

        urls = extract_artwork_urls(html)
        if not urls:
            print(f"# No artwork URLs found on page {page}, stopping.", file=sys.stderr)
            break

        # Avoid duplicates across pages
        new_urls = [u for u in urls if u not in all_urls]
        if not new_urls:
            print(f"# Page {page} contained only duplicates, stopping.", file=sys.stderr)
            break

        all_urls.extend(new_urls)

        page += 1
        time.sleep(REQUEST_DELAY_SECONDS)

    return all_urls


def main():
    if len(sys.argv) != 2:
        print("Usage: python list_deviantart_urls.py <username>", file=sys.stderr)
        sys.exit(1)

    username = sys.argv[1].strip()
    urls = crawl_gallery(username)

    # Print one URL per line to stdout
    for url in urls:
        print(url)

    print(f"# Collected {len(urls)} artwork URLs.", file=sys.stderr)


if __name__ == "__main__":
    main()
