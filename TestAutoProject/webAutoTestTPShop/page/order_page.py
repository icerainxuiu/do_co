# 核对订单页

# 对象层
# 查找 提交订单按钮
from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


class OrderPage(BasePage):
    # 核对订单页的提交订单按钮的属性
    def __init__(self):
        super().__init__()

        self.order_bt = (By.CLASS_NAME, 'Sub-orders')

    def find_order_bt(self):

        return self.find_element(self.order_bt)


# 操作层
class OrderHandler(BaseHandler):
    # 初始化对象库对象
    def __init__(self):
        self.page = OrderPage()

    def click_order_bt(self):
        self.click_element(self.page.find_order_bt())


# 业务层
class OrderProxy(object):

    # 初始化操作层对象
    def __init__(self):
        self.handler = OrderHandler()

    # 点击提交订单按钮业务
    def order_proxy(self):
        self.handler.click_order_bt()

