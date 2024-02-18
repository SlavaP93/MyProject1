import scrapy


class MvideoSpiderSpider(scrapy.Spider):
    name = "mvideo_spider"
    allowed_domains = ["www.mvideo.ru"]
    start_urls = ["http://www.mvideo.ru/"]

    def parse(self, response):
        pass
