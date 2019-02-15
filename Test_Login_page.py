import time

from selenium import webdriver

driver = webdriver.Safari()
driver.get("file:///Users/abhilash60/Desktop/testhtml.html")
time.sleep(20)
driver.find_element_by_name("uname").send_keys("test")
driver.find_element_by_id("pd").send_keys("Test@123")
driver.find_element_by_id("bt").click()