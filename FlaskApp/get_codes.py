

from selenium import webdriver
import pandas as pd
import numpy as np
import csv

stockList = pd.read_csv('Data/NIFTY_STOCKS.csv')
symbols = []
for stock in stockList['Symbol']:
    driver = webdriver.Firefox()
    driver.get("https://www.screener.in/company/"+stock+"/consolidated/")
    results = driver.find_elements_by_xpath('//a[@class="btn btn-info"]')
    for result in results:
        # video = result.find_element_by_xpath('a')
        title = result.get_attribute('title')
        url = result.get_attribute('href')
        temp = url.split("/")
        symbols.append([stock, temp[-2]])
        print("{} ({})".format(title, temp[-2]))
    driver.quit()
print(symbols)
with open("Data/output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(symbols)

# temp = pd.read_csv('Data/output.csv')
# temp.columns = ['Name', 'Code']
# temp.to_csv('Data/output.csv')
