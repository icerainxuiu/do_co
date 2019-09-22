from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


# 登录页对象库
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名
        self.username = (By.ID, 'username')
        # 密码框
        self.password = (By.ID, 'password')
        # 验证码
        self.verify_code = (By.ID, 'verify_code')
        # 登录按钮
        self.sbt = (By.NAME, 'sbtbutton')

    def find_username(self):
        return self.find_element(self.username)

    def find_password(self):
        return self.find_element(self.password)

    def find_verify_code(self):
        return self.find_element(self.verify_code)

    def find_sbt(self):
        return self.find_element(self.sbt)


# 实例化操作层
class LoginHandler(BaseHandler):
    # 初始化方法，实例化对象层对象
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 输入验证码
    def input_verify_code(self, verify_code):
        self.input_text(self.login_page.find_verify_code(), verify_code)

    def click_sbt(self):
        self.click_element(self.login_page.find_sbt())


# 业务层，登录业务
class LoginProxy(object):
    def __init__(self):
        self.handler = LoginHandler()

    # 登录业务
    def login_proxy(self, username, password, verify_code):
        self.handler.input_username(username)
        self.handler.input_password(password)
        self.handler.input_verify_code(verify_code)
        self.handler.click_sbt()
