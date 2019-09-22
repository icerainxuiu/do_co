import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")

ActionChains(driver).move_to_element(driver.find_element_by_tag_name("button")).perform()
time.sleep(5)
driver.quit()
