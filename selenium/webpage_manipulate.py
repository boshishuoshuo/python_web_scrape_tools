#! python

from selenium import webdriver

browser = webdriver.Chrome('')
print(type(browser))
#browser.get('https://inventwithpython.com/')
browser.get('http://www.python.org')
print(browser.title)