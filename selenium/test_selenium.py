#! python

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'
driver_path = r"C:\Users\Yan Feng\Documents\repo\python_web_scrape_tools\selenium\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

#navigate to the website
browser.get('https://python.org')
print(browser.title)
# 
search_field = browser.find_element(By.ID, 'id-search-field')
search_field.clear()
search_field.send_keys('Class datatype')

browser.find_element(By.NAME, 'submit').click()
print(browser.title)
print(browser.current_url)