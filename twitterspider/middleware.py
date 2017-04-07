# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian


import random
from user_agents import agents
from settings import PROXIES
from spiderman import Spider_Aim
import base64
import time
import re

class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        print agent
        request.headers["User-Agent"] = agent


class CheckMiddleware(object):
    """ 检测状态码,解决302重定向 """

    def process_response(self,request, response, spider):
        response_status = response.status
        response_url = response.url
        response_check_url = response_url.split('/')[2]
        request_url = request.url
        request_url_id = re.compile('max_position=(\d*)').findall(request_url)
        if len(request_url_id) > 0:
            request_id = request_url_id[0]
            request_url = "https://twitter.com/i/profiles/show/%s/timeline/tweets?" \
                                "include_available_features=1&include_entities=1&max_position=%s" \
                                "&reset_error_state=false"%(Spider_Aim,request_id)
        print request_url
        if response_status == 200 and response_check_url == 'twitter.com':
            print "爬虫运行正常"
            return response
        else:
            print "遭遇反爬虫,休息5秒"
            clock = 0
            sleep_time = 5
            while (clock < sleep_time):
                nclock = sleep_time - clock
                print nclock
                time.sleep(1)
                clock += 1
            print '爬虫重新启动中'
            return request.replace(url=request_url)


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            request.meta['proxy'] = "https://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print "**************ProxyMiddleware have pass************" + proxy['ip_port']
        else:
            print "**************ProxyMiddleware no pass************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            print "获取请求头"