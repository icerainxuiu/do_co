# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("file:///C:/Users/icerain/Desktop/page/注册A.html")
select = Select(driver.find_element_by_id("selectA"))

select.select_by_index(2)
time.sleep(2)
select.select_by_value("sh")
time.sleep(2)
select.select_by_visible_text("A北京")
time.sleep(2)
driver.quit()
