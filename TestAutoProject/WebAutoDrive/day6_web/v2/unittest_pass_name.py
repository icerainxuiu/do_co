# 创建测试类
import time
import unittest

from selenium import webdriver


class TestLogin(unittest.TestCase):
    # 测试类中封装Fixture中
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("http://localhost")

    def tearDown(self) -> None:
        self.driver.quit()

    # 创建测试账号不存在的方法
    # 并断言
    def test_01_no_username(self):
        self.driver.find_element_by_css_selector('.red').click()
        self.driver.find_element_by_id('username').send_keys('18828827777')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_name('sbtbutton').click()
        time.sleep(1)
        text_msg = self.driver.find_element_by_class_name('layui-layer-content').text
        print('msg=', text_msg)
        self.assertIn('账号不存在', text_msg)
        time.sleep(4)

    # 创建测试账号密码错误的方法
    # 并断言
    def test_02_password_error(self):
        self.driver.find_element_by_css_selector('.red').click()
        self.driver.find_element_by_id('username').send_keys('18828828888')
        self.driver.find_element_by_id('password').send_keys('1234561')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_name('sbtbutton').click()
        time.sleep(1)
        text_msg = self.driver.find_element_by_class_name('layui-layer-content').text
        print('msg=', text_msg)
        self.assertIn('密码错误', text_msg)
        time.sleep(4)




