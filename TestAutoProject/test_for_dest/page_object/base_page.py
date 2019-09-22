# 定义页面对象基类
# 封装初始化方法，获取驱动对象
from util.utils import DriverUtil


class BasePage(object):
    # 初始化方法，获取驱动对象
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    # 封装获取元素对象方法
    def find_element(self, location):
        return self.driver.find_element(location[0], location[1])


# 封装操作基类
# 封装基类的输入文本方法
class BaseHandler(object):

    # 封装输入文本方法
    def input_text(self, element, text):
        # 输入文本前情况
        element.clear()
        element.send_keys(text)