#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:15:49 2019

@author: diego
"""


import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import os
from urllib.request import Request

#Codigo para manejar el buscador
chromedriver = "/home/diego/Documentos/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
my_url="https://www.eleconomista.com.mx/buscar/morena"

#Codigo qur sirve para manejar el busador
#headers='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
req = Request(url=my_url, headers=headers) 
uClient=uReq(req)
page_html=uClient.read()
uClient.close()
driver.get(my_url)
#driver.find_element_by_class_name("btn").click() 
driver.find_element_by_partial_link_text("Buscar").click() 
driver.find_element_by_partial_link_text('LOS POLÍTICOS').click()

#html parsing
page_soup=soup(page_html,"html.parser")
#grabs each 
containers = page_soup.findAll("div",{"class":"entry-data"})

#código para ejecutar botones
#print(boton)
#driver.find_elements_by_xpath('//*[@id="top"]/nav/ul/li[3]/a')[0]
#driver.find_element_by_class_name("btn").click() 
#dates = page_soup.findAll("div",{"class":""})
#print(containers[8].h3.a)


filename="newseconomista.csv"
f=open(filename,"w")
headers="id|title|text|link|\n"
f.write(headers)
i=0

for container in containers:
    if container.p==None:
        print(i)
        title=""
    else:
        title=container.p.text
    id=i
    texto=container.h3.a.text
    link=container.a["href"]
    i+=1
    #print(container)
    f.write(str(id)+"|"+title+"|"+texto+"|"+link+"\n")
f.close()    