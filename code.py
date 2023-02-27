# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:13:22 2023

@author: Ines
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def trip(Destination,Depart,Return):
    

url="https://www.crous-strasbourg.fr/restaurant/resto-u-paul-appell/"


browser=webdriver.Chrome("./chromedriver",options=options)
browser.get('https://www.crous-strasbourg.fr/restaurant/resto-u-paul-appell/')

time.sleep(5)

webdriver.Chrome()

#---------accepter les cookies----------

accept_cookies=driver.find_element(By.XPATH,//*[@id="alert-banner"]/div[2]/a)

driver.execute_script("arguments[0].click();", accept_cookies)


#---------Lancer la recherche-----------


vfgatht
