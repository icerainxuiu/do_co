from day6_web.v3.utils_po import DriverUtils


class BasePage(object):
    # 定义对象层基类，剥离除浏览器驱动对象
    # 封装初始化方法，创建浏览器驱动实例
    def __init__(self):
        self.driver = DriverUtils.get_driver()

    # 定义浏览器驱动寻找元素的方法，并返回找到的元素
    # location 传递的是一个元组，驱动器寻找对象需要两个对象
    # 所以加 * 拆包传传递
    def find_element(self, location):
        return self.driver.find_element(*location)


class BaseHandle(object):
    # 定义操作层基类，封装清除输入框
    # 以及输入文本方法
    # 传递的两个参数未元素对象和要输入的文本
    # @staticmethod
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

