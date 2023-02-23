# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:46:39 2023

@author: Ines
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time

url="https://www.omio.fr/"

options=webdriver.ChromeOptions()
options.add_argument('headless')

from selenium.webdriver.chrome.service import Service
service = Service("./chromedriver")
browser = webdriver.Chrome(service=service, options=options)
browser.get(url)

time.sleep(3)


