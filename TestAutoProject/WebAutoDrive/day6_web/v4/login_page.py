# coding:utf-8

from day6_web.v3.utils_po import DriverUtils


class LoginPage(object):
    # 封装对象库层
    # 封装找元素的方法
    # 设置初始化属性
    def __init__(self):
        # 由驱动对象工具创建浏览器驱动对象
        self.driver = DriverUtils.get_driver()
        self.username = None
        self.password = None
        self.verify_code = None
        self.sbt = None

    def find_username(self):
        # 找登录名
        return self.driver.find_element_by_id('username')

    def find_password(self):
        # 找密码
        return self.driver.find_element_by_id('password')

    def find_verify_code(self):
        # 找验证码
        return self.driver.find_element_by_id('verify_code')

    def find_sbt(self):
        # 找登录按钮
        return self.driver.find_element_by_name('sbtbutton')


class LoginHandle(object):
    # 封装操作层
    # 实例化对象，并封装对象的操作方法
    def __init__(self):
        self.handle = LoginPage()

    # 操作登录框
    def input_username(self, username):
        self.handle.find_username().send_keys(username)

    # 操作密码框
    def input_password(self, password):
        self.handle.find_password().send_keys(password)

    # 操作验证码框
    def input_verify_code(self, verify_code):
        self.handle.find_verify_code().send_keys(verify_code)

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
