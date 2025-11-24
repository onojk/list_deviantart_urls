📜 DeviantArt Gallery URL Scraper

A lightweight Python tool to export every artwork URL from a DeviantArt gallery.

This project provides a simple script for collecting all artwork URLs from a DeviantArt user’s public gallery, across every paginated gallery page. It’s useful for:

Backing up your DeviantArt portfolio

Creating link lists for blogs, websites, and stores

Archiving early artworks

Organizing your online portfolio

Migrating your art library to other platforms

It works entirely client-side using public pages — no API keys or login required.

✨ Features

🔍 Scrapes all pages of a DeviantArt gallery

📄 Extracts every /art/ URL automatically

💾 Outputs clean text (one URL per line)

🔒 No authentication, no API required

🟢 Extremely simple to run and modify

🔄 Written to be easily expandable (CSV, JSON, thumbnails, titles, etc.)

📦 Requirements

This scraper uses:

requests

beautifulsoup4

Because Debian/Ubuntu uses PEP 668 “externally managed environments,” you should install dependencies inside a Python virtual environment.

🛠️ Installation
1. Install required system packages
sudo apt install python3-full python3-venv

2. Create a virtual environment
python3 -m venv da-scraper

3. Activate it
source da-scraper/bin/activate

4. Install dependencies
pip install requests beautifulsoup4

🚀 Usage

Run the script with any DeviantArt username:

python list_deviantart_urls.py onojk123


Save output to a file:

python list_deviantart_urls.py onojk123 > deviantart_urls.txt


This will create a text file with one artwork URL per line.

🧩 Script Overview
list_deviantart_urls.py

This script:

Loads each page of a user’s gallery via
https://www.deviantart.com/<username>/gallery/?page=<n>

Extracts valid DeviantArt artwork links (/art/…)

Automatically continues until no new pages remain

Outputs links to stdout for easy redirect to a file

It uses a polite request delay to avoid hammering DeviantArt’s servers.

🧪 Example Output
https://www.deviantart.com/onojk123/art/Abstract-Figure-417369463
https://www.deviantart.com/onojk123/art/Abstract-Baboon-417353712
https://www.deviantart.com/onojk123/art/Good-Day-979731452
https://www.deviantart.com/onojk123/art/Mandala-1-82374192
...

📚 Extending the Script

You can expand this scraper to also pull:

Artwork titles

Descriptions

Date posted

Thumbnail URLs

Folders / categories

Tags

If you want those enhancements, ask and I’ll generate the extended version.

📝 License

MIT License — modify and use freely.

👤 Author

Jonathan Kendall (onojk123)
Digital Artist • Developer • Visual Systems Engineer
https://www.deviantart.com/onojk123
