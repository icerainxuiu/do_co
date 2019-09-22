import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from scripts.test_goods_cart_case import TestGoodsCart
from scripts.test_login_case import TestLogin
from scripts.test_order import TestOrder
from utils.utils import DriverUtil

# 设置测试用例套件实例对象
suite = unittest.TestSuite()
# 将浏览器驱动对象自动退出设置为False
DriverUtil().set_auto_quit(False)
# 将下订单里的登录帐号设置为False
TestOrder().set_login_flag(False)
# 添加测试登录测试用例
suite.addTest(unittest.makeSuite(TestLogin))
# 添加测试购物车测试用例
suite.addTest(unittest.makeSuite(TestGoodsCart))
# 添加测试下订单测试用例
suite.addTest(unittest.makeSuite(TestOrder))

# 使用TestLoader加载器加载指定目录下的测试用例文件
# unittest.TestLoader().discover("../scripts", pattern='test*.py')
# unittest.defaultTestLoader.discover('../scripts', pattern='test*.py')

# 打开生成报告文件，生成测试报告
with open('../report/{}.html'.format(time.strftime("%Y%m%d%H%M%S")), 'wb')as f:
    HTMLTestRunner(f, verbosity=2, title='test_tp_shop', description='win10x64').run(suite)

# 将下订单的登录帐号标志设置为True
TestOrder().set_login_flag(True)
# 将浏览器驱动自动关闭设置为True
DriverUtil().set_auto_quit(True)
# 退出浏览器驱动
DriverUtil().quit_driver()
