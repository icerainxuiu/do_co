# coding:utf-8

# 定义测试用例类，及测试用例，断言其注册成功
import json
import time
import unittest

from parameterized import parameterized

from day6_web.v6.ex_day6.base_page.register_page import RegisterProxy
from day6_web.v6.ex_day6.util import DriverUtil, get_msg


# 从json文件读取数据的方法
def build_data():
    data_list = list()
    with open('../data/test_Data.json', encoding='utf-8') as f:
        json_data = json.load(f)
        for register_data in json_data.values():
            data_list.append((register_data.get("username"),
                             register_data.get("verify_code"),
                             register_data.get("password"),
                             register_data.get("password2"),
                             register_data.get("expect")))
    print(data_list)
    return data_list


class TestRegister(unittest.TestCase):
    # 测试用例类执行前的共有操作
    # 将其定义为类方法
    @classmethod
    def setUpClass(cls) -> None:
        # 共有操作有实例化一个驱动对象，
        cls.driver = DriverUtil.get_driver()
        # 实例化业务层操作，业务层的注册操作
        cls.register = RegisterProxy()

    # 测试用例类执行完成后的销毁浏览器对象操作
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    # 用例执行前的准备工作，打开页面首页，点击注册功能
    def setUp(self) -> None:
        self.driver.get('http://localhost')
        self.driver.find_element_by_xpath('//a[contains(text(), "注册")]').click()
        time.sleep(1)

    # 测试用例执行后等待1秒
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(text(), '安全退出')]").click()
        time.sleep(1)

    # 批量注册功能用例, 从json文件中读取数据
    @parameterized.expand(build_data())
    def test_register(self, username, verify_code, password, password2, expect):
        self.register.register_fun(username, verify_code, password, password2)
        time.sleep(1)
        print(get_msg())
        self.assertIn(expect, get_msg())


