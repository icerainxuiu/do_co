# 商品搜索页
from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


# 商品搜索页对象
class GoodsPage(BasePage):
    def __init__(self):
        super().__init__()

        # 搜索输入框和搜索的商品
        self.search_input = (By.XPATH, '//div[@class="shop_name2"]/a[contains(text(), "{}")]')

    # 在搜索页查找搜索到的商品
    def find_search_goods(self, kw):

        return self.find_element((self.search_input[0], self.search_input[1].format(kw)))


# 操作搜索框
class GoodsHandle(BaseHandler):

    def __init__(self):
        self.page = GoodsPage()

    # 点击搜索框的搜索按钮
    def click_search_goods(self, kw):
        self.click_element(self.page.find_search_goods(kw))


# 搜索指定商品业务，搜索关键字由调用该方法的对象提供
class GoodsProxy(object):
    def __init__(self):
        self.handle = GoodsHandle()

    def search_proxy(self, kw):
        self.handle.click_search_goods(kw)
