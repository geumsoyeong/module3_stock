# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NaverscraperItem(scrapy.Item):
    stock_rank = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    # ratio_updown = scrapy.Field()
    # ratio = scrapy.Field()
    low = scrapy.Field()
    volume = scrapy.Field()
    payment = scrapy.Field()
    buy = scrapy.Field()
    sell = scrapy.Field()
    capitalization = scrapy.Field()
    per = scrapy.Field()
    roe = scrapy.Field()



    # define the fields for your item here like:
    # name = scrapy.Field()
    
