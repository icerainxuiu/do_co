
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from case.test_login import TestLogin
from data_base import BASE_PATH

# 创建suite套件
suite = unittest.TestSuite()
# 添加测试用例类
suite.addTest(unittest.makeSuite(TestLogin))
# print(BASE_PATH)
# 打开测试报告生成的文件流并写入HTML格式的测试报告
with open(BASE_PATH + "/report/{}test.html".format(time.strftime("%Y%m%d%H%M%S")), 'wb') as f:
    HTMLTestRunner(f, verbosity=2, title="test_login_api", description="win10x64").run(suite)