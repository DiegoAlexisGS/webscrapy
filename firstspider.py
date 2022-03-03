ans#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:50:24 2019

@author: diego

scrapy.spyder.Spider just one webpage
scrapy.spyder.CrawlSpider several webpages

Se ejecuta con consola y estando en el directorio utilizamos el siguiente código
scrapy runspider nombre_del_archivo -o nombre_del_archivo_a_guardar -t tipo_del_archivo
"""

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

#Problem: Extrac information from StackOverflow: Questions
class Pregunta(Item):
    pregunta=Field()
    id=Field()
    
class StackOverflowSpider(Spider):
   name = "Mi primer spider"
   start_urls = ['https://math.stackexchange.com/']
   
   def parse(self,response):
       sel=Selector(response)
       preguntas=sel.xpath('//div[@id="question-mini-list"]/div/div')   #xpath o css 
       
       #Iterar sobre all questions 
       for i,elem in enumerate(preguntas):
           item = ItemLoader(Pregunta(),elem)
           #item.add_xpath('pregunta','.//h3/a/text()')
           item.add_value('id',i)
           yield item.load_item()
          
          
