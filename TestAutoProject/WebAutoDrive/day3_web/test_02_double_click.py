import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")
time.sleep(2)
driver.find_element_by_id("userA").send_keys("admin")
ActionChains(driver).double_click(driver.find_element_by_id("userA")).perform()
time.sleep(5)
driver.quit()
