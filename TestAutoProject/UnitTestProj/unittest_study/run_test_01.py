import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        # 不可写成 self.seq = range(10),python3 中 range(10) 是一个生成器，而不是列表
        self.seq = [x for x in range(10)]

    def runTest(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = [x for x in range(10)]

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, [x for x in range(10)])
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    unittest.main()

