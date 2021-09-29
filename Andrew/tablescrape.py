#listing dependencies
from bs4 import BeautifulSoup as bs
import pymongo
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)

    table_url = "https://www.bls.gov/oes/current/oes_nat.htm"
    
    tablehtml = pd.read_html(table_url)
# https://download.bls.gov/pub/time.series/wm/wm.area
# https://download.bls.gov/pub/time.series/wm/wm.occupation
# https://www.bls.gov/help/hlpforma.htm#WM

    tableraw = tablehtml[0]
    tableraw = tableraw.drop([0, 1041])
    tableraw = tableraw.rename(columns = {"Occupation title (click on the occupation title to view its profile)": "Occupation"})
    filteredtable = tableraw.loc[:, ['Occupation', 'Employment', 'Employment per 1,000 jobs', 'Annual mean wage']]

   
    table = filteredtable.to_html(index = False)

    wagedict = {
        "Table" : table
    }
    browser.quit()
    return wagedict
    


