import scrapy


class BbcnewsSpider(scrapy.Spider):
    name = "bbcnews"
    allowed_domains = ["youtube.com"]
    start_urls = ["https://youtube.com"]

    def parse(self, response):
        pass
