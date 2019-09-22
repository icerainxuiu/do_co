import time
import unittest

from day5_web.day5.ex01 import TestTPShop
from day5_web.day5.tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(TestTPShop("test_login"))
suite.addTest(TestTPShop("test_change_add"))
# suite.addTest(unittest.makeSuite(TestTPShop))
report_my = './report/{}.html'.format(time.strftime("%Y%m%d%H%M%S"))
with open(report_my, 'wb') as f:
    HTMLTestRunner(f, verbosity=2, title='testTPShop', description='window10x64 Chrome').run(suite)