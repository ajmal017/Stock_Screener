# import pandas as pd
# import numpy as np
# a = pd.read_csv('output.csv')
# a.columns = ['Name', 'Code']
# a.to_csv('codes.csv')
# print(a.head())

from selenium import webdriver
import pandas as pd
import numpy as np
options = webdriver.FirefoxOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:/",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Firefox(FirefoxOptions = options)
driver.get("https://www.screener.in/login/")

username = driver.find_element_by_xpath('//input[@name="username"]')
password = driver.find_element_by_xpath('//input[@name="password"]')

username.send_keys("rajeshmprao@gmail.com")
password.send_keys("bakra123")

driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()

driver.get("https://www.screener.in/excel/2333/")
# driver.get("https://www.google.com")
# a = pd.read_csv('data/codes.csv')
# for id in a['Code']:
