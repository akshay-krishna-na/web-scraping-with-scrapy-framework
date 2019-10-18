# -*- coding: utf-8 -*-
import scrapy

from ..items import AmazonItem
class MobilesSpider(scrapy.Spider):
    name = 'mobiles'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/s?k=mobile&i=electronics&rh=n%3A1389401031&page=2&qid=1571152671&ref=sr_pg_2']

    def parse(self, response):
	name=response.xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span::text").extract()
	price=response.xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[1]/span[2]/span[2]::text").extract()  
	
	items['name']=name
	items['price']=price
	yield items
