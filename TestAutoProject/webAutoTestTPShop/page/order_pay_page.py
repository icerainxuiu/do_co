# 订单支付页

# 对象库层
import time

from selenium.webdriver.common.by import By

from base.basePage import BasePage, BaseHandler


class OrderPayPage(BasePage):
    def __init__(self):
        super().__init__()

        self.tips = (By.XPATH, '//div[@class="erhuh"]/h3')

    # 获取提示信息
    def find_tips(self):
        return self.find_element(self.tips)


# 操作层
# 获取对应对象的文本信息
class OrderPayHandler(BaseHandler):
    def __init__(self):
        self.page = OrderPayPage()

    # 获取文本信息
    def get_text(self):
        return self.page.find_tips().text


# 业务层，判断获取到的文本信息和预期是否一致
class OrderPayProxy(object):
    def __init__(self):
        self.handler = OrderPayHandler()

    # 获取消息和预期判断
    def is_success(self):
        return self.handler.get_text()
        # time.sleep(3)
        # print(self.handler.get_text())
        # return expect in self.handler.get_text()


if __name__ == '__main__':
    pass