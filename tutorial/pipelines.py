# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings

from pymongo import MongoClient

from elasticsearch import Elasticsearch

import jieba

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item





class EsPipeline(object):
    def __init__(self):
       self.esclient = Elasticsearch(settings['ES_SERVER'])


    def process_item(self,item,spider):

        ##self.esclient.index(index='test',doc_type='test',body={'title':item['title'],'date':item['date'],'link':item['link'],'tags':item['tags']})


        return item

class MongoPipeline(object):

    def __init__(self):
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

        jieba.load_userdict(settings['DICT_PATH'])

    def process_item(self,item,spider):



        tags = list(jieba.cut(item['title']))

        item['tags'] = tags

        valid = True

        for record in self.collection.find({"title":item['title'],"date":item['date']}):
            if None != record:
                valid = False

        if valid:
            self.collection.insert(dict(item))

        return item