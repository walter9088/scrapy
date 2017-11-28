# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    region = scrapy.Field()

    department = scrapy.Field()

    title = scrapy.Field()

    date = scrapy.Field()

    link = scrapy.Field()

    tags = scrapy.Field()



    pass
