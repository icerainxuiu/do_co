# 创建驱动类，初始化浏览器驱动
import time

from selenium import webdriver


class DriverUtil(object):
    # 设置类属性保存浏览器驱动对象
    _driver = None
    # 设置浏览器退出标记，True 就退出，False就关闭
    _auto_quit = True

    # 定义获取浏览器驱动的方法
    # 使用类方法
    @classmethod
    def get_driver(cls):
        # 做判断，如果没有创建就创建
        if cls._driver is None:
            # 创建浏览器驱动对象
            cls._driver = webdriver.Chrome()
            # 最大化窗口
            cls._driver.maximize_window()
            # 设置隐式等待30秒
            cls._driver.implicitly_wait(30)
        # 将获取到的浏览器驱动对象返回
        return cls._driver

    # 定义退出浏览器驱动类方法
    @classmethod
    def quit_driver(cls):
        # 做判断，如果存在就退出并置空
        if cls._auto_quit and cls._driver:
            cls._driver.quit()
            cls._driver = None

    # 封装外部调用_auto_quit 标记接口
    @classmethod
    def set_auto_quit(cls, flag):
        cls._auto_quit = flag


# 封装获取登录失败的提示框
def get_tips_msg():

    return DriverUtil.get_driver().find_element_by_class_name('layue-layer-content').text


# 封装截屏的方法
def screen_shot_to():
    DriverUtil.get_driver().get_screenshot_as_file(
        '../screenshot/{}.png'.format(time.strftime("%Y%m%d%H%M%S")))


# 封装切换iframe标签的方法
def switch_iframe():
    DriverUtil.get_driver().switch_to.frame(
        DriverUtil.get_driver().find_element_by_tag_name("iframe"))
