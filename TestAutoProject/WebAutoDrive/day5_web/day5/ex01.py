import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import unittest
from parameterized import parameterized

from day5_web.day5.tools.HTMLTestRunner import HTMLTestRunner

"""
1. 打开TPshop网站首页，完成以下操作：

用例一:
1. 点击‘登录’跳转到登录页面
2. 输入用户名、密码和万能验证码，点击登录按钮登录系统

用例二:
3. 重新打开首页，点击‘我的订单’进入后台管理页面
4. 选择‘账户设置’下的‘收货地址’选项
5. 点击地址管理下的‘增加新地址’按钮
6. 输入地址信息，收货地址选择‘上海市-市辖区-浦东新区-三林镇’，其他选项任意输入
7. 点击‘保存收货地址’按钮
8. 关闭当前窗口
要求：
    1. 采用UnitTest管理测试脚本，并生成测试报告
    2. 分成登录和新增收货地址两个用例
    3. 每执行一个操作暂停2秒，方便观看效果
    4. 在浏览器窗口最大化的状态下操作，设置隐式等待为30秒
    5. 在代码正常运行的情况下，实现测试数据的参数化
"""


def data_list1():
    d_list = [('18828828888', '123456', '8888')]
    return d_list


def data_list2():
    d_list = [("王五五", '123432', '18828828888')]
    return d_list


class TestTPShop(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     # driver = webdriver.Chrome()
    #     # driver.get("http://localshost")
    #     pass

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     pass
    @parameterized.expand(data_list1)
    def test_login(self, x, y, z):
        self.driver.find_element_by_css_selector(".red").click()
        self.driver.find_element_by_id("username").send_keys(x)
        self.driver.find_element_by_id("password").send_keys(y)
        self.driver.find_element_by_name("verify_code").send_keys(z)
        self.driver.find_element_by_name("sbtbutton").click()

    @parameterized.expand(data_list2)
    def test_change(self, x, y, z):
        # self.test_login()
        self.driver.add_cookie({"name": "uname", "value": "18828828888"})
        self.driver.add_cookie({"name": "user_id", "value": "2593"})
        self.driver.add_cookie({"name": "PHPSESSID", "value": "7vg9a3lkugv6mfs7cculo6q5v3"})
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//a[contains(text(), '我的订单')]").click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        element_tag = self.driver.find_element_by_xpath(
            "//span[contains(text(),'账户设置')]")
        ActionChains(self.driver).move_to_element(element_tag).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//a[contains(text(), '收货地址')]").click()
        self.driver.find_element_by_xpath(
            "//span[contains(text(), '增加新地址')]").click()
        self.driver.switch_to.frame("layui-layer-iframe100001")
        self.driver.find_element_by_name("consignee").send_keys(x)
        Select(self.driver.find_element_by_id(
            "province")).select_by_visible_text("上海市")
        Select(self.driver.find_element_by_id(
            "city")).select_by_visible_text("市辖区")
        Select(self.driver.find_element_by_id(
            "district")).select_by_visible_text("浦东新区")
        Select(self.driver.find_element_by_id(
            "twon")).select_by_visible_text("三林镇")
        self.driver.find_element_by_id("address").send_keys(y)
        self.driver.find_element_by_name("mobile").send_keys(z)
        self.driver.find_element_by_xpath(
            "//span[contains(text(), '保存收货地址')]").click()
        # self.driver.quit()
#
# if __name__ == '__main__':
# suite = unittest.TestSuite()
# # suite.addTest(unittest.makeSuite(TestTPShop))
# suite.addTest(TestTPShop("test_login"))
# suite.addTest(TestTPShop("test_change_add"))
# report_my = './report/{}.html'.format(time.strftime("%Y%m%d%H%M%S"))
# with open(report_my, 'wb') as f:
#     HTMLTestRunner(f, verbosity=2, title='testTPShop', description='window10x64 Chrome').run(suite)

if __name__ == '__main__':
    unittest.main()