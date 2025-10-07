# scrape.py
import requests
from bs4 import BeautifulSoup
import json

OUT = "data/docs_raw.txt"

def fetch(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    parts = []
    for tag in soup.select('h1,h2,h3,p,li'):
        txt = tag.get_text(separator=' ', strip=True)
        if txt:
            parts.append(txt)
    return parts

def main():
    url = "https://docs.capillarytech.com/"  # Change if needed
    html = fetch(url)
    parts = extract_text(html)
    os.makedirs("data", exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        for p in parts:
            f.write(p + "\n")
    print(f"Saved {len(parts)} text parts to {OUT}")

if __name__ == '__main__':
    import os
    main()
