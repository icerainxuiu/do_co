import time
from selenium import webdriver

"""
2、打开TPshop网站首页，定位‘手机城’链接，并点击
    方法一：使用link_text定位方式来定位元素
    方法二：使用partial_link_text定位方式来定位元素
    方法三：通过使用‘手机’关键字来定位导航菜单中的‘手机城’
"""
driver = webdriver.Chrome()
driver.get("http://localhost")
# driver.find_element_by_link_text("手机城").click()
# time.sleep(10)
# driver.find_element_by_partial_link_text("手机").click()
# time.sleep(10)
driver.find_element_by_xpath("//a[contains(text(),'手机')]").click()
time.sleep(10)
driver.quit()