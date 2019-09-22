# coding: utf-8
# 创建对象层基类
from day6_web.v6.ex_day6.util import DriverUtil


class BasePage(object):
    # 初始化并创建驱动对象
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    # 创建驱动查找对象的方法,传递元组参数
    def find_element(self, location):
        return self.driver.find_element(*location)


# 创建操作层基类
class BaseHandle(object):
    # 封装输入文本内容的方法
    # 需要两个参数，一个元素对象，一个要输入的文本
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)