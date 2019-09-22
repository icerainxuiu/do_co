# coding:utf-8
from selenium.webdriver.common.by import By

from day6_web.v6.ex_day6.base_page.base_page import BasePage, BaseHandle


# 创建对象层库类，继承自对象基类，并重写父类的初始化方法
# 在初始化方法内，定义元素查找的属性值By.ID 和ID的值等
class PageRegister(BasePage):
    # 初始化方法
    def __init__(self):
        super().__init__()
        self.username = (By.ID, 'username')
        self.password = (By.ID, 'password')
        self.verify_code = (By.NAME, 'verify_code')
        self.password2 = (By.ID, 'password2')
        self.regbtn = (By.CLASS_NAME, 'regbtn')

    # 定义寻找元素的方法，调用父类的查找方法，传递对应的值
    # 并返回找到的元素
    def find_username(self):
        return self.find_element(self.username)

    def find_password(self):
        return self.find_element(self.password)

    def find_password2(self):
        return self.find_element(self.password2)

    def find_verify_code(self):
        return self.find_element(self.verify_code)

    def find_regbtn(self):
        return self.find_element(self.regbtn)


# 创建操作层，继承自操作基层，并实例化对象元素，创建操作方法
class PageHandle(BaseHandle):
    # 初始化方法，实例化对象元素
    def __init__(self):
        self.page_handle = PageRegister()

    # 调用父类的输入文本方法
    def input_username(self, username):
        self.input_text(self.page_handle.find_username(), username)

    def input_password(self, password):
        self.input_text(self.page_handle.find_password(), password)

    def input_password2(self, password2):
        self.input_text(self.page_handle.find_password2(), password2)

    def input_verify_code(self, verify_code):
        self.input_text(self.page_handle.find_verify_code(), verify_code)

    def click_regbtn(self):
        self.page_handle.find_regbtn().click()


# 创建业务层，执行注册功能业务
class RegisterProxy(object):
    # 初始化方法，实例化操作层对象
    def __init__(self):
        self.register_proxy = PageHandle()

    # 注册功能方法
    def register_fun(self, username, verify_code, password, password2):
        self.register_proxy.input_username(username)
        self.register_proxy.input_verify_code(verify_code)
        self.register_proxy.input_password(password)
        self.register_proxy.input_password2(password2)
        self.register_proxy.click_regbtn()

