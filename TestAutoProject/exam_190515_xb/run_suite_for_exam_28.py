"""
使用运行器运行测试用例
"""
import unittest

from exam_28 import TestLogin

# 创建测试用例套件
suite = unittest.TestSuite()

# 添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))

# 使用运行器运行测试用例
unittest.TextTestRunner(verbosity=2).run(suite)