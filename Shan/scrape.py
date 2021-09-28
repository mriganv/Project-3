import os
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    url="https://www.cnbc.com/jobs/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    result=soup.find_all('div',class_='Card-titleContainer')
    img=soup.find('img',class_='Card-mediaContainerInner')['src']
    latest=result[0].find('div').text
    return{'Title':latest,'Image':img}