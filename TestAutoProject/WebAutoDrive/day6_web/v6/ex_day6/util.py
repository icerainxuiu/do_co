# coding:utf-8

# 创建测试驱动工具类
from selenium import webdriver


class DriverUtil(object):
    # 设置驱动对象初始值为None
    _driver = None

    # 定义类方法获取驱动对象
    @classmethod
    def get_driver(cls):
        # 判断驱动对象的值，如果是None就创建
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20)

        return cls._driver

    # 定义类方法退出驱动对象
    @classmethod
    def quit_driver(cls):
        # 判断驱动对象的值，非空就退出并重设为空
        if cls._driver:
            cls._driver.quit()
            cls._driver = None


# 定义获取提示消息的方法
def get_msg():
    return DriverUtil.get_driver().\
        find_element_by_class_name('layui-layer-content').text