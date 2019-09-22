# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("file:///C:/Users/icerain/Desktop/page/注册A.html")
element = driver.find_element_by_id("userA")
element.send_keys("admin1")
time.sleep(2)

element.send_keys(Keys.BACK_SPACE)
# ActionChains(driver).double_click(element)
element.send_keys(Keys.CONTROL,'a')
element.send_keys(Keys.CONTROL, 'c')
driver.find_element_by_id("passwordA").send_keys(Keys.CONTROL, 'v')
time.sleep(10)
driver.quit()