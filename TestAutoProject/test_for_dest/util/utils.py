from selenium import webdriver

# 创建驱动对象工具类


class DriverUtil(object):
    # 定义驱动对象初始属性
    _driver = None

    # 定义获取驱动对象方法，判断驱动对象是否已获取
    # 将其设置为类方法
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20)
        return cls._driver

    # 设置退出浏览器驱动方法
    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None


def get_tips_msg():
    return DriverUtil.get_driver().find_element_by_class_name("layui-layer-content").text