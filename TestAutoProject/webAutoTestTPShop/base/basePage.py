import time

from selenium.webdriver.common.by import By




# 页面对象基类
from webAutoTestTPShop.utils.utils import DriverUtil


class BasePage(object):
    def __init__(self):
        # 获取浏览器驱动对象实例
        self.driver = DriverUtil.get_driver()

    def find_element(self, location):
        # 返回获取到的元素
        return self.driver.find_element(location[0], location[1])

    def check(self):
        self.driver.find_element(By.ID, 'name').get_attribute('checkbox')

# 操作类基类


class BaseHandler(object):
    # 输入文本的方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

    # 点击按键的方法
    def click_element(self, element):
        element.click()

    # 点击checkbox方法
    def click_checkbox(self, element):
        time.sleep(1)
        if element.is_selected():
            return None
        else:
            element.click()
