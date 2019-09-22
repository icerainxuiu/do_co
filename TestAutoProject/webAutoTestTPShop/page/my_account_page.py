# 我的账户页面


from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


# 对象库层
class MyAccountPage(BasePage):
    # 父类的初始化方法
    def __init__(self):
        super().__init__()

        # 定位我的购物车
        self.my_cart = (By.XPATH, '//a/div/span[contains(text(), "我的购物车")]')

    # 查找我的购物车元素并返回
    def find_my_cart(self):
        return self.find_element(self.my_cart)


# 操作层
class MyAccountHandler(BaseHandler):
    def __init__(self):
        self.my_account_page = MyAccountPage()

    # 点击我的购物车操作
    def click_my_account(self):
        self.click_element(self.my_account_page.find_my_cart())


# 业务层
class MyAccountProxy(object):
    def __init__(self):
        self.my_handler = MyAccountHandler()

    def click_my_account_proxy(self):
        self.my_handler.click_my_account()

