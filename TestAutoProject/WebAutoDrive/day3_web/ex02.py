"""
2、打开百度首页，完成以下操作：
    1.在搜索框中输入‘python3’，暂停2秒，删除最后的字符‘3’，暂停2秒
    2.在搜索框执行鼠标双击操作，暂停2秒，执行键盘剪切操作，暂停2秒
    3.执行粘贴操作，暂停2秒，清空搜素框中的内容，暂停2秒
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.baidu.com")
element = driver.find_element_by_id("kw")
element.send_keys("python3")
time.sleep(2)
element.send_keys(Keys.BACK_SPACE)
time.sleep(2)
ActionChains(driver).double_click(element).perform()
time.sleep(2)
# element.send_keys(Keys.CONTROL, 'a')
element.send_keys(Keys.CONTROL, "x")
time.sleep(2)
element.send_keys(Keys.CONTROL, "v")
time.sleep(2)
element.clear()
time.sleep(2)
driver.quit()
