import scrapy


class SodimacClSpider(scrapy.Spider):
    name = 'sodimac.cl'
    allowed_domains = ['sodimac.cl']
    start_urls = ['http://sodimac.cl/']

    def parse(self, response):
        pass
