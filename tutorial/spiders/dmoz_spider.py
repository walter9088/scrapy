# -*- coding: utf-8 -*-

import scrapy


from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["most.gov.cn"]
    start_urls = [
        "http://www.most.gov.cn/tztg/"
    ]

    def parse(self, response):

        item = TutorialItem()

        for sel in response.xpath('//td[@class="STYLE30"]'):

            titles = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            date = sel.xpath('text()').extract()

            item['title'] = titles[0]

            item['date'] = date[0]

            item['link'] = link[0]

            yield item



