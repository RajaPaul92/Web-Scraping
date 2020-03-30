import scrapy
from ..items import AdcoilItem



class AdcoSpider(scrapy.Spider):
    name = "adco"
    start_urls = [
        'https://www.ad.co.il/car'
    ]

    def parse(self, response):
        items = AdcoilItem()
        car_data = response.css("div.sec-box-container")
        for car in car_data:
            car_name = car_data.css('h6.grid-box-product-title::text').extract()
            car_model = car_data.css('div.grid-box-car-model::text').extract()
            km = car_data.css('div.box-km::text').extract()
            car_like = car_data.css('div.box-car-hand::text').extract()
            car_price = car_data.css('div.box-price::text').extract()

            # yield {
            #     'car_name': car_name,
            #     'car_price' : car_price,
            #     'car_model': car_model,
            #     'car_like': car_like,
            #     'car_km' : km,
            #
            # }
            items['car_name'] = car_name
            items['car_model'] = car_model
            items['car_km'] = km
            items['car_like'] = car_like
            items['car_price'] = car_price
            yield items

