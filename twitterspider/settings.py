# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

# Scrapy settings for twitterspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'twitterspider'

SPIDER_MODULES = ['twitterspider.spiders']
NEWSPIDER_MODULE = 'twitterspider.spiders'

DOWNLOADER_MIDDLEWARES = {
    'twitterspider.middleware.ProxyMiddleware': 100,#代理中间件
    'twitterspider.middleware.UserAgentMiddleware': 200,#请求头中间件
    'twitterspider.middleware.CheckMiddleware': 300,#检测爬虫状态码,解决302重定向
}

#数据库管道处理
ITEM_PIPELINES = {
    # 'twitterspider.pipelines.information_Pipeline': 300
}
#代理设置(最好使用墙外代理IP池,可减少重定向次数)
PROXIES = [
    {'ip_port': '127.0.0.1:9999','user_pass':None},
]

DEFAULT_REQUEST_HEADERS = {
    'Referer': "https://www.google.com/"
}
#禁用cookies
COOKIES_ENABLES=False
# SPIDER_MIDDLEWARES = {
# 'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': True,
# }
#Twitter~API
# TWITTER_CONSUMER_KEY        = 'SbouzZVBRKwHUjjxfx2zYjo18'
# TWITTER_CONSUMER_SECRET     = 'NNm6hr0UKOcdHoyoHxPwLzlX3uXcXMKXyyjCcQ9B6ajIoSBJzl'
# TWITTER_ACCESS_TOKEN_KEY    = '839305580153974784-kjyjO3I0xheNK8NmvboSaTM2pn6Z0ts'
# TWITTER_ACCESS_TOKEN_SECRET = 'jJhF8xTgdtVs0lnIq2UDbbP6dS0ASr412IdIRZquwQHHR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'twitterspider (+http://www.yourdomain.com)'

# Obey robots.txt rules

ROBOTSTXT_OBEY = False
#302 Problem
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
# 去重队列的信息
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0
FILTER_BLOCK = 1
FILTER_KEY = 'fb_bloomfilter'
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2  # 间隔时间,两次下载的间隔
RANDOMIZE_DOWNLOAD_DELAY = True  # 开启随机延迟
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'twitterspider.middlewares.TwitterspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'twitterspider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'twitterspider.pipelines.TwitterspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
