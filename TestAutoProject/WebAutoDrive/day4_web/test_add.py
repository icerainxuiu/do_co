import unittest

import ddt


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


@ddt.ddt
class TestAddSub(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    @ddt.file_data(".\\data.json")
    def test_add(self, value):
        # print(type(value))
        self.a = value[0]
        self.b = value[1]
        self.assertEqual(add(self.a, self.b), value[2], "testadd is fail")

    @ddt.file_data(".\\data.json")
    def test_sub(self, value):
        # print(list(value)[0])
        self.a = value[0]
        self.b = value[1]
        self.assertEqual(sub(self.a, self.b), -1, "testsub is fail")

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()