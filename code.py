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

def trvlCity(Destination, Depart):
    
    ##Mettre la date au bon format
    
    dep_obj = datetime.strptime(Depart, "%d %B %Y")
    Depart = datetime.strftime(dep_obj, "%b %d, %Y")

    url="https://www.rome2rio.com/"
    
    ##Utilisation du webdriver de Selenium

    browser=webdriver.Chrome()
    browser.get(url)

    #---------accepter les cookies----------

    browser.find_element(By.XPATH,'//*[@id="alert-banner"]/div[2]/a').click()

    #---------aller dans ticket---------

    browser.find_element(By.XPATH, '//*[@id="button-tickets"]').click()

    #---------décocher les hotels---------

    browser.find_element(By.XPATH, '//*[@id="label_search_hotels"]').click()

    #####---------Lancer la recherche-----------

    ##Mettre Strasbourg en ville de départ
    
    search_stras = browser.find_element(By.XPATH,'//*[@id="tickets-from"]')
    search_stras.clear()
    search_stras.send_keys("Strasbourg")
    search_stras.send_keys(Keys.RETURN)

    ##Destination

    search_Destination = browser.find_element(By.XPATH,'//*[@id="tickets-to"]')
    search_Destination.clear()
    search_Destination.send_keys(Destination)
    search_Destination.send_keys(Keys.RETURN)

    ##Depart

    search_depart=browser.find_element(By.XPATH, '//*[@id="tab-tickets"]/div[2]/div[2]/div[1]/a/span[1]')
    search_depart.clear()
    search_depart.send_keys('Depart')
    search_depart.send_keys(Keys.RETURN)

    ##Search

    search=browser.find_element(By.XPATH, '//*[@id="transport-search"]/span[2]').click()

###----------Récupération des résultats------------------

###Vol

    Fly=browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[3]/span[2]/div/span').text

    if Fly == 'N/A':
        print("No flight available")
    else:
        browser.find_element(By.XPATH,'').click
        Ftimedep = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[2]/div[1]/div[1]/span').text
        Ftime = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[3]/span/span[1]/span').text
        FItinerary = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[2]/div[2]/span').text
        FPrice = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[2]/div/div[1]/span/span').text 
        print(Ftimedep, Ftime, FItinerary, FPrice)

###Train

        Train=browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]').text

    if Train == 'N/A':
        print("No train available")
    else:
        Ttimedep = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[2]/div/div[1]/span/span').text
        Ttime = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[3]/span/span[1]/span').text
        TItinerary = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[2]/div[2]/span').text
        TPrice = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[2]/div/div[1]/span/span').text 
        print (Ttimedep, Ttime, TItinerary, TPrice)
  
    ###Bus
    
    Bus=browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/span[2]/div/span/span').text
    if Bus =='N/A':
        print("No bus available")
    else:
        browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]')
        timedep = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[2]/div[1]/div[1]/span').text
        time = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[3]/span/span[1]/span').text
        Itinerary = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[1]/div/div[2]/div[2]/span').text
        Price = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/section[2]/div/div[1]/span/span').text 
        print (timedep, time, Itinerary, Price)

####-----Meteo---

    url='https://www.ecosia.org/'

    browser=webdriver.Chrome()
    browser.get(url)

    search_meteo = browser.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/header/div/form/div/div/div[1]/input')
    search_meteo.clear()
    search_meteo.send_keys(Destination,' Meteo')
    search_meteo.send_keys(Keys.RETURN)

    temp=browser.find_element(By.XPATH,'//*[@id="main"]/div[1]/section/div[2]/div[2]/section/div/div/div[2]/div[1]/div[1]/div').text
    temp

    température = f"La température est de {temp}°"
    température
    
    ###On affiche le résultat
    
    print(timedep, time, Itinerary, Price, température)

