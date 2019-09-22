
# 注册页面测试用例
import time
import unittest

from page_object.page_object_register import RegisterProxy
from util.utils import DriverUtil


class TestRegister(unittest.TestCase):
    # 初始化测试用例前的准备工作
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        # 实例化注册业务对象
        cls.proxy = RegisterProxy()

    # 退出测试用例的操作
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    # 测试用例执行前的回归原点
    def setUp(self) -> None:
        self.driver.get("http://localhost")

    def tearDown(self) -> None:
        time.sleep(2)