from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


# 封装主页对象库层
class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 查找首页登录按钮
        self.sbt = (By.CLASS_NAME, 'red')
        # 查找搜索框
        self.search = (By.ID, 'q')
        # 查找搜索按钮
        self.search_bt = (By.CLASS_NAME, 'ecsc-search-button')

    def find_sbt(self):
        return self.find_element(self.sbt)

    def find_search(self):
        return self.find_element(self.search)

    def find_search_bt(self):
        return self.find_element(self.search_bt)


# 封装操作层
class IndexHandler(BaseHandler):
    def __init__(self):
        self.index_page = IndexPage()

    # 点击首页左上角的登录按钮
    def click_sbt(self):
        self.click_element(self.index_page.find_sbt())

    # 搜索框输入文本操作
    def input_search(self, text):
        self.input_text(self.index_page.find_search(), text)

    # 点击搜索按钮
    def click_search_bt(self):
        self.click_element(self.index_page.find_search_bt())


# 封装业务层
class IndexProxy(object):

    def __init__(self):
        self.handler = IndexHandler()

    # 去登录页业务
    def go_to_login_page(self):
        self.handler.click_sbt()

    # 完成搜索业务
    def go_click_search(self, text):
        self.handler.input_search(text)
        self.handler.click_search_bt()
