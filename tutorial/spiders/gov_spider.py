# -*- coding: utf-8 -*-

import scrapy


from tutorial.items import TutorialItem


domain = 'http://www.most.gov.cn/tztg'

class GovSpider(scrapy.Spider):
    name = "gov"
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

            item['title'] = titles[0].strip()

            item['date'] = date[0].strip().lstrip('(').rstrip(')')

            item['link'] = domain +link[0].strip().lstrip('.')

            item['region'] = '国家级'

            item['department'] = '国家科技部'

            yield item



