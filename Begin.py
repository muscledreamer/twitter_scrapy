#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/6 0006 19:37
# @Author  : Sz
from scrapy import cmdline

cmdline.execute("scrapy crawl twitter_info_start".split())
# cmdline.execute("scrapy crawl twitter_content_start".split())
# cmdline.execute("scrapy crawl weiboSpider".split())
# cmdline.execute("scrapy crawl articleSpider".split())
# cmdline.execute("scrapy crawl relateSpider".split())
