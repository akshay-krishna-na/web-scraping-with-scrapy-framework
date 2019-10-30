# -*- coding: utf-8 -*-
import scrapy
from ..items import FisatItem


class FisatSpySpider(scrapy.Spider):
    name = 'fisat'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/']

    #def __init__(self):
      #  for line in open('./domains.txt', 'r').readlines():
       #     self.allowed_domains.append(line)
        #    self.start_urls.append('http://%s' % line)

    def parse(self, response):
        data1 = response.css('a::text,p::text').extract()
        yield {'home':data1}
        for l in response.css("a::attr('href')"):
            new_url = response.urljoin(l.extract())
            yield scrapy.Request(new_url,callback=self.parse_url)

    def parse_url(self,response):
        itm=FisatItem()
        itm['data']= response.css('a::text,p::text').extract()
        yield itm

        
