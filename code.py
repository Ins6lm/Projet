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

def trip(Destination,Depart,Return):

dep_string = "Depart"
dep_obj = datetime.strptime(dep_string, "%d %B %Y")
Depart = datetime.strftime(dep_obj, "%b %d, %Y")

ret_string = "Return"
ret_obj = datetime.strptime(ret_string, "%d %B %Y")
Return = datetime.strftime(ret_obj, "%b %d, %Y")


url="https://www.rome2rio.com/"


browser=webdriver.Chrome()
browser.get(url)

time.sleep(5)

#---------accepter les cookies----------

browser.find_element(By.XPATH,'//*[@id="alert-banner"]/div[2]/a').click()

#---------aller dans ticket---------

browser.find_element(By.XPATH, '//*[@id="button-tickets"]').click()

#---------décocher les hotels---------

browser.find_element(By.XPATH, '//*[@id="label_search_hotels"]').click()

#####---------Lancer la recherche-----------

##Strasbourg

search_stras = browser.find_element(By.XPATH,'//*[@id="tickets-from"]')
search_stras.clear()
search_stras.send_keys("Strasbourg")
search_stras.send_keys(Keys.RETURN)

##Destination

search_Destination = browser.find_element(By.XPATH,'//*[@id="tickets-to"]')
search_Destination.clear()
search_Destination.send_keys("Destination")
search_Destination.send_keys(Keys.RETURN)

##Depart

search_depart=browser.find_element(By.XPATH, '//*[@id="tab-tickets"]/div[2]/div[2]/div[1]/a/span[1]')
search_depart.clear()
search_depart.send_keys('Depart')
search_depart.send_keys(Keys.RETURN)

##Return

search_return=browser.find_element(By.XPATH, '//*[@id="tab-tickets"]/div[2]/div[2]/div[2]/a/span[1]')
search_return.clear()
search_return.send_keys('Return')
search_return.send_keys(Keys.RETURN)

##Search

search=browser.find_element(By.XPATH, '//*[@id="ticket-search"]/span[2]').click()

###----------Récupération des résultats------------------

soup = BeautifulSoup(browser,'html.parser')

##Nbrésultat

options=0

options = 0
for i in range(1, 4):
    xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[' + str(i) + ']/span[2]/div/span/span'
    try:
        browser.find_element(By.XPATH, xpath)
        options += 1
    except:
        pass
print(options)



    
Return(options)

trip()

