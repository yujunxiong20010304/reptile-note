# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    photot_name = scrapy.Field()

class DetailItem(scrapy.Item):
    detail = scrapy.Field()
