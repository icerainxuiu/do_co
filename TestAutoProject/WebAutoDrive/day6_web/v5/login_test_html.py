import time
import unittest

# from day5_web.day5.tools.HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner

from day5_web.day5.tools.HTMLTestRunner import HTMLTestRunner
from day6_web.v5.login_test_case import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(TestLogin('test01_login_no_username'))
# suite.addTest(TestLogin('test02_login_password_error'))
file_msg = './msg_html/{}.html'.format(time.strftime('%Y%m%d%H%M%S'))

with open(file_msg, 'wb') as f:
    HTMLTestRunner(f, verbosity=2, title='login_test', description='win10x64').run(suite)