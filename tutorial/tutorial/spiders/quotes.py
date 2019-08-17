import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.jalan.net']
    start_urls = [
        'https://www.jalan.net/kankou/130000/page_1/?screenId=OUW1701&influxKbn=0']

    def parse(self, response):
        names = response.xpath(
            '//ul//li///div[@class="item-listContents"]//p/a/text()').extract()
        print(names)
