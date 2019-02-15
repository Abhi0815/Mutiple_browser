import time

from selenium import webdriver
browser='safari'
if browser=='chrome':
    driver=webdriver.Chrome()
elif browser=='safari':
    driver=webdriver.Safari()

driver.get("https://www.facebook.com")
time.sleep(20)
driver.find_element_by_name("uname").send_keys("test")
driver.find_element_by_id("pd").send_keys("Test@123")
driver.find_element_by_id("bt").click()