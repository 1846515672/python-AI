# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaItem(scrapy.Item):
    name = scrapy.Field()
    time = scrapy.Field()
    backboard = scrapy.Field()
    assist = scrapy.Field()
    score = scrapy.Field()
