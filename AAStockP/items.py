# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AastockpItem(scrapy.Item):
    # define the fields for your item here like:
    title_org = scrapy.Field()
    title_stock = scrapy.Field()
    title_price = scrapy.Field()
    title_rating = scrapy.Field()
    pTime = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pass
