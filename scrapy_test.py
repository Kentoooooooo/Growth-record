import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['www.jalan.net']
    start_urls = [
        'https://www.jalan.net/kankou/130000/page_1/?screenId=OUW1701&influxKbn=0']

    def parse(self, response):
        items = []
        cassetteList = response.css('ul.cassetteType')[0]
        item = cassetteList.css('li.item::text').extract_first()
        rating = item.css('span.reviewPoint::text').extract_first()
        print(rating)
