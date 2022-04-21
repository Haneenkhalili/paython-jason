from multiprocessing.connection import wait
from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json


s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('https://mijnoctrooi.rvo.nl/fo-eregister-view/search')

driver.implicitly_wait(5)

element = driver.find_element(By.ID, "patent")
element.click()

check = driver.find_element(By.ID, "SPC")
check.click()

# search = driver.find_element(By.ID,'submitBtn')
# search.click()


f = open('data.json') 

data = json.load(f)

div= driver.find_element(By.ID,'number')
search1=div.find_element(By.ID,'number')
element_list=[]
try:
    for i in data:

        div= driver.find_element(By.ID,'number')
        search1=div.find_element(By.ID,'number')
        search1.send_keys(i)
        butn = driver.find_element(By.ID,'submitBtn')
        butn.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            pup = (i).text

        except:
            pup=""

        try:
            pro = driver.find_element(By.XPATH,'//*[@id="Main"]/p/strong[2]').text
        except:
            pro = ""

        try:
            base = driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[1]/dd[4]/a').text
        except:
            base=""
        
        try:
            name = driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[31]/dd').text
        except:
            name = ""

        try:
            status = driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[1]/dd[5]').text
        except: 
            status=""

        try:
            filing = driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[27]/dd[1]').text
        except:
            filing =""

        try: 
            start=driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[28]/dd[1]').text
        except:
            start= ""

        try:
            expiriy =driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[28]/dd[3]').text
        except:
            expiriy=""

        try:
            markiting=driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[19]/dd[1]').text
        except:
            markiting=""

        try:
            auth =driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[4]/dd[1]').text
        except:
            auth =""
        
        try:
            extention =driver.find_element(By.XPATH,'//*[@id="tt"]/div[2]/div[1]/div/dl[8]/dd[2]').text
        except:
            extention = ""
        element_list.append({
        "puplication number":pup,
        "Product Name":pro,
        "Base patent number":base,
        "patent name":name,
        "Status":status,
        "SPC filing date":filing ,
        "SPC Start date":start,
        "SPC expiriy date":expiriy,
        "Marketing authorization number":markiting,
        "Date of marketing authorization":auth,
        "extention date /normal":extention
        })
        jsonString = json.dumps(element_list)
        jsonFile = open("array.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()  
        time.sleep(2)
       
        
        driver.get('https://mijnoctrooi.rvo.nl/fo-eregister-view/search')
        element = driver.find_element(By.ID, "patent")
        element.click()

        check = driver.find_element(By.ID, "SPC")
        check.click()
        div= driver.find_element(By.ID,'number')
        search1=div.find_element(By.ID,'number')

      
                

except:
    time.sleep(5)