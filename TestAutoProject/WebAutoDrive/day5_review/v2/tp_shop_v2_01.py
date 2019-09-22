"""
v2 使用unittest 框架 编写测试用例，一个py文件可以是多个测试用例
减少了代码的冗余，方便生成测试报告，提供了丰富的断言方法
"""
import unittest

from selenium import webdriver


class TestLogin(unittest.TestCase):
    # 初始化类的方法，封装多个测试用例的开始准备条件
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://localhost")

    # 销毁类的时候，退出浏览器驱动
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 初始化方法固件
    def setUp(self) -> None:
        self.driver.get("http://localhost")

    # 测试登录模块账号不存在的情况，并断言提示信息
    def test_login_username_error(self):
        self.driver.find_element_by_css_selector(".red").click()
        self.driver.find_element_by_id("username").send_keys("14423331234")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_name("verify_code").send_keys("8888")
        # 点击登录按钮，获取错误提示信息
        self.driver.find_element_by_xpath("//a[contains(text(), '登')]").click()
        msg = self.driver.find_element_by_xpath("//div[contains(text(), '账号')]").text
        print('msg=', msg)
        self.assertIn('账号不存在', msg)

    # 测试登录模块密码错误的情况，并断言提示信息
    def test_login_password_error(self):
        self.driver.find_element_by_css_selector(".red").click()
        self.driver.find_element_by_id("username").send_keys("18828828888")
        self.driver.find_element_by_id("password").send_keys("12345116")
        self.driver.find_element_by_name("verify_code").send_keys("8888")
        # 点击登录按钮，获取错误提示信息
        self.driver.find_element_by_xpath("//a[contains(text(), '登')]").click()
        # msg = driver.find_element_by_xpath("//div[contains(text(), '账号')]").text
        msg = self.driver.find_element_by_class_name("layui-layer-content").text
        print('msg', msg)
        self.assertIn('密码错误', msg)