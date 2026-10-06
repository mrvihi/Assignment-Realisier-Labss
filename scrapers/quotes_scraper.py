import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://quotes.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_quotes():
    records = []
    url = BASE_URL

    while url:
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Quotes page failed: {url} - {e}")
            url = None
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for quote in soup.select("div.quote"):
            try:
                text_tag = quote.select_one("span.text")
                author_tag = quote.select_one("small.author")
                tags = [tag.get_text(strip=True) for tag in quote.select("div.tags a.tag")]

                records.append({
                    "source": "Quotes to Scrape",
                    "source_url": urljoin(url, "/"),
                    "name_or_title": text_tag.get_text(strip=True) if text_tag else "",
                    "category": "",
                    "price": "",
                    "rating": "",
                    "author": author_tag.get_text(strip=True) if author_tag else "",
                    "tags": ", ".join(tags),
                    "description": "",
                    "availability": ""
                })
            except Exception as e:
                print(f"Skipping one quote record: {e}")

        next_link = soup.select_one("li.next a")
        url = urljoin(url, next_link["href"]) if next_link else None

    return records
