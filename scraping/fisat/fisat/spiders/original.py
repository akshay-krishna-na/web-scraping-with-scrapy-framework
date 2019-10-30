# -*- coding: utf-8 -*-
import scrapy


class FisatSpySpider(scrapy.Spider):
    name = 'original'
    allowed_domains = ['www.fisat.ac.in']
    start_urls = ['http://www.fisat.ac.in/']

    def parse(self, response):
        data = response.css('a::text,p::text').extract()
        yield { 'data' : data }
        
