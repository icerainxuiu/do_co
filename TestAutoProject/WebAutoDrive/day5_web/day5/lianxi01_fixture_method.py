# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时

import unittest

import time


def myadd(a, b):
    return a + b


# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture(unittest.TestCase):
    # 重写父类的setUp方法--方法级别Fixture -- 测试方法-执行前自动执行
    def setUp(self) -> None:
        print("start time:{}".format(time.time()))

    # 重写父类的tearDown方法--方法级别Fixture -- 测试方法-执行后自动执行
    def tearDown(self) -> None:
        print("end time:{}".format(time.time()))

    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("test_01")
        print(myadd(1, 3))
        print("*" * 50)

    def test_02(self):
        print("test_02")
        print(myadd(3, 1))
        print("*" * 50)
