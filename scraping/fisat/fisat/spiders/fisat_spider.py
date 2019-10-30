# -*- coding: utf-8 -*-
import scrapy
from ..items import FisatItem


class FisatSpySpider(scrapy.Spider):
    name = 'fisat'
    allowed_domains = ['www.fisat.ac.in']
    start_urls = ['http://www.fisat.ac.in/']

    def parse(self, response):
        #data = response.css('a::text,p::text').extract()
        for l in response.css("a::attr('href')"):
            new_url = response.urljoin(l.extract())
            yield scrapy.Request(new_url,callback=self.parse_url)

    def parse_url(self,response):
        itm=FisatItem()
        itm['data']= response.css('a::text,p::text').extract()
        yield itm

        
