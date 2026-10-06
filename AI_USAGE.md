# AI_USAGE.md

## AI Tool Used
ChatGPT

## Used For
- Understanding the assignment requirements
- Designing the project folder structure
- Creating an initial Requests + BeautifulSoup approach
- Understanding pagination
- Designing cleaning, validation and deduplication functions
- Preparing README documentation
- Preparing test cases

## Representative Prompts
1. "Explain this Python web scraping assignment and give me a simple project structure."
2. "Create a beginner-friendly Requests and BeautifulSoup scraper for Books to Scrape with pagination."
3. "Create a Quotes to Scrape scraper with pagination and common output fields."
4. "Create simple cleaning, validation and deduplication functions for the scraped records."

## AI-Assisted Parts
The initial code structure, scraper functions, processing functions and documentation were AI-assisted.

## Review and Changes
The code was kept intentionally simple and separated into source scrapers and processing modules. The expected fields and pagination logic were reviewed against the assignment requirements.

## Testing and Verification
The project includes basic pytest tests for cleaning, rating conversion and duplicate detection. The complete scraper should be run with:

```bash
python main.py
```

The CSV and JSON output should then be checked for source names, URLs, record counts and valid numeric fields.
