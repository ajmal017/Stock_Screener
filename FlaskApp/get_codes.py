# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# driver.get("https://www.screener.in/company/LUPIN/consolidated/")
# print(driver.content())
# # assert "Python" in driver.title
# # elem = driver.find_element_by_name("q")
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# driver.close()

from selenium import webdriver
import pandas as pd
import numpy as np
import csv

stockList = pd.read_csv('data/NIFTY_STOCKS.csv')
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
with open("data/output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(symbols)
