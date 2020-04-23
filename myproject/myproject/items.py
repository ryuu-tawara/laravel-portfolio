# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Weather_Item(scrapy.Item):
    """
    お天気情報
    """
    time = scrapy.Field()
    city = scrapy.Field()
    hight_t = scrapy.Field()
    low_t = scrapy.Field()
    zero_six = scrapy.Field()
    six_twelve = scrapy.Field()
    twelve_eighteenth = scrapy.Field()
    eighteenth_zero = scrapy.Field()
