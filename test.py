# from selenium import webdriver
# import time

# browser = webdriver.Chrome()
# browser.get("https://www.facebook.com/")
# browser.find_element_by_name("email").send_keys("bsse0903@iit.du.ac.bd")
# browser.find_element_by_name("pass").send_keys("rexonmind1062")
# browser.find_element_by_id('loginbutton').click()
import pandas as pd
# time.sleep(5)
# browser.get("https://www.facebook.com/IITSEC.DU")
# time.sleep(60)
# moreComments = browser.find_elements_by_xpath('//a[@class="_4sxc _42ft"]')

# print(len(moreComments))
# print(moreComments)
read_file = pd.read_csv ('data.csv')
read_file.to_excel ('data.xlsx', index = None, header=True)