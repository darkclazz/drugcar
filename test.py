from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")


driver.get("https://172.17.2.45:28081/RTPDService/login.jsf")

driver.find_element_by_id("details-button").click()
driver.find_element_by_id("proceed-link").click()
#driver.implicitly_wait(30)

user_ele=driver.find_element_by_id("userid")
#print(driver.title)
#print(driver.current_url)
#print(user_ele.is_displayed())
#print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_id("password")

#print(user_ele.is_displayed())
#print(user_ele.is_enabled())

user_ele.send_keys("29EH02")
pwd_ele.send_keys("17072529tum")


driver.find_element_by_id("login2").click()

time.sleep(5)

driver.get("https://172.17.2.45:28081/RTPDService/car/car1q010/index.jsf")

#driver.find_element(By.ID, "searchView_opt1").click()


search1 = driver.find_element_by_id("searchView_carDLTView_carNo1")
search2 = driver.find_element_by_id("searchView_carDLTView_carNo2")
search3 = driver.find_element_by_id("searchView_carDLTView_lovTabCarProvince_lovTabCarProvince_input")
search4 = driver.find_element(By.ID, "searchView_carDLTView_gmnFlag_label")
search5 = driver.find_element(By.ID, "searchView_carDLTView_gmnFlag_1")




search1.send_keys("5กฉ")
search2.send_keys("3024")
search3.send_keys("กรุงเทพมหานคร")
search4.click()
search5.click()

time.sleep(5)

driver.find_element_by_name("searchView_searchBtn").click()




#driver.find_element(By.ID, "resultView_dataTableDlt_data").click()







