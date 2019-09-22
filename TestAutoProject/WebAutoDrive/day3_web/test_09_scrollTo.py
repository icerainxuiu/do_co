# -*- coding:utf-8 -*-
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("file:///C:/Users/icerain/Desktop/page/注册A.html")
js = "window.scrollTo(0, 10000)"
driver.execute_script(js)
time.sleep(2)
driver.execute_script("window.scrollTo(0,0)")
time.sleep(2)
driver.quit()