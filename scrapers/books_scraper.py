import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_books():
    records = []
    url = BASE_URL

    while url:
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Books page failed: {url} - {e}")
            url = None
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select("article.product_pod"):
            try:
                title_tag = book.select_one("h3 a")
                price_tag = book.select_one(".price_color")
                availability_tag = book.select_one(".availability")
                rating_tag = book.select_one("p.star-rating")

                rating = ""
                if rating_tag:
                    classes = rating_tag.get("class", [])
                    rating_words = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
                    for word, value in rating_words.items():
                        if word in classes:
                            rating = value
                            break

                records.append({
                    "source": "Books to Scrape",
                    "source_url": urljoin(BASE_URL, title_tag["href"]) if title_tag else "",
                    "name_or_title": title_tag.get("title", "") if title_tag else "",
                    "category": "",
                    "price": price_tag.get_text(strip=True) if price_tag else "",
                    "rating": rating,
                    "author": "",
                    "tags": "",
                    "description": "",
                    "availability": availability_tag.get_text(" ", strip=True) if availability_tag else ""
                })
            except Exception as e:
                print(f"Skipping one book record: {e}")

        next_link = soup.select_one("li.next a")
        url = urljoin(url, next_link["href"]) if next_link else None

    return records
