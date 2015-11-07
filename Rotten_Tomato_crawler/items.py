# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

    # define the fields for your item here like:
    # name = scrapy.Field()
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    cost = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    star = scrapy.Field()

class RottanItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    star1 = scrapy.Field()
    star2 = scrapy.Field()
    star3 = scrapy.Field()
    star4 = scrapy.Field()
    star5 = scrapy.Field()
    star6 = scrapy.Field()
    tomatome_rating = scrapy.Field()
    audience_rating = scrapy.Field()
    review1 = scrapy.Field()
    review2 = scrapy.Field()
    review3 = scrapy.Field()
    review4 = scrapy.Field()
    review5 = scrapy.Field()


