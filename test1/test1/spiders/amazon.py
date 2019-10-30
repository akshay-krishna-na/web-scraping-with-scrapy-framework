# -*- coding: utf-8 -*-
import scrapy
from ..items import Test1Item

class FlipkartSpider(scrapy.Spider):
    
    name = 'amazon'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/gp/site-directory?ref=nav_em_ajax_fail']

    def parse(self, response):
        links = response.css("#shopAllLinks .nav_a::attr(href)").extract()
        
        for i in links:
            new_link='www.amazon.in'+str(i)
            Request(new_link,callback=self.parse_page)
            
    def parse_page(self,response)links:
        item = Test1Item()
        category = response.css('').extract()
        product = response.css('').extract()
        price = response.css('').extract()
        item['category'] = category
        item['name'] = product
        item['price'] = price
        yield item
        next = response.css('').extract()
        if next is not None:
            response.folow(next,callback = self.parse_page)
        yield item

