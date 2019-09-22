# coding:utf-8
# 封装测试用例
# 测试用例1：登录账号不存在
# 测试用例2：登录密码错误
import time
import unittest

import ddt

from day6_web.v3.utils_po import DriverUtils, get_msg
from day6_web.v5.login_page import LoginProxy


@ddt.ddt
class TestLogin(unittest.TestCase):
    driver = None
    # 封装初始化测试用例前的准备工作
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_driver()
        cls.login_proxy = LoginProxy()

    # 封装测试用例类结束后的销毁工作
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()

    # 封装测试用例执行前的工作
    def setUp(self) -> None:
        time.sleep(1)
        self.driver.get('http://localhost')
        time.sleep(1)
        self.driver.find_element_by_css_selector('.red').click()

    # 测试用例1 登录账号不存在
    # def test01_login_no_username(self):
    #     self.login_proxy.login_user_pass('18827828888', '123456', '8888')
    #     msg_text = get_msg()
    #     self.assertIn('账号不存在', msg_text)
    #
    # def test02_login_password_error(self):
    #     self.login_proxy.login_user_pass('18828828888', '1234562', '8888')
    #     msg_text = get_msg()
    #     self.assertIn('密码错误', msg_text)

    def msg(self, m_msg):
        msg_text = get_msg()
        self.assertIn(m_msg, msg_text)

    @ddt.file_data('./data_list.json')
    def test_case(self, data):
        self.login_proxy.login_user_pass(data[0], data[1], data[2])
        time.sleep(1)
        self.msg(data[3])
