import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("file:///C:/Users/icerain/Desktop/page/drag.html")
ActionChains(driver).drag_and_drop(driver.find_element_by_id("div1"),driver.find_element_by_id("div2")).perform()
time.sleep(3)

driver.quit()
