# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdcoilItem(scrapy.Item):
    # define the fields for your item here like:
    car_name = scrapy.Field()
    car_model = scrapy.Field()
    car_km = scrapy.Field()
    car_price = scrapy.Field()
    car_like = scrapy.Field()

