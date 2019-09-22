# 需求，测试购物车接口，但是需要调用登录接口(登录实现比较复杂：需要录入手机号码，以及服务器发送的验证码)
# 实现
# 1. 需要导入unittest
import unittest
from unittest import mock

# 2. 确定被模拟的接口
# 登录函数
# 需要参数：手机号+验证码
# 返回值：True|False


def login():
    return False


class TestCart(unittest.TestCase):
    def test_cart(self):
        # 3. 创建Mock服务
        login = mock.Mock(return_value="我是小叮当")
        # 4. 并且调用mock服务
        result = login()
        if result == "我是小叮当":
            print(result)





