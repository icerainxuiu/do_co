# 创建测试套件，并用测试套件生成html测试报告
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from test_tp_case.test_login_case import TestLogin


suite = unittest.TestSuite()

# 将测试用例添加至测试套件
suite.addTest(unittest.makeSuite(TestLogin))

with open("../test_html/{}.html".format(time.strftime("%Y%m%d%H%M%S")), 'wb') as f:
    # 创建测试报告驱动器
    HTMLTestRunner(f, verbosity=2, title="test_tp_login", description="win10-x64").run(suite)