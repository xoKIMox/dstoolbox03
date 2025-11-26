from pathlib import Path
import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"

    async def start(self):
        url = "https://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = url + "tag/" + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.log(f'กำลังประมวลผลหน้า: {response.url}')
        for div in response.css("div.quote"):
            text = div.css('span.text::text').get()
            author = div.css('small.author::text').get()
            tags = div.css('div.tags a.tag::text').getall()
            yield {
                'text': text,
                'author': author,
                'tags': tags,
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
