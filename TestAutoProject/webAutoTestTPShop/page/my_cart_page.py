# 我的购物车页面
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


# 对象库层
from page.login_page import LoginProxy
from page.my_account_page import MyAccountProxy
from utils.utils import DriverUtil


class CartPage(BasePage):
    def __init__(self):
        super().__init__()

        self.order_pay = (By.XPATH, '//a[contains(text(), "去结算")]')
        self.all_check = (By.XPATH, "//input[@class='checkCart checkCartAll']")

    # 查找全选按钮
    def find_all_check(self):
        return self.find_element(self.all_check)

    # 查找去结算按钮
    def find_order_pay_bt(self):
        return self.find_element(self.order_pay)


# 操作层
class CartHandler(BaseHandler):

    def __init__(self):
        self.cart_page = CartPage()

    # 点击全选按钮
    def click_all_checked(self):
        self.click_checkbox(self.cart_page.find_all_check())

    # 点击 去结算按钮
    def click_order_pay_bt(self):
        self.click_element(self.cart_page.find_order_pay_bt())


# 购物车页的业务
class CartProxy(object):
    def __init__(self):
        self.handler = CartHandler()

    # 点击全选按钮
    #
    def order_pay_proxy(self):
        # 点击全选按钮
        self.handler.click_all_checked()
        # 点击去结算按钮
        self.handler.click_order_pay_bt()


if __name__ == '__main__':
    class Test(unittest.TestCase):
        @classmethod
        def setUpClass(cls) -> None:
            cls.driver = DriverUtil.get_driver()
            cls.proxy = CartProxy()
            cls.account = MyAccountProxy()
            cls.login = LoginProxy()

        def setUp(self) -> None:
            pass

        def test_cart(self):
            self.driver.get('http://localhost')
            self.driver.find_element_by_class_name('red').click()
            self.login.login_proxy('18828828888', '123456', '8888')
            time.sleep(8)
            self.account.click_my_account_proxy()
            time.sleep(2)
            # self.driver.get('http://localhost/Home/Cart/index.html')
            self.proxy.click_all_check_proxy()
            time.sleep(2)
