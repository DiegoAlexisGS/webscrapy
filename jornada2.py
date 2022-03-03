#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:19:49 2019

@author: diego
"""
from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

start=time.time()
#Codigo para manejar el buscador

chromedriver = "/home/diego/Documentos/chromedriver"
#chromedriver="/home/diego/anaconda3/bin/geckodriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Firefox()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
my_url="https://www.eleconomista.com.mx/buscar/morena#"

driver.get(my_url)
#Create a new csv file
filename="economista_news.csv"
f=open(filename,"w")
#Define headers within the csv file
head="Id|Date|Title|Text|\n"
f.write(head)
#Define my flags and counters
i,flag,loop,top=0,1,0,100
aux=[]

while i<top:
    #print("The number of loop is: ",loop,flag)
    if loop>0:
        for r in range(loop):
            botton=driver.find_element_by_xpath('//*[@title="Buscar más noticias"]')
            driver.execute_script("arguments[0].click();", botton)
            time.sleep(3)
        my_url=driver.current_url
        driver.get(my_url)
        containers=driver.find_elements_by_xpath('//*[@class="entry-box-overlay"]/a[@title]')
        titles=[y.get_attribute("title") for y in containers]
        titles=[l for l in titles if l not in aux]
    else:
        containers=driver.find_elements_by_xpath('//*[@class="entry-box-overlay"]/a[@title]')
        titles=[y.get_attribute("title") for y in containers]
    #print("Longitudes: ", len(titles)," ", len(aux))
        
    for j in titles:
        data_text=""
        texto="//*"+"[@title="+'"'+j+'"'+"]"
        try:
            element=driver.find_element_by_xpath(texto)
        except:
            print("Entro")
            element=driver.find_element_by_xpath(texto)
        #wait = WebDriverWait(driver, 10)
        #result = wait.until(ec.element_selection_state_to_be(element, True))
        driver.execute_script("arguments[0].click();",element)
        my_url=driver.current_url
        driver.get(my_url)
        time.sleep(3)
        date=driver.find_element_by_xpath('//*[@class="article-date"]/time')
        txt=driver.find_elements_by_xpath('//*[@class="entry-body"]/p')
        for k in txt:
            data_text+=k.text+" "
        if len(date.text)<10:        
            time.sleep(5)
            date=driver.find_element_by_xpath('//*[@class="article-date"]/time')
         
        if len(data_text)<25:
            time.sleep(3)
            txt=driver.find_elements_by_xpath('//*[@class="entry-body"]/p')
            for k in txt:
                data_text+=k.text+" "        
        f.write(str(i)+"|"+date.text+"|"+j+"|"+data_text+"|\n")
        print(date.text,len(data_text),i)
        driver.back()
        time.sleep(5)
        my_url=driver.current_url
        driver.get(my_url)
        if loop>0:
            for h in range(loop+1):
                botton=driver.find_element_by_xpath('//*[@title="Buscar más noticias"]')
                driver.execute_script("arguments[0].click();", botton)
                time.sleep(2)
        my_url=driver.current_url
        driver.get(my_url)
        aux.append(j)
        i+=1  
    #Define the number of loop.    
    loop+=1
    driver.refresh()
    #flag=2*loop
    

f.close()
driver.close()
print("This code took :",time.time()-start)    

                
    
            