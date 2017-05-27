# -*- coding: utf-8 -*-
import scrapy


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['https://www.douyu.com/']
    start_urls = ['http://https://www.douyu.com//']

    def parse(self, response):
        pass
