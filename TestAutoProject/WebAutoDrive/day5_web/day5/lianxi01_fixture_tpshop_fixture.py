import unittest

from selenium import webdriver


class TestFixtureTPShop(unittest.TestCase):

    # 初始化方法前的准备工作
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost")

    # 退出测试用例后的清理工作
    def tearDown(self) -> None:
        self.driver.quit()

    # 测试用例
    def test_tp_shop(self):
        self.driver.find_element_by_css_selector(".red").click()
        self.driver.find_element_by_id("username").send_keys("18828828888")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_name("sbtbutton").click()
        text = self.driver.find_element_by_xpath("//div[contains(text(),'验证码')]").text
        print("text:", text)
