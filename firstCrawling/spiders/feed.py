# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from firstCrawling.items import TestItem

class FeedSpider(XMLFeedSpider):
    name = 'feed'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator='iternodes'
    itertag='item'
"""
    def parse(self, response):
        pass
"""
    def parse_node(self,response,node):
        self.logger.info('Hi,this is a <%s> node!:%s',self.itertag,''.join(node.extract()))

        item=TestItem()
        item['id']=node.xpath('@id').extract()
        item['name']=node.xpath('name').extract()
        item['description']=node.xpath('description').extract()
        return item
