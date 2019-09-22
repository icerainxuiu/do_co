# coding:utf-8
# 创建浏览器驱动对象工具类
# 定义获取提示信息方法和获取浏览器title方法
from selenium import webdriver


class DriverUtils(object):
    # 设置浏览器驱动初始值
    _driver = None
    # 定义类方法获取浏览器驱动
    @classmethod
    def get_driver(cls):
        # 判断驱动对象是否以获取
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)

        return cls._driver

    # 退出浏览器驱动方法
    @classmethod
    def quit_driver(cls):
        # 判断浏览器驱动对象是否创建，创建了退出，并重置为None
        if cls._driver:
            cls._driver.quit()
            cls._driver = None


# 定义获取提示信息的方法
def get_msg():
    text_msg = DriverUtils.get_driver().find_element_by_class_name('layui-layer-content').text
    return text_msg


def get_title():
    title_msg = DriverUtils.get_driver().title
    return title_msg