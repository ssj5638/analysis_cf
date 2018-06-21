from selenium import webdriver
import time

wd = webdriver.Chrome('D:/pycharmProject/chromedriver.exe')
wd.get('http://www.google.com')

time.sleep(5)
html = wd.page_source
print(html)


wd.quit()