# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class NbaPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host='localhost', user='root', password='', database='myweb')
        cursor = db.cursor()
        sql = f"""insert into NBA(球员姓名, 时间, 篮板, 助攻, 得分)values("{item['name']}", "{item['time']}", "{item['backboard']}", "{item['assist']}", "{item['score']}")"""
        cursor.execute(sql)
        db.commit()#需要提交，要不然没存进去！
        return item
