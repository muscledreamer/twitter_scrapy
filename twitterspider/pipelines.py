# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from items import information_ScrapyItem,content_ScrapyItem

class information_Pipeline(object):
    def __init__(self):
        self.db = MySQLdb.connect(
            host ='192.168.120.5',
            port = 3306,
            user='root',
            passwd='asd123',
            db ='twitter',
            charset='utf8'
            )
        self.cursor=self.db.cursor()

    def process_item(self, item, spider):
        if isinstance(item,information_ScrapyItem):
            nick = item['nick']
            name = item['name']
            info = item['info']
            place = item['place']
            href = item['href']
            time = item['time']
            page_num = item['page']
            see_others_num = item['see_others']
            fans_num = item['fans']
            check_sql = 'select name from twitter_info where nick = "%s"'%nick
            self.cursor.execute(check_sql)
            datas = self.cursor.fetchall()
            if datas:
                print "%s are inserted"%name
            else:
                sql = 'insert into twitter_info (nick,name,info,place,href,time,page_num,see_others_num,fans_num) ' \
                      'value ("%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(nick,name,info,place,href,time,page_num,see_others_num,fans_num)
                print sql
                self.cursor.execute(sql)
                self.db.commit()
            return item
        if isinstance(item,content_ScrapyItem):
            id = item['twitter_id']
            author = item['twitter_author']
            content = item['twitter_content']
            href = item['twitter_href']
            time = item['twitter_time']
            reply = item['twitter_reply']
            trunsmit = item['twitter_trunsmit']
            zan = item['twitter_zan']
            img = item['twitter_img']
            check_sql = 'select href from twitter_content where twitter_id = "%s"' % id
            self.cursor.execute(check_sql)
            datas = self.cursor.fetchall()
            if datas:
                print "%s are inserted" % id
            else:
                sql = 'insert into twitter_content (twitter_id,author,content,href,time,reply,trunsmit,zan,img) ' \
                      'value ("%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                    id,author,content, href, time, reply, trunsmit, zan, img)
                print sql
                self.cursor.execute(sql)
                self.db.commit()
            return item