import unittest


class MyClass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b


# 可在一个py文件中编写多个自定义测试类，
# 这些自定义测试类必须继承自unittest.TestCase类
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("----setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("----tearDownClass")

    def setUp(self):
        self.a = 3
        self.b = 1
        print("setUp")

    def tearDown(self):
        print("----tearDown")

    def test_sum(self):
        self.assertEqual(MyClass.sum(self.a, self.b), 3, 'test sum fail')

    def test_sub(self):
        self.assertEqual(MyClass.sub(self.a, self.b), 2, 'test sub fail')


if __name__ == '__main__':
    unittest.main()