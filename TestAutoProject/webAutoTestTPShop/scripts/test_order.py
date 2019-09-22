# 测试下订单
import time
import unittest

from config.log_tp_test import logger
from page.login_page import LoginProxy
from page.my_account_page import MyAccountProxy
from page.my_cart_page import CartProxy
from page.order_page import OrderProxy
from page.order_pay_page import OrderPayProxy
from utils.utils import DriverUtil, screen_shot_to


class TestOrder(unittest.TestCase):
    # 设置登录标记位，如果位True就初始化登录模块对象，否则不执行
    _login_flag = True

    # 测试用例执行前，初始化驱动对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        if cls._login_flag:
            cls.login = LoginProxy()
        # 获取购物车对象
        cls.my_account_proxy = MyAccountProxy()
        # 获取核对订单页
        cls.order_proxy = OrderProxy()
        # 购物车页
        cls.cart_proxy = CartProxy()
        # 订单支付页
        cls.order_pay_proxy = OrderPayProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('http://localhost')

    def tearDown(self) -> None:
        time.sleep(2)

    # 设置外部调用接口用以更改登录标记
    @classmethod
    def set_login_flag(cls, flag):
        cls._login_flag = flag

    # 下订单测试
    def test_order(self):
        expect = '订单提交成功，请您尽快付款'
        # 判断登录标记是否为真，是真就执行登录业务
        if self._login_flag:
            self.driver.find_element_by_class_name('red').click()
            self.login.login_proxy("18828828888", '123456', '8888')

        self.my_account_proxy.click_my_account_proxy()
        logger.info('点击我的购物车成功')
        time.sleep(1)

        self.cart_proxy.order_pay_proxy()
        logger.info("进入我的订单页，点击去结算按钮成功")
        time.sleep(3)

        self.order_proxy.order_proxy()
        logger.info("点击提交订单按钮成功")
        # print(self.order_pay_proxy.is_success())

        tips = self.order_pay_proxy.is_success()
        logger.info("获取提交订单提示消息成功")
        result = (expect in tips)

        # print(result)
        try:
            self.assertTrue(result)
            logger.info("断言成功，断言消息在提交订单提示消息内")
        except Exception as e:
        # self.assertTrue(self.order_pay_proxy.is_success(expect))
            logger.info('断言失败，截图保存')
            # 调用封装好的截图方法
            screen_shot_to()