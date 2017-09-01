import scrapy
from scrapy_splash import SplashRequest
import logging

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://app.wrh.net.br/site/lmurray/vagas']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 3})

    def parse(self, response):
        html = response.body
        logging.info(html)
