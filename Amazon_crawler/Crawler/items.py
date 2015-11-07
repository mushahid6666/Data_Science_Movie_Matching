# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

    # define the fields for your item here like:
    # name = scrapy.Field()
class DmozItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    cost = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    star = scrapy.Field()

