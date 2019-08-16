# -*- coding: utf-8 -*-
import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['www.jalan.net']
    start_urls = ['http://www.jalan.net/']

    def parse(self, response):
        pass
