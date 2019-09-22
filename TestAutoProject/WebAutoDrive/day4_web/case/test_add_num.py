import unittest


def add(a, b):
    return a + b


@unittest.skip("skipping")
class TestAdd(unittest.TestCase):

    def test_add(self):
        result = add(1, 2)
        print(result)
