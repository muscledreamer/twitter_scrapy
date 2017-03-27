# -*- coding: utf-8 -*-
# author: Bo jingqian email: jqian_bo@126.com

import os
import time


def coding():
    now_time = time.strftime("%H-%M-%S",time.localtime(time.time()))
    print now_time
    cmd = "python Begin.py"
    print "爬虫启动"
    os.system(cmd)
    print "爬虫结束"
    time.sleep(3)

if __name__ == '__main__':
    try:
        while True:
            coding()
            now_time = time.strftime("%H-%M-%S",time.localtime(time.time()))
            if now_time == "23-00-00":
                print "%sSTOP"%now_time
                break
    except KeyboardInterrupt:
        print('Bye~')