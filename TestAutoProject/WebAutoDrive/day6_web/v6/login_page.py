# coding:utf-8
from selenium.webdriver.common.by import By

from day6_web.v6.base_lg import BasePage, BaseHandle


class LoginPage(BasePage):
    # 封装对象库层，继承自对象库层基类，
    # 设置初始化属性，调用父类的初始化方法获取浏览器驱动对象
    # 设置初始化属性及查找元素的使用的查找类型和值
    def __init__(self):
        # 由驱动对象工具创建浏览器驱动对象
        super().__init__()
        self.username = (By.ID, 'username')
        self.password = (By.ID, 'password')
        self.verify_code = (By.ID, 'verify_code')
        self.sbt = (By.NAME, 'sbtbutton')

    def find_username(self):
        # 找登录框元素的方法并返回找到的登录框元素
        return self.find_element(self.username)

    def find_password(self):
        # 找密码输入框元素的方法并返回找到的密码输入框元素
        return self.find_element(self.password)

    def find_verify_code(self):
        # 找验证码输入框并返回
        return self.find_element(self.verify_code)

    def find_sbt(self):
        # 找登录按钮元素并返回
        return self.find_element(self.sbt)


class LoginHandle(BaseHandle):
    # 封装操作层
    # 实例化对象，并封装对象的操作方法
    def __init__(self):
        self.handle = LoginPage()

    # 调用父类的输入文本框方法
    def input_username(self, username):
        self.input_text(self.handle.find_username(), username)

    # 操作密码框
    def input_password(self, password):
        self.input_text(self.handle.find_password(), password)
    # 操作验证码框

    def input_verify_code(self, verify_code):
        self.input_text(self.handle.find_verify_code(), verify_code)
    # 操作登录按钮

    def click_sbt(self):
        self.handle.find_sbt().click()


class LoginProxy(object):
    # 封装业务层
    # 实例化操作对象，封装登录业务
    def __init__(self):
        self.login_proxy = LoginHandle()

    # 登录业务的输入用户名，密码，验证码，并点击登录按钮
    def login_user_pass(self, username, password, verify_code):
        self.login_proxy.input_username(username)
        self.login_proxy.input_password(password)
        self.login_proxy.input_verify_code(verify_code)
        self.login_proxy.click_sbt()
