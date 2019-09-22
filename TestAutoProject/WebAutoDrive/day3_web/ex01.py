"""
1、打开TPshop网站首页，完成以下操作：
    1.依次查看首页展示的一级商品分类，每个分类暂停2秒
    2.查看‘电脑’下的分类信息，暂停2秒，点击三级分类‘手机配件’
    要求：在浏览器窗口最大化的状态下操作，设置隐式等待为10秒。
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://localhost")
time.sleep(2)
items = driver.find_elements_by_xpath("//div[@class='item']")
for item in items:
    ActionChains(driver).move_to_element(item).perform()
    time.sleep(2)
ActionChains(driver).move_to_element(items[1]).perform()
time.sleep(2)
element = driver.find_element_by_xpath("//a[contains(text(), '手机配件')]")
ActionChains(driver).move_to_element(element).perform()
element.click()
time.sleep(5)
driver.quit()