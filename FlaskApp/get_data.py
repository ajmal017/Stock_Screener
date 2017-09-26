from selenium import webdriver
import pandas as pd
import numpy as np
import os
import xlrd
import csv

# # def csv_from_excel():
# #     wb = xlrd.open_workbook('excel.xlsx')
# #     sh = wb.sheet_by_name('Sheet1')
# #     your_csv_file = open('your_csv_file.csv', 'w')
# #     wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
# #
# #     for rownum in range(sh.nrows):
# #         wr.writerow(sh.row_values(rownum))
# #     your_csv_file.close()
#
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {
#   "download.default_directory": "C:\\Users\\Rajesh Rao\\version_control\\Stock_Screener\\FlaskApp\\Data\\Fundamental_Data",
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })
#
# driver = webdriver.Chrome(chrome_options=options)
# driver.get("https://www.screener.in/login/")
# username = driver.find_element_by_xpath('//input[@name="username"]')
# password = driver.find_element_by_xpath('//input[@name="password"]')
# username.send_keys("rajeshmprao@gmail.com")
# password.send_keys("bakra123")
# driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
#
codes = pd.read_csv('Data/output.csv')
# for ids in codes['Code']:
#     driver.get("https://www.screener.in/excel/"+str(ids)+"/")
#
# # runs the csv_from_excel function:
# # csv_from_excel()
#


SAVE_TO_DIRECTORY = "C:\\Users\\Rajesh Rao\\version_control\\Stock_Screener\\FlaskApp\\Data\\Fundamental_Data"

os.chdir(SAVE_TO_DIRECTORY)
files = filter(os.path.isfile, os.listdir(SAVE_TO_DIRECTORY))
files = [os.path.join(SAVE_TO_DIRECTORY, f) for f in files] # add path to each file
files.sort(key=lambda x: os.path.getmtime(x))
for oldName, newName in zip(files, codes['Name']):
    os.rename(oldName, newName+'.xlsx')
