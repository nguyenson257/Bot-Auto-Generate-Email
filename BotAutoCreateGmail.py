from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service

import time
import numpy as np
import csv
import pandas as pd
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True,)
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# edge_options = Options()
# edge_options.add_argument("--remote-debugging-port=9222") 
# edge_options.add_experimental_option('useAutomationExtension', False) 
# edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])

url = "https://accounts.google.com/signup"
header = ('LastName', 'FirstName', 'Email', 'Password', 'Error', 'Status')
csv_filename = 'Information.csv'

with open(csv_filename) as f:
    reader = csv.reader(f)
    next(reader, None)
    lst = list(reader)
array = np.array(lst, dtype='object')


# driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=chrome_options)
# driver = webdriver.Edge(executable_path="msedgedriver.exe",capabilities=edge_options.to_capabilities())

ser = Service("msedgedriver.exe")  # Here you specify the path of Edge WebDriver
driver = webdriver.Edge(service = ser)
driver.maximize_window()
for i in (range(array.shape[1]-1)):   
    driver.get(url)
    time.sleep(1)
    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys(array[i][0])
    first_name = driver.find_element(By.NAME, "firstName")
    first_name.send_keys(array[i][1])
    gmail = driver.find_element(By.NAME, "Username")
    gmail.send_keys(array[i][2])
    passw = driver.find_element(By.NAME, "Passwd")
    passw.send_keys(array[i][3])
    pass_cfm = driver.find_element(By.NAME, "ConfirmPasswd")
    pass_cfm.send_keys(array[i][3])
    next_btn = driver.find_elements(By.XPATH, "//*[@class='VfPpkd-vQzf8d']")
    next_btn[1].click()
    time.sleep(1)
    try:
        
        error1 = driver.find_element(By.XPATH, "//*[@id='nameError']/div[2]/span")
        array[i][4] = array[i][4] + error1.text + " \n"
    except Exception as inst:
        print(inst) 
    try:
        error2 = driver.find_element(By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div")
        array[i][4] = array[i][4] + error2.text + " \n"
    except Exception as inst:
        print(inst) 
    try:
        error3 = driver.find_element(By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[2]/div[2]/span")
        array[i][4] = array[i][4] + error3.text + " \n"
    except Exception as inst:
        print(inst) 
    if array[i][4] =="":
        array[i][5] = 1
    
    time.sleep(1)
pd.DataFrame(array).to_csv('result.csv',index=False,header=header,sep ='\t', encoding='utf-16')
time.sleep(1)



