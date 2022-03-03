#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:42:07 2019

@author: diego
"""

import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()

#html parsing
page_soup=soup(page_html,"html.parser")

#grabs each 
containers = page_soup.findAll("div",{"class":"item-container"})
filename="products.csv"
f=open(filename,"w")

headers="brand,product_name,shipping\n"
f.write(headers)

for container in containers:
    brand=container.select('div>a')[1].img["alt"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_name=title_container[0].text
    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping=shipping_container[0].text.strip()
    
    
    print("Product Name "+product_name)
    print("Shipping"+shipping)
    print("Brand:"+brand)
    f.write(brand+","+product_name.replace(",","|")+","+shipping+"\n")
f.close()    
    