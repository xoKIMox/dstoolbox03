# DSJob Scraping

## Setup

    uv init --no-workspace # สั่งครั้งแรกครั้งเดียว

    uv add scrapy

## Commands

    uv run scrapy crawl quotes

    uv run scrapy crawl quotes -O quotes.json -a tag=humor

## Selenium spider

To run the Selenium-based spider (uses Firefox + geckodriver):

- Install dependencies:

```bash
pip install selenium
# install geckodriver (macOS Homebrew recommended):
brew install geckodriver
```

- Run the spider:

```bash
# run all pages
scrapy crawl seleniumquotes -O quotes_selenium.json

# run only a specific tag
scrapy crawl seleniumquotes -a tag=humor -O humor_selenium.json
```

Notes:
- Ensure `geckodriver` is on your PATH and is compatible with your Firefox.
- Use `-a headless=False` if you want to watch the browser (e.g. `-a headless=False`).