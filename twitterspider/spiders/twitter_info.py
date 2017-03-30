# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
import re
from twitterspider.spiderman import Spider_Aim
from scrapy import Request
from scrapy import Selector
from scrapy.spiders import CrawlSpider
from twitterspider.items import information_ScrapyItem


class Twitter_Spider(CrawlSpider):
    name = "twitter_info_start"

    def start_requests(self):
        url = "https://twitter.com/%s"%Spider_Aim
        yield Request(url=url, callback=self.parse0)

    def parse0(self, response):
        information = information_ScrapyItem()
        selector_demo = Selector(response)
        nick_xpath = "//a[@class='ProfileHeaderCard-nameLink u-textInheritColor js-nav']/text()"
        nick_list = selector_demo.xpath(nick_xpath).extract()
        if len(nick_list) > 0:
            nick = nick_list[0]
            print nick
            information['nick'] = nick
        else:
            information['nick'] = ''
            print "NO nick"
        name_xpath = "//span[@class='u-linkComplex-target']/text()"
        name_xpath_2 = "//b[@class='u-linkComplex-target']/text()"
        name_list = selector_demo.xpath(name_xpath).extract()
        name_list_2 = selector_demo.xpath(name_xpath_2).extract()
        if len(name_list) > 0:
            name = "@"+name_list[0]
            print name
            information['name'] = name
        elif len(name_list_2) > 0:
            name = "@" + name_list_2[0]
            print name
            information['name'] = name
        else:
            information['name'] = ''
            print "NO name"
        info_xpath = "//p[@class='ProfileHeaderCard-bio u-dir']/text()"
        info_list = selector_demo.xpath(info_xpath).extract()
        if len(info_list) > 0:
            info = info_list[0]
            print info
            information['info'] = info
        else:
            information['info'] = ''
            print "NO info"
        place_xpath = "//span[@class='ProfileHeaderCard-locationText u-dir']/text()"
        place_list = selector_demo.xpath(place_xpath).extract()
        if len(place_list) > 0:
            place = place_list[0].replace("\n","").replace(" ","")
            print place
            information['place'] = place
        else:
            information['place'] = ''
            print "NO info"
        href_xpath = "//a[@class='u-textUserColor']/@title"
        href_list = selector_demo.xpath(href_xpath).extract()
        if len(href_list) > 0:
            href = href_list[0]
            print href
            information['href'] = href
        else:
            information['href'] = ''
            print "NO href"
        time_xpath = "//span[@class='ProfileHeaderCard-joinDateText js-tooltip u-dir']/text()"
        time_list = selector_demo.xpath(time_xpath).extract()
        if len(time_list) > 0:
            time = time_list[0]
            print time
            information['time'] = time
        else:
            information['time'] = ''
            print "NO time"
        num_xpath = "//span[@class='ProfileNav-value']/text()"
        num_list = selector_demo.xpath(num_xpath).extract()
        if len(num_list) > 0:
            page_num = num_list[0]
            see_others_num = num_list[1]
            fans_num = num_list[2]
            print page_num,see_others_num,fans_num
            information['page'] = page_num
            information['see_others'] = see_others_num
            information['fans'] = fans_num
        else:
            print "NO num"

        yield information









