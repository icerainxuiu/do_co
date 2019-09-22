# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时

import unittest

# 定义测试类  ---  必须继承unittest.TestCase
import time
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def setUp(self):
        # 实例化浏览器驱动对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # 打开页面
        self.driver.get("http://localhost")

    def tearDown(self):
        # 退出浏览器驱动对象
        time.sleep(2)
        self.driver.quit()

    # 定义测试方法 --- 方法名必须是test开头
    def test_login(self):
        # 业务操作
        # a.首页点击登录--进入登录页
        self.driver.find_element_by_link_text("登录").click()
        # b.输入用户名,密码
        self.driver.find_element_by_id("username").send_keys("13012345678")
        self.driver.find_element_by_id("password").send_keys("123456")
        # c.点击登录按钮
        self.driver.find_element_by_css_selector("[name='sbtbutton']").click()
        # d.获取错误信息
        msg = self.driver.find_element_by_class_name("layui-layer-content").text
        print("msg:", msg)
        # 断言是否提示信息是否包含 "验证码不能为空"
        self.assertIn('验证码不能为空', msg)