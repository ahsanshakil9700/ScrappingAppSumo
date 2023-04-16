import scrapy
import json


class AppsumoSpider(scrapy.Spider):
    name = "sumo_spider"
    start_urls = [
        'https://appsumo2-api-cdn.appsumo.com/api/v2/deals/esbrowse/?page=1&per_page=20&include_aggs=true&profile{'
        'average_rating[gte]}=4.9&profile{default_price[gt]}=0&profile{review_count['
        'gte]}=20&sort=recommended&status=current&__cache=a']
    page_count = 1

    def parse(self, response):
        data = json.loads(response.body)
        if data['deals']:
            for product in data['deals']:
                yield {
                    'name': product['public_name'],
                    'description': product['card_description'],
                    'discounted_price': f'${product["price"]}',
                    'original_price': f'${product["original_price"]}',
                    'total_reviews': product['deal_review']['review_count'],
                    'average_ratings': product['deal_review']['average_rating'],
                    'plan_type': product['default_plan']['plan_type']
                }
            self.page_count += 1
            next_url = f"https://appsumo2-api-cdn.appsumo.com/api/v2/deals/esbrowse/?page={self.page_count}&per_page" \
                       f"=20&include_aggs=true&profile{{average_rating[gte]}}=4.9&profile{{default_price[" \
                       f"gt]}}=0&profile{{review_count[gte]}}=20&sort=recommended&status=current&__cache=a"
            yield scrapy.Request(next_url, callback=self.parse)
