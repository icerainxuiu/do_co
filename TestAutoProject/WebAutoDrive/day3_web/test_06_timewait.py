# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/icerain/Desktop/page/注册A.html")

WebDriverWait(driver, timeout=10, poll_frequency=1).until(lambda x: x.find_element_by_id("userA")).send_keys("admin")
time.sleep(5)
driver.quit()
