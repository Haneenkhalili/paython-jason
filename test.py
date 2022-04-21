from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC
import time

# PATH ="/usr/local/bin/chromedriver"
# driver= webdriver.Chrome(PATH)
s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)


driver.get('https://www.youtube.com/c/ElzeroInfo/videos')

try:
    itm =WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"contents"))
    )
    links=itm.find_elements_by_tag_name("a")
    for link in links:
        imgs=link.find_elements_by_tag_name("img")
        for img in imgs:
            print(img.get_attribute("src"))

except :
    driver.quit()