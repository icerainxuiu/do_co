# encoding=utf-8
import time
import unittest
# import HTML
# from unittest import TestCase

from selenium import webdriver


class GloryRoad(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_register(self):
        self.driver.get("http://localhost")
        time.sleep(3)
        self.driver.find_element_by_css_selector(".red").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(text(), '立即')]").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#username").send_keys("13012345678")
        self.driver.find_element_by_xpath("//input[@placeholder='图像验证码']").send_keys("8888")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("password2").send_keys("123456")
        self.driver.find_element_by_xpath("//a[contains(text(),'同意协议')]").click()
        time.sleep(2)

    def test_local(self):
        self.driver.get("http://localhost")
        time.sleep(3)
        self.driver.find_element_by_css_selector(".red").click()
        time.sleep(5)
        self.driver.find_element_by_css_selector("#username").send_keys("13012345678")
        time.sleep(3)
        self.driver.find_element_by_css_selector("#password").send_keys("123456")
        time.sleep(3)
        self.driver.find_element_by_css_selector("#verify_code").send_keys("8888")
        time.sleep(3)
        self.driver.find_element_by_css_selector(".J-login-submit").click()
        time.sleep(2)
        print(self.driver.title)


    def test_add_market(self):
        self.test_local()



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()