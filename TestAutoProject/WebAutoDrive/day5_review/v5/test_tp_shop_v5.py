import unittest

from day5_review.v3 import utils
from day5_review.v3.utils import DriverUtil
from day5_review.v4.login_page import LoginProxy


class TestLogin(unittest.TestCase):
    """
    对登录模块的功能进行测试
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        # 打开首页
        self.driver.get("http://localhost")
        # 点击首页的登录链接，进入登录页面
        self.driver.find_element_by_css_selector(".red").click()

    # 账号不存在
    def test_login_username_error(self):
        self.login_proxy.login("13112121212", '111111', '8888')
        # 断言提示信息
        msg = utils.get_tips_msg()
        print('msg=', msg)
        self.assertIn('账号不存在', msg)

    # 密码错误
    def test_login_pwd_error(self):
        self.login_proxy.login('18828828888', '111111', '8888')
        msg = utils.get_tips_msg()
        print('msg', msg)
        self.assertIn('密码错误', msg)
