# -*- coding: utf-8 -*-
import scrapy


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['http://www.xicidaili.com/']
    start_urls = ['http://http://www.xicidaili.com/nn//']

    def parse(self, response):
        pass
