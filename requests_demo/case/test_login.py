import unittest

from parameterized import parameterized

from api.login_api import Login
from data_base import data_json


# 创建测试用例类，继承自unittest.TestCase类
class TestLogin(unittest.TestCase):

    # 初始化方法封装，获取登录接口对象
    def setUp(self) -> None:
        self.session = Login()

    # 销毁session对象
    def tearDown(self) -> None:
        self.session.close_login()

    # 测试验证码的用例
    def test01_verify(self):
        # 接收返回的响应
        response = self.session.get_verify_cookie()
        # print(response.headers.get("content-type"))
        # 通过响应头的信息进行断言
        # self.assertEqual('image/png', response.headers.get("content-type"))

    # 测试登录的用例，通过数据文件导入需要测试的数据
    @parameterized.expand(data_json())
    def test02_login(self, username, password, verify_code, msg, status):
        # 先获取验证码cookie
        self.test01_verify()

        # 构造需要输入请求的数据(需要是字典格式)
        my_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        # 接收返回的响应
        response = self.session.login(my_data)
        # print(response.content.decode())
        # 通过响应中的提示信息和状态进行断言
        self.assertEqual(msg, response.json().get("msg"))
        self.assertEqual(status, response.json().get("status"))
