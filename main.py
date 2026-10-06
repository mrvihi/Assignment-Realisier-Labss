import csv
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path

from scrapers.books_scraper import scrape_books
from scrapers.quotes_scraper import scrape_quotes
from processing.cleaning import clean_records
from processing.validation import validate_records
from processing.deduplication import deduplicate

OUTPUT = Path("output")
LOGS = Path("logs")
OUTPUT.mkdir(exist_ok=True)
LOGS.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS / "scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def save_csv(records):
    columns = [
        "source", "source_url", "name_or_title", "category", "price",
        "rating", "author", "tags", "description", "availability", "scraped_at"
    ]

    with open(OUTPUT / "final_dataset.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)

def main():
    start = time.time()
    logging.info("Scraping started")

    books = scrape_books()
    quotes = scrape_quotes()

    collected = books + quotes
    logging.info("Collected %s records", len(collected))

    cleaned = clean_records(collected)
    valid, rejected = validate_records(cleaned)
    unique, duplicates = deduplicate(valid)

    scraped_at = datetime.now(timezone.utc).isoformat()
    for record in unique:
        record["scraped_at"] = scraped_at

    save_csv(unique)

    summary = {
        "books_records_collected": len(books),
        "quotes_records_collected": len(quotes),
        "total_records_collected": len(collected),
        "records_after_cleaning": len(cleaned),
        "records_rejected": len(rejected),
        "duplicate_records_detected": len(duplicates),
        "final_record_count": len(unique),
        "execution_time_seconds": round(time.time() - start, 2)
    }

    with open(OUTPUT / "summary_report.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    logging.info("Scraping completed: %s", summary)
    print(json.dumps(summary, indent=4))

if __name__ == "__main__":
    main()
