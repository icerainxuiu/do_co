# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时

import unittest

import time


def myadd(a, b):
    return a + b


# 定义setUpModule方法--模块级别Fixture -- 模块中所有测试方法-执行前自动执行


# 定义tearDownModule方法--模块级别Fixture -- 模块中所有测试方法-执行后自动执行



# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture0(unittest.TestCase):

    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")

class TestFixture1(unittest.TestCase):

    # 定义测试方法 --- 方法名必须是test开头
    def test_11(self):
        print("test_11")

    def test_12(self):
        print("test_12")
