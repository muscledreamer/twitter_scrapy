# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
import json
import time as ti
import re
from scrapy import Request
from scrapy import Selector
from scrapy.spiders import CrawlSpider
from twitterspider.items import content_ScrapyItem
from twitterspider.spiderman import Spider_Aim
from twitterspider.Bloomfilter import BloomFilter
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Twitter_Spider(CrawlSpider):
    name = "twitter_content_start"
    bf = BloomFilter()

    def start_requests(self):
        self.spiderman = Spider_Aim
        url_spider = "https://twitter.com/i/profiles/show/%s/timeline/tweets?" \
                    "include_available_features=1&include_entities=1&reset_error_state=false"%self.spiderman
        print "爬虫初始化中..."
        print "URL:%s"%url_spider
        yield Request(url=url_spider, callback=self.parse0)

    def parse0(self, response):
        content_Item = content_ScrapyItem()
        cycle_count = 0
        sites = json.loads(response.body_as_unicode())
        data = sites["items_html"]
        if data == "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n":
            print "The Last Page~"
        else:
            twitter_author = re.compile('data-name="(.+)" data-user-id=').findall(data)[0]
            selector_app = Selector(text=data)
            twitter_group = selector_app.xpath("//li[@class='js-stream-item stream-item stream-item\n']").extract()
            twitter_group_count = len(twitter_group)
            for twitter_personal in twitter_group:
                cycle_count +=1
                selector_content = Selector(text=twitter_personal)
                twitter_id = selector_content.xpath("//li[@class='js-stream-item stream-item stream-item\n']/@data-item-id").extract()
                if len(twitter_id) > 0:
                    id = twitter_id[0]
                    if self.bf.isContains(id):
                        print id+"已存在,进行去重过滤"
                        continue
                    else:
                        self.bf.insert(id)
                        content_Item['twitter_id'] = id
                else:
                    content_Item['twitter_id'] = ''
                twitter_content_whole = ""
                twitter_content_list = selector_content.xpath("//div[@class='js-tweet-text-container']").extract()
                for twitter_content in twitter_content_list:
                    selector_content_text = Selector(text=twitter_content)
                    twitter_content_text = selector_content_text.xpath("//text()").extract()
                    twitter_content_text_num = len(twitter_content_text)
                    for i in xrange(twitter_content_text_num):
                        if twitter_content_text[i] != "  " and twitter_content_text[i] != "\n  ":
                            twitter_content_add = twitter_content_text[i].replace("\n","")
                            twitter_content_whole += twitter_content_add
                twitter_content_whole_trun = twitter_content_whole.replace('"','\\"')
                twitter_href = selector_content.xpath("//small[@class='time']/a/@href").extract()
                twitter_time = selector_content.xpath("//small[@class='time']/a/@title").extract()
                twitter_num = selector_content.xpath("//span[@class='ProfileTweet-actionCountForAria']/text()").extract()
                if len(twitter_num) > 0:
                    twitter_reply = twitter_num[0]
                    twitter_trunsmit = twitter_num[1]
                    twitter_zan = twitter_num[2]
                else:
                    twitter_reply = ''
                    twitter_trunsmit = ''
                    twitter_zan = ''

                twitter_img = selector_content.xpath("//div[@class='AdaptiveMedia-photoContainer js-adaptive-photo ']/@data-image-url").extract()
                print "蜘蛛人出击！目标:%s" % twitter_id
                if len(twitter_author) > 0:
                    author = twitter_author
                    content_Item['twitter_author'] = author
                else:
                    content_Item['twitter_author'] = ''
                if twitter_content_whole:
                    content = twitter_content_whole_trun
                    content_Item['twitter_content'] = content
                else:
                    content_Item['twitter_content'] = ''
                if len(twitter_href) > 0:
                    href = "https://twitter.com%s"%twitter_href[0]
                    content_Item['twitter_href'] = href
                else:
                    content_Item['twitter_href'] = ''
                if len(twitter_time) > 0:
                    time = twitter_time[0]
                    content_Item['twitter_time'] = time
                else:
                    content_Item['twitter_time'] = ''
                if len(twitter_num) > 0:
                    reply = twitter_reply
                    content_Item['twitter_reply'] = reply
                else:
                    content_Item['twitter_reply'] = ''
                if len(twitter_num) > 0:
                    trunsmit = twitter_trunsmit
                    content_Item['twitter_trunsmit'] = trunsmit
                else:
                    content_Item['twitter_trunsmit'] = ''
                if len(twitter_num) > 0:
                    zan = twitter_zan
                    content_Item['twitter_zan'] = zan
                else:
                    content_Item['twitter_zan'] = ''
                if len(twitter_img) == 1:
                    img = twitter_img[0]
                    content_Item['twitter_img'] = img
                elif len(twitter_img) > 1:
                    img_list = []
                    for img in twitter_img:
                        img_list.append(img)
                        content_Item['twitter_img'] = img_list
                else:
                    content_Item['twitter_img'] = ''
                yield content_Item
            if cycle_count == twitter_group_count:
                next_page_id = id
                next_page_url = "https://twitter.com/i/profiles/show/%s/timeline/tweets?" \
                                "include_available_features=1&include_entities=1&max_position=%s" \
                                "&reset_error_state=false"%(self.spiderman,next_page_id)
                print "下一页等待中..."
                print "URL:%s"%next_page_url

                yield Request(url=next_page_url, callback=self.parse0,headers={'Referer': "https://twitter.com/"})
