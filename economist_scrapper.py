#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:42:38 2019

@author: diego
"""
#from urllib.request import urlopen as uReq
#from bs4 import BeautifulSoup as soup
from selenium import webdriver
import os
import time
#from urllib.request import Request


#Codigo para manejar el buscador
chromedriver = "/home/diego/Documentos/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
my_url="https://www.eleconomista.com.mx/buscar/morena#"

#req = Request(url=my_url, headers=headers) 
#uClient=uReq(req)
#page_html=uClient.read()
#uClient.close()
driver.get(my_url)

filename="economista.csv"
f=open(filename,"w")
head="Id|Date|Title|Text|\n"
f.write(head)

#It gets a list with all a elements.
containers=driver.find_elements_by_xpath('//*[@class="entry-box-overlay"]/a[@title]')

titles=[j.get_attribute("title") for j in containers] 
i=0

for j in titles:
    data_text=""
    texto="//*"+"[@title="+'"'+j+'"'+"]"
    element=driver.find_element_by_xpath(texto)
    driver.execute_script("arguments[0].click();", element)
    
    
    #Here we have to add the code to extract aour data.
    my_url=driver.current_url
    driver.get(my_url)
    title=driver.find_element_by_xpath('//*[@class="title"]/h1')
    date=driver.find_element_by_xpath('//time[@class="entry-time"]')
    txt=driver.find_elements_by_xpath('//div[@class="entry-body"]/p')
    #We processing text
    for k in txt:
        data_text+=" "+k.text
        
    f.write(str(i)+"|"+date.text+"|"+title.text+"|"+data_text+"|\n")

    i+=1
    time.sleep(3)
    driver.back()
    time.sleep(10)
    my_url=driver.current_url
    driver.get(my_url)

f.close()
driver.close()


