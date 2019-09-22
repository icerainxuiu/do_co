import unittest

version = 20


# 跳过测试类执行

class TestSkip(unittest.TestCase):

    # 跳过测试方法执行
    @unittest.skip("代码未完成")
    def test01(self):
        print("该测试方法未完成...")

    # 在一定条件下跳过测试方法执行
    @unittest.skipIf(version <= 30, "版本大于30才执行")
    def test02(self):
        print("版本号大于30才需要执行...")

    @unittest.skipIf(version > 30, "版本低于30才执行")
    def test03(self):
        print("test03")
