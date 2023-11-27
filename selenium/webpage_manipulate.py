#! python

import bs4
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

# d = 'C:\\Users\\Yan Feng\\Documents\\repo\\python_web_scrape_tools\\selenium\\chromedriver.exe'
# s = Service(d)
# chromeOptions = Options()
# # chromeOptions.headless = False
# chromeOptions.add_experimental_option('prefs', {
#     "download.default_directory": "C:/Users/Yan Feng/Documents/repo/python_web_scrape_tools/selenium",
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "plugins.always_open_pdf_externally": True
# })
    # browser = webdriver.Chrome(service=s, options=chromeOptions)
    # browser = webdriver.Chrome(options=chromeOptions)

house_number_list = [9430 + i for i in range(13)]
street_name = 'Carriage Hill St'
tax_list = []
owner_list =[]
above_grade_living_area_list = []
finished_basement_area_list = []



for house_number in house_number_list:
    print(f'get data for {house_number} {street_name}')
    browser = webdriver.Chrome()
    browser.get('https://frederickcountymd.munisselfservice.com/citizens/RealEstate/Default.aspx?mode=new')
    house_number_element = browser.find_element(By.XPATH, '//table[@role="presentation"]/tbody/tr[3]/td/input')
    house_number_element.send_keys(house_number)

    street_name_element = browser.find_element(By.XPATH, '//table[@role="presentation"]/tbody/tr[4]/td/input')
    street_name_element.send_keys(street_name)

    search_element = browser.find_element(By.XPATH, '//table[@role="presentation"]/tbody/tr[8]/td/input')
    search_element.click()

    view_bill_elements = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'View Bill'))
    )
    #view_bill_element = view_bill_elements[-1]
    view_bill_element = browser.find_elements(By.LINK_TEXT, 'View Bill')[-1]
    view_bill_element.click()

    data_table_elements = browser.find_elements(By.XPATH, '//table[@class="datatable nocaption"]//tr')[-1]
    tax_element = data_table_elements.find_elements(By.XPATH, './td')[1]

    tax_list.append(float(tax_element.text.replace('$', '').replace(',', '')))

    view_state_assessment_data_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'View state assessment data'))
    )
    #view_state_assessment_data_element = browser.find_element(By.LINK_TEXT, "View state assessment data")
    view_state_assessment_data_element.click()

    soup = bs4.BeautifulSoup(browser.page_source, "html.parser")
    owner_names_elements = soup.select('table#detailSearch > tbody > tr:nth-child(5) td:nth-child(2) span')
    owner_names = map(lambda x: x.text, owner_names_elements)
    owner_names = list(filter(None, owner_names))
    if len(owner_names) == 1:
        owner = owner_names[0]
    else:
        owner = ';'.join(owner_names)
    
    owner_list.append(owner)

    above_grade_living_area_elem = soup.select('table#detailSearch > tbody > \
        tr:nth-child(11) > td > table > tbody > tr:nth-child(2) > td > span ')
    above_grade_living_area = above_grade_living_area_elem[1].text.replace(',', '')
    above_grade_living_area_list.append(above_grade_living_area) 
    finished_basement_area = above_grade_living_area_elem[2].text.replace(',', '')
    finished_basement_area_list.append(finished_basement_area)

    browser.close()
    
print(tax_list)
print(owner_list)
print(above_grade_living_area_list)
print(finished_basement_area_list)
