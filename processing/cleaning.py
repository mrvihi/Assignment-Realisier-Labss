import re
from urllib.parse import urlparse

def clean_text(value):
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()

def clean_price(value):
    if not value:
        return ""
    match = re.search(r"[\d.]+", str(value).replace(",", ""))
    return float(match.group()) if match else ""

def clean_rating(value):
    if value in ("", None):
        return ""
    try:
        rating = int(value)
        return rating if 1 <= rating <= 5 else ""
    except (ValueError, TypeError):
        return ""

def valid_url(value):
    try:
        parsed = urlparse(value)
        return value if parsed.scheme in ("http", "https") and parsed.netloc else ""
    except Exception:
        return ""

def clean_records(records):
    cleaned = []

    for record in records:
        item = {key: clean_text(value) for key, value in record.items()}
        item["price"] = clean_price(item["price"])
        item["rating"] = clean_rating(item["rating"])
        item["source_url"] = valid_url(item["source_url"])

        if item["name_or_title"] and item["source"] and item["source_url"]:
            cleaned.append(item)

    return cleaned
