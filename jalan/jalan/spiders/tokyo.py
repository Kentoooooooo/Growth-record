# -*- coding: utf-8 -*-
import scrapy
from jalan.items import JalanItem


class TokyoSpider(scrapy.Spider):
    name = 'tokyo'
    allowed_domains = ['www.jalan.net']
    start_urls = [
        'https://www.jalan.net/kankou/130000/page_1/?screenId=OUW1701&influxKbn=0']

    def parse(self, response):
        names = response.xpath(
            '//*[@id="cassetteType"]/li/div/div[2]/p[1]/a/text()').extract()
        reviewCounts = response.xpath(
            '//*[@id="cassetteType"]/li/div/div[2]/div[3]/span[3]/a/text()').extract()
        ratings = response.xpath(
            '//*[@id="cassetteType"]/li/div/div[2]/div[3]/span[2]/text()').extract()
        items = zip(names, reviewCounts, ratings)
        for item in items:
            inputItem = JalanItem()
            inputItem['name'] = item[0]
            rev = item[1].replace("口コミ", '').replace('件', '').replace(',', '')
            inputItem['reviewCount'] = int(rev)
            inputItem['rating'] = float(item[2])

            print(inputItem)
            yield inputItem

        next_page = response.xpath(
            '//*[@id="rankList"]/div[5]/div/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
