from datetime import datetime

import scrapy

from_date = datetime(2017, 5, 1)
to_date = datetime(2017, 8, 31)

class EnsyuSpider(scrapy.Spider):
    name = 'ensyu'
    allowed_domains = ['docs.pyq.jp']
    start_urls = [
        'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
    ]

    def parse(self, response):
        div_item_list = response.css('div.item-list')[0]
        for div_item in div_item_list.css('div.item'):
            # 発売日の取得
            item_release_date = div_item.css('span.item-release-date::text').extract_first()
            item_release_date = item_release_date.strip()
            item_release_date = datetime.strptime(item_release_date, '%Y-%m-%d')
            
            # 2017-05-01 - 2017-08-31 の範囲外であれ処理をスキップ
            if not (from_date <= item_release_date <= to_date):
                continue
            # 商品URLの取得
            item_url = div_item.css('a.item-name::attr(href)').extract_first()
            #item_url = item_url.strip()

            # 商品URLを個別にスクレイピング
            yield scrapy.Request(item_url, callback=self.parse_item_page)

    def parse_item_page(self, response):
        # 商品名の取得
        item_name = response.css('h1.item-name::text').extract_first()
        item_name = item_name.strip()

        # 価格の取得
        item_price = response.css('span.item-price::text').extract_first()
        item_price = item_price.strip()
        item_price = item_price.replace('円', '')
        item_price = item_price.replace(',', '')
        

        # 発売日の取得
        item_release_date = response.css('span.item-release-date::text').extract_first()
        item_release_date = item_release_date.strip()
        # 解析した内容を辞書にする
        item_info = {
            '商品名': item_name,
            '価格': item_price,
            '発売日': item_release_date,
            
        }
        return item_info
