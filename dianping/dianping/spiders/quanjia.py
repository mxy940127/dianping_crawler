# -*- coding:utf8 -*-
import scrapy
# from scrapy.spider import BaseSpider
from scrapy.selector import Selector
class QuanJiaSpider(scrapy.Spider):
    name = 'quanjia'
    allowed_domains = ['dianping.com']
    start_urls = [
        "https://www.dianping.com/search/keyword/1/0_%E5%85%A8%E5%AE%B6",
    ]

    def parse(self, response):
        # sel = Selector(response)
        # print(sel)
        filename = 'url.txt'
        print(response.body)
        open(filename, 'wb').write(response.body)
