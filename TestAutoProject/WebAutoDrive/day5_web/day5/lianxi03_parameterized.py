# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时

import unittest

import time

from parameterized import parameterized


def myadd(a, b):
    return a + b


def data_list():
    return [(0, 1, 1), (1, 2, 3), (4, 4, 8)]


# 定义测试类  ---  必须继承unittest.TestCase
class TestMyadd(unittest.TestCase):
    # 定义测试方法 --- 方法名必须是test开头
    # def test_myadd1(self):
    #     # 1,1  预期  2
    #     result = myadd(1, 1)
    #     print("result: ", result)
    #     self.assertEqual(2, result)
    #
    # def test_myadd2(self):
    #     # 1,0  预期  1
    #     result = myadd(1, 0)
    #     print("result: ", result)
    #     self.assertEqual(1, result)
    #
    # def test_myadd3(self):
    #     # 0,0  预期  0
    #     result = myadd(0, 0)
    #     print("result: ", result)
    #     self.assertEqual(0, result)

    # def test_myadd(self):
    #     # 通过循环实现
    #     # 执行结果之后一个
    #     # 中间出错停止执行
    #     test_data = [(1, 1, 2), (1, 0, 1), (0, 0, 0)]
    #     for x, y, expect in test_data:
    #         result = myadd(x, y)
    #         print("result: ", result)
    #         self.assertEqual(expect, result)

    # 第一种 -- 直接数据写入参数化方法
    # @parameterized.expand([(1, 1, 2), (1, 0, 1), (0, 0, 0)])
    # def test_myadd_param01(self, x, y, expect):
    #     print("x={}, y={}, expect={}".format(x, y, expect))
    #     result = myadd(x, y)
    #     self.assertEqual(expect, result)

    # 第二种 -- 通过变量保存测试数据
    # test_data = [(1, 1, 2), (1, 0, 1), (0, 0, 0)]
    #
    # @parameterized.expand(test_data)
    # def test_myadd_param02(self, x, y, expect):
    #     print("x={}, y={}, expect={}".format(x, y, expect))
    #     result = myadd(x, y)
    #     self.assertEqual(expect, result)

    # 第三种 -- 通过方法返回测试数据--定义返回数据的方法
    @parameterized.expand(data_list)
    def test_myadd2(self, x, y, expect):
        # 1,0  预期  1
        result = myadd(x, y)
        print("result: ", result)
        self.assertEqual(expect, result)
