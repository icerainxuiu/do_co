# 定义获取驱动对象的工具类
from selenium import webdriver


class DriverUtil(object):
    """
    浏览器驱动对象工具类
    """
    _driver = None

    @classmethod
    def get_driver(cls):
        """
        获取浏览器驱动对象，并完成初始化
        :return: 浏览器驱动对象
        """
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
            cls._driver.get("http://localhost")
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """
        关闭浏览器驱动对象
        并将浏览器驱动对象重置为None
        :return:
        """
        if cls._driver:
            cls._driver.quit()
            cls._driver = None


# 封装获取弹窗框的提示消息
def get_tips_msg():

    msg = DriverUtil.get_driver().find_element_by_class_name("layui-layer-content").text
    return msg

def get_title():
    title = DriverUtil.get_driver().title
    return title