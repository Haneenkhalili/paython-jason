from multiprocessing.connection import wait
from posixpath import split
from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime
import contextlib
import json



s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('https://mijnoctrooi.rvo.nl/fo-eregister-view/search')

driver.implicitly_wait(5)

element = driver.find_element(By.ID, "patent")
element.click()

check = driver.find_element(By.ID, "SPC")
check.click()

selection = driver.find_element(By.CLASS_NAME, "panel-header")
selection.click()

date = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input3"]')
date.send_keys('01/01/1990')

da = driver.find_element(By.XPATH, '//*[@id="_easyui_textbox_input4"]')
da.send_keys('20/04/2022')

search = driver.find_element(By.ID,'submitBtn')
search.click()

time.sleep(5)

select= driver.find_element(By.XPATH,'//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[1]/select')
select.click()
val= driver.find_element(By.XPATH,'//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[1]/select/option[5]')
val.click()

a=[]
number = int(driver.find_element(By.XPATH,'//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[8]/span').text.split()[1])
for i in range(166):
    try:
        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'patent_link')))
        for element in elements:
            a.append(element.text)

        button_link = driver.find_element(By.XPATH, '//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[10]/a')
        button_link.click()
        time.sleep(4)


        jsonString = json.dumps(a)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

    except:
        time.sleep(4)


