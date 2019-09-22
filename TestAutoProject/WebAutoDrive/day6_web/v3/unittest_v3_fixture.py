# coding:utf-8
"""
封装class级别的fixture
将公共部分的浏览器驱动封装

封装方法级别的fixture
将每个用例的起始位置封装至其中
"""
import time
import unittest

from selenium import webdriver

from day6_web.v3.utils_po import DriverUtils, get_msg


class TestLogin(unittest.TestCase):
    driver = None
    # 封装class级别fixture
    # 类方法加装饰器
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_driver()
    # 销毁时退出浏览器驱动
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()

    # 封装方法的公用部分
    def setUp(self) -> None:
        self.driver.get("http://localhost")
        self.driver.find_element_by_css_selector('.red').click()

    def tearDown(self) -> None:
        # self.driver.close()
        time.sleep(2)

    # 测试用例1，账号不存在
    def test01_no_username(self):
        self.driver.find_element_by_id('username').send_keys('18828827777')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_name('sbtbutton').click()
        time.sleep(1)
        # 调用封装好的获取弹出框提示信息方法
        text_msg = get_msg()
        print('msg=', text_msg)
        self.assertIn('账号不存在', text_msg)
        time.sleep(1)

    # 测试用例2，密码错误
    def test02_password_error(self):
        self.driver.find_element_by_id('username').send_keys('18828828888')
        self.driver.find_element_by_id('password').send_keys('1234561')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_name('sbtbutton').click()
        time.sleep(1)
        # 调用封装好的获取弹出框提示信息方法
        text_msg = get_msg()
        print('msg=', text_msg)
        self.assertIn('密码错误', text_msg)
        time.sleep(1)