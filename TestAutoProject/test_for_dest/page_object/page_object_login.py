# PO封装页面(封装)
# 封装对象库层(登录模块对象)
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage, BaseHandler


class PageObjectLogin(BasePage):
    # 封装登录对象层
    # 重写父类初始化方法
    def __init__(self):
        super().__init__()
        # 查找username
        self.username = (By.ID, 'username')
        # 查找密码
        self.password = (By.ID, 'password')
        # 查找验证码
        self.verify_code = (By.ID, 'verify_code')
        # 查找登录按钮
        self.sbt = (By.NAME, 'sbtbutton')

    # 调用父类的查找元素方法并返回找到的元素
    # 查找用户名
    def find_username(self):
        return self.find_element(self.username)

    # 查找密码
    def find_password(self):
        return self.find_element(self.password)

    # 查找验证码
    def find_verify_code(self):
        return self.find_element(self.verify_code)

    # 查找登录按钮
    def find_sbt(self):
        return self.find_element(self.sbt)


# 封装操作层(操作登录模块)
class LoginHandler(BaseHandler):
    # 定义初始化方法，实例化一个对象
    def __init__(self):
        self.handler = PageObjectLogin()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.handler.find_username(), username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.handler.find_password(), password)

    # 输入验证码
    def input_verify_code(self, verify_code):
        self.input_text(self.handler.find_verify_code(), verify_code)

    # 点击登录按钮
    def click_sbt(self):
        self.handler.find_sbt().click()


# 封装登录业务
class LoginProxy(object):
    def __init__(self):
        self.login_proxy = LoginHandler()

    # 登录业务
    def login(self, username, password, verify_code):
        self.login_proxy.input_username(username)
        self.login_proxy.input_password(password)
        self.login_proxy.input_verify_code(verify_code)
        self.login_proxy.click_sbt()

