import time
import unittest

from case.test_articles import TestArticles
from case.test_cacel import TestCancel
from case.test_channels import TestChannels
from case.test_collections import TestCollections
from case.test_login import TestLogin
from data_for_test import BASE_PATH
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestChannels))
suite.addTest(unittest.makeSuite(TestCollections))
suite.addTest(unittest.makeSuite(TestArticles))
suite.addTest(unittest.makeSuite(TestCancel))

with open(BASE_PATH + "/report/{}report.html".format(time.strftime("%Y%m%d%H%MS")), 'wb')as f:
    HTMLTestRunner(f, verbosity=2, title="test_dark_horse", description="win10x64").run(suite)