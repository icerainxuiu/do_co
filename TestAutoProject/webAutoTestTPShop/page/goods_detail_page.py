from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


# 创建商品详情页对象层
class GoodsDetailPage(BasePage):
    def __init__(self):
        # 获取父类的初始化获取浏览器对象的方法
        super().__init__()
        # 加入购物车元素的属性
        self.join_cart = (By.ID, 'join_cart')
        # 加入成功提示框的属性
        self.join_cart_result = (By.XPATH, '//div[@class="conect-title"]/span')

    # 找加入购物车按钮
    def find_join_cart(self):
        return self.find_element(self.join_cart)

    # 找成功加入购物车提示框
    def find_join_cart_result(self):
        return self.find_element(self.join_cart_result)


# 操纵层
class GoodsDetailHandler(BaseHandler):
    # 创建初始化方法，获取商品详情页对象
    def __init__(self):
        self.goods_page = GoodsDetailPage()

    # 点击加入购物车按钮
    def click_join_cart(self):
        self.click_element(self.goods_page.find_join_cart())

    # 获取成功加入购物车文本
    def get_join_cart_result(self):
        return self.goods_page.find_join_cart_result().text


# 业务层
class GoodsDetailProxy(object):
    def __init__(self):
        self.handler = GoodsDetailHandler()

    # 加入购物车
    def join_cart_proxy(self):
        self.handler.click_join_cart()

    # 判断是否加入成功(提示框信息和预判断是否一致)
    def is_success_result(self, expect):
        return expect == self.handler.get_join_cart_result()
