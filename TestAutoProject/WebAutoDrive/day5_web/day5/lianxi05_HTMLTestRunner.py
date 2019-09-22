# 1.实例化一个测试套件  suite
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from day5_web.day5.lianxi02_assert_tpshop_plus import TestLogin

suite = unittest.TestSuite()
# suite.addTest(TestLogin("test_login"))

suite.addTest(unittest.makeSuite(TestLogin))

# 2.向测试套件sutie添加测试用例
report_add = "./report/{}report.html".format(time.strftime("%Y%m%d%H%M%S"))

# 3.实例化一个运行器对象 runner =  HTMLTestRunner(stream,title,description)
with open(report_add, "wb") as f:
    # 4.运行器对象调用run(测试套件) runner.run(suite)
    run_suite = HTMLTestRunner(f, title="TPShop测试报告", verbosity=2, description="Chrome，win10x64")

    run_suite.run(suite)
