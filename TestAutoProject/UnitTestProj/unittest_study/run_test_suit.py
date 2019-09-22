import HTMLTestRunner
import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.seq = [x for x in range(10)]

    def tearDown(self) -> None:
        pass

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.seq = [x for x in range(10)]

    def tearDown(self) -> None:
        pass

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, [x for x in range(10)])
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    suite = unittest.TestSuite([testCase1, testCase2])
    filename = "D:\\test.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description', verbosity=2)

    # unittest.TextTestRunner(verbosity=2).run(suite)
    runner.run(suite)
    fp.close()