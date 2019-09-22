#
# 创建注册页面对象层，操作层，及注册业务
# 注册层对象继承自BasePage基类，拥有其查找元素对象的方法
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage, BaseHandler


class RegisterPageObject(BasePage):
    """
    对象库层
    """
    # 定义初始化方法，重写父类的初始化方法，并增加实例对象属性

    def __init__(self):
        # 获取父类初始化获取浏览器驱动对象
        super().__init__()

        # 注册框用户名查找的方法类型和值
        self.username = (By.ID, 'username')
        # 验证码框
        self.verify_code = (By.ID, 'verify_code')
        # 密码框
        self.password = (By.ID, 'password')
        # 确认密码框
        self.password2 = (By.ID, 'password2')
        # 推荐人电话框
        self.reference_tel = (By.ID, 'reference')
        # 同意条件并注册按钮
        self.sbt = (By.ID, 'sbtbutton')

    # 使用父类的查找元素的方法
    # 查找用户名
    def find_username(self):
        return self.find_element(self.username)

    # 查找密码框
    def find_password(self):
        return self.find_element(self.password)

    # 查找验证码
    def find_verify_code(self):
        return self.find_element(self.verify_code)

    # 查找确认密码框
    def find_password2(self):
        return self.find_element(self.password2)

    # 查找推荐人手机号输入框
    def find_reference_tel(self):
        return self.find_element(self.reference_tel)

    # 查找确认按钮
    def find_sbt(self):
        return self.find_element(self.sbt)


class RegisterHandler(BaseHandler):
    # 操作库层继承自操作基类，拥有其输入文本的方法
    # 初始化属性，拥有对象元素实例
    def __init__(self):
        self.handler = RegisterPageObject()

    # 使用父类输入文本的方法输入用户名
    def input_username(self, username):
        self.input_text(self.handler.find_username(), username)

    # 输入验证码
    def input_verify_code(self, verify_code):
        self.input_text(self.handler.find_verify_code(), verify_code)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.handler.find_password(), password)

    # 输入确认密码
    def input_password2(self, password2):
        self.input_text(self.handler.find_password2(), password2)

    # 输入推荐人手机
    def input_reference_tel(self, reference_tel):
        self.input_text(self.handler.find_reference_tel(), reference_tel)

    # 点击确认注册按钮
    def click_sbt(self):
        self.handler.find_sbt().click()


# 业务层，注册功能业务
class RegisterProxy(object):
    # 初始化操作层实例对象
    def __init__(self):
        self.proxy = RegisterHandler()

    # 注册业务的方法
    def register(
            self,
            username,
            password,
            password2,
            verify_code,
            reference_tel=None):
        self.proxy.input_username(username)
        self.proxy.input_password(password)
        self.proxy.input_password2(password2)
        self.proxy.input_verify_code(verify_code)
        self.proxy.input_reference_tel(reference_tel)
        self.proxy.click_sbt()
