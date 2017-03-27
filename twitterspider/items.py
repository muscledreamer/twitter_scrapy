# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item


class information_ScrapyItem(Item):

    name = scrapy.Field()
    nick = scrapy.Field()
    info = scrapy.Field()
    place = scrapy.Field()
    href = scrapy.Field()
    time = scrapy.Field()
    page = scrapy.Field()
    see_others = scrapy.Field()
    fans = scrapy.Field()

class content_ScrapyItem(Item):

    twitter_id = scrapy.Field()
    twitter_author = scrapy.Field()
    twitter_content = scrapy.Field()
    twitter_href = scrapy.Field()
    twitter_time = scrapy.Field()
    twitter_reply = scrapy.Field()
    twitter_trunsmit = scrapy.Field()
    twitter_zan = scrapy.Field()
    twitter_img = scrapy.Field()