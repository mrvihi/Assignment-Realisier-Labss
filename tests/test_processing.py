from processing.cleaning import clean_text, clean_price, clean_rating
from processing.deduplication import deduplicate

def test_clean_text():
    assert clean_text("  Hello   World ") == "Hello World"

def test_clean_price():
    assert clean_price("£51.99") == 51.99

def test_clean_rating():
    assert clean_rating(5) == 5
    assert clean_rating(7) == ""

def test_deduplicate():
    records = [
        {"source": "Books", "name_or_title": " Test Book ", "author": ""},
        {"source": "Books", "name_or_title": "test book", "author": ""}
    ]
    unique, duplicates = deduplicate(records)
    assert len(unique) == 1
    assert len(duplicates) == 1
