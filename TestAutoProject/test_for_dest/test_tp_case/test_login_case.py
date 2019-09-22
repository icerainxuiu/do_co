# 测试用例for 登录模块
import time
import unittest

from parameterized import parameterized

from page_object.page_object_login import LoginProxy
# 导入数据读取模块
from util.data_load_test_login import data_login
# 导入日志模板
from util.log_tp_test import logger
# 导入驱动类、获取登录失败弹框信息方法
from util.utils import DriverUtil, get_tips_msg


class TestLogin(unittest.TestCase):
    # 测试登录模块用例类开始前的操作
    # 创建浏览器驱动对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        # 创建登录业务实例对象
        cls.login = LoginProxy()

    # 测试用例类执行完成后关闭浏览器驱动
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    # 登录模块测试用例开始前的操作
    def setUp(self) -> None:
        self.driver.get('http://localhost')
        self.driver.find_element_by_class_name('red').click()

    # 测试用例执行后的操作
    def tearDown(self) -> None:
        time.sleep(2)

    # 测试用例及其数据化并断言
    @parameterized.expand(data_login())
    def test_login(self, username, password, verify_code, is_success, expect):
        self.login.login(username, password, verify_code)
        # 登录成功的断言
        if is_success:
            # 断言浏览器驱动获取的title是否是我的账户
            time.sleep(2)
            try:
                self.assertIn(expect, self.driver.title)
                logger.info('断言浏览器驱动获取的页面标题是否和预期一致')
            except Exception as e:
                self.driver.get_screenshot_as_file('../img_test/{}.png'.format(time.strftime("%Y%d%m%H%M%S")))
                logger.error("断言浏览器标题和预期失败")
                raise e
            time.sleep(2)
            self.driver.find_element_by_xpath("//a[contains(text(), '退出')]").click()
            logger.info('登录成功，并点击安全退出按钮')
        # 登录失败的断言
        else:
            # 断言提示消息是否和应该出现的一致
            # 调用工具类定义的获取提示消息方法
            time.sleep(1)
            msg = get_tips_msg()
            try:
                self.assertIn(expect, msg)
                logger.info('断言登录失败的弹窗消息是否和预期一致')
            except Exception as e:
                self.driver.get_screenshot_as_file('../img_test/{}.png'.format(time.strftime("%Y%d%m%H%M%S")))
                logger.error('断言登录失败弹窗消息与预期结果不一致')
                raise e

