# 创建测试用例，测试登录成功
import time
import unittest

from parameterized import parameterized

from config.log_tp_test import logger
from utils.data_list import data_login
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils.utils import DriverUtil, get_tips_msg, screen_shot_to


class TestLogin(unittest.TestCase):
    # 测试用例类的初始化
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        cls.login_proxy = LoginProxy()
        cls.index_proxy = IndexProxy()

    # 测试用例类结束后的收尾
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    # 测试用例的前置条件
    def setUp(self) -> None:
        self.driver.get('http://localhost')
        self.index_proxy.go_to_login_page()

    # 测试用例结束的收尾
    def tearDown(self) -> None:
        time.sleep(2)

    # 编写测试用例
    @parameterized.expand(data_login())
    def test_login(self, username, password, verify_code, is_success, expect):
        # username = "18828828888"
        # password = "123456"
        # verify_code = "8888"
        # is_success = True
        # expect = "我的账户"
        self.login_proxy.login_proxy(username, password, verify_code)
        if is_success:
            time.sleep(2)
            try:
                self.assertIn(expect, self.driver.title)
                logger.info('测试{}成功'.format(username))
            except Exception as e:
                screen_shot_to()
                logger.info('测试失败，断言{}失败'.format(expect))
                raise e
        else:
            time.sleep(1)
            try:
                msg = get_tips_msg()
                self.assertIn(expect, msg)
            except Exception as e:
                screen_shot_to()
                raise e
