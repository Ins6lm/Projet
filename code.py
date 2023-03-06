# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:13:22 2023

@author: Ines
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import re
from selenium.webdriver.common.keys import Keys

def trip(Destination,Depart,Return):

dep_string = "03 March 2023"
dep_obj = datetime.strptime(dep_string, "%d %B %Y")
Depart = datetime.strftime(dep_obj, "%b %#d, %Y")
print(Depart)
ret_string = "05 March 2023"
ret_obj = datetime.strptime(ret_string, "%d %B %Y")
Return = datetime.strftime(ret_obj, "%b %#d, %Y")

Destination='London'

url="https://www.rome2rio.com/"


browser=webdriver.Chrome()
browser.get(url)

time.sleep(5)

#---------accepter les cookies----------

browser.find_element(By.XPATH,'//*[@id="alert-banner"]/div[2]/a').click()

#---------aller dans ticket---------

#browser.find_element(By.XPATH, '//*[@id="button-tickets"]').click()

#---------décocher les hotels---------

browser.find_element(By.XPATH, '//*[@id="label_search_hotels"]').click()

#####---------Lancer la recherche-----------

##Strasbourg

search_stras = browser.find_element(By.XPATH,'//*[@id="search-from"]')
search_stras.clear()
search_stras.send_keys("Strasbourg")
search_stras.send_keys(Keys.RETURN)

##Destination

search_Destination = browser.find_element(By.XPATH,'//*[@id="search-to"]')
search_Destination.clear()
search_Destination.send_keys(Destination)
search_Destination.send_keys(Keys.RETURN)

##Depart

#search_depart=browser.find_element(By.XPATH, '//*[@id="tab-tickets"]/div[2]/div[2]/div[1]/a/span[1]')
#search_depart.send_keys('Depart')
#search_depart.send_keys(Keys.RETURN)

##Return

#search_return=browser.find_element(By.XPATH, '//*[@id="tab-tickets"]/div[2]/div[2]/div[2]/a/span[1]')
#search_return.clear()
#search_return.send_keys('Return')
#search_return.send_keys(Keys.RETURN)

##Search

search=browser.find_element(By.XPATH, '//*[@id="transport-search"]/span[2]').click()

###----------Récupération des résultats------------------

#soup = BeautifulSoup(browser.page_source,'html.parser')

##Nbrésultat##----------------Se débarasser des options drive

ways=browser.find_elements(By.CLASS_NAME,'sc-3enhc-4 kcnpEo')
print(ways)



#count = len(soup.find_all('(^)class="sc-1i17y0o-0 bdLgJQ"'))
p#rint(count)

##Options 

#ways = re.findall('<h1 class="sc-1i17y0o-4 djVajZ">(.*?)</h1>',str(soup))

#print(ways)

##Récup les durées des trajets

#time=browser.find_element(By.XPATH,"//*[@id="main"]/div[1]/div[1]/div/div/div/div[1]/a[2]/div[2]/div[1]/time").text

#price=re.findall('<span>(.*?)</span>',str(soup))


##classer les colonnes et faire un tableau

#-------------choix du trajet---------

Pr=(Fastest, Cheapest, Comfiest)

