"""
PO是Page Object的缩写，PO模式是自动化测试项目开发实践的最佳设计模式之一。
核心思想是通过对界面元素的封装减少冗余代码，同时在后期维护中，若元素定位发生变化，
只 需要调整页面元素封装的代码，提高测试用例的可维护性、可读性。
PO模式可以把一个页面分为三层，对象库层、操作层、业务层。
对象库层：封装定位元素的方法。
操作层：封装对元素的操作。
业务层：将一个或多个操作组合起来完成一个业务功能。
比如登录：需要输入帐号、密码、点 击登录三个操作。
2.1 引入PO模式的好处
减少冗余代码
业务代码和测试代码被分开，
降低耦合性 维护成本低

"""
# from day5_review.v3 import utils
from day5_review.v3.utils import DriverUtil


class LoginPage(object):
    """
    对象库层
    """
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        # 用户名输入框
        self.username = None
        # 密码
        self.password = None
        # 验证码输入框
        self.verify_code = None
        # 登录按钮
        self.login_button = None
        # 忘记密码
        self.forget_pwd = None

    def find_username(self):
        return self.driver.find_element_by_id("username")

    def find_password(self):
        return self.driver.find_element_by_id("password")

    def find_verify_code(self):
        return self.driver.find_element_by_name("verify_code")

    def find_login_button(self):
        return self.driver.find_element_by_name("sbtbutton")

    def find_forget_pwd(self):
        return self.driver.find_element_by_partial_link_text("忘记密码")


class LoginHandle(object):
    """
    操作层
    """
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        self.login_page.find_password().send_keys(password)

    def input_verify_code(self, verify):
        self.login_page.find_verify_code().send_keys(verify)

    def click_login_button(self):
        self.login_page.find_login_button().click()

    def click_forget_pwd(self):
        self.login_page.find_forget_pwd().click()


class LoginProxy(object):
    """
    业务层
    """
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def login(self, username, password, verify_code):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_verify_code(verify_code)
        self.login_handle.click_login_button()

    # 跳转到忘记密码页面
    def to_forget_pwd_page(self):
        self.login_handle.click_forget_pwd()


