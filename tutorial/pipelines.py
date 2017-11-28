# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings

from pymongo import MongoClient

import jieba

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class AlertPipeline(object):
    def process_item(self,item,spider):

        jieba.load_userdict(settings['DICT_PATH'])

        tags = list(jieba.cut(item['title']))

        item['tags'] = tags

        return item


class MongoPipeline(object):

    def __init__(self):
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self,item,spider):

        valid = True

        for record in self.collection.find({"title":item['title'],"date":item['date']}):
            if None != record:
                valid = False

        if valid:
            self.collection.insert(dict(item))

        return item