#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:28:19 2019

@author: diego
"""

from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class vehi(Item):
    motor=Field()
    ano=Field()
    cilindrada=Field()
    kilometros=Field()
    
#Hereda de otra clase ya no de Spider ahora de CrawSpider
class mercaCrawler(CrawlSpider):
    name="Mi primer crawer"
    start_urls=["https://vehiculos.mercadolibre.com.mx/motocicletas"]
    allowed_domains=['https://www.mercadolibre.com.mx/']
    
    rules=(
            Rule(LinkExtractor(allow=r'Desde')),
            Rule(LinkExtractor(allow=r'/MLM'),callback='parse_items'),
            )
    
    def parse_items(self,response):
        item=ItemLoader(vehi(),response)
        item.add_xpath('motor','/html/body/main/div[1]/div[1]/div[1]/section[1]/div[1]/div/div/section/ul/li[1]/span/text()')
        item.add_xpath('ano','/html/body/main/div[1]/div[1]/div[1]/section[1]/div[1]/div/div/section/ul/li[5]/span/text()')
        item.add_xpath('cilindrada','/html/body/main/div[1]/div[1]/div[1]/section[1]/div[1]/div/div/section/ul/li[2]/span/text()')
        item.add_xpath('kilometros','/html/body/main/div[1]/div[1]/div[1]/section[1]/div[1]/div/div/section/ul/li[4]/span/text()')
        yield item.load_item()
        
        
    