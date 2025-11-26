import time
import scrapy

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumQuotesSpider(scrapy.Spider):
    """Scrape quotes.toscrape.com using Selenium (geckodriver).

    Usage examples:
      - Run without tag: `scrapy crawl seleniumquotes -O out.json`
      - With tag: `scrapy crawl seleniumquotes -a tag=humor -O humor.json`

    Requirements:
      - `selenium` Python package
      - `geckodriver` in your PATH (compatible with your Firefox)
    """

    name = "seleniumquotes"

    def __init__(self, tag=None, headless=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = tag
        # Scrapy passes CLI args as strings; normalize headless
        if isinstance(headless, str):
            self.headless = headless.lower() not in ("false", "0", "no")
        else:
            self.headless = bool(headless)

    def start_requests(self):
        """Use Selenium to drive the browser and yield items to Scrapy.

        This generator opens the page, extracts quotes on each page, clicks
        the "Next" button until there is no next page, and finally quits
        the WebDriver.
        """

        options = Options()
        options.headless = self.headless

        self.logger.info("Starting geckodriver (headless=%s)", self.headless)

        driver = webdriver.Firefox(options=options)

        base = "https://quotes.toscrape.com/"
        if self.tag:
            start_url = f"{base}tag/{self.tag}/"
        else:
            start_url = base

        try:
            driver.get(start_url)
            wait = WebDriverWait(driver, 10)

            while True:
                # wait for quotes to be present
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.quote")))

                quotes = driver.find_elements(By.CSS_SELECTOR, "div.quote")
                for q in quotes:
                    try:
                        text = q.find_element(By.CSS_SELECTOR, "span.text").text
                    except Exception:
                        text = None
                    try:
                        author = q.find_element(By.CSS_SELECTOR, "small.author").text
                    except Exception:
                        author = None
                    try:
                        tags = [t.text for t in q.find_elements(By.CSS_SELECTOR, "div.tags a.tag")]
                    except Exception:
                        tags = []

                    yield {
                        "text": text,
                        "author": author,
                        "tags": tags,
                        "url": driver.current_url,
                    }

                # try to navigate to next page
                try:
                    next_btn = driver.find_element(By.CSS_SELECTOR, "li.next a")
                    # click and wait a short moment for nav
                    next_btn.click()
                    time.sleep(0.8)
                except Exception:
                    # no next page, break the loop
                    break

        finally:
            self.logger.info("Quitting geckodriver")
            try:
                driver.quit()
            except Exception:
                pass
