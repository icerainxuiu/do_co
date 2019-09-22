import unittest


def sub(a, b):
    return a - b


class TestSub(unittest.TestCase):

    def test_sub(self):
        result = sub(1, 2)
        print(result)